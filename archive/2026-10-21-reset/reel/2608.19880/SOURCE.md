# SOURCE — EnvHarness: Awakening Static Worlds for Agent Learning

Read from: arXiv 2608.19880v1
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed). No paper figure was reused. Our method diagram and results chart are original drawings grounded in the PDF. Exact-version PDF downloaded directly from https://arxiv.org/pdf/2608.19880v1; all 41 pages, including appendices, read with plain/layout pdftotext. Title/author block, workflow and Tables 2/3/10/11 also inspected in rendered pages. Code URL is provided as a link only; no repository code was run.

## Table/page provenance

| Claim | PDF evidence |
|---|---|
| Exact title; author spelling/order | Title block p1: Chengsong Huang, Zifeng Wang, Rujun Han, Jun Yan, Yanfei Chen, Zoey CuiZhu, Ke Jiang, Peng Xia, Han Yu, Yufan Zhuang, Yifei Ming, Jiaqi Pan, Bhavana Dalvi Mishra, Jiaxin Huang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee. Poster abbreviates to Chengsong Huang et al. |
| Stage / Contract / Chain; frozen backend, not frozen exposed responses | §2 pp4–6; interface implementation Appendix C pp21–23; example response manipulation pp27–32 |
| Diagnose/write/validate, native task scoring vs designer acceptance | §3 pp6–7, Appendix A p19, Table 8 and E.3 p26. Five baseline rollouts, five fresh candidate rollouts, at most five write–validate rounds. Acceptance on aggregate metrics by designer; no explicit standard numerical target band. |
| Main model identifiers; retained skills; Chain excluded | §4.1 p8: Gemini-3.1-Flash-Lite, Gemini-3.5-Flash; ReasoningBank extraction. RL is separate. |
| ALFWorld and WebArena main results/SD/run count | Table 2 p9. Three independent runs explicitly stated here only; all SR values shown as percent. Four evaluated WebArena subdomains: Reddit, Shopping, Shop Admin, GitLab. |
| SWE/Office/spreadsheet main results | Table 3 p9; caption gives SD, not explicit repeat count. Steps are steps; SR/EM/Pass@1/F1/Mean Score printed percentage-scale values. Abstract 9.8% fewer steps compares 55.01 to 49.61 (Original Envs), not No Skills 53.58. No new percentage computed. |
| Baseline access/matched quantities | §4.1 p8 and Appendix E.2 p25: common seed tasks, environment count, extraction/retrieval, policy model; same oracle verification access stated collectively. GenEnv simulated environment; VeriEnv recreated executable websites/programmatic rewards; SWE-smith repository instances. No office generation baseline. |
| Splits / original unreshaped evaluation | Table 7/E.1 p25: ALFWorld 100 train; WebArena 20 train per subdomain; SWE 100 Lite train and 407 Verified-not-Lite test; OfficeQA 50 train/172 test; SpreadsheetBench 100 of 400 verified train/299 held-out tasks, 897 instances. We flag the latter unexplained split arithmetic neutrally, without inventing a cause. ALFWorld seen/unseen are native configuration-based splits. |
| Chain comparison | Table 5 pp10–11: standard single-environment test issues, not chained-test success. No variance/run count in table. Main Stage/Contract row kept within this table for the comparison. |
| Environment scaling | §5 p11 prose: 300 environments, 15 skills, 54.79/52.13/50.37 success rates. These numbers are printed in text, not read from Figure 5 labels. Current-skilled-policy conditioning only for EnvHarness; baselines sample independently. |
| Backbone-specific regeneration | Table 9/F.4 pp33–34. Model names copied from this table: Gemini 3.1 Flash-Lite, Qwen3.6 27B, Gemini 3.5 Flash, Claude Sonnet 4.6. No donor-skill transfer claimed. Averages without variance/CI in this table. |
| Leave-one-type-out transfer; concentrated benefit | Table 10/Appendix G p35. Average 60.6→63.7; clean +16.4, heat −8.7, simple tie, cool +0.8 all printed. No variance/CI. No newly computed win count. |
| Generation cost | Table 11/Appendix G p35: design/rollout/total token triplets, units K or M kept on every component. Estimated quantities; real rollouts for EnvHarness/VeriEnv vs simulated GenEnv rollouts are different work. Tables do not provide SWE-smith/Original Envs totals, money or wall-clock. Appendix H p41 says cost once per environment, not per training episode. |
| Objective-targeting diagnostic vs standard loop | Table 12/Appendix G p36 gives explicit SR [0.4, 0.6] and successful-episode steps [25,35] with K=10; not a documented standard acceptance band. We do not substitute these into the main loop. |
| RL result and reproducibility | Table 4 p10, F.1 pp26–27: Qwen3-8B-base / GRPO; seed 0, 150 epochs/steps, 8 H100 GPUs. OOD regression 89.6→88.8; no variance/CI. Seed 0 does not prove complete-run count. |
| Rejected candidates / limits | F.2 pp31–32 (about a third of round-3 training tasks yield no accepted component), H/I p41 (cost, resettable textual interface, serial implemented Chain). |

