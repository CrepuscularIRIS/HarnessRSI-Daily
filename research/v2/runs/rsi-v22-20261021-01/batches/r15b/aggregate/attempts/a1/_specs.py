"""Opus rulings for r15b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat inputs: all ten a1 seat records match conflicts.json seat_record_hashes (asserted by _build.py; any "
        "git-pinned fallback is listed under validation.seat_input_pinning). No overrides, no seat errors.",
        "2604.14475 Evo-MedAgent (both seats 46.25): final 45.0. Shared correction E.statistics 2 → 1. The only "
        "uncertainty is a three-permutation range for one configuration (GPT-5-mini full memory). The number of "
        "evaluated questions is never stated, and 'incomplete runs' (dashes) have no failure accounting. Under the A2 "
        "ladder, tier 2 needs a usable failure denominator. evidence_level → retained (son55), scoped: same-backbone "
        "store-off and single-store arms on later items of the stream (r04b/r10b/r11b convention). The evaluated-"
        "stream construction and the unaudited sibling-question channel (2,500 questions over 675 cases) are scored "
        "in E.holdout = 1. The paper's 'consistently outperforms either component alone' is not supported for "
        "GPT-5-mini (0.79, range 0.76–0.82, vs episodic-only 0.78).",
        "2604.14399 SpaceMind (Δ1.25): final 46.25. M → son55 2. X → son55 3. E.holdout → son55 1: same-instance "
        "repeated episodes, as in the r08a EvoTest precedent. E.cost → sol 1: step counts are reported, as in "
        "Learning to Commit r13b. Opus adds two findings. (1) The six groups were picked because their single-run "
        "baselines failed or scored low, so regression to the mean is an unexcluded explanation. (2) The two "
        "'no benefit' groups are regressions: CAPSTONE Search C1 went from baseline OK to 0/5, and Huygens Rndz. C2 "
        "from OK to 3/5. son55's 'the other 2 groups unchanged' is corrected. Domain → H00 + H01 (r03a/r13b boundary).",
        "2604.14972 SAGER (Δ6.25): final 57.5 (= son55). G → son55 2: i2Agent is described in the paper's own "
        "baseline appendix as refining its 'internal state or strategy'. The evolved skill content is a preference "
        "profile ('likes: …'), so the how-versus-what premise is weakened. E.measurement → son55 2: evaluation uses "
        "1 positive plus 9 random negatives, and how the baselines were run is not stated. Opus finding: the paper's "
        "own Table 4 contradicts 'directly and exclusively attributable to the policy skill layer'. Removing listwise "
        "takes GoodReads H@1 from 0.459 to 0.427, against a MemRec/no-skill value of 0.399. RS → adapt_via_"
        "conditioning only (heterogeneous_decomposition dropped: no partition of a resource by a characterized property).",
        "2604.15034 Autogenesis (Δ1.25): final 57.5. G and M → son55 2. E.measurement → son55 3. E.causality → son55 "
        "2: matched-opportunity SR/SC/Bo3 controls are present. E.cost → sol 2: the headline GAIA Vanilla→Agent-Evo "
        "gain has no per-variant cost. All quantitative gains are within-task revisions; no committed version is "
        "evaluated on later tasks; evidence_level task. RS → generative_process_redesign (run convention for "
        "harness editors: r01b, r03b, r10a, r11a, r13b, r14b). Domain → H12 + H30 (low fit; the card's F1 "
        "'infrastructure offered as the gate' applies).",
        "2604.15676 EvoRAG (Δ1.25): final 62.5 (= sol). E.measurement → sol 3: ACC/EM/F1 with clear denominators "
        "and a feedback–truth agreement table. E.holdout → sol 1: the training queries are generated inside the "
        "subgraphs retrieved for the test queries. E.cost → sol 2: the training-phase query and feedback budget is "
        "missing. The abstract's 7.34% is the mean over three baselines; against the strongest KG-RAG framework per "
        "dataset the gains are +8.00/+4.06/+3.33 ACC (mean 5.13). RS → generative_process_redesign + relax_discrete_"
        "search_to_continuous (revised). Domain → H29 + H09 + H04 (union).",
        "A4 hygiene: hidden local-ID collisions were renumbered or merged in SpaceMind (local-1), Evo-MedAgent "
        "(local-1/2), Autogenesis (local-1–4) and EvoRAG (local-1/3). Every move is recorded in the affected "
        "resolution or expectation note.",
        "Some expectations come from cards that are not kept as pattern matches: heterogeneous_decomposition "
        "(SAGER), unify_into_shared_representation (Autogenesis) and self_supervised_signal_engineering (EvoRAG). "
        "They are kept as check questions with a note and never score directly.",
        "Figure dependence: SpaceMind Figs 3–4, Evo-MedAgent Fig 2, SAGER Figs 3–7, Autogenesis Figs 2–9 and EvoRAG "
        "Figs 3 and 7–20 are image-only. Only values stated in the text or tables are used, and no figure value was "
        "read off an image.",
        "No material requests. No disputed rating depends on missing neighbour originals.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"

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

    def pmap(s, p, i):
        return prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][i]), s)

    def PM(rs_main, d_main, d_sub, corr, cond, ev):
        return {"rs_main": rs_main, "rs_sub": None,
                "domain": {"namespace": "rsi", "main": d_main, "sub": d_sub},
                "operation_correspondence": corr, "necessary_conditions_and_differences": cond, "evidence_ids": ev}

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def set_claim(claims, cid, **upd):
        for c in claims:
            if c["claim_id"] == cid:
                c.update(upd)
        return claims

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a = prefix(a, s)
        a.update(upd)
        return a

    def moved(old):
        return {"note": f"Merged here from {old} (A4: same question under a colliding or different ID)."}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on rs_pattern)."}

    # =========================================================== 2604.14399 SpaceMind (Δ1.25)
    p = "2604.14399"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "prioritizing combinations where the reasoning evaluation baseline failed or scored low",
                    "§4.4 Skill Self-Evolution",
                    "The six groups were picked because their baseline failed or scored low. Each baseline is a "
                    "single earlier run: Table 5 counts pass per 5 runs over 5 satellites, so there is one run per "
                    "satellite×task×condition×mode. Five fresh episodes of a once-failed instance can improve by "
                    "regression to the mean, without any skill. Neither seat named this alternative.",
                    kind="our_inference"),
            opus_ev(p, "O02", "However, the two groups where the baseline already succeeds, CAPSTONE Search C1 and "
                              "Huygens Rndz. C2, do not benefit from self-evolution",
                    "§4.4; Table 6 rows CAPSTONE Search C1 and Huygens Rndz. C2",
                    "Table 6 lists CAPSTONE Search C1 baseline OK (2.597 m) and Best After Evol. 0/5, and Huygens "
                    "Rndz. C2 baseline OK and 3/5. These are drops in success rate after evolution, and the paper "
                    "calls them 'No benefit'. The four-of-six count therefore sits beside two regressions.",
                    kind="our_inference"),
            opus_ev(p, "O03", "Huygens Insp. C1 from 12 to an average of 59.4 points",
                    "§4.4 text vs Table 6 'Best After Evol.' column",
                    "Table 6 reports the best round (68 pt, '+467%'), the text reports the five-round mean (59.4), "
                    "and the abstract says 59. The 'Best After Evol.' column is a max over rounds set against a "
                    "single baseline run.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning, sub null. Learned skill files are injected as conditioning "
                      "into a frozen VLM. There is no upstream training of a unified schema reader and no category "
                      "holdout, so C03 is not assigned (r04b/r13b convention).",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            pmap("sol", p, 0),
            PM("adapt_via_conditioning", "abstract_experience_into_guidance", "H00",
               "After each episode the VLM reflects on the outcome, the termination reason and recent episode summaries. "
               "It writes Intent/Trigger/Rule/Constraints/Evidence skill files, which are injected into later runs.",
               "H00 needs outcome-grounded lessons (met: success/failure and score) and contrast between outcomes "
               "(partial: recent summaries are given, but no success/failure pairing is specified).",
               ["sol:E003", "son55:E001", "son55:E013"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.14399-1"): "rs:adapt_via_conditioning/RE-1",
                    ("sol", "local:2604.14399-2"): "rsi:abstract_experience_into_guidance/H00-step4",
                    ("sol", "local:2604.14399-3"): "local:2604.14399-1"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "unmet",
                    "reason": "Opus: same question in both seats. There is no same-batch run with skills off or with "
                              "an alternative reflector, only a single historical baseline run (opus:O01).",
                    **moved("sol:local:2604.14399-1")},
                "rsi:abstract_experience_into_guidance/H00-step4": {
                    "status": "unmet",
                    "reason": "Opus: learning and evaluation use the same satellite/task/condition instance for five "
                              "rounds. No frozen-store run on an unseen group exists, and the laboratory campaign "
                              "does not use evolved skills.",
                    **moved("sol:local:2604.14399-2")},
                "local:2604.14399-1": {
                    "status": "unmet",
                    "reason": "Opus: the baseline is one run, with no interval or test, yet the paper says "
                              "'significant'. The two regressions (opus:O02) and best-of-rounds reporting (opus:O03) "
                              "add to this.",
                    "note": "Merged here from sol:local:2604.14399-3 (statistics). sol's local-1 (store-off control) "
                            "moved to rs:adapt_via_conditioning/RE-1."},
                "rsi:abstract_experience_into_guidance/S3": {
                    "status": "met",
                    "reason": "Opus: reflection receives the episode's success/failure outcome and termination reason "
                              "(§3.5). The unstated inspection scorer is a measurement gap (E.measurement), not a "
                              "missing grounding signal."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03"]), "C2", []),
        "assessment": assess("sol", p, [
            "Opus: groups were selected on failing/low single-run baselines, so regression to the mean is not "
            "excluded (opus:O01).",
            "Opus: the two 'no benefit' groups dropped from baseline OK to 0/5 and 3/5 (opus:O02).",
            "Opus: Table 6 'Best After Evol.' is a max over rounds (opus:O03)."],
            evidence_level="task",
            evidence_level_note="Retained skill files are read in later episodes, but those episodes replay the same "
                                "instance that produced the skill. No skills-off control exists, and baselines are "
                                "single runs chosen for failing (EVIDENCE rule 2; r08a EvoTest precedent).",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Space VLM agents are one-shot executors, a concrete "
                   "fixed object. Reflexion/ExpeL/Voyager are named, but only in prose. The 'physical deployment "
                   "experience' selling point is not exercised: evolution runs only in UE5.",
                   ["sol:E001", "sol:E002", "son55:E017", "son55:E018"], ["son55:E014"]),
            "M": R("resolved", 2, "Opus sides with son55. The chain reflect → five mutation types → quality gate → "
                   "top-k injection is clear and fits failure recovery. But the load-bearing assumption (one failed "
                   "episode's reflection yields a correct, reusable rule) is not argued against simple retry at "
                   "temperature ≤0.3 or a hand-written patch. The gate is called a 'safety guarantee' although it is "
                   "lexical and structural (blacklist, fingerprint, scope, parent check). No distinguishing "
                   "prediction is stated. sol's 3 credited the clarity of the chain, which X already rewards.",
                   ["sol:E003", "sol:E004", "son55:E001", "son55:E002", "son55:E013"], ["sol:E009"]),
            "X": R("resolved", 3, "Opus sides with son55. Algorithm 1, the five edit operations, the four gate checks "
                   "with an audit log, provenance/version/scope metadata, the disable operation, human-revertible "
                   "files, top-k scope-matched injection and the observed routing of the seven learned skills are all "
                   "reconstructible. The boundaries (no benefit on solved baselines, no cross-task transfer by "
                   "design) are stated. Not 4: Evaluate(τ), k and the reflection prompt are unspecified, and there is "
                   "no utility-based retirement trigger. sol's objections (safety overclaim, no regression gate, "
                   "regressions) are scored in M and E.",
                   ["sol:E004", "sol:E005", "sol:E006", "son55:E002", "son55:E003", "son55:E004", "son55:E019"],
                   ["son55:E011"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Navigation success, distance and steps are "
                               "objective, though the ~2 m pass threshold is loose (2.597 m counts as OK). The "
                               "inspection 0–100 scorer is unspecified. Table 6 reports best-of-rounds against single "
                               "baselines (opus:O03).",
                               ["sol:E013", "son55:E021", "opus:O03"], ["son55:E005", "son55:E020"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked, with an alternative neither seat named. Groups "
                             "were chosen because their single-run baseline failed, so regression to the mean can "
                             "produce 'recovery' (opus:O01). There is no skills-off rerun, no edit/gate ablation and "
                             "no alternative reflector. Two of six groups regressed (opus:O02). Not 0: the step-count "
                             "convergence (20 → 7) with an inspectable distance-step skill gives some mechanistic "
                             "support.",
                             ["sol:E007", "sol:E008", "son55:E013", "opus:O01"], ["opus:O02", "sol:E009"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. The skill is learned and evaluated on the same "
                           "instance across five rounds, best-of-rounds is reported, and there is no frozen-store "
                           "unseen test. The later rounds are still separate episodes executed after the skill was "
                           "written, as in the r08a EvoTest precedent (E.holdout 1). sol's not_reported 0 would treat "
                           "same-instance replays as no evidence.",
                           ["son55:E008", "sol:E007"], ["son55:E011", "son55:E020"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). The 6 groups × 5 rounds denominators and the "
                              "negative groups are reported. Baselines are single runs, with no interval or test, yet "
                              "the paper says 'significant'.",
                              ["sol:E007", "sol:E013", "son55:E010", "son55:E012"], ["opus:O02"]),
            "E.cost": R("resolved", 1, "Opus sides with sol. Per-episode step counts (decision calls) are reported, "
                        "the evolved group's steps fall from 20 to 7, and the mode call structure is given. Reflection "
                        "calls, tokens, latency and a budget-matched comparison are absent. This follows Learning to "
                        "Commit r13b (measured execution counts give 1), not PsychAgent r13b (settings only give 0).",
                        ["sol:E012", "sol:E014", "son55:E009"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (no appendix). In scope (system_method): the Skill Self-Evolution "
                  "loop writes persistent non-weight skill files from execution outcomes, and later episodes read "
                  "them. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 3–4 (pass-rate and learning curves) are image-only. Values come from Tables 4–7 "
                             "and the text.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "Both apply (r03a/r13b boundary). H00 covers reflection on episode outcomes into Trigger/Rule skills. "
                "H01 covers the explicit create/overlay/rewrite/disable editing of the skill set.",
                ["sol:E003", "son55:E001", "son55:E013"], NOSCORE),
            XC(p, "local:2604.14399-2", "revised", {"moved_to": "rsi:abstract_experience_into_guidance/H00-step4",
                                                    "status": "unmet"},
               "sol's 'no frozen unseen group' question is the card's H00 step 4. Merged; unmet in both.",
               ["sol:E007", "son55:E008"]),
            XC(p, "local:2604.14399-3", "revised", {"moved_to": "local:2604.14399-1", "status": "unmet"},
               "sol's statistics question is son55's local-1 (A4 hidden collision: sol's own local-1 was the store-off "
               "question, now under RE-1). Final unmet, not partial: the baseline is n=1 with no test behind "
               "'significant'.", ["son55:E010", "opus:O02"]),
            XC(p, "local:2604.14399-4", "sol", "partial",
               "Cost (sol only). Verified: step counts and call structure are visible; reflection cost and matched "
               "budget are absent.", ["sol:E012", "sol:E014"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "unmet",
               "Verified: no skills-off rerun in the same batch. sol's local-1 (same question) is merged here.",
               ["son55:E005", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no hand-written-lesson or longer-context comparison.", ["son55:E013"]),
            XC(p, "rsi:abstract_experience_into_guidance/F1", "son55", "partial",
               "Verified: the introduction and contribution 3 present 'without model fine-tuning or reward function "
               "design' as part of the claim. The space-specific skill format keeps this partial.",
               ["sol:E001", "son55:E017"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "unmet",
               "Verified: same-instance learning and evaluation. sol's local-2 is merged here.",
               ["son55:E008", "sol:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step5", "son55", "unmet",
               "Verified: no skills-off retry control and no budget matching.", ["son55:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01-step5", "son55", "unmet",
               "Verified: no edit-operation or gate ablation.", ["son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: the fixed objects named are the monolithic prompt and the one-shot executor. The loop "
               "itself is the generic reflect→store loop.", ["son55:E017"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: recent episode summaries are supplied, but no success/failure pairing is specified.",
               ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "sol", "met",
               "S3 asks for a grounding signal. Reflection receives the outcome and termination reason. son55's "
               "concern (inspection scorer unspecified) is a measurement gap scored in E.measurement.",
               ["sol:E003", "son55:E001"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the core assumption is untested against retry or a hand patch, and the gate's 'safety "
                "guarantee' is overclaimed.", ["son55:E002", "sol:E004"], "−5.0 vs sol (20×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 3,
                "See ratings.X: the retention, version, disable and injection chain is reconstructible, with stated "
                "boundaries. sol's grounds belong to M and E.", ["son55:E003", "son55:E019", "sol:E005"],
                "+5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: same-instance later episodes count as weak evidence (r08a EvoTest = 1), not "
                "as none.", ["son55:E008"], "+2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 1,
                "See ratings.E.cost: measured per-episode step counts give 1 (Learning to Commit r13b). son55's "
                "not_reported 0 overlooks them.", ["sol:E012", "son55:E009"], "+1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.strongest_supported_claim / claims.C1 (son55)",
             "sol_value": "CAPSTONE Search 0/5 noted", "son55_value": "其余2组无变化 (the other two groups unchanged)",
             "final_value": "two regressions: CAPSTONE Search C1 OK→0/5, Huygens Rndz. C2 OK→3/5",
             "reason": "son55-only factual error, recorded because the final uses sol's assessment and claims. Table "
                       "6 shows lower success after evolution in both 'no benefit' groups (opus:O02). Neither seat "
                       "named the selection-on-failure regression-to-the-mean alternative (opus:O01). It is added to "
                       "E.causality without changing the rating.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; evidence "
                                                   "task (same-instance replays, selection on failing single-run "
                                                   "baselines). G 2, M 2, X 3, Em 2, Ec 1, Eh 0–1, Es 1, cost 0–1.",
            "integrity_checks": "Both seats a1 on 2604.14399v1, material sha 87157d55…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: in four of six UE5 groups selected for failing baselines, "
                                "rounds run after reflection-generated skills did better than the single baseline run. "
                                "Two groups regressed. Retained-skill causation is not shown. claim_support scoped.",
            "rating_agreement": "G, Em, Ec and Es agree (re-checked). M → son55, X → son55, Eh → son55, cost → sol. "
                                "Final 46.25.",
        },
    }

    # =========================================================== 2604.14475 Evo-MedAgent (same 46.25)
    p = "2604.14475"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "configuration consistently outperforms either component alone (Table",
                    "§4.2 Division of Memory Labor",
                    "Table 1 GPT-5-mini: episodic-only 0.78 vs full 0.79, whose own permutation range is 0.76–0.82. "
                    "The 'consistently outperforms' claim does not hold for that backbone, and the episodic/procedural "
                    "'division of labor' has no per-category breakdown.", kind="our_inference"),
            opus_ev(p, "O02", "Full-memory GPT-5-mini MCQ is reported as mean (range) across three case-order "
                              "permutations",
                    "Table 1 caption",
                    "This is the only uncertainty in the paper. The number of evaluated questions is never given (the "
                    "benchmark has 2,500 questions over 675 cases), so the three accuracies cannot be turned into "
                    "counts or intervals.", kind="our_inference"),
            opus_ev(p, "O03", "Dashes indicate incomplete runs.", "Table 1 caption",
                    "Configurations with dashes (GPT-5.2 ablations, the open-ended ablations, the tool-enabled open "
                    "rows) are incomplete runs with no failure accounting.", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning, sub null. Retrieved episodes, rules and governance labels "
                      "condition a frozen VLM. There is no upstream schema training and no category holdout, so not "
                      "C03.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "evidence_gated_retention", "H29"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            pmap("son55", p, 0),
            pmap("sol", p, 0),
            PM("adapt_via_conditioning", "evidence_gated_retention", "H29",
               "Each procedural rule carries usage statistics (times selected, correct when active). Selection uses "
               "a utility estimate with an exploration bonus, and tool trust labels come from interaction counts.",
               "H29 needs a counterfactual behind the credit (unmet: correctness while active is a correlation). The "
               "utility term is never ablated.",
               ["son55:E008", "son55:E009", "son55:E011"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.14475-1"): "local:2604.14475-5",
                    ("sol", "local:2604.14475-2"): "local:2604.14475-1"},
            overrides={
                "local:2604.14475-1": {
                    "status": "partial",
                    "reason": "Opus: repeats exist only for GPT-5-mini full memory. The evaluated N is not stated "
                              "and incomplete runs are not accounted for (opus:O02, opus:O03).",
                    "note": "Merged here from sol:local:2604.14475-2 (statistics). A4 collision: sol's local-1 "
                            "(governance) moved to local-5."},
                "local:2604.14475-5": {
                    "reason": "Opus: verified. Tool governance is deferred, and in the tool-free Table 1 runs it has "
                              "no tools to govern, so the three-store claim is tested as a two-store system.",
                    **renum("sol:local:2604.14475-1")},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "unmet",
                    "reason": "Opus (revised from partial): the store is written continually from the evaluated "
                              "stream using its labels, and no frozen-store evaluation exists. Prequential order "
                              "stops same-item leakage only. The sibling-question channel (≈3.7 questions per case) "
                              "is unaudited."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01"]), "C1", ["opus:O02", "opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: the 'consistently outperforms either component alone' claim fails for GPT-5-mini (opus:O01).",
            "Opus: evaluated N and incomplete-run accounting are missing (opus:O02, opus:O03)."],
            evidence_level="retained",
            evidence_level_note="Retained, scoped. Memory written from earlier cases is read on later ones, and "
                                "same-backbone store-off and single-store arms isolate the stores (r04b/r10b/r11b "
                                "convention: held-out preferred, not required). The weak points are scored in "
                                "E.holdout = 1: the store is built from the evaluated stream with ground-truth "
                                "feedback, and sibling questions of the same case may leak. Unlike r02a 2411.13941, "
                                "a same-actor store-off arm exists.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Isolated per-case solving is a real limitation. The "
                   "three-store factorisation and utility selection come from Evo-Memory and ReMe, and no neighbour "
                   "is compared on this benchmark. The residual is mainly the application domain.",
                   ["son55:E001", "son55:E005", "son55:E006", "sol:E002", "sol:E003"], ["son55:E007"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Precedent retrieval plus outcome-grounded rule edits fits "
                   "recurrent mistakes. Rule edits are unvalidated, governance is untested, and the 'memory beats "
                   "tools' reasoning rests on a confounded comparison.",
                   ["son55:E008", "son55:E012", "sol:E004", "sol:E005", "sol:E006"], ["son55:E017"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. The read/write cycle and governance thresholds are given. "
                   "K, K_S, s_epi, the utility formula and the reflection prompt are missing, and there is no "
                   "forgetting, merging, versioning or admission check.",
                   ["son55:E009", "son55:E011", "son55:E012", "sol:E005", "sol:E007"], ["son55:E024"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. MCQ accuracy on an expert-curated public "
                               "benchmark is reliable. The open-ended scorer is unspecified, the evaluated N is "
                               "unstated, and incomplete runs are unexplained (opus:O03).",
                               ["son55:E002", "sol:E008", "sol:E013"], ["son55:E025", "opus:O03"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-backbone store-off and episodic-only / "
                             "procedural-only arms isolate memory as a whole. Missing: comparison with the cited "
                             "nearest neighbours (Evo-Memory, Dynamic Cheatsheet, ReMe), a governance or utility "
                             "ablation, and a budget-matched reflection-only arm. The rule-store increment is within "
                             "noise (opus:O01). The 'memory beats tools' comparison is memory vs no memory (tool-free "
                             "= tool-enabled = 0.68).",
                             ["son55:E016", "son55:E022", "sol:E009"], ["son55:E010", "son55:E017", "opus:O01"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The construction stream is the evaluation stream, "
                           "with ground-truth feedback after every item. There is no frozen-store test and no "
                           "case-level isolation audit (2,500 questions over 675 cases).",
                           ["son55:E014", "sol:E006", "sol:E011"], ["son55:E013", "son55:E019"]),
            "E.statistics": R("resolved", 1, "Shared correction 2 → 1 (A2 ladder). The only uncertainty is a "
                              "three-permutation range for one configuration (GPT-5-mini full memory, 0.76–0.82). "
                              "The evaluated N is never stated, so accuracies cannot become counts or intervals "
                              "(opus:O02). 'Incomplete runs' carry no failure accounting (opus:O03). The "
                              "'consistently outperforms' claim sits inside that range (opus:O01). Tier 2 needs a "
                              "usable denominator; here the denominator itself is missing.",
                              ["son55:E015", "son55:E016", "opus:O02", "opus:O03"], ["sol:E010"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. The marginal call budget is explicit (one extra "
                        "retrieval and one multimodal reflection call per case), so a reader can bound the call "
                        "ratio. No tokens, latency, memory size or matched-budget arm are given.",
                        ["son55:E020", "sol:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (no appendix). In scope (system_method): an episodic, procedural "
                  "and governance memory is written from execution plus ground-truth feedback and read on later "
                  "cases, with a store-off control. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 2 (cumulative accuracy curves) and Figure 3 (case showcase) are image-only; "
                             "Table 1 and the text are used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "See assessment.evidence_level_note. A same-backbone store-off arm and single-store arms on later "
                "stream items meet the run's retained convention (r04b, r10b, r11b). sol's concerns (shared "
                "construction/evaluation stream, case isolation) are real and scored in E.holdout = 1. They do not "
                "trigger EVIDENCE rule 2: no selection set is reused as a test set.",
                ["son55:E014", "son55:E022", "sol:E009"], "none (label only)"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H01"], ["evidence_gated_retention", "H29"],
                 ["index_experience_for_reuse", "H03"]],
                "H29 applies: per-rule utility from usage outcomes with an exploration bonus drives selection (§3.1), "
                "the bandit-statistics case named in H29. Its condition checks fail (correlational credit, no utility "
                "ablation), and patterns never score.", ["son55:E008", "son55:E009"], NOSCORE),
            XC(p, "local:2604.14475-1", "son55", "partial",
               "A4 collision: sol's local-1 (governance not ablated) and son55's local-1 (statistics) differ. Final "
               "local-1 is the statistics question, partial. sol's statistics question (local-2) is merged here; "
               "sol's governance question moves to local-5 (unmet).", ["son55:E015", "opus:O02"]),
            XC(p, "local:2604.14475-2", "son55", "unmet",
               "A4 collision: sol's local-2 (statistics) moves to local-1. Final local-2 is son55's privileged-feedback "
               "question, unmet (verified: ground truth after every case; noisy or delayed supervision untested).",
               ["son55:E019", "sol:E011"]),
            XC(p, "local:2604.14475-3", "sol", "partial",
               "Cost (sol only). Verified: operation-level overhead only.", ["sol:E012"]),
            XC(p, "local:2604.14475-4", "sol", "partial",
               "Measurement (sol only). Verified: MCQ truth is clear; the open-ended judge and N are unspecified.",
               ["sol:E008", "sol:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: store-off and single-store arms exist; they are single runs except full memory.",
               ["son55:E022"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap audit for same-case questions or for Eurorad exposure during pre-training.",
               ["son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: episodic nearest-neighbour retrieval alone reaches 0.78 of 0.79; there is no long-context "
               "control.", ["son55:E022", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: three backbones, one benchmark, one modality.", ["son55:E022"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "unmet",
               "Verified: the stated novelty is the first evaluation in a tool-augmented medical imaging agent "
               "(failure mode present).", ["son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "unmet",
               "Verified: prequential evaluation on the construction stream, with no frozen-store holdout.",
               ["son55:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: names uncorrected procedural errors, but the loop is generic.", ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "partial",
               "S4 asks for explicit maintenance. 'Patch-style procedural edits' with priority tags are localized "
               "deltas (partial). No consolidation, forgetting or bound is described. son55's unmet overlooked the "
               "patch edits.", ["sol:E006", "son55:E012"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: edits are written without trial or test. Utility affects selection, not admission.",
               ["son55:E012", "son55:E009"]),
            XC(p, "rsi:evidence_gated_retention/H29-step5", "son55", "unmet",
               "Verified: no ablation of the utility or exploration term.", ["son55:E009"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "revised", "unmet",
               "F3 ('store built from the test stream') holds fully: the store is updated continually from evaluated "
               "items with their labels. sol's partial credited the prequential order, which prevents same-item "
               "leakage only.", ["son55:E014", "son55:E013", "sol:E006"]),
            XC(p, "rsi:index_experience_for_reuse/H03-step5", "son55", "unmet",
               "Verified: case-level isolation of the 2,500 questions is unstated.", ["son55:E013"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "sol", "met",
               "Verified: store-off, episodic-only, procedural-only and full configurations are compared (S5: the "
               "store is certified by removing it).", ["sol:E009", "son55:E022"]),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.statistics", "sol_value": {"status": "resolved", "rating": 2},
             "son55_value": {"status": "resolved", "rating": 2},
             "final_value": {"status": "resolved", "rating": 1},
             "reason": "Both seats credited the three-permutation σ as tier 2 while each noted that N is unknown and "
                       "that runs are incomplete. Under the frozen A2 ladder, a failure denominator comes before "
                       "uncertainty. The evaluated question count is never given, so neither counts nor intervals can "
                       "be formed (opus:O02). Incomplete runs are unaccounted (opus:O03). The paper's "
                       "complementarity claim lies inside the only reported range (opus:O01).",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "son55:E025", "sol:E013"],
             "score_impact": "−1.25 (5×1/4); 46.25 → 45.0"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; retained "
                                                   "(store-off on later stream items) but weak. Concerns: N never "
                                                   "stated, sibling questions per case, 'consistently outperforms' "
                                                   "within noise, memory-vs-tools confounded, governance untested in "
                                                   "tool-free runs. G 2, M 2, X 2, Em 2, Ec 2, Eh 1, Es 1, cost 1.",
            "integrity_checks": "Both seats a1 on 2604.14475v1, material sha 11d4edde…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: on the ChestAgentBench stream with ground-truth feedback, "
                                "episodic plus procedural memory lifts online MCQ accuracy by about 11 points over "
                                "no-memory on three backbones. Episodic retrieval carries most of the gain. Governance, "
                                "complementarity and 'memory beats tools' are unsupported. claim_support scoped.",
            "shared_error_review": "Same total 46.25 in both seats; every item was re-checked against the text. One "
                                   "shared error (E.statistics) was corrected. Other agreements were confirmed: E.cost "
                                   "1 (the marginal call budget is explicit), E.causality 2 (store-off arms) and "
                                   "E.holdout 1.",
            "rating_agreement": "All eight ratings agree; E.statistics corrected 2 → 1. Final 45.0.",
        },
    }

    # =========================================================== 2604.14972 SAGER (Δ6.25)
    p = "2604.14972"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Removing listwise (reverting to pointwise scoring) causes GoodReads",
                    "§3.4 Component Ablation; Table 4",
                    "Table 4 GoodReads H@1: full 0.459, w/o listwise 0.427, w/o policy skill 0.399 (= MemRec 0.400 "
                    "in Table 5). Listwise accounts for about 0.032 of the 0.060 gain over MemRec when the skill is "
                    "present. A listwise-without-skill arm is absent.", kind="our_inference"),
            opus_ev(p, "O02", "directly and exclusively", "§3.2 Main Results",
                    "The paper says the gains over MemRec are 'directly and exclusively attributable to the policy "
                    "skill layer'. Sager also replaces pointwise with listwise ranking, which its own ablation credits "
                    "with a large share (opus:O01), so exclusivity is contradicted.", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning primary, sub null. A persistent per-user skill document "
                      "conditions a frozen LLM; no upstream schema training, so not C03. son55's heterogeneous_"
                      "decomposition is not kept. That card partitions a resource by an empirically characterized "
                      "property and treats the parts differently. Per-user conditioning is the conditioning content "
                      "itself, and son55 recorded the heterogeneity as uncharacterized (fit weak).",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]),
                                                "son55"),
                           "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "local:2604.14972-1": {
                    "status": "partial",
                    "reason": "Opus: same question in both seats (separating skill from listwise and cheaper "
                              "alternatives). The w/o-listwise arm isolates the skill under pointwise scoring (0.399 "
                              "→ 0.427 GoodReads). No listwise-only arm or cost-matched profile-summary control "
                              "exists, and the paper's exclusivity claim is contradicted (opus:O01, opus:O02).",
                    "origin_note": "merged sol+son55 local-1"},
                "local:2604.14972-3": {
                    "status": "unmet",
                    "reason": "Opus: 'p<0.05' with no test, repeat count, interval or variance. Books (+1.92%) is "
                              "unverifiable."},
                "rs:heterogeneous_decomposition/RE-5": dropped_card("heterogeneous_decomposition"),
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: own Table 4 contradicts 'exclusively attributable to the policy skill layer' (opus:O01, opus:O02)."],
            evidence_level="retained",
            evidence_level_note="Retained, scoped. Skills evolved during warmup are frozen and read on later test "
                                "predictions, with store-off, StatInit-only and full-replacement arms. The warmup "
                                "source and the test-subset hyperparameter choice are scored in E.holdout = 2.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. A shared static policy prompt is a concrete fixed object "
                   "with MemRec as the nearest neighbour. But the 'how vs what' premise is weakened by the paper's own "
                   "material: its baseline appendix describes i2Agent as reflecting 'to refine its internal state or "
                   "strategy', and the evolved skill is a preference profile ('likes: casual Thai…'). The residual "
                   "bottleneck (strategy beyond preferences) is asserted, not shown. sol's 3 did not weigh this.",
                   ["son55:E001", "son55:E004", "sol:E001", "sol:E013"], ["son55:E003", "son55:E005"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Two-representation storage, incremental diffs with "
                   "conservative demotion, and listwise tie-breaking form a reconstructible chain. It makes "
                   "distinguishing predictions (H@1-heavy gains, τ=2 cycle, non-monotone injection length) that are "
                   "observed. Not 4: 'policy vs profile' is conceptually blurred.",
                   ["son55:E006", "son55:E019", "son55:E024", "sol:E002", "sol:E003", "sol:E004"], ["son55:E005"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Prompts, tiers, protection rules, τ, injection length "
                   "and cold/warm initialisation are explicit. The warmup data source, a utility gate or rollback, "
                   "and long-run bounds are missing.",
                   ["son55:E006", "son55:E009", "son55:E030", "sol:E011"], ["son55:E025", "sol:E012"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. H@K/N@K on InstructRec splits are objective, "
                               "but each list is 1 positive plus 9 random negatives, a sampled metric known to "
                               "diverge from full ranking. Whether baselines were rerun on the same candidate sets or "
                               "copied is not stated (Table 4 vs Table 5 MemRec rows differ in the third decimal). The "
                               "headline is a relative H@1 (+14.91%). sol's 3 acknowledged the sampled protocol but "
                               "did not weigh baseline provenance.",
                               ["son55:E010", "son55:E012", "sol:E005"], ["son55:E011", "son55:E029"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Leave-one-out, incremental vs full-replacement, "
                             "StatInit-only and plug-in hosts give real attribution. Missing: a listwise-only arm and "
                             "a same-budget reflective profile control. Exclusivity is contradicted (opus:O01). Half "
                             "of the gain comes from zero-LLM StatInit, not from feedback evolution.",
                             ["son55:E015", "son55:E016", "son55:E018", "sol:E008", "sol:E014", "opus:O01"],
                             ["son55:E013", "opus:O02"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Skills are frozen after warmup and evaluated on "
                           "the benchmark's standard splits. The warmup interaction source is unstated, and τ and "
                           "length were chosen on a 1,000-user subset of the evaluated users.",
                           ["son55:E008", "sol:E005"], ["son55:E009", "son55:E022", "son55:E023"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): user counts are known, p<0.05 is asserted "
                              "without test or variance, and τ=3 regression is reported.",
                              ["son55:E012", "sol:E009"], ["son55:E011", "son55:E027"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Zero-LLM StatInit and ~30-token injection are "
                        "stated. Evolution, extraction and listwise call costs and a baseline budget comparison are "
                        "absent.", ["son55:E025", "sol:E002"], ["son55:E030"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text including Appendices A–E read. In scope (system_method): a per-user "
                  "non-weight skill document is evolved from interaction feedback, retained, frozen and read on "
                  "later predictions. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 3–7 (plug-in bars, τ sweep, injection-length curves) are image-only. Only "
                             "text-stated values (e.g. τ=1 H@1 +4.6/+2.0/+4.4%) and Tables 2–5 are used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "heterogeneous_decomposition needs a resource partitioned by a characterized property with "
                "differentiated treatment. Per-user skills are per-instance conditioning, and the heterogeneity is "
                "uncharacterized (son55's own RE-5 unmet). See rs_pattern.reason.", ["son55:E001", "son55:E014"],
                NOSCORE),
            XC(p, "local:2604.14972-1", "sol", "partial",
               "Same question in both seats. The w/o-listwise arm isolates the skill under pointwise scoring, so "
               "isolation is partial, not absent. The missing listwise-only arm and the contradicted exclusivity are "
               "recorded (opus:O01).", ["opus:O01", "sol:E014", "son55:E014"]),
            XC(p, "local:2604.14972-3", "son55", "unmet",
               "Same statistics question in both seats. No test, repeats or intervals stand behind 'p<0.05'. sol's "
               "partial credited a qualitative 'multiple independent runs' remark about injection length only.",
               ["son55:E011", "son55:E027"]),
            XC(p, "local:2604.14972-4", "sol", "unmet",
               "Cost (sol only). Verified: no total evolution call, latency or cost accounting.", ["sol:E005"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: the w/o-skill row equals MemRec; the conditioning channel is confounded with listwise.",
               ["son55:E014", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: StatInit-only takes about half the gain, and there is no same-budget reflective-profile "
               "control.", ["son55:E016", "son55:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: four datasets and three hosts on one backbone. Plug-in results are figure-only.",
               ["son55:E020", "son55:E021"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "unmet",
               "Kept as a check question (card not retained). Verified: user decision-logic heterogeneity is "
               "posited, not analysed.", ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: a vertical domain, but with domain-specific mechanisms (slim injection, listwise "
               "activation).", ["son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "unknown",
               "Verified: skills are frozen at test, but whether warmup interactions overlap the test candidates is "
               "unstated. unknown is the honest status.", ["son55:E008", "son55:E009"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01-step5", "son55", "partial",
               "Verified: incremental vs full-replacement vs StatInit-only (Table 5); single run.", ["son55:E016"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: names the shared static policy prompt, which overlaps i2Agent's strategy reflection.",
               ["son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: chosen vs unchosen contrast with one positive; unchosen does not mean disliked.",
               ["son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "partial",
               "S4 also asks for forgetting or bounds once the store grows. Entries are 'never deleted outright', and "
               "the appendix example injects a low-confidence item despite the medium threshold. Delta edits and "
               "demotion give partial. son55's met overlooked the missing bound.", ["sol:E004", "sol:E012"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
               "Verified: a confidence threshold for injection, not a utility gate; no rollback.", ["son55:E006"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: the paper's own i2Agent description and the preference-profile skill content weaken "
                "the how/what premise.", ["son55:E003", "son55:E005"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 2,
                "See ratings.E.measurement: the sampled 1+9 protocol and unstated baseline provenance keep this at 2.",
                ["son55:E010", "son55:E029"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims.C1.counterevidence", "sol_value": "exclusive attribution called 'too strong'",
             "son55_value": "exclusive attribution unsupported (no listwise-only arm)",
             "final_value": "exclusive attribution contradicted by the paper's own Table 4",
             "reason": "Both seats treated exclusivity as merely unsupported. The w/o-listwise row shows listwise "
                       "carries about half of the GoodReads H@1 gain over MemRec (opus:O01). The claim is "
                       "contradicted, not just untested. E.causality is unchanged (already 2).",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text with appendices first. Initial view: in "
                                                   "scope; retained (frozen after warmup, store-off). Concerns: "
                                                   "listwise confound, preference-profile content vs 'policy', 1+9 "
                                                   "sampled evaluation, unverifiable p<0.05. G 2, M 3, X 3, Em 2, "
                                                   "Ec 2, Eh 2, Es 1, cost 1.",
            "integrity_checks": "Both seats a1 on 2604.14972v2, material sha 69c473cf…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: on InstructRec 10-candidate reranking with gpt-4o-mini, "
                                "StatInit + two rounds of incremental evolution + slim injection + listwise beats "
                                "MemRec H@1 by 1.9–14.9% relative. Feedback evolution adds 0.7–2.9 H@1 points over "
                                "StatInit-only. claim_support scoped.",
            "rating_agreement": "M, X, Ec, Eh, Es and cost agree (re-checked). G → son55, Em → son55. Final 57.5.",
        },
    }

    # =========================================================== 2604.15034 Autogenesis (Δ1.25)
    p = "2604.15034"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "sol's ruling. Prompts, agents, tools, environments and memory policies become versioned, "
                      "evolvable resources (a fixed component of the agent pipeline turned into a design variable). "
                      "That is the run convention for harness editors: r01b, r03b SICA, r10a, r11a ReCreate, r13b "
                      "Meta-Harness, r14b SkillClaw. son55's unify_into_shared_representation (its own fit: weak) "
                      "concerns mapping heterogeneous inputs into one model representation, not one management "
                      "interface. decompose_and_delegate describes the AGS planner–specialist host, which is not the "
                      "contribution.",
            "matches": [smatch("sol", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]),
                                                "son55"),
                           "revision_proposals": []},
        "pattern_mapping": [
            pmap("sol", p, 0),
            PM("generative_process_redesign", "evidence_gated_retention", "H30",
               "Candidates stay out of the active binding until evaluated. Commit registers a version with provenance, "
               "and new tools and agents are added to the registry.",
               "H30 needs measured marginal-gain admission and retirement under a size bound. Here admission is "
               "same-backbone self-assessment, with no retirement and no bound: the card's F1 'infrastructure "
               "offered as the gate' (fit low).",
               ["son55:E004", "son55:E005", "son55:E026", "son55:E030"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.15034-1"): "local:2604.15034-6",
                    ("sol", "local:2604.15034-3"): "local:2604.15034-1",
                    ("sol", "local:2604.15034-4"): "local:2604.15034-7"},
            overrides={
                "local:2604.15034-1": {
                    "status": "partial",
                    "reason": "Opus: matched primary opportunities for reasoning, with 52–61% more output tokens. "
                              "GAIA and coding have no matched or variant cost.",
                    "note": "Merged here from sol:local:2604.15034-3 (cost). A4 collision: sol's local-1 moved to "
                            "local-6."},
                "local:2604.15034-2": {
                    "status": "unmet",
                    "reason": "Opus: no committed version is evaluated on later tasks. Authors disclaim cross-task "
                              "transfer, and resets do not cover every registry (sol's isolation point)."},
                "local:2604.15034-6": {
                    "reason": "Opus: verified. Python facades, optional adapters and the memory restore path are "
                              "described without claiming identical native APIs.",
                    **renum("sol:local:2604.15034-1")},
                "local:2604.15034-7": {
                    "reason": "Opus: verified. Three GPT-4o runs with counts and SD; no CI or test; single runs "
                              "elsewhere.",
                    **renum("sol:local:2604.15034-4")},
                "rs:unify_into_shared_representation/RE-1": dropped_card("unify_into_shared_representation"),
                "rs:unify_into_shared_representation/RE-2": dropped_card("unify_into_shared_representation"),
                "rs:unify_into_shared_representation/RE-3": dropped_card("unify_into_shared_representation"),
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, [],
                             evidence_level="task",
                             claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The gap (no shared lifecycle for heterogeneous resource "
                   "updates) is clear, and Appendix E.1 compares neighbours carefully. It is an interface-level gap: "
                   "no observable failure caused by lacking a unified contract is shown, and EvoAgentX, Alita, GEPA "
                   "and AFlow already retain candidates or artifacts, as the paper concedes. sol's 3 credited the "
                   "neighbour table without a demonstrated residual bottleneck.",
                   ["son55:E001", "son55:E002", "son55:E003", "sol:E013"], ["son55:E029"]),
            "M": R("resolved", 2, "Opus sides with son55. The invariants (proposal and assessment leave active "
                   "bindings unchanged; only accepted commits publish; publication is separate from binding) are "
                   "reconstructible. But the acceptance step in the evaluated reasoning runs is a same-backbone "
                   "satisfaction flag ('can be wrong'). The protocol makes no testable prediction that separates it "
                   "from per-resource management, and the authors disclaim that isolation. sol's 3 credited the "
                   "specification, which X already rewards.",
                   ["son55:E004", "son55:E005", "son55:E037", "sol:E002", "sol:E005"], ["son55:E024", "son55:E030"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Records, markers, version lineage, binding scope, "
                   "restore boundaries, rejection semantics and cost/failure boundaries are specified in detail and "
                   "honestly. Rollback is never exercised (all cases accepted), and there is no retirement rule or "
                   "measured admission.",
                   ["son55:E004", "son55:E032", "son55:E033", "sol:E003", "sol:E004", "sol:E007"],
                   ["son55:E026", "son55:E031"]),
            "E.measurement": R("resolved", 3, "Opus sides with son55. GPQA/AIME exact scoring, the GAIA official "
                               "evaluator and the LeetCode judge are external, trustworthy verifiers. Self-assessment "
                               "is kept separate from scoring (Table 6), and the authors flag non-pairable efficiency "
                               "aggregates themselves. Not 4: HLE uses an o3-mini judge with no evolution control, "
                               "and the lifecycle's own properties (commit correctness, restore) are shown only by "
                               "cases. sol's lifecycle-reliability point is a causal/coverage gap, scored in "
                               "E.causality.",
                               ["son55:E005", "son55:E016", "son55:E018", "son55:E021", "sol:E015"], ["son55:E015"]),
            "E.causality": R("resolved", 2, "Opus sides with son55. Reasoning has three-run, opportunity-matched "
                             "Vanilla/SC/Bo3/Simple-Reflection controls. Simple Reflection is exactly refinement "
                             "without resource updates, and Joint beats it (59.09 vs 54.04 GPQA; 12/90 vs 9/90 "
                             "AIME25). Not higher: about 50–60% more output tokens, no protocol or gate ablation (the "
                             "authors disclaim isolation), and GAIA and coding have only Vanilla vs Evo with extra "
                             "attempts.",
                             ["son55:E009", "son55:E010", "son55:E011", "sol:E008"],
                             ["son55:E022", "son55:E024", "son55:E029"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Reasoning feedback is label-free and labels are "
                           "used only for scoring, which suits the within-task claim. GAIA has a test split. Coding "
                           "uses hidden-judge verdicts as both feedback and score (an oracle retry, which the paper "
                           "discloses). No committed version is tested on later tasks.",
                           ["son55:E005", "son55:E006", "sol:E009"], ["son55:E020", "son55:E021", "son55:E024"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): three repeated GPT-4o runs with counts and SD "
                              "and an honest denominator note. No CI or test; other tables are single runs.",
                              ["son55:E034", "son55:E035", "son55:E012", "sol:E008"], ["son55:E007", "son55:E014"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Per-method output tokens (with the +52–61% stated) and "
                        "aggregate per-benchmark steps, time and USD are reported, and the paper does not claim "
                        "equal compute. But the headline GAIA Vanilla→Agent-Evo gain (79.07→89.04) and coding have no "
                        "per-variant cost, and input tokens are absent. This is the Meta-Harness r13b E.cost-2 "
                        "pattern.",
                        ["son55:E011", "son55:E027", "sol:E008"], ["son55:E028"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v6 text including Appendices A–G read. In scope (system_method; A3 bullet 2): the "
                  "evaluated objects are non-weight resources (prompts, tools, agents, environments, memory) edited "
                  "from execution feedback and committed as versions. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 2–9 (HLE leaderboard, boxplots, coding curves, case panels) are image-only. "
                             "Tables 1–5 and the text carry the numbers used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "Run convention for frameworks that make harness components editable (see rs_pattern.reason). "
                "unify_into_shared_representation is about a shared model representation, not a management "
                "interface; son55 itself rated the fit weak.", ["sol:E001", "son55:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["generative_process_redesign", None]],
                "decompose_and_delegate describes the AGS planner–specialist host, not the paper's contribution "
                "(son55: 'not the main contribution').", ["son55:E016"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["attribute_and_patch_incumbent", "H12"], ["evidence_gated_retention", "H30"]],
                "The paper's core object is the propose → assess → commit lifecycle with provenance. H30 is kept with "
                "fit low because its operation (admission before activation, versioned provenance) is executed while "
                "the measured-gain and retirement conditions fail, as the card's F1 describes.",
                ["son55:E004", "son55:E030"], NOSCORE),
            XC(p, "local:2604.15034-1", "son55", "partial",
               "A4 collision: sol's local-1 (implementation honesty) differs from son55's local-1 (compute "
               "matching). Final local-1 is compute matching, partial. sol's cost question (local-3) is merged here; "
               "sol's local-1 moves to local-6 (met).", ["son55:E011", "son55:E028"]),
            XC(p, "local:2604.15034-2", "son55", "unmet",
               "Same theme in both seats. The final question is 'do committed versions help later tasks?': unmet "
               "(authors disclaim transfer). sol's reset/isolation partial is subsumed.",
               ["son55:E024", "son55:E033"]),
            XC(p, "local:2604.15034-3", "son55", "unmet",
               "A4 collision: sol's local-3 (cost) moves to local-1. Final local-3 is son55's question (coding judge "
               "verdicts as both feedback and score; contamination not excluded), unmet.",
               ["son55:E020", "son55:E021"]),
            XC(p, "local:2604.15034-4", "son55", "unmet",
               "A4 collision: sol's local-4 (statistics) moves to local-7 (partial). Final local-4 is son55's "
               "rollback question: unmet, since all cases are accepted updates.", ["son55:E026"]),
            XC(p, "local:2604.15034-5", "sol", "partial",
               "Measurement (sol only). Verified: final correctness and hidden judges are meaningful; "
               "self-assessment does not certify gains.", ["sol:E007", "sol:E015"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "Verified: target ablations exist, but there is no ablation that holds editor, feedback and budget "
               "fixed while removing the management layer.", ["sol:E008", "son55:E029"]),
            XC(p, "rs:unify_into_shared_representation/RE-1", "son55", "unmet",
               "Kept as a check question (card not retained). Verified: authors do not isolate resource management.",
               ["son55:E024"]),
            XC(p, "rs:unify_into_shared_representation/RE-2", "son55", "partial",
               "Kept as a check question. Verified: SR/SC/Bo3 skeptic baselines for reasoning only.", ["son55:E009"]),
            XC(p, "rs:unify_into_shared_representation/RE-3", "son55", "partial",
               "Kept as a check question. Verified: five backbones and four benchmarks for the update strategy; the "
               "five-type lifecycle rests on three selected cases.", ["son55:E025"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "unmet",
               "Verified: for reasoning the validator is the same backbone as the proposer (failure mode present).",
               ["son55:E005"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "Verified: real resource patches in cases; no cross-task holdout and no recovery test.",
               ["sol:E010", "sol:E011"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12-step4", "son55", "unmet",
               "Verified: gains are within-task, and coding verdicts are both feedback and score.",
               ["son55:E023", "son55:E020"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "Verified: no regression check; acceptance rests on the satisfaction flag.", ["son55:E030"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met",
               "Verified: reflection reads raw traces and the assessment history.", ["son55:E004", "sol:E006"]),
            XC(p, "rsi:evidence_gated_retention/F1", "son55", "partial",
               "Verified: there is an evaluate-before-commit step, but it is self-assessed. Infrastructure dominates "
               "evidence (failure partly present).", ["son55:E030", "son55:E031"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Verified: commit uses self-assessment with no counterfactual.", ["son55:E005"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Verified: admission without retirement or size bound; restore is not retirement.", ["son55:E032"]),
            XC(p, "rsi:evidence_gated_retention/S3", "son55", "unmet",
               "Verified: no demonstration that ungoverned accumulation degrades.", ["son55:E025"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "partial",
               "Verified: commit is separable, but no gate ablation is run.", ["son55:E004"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial",
               "Verified: system cost and output tokens are reported, but not gate-specific or matched.",
               ["son55:E027", "son55:E028"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: an interface-level gap with no demonstrated failure from its absence; neighbours "
                "partly cover it.", ["son55:E002", "son55:E029"], "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the load-bearing acceptance step is a same-model satisfaction flag, with no "
                "distinguishing prediction.", ["son55:E005", "son55:E030"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 3,
                "See ratings.E.measurement: the external verifiers are sound; lifecycle reliability is a causal gap.",
                ["son55:E016", "son55:E018"], "+2.5 vs sol (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 2,
                "See ratings.E.causality: Simple Reflection is a direct no-resource-update control at matched "
                "opportunities. sol's 1 treated the missing protocol isolation as if no control existed.",
                ["son55:E009", "son55:E010"], "+3.75 vs sol (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 2,
                "See ratings.E.cost: the headline GAIA comparison has no per-variant cost (Meta-Harness r13b = 2).",
                ["son55:E028", "sol:E008"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v6 text with appendices first. Initial view: in "
                                                   "scope (non-weight resources); task level, since every gain is "
                                                   "within-task revision with a self-assessment gate. G 2, M 2, X 3, "
                                                   "Em 3, Ec 1–2, Eh 2, Es 2, cost 2.",
            "integrity_checks": "Both seats a1 on 2604.15034v6, material sha 8fc26b0c…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: within-task prompt and solution editing with a "
                                "propose/assess/commit loop beats opportunity-matched Simple Reflection on GPT-4o "
                                "reasoning at 50–60% more output tokens. The protocol records and reuses accepted "
                                "updates in three selected cases. Cross-task value of committed versions and "
                                "protocol-level benefit are not shown. claim_support scoped.",
            "shared_error_review": "Agreed items (X 3, Eh 2, Es 2, evidence_level task) re-checked. E.holdout 2 is "
                                   "kept: the label-free reasoning evidence fits the within-task claim, and the "
                                   "coding oracle retry is disclosed by the authors.",
            "rating_agreement": "X, Eh and Es agree. G, M, Em and Ec → son55; cost → sol. Final 57.5.",
        },
    }

    # =========================================================== 2604.15676 EvoRAG (Δ1.25)
    p = "2604.15676"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Compared to KG-RAG frameworks, EvoRAG achieves an average improvement of",
                    "§VI-B; Table III",
                    "The 7.34% is the mean over MRAG, LRAG and KRAG. Against the strongest KG-RAG framework per "
                    "dataset (Table III ACC): RGB 84.00 vs 76.00 (+8.00), MTH 80.26 vs 76.20 (+4.06), HPQ 48.16 vs "
                    "44.83 (+3.33), mean 5.13. Including the KGR variants, MTH's best is CAGED 76.72 (+3.54).",
                    kind="our_inference"),
            opus_ev(p, "O02", "The training set is constructed by generating additional query–answer pairs within "
                              "the subgraphs retrieved based on the test queries.",
                    "§VI-A Training and test set construction",
                    "The test queries choose where training feedback is collected, and only EvoRAG receives it. "
                    "Baselines and KGR variants see no training queries. Triplet overlap between training paths and "
                    "test reasoning paths is not quantified.", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["relax_discrete_search_to_continuous"],
            "outside_taxonomy": False,
            "reason": "Revised. Primary generative_process_redesign (sol; run convention for liberated harness "
                      "components): the static KG of the KG-RAG pipeline becomes a feedback-updated design variable. "
                      "Supporting relax_discrete_search_to_continuous (son55's match, sub null; C22 needs a unified "
                      "search space over hand-engineered designs, not present). Discrete top-M path selection is "
                      "relaxed to softmax path priorities over continuous triplet scores, which are optimized by the "
                      "gradient of expected utility (Eq. 2–9) and then thresholded into fusion and suppression; "
                      "r01b Symbolic Learning precedent. Not self_supervised_signal_engineering/C26: default feedback "
                      "uses reference answers, and C26 optimizes a model with a preference objective (son55: fit "
                      "weak). Not reframe_as_solvable_object: no correspondence to the original credit problem is "
                      "claimed; convergence is to a stationary point of the proxy.",
            "matches": [smatch("sol", p, "generative_process_redesign"),
                        smatch("son55", p, "relax_discrete_search_to_continuous", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "evidence_gated_retention", "H29"),
                                       dmatch("sol", p, "attribute_and_patch_incumbent", "H09"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H04")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            pmap("sol", p, 0),
            PM("relax_discrete_search_to_continuous", "attribute_and_patch_incumbent", "H09",
               "Response-level feedback becomes path utility, which is propagated backward to every triplet on the "
               "retrieved paths, so each component receives its own credit.",
               "H09 propagates natural-language critiques across prompts and tools; here the components are KG "
               "triplets and the credit is a numeric gradient (partial operation transfer, medium fit).",
               ["sol:E01", "sol:E03", "sol:E05", "sol:E21"]),
            PM("generative_process_redesign", "index_experience_for_reuse", "H04",
               "Shortcut edges link the endpoints of high-utility multi-hop paths, and low-utility triplets are "
               "softly down-weighted. The store's structure is reorganized for multi-hop recall.",
               "H04's claim rests on index design; here structure changes are driven by feedback credit, without "
               "versioning or size bound (fit medium/low).",
               ["son55:E013", "son55:E015", "son55:E035"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.15676-1"): "local:2604.15676-4",
                    ("sol", "local:2604.15676-3"): "local:2604.15676-5",
                    ("sol", "rsi:evidence_gated_retention/H29"): "rsi:evidence_gated_retention/H29-step5"},
            overrides={
                "local:2604.15676-2": {
                    "status": "unmet",
                    "reason": "Opus: same statistics question in both seats. No CI, variance or seeds for any main "
                              "result; the training query count is not given; the μ±σ thresholds are called "
                              "'statistically significant' with no test."},
                "local:2604.15676-4": {
                    "reason": "Opus: verified. Feedback–truth agreement, EM/F1 and human feedback are given; ACC "
                              "(contains answer) is lenient.",
                    **renum("sol:local:2604.15676-1")},
                "local:2604.15676-5": {
                    "reason": "Opus: verified. Static-base-KG scope is stated honestly; random-flip noise and cold "
                              "start do not cover real fact maintenance.",
                    **renum("sol:local:2604.15676-3")},
                "rsi:evidence_gated_retention/H29-step5": {
                    "status": "partial",
                    "reason": "Opus: SG → FB value ablation on different (test) queries, but the training regions "
                              "are located by the test queries (opus:O02).",
                    **moved("sol:rsi:evidence_gated_retention/H29")},
                "rsi:evidence_gated_retention/S5": {
                    "status": "met",
                    "reason": "Opus: the gate's online cost is stated openly (backprop 23.90% of runtime at batch 20; "
                              "1.12× KRAG latency). The training-phase total is a separate gap (E.cost, SSE RE-5)."},
                "rs:self_supervised_signal_engineering/RE-1": dropped_card("self_supervised_signal_engineering"),
                "rs:self_supervised_signal_engineering/RE-2": dropped_card("self_supervised_signal_engineering"),
                "rs:self_supervised_signal_engineering/RE-3": dropped_card("self_supervised_signal_engineering"),
                "rs:self_supervised_signal_engineering/RE-5": {
                    "status": "partial",
                    "reason": "Opus (revised from met): per-query online overhead is justified, but the loop's total "
                              "training cost (generated queries, evaluator calls, iterations) is not reported.",
                    **dropped_card("self_supervised_signal_engineering")},
                "rs:self_supervised_signal_engineering/RE-6": {
                    "status": "unmet",
                    "reason": "Opus (revised from partial): RE-6 names 'access to test-set information' as an "
                              "unrealistic assumption, and the training set is generated from subgraphs retrieved "
                              "for the test queries (opus:O02).",
                    **dropped_card("self_supervised_signal_engineering")},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": assess("sol", p, [
            "Opus: the headline 7.34% averages over three baselines; vs the strongest framework per dataset the gain is "
            "+8.00/+4.06/+3.33 ACC (opus:O01)."],
            evidence_level="retained",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A concrete fixed object (static triplet priorities and "
                   "structure). An error analysis puts IF/LP/OI above half of errors (17.9/20.7/14.1%). Neighbours "
                   "(KG-RAG frameworks, KG refinement, model-level feedback) are named. Not 4: utility-valued memory "
                   "and feedback-trained retrievers are not discussed, and the error-labelling protocol is unstated.",
                   ["sol:E01", "sol:E22", "son55:E003", "son55:E004", "son55:E037"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Feedback → path utility (with the Fidelity/Conflict gate) → "
                   "expected-utility loss → triplet scores → hybrid retrieval and fusion/suppression is reconstructible "
                   "and targets IF/LP/OI. LLM path utility is a proxy, not causal credit.",
                   ["sol:E01", "sol:E03", "sol:E04", "sol:E05", "son55:E008"], ["son55:E013"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Initialisation, learning rate, thresholds, the BFS fusion "
                   "algorithm, soft suppression, read path and the static-KG boundary are explicit. Versioning, "
                   "rollback, a size bound and the training query volume are missing.",
                   ["sol:E04", "sol:E05", "sol:E06", "sol:E07", "sol:E08"], ["son55:E014"]),
            "E.measurement": R("resolved", 3, "Opus sides with sol. ACC/EM/F1 move in the same direction, with clear "
                               "denominators (300/816/600). Feedback–truth agreement is measured (Table II, 93.38%), "
                               "and human and F1 feedback are run as alternatives. ACC (contains answer) is lenient, "
                               "but EM/F1 corroborate. son55's other grounds belong elsewhere: evaluator truth access "
                               "and the 7.34% averaging go to holdout/claim scope (opus:O01), and manual triplet "
                               "annotation affects only a secondary claim.",
                               ["sol:E02", "sol:E12", "sol:E15", "son55:E019", "son55:E021"],
                               ["son55:E023", "opus:O01"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. SG → FB → evolution ablations, the cross-"
                             "validation gate ablation, feedback-source and noise experiments, and transfer to "
                             "MRAG/LRAG. Baselines receive no training queries or feedback, and there is no simple "
                             "feedback-count alternative, so privileged training data is not separated from the "
                             "specific credit mechanism.",
                             ["sol:E11", "sol:E13", "sol:E14", "son55:E027", "son55:E028"],
                             ["son55:E022", "opus:O02"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. Test queries differ from training queries and are "
                           "evaluated after training. But the training set is generated inside the subgraphs retrieved "
                           "for the test queries (opus:O02): a test-located, transductive construction. Triplet "
                           "overlap is unquantified, there is no out-of-region test, and N/M are chosen on accuracy. "
                           "The large-scale and multi-backbone runs reuse the same construction. son55's 2 credited "
                           "query separation without weighing the test-located regions.",
                           ["sol:E09", "sol:E10", "son55:E017", "opus:O02"], ["son55:E031", "son55:E033"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes and noise-injection degradations "
                              "are reported. No CI, variance or seeds; μ±σ thresholds are called 'statistically "
                              "significant' with no test.", ["sol:E15", "sol:E16", "sol:E18"], ["son55:E013"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Inference-side reporting is rich: prompt length, TTFT, "
                        "GPU memory, backprop share and 1.12×/1.27× latency. The training-phase budget is missing "
                        "(generated query count, evaluator calls, iterations), and baselines get no training budget. "
                        "The efficiency claim charges inference only (SEDM r07a = 2).",
                        ["sol:E17", "sol:E18", "son55:E029", "son55:E030"], ["opus:O02"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read (no appendix). In scope (system_method): non-weight KG state "
                  "(triplet contribution scores, shortcut edges) is updated from response feedback, retained and "
                  "read by later retrieval. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree: retained KG retrieval state is a memory/retrieval component, not "
              "model weights)",
        "figure_dependence": "Figures 3 and 7–20 are image-only. Only values stated in the text (e.g. 6.6%, 3.07%, "
                             "2.24%, 0.75%, 1.15/2.43%, 23.90%, 1.12×, 8.25%) and Tables I–IV are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "See rs_pattern.reason: liberation of the static KG is the problem framing and follows the run "
                "convention. C26/SSE assumes manufactured supervision without labels and optimizes a model.",
                ["sol:E01", "sol:E08", "son55:E006"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["relax_discrete_search_to_continuous", None]],
                "Keep sol's primary and son55's relaxation match, which captures the expected-utility gradient over "
                "relaxed path selection. Drop reframe_as_solvable_object (no correspondence result) and "
                "self_supervised_signal_engineering/C26 (labelled feedback, not model preference optimization).",
                ["sol:E05", "son55:E005", "sol:E21"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["evidence_gated_retention", "H29"], ["attribute_and_patch_incumbent", "H09"],
                 ["index_experience_for_reuse", "H04"]],
                "Union. H29 (both): entry utility drives ranking and demotion. H09 (sol): response feedback is "
                "propagated back to per-component credit, the paper's named mechanism. H04 (son55): relation fusion "
                "adds shortcut edges and suppression reshapes the store for multi-hop recall (contribution 2).",
                ["sol:E03", "sol:E05", "son55:E013", "son55:E035"], NOSCORE),
            XC(p, "local:2604.15676-1", "son55", "unmet",
               "A4 collision: sol's local-1 (measurement) moves to local-4 (partial). Final local-1 is son55's "
               "out-of-region question: unmet, with no region-external or shift test and unquantified overlap.",
               ["son55:E016", "opus:O02"]),
            XC(p, "local:2604.15676-2", "son55", "unmet",
               "Same statistics question in both seats. No main-result uncertainty at all; sol's partial credited "
               "sample sizes and noise runs, which E.statistics already counts at tier 1.", ["son55:E013", "sol:E15"]),
            XC(p, "local:2604.15676-3", "son55", "unmet",
               "A4 collision: sol's local-3 (static-KG scope / noise realism) moves to local-5 (partial). Final local-3 "
               "is son55's: baselines get no equal training exposure, and the 7.34% is an average over baselines "
               "(opus:O01). Unmet.", ["son55:E022", "opus:O01"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "met",
               "Kept as a check question (card not retained). Verified: three datasets plus large scale, four LLMs, "
               "evaluator sizes, MRAG/LRAG.", ["son55:E031", "son55:E032", "son55:E033"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "partial",
               "Kept as a check question. Verified: SG/FB ablation, but no equal-exposure or counting baseline.",
               ["son55:E027", "son55:E022"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "met",
               "Kept as a check question. Verified: ACC/EM/F1 reported directly.", ["son55:E021"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "revised", "partial",
               "The loop's total training cost is not reported. son55's met credited per-query overhead only.",
               ["son55:E030", "opus:O02"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "revised", "unmet",
               "The card names access to test-set information as the unrealistic assumption to avoid. Training "
               "queries are generated from test-query subgraphs (opus:O02). son55's partial weighed only the "
               "evaluator's truth access.", ["opus:O02", "son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "sol", "met",
               "Verified: response → path → triplet local credit (Eq. 2–9).", ["sol:E01", "sol:E05"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "sol", "partial",
               "Verified: F/C gate, clipping and soft recovery; no regression gate or version rollback for new edges.",
               ["sol:E04", "sol:E06", "sol:E07"]),
            XC(p, "rsi:evidence_gated_retention/F5", "son55", "partial",
               "Verified: utility mostly reweights retrieval and nothing is deleted, but shortcut edges change "
               "content (failure partly present).", ["son55:E015", "sol:E07"]),
            XC(p, "rsi:evidence_gated_retention/H29", "revised",
               {"moved_to": "rsi:evidence_gated_retention/H29-step5", "status": "partial"},
               "sol's H29 check is the card's step 5 (value ablation plus holdout). Merged; partial in both.",
               ["sol:E09", "son55:E016"]),
            XC(p, "rsi:evidence_gated_retention/H29-step5", "son55", "partial",
               "Verified: SG → FB on test queries, with training located by the test queries. sol's H29 is merged "
               "here.", ["son55:E027", "opus:O02"]),
            XC(p, "rsi:evidence_gated_retention/H30-step4", "son55", "unmet",
               "Verified: no versions, rollback, size bound or retirement.", ["son55:E015"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "partial",
               "Verified: shortcut admission and soft demotion; no hard bound or deletion.", ["son55:E013"]),
            XC(p, "rsi:evidence_gated_retention/S3", "son55", "met",
               "Verified: the silent failure (IF/LP/OI) is quantified before the method, and its reduction is shown "
               "(83.01% of problematic triplets suppressed on RGB; manual annotation, protocol unstated).",
               ["son55:E003", "son55:E024"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "met",
               "S5 asks that the gate's cost be stated openly: backprop share and end-to-end latency versus KRAG/MRAG "
               "are reported. The missing training total is scored in E.cost and SSE RE-5.",
               ["son55:E030", "sol:E17"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 3,
                "See ratings.E.measurement: verifiers and denominators are sound. son55's grounds belong to holdout "
                "and claim scope.", ["sol:E12", "son55:E019"], "+2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", 1,
                "See ratings.E.holdout: the training set is located by the test queries (opus:O02).",
                ["opus:O02", "sol:E09"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 2,
                "See ratings.E.cost: the training-phase budget is missing and baselines are unequal (SEDM r07a = 2).",
                ["sol:E17", "son55:E030"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.strongest_supported_claim (sol)", "sol_value": "7.34% kept as author report",
             "son55_value": "3.3–8.0 points vs the strongest baseline per dataset",
             "final_value": "+8.00/+4.06/+3.33 ACC vs the strongest KG-RAG framework per dataset (mean 5.13)",
             "reason": "The final uses sol's assessment, which repeats the author's averaged figure. son55's narrower "
                       "figure is verified and made exact (opus:O01).",
             "evidence_ids": ["opus:O01", "son55:E020"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first. Initial view: in scope (KG retrieval "
                                                   "state); retained, transductive. Key issue: the training set is "
                                                   "generated from test-query subgraphs and baselines get no training. "
                                                   "G 3, M 3, X 3, Em 3, Ec 2, Eh 1, Es 1, cost 2.",
            "integrity_checks": "Both seats a1 on 2604.15676v2, material sha 12db744a…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: after feedback training on queries generated in the "
                                "test-query hotspot regions, learned triplet scores plus relation evolution raise "
                                "test ACC by +3.3 to +8.0 over the strongest untrained KG-RAG framework per dataset, "
                                "with consistent direction across feedback sources, backbones and a 5,000-query "
                                "setting. Out-of-region generalization is not shown. claim_support scoped.",
            "rating_agreement": "G, M, X, Ec and Es agree. Em, Eh and cost → sol. Final 62.5.",
        },
    }

    return S
