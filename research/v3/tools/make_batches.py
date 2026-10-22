"""Group v3 inputs into Sol batches by total text length (SCORE_SPEC §6).

Greedy fill in inputs.jsonl order; closes a batch when adding the next paper
would exceed the char budget or the paper cap. Oversize papers get a batch of
their own (worker reads them in segments). Writes batches/<id>-inputs.tsv.

Usage: python3 research/v3/tools/make_batches.py --run rsi-v3-20261022-01 \
         [--budget-chars 480000] [--max-papers 12]
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--budget-chars", type=int, default=480_000)
    ap.add_argument("--max-papers", type=int, default=12)
    args = ap.parse_args()

    run_dir = REPO / "research/v3/runs" / args.run
    inputs = [json.loads(l) for l in open(run_dir / "inputs.jsonl")]
    done = set()
    bdir = run_dir / "batches"
    for tsv in bdir.glob("*-inputs.tsv"):
        for line in tsv.read_text().splitlines()[1:]:
            done.add(line.split("\t")[0])

    batches, cur, cur_chars = [], [], 0
    for p in inputs:
        if p["paper_key"] in done:
            continue
        c = p["chars"] or 0
        if cur and (cur_chars + c > args.budget_chars or len(cur) >= args.max_papers):
            batches.append(cur)
            cur, cur_chars = [], 0
        cur.append(p)
        cur_chars += c
    if cur:
        batches.append(cur)

    start = len(list(bdir.glob("*-inputs.tsv")))
    for i, b in enumerate(batches):
        bid = f"b{start + i + 1:03d}"
        lines = ["paper_key\tarxiv\tversion\ttitle\tchars\ttext_path\tsha256\tsource_url"]
        for p in b:
            lines.append("\t".join(str(p[k]) for k in
                          ("paper_key", "arxiv", "version", "title", "chars", "text_path", "sha256", "source_url")))
        (bdir / f"{bid}-inputs.tsv").write_text("\n".join(lines) + "\n")
        print(f"{bid}: {len(b)} papers, {sum(p['chars'] or 0 for p in b)} chars")
    print(json.dumps({"new_batches": len(batches), "papers": sum(len(b) for b in batches),
                      "budget_chars": args.budget_chars, "max_papers": args.max_papers}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
