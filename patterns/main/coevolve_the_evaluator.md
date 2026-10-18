# Co-Evolve the Evaluator
_id: `coevolve_the_evaluator` · sub-patterns: H24, H25 · corpus support: 25 papers (accepted 8 · rejected 5 · unlabeled 12)_

**Definition.** Treat the grader (rubric, verifier, reward criteria, test suite, benchmark) as an artifact that
evolves alongside the thing it grades instead of a fixed specification. Each revision is anchored to a small trusted
signal the graded candidates cannot see or write, so the evaluator tracks new failure modes without drifting into a
hackable target.

**Operational signature.** observe policy outputs → expose evaluator blind spots → revise criteria/tests → validate
against a trusted anchor → use as reward or acceptance gate

**When to apply.** When a fixed reward or test is stale, hackable, saturated or absent (open-ended, long-horizon or
subjective outputs) and you still hold some trusted signal (verifiable outcomes, oracle bits, sparse labels,
reproducible executions, checkable external facts) to certify each evaluator edit.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H24](../sub/H24.md) | Evolve Rubrics as Training Rewards | 9 | Regenerate per-query criteria from rollout contrasts, keep only discriminative, outcome-correlated ones, feed them to RL as dense reward. |
| [H25](../sub/H25.md) | Revise the Evaluator Against a Trusted Anchor | 16 | Repair or replace verifiers and tests when they disagree with an isolated anchor; accept an edit only if anchor agreement strictly improves. |

The split is by what the evaluator is for: H24 drives weight updates and is judged by the trained policy; H25 gates,
ranks or measures artifacts, and its own validity is the deliverable.

## Success conditions (from accepted work)
- **A named retention test decides which criteria survive.** Reward variance across samples, correlation with a
  verifiable outcome or a strict validation gate keeps the rubric from collapsing into a constant or a target.
- **The anchor is isolated from the candidates.** A separate surrogate verifier checked against opaque oracle bits,
  or expectations formed before the candidate is seen, removes the grader's drift toward agreeing.
- **Criteria are grounded in evidence the policy did not produce.** Retrieved evidence and paired positive/negative
  criteria are load-bearing in the high-fit accepted rubric-reward member.
- **New evaluation items earn their place through reproducible checks.** Recorded trajectories or deterministic
  probes let a benchmark get harder while staying solvable.
- **The evolved component is ablated and its cost is stated.** Of the 6 corpus members with evidence blocks, 2
  report a retained-artifact ablation; one reports 27000 H100 GPU hours beyond supervised fine-tuning.
- **The evaluator need not be prose.** Adaptive objective weights and online reward/bonus filtering were accepted as
  low-fit instances of the same move.

## Failure modes (from rejected work)
- **Closed self-contained loop.** The mechanism co-trains task generator, solver and reward model on one shared
  backbone, so nothing outside the loop checks the supervision it produces.
- **One-shot calibration on a small human batch.** The mechanism fits the evaluator once to a few human ratings and
  then optimizes against it, so its fidelity is bounded by that batch.
- **Selection and validation on the same labels.** Choosing criteria or demonstrations by correlation with the
  labeled set that also scores them is not an independent validity test.
- **Dynamic evaluation without a certificate.** Competition, prompt optimization or adaptive test hardening changes
  what is measured, but no anchor certifies that the new measurement is valid.

## Accepted vs rejected gap
The gap is about where the anchor sits, not whether the evaluator evolves. Accepted executions name an anchor the
candidates cannot write (hidden oracle bits, verifiable outcomes, retrieved evidence, reproducible executions), keep
the grader isolated from what it grades, and accept an evaluator edit only when it measurably improves against that
anchor. Rejected executions either have no outside anchor (a single backbone grading itself) or use a small human set
once, as both calibration and validation, and then optimize against it. The gap is partial and noisy: one accepted
and one rejected member describe nearly the same mechanism (safety tests regenerated from diagnosed failures), so
mechanism alone does not decide outcome here. Full-text corpus members, accepted and unlabeled alike, still list
anchor reuse, weak proxies and missing held-out tests against themselves. Rejected members were extracted from
abstracts only, so their reporting cannot be compared with accepted work; this gap rests on mechanism fields alone.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | — | — | — | insufficient labeled papers | — | — |
| iclr_2025_2026_high_fit | — | — | — | insufficient labeled papers | — | — |
| all_labeled | 13 | 8 | 5 | 0.615 | +3.9 pp | [0.355, 0.823] |

Base rates: 0.344 (iclr_2025_2026), 0.393 (iclr_2025_2026_high_fit), 0.576 (all_labeled). The move has no row in
either ICLR view, so there is no single-venue reading at all. In the pooled view its rate sits 3.9 pp above base with
a CI from 0.355 to 0.823 that comfortably contains the base rate: this is consistent with no effect. Acceptance is
not quality, n is 13, and with ~50 pattern tests per view even a nominally significant row could be chance; this one
is not even nominally significant. Read it as "executing this move neither helps nor hurts at the venue", and let
the anchor-design findings above, not the rate, drive decisions.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
- **Name the trusted anchor and its consultation budget.** Members flag repeated oracle consultation, repeated
  selection on a small validation set, and rollback that reads a locked test set as leakage paths.
- **Report evaluator validity separately from downstream gains.** Unlabeled members list unvalidated rubric fidelity,
  unchecked step attribution and limited human construct validation against themselves.
- **Show held-out separation.** Across the 6 corpus members with evidence blocks, held-out is `yes` in 2, `no` in
  2 and `unclear` in 2; expect the question.
- **Guard the anchor against leakage.** The leakage guard is `untested` or `unclear` in all 6 of those corpus members.
- **Compare evolving vs frozen evaluator at matched budget.** Budget matching is `unclear` in all 6.
- **State evaluator cost and variance.** Optimizer cost is reported (`yes` or `partial`) in 2 of 6, variance in 1.

## Cognitive barriers
- That the objective must stay fixed while the policy improves; a moving grader is treated as cheating rather than
  as the fix for a stale or hackable one.
- That a trusted signal, once used to calibrate the grader, keeps certifying it; in fact each reuse turns it into a
  training signal.
- That a capable judge can grade candidates it has already seen without bias; isolation, not judge strength, is what
  the accepted members buy.
- That the evaluator's correctness is implied by downstream gains; end-task improvement does not validate the rubric,
  the step attribution or the measurement.

## Lessons
### From accepted work
- Pair a dense, isolated surrogate verifier with an opaque oracle bit; strengthen tests only when they conflict.
- Keep criteria by discriminativeness plus agreement with something the policy cannot write.
- Form expected behavior before looking at the candidate, then judge conditioned on it.
- Let every new test or task earn entry through reproducible execution.
- Ablate the evolved evaluator component and publish its compute bill.
- Generate and filter reward candidates during policy improvement, not by retraining from scratch per candidate.
### From rejected work
- Design the external anchor in from the start; a backbone that grades its own tasks has nothing outside to check it.
- Budget for refreshing the anchor and re-validating the grader, not a single calibration batch.
- Do not validate criteria on the same labels used to select them.
- Making evaluation adaptive or competitive needs a certificate that the new measurement is valid.
- Do not over-read any single rejection here: a near-identical mechanism was accepted under another framing.
