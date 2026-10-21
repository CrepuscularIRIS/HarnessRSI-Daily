# SOURCE — SEDM: Selective Self-Evolving Distributed Memory for Agents

Read from: arXiv 2509.09498v4
Paper figures shown: none

The exact-version PDF was freshly downloaded from https://arxiv.org/pdf/2509.09498v4, independently read in full including Appendices A–I, and extracted in layout/plain forms. Previous partial files were not used as evidence. Title and author order were checked against the PDF title block. Figure reuse is prohibited for this assignment; all poster geometry and bars are original redraws of tabulated numbers, not copies/tracings of paper figures. No paper/repository code was executed. No code URL was supplied; Appendix I promises a release.

## Table/page provenance (PDF page numbers)

| Claims/assets | PDF source | Scope |
|---|---|---|
| Exact title; first three authors Yichen Liu, Anna Min, Yinzhi Wang, followed by et al. on poster | p1 title block | Full author order recorded in work-dir facts.md. |
| Episode/SCEC fields; workers return statistics/hashes/version stamps; A/B score and original vs held-out admission | pp3–4, §3.1–3.2, Eqs 1–3 | Independent jobs are described, not a measured synchronization/consistency system. |
| Shared-memory retrieval, tiers, merge, distill, isolate, decay, abstraction | p4 §3.3–3.4; p11 Appendix A | Described logical controller, not a replica reconciliation algorithm. Controller interval/minimum/conflict threshold and all original defaults are not numerically specified. |
| Gate rule, paired outcomes including ties, Qwen3-4B LoRA, calibration, validation selection | pp4–5 §3.5, Eq6; p12 Appendix B | The task-agent weights are fixed; gate weights train. Never claim whole system is weight-free. |
| Original LoCoMo F1 chart and failure cases | p6 Table 1; p5 §4.1–4.2 | SEDM 51.7/33.5/47.5/12.1/12.1; strongest respective baselines G-Memory 53.5/34.6/32.4, A-Mem 45.9, LoCoMo 69.2. All five types shown, not only favorable open-domain. Figure is newly drawn from numbers. |
| Original FEVER/HotpotQA retention ablation, memory budget, prompt/completion tokens | p6 Table 2 and §4.3; p5 setup | Rows cumulative. G-Memory is a memory-equipped baseline with same memory budget on these tasks; not full compute matched. Table 2 is without CMG and original source-task admission. |
| Transfer successes and zero-gain case | p6 Table 3, §4.4 | FEVER-memory→HotpotQA 41 vs in-domain 39; LoCoMo-memory→HotpotQA 34 equals no memory. LoCoMo overall F1 38.1/38.6/37.6 has a distinct original cross-domain protocol; not directly comparable to per-type Table 1. No diffusion-off ablation. |
| Controlled HotpotQA seed-42 headline, tokens and bootstrap intervals | p8 Table 4; pp6–7 §4.5; pp11–12 Appendix B | 489 held-out questions; success F1 ≥ 0.5, not original-table EM. CMG 0.329 [0.288,0.372], always 0.333 [0.292,0.376], skip 0.249 [0.213,0.286]. 18% saving reported by paper. CIs overlap; no claim of superior accuracy or statistical equivalence. |
| Same-memory gate controls; CoT qualification | p12 Appendix B; p9 Limitations | Common paired runs; winner head/SFT use non-tie labels; CoT is zero-shot on same backbone, not trained original checkpoint. Oracle uses outcomes, only an upper bound. Latencies shared-GPU/load dependent. |
| Three seeds and validation-selected price caveat | p12 Table 6; p13 Table 8 | Fixed λ=0 raw 0.324±0.017, calibrated 0.326±0.003; per-seed validation-selected λ 0.318±0.015. Seed43 selects 0.05. Headline 0.329 is seed42 only. Other controlled learned gates seed42 only. |
| Full-pipeline LoCoMo held-out results | p9 Table 5; p7 §4.6 | All values copied directly. CMG averages three seeds; no rowwise confidence intervals in table. Prose gives admission-only 0.556 ±0.011 but does not explicitly name that dispersion statistic; we do not call it SD. Controller mean0.546 vs always0.518/no0.534. Savings19%/31% stated in paper. Independent banks and anchors; not a paired controller ablation. |
| Strict LoCoMo splits and admission budget | pp11–12 Appendices A/C; p13 Appendix C continuation | Conv0 source,1 admission,3–7 train1089,8 val,9 calibration,2 test193. e=3, k=3 each arm, threshold0, zero admission token/latency penalties, unsolved-source and answer-containment filters. Frozen before gate training. |
| HotpotQA memory and leakage boundaries | pp11–12 Appendix B; pp9–10 Limitations | Disjoint question roles enforced by hash manifest/refusal check. Gold answers/supporting sentences from construction split; shared entities/facts remain possible. All development paragraphs form common tool corpus; this is not a test-episode memory bank. No entity-/near-relative-disjoint audit reported. |
| Collection cost vs unreported lifecycle cost | p13 Appendix E; p12 training recipe | About24.7M input/1.3M output tokens, aboutUS$4.5; three epochs on A40. Agent input savings exclude complete admission/build/merge/sync/GPU-training ledger, which is not supplied. No original baseline hyperparameter-search budget or original-default selection split specified. |
| Strategy-note pilot seed sensitivity | p14 Table 9; p13 Appendix H | CMG seed42/43/44:0.275/0.275/0.255; skip0.275. Do not generalize seed42 recovery to all seeds. |
| Overall limits | p9 Limitations; p14 Appendix I | One task-agent/backbone, frozen memories, one LoCoMo test conversation, no large open-ended agent society evaluation; original Tables1–3 not rerun held-out. |

