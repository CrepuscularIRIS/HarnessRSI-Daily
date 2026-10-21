# SOURCE — Huxley-Gödel Machine

Read from: arXiv 2510.21614v3
Paper figures shown: none

Exact PDF title: **Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine**.

Authors, in PDF title-block order: Wenyi Wang, Piotr Piękos, Li Nanbo, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jürgen Schmidhuber. The first two contributed equally. Affiliation: King Abdullah University of Science and Technology (KAUST).

PDF downloaded directly from https://arxiv.org/pdf/2510.21614v3 to `/home/lingxufeng/reel-work/2510.21614/paper.pdf`; title-page stamp: 29 October 2025. All 30 pages read, including Appendix F code listings; layout and plain text extracted. Title page, transfer tables and algorithm page visually inspected. No web abstract, code repository or other paper is used as evidence. Code URL is reproduced from the PDF, not executed or audited.

Figure reuse is prohibited for this assignment. All poster visuals are our own schematic and charts drawn from table values; no paper figure, logo or illustration is included. Work and generator: `/home/lingxufeng/reel-work/2510.21614/`.

## Claim and number provenance

| Claim / content | PDF location | Scope |
|---|---|---|
| Agent code self-modifies into tree descendants | Sections 2–3, pp3–7; Appendix C.1 p18; Appendix F pp21–30 | No model-weight training described. Changes include agent loop and test/error handling. Protected-file list and controller/evaluator mutability boundary not specified. |
| Clade success/failure estimator; separate parent and evaluation sampling | Section 3.3 pp6–7; Algorithm 1 p17 | Operational clade includes root; evaluation uses individual counts, expansion uses clade counts. |
| Archive admission and terminal selection | Section 2 p3; Section 3.3 p7; Algorithm 1 p17 | Child added before task evaluation; no shown parent-beating admission gate. End selection is called posterior-percentile best-belief. See notation caveat below. |
| Initialization, asynchronous bias | Appendix B p17 | Prose describes initial root expansion five times with each parallel process; algorithm only shows root initialization. Bias from easy tasks completing early barely observed after more than 50 evaluations. No statistical bias test given. |
| Defaults and stopping | Section 4 p7; Appendix C.1 p18 | τ=B/b, α=0.6, ε=1; all HGM experiments asynchronous. One-hour comparison execution cap, five-hour full-scale modification/evaluation caps; finite global budget. No hyperparameter-selection split reported. |
| Method comparison accuracy and hours | Table 2 p9; Section 4.2 pp8–9 | SWE initial40%, SICA50.0%, DGM53.3%, HGM56.7%; DGM1231h, HGM517h, SICA infinite-loop entry. Polyglot initial20.3%, SICA25.4%/572h, DGM27.1%/2385h, HGM30.5%/347h. Up to800 task evaluations. SICA SWE stops progressing after360 evaluations. Not held-out. |
| Models, common resources | Section 4.2 p8; Appendix C pp18; Table 5 p20 | All methods same DGM-derived ancestor/backbone pair/evaluation ceiling. SWE GPT-5 expansion + GPT-5-mini evaluation; Polyglot Qwen3-Coder-480B-A35B-Instruct expansion (mixed int4/int8) + Qwen3-Coder-30B-A3B-Instruct evaluation. |
| Baseline policy access | Table 5 p20 | SICA entire-history greedy modification and newest-child full evaluation; DGM performance/child-count parent selection and progressive newest-child evaluation. Neither receives HGM policy. No isolated CMP or asynchronous ablation found. |
| CMP diagnostic | Table 1 / Section 4.1 p8; Appendix D p19 | Weighted Pearson SWE SICA0.444,DGM0.285,HGM0.778; Polyglot0.274,0.383,0.626. Unweighted HGM0.512,0.873. HGM predictor excludes root and winning-child subtree to prevent target reuse. Post-hoc tree diagnostic, not oracle competitor or prospective test. |
| Full-scale optimization | Section 4.3.1 p9; C.1 p18 | Full500-task Verified,8000 evaluations; stronger bash-only ancestor53.2% to61.4%. Optimization data, not test data. |
| Lite split and same-backbone comparison | Section 4.3.2 pp9–10; Table 3 p10 | Standard300 tasks,93 overlap with Verified removed for filtered. Initial34.8/44.0, local SWE-agent+GPT-5-mini39.6/47.6,HGM40.1/49.0 (filtered/standard). Artifact selected on Verified; no Lite reoptimization described. |
| Model transfer and human-level scope | Table 4 and Section 4.3.2 p10; footnote1 p7 | HGM artifact with GPT-5:47.8/57; SWE-agent leading checked design48.3/56.7; paper explicitly says filtered HGM one task behind. Reference design SWE-agent+Claude4Sonnet. Leaderboard as of24October2025; comparison is with human-engineered agents, not human task solvers. |
| Leakage guards | Section 4 p7; Section 4.1 p8; Section 4.3.2 pp9–10; Appendix D p19 | Polyglot private test cases/results denied; Lite overlap filter; CMP diagnostic exclusions. No general contamination audit or explicit SWE self-modifier access firewall reported. |
| Compute cost | Table 2 p9; C.2 p18 | Allocated CPU-hours, not claimed to be comprehensive LLM compute or elapsed time. Approximately$5000 across experiments/all three methods, not HGM-only. No full8000-evaluation run breakdown. |
| Uncertainty, missing controls | Tables1–4 pp8–10; appendices read in full | No run/seed counts, SD,SE,CI; no isolated policy/component ablation; no baseline tuning budgets, tuning split or sweep. CPU worker count, decoding temperature and interaction-length cap numerics not specified. Do not infer single-run. |
| Relationship to other Gödel-machine posters | Related works/references pp11–14 | Direct comparators are DGM and SICA. No Red Queen/Mendel comparison or citation in this version; no claims imported from later papers. |

