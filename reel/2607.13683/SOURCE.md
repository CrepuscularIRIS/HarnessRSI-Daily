# SOURCE — HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution

Read from: arXiv 2607.13683v2
Paper figures shown: none

Figure reuse is forbidden for this task. All poster diagrams, bars and tables are original renderings of the method and reported values; no paper image is embedded. Code: announced upon acceptance, no URL. Authors copied in PDF order: Xiaotian Luo, Dizhan Xue, Fengxingyu Wang, Chuanrui Hu, Yafeng Deng; EverMind AI / Shanda Group.

The exact PDF was downloaded afresh, independently of earlier leftovers, and read in full in layout and plain extraction. It has nine pages, ending in references, with no appendix. PDF result pages 5–7 were also rendered and inspected, including Figure 4 and Tables 1–3.

## Table/page provenance

| Material | Source |
|---|---|
| Frozen weights; mutable surface; train/test roles | §3.1, p3 |
| Empty initial bank; component/pathology cells; training-generated harnesses | §3.2, pp3–4 |
| Highest-training-utility parent, cell competition, train-selected final winner | Eqs. 7–9 and §3.2, p4 |
| Ledger validity; activation; positive paired task gain; z ≥ 1.96; full-train evaluation | §3.3, pp4–5, Eqs. 10–15 |
| Default task/evolver models, three attempts per task | §4.1, pp5 |
| Seven-domain vanilla/evolved values and reported gains | Table 1, p6 |
| Six credited test comparisons; single train-selected winner assessment; no evolution-seed aggregate | §§4.2, 4.4, pp5–6 |
| SWE-bench split 101/26, z=0.78; AppWorld n=168, z=6.44 | §§4.2, 4.4, p5 |
| GEPA/DGM protocol, rollout range and ratio, significance versus vanilla | §4.3, p5; Figures 3–4, pp6–7 |
| Baseline SWE-bench result 56.4; HB52.6, vanilla47.4 | Figure 4, p7, visually checked |
| Gate ablation: full45.4, zero false elites,10.0 rounds; no significance ±0.0,+2 elites, >20 (cap); no confirm+significance −1.6,+3, >20 (cap), as reported; stopping criterion unmet | Table 3 and §4.7, p7 |
| Dominant pathologies, rejected AppWorld patch, qualitative token-budget controls | §§4.5–4.6, p6 |
| Cross-model numerical patch comparisons | Table 2 and §4.6, pp6–7 |
| GDPval test-hindsight alternative11.5 vs selected9.2 | §4.7, p7 |
| Score66,★★,retained, code announced | research/scores.jsonl; latest judgment research/judgments/b20.jsonl |

## ‡ numbers

- **56.4‡ is not computed:** read directly from DGM's SWE-bench bar label in Figure 4, p7, verified on the rendered PDF page. Marked because figure-label numbers may not occur in arXiv HTML text. It is used in both blogs and the poster.
- No computed numerical gains are used. All gains, including SWE-bench +5.1, are copied as reported, not recalculated from rounded endpoints. Table 3 deltas are relative to full HarnessBank, not absolute Pass@1.

## Scope and unresolved details

- Six significant domains plus preliminary SWE-bench are explicitly separated in §4.2; the earlier sentence saying every gain clears the bar is read with that following exception, not called a numerical inconsistency.
- Proposer resources remain unresolved: §4.1 names Claude Opus 4.8 as evolver, while §4.3 says the baselines use Qwen3.6-27B as both task agent and proposer. The complete PDF supplies no specific clarification of HarnessBank's proposer in that comparison. We do not speculate about a cause or assert equal proposer resources.
- Baseline budgets are comparable rollout counts (780–2,310, within2.1×), not equal compute. Separate tuning-search budgets and optimizer token/dollar/wall-clock costs are not supplied. Same paired evaluation ruler does not mean same internal selection mechanism.
- No isolated gene-bank ablation, equal-sized/equally curated semantic bank for baselines, independent evolution-seed aggregates, hyperparameter-selection split, or near-duplicate/related-task contamination audit is reported in the supplied PDF. This is an absence of reported evidence, not a claim that these were impossible or never performed.
- Training-generated bank entries are not held-out data; the paper states test tasks are withheld. No cross-benchmark bank transfer is reported. Model transfer tests use AppWorld and Omni-MATH, Qwen27B/397B and Gemini3 Flash.
- Figure 4's significance statements concern each method against vanilla, not paired method-to-method superiority.
- Bank ablation evidence cannot be inferred from cross-cell recombination examples alone. The significance-only ablation has unchanged deployed score; the reported archive/stopping outcomes favor the full protocol, but their causal interpretation is qualified by an unresolved protocol inconsistency: Eq. 11 (§3.3, p5) requires an activation beacon to fire at least once and rejects never-triggered candidates, while §4.7 (p7), discussing the `w/o 2σ` row, says an admitted elite is inert and its beacon never fires. The complete PDF does not clarify how that happens with the activation gate retained. The significance-gate change is therefore not cleanly isolated by the written protocol; no implementation cause is inferred.
- Table 3 (p7) reports `>20 (cap)` for both modified variants and defines this as the stopping rule never being met. §4.7 says they stop at the cap, but does not independently specify its exact numeric value; §3.2 (p4) gives only symbolic R and P. We preserve the table notation and do not assert that the cap equals 20 rounds.
- The PDF has no seed identifier or independent-evolution-run summary for Table1. K=3 is attempts per task, not three independent optimization runs. Paired p/z evidence does not quantify optimization-run variance.

## Judgment notes

The score66,★★,retained and all judgment files are left unchanged. Three qualifications to latest batch b20 are necessary:

1. `variance: yes` is supported by paired task-level significance, not by repeated evolution seeds or across-run standard deviations/confidence intervals.
2. `budget_matched: yes` rests on approximate rollout comparability, up to2.1×; exact compute parity and proposer parity are not established.
3. `retained_ablation: unclear` misses the explicit Table3 gate ablation. It reports archive and stopping effects, but the unexplained admission of an inert elite despite the stated activation gate prevents clean isolation of the significance-gate change. It does not isolate bank retention and does not by itself justify upgrading to improver.
