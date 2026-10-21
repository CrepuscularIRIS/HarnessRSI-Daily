# SOURCE — EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle

Read from: arXiv 2510.16079v3
Paper figures shown: none

- Exact version downloaded directly from https://arxiv.org/pdf/2510.16079v3 into the work directory. Read all 24 PDF pages, including the appendix, in layout and plain extraction; visually checked title block and tables. The PDF title, rather than the truncated task title, supplies the full title above.
- Authors, PDF p1, in order: Rong Wu, Xiaoman Wang, Jianbiao Mei, Pinlong Cai, Daocheng Fu, Cheng Yang, Licheng Wen, Xuemeng Yang, Yufan Shen, Yuxin Wang, Botian Shi. Rong Wu and Xiaoman Wang contributed equally.
- Figure reuse is forbidden for this assignment. The poster uses an original method diagram and charts/tables redrawn from reported numerical data, never a paper figure or crop.
- Paper: https://arxiv.org/abs/2510.16079v3
- Code URL printed in the PDF: https://github.com/Edaizi/EvolveR . No repository code was run or used as evidence.

## Provenance (PDF page numbering)

| Claim / poster panel | Source | Boundary / interpretation |
|---|---|---|
| Full title and authors | p1 title block | Exact title confirmed visually. Poster author line lists both equal-contribution first authors followed by et al.; full order above. |
| Both memory and weights change | pp3–6, §§3.2–3.3; p19 A.3 | Offline frozen-policy distillation, online GRPO weight updates. Experience-token loss masked by default. Not weight-frozen harness-only improvement. |
| Stored experience | pp4–5, §3.2.1; p4 Figure 2 caption; pp21–22 Tables 14–16 | Natural-language advice + structured triples; linked source trajectories; success/use counts. Diagram drawn independently. |
| Add / merge / prune rules | pp4–5; p16 A.1 | Same-problem semantic dedup; embedding prefilter 0.85 + policy-model semantic check; score (successes+1)/(uses+2); periodic prune below 0.3. Not a validation-set candidate-adoption gate. |
| Feedback and cold start | pp6–7, §§3.3/4.1.4; p19 A.4.1; p20 Table 12 | Exact-match outcome plus format reward. About 700 training samples. GPT-4o cold-start trajectories generated with gold answers/documents; later self-distillation is not a fully teacher-free lifecycle. |
| Headline average EM | p7 §4.1.3, p8 Table 1 | 3B 0.382 vs best baseline average 0.325, 7B 0.417 vs 0.385, both Search-R1-instruct. Seven benchmark values reconcile with reported averages after rounding. No reported seed/run count, SD/CI or Table 1 checkpoint choice. Average means across benchmarks, not across seeds. |
| 7B results chart | p8 Table 1 | EvolveR NQ/HotpotQA/TriviaQA/PopQA/2wiki/Musique/Bamboogle = 0.462/0.411/0.620/0.473/0.395/0.168/0.392. Search-R1-instruct = 0.393/0.370/0.610/0.397/0.414/0.146/0.368, strongest Table 1 baseline in each 7B column. Charts have separate legends for EvolveR and Search-R1-instruct. |
| 3B exceptions and concentration | p8 Table 1 | 3B EvolveR TriviaQA 0.584 < Search-R1-base 0.587; PopQA 0.434 < Search-R1-base 0.435; Bamboogle 0.328 vs Search-o1 0.320. Strongest-column comparison uses different baselines as appropriate, not only Search-R1-instruct. Larger 3B gains over column leaders on 2wiki/HotpotQA; 7B largest gains NQ/PopQA (our qualitative reading). |
| Evaluation-only retrieval ablation | p9 §5.2.2; p10 Table 3 | Identical experience-driven RL training; 3B 0.382 -> 0.340 when retrieval denied only during evaluation; 0.5B 0.150 -> 0.078; 1.5B 0.270 -> 0.123. 3B Bamboogle 0.328 -> 0.240; TriviaQA 0.584 -> 0.569. Not baseline-plus-memory. |
| Components and memory variants | p10 Tables 4–5 | Table 4 no components 0.134; no-distillation RL-only 0.325; distillation+retrieval/no RL 0.357; experience-trained RL/no evaluation retrieval 0.340; full 0.382. Table 5 no memory 0.325; teacher memory 0.370; self memory 0.382. |
| Self versus teacher | p9 Table 2 | Self/teacher averages at 0.5B 0.150/0.220; 1.5B 0.270/0.290; 3B 0.382/0.370. Teacher 3B 2wiki 0.437 vs self 0.381. GPT-4o-mini teacher shares EvolveR's mechanism; this is an internal control, not a Table 1 external competitor. Alignment explanation attributed to authors, not endorsed as identified cause. |
| GRPO versus successful-trajectory SFT | p17 Table 8 and A.2.1; pp16–17 A.1 | Same successful online trajectories used for SFT; GRPO additionally uses failures; averages 0.357/0.382, TriviaQA tied 0.584, Bamboogle 0.248/0.328. SFT settings reported, equal compute not claimed. Do not equate this training recipe with Table 4's differently described no-RL configuration solely because the average is also 0.357. |
| Principle quality | p11 Table 6 | 100 annotations total. High tier ideal82%/vague10%/incorrect8%; low26%/50%/24%. Score-stratified cross-section, not randomized before/after pruning. Per-tier n not given. |
| Pruning and selection boundaries | p17 Table 9, A.2.2 | 1.5B threshold0.3/default average0.270; threshold0.9 average0.276. No selecting split or search budget specified. Baseline SFT training settings ARE supplied but not baseline tuning-search budgets. No claim default selected on test: selection protocol simply unspecified. |
| Scalability | p11 Table 7, §5.3 | Random10% validation subset from six unnamed benchmarks. At45,083 entries EM0.410, at49,934 EM0.387. Evolving policy and memory, not isolated memory-size intervention (our reading). Do not merge these validation numbers with Table 1 headline as if same split/checkpoint. |
| Runtime versus accumulation cost | p16 A.1; p7 §4.1.4 | Reported full3B lifecycle39.4h on8A10080GB;128prompts and8rollouts/prompt each RLstep. No headline RLstep budget, baseline runtimes/token budgets, separate offline curation or cold-start teacher-generation costs. Approximately14,000 principles, top3 lookup0.06s: retrieval overhead only, not experience accumulation. |
| Leakage limits | p7 §4.1.1; p11 §5.3/Table7; full appendix pp16–24 | NQ/HotpotQA TRAINING splits build store; five named OOD datasets described as evaluation-only. No question/answer/near-duplicate overlap audit or explicit evaluation-writeback prohibition found. Validation subset relationship to headline/default selection unspecified. This does not establish leakage or that validation tasks were stored. |
| Experience-token absorption | p19 Table11/A.3 | Unmasking experience token loss0.371 vs default0.382; PopQA0.435 vs0.434 exception. Authors' noisy-retrieval explanation remains a hypothesis. |
| Limits of improver evidence | p18 Table10/A.2.3; p23 A.6 | Creation-phase score0.462 ->0.500 among surviving principles; not a frozen-improver matched-budget test. Capability-bound distillation and lifelong memory efficiency stated limitations. |

