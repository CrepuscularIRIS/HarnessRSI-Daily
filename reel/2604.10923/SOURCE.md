# SOURCE — Mem²Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation

Read from: arXiv 2604.10923v1
Paper figures shown: none

Exact version downloaded directly from https://arxiv.org/pdf/2604.10923v1 into the fresh work directory; all 47 PDF pages, including appendix prompts and case-study listings, were read. Paper/code listings were treated as data, never executed. Figure reuse is disallowed for this task. Every diagram, bar and table in the poster is our original rendering of the paper's method or tabulated values; no paper figure or crop is embedded.

## Title and authors

The title rendered on PDF p1 is **Mem²Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation**. The listing/PDF metadata writes `Mem$^2$Evolve`; the PDF renders the 2 as a superscript with no inter-word space. We use Unicode `Mem²Evolve`, not the spaced `Mem2 Evolve` produced by PDF text extraction. The full title is preserved in both SOURCE and the poster (not shortened to its subtitle).

Authors, in PDF order: Zihao Cheng, Zeming Liu, Yingyu Shan, Xinyi Wang, Xiangrong Zhu, Yunpu Ma, Hongru Wang, Yuhang Guo, Wei Lin, Yunhong Wang. Affiliations: Beihang University; Beijing Institute of Technology; Independent Researcher; Munich Center for Machine Learning; University of Edinburgh. Zeming Liu is marked corresponding author.

## Table/page provenance

| Public content | Source in the exact PDF |
|---|---|
| Dual-memory objects, tools/experts versus implementation/strategy lessons | §3.1, pp3–4; Appendix A.4–A.6, pp17–19 |
| Reuse/create, retrieval threshold, top-1 expert and top-K tools | §3.2, pp4–5; A.5, pp17–19, equations 12–13 |
| Judge inputs, success and critique, ground-truth unavailable assumption | §3.3.1 and footnote 3, p5; judge template C.7, pp28–30 |
| Asset admission, synthesized tests, repair until validation passes, experience append | §3.3.2–3.3.3, p5, equations 8–11; C.8–C.10, pp30–33 |
| Main eight-benchmark averages and all strongest per-column baselines | Table 2, p6; §4.2, pp6–7 |
| Full and four ablation averages | Table 3, p7; Table 6, p22 |
| Per-task ablations and concentration of gains | Table 6, p22 |
| First-pass validity and improvement-iteration averages | Table 4 and §5.2, pp7–8 |
| Subset/remainder same-task initialization, 25%‡/50%‡ legend labels | §5.3, Figure 3, PDF p8; both integer percentages transcribed from the legend and visually verified, not computed |
| GAIA memory reused on seven target benchmarks; comparison with 25% in-domain memory | §5.4, Figure 4, p8; visual checked; only qualitative result used |
| Baseline access, Alita's Promptist/Experience Pool, OpenAlita implementation note | §4.1, p6; §4.2, p7; B.1 pp20–21, footnote 8 |
| Full benchmark test sizes and heterogeneous metrics | Table 5, p21; B.2, pp21–22 |
| Sandbox restriction and deployment limits | Limitations, p9 |
| Task context/outcomes and full implementation retained in memory templates | C.8–C.10, pp30–33 |

## Numerical and protocol notes

