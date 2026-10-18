# Diagnose Whether Self-Improvement Is Real
_id: `diagnose_self_improvement` · sub-patterns: H32, H33, H34, H35 · corpus support: 54 papers (accepted 10 · rejected 9 · unlabeled 35)_

**Definition.** Instead of building a better self-improving system, build the experiment that tests whether an
existing one improves at all. Controlled interventions, stream benchmarks, frozen-evaluator workspaces, or attacks
isolate whether persistent self-modification *causally* yields transferable, safe gains. They separate update
quality, uptake, extra search compute, feedback leakage, and contamination.

**Operational signature.** name the confound behind a rising evolution curve → build a matched, frozen, held-out,
or adversarial condition that kills it → measure the isolated effect → report the failure mode as the finding

**When to apply.** When a headline gain could be explained by extra attempts, reused verifier feedback, memorized
tasks, or executor strength. Also when persistent state is written from untrusted or self-generated inputs and
is only ever evaluated per session.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H32](../sub/H32.md) | Isolate Effects with Controlled Interventions | 13 | Cut the causal chain on an existing system (content perturbation, frozen generation, updater × user cross, compute-matched baseline) |
| [H33](../sub/H33.md) | Benchmark Persistent Improvement over Streams | 18 | Ordered task streams with a frozen artifact, separate validation/ID/OOD/replay views, and cost accounting |
| [H34](../sub/H34.md) | Benchmark Agents Doing AI R&D | 10 | Budgeted workspace, protected protocol, frozen evaluator that reruns the submitted artifact from scratch |
| [H35](../sub/H35.md) | Audit Persistence as an Attack Surface | 13 | Plant poisoning, tampering, or benign misevolution in persistent state and trace it across sessions and generations |

## Success conditions (from accepted work)
- **One alternative explanation, one targeted cut.** Accepted diagnostics name the cheaper story (search budget,
  prompt length, feedback reuse) and pick the single intervention that falsifies it.
- **The retained artifact is ablated directly.** In the evidence audit (corpus papers only), 4 of the 5
  accepted controlled-intervention members report a retained-artifact ablation. It is the move's signature.
- **Evaluation is held apart from the loop.** Held-out or separated tasks, a frozen scorer, and leakage that is
  *tested* rather than assumed. Of the 6 audited corpus papers with a tested leakage guard, 3 sit here.
- **Negative and conditional results are the headline.** Noisy memory hurting, poor transfer of evolved
  artifacts, fabricated guardrails: accepted work reports these as findings.
- **A mitigation or acceptance rule is paired with the diagnosis.** Gated consolidation, warrant-aware edit
  acceptance, or a defense, even one that only partly restores performance or safety.
- **The isolating control *is* the mechanism.** Frozen-generation feedback injection, compute-matched held-out
  comparison, a planted nonexistent failure, a protected protocol: the cut carries the paper, not a side ablation.

## Failure modes (from rejected work)
- **An end-to-end sweep passed off as a diagnosis.** Comparing model pairings or methods without a matched
  control leaves the gain confounded with budget.
- **A normative benchmark with no frozen view.** Arguing that agents *should* be tested on lifelong learning,
  then headlining that current models fail, reads as descriptive rather than diagnostic.
- **A benchmark bundled with a new method.** The contribution splits and neither half is evaluated cleanly.
- **Single-interaction attacks with no persistence trace.** Showing one injected record redirects later answers,
  without tracing it across sessions or generations, leaves the "persistent" claim unexamined.
- **A defense offered in place of a diagnosis.** Consensus self-validation over memory-derived reasoning paths
  is proposed as the fix before the poisoning dynamics it targets are isolated.
- **Relative standing scored instead of artifact effect.** Iterated open-ended tournaments rank agents but do
  not show that the strategy code they produce improves learning.

