# MIPRO: optimize instructions and demonstrations together—but the extra gain is task-dependent

*A Reel interpretation of [arXiv 2406.11695v2](https://arxiv.org/abs/2406.11695v2), **Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** (HarnessRSI Daily score 64, ★★). Authors: Krista Opsahl-Ong, Michael J Ryan, Josh Purtell, David Broman, Christopher Potts, Matei Zaharia, Omar Khattab. The first two authors contributed equally. No code link supplied for this Reel.*

## What the system changes about itself

MIPRO changes the **free-form instructions and few-shot demonstrations of each module** in a language-model program. It jointly selects these prompt components across modules; it does not change model weights or search over the program's control flow. The optimization signal is a downstream task metric, not gold labels for intermediate steps.

## The loop, and the keep/reject rule

1. Run training inputs through the program to bootstrap module-level input/output traces. Keep candidate demonstrations when the final output passes a metric threshold; an intermediate step is assumed useful because the whole trace succeeded, not independently certified.
2. Ask a proposer LM for instruction candidates, grounded in training-data summaries, program information, successful demonstrations and prompting tips.
3. Use a multivariate Tree-structured Parzen Estimator (TPE) to select a **joint combination of instructions and demonstration sets** for the modules.
4. Evaluate the resulting program on a sampled training minibatch and update the surrogate from its end-to-end score. Periodically evaluate promising combinations on the full training set; return the highest-scoring fully evaluated configuration (§4.3). This is the main-text account: Appendix F.1 (p19) instead scores Bootstrap candidates on dev, and F.5 (p21) describes MIPRO selection on a validation set. Section 4.1 (p5) permits training or a dedicated validation split. Per-method selection-split details therefore remain ambiguous; this is not evidence of test-set selection or leakage.

The retained artifact is the configured program's prompts. **0-Shot MIPRO++ is a different variant**: it learns how to propose instructions—summary switches, temperature, tips and demonstrations shown to the proposer—rather than jointly optimizing the deployed demonstrations as well. **Temperature scope is unresolved:** §4.4 (p6) specifies proposer-LM temperature, whereas Appendix B.4 (p14) says the Llama model's temperature is optimized in MIPRO++ while identifying GPT-3.5/GPT-4 as proposers. The PDF does not establish whether task-model sampling was also tuned; we do not attribute the gains to either interpretation.

### Who supplies the signal?

The task LM is Llama-3-8B. Appendix B.4 specifies GPT-3.5 as proposer generally and GPT-4 for ScoNe, HoVer and Iris; §5.2 gives the broader GPT-3.5 default. The demonstration teacher defaults to Llama-3-8B, switching to GPT-4o on ScoNe and HoVer. These are not an LLM jury: selection uses exact match, classification accuracy, gold-document retrieval, or exact match plus formatting checks. For HotPotQA Conditional, GPT-4 with author supervision annotated answer types used by the metric. This is an upstream annotation dependency, not a proposer judging its own output during optimization.

## Headline result, as reported

Table 2 reports **means over five runs**, not a best seed. With Llama-3-8B, joint MIPRO has the highest test mean in five of seven settings. Compare it with the strongest other reported optimizer in each column—not just the unoptimized program:

| Test task / metric | MIPRO | Strongest other optimizer |
|---|---:|---|
| ScoNe exact match | 79.4 | 77.4, Bayesian Bootstrap |
| HotPotQA exact match | 46.4 | 46.2, Bayesian Bootstrap |
| HoVer, 3-supporting-fact subset, Recall@21 | 39.0 | 37.6, Bayesian Bootstrap |
| HotPotQA Conditional custom score | 23.3 | 14.6, 0-Shot MIPRO |
| Iris accuracy | 88.6 | 94.1, Bootstrap RS |
| Iris-Typo accuracy | 68.7 | 58.7, Bootstrap RS |
| Heart Disease accuracy | 74.2 | 79.2, Bootstrap RS |

**HoVer scope:** Appendix A (p13) restricts evaluation to examples with three supporting facts, not the full benchmark. Facts can share documents: approximately 67% of training and 83% of test examples are actually three-hop queries; the remainder are two-hop. The authors recommend a genuine three-hop filter for follow-up work. The HoVer scores and split sizes here refer to this mixed-hop, three-supporting-fact subset.

The largest positive separations are on **Conditional and Iris-Typo**. The abstract's “as much as 13%” is consistent, after rounding, with Conditional versus demonstration-only Bootstrap RS (23.3 versus 10.4); it is not the gap against that column's stronger instruction-only 14.6 comparator. No unresolved text/table discrepancy is needed to explain it.

## The controls that decide whether the gain is real

- **What each baseline can optimize.** Bootstrap RS gets bootstrapped demonstrations and random-search selection, with instructions fixed. Bayesian Bootstrap gets demonstration-only TPE search. 0-Shot MIPRO gets instruction-only search; 0-Shot MIPRO++ additionally learns instruction-proposal settings. Module-Level OPRO generates instructions using module histories and whole-program proxy scores; its grounded version gets extra task/program context. OPRO −G still gets examples and instruction/score histories in the meta-prompt: it is not information-free. The unoptimized program gets no search. Only full MIPRO in Table 2 jointly searches both deployed components.
- **Joint versus single-component search.** On Conditional, instruction-only 14.6 exceeds demonstrations-only 10.4, while joint MIPRO reaches 23.3. On Heart Disease, demonstration-only 79.2 exceeds joint 74.2. Joint search is not universally better.
- **Grounding can hurt.** Module-Level OPRO with versus without extra grounding scores 73.5 versus 76.1 on ScoNe, 39.0 versus 36.0 on HotPotQA, and 32.5 versus 25.7 on HoVer. These are not a direct grounding ablation of full joint MIPRO.
- **Learning to propose is mixed.** Instruction-only MIPRO++ versus MIPRO scores 75.7 versus 71.5 on ScoNe, 39.3 versus 36.8 on HotPotQA, but 32.6 versus 33.1 on HoVer. ScoNe's best instruction-only mean is still OPRO −G at 76.1.
- **Statistics, not seed dispersion.** Table 2 averages five runs and reports Wilcoxon significance via bolding; §5.2 describes testing per-example scores averaged across runs. HotPotQA's 46.4, 46.2 and 45.8 are statistically comparable. Thus five highest means do not mean five significant wins; §6 names HotPotQA, Iris and Heart Disease as exceptions. No SDs, CIs or explicit seed identifiers accompany Table 2. Appendix G's curves and Appendix H's prompt progressions are individual illustrative runs, not variance estimates.

## Splits, budgets and costs

Table 3 says **training data trains the optimizers, dev data supports method iteration, and test data is for final reporting**. Train/dev/test sizes are HotPotQA 500/500/2000; Conditional 500/200/200; ScoNe 500/500/1200; HoVer 500/500/1520. Iris uses 75 training and 75 test examples; Heart Disease 120 and 183. The latter two have no dev set and were not used for method iteration. These are same-benchmark held-out examples, not cross-task transfer of a frozen prompt. We follow the main experiment's stated split roles, but Appendix F's dev/validation selection descriptions leave per-method selection splits unresolved, as noted above; dev isolation cannot be fully reconstructed from the PDF.

Appendix B.3 says candidate-count defaults were chosen from intuition built over past experiments, not extensive sweeps. It does not separately identify which split selected each default. The paper reports split roles, but no explicit overlap/contamination audit or detailed grouping/randomization protocol. Optimization and evaluation concern the same task distributions; held-out examples are not evidence of novel-task transfer. Appendix H explicitly acknowledges instructions overfitting to meta-prompt demonstrations.

**Baseline search budgets are reported.** Appendix B.2 assigns optimizers 50 full-evaluation trials on HotPotQA and ScoNe (about 300 minibatch trials), 30 on Iris, Heart Disease and Conditional, and 20 on HoVer. This is partial evaluation-budget matching, not equal total tokens or LM calls. Proposal, summary and teacher-generation costs are not itemized; total optimization tokens/calls and dollar costs are not reported. Candidate counts vary by method, and separate baseline hyperparameter-tuning budgets are not given. We cannot turn these trial counts into a verified all-in cost comparison.

## Where the gain is absent or small

HotPotQA's small lead is not statistically distinguished from demonstration-only search. MIPRO loses to Bootstrap RS on Iris (88.6 versus 94.1) and Heart Disease (74.2 versus 79.2). Instruction-only MIPRO can even fall below the unoptimized program: Iris 36.4 versus 40.9, Heart Disease 25.8 versus 26.8. Conditional's rules are supplied in a handwritten seed prompt; the experiment does not show autonomous discovery of all task rules. The evaluation uses one task-model setup, without a cross-model transfer study.

## Our read

HarnessRSI score **64**, band **★★**, evidence level **retained**. The paper reports retained prompt configurations evaluated on held-out test data, repeated runs with significance testing, component comparisons and a partially matched evaluation budget. It does not establish cross-task transfer, all-in optimizer cost, leakage-audit results, or seed dispersion. The recorded judgment marks variance evidence as present; more precisely, the published evidence is repeated-run averages and significance tests, **not reported SDs/CIs**. The strongest practical lesson is to optimize demonstrations as well as instructions, while checking whether the incremental benefit of joint search exists on the particular task.
