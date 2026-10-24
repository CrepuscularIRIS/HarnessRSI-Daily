"""Build the L2 queue from completed L1 records (controller-only, PROBLEM_CORE §5).

Order: priority high → medium (both non-confirmed next_action=to_l2), capped at
--budget (default 20% of L1 count). Plus --audit share (default 10% of budget)
sampled with a recorded seed from P0/P1/F0/needs_material/park records.
Papers without cached fulltext stay parked (no auto-download; listed separately).

Usage: python3 research/scoring/tools/l2_queue.py --run rsi-l1-20261022-03 --seed 42
"""

import argparse
import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ORDER = {"high": 0, "medium": 1, "low": 2, "none": 3}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--budget", type=int, default=0, help="0 = 20%% of L1 count")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    run_dir = REPO / "research/scoring/runs" / args.run

    ft = {}
    for p in (REPO / "research/fulltext/review-runs").glob("*/materials/*.txt"):
        ft[p.stem] = str(p.relative_to(REPO))

    recs = {}
    l2_done = set()
    for f in sorted((run_dir / "batches").glob("*.jsonl")):
        for line in open(f):
            line = line.strip()
            if line:
                d = json.loads(line)
                if d.get("stage") == "L1":
                    recs[d["paper_id"]] = d
                elif d.get("stage") == "L2":
                    l2_done.add(d["paper_id"])
    l1_total = len(recs)
    budget = args.budget or l1_total // 5
    audit_n = budget // 10

    def l2_ok(d):
        return d["next_action"] == "to_l2" and d["status"] != "out_of_scope"

    main_pool = sorted((d for d in recs.values() if l2_ok(d) and d["paper_id"] in ft
                        and d["paper_id"] not in l2_done),
                       key=lambda d: (ORDER.get(d["priority"], 9), d["paper_id"]))
    main_pick = [d for d in main_pool if d["priority"] in ("high", "medium")][:budget]

    audit_pool = [d for d in recs.values()
                  if d["paper_id"] in ft and d["paper_id"] not in l2_done
                  and d["paper_id"] not in {x["paper_id"] for x in main_pick}
                  and (d["problem_tier"] in ("P0", "P1") or "F0" in (d.get("families") or [])
                       or d["status"] == "needs_material" or d["next_action"] == "park")]
    rng = random.Random(args.seed)
    audit_pick = rng.sample(audit_pool, min(audit_n, len(audit_pool)))
    for d in audit_pick:
        d["audit_sample"] = True

    queued = main_pick + audit_pick
    no_ft = [d["paper_id"] for d in recs.values() if l2_ok(d) and d["paper_id"] not in ft]

    rows = ["paper_id\tpriority\ttier\tfamilies\tcards\tmaterial\tfulltext_path\taudit_sample\tl1_batch"]
    by_batch = {}
    for d in sorted(queued, key=lambda d: d["paper_id"]):
        bid = next(f.stem for f in (run_dir / "batches").glob("*.jsonl")
                   if d["paper_id"] in {json.loads(l)["paper_id"] for l in open(f) if l.strip()})
        rows.append("\t".join([d["paper_id"], d["priority"], d["problem_tier"] or "null",
                               ",".join(d["families"]), ",".join(d["cards"]), d["material"],
                               ft[d["paper_id"]], str(d.get("audit_sample", False)).lower(), bid]))
        by_batch.setdefault(bid, []).append(d["paper_id"])
    (run_dir / "l2-queue.tsv").write_text("\n".join(rows) + "\n")
    summary = {"l1_total": l1_total, "budget": budget, "queued": len(queued),
               "main": len(main_pick), "audit": len(audit_pick), "seed": args.seed,
               "audit_pool_size": len(audit_pool),
               "l2_blocked_no_fulltext": len(no_ft)}
    (run_dir / "l2-queue-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
