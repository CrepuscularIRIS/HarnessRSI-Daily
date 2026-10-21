# SOURCE — OPD-Evolver

Read from: arXiv 2606.17628v1
Paper figures shown: none

Exact PDF title: **OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation**.
Authors, in PDF title-block order: Guibin Zhang, Xun Xu, Yanwei Yue, Zikun Su, Wangchunshu Zhou, Xiaobin Hu, Shuicheng Yan.

Downloaded the exact version from https://arxiv.org/pdf/2606.17628v1 to `/home/lingxufeng/reel-work/2606.17628/paper.pdf`. Read all 17 pages including appendices A–G, using both plain and layout text. Visually checked PDF pages 6, 7, 13 and 14 for tables, evaluation protocols and training settings. The poster's method diagram and numerical charts/tables are original redraws, not extracted paper figures. Figure reuse was permitted by the task but not used. No paper/repository code was run. Code link supplied in task: https://github.com/bingreeky/opd-evolver.

## Page and table provenance

| Claim / asset | Source in the exact PDF |
|---|---|
| Title, author order, affiliations | p1 title block |
| Fast loop retains trajectories, tips, skills, tools; fixed weights online | pp3–4, §3.1–3.2, Eqs2–10 |
| Agent-controlled writing, lookup/merge/delete maintenance | p4, Eqs9–10; p6 Algorithm1 |
| Candidate-controlled selected/not-selected reward comparison, tier and confidence weighting | p5, §3.3, Eqs11–12 |
| Same-policy privileged teacher, stop-gradient, student prefixes, full-vocabulary token KL | p5, Eqs13–16 |
| Teacher execution sees useful memories and successful same-group trajectory; student execution without memory | p5 Eq13 and following prose |
| Model identifiers, 50 candidates, 20 teacher memories, threshold 0.01, Q=30 | p5 §4.1; pp13–14 Appendix D.2 |
| Writer-side top30% selection; GPU hardware | p14 Appendix D.2, OPD-Evolver paragraph |
| All headline table values, per-column strongest memory comparator, giant-model exceptions | p6 Table1; pp6–7 §4.2 |
| Additional MiniHack training for all Table2 methods | p13 Appendix C.1 and D.1 |
| Training-method comparison and Room exception; author claim of best average | p7 Table2 and §4.2; aggregate itself not numerically tabulated |
| Full ablation percentages and variant meanings | p7 Table3 and §4.3 |
| Memory-free execution diagnostic | p8 Figure4 and §4.4 prose; no figure-label values copied |
| Evaluated subsets and sizes | pp12–13 Appendix C; not full AMA/MemoryArena benchmarks |
| Empty evaluation memory, same environment feedback, no answers/expert solutions | p13 Appendix C.1; also p6 baselines paragraph |
| Main 7,000-task training collection, source counts | p13 Appendix D.1; disjointness claim p5 §4.1 |
| SFT/GRPO settings | p13 Appendix D.2 |
| MemRL, SkillZero, ComplementaryRL settings and access | p14 Appendix D.2 |
| Score 63, band ★★, retained | `/home/lingxufeng/ArxivDaily/research/scores.jsonl`, paper row |
| Existing evidence judgments | `/home/lingxufeng/ArxivDaily/research/judgments/b03.jsonl`, paper row (only matching batch found) |

## Poster chart provenance

Main horizontal chart is a selected view of Table1's Qwen3.5-9B group, task-success metric in percent. Every pair is within Table1, not a comparison across tables.

| Subset | OPD-Evolver-9B | Highest memory baseline in that column |
|---|---:|---|
| LifelongAgentBench OS | 65.00 | MemEvolve 61.00 |
| MemoryArena Math | 10.88 | ExpeL 8.19 |
| MemoryArena Physics | 11.63 | AWM 11.05 |
| AMA-Bench State Abstraction | 52.92 | AWM 48.00 |
| InterCode CTF | 57.00 | MemEvolve 53.00 |

The blogs supply all Table1 9B subsets, including DB, Causal Inference, State Updating and SQL. The diagram is a conceptual redraw of §§3.2–3.3, not a claim that Algorithm1 alternates slow training after each evaluation task. It explicitly separates training from fixed-weight evaluation.

## ‡ numbers / figure-label readings

All task-success decimals come directly from Tables1–3; no numeric figure-label readings are used. **‡ marks conditional task-count reconstructions**, not author-reported outcomes: Appendix C (p13) states 51 test tasks per MiniHack environment. If each task were evaluated once, Room 50/51 versus 51/51‡ and Maze 14/51 versus 13/51‡ reproduce Table2's 98.04% versus 100.00% and 27.45% versus 25.49%, respectively, after rounding. Each difference is one task‡. The paper does not identify a single-pass protocol, so these counts must not be treated as observed run outcomes.

