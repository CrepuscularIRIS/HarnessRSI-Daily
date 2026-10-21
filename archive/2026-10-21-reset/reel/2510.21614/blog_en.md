# Huxley-Gödel Machine: select a coding agent for its descendants, not just its own score

*A Reel interpretation of [arXiv 2510.21614v3](https://arxiv.org/abs/2510.21614v3), **Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine**. HarnessRSI Daily score **63**, band **★★**, evidence level **retained**. Code: [metauto-ai/HGM](https://github.com/metauto-ai/HGM).*

## What the system changes about itself

HGM grows a tree of **coding-agent repositories**. A selected agent edits its own code to create a child; that child can later become the self-modifier. The retained artifact is agent code, not trained model weights. Appendix F shows changes to the agent loop and error/test handling, alongside nested patch histories. The paper specifies the HGM search controller and benchmark utility externally; it does not enumerate protected files or establish that the controller/evaluator itself is rewritten or immutable. “Self-improvement” here should not be read as permission to rewrite every layer.

The central idea is **clade-metaproductivity (CMP)**: a currently modest agent might spawn a productive lineage. HGM estimates this potential from pooled successes and failures of agents in its subtree, including the agent itself. This operational estimate is not the true future-CMP oracle of the theorem.

## The loop, and the keep/reject rule

1. Maintain a tree, individual success/failure counts and clade-aggregated counts.
2. A widening rule chooses expansion versus evaluation. For expansion, Thompson sampling uses **clade** counts to pick a parent, which creates a self-modified child.
3. Add the child to the archive. Algorithm 1 shows **no requirement that it first beat its parent**. For evaluation, independently Thompson-sample an agent using its **own** counts and run one benchmark task; update its ancestors' clade counts.
4. Repeat asynchronously until the computational budget is exhausted; return the stated posterior-percentile “best-belief” agent, rather than always following the latest child.

All reported HGM experiments use the asynchronous variant (p7). Appendix B describes a parallel warm start of five expansions per process; this async-specific implementation detail is described separately from the base HGM pseudocode in Algorithm 1. A separate unresolved specification issue concerns final selection: the prose calls final selection a posterior percentile, but its formula defines the function as the regularized incomplete beta function and sets ε = 1. **Our mathematical reading:** the literal Beta CDF at one is identical for every proper posterior, so the printed formula does not define a useful ranking. The intended implementation is unresolved from the paper alone.

The finite evaluation budget and execution timeouts bound the experiment: one hour per execution in the method comparison, five hours for modification and evaluation in the full-scale experiment. These are not a formal runaway-loop safety guarantee. Descendant code can compound improvements, but the paper does not establish sustained acceleration or characterize eventual saturation.

## Headline result, as reported

Table 2 compares final selected agents with a **maximum allowance of 800 task evaluations**, not a held-out test split:

| Method | SWE-Verified-60 accuracy | Allocated CPU-hours | Polyglot accuracy | Allocated CPU-hours |
|---|---:|---:|---:|---:|
| Initial ancestor | 40% | — | 20.3% | — |
| SICA | 50.0% | infinite loop | 25.4% | 572 |
| DGM | 53.3% | 1231 | 27.1% | 2385 |
| HGM | **56.7%** | **517** | **30.5%** | **347** |

SWE uses GPT-5 for modification and GPT-5-mini for task evaluation; Polyglot uses Qwen3-Coder-480B-A35B-Instruct and Qwen3-Coder-30B-A3B-Instruct, respectively. The larger Qwen is mixed int4/int8 quantized. SICA's SWE run encounters repeated context-window errors after **360 evaluations**: it did not complete an equal-budget comparison.

With a different, stronger bash-only initial agent and **8000 evaluations** on full SWE-Verified, accuracy rises from **53.2% to 61.4%**. Those 500 tasks were used for optimization, so this is not independent test performance.

## The controls that decide whether the gain is real

- **What each baseline gets.** SICA and DGM start from the same DGM-derived ancestor as HGM, use the same backbone pair, and receive the same evaluation ceiling. SICA gets the entire history when modifying the best-scoring agent and evaluates the newest agent on the full dataset. DGM samples parents using performance and child counts and progressively evaluates the newest child. Neither is given HGM's clade-guided, decoupled asynchronous policy. There is no isolated clade-versus-node or asynchronous-versus-synchronous ablation, so the combined method comparison does not attribute the gain to CMP alone.
- **Budget and tuning.** The ceiling matches task evaluations, not tokens, API dollars or CPU-hours. Defaults are τ = B/b, α = 0.6 and ε = 1. The paper does not report a split used to choose them, a hyperparameter sweep or baseline tuning budgets. Numerical decoding temperature, interaction-length cap and CPU worker count are not specified; this is separate from the missing tuning-split information.
- **Estimator diagnostic, not oracle competition.** Table 1 reports weighted correlations with post-hoc descendant performance: HGM **0.778** versus DGM **0.285** and SICA **0.444** on SWE-Verified-60; **0.626** versus **0.383** and **0.274** on Polyglot. To avoid direct target reuse, the diagnostic excludes the root and the child branch containing the target maximum from HGM's predictor. This is a meaningful guard, but not a prospective held-out prediction test or an isolation of CMP on a common search tree. The unweighted Polyglot HGM cell is **0.873** in Table 1 and **0.8783** in its accompanying prose; after checking all weighted/unweighted rows and Appendix D, we leave that discrepancy unresolved and use the table value.
- **Held-out transfer.** The SWE-Verified-selected artifact is evaluated on SWE-Lite without reported re-optimization. Standard Lite has **300** tasks, **93** overlapping with Verified; the filtered evaluation removes them. Table 3, GPT-5-mini, reports initial ancestor **34.8% / 44.0%**, a local SWE-agent rerun **39.6% / 47.6%**, and HGM **40.1% / 49.0%** (filtered / standard). The filtered result is the cleaner evidence for retained generalization; standard Lite is partly exposed through optimization.
- **Leakage boundaries.** Polyglot agents explicitly cannot access private test cases or private test results. The Lite overlap filter and CMP diagnostic exclusions are also reported. The paper does not report a broader contamination audit or an explicit firewall preventing SWE self-modification from seeing optimization problems; optimization tasks are repeatedly evaluated. Do not call these scores all unseen.
- **Uncertainty and cost.** Tables 1–4 do not state evolution-run/seed counts or give SDs, SEs or CIs. These are not documented multi-run means; we also cannot infer that they are single runs. Appendix B notes early asynchronous success-rate inflation from easy tasks finishing sooner, barely observed after more than 50 evaluations. Table 2 reports allocated CPU-hours, not necessarily elapsed wall time or total LLM compute. Approximately **$5000** covers the experiments across all three methods; the paper does not isolate the full 8000-evaluation HGM run's cost.

## Where the gain is absent or small

The gains occur on both Table 2 benchmarks, but the paper gives no per-repository or task-category breakdown to test whether a few tasks carry them. The strongest external comparisons are much narrower than the gain over the initial ancestor.

On filtered Lite with GPT-5-mini, **40.1% versus 39.6%** is a small margin without uncertainty estimates. On the GPT-5 transfer (Table 4), HGM reaches **47.8% filtered / 57% standard**, versus **48.3% / 56.7%** for the leading SWE-agent: HGM is **one task behind on filtered Lite**, as the paper states, while slightly ahead on standard Lite. This is one model-size transfer within the GPT family, not a broad cross-family transfer study.

The authors' **human-level coding-agent development** claim is a comparison with human-engineered agents, not with human programmers solving tasks. Its reference is the checked SWE-Lite leaderboard as of **24 October 2025**; the leading design is identified as SWE-agent with Claude 4 Sonnet. Table 3 reruns that design locally with GPT-5-mini; Table 4 compares HGM with GPT-5 to the leaderboard design, not a same-backbone GPT-5 SWE-agent control. The paper supplies the judgment through benchmark scores; no independent panel certifies human-level design or unrestricted coding ability.

Theorem 1 requires true CMP, repeatable trials, a final-agent-only objective, free proof computation and unit-cost modifications; Appendix A additionally specifies a finite known budget and utility knowledge. That oracle result does not prove the empirical estimator optimal. The paper compares directly to **DGM and SICA**, not Red Queen or Mendel; no claims from those later papers are imported here.

## Our read

HarnessRSI **63 · ★★ · retained**. The record credits transfer, optimizer cost and a comparison of improvement mechanisms, with partial held-out and budget-matching evidence. The filtered Lite evaluation supports a retained code artifact, while the method-comparison scores remain selection-set results. Reports include overlap filtering and target-reuse exclusions; missing evidence includes replicated uncertainty, retained-component/isolated-policy ablations, baseline tuning budgets and a broader contamination audit. The archive supports useful finite-budget search, not a demonstrated open-ended acceleration of the improver itself.
