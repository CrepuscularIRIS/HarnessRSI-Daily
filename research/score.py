"""Validate judgment records (research/SCORE_SPEC.md) and compute HarnessRSI scores.

Quote verification needs research/fulltext/ (local only). Once a batch file has passed it, `build` records the file's
sha256 in research/judgments/VERIFIED.json; later builds re-check only structure for unchanged batches, so a fresh
clone without full texts can still publish. A changed or new batch is always quote-verified again.

Dual-model batches (since 2026-10-21): a batch judged by two blind models is stored as
`research/judgments/<batch>.<model>.jsonl` (one file per model in DUAL_MODELS). `build` quote-checks each file,
scores each independently, and the board row is the average; |Δtotal| > 10 or a band mismatch is written to
research/judgments/DUAL_FLAGS.md. A dual group sorts after any single batch of the same name (later wins).

Usage:
  python research/score.py check <judgments.jsonl> [<ids.txt>]   # validate only, exit 1 on problems
  python research/score.py build                                  # all research/judgments/*.jsonl → research/scores.jsonl
"""

import hashlib
import json
import re
import sys
from pathlib import Path

from check_evidence import KEYS as EV_KEYS, FULLTEXT, squash

R = Path("research")
EV_POINTS = {
    "held_out": {"yes": 10, "partial": 5}, "cross_task": {"yes": 8}, "variance": {"yes": 8},
    "budget_matched": {"yes": 8, "partial": 4}, "optimizer_cost": {"yes": 4, "partial": 2},
    "retained_ablation": {"yes": 6}, "improver_comparison": {"yes": 3}, "leakage_guard": {"tested": 3, "untested": 1},
}
LEVEL_POINTS = {"improver": 10, "retained": 6, "task": 2, "unclear": 0}
CODE_POINTS = {"yes": 10, "announced": 3}
assert sum(max(v.values()) for v in EV_POINTS.values()) == 50

DUAL_MODELS = ("opus", "sol")  # first = primary (descriptive fields); add a model here to widen the panel
DUAL_STEM = re.compile(r"^(.+)\.(opus|sol)$")  # "<batch>.<model>" — gpt-6.1-sol = sol, claude-opus-5-5 = opus


def jl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def context() -> tuple[dict, dict]:
    tax = json.loads((R / "patterns/taxonomy.json").read_text())
    parent = {s["id"]: s["parent"] for s in tax["sub_patterns"]}
    assign = {a["arxiv"]: a for a in jl(R / "patterns/assignments.jsonl")}
    main_of = {k: (a["sub_pattern"], parent[a["sub_pattern"]]) for k, a in assign.items()}
    return main_of, json.loads((R / "patterns/conditions.json").read_text())


def check(rec: dict, main_of: dict, cond: dict, verify_quotes: bool = True) -> list[str]:
    aid = rec.get("arxiv")
    if aid not in main_of:
        return [f"{aid}: not in assignments.jsonl"]
    path = FULLTEXT / f"{aid.replace(':', '_')}.txt"
    if verify_quotes and not path.exists():
        return [f"{aid}: no fulltext file"]
    hay = squash(path.read_text(encoding="utf-8")) if verify_quotes else None
    sub, main = main_of[aid]
    errs = []

    def quoted(label: str, item: dict, allowed: set, needs_quote: set) -> None:
        v, q = (item or {}).get("value"), (item or {}).get("quote")
        if v not in allowed:
            errs.append(f"{label}.value={v!r}")
        elif v in needs_quote:
            if not q or len(q.split()) > 45:
                errs.append(f"{label}: needs a quote ≤45 words")
            elif hay is not None and squash(q) not in hay:
                errs.append(f"{label}: quote not in file: {q[:50]!r}")

    for k in ("title_zh", "one_line", "one_line_zh"):
        if not isinstance(rec.get(k), str) or not rec[k].strip():
            errs.append(f"empty {k}")
    if len((rec.get("one_line") or "").split()) > 30:
        errs.append("one_line > 30 words")
    ev = rec.get("evidence") or {}
    for k, allowed in EV_KEYS.items():
        quoted(f"evidence.{k}", ev.get(k), allowed, allowed - {"unclear"})
    quoted("evidence_level", rec.get("evidence_level"), set(LEVEL_POINTS), {"task", "retained", "improver"})
    for part, key in (("success", "S"), ("failure", "F")):
        want = {c["id"] for c in cond[main][key]}
        got = rec.get(part) or {}
        if set(got) != want:
            errs.append(f"{part} ids {sorted(got)} != {sorted(want)} for {main}")
        for cid, item in got.items():
            quoted(f"{part}.{cid}", item, {"yes", "no", "unclear"}, {"yes"})
    ap = rec.get("ap1") or {}
    if ap.get("value") not in {"yes", "no"} or ap.get("mitigated") not in {"yes", "no", "unclear"}:
        errs.append("ap1 malformed")
    elif ap["value"] == "yes":
        quoted("ap1", {"value": "yes", "quote": ap.get("quote")}, {"yes"}, {"yes"})
    return [f"{aid}: {e}" for e in errs]


