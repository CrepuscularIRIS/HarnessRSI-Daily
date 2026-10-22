"""Opus rulings for r18a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat inputs: 8 of 10 a1 seat records match conflicts.json seat_record_hashes as they sit on disk. Two sol "
        "records (2604.21725, 2604.25850) were rewritten about 10 s after conflicts.json was computed. sol 2604.21725 "
        "was aggregated from the committed HEAD version, whose canonical hash equals conflicts.json; the working copy "
        "only adds E27 and turns score.display into a number. sol 2604.25850 is untracked. Its bound version was "
        "rebuilt by removing the post-conflicts evidence E31/E32 (and all references to them) and restoring "
        "score.display '67.5' as a string. The rebuilt record reproduces the conflicts.json canonical hash exactly. "
        "rv2.diff_pair on the current working copies reproduces every conflicts.json field list, so no conflict "
        "field changed. No overrides and no seat errors.",
        "2604.20133 EvoAgent (sol 41.25 / son55 28.75): final 28.75. M, X and E.measurement → son55 1. Opus "
        "findings: (1) the paper says skill maturity grants 'higher priority in future matching', but Stage 1 returns "
        "the first keyword hit and Stage 2 takes the cosine argmax, so maturity never enters matching; (2) Appendix A "
        "increments usage_count but never writes success_rate, and success is not defined; (3) the declared "
        "length/ROUGE checks are never reported and the judge model is not named. RS: adapt_via_conditioning plus "
        "decompose_and_delegate supporting (son55, low fit). Domain: H02 only (sol); H01's edit-operation condition "
        "is absent. evidence_level task, scoped (both).",
        "2604.20714 TPGO (sol 61.25 / son55 53.75): final 53.75. M → son55 2. Opus finding: the implementation "
        "edits a JSON section tree by node rewrite, insert and delete only; the edge operations of §4.3 do not appear "
        "in it, so 'structure-aware graph' optimisation reduces to sectioned-prompt editing. E.holdout → son55 1. "
        "The main tables are on the optimised task sets, and the GAIA reflector sees the gold answers of the reported "
        "tasks. The only held-out test is Table 4: +1.8 to +3.1 pp in a single run at temperature 1.0. Shared "
        "omission: GAIA overall pass@1 cannot be reproduced from the per-level rates and the stated 49/71/22 split "
        "(72.8 vs 73.8 baseline, 80.7 vs 81.6 after 5 iterations), although the gain is about the same size. RS → "
        "heterogeneous_decomposition primary plus adapt_via_conditioning supporting for GRAO. Domain → H09 plus "
        "H03 (sol).",
        "2604.21003 Last Harness (sol 27.5 / son55 23.75): final 23.75. G → son55 1, because nearest-neighbour "
        "positioning is a single APO citation. A1 applied by both seats and checked: no experiments, so the five E "
        "items are not_reported 0 with search scope, and there is no formal result. evidence_level null (son55's "
        "'none' normalised), claim_support unsupported. Domain: H19 plus H12 (son55); the inner loop is "
        "trace-diagnosed harness patching.",
        "2604.21725 AEL (sol 58.75 / son55 68.75): final 62.5. G → son55 3. X → sol 2: the core evolution "
        "trigger and the admission path contradict each other across §3.4, §3.5, App S and App P.2 (window-gated "
        "average-reward trigger vs a single-loss trigger at episode 84; the same RegimeFilteredRetrieval at seed 42 "
        "ep 84 vs seed 123 ep 95; admission 'by LinUCB' although memory arms are Thompson arms). On top of this, App "
        "N vs §3.1 disagree on the planner pool, and App W runs training past 140 bars. E.measurement → sol 3: "
        "verifiers are objective, and sample size belongs to E.statistics under A2. E.causality → sol 2: reflection "
        "alone sees market side information, the new support-ticket arm is privileged by construction, "
        "diagnose-before-prescribe is never ablated, and the reflection contrast has p=.384. Shared omission: "
        "HyperAgent is 0.72±0.38 in Table 2/5 but 0.46±0.41 in App J/K/Table 16, and the abstract's 'lowest variance "
        "among all stochastic methods' is false against either value. RS → reframe_as_solvable_object plus "
        "adapt_via_conditioning (son55). Domain → H21 plus H05 (son55).",
        "2604.25850 AHE (sol 67.5 / son55 70.0): final 65.0. X → sol 3. Algorithm 1 evaluates H_{t-1} but stores "
        "H_t as best. Rollback is called automatic (§3.3, App C.3), yet the Evolve prompt makes it a KEEP / IMPROVE "
        "/ ROLLBACK judgement, and after the 75.8→73.0 drop at iteration 7 the agent patched instead of rolling "
        "back. E.holdout → son55 2. Shared omission: the headline 77.0% is the in-loop iteration-8 score (76.97 = "
        "137/178 at k=2), i.e. the best of 10 noisy evaluations on the selection set. The ACE and TF-GRPO cells imply "
        "k=3 (91.7% = 11/12; 48.9% = 44/90; 79.4% = 131/165; 55.6% = 50/90). The only independent-task evidence "
        "(SWE-bench-verified) is +0.4 pp success with 12% fewer tokens. RS → decompose_and_delegate/C25 primary "
        "plus generative_process_redesign supporting. Domain → H12 only (sol); H31's statistically sound commit "
        "rule is absent.",
        "A4 hygiene: hidden local-ID collisions renumbered: EvoAgent son55 local-2 → local-3; TPGO son55 local-1 → "
        "local-3, with son55 local-2 merged into sol local-1 (same holdout question); AEL son55 local-1 → local-5; "
        "AHE son55 local-2/3 → local-4/5. RS-card expectations whose card was not kept in the final match "
        "(TPGO rs:self_supervised_signal_engineering/RE-2, AEL rs:generative_process_redesign/RE-1/RE-3, AHE "
        "rs:heterogeneous_decomposition/RE-5) are kept as not_applicable records. Domain-card condition checks the "
        "paper's own claims invoke (TPGO improver checks, AHE evidence_gated_retention checks) are kept as check "
        "questions with the card unmatched.",
        "Figure dependence: EvoAgent Figs 1–3, TPGO Figs 1–3, Last Harness Fig 1, AEL Figs 1–6 and AHE Figs 1, 3–13 "
        "are image-only or empty in the pinned HTML. Only values stated in text or tables were used, and nothing was "
        "read off an image.",
        "No material requests. Seats' standing requests for nearest-neighbour full texts (Voyager, TextGrad, "
        "LLM-AutoDiff, Meta-Reflexion, ACE/TF-GRPO, whole-harness search) are noted. No G rating here depends on a "
        "neighbour's content beyond what each paper itself states.",
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

    def RC(p, k, dec, final, reason, ev, impact):
        return res(f"ratings.{k}", *C(p, f"ratings.{k}"), dec, final, reason, ev, impact)

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

    def PM(rs_main, rs_sub, d_main, d_sub, corr, cond, ev):
        return {"rs_main": rs_main, "rs_sub": rs_sub,
                "domain": {"namespace": "rsi", "main": d_main, "sub": d_sub},
                "operation_correspondence": corr, "necessary_conditions_and_differences": cond, "evidence_ids": ev}

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

    def na(reason):
        return {"status": "not_applicable", "applicable": False,
                "reason": "Opus: " + reason, "note": "RS card not kept in the final match; record retained, not used."}

    # =========================================================== 2604.20133 EvoAgent (sol 41.25 / son55 28.75)
    p = "2604.20133"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "thereby granting it higher priority in future matching", "§3.2 Optimization Objective "
                    "(implicit optimization bullet 1)",
                    "The paper says maturity (usage/success) raises a skill's matching priority. Matching as specified "
                    "is Stage 1, first keyword hit (opus:O02); Stage 2, cosine argmax over descriptions; Stage 3, LLM "
                    "intent classification (Eq. 2–4; Appendix A lines 7–44). None of these reads usage_count, "
                    "success_rate or maturity. The stated feedback-to-behaviour link is therefore not part of the "
                    "algorithm.", kind="our_inference"),
            opus_ev(p, "O02", "performing case-insensitive exact string matching, and returns the first matched result.",
                    "§3.2 Stage 1: Keyword Matching", "Stage 1 returns the first trigger hit, with no ranking by "
                    "maturity.", kind="author_report"),
            opus_ev(p, "O03", "sr \\ $ \\\\ leftarrow \\ $ skill . success_rate", "Appendix A pseudocode line 114",
                    "success_rate is only read (line 114, maturity tiering). Lines 57–58 increment usage_count and "
                    "updated_at, and no line writes success_rate. The paper never defines what counts as a success. "
                    "The 'execution success rate' feedback signal is therefore unspecified in both text and "
                    "algorithm.", kind="static_code_check"),
            opus_ev(p, "O04", "At the basic metric level, we use character count statistics, length ratios, and "
                              "ROUGE-L similarity to quantify textual characteristics.", "§4.1.2 Evaluation Design",
                    "Length and overlap statistics are declared but never reported (no table or number in §4 or the "
                    "appendix). The judge model is not named. Response length, a known LLM-judge bias, is therefore "
                    "uncontrolled for a system that injects long skill documents.", kind="our_inference"),
            opus_ev(p, "O05", "Extract new skills ( with quality gating )", "Appendix A pseudocode line 95 comment",
                    "The comment promises quality gating. Lines 96–99 extract and write every LLM-proposed skill with "
                    "no test, threshold or merge step.", kind="static_code_check"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Opus: both seats' primary is kept. Retrieved skill files and profile/memory are injected as "
                      "context into a frozen model. son55's supporting decompose_and_delegate is kept at low fit. "
                      "Skill-specified sub-agent handoff is an executed operation and part of the titled contribution, "
                      "but it is LLM-to-LLM, statically configured and never evaluated, so the card's "
                      "sound-solver/verified-artifact conditions are unmet. No sub-card fits: C03 needs a trained "
                      "conditioning channel and C25 a checkable intermediate artifact.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H02")],
                           "unassigned": [],
                           "reason": "H02 only. USER.md/MEMORY.md are written by appending LLM-extracted deltas "
                                     "(Appendix A lines 88–94). H01's defining explicit edit vocabulary (add/update/"
                                     "merge/delete) is absent, so the memory files fall under the main card without a "
                                     "sub-card.",
                           "revision_proposals": []},
        "pattern_mapping": [
            PM("adapt_via_conditioning", None, "abstract_experience_into_guidance", "H02",
               "Post-session LLM extraction compiles dialogue histories into multi-file skill packages, which are "
               "retrieved by a three-stage matcher and injected as context into the frozen model.",
               "H02 requires gated, versioned skill packages; there is no gate (opus:O05) and no version or retirement. "
               "The RS card's conditioning-ablation and structural-holdout conditions are unmet.",
               ["son55:E003", "son55:E008", "opus:O05"]),
            PM("decompose_and_delegate", None, "abstract_experience_into_guidance", None,
               "Sub-agent handoff configured per skill has no counterpart in the domain move: delegation does not "
               "evolve from experience.", "Recorded as a static architectural feature only.", ["son55:E021"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.20133-2"): "local:2604.20133-3"},
            overrides={
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "unmet",
                    "reason": "Opus (son55): every extracted skill is written; the 'quality gating' is a comment only "
                              "(opus:O05). No execution test, filter or versioned merge exists."},
                "rsi:abstract_experience_into_guidance/S3": {
                    "reason": "Opus (both partial, kept): the only grounding channel is the review agent reading user "
                              "turns. success_rate is never written (opus:O03) and maturity does not affect matching "
                              "(opus:O01)."},
                "local:2604.20133-3": renum("son55:local:2604.20133-2"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O04"]), "C2", ["opus:O01", "opus:O03", "opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: the claimed maturity-driven matching priority is absent from the matching algorithm (opus:O01).",
            "Opus: success_rate is never written in Appendix A (opus:O03); declared length/ROUGE controls are "
            "unreported (opus:O04)."],
            evidence_level="task",
            evidence_level_note="Both seats task, verified. The only result compares bare GPT5.2 with the whole "
                                "framework. There is no store-on/off or before/after-evolution contrast, so no gain "
                                "is shown to come from retained skills.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Real limitation (manual multi-file skills, "
                   "prompt-level self-evolution) with Reflexion/Voyager/ExpeL-style neighbours named; the residual "
                   "bottleneck and its cost are not established, and the 'multi-file package' difference is largely "
                   "format.", ["son55:E002", "sol:E01"]),
            "M": R("resolved", 1, "Opus sides with son55. The reconstructable chain is: session ends → LLM extracts "
                   "skills from history → files stored → three-stage match → inject. The claimed driver of evolution "
                   "is user feedback via usage/success rates, and it has no operative role: success_rate is "
                   "undefined and never written (opus:O03), and maturity, the claimed route to 'higher priority in "
                   "future matching', is not read by any matching stage (opus:O01, opus:O02). The MDP reward is "
                   "explicitly not computed. What remains is unconditional LLM extraction, with no prediction that "
                   "distinguishes it from static hand-written skills.",
                   ["son55:E003", "son55:E004", "son55:E022", "opus:O01", "opus:O02", "opus:O03"]),
            "X": R("resolved", 1, "Opus sides with son55. Online matching/injection and the post-session writes are "
                   "specified in Appendix A. The operations specific to self-evolution are missing or contradicted: "
                   "no gate despite the 'quality gating' comment (opus:O05); no optimisation operation for existing "
                   "skills, though the abstract claims 'optimization'; no versioning, rollback, pruning or memory "
                   "retirement (E017); single-skill invocation only. This is between anchor 0 (key operations "
                   "missing) and 2 (main steps described). The M defect (feedback without effect) is scored there, "
                   "not here.",
                   ["son55:E003", "son55:E017", "son55:E018", "son55:E020", "opus:O05"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55. The only outcome is a 1–5 LLM-as-judge score "
                               "from an unnamed judge, including an 'accuracy' dimension with no reference answers. "
                               "There is no human agreement check, and the declared length/ROUGE statistics that "
                               "would expose length bias are never reported (opus:O04). Order shuffling (sol:E07) is "
                               "the only control. Above 0 because the dimensions are defined and responses are "
                               "position-shuffled.",
                               ["son55:E009", "son55:E010", "sol:E07", "opus:O04"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. The single control is bare GPT5.2 against the "
                             "full framework, so matching, memory, profile, sub-agents and evolution are all "
                             "confounded. The authors concede no ablation, and the gain reverses on GPT4.1 and Qwen.",
                             ["son55:E008", "son55:E010"], ["son55:E012", "son55:E013", "son55:E014"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Queries are script-generated independently of "
                           "skill triggering, but they are collected inside the deployed EvoAgent, and the authors "
                           "concede non-independence. There is no split between the data that evolved the skills and "
                           "the evaluation data.",
                           ["son55:E005", "son55:E007", "sol:E06"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). Sample sizes and negative results "
                              "(completeness, other backbones) are reported. The main result is single-run with no "
                              "intervals, and 172 instances come from 20 dialogues.",
                              ["son55:E006", "son55:E010", "son55:E011"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. System latency (12–24 s) is reported, but there is "
                        "no token/call comparison with the baseline and no evolution-phase cost. The authors state "
                        "there is no cost tracking.",
                        ["son55:E016", "son55:E019", "sol:E13"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text read (body plus Appendix A pseudocode). In scope: system_method; skills "
                  "and memory files are written after sessions and read in later sessions. All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–3 are image-only. The transfer numbers used (−13% GPT4.1; Qwen 85%) are stated "
                             "in §4.2 text.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", None]],
                "Delegation is an executed, titled operation; kept as supporting at low fit, without C25 (no "
                "checkable artifact or solver).", ["son55:E021"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H02"]],
                "H01 requires an explicit edit vocabulary chosen by a curator; memory here is append-only "
                "LLM-extracted deltas (son55's own check: 'no edit operation set'). H02 only.",
                ["son55:E003", "son55:E017"], NOSCORE),
            XC(p, "local:2604.20133-2", "revised", "partial",
               "A4 collision. sol's local-2 (cross-distribution retention holdout) stays here as partial: the "
               "weak-model regressions are reported, but there is no independent stream. son55's local-2 (judge "
               "validity) is a different question; it moves to local-3 with status unmet, verified by opus:O04.",
               ["sol:E06", "sol:E10", "son55:E009", "opus:O04"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "unmet",
               "Verified: no skills-on/off or evolution-on/off contrast inside the framework.", ["son55:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: evaluation data come from the deployed system; there is no contamination analysis.",
               ["son55:E007"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no long-context or static hand-written skill baseline.", ["son55:E008"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Verified: latency only, with no call/token comparison.", ["son55:E016"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "Verified: the delegation benefit is claimed but never measured.", ["son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "unmet",
               "Verified: the novelty rests on the foreign-trade vertical plus integration; the extract-store-retrieve "
               "loop is generic.", ["son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/F5", "son55", "partial",
               "Verified: the store comes from session history, but outcome grounding is undefined (opus:O03).",
               ["son55:E022", "opus:O03"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: the fixed object (manually written skills) is named; the claimed optimisation of existing "
               "skills has no operation.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "unmet",
               "Verified: no success/failure contrast is described.", ["son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Every extracted skill is written. The 'quality gating' exists only as a pseudocode comment "
               "(opus:O05), so partial overstates it.", ["opus:O05", "son55:E003"]),
            RC(p, "M", "son55", {"status": "resolved", "rating": 1},
               "See ratings.M: the feedback signal has no operative role (opus:O01–O03).",
               ["opus:O01", "opus:O03", "son55:E022"], "−5.0 vs sol (20×1/4)"),
            RC(p, "X", "son55", {"status": "resolved", "rating": 1},
               "See ratings.X: no gate, no skill-optimisation operation, no version/rollback/retirement.",
               ["opus:O05", "son55:E017", "son55:E020"], "−5.0 vs sol (20×1/4)"),
            RC(p, "E.measurement", "son55", {"status": "resolved", "rating": 1},
               "See ratings.E.measurement: an unnamed judge, no reference answers for 'accuracy', and unreported "
               "length controls (opus:O04).", ["son55:E009", "opus:O04"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "gap.method_response / ratings.M (both seats)",
             "sol_value": "usage/success metadata treated as an implicit (if undocumented) selection signal",
             "son55_value": "success_rate noted as undefined; matching-priority link not checked",
             "final_value": "maturity never enters matching (opus:O01, opus:O02) and success_rate is never written "
                            "(opus:O03)",
             "reason": "Neither seat checked the paper's stated maturity→priority route against the matching "
                       "equations and pseudocode. Recorded under M (son55's 1 kept). No further rating change.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none beyond the M resolution"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v3 text and Appendix A first. Initial view: in "
                                                   "scope; evidence task; G 2, M 1–2, X 1–2, Em 1, Ec 1, Eh 1, Es 1, "
                                                   "cost 1. Before opening the seats I noted that the maturity→priority "
                                                   "claim is absent from matching and that success_rate is never "
                                                   "written.",
            "integrity_checks": "Both seats a1 on 2604.20133v3, material sha 930373b8…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: whole framework + GPT5.2 beats bare GPT5.2 on an "
                                "author-built, unnamed-judge score (3.547→4.541); the gain reverses on GPT4.1/Qwen "
                                "and nothing isolates retained skills. claim_support scoped.",
            "shared_error_review": "Agreed items re-checked: G 2, Ec 1, Eh 1, Es 1, cost 1 kept. One shared omission "
                                   "recorded (feedback signal inert).",
            "rating_agreement": "M, X and E.measurement → son55. Final 28.75.",
        },
    }

    # =========================================================== 2604.20714 TPGO (sol 61.25 / son55 53.75)
    p = "2604.20714"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Graph updates are applied atomically at each iteration by a prompt manager that supports "
                              "node rewriting, insertion, and deletion.", "Appendix C Graph representation and updates",
                    "The implemented edit set is node rewrite, insert and delete on a hierarchical JSON PromptNode tree. "
                    "§4.3's PRUNE_EDGE/ADD_EDGE (opus:O07) have no implementation counterpart, and the tree has no "
                    "explicit dependency edges (opus:O02). The 'structure-aware graph' is a sectioned prompt.",
                    kind="our_inference"),
            opus_ev(p, "O02", "Parent nodes organize sections; leaf nodes contain actual text.",
                    "Appendix D Parser prompt key instructions", "TPG nodes are prompt sections in a tree.",
                    kind="author_report"),
            opus_ev(p, "O03", "MiroFlow (GPT-5) 78.8 77.5 44.4 73.8 4014", "§5 Table 2, baseline row",
                    "Weighting the per-level rates by the stated 49/71/22 split (Appendix C) gives (78.8·49 + 77.5·71 "
                    "+ 44.4·22)/142 = 72.8, not the reported 73.8.", kind="our_inference"),
            opus_ev(p, "O04", "+ TPGO(5 iters.) 90.6 (+15.0%) 79.1 (+2.1%) 63.6 (+43.2%) 81.6 (+10.6%) 1765",
                    "§5 Table 2, 5-iteration row",
                    "The weighted mean is 80.7 vs the reported 81.6. Iteration 1 gives 69.2 vs 70.59 and iteration 3 "
                    "gives 73.3 vs 75.7 (opus:O05, opus:O06). Every reported overall exceeds the count-weighted level "
                    "mean by 0.9–2.4 points, so overall pass@1 cannot be reproduced from the paper's own breakdown. "
                    "The baseline-to-5-iteration gain is about the same either way (+7.8 vs +7.9).",
                    kind="our_inference"),
            opus_ev(p, "O05", "+ TPGO(1 iters.) 76.9 71.2 45.5 70.59 3680", "§5 Table 2, 1-iteration row",
                    "Iteration 1 is a net drop (73.8→70.59). The weighted mean is 69.2.", kind="author_report"),
            opus_ev(p, "O06", "+ TPGO(3 iters.) 82.1 73.1 54.5 75.7 2278", "§5 Table 2, 3-iteration row",
                    "The weighted mean is 73.3 vs the reported 75.7.", kind="author_report"),
            opus_ev(p, "O07", "PRUNE_EDGE(u, v)", "§4.3 Step 3 edit operations",
                    "The main text advertises edge operations that Appendix C's implementation does not list "
                    "(opus:O01).", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus: the paper's tested operation partitions the monolithic configuration into typed nodes "
                      "and the failures into clusters, then edits per cluster. Its own ablations test that partition "
                      "(w/o TPG = monolithic rewrite; random clustering), which is the card's 'partition is "
                      "load-bearing' condition (son55). GRAO retrieves past (context, edit, effectiveness) triples as "
                      "few-shot conditioning for a frozen optimizer. That is adapt_via_conditioning (sol's "
                      "supporting card), and it is the closest card for the paper's 'learn to evolve' layer. "
                      "generative_process_redesign is dropped: no staged generative procedure is redesigned. "
                      "self_supervised_signal_engineering is dropped: the signal is benchmark success and, on GAIA, "
                      "gold answers, so it is not label-free.",
            "matches": [smatch("son55", p, "heterogeneous_decomposition", role="primary"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H09"),
                                       dmatch("sol", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [],
                           "reason": "H09 (both seats). H03 (sol): GRAO stores repair records (error context, graph "
                                     "edit, effectiveness) and retrieves them by similarity, re-ranked by outcome, as "
                                     "demonstrations. son55's H15 needs a population/archive search, which is absent "
                                     "(son55's own note: 'no population/archive').",
                           "revision_proposals": seat("son55", p)["domain_pattern"].get("revision_proposals", [])},
        "pattern_mapping": [
            PM("heterogeneous_decomposition", None, "attribute_and_patch_incumbent", "H09",
               "Partitioned prompt sections + clustered textual-gradient failures → per-cluster localized node edits "
               "→ validation on the failing subset → rollback on degradation.",
               "H09 assumes component-specific critique through a computation graph. Here the 'graph' is a section "
               "tree (opus:O01) and validation reuses the failing tasks.",
               ["son55:E006", "son55:E007", "son55:E008", "opus:O01"]),
            PM("adapt_via_conditioning", None, "index_experience_for_reuse", "H03",
               "GRAO: retrieve similar past optimisation cases, rank by effectiveness, prepend as few-shot exemplars "
               "to the frozen optimizer.",
               "The effectiveness score is measured on the cluster's own failing tasks, so cases are not certified on "
               "held-out data. The only memory-off test is one single-run curve.",
               ["son55:E009", "son55:E010", "sol:E14", "son55:E018"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.20714-1"): "local:2604.20714-3",
                    ("son55", "local:2604.20714-2"): "local:2604.20714-1"},
            overrides={
                "local:2604.20714-1": {
                    "status": "partial",
                    "reason": "Opus: same holdout question in both seats (sol local-1, son55 local-2). The main "
                              "tables are on the optimised sets, and the GAIA reflector sees gold answers of the "
                              "reported tasks. Table 4's Browser-only → three unseen domains is the only held-out "
                              "test (+1.8 to +3.1 pp, single run). Partial, because a held-out test exists but is "
                              "weak.",
                    "note": "Merged here from son55:local:2604.20714-2 (same question)."},
                "local:2604.20714-3": renum("son55:local:2604.20714-1"),
                "rs:self_supervised_signal_engineering/RE-2": na(
                    "card dropped from the final match (signal not label-free). The content (no isolating "
                    "optimizer baseline) is carried by local:2604.20714-3 (unmet)."),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O03", "opus:O04"]), "C2", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: implemented edits are node rewrite/insert/delete on a section tree; edge operations are not "
            "implemented (opus:O01, opus:O07).",
            "Opus: GAIA overall pass@1 is not reproducible from per-level rates and the stated split "
            "(opus:O03–O06)."],
            evidence_level="retained",
            evidence_level_note="Both seats retained, verified narrowly. The configuration optimised on Browser "
                                "Automation only and then frozen is better on three unseen domains (+1.8/+2.7/+3.1 "
                                "pp, single run, temperature 1.0). This is the only later-task evidence; the "
                                "headline tables reuse the selection sets (EVIDENCE rule 2). improver is not "
                                "supported: the GRAO contrast is one subset, one run, on the selection set.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. 'Failures sit in tools/workflow, not one prompt' and "
                   "'optimizers do not learn from optimisation history' are concrete. The related work covers "
                   "only three APO methods; workflow/agent-design search and memory-augmented optimizers are not "
                   "positioned, and the 'first' claim cannot be checked.",
                   ["son55:E002", "son55:E003", "son55:E004", "sol:E01"]),
            "M": R("resolved", 2, "Opus sides with son55. The loop is reconstructable and the ablations make "
                   "distinguishable predictions (monolithic vs sectioned, semantic vs random clustering). Two "
                   "load-bearing explanations are thin. (1) The 'structure-aware graph' is a section tree edited "
                   "by node operations, and the edge semantics of §4.3 are not implemented (opus:O01, opus:O02, "
                   "opus:O07), so the account of why structure matters reduces to sectioned-prompt editing. (2) "
                   "'Learning to optimize' is exemplar retrieval ranked by an effectiveness score measured on the "
                   "same failing tasks. Nothing explains why that score identifies edits that generalise, or how it "
                   "prevents forgetting on other tasks.",
                   ["son55:E005", "son55:E006", "son55:E009", "son55:E010", "son55:E016", "son55:E017", "opus:O01",
                    "opus:O02"], ["opus:O07"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Prompts (App D), DBSCAN/MiniLM, the 5-iteration cap, "
                   "atomic updates, targeted rollback, memory contents and the artifact archive are given, and the "
                   "implemented chain (node operations) is reconstructable. Not 4: rollback is judged only on the "
                   "targeted subset, there is no expiry or conflict handling in the memory, and the main text's "
                   "edge operations do not match the implementation (opus:O07). The latter is recorded, but the "
                   "implementation-level chain is clear, and the weakness is scored once in M.",
                   ["son55:E005", "son55:E006", "son55:E007", "son55:E008", "son55:E009", "son55:E026"],
                   ["son55:E018", "opus:O07"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. External verifiers (MCP-Universe task "
                               "completion, GAIA exact answers), pass@1, wall-clock time. Recorded but not lowered: "
                               "GAIA overall does not reproduce from the per-level rates and stated split "
                               "(opus:O03–O06), and the text and Fig. 3 numbers mismatch slightly (son55:E019). The "
                               "gain size is unaffected.",
                               ["son55:E015", "son55:E024", "son55:E012"],
                               ["opus:O03", "opus:O04", "son55:E019"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There are component ablations and a GRAO-off "
                             "curve, but they cover one subset in one run. No other optimizer (TextGrad, PromptAgent, "
                             "EvoPrompt) is run at matched budget. The optimizer (Gemini-2.5-Pro) is stronger than "
                             "the optimised backbones, a possible knowledge-injection confound.",
                             ["son55:E016", "son55:E017", "son55:E018"], ["son55:E013", "son55:E025"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. The headline results (MCP-Universe 146 tasks; GAIA "
                           "142-task validation set) are reported on the sets used for optimisation. Edits are "
                           "validated and rolled back on those tasks, and on GAIA the reflector receives the gold "
                           "answers of the very tasks reported (A2: oracle signal → E.holdout). Only Table 4 is held "
                           "out, with +1.8 to +3.1 pp, roughly one task per domain, in one run at temperature 1.0. "
                           "Above 0 for that test; below 2 because the central claim rests on selection-set numbers.",
                           ["son55:E020", "son55:E021"], ["son55:E013", "son55:E014", "sol:E03"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). Task counts and some negative results "
                              "(iteration-1 drop, GRAO-off collapse) are reported. Every number is a single run at "
                              "temperature 1.0 with no intervals.",
                              ["son55:E024", "son55:E018", "opus:O05"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. One GAIA iteration's tokens and wall-clock are "
                        "reported (19.9M, 1380 s). The 5-iteration total, the MCP-Universe cost and baseline budget "
                        "parity are missing, and the amortised per-trajectory figure does not map to 142 tasks "
                        "(sol:E12).", ["son55:E022", "son55:E023", "sol:E12"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (Appendices A–E). In scope: system_method; prompt-graph edits are "
                  "retained across iterations and evaluated frozen on unseen domains. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "GRAO edits the optimizer's context (retrieved edit history). The only evidence is a "
                          "single-run GRAO-on/off stability curve on the selection subset, so the improver level is "
                          "not supported.",
        "figure_dependence": "Figs 1–3 are image-only. GRAO curve values are taken from §5.4 text only.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "heterogeneous_decomposition",
                "The paper's tested operation is the partition (typed sections, clustered failures) with its own "
                "uniform-treatment ablations. generative_process_redesign has no staged generative procedure here.",
                ["son55:E006", "son55:E016", "son55:E017"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["heterogeneous_decomposition", None], ["adapt_via_conditioning", None]],
                "son55's primary plus sol's GRAO-conditioning card. Dropped: generative_process_redesign (no "
                "generative procedure) and self_supervised_signal_engineering (benchmark labels and gold answers "
                "drive the signal).", ["son55:E006", "sol:E14", "son55:E013"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H09"], ["index_experience_for_reuse", "H03"]],
                "H03's repair-record retrieval matches GRAO. H15 requires population search, absent here.",
                ["sol:E14", "son55:E009", "son55:E010"], NOSCORE),
            XC(p, "local:2604.20714-1", "revised", "partial",
               "A4: sol's local-1 and son55's local-2 ask the same holdout question and are merged here as partial "
               "(Table 4 is a weak held-out test). son55's local-1 asks a different question (no matched-budget "
               "optimizer baseline) and moves to local-3 as unmet, verified.",
               ["sol:E06", "sol:E10", "son55:E013", "son55:E014", "son55:E020"]),
            XC(p, "local:2604.20714-2", "revised", "partial",
               "A4: sol's local-2 (optimizer cost accounting) stays here as partial, verified: one iteration's cost "
               "only. son55's local-2 (holdout) is merged into local-1.", ["sol:E12", "son55:E022"]),
            XC(p, "rs:heterogeneous_decomposition/RE-1", "son55", "partial",
               "Verified: the partition criteria (LLM parsing, MiniLM+DBSCAN) are generic tools.", ["son55:E006"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "partial",
               "Verified: ablations on one subset in one run.", ["son55:E016", "son55:E017"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "son55", "met",
               "Verified: the uniform-treatment (monolithic rewrite) ablation exists.", ["son55:E016"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "unmet",
               "Verified: no analysis of the node-type or cluster distribution; one case study only.",
               ["son55:E006"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "revised", "not_applicable",
               "Card dropped from the final match. The question (no isolating optimizer baseline) is carried by "
               "local:2604.20714-3 (unmet).", ["son55:E013", "son55:E025"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "partial",
               "Verified: certification uses the benchmark verifier (external), but gradients and proposals come "
               "from one model family, and GAIA uses gold answers.", ["son55:E013", "son55:E025"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "unmet",
               "Verified: nothing checks that the edited node caused the failure.", ["son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: the proposer sees a cluster description plus the graph, not raw traces.", ["son55:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "met",
               "Verified: stated for any MAS configuration; applied to ReAct and MiroFlow.", ["son55:E015"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "sol", "partial",
               "Verified: the GRAO-off curve is a store-off contrast, but one run on the selection subset.",
               ["sol:E09", "son55:E018"]),
            XC(p, "rsi:make_the_improver_editable/F3", "son55", "unmet",
               "Verified: repeated evaluation on the reported sets (claim-level check; card not matched).",
               ["son55:E014", "son55:E007"]),
            XC(p, "rsi:make_the_improver_editable/F4", "son55", "unmet",
               "Verified: single run, temperature 1.0.", ["son55:E024"]),
            XC(p, "rsi:make_the_improver_editable/S3", "son55", "partial",
               "Verified: GRAO-off is the fixed-improver contrast, on one subset in one run.", ["son55:E018"]),
            XC(p, "rsi:make_the_improver_editable/S4", "son55", "partial",
               "Verified: one iteration's cost only.", ["son55:E022"]),
            RC(p, "M", "son55", {"status": "resolved", "rating": 2},
               "See ratings.M: the structure is a section tree with no edges implemented (opus:O01), and the meta "
               "layer is exemplar retrieval scored on the failing subset.",
               ["opus:O01", "opus:O07", "son55:E010"], "−5.0 vs sol (20×1/4)"),
            RC(p, "E.holdout", "son55", {"status": "resolved", "rating": 1},
               "See ratings.E.holdout: the headline results are on optimised sets with gold-answer access, and Table "
               "4 is the only small held-out test.", ["son55:E013", "son55:E014", "son55:E021"],
               "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims.C1 / ratings.E.measurement (both seats)",
             "sol_value": "GAIA 73.8→81.6 taken as reported",
             "son55_value": "GAIA 73.8→81.6 taken as reported",
             "final_value": "overall pass@1 not reproducible from the per-level rates and the 49/71/22 split: "
                            "72.8→80.7 count-weighted. The gain is about the same.",
             "reason": "Neither seat checked the Table 2 arithmetic (opus:O03–O06). E.measurement stays 3 because "
                       "the gain size is unaffected. Recorded as a reporting defect.",
             "evidence_ids": ["opus:O03", "opus:O04", "opus:O05", "opus:O06"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text with appendices first. Initial view: in "
                                                   "scope; retained (narrow, Table 4 only); G 2, M 2–3, X 3, Em 3, Ec "
                                                   "2, Eh 1, Es 1, cost 2. Before opening the seats I noted the "
                                                   "selection=test structure with GAIA gold-answer access, the "
                                                   "node-only implementation, and the Table 2 arithmetic.",
            "integrity_checks": "Both seats a1 on 2604.20714v1, material sha f22fc684…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: optimised configurations beat the unoptimised ones on the "
                                "optimised sets; a Browser-only configuration gives small single-run gains on three "
                                "unseen domains. 'Learning to evolve' is not established. claim_support scoped.",
            "shared_error_review": "Agreed items re-checked: G 2, X 3, Em 3, Ec 2, Es 1, cost 2 kept. One shared "
                                   "omission recorded (GAIA arithmetic).",
            "rating_agreement": "M and E.holdout → son55. Final 53.75.",
        },
    }

    # =========================================================== 2604.21003 Last Harness (sol 27.5 / son55 23.75)
    p = "2604.21003"
    A1_SCOPE = ["Full pinned v3 text: Abstract, §1–4, Algorithms 1–2, Eq. 1–2, Table 1; there are no appendices and "
                "no experiment or results section. The Conclusion defers all empirical results to future work "
                "(son55:E008). No proved formal result corresponds to this item (A1)."]
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: the human-fixed evolution blueprint Λ is liberated as a design variable. Design-"
                      "level match only; the card's success conditions cannot be tested in a paper with no "
                      "experiments. No sub-card applies.",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H19"),
                                       dmatch("son55", p, "attribute_and_patch_incumbent", "H12")],
                           "unassigned": [],
                           "reason": "H19 (both): the outer loop edits the improver blueprint by the downstream "
                                     "scores of its products. H12 (son55): the inner loop has an evolution agent "
                                     "read traces and evaluator reports, classify recurring failures and edit "
                                     "harness code (tools, prompts, orchestration), keeping the best. That is the "
                                     "H12 tactic, proposed but not run.",
                           "revision_proposals": []},
        "pattern_mapping": [
            PM("generative_process_redesign", None, "make_the_improver_editable", "H19",
               "Fixed human-designed blueprint Λ (evaluator/evolver prompts, scoring, observation, loop control) "
               "→ outer meta-evolution scored by inner-loop best_score.",
               "H19 needs an immutable anchor. Λ includes the evaluator and the scoring function, so the meta-loop can "
               "edit its own objective (S1 unmet, F5 unmet).", ["son55:E003", "son55:E005", "son55:E006"]),
            PM("generative_process_redesign", None, "attribute_and_patch_incumbent", "H12",
               "Inner loop: worker executes → evaluator diagnoses against ground-truth environment state → evolution "
               "agent patches harness code from full history → best retained.",
               "Design only; the strict-improvement best rule is the only retention gate.",
               ["son55:E009", "son55:E010", "son55:E011", "son55:E017"]),
        ],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": assess("son55", p, [],
                             evidence_level=None,
                             evidence_level_note="null: no measurements at all (no task, no score, no run). This "
                                                 "is not missing material: the paper defers all empirics. son55's "
                                                 "'none' is normalised to null; sol already null.",
                             claim_support="unsupported"),
        "ratings": {
            "G": R("resolved", 1, "Opus sides with son55. The motivation (manual harness engineering, with two "
                   "practitioner reports) is real. Nearest-neighbour positioning is a single APO citation "
                   "(LLM-AutoDiff), and automated harness or agent-design search and self-modifying agents are "
                   "never discussed. No residual bottleneck of existing automated methods is identified. Between "
                   "anchor 0 (no nearest neighbour) and 2 (real limitation, incomplete comparison).",
                   ["son55:E001", "son55:E002", "sol:E01"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. The inner loop (separated evaluator and evolver, full "
                   "history, best retention) is a concrete response to manual harness engineering. Key logic is "
                   "weak: the meta-objective is final best_score but the claim is faster adaptation (son55:E006, "
                   "E007), and the meta-loop may edit the evaluator and scoring that produce its own objective, "
                   "with no immutable anchor.", ["son55:E003", "son55:E005", "son55:E006", "son55:E007"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithms 1–2, the component interfaces and the "
                   "strict-improvement best rule can be reconstructed. Aggregate, E_meta.evolve, all prompts, "
                   "models and K are unspecified, and §3 states Λ is currently fixed (the meta-loop is a proposed "
                   "generalisation).", ["son55:E009", "son55:E010", "son55:E011", "sol:E04"]),
            "E.measurement": R("not_reported", 0, "A1: no experiments; metric/verifier credibility cannot be shown.",
                               ["son55:E008", "sol:E11"], [], A1_SCOPE),
            "E.causality": R("not_reported", 0, "A1: no controls or ablations.", ["son55:E008", "sol:E11"], [],
                             A1_SCOPE),
            "E.holdout": R("not_reported", 0, "A1: a meta-train/test split is only planned.",
                           ["son55:E008", "son55:E014"], [], A1_SCOPE),
            "E.statistics": R("not_reported", 0, "A1: no results, hence no statistics.", ["son55:E008"], [],
                              A1_SCOPE),
            "E.cost": R("not_reported", 0, "A1: no cost report; the meta-loop's cost is not discussed.",
                        ["son55:E008"], [], A1_SCOPE),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text read (no appendices exist). In scope as a proposed execution-feedback "
                  "harness loop (not an incentive/theory analysis, so A3 bullet 3 does not apply). Scored under A1: "
                  "five E items not_reported 0. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope as a design of a non-weight execution-feedback loop; A1 governs E)",
        "improver_check": "The meta-loop that would edit the improver is proposed only; §3 says Λ is currently fixed. "
                          "No improver or retained evidence.",
        "figure_dependence": "Fig 1 (architecture) is image-only; not needed.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["attribute_and_patch_incumbent", "H12"], ["make_the_improver_editable", "H19"]],
                "The inner loop is the H12 tactic (trace diagnosis → code patch → best retention); H19 covers the "
                "outer loop.", ["son55:E009", "son55:E010", "son55:E011"], NOSCORE),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "unmet",
               "Verified: no evidence that the fixed blueprint limits convergence.", ["son55:E008"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "unmet",
               "Verified: no baseline of any kind.", ["son55:E008"]),
            XC(p, "rs:generative_process_redesign/RE-4", "son55", "partial",
               "Verified: a conceptual meta-learning correspondence table, not a guarantee.", ["son55:E015"]),
            XC(p, "rsi:make_the_improver_editable/F4", "son55", "unmet",
               "Verified: a single strict-greater comparison decides improved/regressed.", ["son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/F5", "son55", "unmet",
               "Verified: the meta-agent may edit the evaluator and the scoring function.", ["son55:E005"]),
            XC(p, "rsi:make_the_improver_editable/S4", "son55", "unmet",
               "Verified: meta-loop cost is not discussed.", ["son55:E008"]),
            XC(p, "rsi:make_the_improver_editable/S5", "son55", "unmet",
               "Verified: a greedy best-only lineage, with no archive.", ["son55:E009"]),
            RC(p, "G", "son55", {"status": "resolved", "rating": 1},
               "See ratings.G: nearest-neighbour positioning is a single APO citation; whole-harness/agent search "
               "is absent.", ["son55:E002", "sol:E01"], "−3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v3 text first. Initial view: in scope as a design "
                                                   "of a non-weight loop; A1 applies (no experiments, no formal "
                                                   "result). G 1–2, M 2, X 1–2, E all not_reported 0; evidence_level "
                                                   "null, unsupported.",
            "integrity_checks": "Both seats a1 on 2604.21003v3, material sha b9b54e54…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "A1 check: both seats set the five E items to not_reported 0 with a full search "
                                "scope; no formal theorem exists to lift any item. evidence_level null with reason, "
                                "claim_support unsupported.",
            "shared_error_review": "Agreed items re-checked: M 2, X 2, all E 0 kept. No shared error found.",
            "rating_agreement": "G → son55. Final 23.75.",
        },
    }

    # =========================================================== 2604.21725 AEL (sol 58.75 / son55 68.75)
    p = "2604.21725"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "episode 83 triggers an under-threshold loss that initiates the slow-window reflection; "
                              "episode 84’s reflection introduces", "Appendix S Running Case",
                    "In the flagship trace, a single under-threshold loss at episode 83 leads to a new arm at episode "
                    "84. §3.4 says memory-policy evolution fires only every 5 slow windows after window 10, when the "
                    "average TS reward of all policies is below 0.4 (son55:E008). App A.1 reports the pool's mean "
                    "training reward at about 0.49. The two trigger descriptions are incompatible, so the paper does "
                    "not uniquely specify when the retained pool changes.", kind="our_inference"),
            opus_ev(p, "O02", "LLM-generated memory retrieval policy (episode 95, seed 123).",
                    "Appendix P.2 Code Evolution Examples",
                    "The same RegimeFilteredRetrieval artefact is placed at seed 123, episode 95 here, but at seed 42, "
                    "episode 84 in §3.5/App S (opus:O01).", kind="author_report"),
            opus_ev(p, "O03", "Both artifacts were validated via AST parsing and accepted into the module pool by "
                              "LinUCB, which subsequently selected them when their context features matched.",
                    "Appendix P.2", "Admission is attributed to LinUCB, the planner bandit, which is disabled in the "
                    "main configuration. §3.2–3.4 say new memory policies enter as Thompson-Sampling arms, and §3.4 "
                    "says admission requires a syntax check plus a smoke test, not AST parsing alone.",
                    kind="our_inference"),
            opus_ev(p, "O04", "achieves only 0.46, the lowest variance among prior methods but also among the lowest "
                              "means.", "Appendix J.1",
                    "HyperAgent is 0.46 here and 0.46±0.41 in Table 16 (opus:O05), but 0.72±0.38 in Table 2(a) and "
                    "Table 5 (sol:E13), which carries the p<.001 Welch comparison. Neither value supports the "
                    "abstract's 'lowest variance among all stochastic methods' for AEL (SD 0.47).",
                    kind="our_inference"),
            opus_ev(p, "O05", "Test result (5 seeds) 0.46 ± \\pm 0.41 2.13 ± \\pm 0.47", "Appendix K.3 Table 16",
                    "Second HyperAgent value (0.46±0.41).", kind="author_report"),
            opus_ev(p, "O06", "For the main AEL benchmark configuration, the planner pool is initialized with six "
                              "built-in planners", "Appendix N",
                    "Appendix N describes a six-planner pool selected by the meta-controller for the main "
                    "configuration. §3.1 fixes the planner (opus:O07). Which configuration produced 2.13 is "
                    "therefore not uniquely stated; App B itself warns that the same configuration name carries "
                    "different protocols across result blocks (son55:E026).", kind="our_inference"),
            opus_ev(p, "O07", "The planner identity, the tool set (12 tools), and all tool implementations remain fixed.",
                    "§3.1 Which parts of the harness are learned", "Default: planner fixed.", kind="author_report"),
            opus_ev(p, "O08", "market side information (sector returns, volatility regime, cross-correlation) computed "
                              "from cached price data but", "§3.4 Slow-window reflection",
                    "Only AEL's reflection receives regime side information, and its output is injected into the "
                    "predictor's prompt. No baseline receives it, and the shuffled-reflection control (son55:E019) "
                    "scrambles alignment without removing the information channel. Diagnosis and the "
                    "information advantage are therefore not separated.", kind="our_inference"),
            opus_ev(p, "O09", "and is provably no-harm/no-gain when the best policy is stable", "Abstract",
                    "'Provably' rests on one empirical 20Newsgroups run (AEL 0.253 vs TS 0.254, p=.97). No proof is "
                    "given.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus sides with son55. The paper's own framing is 'recasting memory use as online policy "
                      "selection', solved with Thompson Sampling: the problem is recast as a well-studied object "
                      "(a bandit) whose machinery is imported. Fit is medium because no correspondence theorem is "
                      "given and A.1 concedes that cumulative TS does not track non-stationarity. Retrieved memories "
                      "and the reflection insight condition a frozen LLM (adapt_via_conditioning). "
                      "generative_process_redesign (sol) is dropped: the fixed component is a retrieval policy in a "
                      "decision pipeline, not a stage of a generative procedure.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object"),
                        smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H21"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H05")],
                           "unassigned": [],
                           "reason": "H21 (both): the retrieval-policy pool, i.e. the inner learning mechanism, is "
                                     "extended with new executable arms. H05 (son55, medium-low): retrieval becomes "
                                     "a controller decision that includes 'none'. It is taken per episode, not per "
                                     "step; son55's boundary proposal is kept.",
                           "revision_proposals": seat("son55", p)["domain_pattern"].get("revision_proposals", [])},
        "pattern_mapping": [
            PM("reframe_as_solvable_object", None, "make_the_improver_editable", "H21",
               "Memory use recast as a bandit over retrieval-policy arms; slow reflection injects new executable "
               "arms when the pool underperforms.",
               "H21 requires evaluating each inner-mechanism design by downstream learning. Here new arms only enter "
               "TS with uninformative priors; there is no held-out admission gate and no retirement, and the trigger "
               "is inconsistently specified (opus:O01).",
               ["son55:E006", "son55:E008", "son55:E009", "opus:O01"]),
            PM("adapt_via_conditioning", None, "index_experience_for_reuse", "H05",
               "Per-episode choice among retrieval policies, including no retrieval, conditions a frozen planner.",
               "H05 is step-level triggered retrieval; this is episode-level selection.",
               ["son55:E015", "son55:E009"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.21725-1"): "local:2604.21725-5"},
            overrides={
                "local:2604.21725-2": {
                    "status": "unmet",
                    "reason": "Opus (son55): the support-ticket R3 regime and the synthetic hidden arm are built so "
                              "that only reflection-injected policies can fix them, and the synthetic injection is "
                              "scripted. The gain of the new arm is not separated from its privileged availability "
                              "(opus:O08 adds the side-information channel)."},
                "rsi:make_the_improver_editable/S6": {
                    "status": "met",
                    "reason": "Opus (son55): retrieval policies are executable, swappable Python classes added as "
                              "arms."},
                "local:2604.21725-5": renum("son55:local:2604.21725-1"),
                "rs:generative_process_redesign/RE-1": na(
                    "card dropped from the final match. The content (side information and new-arm access not "
                    "isolated) is carried by local:2604.21725-2 and E.causality."),
                "rs:generative_process_redesign/RE-3": na(
                    "card dropped from the final match. The content (no end-to-end bandit swap with reflection on) "
                    "is carried by rsi:make_the_improver_editable/S3."),
            }),
        "claims": lambda c: add_counter(add_counter(add_counter(c, "C1", ["opus:O04", "opus:O05"]), "C2",
                                                    ["opus:O08"]), "C4", ["opus:O09"]),
        "assessment": assess("son55", p, [
            "Opus: the evolution trigger and arm-admission path conflict across §3.4, §3.5, App S and App P.2 "
            "(opus:O01–O03); App N vs §3.1 disagree on the planner pool (opus:O06, opus:O07).",
            "Opus: HyperAgent is reported as 0.72±0.38 and 0.46±0.41 (opus:O04, opus:O05).",
            "Opus: reflection-only market side information is an uncontrolled advantage (opus:O08)."],
            evidence_level="retained",
            evidence_level_note="Both seats retained, verified. Posteriors, memory tiers, rules and evolved arms are "
                                "frozen and read on a chronologically later 28-bar test (son55:E011, E036), with "
                                "Stateless and +Memory store-off contrasts. improver is not supported: no "
                                "matched-budget comparison shows that the evolved pool yields better later changes.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 3, "Opus sides with son55. The failure condition is specific (one retrieval policy "
                   "helps early and overloads later) and is backed by data: the best fixed policy differs by seed "
                   "(App A.1). The nearest neighbours (Reflexion, ExpeL, Meta-Reflexion, EvoTool, FactorMiner, "
                   "HyperAgent) are positioned and run as baselines, and the residue (selection fails when the pool "
                   "lacks the needed policy) is stated. Not 4: the 'joint tool+memory evolution' gap does not match "
                   "the memory-only default (son55:E030), and adaptive or learned retrieval-routing neighbours are "
                   "absent.", ["son55:E003", "son55:E004", "son55:E005", "son55:E030", "sol:E02"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. The division of labour is clear: the bandit consumes "
                   "scalar rewards, and reflection consumes trajectories to decide whether the pool lacks an arm. "
                   "The predictions are distinguishable (gain only when regimes prefer different retrieval; the "
                   "20NG boundary). Not 4: 'diagnose before prescribe', the named methodology, is never contrasted "
                   "with prescribing without diagnosis, and insight injection and arm addition are not separated.",
                   ["son55:E001", "son55:E006", "son55:E010", "son55:E019", "son55:E020"]),
            "X": R("resolved", 2, "Opus sides with sol. The learned quantities, TS update, tier promotion and pruning, "
                   "memory caps and frozen deployment are specified. The step that changes the retained harness "
                   "cannot be reconstructed uniquely. §3.4 triggers policy evolution every 5 slow windows after "
                   "window 10 when the pool's average reward is below 0.4 (son55:E008). The flagship trace triggers "
                   "on one under-threshold loss at episode 84 (opus:O01). The same artefact appears at seed 42 ep 84 "
                   "and seed 123 ep 95 (opus:O02), and admission is credited to LinUCB rather than the TS arm "
                   "mechanism (opus:O03). App N vs §3.1 disagree on whether the planner pool is active (opus:O06, "
                   "O07), and App W counts training to episode 166 against a 140-bar train split (sol:E24). New arms "
                   "have no held-out admission gate and old arms are never retired.",
                   ["sol:E04", "sol:E07", "sol:E09", "sol:E23", "son55:E007", "son55:E008", "opus:O01", "opus:O02",
                    "opus:O03", "opus:O06"], ["sol:E10", "sol:E24", "opus:O07"]),
            "E.measurement": R("resolved", 3, "Opus sides with sol. The verifiers are objective: realised returns on "
                               "a frozen test window and deterministic gold routes. Trivial baselines (EqW, "
                               "momentum) are reported. son55's main reason, the 28-bar window, is a sample-size "
                               "issue that A2 assigns to E.statistics. Not 4: reporting is inconsistent across "
                               "blocks (HyperAgent 0.72 vs 0.46, opus:O04/O05; same configuration name with different "
                               "numbers, son55:E026; pre/post-fix credit numbers), and cost-adjusted Sharpe is "
                               "approximate.",
                               ["sol:E10", "sol:E12", "sol:E20", "sol:E25", "son55:E014"],
                               ["opus:O04", "opus:O05", "son55:E026"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. The design is rich: incremental build, "
                             "reflection-off, shuffled reflection, single-policy runs, counterfactual replay and "
                             "the 20NG boundary. Key controls for the central claim (reflection's diagnosis causes "
                             "the gain) are missing. (1) Reflection alone receives market side information that "
                             "flows into the predictor prompt, and shuffling does not remove it (opus:O08). (2) The "
                             "support-ticket arm, and the synthetic hidden arm, are privileged by construction "
                             "(son55:E022, E029). (3) Diagnose-before-prescribe is never ablated. (4) Budgets are "
                             "unequal (HyperAgent about 20 evolution calls vs AEL about 400). (5) No end-to-end bandit "
                             "swap is run with reflection on (sol:E21).",
                             ["sol:E05", "sol:E17", "sol:E26", "son55:E015", "son55:E019", "son55:E037"],
                             ["sol:E08", "sol:E14", "sol:E19", "sol:E21", "son55:E022", "son55:E029", "opus:O08"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. The chronological split with frozen test "
                           "(read-only memory, no evolution) is real. However, the default configuration was chosen by "
                           "ablations reported on test Sharpe (son55:E025), App W runs training past the 140-bar "
                           "split (sol:E24), and the support stream is scored online with no split.",
                           ["son55:E011", "son55:E036", "sol:E10", "sol:E23"],
                           ["son55:E025", "son55:E024", "son55:E027", "sol:E24"]),
            "E.statistics": R("resolved", 3, "Both seats 3 (A2: multi-seed + intervals + significance tests). Five "
                              "seeds, SD, 95% CI, Welch/F tests and paired bootstrap are given, and non-significance "
                              "is reported honestly (+Memory p=.384, EvoTool p=.39). Not 4: n=5 with no "
                              "multiple-comparison correction, '4 of 9' in the text against 3 listed, and the "
                              "abstract's strong wording.",
                              ["son55:E016", "son55:E017", "sol:E12", "sol:E14", "sol:E16"], ["son55:E026", "opus:O09"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Per-run cost is about $2.80, with about $0.80 for "
                        "reflection/evolution. Baselines are not budget-matched, and cost is reported for finance "
                        "only.", ["son55:E028", "sol:E22"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read (Appendices A–W). In scope: system_method; memory-policy posteriors, "
                  "tiered memory, rules and evolved retrieval arms persist into a frozen later test. All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "The retrieval-policy pool, i.e. the inner learning mechanism, is extended, but no "
                          "comparison shows the evolved pool producing better later changes at matched budget. "
                          "Retained, not improver.",
        "figure_dependence": "Figs 1–6 are image-only. Incremental-build, ablation and robustness values are taken "
                             "from text and Tables 2–3/5–9 only.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "reframe_as_solvable_object",
                "This is the paper's own stated move ('recasting memory use as online policy selection' solved by "
                "TS).", ["son55:E006", "son55:E008"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["reframe_as_solvable_object", None]],
                "reframe plus conditioning; generative_process_redesign dropped (no generative procedure).",
                ["son55:E006", "son55:E011"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["index_experience_for_reuse", "H05"], ["make_the_improver_editable", "H21"]],
                "H05 kept at medium-low fit: retrieval, including 'none', is a learned controller decision.",
                ["son55:E009", "son55:E015"], NOSCORE),
            XC(p, "local:2604.21725-1", "revised", "unmet",
               "A4 collision. sol's local-1 (is 'provably no-harm' supported?) stays here as unmet: one empirical "
               "20NG non-difference is not a proof (opus:O09). son55's local-1 (abstract overstates the tests) is a "
               "different question; it moves to local-5 as partial, verified.",
               ["sol:E18", "opus:O09", "son55:E016", "son55:E017"]),
            XC(p, "local:2604.21725-2", "son55", "unmet",
               "Same question in both seats (new-arm privilege). Unmet: the benchmarks are constructed so that only "
               "an injected arm can succeed, and side information is unmatched (opus:O08).",
               ["son55:E022", "son55:E029", "sol:E19", "opus:O08"]),
            XC(p, "local:2604.21725-3", "son55", "unmet",
               "Verified: the same configuration name carries different numbers across blocks, and the credit "
               "results flip after the bug fix.", ["son55:E026", "son55:E027"]),
            XC(p, "local:2604.21725-4", "son55", "unmet",
               "Verified: defaults were set by ablations reported on test Sharpe.", ["son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "Verified: Stateless, +Memory, shuffled reflection and single-policy runs isolate the conditioning "
               "channel.", ["son55:E015", "son55:E019"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "met",
               "Verified: fixed policies and the momentum heuristic are reported.", ["son55:E014"]),
            XC(p, "rs:generative_process_redesign/RE-1", "revised", "not_applicable",
               "Card dropped from the final match; the content is carried by local-2 and E.causality.",
               ["sol:E08", "sol:E19"]),
            XC(p, "rs:generative_process_redesign/RE-3", "revised", "not_applicable",
               "Card dropped from the final match; the content is carried by the improver S3 check.", ["sol:E21"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "son55", "unmet",
               "Verified: no correspondence result, and A.1 concedes that TS does not track non-stationarity.",
               ["son55:E032"]),
            XC(p, "rs:reframe_as_solvable_object/RE-3", "son55", "partial",
               "Verified: standard TS use; the novelty is the coupling with reflection.", ["son55:E006"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "partial",
               "Verified: counterfactual replay and reflection-faithfulness checks, with no ground-truth "
               "intervention.", ["son55:E034", "son55:E032"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "met",
               "Verified: the pool includes none, compressed and full.", ["son55:E009"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "met",
               "Verified: Stateless vs +Memory store-off contrast.", ["son55:E015"]),
            XC(p, "rsi:make_the_improver_editable/F4", "son55", "partial",
               "Verified: 5 seeds with tests; noise remains large.", ["son55:E016"]),
            XC(p, "rsi:make_the_improver_editable/F5", "son55", "met",
               "Verified: same backbone, fixed reward. The side-information issue concerns information parity "
               "(E.causality), not anchor leakage.", ["son55:E033", "son55:E036"]),
            XC(p, "rsi:make_the_improver_editable/F6", "son55", "partial",
               "Verified: the scope is limited to regime-varying domains, but the abstract overreaches.",
               ["son55:E021", "opus:O09"]),
            XC(p, "rsi:make_the_improver_editable/S2", "son55", "met",
               "Verified: arms and insights are valued only by downstream reward.", ["son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/S5", "son55", "partial",
               "Verified: new arms get exploration; old arms are never retired.", ["son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/S6", "son55", "met",
               "Retrieval policies are executable, swappable classes; the condition asks for exactly that.",
               ["son55:E009", "son55:E007"]),
            RC(p, "G", "son55", {"status": "resolved", "rating": 3},
               "See ratings.G: the failure condition is evidenced and the neighbours are run as baselines.",
               ["son55:E004", "son55:E005"], "+3.75 vs sol (15×1/4)"),
            RC(p, "X", "sol", {"status": "resolved", "rating": 2},
               "See ratings.X: the evolution trigger and admission path are contradictory across sections "
               "(opus:O01–O03, O06).", ["opus:O01", "opus:O02", "opus:O03", "sol:E24"], "−5.0 vs son55 (20×1/4)"),
            RC(p, "E.measurement", "sol", {"status": "resolved", "rating": 3},
               "See ratings.E.measurement: the verifiers are objective; the 28-bar sample belongs to statistics "
               "(A2).", ["sol:E10", "sol:E25"], "+2.5 vs son55 (10×1/4)"),
            RC(p, "E.causality", "sol", {"status": "resolved", "rating": 2},
               "See ratings.E.causality: side information, privileged arms, the unablated diagnosis step and unequal "
               "budgets.", ["opus:O08", "son55:E022", "sol:E21"], "−3.75 vs son55 (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims.C1 (both seats)",
             "sol_value": "HyperAgent 0.72±0.38 used; 'lowest variance' contradicted by HyperAgent SD",
             "son55_value": "HyperAgent 0.72 used",
             "final_value": "HyperAgent is reported as both 0.72±0.38 (Tables 2/5) and 0.46±0.41 (App J/K, Table 16)",
             "reason": "Neither seat noticed the two HyperAgent values (opus:O04, opus:O05). Recorded under "
                       "E.measurement (sol's 3 kept). The AEL-vs-HyperAgent ordering holds under either value.",
             "evidence_ids": ["opus:O04", "opus:O05", "sol:E13"], "score_impact": "none"},
            {"field_path": "ratings.X (both seats' reasons)",
             "sol_value": "noted 140 vs 166 and mixed optional modes",
             "son55_value": "trigger and verification described as specified",
             "final_value": "trigger, admission and planner-pool descriptions conflict (opus:O01–O03, O06, O07)",
             "reason": "Neither seat cross-checked §3.4's trigger against App S, P.2 and N. This underpins the X "
                       "resolution (→ sol 2).",
             "evidence_ids": ["opus:O01", "opus:O03", "opus:O06"], "score_impact": "none beyond the X resolution"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text with Appendices A–W first. Initial view: "
                                                   "in scope; retained; G 3, M 3, X 2, Em 3, Ec 2, Eh 2, Es 3, cost 2. "
                                                   "Before opening the seats I noted the trigger and admission "
                                                   "contradictions, the side-information channel, the HyperAgent "
                                                   "values, the p=.384 reflection contrast and the 'provably' "
                                                   "wording.",
            "integrity_checks": "Both seats a1 on 2604.21725v2, material sha 1602847b…. sol is read from the "
                                "committed HEAD version whose canonical hash equals conflicts.json; the working copy "
                                "adds only E27 and a numeric display. son55 matches on disk. RS/domain ids valid; "
                                "both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: on a 28-bar frozen test (5 seeds), bandit+reflection has the "
                                "highest mean, significant over Reflexion, Meta-Reflexion and HyperAgent only. On "
                                "author-built streams, a reflection-added arm helps where the pool lacks it, and 20NG "
                                "shows no gain. claim_support scoped.",
            "shared_error_review": "Agreed items re-checked: M 3, Eh 2, Es 3, cost 2 kept. Two shared omissions "
                                   "recorded.",
            "rating_agreement": "G → son55; X, E.measurement, E.causality → sol. Final 62.5.",
        },
    }

    # =========================================================== 2604.25850 AHE (sol 67.5 / son55 70.0)
    p = "2604.25850"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Iteration 8’s overall score lands at 76.97, the run’s high-water mark on Figure",
                    "Appendix C.1.4", "The Table 1 AHE row (77.0%) is the in-loop iteration-8 evaluation: 137/178 "
                    "rollouts at k=2 (Easy 8/8, Medium 97/110, Hard 32/60; opus:O04). It is the maximum of ten noisy "
                    "evaluations on the same 89 tasks used for evolution, not a fresh re-evaluation of the selected "
                    "harness. The trajectory moved 75.8→73.0→76.97 across iterations 6–8 (son55:E035).",
                    kind="our_inference"),
            opus_ev(p, "O02", "ACE 68.9% 91.7% 78.2% 48.9%", "§4.2 Table 1, ACE row",
                    "Easy 91.7% = 11/12 and Hard 48.9% = 44/90 imply k=3 rollouts per task, unlike AHE's in-loop k=2 "
                    "(opus:O06). The baselines are single evaluations, whereas AHE's figure is a best-of-10.",
                    kind="our_inference"),
            opus_ev(p, "O03", "TF-GRPO 72.3% 100.0% 79.4% 55.6%", "§4.2 Table 1, TF-GRPO row",
                    "Medium 79.4% = 131/165 and Hard 55.6% = 50/90, i.e. k=3. The overall (12+131+50)/267 = 72.3% "
                    "is consistent.", kind="our_inference"),
            opus_ev(p, "O04", "AHE 77.0% 100.0% 88.2% 53.3%", "§4.2 Table 1, AHE row",
                    "Medium 88.2% = 97/110 and Hard 53.3% = 32/60 at k=2; overall 137/178 = 76.97% equals the "
                    "iteration-8 in-loop score (opus:O01).", kind="author_report"),
            opus_ev(p, "O05", "NexAU 0 69.7% 87.5% 78.2% 51.7%", "§4.2 Table 1, seed row",
                    "Seed: Easy 7/8, Hard 31/60, so k=2. The seed is also measured inside the loop (iteration 1).",
                    kind="author_report"),
            opus_ev(p, "O06", "Rollouts per task k k 2", "Appendix A Table 4", "The reference run uses k=2 rollouts "
                    "per task over T=10 iterations.", kind="author_report"),
            opus_ev(p, "O07", "all written in the same JSON shape and all subject to the same automatic rollback if "
                              "their predicted fixes do not appear.", "Appendix C.3",
                    "Rollback is described as automatic here and in §3.3. The Evolve prompt instead makes it a KEEP / "
                    "IMPROVE / ROLLBACK judgement by the agent (opus:O08). At iteration 7 the agent patched rather than "
                    "rolled back after a 75.8→73.0 drop (son55:E035). The retention rule, including how many predicted "
                    "fixes must land, is not uniquely specified.", kind="our_inference"),
            opus_ev(p, "O08", "** KEEP ** -- working , leave as - is - ** IMPROVE ** -- directionally correct , refine "
                              "- ** ROLLBACK + PIVOT ** -- not working at this component level",
                    "Appendix B.2 Evolve Agent prompt, step 9", "The keep/rollback decision is delegated to the "
                    "Evolve agent's judgement.", kind="author_report"),
            opus_ev(p, "O09", "terminal bench 2 leaderboard {{ date [:4] }} scores", "Appendix B.3.2 Web-research "
                    "agent prompt, search list item 1",
                    "Before evolution, the explore agent searches the Terminal-Bench 2 leaderboard and top agents' "
                    "harness code, and that research becomes a skill the Evolve agent reads. External, partly "
                    "benchmark-specific human harness knowledge enters the loop. That weakens 'minimal human prior' "
                    "and is not given to ACE/TF-GRPO.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["generative_process_redesign"],
            "outside_taxonomy": False,
            "reason": "Opus: the distinctive operation is a typed, machine-checkable inter-agent deliverable (the "
                      "change manifest's predicted fixes and at-risk tasks, plus git commits), closed by the "
                      "external verifier's next-round task outcomes. That is C25's 'typed inter-agent deliverable "
                      "→ verifier verdict → credit/selection/correction' (son55). Fit is medium: the 'solver' is a "
                      "verifier, the three roles share one model, and the loop is not ablated. sol's "
                      "generative_process_redesign (the fixed human harness liberated as a design variable) is kept "
                      "as supporting. heterogeneous_decomposition is dropped: the seven-type split is engineering "
                      "decoupling, not treatment derived from measured properties (son55's own note).",
            "matches": [smatch("son55", p, "decompose_and_delegate", role="primary"),
                        smatch("sol", p, "generative_process_redesign", role="supporting")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12")],
                           "unassigned": [],
                           "reason": "H12 (both). son55's H31 is not kept: its defining tactic is a statistically "
                                     "sound commit rule (disjoint held-out/regression gate, paired test, e-process). "
                                     "AHE commits on raw next-round deltas on the same 89 tasks at k=2, which the "
                                     "evidence_gated_retention main card explicitly excludes ('rather than ... a raw "
                                     "score delta'). Its condition checks are kept as questions about the paper's "
                                     "claimed per-edit gate.",
                           "revision_proposals": seat("son55", p)["domain_pattern"].get("revision_proposals", [])},
        "pattern_mapping": [
            PM("decompose_and_delegate", "C25", "attribute_and_patch_incumbent", "H12",
               "Agent Debugger turns traces into layered reports → Evolve agent patches files with a typed "
               "manifest of predicted fixes/regressions → the next round's verifier deltas give per-edit verdicts → "
               "keep or roll back.",
               "H12 promotes on a separate validation set; AHE promotes and reports on the same 89 tasks "
               "(opus:O01). C25 asks for a load-bearing ablation of the verification step, which is absent.",
               ["son55:E009", "son55:E010", "son55:E011", "opus:O01"]),
            PM("generative_process_redesign", None, "attribute_and_patch_incumbent", "H12",
               "The fixed human-designed harness (prompt, tools, middleware, memory) becomes the edited object, "
               "starting from a bash-only seed.",
               "Minimal seed by design (son55:E028), but external SOTA research enters through the explore agent "
               "(opus:O09).", ["sol:E03", "son55:E028", "opus:O09"]),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.25850-2"): "local:2604.25850-4",
                    ("son55", "local:2604.25850-3"): "local:2604.25850-5"},
            overrides={
                "local:2604.25850-4": dict(renum("son55:local:2604.25850-2"),
                                           reason="Opus (son55, verified): evolution, best-iteration selection "
                                                  "and the reported Table 1 all use the same 89 TB2 tasks; the "
                                                  "headline is the in-loop iteration-8 score (opus:O01)."),
                "local:2604.25850-5": renum("son55:local:2604.25850-3"),
                "rs:heterogeneous_decomposition/RE-5": na(
                    "card dropped from the final match (the partition is engineering decoupling)."),
                "rsi:evidence_gated_retention/S1": {"note": "Card not matched (no sound commit rule); kept as a "
                                                            "check question on the claimed per-edit verdict gate."},
                "rsi:evidence_gated_retention/S4": {"note": "Card not matched; kept as a check question."},
                "rsi:evidence_gated_retention/S5": {"note": "Card not matched; kept as a check question."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03", "opus:O09"]), "C4",
                                        ["opus:O07"]),
        "assessment": assess("son55", p, [
            "Opus: the headline 77.0% is the in-loop best-of-10 at k=2, while ACE/TF-GRPO cells imply k=3 single "
            "evaluations (opus:O01–O04).",
            "Opus: rollback is called automatic but is decided by the Evolve agent (opus:O07, opus:O08); Algorithm 1 "
            "evaluates H_{t-1} but stores H_t as best (sol:E08, sol:E09).",
            "Opus: the explore agent's web research on the TB2 leaderboard and top harnesses enters the loop "
            "(opus:O09)."],
            evidence_level="retained",
            evidence_level_note="Both seats retained, verified narrowly. The frozen harness, evaluated on "
                                "SWE-bench-verified (500 tasks never used in evolution), keeps success level (75.6 vs "
                                "75.2; three repositories regress) with 12% fewer tokens. That is the only later-task "
                                "evidence. Cross-model gains reuse the 89 selection tasks, and the TB2 headline is "
                                "selection-set (EVIDENCE rule 2).",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Three concrete obstacles (heterogeneous action space, "
                   "buried trajectory signal, hard-to-attribute edits). The nearest neighbours ACE and TF-GRPO are "
                   "run from the same seed. Not 4: other whole-harness or agent-archive evolution work is only "
                   "named by category, and 'observability, not capability, is the bottleneck' is asserted rather "
                   "than tested.", ["son55:E001", "son55:E002", "son55:E033", "son55:E015"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. File-level components, layered evidence and a "
                   "predictive manifest map one-to-one onto the three obstacles. The manifest's precision/recall "
                   "and the single-component swaps give distinguishable predictions. Not 4: none of the three "
                   "pillars is removed, so the central hypothesis is untested, and all roles share one model.",
                   ["son55:E001", "son55:E009", "son55:E010", "son55:E019", "son55:E023", "sol:E07"]),
            "X": R("resolved", 3, "Opus sides with sol. The workspace layout, read-only verifier/LLM config, "
                   "manifest schema, attribution-before-distillation order, git commits, full prompts (App B) and "
                   "k=2/T=10 (opus:O06) are specified. Not 4, because the retention step is not uniquely "
                   "specified. (1) Algorithm 1 evaluates H_{t-1} but assigns H_best ← H_t (sol:E08, E09). (2) "
                   "Rollback is described as automatic (opus:O07), but the Evolve prompt makes it a KEEP / IMPROVE "
                   "/ ROLLBACK judgement (opus:O08), and at iteration 7 the agent patched instead of rolling back "
                   "(son55:E035). (3) The text says all roles run at high reasoning, while App A sets the Evolve "
                   "agent to xhigh (sol:E12, E27).",
                   ["sol:E03", "sol:E04", "sol:E06", "sol:E07", "opus:O06"],
                   ["sol:E08", "sol:E09", "sol:E12", "sol:E27", "opus:O07", "opus:O08", "son55:E035"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Official TB2 verifiers (Harbor) and "
                               "SWE-bench-verified are used, and infrastructure failures count as failures. Not 4: "
                               "verifier outputs also drive the loop, so 'mirror the evaluator' rules and TB2-adjacent "
                               "memory can encode evaluator specifics.",
                               ["son55:E029", "son55:E008", "sol:E11", "sol:E28"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-seed ACE/TF-GRPO comparisons and "
                             "single-component swaps exist. The pillars are never ablated. Comparison protocols are "
                             "unequal: AHE's figure is an in-loop best-of-10 at k=2 against k=3 single evaluations "
                             "for the baselines (opus:O01–O03). External SOTA and leaderboard research enters only "
                             "AHE's loop (opus:O09, son55:E013). Evolution budgets are not matched.",
                             ["son55:E019", "son55:E020", "son55:E023", "son55:E033"],
                             ["son55:E013", "opus:O01", "opus:O02", "opus:O03", "opus:O09"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. The headline is on the selection set: 89 TB2 tasks "
                           "drive diagnosis and editing, the best of 10 in-loop iterations is chosen on the same "
                           "tasks, and that in-loop score is reported (opus:O01, opus:O04, opus:O06). The manifest "
                           "names TB2 tasks by identity. Cross-model transfer reuses those tasks. The only "
                           "independent tasks (SWE-bench-verified, 500, frozen harness) show +0.4 pp success, with "
                           "three repositories regressing, and 12% fewer tokens. A held-out test exists, hence above "
                           "1; its result is too small to carry the central claim, hence not 3.",
                           ["son55:E014", "son55:E015", "son55:E028"],
                           ["son55:E005", "son55:E007", "son55:E022", "opus:O01", "opus:O04"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). Sample sizes, per-tier/per-repo/per-round "
                              "detail and negative results are given. There is one evolution campaign, k=2, and no "
                              "intervals; the authors call the setting high-variance.",
                              ["son55:E006", "son55:E017", "son55:E026", "sol:E30"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Inference tokens, Succ/Mtok and a roughly 32 h "
                        "campaign are reported. Evolve, Debugger and explore token/$ totals and baseline budget "
                        "parity are missing.", ["son55:E007", "son55:E014", "son55:E029", "sol:E18"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 text read (all prompts, case studies, Appendices A–E). In scope: "
                  "system_method; the evolved non-weight harness persists and is evaluated frozen on "
                  "SWE-bench-verified. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "The Evolve agent and its prompt are fixed; no improver claim is made or supported.",
        "figure_dependence": "Figs 1, 3–13 are image-only. Cross-model and self-attribution numbers are taken from "
                             "the §4.3/§4.4.2/App D text only.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "The typed manifest closed by verifier verdicts is the paper's distinctive move (C25).",
                ["son55:E009", "son55:E010", "son55:E011"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["decompose_and_delegate", "C25"], ["generative_process_redesign", None]],
                "son55's C25 primary plus sol's generative_process_redesign as supporting; heterogeneous_"
                "decomposition dropped (engineering decoupling).", ["son55:E009", "sol:E03"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H12"]],
                "H31 needs a statistically sound commit rule; AHE commits on raw same-set deltas.",
                ["son55:E010", "opus:O01"], NOSCORE),
            XC(p, "local:2604.25850-2", "revised", "partial",
               "A4 collision. sol's local-2 (pseudocode index and role-setting conflicts) stays here as partial, "
               "verified. son55's local-2 (same-set selection) is a different question; it moves to local-4 as "
               "unmet, verified by opus:O01.", ["sol:E08", "sol:E09", "sol:E27", "son55:E005", "opus:O01"]),
            XC(p, "local:2604.25850-3", "revised", "unknown",
               "A4: son55's local-3 (baseline budget/prior parity) is renumbered to local-5, unknown kept: the paper "
               "does not say whether ACE/TF-GRPO received the explore agent's SOTA skills (opus:O09).",
               ["son55:E013", "opus:O09"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Verified: inference tokens are reported; evolution-phase cost is not.", ["son55:E014"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: component swaps exist; the pillars are not ablated.", ["son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "met",
               "Verified: prompts, hyperparameters and repository are released in the paper.", ["son55:E008"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: SWE +0.4 pp; cross-model results reuse the TB2 tasks.", ["son55:E015", "son55:E032"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "Verified: same-seed baselines, with budget and prior parity unstated.", ["son55:E033"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "Verified: swaps support the components; observability as the bottleneck is untested.",
               ["sol:E21", "sol:E22"]),
            XC(p, "rs:generative_process_redesign/RE-3", "sol", "partial",
               "Verified: no debugger-off, manifest-off or rollback-off ablation.", ["sol:E21"]),
            XC(p, "rs:generative_process_redesign/RE-5", "sol", "partial",
               "Verified: optimizer cost is not totalled.", ["sol:E13", "sol:E18"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "revised", "not_applicable",
               "Card dropped from the final match.", ["son55:E019"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "met",
               "Verified: official verifiers certify edits (avoided).", ["son55:E029"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "Verified: TB2 is reused for selection and reporting; SWE is a frozen transfer with a small effect.",
               ["sol:E11", "sol:E17", "sol:E18"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S2", "son55", "partial",
               "Verified: k=2 is spread evenly; evaluation is not steered.", ["son55:E030"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "met",
               "Verified: stated for any NexAU coding-agent harness.", ["son55:E008"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "partial",
               "Verified: predicted-fix ∩ observed flips approximates a counterfactual without paired runs.",
               ["son55:E010"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "unmet",
               "Verified: the manifest/verdict/rollback gate is not ablated.", ["son55:E010"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial",
               "Verified: wall-clock time only; no evolution token cost.", ["son55:E007"]),
            RC(p, "X", "sol", {"status": "resolved", "rating": 3},
               "See ratings.X: the best-assignment index and the automatic-vs-discretionary rollback leave retention "
               "underspecified.", ["sol:E09", "opus:O07", "opus:O08"], "−5.0 vs son55 (20×1/4)"),
            RC(p, "E.holdout", "son55", {"status": "resolved", "rating": 2},
               "See ratings.E.holdout: the headline is an in-loop best-of-10 on the selection set, and the only "
               "independent test is +0.4 pp.", ["opus:O01", "son55:E015", "son55:E005"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims.C1 (both seats)",
             "sol_value": "77.0% read as the selected configuration's score",
             "son55_value": "77.0% read as the best-iteration configuration (winner's curse noted, not quantified)",
             "final_value": "77.0% = 137/178, the in-loop iteration-8 score at k=2 (max of 10); ACE/TF-GRPO cells imply "
                            "k=3 single evaluations",
             "reason": "Neither seat derived the rollout counts from the cell values (opus:O01–O05). This "
                       "strengthens the E.holdout resolution (→ 2) and the agreed E.causality 2. No other rating "
                       "change.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O06"],
             "score_impact": "none beyond the E.holdout resolution"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v4 text first, including all prompts and case "
                                                   "studies. Initial view: in scope; retained (narrow: SWE "
                                                   "tokens, flat success); G 3, M 3, X 3, Em 3, Ec 2, Eh 2, Es 1, "
                                                   "cost 2. Before opening the seats I noted Algorithm 1's best "
                                                   "index, the rollback ambiguity and the in-loop headline.",
            "integrity_checks": "Both seats a1 on 2604.25850v4, material sha 5df22cf3…. The sol file is untracked "
                                "and was rewritten after conflicts.json; its bound version was rebuilt (E31/E32 "
                                "removed, display string restored) and reproduces the conflicts.json canonical hash "
                                "exactly. son55 matches on disk. RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: in one campaign, the selected harness scores above seed "
                                "and baselines on the 89 evolution tasks (in-loop best-of-10). Frozen on SWE-bench "
                                "it keeps success (+0.4 pp) with 12% fewer tokens. 'Observability is the bottleneck' "
                                "and 'general engineering experience' are not established. claim_support scoped.",
            "shared_error_review": "Agreed items re-checked: G 3, M 3, Em 3, Ec 2, Es 1, cost 2 kept. One shared "
                                   "omission recorded (headline protocol).",
            "rating_agreement": "X → sol; E.holdout → son55. Final 65.0.",
        },
    }

    return S
