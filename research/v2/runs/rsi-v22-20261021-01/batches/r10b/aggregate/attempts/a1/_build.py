"""Opus 5.5 aggregate a1 for batch r10b: assemble final records from both seat a1 records + Opus rulings.

Writes only into this directory. Seat records, materials, rubric, cards are read-only inputs.
Run: python3 research/v2/runs/rsi-v22-20261021-01/batches/r10b/aggregate/attempts/a1/_build.py
"""
import copy
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[8]
sys.path.insert(0, str(REPO / "research/v2/tools"))
import rv2  # noqa: E402

RUN = "rsi-v22-20261021-01"
BATCH = "r10b"
BDIR = REPO / "research/v2/runs" / RUN / "batches" / BATCH
MAT = REPO / "research/fulltext/review-runs" / RUN / "materials"
MANI = json.load(open(BDIR / "manifest.json"))
CONF = json.load(open(BDIR / "conflicts.json"))
MD = {p["paper_key"]: p for p in MANI["paper_details"]}
MODEL = "fable(claude-opus-5-5[1m])"
TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
FORMULA = "S=(15G+20M+20X+10Em+15Ec+10Eh+5Es+5Ecost)/4"


def seat(s, p):
    return json.load(open(BDIR / "seats" / s / "attempts/a1" / f"{p}.json"))


EV_KEYS = {"evidence_ids", "counterevidence_ids", "counterevidence"}


