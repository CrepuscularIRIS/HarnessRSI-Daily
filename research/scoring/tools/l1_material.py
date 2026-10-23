"""Prepare L1 materials (abstract + intro head) from cached corpus/fulltext.

PROBLEM_CORE §5 L1: 摘要＋引言，由脚本从已缓存原文按标题切出；切不出则只用摘要。
No network — reuses research/corpus.jsonl and the pinned fulltext cache.

Usage: python3 research/scoring/tools/l1_material.py --run <run_id> --ids 2605.19576,...
       python3 research/scoring/tools/l1_material.py --run <run_id> --ids-file run_dir/pilot-ids.txt
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HEAD_CHARS = 9000  # abstract + intro budget per paper


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--ids", default="")
    ap.add_argument("--ids-file", default="")
    args = ap.parse_args()
    run_dir = REPO / "research/scoring/runs" / args.run
    out_dir = run_dir / "l1_materials"
    out_dir.mkdir(parents=True, exist_ok=True)

    corpus = {json.loads(l)["arxiv"]: json.loads(l) for l in open(REPO / "research/corpus.jsonl")}
    ft_dirs = sorted((REPO / "research/fulltext/review-runs").glob("*/materials"))

    ids = [i for i in args.ids.split(",") if i]
    if args.ids_file:
        ids += [l.strip() for l in open(REPO / args.ids_file) if l.strip()]

    stats = {"abstract_intro": 0, "abstract": 0}
    rows = []
    for aid in ids:
        c = corpus[aid]
        title, abstract = c["title"], c.get("abstract") or ""
        text_path = None
        for d in ft_dirs:
            p = d / f"{aid}.txt"
            if p.exists():
                text_path = p
                break
        level, intro = "abstract", ""
        if text_path:
            head = text_path.read_text(errors="replace")[:HEAD_CHARS + 2000]
            nt = norm(title)
            if nt and nt[:60] in norm(head)[:4000]:
                start = norm(head)[:4000].index(nt[:60])
                # map normalized offset back approximately: just slice from a proportional point
                raw_start = int(start * len(head) / max(len(norm(head)[:4000]), 1))
                intro = head[max(0, raw_start - 200):raw_start + HEAD_CHARS]
                if len(intro) > 200:
                    level = "abstract_intro"
        body = f"arXiv: {aid}    title: {title}\n\n[abstract]\n{abstract}"
        if intro:
            body += f"\n\n[intro/head from pinned fulltext]\n{intro}"
        (out_dir / f"{aid}.txt").write_text(body, encoding="utf-8")
        stats[level] += 1
        rows.append({"paper_id": aid, "material": level, "title": title,
                     "material_path": str(out_dir.relative_to(REPO) / f"{aid}.txt"),
                     "source_url": f"https://arxiv.org/abs/{aid}"})
    with open(run_dir / "l1_inputs.jsonl", "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(json.dumps(stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
