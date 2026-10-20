# EvolvingBrain: a frozen multimodal agent builds its own skill library — gains over a no-skill agent, with no variance reported

*A Reel interpretation of [arXiv 2610.20786v1](https://arxiv.org/abs/2610.20786v1) (HarnessRSI Daily score 68, ★★). Authors: Runxuan Liu, Jingqi Shi, Baoxin Wang, Honghong Zhao, Haoyuan Xu, Yueqing Sun, Jiafeng Liang, Tao He, Dayong Wu, Qi Gu, Shijin Wang, Ming Liu, Bing Qin (Harbin Institute of Technology, iFLYTEK, Meituan, Pengcheng Laboratory). Code: the paper says it is "provided in the supplementary materials and will be publicly released in the camera-ready version"; no public link yet.*

## What the system changes about itself

The multimodal agent (Qwen3.8-27B, Kimi-K3 or GPT-5.6-Sol) stays frozen. What changes is an external, model-specific **Skill Brain**: Domain, Plan, Action and Trap Skills plus a graph linking them. It is built offline from training trajectories (Section 2.2.1 says each frozen model collects its own; Appendix A.1 says that on VAB-Minecraft "the released training trajectories cover 90 unique task goals" are used for skill construction, and the paper does not reconcile the two):

1. Training trajectories are collected (per Section 2.2.1, by the frozen model itself); successful and failed ones are both kept (success is the environment's flag).
2. An LLM extracts **procedural patterns** (what advances the task) and **problematic patterns** (what blocks it; for multimodal causes the images of the relevant rounds are inspected).
3. Problematic patterns become **Trap Skills**, reused only if mechanism, root cause and repair steps all match, otherwise created. The model then **retries the same task from its initial state** with the Trap Skills; a persistent problem triggers skill revision, a new problem another iteration, until the task succeeds, the retry budget is exhausted or no actionable root cause remains. Skill evolution is capped at three feedback iterations.
4. **Keep rule:** a trajectory is accepted only when the task succeeds, no known problem recurs and no new problem is detected; otherwise the problem goes back to the retry loop.
5. Accepted trajectories are distilled into Plan Skills and Action Skills (each reused, updated or newly created by comparison with the library). Domain Skills are derived afterwards from the Plan, Action and Trap Skills, with instance-specific detail removed, and the four types are linked in a graph.

At test time the library is frozen. A text-only **Structured Abstractive Memory** (progress, blockers, ineffective attempts, retry conditions) feeds a gate that answers none / reuse / retrieve each round; retrieved skills (Action and Trap Skills first from the graph neighbours of the current Plan Skills, then globally) are fused into temporary Active Guidance that is never written back.

## Headline result, as reported

Success rate, test splits, "averaged over three runs" (Table 2). VAB = VAB-Minecraft; DW = DiscoveryWorld in-domain test.

| Backbone | Direct VAB | MMSkills VAB | EvolvingBrain VAB | Direct DW | EvolvingBrain DW |
|---|---|---|---|---|---|
| Qwen3.8-27B | 57.67 | 69.84 | 73.02 | 50.00 | 58.02 |
| Kimi-K3 | 69.84 | 70.37 | 79.37 | 63.58 | 74.07 |
| GPT-5.6-Sol | 68.78 | 70.10 | 78.83 | 61.72 | 68.52 |

The three backbones run at different inference settings (Qwen3.8-27B and Kimi-K3 at xhigh, GPT-5.6-Sol at high). Averaged over the three backbones the paper reports +11.64 percentage points on VAB-Minecraft and +8.44 on DiscoveryWorld over the direct agent, and +6.97 over MMSkills on VAB-Minecraft. Per backbone the gain over Direct runs from 6.80‡ points (GPT-5.6-Sol, DiscoveryWorld) to 15.35‡ points (Qwen3.8-27B, VAB-Minecraft). The Direct agent uses the same interface, inference settings and interaction budget (60 rounds on VAB-Minecraft; 100 steps on Easy and Normal, 200 on Challenge DiscoveryWorld tasks) but no skills.

## The controls that decide whether the gain is real

- **Trap Skill retrieval ablation (Table 4).** Turning off Trap Skill retrieval at test time (Domain, Plan and Action Skills kept, same adaptive retrieval; the library is still built with Trap-driven retries, so this does not isolate Trap Skills as a whole) gives, on VAB / DW success: Qwen 70.90 / 55.02, Kimi 75.27 / 69.77, GPT 74.58 / 65.72, against 73.02 / 58.02, 79.37 / 74.07 and 78.83 / 68.52 for the full system. The paper reports Trap Skill retrieval adds 3.49 (VAB) and 3.37 (DW) points on average. Single values, no SD.
- **Feedback iterations (Table 6).** Limiting evolution to one pass gives 68.68 / 54.63 (Qwen), 75.29 / 69.44 (Kimi), 75.57 / 65.74 (GPT); three iterations add 3.89 (VAB) and 3.60 (DW) points on average.
- **Retrieval granularity (Table 5, Qwen and Kimi only).** Coarse (Domain-level) retrieval costs Qwen 6.64 / 4.32 points and fine-grained (Plan and Action) retrieval costs Kimi 5.19 / 5.55 points relative to adaptive retrieval. Adaptive beats the better fixed depth by only 0.96‡ and 0.61‡ points (Qwen) and 1.16‡ and 1.23‡ points (Kimi).
- **Held-out themes (Table 7, Section 3.4).** The library is built from six DiscoveryWorld training themes and evaluated unmodified on all 30 tasks of two held-out themes; no out-of-domain trajectory is used. Success Direct → EvolvingBrain: Qwen 36.67 → 46.67, Kimi 48.89 → 60.00, GPT 46.67 → 56.67 (+10.00, +11.11, +10.00; average +10.37). The in-to-out-of-domain drop is 12.42 for EvolvingBrain against 14.36 for Direct; that 1.94‡ point gap is less than one task per run (3.33‡ points of 30), comes with no SD, and compares different task sets (in-domain test versus the 30 held-out tasks), so we treat it as within noise. The in-domain test shares themes (and difficulties) with training; only variants differ (0–2 train, 3–4 test).
- **Comparator.** MMSkills is evaluated on VAB-Minecraft only, with its publicly released skills; the paper does not reconstruct its skill-generation process and could not run it on DiscoveryWorld. MMSkills gains 12.17 points on Qwen but 0.53 and 1.32 on Kimi and GPT; EvolvingBrain gains 9.53 and 10.05 there.

## Where the gain is absent, small or unverified

- **Qwen vs MMSkills is 3.18‡ points** (73.02 vs 69.84); on GPT-5.6-Sol MMSkills' average score (0.7741) is below Direct's (0.7869). MMSkills is the only skill-library baseline and is not run on DiscoveryWorld; no other self-evolving or reflection baseline is compared.
- **No variance.** The captions of Tables 2 and 4 say "averaged over three runs" (Tables 5, 6 and 7 do not say how many runs) and no table gives an SD or CI, and the paper does not say what the three runs vary (evaluation repeats or re-evolved libraries). Gaps like the 0.61‡–1.23‡ points between adaptive and the best fixed depth cannot be judged against noise.
- **Small held-out set.** The out-of-domain test is two themes and 30 tasks; a 10.00-point gain is about 3 tasks‡ of 30 per run. The choice of held-out themes is not explained.
- **Test sizes do not reconcile.** Appendix A.1 states 116 official VAB-Minecraft test tasks and Table 3 states 36 in-domain DiscoveryWorld test instances, but the Table 2 success rates do not fall on those grids (for example 73.02 = 138/189 and 58.02 = 94/162‡, our reading; MMSkills on GPT, 70.10, is off the 1/189 grid; the held-out values do fit a 1/90 grid). Several values in Tables 4–6 (75.27, 74.58, 66.38, 72.06, 68.68, 54.63) fit neither the 1/189 nor the 1/162 grid. The paper does not explain the difference. We use the table values.
- **Cost is not reported.** There is no cost or time for building the library and none for the extra LLM calls per round (memory update, gate, retrieval, fusion). "Same interaction budget" means the same number of rounds, not the same compute. The Limitations section is one sentence about broader settings and the efficiency of online skill evolution.
- **Not ablated.** The Structured Abstractive Memory, the state gate (versus always retrieving) and the use of failed trajectories (versus successes only) have no ablation in the paper. Domain Skills also feed the memory updater, the gate and the fusion step in every variant, and no variant runs without them (the Table 5 "coarse" row retrieves only Domain Skills, which is a different thing). The retry budget and which LLM writes the skills and memory are not stated in the text we searched.
- **Wording.** The Limitations section speaks of "online skill evolution", while the method freezes the library at test time.
- **Case study.** The piston task (Appendix C) was selected as a diagnostic; the paper says it illustrates the mechanism and is not statistical evidence.

## Our read

HarnessRSI score **68**, band ★★, evidence level **retained**: the retained artifact (a skill library) helps on held-out themes. The paper reports held-out evaluation, a Trap-Skill ablation, an iteration ablation and a same-interaction-budget direct baseline across three backbones. It does not report variance, optimizer or inference cost, a compute-matched comparison, or a comparison of the evolution mechanism against other skill-learning methods beyond MMSkills on one benchmark; code is announced but not yet public.

*Numbers marked ‡ were computed or read by us from paper numbers; see SOURCE.md.*
