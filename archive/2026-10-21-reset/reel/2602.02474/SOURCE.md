# SOURCE — MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

Read from: arXiv 2602.02474v2
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but we reused nothing. The method diagram, bar charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from (PDF page numbers)
- Table 1 (headline, p6); Table 2 (ablation, p8); Table 3 (runtime cost, p9); Figure 3 (HotpotQA transfer; values read from the bar labels, p7); Table 4 (extra ALFWorld baselines, p11); Table 5 (ALFWorld without demonstrations, p12); Table 6 (AppWorld, p13); Table 7 (8B model, p14).
- Datasets, splits and evaluation details: Appendix B.1 (p14). Designer, hard-case buffer, rollback rule (Eq. 4 to 8): Appendix B.2 (pp14-15) and Section 3.4 (p5). Training objective: Appendix B.4 (pp16-17). Evolved skills: Appendix C (pp18-27). Prompts: Appendix D (pp27-31). Limitations: Appendix F (p32).
- "Strongest baseline" per column on the poster/blog = the highest baseline cell the paper reports for that setting (Tables 1, 3 and 4; one rule for all cells). LLaMA: LoCoMo F1 MemoryOS 41.39, L-J LightMem 51.95 (Table 3 only; A-MEM 49.71 is the best in Table 1), LongMemEval F1 CoN 30.78, L-J CoN 56.44, ALF-Seen CoN 75.00, ALF-Unseen Mem0 81.34; Qwen: MemoryOS 39.86, CoN 50.96, CoN 29.19, Mem0 46.20, CoN 77.14). For Qwen ALF-Unseen the poster uses Expel 71.64 from Table 4 (higher than CoN 70.90 in Table 1). Table 4 baselines on LLaMA ALFWorld (LightMem, AWM, Expel) and Qwen Seen (Expel 75.71) are below the Table 1 best. The No-Memory row is "-" for LoCoMo/LongMemEval and lower on ALFWorld.
- Mapping of the garbled text extraction of Table 1 was checked against the rendered page image.

## ‡ numbers (computed by us)
- 2.54‡ = 80.36 (MemSkill, LLaMA ALFWorld average, Table 1/4) − 77.82 (Mem0, LLaMA ALFWorld average, Table 1).
- 7.27‡ = 81.29 (MemSkill, Qwen ALFWorld average) − 74.02 (CoN, Qwen ALFWorld average, Table 1).
  Context: Appendix A.1 says MemSkill beats "the strongest baseline LightMem by 5.53 points" (LLaMA) and "Expel by 7.61 points" (Qwen); those are the strongest among the baselines added in Table 4 only. Table 1 has higher baseline averages (Mem0 77.82 and CoN 77.80 on LLaMA; CoN 74.02 on Qwen).

- 1.87‡ = 53.82 (MemSkill, LoCoMo L-J, LLaMA, Table 1/3) − 51.95 (LightMem, Table 3).
- 1.29‡ = 26.71 (MemSkill, AppWorld average PR without demonstrations, LLaMA, Table 6) − 25.42 (AWM, nearest baseline; Mem0 is 24.32).

