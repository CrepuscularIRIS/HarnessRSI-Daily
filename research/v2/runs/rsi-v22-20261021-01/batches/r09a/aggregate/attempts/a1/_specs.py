"""Opus rulings for r09a a1 (data only; consumed by _build.py)."""
import copy


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, dec, final, reason, ev=()):
        s_val, n_val = conflict(p, f"expectations[{eid}].status")
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

    def keep(s, p, k, note):
        r = prefix(copy.deepcopy(seat(s, p)["ratings"][k]), s)
        r["reason"] = note + " " + r["reason"]
        return r

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
                return claims
        raise KeyError(cid)

    def pm_sub(s, p, sub):
        out = prefix(copy.deepcopy(seat(s, p)["pattern_mapping"]), s)
        for m in out:
            m["rs_sub"] = sub
        return out

    # =========================================================== 2511.06449 FLEX (Δ13.75)
    p = "2511.06449"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "evolves a persistent experience library that continuously aggregates cross-task experiences",
                    "§1 Introduction, property (i)",
                    "The distinguishing claim is cross-task aggregation; every reported library is built and tested within "
                    "one benchmark (opus:O02), so this claim has no held-out test."),
            opus_ev(p, "O02", "The library structure is adapted to the benchmark: hierarchical for AIME25 and USPTO50k, and "
                    "non-hierarchical for GSM8k and ProteinGym.", "§4.1 Compared Methods",
                    "Per-benchmark library schema chosen without a stated rule; libraries are per task."),
            opus_ev(p, "O03", "the training was conducted on 49 historical problems from AIME83 to AIME24",
                    "§4.1 Training Configurations", "Temporal split for AIME; GSM8k/USPTO use train vs test splits."),
            opus_ev(p, "O04", "This process continues until the actor produces a correct or sufficiently improved reasoning "
                    "trajectory, or a predefined iteration limit is reached.", "§3.1 Iterative Refinement",
                    "Iteration limit (and parallel sample count) never given."),
            opus_ev(p, "O05", "If semantically similar entries are found, the agent performs a selective merge, preserving the "
                    "more informative or higher-quality trajectory while minimizing redundancy.", "§3.2 Experience Update",
                    "Merge/admission is an LLM judgment with no stated criterion, bound or retirement rule."),
            opus_ev(p, "O06", "as the experience library grows from 1,001 to 1,904 items", "§4.3 Training Accuracy Scaling",
                    "The library grows monotonically over five epochs; no forgetting or size bound."),
            opus_ev(p, "O07", "exhibits consistent improvement from 81.3% to 83.3%, significantly surpassing the 80.8% baseline",
                    "§4.3 Generalization Scaling",
                    "GSM8k test accuracy is tracked per epoch; 'significantly' is unbacked by any test; +2.5 points over "
                    "vanilla at the final epoch."),
            opus_ev(p, "O08", "less than 100$", "Figure 1 caption",
                    "The only cost statement: one aggregate bound, no breakdown and no matched-budget baseline."),
            opus_ev(p, "O09", "the agent can dynamically query the library during reasoning", "§3.2 Experience Retrieval",
                    "Retrieval is an agent-invoked tool call during reasoning (H05-type access policy)."),
            opus_ev(p, "O10", "denotes the optimization direction for improving the experience library", "§2.1 Definition 2",
                    "The library update is cast as a gradient analogue (F3: store as stand-in optimizer) with no weight-"
                    "based comparison run."),
            opus_ev(p, "O11", "which serves both as the source for experience extraction and as the evaluation dataset",
                    "Appendix 8.1 Benchmark",
                    "ProteinGym split is 100 sequences vs the rest of the same protein — held out, but within-protein, "
                    "not the 'out-of-distribution' the text calls it."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning primary. Final sub = C03 (son55): retrieved, ground-truth-derived "
                      "experience entries condition a frozen model as a first-class input — the C03 skip-upstream / "
                      "retrieved-reference branch, which is the run convention for retrieval memories (r07a ArcMemo, r08a "
                      "AAS); fit partial (no category holdout, no overlap audit).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": False,
        },
        "domain_pattern": {
            "namespace": "rsi", "unassigned": False, "revision_proposals": [],
            "reason": "Union: H01 (both seats; updater discard/merge/insert edit policy over a growing store) plus H05 "
                      "(sol; retrieval is an agent-invoked tool during reasoning, opus:O09) as a supporting access-policy "
                      "match. H00 contrastive reflection also resembles the critic loop but one entry per parent card.",
            "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H01"),
                        dmatch("sol", p, "index_experience_for_reuse", "H05",
                               fit="medium (supporting access-policy operation only)")],
        },
        "pattern_mapping": pm_sub("sol", p, "C03"),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2511.06449-3"): "local:2511.06449-1",
                    ("son55", "local:2511.06449-4"): "local:2511.06449-3",
                    ("son55", "local:2511.06449-2"): "local:2511.06449-4",
                    ("son55", "local:2511.06449-5"): "local:2511.06449-2",
                    ("son55", "local:2511.06449-1"): "local:2511.06449-7"},
            overrides={
                "local:2511.06449-2": {"status": "unmet", "score_item": "E.causality",
                                       "reason": "Opus final (sol local-2 + son55 local-5, same question: is FLEX compared "
                                                 "with an alternative abstraction/library scheme or a budget-matched "
                                                 "competitor?). None is run; the ProteinGym exploration/evolution ablation "
                                                 "(Table 3) splits FLEX's own levers and is not an alternative scheme."},
                "local:2511.06449-3": {"status": "unmet", "score_item": "E.statistics",
                                       "reason": "Opus final (sol local-3 + son55 local-4). Sample sizes are stated but "
                                                 "no seed, run, ordering or interval for any headline number; AIME25 n=30 "
                                                 "so one item = 3.3 points; 'significantly' unbacked (opus:O07)."},
                "local:2511.06449-4": {"status": "partial", "score_item": "E.cost",
                                       "reason": "Opus final (sol local-4 + son55 local-2, same cost question). One "
                                                 "aggregate bound (opus:O08) is reported, so not wholly absent; no "
                                                 "breakdown and no best-of-N / equal-budget comparison to the "
                                                 "rejection-sampling + critic exploration."},
                "rsi:abstract_experience_into_guidance/S2": {
                    "status": "partial",
                    "reason": "Opus final (son55). Golden/warning zones and critic diagnosis of failed trajectories exist, "
                              "but the distillation step is failure diagnosis, not an explicit success-vs-failure contrast, "
                              "and contrast is never ablated."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained', re-checked: the library is built on train splits (AIME83–24, "
                                   "GSM8k/USPTO train, 100 sequences per protein) and read at test on disjoint items "
                                   "(opus:O03, O11), with a no-library ReAct control. Not improver: the updater itself is "
                                   "never changed or compared.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + seat("son55", p)["assessment"]["unresolved"],
        },
        "ratings": {
            "G": keep("sol", p, "G", "Both seats 2; re-checked (neighbours dismissed in one line each; no residual shown)."),
            "M": keep("sol", p, "M", "Both seats 2; re-checked (Corollary 1 'guarantees' is circular; mechanism "
                                     "reconstructable)."),
            "X": R("resolved", 2, "Opus sides with son55. The chain explore → critic → updater → tool retrieval is "
                   "described, but the conditions that decide retention are not: no iteration limit or sample count "
                   "(opus:O04), merge/admission by an unstated LLM criterion (opus:O05), monotone growth with no bound or "
                   "retirement (opus:O06), per-benchmark schema with no rule (opus:O02). That is anchor 2 ('main steps "
                   "described, retention or key conditions unclear'); sol's own reason lists the same gaps.",
                   ["opus:O02", "opus:O04", "opus:O05", "opus:O06", "son55:E004", "son55:E005", "sol:E03"]),
            "E.measurement": R("resolved", 3, "Opus sides with sol. Under A2 this item judges the instrument only: "
                               "exact-answer accuracy on AIME25/GSM8k, USPTO50k exact match and ProteinGym Spearman are "
                               "standard and verifiable, and the text reconciles with the tables (Table 2 own-library "
                               "cells equal Table 1 FLEX). Not 4: USPTO equivalence rule not stated. son55's grounds belong "
                               "elsewhere — small n → E.statistics, AIME25 contamination → E.holdout, unspecified ICL → "
                               "E.causality.", ["sol:E07", "sol:E10", "son55:E008", "son55:E010"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. Same-backbone LLM / ICL / ReAct (no library) controls "
                             "on four benchmarks and 10+ models, the ProteinGym exploration × evolution factorial, and "
                             "the cross-model library swap (Table 2) give real partial attribution to the library. Still "
                             "missing: an alternative abstraction/library scheme, budget-matched best-of-N, and component "
                             "ablations outside ProteinGym. That is anchor 2; 1 would understate the store-off evidence "
                             "on every benchmark.",
                             ["sol:E07", "sol:E11", "sol:E12", "son55:E013", "son55:E014", "son55:E016"],
                             ["son55:E021"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. Construction and test are disjoint on all four "
                           "benchmarks (opus:O03, O11), which keeps this at 2. Not 3: the distinguishing claim is cross-"
                           "task aggregation (opus:O01), yet every library is built and tested inside one benchmark "
                           "(opus:O02); ProteinGym 'OOD' is a within-protein random split (opus:O11); GSM8k test accuracy "
                           "is tracked each epoch with no stated stopping rule (opus:O07); no overlap/contamination audit.",
                           ["opus:O01", "opus:O02", "opus:O07", "opus:O11", "son55:E009", "son55:E012", "son55:E020"]),
            "E.statistics": keep("sol", p, "E.statistics", "Both seats 1; re-checked (A2 ladder: counts, no uncertainty)."),
            "E.cost": keep("sol", p, "E.cost", "Both seats 1; re-checked (one '<$100' bound, opus:O08)."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendix 8 read; in scope (system_method): a non-weight experience "
                  "library built on training data and read at test by frozen LLMs. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", "C03"]],
                "C03 is the only child of adapt_via_conditioning and the run convention for retrieval memories; sol's "
                "'main-level only' leaves an applicable child unassigned.", ["son55:E006", "son55:E007"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H01"], ["index_experience_for_reuse", "H05"]],
                "H05 adds a distinct supporting operation: retrieval is a tool the agent calls during reasoning "
                "(opus:O09), not a fixed pre-task injection.", ["opus:O09", "sol:E05"], NOSCORE),
            X(p, "local:2511.06449-2", "revised",
              "local-2 = alternative-scheme / budget-matched competitor control → unmet; son55's local-2 (equal-budget "
              "best-of-N, a cost question) renumbered to local-4",
              "A4 collision: sol local-2 (competitor controls, E.causality) and son55 local-2 (equal-budget best-of-N, "
              "E.cost) are different questions. son55 local-5 asks sol's local-2 question → merged; nothing of that kind "
              "is run, so sol's 'partial' (credited the ProteinGym internal ablation) is revised to unmet.",
              ["sol:E11", "son55:E016"]),
            X(p, "local:2511.06449-4", "revised",
              "local-4 = cost question → partial (sol local-4 + son55 local-2); son55's local-4 (uncertainty) merged into "
              "local-3 → unmet",
              "A4 collision: sol local-4 is cost, son55 local-4 is statistics. Cost: a single aggregate bound exists "
              "(opus:O08), no matched budget → partial. Statistics: no uncertainty at all → unmet, which also revises "
              "sol's local-3 'partial' (sample sizes alone do not answer an uncertainty question).",
              ["opus:O08", "opus:O07", "son55:E011"]),
            X(p, "local:2511.06449-6", "son55", "partial",
              "Only son55 asked whether the cross-task / cross-agent transfer claim is tested. Cross-model inheritance is "
              "tested on held-out items (Table 2); cross-task is not (opus:O01, O02) → partial.",
              ["opus:O01", "opus:O02", "son55:E020"]),
            X(p, "rsi:abstract_experience_into_guidance/F3", "son55", "unmet",
              "Definition 2 casts the library update as the gradient analogue (opus:O10) and the paper claims parity with "
              "parameter-based learning, but no weight-based baseline is run — the card's F3 failure mode is present. sol "
              "noted the theory overreach under local-5 but did not file F3.", ["opus:O10", "sol:E14"]),
            X(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
              "Golden/warning partition exists, but distillation is failure diagnosis rather than an explicit "
              "success-vs-failure contrast, and it is never ablated.", ["sol:E02", "son55:E006"]),
            X(p, "rsi:index_experience_for_reuse/S4", "sol", "partial",
              "Kept with the H05 match: top-k=5 hierarchical tool retrieval is capped, but trigger reliability and "
              "always/never retrieval are not tested.", ["opus:O09", "sol:E05"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "Retention conditions (iteration limit, admission/merge criterion, bound, schema rule) are unspecified; "
                "anchor 2.", ["opus:O02", "opus:O04", "opus:O05", "opus:O06"], "-5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", {"status": "resolved", "rating": 3},
                "Instruments are standard and verifiable; son55's grounds are other items' defects under A2.",
                ["sol:E07", "sol:E10"], "+2.5 vs son55 (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", {"status": "resolved", "rating": 2},
                "Store-off on every benchmark + one factorial + cross-model swap = anchor 2; no alternative scheme or "
                "equal budget keeps it below 3.", ["sol:E07", "sol:E11", "son55:E013"], "+3.75 vs son55 (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 2},
                "Disjoint splits support 2; the cross-task claim is untested, ProteinGym is within-protein and GSM8k "
                "test is tracked per epoch, so not 3.", ["opus:O01", "opus:O02", "opus:O07", "opus:O11"],
                "-2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–7 and Appendix 8 before opening seats: train-built library "
                                                   "read at test with clean AIME/GSM8k splits; controls only LLM/ICL/"
                                                   "ReAct; one component ablation (ProteinGym); single runs; '<$100' only "
                                                   "cost; cross-task claim untested. Expected X 2, E.causality 2, "
                                                   "E.holdout 2, statistics/cost 1.",
            "integrity_checks": "Both seats a1 on 2511.06449v2, material sha 764ec262…; canonical seat hashes equal "
                                "conflicts.json; both completed RS + domain identification.",
            "core_claim_check": "Scoped: held-out within-benchmark gains and cross-model library transfer are supported "
                                "as author reports; 'scaling law', 'continuous' and cross-task evolution are not.",
            "rating_agreement": "G 2, M 2, E.statistics 1, E.cost 1 agree and were re-checked.",
            "material_request": "Non-blocking: pinned ACE / ReasoningBank / AgentKB / Memento originals would let G check "
                                "the one-line neighbour dismissals; no rating here depends on them (both seats and Opus "
                                "already rate G 2 from the paper's own positioning).",
        },
    }

    # =========================================================== 2511.07317 RLVE (both out_of_scope)
    p = "2511.07317"
    a3 = ("out_of_scope (rubric A3 bullet 1; both seats, independently re-checked). RLVE keeps a per-environment "
          "difficulty window that rises when the policy's accuracy passes a threshold (opus:O02), but that window only "
          "controls which problems are generated as RL training data; the 400 environments are hand-engineered and fixed "
          "(opus:O03); and every result is a trained checkpoint evaluated on held-out environments or reasoning benchmarks "
          "(opus:O04). The improver's update target and evaluated product are weights — same ruling as r08a ASL / r02a "
          "WebRL (curriculum or training data for weights). Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "enables each verifiable environment to dynamically adapt its problem difficulty distribution "
                    "to the policy model’s capabilities as training progresses", "Abstract",
                    "Adaptation is of the training-problem distribution, during training."),
            opus_ev(p, "O02", "maintains a difficulty range", "§2.2",
                    "The only adaptive state: a scalar range per environment, raised on accuracy ≥ 90%."),
            opus_ev(p, "O03", "manually engineering all 400 environments", "§6",
                    "Environments are human-built, not produced from execution feedback."),
            opus_ev(p, "O04", "and evaluate checkpoints on", "§4.2", "Evaluated object = trained weights."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("sol", p)["rs_pattern"]), "sol"),
        "domain_pattern": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]), "sol"),
        "pattern_mapping": [],
        "expectations": lambda sol, son: [],
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "convention r05b/r06a/r07a/r08a).",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; RL gains are author-reported checkpoint "
                                             "results.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently re-checked and confirmed)",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "Run convention: out_of_scope rows carry evidence_level null — the task/retained/improver ladder grades "
                "harness changes and does not apply to a weight-level paper.", ["opus:O04"], "none (not scored)"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.claim_support", "sol_value": "unresolved", "son55_value": "unresolved",
             "final_value": None,
             "correction": "Run convention (r08a ASL): claim support is not assessed for excluded rows; null, not "
                           "'unresolved'.", "evidence_ids": ["opus:O04"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §2–5, §6–7 before seats: adaptive difficulty is a "
                                                   "training curriculum over hand-built environments; all results are "
                                                   "checkpoints → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2511.07317v2, material sha b44c6710…; seat hashes equal conflicts.json; "
                                "both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O04. son55's boundary question (can a transient "
                                "difficulty controller count as a harness component?) — no: it is never retained beyond "
                                "the run nor read by a deployed agent.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2511.07800 Trainable graph memory (Δ2.5)
    p = "2511.07800"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "From the HotpotQA training set, we sample 1,000 examples to construct the memory and an "
                    "additional 5,000 examples for weight training.", "Appendix A.2",
                    "Construction and utility training use disjoint HotpotQA train subsets; RL uses the rest."),
            opus_ev(p, "O02", "0.279 (–) 0.298 0.581 0.157 0.268 0.281 0.077 0.290", "Table 1, Qwen3-4B ITR row",
                    "Tool-integrated baseline PopQA = 0.157 …"),
            opus_ev(p, "O03", "0.211 (↓24.4%) 0.158 0.413 0.157 0.183 0.240 0.033 0.290",
                    "Table 1, Qwen3-4B Direct Inference row",
                    "… identical to the no-retrieval row (PopQA 0.157, Bamboogle 0.290), while every memory method is "
                    "≈0.38–0.39 on PopQA and 8B ITR is 0.358 (opus:O04). The 4B baseline cell looks like a copy error; it "
                    "supplies about half of the headline +25.8% relative gain."),
            opus_ev(p, "O04", "0.334 (–) 0.275 0.593 0.358 0.325 0.324 0.094 0.365", "Table 1, Qwen3-8B ITR row",
                    "8B ITR PopQA 0.358, for comparison."),
            opus_ev(p, "O05", "However, these methods typically apply graph structure in a static manner and lack "
                    "mechanisms to assess or refine the utility of memory components.", "§2.2",
                    "The stated residual: no utility assessment in prior memory."),
            opus_ev(p, "O06", "demonstrates how hierarchical graph-based memory can evolve by assimilating new "
                    "collaborative trajectories", "§2.2",
                    "Right after the 'static' claim the paper concedes an evolving graph memory (G-Memory) without "
                    "contrasting its mechanism."),
            opus_ev(p, "O07", "offers the best balance between guidance and prompt efficiency", "§5.4",
                    "Main text: k=3 is the best balance …"),
            opus_ev(p, "O08", "The best overall result is achieved at top_k=5", "Appendix C.1",
                    "… appendix: k=5 is best (Table 3 Avg .355 > .351); k is read off the seven test sets."),
            opus_ev(p, "O09", "All experiments are conducted on a cluster of 8 NVIDIA A100 GPUs.", "Appendix A.2",
                    "The only resource statement; no calls, tokens, time or dollars for GPT-4o construction, the "
                    "5,000 paired utility rollouts, or RL."),
            opus_ev(p, "O10", "we keep all memory edges at uniform weight and retrieve strategies purely based on "
                    "structural presence", "§5.4", "Weight-off ablation is defined; its magnitude is in Figure 4 only."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning primary. Final sub = C03 (son55, run convention for retrieval "
                      "memories): retrieved strategy nodes condition the frozen executor; fit medium because the selector "
                      "is utility-trained.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi", "unassigned": False, "revision_proposals": [],
            "reason": "Final = sol's set. Within abstract_experience_into_guidance the more apt child is H00 (meta-"
                      "cognition induced by contrasting success and failure FSM paths of the same query) rather than H01 "
                      "(the create/update/skip editor is secondary); H29 both seats (guided-minus-unguided utility "
                      "credit); H28 kept at medium (Stage 3 trains the policy on memory-augmented prompts).",
            "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                        dmatch("son55", p, "evidence_gated_retention", "H29"),
                        dmatch("sol", p, "couple_context_and_weight_updates", "H28")],
        },
        "pattern_mapping": pm_sub("sol", p, "C03"),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "rs:adapt_via_conditioning/RE-01"): "rs:adapt_via_conditioning/RE-1",
                    ("sol", "rs:adapt_via_conditioning/RE-02"): "rs:adapt_via_conditioning/RE-2",
                    ("sol", "rs:adapt_via_conditioning/RE-03"): "rs:adapt_via_conditioning/RE-3",
                    ("son55", "local:2511.07800-4"): "local:2511.07800-3",
                    ("son55", "local:2511.07800-1"): "local:2511.07800-6",
                    ("son55", "local:2511.07800-2"): "local:2511.07800-7",
                    ("son55", "local:2511.07800-3"): "local:2511.07800-8"},
            overrides={
                "local:2511.07800-5": {"score_item": "E.causality",
                                       "reason": "Opus final (son55). Partly controlled: A-MEM and ExpeL are built with "
                                                 "the same GPT-4o and a Gemini-built graph gives similar averages, so "
                                                 "teacher knowledge alone is unlikely to explain the gain; strategy "
                                                 "content vs teacher is still not separated. Filed under E.causality "
                                                 "(alternative explanation) per A2, not measurement."},
                "rsi:abstract_experience_into_guidance/S1": {
                    "status": "partial",
                    "reason": "Opus final (sol). The named fixed thing (no utility assessment, opus:O05) is specific, but "
                              "the paper concedes an evolving graph memory one sentence later (opus:O06) without "
                              "contrasting it."},
                "rsi:evidence_gated_retention/S1": {
                    "status": "met",
                    "reason": "Opus final (sol). Every credit is a guided-minus-unguided reward difference (Algorithm 2); "
                              "the single-pair noise is the F4 / statistics question, not absence of a counterfactual."},
                "rsi:evidence_gated_retention/S4": {
                    "status": "met",
                    "reason": "Opus final (son55). Edge weights are a separable component and the uniform-weight "
                              "ablation is run (opus:O10); its magnitude is figure-only, which limits E, not this "
                              "design condition."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02", "opus:O03"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained', re-checked: graph built and utility-trained on HotpotQA train "
                                   "subsets (opus:O01), read at inference on HotpotQA dev + six other QA sets, with store-"
                                   "off (ITR) and three alternative memories under the same agents. Not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + seat("son55", p)["assessment"]["unresolved"]
                          + ["Qwen3-4B ITR PopQA cell equals the no-retrieval row (opus:O02–O04); the 4B relative gain "
                             "may be overstated."],
        },
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The residual is specific (no utility assessment of stored "
                   "strategies, opus:O05) and three memory baselines are run, but the gap claim is undercut in the "
                   "same paragraph by the conceded evolving graph memory (opus:O06), the harm of unscored strategies "
                   "is never measured, and utility-valued memories as a line are not positioned against. Running "
                   "baselines is E evidence; G asks whether the residual is located against the nearest neighbours — "
                   "anchor 2.", ["opus:O05", "opus:O06", "sol:E01", "son55:E003", "son55:E004"]),
            "M": keep("sol", p, "M", "Both seats 3; re-checked (counterfactual-utility REINFORCE gives a distinguishing "
                                     "prediction vs uniform weights; one-pair credit noise)."),
            "X": keep("son55", p, "X", "Both seats 2; re-checked (N, K unstated; discard absent from Algorithm 1; "
                                       "memory use at RL test time unclear)."),
            "E.measurement": R("resolved", 2, "Opus sides with son55 on the value, on a different basis. EM on standard "
                               "QA sets with a shared Wikipedia/E5 retriever is a credible instrument, but the 4B "
                               "tool-integrated baseline reports PopQA 0.157 — identical to the no-retrieval row "
                               "(opus:O02, O03) and far below every other retrieval configuration and the 8B ITR "
                               "(opus:O04) — and that cell carries about half of the headline +25.8%. A reported "
                               "baseline value that cannot be reconciled caps the instrument at 2 (run convention, "
                               "r08a MemoTime / EvoRoute). son55's own grounds (unstated test sizes, teacher leakage) "
                               "belong to E.statistics and E.causality under A2.",
                               ["opus:O02", "opus:O03", "opus:O04", "son55:E012"], ["sol:E08"]),
            "E.causality": keep("sol", p, "E.causality", "Both seats 2; re-checked (store-off, three alternative "
                                "memories with the same constructor, weight-off ablation figure-only (opus:O10); "
                                "margins over Direct Trajectory small; paired utility rollouts not budget-matched)."),
            "E.holdout": R("resolved", 3, "Opus sides with son55. Construction (1,000), utility training (5,000) and RL "
                           "(rest) are disjoint HotpotQA train subsets (opus:O01) and evaluation covers HotpotQA dev plus "
                           "six other datasets; sol's 'unclear allocation' is answered by Appendix A.2. Not 4: k is read "
                           "off the test sets (opus:O07, O08), no overlap/contamination audit, and 'model-agnostic' is "
                           "tested only by swapping the constructor.",
                           ["opus:O01", "opus:O07", "opus:O08", "son55:E010", "son55:E011", "son55:E012"]),
            "E.statistics": keep("sol", p, "E.statistics", "Both seats 1; re-checked (A2 ladder)."),
            "E.cost": R("not_reported", 0, "Opus sides with son55. The only resource line is the A100 cluster "
                        "(opus:O09); no tokens, calls, time or dollars for GPT-4o graph construction, the 5,000 paired "
                        "with/without utility rollouts, or RL, and no budget comparison with A-MEM/ExpeL. Sample sizes "
                        "and GRPO settings are configuration, not cost. Hardware-only = not_reported, run convention "
                        "r02b / r04a / r06a.", ["opus:O09", "son55:E024"],
                        scope=["full pinned v1 text: §4–5, Appendix A.1–A.2, B, C, E (tables, algorithms, prompts)"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–E read; in scope (system_method): a non-weight strategy "
                  "graph with learned retrieval utilities, built on training data and read by frozen executors at test. "
                  "All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", "C03"]],
                "Run convention for retrieval memories; C03 is the only applicable child.", ["son55:E007"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"], ["evidence_gated_retention", "H29"],
                 ["couple_context_and_weight_updates", "H28"]],
                "One child per parent: contrastive induction (H00) is the load-bearing step of this parent, the editor "
                "(H01) secondary; H28 applies at medium because GRPO trains on memory-augmented prompts.",
                ["sol:E02", "sol:E07"], NOSCORE),
            X(p, "local:2511.07800-1", "revised",
              "local-1 = k-optimum consistency → unmet (sol); son55's local-1 (store-off reported) renumbered to local-6 "
              "= met",
              "A4 collision, different questions. Verified: main text k=3 best balance (opus:O07) vs appendix k=5 best "
              "(opus:O08); ITR / Search-R1 store-off rows exist.", ["opus:O07", "opus:O08", "son55:E012"]),
            X(p, "local:2511.07800-3", "revised",
              "local-3 = statistics → unmet (sol local-3 + son55 local-4); son55's local-3 (disjoint splits) renumbered "
              "to local-8 = met",
              "A4 collision, different questions; both statistics checks are unmet; the split check is met "
              "(opus:O01).", ["opus:O01", "son55:E012"]),
            X(p, "local:2511.07800-5", "son55", "partial",
              "Teacher-confound check is real and partly controlled (same GPT-4o for A-MEM/ExpeL; Gemini swap); re-filed "
              "under E.causality per A2.", ["son55:E022", "son55:E025"]),
            X(p, "rs:adapt_via_conditioning/RE-01", "sol", "partial (renamed RE-1)",
              "A4 syntax: run convention is RE-1..RE-6. Verified: conditioning isolated by ITR and k=0, no matched "
              "multitask/no-conditioning budget control.", ["sol:E08", "sol:E12"]),
            X(p, "rs:adapt_via_conditioning/RE-02", "sol", "partial (renamed RE-2)",
              "Verified: disjoint train subsets and other datasets (opus:O01); no overlap audit.", ["opus:O01"]),
            X(p, "rs:adapt_via_conditioning/RE-03", "sol", "partial (renamed RE-3)",
              "Verified: raw trajectory / A-MEM / ExpeL are the cheaper alternatives; no flat-strategy equal-token "
              "control.", ["sol:E09"]),
            X(p, "rsi:abstract_experience_into_guidance/F4", "son55", "partial",
              "The trained quantity is a retrieval ranking over LLM-written strategies, presented as 'trainable memory'; "
              "the paper does argue it as utility-aware selection, so partial.", ["opus:O10", "son55:E008"]),
            X(p, "rsi:abstract_experience_into_guidance/S1", "sol", "partial",
              "Specific residual named (opus:O05) but undercut by the conceded evolving neighbour (opus:O06); consistent "
              "with G 2.", ["opus:O05", "opus:O06"]),
            X(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
              "EM outcome labels on HotpotQA train decide success/failure for contrast and utility.", ["son55:E005"]),
            X(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
              "Admission is an LLM create/update/skip judgment; utility only re-ranks retrieval later.",
              ["son55:E006", "son55:E020"]),
            X(p, "rsi:couple_context_and_weight_updates/H28", "sol", "partial",
              "Kept with the H28 match: policy trained on memory-augmented prompts; no repeated joint memory–policy "
              "cycle.", ["sol:E07"]),
            X(p, "rsi:evidence_gated_retention/F5", "son55", "partial",
              "Utility gates retrieval ranking; content is never demoted or removed by measured utility.",
              ["son55:E008"]),
            X(p, "rsi:evidence_gated_retention/S1", "sol", "met",
              "Counterfactual present by construction (Algorithm 2); its noise is a separate question.",
              ["sol:E05", "son55:E008"]),
            X(p, "rsi:evidence_gated_retention/S4", "son55", "met",
              "Gate separable and ablated (opus:O10); magnitude figure-only limits E, not the design condition.",
              ["opus:O10"]),
            X(p, "rsi:evidence_gated_retention/S5", "son55", "unmet",
              "Cost of the paired with/without rollouts is not stated anywhere (opus:O09).", ["opus:O09"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "Residual named but undercut by the conceded neighbour; nearest-neighbour positioning incomplete.",
                ["opus:O05", "opus:O06"], "-3.75 vs son55 (15×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "Value = son55, basis replaced: the irreconcilable 4B ITR PopQA baseline cell (opus:O02–O04); son55's "
                "listed grounds belong to other items under A2.", ["opus:O02", "opus:O03", "opus:O04"],
                "-2.5 vs sol (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 3},
                "Disjoint construction/utility/RL subsets are stated (opus:O01); k-from-test and no audit keep it below "
                "4.", ["opus:O01", "opus:O08"], "+2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "not_reported", "rating": 0},
                "Hardware line only (opus:O09) = not_reported (r02b/r04a/r06a).", ["opus:O09"], "-1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–6 and Appendices A–E before seats: retained graph read at "
                                                   "inference with strong store-off and alternative-memory controls; "
                                                   "weight-off ablation figure-only; k chosen on test; anomalous 4B ITR "
                                                   "PopQA cell; no variance, no cost.",
            "integrity_checks": "Both seats a1 on 2511.07800v1, material sha 5214761b…; seat hashes equal conflicts.json; "
                                "both completed RS + domain identification.",
            "core_claim_check": "Inference claim scoped to small single-run margins over raw-trajectory memory; 4B "
                                "relative gain likely inflated by the baseline cell; RL claim margins within noise.",
            "rating_agreement": "M 3, X 2, E.causality 2, E.statistics 1 agree and were re-checked. Shared miss: neither "
                                "seat flagged the 4B ITR PopQA cell; it is recorded under the E.measurement resolution and "
                                "as C1 counterevidence (no rating where both seats agreed changes).",
            "material_request": "Non-blocking: pinned G-Memory original would let G check the conceded neighbour.",
        },
    }

    # =========================================================== 2511.10395 AgentEvolver (scope conflict)
    p = "2511.10395"
    a3 = ("out_of_scope (rubric A3 bullet 1; Opus sides with son55 on the scope conflict). The evaluated object is the "
          "GRPO-trained policy: all main and ablation results (Tables 1–3, 5, the 'w/ RL' rows of Table 4) are trained "
          "checkpoints (opus:O01, O02), and evaluation is explicitly run without experience (opus:O03). The non-weight "
          "experience pool exists, but in this paper it is a rollout aid: retrieved experience is injected only into "
          "training rollouts and stripped before the gradient (opus:O04), the pool is a cold-start pool built from the "
          "initial policy on synthetic tasks with construction delegated to the external ReMe implementation (opus:O05, "
          "O06), and the authors present explicit (in-context) use as the inferior path that RL 'internalizes' "
          "(opus:O07). The only evaluation of the pool as an artifact read at inference is one dev-set row (Table 4 "
          "'w/o RL + exp.', opus:O08) plus Figure 13(a) — a side check on a frozen model, not the claim, and on the dev "
          "split. Self-questioning tasks and the LLM judge are training data/rewards for weights (r08a ASL, r07b "
          "2511.03773, r05b SEAgent precedent); the context templates (Table 7) are static within-episode options. This "
          "differs from r08a EvolveR / r06b LatentEvolve, whose evaluated systems read the retained store at test with a "
          "store-off arm. Flip condition: the evaluated agent reads the pool at test, or the pool is evaluated as a "
          "claimed artifact on held-out tasks with a store-off arm. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "These models serve as the agent’s policy network.", "§7.1.2",
                    "Qwen2.5-7B/14B are the policy whose weights are trained."),
            opus_ev(p, "O02", "updates the policy parameters accordingly", "§6.1 Overall Architecture",
                    "The loop's product is updated policy parameters."),
            opus_ev(p, "O03", "we report only the results without experience guidance to provide a fair assessment of the "
                    "impact of experience incorporation", "§7.1.3 Self-Navigating",
                    "The evaluated agent does not read the experience pool."),
            opus_ev(p, "O04", "prior to policy gradient computation, retrieved experience tokens are removed from the "
                    "training samples", "§4.3 Experience Stripping",
                    "Experience conditions training rollouts only; it is stripped before the update."),
            opus_ev(p, "O05", "To construct a cold-start experience pool", "§4.1 Pool Construction",
                    "Pool built once from initial-policy rollouts on synthetic p_train tasks (Eq. 13)."),
            opus_ev(p, "O06", "More implementation details can be found at", "§4.1 footnote (ReMe)",
                    "Pool construction/retrieval is delegated to an external implementation not in the material."),
            opus_ev(p, "O07", "explicit learning yields limited improvements by leveraging external experience, whereas "
                    "implicit learning internalizes experience", "§7.4.2 summary",
                    "Authors frame the in-context pool as the limited path; the contribution is RL internalization."),
            opus_ev(p, "O08", "Columns show avg@4 and best@4 on the dev set for each benchmark", "Table 4 caption",
                    "The single pool-at-inference row (w/o RL + exp.) is on the dev split."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). sol's identification kept: synthetic tasks + LLM judge + step "
                      "attribution as self-built reward/curriculum signals for RL (C26), with experience retrieved as a "
                      "conditioning input to rollouts (C03). son55's null is allowed for excluded rows; completed for "
                      "consistency with r08a ASL.",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering", fit="informational (out_of_scope)"),
                        smatch("sol", p, "adapt_via_conditioning", fit="informational (out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {
            "namespace": "rsi", "unassigned": False,
            "reason": "Informational (out_of_scope). sol's H28/H00 kept as resemblance records: experience-shaped "
                      "rollouts become RL training data (H28 tactic text) and the pool distils success/failure lessons "
                      "(H00). A3 governs scope, not the card match.",
            "matches": [dmatch("sol", p, "couple_context_and_weight_updates", "H28", fit="informational (out_of_scope)"),
                        dmatch("sol", p, "abstract_experience_into_guidance", "H00", fit="informational (out_of_scope)")],
            "revision_proposals": [
                "H28 (couple_context_and_weight_updates): the tactic 'experience-shaped rollouts become training data' "
                "admits papers whose context asset is stripped and never read at evaluation (this paper). Propose an "
                "explicit scope note: members are in Harness-RSI scope only when the evaluated system reads the context "
                "asset at test or the asset is evaluated with a store-off arm (A3 bullet 2); otherwise the row is "
                "out_of_scope and the card match is informational. Not applied (batch-internal card edits forbidden)."],
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol"),
        "expectations": lambda sol, son: [
            dict(e, origin=f"sol:{e['id']}", informational=True,
                 reason="Informational (row out_of_scope; not scored). " + e["reason"])
            for e in prefix(copy.deepcopy(sol["expectations"]), "sol")],
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "convention). The dev-set pool row would at most be 'task' (selection/dev "
                                              "split), as sol itself noted.",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; RL gains are author-reported checkpoint "
                                             "results.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong.",
                                      "Boundary recorded with flip condition (see reason) and H28 revision proposal."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "out_of_scope (scope conflict resolved for son55: evaluated object = GRPO policy weights; pool is a "
              "stripped rollout aid; only a dev-set side row reads it at inference)",
        "resolutions": [
            res("status", *C(p, "status"), "son55", "out_of_scope", a3,
                ["opus:O01", "opus:O03", "opus:O04", "opus:O05", "opus:O07", "opus:O08", "son55:E003", "son55:E004",
                 "son55:E005"],
                "sol 57.5 → not scored (null)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "Out-of-scope rows carry null (run convention).", ["opus:O03"], "none (not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Out-of-scope rows carry null, not 'unresolved' or 'scoped' (r08a ASL convention).", ["opus:O03"],
                "none (not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                "Informational identification kept (r08a ASL precedent); scope is decided by A3, not by card match.",
                ["sol:E001", "sol:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", "C03"], ["self_supervised_signal_engineering", "C26"]],
                "Informational only.", ["sol:E003", "sol:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"], ["couple_context_and_weight_updates", "H28"]],
                "Informational resemblance records; H28 revision proposal filed.", ["sol:E004", "sol:E006"], NOSCORE),
        ] + [
            res(f"expectations[{eid}].status", *C(p, f"expectations[{eid}].status"), "sol",
                f"{C(p, f'expectations[{eid}].status')[0]} (informational)",
                "Kept as informational: son55 recorded no expectations for an excluded row, which the contract allows; "
                "sol's statuses are factually consistent with the text (pool distilled from success/failure/comparative "
                "pairs with an LLM validator; Table 4 is dev; no cross-seed uncertainty) but do not score.",
                ["sol:E003", "sol:E006"], "none (not scored)")
            for eid in ("local:2511.10395-1", "rs:adapt_via_conditioning/RE-2",
                        "rs:self_supervised_signal_engineering/RE-2", "rsi:abstract_experience_into_guidance/S2",
                        "rsi:abstract_experience_into_guidance/S5", "rsi:couple_context_and_weight_updates/H28")
        ] + [
            res(f"ratings.{k}", *C(p, f"ratings.{k}"), "son55", {"status": "unknown", "rating": None},
                "Not scored: out_of_scope under A3. sol's ratings grade the RL-trained policy's results (official TGC/BFCL "
                "checks, RL ablations, training cost) — weight-level evidence this rubric does not score.",
                ["opus:O03"], "sol contribution removed (row not scored)")
            for k in KEYS
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v1 text (§1–8) before seats: every reported result is a "
                                                   "GRPO checkpoint evaluated without experience; the pool is a stripped "
                                                   "rollout aid; one dev-set inference row. Leaned out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2511.10395v1, material sha ba3c99d3…; seat hashes equal conflicts.json. "
                                "sol completed identification; son55 skipped it for an excluded row (allowed).",
            "core_claim_check": "A3 decided on the evaluated object (opus:O01–O08) against EvolveR/LatentEvolve "
                                "(in: store read at test) and SEAgent/2511.03773/ASL (out: non-weight state only feeds "
                                "weight training).",
            "rating_agreement": "No ratings retained (all unknown).",
        },
    }

    # =========================================================== 2511.12997 WebCoach (Δ5)
    p = "2511.12997"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "retrieves relevant experiences based on similarity and recency", "Abstract",
                    "Described retrieval uses recency …"),
            opus_ev(p, "O02", "Once candidate memories are retrieved, they are ranked by their similarity to the current "
                    "context embedding", "§2.2 Retrieval", "… implemented ranking is cosine similarity only."),
            opus_ev(p, "O03", "trainable LLM that decides when and how to intervene mid-episode", "§1",
                    "Coach described as trainable …"),
            opus_ev(p, "O04", "which led us to decide against DPO-based finetuning of Qwen3", "§4",
                    "… but it is used zero-shot."),
            opus_ev(p, "O05", "Qwen-VL-7B 144 16.4 0.328", "Table 1, 7B baseline row", "Main-table 7B baseline 0.328 …"),
            opus_ev(p, "O06", "0.344 221/643 144.0 16.4", "Appendix Table 2, 7B Overall",
                    "… appendix baseline 221/643 = 0.344 for the same configuration (same time/steps)."),
            opus_ev(p, "O07", "which improves from 47.3% to 61.4% success rate when equipped with WebCoach, a 14.4-point "
                    "gain", "§4 Quantitative analysis", "61.4 − 47.3 = 14.1, not 14.4."),
            opus_ev(p, "O08", "In all cases, the number of action steps per task remains flat or decreases", "§4",
                    "Contradicted by Table 1: 7B dynamic 17.4 steps vs 16.4 baseline (opus:O09)."),
            opus_ev(p, "O09", "Qwen-VL-7B 200 17.4 0.311", "Table 1, 7B dynamic row", "7B: success down, steps up."),
            opus_ev(p, "O10", "retrieval explicitly excludes any episode whose WebVoyager task ID matches that of the "
                    "current task", "§3.2 Memory Retrieval and Leakage Control",
                    "Only same-ID exclusion; sibling tasks of the evaluated stream are retrievable."),
            opus_ev(p, "O11", "each main agent iteratively updates its own trajectories into the memory store", "§4",
                    "Dynamic EMS is written from the evaluated 643-task stream."),
            opus_ev(p, "O12", "Baseline: no coaching enabled.", "§4",
                    "The only store-off arm also removes the Coach; no Coach-without-memory arm."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55"),
        "domain_pattern": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]), "son55"),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2511.12997-3"): "local:2511.12997-2",
                    ("son55", "local:2511.12997-4"): "local:2511.12997-1",
                    ("son55", "local:2511.12997-1"): "local:2511.12997-3",
                    ("son55", "local:2511.12997-2"): "local:2511.12997-4"},
            overrides={
                "local:2511.12997-1": {"status": "unmet",
                                       "reason": "Opus final (sol local-1 + son55 local-4, same question: does the "
                                                 "'consistent across backbones / flat-or-fewer steps' claim hold?). No: "
                                                 "7B success falls and steps rise (opus:O08, O09); 14.4 vs 14.1 "
                                                 "(opus:O07). 'challenged_with_evidence' is for a paper that challenges "
                                                 "an expectation with evidence, not for our contradiction of the paper."},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "unmet",
                    "reason": "Opus final (son55). The dynamic store is written from the evaluated stream (opus:O11); "
                              "same-ID exclusion (opus:O10) is a partial guard, not a construction/evaluation split."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O05", "opus:O06", "opus:O07", "opus:O12"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Opus sides with son55. EVIDENCE.md 'retained' needs the retained change shown to "
                                   "cause later gains. Here the only off-arm removes Coach and memory together "
                                   "(opus:O12), so the store's own contribution is not separated from generic coaching; "
                                   "frozen-vs-dynamic changes the store's source, not its presence, in single runs with "
                                   "0.6–4 point gaps. Persisting episodes ≠ showing persisted episodes caused the gain.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("son55", p)["assessment"]["unresolved"] + [
                "7B baseline 0.328 (Table 1) vs 221/643 = 0.344 (Appendix Table 2); 14.4 vs 14.1 pp."],
        },
        "ratings": {
            "G": keep("son55", p, "G", "Both seats 2; re-checked."),
            "M": R("resolved", 2, "Opus sides with son55. The plug-in chain and silence rule are reconstructable, but the "
                   "stated mechanism does not match what was run — retrieval is described as similarity + recency "
                   "(opus:O01) yet implemented as cosine only (opus:O02), the Coach is described as trainable "
                   "(opus:O03) yet used zero-shot (opus:O04) — and there is no argument or distinguishing prediction for "
                   "why summaries of other tasks transfer; the self-vs-foreign explanation is post hoc. Anchor 2.",
                   ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "son55:E011", "son55:E013"]),
            "X": keep("son55", p, "X", "Both seats 2; re-checked."),
            "E.measurement": keep("son55", p, "E.measurement", "Both seats 1; re-checked (agent-side success judge "
                                  "unvalidated; 7B baseline and 14.4 pp inconsistencies, opus:O05–O07)."),
            "E.causality": keep("son55", p, "E.causality", "Both seats 1; re-checked (no Coach-only arm, opus:O12)."),
            "E.holdout": keep("son55", p, "E.holdout", "Both seats 1; re-checked (store from the evaluated stream, "
                              "opus:O10, O11)."),
            "E.statistics": keep("son55", p, "E.statistics", "Both seats 1; re-checked."),
            "E.cost": keep("son55", p, "E.cost", "Both seats 2; re-checked (time/steps per configuration; no tokens/$)."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–B read; in scope (system_method): a persistent cross-"
                  "session episodic store read by a coach that conditions a frozen web agent. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "No store-off arm with the Coach kept (opus:O12); retained persistence is not shown to cause the gain. "
                "sol's own reason concedes the memory net effect is not isolated.", ["opus:O12", "opus:O11"],
                "none (evidence_level is not scored)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "Described mechanism (recency, trainable coach) differs from what was run; no transfer argument.",
                ["opus:O01", "opus:O02", "opus:O03", "opus:O04"], "-5.0 vs sol (20×1/4)"),
            X(p, "local:2511.12997-3", "same_supported_fact",
              "son55 local-3 (judge validity) merged into local-2 = unmet; final local-3 holds son55's former local-1 "
              "(no Coach-only / memory-only control) = unmet",
              "son55 local-3 asks sol's local-2 question with the same answer (unmet).", ["son55:E014", "sol:E007"]),
            X(p, "local:2511.12997-4", "revised",
              "son55 local-4 merged into local-1 = unmet (not challenged_with_evidence); final local-4 holds son55's "
              "former local-2 (statistics) = unmet",
              "Same question as sol local-1; the paper's claim is contradicted (opus:O08, O09), which is 'unmet', not "
              "'challenged_with_evidence'.", ["opus:O07", "opus:O08", "opus:O09"]),
            X(p, "local:2511.12997-5", "son55", "partial",
              "Time and steps reported with overhead acknowledged; no tokens/$/call counts — consistent with E.cost 2.",
              ["son55:E021"]),
            X(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
              "Verified: no-coach baseline exists; no conditioning-off arm with the Coach kept (opus:O12).", ["opus:O12"]),
            X(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
              "Verified: same-ID exclusion only (opus:O10); no overlap audit.", ["opus:O10"]),
            X(p, "rs:adapt_via_conditioning/RE-6", "sol", "partial",
              "Verified: source (GPT-4o vs self) varied; quality/coverage and order not separated.", ["opus:O11"]),
            X(p, "rsi:index_experience_for_reuse/F2", "son55", "partial",
              "Cosine on summaries only (opus:O02); applicability left to the Coach.", ["opus:O02"]),
            X(p, "rsi:index_experience_for_reuse/F3", "son55", "unmet",
              "Failure mode present: store written from the evaluated stream (opus:O11); same-ID guard partial "
              "(opus:O10).", ["opus:O10", "opus:O11"]),
            X(p, "rsi:index_experience_for_reuse/F4", "son55", "unmet",
              "Condenser success flags enter memory without an external gate.", ["son55:E009"]),
            X(p, "rsi:index_experience_for_reuse/S1", "son55", "unmet",
              "Summaries keep episode-specific narrative; no de-instantiation.", ["son55:E009"]),
            X(p, "rsi:index_experience_for_reuse/S4", "son55", "partial",
              "Top-5 cap and silence rule; intervention precision never measured.", ["son55:E012"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–6 and Appendices A–B before seats: store from the evaluated "
                                                   "stream; agent-side success judge; no Coach-only arm; single live "
                                                   "runs; 7B baseline 0.328 vs 0.344; 14.4 vs 14.1; 7B steps rise. "
                                                   "Expected evidence_level task, E items mostly 1.",
            "integrity_checks": "Both seats a1 on 2511.12997v2, material sha 81ba4358…; seat hashes equal conflicts.json; "
                                "both completed RS + domain identification.",
            "core_claim_check": "Scoped: 32B/38B system gains over no-coach at higher wall time; memory attribution and "
                                "'consistent across three backbones' / 'comparable to GPT-4o' not supported.",
            "rating_agreement": "G 2, X 2, E.measurement 1, E.causality 1, E.holdout 1, E.statistics 1, E.cost 2 agree "
                                "and were re-checked.",
        },
    }
    return S


