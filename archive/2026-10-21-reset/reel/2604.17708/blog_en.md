# EvoOR-Agent: an operations-research agent that evolves its own workflow graph — and where the gain stops

*A Reel interpretation of [arXiv 2604.17708v2](https://arxiv.org/abs/2604.17708v2) (HarnessRSI Daily score 81, ★★★). The paper links an anonymous code repository; no public repository is listed.*

## What the system changes about itself

EvoOR-Agent keeps the LLM frozen and evolves the **organization of the agent**. An OR agent (problem analysis → mathematical modeling → solver-code generation and repair) is written as executable code and abstracted into an *activity-on-edge (AOE)* chain: reasoning states as nodes, typed transitions (workflow, reasoning, tool call) as edges. Two things evolve together:

- a **population of 10 reasoning individuals**, each one a complete executable workflow;
- a global **architecture graph** that merges the chains of all individuals, so a new individual can be built by walking a path through fragments that different individuals discovered.

A **knowledge base** built by an LLM agent from OR papers and code repositories (with a sanitization step meant to strip benchmark instances) seeds half of the initial individuals and guides part of the mutations.

## Signal and keep/reject rule

1. Fitness is weighted accuracy on a 120-instance training split drawn from five benchmarks: the solver output must match the ground-truth objective within a relative error of 10⁻³.
2. Each generation (8 in total) keeps the top 20% (elite), adds 50% semantic mutations (one phase or the whole workflow, with or without the knowledge base) and fills the rest by path-conditioned recombination on the graph.
3. Edge weights move toward the fitness of the individuals that traverse them (learning rate 0.5); a sparsity weight favours rarely used edges; nodes and edges below a threshold of 0.1 for several consecutive iterations are pruned.
4. The individual with the highest training accuracy is evaluated on held-out test instances. Two benchmarks, NLP4LP and ReSocratic, are never used during evolution.

## Headline result, as reported

Table III evaluates seven OR benchmarks (six of them cleaned by the authors) with four LLMs; its caption reports mean ± SD over ten independent runs "where available" (the fine-tuned ORLM and StepORLM were decoded greedily). Same model (DeepSeek-v3.2) in every row of the table below:

| Benchmark | EvoOR-Agent | OR-LLM-Agent (fixed pipeline) | EvoAgent | EvoPrompt | Zero-shot |
|---|---|---|---|---|---|
| IndustryOR | 81.55% | 69.04% | 72.82% | 64.91% | 48.72% |
| ComplexLP | 81.98% | 75.67% | 69.81% | 68.28% | 63.75% |
| BWOR | 84.15% | 76.83% | 74.95% | 66.83% | 45.12% |
| NLP4LP (not evolved on) | 93.28% | 88.21% | 85.62% | 84.92% | 76.78% |
| ReSocratic (not evolved on) | 92.55% | 87.44% | 86.79% | 82.95% | 75.92% |

The authors state that the method is best on six of the seven benchmarks, counting the best of its four LLM rows against all baselines. The table above leaves out the EasyLP and NL4OPT columns, where the fine-tuned StepORLM is at or above EvoOR-Agent (see below).

## The controls that decide whether the gain is real

- **Search budget (nominal match).** All three evolutionary methods (EvoPrompt, EvoAgent, EvoOR-Agent) use a 400,000-token cap as the termination criterion rather than a fixed number of generations; EvoOR-Agent actually spends about 410.7K (Fig. 5), and the budgets actually reached by the re-implemented EvoPrompt and EvoAgent are not reported. The train/test split is shared across methods. The fixed OR-LLM-Agent pipeline and the fine-tuned models are not evolved.
- **Ablation (Table V, DeepSeek-v3.2, mean of ten runs).** Weighted accuracy over the five evolved benchmarks rises 62.9% (plain LLM) → 67.4% (+ chain-of-thought) → 75.8% (+ text-level evolutionary search) → 84.1% (+ AOE architecture graph, no knowledge base) → 87.0% (full). The paper calls the AOE step the largest component-level gain; on the headline weighted accuracy it is about the same size as the text-level evolution step before it (75.8% → 84.1% vs. 67.4% → 75.8%), and the ablation is cumulative, so the split depends on the order. The knowledge base adds the smallest step. Without the knowledge base, the +AOE variant is already above every same-model (DeepSeek-v3.2) prompt/agent baseline in Table III on all seven benchmarks (for example IndustryOR 76.10% vs. 72.82%, BWOR 80.72% vs. 76.83%) — but not above the fine-tuned StepORLM on EasyLP (91.08% vs. 97.06%), NL4OPT (91.36% vs. 93.89%), NLP4LP (94.62% vs. 96.06%) or ComplexLP (78.62% vs. 80.18%).
- **Out-of-distribution.** On the two benchmarks excluded from evolution, EvoOR-Agent reaches 93.28% (NLP4LP) and 92.55% (ReSocratic) with DeepSeek-v3.2, and 97.75% on NLP4LP with GPT-5. The knowledge base lowers NLP4LP: 94.62% for +AOE versus 93.28% for the full system (the paper notes this).
- **Is Table III held-out only?** The paper says test instances are not used for fitness, graph updates or model selection. But the population size (10, §V-C) and the generation count (8, §V-D, "the highest Test WA") are read off curves on the test split, with the same DeepSeek-v3.2 setting that then produces Table III; the Table III cells on the evolved benchmarks (e.g. IndustryOR 81.55%, ComplexLP 81.98%) differ slightly from the generation-8 test values in Fig. 5 (81.0%, 82.1%), and the paper does not say whether Table III uses the test split alone. Treat the knee and the generation count as tuned on that split, not as independent findings.
- **Search cost.** Population 10 is where the curve flattens: moving from 6 to 10 raises test weighted accuracy from 81.2% to 86.8%; moving from 10 to 20 adds 86.8% → 87.4% while the token cost grows from 410.7K to 812.3K (chosen using the test curve, see above).
- **Inference cost.** The column is "average token consumption per problem": 5,023–5,334 for EvoOR-Agent against 4,673–5,023 for EvoAgent, 3,821–4,096 for OR-LLM-Agent, 3,394–3,512 for EvoPrompt and 1,586–1,714 for zero-shot prompting. The paper does not say whether the one-off evolution budget is included.

## Where the gain is absent or small

- **A fine-tuned 8B model wins several columns.** StepORLM scores 97.06% on EasyLP, above EvoOR-Agent's best of 94.19% (GPT-5). On NLP4LP it scores 96.06% against 93.28% for EvoOR-Agent with DeepSeek-v3.2; only the GPT-5 row (97.75%) is higher. On ComplexLP it scores 80.18%, above the GPT-5 (75.53%), Gemini 3 Flash (74.89%) and Qwen 3Max (68.82%) rows. On NL4OPT it scores 93.89% against 94.03% for DeepSeek-v3.2 (a gap within the reported SD) and above the other three LLM rows (90.76%, 92.59%, 86.72%).
- **Not every model.** Across the 4 LLMs × 7 benchmarks, EvoOR-Agent is ahead of the best same-model baseline in 27 of 28 cells‡. The exception is Gemini 3 Flash on ComplexLP (74.89% vs. 75.93% for OR-LLM-Agent). Some wins are small relative to the reported standard deviations, for example Qwen 3Max on ComplexLP (68.82% vs. 68.03%).
- **Small benchmarks.** After cleaning, IndustryOR has 42 instances, BWOR 82 and ComplexLP 111 (Table I gives whole-benchmark sizes; per-benchmark test sizes are not reported). The 120 training instances are sampled from the pooled five evolved benchmarks. The text says these hold 983 instances (120 train + 863 test), but the per-benchmark counts in Table I add up to 993‡; the cleaned counts add up to 1,574‡, not the stated total of 1,564.
- **Overfitting after generation 8.** Test weighted accuracy falls from 86.8% to 86.3% by generation 15 while training accuracy keeps rising from 87.4% to 88.7%.
- **Open points on controls.** The ablation reports no standard deviations, has no variant that isolates graph weight updates and pruning, and has no knowledge-base-only variant. The paper does not say whether the baselines receive the knowledge base. The knowledge base's worked example (Supplement Listing S3) is a sanitized entry derived from OR-LLM-Agent — the fixed-pipeline baseline — and the LLM sanitization prompt names only NL4Opt, Mamo, IndustryOR and BWOR as contamination sources, not NLP4LP or ReSocratic (the out-of-distribution benchmarks). The sanitization is described but not empirically audited for leakage.

## Our read

HarnessRSI score **81**, band ★★★, evidence level **retained**: the evolved agent is shown to help on held-out and out-of-distribution data. The paper reports a train/test split, two never-evolved benchmarks, ten-run means with standard deviations, a nominally shared token cap for the evolutionary baselines, inference token cost and a component ablation. The test split is also used to read off the population size and generation count. It does not compare variants of the improver itself (graph update and pruning on or off), does not test the knowledge base for leakage, and has no public code.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
