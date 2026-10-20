# SOURCE — ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement

Read from: arXiv 2609.14857v2
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram and charts on the poster were drawn by us from the paper's table numbers; no figure from the paper is shown.

## Where the numbers come from
- Method and keep/reject rule: §3.2 to §3.7 (pp4-5); schedule and evolution data §5.3 (p6); dataset construction §4 (pp5-6); Appendix F (p17, baseline protocol, web search disabled), Appendix J.3 (p22, diff-review prompt).
- Table 1 (headline and cross-benchmark transfer, p7); Table 2 (cross-model, p7); Table 3 (modular vs joint / non-modular, matched 16 epochs, p8); Table 4 (single-module evolution, p8); Table 5 (ablation CTA / FLM / VG, p8); Table 6 (Meta-Harness and AHE, p9); Figure 2 (scaling, p9; only the labelled values 47.6 and 57.3 are used); Table 8 (other evolution models, p15); Table 9 (paired bootstrap CIs, p18); Table 10 (difficulty distributions, p19); Figure 6 and Appendix M (evolution curve, p27; only the labelled endpoint 52.2 is used); Appendix K caveat sentence (p27).
- Poster chart "Headline" plots the six Table 1 columns (TB 2.0 and SWE-Bench-Verified: Acc, Pass@3, Pass^3) for no evolution, other-family evolution and same-family evolution. "Same family" = TB-related set evaluated on TB 2.0, SWE-related set evaluated on SWE-Bench-Verified, as labelled "In-Domain" in Table 1.
- Poster bar labels "(+4.86)", "(+1.87)", "(+2.24)", "(−1.13)", "(−3.38)" are the Δ accuracy values printed in Table 9 (c) and (d).

