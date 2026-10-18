# Anti-patterns — reject-leaning moves in harness-level RSI

ResearchStudio's anti-patterns are 2-way pattern *compositions* that ICLR/ICML/NeurIPS reviewers rejected far more
often than base (n ≥ 30, Δ ≤ −12 pp, on ~1,900 papers). Our labeled universe is smaller, so **no composition reaches
n ≥ 15** (`research/patterns/contrast.json` → `anti_pattern_candidates` is empty in every view). The entries below are
single sub-/main patterns instead, kept only when the signal is consistent across views.

**How to read this page.** Acceptance is not quality. Each view runs ~50 pattern tests, so a 95% CI that excludes the
base rate can still be chance once in a while; we lean only on signals that hold across views. Rejected papers in our
data are mostly abstract-only OpenReview records, so differences below are about *mechanism and framing*, never about
how much evidence or how many limitations a paper reports.

## AP1 — Single-document critique-and-rewrite as the contribution ([H10](sub/H10.md))

| view | n | accept rate | base | Δ | 95% CI |
|---|---|---|---|---|---|
| ICLR 2025–26 | 30 | 16.7% | 34.4% | −17.7 pp | 7.3–33.6% |
| ICLR 2025–26, high-fit only | 22 | 18.2% | 39.3% | −21.1 pp | 7.3–38.5% |
| all labeled | 39 | 35.9% | 57.6% | −21.7 pp | 22.7–51.6% |

The only signal whose CI excludes the base rate in all three views. The move: hold one textual artifact (prompt,
rule document, rubric, tool description) as the incumbent, verbalize errors as a critique or "textual gradient", rewrite,
keep the best.

**Failure mode.** The critique-and-rewrite loop itself is now shared by accepted and rejected work alike; what reads
as a tweak is keeping that skeleton and only (a) adding one more cue to the per-step critique, or (b) pointing the loop
at a new domain. The root assumption that fails: *a rewrite that fixes the targeted errors is a net improvement* —
in practice it overspecializes to the failures, oscillates under immediate feedback, inherits judge bias, and overfits
the sample questions; a headline selected with test data is an upper bound, not a result.

**Required mitigation if you work here.** Put the novelty in the *selection and retention rule* — how evaluation budget
is spent across candidate rewrites (bandit, tree search, score prediction) and how earlier wins are protected
(edit-level acceptance, preservation checks on previously-correct cases) — and show it against other optimizers at a
matched evaluation budget, with selection data separate from the reported test set.

## AP2 — Attribute-and-patch where the attribution is not the novelty ([attribute_and_patch_incumbent](main/attribute_and_patch_incumbent.md))

ICLR 2025–26: n = 41, 22.0% vs 34.4% (Δ −12.4 pp, CI 12.0–36.7%, contains base); all labeled: n = 56, 42.9% vs 57.6%
(Δ −14.8 pp, CI 30.8–55.9%, excludes base). Most of the ICLR signal is AP1 (30 of 41 members), so this is AP1 seen one
level up rather than an independent finding. Accepted members change *what gets attributed and where budget goes*
(minimal responsible subgraph, local refinement instead of long backward chains, defect-vs-lapse gating); rejected
members keep the skeleton and patch a single domain artifact.

## Watch list (not significant, same direction in every view)

- **Reflect-and-store presented as "learning without weight updates"** ([H00](sub/H00.md), parent
  [abstract_experience_into_guidance](main/abstract_experience_into_guidance.md)): ICLR n = 16, 18.8% (Δ −15.6 pp,
  CI 6.6–43.0%). Rejected members more often port the attempt → reflect → store → retrieve loop into a new vertical and
  claim continual learning, without separating the lesson's effect from extra compute or from exposure to the test stream.
- **Forge-a-tool-on-gap as one component of a larger system** ([H07](sub/H07.md)): below base in the views where it has
  enough labeled papers; rejected members fold tool creation into a bigger architecture instead of making the forged tool
  and its repair loop the measured contribution.

## Not anti-patterns, but often mistaken for them

- Self-generated curricula ([self_generate_the_curriculum](main/self_generate_the_curriculum.md)) sit *above* base at
  ICLR (n = 26, 57.7%, CI 38.9–74.5%) — but they are a boundary pattern (weights are trained), and the rejected ones steer
  generation by difficulty or novelty with no validity check the generator cannot game.
- "Make the improver editable" looks strongly favored in the all-labeled view (n = 13, 92.3%), yet only 6 papers are
  countable at ICLR. Treat it as a hypothesis.

Numbers: `python3 research/contrast.py` regenerates every rate on this page.
