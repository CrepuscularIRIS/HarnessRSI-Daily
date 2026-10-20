# SOURCE — ManimAgent: Self-Evolving Multimodal Agents for Visual Education

Read from: arXiv 2606.30296v2
Paper figures shown: none

The exact-version PDF was freshly downloaded and read in full, including all appendices (31 pages). Title and author order were checked against the PDF. Figure reuse was permitted by the worker assignment, but no paper artwork is used: the method diagram and numerical chart are our drawings. Code link: https://github.com/jwj1342/Paper2Manim (not run or used as factual evidence).

## Table/page provenance

| Content | PDF source |
|---|---|
| Title and ordered authors | Title block, p1 |
| Persistent artifact, retrieval, rendering and stop/delivery rules | §§3.1–3.3, pp4–6; Appendix B p14; Algorithm 1 p30 |
| Positive/negative write gates; local distillation; no eviction | §3.3 p6; Table 10 p23; Appendix L p25 |
| Headline and every ablation value | Table 1 p7 (checked visually against rendered page); §§4.2–4.4 pp8–9 |
| Main endpoint GPT-5.5, weak judge Step-3.7-Flash | §4.2 p8; Table 13 p29 |
| 39 building / 33 probe / 40 exploratory / 25 human tasks; 195 quarantined holdout | §4.1 p7; Table 4 p18; Appendices F/G pp16–18 |
| Blind raters, vote-level Pass@1, quality aggregation and planned sample | Appendix H pp17–20; Table 7 p22 |
| Binary-vote agreement: Fleiss’ κ −0.01, 153 videos, 59.4% complete agreement; Likert ICCs: visual design 0.24, key-claim coverage 0.00, visual robustness 0.10, animation flow 0.33, first-attempt usability −0.09, on 23 videos with three raters | Appendix H p20 |
| VLM–human correlation −0.17 / −0.20, Cohen κ −0.07, paired 37-video analysis | §4.5 p10; Appendix I pp21–22; Table 9 p22 |
| Matching and shuffled content controls | §4.2 pp8–9; Appendix B p14; Appendix E p16; Appendix L p25 |
| Approximate tokens and per-task render wall time | Appendix P pp28–29; Table 12 p29 (visually checked) |
| Per-render limits: 180 s wall, 120 s CPU, 4 GB RAM | Appendix B p14 |
| Fixed defaults; no stated selection split or baseline tuning budget | Appendix P/Table 13 pp28–29, with full-text check |
| Validator / field isolation / cutoff check | Appendices F/G pp16–18; Table 14 p29 |
| No quantitative transfer on cross-test; inspected retrieval types only | §4.1 p7; Appendix N pp26–27 |
| Scope, reward sensitivity, memory scale/rot | Limitations pp10–11 |

## ‡ numbers

None. No computed numerical differences are used. Chart values are transcribed directly from Table 1; its scale uses integer ticks. Model version numbers are identifiers, not performance calculations.

## Interpretation and reporting caveats

- Human Pass@1 is a proportion of individual usability votes (Appendix H), not a majority-vote task success rate. First-attempt human videos and final best-of-N delivery are separate parts of the protocol. Reflection rounds aggregate across the task pipeline; the per-scene retry limits are not a contradiction with larger task-level round counts.
- Table 1 gives point estimates and mean metrics, not run distributions. No repeated-run counts, seed variance, confidence intervals, headline seed, or checkpoint selection rule are stated. We do not infer single-run evaluation merely from that absence.
- The protocol plans 25 tasks across seven headline conditions, 175 videos, three ratings per video. Appendix H also allows two or three ratings; agreement is reported on 153 three-rater videos, ICC on 23 videos, and Figure 7 has different per-condition rater-score counts. The PDF does not provide a complete final denominator ledger for each Table 1 row. We flag the reporting scope as unresolved, do not assert that percentages are wrong, and do not infer every cell contains 75 votes. The 37-video VLM agreement analysis explicitly filters missing or failed renders; this must not be generalized into an unreported headline filtering rule.
- EMB@0, VLM-only and the no-memory ablation are distinct Table 1 conditions, with different numbers; none is silently substituted for another. Manim-code RAG is the strongest static baseline on both human metrics (doc-only RAG is lower). Top-1's near-full quality is a separate ablation. No Table 1 text/table result discrepancy is alleged.
- The main quality judge is blind human raters; the internal reviewer/write gate is GPT-5.5, also the text-agent family. The paper explicitly acknowledges self-confirming reward preferences and poor VLM–human agreement. The weak-reviewer control does not remove that risk. Binary-vote agreement and continuous-quality reliability are distinct: Appendix H p20 reports low ICCs for all five Likert dimensions (visual design 0.24, key-claim coverage 0.00, visual robustness 0.10, animation flow 0.33, first-attempt usability −0.09), on only 23 videos with three raters. Rater agreement is itself poor, and differences have no confidence intervals.
- Paper-level separation and read-only probes support retained-memory evaluation. Defaults match manifests, but their selection split and tuning/search budgets are not disclosed. We do not infer test-set tuning. Cross-test is qualitative, not a quantitative transfer benchmark, and no task/domain breakdown establishes whether gains are concentrated.
- Matching concerns retrieval/prompt and reflection budgets, not total work: RAG is static, not granted the self-grown memory mechanism. Table 12 token counts are estimates rather than tracked consumption; lower reflection rounds coexist with higher render wall time. Cumulative memory-construction cost and dollar expenditure are unreported.
- Local before/after score gates are not independent randomized demonstrations that a distilled lesson caused improvement. “Hard” pitfalls refer to prompt roles. No formal enforcement guarantee is claimed.
- Table 14 gives a limited cutoff-stratification diagnostic; we report its actual strata, not proof of absent pretraining leakage. Table 14 (p29) and Appendix P (p28) print quality Δ +0.17, which does not reconcile with the displayed 3.56 and 3.40 stratum values. There is no other condition/model row in Table 14 resolving this discrepancy. We retain the stratum values and do not use the printed delta; no computed delta or explanation of its cause is introduced.

## Judgment notes

Repository score: 67, band ★★, evidence level retained (research/scores.jsonl). Latest matching judgment is research/judgments/b02.jsonl: budget_matched partial, variance unclear, cross_task no, optimizer_cost yes, retained_ablation yes, improver_comparison unclear, leakage_guard untested.

The full PDF describes more leakage safeguards than the read-only flag quoted in that judgment: paper-overlap and field-isolation validation (Appendix F) and pre/post-cutoff stratification (Table 14). The blogs and poster include these and do not say that there was no leakage check. These safeguards do not establish absence of all contamination. The optimizer_cost quote concerns estimated per-task resources, not cumulative cost of building the retained artifact; we make that distinction explicit. No score or judgment file was changed. The retained classification is supported; no higher evidence-level claim is made.
