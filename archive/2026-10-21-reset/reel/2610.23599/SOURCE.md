# SOURCE — From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents

Read from: arXiv 2610.23599v1
Paper figures shown: none

License: CC BY 4.0, per the Reel candidate record; figure reuse is allowed, but none was used. The method diagram and result chart were drawn by us from the paper. Exact-version PDF downloaded directly from https://arxiv.org/pdf/2610.23599v1 and read in full, including appendices through PDF page 22. PDF title block confirms the exact title and author order: Yewei Zhao, Derong Xu, Wei Chen, Yin Xu, Peilun Zhou, Xiaohan Wang, Guojun Yin, Wei Lin, Mingjun Xiao.

## Table/page provenance

| Content in blogs/poster | PDF source |
|---|---|
| Persistent four-component skill; fixed weights and update protocol; trace-grounded semantic gradients | §§3.1–3.4, pp3–5; Appendix G, pp15–17 |
| Runtime filtering, success/failure analysis, exact trace-line evidence; core + at most two lessons + one script suggestion | G.1, pp15–16 |
| Retention and functional-role ownership, one primary/at most one secondary | §3.3, pp4–5; G.2, p16; router prompt Appendix I, pp21–22 |
| Atomic rule maintenance, capability categories, deterministic Script contracts, self-test/independent verification/one bounded repair | §3.4, p5; G.3, pp16–17 |
| Publication fails on coordination/description-validation failure; checks are edit contracts, not a performance-improvement gate; descriptions visible before loading | G.3, p17; §4.3, pp6–7; Appendix D, p13 |
| All 36 settings; macro-average gains 7.6 and 2.6 pp; after three evolution rounds | Abstract p1; §§4.1–4.2 and Table 1, pp5–6; H.2, pp17–18 |
| Chart: GLM-5.2/Claude Code scores and strongest competing method per column | Table 1, p6: OfficeQA 77.2 vs SkillOpt-lite 76.4; SpreadsheetBench2 30.7 vs Trace2Skill 28.3; SealQA 54.1 vs EvoSkill 52.4; LiveMathBench 87.7 vs SkillOpt-lite 85.0; SWE-Pro 68.4 vs SkillOpt-lite 63.1; AutomationBench 32.9 vs EvoSkill 25.5 |
| Small margins and cross-harness concentration of Automation gains | Table 1, p6; MiniMax-M3/Codex Spreadsheet 29.4 vs SkillOpt-lite 29.1; Automation deltas printed in table: Claude +12.1/+14.6/+10.9 versus Codex +4.9/+8.4/+5.5 for GLM/DeepSeek/MiniMax |
| Mechanism ablations, including same-gradients no-differentiation control | Table 3 and §4.6, p8; Appendix E, p14 |
| Cross-benchmark Meta 9/10, mean 3.6 pp; negative Script transfer and zero Meta transfer | §4.5, p7; Table 2, p8; Appendix D, pp12–13 |
| Cross-model 11/12, mean 4.2 pp for each receiver; cross-harness 12/12, 3.3/3.4 pp | §4.5, p7; Tables 11–12 and Appendix D, pp13–14. GLM/DeepSeek exchanges fix Claude Code; harness exchanges fix GLM. DeepSeek SealQA: Base51.8/native59.4/transferred48.5 |
| Multi-round fixed corpus; GLM R2→R3 regressions Office77.8→77.2/SWE69.0→68.4/Automation33.3→32.9 | §4.4, p7; Appendix C and Table 8, p12. Table 1 is R3, not a claimed best checkpoint. Figure 7 caption p13 says one reported score per round, not one run or seed |
| Single-round input/output totals and efficiency, GLM-5.2/Claude Code only | Tables 4–5, pp8,11; Table 6, p12. Exact totals retained as printed: 50.90/2.800, 127.80/5.800, 24.70/1.100 million tokens. Ratios 7.60/15.04/2.19 use same-round gains; OfficeQA SkillOpt-lite6.64 vs CDSE7.87 comes from Table 6 |
| Selected collections and 2:7 train:test split; training trajectories, test scores | §4.1 p5; H.1–H.2, pp17–18; Table 17 p18 |
| Baseline access, initialization statement and outer rounds | §§4.1–4.2 pp5–6; H.2 pp17–18 |
| Trace2Skill Error+Success; EvoSkill error-only/1.5 epochs/frontier3; SkillOpt-lite10 rounds/batch10; original-method defaults | H.6, p21 |
| Scoring/turn-limit/judge configuration, mentioned runtime bounds without numerical values | H.3–H.5, pp18–21 |
| Fixed-corpus limitation; alternative decompositions not studied | Limitations p9; Appendix C p12 |
| Supplementary code/prompts statement, not a public code URL | Appendix I p21 |

