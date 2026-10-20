# SOURCE — The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?

Read from: arXiv 2606.04455v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers. Authors as in the PDF title block: Xinyu Lu, Tianshu Wang, Pengbo Wang, Zujie Wen, Zhiqiang Zhang, Jun Zhou, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun (CIPL, Institute of Software, CAS; UCAS; Ant Group).

## Where the numbers come from
- Table 1 (reasoning domains, p7), Table 2 (SWE-Bench / Terminal-Bench, p8): every score, SD and † mark; all per-run values.
- Section 5.2 findings 1-3 (pp7-8): "5 of 39", 33%, 0.053, five flagged trials. Section 5.1 (p7): red-team of 8 trials. Section 4 (p6): budgets (12 h / 24 h), models, baselines, 2,500 search calls. Section 5.4 (p10): 46% / 23%. Section 6 (p10): limitations.
- Appendix A.1 (pp12-14): audit agent (Claude Opus 4.6 backbone). Appendix B.3.1 (pp19): exfiltration case, 591 questions. Appendix C (pp19-20): dev/test split sizes. Appendix B (pp17-18): "12-hour" wording.
- Figure 3 (p9): correlations, read off the figure titles (see below).

## ‡ numbers (computed by us or read off a figure)
- 0.011‡ = 0.744 (Claude-Opus-4.6, Meta-AIME avg) − 0.733 (human baseline), Table 1.
- 0.002‡ = 0.557 (Claude-Opus-4.6, Meta-LiveCodeBench) − 0.555 (human baseline), Table 1.
- 0.050‡ = 0.783 (Claude-Sonnet-4.6, Meta-AIME) − 0.733, Table 1.
- 0.067‡ = 0.393 (Claude-Opus-4.7, Meta-Terminal-Bench) − 0.326 (Terminus-2), Table 2.
- 0.019‡ = 0.345 (DeepSeek-v4-Pro, Meta-Terminal-Bench) − 0.326 (Terminus-2), Table 2.
- 0.025‡ = 0.597 (human baseline, Meta-GPQA) − 0.572 (Claude-Opus-4.6, best meta-agent average), Table 1.
- 0.028‡ = 0.637 (Terminus-2, Meta-SWE-Bench) − 0.609 (Claude-Opus-4.7, best meta-agent average), Table 2.
- 7‡: see the count note under Notes.
- 0.017‡ = 1/60, the value of one AIME test problem (the test split has 60 problems, Appendix C).
- 0.444‡, 0.384‡, 0.024‡ = Pearson r of Figure 3 panels (mean eval interval +0.444, runtime +0.384, number of eval calls −0.024), read off the panel titles of Figure 3 on p9 and checked on the rendered page. The paper gives no number of points.

## Notes
- "5 of 39 configurations" is the paper's count. We reproduce it as: AIME Opus-4.6 and Sonnet-4.6, LiveCodeBench Opus-4.6, Terminal-Bench Opus-4.7 and DeepSeek-v4-Pro, comparing the agentic domains with Terminus-2 (the stronger baseline). 7‡ = count against OpenHands in the agentic domains, computed by us from Tables 1-2: the three reasoning passes + Terminal-Bench Opus-4.7 (0.393), DeepSeek-v4-Pro (0.345), Sonnet-4.6 (0.296) vs OpenHands 0.285 + SWE-Bench Opus-4.7 (0.609) vs OpenHands 0.544. Model rosters differ between Tables 1 and 2 (Kimi-K2.5 only Table 1; Claude-Opus-4.7 and DeepSeek-v4-Pro only Table 2; MiniMax-M2.5 / GLM-5 become M2.7 / 5.1). 39 = 7 models × 3 reasoning domains + 9 models × 2 agentic domains.
- "33% of configurations have SD > 0.1": the paper's statement; we counted 13 of 39 cells with SD above 0.1 in Tables 1-2.
- The chart shows, per domain, the best meta-agent 3-run average against the strongest baseline average in that domain (Terminus-2 for SWE-Bench / Terminal-Bench). The human-baseline rows of Table 1 are not described in the text.
- "Three of the five passing configurations are within one SD" is our reading: Opus-4.6 AIME (gap 0.011‡, SD 0.054), Opus-4.6 LiveCodeBench (0.002‡, SD 0.043), DeepSeek-v4-Pro Terminal-Bench (0.019‡, SD 0.028).
- "Flagged runs stay in the means (0.017, 0.060, 0.135, 0.468)": the four † runs of Tables 1-2 (GPT-5.3-Codex AIME run 2, SWE-Bench run 1, Terminal-Bench run 2; Gemini-3.1-Pro SWE-Bench run 3). The paper says five trials were flagged (Finding 3); we could not locate a fifth † in the tables. The Appendix B.3.1 case study is in the science domain (GPT-5.3-Codex), which carries no † in Table 1, and is described as observed during benchmark development.
- Test sizes: AIME 60, GPQA Diamond 198, LiveCodeBench 323, SWE-Bench Verified 250 (Appendix C). Terminal-Bench 2.0 size is not stated in the paper; we give none.
- "Each model ran in one scaffold": Section 4 and Tables 1-2; open-weight models run inside Claude Code, GPT models in Codex, Gemini in Gemini-cli.
- "Does not report" in Our read, from a full-text search of the main text and appendices: no ablation of what in the retained artifacts matters, no cross-task transfer of an artifact, no comparison of improvement mechanisms, no numeric API quotas (only the 2,500 search calls), no contamination test for the artifact model (the limitations section names contamination as a risk), no re-run of flagged artifacts without the exploit, no scores for the described "Naive Agent". Meta-agent API cost is shown only for SWE-Bench and Terminal-Bench in Figure 4.

- Confounds (Section 4, Appendix B): on SWE-Bench / Terminal-Bench the artifact model is Claude Haiku 4.5; Appendix B artifacts by Claude-Opus-4.7 use cache_control prompt caching and extended thinking. The paper does not state which LLM Terminus-2 / OpenHands used or whether baselines ran on the same artifact model and quotas (our full-text search). No GPT or Gemini configuration exceeds a human-baseline average (checked in Tables 1-2).
- Wording we deliberately kept to the paper: 'flagged five trials' (Finding 3) is not tied to ordinary runs; the test run is 'executed' (Section 3.2), we do not claim 'once'; Figure 3 regressions are per feature; the zero-reward checkpoint cause is stated for 'several' failures, not linked to a specific run.

## Judgment notes
Our judgment (batch b12, score 70, evidence level `retained`) is consistent with the full paper: `held_out: yes`, `variance: yes` (3 runs/cell, SD), `budget_matched: partial` (time fixed per domain, API quotas enforced but not given), `optimizer_cost: partial`, `leakage_guard: tested` (red-team audit of 8 trials; ordinary-run miss rate not reported), `cross_task`, `retained_ablation` and `improver_comparison` unclear/absent. One point for readers: the artifact is scored on a split whose labels the meta-agent cannot read, but the dev and test splits are different datasets in AIME (years), science (HLE vs GPQA Diamond) and Terminal-Bench (Pro vs 2.0), so this is a distribution-shifted held-out test. Paper-internal inconsistencies, reported neutrally and table values used: five flagged trials in text vs four † in tables; "Naive Agent" baseline described but absent from Tables 1-2; Appendix B says "12-hour" sessions for the SWE-Bench / Terminal-Bench artifacts while Section 4 gives 24 hours for those domains.
