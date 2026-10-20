# SOURCE — FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness

Read from: arXiv 2606.17642v6
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, chart and tables on the poster were drawn by us from the paper's numbers. Authors as in the PDF title block: Pianran Guo, Pengcheng Zhou, Yuchen Jian, Shuhua Chen, Zhongliang Yang, Linna Zhou (BUPT; Queen Mary University of London).

## Where the numbers come from (PDF page numbers)
- Table 1 (headline, p7), Table 2 (FT/FM ablation, p7), Figure 2 and Section 5.4 (bank-size curve, p7), Section 5.5 and Figure 3 (tau, k_max, pp7-8), Limitations (p9).
- Appendix C (marginal gains, p12), Appendix D / Table 4 (memory strategy ablation, p12-13), Appendix E and Table 5 (retrieval stability, pp13-14), Table 6 (test sizes, p16), Tables 7-8 (baseline attribution, p17), Appendix G.2 (configuration, K = 8, pp15-16).
- Table 9 (five runs, p18), Table 10 (Reflexion/ExpeL, p18), Table 11 (other backbones, p17), Table 12 (235B, p18), Tables 13-14 (cost, pp18-19), Appendix L (prompts, pp19-21).

## ‡ numbers (computed by us)
- 27.48‡ = 55.15 (n = 0 point of Figure 2 / Section 5.4: FT tools with an empty bank) − 27.67 (Base, Table 1).
- 40.98‡ = 68.65 − 27.67 (FinAcumen − Base, BizBench, Table 1): the largest gain over Base in the poster title.
- 3.78‡ = 19.98 − 16.20 (FinAcumen − Base, FinTMMBench, Table 1): the smallest gain over Base in the poster title.
- 3.09‡ = 77.17 (Reflexion or ExpeL, FinMMR Easy, Table 10) − 74.08 (tools only, Table 2).
- 1.46‡ = 52.54 − 51.08 (Qwen2.5-VL-72B − FinAcumen, FinMME, Table 1).
- 8,756‡ = 2000 + 1200 + 1200 + 1000 + 1136 + 2220, the test sizes listed in Table 6 (the paper's Appendix E uses 11,379 test queries; the paper does not reconcile the two).
- 9.00‡ = 67.50 (Table 4 strategy E) − 58.50 (D); +17‡ = 81 (E) − 64 (D) on FinMMR Easy, Table 4 (per-benchmark cells are integers in the table).
- −0.05‡ = the per-step label between the 120 and 240 snapshots, read off Figure 2 (checked against the rendered page); Appendix C text gives −0.04 per 100 entries.
- "About twice" (tool gain vs memory gain): 14.91 / 7.59, 27.48‡ / 13.5, 11.85 / 5.80 are each about 2 (1.96, 2.04, 2.04); stated qualitatively, not as a number.

## Notes
- Table 1 values for FinAcumen and Base equal the five-run means of Table 9 (e.g. 68.65 and 27.67). The paper does not state what varies between the five runs (for example whether the bank was rebuilt); baselines in Table 1 are single published numbers.
- Baselines in Table 1 are copied from the benchmark papers (Appendix G.3), with per-cell model variants in Table 8 (e.g. GPT-4 on BizBench, GPT-4o on FinMMR, GPT-4o-mini on FinTMMBench, Claude 3.7 Sonnet, Llama 4 Maverick 17B). Poster labels for the best published model use those variants; for FinMMR Medium the best is Qwen2.5-VL-72B (63.42; GPT 63.33). Gemini 2.0 Flash is listed on FinMME at 51.85.
- The paper's text (Section 5.2) says FinAcumen "still trails the best General LLM on BizBench, FinMMR Hard, and FinTMMBench"; Table 1 also shows it below Qwen2.5-VL-72B (52.54) and Gemini 2.0 Flash (51.85) on FinMME. We use the table.
- Bank size: Sections 5.1 and 5.4 and Figure 2 use about 2,400 entries; Appendix K describes the bank as "approximately 1800-entry" and Appendix E uses snapshots up to 1200. Retrieval statistics in Table 5 are at 1200 entries.
- Table 4 (Appendix D) is a single run on a 600-question test subsample with MIN_COSINE 0.60 (main experiments: tau = 0.65); strategies A and B run without tools. It is in the blog only.
- tau was selected via hit rate over the test-query embeddings (Appendix E.1: 11,379 test query embeddings; no gold labels are used in a hit rate). The 500 questions used to select k_max are described only as "evenly split across BizBench and FinMMR-M"; the paper does not state whether they are disjoint from the test sets.
- Searched the main text and appendices: no write-time filter or pruning of bank entries is described, no overlap or contamination check between bank-source items and test items (other than the statement that the bank comes from training/validation splits and is frozen), and no accuracy ablation of the tau gate/fallback or of Findings vs Cautions.
- Cost figures (Table 13) are estimates "based on measurements from six source instances" for the ~1,800-entry bank; Table 14 uses a sixth of the test instances of each setting. CNY figures are as printed.

- Added after fact-check: Table 4 shows experience as the larger step (B to D +2.25, D to C +3.50, D to E 9.00‡), in tension with the tools-about-twice-memory splits (different setting: 600-question subsample, tau 0.60, gold answers in rows B to E); the paper states 'Experience provides the dominant marginal improvement' and does not reconcile. The paper does not state how many runs Table 4 or each Figure 2 snapshot has (the 2400-entry point 68.65 equals the Table 9 five-run mean).
- Soft gates: the annotator prompt says 'If you cannot map entities, the entry is NOT useful' and the solver prompt has an opt-out (<OptOut>, 'skip if irrelevant'); not reported separately.
- Unreconciled: Section 5.5 hit rate 79.8% at 1200 entries (tau 0.65) vs Table 5 global 0.71; Section 5.4 'saturation beyond 1800' vs Appendix C '2400 as the saturation knee'; Section 5.1 '~2,400 experience accumulation trajectories' vs K = 8 per item; Algorithm 1 flag omega (consolidation at inference) undefined; Figure 10 badge FinMME 11,099 samples vs 2220 test items. Table 5 values come from a 1200-entry snapshot built uniformly across benchmarks; Appendix K cost is for a ~1,800-entry bank.
- 'Older variants' removed: that was our characterisation, the paper does not say it.

## Judgment notes
No change to our judgment (research/judgments/b17.jsonl, v6): held_out yes, variance yes (five evaluation runs, Table 9), optimizer_cost yes, retained_ablation yes, budget_matched unclear (no matched-compute row found), cross_task unclear, leakage_guard untested, evidence level retained — all consistent with the full paper. One flag for the maintainers: Appendix I / Table 10 compares FinAcumen with Reflexion and ExpeL (same backbone, tools and training data, four settings, single numbers), which bears on `improver_comparison` (judged unclear); the judged text may not have included the appendices. We do not edit judgment files.
