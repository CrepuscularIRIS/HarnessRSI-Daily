# SOURCE — ExpSeek: Self-Triggered Experience Seeking for Web Agents

Read from: arXiv 2601.08605v2
Paper figures shown: none

Exact-version PDF downloaded from https://arxiv.org/pdf/2601.08605v2 into `/home/lingxufeng/reel-work/2601.08605/paper.pdf`. All 29 pages, including the appendix and prompts, were read; both layout-preserving and plain text were extracted. PDF pages 6–8 were rendered and visually checked. The exact title and author order come from the PDF title block, not the repository. No code from the paper or its repository was run.

Figure reuse is forbidden for this assignment (arXiv default license). All poster diagrams and charts are original drawings from paper statements/table values. No cropped, traced or copied paper figure is displayed.

## Table/page provenance

| Material | PDF source | Scope and qualification |
|---|---|---|
| Exact title/authors, code URL | p1 | Wenyuan Zhang, Xinghua Zhang, Haiyang Yu, Shuaiyi Nie, Bingli Wu, Juwei Yue, Tingwen Liu, Yongbin Li. |
| Triplet construction and persistence | §§3–4.1, pp3–4; Table12 p24; Table13 p25 | Standard answers and successful trajectories are available for offline teacher labeling. Only erroneous steps yield triplets; topics reused/modified/created. No validation-score candidate acceptance or rollback rule reported. |
| Entropy definition and calibrated trigger | §3 p3; §4.2 pp4–5; Table1 p5; Algorithm1/AppendixA pp14–15 | Mean vocabulary-distribution token entropy; separate process/answer regressions; bootstrap intervals; no/linear-probability/always intervention, subject to one-step cooldown. Threshold fit is on training labels. Algorithm1 concerns fitting, not inference; no prose/pseudocode gate contradiction identified. |
| Seeking content and storage | §4.3 p5; Tables14–15 pp26–27; Table11 p23 | Three topics selected; guidance appended to observation/history, including reopening an answer step. No described persistent writeback of test-time guidance or trajectories. Inference prompts provide history/experiences, not labeled test answers. |
| Headline accuracy and ablations | Table2 p6, §5.3 p7 | Table explicitly reports five independent-run means for baselines, full and stage ablations. No SD/SE/CI, seed list or statement that repositories are independently rebuilt per run. Split seed 0 is not an evaluation-run seed claim. Chart uses 32B benchmark averages from this table. |
| Evaluation rubric and validation caveat | AppendixC p17; Table19 p29 | Accuracy uses Qwen3-235B-A22B-Instruct-2507 as an LLM judge, with temperature 0 and top-p 1. The prompt accepts predictions containing the labeled answer, even with additional explanation, and also asks whether the prediction truly answers the question correctly. No independent-judge or human grading validation is reported in the full PDF. These are model-judged scores under that rubric; this does not establish biased comparisons. Pages 17 and 29 were visually rechecked for this correction. |
| Main baseline access | §5.1 p6 | TF-GRPO: offline trajectories, semantic advantages, global repository. ReasoningBank+: online accumulation, retrieval into system prompt, 235B experience generation. Identical ExpSeek triplets and step-level mentor access not established for either. Exact baseline data/reset protocols and tuning budgets are not fully documented. |
| Trigger/retrieval controls and online overhead | Table3 p7; §6.2 p8 | Rule and Claude-sonnet-4-20250514 receive the generative mentor and one-step silence. Entropy+emb directly retrieves nearest triplet via text-embedding-v4. Steps/time are per-question averages, 8B GAIA/xbench only; table does not separately specify repetitions. Do not extend Table2's five-run statement to this table. |
| Repository transfer | Table4 p8 | Swap agent-specific repositories, not an explicitly transferred whole trigger/mentor stack. Both transferred repositories underperform native ones but outperform no experience. No CI or independent run count specified here. |
| Repository removal | Figure7 and §6.3 p8 | Only qualitative statement used: removal lowers performance and the mentor without the base still helps. No numeric figure labels are used. |
| Splits and budgets | §5.1 p6; AppendixC p17 | 170 questions, 25% per difficulty, random seed0, rest test; library/threshold source is training (also p7). Cross-benchmark evaluation on GAIA/SEAL-HARD/xbench. Agent non-thinking mode, temperature1.0/top-p0.95, 30-step cap, failures beyond cap. Teacher/mentor/judge/Visit summarizer are Qwen3-235B-A22B-Instruct-2507. |
| Tuning/defaults and preparation cost | §5.1 p6; AppendixA pp14–15; §6.4 pp8–9 | 1000 bootstrap samples; LogisticRegression defaults (numerical defaults/software version not specified). Threshold estimation takes seconds per step type, not total repository construction time. GAIA8B sensitivity sweep does not establish an independent default-selection split. No separate split for top-three topics/cooldown/etc.; no TF-GRPO iteration/group sizes or ReasoningBank+ retrieval count/memory cap specified; baseline tuning budgets unreported. |
| Scope limitations | p9 | Thresholds depend on training/tool-model labels; non-web domains/additional tools/RL rollout applications remain untested. |

