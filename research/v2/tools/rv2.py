"""Deterministic structure/arithmetic checks and conflict diff for v2.2 review runs.

Mechanical only: schema shape, ID coverage, hash binding, rating states, score arithmetic,
seat-vs-seat field diff, aggregate resolution coverage. Semantic quality stays with the two
seats and the Opus aggregate (docs/agents/JUDGE_BATCH.md, AGGREGATE_OPUS.md).

CLI:
  python3 research/v2/tools/rv2.py seats      --run R --batch B   # validate both seat attempts, write conflicts.json
  python3 research/v2/tools/rv2.py aggregate  --run R --batch B   # validate aggregate attempt
  python3 research/v2/tools/rv2.py score      --rec file.json     # recompute + print score
"""

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
WEIGHTS = {"G": 15, "M": 20, "X": 20,
           "E.measurement": 10, "E.causality": 15, "E.holdout": 10, "E.statistics": 5, "E.cost": 5}
RATING_KEYS = ["G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost"]
RATING_STATUS = {"resolved", "unknown", "not_reported"}


def normalize_record(rec: dict) -> dict:
    """Deterministic read-time normalization of known seat shape variances.
    Files are never modified; aggregates must write canonical shapes."""
    import copy
    r = copy.deepcopy(rec)
    # ratings: flatten a nested E group into E.<sub> items
    rt = r.get("ratings")
    if isinstance(rt, dict) and isinstance(rt.get("E"), dict) and "measurement" in rt["E"]:
        for k, v in rt["E"].items():
            rt.setdefault(f"E.{k}", v)
        del rt["E"]
    # status given as {value, reason}
    if isinstance(r.get("status"), dict):
        r["status_reason"] = r["status"].get("reason")
        r["status"] = r["status"].get("value")
    # domain matches: main_id/sub_id aliases + rsi:/rs: prefixes
    def norm_id(v):
        if isinstance(v, str):
            for pre in ("rsi:", "rs:"):
                if v.startswith(pre):
                    return v[len(pre):]
        return v
    dom = r.get("domain_pattern")
    if isinstance(dom, dict):
        for m in dom.get("matches", []) or []:
            if "main" not in m and "main_id" in m:
                m["main"] = m.pop("main_id")
            if "sub" not in m and "sub_id" in m:
                m["sub"] = m.pop("sub_id")
            m["main"] = norm_id(m.get("main"))
            if m.get("sub") is not None:
                m["sub"] = norm_id(m["sub"])
    rsp = r.get("rs_pattern")
    if isinstance(rsp, dict):
        for m in rsp.get("matches", []) or []:
            if m.get("sub_id") is not None:
                m["sub_id"] = norm_id(m["sub_id"])
    a = r.get("assessment")
    if isinstance(a, dict) and a.get("evidence_level") == "none":
        a["evidence_level"] = None  # "no measurements at all" == not assignable, not a level
    sc = r.get("score")
    if isinstance(sc, dict):
        for k in ("raw", "display", "lower", "upper", "coverage"):
            v = sc.get(k)
            if isinstance(v, str):
                try:
                    sc[k] = float(v)
                except ValueError:
                    pass
    return r