## Accepted vs rejected gap
Across all four sub-patterns the split is *attribution versus description*. Accepted executions attach a
measured, isolated effect to a specific variable, such as memory content, feedback subset, edit warrant, the
update path of an attack, or a protected protocol. They also say where the effect stops holding. Rejected
executions mostly *exhibit* a phenomenon: models are deficient on a stream, a poisoned record redirects an
answer, alignment tips in a testbed, optimization still helps. They do so without the matched, frozen, or
paired control that would localize the cause, and often with a new method or defense attached. The skew is also structural. 5 of the 6 labeled controlled-intervention members were accepted, but
all 3 labeled stream-benchmark members were rejected. Each sub-pattern's labeled n is under 10, so this
is a direction to check, not a rate. This gap rests only on design fields (problem, assumption broken,
signature, mechanism). Most rejected members were extracted from abstracts alone, so their missing limitations
and audit blocks reflect the data source and are not used as evidence here.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | — | — | — | insufficient labeled papers (base 0.344) | — | — |
| iclr_2025_2026_high_fit | — | — | — | insufficient labeled papers (base 0.393) | — | — |
| all_labeled | 19 | 10 | 9 | 0.526 | −5.0 pp (base 0.576) | [0.317, 0.727] |

Outcome means venue acceptance, not quality. The pattern falls below the reporting threshold in both ICLR
views, so the only rate is the pooled all-labeled one. That rate is 5 points under base with a CI spanning
roughly 0.32 to 0.73. The move is neither rewarded nor penalized as a category, and nothing here is
significant. About 50 sub-pattern tests run per view, so even an apparent signal at this n would need
replication. The decision-relevant variation lives *within* the pattern, in how the diagnosis is executed. Venue
membership alone says nothing.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
- **Budget matching.** Is the baseline given the same search, inference, and feedback budget? Of the 11 corpus
  papers with an audit block, only 2 say yes and 1 says partial. Every H34 and H35 block leaves it unclear.
- **Variance.** Are there repeated runs or seeds? Only 1 of the 11 audited corpus papers reports variance.
  "Single evolution run per setting" and "single seed" recur in corpus papers' stated limitations.
- **Held-out separation and leakage.** Is the scorer outside the loop, and is leakage tested? Expect questions
  about selection and official evaluation sharing subsets, and about memory-source problems reused in regression tests.
- **Improver comparison.** Is the diagnosed system compared against alternative improvers? None of the 11
  audited corpus papers reports one (no 2, unclear 9).
- **Cost of the thing audited.** What does the evolution or optimizer cost? Only 2 of the 11 audited
  corpus papers report it (yes 1, partial 1). No audited attack paper reports the cost of the evolution it targets.
- **Generality of the cut.** Does an attribution made at a frozen generation, in one micro-lab, or on one
  benchmark family transfer? Corpus papers flag this ceiling themselves.

## Cognitive barriers
- That a rising score curve over evolution steps is evidence of genuine self-improvement.
- That memory being present and helping means the agent *uses its content*. Format and prompt effects can carry
  the gain.
- That a stronger task-solver is a better updater, or gets more out of an evolved artifact. Update quality and
  uptake are separate capabilities.
- That safety checked per entry or per session covers a system whose persistent state keeps changing.

## Lessons
### From accepted work
- Perturb what the retained state *says*, not only whether it exists, and keep raw episodes beside consolidated ones.
- Freeze at a generation and inject feedback subsets to get marginal and interaction effects with matched budgets.
- Match feedback and inference budgets, evaluate on held-out tasks with leakage tested, and report poor transfer.
- Protect the protocol, rerun the submitted artifact from scratch across settings, and report optimizer cost.
- Attack the *update path*, audit safety before and after evolution, and probe fixes with a planted nonexistent failure.
- Bound every claim in writing: seeds, threat model, partial mitigation, scale.
### From rejected work
- A sweep over pairings or methods is not an intervention. It cannot say where a gain comes from.
- A stream benchmark without a frozen, held-out transfer view measures in-situ search, not persistence.
- Do not ship a benchmark and a method in one paper unless each is evaluated on its own.
- A poisoning or drift result needs cross-session or cross-generation tracing to support a persistence claim.
- A defense proposed before the threat is isolated, or a tournament rank, does not show what persistence does.
- Rejected labeled members number 9, mostly abstract-only. Read these as cautions about design, not evidence.
