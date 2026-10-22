"""Opus rulings for r20a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2605.10064 MAGE (seat Δ13.75): final 43.75 = son55 on every disputed rating (X 2, E.measurement 1, "
        "E.causality 1, E.holdout 2). son55's flagged inconsistencies are confirmed: Table 14 accuracies differ from "
        "Table 1 (GSM8K 84.2 vs 88.2, STBench 51.8 vs 54.8/57.8, RealMath 82.5 vs 85.1; Reflexion 12.0/11.5 vs 37.0/34.5), "
        "Table 4 gives 52 runs / 2.12% while §4.3 and Appendix N give 1.91% over thirty-six runs (the per-benchmark run "
        "counts sum to 42). Opus adds two contradictions neither seat recorded: Tables 12/13 put Crafter peaks at "
        "23.4/22.7/22.7 (Llama) and 25.3/26.8/24.0 (Qwen), at or below the 25.5 standalone reference that §4.2 says every "
        "teacher configuration beats (Table 3: 33.5/37.9/34.8); Appendix Q says the Table 2 headline FinQA/MedQA values "
        "are 64.0–64.5 / 68.5, while Table 2 shows 67.5/74.6. The judge that scores the held-out pool is the same Sonnet "
        "4.6 Critic that admits success memories during evolution. Causality: the only memory ablation is success-off; "
        "Table 17 shows 87% new-question accuracy at iteration 0 (no success memories yet) against a 64.5 0-shot base, so "
        "most of the gain may be scaffold, and no teacher-information-matched retrieval baseline exists. Domain → son55 "
        "H03 (flat task-filtered top-K over gated cases; Eq. 3 never reads the graph structure) + H00.",
        "2605.10332 EmbodiSkill (seats tied at 57.5): every rating re-checked against the short paper (no appendix, "
        "no prompts); all eight confirmed, final 57.5. Shared facts verified: relative gains are reported as '%' "
        "(93.28/70.89 = +31.58%); Table 3's Qwen3.5-27B/Gemini row gains only +1.49; Mem0 at 12.69 with four zero "
        "sub-categories on Qwen2.5-14B is below no-memory (46.27), a baseline-integration warning recorded under "
        "E.causality. The 93.28% headline equals the peak of the 10-stage test curve ('reaches 93.28% during evolution, "
        "after which it remains in a high performance range'), so stage selection on test is unmet, not unknown; it "
        "keeps E.holdout at 2 (instance split + frozen skill exist). E.cost not_reported 0 (no token/call/trajectory "
        "counts anywhere). Only expectation-ID hygiene changed.",
        "2605.10366 EGL-SCA (Δ5): final 60.0. G → son55 2: the paper's own Table 7 describes GEPA as 'Evaluator-guided "
        "prompt and program refinement', contradicting the gap that prior work evolves one side in isolation, and "
        "tool-making neighbours are not discussed. E.holdout → son55 2: the four external benchmarks are 200-case "
        "subsets restricted to task kinds that mirror the 19 training families (GraphArena = common_neighbors + tsp; "
        "G-Real = coloring/tsp/vertex_cover). E.cost → sol 2: the main run's own tokens/calls/wall-clock are reported in "
        "detail, but no baseline or ablation budget, and the budget statement itself conflicts (Appendix A: 200 "
        "episodes; Table 2/17: 300). Shared correction E.measurement 3 → 2 (run convention for internal "
        "contradictions): 200 vs 300 episodes, '100% activation' vs 26/27 exercised, Appendix D's '300-episode agent "
        "routinely masters' G-Real vs 0.795 < 0.810, and Table 1(b)'s '2 accepted instruction mutations' (the "
        "anti-thrashing evidence) vs 17–22 per SCA seed run in Table 10 — the same order as the 22 attributed to "
        "w/o-SCA thrashing. RS → son55 C25 primary (typed task_input → verified solver → credit-assigning verifier "
        "loop; w/o Tool Use −0.54) + heterogeneous_decomposition supporting.",
        "2605.11136 EvoChamber (Δ5): final 55.0. M → son55 2: the asymmetric-routing story is asserted, Appendix L says "
        "'most insights are classified as cross-domain', and niche specialisation follows by construction from "
        "metadata niche labels + per-niche EWMA. X → son55 3: Table 9 and E.1 specify every operator and threshold. "
        "E.measurement → sol 2 (cap): Hard Code is 422 tasks in §4.1 but the 0.757 headline averages 586 including "
        "saturated HumanEval; Appendix I's 0.302 math_hard base contradicts Table 2's 0.374. E.holdout → sol 1: "
        "accuracy is prequential on the stream whose gold rewards drive CoDream, competence and lifecycle (A2 oracle "
        "signal), no frozen-state test. E.statistics → son55 1: no uncertainty on any main or ablation result; the "
        "three Hard Math orderings are robustness, not error bars. E.cost → son55 2 (3.6× SA, 72% of SC tokens). "
        "Removing CoDream drops HotpotQA/DROP to 0.572/0.480, far below SA (0.791/0.800), so that ablation removes "
        "more than CoDream; kept at E.causality 2 with the Appendix F isolation.",
        "2605.13941 EvolveMem (Δ2.5): final 36.25, below both seats; each item decided separately. Evolution "
        "optimises F on the evaluation questions with ground truth and returns θ* = argmax_r f_r on that set; "
        "MemBench is evolved on its 28 test samples; the only zero-shot number (C_L on MemBench 0.543) equals its "
        "LoCoMo value, is not a multiple of 1/28 and is below RecentMem/MemGPT 57.1 → E.holdout 0 (sol). Table 6: "
        "'− Self-evolution' costs only 2.03 of the 23.8-point trajectory, hand-built extraction guards carry −23.22, "
        "and extraction always uses GPT-5.1 → E.causality 1 (son55). Answer prompts enforce token-F1 surface formats "
        "(never 'Unknown', Arabic numerals, 'and' connector worth 0.06 F1) → E.measurement 1 (son55). M → son55 2: "
        "'entirely new dimensions' contradicts 'Fields MUST match RetrievalConfig field names exactly' and the "
        "diagnosis rubric/Tier-1 TODO list pre-names entity-swap, verification and LoCoMo flags. X revised to 2: the "
        "action space, thresholds and prompts are reconstructable, but Algorithm 1's stop rule (break when "
        "f_r − f_{r−1} < ε) cannot produce the reported trajectory with drops at R2 and R5, and Algorithm 2's online "
        "loop has no ground-truth signal. E.cost → sol 1 (per-round 15–20 min vs 25–35 min for seven rounds). RS → "
        "son55 outside_taxonomy (run precedent r08b/r09b/cal-dev GrIPS: configuration/prompt search has no main "
        "card). Domain → son55 H12 + sol H21; H17 and H04 kept only as check questions.",
        "A4 hygiene. Hidden collisions renumbered (same ID, different question): 10064 son55 local-2 → local-6; 10332 "
        "son55 local-1 → local-4, local-3 → local-5; 10366 son55 local-1 → local-4, local-2 → local-5; 11136 son55 "
        "local-1 → local-4, local-2 → local-5; 13941 son55 local-2 → local-6, local-3 → local-7. Same-question pairs "
        "merged: 10064 son55 local-1 → local-3; 10332 son55 local-2 → local-3; 11136 local-3; 13941 local-1 and "
        "local-4. son55 used 'challenged_with_evidence' for 'the paper's claim is contradicted'; that status is "
        "reserved for an author challenging the expectation, so those entries are recorded as unmet.",
        "Expectations from cards not kept as pattern matches stay as check questions with a note; they never score "
        "(13941: generative_process_redesign RE-*, H04, H17/S6, population S2; 10064: evidence_gated_retention S2).",
        "Figure dependence: MAGE Figures 1–3, EmbodiSkill Figures 1–3 (incl. the stage curve), EGL-SCA Figure 3, "
        "EvoChamber Figures 1–3, EvolveMem Figures 1–2 are image-only in the pinned text; no value was read from an "
        "image. No material requests: the seats' requests for neighbour originals (A-Mem/MemRL/EvolveR, "
        "Trace2Skill/EvoSkills) are non-blocking for every disputed rating.",
        "Card revision proposal (stage end, not applied): add to index_experience_for_reuse H04 a failure check that "
        "a graph/structured store whose retrieval rule is flat task-filtered top-K (MAGE Eq. 3) should be assigned "
        "H03, not H04.",
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

    def RC(p, k, dec, final, reason, ev=(), impact=""):
        return res(f"ratings.{k}", *C(p, f"ratings.{k}"), dec, {"status": "resolved", "rating": final}, reason, ev,
                   impact)

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

    def base_block(s, p, key, **upd):
        b = prefix(copy.deepcopy(seat(s, p)[key]), s)
        b.update(upd)
        return b

    def amend(claims, cid, counter=(), **fields):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(counter)
                c.update(fields)
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

    def dropped(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on *_pattern)."}

    def renum_chal(old, st="unmet"):
        return {"status": st, "note": renum(old)["note"] + " " + chal(st)["note"]}

    def chal(st="unmet"):
        return {"status": st, "note": "son55 wrote 'challenged_with_evidence'. That status is reserved for an author "
                                      "who challenges the expectation with evidence; here the paper's own claim is "
                                      "contradicted by its material, which is 'unmet'."}

    # =========================================================== 2605.10064 MAGE
    p = "2605.10064"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Crafter peak, Llama-3.1-8B-Instruct execution tier peak success rate (%) 23.4 ± 2.3 n = 5",
                    "Appendix M, Table 13",
                    "Table 13 (and Table 12) give the Llama Crafter peaks as 23.4 / 22.7 / 22.7 for Sonnet / Opus / "
                    "Haiku, below the 25.5 standalone BALROG reference. Table 3 and Table 11 report 33.5 / 37.9 / 34.8 "
                    "for the same cells. Neither seat recorded this."),
            opus_ev(p, "O02", "On Crafter, all teacher-guided configurations improve over the standalone Llama-3.1-8B "
                              "BALROG reference.", "§4.2",
                    "The improvement claim that opus:O01 and opus:O09 contradict."),
            opus_ev(p, "O03", "Headline single-seed numbers under the Llama-3.1-8B-Instruct execution tier are reported "
                              "in Table", "Appendix Q",
                    "Appendix Q then gives FinQA 64.0–64.5% and MedQA 68.5% (Sonnet) as those headline numbers, while "
                    "Table 2 shows 67.5±1.7 and 74.6±2.3 (n=5). A further text–table contradiction."),
            opus_ev(p, "O04", "All methods on Qwen3-8B at fp16 on a single H100.", "Appendix O, Table 14 caption",
                    "Table 14's FinQA/MedQA rows reuse the Llama Table 2 numbers (58.0/64.5 baselines, 67.5/74.6 MAGE), "
                    "and its Reflexion STBench/RealMath cells (12.0/11.5) differ from Table 1 (37.0/34.5). Extends "
                    "son55:E23 and son55:E26."),
            opus_ev(p, "O05", "The STBench Opus row uses the recovery configuration with prerequisite cascade disabled",
                    "Appendix M, Table 13 caption",
                    "A per-benchmark configuration choice for a headline cell (Table 1 STBench Opus 57.8). It conflicts "
                    "with Appendix D's statement quoted in opus:O06 and with Table 15, where cascade lowers STBench "
                    "by 6.0."),
            opus_ev(p, "O06", "All values are fixed across benchmarks; no per-benchmark tuning is performed.",
                    "Appendix D", "Claim contradicted by opus:O05."),
            opus_ev(p, "O07", "We logged every httpx call across thirty-six v20/v21 training runs", "Appendix N",
                    "Thirty-six runs here, 52 in Table 4's aggregate row, and 42 if Table 4's per-benchmark run "
                    "counts are summed."),
            opus_ev(p, "O08", "Per-task-type structured evaluation via LLM-as-judge scoring", "Appendix C, Table 6",
                    "The Critic is the guidance tier (Sonnet 4.6 in Appendix D). It decides which learner answers "
                    "become success memories, and the same Sonnet 4.6 judge scores the held-out pool (son55:E06, "
                    "son55:E24). The stored exemplars are selected by the judge that later grades the test.",
                    kind="our_inference"),
            opus_ev(p, "O09", "Crafter peak, Qwen3-8B execution tier peak success rate (%) 25.3 ± 1.5 n = 5",
                    "Appendix M, Table 13",
                    "Qwen Crafter peaks 25.3 / 26.8 / 24.0. These are also at or near the 25.5 reference."),
        ],
        "rs_pattern": base_block("son55", p, "rs_pattern",
                                 reason="Opus: both seats chose adapt_via_conditioning C03 (frozen executor conditioned "
                                        "on retrieved solved cases and corrections, no parameter update). Kept; fit "
                                        "partial (no class-level holdout, no cheapest-retrieval baseline)."),
        "domain_pattern": base_block("son55", p, "domain_pattern",
                                     reason="Opus = son55. H03, because the operative read is Eq. 3: flat "
                                            "task-type-filtered embedding top-K over near-raw cases (correct "
                                            "learner CoT, teacher failure-to-fix records), appended after each "
                                            "round. The four-subgraph shape never enters retrieval and is not "
                                            "compared with flat retrieval, so H04 is not kept (its failure mode 'a "
                                            "new store shape stands in for an argument' is recorded as a check). "
                                            "H00 agreed.",
                                     revision_proposals=["H04 failure check: graph stores whose retrieval rule is "
                                                         "flat filtered top-K belong to H03 (see batch notes)."]),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.10064-1"): "local:2605.10064-3",
                    ("son55", "local:2605.10064-2"): "local:2605.10064-6"},
            overrides={
                "local:2605.10064-1": {
                    "status": "partial",
                    "reason": "Opus (revised from sol's met). The QA evolution pool and the final pool are declared "
                              "separate and the graph is frozen (sol:E004). But Crafter is reported as the peak across "
                              "iterations (son55:E14), and the STBench Opus headline cell uses a per-benchmark "
                              "configuration (opus:O05) despite 'no per-benchmark tuning' (opus:O06)."},
                "local:2605.10064-3": {
                    "status": "unmet",
                    "reason": "Merged: sol local-3 and son55 local-1 ask the same question (do native metrics "
                              "corroborate the semantic judge?). The only cross-check, HotpotQA EM/F1, ranks 8-shot "
                              "CoT above MAGE (sol:E006, son55:E10). The judge is never calibrated against humans and is "
                              "the same Sonnet 4.6 Critic that admits success memories (opus:O08). FinQA/MedQA native "
                              "EM does not test the judge. Unmet.",
                    **{"note": "son55 status 'challenged_with_evidence' recorded as unmet (that status is reserved for "
                               "an author challenge)."}},
                "local:2605.10064-6": {**renum("son55:local:2605.10064-2"),
                                       "reason": "son55's question: is the empty-graph scaffold separated from "
                                                 "accumulated memory? Table 17 shows 87% at iteration 0 with no "
                                                 "harvested successes against a 64.5 0-shot baseline (son55:E11), and "
                                                 "no scaffold-on/memory-off arm exists. Unmet."},
                "rsi:evidence_gated_retention/S2": dropped("evidence_gated_retention"),
                "rsi:index_experience_for_reuse/F3": {"note": "Failure-mode check: 'met' means the failure mode is "
                                                              "not triggered for the QA stores (built from the "
                                                              "evolution pool only)."},
            }),
        "claims": lambda c: amend(amend(c, "C4", ["opus:O01", "opus:O02", "opus:O09", "opus:O03"],
                                        allowed_conclusion="Native-metric gains on FinQA/MedQA and WebShop over the "
                                                           "listed references (not same-condition). Crafter is not an "
                                                           "improvement claim the paper can support: its own Tables "
                                                           "12/13 put the peaks at or below the 25.5 standalone "
                                                           "reference (Opus shared-error correction)."),
                                  "C1", ["opus:O04", "opus:O05", "opus:O08"]),
        "assessment": assess("son55", p, [
            "Opus: Crafter peaks in Tables 12/13 (23.4/22.7/22.7 Llama) contradict the 33.5–37.9 of Tables 3/11 and the "
            "§4.2 improvement claim (opus:O01, opus:O02).",
            "Opus: Appendix Q headline FinQA/MedQA values contradict Table 2 (opus:O03).",
            "Opus: success memories are admitted by the same Sonnet 4.6 judge that scores the held-out pool (opus:O08)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2, confirmed. A real organisational limitation (flat stores, undifferentiated "
                   "feedback) with neighbours named (Reflexion, EvolveR, MemRL, A-Mem, Voyager). But no experiment shows "
                   "that flat structure is the bottleneck, and no memory-based neighbour is compared under the same "
                   "conditions.", ["sol:E001", "son55:E02"], ["son55:E18"]),
            "M": R("resolved", 2, "Both seats 2, confirmed. The reward → harvest/correct → append → filtered retrieval "
                   "chain is reconstructable, and the success/failure channel split makes a checkable prediction. The "
                   "graph, bandits and delta-guard rest on theorem-style arguments; Theorem 3 as stated is false (j=0 "
                   "gives m_k ≥ any past peak; sol:E013, sol:E014), and Theorem 4 bounds only an oracle-relative "
                   "retrieval quantity.", ["son55:E03", "sol:E002", "sol:E016"], ["sol:E013", "sol:E014", "son55:E20"]),
            "X": R("resolved", 2, "Opus = son55. Nodes, indices, top-K allocation (2+1 / 1+2, 500-char threshold), "
                   "hyperparameters and the delta-guard are specified, and Appendix R shows the read. But the retention "
                   "core is ungated: protected nodes are never retired, so the delta-guard cannot undo a bad "
                   "teacher-written memory. Admission is by the LLM judge. The bandit arms (which retrieval and "
                   "inference strategies) are never listed. How task_type is assigned to a test question is not "
                   "stated. Headline cells come from different code versions (v15.6/v20/v21, cascade on/off; "
                   "opus:O05).", ["son55:E03", "son55:E04", "son55:E22", "sol:E017"], ["opus:O05", "son55:E13"]),
            "E.measurement": R("resolved", 1, "Opus = son55, below the run's cap of 2. FinQA/MedQA/WebShop use native "
                               "metrics (credit). The five reasoning benchmarks rest on a Sonnet 4.6 judge that also "
                               "admits success memories (opus:O08), and HotpotQA EM/F1 reverse the ranking against 8-shot "
                               "(son55:E10). Reported values contradict each other across tables: Table 14 vs Table 1 "
                               "(son55:E23), Table 2 vs Appendix Q (opus:O03), Crafter in Tables 3/11 vs 12/13 "
                               "(opus:O01, opus:O09), and the 'Qwen3-8B' Table 14 carrying Llama FinQA/MedQA rows "
                               "(opus:O04).",
                               ["son55:E06", "son55:E24", "opus:O08"],
                               ["son55:E10", "son55:E23", "son55:E26", "opus:O01", "opus:O03", "opus:O04", "opus:O09"]),
            "E.causality": R("resolved", 1, "Opus = son55. The only memory ablation is success-off (+7.0 mean; GSM8K "
                             "ablation ±12.7). There is no failure-off, graph-off/flat, bandit-off or delta-guard-off "
                             "arm. The 0-shot 'store-off' also removes the scaffold. Table 17's 87% at iteration 0, with "
                             "no harvested successes, against a 64.5 0-shot baseline (son55:E11) suggests the scaffold "
                             "carries much of the gain. The baselines receive no teacher or evolution-pool information "
                             "(no kNN-exemplar or teacher-exemplar baseline). The Crafter success-off was flat.",
                             ["sol:E005", "son55:E09"],
                             ["son55:E11", "son55:E12", "son55:E17", "son55:E18", "son55:E21"]),
            "E.holdout": R("resolved", 2, "Opus = son55. The evolution/final pool split and frozen graph and bandits "
                           "are declared (sol:E004). But Crafter is the peak across iterations (son55:E14), the STBench "
                           "Opus headline uses a per-benchmark configuration (opus:O05), Δ takes the better teacher per "
                           "cell (son55:E08), there is no contamination or class-level holdout analysis, and the "
                           "delta-guard's evaluation set is unspecified.",
                           ["sol:E004", "son55:E05"], ["son55:E14", "son55:E13", "opus:O05", "son55:E08"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2). MAGE cells are mean±std over up to "
                              "five completed seeds, but baselines are single runs, there are no CIs or tests, some "
                              "cells are single-seed, and incomplete seeds are not counted.",
                              ["sol:E007", "son55:E19"], ["sol:E018"]),
            "E.cost": R("resolved", 2, "Both seats 2, confirmed. Teacher/executor call counts (including retries) and "
                        "same-hardware latency against all baselines are reported. Missing are tokens/$, total evolution "
                        "budget, and any budget match against teacher-free baselines. The accounting is internally "
                        "inconsistent: 52 vs thirty-six runs (opus:O07), 2.12% vs 1.91% (sol:E015, son55:E15).",
                        ["sol:E011", "sol:E012", "son55:E15"], ["sol:E015", "opus:O07"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 HTML text read, including Appendices A–R. In scope (frozen executor; the retained "
                  "object is the external EvoKG plus two bandits). All eight items resolved; final = son55 on every "
                  "disputed rating, and Opus adds Crafter and Appendix Q contradictions.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: non-weight graph memory and bandits, executor frozen.",
        "improver_check": "not claimed; the Navigator/Curator rules are fixed.",
        "figure_dependence": "Figures 1–3 are image-only; Figure 3 effect sizes are taken from Tables 1/5.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"]],
                "See domain_pattern.reason. H03 matches the operative read (flat filtered top-K over gated near-raw "
                "cases, appended); H04's certification (store shape vs flat retrieval at scale) is never attempted.",
                ["son55:E22", "sol:E002", "sol:E017"], NOSCORE),
            XC(p, "local:2605.10064-1", "revised",
               "partial (sol's question: QA pool split); son55's local-1 question merged into local:2605.10064-3",
               "A4 hidden collision. sol asks about the evolution/final split: declared, but Crafter is the peak and STBench "
               "Opus uses a per-benchmark configuration, so the answer is partial, not met (opus:O05). son55 asks whether "
               "native metrics corroborate the judge, which is the same question as sol local-3 and is merged there.",
               ["sol:E004", "son55:E14", "opus:O05", "son55:E10"]),
            XC(p, "local:2605.10064-3", "revised", "unmet (merged with son55 local-1)",
               "The only native cross-check reverses the ranking (sol:E006, son55:E10), and the judge is coupled to "
               "memory admission (opus:O08). sol's 'partial' credited FinQA/MedQA EM, which does not test the judge.",
               ["sol:E006", "son55:E10", "opus:O08"]),
            XC(p, "local:2605.10064-4", "sol", "partial",
               "sol-only (statistics). Verified: n=5 std on MAGE cells, single-run baselines, no CI.", ["sol:E007"]),
            XC(p, "local:2605.10064-5", "sol", "partial",
               "sol-only (cost). Verified: call counts and latency, but no budget match and inconsistent run counts.",
               ["sol:E011", "sol:E015", "opus:O07"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "son55-only. Verified: success-off only, and the full-off baseline also removes the scaffold.",
               ["son55:E09", "son55:E17"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "partial",
               "son55-only. Verified: the split is declared, with no contamination analysis; Crafter is the peak.",
               ["son55:E05", "son55:E14"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "son55-only. Verified: no nearest-neighbour exemplar or teacher-exemplar baseline with matched "
               "information.", ["son55:E18"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "unmet",
               "son55-only. Verified: failure memories, graph edges, bandits and delta-guard are never ablated.",
               ["son55:E09", "son55:E04"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "son55-only. Verified: a teacher × learner matrix exists, but no noise/coverage sensitivity of the "
               "store.", ["son55:E19"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "son55-only. Verified: protected nodes are never merged, forgotten or retired.", ["son55:E03"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
               "sol-only. Verified: judge-gated harvest; the delta-guard covers mutable slots only.",
               ["sol:E003", "son55:E04"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "son55-only (check question; card not matched). Admission without retirement verified.", ["son55:E03"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "met",
               "son55-only failure-mode check: not triggered for the QA stores (evolution pool only). The note "
               "records the reading of 'met'.", ["son55:E05", "sol:E004"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "partial",
               "son55-only. Verified: writes are gated by an LLM judge, not an executable check.",
               ["son55:E24", "opus:O08"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "sol", "met",
               "sol-only. Verified: task-type filter and capped top-K (2+1/1+2).", ["sol:E002", "sol:E017"]),
            RC(p, "X", "son55", 2, "See ratings.X.", ["son55:E03", "son55:E04", "opus:O05"], "−5.0 vs sol"),
            RC(p, "E.measurement", "son55", 1, "See ratings.E.measurement. Opus adds opus:O01, O03, O04, O09.",
               ["son55:E10", "son55:E23", "opus:O01", "opus:O03"], "−2.5 vs sol"),
            RC(p, "E.causality", "son55", 1, "See ratings.E.causality. sol's 2 rested on the success-off ablation, "
               "which covers one channel and leaves the scaffold and teacher-information confound open.",
               ["son55:E09", "son55:E11", "son55:E18"], "−3.75 vs sol"),
            RC(p, "E.holdout", "son55", 2, "See ratings.E.holdout. sol's 3 did not weigh the Crafter peak and the "
               "per-benchmark configuration.", ["son55:E14", "opus:O05"], "−2.5 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims (Crafter improvement)",
             "sol_value": "C3: Crafter gains configuration-dependent (accepted as gains)",
             "son55_value": "C4: Crafter 33.5–37.9 vs 25.5 (mixed result, still above reference)",
             "final_value": "Crafter improvement contradicted inside the paper (Tables 12/13: 23.4/22.7/22.7 Llama, "
                            "25.3/26.8/24.0 Qwen, all at or below the 25.5 reference)",
             "reason": "Both seats took Table 3/11's Crafter peaks at face value. The appendix matrix and multi-seed "
                       "table report different and much lower values for the same cells, so §4.2's 'all "
                       "teacher-guided configurations improve' is contradicted.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O09"],
             "score_impact": "none beyond E.measurement=1 (already son55's value); claim scope narrowed"},
            {"field_path": "claims (FinQA/MedQA headline values)", "sol_value": "not examined",
             "son55_value": "not examined",
             "final_value": "Appendix Q gives 64.0–64.5 / 68.5 as the Table 2 headline numbers; Table 2 shows "
                            "67.5 / 74.6", "reason": "A text–table contradiction neither seat recorded.",
             "evidence_ids": ["opus:O03"], "score_impact": "none (supports E.measurement=1)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v3 text first. A frozen 8B executor with a "
                                                   "teacher-written plus self-harvested case store. Leaned to G2/M2. "
                                                   "Evidence weak: judge-coupled measurement with many cross-table "
                                                   "contradictions (Crafter, Table 14, Appendix Q, run counts), a "
                                                   "single-channel ablation, and baselines without teacher information.",
            "integrity_checks": "Both seats a1 on 2605.10064v3, material sha c6f9de19…; canonical seat hashes equal "
                                "conflicts.json (the sol working copy differs from HEAD but matches conflicts.json). "
                                "Both completed the 15+31 and domain identification.",
            "core_claim_check": "Tables 1–5, 9, 12–17, Appendices D/N/P/Q/R and Theorems 1–4 re-read.",
            "shared_error_review": "Shared ratings (G2, M2, E.statistics 2, E.cost 2) re-checked and kept. Two shared "
                                   "claim omissions corrected (Crafter, Appendix Q).",
            "rating_agreement": "All disputed items = son55. Final 43.75.",
        },
    }

    # =========================================================== 2605.10332 EmbodiSkill
    p = "2605.10332"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "Mem0 12.69 0 0 4.35 0 88.89 0", "Table 1, Qwen2.5-14B-Instruct block",
                    "Mem0 scores 0 on four of six sub-categories and is far below the no-memory row (46.27) with the "
                    "same executor. That points to a weak or broken baseline integration. The baseline write model is "
                    "also unstated (son55:E13).", kind="our_inference"),
            opus_ev(p, "O02", "Static Skill uses the initial skill without further revision.", "§4.3",
                    "Table 3's static skill differs by skill model (65.67 vs 58.95 on Qwen2.5-14B; 73.13 vs 79.85 on "
                    "Qwen3.5-27B), so S(0) depends on the skill model. Its construction is never described."),
        ],
        "rs_pattern": base_block("sol", p, "rs_pattern",
                                 reason="Opus: both seats chose heterogeneous_decomposition with sub null (C04 is "
                                        "compression-specific). Kept: the same failure signal is partitioned by "
                                        "attribution (defect vs lapse, discovery vs optimisation) and each partition "
                                        "gets a different write permission (body vs appendix)."),
        "domain_pattern": base_block("sol", p, "domain_pattern",
                                     reason="Both seats: H11 primary (attribute failures, split defect vs lapse, bounded "
                                            "edits) plus H01 (maintenance of a persistent guidance document). Agreed."),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.10332-1"): "local:2605.10332-4",
                    ("son55", "local:2605.10332-2"): "local:2605.10332-3",
                    ("son55", "local:2605.10332-3"): "local:2605.10332-5"},
            overrides={
                "local:2605.10332-3": {
                    "status": "unmet",
                    "reason": "Merged: sol local-3 and son55 local-2 both ask whether uncertainty is reported. Every "
                              "number is a single run with no seed, CI or test; the +1.49 cell is about 2 of 134 tasks. "
                              "Test denominators are given, which keeps E.statistics at 1, but this expectation is "
                              "unmet."},
                "local:2605.10332-4": {**renum("son55:local:2605.10332-1"), "status": "unmet",
                                       "reason": "son55's question: which revision stage is the headline? The text "
                                                 "says the method 'reaches 93.28% during evolution, after which it "
                                                 "remains in a high performance range' (son55:E10) on the test curve "
                                                 "(son55:E11). The headline is therefore the test-curve peak, with no "
                                                 "validation-based stage rule. Revised from unknown to unmet: the "
                                                 "complete text was read and the selection is stated."},
                "local:2605.10332-5": {**renum("son55:local:2605.10332-3"),
                                       "reason": "son55's cost question: no skill-model call, token or trajectory "
                                                 "counts, and the baselines' write-model budget is unstated. Unmet."},
                "rs:heterogeneous_decomposition/RE-2": {
                    "status": "not_applicable",
                    "reason": "Opus: RE-2 asks for deployment-unit efficiency. EmbodiSkill makes no efficiency claim, "
                              "so the expectation does not apply. son55 already marked it applicable=false; its "
                              "'unknown' is replaced by not_applicable. Cost is scored separately in E.cost."},
            }),
        "claims": lambda c: amend(c, "C3", ["opus:O01"]),
        "assessment": assess("sol", p, [
            "Opus: the 93.28% headline is the peak of the test-stage curve (son55:E10).",
            "Opus: S(0) depends on the skill model and its construction is undescribed (opus:O02).",
            "Opus: the Mem0 baseline integration looks broken (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3, confirmed. A specific embodied bottleneck (a failed trajectory is not "
                   "necessarily a skill defect), with a motivating example and lineage (Reflexion/ExpeL/G-Memory; "
                   "Voyager/Trace2Skill/EvoSkills). Not 4: the defect/lapse frequency is never measured, and the "
                   "nearest skill-evolution neighbours are characterised but not compared.",
                   ["sol:E001", "son55:E02", "son55:E03"], ["son55:E22"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Four reflection types are bound to outcome and routed to "
                   "different write channels (body edits vs appendix emphasis), with a distinguishable prediction "
                   "against whole-skill rewriting and a matching control (skill-unaware). Not 4: the attribution is "
                   "self-judged by the same LLM and never audited.",
                   ["sol:E002", "sol:E003", "sol:E004", "son55:E17"], ["son55:E22"]),
            "X": R("resolved", 2, "Both seats 2, confirmed. The reflect → consolidate → body/appendix → inject chain is "
                   "clear. Missing: B, S(0) (which varies with the skill model, opus:O02), prompts, any acceptance "
                   "gate, replay or rollback. Untouched-content preservation is only a prompt instruction.",
                   ["sol:E003", "sol:E004", "sol:E005", "sol:E006"], ["opus:O02", "son55:E18", "son55:E22"]),
            "E.measurement": R("resolved", 3, "Both seats 3, confirmed. Environment binary success with stated test "
                               "denominators is a trustworthy metric, and the text and tables agree. Relative gains are "
                               "written as '%' but are recomputable. No contradiction found that triggers the run cap.",
                               ["sol:E007", "son55:E08", "son55:E14"], ["son55:E15"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. Static-skill and skill-unaware controls use the "
                             "same executor and skill model (a naive-alternative arm). Missing: per-component ablation "
                             "(types, appendix, consolidation), trajectory-budget matching, and the baselines' memory "
                             "write model. One Gemini cell gains only +1.49, and Mem0's integration looks broken "
                             "(opus:O01).", ["sol:E010", "sol:E011", "son55:E16", "son55:E17"],
                             ["sol:E013", "son55:E13", "opus:O01"]),
            "E.holdout": R("resolved", 2, "Both seats 2, confirmed. Instance-level train/test split and a skill frozen "
                           "at test. The headline is the peak of the 10-stage test curve (son55:E10, son55:E11), with "
                           "no validation-based stage rule. No class-level or cross-environment transfer of a learned "
                           "skill.", ["sol:E007", "sol:E008", "son55:E09"], ["son55:E10", "son55:E11", "sol:E012"]),
            "E.statistics": R("resolved", 1, "Both seats 1, confirmed (A2 tier 1). Denominators and negative cells are "
                              "given, but every result is a single run with no uncertainty; the stability claim rests "
                              "on one curve.", ["sol:E007", "son55:E08"], ["sol:E013", "son55:E21"]),
            "E.cost": R("not_reported", 0, "Both seats 0, confirmed. After a complete read there is no skill-model "
                        "call, token, latency, trajectory-count or budget-matching report; the comparison with the "
                        "GPT-5.2 direct agent ignores the offline evolution budget.", [], ["son55:E15"],
                        ["complete pinned v2 text: abstract, §1–§5, Tables 1–3, Figure captions; the paper has no "
                         "appendix (son55:E22)"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text read (the paper has no appendix). In scope (frozen executor; the "
                  "retained object is the external skill document). All eight items resolved; both seats' ratings "
                  "confirmed item by item.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: non-weight skill body and appendix, executor frozen.",
        "improver_check": "not claimed; the reflection/revision prompts are fixed.",
        "figure_dependence": "Figure 3 (stage curve) is image-only; only the text values 73.13 / 93.28 are used.",
        "resolutions": [
            XC(p, "local:2605.10332-1", "revised",
               "unmet (sol's question: attribution accuracy); son55's question kept as local:2605.10332-4 (unmet)",
               "A4 hidden collision. sol asks whether the defect-vs-lapse attribution is validated: no audit or "
               "counterfactual, so unmet. son55 asks which stage is the headline: the test-curve peak (son55:E10), "
               "so unmet rather than unknown.", ["sol:E001", "sol:E011", "son55:E10", "son55:E11"]),
            XC(p, "local:2605.10332-2", "revised",
               "partial (sol's question: factor-level ablation); son55's statistics question merged into "
               "local:2605.10332-3",
               "A4 hidden collision. sol's question (does the unaware arm isolate each factor?) is partial: static, "
               "unaware and full arms exist, but unaware removes several factors at once. son55's question is about "
               "seeds/CI and duplicates sol local-3.", ["sol:E010", "sol:E011", "son55:E17"]),
            XC(p, "local:2605.10332-3", "revised",
               "unmet (merged statistics question); son55's cost question kept as local:2605.10332-5 (unmet)",
               "No uncertainty anywhere; denominators alone do not meet the expectation. son55's local-3 is the cost "
               "question, kept separately.", ["sol:E007", "son55:E08", "son55:E22"]),
            XC(p, "rs:heterogeneous_decomposition/RE-1", "son55", "partial",
               "son55-only. Verified: the partition criterion is new for skill evolution, but neighbour originals are "
               "not compared.", ["son55:E02", "son55:E03"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "revised", "not_applicable",
               "No efficiency claim, so the expectation does not apply; son55 already set applicable=false. Cost is "
               "scored in E.cost.", ["son55:E22"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "unmet",
               "son55-only. Verified: no single-type, consolidation or appendix ablation.", ["son55:E17"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "son55", "partial",
               "son55-only. Verified: a same-model uniform (unaware) arm exists; no skill-evolution neighbour baseline.",
               ["son55:E16", "son55:E17"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "unmet",
               "son55-only. Verified: the reflection-type distribution and accuracy are never reported.", ["son55:E22"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01-step3", "sol", "met",
               "sol-only. Verified: conflict handling and removal of obsolete appendix items.",
               ["sol:E004", "sol:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "partial",
               "son55-only. Verified: a lapse channel exists, but the attribution is never checked.",
               ["son55:E03", "son55:E22"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11", "son55", "unmet",
               "son55-only (sub-card as a whole). Verified: no replay or validation-based keep, and test seen per stage.",
               ["son55:E10", "son55:E11", "son55:E05"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-step2", "sol", "met",
               "sol-only. Verified: defect edits vs lapse reminders.", ["sol:E001", "sol:E002"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-step3", "sol", "partial",
               "sol-only. Verified: semantic locality is a prompt constraint only.", ["sol:E005"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-step4", "sol", "unmet",
               "sol-only. Verified: consolidation replaces the skill without an independent gate.",
               ["sol:E004", "sol:E008"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11-step5", "sol", "partial",
               "sol-only. Verified: instance split, but the test curve is observed per stage.",
               ["sol:E007", "sol:E012"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "met",
               "son55-only. Verified: each reflection names its target content.", ["son55:E04", "son55:E17"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "son55-only. Verified: successes feed reflections, but there is no per-edit regression or rollback.",
               ["son55:E04", "son55:E05"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first (no appendix). A clear mechanism with "
                                                   "a matching unaware control. Weak on cost (nothing), statistics "
                                                   "(single runs) and stage selection (test peak). Leaned to "
                                                   "G3/M3/X2/E around 3/2/2/1/0.",
            "integrity_checks": "Both seats a1 on 2605.10332v2, material sha 45abfdbe…; canonical seat hashes equal "
                                "conflicts.json; identification completed by both.",
            "core_claim_check": "Tables 1–3, §4.2–4.3 and every relative-percentage claim recomputed (31.58, 25.01, "
                                "19.04, 16.29, 17.94, 6.98, 22.10, 26.37 all reproduce).",
            "shared_error_review": "All eight shared ratings re-checked against the text: no shared rating error. "
                                   "E.measurement 3 survives because the text and tables agree. The Mem0 anomaly "
                                   "(opus:O01) is recorded under E.causality.",
            "rating_agreement": "Identical seat ratings confirmed. Final 57.5.",
        },
    }

    # =========================================================== 2605.10366 EGL-SCA
    p = "2605.10366"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Evaluator-guided prompt and program refinement.", "Appendix C, Table 7 (GEPA row)",
                    "The paper's own description of GEPA, its closest prompt-side baseline, covers prompt and "
                    "program refinement. This contradicts the gap that existing approaches improve one side in "
                    "isolation (opus:O04)."),
            opus_ev(p, "O02", "300 planned episodes; 297 counted after 3 exclusions", "Appendix A, Table 2",
                    "Table 2 (and Tables 3/17) put the main run at 300 episodes; Appendix A says 'The main training "
                    "runs use a 200-episode budget' (son55:E16), and Figure 3(a) is described 'by episode 200'."),
            opus_ev(p, "O03", "Instruction mutations 20 22 17 19.7", "Appendix D, Table 10",
                    "Every 150-episode run of the full SCA method accepts 17–22 instruction mutations. That is the "
                    "level Table 1(b) attributes to 'update thrashing' without SCA (22), while the 300-episode full run "
                    "is reported at only 2 (opus:O05). The mechanism statistic behind C2 does not replicate across "
                    "seeds."),
            opus_ev(p, "O04", "Existing approaches usually improve either the instruction side or the tool side in "
                              "isolation", "Abstract", "The stated gap."),
            opus_ev(p, "O05", "the full system maintains an exceptional protocol reliability of 0.936 while accepting "
                              "only 2 instruction mutations", "§4.3",
                    "The anti-thrashing evidence that opus:O03 undercuts."),
        ],
        "rs_pattern": base_block("son55", p, "rs_pattern",
                                 reason="Opus = son55. Primary decompose_and_delegate C25: the LLM emits a typed, "
                                        "machine-checkable task_input, exact solving is delegated to verified tools, and "
                                        "the verifier's structured output closes the loop and assigns credit to "
                                        "sub-decisions (C25 step 3). The delegation is load-bearing (w/o Tool Use 0.380 "
                                        "vs 0.920). heterogeneous_decomposition stays as supporting: failures are "
                                        "partitioned by source and routed to different update operators. sol's "
                                        "single heterogeneous_decomposition match misses the solver-delegation boundary "
                                        "that carries most of the gain."),
        "domain_pattern": base_block("son55", p, "domain_pattern",
                                     reason="Both seats: H09 (route failure evidence to the responsible component), H07 "
                                            "(verified tool crystallisation, frozen reuse), H16 (Pareto retention). "
                                            "Agreed."),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.10366-1"): "local:2605.10366-4",
                    ("son55", "local:2605.10366-2"): "local:2605.10366-5"},
            overrides={
                "local:2605.10366-3": {
                    "status": "unmet",
                    "reason": "Opus (revised from son55's unknown). After a complete read of Appendix C (Table 7 lists "
                              "mechanisms only) and Appendix A, no training budget, iteration count or tuning is given "
                              "for GEPA, ExpeL, Reflexion or AgentSquare. Several of them score below direct prompting "
                              "(son55:E23)."},
                "local:2605.10366-4": {**renum_chal("son55:local:2605.10366-1"),
                                       "reason": "son55's question: does 'SOTA on four benchmarks' hold? The "
                                                 "benchmarks are 200-case subsets restricted to trained task kinds "
                                                 "(son55:E14), and AgentSquare is higher on GraphArena and G-Real "
                                                 "(son55:E07). The average-only superiority is the supported claim."},
                "local:2605.10366-5": {**renum("son55:local:2605.10366-2"),
                                       "reason": "son55's question: do the ablations have uncertainty? All are single "
                                                 "seed; the SCA-routing effect (−0.025) is of seed-noise size. Unmet."},
                "rsi:crystallize_executable_capability/S3": {
                    "status": "met",
                    "reason": "Opus = sol. S3 asks that a tool be checked on inputs it was not built from. Tools pass "
                              "hidden verifier tests at admission and are reused on unseen external instances with "
                              "proposal disabled. Task-kind overlap with training families is a scope limit on "
                              "transfer, scored in E.holdout, not a failure of S3."},
            }),
        "claims": lambda c: amend(c, "C2", ["opus:O03", "opus:O05"],
                                  allowed_conclusion="scoped: the no-routing variant is lower on the external average "
                                                     "(−2.5 pp, single seed). The 'thrashing' mechanism statistic (2 vs "
                                                     "22 accepted mutations) does not replicate: the full method accepts "
                                                     "17–22 per seed run (Opus shared-error correction)."),
        "assessment": assess("son55", p, [
            "Opus: Table 1(b)'s 2 accepted instruction mutations is contradicted by 17–22 per SCA seed run (opus:O03).",
            "Opus: the main-run budget is stated as both 200 and 300 episodes (opus:O02, son55:E16)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus = son55. 'Which side to update after failure' is concrete. But the gap claim "
                   "(one side in isolation, opus:O04) is contradicted by the paper's own description of GEPA as "
                   "prompt-and-program refinement (opus:O01), tool-making self-improvement neighbours are not "
                   "discussed, and 'thrashing' is supported only by a training statistic that does not replicate "
                   "(opus:O03).", ["son55:E02", "opus:O04"], ["opus:O01", "opus:O03", "son55:E11"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. The route table maps evidence to update operators, typed "
                   "interfaces give a structural prior, and admission and Pareto retention fit a small model plus "
                   "verifier. The no-routing prediction is checkable. Not 4: earliest-stage blame is a heuristic with "
                   "unstated thresholds and untested attribution accuracy.",
                   ["son55:E01", "son55:E03", "son55:E05", "son55:E22"], ["son55:E04"]),
            "X": R("resolved", 3, "Both seats 3, confirmed. Information rights (privileged z* in training, text only "
                   "at test), executable tool admission, frontier retention, frozen evaluation with proposal disabled, "
                   "prompt lineage and tool inventory are all reconstructable. Not 4: routing thresholds, the "
                   "mutation-acceptance rule and the frontier pick rule are unstated, and the budget statement "
                   "conflicts (opus:O02).", ["son55:E05", "son55:E06", "son55:E15", "son55:E22", "son55:E24"],
                   ["son55:E04", "opus:O02"]),
            "E.measurement": R("resolved", 2, "Shared-error correction 3 → 2 (run convention: internal contradictions "
                               "cap E.measurement at 2). The structured executable verifier is a strong metric and would "
                               "merit 3. But the paper contradicts itself on which run produced the frozen pair (200 vs "
                               "300 episodes, opus:O02, son55:E16), on its mechanism statistics (Table 1(b) 2 accepted "
                               "mutations vs 17–22 per seed, opus:O03; '100% activation' vs 26/27 exercised), and on "
                               "Appendix D's claim that the 300-episode agent masters G-Real (0.795 < 0.810, son55:E19). "
                               "Benchmarks are re-formatted, author-chosen subsets.",
                               ["son55:E05", "sol:E005", "sol:E006"],
                               ["opus:O02", "opus:O03", "son55:E16", "son55:E19", "son55:E14"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. Five ablations; tool use (−0.54) and instruction "
                             "evolution (−0.06) are clear. SCA routing (−0.025) is single seed and its training "
                             "statistic does not replicate (opus:O03). Baseline budgets are unknown, and several "
                             "self-improving baselines fall below direct prompting. AgentSquare beats the full method on "
                             "two benchmarks.", ["son55:E07", "son55:E10", "sol:E007", "sol:E008"],
                             ["opus:O03", "son55:E23", "son55:E18"]),
            "E.holdout": R("resolved", 2, "Opus = son55. Training is on a synthetic generator, selection uses internal "
                           "validation, and evaluation is frozen with proposal disabled; the separation is real. But "
                           "the four 'benchmarks' are 200-case subsets restricted to task kinds mirroring the training "
                           "families (son55:E14), the sampling of the 200 is undescribed, and there is no contamination "
                           "or cross-domain test.", ["son55:E15", "son55:E13", "sol:E009"], ["son55:E14", "son55:E07"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2). A three-seed sweep with mean±std and "
                              "Wilson CIs at a reduced 150-episode budget, but the CIs treat three evaluations of the "
                              "same 200 cases as independent, and the headline and all ablations are single seed with "
                              "no tests.", ["son55:E18", "sol:E010", "sol:E011"], ["son55:E17"]),
            "E.cost": R("resolved", 2, "Opus = sol. The main run's tokens (6.734M), calls, wall-clock, per-tool cost "
                        "and exclusions are reported in detail. Missing: baseline and ablation budgets (so no fairness "
                        "argument against training-free or unknown-budget baselines), and the run's own budget is "
                        "stated inconsistently (200 vs 300 episodes, opus:O02).",
                        ["son55:E20", "sol:E013", "sol:E014"], ["son55:E23", "opus:O02"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (Appendices A–J and the checklist). In scope (the retained "
                  "objects are an instruction policy and a tool library, frozen at evaluation). All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: non-weight prompt and tool library, base model untouched.",
        "improver_check": "not claimed; the routing and mutation operators are fixed.",
        "figure_dependence": "Figure 3 panels are image-only; the text values 0.809/0.791/0.716/85% are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "See rs_pattern.reason.", ["son55:E05", "son55:E10", "son55:E22"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["decompose_and_delegate", "C25"], ["heterogeneous_decomposition", None]],
                "C25 primary, heterogeneous_decomposition supporting.", ["son55:E05", "son55:E10", "son55:E03"],
                NOSCORE),
            XC(p, "local:2605.10366-1", "revised",
               "partial (sol's question: seed/statistical support); son55's question kept as local:2605.10366-4 "
               "(unmet)",
               "A4 hidden collision. sol asks about seed support: a three-seed sweep exists at a reduced budget, so "
               "partial. son55 asks whether the 'SOTA on four benchmarks' scope holds: unmet (status corrected from "
               "challenged_with_evidence).", ["sol:E010", "son55:E14", "son55:E07"]),
            XC(p, "local:2605.10366-2", "revised",
               "partial (sol's question: cost accounting); son55's question kept as local:2605.10366-5 (unmet)",
               "A4 hidden collision. sol's cost question: own run fully accounted, baselines not, so partial. son55's "
               "ablation-statistics question: single seed, so unmet.", ["sol:E013", "sol:E014", "son55:E18"]),
            XC(p, "local:2605.10366-3", "revised", "unmet",
               "son55-only. The complete text gives no baseline budgets; 'unknown' is replaced by unmet with Appendix "
               "C/A as the search scope.", ["son55:E23"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "son55-only (card kept as primary). Verified: training cost is reported; solver latency and baseline "
               "budgets are not.", ["son55:E20"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "son55-only. Verified: component ablations exist, single seed.", ["son55:E07", "son55:E10"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "partial",
               "son55-only. Verified: a prompt diff is given; routing thresholds are not.", ["son55:E04", "son55:E24"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "son55-only. Verified: four benchmarks, restricted to trained task kinds.", ["son55:E14"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "son55-only. Verified: unified and fixed-toolbox baselines exist; budgets unknown; AgentSquare wins two "
               "benchmarks.", ["son55:E07", "son55:E23"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "partial",
               "son55-only. Verified: delegation is load-bearing (w/o Tool Use); stage-attribution bottleneck shown "
               "only by a training statistic.", ["son55:E10", "son55:E11"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "met",
               "son55-only. Verified: execution-based admission with public and hidden tests.", ["son55:E05"]),
            XC(p, "rsi:crystallize_executable_capability/S3", "sol", "met",
               "See the expectation reason: hidden-test admission plus frozen reuse on unseen instances meets S3. "
               "Task-kind overlap belongs to E.holdout.", ["sol:E005", "sol:E009", "son55:E05"]),
            XC(p, "rsi:crystallize_executable_capability/S5", "son55", "met",
               "son55-only. Verified: w/o Tool Use and w/o Tool Growth ablations.", ["son55:E07", "son55:E10"]),
            RC(p, "G", "son55", 2, "See ratings.G. Opus adds the GEPA self-description (opus:O01).",
               ["opus:O01", "opus:O04"], "−3.75 vs sol"),
            RC(p, "E.holdout", "son55", 2, "See ratings.E.holdout.", ["son55:E14"], "−2.5 vs sol"),
            RC(p, "E.cost", "sol", 2, "See ratings.E.cost. son55's 3 credited complete own-run accounting but not the "
               "absent budget fairness or the conflicting budget statement.", ["opus:O02", "son55:E23"],
               "−1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "reason": "Both seats noted some internal inconsistencies (sol under X: 200/300 and 100% vs 26/27; son55 "
                       "under E.statistics: 200 vs 300 and the Appendix D claim) but scored measurement 3. With these "
                       "contradictions, plus the mechanism statistic in opus:O03, the run convention caps "
                       "E.measurement at 2.",
             "evidence_ids": ["opus:O02", "opus:O03", "son55:E16", "son55:E19"],
             "score_impact": "−2.5 (sol 68.75 → 60.0 together with G and E.holdout; son55 63.75 → 60.0 together with "
                             "E.cost)"},
            {"field_path": "claims.C2 (anti-thrashing evidence)",
             "sol_value": "accepted 22 vs 2 mutations as routing evidence (scoped)",
             "son55_value": "accepted; E24 says the prompt diff 'corroborates only 2 accepted mutations'",
             "final_value": "the 2-mutation statistic does not replicate (17–22 per full-method seed run)",
             "reason": "Table 10 shows the full method accepting as many instruction mutations at 150 episodes as the "
                       "no-SCA variant at 300.", "evidence_ids": ["opus:O03", "opus:O05"],
             "score_impact": "none beyond E.measurement (E.causality stays 2 on the external ablations)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. A strong verifier-centric setup with a "
                                                   "clean synthetic-train / external-test split, but scoped "
                                                   "benchmarks, unknown baseline budgets and a self-contradictory "
                                                   "budget and mechanism report. Leaned to G2, M/X 3, E around "
                                                   "2/2/2/2/2.",
            "integrity_checks": "Both seats a1 on 2605.10366v1, material sha 56157464…; canonical seat hashes equal "
                                "conflicts.json; identification completed by both.",
            "core_claim_check": "Table 1(a)/(b), Tables 2, 6–10, 17–18, §4.2–4.7 and Appendices D/H/I re-read.",
            "shared_error_review": "Shared E.measurement 3 corrected to 2. Claim C2's mechanism statistic corrected. "
                                   "Shared M3, X3, E.causality 2 and E.statistics 2 re-checked and kept.",
            "rating_agreement": "G, E.holdout = son55; E.cost = sol; E.measurement shared-corrected. Final 60.0.",
        },
    }

    # =========================================================== 2605.11136 EvoChamber
    p = "2605.11136"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "In the current implementation, most insights are classified as cross-domain by the "
                              "crystallization step.", "Appendix L",
                    "Niche-specific asymmetric routing, the paper's central distinction from symmetric broadcast, is "
                    "the minority case in practice."),
            opus_ev(p, "O02", "with HotpotQA dropping from 0.895 to 0.572 and DROP from 0.860 to 0.480", "§4.3",
                    "Without CoDream, the system falls far below the stateless single agent (0.791/0.800). Removing "
                    "CoDream therefore also damages something else; in the 30-task isolation (Appendix F) w/o CoDream "
                    "equals SA.", kind="author_report"),
            opus_ev(p, "O03", "A session fires whenever the team fails, either because the mean reward falls below "
                              "threshold", "§3.5",
                    "Online state updates (CoDream triggers, EWMA competence, synergy, lifecycle) are driven by r_t, "
                    "which is the gold-scored metric (exact match / pass@1 / F1) of the very stream on which accuracy is "
                    "reported. This is an oracle feedback signal under A2.", kind="our_inference"),
            opus_ev(p, "O04", "All streams use a fixed task order across methods to ensure comparable learning "
                              "trajectories.", "Appendix E.4",
                    "Evaluation is prequential on the adaptation stream itself; no frozen-state held-out test exists."),
        ],
        "rs_pattern": base_block("son55", p, "rs_pattern",
                                 reason="Both seats: heterogeneous_decomposition, sub null (agents partitioned by "
                                        "niche competence, asymmetric produce/consume). Agreed; fit partial, because "
                                        "the heterogeneity comes from metadata labels and most insights are routed "
                                        "cross-domain (opus:O01)."),
        "domain_pattern": base_block("son55", p, "domain_pattern",
                                     reason="Both seats: H18 (online pool/team rewrite gated by outcomes) + H00 "
                                            "(distilled insights reused). Agreed."),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.11136-1"): "local:2605.11136-4",
                    ("son55", "local:2605.11136-2"): "local:2605.11136-5"},
            overrides={
                "local:2605.11136-3": {
                    "status": "unmet",
                    "reason": "Merged (same question in both seats: uncertainty on the reported comparisons). "
                              "Baselines, main tables and ablations are single runs with no CI or test. The two "
                              "Hard-Math reorderings are a robustness check of one method, not error bars on "
                              "differences."},
                "local:2605.11136-4": {**renum("son55:local:2605.11136-1"),
                                       "reason": "son55's question: is asymmetric routing compared with a symmetric "
                                                 "variant inside the same framework? No. The only removal (w/o "
                                                 "CoDream) falls below SA (opus:O02). Unmet."},
                "local:2605.11136-5": {**renum_chal("son55:local:2605.11136-2"),
                                       "reason": "son55's question: is 'emergent specialisation' more than the "
                                                 "construction (metadata niche labels in ordered blocks plus "
                                                 "per-niche EWMA)? Not shown, and '4–5 stable specialists' has no "
                                                 "count."},
                "rs:heterogeneous_decomposition/RE-4": {
                    "status": "partial",
                    "reason": "Opus = sol. Directly competing methods (MemCollab symmetric sharing, EvoMem) are "
                              "compared, so not unmet. But the isolating baseline (symmetric CoDream inside "
                              "EvoChamber) is missing, so partial."},
            }),
        "claims": lambda c: amend(c, "C2", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: w/o CoDream drops below SA on HotpotQA/DROP (opus:O02), so the −0.108 is not a clean CoDream "
            "effect.",
            "Opus: online rewards are gold-scored on the reported stream (opus:O03)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3, confirmed. A concrete slot between private memory and symmetric "
                   "broadcast, with the nearest neighbours (EvoMem, MemCollab, AgentNet, DyLAN) implemented at matched "
                   "team size. Not 4: 'broadcast erases specialisation' is asserted, and 'first' rests on a feature "
                   "table.", ["son55:E02", "son55:E20", "sol:E001"], ["son55:E29"]),
            "M": R("resolved", 2, "Opus = son55. The roles, deficit gate and five-phase CoDream are clear and "
                   "predict asymmetric > symmetric. But that key assumption is never tested in-framework. Most insights "
                   "are in fact routed cross-domain (opus:O01). The specialisation story follows by construction from "
                   "metadata niche labels plus per-niche EWMA (son55:E05, son55:E17). The 'verified' gate is a "
                   "same-task retry that admits generic advice (son55:E04). A shared team reward is used as "
                   "individual competence.", ["son55:E01", "son55:E03"],
                   ["opus:O01", "son55:E04", "son55:E05", "son55:E17"]),
            "X": R("resolved", 3, "Opus = son55. Table 9 and E.1 specify every threshold and operator (fork top 10%, "
                   "merge > 0.95, prune < 0.8× mean, genesis < 0.4, τ = 10, θ = 0.6), the read paths and the fast/slow "
                   "split. The paper also analyses where the mechanism does not fire. Thin points: no insight-level "
                   "retirement or capacity bound, no roster rollback, and synergy defined as both a running mean and "
                   "an EWMA.", ["son55:E03", "son55:E13", "son55:E28", "sol:E016"], ["son55:E27", "son55:E04"]),
            "E.measurement": R("resolved", 2, "Opus = sol, at the run's cap for internal contradictions. "
                               "EM/pass@1/F1 are standard. But the Hard Code headline 0.757 averages 586 tasks "
                               "including saturated HumanEval while §4.1 describes a 422-task stream (son55:E07), and "
                               "Appendix I's 0.302 math_hard base contradicts Table 2's 0.374 (son55:E22).",
                               ["son55:E21", "son55:E08"], ["son55:E07", "son55:E22", "sol:E019"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. Cross-system baselines at matched team size, "
                             "three level-wise ablations and a 30-task isolation give directional evidence. But "
                             "w/o CoDream falls below SA (opus:O02), so the −0.108 includes collateral damage. There is "
                             "no symmetric-CoDream arm; lifecycle and pool size contribute about zero; everything is "
                             "single run.", ["son55:E10", "son55:E11", "sol:E018"],
                             ["opus:O02", "son55:E12", "son55:E13", "son55:E31"]),
            "E.holdout": R("resolved", 1, "Opus = sol (A2: oracle feedback). Accuracy is prequential on the same "
                           "stream whose gold-scored rewards drive CoDream, competence and lifecycle (opus:O03, "
                           "opus:O04). No frozen-state evaluation on held-out tasks; hyperparameter provenance is "
                           "unstated; niche labels are given from metadata. Same-order runs and two reorderings show "
                           "only that ordering is not the explanation.", ["son55:E19", "son55:E15"],
                           ["opus:O03", "opus:O04", "son55:E05", "son55:E18"]),
            "E.statistics": R("resolved", 1, "Opus = son55 (A2 tier 1). Stream sizes and negative or near-zero cells "
                              "are reported, but there is no uncertainty for any main, backbone or ablation comparison. "
                              "The reorderings are single runs of one method. AFlow +3.1 pp and GPT-4.1-mini +1.9 pp are "
                              "near noise, and the authors call AIME CoDream effects noisy.",
                              ["son55:E15", "son55:E06"], ["son55:E09", "son55:E25", "son55:E31"]),
            "E.cost": R("resolved", 2, "Opus = son55. A quantitative comparison exists: 3.6× SA and 72% of SC(k=5) "
                        "tokens, plus per-phase token caps and hardware. Missing: costs of the memory baselines, "
                        "absolute tokens, CoDream/lifecycle call counts and wall-clock.",
                        ["son55:E14", "sol:E013"], ["son55:E20"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (Appendices A–L). In scope (training-free; the retained objects "
                  "are agent memories, competence/synergy state and the roster). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: non-weight per-agent memories, pool state and roster; no gradient updates.",
        "improver_check": "not claimed; the CoDream/lifecycle procedures are fixed.",
        "figure_dependence": "Figure 3 panels (specialisation heatmaps, flow matrix) are image-only; Table 6 values "
                             "are used instead.",
        "resolutions": [
            XC(p, "local:2605.11136-1", "revised",
               "partial (sol's question: metrics/denominators); son55's question kept as local:2605.11136-4 (unmet)",
               "A4 hidden collision. sol: standard metrics but a 422/586 mismatch and weak 'verified' labels, so "
               "partial. son55: no in-framework symmetric arm, so unmet.",
               ["sol:E007", "sol:E019", "son55:E10", "opus:O02"]),
            XC(p, "local:2605.11136-2", "revised",
               "partial (sol's question: cost); son55's question kept as local:2605.11136-5 (unmet)",
               "A4 hidden collision. sol: relative costs reported, absolute and baseline costs missing, so partial. "
               "son55: specialisation conflated with construction, so unmet (status corrected from "
               "challenged_with_evidence).", ["sol:E013", "son55:E05", "son55:E16", "son55:E17"]),
            XC(p, "local:2605.11136-3", "son55", "unmet",
               "Same question in both seats; no uncertainty on any comparison, so unmet.", ["son55:E09", "son55:E25"]),
            XC(p, "rs:heterogeneous_decomposition/RE-1", "son55", "partial",
               "son55-only. Verified: the partition criterion is not separated from standard competence routing.",
               ["son55:E03", "son55:E05"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "son55", "partial",
               "son55-only. Verified: relative token costs only.", ["son55:E14"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "partial",
               "son55-only. Verified: three level-wise ablations; individual memory, scout and single operators are "
               "not ablated.", ["son55:E10", "son55:E13"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "sol", "partial",
               "Competing methods are present but the isolating symmetric arm is missing; partial, not unmet.",
               ["sol:E001", "son55:E20", "son55:E10"]),
            XC(p, "rs:heterogeneous_decomposition/RE-6", "son55", "met",
               "son55-only. Verified: Appendix I analyses the regimes where CoDream binds.",
               ["son55:E31", "son55:E26"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "son55-only. Verified: LLM dedup only, no capacity bound or forgetting.", ["son55:E27", "son55:E28"]),
            XC(p, "rsi:search_agent_architecture/F1", "son55", "partial",
               "son55-only. Verified: partial axis ablations; lifecycle and pool size near zero.",
               ["son55:E12", "son55:E13"]),
            XC(p, "rsi:search_agent_architecture/H18", "sol", "partial",
               "sol-only. Verified: fast/slow updates; no per-edit gate or rollback.", ["sol:E016", "son55:E28"]),
            XC(p, "rsi:search_agent_architecture/S3", "son55", "met",
               "son55-only. Verified: roster and team updates are reward-driven.", ["son55:E03", "son55:E28"]),
            XC(p, "rsi:search_agent_architecture/S4", "son55", "partial",
               "son55-only. Verified: voting is selectable; roster edits have no rollback.", ["son55:E28"]),
            RC(p, "M", "son55", 2, "See ratings.M.", ["opus:O01", "son55:E04", "son55:E17"], "−5.0 vs sol"),
            RC(p, "X", "son55", 3, "See ratings.X. sol's 2 cited weaknesses (no rollback, cross-domain routing) "
               "that are recorded under M and as thin points; the operating chain itself is fully specified.",
               ["son55:E28", "sol:E016"], "+5.0 vs sol"),
            RC(p, "E.measurement", "sol", 2, "See ratings.E.measurement (run cap).", ["son55:E07", "son55:E22"],
               "−2.5 vs son55"),
            RC(p, "E.holdout", "sol", 1, "See ratings.E.holdout. son55's 2 credited the reorderings, which address "
               "ordering but not oracle-reward adaptation on the reported stream.", ["opus:O03", "opus:O04"],
               "−2.5 vs son55"),
            RC(p, "E.statistics", "son55", 1, "See ratings.E.statistics.", ["son55:E09", "son55:E25"],
               "−1.25 vs sol"),
            RC(p, "E.cost", "son55", 2, "See ratings.E.cost.", ["son55:E14"], "+1.25 vs sol"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. A rich, well-specified online system. "
                                                   "The asymmetry claim is untested in-framework, the CoDream-off "
                                                   "anomaly falls below SA, evaluation is prequential with gold "
                                                   "rewards, and there is no uncertainty anywhere. Leaned to G3, M/X "
                                                   "2–3, E around 2/2/1/1/2.",
            "integrity_checks": "Both seats a1 on 2605.11136v1, material sha db0017fb…; canonical seat hashes equal "
                                "conflicts.json; identification completed by both.",
            "core_claim_check": "Tables 2–7, 9–12, §4.3–4.4 and Appendices F/I/J/L re-read; the Hard Code overall "
                                "recomputed (586-task micro-average reproduces 0.667 and 0.757).",
            "shared_error_review": "Shared G3 and E.causality 2 re-checked and kept (the CoDream-off anomaly is "
                                   "recorded in the E.causality reason). No shared rating error.",
            "rating_agreement": "M, X, E.statistics, E.cost = son55; E.measurement, E.holdout = sol. Final 55.0.",
        },
    }

    # =========================================================== 2605.13941 EvolveMem
    p = "2605.13941"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Self-evolution 52.27", "§4.5, Table 6",
                    "Removing self-evolution costs only 2.03 F1 (54.3 → 52.27), against the 23.8-point R0 → R7 "
                    "trajectory that §4.3 attributes to the autonomous loop (opus:O05). Most of the gain comes from "
                    "hand-designed components (extraction guards −23.22, semantic view −10.32)."),
            opus_ev(p, "O02", "## Tier-1 TODO checklist: levers that are still OFF in the incumbent",
                    "Appendix F.6, diagnosis prompt",
                    "The diagnosis prompt hands the LLM a pre-built checklist of disabled levers to switch on one per "
                    "round. The 'discovered' dimensions are activations of pre-existing switches."),
            opus_ev(p, "O03", "4. If adversarial category weakness -> enable_entity_swap=true.",
                    "Appendix F.6, decision rubric",
                    "The rubric maps a LoCoMo category symptom to the exact lever that §4.3 says the LLM 'discovered' "
                    "at R3."),
            opus_ev(p, "O04", "returning θ ⋆ = arg ⁡ max r ⁡ f r", "§3.3",
                    "The returned configuration is the best round by score on the evaluation questions (son55:E04)."),
            opus_ev(p, "O05", "The full trajectory from 30.5% at R0 to 54.3% at R7, a 78.0% relative improvement, is "
                              "produced end-to-end by the autonomous evolution loop without manual intervention.",
                    "§4.3", "The attribution claim that opus:O01 undercuts."),
            opus_ev(p, "O06", "(LoCoMo only) 0.543 0.543", "§4.4, Table 5",
                    "C_L's zero-shot MemBench score equals its LoCoMo F1 to three decimals. It is not a multiple of "
                    "1/28 (MemBench uses 28 samples), and it is below RecentMem/MemGPT (57.1) on Table 3. The only "
                    "held-out number in the paper is unreliable and does not support 'zero-shot transfer is "
                    "effective'.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "Opus = son55. Run precedent (r08b 2512.09108, r09b 2601.01126, r04b EvoAgentX, cal-dev GrIPS): "
                      "LLM-driven search over an agent/RAG configuration and prompt surface has no main card. "
                      "generative_process_redesign needs a conventionally fixed component of an iterative or staged "
                      "generative procedure, redesigned with a load-bearing mechanism. Here a pre-enumerated config "
                      "and prompt space is searched on the evaluation set, and the redesign itself carries about 2 F1 "
                      "(opus:O01). Evaluated in full without a card.",
            "executes_pattern": False, "resolves_problem": False,
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12", fit="primary"),
                        dmatch("sol", p, "make_the_improver_editable", "H21", fit="supporting")],
            "unassigned": ["Typed store with consolidation and extraction guards: hand-built infrastructure, not the "
                           "evolved object (son55; H04 not kept)."],
            "reason": "Opus revised. H12 (son55) matches the operation: raw per-question logs with sources go to a "
                      "diagnosis LLM, which proposes scoped config patches, and the meta-analyzer reverts to the best "
                      "on regression. H21 (sol) matches the object: the mechanism by which the agent reads its memory "
                      "(retrieval policy) is the search target. H17 (son55) is dropped: H21 is the more specific card "
                      "for a memory-retrieval design search, and both share the held-out failure. H04 (sol) is dropped: "
                      "the store design is static, not evolved.",
            "revision_proposals": [],
        },
        "pattern_mapping": [
            {"rs_main": None, "rs_sub": None, "domain_namespace": "rsi", "domain_main": "attribute_and_patch_incumbent",
             "domain_sub": "H12",
             "operation_correspondence": "No RS counterpart (outside_taxonomy). H12: per-question raw logs → LLM "
                                         "diagnosis → field-level config patch → revert to best on an F1 drop.",
             "necessary_conditions_or_differences": "H12 requires promotion on an independent split and a falsifiable "
                                                    "per-patch prediction; both are missing (promotion on the scored "
                                                    "set).",
             "evidence_ids": ["son55:E05", "son55:E06", "son55:E24"]},
            {"rs_main": None, "rs_sub": None, "domain_namespace": "rsi", "domain_main": "make_the_improver_editable",
             "domain_sub": "H21",
             "operation_correspondence": "Outer loop searches the retrieval/answering policy through which the memory "
                                         "agent uses its store, scored downstream.",
             "necessary_conditions_or_differences": "H21 certifies on held-out tasks and transfer; the one transfer "
                                                    "number is unreliable (opus:O06).",
             "evidence_ids": ["sol:E007", "sol:E017", "opus:O06"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.13941-2"): "local:2605.13941-6",
                    ("son55", "local:2605.13941-3"): "local:2605.13941-7"},
            overrides={
                "local:2605.13941-1": {
                    "status": "unmet",
                    "reason": "Merged (same question in both seats: are the 'new dimensions' outside the original "
                              "action space?). They are pre-existing RetrievalConfig fields (son55:E09), the output "
                              "must match existing field names (son55:E08), and the prompt pre-lists them "
                              "(opus:O02, opus:O03). Unmet.",
                    "note": "son55 status 'challenged_with_evidence' recorded as unmet (that status is reserved for "
                            "an author challenge)."},
                "local:2605.13941-4": {
                    "status": "unmet",
                    "reason": "Merged (same question: statistical support). Single runs throughout, no CI; MemBench has "
                              "28 samples (1 sample ≈ 3.6 pp). Unmet."},
                "local:2605.13941-6": {**renum_chal("son55:local:2605.13941-2"),
                                       "reason": "son55's question: is the diagnosis benchmark-agnostic, and does "
                                                 "transfer hold? LoCoMo-specific flags, regex subtypes and Cat. 5 "
                                                 "priors are in the prompts (son55:E10–E12). The one zero-shot number "
                                                 "is unreliable and below baselines (opus:O06)."},
                "local:2605.13941-7": {**renum("son55:local:2605.13941-3"),
                                       "reason": "son55's question: is the gain attributable to self-evolution rather "
                                                 "than hand-built components? The ablation exists and answers 'mostly "
                                                 "not' (−2.03 vs −23.22; opus:O01), so partial."},
                "rs:generative_process_redesign/RE-1": dropped("generative_process_redesign"),
                "rs:generative_process_redesign/RE-2": dropped("generative_process_redesign"),
                "rs:generative_process_redesign/RE-3": dropped("generative_process_redesign"),
                "rsi:index_experience_for_reuse/H04": dropped("index_experience_for_reuse/H04"),
                "rsi:search_agent_architecture/H17": dropped("search_agent_architecture/H17"),
                "rsi:search_agent_architecture/S6": dropped("search_agent_architecture"),
                "rsi:population_search_executable_fitness/S2": dropped("population_search_executable_fitness"),
            }),
        "claims": lambda c: amend(amend(amend(c, "C2", ["opus:O01"]), "C4", ["opus:O02", "opus:O03"]),
                                  "C5", ["opus:O06"]),
        "assessment": assess("son55", p, [
            "Opus: self-evolution's own ablation share is 2.03 of 23.8 F1 (opus:O01).",
            "Opus: the only zero-shot transfer value equals the LoCoMo value and is not a valid 28-sample accuracy "
            "(opus:O06)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2, confirmed. 'Retrieval infrastructure frozen at deployment' is a real, "
                   "specific limitation. But MemEvolve (joint memory-architecture evolution), adaptive RAG and DB "
                   "auto-tuning are separated only by a feature table, and 'first' is not established.",
                   ["son55:E01", "sol:E001"], ["sol:E002", "son55:E09"]),
            "M": R("resolved", 2, "Opus = son55. The log → diagnosis → patch → revert chain is coherent, and "
                   "diagnosis vs random search is a checkable prediction. But the self-expansion argument is "
                   "contradicted by the interface (fields must match, son55:E08) and by a prompt that pre-lists the "
                   "levers (opus:O02, opus:O03). The gap (adaptation as a deployed store grows) is answered by "
                   "offline tuning on benchmark QA with ground truth, which a deployed system lacks (son55:E28).",
                   ["son55:E02", "son55:E05", "sol:E019"], ["son55:E07", "son55:E08", "opus:O02", "opus:O03",
                                                            "son55:E28"]),
            "X": R("resolved", 2, "Opus revised (sol 1, son55 3). Reconstructable: the action space (Table 7), "
                   "thresholds (τ_rev 0.01, ε 0.005, R_max 7), verbatim prompts, the revert branch (R2) and persisted "
                   "snapshots. Not 3: the stated stop rule (break when f_r − f_{r−1} < ε, sol:E010) cannot generate the "
                   "reported trajectory, which drops at R2 and R5 and continues to R7. Algorithm 2's online "
                   "self-evolution has no ground-truth signal at deployment (son55:E28). Not 1: the core chain and its "
                   "rollback are specified and exercised.",
                   ["son55:E02", "son55:E09", "son55:E24", "sol:E009", "sol:E023"],
                   ["sol:E010", "sol:E015", "son55:E28"]),
            "E.measurement": R("resolved", 1, "Opus = son55. Token F1/BLEU and MCQ EM are standard, but the "
                               "answer prompts are tuned to the token-F1 surface (never 'Unknown', fixed numeral and "
                               "date formats, an 'and' connector worth 0.06 F1; son55:E13, sol:E021), and the verifier "
                               "forces a guess (sol:E026). The transfer values are not valid 28-sample accuracies "
                               "(opus:O06). Model roles conflict (GPT-5.1 extraction and diagnosis throughout vs "
                               "'two backbones'), and baseline provenance is unstated.",
                               ["son55:E26", "sol:E011"],
                               ["son55:E13", "sol:E021", "sol:E026", "opus:O06", "son55:E22", "son55:E25"]),
            "E.causality": R("resolved", 1, "Opus = son55. A random-perturbation replacement (−9.63) and component "
                             "ablations exist, so not 0. But self-evolution's own share is −2.03 (opus:O01) against the "
                             "claimed 23.8 points (opus:O05). Hand-built extraction guards (−23.22) carry most of it, "
                             "and extraction always runs on GPT-5.1 (son55:E22), a confound against every baseline. "
                             "There is no tuned or Bayesian/grid optimiser baseline. Every ablation is a single run "
                             "re-evolved on the test set.", ["son55:E15", "son55:E16", "sol:E019"],
                             ["opus:O01", "opus:O05", "son55:E22", "son55:E25"]),
            "E.holdout": R("resolved", 0, "Opus = sol. The objective, the diagnosis input (with gold answers) and the "
                           "returned argmax are all on the reported question set (son55:E04, son55:E05, opus:O04). "
                           "MemBench is evolved on its 28 test samples, and the 2 'validation' samples are inside "
                           "LoCoMo-10. The only held-out number (C_L zero-shot on MemBench) is invalid as an accuracy "
                           "and below baselines (opus:O06), so the transfer claim is refuted rather than supported.",
                           ["son55:E21"], ["son55:E04", "son55:E05", "opus:O04", "opus:O06", "son55:E17"]),
            "E.statistics": R("resolved", 1, "Both seats 1, confirmed (A2 tier 1). Sizes (1,986 QA; 28 samples) and "
                              "regressing rounds are reported. Single runs, no uncertainty; 18.9% relative on MemBench "
                              "is about 3 samples.", ["son55:E17", "sol:E011"], ["son55:E27"]),
            "E.cost": R("resolved", 1, "Opus = sol. Wall-clock per sample, retrieval latency (15 ms), verification "
                        "overhead and storage are given. There are no tokens/$, no baseline or matched-budget comparison, "
                        "no account of GPT-5.1 extraction and re-extraction, and the timing is internally inconsistent "
                        "(15–20 min QA evaluation per round vs 25–35 min for all seven rounds; sol:E022).",
                        ["sol:E022", "son55:E23"], ["sol:E022", "son55:E25"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (Appendices A–F including all prompts). In scope (the retained "
                  "object is a non-weight retrieval/answer configuration). All eight items resolved; the final score is "
                  "below both seats because each item was decided separately.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: non-weight retrieval configuration and prompt flags.",
        "improver_check": "not claimed; the diagnosis prompt is fixed and hand-written.",
        "figure_dependence": "Figures 1–2 are image-only; the Figure 1(b) trajectory equals Table 4, which is used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", None,
                "outside_taxonomy; see rs_pattern.reason (run precedent for configuration/prompt search).",
                ["son55:E09", "opus:O01"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [],
                "outside_taxonomy. sol's generative_process_redesign is not kept; its RE-* stay as check questions.",
                ["son55:E09", "opus:O01"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H12"], ["make_the_improver_editable", "H21"]],
                "See domain_pattern.reason: son55's H12 (operation) + sol's H21 (object); H17 and H04 not kept.",
                ["son55:E05", "son55:E24", "sol:E007"], NOSCORE),
            XC(p, "local:2605.13941-1", "sol", "unmet",
               "Same question in both seats. Unmet; son55's 'challenged_with_evidence' misapplies that status.",
               ["son55:E08", "son55:E09", "opus:O02"]),
            XC(p, "local:2605.13941-2", "revised",
               "unmet (sol's question: stop rule vs trajectory); son55's question kept as local:2605.13941-6 (unmet)",
               "A4 hidden collision. sol: Algorithm 1 would stop at R2, so unmet. son55: benchmark-specific prompts "
               "and an unreliable transfer number, so unmet.", ["sol:E010", "sol:E015", "son55:E10", "opus:O06"]),
            XC(p, "local:2605.13941-4", "son55", "unmet",
               "Same question (statistics); no uncertainty anywhere, so unmet rather than partial.",
               ["son55:E17", "sol:E011"]),
            XC(p, "local:2605.13941-5", "sol", "partial",
               "sol-only (cost). Verified: timings and latency given, internally inconsistent, no budget comparison.",
               ["sol:E022"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "sol-only (check question; card not kept). Verified: −self-evolution is only −2.03.",
               ["sol:E018", "opus:O01"]),
            XC(p, "rs:generative_process_redesign/RE-2", "sol", "partial",
               "sol-only (check question). Verified: random search only; no strong optimiser baseline.", ["sol:E019"]),
            XC(p, "rs:generative_process_redesign/RE-3", "sol", "partial",
               "sol-only (check question). Verified: component ablations exist, but several fields change per round.",
               ["sol:E018", "sol:E015"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "son55", "unmet",
               "son55-only. Verified: promotion is on the scored set.", ["son55:E04", "son55:E06"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "son55-only. Verified: revert to best on same-set F1, no per-edit regression set.",
               ["son55:E24", "son55:E06"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met",
               "son55-only. Verified: raw per-question logs with sources.", ["son55:E05"]),
            XC(p, "rsi:index_experience_for_reuse/H04", "sol", "partial",
               "sol-only (check question; H04 not kept). Verified: store design is specific, but there is no flat "
               "comparison at scale.", ["sol:E004", "sol:E005"]),
            XC(p, "rsi:make_the_improver_editable/F3", "sol", "unmet",
               "sol-only. Verified: the scored set is reused for promotion and selection (failure mode triggered).",
               ["sol:E008", "son55:E04", "opus:O04"]),
            XC(p, "rsi:make_the_improver_editable/H21", "sol", "partial",
               "sol-only (card kept as supporting). Verified: a swappable retrieval policy, but no held-out "
               "certification.", ["sol:E007", "sol:E017"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial",
               "son55-only (check question). Verified: an objective fitness that answer-format flags can game.",
               ["son55:E13", "son55:E10"]),
            XC(p, "rsi:search_agent_architecture/H17", "son55", "unmet",
               "son55-only (check question; H17 not kept). Verified: search set = evaluation set.",
               ["son55:E04", "son55:E18"]),
            XC(p, "rsi:search_agent_architecture/S6", "son55", "unmet",
               "son55-only (check question). Verified: no certification away from the search set.",
               ["son55:E18", "opus:O06"]),
            RC(p, "M", "son55", 2, "See ratings.M.", ["son55:E08", "opus:O02"], "−5.0 vs sol"),
            RC(p, "X", "revised", 2, "Neither seat. sol's 1 underweights a fully specified, exercised chain; son55's 3 "
               "ignores that the stated stop rule cannot produce the reported run and that the online variant lacks "
               "its signal.", ["sol:E010", "son55:E28", "son55:E09"], "+5.0 vs sol; −5.0 vs son55"),
            RC(p, "E.measurement", "son55", 1, "See ratings.E.measurement.", ["son55:E13", "opus:O06"],
               "−2.5 vs sol"),
            RC(p, "E.causality", "son55", 1, "See ratings.E.causality.", ["opus:O01", "son55:E16", "son55:E22"],
               "−3.75 vs sol"),
            RC(p, "E.holdout", "sol", 0, "See ratings.E.holdout. son55's 1 credited a transfer experiment whose only "
               "zero-shot value is invalid and below baselines.", ["opus:O04", "opus:O06"], "−2.5 vs son55"),
            RC(p, "E.cost", "sol", 1, "See ratings.E.cost.", ["sol:E022"], "−1.25 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first, including all prompts. Same-set "
                                                   "configuration tuning with ground truth. The 'discovered' levers are "
                                                   "pre-listed, the self-evolution ablation share is about 2 F1, the "
                                                   "transfer number is broken, and the prompts are tuned to token F1. "
                                                   "Leaned to G2/M2/X2 and very low E (holdout 0).",
            "integrity_checks": "Both seats a1 on 2605.13941v1, material sha 02467b04…; canonical seat hashes equal "
                                "conflicts.json. son55 recorded outside_taxonomy with full identification reasoning.",
            "core_claim_check": "Tables 2–7, §3.3, Algorithms 1–2, Appendices C.1/D.3/E/F re-read; relative gains "
                                "recomputed (25.7, 78.0, 18.9, 63.4, 68.7, 36.8 reproduce).",
            "shared_error_review": "Shared G2 and E.statistics 1 re-checked and kept. No shared rating error.",
            "rating_agreement": "M, E.measurement, E.causality = son55; E.holdout, E.cost = sol; X revised to 2. Final "
                                "36.25.",
        },
    }
    return S
