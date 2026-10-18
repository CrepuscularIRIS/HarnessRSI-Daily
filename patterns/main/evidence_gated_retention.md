# Gate Retention on Measured Evidence
_id: `evidence_gated_retention` · sub-patterns: H29, H30, H31 · corpus support: 43 papers (accepted 6 · rejected 4 · unlabeled 33)_

**Definition.** What persists in a self-improving system (a memory entry, a library skill, a new incumbent
version of the agent or harness) is decided by measured counterfactual utility or a statistically sound comparison,
not by plausibility, apparent success, or a raw score delta. The move separates *proposing* a change from
*authorizing* it, and gives the authorizing step its own data, statistic and rollback.

**Operational signature.** propose a candidate entry or change → measure its marginal effect (paired, held-out,
utility credit) → admit, demote, or roll back → keep provenance

**When to apply.** When evaluation is noisy, regressions are costly, or accumulated state degrades as it grows;
the tell is a store or agent whose development score rises while solved cases, retrieval quality or constraints erode.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H29](../sub/H29.md) | Value Memory Entries by Measured Utility | 16 | Credit each entry from outcomes against a no-memory or unguided counterfactual, and rank or demote by that value. |
| [H30](../sub/H30.md) | Govern Library Admission and Retirement | 12 | Quarantine new entries until attribution, replay and a regression budget pass; retire on accumulated harm under a size bound. |
| [H31](../sub/H31.md) | Use a Statistically Sound Commit Rule | 15 | Replace the incumbent only when a disjoint, paired, sequential or sealed test says so, with an empty-state fallback. |

The three differ by granularity: H29 re-weights many entries without removing any, H30 decides membership of a
shared pool, H31 makes one commit-or-reject decision about a single artifact. All three share one claim: the
verdict must come from a signal the proposer did not generate and data it did not reuse.

## Success conditions (from accepted work)
- **An explicit counterfactual behind every credit.** Accepted members contrast memory-on with memory-off runs,
  or use the generator's own reliance on an entry; utility without a baseline is only correlation with success.
- **Admission paired with retirement.** The accepted library member combines a prior on how entries are authored
  with conservative retirement and a hard size bound; either gate alone lets the collection degrade silently.
- **A named silent failure that governance demonstrably fixes.** Showing that ungoverned accumulation degrades
  retrieval and injects harmful guidance makes the gate a remedy rather than overhead.
- **The gate's effect is ablatable by design.** Accepted mechanisms keep the value signal or the gate as a
  separable component (a reranker, a reweighting rule, a stopping rule), so stripping it is a clean ablation.
- **Cost of the gate stated openly.** Accepted members list the extra contrastive run, online-learning expense,
  or a large call overhead against a no-skill baseline instead of hiding it.
- **Theory that separates error types.** The accepted formal members distinguish compounding optimization errors
  from non-compounding knowledge errors, and drift from apparent quality gains, and stop on constraints first.

## Failure modes (from rejected work)
- **Infrastructure offered as the gate.** A rejected member versions and registers every refined component under
  one protocol and lets execution feedback refine them, but its mechanism contains no measured admission or
  retirement test; versioning enables rollback without deciding what is kept.
- **Utility routed into training of something else.** Rejected memory members push entry value into policy
  gradients, embedding updates or prior refinement, so the memory's own effect is never isolated.
- **A self-reinforcing loop with no fixed referee.** One rejected design lets memory values refine the model
  prior, whose better trajectories then enrich the memory; the loop has no step that can reject an entry.
- **Credit that needs paired rollouts to exist.** The guided-versus-unguided reward difference is a sound
  counterfactual, but it doubles execution and, by that design's own stated limit, retrieving many strategies adds noise.
- **Gating the retriever rather than the content.** Online embedding updates from task success change what is
  found without ever deciding what is kept, so nothing harmful is demoted or removed.