## ‡ numbers (computed by us)

None. All reported decimal scores, thresholds, latency and runtime are direct paper values. Chart geometry is a visual encoding of Table 1 values, not a new reported statistic. Model-size names and the HarnessRSI score/band are metadata. No figure-only numerical readings are used.

## Checks of potentially misleading wording

- The p8 prose's general claim that PopQA is a winning column has a valid 7B referent (0.473 > 0.397), although the 3B variant loses that column (0.434 < 0.435). We report model-specific exceptions and do not label this a numerical inconsistency.
- The p10 prose loosely calls 0.340 an RL-only baseline; Table4 and Table3 explicitly identify it as experience-trained RL with evaluation retrieval disabled, whereas no-distillation/no-retrieval RL is 0.325. We preserve the table conditions rather than treating these as contradictory results.
- Repeated 0.357 averages in Table4 and Table8 do not establish identical training settings. Both are reported with their own descriptions.
- Threshold0.3 is the named default, not Table9's best average. Nothing in the paper identifies the selecting split; we do not infer test-set tuning.
- No run count is inferred from a table lacking SD/CI. No claims of statistical significance are made from point estimates.

## Judgment notes

Score65, band★★, evidence level retained come from research/scores.jsonl; latest matching judgment is research/judgments/b08.jsonl. No score/judgment files were changed.

The stored judgment marks optimizer_cost unclear. Full v3 PDF AppendixA.1 (p16) reports approximately39.4h for the3B full training lifecycle and retrieval latency. The blogs/poster explicitly credit that report, while noting no comparable baseline budget or separate curation/teacher-cost accounting. This is a judgment coverage correction, not a score recomputation.

The record's held_out/cross_task evidence is based on the declared training versus evaluation datasets; our interpretation preserves that intended separation but flags missing exact evaluation split IDs, model/default selection protocol, memory writeback protocol and overlap audit. The record credits a self-versus-teacher improver comparison, but its evidence level remains retained: this does not show an evolving improvement mechanism outperforming a frozen one at matched budget.
