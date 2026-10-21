# SOURCE — EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

Read from: arXiv 2606.11182v1
Paper figures shown: none

Exact-version PDF downloaded to /home/lingxufeng/reel-work/2606.11182/paper.pdf. All 19 PDF pages, including appendices, were read using plain and layout text; results and reproducibility pages were also inspected as rendered images. Title and author order are from the PDF title block: Weixian Xu, Shilong Liu, Mengdi Wang. The title uses typographic small capitals for EEVEE.

Figure reuse is forbidden for this assignment. No paper figure, screenshot, crop or traced illustration is shown. The poster's method diagram and result/ablation charts are original drawings based on paper text and tables. Paper and code QRs are generated locally.

## Table/page provenance

| Content | Exact source (PDF page) |
|---|---|
| Fixed weights; router and specialized prompts; inference reads input to select slot | §2.1, p3 |
| Router mutation/reflection, solvable-example filter, validation admission, annealed accuracy/consistency/balance | §2.2, p4 |
| Slot-level training/validation routing, target-answer feedback, empty-prompt floor and Pareto admission | §2.2, pp4–5 |
| Initialization coverage, interleaved exploration, fixed-router convergence | §2.3, pp5–6 |
| Main benchmark percentages and baseline-relative gains | Table 1 / §3.2, p6 |
| Qwen3-4B-Instruct ablation means, default/router exceptions | Table 2 / §3.3, pp6–7 |
| Single-benchmark no-router definition | §3.4 / Figure 4 caption, p7 (no figure-label numbers used) |
| Direct Qwen3-4B-Instruct prompt transfer to DeepSeek-V3.2 non-thinking; held-out MBPP/MMLU-Pro | Table 3 / §3.5, p8 |
| Final inference tokens per example, averaged across Qwen benchmarks | §3.6 prose, p9; Appendix B, p18 (not read off a figure) |
| Separate six-run empty-vs-final diagnostic and GPQA losses | Table 4 / §3.7, p9 |
| Procedure versus domain-prior case interpretations | §3.7, pp9–10; Appendix A, pp14–17 |
| Ground-truth/rule-based feedback; prepared adaptation set, not fully online | §6, p11 |
| Benchmark cap, splits, data seed, model identifiers and decoding, EEVEE search budgets | Appendix B, p17 |
| Final-test repeats, prompt cap, resources; no local weight training | Appendix B, p18 |
| Alternative configurations, three trials each; SD across configuration means | Appendix B.1 / Table 6, p18 |
| Main macro means and sample SD, three independent runs including baselines | Appendix B.2 / Table 7, p19 |
| Code link, manual-router writer and LLM roles | Appendix C, p19 |

## ‡ numbers

None. No computed counts, differences or figure-label reads are used in either blog or poster. All decimal values are printed in the PDF text or tables. Main baseline-relative gains are those printed in Table 1 / §3.2. The inference costs 4.32k, 3.47k and 21.30k appear in §3.6 prose and Appendix B, not merely Figure 5. No cumulative-retention figure values are used.

## Scope and audit notes

- Main chart uses Table 7 macro scores (mean ± sample SD over the three independent main runs). Table 1 supplies individual benchmark means without per-task uncertainty. Appendix B's additional statement that final testing uses three repeats does not establish nine independent optimization runs; we do not make that claim.
- Table 2 supplies component means but no row-level variance or explicit independent-search-run count. Do not infer single-run experiments. Manual Router is a diagnostic ablation written once by GPT-5.4, not a same-model learned baseline. Default Router TheoremQA 26.10 versus EEVEE 25.27 is kept within Table 2.
- Table 4 is a separate six-run diagnostic retest, not Table 1. Its GPQA changes −3.7/−7.7 and 1/6 positive runs are scoped to that retest. Different empty-prompt retests can yield different deltas; we make no paper-inconsistency allegation.
- Appendix B explicitly excludes training and validation examples from final testing. The paper gives a 0.5/0.5 split and seed 42 but not realized per-benchmark counts or a random/stratified splitting procedure. We do not describe full official benchmark sets or shifted-OOD splits as evaluated. Held-out benchmark transfer uses the paper's capped/subsampled protocol rather than asserting full MBPP/MMLU-Pro coverage.
- Our reading of the stated protocol: a final test instance is read to route and answer, not used to evolve prompts. This is held-out prepared-set adaptation, not transductive learning on those final test instances. Validation admission and split exclusion are protections, not a proof against validation overfitting. No separate content-overlap or pretraining-contamination audit is described in the full paper.
- Candidate selection uses validation. The split used to select hyperparameter defaults is not specified. Main EEVEE settings are provided; exact numerical alternative annealing schedules/targets, consistency/balance weights, and tighter/wider search budgets, batch sizes and temporary-pool sizes are not supplied by Table 6 or its surrounding text. These numerical omissions are distinct from the missing default-selection split.
- Baseline-specific scope: the unadapted target does not learn; GEPA uses reflective prompt evolution/Pareto selection; ACE edits adaptive playbook context. §3.1 describes methods learning from a mixed training stream with held-out scoring. Exact ground-truth/validation access parity and per-baseline candidate/rollout/tuning budgets are not itemized. No GEPA/ACE variant is reported with EEVEE's router/admission rules. Do not infer deliberate baseline weakening.
- Table 3 explicitly says learned prompts transfer directly. Whether the router text also transfers unchanged is not separately specified. The right-hand held-out benchmark table does not unambiguously name its target model. Both halves average three runs without SD/CI; small gaps are not claimed statistically reliable.
- Token costs are final inference after adaptation for Qwen3-4B-Instruct only, with routing before answer generation. They do not include the adaptation search; total adaptation tokens/dollars, comparable elapsed time, unadapted inference tokens, DeepSeek cost and matched GEPA/ACE search budgets are not reported.
- Main improvements are led by HumanEval on both models; Formula and TheoremQA also improve. GPQA Diamond decreases on both models; DeepSeek Formula is 60.55 against GEPA 60.56 (near-tie, no per-task variance); MMLU-Pro and the held-out macro average fall below unadapted scores.

## Judgment notes

Stored record: research/scores.jsonl, total 63, band ★★, evidence level retained. Latest matching judgment is research/judgments/b20.jsonl, version v1. No score/judgment file was edited.

- `variance: unclear` is incomplete relative to the full PDF: Table 7 (p19) gives main macro-score means and sample standard deviations over three independent runs for EEVEE, GEPA, ACE and unadapted baselines on both models. Blogs and poster report this variance and retain the stored score, which may understate that evidence.
- `leakage_guard: unclear`: Appendix B (p17) explicitly excludes training and validation instances from final testing. This is an instance-level split safeguard, not a reported content-overlap or pretraining-contamination audit.
- `optimizer_cost: unclear` remains apt for search cost: the cost comparison concerns post-learning inference, not total optimization expenditure. Budget matching remains unestablished. The artifact helps on held-out examples; the retained evidence label is not silently upgraded.
