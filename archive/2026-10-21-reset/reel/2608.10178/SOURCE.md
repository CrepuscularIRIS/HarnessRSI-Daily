# SOURCE — One Recipe, Many Harnesses

Read from: arXiv 2608.10178v1
Paper figures shown: none

Exact PDF title: **One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models**.
Authors in PDF order: Siqi Yang, Qianlan Yang, Yu-Xiong Wang, Saurabh Pujar, Martin Hirzel (University of Illinois Urbana-Champaign; IBM).
Downloaded https://arxiv.org/pdf/2608.10178v1 directly to the worker directory and read all 20 pages, including Appendices A–I, using both plain and layout text. Visually checked PDF pages 7, 10, 12, 14 and 17. No external summary or code repository was used as evidence, and no paper code was run.

Figure reuse was forbidden for this task. The poster method diagram and data chart are our own drawings; no PDF crops, paper figures or paper-page images are included in the deliverables. There is a paper QR only; no verified code URL was supplied. The abstract's generic code-availability sentence is not treated as a verified repository link.

## Claim and number provenance

| Material | PDF pages / source | Scope |
|---|---|---|
| Exact title, author order, affiliations | p1 title block | Full title retained in poster |
| Frozen weights, editable P/W/M/T, common seed, diagnostic advisory routing | pp3–4 §3; pp9–10 A.1–A.5 | Main grid uses same underlying model as task policy/analyzer/driver |
| Memory 12 × 400; smoke validation; maximum two changed components | pp9–10 A.1/A.3 | Memory has instance-token admission guard, not demonstrated exhaustive leakage audit |
| Selection s−2.0ρ; tolerance 0.12; patience two; catastrophic 0.25; seed fallback | p10 A.4 | Selection-set guarantee, not test non-regression; no pseudocode algorithm is supplied |
| C++/Haiku 10.0→62.5→72.5→72.5; second-round checkpoint shipped; incomplete predicted fixes | pp10–12 A.6–A.8 | One confirmed named fix and four missed from A.7; hooks are nudges, not hard submission gates |
| Stated 20 evolution / 50 held-out, random disjoint splits, mean_solve@3 | p4 §4.1; p13 B.1–B.2; pp19–20 I.1/Table 9 | Repeated rollouts ≠ repeated searches; not pass-at-least-once; reported rollout totals do not reconcile, so actual per-cell coverage is unverifiable |
| Baseline access, budgets 80 steps/$1.5, three rounds | p13 B.2–B.3 | Static minimal seed and released mini-SWE-agent; neither is granted outer-loop search; no baseline tuning-budget table |
| Every main-grid score in the blogs, selected Haiku chart in poster | p14 Table 3 | Seed / mini / TRIAGE; full table transcribed in both blogs |
| Uncertainty and paired z | p14 Table 4, C.2 | Resample/rollout uncertainty, not independent evolution seeds; Table 4 calls it resample SD and text writes σ=s/√n; we do not relabel it as evolution SD or supply a CI; mini uncertainty absent there |
| One evolution run per cell | p7 conclusion; p19 Appendix H | Explicit statement, not inferred from missing error bars |
| Recovered-instance defects 256/88%/81%/7%; per-model recovery | p15 Table 6, D.1 | Post-hoc detected signatures, not proof of a universal capability ceiling; benchmark protocol contributes |
| Pooled correlation 0.81 vs within-GPT 0.12 | pp15–16 D.2 | Both values in prose, not read off a graph |
| Shared concept/marker overlap 0.55/0.57 vs 0.12/0.14 | p6 §4.4; p14 C.3 | Prose values; content analysis restricted to positive-gain non-Python Haiku/DeepSeek cells; automated tagging/lexical limitations in p13 B.5 |
| Universal artifact, retention definition, JS1.13/Go1.08/Java0.68/C++0.65/TS0.48 | p6 §4.5; p10 A.5; p18 G.3 | All five quoted ratios also occur in prose, so no figure-label marks required; evaluated with DeepSeek-V4-Flash only (§4.5 p6); all-language evolved memories distilled to ten rules; includes target-language evolution experience |
| Full-harness transfer, 18/20 positive, 14/20 below native, mean0.63 | pp6–7 §4.6 | Counts and mean explicitly reported in prose, not newly computed; DeepSeek only; unchanged artifact; no per-pair variance/CI |
| C++→TS1.50, Java→TS1.40, Go→TS1.30; JS→C++1.32 and JS→TS−2.30 | p7 §4.6 prose | These values are explicitly in prose; native point estimate not an absolute ceiling |
| Go→JS−0.09‡ | p7 Figure 7 label | Figure-label transcription, visually verified; only marked figure-label value used |
| Planted-fact failure 78.3→76.1 / 76.1→71.7 | p16 D.3 | Authors describe changes as within noise; not evidence of new-fact discovery |
| Driver ablation 18.5 / 34.2 / 33.3 / 35.6 | p16 Table 7, E.1 | Go/DeepSeek task policy, k=3; no table variance/CI; narrow sensitivity study |
| Tool probe seed11.1, evolved22.2 vs9.3; loss12.9pp | pp16–17 E.2/Table 8 | Selected duplicate-code task family, not Table 3's main-grid C++ row; no table variance/CI |
| Missing controls and protocol dependence | pp18–19 H | Separate routing/contract/gate/two-axis ablations, other optimizer comparisons, stronger static scaffold, matched-total-compute extra-rollout baseline not reported |
| Cost $256 meta separate from $3,667 rollout; aggregate category costs | pp19–20 I, Table 9 | Main grid$1,415, mini$357, transfer$1,088, distillation$615; not per-harness actual-spend matching; donor/search work not free |
| Score64, band★★, retained; original judgments | research/scores.jsonl and research/judgments/b12.jsonl | Repository assessment, not paper-authored result |

