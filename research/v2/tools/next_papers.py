"""Pick the next production papers for batching (controller-only).

Usage: python3 research/v2/tools/next_papers.py --run R --count 5 [--min-chars 60000]
Prints one paper_key per line: state=queued, material complete; long papers
(chars >= LONG_CHAR_THRESHOLD) are grouped into their own smaller batches when
--long-batches is passed. Deterministic queue order (A-first, then B; id asc).
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
LONG = 120_000


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--count", type=int, default=5)
    ap.add_argument("--long", action="store_true", help="emit only long papers")
    ap.add_argument("--short", action="store_true", help="emit only papers below the long threshold")
    args = ap.parse_args()
    run_dir = REPO / "research/v2/runs" / args.run
    batched = set()
    for bm in (run_dir / "batches").glob("*/manifest.json"):
        if bm.parent.name.startswith("_"):
            continue
        batched.update(json.load(open(bm))["papers"])
    mats = {}
    for p in (run_dir / "materials").glob("*.json"):
        if p.stem.endswith(".pages"):
            continue
        m = json.load(open(p))
        if m.get("complete"):
            mats[m["paper_key"]] = m.get("chars") or 0
    out = []
    for line in open(run_dir / "queue.jsonl"):
        q = json.loads(line)
        k = q["paper_key"]
        if q.get("state") != "queued" or k not in mats or k in batched:
            continue
        is_long = mats[k] >= LONG
        if args.long and not is_long:
            continue
        if args.short and is_long:
            continue
        out.append(k)
        if len(out) >= args.count:
            break
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
