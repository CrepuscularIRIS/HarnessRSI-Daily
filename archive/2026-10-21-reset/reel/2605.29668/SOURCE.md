# SOURCE — GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents

Read from: arXiv 2605.29668v3
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed). We reused no figure: the method diagram, bar charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Table 1 (headline, p5), Table 2 (cross-model transfer, p6), Table 3 (cross-benchmark transfer, p7), Table 4 (ablation, p7), Table 5 (gate granted to baselines, p8), Table 6 (non-clinical, p8), Table 7 (calls and library size, p16), Table 13 (confidence intervals, p19), Table 9 (split sizes, p16), Table 14 (cross-writer transfer, p20), Table 16 (probe calls, p20), Appendix F (ground-truth audit, p21), Limitations (p10), §3.4 (training protocol, p4).
- Per-model "strongest baseline" bars on the poster: gpt-oss-120b Evo-MedAgent 67.8, DeepSeek V4 Flash SkillX 55.9, Gemini 3.1 Flash Lite Evo-MedAgent 55.2, GPT-4.1 Batch Memory 47.4, GPT-5.4 (low) Seq. Memory 47.4 (Table 1; matches the comparisons in Table 13).

## ‡ numbers (computed by us)
None. Every decimal number in the blogs and on the poster is printed in the paper.

## Notes
- "At most 10 skills" is the capacity listed in Table 7 ("capacity-bounded (≤10)"); "5 skills on average, 5.6k tokens" is from §3.4 and Table 7.
- "half failing / half passing": the probe holds up to N/2 previously failing and N/2 previously passing samples with N = 36 (§2.2, §3.4).
- Cross-writer baseline comparison (Appendix E.5 / Table 14): the baselines are the *ungated* self-trained versions, run in two writer-to-executor configurations only (Limitations); their GPT-5.4 libraries are weak at source (OOD 1.7 to 16.7). A gated-baseline transfer was not run. The blogs and poster do not claim more.
- Table 2 exceptions to "weaker-writer libraries are worse than self-training": Gemini→gpt-oss OOD 57.8 vs 56.3; gpt-oss→Gemini test 79.7 vs 71.4. The paper draws no conclusion from Gemini-source cells (OOD SD above 30).
- Seed counts: Tables 4, 12 and 2 are labelled three seeds, but the full-method 88.8 ± 5.8 equals the five-seed Table 1 entry and the Table 2 diagonals reproduce Table 1; the rows are therefore not clearly seed-matched. Stated as an observation.
- Table 5 at equal K=1: GRASP 73.4 ± 23.1 test / 50.9 ± 20.0 OOD vs gated Evo-MedAgent 69.4 ± 9.2 / 30.7 ± 11.8. We describe the in-domain gap as inside the noise; no difference is computed.
- Table 13: MAB OOD 56.3 vs 31.3 has CI [3.7, 44.0] and p = 0.087; three-seed rows have a p floor of 0.10; no multiple-comparison correction.
- Non-clinical (Table 6) is described by the paper as exploratory: gpt-oss-120b, three seeds, compared with no skills only; test sizes from Table 9 (ALFWorld 20, OS Interaction 35, WebShop 50, DBBench 60).

## Judgment notes
- `improver_comparison: unclear` and evidence level `retained` (batch b14). The full paper does vary and compare the improvement mechanism itself: Table 4 removes the gate (K=4 and K=1), uses matched-compute selection without the probe scores, restricts the writer to ADD and selects on fixes only; Table 5 grants the same gate to all five baselines at K=1 and K=4. This looks like improver-level evidence that the condensed text cut.
- `leakage_guard: untested` (batch b14). The full paper contains a ground-truth audit of all 106 learned libraries across dev, validation, test and OOD (Appendix F, p21): no held-out value in any Trigger, Rule or Verification section; 30 dev-split episode-specific values, all inside demonstrations or code blocks; 4 collisions with hidden splits that are low-entropy domain constants. The blogs and poster state this as what the paper reports. 
No judgment file was edited.
