# SOURCE — Small but Mighty: Test Suites as Improvement Signals for Self-Evolving Agents

Read from: arXiv 2610.15964v1
Paper figures shown: none

Exact title and author order verified against the PDF title block: Yutong Cheng, Wei Cheng, Wenchao Yu, Dawei Zhou, Haifeng Chen. Affiliations: Virginia Tech; NEC Laboratories America.

PDF downloaded directly from https://arxiv.org/pdf/2610.15964v1 into the worker directory. All 16 pages, including Appendices A–F, were read in layout and plain-text extractions. The title block and Tables 1–2 were also inspected as rendered PDF pages. No abstract page, third-party summary or code repository supplied the scientific claims. No paper/repository code was run.

## Visual provenance

The poster's method flow and horizontal result bars were drawn by us from the method text/Algorithm 1 and Table 1. The tables are our own typesetting of paper numbers. No paper figure, crop or figure-label value is shown, so a figure-reuse credits table is not applicable.

## Claim and number provenance

| Material in poster / blogs | PDF source | Scope |
|---|---|---|
| Exact title, author order, affiliations | p1 title block | Version v1 |
| Python test functions, coverage, mutation score, hv product, maximum-hv/smaller-size tie rule | p2 §3, Definition 1, Eq. 1 | Frozen-backbone suite search, not weight learning |
| Online count correction, UCB, quality-gated size pressure | p3 §4, Eqs. 2–4 | Generation allocation, not harness-rewrite acceptance |
| Archive/grid initialization, failed-measurement calls, overflow niches, written size and passing-subset quality | pp9–10 Appendix A, Algorithm 1 | Seeds precede grid; initial dominance off, then re-file; seed count left as input |
| Parent selection, compression/extension instructions | pp10–13 Appendices C–D, Tables 3–4 | Prompt requirements are not a second measured retention gate |
| Fixtures/stubs/inputs/assertions, source-derived expected values, uncovered lines/surviving mutants/failure marks | pp12–13 Appendix D | The LLM writes the suite from source; existing implementation behavior is intentionally visible |
| 129 modules, 50 calls per module; GPT-5.4 / Claude Opus 4.8 / Gemini 3.1 Pro | p4 §5.1, Table 1 | Table 1 module means; no search-seed mean/variance or per-cell repeat count reported |
| Full hv/size 0.916/38.6, 0.976/29.1, 0.908/36.3 | p4 Table 1 | Model order as above |
| Highest-hv external baseline: OpenEvolve 0.831/51.5; GEPA 0.895/67.2; beam search 0.838/52.6 | p4 Table 1, all baseline rows checked | Excludes the method's ablations; not the smallest baseline per column |
| Cursor/Gemini 37.0 tests; Pynguin 20.4 tests, hv 0.090, 40 modules, 6000 s | p4 Table 1 caption/rows, §5.1 | Pynguin's supported subset is different; not a directly matched full-corpus average |
| Opus ablations full 0.976/29.1; no kernel 0.917/40.8; no UCB 0.960/34.4; random parents 0.934/33.2; no size pressure 0.954/84.6 | p4 Table 1 | Mean hv and mean written size, without uncertainty; direction also checked on GPT/Gemini rows |
| Search/evaluation mutant-fold split, fixed mutant-generation seed | p4 §5.1 | Same modules, not module-disjoint transfer; fold sizes not stated |
| Same-feedback OpenEvolve, harness-feedback Claude Code/Cursor, global three-objective GEPA; other named methods and call matching | p4 §5.1 | No assertion that every baseline gets identical prompt-level annotations; individual wiring for other methods not detailed |
| Kernel spread fixed at holdout median; σ = 0.10, resulting grid ratio ρ = 1.22, grid upper-range parameter γ = 4 | p3 §4; pp9–10 Appendix A | Holdout identity and separation unspecified; no independent tuning split identified |
| Eight modules, 64 revisions/module, 512 generated; 470 verified; 217 divergent/253 equivalent; kappa 0.74 | p5 §5.3/Table 2; pp13–15 Appendix E/Tables 5–6 | Only intent-realizing, human-confirmed revisions enter the denominator; revision generator GPT-5.4 |
| Gate generated once from original; reject tests newly failing after revision | p5 §5.3 | Suite-generation backbone for this gate experiment is not specified; no repeated adoption trajectory reported |
| Pooled DDR 0.253/0.599; FAR 0.000/0.040; mean runtime 5.9/3.5 s | p5 Table 2 | Repository tests / TeSearch, pooled; the prose explicitly also gives 25.3%, 59.9%, 4.0%, 10 false alarms among 253 equivalent edits |
| Module DDR: actions_text 0.040/0.560; content_string 0.057/0.600; agents/default 0.529/0.588; cache_control 0.414 and litellm_model 0.421 for TeSearch | p5 Table 2 | Variation across modules; positive direction everywhere, not uniform margins; no CIs |
| litellm_model FAR 0.080 vs repository 0.000 | p5 Table 2 | Module-specific false alarms, not pooled |
| Tool-call runtime 3.0/3.1; cache 2.9/3.0; config merge 2.9/3.1; content 2.9/2.9 s | p5 Table 2 | Repository / TeSearch; pooled speed advantage is not universal |
| No model calls at gate time | p5 §5.3 | Excludes suite construction/search, whose dollars/tokens/total wall time are not itemized |

