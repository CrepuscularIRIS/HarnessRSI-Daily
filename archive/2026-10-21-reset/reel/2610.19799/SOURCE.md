# SOURCE — Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems

Read from: arXiv 2610.19799v1
Paper figures shown: none

Exact-version PDF downloaded from https://arxiv.org/pdf/2610.19799v1 to /home/lingxufeng/reel-work/2610.19799/paper.pdf. Read all 35 pages including appendices, using layout extraction for tables and plain extraction for prose; visually checked the title block and Table 4. Authors in PDF order: Seojin Hwang, Youngmin Choi, Hwanhee Lee; Chung-Ang University. No paper figure was extracted for or embedded in the deliverable. The diagram and chart are our own renderings of textual method descriptions and table values. Figure reuse is forbidden for this task. No code URL supplied; no paper/repository code run.

## Claim and table provenance

| Claim / material | PDF provenance |
|---|---|
| Exact title, authors, institution | Title block, p1, visually checked |
| Individual, relational and team artifacts; fixed weights; mailbox; memos and permissions | Sections 3.1–3.3, pp3–6; Tables 1–3, pp4–6; Appendix D.2–D.4, pp14–15 |
| L1 mechanism signals and four versus one iterations; strong updater and contradiction judge | Table 2, p5; Table 10, p13; D.1–D.2, pp13–14 |
| SkillOpt ground-truth and trajectory access | D.2.2, p14: prediction, ground truth, correctness or LCBS sub-scores; L2 notes also supplied |
| Role-specific skills/memory versus common constitution; memo access and sharing | Sections 3.1 and 3.3, pp3–6; D.2.3–D.3, p14; Appendix L.3, p31. No pooled all-agent skill/memory library is described; this is scoped to the stated architecture, not a claim of filesystem-level isolation |
| Gates: same 20 val tasks/seeds, alpha 0.3, example thresholds 10/8/12, cap, promotion outside gate | Section 3.1.4, p4; Section 3.3.2, p6; D.5, especially D.5.1, and Table 11, pp15–16; E.1, p16. L1 excludes tasks where the role was not called (n may be below 20); iteration-0 reference measured once under none with the untrained template team, shared within composition, then replaced by accepted scores. The 10-to-12 threshold is the n=20 example; unlike L1, L3 freshly evaluates current/revised teams |
| Weak/strong models and temperature; exact strong-role assignment including two OfficeQA readers | Section 4, p6; B and Table 8, pp12–13 |
| Main chart and headline means / SD | Table 4, p7, visually verified. SkillOpt GAIA mixed competition 74.2 ±3.8 vs strong solo 49.2 ±1.4; LoCoBench all-strong conformity 87.2 ±2.1 vs solo 74.4 ±2.5; OfficeQA all-strong conformity 36.6 ±6.5 vs solo 34.4 ±0.9. Bars show means; caption gives evaluation-only SD scope; no CI is represented |
| 25.0 points, 24/27, large gains concentrated; all-strong GAIA none sometimes better; OfficeQA mixed fails; all-weak competition collapse | Sections 5–6, pp6–8; Table 4, p7. These are specific columns, not pooled cross-benchmark averages |
| Frozen-team three-repeat evaluation versus one evolution run per condition | Table 4 caption, p7; Limitations, p9; F.3, p17. Never treated as three evolution seeds |
| Split sizes 17/20/40, 80/20/99, 51/20/62; seed42, non-overlap, val gates and test evaluation | Appendix A and Table 7, p12 |
| Solo tool and L1 access; no solo constitution/L2/L3; preevolve zero updates; none still has L1/L3 and L3 gate | Section 4, p6; B, p12; D.2.1, p14; Sections 3.3.2 and Table 3, pp5–6 |
| Hyperparameter choice | MemRL thresholds on unlabeled val–train input pairs, D.2.3, p14. Other defaults' full selection split/search budget not stated. Alpha from validation noise, D.5, p15. Revision cap from preliminary uncapped runs, D.5.2, p16; preliminary-run split not stated |
| Test-informed structure and composition choices | Appendix I.6, p20 explicitly says best structure chosen after the fact from three; Appendix J, pp20–21 says additional strong-role ordering uses workload on scored preevolve test sessions. Test is held out from evolution, but best-scaffold reporting is test-selected |
| Paired analysis, seven comparisons p<0.05, optimistic p-values | I.6, p20; Table 21, p23: selected best structure and correlated task repeats; authors call this a noise check rather than confirmation |
| Team-grown leader accepted skills and only-solved pairs | Table 6 and Section 6.3, p8. Diagnostic selected runs, not an isolated note-sharing intervention |
| Session and reflection costs; timeouts/crashes | Section 4, p6; B, p12; F, pp16–17. 900s session, 100 messages team/50 solo, 50 steps per agent; per-role output allowances differ. L3 paired gate consumes 40 sessions per iteration, D.5.2 p16. Separate reflection caps 300/900/900 seconds, F.2 p17. Section 4 p6 and F.1 p17: time/message-limit terminations count as failures in every score, including both gates; crashed sessions are excluded. No crash counts or result effect inferred |
| Selected deployment call counts 19.4,46.8,22.6; 18.3,73.3; expensive mixed conformity 107.3 vs80.0 | Table 5, p8. Counts are final-evaluation means for selected runs, NOT phase-separated evolution costs; solo cost row is preevolve, not evolved solo |
| Whole-experiment timings 4.5–16.0h and14.5–37.2h; no optimizer-only token/$ accounting | Appendix G, p18. Wall-clock ranges on one GPU set (two GPUs); no complete cost-matched baseline table. Serving-load confound acknowledged in Limitations, p9 |
| Tiny-sample ungated promotions | Appendix E.1 p16 and Table 13 p18. SkillOpt validation skill score; Meta-Team training-participation success; MemRL mean Q |
| Model-family counterexamples, no artifact transfer | Appendix J, pp21–22; Tables 26–27, pp24–25: Gemma GAIA mixed none37.5±0.0 vs competition32.5±5.0; Mistral LoCoBench all-strong collaboration58.9±4.7 versus evolved solo80.5±3.5, conformity31.3±5.6. Optimizers and writers fixed to the new family's strong model; these are re-evolved runs, not frozen-artifact transfers |
| Leakage claims | Disjoint splits: Section 4 p6 and Appendix A p12. Unrestricted web access stated in Appendix J p20 as in main experiments. No empirical evaluation-content/retained-artifact contamination audit found in full paper including Appendix L prompts. We do not claim leakage occurred. Prompt advice to learn reusable patterns is not an audit |

