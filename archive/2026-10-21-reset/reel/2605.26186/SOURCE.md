# SOURCE — SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?

Read from: arXiv 2605.26186v2
Paper figures shown: none

Exact-version PDF downloaded directly from https://arxiv.org/pdf/2605.26186v2. All 21 PDF pages, including Appendices A–H, were read using both plain and layout text extraction. Results and family-verdict pages were also rendered and inspected. No paper/code-repository program was run. No external summary or repository source was used as paper evidence.

Figure reuse is prohibited for this assignment. The poster uses an original method diagram, an original bar chart and a newly typeset comparison table. None contains a crop, image or tracing of a paper figure. Figure labels were transcribed as numerical data, not reused as images.

## Page/table provenance

| Claim | Exact source in the PDF |
|---|---|
| Full title; author order | Title block, p1: Zihang Zhou, Ziqian Ren, Yukai Wu, Yingjie Xiong, Wei Zhou, Chao Peng, Dong Zhang, Bingheng Yan, Xuanhe Zhou, Fan Wu |
| XPU fields; trajectory distillation; merge/insert rule | §3, pp3–4; example in Appendix A.1, p12; distiller prompt, Appendix B, p14 |
| Memory can come from guilty runs; verdicts when available | Distiller prompt, Appendix B, p14; not a claim that every donor had a final verdict |
| Delayed audit and success/failure/neutral; up to five steps | §3, p4; Appendix A.2, p12; retriever prompt pp13–14 |
| Telemetry tier defaults a=0.2, b=0.1 chosen from current telemetry; retrieve ten, select three | §4.1, p5. No independent hyperparameter-selection split stated |
| Snapshot trial keep/restore; agent-controlled multi-step rollback; Repo2Run command-level rollback | §4.2, p5; Appendix C.1, p15 |
| VERIFY before FINISH | Setup prompt, Appendix B, p13. §4 says termination is on FINISH; this is not contradictory pseudocode or evidence for a different implementation |
| Read-only verifier; setup vs intrinsic defects | §4.3, p5; prompt p14; /tmp smoke-test writing allowed, no modification of repository files |
| Final prosecutor–judge failure rule; matrix outcome qualification | §5, p6; §6.2, p7; prompt p14. Same qwen3.5-plus backbone, different roles. Table 4 caption, p20, also counts missing evaluation data as failure, alongside timeout and adverse verdict; cells do not distinguish these causes |
| Curated 100-repo evaluation from 329; pinned revisions; preliminary difficulty trials | §6.1, p6 |
| Model, fresh ubuntu:22.04, 3600s timeout and common adjudication for every main system | §6.2, pp6–7. Applies individually to Claude Code, OpenCode, Qwen Code, ExecAgent, Repo2Run, EnvBench and both SetupX variants |
| KB source; target-repository removal; 600 entries | §6.2, p7; Appendix G, p20 |
| 92%, 82%, 19pp and 33pp; 10pp incremental XPU gain | §6.3, p7; headline baseline values additionally read from Figure 5a and checked against Table 4 |
| Single-run scope | §8, p9 explicitly describes single-run containerized setup. Main benchmark pass rates are fractions across repositories, not a multi-run mean; no SD/CI supplied for main comparison or retrieval ablation |
| Difficulty-specific comparisons | Figure 5a, p7; see ‡ ledger below |
| Toolchain zero vs five failures on 20 repositories; remaining failures mainly AI/ML and DevOps | §6.3, p8. We do not repeat the prose’s unqualified largest-gap claim: Figure 5b's grouped Others category has a larger absolute reduction |
| Retrieval and synthetic-noise comparisons | Figure 6b, p8; §6.4 pp8–9; Appendix G p20 |
| Opus 4.6 unchanged at 92%, API cost more than tenfold | §6.4, p9. Figure 6b prints approximately tenfold; prose says more than tenfold. Neither is an absolute end-to-end cost account |
| Multi-repo 22-family verdict distribution | Table 2 and aggregate, pp16–17; §6.3 pp7–8 |
| Multi-repo three evaluators and consensus; different from prosecutor–judge | Appendix D.1, p15; rubric pp15–16 |
| Actual cross-family service-state carryover | Table 2, p17, MISP row: Qwen finds port 80 occupied by a Saleor leftover; Appendix E, p18: leftover containers from a previous family, stale Saleor process. No corrected clean rerun is reported in the full PDF |
| SetupX weaker than Qwen on robotframework, label-studio, flyte, bitcart; MISP tie | Table 2 rows, pp16–17 |
| XPU regressions trax, neuralforecast, ajenti, civet; Claude passes iree-llvm-sandbox and qiita too | Table 4, pp20–21. These are named observed reversals, not causal claims about XPU harming those repositories |

## ‡ ledger: values read from rendered figures

Every figure-label number used in the blogs or poster carries ‡, even when the same value also occurs in prose. No plotted values were estimated from bar lengths.

