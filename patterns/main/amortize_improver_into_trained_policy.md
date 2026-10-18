> **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing.

# Amortize the Improver into a Trained Policy
_id: `amortize_improver_into_trained_policy` · sub-patterns: H26, H27 · corpus support: 45 papers (accepted 13 · rejected 12 · unlabeled 20)_

**Definition.** The component that improves the harness — the memory writer, skill curator, prompt editor, reflector,
or workflow designer — stops being a prompted frozen model and becomes a policy trained by RL or preference learning
on the downstream improvement it causes. Repeated per-task search or zero-shot curation is replaced by one learned,
query-conditioned improver whose weights encode what kinds of edits pay off.

**Operational signature.** improver acts (write memory, edit artifact, design workflow) → measure downstream task
outcome → credit the improver's action → update improver weights

**When to apply.** When the same improvement operation recurs often (per query, per task, per stream), its downstream
effect is cheaply measurable, and a prompted improver is either expensive to search with or writes plausible but
low-utility artifacts.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H26](../sub/H26.md) | Train the Curator on Downstream Utility | 17 | Credit memory/skill write, merge, prune actions by the success of *later* tasks that read the store. |
| [H27](../sub/H27.md) | Train the Proposer to Amortize Search | 28 | Reward an editor or design generator by the score delta its proposal causes, replacing per-query search with one pass. |

The split is about where the value lands: H26 trains the owner of persistent state (delayed, cross-task credit);
H27 trains the proposer of a one-shot change (immediate but noisy single-step credit).

## Success conditions (from accepted work)
- **Reward the improvement, not the score.** Accepted proposers reward the change relative to the pre-edit state,
  the previous episode, or a dominance relation, which separates edit quality from query difficulty.
- **Credit through downstream use.** Accepted curators are rewarded by what a consumer does with the written
  artifact (answer correctness after retrieval, reader traversal), not by the episode that produced it.
- **Co-train or couple writer and reader.** Keeping the improver aligned with the policy that consumes its output
  stops stored skills and designs from going stale as the rollout distribution shifts.
- **Train a new kind of object.** Accepted H27 members produce a query-conditioned distribution over designs, a
  single-pass system program, or a self-rectifying generator team — not a familiar generator with a new loss.
- **Meta-train across task families.** Accepted members that compress examples into instructions or generate
  systems train across many diverse datasets, so the improver learns reusable composition rather than one task.

## Failure modes (from rejected work)
- **Optimizer swap on a known loop.** 3 of the 4 high-fit rejected workflow/system generators keep the
  "generate, execute, score, train the generator" recipe and change only the training procedure.
- **Pattern at the edge.** 7 of 11 rejected H27 members are low-fit (the trained policy is a generic controller,
  data acquirer, or code optimizer) versus 2 of 10 accepted; the amortization story then does not carry the paper.
- **One bolted-on property.** Rejected generators add paraphrase invariance or safety feedback to an existing
  generator loop, so the property, not the trained improver, is the stated contribution.
- **Composite proxy reward on an isolated writer.** The one rejected H26 member trains the writer alone on task
  accuracy mixed with validity, format, and compression terms, rather than coupling it to the reader.

## Accepted vs rejected gap
Judged only on mechanism and design fields (problem, signature, load-bearing mechanism, assumption broken), the gap
is less about the training method than about what is trained and how its credit is defined. Accepted executions
train an improver that is unmistakably a harness component — a curator of a store that a reader consumes later, or a
proposer of edits and designs — with a reference-pointed or downstream-use reward, and the trained object itself is
new. Rejected executions either sit at the pattern's edge, a controller or optimizer relabelled as an improver, or
keep an established generator formulation and vary only the optimizer or reward terms, which reads as incremental.
Most rejected signatures were extracted from abstracts only, so differences in reported limitations or evidence
between the groups are a data-source artifact and are not used here.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 20 | 8 | 12 | 0.400 | +5.6 pp (base 0.344) | [0.219, 0.613] |
| iclr_2025_2026_high_fit | 11 | 6 | 5 | 0.545 | +15.3 pp (base 0.393) | [0.280, 0.787] |
| all_labeled | 25 | 13 | 12 | 0.520 | −5.6 pp (base 0.576) | [0.335, 0.700] |

Interpretation: no view gives a reliable acceptance signal. The two broad views disagree in sign and every CI spans
its base rate. The high-fit view has the largest positive delta and lines up with the low-fit concentration among
rejected H27 members, but n is 11 and roughly 50 tests run per view, so a +15.3 pp point estimate is well within
chance. H26 has only 4 labeled members (accepted 3 · rejected 1), so the parent's numbers are almost entirely H27's
(iclr_2025_2026 n 19, 0.421, CI [0.231, 0.637]). Acceptance is not quality; read these as "the move is neither
penalized nor rewarded per se".

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
The counts below cover only the 8 corpus members with quote-grounded evidence blocks; they describe what corpus
papers report, not a difference between accepted and rejected work.
- **Trained vs prompted improver at matched budget.** Improver comparison is yes in 2 of 8 and budget matching yes
  in 1 (partial 1); expect "does training beat prompting the same model with the same budget?" first.
- **Seed variance.** Variance is unclear in 8 of 8; RL-trained improvers with single-step or delayed credit are
  noisy, so a reviewer will ask for multiple training seeds.
- **Leakage guard.** Leakage guard is unclear in 8 of 8, and 5 of 17 H26 members' own limitations concern store
  construction, verification, or accumulation on test tasks; reviewers will check the train/eval boundary and the
  use of privileged task-family labels at retrieval.
- **Held-out separation.** Held-out is yes in 2 of 8 (partial 1) while cross-task is yes in 7 of 8, so transfer is
  usually reported but the evolution/evaluation boundary often is not.
- **Cost of training vs search saved.** Optimizer cost is reported in 3 of 8; an amortization claim needs both the
  training bill and the per-query search it replaces.
- **Artifact ablation.** Retained-artifact ablation is yes in 3 of 8; expect a store-removed or frozen-proposer
  variant showing the gain lives in what the improver writes.

## Cognitive barriers
- That curation and editing are fixed heuristics or zero-shot abilities rather than trainable skills.
- That the right reward for an improver is the score of the task it just touched, rather than the improvement it
  causes or the later tasks that consume its output.
- That one global best artifact (prompt, workflow, skill set) exists, rather than a query-conditioned distribution.
- That training the improver is the contribution by itself; the object it produces and how credit reaches it are.

## Lessons
### From accepted work
- Use a delta or downstream-use reward with an explicit reference point.
- Condition the improver on the query and price cost (calls, tokens, early exit) inside its objective.
- Couple the writer to the reader, or co-train them, so curated state tracks the consuming policy.
- Make the trained object new: a design distribution, a one-pass system program, a self-rectifying generator team.
- Meta-train across diverse task families so the improver compresses experience into reusable artifacts.
### From rejected work
- An optimizer variant on an existing generator recipe reads as incremental; change the trained object instead.
- If the learned policy is a generic controller, the amortization framing will not hold.
- A single added property on a known loop needs to be the cause of the gain, not a side effect of extra training.
- Isolate each term's contribution when the reward is composite, and tie the writer's reward to the reader.
- Rejected signatures come mostly from abstracts, so these lessons rest on mechanism text only.