def canon(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def record_hash(rec: dict) -> str:
    r = {k: v for k, v in rec.items() if k != "final_record_hash"}
    return hashlib.sha256(canon(r).encode("utf-8")).hexdigest()


def card_ids():
    ref = REPO / "research/reference/researchstudio-15-31"
    mains, subs = set(), {}
    for row in csv.DictReader(open(ref / "MANIFEST.tsv"), delimiter="\t"):
        p = row["path"]
        if p.startswith("ideation-patterns/") and p.endswith(".md") and "overview" not in p:
            mains.add(Path(p).stem)
        elif p.startswith("ideation-sub-patterns/") and p.endswith(".md") and "overview" not in p:
            subs[Path(p).stem] = None
    for row in csv.DictReader(open(ref / "PARENTS.tsv"), delimiter="\t"):
        if row["sub_id"] in subs:
            subs[row["sub_id"]] = row["parent_id"]
    tax = json.load(open(REPO / "research/patterns/taxonomy.json"))
    dmains = {m["id"] for m in tax["main_patterns"]}
    dsubs = {s["id"] for s in tax["sub_patterns"]}
    return mains, subs, dmains, dsubs


def compute_score(rec_raw: dict) -> dict:
    """Deterministic per SCORE_SPEC: S=(Σw·r)/4; unknown → raw/display null + L/U bounds."""
    rec = normalize_record(rec_raw)
    ratings = rec.get("ratings", {})
    unknown, judged_w, total_l, total_u, total = [], 0, 0, 0, 0.0
    for k in RATING_KEYS:
        item = ratings.get(k) or {}
        w = WEIGHTS[k]
        if item.get("status") == "unknown" or item.get("rating") is None:
            unknown.append(k)
            continue
        r = item.get("rating")
        judged_w += w
        total += w * r
        total_l += w * r
    total_u = total  # upper = judged contributions at their ratings + unknown items at 4
    for k in unknown:
        total_u += WEIGHTS[k] * 4
    raw = None if unknown else total / 4
    return {
        "raw": raw,
        "display": None if raw is None else round(raw + 1e-9, 1),
        "lower": total_l / 4, "upper": total_u / 4,
        "coverage": judged_w / 100,
        "unknown": unknown,
    }


def check_record(rec_raw: dict, ids) -> list:
    """Structural checks shared by seat and aggregate records. ids=(rs_mains, rs_subs, d_mains, d_subs)."""
    rec = normalize_record(rec_raw)
    rs_mains, rs_subs, d_mains, d_subs = ids
    errs = []
    def fld_of(field):
        return rec.get(field, (rec.get("provenance") or {}).get(field))
    paper = rec.get("paper") or {}
    oos = rec.get("status") == "out_of_scope"
    for f in ("paper_key", "paper_id", "version"):
        if not paper.get(f):
            errs.append(f"paper.{f} missing")
    if not oos:
        for f in ("claim_type", "central_claim"):
            if not paper.get(f):
                errs.append(f"paper.{f} missing")
        if paper.get("claim_type") not in ("system_method", "component_training", "evaluation_resource"):
            errs.append("paper.claim_type invalid")
    prov = rec.get("provenance") or {}
    for fld in ("schema_version", "run_id", "batch_id", "attempt_id", "seat", "input_hash", "rubric_hash"):
        if not fld_of(fld):
            errs.append(f"{fld} missing (top-level or provenance)")
    if fld_of("schema_version") != "radar-review-v2.2":
        errs.append("schema_version != radar-review-v2.2")
    seat = fld_of("seat")
    if seat not in ("sol", "son55", "opus55"):
        errs.append("provenance.seat invalid")
    ev_ids = {e.get("evidence_id") for e in rec.get("evidence", [])}
    if None in ev_ids:
        errs.append("evidence[] has records without evidence_id")
    ev_ids.discard(None)

    def need_ev(eids, where):
        for e in eids or []:
            if e not in ev_ids:
                errs.append(f"{where}: evidence_id {e} not in evidence[]")

    # ratings
    if set(rec.get("ratings") or {}) != set(RATING_KEYS):
        errs.append("ratings keys != the 8 fixed items")
    for k, item in (rec.get("ratings") or {}).items():
        st = item.get("status")
        if st not in RATING_STATUS:
            errs.append(f"ratings.{k}.status '{st}' invalid")
            continue
        r = item.get("rating")
        if st == "resolved" and (not isinstance(r, int) or r not in range(5)):
            errs.append(f"ratings.{k} resolved but rating invalid: {r}")
        if st == "unknown" and r is not None:
            errs.append(f"ratings.{k} unknown but rating not null")
        if st == "not_reported":
            if r != 0:
                errs.append(f"ratings.{k} not_reported must be rating 0")
            if not item.get("search_scope"):
                errs.append(f"ratings.{k} not_reported needs search_scope")
        if st == "resolved" and not item.get("reason"):
            errs.append(f"ratings.{k} resolved needs reason")
        need_ev(item.get("evidence_ids"), f"ratings.{k}")
    # patterns (full identification required only for reviewed records)
    rsp = rec.get("rs_pattern") or {}
    outside = bool(rsp.get("outside_taxonomy"))
    primary = rsp.get("primary")
    shallow = rec.get("status") in ("out_of_scope", "needs_fulltext")
    if outside and (primary or rsp.get("supporting") or rsp.get("matches")):
        errs.append("rs_pattern: outside_taxonomy with matches")
    if not shallow and not outside and primary not in rs_mains:
        errs.append(f"rs_pattern.primary invalid: {primary}")
    if shallow and not rsp.get("matches") and not outside:
        pass  # identification not required for out_of_scope/needs_fulltext records
    for m in rsp.get("matches", []):
        mid, sid = m.get("main_id"), m.get("sub_id")
        if mid not in rs_mains:
            errs.append(f"rs match main_id invalid: {mid}")
        if sid is not None:
            if sid not in rs_subs:
                errs.append(f"rs match sub_id invalid: {sid}")
            elif rs_subs[sid] != mid:
                errs.append(f"rs match sub {sid} not under parent {mid}")
        if not m.get("evidence_ids"):
            errs.append("rs match needs evidence_ids")
    if len(rsp.get("supporting") or []) > 2:
        errs.append("rs_pattern.supporting > 2")
    if not shallow and not outside and not rsp.get("matches"):
        errs.append("rs_pattern: no matches and not outside_taxonomy")
    dom = rec.get("domain_pattern") or {}
    if not shallow and dom.get("namespace") != "rsi":
        errs.append("domain_pattern.namespace != rsi")
    for m in dom.get("matches", []):
        if m.get("main") not in d_mains:
            errs.append(f"domain match main invalid: {m.get('main')}")
        if m.get("sub") is not None and m.get("sub") not in d_subs:
            errs.append(f"domain match sub invalid: {m.get('sub')}")
    # assessment / score / status
    a = rec.get("assessment") or {}
    if a.get("evidence_level") not in ("task", "retained", "improver", "not_applicable", None,
                                       *(["not_assessed"] if oos else [])):
        errs.append(f"assessment.evidence_level invalid: {a.get('evidence_level')}")
    if a.get("claim_support") not in ("supported", "scoped", "unsupported", "contradicted", "unresolved", None,
                                      *(["not_assessed"] if oos else [])):
        errs.append(f"assessment.claim_support invalid: {a.get('claim_support')}")
    st = rec.get("status")
    if st not in ("reviewed", "needs_fulltext", "needs_evidence", "out_of_scope"):
        errs.append(f"status invalid: {st}")
    if st != "reviewed" and (rec.get("score") or {}).get("raw") is not None:
        errs.append("non-reviewed record must not carry a raw score")
    # score arithmetic if present and complete
    sc = rec.get("score")
    if st == "reviewed" and isinstance(sc, dict):
        want = compute_score(rec)
        if want["raw"] is not None:
            if sc.get("raw") is None or abs(sc["raw"] - want["raw"]) > 1e-6:
                errs.append(f"score.raw mismatch: record={sc.get('raw')} recomputed={want['raw']}")
            if sc.get("display") is None or abs(sc["display"] - want["display"]) > 0.10001:
                errs.append(f"score.display mismatch: {sc.get('display')} vs {want['display']}")
        else:
            if sc.get("raw") is not None:
                errs.append("score.raw present but unknown items remain")
        if abs((sc.get("coverage") or 0) - want["coverage"]) > 1e-6:
            errs.append(f"score.coverage mismatch: {sc.get('coverage')} vs {want['coverage']}")
        if st == "reviewed":
            for bound in ("lower", "upper"):
                if sc.get(bound) is not None and abs(sc[bound] - want[bound]) > 1e-6:
                    errs.append(f"score.{bound} mismatch: {sc.get(bound)} vs {want[bound]}")
    return errs


# ---------- seat validation + conflicts ----------

def diff_pair(sol_raw: dict, son_raw: dict) -> list:
    """Mechanical field-level diff; ALL differences are listed, Opus decides substance."""
    sol, son = normalize_record(sol_raw), normalize_record(son_raw)
    out = []

    def add(field, a, b):
        out.append({"field": field, "sol": a, "son55": b})

    ps, pn = sol.get("paper", {}), son.get("paper", {})
    if ps.get("claim_type") != pn.get("claim_type"):
        add("paper.claim_type", ps.get("claim_type"), pn.get("claim_type"))
    for f in ("evidence_level", "claim_support"):
        a, b = (sol.get("assessment") or {}).get(f), (son.get("assessment") or {}).get(f)
        if a != b:
            add(f"assessment.{f}", a, b)
    rs_a, rs_b = sol.get("rs_pattern") or {}, son.get("rs_pattern") or {}
    if rs_a.get("primary") != rs_b.get("primary"):
        add("rs_pattern.primary", rs_a.get("primary"), rs_b.get("primary"))
    ma = sorted((m.get("main_id"), m.get("sub_id")) for m in rs_a.get("matches", []))
    mb = sorted((m.get("main_id"), m.get("sub_id")) for m in rs_b.get("matches", []))
    if ma != mb:
        add("rs_pattern.matches", ma, mb)
    da = sorted((m.get("main"), m.get("sub")) for m in (sol.get("domain_pattern") or {}).get("matches", []))
    db = sorted((m.get("main"), m.get("sub")) for m in (son.get("domain_pattern") or {}).get("matches", []))
    if da != db:
        add("domain_pattern.matches", da, db)
    ea = {e.get("id"): e.get("status") for e in sol.get("expectations", [])}
    eb = {e.get("id"): e.get("status") for e in son.get("expectations", [])}
    for k in sorted(set(ea) | set(eb)):
        if ea.get(k) != eb.get(k):
            add(f"expectations[{k}].status", ea.get(k), eb.get(k))
    for k in RATING_KEYS:
        a = sol.get("ratings", {}).get(k) or {}
        b = son.get("ratings", {}).get(k) or {}
        if a.get("status") != b.get("status") or a.get("rating") != b.get("rating"):
            add(f"ratings.{k}", {"status": a.get("status"), "rating": a.get("rating")},
                {"status": b.get("status"), "rating": b.get("rating")})
    if sol.get("status") != son.get("status"):
        add("status", sol.get("status"), son.get("status"))
    return out


def cmd_seats(run: str, batch: str) -> int:
    bdir = REPO / "research/v2/runs" / run / "batches" / batch
    mani = json.load(open(bdir / "manifest.json"))
    ids = mani["papers"]
    ids_obj = card_ids()
    ovr = json.load(open(bdir / "overrides.json")) if (bdir / "overrides.json").exists() else {}
    result = {"batch": batch, "papers": ids, "seat_errors": {}, "overrides": ovr, "conflicts": []}
    ok = True
    recs = {}
    for seat in ("sol", "son55"):
        seat_errs = {}
        for pid in ids:
            ov = ovr.get(pid, {})
            sa = ov.get("seat_attempt")
            attempt = (sa.get(seat) if isinstance(sa, dict) else sa) or mani["seats"][seat]["attempt"]
            want_hash = ov.get("input_hash") or mani["input_hash"]
            sdir = bdir / "seats" / seat / "attempts" / attempt
            f = sdir / f"{pid}.json"
            if not f.exists():
                ok = False
                seat_errs[pid] = [f"missing record in attempt {attempt}"]
                continue
            rec = json.load(open(f))
            recs.setdefault(pid, {})[seat] = rec
            errs = check_record(rec, ids_obj)
            if rec.get("provenance", {}).get("input_hash") != want_hash:
                errs.append(f"provenance.input_hash != pinned package hash ({want_hash[:12]}) for attempt {attempt}")
            if errs:
                ok = False
                seat_errs[pid] = errs
        if seat_errs:
            result["seat_errors"][seat] = seat_errs
    for seat in ("sol", "son55"):
        attempt = mani["seats"][seat]["attempt"]
        sdir = bdir / "seats" / seat / "attempts" / attempt
        have = sorted(p.stem for p in sdir.glob("*.json") if p.name != "batch-report.json")
        expect = sorted(p for p in ids if ovr.get(p, {}).get("seat_attempt", attempt) == attempt)
        stale = [p for p in have if p not in expect]  # superseded files may remain on disk
        if have != expect and stale != [p for p in have if p in ovr]:
            pass  # extra superseded files in the old attempt dir are retained by contract
    for pid in ids:
        pair = recs.get(pid, {})
        if "sol" in pair and "son55" in pair:
            hs = {s: hashlib.sha256(canon(pair[s]).encode()).hexdigest() for s in pair}
            result.setdefault("seat_record_hashes", {})[pid] = hs
            result["conflicts"].append({"paper_key": pid, "fields": diff_pair(pair["sol"], pair["son55"])})
    result["ok"] = ok
    out = bdir / "conflicts.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1))
    n_conf = sum(len(c["fields"]) for c in result["conflicts"])
    print(json.dumps({"ok": ok, "papers": len(ids), "conflict_fields": n_conf,
                      "seat_errors": bool(result["seat_errors"]), "wrote": str(out.relative_to(REPO))}))
    return 0 if ok else 1


# ---------- aggregate validation ----------

def cmd_aggregate(run: str, batch: str) -> int:
    bdir = REPO / "research/v2/runs" / run / "batches" / batch
    mani = json.load(open(bdir / "manifest.json"))
    conf = json.load(open(bdir / "conflicts.json"))
    ovr = json.load(open(bdir / "overrides.json")) if (bdir / "overrides.json").exists() else {}
    default_attempt = mani["aggregate"]["attempt"]
    adir = bdir / "aggregate" / "attempts" / default_attempt
    ids = mani["papers"]
    ids_obj = card_ids()
    errs, report = {}, {"batch": batch, "papers": {}, "ok": True}
    n_unresolved = 0
    for pid in ids:
        f = bdir / "aggregate" / "attempts" / (ovr.get(pid, {}).get("aggregate_attempt") or default_attempt) / f"{pid}.final.json"
        if not f.exists():
            report["ok"] = False
            report["papers"][pid] = "missing final file"
            continue
        rec = json.load(open(f))
        e = check_record(rec, ids_obj)
        prov = rec.get("provenance", {})
        seat_now = rec.get("seat", prov.get("seat"))
        if seat_now != "opus55":
            e.append("aggregate seat != opus55 (top-level or provenance)")
        if set((rec.get("input_seat_hashes") or {}).keys()) != {"sol", "son55"}:
            e.append("input_seat_hashes must include both seats")
        else:
            want = (conf.get("seat_record_hashes") or {}).get(pid, {})
            for s in ("sol", "son55"):
                if want and rec["input_seat_hashes"][s] != want[s]:
                    e.append(f"input_seat_hashes[{s}] != controller-computed seat hash")
        if rec.get("final_record_hash") != record_hash(rec):
            e.append("final_record_hash mismatch")
        # every mechanical conflict must be addressed by a resolution (decision != unresolved)
        fields = next((c["fields"] for c in conf["conflicts"] if c["paper_key"] == pid), [])
        field_paths = {f["field"] for f in fields}
        res = rec.get("resolutions") or []
        covered = {r.get("field_path") for r in res if r.get("decision") not in (None, "unresolved")}
        missing = field_paths - covered
        if missing:
            e.append(f"conflict fields without resolution: {sorted(missing)[:8]}")
        rec_unresolved = sum(1 for r in res if r.get("decision") == "unresolved")
        n_unresolved += rec_unresolved
        if rec.get("aggregate_status") not in ("accepted_final", "needs_revision", "needs_evidence", "needs_fulltext"):
            e.append("aggregate_status invalid")
        if rec.get("aggregate_status") == "accepted_final" and rec_unresolved:
            e.append("accepted_final with unresolved resolutions")
        if rec.get("aggregate_status") == "accepted_final" and rec.get("status") == "reviewed" and rec.get("score", {}).get("raw") is None:
            e.append("accepted_final reviewed but score.raw null (unknown ratings remain)")
        if e:
            report["ok"] = False
            errs[pid] = e
        report["papers"][pid] = {"aggregate_status": rec.get("aggregate_status"),
                                 "record_status": rec.get("status"),
                                 "score_raw": (rec.get("score") or {}).get("raw"),
                                 "n_resolutions": len(res), "errors": e}
    report["aggregate_errors"] = errs
    report["unresolved_total"] = n_unresolved
    (adir / "validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))
    print(json.dumps({"ok": report["ok"], "papers": len(ids), "unresolved": n_unresolved,
                      "n_err_papers": len(errs)}))
    return 0 if report["ok"] else 1


def cmd_score(rec_path: str) -> int:
    rec = json.load(open(rec_path))
    print(json.dumps(compute_score(rec), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["seats", "aggregate", "score"])
    ap.add_argument("--run"), ap.add_argument("--batch"), ap.add_argument("--rec")
    a = ap.parse_args()
    if a.cmd == "seats":
        sys.exit(cmd_seats(a.run, a.batch))
    if a.cmd == "aggregate":
        sys.exit(cmd_aggregate(a.run, a.batch))
    sys.exit(cmd_score(a.rec))
