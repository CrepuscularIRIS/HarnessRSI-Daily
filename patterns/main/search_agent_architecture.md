# Search the Agent's Architecture
_id: `search_agent_architecture` · sub-patterns: H17, H18 · corpus support: 35 papers (accepted 11 · rejected 8 · unlabeled 16)_

**Definition.** Treat the agent's structure (which roles and modules exist, how they communicate, what
workflow code runs between them) as an optimization variable rather than fixed scaffolding, and improve it
from execution feedback. The search happens either offline over a declared design space, shipping one frozen
design per task distribution, or online, rewiring a specific team while it works.

**Operational signature.** declare a design space of modules / topologies / workflow code → propose designs
→ execute and score them → retain, cache or adapt the structure that wins

**When to apply.** When hand-designed orchestration, not the wording of individual prompts, is what caps
performance, and a scorable executor makes each candidate design measurable.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H17](../sub/H17.md) | Search an Offline Agent Design Space | 21 | Encode designs as code, typed graphs or module slots, search them offline against execution scores, deploy one frozen design. |
| [H18](../sub/H18.md) | Co-Evolve Roles and Topology at Test Time | 14 | Rewrite roles, edges and routing during inference at two rates, caching verified specialists across instances. |

The two differ on *when* structure stops changing: H17 pays search cost before deployment and none after;
H18 pays it per instance or per stream and needs no labeled search set. Everything below holds for both
unless marked.

## Success conditions (from accepted work)
- **One search-shaping primitive that makes each execution count.** Accepted members win through an archive
  of scored stepping stones, standardized interfaces plus a cheap surrogate filter, an experience tree tying
  edits to measured effects, or a staged local-then-global order, not through the choice of search algorithm.
- **Tune components before searching wiring.** Topology search over untuned prompts measures the wrong thing;
  the accepted ordering is local prompt tuning, then a pruned topology search, then joint retuning.
- **Gate structural change on a task-outcome signal.** Pass/fail or an independent verifier decides what
  persists (H18 especially); the proposer's self-assessment does not.
- **Keep a retreat path.** A verifier allowed to prefer a simple system's answer, or escalation to deeper
  structure only when retained structure stalls, keeps added complexity honest.
- **Change the objective when search is too expensive.** Ranking compositions by tail risk or predicting a
  workflow's utility from its code, prompt and graph views replaces exhaustive execution.
- **Certify the frozen or adapted design away from where it was found.** Held-out problems at minimum;
  a second task family or executor model strengthens the claim.

## Failure modes (from rejected work)
- **Co-evolving every axis at once.** Roles, collaboration structure, mutation operators, curriculum and
  control rules evolved together with no axis-level ablation reads as a system, not a finding.
- **Incremental refinement of an existing search.** A tighter design representation or finer block-level
  blame must show that statically valid designs actually execute and that blame beats the end-to-end score.
- **Proxy-steered edits.** Steering roles by linguistic or embedding proxies of role clarity and
  complementarity, or edits by LLM-ranked failure traces, ties the search to a signal not shown to track
  task success (the single rejected H18 member is of this kind).
- **Infrastructure presented as optimization.** Modular pipeline tooling with caching and cost tracking is
  engineering unless it enables a search result nothing else could.
- **Re-parameterizing the space as the contribution.** Recasting the workflow as a trained connection
  matrix, or bundling dynamic reasoning construction with prompt and hyperparameter tuning, changes how
  designs are written down without isolating a new reason the search succeeds.

