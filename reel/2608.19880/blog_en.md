# EnvHarness: change the practice environment, keep the skills — but count the generation rollouts

*A Reel interpretation of **EnvHarness: Awakening Static Worlds for Agent Learning**, [arXiv 2608.19880v1](https://arxiv.org/abs/2608.19880v1). HarnessRSI Daily score **63**, band ★★, evidence level **retained**. Code: [google-research/envharness](https://github.com/google-research/envharness).*

## What the system changes about itself

EnvHarness changes the **training environment's interface**, not the base model or native task verifier. A **Stage** replays actions before the policy starts, changing the initial state. A **Contract** filters actions, changes returned transition responses, or masks/augments observations. A **Chain** joins tasks and requires both native verifiers to pass. Thus preserving the backend and verifier does not mean preserving everything the agent sees: examples deliberately simulate test-runner failures or block shortcuts.

In the main skill-learning pipeline, accepted environment components generate trajectories from which ReasoningBank-style skills are extracted. These retained skills equip the frozen policy on original, unreshaped evaluation tasks. **Chain is excluded from that automated pipeline** and tested separately. The RL analysis updates weights and is a different learning setting, not the non-weight artifact behind our retained classification.

## The loop, and the keep/reject rule

EnvRigger observes **5** unmodified rollouts per task, diagnoses successes and failures, and writes a candidate set of Stage/Contract components. It then collects **5 fresh rollouts** and the **designer model** decides ACCEPT / REFINE / REJECT from aggregate success rate, failure distribution and timeouts, not one trace. Candidates that are impossible or unchallenging are rejected; intermediate candidates are revised for at most **5** write–validate rounds, after which a task can yield no component (Sections 3 and Appendix A/E.3).

The native benchmark scores task success; the model judges whether that success/failure pattern is a useful training signal. This is not an independently proven solvability test or a gate requiring held-out improvement. The designer and policy share a backbone: **Gemini-3.1-Flash-Lite** on ALFWorld/WebArena, **Gemini-3.5-Flash** elsewhere. No stronger external teacher is used in these comparisons.

## Headline result, as reported

Table 2 reports **mean ± standard deviation over three independent runs**. Success-rate results, in percent:

| Evaluation | Original-environment skills | EnvHarness skills |
|---|---|---|
| ALFWorld In-Dist | 63.3 ± 2.8 | 66.2 ± 0.3 |
| ALFWorld OOD | 61.4 ± 4.3 | 70.4 ± 2.3 |
| ALFWorld average | 62.4 ± 3.4 | 68.3 ± 1.3 |
| WebArena average over evaluated subdomains | 38.5 ± 3.1 | 41.6 ± 1.8 |

The advertised **9.0-point** gain is ALFWorld **OOD**, not an average across all benchmarks; In-Dist improves by 2.9 points. GenEnv's ALFWorld average is 62.6 ± 1.9; VeriEnv's WebArena average is 39.6 ± 1.4.

Table 3 reports SWE-bench Verified success rate **49.88 ± 2.59% → 52.58 ± 2.72%**, versus SWE-smith **50.12 ± 1.74%**. Average steps are **55.01 ± 1.69 → 49.61 ± 2.49**; the abstract's **9.8% fewer steps** compares these Original Envs and EnvHarness rows, not the no-skill row. OfficeQA exact match is **54.40 ± 1.84 → 56.20 ± 2.34**, and SpreadsheetBench Pass@1 **45.88 ± 1.19 → 49.15 ± 0.36**, on percentage scales. Table 3 gives SDs but does not explicitly state the repeat count; do not automatically carry Table 2's three-run claim over. No confidence intervals are provided, and the SWE/Office mean margins overlap the reported run spread.

## The controls that decide whether the gain is real

- **What is matched, per baseline.** Original Envs supplies unmodified training tasks. GenEnv supplies LLM-simulated tasks/transitions/success on ALFWorld; VeriEnv supplies executable recreated websites with programmatic rewards on WebArena; SWE-smith synthesizes repository tasks. The paper gives all the same seed tasks, environment count, model, skill extraction and retrieval, and states the same oracle verification access. It does **not** give these baselines EnvHarness's trajectory-conditioned wrapper-writing/validation loop, quantify matched environment diversity, or equalize every interaction budget. There is no generation baseline for OfficeQA or SpreadsheetBench.
- **Split story and leakage.** Only training tasks are reshaped; evaluation uses original tasks. Table 7 specifies 100 ALFWorld train tasks with benchmark seen/unseen evaluation, 20 WebArena training tasks per evaluated subdomain, 100 SWE-bench Lite training tasks and **407 Verified issues not in Lite**, 50 OfficeQA training tasks and **172 official test tasks**, and 100 SpreadsheetBench training tasks with **299 held-out tasks / 897 instances**. WebArena's reported subdomains are Reddit, Shopping, Shop Admin and GitLab, not a claim over every WebArena site. Explicit instance exclusion reduces direct overlap, but no semantic near-duplicate or pretrained-contamination audit is reported. SpreadsheetBench is described as 100 of 400 verified tasks for training plus 299 held out; the paper does not explain that split arithmetic.
- **Settings versus tuning.** Appendix E.3 gives the rollout/revision defaults and uses them across benchmarks, but names no split that selected them; baseline tuning search/budgets are unreported. Separately missing numerical settings include the standard loop's target success-rate band, skill-learning decoding temperature/episode cap, and the RL learning rate. Appendix F.1 does give many other RL settings. The explicit band in Table 12 belongs to a separate objective-targeting diagnostic, not necessarily the standard loop.
- **Generation cost (Table 11).** ALFWorld estimated design/rollout/total tokens: EnvHarness **1.46M / 226.6M / 228.0M**, GenEnv **38K / 64.2M / 64.2M**. WebArena: EnvHarness **1.58M / 135.7M / 137.3M**, VeriEnv **20K / 137.7M / 137.8M**. Rollouts dominate. WebArena totals are close, while ALFWorld is not compute-matched; GenEnv's simulated interactions are not equivalent work to real execution. No corresponding SWE-smith or Original Envs cost totals, dollar totals or wall-clock figures are reported. The design cost is paid once per generated environment, not per training episode.
- **Component control, not a full optimizer ablation (Table 5).** On standard **single-environment SWE test issues**, Chain-only skills yield **49.63%** success / **41.96 steps**, versus Original Envs **49.88% / 55.01**. Stage/Contract gives **52.58% / 49.61**; combined skills **54.30% / 43.12**. No variance or run count is supplied here, nor separate Stage-only/Contract-only or no-diagnosis/no-validation controls.
- **Adaptation and models.** At 300 environments and 15 skills, the scaling experiment reports SWE success **54.79%**, against Original Envs **52.13%** and SWE-smith **50.37%** (Section 5 prose). Counts and retrieval are matched, but only EnvHarness conditions each new batch on the current skilled policy. Table 9 reruns generation with each policy's own backbone, not donor-skill transfer. Original → EnvHarness success rates are **36.8% → 40.0%** for Gemini 3.1 Flash-Lite, **48.4% → 52.1%** for Qwen3.6 27B, **49.9% → 52.6%** for Gemini 3.5 Flash, and **69.2% → 72.4%** for Claude Sonnet 4.6. This table supplies averages without variance/CI.

## Where the gain is absent, small, or concentrated

- **WebArena GitLab:** VeriEnv **38.9 ± 5.6%** exceeds EnvHarness **37.7 ± 3.1%**. The largest original-to-EnvHarness subdomain gain is **Shop Admin +6.2 points**, versus Reddit +1.9, Shopping +2.2 and GitLab +2.3. Some margins are small against SDs; no significance test resolves them.
- **Leave-one-task-type-out ALFWorld (Table 10):** average **60.6% → 63.7%**, but clean **54.8% → 71.2%** supplies the largest improvement (+16.4 points); heat regresses **61.1% → 52.4%** (−8.7), simple ties **83.6%**, and cool improves only **38.5% → 39.3%**. This transfer mean comes without variance/CI and is not uniform generalization.
- **RL is not uniformly better (Table 4):** Qwen3-8B-base with GRPO improves ALFWorld In-Dist **81.4% → 87.9%**, but OOD falls **89.6% → 88.8%**. WebShop score is **75.6 → 79.2**, success **66.0% → 67.4%**. Appendix F.1 fixes seed 0 and gives 150 training epochs/steps on 8 H100 GPUs; no variance/CI is shown. A fixed seed alone does not establish how many complete runs were conducted.
- **Success gains need not save steps.** In Table 9 Qwen3.6 27B steps increase **37.1 → 40.8** versus original-environment skills; Claude Sonnet 4.6 increases **25.4 → 25.6**. Only the Gemini 3.5 Flash rows improve both success and step count against both controls.
- **Limits:** resettable textual environments are required. Around a third of the round-3 training tasks in the qualitative scaling account exhaust revision without accepted components. Implemented Chain composition is sequential; richer routing sketches are not validated branching-task results.

## Our read

Published HarnessRSI score **63**, band **★★**, evidence level **retained**: generated wrappers leave useful skills that improve held-out original tasks. The full paper reports repeated-run variance in Table 2, SDs in Table 3, leave-one-type-out transfer and estimated generation tokens. These strengthen evidence beyond the condensed judgment's `unclear` entries for variance, cross-task and optimizer cost; we record that in SOURCE.md without editing the score or judgments.

Environment-count matching is not universal compute matching. The decisive remaining gaps are baseline tuning budgets, a stated default-selection split, a semantic leakage audit, and controls isolating diagnosis/acceptance from environment reshaping. The practical takeaway is targeted practice with trusted task scoring—not a claim that all categories improve, that the generator improves itself, or that wrapping is free.

*No ‡ numbers are used: all numerical results above are printed in the paper, and no figure-label values were needed.*
