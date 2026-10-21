"""Opus rulings for r03a a1 (data only; consumed by _build.py).

Seat records: sol a1 for 2502.05907, sol a2 for the other four (overrides.json); son55 a1 for all five.
"""
import copy

VER = "rsi-cards@52ff9657"
OOS_SCOPE = ["complete pinned v3 text: §I–§VI, Eq. 1–26, Tables, Appendix hyperparameters"]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}

    def smatch(s, p, main, **upd):
        for m in seat(s, p)["rs_pattern"]["matches"]:
            if m["main_id"] == main:
                m2 = prefix(copy.deepcopy(m), s)
                m2.update(upd)
                return m2
        raise KeyError((s, p, main))

    def dmatch(s, p, main, **upd):
        for m in seat(s, p)["domain_pattern"]["matches"]:
            if (m.get("main") or m.get("main_id")) == main:
                m2 = prefix(copy.deepcopy(m), s)
                m2["main"] = m2.pop("main_id", None) or m2["main"]
                if "sub_id" in m2:
                    m2["sub"] = m2.pop("sub_id")
                m2["version"] = VER
                m2.update(upd)
                return m2
        raise KeyError((s, p, main))

    def C(p, f):
        return conflict(p, f)

    def X(p, eid):
        return f"expectations[{eid}].status"

    # =========================================================== 2502.05907 EvolvingAgent (out_of_scope)
    p = "2502.05907"
    oos_reason = ("out_of_scope (rubric A3 bullet 1): the improvements are weight updates — the planner is LoRA-fine-tuned on "
                  "input-output pairs from failed subtasks (opus:O01, opus:O02) and the continual world model is updated by "
                  "gradient steps on curriculum-selected experiences with EWC-style regularisation (opus:O03, sol:E003). The "
                  "multimodal experience pool is a replay/training-data store; Eq. 13 lists it as a planner input, but the "
                  "concrete reuse operation is fine-tuning, not injection into a prompt/skill/workflow/memory. Not scored; null "
                  "is not a zero-quality rating.")
    unk = lambda: R("unknown", None, oos_reason, ["opus:O01", "opus:O02", "opus:O03"], [], OOS_SCOPE)
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "The LLM-based planner undergoes lightweight fine-tuning using Low-Rank Adaptation (LoRA)",
                    "§IV-A Self-planning", "Planner improvement is a weight update."),
            opus_ev(p, "O02", "We only use input-output pairs for model fine-tuning.", "§IV-A Self-planning",
                    "Retrieved failure trajectories are converted to fine-tuning pairs, not to retained context."),
            opus_ev(p, "O03", "employs a two-stage CL algorithm to optimize experience selection, which can enable agents to "
                    "efficiently update the world model without human intervention", "§IV-C CL-based reflector",
                    "Curriculum selection exists only to drive world-model weight updates."),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "outside_taxonomy": True, "matches": [],
            "reason": "Informational (out_of_scope), sol's identification kept: C24 (generative conditioning redesign) and C03 "
                      "(inference-only conditioning) both fail on the explicit LoRA/world-model retraining; no RS card is "
                      "forced. son55 did not identify (allowed for out_of_scope records); no mechanical conflict.",
            "executes_pattern": "not assessed (out_of_scope)", "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi", "matches": [],
                           "unassigned": ["Weight-updating embodied world-model agents with a replay pool sit outside all rsi "
                                          "cards by design (both seats)."],
                           "revision_proposals": []},
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": None,
            "evidence_level_note": "Harness evidence labels are not assigned to out-of-scope weight-level self-improvement "
                                   "(run convention: cal-dev 2410.15639, r01a, r02b, r03b).",
            "claim_support": None,
            "claim_support_note": "Not assessed under this rubric; Minecraft/Atari results recorded as author-reported only.",
            "strongest_supported_claim": None,
            "unresolved": ["Out-of-scope disposition is not a judgment that the embodied-agent results are wrong."]},
        "ratings": {k: unk() for k in ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")},
        "status": "out_of_scope",
        "reason": oos_reason,
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "sol", "system_method",
                "The authors' central claim is a whole closed-loop agent (planner-controller-reflector), not a trained harness "
                "component with an interface; component_training in SCORE_SPEC is for non-weight-harness components trained "
                "for a loop. Informational only (record not scored).", ["sol:E007", "son55:E004"], "none"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "revised", None,
                "Neither 'task' (sol) nor 'not_assessed' (son55) is assigned for out-of-scope records; run convention is null "
                "with a note.", ["opus:O01"], "none"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Central claim not checked under this rubric; null with note (run convention).", ["opus:O03"], "none"),
            res(X(p, "local:2502.05907-1"), *C(p, X(p, "local:2502.05907-1")), "sol", "unmet",
                "Kept as the informational scope check: no retained non-weight harness component exists; the replay pool "
                "feeds fine-tuning (opus:O02). son55 recorded the same fact in its status reason without an expectation.",
                ["opus:O02", "sol:E002", "son55:E003"], "none"),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §I–§VI: planner LoRA on failure pairs, DreamerV3-style world-model "
                                                   "updates with curriculum subtask/experience selection and Fisher penalty; "
                                                   "experience pool = replay → out_of_scope (A3 bullet 1).",
            "integrity_checks": "sol a1 (pre-contamination, retained by overrides.json) and son55 a1 on 2502.05907v3, material "
                                "sha d97d9a03…; hashes equal conflicts.json; both out_of_scope independently.",
            "core_claim_check": "Independently confirmed: Eq. 13 nominally maps D_MEP into the planner, but §IV-A specifies the "
                                "use as LoRA fine-tuning pairs (opus:O01–O02); no prompt/memory injection path is described.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2502.07373 EvoFlow
    p = "2502.07373"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "EvoFlow 459.24 459.24 513.34 513.34 972.58 972.58 1,660,284 1,660,284 72.90 % 72.90\\% 479.10 "
                    "479.10 286.05 286.05 565.15 565.15 8,193,669 8,193,669 87.62 % 87.62\\%", "Table 3, EvoFlow row",
                    "MBPP: 479.10+286.05=765.15, not 565.15; with 765.15 EvoFlow is not the lowest-overall-cost workflow on "
                    "MBPP (AFlow-Hermes 692.75, AFlow-Llama 740.29) and its 8.19M tokens are the largest in the MBPP block."),
            opus_ev(p, "O02", "AFlow Hermes 572.09 572.09 1045.20 1045.20 1617.29 1617.29 4,886,371 4,886,371 32.14 % 32.14\\% "
                    "353.04 353.04 339.71 339.71 692.75 692.75 1,289,901 1,289,901 66.13 % 66.13\\%", "Table 3, AFlow-Hermes row",
                    "Comparator for the MBPP cost ranking (overall 692.75 < 765.15)."),
            opus_ev(p, "O03", "Notably, if the generated workflow performs suboptimally, i.e., it does not Pareto dominate any "
                    "existing workflows, it is unlikely to be accepted into the population.", "Appendix B, Algorithm 1 comment",
                    "Admission gate is a Pareto-indicator comparison inside the niche, computed from running averages where a "
                    "new offspring has one query of evidence."),
            opus_ev(p, "O04", "autonomously retrieves domain-relevant and complexity-adapted agentic systems from the "
                    "well-optimized population, to swiftly and efficiently address user queries.", "§1 Introduction",
                    "The only description of test-time use; how many workflows run per test query and how one answer is "
                    "chosen is unspecified (determines Tables 2–3)."),
            opus_ev(p, "O05", "selecting 617 problems from four representative problem types", "Appendix G.1",
                    "Table 5 gives MATH 119 train + 486 test = 605 ≠ 617."),
            opus_ev(p, "O06", "Balancing cost-effectiveness, we set", "§5.4 Sensitivity Analysis",
                    "N=15 is chosen from the sensitivity curves (Figure 6); no development split is named for this choice."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["reframe_as_solvable_object"], "outside_taxonomy": False,
            "reason": "Load-bearing move: the conventionally fixed homogeneous backbone and the single best workflow are turned "
                      "into searchable variables (LLM mutation, population retention) — generative_process_redesign, sub null "
                      "(C15/C23/C24 are diffusion/geometry/conditioning-granularity tactics). The multi-objective (cost, "
                      "utility) formulation is kept as supporting reframe_as_solvable_object, partial: the object is formally "
                      "defined (Eq. 5–6, App. C) but no correspondence between the niching EA output and the Pareto set is "
                      "argued (rs RE-1 unmet). Neither card scores.",
            "matches": [
                smatch("sol", p, "generative_process_redesign", fit="partial"),
                smatch("son55", p, "reframe_as_solvable_object", role="supporting", fit="partial",
                       reason="Supporting: scalar workflow search recast as cost-performance multi-objective search solved "
                              "with an indicator-based niching EA; formal object defined, correspondence/convergence not shown."),
            ],
            "executes_pattern": "partial (backbone/prompt/operator made searchable; niching-retention rule not ablated)",
            "resolves_problem": "partial: held-out gains under gpt-4o-mini and MATH cost/accuracy vs o1-preview; MBPP cost "
                                "advantage not established (opus:O01)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                dmatch("son55", p, "population_search_executable_fitness",
                       reason="H16: niching retains a cost-versus-utility frontier of complementary workflows; both seats "
                              "agree (high)."),
                dmatch("sol", p, "search_agent_architecture", fit="partial",
                       reason="H17: workflow structure searched offline on the train split with execution fitness; deployed "
                              "as a population rather than one frozen design, hence partial (both seats)."),
            ],
            "unassigned": [],
            "revision_proposals": ["sol: H17 wording covers a single frozen design, not an offline multi-design population "
                                   "(proposal only).",
                                   "son55: H16 step 3 could list single-query running-average admission as a recorded "
                                   "weak-gate variant (proposal only)."],
        },
        "pattern_mapping": [
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "population_search_executable_fitness", "domain_sub": "H16",
             "operation_correspondence": "Freeing the backbone/workflow choice is realised as a population whose retention "
                                         "rule keeps cost-diverse candidates.",
             "necessary_conditions_and_differences": "H16 needs an archive-entry gate and a retention-rule ablation; EvoFlow "
                                                     "admits on one-query evidence and never ablates niching.",
             "evidence_ids": ["son55:E005", "son55:E009", "opus:O03"]},
            {"rs_main": "reframe_as_solvable_object", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "search_agent_architecture", "domain_sub": "H17",
             "operation_correspondence": "The multi-objective object is optimised offline over workflow structures.",
             "necessary_conditions_and_differences": "No correspondence argument (RS) and no matched-budget baseline (H17 "
                                                     "step 4).",
             "evidence_ids": ["son55:E001", "son55:E020"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2502.07373-1"): "local:2502.07373-2",
                    ("sol", "local:2502.07373-2"): "local:2502.07373-1"}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "The population is evolved on the 20% train split with ground-truth correctness and cost, "
                                   "then used on the disjoint 80% test split; mutation/retrieval ablations change test "
                                   "accuracy. No evolved-vs-initial-population or retention-rule control, so the size of the "
                                   "retained benefit relative to P0 is not isolated; no improver claim.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single run: under gpt-4o-mini the evolved population scores higher "
                                         "on held-out test splits than reproduced hand-crafted and automated workflows (avg "
                                         "82.55 vs AFlow 78.40), and on MATH the four-open-model population reaches 72.90 vs "
                                         "o1-preview 70.20 at 12.4% of o1's cost. The o1 claim does not hold on MBPP (87.62 vs "
                                         "89.65) and the MBPP cost advantage is not established (opus:O01); attribution to "
                                         "niching and to the model pool is not isolated.",
            "unresolved": ["Test-time workflow selection rule (opus:O04).",
                           "No niching-off / best-single / P0 control; no pool-matched baseline.",
                           "Internal inconsistencies: 7 vs 6 benchmarks, MATH margin 5.91 vs 6.42, MATH 605 vs 617 "
                           "(opus:O05), MBPP overall cost (opus:O01)."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Names what was fixed (single homogeneous backbone, single complex "
                   "workflow) with a capability matrix over AFlow/ADAS/AgentSquare/GPTSwarm and cost stakes; not 4 because "
                   "router/cascade neighbours are not engaged and the 'first' claim is unchecked.",
                   ["son55:E002", "son55:E003", "son55:E030", "son55:E031", "son55:E032", "sol:E001"]),
            "M": R("resolved", 3, "Opus sides with sol. LLM/prompt/operator mutation plus cost-and-tag niching directly target "
                   "the two named bottlenecks, and the design predicts a cost-performance front with cheap workflows for easy "
                   "queries (shown in Figure 4 text). Not 4: admission rests on single-query running averages and the "
                   "test-time dispatch is unspecified; son55's points are charged once, under X (2).",
                   ["son55:E004", "son55:E005", "son55:E006", "son55:E007", "son55:E028", "sol:E002"], ["opus:O03"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1, prompts and hyperparameters are given, but Eq. 16 "
                   "counting/averaging is ambiguous, admission is a one-query Pareto comparison (opus:O03), crossover/mutation "
                   "scheduling and the test-time selection rule are unspecified (opus:O04), and there is no rollback.",
                   ["sol:E003", "son55:E008", "son55:E009", "son55:E026", "opus:O03", "opus:O04"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Answer match, unit-test pass@1 and ALFWorld success "
                               "with measured API cost; not 4 because test denominators are internally inconsistent "
                               "(MATH 605 vs 617, opus:O05) and ablation magnitudes are figure-only.",
                               ["son55:E010", "son55:E011", "son55:E013", "sol:E005", "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-backbone comparison (Table 2) and four "
                             "mutation/retrieval ablations exist, but no niching-off, best-single or P0 control, hetero gains "
                             "are confounded with the 4-model pool, and AFlow is capped at 20 iterations.",
                             ["son55:E018", "son55:E019", "son55:E020", "son55:E014", "sol:E004"], ["son55:E013"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked and kept. Evolution touches only the train split with "
                           "ground truth; tests are disjoint. Deductions: N chosen from sensitivity curves without a named "
                           "dev split (opus:O06), claim scope overstated (o1 only on MATH, 7 vs 6 benchmarks), no "
                           "contamination discussion.",
                           ["son55:E010", "son55:E011", "son55:E017", "son55:E022", "son55:E023", "sol:E005", "opus:O06"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): test sizes are reported and some baselines below "
                              "vanilla are shown, but main results are single numbers with no seeds or intervals; variance "
                              "exists only in figures.",
                              ["son55:E013", "son55:E011", "sol:E005"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Training, inference, overall cost and tokens are tabulated for "
                        "the heterogeneous setting and the MATH ratios recompute (459.24/1223.46=37.5%, 972.58/7840.51=12.4%). "
                        "But the MBPP overall cost is mis-summed and, corrected to 765.15, EvoFlow is not the cheapest overall "
                        "(AFlow-Hermes 692.75, AFlow-Llama 740.29) while using the most tokens (8.19M) (opus:O01, opus:O02); "
                        "Table 2 has no cost, and baseline search budgets are not matched. Relevant but with a key gap in "
                        "one of two cost settings = 2.",
                        ["son55:E016", "son55:E027", "son55:E029", "son55:E015", "sol:E007", "sol:E008", "opus:O01",
                         "opus:O02"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–H; in scope (B: workflow search whose non-weight population is "
                  "retained and reused on held-out tests); all eight items resolved. Figures 4–6 are images not in the pinned "
                  "text; only their textual summaries are used.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "The paper's two named gaps are fixed defaults (one backbone, one workflow) turned into search variables; the "
                "multi-objective object is the vehicle, not a reduction to a solver with guarantees. son55's reframe is kept "
                "as supporting.", ["son55:E003", "son55:E005", "sol:E001"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["reframe_as_solvable_object", None]],
                "Both identifications are real but partial; one primary + one supporting, both sub null (no C-sub tactic fits).",
                ["son55:E001", "sol:E002"], "none"),
            res(X(p, "local:2502.07373-1"), *C(p, X(p, "local:2502.07373-1")), "same_supported_fact", "unmet",
                "A4-type ID swap: sol's local-1 is the cost question (partial) and its local-2 the statistics question "
                "(unmet); son55 numbered them the other way. Same answers. Final local-1 = statistics (unmet).",
                ["son55:E013", "sol:E007"], "none; consistent with E.statistics=1"),
            res(X(p, "local:2502.07373-2"), *C(p, X(p, "local:2502.07373-2")), "same_supported_fact", "partial",
                "Same swap; final local-2 = cost (partial): heterogeneous costs tabulated, homogeneous costs absent, MBPP "
                "total mis-summed.", ["son55:E016", "sol:E007"], "none; consistent with E.cost=2"),
            res(X(p, "local:2502.07373-3"), *C(p, X(p, "local:2502.07373-3")), "son55", "unmet",
                "Verified: no evaluation of P0, best-single member or random search; niching has no w/o variant.",
                ["son55:E018", "son55:E019"], "none; supports E.causality=2"),
            res(X(p, "local:2502.07373-4"), *C(p, X(p, "local:2502.07373-4")), "son55", "unmet",
                "Verified: hetero baselines (AFlow/DyLAN) run one model each; no baseline receives the 4-model pool.",
                ["son55:E014"], "none; supports E.causality=2"),
            res(X(p, "local:2502.07373-5"), *C(p, X(p, "local:2502.07373-5")), "son55", "partial",
                "Verified: o1-preview surpassed on MATH only (MBPP 87.62 vs 89.65); 7 vs 6 benchmarks; 5.91 vs 6.42.",
                ["son55:E017", "son55:E022", "son55:E023", "son55:E024", "son55:E025"], "none; reflected in E.holdout deductions"),
            res(X(p, "rs:reframe_as_solvable_object/RE-1"), *C(p, X(p, "rs:reframe_as_solvable_object/RE-1")), "son55",
                "unmet", "Applies because the supporting card is kept; App. C defines Pareto concepts but nothing ties the "
                "niching EA output to the Pareto set.", ["son55:E001"], "none"),
            res(X(p, "rs:reframe_as_solvable_object/RE-5"), *C(p, X(p, "rs:reframe_as_solvable_object/RE-5")), "son55",
                "partial", "Verified: training cost and N-cost trend reported; scaling beyond six benchmarks unexamined.",
                ["son55:E027", "son55:E029"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/F1"),
                *C(p, X(p, "rsi:population_search_executable_fitness/F1")), "son55", "met",
                "Failure mode not triggered: the change is at the search level (objective and genome), not a generic loop on "
                "a new domain.", ["son55:E001", "son55:E005"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/F2"),
                *C(p, X(p, "rsi:population_search_executable_fitness/F2")), "son55", "partial",
                "Verified: new objective/genome present, but the selector is an adapted indicator-based niching EA.",
                ["son55:E009"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/H16.step1"),
                *C(p, X(p, "rsi:population_search_executable_fitness/H16.step1")), "son55", "met",
                "Axes named (cost, performance, domain/complexity tags).", ["son55:E002", "son55:E004"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/H16.step3"),
                *C(p, X(p, "rsi:population_search_executable_fitness/H16.step3")), "son55", "unmet",
                "Verified: one-query running-average Pareto admission, no paired test or confirmation (opus:O03).",
                ["son55:E009", "opus:O03"], "none; charged under X=2"),
            res(X(p, "rsi:population_search_executable_fitness/H16.step4"),
                *C(p, X(p, "rsi:population_search_executable_fitness/H16.step4")), "son55", "met",
                "K sensitivity and per-query cost of N reported.", ["son55:E029"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/H16.step5"),
                *C(p, X(p, "rsi:population_search_executable_fitness/H16.step5")), "son55", "partial",
                "Disjoint split yes; retention rule not ablated.", ["son55:E010", "son55:E018"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/S2"),
                *C(p, X(p, "rsi:population_search_executable_fitness/S2")), "son55", "met",
                "Fitness = ground-truth correctness / unit tests / ALFWorld success plus measured cost.",
                ["son55:E010", "sol:E009"], "none"),
            res(X(p, "rsi:population_search_executable_fitness/S5"),
                *C(p, X(p, "rsi:population_search_executable_fitness/S5")), "sol", "partial",
                "Verified: experience pools exist (App. F) but no best-only or no-niching retention ablation.",
                ["sol:E004", "son55:E033"], "none"),
            res(X(p, "rsi:search_agent_architecture/S3"), *C(p, X(p, "rsi:search_agent_architecture/S3")), "sol", "met",
                "Verified: correctness/cost on train items, not proposer self-assessment, decides survival.",
                ["sol:E003", "sol:E009"], "none"),
            res(X(p, "rsi:search_agent_architecture/S6"), *C(p, X(p, "rsi:search_agent_architecture/S6")), "sol", "partial",
                "Held-out split and a cross-domain table (Table 6); no different executor or leakage audit.",
                ["sol:E005", "son55:E021"], "none"),
            res("ratings.M", *C(p, "ratings.M"), "sol", {"status": "resolved", "rating": 3},
                "Operations map onto both named bottlenecks and yield a checkable cost-performance prediction; the admission "
                "and dispatch gaps son55 cites are real but are operation-execution gaps already scored under X=2 (A2 spirit: "
                "one defect, one item).", ["son55:E005", "son55:E028", "opus:O03", "opus:O04"], "+5.0 vs son55 value"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "son55's 3 treated the MBPP total as a slip; corrected, the MBPP economy claim fails (opus:O01, opus:O02), "
                "homogeneous costs are absent and budgets unmatched. sol's 2 stands with this reason added.",
                ["son55:E016", "opus:O01", "opus:O02", "son55:E020"], "-1.25 vs son55 value"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims (MBPP cost) / ratings.E.cost.reason",
             "seat_values": {"sol": "MBPP overall-cost discrepancy not discussed", "son55": "noted 565.15≠765.15 as arithmetic"},
             "final_value": "Corrected MBPP overall cost 765.15 makes EvoFlow neither cheapest overall nor most token-economical "
                            "on MBPP; the 'economical' claim is supported on MATH only.",
             "reason": "Neither seat checked the ranking consequence of the mis-summed cell.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none beyond the E.cost resolution (2)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text and appendices first. Provisional: in scope (B workflow "
                                                   "search, retained population, train/test 1:4); G3 M3 X2 Em3 Ec2 Eh2–3 Es1 "
                                                   "Ecost2; found MBPP cost mis-sum changes ranking, MATH 605 vs 617, "
                                                   "unspecified test-time dispatch.",
            "integrity_checks": "sol a2 (clean re-review per overrides.json) and son55 a1 on 2502.07373v1, sha a31dc2fc…; "
                                "hashes equal conflicts.json; son55:E003 matches the material up to whitespace.",
            "core_claim_check": "Recomputed Table 3: MATH 459.24+513.34=972.58 ✓; 37.5%/19.5%/12.4% ✓; o1 +2.7 on MATH ✓; "
                                "MBPP 765.15 vs printed 565.15 ✗. Table 2 MATH margin 57.70−51.28=6.42 (intro 5.91 ✗).",
            "retention_check": "Failure denominators: test splits only (single run). Selection vs test: evolution on train; N "
                               "chosen from sensitivity curves. Extra budget: each train query executes K+1+E workflows; "
                               "pool access not given to baselines. 'Kept population' is shown to beat other systems, not "
                               "shown to beat its own P0.",
        },
    }

    # =========================================================== 2502.11448 AGrail
    p = "2502.11448"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "GPT-4o-mini 67.9 70.9 84.1", "Table 3 (ID row)",
                    "Main-text ID TTA accuracy for GPT-4o-mini is 84.1."),
            opus_ev(p, "O02", "GPT-4o-mini Test Time Adaptation 74.1 ±8.6", "Appendix D.1 Table 9",
                    "The same configuration is 74.1±8.6 in the appendix table: 84.1 vs 74.1 is an unreconciled "
                    "inconsistency in the memory ablation."),
            opus_ev(p, "O03", "EICU-AC (Target) Claude-3.5-Sonnet 100 100 100 100 GPT-4o 94.0 100 89.3 94.3 Claude-3.5-Sonnet "
                    "(base) 100 100 100 100 GPT-4o (base) 100 100 100 100", "Appendix D.3 Table 6",
                    "Transferred memory never beats the no-transfer base: Claude ties at ceiling, GPT-4o drops 6 points."),
            opus_ev(p, "O04", "These results demonstrate AGrail’s strong domain transferability", "§6.2 Domain Transferability",
                    "The authors' transfer conclusion, which Table 6 does not support as a benefit."),
            opus_ev(p, "O05", "We selected Claude-3.5-Sonnet for agreement evaluation due to its strong reasoning ability, "
                    "ensuring reliable consistency checks.", "Appendix C.2.2",
                    "Judge validity is asserted, not measured; Claude-3.5 is also an evaluated AGrail backbone."),
            opus_ev(p, "O06", "Therefore, we computed these predictive performance metrix only for cases where the OS agent "
                    "successfully completed the user request.", "Appendix C.2.1 Normal Scenario",
                    "Benign-accuracy denominator is conditional on agent success."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Retrieved, LLM-curated safety checks condition frozen Analyzer/Executor LLMs (adapt_via_conditioning). "
                      "C03 assigned at partial fit: a uniform checklist/action schema over heterogeneous agents, a retrieved "
                      "reference bank keyed in a shared paraphrase space (the no-upstream-tuning branch), and a domain-level "
                      "OOD split on Mind2Web-SC; step 5 (nearest-neighbour/longer-context baseline) is absent. Per-check "
                      "delegation to environment tools (OS detector executes code) is kept as supporting decompose_and_"
                      "delegate, low fit, sub null (tools are LLM-written, not sound solvers).",
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", fit="partial"),
                smatch("son55", p, "decompose_and_delegate", role="supporting", fit="low"),
            ],
            "executes_pattern": "partial", "resolves_problem": "partial: freeze-memory gain on one dataset; main tables are TTA",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "abstract_experience_into_guidance", fit="medium",
                               reason="H01 (both seats): explicit add/revise/merge/delete over stored checks with "
                                      "similarity-based overwrite; gate is the Executor LLM (+optional tool), not a measured "
                                      "outcome; no curator ablation.")],
            "unassigned": [],
            "revision_proposals": ["son55: H01 could note label-free guard-check memories whose edit signal is the same model "
                                   "family plus tool output (proposal only)."],
        },
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03", "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H01",
             "operation_correspondence": "Stored checks retrieved by step-back action key condition the frozen guard LLMs; "
                                         "the store is curated by explicit edits.",
             "necessary_conditions_and_differences": "H01 asks for an outcome-gated edit signal with stated reliability and a "
                                                     "curator ablation; neither is present.",
             "evidence_ids": ["son55:E004", "son55:E007", "son55:E029", "sol:E002"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2502.11448-2"): "local:2502.11448-6",
                    ("sol", "local:2502.11448-3"): "local:2502.11448-2",
                    ("sol", "local:2502.11448-4"): "local:2502.11448-3"}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "A memory built on a Mind2Web-SC train split and frozen improves held-out accuracy over "
                                   "no memory (Claude OOD 93.9±1.0 vs 89.7±1.0, 3 seeds; ID within noise). Narrow: one "
                                   "dataset; main tables and transfer are TTA on the evaluated stream.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: a frozen check memory helps held-out Mind2Web-SC domains for Claude; "
                                         "online-TTA AGrail blocks far fewer benign actions than same-LLM prompt guardrails at "
                                         "low ASR on 20–100-item groups. 'Strong transferability' is not supported as a gain "
                                         "(opus:O03); 'optimal/lifelong' claims are not tested.",
            "unresolved": ["Table 3 vs Table 9 GPT-4o-mini ID TTA (84.1 vs 74.1; opus:O01–O02).",
                           "Whether labels enter memory 'training' is unstated.",
                           "No tool-off/Executor-off/budget-matched controls; cost only a figure."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Fixed component (manually specified trusted contexts / LLM "
                   "policies) and nearest neighbours (GuardAgent, Conseca) named, with a measured residue (prompt guardrails "
                   "block up to ~50% benign actions).",
                   ["son55:E002", "son55:E003", "son55:E026", "son55:E015"]),
            "M": R("resolved", 2, "Opus sides with son55. The Analyzer/Executor edit loop, step-back key and per-check tools fit "
                   "the over-blocking problem, but the key assumption — that the same LLMs can tell necessary from harmful "
                   "checks without any outcome label — is unexamined, and 'converges to Ω*' is unobservable outside the "
                   "constructed learning analysis.",
                   ["son55:E004", "son55:E006", "son55:E029", "son55:E028", "sol:E002"], ["son55:E024"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithms 1–3, overwrite threshold 0.8 and tool roles given; "
                   "prompts are images, memory 'training' (labels?) unstated, no versioning, rollback, forgetting or growth "
                   "control.", ["son55:E007", "sol:E001", "sol:E002", "son55:E032"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. ASR/accuracy use ground-truth labels and attacks were "
                               "validated, but the headline agreement metric is judged by Claude-3.5 (an AGrail backbone) "
                               "with validity asserted, not measured (opus:O05); Safe-OS is a 100-item author-built set "
                               "scored by keyword matching; benign accuracy is conditional on agent success (opus:O06).",
                               ["son55:E020", "son55:E021", "son55:E031", "sol:E006", "opus:O05", "opus:O06"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. No/freeze/TTA memory ablation with 3 seeds on "
                             "Mind2Web-SC isolates stored checks; no Executor-off, tool-off, nearest-neighbour or budget-"
                             "matched controls; system baselines are single-call and lack the environment tool.",
                             ["sol:E003", "son55:E011", "son55:E012", "son55:E028", "son55:E015"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. A clean ID/OOD freeze-memory split exists but only on "
                           "Mind2Web-SC; all main-table numbers and the transfer test are TTA on the evaluated stream, the "
                           "transfer table shows no gain over the no-transfer base (opus:O03) while the text claims strong "
                           "transferability (opus:O04), and the ablation numbers disagree between Table 3 and Table 9 "
                           "(opus:O01–O02).",
                           ["son55:E008", "son55:E009", "son55:E010", "son55:E033", "sol:E004", "opus:O03", "opus:O04"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): 3-seed std for memory and order ablations and admitted "
                              "learning-phase misses; main tables single runs on 20–100-item groups with no intervals.",
                              ["sol:E003", "son55:E016", "son55:E017", "son55:E021"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only a qualitative input-token figure; no call counts, "
                        "output tokens, latency or tool-codegen cost despite two LLMs plus tools per action.",
                        ["sol:E007", "son55:E018"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendices (prompt/demo figures are images not in the text); in scope (A/B: "
                  "non-weight safety-check memory refined from guarded actions and reused); all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", "C03"], ["decompose_and_delegate", None]],
                "Primary parent agreed. C03 kept (sol) at partial fit because the uniform schema, retrieved bank and a domain-"
                "level OOD split are present; son55's reason for null (upstream tuning) ignores C03's no-tuning retrieval "
                "branch. son55's tool-delegation match is kept as low-fit supporting since the OS detector is load-bearing "
                "for environment attacks.", ["son55:E010", "son55:E029", "son55:E032", "sol:E003"], "none"),
            res(X(p, "local:2502.11448-4"), *C(p, X(p, "local:2502.11448-4")), "son55", "unmet",
                "ID collision: sol's local-4 is the cost question (partial; merged into local-3, same answer as son55); "
                "son55's local-4 asks whether the agreement judge is validated — verified unmet (opus:O05).",
                ["son55:E020", "opus:O05", "sol:E007"], "none; consistent with E.measurement=2"),
            res(X(p, "local:2502.11448-5"), *C(p, X(p, "local:2502.11448-5")), "son55", "partial",
                "Verified: ASR excludes self-refusals, Safe-OS 100 items; learning-phase misses admitted.",
                ["son55:E022", "son55:E021", "son55:E017"], "none"),
            res(X(p, "rs:adapt_via_conditioning/RE-1"), *C(p, X(p, "rs:adapt_via_conditioning/RE-1")), "son55", "met",
                "Memory-on/off isolates the conditioning signal within the same framework (one dataset).",
                ["son55:E011", "son55:E012", "sol:E003"], "none"),
            res(X(p, "rs:adapt_via_conditioning/RE-2"), *C(p, X(p, "rs:adapt_via_conditioning/RE-2")), "son55", "unmet",
                "No overlap/contamination analysis; Safe-OS authored with the method.", ["son55:E021"], "none"),
            res(X(p, "rs:adapt_via_conditioning/RE-3"), *C(p, X(p, "rs:adapt_via_conditioning/RE-3")), "son55", "unmet",
                "No longer-context, nearest-neighbour or append-only baseline.", ["son55:E015"], "none"),
            res(X(p, "rs:adapt_via_conditioning/RE-6"), *C(p, X(p, "rs:adapt_via_conditioning/RE-6")), "son55", "partial",
                "Backbone/order sensitivity and universal-vs-task criteria reported; memory-source quality not varied.",
                ["son55:E016", "son55:E030"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/F2"), *C(p, X(p, "rsi:abstract_experience_into_guidance/F2")),
                "son55", "partial", "Safety-specific mechanism (criteria, per-check tools), not a bare reflect-store port.",
                ["son55:E028", "son55:E032"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/H01"), *C(p, X(p, "rsi:abstract_experience_into_guidance/H01")),
                "sol", "partial", "Edit chain exists; self-judged gate, no rollback, no edit-operation ablation.",
                ["sol:E001", "sol:E002"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S3"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S3")),
                "son55", "partial", "Tools ground some checks in the environment; edits themselves are LLM judgements.",
                ["son55:E004", "son55:E032"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S4"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S4")),
                "son55", "partial", "Merge/revise/delete exist; no size bound or forgetting; whole-entry overwrite at >0.8.",
                ["son55:E007", "sol:E002"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S5"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S5")),
                "son55", "partial", "Gate is the Executor LLM (+optional tool), not a measured utility.", ["son55:E004"], "none"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "The operations fit the problem (sol), but the load-bearing assumption — label-free self-judged pruning finds "
                "the right checks — is neither argued nor tested beyond a constructed single-action convergence plot.",
                ["son55:E004", "son55:E006", "son55:E024"], "-5.0 vs sol value"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "Ground-truth ASR/accuracy are credible (sol), but the agreement metric behind a headline claim uses an "
                "unvalidated same-family judge and Safe-OS is small, keyword-scored and author-built.",
                ["son55:E020", "son55:E021", "opus:O05", "opus:O06"], "-2.5 vs sol value"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 2},
                "sol's 3 credits the clean freeze split, which is real but confined to one dataset; the transfer test gives no "
                "gain over base while the text claims strong transferability, and the ablation table values conflict.",
                ["son55:E008", "son55:E033", "opus:O01", "opus:O02", "opus:O03", "opus:O04"], "-2.5 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims / ratings.E.holdout (memory ablation values)",
             "seat_values": {"sol": "cited Tables 9–10 only", "son55": "cited Table 3 ID GPT-4o-mini TTA 84.1 (son55:E011)"},
             "final_value": "Table 3 (84.1) and Table 9 (74.1±8.6) disagree for GPT-4o-mini ID TTA; Claude rows agree.",
             "reason": "Neither seat cross-checked the main-text ablation against the appendix table.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none (E.holdout already 2; claim scoped)"},
            {"field_path": "assessment.strongest_supported_claim (transfer)",
             "seat_values": {"sol": "transfer: GPT-4o −5.7%, Claude no drop", "son55": "transfer: no degradation for Claude"},
             "final_value": "Transferred memory never exceeds the no-transfer base (Claude 100=100 at ceiling; GPT-4o 94.0 vs "
                            "100); transfer is at best non-harmful for one backbone, not a demonstrated benefit.",
             "reason": "Both seats compared against the source domain, not against the target base rows in Table 6.",
             "evidence_ids": ["opus:O03", "opus:O04"], "score_impact": "none (claim_support stays scoped, narrower wording)"},
            {"field_path": "expectations[local:2502.11448-2|-3]",
             "seat_values": {"sol": "local-2 measurement, local-3 statistics (both partial)",
                             "son55": "local-2 statistics, local-3 cost (both partial)"},
             "final_value": "Renumbered: local-2 statistics, local-3 cost (merged with sol's local-3/-4), sol's measurement "
                            "question kept as local-6 (partial).",
             "reason": "A4 ID collisions hidden from the mechanical diff by equal statuses.",
             "evidence_ids": ["sol:E005", "son55:E016"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text and appendices first. Provisional: in scope; G3 M2 X2 Em2 "
                                                   "Ec2 Eh2 Es2 Ecost1; noticed Table 3/9 inconsistency and that transfer shows "
                                                   "no gain over base.",
            "integrity_checks": "sol a2 and son55 a1 on 2502.11448v2, sha c3befdeb…; hashes equal conflicts.json; all seat "
                                "quotes verbatim.",
            "core_claim_check": "Verified Table 1/2 numbers quoted in text (Norm 95.6, SS 3.8, PI 0, Env 5, EIA 6/28/86.7); "
                                "Claude ID freeze gain (95.6→96.5) is within the reported std; OOD gain (89.7→93.9) is not.",
            "retention_check": "Failure denominators: ASR excludes self-refused samples, benign accuracy only over agent-"
                               "successful runs (opus:O06). Selection vs test: freeze split on Mind2Web-SC only; main results "
                               "TTA. Extra budget/privilege: environment-executing tool not available to baselines. 'Kept "
                               "checks' are shown to help one held-out set, not transfer.",
        },
    }

    # =========================================================== 2502.11799 Table-Critic
    p = "2502.11799"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "TabFact 29.3 0.6 7.8 62.1 20.4 17.1 2.19×", "Appendix C Table 4 (TabFact row)",
                    "0.25·62.1+0.75·2.04=17.06≈17.1 and 17.1/7.8=2.19: the printed 20.4M output is a one-cell typo for "
                    "2.04M; total and ratio are mutually consistent."),
            opus_ev(p, "O02", "Substituting these weights, the formula simplifies to:", "Appendix C.1",
                    "Formula N_total = 0.25·N_in + 0.75·N_out used for the check above."),
            opus_ev(p, "O03", "while our full Table-Critic allows the Curator agent to dynamically maintain and evolve the "
                    "template tree throughout the reasoning process.", "§4.6",
                    "The tree evolves over the evaluated question stream; no construction/evaluation split."),
            opus_ev(p, "O04", "Table-Critic 77.2 92.6 w/o Self-evolving 76.1 90.8", "Table 3",
                    "Retained-store increment 1.1 (WikiTQ, ≈48 of 4,344) and 1.8 (TabFact, ≈36 of 2,024) points, one run, "
                    "one backbone."),
            opus_ev(p, "O05", "On WikiTQ, it successfully corrects 9.6% of Chain-of-Table’s errors while only degrading 0.7% "
                    "of correct solutions", "§4.3",
                    "The 9.6/0.7 figures are shares of all questions (68.3+9.6−0.7=77.2), not of CoT errors/correct solutions."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering"],
            "outside_taxonomy": False,
            "reason": "The retained mechanism conditions a frozen Critic on templates routed from the tree "
                      "(adapt_via_conditioning); C03 not assigned: no category-level holdout and no nearest-neighbour/flat "
                      "baseline (run convention, e.g. r03b 2504.07952). The write signal is manufactured without labels — "
                      "only Judge-accepted refinements are distilled — kept as supporting self_supervised_signal_engineering, "
                      "sub null (C07/C08/C26 are training-data or preference tactics). The per-question critique loop itself "
                      "has no card.",
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", sub_id=None, fit="partial",
                       reason="Primary: routed templates condition the frozen Critic; C03 not assigned (no category holdout, "
                              "no flat-retrieval control)."),
                smatch("son55", p, "self_supervised_signal_engineering", role="supporting", fit="partial"),
            ],
            "executes_pattern": "partial", "resolves_problem": "partial: retained tree adds 1.1/1.8 points, single run",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "abstract_experience_into_guidance", fit="medium",
                               reason="H00: the Curator distils templates from (erroneous → repaired) refinement histories "
                                      "and mostly appends them; vertical/horizontal expansion reorganises categories but there "
                                      "is no update/merge/delete/forget policy over existing entries (H01's defining move).")],
            "unassigned": [],
            "revision_proposals": ["son55: H01 could add a hierarchical-tree store variant with add/vertical/horizontal edits "
                                   "and no deletion — Opus places such stores under H00 (proposal only)."],
        },
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H00",
             "operation_correspondence": "Templates abstracted from repaired chains are retrieved by error route into later "
                                         "critiques.",
             "necessary_conditions_and_differences": "H00 step 1/4 ask for a stated grounding-signal error rate and a frozen "
                                                     "store at test; Judge accuracy is unmeasured and the tree grows on the "
                                                     "test stream.",
             "evidence_ids": ["son55:E004", "son55:E021", "opus:O03"]},
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H00",
             "operation_correspondence": "Judge acceptance is the label-free write gate for new templates.",
             "necessary_conditions_and_differences": "No re-anchoring of the Judge against gold labels.",
             "evidence_ids": ["son55:E004", "sol:E008"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2502.11799-1"): "local:2502.11799-5",
                    ("sol", "local:2502.11799-2"): "local:2502.11799-6",
                    ("sol", "local:2502.11799-3"): "local:2502.11799-4"},
            overrides={"local:2502.11799-4": {
                "score_item": "X",
                "reason": "Merged (sol local-3 + son55 local-4): Judge verdicts gate tree writes but their precision/false-"
                          "accept rate is never measured, and the showcased refinement example keeps an error (sol:E008). The "
                          "Judge is the write gate, not the evaluation verifier (gold labels), so the item maps to X."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Templates written from earlier questions are read on later ones and the static-tree arm "
                                   "isolates the store (77.2→76.1, 92.6→90.8; opus:O04). Weak: prequential on the evaluated "
                                   "stream without labels, one run, one backbone; the bulk of the gain is the per-question "
                                   "loop, which is out of scope as single-answer self-correction.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single greedy run: the four-agent critique loop on Chain-of-Table "
                                         "chains raises WikiTQ/TabFact accuracy by +6.3/+2.2 (avg of three backbones) and beats "
                                         "15-sample self-consistency at ~2x base tokens; the retained template tree adds "
                                         "1.1/1.8 points on Qwen2.5-72B over a static two-template tree.",
            "unresolved": ["Construction/evaluation separation and processing order of the tree.",
                           "Judge reliability as write gate.", "Final tree size/contents."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The critique gap is concrete (error propagation; Critic-CoT degrades "
                   "4.9%), but this domain's G asks what fixed non-weight object becomes adaptive and how it differs from "
                   "same-class neighbours: the template-store gap ('error types are diverse') is asserted, and memory/"
                   "experience/template-library neighbours are absent from related work (only table reasoning and self-"
                   "reflection). Real limitation, incomplete neighbour comparison = 2.",
                   ["son55:E002", "son55:E003", "son55:E008", "son55:E020"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. First-error focus, prefix-only refiner and Judge-gated curation "
                   "are tied to stated observations and predict lower degradation, which is measured; not 4 because the gate "
                   "and critic share one LLM with no reliability check.",
                   ["son55:E004", "son55:E025", "son55:E008", "sol:E001"]),
            "X": R("resolved", 2, "Opus sides with sol. Roles, prompts, edit vocabulary, K and decoding are specified, but the "
                   "retention behaviour is not reconstructible: question order and persistence across the stream, templates "
                   "sampled per route, Curator call when no error was found, growth/pruning and rollback are unstated "
                   "(Algorithm 1 has no K cap), and the showcased refinement keeps an error (sol:E008). son55's own reason "
                   "lists these gaps, which match anchor 2 ('retention/recovery or key conditions unclear').",
                   ["sol:E008", "sol:E009", "son55:E019", "son55:E021", "son55:E023"]),
            "E.measurement": R("resolved", 3, "Opus sides with son55. The verifier is gold-label accuracy on full test sets, "
                               "with correction/degradation rates relative to the base chain; the Judge is not the evaluator. "
                               "sol's denominator point is a text misdescription (opus:O05), not a metric-validity flaw; not 4 "
                               "because the Δ rates are mislabelled in prose.",
                               ["son55:E007", "son55:E008", "son55:E013", "son55:E014", "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Compute-matched SC, same-chain Critic-CoT and the "
                             "static-tree arm are real controls; tree ablation one backbone/one run, no Judge/Curator/routing/"
                             "flat-store variants; retained share ~1–2 of ~9 points.",
                             ["son55:E010", "son55:E011", "son55:E016", "sol:E003", "sol:E006"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. Label-free updates avoid answer leakage, but the tree is built "
                           "on the very stream it is scored on with no split, frozen-tree test or order report (opus:O03); "
                           "this matches the run's anchor for same-stream label-free stores (r01b 2407.08937, r03b "
                           "2504.07952 = 1). son55's 2 has no separating evidence beyond label-freeness.",
                           ["son55:E006", "son55:E005", "sol:E004", "opus:O03"]),
            "E.statistics": R("resolved", 1, "Opus sides with sol (frozen A2 ladder): test sizes and degradation counts are "
                              "reported, but every number is a single greedy run with no intervals, seeds or order variance; "
                              "three backbones are not uncertainty quantification. The 1.1/1.8-point retained effect (~48/~36 "
                              "questions) has no paired test.",
                              ["son55:E015", "son55:E013", "son55:E014", "opus:O04"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Input/output token counts with a stated pricing formula, the "
                        "1.87x/2.19x ratios, and a compute-matched self-consistency baseline up to 15 samples. sol's 1 rested "
                        "on the TabFact row failing the formula; with output 2.04M both the total 17.1M and the 2.19x ratio "
                        "recompute exactly (opus:O01, opus:O02), so it is a one-cell typo. Not 4: tokens only, SC costs "
                        "figure-only, no Critic-CoT cost.",
                        ["son55:E009", "son55:E010", "son55:E017", "sol:E006", "opus:O01", "opus:O02"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. appendices; in scope only through the retained template tree (a non-weight "
                  "store written from earlier questions and read later), which is separately ablated; the per-question "
                  "critique loop alone would be single-answer self-correction. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "The retained object acts by conditioning the frozen Critic with routed templates; son55's manufactured-signal "
                "reading describes the write gate and is kept as supporting.", ["son55:E001", "son55:E004", "son55:E022"],
                "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", None], ["self_supervised_signal_engineering", None]],
                "C03 dropped from sol's match: no category-level holdout and no flat/nearest-neighbour control (C03 steps "
                "4–5); son55's card added as supporting with sub null.", ["sol:E004", "son55:E004"], "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"]],
                "Defining move is extracting templates from repaired-vs-erroneous histories and appending them (H00); H01 "
                "requires an editing policy over existing entries (update/merge/delete/forget), absent here (son55:E021).",
                ["son55:E021", "sol:E001", "sol:E002"], "none"),
            res(X(p, "local:2502.11799-1"), *C(p, X(p, "local:2502.11799-1")), "son55", "unmet",
                "ID collision: sol's local-1 (retained-tree causal isolation, partial) is a different question, kept as "
                "local-5; son55's local-1 asks for a construction/evaluation split — verified none (opus:O03).",
                ["son55:E006", "opus:O03", "sol:E003"], "none; consistent with E.holdout=1"),
            res(X(p, "local:2502.11799-2"), *C(p, X(p, "local:2502.11799-2")), "son55", "unmet",
                "ID collision: sol's local-2 (cost, partial) kept as local-6; son55's local-2 (repeat runs/orders) verified "
                "unmet.", ["son55:E015"], "none; consistent with E.statistics=1"),
            res(X(p, "local:2502.11799-4"), *C(p, X(p, "local:2502.11799-4")), "son55", "unmet",
                "Judge precision never measured; merged with sol's local-3 (same fact), score item set to X (the Judge is the "
                "write gate, not the evaluator).", ["son55:E004", "sol:E008"], "none; charged under X=2"),
            res(X(p, "rs:self_supervised_signal_engineering/RE-1"),
                *C(p, X(p, "rs:self_supervised_signal_engineering/RE-1")), "son55", "partial",
                "Applies (supporting card kept): loop shown on three backbones, tree ablation on one.", ["son55:E012"], "none"),
            res(X(p, "rs:self_supervised_signal_engineering/RE-2"),
                *C(p, X(p, "rs:self_supervised_signal_engineering/RE-2")), "son55", "partial",
                "Static-tree and compute-matched SC exist; no loop-without-Curator beyond static tree.",
                ["son55:E011", "son55:E010"], "none"),
            res(X(p, "rs:self_supervised_signal_engineering/RE-5"),
                *C(p, X(p, "rs:self_supervised_signal_engineering/RE-5")), "son55", "met",
                "Cost justified against compute-matched SC; ratios recompute (opus:O01).", ["son55:E009", "opus:O01"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/F5"), *C(p, X(p, "rsi:abstract_experience_into_guidance/F5")),
                "son55", "partial", "Store derives from refinement experience but its outcome is self-verified.",
                ["son55:E004"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/H00"), *C(p, X(p, "rsi:abstract_experience_into_guidance/H00")),
                "sol", "partial", "Judge-gated abstraction and later use with static-off arm; no frozen-store test.",
                ["sol:E001", "sol:E003"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S2"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S2")),
                "son55", "met", "Curator reads the erroneous and repaired chains with the critique (contrast).",
                ["son55:E004", "son55:E025"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S3"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S3")),
                "son55", "partial", "Grounding is the Judge's verdict; imperfection unquantified.", ["son55:E004"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S4"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S4")),
                "son55", "partial", "Structural edits but no deletion/merge/bounds; final size unreported.",
                ["son55:E021", "son55:E023"], "none"),
            res(X(p, "rsi:abstract_experience_into_guidance/S5"), *C(p, X(p, "rsi:abstract_experience_into_guidance/S5")),
                "son55", "partial", "Writes only after a Judge-verified final chain; self-judged.", ["son55:E004"], "none"),
            res(X(p, "rsi:attribute_and_patch_incumbent/F1"), *C(p, X(p, "rsi:attribute_and_patch_incumbent/F1")), "son55",
                "partial", "The card's F1 names table reasoning with a critique→rewrite loop; most gain is that loop, the "
                "tree is the added retained part.", ["son55:E024", "son55:E011"], "none"),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "son55's 3 credits the critique-loop gap; the retained-store gap has no same-class (memory/template-library) "
                "neighbours at all, which this domain's G requires.", ["son55:E020", "son55:E003"], "-3.75 vs son55 value"),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "son55's reason lists the same unreconstructible retention conditions (order, growth, pruning, rollback) "
                "that define anchor 2; sol:E008/E009 add an uncorrected example error and Algorithm/text K mismatch.",
                ["sol:E008", "sol:E009", "son55:E023"], "-5.0 vs son55 value"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 3},
                "Evaluation uses gold labels on full test sets; the mislabelled Δ denominators are prose errors (opus:O05) "
                "and the Judge's unreliability is a write-gate issue charged under X.",
                ["son55:E007", "son55:E008", "opus:O05"], "+2.5 vs sol value"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "Same-stream, label-free, no frozen-tree test or order report = 1 by run precedent; label-freeness alone does "
                "not reach 2.", ["son55:E006", "opus:O03"], "-2.5 vs son55 value"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", {"status": "resolved", "rating": 1},
                "A2 ladder: sample sizes and failures without any uncertainty = 1; multiple backbones do not substitute.",
                ["son55:E015", "opus:O04"], "-1.25 vs son55 value"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "resolved", "rating": 3},
                "The TabFact row reconciles with output 2.04M (opus:O01): total and ratio are consistent, so sol's 'cannot "
                "confirm 2.19x' does not hold; token accounting plus a compute-matched baseline = 3.",
                ["opus:O01", "opus:O02", "son55:E010", "sol:E007"], "+2.5 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.cost.reason (TabFact cost row)",
             "seat_values": {"sol": "row violates formula; 2.19x unconfirmable (sol:E007)",
                             "son55": "row does not satisfy the stated formula (son55:E017)"},
             "final_value": "Output 2.04M (not 20.4M) reproduces total 17.1M and ratio 2.19x exactly; one-cell typo.",
             "reason": "Both seats stopped at the mismatch without testing the obvious decimal-shift reconciliation.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "supports E.cost=3 (son55 value)"},
            {"field_path": "expectations[local:2502.11799-3]",
             "seat_values": {"sol": "Judge calibration (X), unmet", "son55": "alternative store variants (E.causality), unmet"},
             "final_value": "local-3 = son55's alternative-variant question (unmet); sol's question merged into local-4.",
             "reason": "A4 ID collision hidden from the mechanical diff by equal statuses.",
             "evidence_ids": ["sol:E008", "son55:E011"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first. Provisional: in scope only via the template tree; "
                                                   "most gain is the per-question loop; tree +1.1/+1.8 single run on the "
                                                   "evaluated stream; G2 M3 X2 Em3 Ec2 Eh1 Es1 Ecost3; TabFact cost row "
                                                   "reconciles with 2.04M.",
            "integrity_checks": "sol a2 and son55 a1 on 2502.11799v3, sha 70e7038a…; hashes equal conflicts.json; son55:E016 "
                                "matches up to whitespace.",
            "core_claim_check": "Recomputed Table 2 (68.3+9.6−0.7=77.2; 89.7+3.4−0.5=92.6; Critic-CoT 69.0/89.8 ✓) and Table 4 "
                                "WikiTQ (19.575≈19.6, 36.725≈36.7, 1.87x ✓); TabFact with 2.04M ✓.",
            "retention_check": "Failure denominators: full test sets, degradations counted. Selection vs test: the tree is "
                               "built on the test stream (label-free). Extra budget: ~2x tokens, matched against SC. 'Kept "
                               "templates' improve later questions by 1–2 points in one run; most of the claimed effect is "
                               "within-question refinement.",
        },
    }

    # =========================================================== 2502.12110 A-MEM
    p = "2502.12110"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "our A-Mem demonstrates superior performance in Multi-Hop tasks achieves at least two times better "
                    "performance", "§4.3 Performance Analysis",
                    "Table 1 GPT-4o-mini Multi-Hop F1 is 27.02 vs 26.65 (MemGPT) / 25.02 (LoCoMo); the ~2x gap is in the "
                    "Temporal column (45.85 vs 25.52/18.41)."),
            opus_ev(p, "O02", "achieves a ROUGE-L score of 44.27 in Multi-Hop tasks, more than doubling LoComo’s 18.09",
                    "Appendix A.3", "44.27 and 18.09 are the Temporal-column ROUGE-L values in Table 5, cited as Multi-Hop."),
            opus_ev(p, "O03", "ReadAgent 2.47 1.78 3.01 3.01 5.57 5.22 3.25 2.51 15.78 14.01 4.2 4.2 776",
                    "Table 1, Qwen2.5-3b ReadAgent row", "Same ten metric values as the Llama-3.2-3b ReadAgent row (opus:O04)."),
            opus_ev(p, "O04", "ReadAgent 2.47 1.78 3.01 3.01 5.57 5.22 3.25 2.51 15.78 14.01 4.2 4.2 461",
                    "Table 1, Llama-3.2-3b ReadAgent row", "Duplicated baseline row across backbones."),
            opus_ev(p, "O05", "ReadAgent 2.47 1.78 3.01 3.01 5.07 5.22 3.25 2.51 15.78 14.01", "Table 5, Llama-3.2-3b ReadAgent row",
                    "F1/BLEU values reappear as ROUGE-2/ROUGE-L in Table 5 (one digit differs)."),
            opus_ev(p, "O06", "For models that have already achieved state-of-the-art (SOTA) performance with k=10, we maintain "
                    "this value without further tuning.", "Appendix A.5",
                    "k is tuned on the evaluated categories until A-Mem is SOTA; small-model rows mostly keep k=10."),
            opus_ev(p, "O07", "The system requires approximately 1,200 tokens per memory operation", "§4.3 Cost-Efficiency",
                    "Per-operation figure exists, but no total write-path accounting over all inserted memories."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "The method answers new questions by conditioning a frozen LLM on retrieved, LLM-enriched notes, with no "
                      "parameter updates (adapt_via_conditioning, partial). C03 not assigned: no category-level holdout and no "
                      "equal-k flat-retrieval control (run convention). son55 is right that the novelty is write-time "
                      "restructuring of the store, which no RS card isolates; that part is carried by domain H04 (see "
                      "pattern_mapping) rather than by declaring outside_taxonomy when a parent card does apply.",
            "matches": [smatch("sol", p, "adapt_via_conditioning", sub_id=None, fit="partial",
                               reason="Retrieved notes condition the frozen answerer; C03 not assigned (no category holdout, "
                                      "no equal-k flat retrieval).")],
            "executes_pattern": "partial", "resolves_problem": "partial: structure ablation on one backbone, single run",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                dmatch("son55", p, "index_experience_for_reuse",
                       reason="H04 (both seats, high): raw content kept, LLM-generated keywords/tags/context/links form a "
                              "mutable index updated locally for top-k neighbours."),
                dmatch("son55", p, "abstract_experience_into_guidance", fit="low",
                       reason="H01 (low): memory evolution edits existing entries' context/tags (retrieval features) — an "
                              "editing policy over entries — but without an outcome gate or forgetting."),
            ],
            "unassigned": [],
            "revision_proposals": ["son55: H04 could separate content-triggered LLM metadata evolution (no outcome signal) from "
                                   "outcome-gated restructuring (proposal only)."],
        },
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "index_experience_for_reuse", "domain_sub": "H04",
             "operation_correspondence": "Read side: top-k retrieved notes condition the answerer. Write side (the "
                                         "contribution): H04 restructuring — attributes, links, local neighbour evolution.",
             "necessary_conditions_and_differences": "H04 asks for evidence thresholds before overwrite, costed maintenance and "
                                                     "flat-retrieval ablation at scale; A-Mem has none of the three.",
             "evidence_ids": ["son55:E004", "son55:E005", "son55:E010", "opus:O07"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2502.12110-2"): "local:2502.12110-3",
                    ("sol", "local:2502.12110-3"): "local:2502.12110-2",
                    ("sol", "local:2502.12110-4"): "local:2502.12110-6"},
            overrides={"local:2502.12110-1": {
                "status": "unmet",
                "reason": "Opus (son55's status): k is tuned per category on the evaluated data until A-Mem is SOTA and kept "
                          "at 10 only where already SOTA (opus:O06); no dev split and baselines get no equal tuning. "
                          "Memory construction never sees questions/answers, which is credited under E.holdout, not here."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Notes written from earlier sessions are read for later questions, and the w/o LG&ME / w/o "
                                   "ME rows isolate the retained structure (GPT-4o-mini). Weak: one backbone, one run, k tuned on "
                                   "the evaluated categories; small-model rows with untuned k=10 support the baseline comparison "
                                   "but have no ablation. No outcome-feedback learning or improver claim.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single run: on LoCoMo, LLM-built linked and evolved notes retrieved "
                                         "top-k beat bare notes and the listed memory baselines on most categories for small "
                                         "open models and on Temporal/Multi-Hop for GPT models at a fraction of full-context read "
                                         "tokens; GPT-4o loses Single-Hop/Adversarial to full context. Category-level claims "
                                         "are unreliable (opus:O01–O02), baseline rows are partly duplicated (opus:O03–O05).",
            "unresolved": ["Link traversal at retrieval (caption vs §3.4).", "Equal-k raw/flat retrieval control and Mem0.",
                           "Total write-path cost.", "Category labelling (Multi-Hop vs Temporal) in text vs tables."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Fixed component (predefined memory schemas/operations) and "
                   "neighbours named, but the failure is argued by example, Mem0 is named and not compared, stakes thin.",
                   ["son55:E002", "son55:E003", "sol:E004"]),
            "M": R("resolved", 2, "Opus sides with son55. Zettelkasten notes/links/evolution give a coherent story for "
                   "multi-hop recall, but the key assumption — unverified LLM rewrites of neighbours improve retrieval — is "
                   "never argued, and no distinguishable prediction against flat retrieval at equal k is posed; the one "
                   "category-level prediction the paper states (2x Multi-Hop) is not what its table shows (opus:O01). "
                   "Operation-chain ambiguities are charged under X, not here.",
                   ["son55:E004", "son55:E005", "son55:E020", "opus:O01"], ["sol:E003"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Prompts, encoder, k and edits shown, but link use at retrieval "
                   "(caption vs §3.4), embedding refresh after evolution, the mismatched B.2 prompt and unlisted merge/prune "
                   "actions leave the chain ambiguous; in-place overwrite with no versioning/rollback.",
                   ["son55:E006", "son55:E007", "son55:E025", "son55:E026", "sol:E010"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Standard LoCoMo QA with lexical metrics and per-category "
                               "reporting, but no judge/human answer check, DialSim F1 < 4, the text's Multi-Hop claims cite "
                               "Temporal-column values (opus:O01, opus:O02), and baseline rows are duplicated across backbones "
                               "and across metric tables (opus:O03–O05) — the reported numbers are not reliably attributed.",
                               ["son55:E024", "son55:E015", "sol:E005", "opus:O01", "opus:O02", "opus:O03", "opus:O04",
                                "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. w/o LG&ME and w/o ME rows show large effects, but one "
                             "backbone, one run, no w/o-LG-with-ME, no memory-off/raw-RAG at equal k, no Mem0, baselines not "
                             "tuned like A-Mem.", ["son55:E010", "son55:E021", "sol:E003"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Memory is built from conversation content, never from "
                           "questions/answers (no label leakage), and a second dataset is used; but k is tuned per category on "
                           "the evaluated data (opus:O06) and DialSim TV content contamination is unaddressed.",
                           ["son55:E008", "son55:E009", "son55:E023", "sol:E006", "opus:O06"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): total QA count and losing categories reported; authors "
                              "state no error bars; per-category counts missing.",
                              ["son55:E018", "son55:E022", "sol:E007"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Read-time tokens per question, ~1,200 tokens and <$0.0003 per "
                        "memory operation, latency, and storage/retrieval-time scaling are reported (opus:O07), so the write cost "
                        "per operation is at least stated; gaps: no total write-path accounting, the 85–93% reduction compares "
                        "read tokens only, baselines not budget-matched, and the scaling table counts embeddings only. Relevant "
                        "results with key gaps = 2; sol's 1 under-credits the per-operation write figures.",
                        ["son55:E016", "son55:E017", "son55:E019", "sol:E008", "sol:E009", "opus:O07"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v11 text incl. appendices and checklist (figures are images); in scope as a B-class "
                  "non-weight memory component whose stored notes are revised and reused (no outcome-feedback loop); all eight "
                  "items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "A parent card applies to the method's read-time operation (conditioning a frozen model on retrieved notes); "
                "outside_taxonomy is for no applicable card. son55's point (novelty is write-time) is recorded and carried by "
                "H04.", ["son55:E007", "sol:E002"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["adapt_via_conditioning", None]],
                "C03 dropped: no category holdout or equal-k flat retrieval (C03 steps 4–5), consistent with run precedent.",
                ["son55:E009", "son55:E010"], "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H01"], ["index_experience_for_reuse", "H04"]],
                "H04 agreed; H01 added at low fit because memory evolution is an explicit edit of existing entries' retrieval "
                "features (son55:E005).", ["son55:E005", "son55:E004"], "none"),
            res(X(p, "local:2502.12110-1"), *C(p, X(p, "local:2502.12110-1")), "son55", "unmet",
                "Same question in both seats; no dev split and k tuned to reach SOTA on the evaluated categories (opus:O06) "
                "= unmet; sol's 'partial' credited label-free memory construction, which is scored under E.holdout instead.",
                ["opus:O06", "son55:E009", "sol:E006"], "none; consistent with E.holdout=2"),
            res(X(p, "local:2502.12110-2"), *C(p, X(p, "local:2502.12110-2")), "same_supported_fact", "partial",
                "ID swap: sol's local-2 is statistics (unmet) and local-3 cost (partial); son55 the reverse. Final local-2 = "
                "cost (partial).", ["son55:E016", "sol:E008"], "none"),
            res(X(p, "local:2502.12110-3"), *C(p, X(p, "local:2502.12110-3")), "same_supported_fact", "unmet",
                "Same swap; final local-3 = statistics (unmet; authors state no error bars).",
                ["son55:E018", "sol:E007"], "none"),
            res(X(p, "local:2502.12110-4"), *C(p, X(p, "local:2502.12110-4")), "son55", "unmet",
                "ID collision: sol's local-4 (no external update gate/rollback, X, partial) kept as local-6; son55's local-4 "
                "(DialSim contamination) verified unmet.", ["son55:E023", "sol:E001"], "none"),
            res(X(p, "local:2502.12110-5"), *C(p, X(p, "local:2502.12110-5")), "son55", "unmet",
                "Mem0 is the named structured-memory competitor and is not evaluated.", ["son55:E003"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/F4"), *C(p, X(p, "rsi:index_experience_for_reuse/F4")), "son55",
                "unmet", "Failure present: neighbour attributes overwritten with unverified LLM output.",
                ["son55:E004", "son55:E005"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/F6"), *C(p, X(p, "rsi:index_experience_for_reuse/F6")), "son55",
                "partial", "Structure argued by t-SNE and one ablation, not by equal-budget recall analysis.",
                ["son55:E010"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/H04"), *C(p, X(p, "rsi:index_experience_for_reuse/H04")), "sol",
                "partial", "Content/index separation and local updates present; no gate, embedding sync or full-scale cost.",
                ["sol:E001", "sol:E009", "sol:E010"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/H04.step5"), *C(p, X(p, "rsi:index_experience_for_reuse/H04.step5")),
                "son55", "partial", "Ablation and scaling exist; scaling counts embeddings only; no variance or holdout.",
                ["son55:E010", "son55:E019"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/S2"), *C(p, X(p, "rsi:index_experience_for_reuse/S2")), "son55",
                "unmet", "Writes admitted on the LLM's own output; no external check.", ["son55:E004"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/S3"), *C(p, X(p, "rsi:index_experience_for_reuse/S3")), "son55",
                "met", "Raw content fixed; index-like attributes generated and revised separately.", ["son55:E005"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/S4"), *C(p, X(p, "rsi:index_experience_for_reuse/S4")), "son55",
                "met", "Top-k retrieval with read-token length reported; k sensitivity shows plateau.",
                ["son55:E016", "son55:E007"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/S5"), *C(p, X(p, "rsi:index_experience_for_reuse/S5")), "son55",
                "partial", "Structure-removal ablation on one backbone; no memory-off at equal k.", ["son55:E010"], "none"),
            res(X(p, "rsi:index_experience_for_reuse/S6"), *C(p, X(p, "rsi:index_experience_for_reuse/S6")), "son55",
                "partial", "Evolution is local to top-k neighbours; per-insert LLM calls not totalled.",
                ["son55:E005", "opus:O07"], "none"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "sol's 3 credits content/index separation; the load-bearing assumption (unverified neighbour rewrites help) is "
                "unargued and the paper's stated category prediction is contradicted by its own table (opus:O01).",
                ["son55:E005", "opus:O01"], "-5.0 vs sol value"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "Beyond son55's lexical-metric/DialSim points, Opus verified column mis-citation (opus:O01–O02) and duplicated "
                "baseline rows (opus:O03–O05); the numbers' attribution is not reliable enough for 3.",
                ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05"], "-2.5 vs sol value"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "resolved", "rating": 2},
                "Per-operation write tokens/$/latency are stated (opus:O07), so cost is relevant-with-gaps, not minimal; the "
                "read-only reduction claim and missing totals keep it at 2.", ["opus:O07", "son55:E016", "sol:E008"],
                "+1.25 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason (baseline rows)",
             "seat_values": {"sol": "not noticed", "son55": "not noticed"},
             "final_value": "ReadAgent rows for Qwen2.5-3b and Llama-3.2-3b are identical in Table 1, and the same values "
                            "reappear in Table 5's Llama-3.2-3b ReadAgent ROUGE row.",
             "reason": "Data-integrity defect in baseline reporting missed by both seats.",
             "evidence_ids": ["opus:O03", "opus:O04", "opus:O05"], "score_impact": "none (E.measurement=2 resolution)"},
            {"field_path": "claims / ratings.E.measurement.reason (category attribution)",
             "seat_values": {"sol": "main-text 2x Multi-Hop claim flagged (sol:E005)", "son55": "claim quoted without check"},
             "final_value": "Appendix A.3 also cites Temporal-column ROUGE-L/METEOR/SBERT values as Multi-Hop (opus:O02); the "
                            "Multi-Hop vs Temporal attribution in text is unreliable throughout.",
             "reason": "sol caught the main-text instance only; son55 none.",
             "evidence_ids": ["opus:O01", "opus:O02", "sol:E005"], "score_impact": "none"},
            {"field_path": "expectations[local:2502.12110-*] numbering",
             "seat_values": {"sol": "1 holdout, 2 statistics, 3 cost, 4 gate/rollback",
                             "son55": "1 holdout, 2 cost, 3 statistics, 4 contamination, 5 Mem0"},
             "final_value": "son55 numbering kept; sol's gate/rollback question renumbered local-6 (partial).",
             "reason": "A4 collisions; recorded once here in addition to the per-field resolutions.",
             "evidence_ids": ["sol:E001", "son55:E023"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text, appendices and checklist first. Provisional: in scope (B "
                                                   "memory component, no outcome feedback); G2 M2 X2 Em2 Ec2 Eh2 Es1 Ecost2; "
                                                   "noticed Multi-Hop/Temporal text-table mismatch, duplicated ReadAgent rows, "
                                                   "k tuned on test categories.",
            "integrity_checks": "sol a2 and son55 a1 on 2502.12110v11, sha 69e17ff1…; hashes equal conflicts.json; all seat "
                                "quotes verbatim.",
            "core_claim_check": "Table 1 GPT-4o-mini: A-Mem Multi-Hop 27.02 vs 26.65/25.02, Temporal 45.85 vs 25.52/18.41; "
                                "GPT-4o loses Single-Hop (48.43 vs 61.56) and Adversarial (36.35 vs 52.61). Ablation 9.65→"
                                "21.35→27.02 (Multi-Hop) verified.",
            "retention_check": "Failure denominators: 7,512 QA total, per-category counts absent. Selection vs test: k tuned on "
                               "evaluated categories. Extra budget: three LLM calls per insertion, uncosted in total. 'Kept "
                               "evolved notes' beat bare notes in one run on one backbone.",
        },
    }
    return S


def batch_notes():
    return [
        "Seat inputs per overrides.json: sol a1 for 2502.05907 (pre-exposure record retained), sol a2 (clean re-review on the "
        "identical pinned package) for the other four; son55 a1 for all. Hashes equal conflicts.json seat_record_hashes.",
        "2502.05907 (EvolvingAgent): both seats' out_of_scope independently confirmed under A3 bullet 1 — planner LoRA and "
        "world-model gradient updates; the experience pool feeds fine-tuning/replay only.",
        "Rating disputes resolved: 2502.07373 M,Ecost→sol (62.5; sol 62.5, son55 58.75); 2502.11448 M,Em,Eh→son55 (52.5; "
        "62.5/52.5); 2502.11799 G,X,Eh,Es→sol, Em,Ecost→son55 (55.0; 50.0/67.5); 2502.12110 M,Em,Ecost→son55 (48.75; "
        "55.0/48.75).",
        "Table-Critic (Δ17.5): resolved item by item; the largest swing (E.cost 1 vs 3) is settled by recomputation — output "
        "2.04M reconciles Table 4 exactly. Retained-tree evidence is 1.1/1.8 points, same stream, one run.",
        "Opus-found reporting defects (no extra score impact beyond resolutions): EvoFlow MBPP cost mis-sum flips the MBPP cost "
        "ranking; AGrail Table 3 vs Table 9 (84.1 vs 74.1) and transfer below base; A-Mem duplicated ReadAgent rows and "
        "Multi-Hop/Temporal mis-citation; Table-Critic Δ-rate denominators mislabelled in prose.",
        "Local expectation ID collisions/swaps in 4 papers renumbered; hidden collisions recorded as shared corrections.",
        "Card revision proposals (stage end, not applied): H17 wording for offline multi-design populations (sol); H16 weak-gate "
        "variant (son55); H01 label-free guard memories (son55); H00/H01 boundary for append-mostly tree stores (Opus: H00); "
        "H04 content-triggered vs outcome-gated restructuring (son55).",
        "Material requests (not blocking): pinned originals of AFlow/ADAS, GuardAgent/Conseca, Buffer-of-Thoughts-type template "
        "libraries, Mem0 would let G items check neighbour characterisations.",
    ]
