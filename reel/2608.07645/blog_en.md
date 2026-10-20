# MGM: better evidence for a coding agent's self-edits — with the biggest gain on Polyglot

*A Reel interpretation of [arXiv 2608.07645v1](https://arxiv.org/abs/2608.07645v1), **Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution**, by Changzhi Liu, Yilun Liu, Sikuan Yan, Volker Tresp and Yunpu Ma. HarnessRSI Daily score **65**, ★★. Code: [RealLcz/MGM](https://github.com/RealLcz/MGM).*

## What the system changes about itself

MGM edits and inherits the coding agent's **executable scaffold**, not the backbone model's weights. Its contribution is to change the evidence used for an edit: instead of diagnosing one failed attempt in isolation, reuse trajectories already stored in an archive of agent variants. The target agent itself adapts its source code; cross-lineage hybridization is not literal file splicing.

The actual retained Polyglot lineage illustrates what accumulates (Appendix H.1): first read tests and stubs before coding, then extract a structured API contract and implement against it, then add a test-and-repair loop with up to five attempts. Thus executable prompts, control flow and supporting utilities change. The paper specifies the archive policy and operator settings externally; it does not demonstrate the agent autonomously rewriting those policies or the benchmark evaluator.

## The loop, and the keep/reject rule

1. Maintain agent source code, ancestry, trajectories and binary task outcomes. HGM's node-level Thompson sampling chooses evaluations; its clade-level sampling uses descendant outcomes to choose expansions.
2. Choose eligible evidence: **clonal mutation (CM)** uses one failed trajectory; **reaction-norm mutation (RM)** compares the same agent across distinct tasks, with at least one failure; **cross-lineage hybridization (CH)** compares different agents on a shared task not solved by both.
3. For CH, edit the failing agent when the reference succeeds; if both fail, edit the higher-utility lineage. The child belongs to the edited lineage.
4. **Keep a valid child in the archive.** Algorithm 1 admits it through `c.is_valid()` before task evaluation; it does not specify an immediate parent-beating score threshold. Later outcomes affect sampling and final selection. The exact validity checks and final best-belief selection formula are not fully specified.
5. Stop at a finite search budget: the main HGM/MGM comparison uses **200 task evaluations and 24 expansions** each. Report the best-belief agent, not the raw highest observed success rate of a barely evaluated node.

The demonstrated lineage composes successive edits, but the paper does not establish a long-horizon compounding rate or an empirical saturation curve. Finite budgets, isolated containers and bounded task-level loops constrain these experiments; they are not a guarantee of safe unbounded recursion.

## Headline result, as reported

Table 1 uses Qwen3.6-35B-A3B and the same initial scaffold for HGM and MGM within each benchmark:

| Evaluation setting | Initial | HGM | MGM |
|---|---:|---:|---:|
| SWE-bench Verified-60 | 68.3% | 73.3% | 78.3% |
| Polyglot-60 | 50.8% | 77.9% | 93.2% |
| Average across the two benchmarks | 59.6% | 75.6% | 85.8% |

The margin over HGM is much larger on Polyglot: **15.3‡ points**, versus **5.0 points** on SWE-bench Verified. These are evolution-subset results, not independent held-out task scores. The empirical tables give point scores without a stated per-cell evolution-run count, standard deviation or confidence interval. Their averages aggregate benchmarks or models, not demonstrated seed means.

After evolution, the frozen Qwen scaffold solves **210/225 tasks (93.3%)** on full Polyglot (Appendix E.1). The full benchmark includes the evolution subset, so it is not wholly held out. With the scaffold frozen and the backbone replaced by DeepSeek-V4-Pro, full Polyglot reaches **96.89%** (§5.2); this is a model-transfer result, not evidence that evolution itself improved the model weights. Execution settings also change: Qwen uses thinking mode, whereas DeepSeek uses non-thinking mode with different sampling settings (Appendix C.1, p24). Inference budgets are not demonstrated to be matched across models.

## The controls that decide whether the gain is real

- **Budget-matched HGM.** HGM gets the same ancestor, backbone, task subsets, evaluation count and expansion count. It already has the archive and adaptive node/clade sampling; it uses CM only, not MGM's comparative operators. DGM is compared in the surrogate simulation, not in the main real-coding results. The initial scaffold has no evolution. No separate HGM-plus-comparative-evidence or failed-pool-only control isolates these factors beyond the operator ablations.
- **Operator ablations (Table 4, Polyglot-60 only).** Full MGM **93.2%**, without RM **79.7‡%**, without CH **74.6‡%**, all starting at **50.8%** under 200 evaluations with two workers. Times are **40.14**, **43.01‡** and **39.95‡ hours**. These support both operators in this setting, but no seed uncertainty is supplied.
- **Frozen cross-benchmark transfer (Table 2).** Polyglot-evolved scaffolds are evaluated without further self-improvement: SWE-bench Pro **16.7 / 13.3 / 26.7%** and Multilingual **41.7 / 43.3 / 55.0%** for initial/HGM/MGM. Their cross-benchmark averages are **29.2 / 28.3 / 40.9%**, with no variance or CI. Appendix D says ChatGPT randomly and separately selected 60 representative tasks per target benchmark, with language-coverage requirements; these are not the full target benchmarks.
- **Frozen cross-model transfer (Table 3).** On SWE-bench Verified-60, replace the Qwen backbone but keep its evolved scaffold: DeepSeek-V4-Flash **50.0 / 60.0 / 66.7%**, DeepSeek-V4-Pro **45.0 / 70.0 / 75.0%** for initial/HGM/MGM. The two-target-model average is **47.5 / 65.0 / 70.8%**, not a seed average. Both HGM and MGM transfer; this changes models, not evaluation tasks. Qwen uses thinking mode and DeepSeek non-thinking mode, with different sampling configurations (Appendix C.1); inference budgets are not demonstrated matched across models. This caveat does not invalidate the initial/HGM/MGM comparisons within each target model.
- **Defaults and tuning.** Table 6 sets CM/RM/CH weights to **0.10 / 0.45 / 0.45**, RM's minimum task count to two, and failed-pool weight to **1.0**. Our reading of Equation 17: that last setting gives failed tasks no relative sampling boost, despite the general method's ability to upweight them. The paper does not identify a split used to select these defaults or report HGM's tuning budget.
- **Compute cost.** Table 1 reports HGM/MGM wall-clock times on eight H100 GPUs: **93.02 / 96.11 hours** on SWE-bench and **44.20 / 40.14 hours** on Polyglot. MGM is not faster in both settings. Figure 6 and its accompanying text describe comparable operator token costs, but no numerical total-token or dollar-cost accounting is provided. Equal operation counts are not exact token matching; the full-model transfer result does not include the earlier donor evolution cost as a separately tabulated end-to-end total.
- **Simulation is a conditional diagnostic.** The 100 seeds and 95% CIs belong to the additive-fitness simulation, not Tables 1–4 or 7. Comparative edits are assigned a fix-quality advantage; at the null ratio **1.0**, MGM becomes HGM-like. The oracle is an idealized optimum, not a competing coding system. The proof assumes informative comparisons, sparse causal defects and an editor able to use the evidence.

## Where the gain is absent or small

- **Different evolution backbone (Table 7):** Qwen3-Coder-Next-80B-A3B starts at **33.3%**, reaches **40.0%** with HGM and **41.7%** with MGM on Verified-60. That **1.7‡-point** margin has no uncertainty estimate; it cannot be called statistically reliable. The primary gains are therefore not uniform across backbones.
- **Language coverage is not a per-language gain control.** Full Polyglot counts are C++ **25/26**, Go **36/39**, Java **43/47**, JavaScript **46/49**, Python **33/34**, Rust **27/30**. High absolute performance is spread across languages, but HGM language-level counts are not provided, so these do not locate the comparative gain.
- **Sparse evidence:** the authors note that with few trajectories or little task overlap, MGM may behave like single-trajectory methods.
- **Unresolved prose/table difference:** Appendix F.2 mentions **61.7%** for Qwen3.6 MGM, whereas Tables 1 and 7 give **78.3%** for that setting. We checked the other backbone, transfer and ablation rows and found no matching result to resolve the reference. We use the table value without inferring a cause.

## Our read

HarnessRSI score **65**, band ★★, evidence level **retained** (latest judgment: b18). The useful evidence is matched-count HGM comparison, operator ablations, frozen cross-benchmark and cross-model transfer, and substantial reported evolution cost. This supports retained scaffold improvements, not demonstrated autonomous improvement of the search policy itself.

Leakage scope matters: the paper says agents cannot access **private test cases or test results** during evolution, but the archive necessarily uses outcomes on the evolution tasks, and the evolved code explicitly reads and runs available repository tests. The main 60-task scores are not a separate holdout; full Polyglot contains that subset. Cross-benchmark transfer is the cleaner unseen-task check. The paper acknowledges possible public-benchmark/pretraining overlap and reports no dedicated contamination audit. Empirical run/seed variance, default-selection split, baseline tuning budgets and long-horizon stability remain unspecified.

**Relation to Red Queen Gödel Machine:** this PDF neither cites nor directly compares with arXiv 2606.26294. Its explicitly inherited search machinery and main real-coding comparator are HGM, the **Huxley Gödel Machine**. We do not import the Red Queen paper's mechanisms or claims.

*‡ denotes our arithmetic or verified PDF-table transcriptions missing from the gate's cached text, distinguished in SOURCE.md; no paper figures are reused.*
