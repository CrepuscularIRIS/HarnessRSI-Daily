# SEDM: keeping a memory and using it are different decisions

*A Reel interpretation of **SEDM: Selective Self-Evolving Distributed Memory for Agents**, [arXiv 2509.09498v4](https://arxiv.org/abs/2509.09498v4). HarnessRSI score 65, ★★, evidence level retained. No code link supplied; the paper promises a release.*

## What the system changes about itself

SEDM changes the **shared memory** available to subsequent agents: which experiences enter it, their retrieval weights and tiers, which duplicates are merged, and which patterns are distilled or retired. The task agent is gpt-4o-mini. This is not an agent rewriting its own source code. The recipient-side Calibrated Memory Gating (CMG) component **does train model weights**: Qwen3-4B with LoRA learns whether to show retrieved memories to the task agent. The memory-retention loop and this separately trained gate should not be conflated.

## The loop, and the keep/reject rule

1. Package an episode as a Self-Contained Execution Context (SCEC): task input, output, summaries of tool calls, random seeds and configuration hashes. Extract a candidate memory.
2. Replay tasks with and without that candidate. Admit it if reward gain minus latency and token penalties clears a threshold. **Tables 1–3 use the original configuration, which tests a memory on its own source task.** The authors explicitly warn that this may overestimate utility.
3. The stricter LoCoMo pipeline instead tests each candidate on three similar tasks from a separate admission conversation, with three runs per arm. Its threshold is zero and cost penalties are zero: non-harmful ties can enter. It first rejects memories from unsolved source tasks and candidates containing a tested task's reference answer. Rejected candidates retain audit records, not retrieval eligibility.
4. A controller ranks by relevance and measured utility; periodically and at run end it updates weights, promotes/demotes between short-term, episodic and long-term tiers, merges near-duplicates, distills repeated patterns, isolates harmful items and decays unused ones. Entity abstraction produces a general form alongside the specific memory.
5. For a new question, CMG reads the question and retrieved memory set, predicts success under USE and SKIP, and injects the set only if the calibrated probability gain exceeds a memory-length cost penalty. Training uses paired outcomes, **including ties**, rather than only which action won.

**What is distributed?** Episodes from different agents feed a logically shared memory. SCECs can be replayed on independent workers, returning aggregated statistics, integrity hashes and version stamps. The paper describes merging memory content in the shared controller, but not a replica-consistency protocol, a turn-by-turn synchronization schedule, or measured network/sync cost. In both CMG evaluations, the memory is frozen before evaluation; this is not a test of continuously synchronizing, co-evolving agents.

## Headline results, with the protocols kept separate

**Original retention study, without CMG (Tables 1–3).** LoCoMo open-domain F1 is **47.5 vs 32.4** for G-Memory, the strongest baseline in that column; the paper reports a 15.1-point gain. But this is not an across-the-board LoCoMo win. FEVER accuracy is **66 vs 62** for G-Memory and 57 without memory; HotpotQA exact match is **39 vs 38** and 34. Prompt totals are 2.47M vs 3.62M on FEVER and 3.88M vs 4.63M on HotpotQA, reported as 32% and 16% savings. These tables do not specify repeated-run means, seeds or confidence intervals, and were not rerun with held-out admission.

**Controlled recipient gate, HotpotQA (Table 4).** On 489 held-out questions, seed 42, validation-selected CMG gives **0.329 success [0.288, 0.372]**, compared with always-use **0.333 [0.292, 0.376]** and no-memory **0.249 [0.213, 0.286]**. CMG uses memory on 69% of questions, with **3,047 vs 3,736** agent input tokens: 18% fewer. This supports a quality–cost trade-off, not a statistically established accuracy win over always-use. Success here means token F1 ≥ 0.5, **not** the exact-match metric above.

**Held-out admission plus CMG, LoCoMo (Table 5).** With admission-only memory, success is **0.556** for CMG, **0.539** for always-use and **0.544** for no-memory; input tokens are 2,263 vs 2,790 for always-use, a reported 19% saving. With controller-managed memory, the corresponding success rates are **0.546 / 0.518 / 0.534**, with 1,915 vs 2,781 tokens, a 31% saving. CMG rows are means over three gate-training seeds. These are 193 questions from **one test conversation**; the authors say individual differences are within its noise. Success is SBERT similarity ≥ 0.7. The two memories and no-memory anchors come from independent runs, so their rows are not a clean paired controller ablation.

## Controls that decide what the gain means

- **Retention ablation with a memory baseline (Table 2).** FEVER progresses from G-Memory 62 to admission 64 to admission-plus-controller 66. HotpotQA progresses from 38 to 37 to 39: admission alone is worse. G-Memory has a comparable memory budget on these two tasks. This does not establish equal total execution/optimization cost. LoCoMo baselines partly come from prior work and may have different memory budgets; their tuning budgets and the split used to choose original-study defaults are not reported.
- **Same memories and executions for gate comparisons (Table 4, Appendix B).** All policies are scored on the same paired agent runs, and learned gates share the backbone and training recipe. Similarity and winner-label gates always inject and score 0.333. CoT scores 0.262 with 3.09 s gate latency vs CMG's 0.24 s, but it is a **zero-shot reproduction**, not an original trained checkpoint; GPU load also affects timing. Oracle is an upper-bound diagnostic, not a deployable baseline.
- **Selection and seeds matter (Table 6).** Gate checkpoints minimize validation loss; the cost price and similarity threshold are validation-selected. Temperatures use a separate calibration split. At fixed price zero, calibrated CMG averages **0.326 ± 0.003**, versus raw **0.324 ± 0.017**, over three seeds. But allowing each seed its own validation-selected price gives **0.318 ± 0.015**. Table 4's 0.329 is seed 42, not the multi-seed mean. Other controlled-study gates use only seed 42; their full hyperparameter-search budgets are not given.
- **Transfer exists, abstraction's contribution is not isolated (Table 3).** FEVER-built memory reaches 41 HotpotQA EM vs 39 for in-domain memory. LoCoMo-built memory reaches 34, equal to no memory. All transfer runs use diffusion; there is no diffusion-off control. Their overall LoCoMo F1 values must not be compared directly with Table 1's per-type scores.

## Memory contents, leakage boundaries and cost

The controlled HotpotQA study splits the development set into memory construction and gate training (2,962 questions each), validation and calibration (496 each), and test (489). Each memory contains a construction question, its verified answer and **gold supporting sentences**, retrieved as the five nearest episodes. A hashed manifest and refusal check enforce the construction split. The authors call the gold-evidence construction optimistic. Memories can share entities or facts with later questions; there is no reported entity-disjoint/near-relative audit. Both memory actions also share a frozen tool corpus drawn from all development paragraphs: ordinary retrieval evidence is not the same as copying test episodes into the memory bank.

For full-pipeline LoCoMo, conversation 0 supplies memories, 1 supplies admission tasks, 3–7 supply gate training, 8 validation, 9 calibration and 2 testing. Thus admission is separate from final testing, and answer-containment filters are reported. These safeguards are stronger than the original source-task admission; they do not retroactively validate Tables 1–3.

Paired-data collection costs about **24.7M input and 1.3M output tokens**, about **US$4.5** (Appendix E). Learned gates train for three epochs on one A40. The paper does not provide a complete cost ledger for memory construction, admission replays, controller merging, synchronization and GPU gate training. Per-question agent input savings are not end-to-end lifecycle savings.

## Where gains are absent or narrow

- LoCoMo's strongest gain is concentrated in **open-domain** questions. Single-hop is 51.7 vs G-Memory 53.5; multi-hop 33.5 vs 34.6; temporal 12.1 vs A-Mem 45.9; adversarial 12.1 vs the LoCoMo baseline 69.2 (Table 1).
- Always injecting held-out SEDM memories does not improve LoCoMo success: 0.539 vs 0.544 for admission-only, and 0.518 vs 0.534 with the controller (Table 5). Gating recovers observed value, but one conversation and overlapping uncertainty limit the conclusion.
- Controlled HotpotQA accuracy is comparable to always-use, not higher. Bootstrap intervals resample questions; they are not independent memory-building trials or evidence of cross-model robustness. Original retention/transfer tables have no reported variance; Table 5 gives three-seed averages without rowwise confidence intervals.
- The strategy-note pilot's seed-42 CMG matches no-memory at 0.275, but another seed gives 0.255 (Table 9). Recovery is not universal. Only one task-agent model and one gate backbone are tested.

## Our read

HarnessRSI **65 · ★★ · retained**. The evidence supports execution-gated memory retention and a recipient gate that can reduce task-agent context cost. The paper reports retention ablations, cross-domain memory transfer, partial memory-budget matching, gate seed variance, split/hash checks and answer-containment filters. It does not establish full-compute matching, robust original-table uncertainty, continuously evolving distributed operation or full memory-build/sync cost.

The stored judgment labels held-out and budget evidence partial and leakage protection untested. The full PDF does describe concrete leakage safeguards; we report those in SOURCE.md rather than interpreting that label as “no checks.” The strongest held-out result also involves a separately trained gate over frozen memories, not demonstrated recursive improvement of the improver itself.
