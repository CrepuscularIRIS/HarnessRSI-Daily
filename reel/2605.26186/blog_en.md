# SetupX: reusable setup repairs help — but the failure-memory gain is smaller than the full-system gap

*A Reel interpretation of [arXiv 2605.26186v2](https://arxiv.org/abs/2605.26186v2), **SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?** HarnessRSI Daily score **64**, band **★★**. Code: [OpenDataBox/SetupX](https://github.com/OpenDataBox/SetupX).*

## What the system changes about itself

SetupX retains a **database of reusable environment-repair experience**, not updated model weights. An eXPerience Unit (XPU) contains diagnostic signals and applicability conditions, natural-language root-cause advice, executable atomic operations, and hit/success/failure telemetry. Its source material is setup trajectories containing commands and error logs, plus prosecutor–judge verdicts when available. The distiller extracts problem–fix pairs even from runs ultimately judged guilty: the store is neither a dump of failed tasks nor a library restricted to wholly successful episodes.

The failure signal has several levels. The in-loop verifier attributes test errors to environment setup or intrinsic repository defects. The final prosecutor independently probes dependencies, documented commands and tests; a judge confirms or dismisses charges with targeted commands. Any upheld charge, or a timeout, means the run fails. Table 4 also counts missing evaluation data as failure, without identifying which cells have that status or disclosing its frequency or distribution. A cross therefore need not be a completed adverse functional verdict. Optional-dependency and external-factor charges can be dismissed. This is role separation using the same backbone, not a separate human ground-truth audit of single-repository verdicts.

## The loop, and the keep/reject rules

1. Distill trajectories into generalized XPU records. A vector pre-filter and an LLM check for semantic duplicates; confirmed duplicates merge their signals and advice, while other candidates are inserted. The paper does not specify a held-out performance gate before inserting a new experience.
2. Retrieve candidates using the current situation and raw error output, incorporating historical utility; an LLM selects up to three entries from ten candidates.
3. Snapshot the Docker container, adapt a suggested repair to the current repository, execute it, and compare the error state before and after. A successful trial keeps its changes; otherwise the snapshot is restored. The agent can also retreat through multiple earlier snapshots. This local environment gate is distinct from admitting an XPU to the database.
4. At the next retrieval, audit up to five steps after the preceding retrieval anchor. Adopted advice that resolved or improved the problem is a success; adopted advice followed by a persistent or worse problem is a failure; uncertain adoption or contribution is neutral. These outcomes change telemetry and future ranking, rather than automatically deleting failed entries.
5. The setup prompt allows FINISH only after successful in-loop VERIFY; the independent-role prosecutor–judge audit then supplies the final evaluation verdict.

The telemetry tier thresholds, a = 0.2 and b = 0.1, were chosen from current XPU telemetry to give roughly balanced tiers. **No separate training/development split for choosing these defaults, retrieval settings or baseline tuning is specified.**

## Headline result, as reported

The main experiment uses **100 curated Python repositories**, selected from the 329-repository EnvBench pool after test-asset filtering and preliminary difficulty trials. Revisions are pinned. All compared systems use **qwen3.5-plus**, a fresh **ubuntu:22.04** container, a **3600-second** global timeout per run, and the same final prosecutor–judge adjudication (§6.2).

| Single-repository pass rate | Reported result |
|---|---:|
| SetupX + XPU | 92% |
| SetupX without XPU | 82% |
| Claude Code, strongest CLI baseline | 73%‡ |
| ExecutionAgent (ExecAgent), strongest specialized baseline | 59%‡ |

The paper reports gaps of **19 percentage points** over Claude Code and **33 points** over ExecAgent. But the comparison isolating the retained experience store is **92% versus 82%**, an explicitly reported **10-point** increment. The rest of the full-system gap cannot be credited to failure memory alone.

These are pass fractions over repositories, **not repeated-run averages**. The conclusion describes the evaluation as single-run containerized setup; the main comparison and retrieval ablations give no seed variance, confidence intervals, or repeated-evaluation selection protocol. A common time ceiling does not establish matched tokens, retries, or lifetime experience-acquisition compute.

## The controls that decide whether the gain is real

- **Memory exclusion, not an unrelated-distribution test.** The clean database has 600 advice entries from the EnvBench Python pool. Entries corresponding to the 100 evaluation repositories were removed before evaluation (§6.2, Appendix G). Thus same-repository exclusion is reported. The paper does not report a fork/near-duplicate/family leakage audit, or state whether online telemetry and new experiences are frozen or reset between evaluation targets. Shared dependencies and related repositories are not excluded by the described rule; their actual overlap is not quantified.
- **Retrieval quality matters (Figure 6b).** Clean knowledge with LLM selection scores 92%‡; direct vector retrieval scores 86%‡. With synthetic noisy knowledge, selection scores 88%‡ and direct retrieval 81%‡, against 82% without XPU. The paper reports reranking gains of 6 points on clean knowledge and 7 on noisy knowledge. This is a synthetic-noise stress test, without variance, not proof that all real failure memories self-correct.
- **What each baseline receives.** Claude Code, OpenCode and Qwen Code each receive the common model, container, timeout and final adjudicator. ExecAgent, Repo2Run and EnvBench receive those same common conditions. No comparable XPU database or failure-memory augmentation is reported for any of these baselines. Repo2Run does have command-level adaptive rollback; SetupX adds agent-controlled multi-step snapshot rollback. SetupX-without-XPU is the direct store-removal control. There is no separately reported rollback-only or telemetry-only ablation, nor an equal-memory baseline, equal-retry comparison, or baseline tuning-budget account.
- **Stronger backbone, no higher score here.** Under Selector + Clean, Claude Opus 4.6 also scores 92%, with API cost reported as more than 10 times higher (§6.4). This is one matched configuration on this benchmark, not a general model ranking. Absolute API costs, donor trajectory generation, distillation, embedding, delayed audits and snapshot overhead are not itemized; the cost of accumulating the failure store remains unquantified.
- **Complementary multi-repository evidence.** On 22 families, both SetupX and Qwen Code reach at least Mostly on **17/22**. SetupX has **6 Full / 11 Mostly**, versus **1 Full / 16 Mostly** for Qwen (Table 2). Three evaluators independently inspect containers and resolve disagreements by consensus; this is not the single-repository prosecutor–judge protocol. The gain is at the Full–Mostly boundary, not in the aggregate at-least-Mostly rate. However, Table 2 (p17) and Appendix E (p18) report Qwen’s MISP run encountering port 80 occupied by a stale Saleor process/container from a previous family. Cross-family service isolation was therefore imperfect; no corrected clean rerun is reported. MISP is Partial for both, so this does not establish that a clean rerun would change either aggregate.

## Where the gain is absent or uneven

The experience increment is largest in the **medium-difficulty** stratum: 89%‡ with XPU versus 69%‡ without it. Low difficulty is near the ceiling, 100%‡ versus 95%‡; high difficulty is 79%‡ versus 72%‡ (Figure 5a). The result is therefore not simply a story of the hardest repositories driving all the memory gain. The paper highlights toolchain/testing/documentation, with zero failures versus five on 20 repositories for the strongest CLI baseline, while remaining SetupX failures cluster in AI/ML and DevOps. This is a single curated Python benchmark, not a broad repeated transfer study.

Table 4 also contains individual reversals: **trax, neuralforecast, ajenti and civet** pass without XPU but fail with it. These are observed outcomes, not a causal diagnosis of why the runs diverged. Claude Code passes trax, neuralforecast, civet, iree-llvm-sandbox and qiita, where SetupX + XPU fails; a better aggregate is not universal per-repository dominance.

In the multi-repository track, **robotframework** is Mostly for SetupX versus Full for Qwen; **label-studio** is Shallow versus Partial; **flyte** and **bitcart** are Partial versus Mostly. **MISP** is Partial for both. The table lists label-studio, flyte, MISP, bitcart and frappe/erpnext below Mostly for SetupX; Appendix E's subsequent prose calls them “four Partial/Shallow cases.” That wording does not reconcile with the rows and printed aggregate. We use Table 2 and leave the discrepancy unresolved, without assigning a cause.

## Our read

HarnessRSI score **64**, band **★★**, evidence level **retained** (latest local judgment: batch b17). The strongest supported claim is that **retrieved, retained setup experience helps on repositories whose own entries were excluded**, on top of a useful verification-and-repair harness. Store removal and retrieval/noise controls support that reading.

The paper reports repository-level exclusion, a common timeout, retained-store ablation, and a complementary manually rated multi-repository track. It does not report repeated-run variance, matched total compute, comparable failure stores for competing agents, experience-acquisition cost, a related-repository leakage audit, or a longitudinal test isolating telemetry-driven improvement of the improver itself. This is evidence for useful retained experience, not yet for a cost-accounted, continuously improving learning mechanism.

*‡ denotes a value read from a rendered PDF figure, not our estimate of statistical significance. Provenance and the unresolved appendix count wording are in SOURCE.md.*
