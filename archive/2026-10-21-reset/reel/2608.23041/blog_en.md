# AutoSaddler: patching an agent's harness from its failure traces — a 9–10 point test gain, with baselines that did not get its safeguards

*A Reel interpretation of [arXiv 2608.23041v1](https://arxiv.org/abs/2608.23041v1) (HarnessRSI Daily score 79, ★★★). Code: [microsoft/AutoSaddler](https://github.com/microsoft/AutoSaddler) (the paper itself only says the code "will be available" at aka.ms/AutoSaddler-website; the repository link comes from our candidate list).*

## What the system changes about itself

AutoSaddler optimizes the **harness** around an LLM agent, treated as code: the prompt, the tool set and its interfaces, and the middleware (hooks and agent-loop logic). The model weights are untouched. The signal is the execution traces of failed (and passing) runs on a small mini-batch of training tasks, and what is kept is a patched harness.

## The loop, and the keep/reject rule

1. Run the current harness on a mini-batch of training tasks (on GAIA2, six scenarios per iteration).
2. A coding agent (Claude Agent SDK) reads the traces progressively together with the harness source — evaluation and benchmark code are hidden from it — names a root cause and writes a **typed patch**: Prompt, Tool or Middleware. Patches are either *Capability* (executable code) or *Steering* (text only); the schedule starts with capability patches and then moves to steering ones.
3. Re-run the patched harness on the **same mini-batch**. Only if it improves is it evaluated on a development set.
4. A reflection agent sorts cases into fixed, regressed, still-failing and still-passing and stores lessons in **EvoDAG**, a graph of all explored harnesses. An evolution agent then composes the next harness from any earlier node, so it can cherry-pick good patches or roll back bad ones.
5. After the budget is used, the harness with the best development score is run once on a held-out test set, three times for the mean ± standard deviation.

For GAIA2 the training, development and test sets are different simulated user "Universes", and for SWE-Bench Pro they are different repositories. **Terminal-Bench 2.0 is the exception:** it has only 89 tasks and uses a uniform random split (30 train / 19 dev / 40 test), so its test set carries no distribution shift. All optimizers and the task agent use Claude Opus 4.6.

## Headline result, as reported

Pass@1 on the test sets (mean ± std over three test runs; one optimization run per method):

| Benchmark | Base harness | Strongest automated baseline | AutoSaddler |
|---|---|---|---|
| GAIA2 (average) | 53.0 ± 1.5‡ | 54.6 ± 2.5‡ (GEPA) | 62.0 ± 1.2‡ |
| SWE-Bench Pro (average) | 37.3 ± 4.8‡ | 42.5 ± 1.2‡ (GEPA) | 46.9 ± 1.8‡ |
| Terminal-Bench 2.0 (40 tasks, random split) | 40.0 ± 0.0‡ | 43.3 ± 5.8 (Meta-Harness) | 50.0 ± 0.0‡ |

The abstract gives gains over the base harness of 9.0, 9.6 and 10.0 points; the introduction and the conclusion add gains over the strongest automated baseline of 7.4, 4.4 and 6.7 points. These match the tables. Section 5.2 of the text prints different values for three of its six deltas: +8.4 for SWE-Bench Pro over SWE-agent (its own "37.3% → 46.9%" gives 9.6), +6.2 for SWE-Bench Pro over the strongest baseline (the table gives 4.4), and +4.4 for Terminal-Bench 2.0 over the strongest baseline (the table gives 6.7). We use the table values.

Development-set scores are far higher than test scores: on GAIA2 the dev score goes from about 47.7‡ (seed harness, Figure 6) to 72.3, against test 53.0 → 62.0; on Terminal-Bench from 52.6 to 73.7 (Figure 5), against test 40.0 → 50.0. The dev set is the set used to select the harness, so the paper's efficiency curves are selection-set numbers.

## The controls that decide whether the gain is real

- **Ablations on GAIA2 (Table 2).** Full system 62.0. Replacing in-depth diagnosis with a single-call reflection gives 57.8; removing the patch taxonomy and phase schedule gives 56.9; removing both reflection and the development-set check gives 50.6, below the 53.0 of the default agent. Each variant was re-optimized once, with test standard deviations of 3.8‡–7.6‡ in the per-universe cells. These gaps should be read against the optimization-run variance below: a second AutoSaddler run alone moves by 2.1 points, and on Universe 22 "w/o in-depth diagnosis" (57.1) sits within that spread of the second run's 58.6, while 50.6 versus 53.0 is within the 4.0‡ standard deviation.
- **Optimization-run variance (Table 7, GAIA2 Universe 22 only).** AutoSaddler's second run gives 58.6 against 60.7 for the first; GEPA's runs give 47.9 and 50.6, Meta-Harness's 51.5 and 51.2. SWE-Bench Pro and Terminal-Bench 2.0 had no rerun. The authors call two runs insufficient for a full statistical characterization. Training on a different universe gives 57.4 (default agent 51.5).
- **The same safeguards were not given to the baselines.** The mini-batch gate, development-set filter and reflection are the mechanism whose removal costs 62.0 → 50.6 in Table 2. GEPA and Meta-Harness do not have them (Meta-Harness has no patch-acceptance gate, Table 13), and no baseline-with-gate run is reported.
- **Budget, and how the baselines were configured.** AutoSaddler and GEPA both run 2 epochs on GAIA2 and SWE-Bench Pro, so their budgets are about matched; Meta-Harness was set to use at least as many task executions as AutoSaddler. In Figure 1a AutoSaddler reaches 72.3% dev accuracy at about 1,000 executions (its curve ends near 1,550), GEPA saturates at 64.6% early on (its curve ends near 1,600), and only Meta-Harness runs to about 2,800 executions, ending at 61.5%. The Figure 1 caption says GEPA and Meta-Harness both consumed about 2,800, which the plot does not show. Meta-Harness was also given the union of the training and development sets, so its 61.5% dev score is on data it trained on.
- **Optimizer cost (Table 13).** Per generated patch: AutoSaddler $14.56 (533 s), Meta-Harness $12.65 (883 s), GEPA $5.50 (prompt-only).
- **Patch durability (Table 12) is an in-sample statistic.** Capability patches regress 8% of previously passing cases against 17% for steering patches, but this is measured on the training mini-batch, not on held-out tasks.
- **Different task agent (Table 9).** Harnesses optimized with Opus 4.6 and run on Haiku 4.5 score 35.6 against 30.0 for the default agent, 31.4 for GEPA and 30.2 for Meta-Harness; the margin over the best baseline is 4.2‡ points.

## Where the gain is absent or small

- **SWE-Bench Pro is carried by one repository.** Ansible: AutoSaddler 58.0 vs base 40.6 (+17.4‡). Flipt: 36.5 vs 31.0 (+5.5‡), where GEPA (32.2) and Meta-Harness (31.3) are about at the base. Element-web: 43.5 vs 41.1 (+2.4‡), below GEPA's 45.2.
- **GAIA2 Universe 21:** 61.4 ± 2.4‡ against GEPA's 60.1 ± 3.9‡, overlapping.
- **Baselines that did not help here:** Meta-Harness scores 53.2 against 53.0 for the default agent on GAIA2 and 35.3 against 37.3 on SWE-Bench Pro. The baselines were adapted by the authors to these benchmarks.
- **Terminal-Bench 2.0** has only 40 test tasks and the AutoSaddler rows have a standard deviation of 0.0‡; the manual Terminus KIRA harness scores 47.5. The table lists two AutoSaddler checkpoints (Iter2: 45.0, Iter34: 50.0); the text does not say why the second is the headline.
- **Limits stated by the authors:** it needs gold answers or a pass/fail signal, handles only stateless tasks, and was run on a Claude family; they advise human review before deployment.

## Our read

HarnessRSI score **79**, band ★★★, evidence level **retained**: the retained harness helps on held-out data and the retained-artifact ablations are reported. The paper reports held-out evaluation (distribution-shifted for GAIA2 and SWE-Bench Pro, random for Terminal-Bench), repeated test runs, optimizer cost, ablations and a rollout-efficiency comparison. It reports one optimization run per method in the main tables, only partial budget matching, no leakage test, no baseline given AutoSaddler's gate, and no experiment that varies the improver itself in the sense of our evidence ladder; cross-benchmark transfer is not tested beyond the task-agent swap.

*Numbers marked ‡ were computed by us from paper numbers or are standard deviations read from the PDF tables; see SOURCE.md.*
