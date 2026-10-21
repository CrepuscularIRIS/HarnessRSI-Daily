"""Opus rulings for r09b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2601.02695 EvoRoute (seat Δ15): all five rating conflicts → sol (G2 M2 Em2 Eh1 Ecost2); final 46.25. Basis: the gap is "
        "framed as a 'trilemma' (stated as an argument, not shown) and its nearest neighbours are covered only in part (G). "
        "Step credit copies task-level success to every step (M). Many Table 1/3 percentages cannot be written as k/n for the "
        "stated GAIA level sizes, and the text contradicts the tables (55.15 vs 58.28; 63.18 vs 63.19), so E.measurement is "
        "capped at 2. Whether the experience base keeps writing task-success labels during the reported test streams, and "
        "what the 'Optimization Phase' tree exploration was run on, are not reported: E.holdout 1 and E.cost 2 (A2: hidden "
        "budget → cost). son55's 3s rated the seats' own listed gaps one band too high.",
        "2601.04620 AgentDevel: final 42.5, below both seats (51.25 / 46.25), reached item by item, not by averaging. M → son55 2 "
        "(the non-regression premise is checked only on the TrainSet that generates edits; reconstructibility belongs to X). "
        "E.measurement → sol 2 (same reporting-integrity cap as EvoRoute: Table 1 35.5 vs Table 3 34.2; the text's reason for "
        "rejecting iteration 11 contradicts Table 2). E.causality → son55 1 (the ungated variant tests higher, there is no "
        "rival improver, and baselines are quoted rather than rerun). E.cost → sol not_reported 0 (the only cost information "
        "is qualitative).",
        "2601.01126 RoboPhD: E.cost → son55 3 (evolution cost is disclosed as $/iteration, minutes and quota share, and the "
        "lower-cost claim is explicitly scoped to inference). RS layer: son55 outside_taxonomy, following r08b 2512.09108 / "
        "cal-dev GrIPS (population search over model-input artifacts has no main card). Domain H17 not retained (the pipeline "
        "structure is fixed by the authors; only the tool code and the instructions evolve).",
        "2601.03192 MemRL: E.causality → son55 3 (No-Memory/RAG/MemP baselines, attempt-matched Pass@10, a λ=0 value-signal "
        "ablation and a single-task control). The λ and RL-vs-non-RL ablations are reported in figures, and only the text "
        "description was available here (figure dependence noted). C03 not assigned (run convention: no canonical-schema "
        "training or category holdout).",
        "2512.19682 GenEnv: out_of_scope confirmed independently (agent GRPO and simulator RWR both update weights; the only "
        "retained non-weight state is a training-data pool). The RS record is informational only and set to "
        "self_supervised_signal_engineering/C08, the run convention for proposer–solver co-training.",
        "A4 hygiene: hidden ID collisions (same local:<key>-n, different questions) in 2601.01126, 2601.03192 and 2601.04620 "
        "were renumbered. Seat IDs with a '(met = failure avoided)' suffix were normalised. Expectations from cards that were "
        "not retained were moved to local IDs instead of being dropped. Two seat uses of 'challenged_with_evidence' to mean "
        "'the paper's claim is challenged' were corrected to unmet.",
        "No material requests: every disputed field could be answered from the pinned texts.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def XC(p, eid, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", *C(p, f"expectations[{eid}].status"), dec, final, reason, ev, NOEXP)

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

    def pmap(s, p, idx):
        return prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][idx]), s)

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def assess(s, p, extra_unresolved=()):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        return a

    def conv(old):
        return {"converted_from": old,
                "source_note": f"Moved from {old}: that card was not kept in the final pattern record (see "
                               "resolutions). The check is still a valid question about this paper's claim, so it is "
                               "kept as a paper-local expectation (A4)."}

    # =========================================================== 2512.19682 GenEnv (both out_of_scope)
    p = "2512.19682"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "agent policy is updated by GRPO (opus:O01) and the environment simulator by reward-weighted regression "
          "fine-tuning (opus:O02). The only retained non-weight state is the agent/environment training pools, which "
          "feed later weight updates (sol:E004); nothing editable is read back by a frozen agent at inference. Every "
          "reported result is a trained checkpoint. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "In our experiments, we instantiate this using Group Relative Policy Optimization (GRPO)",
                    "§2.4 Player 1 Update (Agent)", "The evaluated agent is improved in its weights."),
            opus_ev(p, "O02", "We implement this via Reward-Weighted Regression (RWR)", "§2.4 Player 2 Update (Environment)",
                    "The task generator is also improved in its weights (weighted SFT, KL-regularised)."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). A generator manufactures training tasks steered by the learner's batch "
                      "success rate (the α-band reward). A difficulty filter and a valid-trace filter gate what is used, "
                      "and both policies are retrained each epoch. This is C08's generate → steer → filter → retrain loop "
                      "in its 'closed-loop' variant, the run convention for proposer–solver co-training (r05b R-Zero, "
                      "r07a SPELL, r08b Agent0). sol's generative_process_redesign is rejected: the 'liberated' object "
                      "is the training-data distribution of a weight-training loop, not a fixed component of a generative "
                      "procedure.",
            "matches": [{
                "main_id": "self_supervised_signal_engineering", "sub_id": "C08", "role": "primary",
                "fit": "high (informational, out_of_scope)",
                "tactic_steps_checked": "generator = environment LLM; steering = α-curriculum reward on agent batch "
                                        "success; gate = |p̂−α|>k_min batches excluded from env updates and only valid "
                                        "traces enter D_train; retrain = GRPO (agent) + RWR (env), iterated per epoch.",
                "success_checks": "not assessed (out_of_scope)", "failure_checks": "not assessed (out_of_scope)",
                "evidence_ids": ["opus:O01", "opus:O02", "sol:E004"],
                "reason": "Informational identification only; no score effect."}],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": "C08",
            "domain": {"namespace": "rsi", "main": "self_generate_the_curriculum", "sub": "H22"},
            "operation_correspondence": "Generator steered by the learner's success band → filtered tasks → retrain both "
                                        "proposer and solver; H22 is the domain's proposer–solver co-training card.",
            "necessary_conditions/differences": "Informational only: both roles are weight-trained, so the H22 match "
                                                "does not bring the paper into harness scope.",
            "evidence_ids": ["opus:O01", "opus:O02"]}],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b/r06a/r07a/r08b).",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; benchmark gains are author-reported "
                                             "results of trained 7B checkpoints.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results "
                                      "are wrong."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "sol", "component_training",
                "Informational: the evaluated product is a trained agent model (plus a trained simulator). Same as r08b "
                "Agent0/R-Few. son55's null is also allowed for an excluded row.", ["opus:O01", "opus:O02"],
                "none (out_of_scope row; claim_type is identification only)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "revised", None,
                "For out-of-scope rows the canonical value is null (precedent r05b–r08b). The task/retained/improver "
                "ladder does not apply to weight-level work. sol's 'task' was descriptive; son55's 'not_assessed' is "
                "not in the enum.", ["opus:O01", "opus:O02"], "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Null is canonical for out-of-scope rows. Claim support is not assessed under this rubric (sol's "
                "'scoped' and son55's 'not_assessed' both replaced).", ["opus:O01"], "none"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "revised", "self_supervised_signal_engineering",
                "Informational. The run convention for generator/solver co-training is C08. The steering signal (the "
                "learner's success rate) and the filters fit C08's closed-loop variant. sol's generative_process_redesign "
                "would make any curriculum method 'liberate a fixed component'. son55 skipped identification (allowed for "
                "out_of_scope).", ["opus:O01", "opus:O02", "sol:E004"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["self_supervised_signal_engineering", "C08"]],
                "Follows primary.", ["opus:O01", "opus:O02"], NOSCORE),
            XC(p, "rsi:self_generate_the_curriculum/S1", "sol", "partial",
               "Verified (informational): only well-formed, evaluable traces enter D_train, but the validity of generated "
               "references/specifications is not independently audited. No score effect.", ["sol:E004"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–2 (data flow, Algorithm 1) and §4 setup before opening the "
                                                   "seats: GRPO agent + RWR simulator, both Qwen2.5-7B, pools are "
                                                   "training data → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2512.19682v2, material sha 424407a5…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01/O02 and sol:E004.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2601.01126 RoboPhD (Δ1.25)
    p = "2601.01126"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Since evolution is a one-time training cost while inference is ongoing",
                    "§4.2 Main Results, takeaway (2)",
                    "The lower-cost claim is explicitly limited to per-query inference; evolution cost is disclosed "
                    "separately ($/iteration, minutes, quota share)."),
            opus_ev(p, "O02", "the evolutionary agent maintains context across the entire process of creating an agent package",
                    "§3.1", "The improver's context lasts for one package-creation session only; there is no curated "
                    "cross-iteration memory. This is why adapt_via_conditioning / H15 do not apply (unlike r08b "
                    "AccelOpt)."),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "Opus confirms son55. The executed operation is LLM-operator population evolution with ELO "
                      "selection over a two-artifact agent package (a deterministic analysis script whose output becomes "
                      "the prompt, plus instruction text) against an execution-accuracy fitness. Run precedent (cal-dev "
                      "GrIPS, r04b EvoAgentX, r08b 2512.09108): population search over model-input artifacts has no main "
                      "card. generative_process_redesign (sol) would turn every optimizer into 'liberating a fixed "
                      "component'. Also rejected: adapt_via_conditioning (no curated cross-iteration experience is read "
                      "by the executor, opus:O02) and decompose_and_delegate/C25 (it describes only the fixed scaffold "
                      "analysis→SQL→verification, not the evolved operation). The domain card H14 carries the operation. "
                      "The paper is fully evaluated regardless.",
            "executes_pattern": None, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H14")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.01126-1"): "local:2601.01126-5",
                    ("sol", "rs:generative_process_redesign/RE-1"): "local:2601.01126-6",
                    ("son55", "rsi:population_search_executable_fitness/F1 (met = failure avoided)"):
                        "rsi:population_search_executable_fitness/F1",
                    ("son55", "rsi:search_agent_architecture/S6"): "local:2601.01126-7",
                    ("son55", "rsi:search_agent_architecture/F1 (met = failure avoided)"): "local:2601.01126-8"},
            overrides={
                "local:2601.01126-3": {
                    "status": "unmet",
                    "reason": "Opus (status revised from 'challenged_with_evidence', which is for a paper that rebuts an "
                              "expectation with evidence). Here the expectation is a control for the evolution executor, "
                              "and the paper gives none. Evolution ran with Haiku as executor (sol:E009), so the larger "
                              "Haiku gain is confounded with the tuning target. The skip-a-tier margins are +0.4 and "
                              "+0.2 points without uncertainty. Unmet."},
                "local:2601.01126-5": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = champion "
                                               "selection rule)."},
                "local:2601.01126-6": dict(conv("rs:generative_process_redesign/RE-1")),
                "local:2601.01126-7": dict(conv("rsi:search_agent_architecture/S6")),
                "local:2601.01126-8": dict(conv("rsi:search_agent_architecture/F1")),
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Manual engineering of Text-to-SQL systems is a real "
                   "limitation. Neighbours are prompt optimizers and BIRD systems; code-level agent-evolution neighbours "
                   "and an optimizer head-to-head are missing; the residual is not sharply bounded.",
                   ["son55:E001", "son55:E011", "sol:E017"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Error-report-fed proposal, Deep Focus refinement on prior "
                   "iterations, a persistent ELO archive and same-question head-to-head evaluation form a reasoned "
                   "response to hand-fixed tool/instruction design. Not 4: no distinguishing prediction against a "
                   "simpler optimizer is tested, and the non-transitivity rationale for ELO is asserted, not shown.",
                   ["son55:E003", "son55:E005", "sol:E005", "sol:E006"], ["son55:E011"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Artifacts, information access, selection protocol (App. D), "
                   "tool-only interface and deployment are reconstructable. Not 4: the rule that picked the 'Best "
                   "Evolved' package for dev/test is not stated, and the late-stage challenger schedule is hand-set.",
                   ["son55:E005", "son55:E015", "sol:E002", "sol:E007"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. BIRD execution accuracy (set-equivalence) is "
                               "used throughout; the official test is executed by the BIRD team. Not 4: the per-iteration "
                               "fitness uses 150 questions (noisy), and the dev denominator is not restated.",
                               ["son55:E006", "son55:E017", "sol:E006", "sol:E015"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. The only comparison is evolved vs a deliberately "
                             "trivial naive package on the same executor. There is no ELO/archive, Deep Focus, "
                             "tool-vs-instructions, alternative-optimizer or strong hand-written control. The strategy "
                             "comparison is asserted without data. The inverse-scaling claim is confounded by "
                             "Haiku-based evolution.",
                             ["son55:E007", "son55:E008"], ["son55:E011", "sol:E011", "sol:E009"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Evolution on the 69 train DBs; dev DBs are disjoint; "
                           "the official test is held and run by the BIRD team. Not 4: the champion-selection rule and any "
                           "dev use during framework development are unreported, and pretraining contamination of BIRD "
                           "is not discussed.",
                           ["son55:E016", "son55:E017", "sol:E015"], ["son55:E015"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). A single evolutionary campaign; "
                              "the authors acknowledge amplifying non-determinism but give no repeats or intervals. "
                              "Sample sizes per iteration and a negative sub-result (Simple −0.32) are reported.",
                              ["son55:E014", "sol:E014", "sol:E008"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Per-query cost for all three tiers before/after "
                        "evolution, $2 and 22 min per iteration, quota share for a 30-iteration run, hardware, and the "
                        "tool-failure cost share are disclosed. The lower-cost claim is explicitly limited to inference "
                        "(opus:O01). Not 4: evolution cost is not expressed in tokens/$, and there is no budget-matched "
                        "alternative optimizer (the missing control is charged to E.causality).",
                        ["son55:E009", "son55:E010", "sol:E012", "opus:O01"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–E read. In scope (system_method, A class): retained "
                  "non-weight code + instruction package evolved from execution feedback and deployed unchanged. All "
                  "eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", None,
                "outside_taxonomy confirmed, following r08b 2512.09108 / cal-dev GrIPS: population search over model-input "
                "artifacts (prompt text plus a script whose only output is prompt text) has no main card. sol's "
                "generative_process_redesign would cover any optimizer. No curated cross-iteration memory exists for "
                "adapt_via_conditioning (opus:O02).", ["son55:E002", "son55:E003", "opus:O02"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [],
                "Follows primary (outside_taxonomy: matches empty, reason non-empty).", ["son55:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["population_search_executable_fitness", "H14"]],
                "H14 kept (both seats). son55's H17 is not retained: search_agent_architecture lifts roles, topology or "
                "module composition into the search space, but here the pipeline (offline tool → prompt → universal "
                "verification) is fixed by the authors and only the tool code and instruction text evolve (sol:E016, "
                "§4.3 'learning to work within the authors' system design'). son55's two H17 checks are kept as "
                "local-7/local-8.", ["sol:E016", "son55:E001"], NOSCORE),
            XC(p, "local:2601.01126-1", "son55", "unknown",
               "A4 ID collision. sol's local-1 (autonomy claim narrower than stated, G) and son55's local-1 (champion "
               "selection rule, E.holdout) are different questions. Final local-1 = son55's, verified: the text never "
               "says how 'Best Evolved' was chosen for dev/test. sol's question is kept as local-5 (partial, verified: "
               "the tool-only mandate and the hand-written strategy are author design).",
               ["son55:E015", "sol:E004", "sol:E016"]),
            XC(p, "local:2601.01126-2", "son55", "unmet",
               "Verified: a single campaign; non-determinism is acknowledged (App. B) but there are no repeats or "
               "intervals.", ["son55:E014"]),
            XC(p, "local:2601.01126-3", "revised", "unmet",
               "Substance verified (Haiku was the evolution executor; margins 0.4/0.2 points). The status is corrected: "
               "'challenged_with_evidence' records a paper rebutting an expectation, whereas here the paper simply "
               "lacks the control.", ["son55:E007", "son55:E009", "sol:E009"]),
            XC(p, "local:2601.01126-4", "son55", "partial",
               "Verified: $/iteration, minutes and quota share are reported; evolution cost is not in tokens/$.",
               ["son55:E009", "son55:E010"]),
            XC(p, "rs:generative_process_redesign/RE-1", "revised", {"moved_to": "local:2601.01126-6", "status": "partial"},
               "The card is not retained (outside_taxonomy). The question (does any single component explain the gain?) "
               "is still valid and is kept as local-6, partial: the whole package beats naive, but no component is "
               "isolated.", ["sol:E011", "sol:E012"]),
            XC(p, "rsi:population_search_executable_fitness/F1 (met = failure avoided)", "son55", "partial",
               "ID normalised to rsi:population_search_executable_fitness/F1 (A4). Verified: a generic evolve-and-test "
               "loop on one domain, with ELO/Deep Focus as the only search-level additions, both unablated → failure "
               "partly present.", ["son55:E002", "son55:E011"]),
            XC(p, "rsi:population_search_executable_fitness/H14", "sol", "partial",
               "Verified: search uses train DBs and the private test is separate, but a single campaign has no search "
               "variance and no matched optimizer.", ["sol:E008", "sol:E015"]),
            XC(p, "rsi:population_search_executable_fitness/S4", "sol", "met",
               "Verified: the error-analysis report and unique-correct/incorrect question lists are given to the "
               "proposer.", ["sol:E003", "sol:E005"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "unmet",
               "Verified: no ELO/archive/challenger ablation; there is no negative-evidence credit.",
               ["son55:E002", "son55:E005"]),
            XC(p, "rsi:search_agent_architecture/F1 (met = failure avoided)", "revised",
               {"moved_to": "local:2601.01126-8", "status": "unmet"},
               "H17 is not retained. The check (tool vs instructions vs verification not separated) is valid and is kept "
               "as local-8, unmet.", ["son55:E001", "son55:E019"]),
            XC(p, "rsi:search_agent_architecture/S6", "revised", {"moved_to": "local:2601.01126-7", "status": "met"},
               "H17 is not retained. The check (frozen package certified away from where it was found: disjoint dev "
               "DBs, three executors, official test) is valid and is kept as local-7, met.",
               ["son55:E007", "son55:E008", "son55:E016"]),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.cost. Real costs are disclosed in several units and the cost claim is explicitly scoped "
                "(opus:O01). sol's 'not matched against other optimizers' is the missing-control gap already charged "
                "to E.causality (1).", ["son55:E009", "son55:E010", "opus:O01"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: tool+instruction package "
                                                   "evolved on BIRD train with Haiku executor, ELO archive, naive-only "
                                                   "control, official test +1.51, single campaign. Initial bands G2 M3 "
                                                   "X3 Em3 Ec1 Eh3 Es1 Ecost2–3; evidence_level retained.",
            "integrity_checks": "Both seats a1 on 2601.01126v2, material sha 51846a26…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid (son55 outside_taxonomy with empty matches).",
            "core_claim_check": "Re-read §3.2.4–3.2.6, §4.1–4.3, App. A.4–A.5, D; confirmed the evolution executor "
                                "(Haiku) and the test protocol.",
            "rating_agreement": "7/8 identical and re-checked; E.cost → son55.",
            "expectation_renumbering": "sol local-1 → local-5 (A4 collision); sol RE-1 → local-6, son55 H17 S6/F1 → "
                                       "local-7/8 (cards not retained); son55 F1 suffix normalised.",
            "retained_vs_retained_gain": "The retained package is deployed unchanged on disjoint dev DBs and the "
                                         "official test → retained (author-reported, single campaign). No improver "
                                         "evidence (meta-evolution excluded by the authors).",
        },
        "figure_dependence": None,
    }

    # =========================================================== 2601.02695 EvoRoute (Δ15)
    p = "2601.02695"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "during the Optimization Phase, the system engages in a tree-based exploration, sampling "
                    "multiple trajectories for a given task to proactively populate and diversify its knowledge base on "
                    "model behaviors", "§1 Introduction",
                    "A second write phase that samples several trajectories per task is announced, but neither its "
                    "tasks, nor its labels, nor its cost are specified anywhere (App. A describes only the 50-task "
                    "uniform-random TaskCraft cold start)."),
            opus_ev(p, "O02", "Crucially, this selection is not the end of the process.", "§4.3 closing paragraph",
                    "The method writes outcomes back after every decision. The records carry the task-level success "
                    "P(τ) (Eq. 5), which needs a label, yet no experiment says whether this write-back ran on the "
                    "reported test streams."),
            opus_ev(p, "O03", "reaches a strong", "§5.2 (text continues '55.15% on GAIA')",
                    "The text gives Claude-4+CK-Pro as 55.15% on GAIA; Table 1 gives 58.28. The text also gives "
                    "EvoRoute 63.18 against the table's 63.19."),
            opus_ev(p, "O04", "73.91", "Table 1, Smolagent EvoRoute GAIA Level 1",
                    "73.91% is not k/53 (39/53 = 73.58, 40/53 = 75.47). Other cells are also not attainable as single "
                    "passes on the App. D level sizes: CK-Pro EvoRoute L3 33.33 (k/26), All 63.19 (k/165), Claude-4 L3 "
                    "37.50, Table 3 76.50 and 81.50 (k/53). Some unreported averaging, rescoring or subset was used."),
            opus_ev(p, "O05", "manually configured weights", "§5.1 Parameter Configurations",
                    "Utility weights and θ_sim=0.85 are hand-set; the data used to choose them is not stated."),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Opus revised. The load-bearing move replaces a uniform, human-fixed role→model map with treatment "
                      "differentiated per sub-task step: cheap models on routine steps, strong ones on planning "
                      "(Fig. 4). This is heterogeneous_decomposition at parent level; sub null because C04 is "
                      "compression of a trained artifact. son55's adapt_via_conditioning is kept as supporting (partial): "
                      "each decision is conditioned at inference on retrieved precedent from an experience base built "
                      "from the system's own executions, with no parameter update. This follows the run convention for "
                      "experience-store systems (r04a AgentNet, r05b Memento). Its RE checks on conditioning-source "
                      "coverage and contamination apply directly. son55's primary reframe_as_solvable_object is not "
                      "retained: routing is already a selection problem, and applying a Pareto filter plus Thompson "
                      "sampling is re-application of standard machinery, not a recast of an intractable problem into a "
                      "solvable object (that card's own RE-3). Its RE-1 question is kept as local-4.",
            "matches": [
                smatch("sol", p, "heterogeneous_decomposition", role="primary"),
                smatch("son55", p, "adapt_via_conditioning", role="supporting",
                       reason="Per-step routing is conditioned on retrieved step records from a store built from the "
                              "system's own executions, without parameter updates. Partial: the conditioned object is a "
                              "non-parametric selector, not the LLM; C03 not selected (no trained schema parser)."),
            ],
            "executes_pattern": "partial",
            "resolves_problem": "partial: cost/latency reductions at comparable accuracy are author-reported single runs "
                                "with unexplained table arithmetic (opus:O04); continual self-evolution is not isolated.",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [],
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("son55", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "rsi:index_experience_for_reuse/F3 (met = failure avoided)"):
                        "rsi:index_experience_for_reuse/F3",
                    ("son55", "rs:reframe_as_solvable_object/RE-1"): "local:2601.02695-4",
                    ("son55", "rsi:search_agent_architecture/S6"): "local:2601.02695-5"},
            overrides={
                "rsi:index_experience_for_reuse/S2": {
                    "status": "unmet", "score_item": "X",
                    "reason": "Opus final (son55): S2 asks that writes be gated by an external check. Eq. 6 appends "
                              "every step record unconditionally; the success flag is stored, not used to admit. sol's "
                              "'partial' credited that failures are legitimately labelled data, which concerns label "
                              "quality, not gating."},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "unknown",
                    "reason": "Both seats unknown (same check; son55's suffix ID normalised). The method writes outcomes "
                              "back after each decision (opus:O02), and an 'Optimization Phase' samples several "
                              "trajectories per task (opus:O01). Whether either ran on the evaluation streams is not "
                              "stated, so whether the store was built from the test stream cannot be determined."},
                "local:2601.02695-4": dict(conv("rs:reframe_as_solvable_object/RE-1")),
                "local:2601.02695-5": dict(conv("rsi:search_agent_architecture/S6")),
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O03", "opus:O04"]),
        "assessment": assess("sol", p, [
            "Table 1/3 percentages not attainable as k/n on the stated GAIA level sizes; text–table mismatches "
            "(opus:O03, opus:O04).",
            "What the 'Optimization Phase' tree exploration ran on, and its cost (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The changed object (a static, human-fixed role→model map) and "
                   "its cost/latency consequences are concrete. Router neighbours are named and three are run. But the "
                   "'trilemma' is a framing, not a shown impossibility. Neighbours from cascading/cost-aware routing "
                   "and from experience-memory agents are not differentiated, and the remaining gap is only partly "
                   "bounded. son55's own reason states the anchor-2 description; its basis for 3 (run router "
                   "baselines) is evidence, not gap.",
                   ["sol:E010", "son55:E002", "son55:E021"], ["son55:E020"]),
            "M": R("resolved", 2, "Opus sides with sol. Record → union retrieval → Pareto filter → NIG-Thompson utility "
                   "→ append is a coherent response to heterogeneous step demands. But the key assumption that a "
                   "step's value can be estimated from P(τ)·σ_t (whole-task success copied to every step) is weak and "
                   "untested. Normal/NIG posteriors on bounded or binary outcomes and hand-set utility weights "
                   "(opus:O05) are not justified. No distinguishing prediction against a static tuned map is offered. "
                   "son55's own reason lists these weaknesses; reconstructibility belongs to X.",
                   ["sol:E001", "sol:E003", "sol:E004", "sol:E005", "sol:E006", "son55:E007"], ["opus:O05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. The write/retrieve/select chain, model pool, prices and "
                   "parameters are specified. The Optimization Phase (opus:O01), the timing of the end-of-trajectory "
                   "label relative to per-step write-back, few-sample posteriors, store growth, de-duplication and "
                   "staleness are unspecified.",
                   ["sol:E001", "sol:E002", "sol:E007", "son55:E006", "opus:O01"], ["son55:E008"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol, on a wider basis. The standard benchmark scorers "
                               "and price-based cost are credible in themselves. But the reported numbers cannot all "
                               "come from the stated evaluation sets: several Table 1/3 percentages are not k/n on the "
                               "App. D level sizes (opus:O04), and the text contradicts the table (55.15 vs 58.28; 63.18 "
                               "vs 63.19, opus:O03). The task-success label source used in the records is unspecified. "
                               "son55 noted the attainability cells under E.statistics. Here the issue is whether the "
                               "reported results are what the stated verifier produced, which A2 assigns to measurement. "
                               "E.statistics stays 1 on its own single-run basis, so there is no double charge.",
                               ["sol:E013", "sol:E015", "son55:E023"],
                               ["opus:O03", "opus:O04", "son55:E018", "son55:E019"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There are fixed-model and three router "
                             "baselines, and four component removals (cold-start K, retrieval facets, Thompson, Pareto). "
                             "But the ablations are GAIA-L1-only single runs. There is no static tuned map, random "
                             "routing or frozen-vs-online K control, so the 'self-evolving' part is not isolated. The "
                             "routers' training data and budget are not described.",
                             ["sol:E010", "sol:E011", "sol:E012", "son55:E014", "son55:E015"],
                             ["son55:E016", "sol:E017"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. The cold-start store comes from 50 TaskCraft tasks "
                           "separate from the benchmarks (a real positive). But the central claim is continual "
                           "self-evolution from environment feedback. The method writes back records that carry "
                           "task-success labels (opus:O02), and an unspecified Optimization Phase samples several "
                           "trajectories per task (opus:O01). The paper never says whether either ran on the evaluation "
                           "streams, i.e. whether gold labels of test items entered K (A2: oracle/true-label feedback → "
                           "holdout). θ_sim and the utility weights have no stated selection data. With the core "
                           "protocol unreported, the held-out support for the self-evolution claim is below anchor 2.",
                           ["sol:E008", "son55:E009"], ["opus:O01", "opus:O02", "sol:E017", "son55:E022", "opus:O05"],
                           ["§§1, 4–5 and Apps. A–E: no test-stream order, frozen-store report, label-access protocol "
                            "or Optimization-Phase task source."]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Task counts and a negative "
                              "architecture result are given; every main and ablation number is a single point "
                              "estimate with no seeds, intervals or tests; ablation conclusions rest on 53 tasks.",
                              ["sol:E015", "sol:E016", "son55:E017"], ["son55:E016"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Cost and delay are primary outcomes for every method, "
                        "with a price table and a $28.8/3.6 h cold start. But the Optimization Phase, which samples "
                        "several trajectories per task (opus:O01), has no reported cost, and neither do PredictTools' "
                        "LLM fallback, embedding calls, or the baseline routers' training budgets. The headline "
                        "'up to 80%' saving therefore may exclude part of the method's own budget (A2: an unequal or "
                        "hidden budget is charged to cost).",
                        ["sol:E009", "sol:E013", "son55:E011", "son55:E023"], ["opus:O01"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–E read. In scope (system_method, A class): a non-weight "
                  "step-level experience store, written from the system's own executions and read by the router on "
                  "later tasks. All eight items resolved; the protocol gaps are rated, not treated as missing material.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "heterogeneous_decomposition",
                "See rs_pattern.reason. The executed load-bearing move is differentiated per-step model assignment "
                "instead of a uniform fixed map. Pareto+Thompson is standard selection machinery applied to a problem "
                "that is already a selection (reframe RE-3: re-application), so it is not the primary.",
                ["sol:E003", "sol:E005", "son55:E002"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["heterogeneous_decomposition", None], ["adapt_via_conditioning", None]],
                "Primary from sol. son55's adapt_via_conditioning is kept as supporting: retrieved precedent conditions "
                "each decision without parameter updates (run convention for experience stores). son55's "
                "reframe_as_solvable_object is not kept.", ["son55:E004", "son55:E006", "sol:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["index_experience_for_reuse", "H03"]],
                "H03 kept (both seats). son55's H18 (co-evolve roles and topology at test time) is not retained: roles, "
                "scheduler and topology are the host framework's and unchanged; only the backbone per step varies. "
                "son55's H18 S6 check is kept as local-5.", ["son55:E002", "sol:E001"], NOSCORE),
            XC(p, "local:2601.02695-1", "son55", "unknown",
               "Verified: Tables 1/2 do not say whether the embedding, PredictTools fallback or cold-start costs are "
               "included.", ["son55:E011", "son55:E023"]),
            XC(p, "local:2601.02695-2", "son55", "unknown",
               "Verified: the training data and budget of PromptLLM/GraphRouter/MasRouter are not described.",
               ["son55:E013"]),
            XC(p, "local:2601.02695-3", "son55", "unmet",
               "Verified, and widened by opus:O04 (also Smolagent L1 73.91, CK-Pro All 63.19, Claude-4 L3 37.50, Table 3 "
               "81.50). No repeats or intervals.", ["son55:E017", "son55:E018", "son55:E019", "opus:O04"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Applies (card kept as supporting). The empty-K and retrieval-facet ablations exist, but only on GAIA L1 "
               "and as single runs.", ["son55:E014", "son55:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap or contamination analysis between K and the evaluation items, and no statement "
               "on K updates during evaluation (opus:O02).", ["son55:E022", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no random routing, static tuned map or cheap-for-simple-roles heuristic.",
               ["son55:E012", "son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: cold-start vs empty only; no K-size sweep or cross-framework store reuse.",
               ["son55:E011", "son55:E014"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "sol", "partial",
               "Verified: efficiency is measured in deployment units (dollars, wall-clock hours); amortised and "
               "auxiliary costs are not.", ["sol:E009", "sol:E013", "sol:E014"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "sol", "partial",
               "Verified: fixed-model and router baselines exist; no static per-role tuned map isolates per-step "
               "differentiation from simple role-level assignment.", ["sol:E010", "sol:E011", "sol:E012"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "revised", {"moved_to": "local:2601.02695-4", "status": "unmet"},
               "The card is not retained. The question (does the Pareto/Thompson solution actually answer the trilemma "
               "beyond end metrics?) is valid and is kept as local-4, unmet.", ["son55:E005", "son55:E007"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "same_supported_fact", "unknown",
               "Both seats unknown on the same check (son55 under a suffixed ID). Verified: write-back is part of the "
               "method (opus:O02), and the evaluation protocol does not say whether it ran on test streams.",
               ["sol:E007", "son55:E006", "opus:O02"]),
            XC(p, "rsi:index_experience_for_reuse/F3 (met = failure avoided)", "same_supported_fact", "unknown",
               "Same check as rsi:index_experience_for_reuse/F3; ID normalised (A4) and merged.", ["son55:E022", "opus:O01"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "unmet",
               "S2 asks for an external write gate. Eq. 6 appends every record; the success flag is not an admission "
               "test. sol's partial rested on label legitimacy, not gating.", ["sol:E002", "son55:E003"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "sol", "partial",
               "Verified: the store is certified by removal (empty K: 83.02→69.81) on GAIA L1 only; updates are not "
               "frozen.", ["sol:E011"]),
            XC(p, "rsi:search_agent_architecture/S6", "revised", {"moved_to": "local:2601.02695-5", "status": "partial"},
               "H18 is not retained. The check (design certified away from where it was found: TaskCraft source vs "
               "five benchmarks, with the test-stream protocol open) is kept as local-5, partial.",
               ["son55:E009", "son55:E013"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G. son55's reason itself describes anchor 2 (neighbours and gap boundary only partly "
                "drawn; 'trilemma' is a framing). Run baselines are evidence, not gap.",
                ["son55:E002", "son55:E021", "sol:E010"], "-3.75 vs son55 (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.M. The step-credit assumption (task success copied to every step), the NIG assumptions and "
                "the hand-set weights are untested, with no distinguishing prediction against simpler routing. son55 "
                "listed the same weaknesses and still gave 3.",
                ["sol:E004", "sol:E006", "son55:E007", "opus:O05"], "-5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement. The verifiers are standard, but several reported percentages are not "
                "attainable on the stated sets and the text contradicts the tables (opus:O03, opus:O04), so the "
                "reported results cannot be fully tied to the stated measurement. Counted here only; E.statistics "
                "stays 1 on single-run grounds.",
                ["sol:E013", "opus:O03", "opus:O04", "son55:E019"], "-2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout. The separate TaskCraft bootstrap is real, but whether labelled write-back and "
                "the multi-trajectory Optimization Phase touched the evaluation streams is unreported, and that is "
                "the protocol that the central self-evolution claim depends on.",
                ["sol:E008", "opus:O01", "opus:O02", "son55:E022"], "-2.5 vs son55 (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.cost. Cost is a primary outcome, but the method's own exploration budget (Optimization "
                "Phase) and auxiliary calls are unaccounted, and the router baselines' budgets are unknown.",
                ["sol:E009", "son55:E011", "opus:O01"], "-1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: step-level append-all "
                                                   "store with union retrieval + Pareto + NIG-Thompson; TaskCraft cold "
                                                   "start; single-run tables whose GAIA percentages partly fail k/n; "
                                                   "L1-only ablations; unspecified Optimization Phase and test-stream "
                                                   "write-back. Initial bands G2 M2 X2 Em1–2 Ec2 Eh1 Es1 Ecost2; "
                                                   "evidence_level retained (bootstrap store ablation), claim scoped.",
            "integrity_checks": "Both seats a1 on 2601.02695v1, material sha 779d6c9a…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid; son55 suffixed F3 ID normalised.",
            "core_claim_check": "Recomputed GAIA cells against 53/86/26/165 (opus:O04); confirmed the text–table "
                                "mismatches (opus:O03); re-read §1 Optimization Phase vs App. A (opus:O01) and §4.3 "
                                "write-back (opus:O02).",
            "rating_agreement": "3/8 identical and re-checked (X, E.causality, E.statistics); G, M, E.measurement, "
                                "E.holdout, E.cost → sol.",
            "delta_explained": "Seat Δ15 = son55 one band higher on five items. The gap and mechanism weaknesses that "
                               "son55 itself listed match anchor 2. son55 placed the attainability anomaly under "
                               "statistics, where it had no effect, and under-weighted the unreported "
                               "write-back/Optimization-Phase protocol.",
            "retained_vs_retained_gain": "Retained: a store bootstrapped from separate tasks improves later GAIA L1 "
                                         "tasks (single run). Continual retained improvement from online write-back is "
                                         "claimed but not isolated.",
        },
        "figure_dependence": "Fig. 3 (radar) and Fig. 4 (selection shares) are described in text only; no rating "
                             "depends on them.",
    }

    # =========================================================== 2601.03192 MemRL (Δ3.75)
    p = "2601.03192"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Optional repeat-attempt reflection note", "App. I.2 HLE generation prompts",
                    "On HLE, a repeated attempt may carry 'Result: {CORRECT | INCORRECT}' for the same question's previous "
                    "attempt, i.e. a gold-label signal in the prompt. Whether it was enabled in Table 1 is not stated "
                    "(A2: oracle retry signal → holdout)."),
            opus_ev(p, "O02", "Full set (Runtime only)", "App. E.3 Table 9",
                    "HLE has no held-out split, yet App. C.1 reuses the HLE-trained bank for 'cross-model transfer' on "
                    "HLE. Those gains are re-exposure, which the authors themselves call runtime memorisation (B.3)."),
            opus_ev(p, "O03", "plateaus due to an inability to filter functional distractors", "§5.3.2 (Figure 5 text)",
                    "λ=0 (similarity only) vs λ=0.5 is a clean ablation of the value signal inside the same system. Its "
                    "numbers are in a figure; only the text description is available in the pinned material."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["reframe_as_solvable_object"], "outside_taxonomy": False,
            "reason": "Opus confirms son55. Primary adapt_via_conditioning, sub null: a frozen backbone solves later "
                      "tasks conditioned on retrieved experience. C03 is not assigned under the run convention (r08b "
                      "AccelOpt): there is no upstream training of a schema parser and no category-level holdout "
                      "(ALFWorld transfer is seen task types). Supporting reframe_as_solvable_object, sub null, partial: "
                      "memory selection is recast as a one-step value decision with Monte-Carlo/EMA updates. This is a "
                      "distinct executed operation (the Q-reranking) that its RE-4 check addresses; the recast is "
                      "inherited from M-MDP.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"), smatch("son55", p, "reframe_as_solvable_object")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "evidence_gated_retention", "H29"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.03192-2"): "local:2601.03192-1",
                    ("sol", "local:2601.03192-1"): "local:2601.03192-4",
                    ("son55", "rsi:index_experience_for_reuse/F3 (met = failure avoided)"):
                        "rsi:index_experience_for_reuse/F3"},
            overrides={
                "local:2601.03192-1": {"note": "sol's local-2 and son55's local-1 are the same statistics check (both "
                                               "unmet); merged."},
                "local:2601.03192-4": {"note": "sol's local-1 (GEM/monotonic-improvement argument, M) renumbered (A4 "
                                               "collision with son55's local-1)."},
                "rsi:evidence_gated_retention/S5": {
                    "status": "met",
                    "reason": "Opus revised (sol partial). S5 asks that the cost of the gate be stated openly. The gate "
                              "here (z-scored rerank + scalar EMA) is stated as millisecond-level, with HLE token "
                              "parity (~32K/question) and per-epoch wall-clock against MemP. Missing full-benchmark "
                              "totals are an E.cost matter (local-3), not a hidden gate cost."},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "partial",
                    "reason": "Opus final (sol; son55's suffixed ID normalised). Failure present for the runtime table "
                              "(the store is built and scored on the same labelled stream), for HLE, and for the HLE "
                              "cross-model 'transfer' (opus:O02). It is avoided for the frozen-bank transfer on "
                              "OS/DB/BCB held-out splits and ALFWorld valid_seen. Partly present → partial."},
            }),
        "claims": lambda c: add_counter(c, "C4", ["opus:O02"]),
        "assessment": assess("son55", p, [
            "Whether the HLE repeat-attempt CORRECT/INCORRECT note was enabled in reported runs (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Similarity-only retrieval vs functional utility is a sourced, "
                   "concrete limitation; the RAG/agentic-memory neighbour families are run as baselines; M-MDP "
                   "(learned retrieval) is cited and its formulation adopted. Not 4: the delta to M-MDP's parametric "
                   "retrieval is not run, and the remaining-gap boundary is partly drawn.",
                   ["son55:E001", "sol:E001", "sol:E006"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Value-aware rerank (z-scored sim/Q mix), similarity gating "
                   "and an EMA on injected items form a coherent, testable response (prediction: λ=0 plateaus). Not 4: "
                   "co-injected credit is shared, the Q has no memory-off baseline, and the GEM 'guarantee' does not "
                   "follow for TopK retrieval over a growing bank (local-4).",
                   ["son55:E004", "son55:E005", "opus:O03"], ["son55:E019", "sol:E012", "sol:E013"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Write, recall, rerank, inject and update steps plus all "
                   "hyper-parameters and prompts (App. E, I) are reconstructable; low-similarity fallback stated. Not 4: "
                   "no admission, retirement, size bound, versioning or rollback.",
                   ["son55:E002", "son55:E003", "son55:E004", "son55:E022"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Standard benchmark verifiers/rewards; SR and "
                               "CSR are defined; CSR vs Pass@10 is attempt-matched. Not 4: the HLE grader is not "
                               "described, and CSR is monotone by construction (CSR is not used as stability evidence "
                               "here).", ["son55:E007", "son55:E009", "sol:E014"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. Same-backbone No-Memory, RAG, Self-RAG, Mem0, MemP "
                             "and attempt-matched Pass@10 baselines; a λ sweep in which λ=0 removes the value signal "
                             "inside MemRL (opus:O03); RL vs non-RL counterparts on OS; and a single-task control. Each "
                             "isolates part of the claim. Not 4: the λ and RL-vs-non-RL ablations exist only as figures "
                             "(text description only here) and on one benchmark each; there is no alternative utility "
                             "estimator or write-gate ablation; MemP margins are small. sol's per-entry credit concern "
                             "is a mechanism limitation (M, evidence_gated_retention/S1), not a missing system-level "
                             "control. Single-run noise is charged to E.statistics (A2).",
                             ["son55:E017", "son55:E018", "son55:E009", "son55:E027", "opus:O03", "sol:E006"],
                             ["son55:E026", "sol:E007"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked, and the basis is widened. Table 2 freezes the bank "
                           "and tests held-out OS/DB/BCB splits and ALFWorld valid_seen (seen types). The headline Table 1 "
                           "replays the same labelled tasks for 10 epochs. HLE has no held-out split, and its cross-model "
                           "'transfer' re-tests the same questions (opus:O02). 'Best validation results' is undefined. "
                           "An optional CORRECT/INCORRECT note from the previous attempt exists for HLE (opus:O01). "
                           "Not lower: the transfer claims on four of five domains rest on a real held-out split.",
                           ["son55:E010", "son55:E012", "sol:E003"],
                           ["son55:E011", "son55:E013", "son55:E015", "son55:E016", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Task counts and ties/negative "
                              "results are reported (DB tie, HLE single-task tie); a single run and one split seed; no "
                              "intervals or tests.", ["son55:E014", "son55:E017"], ["son55:E009"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. HLE tokens (~32K/question) and per-epoch wall-clock "
                        "against MemP are reported; per-benchmark totals, memory growth, and embedding/summarisation "
                        "overhead are not.", ["son55:E023", "sol:E011"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–I read (long proof derivations skimmed). In scope "
                  "(system_method, A class): a retained, non-weight episodic memory with learned utilities, read by a "
                  "frozen backbone on later tasks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["reframe_as_solvable_object", None]],
                "Primary agreed. Sub null per run convention: C03 needs a trained canonical-schema parser or a "
                "category-level holdout, and neither is present (ALFWorld transfer is seen types). son55's supporting "
                "reframe (retrieval as a one-step value decision) is a distinct executed operation, so it is kept.",
                ["son55:E004", "son55:E005", "son55:E012"], NOSCORE),
            XC(p, "local:2601.03192-2", "son55", "unknown",
               "A4 ID collision. sol's local-2 is the statistics check, identical to son55's local-1 (both unmet), and "
               "is merged there. son55's local-2 is a different question, verified unknown: Table 2 reports 'best "
               "validation results' with no definition of the selection over epochs or splits.",
               ["son55:E011", "sol:E004", "sol:E008"]),
            XC(p, "local:2601.03192-3", "son55", "partial",
               "Verified: tokens and wall-clock against MemP are reported for HLE only; per-benchmark totals are "
               "missing.", ["son55:E023"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "Verified: No-Memory, RAG, λ=0 and single-task controls toggle the conditioning signal on the same "
               "backbone.", ["son55:E017", "son55:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: the HLE bank is built on the full question set and reused for cross-model transfer on HLE "
               "(opus:O02).", ["son55:E013", "son55:E016", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: RAG/Self-RAG/Mem0/MemP/Pass@10 are compared; there is no long-context or success-filtered "
               "nearest-neighbour baseline.", ["son55:E009", "son55:E027"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "met",
               "Verified: one recipe across four domains; δ and k are set per benchmark by a stated rule.",
               ["son55:E024", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: task-similarity correlation and k1/k2 sensitivity are reported; reward-noise robustness is "
               "only discussed.", ["son55:E021", "son55:E026"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "partial",
               "Verified: the Q-bin vs success correlation (r=0.861) is computed on the outcomes that trained Q; there "
               "is no intervention.", ["son55:E019"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Verified: unconditional write of every summarised trajectory; no retirement or size bound.",
               ["son55:E002", "son55:E003", "son55:E022"]),
            XC(p, "rsi:evidence_gated_retention/S4", "sol", "met",
               "Verified: the value signal is separable (λ=0) and ablated.", ["sol:E006", "opus:O03"]),
            XC(p, "rsi:evidence_gated_retention/S5", "revised", "met",
               "The gate's own cost (millisecond rerank and scalar update) is stated, with HLE token and time parity. "
               "Missing full-benchmark totals are charged to E.cost / local-3, not to S5.", ["sol:E011", "son55:E023"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "sol", "partial",
               "Failure present for the runtime table, HLE and the HLE cross-model claim (opus:O02); avoided for the "
               "frozen-bank held-out transfer on four domains. Partial.", ["sol:E003", "sol:E010", "opus:O02"]),
            XC(p, "rsi:index_experience_for_reuse/F3 (met = failure avoided)", "sol", "partial",
               "Same check as rsi:index_experience_for_reuse/F3 (ID normalised). son55's 'unmet' rested on Table 1 and "
               "HLE only; the transfer setting avoids the failure for OS/DB/BCB/ALFWorld.",
               ["son55:E007", "son55:E010", "opus:O02"]),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.causality. Same-backbone baselines, attempt-matched Pass@10 and a λ=0 ablation of the "
                "value signal isolate the system-level claim. sol's basis (per-entry credit cannot be attributed) is a "
                "mechanism limit scored in M and S1. Figure-only ablations keep it below 4.",
                ["son55:E017", "son55:E018", "opus:O03"], "+3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2601.03192-1]",
             "sol_value": "local-1 = GEM monotonic-improvement argument (M), unmet",
             "son55_value": "local-1 = no repeats/intervals (E.statistics), unmet",
             "correction": "Hidden A4 collision (equal status, so not flagged by conflicts.json). Final local-1 = the "
                           "statistics check (= sol's local-2, merged); sol's local-1 is renumbered local-4.",
             "evidence_ids": ["sol:E012", "sol:E013", "son55:E014"], "score_impact": NOEXP},
            {"field_path": "ratings.E.holdout.reason",
             "sol_value": "2 (HLE oracle repetition noted generally)",
             "son55_value": "2 (HLE memorisation and cross-model re-test noted)",
             "correction": "Rating kept at 2. Neither seat's rating reason named the HLE repeat-attempt prompt that can "
                           "carry the previous attempt's CORRECT/INCORRECT label (opus:O01). It is added as a holdout "
                           "caveat and an unresolved item.",
             "evidence_ids": ["opus:O01", "son55:E028"], "score_impact": "none (rating unchanged)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: Q-valued episodic "
                                                   "memory with two-phase retrieval; Table 1 is a 10-epoch replay with "
                                                   "labelled rewards; Table 2 is a frozen-bank held-out transfer on 4 of "
                                                   "5 domains; HLE has no split; cross-model HLE re-test; λ ablation is "
                                                   "figure-only; single runs. Initial bands G3 M3 X3 Em3 Ec2–3 Eh2 Es1 "
                                                   "Ecost2; evidence_level retained.",
            "integrity_checks": "Both seats a1 on 2601.03192v2, material sha c5486533…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid; son55 suffixed F3 ID normalised.",
            "core_claim_check": "Re-read §4–5, App. B.3, C.1, E.3, F, I.2; confirmed the HLE split (opus:O02), the "
                                "repeat-attempt note (opus:O01) and the λ=0 text (opus:O03).",
            "rating_agreement": "7/8 identical and re-checked; E.causality → son55.",
            "expectation_renumbering": "sol local-2 → local-1 (merged with son55 local-1); sol local-1 → local-4; son55 "
                                       "F3 suffix normalised.",
            "retained_vs_retained_gain": "The frozen bank improves held-out instances in four domains → retained "
                                         "(author-reported, single split/seed). The HLE and cross-model gains are "
                                         "re-exposure, not retained transfer.",
        },
        "figure_dependence": "λ sweep (Fig. 5), RL-vs-non-RL curves (Fig. 4), Q-bin analysis (Fig. 7) and forgetting "
                             "(Figs. 8–9) are available only as text descriptions; E.causality=3 relies on Table 1–3 "
                             "numbers plus those descriptions and would not rise without the figure data.",
    }

    # =========================================================== 2601.04620 AgentDevel (Δ5)
    p = "2601.04620"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Rej. 2 3 0.004", "Table 2, iteration 11",
                    "Iteration 11 is rejected with 3 P2F at ρ=0.004, the same regression count and rate as accepted "
                    "iteration 6 ('Acc. 12 3 0.004'). This contradicts the text's reason for rejection ('markedly "
                    "higher pass→fail regressions'); the actual gate rule is not recoverable."),
            opus_ev(p, "O02", "with the same data split and budget.", "Table 3 notes",
                    "'Same budget' is asserted without any number; it is the only budget statement in the paper."),
            opus_ev(p, "O03", "require additional compute and wall-clock time", "App. A Limitations",
                    "The only cost information is qualitative."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus confirms sol. The executed load-bearing operation is converting diagnosis into an executable "
                      "artifact (LLM-written scripts run by an interpreter over trace records) and closing the release "
                      "loop with programmatic scorers and per-example flips that decide promotion. This is C25 (a "
                      "machine-checkable intermediate artifact routed to a sound executor, with verifiable output used "
                      "for candidate selection), as in r08b AccelOpt and r01a OS-Copilot. son55's "
                      "assumption_audit_and_pivot is not retained: that card relaxes or violates the assumption a "
                      "result or guarantee rests on and re-derives the guarantee. Here 'improvement lives inside the "
                      "agent' is a framing contrast, and no guarantee is re-derived (the 'non-regression' property is "
                      "empirical and in-sample). Its two RE checks are kept as local-6/7.",
            "matches": [smatch("sol", p, "decompose_and_delegate")],
            "executes_pattern": True, "resolves_problem": "no (non-regression shown only on the TrainSet that generates edits)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("son55", p, "evidence_gated_retention", "H31")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.04620-1"): "local:2601.04620-5",
                    ("son55", "rs:assumption_audit_and_pivot/RE-6"): "local:2601.04620-6",
                    ("son55", "rs:assumption_audit_and_pivot/RE-4"): "local:2601.04620-7",
                    ("son55", "rsi:attribute_and_patch_incumbent/F4 (met = failure avoided)"):
                        "rsi:attribute_and_patch_incumbent/F4"},
            overrides={
                "local:2601.04620-5": {
                    "status": "unmet",
                    "note": "sol's local-1 renumbered (A4 collision with son55's local-1 = held-out non-regression).",
                    "reason": "Opus (status revised from 'challenged_with_evidence', which is for a paper rebutting an "
                              "expectation with evidence; here the paper's own claim is undercut by its data). The full "
                              "pipeline still has 18 P2F, the bad-release threshold is unreported, and the ungated "
                              "variant tests higher (35.0 vs 34.2). Zero bad releases does not establish non-regression. "
                              "Unmet."},
                "local:2601.04620-2": {"note": "sol's and son55's local-2 are overlapping reporting/statistics checks "
                                               "(both unmet); merged."},
                "local:2601.04620-6": dict(conv("rs:assumption_audit_and_pivot/RE-6")),
                "local:2601.04620-7": dict(conv("rs:assumption_audit_and_pivot/RE-4")),
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O01"]),
        "assessment": assess("son55", p),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The aggregate-score-masks-regressions concern is real and "
                   "neighbours (Reflexion, Self-Refine, PromptBreeder, DGM, Live-SWE) are named. But no neighbour's "
                   "regressions are measured, validation-gated acceptance in existing optimizers is not discussed, "
                   "and the remaining gap is argued, not bounded.",
                   ["son55:E001", "son55:E020", "sol:E010"], ["son55:E019"]),
            "M": R("resolved", 2, "Opus sides with son55. The chain (blind symptom critic → executable diagnosis → one "
                   "RC → flip gate → fallback) is reasoned and matches the stated risk. But the central premise, that "
                   "gating on flips over the same TrainSet that generated the edit controls deployment regressions, is "
                   "untested, and the paper's own ablation runs against it (the ungated variant tests higher). The RC "
                   "synthesis Φ is a black box, and the gate G is left abstract ('does not prescribe a universal set of "
                   "thresholds'). sol's 3 credited reconstructibility, which is scored under X (X=2 here, given the "
                   "missing thresholds).",
                   ["son55:E002", "son55:E003", "son55:E004", "sol:E007"], ["son55:E005", "son55:E006", "son55:E014"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. The version line, discard-on-reject and saved artifacts are "
                   "described. The gate rule, thresholds, stopping values, hit-rate/FTP/P2P definitions, b0 and splits "
                   "are missing, and the iteration-11 rejection contradicts the stated rationale (opus:O01).",
                   ["son55:E005", "son55:E006", "son55:E007", "sol:E007"], ["son55:E017", "son55:E018", "opus:O01"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. The primary metrics use task-native verifiers "
                               "(SWE-bench tests, WebArena checkers), which are credible in themselves. But the "
                               "reported numbers are internally inconsistent: Table 1 WebArena 35.5 vs Table 3 'full' "
                               "34.2 for the same pipeline from the same b0, and Table 3's flip protocol is worded two "
                               "ways. The bad-release threshold and hit-rate are undefined, and StableToolBench SoWR and "
                               "the critic-fallback pass labels rely on LLM judgement with no audit. Same "
                               "reporting-integrity cap as r09b EvoRoute.",
                               ["son55:E009", "son55:E011", "sol:E012"],
                               ["son55:E012", "son55:E013", "sol:E014", "sol:E015", "sol:E018"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. The three WebArena ablations are single runs with "
                             "1–2 point test differences on unreported n. Removing the gate gives the highest test "
                             "score, so the gate's benefit is shown only as in-sample flip counts. A strong improver "
                             "(Claude Code) on an undescribed b0 is an unexamined alternative explanation for the "
                             "headline doublings, and there is no 'just iterate on train' or rival-improver control. "
                             "Baselines are quoted, not rerun. The central comparative claim against in-agent and "
                             "population methods is untested. Single-run noise itself is charged to E.statistics (A2).",
                             ["son55:E014", "son55:E025", "sol:E013"],
                             ["son55:E010", "son55:E019", "sol:E019", "opus:O02"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. The TestSet is declared untouched by gating or "
                           "stopping and used once. But split sizes and disjointness are unreported, the non-regression "
                           "claim is in-sample only, and the train–test gap is large (78.5 vs 34.2).",
                           ["son55:E008", "son55:E022"], ["son55:E005", "son55:E015", "son55:E016"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Candidate-level flip and rejection "
                              "counts are shown for one benchmark; no sizes, seeds, repeated evolutions or intervals.",
                              ["son55:E017", "sol:E017"], ["son55:E012", "son55:E013"]),
            "E.cost": R("not_reported", 0, "Opus sides with sol. After a full search, no quantity of tokens, dollars, "
                        "wall-clock, calls or failed-RC cost appears anywhere. There is only a qualitative limitation "
                        "(opus:O03) and an unquantified 'same budget' assertion (opus:O02). Iteration and reject counts "
                        "(StableToolBench, Table 3) are process counts, not cost. A1/A2: the necessary evidence is absent "
                        "→ not_reported, rating 0.",
                        ["opus:O02", "opus:O03"], [],
                        ["Abstract, §§1–4, Tables 1–3, Appendices A–C: searched for tokens, dollars, calls, wall-clock, "
                         "compute, budget and failed-RC cost; found only the qualitative overhead statement and the "
                         "'same budget' note."]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–C read. In scope (system_method, A class): a retained, "
                  "non-weight agent blueprint (prompt/code/tool wrappers) edited from execution feedback and kept or "
                  "discarded by a gate. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "decompose_and_delegate",
                "See rs_pattern.reason: executable diagnosis plus programmatic verification closing the selection loop "
                "is C25. The 'assumption' son55 named is a framing contrast with no guarantee relaxed and re-derived.",
                ["sol:E002", "son55:E003", "son55:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["decompose_and_delegate", "C25"]],
                "Follows primary; C25 tactic steps checked by sol (step 4: ablation of executable diagnosis exists; "
                "step 5: cost unmet).", ["sol:E002", "sol:E013"], NOSCORE),
            XC(p, "local:2601.04620-1", "son55", "unmet",
               "A4 ID collision. sol's local-1 (zero bad releases ≠ non-regression, E.measurement) and son55's local-1 "
               "(no held-out P→F, E.holdout) are different questions. Final local-1 = son55's, verified: flips are "
               "counted on D_train only. sol's question is kept as local-5, status corrected to unmet (see "
               "expectations).", ["son55:E005", "son55:E015", "son55:E016", "sol:E012", "sol:E015"]),
            XC(p, "local:2601.04620-3", "son55", "unmet",
               "Verified: 35.50 vs 34.2, and iteration 11 contradicts the text (opus:O01).",
               ["son55:E012", "son55:E013", "opus:O01"]),
            XC(p, "local:2601.04620-4", "son55", "unmet",
               "Verified: no numeric cost or budget anywhere (opus:O02, opus:O03).", ["son55:E021", "opus:O02"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-4", "revised", {"moved_to": "local:2601.04620-7", "status": "partial"},
               "The card is not retained. The check (prior work with a similar move is not differentiated; "
               "validation-gated acceptance is not discussed) is kept as local-7, partial.", ["son55:E020"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-6", "revised", {"moved_to": "local:2601.04620-6", "status": "unmet"},
               "The card is not retained. The check (no in-agent or population baseline run to show their regressions) "
               "is kept as local-6, unmet.", ["son55:E010", "son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "sol", "unmet",
               "Verified: no tokens, calls or wall-clock.", ["sol:E016", "opus:O03"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "sol", "partial",
               "Verified: gate, script and critic ablations exist on WebArena only; the gate-off variant tests higher.",
               ["sol:E012", "sol:E013", "sol:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "sol", "unmet",
               "Verified: only generic pseudo-code; experiment prompts, scripts, diffs and thresholds are not given.",
               ["sol:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4 (met = failure avoided)", "son55", "partial",
               "ID normalised to .../F4 (A4). Verified: programmatic scorers are primary, but where they are absent the "
               "pass label comes from a critic of the same model family as the proposer.", ["son55:E009", "son55:E002"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "Verified: cross-example symptom aggregation, RC and fallback exist; there are no patch instances, and "
               "promotion is not independent.", ["sol:E002", "sol:E004", "sol:E005", "sol:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "unmet",
               "Verified: one bundled change over prompt/code/wrappers, not localised to the failing component.",
               ["son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Verified: the per-example flip gate with discard protects earlier wins, but only on the optimisation "
               "set and with unspecified thresholds.", ["son55:E005", "son55:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: scripts aggregate symptom classes and triggers across examples before synthesis.",
               ["son55:E003"]),
            XC(p, "rsi:evidence_gated_retention/H31", "sol", "unmet",
               "Verified: candidate generation and the gate share the TrainSet; there is no sound commit rule or error "
               "control.", ["sol:E005", "sol:E008"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "met",
               "Verified: the gate is a separable component and is ablated (w/o flip gate).",
               ["son55:E014", "son55:E015"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M. The premise that train-set flip gating controls deployment regressions is untested and "
                "contradicted by the gate ablation's test result; Φ and G are unspecified. Reconstructibility (sol's "
                "basis) is X.", ["son55:E005", "son55:E006", "son55:E014"], "-5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement. The verifiers are fine, but the internal inconsistencies (35.5 vs 34.2, "
                "the flip-protocol wording, undefined thresholds and hit-rate) and the unaudited LLM-judged "
                "labels/SoWR cap the credibility of the reported measurement. son55 noted the inconsistencies but did "
                "not apply them.", ["son55:E012", "son55:E013", "sol:E014", "sol:E015"], "-2.5 vs son55 (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.causality. The ablations are relevant but cannot support the central claim: the gate "
                "lowers the test score, there is no rival improver and no naive-iteration control, baselines are "
                "quoted, and the comparative thesis is untested.",
                ["son55:E014", "son55:E019", "sol:E019"], "-3.75 vs sol (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "not_reported", "rating": 0},
                "See ratings.E.cost. No cost quantity exists after a full search; the iteration and reject counts that "
                "son55 credited are process counts. not_reported with search_scope.",
                ["opus:O02", "opus:O03", "son55:E021"], "-1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: single-line RC loop "
                                                   "with blind critic, script diagnosis, abstract flip gate on the "
                                                   "TrainSet; Table 1 b0→final doublings without sizes; Table 3 "
                                                   "WebArena ablations (gate-off tests higher); 35.5 vs 34.2; no cost "
                                                   "numbers. Initial bands G2 M2 X2 Em2 Ec1 Eh2 Es1 Ecost0; "
                                                   "evidence_level retained, claim scoped.",
            "integrity_checks": "Both seats a1 on 2601.04620v1, material sha 10c93431…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid; son55 suffixed F4 ID normalised.",
            "core_claim_check": "Re-read §2.4, §3.2–3.4, Tables 1–3, App. A; confirmed the iteration-11 row against "
                                "iteration 6 (opus:O01) and the absence of any cost figure.",
            "rating_agreement": "4/8 identical and re-checked; M, E.causality → son55; E.measurement, E.cost → sol. "
                                "The final (42.5) is below both seats by per-item ruling.",
            "expectation_renumbering": "sol local-1 → local-5 (A4 collision; status corrected to unmet); son55 "
                                       "assumption_audit RE-6/RE-4 → local-6/7; local-2 merged (overlapping checks); "
                                       "F4 suffix normalised.",
            "retained_vs_retained_gain": "The promoted blueprint is evaluated once on a declared held-out TestSet → "
                                         "retained (author-reported, sizes unknown). Non-regression is shown only "
                                         "in-sample.",
        },
        "figure_dependence": None,
    }

    return S
