"""Opus rulings for r16a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "Seat-input integrity: all ten a1 seat records match conflicts.json seat_record_hashes and the batch manifest "
        "(per-paper version and material sha256). No overrides, no seat errors, no controller action needed.",
        "2604.10992 ArtiCAD (Δ16.25): final 50.0 (sol 61.25, son55 45.0). G → son55 2: the CAD capability gap is "
        "concrete, but the in-scope retained object (experience store) gets no memory/case-reuse neighbour or "
        "residual. M → sol 3: the connector contract makes a separating prediction that the late-prediction "
        "ablation confirms; the store is generic case RAG and the O(1)/Markov-blanket argument is asserted. X → son55 "
        "2: store admission, retrieval size, versioning and ArtiCAD's own repair limits are unspecified, and the "
        "paper has no appendix or prompts. E.measurement → son55 2: the main benchmark is VLM-judged only, "
        "Krippendorff α 0.58–0.64 is called 'robust', Gemini-3-Pro is both judge and the backbone of the Pro row, and "
        "Succ only checks compilation. Store effect: quality deltas ≤0.05 on a 1–5 scale; iterations 4.4 → 3.1; "
        "'improves success rates' is not shown (Succ 100% with and without the store; shared correction).",
        "2604.11610 CluE (Δ1.25): final 70.0 (= son55). E.cost → son55 3: wall time, optimiser calls and evaluation "
        "calls for all four optimisers, and the closest baseline (MemEvolve) is matched on evaluation calls (1,150) "
        "with identical hyperparameters; tokens/dollars and a matched-optimiser-call control are absent. Opus "
        "corrections: son55's 'App. C prompts are images' is wrong (Figures 5–14 are text listings in the pinned "
        "material); son55's F4 'partial' revised to met, since the two LLM-judged sets (LongMemEval, ToolBench) are "
        "OOD test sets that are never used for selection.",
        "2604.11811 M* (Δ3.75): final 72.5 (= sol; son55 76.25). M → son55 3 (reflection vs plain mutation untested; "
        "static-subset fitness is loose: LoCoMo seed 1 has the lowest validation score, 0.273, but the highest test "
        "score, 0.463). X → son55 4 (search space, runtime constraints, compile-fix, softmax parent sampling, subset "
        "construction, retention rule and evolved listings are all in text). E.measurement → sol 2 (4 of 7 "
        "configurations are scored by gpt-5.4-mini rubric judging, the same model as the task agent and as the "
        "search fitness; no judge validation). E.statistics → sol 2 (five search seeds on 3/7 configurations without "
        "intervals or tests; Table 1 reports seed 0, which is above the mean; ALFWorld Unseen rates are multiples of "
        "1/42 while Table 5 states 50 test episodes). The abstract's 'all evaluated tasks' is contradicted by "
        "ALFWorld Seen (0.700 vs GEPA+VS 0.820).",
        "2604.12231 Thought-Retriever (Δ7.5): final 46.25 (= son55). E.holdout → son55 1: thought-construction "
        "queries are LLM-generated from each paper's title and abstract (App. D), the abstract is the Abstract-single "
        "label, the memory-building protocol of Table 2 is never stated, no overlap audit is reported, and the method "
        "beats a ground-truth-selected oracle; only App. Q (disjoint 50/50 split, about 15 test cases per set) is a "
        "clean retained test. M → son55 2: retention is decided by the generator's own binary confidence, with no "
        "outcome signal. The 'consistently outperforms all baselines' claim fails on Gov Report F1 (0.232 vs "
        "OpenOrca 0.244, Nous Hermes 0.238, Full Context left 0.234).",
        "2604.13533 EEAgent (Δ1.25): final 40.0 (sol 41.25, son55 42.5). M → son55 2 (LLM generality and "
        "consistency judgements are untested assumptions; Algorithm 1 has an 'or' retry guard and calls F_ei for "
        "planning). E.causality → son55 2 (the Vanilla EA control and CoT/SC alternatives on the same agent exist; "
        "component ablation and retry/budget parity are missing; run precedent). E.holdout → sol not_reported 0: no "
        "construction/evaluation split and no generalisation tier are stated, and failed tasks are retried up to "
        "3 times using the simulator's success signal, with no statement of whether post-retry success is "
        "scored. E.statistics and E.cost are not_reported in both seats (re-checked).",
        "A4 hygiene: hidden local-ID collisions (same ID, different question) were renumbered in all five papers. "
        "Same-question pairs were merged: 10992 sol local-2 → rs:decompose_and_delegate/RE-1; 11610 son55 local-1 → "
        "local-3. Every move is recorded in the affected expectation's note and in the resolution of the colliding ID.",
        "RS sub-card: C03 is set to null for 10992 and 12231 (frozen retrieval memory, no category holdout, no "
        "schema-reading upstream phase; run convention r09b/r12a/r13b/r14a). self_supervised_signal_engineering is "
        "kept as supporting for 12231 (self-confidence-gated self-generated thoughts with a w/o-Filter ablation) and "
        "rejected for 13533 (the simulator's success signal gates the reflection paths; r13a convention).",
        "Figure dependence: ArtiCAD Figs 1–7, CluE Figs 2–4, M* Figs 3–5 (transfer bars), Thought-Retriever Figs 5–8 "
        "and the prompt figures (3, 9–14), and EEAgent Figs 3–5 are image-only. Only values stated in text or tables "
        "are used; no figure value was read off or invented.",
        "No material requests. Requests for neighbour originals (ExpeL/Reflexion/CAD loops, MemSkill, MemEvolve/ADAS, "
        "MemWalker, CLIN) are non-blocking; no disputed rating depends on them.",
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

    def pm(s, p, idx=None, **upd):
        maps = seat(s, p)["pattern_mapping"]
        if idx is not None:
            maps = [maps[i] for i in idx]
        out = [prefix(copy.deepcopy(m), s) for m in maps]
        for m in out:
            m.update(upd)
        return out

    def dp_extra(s, p, key):
        return prefix(copy.deepcopy(seat(s, p)["domain_pattern"].get(key, [])), s)

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a = prefix(a, s)
        a.update(upd)
        return a

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def merged(other, extra_ev=()):
        return {"note": f"{other} merged here (A4: same question under a different ID).",
                "merged_from": other, "merged_evidence_ids": list(extra_ev)}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def xev(s, p, eid):
        return [f"{s}:{x}" for x in next(e for e in seat(s, p)["expectations"] if e["id"] == eid)["evidence_ids"]]

    SCOPE_FULL = "full pinned text incl. all appendices and tables read by Opus"

    # =========================================================== 2604.10992 ArtiCAD (Δ16.25)
    p = "2604.10992"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "ranges from 0.58 to 0.64, and the 3-rater mean ICC", "§5.1 Evaluation Protocol",
                    "Krippendorff's α of 0.58–0.64 is below the 0.667 level usually required even for tentative "
                    "conclusions, yet the paper calls reliability 'robust'. ICC(2,3) of the averaged scores is "
                    "higher, but there is no human or ground-truth anchor.", kind="our_inference"),
            opus_ev(p, "O02", "We also report results using Gemini-3-Pro on ArtiCAD-Bench to show the effect of a "
                              "stronger backbone.", "§5.1 Backbone Model",
                    "Gemini-3-Pro is one of the three judges (§5.1) and also the backbone of the 'ArtiCAD "
                    "(Gemini-3-Pro)' row; the default backbone, Gemini-3-Flash, is from the same family. Judge/"
                    "backbone self-preference is not controlled.", kind="our_inference"),
            opus_ev(p, "O03", "evaluated independently by three frontier VLMs: GPT-5.2", "§5.1 Evaluation Protocol",
                    "The main benchmark (120 items) is scored only by VLM judges on 1–5 Likert scales."),
            opus_ev(p, "O04", "Second, a self-evolving experience store accumulates design knowledge derived from "
                              "the Review Agent into a partitioned vector database after each task.", "§1",
                    "The store is written after each task. Whether it is built on the 120 benchmark tasks themselves, "
                    "reset per run or order-controlled is never stated."),
            opus_ev(p, "O05", "Success (Succ.) is binary (0/1), marking valid compilation with all parts.",
                    "§5.1 Evaluation Protocol",
                    "Succ checks compilation and part completeness only, not functional or kinematic correctness."),
            opus_ev(p, "O06", "This cycle improves success rates without fine-tuning.", "§4.6 Experience Store",
                    "The stated store benefit (success rates) is not shown: Table 2 gives Succ 100% both with and "
                    "without the store. The only clear store effect is Avg. Iter. 4.4 → 3.1.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Both seats agree: the primary is decompose_and_delegate/C25 (typed connector artifact plus the "
                      "deterministic FreeCAD constraint solver for exact alignment, and the late-prediction "
                      "ablation). adapt_via_conditioning is supporting for the case-retrieval step. Sub null (son55): "
                      "the backbone is frozen, there is no schema-reading upstream phase, and there is no "
                      "category-level holdout, so C03's tactic is not executed (run convention r09b/r12a/r13b/r14a).",
            "matches": [smatch("son55", p, "decompose_and_delegate"), smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True,
            "resolves_problem": "partial: articulated CAD generation works on the authors' benchmark; the store's "
                                "effect on future tasks is not established",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "index_experience_for_reuse", "H03")],
                           "unassigned": dp_extra("son55", p, "unassigned"),
                           "revision_proposals": dp_extra("son55", p, "revision_proposals")},
        "pattern_mapping": pm("sol", p, [0]) + pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.10992-1"): "local:2604.10992-3"},
            drop={("sol", "local:2604.10992-2")},
            overrides={
                "rs:decompose_and_delegate/RE-1": {
                    "status": "partial",
                    "reason": "Opus (son55): Avg. Iter. (3.1 vs 4.4 without the store) is a partial call-count "
                              "proxy for two arms only. Token/API budget, solver latency and the Single-VLM Loop's "
                              "iteration count are absent.",
                    "evidence_ids": xev("son55", p, "rs:decompose_and_delegate/RE-1") + xev("sol", p,
                                                                                           "local:2604.10992-2"),
                    **merged("sol:local:2604.10992-2 (multi-agent total calls/solver cost, sol unmet)")},
                "rs:decompose_and_delegate/RE-3": {
                    "status": "unmet",
                    "reason": "Opus (revised from son55 unknown): the pinned v2 text is complete and has no appendix "
                              "or appendix references (it ends at Limitations), so prompts are not published in the "
                              "paper. Only a project page is linked. This is a missing disclosure, not missing "
                              "material."},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "unknown",
                    "reason": "Opus (son55): the store is written after each task (opus:O04), but whether it was "
                              "populated from the evaluated benchmark stream, from a separate pool, or reset is not "
                              "stated. Not inferred either way.",
                    "evidence_ids": ["son55:E005", "sol:E003", "sol:E006", "opus:O04"]},
                "rsi:index_experience_for_reuse/S5": {
                    "status": "partial",
                    "reason": "Opus (son55): a store-off ablation exists (ablation c), but it is single-run, quality "
                              "moves by −0.04/+0.02/−0.05 on a 1–5 scale and Succ is 100% in both arms. It certifies "
                              "only the iteration reduction, not the claimed success-rate benefit (opus:O06).",
                    "evidence_ids": ["sol:E006", "sol:E007", "sol:E008", "son55:E007", "son55:E008", "opus:O06"]},
                "local:2604.10992-3": renum("local:2604.10992-1"),
            }),
        "claims": lambda c, p=p: add_counter(c, "C3", ["opus:O06"]),
        "assessment": assess("son55", p, [
            "Opus: §4.6's 'improves success rates' is not shown (Succ 100% with and without the store) (opus:O06).",
            "Opus: judge reliability α 0.58–0.64; Gemini-3-Pro is both judge and backbone (opus:O01, opus:O02)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The articulated-CAD capability gap is concrete and its "
                   "neighbours are named (single-part CAD code loops, non-editable articulated reconstruction, "
                   "assembly datasets for given parts); on its own it would merit 3. But the object that brings the "
                   "paper into this domain, the retained experience store, gets no gap analysis: no case-reuse or "
                   "experience-memory neighbour (ExpeL/Reflexion-style stores are cited only generically) and no "
                   "residual bottleneck that the store addresses. 'First'/'unexplored' framing locates a capability, "
                   "not a non-weight object that was previously fixed.",
                   ["son55:E016", "son55:E017", "sol:E013", "son55:E001"]),
            "M": R("resolved", 3, "Opus sides with sol. The connector contract is a concrete operation with a "
                   "separating prediction against the naive alternative (late prediction degrades Motion 3.82 → 3.16 "
                   "and Succ 100 → 89.2%), and the DESIGN/CODE routing with keep/regenerate partitions is reasoned. "
                   "Not 4: the conditional-independence/O(1) argument is asserted (independent part generation does "
                   "not guarantee geometric compatibility), and the store is generic case retrieval whose "
                   "Good/Issue split is judged by the same VLM pipeline. It makes no prediction that separates it "
                   "from plain trace RAG.",
                   ["son55:E018", "son55:E009", "sol:E001", "sol:E002", "sol:E005", "son55:E003"], ["son55:E008"]),
            "X": R("resolved", 2, "Opus sides with son55. Plan validation, the generate–execute–repair loop, "
                   "routing, deterministic assembly and FAISS partitions are described. But the store's admission "
                   "threshold, retrieval k, summary format, dedup/forgetting/versioning, ArtiCAD's own repair and "
                   "rollback limits, and the validation/judge prompts are not given. The paper has no appendix, so "
                   "the retention path cannot be reconstructed.",
                   ["son55:E002", "son55:E003", "son55:E004", "sol:E004", "sol:E005", "sol:E012"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. CADPrompt and ACD use standard geometric/joint "
                               "metrics with worst-case scoring of failures (credible). But every ArtiCAD-Bench "
                               "number, including all ablations and the store claim, comes from VLM judges only "
                               "(opus:O03), with no human or ground-truth check. α is 0.58–0.64, below the usual "
                               "0.667 floor, yet described as 'robust' (opus:O01). Gemini-3-Pro both judges and "
                               "powers the Pro row (opus:O02). Succ checks compilation only (opus:O05). Store-ablation "
                               "deltas (≤0.05 on 1–5) are within plausible judge noise.",
                               ["son55:E013", "son55:E014", "sol:E010", "opus:O01", "opus:O02", "opus:O03",
                                "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. A same-backbone Single-VLM Loop and three "
                             "single-component ablations exist. The late-prediction ablation is informative. "
                             "Rollback removal also removes visual validation, the store ablation moves quality "
                             "negligibly (Detail reversed), runs are single, and budgets are unmatched.",
                             ["son55:E007", "son55:E008", "son55:E009", "son55:E010", "son55:E011", "sol:E014"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The pipeline is tested on two external "
                           "benchmarks (CADPrompt, ACD), but the store's construction stream, order and reset are "
                           "unstated (opus:O04). The only retained-effect test (ablation c) runs on the same "
                           "self-authored benchmark.",
                           ["son55:E005", "son55:E015", "sol:E006", "opus:O04"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes and failure rates are given, "
                              "but there are no seeds, intervals or tests for main or ablation differences. Judge "
                              "agreement is not run variance.",
                              ["son55:E007", "son55:E009", "sol:E009"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only Avg. Iter. for ArtiCAD vs no-store. There "
                        "are no token/API/latency figures, no iteration count for the Single-VLM Loop (capped at 5 "
                        "retries) and no budget-matched comparison.",
                        ["son55:E021", "sol:E012", "sol:E007", "sol:E008"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text read (the paper has no appendix). In scope (system_method): a "
                  "non-weight experience store is written from Review-Agent judgements after each task and retrieved "
                  "in later tasks. The store is peripheral to the CAD claim. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope via the retained experience store; both seats agree)",
        "figure_dependence": "Figs 1–7 image-only; only Tables 1–4 and text values used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["decompose_and_delegate", "C25"], ["adapt_via_conditioning", None]],
                "C25 agreed. C03 → null: frozen backbone, no schema-reading upstream phase, no category holdout "
                "(run convention r09b/r12a/r13b/r14a).", ["son55:E002", "son55:E008", "sol:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["index_experience_for_reuse", "H03"]],
                "H03 agreed. son55's H00 (its own fit 'low') is rejected. The store holds near-raw case summaries "
                "(requirements, connector plans, code, repair trajectories) reused as few-shot templates. Heuristics "
                "are derived at read time; there is no lesson-abstraction or contrast step at write time.",
                ["sol:E003", "sol:E004", "sol:E005", "son55:E003"], NOSCORE),
            XC(p, "local:2604.10992-2", "revised", "partial",
               "A4: sol's local-2 (total multi-agent calls/solver cost) is the same question as "
               "rs:decompose_and_delegate/RE-1 and is merged there. Final status partial: Avg. Iter. is a partial "
               "call-count proxy (sol's 'unmet' treats the proxy as absent).",
               ["sol:E007", "sol:E008", "sol:E012", "son55:E021"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Verified: only Avg. Iter. for two arms. sol's local-2 merged here.", ["son55:E021"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "Verified: three single-component ablations, single run, budgets unmatched.",
               ["son55:E007", "son55:E008", "son55:E009", "son55:E010"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "revised", "unmet",
               "The paper has no appendix and no prompts (complete v2 text ends at Limitations). This is non-"
               "disclosure, so 'unknown' becomes unmet.", []),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "met",
               "Verified: ArtiCAD-Bench plus external CADPrompt (200) and ACD (354), and a physical prototype.",
               ["son55:E015"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "Verified: same-backbone Single-VLM Loop compared; margins modest, budget unmatched.",
               ["son55:E011", "son55:E012"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "met",
               "Verified: the late-prediction ablation links the connector seam to Motion and Succ.",
               ["son55:E009", "son55:E018"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unknown",
               "The construction stream is not stated. sol's 'unmet' amounts to 'separation not shown', which is the "
               "same fact, and the failure itself cannot be confirmed from the text.",
               ["son55:E005", "opus:O04"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "sol", "partial",
               "Verified: asymmetric partition use (Good-only templates for generation) but no cap or relevance "
               "gate stated.", ["sol:E005"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "The ablation exists but certifies only the iteration reduction. Quality deltas are negligible and "
               "Succ is equal (opus:O06).", ["sol:E007", "sol:E008", "opus:O06"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: concrete CAD gap, but no gap or neighbour for the retained store that brings the "
                "paper into scope.", ["son55:E016", "son55:E017", "sol:E013"], "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "sol", 3,
                "See ratings.M: the connector makes a separating prediction confirmed by ablation; the store is "
                "generic, so not 4.", ["son55:E009", "son55:E018", "sol:E001"], "+5 vs son55 (20×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2,
                "See ratings.X: store admission/retrieval/versioning, repair limits and prompts are unspecified; no "
                "appendix.", ["son55:E002", "son55:E003", "son55:E004"], "−5 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", 2,
                "See ratings.E.measurement: main benchmark judged by VLMs only, α below 0.667, judge/backbone "
                "overlap, Succ = compilation.", ["son55:E013", "son55:E014", "opus:O01", "opus:O02", "opus:O05"],
                "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims[C3].counterevidence / assessment.unresolved",
             "sol_value": "store effect reported as small quality change + fewer iterations",
             "son55_value": "store effect reported as small quality change + fewer iterations", "final_value":
                 "plus: §4.6 claims the store 'improves success rates', but Succ is 100% with and without it",
             "reason": "Shared omission, no rating change. Neither seat flagged that the paper's stated store benefit "
                       "(success rates) is directly unsupported by its own Table 2. Recorded as claim counterevidence "
                       "and in E.measurement/S5.",
             "evidence_ids": ["opus:O06", "sol:E007", "sol:E008"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text first (no appendix exists). Initial view: "
                "in scope only via the retained experience store, which is peripheral. Evidence level task. G 2, M 3, "
                "X 2, Em 2, Ec 2, Eh 1, Es 1, E.cost 1. Store ablation: quality flat, iterations down.",
            "integrity_checks": "Both seats a1 on 2604.10992v2, material sha 6f98376a…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid. son55's "
                                "'appendix/prompts missing from material' is corrected: the paper has none.",
            "core_claim_check": "Strongest supported claim: on a self-authored VLM-judged benchmark, connector-based "
                                "decomposition beats a same-backbone single-loop baseline, and late prediction hurts. "
                                "External single-part (CADPrompt) and articulated (ACD) results use standard metrics. "
                                "The store reduces repair iterations on the same stream; a retained quality or success "
                                "benefit is not shown. claim_support scoped.",
            "rating_agreement": "Ec, Eh, Es, E.cost agree and were re-checked. G, X, Em → son55; M → sol. Final 50.0.",
        },
    }

    # =========================================================== 2604.11610 CluE (Δ1.25)
    p = "2604.11610"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Our CluE adopts the exact same hyperparameters as MemEvolve.", "Appendix A.2",
                    "CluE vs MemEvolve is a same-hyperparameter, same-evaluation-budget comparison that isolates the "
                    "cluster-based analysis as one bundle (not its individual steps)."),
            opus_ev(p, "O02", "we hold out one dataset per category, i.e., LongMemEval ( Wu et al., 2025 ) , "
                              "GPQA-Diamond ( Rein et al., 2023 ) , and ToolBench ( Guo et al., 2024 ) , as "
                              "out-of-distribution test sets.", "§3.2",
                    "The two LLM-judged datasets (LongMemEval, ToolBench) are OOD test sets only. They take no part in "
                    "evolution or selection."),
            opus_ev(p, "O03", "SoPR = solvable pass rate (LLM judge), LLM Judge = LLM-as-judge evaluation.",
                    "Table 6 caption",
                    "Every in-distribution training dataset uses an accuracy/EM/rule/success/pass@1 reward. The LLM "
                    "judge appears only in the held-out OOD sets."),
            opus_ev(p, "O04", "The prompts for the different LLM roles in the CluE optimization pipeline are "
                              "provided in Figures 10 , 11 , 12 , and 13 .", "Appendix C.2",
                    "The optimiser prompts are present as text listings in the pinned material, contrary to son55's "
                    "note that they are images."),
            opus_ev(p, "O05", "You are a clustering agent for memory extraction prompt evolution",
                    "Figure 11 listing (Appendix C.2)",
                    "Example of a prompt listing present verbatim in the text (Cluster Manager)."),
            opus_ev(p, "O06", "introducing moderate optimizer overhead (221 vs. 30 calls) at a marginal wall-time "
                              "cost", "Appendix B.2",
                    "The optimiser-call budget is disclosed and not matched (7×). Evaluation calls are equal (1,150)."),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats agree: mixed training logs are partitioned by an LLM-summarised extraction scenario "
                      "and each partition gets its own analysis before synthesis. Sub null: C04 is a "
                      "model-compression tactic.",
            "matches": [smatch("son55", p, "heterogeneous_decomposition")],
            "executes_pattern": True,
            "resolves_problem": "partial: better heterogeneous-task generalisation in the single-step setting; "
                                "clustering's own causal role is not isolated",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H10"),
                                       dmatch("sol", p, "make_the_improver_editable", "H21")],
                           "unassigned": dp_extra("son55", p, "unassigned"),
                           "revision_proposals": dp_extra("son55", p, "revision_proposals")},
        "pattern_mapping": pm("sol", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.11610-1"): "local:2604.11610-3",
                    ("son55", "local:2604.11610-2"): "local:2604.11610-5"},
            overrides={
                "local:2604.11610-3": {
                    "status": "unmet",
                    "reason": "Opus (revised from sol partial; = son55's local-1): the question is variance across "
                              "independent evolution runs. None is reported. The three-repeat std covers only "
                              "extraction+answering of one evolved prompt on small test sets.",
                    **merged("son55:local:2604.11610-1 (independent evolution runs, son55 unmet)",
                             xev("son55", p, "local:2604.11610-1"))},
                "rsi:attribute_and_patch_incumbent/F4": {
                    "status": "met",
                    "reason": "Opus (revised from son55 partial): the certifying signal is never self-constructed. "
                              "Every training dataset uses a ground-truth reward (accuracy/EM/rule/success/pass@1), "
                              "and the two LLM-judged datasets are OOD test sets that play no part in selection "
                              "(opus:O02, opus:O03). A shared Qwen3-32B backbone is a separate (F5-type) concern.",
                    "evidence_ids": ["son55:E018", "son55:E026", "son55:E027", "opus:O02", "opus:O03"]},
                "local:2604.11610-5": renum("local:2604.11610-2"),
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, [
            "Opus: OOD advantage is only on LongMemEval; GPQA-D (48.48 vs GEPA 50.00) and ToolBench (tie with "
            "MemEvolve, below ACE 26.82) do not favour CluE."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed object (a static extraction prompt) and its "
                   "residual are measured: no static prompt dominates (Table 1), and GEPA/ACE/MemEvolve trade "
                   "categories (Table 2). The closest clustering neighbour (MemSkill) is cited but not run, and the "
                   "'designed for homogeneous distributions' premise is asserted.",
                   ["son55:E001", "son55:E002", "son55:E008", "son55:E022", "son55:E023", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Logs → scenario summaries → clusters → per-cluster "
                   "analysis → scoped synthesis responds to the stated instability/dilution dilemma and predicts a "
                   "taxonomy-shaped prompt (Fig. 4/App. B.3). The causal role of clustering vs extra analysis calls "
                   "is not separated.",
                   ["son55:E003", "son55:E004", "son55:E030", "sol:E002", "sol:E003", "sol:E004"],
                   ["son55:E014", "son55:E024"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Rounds, batch sizes, the tournament with fresh+stability "
                   "samples, the persistent cluster pool and all optimiser prompts are given. Opus correction to "
                   "son55: the prompts are text listings in the pinned material (opus:O04, opus:O05), not images. No "
                   "per-edit regression check, versioning or rollback for the retained prompt.",
                   ["son55:E015", "son55:E016", "son55:E028", "sol:E005", "sol:E006", "opus:O04", "opus:O05"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Downstream-utility rewards are mostly "
                               "ground truth (opus:O03), with a No-Memory floor. LLM judges only on two OOD sets. "
                               "Source conversations are completed by the same Qwen3-32B used as generator.",
                               ["son55:E018", "son55:E026", "son55:E027", "sol:E011", "opus:O03"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-hyperparameter comparison with MemEvolve "
                             "isolates the cluster-analysis bundle (opus:O01), and two seeds and two backends are "
                             "tried. There is no step ablation or random-cluster control, 7× optimiser calls are "
                             "unmatched, and prompt length is uncontrolled.",
                             ["son55:E007", "son55:E012", "son55:E014", "son55:E024", "sol:E005", "opus:O01"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. 330 training examples, disjoint in-distribution "
                           "remainder and three whole held-out datasets. Possible target-query sharing between "
                           "in-distribution train and test pairs (App. A.1) and the hand-picked continual tasks "
                           "limit it to 3.",
                           ["son55:E005", "son55:E006", "son55:E009", "son55:E010", "sol:E010", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): three-repeat std on small test sets and "
                              "visible regressions, but no variance across evolution runs and no tests.",
                              ["son55:E019", "sol:E012", "sol:E013"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Wall time, optimiser calls and evaluation calls are "
                        "reported for all four optimisers. The closest baseline is matched on evaluation calls "
                        "(1,150) and hyperparameters, and CluE's 7× optimiser-call overhead is disclosed "
                        "(opus:O06). Not 4: no token/dollar totals and no control matched on optimiser calls. sol's 2 "
                        "treats a disclosed, partly matched budget like an unreported one (cf. EvolveRouter r14b, "
                        "where no matched comparison existed).",
                        ["son55:E014", "sol:E014", "sol:E018", "opus:O06"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text with Appendices A–C (including the prompt listings) read. In scope "
                  "(system_method): a non-weight memory-extraction prompt is evolved from task feedback, retained "
                  "and evaluated on disjoint and held-out data. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–4 image-only; prompt Figs 5–14 are text listings; Tables 1–11 used.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H10"], ["make_the_improver_editable", "H21"]],
                "H10 agreed. sol's H21 kept as supporting: the evolved object is the agent's memory-write "
                "instruction, i.e. part of the inner experience-learning mechanism, scored by the downstream utility "
                "of what it writes. This matches H21's target (memory/context design) as for M* in this batch, at "
                "medium fit, since evolution is single-step.",
                ["sol:E008", "sol:E015", "sol:E016", "sol:E017"], NOSCORE),
            XC(p, "local:2604.11610-3", "revised", "unmet",
               "Merged with son55's local-1 (same question). No independent evolution runs are reported, so unmet.",
               ["sol:E012", "son55:E019"]),
            XC(p, "local:2604.11610-4", "sol", "partial",
               "Verified: calls and wall time but no tokens or dollars.", ["sol:E014", "sol:E018"]),
            XC(p, "rs:heterogeneous_decomposition/RE-2", "son55", "met",
               "Verified: wall-clock time is reported for all four optimisers (deployment units).", ["son55:E014"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "son55", "unmet",
               "Verified: Summarizer, Cluster Manager, per-cluster Analyzer and Proposer are not ablated separately. "
               "Only the whole bundle is compared with MemEvolve.", ["son55:E014", "son55:E015"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "son55", "partial",
               "Verified: direct competitors included; no random-cluster or matched-optimiser-call control.",
               ["son55:E014", "son55:E024", "son55:E025"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "son55", "met",
               "Verified: heterogeneity is analysed empirically (Tables 1–2, App. B.3).",
               ["son55:E008", "son55:E022", "son55:E028"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F2", "son55", "partial",
               "Verified: clustering is added to MemEvolve's analyzer–proposer loop while selection is inherited. "
               "The added topology is substantive, so partial.", ["son55:E015", "son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "revised", "met",
               "The LLM-judged datasets are OOD test-only and every selection reward is ground truth, so the failure "
               "mode is avoided.", ["son55:E026", "opus:O02", "opus:O03"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H10", "sol", "partial",
               "Verified: diagnosed, scoped rewrites retained via tournament; the protected set is small.",
               ["sol:E002", "sol:E003", "sol:E004", "sol:E005", "sol:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Verified: the tournament keeps the incumbent unless beaten. The Survey-seed run shows preservation; "
               "there is no per-edit regression check.", ["son55:E012", "son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: logs are clustered by scenario before any edit.", ["son55:E003", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "partial",
               "Verified: generality is claimed but tested only on extraction prompts.", ["son55:E003"]),
            XC(p, "rsi:make_the_improver_editable/H21", "sol", "partial",
               "Verified: writer prompt evolved; inner-loop evaluation is single-step, with continual use checked "
               "on two tasks.", ["sol:E008", "sol:E015", "sol:E016", "sol:E017"]),
            XC(p, "rsi:make_the_improver_editable/S1", "sol", "met",
               "Verified: outer tournament and reward fixed.", ["sol:E005", "sol:E006"]),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 3,
                "See ratings.E.cost: all optimisers costed, and the closest baseline matched on evaluation calls "
                "and hyperparameters.", ["son55:E014", "opus:O06"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text first. Initial view: in scope, retained "
                "(evolved prompt frozen and tested on disjoint and held-out datasets). G 3, M 3, X 3, Em 3, Ec 2, "
                "Eh 3, Es 2, E.cost 2–3. The MemEvolve comparison is a same-hyperparameter bundle ablation.",
            "integrity_checks": "Both seats a1 on 2604.11610v1, material sha 81e47763…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid. son55's "
                                "'prompt figures are images' is a reading error (they are listings); no field "
                                "depends on it.",
            "core_claim_check": "Strongest supported claim: a CluE-evolved extraction prompt beats GEPA/ACE/MemEvolve "
                                "prompts on disjoint in-distribution tests (Qwen3 and Gemini backends, Simple and "
                                "Survey seeds) and does not drop below the seed OOD. 'Consistent' gains do not hold "
                                "for Gemini agentic (−5.93%) or OOD GPQA/ToolBench. claim_support scoped.",
            "rating_agreement": "G, M, X, Em, Ec, Eh, Es agree and were re-checked; E.cost → son55. Final 70.0.",
        },
    }

    # =========================================================== 2604.11811 M* (Δ3.75)
    p = "2604.11811"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Unseen 4,652 trajectories 145 ep. 50 ep.", "Appendix B.1 Table 5",
                    "Table 5 states 50 ALFWorld Unseen test episodes."),
            opus_ev(p, "O02", "Table 10: Complete per-category results for ALFWorld Unseen.", "Appendix I.1 Table 10",
                    "Table 10's category sizes sum to 42 (8+1+11+1+7+6+8), and every Unseen rate in Table 1 is a "
                    "multiple of 1/42 (e.g. 0.881 = 37/42, 0.738 = 31/42, 0.619 = 26/42). None is a multiple of 1/50. "
                    "Eight stated test episodes are unaccounted for.", kind="our_inference"),
            opus_ev(p, "O03", "Mstar improves performance over existing static memory harnesses across all evaluated "
                              "tasks.", "Abstract",
                    "Contradicted for ALFWorld Seen: M* 0.700 vs GEPA+VS 0.820, Trajectory Retrieval 0.780 and Vector "
                    "Search 0.720 (Table 1).", kind="our_inference"),
            opus_ev(p, "O04", "Table 1 shows that Mstar achieves the highest score on seven of eight reported "
                              "metrics.", "§5",
                    "The body states the narrower 7-of-8 result."),
            opus_ev(p, "O05", "Toolkit LLM call budget 1 call per read / write invocation", "Appendix D.2 Table 7",
                    "The runtime budget is specified; App. G.1 lists allowed imports, a 3,000-char read limit and 60 s "
                    "timeouts."),
            opus_ev(p, "O06", "Listing 4: [Revised] ALFWorld evolved write() — canonical state extraction and fallback "
                              "parsing.", "Appendix F.1",
                    "The evolved program listings are present as text in the pinned material, contrary to son55's "
                    "note that they are not in text form."),
            opus_ev(p, "O07", "All experiments use gpt-5.4-mini as the task agent, judge, and toolkit model",
                    "Appendix D.1",
                    "The rubric judge for HealthBench/PRBench (4 of 7 configurations) and the LoCoMo L-J judge are the "
                    "same model as the task agent. The same judge supplies the search fitness on the static "
                    "validation subset."),
            opus_ev(p, "O08", "Table 14: Best validation score during evolution by seed.", "Appendix I.2",
                    "LoCoMo best-validation scores by seed are 0.333/0.273/0.289/0.312/0.333, while test scores are "
                    "0.459/0.463/0.364/0.394/0.423 (Table 13). The lowest-validation seed has the highest test score, "
                    "so the static-subset fitness ranks programs loosely.", kind="our_inference"),
            opus_ev(p, "O09", "LoCoMo 0.459 0.463 0.364 0.394 0.423 0.421 0.042 10.0% 0.373", "Appendix I.2 Table 13",
                    "Table 1's LoCoMo value (0.459) is seed 0, above the five-seed mean (0.421)."),
            opus_ev(p, "O10", "The aggregated score on the static validation set serves as the performance metric for "
                              "the current memory program.", "§3.2",
                    "Selection is on a static validation subset (32–60 items); reporting is on a disjoint test split."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats agree: the conventionally fixed, hand-designed memory harness becomes a jointly "
                      "searched variable. Sub null (C15/C23/C24 are geometry/diffusion/conditioning tactics).",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H21"),
                                       dmatch("son55", p, "population_search_executable_fitness", "H14")],
                           "unassigned": dp_extra("son55", p, "unassigned"),
                           "revision_proposals": dp_extra("son55", p, "revision_proposals")},
        "pattern_mapping": pm("son55", p) + [{
            "rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
            "domain_main": "population_search_executable_fitness", "domain_sub": "H14",
            "operation_correspondence": "The liberated harness is searched as executable code: softmax-sampled "
                                        "parents, LLM code mutation, compile-fix gate, validation fitness, pool "
                                        "archive.",
            "necessary_conditions_and_differences": "H14 expects an automated, hard-to-game evaluator. That holds "
                                                    "for LoCoMo F1 and ALFWorld success, while the rubric configs "
                                                    "use a same-model LLM judge (opus:O07). The archive's value is "
                                                    "tested only on LoCoMo (−Diversity, Max parent).",
            "evidence_ids": ["son55:E008", "son55:E013", "opus:O07", "opus:O10"], "origin": "opus"}],
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.11811-1"): "local:2604.11811-3"},
            overrides={
                "local:2604.11811-1": {
                    "score_item": "E.statistics",
                    "reason": "Opus (sol, verified): Table 5 says 50 Unseen test episodes (opus:O01), but the "
                              "category sizes sum to 42 and every Unseen rate is k/42 (opus:O02). Under A2 this "
                              "failure-denominator defect is charged once, in E.statistics (moved from sol's "
                              "E.measurement).",
                    "evidence_ids": xev("sol", p, "local:2604.11811-1") + ["opus:O01", "opus:O02"]},
                "rsi:make_the_improver_editable/F3": {
                    "status": "met",
                    "reason": "Opus (son55): fitness uses the static validation subset and reporting uses a disjoint "
                              "held-out test split (opus:O10), so benchmark reuse does not pass for improvement. "
                              "Subset-fitness noise (opus:O08) is a selection-quality issue, not F3.",
                    "evidence_ids": ["son55:E009", "son55:E010", "son55:E011", "sol:E04", "opus:O10"]},
                "local:2604.11811-3": {**renum("local:2604.11811-1"),
                                       "evidence_ids": xev("son55", p, "local:2604.11811-1") + ["opus:O03"]},
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, [
            "Opus: ALFWorld Unseen denominator 42 vs stated 50 (opus:O01, opus:O02).",
            "Opus: abstract 'all evaluated tasks' contradicted by ALFWorld Seen (opus:O03)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A concrete fixed object (hand-designed memory schema, "
                   "logic and instructions), a measured residual (best baseline varies by task; transfer fails) and "
                   "named neighbours (MemEvolve, GEPA, ADAS). The closest closed-space evolver is not run, and "
                   "'subsumes closed spaces' is asserted.",
                   ["son55:E015", "son55:E025", "son55:E026", "sol:E01", "sol:E05"]),
            "M": R("resolved", 3, "Opus sides with son55. Jointly editing Schema/Logic/Instruction from execution "
                   "traces with population selection targets per-task mismatch and makes distinguishable predictions "
                   "(task-specific programs, diversity matters, instruction-only is insufficient). Not 4: the premise "
                   "that reflective diagnosis rather than plain mutation drives the gains is untested, and the "
                   "selection signal is weak. Best-on-validation over a 32–60-item static subset ranks programs "
                   "loosely: LoCoMo's lowest-validation seed has the highest test score (opus:O08).",
                   ["son55:E007", "son55:E008", "son55:E012", "son55:E013", "sol:E02", "sol:E03", "opus:O10"],
                   ["opus:O08"]),
            "X": R("resolved", 4, "Opus sides with son55. The search space and toolkit whitelist, runtime constraints "
                   "(opus:O05), the compile-fix gate (k=3), softmax parent sampling (τ=0.15), static/rotating subset "
                   "construction, the best-on-validation → disjoint-test retention rule, the reflector prompt and the "
                   "evolved program listings (opus:O06) are all in text, and code is released. Failure and transfer "
                   "boundaries (drift to task-specific heuristics, negative transfer, category losses, model-pair "
                   "dependence) are stated. sol's missing 'security certificate' is not an X condition here.",
                   ["son55:E006", "son55:E009", "son55:E021", "son55:E029", "son55:E030", "son55:E034", "opus:O05",
                    "opus:O06"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol on the value, with revised grounds. LoCoMo token "
                               "F1 and ALFWorld success are credible. But 4 of 7 configurations (HealthBench, "
                               "PRBench), which carry the largest gains, are scored by gpt-5.4-mini rubric judging. "
                               "That model is also the task agent and the search fitness (opus:O07), so the search "
                               "optimises against an unvalidated same-model judge (Goodhart risk). LoCoMo L-J uses the "
                               "same model. sol's denominator point is moved to E.statistics (A2).",
                               ["son55:E023", "son55:E024", "son55:E031", "sol:E15", "opus:O07"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Instruction/code/parent/population ablations "
                             "run on LoCoMo only, single run. No no-reflection or random-mutation control, no other "
                             "memory evolver, and evolution compute plus a stronger reflector are not matched.",
                             ["son55:E012", "son55:E013", "son55:E014", "son55:E028", "sol:E06"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Fitness on static validation and reporting on a "
                           "disjoint test split with episode/query disjointness. Cross-task transfer failure is "
                           "reported. Tests are small, there is no contamination check, and the abstract's "
                           "'all tasks' claim is contradicted on ALFWorld Seen (opus:O03).",
                           ["son55:E009", "son55:E010", "son55:E011", "son55:E015", "sol:E05", "opus:O03"]),
            "E.statistics": R("resolved", 2, "Opus sides with sol. Five full-search seeds with SD on 3 of 7 "
                              "configurations exceed the A2 2-step, but there are no intervals or tests, baselines "
                              "and ablations are single runs, Table 1 reports seed 0 (above the mean on LoCoMo: "
                              "0.459 vs 0.421) (opus:O09), and the ALFWorld Unseen denominator is 42 rather than "
                              "the stated 50 (opus:O01, opus:O02). Not 3.",
                              ["son55:E016", "son55:E017", "son55:E018", "sol:E07", "opus:O01", "opus:O02",
                               "opus:O09"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Calls by role, tokens, dollars and wall-clock per "
                        "benchmark for M* and Vector Search/No Memory, plus the one-time vs inference split. GEPA "
                        "costs and a matched-budget comparison are missing.",
                        ["son55:E019", "son55:E020", "sol:E10"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text with Appendices A–L (including the evolved program listings and the "
                  "reflector prompt) read. In scope (system_method, H21): an executable non-weight memory harness is "
                  "searched from execution feedback, retained and evaluated on held-out splits. All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–5 image-only (transfer bars in Fig. 5 not read); Tables 1–14 and listings used.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["make_the_improver_editable", "H21"], ["population_search_executable_fitness", "H14"]],
                "H21 agreed. son55's H14 is kept as supporting: executable programs are evolved by LLM mutation "
                "from softmax-sampled parents in a pool against an automated fitness, and the pool is load-bearing "
                "(−Diversity ablation). Fit is medium because half the configs use a same-model LLM-judge fitness.",
                ["son55:E008", "son55:E013", "opus:O10"], NOSCORE),
            XC(p, "local:2604.11811-2", "son55", "partial",
               "Verified: Table 1 = seed 0, above the LoCoMo mean (opus:O09); the multi-seed table is separate.",
               ["son55:E003", "son55:E017", "opus:O09"]),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "partial",
               "Verified: the −Code ablation (LoCoMo) supports the bottleneck premise for one benchmark only.",
               ["son55:E012", "son55:E014"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "partial",
               "Verified: eight baselines incl. GEPA, but no closed-space memory evolver.",
               ["son55:E004", "son55:E025", "son55:E028"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", "partial",
               "Verified: four ablations on LoCoMo only; Schema, compile-fix and rotating subset not separated.",
               ["son55:E012", "son55:E013", "son55:E014"]),
            XC(p, "rs:generative_process_redesign/RE-5", "son55", "unmet",
               "Verified: $12–90 of evolution with a stronger reflector, against baselines with no search; no "
               "equal-compute search baseline.", ["son55:E019", "son55:E020", "son55:E024"]),
            XC(p, "rs:generative_process_redesign/RE-6", "son55", "met",
               "Verified: per-category breakdown, cost table, transfer failure and limitations reported.",
               ["son55:E015", "son55:E019", "son55:E021", "son55:E027"]),
            XC(p, "rsi:make_the_improver_editable/F3", "son55", "met",
               "Selection on validation, reporting on a disjoint test split. sol's 'partial' charges scope limits "
               "that are not F3.", ["son55:E009", "son55:E010", "opus:O10"]),
            XC(p, "rsi:make_the_improver_editable/F5", "son55", "partial",
               "Verified: same-model rubric judge as fitness, and a stronger reflector model (opus:O07).",
               ["son55:E023", "son55:E024", "opus:O07"]),
            XC(p, "rsi:make_the_improver_editable/S1", "sol", "met",
               "Verified: outer algorithm, task model and metric fixed.", ["sol:E02", "sol:E04"]),
            XC(p, "rsi:make_the_improver_editable/S2", "sol", "met",
               "Verified: program fitness is the downstream task score with rebuilt memory.", ["sol:E01", "sol:E02"]),
            XC(p, "rsi:make_the_improver_editable/S6", "son55", "met",
               "Verified: memory reified as one executable program; held-out split; retained-design ablation "
               "(LoCoMo).", ["son55:E001", "son55:E009", "son55:E012"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial",
               "Verified: executable fitness for LoCoMo F1/ALFWorld; LLM-judged rubrics elsewhere; small subsets.",
               ["son55:E006", "son55:E023", "son55:E034"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 3,
                "See ratings.M: the reflection-vs-plain-mutation premise is untested, and the static-subset fitness "
                "is loose (opus:O08).", ["son55:E012", "son55:E013", "opus:O08"], "−5 vs sol (20×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 4,
                "See ratings.X: every operation, constraint and retention rule is reconstructable, with listings in "
                "text.", ["son55:E006", "son55:E029", "opus:O05", "opus:O06"], "+5 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement: the same-model judge is the fitness and the metric for the largest-gain "
                "configs. The denominator issue is moved to E.statistics.", ["son55:E024", "opus:O07"],
                "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 2,
                "See ratings.E.statistics: seeds on 3/7 configs with no intervals or tests, a seed-0 headline, and "
                "the 42-vs-50 denominator.", ["son55:E017", "opus:O02", "opus:O09"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text first. Initial view: in scope, retained "
                "(evolved program selected on validation, tested on disjoint split). G 3, M 3, X 3–4, Em 2, Ec 2, "
                "Eh 3, Es 2, E.cost 3. Abstract's 'all tasks' contradicted by ALFWorld Seen.",
            "integrity_checks": "Both seats a1 on 2604.11811v2, material sha d14eea27…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid. son55's 'evolved "
                                "listings not in text' is a reading error (opus:O06).",
            "core_claim_check": "Strongest supported claim: an evolved executable memory program beats the compared "
                                "fixed harnesses on 7 of 8 held-out metrics and is stable over five search seeds on "
                                "three configs. The advantage over an equal-compute alternative search, and judge "
                                "validity for the rubric configs, are not shown. claim_support scoped.",
            "rating_agreement": "G, Ec, Eh, E.cost agree and were re-checked. M, X → son55; Em, Es → sol. Final 72.5.",
        },
    }

    # =========================================================== 2604.12231 Thought-Retriever (Δ7.5)
    p = "2604.12231"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "By providing these models with the paper title and abstract, we ask them to generate "
                              "diverse questions at varying levels of abstraction.", "Appendix D",
                    "LLM-based construction queries are conditioned on each paper's abstract."),
            opus_ev(p, "O02", "To model user queries in real-world scenarios for guiding thought generation, we "
                              "primarily use two approaches", "Appendix D",
                    "These queries drive thought generation, i.e. they determine what enters the thought memory."),
            opus_ev(p, "O03", "For Abstract-single , the generated abstract is directly compared with the paper’s "
                              "original abstract.", "§3",
                    "For Abstract-single the abstract is the label. Construction queries built from it, and thoughts "
                    "summarising query+answer, can carry label content into memory. Which query method was used for "
                    "which evaluated item is never stated, and no overlap audit is reported.", kind="our_inference"),
            opus_ev(p, "O04", "Specifically, we utilize the ground truth answers to calculate the ROUGE-L overlap "
                              "scores with all corpus chunks", "Appendix P.2",
                    "The oracle context is selected by ROUGE-L against the ground truth."),
            opus_ev(p, "O05", "Thought-Retriever consistently outperforms the Oracle baseline on AcademicEval "
                              "datasets", "Appendix P.2",
                    "Beating a ground-truth-selected oracle with the same generator and window is what label exposure "
                    "would predict. The paper's compression explanation is not separated from it.",
                    kind="our_inference"),
            opus_ev(p, "O06", "AcademicEval is a good benchmark for evaluating the zero-shot performance of LLM and has "
                              "no risk of label leakage and overfitting.", "§4.2",
                    "The no-leakage claim refers to pretraining contamination and is not audited against the paper's "
                    "own abstract-conditioned memory construction."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering"],
            "outside_taxonomy": False,
            "reason": "Opus: a frozen generator conditioned on retrieved raw chunks plus stored thoughts is "
                      "adapt_via_conditioning. Sub null: no schema-reading upstream phase and no category holdout "
                      "(run convention), so sol's C03 is dropped. son55's supporting "
                      "self_supervised_signal_engineering is kept: thoughts are self-generated and admitted on the "
                      "generator's own confidence plus a novelty filter, and the filter is ablated (w/o Filter). That "
                      "is the card's curation-of-self-generated-signal condition (r02a convention). Sub null: nothing "
                      "is trained on the signal.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": True,
            "resolves_problem": "partial: gains over raw-chunk retrieval are reported, but leakage and compute "
                                "parity are unresolved",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H04")],
                           "unassigned": dp_extra("son55", p, "unassigned"),
                           "revision_proposals": dp_extra("son55", p, "revision_proposals")},
        "pattern_mapping": pm("sol", p, rs_sub=None) + pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.12231-1"): "local:2604.12231-3",
                    ("son55", "local:2604.12231-2"): "local:2604.12231-4"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "partial",
                    "reason": "Opus (sol): the same-retriever raw-chunk control (Contriever row) and App. Q's "
                              "cold-start vs prefilled comparison isolate the thought memory. But construction "
                              "exposes the memory to extra, abstract-conditioned query information (opus:O01), which "
                              "is exactly the 'broader exposure' confound RE-1 asks to exclude."},
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "unmet",
                    "reason": "Opus (son55): no overlap or contamination analysis between abstract-derived "
                              "construction queries and evaluation labels (opus:O01, opus:O03). App. Q is a split, "
                              "not an overlap audit, and §4.2's no-leakage claim concerns pretraining (opus:O06).",
                    "evidence_ids": ["son55:E016", "son55:E017", "son55:E019", "sol:E08", "sol:E11", "opus:O03",
                                     "opus:O06"]},
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "met",
                    "reason": "Opus (son55): longer context (Full Context, OpenOrca-8k, Nous Hermes-32k), sparse/"
                              "dense retrievers, IRCoT, RECOMP and MemWalker are all compared. The unmatched "
                              "construction budget is an E.cost/E.causality matter, not RE-3."},
                "rsi:abstract_experience_into_guidance/S3": {
                    "status": "partial",
                    "reason": "Opus (sol): a self-judge (binary confidence) decides admission, and a human agreement "
                              "check (96%/93%) exists. There is no outcome grounding, so partial rather than met or "
                              "unmet."},
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "unmet",
                    "reason": "Opus (son55): only a write-time novelty filter. No operation acts on existing "
                              "entries (no consolidation, forgetting, delta edits or revision)."},
                "local:2604.12231-3": {**renum("local:2604.12231-1"),
                                       "evidence_ids": xev("son55", p, "local:2604.12231-1") + ["opus:O01", "opus:O03",
                                                                                               "opus:O05"]},
                "local:2604.12231-4": renum("local:2604.12231-2"),
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, [
            "Opus: construction queries conditioned on the abstract (= Abstract-task label) with no audit; the "
            "method beats a GT-selected oracle (opus:O01, opus:O03, opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The top-K/rigid-tree limitation is real and neighbours "
                   "are named (MemWalker, RECOMP, IRCoT), but agent-experience memories of the same category are not "
                   "examined and the 'self-evolving' gap is asserted.",
                   ["son55:E002", "son55:E003", "son55:E033", "son55:E036", "sol:E01"]),
            "M": R("resolved", 2, "Opus sides with son55. Retrieve → answer → query-conditioned abstraction → "
                   "confidence/novelty gate → append → later retrieval is concrete, with a plausible recall "
                   "mechanism. But retention is decided only by the generator's own binary confidence on its own "
                   "answer, with no outcome signal. The key premise, that a self-judged summary of Q+A beats raw "
                   "evidence, is only weakly tested. The oracle-beating 'compression' explanation (opus:O05) makes no "
                   "prediction that separates it from label exposure.",
                   ["son55:E001", "son55:E004", "son55:E007", "sol:E01", "sol:E02"], ["son55:E005", "opus:O05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1 and thresholds (K=8, ε=0.85, Contriever) "
                   "are given, but the memory-population protocol for Table 2, the prompts (image-only figures), and "
                   "update/forget/version rules are missing.",
                   ["son55:E004", "son55:E006", "son55:E018", "sol:E09"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. ROUGE-L F1 (called 'semantic "
                               "similarity'), win rate from a single Qwen1.5-72B judge, and GPT-4o-generated labels "
                               "for Abstract-multi. Human checks covered thought quality only, not output quality.",
                               ["son55:E014", "son55:E015", "son55:E026", "sol:E10"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. A thoughts-off same-retriever control, "
                             "cheaper-alternative baselines and a joint filter ablation exist. Construction compute "
                             "is unmatched, and confidence and merge are ablated together. Leakage is charged once, "
                             "under E.holdout (A2).",
                             ["son55:E010", "son55:E011", "son55:E020", "son55:E025", "sol:E07"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Construction queries are LLM-generated from each "
                           "paper's title and abstract (opus:O01, opus:O02). The abstract is the Abstract-single "
                           "label (opus:O03). The main table's memory-building protocol is never stated, and no "
                           "overlap audit is reported (§4.2's 'no risk of label leakage' concerns pretraining, "
                           "opus:O06). Beating a ground-truth-selected oracle (opus:O04, opus:O05) is consistent with "
                           "exposure. Not 0: App. Q gives a disjoint 50/50 split (about 15 test cases per set) with "
                           "small cold-start → prefilled gains.",
                           ["son55:E012", "son55:E017", "son55:E019", "son55:E021", "son55:E023", "opus:O01",
                            "opus:O03", "opus:O04", "opus:O05", "opus:O06"], ["sol:E11", "sol:E13"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): case counts (30–100) and a visible "
                              "non-improvement, but no seeds, intervals or tests; 0.01–0.015 F1 differences on about "
                              "15 cases.", ["son55:E009", "son55:E022", "sol:E18"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Per-query latency for all methods and the storage "
                        "footprint are given, but not thought-generation calls/tokens or memory-construction cost, "
                        "despite the 'little overhead' claim.",
                        ["son55:E029", "son55:E030", "sol:E14", "sol:E15"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text with Appendices A–T read (prompt figures are image-only). In scope "
                  "(system_method): self-generated, self-gated thoughts are retained in a non-weight memory and "
                  "reused by later queries. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–17 image-only (incl. prompts and Figs 5–8 curves); Tables 1–16 used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["self_supervised_signal_engineering", None]],
                "C03 → null (run convention). Self-signal supporting card kept: the self-confidence-gated, "
                "self-generated memory has a w/o-Filter ablation.", ["son55:E004", "son55:E005", "son55:E025"],
                NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H04"]],
                "H00 agreed (abstracted, query-conditioned knowledge points written to a persistent store). son55's "
                "H04 is kept at low fit: the paper's representational claim is a query-driven hierarchy of thoughts "
                "over raw chunks with recursive provenance and abstraction levels, contrasted with MemWalker's tree. "
                "It has linking and dedup, but no decay.",
                ["son55:E006", "son55:E007", "sol:E02"], NOSCORE),
            XC(p, "local:2604.12231-1", "sol", "unmet",
               "A4 collision: sol's local-1 (statistics) and son55's local-1 (label leakage) are different "
               "questions. Final local-1 = sol's, verified unmet; son55's moved to local-3 (unknown).",
               ["sol:E18", "sol:E20"]),
            XC(p, "local:2604.12231-2", "sol", "partial",
               "A4 collision: sol's local-2 (cost) and son55's local-2 (Gov Report F1) are different questions. "
               "Final local-2 = sol's, verified partial; son55's moved to local-4 (unmet, verified: 0.232 < 0.244 / "
               "0.238 / 0.234).", ["sol:E14", "sol:E15", "son55:E011", "son55:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "The isolation exists, but construction adds abstract-conditioned query exposure (opus:O01).",
               ["sol:E11", "sol:E12", "sol:E13", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "No overlap/contamination analysis. App. Q is a split, not an audit.", ["son55:E017", "opus:O03"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "met",
               "Long-context, retriever, compression and tree baselines are all present.",
               ["son55:E012", "son55:E013", "son55:E033"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: confidence+merge ablated jointly; hierarchy, ε and K not separated.", ["son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: five small English datasets, three backbones.", ["son55:E009", "son55:E031"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: low-quality-thought robustness test and human agreement; no threshold/K/size sweep.",
               ["son55:E026", "son55:E027"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "sol", "met",
               "Verified: replaces static raw chunks and pre-built summaries with query-conditioned stored "
               "abstractions.", ["sol:E01", "sol:E02"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "sol", "unmet",
               "Verified: thoughts summarise Q+A; no success/failure contrast.", ["sol:E09"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "sol", "partial",
               "A self-judge gate with a human agreement check; no outcome grounding.",
               ["sol:E09", "sol:E10", "son55:E004", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "A write-time novelty filter is not maintenance of existing entries.", ["son55:E006", "sol:E09"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "met",
               "Verified: explicit confidence + novelty acceptance rule decides what is kept.", ["sol:E01", "sol:E09"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unknown",
               "Verified: App. Q is disjoint, but the Table 2 memory-building stream is unstated.",
               ["son55:E018", "son55:E021"]),
            XC(p, "rsi:index_experience_for_reuse/F4", "son55", "unmet",
               "Verified: thoughts are admitted on the model's own confidence (failure mode present).",
               ["son55:E004", "son55:E026"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "unmet",
               "Verified: no external write gate (self-confidence + embedding similarity only).",
               ["son55:E004", "son55:E005"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "Verified: raw-only control and cold-start test at small n without variance.",
               ["son55:E010", "son55:E022", "son55:E023"]),
            XC(p, "rsi:index_experience_for_reuse/S6", "son55", "partial",
               "Verified: append-only with similarity scan; no update-rate or consolidation design.",
               ["son55:E006", "son55:E031"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: the self-confidence-only retention decision and the untested premise keep it at 2.",
                ["son55:E004", "son55:E005", "opus:O05"], "−5 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: abstract-conditioned construction queries, unstated main-table protocol, no "
                "audit, oracle-beating. App. Q keeps it above 0.",
                ["son55:E017", "son55:E021", "opus:O01", "opus:O03", "opus:O05"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text first. Initial view: in scope, retained "
                "only via App. Q. Construction queries are built from the abstract (the Abstract-task label), and the "
                "method beats a GT oracle, so leakage is plausible and unaudited. G 2, M 2, X 2, Em 2, Ec 2, Eh 1, "
                "Es 1, E.cost 2.",
            "integrity_checks": "Both seats a1 on 2604.12231v1, material sha ef8f755e…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: adding self-gated thoughts to a Contriever pool raises "
                                "F1 over the same-retriever raw control on most of five small sets, and a prefilled "
                                "memory from a disjoint half gives small gains on about 15 held-out cases. 'Consistently "
                                "outperforms all baselines' fails on Gov Report F1; label exposure is unresolved. "
                                "claim_support scoped.",
            "rating_agreement": "G, X, Em, Ec, Es, E.cost agree and were re-checked; M, Eh → son55. Final 46.25.",
        },
    }

    # =========================================================== 2604.13533 EEAgent (Δ1.25)
    p = "2604.13533"
    SCOPE_13533 = ["Complete 2604.13533v2 text re-read by Opus: §§I–VI, Algorithm 1, Tables I–II, all figure "
                   "captions; the paper has no appendix"]
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "The number of max_trails and maximum long memories are set to 3 and 20 respectively.",
                    "§IV-A",
                    "Failed tasks are retried up to 3 times. Whether reported success counts post-retry outcomes, and "
                    "whether baselines get the same attempts, is never stated."),
            opus_ev(p, "O02", "In this study, we assume that feedback is either a success or failed, and they each have "
                              "different strategies.", "§III-D1",
                    "The reflection branch, and the retry loop on failure, use the simulator's ground-truth success "
                    "signal during the evaluated task stream."),
            opus_ev(p, "O03", "Overall performance comparison of VIMA-Bench in selected task generalizations.",
                    "Table I caption",
                    "Which of the L1–L4 generalisation tiers is reported, and the number of episodes, are not given."),
            opus_ev(p, "O04", "our approach performs very close to VIMA-20M on tasks 1, 2, 3, and 4", "§IV-C",
                    "Table I: EEAgent 94.3/94.2/99.3/87.2 vs VIMA-20M 99.3/100.0/100.0/99.5 on Tasks 1–4. The text "
                    "overstates closeness (12.3 points on Task 4); 'state-of-the-art' holds only on the six-task "
                    "average.", kind="our_inference"),
            opus_ev(p, "O05", "EEAgent (Ours) 94.3 94.2 99.3 87.2 84.8 93.2 92.2", "Table I", "EEAgent row."),
            opus_ev(p, "O06", "VIMA-20M 99.3 100.0 100.0 99.5 58.7 41.5 83.2", "Table I", "VIMA-20M row."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: frozen VLM/LLM adapted by conditioning on accumulated prompt memories; sub null. "
                      "son55's supporting self_supervised_signal_engineering is rejected. The supervisory signal that "
                      "decides the reflection path is the simulator's ground-truth success/failure (opus:O02). The "
                      "LLM consistency checks only localise errors and nothing is trained on them (r13a convention).",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": dp_extra("sol", p, "unassigned"),
                           "revision_proposals": dp_extra("sol", p, "revision_proposals")},
        "pattern_mapping": pm("sol", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.13533-1"): "local:2604.13533-4",
                    ("son55", "local:2604.13533-2"): "local:2604.13533-5"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "partial",
                    "reason": "Opus (sol): Vanilla EA (same agent, no LSTRO) is the right isolating control, but retry "
                              "and feedback parity are unstated (opus:O01) and LM/SM are not separated."},
                "rsi:abstract_experience_into_guidance/S2": {
                    "status": "unmet",
                    "reason": "Opus (son55): successes and failures are summarised in separate branches. The card "
                              "condition is pairing or contrast, which is absent (sol's own reason says so)."},
                "rsi:abstract_experience_into_guidance/S3": {
                    "status": "met",
                    "reason": "Opus (son55): the simulator's success/failure signal decides which reflection path "
                              "writes a lesson (opus:O02). The self-judged localiser is an addition, not the "
                              "grounding.",
                    "evidence_ids": ["son55:E006", "son55:E009", "son55:E010", "sol:E04", "sol:E05", "opus:O02"]},
                "local:2604.13533-4": {**renum("local:2604.13533-1"),
                                       "evidence_ids": xev("son55", p, "local:2604.13533-1") + ["opus:O01", "opus:O03"]},
                "local:2604.13533-5": {**renum("local:2604.13533-2"),
                                       "evidence_ids": xev("son55", p, "local:2604.13533-2") + ["opus:O01"]},
            }),
        "claims": lambda c: c,
        "assessment": assess("sol", p, [
            "Opus: 'very close to VIMA-20M on tasks 1–4' overstated (Task 4: 87.2 vs 99.5) (opus:O04).",
            "Opus: retries use the ground-truth success signal; scoring of post-retry success unstated (opus:O01, "
            "opus:O02)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. A real stated residual (reflection generalisability, "
                   "short-to-long consolidation, ad-hoc localisation) with Reflexion/CLIN named, but not measured, "
                   "and the 'no training' premise is background.",
                   ["sol:E01", "sol:E17", "son55:E002", "son55:E003"]),
            "M": R("resolved", 2, "Opus sides with son55. The LM/SM split, consistency-based localisation, LLM "
                   "generality check and consolidation respond to the residual. But the load-bearing assumptions "
                   "(LLM consistency checks localise errors correctly; LLM-judged 'generality' selects transferable "
                   "lessons) are untested, success and failure are not contrasted, and Algorithm 1 is internally "
                   "inconsistent (an 'or' retry guard; F_ei used for planning). Not 3.",
                   ["son55:E008", "son55:E009", "son55:E010", "son55:E011", "sol:E05", "sol:E07"], ["son55:E026"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1 and key parameters (3 trials, 20 memories) "
                   "are given. Prompts, task stream, eviction rule, injection form and rollback are missing, and the "
                   "printed loop condition is defective.",
                   ["sol:E06", "sol:E07", "sol:E08", "son55:E012", "son55:E013"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Simulator success is an objective verifier. "
                               "Episode counts, tier and success counting are not described (opus:O03), and several "
                               "baselines are re-implemented or quoted.",
                               ["son55:E016", "son55:E024", "sol:E10", "opus:O03"]),
            "E.causality": R("resolved", 2, "Opus sides with son55. Vanilla EA vs EEAgent on the same agent, plus "
                             "CoT and three self-consistency variants on the same backbone, are applicable controls. "
                             "LM/SM, localiser and consolidation are not ablated, no Reflexion or plain-retry control "
                             "is run, and attempt/compute parity is unstated (A2: budget → E.causality and E.cost). "
                             "That is the 2 anchor (key controls present, gaps remain), as for the comparable "
                             "controls in ArtiCAD (this batch) and EvolveRouter (r14b). The ground-truth retry "
                             "signal is charged under E.holdout.",
                             ["son55:E017", "son55:E018", "son55:E019", "son55:E025", "sol:E12", "sol:E13"]),
            "E.holdout": R("not_reported", 0, "Opus sides with sol. The memory is updated online from the evaluated "
                           "VIMA-Bench task stream with the simulator's success signal (opus:O02). Failed tasks are "
                           "retried up to 3 times on that signal, with no statement of whether post-retry success is "
                           "scored (opus:O01). No construction/evaluation split, frozen-memory test or reported "
                           "generalisation tier exists (opus:O03). son55's 1 rests on a mention of the L1–L4 "
                           "protocol, which is not evidence of separation.",
                           ["sol:E04", "sol:E06", "sol:E10", "son55:E015", "opus:O01", "opus:O02", "opus:O03"],
                           scope=SCOPE_13533),
            "E.statistics": R("not_reported", 0, "Both seats not_reported 0; re-checked. No episode counts, seeds, "
                              "intervals or tests; 1–3-point differences unqualified.",
                              ["sol:E10", "son55:E019"], scope=SCOPE_13533),
            "E.cost": R("not_reported", 0, "Both seats not_reported 0; re-checked. No calls, tokens, latency, trial "
                        "usage or money for LSTRO or baselines; 3/20 are configuration values.",
                        ["sol:E10", "son55:E013"], scope=SCOPE_13533),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read (short paper, no appendix). In scope (system_method): long-term "
                  "prompt memories are rewritten from task feedback and persist across tasks. Missing protocol facts "
                  "are recorded as not_reported. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–5 image-only (Fig. 4 bars not read); Tables I–II used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "Self-signal card rejected: ground-truth simulator success gates the reflection paths (opus:O02); "
                "nothing is trained on the self-derived localisation signal.", ["sol:E04", "opus:O02"], NOSCORE),
            XC(p, "local:2604.13533-1", "sol", "unmet",
               "A4 collision: sol's local-1 (Algorithm 1 'or' guard / missing feedback refresh) vs son55's local-1 "
               "(task stream and post-retry scoring). Final local-1 = sol's, verified unmet; son55's moved to "
               "local-4 (unknown).", ["sol:E07", "sol:E08"]),
            XC(p, "local:2604.13533-2", "sol", "unmet",
               "A4 collision: sol's local-2 (statistics) vs son55's local-2 (baseline attempt parity). Final "
               "local-2 = sol's, verified unmet; son55's moved to local-5 (unknown).", ["sol:E10", "sol:E13"]),
            XC(p, "local:2604.13533-3", "sol", "unmet",
               "Verified: no measured calls, tokens, time or money.", ["sol:E10"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "The isolating control exists but retry/feedback parity is unstated (opus:O01).",
               ["sol:E12", "sol:E13", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: CoT/SC and a modified CLIN compared; no Reflexion, retrieval-memory or plain-retry "
               "baseline.", ["son55:E004", "son55:E005", "son55:E019", "son55:E024"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "unmet",
               "Verified: Table II ablates backbones and SAM size only.", ["son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: six tasks in one simulator, four backbones.", ["son55:E025", "son55:E027"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "unmet",
               "Verified: no sensitivity to memory quality, size or noise.", ["son55:E025", "son55:E026"]),
            XC(p, "rsi:abstract_experience_into_guidance/F1", "son55", "partial",
               "Verified: the 'without fine-tuning' premise is prominent, but LM/SM consolidation and error "
               "localisation are also named.", ["son55:E002", "son55:E003", "son55:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01", "sol", "partial",
               "Verified: merge/contradiction resolution and a 20-item cap; no edit vocabulary or eviction policy.",
               ["sol:E09", "sol:E15"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "sol", "met",
               "Verified: names specific static elements (inaccurate/task-specific reflections, no consolidation).",
               ["sol:E01", "sol:E17"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "unmet",
               "No pairing or contrast of successes and failures.", ["son55:E007", "son55:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "The ground-truth success signal decides the reflection path (opus:O02).", ["son55:E006", "opus:O02"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: untested LLM-judgement assumptions, no contrast, inconsistent algorithm.",
                ["son55:E009", "son55:E010", "son55:E011", "sol:E07"], "−5 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 2,
                "See ratings.E.causality: applicable same-agent controls exist; ablations and budget parity are "
                "missing (2 anchor, run precedent).", ["son55:E017", "son55:E018", "son55:E019"],
                "+3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"),
                "sol", {"status": "not_reported", "rating": 0},
                "See ratings.E.holdout: online memory on the evaluated stream, truth-signal retries with unstated "
                "scoring, no split or tier.", ["opus:O01", "opus:O02", "opus:O03"], "−2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text first. Initial view: in scope, evidence "
                "level task (no protocol, no split, truth-signal retries). G 2, M 2, X 2, Em 2, Ec 1–2, Eh 0, Es 0, "
                "E.cost 0.",
            "integrity_checks": "Both seats a1 on 2604.13533v2, material sha 2f4038e0…; canonical seat hashes equal "
                                "conflicts.json; both claim_type system_method; RS/domain ids valid.",
            "core_claim_check": "Strongest supported claim: in the authors' unstated protocol, adding LSTRO to a "
                                "GPT-4o manipulation agent raises average VIMA-Bench success 85.1 → 92.2 and beats "
                                "CoT/SC prompting by 2.9–4.0 points. Retained cross-task benefit, retry parity and "
                                "variance are unestablished; VIMA-20M wins Tasks 1–4. claim_support scoped.",
            "rating_agreement": "G, X, Em, Es, E.cost agree and were re-checked; M, Ec → son55; Eh → sol. Final 40.0.",
        },
    }
    return S
