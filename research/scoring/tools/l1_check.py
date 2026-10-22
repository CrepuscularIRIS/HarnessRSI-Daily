"""Mechanical check for one L1 batch (PROBLEM_CORE §7, controller-only).

Usage: python3 research/scoring/tools/l1_check.py --run rsi-pilot-20261022-01 --batch p1
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
Q1 = {"measured", "asserted", "unknown"}
Q2 = {"challenges_barrier", "open_failure", "vertical_port", "settled", "unknown"}
Q3 = {"family", "multi_card", "single_card", "local"}
Q4 = {"fits", "partial", "misfit", "unknown"}
FAM = {"F0", "F1", "F2", "F3", "F4", "F5"}
TIERS = {"P0", "P1", "P2", "P3", "needs_material", "out_of_scope"}
MAT = {"abstract", "abstract_intro", "core", "full"}


def check(run: str, batch: str, l1_cap: bool = True) -> list[str]:
    errs = []
    bdir = REPO / "research/scoring/runs" / run / "batches"
    inputs = {json.loads(l)["paper_id"]: json.loads(l)
              for l in open(REPO / "research/scoring/runs" / run / "l1_inputs.jsonl")}
    want = [w.split("\t") for w in
            (bdir / f"{batch}-inputs.tsv").read_text().splitlines()[1:] if w.strip()]
    want_ids = [r[0] for r in want]
    got = {}
    for n, line in enumerate(open(bdir / f"{batch}.jsonl"), 1):
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"line {n}: invalid JSON ({e})")
            continue
        pid = d.get("paper_id")
        got[pid] = d
        for f in ("material", "problem_statement", "problem_source", "families", "cards",
                  "card_anchor", "q1_real", "q2_open", "q3_reach", "q4_fit", "tier",
                  "to_l2", "facts", "biggest_gap"):
            if f not in d:
                errs.append(f"line {n} ({pid}): missing {f}")
        if d.get("material") not in MAT:
            errs.append(f"{pid}: bad material")
        if d.get("problem_source") not in {"author_claimed", "card_supported"}:
            errs.append(f"{pid}: bad problem_source")
        fam = d.get("families") or []
        if not isinstance(fam, list) or not fam or not set(fam) <= FAM or len(fam) > 2 and fam != ["F0"]:
            errs.append(f"{pid}: bad families {fam}")
        if d.get("q1_real") not in Q1 or d.get("q2_open") not in Q2 or d.get("q3_reach") not in Q3 or d.get("q4_fit") not in Q4:
            errs.append(f"{pid}: bad Q enum")
        t = d.get("tier")
        if t not in TIERS:
            errs.append(f"{pid}: bad tier {t}")
        if l1_cap and t == "P3":
            errs.append(f"{pid}: P3 not allowed at L1")
        if t == "out_of_scope" or t == "needs_material":
            if d.get("to_l2"):
                errs.append(f"{pid}: {t} with to_l2=true")
        if not isinstance(d.get("facts"), list) or len(d.get("facts") or []) > 2:
            errs.append(f"{pid}: facts must be list of <=2")
        for f in d.get("facts") or []:
            if "loc" not in f or "fact" not in f:
                errs.append(f"{pid}: fact missing loc/fact")
        if t in ("P0", "P1", "P2") and d.get("problem_source") == "author_claimed" and t == "P2":
            pass  # asserted -> max P2 is allowed AT P2; kept as info only
    missing = set(want_ids) - set(got)
    extra = set(got) - set(want_ids)
    if missing:
        errs.append(f"missing: {sorted(missing)}")
    if extra:
        errs.append(f"extra: {sorted(extra)}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--no-l1-cap", action="store_true")
    args = ap.parse_args()
    errs = check(args.run, args.batch, l1_cap=not args.no_l1_cap)
    if errs:
        print(f"FAIL {args.batch}: {len(errs)} error(s)")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK {args.batch}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
