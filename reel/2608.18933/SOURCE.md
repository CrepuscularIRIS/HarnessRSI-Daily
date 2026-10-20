# SOURCE — SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

Read from: arXiv 2608.18933v1
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but no paper figure is used. The method diagram, chart and tables on the poster were drawn by us from the paper's numbers.

Authors (title block, p1): Silin Chen*, Han Li*, Xiaodong Gu†, Yuling Shi, Haibing Guan; Shanghai Jiao Tong University. * equal contribution, † corresponding.

## Where the numbers come from (PDF pages; the paper has 12 pages and no appendix)
- Table I (Verified main results, Pass@1 and Avg Cost, controlled variants, p6); "averaged over three runs", temperature 0, 250-step budget, BM25 top-5 (p6).
- Table II (SWE-bench Pro, p7); Table III (component ablation, p7); Table IV (cross-LLM transfer, p7).
- Temporal-isolation protocol, 577 synthesized issues (p6); dataset sizes 500 / 731 (Section III-B, p5).
- Hyperparameter sweep: Fig. 4 and text (p8): 62.3, 69.7, 67.5, 63.2. Per-repository results: Fig. 5 and text (p8): 13.6, 15.6, 11.8, 4.5, 9.1, 2.0.
- Discussion / threats to validity (Section V, pp9–10): manual inspection, issue-type distributions "do not overlap", test-coverage and LLM-written-statement limits.
- 0.0‡% for DeepSeek on Astropy (SkillForge) is read off the Figure 5 bar label (p8, checked at 400 dpi); it is not in the paper's running text. The poster shows it as "0.0%".

