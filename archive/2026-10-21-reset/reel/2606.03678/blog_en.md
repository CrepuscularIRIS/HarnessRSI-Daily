# EvoDrive: evolve the crash-test generator, not the driver — and keep realism in the loop

*A Reel interpretation of **EvoDrive: Pareto Evolution for Safety-Critical Autonomous Driving via Self-Improving LLM Agents**, [arXiv 2606.03678v2](https://arxiv.org/abs/2606.03678v2). HarnessRSI Daily score **65**, band ★★, evidence level **improver**. No code repository supplied.*

## What the system changes about itself

EvoDrive edits a reusable **scenario generator**: bounded parameters, a typed simulator-operator graph, a scene-conditioned selection policy, and reusable interaction mechanisms. It does not train the ego driving policy inside evolution, change the simulator's scoring rules, or allow arbitrary generated code. All LLM roles use GPT-5.5 through Codex CLI with xhigh reasoning.

The objective is not to make driving safer directly: it is to find **more effective, still-plausible attacks on a fixed driver**. MetaDrive attack is target collision rate. Realism aggregates map/lane validity, initial non-overlap, collision validity, route progress, trajectory continuity, and bounded acceleration/jerk; the reported realism penalty is RP = 100(1 − R). CARLA attack is CR(1 − OS), combining collision rate and the driver's overall score. Its realism score ARS multiplies validity by a weighted combination of kinematic, map, interaction, and distance consistency, with weights 0.40, 0.30, 0.20, and 0.10. These are simulator-based diagnostics, not a certified probability of real-world safety.

## The loop, and the keep/reject rule

1. An actor reads the active parent, declared edit interface, search target, and memories of previous attempts, then proposes a bounded typed patch.
2. Structural, attack, realism, and isolation critics approve, request repair, or reject. A deterministic validator checks schema, parent identity, legal edits, protected resources, and compilation; failure stops simulation.
3. A **world evaluator** selects, rejects, or audits candidates before expensive closed-loop simulation. High uncertainty can force an audit rather than rejection.
4. Simulator labels decide archive membership: nondominated attack–realism trade-offs are kept. Active successors must satisfy hypervolume improvement, a local-frontier push, or a bounded parent trade-off rule. Failures remain as negative memory, not successful archive entries.
5. A separate world agent can change the routing evaluator's features, calibration, ranking, uncertainty, or thresholds. A deterministic judge promotes updates using earlier simulator evidence. This evaluator cannot rewrite simulator labels or admit candidates directly.

MetaDrive uses 10 epochs with 20 parallel proposal slots per epoch and rotating 20-scene development windows. Of 500 Waymo-derived scenes, 240 support evolution, 160 additional scenes expand downstream training, and 100 are protected for evaluation. The active generator and up to three frontier descendants are selected on the **evolution pool**, then frozen before test. The archive uses R ≥ 0.95 and relative tolerance 0.05. The paper does not describe which split, if any, selected these defaults or report baseline hyperparameter-tuning budgets.

## Headline result, as reported

Table 1 averages MetaDrive results over IDM and RL ego policies. Its PF-Area@3 is the percentage increase in attack–realism hypervolume after adding up to three eligible descendants, **not a reduction in collision risk**.

| Generator | Parent attack → evolved | Parent RP → evolved | PF-Area@3 |
|---|---|---|---|
| CAT | 0.345 → 0.330 | 10.66% → 3.85% | +7.4% |
| ADV-BMT | 0.260 → 0.295 | 2.27% → 1.77% | +18.7% |
| AT | 0.231 → 0.265 | 0.09% → 1.06% | +14.9% |
| SEAL | 0.211 → 0.245 | 0.07% → 1.02% | +15.9% |

All eight generator-family averages improve frontier area, but several buy attack with higher realism penalties. These are **parent-versus-descendant comparisons**, not victories over the strongest independent baseline in each metric. Table 1 gives no variance, confidence intervals, or evolution-run count.

CARLA/SafeBench uses four evolution rounds over eight scenario families and ten routes per family. Table 3 reports attack/ARS changes for AdvSim (0.260 → 0.382 / 0.544 → 0.615), AT (0.197 → 0.330 / 0.514 → 0.607), ChatScene (0.394 → 0.507 / 0.729 → 0.924), and Human (0.264 → 0.301 / 0.856 → 0.927). Their PF-Area@3 gains are 142.5%, 255.7%, 143.5%, and 73.7%. Balanced family-route selection reduces unequal group weighting; the table reports no run count or uncertainty. Unlike MetaDrive, the generator-reporting protocol does not explicitly identify a disjoint evolution/test scenario split, so overlap cannot be ruled out.

## The controls that decide whether the gain is real

- **Component ablations, with actual repetition.** Table 4 reports three independent ADV-BMT evolution runs against the RL ego policy: full PF-Area@3 **31.0 ± 4.2%**, without critic/repair **26.8 ± 3.8%**, without long-term memory **19.1 ± 3.5%**, non-LLM Pareto search **10.6 ± 2.8%**, and actor-only with matched LLM calls **21.2 ± 4.0%**. The paper does not specify whether these ± values are SD or SE. The full and no-critic ranges overlap; no significance test is reported. This repetition does not establish multi-run uncertainty for Tables 1 or 3.
- **What each control actually gets.** Every MetaDrive source family is represented through a declared interface and can produce descendants entering the same archive. Actor-only explicitly matches total LLM calls. Non-LLM Pareto search is a separate proposal control, without an explicit matching-budget statement. Attack-only and OpenEvolve scalar search use the same evaluation setting and metrics (Table 8), but their total simulation/tuning budgets are not specified. The three-descendant frontier reporting cap does not establish equal total simulation cost against the unevolved parents.
- **The improver itself is compared.** Table 5 reorders the same candidate sequence under the same simulation budget. Static versus evolving routing requires **0.60 ± 0.04 versus 0.51 ± 0.03** normalized evaluations to reach 90% hypervolume; normalized top-10 yield is **1.30 ± 0.06 versus 1.44 ± 0.05**. Evolving routing uses labels from earlier rounds. Run count and the meaning of ± are not given for this table.
- **Independent realism check.** Table 2 uses held-out rollouts and maneuver-matched naturalistic references only after evolution. Eight-family mean motion JSD improves **0.073 → 0.067**, interaction JSD **0.091 → 0.081**, and out-of-support rate **7.4% → 6.0%**. The naturalistic split-half reference remains better: **0.022**, **0.028**, **1.4%**.
- **Transfer is limited but present.** Frozen scenarios selected under SAC also increase attack on CARLA BasicAgent: **0.0612 → 0.1434**, versus **0.3759 → 0.4477** on the search SAC policy (Table 17). This is cross-policy scenario transfer, not broad cross-task or real-world transfer. Table 16 separately tests three parameter starts for each of two ChatScene families.
- **Cost is one representative run.** Appendix C.5 reports 232 role calls, 5.097M cached input tokens, 0.159M output tokens, 13.5 hours end to end, and estimated API cost $5.88 for a four-round CARLA run. This is not a full simulator-compute bill or a matched baseline cost comparison.

## Where the gain is absent or concentrated

**MetaDrive is policy-dependent.** ADV-BMT's frontier gain is **33.4% on RL but 4.0% on IDM**; AT shows the reverse emphasis, **25.6% on IDM versus 4.1% on RL** (Table 11). LLM-Attacker on IDM, KING on RL, STRIVE on RL, and SAGE at preference w = 0.50 on RL have **0.0%** frontier gain. CAT's active attack rate falls even while realism improves.

**Better aggregates do not make every CARLA scenario better.** ChatScene crossing attack CR falls **0.930 → 0.870**; AdvSim and AT turning-obstacle ARS stays **0.000** (Tables 12–14).

**Downstream safety gains are concentrated.** For SAC trained on original versus evolved ChatScene scenes, route-disjoint test average CR falls **0.163 → 0.106**, and OS rises **0.854 → 0.884** (Table 6). The CR reductions occur in straight-obstacle, turning-obstacle, and right-turn scenarios; right-turn goes **0.350 → 0.000**. Vehicle-passing CR worsens **0.050 → 0.200**, unprotected-left remains **0.500**, and Lane Change, Red-light, and Crossing remain at zero. Unprotected-left OS also worsens **0.711 → 0.682**. Table 6 gives no run count, variance, or CI. The three-run statement applies to **MetaDrive downstream Figure 7**, not this CARLA table. MetaDrive downstream training deliberately reuses the evolution scenes plus the additional training scenes; generator selection and subsequent policy training are separate stages.

## Our read

HarnessRSI score **65**, band ★★, evidence level **improver**. The strongest evidence is a bounded retained generator, protected MetaDrive testing, memory/call-matched actor ablations, and a static-versus-evolving evaluator comparison on the same candidate sequence and simulation budget. The stored judgment's variance field is incomplete: the full paper does report repeats in Table 4, initialization sensitivity in Table 16, and three-run downstream MetaDrive curves. We leave the judgment files unchanged and scope each repetition to its own experiment.

The paper does not establish equal total simulation/tuning budgets for all baseline comparisons, report headline-table CIs, test leakage empirically, or establish deployment safety. Its validators enforce admissibility within the declared simulator interface; they are not formal guarantees that a driving policy is safe. The authors explicitly limit validation to simulation and note possible failures on unseen policies, platforms, and real-world deployment; hardware-in-the-loop validation remains future work.