## ‡ notes

- **−0.09‡** (Go-source → JavaScript-target retention): read directly from the cell label in Figure 7, PDF p7, verified against the rendered page. Not an arithmetic result. Negative retention means the transferred point estimate is below the target's minimal seed, since its native gain is positive.
- No other figure-only numerical values or new decimal arithmetic are used. The 18/20 and 14/20 transfer counts are explicitly stated by the paper; no new win count is computed from Table 3.

## Interpretation and unresolved reporting details

- **Evaluation-accounting discrepancy (independently rechecked).** §4.1 p4 and B.1–B.2 p13 state eight languages, three models, 50 held-out instances per language and three independent rollouts per instance. Appendix I.1 p19 attributes 2,820 held-out rollouts to scoring three arms at k=3 on every held-out instance across the grid. Table 9 p20 repeats 2,820 and separately lists 1,606 mini-SWE-agent rollouts. After checking those separate categories, these counts still do not reconcile with the stated complete-grid protocol. Both blogs and poster panel 2 now label the protocol as stated, retain the reported scores, and disclose that executed per-cell evaluation coverage cannot be verified from the PDF. No cause is inferred; no newly computed rollout totals are retained in the deliverables.
- **Universal model scope.** §4.5 p6 explicitly deploys the universal artifact unchanged on DeepSeek's held-out set. All universal retention ratios quoted here are evaluated with DeepSeek-V4-Flash only, not across all three models. The all-language pool includes target-language evolution experience and is not leave-one-language-out. This restriction now appears in both blogs and poster panel 4, separately from full-harness transplant scope.
- **Manual-baseline endpoints on poster.** Rechecked every DeepSeek row in Table 3 p14: TRIAGE / mini is TypeScript 63.5 / 65.4, Rust 35.2 / 44.4, Python 66.1 / 71.4, and C 65.0 / 65.0. Poster panel 3 now quantifies these comparisons rather than merely naming the exceptions. No derived differences are used.

- **No speculation about execution.** A.2 (p9) explicitly says `wrong_fix` is deliberately not routed; the advisory routing table (p10 Table 2) explicitly includes `wrong_fix`. We disclose this unresolved prose/table detail without guessing what ran. There is no initialization/selection pseudocode to reconcile; the common minimal seed is stated consistently. The numerical selection penalty is not a mathematical guarantee of zero regression, and tolerance/seed fallback apply to evolution data only.
- **Broad content range.** After checking both models and every language in Table 5 (p14), Haiku JavaScript is 18%, below the prose statement that every evolved harness falls in the 20–40% band (pp6,14). We quote the table exception neutrally, not an explanation for it.
- **Python uncertainty.** Main text calls Python a null region. Table 4 DeepSeek/Python has paired −7.1±4.2 and z=−1.69, which has a single star under its stated |z|≥1.64 threshold. The blogs and poster retain that qualification rather than turning all Python cells into exact ties or asserting a strong regression.
- **Baseline gains are not uniform.** Both model axes and all Table 3 rows were checked. Poster chart deliberately shows selected Haiku cells (including Python); its caption labels the selection, and neighboring text gives DeepSeek exceptions and GPT's null. Blogs include the entire main table. No universal outperformance claim is made.
- **Other small reporting differences.** Table 3's printed deltas sometimes differ from the rounded difference of its own endpoints and from Table 4; we use endpoints for plots and Table 4's printed paired deltas when discussing uncertainty, without recomputing or diagnosing causes. We do not promote these rounding-scale differences to a major inconsistency claim.
- **Transfer safeguards and limits.** B.1 promises evolution/test disjointness within each language, never using test to propose/score/select edits, and common target test sets across variants. A.1 rejects instance-specific memory tokens. We found no cross-language source-evolution/target-test instance or repository-overlap audit; do not infer that leakage occurred. The universal memory includes all-language evolution material, including target-language evolution data; not leave-one-language-out. All transplants are unchanged, not target re-evolved. Native per-cell searches reuse the recipe but re-derive content. B.2's uniform per-rollout ceilings do not establish equal realized per-harness or end-to-end budgets.
- **Hyperparameters.** The evolution split selects the final checkpoint. A.4/B.2 report fixed defaults, but the paper does not state the split used to select those defaults or their tuning budget. B.3 says the manual baseline uses its released configuration. No further baseline tuning budget is reported.
- **Ablation and significance scope.** Table 7/8 averages have no reported table variance/CI; §4.5 describes universal JS/Go as statistically indistinguishable but supplies no numerical interval there. Table 4 compares seed vs evolved, not mini vs evolved. Appendix H explicitly excludes independent evolution replication. No isolated routing/contract/gate causal result is claimed.

## Judgment notes

The latest matching record is **b12.jsonl**, with score **64**, band **★★**, evidence level **retained** in scores.jsonl. No scores or judgments were edited.

1. `optimizer_cost: unclear` is incomplete relative to the full exact-version appendix: Appendix I explicitly separates metered meta-model and rollout spend. Both blogs and the poster report that cost evidence, while preserving the existing score.
2. `variance: no` is appropriate for **independent evolution-run variance**, but must not imply no uncertainty evidence: Table 4 supplies rollout/resample uncertainty. Both are stated.
3. `leakage_guard: unclear` needs qualification: explicit within-language split separation and an instance-token memory filter are present. A tested cross-language overlap audit is not reported. We distinguish safeguards from empirical auditing and do not assert contamination.
4. Retained-level evidence remains an appropriately scoped label here: held-out harness gains exist, but the core routing/contract/selection components are evaluated as a bundle rather than independently isolated.
