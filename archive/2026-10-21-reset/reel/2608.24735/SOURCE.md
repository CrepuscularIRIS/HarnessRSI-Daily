# SOURCE — Metaⁿ: Recursive Self-Improvement through Emergent Depth

Read from: arXiv 2608.24735v1
Paper figures shown: none

## Source and title verification

The exact-version PDF was downloaded afresh from https://arxiv.org/pdf/2608.24735v1. Leftover facts and drafts were not used. All 22 PDF pages, including appendices A–J, were read through fresh layout/plain text extraction. The PDF title block and rendered result/appendix pages were visually checked.

The PDF renders **Metaⁿ: Recursive Self-Improvement through Emergent Depth**, with a superscript italic n. The listing's **Meta$^n$: Recursive Self-Improvement through Emergent Depth** uses literal LaTeX math delimiters to represent that superscript; there is no substantive title difference. Plain-text extraction collapses the superscript to “Metan”; the blogs use Unicode superscript n and the poster uses a superscript in the header.

Author order copied from the PDF title block (p1): Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa, Dongyeop Kang. Affiliations: University of Minnesota; Seoul National University.

Figure reuse is forbidden for this assignment. No paper image, screenshot, crop or figure is included in the delivered poster. The method diagram, bar chart and ablation table are our own drawings based on the PDF. Code URL: https://github.com/minnesotanlp/meta-n (also printed on PDF p1); no repository code was run or used as factual evidence.

## Claim and number provenance

| Content | PDF source | Qualification preserved |
|---|---|---|
| Fixed Ω; generated pre-process and helper library; same-model solver/improver | §§2.1–2.2 pp4–5; Appendix D p18 | Neither Ω nor model weights are learned; a separate solver stack is improved |
| Archive parent sampling, all nonempty children, archive-best versus single chain | §2.4 pp6–7; Algorithm 1 p19 | Archive-best is defined as the per-task-max search/archive estimator, not one universal chain; no strict improve-only child gate. Mapping to held-out rows is insufficiently specified; S2D tension below |
| Code validation, smoke tests, skipped helpers | §2.2 p5; Appendix D p18 | Architecture/code checks do not prove general safety |
| Stop rules; caps; depths | §2.4 p6; Table 5 p16; Appendix D p18; limitations p13 | Recursion is designed; depth adapts within finite caps; no unbounded compounding |
| Depth-aware summaries and finite context | §2.2 p4; Appendix E.2 p19 | Input formatting partly scaffolds role specialization; not wholly unstructured emergence |
| Gemma CO archive/chain/baselines; GPT CO, S2D, ARC dev (pass@2) rows | Tables 1–2 pp7–8; ARC metric: Appendix C p16 | Main rows mean ± SD over seeds 42/43/44; ARC chain is one seed; test/dev distinguished; ARC is pass@2, not pass@1 |
| S2D archive-best below best chain on both backbones | Table 1 p7: Gemma 0.733 ± 0.015 vs 0.743 ± 0.034; Table 2 p8: GPT-5.2 0.725 ± 0.014 vs 0.734 ± 0.020; definition §2.4 p6 and Algorithm 1 p19 | Published values retained; unresolved held-out-estimator tension, not a proposed cause |
| ARC held-out qualitative success only | Intro p2, §3.3 p11; Table 2 caption p8 | No numerical held-out row or split size located; dev baseline nonzero is not a contradiction of held-out-zero text |
| Missing model/benchmark cells, TB2 baseline omission and category SD | §3 pp7–8; Appendix C pp16–17 | Not all eight families on both backbones; TB2 GPT one seed; no OE/GA TB2 |
| No held-out AE/AlgoTune/SR | §3 p7; Tables 1–2; Table 5 p16 | Benchmark optimization scores, not generalization evidence |
| Gemma CO ablations 0.845/0.825/0.751/0.714; GPT CO 0.886/0.806; GPT AE 0.917/0.759; 72%/15% attribution | Table 3 and §3.4 p12 | Validation scores; no per-row SD/CI in table; percentages quoted, not computed here |
| GPT depth-1 four resamples, 870K tokens, no held-out pass | Appendix C p17 | Full-stack token parity not demonstrated; 0.806 validation differs from same-valued test best chain |
| OE token-capped prompt controls and full-budget 10–20× statement | §3.2 p9; Appendix C p17 | Selected parity conditions, not all-row parity; no OE-with-shared-library experiment |
| Corrected GA and budget sweep 0.502/0.615/0.628, 5.6M/11.4M, Metaⁿ 0.870 at stated 17M | §3.2 p10; Appendix J p22 | GA sweep s42; Metaⁿ cited three-seed mean; not exact token or seed parity |
| Consolidation 0.71 ± 0.02 vs 0.61 ± 0.03, +0.10, 95% CI [+0.04,+0.16], 8 tasks / 3 seeds | §3.3 p11; Appendix G pp20–21 | Frozen non-focus traces produce monotonicity by construction; earlier 6-task pilot not conflated |
| Tuning on 10-task CO pilot, convergence threshold rationale | Appendix D p18; Table 5 p16; baseline configurations p17 | Which split selected defaults is unspecified; baseline settings are given, tuning-search budgets are not |
| Cost 36.1M/5.3M Gemma CO, 29 candidates, approximate 10h/3h CO, 28h TB2, $632 ARC | Tables 5–6 pp16–17, wall-clock p17 | Whole search runs; Gemma s42 Table 6 costs; TB2 dominated by Docker; not a per-query charge |
| Depth regressions −0.006, 41%; per-depth 0.726→0.602 | §3.3 p11 | Descriptive per-depth means and chain/task pairs, not monotone chain improvement |
| S2D overlaps/no significance; diverse-code versus prompt-task contrast | §§3.1,3.3 pp8,11 | Small means do not establish significant gains |
| SR leads every GPT domain | Table 9 p21 | Four-domain comparison, not just one domain carrying all gains |
| AlgoTune ×18.47/×14.11/×15.96, FFT ×9.72→×1.69 and ×4.17→×1.12, convolution ×105.37/×101.79 | Appendix I pp21–22; Table 10 p22 | Seven versus eight task denominator explained; matched seven used on poster; s42 without per-task variance |
| AE pool 15/16/10 | Appendix C p16 | Published explanation of different pools, not an inferred paper inconsistency; no common-subset aggregate supplied |
| SWE-Bench generation-zero result | §3.3 p12 | Three iterations, B=K=2, Ω inactive; bounded diagnostic only |

