# Reel — posters and interpretations of top papers

Made by the scorer (Dots) after each day's scoring, with the
[ResearchStudio-Reel](https://github.com/microsoft/ResearchStudio) skills. Shown in the README poster gallery.
Procedure: [docs/agents/DOTS_PROMPT.md](../docs/agents/DOTS_PROMPT.md), stage C. Gate: `python3 research/check_reel.py`.

- **Candidates:** [candidates.md](candidates.md) — every board paper scoring ≥ 60, with its arXiv license.
  Refresh after the board changes: `python3 research/reel_candidates.py` (keeps `status`).
- **Figures:** `reuse` = CC BY / BY-SA / CC0 — the paper's figures may be shown, each credited. `redraw` = arXiv
  default or NC/ND license — no figure from the paper; a diagram we draw ourselves, or none.
- **Order:** highest score first.

## Output (one directory per paper, committed)

```
reel/<arxiv_id>/
  poster.png     # ≤ 3 MB, gallery thumbnail
  poster.pdf     # print version
  blog_zh.md     # Chinese interpretation
  blog_en.md     # English interpretation
  SOURCE.md      # see below
```
Never committed: `poster.html`, `.pptx`, `.mp3`, `.docx`, videos, the `paper2assets` bundle, `research/paper_text/`.

`SOURCE.md` must contain these exact lines (checked):
- `Read from: arXiv <version>` — the version in `candidates.jsonl`, read from the PDF or arXiv HTML. No PDF → no poster.
- `Paper figures shown: none` — required when `figure_reuse` is false; otherwise a table of each figure shown and its credit.
- A note for every number marked `‡` (computed by us from paper numbers, e.g. a difference), saying how it was computed.

## Content standard
1. What the system changes about itself, from what signal, and how changes are kept or rejected.
2. Results exactly as the paper reports them (model, benchmark, seeds, budget). Every decimal number must occur in the
   paper — the checker verifies this against the full text, tables included. Never recompute from a code repository.
3. The paper's own controls that decide whether the gain is real (ablations, matched-compute rows, the same mechanism
   granted to baselines, transfer) — the takeaway must follow from these, not from the headline number alone.
4. Where gains are absent or small, say so with the paper's numbers; do not invent weaknesses or strengths.
5. An "Our read" box: HarnessRSI score, evidence level, and what evidence the paper does and does not report — taken
   from `research/scores.jsonl` and `research/judgments/`. Neutral wording, no hype.
