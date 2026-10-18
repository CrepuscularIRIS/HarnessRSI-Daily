"""Generate patterns/overview.md from taxonomy.json + contrast.json (deterministic; rerun after any change)."""

import json
from pathlib import Path

R = Path("research")
BOUNDARY = {"self_generate_the_curriculum", "couple_context_and_weight_updates", "amortize_improver_into_trained_policy"}


def main() -> None:
    tax = json.loads((R / "patterns/taxonomy.json").read_text())
    con = json.loads((R / "patterns/contrast.json").read_text())
    iclr = {r["key"]: r for r in con["iclr_2025_2026"]["main"] + con["iclr_2025_2026"]["sub"]}
    counts: dict[str, int] = {}
    for line in (R / "patterns/assignments.jsonl").read_text().splitlines():
        sid = json.loads(line)["sub_pattern"]
        counts[sid] = counts.get(sid, 0) + 1
    rate = lambda k: (f"{iclr[k]['p_accept']:.0%} ({iclr[k]['delta_pp']:+.1f} pp, n={iclr[k]['n']})" if k in iclr else "n<10")
    base = con["iclr_2025_2026"]["base_p_accept"]
    md = [
        "# Harness RSI patterns — overview", "",
        f"{len(tax['main_patterns'])} main patterns and {len(tax['sub_patterns'])} sub-patterns, induced from 585 harness-level "
        "self-improvement papers (outcome labels withheld during induction). Paper counts below are the arXiv corpus; "
        f"accept rates are within ICLR 2025–2026 submissions (base rate {base:.0%}). "
        "Read the cards for confidence intervals; most differences are not significant. See also [anti-patterns](anti-patterns.md).", "",
        "Like ResearchStudio's ideation patterns, these are diagnostic vocabulary for research moves, not labels for domains.", "",
        "| main pattern | operational signature | papers | ICLR accept rate |", "|---|---|---|---|",
    ]
    for m in tax["main_patterns"]:
        n = sum(counts.get(s["id"], 0) for s in tax["sub_patterns"] if s["parent"] == m["id"])
        flag = " *(boundary: touches weights)*" if m["id"] in BOUNDARY else ""
        md.append(f"| [{m['name']}](main/{m['id']}.md){flag} | {m['operational_signature']} | {n} | {rate(m['id'])} |")
    md += ["", "## Sub-patterns", "", "| id | sub-pattern | parent | papers | ICLR accept rate |", "|---|---|---|---|---|"]
    names = {m["id"]: m["name"] for m in tax["main_patterns"]}
    for s in tax["sub_patterns"]:
        md.append(f"| [{s['id']}](sub/{s['id']}.md) | {s['name']} | {names[s['parent']]} | {counts.get(s['id'], 0)} | {rate(s['id'])} |")
    Path("patterns/overview.md").write_text("\n".join(md) + "\n")
    print(f"wrote patterns/overview.md ({len(md)} lines)")


if __name__ == "__main__":
    main()