## Accepted vs rejected gap
Accepted and rejected executions both *measure* something; the gap is whether the measurement *authorizes* the
retention decision and is isolated from the rest of the system. Accepted members keep the gate local (a contrast
that reweights entries, an attributed replay that admits or retires a skill, a drift index that halts refinement)
and pay for it visibly. Rejected members either have no gate at all (lifecycle and versioning without an
admission test) or let the measured value leak into a second learning process, so a reviewer cannot tell
whether retention, training, or the backbone produced the gain. Evidence profile, corpus papers only (8 members carry a quote-grounded evidence block; rejected members mostly lack one because they were extracted from abstracts, so this is not an outcome comparison): retained-artifact ablation is yes in 5 of 8, while held-out separation, variance, optimizer cost and improver comparison are yes in only 1 of 8, leakage guard is never tested, and budget matching is at best partial. Even the accepted gates are rarely backed by gate statistics.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | — | — | — | insufficient labeled papers (n < 10; base 0.344) | — | — |
| iclr_2025_2026_high_fit | — | — | — | insufficient labeled papers (n < 10; base 0.393) | — | — |
| all_labeled | 10 | 6 | 4 | 0.600 | +2.4 pp (base 0.576) | [0.313, 0.832] |

The only reportable view is the secondary one, where curator-selected venues inflate the base rate. There the
pattern sits essentially at base: +2.4 pp with an interval spanning roughly a third to four-fifths. No ICLR view
reaches the reporting threshold, and no sub-pattern has a rate of its own. Read this as "no detectable outcome
signal", not as a positive or negative effect; acceptance is not quality, and with ~50 tests per view even a
nominally significant row could be chance. None of this pattern's combinations appears among anti-pattern candidates.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
- **Disjoint proposal and commit data.** Reusing development cases to both propose and gate is the most common
  leak across members; expect to be asked which split authorized each retained change.
- **The ungoverned baseline.** Compare against append-only or similarity-only memory and a no-memory agent, not
  only the full system against a weak prior method.
- **Per-candidate versus run-level guarantees, and power.** A gate that rejects small true gains or holds only per
  candidate must say so; non-regression is not improvement.
- **Seeds and repeated evolution runs.** Variance is yes in 1 of 8 corpus-paper evidence blocks, and members'
  own limits cite single runs and one split seed; expect this to be flagged.
- **Matched budgets including the gate's cost.** Paired rollouts, replays and audits are extra calls; report them
  against baselines given equal optimization budget.
- **Grader independence.** Self-graded rewards inflate wrong entries and self-written tests cannot authorize
  deployment; show the verdict comes from a source the proposer cannot edit.

## Cognitive barriers
- That more retained experience, or a higher development score, means improvement.
- That a successful trajectory authorizes storing what it used; success must be attributed to sub-steps first.
- That versioning and provenance are governance; they enable rollback but do not decide what is kept.
- That the outcome signal is a clean measure of an entry's contribution when several entries are co-retrieved.

## Lessons
### From accepted work
- Use the generator's own citations of entries as free online feedback for a light reranker.
- Let a memory-on versus memory-off contrast both reweight entries and revise how guidance is compiled.
- Gate on significance so noise does not churn the store, accepting that subtle heuristics arrive later.
- Bound the library and retire conservatively; admit that governance settings depend on library scale.
- Treat quality gains under iterative refinement as suspect until drift and regression of earlier gains are measured.
- State worst-case assumptions of any safety argument (bounded errors, unlimited modification, no corrigibility).
### From rejected work
- A lifecycle protocol without a measured admission or retirement step leaves the retention claim unsupported.
- Keep the memory's effect separable from any policy, prior or embedding training that consumes its value.
- Paired guided and unguided rollouts give real credit but double cost; plan for it, and cap retrieval width.
- Adapting what is retrieved is not the same as governing what is retained.
- A loop where memory improves the prior and the prior enriches memory needs an outside referee to reject entries.
- No rejected member used a statistical commit rule; that absence is a gap in the corpus, not evidence the rule wins.
