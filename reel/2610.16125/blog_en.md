# Passive imitation: a symbolic controller patches one stage at a time and reuses a fix proactively only after full-task confirmation — in one synthetic domain

*A Reel interpretation of "Imitation Holds a Key to Evolution: Localized Repair and Verified Skill Acquisition for Adaptive Agents" ([arXiv 2610.16125v1](https://arxiv.org/abs/2610.16125v1); Kai Hu, Hua Huang; HarnessRSI Daily score 68, ★★). Code: [FriendOfYishan/PI](https://github.com/FriendOfYishan/PI).*

## What the system changes about itself

This is not an LLM agent. It is a deterministic symbolic controller (no neural model, no gradient updates) working in one synthetic domain: a small simulated reporting pipeline with three ordered stages (select records, resolve revisions, normalize amounts). Each stage has 2–3 opaque actions (18 possible complete programs), and each of ten simulated tool worlds secretly permutes what the action identifiers mean for tool revisions A, B and C.

Two things change:

1. **The current program**, inside one episode: only the action at the failing stage is swapped.
2. **A persistent evidence table** keyed by (tool revision, stage, local goal) and action: success/failure counts, a cumulative "incentive" value, and the set of distinct fully accepted task ids. The table keeps task identifiers and, the authors note, can grow with the acquisition stream.

## Signal and keep/reject rule

- **Signal.** Structured feedback names the violated output path; a public lineage map turns the path into the producing stage; the request gives the local goal. The paper stresses that this feedback is strong, and that effect recognition and goal projection are programmed (a predefined effect vocabulary).
- **Candidates.** Actions with positive acquired evidence first, then source-demonstration fragments with the same stage and inferred effect (preferring the current revision), then every remaining typed action.
- **Small trial.** The patched program is run on a two-order-history subset; the patch is tentatively kept only if the target stage contract passes. The sign of the reward is not the criterion.
- **Full verification.** A final full-task audit against an independent reference computation decides acceptance.
- **What is stored.** Every small trial adds success or failure counts and an incentive value for the tried action during acquisition, whether or not the full task is later accepted; a fully accepted task adds one more success and one unit of incentive to each action in its final program, and its id to the confirmation set.
- **Proactive reuse.** An action may enter the initial program of a later task only after two distinct fully accepted tasks and a score q ≥ 0.7. During evaluation the evidence table is frozen (checked with state hashes).

## Headline, as reported (Table 1, K = 3 small trials, ten worlds, 60 tasks per group per world)

| Condition | Whole-trajectory replay | Full PI |
|---|---|---|
| Cold held-out compositions, final success | 6.17% | 100.00% (1.74 small trials) |
| First-submission success after 96 atomic acquisition tasks | 6.17% | 100.00% |
| Unseen tool revision C, final success (SD across worlds) | 22.67% (12.02) | 70.00% (21.20) |

Collateral regression (a stage that passed initially fails at the end) is 12.83% for replay and 0.00% for PI. The 600 cold composition tasks are ten worlds × 60 tasks that share a task generator, not 600 independent environments, and the SDs are across worlds, not task-level confidence intervals.

## The controls that decide whether the gain is real

- **Matched trial budget.** All controllers share one interpreter, the same tasks, public information and the same K. The whole-trajectory control can only replay complete source programs; the paper itself calls this "a representational disadvantage" on compositions, and says the comparison "does not establish a failure of modern memory-based agents".
- **The informative control: compositional repair.** It keeps local, goal-directed testing and two-task confirmation but removes the score threshold and the source-fragment evidence ranking only. In the reported settings it matches PI on success; its trials, work and collateral regression are reported only for cold K = 3 (Table 1), where they are also identical to PI, and Figure 2 draws its lines overlapping PI. The paper concludes the comparison "prevents attributing the composition result uniquely to the incentive score", and calls its own tie "plausible and substantively important". Proposition 2 argues the 0.7 threshold adds no delay *if* accepted tasks certify the unique correct action; the paper says this is "not a universal equivalence" and that noisy tests can invalidate the premise. The appendix code still ranks actions by an incentive score in other paths, so the control shares some helper ordering with PI: "a targeted control, not an independently engineered competing system".
- **Localization and goal matching.** Without localization, cold success falls to 9.50% with 41.83% collateral regression. Without effect-to-goal matching it is 92.50% (1.90 trials).
- **Small trials.** The no-small-trial variant also reaches 100.00% cold success with 0.00 trials and less work (58.82 vs 75.90 row-stage visits, cold held-out compositions).
- **Retention.** With retention disabled ("no retention"), cold final success is 100.00% but first-submission success after the 96 acquisition tasks stays at 6.17%. On those familiar-revision compositions, mean evaluation work is 75.90 without retention and 28.98 with it (a 61.82% reduction in an interpreter-work proxy; acquisition, demonstrations and retrieval are not amortized, and the paper says it is not a token or cost measurement). The paper notes this is not a clean ablation of the reward formula. On unseen revision C, retention adds nothing: no retention, PI and compositional repair are all 70.00% (SD 21.20), because version-keyed records do not authorize proactive reuse in C.
- **Demonstration-free enumeration.** "Self-trial only" (no source demonstrations, same localization, verification and learning) reaches 80.33% cold success and 100.00% learned first success.
- **Held-out and variance.** Final task identifiers are disjoint from acquisition, source and probe identifiers, but all tasks come from the same hand-designed generator. SDs are across ten worlds and are given only for the unseen-C column; the paper uses descriptive comparisons with no significance threshold. An exhaustive integrity suite checks 3,600 tasks × 18 programs (64,800 full/micro comparisons).

## Where the gain is absent or small

- **Unseen tool revision.** PI's 70.00% is below self-trial enumeration (79.00%) and the no-goal-matching variant (76.00%), but the gaps are smaller than the across-world SDs (21.20, 9.91, 19.57) and no test is run, so these differences are untested and within the SD. At K = 1, PI reaches 21.5%, against 24.0% for the no-small-trial condition; K = 1 values carry no SD, so this is likewise untested. At K = 6, PI, compositional repair and self-trial all reach 100%, and self-trial uses fewer trials (2.46 vs 2.67). The paper concludes that source-induced candidate ordering "is not uniformly useful" and can consume scarce trials.
- **Exploratory adaptation to revision C.** After 24 separately generated C tasks, PI's first-submission success rises from 6.17% to 54.33% (6 tasks), 92.33% (12) and 100% (24), and final success from 70.0% to 100%. The follow-up was designed after the primary results and is labelled exploratory. The 24-task stream contains each of the 12 multi-goal combinations twice, and the final unseen-C tasks are also compositions, so the request types appear to overlap (our reading of Sec. 6.2 and 7.4); the evaluation reuses the same frozen C tasks (the paper's Figure 2 calls this retention within a learned revision, not unseen-revision transfer). The compositional control follows the same curve, and the paper says the follow-up shows neither zero-shot transfer nor a benefit of numerical incentives over simpler verified reuse.
- **Ties.** After acquisition, PI, the compositional control, self-trial, no-localization and no-goal-matching variants all reach 100.00% first success, so the end state does not separate them; the differences are in cold repair and in the unseen revision.
- **Scope stated by the authors.** One synthetic domain (ten tool worlds sharing one generator), 18 programs and predefined stage boundaries; supplied role bindings, typed lineage and stage assertions; a microtest fixture that is identifying by construction; thresholds and cost coefficient not validated across environments. The study does not measure language-model tokens or bound persistent storage, and reports no comparative latency (the appendix gives only unprofiled whole-run times of about 21.93 s and 3.49 s, not offered as comparative). The paper cites Reflexion, ExpeL, Agent Workflow Memory and others but does not compare against them. Its stated conclusion is "a limited correction-and-retention mechanism rather than a unique incentive advantage or general intelligence".

## Our read

HarnessRSI score **68**, band ★★, evidence level **retained**: the retained evidence table improves later first submissions on tasks disjoint from those used to build it, and a no-retention ablation shows it. The paper reports held-out evaluation, a retention ablation, localization / goal / trial ablations at the same trial budget, ten worlds with across-world SDs for the unseen-revision column, exhaustive integrity checks with frozen-state hashes, and released code. It does not report an LLM-agent or natural-language setting, token or acquisition-inclusive cost, a comparison with external agent methods, or a comparison of improvement mechanisms beyond its own controls. The strongest control ties the method, which the authors state themselves.

*No numbers in this note were computed by us; see SOURCE.md.*
