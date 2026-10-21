"""Opus rulings for r07b a1 (data only; consumed by _build.py)."""
import copy


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    opus_page_ev, page_material = g["opus_page_ev"], g["page_material"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev,
                   "none (expectations are not scored directly)")

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

    def oos_ratings(reason):
        return {k: R("unknown", None, reason) for k in KEYS}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run precedent "
                                       "r05b/r06a/r07a).",
                "claim_support": None, "claim_support_note": note, "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_level_res(p, ev):
        return [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "null is canonical for out-of-scope rows (r05b/r06a/r07a precedent); the harness task/retained/improver "
                "ladder does not apply to weight-level work. sol's 'task' described the weight-training result only.",
                ev, "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
                "null is canonical for out-of-scope rows; claim support is not assessed under this rubric.", ev, "none"),
        ]

    OOS_TEXT = ["Opus: abstract, §1 and the method section read, then targeted reads of every retention/update passage "
                "(replay buffer, question pool, optimizer, what is evaluated) and the experiment setup, before opening "
                "seat records; full-text keyword sweep for buffer/reuse/retain/parameter/update/GRPO/REINFORCE."]

    # =========================================================== 2510.18821 SSP (both out_of_scope)
    p = "2510.18821"
    a3 = ("out_of_scope (rubric A3 bullet 1; EVIDENCE.md excludes self-play fine-tuning). Independently checked: one LLM "
          "plays proposer and solver (opus:O01); the proposer is updated by REINFORCE and the solver by GRPO (opus:O02), "
          "and every reported result is a trained checkpoint. The only cross-step non-weight state is a replay buffer of "
          "previously generated valid questions used to fill training slots and reset every 10 steps (opus:O03) — "
          "training data consumed by weight updates, never read by a deployed system; same ruling as r02a WebRL and "
          "r07a SPELL. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "text_sections": OOS_TEXT,
        "opus_evidence": [
            opus_ev(p, "O01", "acts simultaneously as both a task proposer and a problem solver", "Abstract",
                    "Both roles are the same learning LLM."),
            opus_ev(p, "O02", "The proposer is optimized using REINFORCE", "§4 implementation / Table 6",
                    "Both roles are updated by policy-gradient weight training (solver by GRPO)."),
            opus_ev(p, "O03", "We maintain a replay buffer of all previously generated valid questions. Invalid slots are "
                    "filled by sampling from the buffer", "Appendix, batch sampling ablation",
                    "The retained question pool exists only to fill RL training batches."),
            opus_ev(p, "O04", "the replay buffer is cleared every 10 training steps", "Appendix, Periodic Reset",
                    "The buffer is transient training machinery, not a retained harness component."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). Generate deep-search QA → RAG validity gate → train on the gated "
                      "distribution, with the solver's failures steering the proposer: C08's generate→steer→gate→retrain "
                      "loop. sol left sub null after rejecting C26; C08 is the better-fitting sibling (run precedent "
                      "R-Zero/SPELL).",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="partial (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational, out_of_scope)")],
                           "unassigned": False, "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; benchmark gains are author-reported RL checkpoints."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently confirmed)",
        "resolutions": oos_level_res(p, ["opus:O02", "opus:O03"]) + [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "Informational. Both seats agree on the parent; C08 (generate, steer by learner feedback, gate, retrain; "
                "the manufactured object is the training distribution) fits the proposer→RAG-gate→solver loop. sol "
                "rejected C26 correctly but did not test C08.", ["opus:O01", "opus:O03", "son55:E001", "son55:E002"],
                NOSCORE),
            X(p, "rsi:self_generate_the_curriculum/S1", *C(p, "expectations[rsi:self_generate_the_curriculum/S1].status"),
              "sol", "partial",
              "Informational for an excluded row: the RAG check feeds all proposer-retrieved documents to the same model "
              "family, so validity is anchored to retrieved evidence but not independent of the learner. son55 did not "
              "run expectations on an out_of_scope row, which the contract allows.", ["sol:E001", "sol:E002"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before opening seats: one LLM as proposer+solver, REINFORCE/GRPO "
                                                   "weight updates, question replay buffer reset every 10 steps → "
                                                   "out_of_scope under A3 bullet 1.",
            "integrity_checks": "Both seats a1 on 2510.18821v3, material sha 57044e53…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O04; the replay-buffer ablation (Full Reuse vs Periodic "
                                "Reset) concerns training-batch composition, not a retained harness artifact.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2510.23595 MAE (both out_of_scope)
    p = "2510.23595"
    a3 = ("out_of_scope (rubric A3 bullet 1). Independently checked: Proposer, Solver and Judge are one backbone whose "
          "weights are updated for all three roles each cycle (opus:O01); the Judge-filtered question set and pair set "
          "(opus:O02) are training data for those updates, and every result is the trained Qwen2.5-3B checkpoint "
          "(opus:O03). No prompt/skill/tool/workflow/memory/evaluator is retained and evaluated. Not scored; null is not "
          "a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "text_sections": OOS_TEXT,
        "opus_evidence": [
            opus_ev(p, "O01", "After the questions, answers, and scores are collected, the shared LLM backbone is updated "
                    "for all three roles simultaneously using the gradients gathered this cycle.", "§4 training loop",
                    "The improver's update target is the shared weights."),
            opus_ev(p, "O02", "Qualified questions evaluated by the Judge will be added to the valid dataset.",
                    "§4 training loop", "The retained question set is a training-data pool."),
            opus_ev(p, "O03", "Experiments on Qwen2.5-3B-Instruct demonstrate that MAE achieves an average improvement of "
                    "4.54% on multiple benchmarks.", "Abstract", "The evaluated product is the trained model."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). Both seats C26: Judge-produced scalar quality scores from the model "
                      "itself are optimized by RL; kept.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="partial (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="strong (informational, out_of_scope)")],
                           "unassigned": False, "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; gains are author-reported RL checkpoints."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently confirmed)",
        "resolutions": oos_level_res(p, ["opus:O01", "opus:O03"]),
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before opening seats: three roles from one backbone, synchronized "
                                                   "parameter update each cycle, question/pair datasets feed training → "
                                                   "out_of_scope under A3 bullet 1.",
            "integrity_checks": "Both seats a1 on 2510.23595v3, material sha 2ee5f869…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2510.24684 SPICE (both out_of_scope)
    p = "2510.24684"
    a3 = ("out_of_scope (rubric A3 bullet 1). Independently checked: a single model plays Challenger and Reasoner "
          "(opus:O01) and is updated by DrGRPO with role-specific advantages (opus:O02); the evaluated product is the "
          "trained model's reasoning scores. Corpus documents and generated questions are training inputs, not a "
          "retained non-weight harness component. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "text_sections": OOS_TEXT,
        "opus_evidence": [
            opus_ev(p, "O01", "a reinforcement learning framework where a single model acts in two roles", "Abstract",
                    "Both roles are one set of weights."),
            opus_ev(p, "O02", "which updates the LLM via DrGRPO with role-specific advantages", "§3 implementation",
                    "The improver's update target is the model weights."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). The Challenger generates document-grounded questions, invalid ones are "
                      "penalized/gated, the Reasoner's solve-rate variance steers the Challenger, and the model retrains "
                      "on the result: C08 (generate, steer, gate, retrain). Rewards are binary correctness and a variance "
                      "score, not preference pairs or comparative credit, so C26 does not fit.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="partial (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="strong (informational, out_of_scope)")],
                           "unassigned": False, "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; gains are author-reported RL checkpoints."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently confirmed)",
        "resolutions": oos_level_res(p, ["opus:O01", "opus:O02"]) + [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "Informational. C26 needs a comparative/preference signal as the unit of supervision; SPICE's rewards are "
                "document-verified correctness and a solve-rate variance used to steer generation, which is C08's "
                "learner-feedback-steered generate→gate→retrain loop.", ["opus:O01", "opus:O02", "son55:E001", "son55:E002"],
                NOSCORE),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before opening seats: single model in two roles, DrGRPO updates, "
                                                   "trained-model evaluation → out_of_scope under A3 bullet 1.",
            "integrity_checks": "Both seats a1 on 2510.24684v1, material sha 3e3f85c2…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O02.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2510.21614 HGM (both 67.5; shared-error check)
    p = "2510.21614"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "We compare the task performance of their best-belief final agents after a maximum allowance "
                    "of 800 benchmark task evaluations", "§4.2 setup",
                    "Table 2's HGM-vs-DGM/SICA accuracies are measured on the same SWE-Verified-60 / Polyglot tasks that "
                    "the 800 search evaluations and the best-belief choice used: selection set = reported set."),
            opus_ev(p, "O02", "is further adjusted by removing the file-editing tool, leaving only the bash tool, to "
                    "minimize initial inductive bias", "Appendix C.1",
                    "The §4.3 run (the only one with held-out evaluation) starts from a different, bash-only ancestor."),
            opus_ev(p, "O03", "The time limit is extended to five hours for both self-modification and task evaluation",
                    "Appendix C.1", "§4.3 also changes time limits (and uses 8000 evaluations), so it is a separate "
                    "configuration never run for DGM/SICA; its cost is not itemized."),
            opus_ev(p, "O04", "The agent discovered by HGM with GPT outperforms all other agents on the SWE-Bench Lite "
                    "leaderboard with officially checked results", "§4.3.2 Transfer to bigger LLMs",
                    "Leaderboard comparison across different backbones (GPT-5 vs SWE-agent + Claude 4 Sonnet)."),
            opus_ev(p, "O05", "SWE-agent (Best on the LB) 48.3 56.7", "Table 4",
                    "Leaderboard SWE-agent on Lite filtered/standard."),
            opus_ev(p, "O06", "HGM’s Best-belief SWE-Verified Agent + GPT-5 47.8 57", "Table 4",
                    "HGM+GPT-5 is below the leaderboard SWE-agent on the filtered (unseen) split and +0.3 pt (one task) "
                    "on standard: parity, not superiority."),
            opus_ev(p, "O07", "HGM Initial Ancestor 34.8 44.0 SWE-agent+GPT-5-mini 39.6 47.6 HGM’s Best-belief "
                    "SWE-Verified Agent 40.1 49.0", "Table 3",
                    "Held-out evidence: one search's final agent vs its ancestor (+5.3 pt ≈ 11/207 tasks) and vs a "
                    "backbone-matched SWE-agent (+0.5 pt ≈ 1 task); no DGM/SICA agent is evaluated here."),
            opus_ev(p, "O08", "as well as unweighted correlations of 0.512 and 0.8783", "§4.1 Results",
                    "Text gives 0.8783 for Polyglot unweighted; Table 1 gives 0.873 (minor text/table inconsistency)."),
            opus_ev(p, "O09", "HGM (Ours) 0.778 0.512 0.626 0.873", "Table 1", "Table value for the same cell."),
        ],
        "rs_pattern": {
            "primary": "assumption_audit_and_pivot", "supporting": ["reframe_as_solvable_object"],
            "outside_taxonomy": False,
            "reason": "Opus sides with son55. The load-bearing move pivots the assumption inside a selection rule (own "
                      "benchmark score as proxy for descendant productivity) to posterior sampling over clade statistics, "
                      "with an oracle-level certificate (Theorem 1) — C11's selection-rule pivot. The Gödel-POMDP Q-value "
                      "correspondence plus bandit machinery (UCB-Air, Thompson sampling) is a genuine supporting "
                      "reframe_as_solvable_object move (sub null: not relabeling, game or constraint).",
            "matches": [smatch("son55", p, "assumption_audit_and_pivot"),
                        smatch("son55", p, "reframe_as_solvable_object")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "make_the_improver_editable", "H20")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "local:2510.21614-3": {
                    "status": "partial",
                    "reason": "Opus revised from son55's challenged_with_evidence (that status is for a paper that "
                              "legitimately challenges an expectation; here the paper does not). Partly met: a "
                              "backbone-matched SWE-agent+GPT-5-mini control exists (opus:O07), but the GPT-5 'outperforms "
                              "all' statement rests on a cross-backbone leaderboard comparison and is below the leaderboard "
                              "agent on the filtered split (opus:O04–O06); margins are 1–4 tasks."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01"]), "C4", ["opus:O02", "opus:O04", "opus:O06"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained', re-checked: the archived self-modified agent code, selected on "
                                   "SWE-Verified, improves over its ancestor on 207 overlap-filtered SWE-Lite tasks "
                                   "(opus:O07). Not improver: no comparable-budget test that an improved self-modification "
                                   "mechanism yields better later edits; the CMP selector is fixed and human-designed.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("son55", p)["assessment"]["unresolved"] + [
                "The held-out §4.3 run uses a different (bash-only, 5-hour, 8000-evaluation) configuration never run for "
                "DGM/SICA (opus:O02, opus:O03), so held-out evidence does not cover the comparative claim."],
        },
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Specific selection-rule residual (parent chosen by own score) "
                   "in DGM/SICA with explicit lineage and per-sub-policy contrast (Table 5); not 4 because the mismatch is "
                   "shown only by weak positive correlations on each method's own tree, with no node counts or noise "
                   "ceiling, and archive-search neighbours outside the Gödel lineage are not covered.",
                   ["son55:E001", "son55:E009", "son55:E022", "sol:E009"], ["son55:E007"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Clade pooling → Thompson sampling → decoupled single-pair "
                   "evaluation is reconstructable and aimed at the stated allocation problem, with a distinguishable "
                   "prediction (correlation with descendant outcomes). Not 4: Theorem 1 holds only for the true CMP under "
                   "the GM's own policy, the estimator (count-weighted mean) differs from the definition (max), and no "
                   "node-level Thompson baseline separates the clade idea from the sampler.",
                   ["son55:E002", "son55:E003", "son55:E004", "son55:E005", "son55:E025", "sol:E001", "sol:E007"],
                   ["son55:E005"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithm 1, α, τ, ε, the archive and best-belief rule are "
                   "fully specified and all children are archived; deductions: the self-modification step is inherited "
                   "from DGM and not described, no invalid-child rate or rollback accounting (F2), immutable anchor not "
                   "named (S1).",
                   ["son55:E004", "son55:E006", "son55:E022", "son55:E023", "sol:E001", "sol:E002"],
                   ["son55:E012", "son55:E023"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Execution-based pass/fail on SWE-bench/Polyglot "
                               "with overlap filtering for Lite; the mismatch diagnostic target (clade max of empirical "
                               "means) is noisy and computed per tree; minor text/table inconsistency 0.8783 vs 0.873 "
                               "(opus:O08, opus:O09) does not change any conclusion.",
                               ["son55:E007", "son55:E008", "son55:E011", "son55:E017", "sol:E004", "sol:E005",
                                "opus:O08", "opus:O09"], ["son55:E007", "son55:E013"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same ancestor, backbones and 800-evaluation budget "
                             "for DGM/SICA, plus a backbone-matched SWE-agent; but no ablation separates clade pooling from "
                             "Thompson sampling, decoupled evaluation and async execution, SICA crashed mid-run, and the "
                             "'edge is not the backbone' wording rests on a one-task margin.",
                             ["son55:E010", "son55:E011", "son55:E019", "son55:E022", "sol:E003", "sol:E004"],
                             ["son55:E012", "son55:E019"]),
            "E.holdout": R("resolved", 2, "Opus shared-error correction (both seats 3). The comparative core claim (HGM "
                           "vs DGM/SICA, Table 2; and the 61.4% full-Verified result) is reported only on the sets used "
                           "for search and best-belief selection (opus:O01; EVIDENCE rule 2). The clean held-out evidence "
                           "(207 overlap-filtered Lite tasks) covers one HGM search's agent vs its ancestor and a "
                           "backbone-matched SWE-agent (opus:O07) — from a different bash-only, 5-hour, 8000-evaluation "
                           "configuration never run for DGM/SICA (opus:O02, opus:O03); Polyglot has no holdout; the "
                           "'outperforms all on the Lite leaderboard' claim is cross-backbone and below the leaderboard "
                           "agent on the filtered split (opus:O04–O06); no contamination check for GPT-5(-mini) on "
                           "public SWE-bench. Relevant held-out results exist, key coverage gaps remain → anchor 2.",
                           ["son55:E015", "son55:E016", "son55:E017", "son55:E018", "son55:E020", "sol:E005",
                            "opus:O01", "opus:O02", "opus:O03", "opus:O07"],
                           ["opus:O04", "opus:O05", "opus:O06"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder: sample sizes and a negative SICA "
                              "outcome reported, no uncertainty on main results). One run per method; margins of 2–4 "
                              "tasks on 60-task subsets and 1–4 tasks on Lite; correlations without n or CI.",
                              ["son55:E011", "son55:E014", "sol:E004", "sol:E008"],
                              ["son55:E006", "son55:E009", "son55:E018"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Allocated CPU-hours per method for 800 evaluations and "
                        "≈$5000 total are reported; no per-method token/dollar cost or number of generated agents, and the "
                        "8000-evaluation, 5-hour-limit §4.3 run is not itemized (opus:O03).",
                        ["son55:E010", "son55:E011", "son55:E021", "sol:E003", "sol:E006", "opus:O03"],
                        ["son55:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–F read; in scope (system_method): self-modified coding-agent "
                  "code retained in an archive and selected by clade statistics. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["assumption_audit_and_pivot", "C11"], ["reframe_as_solvable_object", None]],
                "C11 is the selection/acquisition-rule pivot with a re-derived certificate, which is exactly HGM's move "
                "(parent criterion: own score → clade posterior; Theorem 1 as oracle certificate). sol's own tactic steps "
                "describe C11 without naming it. The supporting reframe (acceptance as a Q-value in a Gödel POMDP, solved "
                "with bandit machinery) is load-bearing for the method's justification.",
                ["son55:E001", "son55:E002", "son55:E005", "son55:E009", "sol:E001", "sol:E007"], NOSCORE),
        ] + [
            X(p, eid, *C(p, f"expectations[{eid}].status"), "son55", fin, why, ev)
            for eid, fin, why, ev in [
                ("local:2510.21614-1", "partial", "Verified: evaluation counts matched; self-modification count, tokens "
                 "and parallelism differ; SICA crashed. sol covered the same fact under rsi:.../S4 (partial).",
                 ["son55:E010", "son55:E021", "sol:E006"]),
                ("local:2510.21614-2", "unmet", "Verified: no ablation isolates clade pooling from Thompson sampling, "
                 "decoupled evaluation or async; sol records the same gap in E.causality.",
                 ["son55:E022", "sol:E003"]),
                ("local:2510.21614-4", "partial", "Verified: CMP is defined as a clade max, estimated by a count-weighted "
                 "mean argued as a soft maximum; ε for final selection is set to 1 without justification.",
                 ["son55:E005", "son55:E025"]),
                ("rs:assumption_audit_and_pivot/RE-1", "partial", "Verified: Theorem 1 is oracle-level sufficiency only; "
                 "no regret/consistency result for the estimator.", ["son55:E002", "sol:E007"]),
                ("rs:assumption_audit_and_pivot/RE-2", "partial", "Verified: Assumption 1 is explicit but not shown to "
                 "hold for noisy SWE-bench evaluations or the async implementation (acknowledged bias).",
                 ["son55:E003", "son55:E006"]),
                ("rs:assumption_audit_and_pivot/RE-4", "met", "Verified: Table 5 contrasts the three sub-policies of SICA, "
                 "DGM and HGM; lineage from the Gödel Machine is explicit.", ["son55:E022"]),
                ("rs:assumption_audit_and_pivot/RE-6", "partial", "Verified: failure characterization is correlational "
                 "(Table 1, Fig. 1); no worked case of a high-score parent with unproductive descendants.",
                 ["son55:E009", "son55:E007"]),
                ("rsi:make_the_improver_editable/F2", "unmet", "Verified: no invalid-child rate, rollback or validity "
                 "handling reported for self-modifications (card used as a check only, A5).",
                 ["son55:E012", "son55:E023"]),
                ("rsi:make_the_improver_editable/F5", "unknown", "Verified: GPT-5 performs expansions and the agent has "
                 "bash; whether it could reach the evaluator or stronger models is not discussed (searched §4, App. C).",
                 ["son55:E023"]),
                ("rsi:make_the_improver_editable/S2", "met", "Verified: agents are valued by pooled descendant outcomes "
                 "(the CMP estimator), the card's core condition.", ["son55:E004", "sol:E001"]),
            ]
        ] + [
            X(p, "local:2510.21614-3", *C(p, "expectations[local:2510.21614-3].status"), "revised", "partial",
              "son55 recorded challenged_with_evidence, but that status is reserved for a paper that challenges an "
              "expectation with evidence; HGM does not. The expectation is partly met: a backbone-matched SWE-agent+"
              "GPT-5-mini control exists (opus:O07), while the GPT-5 'outperforms all' claim is cross-backbone and below "
              "the leaderboard agent on the filtered split (opus:O04–O06).",
              ["opus:O04", "opus:O05", "opus:O06", "opus:O07", "son55:E019", "son55:E020"]),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3},
             "final_value": {"status": "resolved", "rating": 2},
             "correction": "Both seats credited the 207-task filtered Lite holdout as if it certified the central claim. "
                           "It does not cover the comparative part (HGM vs DGM/SICA is selection-set only, opus:O01), and "
                           "neither seat recorded that the held-out run is a different configuration — bash-only "
                           "ancestor, 5-hour limits, 8000 evaluations (opus:O02, opus:O03) — never run for the baselines. "
                           "Under EVIDENCE rule 2 and the 0/2/4 anchors this is 'relevant results with key coverage gaps', "
                           "not between 2 and 4.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O07"],
             "score_impact": "E.holdout 3→2: −10/4 = −2.5; final 65.0 (both seats 67.5)"},
            {"field_path": "expectations[local:2510.21614-3].status", "sol_value": None,
             "son55_value": "challenged_with_evidence", "final_value": "partial",
             "correction": "Status-vocabulary misuse (son55 only; listed in resolutions as well).",
             "evidence_ids": ["opus:O06", "opus:O07"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before opening seats (full text + App. A–F): in scope, system_method, "
                                                   "retained. Expected G3/M3/X3, E.measurement 3, E.causality 2 (bundled "
                                                   "changes, no CMP-only ablation), E.holdout 2 (comparative claim only on "
                                                   "selection sets; held-out from a separate bash-only configuration), "
                                                   "E.statistics 1 (single runs), E.cost 2 → ≈65.",
            "integrity_checks": "Both seats a1 on 2510.21614v3, material sha 78b37212…; canonical seat hashes equal "
                                "conflicts.json; both completed 15+31 and domain identification; namespaces/parents valid.",
            "core_claim_check": "Table 2 selection-set status (opus:O01), held-out Table 3 scope (opus:O07), the §4.3 "
                                "configuration change (opus:O02/O03) and the GPT-5 leaderboard claim (opus:O04–O06) read "
                                "directly; 'retained' kept, 'improver' not supported.",
            "rating_agreement": "Seven items identical in both seats and confirmed; E.holdout corrected 3→2 as a shared "
                                "error. Final 65.0 vs both seats 67.5.",
        },
    }

    # =========================================================== 2511.03773 DreamGym (a3 both in-scope boundary → OOS)
    p = "2511.03773"
    a3 = ("out_of_scope (rubric A3 bullet 1; shared-error correction — both seats' a3 records judged it an in-scope "
          "boundary case). What is updated and evaluated is policy weights: synthetic rollouts are consumed by GRPO/PPO "
          "(opus:O02), and every reported number — Table 1, Table 2, Fig. 3 — is the trained policy's success rate "
          "(opus:P07, opus:P09). The experience model and task generator are themselves SFT-trained weights. The two "
          "non-weight states the seats relied on, the replay buffer and the generated task pool, exist only to produce "
          "RL training data (opus:O09); neither is read by a deployed agent, and neither is itself evaluated as an "
          "artifact — Fig. 4 judges static simulator variants (w/o History / w/o Reasoning), not the grown buffer or "
          "pool (opus:O08), and Table 2's 'w/o Exp. Replay / w/o Task Generation' measure only downstream policy "
          "success. This is the r02a WebRL ruling (failure-seeded task pool + replay buffer as training data for "
          "weights → out_of_scope) and differs from cal-h1-v2 POET, where the retained environment population is itself "
          "evaluated. son55 recorded exactly this flip condition. Not scored; null is not a zero-quality rating.")
    shadow_note = ("Informational only, NOT a score (row is out_of_scope): had the row been in scope, Opus would rate "
                   "G2 (son55), M2 (son55), X2, E.measurement 2, E.causality 2, E.holdout 2 (conditional), "
                   "E.statistics 1, E.cost 1 (son55) → 47.5. E.holdout is conditional on an unreported fact: the WebArena "
                   "experience model is trained on leaderboard demonstrations (opus:O03) with no stated exclusion of the "
                   "165 Lite evaluation tasks (opus:O12 states exclusion only for agent training tasks); an in-scope "
                   "final would need that evidence.")
    S[p] = {
        "base": "son55",
        "paper_update": {"scope_note": "out_of_scope by Opus aggregate (A3 bullet 1); both seats a3 had in_scope_boundary"},
        "text_sections": ["Opus: complete pinned text read end-to-end (abstract, §1–7, Limitations, Appendices A–B, App. C "
                          "headings) before opening seat records; page images p-07 (Table 1), p-08 (Fig. 3, §5.2) and "
                          "p-09 (Table 2, Fig. 4) read; targeted re-reads for every disputed field. Appendix C prompt "
                          "bodies (image-only) not re-read: they are static prompts and bear on no scope fact."],
        "extra_materials": [
            page_material(p, "p-07.png", ["Table 1 (all cells), §4.3 sim-to-real, §5.1 setup"]),
            page_material(p, "p-08.png", ["Figure 3 (left/middle/right), §5.2 main results"]),
            page_material(p, "p-09.png", ["§6.1–6.3, Table 2, Figure 4"]),
        ],
        "opus_evidence": [
            opus_ev(p, "O01", "achieve success rates exceeding 30% across all backbones", "§5.2 Non-RL-ready environment",
                    "Absolute-rate statement contradicted by Table 1 (WebArena DreamGym 9.1–14.5, opus:P07)."),
            opus_ev(p, "O02", "The collected rollouts are used with standard RL algorithms", "§4.3 Policy training",
                    "Synthetic experience is consumed by policy-gradient weight updates."),
            opus_ev(p, "O03", "we extract successful demonstrations from the highest-performing agents on the public "
                    "WebArena leaderboard", "Appendix A.3 DreamGym Settings",
                    "Experience-model training data are real leaderboard trajectories; overlap with the 165 Lite "
                    "evaluation tasks is not addressed."),
            opus_ev(p, "O04", "In total, we obtain 4,800 offline trajectories for training.", "Appendix A.3",
                    "Real offline data used by DreamGym but not counted in Table 1's 'Real Data = 0'."),
            opus_ev(p, "O05", "we construct a dataset by combining 1,600 human demonstration trajectories from the official "
                    "WebShop repository with an additional 2,000 trajectories collected using an oracle agent and random "
                    "exploration", "Appendix A.1", "3,600 real trajectories (~36K transitions at ~10 steps) for WebShop."),
            opus_ev(p, "O06", "From the training split, we extract 3,200 expert demonstration trajectories paired with task "
                    "instructions, and additionally sample 2,000 offline trajectories using both oracle and random "
                    "policies", "Appendix A.2", "5,200 real trajectories for ALFWorld."),
            opus_ev(p, "O07", "Real data indicates the number of individual transitions", "Table 1 caption",
                    "The 'Real Data' column counts only online transitions; DreamGym's offline real data is excluded."),
            opus_ev(p, "O08", "We randomly sample 100 trajectories and prompt the model to assign discrete scores",
                    "Figure 4 caption", "The only direct evaluation of the simulator compares static model variants by "
                    "an LLM judge; the grown buffer/pool is never evaluated as an artifact."),
            opus_ev(p, "O09", "This buffer is seeded with offline knowledge for essential context and is continuously "
                    "enriched with trajectories generated on-the-fly", "§1",
                    "The replay buffer is simulator context whose purpose is producing training rollouts."),
            opus_ev(p, "O10", "can be made very small even when", "Appendix B.1 after Theorem 1",
                    "ε_R and ε_P are asserted small, never estimated."),
            opus_ev(p, "O11", "perform on par with GRPO and PPO agents trained on 80K real interactions, despite using "
                    "only synthetic rollouts", "§5.2 RL-ready environments",
                    "Contradicted for ALFWorld, where DreamGym is below real RL in all six cells (opus:P07)."),
            opus_ev(p, "O12", "The remaining 647 tasks, excluding those in the evaluation set, are used for training.",
                    "Appendix A.3 Training Set Split",
                    "Test-task exclusion is stated for agent training tasks only, not for the leaderboard demonstrations."),
            opus_page_ev(p, "P07", "p-07.png",
                         "Table 1, WebArena (L3.2-3B / L3.1-8B / Q2.5-7B): GRPO Traditional 7.3/6.1/6.1, DreamGym "
                         "13.3/9.1/12.7; PPO Traditional 6.7/4.8/7.3, DreamGym 14.5/10.9/10.0. ALFWorld: GRPO Traditional "
                         "65.3/70.9/79.8 vs DreamGym 62.1/66.3/71.0; PPO Traditional 47.0/72.9/81.1 vs DreamGym "
                         "40.5/70.8/72.7. Real Data: DreamGym 0, DreamGym-S2R 5K, Traditional 80K, SFT 20K, DPO 40K.",
                         "page 7, Table 1",
                         "All reported outcomes are trained-policy success rates; WebArena 9.1–14.5 (not >30%); ALFWorld "
                         "synthetic-only below real RL in 6/6 cells; no seeds or intervals."),
            opus_page_ev(p, "P09", "p-09.png",
                         "Table 2: DreamGym 63.9 (WebShop) / 13.3 (WebArena); w/o Exp. Replay 59.2 / 9.7; w/o Exp. "
                         "Reasoning 55.8 / 7.3; w/o Task Generation 57.3 / 7.3. Single values, backbone not stated.",
                         "page 9, Table 2",
                         "63.9 equals Table 1's L3.1-8B GRPO WebShop cell, 13.3 the L3.2-3B GRPO WebArena cell: the two "
                         "columns appear to use different backbones; ablations measure only downstream policy success."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). Both seats C08: synthesize tasks and transitions, gate tasks by "
                      "reward variance and LLM selection, steer generation by the learner's outcomes, retrain the policy. "
                      "sol's supporting adapt_via_conditioning/C03 is rejected: C03's load-bearing claim is generalization "
                      "of a frozen model to never-seen task categories via a conditioning schema; here retrieval is an "
                      "internal input of an SFT-trained simulator and no category holdout of that kind is claimed "
                      "(son55 opened and rejected it for the same reason).",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="medium (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H23", fit="medium (informational, out_of_scope)"),
                        dmatch("son55", p, "index_experience_for_reuse", "H03", fit="low (informational, out_of_scope)")],
            "unassigned": False,
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2511.03773-1"): "local:2511.03773-6",
                    ("sol", "local:2511.03773-2"): "local:2511.03773-7",
                    ("sol", "local:2511.03773-4"): "local:2511.03773-1",
                    ("sol", "rs:adapt_via_conditioning/RE-2"): "rs:self_supervised_signal_engineering/RE-6"},
            overrides={
                "local:2511.03773-1": {
                    "status": "unmet",
                    "reason": "Opus final (sol local-4 merged into son55 local-1, A4): Theorem 1's ε_R/ε_P are asserted "
                              "small (opus:O10) but never estimated, so the bound gives no guarantee for any reported run; "
                              "sol's 'partial' credited the existence of the derivation, which is M material, not an "
                              "answer to this check. Informational (out_of_scope)."},
                "local:2511.03773-3": {
                    "reason": "Both seats unmet, same question (A4 merge): text '>30%' success vs Table 1 9.1–14.5 "
                              "(opus:O01, opus:P07). Informational (out_of_scope)."},
                "local:2511.03773-6": {
                    "reason": "sol's local-1 (renamed, A4 hidden collision with son55 local-1): the GPT-4o fidelity judge "
                              "never sees real next states or rewards (opus:O08). Informational (out_of_scope)."},
                "local:2511.03773-7": {
                    "reason": "sol's local-2 (renamed, A4 collision with son55 local-2): no seeds/intervals for any Table "
                              "1/2 cell (opus:P07, opus:P09). Informational (out_of_scope)."},
                "rs:self_supervised_signal_engineering/RE-4": {
                    "status": "partial",
                    "reason": "Opus final (son55): the delta to UI-Simulator is argued in text; no head-to-head with "
                              "UI-Simulator/WebEvolver/WebRL. Answerable from the paper, so not unknown. Informational."},
                "rs:self_supervised_signal_engineering/RE-6": {
                    "status": "unknown",
                    "reason": "Opus final (son55; sol's rs:adapt_via_conditioning/RE-2 merged — same question, card "
                              "rejected): leaderboard demonstrations train the WebArena simulator (opus:O03) and no "
                              "exclusion of the 165 Lite eval tasks is stated (opus:O12 covers agent tasks only). "
                              "Informational (out_of_scope)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:P07", "opus:O11"]), "C2", ["opus:O01", "opus:P07"]),
        "assessment": oos_assessment("Not assessed under this rubric; Table 1/2 gains are author-reported RL checkpoints "
                                     "(seats' scoped narrowing is preserved in claims[] for reference)."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "out_of_scope (shared-error correction of both a3 seats' in_scope_boundary; WebRL precedent; flip condition "
              "named by son55 itself)",
        "figure_dependence": "Table 1/Table 2 cells read from page images p-07/p-09 (text layer agrees); Fig. 3/4 read "
                             "from p-08/p-09.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "Informational. C08 agreed; sol's supporting C03 rejected (see rs_pattern.reason).",
                ["son55:E002", "son55:E003", "son55:E013", "sol:E002", "sol:E004"], NOSCORE),
            X(p, "local:2511.03773-2", *C(p, "expectations[local:2511.03773-2].status"), "revised",
              "unmet (local-2 = son55's offline-data accounting question); sol's question kept as local-7 (partial)",
              "A4 hidden collision: sol's local-2 asks about statistics (seeds/intervals), son55's about uncounted offline "
              "real data. Both are answered on the text: 3.6K–5.2K real trajectories and teacher traces are excluded "
              "from 'Real Data = 0' (opus:O04–O07) → unmet; no seeds/CI (opus:P07) → sol's partial kept under local-7. "
              "Informational (out_of_scope).",
              ["opus:O04", "opus:O05", "opus:O06", "opus:O07", "opus:P07", "son55:E025", "sol:E008"]),
            X(p, "local:2511.03773-4", *C(p, "expectations[local:2511.03773-4].status"), "son55",
              "unmet (merged into local:2511.03773-1)",
              "sol's local-4 is son55's local-1 (Theorem 1 premises). ε never estimated (opus:O10) → unmet. "
              "Informational (out_of_scope).", ["opus:O10", "son55:E031", "sol:E017"]),
            X(p, "local:2511.03773-5", *C(p, "expectations[local:2511.03773-5].status"), "sol", "partial",
              "son55 did not ask this (observation-interface/auxiliary-computation control); verified that the "
              "abstract-state mapping is described but not separately controlled for baselines. Informational.",
              ["sol:E011", "sol:E016"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"),
              "revised", "unknown (merged into rs:self_supervised_signal_engineering/RE-6)",
              "The adapt_via_conditioning match is rejected, so its RE-2 does not apply as such; the question it carried "
              "(leaderboard demonstrations vs evaluation tasks) is son55's RE-6. Status unknown, not partial: the paper "
              "is silent on that overlap (opus:O03, opus:O12). Informational.",
              ["opus:O03", "opus:O12", "son55:E008"]),
            X(p, "rs:self_supervised_signal_engineering/RE-4",
              *C(p, "expectations[rs:self_supervised_signal_engineering/RE-4].status"), "son55", "partial",
              "Answerable from the paper (delta argued, no head-to-head); absent neighbour full texts do not make it "
              "unknown. Informational.", ["son55:E022", "son55:E023"]),
            X(p, "rs:self_supervised_signal_engineering/RE-6",
              *C(p, "expectations[rs:self_supervised_signal_engineering/RE-6].status"), "son55", "unknown",
              "Verified silent in A.3 (opus:O03, opus:O12). Informational.", ["opus:O03", "opus:O12", "son55:E008"]),
            X(p, "rsi:self_generate_the_curriculum/F3", *C(p, "expectations[rsi:self_generate_the_curriculum/F3].status"),
              "son55", "partial",
              "In-loop certificates are LLM-produced; the endpoint is real-env evaluation. sol recorded the same fact as "
              "a domain condition ('present'). Informational.", ["son55:E036", "sol:E010"]),
            X(p, "rsi:self_generate_the_curriculum/S2", *C(p, "expectations[rsi:self_generate_the_curriculum/S2].status"),
              "son55", "unmet",
              "The frontier signal is reward variance on rollouts scored by the simulator itself, not a fixed real "
              "validation environment; sol's domain check said partial on the same fact. Informational.",
              ["son55:E002", "son55:E003", "sol:E003"]),
            X(p, "rsi:self_generate_the_curriculum/S5", *C(p, "expectations[rsi:self_generate_the_curriculum/S5].status"),
              "same_supported_fact", "partial",
              "sol's domain condition S5 is also partial on the same fact (time savings without diagnosis/generation "
              "ledger). Informational.", ["son55:E016", "sol:E007"]),
        ] + [
            res(f"ratings.{k}", *C(p, f"ratings.{k}"), "revised", {"status": "unknown", "rating": None},
                f"Superseded by the scope correction (out_of_scope rows carry eight unknowns). Informational merit "
                f"ruling had the row been in scope: {k} {v}.", ev, "none (row not scored)")
            for k, v, ev in [
                ("G", "→ 2 (son55): the curriculum neighbours (WebRL, AgentSynth, SCA) are named but not contrasted and the "
                      "retained-object residual is not articulated", ["son55:E022", "son55:E023"]),
                ("M", "→ 2 (son55): task gate and reward both come from the simulator, no independent validity anchor, "
                      "Theorem 1 premises never measured (opus:O10)", ["son55:E019", "son55:E036", "opus:O10"]),
                ("E.cost", "→ 1 (son55): 'Real Data 0' omits 3.6K–5.2K real trajectories, teacher annotation and "
                           "simulator SFT (opus:O04–O07); baseline limited to four sessions",
                 ["opus:O04", "opus:O05", "opus:O06", "opus:O07", "son55:E017", "son55:E024"]),
            ]
        ],
        "shared_error_corrections": [
            {"field_path": "status / scope", "sol_value": "reviewed (in scope, A-class, system_method)",
             "son55_value": "reviewed (in_scope_boundary)", "final_value": "out_of_scope",
             "correction": "Both a3 seats read A3 bullet 2 ('evaluated retained object is a non-weight harness component'), "
                           "but the retained buffer/task pool are not the evaluated objects: all results are policy "
                           "success (opus:P07, opus:P09), Fig. 4 evaluates static simulator variants (opus:O08), and the "
                           "pool/buffer serve only RL data production (opus:O02, opus:O09). A3 bullet 1 applies, as in "
                           "r02a WebRL; POET's in-scope ruling required the retained population itself to be evaluated.",
             "evidence_ids": ["opus:O02", "opus:O08", "opus:O09", "opus:P07", "opus:P09", "son55:E013"],
             "score_impact": "row not scored (sol 57.5, son55 47.5 → null; L=0, U=100, coverage 0)"},
            {"field_path": "assessment.evidence_level / assessment.claim_support", "sol_value": "task / scoped",
             "son55_value": "task / scoped", "final_value": "null / null",
             "correction": "Out-of-scope rows carry no harness evidence label or claim-support verdict (run precedent).",
             "evidence_ids": ["opus:O02"], "score_impact": "none"},
            {"field_path": "ratings.X, ratings.E.measurement, ratings.E.causality, ratings.E.holdout, ratings.E.statistics",
             "sol_value": "resolved 2/2/2/2/1", "son55_value": "resolved 2/2/2/2/1",
             "final_value": "unknown ×5 (agreeing values retained only as the informational shadow in aggregate_review)",
             "correction": "Consequence of the scope correction.", "evidence_ids": ["opus:P07"], "score_impact": "none"},
            {"field_path": "expectations[local:2511.03773-1]", "sol_value": "unmet — judge without real reference",
             "son55_value": "unmet — Theorem 1 ε never estimated",
             "final_value": "local-1 = son55's question (+ sol local-4); sol's local-1 renamed local-6",
             "correction": "A4 hidden collision (same ID, different questions, equal status), not flagged mechanically.",
             "evidence_ids": ["opus:O08", "opus:O10"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before opening seats (full text, p-07/p-08/p-09): the only evaluated "
                                                   "product is RL-trained policy weights; the buffer and task pool are "
                                                   "training-data machinery as in WebRL → out_of_scope (A3 bullet 1). "
                                                   "Independently noted: '>30%' vs Table 1 9.1–14.5; ALFWorld below real "
                                                   "RL 6/6; 'Real Data 0' omits 3.6K–5.2K offline trajectories; Table 2 "
                                                   "single values on mismatched backbones; no seeds; ε never estimated.",
            "integrity_checks": "Both seats a3 (a1 superseded, not read) on 2511.03773v2 text sha 8273f563… plus 27 "
                                "pinned page images; input_hash 0f022789… (v3 package); canonical seat hashes equal "
                                "conflicts.json (computed on a3).",
            "core_claim_check": "son55's seven text–table findings verified: '>30%' (opus:O01 vs opus:P07); ALFWorld 6/6 "
                                "below real RL (opus:P07, opus:O11); offline real data uncounted (opus:O04–O07); Table 2 "
                                "single-run, backbone mismatch (opus:P09); no seeds anywhere (text sweep); no gate-off or "
                                "seeded-static-store control (Table 2 removes whole modules); ε not estimated (opus:O10).",
            "rating_agreement": "Seats differed on G/M/E.cost (sol 57.5, son55 47.5); moot after scope correction.",
            "shadow_if_in_scope": shadow_note,
        },
    }

    return S


def batch_notes():
    return [
        "2510.18821 SSP, 2510.23595 MAE, 2510.24684 SPICE: both seats out_of_scope, independently confirmed under A3 bullet "
        "1 (self-play/co-evolution RL on shared weights; question pools and replay buffers are training data). "
        "Informational RS: SSP sub null → C08, SPICE C26 → C08 (run precedent R-Zero/SPELL); MAE C26 kept.",
        "2510.21614 HGM: seven items confirmed; shared-error correction E.holdout 3→2 — the comparative claim (vs DGM/SICA) "
        "is selection-set only and the 207-task held-out result comes from a separate bash-only/5-hour/8000-evaluation "
        "configuration never run for baselines. Final 65.0 (both seats 67.5). son55's challenged_with_evidence on "
        "local-3 revised to partial (status reserved for a paper challenging an expectation).",
        "2511.03773 DreamGym: both a3 seats judged in_scope_boundary; Opus rules out_of_scope (A3 bullet 1, r02a WebRL "
        "precedent; POET distinction) because the replay buffer and task pool are never evaluated as artifacts and serve "
        "only RL data production for policy weights. Informational shadow (not a score): 47.5 with E.holdout conditional "
        "on leaderboard-demo/eval-task overlap. If the controller wants a different scope policy for simulator-memory/"
        "task-pool papers, that is a card/rubric revision, not an in-batch re-score.",
        "Card revision proposals (not applied): son55's DreamGym note — state in self_generate_the_curriculum / A3 that "
        "training-time task pools and simulator memory feeding weight-trained policies are out of scope unless the "
        "retained population is itself evaluated (POET line); son55's H20 note on distinguishing selector improvements "
        "from edited improvers.",
        "No requests for new material.",
    ]