## ‡ numbers and figure-label reads

None. All reported numerical values are printed in PDF prose or tables. No computed deltas, inferred task counts, figure-label percentages, or figure-label model scores are used. Chart positions are drawn from Table 2/3 means; chart tick marks are plotting scales, not extra experimental measurements.

## Interpretation boundaries and unreported controls

- The largest main-table improvement (+9.0 points) is ALFWorld OOD, not a benchmark-wide average. Shop Admin has the largest WebArena subdomain gain. Leave-one-type-out improvement is concentrated in clean, with heat regressing and simple unchanged.
- Table 2 explicitly establishes three independent runs. Table 3 provides SDs but no explicit repeat count in its caption or experimental appendix. We do not call the headline tables a chosen single seed/best checkpoint: the paper provides no such statement. Tables 5/9/10 do not give variance/CI or run counts. No significance is inferred from overlapping SDs.
- Baseline environment counts are matched; diversity and all rollout compute are not. The close WebArena token totals do not establish global compute parity. No baseline-with-EnvRigger wrapper-generation gate is reported. Original Envs controls the environment source, not designer tuning effort.
- Table 8 defaults are shared, but no tuning/selection split is named. Baseline tuning budgets/search are unreported. Missing numerical settings are separately identified: standard target success band, skill-learning decoding temperature and episode cap, RL learning rate. Numerous other RL settings are supplied; we do not describe all hyperparameters as missing.
- Training-only generation and the Lite/Verified exclusion are reported leakage safeguards, not a semantic duplication or pretraining contamination audit. No such audit was found in the full appendix.
- No separate Stage/Contract, no-diagnosis or no-validation ablation is reported; Chain is random-paired outside EnvRigger and its skills are tested on single environments. This does not prove the generator improves its own optimization mechanism.
- General Chain routing examples are distinguished from the serial composition actually evaluated and its limitations. No keep-rule initialization/pseudocode disagreement was identified. We do not assert a text/table numerical inconsistency from differing controls across experiments.

## Judgment notes

Published score record: `research/scores.jsonl`, score 63, band ★★, evidence level `retained`. Latest paper judgment found: `research/judgments/b23.jsonl`, version v1.

- `variance: unclear` is incomplete against the full paper: Table 2 explicitly supplies three independent runs with SDs, and Table 3 provides SDs (repeat count not explicitly stated).
- `cross_task: unclear` misses Appendix G/Table 10 leave-one-task-type-out evaluation. Backbone-specific regeneration is an additional robustness test, not donor transfer.
- `optimizer_cost: unclear` misses Appendix G/Table 11 estimated design and rollout tokens on ALFWorld/WebArena. Dollar/wall-clock cost and all-domain totals remain absent.
- `budget_matched: partial` remains appropriate: matched environment count/common extraction plus near-equal WebArena tokens, but substantially different ALFWorld totals and different rollout grounding.
- The judgment's `improver_comparison: yes` quote compares environment sources, not a no-diagnosis/no-validation optimizer control. Our write-up does not promote that to self-improver-level causal evidence; published level remains retained.

These are full-paper clarification notes, not a rescoring. No score, judgment, candidate or shared-library file was changed.
