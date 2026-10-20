# SOURCE — M⋆: Every Task Deserves Its Own Memory Harness

Read from: arXiv 2604.11811v2
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Table 1 (headline, p5), Table 2 (ablation, p7), Table 3 and Table 13 (seeds, pp8, 29), Table 4 / Table 12 (categories, pp9, 29), Table 5 (split sizes, p14), Table 6 (cost, p17), Table 7 (hyperparameters, p17), Figure 5 (transfer; values read from the bar labels, p8), Appendix J (limitations, pp29–30).

## ‡ numbers (computed by us)
- 0.048‡ = 0.421 (five-seed LoCoMo mean, Table 3) − 0.373 (Mem0, Table 1).
- 0.086‡ = 0.459 (Table 1) − 0.373 (Mem0, Table 1).
- 0.120‡ = 0.820 (GEPA + Vector Search) − 0.700 (M⋆), ALFWorld Seen, Table 1.

- 0.41‡ ≈ (18×0.33 + 18×0.19 + 9×0.35 + 55×0.51) / 100 = 0.406, the n-weighted mean of M⋆'s per-category LoCoMo F1 (Table 4b, n = 18/18/9/55); it differs from Table 1's 0.459 and the paper does not explain the difference. Baselines reconcile to within 0.003.

## Notes
- ALFWorld Unseen: Table 5 lists 50 test episodes; the category counts in Appendix Table 10 sum to 42 (8+1+11+1+7+6+8), and 0.881 = 37/42, 0.857 = 36/42 — we say the margin is one episode if n = 42.
- The Table 1 values for LoCoMo F1, HealthBench Data and PRBench Finance (0.459, 0.390, 0.586) equal the seed-0 column of Table 13 (p29). We state this as an observation; the paper does not say which seed Table 1 reports.
- Baseline cost range "$0.31–$1.51" is the min/max over the No Memory and Vector Search rows of Table 6 only; costs of the other baselines (including GEPA) are not listed in the paper.
- Figure 5 values (0.26, 0.46, 0.02, 0.09; 0.64, 0.62, 0.88, 0.58; 0.47, 0.06, 0.58, 0.66) are read from the figure's bar labels.

## Judgment notes
None. The full paper is consistent with our judgment (batch b18): `budget_matched: unclear` (no matched-compute row found), `leakage_guard: untested`, `variance: yes` (five seeds on three of seven configurations).
