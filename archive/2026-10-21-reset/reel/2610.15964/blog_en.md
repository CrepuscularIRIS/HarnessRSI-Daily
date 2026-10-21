# TeSearch: evolve the tests that judge an agent's self-edits—not proof that the edits improve the agent

*A Reel interpretation of **Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents**, [arXiv 2610.15964v1](https://arxiv.org/abs/2610.15964v1). HarnessRSI Daily score **64 · ★★ · retained**. Code: [ccsnow127/TeSearch](https://github.com/ccsnow127/TeSearch).*

## What changes, and what is kept

TeSearch evolves **executable Python unit-test suites** with a frozen LLM. The retained artifact is a regression-checking signal for later harness rewrites, not model weights. The suites contain pytest test functions, fixture scaffolding, stubs for collaborators, inputs and assertions. The LLM writes them from the original module source; the prompt explicitly asks it to compute expected values from that source. Breeding also exposes uncovered lines, surviving search mutants, parent suites and failing-test exceptions (Appendix D).

Quality is coverage multiplied by mutation-kill score, called hypervolume (hv). Size is the number of **written test functions**, not assertions, runtime or tokens. Importantly, coverage and mutation score are measured on the suite's **passing subset**; the written size still counts its tests (Algorithm 1).

## The loop and keep/reject rules

1. Generate seed suites without specifying a test count. Measure and provisionally file them before building the size grid; then re-file under the grid's Pareto rule.
2. Choose a size niche using quality-gated, size-annealing UCB. An online kernel corrects the LLM's tendency to miss requested counts and predicts where a generation will land.
3. Select the nearest Pareto-front parent on either side of the target in log size; if one side is empty, use the other side. Show the stronger parent last and ask the LLM to compress or expand it.
4. Measure the child and file it at its **actual written size**, retaining nondominated coverage/mutation trade-offs within that niche. Calls that fail measurement still consume the budget. Out-of-range suites enter overflow niches rather than being discarded.
5. Deliver the highest-hv suite, breaking ties by smaller written size. The prompt's requested compression/expansion improvements are instructions, not an additional acceptance gate in Algorithm 1.

The later **harness-revision gate** is different: generate a suite once from the original module, and reject a rewrite if it fails tests that passed on the original. Its comparator is the repository's pre-existing test suite; the paper does not identify those tests' individual authors. Passing this regression check does not establish that a latency, token or capability improvement actually occurred.

## Headline results, as reported

Table 1 reports means over **129 TestGenEval modules**, with **50 model calls per module** and separate search/evaluation mutant folds. These are module averages, not reported multi-seed means; neither repeated search-run counts nor SDs/CIs are supplied.

| Backbone | TeSearch hv / mean tests | Highest-hv external baseline, hv / mean tests |
|---|---|---|
| GPT-5.4 | 0.916 / 38.6 | OpenEvolve: 0.831 / 51.5 |
| Claude Opus 4.8 | 0.976 / 29.1 | GEPA: 0.895 / 67.2 |
| Gemini 3.1 Pro | 0.908 / 36.3 | Beam search: 0.838 / 52.6 |

TeSearch has the highest mean hv and smallest mean suite among the LLM methods on each backbone. Those baseline rows are quality leaders, not size leaders: Cursor on Gemini already delivers 37.0 tests. Pynguin is smaller at 20.4 tests but has hv 0.090, and is scored only on its 40 supported modules.

Table 2 evaluates the revision gate on **mini-swe-agent**, not TestGenEval. GPT-5.4 generates revisions to eight harness modules from paired behavior-preserving/changing intents. Of 512 generated revisions, 470 enter the evaluation after two annotators confirm that they realize their intent (agreement κ = 0.74): 217 divergent and 253 equivalent. The denominator excludes unconfirmed revisions; this is a curated revision-pool diagnostic, not an unattended longitudinal evolution run.

Pooled divergent-revision rejection is **59.9% versus 25.3%** for repository tests. The trade-off is **4.0% false alarms versus none**: TeSearch rejects 10 equivalent revisions. Mean decision time is **3.5 s versus 5.9 s**, with no model call at gate time. The paper does not specify the suite-generating backbone for this particular gate experiment; its three-backbone test-generation result should not be projected onto Table 2.

## Controls that decide what the gain means

- **Ablations, Table 1.** On Claude Opus 4.8, full hv/size is 0.976/29.1; without kernel 0.917/40.8, without UCB 0.960/34.4, without nearest parents 0.934/33.2, without size pressure 0.954/84.6. All ablations lower mean quality and enlarge mean suites on each backbone. No ablation variance is reported.
- **Budget and feedback access.** The LLM methods share the 50-call cap. OpenEvolve explicitly receives the same feedback. Claude Code and Cursor receive harness feedback as tool output and instructions to maximize quality/minimize size; Claude Code runs only on its own backbone. GEPA uses a global Pareto pool over coverage, mutation and negative size. Iterative refinement, best-of-N, beam search, MIPROv2 and ACE are named as call-matched baselines, but their individual feedback wiring is not detailed. Pynguin uses a 6000 s wall-clock allowance, not model calls. Baseline hyperparameter-tuning budgets are not reported; equal calls do not demonstrate equal total compute. Table 2 compares only repository tests, not gates using these other generated suites or a measured rollout gate.
- **Split and leakage boundary.** Cosmic-ray mutants are generated with a fixed seed and split into search and held-out evaluation folds **within the same module**. This is not held-out-module or cross-task transfer. Expected outputs from the module are intentionally visible to the test writer: they specify existing behavior, rather than serving as hidden evaluation-task solutions. The gate suite is described as generated from the original module before checking revisions; no revision labels/solutions are described as generation input. However, no explicit contamination audit or formal separation protocol between suite generation and the revision pool is reported. The source-based tests can preserve implementation quirks as well as intended behavior—our reading of the regression objective, not a measured leakage finding.
- **Default selection.** The kernel spread is fixed at its “holdout median”; Appendix A specifies σ = 0.10, the resulting grid ratio ρ = 1.22, and the grid upper-range parameter γ = 4 (pp9–10). The holdout's identity, split and separation from evaluation are not specified, nor is an independent tuning split identified for these settings. Numerical defaults for η, α, c_e, H and the seed-suite count are not supplied. We cannot verify test-independent tuning.
- **Cost.** Gate execution is cheap after generation, but 3.5 s is not the cost of building the suite. Search executes coverage/mutation checks; generation dollars, tokens and total wall time are not itemized. The fixed seed mentioned for mutants is not evidence for repeated evolution seeds.

## Where gains are small or absent

The Table 1 mean-quality advantage appears on every backbone, but no per-module breakdown is supplied, so its concentration across the 129 modules cannot be checked. The gate improves divergent rejection on every listed module, with very uneven margins: **actions_text 0.040 → 0.560** and **content_string 0.057 → 0.600**, versus **agents/default 0.529 → 0.588**. Cache control still detects only 0.414 of divergent edits, and the model client 0.421; the latter has false-alarm rate 0.080 versus 0.000. There are no CIs to establish the reliability of the small agent-loop margin.

The pooled speedup is not universal: actions_toolcall takes 3.1 s versus 3.0 s, cache_control 3.0 s versus 2.9 s, serialize 3.1 s versus 2.9 s, and content_string ties at 2.9 s. No downstream task-success improvement from repeatedly adopting gated edits is reported.

## Our read

**Score 64 · ★★ · evidence level retained**, from the latest repository judgment. Reports: held-out mutants, call-budget matching, suite-search ablations and a retained-suite revision-gate diagnostic with execution latency. Does not report: multi-seed uncertainty, cross-task artifact transfer, a contamination audit, complete generation cost or a long-run gated-versus-ungated agent comparison. The stored budget judgment is **partial**: call matching is explicit, total compute and tuning parity are not. The retained label should be read narrowly: a once-generated signal catches later revisions, not evidence that the agent's improvement mechanism itself improves over generations.

**Takeaway:** optimize the regression signal, not just the rewrite generator. TeSearch makes that signal stronger and compact, while still missing divergent edits and rejecting some equivalent ones. Better regression detection is useful evidence—not yet a demonstrated recursive performance gain.
