# Make the Improver Editable
_id: `make_the_improver_editable` · sub-patterns: H19, H20, H21 · corpus support: 30 papers (accepted 12 · rejected 1 · unlabeled 17)_

**Definition.** Put the improvement procedure itself — optimizer or mutation prompt, meta-agent code, parent-selection
logic, or the memory/context mechanism through which the agent learns — inside the space being modified, so task
gains can compound into better future improvement. Progress is certified empirically, by evaluating descendants of
the edited improver, not by proofs.

**Operational signature.** improver proposes a change → apply it to the task agent and/or the improver → evaluate
descendants → retain (incumbent or archive) → recurse

**When to apply.** When the hand-designed improvement loop, not the task policy, is the bottleneck, and the products
of the loop can be scored cheaply and reproducibly enough to compare many improver variants.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H19](../sub/H19.md) | Apply the Improver to Itself | 14 | One lineage: run the optimizer on its own definition (or tune it by its products' scores) and replace the incumbent when descendants improve. |
| [H20](../sub/H20.md) | Branch Self-Modifying Agents from an Archive | 8 | Keep every self-edited agent in an open-ended archive and choose parents by estimated descendant productivity, not current score. |
| [H21](../sub/H21.md) | Redesign the Inner Learning Mechanism | 8 | Leave the improver alone; search over executable memory, retrieval, or context-construction designs scored by how well the agent learns with them. |

## Success conditions (from accepted work)
- **A named, immutable anchor.** Accepted members state which level stays fixed (outer algorithm, promotion rule,
  evaluator); without it, gains cannot be attributed to the edited improver.
- **Improver fitness = downstream fitness of its products.** Scoring an optimizer by what it produces needs no
  separate quality signal and keeps the improver from grading itself on a metric it edits.
- **Comparison against the fixed, hand-designed improver.** It is the direct test of the claim that editing the
  improver helps; 6 of the 12 corpus members with an evidence audit report it (the audit covers corpus papers only).
- **Search cost on the table.** 6 of the 12 audited corpus members report optimizer cost; one accepted member reports about $7000 for fifteen
  iterations — the move is expensive and reviewers can see it.
- **Selection that tolerates non-improving steps.** Archiving offspring that do not beat their parent, or picking
  parents by subtree productivity, lets the search escape local optima that a greedy lineage cannot.
- **A reified, swappable learning mechanism (H21).** Expressing memory/retrieval as one executable unit gives the
  strongest audited (corpus-only) profile in the parent: held-out separation and a retained-design ablation in 3 of 4 each.

## Failure modes (from rejected work)
- **Editing the task structure instead of the proposer.** The lone rejected member (low-fit) learns a reusable
  cross-task template and selection strategy; the edited object never generates future edits. The modes below come
  from limitations stated by corpus members, not from outcomes.
- **Self-modification breaks the loop.** Rewrites can terminate optimization; an accepted member reports fourteen
  percent of robustness trials ending worse than initialization. Rollback must be part of the method.
- **Benchmark reuse passes for self-improvement.** Repeated evaluation on small fixed subsets (held-out "no" in 2 of
  the 12 audited corpus members, "partial" in 2) lets the improver overfit the very score that promotes it.
- **Noise compounds across generations.** Variance across runs is reported by 1 of 12 audited; with few seeds, noisy
  evaluations falsely promote rewrites and outer-improver comparisons stay inconclusive.
- **The anchor leaks.** Unrestricted agents can call stronger models, LLM reviewers used as gates share blind spots,
  and evaluator edits require a trustworthy assessor — any of these voids the attribution.
- **Locally evolved mechanisms sold as general (H21).** Transfer is shown within related regimes; in one unlabeled
  member most transferred designs underperform a universal seed design.

## Accepted vs rejected gap
Only one member is labeled rejected, so the gap is read from design fields alone and is thin. In every accepted
member the edited object is something that produces future changes — the mutation or optimizer prompt, the
self-editing agent and its parent-selection rule, or the memory/retrieval mechanism the agent learns through — and
its fitness is the downstream score of what it produces. The rejected member instead runs a bi-level loop that
distils element-level prompt edits into a reusable cross-task template and selection strategy: the improver itself
stays outside the edit space, so the work reads as transferable prompt optimization rather than an editable
improver. The ICLR view adds that both of its 2 countable rejections fall in single-lineage self-application (H19),
while archive branching (H20) is 3 of 3 there — a design-level hint, at n far below the threshold. Evidence-profile
differences are not used here: the audit exists for corpus papers only.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 6 (countable) | 4 | 2 | insufficient labeled papers (n<10) | — (base 0.344) | — |
| iclr_2025_2026_high_fit | — | — | — | insufficient labeled papers (n<10) | — (base 0.393) | — |
| all_labeled | 13 | 12 | 1 | 0.923 | +34.7 pp (base 0.576) | [0.667, 0.986] |

Interpretation: outcome means venue acceptance, not quality. The all_labeled rate is high and its CI lower bound
(0.667) sits above the base, but this is one of ~50 tests per view, n is 13, and the corpus is topic-selected, so
it can be chance or selection. It also does not survive the ICLR view: there only 6 members are countable and 2 are
rejected, because one member accepted elsewhere was rejected at ICLR. By sub-pattern the ICLR split is uneven — H19
0 of 2 accepted, H20 3 of 3 — suggestive that single-lineage self-application is the riskier execution, but far too
small to rely on. Treat the evidence profile, not the rate, as the signal.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
_Counts are over the 12 corpus members with a quote-grounded evidence audit; they describe corpus papers only._
- **Edited vs fixed improver, same budget.** A comparison to the original improver (6 of 12 report it) at matched
  model-call or dollar cost (yes in only 2 of 12, partial 1); matched agent counts are not matched cost.
- **Selection set ≠ reported set.** A clean held-out split (yes in 4 of 12) and an explicit leakage guard (tested in
  0 of 12; 5 "untested").
- **Independent seeds of the whole search.** Variance across runs (1 of 12) and more than one lineage; a single
  deployment lineage cannot isolate the evolution gain.
- **Ablation of what was retained.** Which discovered components carry the gain (5 of 12 report a retained-artifact
  ablation); unlabeled members note discovered components lacking causal attribution.
- **Boundary and safety of self-edits.** What the improver may not touch, how crashes and regressions are rolled
  back, and whether generated code can bypass sandboxing.
- **Transfer beyond the search tasks.** Cross-task or cross-model transfer (5 of 12), and against a strong universal
  baseline design rather than only the seed.

## Cognitive barriers
- That the meta-level optimizer must stay fixed and human-designed; members show it can be scored by its products.
- That the best current agent is the best parent; descendant productivity can diverge from present score.
- That every retained change must improve immediately; stepping-stone agents are what let archives escape plateaus.
- That "the improver" means the proposer of edits; the mechanism through which the agent learns from experience is
  also an improver and can be searched directly.

## Lessons
### From accepted work
- Evolve the improvement rules with the task artifacts under one fitness, and name the level you keep fixed.
- Select parents by estimated productivity of their descendants and decouple evaluation scheduling from modification.
- Pool experience traces across parents so complementary discoveries merge instead of staying on isolated branches.
- Make memory/retrieval an executable unit and score it by learning gains plus resource use across a task stream.
- Report robustness failures (runs ending worse than initialization) next to the headline gain.
- Publish the search cost; it is large and reviewers will compute it if you do not.
### From rejected work
- One rejected member (low-fit) supports a single design lesson: learning a reusable cross-task template is not
  making the improver editable — put the proposer of edits, not only the task structure, in the edit space.
- The ICLR view's 2 rejections both fall in single-lineage self-application (H19) versus 3 of 3 accepted for archive
  branching (H20); with n this small treat it as a hypothesis to test, not a rule.