## ‡ numbers

None. All reported decimal numbers are quoted from the PDF, not newly calculated or read from unlabeled figure coordinates. The poster's bars reproduce Table 2 point estimates; accompanying SDs are table values. No numerical deltas were computed for this interpretation.

## Judgment notes

Local score record: 67, band ★★, evidence level retained. Latest matching judgment found: `research/judgments/b18.jsonl`; no matching later dated judgment was found. It records held_out partial, variance yes, budget_matched yes, optimizer_cost yes, retained_ablation yes, cross_task unclear, improver_comparison no, leakage_guard unclear.

The full-paper reading supports keeping the retained/not-improver boundary: Ω is fixed and the added layers improve solver behavior. The recursive architecture alone is not evidence that Ω becomes a better improver. Descriptive role ratings are not a causal improved-improver comparison. There is no separate oracle/teacher condition to treat as a competitor.

Two qualifications to the record are explicit in the blogs and poster: (1) its supporting ARC held-out quote is qualitative; Table 2 reports dev, and no numerical held-out ARC score was located in the PDF, including appendices. This is an unresolved reporting omission, not an allegation that dev and test disagree. (2) budget_matched yes should be read as the specific OE controls and the small consolidation control, not universal parity: GA's enlarged budget is still below the stated Metaⁿ budget and its sweep is single-seed. Baselines were not separately granted the same shared-library mechanism. No judgments or scores were edited.

Held-out captions exist for CO/S2D/LawBench, but detailed split sizes/construction and the split used to select all defaults are not supplied in the inspected PDF. No dedicated contamination/leakage audit or frozen-artifact cross-benchmark transfer experiment was found. Same-model runs across two backbones should not be described as transfer of a learned artifact between models.

## Independent fact-check follow-up

Both medium findings were independently verified against the original PDF, not adopted solely from the checker. No finding was rejected.

1. **S2D estimator tension:** §2.4 p6 and Algorithm 1 p19 define the search/archive score as the average of per-task maxima over a common archive. For a common set of scored tasks and archive, it cannot be below a constituent chain. Table 1 p7 nevertheless gives held-out Gemma archive 0.733 ± 0.015 below chain 0.743 ± 0.034; Table 2 p8 gives GPT-5.2 archive 0.725 ± 0.014 below chain 0.734 ± 0.020. All other populated archive/chain comparisons in these tables were checked and do not show the inversion. The full PDF's held-out selection/application description does not reconcile this ordering with the search definition. Both blogs now qualify the definition as the search/archive estimator and neutrally disclose the unresolved held-out-estimator tension, preserving all values without speculation. The poster also carries a short caveat. This adds a reporting qualification, not a change to the local evidence-level judgment.
2. **ARC attempt-count metric:** Appendix C p16 explicitly says ARC-AGI-2 is scored pass@2; Table 2 p8 supplies the development values. Both blogs' ARC table labels and following paragraphs, the poster's ARC caption, and the provenance table now identify pass@2. No computation or ‡ marking is needed.

## Production checks

The Python generator adapts the required M⋆ house style and imports the unchanged shared poster library. Body/caption text is at least 22px; SVG method text is enlarged to remain at least 22px after scaling, and chart labels at least 18px. The final render is inspected visually, checked for card overflow and delivered at 2400×1440. `research/check_reel.py` is run against the delivered directory. No external artifact publication, git add, commit or push.
