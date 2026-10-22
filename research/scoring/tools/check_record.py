"""Mechanical check for problem-core-v1.1 L1/L2 records (controller-only).

Usage: python3 research/scoring/tools/check_record.py --run rsi-pilot-20261022-02 --batch p1 [--stage L1|L2]

Structure pass is not scientific validation (PROBLEM_CORE §8).
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
Q1 = {"measured_own", "measured_cited_checked", "measured_cited_unchecked",
      "proof", "counterexample", "constraint_conflict", "asserted", "unknown"}
Q2 = {"challenges_barrier", "open_failure", "new_bottleneck", "vertical_port", "prior_solved", "unknown"}
Q3 = {"capability", "judgment", "incremental", "local"}
Q4 = {"fits", "partial", "misfit", "unknown"}
TIER = {"P0", "P1", "P2", "P3"}
EV = {"confirmed", "pending_method", "pending_experiment", "pending_material"}
PRIO = {"high", "medium", "low", "none"}
ACT = {"to_l2", "to_l3", "park", "exclude"}
STAT = {"assessed", "needs_material", "out_of_scope"}
VERD = {"holds", "partial", "fails", "unknown", "NA", "challenged_with_evidence"}
REQ = ("paper_id", "stage", "supersedes", "status", "material", "problem_statement",
       "problem_source", "families", "cards", "card_anchor", "q1_basis", "q2_open",
       "q3_change", "q3_loss", "q4_fit", "problem_tier", "evidence_status",
       "priority", "next_action", "subcard_checks", "facts", "biggest_gap", "audit_sample")


def tier_num(t):
    return int(t[1]) if t in TIER else None


def check(run: str, batch: str, stage: str) -> list[str]:
    errs = []
    bdir = REPO / "research/scoring/runs" / run / "batches"
    want = [w.split("\t")[0] for w in
            (bdir / f"{batch}-inputs.tsv").read_text().splitlines()[1:] if w.strip()]
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
        if pid in got:
            errs.append(f"line {n}: duplicate {pid}")
        got[pid] = d
        for f in REQ:
            if f not in d:
                errs.append(f"line {n} ({pid}): missing {f}")
        if d.get("stage") != stage:
            errs.append(f"{pid}: stage != {stage}")
        if d.get("status") not in STAT:
            errs.append(f"{pid}: bad status")
        if d.get("problem_source") not in {"author_claimed", "card_supported"}:
            errs.append(f"{pid}: bad problem_source")
        fam = d.get("families") or []
        if not fam or not set(fam) <= {"F0", "F1", "F2", "F3", "F4", "F5"} or len(fam) > 2:
            errs.append(f"{pid}: bad families {fam}")
        if d.get("q1_basis") not in Q1:
            errs.append(f"{pid}: bad q1_basis")
        if d.get("q2_open") not in Q2:
            errs.append(f"{pid}: bad q2_open")
        if d.get("q2_open") == "prior_solved" and not d.get("q2_prior"):
            errs.append(f"{pid}: prior_solved without q2_prior")
        if d.get("q3_change") not in Q3:
            errs.append(f"{pid}: bad q3_change")
        if d.get("q4_fit") not in Q4:
            errs.append(f"{pid}: bad q4_fit")
        t = d.get("problem_tier")
        if t is not None and t not in TIER:
            errs.append(f"{pid}: bad problem_tier {t}")
        if d.get("evidence_status") not in EV or d.get("priority") not in PRIO or d.get("next_action") not in ACT:
            errs.append(f"{pid}: bad evidence_status/priority/next_action")
        # caps (§4)
        if t:
            if d.get("q1_basis") in {"asserted", "measured_cited_unchecked"} and tier_num(t) > 2:
                errs.append(f"{pid}: {d['q1_basis']} caps tier at P2, got {t}")
            if d.get("q2_open") == "vertical_port" and tier_num(t) > 1:
                errs.append(f"{pid}: vertical_port caps tier at P1, got {t}")
            if d.get("q4_fit") == "misfit" and tier_num(t) > 1:
                errs.append(f"{pid}: misfit caps tier at P1, got {t}")
            if t == "P3":
                if d.get("q1_basis") in {"asserted", "unknown", "measured_cited_unchecked"}:
                    errs.append(f"{pid}: P3 without qualifying q1_basis")
                if d.get("q2_open") not in {"challenges_barrier", "open_failure", "new_bottleneck"}:
                    errs.append(f"{pid}: P3 with q2_open={d.get('q2_open')}")
                if d.get("q3_change") not in {"capability", "judgment"}:
                    errs.append(f"{pid}: P3 with q3_change={d.get('q3_change')}")
        if d.get("status") == "needs_material" and t is not None and d.get("evidence_status") not in {"pending_material"}:
            # needs_material with a tier is allowed if partial judgement possible; flag only if marked pending elsewhere
            pass
        if d.get("status") == "out_of_scope" and d.get("next_action") != "exclude":
            errs.append(f"{pid}: out_of_scope must have next_action=exclude (tier may be recorded informationally)")
        if not isinstance(d.get("facts"), list) or len(d.get("facts") or []) > 2:
            errs.append(f"{pid}: facts must be <=2")
        for f in d.get("facts") or []:
            if "loc" not in f or "fact" not in f:
                errs.append(f"{pid}: fact missing loc/fact")
        if stage == "L1":
            if d.get("subcard_checks") != []:
                errs.append(f"{pid}: L1 must have empty subcard_checks")
            if d.get("supersedes") is not None:
                errs.append(f"{pid}: L1 supersedes must be null")
            if d.get("next_action") == "to_l3":
                errs.append(f"{pid}: L1 cannot confirm to_l3 (needs L2)")
        else:
            for c in d.get("subcard_checks") or []:
                if set(c) < {"card", "section", "question", "verdict", "paper_evidence"}:
                    errs.append(f"{pid}: subcard_check missing fields")
                if c.get("verdict") not in VERD:
                    errs.append(f"{pid}: bad verdict {c.get('verdict')}")
            if not d.get("supersedes"):
                errs.append(f"{pid}: L2 must supersedes L1 record")
    missing = set(want) - set(got)
    extra = set(got) - set(want)
    if missing:
        errs.append(f"missing: {sorted(missing)}")
    if extra:
        errs.append(f"extra: {sorted(extra)}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--stage", default="L1", choices=["L1", "L2"])
    args = ap.parse_args()
    errs = check(args.run, args.batch, args.stage)
    if errs:
        print(f"FAIL {args.batch} ({args.stage}): {len(errs)} error(s)")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK {args.batch} ({args.stage})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
