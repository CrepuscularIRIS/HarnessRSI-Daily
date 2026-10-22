"""Opus rulings for r12a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Input override honoured: 2602.11182 (MetaMem) uses both seats' a3 records on the v3 package (text + 20 pinned "
        "page images, input_hash b3c38007…). The a1 MetaMem records were not opened. Opus read the text in full and "
        "opened pages 6, 7, 8, 12, 13 and 16–19.",
        "2602.10885 RLCER: out_of_scope confirmed independently. The reasoner and rubricator share one set of policy "
        "weights, and the gradients of both roles update those weights. Rubrics are generated per question and are not "
        "persisted; the §5.5 in-prompt hints are also per question. The persisted change is weights only (A3). "
        "evidence_level/claim_support set to null (out_of_scope canonical value).",
        "2602.21320 Tool-R0: out_of_scope confirmed independently. The Generator and Solver are both trained with GRPO, and "
        "the algorithm returns a trained Solver policy. The synthesized tasks are training data, not a retained harness "
        "component (A3). RS follows the run convention for proposer–solver co-training: C08 (son55).",
        "2602.05832 UI-Mem (seat Δ10): resolved to 53.75 (= son55). G → 2: related work names only replay and dense "
        "reward. No agent-memory/skill neighbour is examined. X → 2: none of the curriculum, UCB, dedup or "
        "reward-shaping constants are reported (θ_start/θ_end, λ ranges, λ_ucb, α, λ_o/λ_p, δ_dup). Three guidance "
        "strata share a group of G=4. There is no admission test, retirement or rollback. E.cost → not_reported 0: "
        "there is no GPU/emulator time, call count or latency for the 72B-VLM + DeepSeek-V3 judge, the Seed1.8 extractor "
        "or the retrieval LLM; training settings are not costs. The agreed items were re-checked and kept "
        "(M3 Em3 Ec2 Eh2 Es1). Shared omission recorded under E.holdout: the training examples are AndroidWorld apps "
        "(Markor, Audio Recorder), and the paper asserts the benchmarks are out-of-domain without an overlap audit.",
        "2602.08234 SkillRL (seat Δ1.25): final 50.0, below both seats. G → sol 2: the paper's own related work credits "
        "prior methods with distilling insights and names abstraction as the trend (EvolveR), which weakens the 'raw "
        "trajectories only' gap. E.holdout → son55 1: the library evolves on validation-set failures, the evolution "
        "benefit is shown on the validation curve, and the split behind Table 1 is not stated. Shared correction: "
        "E.measurement 3 → 2 (both seats). The text claims 10–20× token compression but measures a ~10.3% "
        "prompt-length reduction, and the Table 2 SkillRL average is 47.1 although its own row averages 47.5 (the "
        "EvolveR row recomputes exactly). The run convention caps cross-table/text inconsistency at 2. evidence_level → "
        "task (sol): EVIDENCE.md rule 2, the selection set is not a holdout. RS → adapt_via_conditioning/C03 primary "
        "(the convention for skill library + RL, as in r12b ARISE/MetaClaw).",
        "2602.11182 MetaMem (seat Δ3.75): final 56.25 (= son55). X → 2: there is no admission test, rollback or "
        "checkpoint rule. Accuracy falls after step 5 while units keep accumulating. 'Training step' cannot be "
        "reconciled with 5 epochs × 7 batches. E.statistics → 2: Table 5 gives paired per-fold results for five "
        "independently built meta-memories, including the losing Llama fold 1, which is A2 ladder level 2. All "
        "text–table inconsistencies the seats reported were verified. Opus adds the exact Table 1 denominators: the "
        "baselines are scored on a 400-item set (category n = 53/43/105/109/66/24; e.g. Full Text 206/400), while "
        "MetaMem is the mean of five 100-item folds (Table 3: 500). The same-fold LightMem means are 65.86 (Qwen) and "
        "66.08 (Llama). 'Over 3.6%' is the two-backbone mean (+4.40/+2.91). Em stays 2: the mismatch is a reporting "
        "flaw that does not inflate the Qwen gain. RS sub → null (sol; r10b convention: no canonical schema, upstream "
        "parsing phase or category holdout). Domain H01 + H00.",
        "A4 hygiene: hidden local-ID collisions renumbered in 2602.05832 (sol local-1/2 → local-5/6; sol local-4 merged "
        "into local-2), 2602.08234 (sol local-2 → local-5; sol local-3 merged into local-2) and 2602.11182 (sol local-2 "
        "→ local-7; sol local-3 merged into local-4).",
        "Figure dependence: UI-Mem Figures 5–7 and SkillRL Figures 3–5 carry their values only as images (not in the "
        "packages). Ratings use the values stated in the text and mark the pairings as such. MetaMem figures were read "
        "from the pinned page images.",
        "No material requests. Every disputed field could be answered from the pinned inputs.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, opus_img_ev, merge_exps = (g["R"], g["res"], g["conflict"], g["opus_ev"],
                                                          g["opus_img_ev"], g["merge_exps"])
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

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a = prefix(a, s)
        a.update(upd)
        return a

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                       "precedent r05b–r11a).",
                "claim_support": None, "claim_support_note": note, "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_level_correction(p, ev):
        sol_a, son_a = seat("sol", p)["assessment"], seat("son55", p)["assessment"]
        return [{"field_path": "assessment.evidence_level", "sol_value": sol_a.get("evidence_level"),
                 "son55_value": son_a.get("evidence_level"), "final_value": None,
                 "reason": "Both seats wrote 'task'. For out_of_scope rows the canonical value is null: the "
                           "task/retained/improver ladder in EVIDENCE.md grades retained non-weight changes, and this "
                           "paper has none (precedent r05b–r11a).", "evidence_ids": ev,
                 "score_impact": "none (evidence_level is not scored; row is unscored)"}]

    # =========================================================== 2602.10885 RLCER (both out_of_scope)
    p = "2602.10885"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "reasoner and rubricator are two prompts of one policy, and the gradients from both roles update the same "
          "parameters (opus:O01). Rubrics are proposed per question, filtered by their correlation with answer "
          "correctness inside the rollout group, and used once as reward. They are never stored as a reusable "
          "evaluator. The §5.5 'rubrics as in-prompt hints' are generated for the same question at inference "
          "(opus:O02), so no retained non-weight artifact is evaluated. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Gradients from both roles are aggregated to update the same set of parameters",
                    "§4 (joint optimisation of the shared policy)", "The improved object is the shared policy weights."),
            opus_ev(p, "O02", "we explicitly employ these self-proposed rubrics as in-prompt hints",
                    "§5.5 (RQ4)", "Hints are per-question generations, not a persisted rubric library."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55") | {
            "reason": "Informational (out_of_scope). Both seats: self_supervised_signal_engineering/C26 (a self-"
                      "manufactured dense CoT reward, filtered by its correlation with the verifiable outcome). "
                      "Identification only; no score effect."},
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "coevolve_the_evaluator", "H24",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; reasoning gains are author-reported results of "
                                     "RL-trained checkpoints."),
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Claim support is not assessed for an excluded row; null is canonical (precedent r09b GenEnv, r11a). "
                "sol's 'scoped' and son55's 'unresolved' both describe a judgment the rubric does not make here.",
                ["opus:O01"], "none (row unscored)"),
            XC(p, "local:2602.10885-1", "sol", "unmet",
               "Informational. Verified: nothing persists across steps except the shared parameters, and the hints are "
               "regenerated per question (opus:O01, opus:O02).", ["opus:O01", "opus:O02"]),
            XC(p, "rsi:coevolve_the_evaluator/H24", "sol", "partial",
               "Informational. Rubrics are generated, filtered by correlation with correctness and used as dense RL "
               "reward (the H24 move), but nothing is archived across steps.", ["opus:O01"]),
            XC(p, "rsi:coevolve_the_evaluator/S1", "son55", "unknown",
               "Informational; kept as son55 recorded it (not applicable to an excluded row). The retention test is "
               "per-question correlation with answer correctness.", ["son55:E004"]),
            XC(p, "rsi:coevolve_the_evaluator/S2", "son55", "unknown",
               "Informational; kept as son55 recorded it. The verifier is a separate frozen model, while rubric writer "
               "and reasoner share weights.", ["son55:E005"]),
        ],
        "shared_error_corrections": oos_level_correction(p, ["opus:O01", "opus:O02"]),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §1, §4 (two roles in one policy, rewards, joint "
                                                   "update), §5.5 and the appendix training details first: one shared "
                                                   "policy is RL-trained, and rubrics are per-question and transient → "
                                                   "out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2602.10885v1, material sha ffeaeb5a…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O02.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2602.21320 Tool-R0 (both out_of_scope)
    p = "2602.21320"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "Generator and Solver start from the same base LLM, are trained independently with GRPO (opus:O01, "
          "opus:O02), and the algorithm returns a trained Solver policy (opus:O03). The generated tasks are transient "
          "training data, and the task-specification config is author-set, not revised from feedback. Not scored; null "
          "is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "initialized from the same base LLM but trained independently", "§3 (framework)",
                    "Two policies, both trained."),
            opus_ev(p, "O02", "are optimized with GRPO", "§3 (training objective)", "The update is RL on weights."),
            opus_ev(p, "O03", "returns a trained Solver policy after K K co-evolutionary iterations",
                    "Appendix (Algorithm 1 description)", "The product is a weight checkpoint."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). The Generator, rewarded by the frozen Solver's answer uncertainty, "
                      "produces tasks that are filtered and used to retrain the Solver. This is C08's "
                      "generate → steer → filter → retrain loop, the run convention for proposer–solver co-training "
                      "(r05b R-Zero, r07b, r09b GenEnv, r11a Dr. Zero). sol's C26 is not used: C26 is the "
                      "preference-pair branch, and GRPO is a scalar group-baseline objective. sol's supporting "
                      "heterogeneous_decomposition is dropped: role separation is an ablation, not a partition by a "
                      "measured property.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering",
                               fit="high (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; tool-calling gains are author-reported results "
                                     "of GRPO-trained checkpoints."),
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Claim support is not assessed for an excluded row; null is canonical (run precedent).", ["opus:O03"],
                "none (row unscored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "Run convention for proposer–solver co-training; see rs_pattern.reason.",
                ["opus:O01", "opus:O02", "son55:E003"], NOSCORE),
            XC(p, "local:2602.21320-1", "sol", "unmet",
               "Informational. Verified: only parameters are updated, and no persisted prompt, tool or workflow is "
               "evaluated (opus:O03).", ["opus:O03"]),
            XC(p, "rsi:self_generate_the_curriculum/H22", "sol", "partial",
               "Informational. The H22 move is executed (difficulty-band reward to a co-trained proposer). The "
               "validity anchor is structural checks plus Solver self-consistency.", ["opus:O01"]),
            XC(p, "rsi:self_generate_the_curriculum/S1", "son55", "unknown",
               "Informational; kept as son55 recorded it (not applicable to an excluded row).", ["son55:E003"]),
        ],
        "shared_error_corrections": oos_level_correction(p, ["opus:O02", "opus:O03"]),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §1, §3 (Generator/Solver rewards, GRPO), the "
                                                   "role-separation ablation and the Algorithm 1 description first: "
                                                   "two GRPO-trained policies whose output is a Solver checkpoint → "
                                                   "out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2602.21320v1, material sha 6a79c92a…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2602.05832 UI-Mem (Δ10)
    p = "2602.05832"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "While our main benchmarks (AndroidWorld and AndroidLab) already evaluate out-of-domain tasks",
                    "§4.4 Cross-Application Generalization",
                    "OOD status of the main benchmarks is asserted, not audited."),
            opus_ev(p, "O02", "Rename file {{current_filename}} to {{new_filename}} in Markor.",
                    "Appendix B, Figure 8 (training memory example)",
                    "Training tasks run on AndroidWorld apps (Markor here; Audio Recorder in Appendix H). Training and "
                    "the AndroidWorld test therefore share apps, and the paper gives no instance-level overlap audit.",
                    kind="our_inference"),
            opus_ev(p, "O03", "For each query, we sample G = 4 G=4 outputs", "§4.1 Training Settings",
                    "Three guidance strata (strong/weak/none) share a group of only four rollouts. The proportions "
                    "λ_strong/λ_weak/λ_none and the curriculum thresholds are never given numerically, so the "
                    "stratification cannot be reconstructed.", kind="our_inference"),
            opus_ev(p, "O04", "disabling the memory update reduces performance to 62.9%", "§4.4 Component Analysis",
                    "The only evidence for the self-evolving loop is one number from Figure 5. The figure (model scale, "
                    "full-method reference value) is image-only and absent from the package; pairing 62.9 with 66.8 is "
                    "an inference.", kind="our_inference"),
            opus_ev(p, "O05", "Then we utilize an experience extraction module (Seed1.8 ( Seed, 2025a ) ) to obtain successful plans and failure diagnoses",
                    "§4.1 Reward Evaluation and Experience Extraction",
                    "Memory content is written by an external frontier model (plus Qwen2.5-VL-72B and DeepSeek-V3 "
                    "judging and abstraction). No call counts or time are reported for any of these."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["heterogeneous_decomposition"], "outside_taxonomy": False,
            "reason": "Opus sides with son55, following the run convention for memory/skill libraries coupled with RL "
                      "(r12b ARISE and MetaClaw, r09a): retrieved, instantiated experience is the conditioning input, "
                      "and the upstream RL phase trains the policy to read it (C03 step 3). The fit is partial because "
                      "weights also change. heterogeneous_decomposition (sub null) is a supporting match: guidance "
                      "strength is partitioned within each GRPO group, with a per-stratum reward bonus, and a "
                      "uniform-guidance ablation shows the drop. C04's compression tactic does not apply. sol's "
                      "generative_process_redesign is not kept. In this run that card marks liberating a "
                      "conventionally fixed component (r11a ReCreate), whereas UI-Mem adds guided sampling to "
                      "GRPO.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "heterogeneous_decomposition")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H04")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2602.05832-1"): "local:2602.05832-5",
                    ("sol", "local:2602.05832-2"): "local:2602.05832-6",
                    ("sol", "local:2602.05832-4"): "local:2602.05832-2"},
            overrides={
                "local:2602.05832-1": {"status": "unmet",
                                       "reason": "Opus verified: θ_start/θ_end, the λ ranges, λ_ucb, α, λ_o/λ_p and "
                                                 "δ_dup appear only as symbols; no values are given anywhere in the text "
                                                 "or Appendices A–H."},
                "local:2602.05832-2": {"status": "unmet",
                                       "reason": "Opus: same cost question in both seats (sol local-4 merged). No GPU, "
                                                 "emulator, wall-clock, token or call figure exists for training, the "
                                                 "judge, the extractor or retrieval. G=4 and 5 epochs are settings, "
                                                 "not costs.",
                                       "note": "sol's local-4 merged here (A4)."},
                "local:2602.05832-5": renum("sol:local:2602.05832-1"),
                "local:2602.05832-6": renum("sol:local:2602.05832-2"),
                "rs:adapt_via_conditioning/RE-6": {"status": "partial",
                                                   "reason": "Opus (revised from son55 'unknown'): sensitivity to the "
                                                             "source's quality is partly characterised (raw vs abstracted "
                                                             "memory, judge accuracy table, five unseen apps for the "
                                                             "source–test gap). Sensitivity to judge noise in what gets "
                                                             "written is not tested."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O04"]), "C1", ["opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: whether the ⋆ inference-time memory keeps updating on benchmark tasks is not stated.",
            "Opus: instance-level overlap between training tasks (AndroidWorld apps, AndroidLab-sourced instructions, "
            "GPT-4o augmentation) and the benchmarks (opus:O01, opus:O02)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The bottleneck is concrete: zero-variance all-failure GRPO "
                   "groups, and repeated errors across tasks. But the only neighbours examined are experience replay "
                   "and dense rewards (son55:E019). Agent-memory and skill neighbours that already abstract "
                   "workflows or failure lessons for reuse, and guidance-in-RL neighbours, are not discussed, so "
                   "the residual gap is unbounded. sol's own reason says the nearest neighbour is not pinned, which "
                   "fits 2, not 3.", ["son55:E019", "sol:E002", "son55:E015"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Abstracted templates → stratified guidance inside the "
                   "GRPO group → guidance withdrawn as success rises → unguided success bonus. This answers the "
                   "variance-collapse premise and makes a checkable prediction: non-zero intra-group variance, and "
                   "the unguided policy catches up (the no-memory 8B model scores 66.8 vs 57.3 for GRPO + progress "
                   "reward). Not 4: the judge-labelled admission premise is untested, and there is no account of why "
                   "gradients on guidance-conditioned contexts transfer to the unguided policy.",
                   ["son55:E001", "son55:E015", "son55:E016", "sol:E007", "sol:E017"], ["son55:E005"]),
            "X": R("resolved", 2, "Opus sides with son55. The read path (Algorithm 1) and the write path "
                   "(Algorithm 2: dedup merge or append, count updates) can be reconstructed. But the curriculum, UCB, "
                   "dedup and reward-shaping constants are all unreported, the two UCB formulas differ (Eq. 1 vs "
                   "Appendix E), and three strata share a group of four (opus:O03). Retention is judge verdict plus "
                   "cosine dedup only, with no admission test, retirement, versioning or rollback. These are key "
                   "conditions left unclear, which is anchor 2.",
                   ["son55:E002", "son55:E003", "sol:E005", "sol:E023", "sol:E025", "opus:O03"], ["son55:E018"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. AndroidWorld success comes from programmatic "
                               "system-state checks and AndroidLab reports standard multi-metrics. The training-time "
                               "judge has a reported accuracy/F1 comparison. In-text numbers match Tables 1–3. Not 4: "
                               "the judge's labelled audit set is undescribed, and ~10% judge error enters memory "
                               "writes.", ["son55:E004", "son55:E005", "son55:E020", "sol:E014", "sol:E022"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-scale 8B arms exist (GRPO, + progress "
                             "reward, + replay, inference-time prompting), along with component ablations. But the gain "
                             "bundles four mechanisms with external-teacher memory content (opus:O05). The self-evolving "
                             "claim rests on one image-only number (opus:O04). Table 1's other baselines are quoted "
                             "models, and no arm is budget-matched.",
                             ["son55:E011", "son55:E012", "son55:E013", "sol:E017", "opus:O04", "opus:O05"],
                             ["son55:E007", "son55:E008"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked with a shared omission added. Memory is built on "
                           "256 training queries and frozen policy/memory is evaluated on the benchmarks; five "
                           "unseen AndroidLab apps are an explicit structural holdout (figure-only). But training "
                           "instructions come partly from AndroidLab, and training examples run on AndroidWorld apps "
                           "(Markor, Audio Recorder: opus:O02). The paper asserts the benchmarks are OOD without any "
                           "overlap audit (opus:O01), and whether ⋆ memory updates at test time is unstated.",
                           ["son55:E006", "son55:E007", "son55:E014", "sol:E012", "sol:E019", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes (116/138 tasks) and failure cases "
                              "are given. Every result is a single run with no interval, seed or test, and gaps of "
                              "3–5 points are a handful of tasks.", ["son55:E020", "son55:E021", "sol:E014"]),
            "E.cost": R("not_reported", 0, "Opus sides with son55. Searched the full text and Appendices A–H: there "
                        "are no GPU/emulator hours, call counts, tokens or latency for policy training, the 72B-VLM + "
                        "DeepSeek-V3 judge, the Seed1.8 extractor, DeepSeek-V3 abstraction/matching or inference "
                        "retrieval, and no stated budget for baselines. sol's 1 credited G=4, 5 epochs and teacher "
                        "names, which are settings rather than cost evidence.",
                        ["son55:E022", "opus:O05"],
                        scope=["§4.1 Implementation Details, §4.3–4.4, Appendices A–H (incl. Algorithms 1–2, reward "
                               "model and extraction details) searched by Opus for compute, time, token, call-count "
                               "and latency figures"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–H read. In scope (system_method): a non-weight hierarchical "
                  "experience memory is written from execution feedback and retained. It is read at inference (⋆ rows), "
                  "and its on/off effect is reported on benchmark tasks not used to build it. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 5 (component analysis), 6 (unseen apps) and 7 (training dynamics) are "
                             "image-only and not in the package; only values stated in the text are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "Run convention for memory/skill libraries coupled with RL (r12b ARISE/MetaClaw); see rs_pattern.reason.",
                ["son55:E001", "son55:E016"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["heterogeneous_decomposition", None]],
                "C03 kept (both seats). heterogeneous_decomposition is kept as a supporting match for stratified "
                "guidance with a uniform-guidance ablation. generative_process_redesign is not kept.",
                ["son55:E016", "son55:E015"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["couple_context_and_weight_updates", "H28"], ["abstract_experience_into_guidance", "H00"],
                 ["index_experience_for_reuse", "H04"]],
                "H28 kept (both seats). H00 (sol) over H02 (son55): the memory distils the agent's own successes and "
                "failure diagnoses into abstracted lessons; it is not mined into portable multi-source skill "
                "packages. H01 (sol) dropped: there is no LLM-chosen edit policy, only a cosine-threshold merge with "
                "counts. H04 (son55) kept: the three-level hierarchy and vector index are load-bearing (hierarchy "
                "ablation). H29 was considered for the UCB ranking but rejected: the counts track plan success, "
                "not a counterfactual with/without credit.",
                ["sol:E008", "sol:E009", "son55:E002", "son55:E003"], NOSCORE),
            XC(p, "local:2602.05832-1", "son55", "unmet",
               "A4 collision: sol's local-1 (control coverage) and son55's local-1 (hyperparameter reconstructibility) "
               "are different questions. Final local-1 = hyperparameters, unmet (verified, no values anywhere). sol's "
               "question moves to local-5 (partial).", ["son55:E022", "opus:O03"]),
            XC(p, "local:2602.05832-2", "son55", "unmet",
               "A4 collision: sol's local-2 (judge audit) and son55's local-2 (cost) differ. Final local-2 = cost, "
               "unmet. sol's judge-audit question moves to local-6 (partial).", ["son55:E022", "opus:O05"]),
            XC(p, "local:2602.05832-3", "sol", "unmet",
               "Statistics check (sol only). Verified: single runs, no intervals or seeds.", ["sol:E014", "son55:E020"]),
            XC(p, "local:2602.05832-4", "revised", {"moved_to": "local:2602.05832-2", "status": "unmet"},
               "sol's cost check is the same question as son55's local-2. Merged there. Status unmet, not sol's "
               "partial: training settings are not cost figures.", ["sol:E011", "opus:O05"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: inference-only prompting and no-stratification variants exist, but no arm toggles training "
               "guidance alone with the other three components fixed.", ["son55:E011", "son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap or contamination audit, and the OOD status is asserted (opus:O01, opus:O02).",
               ["son55:E006", "son55:E007", "opus:O01", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: raw-memory and RAG-style prompting comparisons exist, but there is no budget-matched cheap "
               "alternative.", ["son55:E011", "son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "revised", "partial",
               "son55 wrote unknown, but the paper does report source-quality comparisons (raw vs abstracted, judge "
               "accuracy, unseen apps). Sensitivity to judge noise in writes is absent → partial.",
               ["son55:E005", "son55:E013", "son55:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "partial",
               "Verified: dedup merge, count updates and time decay exist; there is no capacity bound, conflict "
               "resolution or rollback.", ["sol:E010", "sol:E023", "sol:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
               "Verified: the gate is the judge verdict plus similarity dedup, with no marginal-utility test.",
               ["sol:E008", "sol:E010"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "sol", "partial",
               "Verified: memory is built on training queries and five unseen apps are tested, but the train/test "
               "overlap is unaudited and test-time memory updating is unstated.", ["sol:E012", "sol:E019", "opus:O01"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step3", "son55", "unmet",
               "Verified: rollouts are not tagged by memory version and there is no off-policy correction when "
               "guidance changes.", ["son55:E003"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step5", "son55", "partial",
               "Verified: weights-only (GRPO), context-only (prompting) and coupled arms exist, but they are single "
               "runs without budget matching.", ["son55:E011"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Verified: UCB uses success counts with no with/without-entry counterfactual.", ["son55:E018", "sol:E005"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "partial",
               "Verified: writes are gated by an LLM judge (F1 0.90), not an executable test.", ["son55:E004", "son55:E005"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: no agent-memory/skill or guidance-in-RL neighbour is examined, so the residual is "
                "unbounded.", ["son55:E019", "sol:E002"], "−3.75 vs sol (15×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2,
                "See ratings.X: the operating constants are unreported, the UCB formulas are inconsistent, three "
                "strata share G=4, and there is no admission/retirement/rollback.",
                ["son55:E003", "sol:E023", "opus:O03"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.cost: no cost figure of any kind is reported (search scope recorded).",
                ["son55:E022", "opus:O05"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.reason", "sol_value": "2 (no app-overlap note)",
             "son55_value": "2 (no app-overlap note)", "final_value": 2,
             "reason": "Shared omission, no rating change. The training examples run on AndroidWorld apps (Markor in "
                       "Figure 8, Audio Recorder in Appendix H; opus:O02), and the paper asserts the benchmarks are "
                       "out-of-domain without an audit (opus:O01). Recorded in E.holdout. The rating stays 2 because "
                       "the AndroidLab-source overlap both seats charged already bounds it, and the unseen-app test "
                       "remains.", "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–5 and Appendices A–H first. Initial view: in scope through "
                                                   "the ⋆ retained memory. G≈2 (no memory/skill neighbours), M 2–3, X 2 "
                                                   "(no constants, no gate), Em 3 (programmatic AndroidWorld), Ec 2, "
                                                   "Eh 1–2 (AndroidWorld apps in training, AndroidLab-sourced "
                                                   "instructions), Es 1, E.cost 0 (nothing reported).",
            "integrity_checks": "Both seats a1 on 2602.05832v1, material sha 8ef6ea28…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: author-reported single-run gains of the full memory-guided "
                                "RL recipe over same-scale GRPO/replay/dense-reward arms, plus +4.3 from inference-time "
                                "memory. 'Retained' is warranted by the ⋆ on/off on benchmark tasks; the self-evolving "
                                "contribution rests on one figure value.",
            "rating_agreement": "M, Em, Ec, Eh, Es agree and were re-checked (Eh reason supplemented); G, X, E.cost "
                                "resolved to son55. Final 53.75.",
        },
    }

    # =========================================================== 2602.08234 SkillRL (Δ1.25)
    p = "2602.08234"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Current research has moved toward self-improving memory, distilling interactions into higher-level insights or procedural tips",
                    "§5 Related Work (Memory Mechanisms)",
                    "The paper itself credits neighbours with distilling experience into insights/tips, which weakens "
                    "the abstract's 'existing methods primarily store raw trajectories' gap."),
            opus_ev(p, "O02", "recent trends suggest that the key to efficient experience transfer lies in abstraction",
                    "§5 Related Work (Agentic Skills and RL), citing EvolveR",
                    "Abstraction combined with RL already exists in EvolveR. The residual is hierarchy, cold-start SFT "
                    "and failure-triggered growth."),
            opus_ev(p, "O03", "Generate 1-3 NEW actionable skills that would help avoid these failures.",
                    "Appendix C.2, Prompt B.1 (dynamic skill discovery)",
                    "The evolution prompt only adds skills. Combined with 'SkillBank ← SkillBank ∪ S_new', there is no "
                    "refinement, consolidation or retirement step in the executed loop."),
            opus_ev(p, "O04", "Notably, skill distillation achieves 10–20", "§3.2 Skill Retrieval",
                    "The text claims 10–20× token compression, but the measured comparison reports only a ~10.3% "
                    "prompt-length reduction (son55:E026).", kind="our_inference"),
            opus_ev(p, "O05", "SkillRL achieves a state-of-the-art average score of 47.1%", "§4.2, Table 2",
                    "SkillRL's own Table 2 row (45.9, 63.3, 45.9, 43.2, 40.3, 20.2, 73.8) averages 47.51, not 47.1. "
                    "The EvolveR row recomputes exactly to 43.1, so the Avg column is a plain mean.",
                    kind="our_inference"),
            opus_ev(p, "O06", "After each validation epoch, we monitor the success rate", "§3.3 Recursive Skill Evolution",
                    "Library growth is driven by validation-set failures. The evaluation split behind Tables 1/3 is "
                    "never stated, and Figures 1(b)/5 plot the validation set."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["heterogeneous_decomposition"], "outside_taxonomy": False,
            "reason": "Opus sides with son55 on the primary. Both seats matched the same two cards and differed only in "
                      "which is primary. The run convention for skill libraries read by an RL-trained policy is "
                      "adapt_via_conditioning/C03, with cold-start SFT as the upstream phase that teaches the schema "
                      "(r12b ARISE, MetaClaw). heterogeneous_decomposition (sub null) is a supporting match: "
                      "general vs task-specific tiers and outcome-dependent distillation, with a load-bearing hierarchy "
                      "ablation (76.8 vs 89.9). The heterogeneity is designed rather than measured, so the fit is "
                      "partial.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "heterogeneous_decomposition")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2602.08234-2"): "local:2602.08234-5",
                    ("sol", "local:2602.08234-3"): "local:2602.08234-2"},
            overrides={
                "local:2602.08234-1": {"status": "unmet",
                                       "reason": "Opus: same question in both seats (isolating the library's "
                                                 "contribution). No arm keeps o3-trace SFT + GRPO with no skills in "
                                                 "context, and no store-off is run with the same trained policy. The "
                                                 "raw-trajectory swap changes the content, not its presence.",
                                       "note": "sol's local-1 (partial) and son55's local-1 (unmet) are the same "
                                               "check; resolved to unmet."},
                "local:2602.08234-2": {"note": "sol's local-3 (statistics, unmet) merged here; same question as "
                                               "son55's local-2."},
                "local:2602.08234-5": renum("sol:local:2602.08234-2"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C4", ["opus:O05"]), "C2", ["opus:O06"]),
        "assessment": assess("son55", p, [
            "Opus: whether Table 1/3 use the validation split that drives skill evolution (opus:O06)."],
            evidence_level="task",
            evidence_level_note="Opus (sol): the library evolves on validation failures, and its benefit is shown on "
                                "the validation curve. The Table 1/3 split is undeclared and no store-off arm with the "
                                "same trained policy exists. EVIDENCE.md rule 2 (selection set ≠ holdout) caps this "
                                "at task."),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. Raw-trajectory noise is a real, named bottleneck. But the "
                   "abstract's premise that memory methods 'primarily store raw trajectories' is weakened by the "
                   "paper's own related work, which credits prior work with distilling insights/tips (opus:O01) and "
                   "names abstraction plus RL as the trend (EvolveR, opus:O02). The in-paper raw-vs-library test "
                   "compares against raw trajectories, not against insight-distilling neighbours under RL, so the "
                   "residual (hierarchy, SFT, failure-triggered growth) is stated rather than bounded.",
                   ["sol:E001", "son55:E032", "opus:O01", "opus:O02"], ["son55:E014"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Distill → two-tier retrieval → SFT-taught use → GRPO "
                   "with failure-triggered additions is reconstructible and gives distinguishable predictions (raw vs "
                   "distilled, with/without SFT, static vs evolving). Not 4: there is no validity premise for admitted "
                   "skills, and the method depends on a strong teacher (Appendix D.3: a self-distilling 7B reaches only "
                   "42.5).", ["son55:E003", "son55:E004", "son55:E007", "son55:E009"], ["son55:E019"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. The read path, triggers and caps are given. The executed "
                   "evolution prompt only adds skills (opus:O03) and the library only grows (55→100). There is no "
                   "admission test, retirement, versioning or rollback.",
                   ["son55:E005", "son55:E008", "son55:E030", "son55:E036", "opus:O03"], ["son55:E022"]),
            "E.measurement": R("resolved", 2, "Shared correction (both seats 3 → 2). Environment success and EM are "
                               "appropriate metrics, but the reported numbers are not internally consistent. The text "
                               "claims 10–20× token compression while the measurement shows ~10.3% (opus:O04). The "
                               "Table 2 SkillRL average is 47.1 while its own row averages 47.5 (opus:O05). Table 1 "
                               "mixes baselines replicated from another paper (*) with re-run ones, and no test-split "
                               "sizes are given. Run convention (r09b, r11a): cross-table/text inconsistency caps "
                               "E.measurement at 2.",
                               ["son55:E012", "son55:E013", "son55:E035", "son55:E026", "opus:O04", "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Informative ablations exist inside the pipeline "
                             "(raw library, hierarchy, SFT, dynamic evolution). But the headline 'directly attributable "
                             "to skill augmentation' claim (son55:E011) is confounded with o3 SFT (7,500 traces) that "
                             "the replicated GRPO baseline lacks. w/o SFT (65.2) and the self-distilled variant (42.5) "
                             "both fall below that GRPO number. Not 1: the dynamic-evolution and hierarchy claims do "
                             "have matched in-pipeline controls.",
                             ["son55:E014", "son55:E015", "son55:E016", "son55:E020"],
                             ["son55:E011", "son55:E019", "son55:E033"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Evolution is triggered by validation-epoch failures "
                           "(opus:O06), and the benefit of evolution is shown on the validation curve. The split "
                           "behind Tables 1/3 is not stated, so a selection set may double as the reported set (A2: "
                           "selection signal → holdout). Only the QA transfer to unseen datasets gives holdout "
                           "evidence, and it is for the whole system, not the retained library.",
                           ["son55:E008", "son55:E021", "son55:E029", "opus:O06"], ["sol:E006"]),
            "E.statistics": R("not_reported", 0, "Both seats not_reported; re-checked. The authors answer No on "
                              "error bars. There are no seeds, repeats, test denominators or intervals for any table.",
                              ["son55:E025", "sol:E010"],
                              scope=["§4 (all tables), Appendix D (hyperparameters, compute, D.3), NeurIPS checklist "
                                     "item 7 searched by Opus for sample sizes, seeds, intervals or tests"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. 8×H100 and ~30 h per run with a stage breakdown are "
                        "given, plus a prompt-length comparison. o3 teacher usage (distillation, 7,500/2,400 SFT "
                        "traces, evolution calls) and baseline budgets are missing.",
                        ["son55:E023", "son55:E026", "son55:E034"], ["son55:E024"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–F and checklist read. In scope (system_method): a "
                  "non-weight SkillBank is evolved from execution failures and read by the trained policy at inference. "
                  "All eight items resolved (E.statistics not_reported with search scope).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 1(b), 3, 4, 5 are image-only; only text-stated values are used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "EVIDENCE.md rule 2: library edits are driven by validation failures, and the reported split is "
                "undeclared. No store-off with the same trained policy on an independent split exists.",
                ["son55:E008", "son55:E021", "opus:O06"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "Same two cards in both seats; primary set by the run convention for skill library + RL "
                "(see rs_pattern.reason).", ["son55:E005", "son55:E007"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H02"],
                 ["couple_context_and_weight_updates", "H28"]],
                "H00 and H28 are in both seats. H02 is added at medium fit: SkillBank follows the Agent Skills "
                "structured-package design (name/principle/when_to_apply, two-tier hierarchy). Its dedup/quality "
                "gate is absent (S5 unmet).", ["son55:E003", "son55:E009", "sol:E003"], NOSCORE),
            XC(p, "local:2602.08234-1", "son55", "unmet",
               "Same question in both seats (isolate the library's contribution). The required control is absent; "
               "sol's 'partial' credited the raw-swap and static-library ablations, which change the content or its "
               "evolution, not its presence under the same SFT/RL.", ["son55:E019", "son55:E033", "sol:E005"]),
            XC(p, "local:2602.08234-2", "son55", "unmet",
               "A4 collision: sol's local-2 (holdout boundary) vs son55's local-2 (statistics). Final local-2 = "
               "statistics, unmet (checklist No). sol's holdout question moves to local-5 (partial).",
               ["son55:E025", "sol:E010"]),
            XC(p, "local:2602.08234-3", "same_supported_fact", {"moved_to": "local:2602.08234-2", "status": "unmet"},
               "sol's statistics check is the same as son55's local-2; both unmet. Merged.", ["sol:E010", "son55:E025"]),
            XC(p, "local:2602.08234-4", "sol", "partial",
               "Cost (sol only). Verified: GPU hours are given; o3 calls and baseline budgets are absent.",
               ["sol:E008", "son55:E023"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: raw and hierarchy swaps exist, but there is no SFT+RL arm without skills in context.",
               ["son55:E014", "son55:E015"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unknown",
               "Verified: the ALFWorld/WebShop split and its overlap are not stated, so whether a leak exists cannot be "
               "determined.", ["opus:O06"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: raw-memory and Mem0/SimpleMem+GRPO hybrids are compared, but without teacher SFT and "
               "without budget matching.", ["son55:E014", "son55:E035"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "met",
               "Verified: three environment families and a second base model.", ["son55:E020", "son55:E028"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "met",
               "Verified: the hierarchy ablation isolates the two-tier structure (76.8 vs 89.9; 61.4 vs 72.7).",
               ["son55:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "unmet",
               "The executed evolution prompt only generates new skills (opus:O03) and the library is a union that "
               "grows 55→100. The 'refine existing skills' wording in §3.3 is not reflected in the prompt or the "
               "update rule, so no maintenance step exists. son55's partial credited that wording.",
               ["opus:O03", "son55:E022", "sol:E004"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: there is no execution test, quality filter or versioned merge for teacher-proposed skills.",
               ["son55:E009", "son55:E036"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "son55", "unmet",
               "Failure mode present: the library evolves on the validation stream, and the reported split is not "
               "declared.", ["son55:E008", "son55:E021"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step5", "son55", "partial",
               "Verified: weights-only GRPO and coupled arms exist; there is no seeded context-only arm.",
               ["son55:E012", "son55:E015"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", 2,
                "See ratings.G: the paper's own related work credits insight-distilling and abstraction+RL neighbours "
                "(opus:O01, opus:O02), so the residual is not bounded.", ["opus:O01", "opus:O02", "sol:E001"],
                "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: evolution runs on validation failures and the reported split is undeclared. "
                "sol's 2 leaned on QA transfer, which is for the whole system.", ["son55:E008", "opus:O06"],
                "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": 3, "son55_value": 3, "final_value": 2,
             "reason": "Shared error. Both seats rated the metrics as appropriate and missed the internal "
                       "inconsistencies. sol even noted 'do not read 10–20× as overall reduction' without charging it. "
                       "The 10–20× compression claim vs the ~10.3% measured reduction (opus:O04), and the Table 2 "
                       "average 47.1 vs the row mean 47.5 (opus:O05), fall under the run convention that caps "
                       "E.measurement at 2 for cross-table/text inconsistency (r09b; r11a ReCreate).",
             "evidence_ids": ["opus:O04", "opus:O05", "son55:E026", "son55:E028"],
             "score_impact": "−2.5 vs both seats (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–6 and Appendices A–F first. Initial view: in scope "
                                                   "(SkillBank read at inference). G 2 (own related work credits "
                                                   "abstraction neighbours), M 2–3, X 2 (add-only union), Em 2 "
                                                   "(10–20× vs 10.3%, Table 2 avg), Ec 1–2 (o3 SFT confound), Eh 1 "
                                                   "(validation-driven evolution, undeclared split), Es 0–1, "
                                                   "E.cost 1–2.",
            "integrity_checks": "Both seats a1 on 2602.08234v2, material sha f91297cb…; canonical seat hashes equal "
                                "conflicts.json; identical RS match sets with swapped primary; valid ids.",
            "core_claim_check": "Strongest supported claim: an o3-distilled skill library + o3-trace SFT + GRPO pipeline "
                                "beats the listed baselines in single runs, and in-pipeline ablations show the "
                                "hierarchy, the SFT and evolution matter on the (likely validation) split. Attribution "
                                "to skills alone versus teacher SFT is not established.",
            "rating_agreement": "M, X, Ec, Es, Ecost agree and were re-checked; Em corrected 3 → 2 (shared error); G → "
                                "sol, Eh → son55. Final 50.0.",
        },
    }

    # =========================================================== 2602.11182 MetaMem (Δ3.75; a3 / v3 package)
    p = "2602.11182"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Full Text 81.13 88.37 34.29 27.52 66.67 62.50 51.50", "Table 1 (Qwen3-30B rows)",
                    "Baseline cells resolve exactly to a 400-item set with category n = 53/43/105/109/66/24: Full Text "
                    "= 43+38+36+30+44+15 = 206/400 = 51.50, and LightMem = 48+14+66+70+50+22 = 270/400 = 67.50. "
                    "Table 3 lists 70/56/133/133/78/30 = 500 items, and MetaMem's 71.90 equals the mean of five "
                    "100-item folds in Table 5 (71.92). Method and baselines are therefore not scored on the same "
                    "item set.", kind="our_inference"),
            opus_ev(p, "O02", "outperforming the strongest baseline by over 3.6%", "§5.1 Overall Performance",
                    "Table 1 gaps over LightMem are +4.40 (Qwen) and +2.91 (Llama), mean 3.66. 'Over 3.6%' holds only "
                    "as the two-backbone mean. On the same folds (Table 5) the LightMem means are 65.86/66.08, so the "
                    "fold-matched gains are +6.06/+3.00.", kind="our_inference"),
            opus_ev(p, "O03", "compared with MetaMem w/o Evolution, MetaMem achieves more than 3% performance improvements",
                    "§5.2 Ablation Study", "Table 2 gives +3.57 (Qwen) but +2.66 (Llama). The 'more than 3%' claim "
                                           "fails for Llama.", kind="our_inference"),
            opus_ev(p, "O04", "the remaining data is partitioned into 350 samples for meta-memory training and 50 samples for validation",
                    "Appendix A.5", "350 samples at batch size 50 for 5 epochs (A.3) is 35 update steps, yet Figures "
                                    "4/6 plot 'training steps' 1–9. The paper never states which step is reported or "
                                    "whether the 50-sample validation split selects it.", kind="our_inference"),
            opus_img_ev(p, "O05", "p-08.png", "Figure 4: Performance of the Evolved Meta-Memory across Different Training Steps.",
                        "page 8 image, Figure 4(b)",
                        "Read from the image: the Knowledge-Update curve stays at or below ~73.5 over steps 1–9, and "
                        "Multi-Session peaks ~71.6 at step 5. Table 1 reports KU 79.18 for the same backbone, so the "
                        "step curves do not contain the headline checkpoint, and their evaluation set is unstated.",
                        kind="our_inference"),
            opus_img_ev(p, "O06", "p-19.png", "Each must be generalizable (not specific to one question type)",
                        "page 19 image, Figure 15 (filter prompt, Quality Control)",
                        "The batch filter applies a prompt-level generality/format check. It is a quality filter, but "
                        "it does not test an edit against outcomes."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning primary. The learned guideline list conditions a frozen "
                      "answerer at inference. Sub → null (sol), following the r10b Self-Consolidation convention. "
                      "C03's tactic needs a canonical schema, an upstream phase that teaches the model to parse it, "
                      "and category-level holdout. MetaMem has none of these: the model is never trained, the whole "
                      "list is injected without retrieval, and the folds are random rather than by category. Patterns "
                      "do not score.",
            "matches": [smatch("sol", p, "adapt_via_conditioning", sub_id=None, fit="partial")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"][0]), "son55") | {
            "rs_sub": None,
            "opus_note": "rs_sub set to null (C03 tactic not executed; see rs_pattern.reason). The domain "
                         "correspondence to H01 is unchanged; H00 also applies (contrastive reflection over k=5 "
                         "sampled answers)."}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2602.11182-2"): "local:2602.11182-7",
                    ("sol", "local:2602.11182-3"): "local:2602.11182-4"},
            overrides={
                "local:2602.11182-3": {"reason": "Opus verified and extended: Table 1 baselines are scored on a "
                                                 "400-item set while MetaMem is a five-fold mean over 500 (opus:O01). "
                                                 "Qwen LightMem 67.50 vs the Table 5 fold mean of 65.86. 'Over 3.6%' "
                                                 "is a mean, with Llama +2.91 (opus:O02).",
                                       "status": "unmet"},
                "local:2602.11182-4": {"status": "unmet",
                                       "reason": "Opus: same cost question in both seats (sol local-3 merged). "
                                                 "Inference tokens/latency are reported, but the offline construction "
                                                 "cost is not: 5 samples, judge, reflection, edit and filter calls per "
                                                 "question over 5 epochs. Construction is the method's main extra "
                                                 "cost, so the requirement is unmet.",
                                       "note": "sol's local-3 merged here (A4)."},
                "local:2602.11182-7": renum("sol:local:2602.11182-2"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O02"]), "C2", ["opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: what a 'training step' is (35 update steps implied vs 9 plotted) and which checkpoint Tables 1/2 "
            "report (opus:O04, opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The utilisation gap (fragmented, contradictory memory "
                   "units) is concrete. But neighbours cover memory construction only; experience-to-guidance text "
                   "stores and prompt optimisers are absent, and the gap is shown by one case.",
                   ["son55:E003", "son55:E004", "son55:E045", "sol:E07"], ["son55:E054"]),
            "M": R("resolved", 3, "Both seats 3; re-checked on the page-image prompts. Judge → k=5 contrastive "
                   "reflection → add/update/delete proposals → batch filter → next batch reads the list → frozen list "
                   "at inference. This targets the reader side and gives distinguishable predictions. Not 4: the "
                   "learned units are not separated from the new 5-step answer template or the hand-seeded example "
                   "guidelines in the editor prompt.", ["son55:E006", "son55:E007", "son55:E008", "son55:E009",
                                                         "son55:E041", "sol:E03"], ["son55:E040", "son55:E042"]),
            "X": R("resolved", 2, "Opus sides with son55. Information permissions and the read/write chain can be "
                   "reconstructed from Figures 12–15. But retention is unconditional: the filter is prompt-level "
                   "(opus:O06), and no edit is admitted by an outcome test. There is no rollback or version selection, "
                   "and accuracy falls after step 5 while units keep accumulating, so the missing gate is exercised. "
                   "What a 'training step' is (35 implied updates vs 9 plotted) and which checkpoint is reported "
                   "cannot be reconstructed (opus:O04, opus:O05).",
                   ["son55:E009", "son55:E043", "son55:E044", "opus:O04", "opus:O05", "opus:O06"],
                   ["son55:E019", "sol:E11"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked and the cause pinned down. Binary judged "
                               "accuracy with LongMemEval-style prompts is appropriate, and judge swaps during "
                               "construction leave results stable. But the test-time judge is not validated, and Table 1 "
                               "compares item sets that differ: 400 for baselines vs a 500-item five-fold mean for "
                               "MetaMem (opus:O01). The headline wording overstates the gap (opus:O02, opus:O03). Not "
                               "1: same-fold Table 5 comparisons exist and point the same way.",
                               ["son55:E016", "son55:E036", "son55:E046", "son55:E050", "son55:E051", "opus:O01",
                                "opus:O02"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There are w/o-Evolution, w/o-Reflection and "
                             "apply-to-other-system controls, and a ShareGPT-built list. Missing: a static hand-written "
                             "guideline or template-only control (w/o Evolution is already +0.83 over LightMem on Qwen), "
                             "an optimisation-budget-matched baseline, and edit/filter ablations.",
                             ["son55:E013", "son55:E014", "son55:E021", "son55:E033", "son55:E034"],
                             ["son55:E040", "son55:E055", "opus:O03"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Test questions are disjoint from the 350+50 used "
                           "in each fold, the list is frozen at test, and a ShareGPT-built list also beats LightMem. Not "
                           "4: one benchmark and one memory constructor; checkpoint selection and the split behind the "
                           "non-monotone step curves are unstated (opus:O04, opus:O05). The existence of a 50-item "
                           "validation split keeps this above 2.",
                           ["son55:E010", "son55:E011", "son55:E021", "son55:E024", "sol:E06"],
                           ["son55:E019", "son55:E049", "opus:O05"]),
            "E.statistics": R("resolved", 2, "Opus sides with son55. Table 5 reports paired LightMem/MetaMem results "
                              "for all five folds and both backbones. Each fold uses an independently built meta-memory "
                              "on a disjoint 100-item test, and the losing fold (Llama fold 1, −3.1) is shown. That is "
                              "repeated evaluation with failures visible, which is A2 ladder level 2. Not 3: no "
                              "interval, seed or significance test; Tables 2/4/6 and Figure 5 are single runs.",
                              ["son55:E010", "son55:E035", "son55:E053", "sol:E14"], ["son55:E023"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Inference tokens/latency are reported on the same "
                        "device (Table 4). The offline construction cost (sampling, 235B judge, reflection, edit and "
                        "filter calls over 5 epochs) is excluded, and baselines get no optimisation budget.",
                        ["son55:E026", "son55:E038", "sol:E12"], ["son55:E025"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text plus the pinned page images (v3 package) read. In scope (system_method): a "
                  "non-weight guideline list is edited from judged outcomes, frozen and injected into a frozen answerer "
                  "on disjoint test folds. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Resolved by the v3 package: Figures 3–6 and prompt Figures 7–16 were read from the pinned "
                             "page images; figure readings are marked as such (opus:O05, opus:O06).",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "C03 tactic not executed (no schema/upstream parsing phase/category holdout); r10b convention. See "
                "rs_pattern.reason.", ["sol:E01", "son55:E039"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "H01 in both seats (edit operations with consolidation). H00 is kept (sol): the lesson source is a "
                "contrast of successful vs unsuccessful attempts over k=5 samples, and the w/o-Self-Reflection "
                "ablation targets that step.", ["sol:E03", "son55:E041", "son55:E013"], NOSCORE),
            XC(p, "local:2602.11182-2", "son55", "unknown",
               "A4 collision: sol's local-2 (statistics) vs son55's local-2 (checkpoint/split of the step curves). "
               "Final local-2 = checkpoint question. It stays unknown: the rule is unstated, and whether test folds "
               "were used for selection cannot be determined (opus:O04, opus:O05). sol's statistics check moves to "
               "local-7.", ["son55:E049", "opus:O04", "opus:O05"]),
            XC(p, "local:2602.11182-3", "son55", "unmet",
               "A4 collision: sol's local-3 (cost) vs son55's local-3 (table inconsistency). Final local-3 = table "
               "inconsistency, unmet. Verified and extended with exact denominators (opus:O01, opus:O02). sol's cost "
               "check moves to local-4.", ["son55:E050", "son55:E051", "opus:O01", "opus:O02"]),
            XC(p, "local:2602.11182-4", "son55", "unmet",
               "Cost question (son55 local-4 = sol local-3). Unmet: the main extra cost, construction, is entirely "
               "unreported. sol's 'partial' credited inference cost only.", ["son55:E025", "son55:E038", "sol:E12"]),
            XC(p, "local:2602.11182-5", "son55", "unmet",
               "Verified: construction needs ground-truth answers per question, and no label-free or online "
               "experiment exists.", ["son55:E007", "son55:E027"]),
            XC(p, "local:2602.11182-6", "son55", "unknown",
               "Verified: the baseline answer template is unspecified while MetaMem's (Figure 12) adds a 5-step "
               "procedure, so a template effect cannot be excluded or confirmed.", ["son55:E040", "son55:E055"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: evolution-off and reflection-off exist; there is no static-guideline or template-only "
               "control.", ["son55:E013", "son55:E033"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap/contamination analysis.", ["son55:E010"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: Full Text and RAG are compared; there is no hand-written-guideline baseline at equal budget.",
               ["son55:E034"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: only reflection and evolution are ablated.", ["son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: two backbones and three systems, but one benchmark and one constructor.",
               ["son55:E015", "son55:E021"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: judge sensitivity, data scale and ID vs OOD are reported.",
               ["son55:E036", "son55:E022", "son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: the loop is generic, but the learned object (a reader policy for fragmented memory) is "
               "specific to this vertical.", ["son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/F4", "son55", "unknown",
               "Kept as son55 recorded it (not applicable: units are injected globally with no applicability "
               "condition).", ["son55:E039"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step3", "son55", "met",
               "Verified: disjoint folds and an OOD-built list test transfer beyond the source instances.",
               ["son55:E011", "son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "partial",
               "Folds separate the lesson-producing and test streams, but checkpoint selection is unstated "
               "(opus:O04, opus:O05), so the separation is not fully demonstrated. sol's 'met' did not weigh the "
               "missing selection rule.", ["son55:E011", "opus:O04", "opus:O05"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step5", "son55", "partial",
               "Verified: there is a store-off-like control but no equal-budget baseline.", ["son55:E013"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01-step2", "son55", "partial",
               "Verified: edits derive from judged outcomes but are not authorised by an outcome test.",
               ["son55:E007", "opus:O06"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "sol", "met",
               "S1 asks whether a specific previously fixed thing is made learnable: how the answerer reads retrieved "
               "memory. It is, and the frozen-weights framing is background. son55's 'partial' was about neighbour "
               "coverage, which is G's question.", ["sol:E01", "son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: ground-truth correctness via the judge decides what becomes a lesson.", ["son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Verified: add/update/delete and consolidation exist; there is no cap/forgetting, and quality degrades "
               "after step 5.", ["son55:E043", "son55:E019"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
               "The card counts 'quality filters' as a gate. Figure 15's Quality Control rules (opus:O06) are a "
               "prompt-level filter on what survives, which is partial; there is no outcome test. son55's 'unmet' "
               "missed this filter.", ["opus:O06", "sol:E04"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Verified: only whole-list on/off, with no per-unit counterfactual.", ["son55:E013"]),
            XC(p, "rsi:evidence_gated_retention/S3", "son55", "unmet",
               "Verified: degradation after step 5 is observed but not governed.", ["son55:E019"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2,
                "See ratings.X: unconditional retention, no rollback or checkpoint rule, observed post-step-5 "
                "degradation, and an unreconcilable step count. sol's 3 credited the readable prompts, which make the "
                "chain reconstructible but not the retention conditions.",
                ["son55:E019", "opus:O04", "opus:O05", "opus:O06"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", 2,
                "See ratings.E.statistics: paired per-fold results over five independently built meta-memories, with "
                "the losing fold shown, meet A2 level 2. sol's 1 treated folds as a single run.",
                ["son55:E035", "son55:E053"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text, then pages 6–8, 12–13 and 16–19 before opening "
                                                   "the a3 seats. Initial view: in scope (frozen guideline list on "
                                                   "disjoint folds). G 2, M 2–3, X 2 (no gate; post-step-5 decline), "
                                                   "Em 1–2 (Table 1 denominators 400 vs 500, LightMem 67.50 vs 65.86), "
                                                   "Ec 2, Eh 2–3, Es 1–2 (per-fold table), E.cost 1–2.",
            "integrity_checks": "Both seats a3 on 2602.11182v2 with the v3 package (input_hash b3c38007…, text sha "
                                "f6875b22…, 20 page shas match the pages manifest); canonical seat hashes equal "
                                "conflicts.json; a1 records not opened.",
            "core_claim_check": "Strongest supported claim: on LongMemEval with two backbones, a frozen ~25-unit "
                                "guideline list learned from 350 labelled questions per fold gives +3.0 to +6.1 over "
                                "same-fold LightMem (Table 5). The 'over 3.6%' wording is a two-backbone mean, and the "
                                "Table 1 baselines use a different item set. 'Retained' is warranted.",
            "rating_agreement": "G, M, Em, Ec, Eh, Ecost agree and were re-checked (Em cause pinned with exact "
                                "denominators); X and Es resolved to son55. Final 56.25.",
        },
    }
    return S
