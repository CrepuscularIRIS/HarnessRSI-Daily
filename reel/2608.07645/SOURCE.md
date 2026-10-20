# SOURCE — Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution

Read from: arXiv 2608.07645v1
Paper figures shown: none

Exact version downloaded directly from https://arxiv.org/pdf/2608.07645v1 to the work directory. Read the full 56-page PDF, including appendices and code listings, with layout/plain text; visually checked the title block and Tables 1–3 and 7. The PDF title includes **via Comparative Evolution**, beyond the shortened task title. Authors in PDF order: Changzhi Liu, Yilun Liu, Sikuan Yan, Volker Tresp, Yunpu Ma. First two equal contribution.

Figure reuse is forbidden for this task. All poster diagrams and charts are our own schematic/data redraws, not copies, crops or traced paper figures. No code from the paper or repository was run. Code URL comes from PDF p1. Repository contents were not used as evidence.

## Provenance

| Claim or numbers | PDF source |
|---|---|
| Source/scaffold self-editing, fixed model weights, archived evidence, CM/RM/CH, no file splicing | §§2–3, pp3–5; §5.2, pp8–9 |
| Node-level and clade-level Beta/Thompson sampling | §2, p3; §3.2, pp4–5 |
| Validity admission before evaluation, finite loop, no explicit immediate parent-beating gate | Algorithm 1, Appendix A.1, p21 |
| CH target when one or both agents fail | §3.2, p5; Appendix A.2, pp21–22 |
| Initial/HGM/MGM 68.3/73.3/78.3; 50.8/77.9/93.2; benchmark average 59.6/75.6/85.8; 200 evaluations/24 expansions; times 93.02/96.11 and 44.20/40.14 h on eight H100 GPUs | Table 1, p8; §5.1, pp7–8 |
| Same ancestor/model/subsets/operation counts granted to HGM; HGM has archive and adaptive sampling but CM only | §§2–3, pp3–5; §5.1, pp7–8; Appendix E.2, pp28–29 |
| Frozen cross-benchmark initial/HGM/MGM 16.7/13.3/26.7 and 41.7/43.3/55.0; average 29.2/28.3/40.9 | Table 2 and §5.2, pp8–9 |
| Frozen SWE scaffold model transfer: Flash 50.0/60.0/66.7; Pro 45.0/70.0/75.0; two-DeepSeek average 47.5/65.0/70.8 | Table 3 and §5.2, p9 |
| Polyglot frozen scaffold transferred to DeepSeek-Pro, full benchmark 96.89% | §5.2, p9 (text, not read off a figure; intro rounds to 96.9) |
| Polyglot-60 full/w/o RM/w/o CH 93.2/79.7/74.6, initial50.8, time40.14/43.01/39.95h,200 evaluations,two workers | §5.3 and Table 4, p10 |
| 100 simulation seeds,95% CIs,equal edit costs, rho1.0 null, oracle optimum and conditional assumptions | §4, pp5–7; Appendix B, pp22–24; Table 5,p24 |
| Compute configuration and model inference modes | Appendix C.1,p24 |
| Failed-pool weight1.0;CM/RM/CH weights0.10/0.45/0.45;minimum two tasks | Table 6,Appendix C.2,p25 |
| Sixty tasks per transfer target, selected through ChatGPT with language constraints; exact task lists | Appendix D,pp25–28 |
| Full Polyglot210/22593.3%;C++25/26,Go36/39,Java43/47,JavaScript46/49,Python33/34,Rust27/30 | Appendix E.1 prose,p28 (not figure-label reads) |
| Best-belief selection rather than raw sparse maximum | §5.1,p7; Appendix E.2,pp28–29 (exact final formula not provided) |
| Coder-Next initial33.3,HGM40.0,MGM41.7; Qwen3.6 initial68.3,HGM73.3,MGM78.3 | Table 7,p31 |
| Unresolved61.7 prose reference | Appendix F.2,p30 versus Tables1/7,pp8/31 |
| Three successive inherited Polyglot edits, bounded five-attempt task verification | Appendix H.1,p34; listing pp36–45 |
| SWE code-path tracing and diff filtering, including docstring/autodoc-specific utility | Appendix H.2,p35;listing pp46–56 |
| Private-test access restriction | §5,p7 |
| Limited seed/sweep breadth,history dependence,small subsets; safety isolation and public-data/pretraining overlap | Limitations/Ethical Considerations,pp11–12 |

## ‡ numbers (computed by us)

- **15.3‡ percentage points** = 93.2 − 77.9, MGM minus HGM on Polyglot-60, Table1. Used in both blogs and poster.
- **1.7‡ percentage points** = 41.7 − 40.0, MGM minus HGM with Qwen3-Coder-Next-80B-A3B, Table7. Used in both blogs. Poster shows the original pair rather than the computed delta.
- The SWE margin5.0 is explicitly reported in §5.2,p9; it is not an unmarked new calculation.
- No values were taken solely from figure labels; no figure-read ‡ values are used.

