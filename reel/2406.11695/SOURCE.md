# SOURCE — Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs

Read from: arXiv 2406.11695v2
Paper figures shown: none

Exact PDF downloaded directly from https://arxiv.org/pdf/2406.11695v2 into `/home/lingxufeng/reel-work/2406.11695/paper.pdf`. Title, author order and equal-contribution marks verified against its title block. PDF version stamp: 6 Oct 2024. All page references below are one-based PDF pages. Read the complete 28-page PDF including appendices, using layout and plain extractions; rendered the principal results and setup tables for visual verification.

Figure reuse is forbidden for this assignment. The poster contains an original method diagram and original bars drawn from Table 2 values, not crops, traces or reproductions of paper figures. No code URL was supplied, so the poster has only a paper QR. The paper states a DSPy release at dspy.ai; we did not inspect or run any linked code.

## Claim and number provenance

| Content | Exact source |
|---|---|
| Title, authors, contribution marks, version | p1 title block and version stamp |
| Search instructions and demonstrations, fixed weights/control flow, downstream supervision only | pp2–3, §2–3 |
| Threshold-filtered trace bootstrapping | pp3,4–5, §3.1 and §4.1 |
| Grounded proposal, multivariate TPE and minibatch scores | pp3–6, §3.1–3.2, §4.3 |
| Periodic full scoring and final keep rule | p6, §4.3: highest-scoring fully evaluated configuration; explicitly full train-set |
| MIPRO++ proposal settings; unresolved temperature/model scope | p6 §4.4 and p8 §5.2 describe proposer temperature; p14 Appendix B.4 says Llama temperature, despite GPT-3.5/GPT-4 proposers |
| HoVer restricted to three supporting facts, with mixed hop counts | p13 Appendix A: approximately 67% of training and 83% of test queries truly three-hop; remainder two-hop; authors recommend genuine three-hop filtering |
| Metrics and module/task setup | p7 Table 1; p13 Appendix A |
| Task model, teacher model and GPT-4 answer-type annotations | p8 §5.2; p13 Appendix A |
| GPT-3.5 general proposer; GPT-4 on ScoNe, HoVer and Iris | p14 Appendix B.4 (more specific than p8's general GPT-3.5 default) |
| All seven rows of MIPRO and strongest competitors; component comparisons; grounding and ++ values | p9 Table 2, visually verified against rendered PDF page |
| Five-run means, Wilcoxon method, significance interpretation | p8 §5.2 and §6; p9 Table 2 caption and bold values |
| Same-benchmark test splits, role of dev and no-dev exceptions | p14 Table 3 caption and entries |
| 50 / 30 / 20 full-evaluation trial budgets and about 300 minibatch trials | p14 Appendix B.2; the trial budget is not a total LM-call or token bill |
| Candidate defaults and selection rationale | p14 Appendix B.3/Table 4; intuition from past experiments, not extensive sweeps |
| Fixed budget/model scope and dependence on handwritten task rules | p10 Limitations, p8 §6; p13 Appendix A and p17 Appendix E.4 |
| Demonstration-specific instruction overfitting | p21 Appendix H; illustrative one-run progressions pp22,25–28 |
| Appendix curves are individual runs, not dispersion estimates | p21 Appendix G; plots pp22–25 |

## Numerical interpretation and scope

- No numbers marked ‡ are used. No numerical values were taken from figure labels. Chart values are literal Table 2 test means; no error bars are invented.
- The abstract's rounded “as much as 13%” is compatible with Conditional MIPRO 23.3 versus Bootstrap RS 10.4. The stronger alternative in that column is instruction-only 0-Shot MIPRO 14.6. We do not present the rounded abstract claim as a gain over the strongest competitor, nor flag it as an inconsistency. No computed decimal difference is published.
- Five of seven highest test means is a numerical ranking. §6 lists HotPotQA, Iris and Heart Disease as exceptions to the significant-best claim. In the PDF, HotPotQA Bootstrap RS 45.8, Bayesian Bootstrap 46.2 and MIPRO 46.4 are all bold. We explicitly separate a numerical lead from a significant win.
- “Largest positive gaps” refers to the within-task comparisons shown, Conditional and Iris-Typo, not a pooled cross-metric average. Iris and Heart Disease reverse the ranking.
- Table 2 reports five-run means and significance tests, without run-level SDs, CIs or seed IDs. We do not call these five seeds. Appendix G/H single-run plots/examples do not determine the number of runs behind Table 2.
- HoVer scores and 500/500/1520 split sizes cover the three-supporting-fact subset, not full HoVer or a uniformly three-hop set. Appendix A (p13) reports approximately 67% of training and 83% of test examples as genuinely three-hop; the rest are two-hop because facts can share documents.
- Main §4.3 (p6) describes minibatch and final full-train scoring; Table 3 (p14) assigns dev to method development. Appendix F.1 (p19) instead scores Bootstrap candidates on dev, and F.5 (p21) describes MIPRO selection on a validation set. Section 4.1 (p5) permits training or a dedicated validation split. Both blogs and poster disclose the unresolved per-method selection-split details. These conflicting descriptions are not evidence of test-set selection or leakage.
- MIPRO++ temperature scope remains unresolved: §4.4 (p6) and §5.2 (p8) describe proposer temperature, whereas Appendix B.4 (p14) says Llama temperature is optimized and identifies GPT-3.5/GPT-4 as proposers. We do not silently reconcile these statements, establish whether task-model sampling was also tuned, or attribute the results to either interpretation.
- The paper gives no separate per-default split-selection record for the candidate counts. We report dev-based method iteration and the authors' intuition-based default choices without claiming that every hyperparameter was dev-selected.
- Equal full-evaluation trial budgets are partial matching. Prompt lengths differ; teacher bootstrapping, summaries and proposal generation are not costed separately. No verified total tokens, LM-call bill, or dollar cost is supplied. Baseline search budgets are reported; separate tuning/sweep budgets are not.
- No explicit contamination/overlap audit, detailed grouped/randomized splitting procedure, frozen-prompt cross-task transfer, or cross-task-model transfer study was found in the complete PDF. This is an absence of reported evidence, not an assertion of actual contamination. Proposers and teachers are distinct from the task metrics; GPT-4's supervised annotation role for Conditional is stated explicitly.
- Baseline information access is scoped separately: OPRO −G retains examples and instruction/score history in its meta-prompt; grounded OPRO gets additional grounding; demonstration-only methods retain fixed instructions; only the full MIPRO Table 2 row searches both deployed components jointly. The evaluated 0-Shot MIPRO++ variant searches instruction proposals, not deployed demonstration sets; the temperature/model ambiguity above prevents an unqualified proposal-only attribution.

## Judgment notes

Source records: `/home/lingxufeng/ArxivDaily/research/scores.jsonl`, latest matching judgment `/home/lingxufeng/ArxivDaily/research/judgments/b19.jsonl`. Score 64, band ★★, evidence level retained. These records were not modified.

The judgment marks `variance: yes`, based on five runs and Wilcoxon tests. The full PDF supports repeated-run statistics but does not publish SDs/CIs or seed-level dispersion for Table 2. Both blogs and poster make that narrower distinction. `budget_matched: partial` is supported by the shared full-evaluation trial budget, not all-in token/call equality. `optimizer_cost: unclear` remains appropriate. `cross_task: unclear` is not replaced with a claim of transfer: seven tasks are separately optimized. The paper does supply instruction-only, demonstration-only and joint comparisons despite `retained_ablation: unclear` in the record; those are component comparisons, not a direct retention-rule ablation. No score or evidence-level recalculation is made.
