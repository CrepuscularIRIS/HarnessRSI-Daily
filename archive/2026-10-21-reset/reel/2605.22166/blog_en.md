# Life-Harness: evolving the runtime interface around a frozen agent — large gains over the no-harness agent, a closer race against the strongest baseline

*A Reel interpretation of [arXiv 2605.22166v3](https://arxiv.org/abs/2605.22166v3) (HarnessRSI Daily score 72, ★★★). Code: [Tianshi-Xu/Life-Harness](https://github.com/Tianshi-Xu/Life-Harness).*

## What the system changes about itself

Life-Harness leaves the model alone. The solver (Qwen3-4B-Instruct) is frozen, the environments and scorers are unchanged, and what evolves is the **runtime harness** between the two. The harness has four layers, placed at different points of the interaction loop:

1. **Environment Contract** (before interaction): clarified tool descriptions, policy constraints and common pitfalls shown to the model in place of the original contract.
2. **Procedural Skill** (task conditioning): a skill library distilled from training trajectories; the top-1 skill, retrieved with BM25, is inserted into the system prompt.
3. **Action Realization** (before execution): checks whether an action is executable, canonicalizes unambiguous interface errors, and blocks actions that would deterministically fail.
4. **Trajectory Regulation** (after feedback): detects repetition, stagnation or budget exhaustion and triggers recovery messages.

The paper motivates this split with a failure diagnosis of 393 failed Qwen3-4B training episodes (LLM-annotated, all annotations checked by human reviewers): about a third are trajectory degeneration (33.6‡%), a third environment-contract mismatches (33.3%), 23.2‡% action-realization failures and 9.9% general reasoning errors, with the mix varying by environment.

## The loop, and the keep/reject rule

1. Run the frozen solver with the current harness on a batch of up to 50 training tasks.
2. An evolution LLM (GPT-5.5) reads the trajectories and the current harness, finds recurring failures and writes a candidate that can add, revise or remove mechanisms in any of the four layers.
3. The candidate must pass interface checks and a replay on training traces; failures go back for up to three repair attempts.
4. A valid candidate is run against the current harness **on the same training batch** with the benchmark's own scorer. It replaces the current harness only if accuracy strictly improves; otherwise the current harness is kept and the next round uses a new batch.
5. After six rounds the retained harness is frozen and evaluated on held-out tasks. Splits are in Table 5: for example 100 training tasks and 109 test tasks for ALFWorld, 30 and 20 for tau-bench Airline, 74 and 40 for Retail and Telecom.

The harnesses that result are substantial per-environment programs (Tables 7–9): task parsers, state trackers, action validators and, in some environments, forced next actions or forced answer commits. The paper describes the harness as "environment-specific but model-agnostic".

## Headline result, as reported

Qwen3-4B-Instruct, test split, Pass@1 accuracy (%), one evolved harness per environment, six evolution rounds on identical training batches for the three evolving methods (Table 1):

| Environment | No harness | Meta-Harness | AHE | Life-Harness |
|---|---|---|---|---|
| ALFWorld | 16.5 | 35.8 | **89.0** | 88.1 |
| WebShop | 29.5 | 42.5 | 39.0 | **45.5** |
| OS | 21.5 | 25.7 | 37.5 | **39.6** |
| DBBench | 44.0 | 50.3 | 57.3 | **65.0** |
| tau-bench Airline | 35.0 | 11.7 | 35.0 | **60.0** |
| tau-bench Retail | 48.0 | 33.3 | 45.8 | **63.0** |
| tau2-bench Telecom | 25.8 | 50.8 | **95.0** | 90.0 |

Group means: AgentBench 27.9 / 38.6 / 55.7 / 59.5; tau suites 36.3 / 31.9 / 58.6 / 71.0. Across the seven environments the paper reports Life-Harness above Meta-Harness by 28.7 pp and above AHE by 7.5 pp in mean accuracy (Life-Harness mean 64.45), using 8.5% and 68.4% fewer evolution tokens respectively; it has the highest accuracy on five of seven environments. On the stricter Pass3 metric (success in all three runs) the tau mean is 12.5 / 18.3 / 44.2 / 57.5.

## The controls that decide whether the gain is real

- **Baselines.** Meta-Harness and AHE were run by the authors from open-source implementations "under the same conditions": same solver, evolution LLM, rollout settings, six rounds, identical training batches. AHE was designed for coding-agent harnesses (related work), and these are the authors' reproductions. Rounds and batches are matched; evolution tokens are not (Table 1: AHE spends 9.9 and 8.2 (10^7 tokens) on the two group means against 2.5 and 3.5 for Life-Harness). No tuning budget for the baselines and no repeated runs are reported. Costs count evolution-LLM tokens only, not solver or evaluation usage.
- **Leave-one-layer-out ablation (Table 4, Qwen3-4B).** Values are relative accuracy drops against the full harness, no SD reported, and the paper does not say whether the ablated variants were re-evolved or the layer was simply removed from the final harness. Removing Action Realization costs 61.7% on Airline and 59.6% on OS; removing Trajectory Regulation costs 86.5% on ALFWorld and 36.2% on Telecom; removing Contract or Skill costs at most 17.5% / 17.4% on any environment, and about 1% on ALFWorld. The paper's reading: every layer matters on some benchmarks, and the impact varies by environment.
- **Prompt-only evolution (Figure 6).** The paper's text says prompt optimization improves over the baseline and Life-Harness has higher Pass@1 in all seven environments. The figure has no numbers; read off the bars, prompt-evolving is roughly level with or below the unmodified model on ALFWorld, OS and WebShop and above it on DBBench, Airline, Retail and Telecom. The main text gives no budget for the prompt optimizer.
- **Transfer across models.** The Qwen3-4B harness is reused, without re-evolving, on 17 more open-weight backbones (instruct, reasoning, agent-trained): improvements in 116 of 126 model-environment settings (Figure 5) and, with AppWorld, 132 of 144. On three frontier models, the same harnesses give mean gains of 2.8 (GPT 5.5), 4.4 (Opus 4.8) and 3.4 (Gemini 3.1 Pro) pp, with gains in 18 of 21 settings (Table 2). Qwen2.5-32B-Instruct with Life-Harness exceeds the tool-trained xLAM-2-32B by 7.5 pp on tau-bench (Figure 7).
- **ALIGN and AgentSquare (Table 11).** Their released harnesses were evaluated on ALFWorld and WebShop across 18 backbones; Life-Harness is highest of the three on every ALFWorld row and in most WebShop rows (exceptions: Qwen3.6-27B 43.00 vs AgentSquare 47.00, Llama-xLAM-2-70B 42.00 vs 50.00, and a tie at 43.00 for Qwen3.5-35B-A3B). The unmodified model equals or beats Life-Harness on two ALFWorld rows (Qwen3.5-27B 88.99 vs 88.99; Qwen3.6-27B 90.83 vs 89.91). "ALIGN follows its released task split; AgentSquare uses the Life-Harness task selection." So ALIGN is not scored on the same tasks, and both are released final harnesses, not re-evolved under the Table 1 conditions.
- **AppWorld (Table 3).** Mean Pass@1 over 18 backbones rises from 25.5 to 30.8 (16 of 18 backbones improve); the AppWorld test set has 57 tasks.

## Where the gain is absent, small or within noise

- **Not the best everywhere.** AHE is higher on ALFWorld (89.0 vs 88.1) and Telecom (95.0 vs 90.0; Pass3 87.5 vs 77.5). On WebShop and OS Life-Harness leads by small margins over the best baseline (45.5 vs 42.5; 39.6 vs 37.5).
- **Baseline behaviour.** Meta-Harness ends below the unmodified model on Airline (11.7 vs 35.0), Retail (33.3 vs 48.0) and the tau Pass@1 mean (31.9 vs 36.3); AHE is below it on Retail (45.8 vs 48.0). ALIGN and AgentSquare are also often below the unmodified model (for example Qwen3-4B on WebShop: 18.00 and 18.50 vs 29.50). Part of the Life-Harness margin is therefore against baselines that did not improve on the no-harness agent in these runs. Table 12 shows how little the training-batch curve says about test results: Meta-Harness on Airline has training-batch accuracy of 30.00 in all six rounds, yet scores 11.7 on test against 35.0 unmodified; AHE on Retail falls from 50.00 (round 3) to 20.00 (round 6) on training batches and scores 45.8 on test. The paper does not say which round's harness is frozen for evaluation, for the baselines or for Life-Harness.
- **Cost against Meta-Harness is not lower everywhere.** Life-Harness uses more evolution tokens than Meta-Harness on WebShop (3.8 vs 3.7), Retail (2.6 vs 1.4), Telecom (4.3 vs 2.1) and the tau mean (3.5 vs 3.0); the 8.5% saving is an aggregate over the seven environments.
- **Small tau test sets and no variance.** Airline has 20 test tasks (one task is 5 pp of Pass3); Retail and Telecom have 40. AgentBench tasks are run once, tau tasks three times, at temperature 0.0, and the paper reports no seeds, SDs or confidence intervals, and reports one harness per environment with no repeated runs.
- **Gains are uneven across models and environments.** For the larger reasoning models the change is near zero or negative on some environments: Qwen3.5-27B −3.3 on Airline and 0.0 on ALFWorld; Qwen3.6-27B −3.3, −0.8‡ and −0.9‡ on Airline, Retail and ALFWorld. The same models gain elsewhere (Qwen3.5-27B +7.5 on WebShop and +5.7‡ on DBBench; Qwen3.5-35B-A3B +17.4 on ALFWorld). 10 of 126 open-weight settings are not improved. Among frontier models, GPT 5.5 is unchanged on Retail (72.5 vs 72.5) and Gemini 3.1 Pro on ALFWorld (96.3 vs 96.3), and Gemini is lower on OS (50.0 to 48.6); GPT 5.5 is also the evolution LLM. On AppWorld the paper's framing is a mean gain of 5.3 pp over 18 backbones, but it is uneven: Qwen3.6-35B-A3B goes 54.39 to 73.68 and Qwen3.6-27B 70.18 to 82.46, while Qwen3-4B goes 1.75 to 5.26 and two models are unchanged.
- **Internal inconsistencies.** Table 13 lists Qwen2.5-32B-Instruct at 15.10 and 20.40, which are not multiples of 1/57 (57 test tasks) and enter the 25.50 and 30.76 means; Table 10 lists Qwen2.5-72B on Airline at 0.6034 with the harness, not a multiple of 1/60 (20 tasks, 3 trials), and it feeds the +18.7‡ in Figure 5. We use the table values as printed.
- **Scope.** Each harness is evolved per environment; no transfer to unseen environments is tested. Only text- and API-based environments are covered (Limitations).

## Our read

HarnessRSI score **72**, band ★★★, evidence level **retained**: the frozen artifact (a harness evolved on training tasks) is evaluated on held-out tasks and on other model backbones. The paper reports held-out test data excluded from evolution, an optimizer-cost comparison, leave-one-layer-out ablations and a comparison with two other harness-evolution methods on identical rounds and batches. It does not report variance across seeds or runs, transfer across environments, or a leakage test (the evolution prompt instructs the LLM not to read test trajectories, but no audit is shown), nor an ablation of its own accept/reject rule. Baseline budgets are matched in rounds and batches, not in tokens. The headline table is a single evolved harness per environment on test sets of 20–300 tasks, so margins of a few points, especially on tau-bench, are within what one or two tasks can change.

*Numbers are as printed in the paper; numbers marked ‡ are read from figure labels or computed from table values (see SOURCE.md).*
