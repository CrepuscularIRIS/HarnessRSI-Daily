"""Assemble an immutable v2.2 batch manifest (controller-only).

Fixes paper set + versions + material hashes + asset hashes into one input package and
computes input_hash (sha256 of the canonical manifest without the input_hash field).
Workers copy input_hash into every record's provenance; seats see identical inputs.

Usage: python3 research/v2/tools/make_batch.py --run R --batch cal-dev --kind calibration_dev \
         --ids 1112.5309,... [--seats-attempt a1] [--rubric-file research/SCORE_SPEC.md]
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def canon(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--kind", default="production", choices=["calibration_dev", "calibration_holdout", "production"])
    ap.add_argument("--ids", required=True)
    ap.add_argument("--seats-attempt", default="a1")
    ap.add_argument("--aggregate-attempt", default="a1")
    ap.add_argument("--rubric-file", default=None)
    args = ap.parse_args()

    run_dir = REPO / "research/v2/runs" / args.run
    manifest = json.load(open(run_dir / "manifest.json"))
    queue = {q["paper_key"]: q for q in map(json.loads, open(run_dir / "queue.jsonl"))}
    ids = [i for i in args.ids.split(",") if i]

    papers = []
    for key in ids:
        meta = json.load(open(run_dir / "materials" / f"{key}.json"))
        q = queue[key]
        papers.append({
            "paper_key": key, "arxiv": q["arxiv"], "version": q["version"], "title": q["title"],
            "material": {
                "text_path": f"research/fulltext/review-runs/{args.run}/materials/{key}.txt",
                "sha256": meta["sha256"], "chars": meta["chars"], "method": meta["method"],
                "source_url": meta["source_url"], "complete": meta["complete"],
            },
        })

    rubric_path = args.rubric_file or "research/SCORE_SPEC.md"
    rubric_hash = hashlib.sha256((REPO / rubric_path).read_bytes()).hexdigest()
    batch = {
        "batch_id": args.batch, "run_id": args.run, "kind": args.kind, "created_local": "2026-10-21",
        "papers": [p["paper_key"] for p in papers],
        "paper_details": papers,
        "assets": manifest["assets"],
        "rubric": {"path": rubric_path, "sha256": rubric_hash,
                   "note": "calibration phase uses SCORE_SPEC generic anchors" if args.kind.startswith("calibration") and rubric_path.endswith("SCORE_SPEC.md") else "frozen rubric"},
        "seats": {"sol": {"attempt": args.seats_attempt}, "son55": {"attempt": args.seats_attempt}},
        "aggregate": {"attempt": args.aggregate_attempt},
    }
    input_hash = hashlib.sha256(canon(batch).encode("utf-8")).hexdigest()
    batch["input_hash"] = input_hash
    bdir = run_dir / "batches" / args.batch
    for seat in ("sol", "son55"):
        (bdir / "seats" / seat / "attempts" / args.seats_attempt).mkdir(parents=True, exist_ok=True)
    (bdir / "aggregate" / "attempts" / args.aggregate_attempt).mkdir(parents=True, exist_ok=True)
    (bdir / "manifest.json").write_text(json.dumps(batch, ensure_ascii=False, indent=1))
    print(json.dumps({"batch": args.batch, "papers": len(ids), "input_hash": input_hash[:16],
                      "dir": str(bdir.relative_to(REPO))}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
