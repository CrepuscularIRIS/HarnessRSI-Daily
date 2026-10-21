# AGORA: a team can grow a better leader — but the right social structure is task- and model-dependent

*A Reel interpretation of [arXiv 2610.19799v1](https://arxiv.org/abs/2610.19799v1), **Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems**, by Seojin Hwang, Youngmin Choi and Hwanhee Lee (Chung-Ang University). HarnessRSI Daily score **65**, band ★★. No code URL is supplied in our record.*

## What the system changes about itself

AGORA is a controlled testbed for **social scaffolding**, not a new weight-training algorithm. It crosses team composition (all weak, all strong, or mixed) with four structures: none, collaboration, conformity and competition. The retained state includes per-role prompts, skills or memories, notes about teammates, and the team's roles, configurations and constitution. Model weights stay fixed.

The main weak model is Qwen3-30B-A3B-Instruct-2507; the strong model is Qwen3.6-35B-A3B, with thinking off and temperature 0.1. In mixed teams, the information/output bottleneck is strong: the web agent on GAIA, developer on LoCoBench, and both reader instances on OfficeQA Pro. The initial chairman and remaining roles are weak.

### Who scaffolds whom, and what is shared?

Agents exchange task messages through a mailbox. After a batch, **L2 relational notes** record the strengths, weaknesses and collaboration behavior of teammates they worked with. These notes enter the author's later system prompt, inform team revisions and are passed to the SkillOpt or MemRL updater. Tier 1 agents can read the whole team's notes; Tier 2 agents can read only their own. Collaboration encourages exchanging reasoning and checking each other; conformity encourages deference and contact only when stuck; competition discourages sharing and supplies comparative scores. The `none` condition skips L2, **not all task communication**.

Skills and memory banks are role-specific; the paper does not describe a single pooled skill or memory library shared by all agents. The constitution is team-wide. The strong model is also the fixed SkillOpt optimizer, MemRL memory writer and L2 contradiction judge, even in all-weak teams. A contradiction flag does not block saving a note. Thus the support comes from teammates' traces and observations, team rules, and—in two mechanisms—a strong external updater, rather than uniformly from a strong teammate tutoring every weak agent.

## The loop, and the keep/reject rule

1. **Solve training tasks as a team.** A chairman delegates and submits the answer. Success/failure, trajectories and peer observations provide feedback.
2. **L1 individual evolution.** Meta-Team edits its own prompt patches and skills immediately, using the role's own model, without an L1 gate. SkillOpt uses a strong updater to reflect on graded training trajectories, including prediction, ground truth and correctness or LCBS sub-scores; a candidate skill replaces the old one only if it is clearly better on validation. Only validation tasks that invoke the role count, so n can be smaller than 20. Its iteration-0 reference is measured once with the untrained template team under `none` and shared across SkillOpt conditions of the same composition; accepted scores then become the reference (Appendix D.5.1), unlike L3's fresh paired evaluation. MemRL stores successful and failed procedural scripts in a separate bank for each role, updates Q-values from task reward, and has no L1 gate.
3. **L2 notes and L3 team revisions.** Permissions and peer-review rules determine who can propose role additions/removals, prompt/configuration edits and constitution changes. Collaboration tallies reviews; conformity leaves the chairman in charge; competition adds comparative rankings.
4. **L3 validation gate.** Current and revised teams solve the same 20 validation tasks with the same seeds. All L3 changes are reverted only if the revision is worse and a one-sided binomial test finds the drop significant at α = 0.3. At a reference of 10 successes, a revised team with 8 or fewer is reverted. This is a harm filter, **not a requirement that every retained revision improve**. In the n = 20 example, SkillOpt's L1 gate instead requires at least 12 successes against a reference of 10. L3 applies at most two role changes and two patch bundles per iteration.
5. **Competition can rotate the chair after the gate.** The sole top-scoring role is promoted; this promotion is **not itself gated**. SkillOpt ranks by validation skill score, Meta-Team by training-task participation success, MemRL by mean memory Q. There is no minimum sample size, so a rarely called role can win on very little evidence.

SkillOpt and MemRL run four iterations; Meta-Team runs one sequential pass. The final team is frozen for test evaluation.

## Headline result, as reported

Table 4 reports test success rates as **mean ± SD over three evaluations of the same evolved team**. Evolution itself is run **once per condition**; these are not three independent evolution seeds and the SD does not quantify optimization uncertainty.

| SkillOpt, main Qwen pair | Selected team/structure | Team | Strong solo, also evolved |
|---|---|---|---|
| GAIA | Mixed, competition | 74.2 ± 3.8 | 49.2 ± 1.4 |
| LoCoBench | All strong, conformity | 87.2 ± 2.1 | 74.4 ± 2.5 |
| OfficeQA Pro | All strong, conformity | 36.6 ± 6.5 | 34.4 ± 0.9 |

The reported **25.0-point** headline is the GAIA comparison, not an average across benchmarks. The OfficeQA margin is smaller than the team's evaluation SD. Across mechanisms and compositions, the authors report that an appropriate social structure beats `none` in 24 of 27 settings. But the best structure is chosen **after the fact from test results**, not selected on an independent development set. These are descriptive maxima, not a deployable structure-selection rule established on untouched confirmation data.

## The controls that decide whether the gain is real

- **Retained-state and social-condition controls.** Preevolve baselines evaluate the original template teams with zero evolution. `None` teams still get their L1 mechanism, L3 changes, revision cap and the same L3 gate, but no L2 notes. This helps separate evolution alone from the social intervention. The intervention bundles information sharing, permissions, review and leadership, so it does not isolate each ingredient independently.
- **What each solo baseline gets.** Both weak and strong solo agents have **all benchmark tools** and evolve through the same L1 mechanism. They have no constitution, L2 peer notes or L3 team restructuring because they have no teammates. SkillOpt and MemRL retain their strong update model; Meta-Team uses the solo model itself. Solo is therefore not an unevolved or tool-deprived comparison, but it does not receive a comparable peer-scaffolding mechanism.
- **Splits and selection.** GAIA uses 17/20/40 train/validation/test questions without attachments; LoCoBench uses 80/20/99 Python scenarios; OfficeQA Pro uses 51/20/62 problems. Validation is fixed first, with the remaining tasks split using seed 42. Gates use validation; final evaluations use test. These are non-overlapping benchmark partitions, not demonstrated distribution-shift transfer. MemRL retrieval thresholds are explicitly tuned on **unlabeled validation–training input similarities**, without labels or scores. The selection split and search budget for other defaults are not fully specified, nor are separate baseline hyperparameter-search budgets. Additional GAIA role-composition variants order stronger roles using workload measured on scored **preevolve test sessions** (Appendix J).
- **Paired task analysis, with the authors' caveat.** Table 21 compares matched task/rollout pairs. Only 7 of the 27 best-structure-versus-none comparisons have p < 0.05. The paper explicitly calls the p-values optimistic: the best structure was selected from three and rollouts of the same task are not independent. They are exploratory noise checks, not confirmatory significance tests.
- **Leader diagnostics are suggestive, not a pure sharing ablation.** On GAIA under SkillOpt, the team-grown leader accepts 2 of 4 candidate skills versus 0 of 4 for strong solo; their success rates are 74.2 and 49.2 (Table 6). On LoCoBench both accept 2 of 4, yet the team-grown leader follows its evolved constitution and scores 87.2 versus 74.4. Multiple retained components and leadership differ; these comparisons do not establish the isolated causal effect of sharing notes.
- **Leakage scope.** Training ground truth is explicitly available to SkillOpt's updater. The validation set repeatedly gates retained changes and can determine competition leadership; it is not an untouched test. The paper states disjoint splits, but reports no empirical audit for evaluation-content leakage through web access or retained artifacts. Web access is unrestricted in the main and additional experiments. This leaves contamination untested; it is **not evidence that leakage occurred**.

## Where the gain is absent or small

- **OfficeQA is not rescued by a mixed team.** Its best mixed row is 21.5 ± 2.4 (SkillOpt, `none`), below even unevolved strong solo at 28.5 ± 0.9. Competition promotes weak roles and drops this mixed SkillOpt team to 15.1 ± 3.3. Even the all-strong 36.6 ± 6.5 versus evolved solo 34.4 ± 0.9 is a thin margin inside evaluation noise. Large gains are concentrated in GAIA's mixed team and selected LoCoBench settings, not evenly across all tasks.
- **Evolution alone sometimes works.** GAIA all-strong SkillOpt already scores 60.8 ± 5.8 under `none`; its best social structure, conformity, scores 57.5 ± 6.6. The finding is not that an explicit social structure is always necessary.
- **Competition can collapse a team.** LoCoBench all-weak Meta-Team falls from 43.4 ± 5.3 under `none` to 22.6 ± 10.5 under competition. More authority movement is not automatically better.
- **Other model families do not reproduce a universal best scaffold.** Gemma-4 on GAIA, SkillOpt mixed: `none` 37.5 ± 0.0, competition 32.5 ± 5.0. Mistral on LoCoBench, SkillOpt all-strong: best social row 58.9 ± 4.7 (collaboration), below evolved strong solo 80.5 ± 3.5; conformity reaches only 31.3 ± 5.6. These experiments rerun evolution with other models; they do not transfer an already learned artifact.

## Communication and optimization cost

Sessions share a 900-second limit, but teams get 100 messages versus solo's 50, with 50 steps **per agent**. Output allowances also differ by role. Time/message-limit terminations count as failures in every score, including both gates; crashed sessions are excluded (§4, p6; Appendix F.1). No crash counts or effect on results are inferred. This is only partial budget matching, not equal total tokens or calls. Reflection has its own time budget, and each L3 gate adds 40 sessions per iteration, besides SkillOpt's L1 checks.

Table 5 shows **deployment-session** savings in selected cases: GAIA mixed SkillOpt competition uses 19.4 LLM calls versus 46.8 for the unevolved mixed team and 22.6 for unevolved strong solo; LoCoBench all-strong SkillOpt conformity uses 18.3 versus 73.3 before evolution. These are not total optimization costs or a comparison with evolved-solo cost. Coordination can instead add expense: LoCoBench mixed SkillOpt conformity uses 107.3 calls versus 80.0 before evolution, while scoring 79.1 versus 80.5.

Appendix G reports whole-experiment wall-clock ranges: GAIA SkillOpt 4.5–16.0 hours and LoCoBench SkillOpt 14.5–37.2 hours on a GPU pair. It does not separate optimizer-only tokens/dollars or provide a complete matched-cost solo comparison. The authors also acknowledge that shared-GPU serving load plus the time limit may partly explain why reducing active agents helps.

## Our read

HarnessRSI score **65**, band ★★, evidence level **retained**. The paper reports separate test evaluation, preevolve and social-condition controls, repeated **evaluation** variance, partially matched session budgets, process diagnostics and additional model-family experiments. It does not establish repeated-evolution robustness, an independently selected universal scaffold, a fully matched optimization-cost comparison, artifact transfer or an empirical leakage audit. Appendix G does provide whole-experiment timing, more cost information than the board's `optimizer_cost: unclear` field alone conveys; it is not phase-separated optimizer accounting.

**Takeaway:** a team can help an agent acquire a better retained harness and then become less necessary. AGORA's strongest evidence is that who leads and how coordination is permitted materially affect that process—not that competition, conformity or more agents reliably wins everywhere.
