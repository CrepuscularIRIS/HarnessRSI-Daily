# ExpeL: an agent turns its own trial-and-error into a rule list — and the gain depends on which control you read

*A Reel interpretation of [arXiv 2308.10144v3](https://arxiv.org/abs/2308.10144v3) (HarnessRSI Daily score 72, ★★★). Code: [LeapLabTHU/ExpeL](https://github.com/LeapLabTHU/ExpeL).*

## What the system changes about itself

ExpeL never changes model weights. Two things are retained between tasks: an **experience pool** (every trajectory from the training tasks, successes and failures) and a **list of natural-language insights** distilled from it. Both are written into the prompt of a frozen gpt-3.5-turbo-0613 ReAct agent at test time.

## Where the signal comes from, and the keep/reject rule

1. **Gather.** On the training tasks the agent runs ReAct and, if it fails, retries with Reflexion, up to Z = 3 times. The environment's success/failure signal labels each trajectory.
2. **Extract.** gpt-4-0613 reads either a failed and a successful trajectory of the same task, or a list of L successes (L = 8 for HotpotQA and ALFWorld, 4 for WebShop), and edits one insight list with four operations: ADD, EDIT, UPVOTE, DOWNVOTE. A new insight starts with importance count 2; UPVOTE or EDIT adds one, DOWNVOTE subtracts one, and an insight whose count reaches zero is removed. The paper presents this as protection against insights drawn from suboptimal successes.
3. **Use.** At test time the prompt holds the task, the full insight list, and the top-k successful trajectories most similar to the task (Faiss, all-mpnet-base-v2; k = 6 for HotpotQA, 2 for ALFWorld and WebShop). The agent gets a single attempt, with no retries.

## Headline result, as reported

gpt-3.5-turbo-0613 acts at test time; success rate in % (Figure 5, with standard errors over folds; HotpotQA 100 tasks, ALFWorld 134, WebShop 100; mean ± standard error over "four-fold validation").

| Benchmark | ReAct | ExpeL (one attempt) | ReAct + Reflexion, 3 retries (R3) |
|---|---|---|---|
| HotpotQA | 28 | 39 | 40 |
| ALFWorld | 40 | 59 | 54 |
| WebShop | 35 | 41 | 48 |

Table 3 gives the decimals for four cells: HotpotQA 28.0 ± 1.4 for ReAct and 39.0 ± 1.7 for ExpeL; ALFWorld 40.0 ± 0.3 and 59.0 ± 0.3. Against ReAct the gain is 11‡ points on HotpotQA, 19‡ on ALFWorld and 6‡ on WebShop (on HotpotQA Act is 29, so the gain over Act is 10‡). The Reflexion column is not a like-for-like baseline: it retries on the test tasks.

**Runs and variance.** Decoding is greedy at temperature 0, so there are no repeated runs or seeds; the ± values are spread across folds. The ALFWorld ± 0.3 is small for a 134-task pool (the reasoning-similarity row has ± 2.1; Act on FEVER is 58 ± 0.0). With the half/half split each fold evaluates about half of the pool, so the task counts above are pool sizes, not per-fold test sizes. The Reflexion lines in Figure 5 and the Figure 6 bars carry no standard error.

## The controls that decide whether the gain is real

- **Insights vs. retrieval (Figure 5).** Insights-only / retrieve-only: HotpotQA 36 / 31, ALFWorld 50 / 55, WebShop 37 / 38. Both parts help, and the full agent is highest in all three.
- **Where insights come from (Table 3, HotpotQA).** ReAct 28.0 ± 1.4; hand-crafted insights 32.0 ± 1.1; insights built with reflections added 29.0 ± 0.4; gpt-3.5-turbo as the extractor 32.0 ± 0.4; ExpeL (gpt-4-0613 extractor) 39.0 ± 1.7. The paper reads this as learned insights beating hand-crafted ones and a better extractor helping.
- **Retrieval rule (Table 3, ALFWorld).** ReAct 40.0 ± 0.3; random successes 42.5 ± 0.8; reasoning-similarity retrieval 48.5 ± 2.1; task-similarity retrieval (ExpeL) 59.0 ± 0.3.
- **Experience matters (Figure 6, HotpotQA).** ExpeL with only the initial few-shot examples 27, ReAct 28, ExpeL gathering experience with ReAct only (no retries) 35, full ExpeL 39. The paper states that insights extracted from the few-shot examples alone give no advantage over ReAct.
- **Transfer (Table 1).** Insights from HotpotQA, rewritten for FEVER by gpt-4-0613 (§5.4): Act 58 ± 0.0, ReAct 63 ± 0.4, transfer without task demonstrations 65 ± 1.7, transfer with demonstrations 70 ± 0.7. Act and ReAct get no such gpt-4 help; 65 ± 1.7 vs. ReAct's 63 is about one standard error. One source–target pair only; the transferred agent uses fixed few-shot examples, not a retrieval pool.
- **Reflexion on top (Table 2, ALFWorld, "preliminary").** ReAct + Reflexion 40.3 / 47.8 / 52.2 / 54.4 % at R0–R3; ExpeL retrieve-only 54.5 / 57.5 / 59.7 / 60.4 %; ExpeL + Reflexion 59.0 / 60.4 / 63.4 / 64.2 %. The Reflexion add-on helps with or without insights (64.2 vs. 60.4 at R3).
- **Matched experience, but not matched models or compute.** The ReAct and Reflexion baselines never get the training-set experience; the closest control is the paper's retrieve-only variant, which does (HotpotQA 31, ALFWorld 55, WebShop 38). The gpt-4-0613 insight layer adds 8‡, 4‡ and 3‡ points over retrieve-only; on ALFWorld retrieve-only alone gives 15‡ of the 19‡ points over ReAct. The baselines do not get the gpt-4-0613 extractor, and there is no matched-token or matched-compute row. The cost of gathering and extraction is not reported (hardware only). The evaluation tokens per trajectory (Table 6, "average counts per trajectory") are higher for ExpeL than for ReAct: HotpotQA 4310.06 vs 1319.75 (3.3‡ times), ALFWorld 2856.7 vs 2051.49 (1.39‡), WebShop 3291.31 vs 2575.41 (1.28‡). The text does not say how L, k or Z were chosen, and reports no contamination or leakage check; the task sets are the ones used by ReAct and Reflexion.

## Where the gain is absent or small

- **HotpotQA vs. Reflexion.** ReAct + Reflexion reaches 40 at R2 and R3, ExpeL's single attempt 39; the paper calls this "matches". Reflexion retries on the test tasks with environment feedback, ExpeL does not.
- **WebShop.** 41 for ExpeL vs. 43 for Reflexion at R1 (48 at R3); reward 0.701 vs. 0.665 for ReAct (Table 5). The paper itself says there is room for improvement.
- **Small SE-scale gaps.** HotpotQA insights-only 36 vs. full ExpeL 39 (SE of ExpeL 1.7). With gpt-3.5-turbo extracting insights, HotpotQA is 32.0 vs. 28.0 for ReAct, so most of the 11‡-point gain needs the gpt-4-0613 extractor.
- **ALFWorld by task type (Table 5; per-type counts are not given).** ExpeL is 74 on "clean" vs. 87 for insights-only, 67 on "cool" vs. 71 for ReAct, and 43 on "heat" vs. 74 for imitation learning. Against ReAct the gain is large on four of six types (put 83 vs. 50, heat 43 vs. 13, look 39 vs. 0, puttwo 29 vs. 0) and small or negative on clean (74 vs. 61) and cool (67 vs. 71).
- **Wording.** The Figure 5 caption says ExpeL "consistently outperforms the baselines on all domains" and names ReAct and Act as the baselines; this holds for them (and for imitation learning: ALFWorld 37, WebShop 29), while the Reflexion lines lie outside the caption's baseline set. The paper says "four-fold validation" but describes training on one half and testing on the other half and vice versa.
- **Emergent behaviours (§5.3)** are hand-inspected examples with "likely" / "possibly" causal wording; there is no count of how often they occur.
- **Limits stated by the authors.** Text-only observations, closed-source API models, an insight list that fits in the context window.

## Our read

HarnessRSI score **72**, band ★★★, evidence level **retained**: the kept insights and trajectories help on unseen tasks of the same benchmarks. The paper reports held-out tasks, multi-fold means with standard errors, an ablation of the retained components, and one cross-task transfer (HotpotQA to FEVER). It does not report matched-compute baselines, the cost of building the insight list, or a leakage check, and it does not vary the improvement mechanism against alternative improvers, so the evidence stops at the retained level. On the pattern's conditions, our judgment marks the framing as resting on "without gradient updates" rather than on a more specific fixed assumption (S1 no, F1 yes); contrastive pairs, explicit add/edit/vote maintenance and the count-zero removal rule are marked as present.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
