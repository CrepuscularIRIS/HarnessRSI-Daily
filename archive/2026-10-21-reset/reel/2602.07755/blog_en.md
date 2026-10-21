# ALMA: a Meta Agent writes the agent's memory in code — the clearest gain is on ALFWorld, most other cells are within noise

*A Reel interpretation of [arXiv 2602.07755v1](https://arxiv.org/abs/2602.07755v1) (HarnessRSI Daily score 75, ★★★). Code: [zksha/alma](https://github.com/zksha/alma).*

## What the system changes about itself

ALMA (Automated meta-Learning of Memory designs for Agentic systems) treats an agent's **memory design** as a program. A memory design is Python code built on a small abstraction: sub-module layers that each have their own `update()` and `retrieve()` logic and, optionally, their own database (vector store, graph, dictionary), orchestrated by two entry points, `general_update()` and `general_retrieve()`. A **Meta Agent** (GPT-5) writes new designs; designs may contain their own LLM calls and prompts. The agent that uses the memory is fixed and its weights are never touched.

## The loop, and the keep/reject rule

1. The archive starts from one design the Meta Agent generates from the abstract classes.
2. Each learning step samples up to five designs from the archive, with probability rising with success rate and falling with how often a design has already been sampled (softmax, temperature 0.5); every design keeps a non-zero chance.
3. For each sampled design the Meta Agent reads its code, a stratified sample of its logs and its success rate, writes a plan, and implements a new design. A trial run (5 learning tasks) triggers debugging, up to three times.
4. Each new design is scored by a fixed agent (GPT-5-nano) in **static mode**: first a **Memory Collection Phase** (the agent runs tasks without memory; the design builds its memory from those trajectories), then a **Deployment Phase** (the agent retrieves from that frozen memory on new tasks), averaged over three runs.
5. The design and its logs go into the archive. There is no reject step: every evaluated design is kept as a possible stepping stone, and after 11 learning steps (43 designs) the design with the highest learning-set success rate is the output.

## Headline result, as reported

Four sequential decision-making benchmarks (ALFWorld, TextWorld, Baba Is AI, MiniHack), four human-designed baselines (Trajectory Retrieval, Reasoning Bank, Dynamic Cheatsheet, G-Memory), designs learned on a learning split and tested on a separate testing split. Table 1 is entirely in static mode. Success rate in percent, mean ± standard error over three Deployment runs.

| Test | ALMA | Best baseline |
|---|---|---|
| ALFWorld, GPT-5-nano | 12.4 ± 0.5 | 7.6 ± 0.5 (G-Memory) |
| Overall avg., GPT-5-nano | 12.3 | 8.6 (Trajectory Retrieval) |
| ALFWorld, GPT-5-mini (transferred) | 87.1 ± 1.4 | 80.0 ± 1.4 (Trajectory Retrieval) |
| TextWorld, GPT-5-mini | 75.0 ± 2.3 | 68.8 ± 4.7 (G-Memory) |
| Overall avg., GPT-5-mini | 53.9 | 48.6 (Trajectory Retrieval) |

The no-memory averages are 6.1 (GPT-5-nano) and 41.1 (GPT-5-mini), so the paper's "+6.2" and "+12.8" are percentage points over no memory. ALMA is best or tied in 7 of the 8 benchmark columns, but a margin of several combined standard errors (our arithmetic from the table's SEs, runs treated as independent) appears only for ALFWorld: about 6.8‡ with GPT-5-nano and about 3.6‡ with GPT-5-mini. The GPT-5-mini rows reuse the designs learned with GPT-5-nano; neither ALMA nor the baselines are re-tuned.

## The controls that decide whether the gain is real

