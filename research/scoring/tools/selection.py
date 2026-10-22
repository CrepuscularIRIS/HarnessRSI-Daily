"""Build the L3 candidate pool from L2 records (controller-only, SELECTION.md).

Collects next_action=to_l3 (confirmed) records, joins corpus metadata (title,
github), dedups by method family (manual review note), writes l3-candidates.tsv.

Usage: python3 research/scoring/tools/selection.py --run rsi-l1-20261022-03
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()
    run_dir = REPO / "research/scoring/runs" / args.run
    corpus = {json.loads(l)["arxiv"]: json.loads(l) for l in open(REPO / "research/corpus.jsonl")}

    rows = []
    for f in sorted((run_dir / "batches").glob("l2b*.jsonl")):
        for line in open(f):
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            if d.get("next_action") == "to_l3":
                c = corpus.get(d["paper_id"], {})
                rows.append({
                    "paper_id": d["paper_id"], "tier": d["problem_tier"],
                    "status": d["evidence_status"], "priority": d["priority"],
                    "families": ",".join(d["families"]), "cards": ",".join(d["cards"]),
                    "q2_open": d["q2_open"], "q3_change": d["q3_change"], "q4_fit": d["q4_fit"],
                    "problem": d["problem_statement"], "gap": d.get("biggest_gap", ""),
                    "title": c.get("title", ""), "github": c.get("github") or "",
                    "audit": d.get("audit_sample", False),
                })
    rows.sort(key=lambda r: (r["tier"], r["priority"], r["paper_id"]))
    out = ["paper_id\ttier\tstatus\tpriority\tfamilies\tcards\tq2\tq3\tq4\tgithub\taudit\ttitle\tproblem\tgap"]
    for r in rows:
        out.append("\t".join([r["paper_id"], r["tier"], r["status"], r["priority"], r["families"],
                              r["cards"], r["q2_open"], r["q3_change"], r["q4_fit"], r["github"],
                              str(r["audit"]).lower(), r["title"].replace("\t", " "),
                              r["problem"].replace("\t", " "), r["gap"].replace("\t", " ")]))
    (run_dir / "l3-candidates.tsv").write_text("\n".join(out) + "\n")
    n2026 = sum(1 for r in rows if r["paper_id"].startswith("26"))
    print(json.dumps({"to_l3": len(rows), "of_2026": n2026}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
