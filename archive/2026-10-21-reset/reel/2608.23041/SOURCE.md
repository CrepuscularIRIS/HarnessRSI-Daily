# SOURCE — AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

Read from: arXiv 2608.23041v1
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed). We did not reuse any: the method diagram, charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Table 2 and Table 3 (headline and GAIA2 ablations, p7); §5.2 (p8); Table 6 (splits, p20); Table 7 and Table 8 (optimization-run robustness, p21); Table 9 (Haiku 4.5 transfer, p22); Table 10 (fine-grained ablations, p22); Table 12 (capability vs steering patches, p23); Table 13 (optimizer cost, p24); Figure 1 caption and §5.2 / Appendix I (rollout efficiency, pp2, 8, 25); Appendix B (budgets, p20); Limitations (p44).

## ‡ numbers
Two kinds of ‡ marks (the checker's text source, the arXiv HTML, drops the decimal point of subscripted standard deviations such as "54.8 ± 48", and the Figure 6 node labels are not in it at all):
- **Read from the PDF, not computed:** the standard deviations 0.0, 1.8, 2.4, 3.8, 3.9, 4.0, 4.8, 7.6 (Tables 2, 3), and 47.7 (seed-harness dev score, a node label in Figure 6, p25).
- **Computed by us from paper numbers:** +17.4 = 58.0 − 40.6 (SWE-Bench Pro Ansible, AutoSaddler vs SWE-agent); +5.5 = 36.5 − 31.0 (Flipt); +2.4 = 43.5 − 41.1 (Element-web) — all Table 3; 4.2 = 35.6 − 31.4 (Haiku 4.5, AutoSaddler vs GEPA, Table 9).

## Notes
- Internal inconsistency in the paper: §5.2 (p8) prints +8.4 pp (SWE-Bench Pro vs SWE-agent, but its own "37.3% → 46.9%" is 9.6), +6.2 pp (SWE-Bench Pro vs strongest baseline; Table 3 gives 4.4) and +4.4 pp (Terminal-Bench 2.0 vs strongest baseline; Table 3 gives 6.7). So three of its six deltas differ from the tables. The abstract gives 9.0 / 9.6 / 10.0 (over base); the introduction (p2) and conclusion (p10) add 7.4 / 4.4 / 6.7 (over the strongest baseline). We follow the tables.
- Terminal-Bench 2.0 uses a uniform random 30 / 19 / 40 train/dev/test split (Appendix B, Table 6, p20); only GAIA2 (universes) and SWE-Bench Pro (repositories) have task-group splits.
- Figure 1a vs its caption: the caption says GEPA and Meta-Harness both consumed ~2,800 task executions; in the plot GEPA's curve ends near 1,600 and AutoSaddler's near 1,550, and only Meta-Harness reaches ~2,800 (values read from the figure, p2). AutoSaddler and GEPA both run 2 epochs on GAIA2 (Appendix B); Meta-Harness is set to use at least as many task executions and is given the union of train and dev sets (footnote 4, p8; Appendix I).
- Dev-set accuracies (72.3, 64.6, 61.5, 67.7, 73.7, 52.6) are on the set used to select the harness and are labelled so. We do not compute a dev-gain minus test-gain number; the blogs and poster set the paper's own dev and test numbers side by side.
- Tables 11/12 (fix and regression rates) are measured on the training mini-batch (Appendix G, p22–23): in-sample.
- Reruns (Tables 7, 8) exist only for GAIA2 Universe 22; none for SWE-Bench Pro or Terminal-Bench 2.0.
- The paper says code "will be available" at https://aka.ms/AutoSaddler-website; the GitHub repository link used for the code QR comes from our candidates list, not from the paper.
- The Terminal-Bench 2.0 table lists "AutoSaddler (Iter2)" 45.0 and "AutoSaddler (Iter34)" 50.0; the text gives 50.0 as the headline without explaining the checkpoint choice.

## Judgment notes
None. The full paper is consistent with our judgment (batch b06): `budget_matched: partial` (Appendix B sets Meta-Harness's task executions to be no smaller than AutoSaddler's and uses equal epochs for GEPA; tokens and cost are not matched), `cross_task: unclear` (held-out task groups and a Haiku 4.5 agent swap, but no different benchmark), `improver_comparison: unclear`, `leakage_guard: untested`.
