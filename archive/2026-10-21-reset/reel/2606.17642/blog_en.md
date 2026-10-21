# FinAcumen: a frozen 8B vision-language model gets a memory bank of strategies and warnings — but where the paper splits it out, tools give about twice the memory gain

*A Reel interpretation of [arXiv 2606.17642v6](https://arxiv.org/abs/2606.17642v6) (HarnessRSI Daily score 68, ★★). Authors: Pianran Guo, Pengcheng Zhou, Yuchen Jian, Shuhua Chen, Zhongliang Yang, Linna Zhou (Beijing University of Posts and Telecommunications; Queen Mary University of London). Code: [CamelliaLilium/FinAcumen](https://github.com/CamelliaLilium/FinAcumen).*

## What the system changes about itself

FinAcumen leaves the model weights and the tool suite alone. The backbone is a frozen Qwen3-VL-8B-Instruct (temperature 0), the four tools are fixed (a stateful Python executor, a lookup over price/news/indicator tables, an OCR-based chart/table decoder, and an answer gate that checks source traceability, units and format). What accumulates is a **memory bank** of text entries. Each entry holds a training question, its gold answer, and distilled experience in two parts: **Findings** (strategies generalised from trajectories that reached the correct answer) and **Cautions** (guard rules extracted from trajectories that did not).

## The signal, and the keep/reject rule

1. **Build (offline).** For each training/validation item the model samples K = 8 independent trajectories; each is scored against the gold answer; a single summary agent writes the Findings and Cautions. The paper describes a new entry being written for each problem ("incrementally expanding the bank"); we found no write-time filter or pruning step described in the paper or appendix.
2. **Freeze.** The bank (about 2,400 entries in Sections 5.1/5.4; Appendix K says "approximately 1800-entry") is read-only at test time, so no test item writes to it.
3. **Retrieve (per query).** Embed the question plus the first 600 characters of context, keep entries with cosine similarity ≥ τ = 0.65, de-duplicate by source, take at most k_max = 5. An annotator agent rewrites them into directives for the current problem, then the solver runs a ReAct loop (≤ 16 steps) with the tools.
4. **Fallback.** If no entry reaches τ, the solver runs with the tools alone. (Besides the cosine threshold there are two softer gates in the prompts: the annotator may mark an entry not useful ("If you cannot map entities, the entry is NOT useful", though it is told to do so only when the task type is fundamentally different), and the solver may skip entries that do not fit. The paper reports none of these separately.)

The retrieved entries shown to the solver include the gold answer of the retrieved training question (described as a "format reference").

## Headline result, as reported

Table 1 reports accuracy on six settings from four financial benchmarks. FinAcumen and Base use the same frozen Qwen3-VL-8B-Instruct; Base has neither memory nor tools. Table 1 values equal the five-run means of Table 9.

| Setting | Base | FinAcumen (5-run mean ± SD) | Best published general LLM |
|---|---|---|---|
| BizBench SEC-NUM | 27.67 | 68.65 ± 2.45 | 79.30 (GPT) |
| FinMMR Easy | 59.17 | 81.67 ± 1.14 | 78.00 (GPT) |
| FinMMR Medium | 45.75 | 67.00 ± 0.71 | 63.42 (Qwen2.5-VL-72B) |
| FinMMR Hard | 31.40 | 46.10 ± 2.86 | 50.80 (Claude Sonnet) |
| FinTMMBench | 16.20 | 19.98 ± 0.89 | 21.53 (GPT) |
| FinMME Avg | 27.84 | 51.08 ± 2.24 | 52.54 (Qwen2.5-VL-72B) |

The general-LLM numbers are published results copied from the benchmark papers, not re-run, and the model variant differs by cell (Table 8: for example GPT-4 on BizBench, GPT-4o on FinMMR, GPT-4o-mini on FinTMMBench; Claude 3.7 Sonnet; Llama 4 Maverick 17B). The paper itself says the controlled comparison is Base versus FinAcumen. FinAcumen is above the three finance-specialised models in every shared column (Llama-Open-Finance-8B, FinLLaVA, Fin-R1), and above the published GPT entries on FinMMR Easy and Medium.

## The controls that decide whether the gain is real

- **Tools versus memory (the key split).** On FinMMR Easy (Table 2): Base 59.17, plus tools 74.08 (+14.91), plus tools and memory 81.67; memory adds 7.59 over tools alone. On BizBench the bank-size curve (Figure 2) starts at 55.15 with the tools and an empty bank and reaches 68.65 at 2400 entries, +13.5; against Base 27.67 the tools alone are therefore worth 27.48‡. With Qwen3-VL-235B-A22B on BizBench (Table 12): Base 57.45, tools 69.30 (+11.85), full 75.10 (memory +5.80). In all three decompositions the tool gain is about twice the memory gain. The paper gives this split only for these three settings; the other four (FinMMR Medium and Hard, FinTMMBench, FinMME) have none in the main results.
- **Run-to-run variation (Table 9).** Five independent runs of Base and FinAcumen with mean, SD and a 95% CI; the intervals are separated in every setting. The paper does not say what differs between runs (for example whether the bank was rebuilt). The published baselines are single numbers without variance.
- **Other memory methods given the same tools and data (Appendix I, Table 10).** Reflexion, ExpeL and FinAcumen on the same backbone, with the same tool environment and training data and frozen banks: FinMMR Easy 77.17 / 77.17 (an exact tie) / 81.67; FinMMR Medium 63.58 / 60.58 / 67.00; FinTMMBench 14.52 / 16.73 / 19.98; FinMME 42.97 / 45.77 / 51.08. Four settings only (not BizBench, not FinMMR Hard), single numbers with no SD, and the baselines' tuning is not described. On FinMMR Easy the tools-only row of Table 2 is 74.08, so the two baselines add 3.09‡ over it and FinAcumen adds 7.59.
- **What in the memory block helps (Appendix D, Table 4).** On a 600-question test subsample (a threshold of 0.60 rather than 0.65; the number of runs is not stated): Q only 53.00, plus gold answers 56.25, plus experience and tools 62.00, plus annotation and tools without experience 58.50, everything 67.50. The first two rows run without tools, so the 14.50-point total mixes tools, experience and annotation; Findings and Cautions are never ablated separately. **Here experience is the larger step**: tools plus annotation without experience add 2.25 (B to D), while adding experience adds 3.50 (D to C) or 9.00‡ (D to E; on FinMMR Easy 64 to 81, +17‡), and the paper writes "Experience provides the dominant marginal improvement". This sits uneasily with "tools give about twice the memory gain" above; the settings differ (subsample, threshold 0.60, retrieved gold answers in rows B to E), and the paper does not reconcile the two. Gold answers alone add 3.25 (A to B), which is relevant to the leakage question below.
- **More backbones (Table 11, BizBench, Base to FinAcumen).** GLM-4.6V 30.40 to 75.58; GPT-4o-mini 23.60 to 59.60; Gemini-2.5-Flash-Lite 32.60 to 48.40. These compare Base (no tools, no memory) with the full system, single numbers.
- **Hyperparameters (Section 5.5).** τ was chosen by hit rate (not accuracy) over nine values, computed over "test queries" (Section 5.5; Appendix E sweeps the same nine values over 11,379 test query embeddings; no gold labels are involved in a hit rate). Section 5.5 gives a hit rate of 79.8% at 1200 entries for τ = 0.65, while the global value at 1200 entries in Table 5 is 0.71; the paper does not reconcile them. k_max ∈ {1, 3, 5, 7} was tuned on 500 questions from BizBench and FinMMR-Medium (macro 57.80, 57.85, 63.11, 62.17); the paper does not say whether those questions are disjoint from the test sets.
- **Cost (Appendix K).** Building a roughly 1,800-entry bank is estimated from six source instances at 64,200 API calls, 244.43 million tokens, CNY 142.97 and 78.12 hours sequential. Per question at inference (a sixth of the test instances, paired with and without the bank), total tokens go from 20,043.51 to 42,523.13 and cost from CNY 0.0115 to CNY 0.0244. The build estimate is for a roughly 1,800-entry bank, smaller than the roughly 2,400-entry bank evaluated, so it may understate the cost of the evaluated bank. There is no matched-compute baseline.

## Where the gain is absent, small or unexplained

- **Below the best published model in four columns.** BizBench 68.65 vs 79.30; FinMMR Hard 46.10 vs 50.80; FinTMMBench 19.98 vs 21.53; FinMME 51.08 vs 52.54 (Gemini 2.0 Flash also reports 51.85). The paper's text lists the first three and not FinMME. On FinMME the gap (1.46‡) is smaller than FinAcumen's own five-run SD (2.24); on FinTMMBench the published 21.53 lies just above FinAcumen's 95% CI [18.88, 21.08].
- **Smallest gain on FinTMMBench:** 16.20 to 19.98 (3.78‡). There the two other memory methods score 14.52 and 16.73, around the bare Base.
- **Memory fires about half as often on charts.** At τ = 0.65 the hit rate is 0.48 on FinMME against 0.68 to 0.90 elsewhere, and the mean is 1.15 retrieved entries per query over all queries, not only those that hit (Table 5). These come from a 1200-entry snapshot built uniformly across benchmarks, not the roughly 2,400-entry bank used for the main results. The paper gives no tools/memory split for FinMME in the main ablation, so how much of its 27.84 to 51.08 comes from memory is not shown.
- **The "selective" claim is not isolated.** The paper says the accumulation curve "does not by itself isolate the effect of selective retrieval". It reports no accuracy comparison of the τ gate and fallback against always injecting the top entries, and no Findings-only versus Cautions-only ablation.
- **Diminishing accumulation.** Per-interval gains shrink (+1.30 points over the last 600 entries; between 120 and 240 entries Figure 2 shows −0.05‡ points, which Appendix C reports as −0.04 per 100 entries). The paper does not state how many runs each snapshot has; the 2400-entry point (68.65) equals the five-run mean in Table 9, whose SD is 2.45.
- **Inconsistencies in the paper.** Bank size (about 2,400 vs about 1800 entries; Section 5.1 calls the bank "∼2,400 experience accumulation trajectories", though K = 8 trajectories are sampled per item); Section 5.4 puts saturation beyond 1800 entries while Appendix C picks 2400 as the "saturation knee"; the test-query count in Appendix E (11,379) vs the test sizes in Table 6, which sum to 8,756‡, and the FinMME 11,099 samples in the Figure 10 badge vs 2220 test items; Algorithm 1 has an undefined flag ω that schedules an asynchronous consolidation write at inference, odd beside "frozen, read-only at test".
- **Limits stated by the authors:** an upfront LLM cost to build the bank, and English-only benchmarks.

## Our read

HarnessRSI score **68**, band ★★, evidence level **retained**: the frozen bank, built from training/validation items, helps on test items it was not built from. The paper reports a held-out bank source, five evaluation runs with confidence intervals, a tool-versus-memory ablation on three configurations, a comparison with Reflexion and ExpeL on four settings, cost estimates, and three further backbones (Table 11) plus a 235B model besides the main 8B one. It does not report a matched-compute comparison, an overlap or contamination check between the bank's source items and the test items (it relies on the split and the frozen bank; retrieved entries carry gold answers), an accuracy ablation of the threshold/fallback, or transfer of the bank across benchmarks (the bank pools all of them).

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
