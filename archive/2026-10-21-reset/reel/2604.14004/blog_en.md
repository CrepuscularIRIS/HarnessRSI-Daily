# Memory Transfer Learning: borrowing memories from other coding benchmarks helps a little, unevenly

*A Reel interpretation of [arXiv 2604.14004v1](https://arxiv.org/abs/2604.14004v1) (Kangsan Kim, Minki Kang, Taeil Kim, Yanlai Yang, Mengye Ren, Sung Ju Hwang; KAIST, NYU, DeepAuto.ai). HarnessRSI Daily score 67, ★★. Code: [KangsanKim07/MemoryTransferLearning](https://github.com/KangsanKim07/MemoryTransferLearning).*

## What the system changes about itself, and the keep rule

This is not an evolution loop. A coding agent's own earlier attempts become **memory items**, and a later run on a *different* benchmark reads a few of them. Nothing is trained and nothing is gated: the paper describes no keep/reject rule and no validation of memory items.

1. Run the agent on all six benchmarks. An LLM judge labels each attempt as success or failure (the paper does not report the judge's accuracy).
2. Turn the attempts into memories in one of four formats (our reading: one memory item per attempt; the paper says only "memories for each task"): **Trajectory** (commands and outputs), **Workflow** (goal plus reusable commands), **Summary** (task plus a one-paragraph experience summary), **Insight** (title, description and content, written without file names).
3. For a test benchmark, the pool contains memories from all *other* benchmarks, built for the same model and format.
4. At test time the three most similar memories (cosine similarity of text-embedding-3-small vectors) go into the system prompt. For Workflow, Summary and Insight the query is a 4-5 sentence plan the model writes first; for Trajectory the query is the task text.

For the GPT-5-mini rows, memory generation, the agent and the judge are all GPT-5-mini (the paper adopts it "for every LLM usage"), run with mini-swe-agent; the DeepSeek V3.2 and Qwen3-Coder rows use a pool built for the testing model, and the paper does not say which model judged or generated those memories. Each benchmark is capped at 100 randomly sampled tasks, and the score is Pass@3 (Section 4.1.2 says "each model is evaluated over three runs" in the Table 2 context; the paper does not define Pass@3, so applying three runs to every table is our reading).

## What is shared and what is reset between source and target

Shared: the base model (each model uses a pool built by itself), the agent scaffold, the evaluation platform, the embedding model and the judge. Reset: the target benchmark's own memories are excluded. The paper uses "zero-shot" only as the name of its no-memory baseline; it does not describe the transfer itself as zero-shot. There is no fine-tuning, but the memories come from runs of the same model, scaffold and judge on the other benchmarks. The source runs are full agent attempts on the other benchmarks (our reading: the same sampled tasks that are evaluated there). The paper reports no cost for building the pool, and it does not separate near domains from far ones (for example LiveCodeBench and Aider-Polyglot are both function-level). Two of its own numbers do not pin the pool down: Table 2 says the MTL pool has 431 memories, which matches neither 391‡ nor 401‡ (the source-pool sizes our task-count reading implies), and Figure 6's "9 domains" point sits at the same value as the full pool although only six benchmarks are evaluated. So the pool composition is our reading throughout.

## Headline, as reported

GPT-5-mini, Pass@3, Table 1. Insight memories raise the average from 0.523 to 0.560 (+3.7 points). Insight is the best of the four formats on these same test tasks (averages 0.534, 0.538, 0.546, 0.560); the paper reports no separate dev split, and the two other models were run with Insight only, so the format was chosen from the GPT-5-mini test results. The paper reports the same direction for two open models, only with Insight memories: DeepSeek V3.2 0.542 to 0.568 (+2.6) and Qwen3-Coder-480B 0.483 to 0.501 (+1.8).

| GPT-5-mini, Pass@3 | Zero-shot | MTL (Insight) |
|---|---|---|
| LiveCodeBench v6 | 0.910 | 0.930 |
| Aider-Polyglot | 0.470 | 0.470 |
| SWE-Bench Verified | 0.730 | 0.770 |
| Terminal Bench 2 | 0.315 | 0.360 |
| ReplicationBench | 0.111 | 0.189 |
| MLGym-Bench | 0.667 | 0.750 |
| Avg. | 0.523 | 0.560 |

The Avg. column is not the mean of the six columns (that would be 0.534‡ to 0.578‡). Our reading: it matches a task-pooled average, which is consistent with about 100/100/100/89/90/12 tasks (the paper states no benchmark sizes, only that benchmarks with more than 100 tasks are sampled down to 100). On that reading the +3.7 points are about 18‡ extra solved tasks out of 491‡.

## The paper's own controls

- **Four formats (Table 1, GPT-5-mini).** Average 0.534 (Trajectory), 0.538 (Workflow), 0.546 (Summary), 0.560 (Insight), against 0.523 zero-shot. The ordering matches the paper's claim that "more abstract and generalized memory representations tend to yield higher transfer effectiveness", but there is no variance, and the formats also differ in how they are retrieved (task text vs a model-written plan; our reading). Per benchmark, the statement that "all MTL variants outperform the zero-shot baseline" holds only for the average: Trajectory is below zero-shot on Terminal Bench 2 (0.270 vs 0.315) and MLGym (0.583 vs 0.667), Workflow on MLGym (0.583), Summary on Aider-Polyglot (0.460 vs 0.470).
- **Abstraction isolated (Table 4).** Within the Insight format, the 30% of memories judged most task-agnostic gave an average of 0.534 against 0.523 for the 30% most task-specific (+1.1). The table does not name the model or metric (our reading: GPT-5-mini, averaged Pass@1), covers three benchmarks, and gives no variance; ReplicationBench contributes 0.082 vs 0.067.
- **Against memory baselines (Table 2, three benchmarks, Pass@3; the model is not named in the table).** MTL 0.630, AgentKB 0.613 (5,899 memories), ReasoningBank 0.601 (97 memories), zero-shot 0.584. MTL uses 431 memories. The three draw from different pools, so this compares memory sources rather than one mechanism granted to all: ReasoningBank uses "a small number of in-domain memories", AgentKB "out-of-domain memories (from general reasoning tasks)". The paper's gaps are +2.9 and +1.7. AgentKB is above MTL on ReplicationBench (0.200 vs 0.189, about one task of 90‡) and its SWE-Bench 0.720 is below zero-shot 0.730; the +1.7 rests on SWE-Bench (0.770 vs 0.720, about five tasks of 100‡) and LiveCodeBench. How the baselines were set up or tuned, and their variance, are not described.
- **Retrieval variants (Table 7).** Letting the LLM rerank 20 candidates (0.598) or rewrite the retrieved memories (0.608) did not beat plain embedding similarity (0.630).
- **Across models (Table 6, Pass@1, three benchmarks).** On average, another model's memories beat zero-shot for all three targets, but the margins hide per-benchmark losses. With GPT-5-mini as target, zero-shot is 0.515; Qwen3-Coder's memories give 0.528, DeepSeek V3.2's 0.518 — essentially at zero-shot, with SWE-Bench (0.617 vs 0.623) and ReplicationBench (0.048 vs 0.059) below it — and its own memories 0.543. For the Qwen3-Coder target the whole gain over 0.402 comes from LiveCodeBench (0.780 vs 0.733; SWE-Bench 0.347 equals zero-shot 0.347, ReplicationBench 0.111 is below 0.126), and GPT-5-mini's memories tie its own at the printed precision (0.413), although the text says cross-model transfer "consistently underperforms" self-generated memory. For the DeepSeek V3.2 target, GPT-5-mini's memories give 0.501 against zero-shot 0.486 and its own 0.511.
- **Why it helps (Figure 3).** GPT-5 sorted the instances that failed zero-shot but passed with Insight memories into 10 categories. Algorithmic strategy transfer is 5.5% of the gains; the rest are procedural (workflow discipline, test-driven verification, environment adaptation and so on). The paper does not give the number of instances, and it mentions only "manual case studies" alongside the LLM inspection, without saying the GPT-5 labels were human-checked. Figure 3 covers only the gains; the reverse flips (zero-shot succeeds, memory fails) are described qualitatively in Section 4.4.1 without counts.

## Where the gain is absent or small

- **Concentrated in a few tasks and benchmarks.** For GPT-5-mini the gain is 0.0 on Aider-Polyglot and +2.0 on LiveCodeBench. The largest gains are on ReplicationBench (+7.8) and MLGym (+8.3). On our task-count reading MLGym's +8.3 is a single task out of 12‡, and ReplicationBench's is about 7‡ of the 18‡ net tasks, from a baseline that solves 0.111.
- **Pass@3 vs Pass@1.** Appendix A reports averages of 0.435 (zero-shot) and 0.454 (Insight) for GPT-5-mini, a gain of +1.9, about half the Pass@3 figure. For Qwen3-Coder it is +1.2 and for DeepSeek V3.2 +2.0. The paper gives no SD or CI for any number.
- **Other models.** For DeepSeek V3.2 Aider-Polyglot falls (0.590 to 0.580); for Qwen3-Coder ReplicationBench and MLGym do not move (0.211, 0.583). Only Insight memories were run for these two models.
- **Scaling claims.** The average gain at the full pool (+2.8‡ points in Pass@1; Table 6: 0.543 − 0.515) is driven by ReplicationBench (0.059 to 0.119); LiveCodeBench 0.863 to 0.877 and SWE-Bench 0.623 to 0.633 move little. In Figure 6 the per-benchmark curves are not monotone (SWE-Bench dips below zero-shot at the half-size pool; read off the figure). The text says that "9 domains" gives the best result, but the paper evaluates six benchmarks and excludes the target from the pool, and does not explain the nine.
- **Negative transfer is real but uncounted.** Table 9 and Section 4.4.1 describe failures (a pattern from R code applied to a C++ task; a validation insight read as licence for a shortcut) without counts.
- **No limitations section** (the paper has an Impact Statement that mentions negative transfer).

## Our read

HarnessRSI score **67**, band ★★, evidence level **retained**: the retained artifact (memory) helps on a benchmark that its pool was not built from, and the memory formats, which differ in abstraction, are compared against each other. The paper reports: a leave-one-benchmark-out pool, three models, a four-format comparison, an abstraction ablation, two memory baselines, retrieval variants and cross-model transfer. It does not report: variance or confidence intervals of any kind, a zero-shot re-run to give a noise floor, the cost of building or using the pool, baseline tuning, a leakage or overlap check between source and target benchmarks, the accuracy of the success/failure judge, a same-domain memory control with the same pipeline, or a random/irrelevant-memory or generic-hint control — notable because the paper's own mechanism claim is that the gains are generic procedural advice. Gains are mostly a few points on small benchmarks, so we read the direction as plausible and the size as uncertain.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
