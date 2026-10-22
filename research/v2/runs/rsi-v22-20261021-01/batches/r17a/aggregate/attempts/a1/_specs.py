"""Opus rulings for r17a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat inputs: all ten a1 seat records match conflicts.json seat_record_hashes (asserted by _build.py). No "
        "overrides, no seat errors.",
        "2604.15719 Milkyway (sol 62.5 / son55 71.25): final 67.5. X → son55 3 (bounded typed patch chain, caps, "
        "deterministic apply, state boundary all specified). E.causality → sol 2. evidence_level → sol task: the "
        "harness helps later checkpoints of the same question it was written from, and cross-question reuse is "
        "explicitly not quantified (EvoTest r08a / Reflexion cal-dev precedent). Opus findings: (1) Table 2's "
        "Δ_FH−Δ_NH (+13.1/+9.1/+9.3/+11.0) includes a T-4d offset at a checkpoint that is identical by construction "
        "(FH starts 5.6/3.0/1.0/5.5 below NH). The T-1d endpoint gaps in Table 7 are +7.6/+6.1/+8.3/+5.5, still "
        "positive in all four cells. (2) The flagship case writes U1 'between ck1 and ck2' and has it active at T-3d, "
        "which contradicts Algorithm 1 (no edit at t=1) and the Table 7 caption (first non-empty harness at T-2d). "
        "(3) The '±5% compute' claim does not hold for Qwen3.5 (−10.7% tool calls) or GLM (+8.5% prompt tokens). "
        "RS → self_supervised_signal_engineering primary + adapt_via_conditioning supporting. Domain H01 (both).",
        "2604.15840 CoEvolve (scope conflict): out_of_scope, sol. A3 bullet 1: every reported number is a GRPO-"
        "trained checkpoint. The retained non-weight object (task set D_t) is RL training data that the evaluated "
        "agent never reads at test time. Same disposition as WebRL, Confucius, Middo, GenEnv and AgentEvolver in this "
        "run. Not scored; RS C08 and domain H23 kept as informational resemblance records.",
        "2604.16941 MemRes (sol 55.0 / son55 48.75): final 46.25. M → son55 2. E.causality → son55 1: only the "
        "Level-1 cache is ablated, against a PLLM number copied from another paper. E.statistics → sol 2 (A2: 10 "
        "runs with SD, no CI or test). E.cost → sol 2 (success-conditioned latency, not like-for-like). "
        "evidence_level retained (both) is kept, scoped: the store-off evidence is a near-duplicate cache inside one "
        "batch. The paper says disabling Level 1 'only increases runtime', which contradicts Table 2's −146 snippets. "
        "RS → decompose_and_delegate/C25 + heterogeneous_decomposition.",
        "2604.17399 MC² (sol 63.75 / son55 61.25): final 60.0. G → son55 2: Table 10 contains domain tactics, which "
        "weakens the 'meta-level, not task-level' gap. E.cost → son55 2. Shared correction: E.statistics 3 → 2 "
        "for both seats. Under the A2 ladder, 3 seeds with 95% CIs but no significance test is a 2 (r07a/r08a/r14b "
        "precedent). Two best cells overlap the strongest baseline (Qwen MATH-500, Llama Game-of-24). The store-off "
        "ablation (Table 2) is a single run. Correctness labels feed the store on the evaluated stream: E.holdout 1 "
        "(both). Domain → H00 (sol).",
        "2604.17488 AutoVQA-G (sol 50.0 / son55 47.5): final 47.5. X → son55 2 (rubric-update operator and "
        "cross-image lifecycle unspecified). E.holdout → son55 2 (independent human re-annotation; no oracle "
        "signal in the loop). Scope: kept reviewed under the Reflexion cal-dev precedent. The rubric edit carries "
        "into the next regeneration of the same image (boundary A-class, within-instance only), so the record is "
        "evidence_level task and no cross-sample retention is credited. RS → self_supervised_signal_engineering/C08 "
        "+ adapt_via_conditioning.",
        "A4 hygiene: hidden local-ID collisions were renumbered in Milkyway (son55 local-1/2/3 → local-4/3/5), "
        "MemRes (son55 local-1/2 → local-4/5), MC² (son55 local-1/2/3 → local-5/6/7) and AutoVQA-G (son55 "
        "local-1/2/3 → local-4/5/6). Every move is noted in the expectation and its resolution.",
        "Figure dependence: Milkyway Figs 3–4 (values from Tables 7 and 10), CoEvolve Figs 3–5 and 7, MC² Figs 3 "
        "and 6 and the App I prompt figures, AutoVQA-G Fig 2. These are image-only or empty in the pinned HTML. Only "
        "values stated in text or tables were used, and nothing was read off an image.",
        "No material requests. Appendix D (Milkyway) and Appendix I (MC²) prompt boxes are empty in the pinned "
        "HTML. No disputed rating depends on them.",
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

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    # =========================================================== 2604.15719 Milkyway (sol 62.5 / son55 71.25)
    p = "2604.15719"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "T-4d is the null control because the harness is empty for all conditions by construction",
                    "App C.4 Table 7 caption",
                    "T-4d is identical by construction across NH and FH, yet FH starts below NH in all four cells "
                    "(Table 7: 44.0 vs 49.6, 50.0 vs 53.0, 55.5 vs 56.5, 55.0 vs 60.5), i.e. offsets of 5.6/3.0/1.0/5.5 "
                    "points from run-to-run noise alone. The headline Δ_FH−Δ_NH (+13.1/+9.1/+9.3/+11.0) subtracts these "
                    "low FH starts. At the T-1d endpoints the FH−NH gaps are +7.6/+6.1/+8.3/+5.5 (58.0−50.4, 66.9−60.8, "
                    "68.5−60.2, 70.5−65.0). They are smaller but positive in every cell. Neither seat noted the offset.",
                    kind="our_inference"),
            opus_ev(p, "O02", "FH 44.0 50.5 58.6 58.0", "App C.4 Table 7, GPT-5.4 / 05-05 FH row",
                    "FH ladder for the 05-05 cell (n=35). The low T-4d start (44.0 against NH 49.6) enters Δ_FH.",
                    kind="author_report"),
            opus_ev(p, "O03", "NH 53.0 60.2 43.6 60.8", "App C.4 Table 7, GPT-5.4 / 05-06 NH row",
                    "With no persistence, NH swings 16.6 points between adjacent checkpoints at n=28 (60.2 → 43.6 → "
                    "60.8). This is the noise scale against which single-run endpoint gaps of 6–8 points are read.",
                    kind="author_report"),
            opus_ev(p, "O04", "the editor first writes after the second daily run, so T-2d is the first checkpoint at "
                              "which FH consumes a non-empty harness",
                    "App C.4 Table 7 caption",
                    "Protocol statement: no harness content can be read before T-2d. Algorithm 1 agrees: at t=1 the "
                    "harness is copied unchanged (opus:O06).", kind="author_report"),
            opus_ev(p, "O05", "FH after the writes. ck2 (T-3d,", "App C.6 Fig. 5 primary mechanism case",
                    "The flagship case reports U1 written 'between ck1 and ck2' and active at ck2 = T-3d, where FH "
                    "already moves from 35.2 to 5.46. Under the stated protocol (opus:O04, opus:O06) no harness is "
                    "consumable at T-3d. Either the case's T-3d jump precedes any writeback, or T-3d is not the "
                    "pre-writeback control the mechanism study relies on. Both cannot be true. sol flagged the "
                    "contradiction; son55 did not.", kind="our_inference"),
            opus_ev(p, "O06", "9: H t + 1 ← H t H_{t+1}\\leftarrow H_{t}", "App A.4 Algorithm 1, line 9 (t=1 branch)",
                    "Algorithm 1 calls the editor only for t ≥ 2. At t=1 the harness passes through unchanged.",
                    kind="author_report"),
            opus_ev(p, "O07", "NH 54.4 40.1 32.5 52.9", "App C.4 Table 10 same-day control (n=28)",
                    "With the evidence cutoff fixed, NH moves 21.9 points across rounds (54.4 → 32.5 → 52.9). This "
                    "single-run dispersion is as large as or larger than the endpoint FH–NH gaps.",
                    kind="author_report"),
            opus_ev(p, "O08", "Qwen3.5 / 05-06 NH 29.0 407.8 K 28.8 FH 25.9 369.6 K 26.2",
                    "App C.4 Table 9, Qwen3.5 cell",
                    "FH uses 10.7% fewer tool calls and 9.4% fewer prompt tokens than NH. The text's 'within ±5% of "
                    "NH across all four cells' does not hold here.", kind="our_inference"),
            opus_ev(p, "O09", "GLM-5.1 / 05-06 NH 32.7 287.0 K 21.6 FH 34.6 311.3 K 22.3",
                    "App C.4 Table 9, GLM-5.1 cell",
                    "FH uses 8.5% more prompt tokens and 5.8% more tool calls than NH. Per-checkpoint footprints are "
                    "only reported at T-1d, and editor calls are not reported at all.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus: the contribution is the pre-resolution signal. It is a process-level adaptation signal "
                      "derived from the agent's own repeated forecasts while ground truth (the outcome) is "
                      "unavailable, which is the definition of self_supervised_signal_engineering (son55). The signal "
                      "reaches the frozen predictor as a conditioning block, so adapt_via_conditioning (sol) is kept "
                      "as the delivery channel. No sub-card fits: C07/C08/C26 involve training or generated data, and "
                      "C03 needs a canonical schema plus an upstream phase.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", role="primary"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"].get("revision_proposals", [])},
        "pattern_mapping": [
            PM("self_supervised_signal_engineering", None, "abstract_experience_into_guidance", "H01",
               "Temporal contrasts across checkpoint notes (a label-free signal) drive explicit add/revise/deprecate/"
               "null patches to a capped typed store, which is read at the next checkpoint.",
               "H01 needs an explicit edit vocabulary and bounded size (met). Its step 2 assumes an outcome-signal "
               "gate (unmet before resolution: the trigger is self-derived contrast), and step 5 asks for a "
               "curator ablation (partial: GH swaps the store form, not the editor).",
               ["son55:E005", "son55:E006", "sol:E003", "son55:E010"]),
            pmap("sol", p, 0),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.15719-1"): "local:2604.15719-4",
                    ("son55", "local:2604.15719-2"): "local:2604.15719-3",
                    ("son55", "local:2604.15719-3"): "local:2604.15719-5"},
            overrides={
                "local:2604.15719-3": {
                    "status": "unmet",
                    "reason": "Opus: single runs per cell at n=28–35 with no intervals, seeds or tests. Table 10 shows "
                              "NH moving 21.9 points at fixed evidence (opus:O07), and NH swings 16.6 points between "
                              "adjacent checkpoints (opus:O03). Scored/launched counts are given, but they do not "
                              "answer the uncertainty requirement.",
                    "note": "Merged here from son55:local:2604.15719-2 (same statistics question). son55's own local-3 "
                            "(cross-question scope) moved to local-5."},
                "local:2604.15719-4": {
                    "status": "partial",
                    "reason": "Opus (revised from unmet): GH is a matched-budget alternative writer under the same "
                              "revisit schedule, but only in the two GPT-5.4 cells. No note-contrast-free reflection "
                              "arm and no ACE-style writer is run under the same schedule.",
                    **renum("son55:local:2604.15719-1")},
                "local:2604.15719-5": renum("son55:local:2604.15719-3"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O05", "opus:O07"]), "C2",
                                        ["opus:O08"]),
        "assessment": assess("son55", p, [
            "Opus: the Δ-on-Δ headline includes T-4d offsets at an identical-by-construction checkpoint. Endpoint "
            "FH–NH gaps are +5.5 to +8.3 (opus:O01).",
            "Opus: the flagship case's writeback timing contradicts Algorithm 1 and the Table 7 caption (opus:O04–O06).",
            "Opus: the '±5% compute' statement fails for the Qwen3.5 and GLM cells (opus:O08, opus:O09)."],
            evidence_level="task",
            evidence_level_note="Opus sides with sol. The retained typed harness is read at later checkpoints, with a "
                                "same-schedule store-off arm (NH), but those checkpoints revisit the same question "
                                "that produced the entries. Cross-question reuse is explicitly not quantified (App "
                                "A.4/A.5, §5). EVIDENCE.md requires gains on later tasks for retained, and run "
                                "precedent (r08a EvoTest, cal-dev Reflexion, r15b SpaceMind) caps same-instance reuse at "
                                "task. Unlike those cases no outcome label is used before resolution, which is credited "
                                "in E.holdout, not in the level.",
            claim_support="scoped",
            strongest_supported_claim="In four small matched FutureWorld cells (two dates, n=28–35, three cells "
                                      "sharing the 05-06 questions), typed bounded writeback ends above no-persistence "
                                      "at T-1d by +5.5 to +8.3 points and above free-form memory in the two GPT-5.4 "
                                      "cells. These are single runs whose same-day noise reaches ~20 points, so the "
                                      "direction holds in 4/4 cells but the magnitude is uncertain. End-to-end "
                                      "benchmark leads are under an unequal protocol (three revisits vs single runs)."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The gap is specific: outcome-only, delayed supervision "
                   "gives no process credit before resolution. The changed object (a question-local typed "
                   "procedural state) is named, and Reflexion/ExpeL/ACE/Agent KB/MemEvolve/Meta-Harness are "
                   "positioned. Not 4: the paper does not argue why generic multi-round reflection across revisits, "
                   "which also needs no outcome, is insufficient.",
                   ["son55:E002", "son55:E003", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. note contrast → diagnosis → bounded typed patch → "
                   "deterministic apply → next-checkpoint conditioning is reconstructable. It yields distinguishable "
                   "predictions: delayed separation, typed beats blob, procedure not answer. The load-bearing "
                   "assumption (a note diff exposes a procedural lesson rather than mere new evidence) is plausible "
                   "but untested.",
                   ["son55:E001", "son55:E004", "son55:E005", "sol:E002", "sol:E003"]),
            "X": R("resolved", 3, "Opus sides with son55. The state boundary (only H persists), the add/revise/"
                   "deprecate/null vocabulary, ≤1 patch per checkpoint, ≤2 adds, a 5-entry per-axis cap, duplicate "
                   "filtering, fixed apply order and the per-checkpoint versions are all specified. Table 11 audits "
                   "the realized patch stream. Not 4: there is no utility gate or rollback before resolution, the "
                   "post-resolution check is unimplemented in the evaluation, and the App D prompt boxes are empty in "
                   "the pinned HTML (a rendering gap, not scored as absent). sol's timing contradiction (opus:O05) "
                   "concerns the validity of the pre-writeback control and is scored once, in E.causality (A2).",
                   ["son55:E005", "son55:E006", "son55:E007", "sol:E003", "son55:E015"], ["son55:E007"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. The official FutureX scorer is used and the "
                               "FutureWorld scorer is fully specified, on live questions whose outcomes are unknown "
                               "at prediction time. Exclusions are disclosed: resolved-only scoring, numeric items "
                               "without the 8-point history dropped, 28/50 scored. The timing of the FutureWorld "
                               "baseline runs is not stated.",
                               ["son55:E021", "son55:E022", "sol:E007", "sol:E008"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. The design is good: NH (store-off) and GH "
                             "(matched-budget generic memory) on the same schedule, a same-day repeat, and an artifact "
                             "audit. Three things keep it at 2. (1) The headline Δ-on-Δ subtracts FH starts that are "
                             "lower by 1–5.6 points at the identical-by-construction T-4d checkpoint. Endpoint gaps "
                             "are +5.5 to +8.3 (opus:O01). (2) The 'built-in pre-writeback control' is contradicted by "
                             "the flagship case, which has a harness active at T-3d (opus:O04–O06). (3) GH exists only "
                             "in the two GPT-5.4 cells, and there is no note-contrast-free reflection arm. Table 1 "
                             "compares three revisits against single runs. Noise magnitude is scored in "
                             "E.statistics, not here (A2).",
                             ["son55:E009", "son55:E010", "son55:E011", "son55:E013", "son55:E015", "sol:E009",
                              "opus:O01"],
                             ["opus:O05", "sol:E005", "son55:E017"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Under the forward-only live protocol no "
                           "outcome reaches the method before scoring, the harness is built only from earlier "
                           "same-question notes, and the self-evolving baselines are warmed on preceding resolved "
                           "data and then frozen. This fits the scoped within-question claim. The cohorts are two "
                           "dates selected for ladder eligibility, and the milkyway_v5 tuning history is not stated.",
                           ["son55:E021", "sol:E011", "son55:E008", "sol:E006"], ["son55:E023"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). Sample sizes, scored/launched counts and "
                              "flat or negative arms are reported. No intervals, seeds or tests, and single-run swings "
                              "of 16–22 points at n=28 (opus:O03, opus:O07) are comparable to the claimed gaps.",
                              ["son55:E013", "sol:E008", "opus:O07"], ["opus:O03"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Per-question tool calls, prompt tokens and LLM "
                        "calls are given at T-1d for every cell. The 'within ±5%' summary is wrong for Qwen3.5 and "
                        "GLM (opus:O08, opus:O09). Editor calls, cumulative cost across checkpoints, and Milkyway's "
                        "three revisits against single-run baselines in Table 1 are unaccounted.",
                        ["son55:E014", "sol:E010"], ["opus:O08", "opus:O09", "son55:E017"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 HTML text read (App A–D; App D prompt boxes empty in the HTML). In scope "
                  "(system_method): a persistent non-weight typed harness is edited from execution-derived contrasts "
                  "and read at later checkpoints. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 3–4 are image-only. Their values come from Table 7 (stated to match Fig. 3) and "
                             "Table 10.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "Same-question later checkpoints only. Cross-question reuse is not quantified (App A.4/A.5, §5). Run "
                "precedent caps same-instance reuse at task (r08a EvoTest, cal-dev Reflexion).",
                ["son55:E007", "son55:E008", "sol:E006"], "none (level not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "The contribution is a label-free adaptation signal from the agent's own repeated outputs. "
                "Conditioning is the channel, kept as supporting.", ["son55:E001", "son55:E002"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", None], ["adapt_via_conditioning", None]],
                "Union: son55's card as primary and sol's as supporting, both with sub null.",
                ["son55:E001", "sol:E002"], NOSCORE),
            XC(p, "local:2604.15719-1", "sol", "partial",
               "A4 collision: sol's local-1 (is the typed pre-resolution signal causal?) stays here: partial, because "
               "NH/GH/same-day controls exist but the T-4d offset and case timing weaken them (opus:O01, opus:O05). "
               "son55's local-1 (alternative editor under the same schedule) moves to local-4, revised to partial.",
               ["sol:E004", "sol:E009", "opus:O01", "opus:O05"]),
            XC(p, "local:2604.15719-2", "sol", "partial",
               "A4 collision: sol's local-2 (forward-only holdout) stays here: partial (no cross-question "
               "certification). son55's local-2 (statistics) is merged into local-3.", ["sol:E011", "sol:E006"]),
            XC(p, "local:2604.15719-3", "revised", "unmet",
               "sol's local-3 and son55's local-2 ask the same statistics question. Final unmet: no intervals or "
               "seeds, with single-run swings of 16–22 points (opus:O03, opus:O07). son55's local-3 (cross-question "
               "scope, not applicable) moves to local-5.", ["sol:E008", "son55:E013", "opus:O07"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "partial",
               "Verified: three backbones, but the mechanism evidence covers two dates of one benchmark and GH runs "
               "only on GPT-5.4.", ["son55:E011", "son55:E023"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "partial",
               "Verified: repetition, persistence form and compute are partly isolated. The contrast signal itself is "
               "not ablated, and the T-4d offset inflates the Δ-on-Δ (opus:O01).",
               ["son55:E009", "son55:E010", "opus:O01"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "met",
               "Verified: evaluated on the real forecasting score with official or fully specified scorers.",
               ["son55:E020", "son55:E022"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-4", "son55", "partial",
               "Verified: ACE/Agent KB/MemEvolve run on different base agents, frozen. No revisit-reflection "
               "baseline.", ["son55:E019", "son55:E018"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "partial",
               "Verified: T-1d main-agent footprint only, and the ±5% summary is wrong for two cells (opus:O08).",
               ["son55:E014", "opus:O08"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "met",
               "Verified: live forward-only protocol.", ["son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/F5", "son55", "partial",
               "Verified: guidance comes from the agent's own evolving-evidence trajectories, but before resolution "
               "it is not grounded in a verified outcome.", ["son55:E001", "son55:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "met",
               "Verified: the fixed assumption (adaptation only from post-resolution outcomes) is named.",
               ["son55:E002", "son55:E004"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: contrasts are between the agent's own successive notes, not success/failure pairs.",
               ["son55:E001"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
               "Verified: the trigger is model-derived. The outcome check exists only after resolution and is not "
               "evaluated.", ["son55:E006", "son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
               "Verified: the gate is a validity/redundancy filter, not a utility gate.", ["son55:E006", "sol:E003"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", 3,
                "See ratings.X: the retention chain is fully specified. The timing contradiction is scored once in "
                "E.causality (A2).", ["son55:E005", "son55:E006", "sol:E003"], "+5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", 2,
                "See ratings.E.causality: the T-4d offset (opus:O01) and the contradicted pre-writeback control "
                "(opus:O05) leave the attribution's size open, although the direction holds in all four cells.",
                ["opus:O01", "opus:O05", "son55:E009", "son55:E010"], "−3.75 vs son55 (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims.C1 / ratings.E.causality (both seats)",
             "sol_value": "Δ_FH−Δ_NH +13.1/+9.1/+9.3/+11.0 taken as the effect size",
             "son55_value": "Δ_FH−Δ_NH +13.1/+9.1/+9.3/+11.0 taken as the effect size",
             "final_value": "endpoint FH−NH at T-1d +7.6/+6.1/+8.3/+5.5. The difference is the FH-low T-4d offset at an "
                            "identical-by-construction checkpoint",
             "reason": "Both seats used the paper's Δ-on-Δ readout. Table 7 shows that FH starts below NH in all four "
                       "cells at T-4d, where the conditions are identical by construction (opus:O01, opus:O02). The "
                       "effect is real in direction and smaller in size. Recorded under E.causality (sol's 2 kept). "
                       "No rating change beyond the resolution.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v3 text first. Initial view: in scope; evidence "
                                                   "task (same-question reuse; cross-question not quantified). G 3, "
                                                   "M 3, X 3, Em 3, Ec 2, Eh 3, Es 1, cost 2. Noted the T-4d offset in "
                                                   "Table 7 and the case-timing contradiction before opening seats.",
            "integrity_checks": "Both seats a1 on 2604.15719v3, material sha 4b8c4065…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: within-question typed writeback beats no persistence at "
                                "T-1d by +5.5 to +8.3 in 4/4 small single-run cells, and beats generic memory in the "
                                "two GPT cells. claim_support scoped. Table 1 leads are end-to-end under an unequal "
                                "protocol.",
            "shared_error_review": "Agreed items re-checked: G 3, M 3, Em 3, Eh 3, Es 1, cost 2 kept. Shared omission "
                                   "recorded: both seats took the Δ-on-Δ headline as the effect size.",
            "rating_agreement": "X → son55, E.causality → sol, evidence_level → sol. Final 67.5.",
        },
    }

    # =========================================================== 2604.15840 CoEvolve (scope conflict)
    p = "2604.15840"
    OOS = ("out_of_scope (rubric A3 bullet 1; Opus sides with sol on the scope conflict). The evaluated object is "
           "the GRPO-trained Qwen policy. Every reported number is a trained checkpoint on AppWorld/BFCL (Tables 1–5, "
           "7, 8) or ALFWorld/WebShop (Table 10), including the matched-explorer and validation ablations (Tables 11–14) "
           "(sol:E001, opus:O02). The retained non-weight object, the evolving synthetic task set D_t, is RL training "
           "data. Validated tasks are appended to form 'the updated training distribution for the next iteration' "
           "(opus:O01), and the evaluated agent never reads them at test time. The explorer LLM (Qwen3-Max) and its "
           "prompts are fixed. son55's boundary reading (the retained object is the task set) is the situation this run "
           "has already ruled out_of_scope for WebRL (failure-seeded instruction pool), Confucius and Middo (iterated "
           "SFT datasets), GenEnv and AgentEvolver. A3 bullet 2 does not apply because the task set is not evaluated "
           "as a harness component. Table 15's diversity/relevance metrics describe training data. Flip condition: "
           "the synthesized task set or the signal-guided explorer is evaluated as a reusable artifact, e.g. read by a "
           "frozen agent at test time or released and certified as a curriculum/benchmark resource with its own "
           "evidence. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "forming the updated training distribution for the next iteration", "§3.3 Environment "
                    "Validation", "The only retained non-weight state (validated tasks) is defined as the next RL "
                    "iteration's training distribution. It is consumed by GRPO, not read by the deployed agent.",
                    kind="author_report"),
            opus_ev(p, "O02", "CoEvolve is built on top of GRPO and yields complementary gains across model scales",
                    "§4.2 Table 2 caption", "The headline comparison is GRPO-trained checkpoints with versus without "
                    "data evolution. What changes between arms is the weights produced by training on different "
                    "data.", kind="author_report"),
            opus_ev(p, "O03", "Evaluation temperature 0", "App A.2 Table 9",
                    "Evaluation runs the trained policy alone (greedy). The evaluation protocol has no task-set, "
                    "memory or prompt-state input.", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). Both seats: self_supervised_signal_engineering. son55's C08 "
                      "(generator plus one load-bearing quality gate, environment validation, feeding retraining) is "
                      "kept because it fits; a scope-excluded row may carry the resemblance record. Scope is decided "
                      "by A3, not by the card match.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="informational (out_of_scope)",
                               role="primary")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H23",
                                              fit="informational (out_of_scope)")],
                           "unassigned": [],
                           "reason": "Informational (out_of_scope). Both seats H23, which the card itself marks as a "
                                     "boundary pattern involving weight updates.",
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0)],
        "expectations": lambda sol, son: [
            dict(e, informational=True,
                 reason="Informational (row out_of_scope; not scored). " + str(e.get("reason", "")))
            for e in merge_exps(p, sol, son, rename={}, overrides={})],
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O03"]),
        "assessment": assess("sol", p, [
            "Out-of-scope disposition is not a judgment that the RL results are wrong.",
            "Boundary recorded with a flip condition (see reason)."],
            evidence_level=None,
            evidence_level_note="No harness evidence label for an out-of-scope weight-level paper (run convention). "
                                "Both seats wrote 'task'; normalized to null (shared correction).",
            claim_support=None,
            claim_support_note="Not assessed under this rubric. The RL gains are author-reported checkpoint results.",
            strongest_supported_claim=None),
        "ratings": {k: R("unknown", None, OOS, ["sol:E001", "sol:E002", "opus:O01", "opus:O02"])
                    for k in ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")},
        "status": "out_of_scope",
        "reason": OOS,
        "aggregate_status": "accepted_final",
        "a3": "out_of_scope (A3 bullet 1): evaluated product is GRPO weights; task set is training data (Opus = sol)",
        "figure_dependence": "Figs 3–5 and 7 are image-only. Not used (row not scored).",
        "resolutions": (
            [res("status", *C(p, "status"), "sol", "out_of_scope", OOS, ["sol:E001", "opus:O01", "opus:O02"],
                 "son55 56.25 → null (not scored)"),
             res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                 [["self_supervised_signal_engineering", "C08"]],
                 "Informational only. C08's generate-gate-retrain shape fits the operation.",
                 ["son55:E006", "son55:E015"], NOSCORE)]
            + [XC(p, eid, "son55", C(p, f"expectations[{eid}].status")[1],
                  "Informational (row out_of_scope). son55's answer is retained as a check-question record; it "
                  "is not verified for scoring.", ["son55:E001"])
               for eid in ["local:2604.15840-1", "local:2604.15840-2", "local:2604.15840-3",
                           "rs:self_supervised_signal_engineering/RE-1", "rs:self_supervised_signal_engineering/RE-2",
                           "rs:self_supervised_signal_engineering/RE-3", "rs:self_supervised_signal_engineering/RE-4",
                           "rs:self_supervised_signal_engineering/RE-5", "rs:self_supervised_signal_engineering/RE-6",
                           "rsi:self_generate_the_curriculum/F3", "rsi:self_generate_the_curriculum/S1",
                           "rsi:self_generate_the_curriculum/S2", "rsi:self_generate_the_curriculum/S3",
                           "rsi:self_generate_the_curriculum/S4", "rsi:self_generate_the_curriculum/S5",
                           "rsi:self_generate_the_curriculum/S6"]]
            + [res(f"ratings.{k}", *C(p, f"ratings.{k}"), "sol", {"status": "unknown", "rating": None},
                   "Out-of-scope rows carry all eight items unknown (null), not son55's ratings (A3).",
                   ["opus:O01", "opus:O02"], "none (not scored)")
               for k in ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")]),
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level / assessment.claim_support",
             "sol_value": ["task", "scoped"], "son55_value": ["task", "scoped"], "final_value": [None, None],
             "reason": "Out-of-scope rows carry null level and support (run convention, e.g. r09a AgentEvolver). sol "
                       "kept 'task/scoped' despite excluding the row, and son55 assigned them for its in-scope reading.",
             "evidence_ids": ["opus:O01"], "score_impact": "none (not scored)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text with appendices first. Every result is a "
                                                   "GRPO checkpoint, and the evolving task set is training data never "
                                                   "read at test time. Leaned out_of_scope (A3 bullet 1).",
            "integrity_checks": "Both seats a1 on 2604.15840v1, material sha 65836b79…; canonical seat hashes equal "
                                "conflicts.json. sol completed identification for an excluded row, which is allowed.",
            "core_claim_check": "A3 decided on the evaluated object (opus:O01–O03) against this run's out_of_scope "
                                "precedents (WebRL, Confucius, Middo, GenEnv, AgentEvolver) and its in-scope ones "
                                "(stores read at test with a store-off arm).",
            "shared_error_review": "Both seats' 'task/scoped' are normalized to null for an out-of-scope row.",
            "rating_agreement": "No ratings retained (all unknown). son55's 56.25 is not carried.",
        },
    }

    # =========================================================== 2604.16941 MemRes (sol 55.0 / son55 48.75)
    p = "2604.16941"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Disabling it only increases runtime", "§3.1 Threats to validity, order sensitivity",
                    "The authors say disabling Level 1 costs only runtime, and §2.1 adds that the cascade 'independently "
                    "resolves these near-duplicates'. Table 2 reports 146 fewer resolved snippets (−5.0 pp) with "
                    "Level 1 off (opus:O02). If the table is right, the text's account of the memory is wrong. If the "
                    "text is right, the 5 pp is a timeout/runtime effect rather than retained knowledge. The run count "
                    "and variance of the ablation are not stated.", kind="our_inference"),
            opus_ev(p, "O02", "Ablation (Level 1 OFF) 2357", "§3 Table 2",
                    "The only tabulated component ablation: 2357 vs 2503 resolved.", kind="author_report"),
            opus_ev(p, "O03", "to resolve near-duplicate datasets (e.g., identical GitHub forks)", "§2.1 Intra-Session "
                    "Memory", "Level 1 is a solution cache for near-duplicate snippets inside the evaluated batch. The "
                    "measured retained effect is cache reuse on the evaluation stream, not the transfer of 'tips'.",
                    kind="author_report"),
            opus_ev(p, "O04", "Median Resolution (success)", "§3.2 Table 3",
                    "Latency is conditioned on success. Failed snippets (up to 500 s total timeout) are excluded from "
                    "the reported time, and PLLM's ~120–180 s comes from its own paper and hardware.",
                    kind="our_inference"),
            opus_ev(p, "O05", "in practice, levels 1 to 5 handle the vast majority", "§2.2 Confidence Cascade",
                    "Levels 2–5 (curated maps, templates, co-occurrence, heuristics) are said to do most of the work, "
                    "but only Level 1 and co-occurrence (prose, <2%) are ablated.", kind="author_report"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["heterogeneous_decomposition"],
            "outside_taxonomy": False,
            "reason": "Opus: the central operation is 'only call the LLM when all deterministic rules fail'. Each "
                      "sub-problem goes to an exact handler or the pip/Docker resolver, and the LLM emits constrained "
                      "version pins checked by build, which is C25 (son55). The failure-category partition (Python 2 "
                      "syntax / name mismatch / version / C-extension) with tailored treatments is a real secondary "
                      "move (sol's heterogeneous_decomposition; sub null, since C04 is about compressing trained "
                      "artifacts). sol's adapt_via_conditioning is dropped: exact reuse is a cache, and partial-match "
                      "'hints' do not condition a model's task generalization.",
            "matches": [smatch("son55", p, "decompose_and_delegate", role="primary"),
                        smatch("sol", p, "heterogeneous_decomposition", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": seat("son55", p)["domain_pattern"].get("unassigned", []),
                           "revision_proposals": []},
        "pattern_mapping": [
            PM("decompose_and_delegate", "C25", "index_experience_for_reuse", "H03",
               "Docker-validated pip solutions are cached per import set and re-applied to Jaccard-similar later "
               "snippets as the cascade's Level 1. The rest of the cascade delegates to deterministic solvers.",
               "H03 needs a write gate (met: Docker build) and a store-removal certificate (partial: the Level 1 OFF "
               "ablation, built on the evaluated batch). Its F3 (store built from the test stream) is present.",
               ["son55:E009", "son55:E010", "sol:E008", "son55:E018"]),
            pmap("sol", p, 1),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.16941-1"): "local:2604.16941-4",
                    ("son55", "local:2604.16941-2"): "local:2604.16941-5"},
            overrides={
                "local:2604.16941-1": {
                    "reason": "Opus: verified. Text 'Disabling it only increases runtime' versus Table 2's −146 "
                              "snippets (opus:O01, opus:O02). Unmet.",
                    "note": "A4 hidden collision: son55 used local-1 for the copied-baseline question, moved to "
                            "local-4. Both seats rated their own local-1 unmet, so no mechanical conflict was "
                            "raised."},
                "local:2604.16941-4": renum("son55:local:2604.16941-1"),
                "local:2604.16941-5": renum("son55:local:2604.16941-2"),
                "rs:decompose_and_delegate/RE-1": {
                    "status": "partial",
                    "reason": "Opus (revised from met): calls, tokens and latency are reported, but latency is "
                              "success-conditioned (opus:O04) and set against PLLM's published figures on other "
                              "hardware and another LLM. Failed builds and retries are not costed."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01", "opus:O03"]), "C1", ["opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: the text's 'disabling Level 1 only increases runtime' contradicts Table 2 (opus:O01, opus:O02).",
            "Opus: the measured retained effect is a near-duplicate solution cache on the evaluated batch (opus:O03)."],
            evidence_level="retained",
            evidence_level_note="Both seats retained, kept and scoped. A Docker-gated store written during the batch "
                                "is read on later, different snippets, and the same-pipeline Level 1 OFF arm loses 5.0 "
                                "pp. Run precedent (r06a SWE-Exp, r15b Evo-MedAgent) admits same-stream store-off "
                                "evidence as retained. Its weaknesses (cache of near-duplicate forks, built from the "
                                "test stream, contradicted by the authors' own text, no ablation variance) are scored "
                                "in E.causality and E.holdout, not by lowering the level.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The limitation of the nearest system (PLLM 54.7%, "
                   "deterministic root causes, wasted LLM time) is concrete and quantified. But the failure analysis "
                   "is on the evaluation benchmark, the harness-level learning component (memory) is motivated only "
                   "by PLLM's sequential evaluation, and V2/Repo2Run are named, not compared.",
                   ["son55:E002", "son55:E003", "son55:E021", "sol:E001"]),
            "M": R("resolved", 2, "Opus sides with son55. The cascade ordering (exact levels first, LLM last, Docker "
                   "verification) is coherent for the stated root causes. The mechanism behind the headline gain, "
                   "however, is static curated knowledge, and the self-evolving part is thin: the roles of tips and "
                   "anti-patterns are unspecified, nothing argues why memory beats a cache, and the authors' own "
                   "causal account of Level 1 contradicts their ablation (opus:O01). No distinguishing predictions "
                   "against simpler alternatives are made. sol's 3 credits the cascade's clarity, which X already "
                   "rewards.",
                   ["son55:E001", "son55:E009", "son55:E010", "son55:E011"], ["son55:E022", "opus:O01"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Levels, Jaccard 0.5, Docker validation, run-level reset "
                   "and sandboxing are stated. Tip content and use, anti-pattern consumption, KB self-learning "
                   "conflicts, in-batch expiry or rollback, and the prompt text are missing.",
                   ["son55:E007", "son55:E010", "son55:E011", "sol:E004"], ["son55:E011"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. The full 2890 denominator is used and "
                               "runtime passes count as failures. But success is import-level only, and the PLLM "
                               "figure is copied without confirming the same implementation, timeout or LLM.",
                               ["son55:E005", "son55:E006", "son55:E014", "sol:E009"], ["son55:E004"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. Only Level 1 is tabulated (a near-duplicate "
                             "cache, opus:O03), and the authors' text contradicts that row (opus:O01). Co-occurrence "
                             "removal appears only in prose. The 31.9-pp gain over a copied PLLM number is not "
                             "decomposed: KB, Python 2 detector, semantic analyzer and cascade-vs-LLM-first are all "
                             "untested (opus:O05). Tips, shortcuts and runtime KB learning are not separated, and "
                             "there is no same-LLM rerun baseline. Not 0: the store-off row does isolate one retained "
                             "component.",
                             ["son55:E008", "son55:E016", "sol:E008", "opus:O02"],
                             ["son55:E004", "son55:E017", "opus:O01", "opus:O05"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Mitigations are disclosed: about 50 KB entries "
                           "come from a disjoint development subset, co-occurrence data is pre-2020, state resets "
                           "between runs, and no HG2.9K result was used for KB entries. Against that, the design is "
                           "motivated by failure analysis on the evaluation benchmark (including the Python 2 rule), "
                           "the store is built from the evaluated batch, and only one dataset and one LLM are used. "
                           "Not lowered to 1: the test-informed part is a generic rule family rather than "
                           "instance-level tuning, and no oracle signal enters the loop.",
                           ["son55:E012", "son55:E018", "sol:E010", "sol:E011"],
                           ["son55:E002", "son55:E013", "son55:E020"]),
            "E.statistics": R("resolved", 2, "Opus sides with sol (A2 ladder). Ten randomized-order runs with SD (±9.3 "
                              "snippets) and full failure counts go beyond rung 1. There is no interval or "
                              "significance test, the comparator is a single published value, and the ablation has no "
                              "run count or variance, so rung 3 (seeds + intervals + test) is not reached. This "
                              "matches r07a/r08a (cross-run SD, no CI or test → 2).",
                              ["son55:E014", "sol:E007", "sol:E014"], ["opus:O02"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. LLM calls per snippet, the no-LLM share, median and P90 "
                        "latency and hardware are reported. Latency is success-conditioned (opus:O04), the PLLM "
                        "comparison uses that paper's figures on other hardware, and failed or retried builds and "
                        "curation effort are not costed. That is a key fairness gap, not a near-complete ledger.",
                        ["son55:E015", "son55:E019", "sol:E012"], ["son55:E004", "opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (short FSE Companion paper, no appendix). In scope as a boundary "
                  "A-class loop (system_method): Docker-gated solutions and runtime KB mappings are written during a "
                  "batch and reused on later snippets. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Fig. 1 is a pipeline diagram only. All values come from Tables 1–3 and the text.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "The central move is delegation to deterministic solvers with the LLM as last resort.",
                ["son55:E001", "son55:E010"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["decompose_and_delegate", "C25"], ["heterogeneous_decomposition", None]],
                "son55's C25 is primary. sol's failure-partition card is kept as supporting, and sol's "
                "adapt_via_conditioning is dropped (cache reuse, not conditioning).",
                ["son55:E001", "sol:E001", "opus:O03"], NOSCORE),
            XC(p, "local:2604.16941-2", "sol", "partial",
               "A4 collision: sol's local-2 (paired uncertainty for the memory-off gain) stays here: partial, given "
               "ten runs with SD but no ablation variance. son55's local-2 (tips/shortcuts/runtime KB not separately "
               "ablated) moves to local-5 (unmet).", ["sol:E007", "sol:E014"]),
            XC(p, "local:2604.16941-3", "son55", "unmet",
               "Verified: the cascade design comes from failure analysis on HG2.9K itself, with no dev/test split of "
               "the benchmark.", ["son55:E002", "son55:E013"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "revised", "partial",
               "Revised from met: latency is success-conditioned and the comparator is not like-for-like "
               "(opus:O04).", ["son55:E015", "opus:O04"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "Verified: only Level 1 (table) and co-occurrence (prose) are ablated (opus:O05).",
               ["son55:E008", "son55:E016", "opus:O05"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "partial",
               "Verified: the prompt format is summarized and the artifacts are linked.", ["son55:E020"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "unmet",
               "Verified: one benchmark and one LLM.", ["son55:E020"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "unmet",
               "Verified: PLLM number copied, no same-harness LLM-only baseline.", ["son55:E004", "son55:E021"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "met",
               "Verified: the failure categories justify the decomposition, although they were derived on the "
               "evaluation set (scored in E.holdout).", ["son55:E002", "son55:E013"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "sol", "partial",
               "Verified: deployment latency and calls are given, without cost parity.", ["sol:E012", "sol:E013"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "sol", "partial",
               "Verified: one branch is isolated and the interacting components are unablated.", ["sol:E008"]),
            XC(p, "rsi:index_experience_for_reuse/F1", "son55", "partial",
               "Verified: the store carries about 5 of 31.9 pp, and the rest is the static cascade.",
               ["son55:E008", "son55:E022"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unmet",
               "Verified: the store accumulates over the evaluated batch. Order randomization does not separate "
               "construction from evaluation.", ["son55:E009", "son55:E018"]),
            XC(p, "rsi:index_experience_for_reuse/F4", "son55", "met",
               "Verified: Docker-build validation gates shortcut writes.", ["son55:E010"]),
            XC(p, "rsi:index_experience_for_reuse/H03", "sol", "partial",
               "Verified: Docker-gated cases with a no-memory contrast, built on the test stream.",
               ["sol:E004", "sol:E008", "sol:E011"]),
            XC(p, "rsi:index_experience_for_reuse/S1", "son55", "partial",
               "Verified: a case is a full pip solution keyed by import set, and partial matches only yield hints.",
               ["son55:E011", "son55:E009"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "met",
               "Verified: writes are Docker-validated and sandboxed.", ["son55:E010"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "Verified: Level 1 OFF −5.0 pp, a single value contradicted by the authors' own text (opus:O01).",
               ["son55:E008", "opus:O01"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the gain is driven by static knowledge, and the memory's role is thin and "
                "self-contradicted.", ["son55:E009", "son55:E011", "opus:O01"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality: one cache ablation against a copied baseline, with most components "
                "unablated.", ["son55:E008", "opus:O05"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 2,
                "See ratings.E.statistics: cross-run SD without CI or test is rung 2 (A2; r07a/r08a).",
                ["sol:E007", "son55:E014"], "−1.25 vs son55 (5×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", 2,
                "See ratings.E.cost: success-conditioned latency and a non-matched comparator.",
                ["sol:E012", "opus:O04"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope (boundary); "
                                                   "retained in the narrow store-off sense; most gain from static "
                                                   "curated knowledge. G 2, M 2, X 2, Em 2, Ec 1, Eh 1–2, Es 2, "
                                                   "cost 1–2. Noted the Level 1 text/table contradiction.",
            "integrity_checks": "Both seats a1 on 2604.16941v1, material sha 30e563f8…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: the full cascade resolves 86.6% (10-run mean) on HG2.9K, "
                                "and a within-batch Docker-validated cache adds 5 pp over the same pipeline without "
                                "it. Superiority over PLLM is against a copied number and is not decomposed. "
                                "claim_support scoped.",
            "shared_error_review": "Agreed items (G 2, X 2, Em 2, Eh 2, evidence_level retained) re-checked and "
                                   "kept. E.holdout was considered for 1 (design informed by HG2.9K failure analysis) "
                                   "but kept at 2: generic rule family, declared KB provenance, no oracle signal.",
            "rating_agreement": "M and E.causality → son55; E.statistics and E.cost → sol. Final 46.25.",
        },
    }

    # =========================================================== 2604.17399 MC² (sol 63.75 / son55 61.25)
    p = "2604.17399"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "93.07 ( ± 1.60 \\pm 1.60 )", "§3 Table 1, Qwen3-8B MATH-500, MC² cell",
                    "MC² 93.07 ± 1.60 against Meta Prompt 91.93 ± 1.52 (opus:O02). The 95% CIs overlap, so 'best "
                    "accuracy across all combinations' is not statistically separated in this cell.",
                    kind="our_inference"),
            opus_ev(p, "O02", "91.93 ( ± 1.52 \\pm 1.52 )", "§3 Table 1, Qwen3-8B MATH-500, Meta Prompt cell",
                    "Strongest baseline in that cell.", kind="author_report"),
            opus_ev(p, "O03", "45.33 ( ± 5.74 \\pm 5.74 )", "§3 Table 1, Llama-3.1-8B Game-of-24, MC² cell",
                    "MC² 45.33 ± 5.74 against Meta Prompt 41.00 ± 8.96 (opus:O04). The CIs overlap on 100 problems.",
                    kind="our_inference"),
            opus_ev(p, "O04", "41.00 ( ± 8.96 \\pm 8.96 )", "§3 Table 1, Llama-3.1-8B Game-of-24, Meta Prompt cell",
                    "Strongest baseline in that cell.", kind="author_report"),
            opus_ev(p, "O05", "R+ M + C 79.20 47.38", "§4.3 Table 2, GPT-4o-mini",
                    "The store-off arm (MRO without MCA) is one value per cell with no interval, while Table 1 uses "
                    "three seeds. The retained-memory evidence (79.20 → 85.13 MATH-500) has no uncertainty.",
                    kind="our_inference"),
            opus_ev(p, "O06", "The composer itself is realized by a dedicated prompt template (see Appendix I ) and "
                              "is executed by calling the backbone model",
                    "App C.3 MRO role strategy update",
                    "Each instance triggers a per-role backbone call to compose prompts (Eq. 13), on top of batch "
                    "distillation and consolidation. The paper does not say whether Table 1's '#Tokens' (decoding "
                    "tokens) includes these calls or input tokens.", kind="our_inference"),
            opus_ev(p, "O07", "Domain-Specific Tactic (Residue Theorem Application)", "App H.2 Table 10",
                    "The distilled store includes domain tactics (residue expansion), not only meta-level "
                    "monitoring/control habits. This weakens the paper's 'meta-level, not task-level' distinction from "
                    "ReasoningBank/BoT, the residual that the gap rests on.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering",
                                                                "heterogeneous_decomposition"],
            "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning primary, sub null (frozen backbone conditioned on retrieved "
                      "lessons and compiled role prompts; no C03 schema or upstream phase). Supporting cards, both "
                      "low fit, are unioned: son55's self_supervised_signal_engineering (the S+/S− proxy selection "
                      "of what to distil, alongside the gold correctness tag) and sol's heterogeneous_decomposition "
                      "(role-separated trace and memory streams).",
            "matches": [smatch("son55", p, "adapt_via_conditioning", role="primary"),
                        smatch("son55", p, "self_supervised_signal_engineering", role="supporting"),
                        smatch("sol", p, "heterogeneous_decomposition", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.17399-1"): "local:2604.17399-5",
                    ("son55", "local:2604.17399-2"): "local:2604.17399-6",
                    ("son55", "local:2604.17399-3"): "local:2604.17399-7"},
            overrides={
                "local:2604.17399-2": {
                    "reason": "Opus: three seeds with 95% CIs on Table 1. There is no significance test, two best cells "
                              "overlap the strongest baseline (opus:O01–O04), and the ablation, trajectory and "
                              "iteration tables are single runs (opus:O05). Partial."},
                "local:2604.17399-5": renum("son55:local:2604.17399-1"),
                "local:2604.17399-6": renum("son55:local:2604.17399-2"),
                "local:2604.17399-7": renum("son55:local:2604.17399-3"),
            }),
        "claims": lambda c: add_counter(add_counter(add_counter(c, "C1", ["opus:O01", "opus:O03"]), "C3",
                                                    ["opus:O05"]), "C4", ["opus:O07"]),
        "assessment": assess("son55", p, [
            "Opus: two 'best' cells overlap the strongest baseline's CI (opus:O01–O04); the store-off ablation is "
            "single-run (opus:O05).",
            "Opus: per-instance composer calls may be missing from the token comparison (opus:O06)."],
            evidence_level="retained",
            evidence_level_note="Both seats retained, kept and scoped. Lessons written after earlier batches are "
                                "read on later, different items of a single stream pass, and there is a store-off arm "
                                "(R+M+C vs Full). Run precedent (r15b Evo-MedAgent, r06a SWE-Exp) admits same-stream "
                                "store-off evidence as retained. The correctness labels of earlier test items enter "
                                "the store, and the experience curve uses repeated passes; these are scored in "
                                "E.holdout = 1. The repeated-pass curve on its own would be task.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The gap (episodic meta-reasoning with no cross-instance "
                   "carryover) is real and the changed object (role prompts plus meta-knowledge) is clear. But the "
                   "closest cross-instance memory neighbours (Reflexion, ReasoningBank) are not compared, BoT is "
                   "re-implemented best-effort, and the residual 'meta-level not task-level' distinction is asserted. "
                   "The paper's own Table 10 lists domain tactics in the store (opus:O07).",
                   ["son55:E001", "son55:E003", "son55:E025"], ["opus:O07"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. The Reasoner/Monitor/Controller factorization gives "
                   "attributable traces. The chain reflections → batch micro-lessons from best and worst sets → "
                   "windowed global rules → retrieved lessons compiled into role prompts is reconstructable and makes "
                   "testable predictions. The 'no ground truth' framing conflicts with label use, and LLM rewrite "
                   "quality is unchecked.",
                   ["son55:E002", "son55:E004", "son55:E009", "son55:E016", "sol:E005"], ["son55:E005"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithm 1, batch-size rule, w=3/k=3, embedding model, "
                   "trace schema, deterministic reflection heuristics, composer validity checks with fallback, and "
                   "window forgetting are all specified. There is no utility gate or rollback, conflict resolution is "
                   "left to an LLM rewrite, and the App I prompt boxes are empty in the pinned HTML (rendering gap).",
                   ["son55:E008", "son55:E009", "son55:E010", "son55:E024", "sol:E006", "sol:E007"], ["son55:E027"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Standard accuracy with unified answer "
                               "parsing, failures counted, and token counts for all methods. Baselines are "
                               "re-implemented best-effort (TTPI missing on Gemini, Meta-Prompting without the "
                               "interpreter).",
                               ["son55:E011", "son55:E012", "sol:E011"], ["son55:E013", "son55:E014"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. The ablation ladder includes a store-off arm "
                             "(R+M+C 79.20 vs Full 85.13 on GPT-4o-mini MATH-500, opus:O05). Missing: a label-free "
                             "variant to test the stated claim, a static-optimized-prompt or shuffled-lesson control, "
                             "label-using memory baselines (Reflexion/ReasoningBank) at matched calls, and an S+/S− "
                             "ablation. The 'grows with experience' curve uses repeated passes.",
                             ["son55:E016", "sol:E008", "opus:O05"],
                             ["son55:E005", "son55:E015", "son55:E025", "sol:E009"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The adaptation stream is the evaluation stream, "
                           "and the correctness labels of earlier test items enter the reflections despite the 'no "
                           "ground truth' framing (App C.1/C.4). The experience curve reuses the same problems over "
                           "passes, transfer is a warm-start that keeps adapting on the target, and there is no "
                           "frozen-store or held-out split.",
                           ["son55:E019", "son55:E017", "sol:E003", "sol:E004"],
                           ["son55:E005", "son55:E006", "son55:E007", "sol:E009", "sol:E014"]),
            "E.statistics": R("resolved", 2, "Shared correction (both seats 3). The frozen A2 ladder requires seeds + "
                              "intervals + significance test for 3. Table 1 has three seeds and 95% CIs but no test "
                              "of the main comparisons. The Spearman test concerns the proxy, not the effect. Two "
                              "'best' cells overlap the strongest baseline (opus:O01–O04), and the ablation, "
                              "trajectory, iteration and transfer tables are single runs (opus:O05). Run precedent: "
                              "r14a 2603.23129 and cal-h1 2310.02304 (runs with CIs, no tests → 2).",
                              ["son55:E012", "sol:E010", "sol:E013", "son55:E019"],
                              ["opus:O01", "opus:O03", "opus:O05"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Decoding tokens per instance are reported for every "
                        "method and dataset, which is a per-variant ledger, and an iteration-budget sweep is given. "
                        "Whether per-instance composer calls, distillation, consolidation and input tokens are "
                        "counted is unstated (opus:O06), and there is no matched-compute comparison against "
                        "label-using memory methods. Consistent with r15b Autogenesis/EvoRAG (per-variant ledger with "
                        "a key gap → 2).",
                        ["son55:E021", "son55:E022", "sol:E016", "sol:E018"], ["opus:O06"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (App A–I; App I prompt boxes empty in the HTML). In scope "
                  "(system_method): role prompts and meta-knowledge (non-weight) are consolidated from execution "
                  "traces and read in later batches. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Fig. 3 (time evolution) and Fig. 6 (similarity) are image-only. Fig. 3's values are "
                             "taken from the text (84% → 88%, 33.1% → 30.8%). The App I prompt figures are empty.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", None], ["self_supervised_signal_engineering", None],
                 ["heterogeneous_decomposition", None]],
                "Same primary in both seats. The low-fit supporting cards are unioned (S+/S− proxy; role streams).",
                ["son55:E004", "sol:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"]],
                "H00 fits: best/worst contrast distilled into trigger-conditioned DO/AVOID lessons. H01 needs an "
                "explicit edit vocabulary, but MC²'s consolidator rewrites K_b by LLM ('merging ... rewriting the "
                "remaining rules'), which is the monolithic rewrite H01 warns against.",
                ["son55:E004", "son55:E010", "sol:E005"], NOSCORE),
            XC(p, "local:2604.17399-1", "sol", "partial",
               "A4 collision: sol's local-1 (first-try proxy vs correctness) stays here: partial (Spearman and "
               "difficulty checks). son55's local-1 (evaluation-stream updates) moves to local-5 (unmet).",
               ["sol:E017", "son55:E026"]),
            XC(p, "local:2604.17399-2", "sol", "partial",
               "A4 collision: sol's local-2 (statistics) stays here: partial, consistent with E.statistics 2. "
               "son55's local-2 ('no ground truth' claim) moves to local-6 (unmet).",
               ["sol:E010", "opus:O01", "opus:O05"]),
            XC(p, "local:2604.17399-3", "sol", "partial",
               "A4 collision: sol's local-3 (cost ledger) stays here: partial. son55's local-3 (label-using memory "
               "baselines) moves to local-7 (unmet).", ["sol:E016", "opus:O06"]),
            XC(p, "local:2604.17399-4", "son55", "unknown",
               "Verified: whether #Tokens includes the composer, distiller and consolidator calls is not stated "
               "(opus:O06).", ["son55:E021", "opus:O06"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: CoT-SC/ToT/BoT are compared, but there is no longer-context or label-using memory "
               "baseline.", ["son55:E013", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: the roles, micro-update and hierarchy are ablated. S+/S−, w, k and the composer are not.",
               ["son55:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: four benchmarks and four backbones, all within-task, with preliminary transfer.",
               ["son55:E011", "son55:E017"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: an order-shuffle check and a single-run iteration sweep. No lesson-quality sensitivity.",
               ["son55:E019", "son55:E023"]),
            XC(p, "rsi:abstract_experience_into_guidance/F5", "son55", "partial",
               "Verified: outcome-tagged traces, with role self-assessment as the selection proxy.",
               ["son55:E004", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00", "sol", "partial",
               "Verified: role lessons, negative cases and a memory-off control are present. Construction is not "
               "isolated from the test stream.", ["sol:E005", "sol:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "son55", "met",
               "Verified: the fixed assumption (episodic, static role prompts) is named.", ["son55:E001", "son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: best/worst sets within a batch, not paired on the same task.", ["son55:E004"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
               "Verified: monitor/controller behaviour plus a correctness tag. The judge's imperfection is checked by "
               "one correlation only.", ["son55:E004", "son55:E005", "son55:E026"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "met",
               "Verified: windowed consolidation with decay.", ["son55:E009", "son55:E010"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: only format/length validity with fallback, no utility gate.", ["son55:E008"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: nearest memory neighbours are uncompared, and Table 10 undercuts the meta-level "
                "residual (opus:O07).", ["son55:E003", "son55:E025", "opus:O07"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 2,
                "See ratings.E.cost: a per-variant decoding-token ledger exists. Auxiliary-call inclusion is the key "
                "gap (opus:O06).", ["son55:E021", "opus:O06"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.statistics", "sol_value": 3, "son55_value": 3, "final_value": 2,
             "reason": "Frozen A2 ladder: rung 3 needs multi-seed results, intervals and a significance test. Table 1 "
                       "has seeds and CIs but no test of the main comparisons, two 'best' cells overlap the strongest "
                       "baseline (opus:O01–O04), and the retained-memory ablation is a single run (opus:O05). Same "
                       "rung as r14a 2603.23129 and cal-h1 2310.02304.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05"],
             "score_impact": "−1.25 vs both seats (5×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text with appendices first. Initial view: in "
                                                   "scope; retained (same-stream store-off) with label leakage into "
                                                   "the store. G 2, M 3, X 3, Em 3, Ec 2, Eh 1, Es 2, cost 1–2.",
            "integrity_checks": "Both seats a1 on 2604.17399v1, material sha ebc3d815…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: on the evaluated stream, with correctness-tagged feedback, "
                                "prompt-level consolidation raises later-batch accuracy over the same role loop "
                                "without memory (single-run ablation). 'Without ground truth' is contradicted by App "
                                "C.1/C.4, and 'best everywhere' is not separated in two cells. claim_support scoped.",
            "shared_error_review": "Both seats' E.statistics 3 is corrected to 2 (A2). Other agreed items (M 3, X 3, "
                                   "Em 3, Ec 2, Eh 1, evidence_level retained) re-checked and kept.",
            "rating_agreement": "G and E.cost → son55; E.statistics shared correction. Final 60.0.",
        },
    }

    # =========================================================== 2604.17488 AutoVQA-G (sol 50.0 / son55 47.5)
    p = "2604.17488"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "AutoVQA-G 0.735 0.819 0.896 0.634 0.720 0.747", "§3.1.2 Table 2, Visual7W AutoVQA-G row",
                    "On VQA metrics AutoVQA-G is below the tool-matched single-pass GPT-4o (opus:O02): TIFA 0.819 vs "
                    "0.908, VQAScore 0.896 vs 0.923. The overall VQA-G lead comes from grounding (mIoU 0.634 vs "
                    "0.455), so 'competitive VQA quality' is generous.", kind="our_inference"),
            opus_ev(p, "O02", "GPT-4o (ZS, tool-assisted) 0.733 0.908 0.923 0.455 0.510 0.669",
                    "§3.1.2 Table 2, Visual7W tool-matched baseline row", "Tool-matched single-pass baseline.",
                    kind="author_report"),
            opus_ev(p, "O03", "(4) w/o Memory 0.885 0.582", "§3.2.3 Table 3",
                    "The only memory-specific evidence is a single-run, within-image ablation (mIoU 0.634 → 0.582). "
                    "No cross-image use of the rubric or memory is evaluated.", kind="author_report"),
            opus_ev(p, "O04", "iteratively refines VQA-G data for an input image", "Fig. 1 caption",
                    "The loop is described per image, and nothing states that rubrics or memory carry across images. "
                    "The retained change (the rubric edit) persists only into the next regeneration of the same "
                    "image. That is the Reflexion boundary (cal-dev 2303.11366: within-instance retention → in scope, "
                    "task), not single-output self-correction, because a prompt component is edited and carried into "
                    "a new attempt.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus: AutoVQA-G is a data-synthesis pipeline whose load-bearing element is a verifier gate on "
                      "generated annotations. That is C08 (generator plus one quality gate), the data side only, since "
                      "no learner is retrained (son55). The rubric edits reach the frozen generator as prompt "
                      "conditioning, so adapt_via_conditioning (sol) is kept as supporting. Dropped as low fit: "
                      "son55's decompose_and_delegate/C25 (detector and judge are not sound solvers, as son55 itself "
                      "notes) and sol's heterogeneous_decomposition (functional modules, not a partition of one "
                      "resource by a property).",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", role="primary"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H10")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"].get("revision_proposals", [])},
        "pattern_mapping": [
            PM("self_supervised_signal_engineering", "C08", "attribute_and_patch_incumbent", "H10",
               "The verifier critique of a failed draft is routed to one of three module rubrics, which is rewritten, "
               "and the image is regenerated under the patched rubric. Accepted drafts form the synthetic dataset.",
               "H10 patches an incumbent artifact across tasks. Here the patch serves one image's next attempts "
               "(S4/S6 unmet), and the certifying signal is a VLM judge (F4 partial).",
               ["son55:E005", "son55:E006", "sol:E004", "opus:O04"]),
            pmap("sol", p, 0),
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.17488-1"): "local:2604.17488-4",
                    ("son55", "local:2604.17488-2"): "local:2604.17488-5",
                    ("son55", "local:2604.17488-3"): "local:2604.17488-6"},
            overrides={
                "local:2604.17488-1": {
                    "status": "unmet",
                    "reason": "Opus (revised from partial): no fixed-question or coverage-controlled comparison is "
                              "run. The authors say the loop 'selects for less ambiguous queries', so item sets differ "
                              "per method."},
                "local:2604.17488-2": {
                    "status": "unmet",
                    "reason": "Opus (revised from partial): sample sizes are given, but no interval, seed, agreement "
                              "or test exists for any comparison, so the requirement is unanswered."},
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "partial",
                    "reason": "Opus (son55's partial over sol's unmet): best-of selection over attempts and attempt "
                              "memory against cyclic edits protect earlier wins at the output level. There is no "
                              "per-edit improvement gate or regression check across samples."},
                "local:2604.17488-4": renum("son55:local:2604.17488-1"),
                "local:2604.17488-5": renum("son55:local:2604.17488-2"),
                "local:2604.17488-6": renum("son55:local:2604.17488-3"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01"]), "C2", ["opus:O03", "opus:O04"]),
        "assessment": assess("son55", p, [
            "Opus: VQA metrics are below the tool-matched baseline. The overall lead is grounding-driven (opus:O01).",
            "Opus: rubric/memory persistence across images is unspecified. Treated as within-instance (opus:O04)."],
            evidence_level="task",
            evidence_level_note="Both seats task, kept. The rubric edit carries into the next regeneration of the same "
                                "image only (opus:O04). No retained change is shown to help later images.",
            claim_support="scoped"),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The limitation (single-pass hallucination, heuristic "
                   "verification) is concrete and the changed object (per-sample generation rubrics driven by a CoT "
                   "verifier) is clear. Neighbours get one sentence each, and no prompt-optimizer lineage (OPRO/"
                   "TextGrad-style) or prior agentic annotation framework is compared.",
                   ["son55:E003", "son55:E004", "sol:E001"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Generate–verify–critique–route–refine with attempt memory "
                   "is coherent and each part is ablated. Nothing argues why critique-driven rubric edits beat plain "
                   "verifier-filtered resampling, and the update operator ⊎ is unspecified.",
                   ["son55:E001", "son55:E005", "son55:E006", "sol:E003"], ["son55:E011"]),
            "X": R("resolved", 2, "Opus sides with son55. The equations, τ=0.9, 0.7/0.3 weights, five-iteration cap, "
                   "best-of selection, models and a released-code link are given. Missing are how rubric edits are "
                   "applied and bounded (⊎ undefined), whether rubrics and memory reset per image or persist (the "
                   "retention lifecycle, opus:O04), the handling of the ~8–11% non-accepted items, and any versioning "
                   "or rollback beyond best-of. Anchor 2: the main steps are described, but retention and interface "
                   "conditions are unclear.",
                   ["son55:E005", "son55:E006", "son55:E008", "sol:E003", "sol:E006"], ["son55:E004", "opus:O04"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Human re-annotation of grounding (500 per "
                               "method/dataset) and three automatic VQA metrics are reported. The annotator protocol "
                               "and agreement are missing, items differ per method and are verifier-selected for "
                               "unambiguity, beating the human annotations shows consistency rather than "
                               "correctness, and AutoVQA-G is below the tool-matched baseline on TIFA/VQAScore "
                               "(opus:O01).",
                               ["son55:E013", "sol:E007", "opus:O02"], ["son55:E015", "son55:E016", "opus:O01"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. A tool-matched single-pass GPT-4o baseline and "
                             "four ablations show that the loop and verifier matter. Not isolated: prompt "
                             "optimization vs verifier-filtered resampling at five attempts, rejected-item "
                             "survivorship, and the GPT-4o CoT/Gemini rows that lack the grounding tool. Memory "
                             "evidence is one within-image row (opus:O03).",
                             ["son55:E011", "son55:E018", "sol:E008", "opus:O03"],
                             ["son55:E012", "son55:E015"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. The quality claim is evaluated by fresh human "
                           "re-annotation, independent of the in-loop verifier, and no oracle or ground-truth signal "
                           "enters the loop. The verifier's same-image selection is a deployable best-of-5, not "
                           "leakage. Hyperparameters were tuned on an unspecified validation set, only two datasets "
                           "are used, and the 'facilitate VLM training' and 'improve over time' claims are untested. "
                           "Those limit the claim scope (claim_support scoped, evidence task) but do not show "
                           "contamination.",
                           ["son55:E008", "son55:E013", "sol:E006"], ["son55:E021", "sol:E002"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder). Sample sizes (500 per cell) and negative VQA "
                              "metrics are reported. No intervals, seeds, agreement or tests, and ablations are single "
                              "runs.",
                              ["son55:E013", "son55:E019", "sol:E007"], ["son55:E018"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Iterations and tokens per success are reported for "
                        "AutoVQA-G only, despite up to five iterations with a 72B verifier and an API optimizer against "
                        "single-pass baselines. There is no baseline cost and no failure-inclusive or matched-budget "
                        "accounting, although the paper claims cost-effectiveness.",
                        ["son55:E019", "sol:E011"], ["son55:E020", "sol:E013"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (4-page ICASSP paper, no appendix). In scope as a boundary "
                  "A-class loop (system_method): a prompt component (generation rubric) is edited from verifier "
                  "critiques and carried into the next attempt. It is retained only within one image (Reflexion "
                  "cal-dev precedent), so no cross-sample retention is credited. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats reviewed). Within-instance boundary per Reflexion cal-dev precedent "
              "(opus:O04)",
        "figure_dependence": "Fig. 2 is qualitative only. All values come from Tables 1–3.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "A verifier-gated synthetic-data pipeline (C08, data side).", ["son55:E001", "son55:E018"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", "C08"], ["adapt_via_conditioning", None]],
                "C08 is primary and rubric conditioning supporting. C25 and heterogeneous_decomposition are dropped "
                "as low fit.", ["son55:E001", "sol:E003"], NOSCORE),
            XC(p, "local:2604.17488-1", "revised", "unmet",
               "A4 collision: sol's local-1 (fixed-question/coverage comparison) stays here, revised to unmet "
               "because no such comparison exists. son55's local-1 (resampling baseline) moves to local-4 (unmet).",
               ["sol:E009", "son55:E015"]),
            XC(p, "local:2604.17488-2", "revised", "unmet",
               "A4 collision: sol's local-2 (statistics) stays here, revised to unmet (no uncertainty at all). "
               "son55's local-2 (annotator protocol) moves to local-5 (unmet).", ["sol:E007", "son55:E013"]),
            XC(p, "local:2604.17488-3", "sol", "partial",
               "A4 collision: sol's local-3 (cost ledger) stays here: partial (success-conditioned tokens and "
               "iterations). son55's local-3 (downstream VLM training) moves to local-6 (unmet).",
               ["sol:E011", "sol:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "Verified: the loop, history and routing are removed, but there is no equal-retry frozen-rubric "
               "control.", ["sol:E008", "sol:E010"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "sol", "partial",
               "Verified: two datasets, same-image optimization only.", ["sol:E002", "sol:E006"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "partial",
               "Verified: two datasets of one family, no OOD or downstream test.", ["son55:E010", "son55:E021"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "partial",
               "Verified: a tool-matched baseline and ablations, but no compute-matched best-of-N.",
               ["son55:E011", "son55:E018"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "unmet",
               "Verified: no VLM is trained on the data.", ["son55:E021"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-4", "son55", "partial",
               "Verified: compared with VLMs, not with prior agentic annotation frameworks.",
               ["son55:E003", "son55:E011"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "partial",
               "Verified: per-success cost for AutoVQA-G only.", ["son55:E019", "son55:E020"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial",
               "Verified: real images and human re-annotation, on verifier-selected items.",
               ["son55:E013", "son55:E015"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F1", "son55", "unmet",
               "Verified: a domain annotation pipeline that applies a standard critique-rewrite loop.",
               ["son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "sol", "partial",
               "There is no ground truth in the loop (failure present), but the certifying judge (Qwen2.5-VL 72B) is "
               "a different family from the proposer (DeepSeek V3) and generator (MiniCPM), and grounding is "
               "checked post hoc by human re-annotation. So the card's same-family failure is only partly present: "
               "partial, not unmet.", ["sol:E007", "son55:E001", "son55:E013"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Best-of selection over attempts and attempt memory against cyclic edits protect earlier wins at the "
               "output level. There is no per-edit improvement gate, so partial, not unmet.",
               ["son55:E005", "son55:E008"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "unmet",
               "Verified: diagnosis is per image, with no clustering across images.", ["son55:E005"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "unmet",
               "Verified: a task-specific pipeline whose rubrics are not carried across images.",
               ["son55:E004", "son55:E005"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2,
                "See ratings.X: ⊎ is undefined and the retention lifecycle is unspecified.",
                ["son55:E005", "son55:E008", "opus:O04"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 2,
                "See ratings.E.holdout: independent human evaluation and no oracle in the loop. The limits are on "
                "scope, not contamination.", ["son55:E013", "son55:E008"], "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: within-instance "
                                                   "rubric refinement, Reflexion-type boundary → in scope, task. G 2, "
                                                   "M 2, X 2, Em 2, Ec 2, Eh 2, Es 1, cost 1.",
            "integrity_checks": "Both seats a1 on 2604.17488v1, material sha 9c328dec…; canonical seat hashes equal "
                                "conflicts.json; RS/domain ids valid; both claim_type system_method.",
            "core_claim_check": "Strongest supported claim: with the same grounding tool, a verifier-driven per-image "
                                "loop produces annotations with higher human-re-annotation IoU than single-pass GPT-4o "
                                "on two datasets, while its VQA metrics trail. claim_support scoped.",
            "shared_error_review": "Scope re-checked against the 'single-output self-correction' exclusion and kept "
                                   "in scope under the Reflexion precedent. Agreed ratings re-checked and kept.",
            "rating_agreement": "X and E.holdout → son55. Final 47.5.",
        },
    }

    return S
