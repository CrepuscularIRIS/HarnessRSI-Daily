# SOURCE — GrIPS: Gradient-free, Edit-based Instruction Search for Prompting Large Language Models

Read from: arXiv 2203.07281v2
Paper figures shown: none

Authors (from the PDF title block): Archiki Prasad, Peter Hase, Xiang Zhou, Mohit Bansal, UNC Chapel Hill.
License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from (PDF page numbers)
- Method, score function, edit operations: pp3-4; Algorithms 1-3 and extensions: App. C, pp15-16.
- Setup, test-set sizes (300 per task in Table 1, 100 per task elsewhere), seeds, cost, hyperparameters: p5; App. A, pp13-14 (test sets "sampled such that the sets are as balanced as possible", p13).
- Table 1 (headline, p5); Table 2 (edit-operation ablation, p5); Table 3 and Table 4 (baselines, p6); Tables 5-6 (p7); Figure 3 (score-set size, p8); Table 8 (task details, p14); Table 10 (tasks improved and manual-rewriting variants, p17); App. E (manual rewriting and example search, pp17-18); App. G (searched instructions, pp19-20); Limitations (p9).

## Figure-derived statements (read off Figure 4, p14; approximate, no numbers printed on the poster or in the blogs except the integers below)
- Concentration of gains: GPT-2 XL's +9.36 comes mostly from tasks 022, 195 and 021; about half of babbage's +4.29 comes from task 021; curie is slightly lower after search on 021 and 022. Our rough reading of bar heights (GPT-2 XL changes of about +42, +20, +13 on 022, 195, 021 and about 0 elsewhere) sums to about 75 points over 8 tasks, i.e. about 9.4 on average, which reconciles with Table 1. These readings are approximate and are not quoted.
- Majority-label bars for tasks 021 and 022 are about 79% and 90% of the test set (read off Figure 4). The source datasets are more than 90% skewed (Table 8), but the test sets were sampled as balanced as possible (App. A p13), so the Table 8 skew is not the test-set skew.

## ‡ numbers (computed by us, or read off a figure)
- 2.42‡ = 57.79 (|S| = 100, Figure 3 / Table 3) − 55.37 (no search), babbage. The paper's text (p8) says "4.27 point gain when |S| = 100". We could not reproduce 4.27 from any table or figure; we leave this unresolved.
- 56.37‡ and 56.92‡ = values read off Figure 3 (p8; babbage accuracy with score sets of 20 and 50 examples). They appear only as figure labels, not in the text; we checked them against the rendered page. The text's "1.0 point gain when |S| = 20" is consistent with 56.37 − 55.37. The 100-example value 57.79 is also in Table 3.
- 0.39‡ = 53.68 (greedy GrIPS) − 53.29 (prefix-tuning with MLP reparametrization), Table 4.
- 3.21‡ = 56.50 (GrIPS beam search, B = 5) − 53.29, Table 4. The paper's "up to 2.56 and 5.38" compares with the no-MLP prefix variant (51.12): 53.68 − 51.12 and 56.50 − 51.12.

