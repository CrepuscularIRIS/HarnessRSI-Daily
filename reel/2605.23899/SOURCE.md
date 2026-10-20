# SOURCE — From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

Read from: arXiv 2605.23899v1
Paper figures shown: none

The exact-version PDF was downloaded from https://arxiv.org/pdf/2605.23899v1 and read in full, including appendices A–H. The title and author order were checked against the rendered title page. Figure reuse was permitted by the worker assignment; no paper figure is reused. Our diagram and results chart are independently drawn from the method and table values. The PDF points to https://aka.ms/SkillLens; the supplied board record provides https://github.com/microsoft/SkillLens. No repository code was used as evidence or executed.

## Page/table provenance

| Content | Source in the exact-version PDF |
|---|---|
| Exact title, author order, affiliations, code pointer | Title block, p1 |
| Single-step retained skill, target's own traces, success/failure signal; no weights updated | §3.1–3.2, pp4–5; §4.1, p7 |
| Extraction and rejection at model discretion; empty pattern lists, deduplication, vague-pattern removal; schema/length enforcement | Appendix B.3, Tables 2–4, pp16–18 |
| One skill injected directly, optional rather than mandatory; multi-skill tools are a separate documented protocol | §4.1, p7; Appendix A, p15; B.4/Table 5, pp17–19; Table 6, p20 |
| Default budget: 3 modes/trace, groups of 10, 3000 characters, 1 skill, temperature 1.0 | Appendix B.5 and Table 7, pp17,20 |
| Five domains/six targets/five extractors; Qwen3.5-9B extractor exclusion | §4.1, pp5–7 |
| Full matrix, TE and EE, positive/negative cases and all headline table decimals | Table 1, p6; definitions §3.3, p5; authors' approximate percentage summary §4.2, p7 |
| Experience/test allocation, official train exception, fixed-seed random split otherwise, shared splits, three-run means including Base | §4.1, p7; Appendix B.1–B.2, p15 |
| Experience mixture intervention | §5.1/Figure 2, p8; only qualitative domain dependence used, no figure-label numerical readings |
| Format intervention, semantic-preservation verification, run-noise comparison, p > 0.34 | §5.2, pp8–9; Appendix C, p18; Table 8, p21 |
| Two fixed skills from strong/weak target experience, six consumers; +1.8/+9.5/−2.0 transfer values | §5.3 prose, pp9–10 (also Figure 4, p10); our numbers come from prose, not chart labels |
| Judge setup: 151 pairs, gap >0.5 pp, nine votes, randomized skill order | §5.2, p9; Appendix E, p20 |
| Judge accuracy 46.4% → 73.8% on the same pairs; rubric discovery and screening | §6, p11; Appendix H.2, p22 |
| Validated rubric's three dimensions | §6, p11; bold entries in Table 13, p23: Failure Mechanism Encoding, Actionable Specificity, High-Risk Action Blacklist |
| Meta-skill average +1.55 pp, plausibility average −0.59 pp, nine-vs-six cell counts | §6, p11; Table 11, p22 |
| Poster chart: validated gains vs Original (ALFWorld +1.00/+0.50/+0.38; SpreadsheetBench +2.33/+3.58/+3.69; SWE-bench +0.38/+1.25/+0.87) | Table 11 delta column, p22; copied as printed, not recomputed from rounded score columns |
| Still below no skill: ALFWorld Qwen 57.21/53.73/54.11; Spreadsheet Gemini 37.50/33.17/36.75 | Table 11, p22; preserve its own row labels |
| Validated not always strongest: SWE Gemini plausibility 70.96 > validated 70.58 | Table 11, p22 |
| Alternative harnesses +0.4 pp overall; target TE −0.5/+2.3/+0.7/−1.0 | Appendix F/Table 10, pp20–21 |
| Hardware but no cost accounting | Appendix B.6, p17; full PDF/appendices checked for token/dollar/time budget |
| Scope: one skill, no large library/retrieval evaluation | Appendix A, p15 |

## ‡ numbers

None. All decimal numbers used in the blogs and poster are printed in the paper's prose or tables. There are no figure-label-only readings and no computed differences. Chart axis ticks are integer scale markers, not additional empirical observations.

## Interpretation and unresolved reporting details

