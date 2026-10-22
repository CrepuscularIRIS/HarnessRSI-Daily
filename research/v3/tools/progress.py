"""Recompute progress.md from batch outputs on disk (controller-only).

Usage: python3 research/v3/tools/progress.py --run rsi-v3-20261022-01
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = REPO / "research/v3/runs" / args.run
    total = sum(1 for _ in open(run_dir / "inputs.jsonl"))
    n = Counter()
    batches_done, inflight = [], 0
    scores = []
    for f in sorted((run_dir / "batches").glob("b*.jsonl")):
        tsv = f.with_name(f.stem + "-inputs.tsv")
        want = {l.split("\t")[0] for l in tsv.read_text().splitlines()[1:] if l.strip()}
        got_ids = set()
        c = Counter()
        for line in open(f):
            line = line.strip()
            if line:
                d = json.loads(line)
                got_ids.add(d["paper_id"])
                c[d["status"]] += 1
                if d.get("screen_score") is not None:
                    scores.append((d["screen_score"], d["paper_id"]))
        if got_ids == want:
            n.update(c)
            batches_done.append(f"{f.stem}:{c.get('scored', 0)}s/{c.get('needs_material', 0)}n/{c.get('out_of_scope', 0)}o")
        else:
            inflight += 1
    done = sum(n.values())
    scores.sort(reverse=True)
    top = "\n".join(f"  {s} {p}" for s, p in scores[:5]) or "  （暂无）"
    text = f"""# progress — {args.run}（总控维护，从盘上批次文件重算）

| 指标 | 数 |
|---|---|
| 已处理 | {done} / {total} |
| scored | {n.get('scored', 0)} |
| needs_material | {n.get('needs_material', 0)} |
| out_of_scope | {n.get('out_of_scope', 0)} |
| 剩余 | {total - done} |

当前最高分（前 5）：
{top}

批次：{len(batches_done)} 个有输出。
"""
    (run_dir / "progress.md").write_text(text)
    print(json.dumps({"done": done, "total": total, "remaining": total - done, **n}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
