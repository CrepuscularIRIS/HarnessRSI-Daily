# CDSE: separate what a trajectory teaches before deciding how to keep and use it

*A Reel interpretation of [From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents, arXiv 2610.23599v1](https://arxiv.org/abs/2610.23599v1). HarnessRSI Daily score **64**, ★★, evidence level **retained**. No public code URL is supplied in our record; the PDF refers to Software supplementary material.*

## What the system changes about itself

CDSE updates a persistent external skill, not model weights or the improvement protocol. It separates trajectory-derived knowledge into **Meta** (task-wide planning, monitoring and stopping rules), **Experience** (locally triggered heuristics and recovery), **Tool** (capability-specific operational guidance), and **Script** (reusable deterministic procedures and their execution contracts).

The input is an evaluated execution trace: reasoning, actions, observations and outcome. A deterministic filter removes runtime noise without replacing the trace with a model summary. Success analysis identifies supported behaviors and fragile-success safeguards; failure analysis locates an evidenced error or missing transition and a minimal supported recovery. Each candidate “semantic gradient” is a natural-language behavioral update with exact trace-line evidence, not a numerical gradient. The analyzer emits a core finding, up to two reusable lessons and at most one script suggestion.

## The loop, and the keep/reject rule

The router rejects generic, unsupported, instance-specific or redundant findings, then assigns each retained finding one primary role and at most one secondary role. Meta and Experience maintain atomic rules; Tool organizes rules by capability; Script proposals must warrant deterministic reuse, explicit input/output and error contracts, feasible tests, and savings over one-off tool use.

Scripts are implemented or revised, self-tested and independently verified in a clean environment, with one bounded repair; unverified code is withheld. A coordinator resolves cross-component conflicts and duplication, then descriptions are rewritten to explain each component's scope, timing and expected benefit. Failed coordination or description-validation checks prevent publication of the updated state. **These are evidence and edit-contract gates, not an accept-only-if-task-score-improves gate** (Appendix G). At execution time the agent uses its ordinary invocation mechanism to load relevant components; descriptions are visible even before loading, so no recorded invocation does not mean no exposure.

## Headline result, as reported

Table 1 evaluates the skill state after three evolution rounds on six benchmarks, three models and two harnesses. CDSE has the highest score in all 36 settings. The reported **7.6 percentage-point gain over Base** and **2.6 over the strongest competing method in each cell** are macro-averages of within-benchmark changes, not a pooled task accuracy. No variance, confidence intervals or run/seed counts accompany Table 1; “one reported score” is not proof of a single run.

For GLM-5.2 under Claude Code, the test scores are:

| Benchmark | CDSE | Strongest competing skill method |
|---|---:|---:|
| OfficeQA | 77.2 | 76.4, SkillOpt-lite |
| SpreadsheetBench2 | 30.7 | 28.3, Trace2Skill |
| SealQA | 54.1 | 52.4, EvoSkill |
| LiveMathBench | 87.7 | 85.0, SkillOpt-lite |
| SWE-Pro | 68.4 | 63.1, SkillOpt-lite |
| AutomationBench | 32.9 | 25.5, EvoSkill |

## The controls that decide whether the gain is real

- **Held-out, but within related task collections.** Every selected benchmark collection is split training:test at 2:7. The training split supplies the trajectories; reported scores use test. This is learning from relatives of evaluation tasks, not an unrelated external trajectory library. SWE-Pro uses pandas, scikit-learn and xarray; AutomationBench uses Sales and Marketing; the split is not reported as repository- or domain-disjoint. Exact split sizes, split seed/grouping and a train/test overlap audit are not reported. The router excludes sample-specific answers, but that is not an empirical leakage audit.
- **Access and baseline budgets.** Within a model–harness block, Trace2Skill, SkillOpt-lite and EvoSkill share the training split, task instances, tools and context limit with CDSE. Base is the same agent without an evolved skill. Trace2Skill combines Error and Success branches and merges their updates. EvoSkill uses error examples only, 1.5 epochs and frontier size 3. SkillOpt-lite uses 10 optimization rounds and batch size 10. Table 1 uses three outer evolution rounds for each skill-evolution method. The paper does not say these baselines received CDSE's differentiated library, router or validation machinery; the **no-differentiation ablation**, specifically, receives the same semantic gradients. Shared access and comparable token totals are useful but not exact compute matching.
- **Mechanism ablations, GLM-5.2/Claude Code (Table 3).** On SpreadsheetBench2 / SWE-Pro / AutomationBench, full CDSE scores **30.7 / 68.4 / 32.9**. Collapsing the components while retaining the same semantic gradients gives **25.8 / 62.6 / 24.3**; a shared updater gives **27.1 / 65.4 / 28.0**; no coordination gives **29.6 / 67.5 / 30.7**; no adaptive invocation interface gives **26.4 / 64.3 / 27.1**. These comparisons support organization and invocation beyond lesson extraction, but report no uncertainty or run counts.
- **Transfer has boundaries.** Complete skill swaps between GLM-5.2 and DeepSeek-V4-Flash, with Claude Code fixed, improve 11 of 12 receiving settings; the reported average gain is 4.2 points for each receiving model. Swapping Claude Code/Codex states with GLM-5.2 fixed improves all 12 settings, averaging 3.3 and 3.4 points. Cross-benchmark component transfer is much more selective: Meta improves 9 of 10 source–target pairs, averaging 3.6 points; Tool and Script transfer less consistently (Tables 2, 11–12). These experiments do not cover every model–harness pairing.
- **Defaults versus tuning splits.** Appendix H says baseline parameters follow original recommendations unless specified, but reports no split used to select hyperparameters/defaults and no baseline tuning/search budgets. There is no separate development split stated; this does **not** establish test-set tuning. Missing numerical details include rule/category capacities, per-question runtime limits and skill-evolution decoding settings; the evolution-model identity and initialization contents are also unspecified. Benchmark scoring rules, several turn limits and the SealQA judge's temperature and output limit are provided.
- **Distillation cost, not free reuse.** For one GLM-5.2/Claude Code evolution round, CDSE consumes **50.90 million input / 2.800 million output tokens** on SpreadsheetBench2, **127.80 / 5.800** on SWE-Pro and **24.70 / 1.100** on AutomationBench (Table 5). Other methods have similar single-round totals. Table 4 gives **7.60 / 15.04 / 2.19 million input tokens per point of gain**, using that round's gain—not the three-round headline. No dollar or wall-clock cost, full three-round total or separately itemized distillation-stage cost is given.

## Where the gain is absent or small

All Table 1 cells favor CDSE, but not by equally large margins. MiniMax-M3/Codex SpreadsheetBench2 is **29.4 versus 29.1** for SkillOpt-lite; GLM-5.2/Claude Code OfficeQA is **77.2 versus 76.4**. Without uncertainty, statistical significance cannot be assessed. AutomationBench's gains over Base are larger under Claude Code (**12.1, 14.6, 10.9** points for GLM, DeepSeek and MiniMax) than under Codex (**4.9, 8.4, 5.5**); the gain is not uniform across harnesses.

Repeated consolidation reuses the **same trajectory corpus**. GLM-5.2/Claude Code OfficeQA goes **77.8 → 77.2** from round two to three; SWE-Pro **69.0 → 68.4**; AutomationBench **33.3 → 32.9** (Table 8). The headline is the third-round state, not a claimed best checkpoint. These results do not establish sustained improvement with fresh experience.

Transfer can hurt: DeepSeek-V4-Flash receiving GLM skills on SealQA scores **48.5**, below its **51.8** Base and **59.4** native state (Table 11). Spreadsheet-derived Script transferred to SWE-Pro gives **−3.9** points; Spreadsheet Meta transferred to LiveMath gives **+0.0** (Table 2). Token efficiency is not uniformly best either: OfficeQA costs SkillOpt-lite **6.64** versus CDSE **7.87** million input tokens per point (Table 6).

## Our read

**64 · ★★ · retained**, from the latest stored judgment. The paper reports held-out task evaluation, skill/component transfer, mechanism ablations and single-round token costs; budget matching is partial. It does not report seed variance, baseline tuning budgets, a selection split for defaults, or an empirical train/test leakage audit. The evidence supports differentiated maintenance of retained skills, not an improving improvement protocol, and not indefinite self-improvement. The cleanest control is the same-gradients, no-differentiation ablation; the main remaining uncertainties are statistical robustness, split detail and full optimization cost.
