# Crystallize Solutions into Executable Capabilities
_id: `crystallize_executable_capability` · sub-patterns: H06, H07, H08 · corpus support: 48 papers (accepted 20 · rejected 11 · unlabeled 17)_

**Definition.** Turn solutions that worked into verified executable artifacts — functions, tools, tool servers,
programmatic skills — and register them in the agent's action space, so later tasks invoke them instead of
re-deriving them. Execution-based verification gates admission, and composition lets the capability set grow
cumulatively.

**Operational signature.** solve or practice a task → abstract the solution into parameterized code → execute/test
to verify → register in the action space → compose on later tasks

**When to apply.** When recurring subproblems are procedural and an execution environment can tell working code
from broken code; the recurring part must be real, not assumed.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H06](../sub/H06.md) | Discover Skills Through Self-Directed Practice | 14 | Practice on a self-proposed curriculum before demand, admit only execution-verified, genuinely new skills. |
| [H07](../sub/H07.md) | Forge Tools When a Capability Gap Appears | 22 | When a live task exposes a gap, ground, build and repair a tool in a sandbox, then register it. |
| [H08](../sub/H08.md) | Maintain a Compositional Skill Graph | 12 | Restructure an existing library — trace-level repair, evidence-based promotion, rollback-gated refactors. |

The three split on the trigger: H06 grows the library ahead of demand, H07 grows it on demand, H08 does not grow
it at all but reorganizes it once size becomes the bottleneck.

## Success conditions (from accepted work)
- **The admission gate is execution, not judgment.** Replayed task success, evidence the skill was actually
  invoked, and an observable state change keep the action space from filling with plausible but broken code.
- **Each admitted artifact is a capability increment.** Admitting only what the current policy cannot cheaply
  re-derive, or only patterns that have recurred, keeps the library compact and every entry load-bearing.
- **The abstraction is validated, not just the original instance.** A tool that solves the problem it came from
  is a cached trajectory until it is checked on inputs it was not built from.
- **Repair is driven by obtainable signals.** Tracebacks, reproducible environment snapshots and trace-level
  responsibility let a first draft converge, and keep edits local instead of rewriting the library.
- **The retained library is shown to carry the gain.** A retained-artifact ablation is the most common strength
  among the 19 corpus members with a quote-grounded evidence block (yes in 10).
- **Generation is grounded where model knowledge runs out.** External code, documentation or demonstrations
  anchor tools the backbone could not write from memory.

## Failure modes (from rejected work)
- **The artifact is buried inside a larger architecture.** In four of H07's seven rejected members, forging sits
  inside a hierarchical memory, a multi-agent scheme, a workflow planner or a trained arbitration policy, so no
  isolated test of the executable artifact exists.
- **The "skill" stops being verifiable code.** Recasting skills as trained control policies with generated rewards
  or evolved symbolic interpretations forfeits the execution check that gives the move its advantage.
- **The skill source is a human, not the agent.** Encoding human corrections into stored skills makes the
  library grow through supervision, which weakens the self-improvement claim.
- **Reuse is bounded by a fixed input shape.** Templates generated offline from a schema are reusable only on
  inputs sharing that schema — caching, not open-ended capability growth.
- **Structure is validated by review, not execution.** Consolidating tools by semantic similarity and letting an
  agent judge that function was preserved leaves equivalence unverified (one H08 member; tentative).

## Accepted vs rejected gap
Judged on mechanism and design fields only, the separating variable is what the load-bearing mechanism is. In
accepted executions it is the executable artifact plus its execution gate: verified abstraction, admission only of
genuine increments, traceback-driven repair, rollback-protected refactoring. In rejected executions the
load-bearing mechanism is something else — a hierarchical memory, a trained forge-or-invoke policy, a workflow
planner, reward-trained or evolved skills, human-supplied corrections, or similarity-based consolidation checked
by review — and the executable artifact becomes one component among several. The gap is therefore in what the
paper claims is new, not in whether a library grows. Rejected members are mostly described from abstracts only,
so differences in reported limitations or evidence between the two sides are data-source artifacts and are not
used here.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 15 | 4 | 11 | 0.267 | −7.7 pp | [0.109, 0.52] |
| iclr_2025_2026_high_fit | — | — | — | insufficient labeled papers | — | — |
| all_labeled | 31 | 20 | 11 | 0.645 | +6.9 pp | [0.469, 0.789] |

Acceptance is not quality, and both intervals contain their base rates (0.344 and 0.576), so neither direction is
established. The two views point opposite ways for a structural reason: all 11 rejections sit in the ICLR
2025–2026 view, where outcomes of both kinds are observable, and there the move runs below base; the all-labeled
view adds 16 accepted members and no rejections, which lifts the rate. Read the ICLR row as the honest one: in a
recent, crowded venue this move is easily judged incremental, and seven of its rejections come from H07
(per its card, 2 accepted vs 7 rejected in that view). Of the sub-level rows, only H06 sits above base
(0.70, [0.397, 0.892]); with ~50 sub-pattern tests per view, that lone positive could be chance.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
Counts below cover only the 19 corpus members with a quote-grounded evidence block; they describe what this
family typically reports, not an accepted/rejected difference.
- **Held-out reuse.** Only 4 of 19 report clean held-out separation (5 report none);
  expect "were the tools harvested from the test tasks?" first.
- **A leakage guard.** None of the 19 reports a tested guard (none 2, untested 2, unclear 15); a disjoint
  practice/evaluation split with an explicit overlap check is an easy differentiator.
- **Comparison against other improvers.** Improver comparison is unclear in all 19; expect a request to compare
  with text-memory or prompt-optimization alternatives at equal budget (budget matching: yes in 1 of 19).
- **Full cost accounting.** Construction cost is reported in 3 of 19; reviewers will ask what building,
  validating and retrieving the library costs against the per-query saving.
- **Variance and correctness.** Variance is reported in 3 of 19, and members repeatedly concede that running
  without errors is not semantic correctness; expect seeds and a correctness check on known answers.
- **Backbone dependence.** Several members record that weaker backbones fail to populate useful libraries;
  expect results on more than one backbone.

## Cognitive barriers
- That the action space is fixed by the designer rather than grown by the agent.
- That a solution which worked once is a capability; it is only a cached trajectory until its abstraction is
  verified on inputs it did not come from.
- That a bigger or better-organized library is a better library; growth and structure pay only when each entry
  or edit is checked by execution and shown to help.
- That runtime tool creation is self-evidently valuable; without isolation and ablation it is indistinguishable
  from a strong backbone.

## Lessons
### From accepted work
- Gate admission on replayed execution — success, real invocation, observable effect — and keep rollback for
  edits that regress.
- Admit only what the current policy cannot cheaply reproduce, or what has demonstrably recurred.
- Let a strong model build tools once and a cheaper one invoke them; the amortization argument is clean when
  held-out queries confirm transfer.
- Separate abstract tool creation from concrete invocation and drive repair with execution tracebacks.
- Pair a held-out split with a retained-library ablation; together they carry most of the evidential weight.
- Once the library is large, localize faults through traces and promote primitives only on evidence of recurrence.
### From rejected work
- Folding the artifact into a broad memory or coordination architecture leaves nothing isolated to test.
- Delegating forge-or-invoke to a trained policy moves the contribution away from the executable artifact.
- Recasting skills as reward-trained policies or evolved symbolic interpretations gives up the execution check.
- Growing the library from human corrections rather than agent practice weakens the autonomy claim.
- Consolidating by semantic similarity with agent-review preservation leaves equivalence unproven (n = 1).