## Notes
- Manual rewriting has two variants (Table 10, p17): plain rewriting 47.70 / 55.50 / 57.87 and rewriting plus an added label-space line ("+ Labels") 48.12 / 55.37 / 55.37 (GPT-2 XL / babbage / curie). The paper's text on p6 gives GrIPS margins of 5.56, 2.29 and 1.50 over manual rewriting; these equal 53.68 − 48.12, 57.79 − 55.50 and 59.37 − 57.87, i.e. the better variant per model. (An earlier draft of our materials called 5.56 a text/table mismatch; that was our misreading of Table 10 and has been removed.)
- Inconsistencies inside the paper, reported neutrally (we use the table values): (1) abstract "up to 4.30 percentage points" vs text/Table 1 4.29 (60.09 − 55.80); (2) text 4.27 vs 2.42‡ above.
- Table 1 uses 300 test examples per task; Tables 2-6, Figure 3 and Table 10 use 100-example test subsets, so "No search" differs between Table 1 (49.54 / 55.80 / 63.71) and Table 3 (48.38 / 55.37 / 57.25). The majority-label figure (59.83) is given only for Table 1. We do not compare it with Table 3 numbers.
- Confidence intervals appear only in Table 1 (and Figure 4); the paper does not describe how they are computed. Footnote 9 describes two-sided bootstrap tests over examples and seeds (100k resamples). Tables 2-6 give single averages with no variance, so ablation gaps (1.01-2.56) and the Table 3 margins (1.50-2.29) cannot be compared with noise; the Table 1 CI widths (1.6-3.7) are for a different test-set size.
- Example search (Table 3): the paper states the number of iterations is set so that it uses the same maximum number of model queries as GrIPS (p6). It uses Examples-Only prompts, GrIPS uses Instruction-Only prompts. Footnote 10 says example search costs more dollars (longer prompts). App. E.2 says there is "a lot of variability across tasks, more so in the case of InstructGPT curie" (Figure 6 has no error bars); we do not quote per-task numbers.
- Gradient-based methods (Table 4): an 80:20 train/dev split of the score set; footnote 11: "These methods only use test input and not instructions". The paper reports no tuning budget or compute for them; we therefore say "not reported" rather than "not matched". Beam search uses about B times more evaluations (p4).
- Manual rewriting (App. E.1, p17): done by the first three authors, about 5 hours, following the guidelines of Mishra et al. The paper describes no use of a score set for it (it neither says nor denies it; it mentions matching capitalisation with "the input-output example pair"). The rewriters were the method's authors.
- Stopping rule: the text says search stops when the score does not improve for P iterations; the Algorithm 1 pseudocode (App. C) returns only after P + 1 non-improving iterations (P = 2 gives 3). We did not check the released code.
- Hyperparameters (l, m, n, P) were chosen by line search using GPT-2 L and XL "on select tasks during preliminary experiments" (App. A, p13); the tasks are not named and the paper does not state which examples. GPT-2 XL is also a reported model.
- Task choice (App. A): 8 tasks chosen for cost, and for diversity, balance and stability of the dataset versions.
- Table 10 (p17): number of tasks of 8 with positive change under GrIPS Instruction-Only: GPT-2 XL 4, babbage 7, curie 5; plain manual rewriting 1 / 4 / 3 on GPT-2 XL / babbage / curie. App. G (pp19-20): GPT-2 XL search returned the original instruction for tasks 069, 137, 139.
- FLAN-T5 caveat (Table 6, p8) is the authors' own: instruction-tuned on NATURAL-INSTRUCTIONS, "possibly exposing the model to the test instances". No other leakage or contamination check was found in the text or appendix.
- Searched for, not found: transfer of a searched instruction to other tasks or models; confidence intervals in Tables 2-6; runs of other discrete prompt-search methods (AutoPrompt is argued about on p7, not run).
- Poster chart (headline): values and CIs are Table 1; the majority-label line is 59.83.

## Judgment notes
Our judgment (batch b19; score 67, retained) is consistent with the full paper on what we could check: `held_out: yes` (score set separate from test set), `variance: yes` (95% CIs in Table 1; none in later tables), `cross_task: no`, `leakage_guard: untested`. Two refinements for readers, no judgment file edited: (1) `budget_matched: yes` rests on the example-search baseline being capped at GrIPS's maximum model queries (p6); for the gradient-based and beam-search comparisons and for manual rewriting the paper reports no compute-matching. (2) `retained_ablation` and `improver_comparison` are `unclear` in the judgment, while the paper does report an ablation of edit operations and the score function (Table 2, App. C) and comparisons with manual rewriting, example search and gradient methods (Tables 3-4); those are ablations of the search design and baseline comparisons rather than a comparison of retention rules, so "unclear" may undercount what the paper reports.
