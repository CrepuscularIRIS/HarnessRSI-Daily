# SOURCE — Imitation Holds a Key to Evolution: Localized Repair and Verified Skill Acquisition for Adaptive Agents

Read from: arXiv 2610.16125v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers. Authors as in the PDF title block: Kai Hu (Beijing International Studies University), Hua Huang (Chongqing University of Posts and Telecommunications).

## Where the numbers come from
- Table 1 (p8): all cold / learned-composition / unseen-C numbers, SDs across worlds.
- Sec. 3-4 (pp3-4) and Alg. 1 (p5): mechanism, 0.7 threshold, two-task confirmation, K and two full submissions.
- Sec. 6.1-6.3 (pp5-6): environment, ten seeds, 60 tasks per group per world, disjoint ids, integrity suite (3,600 tasks, 64,800 comparisons).
- Sec. 7.1 (p7): 61.82% work reduction (75.90 vs 28.98), no-small-trial work 58.82. Sec. 7.1/7.3: K = 1 (21.5 vs 24.0), K = 6 (2.46 vs 2.67 trials). Sec. 7.4 (pp7-8): exploratory C adaptation curve. Sec. 8 (pp8-9): limitations. Appendix A (p11): 94,595 episodes, run time.

## ‡ numbers (computed by us)
None. Every number in the blogs and poster is quoted from the paper's text or Table 1.

## Notes
- "Collateral" in Table 1 is final collateral regression: a contract that passed initially fails at the final audit (Sec. 6.3).
- The 600-task figure (abstract) is ten worlds x 60 cold held-out composition tasks per world (Sec. 6.2).
- The "no retention" condition is the code's `pi_no_incentive`; the paper states it is not a clean reward-formula ablation (Sec. 6.2).
- Table 1 SDs exist only for the Unseen C column; the cold columns carry no SD in the paper.

- Compositional-repair control: Sec. 6.2 says it removes the score threshold and source-fragment evidence ranking; Sec. 7.1 says the comparison prevents attributing the composition result *uniquely* to the incentive score. The appendix code (p. 11 ff., not run by us) still uses an incentive score to rank eligible actions and known evidence in other paths, so we say it "shares some helper ordering". Trials, work and collateral for this control appear only in Table 1 (cold K = 3); Unseen C, the K sweep and Figure 2 give success only (Figure 2 draws its line overlapping PI).
- Sec. 4.3: every small trial updates success/failure counts and incentive for the tried action during acquisition; only proactive initialization needs |U| >= 2 distinct accepted tasks and q >= 0.7. Sec. 5.2 (Proposition 2) is conditional on its premises ("not a universal equivalence").
- Gaps on Unseen C (PI 70.00 vs 79.00 / 76.00; K = 1: 21.5 vs 24.0) are smaller than the across-world SDs; the paper runs no test, and the K = 1 values carry no SD.
- 75.90 -> 28.98 work (Sec. 7.2) compares PI without vs with retention on held-out compositions at K = 3; 58.82 vs 75.90 (Sec. 7.1) is no-small-trial vs PI, cold.
- Sec. 7.4 / 6.2: the 24-task C stream has each of the 12 multi-goal combinations twice; the final unseen-C tasks are also compositions, so request types appear to overlap (our reading). Figure 2 caption: retention within a learned revision, not unseen-revision transfer.
- Sec. 6.3: the 600 tasks are not 600 independent environments; SDs are across ten worlds, not task-level CIs. Sec. 8.2: the evidence table keeps task identifiers and can grow. Appendix A: ~21.93 s and 3.49 s are unprofiled whole-run times, disclaimed as not comparative.

## Judgment notes
Our judgment (research/judgments/2026-10-19-a.jsonl): `variance: unclear`, `cross_task: unclear`, `budget_matched: partial`, `improver_comparison: unclear`, `leakage_guard: tested`, `retained_ablation: yes`, `held_out: yes`. The full paper is mostly consistent with this. One nuance, with no edit to the judgment file: the paper does report ten worlds and across-world SDs for the Unseen C column of Table 1 (not for other columns), which a reader may count as partial variance evidence; and the unseen-revision-C tests (negative transfer, exploratory adaptation) are within the same synthetic domain and generator, so `cross_task` stays unclear. The score of 68 and level `retained` are consistent with the paper's own statement that its comparison against the strongest control (compositional repair) is a tie.
