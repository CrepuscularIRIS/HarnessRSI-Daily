# SOURCE — Learning to Continually Learn via Meta-learning Agentic Memory Designs (ALMA)

Read from: arXiv 2602.07755v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram and charts on the poster were drawn by us from the paper's Table 1 and Table 2 numbers.

## Where the numbers come from
- Table 1 (headline, p6; GPT-5-nano top block, GPT-5-mini bottom block), Table 2 (greedy search vs ALMA, Appendix C.2, p39), Section 4.4 text (p6-8; "6.2%", "12.8%", "6.6%", 84.1% under distribution shift, $0.09 cost), Section 4.1 (p4-5; 11 learning steps, 43 designs, three Deployment runs), Section 3.2-3.3 (p4), Appendix A.2-A.4 (pp16-18), Algorithm 1 (p24), B.1 (benchmark sizes, pp24-26), B.2 (baselines, p30), B.3 (learning setup, sampling parameters, greedy search, pp30-36), B.4 (testing, p36), Section 5 (safety, limitations, p8). Figures 4, 5, 6 (pp8-9) used only qualitatively (no numbers read from them except those stated in the text).

## ‡ numbers (computed by us)
- 0.5‡ = 12.4 (ALMA, GPT-5-nano) − 11.9 (greedy search), Table 2.
- 10.0‡ = 87.1 (ALMA, GPT-5-mini) − 77.1 (greedy search), Table 2.
- 4.7‡ = 38.0 (Dynamic Cheatsheet) − 33.3 (ALMA), Baba Is AI, GPT-5-mini, Table 1.
- 2.9‡ = 80.0 (Trajectory Retrieval, GPT-5-mini, Table 1) − 77.1 (greedy search, Table 2).
- 7‡ = about 100 / 14 percentage points: one task of a ~14-task deployment set in a single run (see inference below).
- Combined-SE ratios (‡): difference between two Table 1 / Table 2 means divided by sqrt(SE1^2 + SE2^2), treating the three-run means as independent. ALFWorld nano 12.4 vs 7.6: 4.8 / 0.71 = 6.8‡. ALFWorld mini 87.1 vs 80.0: 7.1 / 1.98 = 3.6‡. TextWorld mini 75.0 vs 68.8: 6.2 / 5.23 = 1.2‡. MiniHack mini 20.0 vs 16.7: 3.3 / 3.01 = 1.1‡. Greedy (mini) 77.1 vs Trajectory Retrieval 80.0: 2.9 / 1.61 = 1.8‡. These are rough screening arithmetic, not tests.

## Inferences by us (not stated in the paper)
- Baba Is AI values in Table 1 (9.5, 19.0, 14.3, 21.4, 30.9, 26.2, 33.3, 38.0) are multiples of 1/42 (4/42, 8/42, 6/42, 9/42, 13/42, 11/42, 14/42), consistent with a deployment set of 14 tasks run three times. Appendix B.1 says 52 tasks in total, learning/testing split evenly and each split evenly into collection and deployment, which would give 13 deployment tasks (multiples of 1/39 over three runs); the paper does not reconcile this, and we report it as a paper-internal inconsistency. The value 38.0 for Dynamic Cheatsheet (GPT-5-mini) is not exactly k/42 (16/42 = 38.1).
- ALFWorld values in Table 1 are multiples of 1/210 (e.g. 12.4 = 26/210, 87.1 = 183/210), consistent with 70 deployment tasks x 3 runs; Appendix B.4 names the valid seen set (140 tasks) for the scaling study but does not name the Table 1 test split explicitly. We do not state this split on the poster or in the blogs beyond "separate testing split".

- ALFWorld learning set = first 30 training tasks (B.3), split evenly: 15 deployment tasks x 3 runs = 45; learning-set scores printed in Figures 12 and 14 (0.02, 0.04, 0.09, 0.11 ...) lie on a 1/45 grid. Used only to say the selection metric is small and noisy.
- Greedy vs ALMA initial designs (B.3: each search generates its own initial design; Fig. 14 greedy root appears higher than Fig. 12 ALMA root; best learning-set scores appear similar) are read from small figure labels; no decimals from these figures are printed. Greedy run = 43 steps (B.3); ALMA = 11 steps with up to 5 designs each (Sec 4.1).
- Baseline adaptations (App. B.2): Trajectory Retrieval top-1 "due to context length constraints"; Reasoning Bank uses ground-truth feedback of each trajectory; Dynamic Cheatsheet fixed global cheatsheet at deployment. Table 1 is static mode (Sec 4.4); learning also uses static mode only (Sec 3.2).
- Splits (B.3, B.4): TextWorld and Baba Is AI split evenly with the second half used for testing; MiniHack 30% learning, remaining 70% testing. Not stated: random vs ordered, how MiniHack's 30% is chosen. The remark that an ordered TextWorld half could shift the Treasure Hunter / Cooking mix is ours.
- Reasoning effort: GPT-5-nano/low (learning and nano test), GPT-5-mini/medium (transfer) (B.3, B.4).
- Ablations not run (as far as we found): visit penalty / temperature of the sampling rule, with vs without replacement (B.3 only "expects" minimal impact), Meta Agent model, abstraction. The greedy search (Table 2) IS an ablation of the parent-sampling rule.

## Notes
- "Best baseline" in the poster chart = the highest manual-design value in that column of Table 1 (G-Memory, Reasoning Bank, Trajectory Retrieval or Dynamic Cheatsheet, named under each group). "nm" = No Memory row.
- "Best or tied in 7 of 8 columns": GPT-5-nano ALFWorld, TextWorld, MiniHack best; Baba Is AI tied (19.0 each, Trajectory Retrieval); GPT-5-mini ALFWorld, TextWorld, MiniHack best; Baba Is AI not best (33.3 vs Dynamic Cheatsheet 38.0).
- "Overall avg." in Table 1 is the paper's own column; "+6.2" / "+12.8" are percentage points over No Memory.
- Intro (p2) says the learned designs are "more cost-efficient than most human-designed memory baselines"; Section 4.4 (p8) says lower cost "compared to all manual designs". We report both. The cost metric (Appendix A.3) covers the Memory Collection and Deployment phases only; the paper reports no cost for the Meta-Agent search.
- Figure 5 (distribution shift): only ALMA's 84.1% is stated in text; baseline bars and the overlap of ALMA's and Trajectory Retrieval's error bars are read from the figure.
- Standard errors in Table 1 / Table 2 are over three Deployment runs of one finished design. The paper reports one search per benchmark and no repeats ("seed" does not occur in the paper). Memory collection is done once per design; only the Deployment Phase is repeated.
- The Meta Agent may call GPT-4o-mini / GPT-4.1 inside designs during learning; all designs use GPT-4o-mini and text-embedding-3-small at test time (Sec 4.1, B.3).

## Judgment notes
No change to the judgment (batch b18): `budget_matched: unclear` and `optimizer_cost: unclear` agree with the full paper (search cost not reported; the greedy ablation is matched in number of designs, 43, but baselines get no comparable search), `leakage_guard: untested` agrees (no overlap or contamination audit), `cross_task: unclear` agrees (only GPT-5-nano to GPT-5-mini model transfer and an ALFWorld distribution-shift test; no design carried to another benchmark). Two points for a reader: `variance: yes` rests on standard errors over three Deployment runs of one design, not on repeated meta-learning runs; and the paper's "on all benchmarks" claim (abstract, Section 4.4) is not supported by Table 1 for Baba Is AI (tie with GPT-5-nano; Dynamic Cheatsheet ahead with GPT-5-mini).
