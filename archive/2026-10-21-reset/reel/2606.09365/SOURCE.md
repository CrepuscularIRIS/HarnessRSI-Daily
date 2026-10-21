# SOURCE — SkeMex

Read from: arXiv 2606.09365v4
Paper figures shown: none

Exact PDF title: **Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory**.

Authors, PDF title-block order: Haoran Sun, Wenjie Li, Yujie Zhang, Zekai Lin, Fanrui Zhang, Kaitao Chen, Xingqi He, Yichen Li, Mianxin Liu, Lei Liu, Yankai Jiang. Affiliations: Fudan University; Shanghai Artificial Intelligence Laboratory; University of Science and Technology of China; Huazhong University of Science and Technology.

Paper: https://arxiv.org/abs/2606.09365v4
Code link supplied in the task and printed in the PDF: https://github.com/manglu097/SkeMex
License recorded in reel/candidates.jsonl: CC BY 4.0. Figure reuse was permitted, but all poster diagrams and charts are our own drawings from paper facts. No paper image or figure is reproduced. No code from the paper repository was run.

## Reading and provenance

The exact PDF was downloaded afresh, replacing the stopped run's copy. All 66 pages, including appendices and checklist, were read through fresh layout text; plain text was also consulted. PDF pages 8–10 were rendered and visually inspected to verify the result tables and figure labels. Prior drafts were not used. Work notes: `/home/lingxufeng/reel-work/2606.09365/facts.md`.

| Claim / numbers | PDF location |
|---|---|
| Full title, authors, code URL | p1 title block and abstract |
| External skill repository; fixed weights; general/task/action branches | §§3.1–3.2, pp3–5 |
| Once-per-episode category-aware retrieval and fixed injected skills | §3.3 p5; A.3 p19; Algorithm 1 p24 |
| Trajectory gating, analysis/mutation, CREATE/PATCH/NONE, review | §3.4 pp5–6; Appendix F p31; prompt figures 24–27 pp54–57 |
| Category-relative reward/adoption utility | §3.5 p6; Appendix F p31; analysis prompts pp54–55 |
| Seven-step budget; six retrieved skills; thirty-trajectory window; twenty retained traces; new skill utility | Appendix F pp30–31; Table 11 p32 |
| Two-window governance; deprecation below 0.3; mature threshold 0.75 and 15 uses; branch capacities | Appendix F p31 |
| Shared executor, prompts/tools/permissions, experience split, baseline adaptation | §4.1 p7; Appendix E.1 pp27–28 |
| Offline ID averages and individual baseline/SkeMex cells | Table 1 p8 |
| Online lifecycle ablations and their five-configuration average | Table 2 p9, §§4.2–4.3 pp7–9 |
| Buffer, encoding, branch controls | Tables 4–5 p9 |
| Three online epochs, means, exceptions | Table 3 p10 |
| Additional retrieval/governance controls | Tables 12–13 pp34–35 |
| Preprocessing, preference for difficult cases, near-duplicate removal | Appendix D p25 |
| Full processed-subset category distributions, not test-label proportions | Table 9 p26 |
| Exact ID training/test and OOD test counts | Table 10 p30; Appendix F pp29–30 |
| Reset local conversation/step history for each sample | Appendix A.1 p18 |
| Ground-truth/rubric feedback to writer; scoring; invalid input exclusions and unparsable predictions | Appendix E.2 pp29; Appendix C p23; Figures 24–25 pp54–55 |
| DeepSeek-to-Qwen-Plus frozen repository, no rewriting | §4.1 p7; Appendix F p30 |
| Offline OOD averages, strongest baselines, concentration on AgentClinic-Text, MedJourney loss | Table 14 p36; I.1 pp36–37 |
| Frozen DeepSeek repository consumed by Claude Sonnet-4.6 and Qwen3.6-35B-A3B, including losses | Table 15 and I.3 pp39–40 |
| Extra backbone evaluations distinct from fixed-donor transfer | I.2 pp37–39 |
| Mean interaction steps and approximate inference seconds, including HealthBench exception | Tables 16–17 pp41–42; I.4 pp40–41 |
| Sensitivity studies, not repeated-run variance | Appendix G pp32–34 |
| Separate training-order experiment | Appendix I.5 / Table 18 p43 |
| Clinical/generalization/cost limitations, oversight | Appendix J pp43–44 |
| No statistical-significance tests; no stated seed or repeated-run count per headline cell | Checklist item 7 p62, checked against experiments and appendices |

## ‡ numbers

None. No newly computed decimal gains or ratios are used. The poster chart transcribes reported benchmark averages directly; its axis ticks are integer scale markers. All decimal scores, thresholds and times in the blogs appear in this PDF. The band and score are repository judgments, not paper metrics.

## Protocol and interpretation notes

