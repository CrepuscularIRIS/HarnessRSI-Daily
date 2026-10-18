# Attribute Failures and Patch the Incumbent
_id: `attribute_and_patch_incumbent` · sub-patterns: H09, H10, H11, H12 · corpus support: 117 papers (accepted 24 · rejected 32 · unlabeled 61)_

**Definition.** Keep one deployed artifact (a prompt, rule document, skill file or harness code) as the
incumbent and improve it by tracing failures to the component responsible, then applying localized edits
that must re-validate before they replace it. The load-bearing step is credit assignment from rich traces
(critiques, verifier diagnostics, failing tests, source plus logs) rather than from a scalar score.

**Operational signature.** execute and collect traces → diagnose and attribute failures to a component →
propose a localized edit → re-validate on a disjoint split → replace the incumbent (or roll back)

**When to apply.** When execution traces are rich and the artifact decomposes so that a failure can be
pinned to a node, section or module; if only a scalar score exists, population search is the honest choice.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H09](../sub/H09.md) | Propagate Feedback Through a Compound System | 12 | Route a neighbor-conditioned critique to each upstream node of an executed graph; bound the propagation scope. |
| [H10](../sub/H10.md) | Rewrite a Document from Diagnosed Errors | 55 | Rewrite one textual artifact from verbalized errors and successes; the selection and retention rule decides. |
| [H11](../sub/H11.md) | Revise Skills by Failure Attribution | 14 | Attribute failures to a skill section, separate defects from execution lapses, edit under a budget. |
| [H12](../sub/H12.md) | Patch the Harness from Trace Diagnosis | 36 | A coding agent reads traces plus source, patches a recurring mechanism with a falsifiable prediction. |

The four differ in what is attributed (graph node, document, skill section, code module) and how
(propagated critique, self-critique, defect-vs-lapse gate, source-level diagnosis). H10 is by far the
largest and the only one with enough labels for a rate.

## Success conditions (from accepted work)
- **Attribution scope matches the artifact's structure.** The minimal execution subgraph, section or module
  that produced the failure is edited, not the whole artifact; deep global chains grow and lose specificity.
- **Evaluation budget is steered, not spread.** Accepted mechanisms decide where scoring goes (bandit selection
  over a beam, tree search over future rewrites, local refinement before bounded nudges to neighbors).
- **The retention rule protects earlier wins.** Successes are fed alongside failures, edits are accepted only if
  they individually improve, illegal or regressing updates are rolled back.
- **Mechanisms are diagnosed, not instances.** Traces are clustered across tasks before an edit is proposed, so
  one repair serves a failure family instead of one trajectory.
- **The proposer sees raw evidence.** Full traces, source and the candidate history beat fixed summaries for
  localizing faults that text-only rewriting cannot reach (routing, state, tool dispatch).
- **The object is a general improver.** The patched artifact is the means; the method is stated for any
  artifact of its type, not for one task's deliverable.

## Failure modes (from rejected work)
- **The loop is the vehicle for a domain result.** Many rejected problem statements are domain tasks (table
  reasoning, a retrieval knowledge store, image-generation sampling, alarm analysis, game players, parallel
  mappers, attack generation) with the critique → rewrite loop applied unchanged.
- **One more signal in the update rule.** Rejected mechanisms often add an input to the textual gradient
  (neighbor conditioning, response-history similarity, contrast of best and worst prompts, sample-state cues)
  while topology, selection and certification stay as before.
- **A single executable program is evolved.** Mapper, RL-agent and game-player generators improve one
  deliverable against its own benchmark; that reads as program synthesis, not harness improvement.
- **Self-constructed validation replaces ground truth.** Several rejected loops build their own validation
  (probe-derived tool cases, synthetic examples, pseudo-labels, label-free inference-time feedback), so the
  signal that certifies the edit comes from the same model family that proposes it.
- **Feedback is assumed to isolate the edited artifact.** Editing a knowledge store from expert feedback, or a
  prompt from a critique, presumes the failure was caused there; nothing in the mechanism checks it.
- **Guards are mistaken for a contribution.** Section-level edits and preservation tests appear in rejected
  mechanisms too; they are necessary hygiene, not a differentiator.