def prefix(obj, s):
    """Prefix bare seat evidence ids (E001) with 'sol:'/'son55:' anywhere under evidence-id keys."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in EV_KEYS and isinstance(v, list):
                out[k] = [f"{s}:{x}" if isinstance(x, str) and re.fullmatch(r"E\d+", x) else x for x in v]
            else:
                out[k] = prefix(v, s)
        return out
    if isinstance(obj, list):
        return [prefix(x, s) for x in obj]
    return obj


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


def opus_ev(p, oid, quote, locator, expl, kind="author_report"):
    mid, sha = f"{p}.txt", MD[p]["material"]["sha256"]
    raw = open(MAT / f"{p}.txt").read()
    if norm(quote) not in norm(raw):
        raise SystemExit(f"opus quote not found verbatim in {p}: {quote[:80]}")
    return {"evidence_id": f"opus:{oid}", "material_id": mid, "material_hash": sha, "sha256": sha,
            "locator": locator, "quote": quote, "support_explanation": expl, "kind": kind}


def R(status, rating, reason, ev=(), cev=(), scope=()):
    return {"status": status, "rating": rating, "reason": reason, "evidence_ids": list(ev),
            "counterevidence_ids": list(cev), "search_scope": list(scope)}


def res(field, sol_v, son_v, decision, final, reason, ev=(), impact="none"):
    return {"field_path": field, "sol_value": sol_v, "son55_value": son_v, "decision": decision,
            "final_value": final, "reason": reason, "evidence_ids": list(ev), "score_impact": impact}


def conflict(p, field):
    for c in CONF["conflicts"]:
        if c["paper_key"] == p:
            for f in c["fields"]:
                if f["field"] == field:
                    return f["sol"], f["son55"]
    raise KeyError((p, field))


def merge_exps(p, sol, son, rename, overrides, drop=()):
    """Union of both seats' expectations. rename[(seat,id)] -> new id (same id in both seats = same card
    condition => merged). overrides[id] -> dict of fields to set. drop: (seat,id) to omit."""
    out, seen = [], {}
    for s, rec in (("sol", sol), ("son55", son)):
        for e in rec["expectations"]:
            if (s, e["id"]) in drop:
                continue
            e2 = prefix(copy.deepcopy(e), s)
            e2["id"] = rename.get((s, e["id"]), e["id"])
            e2["origin"] = f"{s}:{e['id']}"
            if e2["id"] in seen:
                prev = out[seen[e2["id"]]]
                prev["origin"] += f"; {s}:{e['id']}"
                prev["evidence_ids"] = prev.get("evidence_ids", []) + e2.get("evidence_ids", [])
                continue
            seen[e2["id"]] = len(out)
            out.append(e2)
    for eid, ov in overrides.items():
        assert eid in seen, (p, eid)
        out[seen[eid]].update(ov)
    return out


def score_of(rec):
    sc = rv2.compute_score(rec)
    return {"raw": sc["raw"], "display": sc["display"], "lower": sc["lower"], "upper": sc["upper"],
            "coverage": sc["coverage"], "rubric_hash": MANI["rubric"]["sha256"], "formula": FORMULA}


def material_entry(p, extra_sections=()):
    m = MD[p]["material"]
    return {"material_id": f"{p}.txt", "url": m["source_url"], "version": MD[p]["version"], "sha256": m["sha256"],
            "local_path": m["text_path"],
            "sections_read": ["Opus: pinned text read before opening seat records (abstract, method, experiments, all tables, appendices; long proof derivations skimmed) "
                              "; targeted re-reads for every disputed field"] + list(extra_sections),
            "complete": True, "missing_sections": []}


# ---------------------------------------------------------------- per-paper specs
SPECS = {}
from _specs import build_specs  # noqa: E402  (kept separate to stay readable)

SPECS = build_specs(globals())


def assemble(p, sp):
    sol, son = seat("sol", p), seat("son55", p)
    base = sol if sp["base"] == "sol" else son
    bs = sp["base"]
    ev = prefix(copy.deepcopy(sol["evidence"]), "sol")
    for e in ev:
        e["evidence_id"] = "sol:" + e["evidence_id"]
    ev2 = prefix(copy.deepcopy(son["evidence"]), "son55")
    for e in ev2:
        e["evidence_id"] = "son55:" + e["evidence_id"]
    ev = ev + ev2 + sp.get("opus_evidence", [])
    paper = copy.deepcopy(base["paper"])
    paper.update(sp.get("paper_update", {}))
    rec = {
        "schema_version": "radar-review-v2.2", "run_id": RUN, "batch_id": BATCH, "attempt_id": "a1", "seat": "opus55",
        "paper": paper,
        "provenance": {
            "input_hash": MANI["input_hash"], "input_package": f"batches/{BATCH}/manifest.json",
            "rubric_version": "frozen v1.0 (calibration/rubric_frozen.md)", "rubric_hash": MANI["rubric"]["sha256"],
            "rs_manifest_hash": MANI["assets"]["rs_manifest"]["sha256"],
            "domain_cards_hash": MANI["assets"]["domain_cards_dir"]["sha256"],
            "expectations_hash": MANI["assets"]["domain_conditions"]["sha256"],
            "model_type": MODEL, "aggregate_model": MODEL, "actual_model": None, "session_id": None, "receipt_ref": None,
            "notes": "Opus aggregate seat via the configured claude-kimi type fable; no route probing. actual_model/"
                     "session_id/receipt_ref are null because the subagent runtime exposes no verifiable provider "
                     "receipt to this worker.",
            "seat_attempts": {"sol": "a1", "son55": "a1"}, "timestamp": TS},
        "materials": [material_entry(p)] + sp.get("extra_materials", []),
        "evidence": ev,
        "signatures": prefix(copy.deepcopy(base["signatures"]), bs),
        "gap": prefix(copy.deepcopy(base["gap"]), bs),
        "rs_pattern": sp["rs_pattern"],
        "domain_pattern": sp["domain_pattern"],
        "pattern_mapping": sp.get("pattern_mapping") or prefix(copy.deepcopy(base["pattern_mapping"]), bs),
        "expectations": sp["expectations"](sol, son),
        "claims": sp["claims"](prefix(copy.deepcopy(base["claims"]), bs)),
        "assessment": sp["assessment"],
        "ratings": sp["ratings"],
        "status": sp["status"], "reason": sp["reason"],
        "resolutions": sp["resolutions"],
        "shared_error_corrections": sp.get("shared_error_corrections", []),
        "aggregate_status": sp["aggregate_status"],
        "aggregate_review": sp["aggregate_review"],
        "input_seat_hashes": CONF["seat_record_hashes"][p],
    }
    rec["score"] = score_of(rec)
    rec["final_record_hash"] = rv2.record_hash(rec)
    return rec


def check(p, rec):
    errs = rv2.check_record(rec, rv2.card_ids())
    ids = {e["evidence_id"] for e in rec["evidence"]}
    for r in rec["resolutions"] + rec["shared_error_corrections"]:
        for e in r.get("evidence_ids", []):
            if e not in ids:
                errs.append(f"resolution cites missing {e}")
    for e in rec["expectations"]:
        for x in e.get("evidence_ids", []):
            if x not in ids:
                errs.append(f"expectation {e['id']} cites missing {x}")
        if not re.match(r"^(rs:[a-z_]+/RE-\d+|rsi:[a-z_]+/(S\d+|F\d+|H\d\d([.-]step\d+)?)|local:%s-\d+)$" % re.escape(p), e["id"]):
            errs.append(f"expectation id syntax: {e['id']}")
    fields = {f["field"] for c in CONF["conflicts"] if c["paper_key"] == p for f in c["fields"]}
    covered = [r["field_path"] for r in rec["resolutions"]]
    if set(covered) != fields or len(covered) != len(fields):
        errs.append(f"resolution coverage mismatch: missing={sorted(fields - set(covered))} extra={sorted(set(covered) - fields)}")
    for r in rec["resolutions"]:
        if r["decision"] not in ("sol", "son55", "revised", "unresolved", "same_supported_fact") or not r["reason"]:
            errs.append(f"bad resolution {r['field_path']}")
    return errs


def write_atomic(path, obj):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1))
    os.replace(tmp, path)


SEAT_QUOTE_NOTE = None


def seat_integrity():
    """Assert seat hashes/bindings; count seat quotes not found verbatim (reported, not fatal)."""
    global SEAT_QUOTE_NOTE
    missing = []
    for p in MANI["papers"]:
        raw = norm(open(MAT / f"{p}.txt").read())
        for s in ("sol", "son55"):
            r = seat(s, p)
            assert hashlib.sha256(rv2.canon(r).encode()).hexdigest() == CONF["seat_record_hashes"][p][s], (p, s)
            assert r["provenance"]["input_hash"] == MANI["input_hash"], (p, s)
            assert r["paper"]["version"] == MD[p]["version"], (p, s)
            assert all(m["sha256"] == MD[p]["material"]["sha256"] for m in r["materials"]), (p, s)
            for e in r["evidence"]:
                q = e.get("quote")
                if q and norm(q) not in raw:
                    missing.append(f"{s}:{p}:{e['evidence_id']}")
    SEAT_QUOTE_NOTE = ("all 10 seat records: seat hash, input_hash, version and material sha256 asserted; evidence quotes "
                       "checked verbatim (whitespace-normalised) against the pinned material; not found: "
                       + (", ".join(missing) if missing else "none"))
    print("seat quotes not found:", missing)


def main():
    seat_integrity()
    report_papers, all_ok = {}, True
    dist_total, n_conf, n_unres, n_sec = {}, 0, 0, 0
    for p in MANI["papers"]:
        rec = assemble(p, SPECS[p])
        errs = check(p, rec)
        if errs:
            all_ok = False
            print(p, "ERRORS", errs)
            continue
        write_atomic(HERE / f"{p}.final.json", rec)
        back = json.load(open(HERE / f"{p}.final.json"))
        assert rv2.record_hash(back) == back["final_record_hash"]
        dec = {}
        for r in rec["resolutions"]:
            dec[r["decision"]] = dec.get(r["decision"], 0) + 1
            dist_total[r["decision"]] = dist_total.get(r["decision"], 0) + 1
        unres = dec.get("unresolved", 0)
        n_conf += len(rec["resolutions"]); n_unres += unres; n_sec += len(rec["shared_error_corrections"])
        sol, son = seat("sol", p), seat("son55", p)
        report_papers[p] = {
            "status": rec["status"], "aggregate_status": rec["aggregate_status"],
            "score_raw": rec["score"]["raw"], "score_display": rec["score"]["display"],
            "score_lower": rec["score"]["lower"], "score_upper": rec["score"]["upper"],
            "seat_scores_raw": {"sol": (sol.get("score") or {}).get("raw"), "son55": (son.get("score") or {}).get("raw")},
            "conflicts": len(rec["resolutions"]), "decisions": dec, "unresolved": unres,
            "shared_error_corrections": len(rec["shared_error_corrections"]),
            "evidence_level": rec["assessment"]["evidence_level"], "claim_support": rec["assessment"]["claim_support"],
            "input_hash": MANI["input_hash"], "final_record_hash": rec["final_record_hash"],
            "a3_recommendation": SPECS[p].get("a3", "none"),
            "figure_dependence": SPECS[p].get("figure_dependence"),
        }
        print(p, rec["aggregate_status"], rec["score"]["raw"], dec)
    if not all_ok:
        raise SystemExit("not writing batch report: errors above")
    from _specs import batch_notes  # noqa: E402
    report = {
        "schema_version": "radar-review-v2.2", "run_id": RUN, "batch_id": BATCH, "attempt_id": "a1", "seat": "opus55",
        "model_type": MODEL, "aggregate_model": MODEL, "session_ref": None, "timestamp": TS,
        "rubric_hash": MANI["rubric"]["sha256"],
        "inputs": {"batch_manifest_input_hash": MANI["input_hash"], "overrides": {},
                   "seat_attempts": {"sol": "a1", "son55": "a1"}},
        "assigned": len(MANI["papers"]),
        "accepted_final": sum(1 for v in report_papers.values() if v["aggregate_status"] == "accepted_final"),
        "needs_revision": sum(1 for v in report_papers.values() if v["aggregate_status"] == "needs_revision"),
        "needs_evidence": sum(1 for v in report_papers.values() if v["aggregate_status"] == "needs_evidence"),
        "needs_fulltext": sum(1 for v in report_papers.values() if v["aggregate_status"] == "needs_fulltext"),
        "dispositions": {st: sum(1 for v in report_papers.values() if v["status"] == st) for st in ("reviewed", "out_of_scope", "needs_fulltext", "needs_evidence")},
        "scored": [p for p, v in report_papers.items() if v["score_raw"] is not None],
        "conflicts_total": n_conf, "decision_distribution_total": dist_total,
        "unresolved_total": n_unres, "shared_error_corrections_total": n_sec,
        "papers": report_papers,
        "validation": {
            "seat_hashes": "canonical SHA-256 of all 10 seat a1 records equals conflicts.json seat_record_hashes (asserted)",
            "seat_bindings": "both seats on manifest version + material sha256 for every paper; input_hash " + MANI["input_hash"][:8] + "…; rubric " + MANI["rubric"]["sha256"][:8] + "…",
            "resolution_coverage": "every conflicts.json field has exactly one resolution (asserted per paper)",
            "evidence_ids": "every id cited in ratings, resolutions and expectations exists in the record's evidence list (asserted)",
            "opus_quotes": "every Opus text quote found verbatim (whitespace-normalised) in the pinned material (asserted)",
            "seat_quotes": SEAT_QUOTE_NOTE,
            "score": FORMULA + "; weights sum 100, E weights sum 45; L=U=raw when no unknown",
            "final_record_hash": "sha256 of compact sort_keys ensure_ascii=False JSON without final_record_hash; re-verified after write",
            "structural": "rv2.check_record passes for all five records",
            "out_of_scope_rows": "score null, L=0, U=100, coverage 0; null is a disposition, not a zero-quality rating",
        },
        "notes": batch_notes(),
    }
    write_atomic(HERE / "batch-report.json", report)
    print("batch-report written", n_conf, dist_total, "unresolved", n_unres)


if __name__ == "__main__":
    main()
