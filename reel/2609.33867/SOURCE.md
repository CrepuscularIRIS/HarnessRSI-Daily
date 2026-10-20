# SOURCE — R² Flow: Recursive Self-Improvement via Recursive Skill Evolution

Read from: arXiv 2609.33867v2
Paper figures shown: none

License on arXiv: CC BY 4.0 (figure reuse allowed); we chose not to reuse any paper figure. The method diagram and charts on the poster were drawn by us from the paper's table numbers.

## Where the numbers come from
- Table 1 (headline, p7), setup paragraph (p7), Table 2 (ablations, p8), Figure 4 text/caption (executor transfer, significance, p8), Figure 5 and RQ4–RQ6 text (objectives, edits, harmful skills, p9), Section 4 and Appendices B–C (method, keep rule, pp5–6, 17–20), Appendix E (protocol, 128-record draws, extended analysis, seeds, pp26–27).
- Strongest baseline per dataset on the poster chart = highest value among all eight baseline columns of Table 1 for the primary metric (EM for QA sets).

## ‡ numbers (computed by us)
- 0.78‡ = 100 / 128, points per record on a 128-record dataset (App. E: fixed 128-record draw).
- 3.33‡ = 100 / 30, points per problem on AIME 2026 (all 30 problems).
- 0.93‡ = 84.84 − 83.91 (GPQA, R2 Flow vs FlowSteer, Table 1).
- 1.10‡ = 95.94 − 94.84 (MATH-Hard vs Trace2Skill, Table 1).
- 1.25‡ = 44.22 − 42.97 (SWE-bench vs SkillOpt, Table 1).
- 8.67‡ = 76.00 − 67.33 (AIME 2026 vs SkillOpt, Table 1). 7.36‡ = 61.89 − 54.53 (HealthBench vs SkillOpt).
- 22.28‡ = 8.67 + 7.36 + 2.03 (MBPP+: 91.25 − 89.22) + 4.22 (ALFWorld: 88.75 − 84.53), all vs SkillOpt, Table 1; it equals 4 × 5.57 (the IID accuracy-type average gain, 79.47 − 73.90). 39%‡ = 8.67 / 22.28; 33%‡ = 7.36 / 22.28.
- 31.78‡ = 84.00 − 52.21: mean of the six IID primary values of the R² Flow (Full) row minus the frozen Qwen3.5-9B row of Table 2 (503.98/6 and 313.29/6); the paper's own 13.71 + 18.07 = 31.78 agrees.
- 72%‡ = 433 / 252 − 1 (learner GPU-seconds per step, R² TB vs GRPO, Figure 5a). 24%‡ = 3,121,184 / 2,510,218 − 1 (learner tokens per step, same table).
- 3.2‡ = 100 × sqrt(0.85 × 0.15 / 128): binomial standard error, in points, of one accuracy near 85% on 128 records (our unpaired approximation, not a paper number).
- On the poster only (not in the blogs): "≈5" for the reset-phase-state ablation is the paper's "about five points on both splits" (p9); the poster's 2.6 problems are not used.

## Notes
- Table 1's R2 Flow row equals Table 2's "R2 Flow (Full)" row; the mean of its six OOD primary values is 81.02, equal to the paper's phase-8 value in the RQ6 text. We state this as our reading; the paper does not say in so many words that Table 1 is the phase-8 model.
- "Strongest baseline" in the text of the paper (p7): 2.03 EM and 5.57 accuracy points above SkillOpt (IID); 3.83 EM and 2.85 accuracy points above "the strongest baselines" (OOD); we name Trace2Skill for the 2.85 because Trace2Skill is the highest OOD accuracy-average (75.78) in Table 1.
- Searched the full text including appendices for: limitations section (none found), baseline tuning/evolution budgets (none found), cost of verification/edit steps (none found), contamination audit (none found; Appendix E states the validation set is disjoint from training queries and every evaluation record), what varies across the five runs (not stated), SDs for Table 2 (none).
- The six executor-transfer results are from Figure 4a,d; we quote only text/Appendix E ranges (15.70 to 24.64; r = −0.97).
- The word "injected harmful skills": twelve; construction not described in the main text or Appendix E.

- Table 1's baselines are compared with the "Qwen3.5" direct-answer column in the Δ column; SFT is lower than that column on AIME 2026 (32.00 vs 51.33), HealthBench, MBPP+, ALFWorld and WebShop, so we call it "near the bottom", not the weakest. Averages: EM averages cover two QA datasets each (HotpotQA, TriviaQA; MuSiQue-Ans, NQ-Open); accuracy-type averages cover four (AIME 2026, HealthBench, MBPP+, ALFWorld; MATH-Hard, GPQA, SWE-bench, WebShop).
- The paper writes R² Flow and R² TB with superscripts; the plain-text extraction shows "R2".
- Authorship of comparators (from the paper's reference list): FlowSteer = Zhang et al. 2026d and SkillFlow = Zhang et al. 2026e, both with author lists beginning Mingda Zhang and including Tiesunlong Shen and Xiaoying Tang (2026d also Qika Lin). The paper does not comment on this.
- Baseline SDs of exactly 0.00 in Table 1 include Trace2Skill on AIME 2026, SkillOpt and AFlow on MATH-Hard.
- Edit precision (Figure 5d) is shown for R² Flow (0.89) and the − Verifier ablation (0.43) only; the abstract claims improved library-edit precision over skill-evolution baselines.

## Judgment notes
Our judgment (batch 2026-10-19-a, score 69, ★★, level retained) is broadly consistent with the paper. Three items where the full paper reads differently or needs context; judgment files were not edited:
- `variance: unclear` — Table 1 reports mean ± SD over five runs (and Welch tests, Figure 4b); what varies across runs is not stated, and Table 2 has no SD. "Partial" may describe it better than "unclear".
- `leakage_guard: tested` — the quote cited is about pruning injected harmful skills (a skill-quality test). The paper has no contamination audit of benchmarks; its statement is that the validation set is disjoint from training queries and evaluation records (Appendix E).
- `improver_comparison: unclear` — Figure 5a,b compares six Supervisor objectives inside the framework and Figure 5e compares edit rules on injected skills (share-only, Bayesian-Agent, SkillFlow), so some improver comparison exists, but not against skill-evolution baselines under a matched evolution budget.
