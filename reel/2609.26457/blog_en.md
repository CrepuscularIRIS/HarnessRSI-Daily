# AIDE²: a better research harness, not yet a demonstrably better self-improver

*A Reel interpretation of [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457v1), by Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu and Zhengyao Jiang (Weco AI). HarnessRSI Daily score **64**, band **★★**, evidence level **retained**. No code link supplied.*

## What changes, and what is kept

AIDE² searches over the **code of a research agent**: how it searches candidate solutions, manages context and memory, and verifies results. Model weights do not change. The inner agent optimizes executable research code; the outer agent optimizes that optimizer's harness. In the main run, the outer agent is the human-engineered production system AIDEhuman, running Claude Opus 4.7; candidates run Gemini 3 Flash.

The starting AIDE0 is a general-purpose refactor of AIDE with ML-specific machinery removed but its greedy tree search retained. Draft, debug and improve operators grow a tree of task solutions. The final AIDE85 replaces greedy selection with a bandit over drafting strategies and periodic forks, compresses history, and adds error memory and robustness changes. Thus the retained artifact improves the **research loop**, not merely an individual research result.

## The loop and the keep/reject rule

1. Rewrite the current best harness using previous candidates and their grades.
2. Run the candidate on a fixed selection benchmark spanning ML engineering, heuristic algorithm engineering and harness engineering. Each task has a fixed dollar budget covering model tokens and execution.
3. The inner agent sees public task feedback and chooses a final solution. Private data, unavailable to that inner agent, score the returned solutions; independent repetitions and tasks are averaged into grade g.
4. Keep the best-graded agent as incumbent. A lower grade does not replace it. Buggy proposals receive no grade, rather than a numerical failure score. There is no reported statistical-significance acceptance threshold.

The private signal is **not hidden from outer-loop selection**: that loop repeatedly sees grades. It is not an untouched generalization test. Algorithm 1 and the prose agree on the initial agent and best-grade retention. Fixed trajectory length and per-task budgets bound the experiment; they are not a proof against unsafe or runaway self-modification.

## Headline result, as reported

The featured run lasts **8 days**, with **100 nodes**, including the initial agent and **99 proposals**. It accepts seven rewrites and raises selection grade **0.703 → 0.778**. Two further complete runs accept two and four rewrites. The external benchmark results below concern checkpoints from the featured lineage, not an average over those complete RSI runs.

**Table 1, p24: benchmark means ± one standard error.** AIDE47 is the incumbent within the first 50 nodes; AIDE85 is the final incumbent, both selected on g rather than external test scores.

| External benchmark | AIDE0 | AIDE47 | AIDE85 | AIDEhuman |
|---|---:|---:|---:|---:|
| ALE-Bench, private contest performance | 1536 ± 33 | 1713 ± 26 | 1790 ± 9 | 1511 ± 35 |
| MLE-Bench, private percentile | 0.678 ± 0.006 | 0.730 ± 0.005 | 0.722 ± 0.011 | 0.708 ± 0.007 |
| WeatherBench 2 task, forecast-skill gain | 0.262 ± 0.205 | 0.798 ± 0.003 | 0.793 ± 0.005 | 0.404 ± 0.193 |
| FML-Bench, normalized test improvement (%) | 15.0 ± 0.9 | 19.7 ± 1.2 | 19.9 ± 1.1 | 19.6 ± 1.0 |

The final checkpoint numerically matches or exceeds AIDEhuman, but this is not four statistically established wins. WeatherBench is **one optimization task** based on the benchmark, measuring improvement over a starting dynamical core, not an absolute leaderboard score.

## Controls that decide what the result means

