# SOURCE — EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents

Read from: arXiv 2609.05903v2
Paper figures shown: none

Authors (PDF title block): Nanxi Li, Yingzi Ma, Yulong Cao, Chong Xiang, G. Edward Suh, Bo Li, Yejin Choi, Dawn Song, Chaowei Xiao.
The method diagram, charts and tables on the poster were drawn by us from the paper's table numbers; no figure from the paper is reproduced. Whole PDF (25 pp, appendix included) was read; the paper has no separate Limitations section.

## Where the numbers come from
- Method and keep rule: Sec. 2 / 2.1 / 2.2 (pp4-6), Algorithm 1 and cascade details (App. B, pp16-17); Designer model default Claude Opus 4.8 (App. D, p18).
- DTAP headline: Table 1 (p7), Average rows; per-domain Progent / Evo rows from Table 1 "Average" block; DeepSeek-V4-Flash os-fs row from Table 1.
- AgentDojo / AgentDyn and Agent-SafetyBench: Table 2a/2b (p8), Mean rows; split sizes and protocol: App. D (p17).
- PAIR adaptive attack: Sec. 3.2 (p8), Table A5 (p18).
- Ablations: App. A (pp13-15): Tables A1, A2, A3 (panels A, B), A4; "−19.5 on average and 31.0 on os-filesystem" from Sec. 3.2 (p8); Meta-Harness 47.3 vs 61.9 from Sec. 3.2 and Fig. 4c (p8-9; both values are also stated in the text).
- Residual risk: App. G (pp20-23), Table A8; 479 -> 105 and os-fs 57/105 from the text on p20.
- Cost: App. H (p23), Table A9. Significance: App. I (pp24-25), Table A10. Extra victim: App. J, Table A11 (p25).
- Chart bars on the poster use Table 1 averages (utility, D-ASR, I-ASR) and Table A3 (Criticizer on/off held-out Score).

## ‡ numbers (computed by us)
- 3.3‡ points per benign task = 100 / 30 benign tasks per DTAP cell (App. D: 30 benign tasks). The paper separately states a 3.3-point average utility cost (83.1 → 79.8); the "one task = 3.3 points" reading is ours.
- 15.7‡ points = 81.43 (GPT-5.6 Sol) − 65.71 (GPT-5.6 Terra), mean scores of the outer-model arms, Table A1 (blog only).
- No other number in the blogs or on the poster is computed by us; differences quoted (23.4, 38.3, −19.5, 43.6%, 78.1%) are the paper's own.

## Notes
- Table 1 percentages that are not multiples of 1/35 or 1/30 (e.g. 61.8, 55.9) are consistent with the paper's statement that tasks lost to provider outages are excluded rather than imputed (App. D, p17); we did not recompute any cell.
- "Progent has lower ASR on os-fs and finance" compares the domain "Average" rows of Table 1 (Progent D/I 6.3/2.3 and 4.6/6.9 vs Evo 24.6/8.0 and 9.7/13.7); on the five-victim average, Progent's indirect ASR (6.3) is below Evo's (7.4) while its direct ASR (14.7) is above (12.6). The paper calls Progent's ASR "similar" and stresses its 23.4-point utility loss.
- Internal inconsistency noted: Sec. 3.1 says one outer coding model drives Designer, Analyzer and Criticizer (default Claude Opus 4.8), while App. A states that the warm-start and Criticizer arms use an Opus 4.8 Designer and a Sonnet 4.6 Criticizer. We report the ablation arms as the appendix states.
- Table A1's primary-grid Opus 4.8 reference (Kimi-K2.5: 73.33 / 77.14 / 51.43 score) used an earlier Criticizer configuration; the Table A3 reviewed arm (same victim, 69.0 / 85.2 / 81.4) is a separate search. We present both without explaining the gap; the paper does not repeat searches of the same cell.
- Table A8 / App. G: the text says counts are never pooled across direct and indirect attacks, yet "telecom finance fraud 5/30 (16.7)" pools direct 4/15 and indirect 1/15; the blogs repeat the paper's 5/30 and flag this.
- Non-nominal denominators: GLM-5 finance no-defense utility 79.3 = 23/29 and CaMeL GLM-5 telecom D-ASR 61.8 = 21/34 (our arithmetic, from Table 1), so some cells have fewer than the nominal 30/35 tasks because outage-lost tasks are excluded (App. D); baseline and EvoSafeHarness cells may therefore not be strictly task-for-task paired (our inference; App. I describes paired tests on the same frozen tasks).
- Cost and cascade caveats: Table A9 says recorded dollars "are not complete billing" so $328.74 is a floor; "Staged" in Tables A3/A4 is the 3+12+30 schedule, so 43.6% compares nested vs staged (Fig. 4b and the text call it "full evaluation").
- AgentDojo uses one attack family (important_instructions, App. D); the AgentDyn attack type is not stated; the PAIR study is one harness, one attacker, one injection surface (App. D).
- Kimi-K2.5 on finance/telecom/os-filesystem is searched under at least seven configurations (primary grid, four outer models, no warm start, no Criticizer) but never repeated under the same configuration; the Criticizer-off os-fs score (50.5) is close to the primary-grid search (51.43), so the 31.0-point os-fs gap is not separable from search noise (our reading).
- Table A8: telecom finance fraud is 4/15 direct + 1/15 indirect, i.e. 5/30 (16.7) pooled, as in the text of p22.
- Baseline costs: the paper gives only aggregate ledgers (Table A9), which mix search, baselines, held-out runs and diagnostics; outer-optimizer dollars are not recorded. The number of search iterations and the Meta-Harness arm's budget are not stated anywhere we read (main text and appendix).
- Whether DTAP train and held-out tasks share risk types or templates is not stated in the text we read; the paper states only that they occupy disjoint directories (App. D).
- The blind-audit token-keyed rule counts (2 vs 4 os-fs, 0 vs 1 telecom, 0 vs 0 finance) are small counts from one Sonnet 4.6 audit (Table A3).

## Judgment notes
Batch b06 judged `variance: unclear`, `budget_matched: unclear`, `improver_comparison: unclear`, `optimizer_cost: partial`, `evidence_level: retained`, score 68 (★★). The full paper is consistent with the first two: search variance is not reported (App. A: "not seed-level variance estimates"; App. I intervals cover only the fixed held-out tasks) and no matched-budget baseline is given. Two points the maintainers may want to weigh: (1) the paper does modify its own improvement mechanism and compare (Criticizer off, warm start off, outer-model swap, an adapted Meta-Harness search), though each as a single search; this bears on `improver_comparison` / evidence level; (2) Appendix H gives aggregate outer and inner cost ledgers (no per-search or per-baseline split), which bears on `optimizer_cost`. We did not edit any judgment file. The `leakage_guard: tested` judgment rests on a blind post-hoc code audit counting token-keyed rules (a Sonnet 4.6 reading each selected harness's code and bundle, Table A3; the Criticizer in those arms is also Sonnet 4.6) and one seven-case rename probe on finance where both arms get 42.86% ASR (p15). We found no replay of the final harnesses on renamed or paraphrased held-out tasks; AgentDyn is a transfer test, not a rename test.
