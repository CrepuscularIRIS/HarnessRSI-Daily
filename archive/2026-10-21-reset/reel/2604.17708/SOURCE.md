# SOURCE — Co-evolving Agent Architectures and Interpretable Reasoning for Automated Optimization (EvoOR-Agent)

Read from: arXiv 2604.17708v2
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and text boxes on the poster were drawn by us from the paper's numbers. Read: main text (pp1–15) and the supplement bundled in the same PDF (pp16–36).

## Where the numbers come from
- Table III (comparison, per-problem tokens), Table V (ablation, §V-B), Table II (hyperparameters), Table I and Supplement Table S-IV (benchmark sizes), §IV-A (split sizes, 400,000-token budget), §V-C/§V-D (population-size and convergence analyses), Supplement S-II.C.3 (baseline re-implementation, 400,000-token cap, ORLM / StepORLM 8B models), Supplement S-III (knowledge-base sanitization).

## ‡ numbers (computed by us)
- "27 of 28 cells‡": for each of 4 LLMs × 7 benchmarks in Table III we compared EvoOR-Agent with the best of EvoPrompt, OR-LLM-Agent and EvoAgent for the same LLM; EvoOR-Agent is ahead in 27 cells, behind in one (Gemini 3 Flash, ComplexLP: 74.89 vs 75.93).
- "1,574‡": sum of the cleaned per-benchmark counts in Table I (213 + 545 + 111 + 178 + 42 + 403 + 82); the paper states a total of 1,564.
- "993‡": sum of the five evolutionary benchmarks in Table I (213 + 545 + 111 + 42 + 82); the text (§IV-A) says 983 (120 train + 863 test).

## Notes
- "+AOE (no knowledge base) is above every same-LLM (DeepSeek-v3.2) prompt/agent baseline on all seven benchmarks" compares Table V (+AOE row) with the DeepSeek-v3.2 rows of EvoPrompt, OR-LLM-Agent and EvoAgent in Table III; it is NOT above the fine-tuned StepORLM on EasyLP, NL4OPT, NLP4LP and ComplexLP. The paper does not state that the ablation used the same budget.
- Ablation steps: the paper calls the AOE step "the largest component-level gain"; on weighted accuracy the +EC step (67.4 → 75.8) and the +AOE step (75.8 → 84.1) are about equal, and the ablation is cumulative, so we say "about as much as".
- Population size 10 and generation 8 are chosen from test-split curves (§V-C, §V-D); the paper does not say whether Table III uses the test split alone, and Table III evolved-benchmark values differ slightly from the generation-8 test values in Fig. 5/6. We state this as an open point.
- Table I sizes are whole-benchmark sizes, not test sizes; per-benchmark test sizes are not reported.
- Table III caption: "mean and standard deviation over ten independent runs where available"; ORLM / StepORLM used greedy decoding (Supplement S-II.C.4). Six of the seven benchmarks were cleaned by the authors.
- Inference tokens ("average token consumption per problem"): the paper does not say whether the evolution budget is included. Ranges over the four LLM rows: zero-shot 1,586–1,714; EvoPrompt 3,394–3,512; OR-LLM-Agent 3,821–4,096; EvoAgent 4,673–5,023; EvoOR-Agent 5,023–5,334.
- Budget: 400K-token cap is a termination criterion per model generation; EvoOR-Agent spends about 410.7K (Fig. 5); budgets actually reached by the re-implemented EvoPrompt / EvoAgent are not reported; train/test split is shared across methods.
- Knowledge base: the supplement's worked example (Listing S3) is a sanitized OR-LLM-Agent entry; the sanitization prompt (Prompt Box S11) names NL4Opt, Mamo, IndustryOR and BWOR, not NLP4LP or ReSocratic; no empirical leakage audit.
- "Best same-model baseline" bars on the poster: EvoAgent on IndustryOR (72.82), OR-LLM-Agent on the other six columns (DeepSeek-v3.2 rows).
- The paper's own text compares "81.55 vs 71.51" on IndustryOR, which mixes the DeepSeek-v3.2 EvoOR-Agent row with the GPT-5 OR-LLM-Agent row; we used same-model numbers.
- The paper links an anonymous repository (anonymous.4open.science); no public code, so the poster carries only the paper QR.
- Standard deviations in Table III are roughly one to two points; Table V reports means only.

## Judgment notes
None. The full paper is consistent with our judgment (batch b21): `budget_matched: yes` (400,000-token cap for all evolutionary methods), `improver_comparison: unclear` (no variants of the improver such as graph update / pruning on-off are compared), `leakage_guard: untested` (sanitization protocol described in Supplement S-III, not tested).
