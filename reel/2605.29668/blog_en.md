# GRASP: an agent edits its own skill library, but only keeps edits that do not break what already worked

*A Reel interpretation of [arXiv 2605.29668v3](https://arxiv.org/abs/2605.29668v3) (HarnessRSI Daily score 84, ★★★). Code: [jomoll/GRASP](https://github.com/jomoll/GRASP). The paper is CC BY 4.0.*

## What the system changes about itself

GRASP keeps a small, versioned **library of skills** — Markdown documents with a trigger condition, a behavioural rule, an optional verification step and a contrastive example — that is injected into the agent's context at inference. The library starts empty. No model weights are updated; the retained artifact is the library (at most 10 skills, 5 on average, about 5.6k tokens).

## The loop, and the keep/reject rule

1. After each batch of 48 development episodes, failed traces are grouped by an LLM-assigned, mechanism-specific failure label.
2. A skill-writing model proposes K = 4 candidate edits for the most frequent failure modes; each one adds, modifies or removes a skill. Adding is blocked at capacity unless a removal frees a slot.
3. Every candidate is re-run on a **probe** of 36 earlier examples, half previously failing and half previously passing; the current library is re-run too, to get a fresh baseline (F0 fixes, R0 regressions).
4. A candidate is accepted only if it fixes more than it breaks, (F(c) − F0) − (R(c) − R0) > 0, **and** causes no regression beyond the baseline, R(c) ≤ R0. The best candidate that passes is applied; otherwise the library is left unchanged.
5. Training runs for 5 epochs; the best-validation checkpoint is restored and the test and out-of-distribution (OOD) splits are evaluated once.

## Headline result, as reported

On MedAgentBench, a FHIR electronic-health-record benchmark scored against server state, gpt-oss-120b goes from **40.6%** (no skills) to **88.8%** test accuracy. The strongest of five self-improvement baselines, Evo-MedAgent, reaches 67.8%, a gap of 21.0 points (95% CI [10.3, 33.8], five seeds). On the OOD split GRASP scores 56.3% against 31.3%. The other four base models gain 17.2 to 40.3 points over no skills. Open-source models use five seeds, proprietary models three.

## The controls that decide whether the gain is real

- **Ablations (Table 4, gpt-oss-120b, labelled three seeds).** Full method 88.8%. Without failure grouping 84.4%; without the regression budget 81.8%; selecting on fixes only 80.2%; append-only 80.2%. Removing the gate altogether: 63.5% at K = 4 and 40.1% at K = 1. The K = 1 test score is close to the no-skills 40.6%, but its OOD score is 27.2 ± 24.7 against 8.7 for no skills (Table 5), so "matches no skills" holds for the test split only. The full-method 88.8 ± 5.8 is the same value as the five-seed Table 1 entry, so ablation rows and full method are not clearly seed-matched; the same applies to the Table 2 diagonals.
- **Matched compute.** Two variants run the full probe but select without its scores (by the writer's preference or at random) and reach 70.8% and 67.2%. Probe compute alone does not explain the gain.
- **Same gate for the baselines (Table 5, five seeds).** Adding the gate to all five baselines raises each one's in-domain test score at K = 1, by +1.6 to +15.0 points, but several of these changes sit well inside seed noise (Evo-MedAgent 67.8 ± 14.1 to 69.4 ± 9.2; Seq. memory 41.2 ± 5.5 to 45.6 ± 13.2); none improves out of distribution (mean change −0.1). At the same K = 1, GRASP scores 73.4 ± 23.1 test and 50.9 ± 20.0 OOD against 69.4 ± 9.2 and 30.7 ± 11.8 for gated Evo-MedAgent, so the in-domain gap at equal K is inside the noise; the 88.8% needs K = 4. Moving the baselines to K = 4 lowers some of them (Evo-MedAgent 69.4 to 55.7; SkillX 57.5 to 55.9), which the paper attributes to candidate collapse. With K = 4 no gated baseline exceeds 62.2% test or 26.1% OOD. Batch memory uses 439 probe calls per batch against GRASP's 411; per-episode methods use 29× and 51× as many. This experiment was run only on gpt-oss-120b and MedAgentBench.
- **Statistics (Table 13).** The in-domain gap to Evo-MedAgent is significant (p = 0.008, five seeds). The OOD headline, 56.3 vs 31.3, has a bootstrap CI of [3.7, 44.0] but p = 0.087, so it is not significant at 0.05. Three-seed rows cannot go below p = 0.10, and no multiple-comparison correction is applied.
- **Transfer.** A frozen library written by GPT-5.4 lifts gpt-oss-120b on OOD from 56.3% (its own library) to 77.8%, and Gemini 3.1 Flash Lite from 41.7% to 71.1%, at a cost of 12.8 points in-domain for gpt-oss (88.8% to 76.0%). Libraries from weaker writers are mostly worse than self-training, with exceptions: a Gemini library on gpt-oss-120b reaches 57.8 OOD vs 56.3, and a gpt-oss library on Gemini 79.7 test vs 71.4. The paper draws no conclusion from the Gemini-source cells (OOD standard deviations above 30). The baseline comparison (Table 14) uses the *ungated* self-trained baselines, in two writer-to-executor configurations only; their GPT-5.4 libraries are weak at the source (OOD 1.7 to 16.7), so little knowledge was there to transfer. A gated-baseline transfer was not run.
- **Independent benchmark.** On FHIR-AgentBench, self-training lifts gpt-oss-120b from 51.5% to 58.2% (+6.8, CI [3.7, 10.0], five seeds), a much smaller gain than on MedAgentBench; libraries from other benchmarks (47.2%, 45.7%, 48.3%) fall below the 51.5% baseline.
- **Leakage audit (Appendix F).** The gate sees only pass/fail, but the failure classifier and skill writer see expected answers, so the authors audited all 106 learned libraries against ground truth for every split: no held-out value appears in any Trigger, Rule or Verification section; thirty dev-split values appear, all inside demonstrations or code blocks; four collisions with hidden splits are low-entropy domain constants.
- **Cost.** The probe is the main cost: 411 probe calls per batch, roughly 3.7× the training-time calls of the simplest memory baselines.

## Where the gain is absent or small

- **MedAgentBench-v2, in-domain.** GRASP leads on gpt-oss-120b (76.9% vs 67.8%) and DeepSeek (30.9% vs 25.3%); the Gemini gap (67.2 ± 2.7 vs 65.1 ± 3.3) is within noise. On GPT-4.1 it scores 70.3%, against 70.5% for no skills and 74.0% for SkillX; on GPT-5.4, 63.3% is within noise of the best baseline.
- **MedAgentBench-v2, OOD.** GRASP is below no skills on three of five models: DeepSeek 67.0% vs 83.6%, GPT-4.1 82.8% vs 84.9%, GPT-5.4 80.0% vs 82.7%; on gpt-oss-120b it scores 86.0% against 87.1% (SkillX). The authors make no superiority claim on v2 OOD.
- **Non-clinical environments (Table 6).** Exploratory: gpt-oss-120b only, three seeds, compared with no skills only (no baselines, no gate control), on small test sets (ALFWorld 20, OS Interaction 35, WebShop 50, DBBench 60 episodes). ALFWorld 23.3% to 51.7%, WebShop 20.7% to 41.3%, DBBench 65.6% to 70.6%, OS Interaction 48.6% to 49.5% (no gain beyond seed noise).
- **Variance.** OOD 56.3 ± 14.5 on gpt-oss-120b; Gemini OOD 41.7 ± 20.9 against 38.3 for SkillX.
- **Scope.** The benchmarks score procedural reliability against FHIR state, not clinical correctness or patient outcomes.

## Our read

HarnessRSI score **84**, band ★★★, evidence level **retained**. The paper reports held-out test and OOD evaluation, cross-model and cross-benchmark transfer, multi-seed variance, optimizer cost, ablations of the retention rule, and a ground-truth leakage audit of the learned libraries (Appendix F). The matched-compute comparison is partial (within GRASP, and for gated baselines on one model). Our judgment left the improver comparison unclear, but the full paper does vary and compare the improvement mechanism itself (gate removed, matched-compute selection, append-only, gate granted to five baselines), so the evidence level may be understated. Caveats: the strongest controls use a single base-model/benchmark pair, several comparisons are inside seed noise, and the OOD headline is not significant at 0.05.