For the denominator compatibility check, enumerate integer successes from zero through 51 and round `100 × integer successes / 51` to two decimals. Compatible Room/Maze/KeyRoom counts‡ are: Vanilla 41/10/0; SFT 42/9/0; GRPO 51/12/2; Skill0 48/13/2; MemRL 49/10/1; OPD-Evolver 50/14/5. These are arithmetic reconstructions only. None of Complementary RL's printed 96.88 / 20.85 / 5.16% matches such an integer count. No averaging/repeated-run rule or alternative denominator is specified to resolve this; we preserve the printed percentages and do not infer the cause.

Counts of wins repeated from the authors' prose are not independently computed counts. Chart axis ticks are scale guides, not empirical measurements. Section/panel numbers and the score are not experimental results.

## Protocol and interpretation notes

- Tables1 and2 have distinct comparisons/protocol descriptions. Table2 additionally trains on MiniHack; its InterCode values must not be silently mapped onto Table1's columns. We quote each table literally and do not call their different rows an unresolved numerical inconsistency. Table2 does not print per-row backbone identifiers; Appendix D.2's defaults and method-specific identifiers do not justify labeling all rows uniformly 9B.
- Table1 caption expands AMA “SA” as “State Updating,” whereas §4.1 and Appendix C distinguish State Updating from State Abstraction. We use **State Abstraction** for SA, following the explicit taxonomy and benchmark description.
- No repeated-run/seed counts, task-order variability, CIs or SDs are provided for Tables1–3. We do not infer single runs, a mean, best-seed selection or significance. Table2 prose says best average but does not give a numerical aggregate or aggregation rule.
- Appendix C.1 says no reference answers/expert solutions are given after evaluation tasks; this does not deny that the environment supplies pass/fail feedback, or that AMA examples include action-observation trajectories as task input. Empty initial memory and disjoint main training sources are stated safeguards, not an empirical contamination audit.
- Extra MiniHack training in Table2 is an explicitly described within-benchmark training regime, not covered by an unqualified claim that every training source is benchmark-disjoint. Appendix C.1/D.1 (p13) establishes the same training data and test tasks across methods, not an explicit guarantee of disjoint training/test instances. The train/test partition, additional training-set size and seed-level overlap are unspecified.
- During online evaluation earlier task-specific experience may persist and help related later evaluation tasks. This is the streaming adaptation protocol, not necessarily illicit leakage; absence of a near-duplicate/content audit limits what can be claimed.
- Eq6 retrieves top-K per tier. Appendix D.2 specifically describes teacher retrieval of 50 candidates then selection of20. We avoid inferring a combined candidate count or a student selection cap. D.2's writer-side top30% filter is stated, while Algorithm1 writes per tier without spelling out this filter. The text does not fully resolve its placement in every online repository update. We report both rather than assume a hidden gate.
- No held-out gate or rollback condition for every edit is described; the learned policy writes/merges/deletes. No disagreement on initialization is asserted: Algorithm1 accepts a generic M0, while the evaluation-specific protocol explicitly sets M0 empty.
- Hyperparameter selection split, search budgets and checkpoint selection are unreported. Separately missing OPD numerical settings include learning rate, batch size, epochs/steps and tier priors. Baseline numerical settings exist (D.2); no matched-total-compute or timing/token/dollar cost table exists. Hardware count alone is not an evolution-cost measurement.
- Baseline access is stated per family/method in the blogs. We do not assert that all baselines lack memory, skills, weight updates or evolution. We only say the paper does not document granting Table1 baselines the same unified hindsight distillation, and does not show matched total training/evolution budgets.
- “Candidate-controlled, not randomized causal identification” is explicitly our reading of the attribution design, not a claim made by the paper.

## Judgment notes

Existing b03 labels: `held_out: yes`, `cross_task: yes`, `improver_comparison: yes`; `variance`, `budget_matched`, `optimizer_cost`, `retained_ablation`, `leakage_guard` are `unclear`. Score63 and `retained` are preserved.

The full PDF adds evidence missing from the condensed `retained_ablation: unclear` judgment: Table3 removes slow evolution, attribution, selection, writing distillation and maintenance training; Figure4 tests execution without external memory. These are meaningful component/retention-related controls. They do not supply matched-compute proof, seed variance or an artifact leakage audit. The `held_out: yes` source-disjointness quote also needs its Table2 MiniHack training exception and streaming evaluation context, both disclosed in the blogs. No score or judgment file was edited.
