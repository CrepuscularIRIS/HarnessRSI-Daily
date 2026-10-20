# DRACO: a judge writes the rubric, then routes the learning signal to individual agent steps

*A Reel interpretation of [DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094v1), by Shubham Gandhi, Saurabh Goyal, Kiran Kate and Yara Rizk. HarnessRSI Daily score **66**, band **★★**. Code: [IBM/draco](https://github.com/IBM/draco).*

## What the system changes about itself

DRACO changes **policy weights through LoRA training**, while generating fresh evaluation criteria from the agent's rollouts. It does not retain a rewritten prompt, tool or harness program. That distinction matters for this repository's non-weight harness-RSI scope: the board records this paper as `retained`, but the retained learned artifact here is a weight adapter, not a harness patch.

The question is nevertheless useful to evaluator design: if there is no training-time checker for task success, can a model judge provide a signal more informative than one reward copied onto every step?

## The loop, and the keep/reject rule

1. Sample six trajectories for each training task. A frozen GPT-5.4 judge proposes criteria from the task instruction, extends them from each rollout's observed failures, and merges/deduplicates them into a shared rubric for that group.
2. Score each completed trajectory against that rubric: pass, fail or not applicable. **Keep a criterion only if at least one group member failed it**; this is the rubric filter, not a ground-truth success gate. Reward is `(passes − fails) / (passes + fails)` over applicable retained criteria.
3. A separate attribution phase asks the judge which steps caused each verdict; it may confirm or override the earlier verdict. A step's quality is the pass fraction of the criteria citing it. Uncited steps inherit the average quality of cited steps.
4. GRPO normalizes rewards within the group. For positive group-relative advantage, concentrate reinforcement on judge-approved steps; for negative advantage, concentrate suppression on judge-disapproved steps. Credits weight the **policy-gradient update**; they do not choose a best rollout or a patch to retain.

The closed-form redistribution conserves the scalar sum of token advantages over credited tokens, **not the gradient vector**. It accounts for step length, excludes gap tokens and falls back to uniform advantage if attribution is unavailable or the normalizer collapses. A trajectory can be a relative winner while failing the actual task. There is no verifier-based accept/reject gate for weight updates. Checkpoints are reported on a fixed late-training schedule, not selected for best test performance.

## Headline result, as reported

Training uses the 90 AppWorld training tasks. Evaluation covers AppWorld test_normal (TN, 168 tasks), test_challenge (TC, 417 tasks with unseen apps/compositions), and zero-shot τ-bench Banking (97 tasks). TGC means task-goal completion, SGC whole-scenario completion and SR success rate. All entries below are percentages at p1, the mean-success metric (Table 2).

| Qwen3.6-27B | Base | Outcome-reward GRPO | DRACO |
|---|---:|---:|---:|
| AppWorld TN TGC | 69.4 | 80.0 | 85.3 |
| AppWorld TN SGC | 41.1 | 59.3 | 70.6 |
| AppWorld TC TGC | 49.7 | 59.9 | 61.5 |
| AppWorld TC SGC | 30.2 | 38.3 | 40.7 |
| τ-bench Banking SR | 15.8 | 17.6 | 20.4 |

The paper reports **+15.9 TGC points over Base and +5.3 over outcome-reward GRPO on TN**. The abstract's separate **+5.3 transfer gain** is the **self-judge** variant, 21.1 against Base 15.8; it is not the frontier-judge row's 20.4. These are different variants, not a numerical contradiction.

These are not best-checkpoint numbers or independent training-seed means. Qwen3.6-27B trains for 100 steps; the headline averages checkpoints at steps 90, 95 and 100, each evaluated three times. Qwen2.5-32B-Instruct trains for 75 steps and averages 65, 70 and 75. Table 4's trained-row standard deviations are **across checkpoints**; Base uses three inference runs of one checkpoint. Training-run variability is explicitly not characterized. The row-level Average has no SD or CI.

## The controls that decide whether the gain is real

- **A crossed rubric/credit ablation.** On TN, static rubric/no credit gives TGC/SGC **81.1/59.9**; static rubric/credit **81.9/60.7**; dynamic rubric/no credit **82.1/64.9**; full DRACO **85.3/70.6**. Adding credit to dynamic rubrics supplies the reported **+3.2/+5.7**. Static criteria are not an empty baseline: they were constructed from 720 untrained-policy rollouts on the training tasks and GPT-5.4 proposals. The static-with-credit arm receives comparable judge-based step attribution, whereas no-credit arms and vanilla outcome-reward GRPO do not. There is no reported outcome-reward-plus-DRACO-credit control. Published SALT supplies a separate outcome-aware step-credit reference on the other model, not a matched outcome-blind competitor.
- **Random-reward training also improves the base.** Section 4.3 reports TN TGC/SGC **74.0/50.0**, above Base's **69.4/41.1** but below DRACO's **85.3/70.6**. Thus some improvement also occurs without the proposed credit signal. This control neither validates causal step attribution nor substitutes for an outcome-reward-plus-step-credit control.
- **Shared RL schedule, unequal total cost.** The settings share precommitted hyperparameters: 16 prompts, six rollouts each, eight H100 GPUs per run and rank-16 LoRA. The paper does not identify a split used to choose those defaults or report hyperparameter-search/baseline-tuning budgets. Equal optimizer steps are not equal judge expenditure. The authors avoid test-based checkpoint selection, but do not report a contamination audit.
- **What variance supports.** TN TGC is **85.3 ± 1.5** versus outcome reward **80.0 ± 1.9**. TC is **61.5 ± 1.0** versus **59.9 ± 1.2**. These checkpoint SDs are not seed robustness or a confidence interval on the difference. The aggregate p1 **55.7** versus the best ablated **53.3** is a descriptive average, without aggregate uncertainty.
- **The judge is the objective, not ground truth.** Rubrics and step citations are computed from task instructions and trajectory text by the model judge, without gold answers or training-time unit tests. AppWorld's final evaluation uses programmatic tests, an independent signal from that reward. τ-bench uses state-matching SR with GPT-5.4 as user simulator and judge, so that evaluation is not wholly independent of the frontier judge. Our reading: judge preferences could favor the behavior it trained; the paper does not demonstrate such favoritism. It explicitly leaves human validation of criteria and causal step attribution for future work.
- **Self-judging is tested, not certified.** The main self-judge enables thinking and requires unanimous passes from three scoring calls. A replay using the weaker single-call/no-thinking setup agrees with GPT-5.4 on **89.4%** of verdicts, versus **72.0%** for always passing. It falsely passes **30.4%** of frontier-failed criteria, but falsely fails **1.3%** of frontier-passed ones. These are agreement-with-frontier numbers, not human correctness. The replay's generation and merging reuse archived frontier-generated inputs, so it is not a clean end-to-end self-judge attribution audit.

## Where the gain is absent or small

- **Much of the extra benefit is on TN, not uniformly across tasks.** On TC SGC, full DRACO **40.7** is below static/no-credit **42.4**. For three-attempt consistency p3, TC TGC **43.9** is below **45.6**, and Banking SR **8.6** is below dynamic/no-credit **9.3**. Table 6 also gives TN hard-task SGC **51.9** versus dynamic/no-credit **55.0**; the strong medium-task improvement does not extend to every difficulty metric.
- **Transfer margins are thin.** Frontier DRACO Banking SR **20.4 ± 1.0** versus dynamic/no-credit **19.7 ± 0.5** is comparable with the reported checkpoint spread, without a significance test. Self-judge is highest at **21.1 ± 1.4**. On Qwen2.5-32B-Instruct, Banking moves only **3.4 ± 0.6 → 4.0 ± 1.0**, with overlapping spreads. This is weaker transfer evidence than the AppWorld gains.
- **The other model does not beat the outcome-aware step-credit reference.** Qwen2.5 TN TGC/SGC rises **35.7/17.3 → 62.9/42.3**, but published SALT reports **66.2/47.9**. TC is **34.0/19.2** versus SALT **36.8/20.9**. SALT sees ground-truth outcomes, and its training/tuning budget is not matched here.
- **Inference savings do not pay the training bill automatically.** TN evaluation cost falls **$10.77 → $8.27**, TC **$43.56 → $38.03**. Separately, the full judge pipeline costs **$1607** over 100 training steps, versus **$570** for static/no-credit. Figure 8's full-DRACO generation phases cost **$63‡** for task criteria, **$527‡** for rollout criteria and **$318‡** for merging; step attribution itself costs **$308‡**. These are judge costs, not GPU-inclusive totals. Figure 8 assigns **$316** to the main thinking-enabled, three-scoring-call self-judge, matching the main row in Tables 2 and 7. Section 4.3's nearby wording has an ambiguous antecedent after mentioning the weaker single-call/no-thinking variant; no separate cost is identified for that weaker variant. Static-rubric setup-cost inclusion is also unspecified.

## Our read

The board records **66**, **★★**, evidence level **retained** (judgment batch b07). The full paper reports held-out evaluation, cross-benchmark transfer, a useful rubric/credit ablation, judge cost and checkpoint/inference variability. It does **not** establish training-seed robustness, human validity of rubric/step judgments, or a judge-cost-matched baseline; no tested leakage audit is reported. Its preserved object is a LoRA adapter, a scope caveat for a board about non-weight harness changes.

Our takeaway is narrower than “fine-grained credit solves attribution”: dynamic rubrics plus credit improve held-out AppWorld outcomes, especially TN scenario completion, but task success does not prove the cited steps are causally correct. The explicit length-normalized rule also gives equal **step totals**, not uniform token advantages, under unanimous non-degenerate verdicts; Appendix B.3's “exactly baseline GRPO” shorthand should be read alongside the more precise Appendix E.7/E.9 equations.

*‡ Phase costs were read from Figure 8's labels; they are not newly estimated costs. See SOURCE.md for provenance and judgment notes.*
