"""Opus rulings for r20b a1 (data only; consumed by _build.py)."""
import copy

PAGE_SET_NOTE = ("2605.18401 page images (71 files) are present in materials/2605.18401.pages/, but the batch manifest "
                 "has no page_images entry and materials/2605.18401.pages.json (named in the dispatch) does not exist. "
                 "Opus computed sha256 for every page it opened and records them per page; the controller should pin the "
                 "page set in the manifest before indexing.")


def batch_notes():
    return [
        "2605.18401 SkillsVote (status conflict: sol needs_fulltext vs son55 reviewed). MATERIAL RULING: reviewed. The "
        "missing Appendix 12 (PDF Appendix G) prompt bodies were read from the page images (pp. 45, 56–63, 71). They "
        "are implementation detail. The core-claim evidence (Tables 1–4, Fig. 5–6, §8 protocol) is in the pinned text "
        "or in the figures (pp. 9–10). The prompts confirm the text's description of what each mode sees: online "
        "attribution gets only task-level verifier counts; offline oracle mode adds solution/, verifier/tests/ and "
        "test-stdout; the skill-creator baseline gets the same verifier counts and ground-truth context (p. 71). "
        "Appendix 12 does not carry core-claim evidence, so no dual-seat a3 is required for material reasons. Because "
        "sol deferred all eight items, this score rests on son55 plus Opus re-check (as with SE-GPT in r01b). An "
        "optional sol a3 (text + page images) is advisable only if the controller requires two independent seat "
        "ratings for this paper. Final 63.75 (= son55; every item re-checked). Opus corrected son55's 'no "
        "de-attribution ablation': skill-creator is that ablation, with the same verifier signal. Its gains are "
        "mixed: 0.0/+5.2/+1.9 on TB2, +1.7/+0.3/+3.8 on SWE-Pro, with no variance.",
        "2605.18729 Robo-Cortex (status conflict: sol needs_fulltext vs son55 reviewed). MATERIAL RULING: reviewed, "
        "following the SE-GPT precedent. The only gap is 'Additional implementation details are provided in the "
        "supplementary material', which is author-side material outside the arXiv v1 record. Every result the claims "
        "rest on (Tables 1–3, the Fig. 4 numbers in §4.3, the real-world 4/10) is in the pinned text. The supplement "
        "could only move X (thresholds/prompts) and E.cost (if it held compute numbers). X=2 rests on design facts "
        "stated in the main text: no retention gate or rollback, an unstated source for the static memory, and online "
        "rewriting that harms the transferred prior. E.cost is not_reported with the search scope recorded. If the "
        "controller later obtains the supplement, re-dispatch only those two items. Final 43.75 (= son55). Opus "
        "additions, not changing ratings: (i) the Fig. 4 round-1 numbers coincide with differently labelled Table 3 "
        "rows ('on-split' = 'w/ manual heur.', 'from-scratch' = 'w/ manual heur. + update'); (ii) IGNav SR values "
        "imply varying episode denominators (144/140/143/142 across Table 1 methods; 72/71/70/68 within splits), "
        "i.e. unexplained dropped episodes. son55's 'all SR are multiples of 1/72' is wrong (36.62 = 26/71).",
        "2605.19576 Library Drift (Δ15): final 47.5 (= sol). The five disputed items go to sol after reading the text. "
        "G 2: the gap premise that unbounded accumulation causes drift is never reproduced (A1 is injection-off, A4 "
        "is over-governance). The paper's own A3 makes the authoring prior the single most valuable component, which "
        "contradicts its 'not the author; the librarian' framing. X 2: rollback exists only in the hyperparameter "
        "table. Table 1's A1 row is inconsistent with the stated mechanism: 42 skills synthesised and 15 retired with "
        "0 critic calls and 0 injections, although synthesis needs critic-verdict clusters and retirement needs "
        "n(s) ≥ N_min trials. E.measurement 2: Eq. 2's 'contribution' is not a contribution, and the A1 row is "
        "inconsistent. E.holdout 1: the router injects on the 40 eval tasks every round and Eq. 2 draws on 'capsules "
        "where s was injected', with no train-only restriction. Those 40 tasks are reused across 100 rounds and 9 "
        "conditions. E.cost 2: the 14.5k-call tally omits the per-task LLM router-gate calls. Shared items (M 2, "
        "E.causality 2, E.statistics 2) confirmed. RS → assumption_audit_and_pivot/C11 (budgeted retention rule "
        "pivoted from append-only to outcome-driven retirement, with a certificate whose failure mode matches Prop. "
        "1) plus supporting controlled_diagnostic_design/C02. adapt_via_conditioning is not kept. Domain → H30 + "
        "H32 + H31.",
        "2605.21240 APEX (Δ10): final 65.0, between the seats (sol 60 / son55 70). G 3 → son55: the bottleneck is "
        "concrete, with a same-backbone diagnostic, and the nearest neighbours (Reflexion/EvoTest/ACE) are run as "
        "baselines. X 2 → sol: Appendix C adds skipped milestones to a 'per-episode completed set', which contradicts "
        "§4.1's actual-achievement eligibility unless the sets are separate. Completion is self-reported, and "
        "LLM-proposed nodes face no gate or rollback. E.cost 3 → son55: episode/step budgets are equal and WebArena "
        "API dollars are given for all six methods. Shared items (M 3, E.measurement 3, E.causality 3, E.holdout 2, "
        "E.statistics 1) confirmed. The Zork1 70.2 vs 73.0 same-config inconsistency is charged once, to E.statistics "
        "(A2). RS → reframe_as_solvable_object (sub null); sol's supporting adapt_via_conditioning is not kept. "
        "Domain → H01 + H04 + H29.",
        "2605.21810 Trace2Skill (Δ1.25): final 52.5 (= sol). E.holdout 0 → sol: the hidden verifier is the selection "
        "signal (pass-dominant SelectQ), the in-rollout feedback source, and the evaluation. Results come from the "
        "optimisation rollouts themselves, and no frozen skill or held-out task is evaluated (A2: oracle signal → "
        "E.holdout). E.statistics 2 → sol (A2 tier 2: per-task repeated-run pass counts with denominators, no "
        "cross-EA-run variance). Both seats' E.causality 1 is confirmed and strengthened by Opus: 'Solved/8' "
        "compares ≥1 pass in 80 rollouts (C3/C4) with ≥1 in 4 (C1/C2), and C1's 0/32 is the selection set (96 = 24×4 "
        "baseline rollouts picked the 8 tasks). Both seats' evidence_level 'task' is correct (EVIDENCE rule 2). RS → "
        "son55 self_supervised_signal_engineering/C26 (sparse pass/fail re-granularised into dense ranking "
        "signals); adapt_via_conditioning not kept. Domain → sol H15 + H10 (single incumbent document rewritten from "
        "diagnosed errors; no defect-vs-lapse gate, so not H11). son55's unknown on the 8-of-15 task selection "
        "criterion is kept: the bold markers are lost in extraction, and only 3 of the 8 are identifiable by name.",
        "Batch-level: (1) " + PAGE_SET_NOTE + " (2) A4 hidden ID collisions: the two seats reused the same local: ID "
        "for different questions in 19576 (-1), 21240 (-1, -2) and 21810 (-1). Opus renumbered the son55 questions "
        "(19576 -1→-3; 21240 -1→-4, -2→-5; 21810 -1→-4). son55's 'rs:assumption_audit_and_pivot/RE-1' quoted RE-6's "
        "content and is renumbered RE-6. (3) adapt_via_conditioning used as a generic 'frozen model reads stored "
        "text' substrate is not retained as an RS match unless the paper's claim is conditioning-based "
        "generalisation (kept only for Robo-Cortex, sub null, r17b convention). Its seat expectations stay as check "
        "questions. (4) No card was edited. Proposals: an H30/H31 note on authoring-prior vs explicit-dedup "
        "(19576, from son55); a C26 note that the target can be a non-weight artifact selected by a manufactured "
        "signal (21810).",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    opus_img_ev = g["opus_img_ev"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"

    def C(p, f):
        return conflict(p, f)

    def XC(p, eid, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", *C(p, f"expectations[{eid}].status"), dec, final, reason, ev, NOEXP)

    def RC(p, k, dec, final, reason, ev=(), impact=""):
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

    def renum(old, new_q):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        f"question). Question: {new_q}"}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as an RS match in this final record "
                        "(see resolutions on rs_pattern.matches)."}

    def rr(v, st="resolved"):
        return {"status": st, "rating": v}

    def with_extra(exps_fn, extra):
        def f(sol, son):
            return exps_fn(sol, son) + extra
        return f

    # =========================================================== 2605.18401 SkillsVote (status conflict)
    p = "2605.18401"
    g["PAGES_READ"][p] = {
        "p-09.png": "§4.3.1–4.3.2, Figure 4 routing curves and Figure 5 recommendation heatmap",
        "p-10.png": "§4.3.3 and Figure 6 offline-evolution checkpoints / library growth",
        "p-45.png": "Appendix G.1 profiling prompt (quality/verifiability rubric) — sample of the missing prompt bodies",
        "p-56.png": "Appendix G.3 end; G.4 post-execution attribution user prompt lines 1–20",
        "p-57.png": "G.4 attribution prompt lines 21–51 (schema)",
        "p-58.png": "G.4 attribution prompt lines 52–72 (attribution enum, skill refs)",
        "p-59.png": "G.4 attribution prompt lines 73–116 (subtask rules, attribution rules)",
        "p-60.png": "G.4 attribution prompt lines 117–151 (judge rules, trusted-verifier assumption)",
        "p-61.png": "G.4 lines 152–181 and the offline Reference Context Prompt header",
        "p-62.png": "Reference Context Prompt body (solution/, verifier/tests/, test-stdout) and G.5 edit system prompt start",
        "p-63.png": "G.5 edit system prompt lines 23–59 (action types)",
        "p-71.png": "G.5 create user prompt and the skill-creator baseline user prompt",
    }
    S[p] = {
        "base": "son55",
        "material_sections": [
            "Appendix 12 (PDF Appendix G) prompt bodies are absent from the text extraction (headings only); they were "
            "read from the page images listed below (pp. 45, 56–63, 71). Figures 4–6 read from pp. 9–10."],
        "opus_evidence": [
            opus_ev(p, "O01", "attribution-guided evolution with a single prompt that instructs the agent to use the",
                    "§8.2 Baselines (3) skill-creator",
                    "skill-creator replaces only the attribution-guided evolution step. The rest of the SkillsVote "
                    "pipeline (recommendation, session resume) is unchanged, so it is the de-attribution / de-gating "
                    "ablation, with prompt differences."),
            opus_img_ev(p, "O02", "p-71.png",
                        "The task-level ground-truth verifier reported: out of a total of {num_total_test_cases} "
                        "private test cases, {num_passed_test_cases} passed and {num_failed_test_cases} failed.",
                        "p.71, User Prompt for skill-creator Baseline, line 14 (also line 12 '{ground_truth_context}')",
                        "The skill-creator baseline receives the same verifier counts and ground-truth context slot as "
                        "SkillsVote's attribution prompt (p.56 line 12), so the comparison is matched on feedback "
                        "information."),
            opus_img_ev(p, "O03", "p-56.png",
                        "This signal should be interpreted as the authoritative final evaluation of the whole task, "
                        "rather than as evidence about any single subtask in isolation.",
                        "p.56, G.4 attribution User Prompt, lines 12–14",
                        "Online attribution reads the benchmark's own ground-truth verifier counts for each test-stream "
                        "task. That is an oracle signal on evaluation tasks (A2 → E.holdout), used only for later tasks."),
            opus_img_ev(p, "O04", "p-60.png",
                        "Please assume that a trusted verifier covers the complete test space, including all relevant "
                        "cases, not just a subset. Therefore, it is possible for the overall task to be successful even "
                        "if some subtasks failed along the way",
                        "p.60, G.4 attribution prompt line 142",
                        "Admission is decided per subtask by the resumed solver's own judgement under this instruction. "
                        "A failed task can still yield 'successful' subtasks that edit skills (NodeBB case, opus:O08)."),
            opus_img_ev(p, "O05", "p-62.png",
                        "`solution/`: the ground-truth solution files for this task. `verifier/tests/`: the verification "
                        "test files for this task. `verifier/test-stdout.txt`: the stdout produced by the verification "
                        "tests. ... Do not copy answers, canary strings, fixed private values, one-off paths, or exact "
                        "ground-truth outputs into `exploration`.",
                        "p.62, Reference Context Prompt (Offline Evolution Optional), lines 4–9",
                        "Offline oracle mode exposes source-task solutions and tests to attribution; leakage into skills "
                        "is prevented only by this instruction. It applies to TB-Pro source tasks, not to TB2 targets."),
            opus_img_ev(p, "O06", "p-09.png",
                        "Online w/o rec. ↑3.3 / ↓6.7; w/ rec. ↑6.0 / ↓6.0. Offline w/o rec. ↑11.3 / ↓3.3; w/ rec. "
                        "↑15.3 / ↓2.0",
                        "p.9, Figure 5 column footers",
                        "Net online w/ rec. = 0.0 and offline w/ rec. = +13.3 on TB2 Hard. These equal the GPT-5.4 mini "
                        "Hard deltas in Table 1 (online 30.0 vs 30.0; TB-Pro 43.3 = +13.3), so the recommendation "
                        "ablation is one backbone on 30 Hard tasks; the caption does not name the backbone.",
                        kind="our_inference"),
            opus_img_ev(p, "O07", "p-10.png",
                        "Figure 6 left: Terminal-Bench 2.0 Hard avg@3 at steps 3/6/9/12 ≈ 30 / 32 / 38 / 42 against a "
                        "w/o-skills line ≈ 28; Terminal-Bench Pro ≈ 53.5 / 51.4 / 49.3 / 52.1 against ≈ 52. Right: "
                        "created ≈ 7/8/5/9, edited ≈ 1/3/2/4, total ≈ 7/15/20/29.",
                        "p.10, Figure 6 (values read approximately from plotted points)",
                        "The offline library's transfer to TB2 Hard grows over checkpoints while source-task "
                        "performance does not. Single run, unstated backbone, avg@3, no variance.",
                        kind="our_inference"),
            opus_ev(p, "O08", "private tests passing with six failures remaining", "§11.2 NodeBB case, Subtask 6",
                    "The task failed the verifier (421/427), yet subtasks 2 and 5 were labelled successful and "
                    "nodebb-bootstrap-repro was edited. Admission is subtask-level self-judgement, not task-level "
                    "verified success."),
            opus_ev(p, "O09", "TypeScript contributes 20 tasks from tutao/tutanota.", "§8.3 Dataset; Table 2 tutanot. column",
                    "Table 2's tutanota column is 0.0 in all 18 rows (every method and backbone, including GPT-5.5 "
                    "xhigh). This is consistent with an environment failure counted in every denominator. It is "
                    "uniform across methods, so deltas are unbiased, but the overall rates include 20 never-solvable "
                    "tasks.", kind="our_inference"),
            opus_ev(p, "O10", "Online mode provides only task-level test counts, including the total, passed, and "
                              "failed counts.", "§10.7 step 4",
                    "Text statement of the online information boundary, confirmed by the prompt (opus:O03)."),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus accepts son55 (sol identified nothing under needs_fulltext). The distinctive operation "
                      "partitions each trajectory into subtasks by a discriminating property (outcome evidence × "
                      "responsibility) and applies a tailored treatment per class (create / edit / skip; Tables 12–13). "
                      "C04 is compression of trained artifacts, so sub=null. Alternatives considered: decompose_and_"
                      "delegate (routing is to LLM prompts, not sound solvers) and attribute_and_patch-style cards "
                      "(failures never drive edits).",
            "matches": [smatch("son55", p, "heterogeneous_decomposition", role="primary")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "reason": "Opus accepts son55. H02: skill packages are mined from interaction streams, "
                                     "with dedup and quality profiling of the corpus. H30 partial: an admission gate "
                                     "exists, but there is no retirement, cap or regression replay. H11 was considered "
                                     "and not added: failure attributions are always skipped, so no failure ever "
                                     "drives a skill revision.",
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={
            "rsi:evidence_gated_retention/S3": {
                "reason": "son55's status confirmed. Fig. 5 (pp. 9; opus:O06) shows that direct exposure of the online "
                          "library is net negative (+3.3/−6.7) and recommendation balances it (+6.0/−6.0). This is "
                          "one backbone (GPT-5.4 mini by Table 1 match) on 30 Hard tasks, and it governs exposure, not "
                          "admission. Partial."},
            "rs:heterogeneous_decomposition/RE-3": {
                "reason": "Unmet confirmed. skill-creator (opus:O01/O02) removes the whole attribution apparatus at "
                          "once. No arm isolates a single differentiated treatment (e.g. admitting failed subtasks, or "
                          "edit vs create)."}}),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O03", "opus:O09"]), "C3", ["opus:O06"]),
        "assessment": assess("son55", p, [
            "Opus: skill-creator (same verifier counts and ground-truth slot, opus:O01/O02) is the de-attribution "
            "ablation. SkillsVote − skill-creator = 0.0/+5.2/+1.9 (TB2) and +1.7/+0.3/+3.8 (SWE-Pro), with no "
            "variance.",
            "Opus: admission is subtask-level self-judgement by the resumed solver. Failed tasks can still edit skills "
            "(opus:O04, opus:O08).",
            "Opus: the Fig. 5 recommendation ablation is one backbone on 30 Hard tasks (opus:O06).",
            "Opus: TB-Pro→TB2 overlap/near-duplicate audit absent (local:2605.18401-1 stays unknown)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus re-check = son55. The problem has sources: skill benchmarks showing that weak or "
                   "poorly matched skills degrade agents ([23,32]), and ecosystem redundancy. The paper's own Fig. 5 "
                   "shows direct-exposure harm. Neighbours ReasoningBank and skill-creator are run as baselines, and "
                   "SkillRouter is compared on routing. Not 4: the claimed residual gap (subtask-level attribution "
                   "between trajectory and step) is argued, not tested against alternative granularities.",
                   ["son55:E001", "son55:E012", "son55:E014", "opus:O06"], ["son55:E013"]),
            "M": R("resolved", 3, "Opus re-check = son55. Three-axis attribution → success-only admission → "
                   "aggregation → edit/create/skip routing is reconstructable (Tables 11–13, prompts pp. 56–63), and it "
                   "predicts a difference from a direct trajectory-to-skill baseline. Thin assumptions: the resumed "
                   "solver's self-attribution is never validated, the verifier-covers-everything instruction (opus:O04) "
                   "lets failed tasks produce admitted subtasks, and failures never repair or retire a skill.",
                   ["son55:E002", "son55:E021", "opus:O04"], ["son55:E019", "opus:O08"]),
            "X": R("resolved", 3, "Opus re-check = son55, now with the prompt bodies read (pp. 56–63, 71). Information "
                   "permissions per mode (opus:O03, opus:O05, opus:O10), the admission rule (§9.7), batch aggregation, "
                   "versioned backup before edits, retry/fallback, and the exact attribution/evolution schemas are "
                   "explicit. Not 4: no retirement, cap, conflict resolution or regression check, and recommendation "
                   "failure falls back to exposing the whole library (son55:E005).",
                   ["son55:E002", "son55:E003", "son55:E004", "opus:O03", "opus:O05", "opus:O10"], ["son55:E005"]),
            "E.measurement": R("resolved", 3, "Opus re-check = son55. Executable official verifiers (TB2 avg@5, "
                               "SWE-Bench Pro avg@1) are used. Exclusions are uniform (4 GPT-5.5 TB2 tasks blocked by "
                               "cyber-risk review, removed from every GPT-5.5 setting). Note: tutanota is 0.0 in all 18 "
                               "rows (opus:O09); this is uniform and does not bias deltas. Attribution quality is not "
                               "measured independently.",
                               ["son55:E009", "son55:E015", "son55:E016"], ["opus:O09"]),
            "E.causality": R("resolved", 2, "Opus re-check = son55, with one correction to its reason. A "
                             "de-attribution control does exist: skill-creator, with matched verifier information "
                             "(opus:O01/O02). Its margins are mixed and small (0.0 to +5.2 pp, no variance). The "
                             "recommendation ablation is a single backbone on Hard (opus:O06). Recommendation guidance "
                             "text is confounded with skill content. TB-Pro and Curated libraries differ in content as "
                             "well as origin. Recommendation and attribution add agent runs with no cost-matched arm.",
                             ["son55:E010", "son55:E012", "son55:E014", "opus:O01", "opus:O02", "opus:O06"],
                             ["son55:E011", "son55:E020"]),
            "E.holdout": R("resolved", 2, "Opus re-check = son55. Offline transfer is a real source/target split "
                           "(TB-Pro → TB2), but there is no overlap audit, and the Apache→git-webserver case shows "
                           "close neighbours. Online evolution uses the evaluation stream's own ground-truth verifier "
                           "counts for later tasks (opus:O03). That fits the online claim but is an oracle signal (A2). "
                           "Offline oracle exposure is controlled only by prompt (opus:O05).",
                           ["son55:E006", "son55:E007", "son55:E008", "son55:E010", "opus:O03", "opus:O05"]),
            "E.statistics": R("resolved", 1, "Opus re-check = son55 (A2 tier 1). TB2 is avg@5 over 5 independent jobs, "
                              "but no std/CI is reported. SWE-Bench Pro is a single run. Online gains of 0.9–2.7 pp sit "
                              "at noise level. Negative results (Curated regressions, Hard-split drops) are reported.",
                              ["son55:E009", "son55:E016", "son55:E011"], ["son55:E013"]),
            "E.cost": R("resolved", 1, "Opus re-check = son55. Only the routing study's per-query API cost is reported "
                        "(Table 3/4, 'We report API cost for SkillsVote only'). The extra recommendation run, the "
                        "resumed attribution session and the evolution calls on TB2/SWE-Pro are not costed against the "
                        "baselines.", ["son55:E017"], [],
                        ["full text incl. Appendices 6–11 and Appendix G prompts (pp. 43–71): cost/token/budget only "
                         "in §4.3.1/Table 3–4"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read. The Appendix 12/G prompt bodies missing from the extraction were read "
                  "from page images pp. 45, 56–63 and 71, and Figures 5–6 from pp. 9–10 (sha256 per page in "
                  "materials). The prompts are implementation detail that confirms §10.6–10.8. Core-claim evidence is "
                  "in Tables 1–4 and Figures 5–6, so the paper is reviewable. All eight items are resolved after "
                  "re-check of son55's ratings; sol deferred.",
        "aggregate_status": "accepted_final",
        "material_ruling": "reviewed (not needs_fulltext). Appendix 12 (prompt bodies) is auxiliary implementation "
                           "detail and does not carry core-claim evidence. It was read from the page images and "
                           "confirms the text.",
        "a3_recommendation": "not required for material reasons. Optional sol a3 (text + page images) only if the "
                             "controller requires two independent seat ratings; the current score rests on son55 + "
                             "Opus re-check.",
        "a3": "none (in scope; non-weight skill library).",
        "improver_check": "not claimed; the attribution/evolution procedure is fixed.",
        "figure_dependence": "Figures 5–6 are image-only; read from page images pp. 9–10 (opus:O06, opus:O07). Figure 6 "
                             "values are approximate readings and are not used for scoring.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "The frozen TB-Pro library transfers to a different benchmark's tasks (+7.8/+5.8/+1.4 pp avg@5), and "
                "Fig. 6 shows transfer growing with checkpoints. Retained changes improve later held-out tasks. sol's "
                "null was its needs_fulltext deferral.", ["son55:E010", "opus:O07"], "none (label is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", "scoped",
                "The narrow conclusion is supported: frozen libraries plus recommendation improve TB2, and online gains "
                "are small and consistent. The attribution-control claim is not established by a controlled margin "
                "(skill-creator margins mixed).", ["son55:E009", "son55:E010", "opus:O01"], "none (label is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "heterogeneous_decomposition",
                "See rs_pattern.reason. sol identified nothing (needs_fulltext).", ["son55:E002", "son55:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["heterogeneous_decomposition", None]],
                "Accepted after checking alternatives (rs_pattern.reason).", ["son55:E002", "son55:E021"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["evidence_gated_retention", "H30"]],
                "Accepted; H11 considered and rejected (domain_pattern.reason).", ["son55:E002", "son55:E004"], NOSCORE),
            XC(p, "local:2605.18401-1", "son55", "unknown",
               "No overlap/near-duplicate check between the 48 TB-Pro source tasks and TB2 is reported anywhere, "
               "including the appendix prompts. It stays unknown and does not affect the score.", ["son55:E007"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "unmet",
               "See expectation override: no per-treatment isolation.", ["son55:E014", "opus:O01"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "son55", "partial",
               "ReasoningBank and skill-creator under matched harness and verifier information (opus:O02); prompts "
               "and flows still differ.", ["son55:E014", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
               "An admission rule plus backup exist; there is no execution test or retirement.", ["son55:E002", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Only success-attributed exploration edits skills, and a backup is kept; there is no regression check or "
               "rollback trigger.", ["son55:E002", "son55:E004"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "No skill-on/off marginal credit for admitted entries; the gate is LLM self-attribution (opus:O04).",
               ["son55:E002", "opus:O04"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "There is an admission gate but no retirement or size bound anywhere, including the G.5 action types "
               "(p.63: error_fix/knowledge_addition/prerequisite_addition/create_skill/skip; no delete).",
               ["son55:E004"]),
            XC(p, "rsi:evidence_gated_retention/S3", "son55", "partial", "See expectation override (Fig. 5 scope).",
               ["son55:E012", "opus:O06"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial",
               "Only the routing per-query cost is stated; attribution/evolution cost is not.", ["son55:E017"]),
            RC(p, "G", "son55", rr(3), "See ratings.G. sol unknown = needs_fulltext deferral (overruled by the material "
               "ruling).", ["son55:E001", "son55:E012"], "+11.25 (row now scored; sol null)"),
            RC(p, "M", "son55", rr(3), "See ratings.M.", ["son55:E002", "opus:O04"], "+15 (row now scored)"),
            RC(p, "X", "son55", rr(3), "See ratings.X; prompt bodies now read from page images.",
               ["son55:E002", "opus:O03", "opus:O05"], "+15 (row now scored)"),
            RC(p, "E.measurement", "son55", rr(3), "See ratings.E.measurement (tutanota note added).",
               ["son55:E009", "opus:O09"], "+7.5 (row now scored)"),
            RC(p, "E.causality", "son55", rr(2), "Rating kept; son55's 'no de-attribution ablation' corrected "
               "(skill-creator is that ablation, with mixed margins).", ["opus:O01", "opus:O02", "son55:E014"],
               "+7.5 (row now scored)"),
            RC(p, "E.holdout", "son55", rr(2), "See ratings.E.holdout (online oracle counts confirmed from p.56).",
               ["son55:E010", "opus:O03"], "+5 (row now scored)"),
            RC(p, "E.statistics", "son55", rr(1), "See ratings.E.statistics.", ["son55:E009", "son55:E016"],
               "+1.25 (row now scored)"),
            RC(p, "E.cost", "son55", rr(1), "See ratings.E.cost.", ["son55:E017"], "+1.25 (row now scored)"),
            res("status", *C(p, "status"), "son55", "reviewed",
                "Material ruling: the missing Appendix 12 bodies were read from the page images. They are implementation "
                "prompts that confirm §10.6–10.8 and carry no core-claim evidence. sol's request is satisfied by the "
                "page images, not by a new text package.", ["opus:O02", "opus:O03", "opus:O05"],
                "sol null → 63.75"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text, then the page images for Appendix G and Figures "
                                                   "5–6. In scope. The offline TB-Pro→TB2 transfer is the strongest "
                                                   "evidence; online gains are small with no variance; attribution "
                                                   "gating is mostly argued; there is no cost accounting. Expected about "
                                                   "G3 M3 X3 Em3 Ec2 Eh2 Es1 Ecost1.",
            "integrity_checks": "Both seats a1 on 2605.18401v2, text sha 913921e2…; canonical seat hashes equal "
                                "conflicts.json. sol completed no identification (needs_fulltext).",
            "core_claim_check": "Tables 1–4, Fig. 5 (backbone inferred from Table 1), Fig. 6, §8.2–8.3 protocol, §10.6–10.8 "
                                "and the Appendix G prompts were re-read.",
            "shared_error_review": "No shared rating (sol unscored). son55's E.causality reason corrected (skill-creator "
                                   "= de-attribution arm).",
            "rating_agreement": "All eight = son55 after re-check. Final 63.75.",
        },
    }

    # =========================================================== 2605.18729 Robo-Cortex (status conflict)
    p = "2605.18729"
    S[p] = {
        "base": "son55",
        "material_sections": [
            "arXiv v1 HTML has no appendix. 'Additional implementation details are provided in the supplementary "
            "material' (§4.1) refers to author-side material outside the arXiv record; per the SE-GPT precedent it is "
            "not part of the pinned document."],
        "opus_evidence": [
            opus_ev(p, "O01", "Additional implementation details are provided in the supplementary material.", "§4.1",
                    "The supplement is described as implementation detail only. No result in §4 refers to it."),
            opus_ev(p, "O02", "which rise from 38.89% SR and 30.96% SPL in round 1 to", "§4.3 Round-wise update dynamics",
                    "Fig. 4's 'on-split heuristics' round 1 (38.89/30.96) equals Table 3's 'w/ manual heur.' row, and "
                    "'from-scratch' round 1 (36.62, traj 50.7; opus:O03) equals 'w/ manual heur. + update'. The series "
                    "labels do not match the table rows.", kind="our_inference"),
            opus_ev(p, "O03", "w/ manual heur. + update 36.62 28.06 50.70", "Table 3",
                    "Table row matching Fig. 4's 'from-scratch' round-1 values (36.62% SR, trajectory 50.7)."),
            opus_ev(p, "O04", "increasing from 36.62% SR in round 1 to 51.39% in round 5, while shortening the trajectory "
                              "from 50.7 to 44.4", "§4.3 Round-wise update dynamics",
                    "Text values for the 'from-scratch' series."),
            opus_ev(p, "O05", "w/ seen heur. + update 41.67 31.69 49.50", "Table 3",
                    "A row named 'seen heur. + update' sits next to 'transferred heur. + update' (41.67/34.84). The text "
                    "describes transferred heuristics as those from the seen split, so the two labels are not "
                    "explained."),
            opus_ev(p, "O06", "Robo-Cortex++ 45.07 35.06 47.50", "Table 1",
                    "IGNav SR values imply different episode counts: MapGPT 17.36 = 25/144, WMNav 26.39 = 38/144, "
                    "World-In-World 38.57 = 54/140, Robo-Cortex 41.26 = 59/143, Robo-Cortex++ 45.07 = 64/142. Within "
                    "splits: Table 3 34.72 = 25/72 but 36.62 = 26/71; Table 2 36.11 = 26/72, 42.65 = 29/68, "
                    "44.29 = 31/70, and 40.18 is not k/n for any n ≤ 111. Episodes appear to be dropped from some runs "
                    "without explanation (EVIDENCE rule 3).", kind="our_inference"),
            opus_ev(p, "O07", "+ SRM 40.18 30.25 50.05", "Table 2 (round 1)",
                    "40.18% cannot be k/72 or k/71; see opus:O06.", kind="our_inference"),
            opus_ev(p, "O08", "Robo-Cortex consistently outperforms strong baselines in both task success and "
                              "exploration efficiency", "Abstract",
                    "Table 1 contradicts 'consistently': static AEQA SPL 21.40 is below WMNav 23.60 and MapGPT 22.40, "
                    "and IGNav trajectory 49.90 is longer than World-In-World's 47.10 (son55:E020/E021)."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus accepts son55. The central claim is generalisation to unseen environments by injecting "
                      "induced heuristics as conditioning into a frozen VLM, with on/off controls on the unseen split. "
                      "That is the parent move. C03 needs an upstream phase that teaches a format, which is absent, so "
                      "sub=null (r17b convention). heterogeneous_decomposition (the dual-grain split by time scale) was "
                      "considered as supporting and not added: the two grains are ablated, but the paper's claim rests "
                      "on transfer.",
            "matches": [smatch("son55", p, "adapt_via_conditioning", role="primary")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "reason": "Opus accepts son55. H00: reflect on success/failure trajectories into "
                                     "guiding/cautionary heuristics. H03: LPM retrieves prior subtasks by "
                                     "nearest-neighbour matching above δ_lpm.",
                           "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={
            "rsi:index_experience_for_reuse/F3": {
                "reason": "Unmet (the failure mode is present). The seen-split LPM gains come from repeated evaluation "
                          "of the same episodes, and Robo-Cortex++ updates online on test episodes. Opus confirms "
                          "son55's expectation status; son55's domain condition-check label "
                          "'challenged_with_evidence' is the same finding stated as a failure mode."}}),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O06", "opus:O08"]), "C3", ["opus:O02", "opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: Fig. 4 round-1 values coincide with differently labelled Table 3 rows (opus:O02, opus:O03).",
            "Opus: IGNav SR values imply per-run episode counts of 144/143/142/140 and 72/71/70/68, i.e. unexplained "
            "dropped episodes (opus:O06).",
            "Opus: the abstract's 'consistently outperforms' is contradicted on AEQA SPL and IGNav trajectory length "
            "(opus:O08)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus re-check = son55. 'Experiential amnesia' is a real limitation, but the "
                   "difference from text-side reflection/abstraction work is mainly the embodied multimodal setting. "
                   "Embodied neighbours (Voyager, EvoAgent, C-NAV, [17,33]) are compared only in prose.",
                   ["son55:E001"]),
            "M": R("resolved", 2, "Opus re-check = son55. The heuristic tuple, cluster-merge and high-confidence "
                   "feedback form a concrete mechanism, and the manual-heuristic control gives a partial causal "
                   "account. Why abstraction beats retrieval is asserted, and the confidence/merge choices are "
                   "unexplained.", ["son55:E003", "son55:E004", "son55:E010"], ["son55:E009"]),
            "X": R("resolved", 2, "Opus re-check = son55. This rating is robust to the missing supplement: it rests on "
                   "main-text design facts, namely no retention gate, expiry or rollback (consolidation is a heuristic "
                   "priority), an unstated build source for the static memory, and online rewriting that overwrites "
                   "the transferred prior (Table 3). Thresholds (w, k, δ_lpm, confidence cut-off) are deferred to the "
                   "supplement.", ["son55:E003", "son55:E004", "son55:E005", "son55:E016"], ["son55:E009"]),
            "E.measurement": R("resolved", 2, "Opus re-check = son55, with Opus additions. SR/SPL/Answer Score are "
                               "standard and follow World-In-World's protocol. But baseline provenance and backbone "
                               "parity are unstated. Fig. 4's series labels do not match the Table 3 rows their round-1 "
                               "values equal (opus:O02/O03/O05). The abstract's 'consistently' is contradicted by Table 1 "
                               "(opus:O08). This is the run's text–table cap of 2.",
                               ["son55:E011", "son55:E012", "opus:O02", "opus:O03"],
                               ["son55:E013", "opus:O05", "opus:O08"]),
            "E.causality": R("resolved", 2, "Opus re-check = son55. Basic / +SRM / +LPM / manual / transferred / "
                             "transferred+update on/off controls attribute gains to the memory components. The seen "
                             "split is replay of the same episodes. There is no retrieval-only or alternative-reflector "
                             "control, and no AKI-internal ablation.",
                             ["son55:E018", "son55:E019", "son55:E022", "son55:E024"], ["son55:E007"]),
            "E.holdout": R("resolved", 1, "Opus re-check = son55. 'Unseen' is the disjoint other half of the same "
                           "evaluation set, with no scene-overlap check. LPM gains come from repeated rounds on the same "
                           "split, the static system's memory source is unstated, and the real-robot test is not held "
                           "out.", ["son55:E006", "son55:E007"], ["son55:E002"]),
            "E.statistics": R("resolved", 1, "Opus re-check = son55 (A2 tier 1): single runs, no variance or seeds, "
                              "about 70 IGNav episodes per split, and negative results reported. Opus correction of "
                              "son55's E023 inference: SR values are not all multiples of 1/72. The denominators vary "
                              "across runs (opus:O06, opus:O07), so failures/drops are not accounted for in the "
                              "denominator.", ["son55:E009", "son55:E019", "opus:O06"], ["son55:E023"]),
            "E.cost": R("not_reported", 0, "Opus re-check = son55. No compute, latency, token or GPU-hour figures for a "
                        "72B VLM + 14B video world model + per-episode AKI, and no budget parity with baselines. The "
                        "author-referenced supplement is outside the arXiv record (material ruling). If the controller "
                        "obtains it and it reports cost, re-dispatch this item only.", [], [],
                        ["pinned arXiv v1 text §1–5 (no appendices in the arXiv record): cost/latency/GPU/token/compute "
                         "— none", "author-referenced supplementary material: outside the arXiv record, not supplied"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (§1–5, Tables 1–3, Fig. 4 values in text, real-world §4.4). The only "
                  "referenced missing material is author-side supplementary implementation detail outside the arXiv "
                  "record (SE-GPT precedent). It carries no core-claim evidence; only X and E.cost could depend on it, "
                  "and X rests on main-text design facts. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "material_ruling": "reviewed (not needs_fulltext). The external supplement is author-side implementation "
                           "detail and does not carry core-claim evidence (SE-GPT precedent). If obtained later, "
                           "re-dispatch only X/E.cost.",
        "a3_recommendation": "not required. Optional: re-dispatch only X/E.cost to both seats if the controller obtains "
                             "the author supplement.",
        "a3": "none (in scope; non-weight heuristic library).",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 1–5 are image-only and were not used. Fig. 4 numbers are taken from the §4.3 text.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "Heuristics induced on the seen half improve IGNav/AR on the disjoint unseen half (Table 3: SR "
                "34.72→48.61). Retained changes help later tasks. Holdout weaknesses are charged to E.holdout.",
                ["son55:E019", "son55:E006"], "none (label is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", "scoped",
                "Narrow support only: IGNav/AR transfer gains, no stable AEQA gain, online updating can hurt, and "
                "'consistently outperforms' is contradicted (opus:O08).", ["son55:E019", "son55:E009", "opus:O08"],
                "none (label is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "See rs_pattern.reason.", ["son55:E002", "son55:E019"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "Accepted (sub null; C03 upstream tuning absent).", ["son55:E010", "son55:E019"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"]],
                "Accepted (domain_pattern.reason).", ["son55:E003", "son55:E006"], NOSCORE),
            XC(p, "local:2605.18729-1", "son55", "unknown",
               "How the static Robo-Cortex's memory/heuristics were built before Table 1 testing is not stated in the "
               "pinned text. Unknown kept; it does not affect the score.", ["son55:E002"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "No contamination/overlap analysis between the seen and unseen halves or for the static build.",
               ["son55:E006", "son55:E002"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "There is a manual-heuristic control, but no nearest-neighbour or longer-context conditioning baseline.",
               ["son55:E010", "son55:E022"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial", "SRM/LPM ablated; AKI internals not.",
               ["son55:E019", "son55:E024"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "partial",
               "The fixed object named is scene/trajectory-level memory; the difference from prior experience work is "
               "argued, not shown.", ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Cluster-merge and consolidation exist; no forgetting threshold or growth curve.",
               ["son55:E003", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "No pre-retention validation; online updates can overwrite useful priors.", ["son55:E004", "son55:E009"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unmet", "See expectation override.", ["son55:E007"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "met",
               "Store-off controls exist (Basic vs +LPM; Basic vs heuristics). Their weaknesses are scored in "
               "E.causality=2.", ["son55:E018", "son55:E019", "son55:E024"]),
            RC(p, "G", "son55", rr(2), "See ratings.G. sol unknown = needs_fulltext deferral (overruled).",
               ["son55:E001"], "+7.5 (row now scored; sol null)"),
            RC(p, "M", "son55", rr(2), "See ratings.M.", ["son55:E003", "son55:E004"], "+10 (row now scored)"),
            RC(p, "X", "son55", rr(2), "See ratings.X (robust to the missing supplement).",
               ["son55:E004", "son55:E016"], "+10 (row now scored)"),
            RC(p, "E.measurement", "son55", rr(2), "See ratings.E.measurement (Opus label/claim inconsistencies "
               "added).", ["son55:E011", "opus:O02"], "+5 (row now scored)"),
            RC(p, "E.causality", "son55", rr(2), "See ratings.E.causality.", ["son55:E019", "son55:E022"],
               "+7.5 (row now scored)"),
            RC(p, "E.holdout", "son55", rr(1), "See ratings.E.holdout.", ["son55:E006", "son55:E007"],
               "+2.5 (row now scored)"),
            RC(p, "E.statistics", "son55", rr(1), "Rating kept; son55's 1/72 inference corrected (opus:O06).",
               ["son55:E009", "opus:O06"], "+1.25 (row now scored)"),
            RC(p, "E.cost", "son55", rr(0, "not_reported"), "See ratings.E.cost (search scope recorded; supplement "
               "caveat).", [], "0 (row now judged; coverage +0.05)"),
            res("status", *C(p, "status"), "son55", "reviewed",
                "Material ruling (SE-GPT precedent): an author-side external supplement of implementation details is "
                "not a gap in the pinned document unless it carries core-claim evidence, and it does not here. The "
                "ratings that could depend on it are X (robust; based on main-text facts) and E.cost "
                "(not_reported with scope).", ["opus:O01", "son55:E016"], "sol null → 43.75"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope. Table 3 transfer (seen→unseen half) is the strongest "
                                                   "evidence, but there is a single run, scene overlap is unchecked, "
                                                   "the static-memory source is unstated, and there is no cost. "
                                                   "Expected about G2 M2 X2 Em2 Ec2 Eh1 Es1 Ecost0.",
            "integrity_checks": "Both seats a1 on 2605.18729v1, text sha 52760128…; canonical seat hashes equal "
                                "conflicts.json. son55's seat file shows 'M' in git status, but its canonical hash "
                                "matches conflicts.json (the working copy is the bound version).",
            "core_claim_check": "Tables 1–3, the §4.3 Fig. 4 numbers, the abstract claims and the real-world §4.4 were "
                                "re-read; SR denominators were recomputed.",
            "shared_error_review": "No shared rating (sol unscored). son55's E023 inference (all SR multiples of 1/72) "
                                   "is wrong; corrected in the E.statistics reason.",
            "rating_agreement": "All eight = son55 after re-check. Final 43.75.",
        },
    }

    # =========================================================== 2605.19576 Library Drift (Δ15)
    p = "2605.19576"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "A1 has 42 active because the pipeline still synthesises skills, they are just never "
                              "injected", "Table 1 caption (A1 row: Active 42, Retired 15, Critic 0)",
                    "With 0 critic calls and no injection, 42 skills were synthesised and 15 retired. Synthesis is "
                    "defined over critic-verdict clusters (opus:O02), and retirement needs n(s) ≥ N_min injected "
                    "trials (opus:O03); the cap (50) was not reached. The A1 row is inconsistent with the stated "
                    "mechanism.", kind="our_inference"),
            opus_ev(p, "O02", "The critic produces 0 calls because no skill-attributed failures exist to judge.",
                    "§3.3 A1", "Paired with §4.2: verdict clusters are the synthesis substrate."),
            opus_ev(p, "O03", "trials have accumulated and the empirical contribution", "§5.1",
                    "Retirement requires n(s) ≥ N_min trials (100 by default); a never-injected skill has n(s)=0."),
            opus_ev(p, "O04", "followed by an LLM gate", "Appendix A Router",
                    "Every routed task makes an LLM gate call. The §6.4 tally of 14.5k = 10k solver + 4.3k critic + 152 "
                    "synthesis (opus:O05) omits these router-gate calls.", kind="our_inference"),
            opus_ev(p, "O05", "14.5k LLM calls per 100 rounds (10k solver + 4.3k critic + 152 synthesis), 43% more "
                              "than the no-skill baseline (A1, 10k calls)", "§6.4",
                    "Cost tally used by both seats; router-gate calls are not itemised."),
            opus_ev(p, "O06", "The bottleneck in self-evolving skill libraries is not the author; it is the librarian.",
                    "§8 Conclusion",
                    "This framing is contradicted by the paper's own A3: removing the authoring prior costs 43% of the "
                    "gain and is 'the single most valuable component' (opus:O07). Meanwhile retirement/cap are never "
                    "removed, so the librarian's role is not isolated.", kind="our_inference"),
            opus_ev(p, "O07", "it is the single most valuable component", "§5.3",
                    "The authoring prior (meta-skill) is the largest measured component."),
        ],
        "rs_pattern": {
            "primary": "assumption_audit_and_pivot", "supporting": ["controlled_diagnostic_design"],
            "outside_taxonomy": False,
            "reason": "Revised. The paper names the load-bearing implicit assumption of Voyager-style libraries "
                      "('compounding': each deposited skill helps) and pivots the budgeted retention rule. Append-only "
                      "becomes outcome-driven retirement with an evidence floor and a hard cap, plus a re-derived "
                      "certificate (Prop. 1). That is C11's object (which elements stay in a budgeted selection) and "
                      "its documented failure shape: a guarantee that does not hold up (contribution ≠ treatment "
                      "effect; vacuous floor E[p0]−0.35) and no 'revert the pivot' arm (no retirement-off / uncapped "
                      "control). son55 picked the right parent but left sub=null; sol's controlled_diagnostic_design/C02 "
                      "is kept as supporting for the trace-diagnostics and null-injection contribution. C02 fit is "
                      "partial because no controlled instance set is built. sol's supporting adapt_via_conditioning is "
                      "not kept: conditioning a frozen solver on stored skills is the shared substrate, not this paper's "
                      "move.",
            "matches": [
                smatch("son55", p, "assumption_audit_and_pivot", sub_id="C11", role="primary", fit="partial",
                       reason="Opus final: the budgeted-retention rule (which skills stay) is pivoted from append-only "
                              "to outcome-driven retirement + cap with a Hoeffding certificate (C11). Execution "
                              "partial: the pivot is never reverted, and the certificate equates success-minus-failure "
                              "with a treatment effect."),
                smatch("sol", p, "controlled_diagnostic_design", role="supporting",
                       reason="Opus: kept as supporting. A null-injection control (A1) and trace diagnostics that "
                              "decompose a conflated end-task metric. No constructed instance set, and no "
                              "accumulation-isolating intervention."),
            ],
            "executes_pattern": "partial", "resolves_problem": "scoped",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "evidence_gated_retention", "H30"),
                                       dmatch("sol", p, "diagnose_self_improvement", "H32"),
                                       dmatch("son55", p, "evidence_gated_retention", "H31")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "reason": "Union. H30: authoring prior + retirement + hard cap is the card's S2 profile. "
                                     "H32: null-injection and governance perturbations. H31 (son55): the N_min "
                                     "evidence floor with a stated Hoeffding non-divergence bound is a statistical "
                                     "commit/retire rule, though its certificate is invalid. Fit partial.",
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [
            {"rs_main": "assumption_audit_and_pivot", "rs_sub": "C11",
             "domain": {"namespace": "rsi", "main": "evidence_gated_retention", "sub": "H30"},
             "operation_correspondence": "C11's pivot of a budgeted keep/evict rule corresponds to H30's governed "
                                         "admission/retirement with a hard size bound.",
             "necessary_conditions": "Per-entry credit that measures marginal effect; a revert-the-pivot control "
                                     "(retirement-off / uncapped).",
             "differences": "Eq. 2 is success-minus-failure among injected tasks, not a contrast with no skill. Neither "
                            "control is run, so the certificate and the 'load-bearing' claim are not bound to the pivot.",
             "evidence_ids": ["sol:E005", "sol:E007", "sol:E008", "sol:E017", "son55:E022"]},
            {"rs_main": "controlled_diagnostic_design", "rs_sub": "C02",
             "domain": {"namespace": "rsi", "main": "diagnose_self_improvement", "sub": "H32"},
             "operation_correspondence": "Disable retained-skill injection (A1) or perturb governance (A4–A8) and read "
                                         "frozen-solver outcomes and bank traces.",
             "necessary_conditions": "One-axis interventions with an independent anchor (executable MBPP+ tests).",
             "differences": "A4 changes two knobs, and no intervention varies unbounded accumulation (the named driver).",
             "evidence_ids": ["sol:E003", "sol:E004", "sol:E013", "son55:E005"]},
        ],
        "expectations": with_extra(lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.19576-1"): "local:2605.19576-3",
                    ("son55", "rs:assumption_audit_and_pivot/RE-1"): "rs:assumption_audit_and_pivot/RE-6"},
            overrides={
                "local:2605.19576-3": renum("son55 local:2605.19576-1",
                                            "task filtering by the same model and regression to the mean (A1 controls "
                                            "it)."),
                "rs:assumption_audit_and_pivot/RE-6": {
                    "note": "Renumbered from son55 'RE-1'. Its content ('establish failure cases of prior approaches "
                            "before the positive result') is the card's 6th reviewer expectation; RE-1 is the "
                            "tightness/lower-bound expectation (added by Opus below).",
                    "reason": "Unmet. The prior approaches' failure (ungoverned accumulation degrading performance) is "
                              "asserted from SkillsBench and never reproduced in the paper's own setting."},
                "rs:adapt_via_conditioning/RE-2": dropped_card("adapt_via_conditioning"),
                "rsi:evidence_gated_retention/S1": {
                    "status": "unmet",
                    "reason": "Opus = sol. S1 asks for a counterfactual behind every credit. Eq. 2 is "
                              "success-minus-failure on injected tasks with no no-skill contrast. A1 is a system-level "
                              "store-off, not a per-entry credit."},
                "rsi:diagnose_self_improvement/S3": {
                    "status": "partial",
                    "reason": "Opus revision of son55's 'unknown'. The known parts settle the status: there is a 60/40 "
                              "split, the scorer is frozen (MBPP+ tests), and leakage is not tested. The open question "
                              "(whether the curator's evidence log includes eval capsules) stays recorded and is "
                              "scored in E.holdout=1."},
            }), [
            {"id": "rs:assumption_audit_and_pivot/RE-1", "version": "card", "source_strength": "observed_in_reviews",
             "source_refs": ["ideation-patterns/assumption_audit_and_pivot.md Reviewer expectations #1"],
             "applies_when": "A guarantee is offered for the pivoted rule", "applicable": True, "status": "unmet",
             "reason": "Opus-added (literal RE-1). Prop. 1 has no tightness or matching bound. With p0 ≈ 0.258 the floor "
                       "E[p0]−0.35 is negative, so the bound is vacuous at the paper's own scale (authors call it "
                       "'loose').",
             "evidence_ids": ["sol:E018", "son55:E011"], "score_item": "M", "origin": "opus"}]),
        "claims": lambda c: add_counter(add_counter(add_counter(c, "C1", ["opus:O04", "son55:E029"]),
                                                    "C2", ["opus:O06", "opus:O07"]), "C4", ["opus:O01"]),
        "assessment": assess("sol", p, [
            "Opus: Table 1's A1 row (42 synthesised / 15 retired with 0 critic calls and 0 injections) is inconsistent "
            "with the stated synthesis and retirement rules (opus:O01–O03).",
            "Opus: the 14.5k-call tally omits per-task LLM router-gate calls (opus:O04).",
            "Opus: the authoring prior, not the librarian, is the largest measured component, contrary to the "
            "conclusion's framing (opus:O06, opus:O07)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus = sol. Lifecycle governance is a real, sourced concern (survey, SkillsBench), and "
                   "neighbours are named with specific differences. But the gap premise (unbounded accumulation causes "
                   "drift) is not demonstrated in the paper's own setting: A1 is injection-off and A4 is over-governance. "
                   "The cited symptom (LLM-authored skills +0.0pp) is an authoring finding, and the paper's own A3 makes "
                   "authoring the largest component (opus:O06/O07). The problem position is therefore partly "
                   "contradicted by its own evidence.",
                   ["sol:E001", "sol:E002", "son55:E032"], ["sol:E003", "sol:E004", "opus:O06", "opus:O07"]),
            "M": R("resolved", 2, "Both seats 2, confirmed. The feedback → synthesis → retirement/cap mechanism is "
                   "concrete. But Eq. 2 is not a treatment effect relative to p0, harder-task skills are retired by "
                   "construction, and Prop. 1's proof equates the two.",
                   ["sol:E005", "sol:E007", "sol:E008", "son55:E009"], ["sol:E017", "son55:E010"]),
            "X": R("resolved", 2, "Opus = sol. Router, synthesis trigger, retirement floor, cap and hyperparameters are "
                   "given, and code is linked. Key retention conditions are unclear or contradictory. Rollback appears "
                   "only in the hyperparameter table, with no trigger data or semantics (son55:E030). Whether the "
                   "curator's evidence log excludes eval capsules is unstated (sol:E016). Table 1's A1 row contradicts "
                   "the synthesis/retirement rules (opus:O01–O03).",
                   ["sol:E006", "sol:E007", "sol:E008", "sol:E016"], ["son55:E030", "opus:O01"]),
            "E.measurement": R("resolved", 2, "Opus = sol. MBPP+ pass@1 with executable tests is credible, and the "
                               "single-call solver isolates the library. But the diagnostic metrics the paper offers as "
                               "a contribution are unvalidated: Eq. 2 is labelled 'contribution' but measures conditional "
                               "success, and the early-warning claim rests on one case (A4). The A1 table row is "
                               "internally inconsistent (opus:O01). This is the run's cap of 2 for table–mechanism "
                               "contradictions.",
                               ["sol:E005", "sol:E010", "sol:E011", "son55:E014"], ["opus:O01", "son55:E031"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. A1 (same pipeline, injection off) is a strong "
                             "store-off control, and A2/A3 attribute the gate and the meta-skill. There is no "
                             "retirement-off or uncapped arm, so 'retirement and cap are load-bearing' is untested; A7 "
                             "doubles the cap and keeps the mean. A4 changes two knobs, and there is no external "
                             "ungoverned baseline.",
                             ["sol:E003", "sol:E013", "son55:E018", "son55:E021"],
                             ["sol:E004", "son55:E020", "son55:E022"]),
            "E.holdout": R("resolved", 1, "Opus = sol. The 60/40 split is stated and skill content comes from train "
                           "failures, but the method's selection step may read the evaluation set. The router injects on "
                           "the 40 eval tasks every round (Appendix A Eval phase), Eq. 2 is computed from 'capsules where "
                           "s was injected' with no train-only restriction, and the undocumented rollback likely "
                           "monitors the same score. The same 40 tasks are reused across 100 rounds, all 9 conditions "
                           "and empirically chosen thresholds. Tasks are filtered by the same model, contamination is "
                           "not checked, and there is one benchmark. The paper's 'held-out' label is thus not "
                           "protected.",
                           ["sol:E010", "sol:E016", "son55:E013", "son55:E028"], ["son55:E029", "son55:E030"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2): 3 seeds with std and a per-seed "
                              "table, and negative results. No CI or test, n=40 eval tasks.",
                              ["sol:E019", "son55:E006", "son55:E015"]),
            "E.cost": R("resolved", 2, "Opus = sol. Calls and wall time are disclosed (Default vs A1, A8 10.1 h). But "
                        "the 14.5k tally omits per-task LLM router-gate calls (opus:O04/O05), there is no token/dollar "
                        "accounting, and no budget-matched alternative.",
                        ["sol:E014", "son55:E024", "son55:E025", "opus:O05"], ["opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text read (§1–8, Appendices A–D). In scope (a non-weight skill bank governed by "
                  "execution outcomes). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "material_ruling": "n/a (both seats reviewed the complete text).",
        "a3": "none (in scope; both seats agree).",
        "improver_check": "not claimed; the meta-skill refresh (A8) is a fixed schedule, not an evaluated improver edit.",
        "figure_dependence": "Figures 1–2 are image-only and were not used. All values come from Tables 1–3 and the text.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "assumption_audit_and_pivot",
                "See rs_pattern.reason (C11 sub added by Opus).", ["son55:E001", "sol:E017", "son55:E022"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["assumption_audit_and_pivot", "C11"], ["controlled_diagnostic_design", "C02"]],
                "son55's parent with Opus's C11 sub, plus sol's C02 as supporting. sol's adapt_via_conditioning/C03 is "
                "not kept (generic substrate).", ["son55:E001", "sol:E003", "sol:E017"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["diagnose_self_improvement", "H32"], ["evidence_gated_retention", "H30"],
                 ["evidence_gated_retention", "H31"]],
                "Union; H31 added from son55 (domain_pattern.reason).", ["sol:E007", "sol:E018", "son55:E011"], NOSCORE),
            res("expectations[local:2605.19576-1].status", *C(p, "expectations[local:2605.19576-1].status"), "revised",
                {"local:2605.19576-1": "unmet", "local:2605.19576-3": "partial"},
                "A4 ID collision: sol's -1 is the Prop. 1 guarantee check (unmet, confirmed: the conditional outcome "
                "does not bound the change from p0, and the bound is vacuous). son55's -1 is a different question "
                "(task filtering / regression to the mean) and is renumbered -3 with status partial (A1's flat line "
                "controls it).", ["sol:E017", "sol:E018", "son55:E012", "son55:E004"], NOEXP),
            XC(p, "local:2605.19576-2", "sol", "partial", "sol-only statistics question; verified (3 seeds, no CI/test).",
               ["sol:E019"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
               "Card not retained; kept as a check question (60/40 split documented, no overlap audit).",
               ["sol:E010", "sol:E016"]),
            res("expectations[rs:assumption_audit_and_pivot/RE-1].status",
                *C(p, "expectations[rs:assumption_audit_and_pivot/RE-1].status"), "revised",
                {"rs:assumption_audit_and_pivot/RE-1": "unmet", "rs:assumption_audit_and_pivot/RE-6": "unmet"},
                "son55's 'RE-1' quoted the card's 6th expectation (establish failure cases first) and is renumbered "
                "RE-6, unmet. Opus also evaluated the literal RE-1 (tightness/matching bound): unmet, since the "
                "Prop. 1 floor is vacuous at p0 ≈ 0.258.", ["son55:E002", "son55:E003", "sol:E018"], NOEXP),
            XC(p, "rs:controlled_diagnostic_design/RE-1", "sol", "partial",
               "Kept (C02 supporting). Injection-off isolates uptake; accumulation is never varied.", ["sol:E003", "sol:E004"]),
            XC(p, "rs:controlled_diagnostic_design/RE-2", "sol", "unmet", "One model, one benchmark.", ["sol:E015"]),
            XC(p, "rs:controlled_diagnostic_design/RE-3", "sol", "partial", "Null baseline present; compute not matched.",
               ["sol:E003", "sol:E014"]),
            XC(p, "rsi:diagnose_self_improvement/S1", "son55", "partial", "A1 is a targeted cut; A4 changes two knobs.",
               ["son55:E004", "son55:E005"]),
            XC(p, "rsi:diagnose_self_improvement/S3", "revised", "partial",
               "See expectation override (known facts settle partial; the open provenance question is scored in "
               "E.holdout).", ["son55:E013", "son55:E029", "sol:E016"]),
            XC(p, "rsi:diagnose_self_improvement/S4", "son55", "met", "A4 and A5/A6 are reported as findings.",
               ["son55:E005", "son55:E033"]),
            XC(p, "rsi:evidence_gated_retention/H30", "sol", "partial",
               "Retirement and cap are described; no quarantine, regression replay or train-only promotion data.",
               ["sol:E007", "sol:E008", "sol:E016"]),
            XC(p, "rsi:evidence_gated_retention/S1", "sol", "unmet", "See expectation override.", ["sol:E005", "son55:E009"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "met",
               "Authoring prior + conservative retirement + hard cap are all present (the S2 profile). Their "
               "effectiveness is a separate question (S3/S4).", ["son55:E007", "son55:E008", "son55:E018"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "partial", "A4/A7 vary knobs; no retirement-off/cap-off.",
               ["son55:E020", "son55:E022"]),
            RC(p, "G", "sol", rr(2), "See ratings.G; Opus adds that the paper's own A3 contradicts its framing.",
               ["sol:E001", "opus:O06", "opus:O07"], "−3.75 vs son55"),
            RC(p, "X", "sol", rr(2), "See ratings.X; son55's 3 does not weigh the rollback/provenance gaps it lists or "
               "the A1 contradiction (opus:O01).", ["sol:E016", "son55:E030", "opus:O01"], "−5 vs son55"),
            RC(p, "E.measurement", "sol", rr(2), "See ratings.E.measurement. son55's 3 credits pass@1 but not the "
               "unvalidated diagnostic metrics or the inconsistent A1 row.", ["sol:E005", "opus:O01"], "−2.5 vs son55"),
            RC(p, "E.holdout", "sol", rr(1), "See ratings.E.holdout. son55 lists the same concerns (eval reuse, "
               "unknown capsule provenance, thresholds, contamination). Together they put the core selection step on "
               "the eval set, which places the rating below the anchor-2 'relevant results with gaps' level.",
               ["sol:E016", "son55:E029", "son55:E028"], "−2.5 vs son55"),
            RC(p, "E.cost", "sol", rr(2), "See ratings.E.cost (router-gate calls missing from the tally).",
               ["sol:E014", "opus:O04"], "−1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings (X, E.measurement) — both seats' evidence",
             "error": "Neither seat noticed that Table 1's A1 row (42 synthesised / 15 retired, 0 critic calls, 0 "
                      "injections) contradicts the stated synthesis (critic-verdict clusters) and retirement "
                      "(n(s) ≥ N_min) rules.",
             "correction": "Recorded as counterevidence for X and E.measurement (both final 2).",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none beyond the sol-side ratings"},
            {"field_path": "ratings.E.cost — both seats' reason",
             "error": "Both seats took the 14.5k-call tally as the full overhead; it omits per-task LLM router-gate calls.",
             "correction": "Added to E.cost (final 2).", "evidence_ids": ["opus:O04", "opus:O05"],
             "score_impact": "none beyond the sol-side rating"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope; a strong A1 store-off control. The drift mechanism "
                                                   "(accumulation) is never reproduced, retirement/cap are never "
                                                   "removed, Eq. 2 is not a contribution, Prop. 1 is vacuous, eval "
                                                   "capsule provenance is unclear, and the A1 row is inconsistent. "
                                                   "Expected about G2 M2 X2 Em2 Ec2 Eh1 Es2 Ecost2.",
            "integrity_checks": "Both seats a1 on 2605.19576v3, text sha f8039e8c…; canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Table 1, §3.3, §5.1–5.3, §6.1–6.4, Appendices A–D re-read; A1 row cross-checked "
                                "against the mechanism.",
            "shared_error_review": "Two shared omissions recorded (A1 row; router-gate calls).",
            "rating_agreement": "Five disputed items → sol; three shared items confirmed. Final 47.5.",
        },
    }

    # =========================================================== 2605.21240 APEX (Δ10)
    p = "2605.21240"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "the skipped milestone is added to a per-episode completed set, excluding it from Policy "
                              "Selection for the remainder of the episode", "Appendix C Milestone Completion and Auto-Skip",
                    "If this 'completed set' is the achieved state s, dependents of a skipped (failed) milestone become "
                    "eligible. That contradicts §4.1's 'failed milestones never satisfy their dependents’ "
                    "prerequisites' (opus:O02). No separate exclusion set is described.", kind="our_inference"),
            opus_ev(p, "O02", "failed milestones never satisfy their dependents’ prerequisites", "§4.1",
                    "The robustness property the DAG design is justified by."),
            opus_ev(p, "O03", "including fact-grounded additions, attribute updates such as refined key actions, and "
                              "deduplication pruning", "§4.2 Map Refinement",
                    "Map Refinement can still add nodes after Fork Discovery is frozen (episode 30, opus:O04). Map "
                    "growth is bounded only by prompt rules, and there is no gate on additions.", kind="our_inference"),
            opus_ev(p, "O04", "Episode at which Fork Discovery is disabled", "Table 10 (Exploration freeze = 30)",
                    "Expansion schedule constant."),
            opus_ev(p, "O05", "APEX achieves the best Final-3 score and leads on all five categories", "§5.2 WebArena Results",
                    "The text cites 'Table 3' for the main WebArena result, which is Table 2. Other cross-references "
                    "are similarly shifted (DAG vs flat cited as Table 5 is Table 4; policy selection cited as Table 7 "
                    "is Table 6). These are reporting errors, not numeric contradictions.", kind="our_inference"),
            opus_ev(p, "O06", "tuned to match the reward scale of the games", "Appendix C UCB",
                    "c=10 was tuned on the evaluation games; UCB is only an ablation arm (Thompson is the default)."),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats' primary (sub null: C00/C21/C27 checked, none fit). sol's supporting "
                      "adapt_via_conditioning is not kept: map/lesson injection into a frozen model is the shared "
                      "substrate, while the paper's move is the milestone-DAG bandit reframe plus frontier expansion.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object", role="primary")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H04"),
                                       dmatch("son55", p, "evidence_gated_retention", "H29")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "reason": "Union (son55). H01 (living map with add/update/prune edits), H04 (DAG-structured "
                                     "substrate). H29 (son55) is kept because the card names 'bandit statistics' "
                                     "learned from outcomes that then drive ranking. In APEX they drive selection, not "
                                     "admission, so fit is partial.",
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.21240-1"): "local:2605.21240-4",
                    ("son55", "local:2605.21240-2"): "local:2605.21240-5"},
            overrides={
                "local:2605.21240-4": renum("son55 local:2605.21240-1",
                                            "hyperparameters (c, N, freeze point) chosen on the evaluation games."),
                "local:2605.21240-5": renum("son55 local:2605.21240-2",
                                            "exploration-collapse avoidance measured on the main benchmarks."),
                "local:2605.21240-1": {
                    "reason": "Opus = sol (unmet as documented). Appendix C adds skipped milestones to a 'completed set' "
                              "(opus:O01), against §4.1's actual-success eligibility (opus:O02). Unless a separate set "
                              "exists, which the paper does not describe, failed prerequisites count as completed."},
                "rs:reframe_as_solvable_object/RE-1": {
                    "status": "unmet",
                    "reason": "Opus = son55. RE-1 asks for a proof of the reduction or correspondence. None is given; "
                              "the formal object definition is credited under RE-2 (met)."},
                "rs:adapt_via_conditioning/RE-2": dropped_card("adapt_via_conditioning"),
                "rs:adapt_via_conditioning/RE-4": dropped_card("adapt_via_conditioning"),
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "partial",
                    "reason": "Opus = son55. There are local edits, dedup and a lesson cap of 20, but Map Refinement can "
                              "keep adding nodes after the Fork freeze (opus:O03), and pruned nodes' statistics are "
                              "discarded. The store is not demonstrably bounded."},
                "rsi:index_experience_for_reuse/F3": {
                    "reason": "Unmet (failure mode present by design for Tables 1–2: the store is built from the test "
                              "stream). Table 3's cross-task view partly answers it."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01", "opus:O03"]), "C1", ["opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: skip bookkeeping (Appendix C) contradicts §4.1's prerequisite semantics unless the sets are separate "
            "(opus:O01).",
            "Opus: Map Refinement can add nodes after the Fork freeze; growth is unbounded by any gate (opus:O03)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus = son55. Exploration collapse is a concrete bottleneck with a same-backbone "
                   "diagnostic (maze; average vs maximum in three games), and the nearest memory/reflection/evolution "
                   "systems (Reflexion, EvoTest, ACE) are run as baselines; the fixed-action-space exploration lineage "
                   "is distinguished. Not 4: ReasoningBank/JitRL are distinguished only in prose, collapse is not "
                   "quantified on the main benchmarks, and archive-based exploration lineages are not discussed "
                   "(our_inference).",
                   ["son55:E001", "son55:E003", "son55:E004", "sol:E003"], ["son55:E035"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Map + prerequisites + bandit selection target the stated "
                   "failure, and the DAG/flat, FD/no-FD and credit-scheme predictions are distinguishable. Self-reported "
                   "completion, LLM-attributed rewards and a non-stationary bandit are unargued.",
                   ["son55:E005", "son55:E006", "sol:E004", "sol:E008"], ["son55:E010", "sol:E023"]),
            "X": R("resolved", 2, "Opus = sol. Algorithm, hyperparameters, prompts, dedup and freeze are reconstructable. "
                   "But the key condition behind the DAG design, eligibility only after actual achievement, is "
                   "contradicted by Appendix C's skip bookkeeping unless an undescribed separate set exists "
                   "(opus:O01/O02), and achievement is self-reported. LLM-proposed nodes face no admission gate, "
                   "version or rollback, and Map Refinement can still add nodes after the freeze (opus:O03). Key "
                   "conditions remain unclear (anchor 2).",
                   ["sol:E006", "sol:E010", "sol:E021", "sol:E028", "son55:E011"],
                   ["opus:O01", "opus:O02", "opus:O03", "son55:E010"]),
            "E.measurement": R("resolved", 3, "Both seats 3, confirmed. Game score and the WebArena evaluator are "
                               "standard, all methods share a backbone, and Static is a trivial baseline. Table "
                               "cross-reference errors (opus:O05) are reporting slips. The 70.2 vs 73.0 same-config "
                               "inconsistency is charged to E.statistics (A2 single-defect rule).",
                               ["son55:E012", "son55:E014", "sol:E011", "sol:E013"], ["opus:O05"]),
            "E.causality": R("resolved", 3, "Both seats 3, confirmed. Five same-backbone baselines with equal "
                             "episodes/steps, plus single-variable DAG/FD/selection/credit ablations with large gaps on "
                             "Pentari/Ztuu. Limits: 3/9 games, single runs, lessons and stuck-diagnosis never ablated, "
                             "and no 'no map, keep lessons' arm.",
                             ["sol:E012", "sol:E015", "sol:E016", "sol:E017"], ["sol:E022", "son55:E030", "son55:E031"]),
            "E.holdout": R("resolved", 2, "Both seats 2, confirmed. The online claim is evaluated on later episodes of "
                           "the same environment (F3 by design). The WebArena cross-task table is a partial held-out "
                           "view with an unclear protocol. c was tuned on the evaluation games (opus:O06), and the N "
                           "sweep was run on them.", ["sol:E014", "sol:E024", "son55:E032"], ["opus:O06"]),
            "E.statistics": R("resolved", 1, "Both seats 1, confirmed (A2 tier 1). A single run per configuration; "
                              "std is over the final K episodes. The default config gives Zork1 73.0 in Tables 1/4–6/8 "
                              "and 70.2 in Table 7, showing at least 2.8 points of unreported run-to-run variance.",
                              ["sol:E025", "son55:E013", "son55:E018", "son55:E039"]),
            "E.cost": R("resolved", 3, "Opus = son55. Interaction budgets are matched (50 episodes × 120 steps; 5 per "
                        "WebArena task), and actual WebArena API dollars are reported for all six methods (APEX 318 vs "
                        "278–324). Not 4: no Jericho or ablation/tuning cost.",
                        ["sol:E018", "sol:E019", "son55:E028"], ["son55:E027"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (§1–6, Appendices A–E with prompts and std tables). In scope (persistent "
                  "strategy map and lesson buffer). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "material_ruling": "n/a (both seats reviewed the complete text).",
        "a3": "none (in scope; both seats agree).",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 1–2 (collapse diagnostic) and 4–6 (curves, Fork case maps) are image-only. Only "
                             "text statements (e.g. Pentari 28→43, Deephome 33→71) are used; no plotted values.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["reframe_as_solvable_object", None]],
                "Primary agreed; sol's supporting C03 is dropped (rs_pattern.reason).", ["son55:E005", "sol:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H01"], ["evidence_gated_retention", "H29"],
                 ["index_experience_for_reuse", "H04"]],
                "Union; H29 added from son55 (domain_pattern.reason).", ["son55:E006", "sol:E008"], NOSCORE),
            res("expectations[local:2605.21240-1].status", *C(p, "expectations[local:2605.21240-1].status"), "revised",
                {"local:2605.21240-1": "unmet", "local:2605.21240-4": "unknown"},
                "A4 ID collision. sol's -1 (skip bookkeeping vs prerequisites) is unmet, confirmed (opus:O01). son55's "
                "-1 (hyperparameters chosen on the evaluation games) is renumbered -4 and kept unknown: c is 'tuned to "
                "match the reward scale' (opus:O06), but the tuning data is not stated. son55's -2 was likewise "
                "renumbered -5 (see shared_error_corrections).", ["sol:E020", "opus:O01", "son55:E032"], NOEXP),
            XC(p, "local:2605.21240-3", "sol", "partial", "WebArena dollars only; verified.", ["sol:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial", "Card not retained; kept as a check question.",
               ["sol:E014", "sol:E024"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "sol", "partial", "Card not retained; kept as a check question "
               "(lessons/diagnosis not isolated).", ["sol:E022"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "son55", "unmet", "See expectation override.",
               ["son55:E005", "son55:E006"]),
            XC(p, "rs:reframe_as_solvable_object/RE-2", "sol", "met", "Milestone abstract MDP formally defined.",
               ["sol:E004", "sol:E005"]),
            XC(p, "rs:reframe_as_solvable_object/RE-3", "son55", "partial",
               "The new structure lives in the DAG/Fork Discovery; the bandit is standard.", ["son55:E008", "son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "met",
               "The implicit, unbounded strategy space is made explicit and learnable.", ["son55:E001", "son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial", "See expectation override.",
               ["son55:E011", "opus:O03"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "partial", "Outcome statistics without per-entry "
               "counterfactual.", ["son55:E006"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "partial", "Selector/credit swappable and ablated; no "
               "value-off arm.", ["son55:E021", "son55:E037"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unmet", "See expectation override.", ["son55:E012"]),
            XC(p, "rsi:index_experience_for_reuse/H04", "sol", "partial", "Local periodic edits and a flat baseline; no "
               "growth stress test.", ["sol:E006", "sol:E015"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "sol", "unmet", "No external per-edit admission check.",
               ["sol:E028", "sol:E029"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "Static/Memory and structure ablations; no 'map off, lessons on' arm.", ["son55:E016", "son55:E031"]),
            RC(p, "G", "son55", rr(3), "See ratings.G. sol's 2 rested on the lack of independent lineage verification, "
               "which the seats cannot do. The in-paper positioning and baseline coverage support 3.",
               ["son55:E003", "son55:E004"], "+3.75 vs sol"),
            RC(p, "X", "sol", rr(2), "See ratings.X. son55 listed the missing gate/rollback but not the "
               "skip-vs-prerequisite contradiction.", ["opus:O01", "opus:O02", "sol:E020"], "−5 vs son55"),
            RC(p, "E.cost", "son55", rr(3), "See ratings.E.cost. sol's 2 asked for a cost-matched sweep, but "
               "interaction budgets already match and API dollars are near-equal.", ["sol:E018", "son55:E028"],
               "+1.25 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations local:2605.21240-2",
             "error": "A4 hidden ID collision: both seats used local:2605.21240-2 (both 'partial') for different "
                      "questions (sol: statistics; son55: collapse measured on the main benchmarks). It was not flagged "
                      "by conflicts.json because the statuses matched.",
             "correction": "son55's question renumbered local:2605.21240-5; statuses unchanged.",
             "evidence_ids": ["sol:E025", "son55:E003"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope. Strong same-backbone baselines and targeted ablations, but "
                                                   "single runs (70.2 vs 73.0), unablated lessons/diagnosis, "
                                                   "skip-bookkeeping ambiguity, and tuning on evaluation games. "
                                                   "WebArena cost is reported. Expected about G3 M3 X2–3 Em3 Ec3 Eh2 "
                                                   "Es1 Ecost3.",
            "integrity_checks": "Both seats a1 on 2605.21240v1, text sha ec9508e6…; canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Tables 1–13, §4.1–4.4, Appendix C re-read; same-config values cross-checked.",
            "shared_error_review": "One shared ID collision (local -2) fixed; no shared rating error.",
            "rating_agreement": "G/E.cost → son55, X → sol; five shared items confirmed. Final 65.0.",
        },
    }

    # =========================================================== 2605.21810 Trace2Skill (Δ1.25)
    p = "2605.21810"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "Four-configuration ablation on the 8 hard tasks with zero CVDP baseline agent passes.",
                    "Table 1 caption",
                    "The 8 tasks were chosen because the seed agent had zero passes. §3.2 says 96 baseline rollouts were "
                    "completed (24 tasks × 4), and C1 uses 4 per task. C1's 0/32 is therefore very likely the same "
                    "rollouts that selected the tasks, i.e. zero by construction. Any re-run (C2–C4) benefits from "
                    "regression to the mean.", kind="our_inference"),
            opus_ev(p, "O02", "Unified outcome metrics: pass rate over attempted rollouts, tasks solved/8, and "
                              "AgentProgressQ.", "Table 1",
                    "'Solved/8' is ≥1 pass among a configuration's rollouts: 80 per task for C3/C4 (Fig. 4: 'over five "
                    "generations × four candidate skills × four repeats') vs 4 for C1/C2. The headline 6/8 vs 0/8 "
                    "compares pass@80 (with oracle-selected parents) to pass@4.", kind="our_inference"),
            opus_ev(p, "O03", "Rather than training a new model or only sampling more candidate solutions",
                    "Abstract",
                    "The paper positions itself against 'only sampling more'. No equal-budget repeated-sampling arm (C1 "
                    "with 80 rollouts per task) is reported, so this distinction is untested."),
            opus_ev(p, "O04", "prior shared-skill tests suggested weak transfer across heterogeneous tasks",
                    "§4.2", "The reason for evaluating on the selection tasks is cited from unreported tests."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus = son55. Contribution 2 and the method core turn a sparse hidden-verifier pass/fail into "
                      "dense, decomposed ranking signals (verifier progress, phase, harness alignment, edit quality, "
                      "path penalty; an LCB summary; SkillQ). The skill text is then adapted by selecting on them. C26 "
                      "fits the 're-granularise credit where a single end scalar fails' step. Difference noted: C26 "
                      "members train weights with preference objectives, while here the optimised object is a "
                      "non-weight skill selected by pass-dominant SelectQ (revision note in batch notes). sol's "
                      "adapt_via_conditioning is not kept: the frozen agent reading injected text is the shared "
                      "substrate, and sol itself found C03 absent.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", role="primary")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "population_search_executable_fitness", "H15"),
                                       dmatch("sol", p, "attribute_and_patch_incumbent", "H10")],
                           "unassigned": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]["unassigned"]), "son55"),
                           "reason": "Opus = sol. H15: an evolving lesson bank conditions mutation, and an executable "
                                     "verifier selects. H10: one incumbent text artifact per task is rewritten from "
                                     "diagnosed errors and successes, keep-best, with earlier wins protected "
                                     "(M_keep). It is not H11: there is no skill library and no gate separating skill "
                                     "defects from execution lapses before an edit. Every generation mutates the "
                                     "survivor.",
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": "C26",
             "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": "H15"},
             "operation_correspondence": "A manufactured dense ranking signal (LCB progress, SkillQ) breaks ties under a "
                                         "pass-dominant executable fitness; the distilled lesson bank conditions the "
                                         "next mutation.",
             "necessary_conditions": "Signal validity independent of the target, and a matched-budget comparison "
                                     "against plain search/sampling.",
             "differences": "The proxy includes 40% verifier progress (partly circular), and there is no equal-budget "
                            "repeated-sampling or memory-off arm.",
             "evidence_ids": ["sol:E005", "sol:E007", "sol:E010", "son55:E015", "opus:O03"]},
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": "C26",
             "domain": {"namespace": "rsi", "main": "attribute_and_patch_incumbent", "sub": "H10"},
             "operation_correspondence": "Oracle KEEP/ADD/REMOVE lessons drive rewrites of one incumbent skill; the dense "
                                         "signal ranks the candidate rewrites.",
             "necessary_conditions": "Certification on data disjoint from critique and selection (H10).",
             "differences": "The paper explicitly reports on the selection tasks themselves (opus:O04).",
             "evidence_ids": ["sol:E019", "sol:E020", "sol:E009", "opus:O04"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.21810-1"): "local:2605.21810-4"},
            overrides={
                "local:2605.21810-4": renum("son55 local:2605.21810-1",
                                            "why these 8 of the 15 seed failures were selected."),
                "rs:adapt_via_conditioning/RE-1": dropped_card("adapt_via_conditioning"),
                "rs:adapt_via_conditioning/RE-3": dropped_card("adapt_via_conditioning"),
                "rs:adapt_via_conditioning/RE-4": dropped_card("adapt_via_conditioning"),
                "rs:adapt_via_conditioning/RE-5": dropped_card("adapt_via_conditioning"),
                "rs:self_supervised_signal_engineering/RE-6": {
                    "status": "unmet",
                    "reason": "Opus revision of son55's 'challenged_with_evidence'. That status means the paper "
                              "challenges the expectation with evidence; here the paper relies on runtime queries to "
                              "the hidden verifier, whose sanitised feedback includes test parameters (MAX_LENGTH=192, "
                              "'Failed 3 of 5 tests'). The expectation (avoid test-set information access) is therefore "
                              "unmet."},
                "rsi:attribute_and_patch_incumbent/F4": {
                    "applicable": False, "status": "not_applicable",
                    "reason": "Opus normalisation of son55's 'unknown' + applicable=false. The certifying signal is the "
                              "official CVDP hidden verifier, not self-constructed validation, so the failure mode does "
                              "not apply. The self-built proxy is a tie-breaker only."},
                "rsi:population_search_executable_fitness/S5": {
                    "status": "partial",
                    "reason": "Opus = sol. Candidate deltas are logged against the parent ('EFFECTIVE selection +0.523 "
                              "pass +0.500', sol:E020), and negative lessons are kept (REMOVE). No memory-off arm and no "
                              "per-lesson utility certification, so partial, not unmet."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "CL1", ["opus:O01", "opus:O02", "opus:O03"]), "CL3",
                                        ["son55:E015"]),
        "assessment": assess("sol", p, [
            "Opus: C1's 0/32 is very likely the selection set itself (opus:O01). 'Solved/8' compares pass@80 with pass@4 "
            "(opus:O02).",
            "Opus: the identity of 5 of the 8 tasks is not recoverable from the pinned text (bold lost); only PCIe_0004, "
            "802.11a_0001 and NoobsCpu_0002 are named."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2, confirmed. The sparse-hidden-verifier recovery bottleneck is real and "
                   "specific, but the only neighbour discussed is ACE-RTL ('complementary', not compared). General "
                   "prompt/skill-evolution and reflection optimisers are not covered.",
                   ["sol:E001", "son55:E024", "son55:E028"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Pass-dominant selection, repeat-robust LCB progress, "
                   "task-local oracle/mutator and repair form a coherent response to all-zero rewards. The "
                   "SelectQ-component design is asserted ('Empirically…') without data.",
                   ["sol:E004", "sol:E006", "sol:E007", "son55:E016"], ["son55:E017"]),
            "X": R("resolved", 3, "Both seats 3, confirmed. Algorithm 1, the SelectQ formula, M_keep, sanitiser/health "
                   "checks, parent re-evaluation and the visibility contract are explicit. Not 4: SkillQ sub-scores "
                   "(L, G, R_p, A_act, …) and the semantic-floor τ are not specified.",
                   ["sol:E004", "sol:E020", "sol:E021", "sol:E022"], ["son55:E029"]),
            "E.measurement": R("resolved", 3, "Both seats 3, confirmed. The official hidden verifier is the endpoint. "
                               "The AgentQ–pass correlation (r=0.90) is partly circular (40% verifier-progress term). "
                               "The budget-dependence of 'Solved/8' (opus:O02) is charged to E.causality/E.cost "
                               "(A2).", ["sol:E002", "sol:E010", "son55:E010"], ["son55:E015"]),
            "E.causality": R("resolved", 1, "Both seats 1, confirmed and strengthened. C1→C3 confounds skill evolution "
                             "with 20× rollouts and oracle-selected survivors, and no equal-budget sampling arm exists "
                             "despite the abstract's contrast with sampling (opus:O03). C1 = 0 is by selection "
                             "(opus:O01). C3→C4 is the only matched comparison (+6.6 pp, 3→6 tasks; single EA run). The "
                             "oracle, lesson bank and SelectQ components are not ablated.",
                             ["sol:E009", "sol:E013", "son55:E034"], ["opus:O01", "opus:O02", "opus:O03"]),
            "E.holdout": R("resolved", 0, "Opus = sol. The necessary separation is absent. The hidden verifier is the "
                           "selection signal (pass-dominant SelectQ), the source of in-rollout dense feedback (which "
                           "leaks test parameters, son55:E029), and the reported evaluation. Results are the "
                           "optimisation rollouts themselves (sol:E009), with no frozen-skill replay, held-out task or "
                           "transfer. The task subset was itself selected on the baseline's failures with an unstated "
                           "criterion. The honest scoping is credited in claim_support=scoped, not here (A2: oracle "
                           "signal → E.holdout).",
                           ["sol:E009", "sol:E012", "son55:E006", "son55:E029"], [],
                           ["entire text §§1–5 and Appendix A1–A6: no held-out, frozen-replay or transfer evaluation; "
                            "§3.1/§4.2 explicitly decline it"]),
            "E.statistics": R("resolved", 2, "Opus = sol (A2 tier 2). Repeated-run pass counts with denominators are "
                              "reported per task and configuration (1/80, 11/80, 35/80; C1 0/32, C2 4/32; 9/16 for one "
                              "generation), with candidate-level SEM. No CI, no significance test, and a single EA run "
                              "per configuration (no cross-search variance), which is the tier-2 limit.",
                              ["sol:E006", "sol:E015", "sol:E017", "son55:E011"], ["son55:E033"]),
            "E.cost": R("resolved", 1, "Both seats 1, confirmed. Rollout counts (32 vs 640) and the feedback cap are "
                        "stated, the paper admits it is 'compute-intensive', and there are no token/dollar/wall-time "
                        "figures or equal-compute baseline.", ["sol:E009", "sol:E016", "son55:E026"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (§1–5, Appendix A1–A6). In scope (a non-weight skill document evolved from "
                  "execution traces). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "material_ruling": "n/a (both seats reviewed the complete text). Bold task markers in Table 4 are lost in the "
                           "extraction (son55); that limits identifying the 8 tasks, not the claims' evidence.",
        "a3": "none (in scope; both seats agree).",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 2–4 are image-only. The Fig. 4 counts used (1/80, 11/80, 35/80) are stated in §4.4 "
                             "text; no plotted values used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "See rs_pattern.reason.", ["son55:E014", "son55:E015", "sol:E005"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C26"]],
                "C26 kept with the noted difference (non-weight target); sol's adapt_via_conditioning (null sub) is "
                "dropped.", ["son55:E014", "son55:E016", "sol:E007"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H10"], ["population_search_executable_fitness", "H15"]],
                "H10 over H11 (domain_pattern.reason). H15 is agreed by both seats.", ["sol:E019", "sol:E020", "sol:E021"],
                NOSCORE),
            res("expectations[local:2605.21810-1].status", *C(p, "expectations[local:2605.21810-1].status"), "revised",
                {"local:2605.21810-1": "unmet", "local:2605.21810-4": "unknown"},
                "A4 ID collision. sol's -1 (same verifier gives feedback, fitness and evaluation) is unmet, confirmed. "
                "son55's -1 (8-of-15 selection criterion) is renumbered -4 and kept unknown: the criterion is never "
                "stated and the bold markers are lost.", ["sol:E009", "son55:E025", "opus:O01"], NOEXP),
            XC(p, "local:2605.21810-2", "sol", "partial", "sol-only statistics question; verified.", ["sol:E006", "sol:E015"]),
            XC(p, "local:2605.21810-3", "sol", "partial", "sol-only cost question; verified.", ["sol:E009", "sol:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial", "Card not retained; kept as a check question.",
               ["sol:E009", "sol:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "sol", "unmet", "Card not retained; kept as a check question (no "
               "cheaper equal-budget alternative).", ["sol:E009", "opus:O03"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "sol", "partial", "Card not retained; kept as a check question.",
               ["sol:E007", "sol:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "sol", "partial", "Card not retained; kept as a check question.",
               ["sol:E008", "sol:E016"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "unmet", "One rollout model family, one "
               "benchmark, task-local evolution.", ["son55:E007", "son55:E032"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "unmet", "No equal-budget arm separating the "
               "manufactured signal from extra rollouts.", ["son55:E008", "son55:E009", "opus:O03"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "met", "The headline is the hidden-verifier "
               "pass rate.", ["son55:E010"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "unmet", "Cost is only qualitative.",
               ["son55:E026"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "revised", "unmet", "See expectation override (status "
               "semantics).", ["son55:E029", "son55:E003"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "revised", "not_applicable", "See expectation override.",
               ["son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "unmet", "Aggregation is task-local by design.",
               ["son55:E018", "sol:E007"]),
            XC(p, "rsi:population_search_executable_fitness/H15", "sol", "partial", "Task-local lesson bank and "
               "lineage; no frozen-skill or new-campaign test.", ["sol:E009", "sol:E018", "sol:E020"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "sol", "partial", "See expectation override.",
               ["sol:E020", "sol:E018"]),
            RC(p, "E.holdout", "sol", rr(0), "See ratings.E.holdout. son55's 1 credits the disclosed scope; scope "
               "honesty is reflected in claim_support, while the holdout item has no protecting evidence.",
               ["sol:E009", "son55:E006"], "−2.5 vs son55"),
            RC(p, "E.statistics", "sol", rr(2), "See ratings.E.statistics. Repeated-run failure counts with "
               "denominators meet A2 tier 2; son55's reasons (8 tasks, single EA run, no CI) are the tier-2 "
               "limitation itself.", ["sol:E015", "son55:E011"], "+1.25 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope. Same-task optimisation with oracle selection and in-rollout "
                                                   "oracle feedback. A 20× budget with no sampling control, C1 is the "
                                                   "selection set, no cost. evidence_level task. Expected about G2 M3 "
                                                   "X3 Em3 Ec1 Eh0 Es2 Ecost1.",
            "integrity_checks": "Both seats a1 on 2605.21810v1, text sha 8b827e99…; canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Tables 1–4, §2.2, §3.1–3.2, §4.2–4.4, Appendix A2–A4 re-read; C1 provenance inferred "
                                "from 96 = 24×4.",
            "shared_error_review": "No shared rating error. Both seats' E.causality 1 is strengthened (opus:O01–O03).",
            "rating_agreement": "E.holdout and E.statistics → sol; six shared items confirmed. Final 52.5.",
        },
    }
    return S