- “All nine improve” refers to Table 11's validated-vs-Original comparison, not validated-vs-No Skill or validated-vs-Plausibility. The ALFWorld Qwen and Spreadsheet Gemini counterexamples are explicitly included in the blogs/poster. The largest validated-vs-Original gains occur on SpreadsheetBench; we do not compute domain averages or claim statistical significance.
- Three independent evaluation runs are explicitly specified for all Table 1 entries in Appendix B.2, p15. Section 6, p11 and Appendix G/Table 11, pp21–22 do not separately specify Table 11’s run/seed aggregation or extractor identity. The Table 1 guarantee is not silently extended to Table 11, nor is Table 11 inferred to be single-run. Repetition of the entire extraction process with independent seeds is not specified. The main matrix and Table 11 lack per-cell SD/CI; Appendix C/Table 8 nonetheless provides round-noise statistics. We do not call the study single-run or say no variance analysis exists.
- The three generic conditions have comparable access to an extracted skill through the unified framework. The no-skill comparator has no extracted skill context. No retrieval library is used in the main experiment, and the paper does not report a matched-extra-compute no-skill comparator or a tuned alternative skill-extraction-method comparison. We make no blanket claim about tool privileges beyond these specified differences.
- Neither the split used to select the Table 7 defaults nor baseline tuning budgets is stated. The main split is for experience generation versus task evaluation; no separate hyperparameter-selection split is documented. Numerical experience-pool sizes, exact per-domain test counts, and library-building/trajectory/rubric costs are also not supplied.
- Rubric discovery uses high-gap pairs from the main cross-matrix, and its dimensions are screened with downstream utilities. Guided judging is evaluated on the same 151 pairs. No independent rubric-design/test partition is described for this analysis or a separately reserved benchmark split for the resulting intervention. Calling this less independent than the initial skill train/test split is our reading of the stated protocol, not a claim of direct answer leakage.
- Tables 2–3, pp16–17 instruct removal of task-specific details, without reported verification of compliance. Prompts explicitly discourage task-specific details; that is a leakage precaution, not a measured overlap or near-duplicate audit. Same-domain related tasks may share operational patterns; no contamination is asserted.
- Table 11's SpreadsheetBench row is labelled only “Gemini”; Figure 5 labels its corresponding row 3.1-Pro. Table 11's no-skill value is 37.50, whereas Table 1's SpreadsheetBench Gemini-3.1-Pro value is 35.83 and Gemini-3.1-Flash-Lite is 25.00. Both Gemini variants and the other Table 1 rows were checked; no matching SpreadsheetBench no-skill row explains 37.50. The precise cross-table alignment remains unresolved. We therefore keep Table 11's Gemini label and its within-table comparisons and do not mix its scores with Table 1's baselines or speculate about a cause. The poster flags the unresolved Gemini/Table 1 alignment.
- Table 8's target roster includes GPT-5.2 and GPT-5.4-nano rather than Table 1's Gemini models. The format-control significance statement is restricted to the six models actually listed in that control.
- We do not repeat the paper's blanket “all-failure pools are consistently worst” claim as our own: the plotted SpreadsheetBench curve has its quarter-success point below its all-failure point. No numerical values are read off that curve; the interpretation is limited to domain-dependent mixtures.
- Figure 1's schematic names Environment/Tool Semantics among the quality principles. The final validated rubric is explicitly specified in §6/Table 13 and includes High-Risk Action Blacklist instead; our method diagram follows the final definition.

## Judgment notes

Published board record: score **65**, band **★★**, evidence level **retained**; latest matching judgment is `research/judgments/b11.jsonl`. No scores or judgments were edited.

- The judgment leaves `variance` unclear. The full PDF explicitly states three-run means for Table 1, and Appendix C/Table 8 quantifies run noise. This is more detail than the condensed judgment captures, although it is not per-cell uncertainty for the main/intervention results.
- `cross_task` is unclear. The PDF reports fixed-skill cross-model transfer on SpreadsheetBench and an alternative-harness check, but not skill transfer across domains. We report the former without upgrading it to the latter.
- `improver_comparison` is yes: original, plausibility-guided and utility-guided extraction are compared. The utility-derived rubric's lack of a described independent development/test split limits how strongly to read that comparison. We retain the board's `retained` level and do not silently re-score it.
- `leakage_guard` is unclear. The prompt-level instruction to remove task-specific details is present, but no measured task-overlap audit is reported. The broader statements in the blogs distinguish this from rubric-selection reuse.