## ‡ numbers

None. No derived decimal results, computed table counts, or figure-label readings are used. Percentages in the headline are explicitly printed in §5.3, not conversions invented for the poster. Integer counts 512, 470, 217 and 253 are printed in the paper. The method diagram's numbered steps are editorial organization, not empirical counts.

## Reading boundaries and unresolved items

- Checked every baseline/ablation/model column of Table 1 before selecting the per-model quality leaders. The paper's textual 7.0–8.5 point summary is compatible with those rows; no unresolved text/table discrepancy is asserted.
- The suite writer sees source-derived expected outputs intentionally. Search and evaluation mutants are disjoint folds of the same source module; that is the demonstrated split. It does not establish cross-module generalization or absence of pretraining contamination. No formal revision-pool isolation protocol or contamination audit was found in the appendix. Source access can preserve implementation quirks: this is our interpretation of a regression objective, not a measured leakage result.
- Table 2 is a curated edit-classification experiment, not an end-to-end self-improvement trial. Its generated suite is retained for later edits, but passing this gate is not shown to improve task success. The test-generation backbone and generation budget for that specific experiment are not explicitly stated, and we do not borrow them from Table 1.
- Tests' quality scores use only their passing subsets, while size uses written tests. The paper does not specify a separate final cleanup procedure; we do not infer one.
- Appendix A reports σ = 0.10, the resulting ρ = 1.22, and γ = 4 (pp9–10). Kernel spread is estimated on an unidentified holdout; its identity and evaluation separation, and an independent tuning split for these settings, are not specified. Numerical defaults for η, α, c_e, H and the seed-suite count are not supplied. Baseline tuning budgets are not reported. A fixed mutant-generation seed does not establish search-run replication.
- Table 1 supplies model-level means, no module-level performance breakdown; task/module concentration cannot be verified. Table 2 does expose uneven module gains and runtime exceptions.
- Construction cost and gate execution cost are distinct. Call matching is not evidence of matched total compute; Pynguin's wall-clock allowance is the only explicit wall-clock-matched baseline condition.

## Judgment notes

Source records: `research/scores.jsonl` and latest matching judgment `research/judgments/2026-10-19-a.jsonl` (read only). Stored score **64**, band **★★**, evidence level **retained**. Stored judgments: held_out yes; budget_matched partial; retained_ablation yes; leakage_guard untested; variance, cross_task, optimizer_cost and improver_comparison unclear.

No score or judgment file was changed. Full-paper scope clarification: the retained evidence is a once-generated suite tested on later revisions, with held-out mutants in the separate suite-quality experiment. It is not a longitudinal retained-harness performance gain. The budget judgment remains partial despite explicit matching of LLM-call caps: total compute and tuning parity are not established. Gate latency is reported, but it does not resolve the stored uncertainty about suite-optimizer cost.

## Production verification

House-style 2400×1440 poster, local shared poster library unchanged. Body/captions at least 22 px; method text at least 22 px and chart labels at least 18 px at rendered width, checked through SVG screen-transform measurements. Poster was visually reviewed after rendering and overflow corrections. Panel 2 uses separate label and bar columns; an explicit browser bounding-box check found no text–bar intersections, with minimum effective chart text 20.79 px. No connector crosses step text. The prescribed repository checker is run on the delivery directory; its result is reported in the worker's final response.
