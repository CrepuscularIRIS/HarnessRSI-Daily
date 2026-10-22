"""Opus rulings for r14b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat-input integrity: all ten a1 seat records match conflicts.json seat_record_hashes and the batch "
        "manifest (input_hash f1e0164c…, per-paper version and material sha256). No controller action needed.",
        "2604.05149 EvolveRouter (Δ6.25): final 68.75 (= sol). G → sol 3 (lineage to AgentRouter is explicit, the "
        "residual against HiveMind/MAPRO/MASS is stated in App. A.2; the 'first framework' wording is overclaim but "
        "the bottleneck is shown in Fig. 1/Tables 5–6). E.holdout → sol 3 (500/100/100 disjoint split; candidate "
        "selection, rounds and K-thresholds all on validation; transfer failure reported). RS → "
        "generative_process_redesign primary + heterogeneous_decomposition supporting. Shared omission recorded "
        "(no rating change): Table 7's EvolveRouter NGQA row (53.28) copies the PO-Round-3 row and contradicts "
        "Tables 3/8 (54.04).",
        "2604.07645 PRIME (Δ8.75): final 33.75 (= son55). G → son55 1 ('training-free / frozen model' is the "
        "background the spec excludes as a gap; no residual against experience-memory agents). M → son55 2 (the "
        "credit-assignment step degenerates to positional key turns under the 'Equalized' credit used for "
        "IntentionGym/TravelGym; no distinguishing prediction against plain reflective memory). Evaluation "
        "protocol absent (holdout/statistics not_reported). The abstract's 'competitive with gradient-based "
        "methods' is contradicted by Table 1: GRPO is higher in all 16 matched cells. son55's "
        "challenged_with_evidence on local-3 corrected to unmet.",
        "2604.08377 SkillClaw (Δ1.25): final 47.5 (= sol). E.holdout status → son55 (resolved 0: the paper states "
        "that validation tasks come from the same day's benchmark interactions). E.cost → sol not_reported 0 "
        "(qualitative 'additional token cost' only; PsychAgent r13b convention). RS → sol generative_process_redesign "
        "(EvoSkill r11b / MemSkill r10b convention); domain → H02 + H11 + H30. Opus finding: Safety's whole +8.00 "
        "and Search's last +4.55 arise from same-pool retests, and the Social series is carried forward unchanged; "
        "Table 3 is a running-best readout on the selection tasks. Per A2 this is charged once, under E.holdout.",
        "2604.08618 SkillForge (Δ11.25): final 53.75 (= son55). G → son55 2 (the 'no systematic mechanism' premise "
        "is contradicted by skill-evolution work the paper itself cites, e.g. Steve-Evolving; residual is the "
        "enterprise reference-reply setting). X → son55 2 (every rewrite is committed as Skill_v_n+1 with no "
        "acceptance test, regression check or rollback). E.measurement → son55 2 (LLM judge validated on an "
        "unsized sample, same judge selects bad cases, judge and Analyzer share style targets, only Δ reported). "
        "RS → generative_process_redesign primary + decompose_and_delegate/C25 supporting; domain → H11 + H02.",
        "2604.09297 SkillMOO (Δ6.25): final 52.5 (between seats: sol 51.25, son55 57.5). E.measurement → sol 2 "
        "(Opus finding: the stated binary per-run pass definition is inconsistent with cells such as 0.89±0.03 and "
        "0.99±0.01, which ten binary runs cannot produce). E.holdout → revised resolved 0 (selection and reporting "
        "on the same task verifier; disclosure is not holdout evidence; SkillClaw convention). E.statistics → "
        "son55 3 (10 independent search runs with SD, Scott-Knott ESD, zero-pass tasks disclosed). The abstract's "
        "'+42pp' is traceable (Task 6, 0.42 vs 0.00, under the RQ1 'larger skill bundles' qualifier); son55's "
        "'does not match Table 2' is corrected to partial.",
        "A4 hygiene: hidden local-ID collisions handled in 05149, 07645, 08377, 08618 and 09297; every merge, move "
        "and renumbering is recorded in the affected expectation's note and in the resolution of the conflicting ID.",
        "Figure dependence: EvolveRouter Figs 1/3/4, PRIME Figs 3–4 and SkillClaw Figs 1–5 are image-only; only "
        "values stated in the text or tables are used. PRIME's GPU-hour ratio and transfer gains are taken from the "
        "text, not read off the bars.",
        "No material requests. Seats' requests for neighbour originals (MASS/HiveMind/AgentRouter, Reflexion/UserRL, "
        "SkillRL/EvoSkill/MemSkill/WildClawBench, TextGrad/EvoSkills, SkillsBench) are non-blocking: no disputed "
        "rating depends on them.",
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

    def pm(s, p, idx=None):
        maps = seat(s, p)["pattern_mapping"]
        if idx is not None:
            maps = [maps[i] for i in idx]
        return [prefix(copy.deepcopy(m), s) for m in maps]

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

    def merged(other, extra_ev=()):
        return {"note": f"{other} merged here (A4: same question under a colliding or different ID).",
                "merged_from": other, "merged_evidence_ids": list(extra_ev)}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def sol_ev(p, eid):
        return [f"sol:{x}" for x in next(e for e in seat("sol", p)["expectations"] if e["id"] == eid)["evidence_ids"]]

    SCOPE_FULL = "full pinned text incl. all appendices and tables read by Opus"

    # =========================================================== 2604.05149 EvolveRouter (Δ6.25)
    p = "2604.05149"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "the full EvolveRouter achieves the best result in each case",
                    "Appendix D.1 (Table 7 discussion)",
                    "Table 7's 'EvolveRouter' NGQA row (53.28 F1 / 9.67 EM) repeats the +PO (Round 3) row of Table 4, "
                    "while Table 3 and the Table 8 in-domain row give 54.04 F1 for the same system. One reported "
                    "headline value is mis-copied; the ordering conclusions do not change.", kind="our_inference"),
            opus_ev(p, "O02", "Among the candidates, we retain the one with the best validation performance.",
                    "Appendix B.1 Targeted validation subset",
                    "Candidate selection uses the validation subset (diagnosed training failures plus validation "
                    "samples); the 100-item test split is not touched by selection."),
            opus_ev(p, "O03", "and the process terminates early when no candidate prompt passes validation or when "
                              "all remaining candidates are frozen",
                    "Appendix B.1 Regression check and multi-round chaining",
                    "The number of PO rounds per dataset (2 or 3 in Table 4) is fixed by validation outcomes, not by "
                    "test results."),
            opus_ev(p, "O04", "Our work differs from these methods in problem formulation.",
                    "Appendix A.2",
                    "The residual against HiveMind/MAPRO/MASS is stated (routing-induced diagnostics choose which "
                    "prompts to refine and the router is retrained on the refined pool), not left implicit."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["heterogeneous_decomposition"],
            "outside_taxonomy": False,
            "reason": "Opus: the paper's first move (§2.2) is to take the prompt set, held fixed by every prior "
                      "router, and make it a jointly optimised variable; Table 4's w/o-PO arm removes exactly that "
                      "liberation. That is generative_process_redesign (sol; sub null: C15/C23/C24 are "
                      "geometry/diffusion/interface tactics). son55's heterogeneous_decomposition is kept as "
                      "supporting, not primary: the role-consistency filter and the severity×router-weight priority "
                      "partition the 24 agents by measured properties (Fig. 1, Tables 5–6) and treat only the top "
                      "partition, and the worst-only arm tests that partition, but this is the target-selection step "
                      "inside the liberation, not the paper's framing.",
            "matches": [smatch("sol", p, "generative_process_redesign"),
                        smatch("son55", p, "heterogeneous_decomposition", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H10")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("sol", p) + pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son, rename={}, drop={("sol", "local:2604.05149-1")},
            overrides={
                "rs:heterogeneous_decomposition/RE-4": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 unmet): the worst-agent-only arm isolates the priority "
                              "criterion against a simpler criterion at the same budget (Table 4, son55:E23), so the "
                              "partition is partly tested. Missing: uniform/random-target and ungated arms, and any "
                              "competing multi-agent prompt optimiser (HiveMind/MAPRO/MASS) at matched budget.",
                    "evidence_ids": ["son55:E12", "son55:E23", "son55:E20"] + sol_ev(p, "local:2604.05149-1"),
                    **merged("sol:local:2604.05149-1 (strong prompt-optimiser control, sol partial)")},
                "local:2604.05149-1": {
                    "status": "unmet",
                    "reason": "Opus: verified; no ungated, random-rewrite or router-only-extra-epochs arm. Final "
                              "local-1 is son55's question; sol's local-1 (competing optimiser) moved to RE-4."},
                "rsi:attribute_and_patch_incumbent/S1": {
                    "status": "met",
                    "reason": "Opus (sol): the role-consistency filter attributes weakness to the prompt rather than "
                              "the backbone, and edits are bounded to 1–3 sentences of the instruction suffix; that "
                              "matches the artifact's unit (one agent's prompt)."},
                "rsi:attribute_and_patch_incumbent/S5": {
                    "status": "partial",
                    "reason": "Opus (son55): the rewriter sees representative failure cases with gold answers and "
                              "aggregated error statistics, not full traces or candidate history."},
            }),
        "claims": lambda c: add_counter(c, "C4", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: Table 7's EvolveRouter NGQA value (53.28) contradicts Tables 3/8 (54.04) (opus:O01).",
            "Opus: NewsQA EM of the full system (41.67) is below w/o Adaptive K (42.00) (sol unresolved item)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus sides with sol. The bottleneck is concrete and shown (Fig. 1 and Tables 5–6: "
                   "prompt choice changes per-agent F1 by role), the immediate parent is explicit (the 'KG Router "
                   "(base)' rows equal AgentRouter), and the residual against HiveMind, MAPRO and MASS is stated "
                   "(opus:O04). Not 4: Table 2's 'first framework' wording overstates the gap and MASS's "
                   "alternating prompt/topology optimisation is only contrasted verbally.",
                   ["son55:E01", "son55:E02", "son55:E22", "son55:E29", "sol:E001", "sol:E013", "opus:O04"],
                   ["son55:E20", "son55:E28"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Failure archive and router weights → reliance-weighted "
                   "priority → bounded rewrites → validation gate → resumed router is reconstructable, with a "
                   "separating prediction (worst-only) and a mechanistic account of resume-vs-scratch. Not 4: the "
                   "premise that cross-backbone weakness is prompt-caused is not tested.",
                   ["son55:E05", "son55:E06", "son55:E12", "son55:E13", "sol:E002", "sol:E003"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. N_max=3, three candidates at fixed temperatures, freeze "
                   "after 3 rejections, prompt-hash cache, checkpoint resume and a 0.03 router revert are specified. "
                   "Not 4: δ is never given, the main-text gate ('no significant regression') and App. C.3 ('does not "
                   "regress') differ from the coded rule, and accepted prompts are never rolled back.",
                   ["son55:E04", "son55:E07", "son55:E08", "son55:E09", "son55:E10", "sol:E004", "sol:E005"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Token F1 and EM against gold answers on "
                               "standard QA sets, no LLM judge. Shared omission recorded (no change): Table 7's "
                               "NGQA value contradicts Tables 3/8 (opus:O01); NGQA EM below 10% for every method "
                               "makes its EM deltas one-item effects.",
                               ["son55:E14", "son55:E30", "sol:E014", "opus:O01"], ["son55:E25"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. w/o-PO, w/o-Adaptive-K, worst-agent-only and "
                             "from-scratch arms are useful. Missing: ungated/random rewrites, a base router given the "
                             "same extra fine-tuning epochs, and a matched-budget competing prompt optimiser.",
                             ["son55:E11", "son55:E12", "son55:E13", "son55:E22", "son55:E23", "sol:E009", "sol:E012"],
                             ["son55:E26", "son55:E20"]),
            "E.holdout": R("resolved", 3, "Opus sides with sol. A disjoint 500/100/100 split per benchmark; candidate "
                           "selection (opus:O02), the number of rounds (opus:O03), Adaptive-K thresholds and router "
                           "reverts all use validation; the failure of cross-benchmark transfer is reported (Table 8), "
                           "which bounds the claim to in-distribution use. son55's 2 charged in-distribution scope "
                           "and test size (an E.statistics matter under A2) and training-gold rewriter input (training "
                           "data, not a leak). Not 4: 100 test items and no contamination check.",
                           ["son55:E14", "son55:E15", "sol:E006", "sol:E010", "opus:O02", "opus:O03"],
                           ["son55:E18"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): three seeds with mean ± std on every cell, "
                              "but 100 test items, no intervals or significance tests, and several PO gains are "
                              "within seed spread.", ["son55:E30", "son55:E11", "sol:E007"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Stage-1 calls (12,000), ~10% incremental cost per "
                        "round and inference calls (24 → 2.9–7.4) are reported; rewriter/validation tokens and a "
                        "budget-matched comparison are absent.",
                        ["son55:E16", "son55:E17", "sol:E011"], ["son55:E26"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text with Appendices A–F read. In scope (system_method): non-weight agent "
                  "prompts are rewritten from execution feedback, gated on validation, retained and used on a "
                  "disjoint test split. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1, 3 and 4 are image-only; only table/text values used (Tables 3–10).",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "The framing operation is liberating the fixed prompt set (§2.2); see rs_pattern.reason.",
                ["sol:E001", "son55:E02"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["heterogeneous_decomposition", None]],
                "sol's card as primary; son55's partition-by-measured-property match kept as supporting because "
                "the target-selection step does partition agents and is tested by the worst-only arm.",
                ["sol:E001", "son55:E04", "son55:E05", "son55:E23"], NOSCORE),
            XC(p, "local:2604.05149-1", "son55", "unmet",
               "A4 collision: sol's local-1 (competing prompt optimiser) and son55's local-1 (ungated/random/extra-"
               "epochs control) are different questions. Final local-1 = son55's, unmet (verified). sol's question "
               "merged into rs:heterogeneous_decomposition/RE-4.", ["son55:E22", "son55:E34"]),
            XC(p, "local:2604.05149-3", "sol", "partial",
               "Statistics (sol only). Verified: three seeds, mean ± std, no CI or test.", ["sol:E007"]),
            XC(p, "local:2604.05149-4", "sol", "partial",
               "Cost (sol only). Verified: call counts and incremental cost given, token/dollar cost absent.",
               ["sol:E011"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "son55", "partial",
               "Kept with the supporting card. Agent-call reduction is a deployment unit; latency and tokens absent.",
               ["son55:E16", "son55:E17"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "partial",
               "Verified: PO and Adaptive K ablated; role filter, multi-candidate sampling, gate and freezing not.",
               ["son55:E11", "son55:E12"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "revised", "partial",
               "son55 wrote unmet. The worst-only arm is a same-budget test of the partition criterion, so the "
               "expectation is partly answered; competing optimisers and uniform/random targets remain missing. "
               "sol's local-1 merged here.", ["son55:E12", "son55:E23", "sol:E009"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "met",
               "Verified: Fig. 1 and Tables 5–6 measure the per-agent heterogeneity before treatment.",
               ["son55:E01"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "met",
               "Verified (met = failure avoided): the gate scores against gold labels, not self-constructed data.",
               ["son55:E07", "son55:E14"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "sol", "met",
               "The prompt is the attributable unit and edits are bounded sentence-level patches; the role filter "
               "does the prompt-vs-backbone attribution. son55's partial asked for section-level attribution "
               "inside a short role prompt.", ["son55:E04", "son55:E06", "sol:E003"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: failure cases plus aggregated statistics, not raw traces.", ["son55:E03", "sol:E003"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", 3,
                "See ratings.G: shown bottleneck, explicit parent and a stated residual; the overclaim keeps it "
                "below 4.", ["son55:E01", "son55:E22", "opus:O04"], "+3.75 vs son55 (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", 3,
                "See ratings.E.holdout: all selection on validation, disjoint test, transfer limit reported; son55's "
                "deductions belong to E.statistics or are not leaks.",
                ["son55:E14", "son55:E15", "opus:O02", "opus:O03"], "+2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "3 (no table-inconsistency note)",
             "son55_value": "3 (no table-inconsistency note)", "final_value": 3,
             "reason": "Shared omission, no rating effect: Table 7's EvolveRouter NGQA row (53.28) copies the "
                       "PO-Round-3 row and contradicts Tables 3/8 (54.04) (opus:O01). Recorded in E.measurement and "
                       "assessment.unresolved.",
             "evidence_ids": ["opus:O01"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text first. Initial view: in scope, retained "
                                                   "(prompts selected on validation, used on a disjoint test). G 2–3, "
                                                   "M 3, X 3, Em 3, Ec 2, Eh 3, Es 2, E.cost 2.",
            "integrity_checks": "Both seats a1 on 2604.05149v1, material sha e13e37cb…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: on five QA benchmarks (100 test items each, 3 seeds), "
                                "diagnostic-guided prompt refinement plus a resumed router beats the same router "
                                "without refinement and the listed routers, and Adaptive K cuts calls 69–88%. "
                                "Superiority over other prompt optimisers is not tested; claim_support scoped.",
            "rating_agreement": "M, X, Em, Ec, Es, E.cost agree and were re-checked; G and Eh → sol. Final 68.75.",
        },
    }

    # =========================================================== 2604.07645 PRIME (Δ8.75)
    p = "2604.07645"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Assigns uniform credit to all turns, treating each action as equally important.",
                    "Appendix D, Credit assignment methods",
                    "Under the 'Equalized' credit used for IntentionGym and TravelGym every turn gets 1.0, so the "
                    "top-K 'key turns' are chosen by position (Fig. 9: 'top-K=3 by position in exploration stage'). "
                    "The credit-assignment step the paper names as a contribution carries no information there.",
                    kind="our_inference"),
            opus_ev(p, "O02", "PRIME achieves competitive performance with gradient-based methods while offering "
                              "cost-efficiency and interpretability",
                    "Abstract", "The central competitiveness claim."),
            opus_ev(p, "O03", "The trade-off is that GRPO achieves higher absolute performance through direct "
                              "parameter updates",
                    "§4.2 Computational Budget",
                    "Conceded in the text; Table 1 shows GRPO above PRIME in all 16 matched cells (4B and 8B × eight "
                    "environments), by wide margins on TravelGym, FunctionGym and TauGym.", kind="our_inference"),
            opus_ev(p, "O04", "the Preference Zone records user behavior patterns that enable personalization",
                    "§3.1 Structuring Interaction Knowledge",
                    "With golden ≥ 0.7, warning ≤ 0.3 and preference in between (Appendix D Table 2), every "
                    "trajectory lands in some zone: admission has no reject path; only scheduled pruning removes "
                    "entries.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning/C03 (retrieved reference substrate conditions a frozen "
                      "policy; no upstream schema training and no category holdout, so the C03 steps are only partly "
                      "executed). Kept as agreed.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "no",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "revision_proposals": []},
        "pattern_mapping": pm("son55", p) + pm("sol", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.07645-3"): "local:2604.07645-5"},
            drop={("sol", "local:2604.07645-1"), ("sol", "local:2604.07645-2")},
            overrides={
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "unmet",
                    "reason": "Opus: verified; no evaluation-episode count, split or overlap analysis anywhere.",
                    "evidence_ids": ["son55:E09"] + sol_ev(p, "local:2604.07645-1"),
                    **merged("sol:local:2604.07645-1 (construction/test split, sol unmet)")},
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "unmet",
                    "reason": "Opus: verified; ReAct and Reflexion are named baselines with no rows in Table 1; no "
                              "raw-trajectory or non-evolved memory arm.",
                    "evidence_ids": ["son55:E12"] + sol_ev(p, "local:2604.07645-2"),
                    **merged("sol:local:2604.07645-2 (store-off/evolution-off/Reflexion control, sol partial)")},
                "local:2604.07645-1": {
                    "status": "unmet",
                    "note": "Hidden A4 collision (same status): final local-1 is son55's question (evolution-off "
                            "arm); sol's local-1 (split) merged into rs:adapt_via_conditioning/RE-2."},
                "local:2604.07645-2": {
                    "status": "unmet",
                    "reason": "Opus: verified; GPT-4o writes and evolves the library and no same-model or static-hint "
                              "control exists. Final local-2 is son55's question; sol's local-2 moved to RE-3."},
                "local:2604.07645-3": {
                    "status": "unmet",
                    "reason": "Opus (revised): the expectation asks whether the scores support competitiveness with "
                              "GRPO. They do not: GRPO is higher in all 16 matched cells (opus:O03). "
                              "challenged_with_evidence is reserved for a paper's evidence-backed challenge to an "
                              "expectation, not for a claim contradicted by its own table.",
                    "evidence_ids": ["son55:E13", "son55:E14", "son55:E17", "opus:O02", "opus:O03"]},
                "local:2604.07645-5": {"status": "partial", **renum("sol:local:2604.07645-3 (cost)")},
                "rsi:abstract_experience_into_guidance/S3": {
                    "status": "met",
                    "reason": "Opus (son55): environment trajectory rewards decide zone and key turns; S3 asks for a "
                              "grounding signal, which exists. Simulator reliability is an E.measurement matter."},
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "met",
                    "reason": "Opus (sol): mutation, generalisation, crossover and threshold-based pruning are "
                              "explicit maintenance operations; whether they help is E.causality."},
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "partial",
                    "reason": "Opus (sol): admission has no reject path (opus:O04), but pruning on usage < 2 and "
                              "success < 0.3 is a survival gate; mutations are not validated."},
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O02", "opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: 'Equalized' credit makes key-turn selection positional for IntentionGym/TravelGym (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 1, "Opus sides with son55. The stated gap is the cost and opacity of RL; 'improve a "
                   "frozen model without gradients' is the background SCORE_SPEC excludes as a gap and the "
                   "domain card's F1 failure shape. No residual against experience-memory agents is shown: Reflexion "
                   "and ReAct have no results and related work names only MemGPT and MemoryAgent. Not 0: the "
                   "user-centric credit-assignment setting is a real, specific target.",
                   ["son55:E02", "son55:E33", "son55:E34", "sol:E014", "opus:O02"], ["son55:E12"]),
            "M": R("resolved", 2, "Opus sides with son55. Zones, stage tags and evolution operators form a coherent "
                   "mechanism, but its key assumptions are thin: the credit-assignment step is positional under "
                   "'Equalized' credit (opus:O01), the credit method is hand-picked per environment, operators fire "
                   "at fixed probabilities, the 'forward gradient' rationale is an analogy, and no prediction "
                   "distinguishes it from plain reflective memory.",
                   ["son55:E04", "son55:E05", "son55:E25", "son55:E26", "opus:O01"], ["son55:E08"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Hyperparameters, thresholds and the retrieval pipeline "
                   "are listed; no acceptance test, versioning or rollback for edits, and admission has no reject "
                   "path (opus:O04).", ["son55:E06", "son55:E07", "son55:E10", "son55:E24", "opus:O04"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. UserRL task scores under a fixed Qwen3-32B "
                               "simulator are comparable across arms; episode counts, simulator variance and the "
                               ">1 IntentionGym scale are unexplained, and SearchGym 14B's '+35%' is +74% by the "
                               "table's own numbers.", ["son55:E22", "son55:E29", "son55:E31", "son55:E32", "sol:E007"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Raw vs PRIME is a store-off contrast; zones, "
                             "credit, evolution and retrieval are never ablated, Reflexion/ReAct have no rows, and "
                             "GPT-4o authorship of the library is uncontrolled.",
                             ["son55:E14", "son55:E15", "sol:E006"], ["son55:E12", "son55:E19"]),
            "E.holdout": R("not_reported", 0, "Both seats not_reported 0. Neither the evaluation-episode count nor "
                           "the relation between the 100 exploration episodes and the scored episodes is stated; the "
                           "only transfer test reuses the same environments.", ["son55:E09"], ["son55:E21"],
                           [SCOPE_FULL + ": §4.1–4.2, Table 1, Appendices A–D searched for evaluation episodes, "
                            "split, held-out environments, overlap or contamination analysis; none found"]),
            "E.statistics": R("not_reported", 0, "Both seats not_reported 0. Every Table 1 cell is a single number; "
                              "no seeds, SD, intervals or episode counts despite temperature-1.0 rollouts and a "
                              "stochastic simulator.", [], [],
                              [SCOPE_FULL + ": Table 1, §4.2 and Appendix D searched for seeds, variance, "
                               "intervals, tests, run or episode counts; none found"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. A 5–6× GPU-hour ratio against GRPO is stated, but "
                        "GPT-4o distillation/evolution, embeddings and the selection LLM are not counted, which "
                        "contradicts 'only forward passes through the frozen base model'.",
                        ["son55:E18", "sol:E010"], ["son55:E19", "son55:E20"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text with Appendices A–D read. In scope (system_method): a non-weight "
                  "experience library is built from execution rewards, maintained by edit operators and retrieved "
                  "in later episodes. All eight items resolved (two not_reported after full search).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 3 and 4 (GPU hours, cross-size transfer) are image-only; only the text's "
                             "'5–6×' and qualitative transfer statements are used.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "Both apply: H00 for outcome-grounded lessons with trigger conditions distilled from the agent's "
                "trajectories, H01 for the explicit mutation/crossover/generalise/prune edit vocabulary over the "
                "living store (r13b convention).", ["son55:E01", "son55:E06", "son55:E07", "sol:E004"], NOSCORE),
            XC(p, "local:2604.07645-2", "son55", "unmet",
               "A4 collision: sol's local-2 (store-off/evolution-off/Reflexion control) and son55's local-2 (GPT-4o "
               "confound) differ. Final local-2 = son55's, unmet (verified). sol's question merged into "
               "rs:adapt_via_conditioning/RE-3 (unmet).", ["son55:E19", "sol:E006"]),
            XC(p, "local:2604.07645-3", "revised", "unmet",
               "Final local-3 = son55's question (competitiveness with GRPO), status corrected from "
               "challenged_with_evidence to unmet (opus:O03). sol's local-3 (cost, partial) renumbered to "
               "local:2604.07645-5.", ["son55:E13", "son55:E14", "opus:O03"]),
            XC(p, "local:2604.07645-4", "sol", "unmet",
               "Statistics (sol only). Verified: no test n, seeds or variance.", ["sol:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: memory-on vs memory-off exists; no component isolation.", ["son55:E14", "son55:E15"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified. sol's local-1 (same split question, unmet) merged here (hidden collision).",
               ["son55:E09", "sol:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified. sol's local-2 merged here; its 'partial' credited the raw control, which is RE-1.",
               ["son55:E12", "sol:E014"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: one source-quality variation (8B library on 4B), same environments.", ["son55:E21"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: credit, stages and operators go beyond the generic loop but none is isolated.",
               ["son55:E05", "son55:E10"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: success and failure zones exist; no paired contrast on the same task.", ["son55:E04"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "S3 asks for a grounding signal in the loop; trajectory rewards provide it. sol's 'no simulator "
               "audit' is a measurement-validity point.", ["son55:E04", "son55:E11"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "met",
               "S4 asks for explicit maintenance; the four operators with pruning thresholds are that. Their effect "
               "is untested (E.causality), which was son55's reason for partial.", ["son55:E06", "son55:E07", "sol:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
               "Pruning on usage/success is a survival gate; admission has no reject path (opus:O04) and mutations "
               "are unvalidated. son55's unmet ignored the pruning gate.", ["son55:E07", "sol:E005", "opus:O04"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 1,
                "See ratings.G: the frozen-model framing is background, not a gap, and no residual against "
                "experience-memory neighbours is shown.", ["son55:E02", "son55:E33", "opus:O02"],
                "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: positional key turns under Equalized credit (Opus finding) plus hand-picked credit "
                "and probabilistic operators keep the causal story at 2.",
                ["son55:E25", "son55:E26", "opus:O01"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text first. Initial view: in scope, evidence "
                                                   "level task (no evaluation protocol). G 1, M 2, X 2, Em 2, Ec 0–1, "
                                                   "Eh 0, Es 0, E.cost 1. Competitiveness with GRPO contradicted by "
                                                   "Table 1.",
            "integrity_checks": "Both seats a1 on 2604.07645v1, material sha 133b42cc…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: adding a GPT-4o-distilled, evolved experience library "
                                "raises frozen Qwen3 scores over raw in 24/24 cells under an unstated evaluation "
                                "protocol. The 'competitive with RL' part is contradicted; claim_support scoped.",
            "rating_agreement": "X, Em, Ec, Eh, Es, E.cost agree and were re-checked; G and M → son55. Final 33.75.",
        },
    }

    # =========================================================== 2604.08377 SkillClaw (Δ1.25)
    p = "2604.08377"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "These changes may not immediately yield higher scores but, once validated, are "
                              "retained in the deployment pool",
                    "§3.3 Main Results (Safety & Alignment)",
                    "Safety pools with skills accepted on Nights 1–3 read 24.00 on Days 2–4, equal to Day 1; the only "
                    "rise (32.00, Day 5) follows the Night-4 same-pool retest (son55:E19). The whole Safety gain is a "
                    "re-reading of an unchanged pool.", kind="our_inference"),
            opus_ev(p, "O02", "Although additional skill updates are proposed in later rounds, Day 2 already "
                              "establishes the current best skill pool for this category, leading to consistently "
                              "strong user-side performance.",
                    "§3.3 Main Results (Social Interaction)",
                    "Social reads exactly 60.34 on Days 2–6 although a same-pool retest ran on Nights 2, 4 and 5; "
                    "with Search's Night-3 retest (son55:E20) this shows Table 3 carries forward the best readout "
                    "instead of re-measuring each day (a running best on the selection tasks).",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus sides with sol. The abstract names the conventionally fixed component ('these skills "
                      "remain largely static after deployment') and the method makes it a variable updated from "
                      "execution evidence: the run convention for trace-driven skill editors (r11b EvoSkill, r10b "
                      "MemSkill). son55's outside_taxonomy would leave the paper unmatched although the same move is "
                      "matched elsewhere in the run; the closed-loop retention part is covered by the domain layer.",
            "matches": [smatch("sol", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("sol", p) + [
            {"rs_main": "generative_process_redesign", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "attribute_and_patch_incumbent", "sub": "H11"},
             "operation_correspondence": "The static skill becomes an edited incumbent: sessions grouped per skill, "
                                         "defects separated from agent/environment lapses, targeted section edits, "
                                         "candidate re-run against the incumbent before retention.",
             "necessary_conditions_and_differences": "The gate compares outcomes with the same model on the same "
                                                     "day's tasks; no budget on edits beyond 'conservative' mode.",
             "evidence_ids": ["son55:E08", "son55:E09", "son55:E32"]}],
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son, rename={}, drop={("sol", "local:2604.08377-4")},
            overrides={
                "local:2604.08377-3": {
                    "status": "unmet",
                    "reason": "Opus (revised): same question in both seats (variance across runs). No run-level "
                              "variance; same-pool retests moved readings by +4.55 and +8.00 with no skill change "
                              "(opus:O01). son55's challenged_with_evidence is not the right status for a claim the "
                              "paper's own data undercut.",
                    "evidence_ids": ["son55:E19", "son55:E20", "opus:O01"]},
                "local:2604.08377-4": {
                    "note": "Hidden A4 collision (same status): final local-4 is son55's question (4 of 6 categories "
                            "reported); sol's local-4 (cost) merged into local:2604.08377-5."},
                "local:2604.08377-5": {
                    "status": "unmet",
                    "reason": "Opus: verified; only a qualitative remark about extra token cost.",
                    "evidence_ids": ["son55:E27"] + sol_ev(p, "local:2604.08377-4"),
                    **merged("sol:local:2604.08377-4 (cost, sol unmet)")},
                "rsi:evidence_gated_retention/S1": {
                    "status": "met",
                    "reason": "Opus (son55): old and candidate skill are executed under identical conditions before "
                              "admission, an explicit counterfactual. Readout noise is charged in E.holdout/"
                              "E.statistics, not here."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: Safety's +8.00 and Search's last +4.55 come from same-pool retests; Social's series is carried "
            "forward (opus:O01, opus:O02)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static per-user skills and repeated rediscovery are a "
                   "concrete limitation with a residue (cross-user aggregation), but the 'static library' premise "
                   "is weakened by skill-evolution work the paper cites and does not position against.",
                   ["son55:E01", "son55:E02", "son55:E05", "son55:E06", "sol:E001"], ["son55:E03", "son55:E29"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Grouping by skill, success-as-invariant/failure-as-target, "
                   "skill/agent/environment triage and an incumbent A/B gate form a reasoned chain; the cross-user "
                   "premise has no distinguishing test against single-user evolution.",
                   ["son55:E05", "son55:E08", "son55:E09", "son55:E32", "sol:E002", "sol:E003"], ["son55:E06"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Session structuring, grouping, four evolver actions, "
                   "versioned history files, nightly A/B, accept/reject and synchronisation are reconstructable from "
                   "text and prompts. Gaps: model-judged comparison, no retirement or size bound, history "
                   "persistence depends on an unstated mode.",
                   ["son55:E07", "son55:E09", "son55:E11", "son55:E30", "son55:E31", "sol:E013", "sol:E014"],
                   ["son55:E10"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. WildClawBench scoring is execution-based with "
                               "hard constraints; per-category task counts and the gate's model-judged comparison are "
                               "unreported. The running-best readout (opus:O01, opus:O02) is a selection-on-test "
                               "defect and is charged once, under E.holdout (A2).",
                               ["son55:E17", "son55:E18", "son55:E37", "sol:E004"], ["son55:E10"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only Day 1 vs the later best pool on the same "
                             "tasks; no concurrent no-evolution run, no single-user arm, no evolver ablation; "
                             "same-pool retests show readings move without any skill change.",
                             ["son55:E17", "son55:E22", "sol:E011"], ["son55:E19", "son55:E20", "opus:O01"]),
            "E.holdout": R("resolved", 0, "Opus sides with son55 on status. The paper reports that validation tasks "
                           "are drawn from the day's interaction data on the very benchmark tasks it scores, and "
                           "Table 3 carries forward the best readout across same-pool retests (opus:O01, opus:O02). "
                           "This is evidence against held-out improvement, so resolved 0 rather than not_reported.",
                           ["son55:E16", "son55:E18", "sol:E008", "opus:O01", "opus:O02"],
                           ["son55:E14", "son55:E15", "son55:E25"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 tier 1): 8 users, 60 tasks, 6 rounds and the rejected "
                              "candidates are disclosed; single run, no variance or interval.",
                              ["son55:E13", "son55:E14", "son55:E22", "son55:E23", "sol:E006"],
                              ["son55:E19", "son55:E20"]),
            "E.cost": R("not_reported", 0, "Opus sides with sol. The only cost statement is that validation 'introduces "
                        "additional token cost'; no tokens, dollars, calls or runtime for evolution or validation. A "
                        "qualitative acknowledgement is not a cost result (r13b PsychAgent convention).",
                        ["son55:E27", "sol:E012"], [],
                        [SCOPE_FULL + ": §2–3, Tables 3–8 and the three prompt appendices searched for tokens, cost, "
                         "dollars, calls, runtime and budget; only the qualitative remark in §3.2 found"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text with all prompt appendices read. In scope (system_method): shared "
                  "non-weight skills are edited from execution traces, gated, retained and synchronised. All eight "
                  "items resolved (E.cost not_reported after full search).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–5 are schematic/case-study images; all numbers come from Tables 3–8.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "Run convention for trace-driven skill editors; see rs_pattern.reason.", ["son55:E01", "sol:E001"],
                NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["generative_process_redesign", None]],
                "outside_taxonomy is not needed: the abstract names the fixed component that the method liberates.",
                ["son55:E01", "sol:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["attribute_and_patch_incumbent", "H11"],
                 ["evidence_gated_retention", "H30"]],
                "son55 adds H11: the evolve prompt separates skill defects from agent/environment lapses and edits "
                "only the implicated section (son55:E32), which is H11's tactic (r11b EvoSkill convention).",
                ["son55:E32", "son55:E08", "son55:E09"], NOSCORE),
            XC(p, "local:2604.08377-3", "revised", "unmet",
               "Same question (statistics) in both seats; sol's partial is too generous given same-pool shifts and "
               "son55's challenged_with_evidence is a status misuse. Final unmet.", ["son55:E19", "son55:E20", "opus:O01"]),
            XC(p, "local:2604.08377-5", "son55", "unmet",
               "Cost, unmet (verified). sol's local-4 (cost, unmet) merged here; final local-4 is son55's "
               "selective-reporting question (hidden collision).", ["son55:E27", "sol:E012"]),
            XC(p, "rsi:abstract_experience_into_guidance/H02", "sol", "partial",
               "Verified: portable versioned packages with history and sync; no reuse test on disjoint tasks or "
               "consumers.", ["sol:E014", "son55:E11"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: names a specific fixed object, but prior skill evolution is cited.", ["son55:E01", "son55:E03"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "sol", "met",
               "Verified: success sessions define invariants, failures define targets.", ["sol:E003", "son55:E08"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: tool errors, PRM/ORM scores and A/B outcomes ground the edits.", ["son55:E35", "son55:E09"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Verified: targeted edits and history; no retirement, deduplication or staleness rule.", ["son55:E31"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "met",
               "S5 asks for a gate before publication; the nightly execution A/B with non-deployment of rejects is "
               "one. Gate quality (model-judged, same tasks) is recorded under F4 and E.holdout.",
               ["son55:E09", "son55:E11"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "partial",
               "Verified (met = failure avoided): real execution, but the outcome comparison is made by Qwen3-Max "
               "on the same day's tasks.", ["son55:E10", "son55:E28"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "met",
               "Verified: invariants preserved, candidates must beat the incumbent, rejects not deployed.",
               ["son55:E08", "son55:E11"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: sessions grouped per skill across users before an edit.", ["son55:E05"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: truncated step traces (~400 chars per field) plus an LLM summary.", ["son55:E33"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "met",
               "An identical-conditions old-vs-candidate run is the counterfactual S1 asks for; noise in the "
               "readout is an E.holdout/E.statistics issue (sol's reason for partial).", ["son55:E09", "sol:E004"]),
            XC(p, "rsi:evidence_gated_retention/S2", "sol", "unmet",
               "Verified: no size bound or retirement rule.", ["sol:E014"]),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 0},
                "Same rating; the paper itself reports selection on the scored tasks, so resolved rather than "
                "not_reported. See ratings.E.holdout.", ["son55:E16", "opus:O02"], "none (0 either way)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "not_reported", "rating": 0},
                "A qualitative acknowledgement is not a reported cost; see ratings.E.cost.", ["son55:E27"],
                "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text first. Initial view: in scope, evidence "
                                                   "level task (selection = reporting tasks; Table 3 is a running best "
                                                   "with same-pool re-reads). G 2, M 2–3, X 3, Em 1–2, Ec 1, Eh 0, "
                                                   "Es 1, E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.08377v2, material sha f1ca1d61…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: in one 6-round, 8-user simulation, the gated loop's "
                                "best-so-far readouts on the validation task pool rose in four categories; part of "
                                "that rise is re-measurement of unchanged pools, and the cross-user effect is "
                                "untested. claim_support scoped.",
            "rating_agreement": "G, M, X, Em, Ec, Es agree and were re-checked (Em kept at 2 because the running "
                                "best is charged once, under Eh); Eh status → son55, E.cost → sol. Final 47.5.",
        },
    }

    # =========================================================== 2604.08618 SkillForge (Δ11.25)
    p = "2604.08618"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "in Strict CR and Lenient CR on the held-out evaluation set",
                    "§3.3 (Table 3 lead-in)",
                    "Table 3 reports only gains relative to each starting skill; no absolute CR is given for S_manual "
                    "or any evolved version, so 'automated evolution can surpass manually curated expert knowledge' "
                    "is only shown as S_manual improving on itself.", kind="our_inference"),
            opus_ev(p, "O02", "The modified VFS state is committed as Skill_v_n+1 , ensuring full traceability.",
                    "§2.7 Versioning",
                    "Each round's rewrite becomes the next version without an acceptance test, regression check or "
                    "rollback; 'Do No Harm' is an instruction to the optimiser, not a gate."),
            opus_ev(p, "O03", "Acceptable action but less optimal than the reference (e.g., customer asked a simple "
                              "confirmation question; reference answered briefly; actual response is overly verbose).",
                    "Appendix D, LLM-Judge prompt (Partially Consistent)",
                    "The judge penalises verbosity, and the same judge selects the bad cases that drive evolution."),
            opus_ev(p, "O04", "Reviews the response tone, ensuring it is not robotic, overly verbose, or cold.",
                    "§2.6.1 Style Analysis",
                    "The Analyzer's style dimension targets the same surface feature the judge scores (style:verbose "
                    "is the top issue in Appendix F), so part of a Strict-CR gain can be judge-aligned style rather "
                    "than better resolution.", kind="our_inference"),
            opus_ev(p, "O05", "no systematic mechanism exists to trace execution failures back to skill deficiencies "
                              "and drive targeted refinements",
                    "§1", "The second stated gap, asserted without qualification."),
            opus_ev(p, "O06", "distills success trajectories into reusable skills and failure trajectories into "
                              "executable guardrails",
                    "§4.3 Related Work (Steve-Evolving)",
                    "The paper's own related work cites failure-driven skill evolution, which contradicts the "
                    "unqualified 'no systematic mechanism' premise (opus:O05).", kind="our_inference"),
            opus_ev(p, "O07", "We compare v3 against the production legacy system",
                    "§3.4", "Which starting point's v3 is compared, and the legacy system's backbone and tools, are "
                            "not stated."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["decompose_and_delegate"],
            "outside_taxonomy": False,
            "reason": "Opus: the abstract names the fixed component ('skill quality stagnant' after deployment) and "
                      "the method makes the deployed skill an evolving variable, the same move as SkillClaw in this "
                      "batch and EvoSkill (r11b): generative_process_redesign primary (sol, sub null). son55's "
                      "decompose_and_delegate/C25 is kept as supporting: the improver is split into Analyzer → "
                      "aggregation → Diagnostician → Optimizer with typed JSON/plan artifacts and a deterministic "
                      "verdict rule, which is the paper's distinguishing mechanism; fit is partial because no sound "
                      "external solver closes the loop and the artifacts are advisory.",
            "matches": [smatch("sol", p, "generative_process_redesign"),
                        smatch("son55", p, "decompose_and_delegate", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "revision_proposals": []},
        "pattern_mapping": pm("sol", p) + pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.08618-3"): "local:2604.08618-5"},
            drop={("sol", "local:2604.08618-1"), ("sol", "local:2604.08618-2"), ("sol", "local:2604.08618-4")},
            overrides={
                "local:2604.08618-1": {
                    "status": "unmet",
                    "reason": "Opus: verified; Table 3 gives only Δ, S_manual v0 and evolved absolute CR are never "
                              "reported (opus:O01). Final local-1 is son55's question; sol's local-1 moved to local-3."},
                "local:2604.08618-2": {
                    "status": "partial",
                    "reason": "Opus: verified; '>90% agreement' with two-expert consensus on an unsized sample, judge "
                              "model unnamed. Final local-2 is son55's question; sol's local-2 moved to RE-5."},
                "local:2604.08618-3": {
                    "status": "unmet",
                    "reason": "Opus (revised from unknown): the full text was read; which tickets the Creator mined is "
                              "never disclosed, so the expectation (creator data disjoint from the held-out split) is "
                              "not met. The evolution claim's split is clean (E.holdout).",
                    "evidence_ids": ["son55:E34", "son55:E07"] + sol_ev(p, "local:2604.08618-1"),
                    **merged("sol:local:2604.08618-1 (creator source boundary, sol partial)")},
                "local:2604.08618-4": {
                    "status": "unmet",
                    "reason": "Opus (revised from unknown): after a full read, the compared v3 starting point and the "
                              "legacy system's backbone/tools are not reported (opus:O07); the like-for-like "
                              "expectation is unmet.",
                    "evidence_ids": ["son55:E18", "opus:O07"]},
                "local:2604.08618-5": {"status": "partial", **renum("sol:local:2604.08618-3 (statistics)")},
                "rs:decompose_and_delegate/RE-1": {
                    "status": "unmet",
                    "reason": "Opus: verified; no token, call, latency or dollar figure.",
                    "evidence_ids": sol_ev(p, "local:2604.08618-4"),
                    **merged("sol:local:2604.08618-4 (cost, sol unmet)")},
                "rs:decompose_and_delegate/RE-5": {
                    "status": "unmet",
                    "reason": "Opus: verified; no direct-rewrite, TextGrad/OPRO or skill-evolution baseline, and the "
                              "creator contrast changes model and information together.",
                    "evidence_ids": ["son55:E16", "son55:E22"] + sol_ev(p, "local:2604.08618-2"),
                    **merged("sol:local:2604.08618-2 (same-information creator / naive-rewrite control, sol unmet)")},
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "unmet",
                    "reason": "Opus (son55): nothing re-validates a rewrite before it replaces the incumbent "
                              "(opus:O02); additive-edit instructions are not a retention rule."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01", "opus:O07"]), "C2", ["opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: judge and Analyzer share style targets (opus:O03, opus:O04).",
            "Opus: the 'no systematic mechanism' premise conflicts with the paper's own related work (opus:O06)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The domain-grounding gap is concrete and the case study "
                   "shows real knowledge/tool/clarification failures, but the second gap is stated as 'no systematic "
                   "mechanism exists' (opus:O05) while the paper's own related work cites failure-driven skill "
                   "evolution (opus:O06), and the residual against TextGrad/OPRO/skill evolvers is asserted "
                   "structurally. The residue is the enterprise reference-reply setting.",
                   ["son55:E01", "son55:E02", "son55:E23", "sol:E001", "sol:E012", "opus:O05"],
                   ["son55:E22", "opus:O06"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Four-dimension analysis with a deterministic verdict, "
                   "defect-type attribution to SKILL.md locations, additive optimiser with layered knowledge "
                   "placement, and an explained knowledge plateau. No distinguishing test against a direct "
                   "bad-case rewrite.", ["son55:E03", "son55:E04", "son55:E05", "son55:E19", "son55:E20", "sol:E002"],
                   ["son55:E22"]),
            "X": R("resolved", 2, "Opus sides with son55. Stages, schemas, thresholds and VFS versioning are "
                   "described in detail, but the retention step is missing: every rewrite is committed as the next "
                   "version (opus:O02) with no acceptance test, regression check on fixed cases or rollback, and "
                   "recommended tools that may not exist are not handled. sol's 3 credited versioning as retention.",
                   ["son55:E03", "son55:E05", "son55:E06", "sol:E003", "sol:E011", "opus:O02"], ["son55:E30"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Consistency against real expert replies with a "
                               "stated human check is a sound basis, but the check's sample size and the judge model "
                               "are not given, the same judge selects the bad cases that drive evolution, the judge "
                               "and the Analyzer share style targets (opus:O03, opus:O04), and only Δ values are "
                               "reported (opus:O01). sol's 3 credited the >90% agreement alone.",
                               ["son55:E11", "son55:E12", "son55:E28", "sol:E007", "opus:O01", "opus:O03", "opus:O04"],
                               ["son55:E10", "son55:E32"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. v0 → v3 on the held-out split from three "
                             "starting skills, with monotone gains per round, supports the loop over no evolution; no "
                             "stage ablation or alternative optimiser, the creator contrast is confounded and the "
                             "legacy comparison is unmatched (opus:O07).",
                             ["son55:E14", "son55:E09", "son55:E31", "sol:E008"], ["son55:E16", "son55:E18", "opus:O07"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Chronological fourth split never seen during "
                           "evolution; the creator's mining source is undisclosed (affects S_domain v0, not the "
                           "per-start Δ); single provider, single backbone.",
                           ["son55:E07", "son55:E08", "son55:E09", "sol:E004", "sol:E005"], ["son55:E34"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 tier 1): 3,737 tasks and three repeats, means only; "
                              "no SD, intervals, tests or per-scenario evolution results.",
                              ["son55:E13", "son55:E29", "sol:E006"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported 0; re-checked.", [], [],
                        [SCOPE_FULL + ": §1–4 and Appendices A–F searched for cost, tokens, latency, calls, GPU, "
                         "budget, runtime; none found"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text with Appendices A–F read. In scope (system_method): a non-weight "
                  "skill package is rewritten from diagnosed execution failures, retained across rounds and "
                  "evaluated on a later held-out split. All eight items resolved (E.cost not_reported).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 1 is a schematic; all numbers come from Tables 1–5 and the text.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "The framing move is liberating the stagnant deployed skill; see rs_pattern.reason.",
                ["son55:E02", "sol:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["decompose_and_delegate", "C25"]],
                "sol's card as primary; son55's C25 kept as supporting for the staged, typed-artifact diagnosis "
                "pipeline (fit partial).", ["sol:E002", "son55:E03", "son55:E04"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["attribute_and_patch_incumbent", "H11"]],
                "H11 (both seats) for failure attribution to skill sections; H02 (son55) for the Creator, which "
                "mines historical resolution traces and documents into a structured skill package, a central claim "
                "(RQ1). H02's source list includes guides and domain resources.", ["son55:E33", "son55:E34"], NOSCORE),
            XC(p, "local:2604.08618-1", "son55", "unmet",
               "A4 collision: sol's local-1 (creator source vs holdout) and son55's local-1 (absolute scores / "
               "surpass claim) differ. Final local-1 = son55's, unmet (opus:O01). sol's question merged into "
               "local-3.", ["son55:E14", "son55:E17", "opus:O01"]),
            XC(p, "local:2604.08618-2", "son55", "partial",
               "A4 collision: sol's local-2 (causal controls) and son55's local-2 (judge validation) differ. Final "
               "local-2 = son55's, partial (verified). sol's question merged into rs:decompose_and_delegate/RE-5.",
               ["son55:E12", "sol:E007"]),
            XC(p, "local:2604.08618-3", "revised", "unmet",
               "Final local-3 = son55's question (creator mining source), with sol's local-1 merged. Status "
               "unknown → unmet: the material is complete and the disclosure is absent. sol's local-3 (statistics) "
               "renumbered to local:2604.08618-5.", ["son55:E34", "sol:E005"]),
            XC(p, "local:2604.08618-4", "revised", "unmet",
               "Final local-4 = son55's question (legacy comparison), unknown → unmet after a full read (opus:O07). "
               "sol's local-4 (cost) merged into rs:decompose_and_delegate/RE-1.", ["son55:E18", "opus:O07"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Kept with the supporting card. Verified: no cost figure. sol's local-4 merged here.", ["son55:E29"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "Verified: no stage ablation.", ["son55:E14"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "partial",
               "Verified: judge prompt and schemas given; analyzer/diagnostician/optimiser prompts described only.",
               ["son55:E32"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: five scenarios, three starts, one provider/backbone/judge family.", ["son55:E29", "son55:E21"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "unmet",
               "Verified. sol's local-2 merged here.", ["son55:E22", "son55:E16"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "partial",
               "Verified: Appendix F distributions and the plateau analysis, no stage-outcome experiment.",
               ["son55:E19"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "partial",
               "Verified (met = failure avoided): real expert references, but the LLM judge both triggers evolution "
               "and scores the held-out set.", ["son55:E10", "son55:E28"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11", "sol", "partial",
               "Verified: section attribution and defect types exist; the re-run-and-retain step of H11 is absent.",
               ["sol:E002", "opus:O02"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "No re-validation before replacement (opus:O02); additive editing is an optimiser instruction. sol's "
               "partial credited that instruction.", ["son55:E05", "opus:O02"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: per-case records aggregated by category before diagnosis.", ["son55:E04"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: the 'no systematic mechanism' premise is contradicted by the paper's own related "
                "work (Opus finding).", ["opus:O05", "opus:O06", "son55:E23"], "−3.75 vs sol (15×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2,
                "See ratings.X: no acceptance/regression gate or rollback; versioning is traceability.",
                ["son55:E06", "opus:O02"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 2,
                "See ratings.E.measurement: unsized human check, unnamed judge in the optimisation loop, shared "
                "style targets, Δ-only reporting.", ["son55:E12", "opus:O01", "opus:O03", "opus:O04"],
                "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text first. Initial view: in scope, retained "
                                                   "(chronological held-out split). G 2, M 3, X 2 (no gate), Em 2, "
                                                   "Ec 1–2, Eh 3, Es 1, E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.08618v2, material sha 42924beb…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: three rounds of diagnosis-driven skill rewriting on "
                                "earlier tickets raise LLM-judged strict consistency by 9–12 points on later held-out "
                                "tickets from three starting skills (mean of 3 runs, one provider). 'Surpasses expert "
                                "knowledge' is only shown as the expert skill improving on itself. claim_support "
                                "scoped.",
            "rating_agreement": "M, Ec, Eh, Es, E.cost agree and were re-checked (Ec kept at 2: v0→v3 from three "
                                "starts on held-out data controls for no evolution); G, X, Em → son55. Final 53.75.",
        },
    }

    # =========================================================== 2604.09297 SkillMOO (Δ6.25)
    p = "2604.09297"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "so pass rate is the fraction of passing runs",
                    "§4 Experimental Setup",
                    "The stated metric is binary per run. Table 2 nevertheless reports cells such as Task 2 SkillMOO "
                    "0.89 ± 0.03, Task 14 0.99 ± 0.01, Task 5 0.37 ± 0.16 and no_skill Task 5 0.10 ± 0.00, which ten "
                    "binary runs cannot produce (mean 0.89 would give SD ≈ 0.33), while Task 1's 0.90 ± 0.32 can. The "
                    "per-run quantity behind the means and Scott-Knott ranks is therefore not the one defined.",
                    kind="our_inference"),
            opus_ev(p, "O02", "SD over 10 independent runs.", "Table 2 caption",
                    "The caption asserts per-cell SD over 10 runs, the unit whose definition conflicts with §4."),
            opus_ev(p, "O03", "On tasks with larger skill bundles, SkillMOO consistently finds better pass/cost "
                              "tradeoffs than static deployment, with pass rate gains up to +42 percentage points and "
                              "cost reductions up to 32.1%.",
                    "§5.1 RQ1 answer",
                    "+42 pp is Task 6 (0.42 vs 0.00), the largest gain among multi-skill tasks, and 32.1% matches "
                    "Task 5 (1.10 vs 1.61). The abstract drops the 'larger skill bundles' qualifier and so "
                    "understates the single-skill gains (Task 1 +80 pp, Task 2 +73 pp); it is traceable, not "
                    "mismatched.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: reframe_as_solvable_object, sub null (skill-bundle design recast as bi-objective "
                      "selection solved with NSGA-II; C00/C21/C27 do not fit). Kept as agreed.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H16")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "revision_proposals": []},
        "pattern_mapping": pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.09297-3"): "local:2604.09297-5"},
            drop={("sol", "local:2604.09297-4")},
            overrides={
                "local:2604.09297-2": {
                    "status": "unmet",
                    "reason": "Opus (sol): search and reporting share task and verifier; no held-out task or model, "
                              "and a fresh re-execution of the selected bundle is not stated (son55's unknown folded "
                              "in)."},
                "local:2604.09297-3": {
                    "status": "partial",
                    "reason": "Opus (revised from unknown): +42 pp traces to Task 6 under the RQ1 'larger skill "
                              "bundles' qualifier (opus:O03); the abstract omits the qualifier, understating the "
                              "single-skill gains. Final local-3 is son55's question; sol's local-3 renumbered to "
                              "local:2604.09297-5.",
                    "evidence_ids": ["son55:E20", "son55:E21", "opus:O03"]},
                "local:2604.09297-4": {
                    "status": "unmet",
                    "reason": "Opus: verified; no pass-only or single-objective arm. Final local-4 is son55's "
                              "question; sol's local-4 (cost) merged into rs:reframe_as_solvable_object/RE-5."},
                "local:2604.09297-5": {"status": "partial", **renum("sol:local:2604.09297-3 (statistics unit)"),
                                       "evidence_ids": ["sol:E005", "sol:E008", "opus:O01"]},
                "rs:reframe_as_solvable_object/RE-5": {
                    "status": "partial",
                    "reason": "Opus: verified; per-task search cost/runtime and a cost-only break-even are reported "
                              "(4×3 search); larger pools are acknowledged, not tested; reuse is hypothetical.",
                    "evidence_ids": ["son55:E12", "son55:E13"] + sol_ev(p, "local:2604.09297-4"),
                    **merged("sol:local:2604.09297-4 (search cost / reuse, sol partial)")},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: the per-run pass-rate unit in Table 2 conflicts with the binary definition in §4 (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The cost/misleading-guidance problem is sourced "
                   "(SkillsBench, SWE-Skills-Bench) and visible in Table 2 (ori_skill averages 0.14 pass vs 0.21 for "
                   "no skill); pass-only neighbours are named and the delta (cost-aware Pareto selection) is bounded.",
                   ["son55:E01", "son55:E02", "son55:E03", "son55:E04", "son55:E16", "sol:E001"], ["son55:E15"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. The bi-objective formulation answers the stated problem "
                   "and mutation is grounded in evaluation evidence; no test against pass-only search.",
                   ["son55:E05", "son55:E07", "son55:E08", "sol:E002", "sol:E003"], ["son55:E21"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Phases, sizes, objectives and selection are clear; the "
                   "final-bundle choice from the archive, optimiser prompts, noise handling of single evaluations "
                   "and any reuse protocol are not.", ["son55:E06", "son55:E08", "son55:E12", "sol:E004", "sol:E007"],
                   ["son55:E32", "son55:E30"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol, on a further ground. The verifier is execution-"
                               "based (original gates plus manually checked expanded tests). But the per-run pass "
                               "unit contradicts its own definition (opus:O01, opus:O02), so what the means and ranks "
                               "aggregate is unclear, and the threats section's 'same model family' statement "
                               "conflicts with GPT-5.4 test generation for a GLM-5 solver. The abstract's +42 pp is "
                               "traceable (opus:O03), so son55's mismatch note is withdrawn; it did not drive the "
                               "rating.",
                               ["son55:E09", "son55:E10", "son55:E11", "sol:E005", "sol:E006", "opus:O01", "opus:O02"],
                               ["sol:E015", "son55:E14"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only static ori_skill/no_skill baselines; no "
                             "pass-only, random-edit/subset or budget-matched search; edit causality deferred by the "
                             "authors.", ["son55:E15", "son55:E16", "sol:E010", "sol:E013"], ["son55:E28", "son55:E24"]),
            "E.holdout": R("resolved", 0, "Opus revises both seats. Each run's bundle is selected and reported on the "
                           "same task and verifier (son55:E34), no held-out task or model exists and fresh "
                           "re-execution is not stated. The authors disclose this, but disclosure is not holdout "
                           "evidence (sol's ground; son55's 1 credited disclosure). Status resolved rather than "
                           "not_reported, because the setup itself shows selection = reporting (SkillClaw convention "
                           "in this batch).", ["son55:E26", "son55:E27", "son55:E34", "sol:E014"], ["son55:E30"]),
            "E.statistics": R("resolved", 3, "Opus sides with son55. Ten independent search runs per method and task "
                              "give cross-search dispersion (SD), Scott-Knott ESD supplies significance-based ranks, "
                              "and the four zero-pass tasks are disclosed and excluded from comparisons. Not 4: no "
                              "intervals or multiple-comparison treatment. The unit ambiguity is charged once, under "
                              "E.measurement (A2).", ["son55:E09", "son55:E18", "son55:E29", "sol:E008", "sol:E009"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Per-task search cost and runtime, per-candidate "
                        "cost range, deployed cost per run and a break-even analysis are reported; baselines get no "
                        "search budget and reuse is hypothetical.",
                        ["son55:E13", "son55:E22", "son55:E23", "son55:E31", "sol:E011"], ["son55:E15"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 HTML text read (no appendix). In scope (system_method): non-weight skill "
                  "bundles are edited from execution evidence and selected by an executable bi-objective fitness. "
                  "All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 1 is a schematic; all numbers come from Tables 1–4.",
        "resolutions": [
            XC(p, "local:2604.09297-2", "sol", "unmet",
               "Same question (holdout). Selection and reporting share task and verifier, so unmet; son55's narrower "
               "'fresh re-evaluation not stated' is part of that and does not make the status unknown.",
               ["son55:E34", "sol:E014"]),
            XC(p, "local:2604.09297-3", "revised", "partial",
               "A4 collision: sol's local-3 (statistics unit, partial) and son55's local-3 (+42 pp vs Table 2, "
               "unknown) differ. Final local-3 = son55's question; +42 pp is traceable to Task 6 under the RQ1 "
               "qualifier (opus:O03), the abstract drops it: partial. sol's local-3 renumbered to "
               "local:2604.09297-5.", ["son55:E20", "opus:O03"]),
            XC(p, "local:2604.09297-4", "son55", "unmet",
               "A4 collision: sol's local-4 (cost, partial) and son55's local-4 (single-objective arm) differ. Final "
               "local-4 = son55's, unmet. sol's question merged into rs:reframe_as_solvable_object/RE-5.",
               ["son55:E15", "sol:E011"]),
            XC(p, "rs:reframe_as_solvable_object/RE-3", "son55", "partial",
               "Verified: the cost objective and bundle operators are new; NSGA-II/HV/ESD are off-the-shelf.",
               ["son55:E05", "son55:E08"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "unmet",
               "Verified: no fresh-task/model or randomised-edit validation.", ["son55:E28"]),
            XC(p, "rs:reframe_as_solvable_object/RE-5", "son55", "partial",
               "Verified. sol's local-4 merged here.", ["son55:E12", "son55:E26"]),
            XC(p, "rs:reframe_as_solvable_object/RE-6", "son55", "partial",
               "Verified: prune/replace principle drawn from filtered traces, labelled exploratory.", ["son55:E24"]),
            XC(p, "rsi:population_search_executable_fitness/F1", "son55", "partial",
               "Verified: search-level change (cost objective) inside a standard loop, not tested against pass-only.",
               ["son55:E08"]),
            XC(p, "rsi:population_search_executable_fitness/H16", "sol", "partial",
               "Verified: non-dominated archive kept; frontier vs single-winner not ablated.", ["sol:E012"]),
            XC(p, "rsi:population_search_executable_fitness/S4", "son55", "met",
               "Verified: the optimiser receives each bundle with its evaluation evidence.", ["son55:E07"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "partial",
               "Verified: axis named and HV measured; final choice and archive benefit not evaluated.",
               ["son55:E32"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement: the per-run unit contradicts its definition (Opus finding); son55's 3 "
                "assumed binary runs.", ["opus:O01", "opus:O02", "sol:E005"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "revised", {"status": "resolved", "rating": 0},
                "Rating as sol, status as son55: the setup shows selection = reporting; disclosure earns no holdout "
                "credit.", ["son55:E34", "son55:E26"], "−2.5 vs son55 (10×1/4); none vs sol"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", 3,
                "See ratings.E.statistics: cross-search SD plus ESD significance ranks exceed A2 tier 2; sol's "
                "unit concern is charged to E.measurement.", ["son55:E09", "son55:E29"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v3 text first. Initial view: in scope, evidence "
                                                   "level task (per-task search, same verifier). G 3, M 3, X 2, Em 2 "
                                                   "(binary-vs-fractional unit conflict), Ec 1, Eh 0, Es 2–3, "
                                                   "E.cost 3.",
            "integrity_checks": "Both seats a1 on 2604.09297v3, material sha 22e8109c…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: per task, a small LLM-edit + NSGA-II search finds "
                                "bundles that score higher, often at lower cost, than the original or empty bundle on "
                                "the same verifier (10 runs, GLM-5), at $1.76–13.73 per task. The value of the "
                                "multi-objective part and transfer are untested. claim_support scoped.",
            "rating_agreement": "G, M, X, Ec, E.cost agree and were re-checked; Em → sol, Es → son55, Eh revised "
                                "(resolved 0). Final 52.5.",
        },
    }

    return S