## ‡ numbers and figure-label reads

None. No derived decimal, computed task count or figure-label number is used in the blogs or poster. All chart numbers come from Table 2. Poster table values come from Tables 1, 3 and 4. The phrase “one task behind” on filtered Lite is stated by the paper itself (p10), not computed by us. Integer chart axis ticks are graphical scale labels, not empirical claims.

## Async implementation detail and unresolved specification / text-table issues

- **Final selection:** p7 describes a posterior percentile but calls `I` the regularized incomplete beta function; p7 sets ε=1 and Algorithm 1 repeats the expression. Our explicitly labelled mathematical reading is that a literal Beta CDF at1 gives1 for all proper Beta posteriors, so this does not specify a nontrivial ranking. We neither substitute an inverse CDF nor infer what the code ran. No number in this observation is an empirical result.
- **Async implementation detail (not an unresolved initialization discrepancy):** p7 explicitly says all reported HGM experiments use HGM-Async. Appendix B p17 describes its parallel warm start of five expansions per process to address asynchronous startup bias. This async-specific implementation detail is described separately from the base HGM pseudocode in Algorithm 1; the omission there does not imply competing or unspecified experimental initialization choices.
- **Correlation:** Table 1 unweighted HGM Polyglot value0.873 differs from Section4.1 prose0.8783. Checked all weighted/unweighted, SWE/Polyglot and method rows plus Appendix D; no alternative reported variant resolves it. We use0.873 and flag neutrally, without an explanation of cause.

## Judgment notes

Stored score:63,band★★,evidence level retained (`research/scores.jsonl`). Latest matching judgment:`research/judgments/b18.jsonl` (v3). It marks held_out partial,budget_matched partial,variance unclear,retained_ablation unclear,optimizer_cost yes,improver_comparison yes,leakage_guard untested.

The full PDF adds specificity absent from the judgment's short quotes: a Lite split with Verified-overlapping tasks removed, private-test exclusion for Polyglot, and CMP diagnostic target exclusions. “Untested” must not be paraphrased as “no leakage precautions.” These narrow guards do not establish a general contamination audit. The stored held-out quote concerns optimization on Verified; cleaner retained-generalization evidence is Table3 filtered Lite. Score and evidence level are retained, not silently recomputed; no score or judgment files edited.

The paper's appendix labels patch inspection as recursive meta-improvement, but this is not a controlled demonstration of a faster improving improver. No sustained compounding/saturation characterization, replicated uncertainty or isolated controller ablation was found.
