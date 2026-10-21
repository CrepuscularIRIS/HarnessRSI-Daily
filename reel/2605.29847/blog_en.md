# EvoRubric: learning the checklist as well as the answer — with an independent judge and incomplete compute accounting

*A Reel interpretation of [EvoRubric: Self-Evolving Rubric-Driven RL for Open-Ended Generation](https://arxiv.org/abs/2605.29847v2), arXiv 2605.29847v2. HarnessRSI score 63, band ★★; recorded evidence level: improver. No code link supplied.*

## What the system changes about itself

EvoRubric changes both **model weights** and **the criteria used to reward responses**. One Qwen3 policy plays two roles: Reasoner and Rubric Generator. Its non-weight artifact is a memory pool attached to each training query, not a universal inference-time checklist. Separate policies are trained for Medical, Writing and Science, at both 8B and 14B.

A rubric is a list of observable positive requirements and negative, active-error constraints with signed points. The Generator template permits integer weights from −10 to 10. For the paper's insulin-storage example, new criteria address formulation-specific storage duration, handling, device instructions and source verification. The frozen pre-RL Qwen3 model writes the fixed base rubrics once; the learned shared policy proposes additional criteria from its current responses, base rubrics and historical pool.

## The loop and the keep/reject rule

1. Start with an empty per-query evolved pool; keep the base rubrics separate and fixed.
2. Sample 8 Reasoner responses and 4 candidate rubric sets per query.
3. A **frozen copy of the initial, same-scale Qwen3 policy** screens criteria for validity and redundancy. **GPT-OSS-120B**, also frozen, grades responses against the accepted criteria.
4. A verified candidate batch is eligible only if its response-score vector is nonconstant and its leave-one-out correlation with peer batches exceeds **0.2**. All eligible batches contribute to the current response reward, but **only the highest-consensus eligible batch** can add criteria to memory, after exact-text duplicate checks. Empty or fully rejected batches add nothing.
5. Remove saturated criteria: positive requirements satisfied by every response, or penalized errors avoided by every response. Exclude zero-variance historical criteria from current scoring. Keep at most 10 evolved entries per query, evicting the oldest when necessary.
6. Update both roles' shared weights with GRPO, standardizing their advantages separately. The next visit uses the updated policy and revised memory.

The Reasoner reward is the normalized base-rubric score plus the historical and mean eligible-current scores, each pool term weighted **0.5**, minus a length penalty. Generator rewards combine validity, discrimination and peer agreement, with count, length and weight-concentration penalties (Appendix C). This is **not outcome-only RL**; the paper does not include an outcome-only RL comparator. Nor is memory admission a held-out performance gate: peer agreement does not establish correctness. The prose and Algorithm 1 agree on empty initialization and the admission rule.

## Headline result, as reported

Table 1 gives means ± standard deviations over **three training seeds for RL methods**, versus **three response-sampling runs for Base**. Its unweighted five-benchmark averages are:

| Backbone | Static Rubric-RL | External Evolving-RL | EvoRubric | Reported margin over best matched average |
|---|---:|---:|---:|---:|
| Qwen3-8B | 52.90 | 53.19 | 56.28 | 3.09 |
| Qwen3-14B | 59.05 | 59.07 | 61.13 | 2.06 |

**No variance or confidence interval is reported for these macro-averages.** The per-benchmark EvoRubric means are highest among the matched Table 1 methods at both scales, but this is not a significance claim. At 8B the largest relative gains are on HealthBench (**14.2%**) and Creative Writing (**8.4%**); the gain is uneven rather than confined to one benchmark.

Training uses 3,000 queries per domain from HealthBench, Long-writer-zero and ResearchQA. Evaluation includes **500 held-out HealthBench instances**, Chinese LLMEval-Med, WritingBench, Creative Writing and held-out ResearchQA queries. The paper does not give the other evaluated sample counts or detailed partition construction. The final judge is **claude-sonnet-4-6**, retaining benchmark evaluation criteria but replacing the original judge. A different model family reduces direct coupling to the Qwen3 verifier and GPT-OSS training Grader; it does not establish that judge preferences cannot favor the method. No multi-judge robustness experiment is reported.

## The controls that decide whether the gain is real

- **Explicitly learning the Generator matters (Table 2, Medical, Qwen3-8B).** Full HealthBench/LLMEval-Med scores are **45.13 / 53.75**. Removing Generator loss gives **41.58 / 49.93**. This variant still generates rubrics and retains verification, grading, memory and selection; its Generator can change indirectly through shared Reasoner updates. Removing discrimination gives **38.92 / 51.11**; consensus **40.80 / 50.16**; historical memory **42.26 / 52.41**; Meta-Verifier **43.13 / 47.81**. Without memory, current-rollout criteria remain. These are averages over **3 matched runs, without per-variant variance or CIs**; they do not establish the same effects across all domains or both scales.
- **What each baseline gets.** Static Rubric-RL uses frozen-base-model, few-shot-generated fixed rubrics. External Evolving-RL uses a separate unoptimized same-scale generator. Both share the policy backbone, training data and policy-side configuration with EvoRubric. The Medical-only Qwen3-8B GPT-4.1 variant proposes evolving criteria using current responses and existing rubrics: **42.25 / 52.92**, versus EvoRubric **45.13 / 53.75** (Table 3; means over 3 runs, no SD/CI). It is DR-Tulu-style generation **within this training setting**, not the full DR-Tulu system with search and citation training. The paper does not fully enumerate which verifier, consensus, admission and generator-budget settings each external baseline shares; we do not infer that they lack all safeguards. No end-to-end matched-compute comparison or comparable reward-model training budgets are established.
- **Initialization (Table 4).** On HealthBench-8B, expert rubrics raise Static Rubric-RL from **38.89 to 41.83**; EvoRubric with expert initialization reaches **44.64**, versus **45.13** with model initialization. The reported **0.49** difference has no variance/CI here, so it does not show model-written priors are superior.
- **Human validity audit is not a leakage audit.** Three experienced annotators examine 20 Medical prompts. Final 8B invalid criteria are **8/157 (5.10%)**, versus **75/192 (39.06%)** without verification; at 14B, **6/139 (4.32%)** (Table 5). A separate fixed-response comparison prefers EvoRubric rubrics **72% versus 28%** on 100 HealthBench queries (Appendix G, Claude judge). The split membership of these audit/comparison prompts is not specified; neither is a demonstrated held-out rubric-transfer test.
- **Split and tuning story.** Algorithm 1 evolves pools on training queries, and final evaluation includes explicitly held-out sets. However, neither the split used to select hyperparameters/defaults nor the checkpoint-selection rule is stated. Baseline tuning trial budgets are unreported. Numerical training defaults themselves **are** given: Table 7 includes 4 epochs, learning rate, batch size, decoding settings, rollout counts and clip bounds; Appendix C gives the consensus threshold and penalties. The evaluation judge uses “default settings” without explicit numerical decoding values. We found no prompt-overlap/contamination audit in the full appendix; the paper does not establish evolution on evaluation prompts, but also does not supply a detailed leakage audit.
- **Compute.** Table 7 lists **8 × NVIDIA H20**, 4 epochs, 8 responses and 4 rubric sets per prompt. No total EvoRubric cost, GPU-hours or wall-clock time is reported. Appendix H reports only the GPT-4.1 generator's API usage, averaged across three runs: **81.20 million input + 2.91 million output tokens**, **84.11 million total**, approximately **USD 185.70 per run**. This excludes other baseline costs and is not an EvoRubric cost comparison. The training Grader stays frozen; there is no separately trained baseline reward model with a documented comparable optimization budget.

## Where the gain is absent or small

**LLMEval-Med is modest.** EvoRubric-8B scores **53.75 ± 0.84** versus Static **52.95 ± 0.47**; at 14B, **59.23 ± 0.91** versus **58.30 ± 0.25**. The reported gains **0.80 / 0.93** are similar to EvoRubric's seed SDs. No significance tests are supplied. Removing the verifier actually drops 8B LLMEval-Med to **47.81**, below Base **49.25**.

**Human response improvements are concentrated in conciseness and relevance, not uniformly in factual quality.** On 50 Medical prompts, all following triplets are prompt-level win/tie/loss percentages (%), not counts. Overall quality is **42/30/28** against same-scale External and **48/14/38** against the GPT-4.1 variant. Completeness favors the baselines: **20/52/28** and **36/18/46**. Factual correctness is close: **40/22/38** and **42/14/44**; safety is mostly tied (Table 6). No CIs are reported.

**Rubric quality still drifts.** With verification, 8B invalidity rises from **1.08% to 5.10%** across epoch-end snapshots, while effective diversity falls from **89.19% to 75.16%**; at 14B diversity falls from **91.62% to 76.26%** (Tables 9–10). This diversity measure pools counts across the 20 prompts and deduplicates within each prompt, not across prompts. Frozen verification reduces errors, not eliminates them.

## Our read

The repository records **score 63, band ★★, evidence level improver** (batch b07). The full PDF supports held-out evaluation, cross-benchmark evaluation, multi-seed per-task SDs, retained-memory and improver-loss ablations, independent-family judging and narrow human audits. Its comparisons match policy-side configuration, not demonstrated total compute. Cross-benchmark gains come from domain-specific trained policies, not a frozen rubric pool transferred between domains.

**Judgment notes:** the stored `variance: unclear` understates Table 1's explicit three-training-seed SDs. The stored `leakage_guard: tested` cites criterion-validity auditing, which is not a train/test leakage test. We leave the judgment and score unchanged and record both corrections in SOURCE.md. Takeaway: learning a rubric writer together with the responder helps these reported means, but correctness, leakage protection and cost parity need evidence beyond consensus and a validity audit.