## ‡ numbers and aggregation reading

- **six‡ / 六‡** is our count of the Table2 component columns that reproduce the printed Avg.: WebWalkerQA Easy, Medium, Hard, GAIA, SEAL and xbench. This is an arithmetic reading of the table, not an explicit averaging-formula statement by the authors. It is not the four-benchmark macro average. For example, the six 8B No Experience entries are 42.67, 40.19, 32.56, 29.13, 23.23, 25.60; their mean rounds to the reported 32.23. The same check reproduces the 8B ExpSeek Avg.41.50 and the 32B Avg.37.79/45.32. No derived numerical mean is published as a new result.
- No figure-label numbers are reproduced anywhere. Figure7 is discussed qualitatively from §6.3; the original chart is not reused. The poster's 9.3/7.5/14.6 improvements are printed by the paper, not new calculations. All other displayed accuracy/step/time decimals are table entries. Integer axis ticks are chart scales, not experimental measurements.

## Fidelity and scope notes

- The headline has broad gains, not a single-benchmark-only win; 32B xbench has the largest reported individual increase, while WW Hard and full-vs-single-stage SEAL comparisons are smaller. No uncertainty is reported, so small differences are not presented as reliable wins.
- On GAIA the Rule and Claude trigger controls outperform entropy in accuracy (38.81/39.47 versus36.89), while entropy takes less time (127.57 s versus329.71/370.82 s). Thus superiority is scoped to the headline baselines, not every variant or every metric.
- A common step cap is not matched realized compute. Table3 reports 8B deployment overhead; it does not establish equal-token/time baseline budgets, total dollar cost, 32B overhead or full offline construction cost. Regressions being fast does not account for teacher trajectory/triplet generation.
- The explicit split prevents direct reuse of the same declared training questions as WW test questions, but does not prove related questions/source pages or cross-benchmark material are disjoint. No contamination/near-duplicate audit is described in the full appendix. ReasoningBank+'s online memory resets are insufficiently specified to reconstruct its evaluation-task exposure. We do not infer confirmed leakage.
- No paper inconsistency is alleged. Some prose generalizations about baseline gains would be too broad if quoted without scope (ReasoningBank+ gains on xbench exceed its overall Avg. gain); we use the relevant model/column values rather than treating broad prose as a contradictory experimental result.

## Judgment notes

Board record: `/home/lingxufeng/ArxivDaily/research/scores.jsonl` gives score63, band★★, evidence level `retained`. Latest matching judgment is `research/judgments/b16.jsonl`; held_out/cross_task/retained_ablation yes; variance/budget_matched/optimizer_cost/improver_comparison/leakage_guard unclear. No judgment files were edited.

Clarifications, not a score revision: Table2 does report five-run means, but not variance; Table3 does report online inference time/steps, but not the complete offline construction/optimizer cost. The `optimizer_cost: unclear` field should not be read as an absence of any cost data. No evidence establishes an improvement mechanism that itself improves; retained is the appropriate displayed evidence level.
