"""Opus rulings for r11b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2602.21611 subtask-level memory (seat Δ10): final 61.25. G → son55 2: the gap is concrete, but the neighbours "
        "named are instance- or repository-level only; step- or workflow-level memory is not compared, and the "
        "'empirical demonstration' of the mismatch is one case study plus the baseline numbers. X → son55 2: no write "
        "gate, no relevance threshold (top-1 is always injected), append-only store, embedding model unnamed, prompts "
        "unreleased. E.causality → sol 3: structure-only, category-off and raw-trajectory controls run on the same scaffold "
        "and step budget. The category-off arm injects the same top-1 per subtask, so injection quantity is matched. "
        "Single-backbone/no-variance limits are E.statistics (A2). E.holdout → son55 2: the prequential stream is label-free "
        "and is the paper's stated setting; there is no frozen-store or cross-benchmark test. evidence_level → retained "
        "(store-off structure-only arm; precedent r03b Dynamic Cheatsheet, r06b ReasoningBank). Domain → H00 + H03. "
        "H03 names 'cutting episodes into functional subtasks' and 'category filter', which is this paper's design; "
        "H04 is about hierarchical or graph substrates.",
        "2603.01145 AutoSkill (status conflict): final status reviewed, 27.5. The pinned v2 text is complete. The paper "
        "simply contains no downstream evaluation: §5 gives only SkillBank counts, tags and two skill cards. That is "
        "rubric A1, not a missing-material case; needs_evidence/needs_fulltext are reserved for material we could not "
        "read. All five E items are not_reported = 0 with a search scope. Precedent: r03b 2505.17716 AgentRR (A1, 27.5) and "
        "cal-dev 1112.5309. G → sol 2 (the AgentRR precedent). M → son55 2: no outcome signal ever decides whether a skill "
        "helps; skills evolve by repetition. X → son55 2: λ/K/η/α and the extraction LLM are unstated, there is no rollback "
        "or retirement, and §3.1 says 'five' modules but lists six. claim_support → unsupported; evidence_level → null (no "
        "observed gain). sol's seat file was edited in place after the seat run (raw nulled, L/U 40 kept). conflicts.json "
        "hashes match the edited version, which is the one aggregated.",
        "2603.02623 Uni-Skill (Δ5): final 56.25. X → son55 2: the base VLM and its 106K-sample training recipe are unnamed, "
        "tree-expansion and matching thresholds are absent, and whether L_ext skills persist across tasks is never "
        "stated. Shared correction: E.measurement 3 → 2. Table III prints the CaP average as 0.00 while its own per-task "
        "values average 0.29, and the introduction's '+34.0% in unseen skills' cannot be recomputed from Table III "
        "(+33.3 vs MOKA over the six non-pick-place tasks). Run convention r09b/r10b/r11a caps text–table contradictions at "
        "2. Scope kept in-scope B (both seats): the evaluated, retained object is a non-weight skill repository, while the "
        "planner VLM training is a component confound (A3 bullet 2). The only execution-feedback loop is in-episode "
        "re-planning. Domain → H07 + H04 (revised; H02's interaction-stream mining does not describe offline video "
        "annotation). The Fig. 5 ablation values are image-only, so no number was used.",
        "2603.02766 EvoSkill (equal 58.75, shared-error audit): final 56.25. E.measurement → sol 2. The headline 67.9 "
        "(abstract, text, Fig. 2) contradicts Table 1's merge-unique 68.1. BrowseComp 43.5%/48.8% are not integer counts of "
        "the stated 128 examples (55.7 and 62.5 correct), so the denominator is unstated. The substring scorer is "
        "unaudited. E.causality → sol 2: the base-vs-evolved comparison on the held-out test isolates the retained skill "
        "package (skill-only mode inherits the parent's system prompt). Component and prompt-only controls are missing, "
        "so it is not 3. E.cost → sol not_reported 0: no iteration count, tokens, dollars or time. 'Computational cost' "
        "and '1.5 epochs' are not accounting. Shared correction: E.holdout 3 → 2. The headline is the best of four "
        "configurations ranked on the test partition, and merge-unique was added post hoc. Its overlap rule keeps 'the "
        "version from the highest-performing run' without naming the split. The test partitions differ across the "
        "5/10/15% configurations, and the baseline's alignment is unstated. The transfer evidence is one skill, one "
        "direction, single run. RS → generative_process_redesign/null (ReCreate/SICA convention). Domain → H11 + H15 "
        "(revised; H16 rejected because the frontier is a scalar top-k with no complementarity axis).",
        "2603.03329 AutoHarness (Δ5): final 65.0. G → son55 3: illegal moves are a sourced bottleneck (78% of Flash losses), "
        "the replaced object (hand-written harness) is explicit, and neighbours (code world models, code-as-policies, "
        "Voyager, AlphaEvolve, Tang et al. search) are named with distinctions, but not compared. E.cost → son55 2: "
        "learning-step counts are reported per game for all 145 games (the Table 1 caption calls them LLM calls), and "
        "test-time cost is compared in policy mode. Retry calls in verifier mode and synthesis tokens/dollars are missing. "
        "RS → decompose_and_delegate/C25 (LATM/Alita convention): legality, which the LLM handles unreliably, is offloaded "
        "to executable code checked against the environment. son55's recomputation was verified: the 32 starred games "
        "average 14.5 learning steps with 19 under 10, while all 145 average 10.3.",
        "A4 hygiene: hidden ID collisions were renumbered or merged in all five papers (local IDs reused by the two seats for "
        "different questions). Expectations from RS cards that were not kept were merged into the kept card's equivalent "
        "question or moved to local IDs. None were dropped.",
        "Figure dependence: 2602.21611 Figs 3–6, 2603.02623 Fig. 5 (ablation) and 2603.03329 Figs 3–7 carry values only as "
        "images. Ratings rely on text and tables, and no figure value was invented.",
        "No material requests: every disputed field was answerable from the pinned texts.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

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

    def assess(s, p, extra_unresolved=()):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        return prefix(a, s)

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def conv(old):
        return {"converted_from": old,
                "source_note": f"Moved from {old}: that card was not kept in the final pattern record (see "
                               "resolutions). The check is still a valid question about this paper's claim, so it is "
                               "kept under the ID shown (A4)."}

    def NR(reason, ev, scope):
        return R("not_reported", 0, reason, ev, (), scope)

    # =========================================================== 2602.21611 subtask-level memory (Δ10)
    p = "2602.21611"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "is initialized as empty and accumulates experience on-the-fly.", "§4.1 Baselines, Models, and Protocol",
                    "Prequential protocol: each instance is scored by the hidden SWE-bench tests, and memory is written "
                    "only from the agent's own trajectories. The stream is the stated test-time-learning setting, not a "
                    "label leak."),
            opus_ev(p, "O02", "evaluates the correctness of the subtask execution.", "§3.5 Experience Extraction",
                    "The write path's correctness signal is the backbone's own judgment. No external check gates what "
                    "enters the store."),
            opus_ev(p, "O03", "denotes a fixed embedding model.", "§3.4 Semantic Matching (Eq. 2)",
                    "The embedding model is not named, and no similarity threshold is given (top-1 is always injected)."),
            opus_ev(p, "O04", "In this baseline, the retrieval mechanism performs a global search across the entire collection of accumulated memories to select the top-1 experience based on similarity",
                    "§4.3 Impact of Category Isolation",
                    "The category-off arm still injects one entry per subtask, so injection count is matched between "
                    "it and the full method. This answers son55's 'injection quantity uncontrolled' concern for the "
                    "routing claim."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "reason": "Opus keeps C03 (sol and son55 agree on it). The frozen agent is conditioned on retrieved "
                      "reference entries from a store that grows online, with no parameter updates. This is C03's "
                      "reference-substrate sub-move, the run convention for experience-memory papers (ExpeL, AWM, "
                      "ReasoningBank). son55's supporting heterogeneous_decomposition is dropped. The four categories "
                      "are author-fixed functional stages, not a partition by a measured discriminating property, and "
                      "every partition gets the same treatment (same top-1 cosine retrieval). The category-off ablation "
                      "tests routing, not a per-partition treatment.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "index_experience_for_reuse", "sub": "H03"},
             "operation_correspondence": "Subtask-level (category, intent, experience) cases are retrieved by category "
                                         "filter + cosine top-1 and injected into a frozen agent. That is a reference "
                                         "substrate conditioning inference (C03) and precedent-case retrieval with "
                                         "functional subtask units (H03 step 1/3).",
             "necessary_conditions/differences": "H03's write gate (step 2) and construction/evaluation separation "
                                                 "(step 5) are absent. C03's upstream schema training is absent "
                                                 "(training-free branch).",
             "evidence_ids": ["son55:E003", "opus:O02", "opus:O01"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H00"},
             "operation_correspondence": "The extractor turns each subtask trajectory into success patterns or "
                                         "failure-avoidance lessons (H00 reflect-into-lessons), which are then consumed "
                                         "as conditioning.",
             "necessary_conditions/differences": "The lesson unit is a subtask, not an episode. There is no "
                                                 "consolidation or forgetting (H00/S4 unmet).",
             "evidence_ids": ["son55:E004", "son55:E015"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2602.21611-1"): "rsi:index_experience_for_reuse/S5"},
            overrides={
                "rsi:index_experience_for_reuse/S5": {
                    "status": "met",
                    "reason": "Opus: same question as sol's local-1 (merged, A4). The structure-only arm keeps segmentation "
                              "and prompting but removes retrieval and update (Table 2: 53.2 vs 56.1 full, 52.2 vanilla), "
                              "so the retained-store ablation the condition asks for is reported. Single-backbone, "
                              "no-variance and stream-construction limits are scored in E.statistics/E.holdout (A2)."},
                "rsi:index_experience_for_reuse/S4": {
                    "status": "partial",
                    "reason": "Opus sides with son55. Category filter and cap 1 are present, but there is no relevance gate "
                              "(opus:O03). The authors attribute the early-bucket dip to retrieval without relevant "
                              "matches, which is the stated harm."},
            }),
        "claims": lambda c: add_counter(c, "C3", ["opus:O04"]),
        "assessment": assess("son55", p, ["Embedding model and extraction/segmentation prompts unreleased (opus:O03, son55:E022)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The changed object (memory unit granularity) is concrete, and the "
                   "inst-level baseline's Claude regressions are consistent with it. But the neighbours compared are "
                   "instance- and repository-level only (son55:E021). Step- or workflow-level experience memories are "
                   "not compared, and the abstract's 'we empirically demonstrate' mismatch rests on one case study and "
                   "baseline scores, with no retrieval-precision diagnostic (son55:E020). Anchor 2: real limitation, "
                   "incomplete neighbour comparison.", ["son55:E001", "son55:E020", "son55:E021"], ["sol:E013"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Segment → intent → category-filtered top-1 → abstracted "
                   "lesson → append targets cross-stage interference directly, and the ablations embody distinguishable "
                   "predictions (category-off and raw-trajectory). Not 4: the write signal is self-judged correctness "
                   "(opus:O02), and always injecting top-1 is an untested assumption.",
                   ["son55:E002", "son55:E003", "son55:E004", "sol:E002", "opus:O02"]),
            "X": R("resolved", 2, "Opus sides with son55. The read/write chain is reconstructible (Algorithm 1). But "
                   "retention has no gate (every subtask is appended, opus:O02), there is no dedup, merge, retirement "
                   "or rollback, retrieval has no threshold, the embedding model is unnamed (opus:O03), and the "
                   "segmentation/extraction prompts are unreleased (son55:E022). Anchor 2: main steps described, "
                   "retention and key conditions unclear.",
                   ["son55:E003", "son55:E006", "son55:E022", "son55:E023", "opus:O02", "opus:O03"], ["sol:E001"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Pass@1 is from SWE-bench Verified's executable "
                               "tests over 500 issues, and Avg (3 runs) is kept separate from Best@3. The Table 1 "
                               "margins and relative gains recompute (+5.6/+6.8/+3.9/+2.3; mean 4.65 ≈ 4.7). Not 4: the "
                               "inst-level baseline is a self-reproduction with no fidelity check (son55:E009).",
                               ["son55:E008", "son55:E010", "sol:E005", "sol:E009"], ["son55:E009"]),
            "E.causality": R("resolved", 3, "Opus sides with sol. On the same scaffold and step budget, structure-only "
                             "(no memory), category-off and raw-trajectory controls each remove one ingredient (Tables "
                             "2–4). The category-off arm injects one entry per subtask like the full method (opus:O04), "
                             "so son55's injection-quantity objection does not hold for the routing claim. The "
                             "ReasoningBank reproduction gives a second memory baseline on four backbones. Not 4: "
                             "there is no longer-context or alternative-abstraction control, and ablations are on one "
                             "backbone. Their missing variance is scored in E.statistics (A2).",
                             ["sol:E010", "sol:E011", "son55:E013", "son55:E014", "son55:E015", "opus:O04"],
                             ["son55:E012"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. The stream is prequential and label-free (opus:O01): "
                           "hidden tests score each instance, the memory is written only from the agent's own "
                           "trajectories, and three shuffled orders are run. This is the paper's claimed test-time setting, "
                           "so sol's 1 over-penalises. Not 3: there is no frozen-store evaluation, no cross-repository or "
                           "cross-benchmark test, and no contamination discussion for public SWE-bench.",
                           ["son55:E008", "opus:O01"], ["sol:E007"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): three shuffled runs with mean±std for the main "
                              "table. There is no interval or test, ablation run counts are unstated, and the temporal and "
                              "difficulty analyses use one 'representative' run.",
                              ["son55:E008", "son55:E016", "sol:E008"]),
            "E.cost": R("resolved", 2, "Both seats 2. The per-instance step cap includes memory-extraction steps (budget-"
                        "neutral in steps), and the extractor uses the same backbone. There are no tokens, dollars, "
                        "latency or embedding/storage figures.", ["son55:E007", "sol:E006"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read. In scope (A): a non-weight memory written from execution trajectories, "
                  "retained across instances and read by later ones. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 3–6 (temporal buckets, complexity tiers, retrieval frequency, phase distribution) "
                             "are cited only through their prose values.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "Memory written from earlier instances is read by later ones, and the structure-only arm (same prompting, "
                "no store) shows the gain disappears without it. That meets EVIDENCE.md 'retained' (later-task gain from "
                "the retained change). No selection set is involved, so rule 2 does not cap it. Precedent: r03b Dynamic "
                "Cheatsheet and r06b ReasoningBank (prequential stream + store-off arm → retained). The stream origin is "
                "recorded in E.holdout.", ["son55:E013", "opus:O01"], "none (evidence_level is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "heterogeneous_decomposition is dropped: the categories are fixed functional stages, not a partition "
                "by a measured property, and every partition gets the same treatment (see rs_pattern.reason).",
                ["son55:E002", "son55:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"]],
                "H03 explicitly covers 'cutting episodes into functional subtasks' with 'category filter' retrieval and "
                "append-with-outcome, which is this paper's design. H04 targets hierarchical, graph or tiered substrates "
                "certified by recall cost at scale, and a flat category-partitioned store is not that.",
                ["son55:E003", "son55:E004", "son55:E006"], NOSCORE),
            XC(p, "local:2602.21611-1", "revised",
               {"local:2602.21611-1": "unmet (son55: extraction token/dollar cost)",
                "rsi:index_experience_for_reuse/S5": "met (sol's structure-only question, merged)"},
               "A4 collision: sol's local-1 (structure-only control) and son55's local-1 (unaccounted extraction cost) "
               "are different questions. son55's question keeps local-1, unmet (verified: steps only, no tokens or "
               "dollars). sol's question is the store-removal condition and merges into index S5, met.",
               ["son55:E007", "sol:E010"]),
            XC(p, "local:2602.21611-2", "sol", "partial",
               "Verified: later instances use memory from earlier ones in three shuffled orders, but there is no frozen "
               "separate test stream. Partial is consistent with E.holdout=2.", ["sol:E007", "sol:E008", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap or contamination analysis for public SWE-bench Verified against the four backbones.",
               ["son55:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: the raw-trajectory store (a nearest-neighbour-like alternative) and ReasoningBank are compared. "
               "There is no longer-context alternative.", ["son55:E009", "son55:E013", "son55:E015"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step5", "son55", "partial",
               "Verified: the step budget includes extraction, but token and dollar cost are not reported.",
               ["son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "sol", "partial",
               "Verified: success/failure is a self-judgment whose error rate is neither acknowledged nor measured "
               "(opus:O02).", ["sol:E003", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "unmet",
               "Verified: append-only. There is no consolidation, conflict handling or forgetting, and 50.7% of "
               "retrieved entries are single-use.", ["sol:E004", "son55:E019"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unmet",
               "Failure mode present (son55 convention: unmet = present). The store is built from the evaluated stream "
               "(prequential, label-free), so the gain is not separated from it.", ["son55:E008", "opus:O01"]),
            XC(p, "rsi:index_experience_for_reuse/F4", "son55", "unmet",
               "Failure mode present: model-judged entries are admitted without an external gate (opus:O02).",
               ["son55:E005", "son55:E006", "opus:O02"]),
            XC(p, "rsi:index_experience_for_reuse/S1", "son55", "met",
               "Verified: subtask units, with file paths stripped by the extractor. Raw trajectory vs abstracted lesson "
               "is 53.4 vs 56.1.", ["son55:E004", "son55:E015"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "unmet",
               "Verified: every extracted entry is appended after the same-backbone self-judgment, with no test or "
               "threshold gate.", ["son55:E005", "son55:E006"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "partial",
               "Category filter and cap 1 are present, but there is no relevance threshold (opus:O03), and the authors "
               "attribute the early dip to irrelevant retrieval.", ["son55:E003", "son55:E017", "opus:O03"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "revised", "met",
               "The structure-only arm removes the store under the same prompting (Table 2). The condition asks whether "
               "the retained-store ablation exists, and it does. son55's reasons (one backbone, no variance, no frozen "
               "store) are scored in E.statistics/E.holdout (A2), not here. sol's local-1 is merged into this ID.",
               ["son55:E013", "sol:E010"]),
            XC(p, "rsi:index_experience_for_reuse/S6", "son55", "partial",
               "Verified: updates are local, cheap appends, but there is no consolidation or decay, and the store grows "
               "without bound.", ["son55:E006", "son55:E019"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2, "See ratings.G: step- or workflow-level neighbours are "
                "missing, and the mismatch diagnosis is one case.", ["son55:E020", "son55:E021"], "−3.75 vs sol (15×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2, "See ratings.X: no write gate, no threshold, append-only, "
                "unnamed embedder, prompts unreleased.", ["son55:E006", "son55:E022", "opus:O03"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", 3, "See ratings.E.causality: three "
                "one-ingredient controls on the same scaffold, and the category-off arm has matched injection count "
                "(opus:O04). Single-backbone variance belongs to E.statistics (A2).", ["sol:E010", "sol:E011", "opus:O04"],
                "+3.75 vs son55 (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 2, "See ratings.E.holdout: a label-free "
                "prequential stream with three orders is the claimed setting. There is no frozen or cross-benchmark "
                "test.", ["son55:E008", "opus:O01"], "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole pinned text before opening the seats. Initial view: in "
                                                   "scope (A, retained). G≈2 (neighbours are instance-level only), M 3, X 2 "
                                                   "(no gate or threshold, append-only). E: measurement 3, causality 3 "
                                                   "(three one-ingredient controls), holdout 2 (prequential stream), "
                                                   "statistics 2, cost 2.",
            "integrity_checks": "Both seats a1 on 2602.21611v1, material sha 1b53121d…. Canonical seat hashes equal "
                                "conflicts.json. Both completed 15+31 and domain identification with valid namespaces.",
            "core_claim_check": "Table 1 arithmetic recomputed (Δ and Rel.). The structure-only arm is the store-off "
                                "control, so retained is supported for the stream setting. The 'consistent across seeds' "
                                "claim cannot be checked from the text.",
            "rating_agreement": "M, Em, Es and Ecost agree and were re-checked. G, X and Eh resolved to son55, Ec to sol.",
        },
    }

    # =========================================================== 2603.01145 AutoSkill (status conflict)
    p = "2603.01145"
    scope = ["Opus: complete pinned v2 text §1–6, Tables 1–2, Figures 2–3 (inline values), all skill cards after §6; "
             "no appendix exists",
             "§5 contains only SkillBank counts, tags, platform mentions, version numbers and two qualitative cards; "
             "no downstream response/task metric, control, split, uncertainty or cost appears anywhere"]
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "We propose a training-free lifelong learning framework that improves dialogue quality through explicit skill self-evolution rather than parameter updates.",
                    "§3 Method", "The central claim includes improved dialogue quality, which needs a downstream measurement."),
            opus_ev(p, "O02", "For each subset, we apply the same large language model based skill extraction pipeline and organize the extracted results into a corresponding SkillBank.",
                    "§5.1 Dataset and Protocol", "The only experiment is offline extraction. No response is generated or "
                                                 "scored with the bank, and the extraction LLM is not named."),
            opus_ev(p, "O03", "These observations provide qualitative evidence that the proposed versioned maintenance mechanism supports continual refinement rather than simple skill duplication.",
                    "§5.2 SkillBank Statistics", "The authors themselves label the version-count evidence as qualitative."),
            opus_ev(p, "O04", "the system is implemented with five prompt-driven modules: a query rewriting model, a dialogue response model, a skill extraction model, a skill management judge, a skill merge model, and an embedding model for skill vectorization.",
                    "§3.1 Problem Definition", "Says five modules but lists six. This is a small internal inconsistency "
                                               "in the method description, recorded under X."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "reason": "Opus sides with sol on the sub-card. Retrieved skills are injected as conditioning into a frozen "
                      "response model (hybrid BM25/dense retrieval with threshold and no-skill fallback). This is C03's "
                      "reference-substrate sub-move (retrieve reference items as first-class input, no upstream tuning), "
                      "the convention used for retrieval-conditioned skill and memory papers (2602.21611 in this batch, "
                      "ExpeL, AWM). son55's null is defensible, but it would split the convention. The pattern's "
                      "category-holdout and cheaper-baseline steps are not executed.",
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H02")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H02"},
             "operation_correspondence": "User-query streams are mined into versioned SKILL.md packages, gated by an LLM "
                                         "judge (add/merge/discard), merged with versioning, and retrieved as "
                                         "conditioning for later responses.",
             "necessary_conditions/differences": "H02 step 5 (downstream reuse on disjoint tasks) is entirely absent, "
                                                 "which is H02's recorded failure 'library statistics instead of downstream "
                                                 "gains'.",
             "evidence_ids": ["son55:E003", "son55:E004", "son55:E006", "son55:E011"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.01145-1"): "rs:adapt_via_conditioning/RE-1",
                    ("sol", "local:2603.01145-2"): "local:2603.01145-3"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "unmet",
                    "reason": "Opus: same question in both seats (sol local-1 = son55 RE-1, merged, A4). There is no "
                              "skill-on/skill-off comparison of later responses."},
                "local:2603.01145-3": {"note": "sol's local-2 (cost) renumbered: A4 collision with son55's local-2 "
                                               "(version-effect question)."},
                "rsi:abstract_experience_into_guidance/H02.step3": {
                    "status": "partial",
                    "reason": "Opus revises son55's unmet. H02 step 3 has two parts. A quality-judge gate with versioned "
                              "merge exists (P_judge add/merge/discard, Bump). Survival, merge and discard fractions are "
                              "not reported."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02"]) if any(x.get("claim_id") == "C1" for x in c) else c,
        "assessment": {
            "evidence_level": None,
            "evidence_level_note": "No EVIDENCE.md level: no task output or score is measured (opus:O02). Levels start at "
                                   "an observed gain (precedents cal-dev 1112.5309 and r03b 2505.17716). Null, not "
                                   "'none'; son55's 'none' is not a valid label and sol's 'task' asserts a measured gain "
                                   "that does not exist.",
            "claim_support": "unsupported",
            "strongest_supported_claim": "The pipeline produced 1,858 SKILL.md artifacts from four WildChat subsets (counts "
                                         "add up). Some skills went through many judge-approved merges (e.g. v0.1.34). "
                                         "The claimed improvement in dialogue quality and lifelong personalized "
                                         "capability (opus:O01) has no measurement.",
            "unresolved": ["Whether retrieved skills change or improve any response", "Judge accuracy and wrong-merge "
                           "rate", "Extraction LLM and λ/K/η/α values", "Safety review of user-sourced skill content "
                           "(son55:E018)"],
        },
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The limitation is real and specific: recurring user preferences "
                   "are not consolidated into explicit, maintained behavior units. Memory systems (Mem0, A-MEM, "
                   "MemGPT) and skill libraries (Voyager) are named and contrasted, but only conceptually, with no "
                   "measured failure of those neighbours. Anchor 2 (real limitation, incomplete neighbour comparison). "
                   "Same grade as the A1 precedent AgentRR (r03b).", ["sol:E010", "son55:E016", "son55:E017"]),
            "M": R("resolved", 2, "Opus sides with son55. The extract → nearest-neighbour judge → versioned merge → "
                   "thresholded retrieval chain is coherent, and query-only extraction is a sensible guard. But no outcome "
                   "signal ever tells the system whether a skill helped. Skills evolve by repetition of user requests, "
                   "the judge sees only the top-1 neighbour, and no prediction separates this from plain preference "
                   "memory. Anchor 2: concrete mechanism, key assumption weak.",
                   ["son55:E003", "son55:E004", "son55:E005", "son55:E006"], ["sol:E002"]),
            "X": R("resolved", 2, "Opus sides with son55. The prompts are summarised, and the storage layout, versioning "
                   "and serving/background split are described. But λ, K, η, α, M and the extraction model are unstated "
                   "(son55:E007, opus:O02). There is no rollback, retirement or conflict arbitration beyond the merge "
                   "prompt, the library has no bound, and §3.1's module count is inconsistent (opus:O04). Anchor 2.",
                   ["son55:E004", "son55:E006", "son55:E007", "opus:O04"], ["sol:E005"]),
            "E.measurement": NR("Opus sides with son55 (rubric A1). No metric measures the central claim (dialogue "
                                "quality or personalization). The counts, tags and versions measure artifact production, "
                                "not the claimed effect, and the authors call the version evidence qualitative "
                                "(opus:O03).", ["son55:E011", "son55:E012", "opus:O03"], scope),
            "E.causality": NR("Both seats; A1. There is no skill-bank on/off comparison, no alternative memory or "
                              "extractor, and no budget-matched control.", ["son55:E002", "opus:O02"], scope),
            "E.holdout": NR("Both seats; A1. There is no selection/test split and no cross-user or cross-model reuse "
                            "experiment ('model families' are the dialogue sources).", ["son55:E009", "son55:E015"], scope),
            "E.statistics": NR("Both seats; A1. There are no repeated outcome runs, intervals or failure denominators, "
                               "only corpus totals.", ["son55:E011"], scope),
            "E.cost": NR("Both seats; A1. No extraction, judge or merge calls, tokens, latency or storage are reported. "
                         "Asynchrony is architectural only.", ["sol:E011"], scope),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read (§1–6, tables, figures, all skill cards; no appendix). In scope (B, "
                  "H02-type skill-mining component). The paper has no downstream evaluation, so it is scored under "
                  "frozen rubric A1: five E items not_reported with search scope. This is a property of the paper, not "
                  "missing material, so needs_evidence does not apply (BATCH_CONTRACT reserves needs_* for material we "
                  "could not read).",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope B; both seats agree)",
        "figure_dependence": None,
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "No observed task gain exists (opus:O02), so no level applies. son55's raw value was the string 'none', "
                "which the normaliser reads as null. The final is canonical null with a note. sol's 'task' would assert "
                "a measured output gain.", ["opus:O02", "son55:E011"], "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", "unsupported",
                "The central claim is improved dialogue quality and lifelong personalized capability (opus:O01, "
                "son55:E002). Nothing measures it. Only the artifact-production description is supported, which is "
                "kept as strongest_supported_claim. A narrower supported claim would not be the author's claim. "
                "Precedent r03b AgentRR: unsupported.", ["opus:O01", "opus:O02"], "none (claim_support is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "Same parent card. C03's reference-substrate sub-move matches retrieval-conditioned injection, and it is "
                "the batch and run convention (see rs_pattern.reason).", ["sol:E004", "son55:E008"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["abstract_experience_into_guidance", "H02"]],
                "H02 already covers 'deduplication, merging with neighboring skills ... and how a new version merges with "
                "an existing one'. H01 would add nothing distinct: its edit vocabulary is about deleting or consolidating "
                "entries of one living document, and AutoSkill's 'discard' rejects a candidate rather than deleting a "
                "stored entry.", ["son55:E004", "son55:E006"], NOSCORE),
            XC(p, "rs:adapt_via_conditioning/RE-1", "same_supported_fact", "unmet",
               "Same question as sol's local-1 (later-response improvement vs the same model without skills). Both seats "
               "found it unmet, so the two are merged under the RE-1 ID.", ["son55:E002", "sol:E007", "sol:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/F1", "son55", "partial",
               "Verified: 'training-free' is repeatedly framed as the distinguishing property (§3.5), although the explicit "
               "artifact lifecycle is also argued. Failure mode partly present.", ["son55:E002", "opus:O01"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00.step5", "son55", "unmet",
               "Verified: there is no budget-matched baseline and no store-off ablation, since no downstream experiment "
               "exists. Kept although H00 is not a final match: the parent card is kept, and the question applies to "
               "this paper's claim.", ["son55:E002", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/H02", "sol", "partial",
               "Verified: package contract, judge-gated neighbour merge and versioning are specified, and disjoint "
               "downstream reuse is absent.", ["sol:E001", "sol:E002", "sol:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/H02.step3", "revised", "partial",
               "son55's unmet covered only the unreported survival fractions. The step also asks for a quality-judge gate "
               "with versioned merge, which exists. One part met and one part absent gives partial. (The final record's "
               "domain match keeps son55's condition note on this step.)", ["son55:E005", "son55:E006", "son55:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/H02.step5", "son55", "unmet",
               "Verified: library statistics are reported instead of downstream gains, which is H02's recorded failure.",
               ["son55:E011", "son55:E012", "opus:O03"]),
            XC(p, "rsi:evidence_gated_retention/F1", "son55", "unmet",
               "Failure mode present: versioning and registration infrastructure stands in for a measured admission or "
               "retirement test.", ["son55:E004", "son55:E006"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Verified: no counterfactual (skill on/off) value is measured for any skill.", ["son55:E004", "son55:E005"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", 2, "See ratings.G: a real, specific limitation with a "
                "conceptual-only neighbour contrast is anchor 2. Grade 1 would require the limitation to be largely "
                "unsubstantiated. Consistent with the AgentRR A1 precedent.", ["sol:E010", "son55:E016"],
                "+3.75 vs son55 (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2, "See ratings.M: no outcome signal governs skill evolution, "
                "and there is no distinguishing prediction against preference memory.", ["son55:E003", "son55:E004"],
                "−5.0 vs sol (20×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2, "See ratings.X: hyperparameters and extraction model are "
                "unstated, there is no rollback or retirement, and the module count is inconsistent.",
                ["son55:E007", "opus:O02", "opus:O04"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "not_reported", "rating": 0},
                "A1: the counts do not measure the claimed effect. sol's 1 credits measuring artifact production, which "
                "is not the central claim, and the same fact is already reflected in X.", ["opus:O02", "opus:O03"],
                "−2.5 vs sol (10×1/4)"),
            res("status", *C(p, "status"), "son55", "reviewed",
                "The material is complete (manifest complete=true; sol itself says 'not missing fulltext'). A paper that "
                "ran no downstream evaluation is scored under A1 with not_reported items. needs_evidence would leave a "
                "fully read paper permanently unscored and treat 'the authors did not test it' as 'we could not see it', "
                "which BATCH_CONTRACT forbids conflating. Precedent: r03b 2505.17716 and cal-dev 1112.5309, both reviewed "
                "under A1.", ["opus:O02", "son55:E011"], "row becomes scored: raw 27.5 (sol withheld raw; son55 23.75)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole pinned text before opening the seats. Initial view: a "
                                                   "system description whose §5 is library statistics only. A1 applies: "
                                                   "five E items not_reported. G≈2, M 2 (no outcome signal), X 2 "
                                                   "(parameters and extractor unstated). Unsupported central claim.",
            "integrity_checks": "Both seats a1 on 2603.01145v2, material sha dc690a5e…. Canonical seat hashes equal "
                                "conflicts.json. sol's file was edited after its run (raw nulled, git diff), and "
                                "conflicts.json was computed on the edited file. Both completed 15+31 and domain "
                                "identification.",
            "core_claim_check": "son55's sums verified (400+631+224+603 = 1858; category counts also 1858). No response is "
                                "ever generated with the bank in §5 (opus:O02).",
            "rating_agreement": "The four E items other than measurement agree (not_reported). G resolved to sol; M, X and "
                                "Em to son55.",
        },
    }

    # =========================================================== 2603.02623 Uni-Skill (Δ5)
    p = "2603.02623"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Average 0.00 0.39 0.73", "Table III (last row)",
                    "CaP's printed average is 0.00, but its per-task column (0.80, 0.20, 0.80, 0.00, 0.50, 0.00, 0.00, 0.00) "
                    "averages 0.29. This is an internal table inconsistency.", kind="our_inference"),
            opus_ev(p, "O02", "On real-world settings, the performance of Uni-Skill achieves an improvement of 20.0% on long-horizon tasks and 34.0% in unseen skills.",
                    "§I Introduction",
                    "From Table III, Pick Place + Stack Blocks give Uni 0.70 vs CaP 0.50 (+20.0, reproduced). The other six "
                    "tasks give Uni 0.733 vs MOKA 0.400 (+33.3), so 34.0 is not reproduced under that grouping, and the "
                    "paper states no other grouping.", kind="our_inference"),
            opus_ev(p, "O03", "is synthesized or retrieved on demand, ensuring sufficiency for specific task requirements.",
                    "§III-A Skill-Aware Planning",
                    "L_ext is per-instruction. The text never states that synthesized skills persist into later tasks, "
                    "so the 'self-augmented library' is not a defined retention mechanism."),
            opus_ev(p, "O04", "it further improves the success rates on Close Drawer and Seat Down by 12%.",
                    "§IV-D Failure mode and recovery",
                    "The only execution-feedback loop is in-episode re-planning with negative examples. It has no "
                    "denominator and is not retained across tasks."),
            opus_ev(p, "O05", "we trained it with 106K runtime code samples derived from videos demonstrations.",
                    "§III-A", "The planner VLM is weight-trained (base model unnamed). This confounds the comparison with "
                              "prompted CaP/MOKA. The retained object being evaluated is still the non-weight repository "
                              "(A3 bullet 2)."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "reason": "Both seats C03. Retrieved demonstration slices (semantic constraints + projected trajectories) are "
                      "a reference substrate conditioning waypoint generation for never-seen skills without per-skill "
                      "training. son55's supporting decompose_and_delegate/C25 is dropped. C25's load-bearing move is "
                      "closing the loop with a sound solver's verifiable output during construction. Here the planner's "
                      "code calls fixed APIs, and waypoints are VLM-selected with no verifier (son55 itself graded S2–S5 "
                      "unmet or absent). The one closed loop is an in-episode retry (opus:O04).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07"),
                                       dmatch("sol", p, "index_experience_for_reuse", "H04")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "crystallize_executable_capability", "sub": "H07"},
             "operation_correspondence": "A sufficiency discriminator detects a capability gap, a generator writes the "
                                         "missing skill description, and the skill is implemented from retrieved external "
                                         "demonstrations (H07 steps 1–2; C03 reference substrate).",
             "necessary_conditions/differences": "H07 steps 3–5 (execution repair, registration, reuse evaluation) are "
                                                 "absent. The 'skill' is a VLM-generated trajectory, not a verified "
                                                 "registered tool (F2 partial).",
             "evidence_ids": ["son55:E003", "son55:E009", "opus:O03"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "index_experience_for_reuse", "sub": "H04"},
             "operation_correspondence": "SkillFolder is a four-layer VerbNet hierarchy with local child-node expansion. "
                                         "Content (slices) is reached through a separate semantic index, which is H04's "
                                         "restructured substrate.",
             "necessary_conditions/differences": "There is no flat-retrieval comparison at matched information and no "
                                                 "scaling-cost certification. The substrate is built offline from videos, "
                                                 "not from the agent's own execution.",
             "evidence_ids": ["sol:E002", "sol:E003", "son55:E007"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.02623-1"): "local:2603.02623-2",
                    ("son55", "rs:decompose_and_delegate/RE-1"): "local:2603.02623-3",
                    ("son55", "rs:decompose_and_delegate/RE-5"): "local:2603.02623-4"},
            overrides={
                "local:2603.02623-2": {
                    "status": "unmet",
                    "reason": "Opus: same question in both seats (sol local-1 = son55 local-2, merged, A4). No experiment "
                              "shows a skill created at deployment being retained and reused on later tasks "
                              "(opus:O03)."},
                "local:2603.02623-3": dict(conv("rs:decompose_and_delegate/RE-1")),
                "local:2603.02623-4": dict(conv("rs:decompose_and_delegate/RE-5")),
                "rs:adapt_via_conditioning/RE-6": {
                    "status": "partial",
                    "reason": "Opus sides with sol. Table IV compares two sources that differ in coverage and quality, and "
                              "a 135-slice audit exists. The distribution gap between real-robot or human videos and the "
                              "RLBench test domain is not characterised."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01", "opus:O02"]), "C5", ["opus:O03"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats. The output gains on RLBench and on the real robot are reported, but no "
                                   "retained change is shown to improve later tasks. Repository growth is offline, and "
                                   "L_ext persistence is undefined (opus:O03).",
            "claim_support": "scoped",
            "strongest_supported_claim": "With a trained planner VLM plus SkillFolder-conditioned trajectory generation, "
                                         "Uni-Skill's average success on 10 author-chosen out-of-API RLBench tasks (0.41 vs "
                                         "MOKA 0.10; 3×25 episodes) and on 8 real tasks (0.73 vs 0.39, 10 trials) exceeds "
                                         "prompted baselines. Trained VLM and retrieval are confounded, and runtime "
                                         "self-evolution is not shown.",
            "unresolved": ["Retrieval vs trained-VLM share of the gain", "Discriminator accuracy",
                           "Cross-task retention of synthesized skills", "Fig. 5 ablation magnitudes (image-only)", "Costs"],
        },
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed-API and manual-demonstration bottleneck is concrete, "
                   "and the closest lines (code-as-policies, human-feedback skill addition, retrieval-based BC) are "
                   "named with stated differences. Not 4: library-growing agents (Voyager-style, tool-making) are not "
                   "positioned, and the 'self-evolving' lineage is overstated.",
                   ["son55:E002", "sol:E012", "son55:E023"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Gap detection → skill description → hierarchical retrieval → "
                   "semantic-constraint and trajectory conditioning → SE(3) lifting is a coherent response, and the "
                   "ablation embodies category-specific predictions (contact-sensitive tasks need constraints, precise "
                   "tasks need trajectories). Not 4: discriminator reliability is assumed.",
                   ["son55:E003", "son55:E009", "son55:E018", "sol:E005"]),
            "X": R("resolved", 2, "Opus sides with son55. Annotation roles, tree layers and the orientation transfer are "
                   "described. But the base VLM and its 106K-sample training are unnamed (opus:O05), matching and "
                   "tree-expansion thresholds are absent, whether L_ext persists across tasks is undefined (opus:O03), "
                   "retrieved slices have no execution check, and the self-correction mechanism is one sentence "
                   "(opus:O04). Anchor 2: retention and key conditions unclear.",
                   ["son55:E005", "son55:E007", "son55:E008", "opus:O03", "opus:O05"], ["sol:E003"]),
            "E.measurement": R("resolved", 2, "Shared correction 3 → 2. Simulator binary success (25 episodes × 3) and real "
                               "trials are appropriate metrics, and Tables I/II averages recompute. But Table III's CaP "
                               "average is printed 0.00 against a per-task mean of 0.29 (opus:O01). The introduction's "
                               "'+34.0% in unseen skills' does not recompute from Table III (opus:O02), and the real-world "
                               "success criteria are unstated. Run convention (r09b/r10b/r11a): text–table "
                               "contradictions cap E.measurement at 2. Both seats saw the 0.00 error and still gave 3.",
                               ["son55:E011", "son55:E014", "opus:O01", "opus:O02"], ["son55:E016"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Update-off and constraint/trajectory ablations "
                             "exist (values image-only), as does a data-source comparison. But a trained VLM is compared "
                             "against prompted GPT baselines (opus:O05), with no same-VLM no-retrieval or flat-retrieval "
                             "arm.", ["son55:E018", "son55:E019", "sol:E008"], ["son55:E010", "opus:O05"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. The test domains (RLBench sim, Franka) differ from "
                           "DROID. The out-of-API tasks are author-chosen with unstated criteria, and there is no overlap "
                           "audit against the 106K code samples or SkillFolder.",
                           ["son55:E012", "sol:E002"], ["son55:E005"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2): σ over 3 simulation repeats. Real-world results are "
                              "10 trials with no interval, and there is no test.", ["son55:E011", "son55:E015"]),
            "E.cost": NR("Both seats; not reported. No VLM training cost, 350 h annotation cost, GPT-4o/VLM call counts "
                         "or latency are given. 'Efficient retrieval' is qualitative.", ["sol:E002"],
                         ["Opus: complete pinned v1 §I–V, Tables I–IV, figure captions; no appendix exists",
                          "no cost, call-count, latency or annotation-expense figure anywhere"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read. In scope (B, rubric A3 bullet 2). The evaluated, retained object is a "
                  "non-weight skill repository with gap-triggered skill requests. The trained planner VLM is a confound, "
                  "not the evaluated object. The paper has no runtime self-evolution loop and is evaluated on its own "
                  "zero-shot claim. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope B; both seats agree; boundary noted: repository built offline from videos)",
        "figure_dependence": "Fig. 5 (ablation) values are image-only and used only as the qualitative direction stated "
                             "in §IV-C. Figs 4/6 not used numerically.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "C25 dropped: there is no solver-verified intermediate artifact and no construction-time verification "
                "loop (see rs_pattern.reason).", ["son55:E009", "opus:O04"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["crystallize_executable_capability", "H07"], ["index_experience_for_reuse", "H04"]],
                "H07 (son55) carries the central claim: an explicit gap-detection decision, then a capability built "
                "on demand from external demonstrations. H04 (sol) carries SkillFolder: a semantic hierarchy whose "
                "index is decoupled from its content, with local child expansion. H02 (son55) is dropped. Its stream "
                "is the agent's or users' interaction histories compiled into gated skill packages, whereas SkillFolder "
                "is VLM-annotated third-party video slices without a package contract or retention gate.",
                ["son55:E003", "son55:E007", "sol:E003"], NOSCORE),
            XC(p, "local:2603.02623-2", "same_supported_fact", "unmet",
               "son55's local-2 (no cross-task retention or reuse experiment) is the same question as sol's local-1. Both "
               "are unmet and merged here. son55's local-1 (discriminator accuracy) keeps its ID.",
               ["son55:E004", "sol:E010", "opus:O03"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "Verified: the update-off and constraint/trajectory ablations isolate parts of the conditioning. There is "
               "no same-VLM no-retrieval arm.", ["sol:E008", "opus:O05"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "Verified: there is no flat-index or nearest-neighbour alternative to the VerbNet hierarchy.",
               ["son55:E010", "son55:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "sol", "partial",
               "There is source sensitivity (Table IV) and a slice audit, but the source-to-test distribution gap is not "
               "characterised. son55's 'met' over-reads two-source coverage.", ["sol:E009", "sol:E011", "son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "revised", {"moved_to": "local:2603.02623-3", "status": "unmet"},
               "The card was not kept. The question (cost of the added structure) still applies and moves to local-3. "
               "Verified unmet.", ["son55:E006"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "revised", {"moved_to": "local:2603.02623-4", "status": "partial"},
               "The card was not kept. The question (fair comparison with simpler baselines) moves to local-4, partial: "
               "the basic skills are shared, but VLM training and retrieval are not.", ["son55:E010", "opus:O05"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "partial",
               "Verified: skill implementation is one stage inside planner, retrieval and visual prompting, and only "
               "coarse ablations exist.", ["son55:E009", "son55:E018"]),
            XC(p, "rsi:crystallize_executable_capability/F2", "son55", "partial",
               "Verified: new skills are VLM-chosen waypoints, not verifiable code. The planner's plan is code.",
               ["son55:E009"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "unmet",
               "Verified: admission uses VLM annotation plus out-of-view and inactivity filters, with no execution "
               "replay.", ["son55:E008", "son55:E020"]),
            XC(p, "rsi:crystallize_executable_capability/S2", "son55", "partial",
               "Verified: a new node is added when no match exists, with no test of whether it is an increment.",
               ["son55:E007"]),
            XC(p, "rsi:crystallize_executable_capability/S3", "son55", "partial",
               "Verified: tested on out-of-API RLBench and real tasks, but the tasks are author-chosen and there is no "
               "overlap audit.", ["son55:E012"]),
            XC(p, "rsi:crystallize_executable_capability/S5", "son55", "partial",
               "Verified: the update-off arm exists (Fig. 5, values image-only), but there is no same-VLM no-retrieval arm.",
               ["son55:E018"]),
            XC(p, "rsi:crystallize_executable_capability/S6", "son55", "met",
               "Verified: implementation is grounded in retrieved external demonstrations, and the source is varied in "
               "Table IV.", ["son55:E009", "son55:E019"]),
            XC(p, "rsi:index_experience_for_reuse/H04", "sol", "partial",
               "Verified: the hierarchy and local insertion are explicit. There is no flat-index or scaling-cost "
               "certification.", ["sol:E002", "sol:E003"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", 2, "See ratings.X: unnamed VLM and training recipe, "
                "missing thresholds, undefined L_ext persistence, one-line self-correction.",
                ["son55:E005", "opus:O03", "opus:O04", "opus:O05"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": 3, "son55_value": 3, "final_value": 2,
             "reason": "Both seats recorded Table III's 0.00 CaP average as an error but kept 3. Run convention: an "
                       "internal text–table contradiction caps E.measurement at 2 (r09b EvoRoute, r10b, r11a ReCreate). "
                       "The introduction's '+34.0% in unseen skills' also does not recompute (opus:O02).",
             "evidence_ids": ["opus:O01", "opus:O02", "son55:E016"], "score_impact": "−2.5 (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole pinned text first. Initial view: a boundary in-scope B "
                                                   "(offline video repository, gap-triggered skills, trained planner). G 3, "
                                                   "M 3, X 2 (VLM, thresholds and retention undefined). E: measurement 2 "
                                                   "(Table III CaP 0.00), causality 2 (trained VLM confound), holdout 2, "
                                                   "statistics 2, cost 0.",
            "integrity_checks": "Both seats a1 on 2603.02623v1, material sha 76eb7168…. Canonical seat hashes equal "
                                "conflicts.json. Both completed 15+31 and domain identification.",
            "core_claim_check": "Tables I–III averages recomputed. Uni-Skill and MOKA rows match, the CaP real-world average "
                                "does not (0.29 vs 0.00). The +31.0 sim claim is 0.41−0.10.",
            "rating_agreement": "G, M, Ec, Eh, Es and Ecost agree and were re-checked. Em was corrected for both seats. X "
                                "resolved to son55.",
        },
    }

    # =========================================================== 2603.02766 EvoSkill (equal 58.75)
    p = "2603.02766"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "The skill-merge configuration achieves the strongest result at 67.9% exact match (+7.3% over baseline), outperforming every individual run.",
                    "§3.1.3 Results",
                    "The headline (abstract, intro, Fig. 2) is the best of four configurations compared on the test "
                    "partition. merge-unique is a post-hoc combination of runs."),
            opus_ev(p, "O02", "we retain the version from the highest-performing run", "§3.1.2 Setup",
                    "The merge's conflict rule ranks runs by performance on an unnamed split. If it is the test split, "
                    "selection touched test data. Either way it is unreported."),
            opus_ev(p, "O03", "We evaluate three training set sizes: 5% (12 examples), 10% (24 examples), and 15% (36 examples)",
                    "§3.1.2 Setup",
                    "With validation fixed at 17 and the test equal to 'the remaining questions', the test partitions "
                    "differ across configurations (217/205/193). The single baseline 60.6 cannot be on all of them, "
                    "unless it was rerun per split, which is not stated.", kind="our_inference"),
            opus_ev(p, "O04", "the transferred skill improves accuracy from 43.5% to", "§3.3 Zero-Shot Skill Transfer",
                    "43.5% and 48.8% of 128 are 55.7 and 62.5 questions, not integers. The effective denominator or "
                    "averaging is unstated.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "reason": "Opus sides with son55. The paper's move frees a conventionally fixed component, the hand-authored "
                      "skill library, and makes it the evolved unit of a feedback-descent loop around a frozen agent. "
                      "That is the run convention for agent-harness evolution loops (r11a ReCreate, r03b SICA, r08b "
                      "Live-SWE: generative_process_redesign, sub null; C15/C23/C24 are representation, diffusion and "
                      "conditioning tactics and do not apply). sol's C03 is rejected: skills are loaded by trigger or "
                      "progressive disclosure, not retrieved as reference instances, and no category-holdout or "
                      "cheaper-conditioner logic is executed. C03 describes how the artifact is consumed, not the "
                      "paper's operation.",
            "executes_pattern": "partial", "resolves_problem": "unresolved",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("son55", p, "population_search_executable_fitness", "H15")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "generative_process_redesign", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "attribute_and_patch_incumbent", "sub": "H11"},
             "operation_correspondence": "Failures on training items are attributed (with gold answers) to a missing or "
                                         "deficient skill. A create/edit proposal is materialised as a skill folder and "
                                         "retained only if validation improves. The freed component (skill library) "
                                         "is edited by failure attribution.",
             "necessary_conditions/differences": "H11's defect-versus-lapse split and edit budget are absent. The "
                                                 "validation gate is 17 items on OfficeQA.",
             "evidence_ids": ["son55:E003", "son55:E007", "son55:E009"]},
            {"rs_main": "generative_process_redesign", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": "H15"},
             "operation_correspondence": "A top-k frontier of programs with a cumulative proposal history (outcomes and "
                                         "score deltas) conditions later proposals, as H15's search-memory layer does.",
             "necessary_conditions/differences": "The history's value is never measured (S5 unmet). The frontier is a "
                                                 "scalar top-k, not complementary (H16 rejected).",
             "evidence_ids": ["son55:E004", "son55:E007"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.02766-1"): "local:2603.02766-4",
                    ("sol", "local:2603.02766-2"): "local:2603.02766-5",
                    ("sol", "rs:adapt_via_conditioning/RE-1"): "rs:generative_process_redesign/RE-3",
                    ("sol", "rs:adapt_via_conditioning/RE-2"): "local:2603.02766-6",
                    ("sol", "rs:adapt_via_conditioning/RE-5"): "local:2603.02766-7"},
            overrides={
                "local:2603.02766-4": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = single-run "
                                               "statistics)."},
                "local:2603.02766-5": {"note": "sol's local-2 renumbered (A4 collision with son55's local-2 = best-of-"
                                               "configurations/merge partition)."},
                "rs:generative_process_redesign/RE-3": {
                    "status": "unmet",
                    "reason": "Opus: sol's adapt RE-1 (no prompt-only, history or frontier ablation) is merged here (A4; card "
                              "not kept). Proposer, Builder, frontier, history and meta-skill are introduced together, "
                              "with no per-component ablation. The no-skill baseline answers neither question."},
                "local:2603.02766-6": dict(conv("rs:adapt_via_conditioning/RE-2"), status="partial"),
                "local:2603.02766-7": dict(conv("rs:adapt_via_conditioning/RE-5"), status="partial"),
                "rs:generative_process_redesign/RE-1": {
                    "status": "partial",
                    "reason": "Opus revises son55's unmet. Removing the redesign collapses the gain: base vs evolved on the "
                              "held-out test (60.6 vs 63.4–68.1) is the reverse ablation. The claim that the prompt- or "
                              "code-level unit is the bottleneck is untested (prompt-only mode exists but is not "
                              "reported)."},
            }),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats, re-checked. Skills retained by the validation gate improve the disjoint "
                                   "test partition over the same frozen agent without skills, and one skill transfers "
                                   "unmodified to BrowseComp. This is weak retained: the headline is best-of-configs on "
                                   "test (opus:O01), and runs are single. Not improver: the proposer and builder are "
                                   "never changed.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Validation-gated skill folders evolved from 12–36 OfficeQA training items "
                                         "raise held-out exact match over the no-skill Claude Code baseline in each single "
                                         "run (63.4/65.8/64.5 vs 60.6; post-hoc merge 67.9/68.1). SealQA rises 26.6 → "
                                         "38.7. One unmodified search skill raises a 128-item BrowseComp sample 43.5 → "
                                         "48.8. 'Skill-level beats prompt/code-level' and generic transfer are untested.",
            "unresolved": ["Prompt-only and component controls", "Variance across runs", "Merge selection split "
                           "(opus:O02) and per-config test alignment (opus:O03)", "Transfer denominator (opus:O04)", "Cost"],
        },
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The hand-authored-skill gap is real. But the premise that "
                   "prompt- or code-level artifacts 'do not transfer' is asserted, not shown. The loop is Feedback "
                   "Descent applied to skills, and failure-driven skill-revision neighbours are not compared.",
                   ["son55:E002", "son55:E021", "sol:E003"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Failure diagnosis with gold labels on train only, "
                   "create/edit proposals, builder-only write access, a validation-gated frontier and a proposal "
                   "history form a coherent loop. Not 4: no prediction distinguishes skills from prompts, and the "
                   "17-item gate is weak (one item = 5.9 pp).", ["son55:E003", "son55:E004", "son55:E007", "son55:E025"],
                   ["son55:E009"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Git branch lineage, frontier tags, eviction, early stop, "
                   "prompts, scorer and failure threshold are specified. Not 4: parent selection contradicts itself "
                   "(round-robin in §2.2 vs highest-scoring in App. D), T and batch size are unstated, and the merge "
                   "rule's split is unnamed (opus:O02).", ["son55:E005", "son55:E006", "son55:E008", "sol:E013"],
                   ["sol:E012"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. OfficeQA uses a deterministic fuzzy scorer, and the "
                               "baseline is cross-checked with the benchmark authors. But the headline 67.9 contradicts "
                               "Table 1's 68.1 (son55:E014). The BrowseComp percentages imply non-integer counts of "
                               "128 (opus:O04), and substring matching and the SealQA LLM judge are unaudited. Run "
                               "convention: text–table contradictions cap at 2.",
                               ["son55:E017", "son55:E023", "sol:E011"], ["son55:E014", "opus:O04"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. In skill-only mode the child inherits the parent's "
                             "system prompt, so base vs evolved on the held-out test isolates the retained skill package. "
                             "The BrowseComp ± one-skill arm does the same. Not 3: there are no frontier, history or "
                             "meta-skill ablations and no budget-matched alternative optimizer, and the implemented "
                             "prompt-only mode is unreported (son55:E022). The skill-versus-prompt claim is untested.",
                             ["sol:E001", "sol:E006", "son55:E019", "son55:E020"], ["son55:E021", "son55:E022"]),
            "E.holdout": R("resolved", 2, "Shared correction 3 → 2. Train, validation and test are disjoint, and the test "
                           "is never used during evolution. But the headline +7.3 is the best of four configurations "
                           "compared on that test, and merge-unique was added post hoc (opus:O01). Its overlap rule keeps "
                           "'the version from the highest-performing run' on an unnamed split (opus:O02). Test partitions "
                           "differ across 5/10/15% while one baseline is quoted (opus:O03). The transfer is one skill, "
                           "one direction, one sample. Selection on the test set is scored here (A2), not in statistics.",
                           ["son55:E010", "son55:E024", "son55:E020", "opus:O01", "opus:O02", "opus:O03"], ["son55:E009"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2): sample sizes and a non-monotone 10%→15% result are "
                              "reported. Every configuration is a single run, with no intervals or tests (the authors say "
                              "so).", ["son55:E016", "son55:E015", "sol:E008"]),
            "E.cost": NR("Opus sides with sol. No iteration count T, proposer/builder/executor tokens, dollars or "
                         "wall-clock, and no inference overhead of skills vs base. '1.5 epochs' and 'computational cost' "
                         "are not accounting (precedent r09a: a hardware line alone is not_reported).",
                         ["son55:E011", "son55:E016"],
                         ["Opus: complete pinned v1 §1–5 and Appendices A–D (skills, scripts, prompts, scorer, branch "
                          "environment)", "no iteration count, token, dollar, time or call figure anywhere"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–D read. In scope (A): failure-driven evolution of non-weight "
                  "skill folders on a frozen agent, retained by a validation gate and used on disjoint test items. All "
                  "eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Fig. 2 duplicates Table 1. The Table 1 values were used and the 67.9/68.1 conflict is "
                             "recorded.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "generative_process_redesign",
                "See rs_pattern.reason: freeing the hand-fixed skill library inside a feedback-descent loop is the "
                "generative_process_redesign move (ReCreate/SICA convention). C03 only describes how skills are "
                "consumed.", ["son55:E002", "son55:E026"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["generative_process_redesign", None]],
                "Follows primary. No sub-card fits (C15/C23/C24 are 3D-representation, diffusion and conditioning "
                "tactics).", ["son55:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H11"], ["population_search_executable_fitness", "H15"]],
                "H11 is kept (both seats). For the population parent, sol's null sub is replaced by H15: the cumulative "
                "history of proposals, outcomes and score deltas conditions the proposer, which is H15's search-memory "
                "layer (low fit; its value is unmeasured). son55's H16 is rejected. H16 is defined by a complementarity "
                "axis, while EvoSkill's 'Pareto frontier' is a scalar top-k replacing the weakest member (son55 itself "
                "graded it 'nominal').", ["son55:E004", "son55:E007", "sol:E004"], NOSCORE),
            XC(p, "local:2603.02766-3", "son55", "unmet",
               "Verified: no T, tokens, dollars or time.", ["son55:E011", "son55:E016"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "revised",
               {"moved_to": "rs:generative_process_redesign/RE-3", "status": "unmet"},
               "The card was not kept. sol's question (no equal-budget prompt-only, history or frontier ablation) is the "
               "same as the kept card's RE-3 (and partly RE-2), so it is merged into RE-3. Final unmet: sol's 'partial' "
               "credited the no-skill baseline, which tests neither ablation.", ["sol:E003", "son55:E022"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "revised", {"moved_to": "local:2603.02766-6", "status": "partial"},
               "The card was not kept. The overlap question (separate test plus external transfer, merge-partition "
               "audit absent) moves to local-6 and stays partial (opus:O02).", ["sol:E005", "sol:E007", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "revised", {"moved_to": "local:2603.02766-7", "status": "partial"},
               "The card was not kept. The generality question (two domains, one transfer pair, no cross-model or "
               "cross-harness test) moves to local-7 and stays partial.", ["sol:E009", "sol:E010"]),
            XC(p, "rs:generative_process_redesign/RE-1", "revised", "partial",
               "son55's unmet is revised. The reverse ablation (remove evolved skills → baseline) exists on the held-out "
               "test. What is missing is evidence that the prompt- or code-level unit is the bottleneck.",
               ["son55:E021", "son55:E022", "sol:E001"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "unmet",
               "Verified: no GEPA or prompt-only comparison is reported, although prompt-only mode is implemented.",
               ["son55:E022"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", "unmet",
               "Verified: none of the five introduced components is ablated. sol's adapt RE-1 is merged here.",
               ["son55:E004", "son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "met",
               "Failure mode absent (son55 convention: met = avoided). Benchmark gold answers and the official scorer "
               "are used, not self-constructed validation.", ["son55:E003", "son55:E023"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11", "sol", "partial",
               "Verified: skill-level attribution is present. There is no defect/lapse split or edit budget.",
               ["sol:E002", "sol:E014"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H11.step2", "son55", "unmet",
               "Verified: every failure is treated as fixable by a skill edit. There is no lapse routing.",
               ["son55:E003", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: create-vs-edit at whole-skill granularity, not at the failing section.",
               ["son55:E003", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Verified: a candidate must beat the weakest frontier member, otherwise it is discarded. There is no "
               "per-item regression check, and the validation set is 17 items.", ["son55:E007", "son55:E009"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met",
               "Verified: the proposer sees traces, predictions, gold answers, the repository and the full proposal "
               "history.", ["son55:E003", "son55:E004", "son55:E025"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "unmet",
               "Verified: the gate, history and meta-skill are separable by design but never ablated.",
               ["son55:E004", "son55:E007"]),
            XC(p, "rsi:population_search_executable_fitness/S1", "son55", "partial",
               "Verified: the contribution is the evolved unit, not the search mechanism (Feedback Descent loop "
               "reused).", ["son55:E001", "son55:E007"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial",
               "Verified: OfficeQA uses a deterministic scorer. SealQA and BrowseComp use an unaudited LLM judge.",
               ["son55:E023"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "unmet",
               "Verified: the history's value is never measured, and the frontier names no complementarity axis.",
               ["son55:E004"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 2,
                "See ratings.E.measurement: the 67.9/68.1 contradiction and the non-integer BrowseComp rates. Run "
                "convention caps at 2. son55 recorded the contradiction but kept 3.", ["son55:E014", "opus:O04"],
                "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", 2,
                "See ratings.E.causality: the store-off comparison on the held-out test isolates the retained package. "
                "The missing component and alternative-optimizer controls bound it at 2, not 1. son55's 1 penalises "
                "the untested skill-vs-prompt claim, which RE-2/RE-3 record without zeroing the package evidence.",
                ["sol:E001", "sol:E006"], "+3.75 vs son55 (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "not_reported", "rating": 0},
                "No quantitative cost of any kind exists. A training-set fraction and epoch count do not account search "
                "or inference cost, and the 'computational cost' remark is a reason for not doing variance, not a "
                "figure.", ["son55:E011", "son55:E016"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout", "sol_value": 3, "son55_value": 3, "final_value": 2,
             "reason": "Both seats credited the disjoint three-way split and overlooked that the reported headline is "
                       "chosen on the test partition. merge-unique is a post-hoc fourth configuration announced as best "
                       "because it 'outperform[s] every individual run' on test (opus:O01). Its overlap rule keeps the "
                       "version from the 'highest-performing run' on an unnamed split (opus:O02). Per-config test sets "
                       "differ while one baseline is quoted (opus:O03). Under EVIDENCE.md rule 2 and A2, test-set "
                       "selection and partition alignment are E.holdout defects. With one-skill, one-direction transfer, "
                       "anchor 2 applies.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "son55:E012", "son55:E013"],
             "score_impact": "−2.5 (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole pinned text incl. App. A–D first. Initial view: in scope "
                                                   "(A). G 2, M 3, X 3 (parent-selection contradiction). E: measurement 2 "
                                                   "(67.9/68.1), causality 2 (store-off only), holdout 2 (headline chosen "
                                                   "on test), statistics 1 (single runs), cost 0.",
            "integrity_checks": "Both seats a1 on 2603.02766v1, material sha fe84f565…. Canonical seat hashes equal "
                                "conflicts.json. Both completed 15+31 and domain identification.",
            "core_claim_check": "Table 1 tolerance gaps recomputed against 'gains 2.7–4.5% at stricter tolerances' "
                                "(4.5/4.3/3.3/2.7, consistent). Exact-match deltas: +2.8/+5.2/+3.9, and merge +7.5 by the "
                                "table vs +7.3 by the text. BrowseComp counts are non-integer.",
            "shared_error_audit": "The equal 58.75 hid two compensating disagreements (Em, Ec, Ecost) and one shared "
                                  "over-credit (Eh). The final is 56.25.",
            "rating_agreement": "G, M, X and Es agree and were re-checked. Em, Ec and Ecost resolved to sol. Eh was "
                                "corrected for both seats.",
        },
    }

    # =========================================================== 2603.03329 AutoHarness (Δ5)
    p = "2603.03329"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Our work differs by offloading the state-transition validity checker to an external, verifiable program rather than relying on the model’s internal simulation.",
                    "§2 Related work", "The responsibility boundary: legality, which the LLM handles unreliably, is "
                                       "delegated to executable code checked against the environment (C25 step 1)."),
            opus_ev(p, "O02", "Our results show that using a smaller model to synthesize a custom code harness (or entire policy) can outperform a much larger model, while also being more cost effective.",
                    "Abstract", "The cost-effectiveness claim is backed by synthesis LLM-call counts (Table 1) and a "
                                "policy-mode test-time comparison. Verifier-mode retries are not costed."),
            opus_ev(p, "O03", "We measure the accuracy of the action filter by applying it to novel test rollouts",
                    "§4.1 Training", "The 100% legality figure measures the harness on new-seed rollouts. Whether those "
                                     "actions come from the code proposer or an LLM is not stated."),
            opus_ev(p, "O04", "The 32 games used for end-to-end agent eval are marked with *.", "Appendix A, Table 1 caption",
                    "Opus recomputed from Table 1: the 32 starred games average 14.5 learning steps, with 19 below 10, "
                    "while all 145 games average 10.3. This confirms son55:E009, so §4.1's '14.5' describes the "
                    "evaluated subset.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "matches": [smatch("son55", p, "decompose_and_delegate")],
            "reason": "Opus sides with son55. The LLM emits executable code (is_legal_action/propose_action), the "
                      "environment checks it, and that verdict drives construction-time refinement. At inference, "
                      "legality is offloaded to the code while the LLM keeps strategy (opus:O01). Every C25 element is "
                      "present: a typed, machine-checkable artifact, a sound checker, and the loop closed with its "
                      "output. It is also the run convention for tool and harness makers (LATM, Alita). sol's "
                      "generative_process_redesign is weaker: what is freed is not a component of a generative process "
                      "but a verification/control boundary, and sol itself found no sub-card.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H14"),
                                       dmatch("son55", p, "attribute_and_patch_incumbent", "H12")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "decompose_and_delegate", "rs_sub": "C25",
             "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": "H14"},
             "operation_correspondence": "Code is evolved by LLM mutation under Thompson-sampled tree search against "
                                         "the environment's legality/reward evaluator (H14). The retained program is "
                                         "the checkable artifact that C25 delegates to.",
             "necessary_conditions/differences": "The search algorithm is reused (Tang et al. 2024). There is no search "
                                                 "ablation (F1 partial).",
             "evidence_ids": ["son55:E004", "son55:E005", "son55:E023"]},
            {"rs_main": "decompose_and_delegate", "rs_sub": "C25",
             "domain": {"namespace": "rsi", "main": "attribute_and_patch_incumbent", "sub": "H12"},
             "operation_correspondence": "Failed steps with error messages are consolidated by a Critic, and the harness "
                                         "functions are patched (both or only propose_action, depending on which was "
                                         "wrong).",
             "necessary_conditions/differences": "There is no regression replay or rollback beyond the tree. At most "
                                                 "five failed steps are shown, not full traces.",
             "evidence_ids": ["sol:E002", "son55:E006"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.03329-1"): "local:2603.03329-4",
                    ("sol", "local:2603.03329-2"): "local:2603.03329-5",
                    ("sol", "rs:generative_process_redesign/RE-1"): "rs:decompose_and_delegate/RE-5",
                    ("sol", "rs:generative_process_redesign/RE-3"): "rs:decompose_and_delegate/RE-2",
                    ("sol", "rs:generative_process_redesign/RE-6"): "rs:decompose_and_delegate/RE-1"},
            overrides={
                "local:2603.03329-4": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = game-subset "
                                               "selection)."},
                "local:2603.03329-5": {"note": "sol's local-2 renumbered (A4 collision with son55's local-2 = legality "
                                               "measurement protocol)."},
                "rs:decompose_and_delegate/RE-5": {
                    "status": "partial",
                    "reason": "Opus: sol's gpr RE-1 (no equal-retry control) is merged here (A4). Same-model Flash vs "
                              "Flash+harness and stronger models are compared, but retry budget is not aligned and there "
                              "is no hand-written-harness or legal-moves-hint baseline."},
                "rs:decompose_and_delegate/RE-2": {
                    "status": "unmet",
                    "reason": "Opus: sol's gpr RE-3 is merged here (A4). There is no tree-search vs linear refinement, "
                              "Critic-off or feedback-content ablation."},
                "rs:decompose_and_delegate/RE-1": {
                    "status": "partial",
                    "reason": "Opus: sol's gpr RE-6 is merged here (A4). Per-game LLM-call counts for synthesis (Table 1) "
                              "and a policy-mode test-time comparison exist. Verifier-mode retry calls and synthesis "
                              "tokens/dollars do not."},
                "rs:decompose_and_delegate/RE-3": {
                    "status": "partial",
                    "reason": "Opus revises son55's met. The policy prompt, refinement prompt, signatures and code excerpts "
                              "are given, but the Critic (error-consolidation) prompt and the Thompson prior are not."},
                "local:2603.03329-2": {
                    "status": "unmet",
                    "reason": "Opus revises son55's 'unknown'. The text is complete and does not say whose actions the "
                              "legality test scores (opus:O03), nor report checker recall on LLM proposals or false "
                              "rejection. A reporting requirement left unanswered in complete material is unmet."},
                "local:2603.03329-3": {
                    "status": "unmet",
                    "reason": "Opus revises son55's 'unknown'. Gameplay uses 'random seeds' with no statement that they "
                              "differ from training seeds. This matters for reward-trained harness-as-policy on puzzle "
                              "instances. Not reported in complete material, so unmet."},
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, ["Verifier-mode retry cost vs single-call baselines (opus:O02)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus sides with son55. Illegal actions are a sourced bottleneck (78% of Flash losses in "
                   "Kaggle GameArena chess), and the replaced object (a hand-written harness) is explicit. Neighbours "
                   "are named with stated differences: code world models (Lehrach 2025), code-as-policies, Voyager, "
                   "Eureka, AlphaEvolve, and the Tang 2024 search. Not 4: none is compared, and action-applicability "
                   "work is only footnoted.", ["son55:E002", "son55:E003", "son55:E023", "opus:O01"], ["sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Environment legality and reward feedback → Critic → LLM code "
                   "refinement → Thompson-sampled node choice targets the illegal-move failure directly. Three harness "
                   "forms are delimited. Not 4: no prediction distinguishes tree search from plain refinement.",
                   ["son55:E004", "son55:E005", "son55:E006", "sol:E002"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Rollout settings, stopping rule, signatures, refinement "
                   "prompt and code excerpts are given, and scope boundaries are clear (free-text games excluded, policy "
                   "mode 1P only). Not 4: the Critic prompt, Thompson prior and sandboxing are absent.",
                   ["son55:E006", "son55:E007", "son55:E027", "sol:E004"], ["son55:E026"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Legality and reward are judged by the environment, "
                               "and 2P matches are seat-balanced. The learning-step statistics recompute for the "
                               "32-game subset (opus:O04). Not 4: the legality-test protocol does not say whose actions "
                               "are scored (opus:O03), and per-game results are figure-only.",
                               ["son55:E005", "son55:E013", "sol:E007", "opus:O04"], ["opus:O03"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Flash vs Flash+harness with the same optimized "
                             "prompt attributes the gain to the harness. But verifier retries add LLM calls the baseline "
                             "lacks, there are no search, Critic or feedback ablations, and there is no hand-written "
                             "harness or hints baseline.", ["son55:E014", "son55:E015", "son55:E022"],
                             ["son55:E016", "sol:E003"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Legality is tested on 10 new seeds per game. The "
                           "selection of 32 of 145 games is unexplained, gameplay seeds are not stated to be disjoint from "
                           "training, and reward-trained policy mode is evaluated on the same 16 games.",
                           ["son55:E010", "son55:E012", "sol:E007"], ["son55:E017"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2): match counts (20/40; 10/5 for GPT-5.2) are given. There "
                              "are no intervals, no synthesis-run repeats, and no test for the 0.870 vs 0.844 gap.",
                              ["son55:E013", "son55:E018", "sol:E015"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Synthesis effort is reported per game for all 145 games "
                        "(learning steps, i.e. LLM calls) with means 14.5 and 89.4, and test-time cost is compared in "
                        "policy mode (≈0 vs $640). Not 3: synthesis tokens and dollars and verifier-mode retry calls "
                        "are missing, so the main mode's cost-effectiveness claim (opus:O02) is only partly accounted.",
                        ["son55:E008", "son55:E017", "son55:E021", "opus:O02"], ["son55:E016"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. appendices read. In scope (B): per-game executable harnesses are "
                  "synthesised from environment feedback, retained, and reused in later games. Recursive self-improvement "
                  "is explicitly future work. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 2–7 (per-game curves, win/loss bars, per-game rewards) are image-only. Ratings use the "
                             "prose aggregates (56.3%/38.2%, 0.745/0.707/0.673, 0.870/0.844) and Table 1.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "See rs_pattern.reason: a checkable code artifact plus an environment verifier closing the loop is "
                "C25's move.", ["son55:E004", "son55:E005", "opus:O01"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["decompose_and_delegate", "C25"]],
                "Follows primary. C25 is under its own parent (PARENTS.tsv).", ["son55:E005", "opus:O01"], NOSCORE),
            XC(p, "local:2603.03329-1", "revised",
               {"local:2603.03329-1": "unmet (son55: game-subset selection)",
                "local:2603.03329-4": "partial (sol: finite-sample legality / soundness)"},
               "A4 collision: different questions under one ID. son55's local-1 keeps the ID, unmet (verified: no "
               "selection criterion for 32 of 145 games). sol's local-1 moves to local-4, partial (verified: legality "
               "is 100% on finite new-seed rollouts, with no soundness or false-rejection analysis).",
               ["son55:E012", "sol:E007", "sol:E008"]),
            XC(p, "local:2603.03329-2", "revised",
               {"local:2603.03329-2": "unmet (son55's question; 'unknown' revised)",
                "local:2603.03329-5": "met (sol: verifier and policy results reported separately)"},
               "A4 collision. son55's local-2 keeps the ID. Its 'unknown' is revised to unmet, because the complete text "
               "never states the protocol (opus:O03). sol's local-2 moves to local-5, met (verified: §4.2 and §4.3 "
               "separate the two modes, and the recursive library is future work).",
               ["son55:E010", "opus:O03", "sol:E013", "sol:E017"]),
            XC(p, "local:2603.03329-3", "revised", "unmet",
               "son55's 'unknown' is revised to unmet: train/eval seed disjointness for gameplay is not reported in "
               "complete material. The rating impact is already in E.holdout=2.", ["son55:E017", "son55:E019"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "same_supported_fact", "partial",
               "son55's RE-1 and sol's gpr RE-6 ask the same cost question. Both are partial and merged.",
               ["son55:E008", "son55:E021", "sol:E016"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "same_supported_fact", "unmet",
               "son55's RE-2 and sol's gpr RE-3 ask the same component-ablation question. Both are unmet and merged.",
               ["son55:E004", "sol:E001"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "revised", "partial",
               "Most prompts and signatures are disclosed, but the Critic prompt and Thompson prior are not. son55's "
               "'met' over-reads the disclosure.", ["son55:E026", "sol:E004"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: 145 games, but all from one TextArena framework with free-text games excluded.",
               ["son55:E012", "son55:E027"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "same_supported_fact", "partial",
               "son55's RE-5 (unaligned budget, no hand-written baseline) and sol's gpr RE-1 (no equal-retry control) "
               "are the same fairness question. Both are partial and merged.", ["son55:E016", "son55:E022", "sol:E003"]),
            XC(p, "rs:generative_process_redesign/RE-1", "revised",
               {"moved_to": "rs:decompose_and_delegate/RE-5", "status": "partial"},
               "The card was not kept. The equal-retry question merges into the kept card's RE-5.", ["sol:E003"]),
            XC(p, "rs:generative_process_redesign/RE-3", "revised",
               {"moved_to": "rs:decompose_and_delegate/RE-2", "status": "unmet"},
               "The card was not kept. The component-ablation question merges into RE-2.", ["sol:E001", "sol:E004"]),
            XC(p, "rs:generative_process_redesign/RE-6", "revised",
               {"moved_to": "rs:decompose_and_delegate/RE-1", "status": "partial"},
               "The card was not kept. The cost/trade-off question merges into RE-1.", ["sol:E006", "sol:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "Verified: failure-scoped function repair exists. There is no regression replay or rollback, and at most "
               "5 failed steps are summarised.", ["sol:E002", "sol:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: the proposer sees code plus a Critic summary of at most 5 failed steps, not full traces or "
               "history.", ["son55:E006"]),
            XC(p, "rsi:population_search_executable_fitness/F1", "son55", "partial",
               "Verified: the search is reused from Tang et al. The novelty is the target (the harness) and its coverage "
               "of 145 games.", ["son55:E023"]),
            XC(p, "rsi:population_search_executable_fitness/H14", "sol", "partial",
               "Verified: executable mutation with Thompson sampling. There are no repeated syntheses or search "
               "comparisons.", ["sol:E001", "sol:E005"]),
            XC(p, "rsi:population_search_executable_fitness/H14.step5", "son55", "partial",
               "Verified: legality is tested on new seeds. The reward-eval split is unstated, and there is no variance.",
               ["son55:E010", "son55:E013"]),
            XC(p, "rsi:population_search_executable_fitness/S1", "son55", "partial",
               "Verified: the contribution is the application and the harness forms, not the search level.",
               ["son55:E004", "son55:E023"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "met",
               "Verified: the environment legality and reward evaluator exists before the loop and is hard to game.",
               ["son55:E005", "son55:E007"]),
            XC(p, "rsi:population_search_executable_fitness/S3", "son55", "met",
               "Verified: two fixed-signature functions inside a fixed rejection-sampling scaffold.",
               ["son55:E004", "son55:E005"]),
            XC(p, "rsi:population_search_executable_fitness/S4", "son55", "met",
               "Verified: mutations are conditioned on environment-observed legality violations.",
               ["son55:E005", "son55:E006"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 3, "See ratings.G: the bottleneck is sourced and neighbours are "
                "named with distinctions, though not compared. sol's 2 penalises the reused search lineage, which is "
                "not the claimed gap (the claimed gap is the hand-written harness).", ["son55:E002", "opus:O01"],
                "+3.75 vs sol (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 2, "See ratings.E.cost: per-game synthesis call "
                "counts for all 145 games plus a policy-mode test-time comparison are substantive accounting. Retries "
                "and synthesis dollars are missing.", ["son55:E008", "son55:E021", "opus:O02"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole pinned text incl. App. A–D first. Initial view: in scope "
                                                   "(B, retained per-game harness). G 3, M 3, X 3. E: measurement 3, "
                                                   "causality 2 (retry budget, no search ablation), holdout 2 (game subset "
                                                   "and seed split), statistics 1, cost 2 (per-game call counts).",
            "integrity_checks": "Both seats a1 on 2603.03329v1, material sha 8695c22d…. Canonical seat hashes equal "
                                "conflicts.json. Both completed 15+31 and domain identification. The domain matches "
                                "agree.",
            "core_claim_check": "son55's Table 1 recomputation verified (opus:O04). 2P rates are 56.3 + 38.2 with 5.5% "
                                "draws. 'Prevents all illegal moves' rests on code-driven new-seed rollouts (opus:O03).",
            "rating_agreement": "M, X, Em, Ec, Eh and Es agree and were re-checked. G and Ecost resolved to son55.",
        },
    }

    return S
