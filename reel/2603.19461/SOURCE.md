# SOURCE — Hyperagents (HyperAgents, Zhang et al.)

Read from: arXiv 2603.19461v1
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but no paper figure is shown. The method diagram and the charts on the poster were drawn by us; every plotted value and CI whisker is a number stated in the paper text (not read off the figure).

## Where the numbers come from (PDF pages)
- Method, keep rule, fixed outer loop: Sec 3 (pp4-5), Appendix A.1-A.3 (pp22-23, parent-selection formula, Algorithm 1).
- Baselines (DGM-H w/o self-improve = ADAS-style, w/o open-ended, DGM, DGM-custom): Sec 4.1 (p6), Appendix B (pp24-28).
- Splits: Table 2 (p28) and C.1-C.4; models: Table 3 (p35).
- Headline and controls (paper review, robotics, Polyglot, CIs, p-values): Sec 5.1 (pp7-9), Figure 2 (p8; values taken from the text, not the bars).
- Transfer / imp@50: Sec 5.2 (pp9-12), Figure 3 (p10), Appendix D.3-D.4 (pp36-37).
- Compounding and ProofAutoGrader: Sec 5.3 (pp12-13), Figure 4 (p13), Appendix E.4 (p56).
- Cost: Appendix D.2 (p35). Modifiable parent selection: Appendix E.5 (p57). Limitations: Sec 7 (p14).

## ‡ numbers (computed by us)
- 83.6M‡ = 33M (self-modification, 100 iterations) + 0.506M × 100 (evaluation), from Appendix D.2 (p35). The paper states the total as "approximately 88.6M tokens"; its own components sum to 83.6M. We report both and flag the paper-internal inconsistency; we do not know which figure is intended.
Every other decimal in the blogs and on the poster occurs in the paper text.

## Notes
- Chart whiskers are the 95% bootstrap CIs given in the text. The initial agent has no CI in the paper; "Initial" bars show 0.0 (paper review) and 0.060 (robotics).
- DGM numbers on Polyglot (0.140 to 0.380 train subset; 0.142 to 0.307 full) are quoted by this paper from the DGM paper, not re-run.
- Not verifiable from the paper: token cost of the baselines (only DGM-H's ~33M self-modification + 0.506M/iteration evaluation tokens are given); a contamination/leakage audit (none found in the appendix); the Wilcoxon test details; any breakdown of how much of the transfer result (imp@50 0.630) is output-format repair versus grading skill.
- The two transfer arms (DGM-custom sources + DGM w/o self-improve; DGM-H sources + DGM-H w/o self-improve) differ in agent-generation procedure as well as source run type (pp9-10); we state this on the poster rather than call it a single-factor control.
- Table 2 gives robotics train/test as 6 / 6 (repetitions of one training task and one different test task); the "1 test task" on the poster reflects the single torso-height task described on p7 and in C.3.
- Significance tests: the paper reports p<0.05 / p>0.05 from a Wilcoxon signed-rank test with 5 runs per method (p7) and does not say what was paired or whether it is one- or two-sided. That a two-sided exact test on 5 pairs cannot go below p = 0.0625 is our inference, not a statement of the paper.
- Paper review 0.710 (CI 0.590-0.750) vs static baseline 0.630: the CI contains 0.630; the baseline is a single dashed line in Figure 2 (pp8-9) with no run variance or test.
- Full IMO-GradingBench (0.561 -> 0.601, MAE 0.178 -> 0.175, Appendix E.4 p56): Appendix C.4 describes 100/100/100 train/validation/test tasks sampled from the benchmark, so the full-benchmark estimate includes tasks used in optimisation (the paper does not discuss the overlap). The Figure 10 confusion-matrix cells sum to 1000 items per grader (our count). The 0.700 vs 0.670 test comparison is one selected agent, 3 tasks out of 100, with no run count, CI or test, and Figure 4 has no control for DGM-H from ProofAutoGrader without the transferred meta agent. E.4 prints "+4.06%" accuracy gain while 0.601 - 0.561 = 0.040; not used.
- Polyglot (p7): "same number of 80 iterations" as the DGM (other experiments: 100). The "full benchmark" is called "largely" unseen (p7) and "165 unseen tasks" (C.1, p29), while Table 2 lists 60 train and 165 test tasks; wording differs on whether the training tasks are included.
- Parent-selection numbers (random 0.428, modifiable 0.491, handcrafted 0.532, initial 0.030; E.5 p57) are averages over paper review and robotics; modifiable vs random was also not significant (p>0.05).
- Joint optimisation: paper review and robotics are optimised jointly in one run (staged-evaluation failure in either domain zeroes the agent on both; parent selection uses the cross-domain average; p8, A.4 p24). The paper does not say whether the baselines were also run jointly; robotics has no validation split (p7).
- Transfer start scores: for the INITIAL agent the paper attributes 0.0 to missing output parsing (p8 paper review, p10 math grading). For transferred agents it gives other reasons: 0.0 (CI 0.0-0.010) "because the agents were optimized for paper review and robotics reward design" and "reflecting the domain shift" (p11). We found no breakdown of format repair vs grading skill in the 0.630.
- Wording "improver" etc. follows docs/EVIDENCE.md; poster text avoids claims beyond the paper's controls.

## Judgment notes
Our judgment (research/judgments/pilot.jsonl) is `variance: unclear`. The full paper runs every method 5 times and reports medians with 95% bootstrap CIs and Wilcoxon tests (p7), which looks closer to `variance: yes`. It also has `budget_matched: unclear`: iterations are matched (100 per method; 50 for imp@50) but token cost of baselines is not reported, so `unclear` is consistent. `leakage_guard: unclear` is consistent (separate test splits, but no contamination audit). No judgment file was edited.