## ‡ numbers (computed by us)
- 2.62‡ = 52.43 (ModularRSI) − 49.81 (AHE), Table 6. 2.99‡ = 52.43 − 49.44 (Meta-Harness), Table 6. (2.62 also happens to be the upper CI bound printed for AHE's gain in Table 9c; the two are unrelated.) Used in the blogs only; the poster states the raw values 49.44, 49.81 and 52.43.

- 47.6‡, 57.3‡ and 52.2‡ (blogs; 52.2 also on the poster) are not computed: they are the labels printed inside Figure 2 (p9: baseline 47.6, 600-task point 57.3) and Figure 6 (p27: final-generation accuracy 52.2). They do not occur in the paper's extractable text, so they carry ‡ for the checker; they were read by us from the figure images (not recomputed, not from the code repository). The other points of Figure 2 and Figure 6 are unlabelled and not used.

- 7‡ = 140‡ − 133‡ successful rollouts of 267 (89 TB 2.0 tasks × 3 rollouts): 52.43% × 267 = 140.0, 49.81% × 267 = 133.0. Used in blogs and on the poster to express the ModularRSI-vs-AHE gap in rollouts. 1.13‡ = 65.17 (ModularRSI Pass@3) − 64.04 (non-modular Pass@3), Table 3.
- 2.62‡ also equals the Table 5 gap 52.43 − 49.81 between the full system and "w/o FLM"; the paper does not comment on this numerical coincidence with AHE (49.81), and we do not claim a causal link.

## Notes
- "Budget matched" is stated by the paper in epochs: joint and non-modular evolution, Meta-Harness and AHE were each run for 16 epochs, equal to 5 modules × 3 epochs + 1 integration epoch (§6.3, App F). The paper reports no evolution tokens, dollars or wall-clock (only a 2M tokens-per-minute rate limit and batch size 10, §5.3).
- Meta-Harness and AHE are the authors' adaptations/reproductions in Harbor (App F). Tuning budgets and variance for them are not reported; whether Meta-Harness and AHE were given the Task-Aware Function Composer, Function Merge or ModularRSI's validation gates is not stated in the paper (each ran its own pipeline). This matters because Table 5's "w/o FLM" (function-library management = Function Merge + Task-Aware Composer, §3.7, §6.4) scores 49.81, numerically equal to AHE's 49.81. The composer is an LLM call at test time; the paper does not name its model (including for GLM-5.2 / MiniMax-2.5 in Table 2) or report its cost. The poster and blogs flag this as an open confound.
- Table 9 CIs are task-level paired bootstrap intervals (100,000 resamples): each task's three runs are averaged and kept together, and only tasks are resampled (App G, p18), for a fixed harness evaluated three times. The paper reports no repeated evolution runs, so they do not reflect variation between evolution runs. Table 9 gives no CIs for the ablations (Tables 4-5), scaling (Fig. 2), difficulty (Table 10) or evolution-model (Table 8) results, and no direct CI for ModularRSI against Meta-Harness or AHE. The CIs for Meta-Harness [-0.07, 2.24] and AHE [-0.03, 2.62] include zero.
- Table 8 baselines differ by model (47.57, 61.79, 61.05) because each is the same model without evolution; it is not a comparison across models.
- Figure 6 ends at 52.2 on accuracy at the last generation (22) while Table 1 / Table 5 list 52.43; the paper does not explain the difference. We state it as an observation.
- Web search: App F (p17) says it was disabled "for all methods" in the comparison with Meta-Harness/AHE. Table 6's ModularRSI row (52.43) equals the Table 1 headline; the paper does not say whether Table 1 was also run with web search disabled.
- Table 10 vs Table 1: Table 10's Medium-centered 76.40 equals the Table 1 SWE-related (in-domain) headline 76.40; the Hard & Easy variant gives 74.20. The paper does not say whether the headline harness was selected from these two variants; Figure 5 (p19) covers epochs 0-2 only. We state the identity and that selection is not stated.
- Table 3 is accuracy-specific: joint and non-modular evolution are below the no-evolution harness on accuracy and Pass^3 (24.72 vs 30.34) but above it on Pass@3 (61.80 and 64.04 vs 58.43); non-modular uses fewer steps (29.03 vs 34.70; ModularRSI 35.57).
- Figure 6 (p27) runs to generation 22 while the method and all comparisons count 16 epochs (3 per module × 5 + 1 integration); the paper does not explain the generation count. The text (p7) says "largely monotonic"; the curve has a dip near generation 12. Table 9 intervals are strongly asymmetric around the point estimates (e.g. +1.87 [1.49, 5.24] vs +1.87 [-0.07, 2.24]; +4.86 [3.37, 9.36]); reported as printed. ModularRSI's own intervals (+4.86 [3.37, 9.36], +3.00 [1.06, 4.26]) lie above the baselines' printed upper bounds (2.24, 2.62), but the paper runs no direct test.
- The 120 + 120 tasks are two separate evolution sets, each producing its own harness (TB-related, SWE-related), not 240 tasks in one run.
- Leakage: the paper's measures are construction guidance at category level, manual review, "LLM-based semantic similarity screening", and web search disabled in the comparison with other methods. We found no overlap statistic, threshold, number of removed instances or pretraining-contamination discussion in the paper or appendices.
- Appendix K (p27) says the case-study runs "contain other updates, so the comparisons do not isolate the effect of a single change".
- The paper has no Limitations section; the "does not report" list on the poster is our reading of what the tables contain.
- The 2,000-task pool (1000 SWE-type, 1000 terminal-type, Fig. 4) is described in the paper; only 120 + 120 are used for evolution, and how the 120 were chosen is not stated beyond computational constraints.

## Judgment notes
Our judgment (batch b06, score 72, evidence level `retained`) is mostly consistent with the full paper, with two points the full text may support differently:
- `variance: unclear`: the paper does report task-level paired bootstrap CIs (Table 9) and three rollouts per task, but no repeated evolution runs or seeds. We therefore say on the poster that variance across evolution runs is not reported and that CIs cover tasks only.
- `improver_comparison: unclear`: the full paper compares ModularRSI against joint and non-modular evolution (Table 3) and against Meta-Harness and AHE (Table 6) at matched epochs, and ablates the gates, contrastive analysis and library management (Table 5). This looks like improver-level evidence that the condensed text cut; the paper does not report evolution cost or repeat the evolution, so we leave the evidence-level call to the maintainers.
- `budget_matched: partial` and `leakage_guard: untested` agree with the full text (epochs matched, tokens/cost not reported; similarity screen without statistics). `optimizer_cost: unclear` agrees (no cost reported).
No judgment file was edited.
