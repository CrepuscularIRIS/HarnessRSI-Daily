# HarnessBank: keep diverse harness patches, but make them earn their place

*A Reel interpretation of [HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution](https://arxiv.org/abs/2607.13683v2), by Xiaotian Luo, Dizhan Xue, Fengxingyu Wang, Chuanrui Hu and Yafeng Deng (EverMind AI / Shanda Group). HarnessRSI Daily score **66**, ★★, evidence level **retained**. Code is announced upon acceptance; no code link is supplied.*

## What the system changes about itself

HarnessBank edits a frozen model's **prompts, injected knowledge, runtime logic and configuration**, not its weights. An evolver diagnoses execution outcomes, trajectories and evaluation metadata, then proposes new harnesses or recombines earlier mechanisms. The evaluation/bookkeeping/interface kernel is kept immutable (§3).

The **gene bank starts empty**. It contains executable candidate harnesses generated during training, not a preloaded corpus of papers, task solutions or externally curated skills. A cell is keyed by **where** an edit acts and **why** it is proposed: component × hypothesized failure pathology. The pathology is an LLM diagnosis, not ground truth. Entries therefore come from the benchmark's own training tasks; the paper says test tasks are withheld from evolution, but supplies no related-task/near-duplicate contamination audit. It does not report giving baselines an equally sized or equally curated semantic bank.

## The loop, and the keep/reject rule

1. Choose the highest-training-utility harness among vanilla and bank entries (the argmax in Eq. 7).
2. Diagnose its training traces and generate new or recombined candidates.
3. Screen on a random training subset: require a complete **protocol-valid ledger** (repair/retry infrastructure failures), a deterministic **activation beacon** firing at least once, and a **positive paired gain with z ≥ 1.96** against the parent on the same tasks. Each task's score difference averages three attempts. Activation proves execution, not correctness by itself.
4. Evaluate the first candidates that pass on the full training set. Fill an empty cell or replace its incumbent only with higher full-training utility.
5. Stop at the round cap or after consecutive rounds without a cell update. Evaluate the training-selected winner on the sealed test.

The gate uses task scores from the evaluator, not the evolver's assertion that a patch is useful. Bank admission is a training decision; it is not itself evidence of held-out improvement.

## Headline result, as reported

The default task model is **Qwen3.6-27B**; §4.1 names **Claude Opus 4.8** as evolver. Table 1 reports test Pass@1, averaged over **K = 3 attempts per task**, for one train-selected winner per domain, not a mean across independent evolution runs.

| Test domain | Vanilla | HarnessBank | Reported gain, percentage points |
|---|---:|---:|---:|
| Terminal-Bench-2 | 36.1 | 45.4 | +9.3 |
| LiveCode | 58.1 | 71.8 | +13.7 |
| Omni-MATH | 54.3 | 66.0 | +11.7 |
| BrowseComp+ | 16.9 | 30.8 | +13.9 |
| GDPval | 43.7 | 52.9 | +9.2 |
| AppWorld | 41.3 | 56.7 | +15.4 |
| SWE-bench | 47.4 | 52.6 | +5.1 |

We preserve the paper's reported gains rather than recomputing rounded endpoints. Six domains clear its paired significance threshold; **SWE-bench does not** (z = 0.78, 26 test tasks, 101 training tasks). AppWorld has the largest reported gain and strongest paired result (z = 6.44, 168 test tasks). The other six gains are not confined to one benchmark, but the mechanisms are concentrated: selective recovery from runaway reasoning and verify-finalize checks recur; thinking-runaway dominates four of the six domains discussed in §4.6. Most headline evidence uses one task model.

## The controls that decide whether the gain is real

- **Held-out selection and uncertainty (§§3–4).** Harnesses and bank elites are selected on training, with test reportedly excluded from all evolution decisions. The six credited gains have reported p-values from below 10⁻⁴ to 0.033. These are paired task-level statistics, **not evolution-seed variance**: no across-run mean/SD/CI or headline seed identifier is supplied. The paper does not specify which split selected hyperparameters/defaults, nor a full split-construction recipe. It reports no separate hyperparameter-tuning budget for the baselines.
- **Baseline search effort (§4.3).** GEPA and DGM share the frozen task model and splits, with the same paired evaluation ruler. Reported budgets are **780–2,310 rollouts**, within **2.1×** per domain: comparable, not exactly matched compute. GEPA outspends HarnessBank on two domains and DGM on one. No complete optimizer token, dollar or wall-clock accounting is given. GEPA remains prompt-only and DGM's internal selection ungated; evaluating them with a paired ruler is not granting them HarnessBank's screening/bank. No equal-bank control is reported.
- **Proposer parity remains unresolved.** §4.1 names Opus as evolver, whereas §4.3 describes the baselines as using Qwen3.6-27B “as task agent and proposer.” After checking the entire PDF, including all model/variant rows, we found no experiment-specific clarification of HarnessBank's proposer for that comparison. We therefore do not claim identical proposer resources.
- **Gate ablation (Table 3, TB2).** Full HarnessBank scores 45.4 with zero false elites and 10.0 rounds. Removing the significance gate changes deployed score by **±0.0**, but adds two false elites and runs to the cap rather than meeting the stopping criterion; removing confirmation plus significance gives **−1.6** and three extra false elites. Both modified rows report **>20 (cap)**, defined as the stopping rule never being met, not an independently specified exact cap of 20 rounds. The table reports no repeated-run variance. These outcomes suggest cleaner archives and earlier stopping more directly than better final accuracy, but **the ablation protocol is internally unclear**: §4.7 says an admitted elite is inert and its activation beacon never fires, whereas Eq. 11 (§3.3) rejects never-triggered candidates. The PDF does not explain how that happens with the activation gate retained, so the significance-gate change is not cleanly isolated by the written protocol. There is no isolated bank-removal or equal-bank ablation.
- **Cross-model controls (Table 2).** The paper combines cold-start evolution on other models with transplantation of existing patches. On Omni-MATH, the 27B stack gives **+11.7** on its source and **+11.0** on the 397B Qwen model, but **−1.5** on Gemini; Gemini's matched raise-reasoning patch gives **+15.3**. On AppWorld, verify-finalize gives **+15.4 / +0.2 / +5.8** on 27B / 397B / Gemini, while submit-verify gives **+1.2 / +13.6 / +13.5**. These are two domains and two model families, not evidence of a universally transferable harness or cross-benchmark bank transfer.

## Where the gain is absent or small

- **SWE-bench is preliminary, not a demonstrated win.** Its +5.1 fails the paired bar. DGM reaches **56.4‡** against HarnessBank's 52.6 (Figure 4); neither has a credited gain over vanilla, so the small test cannot establish superiority. The authors attribute this to small-sample noise; our reading is narrower: the experiment does not distinguish the methods reliably.
- **Removing the gate does not reduce TB2's deployed score** in the significance-only ablation (±0.0). The archive/stopping benefits should not be rewritten as an accuracy gain.
- **Transfer is selective, not simply absent.** The Qwen-to-Qwen math patch transfers, but the same stack harms Gemini (−1.5). On AppWorld the 27B patch gives only +0.2 on 397B. Conversely, Gemini still gains +5.8 from that patch, so mismatched patches are not universally useless.
- **GDPval hindsight is not the headline.** A variant ranked below the winner on training later gets +11.5 on test versus the chosen winner's +9.2 (§4.7). That diagnostic does not make the test-best variant a valid training-selected result.

## Our read

HarnessRSI score **66**, band **★★**, evidence level **retained** (latest judgment: b20). Reports: held-out evaluation, paired task-level uncertainty, comparable rollout budgets, gate ablation and cross-model patch tests. Does not report: independent evolution-seed variance, an isolated bank ablation/equal-bank baseline, a tested contamination audit, hyperparameter-selection protocol or full optimizer cost. The stored judgment's `variance: yes` refers to task-level paired evidence, and `budget_matched: yes` to the comparable rollout comparison; neither should be read as multi-seed robustness or exact compute parity. Table 3 adds a gate ablation despite the record's `retained_ablation: unclear`; we note this without changing the score or evidence level.

**Takeaway:** keeping semantically different patches and screening measured gains is a plausible way to retain useful harness changes. The strongest evidence here is held-out lift; the archive/stopping outcomes are suggestive, but the unexplained inert elite limits causal interpretation of the gate ablation. This is not proof that the bank itself causes the lift, or that every patch generalizes.

*56.4‡ is read from the rendered Figure 4 bar label, not computed; see SOURCE.md.*
