"""Opus rulings for r17b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2604.26805 Bian Que (seat Δ5): final 45.0 (= son55). Only rating conflict M → son55 2: the failure-mode routing "
        "(retrieval gap → LoadDataSchema, reasoning flaw → Prompt, wrong content → knowledge pathway) is reconstructible, "
        "but the attribution step it depends on is stated, not specified (opus:O01), and the headline 'one signal, two "
        "co-evolving pathways' carries no distinguishing prediction (the authors defer it). RS → sol (adapt_via_conditioning "
        "+ generative_process_redesign; the Static arm tests the liberated mapping; the schema check verifies field "
        "returns, not diagnoses, so C25 is not kept). Domain H11 + H01 (both seats).",
        "2604.26969 AgenticRecTune (Δ5): final 40.0 (= son55). M → son55 2 (skill evolution reduces to appending domain "
        "knowledge, opus:O04; no argument against BO/bandit tuners). RS → sol (adapt_via_conditioning only; the A/B "
        "platform is an evaluator, not a sound solver, and son55 itself calls the split 'a role split of LLM prompts'). "
        "Domain → son55 H15 + H16 (distilled search memory + Pareto elites; H01 dropped). Table 2/3 full arms are the "
        "Table 1 launch rows (opus:O02, opus:O03); the §5.3 stage label contradicts the caption (opus:O01).",
        "2604.27221 Web2BigTable (Δ8.75): final 55.0, between the seats (53.75 / 62.5). G → son55 3; E.causality → sol 2 "
        "(clean store-off of the orchestrator skills, but no hand-written or non-feedback decomposition-skill arm and "
        "no budget-matched baseline; r11b EvoSkill / r15a CoEvoSkills convention); E.statistics → sol 1 (A2: Avg@4/Max@4 "
        "from one skill-learning run, r15a SkillX precedent). Shared correction E.holdout 2 → 1: the paper's own "
        "displayed learned skills carry test-task-specific content (AMD product lines and a cache/GPU spec worker for "
        "ws_en_091; an arXiv-date reconciliation rule for ws_zh_069), consistent with training queries being parameter "
        "perturbations of the test tasks, and contrary to the 'structural placeholders only' claim (opus:O01–O05). RS → "
        "son55 (decompose_and_delegate/C25 primary + adapt_via_conditioning). Domain → son55 H00 + H02 + H07.",
        "2604.27264 Self-Evolving Software Agents (Δ5): final 13.75 (= son55). Two-page extended abstract, no reported "
        "measurement; A1 applied by both seats (five E items not_reported) and kept. M → son55 1. claim_support → sol "
        "'unsupported' (r03b AgentRR / r11b AutoSkill precedent). evidence_level: son55 wrote 'none'; normalised to "
        "canonical null with evidence_level_note (recorded in shared_error_corrections as a normalisation, not a "
        "mechanical conflict because rv2 reads 'none' as null). Domain → sol H07 only (H06 needs self-proposed practice "
        "tasks and a curriculum; here operational goals are generated). RS outside_taxonomy (both).",
        "2604.27488 Skills-Coach (Δ5): final 33.75, below both seats (40.0 / 35.0) because each disputed item went to "
        "the lower seat on the text: G → son55 1; E.holdout → son55 1 (test tasks, rubric and retain-or-discard decision "
        "come from one pipeline and the reported set is the retention set; Table 2 lists no regression, opus:O03); "
        "E.cost → sol not_reported 0 (settings, not cost; r12a UI-Mem / r13b PsychAgent precedent). evidence_level → son55 "
        "task (selection set = reported set). RS → son55 self_supervised_signal_engineering (tasks, criteria and "
        "variant scores are manufactured by the pipeline). Domain → H11 + H13; H31 dropped (commit statistic unstated and "
        "applied on the reporting set). Shared omission recorded under E.measurement (no rating change): Table 2 "
        "per-task fractions (fifths, sevenths) do not fit the stated 4 + 4 test tasks, a 100% pass rate coexists with a "
        "57.1% advanced-task score under a 70% threshold, and Table 1's original average (0.378) does not match its "
        "subgroups (0.370).",
        "A4 hygiene: same-ID/different-question collisions were renumbered (26805 son55 local-1/2 → local-4/5; 26969 "
        "son55 local-2 → local-4; 27264 son55 local-1/2 swapped onto sol's numbering; 27488 son55 local-3 → local-4); "
        "same-question pairs were merged (27221 son55 local-2 → local-3). Step-suffixed IDs (H00-4, H11-2, H13-4, H15-5, "
        "H31-2, …) rewritten to the A4 grammar (H00.step4 …). Every move is recorded on the affected resolution or "
        "expectation note.",
        "Expectations from cards not retained as pattern matches (decompose_and_delegate in 26805/26969; "
        "abstract_experience_into_guidance in 26969; evidence_gated_retention in 27488) are kept as check questions with a "
        "note; they never score directly.",
        "Figure dependence: Bian Que Figure 4 (13-day on/off) is image-only; only the approximate values stated in the "
        "text are used. Skills-Coach Figures 1, 3, 4 and Web2BigTable Figures 1–6 are schematics or duplicate tabled "
        "values. No values were read from images.",
        "No material requests. Seats' wishes for neighbour originals (Memento-Skills, ACE, training-free GRPO, RCAgent) "
        "are non-blocking: no disputed rating depends on them.",
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

    def moved(old):
        return {"note": f"Merged here from {old} (A4: same question under a colliding or different ID)."}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def stepid(old):
        return {"note": f"Renamed from {old} to the A4 grammar (H##.stepN)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on *_pattern.matches)."}

    # =========================================================== 2604.26805 Bian Que (Δ5)
    p = "2604.26805"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "The same feedback signal is also analyzed to identify the root cause of any agent error "
                              "and routed to the corresponding Skill lifecycle operation",
                    "§2.4.2 Skill Pathway",
                    "The routing rule is stated, but the step it hinges on (who or what attributes one natural-language "
                    "correction to schema, prompt or knowledge content) is not specified."),
            opus_ev(p, "O02", "Overall 104 67 (65.3%) 75 (72.1%)", "Table 6 (Static ablation), overall row",
                    "Alert 26 + inspection 42 = 68, and 68/104 = 65.4%, whereas 67/104 = 64.4%: the overall count and "
                    "its percentage disagree (sol noted this). Minor, but it is the headline −13.5 pp ablation.",
                    kind="our_inference"),
            opus_ev(p, "O03", "Figure 4 : Day-level alert-analysis accuracy on production traffic.",
                    "§3.4, Figure 4 caption",
                    "The 13-day on/off result is image-only; only the approximate values stated in the text (~75–80% on "
                    "day 1, ~32% by day 13 without feedback, >80% with feedback) are used. No per-day n or interval."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["generative_process_redesign"], "outside_taxonomy": False,
            "reason": "Opus sides with sol. Primary adapt_via_conditioning (sub null; no category holdout or upstream "
                      "schema training, so C03 is not assigned): each event is solved by conditioning a frozen LLM on "
                      "Skill-selected data and distilled knowledge. Supporting generative_process_redesign (sub null): "
                      "the conventionally static event-to-(data, knowledge) configuration is turned into an LLM-generated, "
                      "feedback-edited artifact, and the Static arm is exactly that card's 'remove the redesign' test. "
                      "son55's decompose_and_delegate/C25 is not kept: the LoadDataSchema check only verifies that "
                      "sources return fields, so the artifact is not closed by a verifier of the diagnosis (C25 "
                      "tactical failure mode), and the agent×Skill matrix routes to the same LLM, not to a sound solver.",
            "matches": [smatch("sol", p, "adapt_via_conditioning"), smatch("sol", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.26805-1"): "local:2604.26805-4",
                    ("son55", "local:2604.26805-2"): "local:2604.26805-5"},
            overrides={
                "local:2604.26805-4": {"status": "unmet",
                                       "reason": "Opus (revised from unknown): the complete text was read; the recall of "
                                                 "alerts suppressed as non-actionable (missed incidents) is not reported "
                                                 "anywhere, so the expectation is unmet, not undetermined.",
                                       **renum("son55:local:2604.26805-1")},
                "local:2604.26805-5": renum("son55:local:2604.26805-2"),
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "partial",
                    "reason": "Opus sides with son55: daily dedup/prune and the short-/long-term split are named, but "
                              "the pruning rule, size bound and conflict resolution are not specified."},
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "unmet",
                    "reason": "Opus sides with son55: the validate-and-retry loop checks that the schema executes and "
                              "returns fields; no replay on earlier successes, improvement test or rollback protects "
                              "earlier wins."},
                "rs:decompose_and_delegate/RE-1": dropped_card("decompose_and_delegate"),
                "rs:decompose_and_delegate/RE-5": dropped_card("decompose_and_delegate"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O02"]), "C4", ["opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: how one natural-language correction is attributed to schema, prompt or knowledge content is "
            "unspecified (opus:O01).",
            "Opus: the 13-day on/off arms are figure-only with no per-day n (opus:O03)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The bottleneck (selecting event-specific data and knowledge "
                   "rather than reasoning; a drifting event-to-(data, knowledge) mapping) is concrete, and the frozen arm's "
                   "decay supports it. Not 3: no all-signals or static-context baseline tests the 'dilution' premise, and "
                   "RCAgent and self-evolving memory/skill agents are cited, not contrasted.",
                   ["son55:E002", "son55:E020", "sol:E003", "son55:E017"]),
            "M": R("resolved", 2, "Opus sides with son55. The Skill structure (LoadDataSchema + Prompt + Meta) and the "
                   "failure-mode routing are reconstructible, which is what sol's 3 credited. But the routing hinges on an "
                   "attribution step that is not specified (opus:O01), Skill matching is keyword-based, and the paper's own "
                   "distinguishing claim (one signal driving two co-evolving pathways beats separate pipelines) is argued "
                   "as convenience and left untested by the authors (son55:E007). Key assumptions remain weak: anchor 2.",
                   ["son55:E004", "son55:E005", "son55:E006", "opus:O01"], ["son55:E007"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Generation with execution validation (≤3 retries), NL "
                   "updates, short-term case memory and daily consolidation are described and read back on later events. "
                   "No regression check or rollback for Skill edits, no admission gate for knowledge entries, and the "
                   "Meta 'version' field has no stated semantics.",
                   ["son55:E003", "son55:E005", "son55:E006", "sol:E001", "sol:E002"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. SRE-annotated ground truth on 104 production "
                               "events and production KPIs are meaningful. Limits: pass@k counts an event as passed if any "
                               "of k Skill generations yields the ground-truth diagnosis (oracle selection); RCA accuracy is "
                               "'confirmed by practitioners' with no protocol or agreement; online KPIs are normalised "
                               "relatives; suppressed-alert recall is absent; Table 6's overall count disagrees with its "
                               "groups (opus:O02).",
                               ["son55:E010", "son55:E011", "sol:E006", "opus:O02"], ["son55:E021"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Static (hand-written fixed Skills) and NoKnow arms "
                             "on the same 104 events and a 13-day feedback on/off arm are relevant store-off style "
                             "contrasts for the retained Skills/knowledge. The headline online KPIs are pre/post with no "
                             "concurrent control and are attributed by the authors mainly to release interception and "
                             "inspection, the Static Skills' authorship and budget are unstated, the two pathways are not "
                             "separated, and no alternative context-assembly baseline exists.",
                             ["son55:E013", "son55:E014", "son55:E016", "sol:E008", "sol:E010"],
                             ["son55:E009", "son55:E007"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The 104-event set serves generation, retries, the "
                           "SRE corrections behind the 97.1%/99.0% figures, and the ablations; the knowledge-base state "
                           "during the offline runs is not described (only the Skill directory is reset). The 13-day "
                           "stream is a prospective quasi-holdout but figure-only (opus:O03).",
                           ["son55:E012", "son55:E015", "sol:E005", "sol:E007", "opus:O03"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder tier 1): denominators and residual failures are "
                              "given (104, 44/60, 36; six unresolved cases), with no intervals, seeds or run-to-run "
                              "variance, and the online arms have no uncertainty.",
                              ["son55:E010", "sol:E006", "sol:E007"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Serving footprint (Qwen3.5-35B-FP8 on one L20), "
                        "diagnosis latency (≤5 min in 95% of cases), retry caps and a backbone-size sweep are reported; "
                        "per-event tokens/calls, the cost of generation/update/consolidation loops and practitioner "
                        "correction effort are not, and no budget-matched baseline exists.",
                        ["son55:E019", "sol:E012", "sol:E001"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text read (body, 8 tables, appendices A–C). In scope (system_method): Skills "
                  "(LoadDataSchema + Prompt) and a distilled knowledge base are written from practitioner feedback, "
                  "persisted, and re-read on later events, with store-off style controls. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "not claimed; no evidence that the updating procedure itself improves.",
        "figure_dependence": "Figure 4 (13-day on/off) image-only; text values used only.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", None], ["generative_process_redesign", None]],
                "See rs_pattern.reason: the Static arm tests the liberated configuration (generative_process_redesign "
                "RE-1); the schema check verifies field returns, not diagnoses, so C25's verifier-closed artifact is "
                "absent.", ["sol:E010", "son55:E003", "son55:E022"], NOSCORE),
            XC(p, "local:2604.26805-1", "sol", "partial",
               "A4 collision: sol's local-1 asks about holdout (Skill reset only; corrections on the same cases), son55's "
               "local-1 about suppressed-alert recall. Final local-1 = sol's question, partial (verified: the Skill "
               "directory is reset, but the 99.0% includes SRE corrections on the failing test cases). son55's question "
               "moved to local-4 and revised unknown → unmet (the full text reports no recall).",
               ["sol:E005", "sol:E007", "son55:E021"]),
            XC(p, "local:2604.26805-3", "sol", "unmet",
               "Statistics question (sol only). Verified: counts and residual failures, no intervals or run variance.",
               ["sol:E006"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "Verified: Static and NoKnow toggle the Skill/knowledge channel on one benchmark; no matched alternative.",
               ["son55:E013", "son55:E014"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no all-signals, longer-context or nearest-neighbour baseline.", ["son55:E002"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: errors are attributed to missing knowledge for new services, with no sensitivity study.",
               ["son55:E018"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Kept as a check question (card not retained). Verified: no per-event tokens/calls or loop cost.",
               ["son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "unmet",
               "Kept as a check question. Verified: no single-agent/all-signals or RCAgent comparison.", ["son55:E020"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: routing per business-module is domain-specific, but the headline online gains are attributed "
               "to the paradigm (interception/inspection), not to the self-evolving store.", ["son55:E009"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
               "Verified: practitioner feedback grounds updates; knowledge extraction from un-fed-back cases is not "
               "grounded.", ["son55:E004", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Maintenance exists (daily dedup/prune, short/long-term split) but its rule and bound are unspecified; "
               "sol's 'met' credited the existence only.", ["son55:E005", "sol:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
               "Verified: Skills pass an execution check of data loading; knowledge entries have no admission gate.",
               ["son55:E003", "son55:E005"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "partial",
               "Verified: schema execution is the only automatic check; diagnostic correctness comes from practitioners.",
               ["son55:E003", "son55:E015"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: edits are routed to schema or prompt, but the attribution procedure is unspecified "
               "(opus:O01).", ["son55:E004", "opus:O01"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "S3 asks whether retention protects earlier wins. The retry loop gates executability, not improvement; "
               "there is no replay or rollback. sol's partial credited the executability check.",
               ["son55:E003", "sol:E001"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the routing logic is reconstructible but the attribution step is unspecified and the "
                "co-evolution premise carries no distinguishing prediction.",
                ["son55:E004", "son55:E007", "opus:O01"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first. Initial view: in scope; retained via "
                                                   "Static/NoKnow and the 13-day on/off arm. G 2, M 2–3, X 2, Em 2, Ec 2, "
                                                   "Eh 1–2 (corrections on test cases; pass@k oracle selection), Es 1, "
                                                   "E.cost 1.",
            "integrity_checks": "Both seats a1 on 2604.26805v2, material sha 9c1839a9…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: with practitioner feedback enabled, the authors' 13-day stream "
                                "kept accuracy above 80% versus decay to ~32% without it, and LLM-generated Skills beat "
                                "hand-written ones on 104 events (pass@5 94.2 vs 83.7). The online KPIs are pre/post. "
                                "'Retained' is the right label type; co-evolution is unmeasured. claim_support scoped.",
            "rating_agreement": "G, X and all five E items agree and were re-checked; M → son55. Final 45.0.",
        },
    }

    # =========================================================== 2604.26969 AgenticRecTune (Δ5)
    p = "2604.26969"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "We use the diversity task in the pre-ranking stage.", "§5.3 Model Ablation Study",
                    "Contradicts the Table 2 caption (re-ranking). The Gemini 3 Pro row equals the Table 1 re-ranking row "
                    "(opus:O02), so the caption is right and the text wrong."),
            opus_ev(p, "O02", "Gemini 3 Pro 0.21% 0.29% 3.43%", "Table 2, Gemini 3 Pro row",
                    "Identical to Table 1's Diversity/Re-Ranking launch row: the model ablation's best arm is the launched "
                    "(selected) result, while the other arms' selection histories are not given.", kind="our_inference"),
            opus_ev(p, "O03", "Actor-Critic Strategy 0.75% 0.90% 0.48%", "Table 3, Actor-Critic row",
                    "Identical to Table 1's Value-Based Retrieval launch row: the strategy ablation compares a launched "
                    "winner against a single-agent run of unstated rounds and traffic.", kind="our_inference"),
            opus_ev(p, "O04", "It mainly update the domain knowledge section.", "§4.4.2 Novel Skill Generation",
                    "'Novel skill generation' reduces to appending domain-knowledge text; the update logic of the "
                    "self-evolving Skillhub is not otherwise specified."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus sides with sol. adapt_via_conditioning (sub null; no C03 schema training or category "
                      "holdout): the frozen Gemini Actor is conditioned on per-task skills, distilled rules and Pareto "
                      "elites to propose configurations, with no parameter updates. son55's decompose_and_delegate/C25 "
                      "primary is not kept: the production A/B platform is an evaluator of proposals, not a sound solver "
                      "of a delegated sub-problem, and son55's own match reason calls the split 'a role split of LLM "
                      "prompts rather than a solver seam' (C25 tactical failure mode).",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H15"),
                                       dmatch("sol", p, "population_search_executable_fitness", "H16")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 1), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.26969-2"): "local:2604.26969-4",
                    ("son55", "rsi:population_search_executable_fitness/H15-5"):
                        "rsi:population_search_executable_fitness/H15.step5"},
            overrides={
                "local:2604.26969-1": {"status": "unmet",
                                       "reason": "Opus (revised; sol partial, son55 unknown — same question): the "
                                                 "reported lifts come from candidates chosen over 'rounds of small "
                                                 "traffic', and no confirmation on fresh traffic is reported. With the "
                                                 "full text read, the absence is a fact, not an unknown; the randomized "
                                                 "buckets are real traffic but selection and reporting are not "
                                                 "separated.",
                                       **moved("son55:local:2604.26969-1")},
                "local:2604.26969-4": renum("son55:local:2604.26969-2"),
                "rsi:population_search_executable_fitness/H15.step5": stepid(
                    "rsi:population_search_executable_fitness/H15-5"),
                "rsi:population_search_executable_fitness/S5": {
                    "status": "partial",
                    "reason": "Opus sides with sol: the elite archive keeps configurations by measured online outcomes "
                              "and names its axis of complementarity (non-dominated over several metrics), but the "
                              "distilled rules carry no credit and no archive/memory ablation exists."},
                "rsi:abstract_experience_into_guidance/S5": dropped_card("abstract_experience_into_guidance"),
                "rs:decompose_and_delegate/RE-1": dropped_card("decompose_and_delegate"),
                "rs:decompose_and_delegate/RE-2": dropped_card("decompose_and_delegate"),
                "rs:decompose_and_delegate/RE-4": dropped_card("decompose_and_delegate"),
                "rs:decompose_and_delegate/RE-5": dropped_card("decompose_and_delegate"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O03"]), "C4", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: the full arms of Tables 2 and 3 are the Table 1 launch rows (opus:O02, opus:O03); §5.3 mislabels the "
            "stage (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. System-level configuration retuning after model changes is "
                   "a real, specific non-weight object. Classical online tuners (BO/bandits) are not treated as "
                   "neighbours, ACE gets one sentence, and the residual against recsys agents is stated, not shown.",
                   ["son55:E002", "son55:E003", "son55:E021", "sol:E010"]),
            "M": R("resolved", 2, "Opus sides with son55. The propose → critique → live A/B → memory → insight → skill "
                   "chain is reconstructible and the A/B oracle fits the problem (sol's ground for 3). But the "
                   "self-evolution step reduces to appending domain-knowledge text and tightening bounds (opus:O04, "
                   "son55:E004), there is no argument why LLM proposals plus appended rules should beat BO/bandit tuners, "
                   "and how appended rules generalise is not stated. Anchor 2.",
                   ["son55:E007", "son55:E009", "son55:E017", "son55:E004", "opus:O04"], ["son55:E018"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Memory schema, Pareto pruning, greedy diversity selection and "
                   "next-prompt reading are described. Skill updates have no admission gate, versioning, rollback or "
                   "conflict handling, no learned rule is shown, and a human review step precedes every A/B test.",
                   ["son55:E004", "son55:E005", "son55:E008", "son55:E006"], ["son55:E023"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Randomized production A/B is a credible channel, "
                               "but the metrics are anonymised relative lifts with no definitions, absolute values or "
                               "per-row tests, and the ablation stage is mislabelled in the text (opus:O01).",
                               ["son55:E010", "son55:E011", "son55:E012", "opus:O01"], ["son55:E015"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only Actor-Critic vs Actor-only and an LLM sweep "
                             "exist, and their full arms are the launched winners (opus:O02, opus:O03). The central "
                             "Skillhub/memory/Insight claim has no on/off arm and no tuner baseline supports the "
                             "efficiency claim.",
                             ["son55:E014", "son55:E016", "sol:E009", "opus:O03"], ["son55:E018"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Live traffic is a real outcome channel, but the "
                           "reported lifts come from candidates selected over prior small-traffic rounds with no fresh "
                           "confirmation, the ablations reuse launch rows, and nothing transfers beyond Discover.",
                           ["son55:E010", "son55:E022", "sol:E006", "opus:O02"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 tier 1): a blanket p<0.05 statement; no sample sizes, "
                              "intervals, per-row tests, run variance or multiple-comparison control across arms.",
                              ["son55:E011", "sol:E007"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported. Efficiency and scalability are claimed, but no LLM "
                        "calls, A/B rounds, traffic share, wall-clock or review time is reported.",
                        [], ["son55:E018", "son55:E006"],
                        ["Full text §§1–6, both prompts, Tables 1–3; no appendix exists in the pinned source"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text read (no appendix exists). In scope (system_method): non-weight system "
                  "configurations and a Skillhub are updated from live A/B feedback and re-read in later rounds. All "
                  "eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; configurations and Skillhub are non-weight harness components; both seats agree)",
        "improver_check": "not claimed beyond narrative; no improver evidence.",
        "figure_dependence": "Figure 1 is a schematic; all results are in Tables 1–3.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "See rs_pattern.reason: the A/B platform evaluates proposals; it does not solve a delegated sub-problem.",
                ["son55:E007", "sol:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "decompose_and_delegate/C25 dropped (role split of LLM prompts, no solver seam).",
                ["son55:E007", "sol:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["population_search_executable_fitness", "H15"], ["population_search_executable_fitness", "H16"]],
                "H15 (search history distilled into rules that condition later proposals) is the exact shape of the "
                "Insight → Skill path; H16 (Pareto elites) agreed by both. sol's H01 (curated living memory with edit "
                "operations) is not kept: rules are appended, with no edit vocabulary or consolidation.",
                ["son55:E004", "son55:E017", "son55:E008"], NOSCORE),
            XC(p, "local:2604.26969-1", "revised", "unmet",
               "Same question in both seats (selection rounds vs reported lift). Revised to unmet: no fresh-traffic "
               "confirmation is reported; 'unknown' is not apt once the full text is read, and 'partial' credited the "
               "randomized buckets, which are charged in E.holdout.", ["son55:E022", "sol:E006"]),
            XC(p, "local:2604.26969-2", "sol", "partial",
               "A4 collision: sol's local-2 asks for a Skillhub/static or budget-matched control (partial: only "
               "Actor-only exists); son55's local-2 asks for examples of learned rules (unmet) and moves to local-4.",
               ["sol:E009", "son55:E019"]),
            XC(p, "local:2604.26969-3", "sol", "unmet",
               "Verified: 'no longer requires human effort' vs 'the users' review is required' before every A/B test.",
               ["sol:E001", "son55:E023"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: no no-memory or no-domain-knowledge prompt baseline.", ["son55:E004"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Kept as a check question (card not retained). Verified: no calls, rounds, traffic or latency.",
               ["son55:E018"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Kept as a check question. Verified: Actor-Critic and LLM ablations only.", ["son55:E014", "son55:E016"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Kept as a check question. Verified: three tasks in one product.", ["son55:E012", "son55:E013"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "unmet",
               "Kept as a check question. Verified: no human, grid, BO or bandit baseline.", ["son55:E018"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "unmet",
               "Kept as a check question (H01 not retained). Verified: rules are appended and bounds tightened with no "
               "utility gate.", ["sol:E005"]),
            XC(p, "rsi:population_search_executable_fitness/F1", "son55", "partial",
               "Verified: Pareto elites, diversity selection and rule distillation are standard; the recsys "
               "configuration domain carries most of the novelty.", ["son55:E003", "son55:E008"]),
            XC(p, "rsi:population_search_executable_fitness/F3", "son55", "partial",
               "Verified: the Skillhub's contribution cannot be separated from plain LLM-driven search.",
               ["son55:E016"]),
            XC(p, "rsi:population_search_executable_fitness/H15-5", "son55", "unmet",
               "Renamed rsi:population_search_executable_fitness/H15.step5 (A4). Verified: no matched-budget "
               "memory-off arm.", ["son55:E016"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "met",
               "Verified: randomized live A/B on production metrics is hard to game; caveats charged in E items.",
               ["son55:E010", "son55:E011"]),
            XC(p, "rsi:population_search_executable_fitness/S4", "son55", "met",
               "Verified: A/B results are written back and elites/insights enter the next prompt.",
               ["son55:E009", "son55:E017"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "sol", "partial",
               "The archive retains configurations by measured outcomes and names its complementarity axis (half of "
               "S5); the distilled rules carry no credit and no archive ablation exists. son55's unmet ignored the "
               "frontier half.", ["sol:E004", "son55:E008", "son55:E004"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the improver step is appending text (opus:O04) with no argument against classical "
                "tuners.", ["son55:E004", "son55:E017", "opus:O04"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first. Initial view: in scope; task level "
                                                   "(no Skillhub-off arm). G 2, M 2, X 1–2, Em 2, Ec 1, Eh 1 (winner's "
                                                   "curse), Es 1, E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.26969v2, material sha 1daddb37…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: author-reported, at least one agent-proposed configuration per "
                                "task beat the production control in live A/B at p<0.05. Nothing isolates the persisted "
                                "Skillhub or memory; evidence_level task, claim_support scoped.",
            "rating_agreement": "G, X and all five E items agree and were re-checked; M → son55. Final 40.0.",
        },
    }

    # =========================================================== 2604.27221 Web2BigTable (Δ8.75)
    p = "2604.27221"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Assign one worker per major product line (Desktop, Server, Mobile, Workstation, "
                              "Embedded, PRO).",
                    "Appendix C, Case B, learned skill decompose-split-by-category ('auto-generated in Phase 1')",
                    "The 'learned' skill names AMD's product lines, the entities of test task ws_en_091."),
            opus_ev(p, "O02", "Always assign a dedicated worker for cache/GPU spec lookup.",
                    "Appendix C, Case B, learned skill",
                    "cache and graphics fields are columns of test task ws_en_091: column-specific content in a "
                    "training-time skill."),
            opus_ev(p, "O03", "List all AMD processors with Zen architecture released from Lisa Su becoming CEO (2014) "
                              "to 2024 inclusive.",
                    "Appendix C, Case B, user query ws_en_091 (test task)",
                    "The test query whose entities and columns the learned skill already encodes."),
            opus_ev(p, "O04", "assign a dedicated verification worker that cross-references the field across sources.",
                    "Appendix C, Case C, learned skill split-by-source (rule keyed on the example 'arXiv date takes "
                    "precedence')",
                    "The learned rule mirrors test task ws_zh_069's instruction 'If two records refer to the same "
                    "paper, the canonical date is the arXiv first-submit timestamp.'"),
            opus_ev(p, "O05", "we generate 20 modified queries for strategy learning.",
                    "§3.1 XBench-DeepSearch (WideSearch: 'perturbing task parameters (e.g., entity counts or time "
                    "ranges)')",
                    "Training queries are modifications of benchmark tasks on both benchmarks. Perturbing counts or time "
                    "ranges keeps the entities, which explains O01–O04 and contradicts 'constrained to use only "
                    "structural placeholders'.", kind="our_inference"),
            opus_ev(p, "O06", "the architecture dynamically discovers, synthesizes, and refines executable search "
                              "skills at inference time.",
                    "§4 Related Work, Autonomous Web Search",
                    "Contradicts §2.4 ('frozen read-only inputs'; 'no ... memory update is performed'): the test-time "
                    "system can still create and repair worker skills."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Opus sides with son55. Decomposition is the paper's central object: the orchestrator partitions a "
                      "wide query into entity/source/category subtasks with a typed result schema and tag-partitioned "
                      "slots (C25 lists a 'typed inter-agent deliverable'), the loop is closed at training by gold-table "
                      "Item-F1, and the store-off ablation collapses the system toward the generic-decomposition "
                      "baseline (C25 step 4). The delegated solver is a worker-agent pool, not a symbolic solver, so fit "
                      "is partial on step 1. adapt_via_conditioning (sub null) supports: the learned SKILL.md banks are "
                      "read as in-context conditioning of frozen LLMs. sol's adapt_via_conditioning-only reading misses "
                      "the decomposition that the method learns.",
            "matches": [smatch("son55", p, "decompose_and_delegate"), smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "crystallize_executable_capability", "H07")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0), pmap("son55", p, 1), pmap("sol", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.27221-2"): "local:2604.27221-3",
                    ("son55", "rsi:abstract_experience_into_guidance/H00-4"):
                        "rsi:abstract_experience_into_guidance/H00.step4",
                    ("son55", "rsi:abstract_experience_into_guidance/H00-5"):
                        "rsi:abstract_experience_into_guidance/H00.step5"},
            overrides={
                "local:2604.27221-1": {"status": "unmet",
                                       "reason": "Opus (revised; sol partial, son55 unknown — same question): no overlap "
                                                 "audit is reported, and the paper's own learned skills carry test-task "
                                                 "entities and columns (opus:O01–O04), consistent with training queries "
                                                 "being parameter perturbations of test tasks (opus:O05).",
                                       **moved("son55:local:2604.27221-1")},
                "local:2604.27221-3": {"status": "partial",
                                       "reason": "Opus sides with sol: four inference runs with Avg@4/Max@4 exist; no "
                                                 "interval and a single skill-learning run (son55's local-2, the same "
                                                 "question, merged here).",
                                       **moved("son55:local:2604.27221-2")},
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "unmet",
                    "reason": "Opus sides with son55: skills are appended monotonically with no test before keeping; "
                              "worker skills are gated only by AST validity. A store-off ablation is not a gate."},
                "rsi:abstract_experience_into_guidance/H00.step4": {
                    **stepid("rsi:abstract_experience_into_guidance/H00-4"),
                    "reason": "Skills are frozen before testing on the unmodified benchmark, but training queries are "
                              "perturbations of benchmark tasks and the displayed skills carry test-task content "
                              "(opus:O01–O05)."},
                "rsi:abstract_experience_into_guidance/H00.step5": stepid(
                    "rsi:abstract_experience_into_guidance/H00-5"),
                "rs:adapt_via_conditioning/RE-2": {
                    "reason": "No overlap/contamination analysis between the perturbed training queries and the test "
                              "tasks; the displayed learned skills show the overlap (opus:O01–O05)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O04", "opus:O05"]),
                                        "C4", ["opus:O06"]),
        "assessment": assess("son55", p, [
            "Opus: displayed learned skills encode test-task entities/columns (opus:O01–O05); held-out status of the "
            "gain is weaker than 'unmodified test set' suggests.",
            "Opus: test-time skill creation/repair contradicts the frozen-inference description (opus:O06)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus sides with son55. The bottleneck (a fixed decomposition axis leaves coverage "
                   "gaps in wide search; context saturation of monolithic agents) is concrete and directly exhibited by "
                   "the generic-decomposition arm and case studies. The lineage is explicit: workers are Memento-Skills "
                   "agents, and the delta is the orchestrator-level skill learning plus the workboard; single-level "
                   "self-evolving skill agents are named with the difference stated. Not 4: the residual against "
                   "automatically searched workflows, which also learn decomposition from execution, is asserted "
                   "('fixed or weakly adaptive') rather than contrasted.",
                   ["son55:E002", "son55:E003", "son55:E024", "son55:E016", "sol:E015"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Gold-verified error reports, clustering by structural "
                   "decomposition pattern, per-cluster skill synthesis and a router skill form a reconstructible "
                   "response to the coverage gap. Not 4: no argument why learned skills should beat a hand-written "
                   "decomposition prompt, and the worker-level rationale is thin.",
                   ["son55:E007", "son55:E008", "son55:E024", "sol:E003"], ["son55:E014"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Training/inference split, router and workboard locking are "
                   "clear. Retention is append-only with no gate, conflict handling or forgetting; bank size is "
                   "unreported; and the description contradicts itself (read-only inference vs runtime skill creation, "
                   "opus:O06; 'no deduplication' vs deduplicated case studies; single pass vs Round 2).",
                   ["son55:E006", "son55:E013", "son55:E014", "son55:E015", "son55:E016", "opus:O06"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Established benchmarks with strict SR plus "
                               "row/item F1 against gold tables. Concerns: LLM judgement for free-text cells and XBench, "
                               "and baselines taken from published reports (comparability is charged in E.causality).",
                               ["son55:E017", "son55:E019", "son55:E021", "sol:E008"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. The store-off ablation of the retained orchestrator "
                             "skills (same system, both benchmarks) and same-backbone single agents are the key controls, "
                             "and they are large. But the strongest alternative for the RSI claim — decomposition skills "
                             "written without feedback (hand-written, or one LLM pass) — is untested, the 'generic' "
                             "decomposition arm is a weak default, baselines are not budget- or backbone-matched (10 "
                             "workers, 8,000 cloud skills), and the worker-evolution arm also removes catalogue "
                             "discovery. Run convention: store-off without an alternative-optimizer or budget-matched "
                             "arm = 2 (r11b EvoSkill, r15a CoEvoSkills); MineEvolve's 3 had matched alternative stores.",
                             ["son55:E009", "son55:E011", "son55:E012", "son55:E019", "sol:E010", "sol:E011"],
                             ["son55:E029", "son55:E014"]),
            "E.holdout": R("resolved", 1, "Shared correction 2 → 1. Frozen skills evaluated on the unmodified benchmark "
                           "is the right design, but training queries are parameter perturbations of benchmark tasks "
                           "(opus:O05), and the paper's own displayed learned skills encode specific test tasks: AMD "
                           "product lines and a cache/GPU worker for ws_en_091 (opus:O01–O03), an arXiv-date rule for "
                           "ws_zh_069 (opus:O04). The 'structural placeholders only' safeguard is contradicted, no "
                           "overlap audit exists, skills are learned per benchmark, and test-time skill creation persists "
                           "(opus:O06).",
                           ["son55:E004", "son55:E005", "son55:E008", "sol:E006", "opus:O01", "opus:O02", "opus:O03",
                            "opus:O04", "opus:O05"], ["son55:E027"]),
            "E.statistics": R("resolved", 1, "Opus sides with sol (A2 ladder; r15a SkillX precedent). Avg@4 and Max@4 "
                              "average four inference runs into point estimates with no dispersion, interval or test, "
                              "from a single skill-learning run; XBench is a single run with 1-point margins.",
                              ["son55:E018", "son55:E022", "sol:E009"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported. 'Cost-efficient' models are asserted, but no "
                        "tokens, calls, wall-clock, dollars or training-phase cost are reported for 10 parallel workers, "
                        "reflection LLMs and skill retrieval.",
                        [], ["son55:E020", "son55:E028"],
                        ["§§2.3–2.4, §§3.1–3.5, Tables 1–5, Appendices A–C of the pinned v1 text"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (method, algorithms, Tables 1–5, Appendices A–C). In scope "
                  "(system_method): orchestrator and worker SKILL.md banks are written from gold-referenced feedback, "
                  "frozen, and read on later test tasks, with a store-off control. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "not claimed; the reflect pipeline is fixed.",
        "figure_dependence": "Figures 1–6 are schematics or plot tabled values; case-study content is in text.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "See rs_pattern.reason: the learned object is the decomposition itself, with a typed deliverable and a "
                "store-off collapse.", ["son55:E009", "son55:E007"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["decompose_and_delegate", "C25"], ["adapt_via_conditioning", None]],
                "C25 kept at partial fit (worker pool, not a symbolic solver); adapt_via_conditioning supporting.",
                ["son55:E009", "son55:E026"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H02"],
                 ["crystallize_executable_capability", "H07"]],
                "H00 added: the orchestrator path reflects on gold-graded outcomes into transferable decomposition "
                "lessons with trigger conditions (router). H02 (SKILL.md packages) and H07 (worker forge-on-gap) agreed "
                "by both.", ["son55:E006", "son55:E007"], NOSCORE),
            XC(p, "local:2604.27221-1", "revised", "unmet",
               "Same question in both seats (training-test independence). Revised to unmet on Opus evidence: the "
               "learned skills encode test-task specifics (opus:O01–O05).",
               ["sol:E006", "son55:E004", "opus:O01", "opus:O04", "opus:O05"]),
            XC(p, "local:2604.27221-3", "sol", "partial",
               "Statistics question; son55's local-2 (same question, unmet) merged here. Partial: repeated inference "
               "runs exist, skill-learning variance does not.", ["sol:E009", "son55:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified and strengthened by opus:O01–O05: no contamination analysis, and overlap is visible.",
               ["son55:E004", "opus:O05"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Verified: no token, call, latency or dollar cost.", ["son55:E020", "son55:E028"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: three component ablations; worker arm confounded with catalogue use; no matched compute.",
               ["son55:E009", "son55:E011", "son55:E012"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: two benchmarks, skills learned per benchmark.", ["son55:E027", "son55:E023"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "Verified: same-backbone single agents included; multi-agent baselines are published numbers with other "
               "backbones.", ["son55:E019", "son55:E017", "son55:E029"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "met",
               "Verified: case studies tie the decomposition axis to retrieved-row coverage.",
               ["son55:E024", "son55:E016"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "met",
               "Verified: the decomposition-axis mechanism is specific to why wide search is hard.",
               ["son55:E024", "son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-4", "son55", "partial",
               "Renamed H00.step4 (A4). Partial kept: frozen before testing, but test-task content leaks into skills "
               "(opus:O01–O05).", ["son55:E004", "son55:E005", "opus:O05"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-5", "son55", "partial",
               "Renamed H00.step5 (A4). Verified: store-off present; no budget match or training-run variance.",
               ["son55:E009", "son55:E018"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "met",
               "Verified: the fixed object (how a wide query is decomposed) is made learnable.",
               ["son55:E002", "son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: errors and successful trajectories are reflected per cluster; explicit contrast is not "
               "described.", ["son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: gold-referenced Item-F1 grounds the lessons (privileged, training only).", ["son55:E026"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Verified: append-only; no merge, forgetting or conflict handling.", ["son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "S5 asks for a gate before an entry is kept; none exists. sol's partial credited the store-off "
               "ablation, which tests the bank, not admission.", ["son55:E006", "son55:E025", "sol:E002"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "sol", "partial",
               "Verified: AST parsing is not execution; error-trace repair uses execution failures.",
               ["sol:E004", "sol:E005"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 3,
                "See ratings.G: the bottleneck is exhibited, the Memento-Skills lineage and delta are explicit; not 4 "
                "because the workflow-search residual is asserted. sol's 2 charged an unverified ancestor residual "
                "that the paper does state.", ["son55:E002", "son55:E024", "sol:E015"], "+3.75 vs sol (15×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", 2,
                "See ratings.E.causality: clean store-off but no feedback-free skill arm or budget-matched baseline; "
                "run convention for store-off-only evidence is 2.",
                ["son55:E009", "son55:E029", "sol:E011"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 1,
                "A2 ladder: averaged repeat runs without dispersion from one skill-learning run = 1 (r15a SkillX).",
                ["son55:E018", "sol:E009"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout", "sol_value": 2, "son55_value": 2, "final_value": 1,
             "reason": "Both seats saw the perturbation risk but did not check the paper's own displayed skills. Those "
                       "skills encode specific test tasks (AMD product lines and a cache/GPU worker for ws_en_091; an "
                       "arXiv-date reconciliation rule for ws_zh_069), contradicting the 'structural placeholders' "
                       "safeguard and showing that test-task content reached the frozen banks via perturbed training "
                       "queries. Under A2 contamination is an E.holdout defect.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05", "son55:E008"],
             "score_impact": "−2.5 (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; retained "
                                                   "(frozen banks, store-off on 200 test tasks). G 2–3, M 3, X 2, Em 3, "
                                                   "Ec 2, Eh 1–2 (perturbed test tasks; displayed skills look "
                                                   "task-specific), Es 1, E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.27221v1, material sha 253b4727…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: decomposition skills learned from 20 gold-graded perturbed "
                                "queries and frozen give a large gain over generic decomposition (SR 7.0 → 38.5; XBench "
                                "41 → 73). The held-out reading is weakened by test-task content in the skills. "
                                "evidence_level retained (store-off on later tasks), claim_support scoped.",
            "rating_agreement": "M, X, Em, E.cost agree and were re-checked; G → son55, Ec → sol, Es → sol; shared "
                                "correction Eh 2 → 1. Final 55.0.",
        },
    }

    # =========================================================== 2604.27264 Self-Evolving Software Agents (Δ5)
    p = "2604.27264"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Preliminary experiments show that the agent is able to autonomously discover operational "
                              "goals",
                    "§3 Prototype and Preliminary Evaluation",
                    "The only result statement in the extended abstract: no environment instance, metric, count, run or "
                    "failure is given (A1 applies)."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55"),
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "crystallize_executable_capability", "H07")],
                           "unassigned": copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]),
                           "revision_proposals": []},
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.27264-1"): "local:2604.27264-2",
                    ("son55", "local:2604.27264-2"): "local:2604.27264-1"},
            overrides={
                "local:2604.27264-1": {"status": "unmet",
                                       "reason": "Coherence/inheritance of evolved behaviour (sol's local-1; son55's "
                                                 "local-2 asks the same). Unmet: modular separation is asserted, and the "
                                                 "authors report weak inheritance and robustness. son55's "
                                                 "'challenged_with_evidence' is reserved for a paper arguing against an "
                                                 "expectation; here the paper's own report shows the expectation unmet.",
                                       **moved("son55:local:2604.27264-2")},
                "local:2604.27264-2": {**moved("son55:local:2604.27264-1"),
                                       "reason": "Measurement of the prototype (environment, metric, runs, failures); "
                                                 "none reported (both seats unmet)."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01"]),
        "assessment": assess("son55", p, [], evidence_level=None,
                             evidence_level_note="No EVIDENCE.md level: no task output or score is measured (opus:O01). "
                                                 "Levels start at an observed gain (precedents cal-dev 1112.5309, r03b "
                                                 "2505.17716, r11b 2603.01145). Null, not 'none': son55's raw 'none' "
                                                 "is normalised to null.",
                             claim_support="unsupported",
                             strongest_supported_claim="A BDI–LLM architecture with an evolution module is proposed and a "
                                                       "prototype is said to exist; the feasibility claim (agents discover "
                                                       "goals and generate executable behaviours) has no reported "
                                                       "measurement, and the coherence claim is undercut by the authors' "
                                                       "own inheritance/robustness limits."),
        "ratings": {
            "G": R("resolved", 1, "Both seats 1; re-checked. 'Goals and capabilities fixed at design time' is a genuine "
                   "but generic limitation cited to software-engineering sources; no LLM-agent self-evolution neighbour "
                   "(code-writing or skill-library agents) is compared and no baseline failure is shown.",
                   ["son55:E002", "son55:E003", "sol:E001"]),
            "M": R("resolved", 1, "Opus sides with son55. Variation–selection–inheritance over knowledge, goals and "
                   "actions is a recognisable idea, but the operations, selection signal, trigger threshold and "
                   "assumptions are not given, and the stated coherence mechanism is undercut by the authors' own "
                   "inheritance/robustness limits. Between the 0 and 2 anchors; sol's 2 credited the conceptual fit.",
                   ["son55:E004", "son55:E010", "son55:E008", "sol:E003"]),
            "X": R("resolved", 1, "Both seats 1; re-checked. Trigger, environment validation and keep/discard are named; "
                   "selection criteria, persistence form, versioning, rollback and later reading are not described.",
                   ["son55:E006", "son55:E009", "son55:E011", "sol:E005"]),
            "E.measurement": R("not_reported", 0, "A1 (both seats): no metric, benchmark or validator is reported; the "
                               "one sentence on preliminary experiments is not a measurement (opus:O01).",
                               [], ["son55:E007", "opus:O01"],
                               ["Whole 2-page extended abstract (Abstract, §§1–4, Figure 1 caption); no tables, data "
                                "figures or appendix"]),
            "E.causality": R("not_reported", 0, "A1: no baseline, ablation or evolution-off comparison.", [], [],
                             ["Whole extended abstract, §3 and §4; no appendix"]),
            "E.holdout": R("not_reported", 0, "A1: no selection/test separation or held-out environment.", [], [],
                           ["Whole extended abstract, §3 and §4; no appendix"]),
            "E.statistics": R("not_reported", 0, "A1: no run counts, failures or uncertainty.", [], [],
                              ["Whole extended abstract, §3 and §4; no appendix"]),
            "E.cost": R("not_reported", 0, "A1: no model calls, tokens, time or evolution cost.", [], [],
                        ["Whole extended abstract, §3 and §4; no appendix"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text (2-page AAMAS extended abstract, no appendix) read. In scope as a minimal "
                  "system_method: LLM-generated goals/code are validated in the environment, retained and reused. Scored "
                  "under frozen anchor A1 (no reported measurement → five E items not_reported); the missing data is "
                  "the paper's property, not missing material. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "not claimed.",
        "figure_dependence": "Figure 1 is an architecture diagram; no data figures.",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "sol", "unsupported",
                "The central feasibility claim is asserted with no measurement in a complete text (opus:O01); a narrower "
                "supported claim would not be the authors'. 'unresolved' implies a pending evidence question; here the "
                "evidence is simply absent. Precedents r03b AgentRR and r11b AutoSkill: unsupported.",
                ["opus:O01", "sol:E006"], "none (claim_support is not scored)"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["crystallize_executable_capability", "H07"]],
                "H07 (forge capability when a gap appears) matches the trigger. H06 is not kept: it needs self-proposed "
                "practice tasks, execution-verified solutions and a curriculum-driven library; here operational goals "
                "are generated in deployment and no library or curriculum is described (son55 itself rated H06 'low').",
                ["sol:E002", "son55:E009"], NOSCORE),
            XC(p, "local:2604.27264-2", "sol", "unmet",
               "A4 cross-numbering: sol's local-2 (measurement) = son55's local-1; sol's local-1 (coherence) = son55's "
               "local-2. Final follows sol's numbering. local-2 (measurement) is unmet in both seats; son55's "
               "'challenged_with_evidence' belonged to the coherence question (now local-1, revised to unmet, see its "
               "note).", ["sol:E006", "son55:E007", "son55:E008"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "unmet",
               "Verified: behaviour generation sits inside the full BDI–LLM architecture with no isolated test.",
               ["son55:E004", "son55:E013"]),
            XC(p, "rsi:crystallize_executable_capability/F4", "son55", "unknown",
               "Verified: reuse conditions of retained behaviours are not described, so whether reuse is bounded by an "
               "input shape cannot be determined.", ["son55:E008"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 1,
                "See ratings.M: no operations, signals or assumptions are specified; the coherence claim is undercut by "
                "the authors.", ["son55:E004", "son55:E008", "son55:E010"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level", "sol_value": None, "son55_value": "none", "final_value": None,
             "kind": "normalisation (son55 only; not a mechanical conflict because rv2 normalises 'none' to null)",
             "reason": "'none' is not an EVIDENCE.md level. Canonical null with evidence_level_note: no measured output "
                       "exists, and levels start at an observed task gain.",
             "evidence_ids": ["opus:O01"], "score_impact": "none (evidence_level is not scored)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole text first. Initial view: in scope; A1 applies (no "
                                                   "measurement). G 1, M 1–2, X 1, E all not_reported; claim "
                                                   "unsupported, no evidence level.",
            "integrity_checks": "Both seats a1 on 2604.27264v1, material sha adbfdf18…; canonical seat hashes equal "
                                "conflicts.json; both outside_taxonomy with empty matches and non-empty reasons; domain "
                                "ids valid; both claim_type system_method.",
            "core_claim_check": "No measured result. A1's five not_reported items checked against the full text; no "
                                "formal result exists that would allow the A1 exception.",
            "rating_agreement": "G, X and the five E items agree; M → son55. Final 13.75.",
        },
    }

    # =========================================================== 2604.27488 Skills-Coach (Δ5)
    p = "2604.27488"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "agent-browser-clawdbot 0.0→0.75 0%→100% 0%→100% 0%→57.1%", "Table 2, first improved row",
                    "Pass rate 100% (every test task ≥70% of its maximum) coexists with a 57.1% advanced-task score; "
                    "under the stated metric definitions both cannot hold, so at least one metric is defined otherwise "
                    "than described.", kind="our_inference"),
            opus_ev(p, "O02", "azure-ai 0.17→0.83 0%→100% 20%→100% 14.3%→71.4%", "Table 2",
                    "Standard-task scores in fifths and advanced-task scores in sevenths recur across rows, which does "
                    "not fit the stated protocol of 4 standard + 4 advanced test tasks per skill.",
                    kind="our_inference"),
            opus_ev(p, "O03", "Limited Improvement (below +0.1) react-view-transitions 0.92→1.0",
                    "Table 2, lowest category",
                    "No skill regresses across 48 skills scored on 8 LLM-generated tasks; together with retain-or-discard "
                    "decisions made on the same test comparison, this is consistent with the reported 'optimized' "
                    "version being selected on the reporting set.", kind="our_inference"),
            opus_ev(p, "O04", "a rule-driven optimizer that automatically integrates caching, input validation, and "
                              "error-handling logic",
                    "§2.3 Code Optimization Pathway",
                    "The optimizer inserts exactly the features that the evaluation criteria reward (error handling, "
                    "validation), so gains can come from rubric conformance."),
            opus_ev(p, "O05", "Instruction-only skills Original 0.388 37.93% 46.90% 33.01%", "Table 1",
                    "With code-inclusive 0.343 (n=19) and instruction-only 0.388 (n=29), the weighted original average "
                    "is 0.370, not the 0.378 reported for all skills; the pass rates do reconcile (33.59%).",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus sides with son55. There is no ground-truth supervision per skill; the pipeline manufactures "
                      "it (generated train/test tasks, generated validation criteria, LLM judging, group-relative variant "
                      "scores) and adapts the artifact on that signal. Sub null: C08/C26 assume a trained model as the "
                      "adapted object. sol's adapt_via_conditioning (the optimised skill conditions a later agent) is "
                      "generic to every skill paper, and heterogeneous_decomposition (instruction-only vs code-inclusive "
                      "paths) describes a routing detail, not the paper's operation.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("son55", p, "population_search_executable_fitness", "H13")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.27488-3"): "local:2604.27488-4",
                    ("son55", "rsi:attribute_and_patch_incumbent/H11-2"): "rsi:attribute_and_patch_incumbent/H11.step2",
                    ("son55", "rsi:attribute_and_patch_incumbent/H11-5"): "rsi:attribute_and_patch_incumbent/H11.step5",
                    ("son55", "rsi:population_search_executable_fitness/H13-4"):
                        "rsi:population_search_executable_fitness/H13.step4",
                    ("son55", "rsi:population_search_executable_fitness/H13-5"):
                        "rsi:population_search_executable_fitness/H13.step5",
                    ("son55", "rsi:evidence_gated_retention/H31-2"): "rsi:evidence_gated_retention/H31.step2"},
            overrides={
                "local:2604.27488-1": {"status": "unmet",
                                       "reason": "Opus sides with son55 (same measurement-validity question): tasks, "
                                                 "criteria, optimisation scoring and evaluation share one generated "
                                                 "rubric family; instruction-only skills are judged on document-form "
                                                 "criteria the optimiser targets (opus:O04); fallback-mode use is not "
                                                 "reported; Table 1/2 numbers do not fit the stated protocol "
                                                 "(opus:O01, opus:O02, opus:O05).",
                                       **moved("son55:local:2604.27488-1")},
                "local:2604.27488-2": {"status": "unmet",
                                       "reason": "Opus sides with son55 (same holdout question): train and test tasks "
                                                 "come from the same generator and specification, the retain-or-discard "
                                                 "decision uses the reported test comparison (opus:O03), and no "
                                                 "downstream agent run uses the optimised skills on independent tasks.",
                                       **moved("son55:local:2604.27488-2")},
                "local:2604.27488-4": renum("son55:local:2604.27488-3"),
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "partial",
                    "reason": "Opus sides with son55: original and optimised versions are compared and a "
                              "retain-or-discard engine exists, which protects the incumbent at skill level; its rule is "
                              "unspecified and no per-task regression check is described."},
                "rsi:attribute_and_patch_incumbent/H11.step2": stepid("rsi:attribute_and_patch_incumbent/H11-2"),
                "rsi:attribute_and_patch_incumbent/H11.step5": stepid("rsi:attribute_and_patch_incumbent/H11-5"),
                "rsi:population_search_executable_fitness/H13.step4": stepid(
                    "rsi:population_search_executable_fitness/H13-4"),
                "rsi:population_search_executable_fitness/H13.step5": stepid(
                    "rsi:population_search_executable_fitness/H13-5"),
                "rsi:evidence_gated_retention/H31.step2": {
                    **stepid("rsi:evidence_gated_retention/H31-2"),
                    "reason": "Kept as a check question only (H31 not retained as a match): the retain rule's statistic "
                              "is not stated; it is applied on the test comparison that is also reported."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: Table 1/2 values do not fit the stated 4+4 test protocol and metric definitions (opus:O01, opus:O02, "
            "opus:O05).",
            "Opus: no regression across 48 skills is consistent with test-set retention (opus:O03)."]),
        "ratings": {
            "G": R("resolved", 1, "Opus sides with son55. 'Abundant volume but fragmented coverage' is asserted with "
                   "generic citations, and the method (optimising one skill against tasks derived from its own "
                   "documentation) does not address ecosystem coverage. The nearest neighbours — prompt/code optimisers "
                   "(TextGrad, DSPy, APO, cited as method sources) and existing skill-improvement skills (skill-creator, "
                   "self-evolving-skill, which sit inside Skill-X itself) — are not positioned. Between 0 and 2.",
                   ["son55:E002", "son55:E003", "sol:E003"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. A concrete pipeline (generated tasks, grouped variant "
                   "selection, rule/LLM/auto-fix code optimisation, paired comparison, retain/discard) with execution "
                   "evidence for code skills. 'Training-free GRPO' reduces to best-of-3 selection, the optimisation "
                   "signal is the evaluation rubric, and the rule-driven optimiser inserts rubric features (opus:O04).",
                   ["son55:E007", "son55:E010", "son55:E024", "sol:E003", "opus:O04"], ["son55:E012"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Epochs, group size, task counts, isolation and modes are "
                   "specified; the retention rule, persistence/versioning, rollback, ecosystem-consistency handling and "
                   "later reading by an agent are missing.",
                   ["son55:E006", "son55:E007", "son55:E016", "son55:E022", "sol:E005"]),
            "E.measurement": R("resolved", 1, "Both seats 1; re-checked, with an Opus addition (shared omission, no "
                               "rating change). Code-skill checks are execution-based but shallow (file existence, "
                               "keywords, regex); 29 of 48 skills are LLM-scored on documentation-form criteria an "
                               "optimiser can satisfy by restructuring; tasks and criteria come from the optimising "
                               "pipeline. The reported numbers also do not fit the stated protocol (opus:O01, opus:O02, "
                               "opus:O05).",
                               ["son55:E011", "son55:E012", "son55:E025", "sol:E001", "sol:E012", "opus:O01",
                                "opus:O02", "opus:O05"], ["son55:E024"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only original vs optimised; no ablation of GRPO "
                             "selection, auto-fix or task generation, and no one-shot rewrite, alternative optimiser or "
                             "equal-budget baseline, so gains cannot be separated from rubric-conforming rewriting "
                             "(opus:O04).", ["son55:E014", "son55:E015", "sol:E013", "opus:O04"], ["son55:E010"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Train and test tasks are separate but come from the "
                           "same generator and specification; the retain-or-discard decision is made on the test "
                           "comparison that is reported (son55:E017, son55:E018), and Table 2 shows no regression across "
                           "48 skills (opus:O03); no external task or downstream agent run exists. sol's 2 relied on "
                           "variant selection using the training set, which does not cover the final retention.",
                           ["son55:E006", "son55:E009", "son55:E017", "son55:E018", "opus:O03"], ["sol:E002"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 tier 1): per-skill rows and the no-gain cases are "
                              "reported; single run, no intervals or variance, means over ~8 tasks per skill.",
                              ["son55:E006", "son55:E021", "sol:E014"]),
            "E.cost": R("not_reported", 0, "Opus sides with sol. Epochs, group size, task counts, fix rounds and model "
                        "are settings, not cost (r12a UI-Mem, r13b PsychAgent precedent); the 'hours to minutes' and "
                        "'thousands to dozens' claims are unmeasured, and no tokens, calls, time or dollars are given.",
                        [], ["son55:E019", "sol:E015"],
                        ["Full text §§1–4, Tables 1–3, Appendices A–B and figure captions of the pinned v1 text"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (method, Tables 1–2, Appendix A rubric, Appendix B sources). In scope "
                  "(system_method): non-weight skill instructions and code are rewritten from generated-task feedback "
                  "and kept or discarded; downstream reuse is not shown. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 1, 3, 4 restate tabled values or show a case report; values from Tables 1–3 only.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "'Retained' needs the kept modification to improve later tasks beyond the selection set. The "
                "retain-or-discard decision uses the same test comparison that is reported (son55:E017, son55:E018; "
                "opus:O03), and no downstream use is shown. SCORE_SPEC: selection-set gains do not justify 'retained'.",
                ["son55:E017", "son55:E018", "opus:O03"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "See rs_pattern.reason: the supervisory signal is manufactured by the pipeline.",
                ["son55:E010", "son55:E025"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", None]],
                "adapt_via_conditioning is generic here; heterogeneous_decomposition is a routing detail without the "
                "card's evidence that differentiated treatment is needed.", ["son55:E010", "sol:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H11"], ["population_search_executable_fitness", "H13"]],
                "H11 and H13 agreed. son55's H31 (fit low) is not kept: a commit rule whose statistic is unstated and "
                "which is applied on the reported test comparison does not instantiate a statistically sound commit "
                "rule; the question stays as check question H31.step2.", ["son55:E016", "son55:E018"], NOSCORE),
            XC(p, "local:2604.27488-1", "son55", "unmet",
               "Same measurement-validity question in both seats. Unmet: shared rubric family, document-form criteria, "
               "and numbers inconsistent with the protocol (opus:O01, opus:O02). sol's partial credited the disclosure "
               "of real/virtual modes, which is son55's separate local-3 (now local-4, met).",
               ["son55:E012", "son55:E025", "opus:O01", "opus:O02"]),
            XC(p, "local:2604.27488-2", "son55", "unmet",
               "Same holdout question. Unmet: same generator, test-set retention (opus:O03), no downstream run.",
               ["son55:E017", "sol:E002", "opus:O03"]),
            XC(p, "local:2604.27488-3", "sol", "unmet",
               "A4 collision: sol's local-3 asks whether the efficiency claim is measured (unmet, verified); son55's "
               "local-3 (mode disclosure, met) moved to local-4.", ["sol:E015", "son55:E005"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "partial",
               "Verified: 48 skills from three sources; one model family; no cross-model or downstream test.",
               ["son55:E008"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "unmet",
               "Verified: no ablation of GRPO, auto-fix or task generation.", ["son55:E014", "son55:E015"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "unmet",
               "Verified: for instruction-only skills the objective is a documentation-quality score.",
               ["son55:E011", "son55:E012"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "unmet",
               "Verified: no cost versus benefit.", ["son55:E019"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "unmet",
               "Verified: tasks, criteria, optimisation and LLM-mode judging come from one pipeline/model family.",
               ["son55:E008", "son55:E010", "son55:E025"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-2", "son55", "unmet",
               "Renamed H11.step2 (A4). Verified: no separation of skill defects from execution lapses.",
               ["son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-5", "son55", "unmet",
               "Renamed H11.step5 (A4). Verified: retention uses the reported test comparison.",
               ["son55:E017", "son55:E018"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "The skill-level original-vs-optimised comparison with retain-or-discard protects the incumbent; the "
               "rule and per-task regression checks are missing. sol's unmet looked only at the auto-fixer.",
               ["son55:E016", "son55:E017", "sol:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: the auto-fixer sees failure analyses and logs; instruction-only skills get judged text only.",
               ["son55:E007", "son55:E017"]),
            XC(p, "rsi:evidence_gated_retention/H31-2", "son55", "unknown",
               "Renamed H31.step2; kept as a check question (H31 not retained). The statistic of the retain rule is not "
               "stated, so soundness cannot be determined.", ["son55:E016", "son55:E018"]),
            XC(p, "rsi:population_search_executable_fitness/H13", "sol", "partial",
               "Verified: variants are scored on a small generated set and the best kept; no random, one-shot or "
               "simple-rewrite control.", ["sol:E003", "sol:E008"]),
            XC(p, "rsi:population_search_executable_fitness/H13-4", "son55", "partial",
               "Renamed H13.step4 (A4). Verified: budget parameters listed, no calls/tokens/time.", ["son55:E007"]),
            XC(p, "rsi:population_search_executable_fitness/H13-5", "son55", "unmet",
               "Renamed H13.step5 (A4). Verified: no single-pass rewrite, random selector or other optimiser.",
               ["son55:E007", "son55:E019"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "unmet",
               "Verified: surface rubric items and keyword/regex checks are easy to satisfy by rewriting (opus:O04); "
               "no rank transfer to downstream success.", ["son55:E012", "son55:E013", "opus:O04"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 1,
                "See ratings.G: the stated gap is not what the method addresses, and the nearest neighbours are not "
                "positioned.", ["son55:E002", "son55:E003"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: retention is decided on the reported test comparison; same generator; no "
                "external tasks.", ["son55:E017", "son55:E018", "opus:O03"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 0,
                "See ratings.E.cost: settings are not cost; the efficiency claims are unmeasured. Final status "
                "not_reported with search scope.", ["son55:E019", "sol:E015"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "1 (protocol-inconsistent numbers not noted)",
             "son55_value": "1 (protocol-inconsistent numbers not noted)", "final_value": 1,
             "reason": "Shared omission, no rating change. Table 2 fractions (fifths, sevenths) do not fit 4 + 4 test "
                       "tasks (opus:O02); a 100% pass rate coexists with a 57.1% advanced-task score under a 70% "
                       "threshold (opus:O01); Table 1's original average 0.378 does not match its subgroups (0.370, "
                       "opus:O05). Recorded in E.measurement.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O05"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; task level "
                                                   "(retention on the test comparison). G 1, M 2, X 2, Em 1 (rubric "
                                                   "gaming; inconsistent tables), Ec 0–1, Eh 1, Es 1, E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.27488v1, material sha 50d5343e…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: under the pipeline's own generated tasks and rubric, rewritten "
                                "skills score higher than the originals on 48 public skills. Real-use improvement, "
                                "retained reuse and efficiency are not shown. evidence_level task, claim_support scoped.",
            "rating_agreement": "M, X, Em, Ec, Es agree and were re-checked; G → son55, Eh → son55, E.cost → sol. "
                                "Final 33.75.",
        },
    }

    return S