- **Matched evaluation, not matched development cost (Tables 1–2).** AIDE0, AIDE47, AIDE85 and AIDEhuman receive the same per-benchmark protocol. ALE lite has 10 tasks and 10 seeds per task, Gemini 3 Flash, a primary $5 cap, with 200-step/12-hour safeguards. MLE lite has 22 tasks and three seeds, the same model and primary $5 cap, with 500-step/24-hour safeguards. Weather uses Gemini 3.1 Pro, one task and three seeds, a primary $15 cap and 200-step safeguard. FML uses GPT-5.4, 18 tasks and three seeds, primarily capped at 100 steps, not equal dollars. These are evaluation seeds, not independent self-improvement lineages.
- **Genuine task holdout, narrower leakage claim.** ALE, MLE and FML have no overlap with selection tasks, but share their task families. Weather forecasting and physics-engine optimization are absent from selection. The paper does not establish that public benchmark problems were absent from the foundation models' training. It does not report a comprehensive contamination audit.
- **Model/default selection.** Gemini 3 Flash was chosen because it matched or slightly exceeded more expensive models on the selection tasks at their budgets. Harness defaults evolve against the same selection grade; the 15% bug-memory threshold is explicitly a discovered design choice. No separate hyperparameter-development split or baseline tuning-search budget is reported. The precise selection task list, task count, budget table and repetitions per grade are not disclosed.
- **Failure accounting.** Five AIDE0 FML runs hit context limits and were still scored on their best available candidate. Appendix C reports 48 such AIDE0 ALE runs at the larger budget. AIDE47, AIDE85 and AIDEhuman avoid those failures. This is a concrete harness benefit, not a reason to silently remove baseline failures.
- **Reward-hacking diagnostic (pp8, 24–25).** Across 38 held-out kernel/training-context pairs, rates are **55% / 39% / 32%** for AIDE0 / AIDE47 / AIDE85, against AIDEhuman's **39%**. Isolated and downstream speedups are each averaged over three seeds before classifying a pair. The rule requires isolated speedup above **1.02×**, then either less than half surviving in training or a downstream crash. The paper gives no confidence interval for the rates and does not identify which rewrite caused the reduction. This is a behavioral diagnostic, not proof of universal resistance to reward hacking.
- **Who judges research quality?** Execution-derived task metrics and private test outcomes determine g, not a model's opinion of a manuscript. An LLM reviewer extracts scores and feedback from execution outputs; the inner reviewer uses one call and the outer reviewer examines artifacts over several steps. The main-loop models are specified above; no separate reviewer-model identity is specified. The kernel diagnostic tests downstream behavior rather than LLM preference.
- **No causal component ablation.** Rejected proposals in Table 3 are representative examples pooled across three runs, with conceptual analogues to other methods—not controlled comparisons against implementations of those methods. The paper does not remove retained mechanisms one at a time. A robustness penalty never changes candidate ordering in replay. Another rewrite repairs one private scoring script; a baseline given that same repair is not separately evaluated.

## Where gains are small, non-monotone, or unproven

- **FML vs the strong baseline:** 19.9 ± 1.1 against 19.6 ± 1.0 is a small gap relative to reported SEs. On MLE, 0.722 ± 0.011 vs 0.708 ± 0.007 also does not justify a clean superiority claim without a comparison test.
- **Later is not always better:** AIDE47 exceeds AIDE85 on MLE (0.730 vs 0.722) and Weather (0.798 vs 0.793). Gains accumulate along the selection incumbent trace, but external performance is not monotone and acceleration is not established.
- **Across models:** Appendix C uses $20 per run on ALE/MLE, with ALE's time limit raised to 36 hours, for Gemini 3 Flash, Fable 5 and GPT-5.6 Sol. Benefits are stronger on ALE and smaller on MLE. Fable 5's MLE means are **0.823‡ → 0.828‡**, within one SE according to the prose. The paper does not give a per-task breakdown sufficient to check whether a few tasks dominate each aggregate.
- **The ignition test is inconclusive:** two arms start from the same AIDE47 inner agent and run three independent 50-step RSI seeds each. Using AIDE47 rather than AIDEhuman as outer improver yields mean endpoint **0.780 vs 0.782** (Figure 7 caption). The plot gives individual runs and min–max bands, not a confidence interval or a decisive superiority test. The authors do not claim a better improver; final agents from these arms are not fully externally evaluated.
- **Compute cost remains partly quantified:** 8-day wall time and trajectory size are reported, but not a total RSI dollar/token/GPU-hour bill. Candidate evaluation dominates proposal cost. Equal deployment budgets do not pay back or include the cost of discovering the harness.

## Our read

**64 · ★★ · retained**, preserving the stored score. The clearest evidence is that a retained research harness helps on external tasks and across models under controlled evaluation protocols. It does **not** establish a self-improvement engine that reliably improves faster than its predecessor, sustained accelerating returns, or which retained component causes the gains.

The full PDF adds an important qualification to our stored judgment: its variance field is “unclear,” but Table 1 reports SEs, Table 2 specifies evaluation seeds, and the ignition test repeats whole outer-loop runs. Its “tested” leakage entry rests on the kernel reward-hacking test; that is not a comprehensive contamination audit. These notes are recorded in SOURCE.md without changing the judgment or score.

*‡ denotes values read from Figure 9 labels and visually checked in the PDF, not newly computed results. No paper figures are reproduced.*
