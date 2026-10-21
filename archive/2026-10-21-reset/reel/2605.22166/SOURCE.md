# SOURCE — Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents (Life-Harness)

Read from: arXiv 2605.22166v3
Paper figures shown: none

License: figure_reuse = true for this paper, but we show none of its figures. The method diagram, the bar chart and the tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from (printed page numbers of the v3 PDF)
- Table 1 (headline, Qwen3-4B-Instruct, p7); Table 2 (frontier models, p7); Figure 5 (gain heatmap over 18 backbones, p7; values also in Table 10, p18); Figure 6 (prompt-only comparison, bar chart without numbers, p7).
- Table 3 and Table 13 (AppWorld, pp8, 21); Table 4 (leave-one-layer-out ablation, p8); Figure 7 (xLAM case study, p8; only the 7.5 pp statement from the text is used).
- Table 5 (train/test sizes, p14); Table 6 (evaluation settings, p14); Tables 7–9 (harness inventory, pp15–17); Table 11 (ALIGN / AgentSquare, p19); Table 12 (per-round accuracy and cumulative evolution tokens, p20).
- Figure 3 and Appendix A.1 (failure diagnosis, 393 failed episodes, LLM annotation with human review, pp4, 11); Appendix A.2 (evolution prompt, accept rule, p12–13); Section 4.4 (loop, p6); Section 5.1 (setup, baselines run under the same conditions, six rounds, identical training batches of up to 50 tasks, p6); Limitations (p9).

## ‡ numbers (computed by us)
- 33.6‡% and 23.2‡% (failure diagnosis): read from the Figure 3 labels (trajectory degeneration 33.6%, action realization 23.2%); the figure text is not in the paper's text layer, so the checker flags them. Confirmed by looking at the rendered page 4.
- −0.8‡ and −0.9‡ (Qwen3.6-27B, Retail and ALFWorld): printed in the Figure 5 heatmap; computed here from Table 10: Retail 0.8417 -> 0.8333 (−0.8 pp), ALFWorld 0.9083 -> 0.8991 (−0.9 pp).
- +18.7‡ (Qwen2.5-72B Airline, Figure 5 label): Table 10, 0.6034 − 0.4167 = 0.1867. +5.7‡ (Qwen3.5-27B DBBench, Figure 5 label): Table 10, 0.7400 − 0.6833 = 0.0567.
All other numbers in the blogs and on the poster are printed in the paper text or tables.

## Notes
- The 8.5% and 68.4% evolution-token savings are the paper's numbers (abstract, p1). We checked that they reconcile with the sums of the round-6 cumulative tokens in Table 12 (Meta-Harness 222.3M, AHE 644.0M, Life-Harness 203.4M); this check is not shown on the poster.
- Table 1 costs are in units of 10^7 evolution-LLM tokens and exclude solver and evaluation usage (Table 12 caption). Life-Harness uses more tokens than Meta-Harness on WebShop (3.8 vs 3.7), Retail (2.6 vs 1.4), Telecom (4.3 vs 2.1) and the tau mean (3.5 vs 3.0); the text claim "fewer evolution tokens in every environment" (p7) is made against AHE.
- Table 4 reports relative drops; the paper does not say whether the ablated variants were re-evolved or whether the layer was removed from the final harness, and gives no SD.
- Table 12 reports accuracy on each round's training batch; the paper does not say which round's harness is the one frozen for the test set (it says "retained harness").
- The 116 of 126 (7 environments x 18 backbones) and 132 of 144 (adding AppWorld: 16 of 18) counts are the paper's; our count of non-improved cells in Figure 5 (8 negative + 2 zero) agrees with 10 of 126.
- Telecom has 40 test tasks and Airline 20 (Table 5); tau tasks are run three times (Pass@1 = single-run success, Pass3 = success in all three), AgentBench tasks once, temperature 0.0 (p6, Table 6).
- Table 13: Qwen2.5-32B-Ins values 15.10 / 20.40 are not multiples of 1/57 (the AppWorld test set has 57 tasks); we use the table values as printed.
- Table 11: ALIGN follows its released task split and AgentSquare uses the Life-Harness task selection (caption); these baselines were not re-evolved under the Table 1 conditions. WebShop rows where Life-Harness is not strictly highest of the three: Qwen3.6-27B (43.00 vs AgentSquare 47.00), Llama-xLAM-2-70B (42.00 vs 50.00), Qwen3.5-35B-A3B (tie at 43.00).
- The failure-diagnosis percentages (33.6, 33.3, 23.2, 9.9) are read from the Figure 3 labels.

- Figure 6 (prompt-only evolution) has no numbers; the blogs' description (prompt-evolving roughly level with or below the unmodified model on ALFWorld, OS, WebShop and above it on DBBench, Airline, Retail, Telecom) is read from the bar heights and is approximate. The paper's text says prompt optimization "improves accuracy over the baseline".
- Table 12 observations used in the blogs: Meta-Harness Airline training-batch accuracy 30.00 in all six rounds (test 11.7 vs 35.0 unmodified, Table 1); AHE Retail training-batch accuracy 50.00 at round 3 and 20.00 at round 6 (test 45.8). Batches differ per round, so these are not a like-for-like curve; we state only that the paper does not say which round's harness is evaluated.
- Table 10, Qwen2.5-72B Airline with Life-Harness 0.6034 is not a multiple of 1/60 (20 tasks x 3 trials).
- AHE was designed for coding-agent harnesses (related work, p3); Meta-Harness and AHE are the authors' runs of open-source implementations (§5.1).
- App B (p13): "Each evolution round uses a batch of up to 50 tasks drawn from this subset"; the next round uses a new batch after a rejection (§4.4). The train subsets are 100 / 100 / 100 / 100 / 30 / 74 / 74 tasks, so six batches of 50 cannot all be disjoint; the poster says "up to 50 training tasks per round".
- The paper reports one harness per environment and never says whether evolution was run once; the blogs say "no repeated runs reported".

## Judgment notes
Our judgment (batch b05, v3): score 72, evidence level retained. Consistent with the full paper on `held_out: yes`, `cross_task: unclear` (each environment is evolved separately; only cross-model transfer is tested), `variance: unclear` (no seeds, SD or CI anywhere), `optimizer_cost: yes`, `retained_ablation: yes`, `leakage_guard: untested` (the evolution prompt tells the LLM not to read test trajectories, but no audit is reported; train and test splits are disjoint per Table 5). Two points to read carefully, no judgment file edited:
- `budget_matched: yes` rests on identical rounds and training batches (six rounds, up to 50 tasks); evolution tokens are not matched (Table 12: AHE about three times Life-Harness's total), and no tuning budget or repeats are reported for the baselines.
- `improver_comparison: unclear`: Table 1 compares against two other harness-evolution methods under the same rounds and batches, but the paper has no ablation of its own accept/reject rule or evolution step.
