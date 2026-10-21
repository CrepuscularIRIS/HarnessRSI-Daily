# ExpSeek: ask for experience when entropy rises—not only before the task

*A Reel interpretation of **ExpSeek: Self-Triggered Experience Seeking for Web Agents**, [arXiv 2601.08605v2](https://arxiv.org/abs/2601.08605v2). HarnessRSI score **63**, band ★★, evidence level **retained**. Code: [WYRipple/ExpSeek](https://github.com/WYRipple/ExpSeek).*

## What the system changes about itself

ExpSeek builds a reusable **experience repository**, then changes the agent's context at selected reasoning steps. It does not train the agent's weights or describe an online optimizer that rewrites itself after each evaluation task.

Offline, Qwen3-8B or Qwen3-32B samples five trajectories per training question. A Qwen3-235B-A22B-Instruct-2507 tool model contrasts successful and failed trajectories, sees the training answer, labels step correctness, and extracts **Behavior / Mistake / Guidance** triplets for erroneous steps. Topics can be reused, modified or created during construction; process-step and answer-step experiences are stored separately. There is no reported validation-score acceptance/rollback gate for these triplets.

## The trigger, and what gets kept

The trigger is the **mean token entropy of the agent's response distribution**, not a self-written confidence score. Separate logistic regressions relate entropy to the tool model's correctness labels on training trajectories. Bootstrap resampling produces an interval of decision boundaries for each step type. Below the lower boundary: no guidance; above the upper boundary: guidance; between them: an intervention probability that rises linearly. A step immediately following intervention cannot trigger again.

When triggered, the experience model reads the current interaction history, selects the three most relevant topics and generates tailored guidance from their triplets. For a process step, guidance is appended to the tool observation. For an answer step, it becomes a new observation, allowing the agent to revise the answer or resume tool use. The guidance stays in the **current history**; the method does not describe writing newly sought test-time guidance or test trajectories back into the persistent repository. That repository and the fitted thresholds are the retained artifacts, not a growing test-time memory. The inference prompt forbids direct answers and clues, but that instruction is not a leakage audit.

## Headline result, as reported

Table 2 reports **mean accuracy over five independent runs**, not a best run. Its Avg. column rises from **32.23 to 41.50** on Qwen3-8B and **37.79 to 45.32** on Qwen3-32B: the paper's rounded **9.3 and 7.5 percentage-point** improvements. The strongest experience baseline in that Avg. column, ReasoningBank+, scores 34.80 and 39.33.

| Benchmark | 8B: no experience → ExpSeek | 32B: no experience → ExpSeek |
|---|---:|---:|
| WebWalkerQA Avg. | 38.47 → 48.25 | 45.01 → 51.09 |
| GAIA | 29.13 → 36.89 | 36.50 → 43.88 |
| SEAL-HARD | 23.23 → 30.16 | 27.80 → 32.76 |
| xbench-DeepSearch | 25.60 → 37.20 | 27.40 → 42.00 |

**Aggregation caveat:** our reading of Table 2 is that Avg. equally weights WebWalkerQA Easy, Medium and Hard separately, plus GAIA, SEAL and xbench (six‡ columns), rather than averaging the four benchmark averages. The improvements are not confined to one benchmark, but the largest reported increase is on **32B xbench, 14.6 points**, whereas 32B WebWalkerQA Hard gains 4.8.

Agents use non-thinking mode, temperature 1.0, top-p 0.95, Search and Visit tools, and a 30-step cap; exceeding it counts as failure. The main experience model is **235B**. The same model family also supplies experience construction, judging and Visit summarization. These results are therefore not an isolated small-model-only system. Table 2 gives no SD, SE or confidence intervals, no run seed list, and no statement that repositories were rebuilt independently per run. The split's seed 0 must not be mistaken for the evaluation-run seeds.

**Evaluation-rule caveat:** accuracy uses Qwen3-235B-A22B-Instruct-2507 as an LLM judge (Appendix C, PDF p17). Its prompt accepts predictions containing the labeled answer, even with additional explanation (Table 19, PDF p29). No independent-judge or human grading validation is reported. These are model-judged scores under that rubric; this does not establish that the comparison is biased.

## The controls that decide whether the gain is real

- **Process versus answer guidance (Table 2).** Full / process-only / answer-only Avg.: **41.50 / 36.59 / 39.06** for 8B; **45.32 / 40.81 / 41.20** for 32B. Both stages help the aggregate. These rows share Table 2's five-run-mean description, but no variance is reported.
- **Comparable guidance access (Table 3).** Rule-based and Claude-sonnet-4-20250514 triggers both receive the generative experience model and the same one-step cooldown. On 8B GAIA, entropy achieves **36.89**, below Rule's **38.81** and Claude's **39.47**, but costs **127.57 s** per question versus **329.71 s** and **370.82 s**. On xbench it scores **37.20**, against **36.40** and **36.60**. Thus entropy is an efficiency–accuracy choice, not the highest-accuracy trigger everywhere. Table 3 does not independently specify its run count or give uncertainty.
- **Retrieval versus generation (Table 3).** Keeping entropy triggering but directly using the nearest triplet via text-embedding-v4 scores **30.92** on GAIA and **27.80** on xbench, versus **36.89** and **37.20** with generated guidance. This is a stronger retrieval control than simply comparing with no experience.
- **Headline baseline access is different (§5.1).** Training-Free GRPO iteratively derives experience from offline trajectories using semantic advantages, then supplies it globally. ReasoningBank+ accumulates online experience and retrieves it into the system prompt; its experience generator is explicitly upgraded to **235B**. The paper does not establish that these two baselines receive ExpSeek's identical triplets or its step-level generative mentor. Their exact data/reset protocol is not fully specified. Do not extend this access limitation to the Table 3 trigger controls, which do get the mentor.
- **Repository contribution and transfer (§6.3, Figure 7, Table 4).** Removing the repository lowers performance, but the mentor without it still helps; the full gain cannot all be attributed to stored experience. Swapping repositories across agent sizes retains gains over no experience but underperforms each agent's own repository: 32B GAIA **43.88 → 40.33**, xbench **42.00 → 37.20**; 8B GAIA **36.89 → 35.60**, xbench **37.20 → 36.00**. This swaps repositories, not a demonstrated transfer of the whole calibrated trigger.

## Splits, tuning and leakage

The repository and entropy thresholds come entirely from **170 WebWalkerQA training questions**, sampled with seed 0 from 25% of each difficulty level; the remainder is the WebWalkerQA test set. GAIA, SEAL-HARD and xbench evaluate cross-benchmark reuse of those experiences. Seeking reads the current test context, but no evaluation gold answer is supplied in the inference prompts.

That explicit train/test separation is useful, but random question splitting does not establish that related questions or source pages are disjoint. The paper reports no near-duplicate/cross-benchmark contamination audit. It also does not fully specify ReasoningBank+'s online memory resets, so evaluation-task exposure for that baseline cannot be reconstructed from the paper alone.

Thresholds are fitted on the training labels, with 1000 bootstrap samples and scikit-learn LogisticRegression defaults. A separate split for choosing the top-three-topic rule, cooldown or other defaults is not identified; the threshold/interval sensitivity sweep is performed on **8B GAIA**, and the paper does not say a held-out tuning split chose the default. Missing numerical baseline settings include Training-Free GRPO's iteration count/group size and ReasoningBank+'s retrieval count/memory cap; baseline tuning/search budgets are not reported. This is different from saying the threshold-fitting split is missing—it is not.

## Where the gain is absent or small—and what seeking costs

- **Little extra benefit on SEAL from process guidance.** Full versus answer-only: **30.16 versus 30.08** for 8B, **32.76 versus 32.52** for 32B. On 32B WebWalkerQA Hard, full **45.89** is close to process-only **45.56**. Without uncertainty, these are small differences, not established reliable wins.
- **Entropy loses the GAIA accuracy comparison** against the more expensive Rule and Claude triggers above. ExpSeek leads the headline baselines in Table 2, not every variant in the paper.
- **Extra interactions are real (Table 3, 8B only).** GAIA goes from **4.47 steps / 66.94 s** without experience to **5.75 / 127.57 s**; xbench from **3.31 / 51.06 s** to **5.73 / 143.81 s**. The common step cap does not match actual compute. No matched-token or matched-wall-clock headline baseline, token/dollar accounting, or full offline trajectory-and-triplet construction cost is reported. Threshold regression alone takes seconds per step type; that is not the total preparation cost.

## Our read

**63 · ★★ · retained**, following the latest matching judgment (b16). The paper reports held-out evaluation, cross-benchmark and cross-model repository reuse, guidance/retrieval ablations and five-run means. It does **not** report run variance, matched-compute headline comparisons, a contamination audit or complete construction cost. The judgment's `optimizer_cost: unclear` should not obscure the online steps/time in Table 3; those measure deployment overhead, not the full offline cost.

The defensible takeaway is **reusing error-guidance triplets through a conditional mentor improves web reasoning, with a measurable inference-time bill**. It is not evidence that a self-improvement algorithm itself gets better, nor that entropy always maximizes accuracy.

*‡ marks our aggregation reading/count, checked against Table 2 arithmetic; see SOURCE.md. No paper figures are reproduced.*
