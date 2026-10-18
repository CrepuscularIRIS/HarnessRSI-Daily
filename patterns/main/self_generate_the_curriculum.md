> **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing.

# Self-Generate the Curriculum
_id: `self_generate_the_curriculum` · sub-patterns: H22, H23 · corpus support: 63 papers (accepted 30 · rejected 13 · unlabeled 20)_

**Definition.** The system produces its own training tasks or environments, aimed at its current competence
frontier or at diagnosed weaknesses, and trains on them so the data distribution moves with the learner.
Validity and difficulty are controlled by verification, solver success rates, or failure analysis — and that
control, not the generator, is what the whole move rests on.

**Operational signature.** estimate frontier or weakness → generate tasks/environments → verify solvability and
difficulty independently of the generator → train the learner → re-estimate and regenerate

**When to apply.** When curated data saturates or is unavailable but generated tasks can be checked without
trusting whoever generated them, and the learner (or a teacher) is strong enough to propose valid tasks.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H22](../sub/H22.md) | Co-Train a Proposer Against a Solver | 30 | Train a proposer with a frontier reward (success band, uncertainty, regret, learning progress) against a solver reinforced on verifiable or consensus rewards. |
| [H23](../sub/H23.md) | Synthesize Tasks from Diagnosed Weaknesses | 33 | Read a measured deficit of the current learner and let a prompted, procedural or planned generator rewrite, compose or program tasks that target it. |

The split is who steers generation: a learned adversary (H22, inherits two-player instability) or a measured
diagnostic (H23, inherits diagnostic noise and generator ceilings). Both fail at the same joint.

## Success conditions (from accepted work)
- **A validity anchor the generator cannot game.** Execution, generated tests, runnable repositories, retrieval
  checks, documents hidden from the solver, or answer-preserving variants of solved problems keep hard tasks honest.
- **A frontier signal tied to that anchor.** Difficulty bands, uncertainty, or learning progress measured on a
  fixed held-out validation environment — not on the generator's own outputs — keep the curriculum learnable.
- **A real per-instance or per-skill diagnostic.** Failures, high-perplexity instances, forgetting and boundary
  signals, or frontier accuracy decide what to make; regeneration happens every round, not once.
- **Verified composition and stepping stones.** Harder tasks built from verified atomic ones, or conditioned on
  unsolved real-data goals, inherit known solutions and stay pointed at capabilities that matter.
- **Cost treated as a first-class problem.** Difficulty estimation needs repeated solver rollouts; one accepted
  member's main contribution is making nested proposer-solver sampling affordable.
- **Certification outside the loop.** Held-out and cross-task gains against static-synthetic, frozen-generator,
  or random/heuristic curricula.

## Failure modes (from rejected work)
- **Difficulty without validity.** In H22, 4 of 5 rejected members reward progress, difficulty, diversity or
  learnability with no stated independent validity check.
- **A schedule dressed as a diagnosis.** In H23, 3 of 8 rejected members raise difficulty by a generic schedule
  (deeper composition, difficulty buckets, a solved-level floor) rather than by a measured weakness.
- **A learned proxy as the only certificate.** 2 of 8 rejected H23 members certify with a reward model or a
  model-judged success signal, so the curriculum inherits the proxy's errors.
- **The learner as its own improvement source.** A rejected loop feeds a small student's action divergences
  back into synthesis, so what gets generated is bounded by what that student can reveal about itself.

All four are read from mechanism fields (load-bearing mechanism, signature). Rejected members were extracted
from abstracts only, so their missing limitations or evidence blocks say nothing about the papers.

