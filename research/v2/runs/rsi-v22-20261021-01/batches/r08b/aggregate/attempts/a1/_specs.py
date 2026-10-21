"""Opus rulings for r08b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Ratings: 2511.13646 M and E.causality → son55 (2/2); 2511.15915 E.measurement → son55 (2), E.causality → sol (3), "
        "so the final (65.0) is above both seats by per-item ruling, not by averaging; 2512.09108 M and E.holdout → son55 (1/1).",
        "RS layer: 2512.09108 outside_taxonomy confirmed (cal-dev GrIPS / r04b EvoAgentX precedent: black-box population search "
        "over model-input text has no main card; generative_process_redesign would then cover any optimizer). 2511.15915 revised "
        "to adapt_via_conditioning (null) + decompose_and_delegate/C25 supporting (run convention for frozen-model curated "
        "memory: r03b Dynamic Cheatsheet, r06b ACE).",
        "A4 hidden ID collisions (same local:<key>-n, different questions) found in 2511.13646, 2511.15915 and 2512.09108; "
        "renumbered/merged and recorded (flagged ones as resolutions, equal-status ones as shared_error_corrections).",
        "2511.13646 scope: both seats in scope; independently confirmed as a boundary case (tool scripts are a non-weight "
        "action-space component created from execution feedback and reused within one trajectory; discarded after the task, "
        "§4.4). evidence_level task, not retained. son55's H07 revision proposal (within-episode, non-persistent tool "
        "synthesis) is forwarded, not applied.",
        "2511.16043 / 2512.02472: A3 out_of_scope independently confirmed (both agents' weights updated by RL; the code "
        "interpreter / anchor pool are fixed inputs). Both seats left domain unassigned; earlier aggregates (r05b R-Zero, "
        "r07a SPELL) carried H22 informationally for the same shape — precedent variance noted, no score effect, not changed.",
        "No material requests: all disputed fields were answerable from the pinned texts.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")
    PS = "rsi:population_search_executable_fitness"

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev, NOEXP)

    def XC(p, eid, dec, final, reason, ev=()):
        return X(p, eid, *C(p, f"expectations[{eid}].status"), dec, final, reason, ev)

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

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def son_assessment(p, extra_unresolved=()):
        a = copy.deepcopy(seat("son55", p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        return a

    # ------------------------------------------------------------------ out-of-scope helpers
    def oos_ratings(reason):
        return {k: R("unknown", None, reason) for k in KEYS}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run precedent "
                                       "r05b/r06a/r07a).",
                "claim_support": None, "claim_support_note": note, "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_common_res(p, ev, claim_reason):
        return [
            res("paper.claim_type", *C(p, "paper.claim_type"), "sol", "component_training", claim_reason, ev,
                "none (out_of_scope row; claim_type is identification only)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "null is canonical for out-of-scope rows (r05b/r06a/r07a precedent); the harness task/retained/improver "
                "ladder does not apply to weight-level work. sol's 'task' was descriptive only.", ev,
                "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
                "null is canonical for out-of-scope rows; claim support is not assessed under this rubric.", ev, "none"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                "Informational; verified: a proposer generates tasks, a self-consistency / majority-vote gate manufactures "
                "pseudo-labels, and both policies are retrained by RL — the C08 generate→gate→retrain loop. son55 skipped "
                "identification for an out_of_scope row (allowed); its rs record is 'not_assessed', not outside_taxonomy.",
                ev, NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["self_supervised_signal_engineering", "C08"]],
                "Follows primary; C08 is the run convention for challenger/solver self-play (r05b R-Zero, r06a "
                "2508.03682, r07a SPELL).", ev, NOSCORE),
        ]

    # =========================================================== 2511.13646 Live-SWE-agent (Δ8.75)
    p = "2511.13646"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "while the number of tools do not necessary correlate with solving performance",
                    "§4.3 Effectiveness of tool creation steps (Table 4 discussion)",
                    "Table 4: 2.92 vs 3.28 tools per issue for 64% vs 76%; the 12-point gap tracks the per-step reflection "
                    "message, not the amount of tooling, and no per-issue tool-use/credit analysis is given."),
            opus_ev(p, "O02", "Reflect on the previous trajectories and decide if there are any tools you can create to help "
                    "you with the current task.", "Appendix D.2 feedback message",
                    "The reflection text is appended after every step: it is both an extra-deliberation nudge and a "
                    "tool-creation nudge, and no arm separates the two."),
            opus_ev(p, "O03", "Furthermore, we hope to extend the self-evolution loop across different tasks as well.",
                    "§4.4 Towards general, on the fly self-evolution",
                    "Cross-task persistence is future work: retention is within one trajectory only."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats generative_process_redesign, sub null; re-checked and kept. The conventionally fixed "
                      "component of an iterative agent loop (its tool/action inventory) becomes a runtime variable; same "
                      "ruling as SICA (r03b) and Gödel Agent (cal-dev). C15/C23/C24 (3D substrate, diffusion chain, "
                      "conditioning granularity) do not fit, so sub null. decompose_and_delegate/C25 (LATM/Alita "
                      "convention) not used: there is no maker/user split or checker-closed admission — the single agent "
                      "writes and uses its scripts unverified.",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2511.13646-1"): "local:2511.13646-3"},
            overrides={
                "rsi:crystallize_executable_capability/S1": {
                    "status": "unmet",
                    "reason": "Opus final (son55): S1 asks for an execution-based admission gate. Scripts are written and "
                              "used immediately; failure only surfaces when the agent itself runs them. Use is not "
                              "admission (sol's 'execution and reuse visible' describes use)."},
                "local:2511.13646-3": {
                    "reason": "Opus (sol local-1 renumbered, A4): positive on GPT-5, Claude 3.7/4/4.5 Sonnet; GPT-5-Nano "
                              "drops 44→14 and GPT-5-Mini 60→58 on the 50-problem subset (but +3.2 on full Verified). "
                              "Cross-model generality holds for strong LLMs only; partial."},
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O01", "opus:O02"]),
        "assessment": son_assessment(p, ["Whether created tools are actually invoked in resolved instances (no tool-use "
                                         "or credit analysis, opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Sourced bottleneck for offline self-improvers (~$22k DGM run, "
                   "512–1231 offline hours, benchmark/LLM specialisation) with clear SICA/DGM/HGM lineage; the residual "
                   "(runtime, per-issue tooling, no offline cost) is stated. Not 4: runtime tool-making neighbours "
                   "(LATM/CREATOR-type) are dismissed in one sentence as 'not SE', and 'static action space is limiting' "
                   "is argued by example.",
                   ["son55:E001", "son55:E008", "sol:E010"]),
            "M": R("resolved", 2, "Opus sides with son55. Mechanism is concrete (script tools + per-step reflection prompt) "
                   "with plausible reasons (silent sed failures, multi-step searches) and one confirmed prediction "
                   "(stronger LLMs gain more, weak ones loop). But in this domain's M criterion there is no "
                   "accept/reject step and no write-back beyond the trajectory, and the key assumption — that tool "
                   "creation rather than the per-step reflection nudge drives the gain — is untested and partly "
                   "contradicted by the paper's own tool counts (opus:O01). sol's 3 credited reconstructibility, which is "
                   "scored under X.",
                   ["son55:E003", "son55:E004", "son55:E017", "son55:E010", "opus:O02"], ["opus:O01"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Operation chain, interface (script via bash), caps and exact "
                   "prompts are fully given (App. D) and the boundaries are explicit (discard after task, weak-LLM "
                   "looping). Not 4: no admission gate, versioning, rollback or cross-task read.",
                   ["son55:E002", "son55:E004", "son55:E015", "son55:E016", "son55:E013", "sol:E012"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Official hidden-test resolve rates on full "
                               "Verified (500), Pro (731) and a Multilingual subset; the verifier is not touched by the "
                               "agent. Not 4: single sample per issue and benchmark-test weakness is not discussed; "
                               "cross-LLM leaderboard mixing is a causality issue (A2).",
                               ["son55:E006", "son55:E007", "son55:E011", "son55:E012", "sol:E008"]),
            "E.causality": R("resolved", 2, "Opus sides with son55. Same-scaffold, same-cap comparisons on full Verified "
                             "across four LLMs (+3.2 to +4.8) support the bundled prompt change. Attribution to tools is "
                             "not established: the 'w/o tool creation' arm is the base agent, the reflection message "
                             "bundles extra deliberation with the tool nudge (opus:O02), the 12-point reflection effect "
                             "comes with nearly equal tool counts (opus:O01), there is no tools-given or reflection-only "
                             "control, and DGM/HGM/SWE-agent numbers are reused rather than rerun (son55:E009). Single runs "
                             "are charged to E.statistics (A2), not here.",
                             ["son55:E005", "son55:E006", "son55:E007", "son55:E012", "opus:O02"],
                             ["opus:O01", "son55:E009", "son55:E018"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Nothing is selected on evaluation data, Pro and "
                           "Multilingual act as out-of-benchmark checks with an unchanged prompt; but the prompt's "
                           "development data are undescribed, the ablation subset is drawn from Verified, contamination "
                           "of public benchmarks is not addressed, and cross-task retention is untested (opus:O03).",
                           ["son55:E011", "son55:E012", "son55:E014", "opus:O03"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder: sample sizes and negative results "
                              "reported, no uncertainty on main results). Single runs, no intervals; 50-problem subsets with "
                              "6–7-problem gaps; subset vs full-set inconsistency for GPT-5-Mini.",
                              ["son55:E014", "son55:E018", "son55:E010"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Average $ per issue for both arms under the same "
                        "250-step/$3 caps, including tool-creation overhead; offline hours of DGM/HGM contrasted. Not 4: "
                        "no token/step counts, Pro baseline cost missing, offline baselines not budget-matched.",
                        ["son55:E006", "son55:E007", "son55:E016", "son55:E008"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–D read; in scope (system_method, boundary): agent-written tool "
                  "scripts are a non-weight action-space component created from execution feedback and reused within one "
                  "trajectory; not retained across tasks (opus:O03). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope, boundary confirmed: a component changes and is reused within the episode, so it is not "
              "single-answer self-correction; retention claims are capped at evidence_level task)",
        "resolutions": [
            XC(p, "local:2511.13646-1", "son55", "unmet",
               "A4 ID collision: sol's local-1 (cross-LLM generality, M) and son55's local-1 (instruction-bundle control, "
               "E.causality) are different questions. Final local-1 = son55's question, verified unmet: no "
               "reflection-only or tools-given arm, and the reflection effect arrives with nearly equal tool counts "
               "(opus:O01). sol's question kept as local-3 (partial, verified).",
               ["son55:E005", "son55:E015", "opus:O01", "opus:O02"]),
            XC(p, "local:2511.13646-2", "son55", "unmet",
               "Verified: every number is a single run without intervals; 50-problem subsets; GPT-5-Mini is 58 vs 60 on the "
               "subset but +3.2 on full Verified.", ["son55:E014", "son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "partial",
               "Applies (card kept). Removing tool creation lowers 76→62, but the arm also removes the reflection prompt and "
               "how often the static action space actually binds is not measured.",
               ["son55:E005", "son55:E017", "opus:O01"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "partial",
               "Verified: same-scaffold mini-SWE-agent on Verified; Pro and Verified-60 baselines are reused published "
               "numbers; no tools-given or other tool-synthesis baseline.", ["son55:E008", "son55:E009", "son55:E011"]),
            XC(p, "rs:generative_process_redesign/RE-5", "son55", "partial",
               "Verified: same-LLM comparisons exist (4 LLMs), but the headline 'beats all agents' compares Live-SWE+Gemini 3 "
               "Pro with systems on other LLMs.", ["son55:E007", "son55:E009"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "met",
               "Failure avoided: the change is an isolated prompt on the unmodified mini-SWE-agent loop, so the forging "
               "effect is the measured contribution.", ["son55:E002"]),
            XC(p, "rsi:crystallize_executable_capability/H07-step1", "son55", "partial",
               "Verified: an explicit decision point exists but fires on every step rather than on a detected gap (the "
               "noise/latency risk the card names); weak LLMs loop.", ["son55:E003", "son55:E010", "opus:O02"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "unmet",
               "S1 asks for an execution-based admission gate. No admission step exists: scripts are used as soon as written "
               "and only the agent's own later runs reveal faults. sol's 'partial' credited use and reuse, which is not a "
               "gate.", ["son55:E004", "son55:E003", "sol:E012"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M: no accept/reject or write-back beyond the trajectory, and the tools-not-reflection "
                "assumption is untested and weakened by Table 4's tool counts (opus:O01). Reconstructibility (sol's basis) "
                "is credited under X.", ["son55:E003", "son55:E017", "opus:O01", "opus:O02"], "-5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.causality: the bundle is supported by same-scaffold comparisons, but the strongest "
                "alternative (per-step reflection without tools) is untested and the paper's own tool counts are "
                "consistent with it; external baselines are reused. Single-run noise is A2-charged to E.statistics, so "
                "sol's 3 was not lowered for that.", ["son55:E005", "son55:E009", "opus:O01", "opus:O02"],
                "-3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening seats: per-issue scripts created on "
                                                   "a reflection prompt, discarded after the task (§4.4); same-scaffold "
                                                   "+3–5 on full Verified; ablation n=50 single run; Table 2/3 baselines "
                                                   "reused. Initial bands G3 M2 X3 Em3 Ec2 Eh2 Es1 Ecost3; evidence_level "
                                                   "task; boundary in-scope.",
            "integrity_checks": "Both seats a1 on 2511.13646v3, material sha f41da763…; canonical seat hashes equal "
                                "conflicts.json; both identified generative_process_redesign + H07; namespaces valid.",
            "core_claim_check": "Re-read §2, §4.1–4.4, Tables 1–6 and App. D; recomputed Table 4/5 gaps (7 and 6 problems "
                                "of 50) and checked that the 'w/o tool creation' arm is the base agent.",
            "rating_agreement": "6/8 identical and re-checked; M and E.causality → son55.",
            "expectation_renumbering": "sol local-1 → local-3 (A4 collision).",
            "retained_vs_retained_gain": "Nothing is retained beyond the trajectory; 'self-evolve' is within-episode tool "
                                         "creation. No retained or improver claim is supported.",
        },
    }

    # =========================================================== 2511.15915 AccelOpt (Δ1.25)
    p = "2511.15915"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "We match the number of generated kernels with Table", "§4.4 Reflexion-style Baseline",
                    "The alternative memory design is compared at the same number of generated kernels, with cost."),
            opus_ev(p, "O02", "matching the number of profiled kernels with Table", "§4.4 Validate the Diversity Design",
                    "The B=1 memory/no-memory comparison is held at the same number of profiled kernels."),
            opus_ev(p, "O03", "AccelOpt already reduces expenses compared with repeated sampling", "§4.5 (Table 3 text)",
                    "With the same model (Claude Sonnet 4) the workflow reaches 1.226 at $1732.73 vs repeated sampling "
                    "1.222 at $5806.83, isolating the workflow from the model-price effect in the 26× headline."),
            opus_ev(p, "O04", "This finding calls for more rigorous equivalence checking than the common practice of "
                    "testing with random inputs.", "Appendix A.2",
                    "The authors' own verdict on the correctness checker; no statement that reported kernels were "
                    "re-audited."),
            opus_ev(p, "O05", "AccelOpt’s memory component is part of the test-time learning paradigm", "§2.3 (end)",
                    "The memory is per-problem inference-time conditioning of frozen planner LLMs."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Opus revised. Load-bearing new move: frozen planner LLMs are conditioned at inference on a curated "
                      "experience queue (slow-fast pseudocode + strategy) that a summarizer writes from profiled outcomes — "
                      "the run convention for frozen-model curated memory (r03b Dynamic Cheatsheet, r06b ACE: "
                      "adapt_via_conditioning, sub null). C03 not assigned: no upstream canonical-schema phase or "
                      "category-level holdout; memory is per problem with transfer deferred (son55:E014). son55's C25 kept "
                      "as supporting: executable kernels are routed to the profiler/CPU-reference checker and that "
                      "verifiable signal drives beam selection and memory credit. sol's generative_process_redesign "
                      "rejected as in cal-dev GrIPS: the liberated 'expert recipe list' is model input, and freeing it would "
                      "make the card cover any optimizer. Beam search itself is inherited (Autocomp) and carried by the "
                      "domain card H14.",
            "matches": [
                {"main_id": "adapt_via_conditioning", "sub_id": None, "role": "primary", "fit": "partial",
                 "tactic_steps_checked": "frozen LLMs; the task is expressed to the planner as kernel + profile + curated "
                                         "experience items; no parameter update; conditioning source rebuilt every "
                                         "iteration from measured slow-fast pairs (positive and negative).",
                 "success_checks": "Cheaper-conditioning alternative tested: a Reflexion-style reflector at matched kernel "
                                   "count (opus:O01); no-memory arm (son55:E005).",
                 "failure_checks": "Memory does not raise best speedup given enough samples (son55:E002) and hurts at B=1 "
                                   "(son55:E007); no cross-kernel generalisation (son55:E014).",
                 "evidence_ids": ["son55:E001", "son55:E003", "son55:E005", "son55:E006", "son55:E014", "opus:O05",
                                  "opus:O01"],
                 "reason": "Main-card operation executed (condition, don't retrain); sub null per run convention."},
                smatch("son55", p, "decompose_and_delegate", role="supporting"),
            ],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "population_search_executable_fitness", "H15"),
                        dmatch("son55", p, "population_search_executable_fitness", "H14")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"]), "son55") + [{
            "rs_main": "adapt_via_conditioning", "rs_sub": None,
            "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": "H15"},
            "operation_correspondence": "RS: condition a frozen model instead of retraining. H15: a distilled knowledge layer "
                                        "conditions the next proposals and is rewritten as fitness results arrive.",
            "necessary_conditions_or_differences": "H15 additionally requires item credit by evidence, declared and tested "
                                                   "sharing scope and a matched-budget held-out memory ablation; AccelOpt "
                                                   "credits by pair speedup, scope is per problem, ablation is "
                                                   "iteration-matched without held-out.",
            "evidence_ids": ["son55:E003", "son55:E004", "son55:E005", "son55:E014", "opus:O05"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2511.15915-1"): f"{PS}/H15-step4",
                    ("sol", "local:2511.15915-2"): "rs:decompose_and_delegate/RE-1"},
            overrides={
                "rs:decompose_and_delegate/RE-1": {
                    "status": "partial", "score_item": "E.cost",
                    "reason": "Opus revised (sol local-2 merged, A4): dollar API cost for nearly every configuration and "
                              "cost-benefit sweeps are given, but solver latency (profiling hardware time, failed-kernel "
                              "profiling) is not reported and the 26× figure is API price only; RE-1 asks for solver "
                              "latency too."},
                f"{PS}/S2": {
                    "status": "partial",
                    "reason": "Opus final (son55): the evaluator is built first (profiler, CPU reference, multi-seed "
                              "tolerance), but the authors show it can be gamed and call for stronger equivalence checks "
                              "(opus:O04) without saying reported kernels were audited — partial, not unmet."},
                f"{PS}/H15-step4": {
                    "status": "unmet",
                    "reason": "Opus final (son55; sol local-1 merged, A4): scope is declared per problem and transfer is "
                              "explicitly deferred; the card records exactly this as the limitation."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O04"]),
        "assessment": son_assessment(p),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Concrete, sourced problem (no expert recipes or heuristics on "
                   "a new accelerator; Autocomp's hand-written optimisation lists; LessonL's baseline-anchored memory) "
                   "and a stated residual (cross-kernel transfer). Not 4: neighbour texts are not pinned and memory "
                   "accumulation is not shown to be the binding residual.",
                   ["son55:E001", "son55:E014", "sol:E012", "sol:E013"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Positive and negative slow-fast pairs, grouping by candidate "
                   "and plan, thresholds and a FIFO cap are reconstructable with reasons, and the paper produces "
                   "distinguishing observations (memory hurts at B=1; planner choice irrelevant, executor matters; "
                   "Reflexion reflects on all kernels and costs more). Not 4: heuristic thresholds, unvalidated "
                   "summarizer, memory not shown to raise best speedup.",
                   ["son55:E003", "son55:E006", "son55:E007", "sol:E003"], ["son55:E002"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithms 1–2, capacities, thresholds, prompts and model "
                   "settings are given and the next-iteration read is explicit; failure and saturation analysis plus "
                   "platform requirements are reported. Not 4: no item-level utility, versioning, rollback or conflict "
                   "handling; prose ('append to tail') vs Algorithm 2 (prepend, truncate) ordering differs, though both "
                   "evict the oldest.",
                   ["son55:E003", "son55:E004", "son55:E017", "son55:E021", "sol:E002"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Latency is measured with warm-up and repeated "
                               "rounds, percent-of-peak is roofline-based, correctness is multi-seed tolerance against a CPU "
                               "reference — a credible design. But the authors found gpt-oss exploiting the checker "
                               "(skipped computation passing as speedup) and themselves call for stronger equivalence "
                               "checking (opus:O04), without stating that reported best kernels were audited: a key gap, "
                               "not a refutation of the metric. Run precedent: cal-h1-v2 STOP (exploitable utility found "
                               "during development) = 2.",
                               ["son55:E015", "sol:E010", "sol:E011", "son55:E018"], ["son55:E011", "opus:O04"]),
            "E.causality": R("resolved", 3, "Opus sides with sol. Controls are matched where it matters: beam search vs "
                             "repeated sampling with the same LLMs; memory vs no memory; B=1 with/without memory at the "
                             "same number of profiled kernels (opus:O02); a Reflexion-style alternative memory at the same "
                             "number of generated kernels, with cost (opus:O01); same-model workflow vs repeated sampling "
                             "for the cost claim (opus:O03); planner/executor swaps. Negative results are kept (memory "
                             "does not lift best speedup; hurts at B=1). Not 4: no per-role ablation, the memory ablation "
                             "is iteration- not token-matched, no non-LLM optimiser. son55's 'no repeats' is charged to "
                             "E.statistics under A2.",
                             ["son55:E019", "son55:E005", "son55:E006", "son55:E007", "opus:O01", "opus:O02", "opus:O03"],
                             ["son55:E002", "son55:E020"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. B, N, K, TopK and ExpN are chosen on the same 14 "
                           "kernels that are reported (son55:E012); memory is used only within the problem that produced "
                           "it; out-of-benchmark results (CS149 Conv2D, 24 FlashInfer Triton kernels) are single, "
                           "uncontrolled reports.",
                           ["son55:E012", "son55:E013", "son55:E016", "sol:E004"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). 14-task denominator and negative/"
                              "saturation cases are shown, but no repeated searches, seeds or intervals while 0.6–4.6% "
                              "differences are interpreted; timing repeats are not search variance.",
                              ["son55:E008", "son55:E007", "son55:E017"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Dollar cost for almost every configuration, ExpN/TopK "
                        "cost-benefit sweeps, matched-kernel baselines and same-model workflow vs repeated sampling "
                        "(opus:O03). Not 4: profiling hardware time and failed-kernel profiling excluded; 26× is API "
                        "price only.",
                        ["son55:E008", "son55:E009", "son55:E010", "opus:O03"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendix A (prompts, memory examples) read; in scope (system_method): a "
                  "non-weight optimisation memory curated from profiled outcomes and read by later iterations (per-problem "
                  "scope). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "revised", "adapt_via_conditioning",
                "See rs_pattern.reason: the new move is conditioning frozen planners on a curated per-problem memory (run "
                "convention: Dynamic Cheatsheet, ACE). sol's generative_process_redesign: the 'fixed recipe' is model input "
                "(cal-dev GrIPS ruling). son55's decompose_and_delegate/C25 is real but secondary (the checker-closed "
                "selection loop), and its parent's 'route sub-problems to sound solvers' is only partly present (the "
                "checker grades, it does not solve).",
                ["son55:E001", "son55:E003", "son55:E014", "opus:O05"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "Primary adapt_via_conditioning (sub null, C03 conditions absent); son55's C25 kept as supporting.",
                ["opus:O05", "son55:E005", "son55:E019"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["population_search_executable_fitness", "H15"], ["population_search_executable_fitness", "H14"]],
                "H14's genome list names kernels: LLM-proposed kernel edits, an automated evaluator and retained winners "
                "are the base beam search; H15 is the memory layer on top (primary). sol recorded only H15.",
                ["son55:E019", "son55:E021", "son55:E003"], NOSCORE),
            XC(p, "local:2511.15915-2", "son55", "unknown",
               "A4 ID collision: sol's local-2 (cost claim) and son55's local-2 (checker exploitation of reported kernels) "
               "are different questions. Final local-2 = son55's question: unknown is correct — the paper reports the "
               "exploit and calls for stronger checking (opus:O04) but never says whether reported kernels were "
               "affected. sol's question merged into rs:decompose_and_delegate/RE-1.",
               ["son55:E011", "opus:O04"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "revised", "partial",
               "Applies (C25 kept as supporting). RE-1 asks for token/API budget, call counts and solver latency. Dollar "
               "costs are thorough, but profiling hardware time is not reported (son55's own note) and 26× is API price "
               "only (sol local-2): partial, not met.", ["son55:E008", "son55:E010", "sol:E015"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: beam vs repeated sampling, memory vs none, B=1 and ExpN/TopK sweeps; no planner/summarizer "
               "role ablation.", ["son55:E005", "son55:E007", "son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "met",
               "Verified: repeated sampling with the same LLMs and with Claude Sonnet 4, and a Reflexion-style reflector at "
               "matched generated-kernel count.", ["son55:E006", "son55:E010", "son55:E019", "opus:O01"]),
            XC(p, f"{PS}/F1", "son55", "partial",
               "Verified: LLM beam search over kernels is the H14 shape the card warns about; the search-level additions "
               "are the positive/negative slow-fast memory and the percent-of-peak benchmark.",
               ["son55:E001", "son55:E018"]),
            XC(p, f"{PS}/H15", "sol", "partial",
               "Verified as a whole-sub-card summary: queue, negative knowledge and real next-iteration read exist; "
               "sharing is per problem. Kept alongside son55's step items.",
               ["sol:E001", "sol:E002", "sol:E003", "sol:E004"]),
            XC(p, f"{PS}/H15-step4", "son55", "unmet",
               "Verified: per-problem scope with transfer deferred. sol asked the same question as local-1 (unmet); merged "
               "here (A4).", ["son55:E013", "son55:E014", "sol:E004"]),
            XC(p, f"{PS}/H15-step5", "son55", "partial",
               "Verified: Search vs Search+Memory exists but is iteration-matched, without held-out split; cost saving is "
               "the main effect.", ["son55:E002", "son55:E005", "son55:E012"]),
            XC(p, f"{PS}/S2", "son55", "partial",
               "The evaluator is built first and is mostly sound, but gameable with no stated audit (opus:O04). 'Unmet' "
               "(sol) would mean no meaningful evaluator; the documented hole makes it partial, consistent with "
               "E.measurement=2.", ["son55:E011", "son55:E015", "opus:O04"]),
            XC(p, f"{PS}/S4", "son55", "met",
               "Verified: the hardware profile of each candidate is in the planner prompt (Fig. 21) and the Fig. 3 trace "
               "shows it driving the plan.", ["son55:E001", "son55:E021"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: credible design with a documented, unaudited gaming hole = key gap (2), not "
                "refuted metric; consistent with cal-h1-v2 STOP.", ["son55:E011", "son55:E015", "opus:O04"],
                "+2.5 vs sol (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.E.causality: matched-kernel controls for both memory designs and for B=1 (opus:O01, "
                "opus:O02), same-LLM repeated sampling and same-model cost isolation (opus:O03); negative results kept. "
                "son55's docking reasons are a small effect size (a result, not a design gap) and no repeats (A2: "
                "E.statistics).", ["son55:E006", "son55:E007", "son55:E019", "opus:O01", "opus:O02", "opus:O03"],
                "+3.75 vs son55 (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2511.15915-1]",
             "sol_value": "unmet — same-problem search vs later-task learning (E.holdout)",
             "son55_value": "unmet — 0.6–4.6% differences without noise estimates (E.statistics)",
             "final_value": "local-1 = son55's statistics question (unmet); sol's question merged into "
                            f"{PS}/H15-step4 (unmet)",
             "correction": "A4 hidden collision: same ID, different questions, equal status, so the mechanical diff did "
                           "not flag it.", "evidence_ids": ["son55:E007", "son55:E008", "sol:E004"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening seats: per-problem FIFO memory of "
                                                   "slow-fast pairs on top of inherited beam search; memory saves ~16% cost "
                                                   "but not best speedup; B=1 memory hurts; Reflexion baseline matched; A.2 "
                                                   "checker exploit; hyperparameters chosen on the 14 kernels; no repeats. "
                                                   "Initial bands G3 M3 X3 Em2 Ec2–3 Eh1 Es1 Ecost3; evidence_level task.",
            "integrity_checks": "Both seats a1 on 2511.15915v2, material sha c88b9a12…; canonical seat hashes equal "
                                "conflicts.json; both seats in scope; namespaces valid. son55 read the A.3 NKI prompt "
                                "listing structurally only — it contains API/profile documentation and templates and no "
                                "method or result facts that bear on any disputed field (checked by Opus in full).",
            "core_claim_check": "Re-read §2–4, Tables 1–3, Figs 13–14 text and App. A; confirmed the matched-count wording "
                                "for Reflexion and B=1 and the same-model Table 3 cost comparison.",
            "rating_agreement": "6/8 identical and re-checked; E.measurement → son55 (2), E.causality → sol (3). Final 65.0 "
                                "is above both seats (62.5 / 61.25) by per-item rulings.",
            "expectation_renumbering": "sol local-1 → H15-step4, sol local-2 → rs:decompose_and_delegate/RE-1.",
            "retained_vs_retained_gain": "Memory is retained across iterations of one problem only; its measured effect is "
                                         "cost-efficiency, not a better final kernel; no cross-kernel retained gain.",
        },
    }

    # =========================================================== 2511.16043 Agent0 (both out_of_scope)
    p = "2511.16043"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "curriculum agent is RL-trained to propose tasks and the executor is RL-trained (ADPO) on them (opus:O01, "
          "opus:O02); the code interpreter is a fixed sandboxed tool, not created or retained by the loop (opus:O03); "
          "generated tasks are transient training data. Every reported result is a trained checkpoint. Not scored; null is "
          "not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "the curriculum agent is trained using RL to propose frontier tasks", "§1",
                    "The task generator's product is updated weights."),
            opus_ev(p, "O02", "the executor agent is trained via RL to successfully solve these tasks", "§1",
                    "The evaluated executor is a trained checkpoint."),
            opus_ev(p, "O03", "we integrate a sandboxed code interpreter", "§4.1 Implementation",
                    "The tool is a fixed integration, not an evolved harness component."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): the curriculum agent manufactures tasks, executor self-consistency and "
                      "majority vote manufacture pseudo-labels and the uncertainty/tool-use reward, and both policies are "
                      "retrained — C08 (generate → gate → retrain, iterated).",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering", fit="high (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]), "sol"),
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; benchmark gains are author-reported RL results."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": oos_common_res(p, ["opus:O01", "opus:O02"],
                                      "Informational: the evaluated product is a trained executor (and curriculum) model; "
                                      "run precedent r05b R-Zero keeps component_training for identification. son55 left "
                                      "it null for an excluded row, which is also allowed.") + [
            XC(p, "local:2511.16043-1", "sol", "unmet",
               "Verified (informational): the new state is weights; tasks and code are not evaluated as deployed "
               "components.", ["opus:O01", "opus:O02", "opus:O03"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "sol", "partial",
               "Verified (informational): curriculum/tool-reward/repetition-penalty/ADPO ablations exist; no "
               "compute-matched plain-RL control. No score effect.", ["sol:E005"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §1–4 and appendix setup before opening seats: two RL-"
                                                   "trained agents from one base model, fixed sandboxed interpreter → "
                                                   "out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2511.16043v2, material sha 7134be58…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2512.02472 R-Few (both out_of_scope)
    p = "2512.02472"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes self-play fine-tuning). Independently checked: Challenger and "
          "Solver are both updated by GRPO (Challenger after an SFT warm-up) (opus:O01, opus:O02) and the algorithm "
          "returns trained models (opus:O03); the few-shot human anchor pool is a fixed input, not a component the loop "
          "changes and retains. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "which guides the policy updates of both agents via reinforcement learning", "§2",
                    "Both roles are weight-updated."),
            opus_ev(p, "O02", "The Challenger parameters are updated via GRPO as:", "§3.2",
                    "The task generator is trained, not prompted-and-retained."),
            opus_ev(p, "O03", "Return: Trained Challenger", "Algorithm 1", "The product of the loop is trained models."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): anchor-grounded Challenger generation, self-consistency pseudo-labels "
                      "and an online difficulty curriculum feed GRPO retraining of both roles — C08. Few-shot anchors are "
                      "not a C03 conditioning contribution (sol's reason holds).",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering", fit="high (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]), "sol"),
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; gains are author-reported RL results."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": oos_common_res(p, ["opus:O01", "opus:O03"],
                                      "Informational: the evaluated product is a trained Solver; r05b R-Zero precedent "
                                      "keeps component_training for identification.") + [
            XC(p, "local:2512.02472-1", "sol", "unmet",
               "Verified (informational): non-weight inputs (anchors, prompts) are fixed; the trained product is weights.",
               ["opus:O02", "opus:O03"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "sol", "partial",
               "Verified (informational): no-Challenger-training, warm-up and curriculum ablations exist; no "
               "compute-matched mixed-data RL control. No score effect.", ["sol:E006"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §2–3, Algorithm 1 and appendix before opening seats: "
                                                   "Challenger/Solver both GRPO-trained → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2512.02472v1, material sha 30c31857…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2512.09108 Artemis / Evolving Excellence (Δ7.5)
    p = "2512.09108"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "For prompt optimization, we employ evolutionary prompt engineering to evolve prompts from "
                    "simple Chain-of-Thought (CoT) approaches to include sophisticated self-correction checklists.",
                    "§5.1 ALE Agent", "ALE prompt optimisation is one run …"),
            opus_ev(p, "O02", "For search optimization, we apply genetic algorithms with advanced search strategies (such "
                    "as beam search and taboo memory) for systematic exploration of the solution space.", "§5.1 ALE Agent",
                    "… and search-strategy optimisation a separate run (reported separately in Fig. 6): the joint "
                    "multi-component optimisation that answers the paper's stated gap is not exercised in this case."),
            opus_ev(p, "O03", "Artemis incorporates novel mutation and crossover operators specifically designed for "
                    "natural language components", "§1 contribution 2",
                    "The claimed novel mechanism; its prompts, algorithm and selection rule are never specified."),
            opus_ev(p, "O04", "Finally, validate improvements on held-out data to ensure generalization beyond training "
                    "benchmarks.", "§7 Discussion (guidelines)",
                    "The authors' own guideline, not followed for ALE, Mini-SWE or CrewAI."),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "Opus confirms son55. The executed operation is LLM-operator evolutionary + Bayesian search over agent "
                      "configuration text/parameters against benchmark fitness. Run precedent cal-dev GrIPS (instruction "
                      "search, H13) and r04b EvoAgentX ruled outside_taxonomy: generative_process_redesign needs a fixed "
                      "component of an iterative/staged generative procedure; agent prompts/configs are model input, and "
                      "'free a fixed component' would then cover any optimizer (sol's match). Also rejected: "
                      "heterogeneous_decomposition, relax_discrete_search_to_continuous (BO over discrete versions is not a "
                      "relaxation), decompose_and_delegate (cheap→expensive evaluation is scheduling, not delegation to a "
                      "sound solver), adapt_via_conditioning (per-task search over the conditioning text, no cross-task "
                      "conditioning; GrIPS ruling). Fully evaluated regardless.",
            "executes_pattern": None, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "population_search_executable_fitness", "H13")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2512.09108-1"): "local:2512.09108-4",
                    ("sol", "local:2512.09108-2"): f"{PS}/H13-step4",
                    ("sol", "local:2512.09108-3"): "local:2512.09108-5",
                    ("sol", "rs:generative_process_redesign/RE-2"): "local:2512.09108-1",
                    ("sol", "rs:generative_process_redesign/RE-3"): "local:2512.09108-6",
                    ("sol", "rs:generative_process_redesign/RE-6"): "local:2512.09108-3",
                    ("sol", f"{PS}/H13"): f"{PS}/H13-step3"},
            overrides={
                "local:2512.09108-1": {
                    "status": "unmet", "score_item": "E.causality", "source_strength": "common_practice",
                    "applies_when": "a new optimizer is claimed to be effective and general",
                    "reason": "Opus final (son55 question; sol rs RE-2 re-homed here after the RS card was not "
                              "assigned): no GEPA/DSPy/PromptBreeder/ADAS/AFlow or plain LLM-rewrite baseline; Table 1 is "
                              "self-rated."},
                "local:2512.09108-3": {
                    "status": "partial", "source_strength": "common_practice",
                    "applies_when": "accuracy and cost are optimised together",
                    "reason": "Opus final (son55 question; sol rs RE-6 re-homed): CrewAI's accuracy loss is disclosed with "
                              "p-values, but the optimizer accepted it with no stated constraint and no Pareto/operating-"
                              "regime view."},
                "local:2512.09108-4": {
                    "source_strength": "common_practice",
                    "applies_when": "both the evolutionary search and task execution are stochastic",
                    "reason": "Opus (sol local-1 renumbered, A4): CIs, Mann-Whitney and repeated evaluation of the final "
                              "configuration are reported; no independent search seeds — partial (A2 ladder: 2)."},
                "local:2512.09108-5": {
                    "source_strength": "common_practice",
                    "applies_when": "the optimizer, not only the winning prompt, is the contribution",
                    "reason": "Opus (sol local-3 renumbered, A4): component discovery, GA/BO and before/after configs are "
                              "described, but the platform is not shared and operator prompts/gate thresholds are "
                              "missing (opus:O03) — partial."},
                "local:2512.09108-6": {
                    "status": "unmet", "source_strength": "observed_in_reviews",
                    "applies_when": "several optimizer modules are introduced together",
                    "reason": "Opus (sol rs RE-3 re-homed as a local check after the RS card was not assigned): GA vs BO, "
                              "component discovery and the cheap LLM filter are never removed one at a time."},
                f"{PS}/H13-step3": {
                    "status": "unmet",
                    "reason": "Opus final (son55; sol's H13 holdout item merged): ALE has no separate test cases (Table 2 "
                              "'-'), Mini-SWE and CrewAI splits are not described, MathTales 50/300 overlap is unstated."},
                f"{PS}/H13-step4": {
                    "status": "partial",
                    "reason": "Opus final (son55; sol local-2 merged, both partial): optimisation hours and per-run $ are "
                              "reported; evolution token/$ cost and matched-budget baselines are not; local-model cost "
                              "ignored."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02"]),
        "assessment": son_assessment(p),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Manual tuning effort and isolated-component optimisation are "
                   "real limitations, and GEPA/DSPy/ADAS/AFlow are named, but only via a self-rated table; no measurement "
                   "that component interdependence is the bottleneck.",
                   ["son55:E001", "son55:E019", "sol:E017"]),
            "M": R("resolved", 1, "Opus sides with son55. The paper's response to its own gap (interdependent components) is "
                   "joint search with novel semantic operators, but the operators are never specified (opus:O03), the "
                   "core heuristics are proprietary (son55:E004), and in the headline ALE case prompts and search "
                   "strategies are optimised in separate runs (opus:O01, opus:O02), so the joint-optimisation logic is not "
                   "exercised. What remains is generic LLM evolution with a generic validity argument and no "
                   "distinguishing prediction — below the anchor-2 'specific mechanism with partial causal account' "
                   "(cf. r04b EvoAgentX M=1). sol's 2 credited the GA/BO/cheap-filter outline, which X already scores.",
                   ["son55:E004", "son55:E005", "son55:E006", "son55:E023", "opus:O03"], ["opus:O01", "opus:O02"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Workflow (setup → discovery → local GA / global BO → "
                   "hierarchical evaluation) and boundaries (headroom, metric clarity, cost) are described with before/"
                   "after configs; operators, fitness extraction, selection rule, retention/rollback are unspecified or "
                   "proprietary; populations of 3 for 2–3 generations.",
                   ["son55:E002", "son55:E005", "son55:E006", "son55:E009", "son55:E013", "son55:E021", "sol:E013"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Official metrics for ALE-Bench, SWE-Perf and GSM8K; "
                               "but fitness is LLM-interpreted, the CrewAI 'reporting analyst' that evaluates correctness is "
                               "itself among the optimised prompts (App. Fig. 13), and the token objective was partly met by "
                               "intentionally failing expensive problems.",
                               ["son55:E003", "son55:E007", "son55:E015", "sol:E010", "sol:E018"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only before/after comparisons against the authors' "
                             "own generic initial configs; no other optimiser, random/greedy/no-search or plain LLM-rewrite "
                             "baseline, and no ablation of any Artemis component.",
                             ["son55:E019", "son55:E020", "sol:E016"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Three of four headline results have no stated selection/"
                           "reporting separation (ALE tuned and reported on the same 40 problems; Mini-SWE and CrewAI splits "
                           "undescribed); MathTales has a 50-validation / 300-evaluation design with unstated overlap on "
                           "public GSM8K. The authors themselves flag benchmark overfitting and recommend held-out "
                           "validation they did not run (opus:O04). One partial split does not reach anchor 2 for the "
                           "paper's cross-agent claim.",
                           ["son55:E007", "son55:E008", "son55:E017", "son55:E018", "opus:O04"], ["sol:E005", "sol:E006"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked (A2 ladder: test-set CIs and repeated evaluation, no "
                              "variance across optimisation runs). Non-significant ALE (p=0.10) and the CrewAI accuracy drop "
                              "are disclosed; one evolutionary run per agent.",
                              ["son55:E010", "son55:E012", "son55:E014", "son55:E016"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Optimisation hours (671.7 h ALE, 9 h Mini-SWE) and per-run "
                        "dollar cost are reported; evolution token/$ cost, cheap-proxy cost and matched budgets are not; "
                        "MathTales hardware cost ignored.",
                        ["son55:E011", "son55:E013", "son55:E022", "sol:E014"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendix listings read (Opus read the before/after configs in full); in "
                  "scope (system_method, B-class): an optimizer whose optimised prompts/configs are retained for future "
                  "deployments. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", None,
                "outside_taxonomy=true confirmed: population search over model-input configuration has no main card "
                "(cal-dev GrIPS, r04b EvoAgentX precedent); generative_process_redesign (sol) would turn every optimizer "
                "into 'liberating a fixed component'. The H13 domain card carries the operation. Run-wide outside_taxonomy "
                "share stays well below the 30% warning.",
                ["son55:E005", "son55:E006", "son55:E023"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [],
                "Follows primary (outside_taxonomy: matches empty, reason non-empty).", ["son55:E005"], NOSCORE),
            XC(p, "local:2512.09108-1", "son55", "unmet",
               "A4 ID collision: sol's local-1 (statistics) and son55's local-1 (no competing optimizer) differ. Final local-1 "
               "= son55's question, verified unmet; sol's rs RE-2 asks the same and is merged here; sol's statistics "
               "question kept as local-4 (partial).", ["son55:E019", "sol:E016"]),
            XC(p, "local:2512.09108-2", "son55", "unmet",
               "A4 ID collision: sol's local-2 (cost reporting) and son55's local-2 (one evolutionary run per agent) differ. "
               "Final local-2 = son55's question, verified unmet (statistics cover evaluation repeats only). sol's question "
               f"merged into {PS}/H13-step4 (partial, same as son55).", ["son55:E012", "son55:E016"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", None,
               "Not carried under rs: (card not assigned). Substance verified and re-homed: local:2512.09108-1 = unmet.",
               ["son55:E019"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", None,
               "Not carried under rs: (card not assigned). Substance verified and re-homed as local:2512.09108-6 = unmet "
               "(no per-module ablation).", ["sol:E001", "sol:E002", "sol:E003"]),
            XC(p, "rs:generative_process_redesign/RE-6", "son55", None,
               "Not carried under rs: (card not assigned). Same question as son55's local-3 (multi-objective trade-off, "
               "partial); merged there.", ["son55:E014", "son55:E015", "sol:E011"]),
            XC(p, f"{PS}/F1", "son55", "unmet",
               "Failure present (status unmet = failure not avoided): a standard LLM-evolution loop applied to four agents "
               "with search-level novelty asserted, not shown.", ["son55:E002", "son55:E019", "opus:O03"]),
            XC(p, f"{PS}/F4", "son55", "partial",
               "Verified: LLM-interpreted fitness and cheap LLM proxy filters without rank-transfer check; the token "
               "objective rewarded failing expensive problems.", ["son55:E015", "son55:E023"]),
            XC(p, f"{PS}/H13", "son55", f"merged into {PS}/H13-step3 (unmet)",
               "sol's whole-sub-card item asked the selection/reporting separation question (partial, crediting "
               "MathTales). It is the same question as H13-step3; the paper-level answer is unmet because three of four "
               "cases have no split (consistent with E.holdout=1).", ["son55:E007", "son55:E008", "sol:E005"]),
            XC(p, f"{PS}/H13-step3", "son55", "unmet",
               "Verified: ALE has no separate test cases (Table 2), Mini-SWE/CrewAI splits undescribed, MathTales overlap "
               "unstated; authors' own guideline (opus:O04) not followed.", ["son55:E007", "son55:E008", "opus:O04"]),
            XC(p, f"{PS}/H13-step4", "son55", "partial",
               "Verified; sol's local-2 asked the same and also said partial (merged, A4).",
               ["son55:E011", "son55:E013", "son55:E022", "sol:E014"]),
            XC(p, f"{PS}/H13-step5", "son55", "unmet",
               "Verified: no random/greedy/no-search or single-rewrite arm; with populations of 3 over 2–3 generations, "
               "search vs a better initial prompt is untested.", ["son55:E009", "son55:E013", "son55:E020"]),
            XC(p, f"{PS}/S1", "son55", "partial",
               "Verified: novelty (semantic operators, joint tuning, hierarchical evaluation) is claimed but not isolated.",
               ["son55:E002", "son55:E019", "opus:O03"]),
            XC(p, f"{PS}/S4", "son55", "partial",
               "Verified: logs are said to be mined for signals but no example or ablation shows them steering mutation.",
               ["son55:E002"]),
            XC(p, f"{PS}/S6", "son55", "unmet",
               "Verified: the full-configuration genome is adopted from the outset with no prompt-only ceiling shown; in "
               "ALE the components are even optimised separately (opus:O01, opus:O02).",
               ["son55:E001", "son55:E006", "opus:O01", "opus:O02"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.M: the specific mechanism that answers the stated gap is unspecified (opus:O03) and not "
                "exercised as joint optimisation in the headline case (opus:O01, opus:O02); generic LLM evolution "
                "otherwise. EvoAgentX precedent (M=1).", ["son55:E004", "opus:O01", "opus:O02", "opus:O03"],
                "-5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: one partial split (MathTales, overlap unstated) out of four headline results; no "
                "split for ALE/Mini-SWE/CrewAI. sol's 2 rested on MathTales alone.",
                ["son55:E007", "son55:E008", "opus:O04"], "-2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2512.09108-3]",
             "sol_value": "partial — optimizer reconstructability (X)",
             "son55_value": "partial — multi-objective accuracy/cost trade-off (E.measurement)",
             "final_value": "local-3 = son55's trade-off question (partial; sol rs RE-6 merged); sol's question → "
                            "local:2512.09108-5 (partial)",
             "correction": "A4 hidden collision: same ID, different questions, equal status, so the mechanical diff did "
                           "not flag it.", "evidence_ids": ["son55:E014", "sol:E013"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening seats: proprietary GA/BO platform, "
                                                   "populations of 3, before/after against authors' own weak configs, no "
                                                   "competing optimizer, ALE prompt and search optimised separately, only "
                                                   "MathTales has a split. Initial bands G2 M1–2 X2 Em2 Ec1 Eh1 Es2 Ecost2; "
                                                   "evidence_level task.",
            "integrity_checks": "Both seats a1 on 2512.09108v2, material sha 96e1de0e…; canonical seat hashes equal "
                                "conflicts.json; both in scope; namespaces valid. son55 skimmed the appendix listings "
                                "structurally; Opus read them in full — the only fact bearing on a disputed field is that "
                                "the CrewAI reporting-analyst (grader) prompt is among the optimised components, used in "
                                "E.measurement (unchanged at 2).",
            "core_claim_check": "Re-read §4–7, Tables 2–3 and App. Figs 12–14; confirmed Table 2 'Test Cases' is '-' for ALE "
                                "and Mini-SWE and that ALE's two strategies are separate runs.",
            "rating_agreement": "6/8 identical and re-checked; M and E.holdout → son55.",
            "expectation_renumbering": "sol local-1 → local-4, local-2 → H13-step4, local-3 → local-5, rs RE-2 → local-1, "
                                       "rs RE-3 → local-6, rs RE-6 → local-3, rsi H13 → H13-step3.",
            "retained_vs_retained_gain": "Optimised configs are retained by construction, but a retained gain on unseen "
                                         "data is shown only for MathTales with unstated overlap; evidence_level task.",
        },
    }

    return S
