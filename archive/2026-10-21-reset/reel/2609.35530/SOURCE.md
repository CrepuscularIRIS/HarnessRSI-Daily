# Source and claim audit

Read from: arXiv 2609.35530v1
Paper figures shown: none

Exact PDF downloaded from https://arxiv.org/pdf/2609.35530v1 to the worker's paper.pdf. The full 31-page paper, including appendices A–J, was read through both plain and layout text extraction; title page and key Tables 1/2 and 7/8/9 were visually checked. The qualitative comparisons in Figures 11–16 on pp29–31 were also visually reviewed. Extraction emitted font warnings but succeeded. No abstract page, blog, repository implementation or other external research source was used. The announced code URL is a link only; its code was not run or used as evidence.

Title: AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation.
Authors (PDF order): Yuta Oshima, Ku Onoda, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta. First two equal contribution. PDF attaches University of Tokyo affiliation markers to the first five, not Furuta.

## Provenance

| Claim / visual | PDF evidence |
|---|---|
| Executable harness optimization; model roles | §§3–4, pp3–4; implementation details Appendix A, p17. Runtime GPT-5.5 is pinned gpt-5.5-2026-04-23; proposer is the paper's Claude Fable 5.1, unrelated to local model overlays. |
| Original search diagram | §4 pp3–4, Algorithm 1 p18, Appendices D/E pp19–21. Beam 2, four proposals per iteration, five iterations; train feedback history includes rejects; validation selects only new candidates. Final best member of final beam, not necessarily all-time best. |
| Split / selection | §6.1 p5: 229 four-reference tasks split into 48 train, 48 validation, 133 test. Hyperparameters specified without reported tuning-selection procedure. Validation gates survival; held-out test does not gate final adoption. |
| Original runtime diagram | §5 pp4–5; Appendix F, Figure 8, pp22–23. Two diverse grounded drafts, hard-failure-first and both-order selection, complaints/revision draft, three images; fallbacks described in blogs. |
| Main chart / category scope | Table 1 p6: 4B 5.72→7.37; per-type 5.95→7.27,6.11→7.87,5.50→7.64,5.34→6.70. Mean over five criteria and then equal mean over four task types. Not pooled task-weighted mean. Proprietary local/global exceptions and 9B object result from same table. |
| Runtime controls and search methods | Table 6 p24, not figure labels: Best-of-3 6.01/3 images; IPR 7.02/3; Idea2Img 6.42/3 and7.12/9; GEMS5.37/2.7; Meta6.23/4.2; Greedy6.67/5; AutoRef7.37/3. Vanilla5.72/1. |
| Baseline access / implementation | Appendix G pp23–24: same generator/reasoner for human-designed harnesses; Best-of-3 sees references/candidates; GEMS verifier adapted to see references; IPR reimplemented and planner sees references/current output; Idea2Img original feedback rounds vs one-round matched version. Default API settings Appendix A. Meta-Harness same budget stated, five iterations, full history and same-task feedback/ranking; Greedy split separation with one parent. Exact total token/GPU cost parity and separate baseline tuning budgets not provided. |
| Ablation chart | Tables 4 p9 and9 p25:7.37 full;7.01 no diversity;6.99 no complaint revision;6.93 no failure-aware selector;6.91 grounding only;6.15 selection only;5.72 generator only. First four and selection-only use3 images, grounding/generator only1. Removed generation replaced by resampling; selector replaced by Best-of-N. Small object complaint effect7.24vs7.27 and local7.01vs7.87 Table9. Not a pure grounding leave-one-out. |
| Transfer / failure | Table1 p6,Table2 p6,Tables7/8 p25: unchanged harness across models/reference counts;96tasks each3/5reference setting.4B6.94→7.76 and5.19→6.36;9B4ref5.78→7.10;Qwen4ref4.44→5.69;Qwen5ref1.89→1.87. Appendix I p27 prose:87/96(91%)Qwen5ref tasks all three drafts hard-fail. |
| OmniContext / concentration | Table3 p8 and Tables10/11 p26:120tasks,15 each of8types,externalGPT-4.1 evaluator,geometric PF/SC per-type then equal-type mean.4B8.30→8.85;singlechar9.22→8.94;multichar+obj8.68→8.59;sceneobj7.47→8.89;scenechar9.18→9.28. ProprietaryGPT9.41. Best-of-3 also wins some individual cells, e.g.singlechar9.26vs8.94; no claim AutoRef wins every cell. |
| Human assessment | §6.6 p9 prose:four raters,50tasks/comparison;Nano win46%/loss40%;4B70%/17%. No figure-only tie percentages transcribed. |
| Uncertainty / cost / leakage caveats | Full methods/results/appendix search: no per-cell run/seed count, repeated-search variance or CI; cannot establish within-noise significance or call tables single-run. No total optimization dollars,tokens,GPU-hours,wallclock or generation count. RTX6000Ada stated;20new candidates not a cost measurement. Isolated proposer and split-separation comparison are protocol evidence, not a reference/content duplication audit. No actual overlap asserted. |
| Qualitative selection | Appendix J p28: examples selected from largest score gaps, not random. No examples reused. |

## Numerical policy

No ‡ numbers are used: all empirical decimals come directly from PDF tables or prose, not calculations or chart reads. Chart axes use integer ticks, not newly computed decimal statistics. Model version strings are identifiers, not measurements. No paper figure labels are used as numerical sources. Both poster charts and diagrams are original redrawings of table values and method descriptions. Thus figure reuse was permitted but not exercised; no paper-image credits are needed.

## Judgment notes

Published record: research/scores.jsonl, arXiv2609.35530, score65,band★★,evidence level retained; latest matching judgment found in research/judgments/b20.jsonl. No registry file was changed.

- Stored retained_ablation=unclear understates the full paper: Tables4/9 explicitly ablate the retained harness components on held-out tests. The grounding experiment is grounding-only rather than pure leave-one-out.
- budget_matched=yes is supported by the stated same-search-budget comparison and matched image-count runtime rows. It must not be read as audited equal tokens,dollars,GPU time or baseline tuning access. Meta-Harness's shortened protocol is disclosed in the blogs.
- leakage_guard=tested reflects separated proposal/selection feedback, isolated access and the comparison against same-task Meta-Harness. It is not evidence of a direct reference-image/content-overlap contamination audit. Validation survivor identities/code still inform future proposals; validation is adaptively reused.
- variance and optimizer_cost remain unclear. The absence of seed/run counts is not evidence that each result is a single run.
- No numerical inconsistency was identified after checking table variants. Validation7.32 and test7.37 are different splits, not conflicting measurements; headline values use test tables. Published score and evidence label are preserved.

## Render and validation

2400×1440 house-style poster built with the existing shared poster helper; local CSS raises captions to22px. Original method diagrams and table-backed bars only. The final PNG was visually inspected and the local card-overflow check and research/check_reel.py were run before delivery. File-size and font/geometry measurements are recorded in the worker validation output, not treated as paper measurements.
