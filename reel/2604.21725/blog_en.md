# AEL: a bandit chooses how an agent retrieves memory, an LLM reflection adds new retrieval policies — and what the controls say

*A Reel interpretation of [arXiv 2604.21725v2](https://arxiv.org/abs/2604.21725v2) (HarnessRSI Daily score 74, ★★★). Code: [WujiangXu/AEL](https://github.com/WujiangXu/AEL).*

## What it changes about itself

AEL (Agent Evolving Learning) keeps the LLM frozen and learns the **memory-use part of the harness**. In the default configuration the planner and the 12 tools are fixed; three things are learned online:

1. a Beta posterior over a pool of **memory-retrieval policies** (which memory tiers are visible, how many entries, in what format), updated by Thompson Sampling after every episode;
2. a **reflection insight** (a causal explanation of why the last window went well or badly, plus a regime label) regenerated each slow window and put into the planner prompt;
3. **procedural rules** promoted from recurring semantic patterns in a three-tier memory (episodic, semantic, procedural).

## The loop, and the keep/reject rule

- **Fast timescale.** Each episode, sample from every policy's posterior and play the highest sample. The episode score s in [−1, 1] is mapped to a reward in [0, 1] and added to the chosen policy's Beta posterior (uniform credit).
- **Slow timescale.** After each slow window an LLM reads per-ticker summaries, per-tool accuracy, market side information that the predictor does not see, and its last three reflections, and writes the insight.
- **New arms.** Every 5 slow windows after window 10, and only if the mean Thompson Sampling reward over all policies is below 0.4, the LLM designs a new retrieval policy. The paper's example artifacts were validated by AST parsing (Appendix P.2; the syntax-and-smoke-test gate in Section 3.4 is stated for LLM-written planner classes) and joined the bandit as a new arm with a uniform Beta(1, 1) prior; the posterior then decides how often the arm is used. Appendix P.2 says such artifacts were "accepted into the module pool by LinUCB", although LinUCB is described only for planner selection.
- **Evaluation.** Episodes are split chronologically into train / validation / test; posteriors are selected on validation and frozen. At test time bandits are frozen, memory is read-only and nothing evolves. The task agent is Claude Haiku 4.5.

## Headline results, as reported

**Portfolio benchmark (D-full).** 10 equities, 208 hourly episodes: 140 train, 40 validation, 28 test; the test window is a bear-to-bull transition. Five seeds, mean ± SD of the test-phase Sharpe ratio (Table 2a):

| Method | Sharpe |
|---|---|
| **AEL** | **2.13 ± 0.47** |
| +Memory (bandit, no reflection) | 1.68 ± 0.96 |
| Momentum-weighted (non-LLM, deterministic) | 1.44 |
| EvoTool | 1.37 ± 1.74 |
| Stateless | 1.35 ± 1.03 |
| FactorMiner / ExpeL / HyperAgent | 0.85 / 0.76 / 0.72 |
| Meta-Reflection / Reflexion | 0.20 / −0.59 |

AEL also has the best Sortino (4.08) and Calmar (10.40). The abstract's "+27%" is 2.13 against the memory-only variant 1.68.

**Support-ticket routing.** An LLM-generated stream with four regimes (the last is a route-aware regression); Gemini 3.1 Flash-Lite, 160 stratified episodes per seed, five seeds (Table 2b): AEL 0.840 ± 0.031, bandit without reflection 0.711 ± 0.039, strongest prior baseline (FactorMiner) 0.557 ± 0.037. In the last regime AEL reaches 0.885 against 0.705 for the best prior baseline (ExpeL); the bandit without reflection already scores 0.685 there, and AEL's gain over it also appears in the other regimes (R1/R2: 0.590/0.585 to 0.775/0.715; the paper says the gain is "not only in the route-aware regime").

## The controls that decide whether the gain is real

- **Component ablation (Table 3, five seeds, no SDs given).** Removing reflection gives 1.68; removing the 15-episode warm-up gives 1.25. Every addition lowers the score: cold-start priors 0.82, planner evolution 0.41, per-tool selection 0.43, skill extraction 1.02, factored credit 1.04, LLM credit 1.49. The paper's conclusion is that the simplest configuration is the best one in this short-horizon, noisy setting.
- **Is the reflection text what matters? (Appendix A.2.)** Replacing each window's reflection with one shuffled in from another window gives Sharpe 1.54 ± 0.71 against 2.13 ± 0.47. The paper reads this as content, not extra context. No significance test is reported for this comparison, and the two SDs are large. On seed 42, 40 of 49 LLM regime labels (82%) match a deterministic rule (chance about 39%).
- **Single fixed policy plus reflection (Table 7).** The best fixed policy gives 1.44 ± 0.71, so AEL's bandit-plus-reflection is at least 0.69 Sharpe ahead of every single-policy variant. But none + reflection scores 1.41 against Stateless 1.35, and +Memory (bandit, no reflection, 1.68) is above every fixed-policy-plus-reflection variant, so the tables do not by themselves isolate reflection as the driver; the paper reads the bandit as the substrate that lets injected arms enter the pool. A counterfactual replay on training reward (Table 6) shows Thompson Sampling (0.490) close to round-robin (0.490), UCB1 (0.494) and epsilon-greedy (0.516), while the best fixed policies (compressed 0.523, recent_window 0.514) are above it; the end-to-end swap of the bandit with reflection kept on was not run (Appendix B).
- **How often are new arms injected in finance?** Not reported. The evidence is the seed-42 trace (Section 3.5, Appendix S) and a seed-123 example (Appendix P.2). The slow-window size for the finance runs is not stated, there is no ablation separating injected arms from the insight text, and per-seed Sharpe values for AEL are not listed (only for baselines, Appendix J.1).
- **Significance (Table 5, five seeds).** Welch tests on mean Sharpe: AEL is above Reflexion (p = .008), Meta-Reflection (.017) and HyperAgent (.001), but not significantly different from EvoTool (.393), +Memory (.384), ExpeL (.190), FactorMiner (.066), Stateless (.178) or +Tools (.200). The F-test for lower variance is significant against ExpeL (.018) and EvoTool (.027) only, and HyperAgent's SD (0.38) is lower than AEL's (0.47); the paper itself calls variance reduction the robust finding. The printed 95% interval [1.72, 2.54] matches mean ± 1.96‡ × SD/√5, a normal rather than a t interval for five seeds (our check, SOURCE.md). Nine Welch tests are reported and no multiplicity correction is mentioned; at a threshold of 0.05/9 the Reflexion result (p = .008) would not pass.
- **Same mechanism for the baselines?** No. The baselines are the authors' adaptations of Reflexion, ExpeL, Meta-Reflection, FactorMiner and EvoTool to the same backbone, tools and data split; none has a bandit over retrieval policies or arm injection. Appendix K describes a tuned HyperAgent (20 generations instead of 10, real tool schemas) that scores 0.46 ± 0.41, not the 0.72 ± 0.38 of Tables 2a and 5; the paper does not say which version the Table 2a row is. Tuning budgets of the other baselines are not stated, and no matched-budget row is reported. Appendix B notes that the same configuration name takes different values across result blocks (different reflection budgets, cadences, pre-fix and post-fix credit code), so same-protocol runs for every row cannot be confirmed from the paper.
- **Cost and transaction costs.** Appendix E gives about $2.80 per full AEL run (about $2 predictions, $0.80 reflection and evolution). Separately, Table 16 lists "evolution cost" as about 400 LLM calls for AEL against about 20 for HyperAgent. Baseline costs are not reported. The headline numbers assume zero transaction cost (Appendix R); the paper's approximate cost-adjusted Sharpe at 20 bp is about 1.3 for AEL, 1.0 for the momentum baseline and 0.7 for EvoTool.
- **Other domains are mechanism checks.** A synthetic 10-arm bandit with a hidden 11th arm that only "reflection" can add: AEL reaches 0.452 in the regime where the arm pays, pure Thompson Sampling 0.359; overall 0.400 vs UCB1's 0.402 (AEL's regime-3 SD is 0.104, Table 12). The arm injection there is scripted, without an LLM. Every domain is learned from scratch; no evolved artifact is transferred.

