# SOURCE — EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer

Read from: arXiv 2607.05202v1
Paper figures shown: none

License: CC BY-SA 4.0 (figure reuse allowed). We reused no figure: the pipeline diagram, the gain chart and the tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Table 3 (headline: per-cell accuracy, SE and Δ, Average column, p7); Table 4 (turn-cost change, p8); Table 2 (split sizes, p6); Table 6 (graph statistics, p13); Table 5 (raw-card statistics, p12); Table 7 (support, p13); Table 8 (information access, p14); Sections 3.2 (pp4-5), 4.1 (p6), 4.2-4.4 (pp6-8); Limitations (p9); Appendix A.2-A.6 (pp12-13), Appendix C (p14).
- Data link: the poster's second QR points to https://huggingface.co/datasets/EverMind-AI/EvoAgentBench, the exact URL given in the paper's abstract (the candidate list has the organisation page only). No code repository is named in the paper.

## ‡ numbers (computed by us)
All counts come from Table 3 (24 cells per method = 4 domains x 2 scaffolds x 3 backbones). Cell Δ values were re-derived from the table's own accuracies to check the parse.
- Memento negative cells = 7‡: Qwen3.5-27B Nanobot SWE (−36.3); Qwen3.5-397B OpenClaw SWE (−3.0), OpenClaw KW (−5.8), Nanobot KW (−1.2); Gemma-4-31B OpenClaw Algo (−4.3), SWE (−4.8), KW (−10.9). The paper states the counts for GEPA (4), ReasoningBank (6) and Anchor (0, "positive in every cell"); the counts reproduce from the table.
- "|Δ| smaller than the cell's own SE": Memento 16‡, ReasoningBank 11‡, GEPA 14‡, Anchor 6‡ of 24. Each Δ (as printed) is compared with the SE printed for the same method cell. This is not a test and not the SE of a difference; the paper reports no significance test.
- "An automatic method scores above Anchor in 3‡ of 24 cells": Qwen3.5-27B Nanobot SWE (ReasoningBank 53.0 vs Anchor 49.4); Gemma-4-31B OpenClaw SWE (GEPA 42.3 vs 32.7); Gemma-4-31B Nanobot SWE (GEPA 37.5 vs 26.8).
- "The other seven Memento cells on Qwen3.5-27B are positive" is read from Table 3 (+0.5, +2.0, +2.9, +0.7, +3.6, +4.3, +3.7); the printed average −2.4 is the paper's.

## Notes
- The Average column in Table 3 is the equal-weighted mean over four domains and both scaffolds (eight cells), as stated on p6; it is not weighted by task count.
- "Anchor exceeds the best automatic method by +3.9 and +7.0" and "GEPA nearly matches Anchor on Gemma" are the paper's own statements (p7); both reproduce from the Average column (45.0 vs 41.1; 59.7 vs 52.7; 42.5 vs 42.4).
- Our statements on what is NOT reported (random-split comparison, routing-vs-content or teacher-matched ablation, empirical leakage / near-duplicate test, evolution-step cost or compute, whether evolution is repeated across the three runs, significance tests) come from reading the whole paper including the appendix: none of them appears. Appendix B (Table 8, pp13-14) is an access-control protocol (no test answers, traces or raw cards reach automatic methods or Anchor), not an empirical leakage test; the Limitations paragraph only discusses pretraining contamination. The only budget stated is a top-10 retrieval budget for skill- and case-based methods (A.6, p13).
- Cell SE range 2.2-5.9 is the min/max of all SEs printed in Table 3.
- Teacher asymmetry: Anchor's extractor (Claude Sonnet 4.6) sees the ground-truth target of training tasks and the traces of Kimi-K2.5 / GLM-5.1 / DeepSeek-V3.2 (Sec 3.2.2, A.3). Automatic methods use their own rollouts with the evaluation scaffold-backbone (Protocol, p6); Sec 3.1 allows construction traces as input but no experiment gives them to the automatic methods. The paper argues the protocol, if anything, favours the automatic methods. We do not claim the construction backbones are stronger (the paper does not say). Vanilla Web accuracy for Qwen3.5-27B and Gemma-4-31B is 8.7-13.3 (10.8, 8.7, 13.3, 9.2, Table 3). The paper does not say which LLM runs inside the automatic methods' reflection / distillation steps.
- Split-rule wording differs: Sec 3.2.5 (p5) requires shared support with a train task in the test task's own community; the A.6 algorithm (p13) requires only that some family of the task has train support (no community clause). Blogs state both. Headroom signal: Sec 3.2.5 and Limitations say it is the no-evolution scores of the construction backbones (A.6 says only 'baseline reward'); the blogs follow Sec 3.2.5.
- Table 1 marks EvoAgentBench 'Cross-Task ✓' (held-out tasks from the same domain). The blogs/poster therefore say 'cross-domain transfer' (an artifact evolved in one domain used in another) is not reported.
- Anchor within-SE count: 6 of 24 (‡), incl. Gemma-4-31B OpenClaw Algo +0.4 (SE 4.6); §4.2 says the gap 'cannot be attributed to evaluation noise or task difficulty' with 3 runs and no significance test; blogs and poster pair '24 of 24' with this.
- No internal inconsistency found in the tables: Table 2 totals (528 / 267 / 170 / 56), Table 6 nodes (1,108) and Table 5 tasks (2,516) add up.

## Judgment notes
None that change the judgment (batch b12): `budget_matched: partial` matches the paper (test-time environment matched; no evolution budget reported), `optimizer_cost` and `improver_comparison: unclear`, `cross_task: no` (the paper's Table 1 marks 'Cross-Task ✓' for held-out tasks within a domain; no cross-domain transfer of an evolved artifact is reported, which is how we read the `no`), `leakage_guard: untested`, `variance: yes` (three runs per instance with SE; whether evolution is repeated is not stated). The `code: yes` credit rests on a Hugging Face dataset link, not a code repository. No judgment file was edited.
