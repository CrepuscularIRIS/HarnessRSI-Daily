# Abstract Experience into Reusable Guidance
_id: `abstract_experience_into_guidance` · sub-patterns: H00, H01, H02 · corpus support: 97 papers (accepted 23 · rejected 16 · unlabeled 58)_

**Definition.** The agent turns its own task outcomes into compact natural-language guidance — lessons, principles,
curated notes, or skill packages — that lives outside the weights and conditions later episodes. The learned state
is an editable text store; the model stays frozen. The load-bearing choice is the abstraction level: specific
enough to act on, general enough to fire on a task that did not produce it.

**Operational signature.** act and observe an outcome → reflect or contrast to abstract guidance → write / curate
the guidance store → retrieve and inject into later tasks

**When to apply.** The model is frozen or costly to train, tasks recur enough that distilled lessons can transfer,
and there is a per-attempt outcome signal you trust more than the reflector itself.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H00](../sub/H00.md) | Reflect on Outcomes into Transferable Lessons | 57 | Contrast successes with failures and append a trigger-conditioned lesson to a retrieved store. |
| [H01](../sub/H01.md) | Curate a Living Memory with Edit Operations | 24 | An LLM curator applies add / update / merge / delete / delta edits so the store stays compact and consistent. |
| [H02](../sub/H02.md) | Mine Interaction Streams into Skill Packages | 16 | Compile recurring procedures from many sources into versioned, execution-gated packages other agents can reuse. |

The three differ in where the effort sits: H00 on *extracting* a lesson, H01 on *maintaining* the store once it
grows, H02 on *packaging* guidance so it leaves the agent that produced it.

## Success conditions (from accepted work)
- **Break a specific "fixed" assumption, not the generic one.** Accepted members name what was previously static —
  a human-designed strategy repertoire, predefined task categories, a fixed memory schema, a monolithic summary,
  manually authored skills — and make that thing learnable; the frozen-weights framing is background, not the claim.
- **Contrast, not narration.** Pairing successes with failures (or repaired failures with successes) isolates what
  actually differed and yields guidance that complements retrieved demonstrations.
- **A grounding signal in the loop.** Execution feedback, verification, correctness judgments, or a self-judge whose
  imperfection is acknowledged decide what becomes a lesson.
- **Explicit maintenance once the store grows.** Localized delta edits, consolidation, forgetting thresholds, and
  revised retrieval hooks keep the store bounded and avoid the detail loss of rewriting it as one summary.
- **A gate on what is kept.** Execution tests, quality filters, or judge-controlled versioned merges decide which
  entries or skills survive before they are published for reuse.

## Failure modes (from rejected work)
- **Restating the parent assumption as the contribution.** 9 of 16 rejected members frame the broken assumption as
  "improvement without weight / parameter updates", versus 3 of 23 accepted — the move's premise offered as its novelty.
- **The new domain is the novelty.** Most rejected H00 members re-apply attempt → reflect → store → retrieve to one
  more vertical (web, database querying, navigation, customer service, attack generation, clinical deliberation,
  simulated markets, productivity tasks) with a generic signature.
- **Casting the store as a stand-in optimizer.** Group-relative "semantic advantages", graded state-space search
  over edits, or library updates presented as replacing weight-based optimization set up a head-to-head with the
  optimizer they claim to replace.
- **A retrieval fix presented as learning.** Evolving entries' applicability conditions to correct retrieval
  misalignment is mechanism-wise a retrieval improvement and must be argued as one.
- **No outcome-grounded store at all.** Prompting for metacognition or self-assessment, or abstracting schemas from
  a demonstration or factoring a prompt into shared and residual parts, reuses structure rather than experience.

