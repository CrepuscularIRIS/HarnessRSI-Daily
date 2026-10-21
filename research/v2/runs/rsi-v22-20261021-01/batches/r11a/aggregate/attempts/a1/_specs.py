"""Opus rulings for r11a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2601.07055 Dr. Zero: out_of_scope confirmed independently. The proposer is trained with HRPO and the solver with "
        "GRPO, so every retained change is a weight change; the generated QA pairs are only training data. claim_type is "
        "set to component_training and the RS record to self_supervised_signal_engineering/C08 (run convention for "
        "proposer–solver co-training: r05b R-Zero, r07b Search Self-play/SPICE, r09b GenEnv). evidence_level and "
        "claim_support are set to null, which is the out_of_scope canonical value (both seats wrote task/scoped).",
        "2601.22628 TTCS: out_of_scope confirmed independently. The synthesizer and the solver are both GRPO-updated, and "
        "the solver adapts its weights on the very test questions that are then scored (transductive TTT). Identification "
        "follows son55 (C08/H22, informational). Same null evidence_level/claim_support correction as above.",
        "2601.07477 JudgeFlow (seat Δ8.75): M → son55 2 and E.causality → son55 1. Final 51.25. M: the Judge is forced to "
        "give a full ranking for every failure, it sees the gold answer, and workflows have at most 3 blocks. With so few "
        "blocks the localisation advantage over a random-block edit is small, and the paper states no prediction that "
        "would separate the two. E.causality: the only isolating comparison, against AFlow, changes three things at once "
        "(block abstraction, Judge signal, MCTS replaced by a top-K softmax pool). The Table 1 baselines are quoted "
        "'to keep consistent with prior literature'. There is no Judge-off, random-block or Judge-accuracy control. RS: "
        "outside_taxonomy (son55); the blocks are not split by a measured property, so heterogeneous_decomposition does "
        "not apply. Domain: H12 + H17.",
        "2601.07641 Test-Time Tool Evolution: final 37.5, below both seats (42.5 / 43.75), reached item by item. "
        "E.measurement → sol 1. The appendix case traces contradict the stated 1e-5 tolerance: Case 1 shows "
        "13.738 L/mol for RT/P with P=20 kPa and T=330 K, which is 137.2 L/mol, and 1.23×13.738 is reported as 169.0. "
        "Case 2 records 31.6 g against a 33.98 g ground truth as 'correct'. The answer prompt also asks the model to "
        "'simulate' tool execution. E.causality → sol 1 (the central TTE-Zero retention claim has no library-off or "
        "per-problem-synthesis control). M → son55 2. E.cost stays not_reported 0 in both seats. Domain: H07 + H30.",
        "2601.11100 ReCreate (seat Δ8.75): G, E.measurement and E.holdout all → sol 2. Final 55.0. G: trajectory-reading "
        "neighbours (ExpeL, AWM, Live-SWE-agent, SCOPE) blur the 'metric-only' gap. E.measurement: the Table 2 ReCreate "
        "row does not match Table 1 (SWE 60.19 is Django only; DS 77.74 cannot be derived from 77.00/68.63/85.19), and "
        "the run convention for table inconsistency (r09b) caps this at 2. E.holdout: the retained Django memory tells "
        "the agent to run 'FAIL_TO_PASS tests mentioned in expected_tests.txt', which are the hidden evaluation tests. "
        "Whether test-time sandboxes expose that file is not reported. RS → sol generative_process_redesign (sub null; "
        "the SICA/Live-SWE convention); the adapt_via_conditioning supporting entry is dropped. Domain: H12 + H02.",
        "A4 hygiene: hidden ID collisions (same local:<key>-n used for different questions) in 2601.07477, 2601.07641 and "
        "2601.11100 were renumbered. Expectations from an RS card that was not kept (JudgeFlow "
        "heterogeneous_decomposition RE-4/RE-5) were moved to local IDs instead of being dropped.",
        "Figure dependence: ReCreate Figures 5/6/8/10/11 and JudgeFlow Figure 6 carry their values only as images. Ratings "
        "rely on captions, body text and tables. No figure value was invented.",
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
        return prefix(a, s)

    def conv(old):
        return {"converted_from": old,
                "source_note": f"Moved from {old}: that card was not kept in the final pattern record (see "
                               "resolutions). The check is still a valid question about this paper's claim, so it is "
                               "kept as a paper-local expectation (A4)."}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                       "precedent r05b–r09b).",
                "claim_support": None,
                "claim_support_note": note,
                "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_corrections(p, ev):
        sol_a, son_a = seat("sol", p)["assessment"], seat("son55", p)["assessment"]
        return [
            {"field_path": "assessment.evidence_level", "sol_value": sol_a.get("evidence_level"),
             "son55_value": son_a.get("evidence_level"), "final_value": None,
             "reason": "Both seats wrote 'task'. For out_of_scope rows the canonical value is null: the "
                       "task/retained/improver ladder in EVIDENCE.md grades retained non-weight changes, and this paper "
                       "has none (precedent r05b–r09b).", "evidence_ids": ev,
             "score_impact": "none (evidence_level is not scored; row is unscored)"},
            {"field_path": "assessment.claim_support", "sol_value": sol_a.get("claim_support"),
             "son55_value": son_a.get("claim_support"), "final_value": None,
             "reason": "Both seats wrote 'scoped'. Claim support is not assessed under this rubric for an excluded row; "
                       "null is canonical (precedent r09b GenEnv).", "evidence_ids": ev,
             "score_impact": "none"},
        ]

    # =========================================================== 2601.07055 Dr. Zero (both out_of_scope)
    p = "2601.07055"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "proposer is optimised with HRPO on solver feedback (opus:O01) and the solver with GRPO on the generated data "
          "(opus:O02); both start from the same base LLM (opus:O03). The prompts and the search tool are fixed; the only "
          "persisted change is model weights, and the generated QA pairs are training inputs, not a harness component "
          "read back at inference. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p, "claim_type": "component_training"},
        "opus_evidence": [
            opus_ev(p, "O01", "Utilizing solver feedback, the proposer is optimized via HRPO to produce verifiable, diverse and challenging queries.",
                    "§3 (overview of the self-evolution loop)", "The proposer improves by a weight update (HRPO)."),
            opus_ev(p, "O02", "Meanwhile, the solver leverages the generated data through GRPO to refine its search and reasoning capabilities.",
                    "§3 (overview of the self-evolution loop)", "The evaluated solver improves by a weight update (GRPO)."),
            opus_ev(p, "O03", "Both models are initialized from the same base LLM and evolve without human-written training questions or annotated answers",
                    "§3 (overview of the self-evolution loop)", "Both roles are policies whose evolution is parameter training."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). The proposer generates multi-hop questions, the solver's pass rate on "
                      "them is turned into a difficulty-guided reward, and both policies are retrained each iteration. "
                      "This is C08's generate → steer → filter → retrain loop in its closed-loop variant. C08 is the run "
                      "convention for proposer–solver co-training (r05b R-Zero, r07b Search Self-play and SPICE, r09b "
                      "GenEnv); Search Self-play is the closest precedent (a search agent in self-play). sol's C26 is "
                      "rejected: C26 is the preference-pair branch, and HRPO is a scalar group-baseline RL objective. "
                      "son55's null sub is replaced to keep the convention.",
            "matches": [{
                "main_id": "self_supervised_signal_engineering", "sub_id": "C08", "role": "primary",
                "fit": "medium (informational, out_of_scope)",
                "tactic_steps_checked": "generator = proposer with search tool; steering = solver pass-rate reward with "
                                        "hop-grouped baseline; filter = format reward and grounded-answer requirement; "
                                        "retrain = HRPO (proposer) + GRPO (solver), 3 iterations.",
                "success_checks": "not assessed (out_of_scope)", "failure_checks": "not assessed (out_of_scope)",
                "evidence_ids": ["opus:O01", "opus:O02", "son55:E001"],
                "reason": "Informational identification only; no score effect."}],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": "C08",
            "domain": {"namespace": "rsi", "main": "self_generate_the_curriculum", "sub": "H22"},
            "operation_correspondence": "A proposer steered by the solver's pass rate generates tasks, and both proposer "
                                        "and solver are retrained; H22 is the domain's proposer–solver co-training card.",
            "necessary_conditions/differences": "Informational only: both roles are weight-trained, so the H22 match "
                                                "does not bring the paper into harness scope.",
            "evidence_ids": ["opus:O01", "opus:O02"]}],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; benchmark gains are author-reported results of "
                                     "trained 3B/7B checkpoints."),
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "son55", "component_training",
                "Informational. The evaluated product is a trained search-agent checkpoint; this is the run convention for "
                "out-of-scope proposer–solver papers (r05b–r09b). sol's system_method would describe the whole loop as "
                "the contribution even though the loop's output is weights.", ["opus:O02", "opus:O03"],
                "none (out_of_scope row; claim_type is identification only)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", "C08"]],
                "Same main card in both seats. The sub-card is set to C08 (run convention, Search Self-play precedent). "
                "C26's preference-pair tactic is not executed (HRPO is a scalar RL objective), and null would break "
                "consistency with r05b–r09b.", ["opus:O01", "opus:O02"], NOSCORE),
        ],
        "shared_error_corrections": oos_corrections(p, ["opus:O01", "opus:O02"]),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §1 and §3 (loop overview, HRPO) and Appendix A "
                                                   "(training schedule) before opening the seats: HRPO proposer and GRPO "
                                                   "solver weights → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2601.07055v2, material sha 76ff914f…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2601.22628 TTCS (both out_of_scope)
    p = "2601.22628"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "synthesizer and the solver are both optimised online with GRPO (opus:O02). The solver updates its parameters "
          "with self-consistency rewards on the original test questions and on synthetic variants of them (opus:O01, "
          "opus:O03), so the scored test items are also the adaptation data. No prompt, tool, workflow, memory or "
          "evaluator is edited and retained. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p, "claim_type": "component_training"},
        "opus_evidence": [
            opus_ev(p, "O01", "the solver updates itself using self-consistency rewards computed from multiple sampled responses on both original test and synthetic questions",
                    "Abstract", "Weight adaptation uses the test questions themselves (transductive)."),
            opus_ev(p, "O02", "Both agents are optimized online via Group Relative Policy Optimization (GRPO)",
                    "§1 Introduction", "Both persisted objects are policies updated by RL."),
            opus_ev(p, "O03", "TTT enables the model to dynamically adapt its parameters only using test questions.",
                    "§3 Preliminaries (Test-Time Training)", "The adaptation target is the parameters."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55") | {
            "reason": "Informational (out_of_scope). Opus confirms son55: the synthesizer generates question variants, "
                      "self-consistency filters them, both policies retrain iteratively, and the solver's capability "
                      "steers the synthesizer. This is the C08 closed-loop variant, the run convention for "
                      "generator–solver co-training (r09b GenEnv, r05b R-Zero). sol's null primary with "
                      "outside_taxonomy=false is not a valid shape and is replaced."},
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; gains are author-reported results of "
                                     "test-time-trained checkpoints in a transductive setting."),
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "son55", "component_training",
                "Informational. The evaluated product is a test-time-trained checkpoint; run convention for "
                "out-of-scope weight-level papers.", ["opus:O02", "opus:O03"],
                "none (out_of_scope row; claim_type is identification only)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "Identification is still recorded for excluded rows (run convention). Exclusion settles scope, not "
                "whether a card describes the operation; the generator → filter → retrain loop is C08.",
                ["opus:O01", "opus:O02", "son55:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["self_supervised_signal_engineering", "C08"]],
                "Follows primary.", ["son55:E001", "son55:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55", [["self_generate_the_curriculum", "H22"]],
                "Informational H22 (proposer co-trained against a solver, with a capability-band signal). As with r09b "
                "GenEnv, an H22 match on a weight-level member does not bring the paper into scope.",
                ["opus:O02", "son55:E001"], NOSCORE),
            XC(p, "rsi:self_generate_the_curriculum/S1", "son55", "unmet",
               "Informational. Similarity penalties prevent copying, but nothing independently checks that a variant is "
               "valid or that its majority-vote pseudo-label is right.", ["son55:E001", "son55:E003"]),
            XC(p, "rsi:self_generate_the_curriculum/S2", "son55", "partial",
               "Informational. The capability signal is measured on the solver's own samples of the test-derived "
               "variants, not on a fixed held-out validation environment.", ["son55:E001", "opus:O01"]),
        ],
        "shared_error_corrections": oos_corrections(p, ["opus:O01", "opus:O02"]),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §1, §3 (TTT definition) and §4 (synthesizer and "
                                                   "solver updates) first: GRPO on both policies, using the test "
                                                   "questions themselves → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2601.22628v1, material sha b6d8a72d…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03; the transductive use of test items is noted.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2601.07477 JudgeFlow (Δ8.75)
    p = "2601.07477"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Return a JSON object mapping each block name to a unique integer rank (1 = most responsible, n = least responsible).",
                    "Appendix C, Judge prompt (Output Contract)",
                    "The Judge must output a full ranking for every failure, even when only one block is at fault or "
                    "none is clearly at fault."),
            opus_ev(p, "O02", "CRITICAL: Maximum 3 blocks per workflow", "Appendix D, optimization prompt",
                    "At most three candidate blocks, so random block choice already hits the culprit ≥1/3 of the time."),
            opus_ev(p, "O03", "to keep consistent with prior literature", "§4.1 Implementation Details",
                    "The setup mirrors MermaidFlow (Zheng et al.); the Table 1 baselines read as quoted, not rerun under "
                    "a matched budget."),
            opus_ev(p, "O04", "Following Zhang et al. (2025b) , the refined workflow", "§3.2.2 Optimization-Update",
                    "Retention is AFlow-style score-ranked top-K pool with softmax parent sampling. The search procedure "
                    "also differs from AFlow's MCTS, so the AFlow comparison changes more than the Judge."),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "Opus confirms son55. heterogeneous_decomposition requires a partition by a measured "
                      "discriminating property, with a differentiated treatment per partition and a load-bearing "
                      "uniform-treatment ablation. JudgeFlow's blocks are author-defined control-flow units (seq/for/cond), "
                      "not partitions by a measured property. Its 'treatment' is to edit the single worst-ranked block and "
                      "leave the others alone, which is a localise-and-patch move rather than a tailored per-component "
                      "operation (sol itself found C04 inapplicable). decompose_and_delegate does not apply (no external "
                      "solver). generative_process_redesign would need a conventionally fixed component, but the workflow "
                      "was already free in AFlow; the contribution here is the attribution signal. The operation is "
                      "carried by the domain cards H12/H17. The paper is fully evaluated regardless.",
            "executes_pattern": None, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("son55", p, "search_agent_architecture", "H17")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.07477-1"): "local:2601.07477-2",
                    ("sol", "rs:heterogeneous_decomposition/RE-5"): "local:2601.07477-1",
                    ("sol", "rs:heterogeneous_decomposition/RE-4"): "local:2601.07477-3"},
            overrides={
                "local:2601.07477-1": {
                    "status": "unmet",
                    "reason": "Opus: same check in both seats under different IDs (sol RE-5, son55 local-1). There is no "
                              "Judge-accuracy check (no annotated responsibility, no counterfactual replay) and no "
                              "Judge-off or random-block control on the same blocks; the authors list a 'more robust "
                              "Judge' as future work.",
                    **conv("rs:heterogeneous_decomposition/RE-5")},
                "local:2601.07477-2": {
                    "status": "unmet",
                    "reason": "Opus: same check in both seats (sol local-1, son55 local-2). Only run counts (3 runs for "
                              "Table 1, 5 for AIME) are given; there is no spread, interval or test, and the margins are "
                              "small (1.4 avg points; 2.7 on AIME). The requirement is uncertainty, and none is reported, "
                              "so unmet.",
                    "note": "sol's local-1 renumbered (A4 collision with son55's local-1 = Judge validation)."},
                "local:2601.07477-3": dict(conv("rs:heterogeneous_decomposition/RE-4")),
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O04"]),
        "assessment": assess("son55", p),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Coarse end-to-end signal in code-workflow search is a real "
                   "limitation, and the neighbours (AFlow, MaAS, MermaidFlow, ADAS, failure attribution) are named. Not 3: "
                   "TextGrad-style component-level feedback, the closest prior answer to 'where to refine', is cited "
                   "only as prompt optimisation, and the residual cost of coarse signals is argued, not measured.",
                   ["son55:E002", "sol:E002", "sol:E010"]),
            "M": R("resolved", 2, "Opus sides with son55. The trace → ranked blame → one-block edit → top-K chain is "
                   "coherent, but its load-bearing premise is thin in ways that belong to the method, not to the "
                   "evidence. (i) The Judge must emit a full ranking for every failure (opus:O01), even when no block "
                   "is clearly at fault. (ii) It sees the gold answer (son55:E005). (iii) Workflows have at most 3 blocks "
                   "(opus:O02), so selecting by rank-sum gains little over a random-block or whole-workflow edit, and no "
                   "prediction that would separate them is stated. sol's 3 credits reconstructibility, which is X's "
                   "question.", ["son55:E003", "son55:E005", "opus:O01", "opus:O02"], ["sol:E004"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithm 1, the action set, the top-K pool and softmax "
                   "parent sampling, both prompts, 20 rounds and K=3 are given. Not 4: τ, the rule that picks the "
                   "reported workflow, and any regression guard or rollback are unstated.",
                   ["son55:E003", "son55:E004", "son55:E009", "sol:E005"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Standard solve-rate and pass@1 metrics are "
                               "used, and the Table 1 arithmetic is internally consistent (each margin and average "
                               "recomputes). Not 4: test-set sizes and contamination of public sets for gpt-4o-mini "
                               "are not discussed.", ["son55:E010", "sol:E008", "sol:E006"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. The central claim is that block-level Judge signals "
                             "drive better optimisation. The only isolating comparison, the MBPP curves against AFlow, "
                             "changes the representation (blocks), the signal (Judge) and the search (MCTS replaced by a "
                             "top-K softmax pool, opus:O04) all at once. The Table 1 baselines follow prior literature "
                             "(opus:O03) with no matched budget, and the LLM-swap table varies Judge and optimizer "
                             "together. There is no Judge-off, random-block or Judge-accuracy control.",
                             ["son55:E012", "son55:E013", "opus:O03", "opus:O04"], ["sol:E013"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. There is a train/test split 'following previous "
                           "studies' plus two zero-shot cross-benchmark pairs. Split sizes, the rule that selects the "
                           "reported workflow, and per-iteration test monitoring (the MBPP test curve is plotted per "
                           "iteration) are unspecified. Shared omission added: whether the MBPP 'test' operator runs "
                           "public example tests or the evaluation tests is also unreported.",
                           ["son55:E007", "son55:E014", "sol:E006", "sol:E011"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): run counts given, no spread or test, small "
                              "margins.", ["son55:E008", "sol:E007", "sol:E009"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only one round's GSM8K evaluation vs Judge dollars "
                        "($0.45 vs $0.01) is given. There is no total optimisation cost and no call counts against "
                        "AFlow/MaAS/MermaidFlow, despite the sample-efficiency claim.", ["son55:E015", "sol:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–D read. In scope (system_method): a non-weight agentic "
                  "workflow optimised from execution feedback and retained in a score-gated pool, then deployed on "
                  "held-out splits. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 6 (JudgeFlow vs AFlow curves) values are image-only; used as described in §4.3.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", None,
                "outside_taxonomy confirmed: the blocks are structural units, not a partition by a measured property, and "
                "the 'treatment' is edit-the-worst, not tailored per component (see rs_pattern.reason).",
                ["son55:E003", "opus:O01"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [],
                "Follows primary (outside_taxonomy: matches empty, reason non-empty).", ["son55:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["attribute_and_patch_incumbent", "H12"], ["search_agent_architecture", "H17"]],
                "H17 kept (both seats; offline workflow search, frozen design deployed). H12 added: the paper's "
                "load-bearing step is credit assignment from failure traces to one component, followed by a scoped edit "
                "of the incumbent. That is the parent card's signature (attribute_and_patch_incumbent); the workflow "
                "JSON is executable harness configuration, and rank aggregation across failures is the 'diagnose "
                "mechanisms, not instances' step. H09 was considered and rejected: JudgeFlow does not propagate a "
                "critique to every node.", ["son55:E001", "son55:E003", "son55:E004"], NOSCORE),
            XC(p, "local:2601.07477-1", "son55", "unmet",
               "A4 ID collision: sol's local-1 (statistics) and son55's local-1 (Judge validation) are different "
               "questions. Final local-1 = Judge validation, unmet (verified: no attribution-accuracy check and no "
               "Judge-off/random-block control). sol's question moves to local-2.", ["son55:E012", "son55:E016"]),
            XC(p, "local:2601.07477-2", "son55", "unmet",
               "Statistics check (son55 local-2 = sol local-1 'partial'). The requirement is uncertainty reporting; only "
               "run counts appear, so unmet. Rating E.statistics=1 unaffected.", ["son55:E008", "sol:E007"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "revised", {"moved_to": "local:2601.07477-3", "status": "partial"},
               "The card is not kept (outside_taxonomy). The question (does the comparison set isolate the "
               "contribution?) is still valid and is kept as local-3. Status partial verified: AFlow is a relevant "
               "baseline, but it changes blocks, signal and search together (opus:O04).", ["sol:E010", "opus:O04"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "same_supported_fact", {"moved_to": "local:2601.07477-1", "status": "unmet"},
               "The same check as son55's local-1 (is the responsibility ranking validated?). Both seats found it "
               "unmet; merged into local-1.", ["sol:E004", "son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F2", "son55", "partial",
               "Verified. The added blame signal is the contribution, while the pool and selection follow AFlow "
               "(opus:O04), and no matched control isolates the signal. The 'one more signal in the update rule' "
               "failure is therefore partly present.", ["son55:E004", "opus:O04"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "met",
               "Verified: edits are restricted to the selected block (Add next to it, Remove it, or Modify it).",
               ["son55:E006", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Verified: the score-ranked top-K pool protects the best averages, but there is no per-instance "
               "regression check or rollback, and prior workflows are only banned from repetition.", ["son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: rank vectors are summed over all failures before the block is chosen.", ["son55:E003"]),
            XC(p, "rsi:search_agent_architecture/H17-step4", "sol", "partial",
               "Verified: only one round's GSM8K Eval/Judge dollars are given; there is no total search cost and no "
               "budget-matched baselines.", ["sol:E012"]),
            XC(p, "rsi:search_agent_architecture/S3", "sol", "met",
               "Verified: what persists is decided by re-executed task scores (top-K), not by the Judge's own "
               "assessment.", ["sol:E005"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M. Forced full ranking with gold-answer access (opus:O01, son55:E005) and a 3-block cap "
                "(opus:O02) leave the localisation premise thin. No prediction separating it from a naive edit is "
                "stated.", ["opus:O01", "opus:O02", "son55:E005"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality. The only isolating comparison changes three factors (opus:O04), and the "
                "baselines are quoted (opus:O03). The central Judge claim has no control. sol's 2 credits Table 1 and "
                "the LLM-swap table, but neither isolates the Judge.", ["son55:E012", "opus:O03", "opus:O04"],
                "−3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.reason", "sol_value": "2 (reason omits test-operator provenance)",
             "son55_value": "2 (reason omits test-operator provenance)", "final_value": 2,
             "reason": "Shared omission, no rating change. MBPP/HumanEval workflows contain a 'test' operator that runs "
                       "generated code 'against test cases' (Appendix A). Neither seat noted that the paper does not "
                       "say whether these are the public example tests (AFlow convention) or the evaluation tests. "
                       "Recorded in the E.holdout reason; the rating stays 2 because the split and selection gaps "
                       "already bound it.", "evidence_ids": ["sol:E006"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–4 and Appendices A–D before opening the seats. Initial "
                                                   "view: in scope (non-weight workflow, score-gated pool, held-out "
                                                   "test). G≈2 (TextGrad-style neighbour under-addressed), M 2–3, X 3. "
                                                   "E is weak on causality (only a confounded AFlow comparison; "
                                                   "baselines quoted), statistics 1 (means only), cost 1 (one round).",
            "integrity_checks": "Both seats a1 on 2601.07477v2, material sha e528c8de…; canonical seat hashes equal "
                                "conflicts.json; both did 15+31 identification with valid namespaces.",
            "core_claim_check": "The strongest supported claim is the full system beating listed baselines on test "
                                "splits (3-run means). The Judge's own contribution is not isolated. 'Retained' is "
                                "warranted: frozen workflows are used on test splits and in transfer.",
            "rating_agreement": "G, X, Em, Eh, Es, Ecost agree and were re-checked; M and Ec resolved to son55.",
        },
    }

    # =========================================================== 2601.07641 Test-Time Tool Evolution (Δ1.25)
    p = "2601.07641"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "simulate its execution and write down the structured result",
                    "Appendix B.3, hybrid tool-synthesis / answer prompt (Figure 7)",
                    "The prompt that produces the final answer asks the model to simulate code execution. This conflicts "
                    "with the 'Runtime Execution Engine' description and explains traces whose numbers do not follow "
                    "from the shown code."),
            opus_ev(p, "O02", "calculate_molar_mass(1.23, 13.738)", "Appendix G.1, Table 6 (Case 1 trace)",
                    "The step-3 'evolved' tool returns 13.738 L/mol. RT/P = 8.314·330/20000 m³/mol = 137.2 L/mol, and the "
                    "Figure 10 code would return 137.2. 1.23 × 13.738 = 16.9, not the reported 169.0. The trace is "
                    "arithmetically inconsistent.", kind="our_inference"),
            opus_ev(p, "O03", "The ground truth values are 33.98", "Appendix G.2, Case 2 problem definition",
                    "Ground truth for the Case 2 mass."),
            opus_ev(p, "O04", "In contrast, S+Tools achieves high precision", "Appendix G.2, Case 2",
                    "31.6 g (and 1283 cm² vs 1275.6) is presented as correct against 33.98 g, a 7% deviation. This "
                    "contradicts the stated 1e-5 relative tolerance, and Q=30,500 C does not equal 8.46 A × 8.0 h "
                    "(243,648 C).", kind="our_inference"),
            opus_ev(p, "O05", "For instance, with a library size of 100 on Qwen2.5-7B", "§6.1 Ablation Study",
                    "Accuracy is reported at preset library sizes (100/250/500, Table 4) although TTE-Zero is defined to "
                    "start from an empty library. The relation between the SciEvo library built with ground truth and "
                    "the scored runs is unclear."),
            opus_ev(p, "O06", "In the TTE-Adapt setting, we compare against a “No Tool” baseline and a “Source Only” baseline",
                    "§5.1 Baselines", "The only control that isolates evolved tools applies to the secondary "
                                     "adaptation claim; it has extra synthesis budget and is a single run."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("sol", p)["rs_pattern"]), "sol"),
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.07641-1"): "rs:decompose_and_delegate/RE-1"},
            overrides={
                "local:2601.07641-2": {
                    "status": "unmet",
                    "reason": "Opus: same statistics check in both seats. One run per cell; no seeds, intervals or "
                              "tests. Sample size and the non-monotone library-size result do not answer an "
                              "uncertainty requirement."},
                "rs:decompose_and_delegate/RE-1": {
                    "note": "sol's local-1 (cost) merged here: the same check as son55's RE-1 (both unmet)."},
                "rsi:crystallize_executable_capability/S2": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'met'). Synthesis only on a retrieval miss, plus CodeBERT "
                              "dedup, keeps the library compact. But a retrieval miss tests 'not in the library', not "
                              "'the policy cannot cheaply re-derive it', and Appendix F shows retrieval collisions grow "
                              "with library size. No check shows that admitted tools are capability increments."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02", "opus:O04"]),
        "assessment": assess("sol", p, [
            "Opus: whether final answers come from real tool execution or from the LLM 'simulating' execution "
            "(opus:O01); the appendix traces suggest the latter.",
            "Opus: how the scored SciEvo runs relate to the 925-tool library built with ground-truth answers on the "
            "same seed questions (opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static-library limits are real and the dynamic-tool "
                   "neighbours (CREATOR, CRAFT, LATM, ToolMaker, Voyager) are named. Scientific tool sparsity is "
                   "asserted, not measured, and the delta over persistent-library work is thinly argued.",
                   ["sol:E01", "sol:E02", "son55:E002"]),
            "M": R("resolved", 2, "Opus sides with son55. Decompose → retrieve → synthesize → verify → atomise → "
                   "dedup → prune is a coherent chain, but its premises are weak. 'Domain validation' is undefined. "
                   "The Eq. 8 bound assumes independent atomic reuse. Embedding similarity is used as functional "
                   "equivalence, and the paper's own Appendix F shows this collides as the library grows. The answer "
                   "prompt asks the model to simulate execution (opus:O01). No prediction separates the method from "
                   "per-problem generation. sol's 3 rated reconstructibility, which is X's question.",
                   ["son55:E004", "son55:E018", "opus:O01", "sol:E08"], ["son55:E016"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1, thresholds and capacity are given, and there "
                   "is admission plus usage-based retirement. Missing: domain validation, θ_min, label use at "
                   "evaluation, and a repair loop. Shared omission added: the answer prompt's 'simulate its execution' "
                   "(opus:O01) contradicts the execution-engine description. This fits X=2 ('key conditions unclear'), "
                   "not X=0, because the verifier and sandbox are still described as executing.",
                   ["son55:E004", "son55:E006", "son55:E019", "sol:E03", "opus:O01"]),
            "E.measurement": R("resolved", 1, "Opus sides with sol and extends the reason. Accuracy is judged by "
                               "GPT-4.1-nano under a stated 1e-5 relative tolerance (sol:E09), but the paper's own case "
                               "traces contradict that protocol. Case 1's evolved tool outputs 13.738 L/mol where RT/P "
                               "gives 137.2 L/mol, and the product 1.23×13.738 is reported as 169.0 (opus:O02). Case 2 "
                               "counts 31.6 g against a 33.98 g ground truth as correct, from a charge that is not "
                               "8.46 A×8 h (opus:O03, opus:O04). TRR is self-defined, and SciEvo is built by the method "
                               "under test (son55:E008). Not 0: the main tables use public benchmarks with an explicit "
                               "protocol.", ["sol:E09", "sol:E15", "opus:O02", "opus:O03", "opus:O04", "son55:E008"]),
            "E.causality": R("resolved", 1, "Opus sides with sol. The central TTE-Zero claim (accuracy from evolving a "
                             "retained library) has no library-off, per-problem-synthesis or module ablation. The "
                             "baselines' configurations and budgets are undescribed. Q+Tools vs S+Tools isolates "
                             "decomposition only, and Table 4 shows it is not uniformly better. The one control that "
                             "isolates evolved tools (Source Only vs TTE-Adapt, about +3 points, opus:O06) concerns the "
                             "secondary adaptation claim, is a single run, and leaves the extra synthesis budget "
                             "unmatched (A2: budget-unmatched controls → causality and cost). son55's 2 over-credits "
                             "that secondary control.",
                             ["sol:E11", "sol:E12", "opus:O06"], ["sol:E18"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The library evolves on the scored stream with no "
                           "adaptation/test split. SciEvo's 925 tools were admitted only if they produced the correct "
                           "ground-truth answers on the seed questions (son55:E007), and scored runs use preset library "
                           "sizes (opus:O05). The Materials→Chemistry/Physics adaptation gives only partial transfer "
                           "evidence.", ["son55:E007", "son55:E008", "sol:E05", "opus:O05"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample size (1,590) and negative boundaries "
                              "(non-monotone library size, weak models) are reported; main results are single runs "
                              "without intervals.", ["sol:E06", "sol:E18", "son55:E016"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked. Only the qualitative admission of "
                        "higher overhead appears (§8). No token, API-call, latency or wall-clock figures for synthesis, "
                        "verification or baselines.", ["sol:E13", "son55:E015"],
                        scope=["§5 implementation, §6 results, §8 limitations, Appendices A–J (incl. Tables 4–9, "
                               "case studies, theory) re-searched by Opus for cost/token/latency/time figures"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–J read. In scope (system_method): a persistent "
                  "executable tool library written from execution feedback and reused on later problems. All eight "
                  "items resolved (E.cost not_reported with search scope).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 4, 8, 9 are image-only; ratings use Tables 1–4 and text.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["crystallize_executable_capability", "H07"], ["evidence_gated_retention", "H30"]],
                "H07 kept (both seats). H30 added at medium fit: admission (verification + CodeBERT dedup) is paired "
                "with retirement (usage-count pruning under a hard capacity C=500), which is H30's admission/retirement "
                "pairing. The marginal-gain or counterfactual test H30 also expects is absent (recorded as S2 "
                "partial).", ["son55:E005", "son55:E006"], NOSCORE),
            XC(p, "local:2601.07641-2", "son55", "unmet",
               "Same statistics check in both seats. No seeds, intervals or tests for any cell, so unmet. sol's "
               "'partial' credited sample size, which is not uncertainty.", ["son55:E010", "sol:E18"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "same_supported_fact", "unmet",
               "Cost accounting. sol recorded the same unmet check as local-1 (A4 collision with son55's local-1 = "
               "holdout), and it is merged here.", ["son55:E015", "sol:E13"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: only decomposition is ablated; verifier, dedup, atomisation, pruning and retention are not.",
               ["son55:E011"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: three benchmarks, four sciences, three backbones and one adaptation pair. SciEvo is "
               "self-built.", ["son55:E008", "son55:E012"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "Verified: the baselines are named, but their configurations, backbone parity and budgets are not "
               "described.", ["son55:E010"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "partial",
               "Verified: five-module system with only decomposition ablated, so the executable artifact's isolated "
               "contribution is untested.", ["son55:E011"]),
            XC(p, "rsi:crystallize_executable_capability/S2", "revised", "partial",
               "A retrieval-miss trigger plus dedup bounds redundancy but does not show capability increment, and "
               "Appendix F's tool-overload result cuts against it. Matches sol's own condition check (partial).",
               ["son55:E005", "sol:E07", "sol:E08", "son55:E016"]),
            XC(p, "rsi:crystallize_executable_capability/S4", "son55", "unmet",
               "Verified: a failed synthesis falls back to reasoning or PoT (App. A.2); there is no traceback-driven "
               "repair.", ["son55:E019"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "partial",
               "Verified: admission and retirement both exist; θ_min and the gate's measured effect are not reported.",
               ["son55:E005", "son55:E006"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: undefined domain validation, similarity used as functional equivalence (contradicted by "
                "App. F), simulated execution in the answer prompt (opus:O01), and no separating prediction against "
                "per-problem synthesis.", ["son55:E004", "son55:E018", "opus:O01"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 1,
                "See ratings.E.measurement. Both case traces contradict the stated grading protocol: an arithmetic error "
                "of 10× in an 'executed' tool, and a 7% miss graded correct under a 1e-5 tolerance (opus:O02–O04). "
                "son55 did not check the traces.", ["sol:E15", "opus:O02", "opus:O03", "opus:O04"],
                "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", 1,
                "See ratings.E.causality. The central retention claim has no control. The only isolating control "
                "concerns the secondary adaptation claim, without budget matching or repeats.",
                ["sol:E11", "sol:E12", "opus:O06"], "−3.75 vs son55 (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.X.reason", "sol_value": "2 (no mention of simulated execution)",
             "son55_value": "2 (no mention of simulated execution)", "final_value": 2,
             "reason": "Shared omission, no rating change. Appendix B.3's answer prompt tells the model to 'simulate its "
                       "execution and write down the structured result' (opus:O01). This contradicts the "
                       "execution-engine description and is consistent with the inconsistent traces. Recorded in X "
                       "and M; X stays 2 because the verifier and sandbox are still described as executing.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–6, the limitations and Appendices A–I first. Initial view: "
                                                   "in scope (persistent tool library). Benchmark built by the method "
                                                   "with ground-truth admission (holdout weak), no retention ablation "
                                                   "(causality weak), no cost figures. The case traces are "
                                                   "arithmetically wrong and graded inconsistently with the stated "
                                                   "tolerance, and the answer prompt 'simulates' execution "
                                                   "(measurement weak).",
            "integrity_checks": "Both seats a1 on 2601.07641v1, material sha cadba4ff…; canonical seat hashes equal "
                                "conflicts.json; both used decompose_and_delegate/C25 and H07 with valid parentage.",
            "core_claim_check": "The strongest supported claim is author-reported higher accuracy and tool reuse in "
                                "single runs. Retained-library causality, measurement fidelity and holdout are not "
                                "established. evidence_level 'task' kept: the library evolves on the scored stream.",
            "rating_agreement": "G, X, Eh, Es, Ecost agree and were re-checked (X reason supplemented); M → son55, "
                                "Em and Ec → sol.",
        },
    }

    # =========================================================== 2601.11100 ReCreate (Δ8.75)
    p = "2601.11100"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "always run the specific FAIL_TO_PASS tests mentioned in expected_tests.txt before submitting",
                    "Appendix M, Figure 21 (retained Django memory mem_002)",
                    "The retained scaffold memory points the task agent at a file listing the FAIL_TO_PASS tests, which "
                    "are SWE-bench's hidden evaluation tests. Whether test-time sandboxes expose it is not reported."),
            opus_ev(p, "O02", "NEVER touch test files - your fix will be evaluated against hidden tests",
                    "Appendix M, Figure 19 (created instance template)",
                    "The same final scaffold forbids test access, which contradicts mem_002."),
            opus_ev(p, "O03", "ReCreate 60.19 39.77 77.74", "§5.4 Table 2 (action-level ablation)",
                    "The 'SWE' cell equals Table 1 Django only (Sympy 63.64 omitted). DS 77.74 cannot be derived from "
                    "Table 1 (mean of 77.00/68.63/85.19 is 76.94; instance-weighted is about 75.1). DA-Code 39.77 does "
                    "match the mean.", kind="our_inference"),
            opus_ev(p, "O04", "Django 60.66 61.14 63.51", "Appendix G, Table 4 (temperature sensitivity)",
                    "At the main setting t=0.0, Table 4 gives values that differ from Table 1 (Django 60.66 vs 60.19; "
                    "Algebra 95.16 vs 92.74; average 65.66 vs 66.15). This is an unstated rerun, evidence of run-to-run "
                    "variance."),
            opus_ev(p, "O05", "we configure the loop with a maximum iteration", "§5.1 Implementations",
                    "N_max=2 with batch size 4: at most 8 dev instances drive edits per domain."),
            opus_ev(p, "O06", "whereas ReCreate with gpt-5-mini fails to outperform them in most domains",
                    "§5.4 Reasoning-level ablation",
                    "Optimizer strength is load-bearing, yet the baselines' optimizer model is not stated."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus sides with sol on the main card, following the run convention for agents that turn a "
                      "conventionally fixed scaffold of an iterative agent loop into an editable variable (r03b SICA, "
                      "r08b Live-SWE-agent, r01b 2402.11359). ReCreate frames the human-designed scaffold "
                      "(role/process/tool/memory) as fixed and makes it a variable that is rewritten from experience. "
                      "Sub null: C15/C23/C24 are 3D/diffusion/conditioning-granularity specific. sol's supporting "
                      "adapt_via_conditioning is dropped: every harness paper conditions a frozen model, so the entry "
                      "does not discriminate, and sol itself marked C03's schema/held-out-category conditions as unmet. "
                      "son55's outside_taxonomy was considered and rejected. This differs from JudgeFlow in the same "
                      "batch (outside_taxonomy) because the two papers frame their move differently: ReCreate liberates "
                      "a human-fixed scaffold, while JudgeFlow adds a credit-assignment signal to a workflow that was "
                      "already free in AFlow.",
            "matches": [smatch("sol", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2601.11100-1"): "local:2601.11100-6",
                    ("sol", "local:2601.11100-2"): "local:2601.11100-3",
                    ("sol", "local:2601.11100-3"): "local:2601.11100-4"},
            overrides={
                "local:2601.11100-6": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = optimizer "
                                               "parity)."},
                "local:2601.11100-3": {"note": "sol's local-2 (statistics) merged with son55's local-3 (same question; "
                                               "both partial)."},
                "local:2601.11100-4": {"note": "sol's local-3 (cost) merged with son55's local-4 (same question; both "
                                               "partial)."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O04", "opus:O06"]),
        "assessment": assess("sol", p, [
            "Opus: the baselines' optimizer model and dev budget (opus:O06).",
            "Opus: whether expected_tests.txt (FAIL_TO_PASS) is visible to the task agent at test time (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The black-box scalar-metric framing of agent generation is "
                   "concrete and partly sourced (ADAS cost; Appendix E's 37-issue scaffold headroom shows scaffolds "
                   "matter). But the residual gap is drawn against metric-only optimisers, while trajectory-reading "
                   "scaffold editors (ExpeL, AWM, Live-SWE-agent, SCOPE, and the H12 trace-reading harness patchers) "
                   "already use 'why' evidence. The remaining gap beyond them is stated as scope, objective and "
                   "strategy, not shown. son55's own reason names this blur, which fits 2 better than 3.",
                   ["sol:E01", "sol:E02", "sol:E20", "son55:E003", "son55:E004"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Evidence retrieval → attribution → routed component edits "
                   "→ instance-to-domain synthesis responds to the stated bottlenecks. Not 4: attribution correctness "
                   "is unchecked, and no prediction separating it from simpler trace-based editors under equal "
                   "optimizer strength is tested.", ["son55:E001", "son55:E005", "son55:E006", "sol:E02"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Versioned global scaffolds, a skill-package tool layout, a "
                   "memory policy and conflict-resolution rules are described. There is no admission gate, replay or "
                   "rollback; N_max=2 (opus:O05); and the final scaffold contains a memory that contradicts its own "
                   "test prohibition (opus:O01, opus:O02).", ["son55:E007", "son55:E008", "sol:E05", "sol:E19", "opus:O05"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. Deterministic verifiers (SWE-bench tests, DS-1000 "
                               "checks, MATH answers, AppWorld) and a continuous DA-Code score are appropriate. But the "
                               "reported numbers are not internally consistent: Table 2's ReCreate row does not "
                               "reproduce Table 1 (SWE = Django only; DS 77.74 underivable, opus:O03), and Table 1 "
                               "averages pass rates with continuous scores. The run convention (r09b EvoRoute/AgentDevel) "
                               "caps E.measurement at 2 for cross-table inconsistency. The t=0.0 Table 4 rerun differing "
                               "from Table 1 (opus:O04) is charged to statistics, not here.",
                               ["sol:E08", "sol:E10", "opus:O03", "son55:E016"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There are a seed control and observation-, "
                             "action- and reasoning-level ablations. The weaker-optimizer ablation shows optimizer "
                             "strength is load-bearing, while the baselines' optimizer and dev budget are unstated "
                             "(opus:O06), and no per-edit store-off exists.",
                             ["son55:E017", "son55:E018", "son55:E019", "sol:E07", "opus:O06"]),
            "E.holdout": R("resolved", 2, "Opus sides with sol. The design is strong on paper: a separate ~20-instance "
                           "dev set, the rest held out, Math developed on AIME24 and tested on MATH500, the AppWorld "
                           "standard split, and extra SWE dev sets drawn from SWE-bench Full excluding Verified. But the "
                           "retained Django memory tells the task agent to run 'the FAIL_TO_PASS tests mentioned in "
                           "expected_tests.txt' (opus:O01). Those are SWE-bench's hidden evaluation tests, and the same "
                           "scaffold forbids test access (opus:O02). Whether that file exists in test-time sandboxes is "
                           "not reported, so the SWE holdout cannot be confirmed (A2: oracle/ground-truth signal → "
                           "holdout). Baseline dev usage is also unstated. son55's 3 did not examine the retained "
                           "artifacts.", ["sol:E04", "sol:E12", "sol:E15", "sol:E17", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder); re-checked. There are pooled McNemar tests "
                              "(N=1681) and a three-dev-set std on SWE. Main cells are single creation runs, and the "
                              "unstated t=0.0 rerun shows per-dataset swings of 2–3 points (opus:O04; ML varies up to "
                              "~10 across temperatures). No intervals.",
                              ["sol:E11", "sol:E13", "son55:E022", "son55:E024", "opus:O04"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. A 36–82% lower optimisation cost than ADAS is given "
                        "in text, but the absolute values are image-only (Figure 8). There is no comparison with other "
                        "baselines, no token accounting and no deployed-scaffold inference cost.",
                        ["sol:E09", "son55:E027"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–M read. In scope (system_method): a versioned non-weight "
                  "scaffold (prompts, workflow, skill tools, memory) is rewritten from execution experience and "
                  "evaluated on held-out instances. All eight items resolved; figure-only values recorded as such.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 5, 6, 8, 10, 11 carry their values only as images. Observation-level and "
                             "reasoning-level ablations, cost and model-swap results are used as described in captions "
                             "and text (e.g. 36–82%, +8.3/+8.7); no figure value was read or invented.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "Run convention for 'fixed scaffold of an iterative agent loop becomes an editable variable' (SICA, "
                "Live-SWE-agent). See rs_pattern.reason for the contrast with JudgeFlow.",
                ["sol:E02", "sol:E05", "son55:E005"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["generative_process_redesign", None]],
                "The primary is kept with sub null. sol's supporting adapt_via_conditioning is dropped: it does not "
                "discriminate, and C03's conditions are unmet by sol's own check.", ["sol:E03", "sol:E06"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["attribute_and_patch_incumbent", "H12"]],
                "H12 kept (both seats). H02 added at medium fit: the optimizer packages experience into SKILL.md-style "
                "tool directories and a static lesson memory that are reused across instances (App. D). The H02 "
                "retention gate is only the synthesis prompt.", ["son55:E010", "son55:E011", "sol:E06"], NOSCORE),
            XC(p, "local:2601.11100-1", "son55", "unmet",
               "A4 ID collision: sol's local-1 (component ablations/retention gate, partial) and son55's local-1 "
               "(optimizer parity with baselines) are different questions. Final local-1 = optimizer parity, unmet "
               "(opus:O06: a weaker optimizer erases the advantage, and the baselines' optimizer is unstated). sol's "
               "question becomes local-6 (partial).", ["son55:E019", "opus:O06"]),
            XC(p, "local:2601.11100-2", "son55", "unmet",
               "A4 ID collision: sol's local-2 (statistics) vs son55's local-2 (acceptance re-run before promotion). "
               "Final local-2 = acceptance gate, unmet (verified: the synthesised scaffold replaces the incumbent with "
               "no re-run or threshold). sol's statistics check merges into local-3.", ["son55:E008", "sol:E19"]),
            XC(p, "local:2601.11100-4", "same_supported_fact", "partial",
               "Cost check: sol's local-3 and son55's local-4 are the same question, and both are partial "
               "(ADAS-only, figure).", ["sol:E09", "son55:E027"]),
            XC(p, "local:2601.11100-5", "son55", "unmet",
               "Verified: there is no contamination or overlap analysis between public dev/test sets and model "
               "training data.", ["son55:E013"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "H12 step 4 (promote on a separate split). The dev/test split exists, but the retained mem_002 "
               "references the FAIL_TO_PASS evaluation tests (opus:O01), so test visibility needs an audit.",
               ["sol:E15", "opus:O01"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: evidence retrieval narrows attribution, but edits land as scaffold-wide diffs across "
               "prompt, tool and memory.", ["son55:E005", "son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "met",
               "Verified: the same DomainAdapter pipeline runs across four domains; the object is a general "
               "improver.", ["sol:E05", "son55:E009"]),
            XC(p, "rsi:evidence_gated_retention/F1", "son55", "unmet",
               "Failure mode present (unmet = not avoided): scaffold versions are stored without a measured "
               "admission or retirement test.", ["son55:E009", "son55:E008"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Verified: there is no with/without measurement per retained tool, rule or memory entry.",
               ["son55:E017", "son55:E018"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", 2,
                "See ratings.G: the 'metric-only' residual is blurred by trajectory-reading neighbours, and son55's own "
                "reason says so.", ["sol:E20", "son55:E003", "son55:E004"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement: Table 2's ReCreate row is inconsistent with Table 1 (opus:O03). Run "
                "convention caps this at 2.", ["sol:E08", "opus:O03"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", 2,
                "See ratings.E.holdout: the retained memory points at the hidden FAIL_TO_PASS tests (opus:O01, "
                "opus:O02), and test-time visibility is unreported. son55 did not inspect the retained artifacts.",
                ["sol:E15", "opus:O01", "opus:O02"], "−2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–7 and Appendices B–M first. Initial view: in scope "
                                                   "(versioned scaffold incl. tools/memory). The split design is "
                                                   "strong, but the retained Django memory references FAIL_TO_PASS "
                                                   "tests (holdout risk). There is no admission gate (X≈2). Table 2 "
                                                   "and Table 4 do not reproduce Table 1. The optimizer-strength "
                                                   "confound is unaddressed.",
            "integrity_checks": "Both seats a1 on 2601.11100v3, material sha 61c4ba40…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid (sol main card + null sub; son55 outside_taxonomy).",
            "core_claim_check": "The strongest supported claim is a ~20-instance-dev scaffold from a strong optimizer "
                                "beating the listed baselines on held-out instances (single runs, pooled McNemar). "
                                "Attribution of the gain to experience-driven design versus optimizer strength, and "
                                "the SWE test visibility, are unresolved. 'Retained' kept.",
            "rating_agreement": "M, X, Ec, Es, Ecost agree and were re-checked; G, Em and Eh resolved to sol.",
        },
    }
    return S