### ‡ PDF-table transcriptions (not computed)

- **79.7‡%** (without RM), **74.6‡%** (without CH), **43.01‡ h** (without RM), and **39.95‡ h** (without CH) are verbatim Table 4 values, PDF p10, not arithmetic or figure estimates. All four were independently checked against the rendered page (`table4.png` in the work directory). They occur in the downloaded PDF but are absent from the repository gate's cached paper text. The marks explicitly document this extraction gap; no true number was deleted or changed to satisfy the gate. The poster uses the same verified table values.

## Scope and unresolved reporting

- Main tables report best-belief scaffold point scores. No empirical per-cell run count, seed SD or CI is supplied. We do **not** assert one run: the paper's lack of count is not proof of a single run. Simulation uncertainty is kept separate. Benchmark/model averages are not labeled seed means.
- Cross-model transfer freezes the scaffold and replaces the backbone, but does not hold the entire execution configuration fixed. Appendix C.1, p24 specifies thinking-enabled Qwen versus non-thinking DeepSeek-V4, with different sampling configurations. Inference budgets are not demonstrated to be matched across models, including full-Polyglot transfer. This does not invalidate the initial/HGM/MGM comparisons within each target model.
- Operation counts are matched for HGM/MGM, not exact token totals. Figure6's qualitative token-cost description is not converted into a numerical total. No total dollar-cost accounting is provided. The model-transfer results do not supply an end-to-end donor-evolution-inclusive cost table.
- Hyperparameter defaults are given, but the selection split, sweep procedure and baseline tuning budgets are not. Under Eq17,beta_fail1.0 yields equal weight for failed/nonfailed unseen tasks: this is explicitly our reading, not an ablation result.
- No immediate score-based admission rule is described: Algorithm1's validity check admits a child with no recorded outcomes. Outcome-driven sampling and final choice are separate. The paper does not fully define the validity check or exact best-belief final selector.
- Main evolution subsets are not independent test tasks. Full Polyglot contains the source subset and is evaluated after freezing; cross-model Verified transfer uses the same tasks. Cross-benchmark transfer uses new benchmark subsets. Denial of private tests is not equivalent to denying all visible repository tests (AppendixH explicitly reads/runs them). No dedicated empirical contamination audit was found across the full PDF. Public/pretraining overlap is acknowledged.
- Tables1/7 give78.3 for Qwen3.6 MGM Verified-60; F.2 p30 says61.7. Checked other model blocks in Tables3/7,benchmark-transfer Table2,ablation Table4,full Polyglot E.1,and all text occurrences. No alternative row resolves61.7. We flag the reference neutrally, use the table value, and do not speculate about its cause. This caveat appears on the poster and both blogs.
- Full Polyglot counts demonstrate broad absolute success, not a per-language comparative gain: corresponding HGM counts are not supplied. Main relative advantage is larger on Polyglot; Coder-Next margin is small with no uncertainty.
- AppendixH shows successive retained edits, but no empirical long-horizon growth/saturation curve is supplied. A conditional surrogate convergence result is not a guarantee for coding systems. Oracle optimum is diagnostic only.
- No Red Queen Gödel Machine title/arXiv2606.26294 citation or comparison found anywhere in the PDF. Explicit shared historical machinery is with DGM/HGM; HGM is Huxley Gödel Machine. No claims copied from the separate Red Queen poster.

## Judgment notes

Existing score record: **65,★★,retained**; latest matching judgment **research/judgments/b18.jsonl**. No judgment files modified. Full-PDF reading supports its partial-held-out qualification,matched-operation budget,cross-task transfer,cost reporting and uncertain empirical variance. Its improver-comparison yes describes designer-provided operator comparisons; it should not be read as evidence that MGM autonomously rewrites its outer search/selection policy. Simulation has variance, empirical tables do not report it. Leakage guard remains an access-policy statement rather than a tested contamination audit. These are scope clarifications, not a score recalculation.

## Rendering and delivery checks

Poster uses a 2400×1800 house-style canvas and the shared poster library, with original method schematic and chart. Height was increased to retain the controls while meeting the task's 2400px-width readability floors; the shared library was not edited. The generic poster skill's real-figure requirement is overridden by this brief's explicit no-reuse instruction; no venue-specific conference format is claimed. No external reviewer/subagent was spawned, as forbidden by the brief. After the independent review, QR captions were enlarged to 22px and chart benchmark headings to 23.36px effective size, verified from the final PDF at 2400px raster width. Body/captions are at least 22px; method text is at least 24.16px, and chart series/value labels remain at least 18.52px. Final PNG visually inspected: no clipping/collisions; rerender and measured card-overflow count both zero. Review finding 1 was independently verified against Appendix C.1, p24 and applied to both blogs, the transfer caption and this source note; finding 2 was independently confirmed by PDF text-size measurements and corrected. No review items rejected. Repository gate result recorded in final worker report.
