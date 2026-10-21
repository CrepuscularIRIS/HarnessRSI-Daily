# SOURCE — EvoRubric: Self-Evolving Rubric-Driven RL for Open-Ended Generation

Read from: arXiv 2605.29847v2
Paper figures shown: none

Exact-version PDF downloaded directly from https://arxiv.org/pdf/2605.29847v2 into /home/lingxufeng/reel-work/2605.29847/paper.pdf. PDF title block confirms title, author order, Alibaba Group, v2 dated 8 Oct 2026. All 22 pages, including references and appendices, read using layout and plain pdftotext; title and main result/ablation tables also visually checked. No web summaries or code were evidence sources. No paper figures reused; method diagram and result chart independently drawn from prose and tables. No code URL supplied.

## Provenance

| Claim / numbers | PDF source |
|---|---|
| Exact title, authors | p1 title block: Xin Guan, Xiaomeng Hu, Shen Huang, Zhenyi Wang, Bo Zhang, Zijian Li, Pengjun Xie, Bo Liu, Jiuxin Cao |
| Shared weight updates; rubric contents and signed weights | pp3–5; Appendix C pp14–16; Generator prompt, Table 11 pp20–21 |
| Fixed base rubrics, empty evolved memory, N=8/M=4, eligibility >0.2, highest-consensus batch, saturation, exact-text duplicate checks, FIFO capacity10 | Sections3.1–3.3 pp4–5; Algorithm1 p15; Appendices C–D pp15–16 |
| Reasoner reward base + half historical + half eligible current minus length; Generator reward validity/discrimination/consensus and penalties | p5 Eqs3–4; Appendix C pp15–16 (includes auxiliary concentration penalty) |
| Insulin-storage example dimensions | Appendix F, Table8 pp16–17; presented descriptively, not medical advice |
| Macro averages 52.90/53.19/56.28 and 59.05/59.07/61.13; gains3.09/2.06; per-task means/SDs and relative gains | Table1 p6; reported differences also abstract p1 and Section4.2 p7. Macro means have no SD/CI. RL cells summarize three training seeds; Base cells summarize three response-sampling runs. No claim about single-run results. |
| Benchmark scope, training data3000 per domain, held-out500 HealthBench and held-out ResearchQA, independent judge | Section4.1 p6. Each domain gets a separate policy per scale. Other evaluated sizes/partition construction not specified. |
| Medical8B ablations and retained mechanisms | Table2 and surrounding Section4.3 p7: means over3 matched runs, no per-variant SD/CI. No-Generator-loss retains generation/screening/grading/memory/rules and allows indirect shared-parameter change; no-memory retains current supervision. |
| Static / same-scale External / stronger GPT-4.1 baseline access and scope | Section4.1 p6; Table3 and Section4.3 p7; AppendixA p14. Full DR-Tulu search/citation training is not evaluated. External per-baseline verifier/consensus/admission settings and generator compute are not exhaustively enumerated; do not assume their absence. |
| Expert/model initialization38.89/41.83/44.64/45.13, gap0.49 | Table4 and text p8; means3 runs without variance/CI |
| Human criterion invalidity counts and percentages; diversity | Table5 p9; Tables9–10 and AppendixI pp18–19. Majority of3 annotators,20 Medical prompts. Criterion counts pooled across prompts; effective-diversity deduplication is within-prompt only. This is not contamination/leakage testing. |
| Blind response W/T/L percentages,50 Medical prompts | Table6 p9, AppendixI.3 p19; majority of3 annotators, three-way disagreement becomes tie, no CIs. Overall wins not generalized to all quality dimensions. |
| Fixed-response rubric preference72/28%,100 queries with3 fixed responses | Section4.5 p9, AppendixG p17; Claude default evaluator, not human preference. Train/eval membership of these sampled prompts not specified. |
| Hyperparameters and hardware | Table7 p18, AppendixC p16. 4 epochs,8×H20, explicit training numerical settings. Tuning selection split, checkpoint selection rule and baseline trial budgets not stated; do not conflate missing selection details with missing training values. Final judge numerical default decoding parameters not given. |
| GPT-4.1 generation81.20M input/2.91M output/84.11M total tokens,USD185.70 | AppendixH p17, averaged3 runs; generator API only, not full baseline cost or Evo cost. No GPU-hours, wall time or full Evo training cost found. |

## ‡ numbers

None. All displayed result values, percentages and differences are explicitly reported in the PDF text or tables. No figure-label reads, computed win counts, new deltas, ratios or aggregate recomputations are used. The result chart includes original table averages and does not manufacture average uncertainty.

## Scope and unresolved reporting limits

- Independent-family Claude evaluation and blind human comparisons reduce direct self-judging concerns; neither proves absence of judge preferences or rubric/evaluation leakage.
- Algorithm1 operates on training D. Explicitly held-out HealthBench/ResearchQA evaluation is reported, but detailed partitioning, tuning/selection split and overlap/contamination audit are not. We do not allege test-prompt evolution.
- No outcome-only RL comparator, total-compute-matched comparison, separately optimized baseline reward-model budget or frozen-rubric cross-domain transfer experiment was found. Shared policy-side settings alone are not a total compute match.
- Main mean wins include modest LLMEval gains comparable to method seed SD; no significance tests. Tables2–4 report averages without SD/CI. Human advantages concentrate in conciseness/relevance; completeness often favors baselines and factual correctness is close.
- Prose and Algorithm1 agree on empty memory initialization and highest-eligible-consensus admission. No text-versus-table numerical inconsistency identified after checking model variants and relevant rows.

## Judgment notes

Score retained verbatim from research/scores.jsonl: 63, band ★★, evidence level improver. Latest matching judgment found in research/judgments/b07.jsonl. No score/judgment files changed.

1. `variance: unclear` understates the full PDF: Table1 explicitly gives means ± standard deviations across three RL training seeds (Base uses response-sampling runs). This evidence does not extend to macro-average uncertainty or missing SDs in Tables2–4.
2. `leakage_guard: tested` is supported in the stored record by a quotation about invalid-criterion rates. That quotation and the human audit test criterion validity, not train/test leakage or contamination. No leakage audit was found after reading the full appendix. We therefore do not repeat the stored tested-leakage claim.
3. Policy-side budget matching and the GPT-4.1-only API cost justify qualified, partial statements, not end-to-end cost parity.
4. The recorded improver level is presented as the repository's judgment. This is a hybrid weight-training / non-weight rubric-memory system, not a weights-frozen harness intervention; domain-specific policies' benchmark gains are not cross-domain transfer of a retained pool.