- **‡ marks figure-read initialization percentages.** 25%‡ and 50%‡ are transcribed from the initialization legend of Figure 3, PDF p8; visually verified against the exact PDF, not computed estimates. All displayed decimal values come directly from Tables 2–4 or 6; no figure-only decimal values are used. GAIA aggregation and point-unit comments are our arithmetic observations, but introduce no new numerical result.
- Table 2 averages are the paper's benchmark-level aggregates, not a pooled percentage of all tasks. Its full-system eight-column mean rounds to 70.24. Appendix B.2 explicitly distinguishes QA exact match, environment success rate and TravelPlanner's average of five delivery/constraint metrics despite the generic Pass@1 caption. We call these reported scores rather than eight identical Pass@1 metrics.
- **GAIA aggregation unresolved:** the full-system Total satisfies (88.68 + 82.56 + 57.69) / 3 = 76.31, while Alita's displayed 81.13 / 75.58 / 46.15 do not average to its 72.73 Total. We checked all Table 2 GAIA rows: Direct, CoT, ReAct, DyLAN, EvoAgent, AFLOW, DSPy, AgentVerse, AutoAgens and Mem²Evolve Totals match the equal-level mean within rounding; imported DeepResearch, Alita and SwarmAgentic do not. Neither Table 6 nor the initialized-memory variants supplies a definition resolving the aggregation rule. We retain the printed totals and flag the cross-method comparability as unresolved, without hypothesizing a cause or changing a result. We do not infer any denominator from percentage rounding.
- The paper's 6.46%, 11.80% and 18.53% headline comparisons equal subtraction of Table 2's 63.78 / 58.44 / 51.71 from 70.24; they are point differences. CoT, not Direct or ReAct, is the naive comparator for 18.53. The lower Direct score does not make this a contradiction: the stronger naive baseline resolves the wording.
- Full Table 2 baseline rows were checked per column, not just the overall strongest framework. HotpotQA ties AFLOW; Direct is strongest on 2Wiki; SwarmAgentic is strongest on TravelPlanner. OpenAI DeepResearch is reported only on GAIA and explicitly imported. ToolMaker is discussed as a baseline but has no Table 2 result row; no superiority claim against an unreported ToolMaker row is made.
- The main table, ablations and Table 4 contain no seed/run counts, SDs or CIs. No seed or checkpoint can be identified. We do not infer single-run experiments or interpret small differences as statistically established wins.
- Table 5's test sizes are full main-experiment sizes, not the subset/remainder sizes of §5.3. The paper specifies random sampling for the two QA datasets. It does not give memory-initialization item IDs, group separation, exact remaining counts, or an explicit freeze of memory updates during evaluation; cross-task GAIA memory is an initialization, not a verified frozen artifact test.
- Numeric retrieval δ/K, hyperparameter/default selection split, baseline tuning budgets, resource-matched experiments, accumulation/storage-growth cost and measured token/dollar/wall-clock totals were not found after reading the full PDF and searching its text. Table 4 measures repair iterations, not end-to-end compute. No matched-compute inference is drawn from 'same backbone' or the paper's 'matched conditions' wording.
- The evaluator is stated not to access ground-truth labels during backward evolution. The task/trajectory/outcome are still visible; templates can retain task-specific information. No task-overlap, near-duplicate or web-search contamination audit was found. We describe this as unresolved exposure risk, not demonstrated leakage. An independent regression set for admission is not specified.
- Same-task and GAIA-to-other-task performance results are only plotted; no plotted performance values are transcribed. The Figure 3 initialization legend percentages are the marked exceptions documented above. Source memory comes from one donor benchmark, with no cross-backbone experiment and no equal-budget shared-memory baseline control. The minimal web-search configuration in §4.2 (p7) applies to experience-centric frameworks and Mem²Evolve, not every naive baseline: B.1 (p20) explicitly defines Direct without external tools, does not establish CoT search access, and permits web search for ReAct. Alita is explicitly acknowledged to have experience and tool creation; no claim that it is experience-free or experimentally weakened is made.

## Judgment notes

Stored score: **65**, band **★★**, evidence level **retained**, from `research/scores.jsonl`; latest matching judgment is `research/judgments/b10.jsonl`. It records held_out partial, cross_task yes, retained_ablation yes; variance, budget_matched, optimizer_cost, improver_comparison and leakage_guard unclear. The full PDF supports keeping these conservative evidence labels. No score/judgment file was edited.

**Code metadata limitation:** the stored score includes 10 code points based on the PDF p1 'Code is available' project-page claim, although scores.jsonl has `code_url: null` and the task supplies code none. We preserve the supplied score 65, make no repository-availability or verified-code assertion, and provide only a paper QR. No project page or repository was used as scientific evidence. This is a metadata caveat, not a rescoring.

## Production checks

Poster built with the required existing house-style library and a paper-local script; user/brief requirements for no paper figures, fixed gallery canvas, no subagents and exact deliverable set override the generic poster skill's conference/figure-reuse defaults. Body/caption/method text is at least 22 px at 2400 px canvas width; chart labels at least 18 px. Layout overflow and actual SVG-scaled text sizes are checked in Chromium, and the PNG is visually reviewed. `research/check_reel.py` is run on the final delivery directory; exact outcome is reported with the delivery.
