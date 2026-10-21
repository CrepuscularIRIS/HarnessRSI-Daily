# SOURCE — DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training

Read from: arXiv 2609.04094v1
Paper figures shown: none

License: CC BY 4.0, as recorded in reel/candidates.jsonl. Figure reuse was permitted but not used. All poster visuals are our own method diagram and charts/tables reconstructed from the paper's reported numbers.

The exact-version PDF was downloaded afresh for this task. The entire 35-page PDF, including appendices and prompts, was read through fresh layout text; the title block, Table 6/7/8 page and Figure 8 cost page were also rendered and visually checked. Prior drafts were not used as evidence. The source PDF and fresh facts are in /home/lingxufeng/reel-work/2609.04094/.

## Provenance by claim

| Content | PDF location | Scope / interpretation |
|---|---|---|
| Exact title, author order and affiliations | p1 title block | Shubham Gandhi, Saurabh Goyal, Kiran Kate, Yara Rizk; Gandhi CMU, others IBM Research; first two equal contribution. |
| Rubric generation, merge and criterion keep rule | pp3–5, §§3.2–3.3 | Criterion retained iff at least one group rollout fails it; no ground-truth reward. This is not candidate-patch retention. |
| Reward, cited-step quality, winner/loser weighting, length handling | pp3–5 Eqs1–7; pp19–23 Appendix E | Token advantages weight GRPO updates; scalar advantage total conserved only over credited tokens, not gradient vector (explicit p20). No-citation/collapsed-normalizer fallback. |
| Separate step-attribution judge call | p23 Appendix F overview; pp32–33 Listings4–5 | Attribution may override earlier pass/fail verdict and must cite a step. Closed-form redistribution does not eliminate LLM attribution expense. |
| LoRA policy training rather than harness edits | p5 §4.1.2, p18 Appendix D, p26 Table10 | Rank-16 adapters update weights; base model frozen. Dynamically regenerated rubric sets are not a selected permanent harness library. |
| Data, benchmark splits, evaluation independence | pp5–6 §§4.1.2–4.1.3; p6 Table2 | 90 train; TN168, TC417, Banking97 test. TC has unseen apps/compositions. Only AppWorld training; Banking zero-shot. AppWorld unit-test evaluation; Banking state-matching SR with GPT-5.4 simulator/judge. |
| Headline chart, comparisons and crossed ablation | p6 Table2; p7 §4.3 | Chart is Qwen3.6-27B p1: Base / outcome / full DRACO, all five metric columns. Outcome-aware reference gets programmatic training rewards, not rubric step attribution. Static-with-credit is the matched mechanism arm; outcome+DRACO-credit control not reported. |
| Random-reward training control | p7 §4.3; p6 Table2 for Base/full | TN TGC/SGC74.0/50.0 vs Base69.4/41.1 and full DRACO85.3/70.6. Some improvement occurs without the proposed credit signal; neither causal-attribution validation nor an outcome+step-credit control. Reported values, no ‡. |
| Headline checkpoint identity and variability | pp5–6 protocol; p12 Table4 and caption; p9 Limitations | Qwen3.6 checkpoints90/95/100; Qwen2.5 checkpoints65/70/75. Three inference runs each, then mean across checkpoints. Trained SD across checkpoints; Base and cited SALT SD across inference runs. Training variability not characterized. No SD/CI on Average. |
| Hyperparameters and tuning-selection caveats | p5 §4.1.2, p18 Appendix D, p26 Table10 | Precommitted configuration, B16/G6, eight H100, 100 vs75 steps per explicit evaluation protocol. No split identified as hyperparameter/default selection set; no hyperparameter-search or baseline-tuning budgets reported. Avoid test-selected checkpoints; no tested contamination/leakage audit found in full text. |
| Where full DRACO is not best | p6 Table2; p12 Table4 | TC SGC40.7 vs static/no-credit42.4; TC TGC p3 43.9 vs45.6; Banking p3 8.6 vs dynamic/no-credit9.3, self-judge11.7. No claim of blanket dominance. |
| Difficulty concentration | p14 Table6 | TN hard SGC51.9 vs dynamic/no-credit55.0; TN medium benefits much more. All Table6 denominators are stratum-specific, and task-weighted full-DRACO TGC values reconcile with Table2 to rounding. |
| Cross-model and thin transfer results | pp6,12 Tables2/4 | Qwen2.5 Banking3.4±0.6→4.0±1.0. TN62.9/42.3 vs cited outcome-aware SALT66.2/47.9; TC34.0/19.2 vs36.8/20.9. Published SALT protocol not matched here. Frontier Banking20.4±1.0 vs no-credit19.7±0.5; selfjudge21.1±1.4. No significance/difference CI; checkpoint spreads not training-seed uncertainty. |
| Self-judge variants and bias audit | pp7,11 §A.1, p14 Table7, pp11–16 Appendix B.1 | Main selfjudge thinking+three-call unanimity; weaker variant single-call/no thinking. Replay uses weaker variant, reports agreement not correctness:89.4%, always-pass72.0%, false-pass30.4%, false-fail1.3%. Archived frontier proposals condition generation/union replay. No human ground-truth criterion or step-attribution validation (p9 Limitations). |
| Evaluation costs | pp7–8 §4.4; p14 Table8 for TN | TN$10.77→$8.27; TC$43.56→$38.03; separate from training. Not GPU-inclusive life-cycle cost. |
| Training judge costs | p7 §4.3; p15 Figure8 (visually checked) | Full$1607, static/no-credit$570, main thinking/three-call selfjudge$316 over100 steps per Figure8; no separate weaker-variant cost identified. All prices are token-based reference costing. GPU and wall-clock totals absent; static rubric-construction setup inclusion unspecified. |

