# REFLEX: a vision critic diagnoses, a code writer repairs, and credited snippets are kept — fewer LLM calls on small tasks, with thinner controls on the memory

*A Reel interpretation of [arXiv 2606.16496v2](https://arxiv.org/abs/2606.16496v2) (HarnessRSI Daily score 71, ★★★). The paper gives no code link.*

## What the system changes about itself

REFLEX evolves a **program** (a control policy in Python, or an antenna-design function) with LLMs; model weights never change. Each program is run and gives two signals: a scalar fitness and a rendered **Behavioral Evidence** image (a trajectory, a phase portrait, an action timeline; for antennas the array layout and radiation cuts). It then adds a **Skill Memory** that survives across campaigns.

## The loop, and the keep/reject rule

1. A **vision Critic** reads the parent's image and fitness and writes a structured JSON diagnosis (failure mode, root cause, suggested fix). It never writes code.
2. The diagnosis is the query for **BM25** retrieval of the top 3 code snippets from the Skill Memory.
3. A **text-only Actor** (it never sees the image) writes the child from the parent code, the diagnosis and the snippets.
4. The child is evaluated. Every valid, non-duplicate child enters the population and the 16 best are kept (elitist selection).
5. **Credit rule.** Each retrieved snippet that the Actor reports using gets utility `+min(Δ, 1)` if the child beat its parent, else `−0.5·min(|Δ|, 1)` (an invalid child counts as Δ = −1). A snippet is archived when its utility falls below −1 after at least 3 retrievals; near-duplicates are merged; capacity is 256 skills. New snippets are extracted only when a child improves on its parent.
6. A **UCB1 bandit** picks among five operators (diagnostic mutation, text mutation, three-parent crossover, from-scratch, cross-domain inspiration), with a forced burst after 12 children without a new best.

Every Critic, Actor, repair, abstraction, merge and failed call counts against the budget.

## Headline result, as reported

Same weights (Qwen3-VL-235B-A22B-Instruct) for every LLM role in REFLEX, the official MLES baseline and a compute-matched Actor-only ablation (Critic removed, saved calls spent on more Actor proposals); population 16; 10 paired seeds; 100 total LLM calls.

| Median LLM calls to reach the solve threshold (Table 1) | Official MLES | Actor-only | REFLEX |
|---|---|---|---|
| Acrobot | 41 | 28 | 13 |
| Pendulum | 53 | 46 | 20 |
| Lunar Lander | 49 | 43 | 24 |

Seeds solved: 10/10 for REFLEX on all three tasks; MLES 9/10, 8/10, 9/10; Actor-only 10/10, 9/10, 9/10 (Acrobot, Pendulum, Lunar Lander). The 50-call and 100-call budgets are separate runs with different seeds.

On a 36-dimensional antenna-array task (240 objective evaluations, 10 paired seeds, shared-prior initialization), REFLEX reaches the harder 25.25 score on 9/10 seeds against 3/10 (PSO), 2/10 (GA), 1/10 (CMA-ES) and 0/10 (Random Search); with random-vector initialization it is 7/10 against 0/10 for all four.

## The controls that decide whether the gain is real

- **Compute-matched Actor-only (Table 1).** The comparison is at equal total LLM calls. REFLEX spends about 40% of its calls on the Critic and so evaluates fewer programs (27 against 48 for Actor-only and 42 for MLES in a 50-call Lunar Lander campaign). Actor-only keeps the Skill Memory rules, but its placeholder diagnosis lists only the parent's scalar metrics and also serves as the BM25 query (p6), so removing the Critic also changes what is retrieved: the gap is the Critic plus diagnosis-driven retrieval, not the image alone. Official MLES is run with its native prompts and operators; the paper describes no Skill Memory for it.
- **Statistics (p6).** Paired AUC gains over both baselines are significant on Lunar Lander and Pendulum at both budgets (Holm-corrected p ≤ 0.032); for example on Pendulum at 50 calls +0.125 [0.045, 0.205] over Actor-only. Acrobot has no paired tests.
- **Is the image what matters? (Table 3a, Acrobot only).** Giving the Critic a shuffled or a blank image instead of the right one: AUC −0.4270 and −0.3620 against −0.2850 with the correct image and −0.3450 for Actor-only; calls to target 14.70 and 9.50 against 5.50 and 10.30. Paired AUC gain +0.142 over shuffled, +0.077 over blank, +0.060 over Actor-only (p = 0.004, 0.012, 0.012). This is the only control that speaks to the image itself. It is a single task with means ± SEM and no significance test for calls to target. Its budget is described only as "an identical call budget for all conditions", with no seed count beyond 10 paired seeds, and its numbers do not reconcile with Table 1 (REFLEX 5.50 mean calls with 10/10 solved, against a median of 13 [7, 21] in Table 1; AUC −0.2850 against −0.280) or with the 20-call paragraph (6/10 each), so we do not place them side by side.
- **Skill Memory transfer (Section 4.4, Acrobot target, Qwen3.5-27B, 20 calls, 10 paired seeds).** Frozen top-2 skill banks from Pendulum or Lunar Lander campaigns versus an empty bank. The final score rises on 10/10 paired seeds for each bank (Wilcoxon p = 0.002), from a cold mean of −0.139 to −0.105 (Pendulum) and −0.118 (Lunar Lander). The banks were hash-verified and audited to exclude Acrobot-specific identifiers. Note that the Acrobot target is −0.20, so even the cold mean final (−0.139) is above it and the cold median calls to target is 4.0: the gains are small refinements on a nearly saturated task.
- **Cost.** A 100-call control run takes about 10–15 minutes, dominated by inference latency (Appendix D). The paper reports no dollar cost, and no cost for the antenna runs.

## Where the gain is absent or small

- **Lunar Lander final score at 100 calls** is similar for all three methods (REFLEX 1.082 ± 0.009, Actor-only 1.064 ± 0.012, MLES 1.069 ± 0.011); the gain there is in calls to solve and AUC, not final score. On Acrobot the final-score difference over Actor-only in the ablation is +0.0021 [−0.0005, 0.0046], p = 0.18.
- **Tight budget.** With a 20-call cap on Acrobot, REFLEX and Actor-only each solve 6/10 seeds and differ by nothing significant; the authors write that the Critic calls "pay off once the budget allows several diagnosis-conditioned mutations", and the Limitations say that at 20 calls "the Critic brings no measurable benefit over Actor-only". The transfer study itself runs at this 20-call cap.
- **Transfer is partly weak.** AUC@20 is significantly better only for the Pendulum bank (p = 0.049; Lunar Lander p = 0.065), and calls-to-target improve consistently only for the Pendulum bank (p = 0.039; Lunar Lander p = 0.91, two seeds needing 16–17 calls). Skills were used in 58 evaluated Acrobot children from Pendulum (13 improvements, 45 regressions) and 14 from Lunar Lander (5 improvements, 9 regressions): the Actor rewrites the snippets and selection keeps the few that work. Only two source–target pairs and one model were tested.
- **Executable memory is not shown better than textual memory.** Textual strategies against executable fragments: final −0.0010, p = 0.82; AUC +0.017, p = 0.70; no pairwise difference is significant. Executable fragments produced no invalid children (0/163, against 1/166 for textual strategies and 3/160 for no memory), but textual strategies solve 10/10 seeds against 9/10 for both others. In Table 3b executable fragments barely exceed no memory on AUC@20 (−0.5445 against −0.5618) and sit below textual strategies (−0.4742; mean gap 0.070‡, while the +0.017 is a median of paired differences), whereas Section 4.4 reports a lift from −0.523 to −0.310 with frozen banks. The paper does not say which source bank, model or seeds Table 3b uses and does not reconcile the two results.
- **Antenna task.** At the 25.0 threshold with the shared prior, GA and PSO also reach 10/10 seeds; REFLEX's lead is in evaluations to 25.0 (median 19 against 48–148) and at the 25.25 threshold. Best@240 is 25.33 ± 0.02 against 25.21 ± 0.02 for PSO. The paper does not give tuning settings for CMA-ES, GA, PSO or Random Search, or how the thresholds were chosen, and reports no significance test for the antenna comparison. All methods get the same first LLM/analytical designs (the shared prior), so the classical optimizers are seeded from designs that are partly LLM-produced; "equal budget" means equal objective evaluations (REFLEX's inner local-search evaluations included), not equal LLM cost, and REFLEX's LLM call count on the antenna task is not stated.
- **Not run (authors' limitations and our reading).** No sensitivity study of population size, UCB1 constant or memory capacity; no human study of whether diagnoses are correct; the control tasks are low-dimensional. The paper reports no numeric ablation that removes the Skill Memory or the utility credit rule inside the main campaigns (Figure 6 shows such variants only as a qualitative profile).

## Our read

HarnessRSI score **71**, band ★★★, evidence level **retained**: the retained artifact (frozen skill banks) helps on a task other than the one that produced it, under a hash-verified, identifier-audited protocol. The paper reports matched call budgets, paired seeds with confidence intervals, an image-shuffle control (one task), wall-clock time and cross-task transfer. It does not report a comparison of the improvement mechanism (credit rule, bandit) against alternatives, a Skill Memory ablation inside the main comparisons, or a code release. The gains are in sample efficiency on three low-dimensional control tasks and one antenna design problem; transfer rests on one target task.

## Reading cautions

- "±" in Tables 1 and 2 is the standard error of the mean. Table 1 does not say whether seeds that never reach the target are excluded from the median calls to solve (Table 2 says its medians are over seeds that reach it).
- "Paired" means the same seed index across methods, with stochastic LLM sampling. Table 5 lists seeds 0–9 for all formal comparisons, while Section 4.1 says the 50- and 100-call budgets used different seeds.
- The 20-call Acrobot interval (final +0.015, CI [−0.123, 0.453]) is asymmetric around its estimate; the paper does not comment.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
