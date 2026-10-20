# Library Drift: a frozen LLM curates its own skill library — which governance knobs matter, and what the ablations do not test

*A Reel interpretation of [arXiv 2605.19576v3](https://arxiv.org/abs/2605.19576v3) (HarnessRSI Daily score 74, ★★★). Code: [amazon-science/Self-Evolving-Agents-Ratchet](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet). Workshop paper (FAGEN @ ICML 2026).*

## What the system changes about itself

The paper studies **Ratchet**, a loop in which a frozen LLM (Claude Opus 4.7) writes, retrieves, curates and retires its own natural-language **skills**; no weights change. The authors name a failure mode, **library drift**: skills accumulate without outcome-driven lifecycle management, retrieval degrades, stale skills are injected, and the agent stagnates or falls below its no-skill pass rate.

Each round the loop does five things: route the held-out tasks (the Router picks one skill or NONE: tf-idf and embedding shortlists, then an LLM gate); run the same pipeline on the train tasks to collect failures; have a Critic LLM label every failure HELPED / HURT / NEUTRAL / INAPPLICABLE with a pattern; have a Synthesizer write a new skill from a cluster of at least 3 failures with the same canonical pattern; have a Curator update per-skill scores and retire skills.

## The keep/reject rule

The signal is a per-skill **contribution score** ĉ(s) = (successes − failures) / trials, over the tasks where the skill was injected. Three governance mechanisms form the "fix":

1. **Outcome-driven retirement.** A skill is retired once it has at least N_min = 100 trials and ĉ ≤ −0.10.
2. **Bounded active cap.** At most 50 active skills; the lowest-contribution skill is evicted when synthesis would exceed the cap.
3. **Meta-skill authoring prior.** A document in the Synthesizer prompt that makes new skills stylistically consistent.

## Headline, as reported

MBPP+ hard-100: from the 378-task MBPP+ test split the authors drop tasks Claude Opus 4.7 solves on all 5 baseline seeds and sample 100 of the rest (60 train / 40 eval, fixed seed). The solver is one LLM call, with no execution feedback or tools. Each run is 100 rounds; results are mean ± std over 3 seeds (Table 1).

| | Default (full governance) |
|---|---|
| Baseline (round-0 held-out pass@1) | 0.258 ± 0.047 |
| Late-window mean (abstract) | 0.584 |
| Peak | 0.658 ± 0.042 |
| Gain = mean(last 10 rounds) − mean(first 10 rounds), within each run | +0.328 ± 0.018 |

Per seed the Default gain is +0.303, +0.340, +0.343 (Table 3). Note that 0.584 − 0.258 = 0.326‡, not 0.328: the paper computes the gain within each run.

## The controls that decide whether the gain is real

All controls are ablations of the paper's own system; 3 seeds each, 40 eval tasks from one fixed-seed split (Sec. 6.1; Table 1, Table 3).

- **A1, no skill injection** (Router forced to NONE; the paper says the synthesizer, critic and curator still run): +0.002 ± 0.005. This is the paper's no-skill floor: with injection off the loop shows no gain. One internal inconsistency: Table 1 lists 0 critic calls for A1 yet 42 active and 15 retired skills at round 100, although skills are born from critic-labelled failure clusters and retirement needs injection trials, so the floor is less clean than the text suggests.
- **A2, retrieval-only routing** (no LLM gate): +0.077 ± 0.065 (per seed +0.148, +0.095, −0.010).
- **A3, no meta-skill:** +0.187 ± 0.036, i.e. 0.141 below the Default; the paper calls the meta-skill the single most valuable component.
- **A4, harsh retirement** (two knobs changed together: N_min 100 → 20 and τ 0.10 → 0.0, although the paper says each ablation modifies one knob; it attributes the harm to the evidence floor but cannot separate the two): −0.019 ± 0.010 (per seed −0.005, −0.027, −0.025). The bank collapses to 2 active skills and router engagement falls to 19%. This is the paper's example of drift below the no-skill baseline, and it is produced by over-aggressive governance, not by unbounded growth.
- **A5 no canonicalisation +0.374 ± 0.023, A6 no cover-guard +0.363 ± 0.033, A8 meta-skill refreshed every 10 rounds +0.372 ± 0.017** (peak 0.725; 10.1 h vs 6.5 h wall time). All three are numerically above the Default; the paper calls A5/A6 "within ±2σ at n = 3" and concludes explicit dedup is not necessary at this scale.
- **A7, cap = 100:** +0.317 ± 0.110, per seed +0.172, +0.340, +0.440. Comparable mean (+0.317 vs +0.328), much higher spread; the paper says the cap "primarily controls variance rather than mean".
- **Cost.** The Default uses about 14.5k LLM calls per 100 rounds (10k solver + 4.3k critic + 152 synthesis), 43% more than A1 (10k) by the paper's figure (its own breakdown sums to about 45%‡), and 6.5 h vs 2.3 h of wall time. The solver calls are the same count; the extra calls are critic and synthesis.

## Where the gain is absent or the evidence is thin

- **No row removes retirement or the cap.** Table 1 has eight variants; none runs without retirement, none without a cap, and none lets the library grow unbounded. The "bloat" sub-mode is attributed to earlier systems and described as prevented in the Default, not run. So the statement that retirement and the cap are the load-bearing pieces rests on A4 (harsher retirement hurts) and A7 (looser cap: same mean, more variance), plus the meta-skill ablation A3.
- **No external baseline.** No other skill-library system (Voyager, ExpeL, …) and no human-curated skills are run; the +0.0pp vs +16.2pp SkillsBench figures are cited from another paper. No compute-matched no-skill run is reported.
- **Small eval set, noisy numbers.** 40 eval tasks (one task = 0.025‡). Round-0 baselines of the identical pipeline range from 0.200 to 0.300 across condition means (0.175 to 0.350 per seed, Table 3), which the paper attributes to sampling noise from the 40 eval tasks. A4's harm (−0.019) is smaller than one task. Peak is a maximum over noisy rounds: A1, which never injects a skill, has a peak of 0.375 against a baseline of 0.283.
- **A2 is small and noisy** (+0.077 ± 0.065, one seed negative). Three variants (A5, A6, A8) score above the Default, so the Default is not the best-scoring recipe in the table.
- **The proof is loose.** Proposition 1 bounds the pass rate at no worse than E[p0] − 0.35; the paper itself calls the bound loose at this scale. Separately, its quoted Hoeffding ε ≈ 0.20 (N_min = 100) and 0.44 (N_min = 20) match a range-1 bound with δ = 10⁻³ in our recomputation, whereas ĉ ranges over [−1, 1]; and A4 does not test the bound, although the paper says it "validates Prop. 1".
- **Scope.** One benchmark, one model, thresholds chosen empirically; multi-step agents, where the authors expect drift to matter more, are future work. The paper does not say how the Default's meta-skill was written or how the Default knob values were chosen, and it describes no leakage check beyond the fixed train/eval split.

## Our read

HarnessRSI score **74**, band ★★★, evidence level **retained**: the retained artifact (a governed skill library) helps on a held-out eval split. Skills are written from train-split failures (App. A), but the paper is silent on whether eval-task outcomes also feed the Curator's contribution scores, so the held-out claim is less clean than it looks. The paper reports a held-out split, 3-seed variance with a per-seed table, eight ablations of the governance mechanisms, and the optimizer cost. It does not report transfer to another task or model, a run against other skill-library systems, a fully compute-matched comparison (our judgment: partial), or a leakage check. The one-benchmark, 40-task scale and the missing no-retirement / no-cap rows mean the diagnosis of drift and the claim that retirement and the cap are essential are supported more by the A1 and A4 triggers than by a direct unbounded-library run.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
