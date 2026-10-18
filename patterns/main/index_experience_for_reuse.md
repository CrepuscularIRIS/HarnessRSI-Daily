# Index Raw Experience for Reuse
_id: `index_experience_for_reuse` · sub-patterns: H03, H04, H05 · corpus support: 86 papers (accepted 24 · rejected 16 · unlabeled 46)_

**Definition.** Keep experience close to its raw form — trajectories, workflows, cases, facts — and put the
engineering effort into how that store is organized and when it is consulted, so the right precedent is found
and adapted as the store grows. The gain is claimed from recall and adaptation of precedent, not from
compressing experience into abstract lessons.

**Operational signature.** record episodes/cases → structure the store (index, hierarchy, graph, tiers) →
retrieve relevant precedent when needed → adapt it and append the new outcome

**When to apply.** When tasks recur with concrete details that abstraction would lose, and retrieval quality —
not storage capacity — is what limits the gain.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H03](../sub/H03.md) | Retrieve and Adapt Precedent Cases | 44 | Store gated, de-instantiated cases; filter, match, re-bind, append. |
| [H04](../sub/H04.md) | Restructure the Memory Substrate | 33 | Reshape the store (tiers, graphs, clusters, paging) with local updates and decay rules. |
| [H05](../sub/H05.md) | Retrieve Only When Needed | 9 | Make retrieval a triggered, gated decision with a no-retrieval fallback. |

The three sub-patterns split the move along one axis each: *what unit* is reused (H03), *what shape* the store
takes (H04), and *when* it is read (H05). They compose — a gated trigger can sit on top of a structured case base.

## Success conditions (from accepted work)
- **The case unit is re-bindable.** Stripping instance-specific values or cutting episodes into functional
  subtasks is what lets precedents compose instead of merely resembling the new task.
- **Writes are gated by an external check.** Admitting cases only after an executable test, simulation, or
  outcome threshold keeps unsupported patterns from accumulating as the store grows.
- **Content and index are decoupled.** Stable consolidated content reached through separate cues, pointers, or
  cluster boundaries lets one item be found by several paths without duplication.
- **Retrieval is selective, not maximal.** Category filters, caps on injected cases, relevance gates, and
  triggers at uncertain steps keep context small; injected-but-irrelevant experience is a stated harm.
- **The store is certified by removing it.** Among the 24 corpus members with a quote-grounded evidence
  audit, the retained-store ablation is the most often reported item (12 of 24).
- **Updates are local and cheap.** Accepted structure-centric designs touch only affected clusters or subtrees,
  use separate update rates for fast facts and slow traits, and defer heavy consolidation off the online path.

## Failure modes (from rejected work)
_Derived from rejected members' mechanism fields only; their limitation and evidence fields come mostly from
abstracts and are not comparable with corpus papers._
- **The store is incidental to the method.** Several rejected designs are exemplar selection, synthetic
  demonstrations, context-chunk covering, or simulation-scored best-of-N — not a growing, reused store;
  7 of 16 rejected members are low-fit to the move.
- **Similar-looking is taken as applicable.** Retrieval that trades task-distribution distance against
  utility matches on resemblance, not on whether the precedent's local reasoning transfers.
- **The store is built from the test stream.** A knowledge bank updated continually from test inputs makes the
  gain inseparable from the evaluation stream.
- **Model outputs enter memory without an external gate.** Stored intermediate answers or generated memories
  are admitted on the model's own word, so errors can propagate as the store grows.
- **Curation does not scale.** Manually verified examples undercut the "improves with use" claim.
- **A new store shape stands in for an argument.** Rejected H04 designs (sentence graphs, native key-value
  memory, evolving schemas, profile-plus-hierarchy) resemble accepted ones; shape alone does not separate.