## Where the gain is absent or small

- **No lift when the best policy is stable.** On a 20Newsgroups stream AEL scores 0.253 and Thompson Sampling without reflection 0.254 (p = 0.97); the paper reports it as a "no-harm/no-gain" boundary case. The text names fixed *compressed* (0.267) as the best fixed policy; Table 10 lists fixed *full_detailed* at 0.271.
- **Mean gains over the strongest comparators are not significant** (EvoTool, +Memory; see above), and reflection's +0.45 over +Memory is within the seed spread (0.96 vs 0.47 SD).
- **Not best on every metric.** Maximum drawdown: EvoTool −1.46 and equal-weight −1.47 are better than AEL's −1.53. The deterministic momentum baseline (1.44) beats every prior LLM method on Sharpe and has no significance test against AEL. The abstract's "lowest variance among all stochastic methods" does not hold in Table 2a, where HyperAgent's SD is 0.38 (the figure caption restricts the claim to LLM methods with mean Sharpe above 1.0).
- **Routing: a stronger no-learning row.** The fixed class-balanced policy (0.565) is above every prior baseline (best 0.557). In the paper's deterministic version of the stream the last regime needs a retrieval policy that is not in the initial pool (bandit without reflection 0.206, AEL-style 0.863, Table 11); in the LLM-agent run of Table 2b the bandit without reflection already scores 0.685 in that regime and ExpeL 0.705.
- **Short, single test window.** 28 test bars from one bear-to-bull transition; the authors say absolute magnitudes should be read as benchmark-specific, and that coding and web benchmarks are the next step.
- **Inconsistencies inside the paper** (we use Table values): HyperAgent is 0.72 ± 0.38 in Table 2a but 0.46 ± 0.41 in Appendix K and Table 16; the text says "4 of 9" mean comparisons are significant but names three, and Table 5 shows three; LLM-credit is 1.37 in the text, 1.49 in Table 3, and −0.53 after a credit-code fix described in Appendix H (FCC: 1.04 in Table 3, −0.07 post-fix), although Appendix J.3 says Table 3 already uses post-fix code; Section 4.1 and Appendix E say the matched incremental build uses three seeds while Table 2 says five; the appendix text calls the shuffled-reflection result (1.54) "marginally better" than +Memory (1.68), but 1.54 is lower.

## Our read

HarnessRSI score **74**, band ★★★, evidence level **improver**: the learning mechanism itself (bandit over retrieval policies, reflection, new-arm injection) is varied and compared, on a chronologically held-out test window. The paper reports a held-out split, five seeds with SDs for the main comparison, component ablations including a shuffled-reflection control, and the cost of an AEL run. It does not report a budget-matched comparison against the baselines, a test of a retained artifact on a different task, a leakage test (it argues contamination is symmetric because all methods share one backbone), or per-baseline costs. The finance result is a mean gain on a 28-bar test window: AEL's own seed SD (0.47) is the smallest among LLM methods above Sharpe 1.0, while the comparators' spreads (EvoTool 1.74, +Memory 0.96) are large and keep most mean differences non-significant; the routing result is larger but comes from a generated stream designed around a late regime.

*All numbers are printed in the paper except the 1.96‡ in the interval check. Counts such as "three of nine" are read off Table 5; see SOURCE.md.*
