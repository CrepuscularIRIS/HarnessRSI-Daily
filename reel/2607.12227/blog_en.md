# Rethinking harness-evolution evaluation: a flat held-out result, but useful task-specific game adaptation

*A Reel interpretation of **Rethinking the Evaluation of Harness Evolution for Agents**, [arXiv 2607.12227v4](https://arxiv.org/abs/2607.12227v4). HarnessRSI Daily score **63**, ★★. [Code](https://github.com/rethinking-harness-evolution/code); we did not run it.*

## What changes, and what this critique actually tests

This paper asks whether better scores come from a reusable improvement to an agent's harness or simply from spending more inference and feedback on the evaluated tasks. Its introduction critiques the evaluation of **Meta-Harness, Agentic Harness Engineering (AHE), and AEVO**. It does **not** independently reproduce all those systems: the Terminal-Bench experiment instantiates **AHE with its external explore agent disabled**, retaining its feedback-driven editing loop. The explore agent would retrieve benchmark-specific harnesses from external sources; disabling it isolates a narrower mechanism, not the complete original AHE system.

The four methods hold model weights fixed. **Parallel Sampling** generates independent attempts with a fixed harness. **Sequential Refinement** revises solutions from prior trajectory summaries, still with a fixed harness. **Harness Evolution** edits a shared harness across a batch of tasks. **Harness Scaling** edits a separate harness for each evaluation task. Editable artifacts include prompts, tools, middleware and memory; the signal is execution trajectories, with correctness outcomes when available.

## The loop and the keep/selection rule

For shared Harness Evolution, a meta agent reads the accumulated harness/trajectory store and proposes another harness. Without unit tests, the final harness is used. With tests, the harness with the highest aggregate outcome is selected; the held-out experiment specifically selects on validation tasks. For task-specific Harness Scaling, the next harness is conditioned on the task, previous harness and trajectory, plus the outcome when available. Without tests it returns the last trajectory; with tests it can return a successful attempt.

The baselines receive the corresponding feedback too: Parallel Sampling uses model self-selection without tests and test-based oracle selection with tests; Sequential Refinement sees the prior trajectory summary and, in the test-available setting, its outcome. Neither baseline can edit its harness. The comparison tests **where extra search is spent**, not a harness-update mechanism granted identically to every baseline.

## Headline results, with the measurement kept explicit

On all **89 Terminal-Bench 2.1 tasks**, the methods share the same minimal bash-only initial harness. The models are **Claude Opus 4.6, GPT-5.4, GPT-5.4 mini**. The default budget is **K = 5**, with one rollout per task per harness; Section 4 averages two independent runs. These tables do not give SDs or confidence intervals.

| Method | No unit tests: average pass@1 (%) — Table 1 | With unit tests: average pass@1 / pass@5 (%) — Table 2 |
|---|---:|---:|
| Initial harness, direct sampling | 68.2 | 67.6 / — |
| Parallel Sampling | 72.3 | 82.0 / 82.0 |
| Sequential Refinement | 69.3 | 76.9 / 87.1 |
| Harness Evolution | 67.4 | 69.7 / 79.0 |
| Harness Scaling | 71.8 | 75.5 / 85.6 |

Appendix A defines pass@1 as the **mean reward across rollouts** and pass@5 as success on at least one attempt. Do not read every pass@1 cell as the success rate of an oracle-selected final answer. The initial controls differ between tables; the comparisons above stay within each table.

The more direct test of reusable improvement is **Table 3**: evolve on **45 training tasks**, select the harness on **10 validation tasks**, then test on **34 disjoint tasks**. Initial and evolved harnesses both average **63.2% pass@1**. Per model, the initial → evolved scores are **63.3 → 64.5** for Claude Opus 4.6, **72.1 → 72.1** for GPT-5.4, and **54.4 → 53.0** for GPT-5.4 mini (all %). This supports a limited-generalization finding for this implementation and split; the paper supplies no significance test or interval for it.

The positive results concern a different target: **task-specific adaptation**, not a shared artifact transferred to unseen games.

- **All 25 public ARC-AGI-3 games, 2,000 environment actions (Table 4):** fixed **VISTA*** → memory-evolving **VISTA** → **full harness** gives **43.3 → 59.3 → 77.5 RHAE** with **Claude Opus 4.8**, and **21.1 → 25.9 → 38.2 RHAE** with **GPT-5.6 Terra**. The paper reports relative improvements of **79.0%** and **81.0%** over VISTA*. RHAE measures action efficiency as well as completion; these are not win percentages. The plain Claude Code and Codex reference averages are **44.3** and **4.6 RHAE**, respectively.
- **EdgeBench's five Interactive Games & Simulators bot-programming tasks, not the whole benchmark (Table 5):** fixed-harness Sequential Refinement → Harness Scaling gives **48.3 → 54.7** with **Claude Opus 4.8**, and **45.9 → 49.8** with **GPT-5.4**, on a **0–100 score scale**. The paper reports **13.3%** and **8.5%** relative improvement. These are two-run means of the **highest score achieved in a 12-hour window**, not fresh held-out test scores.

## Controls that determine what follows

- **Matching is setting-specific.** Terminal-Bench matches rollout budget and feedback, but Appendix A explicitly excludes harness-editing cost, calling it small without measuring it. ARC matches environment actions; internal reasoning and read-only inspection are free under that protocol, so this is not token/dollar matching. EdgeBench's wall-clock budget includes summarization, editing and the paused agent's idle time.
- **The ARC control is informative but bundled.** VISTA* retains visual observations, inspection tools and context-reset continuation, while disabling GUIDE.md and WORKING.md. VISTA restores evolving memory; full harness additionally allows skills, tools and hooks. This is not an isolated causal ablation of each added component, nor a baseline with the same writable artifact interfaces but a different update rule. Artifact-use counts in Appendix B measure usage, not value.
- **Larger-budget exception (Appendix A.3).** At **K = 10**, with tests and **Claude Opus 4.6 only**, Harness Scaling reaches **90.5% pass@1 / 94.4% pass@10**, versus Sequential Refinement's **89.6% / 93.1%** (Table 8). The authors describe this gap as within run-to-run variance, but do not print the variance. Shared Harness Evolution still scores **73.6% / 86.5%**; on held-out tasks it scores **63.0%** versus initial **63.3%** (Table 9). The negative conclusion is not a claim that task-specific scaling never has the largest cell.
- **Selection and tuning are different questions.** Terminal configurations are fixed from a reference-run snapshot (Table 6); the validation split selects the final harness, not a documented hyperparameter sweep. ARC model/reasoning settings were chosen to leave solvable but unsaturated tasks; no separate tuning split is identified. Edge update defaults are three submissions or 120 minutes. Separate baseline tuning/search budgets are not reported. Numerical settings still unspecified include Terminal sampling temperature and split seed/assignments, and an ARC internal token ceiling; these omissions are not evidence of test-set tuning.
- **Repetition and failures.** Terminal Section 4 and its larger-budget appendix report two independent runs; Edge Table 5 explicitly does too. ARC's run count is not specified. No SDs/CIs or cross-condition seed-pairing protocol are supplied for these comparisons. Terminal infrastructure failures count as failures rather than being dropped.
- **Game feedback is not unseen-task transfer.** Edge submissions expose judge feedback, while periodic host snapshots are hidden from the agent; the reported maximum includes both. A validated harness update is installed, otherwise the old harness remains, but the validation criterion is not specified. No held-out-game or cross-model artifact-transfer experiment is reported.

## Where improvement is absent, uneven, or not established

The flat Terminal held-out average is the central negative result. Without tests, shared evolution particularly hurts **GPT-5.4: 75.3 → 69.7%** (Table 1). But task-specific scaling is best for **Claude Opus 4.6: 76.0%**, versus parallel sampling's **74.7%**, so even the no-test result varies by model.

ARC benefits are heterogeneous, not universal: with **GPT-5.6 Terra**, full harness reaches **100 RHAE** on **tr87** versus VISTA* **11.8**, but scores **0.0** on **sk48** versus VISTA* **0.8**, and **0.0** on **vc33** versus **0.6**. With **Claude Opus 4.8**, **tn36** declines from VISTA* **18.5** to full harness **3.6 RHAE**. The large aggregate should not be read as a uniform per-game improvement.

Edge gains also depend on task and model. With **Claude Opus 4.8**, NetHack rises **44.3 → 61.3**, but Wesnoth falls **88.0 → 86.0**. With **GPT-5.4**, OpenRCT2 rises **36.2 → 50.0**, while NetHack falls **50.4 → 49.0** and OpenTTD **51.6 → 50.5** (Table 5, all score points on the same 0–100 scale). No uncertainty estimates establish which small task-level differences are reliable.

## Our read

HarnessRSI score **63**, band **★★**, evidence level **task** (latest judgment: batch b12). The paper reports a matched-rollout comparison, an explicit held-out test, a memory-versus-full-harness control, and negative as well as positive outcomes. Its positive game results demonstrate same-task adaptation; the held-out shared-harness test is flat. It does not establish an improved improver, broad transfer, exact total-compute equivalence, or statistical certainty for the small differences.

Our board should apply this critique to itself: budget matching must name the resource and overhead counted; held-out evidence must distinguish an evaluation's existence from a positive transferable gain; a retained-artifact ablation should not silently stand in for equal-access baselines; and two-run means are not reported variance. The score is our evidence rubric's summary, not a refutation of the paper's critique or a universal rating of harness evolution. SOURCE.md records these qualifications without changing the judgment files.