- **No claim that evaluated traces enter the offline library:** the paper explicitly restricts offline skill accumulation to training cases, freezes memory during tests, reserves OOD families for testing and removes cross-split near-duplicates. The writer's access to answers/rubric failures concerns accumulation data. There is no reported quantitative residual-contamination audit or matching-threshold detail. Resetting case-local conversation history is not the same as resetting persistent skill memory.
- **Online is not that protocol:** Table 3 updates memory while processing benchmark streams and reports three epochs. Earlier scored stream trajectories may inform later memory. The paper does not sufficiently specify whether successive epochs revisit the same cases, the split/reshuffling/reset policies or the precise scoring/update ordering to certify a clean held-out interpretation. We flag uncertainty; we do not assert that offline held-out evaluation is leaked, or claim proven online contamination.
- Table 2 is explicitly discussed as an **online** lifecycle ablation on five configurations, including AgentClinic-Text. It should not be compared as an identical average to Table 1's seven offline ID configurations or Table 14's frozen OOD setting.
- Transfer shares the fixed source repository; target-side distillation/writing is not performed in the reported frozen transfer setup. We do not infer that unrelated local state is shared, or that all source datasets are necessarily pooled in one library. The precise combined-versus-per-dataset construction is not fully described.
- Baselines get the same execution setup and accumulation split, but use their original or adapted memory mechanisms. No separate experiment adds SkeMex's valuation/governance module to each competing baseline. Same upper inference budget is not equal realized computation or equal donor/repository-construction cost.
- Category counts in Table 9 refer to **full processed pools**. Test counts are explicitly reported in Table 10; none are reconstructed by us. The evaluation excludes missing-input/invalid benchmark records; unparsable answers count as wrong. Maximum-step failures are filtered out of skill writing; that does not establish their exclusion from evaluation denominators.
- **Unresolved same-setting OOD disagreement:** §4.2 p7 calls about +8.24 the gain of the strongest competing memory baseline for DeepSeek offline OOD. Table 14 p36 instead reports **Evolver 70.35 / +8.34**, above **GM 70.25 / +8.24**. Figure 3 p9 explicitly covers DeepSeek offline OOD and includes both Evolver and GenerativeMemory; it plots Evolver below GM in the average panel. Its MedJourney panel also plots Evolver below GM, whereas Table 14 has **Evolver 78.79 versus GM 72.73**, above SkeMex 76.52. Appendix I.1 pp36–37 describes Table 14 as complementing Figure 3 in this setting; no different model/epoch/transfer variant explains the disagreement in the PDF. We use Table 14 for the OOD comparator and MedJourney exception, explicitly flag the disagreement in both blogs and poster, and cannot resolve it from the paper. Our prior suggestion that the text might refer to a plotted subset was unsupported and has been removed. No numerical value has been estimated from Figure 3.
- Table 18's training-order default has HealthBench 31.42 and LiveMedBench 58.63, whereas Table 1 has 27.65 and 57.95. We treat it as a separate reported experiment, not a variance estimate or replacement headline, because its relation to the main run is not clarified.
- Main tables give benchmark averages without SD/SE/CI. Run count, seed and checkpoint choice are unstated; we deliberately do not infer “single run.” No statistical-superiority claim is made for small margins. The checklist explicitly declines statistical-significance tests.
- **Unspecified selection and baseline tuning:** Appendix F pp29–32 / Table 11 lists defaults; Appendix G pp32–34 varies hyperparameters on HealthBench and LiveMedBench, but does not identify the default-selection split or an independent validation protocol. Appendix E pp27–28 describes baseline adaptations and shared accumulation data, not baseline tuning procedures or matched tuning budgets. Whole-PDF searches for validation, tuning, hyperparameter and selection descriptions (including checklist item 6 p62) supply no missing selection protocol. Thus selection-independent evaluation and equally tuned comparisons are not established; this is not evidence that test-set tuning occurred.
- Inference time and steps are not complete improvement costs. The paper does not itemize total repository construction, donor model calls, dollar or token budgets; no equal-total-compute comparison is established.
- Skill content/novelty review and utility promotion are not held-out candidate acceptance tests. Adoption attribution is model-judged from trajectories; calling it non-randomized attribution is our interpretation of the stated procedure.

## Judgment notes

Repository score: **67**, band **★★**, evidence level **retained**, from `research/scores.jsonl`. Latest matching judgment: `research/judgments/b14.jsonl` (no later matching record found).

The stored judgment marks held-out/cross-task evidence yes, budget matching partial, variance and optimizer cost unclear, leakage guard unclear. The full PDF supports held-out/frozen transfer and partial matched-inference ablations, but **does describe offline near-duplicate removal and split exclusion** (Appendix D p25, F pp29–30). Thus the leakage-guard field is incomplete relative to the safeguards stated in this version. This does not establish a quantitative leakage audit, and online epoch-case reuse remains unclear. We record the distinction here; no score or judgment file was changed. Evidence remains described as retained, not improver: the retained memory improves later task solving, without an experiment establishing that a modified improvement algorithm produces better subsequent improvements at comparable total budget.
