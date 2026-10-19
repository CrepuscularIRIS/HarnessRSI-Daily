"""Validate judgment records (research/SCORE_SPEC.md) and compute HarnessRSI scores.

Quote verification needs research/fulltext/ (local only). Once a batch file has passed it, `build` records the file's
sha256 in research/judgments/VERIFIED.json; later builds re-check only structure for unchanged batches, so a fresh
clone without full texts can still publish. A changed or new batch is always quote-verified again.

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
    band = "★★★" if total >= 70 else "★★" if total >= 50 else "★" if total >= 30 else "—"
    return {"evidence": evidence, "execution": round(execution, 1), "level": level, "code": code, "total": total,
            "band": band, "s_yes": s_yes, "s_n": len(s), "f_yes": f_yes, "f_n": len(f)}


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
        out, bad, srcs = {}, 0, code_sources()
        ledger_path = R / "judgments/VERIFIED.json"
        ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
        # legacy batches (pilot, bNN) first, then dated batches in date order: a later re-judgment of a paper wins
        for p in sorted((R / "judgments").glob("*.jsonl"), key=lambda p: (p.stem[:1].isdigit(), p.name)):
            recs, ids_file = jl(p), p.with_name(f"ids_{p.stem}.txt")
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            verified = ledger.get(p.name) == digest
            want = set(ids_file.read_text().split()) if ids_file.exists() else {r["arxiv"] for r in recs}
            if {r["arxiv"] for r in recs} != want or any(check(r, main_of, cond, verify_quotes=not verified) for r in recs):
                print(f"skip {p.name}: incomplete or invalid batch ({len(recs)}/{len(want)})")  # still being written
                bad += 1
                continue
            ledger[p.name] = digest
            for r in recs:
                sub, main = main_of[r["arxiv"]]
                url = code_url(r["evidence"]["code"].get("quote") or "") or srcs.get(r["arxiv"], {}).get("url")
                out[r["arxiv"]] = ({"arxiv": r["arxiv"], "sub_pattern": sub, "main_pattern": main,
                            **{k: r[k] for k in ("title_zh", "one_line", "one_line_zh")},
                            "evidence_level": r["evidence_level"]["value"], "code": r["evidence"]["code"]["value"],
                            "code_url": url, "stars": srcs.get(r["arxiv"], {}).get("stars"),
                            **score(r, main, cond, code_found=bool(url))})
        (R / "scores.jsonl").write_text("".join(json.dumps(o, ensure_ascii=False) + "\n" for o in out.values()))
        ledger_path.write_text(json.dumps(dict(sorted(ledger.items())), indent=1) + "\n")
        print(f"scored {len(out)} papers ({bad} batches skipped) → research/scores.jsonl")
        return 1 if bad else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
