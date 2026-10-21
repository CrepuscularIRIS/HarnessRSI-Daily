"""Controller-only: advance queue states from accepted batch validations.

Usage: python3 research/v2/tools/update_queue.py --run R --batch cal-dev
Reads batches/<b>/aggregate/attempts/<a>/validation.json (accepted papers) and
marks queue rows: scored (final_record pointer) or blocked (needs_*/out_of_scope).
Idempotent: re-running keeps the latest accepted pointer per paper.
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--batch", required=True)
    args = ap.parse_args()
    run_dir = REPO / "research/v2/runs" / args.run
    bdir = run_dir / "batches" / args.batch
    mani = json.load(open(bdir / "manifest.json"))
    att = mani["aggregate"]["attempt"]
    val = json.load(open(bdir / "aggregate" / "attempts" / att / "validation.json"))
    rows = [json.loads(l) for l in open(run_dir / "queue.jsonl")]
    by_key = {r["paper_key"]: r for r in rows}
    changed = 0
    for pid, info in val["papers"].items():
        r = by_key[pid]
        final_rel = f"batches/{args.batch}/aggregate/attempts/{att}/{pid}.final.json"
        if info.get("errors"):
            continue  # only accepted results advance the shared queue
        st = info.get("record_status")
        agg = info.get("aggregate_status")
        if agg == "accepted_final" and st == "reviewed":
            new = {"state": "validated", "score_raw": info.get("score_raw"),
                   "valid_attempt": final_rel, "batch": args.batch}
        elif agg == "accepted_final":
            new = {"state": "validated", "disposition": st, "score_raw": None,
                   "valid_attempt": final_rel, "batch": args.batch}
        else:
            new = {"state": "blocked", "disposition": agg, "score_raw": None,
                   "valid_attempt": final_rel, "batch": args.batch}
        if {k: r.get(k) for k in new} != new:
            r.update(new)
            changed += 1
    if changed:
        with open(run_dir / "queue.jsonl", "w") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_scored = sum(1 for r in rows if r.get("state") == "validated" and r.get("score_raw") is not None)
    n_disp = sum(1 for r in rows if r.get("state") == "validated")
    print(json.dumps({"batch": args.batch, "rows_updated": changed,
                      "queue_scored_total": n_scored, "queue_validated_total": n_disp,
                      "queue_total": len(rows)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