## Notes (non-decimal inferences and caveats)
- ALFWorld test sizes are not stated. The reported percentages match the official 140 Seen / 134 Unseen tasks (our inference): Seen 77.14 vs 75.00 = 108 vs 105 tasks, Unseen 83.58 vs 81.34 = 112 vs 109, Qwen Unseen 76.87 vs 71.64 = 103 vs 96. Stated in the blog only as "if the official sizes were used".
- LoCoMo: about 200 queries per sample (App B.1), so about 2 test conversations is roughly 400 questions before adversarial removal (our inference). The paper creates a LoCoMo validation split (6/2/2) and never says what it is used for; the split behind Table 2 is not stated (its full-model row equals Table 1, so probably test).
- Table 3 sweeps span size on the LoCoMo LLaMA run; the Table 1 headline (53.82) is the SS=512 row, the best of the five (SS=128 53.14, 256 51.61, 1024 48.11, 2048 50.46). The paper says 512 is the default and "best overall balance" and does not say it was chosen on validation.
- HotpotQA baselines (Figure 3): §4.3 calls MemoryOS and A-MEM "the most competitive methods on conversational benchmarks in Table 1", but on LLaMA CoN's conversational average L-J (49.08) is above MemoryOS (44.24) and A-MEM (43.88); CoN and LightMem are not shown. §4.3's "increasing K generally improves performance" is not monotone at 100 docs (K=3 68.75 > K=5 68.36); "consistently outperforms" holds for K = 7 only (K=5 is below both baselines at 50 docs).
- All L-J scores use gpt-oss-120b with a 0 / 0.5 / 1 rubric (App B.1, D).
- Snapshots and rollback concern "the skill bank" (§3.4, App B.2); the paper does not say what happens to controller weights on rollback.
- Appendix C lists 9 LoCoMo and 7 ALFWorld skills in total (4 initial primitives plus 5 and 3 additions, some primitives refined). Figure 4 and §4.5 call them "representative", so these are not confirmed final bank sizes.
- ExpeL and AWM appear as baselines in Tables 4 to 6 (ALFWorld / AppWorld only); the paper does not say what training or tuning any baseline receives, so the blog says "not stated" instead of "none".
- Eq. 4 as printed, d(q) = 1 − r(q)·c(q), falls with the failure count c(q), although the text says higher d marks more critical cases; the blog notes this and relies on the text.
- LoCoMo has 10 samples split by sample 6/2/2 (Appendix B.1), so the test set is about 2 conversations (our inference; the paper does not state the test query count). LongMemEval test is "approximately 100 samples". ALFWorld test-set sizes are not stated.
- No seeds, repeats or standard deviations appear anywhere in the paper; all tables are single numbers.
- The paper does not name the designer LLM. Training/evolution cost is not reported ("preparation cost is amortized"); Table 3 is inference-time cost on LoCoMo (LLaMA) only. Which split Table 2 is measured on is not stated; whether the controller is retrained for each ablation is not stated.
- Baselines: all use up to 20 retrieved memory items; the paper does not describe training or tuning for them. The designer is compared with "no designer" and "refine-only", not with another memory-skill evolver.
- Selection of the best skill bank uses the training-reward estimate (Eq. 8), not a held-out score. The patience value is not given. Eq. 4 as printed, d(q) = 1 − r(q)·c(q), decreases with the failure count c(q), although the text says higher d marks more critical cases; we did not rely on the formula.
- LongMemEval is "transfer", but Appendix B.1 says its validation split is used to tune dataset-specific configurations.
- HotpotQA (Figure 3): K = 3 variant is below both MemoryOS and A-MEM at 50 docs (64.06 vs 66.02 / 65.63) and 200 docs (59.76 vs 60.55 / 61.72); K = 5 is below both at 50 docs (64.85). How K was selected is not stated; only these two baselines are shown.
- Figure 3 values read from bar labels: 67.97, 62.89, 59.76, 60.55, 61.72 (200 docs); 71.48, 68.36, 68.75, 67.19, 66.80 (100 docs); 67.57, 64.85, 64.06, 66.02, 65.63 (50 docs).

## Judgment notes
Consistent with our judgment (batch b18, score 70, evidence level improver): `variance: unclear` (no seeds/SD found), `budget_matched: unclear` (no matched-compute or baseline-tuning row), `optimizer_cost: unclear` (only runtime cost, Table 3), `leakage_guard: unclear` (only split design: by conversation sample for LoCoMo, non-overlapping trajectories for ALFWorld; no test), `held_out`/`cross_task: yes` (LongMemEval, HotpotQA, Qwen transfer). One nuance for the record: the LongMemEval "held-out" result still used that dataset's validation split to tune configurations (Appendix B.1). The `code: unclear` field in the b18 evidence block is superseded by the score record (code URL found, code = 10).
