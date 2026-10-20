# SOURCE — Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills

Read from: arXiv 2610.17860v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, forest chart and tables on the poster were drawn by us from the paper's numbers.
Authors (PDF title block, order checked on the rendered page): Letian Zhu*, Han Li*, Yifan Yao*, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu (corresponding); Nanjing University, Alibaba Group. The poster header abbreviates the list.

## Where the numbers come from
- Headline: Table 1 (p7) and Table 8 (p18, gains and 95% CIs, full-pass, tokens/run). Paired contrasts and the 16-of-22 count: Appendix D.1 (p18).
- Per-family values: Table 9 (p18). Case-level counts: Table 10 (p19). Repeats and SD: Table 11 (p19).
- Cross-model: Table 2(a)/(b) (p8), Table 12 and Table 13 (CIs, p20), Appendix D.3 (4.88 / 2.54 / 4.09, p19).
- Review schedules and cost: Table 17 (p23), text of Section 5.4 (p9), Appendix F.1 (158.2 M vs 60.6 M Educator tokens, p23), Table 18/19 (p24), Figure 5 (p9, per-run Educator tokens; not used on the poster).
- Process analysis: Figure 4 and Section 5.3 (p8), Appendix E.2-E.3 and Table 16 (pp21-22). Case study: Table 3 and Appendix G.1 (pp9, 25).
- Benchmark and cohort selection: Section 3 (pp3-5), Appendix B (pp12-14), Table 5 (p13). Models and sessions: Appendix C.1 (pp14-15). Loop and issue rules: Section 4 (pp5-6), Appendix C.2 (pp15-16), Table 7 (p17). Baseline adaptation and SKILL-KD cost scope (1.94 M tokens per run): Appendix C.3 (pp16-17). Limitations: Appendix H (p25).

## ‡ numbers (computed by us)
- 5.0‡ points = (0.411 + 0.282 + 0.222 + 0.186) / 22 = 1.101 / 22, the sum of the four largest Fixed-Window-minus-No-Skill family gains in Table 9 (DB WAL recovery 0.884 − 0.473, Flask 0.690 − 0.408, Organization JSON 1.000 − 0.778, HTML finance verification 0.917 − 0.731), divided by 22 families. This is about 65% of the 7.75-point macro gain; the 22 No-Skill and Fixed-Window values average to 0.723 and 0.801, matching Table 8. The percentage is not printed in the blogs. The poster footnote reads "‡ computed by us from Table 9".

- 0.025‡ = 0.801 − 0.776 (Table 17, Fixed-Window g = 10 vs g = 5 / g = 20), compared by us with the repeat SD of 0.030 (Table 11).

## Notes
- Headline numbers use Table 8 (three-decimal) values; Table 1 prints the same on a 0-100 scale (72.3, 80.1, 80.5, ...).
- The paper does not say how g = 10 was chosen as the main condition; g = 5 and g = 20 are evaluated on the same held-out cohort.
- Adapted Trace2Skill and SKILL-KD: the paper does not state a tuning budget for them (searched the text for tuning / hyperparameter terms) and gives their cost on a different scope (Table 8 dashes; SKILL-KD audit 1.94 M tokens per run). Whether adapted Trace2Skill uses the Max model is not stated in the main text or Appendix C.3.
- "No best-round selection or accept/reject gate": from the Appendix C.2 pseudocode, which freezes K after round 3 and evaluates the final K; we found no selection step described.
- "No contamination check": we searched the full text for contamination / memorisation / leakage terms; the only hits are the "Git leak recovery" task family. The paper states that private tests and reference solutions stay outside agent workspaces and that held-out materials are inaccessible during acquisition (Appendix B.3, C.1).
- The 13 catalog families outside the 22-family main cohort: we found no results for them in the main text or appendix.
- Expert Authoring vs Post-hoc Teaching ordering differs between the main cohort (Table 1: 0.728 vs 0.748) and the shared lite subset (Table 2a: Post-hoc trails Expert in all three pairs); the paper's text discusses only the latter.
- Table 2(a), Qwen column: Fixed-Window +4.1 and Issue-Guided +4.5, so Issue-Guided is the higher point estimate there, while DeepSeek and Kimi favour Fixed-Window. All Issue-minus-Fixed intervals in Table 13 include zero.
- Process-analysis figures (73.0%, 16.1%, 23.9, 38.6) are taken from the text and Table 16; the paper states they are observational associations. Only 112 of 193 ten-call windows have a comparable Skill pair (E.2).

## Judgment notes
- Our judgment (batch 2026-10-19-a): `budget_matched: unclear`, `leakage_guard: untested`, `cross_task: unclear`, `improver_comparison: unclear`, `evidence_level: retained`. The full paper is consistent with these. Two observations, no change proposed: (1) the paper does compare variants of the acquisition mechanism itself (Expert Authoring, Post-hoc Teaching, Fixed-Window g = 5/10/20, Issue-Guided; Tables 2, 8, 17) and reports tokens per run for them, but never runs a matched-token comparison, so `budget_matched` stays `unclear`; (2) the `improver` level would need the improvement mechanism to be modified and compared as the improver, which these protocol variants approximate but do not isolate (Limitations, Appendix H).
No judgment file was edited.
- Added after independent check: Issue-Guided has an initial review (first revision or warm-up of tool calls, Appendix C.2); no main-cohort interval for Issue minus Fixed exists in the paper (Table 13 covers the shared subset only), so 'not separated' on the main cohort is our inference from the repeat SDs; whether the No-Skill screening runs overlap the reported No-Skill repeats is not stated (our inference about possible inflation is flagged as such); Expert Authoring has the external Max model explore and write (Table 7), and adapted Trace2Skill / SKILL-KD do not use the 3-round anchor loop (C.3, C.3.1); HTML finance case study is one repeat of one family where Expert Authoring (1.000) > Fixed-Window (0.917) (Table 9, Table 3).