- **Open-ended vs greedy search (Table 2, ALFWorld only).** This is the paper's only ablation, and it varies the parent-sampling rule: greedy always expands the best design so far. With GPT-5-nano it gives 11.9 ± 0.5 (ALMA 12.4 ± 0.5, a 0.5‡ gap, under one combined SE); with GPT-5-mini 77.1 ± 0.8 (ALMA 87.1 ± 1.4). Against Trajectory Retrieval (80.0 ± 1.4) the greedy design is 2.9‡ behind, about 1.8‡ combined SEs. Caveats on the comparison: each search generates its own initial design (Appendix B.3); the greedy tree's root appears to score higher than ALMA's in Figures 14 and 12 (read from small node labels); the best learning-set scores of the two searches look similar; the greedy run is 43 sequential steps, ALMA 11 steps of up to five designs; the gap appears only on the test split, with GPT-5-mini. Each search was run once as far as the paper reports.
- **Not ablated.** The parts of the sampling rule (visit penalty, temperature); sampling with vs without replacement (Appendix B.3 only "expects" a minimal effect); the Meta Agent model; the code abstraction.
- **Variance.** The standard errors are over three Deployment runs of one finished design; memory collection happens once per design. The paper reports one search per benchmark, no repeats, so run-to-run variation of the search itself is unknown.
- **Selection noise.** The output is the best of 43 designs on the learning set. For ALFWorld the learning set is 30 tasks, i.e. 15 deployment tasks × 3 runs (our inference from Appendix B.3; learning-set scores in Figures 12 and 14 lie on a 1/45 grid), so the pick is made on a small, noisy metric. The paper does not quantify this selection effect.
- **Same mechanism for baselines?** No. The baselines are adapted by the authors to the same static protocol (Appendix B.2): Trajectory Retrieval gets top-1 retrieval "due to context length", Reasoning Bank uses ground-truth trajectory feedback, and Dynamic Cheatsheet is frozen to a fixed cheatsheet at deployment. ALMA is searched under the static protocol it is tested on; the baselines are not searched or tuned, and no tuning budget is reported. At test time every design uses GPT-4o-mini and text-embedding-3-small, so model capacity inside the memory is matched.
- **Held-out.** Learning and testing sets are separate tasks. ALFWorld learns on the first 30 training tasks; TextWorld and Baba Is AI are split evenly, with the second half used for testing; MiniHack learns on 30% of its tasks and tests on the remaining 70%. Not stated: whether those splits are random or ordered, and how MiniHack's 30% is picked. TextWorld mixes Treasure Hunter and Cooking games, so an ordered half could shift the game mix (our remark). The paper reports no contamination or overlap audit; it does describe sandboxed execution and human review of learned designs for harmful content.
- **Transfer, shift, scaling.** GPT-5-nano to GPT-5-mini changes the model and the reasoning effort (low to medium, Appendix B.4); the same designs are used. Under ALFWorld task distribution shift (memory from valid seen, test on valid unseen, dynamic memory, GPT-5-mini) ALMA reaches 84.1%; the baseline bars appear only in Figure 5, and ALMA's error bar slightly overlaps Trajectory Retrieval's. In the ALFWorld scaling study (Figure 4, GPT-5-mini, static) ALMA is above the baselines at most memory-collection sizes from 0 to 70 tasks (read from the figure); it is one benchmark and one agent. No design learned on one benchmark was tried on another.
- **Cost.** ALMA's end-to-end memory cost across benchmarks is $0.09, counting the Memory Collection and Deployment phases only (Appendix A.3). The cost of the Meta-Agent search itself is not reported. The introduction says "more cost-efficient than most" baselines; Section 4.4 says lower than all.

## Where the gain is absent or small

- **Baba Is AI.** With GPT-5-nano ALMA ties Trajectory Retrieval at 19.0 (± 2.4 vs ± 6.3). With GPT-5-mini ALMA scores 33.3 ± 2.4, below Dynamic Cheatsheet at 38.0 ± 6.3, a gap of 4.7‡. The abstract says the learned designs win "on all benchmarks" and Section 4.4 calls the improvements consistent across benchmarks; Table 1 does not show that for Baba Is AI. Appendix B.1 gives 52 Baba Is AI tasks in total and Appendix B.4 tests on the second half, split evenly again, which would be 13 deployment tasks (multiples of 1/39 over three runs); Table 1's Baba Is AI values are multiples of 1/42, which implies 14. The paper does not reconcile the two. On the 1/42 grid one task is worth about 7‡ points in one run.
- **Within noise.** TextWorld with GPT-5-nano: 6.2 ± 1.7 against 5.4 ± 1.0 with no memory and 5.3 ± 0.8 for the best baseline. MiniHack with GPT-5-nano: 11.7 ± 2.2 against 9.8 ± 1.7. TextWorld with GPT-5-mini: 75.0 ± 2.3 against 68.8 ± 4.7, about 1.2‡ combined SEs. MiniHack with GPT-5-mini: 20.0 ± 2.9 against 16.7 ± 0.8, about 1.1‡.
- **Low absolute numbers.** In the GPT-5-nano setting the best result on any benchmark is 19.0, and ALFWorld is 12.4.
- **Limits stated by the authors.** Designs are learned offline on a predefined learning set rather than online; the search space is code, so capability is bounded by the underlying foundation models.

## Our read

HarnessRSI score **75**, band ★★★, evidence level **improver**: the improvement mechanism (the sampling rule over the archive) is varied and compared, and the learned designs are evaluated on tasks not used to select them. The paper reports held-out testing, three-run standard errors, a model transfer, a distribution-shift test, a greedy-search ablation with the same number of designs and a deployment-cost comparison. It does not report repeated searches, a search-cost figure, baselines given a comparable search or tuning budget, ablations of the sampling-rule parts, the Meta Agent or the abstraction, a cross-benchmark transfer test or a leakage check. The ALFWorld gains are the clearest; the other columns, the Baba Is AI results and the greedy-vs-open-ended gap with GPT-5-nano are within noise, and the mini gap to greedy search is an ALFWorld-only, single-run comparison.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
