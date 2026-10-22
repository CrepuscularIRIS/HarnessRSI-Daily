"""Opus rulings for r13b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat-input integrity (controller action needed): the sol working copy of "
        "seats/sol/attempts/a1/2604.00931.json was rewritten at 20:30:57 local, after conflicts.json (20:23:41). "
        "Its canonical hash no longer equals conflicts.json seat_record_hashes (35ddf9d2…). The committed HEAD "
        "version does match, and this aggregate is bound to it (read with git show, read-only). The rewrite adds a "
        "second domain match (H28), one signature, one expectation and corrects two evidence locators; ratings and "
        "score (55.0) are unchanged, and sol's own batch-report now cites the rewritten file (sha256 893a1cc5…). "
        "A closed attempt must not be edited in place: restore the committed file, or register the edit as sol a2 "
        "and recompute conflicts. The PsychAgent final already carries H28 (from son55), so a re-aggregation "
        "against the edit is not expected to change any decision.",
        "2604.00830 Meta-TTL: evidence_level improver confirmed under a strict reading of EVIDENCE.md. (1) The edited "
        "object is the improver: the meta-prompt φ governs the meta-agent that rewrites the actor prompt between "
        "episodes, and that guidance is the only state carried between episodes. (2) Comparable budget: the Naive "
        "meta-agent has the same architecture, the same GPT-5 meta-agent and Gemini-3-Flash actor, and the same "
        "episode protocol; only φ differs (φ0 vs φ*). (3) More effective subsequent changes: higher W-AUC and "
        "average score on whole held-out games/sites/domains (Jericho OOD 0.414 vs 0.286, WebArena OOD 0.766 vs "
        "0.722, τ²-Telecom 0.583 vs 0.433), on held-out instances for WebArena/τ², with an independently "
        "meta-trained GLM-5.3-Flash replication. Scope limits are kept: one meta-training run per benchmark, OOD "
        "only within each benchmark family, Jericho ID reuses the meta-training games, and φ0 is not disclosed. "
        "This is the first improver label in the run; STOP and metaTextGrad were held at retained because they "
        "lacked exactly this edited-vs-fixed comparison at comparable budget.",
        "2603.26664 Learning to Commit (seat Δ8.75): final 48.75. M → sol 3; E.measurement → sol 2; E.causality → "
        "son55 1; E.holdout → sol 2. Opus adds a holdout channel neither seat found: the by_category curriculum "
        "pairs each test task with learning commits of 'its own category', and every commit's category is assigned "
        "by an LLM that reads the full (oracle) patch. Shared omission recorded under E.measurement (no rating "
        "change): the Table 3 'overall' win rate is undefined and cannot be derived from the Table 4 per-dimension "
        "rates, and the promised judge-agreement rates are never given.",
        "2603.28052 Meta-Harness (Δ2.5): final 71.25. M → son55 3 (the raw-trace prediction is tested; the "
        "full-history and agentic-access parts of the hypothesis are not separated from it). E.statistics → sol 1 "
        "(the medians and '>ZS' counts are candidate-level within a single search, not repeated runs). E.cost → "
        "son55 2 (evaluation-count matching plus deployed-context cost against baselines; proposer tokens/dollars "
        "absent; r10a MemEvolve / r11b AutoHarness convention). Domain → H12 + H21 + H14 (H16 and H17 dropped). "
        "TerminalBench-2 stays task-level (search set = test set). The 'five held-out models' wording includes the "
        "selection model.",
        "2604.00830 Meta-TTL (Δ6.25): final 73.75 (= son55). E.causality and E.holdout → son55 3. RS → sol "
        "(generative_process_redesign primary with C03 supporting; the taxonomy maps make_the_improver_editable to "
        "this card). Domain → H19 + H10 + H31.",
        "2604.00901 HERA (Δ3.75): final 47.5. M → son55 2; E.holdout → son55 2 (standard splits plus two OOD sets; "
        "the unstated test-time freeze is recorded as an unresolved leak route, in line with r11a ReCreate); "
        "E.statistics → sol 1 (A2 ladder tier 1: split sizes and negative results are given, uncertainty is not). "
        "RS → son55 (adapt_via_conditioning null + decompose_and_delegate null, the r08b convention for frozen-model "
        "curated memory). Domain → H00 + H01 + H09.",
        "2604.00931 PsychAgent (Δ11.25): final 42.5, below both seats (55.0 / 43.75). M, E.measurement and "
        "E.causality → son55 (2/2/1): the RFT reward and the evaluation follow the same PsychEval LLM-judge "
        "protocol, there is no same-backbone SFT-only arm or initial-vs-evolved library arm, and the ablation drops "
        "(≤0.52) are far smaller than the gaps to baselines (1.07–1.44). Shared correction E.cost 1 → not_reported "
        "0: hardware, N=8 and epochs are settings, not cost (UI-Mem r12a precedent). In scope under A3 bullet 2 "
        "(the evolved skill tree is a retained non-weight component evaluated by the w/o SEE ablation); "
        "evidence_level task. RS → adapt_via_conditioning/C03 primary + self_supervised_signal_engineering/C08 "
        "supporting (skill-library-plus-training convention, r12a/r12b).",
        "A4 hygiene: hidden local-ID collisions renumbered or merged in all five papers; every merge and move is "
        "recorded in the resolution for the affected ID.",
        "Expectations from cards that are not retained as pattern matches (controlled_diagnostic_design in "
        "2603.26664; search_agent_architecture in 2603.28052) are kept as check questions with a note; they never "
        "score directly.",
        "Figure dependence: Meta-Harness Figures 1, 3, 4 and 7, Meta-TTL Figure 3, HERA Figures 2–8 and PsychAgent "
        "Figures 2–3 are image-only. Only values stated in the text or tables are used.",
        "No material requests. Seats' requests for neighbour originals (GEPA, LAMER/MR-Search/LSE, training-free "
        "GRPO, TheraMind, ELL) are non-blocking: no disputed rating depends on them.",
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

    def moved(old, new):
        return {"note": f"Merged here from {old} (A4: same question under a colliding or different ID)."}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on *_pattern.matches)."}

    # =========================================================== 2603.26664 Learning to Commit (Δ8.75)
    p = "2603.26664"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "each retained commit is then assigned a primary category label by an LLM that considers "
                              "the commit title, the rationale, and the full patch content",
                    "§3.4 Dataset Construction, stage (iii)",
                    "Every commit's category, including the 7 test commits, is derived from its oracle patch."),
            opus_ev(p, "O02", "each test task is paired either with learning commits strictly from its own category",
                    "§4.1 Experimental design and baselines",
                    "In the by_category conditions the skill curriculum for a test task is chosen with the test task's "
                    "patch-derived label, an information channel from the held-out oracle into skill building that "
                    "neither seat noted.", kind="our_inference"),
            opus_ev(p, "O03", "Across all four settings, Q3 (redundancy and hallucination) shows the most consistent "
                              "skill advantage (39–69% win rate), with high inter-judge agreement.",
                    "§4.2 Multi-dimensional LLM judge",
                    "Judge agreement is asserted ('high') but never quantified, although §3.5 promises agreement rates."),
            opus_ev(p, "O04", "Overall pairwise win rates (%) of the skill-conditioned agent, as judged by two "
                              "independent LLMs.",
                    "Table 3 caption",
                    "The 'overall' rate is not defined. For par-bycat, Table 4's per-dimension skill wins (25/50/54/27, "
                    "judge-averaged) average 39%, or about 51% with ties excluded, while Table 3 gives 54%/57%; the "
                    "overall rate cannot be derived from the dimension table.", kind="our_inference"),
            opus_ev(p, "O05", "71% / 71%", "Table 2, seq-bycat row (File IoU)",
                    "The no-skill base agent is the same configuration in all four rows, yet its File IoU is "
                    "61/68/72/71% and its steps 71.9/62.7/68.3/76.4: rerun spread of ~11 points, the same order as the "
                    "reported gains (+19/+12/+9/0).", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning (sub null; no upstream phase trains a reader of a canonical "
                      "schema and there is no category holdout, so C03 is not assigned, r04b convention). son55's "
                      "controlled_diagnostic_design/C02 is not kept: C02 builds an instrument whose headline is the gap "
                      "between apparent and de-confounded performance, whereas the time split here is a leakage "
                      "control around a method result, and the benchmark is unreleased with 7 test tasks.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"][0]), "son55"),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.26664-1"): "rs:adapt_via_conditioning/RE-2",
                    ("sol", "local:2603.26664-2"): "rs:adapt_via_conditioning/RE-3",
                    ("sol", "local:2603.26664-3"): "local:2603.26664-1",
                    ("sol", "local:2603.26664-4"): "local:2603.26664-2"},
            overrides={
                "local:2603.26664-1": {"status": "unmet",
                                       "reason": "Opus: the abstract lists functional correctness and internal API "
                                                 "reuse rate, but neither is reported; style is judged only by LLMs "
                                                 "(base agent ahead on Q4) and there is no human or maintainer check.",
                                       **moved("sol:local:2603.26664-3", "")},
                "local:2603.26664-2": {"status": "unmet",
                                       "reason": "Opus: n=7, single runs, no intervals; the no-skill base agent itself "
                                                 "varies 61–72% File IoU across rows (opus:O05).",
                                       **moved("sol:local:2603.26664-4", "")},
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "partial",
                    "reason": "Opus: the temporal split structurally keeps test commits out of skill building, and the "
                              "repository is internal. But 'zero data leakage' is asserted, test issues are LLM-written "
                              "from the oracle diff, and the by_category curriculum is chosen with test-patch-derived "
                              "labels (opus:O01, opus:O02).",
                    **moved("sol:local:2603.26664-1", "")},
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "unmet",
                    "reason": "Opus: the only control is no skill document. No raw-diff/commit-RAG, oracle-summary or "
                              "unsupervised-reflection arm.",
                    **moved("sol:local:2603.26664-2", "")},
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "unmet",
                    "reason": "Opus: edits are grounded in the oracle diff but no entry is tested, filtered or rolled "
                              "back before reuse; grounding is S3, not a gate."},
                "rsi:abstract_experience_into_guidance/H00.step4": {
                    "status": "partial",
                    "reason": "Opus (revised from met): the time split separates the streams, but in the by_category "
                              "conditions the test task's oracle-derived label selects the curriculum "
                              "(opus:O01, opus:O02)."},
                "rs:controlled_diagnostic_design/RE-3": dropped_card("controlled_diagnostic_design"),
                "rs:controlled_diagnostic_design/RE-4": dropped_card("controlled_diagnostic_design"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O05", "opus:O02"]), "C3", ["opus:O03", "opus:O04"]),
        "assessment": assess("son55", p, [
            "Opus: by_category conditions select the skill curriculum with the test task's patch-derived category "
            "(opus:O01, opus:O02).",
            "Opus: the Table 3 'overall' win-rate definition and the judge-agreement numbers are not reported."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The bottleneck (snapshot-only context, conventions learned "
                   "from history) is concrete and SWE-Bench-CL/RepoMem/Coeditor are named, but the 'unsupervised "
                   "reflection accumulates errors' residual is cited, not shown, and general experience-memory/skill "
                   "neighbours appear only as citation numbers.", ["son55:E005", "son55:E018", "sol:E10", "sol:E11"]),
            "M": R("resolved", 3, "Opus sides with sol. Blind attempt → oracle-diff contrast → CRUD skill edits targets "
                   "the agent's own gaps, and the paper states a prediction that separates it from passive history "
                   "('Unlike static RAG over commit histories … calibrated to the agent's own capability gaps'). M "
                   "grades the logic, not its test, which belongs to E.causality. Not 4: skill format, granularity "
                   "and the parallel merge are not shown, and 'larger discrepancy = richer signal' is an untested "
                   "premise.", ["sol:E01", "sol:E02", "sol:E03", "son55:E003", "son55:E004"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Write/read chain reconstructible; no entry gate, "
                   "versioning, rollback, conflict handling or size bound; the parallel pairwise merge and skill "
                   "format are unspecified.", ["sol:E01", "sol:E03", "son55:E003", "son55:E004"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. File IoU is a deterministic, valid localisation "
                               "measure, and two judge families score against the oracle diff. It is not higher: the "
                               "promised functional-correctness and API-reuse metrics are missing, judge agreement is "
                               "asserted but never quantified (opus:O03), the Table 3 'overall' rate is undefined "
                               "(opus:O04), and line deviation is a size proxy. It is not 1, because the localisation "
                               "metric needs no judge and is the paper's clearest result.",
                               ["sol:E06", "sol:E08", "son55:E011", "son55:E013", "son55:E014", "opus:O03", "opus:O04"],
                               ["son55:E002", "son55:E019"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. The paper's distinguishing ingredient, oracle-"
                             "supervised contrast versus passive history or unsupervised reflection, has no control: "
                             "the only arm is 'no skill document', which also receives no onboarding budget. Its "
                             "outcome is mixed (seq-bycat 0 File IoU gain, Claude judge 26%). Noise is charged under "
                             "E.statistics, not here.",
                             ["son55:E010", "son55:E011", "son55:E013", "sol:E05"], ["son55:E014", "sol:E07"]),
            "E.holdout": R("resolved", 2, "Opus sides with sol, for a reason neither seat gave. The strict time split "
                           "and internal repository support later-task use. But by_category pairs each test task "
                           "with learning commits from its own category, and that category comes from an LLM reading "
                           "the test commit's full patch (opus:O01, opus:O02). All four conditions are reported on the "
                           "same 7 test tasks with seq-all foregrounded, and 'zero leakage' is asserted, not audited. "
                           "son55's 3 did not see the label channel.",
                           ["sol:E04", "sol:E09", "son55:E006", "son55:E009", "opus:O01", "opus:O02"], ["son55:E007"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): n=7 and negative cases (seq-bycat, Q1/Q4, "
                              "case study) are reported; single runs with no interval, while the conclusion says "
                              "'significantly'. The base agent's own rerun spread (opus:O05) is of the same order as "
                              "the gains.", ["sol:E04", "sol:E12", "son55:E009", "son55:E017", "opus:O05"]),
            "E.cost": R("resolved", 1, "Both seats 1. Solve-phase tool calls are measured (56.8 vs 71.9 in seq-all), "
                        "but the onboarding cost (24 Opus 4.6 attempts plus reflection and merges) is absent and no "
                        "budget-matched comparison exists.", ["sol:E06", "son55:E011"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (no appendix exists). In scope (system_method): a non-weight skill "
                  "document is written from execution feedback (blind attempt vs oracle diff), retained, and read on "
                  "later held-out commits with a store-off control. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 1 is a schematic; all results are in Tables 2–4.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "C02 is a confound-isolating diagnostic whose headline is the de-confounded gap; this paper's time "
                "split is a leakage control for a method result. See rs_pattern.reason.", ["son55:E006"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "Both apply: H00 for distilling the agent's own contrast with the oracle into lessons, H01 for the "
                "explicit create/revise/deprecate editing of one living document (r03a H00/H01 boundary).",
                ["sol:E01", "sol:E02", "son55:E003"], NOSCORE),
            XC(p, "local:2603.26664-1", "son55", "unmet",
               "A4 collision: sol's local-1 (holdout audit) and son55's local-1 (missing functional-correctness / API "
               "metrics) differ. Final local-1 = son55's question, unmet (verified). sol's holdout question merged "
               "into rs:adapt_via_conditioning/RE-2; sol's local-3 (measurement) merged here.",
               ["son55:E002", "sol:E08"]),
            XC(p, "local:2603.26664-2", "son55", "unmet",
               "A4 collision: sol's local-2 (cheaper-alternative control) and son55's local-2 (statistics) differ. "
               "Final local-2 = statistics, unmet. sol's local-2 merged into rs:adapt_via_conditioning/RE-3; sol's "
               "local-4 (statistics) merged here.", ["son55:E011", "opus:O05"]),
            XC(p, "local:2603.26664-3", "revised", {"moved_to": "local:2603.26664-1", "status": "unmet"},
               "sol's measurement-validation question is son55's local-1. Merged; status unmet, because the promised "
               "functional and API-reuse metrics are absent rather than partially reported.", ["sol:E08", "son55:E002"]),
            XC(p, "local:2603.26664-4", "revised", {"moved_to": "local:2603.26664-2", "status": "unmet"},
               "sol's statistics question is son55's local-2. Merged; unmet in both.", ["sol:E04"]),
            XC(p, "local:2603.26664-5", "sol", "partial",
               "Cost (sol only). Verified: solve-phase tool calls only; onboarding cost absent.", ["sol:E06"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "partial",
               "Verified, with the Opus by_category label channel added (opus:O01, opus:O02). sol's local-1 merged "
               "here.", ["son55:E006", "son55:E007", "opus:O01", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no raw-diff, commit-RAG, oracle-summary or unsupervised-reflection arm. sol's local-2 merged "
               "here.", ["son55:E010"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: the four conditions vary the source corpus but results are inconsistent and not "
               "single-variable.", ["son55:E011", "son55:E013"]),
            XC(p, "rs:controlled_diagnostic_design/RE-3", "son55", "unmet",
               "Kept as a check question (card not retained as a match). Verified: no shuffled/empty-skill or "
               "length-only null baseline.", ["son55:E011"]),
            XC(p, "rs:controlled_diagnostic_design/RE-4", "son55", "partial",
               "Kept as a check question. Verified: one judge shares the agent's model family; agreement is not "
               "quantified (opus:O03).", ["son55:E015", "opus:O03"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: the loop is generic; the domain-specific element (oracle supervision) is argued but not "
               "isolated.", ["son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step4", "revised", "partial",
               "son55 wrote met. The time split separates streams, but the by_category curriculum uses the test "
               "task's oracle-derived label (opus:O01, opus:O02).", ["son55:E006", "opus:O01", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step5", "son55", "partial",
               "Verified: store-off exists; no budget match, variance, or alternative abstraction.", ["son55:E010"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: names a specific fixed object (repository conventions invisible in a snapshot) but also "
               "lists 'training-free' as a contribution.", ["son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: expert-approved oracle diffs ground every edit.", ["son55:E003", "sol:E02"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "S5 asks for a gate on what is kept. Oracle grounding is S3; no entry is tested, filtered or rolled "
               "back before reuse. sol's partial credited grounding.", ["son55:E003", "sol:E01"]),
            res("ratings.M", *C(p, "ratings.M"), "sol", 3,
                "See ratings.M: the mechanism and its separating prediction are stated; the test of that prediction "
                "is charged in E.causality.", ["sol:E01", "sol:E02", "son55:E004"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement: deterministic File IoU keeps it at 2; missing promised metrics and "
                "unquantified judge agreement keep it below 3.",
                ["sol:E06", "son55:E002", "opus:O03", "opus:O04"], "+2.5 vs son55 (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality: the claimed causal ingredient has no control and the single store-off "
                "contrast is outcome-mixed. sol's 2 credited the store-off contrast as if it isolated the mechanism.",
                ["son55:E010", "son55:E013"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", 2,
                "See ratings.E.holdout: the time split is real, but the by_category curriculum is chosen with "
                "test-patch-derived labels (Opus finding) and conditions are compared on the test set.",
                ["opus:O01", "opus:O02", "sol:E09"], "−2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "2 (no overall-rate note)",
             "son55_value": "1 (no overall-rate note)", "final_value": 2,
             "reason": "Shared omission, no rating effect beyond the resolution. The Table 3 'overall' win rate is "
                       "undefined and cannot be derived from Table 4 (par-bycat dimension wins average 39%, ~51% "
                       "without ties, vs 54%/57%; opus:O04). Recorded in E.measurement.",
             "evidence_ids": ["opus:O04"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; retained via "
                                                   "store-off on 7 future tasks. G 2, M 2–3, X 2, Em 1–2 (promised "
                                                   "metrics missing), Ec 1, Eh 2 (by_category uses patch-derived test "
                                                   "labels), Es 1, E.cost 1.",
            "integrity_checks": "Both seats a1 on 2603.26664v1, material sha 6d28d05d…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: on one internal repository, skill-conditioned Opus 4.6 has "
                                "higher File IoU and smaller patches in 3 of 4 conditions on 7 later tasks. 'Retained' "
                                "is the right label type (store-off on later tasks), but the evidence is thin and "
                                "within rerun noise; claim_support scoped.",
            "rating_agreement": "G, X, Es, E.cost agree and were re-checked; M and Em → sol, Ec → son55, Eh → sol (on "
                                "an Opus-found ground). Final 48.75.",
        },
    }

    # =========================================================== 2603.28052 Meta-Harness (Δ2.5)
    p = "2603.28052"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "we evaluate the same retrieval harness on four models not seen during search",
                    "§4.2", "Only four executors are unseen; the abstract's 'five held-out models' counts the "
                            "GPT-OSS-20B selection model."),
            opus_ev(p, "O02", "number of runs whose accuracy exceeded the zero-shot baseline",
                    "Table 3 caption",
                    "With 20 iterations × 2 candidates per search (§4.1), the 26/23/39 counts and the median/best "
                    "values describe candidates within one search per condition, not repeated searches.",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: generative_process_redesign, sub null. The conventionally fixed feedback interface "
                      "of text optimizers (scores/summaries) is replaced by full raw history, and the harness code "
                      "itself becomes the search variable; run convention for trace-reading harness editors (r11a "
                      "ReCreate, r03b SICA). Not outside_taxonomy: this is not black-box population search over "
                      "model-input text (r08b), because the proposer diagnoses traces.",
            "matches": [smatch("sol", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("sol", p, "make_the_improver_editable", "H21",
                                              fit="medium (classification online-memory and math retrieval harnesses)"),
                                       dmatch("son55", p, "population_search_executable_fitness", "H14")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"][0]), "son55"),
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "make_the_improver_editable", "domain_sub": "H21",
             "operation_correspondence": "The fixed inner learning mechanism of the online classifier (how labelled "
                                         "examples are stored, retrieved and shown) becomes an executable search "
                                         "variable evaluated by downstream accuracy.",
             "conditions_or_differences": "The outer proposer and evaluator stay fixed (S1); the discovered memory "
                                          "update itself is simple, the gains come from retrieval/prompt construction.",
             "evidence_ids": ["sol:E03", "sol:E07", "sol:E08"]},
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "population_search_executable_fitness", "domain_sub": "H14",
             "operation_correspondence": "Whole-file harness programs are proposed by an LLM agent, scored by an "
                                         "executable evaluator and archived with a Pareto frontier.",
             "conditions_or_differences": "No parent-selection rule or mutation operators; the search-level novelty "
                                          "is the raw-history interface (S1).",
             "evidence_ids": ["son55:E007", "son55:E012"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.28052-2"): "rsi:search_agent_architecture/S6",
                    ("sol", "local:2603.28052-3"): "rsi:population_search_executable_fitness/H14.step5",
                    ("sol", "local:2603.28052-4"): "rs:generative_process_redesign/RE-5"},
            overrides={
                "local:2603.28052-1": {"status": "partial",
                                       "reason": "Opus: same question in both seats. The optimizer comparison is "
                                                 "evaluation-count matched with the same proposer, but only on the "
                                                 "search set and not proposer-token matched."},
                "rsi:search_agent_architecture/S6": {
                    "status": "partial",
                    "reason": "Opus: classification test + 9 OOD datasets and math with 4 unseen executors certify "
                              "away from the search set; TerminalBench-2 does not (search = test).",
                    "note": moved("sol:local:2603.28052-2", "")["note"] + " "
                            + dropped_card("search_agent_architecture")["note"]},
                "rsi:search_agent_architecture/H17.step4": dropped_card("search_agent_architecture"),
                "rsi:population_search_executable_fitness/H14.step5": {
                    "status": "unmet", "reason": "Opus: no independent search seeds or test intervals (opus:O02).",
                    **moved("sol:local:2603.28052-3", "")},
                "rs:generative_process_redesign/RE-5": {
                    "status": "partial",
                    "reason": "Opus: Best-of-N and evaluation-count matching exist; the proposer's ~10 MTok/iteration "
                              "context and the hand-debugged skill are not matched or costed.",
                    **moved("sol:local:2603.28052-4", "")},
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "partial",
                    "reason": "Opus: no acceptance gate or rollback, but nothing overwrites earlier wins: every "
                              "candidate is archived and the frontier is retained."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C5", ["opus:O01"]), "C3", ["opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: the abstract's 'five held-out models' includes the selection model; four executors are unseen "
            "(opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Quantified feedback-compression gap (Table 1), named "
                   "neighbours with stated differences; neighbour originals not pinned and the non-agentic-same-"
                   "information residual not separated.", ["son55:E004", "son55:E005", "son55:E006", "sol:E01", "sol:E19"]),
            "M": R("resolved", 3, "Opus sides with son55. The raw-trace hypothesis yields a separating prediction that "
                   "Table 3 tests (traces ~50 vs scores/summary ~35). But the stated mechanism is three things at "
                   "once (full history, agentic selective access, raw traces), and only the third is distinguished "
                   "from its naive alternative; the authors also call the skill text the strongest lever. Not 4.",
                   ["son55:E001", "son55:E018", "son55:E037", "sol:E06"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithm 1, directory layout, interface validation, "
                   "frontier and selection rule reconstructible; no regression guard or rollback; search-set size "
                   "250 vs 88 inconsistent (sol:E16, son55:E039).", ["sol:E02", "sol:E03", "sol:E04", "son55:E007",
                                                                       "son55:E038"], ["sol:E16"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Standard dataset metrics and the official "
                               "TerminalBench-2 verifier; accuracy and context cost reported together. Not 4: proof-"
                               "problem grading follows prior work without description, and TB2 baselines are "
                               "leaderboard values. The run's text–table cap is not applied: the 250/88 search-set "
                               "discrepancy is a protocol description (charged in X), not a reported result.",
                               ["son55:E015", "son55:E020", "son55:E024", "sol:E07", "sol:E08"], ["son55:E032"]),
            "E.causality": R("resolved", 3, "Both seats 3; re-checked. Information-interface ablation, same-proposer "
                             "evaluation-matched optimizers and Best-of-N on classification; math vs BM25 +1.3 only; "
                             "TB2 compares against leaderboard entries while the in-search Terminus-KIRA run scored "
                             "64.4%.", ["son55:E014", "son55:E015", "son55:E018", "sol:E05"],
                             ["son55:E026", "son55:E032"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Classification test sets held out, 9 OOD datasets; "
                           "math corpus decontaminated, 200 new problems and four unseen executors (opus:O01). "
                           "TerminalBench-2 is search = test and stays task-level.",
                           ["son55:E013", "son55:E024", "sol:E15", "opus:O01"], ["son55:E028"]),
            "E.statistics": R("resolved", 1, "Opus sides with sol (A2 ladder). The medians, best values and '>ZS' "
                              "counts describe candidates within one search per condition (opus:O02); math averages "
                              "three samples without variance. Sample sizes and negative results (USPTO, dense-"
                              "retrieval regressions, crashed iteration) are given, but no main result has an "
                              "interval or repeated-run count. Level 2 needs test intervals or repeated-run failure "
                              "counts.", ["sol:E06", "sol:E09", "son55:E018", "son55:E025", "opus:O02"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Deployed context cost is measured against every "
                        "baseline (11.4K vs 50.8K/28.5K), comparisons are evaluation-count matched, and Table 1 gives "
                        "the ~10 MTok/iteration scale. Proposer tokens/dollars are absent ('a few hours'). Same "
                        "pattern scored 2 in r10a MemEvolve and r11b AutoHarness.",
                        ["son55:E005", "son55:E014", "son55:E020", "son55:E036", "sol:E17"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–E read. In scope (system_method): executable harness code "
                  "is edited from execution traces, retained, and evaluated on held-out test sets, OOD datasets and "
                  "unseen executors. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 1, 3, 4 and 7 are image-only; only values in the text and Tables 2–11 are used.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H12"], ["make_the_improver_editable", "H21"],
                 ["population_search_executable_fitness", "H14"]],
                "H12 kept (both). H21 (sol) kept: for classification and math the search target is the inner "
                "learning/retrieval mechanism, evaluated by how well the system learns (r10a MemEvolve convention, "
                "where H21 also displaced H17). H14 (son55) over H16 (sol): the frontier is reported, not "
                "load-bearing, and there is no frontier-off control; H14 names the executable-program search. H17 "
                "(son55) dropped: covered by H12/H21.", ["sol:E03", "son55:E007", "son55:E009"], NOSCORE),
            XC(p, "local:2603.28052-1", "son55", "partial",
               "Same question in both seats (budget-matched optimizer comparison). partial: search set only and "
               "evaluation-count, not token, matched.", ["son55:E014", "son55:E016", "sol:E05"]),
            XC(p, "local:2603.28052-2", "son55", "unmet",
               "A4 collision: sol's local-2 (holdout separation) and son55's local-2 (TB2 statistics/baseline gap) "
               "differ. Final local-2 = son55's question, unmet (verified: in-search Terminus-KIRA 64.4% vs "
               "leaderboard 74.7% unexplained; +1.7 points on 89 tasks, single run). sol's question merged into "
               "rsi:search_agent_architecture/S6.", ["son55:E032", "son55:E030"]),
            XC(p, "local:2603.28052-3", "revised",
               {"moved_to": "rsi:population_search_executable_fitness/H14.step5", "status": "unmet"},
               "sol's statistics question equals son55's H14.step5. Merged; unmet.", ["sol:E06", "opus:O02"]),
            XC(p, "local:2603.28052-4", "revised", {"moved_to": "rs:generative_process_redesign/RE-5", "status": "partial"},
               "sol's cost question equals son55's RE-5. Merged; partial.", ["sol:E05", "sol:E17"]),
            XC(p, "local:2603.28052-5", "sol", "partial",
               "Protocol reconstructibility (sol only). Verified: 250 vs 88 search-set count and the five-held-out "
               "wording are unresolved.", ["sol:E16", "opus:O01"]),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "met",
               "Verified: removing raw traces collapses search quality (Table 3).", ["son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "partial",
               "Verified: ACE/MCE on test; optimizers on search set only; TB2 vs leaderboard.", ["son55:E016", "son55:E030"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", "partial",
               "Verified: only the information interface is ablated.", ["son55:E018", "son55:E037"]),
            XC(p, "rs:generative_process_redesign/RE-5", "son55", "partial",
               "Verified; sol's local-4 merged here.", ["son55:E014", "son55:E006"]),
            XC(p, "rs:generative_process_redesign/RE-6", "son55", "met",
               "Verified: Pareto frontier (Table 9) and non-winning datasets/regressions reported.", ["son55:E041"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12.step4", "son55", "partial",
               "Verified: search/test split for classification and math; none for TB2.", ["son55:E013", "son55:E028"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "sol", "partial",
               "No gate or rollback (son55), but earlier wins are never overwritten: all candidates are archived and "
               "the frontier is kept. partial fits the card's 'protect earlier wins'.", ["sol:E04", "son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "met",
               "Verified: the same loop is applied in three domains.", ["son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/S1", "sol", "met",
               "Verified: proposer, skill and evaluator are fixed and evaluation runs outside the proposer.",
               ["sol:E02", "son55:E008"]),
            XC(p, "rsi:make_the_improver_editable/S6", "sol", "met",
               "Verified: the classification harness is one swappable executable unit, re-evaluated on new datasets.",
               ["sol:E03", "sol:E08"]),
            XC(p, "rsi:population_search_executable_fitness/H14.step5", "son55", "unmet",
               "Verified; sol's local-3 merged here.", ["son55:E018", "opus:O02"]),
            XC(p, "rsi:population_search_executable_fitness/S1", "son55", "met",
               "Verified: the contribution is the information granularity of search, compared head-to-head.",
               ["son55:E017"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial",
               "Verified: real dataset metrics; TB2 fitness = final test.", ["son55:E028"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "sol", "partial",
               "Verified: accuracy–context frontier named; no frontier-off control.", ["sol:E18"]),
            XC(p, "rsi:search_agent_architecture/H17.step4", "son55", "partial",
               "Kept as a check question (H17 not retained). Verified: deployed cost reported, proposer cost not.",
               ["son55:E006", "son55:E020"]),
            XC(p, "rsi:search_agent_architecture/S6", "son55", "partial",
               "Kept as a check question (H17 not retained); sol's local-2 merged here.", ["son55:E022", "sol:E09"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 3,
                "See ratings.M: only the raw-trace part of a three-part hypothesis is separated from its naive "
                "alternative.", ["son55:E018", "son55:E037"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 1,
                "See ratings.E.statistics: candidate distributions inside one search are not repeated runs "
                "(opus:O02); A2 level 1.", ["sol:E06", "opus:O02"], "−1.25 vs son55 (5×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 2,
                "See ratings.E.cost: deployed cost measured against all baselines plus evaluation matching; search "
                "cost absent (r10a/r11b convention).", ["son55:E020", "son55:E014"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text and Appendices A–E first. Initial view: "
                                                   "retained (classification test/OOD, math unseen problems and "
                                                   "models), not improver (proposer fixed); TB2 task-level. G 3, M 3, "
                                                   "X 3, Em 3, Ec 3, Eh 3, Es 1, E.cost 2.",
            "integrity_checks": "Both seats a1 on 2603.28052v1, material sha b8927d8a…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; both evidence_level retained.",
            "core_claim_check": "Strongest supported claim: one search's selected classification harness beats ACE/MCE "
                                "on test with less context and transfers to 9 OOD datasets; raw-trace access is the "
                                "load-bearing interface on the search set. Math gain over BM25 is ~1 point; TB2 is a "
                                "same-set discovery result.",
            "rating_agreement": "G, X, Em, Ec, Eh agree and were re-checked; M → son55, Es → sol, E.cost → son55. "
                                "Final 71.25.",
        },
    }

    # =========================================================== 2604.00830 Meta-TTL (Δ6.25)
    p = "2604.00830"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "This guidance becomes the actor’s entire system prompt for the next episode, so it is "
                              "the only information carried from one episode to the next.",
                    "Appendix B Setup",
                    "φ acts only through the post-episode rewrites; episode 1 runs the same initial actor prompt in "
                    "every arm. Differences between Naive and Meta-TTL sessions therefore come from the subsequent "
                    "changes the improver writes."),
            opus_ev(p, "O02", "The meta-prompt used for evaluation is independently meta-trained with this backbone.",
                    "Appendix D",
                    "A second, independent meta-training run (GLM-5.3-Flash meta-agent) reproduces the ordering "
                    "against Naive/AWM/EvoTest on Jericho and WebArena-Lite (Tables 7–8)."),
            opus_ev(p, "O03", "A visibly confirmed committed application change is normally durable.",
                    "Appendix A.2 (learned WebArena-Lite meta-prompt)",
                    "The learned prompt treats committed web-application state as persisting across episodes, while "
                    "§3.1 says the environment resets. If WebArena state persists, part of the cross-episode gain in "
                    "every arm comes from environment continuity. Unresolved; it affects all arms equally.",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Opus sides with sol. The paper liberates a conventionally fixed component, the hand-crafted "
                      "self-improvement policy, and makes it a learned artifact; the taxonomy note maps "
                      "make_the_improver_editable to generative_process_redesign. adapt_via_conditioning/C03 (both "
                      "seats) is supporting: meta-training over a task distribution with whole-domain holdout, acting "
                      "through conditioning text. son55's reframe_as_solvable_object (bi-level formulation) is a "
                      "framing, weak by son55's own note, and is not kept.",
            "matches": [smatch("sol", p, "generative_process_redesign"),
                        smatch("son55", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H19"),
                                       dmatch("sol", p, "attribute_and_patch_incumbent", "H10"),
                                       dmatch("son55", p, "evidence_gated_retention", "H31")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"][0]), "sol"),
            prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"][0]), "son55"),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.00830-1"): "local:2604.00830-4"},
            overrides={
                "local:2604.00830-4": renum("sol:local:2604.00830-1"),
                "local:2604.00830-3": {"status": "partial",
                                       "reason": "Opus (revised from unmet): Jericho tables average 5 runs and Fig. 3 "
                                                 "shows standard errors; the tables carry no intervals, the τ² repeat "
                                                 "count is unstated, and there is one meta-training run per benchmark."},
                "rsi:make_the_improver_editable/S1": {"status": "partial",
                                                      "reason": "Opus: the outer loop, BIS rule, validation tasks and "
                                                                "W-AUC are fixed in practice but not stated as the "
                                                                "anchor; the proposer prompts and φ0 are not given."},
                "rsi:make_the_improver_editable/S3": {"status": "met",
                                                      "reason": "Opus: Naive meta-agent (same architecture/models, "
                                                                "unoptimized φ) plus Reflexion/AWM/EvoTest with the same "
                                                                "GPT-5 adaptation LLM."},
                "rsi:make_the_improver_editable/F3": {"status": "partial",
                                                      "reason": "Opus: Jericho ID reuses the meta-training games, but "
                                                                "the improver claim rests on whole held-out games/"
                                                                "domains and held-out instances."},
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: WebArena application-state persistence across episodes vs §3.1 reset (opus:O03)."],
            evidence_level_note="improver, checked strictly against EVIDENCE.md: the edited object is the improver "
                                "(φ governs the post-episode rewrites, the only state carried between episodes; "
                                "opus:O01); the Naive meta-agent is the fixed improver at the same architecture, "
                                "models and episode protocol (son55:E012); the improved φ yields better subsequent "
                                "changes on whole held-out games/sites/domains and held-out instances (son55:E017, "
                                "son55:E020, son55:E022), replicated by an independent GLM meta-training (opus:O02). "
                                "Limits: one meta-training run per benchmark, OOD within each benchmark family, "
                                "Jericho ID = training games, φ0 undisclosed."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed object (hand-crafted self-improvement policy) "
                   "is named, neighbours are grouped, and Reflexion/Memory/TextGrad falling below Static on Jericho ID "
                   "supports the gap. No strong hand-written meta-prompt is compared.",
                   ["son55:E001", "son55:E012", "son55:E016", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. φ as the optimized improver with product-based fitness "
                   "(W-AUC), train/validation separation and BIS; Naive gives a separating prediction. BIS and two-"
                   "stage reflection are unjustified by evidence.", ["son55:E004", "son55:E005", "son55:E006", "sol:E003"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithms 1–2, BIS, freezing, iteration/session counts and "
                   "the final meta-prompts are given; retention is BIS>0 with the old φ⋆ as fallback. Proposer "
                   "prompts, φ0 and validation-set size are missing; δ is listed but unused (son55:E032).",
                   ["son55:E004", "son55:E006", "son55:E007", "sol:E004"], ["son55:E032"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Native rewards/checkers, W-AUC normalised to "
                               "max return plus Average Score, Static as trivial baseline. W-AUC is also the meta-"
                               "training objective; WebArena state persistence is unresolved (opus:O03).",
                               ["son55:E014", "son55:E016", "son55:E021", "sol:E006"], ["opus:O03"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. The Naive meta-agent differs from Meta-TTL only in "
                             "φ (same architecture, GPT-5 meta-agent, Gemini actor), which isolates the learned "
                             "improver; GEPA/GRPO outer loops with a shared meta-agent and a second backbone (opus:O02) "
                             "add alternatives. Not 4: BIS and two-stage reflection are not ablated and there is no "
                             "strong hand-written φ. sol's 2 asked for component ablations that test sub-mechanisms, "
                             "not the central claim.",
                             ["son55:E012", "son55:E015", "son55:E019", "son55:E024", "son55:E025", "opus:O02"],
                             ["son55:E028"]),
            "E.holdout": R("resolved", 3, "Opus sides with son55. φ is frozen and tested on whole held-out games, sites "
                           "and a held-out τ² domain, plus held-out instances in WebArena/τ². Jericho ID reuses training "
                           "games (labelled as such), OOD stays within each benchmark family, and public-benchmark "
                           "pretraining exposure is unaudited. sol's point about checker feedback at test time is the "
                           "TTL setting itself, applied to every arm, and limits scope rather than holdout.",
                           ["son55:E007", "son55:E008", "son55:E009", "son55:E017", "son55:E020", "sol:E005"],
                           ["son55:E007"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): 5/3 repeated runs and Fig. 3 standard errors; "
                              "no intervals in tables, τ² repeats unstated, no meta-training seed variance.",
                              ["son55:E014", "son55:E018", "sol:E008"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Meta-training $30–70, 12–15 iterations, 205–350 "
                        "sessions; test-time latency/calls/tokens vs all baselines (Table 6); 350 vs 1,920 rollouts vs "
                        "GRPO. Baseline tuning cost not counted.", ["son55:E026", "son55:E027", "sol:E010"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 text incl. Appendices A–E read. In scope (system_method): a non-weight "
                  "self-improvement policy (meta-prompt) is learned from execution feedback, frozen, and reused on "
                  "held-out tasks and domains. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "improver confirmed: edited object = improver (φ, opus:O01); comparable-budget fixed-improver "
                          "control = Naive meta-agent (son55:E012); better subsequent changes on whole held-out "
                          "games/domains and held-out instances, replicated by an independent GLM meta-training "
                          "(opus:O02). Scoped: single meta-training run per benchmark; within-family OOD.",
        "figure_dependence": "Figure 3 (per-episode curves with standard errors) is image-only; only its caption and "
                             "the tables are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "Liberating a fixed component (the improver) is the taxonomy's counterpart of make_the_improver_editable; "
                "see rs_pattern.reason.", ["sol:E001", "son55:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["generative_process_redesign", None], ["adapt_via_conditioning", "C03"]],
                "C03 is shared by both seats; reframe_as_solvable_object is a formulation, weak by son55's own fit.",
                ["sol:E001", "son55:E009"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["make_the_improver_editable", "H19"], ["attribute_and_patch_incumbent", "H10"],
                 ["evidence_gated_retention", "H31"]],
                "H19 shared. H10 (sol) names the outer move: one document (φ) rewritten from diagnosed adaptation "
                "failures. H31 (son55) names the commit rule: BIS on a validation set disjoint from the proposal task. "
                "Each names a distinct operation (r10b MemSkill convention).",
                ["son55:E005", "son55:E006", "sol:E003", "sol:E004"], NOSCORE),
            XC(p, "local:2604.00830-1", "son55", "unmet",
               "A4 collision: sol's local-1 (native-reward measurement, met) and son55's local-1 (no BIS/two-stage "
               "ablation) differ. Final local-1 = son55's question, unmet (verified). sol's question renumbered to "
               "local-4 (met).", ["son55:E006", "son55:E005"]),
            XC(p, "local:2604.00830-2", "son55", "partial",
               "Verified: the Jericho meta-prompt is full of text-adventure rules; no cross-family transfer test.",
               ["son55:E028"]),
            XC(p, "local:2604.00830-3", "revised", "partial",
               "son55 wrote unmet. Repeats (5/3) and Fig. 3 standard errors exist; tables lack intervals and τ² "
               "repeats are unstated. partial matches the agreed E.statistics=2.", ["son55:E014", "son55:E018", "sol:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "Verified: Naive vs Meta-TTL differ only in φ.", ["son55:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "partial",
               "Verified: whole-domain OOD, but no pretraining-overlap audit for public benchmarks.", ["son55:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: Static/Memory Agent/Reflexion exist; no equal-token raw-context or strong hand-written φ.",
               ["son55:E015", "son55:E033"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: backbone swaps reported; no training-task coverage study.", ["son55:E034", "son55:E023"]),
            XC(p, "rsi:evidence_gated_retention/H31.step3", "son55", "unmet",
               "Verified: acceptance is mean normalised difference > 0, with no paired test or margin (δ unused).",
               ["son55:E006", "son55:E032"]),
            XC(p, "rsi:make_the_improver_editable/F3", "sol", "partial",
               "Jericho ID = training games triggers F3, but the improver evidence is on held-out games/domains and "
               "instances; partial, not unmet.", ["son55:E007", "son55:E008", "son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/F6", "son55", "partial",
               "Verified: OOD only within each benchmark family; meta-prompt contains family-specific rules.",
               ["son55:E028", "son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/S1", "son55", "partial",
               "The fixed levels exist but are not named as the anchor; proposer prompts and φ0 missing.",
               ["son55:E005", "son55:E032"]),
            XC(p, "rsi:make_the_improver_editable/S3", "son55", "met",
               "S3 asks for a comparison against the fixed, hand-designed improver: Naive plus hand-designed TTL "
               "methods with the same adaptation LLM. sol's partial concerned BIS/two-stage ablations, which is "
               "local-1.", ["son55:E012", "son55:E015"]),
            XC(p, "rsi:make_the_improver_editable/S5", "son55", "unmet",
               "Verified: single incumbent, strict BIS>0, no archive.", ["son55:E006"]),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 3,
                "See ratings.E.causality: the Naive control isolates the learned φ; missing sub-mechanism ablations "
                "keep it below 4.", ["son55:E012", "son55:E025", "opus:O02"], "+3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 3,
                "See ratings.E.holdout: whole-domain and instance holdouts across three families; Jericho ID reuse "
                "is disclosed and not the basis of the improver claim.", ["son55:E009", "son55:E020", "son55:E022"],
                "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "3 (no reset note)",
             "son55_value": "3 (no reset note)", "final_value": 3,
             "reason": "Shared omission, no rating change. The learned WebArena meta-prompt treats committed "
                       "application state as durable across episodes, while §3.1 states that the environment resets "
                       "(opus:O03; sol listed it only under unresolved). If state persists, cross-episode gains include "
                       "environment continuity in every arm; the comparison between arms is unaffected.",
             "evidence_ids": ["opus:O03"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v4 text and Appendices A–E first. Initial view: "
                                                   "improver is defensible (Naive same-architecture control on OOD); "
                                                   "G 3, M 3, X 3, Em 3, Ec 3, Eh 3, Es 2, E.cost 3.",
            "integrity_checks": "Both seats a1 on 2604.00830v4, material sha 93c421cf…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; both evidence_level improver.",
            "core_claim_check": "Strongest supported claim: a meta-trained φ makes the same GPT-5 meta-agent improve a "
                                "frozen actor more across episodes than the unoptimized φ and hand-designed TTL methods, "
                                "on held-out games/sites/domains within each benchmark family (author_report).",
            "improver_check": "Strict EVIDENCE.md check passed; see assessment.evidence_level_note.",
            "rating_agreement": "G, M, X, Em, Es, E.cost agree and were re-checked; Ec and Eh → son55. Final 73.75.",
        },
    }

    # =========================================================== 2604.00901 HERA (Δ3.75)
    p = "2604.00901"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "trajectories are first ranked by downstream task performance",
                    "§3.1 Orchestrator",
                    "Every library update needs gold-answer F1 (Algorithm 2). With the library 'updated online' "
                    "(§3.2) and no freeze statement, whether updates also ran on evaluation queries is unknown.",
                    kind="our_inference"),
            opus_ev(p, "O02", "vs. CORAG), reflecting the transferability of the accumulated experience library and "
                              "evolving agent behaviors.",
                    "§5.1 (ii)",
                    "HoVer +64.95% is computed against CORAG (40.82); ExSearch (66.62) is 0.73 below HERA's 67.35 "
                    "(Table 1). The Bamboogle '−5.4%' vs ExSearch recomputes to −5.1% (60.53 vs 63.80).",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Opus sides with son55, following the r08b convention for frozen-model curated memory: "
                      "adapt_via_conditioning (sub null) with decompose_and_delegate (sub null) supporting, since the "
                      "orchestrator emits a typed JSON topology executed by role agents and a retriever. C03 is not "
                      "assigned (r04b: no canonical-schema training phase and no simpler-conditioning control). sol's "
                      "generative_process_redesign is not kept: the searchable orchestration is captured by the "
                      "domain cards.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"), smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "attribute_and_patch_incumbent", "H09")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.00901-1"): "local:2604.00901-4",
                    ("sol", "local:2604.00901-2"): "rs:decompose_and_delegate/RE-1",
                    ("sol", "local:2604.00901-3"): "local:2604.00901-3"},
            overrides={
                "local:2604.00901-4": renum("sol:local:2604.00901-1"),
                "rs:decompose_and_delegate/RE-1": {
                    "status": "partial",
                    "reason": "Opus: inference tokens are reported against selected baselines; learning-phase calls, "
                              "group rollouts, variant replays and library management are not.",
                    **moved("sol:local:2604.00901-2", "")},
                "local:2604.00901-3": {"status": "unmet",
                                       "reason": "Opus: same question in both seats; no seeds, repeats, variance or "
                                                 "intervals anywhere (sizes and negative cases exist, which is "
                                                 "E.statistics level 1, but this check asks for uncertainty)."},
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "unmet",
                    "reason": "Opus: no overlap or contamination analysis, and the test-time freeze is unstated "
                              "(opus:O01)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O02"]), "C2", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: whether library/prompt updates (which need gold F1) also ran on evaluation queries (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Fixed orchestration and static prompts are named and "
                   "neighbours listed, but training-free GRPO is distinguished in one sentence and static failure is "
                   "not measured under the same agents.", ["son55:E001", "son55:E003", "sol:E001", "sol:E019"]),
            "M": R("resolved", 2, "Opus sides with son55. The chain (group contrast → semantic advantage → library → "
                   "topology; failure replay → prompt variants → consolidation) is concrete, but the load-bearing "
                   "assumptions (LLM credit assignment, consolidation quality) are untested, the EM/KL account is "
                   "self-described as heuristic, and no prediction separates HERA from a fixed best topology or plain "
                   "reflective memory. The store is cast as a stand-in optimizer (F3).",
                   ["son55:E004", "son55:E009", "son55:E010", "son55:E013", "sol:E008"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Prompts and pseudocode are given; G, T, K, training size "
                   "and thresholds are missing, Algorithm 5's axes differ from the text, utility is a count in "
                   "Algorithm 3 but a success rate in §3.2, and writes have no gate or rollback.",
                   ["son55:E006", "son55:E011", "son55:E029", "sol:E013", "sol:E015"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Standard EM/F1/Acc, but 'Acc' is undefined, "
                               "baseline provenance is mixed, the 38.69% aggregate is unexplained, and the HoVer "
                               "'+64.95%' uses the weakest baseline while the Bamboogle gap is misstated (opus:O02). "
                               "Run text–number cap at 2.",
                               ["son55:E020", "son55:E021", "son55:E022", "sol:E017", "opus:O02"],
                               ["son55:E018", "son55:E019"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Library-off and prompt-evolution-off ablations "
                             "on two backbones (values partly figure-only); no all-static same-agent arm, no "
                             "simple-reflection or random-attribution control, heterogeneous quoted baselines.",
                             ["son55:E024", "son55:E025", "sol:E004"], ["son55:E023", "son55:E026"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. Standard train/test splits with a separately "
                           "curated training set and two whole OOD datasets. The test-time freeze is unstated while "
                           "updates need gold F1 (opus:O01), and there is no overlap audit; as in r11a ReCreate, an "
                           "unreported possible leak route on otherwise standard splits is 2, not 1.",
                           ["son55:E014", "son55:E016", "son55:E028", "sol:E012", "opus:O01"], ["sol:E003"]),
            "E.statistics": R("resolved", 1, "Opus sides with sol (A2 ladder tier 1): split sizes (Table 2, Bamboogle "
                              "125) and negative results (Bamboogle second, Llama ablation exceptions, failure cases "
                              "H.3–H.4) are reported; no main-result uncertainty. not_reported 0 is for a complete "
                              "absence of the relevant statistics, which is not the case here.",
                              ["sol:E012", "sol:E016", "son55:E026", "son55:E030"]),
            "E.cost": R("resolved", 1, "Both seats 1. Inference token use is measured against selected baselines (Llama "
                        "~4.7k–6.6k vs CORAG 20k+); learning-phase cost is absent and nothing is budget-matched.",
                        ["son55:E027", "sol:E006", "sol:E007"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–H read. In scope (system_method): an experience library "
                  "and role prompts are evolved from execution feedback without weight updates and reused on test and "
                  "OOD queries. All eight items resolved; the test-time freeze is recorded as unresolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 2–8 (ablations, token curves, topology metrics) are image-only; only values "
                             "stated in the text (e.g. Appendix F.2 Llama ablation numbers) are used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", None]],
                "r08b convention for frozen-model curated memory; C03 dropped per r04b; see rs_pattern.reason.",
                ["son55:E003", "son55:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"],
                 ["attribute_and_patch_incumbent", "H09"]],
                "H00 (son55) names the group-contrast reflection into lessons; H01 the ADD/MERGE/PRUNE/KEEP curator; "
                "H09 the orchestrator's credit to the responsible agent prompt. sol's search_agent_architecture with "
                "no sub is dropped: neither H17 (one offline design) nor H18 (test-time rewiring with a gate) fits, "
                "and per-query topology generation is the read path of H00.",
                ["son55:E004", "son55:E006", "son55:E010"], NOSCORE),
            XC(p, "local:2604.00901-2", "son55", "unmet",
               "A4 collision: sol's local-2 (cost) and son55's local-2 (measurement: heterogeneous baselines, 38.69% "
               "aggregate) differ. Final local-2 = son55's, unmet (verified, plus opus:O02). sol's cost question "
               "merged into rs:decompose_and_delegate/RE-1.", ["son55:E022", "opus:O02"]),
            XC(p, "local:2604.00901-3", "son55", "unmet",
               "Same question in both seats; the check asks for uncertainty, of which there is none.",
               ["son55:E016", "sol:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "RE-2 asks for an overlap/contamination analysis: none, and the freeze is unstated (opus:O01).",
               ["son55:E014", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no fixed-best-topology, raw-trajectory-context or plain reflective-memory arm.", ["son55:E024"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: only two modules ablated.", ["son55:E024", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "unmet",
               "Verified: no sensitivity to training size or library coverage.", ["son55:E014"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Verified; sol's local-2 merged here.", ["son55:E027"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "met",
               "Verified: Appendix B gives all prompts (hyperparameters missing, charged under X).", ["son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/F3", "son55", "unmet",
               "Verified: semantic advantages are presented as replacing numerical gradients and set head-to-head "
               "with RL-trained baselines of different capacity.", ["son55:E023"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step4", "son55", "unknown",
               "Verified: a split exists but whether the library is frozen at evaluation is not stated (opus:O01).",
               ["son55:E028", "opus:O01"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step5", "son55", "partial",
               "Verified: store-off exists; no budget match or variance.", ["son55:E024"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "Verified: specific fixed objects named, but 'no parameter updates' is contribution (i).", ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "met",
               "Verified: insights only from mixed success/failure groups.", ["son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: gold F1 and tokens rank trajectories during learning.", ["son55:E004", "opus:O01"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: admission is an LLM decision without a held-out test or rollback.", ["son55:E011"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H09", "sol", "partial",
               "Verified (sol only): variant replay gives component feedback; attribution accuracy and rollback are "
               "unchecked.", ["sol:E014", "son55:E010"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: only the agent judged primary contributor is edited; attribution accuracy is untested.",
               ["son55:E010"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "Verified: no regression check on earlier successes; variants are scored on the failures that "
               "triggered them.", ["son55:E009", "son55:E011"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: untested credit-assignment premises and no separating prediction against simple "
                "alternatives; the EM/KL account is heuristic by the authors' own statement.",
                ["son55:E010", "son55:E013"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 2,
                "See ratings.E.holdout: standard splits and two OOD datasets; the unstated freeze is an unreported "
                "possible leak route, which the run scores 2 (r11a ReCreate).", ["son55:E028", "opus:O01"],
                "+2.5 vs sol (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"),
                "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.statistics: sizes and negative results exist (A2 tier 1); not_reported is for a full "
                "absence.", ["sol:E012", "son55:E030"], "+1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text and Appendices A–H first. Initial view: in "
                                                   "scope; retained conditional on an unstated freeze. G 2, M 2, X 2, "
                                                   "Em 2 (aggregate/baseline problems), Ec 2, Eh 1–2, Es 1, E.cost 1.",
            "integrity_checks": "Both seats a1 on 2604.00901v2, material sha 12427e26…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; both evidence_level retained.",
            "core_claim_check": "Strongest supported claim: with frozen LLMs, HERA is best or near-best on several QA "
                                "datasets and removing the library or prompt evolution lowers test scores. The 38.69% "
                                "aggregate, the HoVer framing and 'robust OOD' are not supported as stated; 'retained' "
                                "holds only if the library was frozen at evaluation.",
            "rating_agreement": "G, X, Em, Ec, E.cost agree and were re-checked; M and Eh → son55, Es → sol. "
                                "Final 47.5.",
        },
    }

    # =========================================================== 2604.00931 PsychAgent (Δ11.25)
    p = "2604.00931"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "using LLMs-as-a-Judge", "§3.3 Reward Evaluation (followed by 'following (21)')",
                    "The RFT selection reward is a PsychEval-style LLM judge; §4.1 adopts the PsychEval evaluation "
                    "protocol for the reported metrics, so training selects on the evaluator family it is scored by."),
            opus_ev(p, "O02", "Training is conducted on two servers, each equipped with 8 NVIDIA H200 GPUs.",
                    "§4.1 Implementation Details",
                    "Hardware and settings only: no GPU-hours, rollout counts, judge calls, tokens or dollars anywhere."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering"],
            "outside_taxonomy": False,
            "reason": "Revised. The in-scope object is the skill tree read through <skill> tokens that SFT trains the "
                      "policy to use, which is the run convention for a skill library coupled with training "
                      "(adapt_via_conditioning/C03 primary, r12a/r12b; fit partial because weights also change). "
                      "son55's self_supervised_signal_engineering/C08 is kept as supporting: parallel rollouts → judge "
                      "filter → rejection fine-tuning is C08's generate–filter–retrain. sol's generative_process_redesign "
                      "primary is not kept: the evolving skill tree is a conditioning store, not a liberated generative "
                      "component.",
            "matches": [smatch("sol", p, "adapt_via_conditioning", role="primary"),
                        smatch("son55", p, "self_supervised_signal_engineering", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": seat("son55", p)["domain_pattern"]["unassigned"],
                           "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03", "domain_namespace": "rsi",
             "domain_main": "couple_context_and_weight_updates", "domain_sub": "H28",
             "operation_correspondence": "Skills retrieved into context are the conditioning input; SFT/RFT train the "
                                         "policy to read them (C03 step 3), and the same selected trajectory feeds "
                                         "both the skill tree and RFT (H28 S1).",
             "conditions_or_differences": "C03 expects category holdout; all five schools are seen in training.",
             "evidence_ids": ["son55:E015", "son55:E034", "sol:E005", "sol:E010"]},
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": "C08", "domain_namespace": "rsi",
             "domain_main": "couple_context_and_weight_updates", "domain_sub": "H28",
             "operation_correspondence": "N=8 session rollouts filtered by a judge reward and used for rejection "
                                         "fine-tuning: the weight lever of H28.",
             "conditions_or_differences": "The filter is the evaluator family itself (opus:O01), C08's step-3 "
                                          "failure shape.",
             "evidence_ids": ["son55:E012", "son55:E015", "opus:O01"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03", "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H02",
             "operation_correspondence": "Atomic skills mined from high-reward sessions, placed under meta-skills, "
                                         "appended or merged, and retrieved as conditioning.",
             "conditions_or_differences": "No admission test; not shown portable to other agents.",
             "evidence_ids": ["sol:E006", "sol:E007", "son55:E026"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.00931-1"): "rs:self_supervised_signal_engineering/RE-3",
                    ("sol", "local:2604.00931-2"): "local:2604.00931-4",
                    ("sol", "local:2604.00931-3"): "rs:self_supervised_signal_engineering/RE-5"},
            overrides={
                "rs:self_supervised_signal_engineering/RE-3": {
                    "status": "partial",
                    "reason": "Opus: PsychEval metrics plus a 522-dialogue, two-rater human study with QWK; clients are "
                              "simulated and no clinical outcome is measured.",
                    **moved("sol:local:2604.00931-1", "")},
                "local:2604.00931-4": {"status": "unmet",
                                       "reason": "Opus: same question in both seats; single runs, no seeds, intervals "
                                                 "or tests.",
                                       **moved("sol:local:2604.00931-2", "")},
                "rs:self_supervised_signal_engineering/RE-5": {
                    "status": "unmet",
                    "reason": "Opus: no rollout totals, GPU-hours, judge calls or dollars; settings only (opus:O02).",
                    **moved("sol:local:2604.00931-3", "")},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01"]), "C2", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: the seat working copy for sol was rewritten after conflicts.json; this record is bound to the "
            "conflicts-hashed version (see provenance.seat_input_pinning)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static post-SFT counselors and fixed skill libraries are "
                   "named; TheraMind already adapts across sessions and is separated in one sentence; 'static' is "
                   "not measured.", ["son55:E001", "son55:E005", "son55:E006", "sol:E024"]),
            "M": R("resolved", 2, "Opus sides with son55. The loop (shared selected trajectory → skill extraction and "
                   "RFT; skills read via <skill>) is concrete, but the selection reward is the evaluator family "
                   "(opus:O01), append/merge and extraction are themselves learned behaviours with no stated quality "
                   "criterion, and no prediction separates evolved skills from the initial library or RFT from plain "
                   "SFT.", ["son55:E009", "son55:E011", "son55:E012", "son55:E014", "opus:O01"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Engines, formulas, N=8 and training settings are given; "
                   "no skill admission gate or rollback, tree size/versioning, append/merge ratio, judge identity, "
                   "RFT iteration count or evaluation-time freeze.", ["son55:E007", "son55:E008", "son55:E014",
                                                                       "sol:E007"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. The reported PsychEval metrics come from the "
                               "same LLM-judge protocol that selects RFT trajectories (opus:O01), so the main metric is "
                               "one the system is optimized against, with simulated clients. The human study (522 "
                               "dialogues, QWK 0.675, ranking agreement) is a real independent anchor and keeps this "
                               "at 2, but it covers three systems, shows ceiling effects, and does not state rater "
                               "blinding.", ["son55:E012", "son55:E013", "son55:E029", "son55:E031", "sol:E014",
                                             "sol:E017", "opus:O01"], ["son55:E032"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. There is no same-backbone SFT-only arm and no "
                             "initial-vs-evolved skill tree arm; w/o SEE removes the whole engine. Ablation drops "
                             "(0.06–0.52) are far below the gaps to baselines (1.07–1.44), so most of the headline "
                             "advantage is unattributed (SFT on the benchmark's own corpus, reward = evaluator). "
                             "Table 4 swaps backbones. sol's 2 credited the ablation table as isolating components.",
                             ["son55:E022", "son55:E024", "son55:E028", "sol:E015", "sol:E022"], ["son55:E024"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. 120/20 profile split per school; SFT-corpus/"
                           "profile overlap and the evaluation-time freeze are unstated; all schools seen.",
                           ["son55:E016", "son55:E017", "sol:E011"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): evaluation and human-study sizes, QWK and "
                              "neutral memory results are reported; single runs with no intervals.",
                              ["son55:E016", "son55:E029", "son55:E031", "sol:E017"]),
            "E.cost": R("not_reported", 0, "Shared correction (both seats 1). Searched the full text and Appendices "
                        "A–C: there are no GPU-hours, rollout totals, judge-call counts, tokens, dollars or inference "
                        "cost comparisons. Hardware (16 H200), N=8, epochs and the 729-session internalization set are "
                        "settings, not cost evidence (r12a UI-Mem precedent).",
                        ["opus:O02", "son55:E018", "sol:E012"],
                        scope=["§4.1 Implementation Details, §4.2–4.5, Appendices A–C (human-evaluation protocol, "
                               "skill audits, Tables 5–9) searched by Opus for compute time, rollout counts, judge "
                               "calls, tokens, dollars and latency"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–C read. In scope under A3 bullet 2 (system_method): the "
                  "evaluated object includes a non-weight skill tree evolved from execution feedback and read at "
                  "inference, although SFT/RFT also update weights. Harness-level evidence is task (evolution not "
                  "isolated from the initial library or RFT). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (A3 bullet 2), confirmed: the w/o SEE ablation evaluates the retained non-weight skill engine; "
              "weight-side gains are not counted as harness evidence.",
        "figure_dependence": "Figures 2 (emotional trajectories) and 3 (per-metric radar) are image-only; only text "
                             "values are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "revised", "adapt_via_conditioning",
                "Skill library read by a trained policy: run convention (r12a/r12b). See rs_pattern.reason.",
                ["sol:E005", "son55:E034"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", "C03"], ["self_supervised_signal_engineering", "C08"]],
                "C03 from sol (policy trained to read the skill channel); C08 from son55 (RFT generate–filter–"
                "retrain). generative_process_redesign not kept.", ["sol:E005", "son55:E012", "son55:E015"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["couple_context_and_weight_updates", "H28"], ["abstract_experience_into_guidance", "H02"],
                 ["abstract_experience_into_guidance", "H01"]],
                "H28: one selected trajectory feeds both skill extraction and RFT, and the policy is trained to read "
                "skills (as UI-Mem r12a). H02: hierarchical skill entries with when_to_use/trigger fields, mined, "
                "deduplicated and merged. H01: the learned append/merge policy. The hash-bound sol record had H01 "
                "only (its later working-copy edit adds H28; see batch notes).",
                ["son55:E014", "son55:E034", "sol:E007", "son55:E026"], NOSCORE),
            XC(p, "local:2604.00931-1", "son55", "unmet",
               "A4 collision: sol's local-1 (clinical validity of measurement) and son55's local-1 (w/o SEE removes "
               "the whole engine) differ. Final local-1 = son55's, unmet (verified). sol's question merged into "
               "rs:self_supervised_signal_engineering/RE-3.", ["son55:E024", "son55:E027"]),
            XC(p, "local:2604.00931-2", "son55", "unmet",
               "A4 collision: sol's local-2 (statistics) and son55's local-2 (reward = evaluator family) differ. "
               "Final local-2 = son55's, unmet (opus:O01). sol's statistics question merged into local-4.",
               ["son55:E012", "son55:E013", "opus:O01"]),
            XC(p, "local:2604.00931-3", "son55", "unknown",
               "A4 collision: sol's local-3 (cost) and son55's local-3 (SFT-corpus overlap with evaluation profiles) "
               "differ. Final local-3 = son55's, unknown (not stated). sol's cost question merged into "
               "rs:self_supervised_signal_engineering/RE-5.", ["son55:E017"]),
            XC(p, "local:2604.00931-4", "son55", "unmet",
               "Verified; sol's local-2 merged here.", ["son55:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "Verified (sol only): engine-level ablations exist; no fixed-weight initial-vs-evolved tree arm.",
               ["sol:E015"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
               "sol only. The disjoint 120/20 profile split is a structural overlap control for rollouts and skills; "
               "the SFT corpus overlap is unaudited (son55 local-3). partial, as for the time split in 2603.26664.",
               ["sol:E011", "son55:E016", "son55:E017"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "partial",
               "Verified: two model sizes, one benchmark.", ["son55:E021"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "unmet",
               "Verified: no SFT-only or plain extra-fine-tuning baseline; ablation drops far below baseline gaps.",
               ["son55:E022", "son55:E024"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "partial",
               "Verified; sol's local-1 merged here.", ["son55:E029", "son55:E032"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "unmet",
               "Verified (opus:O02); sol's local-3 merged here.", ["son55:E018", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "sol", "partial",
               "Verified (sol only): the loop is generic; the goal-anchored meta-skill branch is the domain-specific "
               "element and is not isolated.", ["sol:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01", "sol", "partial",
               "Verified (sol only): append/merge exist; no delete, capacity or curator ablation.", ["sol:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/H02.step5", "son55", "unmet",
               "Verified: no evolved-vs-initial library comparison and no reuse in other agents.", ["son55:E026",
                                                                                                    "son55:E027"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "sol", "partial",
               "Verified (sol only): the grounding signal is the judge reward, partly anchored by the human study.",
               ["sol:E008", "sol:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Verified: append/merge against redundancy; no bound, forgetting or size report.", ["son55:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: only trajectory-level selection; no per-skill test or rollback.", ["son55:E014"]),
            XC(p, "rsi:couple_context_and_weight_updates/F4", "son55", "unmet",
               "Verified: consolidation is anchored in an LLM-judge reward, not a verifiable outcome (opus:O01).",
               ["son55:E012", "opus:O01"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "son55", "partial",
               "Verified: split declared; freeze and overlap unstated.", ["son55:E016", "son55:E017"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28.step4", "son55", "unmet",
               "Verified: reward from the evaluator family, no independent checker.", ["son55:E012", "son55:E013"]),
            XC(p, "rsi:couple_context_and_weight_updates/H28.step5", "son55", "unmet",
               "Verified: no context-only/weights-only/coupled comparison, no variance or matched budget.",
               ["son55:E024"]),
            XC(p, "rsi:couple_context_and_weight_updates/S1", "son55", "met",
               "Verified: the same S* feeds skill extraction and RFT.", ["son55:E014", "son55:E015"]),
            XC(p, "rsi:couple_context_and_weight_updates/S2", "son55", "partial",
               "Verified: typed split argued and each lever ablated, no three-way comparison.", ["son55:E024"]),
            XC(p, "rsi:couple_context_and_weight_updates/S3", "son55", "met",
               "Verified: 154,959 of 154,966 SFT counselor turns carry <skill> tags.", ["son55:E034"]),
            XC(p, "rsi:couple_context_and_weight_updates/S4", "son55", "unknown",
               "Verified: 'reduces reliance on retrieval' is claimed but context length is not measured.",
               ["son55:E015"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: reward = evaluator family and no separating prediction for evolution or "
                "internalization.", ["son55:E012", "opus:O01"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 2,
                "See ratings.E.measurement: the main metric is the training selector's family; the human study "
                "anchors it at 2 but not 3.", ["son55:E013", "son55:E031", "opus:O01"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality: no SFT-only or initial-library arm; ablation drops leave most of the gap "
                "unattributed.", ["son55:E022", "son55:E024"], "−3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.cost", "sol_value": {"status": "resolved", "rating": 1},
             "son55_value": {"status": "resolved", "rating": 1},
             "final_value": {"status": "not_reported", "rating": 0},
             "reason": "Both seats credited hardware, N=8, epochs and dataset size. These are settings: nothing lets "
                       "a reader compute compute time, judge calls, tokens or dollars, and no baseline is costed. Run "
                       "precedent r12a UI-Mem ('training settings are not costs') and r11b EvoSkill. Search scope "
                       "recorded in ratings.E.cost.",
             "evidence_ids": ["opus:O02", "son55:E018", "sol:E012"], "score_impact": "−1.25 vs both seats (5×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v3 text and Appendices A–C first. Initial view: in "
                                                   "scope (A3 bullet 2), evidence task. G 2, M 2, X 2, Em 2 (reward = "
                                                   "evaluator family; human study helps), Ec 1 (no SFT-only arm; "
                                                   "ablation drops ≪ baseline gaps), Eh 2, Es 1, E.cost 0 (settings "
                                                   "only).",
            "integrity_checks": "son55 a1 hash equals conflicts.json. sol a1: the working copy was rewritten at "
                                "20:30:57, after conflicts.json (20:23:41); the committed HEAD version matches the "
                                "conflicts hash and is the input used (read-only git show). Both on 2604.00931v3, "
                                "material sha a7b12f93…; both claim_type system_method; both evidence_level task.",
            "core_claim_check": "Strongest supported claim: the full SFT + memory + skill-tree + RFT system scores "
                                "above the listed general and counseling models on PsychEval (100 held-out profiles) "
                                "and in a three-system human study; removing any engine lowers scores slightly. The "
                                "contribution of skill evolution itself is not isolated, so harness-level evidence is "
                                "task.",
            "rating_agreement": "G, X, Eh, Es agree and were re-checked; E.cost shared correction 1 → 0; M, Em, Ec → "
                                "son55. Final 42.5.",
        },
    }
    return S
