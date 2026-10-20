# ManimAgent: remembering animation repairs helps first drafts — but fewer repair rounds do not mean faster rendering

*A Reel interpretation of [ManimAgent: Self-Evolving Multimodal Agents for Visual Education](https://arxiv.org/abs/2606.30296v2), confirmed from the PDF (HarnessRSI Daily score 67, ★★). Code: [jwj1342/Paper2Manim](https://github.com/jwj1342/Paper2Manim).*

## What the system changes about itself

ManimAgent turns a scientific paper section into a short Manim animation. Its persistent change is an external **Episodic Memory Bank (EMB)**, not model weights. A positive channel stores distilled success rationales and selected code; a negative channel stores failure patterns, causes and repair recipes. Later scenes retrieve two positive records as soft **Reference Examples** and three negative records as **Known Pitfalls**. The latter are hard constraints in the prompt, not a formal guarantee that generated code obeys them (§3).

## The loop, and the keep/reject rule

The storyboard feeds a Coder, static checker and sandbox renderer. Crashes trigger text-only review, with two repair retries and a repeated-error short circuit. Renderable scenes enter a separate visual loop with two revision opportunities. A GPT-5.5 reviewer sees four keyframes and scores logical flow, layout/occlusion and accuracy; their unweighted mean drives revision. A score of 90 auto-passes; a reviewer verdict or the budget can also stop the loop. Delivery selects the highest-scoring renderable candidate, with earliest-candidate tie breaking.

Memory writes have separate gates (§3.3):

- **Positive:** the selected candidate must score at least 85; an LLM distills a rationale and retains the chosen code and provenance.
- **Negative:** an adjacent crash→successful-render transition qualifies, or two adjacent renderable versions must improve the visual score by at least 5 points. An LLM distills a structured lesson rather than a literal code diff.

A trace that misses a gate does not generate that kind of record. The bank starts empty and grows without eviction or paraphrase-level deduplication. These are local improvement gates; our reading is that they do not establish the causal effect of a lesson through an independent intervention.

## Headline result, as reported

The experiment uses a single GPT-5.5 family endpoint for text agents and the visual reviewer. A 39-task memory-building stream produces frozen banks; a paper-disjoint 33-task fixed probe reads each bank without writing back. Human evaluation uses a stratified 25-task subset, not all probe tasks (§4, Appendix H).

| Condition (Table 1) | Human Pass@1 (%) | Mean reflection rounds ↓ | Mean human quality (1–5) |
|---|---:|---:|---:|
| VLM reflection only | 68.5 | 12.2 | 3.41 |
| Manim-code RAG | 83.3 | 11.4 | 3.65 |
| Random EMB | 69.6 | 11.3 | 3.42 |
| EMB@0 | 62.0 | 12.2 | 3.26 |
| EMB@50 | 66.7 | 11.3 | 3.31 |
| EMB@100 | 75.0 | 10.8 | 3.43 |
| EMB@200 | **84.9** | **6.5** | **3.88** |

**Pass@1 is the proportion of individual human usability votes**, not the percentage of tasks passing a majority vote. Quality averages five Likert dimensions across raters. Human judgements concern first-attempt videos, whereas the repair metric concerns convergence; do not confuse first-attempt evaluation with best-of-N final delivery. The table gives point estimates without seed variance, confidence intervals or a stated number of independent runs per cell. It does not identify a headline seed or best-run selection rule.

## The controls that decide whether the gain is real

- **Retrieval rather than extra context alone.** Manim-code RAG uses public documentation and community code with the same encoder, index, retrieval depth and truncation budget. Random EMB preserves record count, format and token budget but shuffles task alignment. These are useful controls, not equal-total-cost controls: the static baseline does not receive the self-grown write/consolidation loop or a matched memory-building expenditure.
- **Channels and content (Table 1).** Without positive memories, Pass@1 is 70.0 and rounds 12.0; without negative memories, 80.9 and 11.6, versus full 84.9 and 6.5. Removing the positive code excerpt gives 75.0 / 10.5 / 3.50; ungated failure memories give 81.8 / 8.4 / 3.64. Top-1 retrieval gives 81.0 / 9.9 / 3.84. These support complementary channels, but none of the ablation margins has uncertainty estimates. The separate no-memory ablation is 61.8 / 12.2 / 3.20; it is not the EMB@0 or VLM-only row.
- **Who judges quality?** There are 54 blind graduate raters; condition, bank size and VLM score are hidden. The main plan covers 175 videos with three ratings each, although the appendix also describes two or three ratings per video and reports agreement on 153 three-rater videos. Final per-condition denominators are not fully reconciled in the PDF. For binary usability votes, Fleiss’ κ is −0.01 and full agreement is 59.4%. Continuous-quality reliability is also low: the five Likert-dimension ICCs are visual design 0.24, key-claim coverage 0.00, visual robustness 0.10, animation flow 0.33 and first-attempt usability −0.09, measured on only 23 videos with three raters (Appendix H, p20). Disagreements are aggregated, not adjudicated. Low agreement and absent CIs make the small RAG margin hard to interpret.
- **Reward-model favoritism.** The same GPT-5.5 reviewer guides revisions and gates memory, so its preferences could become self-confirming. Blind humans supply headline quality instead. On 37 paired videos after filtering missing/failed renders, VLM–human Pearson correlation is −0.17, Spearman −0.20 and Cohen’s κ −0.07 (Table 9). Replacing the reviewer with Step-3.7-Flash gives 80.0 / 8.6 / 3.42. This sensitivity control does not eliminate shared blind spots or establish that the visual reward is human-aligned.
- **Selection and leakage.** Defaults are fixed across conditions and match manifests (Table 13); the paper does not state which split selected them or report baseline tuning/search budgets. It describes paper-overlap and input/evaluation-field validation, read-only probe memory, and pre-/post-cutoff stratification. The latter gives Pass@1 74.1% vs 80.0%, quality 3.56 vs 3.40 (Table 14): no consistent directional advantage, not proof of absent pretraining contamination. The 40-task cross-test is only an exploratory qualitative memory inspection, not quantitative transfer evidence.

## Where the gain is absent or small

The large contrast is against empty memory, not the strongest static retrieval baseline. Only EMB@200 exceeds Manim-code RAG on both human metrics; EMB@50 and EMB@100 remain below its 83.3% Pass@1 and 3.65 quality. Full EMB reaches 84.9% and 3.88; Top-1 retrieval is already close on quality at 3.84. Without variance or CIs, these are numerical differences, not demonstrated statistically reliable wins.

**Fewer rounds are not lower latency.** Table 12 reports EMB@200 at 31 minutes per task versus RAG at 27, Random EMB at 25 and EMB@0 at 19. Estimated LLM/VLM token counts are 36K/20K for full EMB versus 38K/23K for RAG. Counts come from output characters and review calls, not explicit token tracking. Appendix P attributes the longer rendering time to more elaborate scenes. Per-scene limits are the same: two text retries, two visual revisions, and sandbox wall time 180 seconds, CPU 120 seconds, RAM 4 GB. Total bank-building cost and dollar expenditure are not reported.

There is no per-domain or per-task gain breakdown to tell whether a few tasks dominate the averages. The evidence is limited to one main model family, one renderer and five English scientific domains; no student-learning outcome is tested.

## Our read

HarnessRSI score **67**, band **★★**, evidence level **retained**. Frozen, paper-disjoint, read-only evaluation and channel/gate ablations support the claim that retained experience helps later animation tasks. Retrieval budgets are partially matched, not total compute. The paper reports human evaluation, estimated per-task resources, reward–human agreement and leakage safeguards; it does not report repeated-run variance, CIs, total memory-construction cost or quantitative cross-renderer/model transfer. The weak human agreement and modest advantage over strong RAG are central caveats, not footnotes. This is evidence for useful retained memory, not a demonstrated recursively improving improver.
