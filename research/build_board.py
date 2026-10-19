"""Render the paper board from research/scores.jsonl (format inspired by Aerial-VLN-Arxiv-Daily, plus scores).

Writes papers/README.md (every scored paper, grouped by main pattern, best first) and rewrites the block between
<!-- BOARD:START --> and <!-- BOARD:END --> in README.md with the ★★★ papers. Deterministic; rerun after scoring.
"""

import json
import re
from pathlib import Path

R = Path("research")
BOUNDARY = {"self_generate_the_curriculum", "couple_context_and_weight_updates", "amortize_improver_into_trained_policy"}


def jl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def row(s: dict, meta: dict) -> str:
    m = meta[s["arxiv"]]
    title = m["title"].replace("|", "\\|")
    code = f"[code]({s['code_url']})" if s.get("code_url") else ("✓" if s["code"] == "yes" else "announced" if s["code"] == "announced" else "—")
    return (f"| {m['published']} | **[{title}](https://arxiv.org/abs/{m['latest_version']})**<br>{s['title_zh']}<br><sub>{s['one_line']}</sub> "
            f"| [{s['sub_pattern']}](../patterns/sub/{s['sub_pattern']}.md) | **{s['total']}** {s['band']}<br><sub>E{s['evidence']} X{s['execution']:.0f} L{s['level']} C{s['code']}</sub> | {code} |")


def main() -> None:
    scores = sorted(jl(R / "scores.jsonl"), key=lambda s: (-s["total"], s["arxiv"]))
    meta = {r["arxiv"]: r for r in jl(R / "corpus.jsonl")}
    tax = json.loads((R / "patterns/taxonomy.json").read_text())
    head = "| Date | Paper | Sub-pattern | Score | Code |\n|---|---|---|---|---|"
    legend = ("Score (0–100) = **E**vidence (50) + e**X**ecution against the pattern card (30) + evidence **L**evel (10) + "
              "**C**ode (10); every judgment is quote-backed — see [SCORE_SPEC](../research/SCORE_SPEC.md). "
              "It measures what a paper reports and how it executes its move, not the value of the idea.")
    md = ["# Paper board", "", f"{len(scores)} harness-level RSI papers scored. {legend}", ""]
    md += [f"- [{m['name']}](#{m['id'].replace('_', '-')})" for m in tax["main_patterns"]] + [""]
    for m in tax["main_patterns"]:
        rows = [s for s in scores if s["main_pattern"] == m["id"]]
        if not rows:
            continue
        flag = " *(boundary: touches weights)*" if m["id"] in BOUNDARY else ""
        md += [f'<a id="{m["id"].replace("_", "-")}"></a>', f"## {m['name']}{flag}", "",
               f"Pattern card: [{m['id']}](../patterns/main/{m['id']}.md) · {len(rows)} papers", "", head]
        md += [row(s, meta) for s in rows] + [""]
    Path("papers").mkdir(exist_ok=True)
    Path("papers/README.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    top = [s for s in scores if s["band"] == "★★★"]
    block = ["<!-- BOARD:START -->", "## Top papers (★★★, score ≥ 70)", "",
             f"{len(top)} of {len(scores)} scored papers. Full board, grouped by pattern: [papers/](papers/README.md).", "",
             head.replace("Sub-pattern", "Pattern")]
    block += [row(s, meta).replace("](../", "](") for s in top]
    block.append("<!-- BOARD:END -->")
    readme = Path("README.md").read_text(encoding="utf-8")
    if "<!-- BOARD:START -->" in readme:
        readme = re.sub(r"<!-- BOARD:START -->.*?<!-- BOARD:END -->", "\n".join(block), readme, flags=re.S)
    else:
        readme = readme.replace("## What is here", "\n".join(block) + "\n\n## What is here", 1)
    Path("README.md").write_text(readme, encoding="utf-8")
    print(f"board: {len(scores)} papers, {len(top)} top")


if __name__ == "__main__":
    main()