## Accepted vs rejected gap
Both sides run the same loop, so the loop does not separate them; the framing of what is learned does. Accepted
members typically identify a concrete component that prior work held fixed — who designs the strategies, how tasks
are categorized, how memory entries are edited or forgotten — and make the guidance store the place where it is
learned, with contrast or a gate deciding what enters. Rejected members more often present "a frozen agent can
improve from text" as the insight and supply a domain as the novelty, or relabel a retrieval or prompt-structuring
improvement as experience learning. The design-field split above (9 of 16 vs 3 of 23) is a post-hoc keyword count
on small n, not a tested effect, and rejected signatures were extracted from abstracts while most accepted ones
come from full text — read it as a framing risk to check, not a measured cause.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 20 | 4 | 16 | 0.200 | -14.4 pp (base 0.344) | [0.081, 0.416] |
| iclr_2025_2026_high_fit | 15 | 3 | 12 | 0.200 | -19.3 pp (base 0.393) | [0.070, 0.452] |
| all_labeled | 39 | 23 | 16 | 0.590 | +1.4 pp (base 0.576) | [0.434, 0.729] |

Outcome is venue acceptance, not quality, and every interval here contains its base rate — nothing is significant,
and with ~50 sub-pattern tests per view a lone outlier would be expected by chance anyway. All 16 rejected members
fall in the ICLR window, so the all-labeled rate mixes in accepted work from sources where rejections are not
observed; the ICLR rows are the like-for-like comparison, and there the move sits below base (more so on high-fit
members), driven by H00 (0.188, CI [0.066, 0.430]). H01's all-labeled 0.818 (CI [0.523, 0.949]) rests on 2
rejections. The honest reading: abstracting experience into text is now common enough that the recent window does
not reward it by itself — not that the move fails to work.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
The quote-grounded evidence audit covers corpus papers only (24 members of this pattern, nearly all accepted); the
counts below describe what those papers report, not a contrast with rejected work.
- **Separation of construction and evaluation streams.** A leakage guard is never reported as present (none 3,
  untested 2, unclear 19), and several of these papers themselves admit memories updating during test evaluation,
  test inputs guiding online learning, or evaluation on requests seen while building the store.
- **Budget-matched baselines** — same frozen model, same calls, retries, and exploration rollouts. Budget matching is
  yes in none of the 24 (partial 2, no 3, unclear 19).
- **A store-off ablation with the loop kept**, the most common control: yes in 16 of 24.
- **Variance across runs or stream orderings**, reported by only 3 of 24; order matters for an accumulating store.
- **Reflector / curator cost**, reported by 5 of 24; repeated model calls are a self-stated limit.
- **A comparison against an alternative abstraction or editing scheme** — unclear in all 24; the open slot for
  showing that this abstraction level, not any stored text, earns the gain.

## Cognitive barriers
- *Learning requires parameter updates.* Editable text in context can itself be the learned state.
- *"No weight updates" is the insight.* It is the premise; the contribution is what the store makes learnable.
- *More stored experience is better.* Without consolidation and forgetting the store bloats, contradicts itself, or
  collapses when rewritten; maintenance is part of the method.
- *A plausible lesson is a correct lesson.* The reflector is only as good as the outcome signal behind it.

## Lessons
### From accepted work
- Name the component prior work kept fixed and make the store the place it is learned.
- Contrast failed with successful trajectories; the insights complement retrieved demonstrations.
- Label-free lessons are viable if self-judged outcomes are contrasted and the proxy's imperfection is acknowledged.
- Treat forgetting and localized delta edits as features; they keep a growing store usable.
- Gate retention by execution or tests and track coverage, so mining targets gaps instead of frequent procedures.
### From rejected work
- "A frozen agent improves from text" restates the pattern; it cannot carry a paper on its own.
- One more domain for the same loop needs a mechanism that is specific to why that domain is hard.
- Framing the store as an optimizer replacement invites the optimizer as the baseline.
- Fixing what gets retrieved is a retrieval contribution; argue it as one.
- Metacognitive prompting or demonstration-derived schemas without an outcome-grounded store are not this move.
