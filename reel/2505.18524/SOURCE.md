# SOURCE — metaTextGrad: Automatically optimizing language model optimizers

Read from: arXiv 2505.18524v2
Paper figures shown: none

Exact PDF downloaded directly from https://arxiv.org/pdf/2505.18524v2 into `/home/lingxufeng/reel-work/2505.18524/paper.pdf`. Read all 32 pages, including appendices and checklist, with both plain and layout-preserving pdftotext. Visually verified title/authors on p1 and Tables 1–7 on pp8–9,24. No paper or repository code was executed. Code URL supplied by the task/score record: https://github.com/zou-group/metatextgrad.

Figure reuse is forbidden for this assignment. All diagram geometry and charts are our own renderings of the algorithm descriptions and table numbers, not reproductions or crops of paper figures. No paper figures appear in the deliverables.

## Claim and number provenance

| Content | PDF page / source | Scope |
|---|---|---|
| Exact title, author order and affiliations | p1 title block | Guowei Xu (Tsinghua), Mert Yuksekgonul, Carlos Guestrin, James Zou (Stanford) |
| Inner program vs outer optimizer changes, validation scoring and strict improvement rule | pp3,7,14, Algorithms 1–4; pp16–17 Appendix D | Prompt stage changes optimizer task descriptions; structure stage generates Python composition code, not unrestricted algorithm search; both nested algorithms reuse Dval |
| Fixed top-level meta-optimizer | p10 conclusion | Human-designed, not itself learned |
| Models, baseline types and main seed statement | pp7–8, §§4.1–4.2 | GPT-4o-mini task program, GPT-4o TGD/MIPRO, o1 structure/meta; five-seed average test accuracy, not evidence for five independent full meta-searches |
| Headline and per-task chart | p8 Table 1 | Test rows: meta 0.65 / 0.37 / 0.40 / 0.71; strongest baseline per task ADAS-TG 0.58 / eight-shot MIPROv2 0.26 / self-consistency 0.42 / zero-shot MIPROv2 0.77; averages 0.53 vs 0.47 are complete method row averages |
| Ties/exceptions | p8 Table 1 | GPQA best-of-N 0.40 matches meta; Algebra TGD and eight-shot CoT 0.71 match meta. Self-consistency and zero-shot MIPRO lead those columns |
| Six optimization steps per training epoch | p8 §4.2 | Not a statement of complete outer-search iterations or matched total budget |
| Dyck ablation | p9 Table 6 and text below | TGD 0.10 → 0.24 with meta prompt; ADAS-TG 0.16 → 0.37; structure-only 0.16; full 0.37. Validation ADAS 0.21 vs structure-only 0.24; no new best composition found |
| Model transfer | p9 Table 4 | Haiku Dyck meta val/test 0.32/0.35, ADAS 0.35/0.34. Tiny test margin has no uncertainty estimate |
| Task transfer | p9 Table 5; compare Table 1 p8 | GPQA-trained optimizer → Algebra 0.77, TGD 0.71, ADAS 0.70. MIPRO not in Table 5; its in-domain Table 1 result is also 0.77. Target adaptation/reset details are not specified fully |
| Data splits and evaluation rules | p15 Appendix C | BBH 50/100/100, Algebra 10/50/40, GPQA 30/100/68; GPT-4o correctness judge for BBH; regex exact match for Algebra/GPQA except GPT-4o judging for DSPy outputs |
| Compound optimization cost | pp8–9 §4.3, Table 2 | Algebra per meta epoch: ~400k / ~100k / ~2.5k tokens at program/optimizer/meta levels; zero-shot round ~140k. No computed total is presented |
| Separate performance/$ comparison | p9 Table 3 | Dyck optimized mini 0.37/$0.44, zero mini 0.05/$0.14, zero 4o 0.18/$0.52. Full meta-search inclusion/amortization is unspecified, not assumed excluded or included |
| Open-model configuration | p24 Appendix G, Table 7 | Non-thinking Qwen3-8B program, Qwen3-235B-A22B optimizer/meta; Dyck 0.77 vs strongest baseline TGD 0.68 |
| ARC configuration | p24 Appendix H, Table 7 | ≤5×5 grids, 20/30/30 train/val/test, Claude 3 Haiku program and Claude 3.5 Sonnet optimizer/meta; one-shot test success rates 0.40 vs TGD 0.33; no appendix table-specific seed protocol; Table 7 results retained in blogs only |
| Absent gains and strong-meta-model dependence | p25 Appendix I | AIME 2024 / GPT-4o-mini no significant gains, no scores supplied; Gemini 1.5 Pro inadequate as meta model |
| Repetition vs variance | p7 §4.1; p28 checklist item 7; tables | Five-seed test average stated in §4.1, experimental-section repetition asserted in checklist. No SD/SE/CI or per-seed results; does not identify which stages rerun. Table 7 appendices do not have their own seed specification |

