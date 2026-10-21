# EvolveR: retaining strategic experience helps a trained agent — but self-distillation is not the whole gain

*A Reel interpretation of [arXiv 2510.16079v3](https://arxiv.org/abs/2510.16079v3), **EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle** (HarnessRSI Daily score 65, ★★). Code: [Edaizi/EvolveR](https://github.com/Edaizi/EvolveR).*

## What the system changes about itself

EvolveR changes **both an external experience repository and the agent's policy weights**. It is not a weight-frozen memory-only method. Its harness-level artifact is a searchable library of strategic principles: each entry contains a concise natural-language description, structured subject–predicate–object triples, linked source trajectories, and historical usage/success counts. Successful trajectories yield guiding principles; failures yield cautionary ones. The same policy model distills these principles during an offline phase with its parameters frozen; online trajectories subsequently train the policy with GRPO.

During problem solving, the agent can search its experience base, search an external factual knowledge base, or answer, interleaved with reasoning. Each experience search returns the top three principles. Retrieved experience and external information are context with their token losses masked by default, not direct imitation targets.

## The loop, and the keep/reject rule

1. Collect online trajectories while the agent uses knowledge search and experience retrieval.
2. With policy parameters frozen, self-distill the successful and failed trajectories into principles.
3. Deduplicate semantically equivalent principles from the same problem. Match candidates against existing entries using embedding similarity (prefilter threshold **0.85**) followed by the policy model's yes/no semantic-equivalence judgment. Add a novel principle; merge a redundant trajectory under its existing principle.
4. Track historical effectiveness using **s(p) = (successes + 1) / (uses + 2)**. Periodically remove principles scoring below **0.3**.
5. Train the policy with GRPO using ground-truth exact-answer correctness plus a format reward that shapes reasoning and search actions; repeat the lifecycle.

This is a historical-utility retention rule, not a candidate-versus-incumbent validation test. The paper does not specify a more granular causal attribution rule for success when several principles are retrieved together. The lifecycle also has a teacher-assisted cold start: GPT-4o constructs about 700 training trajectories from NQ/HotpotQA questions with relevant documents and gold answers supplied. “Self-distillation” describes the subsequent principle writer, not a wholly teacher-free training pipeline.

## Headline result, as reported

Table 1 reports normalized Exact Match (EM), with a seven-benchmark average:

| Model | EvolveR | Strongest baseline average |
|---|---:|---:|
| Qwen2.5-3B | 0.382 | 0.325 (Search-R1-instruct) |
| Qwen2.5-7B | 0.417 | 0.385 (Search-R1-instruct) |

The experience base is described as built from **NQ and HotpotQA training splits**. TriviaQA, PopQA, 2WikiMultiHopQA, Musique and Bamboogle are described as out-of-domain evaluation datasets. The paper does not specify the precise evaluation split identifiers/sizes, which checkpoint produced Table 1, or seeds/runs per cell. These are **averages across benchmarks, not reported multi-seed means**; no variance or confidence intervals accompany the main comparisons.

The gains are uneven. At 7B, the largest improvements over Search-R1-instruct are on **NQ (0.462 vs 0.393)** and **PopQA (0.473 vs 0.397)**. HotpotQA is 0.411 vs 0.370, while TriviaQA is only 0.620 vs 0.610. At 3B, relative to the best baseline in each column, the more pronounced gains are on 2WikiMultiHopQA (0.381 vs 0.319) and HotpotQA (0.373 vs 0.324); Bamboogle is only 0.328 vs 0.320. Improvement spans several tasks, but the average should not be read as an equal benefit everywhere.

## The controls that decide whether the gain is real

- **Same trained policy, retrieval disabled only at evaluation (Table 3).** At 3B the average falls from **0.382 to 0.340**. This is the cleanest evidence that the retained repository matters beyond the policy weights. The largest per-benchmark drop is Bamboogle, 0.328 to 0.240; TriviaQA changes only from 0.584 to 0.569. The averages fall from 0.150 to 0.078 at 0.5B and from 0.270 to 0.123 at 1.5B. This tests an experience-trained agent's dependence on its memory, not whether another baseline would benefit equally from that memory.
- **Component attribution (Table 4).** At 3B: neither memory nor RL, 0.134; RL without principle distillation/retrieval, 0.325; distillation plus retrieval without RL, 0.357; experience-driven RL with evaluation retrieval disabled, 0.340; full system, 0.382. The two RL-related controls at 0.325 and 0.340 are different conditions, not interchangeable “RL-only” scores.
- **Same mechanism, different principle writer (Table 2).** GPT-4o-mini teacher distillation beats self-distillation at 0.5B (**0.220 vs 0.150**) and 1.5B (**0.290 vs 0.270**). Self-distillation leads on the 3B average (**0.382 vs 0.370**), but not on every task: the teacher reaches **0.437 on 2WikiMultiHopQA**, against self-distillation's 0.381. The authors' “cognitive alignment” explanation is an interpretation, not an isolated causal test.
- **SFT versus GRPO with the same successful online trajectories available (Table 8).** SFT gives 0.357 against GRPO's 0.382; GRPO additionally learns from failed trajectories. TriviaQA is tied at 0.584, and Bamboogle shows the largest difference, 0.248 vs 0.328. SFT training settings are provided, but the comparison is not stated to be compute-matched.
- **Curation diagnostics, not a direct causal pruning ablation.** Among 100 manually annotated principles, the high-score tier is 82% ideal and 8% incorrect/misleading, versus 26% and 24% in the low-score tier (Table 6). These are different score tiers, not a before/after pruning experiment. The pruning sweep at 1.5B gives 0.270 at the default 0.3 and 0.276 at 0.9 (Table 9). The paper does not state which split selected the default, other hyperparameters, or checkpoints, nor the baselines' tuning-search budgets.
- **Comparable experience and compute.** The teacher-distilled variant gets the same experience mechanism, and the SFT control gets the same successful trajectories. The main Search-R1 and other Table 1 baselines are not reported with EvolveR's curated principle/trajectory store; no raw-trajectory-store comparator or matched accumulation-budget comparison is reported. For 3B, the reported full lifecycle takes **39.4 hours on eight A100 (80GB) GPUs**, including cold-start SFT and GRPO. Separate offline curation and teacher-generation costs are not itemized, and baseline training runtimes/token budgets are not provided. A roughly 14,000-principle lookup takes 0.06 seconds; that is retrieval latency, not the cost of accumulating the store.
- **Leakage boundary.** Training-split construction and evaluation-only datasets are stated, but the full appendix reports no question/answer or near-duplicate overlap audit and does not explicitly specify whether evaluation trajectories are barred from later memory updates. The scalability experiment uses a random 10% validation subset across six unnamed benchmarks (Table 7); its relationship to the headline evaluation and default/checkpoint selection is unspecified. Related train/evaluation questions therefore cannot be ruled out from the paper alone. This is an unresolved protocol boundary, not evidence that evaluation tasks entered the store.

## Where the gain is absent or small

- **3B does not lead every benchmark.** TriviaQA: 0.584 vs Search-R1-base's 0.587. PopQA: 0.434 vs that baseline's 0.435. Its Bamboogle margin over Search-o1 (0.328 vs 0.320) is small, with no uncertainty reported.
- **7B loses 2WikiMultiHopQA.** EvolveR 0.395 vs Search-R1-instruct 0.414. Its small TriviaQA margin cannot be assessed against run-to-run noise because variance is unreported.
- **Self-distillation is scale-dependent.** It loses the average to teacher distillation at both smaller scales; the favorable 3B comparison does not establish a general advantage over teachers.
- **More accumulated experience is not monotonically better.** On the scalability validation subset, 45,083 principles give 0.410 EM, while 49,934 give 0.387 (Table 7). Since memory and policy evolve together, our reading is that this is a joint training trajectory, not an isolated memory-size experiment.
- **Directly training on retrieved experience tokens does not improve the average.** Unmasking their loss gives 0.371 vs the default 0.382 (Table 11), although PopQA slightly reverses this, 0.435 vs 0.434.

## Our read

HarnessRSI score **65**, band **★★**, evidence level **retained**. The record credits cross-task evaluation, retrieval ablation and the self-versus-teacher comparison. The retained-memory evidence is stronger than an unablated headline: the same trained policy loses accuracy without the store. But the overall result couples memory with weight updates, and the paper does not establish that the experience curator itself becomes a better improver at comparable budget. Later-phase principle scores are measured only among surviving entries (Table 10), not against a frozen improver.

The stored judgment leaves optimizer cost unclear; the full v3 PDF does report the 39.4-hour lifecycle runtime and retrieval latency, so we note that correction without changing the score or judgment files. The central remaining limits are unreported run variance, unmatched experience/training budgets, and incompletely specified split, selection and contamination boundaries.