## ‡ values

No new decimal differences or percentages were computed for the blogs or poster. Four integer phase costs carry ‡ because their source is a figure label, not a numerical table:

- **$63‡**: full DRACO task-specific rubric-generation bar, Figure8(a), p15.
- **$527‡**: full DRACO rollout-specific rubric-generation bar, Figure8(a), p15.
- **$318‡**: full DRACO union/merge bar, Figure8(a), p15.
- **$308‡**: full DRACO credit-reallocation/attribution-call bar, Figure8(a), p15.

These are read directly from the red full-DRACO bars, not approximated from bar height and not calculated from repository code. The separate scoring phase is $391 (not displayed in our outputs). Total $1607 is printed in the paper's main text and the figure legend; we do not compute an unnecessary generation subtotal. No paper image or crop appears in the deliverables.

## Reading notes and unresolved wording

- **The two 5.3-point gains refer to different comparisons.** Abstract TN gain is85.3−80.0 (full frontier-judge model vs outcome reward); abstract Banking gain is21.1−15.8 (selfjudge vs Base). Table2 reconciles both. We do not label this a paper inconsistency.
- **Figure8 explicitly assigns the self-judge cost.** Figure8 (p15) assigns $316 to the main thinking-enabled, k=3 scoring-call selfjudge; its plotted TN TGC matches the main Table2/Table7 row. Table7 (p14) distinguishes this variant from the weaker no-thinking/single-call variant. Section4.3 (p7) mentions that weaker variant immediately before quoting $316, leaving an ambiguous prose antecedent, but the figure's assignment is explicit. No separate cost is identified for the weaker variant. We do not speculate about the wording or compute an efficiency frontier between variants.
- **Uniform tokens versus equal step totals.** AppendixB.3 (pp17–18) calls unanimous verdict credit “exactly baseline GRPO.” AppendixE.7/E.9 explicitly give equal step totals AiN/M with per-token advantage AiN/(njM), which need not equal uniform Ai when step lengths differ. We follow the explicit equations, flag the wording neutrally, and do not claim the inertness analysis proves that only correct judge attribution caused the gain.
- **Judge favoritism is a possibility, not an observed finding.** Both blogs label this as our reading, grounded in the paper's Limitations/Ethics statements on inherited judge bias. AppWorld programmatic evaluation supplies a separate outcome signal; Banking's simulator/judge shares GPT-5.4 with frontier reward generation.
- The reported Average averages five metric columns, including both TGC and SGC on each AppWorld split. It is not a task-count-weighted estimate of all-task success and has no aggregate SD/CI. We avoid promoting it as an uncertainty-supported overall win.

## Judgment notes

Board record: research/scores.jsonl, score66, band★★, evidence level `retained`; latest matching judgment research/judgments/b07.jsonl. No score or judgment file was edited.

1. **Scope caveat:** the full paper explicitly trains LoRA weights, whereas docs/EVIDENCE.md defines this board's core harness RSI as non-weight changes. Its dynamic evaluator is relevant as a component, but the recorded `retained` label should not be read as evidence of a retained non-weight harness improvement. Both blogs and the poster make this boundary visible.
2. **Variance clarification:** b07 marks variance `unclear`. Full AppendixA/Table4 does report across-checkpoint SD and inference repeats; the paper explicitly says training-time variability is not characterized. We therefore report the available variance without upgrading it to multi-training-seed evidence.
3. **Budget/leakage:** b07's partial budget match is compatible with common precommitted RL hyperparameters but unequal judge bills. Avoiding held-out checkpoint selection is a protocol precaution, not a tested leakage audit. Full-paper reading did not identify a hyperparameter-selection split, baseline tuning-search budget, human validity audit, or cost-matched outcome+step-credit control.

## Output checks

The poster follows the existing Reel Python house style, not the unrelated conference-poster template. It contains no reused paper figures. Final print-media measurement at 2400×1440 found no card overflow, out-of-bounds SVG text or overlapping chart labels. Minimum rendered sizes: body/caption 22px, method 23.94px, chart ticks/value labels 19.64px. The PDF is one page, 1800×1080pt (2400×1440 CSS px); the PNG is below 3 MB. Repository gate: `python3 research/check_reel.py reel/2609.04094` passed (1 directory, 0 failing).
