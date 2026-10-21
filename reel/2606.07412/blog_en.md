# Socratic-SWE: turn repair traces into the next curriculum — with weight training inside the loop

*A Reel interpretation of [arXiv 2606.07412v1](https://arxiv.org/abs/2606.07412v1), **Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills** (HarnessRSI Daily score 64, ★★). No code link supplied. We read v1; the task flags an original candidate-metadata discrepancy naming an unavailable v2 (see SOURCE.md).*

## What the system changes about itself

Socratic-SWE distills successful and failed repository-repair traces into an **Agent Skill Registry**, then uses those skills to generate the next training tasks. A skill is a structured document with a name, natural-language description, applicability conditions and ordered operations. Traces contain repository inspection, edits, command execution and test outcomes; Qwen3.6-27B extracts successful strategies and corrective lessons. Semantic deduplication and trace-coverage filtering build the registry (§3.2).

The skills condition the **Generator**, not an evaluated frozen Solver with an inference-time skill library. Both Generator and Solver share Qwen3.5-9B weights, updated through GRPO and GDPO respectively. Thus the retained changes include the task curriculum and skills **and trained policy weights**. Our reading is that the results support a trace-guided training curriculum, not a weights-frozen harness-only improvement claim.

## The loop, and the keep/reject rule

1. The current Solver produces successful and failed traces; the extractor turns recurring behaviors into skills.
2. The Generator conditions on skills, repository context and Solver evidence to propose repair tasks. The implementation prompt describes a reversible semantic bug in one production file, with the original code serving as the reference fix; tests must not be edited (Appendix G).
3. Candidates must pass **format, grounding, execution stability and semantics/solvability** checks. The OAuthLib worked example additionally requires targeted tests to fail after injection, pass after reversing the patch, repeat stably, and an issue description that does not leak the oracle patch (Appendix H).
4. The Generator receives `Valid × cosine(candidate Solver gradient, validation gradient)`. The reference direction comes from trusted BeyondSWE tasks and is refreshed once per iteration. This is a **training reward**, not a documented hard rule that only positive-alignment tasks enter the pool: Equation 2 and Algorithm 1 admit tasks when `Valid = 1`. Appendix D/F discuss reward-based selection without specifying an additional cutoff; the precise selection implementation remains unresolved.
5. The Solver trains on accepted tasks using full-pass, partial-repair and regression-avoidance rewards. It sees task specifications and repository feedback, not the Generator's reference solution or verifier internals (§3.4). Updated behavior supplies the next traces.

**Initialization and refresh are underspecified.** Section 3.2 collects traces on a seed task set, whereas Appendix B says Socratic-SWE starts with seed repositories and no pre-existing SWE tasks or repair trajectories. Algorithm 1 takes a curriculum and registry as inputs and does not explicitly show registry refresh. The paper does not reconcile the bootstrap or refresh schedule; we do not infer which implementation ran.

## Headline result, as reported

Table 1 uses **Qwen3.5-9B**, three iterations of **12k validated training instances** each, **36k total**. SWE repair uses Bash-only mini-swe-agent; Terminal-Bench uses little-coder. The named evaluations are SWE-bench Verified (500 issues), Lite (300), Pro Public (731) and Terminal-Bench 2.0.

| Final-iteration pass rate (%) | Base agent | SSR | Socratic-SWE |
|---|---:|---:|---:|
| SWE-bench Verified | 42.60 | 47.00 | **50.40** |
| SWE-bench Lite | 29.67 | 34.00 | **36.67** |
| SWE-bench Pro Public | 17.24 | 20.66 | **22.85** |
| Terminal-Bench 2.0 | 10.11 | 12.36 | **14.61** |
| Overall: mean across benchmarks | 24.91 | 28.51 | **31.13** |

SSR is the strongest final-iteration baseline in each column, tied with Socratic-Zero on Terminal-Bench. The reported Verified gain is +7.80 points over the base and +3.40 over SSR. Gains are not restricted to one benchmark: the reported improvements over base are +7.80, +7.00, +5.61 and +4.50, respectively, with larger absolute changes on Verified/Lite. There is no per-repository breakdown to determine concentration inside benchmarks, and only one Solver model is evaluated.

**Overall is an average across benchmarks, not a mean across seeds.** The paper gives no seed identities, number of training/evaluation repetitions, standard deviations or confidence intervals for Table 1 or its ablations. We cannot infer a single run or statistical significance.

## The controls that decide whether the gain is real

- **Registry and trace ablations (Table 2, Verified, iteration 3).** Full 50.40; no Skill Registry 46.20; manual skills replacing trace distillation 48.00; GRPO replacing GDPO 48.60. They support contributions from skills, trace-derived content and Solver optimization, but do not isolate an inference-only library effect from policy learning.
- **Reward controls (Tables 3 and 6).** Hardness 47.40, uncertainty 48.20, Gaussian variance 48.80, gradient alignment 50.40; unnormalized inner product 49.40. The gradient-plus-difficulty hybrid reaches **50.60**, so the default is not the best configuration in the paper.
- **Extractor controls (Table 2).** Qwen3.5-9B self-extraction 49.80; Qwen3.6-27B default 50.40; Claude Opus 4.5 extraction 51.00. These are extractor variants, not repeated seeds; the 0.60-point changes have no uncertainty estimates.
- **Budgets and baseline access (Appendix B).** All self-evolving methods are stated to share Solver architecture, harnesses, interaction budget and validated-instance counts. Seed-requiring baselines receive 10% of SWE-smith task instances, but the paper does not map that initialization to each baseline individually. SPIRAL gets defect-injection/repair self-play and role-conditioned advantage estimation. R-Zero gets Challenger-generated tasks and majority-vote rewards. **Absolute-Zero does get execution-based verification**, without structured bug artifacts or skill guidance. Socratic-Zero gets a Qwen3.5-397B Teacher and distills its task-design strategy into its Generator. SSR gets code-removal/history-reversion bugs, execution consistency checks and binary Solver rewards. No reported baseline is granted Socratic-SWE's same trace-derived registry or BeyondSWE alignment reward. Baseline-specific tuning budgets are not reported; describing them all as lacking verification or distillation would be wrong.
- **Validation and default selection (Appendix E).** The 100-task BeyondSWE subset is excluded from Solver training and final evaluation, but its gradients shape generation. It is therefore a curriculum-optimization signal, not an untouched final test. Validation-size sensitivity is reported on **SWE-bench Verified**: 20 tasks gives 49.20, 100 gives 50.40, 200 gives 50.60. The authors motivate the 100-task default through this analysis, but do not state a separate split for selecting defaults/hyperparameters. The two independent rollout sets in Table 4 measure gradient stability, not benchmark-run variance.
- **Cost (Appendix F, Table 5).** On 8×A100-80G, each iteration takes 15.0 hours: proposal/validation 4.2, Solver rollout/execution 7.8, policy update 1.7, validation-gradient computation 0.5 and candidate scoring 0.8. The paper reports 1.3 hours alignment overhead per iteration, about 3.9 hours over the 45-hour three-iteration budget, and claims comparable total FLOPs to SSR. It gives no baseline-by-baseline timing/FLOP ledger and no separately itemized skill-distillation cost or explicit statement that extractor/Teacher costs are included. Most listed time is rollout/execution; the table does not split environment time from model time.

## Where the gain is absent or small

- **Not superior at every stage.** At iteration 1, Socratic-SWE's Terminal-Bench 12.36 equals SSR at iterations 2/3 and Socratic-Zero at iterations 2/3. Although §4.2 singles out SSR and Socratic-SWE for meaningful terminal gains, Table 1 also gives Socratic-Zero 12.36 (+2.25). We retain that baseline tie rather than imply a significance distinction.
- **Small design increments are uncertain.** The hybrid's +0.20 over gradient alignment and the 200-task validation set's +0.20 over the 100-task default have no variance/CI. They are numerical differences, not established reliable improvements.
- **Finite-pool saturation.** Section 5.1 extends training to five iterations and reports Verified 52.00 versus SSR 48.00, nearly plateauing. That extension is outside the three-iteration/36k headline budget. The authors explicitly limit the result to a fixed repository distribution, not open-ended improvement.
- **Leakage and generalization scope.** The paper names separate BeyondSWE validation and final benchmarks but does not identify the seed-repository corpus or establish repository/task disjointness between training traces and evaluation. The trace source's exact relationship to evaluation repositories is therefore unknown. No benchmark overlap/decontamination audit, pretraining-contamination analysis or temporal split is reported in the full paper. Hiding benchmark tests and preventing oracle patches in generated issue text are local safeguards, not proof against SWE-bench-style contamination. Broader repository/language transfer and settings without reliable execution tests remain unestablished.

## Our read

HarnessRSI score **64**, band **★★**, recorded evidence level **retained** (judgment batch b23). **Reports:** named separate evaluation benchmarks, transfer to terminal tasks, registry/trace/reward ablations, matched instance/interaction budgets and appendix runtime accounting. **Does not report:** run/seed uncertainty, baseline tuning budgets, comparable trace-registry access for baselines, itemized distillation cost, or a train/evaluation overlap audit.

The full PDF improves on one part of our stored judgment: optimizer cost was marked unclear, but Appendix F does report runtime. We leave the score and judgment untouched and record that correction in SOURCE.md. The key qualification is that skills steer a **weight-updating** training loop; the paper does not establish the same gains from a retained non-weight artifact alone.
