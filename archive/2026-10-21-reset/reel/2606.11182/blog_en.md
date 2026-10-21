# EEVEE: evolve the router as well as the prompts — useful procedures improve, domain knowledge can regress

*A Reel interpretation of [EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents](https://arxiv.org/abs/2606.11182v1), by Weixian Xu, Shilong Liu and Mengdi Wang. HarnessRSI Daily score **63**, band **★★**, evidence level **retained**. Code: [Princeton-AI2-Lab/EEVEE](https://github.com/Princeton-AI2-Lab/EEVEE).*

## What the system changes about itself

EEVEE changes **text prompts, not model weights**: a router prompt chooses among specialized prompt slots, and each slot's instructions evolve from feedback. The router and the slot prompts are the retained artifacts. This addresses a specific problem: an update helpful for code generation may harm knowledge QA when both share one prompt.

Despite the title's “test-time” framing, the experiments use a **prepared adaptation set with ground-truth or rule-based correctness feedback**, not just self-generated judgments and not a fully online, unlabeled stream. The paper explicitly acknowledges this limitation (§6).

## The loop, and the keep/reject rule

1. **Initialize complementary prompts.** Learn prompts on mixed training data, keep a Pareto frontier of validation correctness vectors, and greedily choose prompts with complementary example coverage.
2. **Evolve the router while holding prompts fixed.** Router mini-batches contain training examples that at least one current slot can solve. Mutation, analysis of misrouting, and reflection use ground-truth correctness. Choose the better mutation/reflection candidate on the mini-batch, then admit it to the router pool only if validation performance improves over the phase's starting router. Router scoring combines downstream accuracy, behavioral consistency and routing balance, shifting toward accuracy.
3. **Evolve prompts while holding the router fixed.** Route training and validation data into slot-specific groups. Mutation and reflection see the question, target answer, model answer and correctness. The better mini-batch candidate enters the prompt pool only if it **beats the empty prompt on that slot's validation set and remains Pareto-nondominated**. This preserves complementary candidates, not a guarantee that no individual example regresses.
4. Alternate the two phases, then freeze the router and spend a larger prompt-learning budget per slot. Final router selection uses downstream accuracy alone.

The split matters. Appendix B caps each benchmark at 500 examples, uses a 0.5/0.5 train/test split, reserves half the training partition for validation, and explicitly excludes train/validation examples from final testing; the data seed is 42. Exact realized split sizes and a random-versus-stratified splitting procedure are not given. The final test input is read by the router and target model **for routing and answering, not for updating the prompts**. Our reading is therefore held-out adaptation, not transductive optimization on the final test instances. Validation gates and split exclusion provide safeguards, but repeated validation reuse is not an overfitting guarantee, and the paper does not describe a separate content-overlap or pretraining-contamination audit.

## Headline result, as reported

Table 1 reports percentage scores averaged over three independent main runs; Table 7 supplies sample standard deviations for the **four-benchmark macro average**, including the baselines:

| Target model | Unadapted | ACE | GEPA | EEVEE |
|---|---|---|---|---|
| Qwen3-4B-Instruct | 41.37 ± 0.51 | 34.92 ± 4.14 | 37.73 ± 1.73 | **51.75 ± 1.62** |
| DeepSeek-V3.2, non-thinking | 39.75 ± 1.52 | 49.83 ± 2.07 | 55.83 ± 4.48 | **64.07 ± 1.08** |

The reported gains over the unadapted models are **10.38** and **24.32** points. These are not best-seed results. Appendix B additionally says final tests use three repeats; those repeats should not be conflated with additional independent prompt searches. No per-benchmark standard deviations or confidence intervals are reported in Table 1.

The gain is uneven. On Qwen3-4B-Instruct, HumanEval improves **49.46 → 72.63** (+23.17 points), Formula **45.22 → 54.55**, and TheoremQA **14.79 → 25.27**, but GPQA Diamond falls **56.00 → 54.55**. On DeepSeek-V3.2, the largest gain is again HumanEval, **42.82 → 92.82** (+50.00); Formula improves **30.00 → 60.55** and TheoremQA **21.21 → 39.84**, while GPQA Diamond falls **64.98 → 63.08**. The macro gains are led by code generation, with substantial mathematical/financial-procedure gains too, not uniform improvement across tasks.

## The controls that decide whether the gain is real

- **Routing and co-evolution ablations (Table 2, Qwen3-4B-Instruct).** Full EEVEE scores **51.75**, versus **43.58** with a blank/simple default router, **37.18** with a router written once by GPT-5.4 and then fixed, and **42.88** when router learning precedes prompt learning without interleaving. The unadapted control is **41.37**. These support learned routing and alternation in this configuration, but Table 2 gives neither uncertainty nor an explicit independent-search-run count, and does not establish equal total compute. Not every subtask favors the full system: default-router TheoremQA is **26.10**, versus **25.27** for full EEVEE.
- **Baseline access is only partly documented.** §3.1 describes methods as learning from the mixed training stream and testing outside it. GEPA is a reflective prompt optimizer with Pareto selection; ACE edits an adaptive playbook; the unadapted baseline does not learn. The paper does not spell out GEPA's or ACE's exact ground-truth/validation access parity, candidate/rollout limits, or tuning budgets. Neither has a reported variant given EEVEE's router and admission rules. That is missing control detail, not evidence that either baseline was deliberately weakened.
- **Defaults versus candidate selection.** Appendix B gives EEVEE's main numerical settings: four bootstrap prompts, 10 bootstrap candidate steps, 150 co-evolution mini-steps, windows of 3, phase-switch threshold **0.005**, final per-label budget 60 and mini-batch size 5. The candidate-selection split is validation. However, the split used to choose the *hyperparameter defaults* is not specified. Table 6 tests eight alternatives, each averaged over three independent trials, with macro means **45.05–50.97**. Its **1.73** standard deviation is across configuration means, not seed uncertainty. Missing numerical details include the alternative annealing schedules/targets, consistency/balance weights, and tighter/wider search budgets, mini-batch sizes and temporary-pool sizes.
- **Cross-model transfer (Table 3).** Prompts learned with Qwen3-4B-Instruct are directly applied to DeepSeek-V3.2 in non-thinking mode: **39.75 → 54.10** average, but GPQA Diamond **64.98 → 60.27**. The text establishes prompt transfer; it does not separately specify whether router text is transferred unchanged or reconstructed. Table 3 is a three-run mean without standard deviations or confidence intervals.
- **Unseen benchmarks (Table 3).** After learning on the main suite, EEVEE scores **70.42** on MBPP versus **69.29** unadapted, GEPA **68.20** and ACE **67.47**. On MMLU-Pro it scores **68.92**, below unadapted **70.74** and ACE **69.32**, though above GEPA **68.85**. The combined average is **69.67**, below unadapted **70.01**. The right-hand table does not unambiguously name the target model. Without variance, the small MBPP improvement is not a demonstrated statistically reliable gain.
- **Compute is inference-only in the cost comparison (§3.6).** After learning, Qwen3-4B-Instruct uses **4.32k total tokens per test example** with EEVEE, versus GEPA **3.47k** and ACE **21.30k**, averaged across the four benchmarks. EEVEE adds a router before answering: cheaper than ACE here, not cheaper than GEPA. These are not evolution costs. Total adaptation tokens, dollars, comparable wall-clock time, unadapted inference tokens, and matched search budgets for GEPA/ACE are not reported. The stated final-test prompt limit of 2,000 tokens and three repeats do not establish matching adaptation budgets.

## Where the gain is absent or small

**GPQA Diamond worsens on both main models.** The DeepSeek-V3.2 Formula score is also essentially tied with GEPA, **60.55 versus 60.56**, with no per-task uncertainty to interpret that tiny gap. The held-out MMLU-Pro and combined held-out average do not beat the unadapted model.

Table 4 is a **separate diagnostic retest** of six completed runs, three per model, against empty prompts on the same held-out examples. It reports GPQA Diamond changes of **−3.7** points for Qwen and **−7.7** for DeepSeek, with positive change in only **1/6 runs**. Those are not the Table 1 deltas and should not be mixed with them. The code example shows a learned executable function body rather than a bare expression; the Formula example shows better unit scale and output discipline. The negative science example shows generic reasoning overriding a correct physical prior. These examples illustrate the authors' interpretation—procedures are easier to acquire than missing domain knowledge—not a general causal proof.

## Our read

HarnessRSI score **63**, band **★★**, evidence level **retained**. The paper supports retained prompt/router learning on excluded test examples, component ablations and cross-model/cross-task evaluation. It reports main macro-score run variance **for all methods**. Our stored b20 judgment marked variance unclear; the full PDF's Table 7 resolves that omission, so the current score may understate this evidence. Appendix B also explicitly excludes adaptation and validation instances from final testing; that is not a full contamination audit. We leave the score and judgment files unchanged.

The defensible takeaway is a router-conditioned prompt set that helps a heterogeneous **prepared, labeled adaptation workload**, especially executable and formula-based procedures. It is not yet a fully online learner, a compute-matched win, or evidence of across-the-board knowledge improvement.
