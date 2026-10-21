# SOURCE — EvoDrive: Pareto Evolution for Safety-Critical Autonomous Driving via Self-Improving LLM Agents

Read from: arXiv 2606.03678v2
Paper figures shown: none

The exact version PDF was downloaded directly from https://arxiv.org/pdf/2606.03678v2 to `/home/lingxufeng/reel-work/2606.03678/paper.pdf`. Its title block confirms the full title and author order: Tong Nie, Yuewen Mei, Yihong Tang, Junlin He, Jie Deng, Jian Sun, Wei Ma. The complete 32-page PDF, including appendices and prompt catalog, was read through layout-preserving text; plain text was also extracted. Rendered PDF pages 9, 24, and 26 were inspected to verify the key tables.

Figure reuse is forbidden for this assignment. All poster visuals are our own diagram and chart drawn from the paper's textual definitions and table values. No screenshots, cropped paper figures, or paper figure-label values are shown. No code repository was supplied; the PDF project-page URL is not treated as a released-code claim.

## Table/page provenance

| Material used | PDF source | Scope / interpretation |
|---|---|---|
| Title, authors | p1 title block | Exact title, original author order; affiliations abbreviated on poster |
| Typed generator, critics, validators, archive acceptance, memory | §§2–3, pp2–6; Appendix B, pp14–19 | Parameters, operator graphs, scene-conditioned policies and mechanisms; not ego weights; simulation gates archive promotion |
| Nested world evaluator updates | §3.4 p5; B.7 pp18–19; Algorithm 3 p16 | Earlier simulator labels, deterministic judge, protected simulator labels and archive rules |
| MetaDrive objective | B.5 pp17–18, Eq15; C.1 pp20–21 | Collision attack, weighted feasibility realism, RP=100(1−R); numerical diagnostic weights/tolerances not specified in these definitions |
| CARLA objective | C.2 p21, Eqs22–24 | Attack=CR(1−OS); ARS validity-weighted kinematic/map/interaction/distance consistency with weights 0.40/0.30/0.20/0.10; trace scalar is visualization only |
| Split, proposal and selection protocol | §4 p6; C.1 pp20–21; C.4 p22 | 240 evolution, 160 extra training, 100 protected test; 10 epochs, 20 proposals, rotating 20-scene windows; evolution-pool selected and frozen active/≤3 descendants; R≥0.95 and tolerance0.05 |
| MetaDrive headline / chart | Table1 p6 | All eight PF gains transcribed directly; means over IDM/RL; not best-baseline victories and no headline run count/variance/CI |
| Naturalistic realism validation | Table2 p7 | Eight-family means, maneuver-matched held-out reference, post-evolution only; naturalistic split-half reference also given in blog |
| CARLA headline | Table3 p7; C.2 pp21–22 | Four rounds, eight families × ten routes, balanced family-route selection; attack/ARS and PF gains transcribed; no explicit generator evolution/test disjointness or headline uncertainty |
| Component controls | Table4 p9 and preceding prose p8 | Three independent ADV-BMT/RL evolution runs only; actor-only matches total LLM calls; non-LLM budget equality not stated; ± not defined as SD/SE |
| Evaluator evolution control | Table5 p9 | Same candidate sequence and simulation budget; evolving model uses earlier labels; normalized counts/yields against random; repetition count and ± definition not specified |
| Downstream SAC benefits and exceptions | Table6 p9; C.4 p22 | CARLA original/evolved ChatScene training, route-disjoint evaluation; no run count or CI for this table; CR reductions confined to straight/turning obstacles and right-turn, vehicle-passing worsens, unprotected-left unchanged, Lane Change / Red-light / Crossing remain at zero |
| MetaDrive downstream repeats | Figure7 caption p9; C.4 p22 | Three seeds/random runs applies to this curve experiment only; sources frozen before SAC, training includes evolution scenes; no figure numbers transcribed |
| Cost / model | C.5 p23 | All roles GPT-5.5/Codex/xhigh; representative four-round CARLA run 232 calls, 5.097M cached input, 0.159M output, 13.5h, estimated API $5.88; no whole-system matched cost claim |
| Additional search controls | Tables8–10 pp23–24; C.3 p22 | Attack-only/OpenEvolve same evaluation metrics, no explicit total-budget match; width comparison changes proposal count; no inference of baseline weakening or single runs |
| Policy dependence and zero gains | Table11 p24 | ADV-BMT RL33.4%/IDM4.0%; AT IDM25.6%/RL4.1%; four zero-gain rows named exactly; active and endpoint are distinct columns |
| Family exceptions | Tables12–15 pp25–26 | ChatScene crossing CR0.930→0.870; AdvSim and AT turning ARS0.000; these are weaker attacks / unchanged realism, not downstream safety failures |
| Initialization sensitivity | Table16 p26 | Three starts in each of two ChatScene families, not six repeats of Table3 |
| Cross-policy transfer | Table17 p26 | Frozen SAC-selected scenarios evaluated under SAC and BasicAgent; no broad task/platform transfer or CI claim |
| Safety / sim-to-real limit | §5 p9 | Fixed policies, finite budgets, simulation-only; unseen policies/platforms/real deployment may expose missed failures; hardware-in-loop future |