## Accepted vs rejected gap
Compared on mechanism and problem fields only, the core loop barely separates the sides: critique-driven
rewriting, tree search over candidates, section-level edits and preservation gates appear on both. What
differs is where the novelty is placed. Accepted mechanisms change *what gets attributed and where budget
goes*: the minimal subgraph, local equilibrium instead of long backward chains, bandit or planning-based
candidate selection, defect-vs-lapse gating, raw-history access for a code-reading proposer. Rejected
mechanisms more often keep that skeleton and either add a further cue to the per-step critique or point the
loop at a single domain task or program, which makes the contribution read as an application or a tweak.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 41 | 9 | 32 | 0.22 | −12.4 pp | [0.12, 0.367] |
| iclr_2025_2026_high_fit | 29 | 7 | 22 | 0.241 | −15.1 pp | [0.122, 0.421] |
| all_labeled | 56 | 24 | 32 | 0.429 | −14.8 pp | [0.308, 0.559] |

Base rates: 0.344, 0.393 and 0.576. The pattern sits below base in every view, but in both ICLR views the
95% CI still contains the base rate, so the deficit is not established there. Only all_labeled excludes its
base, and that view is venue-mixed: all 32 rejected members are already in the ICLR view, while the 15 extra
labeled members are all accepted. The deficit is concentrated in H10, which supplies 30 of the 41 ICLR-labeled
members (0.167, CI [0.073, 0.336], upper bound just under 0.344); with ~50 sub-pattern tests per view this one
"significant" sub result can be chance. The other three sub-patterns together hold 10 accepted and 7 rejected
labeled members, too few for a rate. Outcome is venue acceptance, not quality.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
Counts below cover only the 21 corpus papers that carry a quote-grounded audit block; they describe what
those papers report and are not an accepted-vs-rejected comparison.
- **An improver comparison.** Against undirected search, or simply re-running the agent more, at matched budget:
  unclear in all 21; budget matching is a clear yes in 1 (partial 4).
- **A held-out split disjoint from critique and selection data.** Yes 9 · partial 5 · unclear 6 · no 1. Corpus
  members concede maxpooling over a final beam and test-guided selection, so expect this to be probed.
- **Optimizer cost, including proposer tokens.** Yes 6 · partial 2; cost grows with graph edges and proposer
  histories, and equal evaluation budgets hide it.
- **Variance across runs.** Yes in only 3 of 21; expect a request for seeds or repeated runs.
- **Evidence that attribution is right.** A retained-artifact ablation (yes 4) and a leakage or test-selection
  guard (tested 1) are the closest proxies reported; attribution accuracy itself is rarely measured.
- **Certification beyond proxies.** Auto-generated proxy tests and model-generated evaluation are conceded
  limitations in corpus members; a reviewer will ask for ground-truth or hidden checks.

## Cognitive barriers
- That a black-box score is the only usable optimization signal for non-differentiable artifacts.
- That a failed run means the artifact is wrong; the failure can be an execution lapse of correct guidance.
- That propagating feedback further back gives better credit; deep chains grow and lose specificity.
- That a richer critique is the contribution; selection, retention and scope decide what the loop can claim.

## Lessons
### From accepted work
- Tie output feedback to the minimal part of the artifact that produced it, and edit only that part.
- Feed successes as well as failures, and accept only edits that individually improve a validation set.
- Spend evaluation budget deliberately (bandits, tree search, score predictors) and report its cost.
- Give the proposer raw traces and the full candidate history instead of compressed summaries.
- Package improvements as portable artifacts and concede open transfer questions rather than claim them.
- Attribution itself can be supervised, e.g. from counterfactual replay and injected faults.
### From rejected work
- Pointing the unchanged loop at a new domain task reads as an application, whatever the domain gain.
- Adding a cue to the per-step critique, with topology and selection unchanged, reads as a tweak.
- Check that feedback actually isolates errors in the edited artifact before optimizing against it.
- Evolving one executable program is program synthesis; make the harness, not the deliverable, the object.
- When the loop builds its own validation data, certify on data it did not generate.
- Preservation tests and section edits are table stakes; do not present them as the novelty.
