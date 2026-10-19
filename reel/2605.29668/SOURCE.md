# Source — 2605.29668 (GRASP)

| | |
|---|---|
| Paper | GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents — Moll, Corbeil, Pan, Hadamitzky, Rueckert, Adams, Bressem |
| Paper version | [2605.29668v3](https://arxiv.org/abs/2605.29668v3) (version in `candidates.jsonl`; see the read limitation below) |
| Paper license | CC BY 4.0 (`figure_reuse: true`) |
| Code | [jomoll/GRASP](https://github.com/jomoll/GRASP) @ `9d7d125a3e9b46ed591692475eb07aff4ae67d34` (2026-08-21), MIT License |
| HarnessRSI context | `research/scores.jsonl`: 84 ★★★, evidence level `retained`, sub-pattern [H30](../../patterns/sub/H30.md) |

## How the content was sourced (read limitation)

The arXiv PDF and e-print could not be downloaded: this run's cloud network policy blocks `arxiv.org` and
`export.arxiv.org` (and the alphaxiv/emergentmind mirrors). Following the maintainer's instruction to use web
search instead, the poster and blogs were built from:

1. The abstract, via web search results for the paper.
2. The authors' code repository at the commit above: `docs/method.md` (algorithm, gate rule, injection, capacity),
   `results/README.md` (which result directory backs which paper table) and `results/main/run_001/config.yaml`.
3. Verbatim v3 quotes already recorded in `research/judgments/b14.jsonl` (held-out splits, seeds, OOD 56.3 vs 31.3,
   call cost, transfer, memory regression).
4. Numbers recomputed from the repository's released per-seed results (`results/main`, `results/ablations`,
   `results/nonmedical`) with the logic of the repository's `results/reproduce_tables.py`. The recomputed headline
   values match the abstract (40.6 → 88.8 %, +21.0 pts over the best baseline).

Not checked against the PDF: figure numbering in the paper, the exact Table 4 rows (the ablation numbers come
from `results/ablations`, per `results/README.md`), and any caveats in the paper text that are not in the sources above.
Please re-check against the v3 PDF before this is shared.

## Figures shown

| Where | Figure | Source | License |
|---|---|---|---|
| Poster, Method | GRASP overview diagram | `assets/central_illustration.png` in the code repository (the paper's figure numbering was not verified) | MIT (repository); paper CC BY 4.0 |
| Poster, Key Results | Bar chart of MedAgentBench test accuracy (gpt-oss-120b, 5 seeds) | drawn by us in HTML/CSS from `results/main/gpt-oss-120b/MedAgentBench/*` | ours, from released data |

The blogs embed the same overview diagram in their DOCX versions. The Markdown versions here contain no images,
only the credited caption pointing to `poster.png`.

## Tools

- Skills: ResearchStudio-Reel ([microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) @ `063f100`)
  `paper2assets` (bundle built by hand: no PDF, so `source_figures.py --images` plus a hand-written `paper_spec.md`),
  `paper2poster` (compose, `check_poster.py` preflight/slack, `render_poster.py`), `paper2blog` (`build_wechat_docx.py`,
  `check_blog_package.py`: 0 errors, 4 warnings for short final lines and one false-positive number diff).
- Poster: landscape 60 × 36 in, `full` layout, header `v6` (no institution logos), theme blue. No narration audio (Edge TTS host blocked).
- Blogs: DOCX converted with `pandoc -t gfm`. Title restored and image links removed afterwards.
- Model: Claude (Claude Code cloud session).