## ‡ numbers

None. No differences, weighted aggregates, or figure-label numbers are newly calculated. All numerical results displayed are printed in the PDF tables or prose. Poster bars have no generated numeric axis ticks. The plotted values are the literal Table1 PF-Area@3 percentages.

## Baseline access and budget scoping

- MetaDrive CAT, ADV-BMT, AT, SAGE, LLM-Attacker, KING, SEAL and STRIVE are each represented by family-specific interfaces and evolved with the common declared protocol; this is not a claim that every family has identical editable mechanisms. The parents are starting generators, not equal-cost optimized competitors.
- CARLA AdvSim, AT, ChatScene and Human each seed their own archives and undergo four rounds under the same fixed ego and benchmark metrics. Balanced final selection and the three-descendant reporting cap do not establish equal total simulation budget relative to the original parents.
- Actor-only explicitly matches LLM calls. The non-LLM Pareto row does not explicitly state matching compute. Attack-only and OpenEvolve are evaluated in the same setting with the same metrics; their tuning and total simulation budgets are not stated.
- Only Table5 explicitly establishes both the same candidate sequence and simulation budget for its random/static/evolving routing comparison.
- Candidate/default distinction: the evolution pool chooses the MetaDrive active generator and frontier descendants. The paper gives R≥0.95 and tolerance0.05 but no split-based procedure for choosing those defaults. Baseline hyperparameter-tuning budgets are unreported.

## Leakage / overlap and safety scoping

The MetaDrive 100-scene reporting suite is explicitly protected, with candidates frozen before testing. Its downstream training intentionally includes 240 evolution scenes and 160 additional training scenes. CARLA Table6 explicitly uses route-disjoint downstream tests; this statement must not be transferred to generator Table3, whose described evolution/reporting routes could overlap. Protected-resource gates and causal memory retrieval are design safeguards; the paper reports no empirical contamination/leakage audit. No formal deployment-safety guarantee or physical validation is established. Higher attack means a worse outcome for the fixed driver during generator evaluation, whereas lower CR is desired after downstream policy training.

## Judgment notes

Stored score: **65**, band **★★**, evidence level **improver**, in `research/scores.jsonl`. Latest matching judgment located: `research/judgments/b20.jsonl`.

- Its `variance: unclear` omits evidence present in the full PDF: Table4 has three independent ADV-BMT/RL evolution runs; Table16 has three initialization starts for each of two families; MetaDrive Figure7/C.4 report three downstream runs. We report these precisely without claiming headline Tables1/3 or CARLA downstream Table6 have the same replication.
- `cross_task: unclear` remains compatible with Table17's limited cross-policy test: one extra rule-based policy, not a different benchmark/task family.
- Partial budget evidence is retained: Table5 is matched for routing, Table4 actor-only matches calls, but neither establishes all-baseline total-compute parity.
- The evidence level is supported by the explicit static-versus-evolving evaluator comparison, with its restricted candidate-sequence/budget scope.
- No paper-inconsistency claim is made. Table11 includes multiple SAGE preferences and distinguishes active versus endpoint; we do not infer an aggregate discrepancy without a specified aggregation over those variants.

No score or judgment file was changed.
