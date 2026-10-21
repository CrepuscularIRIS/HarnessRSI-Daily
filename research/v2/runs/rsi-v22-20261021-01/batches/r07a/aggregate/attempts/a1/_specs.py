"""Opus rulings for r07a a1 (data only; consumed by _build.py)."""
import copy


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev,
                   "none (expectations are not scored directly)")

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

    def oos_ratings(reason):
        return {k: R("unknown", None, reason) for k in KEYS}

    def oos_assessment(note):
        return {"evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run precedent r05b/r06a).",
                "claim_support": None, "claim_support_note": note, "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]}

    def oos_level_res(p, ev):
        return [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "null is canonical for out-of-scope rows (r05b/r06a precedent); the harness task/retained/improver ladder "
                "does not apply to weight-level work. sol's 'task' was descriptive only (its own scope_note).", ev,
                "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
                "null is canonical for out-of-scope rows; claim support is not assessed under this rubric.", ev, "none"),
        ]

    # =========================================================== 2508.21589 Middo (both out_of_scope; boundary)
    p = "2508.21589"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Boundary checked independently: "
          "Middo's retained, iteratively rewritten artifact is the SFT dataset, but that dataset is never read at inference — "
          "each iteration it is consumed only by re-fine-tuning the base model for one epoch (opus:O01, opus:O02), and every "
          "reported result (Tables 1–3, 5–7) is a fine-tuned LLaMA-3.1-8B/Mistral-7B checkpoint (opus:O03). The loss/"
          "embedding/self-alignment diagnostics are a training-data curriculum, not a prompt/skill/tool/workflow/memory/"
          "evaluator/config retained and reused by a frozen system; same ruling as r06a SyncLoop (evolved training data + "
          "retraining). Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "In each iteration, after the three data selection and optimization processes described above, "
                    "the optimized dataset is then fed back for the next round of model training.", "§3.4 (end)",
                    "The only consumer of the refined dataset is the next round of weight training."),
            opus_ev(p, "O02", "the base model is fine-tuned for one epoch on the dataset optimized in that specific iteration",
                    "§4.1 Training and Evaluation Settings", "Each iteration's product is a fine-tuned checkpoint."),
            opus_ev(p, "O03", "Models trained with Middo optimized data achieve consistent performance gains over baselines",
                    "§1", "The evaluated object is the trained model, not a reusable non-weight harness component."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): model-signal gates (loss thresholds, kNN sparsity, self-alignment scores) "
                      "select samples, an LLM rewrites/extends them, and the model is retrained on the refined set each "
                      "iteration — C08's generate→gate→retrain loop with 'per-instance loss threshold' and 'model "
                      "self-scoring' gates and the training distribution as the manufactured object.",
            "matches": [{"main_id": "self_supervised_signal_engineering", "sub_id": "C08", "role": "primary",
                         "fit": "medium (informational, out_of_scope)",
                         "tactic_steps_checked": "C08: data defect named (static curation ignores model state) → LLM rewrite/"
                                                 "neighbour-conditioned extension → threshold gates on model signals → retrain "
                                                 "→ iterate with the improved model re-diagnosing.",
                         "success_checks": "Iterated loop run on Alpaca/WizardLM with two base models (author-reported).",
                         "failure_checks": "Iteration count and thresholds are tuned on the reported benchmarks (App. 8.2–8.3); "
                                           "not used as Harness-RSI evidence.",
                         "evidence_ids": ["opus:O01", "opus:O02", "sol:E004", "sol:E005", "sol:E006"],
                         "reason": "heterogeneous_decomposition (sol) describes the three detectors but its load-bearing "
                                   "artifact is an error/fidelity decomposition for differentiated compression (sol itself "
                                   "rejected C04); the executed loop is C08, consistent with r06a SyncLoop."}],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi", "matches": [], "unassigned": True, "revision_proposals": [],
                           "reason": "Kept from sol: self_generate_the_curriculum/H23 was checked; the diagnose→regenerate "
                                     "move resembles H23 but the only product is SFT weights (A3), so no domain card is "
                                     "assigned for an excluded row."},
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; Table 1–3 gains are author-reported SFT results."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; son55's boundary flag independently re-checked and confirmed)",
        "resolutions": oos_level_res(p, ["opus:O02", "opus:O03"]) + [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "revised", "self_supervised_signal_engineering",
                "Informational. See rs_pattern.matches reason: generate→gate→retrain is C08; heterogeneous_decomposition's "
                "decisive artifact (an error decomposition for differentiated compression) is absent. son55 skipped "
                "identification for an out_of_scope row, which the contract allows.",
                ["opus:O01", "sol:E004", "sol:E006"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", "C08"]], "See rs_pattern.primary.", ["opus:O01", "opus:O02"], NOSCORE),
            X(p, "local:2508.21589-1", *C(p, "expectations[local:2508.21589-1].status"), "sol", "unmet",
              "Verified (informational): the retained data feeds weight updates only; no non-weight harness effect is "
              "evaluated.", ["opus:O01", "opus:O03"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §1–5, Limitations and App. 7–9 before opening seats: "
                                                   "dataset rewritten each iteration, base model re-fine-tuned on it, all "
                                                   "results are checkpoints → out_of_scope (A3), boundary because the "
                                                   "retained object is data rather than weights.",
            "integrity_checks": "Both seats a1 on 2508.21589v5, material sha e28e2cf4…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03; son55's 'boundary, moderate confidence' resolved to "
                                "confirmed: training data is not in the scope's non-weight component list and is never read "
                                "by a deployed system.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2509.04439 ArcMemo (Δ2.5)
    p = "2509.04439"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Verify returns true if the program successfully passes the test case.", "Appendix B scoring",
                    "Scoring executes the generated program against the puzzle's test cases (exact-grid verifier)."),
            opus_ev(p, "O02", "some signal is needed to discriminate correct from incorrect traces to ensure only productive "
                    "ideas and patterns are added to memory.", "§3.1 Problem Assumptions",
                    "Only correct traces are written; there is no success/failure contrast (H00 step 2 / S2)."),
            opus_ev(p, "O03", "+ continual memory update 46.33 (1.53) 56.00 (0.00) 61.00", "Table 3, retry 0",
                    "With continual updates OE is lower or equal at retry 0 (and at retry 1, 65.00 vs 65.67 official); "
                    "only retry 2 is higher, and only OE was tested."),
            opus_ev(p, "O04", "ArcMemo-OE (ours) 59.00 55.00 56.00 56.67 (2.08) 65.67 (1.53) 70.00", "Table 4, retry 1",
                    "OE is below the no-memory baseline (57.83 / 66.67 / 71.50) at retry 1 and retry 2: abstraction per se "
                    "is not what beats baseline; only PS does."),
            opus_ev(p, "O05", "we conducted small-scale experiments using tiny (n=10) subsets of the validation split",
                    "Appendix C Concept Specificity", "Design pilots used validation-split puzzles; overlap with the "
                    "100-puzzle evaluation subset is not stated."),
            opus_ev(p, "O06", "- selection 46.83 (5.25) 55.17 (2.02) 60.00", "Table 2, retry 0",
                    "Without selection PS equals the no-memory baseline (55.17) at the official setting."),
            opus_ev(p, "O07", "moving from additive concept updates toward consolidation operations that restructure the "
                    "memory across multiple experiences", "Appendix D.2", "Consolidation/forgetting is future work."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats adapt_via_conditioning/C03 (skip-upstream reference-substrate branch: canonical PS/OE concept "
                      "schema + retrievable bank conditioning a frozen o4-mini). Re-checked against the run convention: "
                      "category holdout absent but train/val split separation and a same-budget simpler conditioning "
                      "control (frozen all-in-context cheatsheet, -selection) are partially present, so C03 is kept with "
                      "son55's 'partial' fit (sol 'high' overstates: no category holdout, no contamination audit).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "unresolved",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                        dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("son55", p)["pattern_mapping"]), "son55") + [{
            "rs_main": "adapt_via_conditioning", "rs_sub": "C03",
            "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H01"},
            "operation_correspondence": "Same read path (retrieve-and-condition); H01 adds the PS write-time revision of "
                                        "existing concept descriptions, parameters and relevance cues.",
            "conditions_and_differences": "H01 expects an explicit edit vocabulary with consolidation/forgetting and a curator "
                                          "ablation; ArcMemo has add+revise only, consolidation deferred (opus:O07).",
            "evidence_ids": ["son55:E009", "son55:E008", "opus:O07"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2509.04439-1"): "rsi:abstract_experience_into_guidance/H00-step4",
                    ("sol", "local:2509.04439-2"): "rsi:abstract_experience_into_guidance/H00-step5",
                    ("sol", "local:2509.04439-3"): "local:2509.04439-1",
                    ("sol", "local:2509.04439-4"): "local:2509.04439-3"},
            overrides={
                "rsi:abstract_experience_into_guidance/H00-step4": {
                    "status": "partial", "applies_when": "a store is updated while results are reported",
                    "reason": "Opus final (sol local-1 merged, A4): fixed-memory runs seed from 160 train-split solutions and "
                              "test on validation puzzles (clean stream separation); the continual-update claim updates on "
                              "the same evaluation stream across retry passes, order matters, and design pilots used "
                              "validation-split puzzles (opus:O05)."},
                "rsi:abstract_experience_into_guidance/H00-step5": {
                    "status": "partial", "applies_when": "gain is attributed to the store",
                    "reason": "Opus final (sol local-2 merged, A4): same-model store-off baseline with identical retries/"
                              "parallel samples and a -selection ablation exist; memory runs emit more output tokens and no "
                              "matched-token or random-concept control is given."},
                "local:2509.04439-1": {
                    "status": "partial",
                    "reason": "Opus final (sol local-3 merged, A4): three runs with SD and full per-run tables, but no CI or "
                              "significance test, one evaluation order, headline gains ≈ one baseline SD."},
                "local:2509.04439-3": {
                    "status": "partial",
                    "reason": "Opus final (sol local-4 merged, A4): token plot counts solver reasoning tokens only; GPT-4.1 "
                              "abstraction, VLM captioning and selection calls are not charged."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O03"]), "C4", ["opus:O04"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained', re-checked: the fixed concept store (abstracted from train-split seed "
                                   "solutions) is read on separate validation puzzles and PS beats the same-budget store-off "
                                   "baseline in all 9 Table 4 cells. The gain is small (≈1 SD) and the self-generated "
                                   "continual-update claim is only retry-2/OE (opus:O03) — retained, not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "not_supported": seat("son55", p)["assessment"]["not_supported"],
            "unresolved": seat("son55", p)["assessment"]["unresolved"] + [
                "Overlap between the n=10 validation design pilots and the 100-puzzle evaluation subset (opus:O05)."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Specific changed object (entry abstraction level + read-time "
                   "selection) against named neighbours (Buffer of Thoughts, Dynamic Cheatsheet, MemP); not 4 because no "
                   "experiment shows instance-level memory failing on ARC, the authors' own pilot favours specificity, "
                   "and neighbour full texts are not pinned.",
                   ["son55:E001", "son55:E002", "son55:E034", "son55:E035", "sol:E001", "sol:E017"], ["son55:E028"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. OE situation/suggestion vs PS typed parameterized concepts, "
                   "pseudocode before abstraction, and reasoning-based selection (motivated by failed embedding retrieval) "
                   "are reconstructable with a tested prediction (selection matters); the abstraction-beats-instance "
                   "hypothesis has no direct control and the write gate is an assumption.",
                   ["son55:E009", "son55:E010", "son55:E027", "son55:E005", "sol:E002", "sol:E003", "sol:E004"],
                   ["son55:E028"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Write/read steps are described, but the store is flat and "
                   "additive, OE writes ignore existing contents, admission is 'assumed-correct trace' with no marginal test "
                   "(opus:O02), consolidation/forgetting/rollback are deferred (opus:O07), and the certifying signal for "
                   "continual writes is unstated.",
                   ["son55:E007", "son55:E008", "son55:E009", "son55:E006", "son55:E023", "sol:E013", "sol:E018",
                    "opus:O02", "opus:O07"]),
            "E.measurement": R("resolved", 4, "Opus sides with sol. The verifier is exact execution of the generated program "
                               "on each puzzle's test cases (opus:O01) under the official oracle@2 metric, and a strict "
                               "single-program-solves-all regime (Table 5) reproduces the ordering; for this central claim "
                               "the metric and verifier cannot be satisfied by non-target factors. son55's docking reason "
                               "(public-ARC exposure) is, by its own note, scored under E.holdout; A2 keeps it there.",
                               ["sol:E007", "sol:E019", "son55:E033", "son55:E014", "opus:O01"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Store-off baseline at equal retries/parallel samples, "
                             "-selection ablation, frozen cheatsheet and OE comparisons exist. Missing: an instance-level "
                             "memory under the same pipeline, a matched-token control, and the abstraction claim is "
                             "contradicted for OE (below baseline in 6/9 cells, opus:O04); without selection PS equals "
                             "baseline at the official setting (opus:O06); continual vs fixed is mixed (opus:O03).",
                             ["son55:E014", "son55:E018", "son55:E032", "son55:E030", "son55:E031", "sol:E011", "sol:E015",
                              "opus:O04", "opus:O06"],
                             ["son55:E025", "son55:E022", "son55:E028", "opus:O03"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Fixed memory from train-split seeds tested on "
                           "validation puzzles is clean; but no public-ARC exposure audit, design pilots on validation-split "
                           "puzzles (opus:O05), the lifelong claim is tested on the same stream whose order matters, and "
                           "scope is one benchmark × 100 puzzles.",
                           ["son55:E011", "son55:E013", "son55:E024", "sol:E005", "sol:E006", "sol:E010", "sol:E014",
                            "opus:O05"], ["son55:E023", "son55:E036"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked (A2 ladder: cross-run SD but no CI/significance → 2). "
                              "Three runs with SD and per-run tables; headline gains ≈ one baseline SD; several SD=0.00 "
                              "values unexplained; authors flag large sampling variance.",
                              ["son55:E016", "son55:E017", "son55:E029", "sol:E008", "sol:E009"], ["son55:E022"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Token-efficiency plot counts solver reasoning tokens only; "
                        "abstraction (GPT-4.1), captioning and selection calls are not charged, and memory runs increase "
                        "output tokens.", ["son55:E025", "son55:E026", "sol:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–E read; in scope (system_method): a non-weight concept memory "
                  "written from verified solutions and read on later puzzles. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "PS abstraction is explicitly aware of existing concepts and revises descriptions, parameter lists and "
                "relevance cues (son55:E009) — an H01 update operation including retrieval-hook revision; fit is partial "
                "because there is no merge/delete/forget and consolidation is future work (opus:O07). H00 remains the "
                "primary (extraction at a chosen abstraction level). sol covered the same fact via S4 only.",
                ["son55:E009", "son55:E008", "opus:O07"], NOSCORE),
            X(p, "local:2509.04439-2", *C(p, "expectations[local:2509.04439-2].status"), "son55", "unmet",
              "A4 hidden-ID collision: sol's local-2 (attribution to abstraction/selection vs extra reasoning) and son55's "
              "local-2 (abstraction level vs any stored text) are different questions. Final local-2 = son55's question: "
              "unmet — no instance-level memory baseline and OE (abstract) is below no-memory in 6/9 cells (opus:O04). "
              "sol's question is merged into H00-step5 (partial).", ["son55:E032", "son55:E015", "opus:O04"]),
            X(p, "local:2509.04439-4", *C(p, "expectations[local:2509.04439-4].status"), "same_supported_fact",
              "partial (merged into local:2509.04439-3)",
              "sol's local-4 (token-efficiency claim, partial) is the same check as son55's local-3 (cost of construction "
              "and selection, partial): both cite the solver-only token plot. Merged; status partial.",
              ["sol:E012", "son55:E025", "son55:E026"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55",
              "unmet", "Verified: no analysis of o4-mini exposure to public ARC or of seed/eval overlap. Applies because the "
                       "central claim is generalization to held-out puzzles with a pretrained backbone.",
              ["son55:E011", "son55:E013"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "partial", "Verified: frozen all-in-context cheatsheet and -selection ablation exist; no instance-level or "
                         "longer-context baseline under the same pipeline.", ["son55:E032", "son55:E018", "opus:O06"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55",
              "unmet", "Verified: ARC-AGI-1 only (100 puzzles); ARC-AGI-2 not run; the paper presents concept memory as "
                       "broadly reusable.", ["son55:E013", "son55:E036"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55",
              "partial", "Verified: an n=10 specificity pilot and qualitative coverage analysis; no seed-bank size/quality "
                         "sweep.", ["son55:E028", "son55:E031"]),
            X(p, "rsi:abstract_experience_into_guidance/F4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/F4].status"), "son55", "partial",
              "Verified: selection is argued as a co-contribution and ablated; without it PS equals baseline at the "
              "official setting (opus:O06), so part of the gain is a retrieval fix argued as such.",
              ["son55:E018", "son55:E019", "opus:O06"]),
            X(p, "rsi:abstract_experience_into_guidance/H00-step4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H00-step4].status"), "son55", "partial",
              "Verified; sol asked the same question under local-1 (also partial) and is merged here (A4).",
              ["son55:E011", "son55:E024", "son55:E023", "sol:E010", "opus:O05"]),
            X(p, "rsi:abstract_experience_into_guidance/H00-step5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H00-step5].status"), "son55", "partial",
              "Verified; sol asked the same question under local-2 (partial) and is merged here (A4).",
              ["son55:E014", "son55:E025", "sol:E015"]),
            X(p, "rsi:abstract_experience_into_guidance/S2",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"), "son55", "unmet",
              "Verified: only verified-correct traces are abstracted; incorrect traces are explicitly not used, so no "
              "success/failure contrast (opus:O02). Applies because lessons are extracted from outcomes.",
              ["son55:E006", "opus:O02"]),
            X(p, "rsi:abstract_experience_into_guidance/S5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S5].status"), "son55", "partial",
              "Verified: correctness gates what is written, but there is no per-entry marginal-effect test or retirement.",
              ["son55:E006", "son55:E005", "opus:O02"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", {"status": "resolved", "rating": 4},
                "See ratings.E.measurement: exact program execution on test cases + official and strict scoring; son55's "
                "only docking reason is contamination, which A2 assigns to E.holdout (already 2).",
                ["sol:E007", "sol:E019", "opus:O01"], "+2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2509.04439-1]",
             "sol_value": "partial — continual self-improvement / stream separation (E.holdout)",
             "son55_value": "partial — stream statistics (E.statistics)",
             "final_value": "local-1 = statistics (sol local-3 + son55 local-1); sol's local-1 merged into H00-step4",
             "correction": "A4 hidden collision: same ID, different questions, equal status, so the mechanical diff did not "
                           "flag it.", "evidence_ids": ["son55:E029", "sol:E010"], "score_impact": "none"},
            {"field_path": "expectations[local:2509.04439-3]",
             "sol_value": "partial — statistics (E.statistics)", "son55_value": "partial — construction/selection cost (E.cost)",
             "final_value": "local-3 = cost (sol local-4 + son55 local-3); sol's local-3 merged into local-1",
             "correction": "A4 hidden collision (same ID, different questions, equal status).",
             "evidence_ids": ["sol:E009", "son55:E026"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before seat scores: in scope, fixed concept memory seeded from train-split "
                                                   "human solutions, read on 100 val puzzles; PS > no-memory everywhere but "
                                                   "≈1 SD; OE below baseline at higher retries; continual update mixed; "
                                                   "initial bands G3 M3 X2 Em3–4 Ec2 Eh2 Es2 Ecost2; evidence_level retained.",
            "integrity_checks": "Both seats a1 on 2509.04439v3, material sha 2ee2aaf7…; canonical seat hashes equal "
                                "conflicts.json; both C03 + H00 identified; namespaces valid.",
            "core_claim_check": "Re-read §3–5, Tables 1–5 and App. B–D; recomputed OE-vs-baseline cells (6/9 below) and "
                                "the -selection = baseline official cell.",
            "rating_agreement": "7/8 identical and re-checked; E.measurement → sol (4).",
            "expectation_renumbering": "sol local-1→H00-step4, local-2→H00-step5, local-3→local-1, local-4→local-3.",
            "retained_vs_retained_gain": "Retained store with a small store-off gain on separate puzzles; the self-generated "
                                         "continual gain is not established (opus:O03).",
            "card_leakage_A5": "son55 flagged that H00's rejected-work lesson ('Composing modular abstract concepts … needs a "
                               "feedback gate … and an evaluation larger than a small public set') effectively identifies "
                               "this paper. Confirmed; not used as evidence or anchor; kept as son55 revision proposal.",
        },
    }

    # =========================================================== 2509.09498 SEDM (Δ6.25)
    p = "2509.09498"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "here the memory comes from a single conversation and is frozen, so merged and distilled items "
                    "become more general but may not fit a new conversation, and the controller cannot correct their "
                    "weights during testing.", "§4.6",
                    "By contrast with §4.6, the Table 2 scheduling gain is obtained with a controller that keeps correcting "
                    "item weights during testing, i.e., from outcomes on the evaluation stream."),
            opus_ev(p, "O02", "Tables 1 – 3 use the original SEDM configuration (§ 3.2 ), while § 4.6 uses the stricter "
                    "held-out configuration.", "§4.1", "All headline sender-side gains use the source-task admission "
                    "configuration."),
            opus_ev(p, "O03", "is the average realized utility of", "Appendix A, Original configuration",
                    "Original-configuration weights are updated from realized utility on processed tasks."),
            opus_ev(p, "O04", "Always injecting SEDM memory helps little here", "§4.6",
                    "Under held-out admission the SEDM-produced frozen memory gives no success gain when always used."),
            opus_ev(p, "O05", "Each arm is run k k times", "§3.2 Paired A/B test",
                    "Admission replays each candidate k times per arm on e tasks (e=k=3 in §4.6); these calls are not "
                    "charged in the Table 2 token comparison."),
            opus_ev(p, "O06", "For FEVER and HotpotQA we also report prompt and completion tokens as a measure of cost.",
                    "§4.1", "Reported cost is agent prompt/completion tokens of the evaluated runs."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus revised. The executed agent-side operation is the main-card definition: a frozen gpt-4o-mini solves "
                      "new tasks conditioned on retrieved memories with no parameter update; SEDM's contribution decides "
                      "which entries the conditioning bank holds (paired admission, utility ranking, decay) and whether to "
                      "inject them (CMG). This matches the run convention for memory systems (r03–r06, sub null when C03's "
                      "schema/upstream/category-holdout steps are absent). assumption_audit_and_pivot (sol) is rejected: no "
                      "assumption is relaxed and a guarantee re-derived, and 'relevance ≠ utility' is a motivating empirical "
                      "observation, not a violated precondition with a tightness or exploit template. outside_taxonomy "
                      "(son55) is rejected because a card does describe the executed operation; the retention governance "
                      "lives in the domain layer (H29/H30/H05).",
            "matches": [{"main_id": "adapt_via_conditioning", "sub_id": None, "role": "primary", "fit": "partial",
                         "tactic_steps_checked": ["retrieved memories appended to the agent prompt (only difference between "
                                                  "arms)", "no per-task parameter update of the agent",
                                                  "C03 schema/upstream-reading/category-holdout steps not executed → sub null"],
                         "success_checks": ["conditioning toggled against no-memory on identical executions: met (Tables 4–5)"],
                         "failure_checks": ["gate itself is a LoRA-trained Qwen3-4B, outside this card",
                                            "retention governance not covered by any RS card"],
                         "evidence_ids": ["son55:E013", "son55:E012", "son55:E026", "sol:E022"],
                         "reason": "Operation-level match; governance and gate are domain-layer content."}],
            "executes_pattern": "partial", "resolves_problem": "unresolved",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "evidence_gated_retention", "H30"),
                        dmatch("son55", p, "evidence_gated_retention", "H29"),
                        dmatch("son55", p, "index_experience_for_reuse", "H05")],
            "unassigned": [],
            "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"],
        },
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "evidence_gated_retention", "sub": "H30"},
             "operation_correspondence": "RS: frozen agent conditioned on retrieved memories. H30: which entries the bank holds "
                                         "— paired-replay admission, quarantine/isolation, decay-based removal, provenance.",
             "conditions_and_differences": "H30 expects a hard size bound, regression budget and a governed-vs-ungoverned "
                                           "held-out comparison; SEDM has η=0 and decay only, and no held-out comparison.",
             "evidence_ids": ["son55:E005", "son55:E008", "son55:E009", "opus:O02"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "evidence_gated_retention", "sub": "H29"},
             "operation_correspondence": "Per-item weights from with/without-memory reward deltas reorder what conditions the "
                                         "agent.", "conditions_and_differences": "Value-stripped ablation only in the original "
                                                                                 "configuration (Table 2).",
             "evidence_ids": ["son55:E011", "son55:E021", "opus:O01"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "index_experience_for_reuse", "sub": "H05"},
             "operation_correspondence": "CMG decides whether the conditioning is injected at all.",
             "conditions_and_differences": "H05's trigger is usually uncertainty at reasoning steps; here a supervised, "
                                           "calibrated, cost-aware pre-injection gate.",
             "evidence_ids": ["son55:E012", "son55:E027", "son55:E029"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "rsi:index_experience_for_reuse/H05"): "rsi:index_experience_for_reuse/H05-step3",
                    ("sol", "local:2509.09498-1"): "local:2509.09498-2",
                    ("sol", "local:2509.09498-2"): "local:2509.09498-4"},
            overrides={
                "rsi:evidence_gated_retention/S4": {
                    "status": "met", "applies_when": "a gate or value signal is claimed", "score_item": "E.causality",
                    "reason": "Opus final (son55): value weighting and CMG are separable components by design and both are "
                              "stripped in ablations (Table 2 cumulative rows; always-use/skip/random vs CMG). The weakness "
                              "sol notes — the sender ablation uses the original configuration — is scored in E.causality/"
                              "E.holdout, not in this design-level condition."},
                "rsi:index_experience_for_reuse/H05-step3": {
                    "status": "met",
                    "reason": "Opus final (sol H05 + son55 H05-step3, same fact): gated use compared with always-inject and "
                              "never-inject on the same frozen store and the same cached executions, with gate latency and "
                              "tokens counted."},
                "local:2509.09498-2": {
                    "status": "unmet", "applies_when": "headline retained-memory gains are read as future-task gains",
                    "score_item": "E.holdout",
                    "reason": "Opus final (sol local-1 + son55 local-2, A4): the headline sender-side numbers (Tables 1–3) use "
                              "source-task admission and a controller that keeps correcting weights from evaluation-stream "
                              "outcomes (opus:O01–O03) and were not re-run held-out; under held-out admission the frozen "
                              "SEDM memory gives no gain when always used (opus:O04). The strict CMG splits (sol's point) are "
                              "clean but test the gate, not retained-memory gains.",
                    "evidence_ids": ["son55:E022", "son55:E023", "sol:E017", "opus:O01", "opus:O02", "opus:O04"]},
                "local:2509.09498-4": {
                    "reason": "Renumbered from sol local-2 (A4 collision). Success proxies (HotpotQA token F1≥0.5, LoCoMo "
                              "SBERT≥0.7) are lenient and unaudited; token F1 is reported alongside. Partial."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01", "opus:O05"]), "C5", ["opus:O04"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Opus sides with son55. The positive retained-memory numbers (Tables 1–3) come from source-task "
                                   "admission with a controller that updates weights from outcomes on the evaluation stream "
                                   "(opus:O01–O03), so the selection set is not separated from the test set (EVIDENCE rule 2 "
                                   "→ at most task). The one clean test of SEDM-produced memory (§4.6, held-out admission, "
                                   "frozen) shows no gain from always using it (opus:O04) and a within-noise gain with CMG; the "
                                   "clean HotpotQA retained store is gold-evidence memory not produced by the SEDM loop.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "not_supported": seat("son55", p)["assessment"]["not_supported"],
            "unresolved": seat("son55", p)["assessment"]["unresolved"] + [
                "Admission replay and controller cost relative to the reported token savings (opus:O05)."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Relevance/past utility vs marginal gain over no-memory and the "
                   "tie-discarding winner-label problem are specific and shown (73 rescued vs 32 broken); neighbours named "
                   "but not pinned, society framing nominal, LoCoMo baselines borrowed.",
                   ["son55:E001", "son55:E002", "son55:E046", "son55:E045", "son55:E026", "sol:E001"],
                   ["son55:E036", "son55:E017"]),
            "M": R("resolved", 3, "Opus sides with son55. CMG (two independent heads on all four paired outcomes, per-action "
                   "temperature, cost threshold) is fully reconstructable with a tested distinguishing prediction, which "
                   "would merit 4 alone; but the sender half of the central claim rests on an original admission test that "
                   "replays the candidate's own source task (self-confirming, conceded by the authors), ad hoc tier/decay "
                   "constants and an unjustified rule-based abstraction, so the method as claimed is 3.",
                   ["son55:E005", "son55:E012", "son55:E014", "son55:E029", "sol:E007", "sol:E008"], ["son55:E006"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. SCEC contents, gate input exclusions, hashed splits, leak filters, "
                   "weights/tiers/merge/isolation/decay with provenance are explicit; no rollback or hard size bound, "
                   "minimum weight unstated, η=0, gate and memory never co-adapt, code not released.",
                   ["son55:E005", "son55:E015", "son55:E007", "son55:E009", "son55:E010", "son55:E038", "sol:E002",
                    "sol:E004", "sol:E005"], ["son55:E008", "son55:E033"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Paired exact scoring on identical executions, "
                               "bootstrap CIs and a fixed invented-Observation bug; success proxies lenient and LoCoMo "
                               "baselines on different metrics/budgets.",
                               ["son55:E013", "son55:E044", "son55:E039", "sol:E025", "sol:E022"], ["son55:E017"]),
            "E.causality": R("resolved", 3, "Both seats 3; re-checked. CMG attribution is strong (always/skip, similarity, "
                             "winner head, SFT, CoT, random-gating line, oracle, uncalibrated, three seeds); sender side is "
                             "weak (cumulative ablation only in the original configuration with test-time weight correction "
                             "(opus:O02, opus:O01), diffusion not ablated, no ungoverned-store control held-out). Not lowered: "
                             "the gate half is near-4 and the sender weakness is mostly a holdout defect scored there (A2).",
                             ["son55:E026", "son55:E027", "son55:E028", "son55:E029", "son55:E021", "sol:E013"],
                             ["son55:E025", "son55:E030", "son55:E032", "opus:O01", "opus:O02"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. CMG studies use disjoint hashed splits and conversation-level "
                           "splits (strong), but the headline retained-memory gains use source-task admission plus "
                           "evaluation-stream weight correction (opus:O01–O03) and were not re-run held-out; the held-out "
                           "SEDM memory gives no gain (opus:O04); controlled memories are gold evidence; one agent model.",
                           ["son55:E038", "son55:E039", "son55:E040", "sol:E014", "sol:E021", "opus:O01", "opus:O03"],
                           ["son55:E022", "son55:E023", "son55:E034", "son55:E035", "opus:O04"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked (A2 ladder). Bootstrap CIs and three gate seeds on "
                              "HotpotQA but between-gate differences mostly within CIs; LoCoMo 193 questions of one "
                              "conversation without CI; Tables 1–3 single runs without n or variance.",
                              ["son55:E027", "son55:E041", "son55:E038", "sol:E023", "sol:E024", "sol:E015"],
                              ["son55:E037", "son55:E031"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Agent tokens, injection rates, gate latency, λ curves and the "
                        "paired-collection bill ($4.5) are reported, but the headline efficiency claim (16–32% fewer prompt "
                        "tokens than G-Memory) charges only evaluated-run tokens (opus:O06) while sender-side admission "
                        "replays k runs × 2 arms × e tasks per candidate (opus:O05) plus controller and LoRA gate training "
                        "are uncharged — a key coverage gap for a cost claim, so 2 not 3.",
                        ["son55:E042", "son55:E043", "son55:E027", "sol:E026", "opus:O05", "opus:O06"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 text incl. Appendices A–I read; in scope (system_method): a non-weight shared memory with "
                  "paired admission/governance and a use gate (the LoRA gate is a trained component, the retained object is "
                  "memory). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "See assessment.evidence_level_note: positive retained-memory results lack selection/test separation "
                "(evaluation-stream weight correction, opus:O01–O03); the clean held-out SEDM memory shows no gain "
                "(opus:O04). sol's 'frozen memory read on later different tasks' holds for the CMG studies, whose gains are "
                "token savings at equal success, not a retained-memory improvement.",
                ["opus:O01", "opus:O02", "opus:O04", "son55:E030"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "revised", "adapt_via_conditioning",
                "See rs_pattern.reason.", ["son55:E013", "son55:E026"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["adapt_via_conditioning", None]],
                "See rs_pattern.reason; sub null (no C03 schema/upstream/category holdout).", ["son55:E013"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["evidence_gated_retention", "H30"], ["evidence_gated_retention", "H29"],
                 ["index_experience_for_reuse", "H05"]],
                "H30 is load-bearing: candidates are quarantined until a paired replay passes, rejected items are never "
                "retrieved, conflicting items isolated, decayed items removed, with provenance — membership governance, "
                "not only re-weighting (H29). sol noted the H30 elements but declined to match for lack of a hard size "
                "bound, which is a condition check, not a reason to omit the sub-card.",
                ["son55:E007", "son55:E009", "son55:E010", "sol:E005"], NOSCORE),
            X(p, "local:2509.09498-1", *C(p, "expectations[local:2509.09498-1].status"), "son55", "unmet",
              "A4 hidden-ID collision: sol's local-1 (future-memory holdout) ≠ son55's local-1 (borrowed LoCoMo baselines). "
              "Final local-1 = son55's question: verified unmet — baselines are carried over from prior work with possibly "
              "different memory budgets. sol's question is merged into local-2.", ["son55:E017", "son55:E018"]),
            X(p, "local:2509.09498-2", *C(p, "expectations[local:2509.09498-2].status"), "son55", "unmet",
              "A4 collision: sol's local-2 (success-label measurement) is renumbered local-4 (partial); final local-2 = "
              "headline holdout (son55 local-2 + sol local-1): unmet — see expectation reason (opus:O01–O04).",
              ["son55:E022", "son55:E023", "opus:O01", "opus:O04"]),
            X(p, "rs:self_supervised_signal_engineering/RE-2",
              *C(p, "expectations[rs:self_supervised_signal_engineering/RE-2].status"), "son55", "met",
              "Verified and applicable to the CMG component, whose training signal is manufactured from the system's own "
              "paired executions: winner-label gates and a similarity threshold collapse to always-use while CMG does not, "
              "and calibration stabilises seeds. Kept although the RS primary is adapt_via_conditioning — the expectation "
              "checks the gate's training signal, not pattern membership.", ["son55:E029", "son55:E014", "son55:E027"]),
            X(p, "rs:self_supervised_signal_engineering/RE-6",
              *C(p, "expectations[rs:self_supervised_signal_engineering/RE-6].status"), "son55", "partial",
              "Verified: memory frozen during gate training/test, gold-evidence memories acknowledged as optimistic, every "
              "training task run twice.", ["son55:E033", "son55:E034", "son55:E013"]),
            X(p, "rsi:evidence_gated_retention/F3", *C(p, "expectations[rsi:evidence_gated_retention/F3].status"), "son55",
              "partial", "Verified: a fixed task-reward referee and an explicit rejection step exist (so F3 is largely "
                         "avoided), but in the original configuration the candidate is replayed on its own source task.",
              ["son55:E006", "son55:E022"]),
            X(p, "rsi:evidence_gated_retention/F4", *C(p, "expectations[rsi:evidence_gated_retention/F4].status"), "son55",
              "partial", "Verified: paired rollouts double execution for gate data and admission replays k×2×e runs per "
                         "candidate (opus:O05); no budget-matched baseline spending the same extra calls.",
              ["son55:E013", "son55:E042", "opus:O05"]),
            X(p, "rsi:evidence_gated_retention/H29-step5",
              *C(p, "expectations[rsi:evidence_gated_retention/H29-step5].status"), "son55", "partial",
              "Verified: value-stripped (self-scheduling off) comparison only in the original configuration, +2 points, "
              "single run.", ["son55:E021", "son55:E022"]),
            X(p, "rsi:evidence_gated_retention/H30-step5",
              *C(p, "expectations[rsi:evidence_gated_retention/H30-step5].status"), "son55", "partial",
              "Verified: frozen memory on a held-out conversation exists for CMG, but no governed-vs-ungoverned held-out "
              "comparison and the frozen SEDM memory gives no gain (opus:O04).",
              ["son55:E040", "son55:E041", "son55:E023", "opus:O04"]),
            X(p, "rsi:evidence_gated_retention/S3", *C(p, "expectations[rsi:evidence_gated_retention/S3].status"), "son55",
              "partial", "Verified: indiscriminate injection hurts in two settings (controller memory 0.518 vs 0.534; "
                         "insight-note pilot), effects within noise by the authors' own statement.",
              ["son55:E032", "son55:E031", "son55:E026"]),
            X(p, "rsi:evidence_gated_retention/S4", *C(p, "expectations[rsi:evidence_gated_retention/S4].status"), "son55",
              "met", "S4 is a design-level condition (separable gate/value signal); met. The original-configuration "
                     "weakness sol cites is scored in E.causality/E.holdout.", ["son55:E027", "son55:E028", "son55:E021"]),
            X(p, "rsi:index_experience_for_reuse/H05", *C(p, "expectations[rsi:index_experience_for_reuse/H05].status"),
              "same_supported_fact", "met (merged into rsi:index_experience_for_reuse/H05-step3)",
              "sol's bare-H05 check (gate picks right, not just less, on the same store and runs) is the same fact son55 "
              "recorded as H05-step3; both met. Merged.", ["sol:E013", "son55:E026", "son55:E028"]),
            X(p, "rsi:index_experience_for_reuse/H05-step3",
              *C(p, "expectations[rsi:index_experience_for_reuse/H05-step3].status"), "son55", "met",
              "Verified; merged with sol's H05 (same fact).", ["son55:E026", "son55:E027", "son55:E043", "sol:E013"]),
            X(p, "rsi:index_experience_for_reuse/H05-step5",
              *C(p, "expectations[rsi:index_experience_for_reuse/H05-step5].status"), "son55", "partial",
              "Verified: one agent model and one gate backbone; two datasets for the gate.", ["son55:E035"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.M: CMG alone would be 4; the sender half (self-confirming original admission, ad hoc "
                "constants) holds the method at 3.", ["son55:E006", "son55:E029"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.holdout: headline gains lack selection/test separation (evaluation-stream weight "
                "correction) and the held-out memory shows no gain.", ["opus:O01", "opus:O04", "son55:E023"],
                "−2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.cost: admission replay/controller/gate-training costs uncharged against a headline token "
                "claim.", ["opus:O05", "opus:O06", "sol:E026"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.reason", "sol_value": "3 — strict splits; old tables source-task admission",
             "son55_value": "2 — source-task admission not re-run; gold-evidence memory",
             "final_value": "2, adding the defect neither seat recorded: in the original configuration the controller keeps "
                            "correcting item weights from outcomes on the evaluation stream (§4.6 contrast, App. A update rule)",
             "correction": "Both seats framed the Table 1–3 problem only as source-task admission; §4.6 states that, unlike "
                           "there, the frozen held-out memory's weights cannot be corrected during testing, which implies "
                           "test-stream feedback in the headline runs.",
             "evidence_ids": ["opus:O01", "opus:O03"], "score_impact": "none beyond the son55 value already chosen"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before seat scores: in scope; CMG well controlled (same cached executions, "
                                                   "random-gating line); sender-side gains only in the original configuration "
                                                   "with test-time weight correction; held-out SEDM memory no gain; initial "
                                                   "bands G3 M3 X3 Em3 Ec3 Eh2 Es2 Ecost2; evidence_level task.",
            "integrity_checks": "Both seats a1 on 2509.09498v4, material sha 01358ed0…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid; son55 outside_taxonomy and sol AAP both checked.",
            "core_claim_check": "Re-read §3–4.7, Limitations and App. A–H; located the §4.6 'cannot correct their weights "
                                "during testing' contrast and the App. A original update rule.",
            "rating_agreement": "5/8 identical and re-checked; M → son55, E.holdout → son55, E.cost → sol.",
            "expectation_renumbering": "sol local-1→local-2 (merged), local-2→local-4, H05→H05-step3 (merged); local-3 "
                                       "same question in both seats (statistics), merged without collision.",
            "retained_vs_retained_gain": "Memory is retained with provenance; a retained gain under held-out admission is not "
                                         "shown (opus:O04).",
        },
    }

    # =========================================================== 2509.23863 SPELL (both out_of_scope)
    p = "2509.23863"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes self-play fine-tuning). Independently checked: one policy plays "
          "questioner/responder/verifier and all role samples supervise that single policy via GRPO (opus:O01, opus:O02); "
          "every reported result is a trained checkpoint. The history memory is a per-document-cluster training-time queue "
          "that conditions the questioner during rollouts (opus:O03); it is ablated (w/o History Memory) but its effect is "
          "measured only through the trained model, and it is not a non-weight component retained and read by a deployed "
          "system. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "where the unified policy is refined using the collected data, and the enhanced model serves as "
                    "the starting point for the next rollout cycle.", "Figure 2 caption",
                    "Each cycle's product is updated weights."),
            opus_ev(p, "O02", "A central feature of SPELL is that samples generated under different roles supervise a single "
                    "policy", "§3.3", "Questioner, responder and verifier outputs are all training data for one policy."),
            opus_ev(p, "O03", "Initialize a history memory for each document cluster", "Algorithm 1, line 3",
                    "The history memory is a training-loop queue scoped to a document cluster."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): label-free gap; the questioner generates QA from documents, a "
                      "self-consistency verifier plus cover-exact-match manufactures the correctness label, a Gaussian "
                      "difficulty reward steers generation, and the policy is retrained by GRPO — C08 (generate → gate/"
                      "pseudo-label → retrain, iterated).",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering", sub_id="C08",
                               fit="partial (informational, out_of_scope)",
                               reason="Revised from sol's C26: the manufactured signal is a pseudo-label of correctness "
                                      "(verifier majority vote / CEM) for a no-labels gap, which C26's own step 1 routes to "
                                      "the pseudo-label-and-filter loop (C08); consistent with r05b R-Zero and r06a "
                                      "2508.03682 (proposer difficulty reward + majority vote → C08).")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22", fit="medium (informational, out_of_scope)")],
            "unassigned": [], "revision_proposals": [],
        },
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": "C08", "domain_namespace": "rsi",
            "domain_main": "self_generate_the_curriculum", "domain_sub": "H22",
            "operation_correspondence": "Self-generated QA → verifier pseudo-label → GRPO retrain; H22 adds the proposer trained "
                                        "with an intermediate-difficulty (Gaussian) reward against the current responder.",
            "necessary_conditions": ["validity anchor independent of the generator", "difficulty measured on the current solver"],
            "differences": "Informational only; matching is not a Harness-RSI inclusion criterion.",
            "evidence_ids": ["sol:E001", "sol:E002", "sol:E004", "opus:O02"]}],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; benchmark gains are author-reported RL results."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently confirmed)",
        "resolutions": oos_level_res(p, ["opus:O01", "opus:O02"]) + [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                "Informational; main card verified (label-free, signal manufactured from the model's own outputs). son55 "
                "skipped identification for an out_of_scope row, which the contract allows.", ["opus:O02", "sol:E001"],
                NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", "C08"]],
                "Sub-card revised C26 → C08: see rs_pattern.matches reason (pseudo-label-and-filter, run precedent).",
                ["opus:O02", "sol:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["self_generate_the_curriculum", "H22"]],
                "Informational: a proposer trained against the solver with an intermediate-difficulty reward is the H22 "
                "definition (r06a precedent).", ["sol:E001", "sol:E004"], NOSCORE),
            X(p, "local:2509.23863-1", *C(p, "expectations[local:2509.23863-1].status"), "sol", "unmet",
              "Verified (informational): the evaluated product is weights; the history queue is training-time only.",
              ["opus:O01", "opus:O03"]),
            X(p, "rsi:self_generate_the_curriculum/S1", *C(p, "expectations[rsi:self_generate_the_curriculum/S1].status"),
              "sol", "partial", "Verified (informational): grounding filter + CEM are anchors, but the verifier is the same "
                                "policy.", ["sol:E001", "sol:E002"]),
            X(p, "rsi:self_generate_the_curriculum/S3", *C(p, "expectations[rsi:self_generate_the_curriculum/S3].status"),
              "sol", "met", "Verified (informational): the history queue is read by the next questioner rollouts.",
              ["sol:E004", "opus:O03"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §1–3, Algorithm 1, ablation table and App. B/F before "
                                                   "opening seats: one policy, three roles, GRPO; history memory is a "
                                                   "per-cluster training queue → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2509.23863v4, material sha 5f00e01c…; canonical seat hashes equal "
                                "conflicts.json (the sol file's uncommitted E007 locator/quote edit is the hashed version; "
                                "its quote is verbatim in the material); both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03; sol's 'history QA reused across rounds and ablated' "
                                "is correct and does not change scope.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2509.24726 Socratic-Zero (both out_of_scope)
    p = "2509.24726"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the Solver "
          "is updated by DPO on Teacher-verified correct-vs-incorrect pairs and the Generator by value-weighted SFT "
          "distilling the Teacher's problem refinement (opus:O01, opus:O02); the Teacher, its prompts and verification are "
          "fixed. The growing curriculum is training data; every reported result is a trained Solver or a student "
          "fine-tuned on Generator data. No non-weight component is retained and reused. Not scored; null is not a "
          "zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "a fixed Teacher that acts as an oracle for evaluation and problem refinement, and a Generator "
                    "that learns to synthesize a curriculum", "§3.1", "Teacher fixed; Generator learns (weights)."),
            opus_ev(p, "O02", "the Generator learns strategic distillation through value-weighted supervised fine-tuning (WSFT)",
                    "§1 contributions", "Generator update operator is weight training."),
            opus_ev(p, "O03", "to produce 3 variants each, resulting in 3,000 total generated questions", "§4.1 Generator "
                    "Evaluation", "Three variants per seed."),
            opus_ev(p, "O04", "tasked with producing five augmented variants per seed, resulting in 3,000 total generated "
                    "problems per model", "§4.3.1 / appendix procedure",
                    "Five variants per seed for the same 1,000 seeds, yet the same 3,000 total — internally inconsistent."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): the Solver's supervision is a manufactured preference signal — Teacher-"
                      "verified correct vs incorrect attempts harvested into DPO pairs — C26 ('execution-verified versus "
                      "failed trajectories' → contrastive objective).",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering", fit="strong (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H23", fit="medium (informational, out_of_scope)")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": oos_assessment("Not assessed under this rubric; gains are author-reported DPO/WSFT results."),
        "ratings": oos_ratings(a3),
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently confirmed)",
        "resolutions": oos_level_res(p, ["opus:O01", "opus:O02"]) + [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                "Informational; verified. son55 skipped identification for an out_of_scope row, which the contract allows.",
                ["opus:O02", "sol:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["self_supervised_signal_engineering", "C26"]],
                "Informational: unlike SPELL/R-Zero, the load-bearing signal is a preference ordering (verified vs failed "
                "attempts, reference solution as fallback winner) consumed by DPO — C26's harvested-comparison branch.",
                ["sol:E001", "sol:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["self_generate_the_curriculum", "H23"]],
                "Informational: the Teacher turns each Solver failure into a targeted new problem — a per-instance "
                "diagnostic drives regeneration (H23), with a fixed rather than co-trained proposer.",
                ["sol:E004", "opus:O01"], NOSCORE),
            X(p, "local:2509.24726-1", *C(p, "expectations[local:2509.24726-1].status"), "sol", "unmet",
              "Verified (informational): products are trained Solver/Generator weights.", ["opus:O01", "opus:O02"]),
            X(p, "local:2509.24726-2", *C(p, "expectations[local:2509.24726-2].status"), "sol", "unmet",
              "Verified (informational): 100 MATH seeds plus a 1,500-problem SFT warm-up are prerequisites, and the "
              "generator evaluation states both 3 and 5 variants per seed for the same 3,000 total (opus:O03, opus:O04).",
              ["sol:E003", "sol:E006", "opus:O03", "opus:O04"]),
            X(p, "rsi:self_generate_the_curriculum/S1", *C(p, "expectations[rsi:self_generate_the_curriculum/S1].status"),
              "sol", "partial", "Verified (informational): validity rests on the fixed Teacher's own verification.",
              ["sol:E001", "sol:E002"]),
            X(p, "rsi:self_generate_the_curriculum/S3", *C(p, "expectations[rsi:self_generate_the_curriculum/S3].status"),
              "sol", "met", "Verified (informational): Solver failures each iteration decide what the Teacher makes next.",
              ["sol:E004"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §1–4 and Algorithm 1 before opening seats: DPO Solver + "
                                                   "WSFT Generator under a fixed Teacher → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2509.24726v1, material sha 04b81aa7…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O02; sol's 3-vs-5-variants inconsistency verified "
                                "(opus:O03, opus:O04).",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }
    return S


def batch_notes():
    return [
        "2508.21589 Middo: son55's boundary flag (SFT data, not weights, is rewritten) independently re-checked and "
        "confirmed out_of_scope — the refined dataset is consumed only by the next SFT round and never read at inference; "
        "all results are checkpoints (same as r06a SyncLoop). Informational RS revised heterogeneous_decomposition → C08.",
        "2509.23863 SPELL and 2509.24726 Socratic-Zero: both seats out_of_scope, confirmed (GRPO single policy; DPO Solver + "
        "WSFT Generator). SPELL's history memory is a per-cluster training queue. Informational RS: SPELL C26 → C08 (run "
        "precedent R-Zero/SQLM); Socratic-Zero C26 kept (DPO on verified-vs-failed pairs).",
        "2509.04439 ArcMemo: only E.measurement differed (→ sol 4, contamination belongs to E.holdout per A2). Final 63.75. "
        "Four sol local IDs collided with son55's (two hidden) and were merged into card-condition or son55 IDs.",
        "2509.09498 SEDM: evidence_level → task (headline retained-memory gains use source-task admission and evaluation-"
        "stream weight correction; held-out frozen SEDM memory gives no gain). M → 3, E.holdout → 2 (son55), E.cost → 2 "
        "(sol: admission replay cost uncharged against the token claim). RS revised to adapt_via_conditioning (sub null) per "
        "run memory-system convention. Final 70.0 (sol 77.5, son55 71.25).",
        "Card revision proposals (not applied, for calibration/card_revision_proposals.md): (1) A5 leakage — patterns/sub/"
        "H00.md 'From rejected work' bullet 'Composing modular abstract concepts is a sound idea, but it needs a feedback "
        "gate against flawed concepts and an evaluation larger than a small public set' identifies ArcMemo; rewrite as a "
        "generic condition without outcome detail. (2) son55's H05 variant (supervised calibrated pre-injection gate) and "
        "evidence_gated_retention failure mode (self-confirming source-task admission replay). (3) son55's "
        "abstract_experience_into_guidance condition distinguishing externally seeded from self-generated memories.",
        "Seat file note: seats/sol/attempts/a1/2509.23863.json has an uncommitted working-tree edit (E007 locator/quote); "
        "conflicts.json seat_record_hashes match the edited file, so it is the bound input; the edited quote is verbatim in "
        "the material. Controller should commit or explain it.",
        "No requests for new material.",
    ]
