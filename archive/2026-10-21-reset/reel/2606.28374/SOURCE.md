# SOURCE — Recursive Self-Evolving Agents via Held-Out Selection

Read from: arXiv 2606.28374v1
Paper figures shown: none

All method graphics, bars and tables were drawn by us from the PDF's algorithm and tabular results. Figure reuse was allowed by the assignment, but no paper figure was reused. Authors, in PDF order: Michael Nguyen; Quoc Nguyen; Paul Vuong (Monash University Malaysia).

## Read and provenance

The exact-version PDF was re-downloaded from https://arxiv.org/pdf/2606.28374v1 for this run. All 15 pages were read in fresh plain and layout extracts, including references and Appendices A/B. The title page and tables on PDF pp7–9 were also checked visually. No earlier draft/facts, abstract webpage or repository supplied paper claims.

| Claims / visuals | PDF provenance |
|---|---|
| Three-layer state; frozen model; rewrite signal and full keep/reject rule | §4, pp4–5; Algorithm 1, p5 |
| Backbones, task sizes, development pool and shuffled tool-use splits | §5, pp5–6 |
| Native baseline selection rules | Table 1, p4; §5, p6 |
| Headline five-seed success and 95% CIs; retry results | Table 2, p7; paired tests §6, p6 |
| Concentration across task families; clean regression | Table 3, p7; §6, p6; example state Appendix A, p14 |
| GAIA / τ-bench / WebShop rows, counts and strongest baselines | Table 4, p8; §7, p7 |
| Layer ablation, 54 tasks × three seeds | Table 5, p9; §8, p7; temperature and general multi-seed description pp7,15 |
| Selection ablation: in-sample vs test, not gated-vs-ungated 33-point gain | Table 6, p9; §8, p8 |
| Cost: 190 meta+selection calls for τ-bench, short inference prefix | §9, pp8–9 |
| One split seed on tool-use, web noise, validation-only guarantee | §7, p7; §10, p9; Appendix B, pp14–15 |
| Scope and absent reporting checked throughout full PDF | §§5,8–10; Appendices A/B, pp14–15 |

## ‡ numbers

None. No computed decimal numbers are used in either blog or the poster. Poster bars use Table 2 numbers, and the displayed CI half-widths are reported 95% CIs, not standard deviations. The poster does not add derived deltas or unreported error bars. Model names are identifiers, not calculated measurements.

## Scope / unresolved wording

- The abstract, §6 and captions call RSEA strongest/best single-pass; explicitly single-pass Tables 2 and 4 instead show Dynamic Cheatsheet 70.7 vs RSEA 69.3, and §6 reports their p=0.45 comparison. Checked all single-pass and retry rows and Tables 1–6; no alternative variant resolves that single-pass ranking wording. We report the table ranking and mark the wording discrepancy unresolved; no explanation of its cause is inferred.
- Main Table 2 is a five-seed mean, not one best checkpoint/seed. RSEA's paired p=0.015 vs ReAct and broad marginal 95% CI are both reported. Retry's highest mean is not a significant win over the three reported retry comparators at their listed p-values.
- Tables 5 and 6 are separate ablation protocols, not interchangeable anchors for Table 2. Table 5 has 54 tasks × three seeds, no cell-wise uncertainty. §8 describes multi-seed decoding for ablations, but Table 6 does not identify exact task/seed counts and reports no uncertainty. Its 100.0→66.7 is in-sample-to-test; strict-gate test 67.3 is the relevant controlled comparator.
- Validation is reused for adoption: working-state acceptance is non-regression (>= current); frozen best update is strict (> historical best). It is not untouched test data. An empty fallback guarantees validation non-regression under this selection rule, not arbitrary test-draw safety. Tool-use splits are disjoint slices of a seed-shuffled test pool, not a reported distribution-shift benchmark.
- Backbone/scaffold are shared within benchmark; ALFWorld uses Qwen2.5-7B-Instruct, the other benchmarks Qwen3-30B-A3B-Instruct. The paper reports benchmark-specific evolved states, not frozen-state transplantation. Exact episode reset details, evolve/val sizes, full rollout/retry counts and the split used to select hyperparameters/defaults are not supplied in the PDF. Best-state selection uses val; this is not evidence that all defaults were tuned on val.
- Equal rollout budgets and decoding are asserted; total meta-call/context costs differ. No baseline tuning budgets or per-method monetary/token/wall-time accounting is supplied. Some baselines have native validation selection; no control gives every baseline RSEA's strict rule. DC collapse cannot be attributed solely to gate removal from this cross-method comparison.
- §7 says WebShop's frozen state is empty, yet Table 4 separately reports 0.437 vs ReAct 0.429. We quote these as separate evaluations without inferring why they differ. GAIA two evaluations concern the same frozen states; only one shuffled-split seed is used on tool-use benchmarks. Table 4 gives no uncertainty and only two GAIA methods.
- Table 3 clean: 80.0 ReAct, 73.5 RSEA, 79.4 retry. We do not turn the prose's recovery wording into a claim that retry beats ReAct. No family task counts are supplied, so aggregate reconciliation is not independently possible.

## Judgment notes

Local source: research/scores.jsonl (67, ★★, retained; code announced, URL null) and the latest matching judgment, research/judgments/b14.jsonl. No judgment/score file was edited.

The retained level is consistent with test evaluation of a frozen state selected elsewhere. The stored one-line description emphasizes strict commitment; our explanation additionally distinguishes lateral working-state acceptance from strict frozen-best selection.

The stored leakage_guard=tested is backed by the selection-set ablation. Our reading is narrower than a full contamination audit: it tests selecting on evolve versus a separate validation set, not overlap of learned artifacts with all hidden test answers. The PDF describes disjoint splits but reports no separate contamination audit. We preserve the recorded score and level and explain this distinction in both blogs. cross_task and improver_comparison remain unestablished: multiple benchmarks alone do not demonstrate transfer of the same artifact or evolution of the improvement operator itself.
