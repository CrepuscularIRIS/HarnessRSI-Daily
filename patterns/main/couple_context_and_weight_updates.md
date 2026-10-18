> **Boundary pattern** — involves weight updates (touches L1); listed because the harness-level part is load-bearing.

# Couple Context-Level and Weight-Level Learning
_id: `couple_context_and_weight_updates` · sub-patterns: H28 · corpus support: 26 papers (accepted 7 · rejected 6 · unlabeled 13)_

**Definition.** Run fast, editable context adaptation (memory, skill library, harness, system prompt) and slow
parameter updates as one learning system instead of two separately tuned ones. Validated experience either crosses
from context into weights (or learnable tokens/adapters), or both levers train on the same rollouts, or a controller
decides which lever to pull when the other plateaus.

**Operational signature.** adapt in context → collect experience-shaped rollouts → train weights on them →
re-adapt context for the updated model

**When to apply.** A context-level loop already works but has hit a ceiling (memory bloats past the context limit,
the executor stops following evolved skills, gains flatten across rounds) while weight-only RL is sample-inefficient
on the same tasks — and a verifiable reward plus policy-update compute are available.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H28](../sub/H28.md) | Couple In-Context Adaptation with Weight Training | 26 | Internalize validated context, co-train both levers on shared rollouts, or arbitrate between scaffold edits and weight updates on different timescales. |

H28 is the parent's only sub-pattern, so this card's job is to lift its three variants — *internalize*,
*co-train on shared rollouts*, *arbitrate* — into a decision rule, not to compare siblings.

## Success conditions (from accepted work)
- **One rollout stream serves both levers.** When the same on-policy rollouts rank context candidates and drive the
  weight update, the coupling interface is the data itself and cannot be dismissed as two optimizers in sequence.
- **Each lever has a distinct, typed job.** Declarative knowledge refined in context, procedural competence trained
  into weights; the split makes a lever-wise ablation meaningful.
- **The policy is trained to condition on the context artifact.** A skill or memory library that is an explicit
  input of the trained policy, and is revised from diagnosed failures as well as successes, keeps both sides aligned.
- **Internalization shrinks the context.** Compressing trajectory-heavy experience into a few learnable tokens or
  adapters on a frozen backbone, with recent insights kept as text, answers the "memory grows without bound" plateau.
- **Memory pays for itself.** Retrieved test-time memories that are curated into training data turn an inference
  cost into a training asset.

## Failure modes (from rejected work)
Drawn only from rejected members' mechanism and design fields (most were extracted from abstracts, so their
stated limitations and evidence are not comparable to accepted corpus papers and are not used here).
- **Weight-side machinery carries the paper.** 4 of 6 rejected mechanisms center on a new weight-update procedure
  (bi-level meta-RL, capacity expansion with synthetic rehearsal, selective single-step RL, per-module policy
  gradients); the context lever is secondary, so "coupling" reads as composition.
- **Context as a recall store, not a trained-on input.** Where the context side is a bank that retains and recalls
  prior solutions or knowledge, the policy is not shown to be trained to read it, so neither lever depends on the other.
- **Sequenced, not coupled.** Composing an existing policy-gradient recipe with a prompt optimizer, or integrating
  retrieved principles "with RL", leaves no shared interface (shared rollouts, versioned data, conditioning).
- **Confidence-selected consolidation.** A design that consolidates high-confidence traces into a learned component
  risks baking confident-but-wrong behavior into weights unless curation is anchored in verifiable outcomes.
- **Test-time evolution with no declared split.** A loop that accumulates experience on its incoming query stream
  makes the adaptation stream and the reported stream coincide unless a split is fixed in advance.