## ‡ numbers

None. No derived deltas, computed win counts, or figure-label values are used. Every empirical decimal is transcribed from PDF text/tables. The chart uses the Table 1 proportions directly; its evenly spaced axis ticks are a plotting scale, not extra empirical measurements.

## Important scope and missing-control notes

- Main average 0.53 vs 0.47 compares metaTextGrad to the highest-average single baseline row (zero-shot MIPROv2), not to the per-task baseline envelope. Gains are concentrated in Word Sorting and Dyck; no universal-win claim.
- The method retains candidates according to downstream validation score. Section 3.3 describes an initial incumbent evaluation; Appendix A pseudocode initializes best score to zero. We describe the prose's incumbent comparison and do not assert these initialization details reconcile.
- The paper specifies separate train/validation/test splits and same-task optimization. Reuse of validation for nested selection is explicit in Algorithms 1–2. No contamination/overlap audit was found after reading the full appendix and checklist; this is not an allegation of actual test contamination.
- Hyperparameter/default selection procedure and the split used for that selection are not specified. Validation's role in program/optimizer selection does not establish how defaults were tuned. Total outer iterations, per-baseline iteration/tuning budgets and matched full-search compute are unreported.
- Baseline scope: direct zero-shot CoT; eight-shot demonstrations; eight-sample self-consistency and best-of-N (further selection/ground-truth access not specified); GPT-4o MIPROv2 and TGD optimization; o1 structure optimization for ADAS-TG. Do not claim these baselines lack task feedback, validation optimization or a capable optimizer model. Ordinary baseline rows lack the outer optimizer-rewriting stage; ablations separately show prompt-meta-optimized variants.
- GPT-4o judging is common to BBH methods, and is additionally used for DSPy on Algebra/GPQA where other methods use regex exact match. This is a measurement asymmetry. We explicitly label judge-family/robustness concerns as our reading; no favoritism is demonstrated. No alternate-judge robustness control is reported.
- Transfer artifacts are optimizers, not frozen final programs. The paper does not fully state reset/reuse or target-side data exposure; transfer is not described here as zero-shot/no-target-data.
- **Paper prose versus test tables (scope unresolved):** §4.2 (p8) says metaTextGrad outperforms TGD and ADAS-TG across all benchmarks, but Table 1's Algebra test column ties metaTextGrad and TGD at 0.71; validation is 0.78 versus 0.76. §4.5 (p9) says all meta optimizers improve performance, but Table 6's structure-only and ADAS-TG test cells both read 0.16, while validation improves from 0.21 to 0.24. Thus the prose is broader than a strict-improvement claim on every test column; validation/test scope matters. We use the values as printed, leave the prose/test scope discrepancy unresolved, and propose no cause. The abstract's average gain and Table 1 row averages agree at reported precision.

## Judgment notes

Source records: `/home/lingxufeng/ArxivDaily/research/scores.jsonl` (64, ★★, improver) and latest matching judgment `/home/lingxufeng/ArxivDaily/research/judgments/b18.jsonl`. No score or judgment record was changed.

- `held_out: unclear` understates Appendix C's explicit separate test splits. Retention and selection use validation; test is distinct. This is held-out-example evidence, not leave-task-out evidence.
- `variance: unclear` should not be read as no repetitions: §4.1 reports five-seed average test accuracy and checklist item 7 says experimental-section results were repeated five times. However dispersion is genuinely not reported, and which stochastic stages are rerun remains unspecified.
- `optimizer_cost: yes` is supported by per-meta-epoch token tiers and a separate task-cost comparison, not by a full multi-epoch optimizer-construction bill.
- The recorded improver level is retained in the presentation, while emphasizing that budget equality is unclear. Dyck's strongest ablation supports task-aligned optimizer prompts, and gives no incremental composition benefit.

## Rendering and verification

The poster is a 2400×1440 house-style HTML render, adapted from the M⋆ script using the unmodified shared poster library. No figure extraction is embedded. Measured under print emulation at 2400×1440: no overflowing cards; HTML body/caption/table minimum 22 px; actual method-text minimum 22.71 px; actual chart-text minimum 19.39 px (after SVG scaling). Method labels use at least 25 SVG units; chart values/categories 26 and tick labels 28. The final PNG and chart detail were visually inspected; connectors occupy the gaps between method boxes. PNG size 474,849 bytes. After independent fact-check revision, reverified the initialization difference against pp6–7 and Algorithm 3–4 on p14, removed optional Table 7 results from the poster (fully scoped in both blogs, including ARC one-shot success rates), and added explicit unresolved prose/test-scope notes against Tables 1 and 6. No findings were rejected. The skill's paper-figure requirement is superseded by the assignment's explicit prohibition of any paper figures; the requested house-style library and reel gate are used instead.