- **73%‡ / 59%‡:** Claude Code / ExecAgent overall pass rates, Figure 5a, p7, verified visually in `page-07.png`. Independently cross-checked against the corresponding columns of Table 4. The other headline numbers (92%, 82%, 19pp, 33pp, 10pp) are printed in §6.3 prose.
- **100%‡ / 95%‡; 89%‡ / 69%‡; 79%‡ / 72%‡:** SetupX + XPU / SetupX without XPU, low / medium / high difficulty respectively, Figure 5a, p7, read from bar-segment labels. The prose also mentions high-difficulty 79% but the full paired breakdown is a figure-label read.
- **92%‡ / 86%‡ / 88%‡ / 81%‡:** Selector + Clean / Direct + Clean / Selector + Noisy / Direct + Noisy, Figure 6b's table, p8, verified visually in `page-08.png`. The table is embedded within a numbered figure, so we mark the transcribed cells despite their tabular appearance. The reranking differences 6pp and 7pp are explicitly reported in §6.4 prose, not newly computed by us.
- No new decimal differences, computed win counts or inferred statistical significance are used. The named Table 4 regressions avoid introducing a computed count.

## Split, access, cost and attribution limits

- Identity-level exclusion is documented; a tested fork/family/near-duplicate leakage audit is not. Evaluation and donor experience come from the same EnvBench Python pool. The text does not specify cross-target freezing/resetting of online telemetry or new XPU ingestion, or demonstrate actual related-repository contamination. We report this as an unresolved protocol detail, not as evidence that leakage occurred.
- No train/dev split for selecting retrieval defaults or baseline hyperparameters is reported. Tier thresholds explicitly depend on current telemetry. No baseline tuning budget is stated.
- No comparable XPU/failure store is reported for Claude Code, OpenCode, Qwen Code, ExecAgent, Repo2Run or EnvBench. Shared model/time cap/adjudicator is not a claim of equal tokens, retry counts or lifetime collection cost. Repo2Run does have its own command-level rollback; we do not deny that baseline mechanism.
- Figure 6b uses nominal 1.0× relative costs for qwen settings; this is not evidence of matched full-system compute across competing baselines. The paper does not itemize donor run generation, distillation, embeddings, audits or snapshot costs.
- Store-removal and retrieval ablations do not separately isolate delayed telemetry, speculative rollback, or long-term online experience evolution. We do not infer continuous improver improvement from the architecture alone.
- No separate performance-selected memory admission gate is specified. Local trial acceptance and final run adjudication are separate gates. No prose/pseudocode contradiction on initialization or retention was identified; no implementation behavior is guessed.

## Evaluation-outcome and service-isolation qualifications

- Table 4's caption (p20) counts missing evaluation data as failure, in addition to timeout and adverse verdict. The matrix does not identify affected cells or disclose the frequency/distribution of missing data. We do not assign missing-data status to any named repository or use it to explain any reversal; the headline rates still reconcile with the matrix.
- Table 2's MISP row (p17) and Appendix E (p18) report an actual Qwen run affected by a stale Saleor process/container occupying port 80 from a previous family. This is imperfect cross-family service isolation in the separate multi-repository track, not XPU-memory leakage or the count-wording issue below. The §6.2 fresh-container statement for the main track does not establish clean sibling-service isolation here. Full-PDF reading and searches for reruns, repeats, stale/leftover state and Saleor found no reported corrected clean rerun. Both MISP verdicts are Partial; no aggregate change under a clean rerun can be inferred.

## Unresolved paper wording

- Appendix E, p18, says SetupX has “four Partial/Shallow cases.” We checked all Table 2 rows on pp16–17, its caption and printed aggregate, §6.3's multi-repo result, and both worked cases in Appendix F. The below-Mostly members are label-studio, flyte, MISP, bitcart and frappe/erpnext. Table 2's printed distribution is Full=6, Mostly=11, Partial=4, Shallow=1, consistent with those members and the reported 17/22 at-least-Mostly rate. We use the table and list the members instead of reproducing the incorrect count; the prose discrepancy remains unresolved, with no speculation about its cause. The poster flags this wording mismatch.
- The printed aggregates for both agents reconcile with their Table 2 rows; Table 4's columns reconcile with all eight headline overall rates. We do not label headline pass rates inconsistent.
- Appendix E's broad statement that Qwen's Mostly families never cross the cross-container protocol layer is not repeated: its own Table 2 and Appendix F document running sibling services for some such families.

## Judgment notes

Latest matching local judgment found: `research/judgments/b17.jsonl`; score record: `research/scores.jsonl`. Score **64**, band **★★**, evidence level **retained**. No judgment/score file was edited.

The full PDF supports the scoped record: held-out=yes refers to removing target-repository entries, budget_matched=partial to a common timeout, variance=no to single-run evaluation, retained_ablation=yes to no-XPU, leakage_guard=untested despite identity exclusion, optimizer_cost=unclear and improver_comparison=unclear. The manually rated 22-family track is complementary evidence, not an isolated transfer or repeated-run study of an independently trained improver. No correction to the stored judgment is proposed.

## Rendering / delivery

House-style canvas 2400×1440; original diagram/chart/table, paper and code QRs. Body/captions at least 22px and chart labels at least 18px at rendered width; method step text also checked after SVG scaling. Final layout was rendered using the shared poster library; no library edits or subagents. The exact PDF, text extracts, page previews, facts and render script remain in `/home/lingxufeng/reel-work/2605.26186/`. Only the five required deliverables are copied to `/home/lingxufeng/ArxivDaily/reel/2605.26186/`.
