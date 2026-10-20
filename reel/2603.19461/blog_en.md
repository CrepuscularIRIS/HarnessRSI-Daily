# Hyperagents: an agent that edits its own improver — and what the controls show

*A Reel interpretation of [arXiv 2603.19461v1](https://arxiv.org/abs/2603.19461v1) (HarnessRSI Daily score 74, ★★★). Code: [facebookresearch/Hyperagents](https://github.com/facebookresearch/Hyperagents).*

## What the system changes about itself

A **hyperagent** puts the **task agent** (solves the target task) and the **meta agent** (edits agents) into one editable Python program. The meta agent may rewrite the task agent and also its own code, so the procedure that produces future edits is itself editable. The paper calls this metacognitive self-modification. The starting point is deliberately minimal: the task agent is one foundation-model call, and the meta agent's whole prompt is "Modify any part of the codebase". The instantiation, **DGM-H**, keeps the open-ended archive of the Darwin Gödel Machine (DGM). The original DGM generates its self-improvement instructions with a fixed, handcrafted step; DGM-H removes that step.

## The loop, and the keep/reject rule

1. Sample parent hyperagents from the archive. The sampling weight is a sigmoid of the parent's score (relative to the mean of the top three) times 1/(1 + number of compiled children).
2. The parent's meta agent sees its repository, past evaluation results and the remaining iteration budget, and edits the code.
3. The child is evaluated on training tasks (10 tasks first; the full training set only if it passes that screen). Where a validation split exists, parent selection uses the validation score.
4. Every child that compiles is added to the archive. Parent selection and the evaluation protocol are handcrafted and not modifiable in the main experiments.
5. At the end, the best agent by validation score (training score if there is no validation split) is evaluated once on held-out test tasks.

## Headline result, as reported

Five runs per method, 100 iterations each, median with 95% bootstrap CI. Paper review and robotics are optimised jointly in one run: an agent that fails the staged screen in either domain is zeroed on both, and parent selection uses the cross-domain average. The paper does not say whether the baselines were also run jointly; robotics has no validation split. Test results:

| Domain (test) | Initial agent | DGM-H | Static baseline |
|---|---|---|---|
| Paper review accuracy (100 tasks, GPT-4o evaluates) | 0.0 | 0.710 (CI 0.590–0.750) | 0.630 (AI-Scientist-v2 reviewer) |
| Robotics reward design (torso-height task) | 0.060 | 0.372 (CI 0.355–0.436) | 0.348 (default reward) |

On Polyglot coding (80 iterations, as in the DGM paper), DGM-H goes from 0.140 to 0.340 (CI 0.300–0.380) on the 50-task training subset and from 0.084 to 0.267 (CI 0.231–0.280) on the full benchmark. The paper calls this comparable to the original DGM's 0.140 to 0.380 and 0.142 to 0.307, which are numbers from the DGM paper, not a rerun. The "full benchmark" is described as "largely" unseen tasks (Sec 5.1) and as 165 unseen tasks (Appendix C.1), with 60 training tasks (Table 2).

## The controls that decide whether the gain is real

- **Ablations (same 100 iterations, 5 runs).** Freezing the meta agent (DGM-H w/o self-improve, the paper's ADAS-style replication): 0.0 (CI 0.0–0.130) on paper review and 0.213 (CI 0.180–0.348) on robotics. Removing the archive (w/o open-ended exploration): 0.0 (CI 0.0–0.560) and 0.116 (CI 0.0–0.348). The original coding-tuned DGM: 0.0 (CI 0.0–0.510) and 0.0 (CI 0.0–0.090). DGM-H is reported as significantly better than all three (p < 0.05); with 5 runs per method, the paper does not say what was paired or whether the Wilcoxon test is one- or two-sided (a two-sided exact test on 5 pairs cannot go below p = 0.0625, our inference). The baselines receive the same iteration count; their token cost is not reported.
- **Human-customized baseline.** DGM-custom has an instruction-generation step engineered by hand for each domain: 0.590 (CI 0.570–0.650) on paper review and 0.348 (CI 0.305–0.385) on robotics. DGM-H has the higher median in both, but the difference is not significant (p > 0.05).
- **Transfer of the "improver" (imp@50, Olympiad-math grading, 5 runs).** Run for 50 iterations in a held-out domain, the initial meta agent has imp@50 of 0.0 (CI 0.0–0.130). Meta agents from earlier DGM-custom runs: 0.0 (CI 0.0–0.010). Hyperagents from earlier DGM-H runs on paper review and robotics: 0.630 (CI 0.540–0.630), reported as significantly above the initial agent (p < 0.05; test details unspecified, n = 5). Transfer agents were chosen by how well their descendants improved on the source domain.
- **Compounding.** Over 200 iterations on math grading, DGM-H started from transferred hyperagents reaches 0.640 (CI 0.550–0.720) against 0.610 (CI 0.510–0.680) from the initial agent; the difference is not significant (p > 0.05). Started from the ProofAutoGrader baseline plus a transferred meta agent, the best agent scores 0.700 against 0.670 on the 100-task test set. That is one selected agent, three tasks apart, with no run count, CI or test given, and no control starting from ProofAutoGrader without the transferred meta agent. On the full IMO-GradingBench, accuracy goes from 0.561 to 0.601 and mean absolute error from 0.178 to 0.175; the full benchmark contains the sampled training, validation and test tasks (100 each, Appendix C.4), so the estimate includes tasks used during optimisation.
- **Cost.** About 33M tokens for self-modification plus 0.506M tokens of task evaluation per iteration for a 100-iteration paper-review + robotics run. The paper states a total of roughly 88.6M tokens, but its own components (33M + 0.506M × 100) add up to 83.6M‡. No baseline cost is given.

## Where the gain is absent or small

- **Versus a human-customized improver the gain is not established.** Against DGM-custom the medians favour DGM-H (0.710 vs 0.590; 0.372 vs 0.348) but p > 0.05, and the confidence intervals overlap. Robotics is a single test task, and DGM-H's 0.372 is close to the default reward's 0.348.
- **The initial agent scores 0.0 on paper review because it fails the output format** (no parsing is provided). The static baseline is the more informative reference: 0.710 (CI 0.590–0.750) against 0.630. The interval contains 0.630, and the baseline is a single fixed number with no run variance or significance test. The paper says several top agents, not all, beat it.
- **Coding:** 0.267 on the full Polyglot benchmark against the DGM's reported 0.307, with different starting scores (0.084 vs 0.142); 80 iterations, and the "full" set overlaps the training tasks to some degree (see above).
- **Transfer is shown for one target domain** (math grading, o4-mini as the evaluated model). The two transfer arms differ both in where the agents come from and in the agent-generation procedure. The initial agent's 0.0 is a format failure; the paper attributes the transferred agents' 0.0 (CI 0.0–0.010) to being optimised for other domains and to domain shift. We found no breakdown of how much of the 0.630 is format repair versus grading skill.
- **Compounding is not significant.** The paper itself says so (p > 0.05). The math-grading gain over ProofAutoGrader is small: 0.561 to 0.601 accuracy on a benchmark that includes optimisation tasks, and 0.178 to 0.175 mean absolute error.
- **Modifiable parent selection did not beat the handcrafted rule.** Averaged over paper review and robotics: random 0.428 (CI 0.407–0.432), modifiable 0.491 (CI 0.387–0.512), handcrafted 0.532 (CI 0.384–0.586), not significant (p > 0.05, including modifiable vs random), starting from 0.030.
- **Stated limits:** a fixed task distribution; parent selection and evaluation stay outside the self-modifiable part.

## Our read

HarnessRSI score **74**, band ★★★, evidence level **improver**: the improvement mechanism itself (meta agent editable vs frozen, archive vs none) is varied and compared, and results are reported on held-out test tasks and a held-out transfer domain. The paper reports separate test splits, five runs per method with median and bootstrap CIs, ablations, cross-domain transfer and a token-cost estimate for DGM-H. It does not report baseline token costs (iterations are matched, compute is not stated), a contamination or leakage audit, or a significant advantage over the human-customized baseline. Test splits for paper review and math grading are random samples from the same datasets as training; the robotics test is a different task.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