## Accepted vs rejected gap
Store shape does not separate the two sides: rejected members propose graphs, hierarchies, profile stores,
and case bases that resemble accepted ones. The visible difference in the design fields is whether the store
is the load-bearing, externally gated, reusable artifact. Accepted designs define a clean, re-bindable unit
(de-instantiated routines, functional subtasks), admit cases only through an executable or outcome check,
decouple content from index, and gate when memory is read. Rejected designs more often make the store
incidental (per-query exemplar choice, synthetic demonstrations, compression, best-of-N simulation), build it
from the test stream, admit unverified model outputs, or rely on manual verification. Evidence fields cannot
be used for this comparison: rejected signatures are mostly abstract-derived, so their missing limitations
or evidence audits are a data-source artifact, not a property of the papers. Among corpus papers, variance
(1 of 24 audits) and a tested leakage guard (none) are rarely reported regardless of outcome.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 23 | 7 | 16 | 0.304 | -4.0 pp (base 0.344) | [0.156, 0.509] |
| iclr_2025_2026_high_fit | 13 | 4 | 9 | 0.308 | -8.5 pp (base 0.393) | [0.127, 0.576] |
| all_labeled | 40 | 24 | 16 | 0.6 | +2.4 pp (base 0.576) | [0.446, 0.737] |

Outcome is venue acceptance, not quality, and every CI comfortably contains its base rate: there is no
acceptance signal for this move in either direction. The sign flip is a sampling artifact, not a finding —
all 16 rejections appear in every view, so the extra labeled members in `all_labeled` are accepted-only and
push the rate up mechanically. The only two-sided view (ICLR) places the move at or slightly below base, and
restricting to high-fit members does not help. Sub-level rows (H03 −9.4 pp, H04 −4.4 pp in the ICLR view;
H05 has no labeled rejections) are each one of ~50 tests per view and none is distinguishable from base.
Read this as: indexing experience is a neutral bet on acceptance; execution, not the move, decides.

_Evidence counts below cover the 24 corpus members with a quote-grounded audit only._
- **Retained-store ablation.** Remove or freeze the store and show the gain disappears; 12 of 24 audits
  report it, so its absence is conspicuous.
- **Construction/evaluation separation.** Held-out separation is clear in only 5 of 24 audits (4 partial,
  1 no), and 14 H03 members state construction/evaluation overlap or task-order dependence as a limitation;
  expect a question on whether the store saw the test tasks.
- **Budget matching.** Only 1 of 24 is clearly budget-matched; expect a challenge that gains come from extra
  attempts, calls, or retrieval-time compute rather than reuse.
- **Scaling cost.** Recall and cost (tokens, calls, maintenance) as the store grows, against flat retrieval
  over the same raw material; 6 of 24 report optimizer/maintenance cost.
- **Comparison against other improvers.** Unclear in all 24 audits — none positions the store against
  abstraction-based or other self-improvement baselines; a reviewer may ask why raw beats distilled.
- **Write-gate and noise handling.** Whether cases are admitted by a model judge (9 H03 members say so), and
  what happens when retrieved precedents are noisy or dissimilar (stated as degrading by 5 H03 members).

## Cognitive barriers
- **"More history or wider context helps automatically."** Retrieval organization and timing are the
  bottleneck; unfiltered injection is a stated source of degradation.
- **"Abstraction is always the better form of memory."** Concrete, re-bound precedent can replace new-task
  search outright when tasks recur; abstraction discards the arguments that make reuse cheap.
- **"A better-shaped store yields better recall by itself."** Rejected structures resemble accepted ones;
  shape without update rules and an external write gate is not the load-bearing part.
- **"The agent can tell when it needs help."** Gated retrieval is only as good as its trigger signal, which
  can weakly discriminate failing steps and depends on base-model strength.

## Lessons
### From accepted work
- Remove instance-specific values and segment by functional intent so cases compose across tasks.
- Gate writes with executable verification; keep a derived unit only if it is non-redundant.
- Let content and index use different representations; confine search with hierarchy pointers.
- Make updates local, use separate update rates for fast facts and slow traits, defer heavy consolidation.
- Trigger retrieval at uncertain steps with a weak-match fallback; compare against always- and never-inject.
- Certify with a retained-store ablation and report what the store saves in cost.
### From rejected work
_Mechanism-level only; rejected limitation/evidence fields are abstract-derived and not used._
- Retrieval tuned on distance-to-task matches resemblance, not transferable reasoning.
- A knowledge bank updated from the test stream cannot certify reuse.
- Hand-verified examples contradict the "improves with use" framing.
- Exemplar selection, synthetic demonstrations, or context compression framed as experience reuse fit weakly.
- Stored model outputs without an external gate invite error propagation.
- A novel store shape is not by itself the contribution; the gate and the unit are.
