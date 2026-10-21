# SOURCE — REFLEX: Reflective Evolution from LLM Experience

Read from: arXiv 2606.16496v2
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers. The paper gives no code link, so the poster carries the paper QR only.

## Where the numbers come from
- Method and credit rule: Section 3.2–3.4, Algorithm 1 (pp3–5), Table 5 (hyperparameters, p17).
- Table 1 (headline, matched comparison at 50 and 100 calls, p7); statistics and invalid-child counts in Section 4.2 (p6); 20-call-cap result (p6).
- Table 2 (CCAA, p8) and Section 4.3 (pp6–8).
- Section 4.4 and Figure 7 (transfer, pp8–9), Section 4.5 and Table 3a/3b (pp9–10), Limitations (p10), Appendix B (p16), Appendix D (p18).
- Poster bars for median calls to solve are the 100-call "Calls" medians of Table 1; "solved" counts are the Table 1 Solved columns. CCAA bars are the "≥ 25.25" column of Table 2 (shared-prior rows). The bar heights are only the counts printed in the table; no figure values were read from images.

## ‡ numbers (computed by us)
- 0.070‡ = −0.4742 (textual strategies, Table 3b AUC@20) − (−0.5445) (executable fragments, Table 3b AUC@20), the gap between the table means; the paper's +0.017 (p = 0.70) is a median of paired differences, not this mean gap. Blogs only; not on the poster.

Every other decimal number in the blogs and on the poster is printed in the paper. The "about half" and "40%" wording is the paper's own ("roughly half the calls", "about 40% of its calls on the Critic").

## Notes
- Table 3a vs Table 1 (not reconcilable): Table 3a gives REFLEX 5.50 mean calls to target with 10/10 solved and AUC −0.2850; Table 1's Acrobot 100-call row gives median 13 [7, 21] and AUC −0.280±0.035, Actor-only 28 [17, 43] and −0.410±0.050, and the 20-call paragraph says Actor-only and REFLEX each solve 6/10. A mean of 5.50 over 10/10 solved seeds cannot be the same runs as a median of 13. Table 3a's budget and seeds are described only as "an identical call budget for all conditions" / 10 paired seeds. The blogs say so and the poster does not set the two side by side except to flag it; the image-shuffle control is single-task, mean-based, and has p-values for AUC only (none for calls to target).
- Actor-only is not a clean isolation of the image or of the memory: its placeholder diagnosis lists only the parent's scalar metrics and also serves as the BM25 query (p5), so removing the Critic also changes retrieval; its Skill Memory rules are unchanged.
- Table 3b vs Section 4.4: in Table 3b executable fragments (AUC@20 −0.5445) are barely above no memory (−0.5618) and below textual strategies (−0.4742, 10/10 vs 9/10 solved), no pairwise difference significant; Section 4.4 reports AUC@20 −0.523 → −0.310 (Pendulum bank) and −0.380 (Lunar Lander bank). The paper does not say which source bank, model or seeds Table 3b used and does not reconcile the two.
- Acrobot target is −0.20; the cold mean final (−0.139) and every bank result already lie above it (higher is better), cold median calls to target is 4.0 (Section 4.4).
- Section 4.2 says the Critic calls "pay off once the budget allows several diagnosis-conditioned mutations"; Limitations (p10): at a 20-call cap "the Critic brings no measurable benefit over Actor-only"; the transfer study runs at the 20-call cap.
- Reading cautions stated in the blogs: ± is SEM (Tables 1, 2); Table 1 does not say whether unsolved seeds are excluded from the median calls (Table 2 does); Table 5 says seeds 0–9 for all formal comparisons while p5 says the 50- and 100-call budgets used different seeds; the 20-call interval [−0.123, 0.453] around +0.015 is asymmetric; no significance tests for the antenna comparison.
- Antenna baselines: the shared prior is "the same first LLM/analytical designs for every method", so Random Search, CMA-ES, GA and PSO start from designs that are partly LLM-produced; whether those designs count within the 240 evaluations is not stated; REFLEX's inner local-search evaluations are counted in the 240 but the paper does not say baselines get an equivalent local search. "Equal budget" is equal objective evaluations only, not LLM cost; REFLEX's LLM call count on the antenna task is not reported.
- Which row is the headline: Table 1 reports mean ± SEM over 10 paired seeds (seeds 0–9); the 50-call and 100-call budgets are separate runs with different seeds (p5). The poster uses the 100-call block. In the Acrobot 50-call block Final is a median and AUC has no SEM (Table 1 caption).
- The Actor-only ablation keeps the Skill Memory ("all other operators and Skill Memory rules are unchanged", p5), so it isolates the Critic, not the memory. Official MLES is run at its public commit acda6457 with native prompts and operators; the paper describes no Skill Memory for it.
- Table 3a states "an identical call budget for all conditions" but not its size. Its REFLEX calls-to-target (5.50, mean) and Actor-only (10.30) differ from Table 1's Acrobot medians (13 and 28 at 100 calls) and all four conditions reach the target 10/10, whereas the 20-call-cap paragraph says REFLEX and Actor-only each solve 6/10. The paper does not reconcile these; we report the Table 3a values as printed and flag the budget as unstated.
- Table 3b says "the same frozen source bank" without naming which one; no pairwise difference is significant, so the poster only states that.
- The transfer study uses Qwen3.5-27B and a 20-call budget; the main comparisons use Qwen3-VL-235B-A22B-Instruct. Transfer p-values (final p = 0.002, AUC@20 p = 0.049 / 0.065, calls p = 0.039 / 0.91) are quoted from Section 4.4 text.
- CCAA: all methods get 240 objective evaluations including REFLEX's inner local search; the number of LLM calls REFLEX uses on CCAA is not stated in the text. Tuning settings for CMA-ES, GA, PSO and Random Search and the way the 25.0 / 25.25 thresholds were chosen are not reported (Table 5 lists only the matched-comparison settings of the LLM methods).
- Figure 6 (component profile with "w/o Skill Memory" and "w/o Burst" variants) is qualitative with no numbers; the poster does not use it and the blogs say no numeric Skill Memory ablation is reported in the main runs.
- Lunar Lander final-score comparison at 100 calls: the paper says all three methods reach a similar final NWS and the final-score CI excludes zero only at 50 calls.

## Judgment notes
No correction. The full paper is consistent with our judgment (latest batch, version_read v2): `held_out: partial`, `cross_task: yes`, `variance: yes` (paired seeds with bootstrap CIs), `budget_matched: yes` (total LLM calls incl. Critic/Actor/repair/abstraction; for CCAA the budget is objective evaluations, not LLM cost), `optimizer_cost: yes` (only wall-clock for control tasks, App D; no dollar cost, no antenna cost, so this item is generous), `retained_ablation: yes` (empty vs frozen banks), `improver_comparison: unclear` (no comparison of the credit rule or the UCB1 bandit against alternatives was found), `leakage_guard: tested` (hash-verified banks, audit for Acrobot identifiers). Caveat for readers: transfer rests on one target task and one model, and the within-campaign Skill Memory contribution is not ablated numerically.
No judgment file was edited.