def code_url(quote: str) -> str | None:
    text = re.sub(r"(github|gitlab|huggingface)\s*\.\s*(com|co)\s*/\s*", r"\1.\2/", quote)  # PDF/HTML line-break artifacts
    m = re.search(r"https?://(?:www\.)?(?:github\.com|gitlab\.com|huggingface\.co)/[\w.\-]+/[\w.\-]+", text)
    return m.group(0).rstrip(".") if m else None


def code_sources() -> dict[str, dict]:
    """arXiv id -> {url, stars} from verified anchors, arXiv comments and HF Papers (first hit wins, in that order)."""
    out: dict[str, dict] = {}
    for w in json.loads(Path("keywords.json").read_text())["anchor_works"]:
        if w.get("arxiv") and w.get("code"):
            out[w["arxiv"]] = {"url": w["code"], "stars": None}
    for r in jl(R / "corpus.jsonl"):
        if r["arxiv"] not in out and (u := code_url(r.get("comment") or "")):
            out[r["arxiv"]] = {"url": u, "stars": None}
    hf = {h["arxiv"]: h for h in jl(R / "hf_meta.jsonl")} if (R / "hf_meta.jsonl").exists() else {}
    for aid, h in hf.items():
        if h.get("github"):
            out.setdefault(aid, {"url": h["github"], "stars": None})
            out[aid]["stars"] = h.get("stars")
    return out


def band(total: float) -> str:
    return "★★★" if total >= 70 else "★★" if total >= 50 else "★" if total >= 30 else "—"


def score(rec: dict, main: str, cond: dict, code_found: bool = False) -> dict:
    ev = rec["evidence"]
    evidence = sum(EV_POINTS.get(k, {}).get(ev[k]["value"], 0) for k in EV_POINTS)
    s, f = cond[main]["S"], cond[main]["F"]
    s_yes = sum(rec["success"][c["id"]]["value"] == "yes" for c in s)
    f_yes = sum(rec["failure"][c["id"]]["value"] == "yes" for c in f)
    execution = 20 * s_yes / len(s) + 10 * (1 - f_yes / len(f))
    if rec["ap1"]["value"] == "yes" and rec["ap1"]["mitigated"] != "yes":
        execution = max(0.0, execution - 5)
    level = LEVEL_POINTS[rec["evidence_level"]["value"]]
    code = 10 if code_found else CODE_POINTS.get(ev["code"]["value"], 0)
    total = round(evidence + execution + level + code)
    return {"evidence": evidence, "execution": round(execution, 1), "level": level, "code": code, "total": total,
            "band": band(total), "s_yes": s_yes, "s_n": len(s), "f_yes": f_yes, "f_n": len(f)}


