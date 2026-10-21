"""Opus rulings for r06b a1 (data only; consumed by _build.py)."""
import copy


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}

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

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, dec, final, reason, ev=()):
        sv, nv = C(p, f"expectations[{eid}].status")
        return res(f"expectations[{eid}].status", sv, nv, dec, final, reason, ev, "none (expectations are not scored directly)")

    def RS(p, k, dec, rating, reason, ev, impact):
        sv, nv = C(p, f"ratings.{k}")
        return res(f"ratings.{k}", sv, nv, dec, {"status": "resolved", "rating": rating}, reason, ev, impact)

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    NOSCORE = "none (patterns never score)"

    # =========================================================== 2509.24771 LatentEvolve (Δ11.25)
    p = "2509.24771"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "both MATH and SciBench exhibit similar patterns: as", "§5.4 Sensitivity Analysis",
                    "L′ is swept on two reported test benchmarks; best at L′=30 (MATH 80.3, SciBench 33.4) while the main "
                    "configuration is L′=15 (§5.1). The quoted ablation numbers (SciBench 33.4→28.5 / −6.8) are at L′=30 with "
                    "the backbone unnamed; 33.4 exceeds every SciBench cell in Table 2 (max 31.93), so the ablation is not run "
                    "on the configuration that produced the headline tables."),
            opus_ev(p, "O02", "is set as 15", "§5.1 Evaluation Setup",
                    "Main-table configuration L′=15 (contrast with the L′=30 ablation point, opus:O01)."),
            opus_ev(p, "O03", "is trained to predict the refined latent sequence", "§4.2 Latent Weaver",
                    "The weaver is trained to output z* (the refined latent) from (e_c, z_base)."),
            opus_ev(p, "O04", "first transforms the base latent state (except in the initial round, when", "§4.3 Eq. 8",
                    "At inference the weaver output replaces z_base and momentum Σα(z*−z_base) is then added on top, so a "
                    "refinement offset is applied to an initialiser already trained to predict refined latents; the paper "
                    "neither explains nor ablates this double application."),
            opus_ev(p, "O05", "Results across different iterations with different", "Appendix A.6 Table 6 caption",
                    "Evolution period T is swept on MMLU (a reported test benchmark) with the backbone unnamed."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "son55 adopted. The step that is new relative to LatentSeek is generate (self-rewarded refined latents) → "
                      "single self-score gate τ=0.5 → retrain the weaver on retained triplets, iterated every T=200 queries: C08. "
                      "C26 (sol) needs a comparative/preference unit of supervision consumed as the training signal; here the "
                      "scalar REINFORCE self-reward is inherited from LatentSeek. Retrieval of momenta conditions the frozen "
                      "model (adapt_via_conditioning) but C03 is not assigned under the run convention: the only category-level "
                      "holdout is the one-backbone Fig. 3 study and no equal-budget simpler-conditioning control is run "
                      "(averaging retrieved latents is dismissed in §4.1 but never tested).",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering"), smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                        dmatch("son55", p, "index_experience_for_reuse", "H03")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2509.24771-1"): "local:2509.24771-2",
                    ("son55", "local:2509.24771-2"): "local:2509.24771-1"},
            overrides={
                "local:2509.24771-1": {
                    "status": "partial",
                    "reason": "Opus final (A4 collision: sol local-1 ≡ son55 local-2, both the measurement question). Pass@1 at "
                              "temperature 0 against benchmark answers is a valid outcome metric; the format-heavy self-reward "
                              "(4/7 on format/clarity) is the method's internal signal, not the outcome metric. Its format-repair "
                              "risk is a Vanilla-vs-CoT alternative explanation (E.causality), not a defect of the metric."},
                "local:2509.24771-2": {
                    "status": "unmet",
                    "reason": "Opus final (A4 collision: son55 local-1 ≡ sol local-2, statistics). Full text and appendix "
                              "searched: one run per cell, no seeds, intervals or stream-order variance; 'unknown' is not the "
                              "right state for a completely searched absence."},
                "rsi:index_experience_for_reuse/S2": {
                    "status": "unmet",
                    "reason": "Opus final: S2 requires an external check (executable test, simulation, outcome threshold); "
                              "τ=0.5 is applied to the model's own self-score, i.e. the H03 F4 failure (son55)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01", "opus:O02"]), "C1", ["opus:O05"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Weak retained: the non-weight episodic buffer written from earlier queries is read by later "
                                   "queries and a retrieval-off (w/o Daytime) arm exists, plus one-backbone cross-domain carry-"
                                   "over (Fig. 3). In-domain results are measured on the stream the system evolves on; the "
                                   "ablation is at a non-headline configuration (opus:O01).",
            "claim_support": "scoped",
            "strongest_supported_claim": "Adding a self-score-gated latent episodic buffer and a periodically distilled 1.5B "
                                         "initialiser to LatentSeek-style self-rewarded latent optimisation raises single-run "
                                         "Pass@1 over vanilla/CoT on eight benchmarks and roughly matches TTRL (mostly ≤2 "
                                         "points, losing on AIME25); retrieval-off and weaver-off ablations at L′=30 on one "
                                         "unnamed backbone lower SciBench by 4.9/6.8. Not compute-matched, not reproduced.",
            "unresolved": ["Compute-matched comparison against LatentSeek/TTRL (K=10 × M=8 rollouts plus five judge prompts per "
                           "sample per query).",
                           "Ablation backbone and configuration (L′=30) differ from the headline tables.",
                           "Validity of the format-heavy self-reward as a retention gate; stream-order variance."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. Inter-query independence is a real limitation of per-query latent TTS "
                   "(LatentSeek/SoftCoT), but 'TTS does not evolve' is overbroad: parametric test-time training is acknowledged "
                   "(son55:E003), TTRL — itself a stream-accumulating baseline in Table 1 — sits within ≤2 points, and explicit "
                   "experience memories listed in §2 are neither compared nor shown to leave a residue that latent memory fills. "
                   "sol's 3 relies on lineage it could not check independently.",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E012", "sol:E012"]),
            "M": R("resolved", 2, "Opus sides with son55. The two-timescale mechanism is concrete, but its key assumptions are "
                   "asserted, not tested: that momenta transfer across queries better than averaged latents (son55:E004), that "
                   "the self-score — 4/7 format/clarity — tracks correctness well enough to gate memory, and why a momentum "
                   "offset is added to an initialiser already trained to predict refined latents (opus:O03, opus:O04).",
                   ["son55:E004", "son55:E006", "son55:E009", "opus:O03", "opus:O04", "sol:E009"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Retrieval, τ, T, K, M, L′ are given; top-k, buffer bound/retirement, "
                   "injection point of z and weaver–backbone mapping are not; the retention gate is self-score only; App. A.2 "
                   "names the stored triplet (e, z0, z*) where §4.1 stores (e, z_base, z*).",
                   ["son55:E005", "son55:E008", "son55:E020", "sol:E003", "sol:E004"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. Outcome metric is Pass@1 at temperature 0 against dataset "
                               "answers on standard benchmarks with stated sizes — a valid instrument. son55's concern (vanilla "
                               "far below CoT, deltas computed against Vanilla) is real but is an alternative explanation of the "
                               "gain (scored once, in E.causality per A2), not a defect of the metric. Remaining measurement "
                               "issues: answer-extraction protocol not described; AIME at 30 items with a 2048-token cap.",
                               ["sol:E010", "son55:E013", "son55:E014", "son55:E024", "son55:E025"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked with added defects. Day/night ablations and 13 baselines "
                             "exist, but the ablations are at L′=30 on an unnamed backbone (opus:O01), no gate-off, averaging or "
                             "compute-matched latent-optimisation control is run, Table 2 deltas are against a format-broken "
                             "Vanilla (CoT already +13.8 MMLU), and margins over TTRL are mostly ≤2 points.",
                             ["son55:E012", "son55:E013", "son55:E016", "son55:E017", "sol:E006", "opus:O01"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Unlabelled transductive adaptation on each test stream is a "
                           "legitimate TTS protocol and AIME/GPQA/JAMA give some held-out transfer, but L′ and T are swept on "
                           "reported test benchmarks (opus:O01, opus:O05), the cross-domain study is one backbone, and there is no "
                           "overlap analysis.",
                           ["son55:E010", "son55:E018", "son55:E019", "sol:E005", "sol:E008", "opus:O05"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 rung 1). Sizes stated (AIME 30 → 3.33 per item), "
                              "losses to TTRL reported; one deterministic run per cell, no seeds, intervals or order variance.",
                              ["son55:E024", "sol:E010"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only answer-length ratios (Table 5); per query K=10 × M=8 "
                        "rollouts plus five self-judge prompts per sample and periodic weaver training are neither costed nor "
                        "matched against Pass@1 baselines.",
                        ["son55:E020", "son55:E021", "sol:E011"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendix A (figure-only values used only where quoted in text); in scope (A3 "
                  "second bullet): the retained, later-read episodic buffer is non-weight, the weaver is an auxiliary trained "
                  "component (H28 boundary). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (mixed: evaluated retained non-weight buffer with a retrieval-off arm; auxiliary weaver weights)",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "The contribution beyond LatentSeek is the self-score-gated archive retrained into the weaver (C08 generate → "
                "gate → retrain); the conditioning move is supporting.", ["son55:E008", "son55:E009", "sol:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["self_supervised_signal_engineering", "C08"]],
                "C08 fits (single self-score gate, retained instances retrain a component, iterated). C26 needs a comparative "
                "unit of supervision; C03 dropped under the run convention (no equal-budget simpler-conditioning control; "
                "category holdout only in the one-backbone Fig. 3 study).", ["son55:E004", "son55:E008", "son55:E009"], NOSCORE),
            X(p, "local:2509.24771-1", "revised", "local-1 = measurement question → partial; son55 local-1 (statistics) "
              "renumbered local-2 → unmet",
              "A4 collision: the seats swapped local-1/local-2 (measurement vs statistics). Measurement: valid outcome metric, "
              "format-repair risk belongs to E.causality → partial. Statistics: complete search shows no variance reporting → "
              "unmet (not unknown).", ["sol:E009", "sol:E010", "son55:E006", "son55:E013"]),
            X(p, "local:2509.24771-3", "sol", "partial", "Verified: only answer-length ratios are reported.", ["sol:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
              "Verified: source/target domains separated in Fig. 3 and MATH→AIME; no overlap analysis.", ["sol:E005", "sol:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
              "Verified: averaging retrieved latents is argued against in §4.1 but never run; no nearest-neighbour or longer-"
              "context alternative.", ["son55:E004"]),
            X(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "met",
              "Verified: five backbones from three families on eight benchmarks (Table 2).", ["son55:E012"]),
            X(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "partial",
              "Verified: day/night ablations and Self-Rewarding/Genius baselines; no compute-matched control.",
              ["son55:E016", "son55:E017"]),
            X(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "unmet",
              "Verified: the generation/filter loop cost (K×M rollouts, self-judge calls, weaver training) is not justified.",
              ["son55:E020", "son55:E021"]),
            X(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial",
              "Verified: label-free, but adaptation and scoring share the test stream.", ["son55:E010"]),
            X(p, "rsi:couple_context_and_weight_updates/F4", "son55", "unmet",
              "Failure present (unmet = present): high-self-confidence latents are consolidated into the weaver with no "
              "verifiable-outcome anchor.", ["son55:E008", "son55:E009"]),
            X(p, "rsi:couple_context_and_weight_updates/F5", "son55", "partial",
              "Verified: adaptation stream = scored stream per benchmark; only AIME and the Fig. 3 study separate them.",
              ["son55:E010", "son55:E019"]),
            X(p, "rsi:couple_context_and_weight_updates/S2", "son55", "partial",
              "Verified: episodic vs procedural split with a lever-wise ablation, but only one benchmark's numbers are in text "
              "and at a non-headline configuration.", ["son55:E016", "son55:E017", "opus:O01"]),
            X(p, "rsi:index_experience_for_reuse/S2", "revised", "unmet",
              "The card's S2 asks for an external write check; a self-score threshold is the F4 failure, so sol's partial is "
              "revised to unmet.", ["sol:E003", "son55:E008"]),
            X(p, "rsi:index_experience_for_reuse/S5", "sol", "partial",
              "Verified: retrieval-off (w/o Daytime) arm exists, on the evaluation stream and one benchmark in text.",
              ["sol:E006", "sol:E007"]),
            RS(p, "G", "son55", 2, "See ratings.G: gap overbroad; TTRL and explicit memories leave the residue unmeasured.",
               ["son55:E003", "son55:E012"], "−3.75 vs sol (15×1/4)"),
            RS(p, "M", "son55", 2, "See ratings.M: transfer and gate assumptions asserted; double refinement offset "
               "unexplained.", ["son55:E004", "opus:O03", "opus:O04"], "−5.0 vs sol (20×1/4)"),
            RS(p, "E.measurement", "sol", 2, "See ratings.E.measurement: valid outcome metric; vanilla-format issue is causal "
               "(A2 single-defect rule).", ["sol:E010", "son55:E013"], "+2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.causality.reason",
             "sol_value": "2 — two-lever ablation, no equal total-compute control",
             "son55_value": "2 — ablations, no gate-off/averaging/compute-matched control",
             "final_value": "2 (unchanged) with added defect: ablation and sensitivity numbers are at L′=30 on an unnamed "
                            "backbone, not the L′=15 headline configuration; SciBench 33.4 matches no table cell",
             "correction": "Neither seat noticed that the only quantified ablation is run off the headline configuration.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
            {"field_path": "ratings.M.reason",
             "sol_value": "3 — self-score and latent transfer premises under-verified",
             "son55_value": "2 — momentum vs averaging asserted",
             "final_value": "2 with added point: the weaver is trained to output z* and the momentum offset is then added again",
             "correction": "Both seats missed the unexplained composition of weaver output and momentum transfer (Eq. 7 vs Eq. 8).",
             "evidence_ids": ["opus:O03", "opus:O04"], "score_impact": "none beyond the M resolution"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all sections and Appendix A first: in scope (non-weight episodic buffer "
                                                   "read by later queries; auxiliary weaver weights); self-score gate; single "
                                                   "runs; ablations only at L′=30; compute uncosted; initial bands G2 M2 X2 "
                                                   "Em2 Ec1–2 Eh1–2 Es1 Ecost0–1.",
            "integrity_checks": "Both seats a1 on 2509.24771v1, material sha 7399f078…; canonical seat hashes equal "
                                "conflicts.json; RS parents valid (C08⊂sse, C26⊂sse, C03⊂avc); domain ids valid.",
            "core_claim_check": "Re-read Table 1/2, §5.3–5.4, A.1–A.6; recomputed TTRL margins and abstract '13.33' (vs LatentSeek, "
                                "AIME24); located the L′=30 ablation and T sweep on test benchmarks.",
            "rating_agreement": "5/8 identical and re-checked (E.causality kept with added defect); G, M → son55; E.measurement → sol.",
            "expectation_renumbering": "son55 local-1 ↔ local-2 swapped to match sol's questions (A4).",
        },
    }

    # =========================================================== 2509.25140 ReasoningBank (Δ7.5)
    p = "2509.25140"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "scaling actually reduces performance for weaker memories, where Synapse slightly increases from",
                    "§4.4 Scaling yields better memory curation",
                    "Text says scaling reduces performance for weaker memories while the quoted numbers rise (Synapse 40.6→41.2, "
                    "AWM 44.4→45.5): a text–number contradiction in the synergy argument."),
            opus_ev(p, "O02", "but also sustains strong growth with scaling, reaching 62.1 at", "Appendix C.3 Pass@k",
                    "C.3 attributes 52.4 at k=5 to 'MaTTS w/o memory', whereas §4.3 gives 52.4 at k=5 for vanilla TTS (w/o "
                    "aggregation) and w/o memory peaks at 42.2 — a label inconsistency."),
            opus_ev(p, "O03", "or instance-level concepts", "§2 Related Work",
                    "Neighbours that store strategy/concept-level lessons (cited Suzgun et al. 2025; Zhao et al. 2024) are "
                    "listed but not run; only Synapse and AWM are baselines (son55:E026)."),
            opus_ev(p, "O04", "pass@1) on WebArena benchmark.", "Table 1 caption",
                    "The '+MaTTS' rows in Table 1 are parallel scaling with k=5 rollouts per query, placed next to k=1 "
                    "baselines."),
            opus_ev(p, "O05", "System instructions for extracting memory items from agent trajectories", "Appendix A.1 Figure 9 caption",
                    "Extraction, judge, MaTTS and BoN prompts are figure images (Figs. 9–12); their text is not in the pinned material."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering"], "outside_taxonomy": False,
            "reason": "Both seats C03 (retrieved strategy items condition a frozen agent; Mind2Web cross-website/cross-domain "
                      "splits and the WebArena Multi subset give category-level evaluation, and Synapse under identical "
                      "retrieval/consolidation is the simpler-conditioning control, so C03 is kept under the run convention). "
                      "son55's supporting self_supervised_signal_engineering (sub null) is kept: the label-free LLM-judge "
                      "success/failure signal is load-bearing (it routes extraction and is the object of the Fig. 8 noise "
                      "study), though it trains nothing, so no C07/C08/C26.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"), smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2509.25140-2"): "local:2509.25140-3"},
            overrides={
                "local:2509.25140-1": {
                    "status": "unmet",
                    "reason": "Opus final: complete search finds no seeds, repeats, intervals or order variance at temperature "
                              "0.7; son55's 'partial' credited controls (store-off, matched-k scaling), which answer other "
                              "questions."},
                "local:2509.25140-3": {
                    "reason": "son55 local-2 renumbered (A4 collision with sol local-2 = cost). Raw-trajectory (Synapse) and "
                              "workflow (AWM) extraction compared under identical retrieval/consolidation."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01", "opus:O02", "opus:O04"]), "C2", ["opus:O03"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Memory written from earlier queries is read by later queries and a same-agent No-Memory control "
                                   "exists on three benchmarks; the stream is prequential (each query scored before its own "
                                   "memory is written) but there is no frozen-memory held-out split.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, author-reported: strategy items distilled from LLM-judged successes and "
                                         "failures, appended and retrieved top-1, raise WebArena SR by +8.3/+7.2/+4.6 and "
                                         "SWE-Bench-Verified by +4.6/+3.4 over no memory and by ~4–6 over Synapse/AWM under "
                                         "identical retrieval/consolidation, at ~4% extra tokens; failure inclusion and MaTTS "
                                         "synergy shown on one subset/backbone. Not reproduced.",
            "unresolved": ["Run/order variance at temperature 0.7.",
                           "Comparison with other strategy/failure-aware memories (cited, not run).",
                           "§4.4 and C.3 text–number inconsistencies (opus:O01, opus:O02).",
                           "Unbounded append-only store; judged-wrong items admitted."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The limitation of raw-trajectory and success-only memories is specific "
                   "and the two named neighbours are run, but the paper's own related work lists strategy/concept-level stores "
                   "(opus:O03) and the Limitations concede no broader memory comparison (son55:E026), so the 'uniquely learns "
                   "from failures' residue is not established against the nearest neighbours.",
                   ["son55:E001", "son55:E008", "son55:E026", "opus:O03", "sol:E003"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Outcome-branched extraction, top-1 retrieval and MaTTS self-contrast "
                   "make distinguishable predictions that are tested (extraction-only comparison, failure on/off, k sweep, "
                   "memory-vs-no-memory scaling).",
                   ["son55:E002", "son55:E004", "son55:E008", "son55:E017", "son55:E018"]),
            "X": R("resolved", 2, "Opus sides with son55. Retrieval/injection and append are stated, but consolidation is "
                   "append-only with no gate, dedup, retirement or bound, judged-wrong items enter unchecked, query order and "
                   "memory sharing across WebArena subsets are unspecified, and the extraction/judge prompts exist only as "
                   "figure images (opus:O05); sol's 'prompt injection reconstructable' covers only the retrieval instruction.",
                   ["son55:E005", "son55:E006", "son55:E007", "opus:O05", "sol:E002"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Official WebArena/SWE-Bench-Verified evaluators, "
                               "standard Mind2Web metrics, measured judge accuracy (72.7%) and noise simulation; Mind2Web task "
                               "SR sits near a 1–5% floor and BoN uses the backbone as selector.",
                               ["son55:E009", "son55:E013", "son55:E015", "son55:E016", "son55:E020", "sol:E011"]),
            "E.causality": R("resolved", 3, "Both seats 3; re-checked with added defects. No-Memory and extraction-only "
                             "comparisons under identical retrieval/consolidation are strong controls; failure on/off and "
                             "matched-k w/o-memory/w/o-aggregation scaling support the secondary claims. Weakening: ablations on "
                             "one subset/backbone and text–number contradictions in the synergy argument (opus:O01, opus:O02).",
                             ["son55:E008", "son55:E011", "son55:E017", "son55:E018", "son55:E019", "opus:O01", "opus:O02"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Label-free prequential streaming (each query answered "
                           "before its memory is written) is declared, but there is no frozen held-out split, no overlap "
                           "analysis, and k=1 was chosen on a reported subset.",
                           ["son55:E003", "son55:E021", "sol:E001"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 rung 1). Subset sizes given, negative results "
                              "reported (k>1 declines, AWM drop); single runs at temperature 0.7 with few-task differences "
                              "(Multi n=29).", ["son55:E009", "son55:E017", "son55:E024", "sol:E008"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Per-trajectory token breakdown including judge and extraction "
                        "for the method and both memory baselines (+4.3% vs No Memory), step counts, and matched-k w/o-memory "
                        "scaling controls; MaTTS k-fold rollout cost is only implicit (opus:O04) and Table 5's setting is "
                        "unstated, which keeps it below 4.",
                        ["son55:E022", "son55:E023", "son55:E018", "sol:E007", "opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–F (prompts and Figs. 4–8 values only where quoted in text); in "
                  "scope (A): non-weight strategy memory written after each task and read by later tasks. All eight resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (both seats; non-weight memory evaluated)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["self_supervised_signal_engineering", None]],
                "C03 kept (category-level splits and Synapse as same-pipeline simpler conditioning). The LLM-judge proxy label "
                "is a load-bearing manufactured signal (main card), no sub-card because nothing is trained on it.",
                ["son55:E002", "son55:E004", "son55:E015", "son55:E016"], NOSCORE),
            X(p, "local:2509.25140-1", "sol", "unmet",
              "Statistics question in both seats; no variance reporting anywhere.", ["son55:E024", "sol:E008"]),
            X(p, "local:2509.25140-2", "revised", "local-2 = cost question → partial; son55 local-2 renumbered local-3 → met",
              "A4 collision: sol local-2 asks about cost (Table 5 covers judge/extraction, MaTTS k-fold not tabulated → "
              "partial); son55 local-2 asks about abstraction alternatives (Synapse/AWM under identical retrieval → met).",
              ["sol:E007", "son55:E008", "opus:O04"]),
            X(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
              "Verified: No-Memory with the same agent and extraction-only variants.", ["son55:E008", "son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
              "The expectation asks for a contamination/overlap analysis; none exists. Category splits (sol's credit) do not "
              "answer it.", ["son55:E003"]),
            X(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
              "Verified: Synapse (raw-trajectory retrieval) is the cheaper baseline; no long-context baseline.", ["son55:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
              "Verified: k sweep and judge-noise simulation on one subset.", ["son55:E016", "son55:E021"]),
            X(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "met",
              "Verified for the base loop: judge + extraction tokens costed against the benefit (+4.3% tokens).",
              ["son55:E022", "son55:E023"]),
            X(p, "rsi:abstract_experience_into_guidance/H00", "sol", "partial",
              "H00 certification: later tasks (not the lesson sources) improve with a store-off control, but no frozen held-out "
              "set and no retries-matched control for the base loop.", ["sol:E001", "sol:E012"]),
            X(p, "rsi:abstract_experience_into_guidance/S3", "sol", "met",
              "Verified: self-judge with measured 72.7% accuracy and noise simulation; son55 recorded the same as met in its "
              "H00 condition checks.", ["sol:E004", "son55:E015"]),
            X(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
              "No test decides which entries survive: every extracted item is appended; the judge only routes the extraction "
              "prompt.", ["son55:E005", "sol:E002"]),
            RS(p, "G", "son55", 2, "See ratings.G: nearest strategy-level stores listed but not compared.",
               ["son55:E026", "opus:O03"], "−3.75 vs sol (15×1/4)"),
            RS(p, "X", "son55", 2, "See ratings.X: append-only, no gate/retirement, prompts figure-only, order unspecified.",
               ["son55:E005", "son55:E007", "opus:O05"], "−5.0 vs sol (20×1/4)"),
            RS(p, "E.cost", "son55", 3, "See ratings.E.cost: full token breakdown incl. judge/extraction; MaTTS implicit.",
               ["son55:E023", "sol:E007"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.causality.reason",
             "sol_value": "3 — fixed-retrieval abstraction, failure and aggregation ablations",
             "son55_value": "3 — store-off, extraction-only, failure, scaling controls",
             "final_value": "3 (unchanged) with added defects: §4.4 says scaling reduces weaker memories while its numbers rise; "
                            "C.3 labels the 52.4 vanilla-TTS figure as 'w/o memory'",
             "correction": "Both seats missed two internal inconsistencies in the MaTTS synergy evidence.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all sections and appendices first: in scope; strong same-pipeline controls; "
                                                   "official metrics; single runs at T=0.7; prequential stream; append-only; "
                                                   "neighbours partly unrun; initial bands G2 M3 X2–3 Em3 Ec3 Eh2 Es1 Ecost2–3.",
            "integrity_checks": "Both seats a1 on 2509.25140v2, material sha e26c66a8…; hashes equal conflicts.json; C03⊂avc valid.",
            "core_claim_check": "Recomputed Table 1 overall deltas, checked Table 5 (+4.3%), Fig. 7/13 quoted values; found §4.4 and "
                                "C.3 inconsistencies.",
            "rating_agreement": "5/8 identical and re-checked; G, X, E.cost → son55.",
            "expectation_renumbering": "son55 local-2 → local-3.",
        },
    }

    # =========================================================== 2509.26100 AgenticEval (Δ3.75)
    p = "2509.26100"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "omits the self-evolving loop, reducing the pipeline to a static audit.", "§4.2 Ablation (3)",
                    "w/o Refine is described as a static audit, yet its final-iteration GPT-5 EU AI Act rate is 48.60 while the "
                    "initial (static) round is 72.50; what the variant regenerates across rounds is unstated."),
            opus_ev(p, "O02", "Safety performance (%) of evaluated LLMs under three frameworks", "Table 1 caption",
                    "Table 1 does not state which iteration it reports; GPT-5 EU AI Act AVG 67.16 matches neither the initial "
                    "72.50 nor the final 36.36."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Low fit either way. The ablated load-bearing step is decomposing a regulation into atomic rules plus "
                      "search-grounded guidance that the Generator consumes (w/o Structure 64.29→75.40), i.e. decompose_and_"
                      "delegate. C25 is not assigned: its crux — a machine-checkable artifact whose solver/validator verdict "
                      "closes the loop — is absent (rule trees are advisory, the loop signal is an LLM judge on generated "
                      "criteria). controlled_diagnostic_design (son55) is rejected: no named confound is isolated and the "
                      "headline is a pass-rate drop, not a de-confounded gap.",
            "matches": [smatch("sol", p, "decompose_and_delegate", sub_id=None, fit="low",
                               reason="Regulation → atomic rules → typed agent deliverables; no sound solver or mechanically "
                                      "checkable artifact, so no C25.")],
            "executes_pattern": "partial", "resolves_problem": "not_shown",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "coevolve_the_evaluator", None)],
            "unassigned": [], "revision_proposals": [],
        },
        "paper_update": {"claim_type": "evaluation_resource"},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2509.26100-1"): "local:2509.26100-3"},
            overrides={
                "rs:controlled_diagnostic_design/RE-3": {
                    "status": "partial",
                    "reason": "Opus final: a static variant (w/o Refine) and three jailbreak baselines exist, so the item is not "
                              "absent, but none is test-count or compute matched and the static variant is ill-defined "
                              "(opus:O01). Card not matched; kept as a valid check question."},
                "rs:controlled_diagnostic_design/RE-6": {
                    "status": "unmet",
                    "reason": "Opus final: complete search finds no attempt to show hardened tests reflect real deployment "
                              "failures; a searched absence is unmet, not unknown."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O02"]), "C2", ["opus:O01"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Within-run adaptation on the same target: tests evolved from a model's failures are scored on "
                                   "that model; no cross-target or cross-run retention is evaluated (EVIDENCE rule 2).",
            "claim_support": "scoped",
            "strongest_supported_claim": "In a three-round, single-run protocol (GPT-4.1 judge/analyst, Gemini-2.5-Pro generator), "
                                         "failure-conditioned regeneration lowers judged safety rates (GPT-5 EU AI Act 72.50→36.36) "
                                         "and the judge agrees with humans on 88–91% of 100 sampled cases per framework; the "
                                         "validity of hardened tests, suite sizes and transfer across targets are not shown.",
            "unresolved": ["Test-validity audit of evolved items.", "Suite sizes/denominators.",
                           "Definition of the w/o-Refine variant (opus:O01) and Table 1 iteration (opus:O02).",
                           "Fig. 3/4 values beyond the quoted sentences (page render optional; would not change ratings)."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. Static lag is a real evaluation defect, but adaptive self-evolving "
                   "red-teamers (AutoDAN-Turbo, AutoRedTeamer, ALI-Agent) and regulation codification (COMPL-AI, PolicyPulse) are "
                   "acknowledged; the residue is their combination, and its marginal value over adaptive red-teaming is not "
                   "isolated (no static regulation benchmark or ALI-Agent run).",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E004", "sol:E001"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Concrete pipeline (rule tree, grounded guidance, question groups, "
                   "rubric judge, Analyst→Generator loop), but 'lower pass rate = deeper vulnerability' is an unsupported "
                   "assumption and no test-validity mechanism exists.",
                   ["son55:E005", "son55:E006", "son55:E012", "son55:E022"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Roles, models, K_max=3 and Algorithm 1 given; suite sizes, de-"
                   "duplication/validity filtering of generated tests, Analyst state across rounds and full prompts missing.",
                   ["son55:E006", "son55:E007", "son55:E008", "son55:E021", "sol:E009"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked with added defect. Judge validated against 100 human-"
                               "labelled cases per framework (κ 0.77–0.81); but efficacy is defined as a lower pass rate (a "
                               "metric invalid tests can satisfy), evolved-item validity is never audited, the audited round is "
                               "unstated, and Table 1's iteration is unspecified (opus:O02).",
                               ["son55:E012", "son55:E016", "son55:E017", "sol:E006", "opus:O02"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked with added defect. Three component ablations and jailbreak "
                             "baselines exist (mostly figure-only); test counts/compute unmatched; adversarial conditioning on the "
                             "target's own failures predicts a drop regardless of validity; the w/o-Refine 'static audit' "
                             "(48.60) does not equal the initial static round (72.50), so the variant is ill-defined (opus:O01).",
                             ["son55:E013", "son55:E014", "son55:E015", "sol:E004", "opus:O01"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Tests evolved on a target are scored on that target; no "
                           "cross-target transfer, static-benchmark comparison or contamination analysis; breadth (3 regulations, "
                           "11 models) only.", ["son55:E011", "son55:E002", "sol:E001"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 rung 1, marginal). Judge audit gives n=100 and κ; "
                              "main safety rates have no suite sizes (implied 16–29 per category), seeds or intervals.",
                              ["son55:E010", "son55:E017", "sol:E006"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked. Full text and appendix give no tokens, calls, "
                        "dollars or latency; only a qualitative limitation sentence.", ["son55:E019", "sol:E008"],
                        scope=["full pinned text incl. Limitations and Appendix A.1–A.3: no quantitative cost, token, call or "
                               "latency figure for the loop or for baselines"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendix (Figs. 2–4 values only where quoted); in scope as evaluation_resource "
                  "(an evaluator/test-suite component updated from execution feedback across rounds). All eight resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (both seats; evaluator component is non-weight)",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "son55", "evaluation_resource",
                "The product is a benchmark-generating evaluator and its pass-rate findings; no agent is improved. SCORE_SPEC "
                "evaluation_resource reading applies.", ["son55:E009", "son55:E011"], "none (frozen type reading)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "Retained requires the retained change to help later, ideally held-out, use; here the 'improvement' is measured "
                "on the same target that produced the feedback, within one run (EVIDENCE rule 2).",
                ["son55:E011", "sol:E002"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "decompose_and_delegate",
                "The ablated load-bearing step is regulation decomposition consumed downstream; no confound is isolated.",
                ["son55:E013", "sol:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["decompose_and_delegate", None]],
                "Main card from sol, sub null as in son55's reasoning: C25 needs a mechanically checkable artifact and a "
                "solver/validator verdict closing the loop.", ["son55:E006", "sol:E011"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55", [["coevolve_the_evaluator", None]],
                "H25 requires evaluator revision gated by agreement with an isolated trusted anchor; tests here harden from "
                "target failures with no anchor-gated acceptance — the card's F4 failure, not H25.",
                ["son55:E006", "son55:E016"], NOSCORE),
            X(p, "local:2509.26100-2", "son55", "unmet", "Verified: no suite evolved on one model is run against another.",
              ["son55:E011"]),
            X(p, "local:2509.26100-3", "same_supported_fact", "unmet",
              "sol asked the same statistics question under local-1 (A4 collision, renumbered to local-3); both unmet.",
              ["son55:E010", "sol:E006"]),
            X(p, "rs:controlled_diagnostic_design/RE-2", "son55", "met", "Verified: 3 regulations × 11 models.",
              ["son55:E010"]),
            X(p, "rs:controlled_diagnostic_design/RE-3", "revised", "partial",
              "Static variant and jailbreak baselines exist (not unmet) but none is matched and the static variant is "
              "ill-defined.", ["son55:E014", "son55:E015", "opus:O01"]),
            X(p, "rs:controlled_diagnostic_design/RE-4", "son55", "partial",
              "Verified: human audit of the judge only; GPT-4.1 both authors guidance and judges.", ["son55:E008", "son55:E016"]),
            X(p, "rs:controlled_diagnostic_design/RE-6", "revised", "unmet",
              "Searched absence → unmet, not unknown.", ["son55:E012"]),
            X(p, "rs:decompose_and_delegate/RE-1", "sol", "unmet", "Verified: no quantitative cost.", ["sol:E008"]),
            X(p, "rs:decompose_and_delegate/RE-2", "sol", "partial",
              "Verified: Structure/Enrich/Refine ablations, unmatched budgets.", ["sol:E004", "son55:E013"]),
            X(p, "rs:decompose_and_delegate/RE-3", "sol", "partial", "Verified: prompts are stated abstractions only.",
              ["sol:E009", "son55:E021"]),
            X(p, "rsi:coevolve_the_evaluator/F4", "son55", "unmet",
              "Failure present: adaptive hardening changes what is measured and no anchor certifies the new items; the human "
              "audit validates judge decisions, not test validity.", ["son55:E012", "son55:E016"]),
            X(p, "rsi:coevolve_the_evaluator/S4", "son55", "unmet", "Verified: no reproducible validity check on new items.",
              ["son55:E006"]),
            RS(p, "G", "son55", 2, "See ratings.G: adaptive evaluators exist; regulation-ingestion residue not isolated.",
               ["son55:E003", "son55:E004"], "−3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.causality.reason",
             "sol_value": "2 — ablations and attack baselines, unmatched distribution/budget",
             "son55_value": "2 — ablations mostly figure-only, unmatched, no random regeneration",
             "final_value": "2 (unchanged) with added defect: the w/o-Refine 'static audit' scores 48.60 vs 72.50 for the "
                            "initial static round, so the variant is undefined",
             "correction": "Neither seat checked the static variant against the initial-round score.",
             "evidence_ids": ["opus:O01"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all sections and appendix first: evaluation_resource; lower pass rate taken "
                                                   "as efficacy without test-validity audit; judge audited; no suite sizes; no "
                                                   "cost; same-target selection = test; initial bands G2 M2 X2 Em1–2 Ec1–2 Eh1 "
                                                   "Es0–1 Ecost0.",
            "integrity_checks": "Both seats a1 on 2509.26100v2, material sha 97add114…; hashes equal conflicts.json.",
            "core_claim_check": "Re-read §3.3, §4.2 ablation and Table 1/2; checked 72.50/36.36/48.60/67.16 consistency.",
            "rating_agreement": "7/8 identical and re-checked (E.measurement and E.causality kept with added defects; E.statistics "
                                "kept at 1 as marginal); G → son55.",
            "expectation_renumbering": "sol local-1 → local-3 (merged with son55 local-3).",
        },
    }

    # =========================================================== 2510.04618 ACE (Δ1.25)
    p = "2510.04618"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "ReAct + ACE + offline warmup ✗ 69.6 + 5.9", "Table 3 (ablations), online block",
                    "The online ACE row of Table 1 (69.6/53.6/66.0/48.9/59.5) is identical to Table 3's 'ACE + offline warmup' "
                    "row; pure online ACE is 56.1 average. The online '+7.6 over DC' (59.5 vs 51.9) therefore uses a context "
                    "warmed up on the training split; without warmup the margin is +4.2."),
            opus_ev(p, "O02", "56.1 + 13.7", "Table 3, online ACE without warmup (average)",
                    "Pure online ACE average 56.1."),
            opus_ev(p, "O03", "These gains extend to the online setting, where ACE continues to outperform prior adaptive "
                              "methods such as Dynamic Cheatsheet by an average of 7.6%.", "§4.3 Analysis",
                    "The online headline margin is stated without noting the offline warmup."),
            opus_ev(p, "O04", "Empirically, 5 rounds offers a good balance.", "Appendix A.6, Table 19",
                    "Table 19's 5-round offline row is 72.6/62.5 (avg 67.6) vs Table 1/18 offline ACE 76.2/64.3 (avg 70.3) in "
                    "what is described as the default 5-round configuration; the difference (−3.6 TGC) is unexplained — either "
                    "an unstated config change or run-to-run variance the paper never reports."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "son55 adopted. Conditioning a frozen model on an evolving playbook is the main move; C03 is not assigned "
                      "under the run convention (no category holdout: offline is an instance split of the same benchmark, no "
                      "cross-domain playbook transfer). Many-shot ICL is a simpler-conditioning control but does not substitute "
                      "for the holdout. The load-bearing, ablated innovation — LLM-written itemized deltas merged by "
                      "deterministic non-LLM logic (Table 18) — is the C25 move of confining the LLM to extraction/interfacing "
                      "and offloading structured bookkeeping to exact code (partial: no verifier closes the loop).",
            "matches": [smatch("son55", p, "adapt_via_conditioning"), smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2510.04618-1"): "local:2510.04618-2",
                    ("son55", "local:2510.04618-2"): "local:2510.04618-1"},
            overrides={
                "local:2510.04618-1": {
                    "status": "partial",
                    "reason": "Opus final (A4 collision: son55 local-2 ≡ sol local-1 = cost). Latency, rollouts, tokens and "
                              "dollars are reported in detail (so not unmet), but Table 4(a) (357 rollouts, −75.1%) contradicts "
                              "Table 12 (2,075, +42.6%, at a cheaper 1-epoch/1-round setting), evaluation input tokens are "
                              "+117%, and the cache study uses another model."},
                "local:2510.04618-2": {
                    "status": "unmet",
                    "reason": "Opus final (A4 collision: son55 local-1 ≡ sol local-2 = statistics). No seeds, intervals or order "
                              "variance; Table 19 vs Table 1 suggests unreported variance (opus:O04). son55's 'partial' credited "
                              "store-off/ablation controls, which answer a different question."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03", "opus:O04"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Offline playbooks built on the training split improve the held-out test split; removing "
                                   "incremental updates removes most of the AppWorld gain. Not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, DeepSeek-V3.1 in all roles: an itemized playbook updated by LLM-written "
                                         "deltas with deterministic merge/dedup raises offline AppWorld by +17.0 (with GT) / "
                                         "+14.8 (execution feedback only) average and labelled finance by +12.8 over the base "
                                         "agent, above ICL/MIPROv2/GEPA; online it beats DC by +4.2 without warmup (+7.6 with "
                                         "offline warmup). Gains need informative feedback; the rollout-saving claim is "
                                         "internally contradicted. Not reproduced.",
            "unresolved": ["357 vs 2,075 rollout contradiction (Table 4a vs Table 12).",
                           "Online headline uses offline warmup (opus:O01).",
                           "Table 19 vs Table 1 offline discrepancy; run/order variance.",
                           "Contamination/overlap; dedup and counter ablations."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Brevity bias and context collapse are specific and sourced (DC "
                   "18,282→122-token collapse with accuracy 66.7→57.1), DC/GEPA/MIPROv2 are run under a matched LLM; A-MEM/AWM-"
                   "style incremental stores are discussed but not run and collapse rests on one trace.",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E034", "sol:E007"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Itemized deltas merged deterministically answer detail loss under "
                   "monolithic rewriting with a distinguishable prediction tested by the no-incremental-update ablation and "
                   "reflector-noise stress tests.", ["son55:E005", "son55:E006", "son55:E019", "son55:E020"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Roles, merge/dedup/pruning triggers, epochs and rounds specified; "
                   "missing admission validation, retirement/rollback, use of helpful/harmful counters, the no-incremental "
                   "variant's implementation, and prompt text (figures).",
                   ["son55:E005", "son55:E006", "son55:E007", "son55:E008", "son55:E012"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Official AppWorld TGC/SGC and exact-match finance "
                               "accuracy; BIRD-SQL (appendix) uses an LLM judge; GT-label vs no-label rows separated.",
                               ["son55:E030", "son55:E029", "son55:E016", "sol:E006"]),
            "E.causality": R("resolved", 3, "Both seats 3; re-checked with added defect. Same-LLM ICL/MIPROv2/GEPA/DC baselines, "
                             "Reflector/multi-epoch/warmup/incremental-update ablations, weaker/harmful-reflector tests and "
                             "label/no-label rows are strong. Weakening: baselines not rollout-matched, no dedup/counter "
                             "ablation, and the online comparison with DC uses an offline-warmed ACE (opus:O01: +7.6 → +4.2 "
                             "without warmup). The direction of every main comparison survives, so 3 holds.",
                             ["son55:E011", "son55:E014", "son55:E015", "son55:E018", "son55:E019", "son55:E020",
                              "opus:O01", "opus:O02", "opus:O03"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Offline train→test splits and a declared prequential online "
                           "protocol with a shared order; hyperparameters swept on test data (Tables 19–21) and no overlap "
                           "analysis keep it below 4.", ["son55:E009", "son55:E010", "son55:E028", "sol:E004"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 rung 1). Negative cells reported honestly (no-label "
                              "finance −3.4, harmful-reflector −4.0, Llama small gains); single runs, no seeds/intervals, and "
                              "an unexplained 3.6-point gap between nominally identical offline configurations (opus:O04).",
                              ["son55:E017", "son55:E032", "sol:E005", "opus:O04"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Costs are tabulated in detail, but the headline '−75.1% rollouts' "
                        "(Table 4a: 357) is contradicted by Table 12 (2,075, +42.6%) measured at a cheaper 1-epoch/1-round "
                        "setting than the 5/5 configuration that produced the accuracy; evaluation-stage input tokens are "
                        "+117%; the caching mitigation is measured on GPT-5.1. sol's 3 notes the configuration mismatch but "
                        "still credits the reduction.",
                        ["son55:E022", "son55:E023", "son55:E024", "son55:E025", "son55:E026", "sol:E008", "sol:E009"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–F (prompt figures not readable; Table values read from text); in "
                  "scope (A): non-weight playbook updated from execution feedback and reused. All eight resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (both seats)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "C03 not assigned (no category holdout); C25 partial for the LLM-delta → deterministic-merge split, the ablated "
                "core of the method.", ["son55:E005", "son55:E019", "son55:E009"], NOSCORE),
            X(p, "local:2510.04618-3", "son55", "partial",
              "Verified: reflection rounds, dedup threshold and pruning trigger swept on test-normal / FiNER test (Tables 19–21).",
              ["son55:E028"]),
            X(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
              "Verified: base agent, many-shot ICL, GEPA, DC and update ablations under one LLM.", ["son55:E011", "son55:E019"]),
            X(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
              "No contamination/overlap analysis exists; splits are not that analysis (same ruling as 2509.25140).",
              ["son55:E009", "son55:E010"]),
            X(p, "rs:adapt_via_conditioning/RE-5", "son55", "met",
              "Verified: agent, finance, medical, SQL tasks and four LLM families without per-task search.",
              ["son55:E033", "son55:E032"]),
            X(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
              "Verified: cost of the added structure reported but internally inconsistent.", ["son55:E023", "son55:E024"]),
            X(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
              "Verified: DC/GEPA/MIPROv2 compared; other itemized memories not run.", ["son55:E034"]),
            X(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
              "Verified: execution/GT signals ground lessons; without reliable feedback finance degrades (sol recorded the same "
              "partial in its H01 checks).", ["son55:E016", "son55:E017", "sol:E005"]),
            X(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
              "No test or quality filter decides which entries survive; dedup removes redundancy, not bad entries; harmful "
              "reflections enter (Table 17). The metadata filter is described as a capability, not shown.",
              ["son55:E020", "son55:E006", "sol:E011"]),
            RS(p, "E.cost", "son55", 2, "See ratings.E.cost: headline rollout reduction contradicted by Table 12.",
               ["son55:E024", "sol:E009"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.causality.reason",
             "sol_value": "3 — strong alternatives; no matched content length/query budget (C1 notes some online rows use warmup)",
             "son55_value": "3 — same-LLM baselines and ablations; not rollout-matched",
             "final_value": "3 (unchanged) with added defect: Table 1 online ACE is the offline-warmed variant; the DC margin "
                            "falls from +7.6 to +4.2 without warmup",
             "correction": "son55 missed the warmup; sol noticed it in a claim note but did not carry it into the rating reason.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none"},
            {"field_path": "ratings.E.statistics.reason",
             "sol_value": "1 — no seed/order CI", "son55_value": "1 — single run per cell",
             "final_value": "1 (unchanged) with added evidence: nominally identical offline 5-round configurations differ by 3.6 "
                            "TGC (Table 19 vs Table 1)",
             "correction": "Both seats missed this internal sign of unreported variance or config drift.",
             "evidence_ids": ["opus:O04"], "score_impact": "none"},
            {"field_path": "expectations[local:2510.04618-1/-2]",
             "sol_value": "local-1 cost partial; local-2 statistics unmet",
             "son55_value": "local-1 statistics partial; local-2 cost unmet",
             "final_value": "local-1 = cost partial; local-2 = statistics unmet",
             "correction": "A4 hidden collision (same IDs, swapped questions, equal statuses so not flagged); son55 renumbered.",
             "evidence_ids": ["son55:E024", "sol:E009"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all sections and appendices first: in scope; offline train→test; strong "
                                                   "baselines and ablations; online headline = warmup row; rollout claim "
                                                   "contradicted by A.3; HPs swept on test; single runs; initial bands G3 M3 X3 "
                                                   "Em3 Ec2–3 Eh3 Es1 Ecost1–2.",
            "integrity_checks": "Both seats a1 on 2510.04618v3, material sha 8f96bd03…; hashes equal conflicts.json; C25⊂dd valid.",
            "core_claim_check": "Matched Table 1 online row to Table 3 warmup row; recomputed DC margins; confirmed 357 vs 2,075 "
                                "rollouts and A.3's 1-epoch/1-round setting; Table 19 vs Table 1 gap.",
            "seat_flag_checked": "son55's E.cost flag (Table 4a vs Table 12) verified in the pinned text.",
            "rating_agreement": "7/8 identical and re-checked (E.causality, E.statistics kept with added evidence); E.cost → son55.",
            "expectation_renumbering": "son55 local-1 ↔ local-2 swapped to match sol's questions (A4).",
        },
    }

    # =========================================================== 2510.08191 Training-Free GRPO (Δ6.25)
    p = "2510.08191"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "significantly improves out-of-domain performance.", "Abstract",
                    "Headline scope claim: DAPO-Math → AIME is labelled out-of-domain though both are competition math."),
            opus_ev(p, "O02", "our approach fully preserves the generalization power", "§1 Contributions (Superior Generalization)",
                    "Generalization claim is supported only by Table 6, which plugs separate domain libraries into a 671B base "
                    "and compares with 32B RL models — no single-library cross-domain transfer, no same-base comparison."),
            opus_ev(p, "O03", "We run the learning process for 3 epochs with a single batch per epoch", "§3.1 Setup",
                    "The 3-step protocol is stated a priori, while Fig. 4 tracks AIME Mean@32 at each step; no stopping rule "
                    "independent of AIME is given."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats adapt_via_conditioning. C03 not assigned under the run convention: training (DAPO-100, "
                      "AFM-100) and testing (AIME, WebWalkerQA) are same-category, and cross-domain use swaps libraries rather "
                      "than holding a category out; the count-matched directly generated experiences are a simpler-"
                      "conditioning control but do not supply the holdout. The GRPO framing is an analogy, not a manufactured "
                      "training signal (GT rewards; nothing trained), so no supporting card.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                        dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2510.08191-2"): "local:2510.08191-1",
                    ("son55", "local:2510.08191-3"): "local:2510.08191-2",
                    ("son55", "local:2510.08191-1"): "local:2510.08191-3"},
            overrides={
                "local:2510.08191-4": {
                    "status": "unmet",
                    "reason": "Opus final: AIME is evaluated at every learning step (Fig. 4) and no stopping criterion "
                              "independent of AIME is stated; after a complete search this is an unmet requirement, not "
                              "unknown."},
                "local:2510.08191-3": {
                    "reason": "son55 local-1 renumbered (A4 collision). RL baselines use different, smaller bases; no GRPO on the "
                              "same DeepSeek base."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C4", ["opus:O01", "opus:O02"]), "C1", ["opus:O03"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "A 48-item library learned on 100 separate training samples is frozen and improves different "
                                   "test benchmarks, beating a count-matched unoptimised library. Not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "A 3-step, 100-sample, ~$18 group-relative reflection loop builds a short experience "
                                         "library that raises a frozen DeepSeek-V3.1-Terminus by +2.7/+5.4 Mean@32 (AIME24/25, "
                                         "ReAct+CI) and +4.6 pass@1 (WebWalkerQA), beating count-matched unoptimised experiences, "
                                         "no-GT and group-size-1 variants on AIME; superiority over RL fine-tuning and cross-"
                                         "domain generalization are confounded by base model and untested. Single learning run.",
            "unresolved": ["Same-base GRPO comparison.", "Variance across learning runs/training draws.",
                           "DAPO/AIME overlap and the stopping rule.", "WebWalkerQA judge and test size."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The cost/data problem of parametric agentic RL is real, but the "
                   "stated novelty is the 'no weight update' premise (H00 F1), and cross-sample experience libraries are "
                   "separated only verbally (Agent KB) or not discussed.",
                   ["son55:E001", "son55:E024", "son55:E025", "sol:E001"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Group contrast → text advantage → library edit is reconstructable "
                   "and its group/GT predictions are tested, but the method's own justification — equivalence to GRPO "
                   "advantages and a KL-like stability from the frozen prior — is analogy, and the anti-overfitting advantage "
                   "over parametric RL is asserted.",
                   ["son55:E002", "son55:E004", "son55:E006", "son55:E011", "sol:E015"]),
            "X": R("resolved", 3, "Opus sides with sol. The full math prompts (summary, group comparison, library-edit with "
                   "≤32-word, merge/delete rules; App. B), ops, epochs, batch, group sizes and temperatures are given, so the "
                   "chain from rollouts to retained library is reconstructable. Missing: a validation gate or rollback on "
                   "edits, a stopping rule (opus:O03), web prompts/reward implementation. This matches ACE's X=3 in this batch "
                   "(reconstructable maintenance, no acceptance gate).",
                   ["sol:E002", "sol:E013", "sol:E014", "son55:E005", "son55:E008", "opus:O03"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. AIME answer matching with Mean@32 is trustworthy; the "
                               "learning reward/verifier, the WebWalkerQA judge and test size are unstated, and web ablations "
                               "use 51 items.", ["son55:E009", "son55:E014", "sol:E004"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Count-matched generated experiences, no-GT and G=1 "
                             "controls on AIME are useful (G=1 also changes rollout budget); headline superiority over RL-"
                             "trained 32B models is confounded by base model (untrained 671B ReAct already 80.0/67.9); no same-"
                             "base GRPO or other training-free memory baseline; web ablations differ by 1–2 items.",
                             ["son55:E011", "son55:E012", "son55:E015", "son55:E018", "son55:E019", "sol:E007"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. The train/test datasets are separate (a clean split for the "
                           "math and web results), but the central scope claims go beyond it: 'out-of-domain' is same-category "
                           "math (opus:O01), the generalization claim rests on swapping libraries across different bases "
                           "(opus:O02), AIME is tracked at each step without an independent stopping rule (opus:O03), and DAPO–"
                           "AIME overlap is unexamined. sol's 3 credits the split without the claim-scope part of this item.",
                           ["son55:E007", "son55:E021", "son55:E026", "sol:E005", "sol:E010", "opus:O01", "opus:O02",
                            "opus:O03"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 rung 1). Mean@32 averages decoding noise and the QwQ "
                              "negative is reported, but each variant is one learned library from one 100-sample draw with no "
                              "intervals; 30-item AIME.", ["son55:E009", "son55:E028", "sol:E009"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Learning tokens (38M/6.6M), hours and dollars and per-problem "
                        "inference tokens/dollars are reported, with the higher per-query inference cost than a dedicated 32B "
                        "disclosed; gaps (no per-role breakdown, web cost, failed trials, cross-model $10k comparison) keep it "
                        "below 4. Not 2: unlike ACE there is no internal contradiction and the downside is disclosed.",
                        ["son55:E022", "son55:E023", "sol:E011", "sol:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–C (Fig. 4 curve values not in text); in scope (A/B): non-weight "
                  "experience library edited from grouped rollouts and reused frozen on later tasks. All eight resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (both seats)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "C03 not assigned under the run convention (no category holdout).", ["son55:E007", "son55:E021"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "H00's tactical pattern names contrasting 'winners against losers inside one sampled group' — the method's "
                "semantic advantage; H01 covers the add/delete/modify library edits. Both apply.",
                ["son55:E003", "son55:E005"], NOSCORE),
            X(p, "local:2510.08191-2", "revised", "local-2 = cost → partial; son55 local-2 (statistics) mapped to local-1 → unmet",
              "A4 collision: son55 shifted IDs (local-1 GRPO baseline, local-2 statistics, local-3 cost). Renumbered to sol's "
              "questions; cost partial (both seats), statistics unmet (both seats).", ["sol:E011", "son55:E022", "son55:E009"]),
            X(p, "local:2510.08191-3", "revised", "local-3 = same-base GRPO question (son55 local-1) → unmet",
              "son55's local-3 (cost, partial) is merged into local-2; local-3 now carries son55's same-base GRPO question.",
              ["son55:E019"]),
            X(p, "local:2510.08191-4", "revised", "unmet",
              "Stopping rule not stated while AIME is tracked per step; searched absence → unmet.", ["son55:E026", "opus:O03"]),
            X(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
              "Verified: ReAct, count-matched generated experiences, no-GT and G=1 controls.", ["son55:E011", "son55:E012"]),
            X(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
              "No overlap analysis (same ruling as 2509.25140, 2510.04618).", ["son55:E007"]),
            X(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
              "Verified: math and web with separate libraries; four bases.", ["son55:E021"]),
            X(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
              "Verified: no-GT and weak-model results; no library-size or sample-draw sensitivity.", ["son55:E013", "son55:E017"]),
            X(p, "rsi:abstract_experience_into_guidance/F1", "son55", "unmet",
              "Failure present: the research question is 'can we improve without parameters', the parent premise.",
              ["son55:E001"]),
            X(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
              "Verified: GT rewards ground the comparison; no-GT variant gains little.", ["son55:E011", "son55:E013"]),
            X(p, "rsi:abstract_experience_into_guidance/S4", "sol", "met",
              "Verified: delete/modify/merge with ≤32-word items keep a 48-item library (son55 judged partial for lack of a "
              "size bound inside H01; the S4 condition is met by explicit consolidation and deletion).",
              ["sol:E013", "son55:E027"]),
            X(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
              "The optimiser explicitly deletes/modifies low-quality entries from GT-grounded advantages each batch (a judge-"
              "controlled, unversioned merge), so partial; ACE in this batch is unmet because nothing removes entries on "
              "quality.", ["sol:E002", "son55:E005"]),
            RS(p, "X", "sol", 3, "See ratings.X: full prompts and ops reconstructable; no gate/rollback/stopping rule.",
               ["sol:E013", "opus:O03"], "+5.0 vs son55 (20×1/4)"),
            RS(p, "E.holdout", "son55", 2, "See ratings.E.holdout: clean split but scope claims exceed it.",
               ["opus:O01", "opus:O02", "son55:E026"], "−2.5 vs sol (10×1/4)"),
            RS(p, "E.cost", "son55", 3, "See ratings.E.cost: concrete learning and inference costs, downside disclosed.",
               ["son55:E022", "son55:E023"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2510.08191-1]",
             "sol_value": "local-1 statistics unmet", "son55_value": "local-1 same-base GRPO unmet",
             "final_value": "local-1 = statistics unmet (son55 local-2 merged); son55 local-1 → local-3",
             "correction": "A4 hidden collision (equal statuses, different questions; not flagged mechanically).",
             "evidence_ids": ["son55:E009", "sol:E004"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all sections and appendices first: in scope; separate train/test datasets; "
                                                   "count-matched and ablation controls; RL comparisons confounded by base; "
                                                   "generalization claim untested; single learning run; initial bands G2 M3 X3 "
                                                   "Em3 Ec2 Eh2–3 Es1 Ecost2–3.",
            "integrity_checks": "Both seats a1 on 2510.08191v1, material sha 8e3cddf9…; hashes equal conflicts.json.",
            "core_claim_check": "Re-read Tables 1–6, §4.2 costs, App. B prompts; checked web ablation n=51 arithmetic.",
            "rating_agreement": "5/8 identical and re-checked (M and E.measurement kept at the seats' 2 after weighing my initial 3: "
                                "GRPO/KL analogy and unstated web judge); X → sol; E.holdout, E.cost → son55.",
            "expectation_renumbering": "son55 local-2→1, local-3→2, local-1→3.",
        },
    }
    return S


def batch_notes():
    return [
        "2509.24771 LatentEvolve (Δ11.25): in scope as a mixed buffer+weaver system; final 47.5 between seats. New: the only "
        "quantified ablation is at L′=30 on an unnamed backbone (headline config L′=15); weaver output plus momentum offset "
        "unexplained. RS primary → son55 (C08).",
        "2509.25140 ReasoningBank (Δ7.5): final 61.25 (son55). New: §4.4 text–number contradiction and C.3 label mismatch in the "
        "MaTTS synergy evidence (no score change).",
        "2509.26100 AgenticEval (Δ3.75): evaluation_resource, evidence_level task; final 43.75 (son55). RS → decompose_and_"
        "delegate with sub null (neither C25 nor controlled_diagnostic_design fits well). New: w/o-Refine 'static audit' 48.60 "
        "≠ initial static round 72.50.",
        "2510.04618 ACE (Δ1.25): final 71.25 (son55). son55's 357 vs 2,075 rollout contradiction verified (E.cost 2). New: "
        "Table 1 online ACE is the offline-warmed variant (DC margin +7.6 → +4.2 without warmup); Table 19 vs Table 1 offline gap.",
        "2510.08191 Training-Free GRPO (Δ6.25): final 55.0 (X→sol 3; E.holdout→son55 2 on claim scope; E.cost→son55 3).",
        "Consistency rules applied within the batch: C03 only with a category-level holdout (kept for ReasoningBank, dropped for "
        "LatentEvolve/ACE/TF-GRPO); RE-2 overlap/contamination = unmet whenever no overlap analysis exists; searched absences "
        "recorded as unmet, not unknown.",
        "A4 hidden collisions (same local IDs, swapped questions) renumbered for 2509.24771, 2509.25140, 2509.26100, "
        "2510.04618, 2510.08191.",
        "Figures: no page renders required for any final rating. Optional (would only refine unresolved notes): 2509.24771 "
        "Fig. 4 (ablation backbone, MATH bars); 2509.26100 Figs. 3–4 (iteration curves, jailbreak-baseline bars).",
        "No requests for new material.",
    ]
