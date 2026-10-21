"""Opus rulings for r04b a1 (data only; consumed by _build.py)."""
import copy


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

    def dmatch(s, p, main, sub, **upd):
        for m in seat(s, p)["domain_pattern"]["matches"]:
            if m["main"] == main and m.get("sub") == sub:
                m2 = prefix(copy.deepcopy(m), s)
                m2.update(upd)
                return m2
        raise KeyError((s, p, main, sub))

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev, "none (expectations are not scored directly)")

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    NOSCORE = "none (patterns never score)"

    # =========================================================== 2506.07398 G-Memory
    p = "2506.07398"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "surpasses the best-performing single-/multi-agent memory baselines by an average of", "§5.2 Takeaway 1",
                    "Prose says G-Memory beats the best baselines by 6.8 / 5.5 on average (AutoGen / MacNet, Qwen-2.5-7b); Table 3 "
                    "shows 6.80 and 5.47 are the gains over No-memory (opus:O02, opus:O04)."),
            opus_ev(p, "O02", "45.10 ↑6.80", "Table 3, AutoGen / G-Memory Avg. (whitespace-normalised)",
                    "AutoGen Qwen-7b: G-Memory avg 45.10, +6.80 over No-memory 38.30."),
            opus_ev(p, "O03", "41.49 ↑3.19", "Table 3, AutoGen / Generative Avg. (whitespace-normalised)",
                    "Best AutoGen baseline (Generative) avg 41.49 → G-Memory margin over best baseline is +3.61, not 6.8."),
            opus_ev(p, "O04", "38.17 ↑5.47", "Table 3, MacNet / G-Memory Avg. (whitespace-normalised)",
                    "MacNet Qwen-7b: G-Memory avg 38.17, +5.47 over No-memory 32.70."),
            opus_ev(p, "O05", "35.77 ↑3.06", "Table 3, MacNet / MetaGPT-M Avg. (whitespace-normalised)",
                    "Best MacNet baseline (MetaGPT-M) avg 35.77 → margin over best baseline is +2.40, not 5.5."),
            opus_ev(p, "O06", "interactions offer a slightly greater impact", "§5.4 Ablation Study",
                    "Inverted conclusion: interactions-only (insights removed) drops 4.47 / 3.82 while insights-only drops 3.95 / "
                    "3.39 (Table 2, recomputed), so removing insights hurts more; the prose credits interactions."),
            opus_ev(p, "O07", "Collectively, we employ 1-hop expansion and", "§5.4 Sensitivity Analysis",
                    "Hop count and k are fixed after sensitivity sweeps on the same benchmarks and MAS that are reported; M is "
                    "set per setting from {2,3,4,5} (§5.1) with no stated selection data."),
            opus_ev(p, "O08", "and receiving environmental feedback, including execution status", "§4.3",
                    "Write-time status Ψ comes from the environment; for HotpotQA/FEVER this is label-derived (EM vs gold) and it "
                    "is computed on the same stream that is scored."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Frozen LLMs in a host MAS are conditioned on retrieved insights and sparsified past trajectories with no "
                      "parameter updates (adapt_via_conditioning). C03 not assigned under the run convention (r03a A-MEM, r03b "
                      "Dynamic Cheatsheet): no category-level holdout and no equal-budget flat-retrieval control (C03 steps 4–5); "
                      "the hierarchical store organisation that is the contribution is carried by domain H04. "
                      "heterogeneous_decomposition (sol) not kept: the insight/interaction split is a multi-granularity index "
                      "design, not a partition of a resource by an empirically characterised property.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "index_experience_for_reuse", "H04"),
                        dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2506.07398-1"): "local:2506.07398-2",
                    ("son55", "local:2506.07398-2"): "local:2506.07398-1"},
            overrides={"rsi:index_experience_for_reuse/F3": {
                "status": "unmet",
                "reason": "Opus final (son55 convention: unmet = failure mode present). The three-tier store is written from the "
                          "same benchmark queries that are scored, with label-derived status on QA (opus:O08); no separate "
                          "construction stream or frozen-store evaluation. sol's own reason (no frozen store / new-task split) "
                          "describes the failure as present; its 'partial' under-states it."}}),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O03", "opus:O05"]), "C2", ["opus:O06"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Later queries read graph entries written after earlier queries (case study: a different ALFWorld "
                                   "query retrieved), and the No-memory host MAS is a store-off control in all nine MAS×backbone "
                                   "settings. Construction stream = evaluation stream (prequential), label-derived status on QA, "
                                   "ALFWorld trial protocol undefined; no frozen-store or held-out evaluation → not transfer/improver. "
                                   "Same level as in-stream memory precedents (r03a A-MEM, r03b Dynamic Cheatsheet).",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single runs: on five benchmarks × three host MAS × three backbones the "
                                         "plug-in raises scores over No-memory (avg +5.5 to +10.7) and over author-adapted memory "
                                         "baselines by smaller margins (e.g. Qwen-7b avg +3.61 AutoGen, +2.40 MacNet vs the best "
                                         "baseline, not the 6.8/5.5 stated in §5.2). Both tiers contribute on two benchmarks; "
                                         "insights matter slightly more than the prose says. Not reproduced.",
            "unresolved": ["No held-out stream or order control; hop/k/M chosen on reported benchmarks (opus:O07).",
                           "No sample sizes, repeats or intervals.",
                           "Two prose/table mismatches (opus:O01, opus:O06); Table values used."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The non-weight object (MAS memory) and its stated bottleneck are concrete and "
                   "the lineage is laid out, but the closest neighbour is ExpeL, whose insight prompts G-Memory adapts (Appendix C "
                   "credit), and ExpeL / A-Mem / Mem0 are distinguished only in prose (son55:E016); the 'flat vs hierarchical' "
                   "residue is never tested and the 10× token premise rests on an unreadable figure. Adapted-baseline "
                   "degradations (son55:E007) are author re-implementations, not an independent diagnosis. Consistent with "
                   "A-MEM (r03a) and Dynamic Cheatsheet (r03b) G=2.",
                   ["son55:E002", "son55:E003", "son55:E007", "son55:E016", "sol:E008"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Retrieve → hop-expand → upward insights / downward LLM-sparsified "
                   "trajectories → role projection → three-level write is reconstructable from equations and prompts and makes "
                   "checkable predictions (role-specific delivery matters; over-retrieval hurts) that are partly tested.",
                   ["son55:E001", "son55:E004", "son55:E008", "son55:E009"]),
            "X": R("resolved", 2, "Opus sides with son55. Retrieval and write steps are explicit, but retention governance is thin: "
                   "every query (failed or resolved) is written, the merge prompt has no stated trigger, there is no versioning, "
                   "retirement or rollback, and invocation order/initial state are unspecified. sol's 3 credits sensitivity "
                   "analysis (an E item) to execution. Same as A-MEM (r03a) / Dynamic Cheatsheet (r03b) X=2.",
                   ["son55:E004", "son55:E015", "son55:E009"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55 and adds two reporting errors. Benchmark metrics (success, "
                               "progress rate, EM) are standard, but the prose claims a 6.8 / 5.5 average margin over the best "
                               "baselines where Table 3 gives +3.61 / +2.40 (opus:O01–O05), the ablation prose inverts which tier "
                               "matters more (opus:O06), the AutoGen host contains a reference-standard agent and the ALFWorld "
                               "multi-trial protocol is undefined. sol's 3 did not register the mismatches.",
                               ["son55:E017", "son55:E012", "son55:E013", "opus:O01", "opus:O02", "opus:O03", "opus:O04",
                                "opus:O05", "opus:O06"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. No-memory control in every setting, six author-adapted "
                             "alternative memories and a two-tier ablation on two benchmarks; no equal-budget flat store, no "
                             "role-projection / sparsifier / query-graph ablation, and best-baseline margins are 1–4 points per "
                             "cell in single runs.",
                             ["son55:E006", "son55:E008", "son55:E018", "opus:O03", "opus:O05"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Memory is built from the scored queries with label-derived "
                           "status on QA (opus:O08), hop/k/M are fixed on the reported benchmarks (opus:O07), the AutoGen host has a "
                           "reference-standard agent, no order control or contamination check; breadth over 5 benchmarks × 3 "
                           "backbones only partly offsets.",
                           ["son55:E004", "son55:E005", "son55:E013", "son55:E014", "opus:O07", "opus:O08"]),
            "E.statistics": R("not_reported", 0, "Opus sides with sol under the frozen A2 ladder: rung 1 needs reported sample sizes "
                              "plus negative results; G-Memory reports neither N per benchmark nor repeats, seeds, intervals or "
                              "tests (son55 itself infers N from percentages). Baseline negative deltas and direction consistency "
                              "across nine settings are not a substitute for the missing statistics.",
                              [], [], ["§5.1–5.5 text, Tables 1–4 (all cells), Figures 3–7 captions, Appendix A.1–A.4 "
                                       "(datasets, metrics, MAS setups), Appendix B.1–B.3, Appendix C/D: searched for sample "
                                       "counts, seeds, repeats, variance, intervals, significance — none reported."]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Overall-system token cost vs performance is plotted (Fig 3/7) and "
                        "quoted for PDDL+AutoGen (1.4×10^6 vs MetaGPT-M 2.2×10^6); whether relevance-rating, sparsifier, insight "
                        "and projection calls are included is not stated; no latency or dollars.",
                        ["son55:E011", "sol:E007"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendices A–D (figure values not in text; no rating depends on them beyond what "
                  "the prose states); in scope (A): non-weight MAS memory written after each query and read on later queries; "
                  "all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "Later queries read entries written from earlier queries, and the No-memory host is a store-off control in all nine "
                "settings; that is retained at stream level under EVIDENCE.md (held-out is preferred, not required). sol's "
                "concern (no independent new-task split) is scored in E.holdout=1, not by lowering the level. Same as in-stream "
                "memory precedents (r03a A-MEM, r03b Dynamic Cheatsheet).",
                ["son55:E001", "son55:E006", "son55:E014", "opus:O08"], "none (evidence_level is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "C03 dropped (no category holdout, no equal-budget flat-retrieval control; run convention r03a/r03b). "
                "heterogeneous_decomposition dropped: tiers are an index design without a measured heterogeneity, carried by H04.",
                ["son55:E001", "son55:E008", "sol:E004"], NOSCORE),
            X(p, "local:2506.07398-1", *C(p, "expectations[local:2506.07398-1].status"), "revised",
              "local-1 = cost question → partial (sol local-1 + son55 local-2 merged); son55's local-1 (statistics) renumbered "
              "local-2 = unmet",
              "A4 collision: same ID, different questions. sol local-1 asks the cost question; son55 local-1 asks the statistics "
              "question and files cost as local-2 with the same 'partial'.", ["sol:E007", "son55:E011", "son55:E017"]),
            X(p, "local:2506.07398-2", *C(p, "expectations[local:2506.07398-2].status"), "same_supported_fact",
              "son55 local-2 (cost, partial) merged into local-1; final local-2 = son55's statistics question = unmet",
              "son55 local-2 is the cost question sol answered as local-1 with the same status (partial).",
              ["son55:E011", "sol:E007"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55", "unmet",
              "Verified: no overlap/contamination or order analysis between stored and scored queries.", ["son55:E014", "son55:E010"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55", "partial",
              "Verified: Voyager/MemoryBank/Generative are retrieval-style alternatives, but no long-context or flat store at equal "
              "budget.", ["son55:E012", "son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55", "met",
              "Verified: same recipe on 5 benchmarks / 3 domains / 3 MAS / 3 backbones; only k, M, hop are picked per setting "
              "from small sets (noted under E.holdout).", ["son55:E006", "son55:E017", "opus:O07"]),
            X(p, "rsi:abstract_experience_into_guidance/S2",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"), "son55", "met",
              "Verified: Appendix C insight prompt contrasts a failed and a successful trajectory.", ["son55:E004"]),
            X(p, "rsi:abstract_experience_into_guidance/S4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "son55", "partial",
              "Verified: a merge/consolidate prompt with a count limit exists, its trigger is never stated.", ["son55:E015"]),
            X(p, "rsi:index_experience_for_reuse/F3", *C(p, "expectations[rsi:index_experience_for_reuse/F3].status"), "son55",
              "unmet", "Failure mode fully present (store built from the scored stream, label-derived status on QA); unmet = "
              "present under son55's convention, and sol's reason describes the same fact.", ["son55:E004", "son55:E014", "opus:O08"]),
            X(p, "rsi:index_experience_for_reuse/S2", *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"), "son55",
              "unmet", "Verified: every completed query is written; no external test or threshold gates writes.",
              ["son55:E004", "son55:E005"]),
            X(p, "rsi:index_experience_for_reuse/S3", *C(p, "expectations[rsi:index_experience_for_reuse/S3].status"), "sol", "met",
              "Verified: query nodes index interaction graphs; insight nodes point to supporting-query sets — content and index "
              "are decoupled.", ["sol:E001", "sol:E002"]),
            X(p, "rsi:index_experience_for_reuse/S4", *C(p, "expectations[rsi:index_experience_for_reuse/S4].status"), "son55", "met",
              "Verified: k, hop, top-M, LLM relevance filter and sparsifier cap injected context; over-retrieval shown to hurt.",
              ["son55:E009", "son55:E018"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "son55",
              "partial", "Verified: No-memory store-off in all settings (but not a same-prompt empty store); tier removal on two "
              "benchmarks only.", ["son55:E006", "son55:E008"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G: closest neighbour (ExpeL, whose prompts are adapted) not compared; hierarchy-vs-flat residue untested.",
                ["son55:E016", "sol:E008"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.X: no write gate, trigger-less merge, no versioning/retirement/rollback.",
                ["son55:E004", "son55:E015"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: two prose/table mismatches plus reference-standard host agent and undefined trial protocol.",
                ["opus:O01", "opus:O06", "son55:E013"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", {"status": "not_reported", "rating": 0},
                "A2 ladder rung 1 requires reported sample sizes; none are given (son55 infers them).",
                ["son55:E017"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): three-tier non-weight MAS memory written after each query, read on "
                                                   "later ones. No-memory control in nine settings; margins over the best adapted "
                                                   "baseline are a few points; §5.2 overstates them; ablation prose inverted; "
                                                   "hyper-parameters picked on reported benchmarks; no N, repeats or intervals.",
            "integrity_checks": "Both seats a1 on 2506.07398v2, material sha 07751bdb…, input_hash de46e77b…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read §4–§5 and Tables 1–4; recomputed best-baseline margins (Table 3) and Table 2 averages "
                                "(AutoGen 63.335 vs 58.865 / 59.385; DyLAN 58.89 vs 55.07 / 55.50).",
            "rating_agreement": "4/8 identical (M, E.causality, E.holdout, E.cost) and re-checked; G→sol, X→son55, "
                                "E.measurement→son55, E.statistics→sol.",
            "expectation_renumbering": "son55 local-1 (statistics) → local-2; son55 local-2 (cost) merged into sol local-1.",
        },
    }

    # =========================================================== 2506.10484 ExpeRepair
    p = "2506.10484"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "The empirically best configuration, i.e., 15 stored insights and top-3 demonstration retrieval",
                    "§4.4 Answering RQ4", "The deployed k and insight cap are the argmax of sweeps on the same Lite/Verified scores "
                    "that are reported (selection on evaluation data)."),
            opus_ev(p, "O02", "PatchPilot Claude 3.5 Sonnet 45.3", "Table 1 (whitespace-normalised)",
                    "Several leaderboard baselines use the same Claude 3.5 Sonnet backbone as the 48.3 row (also SWE-agent, "
                    "Agentless-1.5), so the 3.5 row is backbone-matched though not re-run; the Claude 4 row has no matched baseline."),
            opus_ev(p, "O03", "a dual-agent architecture with experience banks to improve repair performance", "§3.3 Baselines",
                    "The paper's own description of a baseline with experience banks contradicts the gap premise that current "
                    "approaches treat each issue in isolation."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Frozen repair agents are conditioned on BM25-retrieved demonstrations and an appended insight list; no weights "
                      "change. C03 not assigned under the run convention: no category/repository-level holdout (C03 step 4); "
                      "BM25 vs embedding vs hybrid is a retriever comparison, not a simpler-conditioning baseline at equal budget.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03"),
                        dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2506.10484-1"): "local:2506.10484-4"},
            overrides={"local:2506.10484-1": {
                "status": "partial",
                "reason": "Opus revision of son55 'unmet'. The Claude 3.5 Sonnet row (48.3 / 57.2) has backbone-matched published "
                          "baselines (SWE-agent, Agentless-1.5, PatchPilot, opus:O02), though none re-run under one protocol; "
                          "only the Claude 4 headline (60.3 / 74.6) has no matched baseline. Partial, not unmet."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Per-repository memories written after each issue are read on later issues, and the same pipeline "
                                   "with the memory module off (42.3 / 50.4) isolates the store. Labels are self-generated (no gold "
                                   "tests), evaluation is prequential in dataset order with the first five issues counted; no "
                                   "frozen-store or held-out repository evaluation → not transfer/improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single run: on SWE-Bench Lite (300) and Verified, the same Claude 3.5 "
                                         "Sonnet pipeline resolves 6.0 / 6.8 points more issues with its per-repository dual "
                                         "memory than without it, mostly via episodic demonstrations (semantic memory adds 1.0–1.3 "
                                         "points, within plausible noise). SOTA standing holds only against published, un-rerun "
                                         "numbers; the Claude 4 headline is unmatched. Not reproduced.",
            "unresolved": ["No held-out repository or contamination audit.",
                           "k, insight cap, α and update set chosen on reported scores (opus:O01).",
                           "No repeats or intervals; semantic-memory effect is 4–5 issues."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The repository-level residue (recurring same-repo failures, environment "
                   "set-up for reproduction) is concrete, but the closest neighbour ExpeL already curates insights with near-identical "
                   "ADD/EDIT operations (son55:E020) and is distinguished only by domain, and the gap premise 'each issue in "
                   "isolation' is undercut by the paper's own description of OpenHands' experience banks (opus:O03). Not run, not "
                   "tested. Same anchor as G-Memory/A-MEM/Dynamic Cheatsheet G=2.",
                   ["son55:E019", "son55:E020", "son55:E021", "opus:O03", "sol:E013"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Feedback-bearing retrieval queries, corrected-failure demonstrations, "
                   "role-split insights and lexical-overlap reasoning for BM25 are explicit and yield predictions that are tested "
                   "(BM25 > dense; failure when no analogue exists).",
                   ["son55:E003", "son55:E009", "son55:E017"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Write rule, labels, ADD/REMOVE/EDIT with cap 15, per-role/per-repo "
                   "stores, trial counts, cold start and prompts are specified, and the update-operation set is ablated; missing "
                   "utility-based admission, versioning and rollback.",
                   ["son55:E001", "son55:E003", "son55:E004", "son55:E005", "son55:E011"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Hidden-test pass@1 is a credible verifier, memory labels are "
                               "not the gold tests, RSR is human-verified; all Table 2 ESR/RSR deltas recompute exactly. Not 4: "
                               "annotator protocol unstated and baselines are copied from leaderboards.",
                               ["son55:E003", "son55:E024", "son55:E006", "sol:E008"]),
            "E.causality": R("resolved", 3, "Both seats 3; re-checked. Same-pipeline memory-off, episodic-off and semantic-off "
                             "ablations on both benchmarks plus retriever and update-operation ablations; lacks a compute-matched "
                             "or random-demonstration control and a no-memory longitudinal curve; the SOTA table is not controlled.",
                             ["son55:E006", "son55:E007", "son55:E009", "son55:E011", "son55:E013"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. Memory is built from the scored issues in dataset order with the seed "
                           "issues counted, k / insight cap / α / update set are chosen as the argmax on the reported scores "
                           "(opus:O01, son55:E010), one ordering, contamination argued not measured. Label-free writes prevent gold "
                           "leakage but this is the same situation rated 1 for Dynamic Cheatsheet (r03b) and G-Memory (this batch); "
                           "son55's 2 credits label-freeness that the precedent already priced in.",
                           ["son55:E001", "son55:E002", "son55:E010", "son55:E012", "son55:E018", "opus:O01"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): Lite N=300 stated, negative/boundary cases reported, single "
                              "runs with no intervals; semantic-memory effect is 4–5 issues.",
                              ["son55:E025", "son55:E008", "son55:E017"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. USD per instance for all rows (1.89 / 1.74 / 1.96 / 1.91) but "
                        "memory-off cost, seed-phase and summarize/update calls are not separated and baseline costs come from "
                        "different setups.",
                        ["son55:E014", "son55:E022", "sol:E010"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 (FSE) text; figure values and website prompts absent, no rating depends on them; in scope (A): "
                  "non-weight episodic/semantic memory written after each issue and read on later issues; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "Later issues read memories written from earlier ones and the same-pipeline memory-off ablation isolates the store; "
                "held-out evaluation is preferred, not required, by EVIDENCE.md. sol's concern is scored in E.holdout=1.",
                ["son55:E001", "son55:E006", "son55:E003"], "none (evidence_level is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "C03 dropped: no category/repository holdout; retriever comparison is not an equal-budget simpler-conditioning "
                "baseline (run convention).", ["son55:E009", "sol:E006"], NOSCORE),
            X(p, "local:2506.10484-1", *C(p, "expectations[local:2506.10484-1].status"), "revised",
              "local-1 = son55's matched-baseline question → partial; sol's cost question renumbered local-4 = partial",
              "A4 collision: sol local-1 is the cost question, son55 local-1 the baseline-matching question. Opus revises son55's "
              "answer to partial because Claude-3.5 baselines are backbone-matched (opus:O02).",
              ["son55:E013", "son55:E015", "opus:O02", "sol:E009"]),
            X(p, "local:2506.10484-2", *C(p, "expectations[local:2506.10484-2].status"), "son55", "unmet",
              "Verified: no repeats or intervals (sol filed the same fact under E.statistics, not as an expectation).",
              ["son55:E008", "son55:E025"]),
            X(p, "local:2506.10484-3", *C(p, "expectations[local:2506.10484-3].status"), "son55", "unmet",
              "Verified: k, cap, retrieval method and α chosen on reported scores (opus:O01).", ["son55:E010", "son55:E012", "opus:O01"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "son55", "met",
              "Verified: memory / episodic / semantic each toggled off in the identical pipeline.", ["son55:E006", "son55:E007"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55", "unmet",
              "Verified: contamination stated and argued away, not audited.", ["son55:E018"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55", "partial",
              "Verified: BM25 / embedding / hybrid compared; no longer-context or cross-repository control.", ["son55:E009", "son55:E010"]),
            X(p, "rs:adapt_via_conditioning/RE-4", *C(p, "expectations[rs:adapt_via_conditioning/RE-4].status"), "sol", "met",
              "Verified: each memory, the retriever and the update-operation set are ablated separately.", ["sol:E006", "sol:E007"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55", "partial",
              "Verified: k and insight-count sweeps and a stated no-analogue failure; no coverage/gap analysis.",
              ["son55:E012", "son55:E017"]),
            X(p, "rsi:abstract_experience_into_guidance/S3",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "son55", "met",
              "Verified: insights are written from trajectories with execution results of self-generated tests.", ["son55:E003"]),
            X(p, "rsi:abstract_experience_into_guidance/S5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S5].status"), "son55", "partial",
              "Verified: ADD/REMOVE/EDIT decided by an LLM prompt, not by measured marginal effect; no rollback.", ["son55:E004"]),
            X(p, "rsi:index_experience_for_reuse/F4", *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"), "son55",
              "partial", "Failure partly present: writes gated by execution of self-generated tests, but reproduction is LLM-judged.",
              ["son55:E003"]),
            X(p, "rsi:index_experience_for_reuse/S4", *C(p, "expectations[rsi:index_experience_for_reuse/S4].status"), "son55", "met",
              "Verified: top-3 BM25; k=5 shown to interfere.", ["son55:E009", "son55:E012"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "son55", "met",
              "Verified: same-pipeline store removal on both benchmarks.", ["son55:E006", "son55:E007", "son55:E008"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G: ExpeL near-identical maintenance only distinguished by domain; isolation premise undercut by OpenHands.",
                ["son55:E020", "opus:O03"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: prequential stream + test-tuned hyper-parameters, same as Dynamic Cheatsheet precedent.",
                ["son55:E002", "opus:O01"], "−2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): per-repo episodic + semantic memory from self-generated test signals "
                                                   "(no gold leakage). Clean same-pipeline store-off/component/update-op ablations; "
                                                   "all ESR/RSR deltas recompute. Hyper-parameters and α chosen on reported "
                                                   "benchmarks; single runs; leaderboard baselines uncontrolled.",
            "integrity_checks": "Both seats a1 on 2506.10484v2, material sha a8344683…, input_hash de46e77b…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read §2–§5; recomputed Table 2 ESR/RSR drops (Lite 20.7/21.0, 14.0/13.7, 4.7/6.4; Verified "
                                "25.0/25.2, 16.2/17.6, 6.4/5.6) and k=0 / 0-insight sensitivity endpoints against Table 2.",
            "rating_agreement": "6/8 identical and re-checked; G→sol, E.holdout→sol.",
            "expectation_renumbering": "sol local-1 (cost) → local-4.",
        },
    }

    # =========================================================== 2506.14234 Xolver
    p = "2506.14234"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "while the QWQ-32B backbone sees gains from 78.1 to 89.9 on AIME’24 and from 63.4 to 76.2 on LiveCodeBench",
                    "§3.2 Strong Gains", "89.9 and 76.2 are the Xolver(–) QwQ numbers in Table 1; with son55:E013 (o3-mini-medium "
                    "LCB 79.6 is also the (–) value) the paragraph mixes variants twice."),
            opus_ev(p, "O02", "90.9 ± \\pm 1.1", "Appendix D.3 Table 5, o3-mini-medium LiveCodeBench (whitespace-normalised)",
                    "Shuffled-order mean 90.9 vs 87.3 ± 0.4 in Tables 1/4 (opus:O04): +3.6 points, many SDs away."),
            opus_ev(p, "O03", "83.6 ± \\pm 1.6", "Appendix D.3 Table 5, QwQ-32B LiveCodeBench (whitespace-normalised)",
                    "Shuffled-order mean 83.6 vs 79.2 ± 0.5 in Tables 1/4 (opus:O05): +4.4 points; o3-mini-medium AIME’24 92.2 vs "
                    "93.8, AIME’25 91.0 vs 89.4 also differ."),
            opus_ev(p, "O04", "87.3 ± \\pm 0.4", "Appendix D.2 Table 4 (whitespace-normalised)", "Default-order Xolver(+) o3-mini-medium LCB."),
            opus_ev(p, "O05", "79.2 ± \\pm 0.5", "Appendix D.2 Table 4 (whitespace-normalised)", "Default-order Xolver(+) QwQ-32B LCB."),
            opus_ev(p, "O06", "indicating that its performance is largely stable regardless of data ordering", "§4 Data Shuffling",
                    "The 'minimal variation' conclusion is stated against shuffle means that differ from the main results by up to "
                    "4.4 points; the order study therefore does not establish order-insensitivity as claimed."),
            opus_ev(p, "O07", "93.8 ± \\pm 0.3", "Appendix D.2 Table 4 (whitespace-normalised)",
                    "SD 0.3 over 16 runs on 30-question AIME’24 (one question = 3.3 points); the dispersion statistic is not "
                    "defined beyond 'standard deviation within ~1%'."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Each problem is solved by conditioning frozen agents on BM25-retrieved exemplars (first iteration) and a "
                      "per-query shared memory of judged responses; Xolver(+) appends the top-judged solution to the episodic "
                      "corpus. C03 not assigned (run convention): no category holdout or contamination audit (C03 step 4).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03")],
            "unassigned": copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2506.14234-1"): "local:2506.14234-4",
                    ("sol", "local:2506.14234-2"): "local:2506.14234-3"},
            overrides={}),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01"]), "C2", ["opus:O02", "opus:O03", "opus:O06"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Xolver(+) appends top-judged solutions to the episodic corpus and later problems retrieve them; "
                                   "the same scaffold with a static corpus, Xolver(–), isolates the write-back (+3.5 average). "
                                   "Write-back is on the evaluated stream (prequential, LLM-judged, no gold) → not transfer/improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: a judge-driven multi-agent scaffold lifts math and code benchmarks well "
                                         "above the same backbones' LongCoT and above reproduced agent baselines at higher token "
                                         "cost; writing solved problems back to the episodic corpus adds 1.5–7.7 points in-stream. "
                                         "Most of the gain is per-problem multi-agent iteration, not retained experience; the "
                                         "order-robustness claim is not established (opus:O06). Not reproduced.",
            "unresolved": ["Retrieval corpora (OpenMathReason, cp-algorithms) not audited against test sets.",
                           "Shuffle means inconsistent with main results by up to 4.4 points.",
                           "GPT-4o math grading unvalidated; headline comparisons not compute-matched."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The isolation premise is already addressed by CheatSheet and Search-o1, "
                   "which are run as baselines; the residual (holistic integration) is integration-level.",
                   ["son55:E002", "son55:E023", "son55:E024"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Algorithm and prompts separate per-query refinement from persistent "
                   "episodic memory and yield tested predictions (self-judge bias, budget-controlled agents × iterations, order).",
                   ["son55:E003", "son55:E004", "son55:E015", "son55:E016"]),
            "X": R("resolved", 2, "Opus sides with son55. The inference loop is fully specified, but the retained step is a bare "
                   "append of the top-judged entry, scored by LLM-estimated correctness (math) or LLM-simulated tests (code), with "
                   "no threshold, dedup, versioning, retirement or rollback. sol's X reason lists experiments (tasks, backbones, "
                   "ablations), which are E evidence.",
                   ["son55:E003", "son55:E005", "son55:E006", "son55:E021"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55 and adds findings. Code uses benchmark tests, but math accuracy "
                               "is graded by GPT-4o without validation, §3.2 twice attributes Xolver(–) numbers to the gains it "
                               "describes (son55:E013, opus:O01), and Table 5 shuffle means differ from Tables 1/4 by up to 4.4 "
                               "points while described as minimal variation (opus:O02–O06); the dispersion statistic is undefined.",
                               ["son55:E007", "son55:E013", "opus:O01", "opus:O02", "opus:O03", "opus:O06", "opus:O07"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. For the retained claim, Xolver(+) vs (–) is a same-scaffold "
                             "store-update control; external/self/no retrieval, component removals, self- vs external judge and a "
                             "budget-controlled agents × iterations study address the main alternatives, and agent baselines are "
                             "re-run on the same backbones. Not 4: no equal-token self-consistency baseline and component values "
                             "only in a figure. sol's 2 discounts the store control for the scaffold's unmatched budget, which "
                             "A2 assigns to E.cost.",
                             ["son55:E012", "son55:E014", "son55:E015", "son55:E016", "son55:E010"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. Xolver(+) writes back the evaluated problems; the external corpora "
                           "(OpenMathReason for math, cp-algorithms for code) feed every variant and are not audited for overlap "
                           "with GSM8K/MATH/AIME/LCB (son55:E011, son55:E022); defaults m=3, I=2 have no stated selection data; "
                           "and the order study that son55 credits reports means inconsistent with the main results "
                           "(opus:O02, opus:O03), so it does not establish order-independence. Recency of AIME’25 / LCB v5 is real "
                           "but partial. Same tier as the other in-stream memories in this batch.",
                           ["son55:E011", "son55:E017", "son55:E021", "son55:E022", "opus:O02", "opus:O03", "opus:O06"]),
            "E.statistics": R("resolved", 2, "Opus sides with son55 (A2 ladder): 16/32-run means with SD for the method and a 5-run "
                              "shuffle SD reach rung 2; rung 3 needs significance tests on the claims (only the reasoning-pattern "
                              "analysis has t-tests), baselines have no variance, GSM8K/Math-500 are single greedy runs, and the "
                              "SDs are undefined and inconsistent with Table 5 (opus:O07).",
                              ["son55:E008", "son55:E019", "son55:E009", "opus:O07"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Token usage is plotted per dataset and summarised as ~1.5× Search-o1 "
                        "tokens with O(mI) complexity, but the conclusion concedes substantially higher consumption, CheatSheet's "
                        "cost is argued not measured, no dollars/latency, planner/judge/verifier/debugger calls are not "
                        "itemised, and headline comparisons are not compute-matched. The fixed-budget agents × iterations study is "
                        "internal and is credited under E.causality.",
                        ["son55:E018", "son55:E020", "son55:E024", "sol:E011"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. appendices A–D (figure values not in text; component-ablation magnitudes are taken "
                  "only as directions); in scope (A): non-weight episodic corpus written after each solved problem and retrieved "
                  "later; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "Xolver(+) vs (–) is a same-scaffold store-update control on later problems; held-out preferred, not required. "
                "sol's no-independent-stream concern is scored in E.holdout=1.",
                ["son55:E012", "son55:E021", "son55:E017"], "none (evidence_level is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "C03 dropped (no category holdout, no contamination audit; run convention).", ["son55:E011", "sol:E012"], NOSCORE),
            X(p, "local:2506.14234-1", *C(p, "expectations[local:2506.14234-1].status"), "revised",
              "local-1 = son55's cost question → partial; sol's holdout question renumbered local-4 = unmet",
              "A4 collision: sol local-1 asks for a frozen-store evaluation on an independent stream; son55 local-1 is the "
              "compute-matching question. Both answers stand under their own questions.", ["son55:E015", "son55:E018", "sol:E010"]),
            X(p, "local:2506.14234-2", *C(p, "expectations[local:2506.14234-2].status"), "revised",
              "local-2 = son55's GPT-4o math-grading question → unmet; sol's statistics question merged into local-3",
              "A4 collision: sol local-2 is the statistics question (partial) that son55 filed as local-3 with the same answer.",
              ["son55:E007", "sol:E009"]),
            X(p, "local:2506.14234-3", *C(p, "expectations[local:2506.14234-3].status"), "same_supported_fact",
              "partial (son55 local-3 + sol local-2)", "Same statistics question, same status in both seats.",
              ["son55:E008", "son55:E019", "sol:E009", "sol:E010"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55", "unmet",
              "Verified: no overlap analysis between retrieval corpora and test sets.", ["son55:E011", "son55:E022"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55", "partial",
              "Verified: same-backbone agent baselines re-run, but no equal-token self-consistency/best-of-N.",
              ["son55:E010", "son55:E018"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55", "partial",
              "Verified: external vs self vs no retrieval; corpus coverage / C++-for-Python gap noted, not analysed.",
              ["son55:E011", "son55:E022"]),
            X(p, "rsi:index_experience_for_reuse/F3", *C(p, "expectations[rsi:index_experience_for_reuse/F3].status"), "son55",
              "unmet", "Failure present: (+) writes back the evaluated problems; the shuffle study does not remove it.",
              ["son55:E021", "son55:E017"]),
            X(p, "rsi:index_experience_for_reuse/F4", *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"), "son55",
              "unmet", "Failure present: the model's own top-judged output is admitted; self-judge bias is shown by the authors.",
              ["son55:E003", "son55:E016"]),
            X(p, "rsi:index_experience_for_reuse/H03", *C(p, "expectations[rsi:index_experience_for_reuse/H03].status"), "sol",
              "partial", "Verified: case store and retrieval explicit; admission relies on LLM-simulated judging.",
              ["sol:E001", "sol:E002"]),
            X(p, "rsi:index_experience_for_reuse/S2", *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"), "son55",
              "unmet", "Verified: top-ranked entry always written; no executable gate.", ["son55:E003", "son55:E005", "son55:E006"]),
            X(p, "rsi:index_experience_for_reuse/S4", *C(p, "expectations[rsi:index_experience_for_reuse/S4].status"), "son55",
              "partial", "Verified: fixed top-K at first iteration only; no relevance gate or K sweep.", ["son55:E011"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "son55",
              "met", "Verified: Xolver(–) static corpus vs (+) write-back, and retrieval-source ablation.",
              ["son55:E012", "son55:E014"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.X: retention is a bare append of the top-judged entry; sol's reason cites E evidence.",
                ["son55:E003", "son55:E021"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: unvalidated GPT-4o grading, two variant mix-ups, Table 5 vs Tables 1/4 inconsistency.",
                ["son55:E007", "opus:O01", "opus:O02", "opus:O03"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.causality: same-scaffold store-update control plus retrieval/component/judge/budget studies.",
                ["son55:E012", "son55:E015"], "+3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: unaudited external corpora and an order study contradicted by its own numbers.",
                ["son55:E011", "opus:O02", "opus:O06"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.statistics: run variance without significance tests or baseline variance → rung 2.",
                ["son55:E019", "opus:O07"], "−1.25 vs sol (5×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.cost: token ratio only vs one baseline; no dollars/latency/call itemisation; unmatched headlines.",
                ["son55:E018", "son55:E020"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A) via the episodic write-back only; most gain is per-problem "
                                                   "multi-agent iteration. (+) vs (–) isolates retention (+3.5 avg). LLM-estimated "
                                                   "math judging and LLM-simulated tests; GPT-4o grading; corpora unaudited; prose "
                                                   "variant mix-ups; Table 5 shuffle means inconsistent with Table 1/4.",
            "integrity_checks": "Both seats a1 on 2506.14234v1, material sha 3d10a157…, input_hash de46e77b…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read §2–§4 and Appendix D; recomputed intro averages (91.6 = (93.8+89.4)/2; 94.05; +18.5; +7.15), "
                                "best-baseline margins (+12.7 AIME’25, +13.5 LCB), and Table 5 vs Table 4 differences.",
            "rating_agreement": "2/8 identical (G, M) and re-checked; X→son55, E.measurement→son55, E.causality→son55, "
                                "E.holdout→sol, E.statistics→son55, E.cost→sol.",
            "expectation_renumbering": "sol local-1 (holdout) → local-4; sol local-2 (statistics) merged into son55 local-3.",
        },
    }

    # =========================================================== 2507.02004 STELLA
    p = "2507.02004"
    adapt_sup = smatch("sol", p, "adapt_via_conditioning", sub_id=None, role="supporting", fit="weak",
                       reason="Opus: the Manager plans 'guided by its reasoning experience' from saved templates (conditioning a "
                              "frozen model on retained text), but the read/write rule is undescribed; C03 not assigned (no "
                              "schema learned upstream, no category holdout).")
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "rising from 14% to 26%", "Introduction",
                    "The 26% headline equals the 9× trial-budget point of Fig 2B, so the SOTA comparison (Fig 2A, 'top accuracy of "
                    "26%') pits a 9× budget against single-pass baselines; how trials are aggregated into one answer is never stated."),
            opus_ev(p, "O02", "with some modifications", "Methods, Q&A Benchmarks",
                    "The evaluation protocol follows Biomni/OriGene 'with some modifications' that are not described."),
            opus_ev(p, "O03", "STELLA attained a top accuracy of 26%", "Results",
                    "'Top accuracy' — the reported number is the best budget setting, not a fixed-budget comparison."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Executed operation: a Manager decomposes, a Dev agent emits executable Python run in conda environments, a "
                      "Critic loops on intermediate results, and a Tool Creation agent builds tools for capability gaps "
                      "(decompose_and_delegate / C25, matching the r01a OS-Copilot and cal-h1 LATM rulings for tool-forging "
                      "systems). The Template Library adds a weakly specified conditioning channel (adapt_via_conditioning, sub null).",
            "matches": [smatch("son55", p, "decompose_and_delegate"), adapt_sup],
            "executes_pattern": True, "resolves_problem": "unresolved",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07"),
                        dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
            "unassigned": copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "revision_proposals": [],
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"]), "son55") + [{
            "rs_main": "adapt_via_conditioning", "rs_sub": None,
            "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H00"},
            "operation_correspondence": "Successful workflows distilled into templates that later condition the Manager's plan.",
            "conditions_differences": "RS card wants a conditioning-off ablation and holdout; domain card wants contrast, grounding "
                                      "and a keep-gate. None is described or tested in v1.",
            "evidence_ids": ["son55:E001", "son55:E004", "sol:E001"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2507.02004-2"): "local:2507.02004-4",
                    ("sol", "local:2507.02004-3"): "local:2507.02004-5"},
            overrides={}),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Accuracy rises with the number of trials (1×→9×) averaged over three runs, but nothing isolates "
                                   "retained templates or tools from repeated sampling or retry; no store-off or equal-trial control.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, figure-only values: with up to 9× trials and a Claude 4 Sonnet + Gemini 2.5 "
                                         "Pro multi-agent setup, STELLA scores higher than listed single-pass LLMs and Biomni on a "
                                         "50-question HLE-Biomedicine set and 12.5% LAB-Bench subsets, and accuracy rises with "
                                         "trials. The author claim that the self-evolving Template Library / Tool Ocean causes the "
                                         "improvement is not supported by any isolating evidence. Not reproduced.",
            "unresolved": ["Trial protocol and answer aggregation undefined (opus:O01).",
                           "Whether ground-truth correctness feeds template/tool storage between trials.",
                           "No template/tool ablation, equal-trial baseline, cost or held-out set."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static curated toolsets are a real limitation and Biomni is the named "
                   "neighbour, but tool-forging/experience-library neighbours are not discussed and the binding of tool coverage is "
                   "not shown.", ["son55:E003", "son55:E013", "sol:E002"]),
            "M": R("resolved", 1, "Opus sides with son55. The mechanism is narrative: success criterion, template format and "
                   "retrieval, and how created tools are tested are never specified, so the problem-to-operation reasoning cannot "
                   "be reconstructed or turned into a distinguishing prediction (anchor 2 needs a specific mechanism). sol's 2 "
                   "credits the role split alone.", ["son55:E001", "son55:E002", "son55:E004"]),
            "X": R("resolved", 1, "Both seats 1; re-checked. Roles are named; admission, storage, versioning, retrieval, tool "
                   "testing and rollback are absent from the complete v1 text.", ["son55:E002", "son55:E004"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55. Benchmarks and the LAB-Bench abstention protocol are standard, "
                               "but numbers exist only as approximate figure readings, how multiple trials become one scored answer "
                               "is undefined (opus:O01), the protocol carries unspecified modifications (opus:O02), the headline "
                               "margin is 6 pp in the abstract and 8 pp in the introduction, and baseline provenance (re-run or "
                               "copied) is not stated.",
                               ["son55:E007", "son55:E010", "son55:E011", "opus:O01", "opus:O02", "opus:O03"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Baseline comparison and a trials-vs-accuracy curve only; no "
                             "template/tool ablation, no equal-trial or equal-backbone baseline.", ["son55:E005", "son55:E009", "son55:E012"]),
            "E.holdout": R("not_reported", 0, "Opus sides with son55. No development split is used, evolution and scoring happen on "
                           "the same questions, the trial protocol and any correctness feedback into stored templates/tools are "
                           "unstated, and no contamination discussion exists; no positive holdout evidence was found in the complete "
                           "text. Following Biomni's question sampling avoids author cherry-picking but is not holdout evidence.",
                           ["son55:E008", "son55:E015"], [],
                           ["Abstract, Introduction, Results (framework, self-evolving mechanisms, benchmark results), Conclusion, "
                            "Methods (Baselines, Q&A Benchmarks), Figure 1–2 captions: searched for development/held-out split, "
                            "separation of library construction from scoring, trial protocol, correctness feedback, contamination — "
                            "none reported."]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): HLE N=50 stated and three runs averaged, no spread, "
                              "intervals or tests; LAB-Bench subset sizes not stated.", ["son55:E006", "son55:E007", "sol:E008"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Budget is disclosed only as trial multiples (1×–9×) against "
                        "single-pass baselines; no tokens, calls, tool-creation or dollar cost.", ["son55:E005", "sol:E011"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 (short preprint, no appendix exists); absent procedures are author-side gaps rated as such; "
                  "in scope (A, nominally): retained Template Library and Tool Ocean; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "sol", "scoped",
                "SCORE_SPEC: scoped keeps the author claim and states the narrower supported conclusion. The material is complete "
                "and a narrower conclusion is determinable (task-level scores with multi-trial budget; self-evolution attribution "
                "unsupported), so 'unresolved' (undeterminable) is not the right value. The unsupported attribution is recorded in "
                "strongest_supported_claim and in E.causality=1.",
                ["son55:E009", "son55:E014", "opus:O01"], "none (claim_support is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "The executed operation is decompose → execute code → critique → forge tools; template conditioning is secondary "
                "and unspecified.", ["son55:E002", "son55:E012", "son55:E017"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["decompose_and_delegate", "C25"], ["adapt_via_conditioning", None]],
                "son55's C25 primary kept; sol's conditioning match kept as supporting with sub null (C03 conditions absent).",
                ["son55:E002", "son55:E017", "sol:E001"], NOSCORE),
            X(p, "local:2507.02004-3", *C(p, "expectations[local:2507.02004-3].status"), "revised",
              "local-3 = son55's ground-truth-feedback question → unknown; sol's statistics question renumbered local-5 = partial",
              "A4 collision: different questions under one ID; each answer stands under its own question.",
              ["son55:E008", "son55:E015", "sol:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "sol", "unmet",
              "Verified: no template-off or fixed-template control (adapt kept as supporting).", ["sol:E001", "sol:E011"]),
            X(p, "rs:decompose_and_delegate/RE-1", *C(p, "expectations[rs:decompose_and_delegate/RE-1].status"), "son55", "unmet",
              "Verified: cost only as trial multiples.", ["son55:E005"]),
            X(p, "rs:decompose_and_delegate/RE-2", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"), "son55", "unmet",
              "Verified: no component ablation.", ["son55:E009", "son55:E012"]),
            X(p, "rs:decompose_and_delegate/RE-3", *C(p, "expectations[rs:decompose_and_delegate/RE-3].status"), "son55", "unmet",
              "Verified: no prompts or procedures in the pinned text.", ["son55:E004"]),
            X(p, "rs:decompose_and_delegate/RE-4", *C(p, "expectations[rs:decompose_and_delegate/RE-4].status"), "son55", "partial",
              "Verified: three QA benchmarks in one domain; workflow case anecdotal.", ["son55:E007", "son55:E016"]),
            X(p, "rs:decompose_and_delegate/RE-5", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"), "son55", "unmet",
              "Verified: single-pass LLMs and Biomni only; no equal-trial or same-mixture baseline.", ["son55:E012", "son55:E013"]),
            X(p, "rsi:abstract_experience_into_guidance/S5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S5].status"), "son55", "unknown",
              "Kept: only 'successful' workflows are saved and 'successful' is undefined, so whether a keep-gate exists cannot be "
              "read from the complete text.", ["son55:E004"]),
            X(p, "rsi:crystallize_executable_capability/F1",
              *C(p, "expectations[rsi:crystallize_executable_capability/F1].status"), "son55", "unmet",
              "Failure present: tool creation is buried in a four-agent system with no isolated test.", ["son55:E002", "son55:E012"]),
            X(p, "rsi:crystallize_executable_capability/H07",
              *C(p, "expectations[rsi:crystallize_executable_capability/H07].status"), "sol", "partial",
              "Verified: gap-triggered creation and execution environment described; registration/test/reuse not.",
              ["sol:E002", "sol:E003"]),
            X(p, "rsi:crystallize_executable_capability/S1",
              *C(p, "expectations[rsi:crystallize_executable_capability/S1].status"), "son55", "partial",
              "Verified: 'test and validate' asserted without criterion.", ["son55:E002"]),
            X(p, "rsi:crystallize_executable_capability/S3",
              *C(p, "expectations[rsi:crystallize_executable_capability/S3].status"), "son55", "unknown",
              "Kept: abstraction validation on new inputs is not described either way.", ["son55:E002"]),
            X(p, "rsi:crystallize_executable_capability/S5",
              *C(p, "expectations[rsi:crystallize_executable_capability/S5].status"), "son55", "unmet",
              "Verified: no retained-library ablation.", ["son55:E009", "son55:E014"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.M: narrative mechanism, nothing reconstructable.", ["son55:E001", "son55:E004"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.measurement: undefined trial aggregation, approximate figure values, 6 vs 8 pp, unspecified "
                "protocol modifications.", ["son55:E010", "son55:E011", "opus:O01", "opus:O02"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.holdout: no holdout evidence of any kind in the complete text.", ["son55:E008"],
                "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2507.02004-2]", "sol_value": "unmet — no frozen-library held-out / overlap audit",
             "son55_value": "unmet — abstract 6 pp vs introduction 8 pp headline",
             "final_value": "local-2 = son55's headline-inconsistency question (unmet); sol's held-out question renumbered local-4 (unmet)",
             "correction": "Same ID used by both seats for different questions (A4 collision hidden by equal status).",
             "evidence_ids": ["son55:E010", "son55:E011", "sol:E006"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Short report. Self-evolution evidence is only accuracy vs number of trials (1×→9×, "
                                                   "3 runs, figure-only); no store-off/component control; trial protocol, "
                                                   "template/tool admission and baseline provenance undefined; abstract 6 pp vs "
                                                   "intro 8 pp; headline 26% is the 9× point.",
            "integrity_checks": "Both seats a1 on 2507.02004v1, material sha 21d3e869…, input_hash de46e77b…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read the entire text; confirmed no appendix exists, no ablation, no cost, no split description.",
            "rating_agreement": "5/8 identical and re-checked; M→son55, E.measurement→son55, E.holdout→son55 (not_reported).",
            "expectation_renumbering": "sol local-2 → local-4, sol local-3 → local-5; sol local-1 = son55 local-1 (same question).",
        },
    }

    # =========================================================== 2507.03616 EvoAgentX
    p = "2507.03616"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "EvoAgentX’s optimization algorithms consistently enhance performance across all benchmarks", "§4.1",
                    "Contradicted by Table 2: MIPRO lowers MBPP from 69.00 to 68.00 (opus:O02, opus:O03)."),
            opus_ev(p, "O02", "MIPRO 69.16 68.00 72.30", "Table 2 (whitespace-normalised)", "MIPRO row."),
            opus_ev(p, "O03", "Original 63.58 69.00 66.00", "Table 2 (whitespace-normalised)", "Unoptimised row."),
            opus_ev(p, "O04", "These results demonstrate the EvoAgentX can effectively refine multi-agent workflow topologies",
                    "§4.1", "The two best results (HotPotQA, MATH) come from TextGrad, a prompt optimizer; the topology claim is "
                    "not what the table shows."),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "The paper's own operation is platform integration: five software layers wrapping existing optimizers "
                      "(TextGrad, MIPRO, AFlow, SEW). reframe_as_solvable_object (sol) requires recasting an intractable problem "
                      "into a well-studied object with mature solvers; representing workflows as graphs/prompts for these "
                      "optimizers is the integrated algorithms' own reframing, reused here. adapt_via_conditioning/C03 (sol) "
                      "covers only MIPRO's inherited few-shot conditioning, with no holdout. decompose_and_delegate considered: "
                      "MAS decomposition is background. No RS card is executed as a new operation (son55).",
            "executes_pattern": False, "resolves_problem": "no",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "search_agent_architecture", "H17"),
                        dmatch("son55", p, "attribute_and_patch_incumbent", "H10")],
            "unassigned": copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "revision_proposals": [],
        },
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2507.03616-2"): "local:2507.03616-5",
                    ("sol", "local:2507.03616-3"): "local:2507.03616-2",
                    ("sol", "local:2507.03616-4"): "local:2507.03616-6"},
            overrides={}),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O04"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Optimized prompts/workflows score higher than the original on the reported sets, but the split "
                                   "used for optimization vs scoring is never stated; nothing shows a retained change helping "
                                   "later, held-out tasks.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single numbers with unstated model, split, N and budget: running "
                                         "TextGrad / AFlow / MIPRO through the platform raises some benchmark scores over the "
                                         "original workflow (best per benchmark +7.44 F1, +10, +10) while MIPRO lowers MBPP; GAIA "
                                         "gains are figure-only relative changes. Platform-specific contribution, 'consistent' "
                                         "improvement and automatic workflow generation are not supported. Not reproduced.",
            "unresolved": ["Optimization vs evaluation split, executor model, N and rounds for Table 2 and GAIA.",
                           "Platform vs direct-run attribution.", "Memory optimizer unimplemented; workflow generation unevaluated."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. A real practitioner integration gap with broad lineage, but no evidence "
                   "fragmentation limits outcomes and no platform-level neighbour (e.g. DSPy as a multi-optimizer toolkit) is "
                   "compared.", ["son55:E002", "son55:E003", "son55:E016"]),
            "M": R("resolved", 1, "Opus sides with son55. The paper adds no mechanism of its own: generic operator equations wrap "
                   "existing algorithms, automatic workflow generation is never described, the memory optimizer is unimplemented, "
                   "and acceptance/rejection is inherited, so no distinguishing prediction follows (anchor 2 needs a specific "
                   "mechanism with partial causal account). sol's 2 credits the integrated algorithms' mechanisms to the platform.",
                   ["son55:E001", "son55:E004", "son55:E015"]),
            "X": R("resolved", 2, "Opus sides with sol. As executed, the loop is reconstructable at the interface level: graph/node "
                   "formalism with execution states, agent/workflow/optimizer APIs with code, separate optimizer/executor LLMs, "
                   "validation/eval/max-round parameters, persisted optimized paths and before/after artifacts (sol:E006, "
                   "sol:E014, son55:E019), with selection inherited from published, specified algorithms. Missing: the "
                   "experiment configuration, platform-level acceptance/rollback/versioning, workflow generation and the memory "
                   "optimizer — anchor 2 ('main steps described, retention/recovery or key conditions unclear'), not 1.",
                   ["sol:E002", "sol:E006", "sol:E014", "son55:E019", "son55:E020", "son55:E004"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Ground-truth metrics are credible, but executor model, N, "
                               "splits and per-benchmark optimizer choice are unreported, GAIA appears only as percentage changes "
                               "(Level-3 +100% implies a tiny base), and the prose claims consistent gains against its own table "
                               "(opus:O01).",
                               ["son55:E007", "son55:E010", "son55:E011", "opus:O01", "opus:O04"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Original vs optimized only; no direct-run reference, no "
                             "compute-matched or random-edit control; one optimizer lowers a score.",
                             ["son55:E007", "son55:E008", "opus:O02"]),
            "E.holdout": R("not_reported", 0, "Opus sides with son55. The optimization vs scoring split is never stated for Table 2 or "
                           "GAIA (Table 1 is generic dataset statistics: MBPP test-only, HotPotQA without test), the headline takes "
                           "the best of three optimizers per benchmark on the reported numbers, and no contamination check exists; "
                           "the Appendix A.3 optimize/test call is a usage example, not the experiment protocol.",
                           ["son55:E005", "son55:E006", "son55:E013"], [],
                           ["§4.1–4.3 text and Table 2", "Table 1 benchmark statistics", "Figure 2 caption and §4.2 text",
                            "Appendix A.1–A.4 code and case studies", "§3.5 Evaluation Layer"]),
            "E.statistics": R("not_reported", 0, "Opus sides with son55 under the A2 ladder: rung 1 needs reported sample sizes and "
                              "negative results; the MIPRO decrease is visible but no evaluation N, repeats, seeds or intervals are "
                              "reported for any experiment (Table 1 lists dataset sizes, not what was scored).",
                              ["son55:E007", "opus:O02"], [],
                              ["Table 2", "Table 1", "Figure 2 caption and §4.2", "Appendix A.3–A.4"]),
            "E.cost": R("not_reported", 0, "Both seats 0 (not_reported); re-checked: no rounds, tokens, calls, dollars or wall-clock "
                        "for any experiment; max_rounds=20 is an example configuration.",
                        ["son55:E013"], [], ["§3–4", "Tables 1–2", "Figure 2 text", "Appendix A.1–A.4"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendix A (figure values absent; GAIA rated on stated text only); in scope (B): "
                  "integrated prompt/workflow optimizers producing persisted non-weight artifacts; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", None,
                "No RS card is executed as the paper's own operation; reframing belongs to the integrated algorithms.",
                ["son55:E001", "son55:E017", "son55:E018"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [],
                "outside_taxonomy=true with reason (PATTERN_PROTOCOL step 3); reframe and C03 matches describe inherited algorithms.",
                ["son55:E001", "sol:E010"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["search_agent_architecture", "H17"], ["attribute_and_patch_incumbent", "H10"]],
                "Domain layer records the retention mechanisms the system runs: AFlow workflow-code search (H17) and TextGrad "
                "feedback rewriting with retained best prompt (H10), which produces two of the three headline gains.",
                ["son55:E017", "son55:E018", "son55:E007"], NOSCORE),
            X(p, "local:2507.03616-4", *C(p, "expectations[local:2507.03616-4].status"), "revised",
              "local-4 = son55's workflow-generation question → unmet; sol's statistics question renumbered local-6 = partial",
              "A4 collision: different questions under one ID; each answer stands under its own question.",
              ["son55:E015", "sol:E016"]),
            X(p, "rsi:attribute_and_patch_incumbent/S3",
              *C(p, "expectations[rsi:attribute_and_patch_incumbent/S3].status"), "son55", "unknown",
              "Kept: regression protection is delegated to TextGrad and not described in this paper.", ["son55:E017"]),
            X(p, "rsi:search_agent_architecture/F4", *C(p, "expectations[rsi:search_agent_architecture/F4].status"), "son55",
              "unmet", "Failure present: infrastructure presented as optimization; no result the wrapper uniquely enables.",
              ["son55:E001", "son55:E003"]),
            X(p, "rsi:search_agent_architecture/H17", *C(p, "expectations[rsi:search_agent_architecture/H17].status"), "sol",
              "partial", "Verified: offline graph search and saving explicit; split and gate not.", ["sol:E002", "sol:E014"]),
            X(p, "rsi:search_agent_architecture/S3", *C(p, "expectations[rsi:search_agent_architecture/S3].status"), "son55",
              "partial", "Verified: optimizers use evaluation scores; acceptance/rollback not described here.",
              ["son55:E013", "son55:E020"]),
            X(p, "rsi:search_agent_architecture/S6", *C(p, "expectations[rsi:search_agent_architecture/S6].status"), "son55",
              "unmet", "Verified: no held-out certification; split unstated.", ["son55:E005", "son55:E006"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.M: no own mechanism beyond wrapping.", ["son55:E001", "son55:E015"], "−5.0 vs sol (20×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.X: interface-level loop reconstructable with persisted artifacts; key conditions missing.",
                ["sol:E006", "sol:E014", "son55:E019"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.holdout: split never stated; best-of-three on reported numbers.", ["son55:E005", "son55:E006"],
                "−2.5 vs sol (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.statistics: no evaluation N or variance anywhere.", ["son55:E007"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2507.03616-2]", "sol_value": "unmet — optimization/test separation not shown",
             "son55_value": "unmet — rounds, tokens, wall clock not reported",
             "final_value": "local-2 = cost question (son55 local-2 + sol local-3, unmet); sol's split question renumbered local-5 (unmet)",
             "correction": "Same ID used by both seats for different questions (A4 collision hidden by equal status).",
             "evidence_ids": ["son55:E013", "sol:E011", "sol:E014"], "score_impact": "none"},
            {"field_path": "expectations[local:2507.03616-3]", "sol_value": "unmet — no equal-budget baseline / token report (cost)",
             "son55_value": "unmet — MIPRO below original; best-of-three headline",
             "final_value": "local-3 = son55's question (unmet); sol's cost question merged into local-2",
             "correction": "Same ID, different questions, equal status (hidden A4 collision).",
             "evidence_ids": ["son55:E007", "son55:E009", "sol:E011"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Demo/platform paper wrapping TextGrad/MIPRO/AFlow/SEW. Table 2 lacks model, split, "
                                                   "N and budget; text claims consistent gains though MIPRO lowers MBPP; GAIA "
                                                   "figure-only relative changes; no cost, statistics or holdout description.",
            "integrity_checks": "Both seats a1 on 2507.03616v2, material sha 7232311a…, input_hash de46e77b…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read §3–§4 and Appendix A; recomputed Table 2 deltas (+7.44, +10, +10; AFlow HotPotQA +1.51; "
                                "MIPRO MBPP −1).",
            "outside_taxonomy_check": "Controller flag: son55 outside_taxonomy vs sol reframe/C03. Re-read reframe_as_solvable_object "
                                      "definition and C03; ruled outside_taxonomy (resolutions rs_pattern.primary/matches).",
            "rating_agreement": "4/8 identical and re-checked; M→son55, X→sol, E.holdout→son55, E.statistics→son55.",
            "expectation_renumbering": "sol local-2 → local-5, sol local-3 → local-2 (merged), sol local-4 → local-6.",
        },
    }
    return S


def batch_notes():
    return [
        "C03 convention applied to all four memory/conditioning papers (dropped without category holdout and equal-budget "
        "simpler-conditioning control), consistent with r03a A-MEM and r03b Dynamic Cheatsheet.",
        "In-stream (prequential) memory papers rated retained when a same-system store-off control exists (G-Memory, ExpeRepair, "
        "Xolver); E.holdout=1 for all three, as for r03b Dynamic Cheatsheet.",
        "A2 statistics ladder applied strictly: no reported evaluation N → not_reported 0 (G-Memory, EvoAgentX).",
        "New reporting errors found by Opus: G-Memory §5.2 best-baseline margins and §5.4 inverted ablation conclusion; Xolver "
        "§3.2 variant mix-ups and Table 5 vs Table 1/4 inconsistency; EvoAgentX 'consistent' gains vs MIPRO MBPP decrease.",
        "2507.03616: controller flag resolved — outside_taxonomy (platform wrapping existing optimizers); in scope as B.",
        "2507.02004: claim_support scoped (not unresolved): material complete, narrower conclusion determinable.",
        "No requests for new material and no card revision proposals; seats' requests for neighbour full texts do not affect any "
        "final rating.",
    ]
