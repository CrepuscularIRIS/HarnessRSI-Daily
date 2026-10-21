# OPD-Evolver: learning how to maintain memory, not merely adding more of it

*A Reel interpretation of [arXiv 2606.17628v1](https://arxiv.org/abs/2606.17628v1), **OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation**, by Guibin Zhang, Xun Xu, Yanwei Yue, Zikun Su, Wangchunshu Zhou, Xiaobin Hu and Shuicheng Yan. HarnessRSI score **63 · ★★ · retained**. [Code](https://github.com/bingreeky/opd-evolver); not executed for this review.*

## What changes, and what is kept

OPD-Evolver has two distinct kinds of change. The **fast loop** keeps model weights fixed while updating a persistent repository of trajectories, tips, skills and executable tool templates. The same policy selects memories, executes the task, writes experience and periodically merges or deletes memories. The **slow loop trains the policy weights** to do these jobs better. This is not a wholly weight-free training method, nor a coding agent rewriting its own optimizer.

The signal is environmental task feedback. Within each task group, a memory is scored by comparing outcomes when it was retrieved and selected against outcomes when it was retrieved but not selected, with selection-frequency, tier and confidence weighting (§3.3). Our reading: this controls candidate availability, but is not a randomized causal-effect estimate.

The keep rule is learned memory writing and maintenance, **not a held-out accept/reject gate** for each repository edit. Appendix D.2 specifies a teacher-memory score threshold of **0.01**, up to **20** selected teacher memories from **50** candidates, the top **30%** of generated memories for writer-side selection, and maintenance every **30** tasks. The paper does not fully specify how writer-side filtering maps onto every online repository update; Algorithm 1 simply writes and updates each tier. We do not replace that description with an invented success-only gate.

The privileged teacher is the same evolver under stop-gradient conditioning, not an independently larger teacher. It sees memory values, successful trajectories from the same task group, later utility of written memories and repository diagnostics. Student outputs are sampled under deployment-facing inputs; token-level KL distills the teacher on the student's own prefixes. In execution distillation, the student solves without memory while the teacher gets useful experience. Deployment returns the student to the fast memory loop.

## Headline results, with the comparison kept local to its table

Table 1 reports the best task-success metric on all ten evaluated subsets against same-backbone memory baselines for both model sizes. The setup names **Qwen3-4B-Instruct-2507** and **Qwen3.5-9B**; Table 1 shortens the former group label to **Qwen3-4B**. The following are the complete **9B** comparisons, using the strongest memory baseline separately in each column. Values are percentages.

| Evaluated subset | OPD-Evolver-9B | Strongest same-backbone memory baseline |
|---|---:|---|
| LifelongAgentBench DB | 84.50 | 82.50 · EvolveR |
| LifelongAgentBench OS | 65.00 | 61.00 · MemEvolve |
| MemoryArena Math | 10.88 | 8.19 · ExpeL |
| MemoryArena Physics | 11.63 | 11.05 · AWM |
| AMA-Bench Causal Inference | 47.32 | 45.81 · Memp |
| AMA-Bench State Updating | 53.94 | 49.77 · MemEvolve |
| AMA-Bench State Abstraction | 52.92 | 48.00 · AWM |
| InterCode Bash | 49.55 | 45.98 · MemEvolve |
| InterCode CTF | 57.00 | 53.00 · MemEvolve |
| InterCode SQL | 64.01 | 61.15 · MemEvolve |

These are **streaming test evaluations**, not an untouched test set queried by a frozen repository: memory starts empty and grows from earlier evaluation episodes. Table 1 reports no seed/run count, task-order repeats, standard deviations or confidence intervals; it does not identify a best seed or validation-selected checkpoint. Do not read the decimal granularity as evidence of repeated runs.

Table 2 is a separate training-method comparison. All compared methods receive additional MiniHack training on the same training data and are evaluated on the same test tasks. The authors describe the best average performance but provide no numerical aggregate or uncertainty. They report wins on five of six subsets, with a Room exception. Table 2 does not label a backbone for each row; Appendix D.2 gives shared defaults and some method-specific identifiers, so we do not assign the entire table an unqualified common model.

## Controls that decide whether the gain is real

**Component ablations (Table 3, explicitly OPD-Evolver-4B).** Every entry below is a percentage, ordered Bash / CTF / SQL. No variance or repetition count is given for this table.

| Variant | Bash / CTF / SQL (%) |
|---|---|
| Full | 36.16 / 34.00 / 45.86 |
| Without slow evolution | 32.14 / 28.00 / 39.17 |
| Without memory attribution | 31.20 / 26.69 / 38.50 |
| Without learned selection | 35.27 / 32.00 / 42.04 |
| Without writing distillation | 34.38 / 29.00 / 41.08 |
| Without maintenance | 35.30 / 30.10 / 43.51 |

Removing attribution means replacing it with a frequency-calibrated score, not removing all scoring. Removing selection means taking the top five by similarity. The paper describes the maintenance ablation as disabling repository-update training. These rows support the relevance of lifecycle training; they do not establish statistical significance or isolate each component at matched total compute. Figure 4 additionally compares memory-free execution before and after training for both sizes, reporting higher success and fewer steps; it is an execution diagnostic, not the full online-memory result.

**What the baselines actually receive.** ExpeL, AWM, Cheatsheet, Memp, ReasoningBank, EvolveR and MemEvolve are memory-system comparators, not all frozen no-memory agents. The evaluation protocol gives all memory-based methods an empty initial repository and the same available environment feedback, without ground-truth answers or expert solutions. The paper does not document giving each Table 1 baseline OPD-Evolver's unified hindsight distillation. In Table 2, SFT receives LoRA training for three epochs; GRPO receives one epoch; Skill0 (called SkillZero in Appendix D.2) receives a MiniHack-specific skill set and a staged skill-removal curriculum for one GRPO epoch. MemRL uses runtime memory Q-value updates rather than weight updates, retrieving at most three memories, with other reinforcement-learning settings left at package defaults. Complementary RL has a **Qwen3.5-9B** actor plus separate **Qwen3-4B-Thinking-2507** memory model and memory actor, trained for **512** steps; its episode limit is **80** actions against the shared **40**-step default. Comparable feedback and MiniHack data are reported; comparable total training/evolution machinery and compute are not demonstrated.

**Splits and leakage.** The main training collection has **7,000** tasks: **3,000** Agent World Model, **2,000** nvidia/Nemotron-Terminal-Corpus and **2,000** EnvScaler. Section 4.1 says these sources are disjoint from evaluation benchmarks. The explicit Table 2 exception is added training within MiniHack, using the same MiniHack training data and test tasks across methods; the paper does not describe the train/test partition, disjointness of instances, seed-level overlap or additional training-set size. Appendix C.1 says evaluation memory is built only from the current stream and receives success/failure feedback, not answer keys. This prevents a preloaded benchmark-memory advantage, but the retained artifact can contain earlier evaluation tasks and task-specific lessons; related later tasks can benefit by design. No near-duplicate or artifact-content leakage audit is reported. AMA-Bench evaluates Causal Inference, State Updating and State Abstraction, not Recall; MemoryArena evaluates Math and Physics, not its whole benchmark.

**Tuning and cost.** No split is named for selecting the threshold, writer fraction, maintenance period, checkpoint or other defaults; baseline hyperparameter-search budgets are not reported. That is separate from missing numerical settings: OPD-Evolver's learning rate, batch size, training epochs/steps and memory-tier priors are not specified. Some baseline learning rates, batches and training durations are given, so “no baseline settings” would be inaccurate. The paper lists **8 NVIDIA A800 (80G)** GPUs, but no training/evolution wall-clock time, GPU-hours, token usage or dollar cost, and no matched-total-compute comparison.

## Where gains are absent or small

The Table 1 gains are broad in sign, not uniform in size. For **9B**, MemoryArena Physics is **11.63% vs 11.05%** and AMA Causal Inference **47.32% vs 45.81%**; the clearer separations include OS **65.00% vs 61.00%**, State Updating **53.94% vs 49.77%** and State Abstraction **52.92% vs 48.00%**. For **4B**, Causal Inference is **32.89% vs Memp's 32.38%**, and DB **74.00% vs 73.00%**. Thus the gain is not confined to a single task or model, but magnitude depends substantially on the subset. Without uncertainty, small margins cannot be called statistically reliable.

In **Table 2**, OPD-Evolver loses MiniHack Room to GRPO (**98.04% vs 100.00%**). It improves Maze over Skill0 (**27.45% vs 25.49%**) and KeyRoom over Complementary RL (**9.80% vs 5.16%**), but absolute KeyRoom success remains low. Bash is **64.01% vs GRPO's 63.69%**, CTF **59.00% vs 58.00%**, and SQL **49.55% vs Complementary RL's 48.10%**. Appendix C lists **51 test tasks per MiniHack environment**. If these were single passes over those tasks, the Room loss and Maze gain would each be only **one task‡**: Room **50/51 vs 51/51‡**, Maze **14/51 vs 13/51‡** reproduce the printed percentages after rounding. These are conditional reconstructions, not reported run outcomes; the run/averaging protocol is unspecified. Complementary RL's MiniHack Room / Maze / KeyRoom percentages (**96.88 / 20.85 / 5.16%**) do not match any single integer-success count over 51 after rounding; any averaging or alternative reporting rule is unspecified. We retain the printed values without assuming their cause. No uncertainty is available for the claimed average or its components.

The giant-model claim also has limits in **Table 1**: **Qwen3.5-397B-A17B** remains ahead on DB (**86.00% vs 84.50%**), Causal Inference (**57.21% vs 47.32%**), State Updating (**58.73% vs 53.94%**) and Bash (**51.34% vs 49.55%**). **STEP-3.5-Flash (196B)** remains ahead on Causal Inference (**49.50% vs 47.32%**). This is competitiveness on selected subsets, not replacement of larger models across the board.

## Our read

**63 · ★★ · evidence level: retained**, from the existing HarnessRSI score and judgment batch b03. The useful result is that a trained policy can improve the whole memory lifecycle, then build a new repository from evaluation feedback. The paper reports cross-environment evaluation, component ablations and a memory-free execution diagnostic. It does not quantify seed/task-order uncertainty, evolution cost or matched-compute gains; source-disjointness is not a tested contamination audit. A stronger improver claim needs those controls, not simply the word “evolver.” The full PDF contains richer component ablations than the condensed judgment's `retained_ablation: unclear` suggests; SOURCE.md records this without changing the score or judgments.

All task-success percentages are printed in the paper. The ‡ task counts are our conditional reconstructions, not reported outcomes; no numeric figure-label readings are used. See SOURCE.md for the calculations, provenance and table-local protocol caveats.