## Accepted vs rejected gap
This comparison uses only mechanism and design fields (problem, signature, load-bearing mechanism, broken
assumption); evidence and limitations fields come from different data sources per outcome and are not compared.
What separates the outcomes is where the contribution sits. All 7 accepted mechanisms make the *interface* the
novelty — matched rollouts shared by both levers, a declarative-context / procedural-weights split, a policy trained
on a co-evolving skill library, retrieved memories curated into training data, small learnable tokens or adapters
on a frozen backbone, or a shared encoder generating prompt and parameters jointly. Rejected mechanisms mostly put
the novelty in a heavy weight-side procedure (4 of 6) with a retention store or a composed prompt optimizer beside
it, and one consolidates by confidence during test-time adaptation. Fit does not explain the gap: 6 of 7 accepted
and 4 of 6 rejected labeled members are high-fit.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 11 | 4 | 7 | 0.364 | +2.0 pp (base 0.344) | [0.152, 0.646] |
| iclr_2025_2026_high_fit | — | — | — | no row in contrast.json | (base 0.393) | — |
| all_labeled | 13 | 7 | 6 | 0.538 | −3.8 pp (base 0.576) | [0.291, 0.768] |

Acceptance is a venue outcome, not a quality score. The ICLR rate of 0.364 (95% CI [0.152, 0.646]) and the
all-labeled rate of 0.538 (95% CI [0.291, 0.768]) both sit within a couple of points of their base rates, and each
interval is roughly 0.5 wide, so the move carries neither a premium nor a penalty that this n can detect; the sign
of Δ even flips between views. With ~50 sub-pattern tests per view, any single "significant" contrast would be
suspect anyway, and none is claimed here. Half of the corpus support (13 of 26) is unlabeled, and every member that co-evolves
a harness (not just memory or prompts) with the policy is among them, so the labeled contrast describes the
memory/prompt-plus-RL end of the pattern, not its harness-level end.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
Evidence counts below describe corpus papers only: the 7 members with a quote-grounded evidence block (5 accepted,
2 rejected). They say what is commonly missing, not what distinguishes outcomes.
- **Three-arm lever ablation.** Context-only, weights-only and coupled, on the same tasks; improver comparison is
  yes in only 1 of those 7 corpus members.
- **Clean split.** Held-out tasks never used for adaptation or training; held-out separation is yes in 2 of 7, and
  6 corpus members' own limitations flag train/eval overlap or test-derived feedback.
- **Variance and matched budget.** Seeds with spread, and the coupled system compared at equal rollout budget —
  unclear in all 7.
- **Cost of the slow loop.** RL compute, teacher calls and experience-base maintenance reported; also unclear in all 7.
- **Externally grounded reward.** Verifiable outcomes or an independent checker for both curation and the update.
- **An exercised cycle.** At least two full context→weights→context rounds; some unlabeled corpus members show one
  round with no model update, or separate harness and model case studies.

## Cognitive barriers
- That in-context adaptation and weight training are alternative, separately optimized pathways, so a paper must pick one.
- That experience which helped in context is automatically clean training signal for the weights.
- That the harness and the policy can each be optimized to convergence alone; an evolved interface the executor cannot
  follow is a failure of the pair, not of either half.
- That "self-improving" requires a single timescale; fast context injection and slow idle-time training can coexist.

## Lessons
### From accepted work
- Reuse matched on-policy rollouts for both levers; shared data is the strongest coupling evidence.
- Give context and weights separate roles so each ablation isolates one lever.
- Train the policy to condition on the skill/memory library and revise that library from failures too.
- Internalize bulky experience into small learnable tokens or adapters; keep only recent insights as text.
- Curate retrieved memories into training data so the memory is amortized after internalization.
### From rejected work
- Keep weight-side machinery light enough that the coupling interface remains the visible contribution.
- Make the context artifact an input the policy is trained on, not a recall bank beside it.
- Show a shared interface, not a sequence of two known optimizers.
- Curate by verifiable outcome, not by the model's own confidence, before anything reaches the weights.
- For test-time evolution, fix the adaptation/reporting split before the loop runs.
