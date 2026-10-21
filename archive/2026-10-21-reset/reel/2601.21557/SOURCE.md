# SOURCE — Meta Context Engineering via Agentic Skill Evolution

Read from: arXiv 2601.21557v2
Paper figures shown: none

Exact-version PDF downloaded directly from https://arxiv.org/pdf/2601.21557v2 into `/home/lingxufeng/reel-work/2601.21557/paper.pdf`. Title and author order copied from its title block: Haoran Ye, Xuning He, Vincent Arak, Haonan Dong, Guojie Song. Affiliation: Peking University. Full paper and appendix read, including prompts, learned skill, case studies and utility listings. Layout and plain text extracted; PDF pages containing Tables 1–4 inspected visually.

Figure reuse is forbidden for this assignment. All poster visuals are our own diagram, bars and table from the paper's method and numbers. No paper image, crop or traced figure is used. No external abstract, blog or code repository was used as evidence; no paper code was run. No code QR/link is included, per assignment metadata.

## Table/page provenance

| Claim / content | Evidence in this PDF |
|---|---|
| Skill folders, scripts, templates, validation protocols, retrieval operators; frozen models | §3.1–3.3, pp5–6; Appendix B, pp21–26; Appendix C, pp26–31 |
| History-informed crossover; empty initialization; warm-start best context; archive all, validation argmax retain; tie unspecified | Algorithm 1 and §3.4, p6; §3.3, p5; meta/base prompts, pp21–26 |
| Generator / reflector DeepSeek V3.1, AEGIS Qwen3-8B, agentic model MiniMax M2.1; five epochs; one-shot interface | §4.1, p7 |
| Every offline and online result in blogs/poster, base scores and average relative gains | Table 1, p8 |
| Strongest offline baseline per column: ACE 71.0/18.0, ICL 84.4, GEPA 0.69/0.76 | Table 1, p8; inspected complete baseline rows, not just ACE |
| Context transfer, excluded benchmarks, Gemma 65.0/64.0 and 0.03/0.00/base 0.01; 172.6% relative average | Table 2 and caption, p8; §4.2.2, p9 |
| FiNER skill/no-skill/fixed/evolving ablation, no full online evolution | Table 3 and §4.3, p10; online Table 1 MCE is fixed-skill, not full iterative evolution |
| ACE model-swap final 67 vs 70; checkpoints and window-stop explanation | Table 4 and §4.3, p10 |
| 1.9h, 25.8h, 13.6×; 450 rollouts/95% vs 2169/94%, 4.8× | Explicit prose §4.2.3, pp9–10; Figure 4 caption on p9 says MCE counts both training and validation inference. No numerical value was sourced solely from figure labels. |
| Baseline-by-baseline access and budget settings | §4.1, p7: zero-shot prompt/no context; ICL fitting demos; MIPROv2 official heavy; GEPA official heavy plus rollout matching; DC cumulative; ACE original settings/up to five epochs with window/validation stop; common starting templates and general training-budget guarantee |
| Train/validation/test counts and data restrictions | Appendix A.1 pp16–17 (FiNER); A.2 pp17–18 (USPTO); A.3 pp18–19 (Symptom); A.4 p19 (Law); A.5 pp20–21 (AEGIS) |
| Close symptom train/test descriptions, example-based learning and keyword routing | Appendix D.3, pp35–38; concrete training examples also in C/D.1/D.2 |
| LawBench criminal charge prediction; AEGIS selected four worst-performing risk categories, binary safety F1 (unsafe positive), test 70 unsafe + 70 safe; category-selection split unspecified | Appendix A.4, p19; A.5, p20 |
| USPTO single-step retrosynthesis supplies product SMILES and reaction type; reaction-type-stratified sampling | Appendix A.2, pp17–18; explicit question specification on p18 |
| Utility temperature zero only, DeepSeek utility model and text-embedding-3-small | Appendix E, pp43–46; do not generalize utility temperature to task-model decoding |
| Reasoning-intensive / complex long-trajectory limitations; cross-task skill transfer future work | §5, pp10–11 |

## ‡ numbers and figure-label reads

None. No calculated numerical differences, computed task counts, or figure-label-only values appear in the delivered blogs or poster. All result decimals and cost numbers are explicitly printed in the paper's tables or prose. The bars show the published numbers with accuracy and F1 scales separated and stated; F1 values were not converted to percentages. Method step numbering is our organization, not an experimental count.

