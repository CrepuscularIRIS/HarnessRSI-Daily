"""Opus rulings for r12b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2603.15255 SAGE and 2603.15957 GASP: out_of_scope confirmed independently (A3). In SAGE, Challenger, Planner, "
        "Solver and Critic share one backbone, and all four are jointly LoRA-updated with Task-Relative REINFORCE++. "
        "In GASP, teacher and student share parameters and 'all updates are applied to the same weights'. The "
        "generated question pools are RL training data, not a retained harness component. Identification follows "
        "sol (C08 + H22, the run convention for proposer–solver co-training: r05b, r07b, r09b, r11a). evidence_level "
        "and claim_support are null, the canonical out_of_scope value; sol had written task/scoped.",
        "2603.16060 ARISE (seat Δ11.25): final 43.75, below both seats (46.25 / 57.5). X, E.measurement and E.cost go "
        "to sol (2/2/2) and E.holdout to son55 (2). Shared correction on M (2 → 1): the paper's own selection rule "
        "gives one skill per query to all G rollouts (§3.2 Phase II; App. A.2 step 2), and the confidence gate is a "
        "query-level test (Eq. 7). So R=2 and R=1 never coexist in a group: groups are {0,1} or {0,2}, and Eq. 5's "
        "mean/std normalisation is scale-invariant. The hierarchical reward, called 'the primary driver of skill "
        "adoption', therefore cannot change the GRPO advantages as described, and the binary-reward ablation's "
        "reported −1.7 to −2.3 points and 73%→31% utilisation drop cannot follow from the written algorithm. With "
        "son55's finding that Eq. 6 gives selection/summary tokens no advantage, two of the three load-bearing "
        "claims are refuted by the paper's own equations. X=2 rests on separate defects (A2): new skills enter with "
        "u=0 and are the eviction target while selected skills keep u>0; 24 vs 5 seed skills; an eval-time library "
        "state that is not stated explicitly. E.measurement=2 follows the table-inconsistency cap (r09b, r11a "
        "ReCreate): the Table 2 full row (AIME25 49.1, Omni 28.0) differs from Table 1 (48.3, 26.8), and the 'every "
        "benchmark' text is false in 3 cells. RS → C03 and evidence_level retained (run convention, r08a EvolveR). "
        "Domain → H00 + H28; H01 and H26 are rejected.",
        "2603.17187 MetaClaw (Δ3.75): final 41.25. M → son55 2: the meta-learning framing is not carried by any "
        "objective, mutual reinforcement is only asserted, and the RL-buffer rules conflict. Sec. 3.3 says the buffer "
        "accumulates across generations g'≤g*, Sec. 3.4 and Alg. 1 line 16 flush everything ≤g on each skill update, "
        "and Alg. 1 lines 7–10 admit only non-failure trajectories. E.cost → son55 1: the '5-day training run' is a "
        "wall-clock disclosure, the same level as r05a 'Agents of Change' (60 h wall-clock = 1). RS → "
        "adapt_via_conditioning/C03 primary with heterogeneous_decomposition supporting. Noted: the text says "
        "skills-only leaves Part I completion 'unchanged for both models', but Table 1 shows GPT-5.2 at 14.7→17.1.",
        "2603.17613 VeriAgent (Δ2.5): final 38.75. E.measurement → son55 1, extended by an Opus recomputation of Table 2 "
        "(44 designs; valid designs 44/38/32/41). The reported 'Geometric Mean' row reproduces only for the Original "
        "column. Recomputed over each column's valid designs: ChipSeek-R1 0.310/92.9/1.80e-5 vs reported "
        "0.329/112/1.93e-5; gpt-4o 0.345/129.3/5.85e-6 vs 0.362/122/6.89e-6; gemini3 0.286/103.5/5.31e-6 vs "
        "0.294/109/5.72e-6. Normalising per design against Original, as the text says, gives geometric means of "
        "2.49/9.44/9.99, not 2.196/5.119/8.539; the reported scores match the ratio of the reported column GMs. Power "
        "drops 17× at identical delay/area (comparator_3bit 0.1/11.704) and 1579× for div_16bit. claim_support → "
        "sol 'scoped'. RS → son55 (C25 primary, adapt_via_conditioning supporting); domain H00 + H01.",
        "A4 hygiene: hidden local-ID collisions (the same local:<key>-n used for different questions) in 2603.16060, "
        "2603.17187 and 2603.17613 were renumbered. Same-question pairs under different IDs (sol 'rsi:…/H28' vs son55 "
        "'rsi:…/H28-step5'; sol 'rsi:…/H01' vs son55 'rsi:…/H01-step5') were merged into the step-level ID.",
        "Figure dependence: ARISE Figures 1/3, MetaClaw Figures 2/3 and VeriAgent Figure 2 (win rates) carry their "
        "values only as images. Ratings rely on captions, body text and tables. No figure value was invented.",
        "Not used for scoring: whether DeepScaleR's actual composition includes Omni-MATH. The pinned ARISE text lists "
        "only 'AMC, AIME, MATH, and OlympiadBench', and checking it needs material outside the input package. It is "
        "recorded as an unresolved overlap question, and E.holdout already reflects the missing overlap audit.",
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

    def pmap(s, p, idx, **upd):
        m = prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][idx]), s)
        m.update(upd)
        return m

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def moved(new_id):
        return {"note": f"A4: renumbered/merged into {new_id} (same question; see resolutions)."}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                       "precedent r05b–r11a).",
                "claim_support": None,
                "claim_support_note": note,
                "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_spec(p, a3, opus, sol_exp_reasons, review, assess_note):
        rec = {
            "base": "sol",
            "paper_update": {"paper_id": p, "claim_type": "component_training"},
            "opus_evidence": opus,
            "rs_pattern": prefix(copy.deepcopy(seat("sol", p)["rs_pattern"]), "sol") | {
                "reason": "Informational (out_of_scope). Opus confirms sol: the generator proposes verifiable tasks, the "
                          "solver's pass rate steers the generator, a filter (critic score / validity checks) admits "
                          "tasks, and the shared policy is retrained. This is C08's generate → steer → filter → "
                          "retrain loop, the run convention for proposer–solver co-training (r05b R-Zero, r07b Search "
                          "Self-play/SPICE, r09b GenEnv, r11a Dr. Zero). son55 skipped identification. The run records "
                          "identification for excluded rows, so the empty pattern is replaced. No score effect."},
            "domain_pattern": {"namespace": "rsi",
                               "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22",
                                                  fit="high (informational; out_of_scope weight-level member)")],
                               "unassigned": [],
                               "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
            "pattern_mapping": [pmap("sol", p, 0)],
            "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
            "claims": lambda c: c,
            "assessment": oos_assessment(assess_note),
            "ratings": {k: R("unknown", None, a3) for k in KEYS},
            "status": "out_of_scope", "reason": a3,
            "aggregate_status": "accepted_final",
            "a3": "none (both seats out_of_scope; confirmed independently)",
            "resolutions": [
                res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                    "The out_of_scope value is null. The task/retained/improver ladder in EVIDENCE.md grades retained "
                    "non-weight changes, and this paper has none (precedent r05b–r11a).",
                    ["opus:O01"], "none (evidence_level is not scored; row is unscored)"),
                res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
                    "Claim support is not assessed for an excluded row; null is canonical (precedent r09b GenEnv, r11a).",
                    ["opus:O01"], "none"),
                res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                    "Identification is still recorded for excluded rows (run convention). The generate/steer/filter/"
                    "retrain loop is C08's operation (see rs_pattern.reason).", ["opus:O01", "opus:O02"], NOSCORE),
                res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["self_supervised_signal_engineering", "C08"]],
                    "Follows primary; C08 is the closed-loop variant used for every proposer–solver row in this run.",
                    ["opus:O01", "opus:O02"], NOSCORE),
                res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["self_generate_the_curriculum", "H22"]],
                    "Informational H22 (proposer co-trained against a solver with a difficulty reward). As in r09b GenEnv "
                    "and r11a, an H22 match on a weight-level member does not bring the paper into scope.",
                    ["opus:O01", "opus:O02"], NOSCORE),
            ] + [XC(p, eid, "sol", st, why, ev) for eid, st, why, ev in sol_exp_reasons],
            "shared_error_corrections": [],
            "aggregate_review": review,
        }
        return rec

    # =========================================================== 2603.15255 SAGE (both out_of_scope)
    p = "2603.15255"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "Challenger, Planner, Solver and Critic are role prompts on one shared backbone, and 'all agents are jointly "
          "updated using Task-Relative REINFORCE++' (opus:O01) with LoRA (opus:O02). The verified question pool that "
          "'expands the dataset' (opus:O03) is RL training data. The evaluated product is the trained checkpoint; no "
          "prompt, tool, workflow, memory or evaluator is edited and retained for inference. Not scored; null is not "
          "a zero-quality rating.")
    S[p] = oos_spec(
        p, a3,
        [opus_ev(p, "O01", "all agents are jointly updated using Task-Relative REINFORCE++ with per-role advantage normalization.",
                 "Figure 2 caption (training pipeline)", "All four roles improve by a shared weight update."),
         opus_ev(p, "O02", "All agents are initialized from their corresponding base models. We apply LoRA",
                 "§5 Experimental setup (implementation details)", "The persisted change is LoRA weights."),
         opus_ev(p, "O03", "verified questions expand the dataset", "Figure 2 caption",
                 "The growing question pool is training data for the RL update, not a harness component read at test time.")],
        [("rsi:self_generate_the_curriculum/S1", "partial",
          "Informational. Generated verifiers are validated for parseability/executability and the Critic filters "
          "quality (α=0.7), but the generator itself writes the verifier and nothing audits its semantic correctness.",
          ["sol:E03"]),
         ("local:2603.15255-1", "met",
          "Informational. The A3 basis holds: joint RL/LoRA updates of one backbone, and the trained checkpoint is "
          "evaluated (opus:O01, opus:O02).", ["sol:E01", "opus:O01"])],
        {"initial_judgment_before_seat_scores": "Read the abstract, §3–4 (preliminaries, Challenger/Planner/Solver/Critic "
                                                "rewards, quality filter) and the implementation details first: the four "
                                                "roles share one backbone that is jointly RL/LoRA-updated → out_of_scope (A3).",
         "integrity_checks": "Both seats a1 on 2603.15255v2, material sha 6b050491…; canonical seat hashes equal "
                             "conflicts.json; both out_of_scope independently.",
         "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
         "rating_agreement": "All eight unknown in both seats; kept."},
        "Not assessed under this rubric; benchmark gains are author-reported results of RL-trained checkpoints.")

    # =========================================================== 2603.15957 GASP (both out_of_scope)
    p = "2603.15957"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: "
          "teacher and student share parameters and 'differ only by role prompting; all updates are applied to the same "
          "weights' (opus:O01). The teacher is rewarded on the student's pass rate (opus:O02), and the lemma/lift "
          "questions are RL training data. Goalposts, role prompts and the curriculum rules are fixed, and the novelty "
          "buffer is training infrastructure. The evaluated product is the trained checkpoint (LCB pass@k). Not "
          "scored; null is not a zero-quality rating.")
    S[p] = oos_spec(
        p, a3,
        [opus_ev(p, "O01", "and differ only by role prompting; all updates are applied to the same weights.",
                 "§3 Background: asymmetric self-play", "Teacher and student are one policy whose improvement is a weight update."),
         opus_ev(p, "O02", "The teacher is rewarded based on the student’s performance on its proposals",
                 "§3 Background: asymmetric self-play", "Difficulty-steered proposer reward, the H22 / C08 signal.")],
        [("rsi:self_generate_the_curriculum/S6", "partial",
          "Informational. The temporal split (training ≤2024.08, evaluation 2024.10–2025.02) avoids direct overlap, but "
          "sol records that LCB evaluation is also used to pick checkpoints.", ["sol:E03"]),
         ("local:2603.15957-1", "partial",
          "Informational. Per-iteration cost is disclosed as higher than AZR's, but 50 vs ~200 steps does not "
          "establish matched compute.", ["sol:E05"])],
        {"initial_judgment_before_seat_scores": "Read the abstract, §1, §3 (asymmetric self-play background), §4 "
                                                "(goalpost filtering, lemma/lift loop, Algorithm 1) first: shared "
                                                "teacher/student weights updated by Task-Relative REINFORCE++ → "
                                                "out_of_scope (A3).",
         "integrity_checks": "Both seats a1 on 2603.15957v1, material sha 021510b3…; canonical seat hashes equal "
                             "conflicts.json; both out_of_scope independently.",
         "core_claim_check": "A3 basis confirmed with opus:O01–O02.",
         "rating_agreement": "All eight unknown in both seats; kept."},
        "Not assessed under this rubric; LCB gains are author-reported results of RL-trained checkpoints.")

    # =========================================================== 2603.16060 ARISE (Δ11.25)
    p = "2603.16060"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "solutions conditioned on the augmented prompt", "§3.2 Phase II: Skill-Augmented GRPO",
                    "Phase II: the manager selects one skill (Eq. 3) and the worker generates all G solutions conditioned "
                    "on the same augmented prompt. Every rollout in a group therefore shares the same skill status."),
            opus_ev(p, "O02", "For each query, the manager scores all cache entries via Eq.", "Appendix A.2 step 2 (skill selection)",
                    "One skill (or none, if the gate rejects) per query, before the G solution rollouts (step 4)."),
            opus_ev(p, "O03", "Within a rollout group containing both", "§3.1 Hierarchical Reward",
                    "The authors' argument for the hierarchical reward assumes R=2 and R=1 trajectories coexist in a group."),
            opus_ev(p, "O04", "assigns trajectories with", "Appendix D.2 (Hierarchical Reward Details)",
                    "Opus inference from the paper's own Eqs. 5 and 7 and O01/O02. The gate is a query-level test "
                    "(max_k p_k ≥ δ), so each group is all-skill or all-no-skill, and rewards are {0,2} or {0,1}. "
                    "Eq. 5's (r−μ_G)/(σ_G+ϵ) is invariant to rescaling the rewards, so a {0,2} group gets the same "
                    "advantages as a {0,1} group. 'Both outcomes coexist in the same group' never occurs. The "
                    "hierarchical reward cannot change the policy gradient as described, and the EMA utilities it "
                    "feeds are only rescaled (rank-preserving). The binary-reward ablation's reported effect is "
                    "therefore unexplained by the written algorithm.", kind="our_inference"),
            opus_ev(p, "O05", "it is inserted into the cache with initial utility", "Appendix C.2 (Add)",
                    "New skills enter at u=0."),
            opus_ev(p, "O06", "the entry with the lowest utility is moved to the reservoir", "Appendix C.2 (Evict)",
                    "With a full cache of selected skills whose EMA utility is >0 (R≥0, positive whenever solved), a new "
                    "u=0 skill is the eviction target. Reservoir skills are never selected, so their utility never "
                    "updates (C.2 Update) and Load cannot promote them. Late-stage specialised skills (Table 8) are "
                    "hard to reconcile with this rule.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [],
            "matches": [smatch("son55", p, "adapt_via_conditioning",
                               reason="Opus confirms son55, which is also the run convention for co-evolving skill "
                                      "libraries under RL (r08a EvolveR → C03). A uniform 5-field JSON schema with a "
                                      "220-char cap is a canonical conditioning format (step 1). The policy is trained "
                                      "on SKILL:-prefixed prompts to read it (step 3). Steps 4–5 (category holdout, "
                                      "cheap-baseline isolation) are evaluation gaps, not identification failures. "
                                      "sol's generative_process_redesign is rejected: the paper does not liberate a "
                                      "conventionally fixed component of an iterative generative procedure; it "
                                      "retrieves conditioning text, and sol itself found no sub-card fit.")],
            "outside_taxonomy": False,
            "reason": "Skills retrieved by policy log-probability and prepended to the prompt condition inference without "
                      "per-task updates. That is adapt_via_conditioning/C03 with an RL upstream phase teaching the model "
                      "to read the schema.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [],
                           "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.16060-1"): "local:2603.16060-3",
                    ("son55", "local:2603.16060-3"): "local:2603.16060-1",
                    ("sol", "rsi:couple_context_and_weight_updates/H28"): "rsi:couple_context_and_weight_updates/H28-step5"},
            overrides={
                "local:2603.16060-1": {
                    "status": "partial",
                    "reason": "Opus: the same held-out/selection question in both seats (sol local-1, son55 local-3). "
                              "Training data (DeepScaleR) and the test sets are separated temporally. But the only "
                              "hyperparameter study is scored on AIME 2024, a reported test set, and each of the four "
                              "defaults sits at that sweep's peak; no validation split is described. The selection "
                              "protocol itself stays undisclosed (son55's 'unknown' part), and the OOD Omni-MATH claim "
                              "has no overlap audit.",
                    "note": "A4 collision fix: son55's local-1 (cost) moved to local-3; son55's local-3 merged here."},
                "local:2603.16060-3": {
                    "status": "partial",
                    "reason": "Opus: the same cost/budget question in both seats (sol local-3, son55 local-1). Token "
                              "overhead (+3.0%) and per-step wall-clock (+16.6%) are reported, but the 'same "
                              "computational budget' statement is contradicted by that overhead at an equal 2,000 "
                              "steps, and there is no equal-compute baseline.",
                    "note": "A4 collision fix: son55's local-1 merged here."},
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'unmet'). Plain fine-tuning on the same data (GRPO family) and "
                              "two external-retriever memory baselines (EvolveR/SimpleMem + GRPO) are present, so cheaper "
                              "alternatives are not wholly missing. But there is no in-system swap of log-prob selection "
                              "for an embedding retriever, and no equal-budget accounting."},
                "rsi:couple_context_and_weight_updates/H28-step5": {
                    "status": "partial",
                    "reason": "Opus (sol's 'H28' and son55's 'H28-step5' ask the same lever-ablation question). A "
                              "weights-only arm (GRPO family, same data and steps) and the coupled arm exist on held-out "
                              "benchmarks, plus a frozen-seed-library variant. The context-only arm (frozen policy with "
                              "an evolving library) and seeds are missing, so partial rather than unmet."},
                "rsi:couple_context_and_weight_updates/F5": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'unknown'). The adaptation stream (DeepScaleR training) is "
                              "declared separate from the reported benchmarks. App. A.3 lists only skill selection "
                              "(ε=0) at evaluation, with no O_{G+1} or library update. That the library is frozen is "
                              "implied, not stated."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O04"]), "C3", ["opus:O04", "opus:O01"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "The library evolved during training is retained and read at evaluation (son55:E012). "
                                   "The frozen-seed-library variant (w/o O_{G+1}) scores lower on held-out benchmarks. "
                                   "This is author-reported and confounded with re-training, so the retained label is "
                                   "kept at the run's convention level (r08a EvolveR) and is not a fixed-policy store-off "
                                   "result.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, author-reported gains of about 2–3 points over GRPO (1–1.5 over "
                                         "DAPO/GSPO on most cells) on AMC/AIME/Omni-MATH for two 4B-class models, from "
                                         "an RL-trained policy that reads a self-built skill library retained from "
                                         "training. The library-evolution and random-selection ablations point the "
                                         "same way. The hierarchical reward's claimed role is not supported as "
                                         "written (opus:O04), and end-to-end selection learning is not carried by Eq. 6.",
            "unresolved": [
                "Whether the implementation mixes skill/no-skill rollouts within a group (needed for the hierarchical "
                "reward to act), given the written per-query selection (opus:O01, opus:O02, opus:O04).",
                "Library vs reward-shaping vs extra-prompt attribution; no fixed-policy skill-off test.",
                "Table 2 full row vs Table 1; 24 vs 5 seed skills; 'every benchmark' text vs Table 1.",
                "Omni-MATH overlap with the DeepScaleR sources is unaudited; the pinned text lists only AMC/AIME/MATH/"
                "OlympiadBench as sources.",
                "Training-seed variance; nearest neighbours (SkillRL, SAGE-Wang) not tabulated."],
        },
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. 'External retriever, library updated independently of RL' is "
                   "a concrete limitation, and neighbours are named (EvolveR, SkillRL, SAGE-Wang). SkillRL is listed as a "
                   "baseline but absent from Table 1, and the decoupling is not shown to be the binding bottleneck.",
                   ["son55:E002", "son55:E003", "son55:E015", "son55:E016"], ["son55:E031"]),
            "M": R("resolved", 1, "Opus shared correction (both seats 2). The method has three load-bearing ideas. Two are "
                   "contradicted by the paper's own equations. (i) The hierarchical reward is said to give skill-augmented "
                   "correct rollouts a higher advantage than unaided correct ones in the same group (opus:O03). But "
                   "selection is one skill per query for all G rollouts (opus:O01, opus:O02), and the gate is "
                   "query-level, so groups are {0,1} or {0,2}. Eq. 5's normalisation is scale-invariant, so the reward "
                   "cannot act as described (opus:O04). (ii) 'The advantage propagates end-to-end through the selection "
                   "mechanism' is not carried by Eq. 6, which credits only worker tokens (son55:E004, son55:E005). What "
                   "remains is a plausible, concretely specified distil-and-retrieve chain (summary rollout from τ+, a "
                   "uniform schema, log-prob scoring). That is not 0, but the stated reasoning for the key operations is "
                   "directly refuted, so it falls below the 2 anchor.",
                   ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "son55:E004", "son55:E005"], ["son55:E010"]),
            "X": R("resolved", 2, "Opus sides with sol. The read path, write path, five operations, validation pipeline "
                   "and hyperparameters are given, but key conditions conflict. New skills enter at u=0 (opus:O05) and are "
                   "the eviction target once selected cache entries have positive EMA utility (opus:O06). Reservoir "
                   "skills are never selected or updated (sol:E11), so Load (sol:E05) cannot promote them, which sits "
                   "badly with the late-stage specialised skills of Table 8. The library is said to be 'frozen at 24 "
                   "seed skills' (sol:E02) against 5 seeds in Table 3/5 (son55:E023). The eval-time library state is "
                   "implied, not stated. son55's 3 credits reconstructibility without these contradictions.",
                   ["sol:E02", "sol:E05", "sol:E11", "son55:E007", "son55:E009", "opus:O05", "opus:O06"], ["son55:E012"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. The verifiers (exact match; official Omni-MATH symbolic "
                               "equivalence) are sound, and Table 1's subscripts and averages recompute exactly. But the "
                               "reported results disagree with each other. The Table 2 full row gives AIME25 49.1 and "
                               "Omni 28.0, against 48.3 and 26.8 in Table 1 (sol:E15, sol:E16). The text says ARISE "
                               "beats all baselines 'across every' benchmark and 'across all benchmarks', but GSPO wins "
                               "Qwen AIME25/Geometry and DAPO wins Phi AIME25 (son55:E033, son55:E032). Phi's Omni gain "
                               "is quoted as 1.9 against 2.0 in the table. Run convention caps table inconsistency at "
                               "2 (r09b, r11a ReCreate). son55's 3 treats these as slips that do not touch the metric, "
                               "but this item covers result credibility too.",
                               ["son55:E019", "sol:E04", "sol:E15", "sol:E16"], ["son55:E032", "son55:E033", "son55:E022"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There are relevant controls: four ablations "
                             "(binary reward, random selection, no O_{G+1}, no gate), a weights-only GRPO family under "
                             "the same data and steps, and two retriever-memory baselines. Limits: single runs, no "
                             "fixed-policy skill-off test, no equal-compute arm. The binary-reward ablation's reported "
                             "effect cannot follow from the written algorithm (opus:O04), so it does not show the "
                             "'primary driver' claim. That is recorded here without a further deduction, because the "
                             "defect is already counted under M (A2).",
                             ["son55:E021", "son55:E022", "son55:E027", "son55:E028", "son55:E014"], ["opus:O04", "son55:E013"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. Training (DeepScaleR) and test sets (AMC23, AIME24/25, "
                           "Omni-MATH) are separated, and evaluation reads a training-built library (son55:E012). Gaps: "
                           "the only hyperparameter study is scored on AIME 2024 with every default at the sweep's "
                           "peak and no validation split (son55:E024). The 'OOD' Omni-MATH claim has no overlap audit "
                           "(son55:E025, son55:E026). These leave the anchor-2 'key coverage gaps', but the main tables "
                           "are not built on the scored stream, unlike r11a's TTE (1). sol's 1 weighs AIME24 tuning as "
                           "if it contaminated all seven columns.",
                           ["son55:E017", "son55:E018", "son55:E012"], ["son55:E024", "son55:E025", "son55:E026", "sol:E08"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample counts and negative cells are reported, but "
                              "there is no std/CI or training-seed variation. The '32 independent runs' use greedy "
                              "decoding with ε=0, so they are not independent, and AIME gaps of 0.4–2.3 points are under "
                              "one problem.", ["son55:E019", "sol:E03"], ["son55:E020"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Cost reporting is genuine: per-step wall-clock with a "
                        "component breakdown (+16.6%) and token overhead (+3.0%) (son55:E027, son55:E028). But the paper "
                        "states all methods ran 'under the same computational budget' (son55:E013) while ARISE spends "
                        "~16.6% more per step over an equal 2,000 steps. There is no equal-wall-clock or equal-compute "
                        "comparison, and memory baselines' training costs are not given. son55's 3 would need budget "
                        "matching or a cost frontier.",
                        ["son55:E027", "son55:E028", "sol:E09"], ["son55:E013"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text including Appendices A–E read. In scope (A3): a non-weight JSON skill library "
                  "is built from execution feedback, retained across training and read at evaluation (App. A.3), even "
                  "though the policy is also RL-trained. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 1 and 3 (co-evolution and utilisation curves) are image-only; used only as described "
                             "in §4.3 and App. E.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "The training-built library is retained and read at evaluation on separate benchmarks (son55:E012), and "
                "the frozen-seed-library variant scores lower. That meets the ladder's 'retained' at author-report "
                "level, as in the run convention for co-trained skill libraries (r08a EvolveR). The confound with "
                "re-training is recorded in the evidence_level_note. sol's 'task' would require the library's effect "
                "to be untraced, but it is traced, if weakly.",
                ["son55:E012", "son55:E022", "sol:E02"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "See rs_pattern.reason: retrieved conditioning text read by an RL-trained policy is C03 (run convention "
                "EvolveR). generative_process_redesign needs a conventionally fixed generative component to be freed, "
                "and the paper has none.", ["son55:E009", "son55:E012", "sol:E01"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", "C03"]],
                "Follows primary; C03's canonical schema (uniform JSON, 220-char cap) and upstream phase (Phase II RL on "
                "SKILL:-prefixed prompts) are executed.", ["son55:E009", "son55:E006"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"], ["couple_context_and_weight_updates", "H28"]],
                "H28 is kept (both seats). For the parent abstract_experience_into_guidance, H00 fits: skills are "
                "distilled from the group's positive-advantage rollouts into an appended store. H01 is rejected: its "
                "signature is an LLM curator choosing edits over existing entries, while ARISE's five operations are "
                "fixed utility rules that never edit or merge content (son55's own S4 check). H26 is rejected: the "
                "skill-writing O_{G+1} rollout gets no advantage in Eq. 6, so the curator is not trained on downstream "
                "utility (son55's own S2 'unmet', fit 'low').", ["sol:E01", "son55:E005", "son55:E007"], NOSCORE),
            XC(p, "local:2603.16060-3", "sol", "partial",
               "A4 ID collision: sol's local-3 is cost and son55's local-3 is AIME24 selection. Final local-3 is cost, "
               "partial, the same as son55's own cost check (its local-1, also partial). son55's local-3 question moved "
               "to local-1 (selection/held-out, partial; the undisclosed selection protocol is noted there).",
               ["son55:E027", "son55:E028", "son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified. Random-selection and frozen-seed-library ablations exist (single run), but there is no "
               "skill-off-at-inference test of the trained policy.", ["son55:E021", "son55:E022"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: there is no overlap analysis between the DeepScaleR sources and the 'OOD' Omni-MATH set.",
               ["son55:E025", "son55:E026"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "revised", "partial",
               "Plain fine-tuning (GRPO family) and retriever memory baselines (EvolveR/SimpleMem + GRPO) are cheaper "
               "alternatives that are present. There is no in-system retriever swap and no budget matching, so partial, "
               "not unmet.", ["son55:E014", "son55:E015"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: gate/ε/cache/warm-up sensitivity is given, but only on AIME24 and with no library-coverage analysis.",
               ["son55:E024"]),
            XC(p, "rsi:abstract_experience_into_guidance/F4", "son55", "partial",
               "Verified: selection is log-prob retrieval scoring, and learning-by-gradient is asserted (son55:E004) but "
               "not carried by Eq. 6 (son55:E005).", ["son55:E004", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Verified: Add/Update(utility)/Evict/Load/Delete with caps exist; there is no content merge, conflict "
               "handling or dedup.", ["son55:E007", "son55:E008"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S2", "son55", "unmet",
               "Kept as a check question although H26 is not matched. Verified: selection and summary tokens receive no "
               "advantage in Eq. 6.", ["son55:E005", "son55:E006"]),
            XC(p, "rsi:couple_context_and_weight_updates/F2", "son55", "met",
               "Verified: the failure is avoided. The policy is trained on SKILL:-prefixed prompts, so the library is a "
               "trained-on input, not a recall bank beside it.", ["son55:E006"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "revised", "partial",
               "son55's 'unknown' is narrowed by App. A.3: the adaptation stream (DeepScaleR) is declared separate, and "
               "the evaluation pipeline lists only selection with ε=0, with no generation or library update. Freezing "
               "is implied but not stated, so partial (not met).", ["son55:E012"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28", "sol",
               {"moved_to": "rsi:couple_context_and_weight_updates/H28-step5", "status": "partial"},
               "sol's tactic-level 'H28' check is the lever-ablation question, which son55 asked as H28-step5. Merged "
               "there. sol's 'partial' is verified (a weights-only arm exists; the context-only arm is missing).",
               ["sol:E14", "sol:E02"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step1", "son55", "unmet",
               "Verified: neither a context-only plateau nor weights-only sample inefficiency is demonstrated; the "
               "motivation is the retriever/RL decoupling.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step5", "revised", "partial",
               "Same question as sol's 'H28' (partial). There is a weights-only arm (GRPO family, same data and steps), "
               "a coupled arm and a frozen-library variant on held-out benchmarks. The context-only arm and seeds are "
               "missing, so partial, not son55's unmet.", ["son55:E021", "son55:E022", "sol:E14"]),
            XC(p, "rsi:couple_context_and_weight_updates/S2", "son55", "partial",
               "Verified: declarative skills vs procedural policy are argued, but not separated experimentally.",
               ["son55:E021", "son55:E022"]),
            XC(p, "rsi:couple_context_and_weight_updates/S3", "son55", "partial",
               "Verified: the policy is trained to read SKILL:-prefixed prompts, but the library is revised only from "
               "successes (τ+), not from diagnosed failures.", ["son55:E007", "son55:E012"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Kept as a check question. Verified: eviction and loading use a raw reward EMA with no memory-on/off "
               "counterfactual, and the authors themselves say high utility may only track easy problems.",
               ["son55:E010", "son55:E011"]),
            res("ratings.X", *C(p, "ratings.X"), "sol", 2,
                "See ratings.X. The admission/eviction rules trap new u=0 skills (opus:O05, opus:O06; sol:E05, sol:E11), "
                "and 24 vs 5 seeds conflict. These are 'key conditions unclear/conflicting' (anchor 2), so not 3.",
                ["opus:O05", "opus:O06", "sol:E02", "sol:E11"], "−5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement. The Table 1 vs Table 2 full rows and the text vs table (3 cells) conflict; "
                "run convention caps this at 2.", ["sol:E15", "sol:E16", "son55:E033"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 2,
                "See ratings.E.holdout. The temporal separation and a training-built library read at test time hold; "
                "AIME24 tuning and the unaudited OOD claim are coverage gaps (anchor 2), not a compromised main "
                "evaluation.", ["son55:E012", "son55:E024", "son55:E025"], "+2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 2,
                "See ratings.E.cost. Cost is transparent, but the 'same computational budget' claim is contradicted by "
                "+16.6% per step, and there is no budget-matched comparison.", ["son55:E013", "son55:E028", "sol:E09"],
                "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.M", "sol_value": 2, "son55_value": 2, "final_value": 1,
             "reason": "Both seats missed that the hierarchical reward is inert under the paper's own selection rule. The "
                       "rule gives one skill per query to all G rollouts (opus:O01, opus:O02), with a query-level gate "
                       "(Eq. 7). So skill-aided and unaided correct rollouts never share a group, and Eq. 5's group "
                       "normalisation makes {0,2} and {0,1} groups identical (opus:O04). The authors' central rationale "
                       "(opus:O03) is therefore refuted by their own equations. Combined with son55's own finding that "
                       "Eq. 6 does not credit selection, M falls below the 2 anchor.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "son55:E005"],
             "score_impact": "−5.0 vs both seats (20×1/4)"},
            {"field_path": "ratings.E.causality.reason", "sol_value": "2 (binary-reward ablation read as evidence)",
             "son55_value": "2 (binary-reward ablation read as evidence)", "final_value": 2,
             "reason": "Shared omission, no rating change (A2: the defect is counted under M). The binary-reward "
                       "ablation's −1.7 to −2.3 points and 73%→31% utilisation drop (sol:E14) cannot come from the "
                       "described algorithm, so the ablation does not support 'the hierarchical signal is the primary "
                       "driver'.", "evidence_ids": ["sol:E14", "opus:O04"], "score_impact": "none"},
            {"field_path": "expectations[local:2603.16060-1].id", "sol_value": "local-1 = held-out/AIME24 (partial)",
             "son55_value": "local-1 = cost (partial)", "final_value": "local-1 = held-out/selection; local-3 = cost",
             "reason": "A4 hidden ID collision: both seats used local-1 for different questions with the same status, so "
                       "the mechanical diff missed it. Renumbered.", "evidence_ids": ["sol:E08", "son55:E013"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–5 and Appendices A–E first. Initial view: in scope (the "
                                                   "library is retained and read at evaluation). Table 1 is internally "
                                                   "consistent, but the text overclaims (3 cells), Table 2's full row "
                                                   "differs and seeds are 5 vs 24. The hyperparameter sweep is on "
                                                   "AIME24. While reading A.2/§3.2 I derived that per-query selection "
                                                   "plus group-std normalisation makes the hierarchical reward inert "
                                                   "(M ≤ 1–2). G 2, X 2, Em 2, Ec 2, Eh 1–2, Es 1, Ecost 2–3.",
            "integrity_checks": "Both seats a1 on 2603.16060v2, material sha 666e62b4…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both completed 15+31 identification.",
            "core_claim_check": "The strongest supported claim is single-run 2–3 point gains over GRPO with a retained "
                                "library. The reward-mechanism and end-to-end-selection claims are not supported as "
                                "written. 'Retained' is kept at author-report level.",
            "rating_agreement": "G, Ec, Es agree and were re-checked. M has a shared correction (1). X/Em/Ecost → sol; "
                                "Eh → son55.",
        },
    }

    # =========================================================== 2603.17187 MetaClaw (Δ3.75)
    p = "2603.17187"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "On Part I, MetaClaw (Skills) leaves task completion rates unchanged for both models",
                    "§4.2 'The full pipeline unlocks end-to-end task completion'",
                    "Text vs Table 1: GPT-5.2 Part I completion goes 14.7→17.1 under Skills, so it is not unchanged for "
                    "both models (only Kimi stays at 2.0)."),
            opus_ev(p, "O02", "This means policy optimization naturally lags behind skill-driven adaptation by days or longer",
                    "§3.3", "The RL buffer is meant to span several skill generations, which conflicts with flushing "
                            "every sample with version ≤g on each skill update (§3.4, Alg. 1 line 16)."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["heterogeneous_decomposition"],
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", role="primary",
                       reason="Opus: primary per son55 and the run convention for retained skill libraries (r01a ExpeL, "
                              "r08a EvolveR). Failure-distilled skills retrieved into the system prompt condition "
                              "inference without parameter updates. Sub-card C03 per sol: skills share one Claude-skill "
                              "schema, and the Full arm runs an upstream RL phase on trajectories collected under skill "
                              "conditioning (step 3). The missing category holdout and cheap baseline (steps 4–5) are "
                              "evaluation gaps, not identification failures; this matches ARISE in this batch."),
                smatch("son55", p, "heterogeneous_decomposition", role="supporting",
                       reason="Supporting, as both seats identified it. Trajectories are partitioned by skill-generation "
                              "version into support (→ skill evolver) and query (→ RL) data, and adaptation is split by "
                              "timescale (skills now, weights in idle windows). Sub null: C04's tactic does not fit. Not "
                              "primary, because the in-scope retained object is the conditioning library and no "
                              "uniform-treatment ablation exists."),
            ],
            "outside_taxonomy": False,
            "reason": "adapt_via_conditioning/C03 primary (skill library as conditioning, RL-trained reader in the Full "
                      "arm); heterogeneous_decomposition supporting (support/query partition and two timescales).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]), "son55"),
        "pattern_mapping": [pmap("son55", p, 0, rs_sub="C03"), pmap("son55", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.17187-1"): "local:2603.17187-5",
                    ("son55", "local:2603.17187-3"): "local:2603.17187-6",
                    ("son55", "local:2603.17187-4"): "local:2603.17187-3",
                    ("sol", "rsi:couple_context_and_weight_updates/H28"): "rsi:couple_context_and_weight_updates/H28-step5"},
            overrides={
                "local:2603.17187-3": {
                    "status": "unmet",
                    "reason": "Opus: the same cost question in both seats (sol local-3, son55 local-4). Zero downtime is "
                              "an architectural assertion; there is no throughput, interruption, return-latency, "
                              "API/PRM/evolver or LoRA cost measurement.",
                    "note": "A4 collision fix: son55's local-4 merged here; son55's local-3 (buffer semantics) moved to local-6."},
                "local:2603.17187-6": {
                    "status": "unmet",
                    "reason": "Opus (revised from son55 'unknown'). The question is whether the RL-buffer rule is "
                              "specified consistently, and the text answers it negatively. §3.3 accumulates across "
                              "generations g'≤g* (son55:E013, opus:O02), §3.4/Alg. 1 line 16 flush ≤g on every skill "
                              "update (son55:E014), and Alg. 1 lines 7–10 admit only non-failure trajectories "
                              "(son55:E015, son55:E016). Which rule was implemented remains unknown; the specification "
                              "is self-contradictory.",
                    "note": "A4: son55's local-3 renumbered."},
                "local:2603.17187-5": {"note": "A4: son55's local-1 (statistics) renumbered to avoid collision with sol's local-1 (holdout)."},
                "rsi:couple_context_and_weight_updates/H28-step5": {
                    "status": "partial",
                    "reason": "Opus (sol's 'H28' and son55's 'H28-step5' ask the same question). A context-only arm "
                              "(Skills) and a coupled arm (Full) exist; the weights-only arm, seeds and a clean split are "
                              "missing. Two of three arms make it partial, not unmet."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01"]),
        "assessment": prefix(copy.deepcopy(seat("son55", p)["assessment"]), "son55") | {
            "evidence_note": "Opus: 'retained' as in both seats. Skills distilled on earlier days are reused on later "
                             "days of the same stream (e.g., a Day 2 skill used on Day 19), and the same-backbone "
                             "skills-on/off toggle isolates the skill arm. This is narrow: online stream, no held-out "
                             "stream, single runs."},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static skill libraries and stale RL rewards after skill "
                   "changes are concrete gaps, but 'no existing system unifies' is untested, and co-evolution neighbours "
                   "(EvolveR, SkillRL-type) are not compared.", ["son55:E002", "son55:E003", "son55:E004", "sol:E02"]),
            "M": R("resolved", 2, "Opus sides with son55. The two-timescale design and the support/query rationale are "
                   "coherent and responsive. The 'meta-learning' claim, that θ is trained to become better at adapting, "
                   "is not carried by any objective: the evolver is a fixed prompt, and Eq. 4 is ordinary RL on "
                   "skill-conditioned rollouts. 'Mutually reinforcing' is asserted only (son55:E027). The buffer "
                   "rationale is internally inconsistent (son55:E013, son55:E014, opus:O02). sol's 3 credits interface "
                   "clarity, which is X's question.",
                   ["son55:E005", "son55:E011", "son55:E014"], ["son55:E013", "son55:E016", "son55:E027", "opus:O02"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1, versioning, OMLS signals, the evolver prompt and "
                   "the injection format are given. k, the embedder, the failure threshold, the evolver model and the PRM "
                   "are unspecified. The library is add-only with no gate or rollback. Buffer semantics conflict across "
                   "§3.3/§3.4/Alg. 1.",
                   ["son55:E005", "son55:E010", "son55:E014", "son55:E017", "sol:E13"], ["son55:E013", "son55:E016"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Deterministic checkers and a stated multi-choice "
                               "scoring rule exist, but the benchmark is self-authored with rule-revealing feedback, the "
                               "RL reward is a learned PRM, and the AutoResearchClaw composite is an author-defined "
                               "process metric. Added: the text says skills-only leaves Part I completion 'unchanged for "
                               "both models', while Table 1 has GPT-5.2 14.7→17.1 (opus:O01). Within the cap.",
                               ["son55:E019", "son55:E030", "sol:E05"], ["son55:E020", "son55:E012", "opus:O01"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Skills-on/off with identical prompts and tools "
                             "isolates the skill arm. There is no weights-only arm, no versioning/OMLS/retrieval "
                             "ablation and no raw-trajectory memory baseline, and Full is one run on one model, so the "
                             "coupling claim is not isolated.",
                             ["son55:E024", "sol:E07"], ["son55:E022", "son55:E031", "son55:E027"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The learning and reporting streams coincide with no "
                           "declared split, and the per-round feedback states the hidden rules. The second domain reuses "
                           "one topic across runs. This is an in-claim online setting (cf. r11a TTE = 1), so not 0.",
                           ["son55:E021", "sol:E05"], ["son55:E020", "son55:E028"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): 346/588-question denominators and negative cells "
                              "(Kimi Part I completion 2.0→2.0; multi-choice decline under Full) are reported, but there "
                              "are no seeds, variance or tests, and Full is a single run.",
                              ["son55:E026", "sol:E09"], ["son55:E022"]),
            "E.cost": R("resolved", 1, "Opus sides with son55. The only quantitative resource disclosure is the '5-day "
                        "training run' (sol:E07). There are no GPU hours, API/PRM/evolver calls, prompt-token overhead "
                        "or interruption measurements, and zero downtime is architectural. A wall-clock disclosure "
                        "without totals rates 1 under run precedent (r05a 'Agents of Change': 60 h wall-clock = 1). "
                        "not_reported would require no cost-relevant figure at all.",
                        ["sol:E07", "son55:E008", "son55:E022"], ["sol:E04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text including Appendix A prompts/templates read. In scope (A3): a failure-distilled, "
                  "non-weight skill library is retained and injected into later tasks; parallel LoRA RL does not "
                  "remove the harness component from evaluation. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 2–3 (per-day and per-task-type curves) are image-only; used only as described in §4.3.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "The retained, in-scope object is the conditioning library; primary follows the run convention for "
                "skill libraries. heterogeneous_decomposition is kept as supporting (both seats identified it).",
                ["son55:E009", "son55:E010", "son55:E024"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", "C03"], ["heterogeneous_decomposition", None]],
                "Both seats list the same two main cards. Sub C03 is taken from sol: one skill schema plus an RL upstream "
                "phase on skill-conditioned rollouts, consistent with ARISE in this batch. Roles are taken from son55 "
                "(adapt primary). Sub null for heterogeneous_decomposition as in both seats.",
                ["son55:E013", "sol:E01", "sol:E03"], NOSCORE),
            XC(p, "local:2603.17187-3", "sol", "unmet",
               "A4 ID collision: sol's local-3 is zero-downtime/cost and son55's local-3 is buffer semantics. Final local-3 "
               "= cost, unmet, matching son55's own cost check (its local-4, unmet). son55's buffer question moved to "
               "local-6 (unmet; see expectations).", ["sol:E04", "sol:E07", "son55:E008"]),
            XC(p, "local:2603.17187-4", "sol", "partial",
               "A4 ID collision: sol's local-4 is narrow retained/transfer and son55's local-4 is cost (merged into local-3). "
               "Final local-4 = sol's question. Partial verified: the Day 2→Day 19 skill reuse supports a narrow retained "
               "effect, and the second domain regenerates skills on the same topic rather than transferring frozen skills.",
               ["sol:E08", "sol:E11", "sol:E12"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "Verified: skills-on vs skills-off with the same backbone, prompts and tools isolates the conditioning arm.",
               ["son55:E024", "son55:E029"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: the feedback states the hidden rules, and there is no overlap or held-out stream analysis.",
               ["son55:E020", "son55:E021"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: the motivating claim that raw-trajectory memory is verbose is never tested against a "
               "raw-trajectory or Reflexion-type baseline.", ["son55:E004"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: AutoResearchClaw is a second domain, but skills-only, one topic, one A/B.",
               ["son55:E028", "son55:E029"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "son55", "unmet",
               "Verified: there is no versioning-off variant that mixes support and query data.", ["son55:E003", "son55:E014"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "unmet",
               "Verified: the stale-reward harm is described but never measured.", ["son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "unmet",
               "Verified: the evolver prompt shows only failed conversations, with no success contrast.", ["son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Verified: S_{g+1} = S_g ∪ ΔS is add-only, and 'do NOT duplicate' is a prompt instruction, not "
               "consolidation or forgetting.", ["son55:E007", "sol:E13"]),
            XC(p, "rsi:couple_context_and_weight_updates/F3", "son55", "partial",
               "Verified: version stamps are the only shared interface, and mutual reinforcement is asserted without a "
               "test.", ["son55:E014", "son55:E027"]),
            XC(p, "rsi:couple_context_and_weight_updates/F4", "son55", "unknown",
               "Verified: the reward is a learned PRM, failure detection is unspecified, and only non-failure "
               "trajectories reach the buffer. Whether curation is anchored in verifiable outcomes cannot be determined.",
               ["son55:E012", "son55:E016"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "son55", "unmet",
               "Verified: the adaptation and reported streams are the same 30/14-day stream with no declared split.",
               ["son55:E019", "son55:E021"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28", "sol",
               {"moved_to": "rsi:couple_context_and_weight_updates/H28-step5", "status": "partial"},
               "sol's tactic-level 'H28' check is the lever-ablation question that son55 asked as H28-step5. Merged; "
               "sol's partial is verified (context-only and coupled arms exist, weights-only does not).",
               ["sol:E07", "sol:E08"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step3", "son55", "met",
               "Verified: every sample carries its skill-generation index, and stale samples are flushed.", ["son55:E014"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28-step5", "revised", "partial",
               "Same question as sol's 'H28' (partial). The Skills arm is context-only and Full is coupled. The "
               "weights-only arm, seeds and a clean split are missing, so partial rather than unmet; no score effect.",
               ["son55:E022", "son55:E031", "son55:E024"]),
            XC(p, "rsi:couple_context_and_weight_updates/S1", "son55", "partial",
               "Verified: the support and query streams are disjoint by design, and the interface is the "
               "version-stamped data rather than shared rollouts.", ["son55:E013", "son55:E014"]),
            XC(p, "rsi:couple_context_and_weight_updates/S2", "son55", "partial",
               "Verified: typed roles are argued (Case 2) but not isolated by a weights-only arm.",
               ["son55:E025", "son55:E026", "son55:E031"]),
            XC(p, "rsi:couple_context_and_weight_updates/S3", "son55", "met",
               "Verified: RL runs on trajectories collected under the evolving skill context, and skills come from failures.",
               ["son55:E013", "son55:E005"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M. The meta-learning and mutual-reinforcement premises are not carried by an objective or a "
                "test, and the buffer rationale is inconsistent; interface clarity belongs to X.",
                ["son55:E013", "son55:E014", "son55:E027", "opus:O02"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 1,
                "See ratings.E.cost. A wall-clock disclosure (5-day run) without totals is 1 under run precedent; "
                "not_reported would need no cost figure at all.", ["sol:E07", "son55:E022"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2603.17187-1..4].id", "sol_value": "1 holdout, 2 measurement, 3 cost, 4 retained-transfer",
             "son55_value": "1 statistics, 2 measurement, 3 buffer semantics, 4 cost",
             "final_value": "1 holdout, 2 measurement, 3 cost, 4 retained-transfer, 5 statistics, 6 buffer semantics",
             "reason": "A4 hidden ID collision: local-1 had the same status ('unmet') in both seats for different "
                       "questions, so the mechanical diff missed it. Renumbered.",
             "evidence_ids": ["sol:E03", "son55:E022"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–6 and Appendix A first. Initial view: in scope (retained skill "
                                                   "library). The two-timescale design is coherent, but the buffer rules "
                                                   "contradict each other (§3.3 vs §3.4 vs Alg. 1). There is no "
                                                   "weights-only, versioning-off or memory baseline. The stream is "
                                                   "online with rule-revealing feedback. Cost is only '5-day run'. "
                                                   "Expected G2 M2 X2 Em2 Ec1 Eh1 Es1 Ecost0–1.",
            "integrity_checks": "Both seats a1 on 2603.17187v1, material sha 37a39048…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid.",
            "core_claim_check": "The strongest supported claim is a skills-on vs skills-off gain of 3–7 accuracy points on "
                                "an authored online stream (single runs), with Full larger for one model. The coupling, "
                                "versioning and zero-downtime claims are untested. 'Retained' is kept as narrow.",
            "rating_agreement": "G, X, Em, Ec, Eh, Es agree and were re-checked; M and Ecost resolved to son55.",
        },
    }

    # =========================================================== 2603.17613 VeriAgent (Δ2.5)
    p = "2603.17613"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "0.329 / 112 / 1.93e-05", "Table 2, 'Geometric Mean' row, ChipSeek-R1 column",
                    "Opus recomputation from the 44 per-design rows. The reported Geometric Mean reproduces only for "
                    "Original (0.417/141.5/2.65e-5, n=44). Over each column's valid designs: ChipSeek-R1 "
                    "0.310/92.9/1.80e-5 (n=38) vs reported 0.329/112/1.93e-5; VeriAgent-gpt-4o 0.345/129.3/5.85e-6 "
                    "(n=32) vs 0.362/122/6.89e-6; VeriAgent-gemini3 0.286/103.5/5.31e-6 (n=41) vs 0.294/109/5.72e-6.",
                    kind="our_inference"),
            opus_ev(p, "O02", "The relative PPA score is obtained by normalizing each design with respect to the original reference implementation provided by the benchmark.",
                    "§3.2 PPA Scores", "Opus recomputation. Per-design normalisation against Original, over designs "
                    "valid in both, gives geometric means of 2.49 (ChipSeek-R1), 9.44 (gpt-4o) and 9.99 (gemini3); "
                    "arithmetic means are 280/154/129. Neither matches the reported 2.196/5.119/8.539, which equal the "
                    "ratio of the reported column GMs (2.21/5.16/8.56) over unequal design sets.", kind="our_inference"),
            opus_ev(p, "O03", "0.1 / 11.704 / 3.03e-07", "Table 2, comparator_3bit, VeriAgent columns",
                    "Identical delay and area to Original (0.1 / 11.704) with 17× lower power (5.26e-06 → 3.03e-07). The "
                    "same pattern holds for barrel_shifter and ROM. This suggests different power-estimation conditions, "
                    "not design differences; div_16bit shows 1579×.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate",
            "supporting": ["adapt_via_conditioning"],
            "matches": [
                smatch("son55", p, "decompose_and_delegate",
                       reason="Opus confirms son55. The LLM emits an executable RTL artifact, which is routed to sound "
                              "external solvers (simulation testbenches, Yosys/OpenROAD synthesis), and their outputs "
                              "close the loop during construction (≤2 rounds each). That is C25. The paper's own ablation "
                              "makes this loop load-bearing (removing tool feedback/PPA agent costs more than removing "
                              "memory)."),
                smatch("son55", p, "adapt_via_conditioning",
                       reason="Supporting (sol's primary). Trigger-matched memory guidance injected into prompts conditions "
                              "the frozen generator. Sub null as in both seats: there is no canonical cross-task schema "
                              "and no upstream phase teaching the model to read it."),
            ],
            "outside_taxonomy": False,
            "reason": "decompose_and_delegate/C25 for the tool-in-the-loop generation; adapt_via_conditioning for the "
                      "retained memory read path. Identification only; the memory is still the in-scope retained object.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]), "son55"),
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.17613-3"): "local:2603.17613-5",
                    ("sol", "rsi:abstract_experience_into_guidance/H01"): "rsi:abstract_experience_into_guidance/H01-step5"},
            overrides={
                "local:2603.17613-2": {
                    "status": "unmet",
                    "reason": "Opus: the same aggregate-metric question in both seats. The headline Relative PPA does not "
                              "follow its stated per-design definition (opus:O02). The reported column GMs do not "
                              "reproduce from Table 2 for three of four columns (opus:O01), and they are taken over "
                              "unequal valid subsets (44/38/32/41) with failures excluded. Unmet, not partial."},
                "local:2603.17613-5": {"note": "A4: son55's local-3 (in-loop testbench identity) renumbered; sol's local-3 is cost."},
                "rsi:abstract_experience_into_guidance/H01-step5": {
                    "status": "unmet",
                    "reason": "Opus: sol's 'H01' and son55's 'H01-step5' ask the same question. Step 5 requires "
                              "ablating the curator, not just the store, and separating the construction and evaluation "
                              "streams. w/o Memory removes the whole store, there is no append-only/frozen/expert-memory "
                              "arm, and the streams are not separated. sol's 'partial' credits the store ablation, which "
                              "step 5 explicitly says is insufficient."},
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O01", "opus:O02", "opus:O03"]),
        "assessment": {
            "evidence_level": "task",
            "claim_support": "scoped",
            "strongest_supported_claim": "Feedback-equipped agents (testbench + synthesis loops) report higher functional "
                                         "pass rates than direct prompting on saturated benchmarks, and lower delay/area "
                                         "than the reference implementations on many RTLLM v2.0 designs (per-design raw "
                                         "values). The headline Relative PPA (5.119/8.539) and the memory ablation that "
                                         "uses it cannot be reproduced from Table 2 (opus:O01, opus:O02), and the power "
                                         "column is not comparable across columns (opus:O03). Retained, transferable "
                                         "memory gains are not shown.",
            "claim_support_note": "Scoped (sol), not unresolved (son55): the author claim is kept and narrowed to what "
                                  "the per-design table supports. The memory-attribution part stays open in 'unresolved'.",
            "unresolved": ["Memory construction vs evaluation streams; initial memory; order.",
                           "Whether the in-loop testbenches are the scoring testbenches.",
                           "Power-estimation conditions per column; the GM/Relative PPA computation.",
                           "Flow identity for ChipSeek-R1 and VeriPPA numbers; Figure 2 contents (image only).",
                           "Cost; seeds; prompts and node examples."],
        },
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. PPA neglect, shallow tool feedback and no accumulation are "
                   "concrete limitations with neighbours named (VeriPPA, VeriOpt, ChipSeek-R1). The memory gap is generic "
                   "agent memory transplanted, and the neighbours are cited, not studied.",
                   ["son55:E003", "sol:E15"], ["son55:E027"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Tool-in-the-loop plus trigger-conditioned memory is coherent, "
                   "but there is no account or node example of why memory should raise PPA, and retention is an "
                   "unexamined LLM Decide call.", ["son55:E004", "son55:E005", "son55:E007", "sol:E05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. The node schema, read path and insert/refine/discard are "
                   "described. Prompts, K beyond top-3, thresholds, initial memory, size and task order are absent, and "
                   "there is no gate, versioning or retirement.",
                   ["son55:E004", "son55:E005", "son55:E006", "son55:E010"], ["son55:E007", "son55:E008"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55 and extends the reason. The tools (Yosys/OpenROAD, "
                               "NanGate45) are standard, but the headline measurement is not reproducible. (i) The "
                               "reported Geometric Mean row reproduces only for Original, not for ChipSeek-R1 or either "
                               "VeriAgent column (opus:O01). (ii) Relative PPA does not equal the stated per-design "
                               "normalisation; it equals a ratio of column GMs over unequal valid subsets (opus:O02, "
                               "son55:E015). (iii) Power drops 17× at identical delay and area (opus:O03) and 1579× for "
                               "div_16bit (son55:E017, son55:E018), which points to non-comparable power conditions. "
                               "(iv) VeriPPA is compared across protocols. sol's 2 notes the power-activity and "
                               "aggregation questions but does not test them. This is r11a's TTE level, where reported "
                               "numbers contradict the stated protocol.",
                               ["son55:E013", "son55:E021", "opus:O01", "opus:O02", "opus:O03"],
                               ["son55:E015", "son55:E016", "son55:E018", "son55:E022", "son55:E024", "son55:E027"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. w/o Memory with the same LLM, prompts and rounds on "
                             "two backbones is the relevant store-off toggle. The ablation is cumulative and single-run, "
                             "with no static/expert memory or curator-off arm, and tool/PPA components explain more of "
                             "the score. The metric's reproducibility is counted under E.measurement only (A2).",
                             ["son55:E028", "son55:E029", "sol:E10"], ["son55:E030", "son55:E031"]),
            "E.holdout": R("not_reported", 0, "Both seats 0; re-checked. Memory evolves 'after each task execution' on the "
                           "benchmarks being reported, with no construction/evaluation split, freeze, initial-memory or "
                           "order disclosure. Whether the in-loop testbenches are the scoring testbenches is unstated.",
                           [], ["son55:E006", "son55:E008", "son55:E009"],
                           ["§2.3 Memory (all subsections)", "§3.1 Setup (benchmarks, metrics, implementation)",
                            "§3.3 Ablation", "no appendix exists in the pinned v1 text"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): benchmark sizes and per-design N/A failures are "
                              "visible; there are no seeds, variance, CI or tests despite T=0.8 sampling.",
                              ["son55:E016", "sol:E13"], ["son55:E012"]),
            "E.cost": R("not_reported", 0, "Both seats 0; re-checked. There are no LLM-call, token, wall-clock or "
                        "synthesis-time figures for agents, memory manager or EDA runs; the smaller-model remark is "
                        "intent, not measurement.", [], ["son55:E011"],
                        ["§3.1 Implementation Details", "§3.2 Main Results", "§3.3 Ablation", "whole v1 text (no appendix)"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (no appendix exists; Figures 1–2 are images). In scope (A3): a non-weight "
                  "structured memory is edited after each task from EDA/testbench feedback and injected into later "
                  "generations. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 2 (win rates vs VeriPPA/ChipSeek-R1) is image-only; not used for any rating beyond "
                             "its described protocol.",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "sol", "scoped",
                "The author claim (memory + tools improve correctness and PPA) can be kept and narrowed to the per-design "
                "table and functional pass rates. son55's 'unresolved' items are carried in assessment.unresolved. "
                "claim_support is not scored.", ["sol:E16", "son55:E013", "opus:O02"], "none (not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "See rs_pattern: the tool-in-the-loop artifact/solver loop is C25 and is load-bearing in the paper's own "
                "ablation. The memory read path is kept as supporting adapt_via_conditioning.",
                ["son55:E008", "son55:E010", "son55:E028"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "Follows primary; adapt_via_conditioning sub null as in both seats.", ["son55:E005", "son55:E013"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "H01 is kept (both seats): an LLM Decide call chooses insert/refine/discard over existing entries. H00 "
                "is added: nodes are extracted from the agent's own outcome trajectories with explicit trigger "
                "conditions, H00's extraction step. Same pairing as the run precedents for extract-then-curate stores "
                "(r06b Training-Free GRPO, r07a ArcMemo).", ["son55:E004", "son55:E006", "son55:E007"], NOSCORE),
            XC(p, "local:2603.17613-2", "son55", "unmet",
               "The same aggregate-metric question in both seats. The Opus recomputation (opus:O01, opus:O02) shows the "
               "headline does not follow its definition and the GM row does not reproduce, so unmet.",
               ["son55:E015", "son55:E022", "opus:O01", "opus:O02"]),
            XC(p, "local:2603.17613-3", "sol", "unmet",
               "A4 ID collision: sol's local-3 is cost and son55's local-3 is testbench identity. Final local-3 = cost, "
               "unmet (no cost table; matches son55's decompose RE-1 'unmet'). son55's question moved to local-5 "
               "(status unknown, kept).", ["sol:E07", "son55:E011"]),
            XC(p, "local:2603.17613-4", "son55", "unmet",
               "Verified: no repeated runs, std or CI; one number per cell at T=0.8.", ["son55:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: there is no static/expert-curated or non-evolving memory comparison, although the authors name "
               "it as the ideal.", ["son55:E030"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Verified: no latency, call, token or synthesis-time numbers.", ["son55:E011"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: the progressive ablation is cumulative and single-run, so component effects are order-dependent.",
               ["son55:E028"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "unmet",
               "Verified: no agent or memory-manager prompts, node examples or thresholds in the text.", ["son55:E005"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "unmet",
               "Verified: Table 2 has no direct-LLM or PPA-prompted single-agent column.", ["son55:E031", "son55:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: domain-specific trigger types are tailored, but the extract–decide–inject loop is generic.",
               ["son55:E004", "son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01", "revised",
               {"moved_to": "rsi:abstract_experience_into_guidance/H01-step5", "status": "unmet"},
               "sol's tactic-level 'H01' check (partial) asks H01 step 5's question (curator ablation plus separated "
               "streams). Merged. Final unmet: step 5 says a store-only ablation is insufficient.", ["sol:E09", "son55:E030"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01-step5", "son55", "unmet",
               "Verified: w/o Memory removes the store, not the curator, and the construction and evaluation streams are "
               "not separated.", ["son55:E006", "son55:E030"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: nodes derive from trajectories whose correctness and PPA outcomes come from simulation and "
               "synthesis.", ["son55:E004", "son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: admission is an LLM Decide call with no outcome test of a node.", ["son55:E007"]),
            XC(p, "rsi:evidence_gated_retention/F1", "son55", "partial",
               "Kept as a check question (card not matched). The memory-manager structure stands in for a gate, and its "
               "decisions are not evidence-based.", ["son55:E007"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Kept as a check question. No memory-on/off counterfactual credits individual nodes.", ["son55:E007"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 1,
                "See ratings.E.measurement. The GM row is non-reproducible for 3/4 columns (opus:O01), the headline "
                "definition is not followed (opus:O02), and power anomalies at identical delay/area (opus:O03) put this "
                "at the r11a TTE level (1), not 2.", ["opus:O01", "opus:O02", "opus:O03", "son55:E018"],
                "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "2 (aggregation rule unclear)",
             "son55_value": "1 (ratio of column GMs over unequal subsets)", "final_value": 1,
             "reason": "Neither seat recomputed Table 2. The reported Geometric Mean row itself does not reproduce from "
                       "the per-design rows for ChipSeek-R1 or either VeriAgent column (opus:O01). Recorded in the "
                       "reason; the rating equals son55's.", "evidence_ids": ["opus:O01", "opus:O02"],
             "score_impact": "none beyond the son55 resolution"},
            {"field_path": "expectations[local:2603.17613-3].id", "sol_value": "local-3 = cost", "son55_value": "local-3 = testbench identity",
             "final_value": "local-3 = cost; local-5 = testbench identity",
             "reason": "A4 ID collision. Renumbered.", "evidence_ids": ["son55:E008", "sol:E07"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope (an edited, "
                                                   "re-injected memory). I recomputed Table 2: valid designs "
                                                   "44/38/32/41, GMs not reproducible for 3 columns, Relative PPA "
                                                   "≠ per-design definition, and power anomalies at identical "
                                                   "delay/area. Em 1. Memory builds on the scored benchmark (Eh 0), no "
                                                   "cost (0), single runs (Es 1), store-off ablation present but "
                                                   "cumulative (Ec 2), G/M/X 2.",
            "integrity_checks": "Both seats a1 on 2603.17613v1, material sha 9ebe9986…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid.",
            "core_claim_check": "The strongest supported claim is functional gains on saturated benchmarks plus raw "
                                "per-design delay/area improvements. The headline PPA ratio and memory attribution are "
                                "not reproducible. evidence_level task (memory evolves on the scored stream).",
            "rating_agreement": "G, M, X, Ec, Eh, Es, Ecost agree and were re-checked; Em resolved to son55 with an "
                                "extended reason.",
        },
    }
    return S
