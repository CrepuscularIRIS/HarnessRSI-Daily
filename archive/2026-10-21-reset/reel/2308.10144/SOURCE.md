# SOURCE — ExpeL: LLM Agents Are Experiential Learners

Read from: arXiv 2308.10144v3
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but we reuse nothing: the method diagram and charts on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Headline success rates (HotpotQA, ALFWorld, WebShop; ReAct, insights-only, retrieve-only, ExpeL, Reflexion R1-R3): Figure 5 (p8); integer values are read from the bar / line labels. Decimals for ReAct and ExpeL on HotpotQA and ALFWorld: Table 3 (p10).
- Insight-source and retrieval ablations: Table 3 (p10). Experience ablation (27, 28, 35, 39): Figure 6 (p9), read from the bar labels. Transfer: Table 1 (p9). Reflexion rounds: Table 2 (p9).
- ALFWorld per-type success and WebShop reward: Table 5 (p36). Tokens per trajectory: Table 6 (p38).
- Test-set sizes, fold description, models: Appendix D.1 and D.5 (p14), Table 4 (p15). Insight operations and counts: Section 4.2 (p5). Limitations: Section 6 (p10).

## ‡ numbers (computed by us)
- 11‡ = 39 − 28 (ExpeL minus ReAct, HotpotQA, Figure 5 / Table 3).
- 19‡ = 59 − 40 (ALFWorld, Figure 5 / Table 3).
- 6‡ = 41 − 35 (WebShop, Figure 5).
- 3.3‡ = 4310.06 / 1319.75 (HotpotQA tokens per trajectory, Table 6) = 3.27.
- "+11" on the poster is the same 11‡.
- 10‡ = 39 − 29 (ExpeL minus Act, HotpotQA, Figure 5).
- 8‡, 4‡, 3‡ = ExpeL minus retrieve-only: 39 − 31 (HotpotQA), 59 − 55 (ALFWorld), 41 − 38 (WebShop), Figure 5. 15‡ = 55 − 40 (retrieve-only minus ReAct, ALFWorld).
- 1.39‡ = 2856.7 / 2051.49 (ALFWorld) and 1.28‡ = 3291.31 / 2575.41 (WebShop), Table 6.
- Poster "+13" and "−4" (ALFWorld clean, cool) = ExpeL minus ReAct in Table 5: 74 − 61, 67 − 71.

## Notes
- The Reflexion lines (R1-R3) in Figure 5 are the paper's ReAct+Reflexion baseline, which retries on the test tasks with environment feedback; ExpeL is a single attempt. We state this as a difference in setup, not as a flaw.
- Figure 5 integers vs. Table 2 decimals differ only by rounding (retrieve-only 55 vs 54.5; ExpeL 59 vs 59.0).
- The paper says "four-fold validation" but Appendix D.1 describes training on one half and evaluating on the other half and vice versa; we report both wordings as written. The number of training tasks N is not given in the text. No variance beyond folds is reported (decoding is greedy, temperature 0).
- Table 3's ReAct ALFWorld 40.0 and Table 2's ReAct+Reflexion R0 40.3 are shown as reported.
- Table 6 token counts are "average counts per trajectory"; we do not know from the paper whether they include the few-shot prompt, and we call them "tokens per trajectory".
- Table 5 ExpeL vs ReAct by type: put 83/50, clean 74/61, heat 43/13, cool 67/71, look 39/0, puttwo 29/0. Per-type ALFWorld counts are not given in the paper; we say so.

- Fig. 5 caption names ReAct and Act as baselines (imitation learning is also below ExpeL: ALFWorld 37, WebShop 29); the Reflexion lines are outside that set.
- Task counts 100 / 134 / 100 are pool sizes; with the half/half split each fold evaluates about half of them. Reflexion lines in Fig. 5 and Fig. 6 carry no SE. Table 1: gpt-4-0613 rewrote the insights for FEVER (Sec. 5.4); Act and ReAct got no such help.

## Judgment notes
None that change the judgment (batch b00): `retained_ablation: yes`, `cross_task: yes` (a single HotpotQA to FEVER pair; the paper's own wording), `variance: yes` (mean ± standard error over folds; the fold description is inconsistent as noted above), `budget_matched`, `optimizer_cost`, `improver_comparison` and `leakage_guard` unclear. The full paper is consistent with these; we found no matched-compute row, no cost for gathering and gpt-4 extraction, and no leakage check. The poster also notes that baselines do not receive the gpt-4-0613 extractor, which the judgment does not address.