## ‡ numbers (computed by us)

None. All reported decimals and savings are printed in the PDF. Poster bars encode Table 1 numbers directly; their geometric lengths are only a visual scale, not additional empirical statistics. We avoid unnecessary derived differences/ratios and figure-only values.

## Judgment notes

- Stored score: 65, band ★★, evidence level retained (`research/scores.jsonl`). Latest matching judgment: `research/judgments/b13.jsonl` (no newer matching row found). It records held_out partial, budget_matched partial, optimizer_cost partial, variance yes and leakage_guard untested. No score or judgment file was edited.
- The full PDF reports concrete split/hash enforcement in the controlled HotpotQA study (Appendix B), conversation-separated LoCoMo roles (Appendix C), and a reference-answer-containment rejection rule for held-out admission (§3.2). Thus `leakage_guard: untested` must not be rendered as “no leakage checks.” These are reported safeguards, not a comprehensive audit of overlapping facts/related questions or retroactive protection for source-task Tables1–3.
- The partial held-out label is appropriate to the mixed protocols: original memory tables test candidates on source tasks, while §4.6 builds on one conversation, admits on another and evaluates on a third. Gate selection/calibration are separate from final test. The full memory is frozen during the strongest gate comparisons.
- Retained describes the persistent-memory evidence; CMG separately changes gate weights via LoRA. We make this hybrid nature explicit, rather than presenting the entire method as weight-free or as proven recursive improver improvement.
- No unresolved text-versus-table discrepancy is asserted. Fixed-λ versus validation-selected seed means (Table6), and original per-type versus cross-domain LoCoMo scores (Tables1/3), are distinct rows/protocols, not inconsistencies.

## Render and checks

Poster canvas 2400×1440, house-style Python/HTML renderer. Body and captions are at least22px; original method-step text remains above22px after SVG scaling, chart category labels at least22px and numerical labels above18px. The final PNG is visually inspected for clipping/overlap, and render() must report no OVERFLOW. Delivery gate: `python3 research/check_reel.py reel/2509.09498`.