def batch_notes():
    return [
        "2511.06449 FLEX (seat Δ13.75): X 2 (son55), E.measurement 3 (sol), E.causality 2 (sol), E.holdout 2 (son55). "
        "The cross-task aggregation claim is untested (per-benchmark libraries); ProteinGym 'OOD' is within-protein. "
        "RS → C03; domain H01 + H05. Final 50.0 (sol 57.5, son55 43.75).",
        "2511.07317 RLVE: both out_of_scope confirmed (difficulty window is a training curriculum over hand-built "
        "environments; checkpoints evaluated). Shared correction: claim_support unresolved → null.",
        "2511.07800 trainable graph memory (Δ2.5): G 2 (sol), E.measurement 2 (son55 value; basis = Qwen3-4B ITR PopQA "
        "0.157 identical to the no-retrieval row, carrying ~half the +25.8% headline), E.holdout 3 (son55), E.cost "
        "not_reported 0 (hardware-only, r02b/r04a/r06a). Domain H00 + H29 + H28. Final 53.75 (sol 55.0, son55 57.5).",
        "2511.10395 AgentEvolver (scope conflict): out_of_scope (son55). Every result is a GRPO checkpoint evaluated "
        "without experience; the pool is a stripped rollout aid built cold-start via ReMe; the only pool-at-inference "
        "evidence is one dev-set row. Distinguished from EvolveR/LatentEvolve (store read at test). sol 57.5 → not "
        "scored. Card revision proposal (not applied): H28 scope note.",
        "2511.12997 WebCoach (Δ5): M 2 (son55; described recency and trainable coach not as run), evidence_level task "
        "(no Coach-kept store-off arm). sol's inconsistency findings (7B 0.328 vs 221/643; 14.4 vs 14.1 pp) verified. "
        "Final 40.0 (sol 45.0, son55 40.0).",
        "Material requests (not blocking): pinned ACE / ReasoningBank / AgentKB / Memento (FLEX G) and G-Memory "
        "(2511.07800 G) originals; no rating depends on them beyond what the pinned texts show.",
        "Calibration note: son55 again used 'challenged_with_evidence' for a contradicted paper claim (12997 local-4); "
        "sol used zero-padded RE-01..03 (07800) against the run's RE-1..6 syntax (A4) — normalised here.",
    ]