## Accepted vs rejected gap
Across both sub-patterns the separator is not the generator but the check behind it. Near-twin mechanisms split
by outcome on exactly this: an accepted bandit learns which task categories help from a learning-gain proxy while
a rejected one schedules across difficulty buckets; an accepted composer verifies tool necessity at every level
while a rejected one only deepens chains and rewards outcomes; an accepted learning-progress proposer measures
progress on a fixed ground-truth validation environment while rejected ones reward progress or difficulty with
nothing independent underneath. The recurring rejected shape is a generator steered by a target it optimizes
(progress, diversity, mutation matched to ability, a reward-model gap) with no check it cannot move. Accepted
work is not clean either: five accepted H22 members list consensus labels reinforcing shared errors, and several
report plateaus or degradation after a few rounds.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 26 | 15 | 11 | 0.577 | +23.3 pp | [0.389, 0.745] |
| iclr_2025_2026_high_fit | 24 | 14 | 10 | 0.583 | +19.1 pp | [0.388, 0.755] |
| all_labeled | 43 | 30 | 13 | 0.698 | +12.1 pp | [0.549, 0.814] |

Base rates: 0.344 (iclr_2025_2026), 0.393 (high_fit), 0.576 (all_labeled). The lift is positive in every view,
but only the full ICLR interval excludes its base rate, and only by about 4.5 pp at the lower bound; restricting
to high-fit members (dropping 2) puts the lower bound just under base, and the all-labeled interval contains base
comfortably. With ~50 sub-pattern tests per view, one narrow exclusion can be chance. Neither sub-pattern
excludes base on its own (H22 [0.313, 0.832], H23 [0.332, 0.769] in the ICLR view). Read this as "the move is
not penalized and may be favoured", not as evidence that it raises acceptance; acceptance is not quality.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
- **What keeps generated tasks valid?** Expect this question first; name the anchor and show it is independent
  of the generator, especially when labels come from majority vote or a same-family judge.
Evidence counts below cover only the 26 corpus members with a quote-grounded evidence block (14 in H22,
12 in H23); they describe corpus papers, not rejected-vs-accepted differences.
- **Seed variance across co-evolution rounds.** None of the 26 reports it; a round-by-round curve with seeds and
  a stopping rule is an easy differentiator.
- **Budget-matched untargeted baseline.** 1 of 26 reports full budget matching, 5 partial; reviewers will ask
  whether targeted generation beats the same volume of untargeted generation.
- **Leakage guard.** Tested by 1 of 26; mandatory whenever the diagnostic reads benchmark failures or the
  benchmark is used for unlabeled adaptation, as one accepted member does.
- **Cost of the loop.** Generator plus nested sampling or repeated diagnosis-and-retrain cost is reported
  (yes or partial) by 5 of 26; give it in the same units as the gain.
- **Honest "data-free" claims.** Disclose seed sets, warm-up examples, teacher models and fixed validation
  environments; accepted members' own limitations show these are where the claim is punctured.

## Cognitive barriers
- **The training distribution is a fixed external input.** It can be an output of the system, re-drawn each round.
- **Difficulty is the objective.** Difficulty is only useful under a validity and relevance constraint; hardness
  rewards alone favour ambiguous or wrong tasks.
- **Self-generated means self-certified.** The generator and the certifier must be decoupled; consensus of the
  learner with itself is a noisy label, not a verifier.

## Lessons
### From accepted work
- Pick the validity anchor before the generator; choose domains where a generated task is checkable cheaply.
- Reward a difficulty band or uncertainty and filter for solvability before the learner trains on anything.
- Measure learning progress on a fixed held-out environment, never on the generator's own outputs.
- Seed generation from real failures or unsolved real goals and regenerate every round.
- Compose harder tasks from verified atomic ones so every level carries a known solution.
- Track forgetting next to weakness and constrain updates so targeted data does not erode earlier skill.
### From rejected work
- A proposer rewarded only for progress, difficulty or diversity does not carry the case.
- A generic difficulty schedule presented as self-generated curriculum reads as a knob, not a diagnosis.
- A learned reward model or model-judged success as the sole certificate imports that proxy's errors.
- Rewarding diversity, or mutating problems to match ability, still needs a check the generator cannot move.
- A loop that mines a small learner's own divergences is capped by that learner.