## Accepted vs rejected gap
The move itself does not separate outcomes; the shape of the contribution does. Accepted executions isolate
one primitive that makes architecture search tractable or better-founded (an archive, an interface standard
with a surrogate, a staged order, a reversion gate, a new objective) and show what it buys. Rejected
executions either widen the space (joint optimization of everything, "holistic" function-plus-structure
search) without showing which axis pays, refine an existing search's representation or credit signal
without proving the refinement matters at execution time, or steer edits with signals not tied to task
success. This contrast is drawn from mechanism and design fields only; rejected members were extracted
mostly from abstracts, so their reporting quality cannot be compared with accepted work.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 16 | 7 | 9 | 0.438 | +9.4 pp (base 0.344) | [0.231, 0.668] |
| iclr_2025_2026_high_fit | 11 | 5 | 6 | 0.455 | +6.2 pp (base 0.393) | [0.213, 0.72] |
| all_labeled | 19 | 11 | 8 | 0.579 | +0.3 pp (base 0.576) | [0.363, 0.769] |

Outcome means venue acceptance, not quality. The ICLR views show a modest positive Δ, but every interval
contains its base rate and the all-labeled Δ is essentially zero, so membership carries no reliable
acceptance signal. With roughly 50 sub-pattern tests per view, even an interval that excluded the base would
need replication before being trusted; none does here. The labeled rows come almost entirely from H17
(H18 has only 4 labeled members and no contrast row), so this table describes offline search, not
test-time co-evolution.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
Counted over the 10 corpus papers with a quote-grounded evidence block; this describes corpus practice,
not an accepted-vs-rejected comparison. Recurring limitations in unlabeled members (fitness and scoring on
one small subset, strong-initial-archive dependence, strategy collapse, unmatched adaptation compute) point
the same way.
- **Search/evaluation separation with a leakage guard.** Held-out separation is reported by 7/10, but a
  leakage guard by 0/10; expect questions about archives or knowledge bases built on evaluation data.
- **Seed variance.** Reported by 0/10. Search over designs is stochastic; a single run is the obvious attack.
- **Ablation of the retained artifact.** 0/10 ablate the archive, cached specialists or the frozen design's
  key component; the rejected co-evolve-everything designs make this the first question a reviewer asks.
- **Total cost at matched budget.** Optimizer cost is reported by 5/10, budget matching fully by 1/10
  (partial 3); expect search, adaptation and inference cost against hand-built and prompt-only baselines.
- **Transfer beyond the search setting.** Cross-task transfer yes 2/10; limitations repeatedly cite executor
  dependence and degraded cross-benchmark routing. Expect a second task family and a second backbone.
- **Comparison against other improvers.** Improver comparison is no 1, unclear 9: show the architecture
  search beats spending the same budget on prompt-level optimization.

## Cognitive barriers
- That orchestration is fixed scaffolding around tunable prompts, rather than the variable that caps results.
- That a larger or more jointly optimized design space is a contribution in itself.
- That the editing model's own judgments (judge scores, self-diagnosis, role-quality proxies) reliably point
  toward improvement; convergence arguments in H18 explicitly assume they do.
- That one must choose between a frozen design and rebuilding per query; retaining verified structure and
  escalating only on failure is a third option.

## Lessons
### From accepted work
- Keep an expanding archive of scored designs so a meta-agent recombines stepping stones instead of
  restarting from a template.
- Standardize module interfaces so parts of separate systems recombine, and filter candidates with a cheap
  predictor before paying for execution.
- Tune local prompts first, prune the topology space, then retune globally.
- Let a verifier choose between the evolved team and a simple one; the right to revert is a feature.
- Retain discovered specialists as state and escalate to structural change only when they fall short.
- Gate every persisted edit on task outcome, not on the proposer's opinion of its own edit.
### From rejected work
- Co-evolving all axes without isolating the one that pays will be read as an engineering bundle.
- Refining an existing workflow search's representation or blame signal must prove execution validity and
  a gain over plain end-to-end scoring.
- Proxy metrics of role clarity or complementarity are not evidence of competence.
- Modular tooling is infrastructure unless it unlocks a search outcome.
- Jointly optimizing function and structure needs the per-dimension ablation that justifies going joint.
- With 8 rejected members (1 in H18), treat these as cautions, not laws.