## ‡ numbers

None. No computed numbers or numbers read only from figure labels are used in either blog or the poster. The 25.0-point headline is explicitly reported in Section 5 (p7), not introduced as our calculation. All displayed result values come from tables. The chart axis is a plotting scale rather than a paper measurement.

## Scope and unresolved issues

- The chart deliberately compares the same evolution mechanism (SkillOpt), showing selected team maxima on each benchmark. It is not an average, nor does it imply each composition or each structure wins.
- Repeated-evaluation SD is reported for Table 4 and the model-family tables according to their captions; it does not establish repeated-evolution variance. Poster chart bars show means only; the caption and controls state what the three repeats measure.
- Hyperparameter and baseline tuning-search budgets are not fully reported; do not infer a weakened baseline. Solo baselines do get the same L1 mechanism and all benchmark tools, but no peers/L2/L3 and a smaller message cap.
- The paper's claim that scaffolding grows the leader is supported by process traces and selected comparisons; our interpretation does not present it as an independently isolated causal effect of memo sharing.
- No numerical paper inconsistency is asserted. Relevant rows, mechanisms and model-family variants were checked before choosing counterexamples.

## Judgment notes

Board record: /home/lingxufeng/ArxivDaily/research/scores.jsonl, score65, band★★, retained. Latest judgment: /home/lingxufeng/ArxivDaily/research/judgments/2026-10-19-a.jsonl. No score or judgment file was changed.

The recorded `variance: yes` is evaluation-only variance, not independent evolution runs, exactly as the judgment's supporting quote says. `budget_matched: partial` matches the common session time limit but unequal message and per-agent budgets. `cross_task: unclear` must not be replaced by a claim of artifact transfer merely because there are several benchmarks/model families. `leakage_guard: untested` remains appropriate: partitioning is stated, contamination is not empirically audited.

The judgment's `optimizer_cost: unclear` omits Appendix G's whole-experiment wall-clock ranges (p18). We explicitly report those ranges while distinguishing them from phase-separated optimizer token/dollar costs and a matched-cost baseline comparison. This is a clarification of available evidence, not a rescore. Test-selected best structures and test-workload-informed additional role assignments are explicit qualifications to the retained-evidence narrative; test remains separate from the evolution gates, but is not an independent confirmation set for choosing a universal social scaffold.