## ‡ numbers

None. No computed differences, table-derived win counts or figure-label values are used in the deliverables. Counts such as 36 settings, 11 of 12 transfer settings and 9 of 10 component-transfer pairs are stated in the paper's prose. The poster axis ticks are drawing aids, not measured paper results. Figure 4 was visually checked but its label-only numbers and percentages are intentionally not quoted. All performance values shown come from tables or prose.

## Evidence and scope notes

- Table 1 reports macro-averaged percentage-point changes across heterogeneous benchmark metrics, not pooled accuracy, and provides no SD/CI or run/seed counts. Table 3 likewise provides no uncertainty/run counts. We do not infer single-run experiments. Figure 7's “one reported score” caption is scoped to its curves and is not a seed-count statement.
- The training/test split comes from the same selected benchmark collections. The PDF gives neither exact split counts nor split seeds/grouping/dedup audits; it does not establish repository- or domain-disjoint testing. This is not evidence of actual leakage. The router's answer-specificity filter and exact provenance are preventive design elements, not empirical contamination tests.
- The paper reports no split used to choose defaults/hyperparameters and no separate development split or baseline tuning budgets. These absences do not prove test-set tuning. Separately missing numerical settings include rule/category capacities, runtime bounds and evolution decoding settings; the evolution-model identity and initialization contents are unspecified. Judge decoding and several task-agent turn limits are specified.
- Access is shared per model–harness block for the named skill baselines, but CDSE's differentiated library/router/validation machinery is not stated as supplied to them. The same semantic gradients are explicitly supplied to the no-differentiation ablation. We do not describe any baseline as weakened.
- Script verification checks executable correctness/contracts; coordination/description validation checks allowable edits. Appendix G explicitly separates these checks from experimental task-performance assessment. We do not substitute a performance-based retention gate.
- Costs are the paper's single-round totals for GLM-5.2/Claude Code; no exact token matching, other-model cost extrapolation, full three-round sum, dollar/wall-clock estimate or isolated distillation-stage price is claimed. Table 6 also contains a cheaper OfficeQA baseline per point, which the blogs state.
- No unresolved prose/table discrepancy is alleged. One-round cost-efficiency denominators and three-round headline scores are different experimental points and are kept separate.

## Judgment notes

No score/judgment files changed. The stored score is 64, band ★★, evidence level retained in research/scores.jsonl; latest judgment is research/judgments/2026-10-19-a.jsonl. It marks held-out, cross-task, optimizer cost and retained ablation yes; budget matching partial; variance and leakage guard unclear; improver comparison no. The full PDF supports those qualifications. It compares maintenance/invocation variants, but explicitly keeps the update protocol fixed; our interpretation does not promote it to an evolving improver. No judgment correction is proposed.

## Rendering checks

House-style 2400 × 1440 poster; no reused figures. The final PNG was visually inspected after fixing method-card spacing and chart value-label crowding. Shared render() reports no OVERFLOW. Body/caption font floor is 22 px; SVG text is checked at rendered scale separately. Work files, exact-version PDF, extracted full text and per-page facts remain under /home/lingxufeng/reel-work/2610.23599/.
