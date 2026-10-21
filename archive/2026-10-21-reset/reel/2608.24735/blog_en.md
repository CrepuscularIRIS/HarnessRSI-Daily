# Metaⁿ: a fixed improver builds deeper solver stacks—not an improver that rewrites itself

*A Reel interpretation of [arXiv 2608.24735v1](https://arxiv.org/abs/2608.24735v1) (HarnessRSI Daily score 67, two-star band, evidence level retained). Code: [minnesotanlp/meta-n](https://github.com/minnesotanlp/meta-n).*

## What the system changes about itself

Metaⁿ retains **Python pre-processes and callable helper libraries** around a solver. A fixed meta-operation, Ω, reads execution traces, evaluator feedback and earlier layers' code, then writes the next layer. The improver and solver use the same backbone: Gemma 4 31B-IT or GPT-5.2. Neither weights nor Ω's prompt template are updated. This is a fixed improver improving a separate solver stack, not the improver model learning to rewrite its own improvement algorithm.

Recursion is designed into the architecture. What adapts is the selected depth and the generated code; the reported layer roles are not manually prescribed. However, the input formatter **is depth-dependent**: raw traces at the first added layer become structured performance/failure summaries at deeper layers (Appendix E.2). The authors acknowledge that this partly scaffolds the tactical/strategic division of attention.

## The loop, and the keep/reject rule

1. Run a base solver, either single-shot with executor-level retries or agentic with up to 8 observe/act turns.
2. Sample parent chains from an archive using their scores plus an exploration bonus. Ω reads their traces and code, with rival traces for tasks where a parent trails the archive.
3. Emit a pre-process that passes strategic context inward and helpers that are prepended to the final solver script. Deeper helpers override earlier ones by name; the inner solver is wrapped, not patched.
4. Validate generated code and smoke-test helper definitions; invalid helpers are skipped. Nonempty candidate chains enter the growing archive even if their mean score is worse. This is **not an accept-only-if-better gate**.
5. During search, track both the best single chain and the mean of per-task best scores across chains, called **archive-best** (§2.4; Algorithm 1). This archive/search estimator lets different tasks be won by different chains; it is not one universal chain. Its mapping to the reported held-out estimators is not fully specified; see the S2D qualification below.

Linear deepening stops on empty output, patience without sufficient improvement, or a depth cap. Evolutionary search also has benchmark-specific iteration and patience settings. Maximum depth is 10 except TerminalBench's 4; useful depths are generally 3–4, reaching 6 in symbolic regression. Fixed drivers, wrapper isolation, code checks and finite budgets limit the process; they are not a proof of general safety.

## Headline results, as reported

Mean ± standard deviation over seeds 42/43/44, agentic mode (Tables 1–2). CO-Bench and Symptom2Disease (S2D) are labelled held-out test; **ARC-AGI-2 below is development**, not held-out test.

| Backbone / benchmark | Metaⁿ archive-best | Metaⁿ best chain | OpenEvolve | Gödel Agent |
|---|---|---|---|---|
| Gemma / CO-Bench | 0.851 ± 0.014 | 0.782 ± 0.016 | 0.814 ± 0.022 | 0.451 ± 0.023 |
| GPT-5.2 / CO-Bench | 0.870 ± 0.011 | 0.806 ± 0.017 | 0.702 ± 0.025 | 0.527 ± 0.033 |
| GPT-5.2 / S2D | 0.725 ± 0.014 | 0.734 ± 0.020 | 0.721 ± 0.007 | 0.708 ± 0.037 |
| GPT-5.2 / ARC-AGI-2 dev (pass@2) | 0.331 ± 0.010 | 0.123 (one seed) | 0.003 ± 0.001 | 0.054 ± 0.006 |

**Unresolved S2D estimator tension.** The held-out archive-best is below best-chain on both backbones: GPT-5.2 0.725 ± 0.014 versus 0.734 ± 0.020 (Table 2), and Gemma 0.733 ± 0.015 versus 0.743 ± 0.034 (Table 1). On the same scored tasks and archive, the per-task-max search definition cannot yield a value below a constituent chain. Other populated archive/chain cells in Tables 1–2 do not show this inversion. The PDF does not specify the held-out selection/application protocol sufficiently to reconcile these S2D rows with the definition. We preserve the published values and leave this unresolved, without proposing a cause.

ARC-AGI-2 development results use **pass@2** (Appendix C, p16). The paper qualitatively says only Metaⁿ solves any held-out ARC tasks. We could not locate a numerical held-out ARC result or split size in the full PDF, despite Table 2's caption pointing to the text. Its nonzero baseline development scores are not a contradiction of the held-out-zero claim: these are different splits. We do not substitute 0.331 for the missing held-out number.

Nor is this an all-method/all-backbone sweep: GPT-5.2 LawBench and AlgoTune were not run; TerminalBench has no OpenEvolve or Gödel Agent comparison. AlphaEvolve Math, AlgoTune and symbolic regression report benchmark scores without held-out splits. TerminalBench's standard deviations are across categories, not seeds; GPT-5.2 TerminalBench is single-seed.

## The controls that decide whether the gain is real

- **Component ablations (Table 3, validation).** Gemma CO-Bench: full 0.845, without library injection 0.825, without outer context 0.751, without recursion 0.714. The authors attribute about 72% of recursion's lift to context, about 15% to code transfer. GPT-5.2 CO-Bench is 0.886 versus 0.806 without recursion; AlphaEvolve Math is 0.917 versus 0.759. Table 3 gives means without per-row variance or confidence intervals, despite the general three-seed policy. GPT depth-1 uses four resamples per seed at about 870K tokens; no held-out pass or full-stack token-matched ablation is reported. The depth-1 validation 0.806 and best-chain test 0.806 are different results.
- **OpenEvolve compute controls (§3.2).** CO-Bench is described as near-identical in token budget. Full-budget prompt runs use 10–20 times OpenEvolve's tokens; at OpenEvolve-capped spend, Gemma Metaⁿ still reaches S2D 0.732 ± 0.023 versus 0.718 ± 0.022 and LawBench 0.784 ± 0.013 versus 0.745 ± 0.034. The S2D difference is within seed spread. OpenEvolve is not given Metaⁿ's shared cross-task library in a separate control.
- **A repaired Gödel Agent, not its failed interface (§3.2, Appendix J).** Main tables use the corrected per-task configuration. On GPT-5.2 CO-Bench seed 42, extra budget raises its test score from 0.502 to 0.615 and 0.628, at 5.6M and 11.4M tokens. Metaⁿ's cited 0.870 is a three-seed mean at a stated 17M tokens. This is a useful budget sweep, **not exact token parity or a seed-matched proof that compute cannot explain any remaining gap**.
- **Consolidation guard (Appendix G).** On an 8-task CO-Bench band, three-seed consolidation scores 0.71 ± 0.02 against compute-matched best-of-4 resampling's 0.61 ± 0.03; the reported gain is +0.10 with 95% CI [+0.04, +0.16]. Zero regressions are guaranteed by inheriting frozen best traces for non-focus tasks—not by making every newly executed chain non-regressing.
- **Selection and tuning (§C–D).** The failure/success trace ratio was tuned on a 10-task CO-Bench pilot; the convergence threshold was motivated by CO-Bench variability. The paper lists benchmark-specific beam, branching, patience and iteration settings but does not identify the split used to choose all defaults or a baseline hyperparameter-search budget. Held-out captions do not supply detailed split construction or sizes. No dedicated leakage audit or frozen-artifact cross-benchmark transfer evaluation is reported.
- **Search cost (Table 6).** Gemma CO-Bench agentic seed 42 uses 29 candidates and 36.1M tokens; single-shot uses 5.3M. These are whole search-run costs. CO-Bench takes roughly 10 hours agentic versus 3 single-shot; TerminalBench roughly 28 hours, dominated by Docker startup. ARC costs approximately $632 per Metaⁿ seed. Cost is not interchangeable across backbones.

## Where the gain is absent, small, or hard to compare

- **Depth does not compound monotonically.** Mean depth-2-to-3 lift is −0.006; 41% of chain/task pairs regress at depth 3. Per-depth mean peaks at 0.726 at depth 3 and falls to 0.602 at depth 6. Deep specialists can still win individual tasks, while the archive keeps shallower fallbacks. That supports selective reuse, not runaway improvement.
- **Small prompt gains; larger diverse-code gains.** S2D best-chain margins overlap seed ranges on both backbones; the authors claim no significance. Gemma CO-Bench's best chain (0.782) is below OpenEvolve (0.814), even though archive-best wins. Under GPT-5.2, symbolic regression leads both baselines in all four domains (Table 9), so that result is not only one domain carrying the family mean.
- **AlgoTune's inversion is concentrated.** In seed 42, single-shot averages ×18.47 over seven logged tasks; agentic averages ×14.11 over eight, or ×15.96 on the matched seven. The FFT kernels drop from ×9.72 to ×1.69 and ×4.17 to ×1.12, accounting for most of the lost speedup. The aggregate is also strongly influenced by convolve2d_full_fill at ×105.37 versus ×101.79. Table 10 has no per-task variance.
- **AlphaEvolve Math pools differ (Appendix C).** GPT-5.2 Metaⁿ and Gödel Agent use 16 problems, OpenEvolve a 10-problem subset; Gemma single-shot uses 15 and agentic 16. These aggregates are not a common-task comparison. We therefore do not treat their headline gap as a clean matched-benchmark effect.
- **Short SWE-Bench diagnostic.** With three iterations and beam/branching both 2, the initial candidate remains best and Ω never activates. This is a bounded negative result, not a general claim about SWE-Bench.

## Our read

HarnessRSI score **67**, two-star band, evidence level **retained** (judgment batch b18). Reports: partial held-out evaluation, multi-seed main comparisons, optimizer costs, component ablations, selected compute controls and cross-task sharing within an archive. Does not establish: an improved Ω, general cross-benchmark transfer, a leakage audit, exact parity everywhere, or indefinitely compounding gains.

Our reading is that the strongest result is **a fixed improver exploiting richer solver context and an archive**, especially on diverse code tasks. The recursive architecture is intentional; depth and generated roles adapt inside it. The local retained-level judgment is consistent with that boundary. Its ARC supporting quote is qualitative, and its budget-matched flag should be read with the specific controls and unequal budgets above—not as blanket parity. No judgment records were changed.
