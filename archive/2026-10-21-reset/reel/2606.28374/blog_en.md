# RSEA: evolve the context, select on validation — but the safety guarantee stops there

*A Reel interpretation of [arXiv 2606.28374v1](https://arxiv.org/abs/2606.28374v1), by Michael Nguyen, Quoc Nguyen and Paul Vuong (Monash University Malaysia). HarnessRSI Daily score **67**, ★★. Code: announced in the paper; no code URL supplied in our record.*

## What the system changes about itself

RSEA keeps a **strategy, skills and playbook** as natural-language state. The strategy supplies high-level instructions, skills supply reusable conditional rules, and the playbook supplies procedures distilled from successful trajectories. The state is injected before a task in a standard ReAct loop. The model weights and action/tool interface stay fixed; the same frozen LLM performs tasks and rewrites the state.

## The loop, and the keep/reject rule

1. Start with an empty working state and empty best state: vanilla ReAct.
2. Roll out the working state on an **evolve set**. Give the rewrite model the current state and a balanced sample of successful and failed trajectories, including verified outcomes. It may rewrite or drop any layer.
3. Evaluate the candidate on a **disjoint validation set**. Adopt it as the working state if its validation score is at least the current working state's score; otherwise keep the working state unchanged.
4. Update the frozen best state only on a **strict improvement** over its previous best validation score. Ties can advance the working search but cannot replace the frozen best.
5. Evaluate only the frozen best on a separate test set. If nothing strictly improves over the empty state, return empty-state ReAct. RSEA+retry adds the same kind of within-task Reflexion retry used by the retry comparators.

Here, validation is held out **from the rewrite trajectories**, but its scores repeatedly gate adoption. Adopted working candidates do not regress on that selection metric by construction; this is not independent generalization evidence. The separate test split supplies that evidence. The guarantee is about validation, **not every unseen test draw**, as the authors explicitly acknowledge in §10.

For ALFWorld, a disjoint 30-task development pool is separate from 134 test tasks. For the tool-use benchmarks, the authors judged official development data saturated and made disjoint evolve/validation/evaluation slices from a seed-shuffled test pool. These are within-benchmark splits, not demonstrated distribution-shift transfer. The backbone and ReAct scaffold are shared within each benchmark; each benchmark has its own evolution. The paper does not report transferring one benchmark's frozen state to another. Exact evolve/validation sizes and episode-reset details are not printed.

## Headline result, as reported

ALFWorld uses **Qwen2.5-7B-Instruct, 134 tasks and five seeds**. Table 2 reports means ± 95% confidence intervals, not a best-seed result:

| Method | Single-pass success (%) | With retry (%) |
|---|---:|---:|
| ReAct / Reflexion | 64.6 ± 4.3 | 76.4 |
| GEPA | 63.9 ± 5.3 | 75.8 ± 5.4 |
| AWM | 65.4 ± 3.3 | — |
| ACE | 66.9 ± 2.5 | 76.7 ± 4.9 |
| Dynamic Cheatsheet | 70.7 ± 3.4 | — |
| RSEA | 69.3 ± 9.3 | 79.4 ± 7.4 |

RSEA improves over ReAct in the reported paired McNemar test (**p=0.015**), also over GEPA (p=0.004) and AWM (p=0.037). It is not significantly different from ACE (p=0.20) or Dynamic Cheatsheet (p=0.45). Its large individual confidence interval does not invalidate the paired test, but should remain visible. Retry gives the highest reported mean, yet the comparisons with Reflexion (p=0.09), ACE+retry (p=0.13) and GEPA+retry (p=0.052) do not establish significant superiority.

**Ranking wording needs qualification.** The text and captions call RSEA the strongest single-pass method, but the explicitly single-pass Tables 2 and 4 put Dynamic Cheatsheet at 70.7 and RSEA at 69.3. Checking retry variants and the other tables does not resolve that wording; §6 itself reports the nonsignificant comparison. We use the table ranking and leave the wording discrepancy unresolved.

## The controls that decide whether the gain is real

- **Layer ablation (Table 5).** On 54 ALFWorld test tasks × three seeds, with temperature 0.6, empty-state ReAct scores 64.2; strategy alone 67.3; skills alone 69.8; playbook alone 69.8; strategy+skills 67.9; full state 68.5. The layers overlap: the full combination does not beat the best individual layer. These are averages without per-cell variance/CI, under a different protocol from Table 2.
- **Selection ablation (Table 6).** Selecting on the evolve set itself yields **100.0 in-sample, 66.7 test**; independent-validation selection gives **67.3 test**, against empty-state **63.6**. The paper's 33-point drop is the in-sample–test gap, **not** a 33-point penalty relative to the gated method. The table gives no variance or exact task/seed count; §8 describes multi-seed decoding generally. The controlled test difference is modest, and uncertainty is unreported.
- **Same mechanism for baselines?** GEPA already uses validation-minibatch Pareto selection, and ACE validation keep-best with non-strict updates (Table 1). AWM and Dynamic Cheatsheet retain their native ungated mechanisms. No experiment gives RSEA's strict gate to every baseline. Dynamic Cheatsheet's WebShop collapse is therefore not an isolated, same-method gate ablation.
- **Budget and tuning.** The authors state equal per-method rollout budgets and shared backbones/decoding budgets. This is partial budget matching: meta calls and injected context still differ. Best-state selection uses validation; the split used to choose hyperparameters/defaults, baseline tuning budgets, exact per-method rollout counts and retry limits are not reported in the PDF, including Appendix B.
- **Cost (§9).** Each generation includes evolve rollouts, one rewrite and validation rollouts; the τ-bench run used **190 meta+selection calls**. Inference adds at most a few hundred preamble tokens. No per-method dollar/token/wall-time cost table demonstrates equal total compute.

## Where the gain is absent or small

The gain is concentrated on **ALFWorld with the smaller backbone**, especially procedural families (Table 3): examine **6.7 → 26.7**, pick_two **36.5 → 43.5**, pick_and_place **82.5 → 91.7**. Heat **76.5 → 79.1** and cool **81.0 → 83.8** move less; clean regresses **80.0 → 73.5**, and even retry's **79.4** remains below ReAct on clean. Family counts are not supplied, so their weighted reconciliation with the overall mean cannot be checked from the PDF.

The other benchmarks use **Qwen3-30B-A3B-Instruct** (Table 4):

| Evaluation | ReAct | RSEA | Strongest reported baseline |
|---|---:|---:|---|
| GAIA, 30 text tasks, accuracy % | 16.7 | 13.3 | ReAct 16.7 |
| τ-bench retail, 60 tasks, success % | 41.7 | 40.0 | AWM 51.7 |
| WebShop, 100 tasks, mean dense score | 0.429 | 0.437 | AWM 0.460 |

Only ReAct and RSEA are reported on GAIA. These tool-use results use **one shuffled-split seed** and have no reported per-cell variance/CI. The authors report no significant difference from ReAct (p>0.1); GAIA's gap is at most one task and flips sign in two evaluations of the same frozen states. WebShop retains an empty state because every evolved candidate hurt validation; the reported 0.437 and 0.429 are separate evaluation results, not evidence that the empty prior is better. Dynamic Cheatsheet scores 0.136 on WebShop and 36.7 on τ-bench: context evolution can hurt, but the comparison alone does not isolate why.

## Our read

HarnessRSI score **67**, band ★★, evidence level **retained**. The frozen artifact is tested on tasks outside the adoption split. The paper reports multi-seed ALFWorld statistics, layer and selection ablations, partial rollout-budget matching and some optimizer-cost information. It does **not** demonstrate universal gains, equal total compute, cross-benchmark reuse of a frozen artifact, or evolution of the optimizer itself.

Our stored judgment marks the leakage guard as tested based on the no-held-out-selection ablation. **Our reading:** that is an overfitting/selection control, not a comprehensive contamination audit. Disjoint splits are described, but no separate artifact-to-test contamination audit is reported in the full PDF. The validation gate is useful engineering; monotonic selection scores should not be marketed as guaranteed test safety.