The relative-gain denominator observation is explicitly labelled our reading: Table 1 defines the statistic as the mean of per-benchmark relative improvements over base. USPTO's base is 6.0 and MCE 20.0. We do not present a recomputed contribution or pooled accuracy. Similarly, online benefits being concentrated on USPTO is our comparison of the fixed-skill/no-skill rows, not an author-reported statistical significance claim.

## Scope and missing evidence checked

- Tables 1–4 do not state run/seed counts, SDs, CIs or a seed/checkpoint identity for the main table. We do not infer single runs. The paper's phrase about fixed-skill variance across tasks is not repeated-run variance.
- The numerical adoption gate is validation performance. No LLM correctness judge or contain-the-answer acceptance rule is specified. Task metrics are label-based; the listed LLM utility calls perform analysis/context generation. LawBench's task specification describes exact set match whereas the results and dataset evaluation prose specify micro-F1; delivered material consistently follows the reported micro-F1 metric, without speculating about executed evaluation code.
- Algorithm 1's empty initial state and prompt warm-start from the previous best are compatible after initialization. No conflicting keep/reject implementation is asserted. Argmax does not specify tie-breaking.
- The validation split is explicitly used to select context, and ACE may stop on validation. Which split selected global defaults/hyperparameters is not stated. This is separate from missing numerical settings: generator-wide temperature/output-token limit, actual batch/iteration schedule beyond five epochs and ACE's numerical plateau criterion. Per-baseline hyperparameter-search trial budgets are not provided, although heavy presets, epoch limits and explicit GEPA rollout matching are given.
- Common initial prompts/data/budget statements do not mean that every baseline receives learned MCE skills, the same filesystem optimizer or equal all-in dollars/tokens. MiniMax reflector/curator substitution in ACE does not grant the full MCE mechanism. Its lower final score is scoped to that control; we do not repeat the paper's global assertion that it rules out knowledge transfer.
- Table 1 ACE FiNER is 71.0; Table 4's final DeepSeek checkpoint is 70 (with Epoch 1 at 71). Both variants/checkpoints were checked; this is not called an inconsistency.
- Cross-model context transfer in Table 2 is not cross-task skill transfer. Online first-inference scoring plus continual learning on processed test instances is not untouched offline holdout.
- Full appendix checked for empirical held-out-label, duplicate/near-duplicate audits: none reported. Access scoping is a design constraint, not such an audit. Training-example encoding and near-neighbor matching are possible mechanisms, not evidence that evaluation labels leaked. AEGIS category-selection split is unspecified, not asserted to be test.
- FiNER cost is a reported end-to-end training comparison, not an optimizer-only cost ledger. No per-task dollar/token table or repeated timings. Rollout matching does not establish all-method total-compute parity.

## Judgment notes

Current score record: 63, band ★★, evidence level `improver`. Latest matching judgment: `research/judgments/b18.jsonl` (v2). No judgment or score file was edited.

- `budget_matched: yes` is supported by explicit GEPA total-rollout matching and the broad baseline training-budget statement. Delivered interpretation distinguishes these from equal all-method total compute and from tuning-search accounting.
- `retained_ablation: unclear`: full PDF Table 3 does compare the evolved-skill system with fixed/no-skill retained-context variants on FiNER. We report this evidence narrowly rather than treating it as absent or general across domains.
- `cross_task: unclear`: consistent with context transfer across generator models only; cross-task skill transfer is future work.
- Metadata has code score zero / no code URL, and the assignment specifies code none. PDF p1 does announce a GitHub repository. We did not inspect it, change metadata or represent the absence of an assignment code link as a claim that no repository exists.

## Independent fact-check corrections

All four findings accepted after direct PDF verification: restricted LawBench/AEGIS scope (pp19–20), supplied USPTO reaction type (p18), author-attributed reasoning/long-trajectory cautions rather than measured failures (§5, pp10–11), and both fixed/no-skill online variants (§4.1 p7; Tables 1/3 pp8/10). Bilingual text and poster updated; numerical results unchanged. No findings rejected.

## Rendering checks

House-style Python renderer used without library modifications. Final poster is 2400×1440; no card OVERFLOW. Actual rendered SVG font measurements: method text above 22px and chart labels above 18px. HTML body/captions are at least 22px. Visual inspection performed on the rendered PNG; arrows occupy gaps, chart labels and values do not overlap bars/headings. No external publishing or git operations performed.