## ‡ numbers (computed by us, or read off a figure where stated)
- 2.2‡ = 60.6 (SkillForge) − 58.4 (EvoCoder), GPT-5-mini, Verified, Table I. EvoCoder is the highest other row in that column; the paper's text names MemGovern (58.0) as the strongest competitor and reports +2.6 against it. "About 11‡ tasks" = 2.2 / 0.2.
- 0.2‡ = 100 / 500 (one task on SWE-bench Verified, 500 tasks); "about 15‡ tasks" = 3.0 / 0.2.
- 2.0‡ = 68.4 − 66.4; 1.4‡ = 67.8 − 66.4 (DeepSeek-V3.2, Table III vs Table I Mini-SWE-Agent); 2.6‡ = 57.6 − 55.0; 2.2‡ = 57.2 − 55.0 (GPT-5-mini).
- 0.0‡ (cross-model, Table IV) = 55.0 (GPT-5-mini with DeepSeek-V3.2's skills) − 55.0 (Mini-SWE-Agent, Table I).
- 7.4‡ = 69.7 − 62.3 (Fig. 4 text values, k = 5 vs k = 0).
- 22‡ (Astropy task count) is our inference from the Fig. 5 label steps: 4.5 ≈ 1/22, 9.1 ≈ 2/22, 13.6 ≈ 3/22. The paper gives no per-repository counts.
- Read off Figure 5 (p8, 400 dpi), not in the paper's running text: 0.0‡ (SkillForge, DeepSeek, Astropy); 9.4‡ (SkillForge, DeepSeek, Scikit-learn; SWE-Exp is +15.6 there); 2.9‡ (SWE-Exp) and 2.7‡ (SkillForge), GPT-5-mini, Sympy; 9.1‡ (both methods, DeepSeek, Pydata); 12.9‡ (SWE-Exp, DeepSeek, Sphinx; SkillForge is +13.6, in the text); +7.4‡ (SkillForge, GPT-5-mini, Django). The GPT-5-mini Scikit-learn tie (+15.6 both) is also read off the figure. The poster shows 0.0% for DeepSeek Astropy.
- "19 of 20 Verified values are multiples of 0.2" (Table I; Tables III and IV too) is our count: 68.7 is the only Table I Verified value that is not (68.7 × 5 = 343.5). Pro values in Table II are consistent with whole counts out of 731 (for example 28.3% ≈ 207/731, 34.1% ≈ 249/731, 51.7% ≈ 378/731). The paper states only "averaged over three runs", "temperature is 0" and "default inference settings".

## Notes and internal inconsistencies of the paper (we use the table values)
- p6 text: "MemGovern is the strongest competitor (69.2%/58.0%)" — in Table I, EvoCoder on GPT-5-mini is 58.4%, above MemGovern's 58.0%. SkillForge's 60.6% still exceeds both.
- Fig. 4(a): the text says the "full" retrieval condition drops to 67.5%; the plotted "full" point looks lower than that (read by eye, not given as a number). We quote only the text value.
- Fig. 5: the text says SkillForge improves over the baseline on all seven repositories under both backbones "without any regression"; the DeepSeek / Astropy label reads 0.0%. The caption says "Baseline and our method" while the figure and text show three methods (Baseline, SWE-Exp, SkillForge).
- "Best other method" bars on the poster take the highest other row per column from Tables I and II (Verified DeepSeek: MemGovern 69.2; Verified GPT-5-mini: EvoCoder 58.4; Pro: Live-SWE-agent 32.4 / 49.1). On Pro only SWE-Exp and Live-SWE-agent were evaluated ("available for each benchmark").
- Daggers in Tables I–II mean p < 0.05; the footnote names neither the test nor the comparison. The text states the Pro gains over Mini-SWE-Agent are significant. The paper gives no standard deviations; only Table I is stated to average three runs.
- Verified protocol: the LLM that "localizes semantically relevant tests" on the rolled-back snapshot — its input is not stated. No temporal-isolation protocol is described for SWE-bench Pro (we searched the whole text; no appendix exists). The paper does not discuss pre-training exposure of the evaluated LLMs to SWE-bench.
- The hyperparameter sweep (k_r, k_s) uses Django and Sphinx with GPT-5-mini only, the same repositories as the evaluation; the paper does not say how the default (k = 5) was selected.
- The paper says the manual inspection of skills and problem statements was done but gives no counts.
- The poster's "keep/reject rule" is our reading: a synthetic instance exists only if the rewrite makes tests fail (p3); the paper describes no further skill filter or validation signal and no iteration of the pipeline.

## Judgment notes
Our judgment (batch b02, score 69, ★★, evidence level retained) is consistent with the paper in its main lines (`budget_matched: unclear`, `cross_task: unclear`, `improver_comparison: unclear`). Two items are weaker than the record reads:
- `variance: yes` rests on the statement that Pro gains are "statistically significant"; the paper gives only a dagger (p < 0.05) with no named test or comparison, no standard deviations, and states a three-run average only for Table I.
- `leakage_guard: tested` rests on a comparison of issue-type distributions of synthetic vs real issues plus manual inspection; this is a distribution check, not a test for overlap between the synthetic issues / skills and the evaluated instances. The temporal protocol is described for Verified only.
We have not edited any judgment file.

## Further notes (second pass)
- Cost comparison (Table I, Verified; DeepSeek / GPT-5-mini): SkillForge $0.074 / $0.066. Cheaper than SWE-Debate ($0.382 / $0.167) on both models; cheaper than SWE-Exp ($0.090) and SAGE ($0.081) on DeepSeek only. On GPT-5-mini it is more expensive than SWE-Exp ($0.065), SAGE ($0.052), EvoCoder ($0.052) and Live-SWE-agent ($0.042); on DeepSeek more expensive than EvoCoder ($0.064) and Live-SWE-agent ($0.050).
- Dagger pattern in Table I does not follow the size of the gain: EvoCoder GPT-5-mini (+3.4) has no †, SWE-Exp GPT-5-mini (+1.6) and SAGE GPT-5-mini (+1.0) have †; SWE-Debate GPT-5-mini (56.4) has none while SkillForge w/ SWE-Smith GPT-5-mini (56.4) has †. The paper does not explain the test.
- Fig. 4 provenance: the caption says Django and Sphinx. The k = 0 / k = 5 values (62.3 → 69.7, +7.4) coincide with the GPT-5-mini Django bars of Fig. 5 (+7.4 label), so the plotted data may be Django alone; this is our observation, not a statement of the paper.
- Fig. 5 caption: "Baseline and our method"; the figure and text show three methods (Baseline, SWE-Exp, SkillForge).
- Entity alignment (p4): "files surfaced in the agent's submission diff, the golden patch, and the test patch are additionally incorporated"; the paper does not say whether this golden patch is the synthetic instance's reference patch. We mention it as an unanswered leakage question; we do not claim leakage.
- Our earlier wording "built once per repository state" was our paraphrase and was removed: for Verified the paper redoes synthesis for each target instance on a rolled-back snapshot (p6) and filters skills by source-commit date; the paper describes no iteration of the pipeline. The AST-index alignment of trajectories to repository entities (p4, E_cand ⊆ R) is now described in the blogs and poster.
- "Gain is real" was dropped from the blog title: the paper gives no SD, no named test, no significance test against the strongest baseline and no matched-compute row; the claim is limited to the gain over the plain agent.
- Cross-model transfer is one benchmark (Verified), two models and one cross pair per resolver, run counts not stated; the paper's wording is "limited guidance ... may even introduce irrelevant context".
