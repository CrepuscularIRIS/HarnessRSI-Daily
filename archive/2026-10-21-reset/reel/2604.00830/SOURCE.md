# SOURCE — Meta-TTL: Meta-Learning Self-Improvement Policies for Language Agents

Read from: arXiv 2604.00830v4
Paper figures shown: none

License: CC BY 4.0 (figure reuse permitted), but we reused no figure. The method diagram, chart and tables on the poster were drawn by us from the paper's numbers. Authors as printed in the PDF title block: Zhanzhi Lou, Hui Chen, Yibo Li, Qian Wang, Bryan Hooi (National University of Singapore).

| Figure from the paper | Credit |
|---|---|
| (none shown) | n/a |

## Where the numbers come from
- Method: Sec. 3 (pp3–5), Eqs. 1–7, Algorithm 2 (p26); episodes per session and benchmark split: Sec. 4.1 (p5); meta-training cost: Sec. 4.4 "Efficiency analysis" (p9).
- Table 1 Jericho (p6), Table 2 WebArena-Lite (p7), Table 3 τ²-bench (p8), Table 4 parameter-updating comparison (p8), Table 5 RL / GEPA outer loops (p8), Table 6 efficiency (p9), Tables 7–8 GLM-5.3-Flash backbone (p27), Appendix E (pp27–28), Appendix A (meta-prompts, pp13–23).
- "ID evaluation uses the meta-training games" is from Sec. 3.4 (p5).
- Run counts: Table 1 "five repeated runs", Table 2 "three repeated runs", Table 6 "3 runs"; Table 3, Table 4, Table 5 and Tables 7–8 state none (searched the full text).

## ‡ numbers (computed by us)
- 0.162‡ = 0.790 − 0.628 (Meta-TTL − EvoTest, Detective W-AUC, Table 1).
- 0.011‡ = 0.150 − 0.139 (Zork 1, Table 1). 0.046‡ = 0.248 − 0.202 (Temple, Table 1). EvoTest is the strongest baseline in all three ID columns.
- 0.004‡ = 0.427 − 0.423 (Zork 3 OOD, Meta-TTL − EvoTest, Table 1).
- 0.092‡ = 0.292 − 0.200 (Balances OOD, Meta-TTL − Naive Meta-Agent, strongest baseline in that column, Table 1); 0.113‡ = 0.522 − 0.409 (Library OOD, same, Table 1).

## Notes
- Table 4 / Appendix E: Meta-TTL row = Qwen3-8B actor + Qwen3-8B meta-agent running the main-experiment meta-prompt (meta-trained with GPT-5 / Gemini-3-Flash), K = 3 episodes, at most 30 steps; SFT+MAML meta-learns a LoRA initialisation on the ID games (15 meta-steps, 2×H200). Tables 4 and 5 ID games (Detective, Zork 1, Temple) are the meta-training games (Sec. 4.1).
- Table 5 explanation of GEPA's OOD result: Sec. 4.3 (p7–8): candidate selection "preserves prompts specialized to individual tasks", "also consistent with our finding that the prompts produced by GEPA contain substantial task-specific facts and solutions"; GEPA prompt: Appendix A.4 (contains "330/360").
- Appendix D covers Jericho and WebArena-Lite only; Table 7 W-AUC 0.379 ID / 0.371 OOD vs main Table 1 0.396 / 0.414.
- Internal inconsistencies noted (neutral): abstract "up to 23% ID / 27% OOD" is W-AUC, Table 1 OOD average score is +33% (10.61 vs 7.99); Algorithm 2 inputs list δ and episode-0 baseline results but the rule is mean z̃ > mean z⋆; Tables 7–8 average score is normalised, Table 1's is raw.
- Spread statistics present: Figure 3 SE over five runs (Jericho), Table 6 ± SD (wall-clock); none in Tables 1–5, 7–8.
- The "+23%" etc. are the paper's own subscripts in Tables 1–3 and Sec. 4.2/abstract.
- "Strongest baseline" in the headline table is the highest baseline value (Naive Meta-Agent included among baselines) in that Table 1–3 W-AUC column; it is always a named method, not the Naive Meta-Agent, in the seven rows shown. The poster chart's third series is the Naive Meta-Agent value from the same column.
- No limitations section, no contamination/leakage test, no task counts and no standard deviations in tables were found in the full text including appendices; Figure 3 shades the standard error over five runs for Jericho (values not used).
- Naive Meta-Agent: the paper says only that it "shares the same architecture and models of Meta-TTL but uses an unoptimized self-improvement policy"; we do not claim it equals the seed meta-prompt.
- Table 5: GEPA's rollout count is not stated; 350 (Meta-TTL) vs 1,920 (GRPO) is stated in the caption.

## Judgment notes
No change to our judgment (batch b18) is warranted by the full paper. Observations: (1) `variance: unclear` stands — performance tables give means over 5 / 3 runs without SD; only Figure 3 (Jericho, SE) and Table 6 (wall-clock ± SD) show spread. (2) `held_out: partial` stands — Jericho ID is the meta-training games; WebArena-Lite and τ²-bench ID use held-out task instances, and OOD domains are unseen. (3) `budget_matched: unclear` stands — the only rollout-count comparison (Table 5) is 350 vs 1,920 against GRPO, and the main baselines receive no meta-training budget. (4) The `retained_ablation`/`improver_comparison` rows rest on the Naive Meta-Agent, whose relation to the seed meta-prompt the paper does not state.