def main(argv: list[str]) -> int:
    main_of, cond = context()
    if argv[:1] == ["check"]:
        recs = jl(Path(argv[1]))
        errs = [e for r in recs for e in check(r, main_of, cond)]
        if len(argv) > 2:
            want, got = set(Path(argv[2]).read_text().split()), [r.get("arxiv") for r in recs]
            if set(got) != want or len(got) != len(set(got)):
                errs.append(f"id mismatch: missing={sorted(want - set(got))[:8]} extra={sorted(set(got) - want)[:8]}")
        print("\n".join(errs) + ("\n" if errs else "") + f"{len(recs)} records, {len(errs)} problems")
        return 1 if errs else 0
    if argv[:1] == ["build"]:
        out, bad, flags, srcs = {}, 0, [], code_sources()
        ledger_path = R / "judgments/VERIFIED.json"
        ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}

        def publish(r: dict) -> None:
            sub, main = main_of[r["arxiv"]]
            url = code_url(r["evidence"]["code"].get("quote") or "") or srcs.get(r["arxiv"], {}).get("url")
            out[r["arxiv"]] = {"arxiv": r["arxiv"], "sub_pattern": sub, "main_pattern": main,
                               **{k: r[k] for k in ("title_zh", "one_line", "one_line_zh")},
                               "evidence_level": r["evidence_level"]["value"], "code": r["evidence"]["code"]["value"],
                               "code_url": url, "stars": srcs.get(r["arxiv"], {}).get("stars"),
                               **score(r, main, cond, code_found=bool(url))}

        # legacy batches (pilot, bNN) first, then dated batches in date order: a later re-judgment of a paper wins.
        # A dual group ("<batch>.<model>.jsonl" per model) sorts just after a same-named single batch.
        singles, groups = [], {}
        for p in (R / "judgments").glob("*.jsonl"):
            m = DUAL_STEM.match(p.stem)
            if m:
                groups.setdefault(m.group(1), {})[m.group(2)] = p
            else:
                singles.append(p)
        units = [((p.stem[:1].isdigit(), p.name), [p]) for p in singles]
        units += [((b[:1].isdigit(), b + "~"), [groups[b].get(m) for m in DUAL_MODELS]) for b in groups]
        for _, files in sorted(units, key=lambda u: u[0]):
            if None in files:  # dual group missing a model file — still being written
                print(f"skip {files[0].name.rsplit('.', 2)[0]}: dual group incomplete (need {'+'.join(DUAL_MODELS)})")
                bad += 1
                continue
            p0 = files[0]
            stem = DUAL_STEM.match(p0.stem)
            batch = stem.group(1) if stem else p0.stem
            ids_file = p0.with_name(f"ids_{batch}.txt")
            recs = {p: jl(p) for p in files}
            want = set(ids_file.read_text().split()) if ids_file.exists() else {r["arxiv"] for rs in recs.values() for r in rs}
            for p in files:
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                if {r["arxiv"] for r in recs[p]} != want or any(check(r, main_of, cond, verify_quotes=ledger.get(p.name) != digest) for r in recs[p]):
                    print(f"skip {p.name}: incomplete or invalid batch ({len(recs[p])}/{len(want)})")  # still being written
                    bad += 1
                    recs = {}
                    break
                ledger[p.name] = digest
            if not recs:
                continue
            if len(files) == 1:
                for r in recs[p0]:
                    publish(r)
                continue
            by = {p.name.rsplit(".", 2)[1]: {r["arxiv"]: r for r in recs[p]} for p in files}
            for aid in sorted(want):
                scored = {}
                for m in DUAL_MODELS:
                    r = by[m][aid]
                    url = code_url(r["evidence"]["code"].get("quote") or "") or srcs.get(aid, {}).get("url")
                    scored[m] = (score(r, main_of[aid][1], cond, code_found=bool(url)), r, url)
                mean = {k: round(sum(scored[m][0][k] for m in DUAL_MODELS) / len(DUAL_MODELS), 1)
                        for k in ("evidence", "execution", "level", "code")}
                total = round(sum(scored[m][0]["total"] for m in DUAL_MODELS) / len(DUAL_MODELS))
                r, url0 = scored[DUAL_MODELS[0]][1], scored[DUAL_MODELS[0]][2]
                sub, main = main_of[aid]
                out[aid] = {"arxiv": aid, "sub_pattern": sub, "main_pattern": main,
                            **{k: r[k] for k in ("title_zh", "one_line", "one_line_zh")},
                            "evidence_level": r["evidence_level"]["value"], "code": r["evidence"]["code"]["value"],
                            "code_url": url0 or next((u for _, _, u in scored.values() if u), None),
                            "stars": srcs.get(aid, {}).get("stars"), **mean, "total": total, "band": band(total),
                            "s_yes": scored[DUAL_MODELS[0]][0]["s_yes"], "s_n": scored[DUAL_MODELS[0]][0]["s_n"],
                            "f_yes": scored[DUAL_MODELS[0]][0]["f_yes"], "f_n": scored[DUAL_MODELS[0]][0]["f_n"]}
                totals = [scored[m][0]["total"] for m in DUAL_MODELS]
                if max(totals) - min(totals) > 10 or len({scored[m][0]["band"] for m in DUAL_MODELS}) > 1:
                    flags.append(f"{batch} {aid}: " + " ".join(f"{m}={scored[m][0]['total']}{scored[m][0]['band']}"
                                                               for m in DUAL_MODELS) + f" → avg {total}")
        (R / "scores.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out.values()))
        ledger_path.write_text(json.dumps(dict(sorted(ledger.items())), indent=1) + "\n")
        (R / "judgments/DUAL_FLAGS.md").write_text(
            "# Dual-model flags — regenerated by `score.py build`; do not edit by hand\n\n"
            "Papers whose blind judgments disagree by >10 points or by band. Review the paper, then re-judge it into a\n"
            "NEW dated dual batch (the later batch wins); the average stays on the board until then.\n\n"
            + ("\n".join(flags) + "\n" if flags else "(none)\n"))
        print(f"scored {len(out)} papers ({bad} batches skipped, {len(flags)} dual flags) → research/scores.jsonl")
        return 1 if bad else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
