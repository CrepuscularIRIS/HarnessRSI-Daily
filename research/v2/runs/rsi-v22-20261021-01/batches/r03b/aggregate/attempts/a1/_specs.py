"""Opus rulings for r03b a1 (data only; consumed by _build.py)."""
import copy

VER = "rsi-cards@52ff9657"
EIGHT = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")


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

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev, "none (expectations are not scored directly)")

    # =========================================================== 2504.07952 Dynamic Cheatsheet
    p = "2504.07952"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Similarly, GPT-4o managed a baseline of 20.0% but fell to 6.7% using FH", "§4.3",
                    "Prose contradicts Table 2 (GPT-4o AIME 2024: BL 20.0, FH 13.3, DC-RS 40.0; 6.7 is not in the row)."),
            opus_ev(p, "O02", "AIME 2024 23.3 26.7 50.0 20.0 13.3 40.0", "Table 2 (whitespace-normalised)",
                    "Table 2 values used as the record of fact (FH 13.3 for GPT-4o AIME 2024)."),
            opus_ev(p, "O03", "provided a 20.0% boost, but both DC-Cu and DC-RS performed worse than baseline", "§4.5",
                    "Third prose/table mismatch: Table 3 GPT-4o-mini AIME 2024 is BL 16.7 → DC-∅ 20.0 (+3.3 points), not a 20.0% boost."),
            opus_ev(p, "O04", "is an even more flexible metric that evaluates whether the model’s output satisfies the task-specific constraints",
                    "§3.3.1", "AIME/Game of 24/Equation Balancer are scored by a 'flexible' Functionally Correct checker whose rules are not given."),
            opus_ev(p, "O05", "does not have access to ground-truth labels; so, it has to assess the correctness and efficiency of the solutions by itself before updating the memory",
                    "§2.1.2", "Write gate is the curator's self-judgment; evaluation is prequential on the same stream (no labels leak, but no frozen/held-out memory)."),
            opus_ev(p, "O06", "values such as 5 and 7, but the gain was insignificant.", "§2.2 footnote 2",
                    "Retrieval k was chosen from preliminary runs on an unspecified set."),
            opus_ev(p, "O07", "Consequently, tasks arranged to present", "§4.6",
                    "Authors state order shapes the gain; only one ordering is reported."),
            opus_ev(p, "O08", "MV slightly underperformed (33.3% vs. 36.7%). In contrast, DC-Cu outperformed MV, reaching 50.0% on AIME 2024 and 36.7% on AIME 2025.",
                    "§5 / Table 4", "A 3-sample MV over the same structured prompt (DC-∅) is a partial extra-compute control; DC-Cu still wins on AIME."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "A frozen black-box LM is conditioned on a self-curated text memory (DC-Cu) or on curated memory plus retrieved "
                      "past (x, ỹ) pairs (DC-RS); no parameters change. C03 is not assigned: its load-bearing elements (one canonical "
                      "conditioning schema learned in an upstream phase, category-level holdout) are absent, and its retrieval sub-move "
                      "covers only DC-RS's retrieval, not the curation that is the paper's contribution (same ruling as r02b MobileSteward).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial (in-stream gains on strong models; no held-out or variance)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                dmatch("son55", p, "index_experience_for_reuse", "H03"),
            ],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2504.07952-4"): "local:2504.07952-3",
                    ("son55", "local:2504.07952-5"): "local:2504.07952-4",
                    ("son55", "local:2504.07952-3"): "local:2504.07952-5"},
            overrides={"rsi:abstract_experience_into_guidance/H01-step5": {
                "status": "partial",
                "reason": "Opus revision of son55 'unmet'. H01 step 5 asks to ablate the curator and separate construction from "
                          "evaluation. DR (retrieval without curation, all tasks) vs DC-RS and FH (uncurated full history, AIME only) vs "
                          "DC-Cu do remove the curation step; what is missing is a fixed/alternative curator and a separate "
                          "construction stream (opus:O05). Partial, not unmet."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Memory written from earlier test items is read on later ones, and DC-∅ (same structured prompt, "
                                   "empty memory) isolates its effect (e.g. Claude AIME 2024 36.7→50.0, GPT-4o Game of 24 19→99). "
                                   "Construction stream = evaluation stream (prequential, label-free); no frozen-memory or held-out "
                                   "evaluation, so not improver/transfer.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single run, one ordering: on Claude 3.5 Sonnet and GPT-4o a label-free, "
                                         "self-curated text memory raises accuracy over the same-prompt empty-memory control on "
                                         "AIME, GPQA (Claude), Game of 24 (GPT-4o) and Math Equation Balancer, with largest gains "
                                         "where a reusable code routine exists; no or negative gain for GPT-4o on knowledge tasks and "
                                         "for smaller models. The abstract's 'more than doubled' is against the minimal-prompt BL. Not reproduced.",
            "unresolved": ["Order/seed variance (single run; order said to matter, opus:O07).",
                           "Curator vs alternative abstraction/editing scheme under equal budget.",
                           "Three prose-vs-table number mismatches (son55:E018, opus:O01, opus:O03); Table values used."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The fixed object (static retrieval corpus / raw history; no cross-query "
                   "curation) is named, but the closest memory neighbours (Buffer-of-Thoughts, Thought-Retriever, MemPrompt, "
                   "Reflexion) are distinguished only in related-work prose, and 'no weight updates' carries much of the framing.",
                   ["son55:E027", "son55:E028", "son55:E029", "sol:E009"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Generation/curation split and the DC-Cu vs DC-RS ordering are explicit and "
                   "make checkable predictions against DC-∅, DR and FH (curated > raw retrieval/history > empty), plus the "
                   "capacity dependence that is observed. The self-judged write gate (opus:O05) is the weak assumption.",
                   ["son55:E004", "son55:E005", "son55:E008", "sol:E003", "opus:O05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Write/refine/delete/merge are left to the curator prompt and the whole memory "
                   "is rewritten each step (truncation observed by the authors); no external gate, versioning, rollback or conflict rule.",
                   ["son55:E003", "son55:E025", "sol:E007"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Ground-truth answers make the underlying verifiers credible, but the "
                               "'Functionally Correct' checker used for AIME/Game of 24/Balancer is undefined beyond 'flexible' "
                               "(opus:O04), and the prose contradicts the tables three times: GPQA GPT-4o DC-RS 58.1 vs Table 1 57.1 "
                               "(son55:E018 vs son55:E013), GPT-4o FH 'fell to 6.7%' vs Table 2 13.3 (opus:O01/O02, found by sol), and "
                               "GPT-4o-mini '20.0% boost' for +3.3 points (opus:O03). sol's 3 counted only one mismatch.",
                               ["son55:E011", "son55:E013", "son55:E018", "opus:O01", "opus:O02", "opus:O03", "opus:O04"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. The store-off control keeps the identical structured prompt (DC-∅), "
                             "retrieval-without-curation (DR) is run on every task, uncurated full history (FH) on AIME, and a 3-sample "
                             "MV over DC-∅ partly controls extra compute (opus:O08); together these rule out the prompt and simple "
                             "retrieval explanations for the main gains. Not 4: no budget-matched alternative curator, DR ≈ DC on some "
                             "cells (Claude AIME 2020–24 39.1 vs 38.4/40.6), FH only on AIME. sol's 2 under-credits these controls.",
                             ["son55:E008", "son55:E010", "son55:E016", "son55:E019", "son55:E022", "opus:O08"], ["son55:E016"]),
            "E.holdout": R("resolved", 1, "Shared-error correction (both seats 2). Memory is built from the evaluated stream itself "
                           "(prequential; no labels, opus:O05), with no frozen-memory or independent held-out evaluation, no "
                           "contamination check on AIME/GPQA, k chosen on an unspecified set (opus:O06), one ordering whose effect the "
                           "authors acknowledge (opus:O07), and cross-model memory transfer reported only as 'mixed'. This is the same "
                           "situation rated 1 for in-stream memory in SE-GPT (r01b 2407.08937) and Buffer-of-Thoughts (r01b 2406.04271).",
                           ["son55:E007", "son55:E006", "son55:E031", "opus:O05", "opus:O06", "opus:O07"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes (30/133/100/198/250) and negative results are "
                              "reported; every number is one run with no interval; ±4 AIME questions move 13 points.",
                              ["son55:E011", "son55:E020", "sol:E011"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only Claude AIME 2024 tokens per item (370/494/1035/1831); no call "
                        "counts, curator/embedding cost or totals; DC-Cu ≈5× BL tokens while the paper calls maintenance a net gain.",
                        ["son55:E023", "son55:E024", "sol:E008"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. appendices (figure images not in text; no judgment depends on them); in scope (A): "
                  "retained non-weight memory written from executions and read on later items; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "C03 requires a canonical conditioning schema taught upstream and category-level holdout; neither exists, and its "
                "retrieval sub-move only covers DC-RS retrieval, not curation. Parent match kept, sub null (r02b precedent).",
                ["son55:E005", "sol:E003"], "none (patterns never score)"),
            X(p, "local:2504.07952-4", *C(p, "expectations[local:2504.07952-4].status"), "revised",
              "local-4 = sol's cost question → partial; son55's local-4 (order/seed variance) renumbered to local-3 = unmet",
              "A4 collision: same ID, different questions. sol local-4 (token means only, partial) and son55 local-5 (single-benchmark "
              "token mean, partial) are the same cost question → merged as local-4; son55 local-4 is the statistics question that "
              "sol filed as local-3 (both unmet) → merged as local-3.", ["sol:E008", "son55:E023", "son55:E031"]),
            X(p, "local:2504.07952-5", *C(p, "expectations[local:2504.07952-5].status"), "same_supported_fact",
              "merged into local:2504.07952-4 = partial; final local-5 now holds son55's former local-3 (MV budget unmatched) = unmet",
              "son55 local-5 asks the cost question sol answered as local-4 with the same value (partial).", ["son55:E023", "sol:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55", "unmet",
              "Verified: no contamination/overlap analysis anywhere; applies because the paper argues transfer across questions.",
              ["son55:E007"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55", "met",
              "Verified: nearest-neighbour retrieval (DR, all tasks) and longer raw context (FH, AIME) are both run.",
              ["son55:E010", "son55:E019"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55", "partial",
              "Verified: sensitivity to memory quality discussed by model size and retrieval noise; no controlled sweep; transfer 'mixed'.",
              ["son55:E020"]),
            X(p, "rsi:abstract_experience_into_guidance/F1", *C(p, "expectations[rsi:abstract_experience_into_guidance/F1].status"),
              "son55", "partial", "Verified: abstract foregrounds 'without modifying their underlying parameters', but curation vs "
              "append is also made a concrete claim.", ["son55:E001", "son55:E002"]),
            X(p, "rsi:abstract_experience_into_guidance/H01-step5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H01-step5].status"), "revised", "partial",
              "DR vs DC-RS and FH vs DC-Cu remove the curation step (a curator ablation in the H01 sense); missing are an "
              "alternative/fixed curator and a separate construction stream. Partial.", ["son55:E010", "son55:E019", "opus:O05"]),
            X(p, "rsi:abstract_experience_into_guidance/S1", *C(p, "expectations[rsi:abstract_experience_into_guidance/S1].status"),
              "son55", "partial", "Verified: static retrieval corpus and raw history are named as the fixed things, alongside the "
              "frozen-weights framing.", ["son55:E002", "son55:E027"]),
            X(p, "rsi:abstract_experience_into_guidance/S2", *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"),
              "son55", "unmet", "Verified: curation reads one answer at a time; no success/failure contrast step.", ["son55:E004"]),
            X(p, "rsi:abstract_experience_into_guidance/S5", *C(p, "expectations[rsi:abstract_experience_into_guidance/S5].status"),
              "son55", "unmet", "Verified: no execution test, quality filter or versioned merge gates retention (opus:O05).",
              ["son55:E003", "opus:O05"]),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: undefined FC checker plus three prose/table mismatches.",
                ["son55:E018", "opus:O01", "opus:O03", "opus:O04"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.causality: same-prompt store-off, DR on all tasks, FH and MV controls.",
                ["son55:E008", "son55:E010", "opus:O08"], "+3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout", "sol_value": {"status": "resolved", "rating": 2},
             "son55_value": {"status": "resolved", "rating": 2}, "final_value": {"status": "resolved", "rating": 1},
             "correction": "Both seats 2. In-stream, label-free memory with no frozen/held-out evaluation, no contamination audit, "
                           "k tuned on an unspecified set and a single acknowledged-order-sensitive stream is rated 1 under the frozen "
                           "rubric's applied precedent (SE-GPT r01b 2407.08937; BoT r01b 2406.04271).",
             "evidence_ids": ["opus:O05", "opus:O06", "opus:O07", "son55:E007"], "score_impact": "−2.5 vs both seats (10×1/4)"},
            {"field_path": "expectations[local:2504.07952-3]", "sol_value": "unmet — statistics: no seeds/order intervals",
             "son55_value": "unmet — cost: MV vs DC budget unmatched",
             "correction": "Same ID used by both seats for different questions (A4 collision hidden by equal status). sol's kept as "
                           "local-3 (son55's own statistics question merged in); son55's budget question renumbered local-5.",
             "evidence_ids": ["sol:E011", "son55:E022"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): self-curated text memory, label-free, written and read along the "
                                                   "test stream. DC-∅ is the right store-off control; memory gains over DC-∅ are few "
                                                   "items on AIME (+4/30) and GPQA (+17/198), large on Game of 24 and Balancer; single "
                                                   "run/order; prequential, no frozen holdout; cost only as AIME-2024 token means; "
                                                   "several prose/table mismatches.",
            "integrity_checks": "Both seats a1 on 2504.07952v1, material sha c9856e09…, input_hash 70591124…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids/parents valid.",
            "controller_flag_58_1": "son55 quoted the §4.2 sentence (son55:E018: DC-RS 57.1→58.1) verbatim and recorded it as a "
                                    "contradiction of Table 1 (son55:E013: DC-Cu 58.1, DC-RS 57.1) in E.measurement and as "
                                    "counterevidence to its claim C3; its claims use the Table values (GPT-4o no GPQA gain). Not a seat "
                                    "error; the final record uses Table 1 and adds two further mismatches (opus:O01, opus:O03).",
            "core_claim_check": "Re-read §2–§5 and Tables 1–4; recomputed per-question counts (AIME 15/30 vs DC-∅ 11/30; GPQA "
                                "136/198 vs 119/198) and DC-∅ deltas.",
            "rating_agreement": "6/8 identical; E.measurement → son55 (2), E.causality → son55 (3); E.holdout 2→1 as shared error.",
            "expectation_renumbering": "son55 local-4→local-3, local-5→local-4 (merged with sol), local-3→local-5.",
        },
    }

    # =========================================================== 2504.15228 SICA
    p = "2504.15228"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "takes the best performing agent from the archive up until this point as the meta-agent, which is instructed to look through the archive",
                    "§3", "Promotion = argmax utility over the archive, computed on the benchmark set B that is also reported."),
            opus_ev(p, "O02", "looks at the best performing benchmark problems in a given iterations to understand success cases, as well as the worst performing benchmark problems at a given iteration to understand the failure modes",
                    "Appendix B", "The improver reads per-problem failures of the very benchmark it is later reported on."),
            opus_ev(p, "O03", "from which we select a fixed random subset of 50 questions", "§4",
                    "One fixed 50-question SWE-Bench Verified subset for all 15 iterations."),
            opus_ev(p, "O04", "0.17 0.17 0.65 0.65 1.91", "Table 1 iteration 0 (whitespace-normalised)",
                    "SWE-Bv 0.17 of 50 questions = 8.5 solved; likewise 0.51 (iter 15) = 25.5 and 0.53 (iter 14) = 26.5. Accuracies "
                    "are not integer proportions of the stated denominator and the aggregation (repeats/partial credit) is never stated."),
            opus_ev(p, "O05", "0.53 0.53 0.67 0.67 2.20", "Table 1 iteration 14 (whitespace-normalised)",
                    "The headline 53% is the peak of a noisy series (iter 13 = 0.27, iter 15 = 0.51), not the final agent."),
            opus_ev(p, "O06", "the tools, sub-agents and oversight mechanisms were all amenable to self-improvement", "§3.1",
                    "The overseer is inside the editable surface; no immutable anchor is named."),
            opus_ev(p, "O07", "defined and curated entirely within the agent’s codebase", "§4",
                    "The two synthetic benchmarks (part of the utility) live in the editable codebase."),
            opus_ev(p, "O08", "much of the initial improvement we report arises from features speeding up file editing and agent cost",
                    "§5.1", "Under a 300 s timeout, accuracy partly measures speed; authors attribute early gains to speed/cost features."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "The move is to treat the conventionally fixed component of an iterative agent-design loop — ADAS's separate, "
                      "fixed meta-agent — as a free design variable (the agent edits its own improver code). This is the literal "
                      "generative_process_redesign signature ('identify a conventionally-fixed component of an iterative/staged "
                      "procedure → treat it as a free design variable'). assumption_audit_and_pivot targets an assumption a guarantee "
                      "or defense rests on; ADAS's separation is a design default, not a load-bearing assumption of a result. Sub null "
                      "(C15/C23/C24 are geometry/diffusion specific).",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": "partial", "resolves_problem": "not shown (no fixed-improver control)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                dmatch("son55", p, "make_the_improver_editable", "H19",
                       condition_checks="S1 partial; S2 partial; S3 unmet; S4 met; S5 partial; F2 partial; F3 unmet (present); "
                                        "F4 unmet (present); F5 unmet (anchor not established: overseer and synthetic benchmarks "
                                        "editable, opus:O06/O07). H20 elements present but not load-bearing: all iterations archived "
                                        "and the archive informs edits (H20 steps 3–4), parent selection is greedy argmax (H20 step 2 "
                                        "absent) — functionally a single elitist lineage, so H19 is the best-fitting sub.",
                       evidence_ids=["son55:E002", "son55:E007", "son55:E008", "son55:E010", "son55:E009", "opus:O01", "opus:O06"]),
                dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
            ],
            "unassigned": [],
            "revision_proposals": [
                "son55 (endorsed): state in H19/H20 'when to pick' where an archive-with-greedy-argmax parent rule belongs (stage end).",
                "A5 leak: H20 step 4 and the make_the_improver_editable success conditions quote 'about $7000 for fifteen iterations' "
                "— this paper's own figure. Rewrite as a member-free check question (stage end; not used as evidence here)."],
        },
        "pattern_mapping": [
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "make_the_improver_editable", "domain_sub": "H19",
             "operation_correspondence": "Fixed meta-agent of the iterative design loop → editable; the best agent edits its own codebase.",
             "necessary_conditions_and_differences": "RS card wants the freed component shown to be the bottleneck by ablation; H19 "
                                                     "wants a named anchor, improver scored by its products and a fixed-improver "
                                                     "comparison — none fully present.",
             "evidence_ids": ["son55:E003", "son55:E007", "opus:O01"]},
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "attribute_and_patch_incumbent", "domain_sub": "H12",
             "operation_correspondence": "Archive explorer reads best/worst problems of the incumbent, then a developer sub-agent patches tools.",
             "necessary_conditions_and_differences": "No falsifiable patch prediction or replay regression gate; regression is "
                                                     "judged on the selection benchmark.",
             "evidence_ids": ["opus:O02", "son55:E019"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2504.15228-1"): "local:2504.15228-3",
                    ("son55", "local:2504.15228-2"): "local:2504.15228-4",
                    ("son55", "rsi:make_the_improver_editable/H20-step5"): "rsi:make_the_improver_editable/H19-step4"},
            overrides={
                "local:2504.15228-4": {
                    "status": "met",
                    "reason": "Opus revision of son55 'challenged_with_evidence'. The question is whether the paper reports where "
                              "self-improvement does not help; it does (AIME/GPQA run, Fig. 4, near-flat). The paper never claims gains "
                              "on reasoning tasks, so nothing is 'challenged'; the boundary is reported (met)."},
                "rsi:make_the_improver_editable/F5": {
                    "status": "unmet",
                    "reason": "Opus revision of son55 'unknown'. The text states the oversight mechanisms are amenable to "
                              "self-improvement (opus:O06) and the synthetic benchmarks are defined inside the agent codebase "
                              "(opus:O07); no immutable anchor is named. Whether the agent exploited this is unknown, but the "
                              "anchor-leak condition is present by design."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "EVIDENCE.md: selection set = reported set caps the level at task. Edits persist and are reused, "
                                   "but no independent task shows the retained edits help.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, one 15-iteration run (~$7,000): agents promoted by argmax utility on a fixed "
                                         "50-question SWE-Bench Verified subset, 50 LiveCodeBench items and two synthetic tasks score "
                                         "higher on those same items than iteration 0 (SWE-Bv 0.17→0.51 final, 0.53 peak), with much of "
                                         "the early gain from faster editing under a 300 s timeout; no gain on AIME/GPQA. No held-out "
                                         "set, fixed-improver control, ablation or repeat; compounding self-improvement is not shown.",
            "unresolved": ["SWE-Bv accuracies are not integer proportions of 50 (opus:O04); aggregation unstated.",
                           "Held-out evaluation, independent lineages, fixed meta-agent comparison."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The fixed object is named with a source (ADAS's separate, fixed meta-agent "
                   "editing one DSL forward function) and neighbours are listed, but the closest self-referential neighbours "
                   "(Gödel Agent, STOP) already let the improver modify itself; the residue claimed against them is scope "
                   "(full Python codebase, coding benchmarks), and the stake ('hopefully compounding') is asserted. Real gap, "
                   "incomplete residual against the nearest neighbours = anchor 2; son55's 3 takes the authors' distinctions at face value.",
                   ["son55:E003", "son55:E005", "son55:E006", "sol:E001", "sol:E002"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Archive → archive analysis of best/worst problems → edit own code → "
                   "evaluate → argmax promotion is reconstructable with a multi-objective utility; the key hypothesis (self-reference "
                   "compounds) is not turned into a distinguishing prediction.",
                   ["son55:E007", "son55:E008", "son55:E002", "opus:O01", "opus:O02"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Full prompts, utility, timeouts, archive tooling, the 14 accepted changes "
                   "and released code make the chain reconstructable. Deductions: no named immutable anchor (overseer and synthetic "
                   "benchmarks are editable, opus:O06/O07), no rollback/crash rule, greedy promotion on noisy scores.",
                   ["son55:E007", "son55:E008", "son55:E022", "son55:E018", "opus:O06", "opus:O07"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. SWE-Bench Verified and LiveCodeBench tests are credible verifiers, "
                               "but the 300 s cap makes accuracy partly a speed measure (opus:O08, A2: metric satisfiable by a "
                               "non-target factor), Table 1 accuracies are not integer proportions of the 50-item denominator with no "
                               "stated aggregation (opus:O04), and the symbol benchmark has admitted data-quality defects.",
                               ["son55:E009", "son55:E012", "son55:E020", "opus:O04", "opus:O08"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only an iteration trajectory with feature annotations; no fixed "
                             "meta-agent, ADAS-style or random-edit control, no per-feature ablation; the speed/timeout explanation is "
                             "conceded by the authors.", ["son55:E015", "son55:E012", "son55:E014", "opus:O08"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. The same fixed subsets drive promotion and are reported (opus:O01, "
                           "opus:O03), and the improver reads per-problem failures of that set (opus:O02); no held-out split, "
                           "contamination audit or second model. Results exist but are selection-contaminated — rated 1 as for POET "
                           "(cal-h1-v2 1901.01753) where selection and test coincide; 0/not_reported is kept for papers with no "
                           "evaluation split at all.", ["son55:E009", "son55:E021", "opus:O01", "opus:O02", "opus:O03"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder: interval on the test metric, no cross-run variance). Fig. 3/4 "
                              "show 95% CIs on mean utility; the headline accuracy has none, is one meta-run, and is the series peak "
                              "(opus:O05).", ["sol:E006", "son55:E013", "son55:E014", "opus:O05"]),
            "E.cost": R("resolved", 3, "Both seats 3; re-checked. Total ≈$7,000 for 15 iterations plus per-iteration $/time/tokens/"
                        "cache; no alternative optimiser to compare budgets against.",
                        ["son55:E010", "son55:E012", "sol:E005"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendices A–D; in scope (A): the agent's own code (tools, sub-agents, prompts) is "
                  "edited from benchmark feedback, archived and reused; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "generative_process_redesign",
                "Literal definitional match (fixed component of an iterative procedure freed); assumption_audit_and_pivot is about "
                "assumptions under guarantees/defenses.", ["son55:E003", "son55:E004"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["generative_process_redesign", None]],
                "As primary; no sub-card fits.", ["son55:E003"], "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H12"], ["make_the_improver_editable", "H19"]],
                "One entry per main card with its best sub. SICA archives every iteration but always promotes the argmax, i.e. a "
                "single elitist lineage (H19); H20's load-bearing element, a parent rule beyond 'pick the top scorer', is absent. "
                "H20's archive traits are recorded as condition notes on the H19 entry.", ["opus:O01", "son55:E007"], "none"),
            X(p, "local:2504.15228-2", *C(p, "expectations[local:2504.15228-2].status"), "revised",
              "local-2 = sol's cost question → met; son55's local-2 (negative regime reported) renumbered local-4 → met",
              "A4 collision: different questions under one ID. sol's cost answer verified (≈$7,000 + per-iteration costs). son55's "
              "question is answered by the AIME/GPQA run; 'challenged_with_evidence' is the wrong status because the paper never "
              "claims reasoning gains — the boundary is reported (met).", ["sol:E005", "son55:E022", "son55:E023"]),
            X(p, "rs:assumption_audit_and_pivot/RE-4", *C(p, "expectations[rs:assumption_audit_and_pivot/RE-4].status"), "sol",
              "partial", "Kept as an informational check although the card is not the final match: differentiation from the "
              "closest precedent (Gödel Agent/STOP) is argued only by scope — it supports G=2.", ["sol:E001", "son55:E005"]),
            X(p, "rs:generative_process_redesign/RE-1", *C(p, "expectations[rs:generative_process_redesign/RE-1].status"), "son55",
              "unmet", "Verified: no ablation showing the meta/target separation was the bottleneck.", ["son55:E015"]),
            X(p, "rs:generative_process_redesign/RE-2", *C(p, "expectations[rs:generative_process_redesign/RE-2].status"), "son55",
              "unmet", "Verified: no ADAS/hand-designed/alternative-search baseline.", ["son55:E015"]),
            X(p, "rs:generative_process_redesign/RE-3", *C(p, "expectations[rs:generative_process_redesign/RE-3].status"), "son55",
              "unmet", "Verified: 14 changes listed (Appendix D), none ablated.", ["son55:E015"]),
            X(p, "rsi:make_the_improver_editable/F2", *C(p, "expectations[rsi:make_the_improver_editable/F2].status"), "son55",
              "partial", "Verified: argmax keeps regressions from promotion and the overseer cancels stuck agents; no crash/rollback "
              "rule. Card's member figure (14%) not used (A5).", ["son55:E007", "son55:E011"]),
            X(p, "rsi:make_the_improver_editable/F3", *C(p, "expectations[rsi:make_the_improver_editable/F3].status"), "son55",
              "unmet", "Verified: failure mode present — one fixed subset promotes and reports (opus:O03).", ["son55:E009", "opus:O03"]),
            X(p, "rsi:make_the_improver_editable/F4", *C(p, "expectations[rsi:make_the_improver_editable/F4].status"), "son55",
              "unmet", "Verified: single run, greedy promotion on a jittery series (opus:O05).", ["son55:E013", "opus:O05"]),
            X(p, "rsi:make_the_improver_editable/F5", *C(p, "expectations[rsi:make_the_improver_editable/F5].status"), "revised",
              "unmet", "Not unknown: the text puts the overseer and the synthetic benchmarks inside the editable codebase and names "
              "no immutable anchor (opus:O06, opus:O07). Already charged under X (no rating change).", ["opus:O06", "opus:O07"]),
            X(p, "rsi:make_the_improver_editable/H19-step1", *C(p, "expectations[rsi:make_the_improver_editable/H19-step1].status"),
              "sol", "partial", "Verified: utility and caps fixed by the authors; editable boundary not stated.", ["sol:E003", "opus:O06"]),
            X(p, "rsi:make_the_improver_editable/H19-step4", *C(p, "expectations[rsi:make_the_improver_editable/H19-step4].status"),
              "sol", "unmet", "Verified: no separate selection/report sets, one lineage.", ["sol:E004", "opus:O03"]),
            X(p, "rsi:make_the_improver_editable/H19-step5", *C(p, "expectations[rsi:make_the_improver_editable/H19-step5].status"),
              "sol", "unmet", "Verified: no fixed-improver comparison or ablation of the self-applied part.", ["sol:E001"]),
            X(p, "rsi:make_the_improver_editable/H20-step5", *C(p, "expectations[rsi:make_the_improver_editable/H20-step5].status"),
              "same_supported_fact", "merged into rsi:make_the_improver_editable/H19-step4 = unmet",
              "Same check (held-out tasks / independent seeds) as H19 step 4, which sol answered unmet; H20 is not a final match.",
              ["son55:E009", "sol:E004"]),
            X(p, "rsi:make_the_improver_editable/S1", *C(p, "expectations[rsi:make_the_improver_editable/S1].status"), "son55",
              "partial", "Verified (opus:O06 shows the overseer is editable).", ["son55:E008", "opus:O06"]),
            X(p, "rsi:make_the_improver_editable/S2", *C(p, "expectations[rsi:make_the_improver_editable/S2].status"), "son55",
              "partial", "Verified: the agent is scored on its own task utility, not on descendants it produces.", ["son55:E007"]),
            X(p, "rsi:make_the_improver_editable/S3", *C(p, "expectations[rsi:make_the_improver_editable/S3].status"), "son55",
              "unmet", "Verified: no fixed meta-agent comparison.", ["son55:E015"]),
            X(p, "rsi:make_the_improver_editable/S4", *C(p, "expectations[rsi:make_the_improver_editable/S4].status"), "son55",
              "met", "Verified from the paper's own text (son55:E010), not from the card's quotation of it (A5).", ["son55:E010"]),
            X(p, "rsi:make_the_improver_editable/S5", *C(p, "expectations[rsi:make_the_improver_editable/S5].status"), "son55",
              "partial", "Verified: failed iterations archived; promotion greedy; path dependence admitted.", ["son55:E018"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G: residual against Gödel Agent/STOP is scope, not mechanism.",
                ["son55:E005", "son55:E006", "sol:E001"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: timeout-confounded accuracy and non-integer proportions.",
                ["opus:O04", "opus:O08", "son55:E012"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: results exist but are selection-contaminated (POET precedent), not absent.",
                ["opus:O01", "opus:O02", "opus:O03"], "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2504.15228-1]",
             "sol_value": "partial — statistics: CIs but no independent-search variance",
             "son55_value": "partial — measurement: speed vs capability not separated",
             "correction": "Same ID for different questions (A4 collision hidden by equal status). sol's kept as local-1; son55's "
                           "renumbered local-3.", "evidence_ids": ["sol:E006", "son55:E016"], "score_impact": "none"},
            {"field_path": "ratings.X / ratings.E.holdout (reasons)",
             "sol_value": "safety/edit boundary 'not audited'; holdout = repeated selection on fixed set",
             "son55_value": "edit boundary 'not stated' (F5 unknown); holdout = same subset",
             "correction": "Both seats missed two textual facts: the overseer and synthetic benchmarks are explicitly editable "
                           "(opus:O06/O07), and the archive explorer reads the worst problems of the reported benchmark (opus:O02). "
                           "Added to the reasons; ratings unchanged (X 3, E.holdout 1).",
             "evidence_ids": ["opus:O02", "opus:O06", "opus:O07"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): agent code edited from benchmark feedback, archived, best promoted. "
                                                   "Selection set = report set; one run; no baseline optimiser/gate-off; timeout "
                                                   "confound conceded; full cost reported; SWE-Bv values are half-integers over 50; "
                                                   "honest negative AIME/GPQA run.",
            "integrity_checks": "Both seats a1 on 2504.15228v2, material sha e987b743…; hashes equal conflicts.json; ids valid.",
            "controller_flags": "Selection set = scoring set confirmed (opus:O01–O03) → E.holdout 1, evidence_level task. Non-integer "
                                "SWE-Bv proportions confirmed for 0.17/0.51/0.53 and most other rows (opus:O04) → charged once, "
                                "under E.measurement.",
            "core_claim_check": "Re-read §3–§5, Table 1 and Appendices B/D; headline 53% is iter 14 peak, final 0.51 (opus:O05).",
            "rating_agreement": "5/8 identical; G → sol (2); E.measurement → son55 (2); E.holdout → son55 (1).",
        },
    }

    # =========================================================== out-of-scope helpers
    def oos_spec(p, reason, opus_evs, rs_reason, rs_main, rs_extra, dom_extra, scope, review):
        unk = lambda: R("unknown", None, reason, [e["evidence_id"] for e in opus_evs], [], scope)
        return {
            "base": "son55",
            "opus_evidence": opus_evs,
            "rs_pattern": {"primary": rs_main, "supporting": [], "outside_taxonomy": False, "reason": rs_reason,
                           "matches": [smatch("son55", p, rs_main, **rs_extra)],
                           "executes_pattern": "not assessed (out_of_scope)", "resolves_problem": "not assessed (out_of_scope)"},
            "domain_pattern": {"namespace": "rsi", "matches": [dom_extra], "unassigned": [], "revision_proposals": []},
            "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
            "claims": lambda c: c,
            "assessment": {
                "evidence_level": None,
                "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (cal-dev/r02b precedent).",
                "claim_support": None,
                "claim_support_note": "Not assessed under this rubric; results recorded as author-reported only.",
                "strongest_supported_claim": None,
                "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong."]},
            "ratings": {k: unk() for k in EIGHT},
            "status": "out_of_scope", "reason": reason, "aggregate_status": "accepted_final",
            "shared_error_corrections": [],
            "aggregate_review": review,
        }

    # =========================================================== 2505.03335 Absolute Zero
    p = "2505.03335"
    reason = ("out_of_scope (rubric A3): one model π_θ plays proposer and solver and both roles are updated by Task-Relative "
              "REINFORCE++; the triplet buffer and Python executor are the RL training environment/data, and the evaluated "
              "products are the trained Qwen2.5 checkpoints. No non-weight harness component is retained and evaluated. Not "
              "scored; null is not a zero-quality rating.")
    evs = [opus_ev(p, "O01", "RL update: use Task Relative REINFORCE++ to update", "Algorithm 1 line 18",
                   "Both proposer and solver improvement is delivered through weight updates."),
           opus_ev(p, "O02", "be our parameterized language model, it is used to play two roles, proposer", "§3.1",
                   "Proposer and solver are the same parameterized model."),
           opus_ev(p, "O03", "For the main experiments, we train AZR models on Qwen2.5-7B and Qwen2.5-7B-Coder", "§4.1",
                   "The evaluated artifacts are trained model checkpoints.")]
    S[p] = oos_spec(
        p, reason, evs,
        "Informational (out_of_scope): the proposer manufactures executor-validated tasks that become RL training data for the "
        "same model — C08 (controllable generator → single validity/learnability gate → retrain).",
        "self_supervised_signal_engineering", {},
        dmatch("son55", p, "self_generate_the_curriculum", "H22",
               fit="high (boundary card, informational)",
               condition_checks="Not checked item by item (out_of_scope). Executable validity anchor and learnability reward match "
                                "H22's tactic; the boundary card itself notes it touches weights; resemblance does not override A3.",
               evidence_ids=["son55:E001", "son55:E002", "son55:E004", "opus:O01"]),
        ["complete pinned v3 text incl. appendices (method §3, Algorithm 1, §4 experiments)"],
        {"initial_judgment_before_seat_scores": "Read abstract, §3 (roles, buffers, validation, TRR++) and §4.1 setup: joint RL on "
                                                "one model's weights; buffer/executor are training environment → out_of_scope (A3).",
         "integrity_checks": "Both seats a1 on 2505.03335v3, material sha b0044d87…; both independently out_of_scope; hashes "
                             "equal conflicts.json.",
         "core_claim_check": "Independently confirmed the A3 basis (opus:O01–O03).",
         "rating_agreement": "All eight unknown in both seats; kept."})
    S[p]["resolutions"] = [
        res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
            "Out-of-scope records carry no harness evidence label; null is canonical (sol's 'not_applicable' means the same).",
            ["opus:O01"], "none"),
        res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
            "The central claim was not checked under this rubric, so 'unresolved' (sol) overstates; null with a note.",
            ["opus:O03"], "none"),
        res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
            "sol stopped identification at the scope ruling (allowed); son55's informational identification is correct and kept.",
            ["son55:E001", "son55:E002"], "none"),
        res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["self_supervised_signal_engineering", "C08"]],
            "Generate → executor gate → retrain is C08's shape (informational).", ["son55:E002", "opus:O01"], "none"),
        res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55", [["self_generate_the_curriculum", "H22"]],
            "Co-trained proposer vs solver with an executable anchor is H22 (boundary card, informational).",
            ["son55:E001", "son55:E004"], "none"),
        X(p, "local:2505.03335-1", *C(p, "expectations[local:2505.03335-1].status"), "sol", "met",
          "Informational: the evaluated object is the RL-trained model; no independent non-weight component claim (opus:O01–O03).",
          ["sol:E001", "opus:O03"]),
    ]

    # =========================================================== 2505.14970 SEC
    p = "2505.14970"
    reason = ("out_of_scope (rubric A3): the curriculum bandit (category Q-values updated by TD(0) from absolute advantage) "
              "only schedules batches inside one GRPO fine-tuning run; it is neither retained nor evaluated as a component, and "
              "every result is a fine-tuned checkpoint (best checkpoint pass@1). The improver's product is weights. Not scored; "
              "null is not a zero-quality rating.")
    evs = [opus_ev(p, "O01", "an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process",
                   "Abstract", "The curriculum policy exists only inside the RL fine-tuning run."),
           opus_ev(p, "O02", "We report average pass@1 accuracy from the best checkpoint", "§3.1",
                   "Evaluated artifacts are fine-tuned checkpoints."),
           opus_ev(p, "O03", "is updated using the TD(0) method", "Abstract",
                   "The only non-weight state is the bandit, a training-time scheduler.")]
    S[p] = oos_spec(
        p, reason, evs,
        "Informational (out_of_scope): curriculum choice is recast as a non-stationary multi-armed bandit solved with TD(0) — "
        "reframe_as_solvable_object; sub null (C00/C21/C27 do not fit).",
        "reframe_as_solvable_object", {},
        dmatch("son55", p, "self_generate_the_curriculum", "H23",
               fit="low (boundary card, informational)",
               condition_checks="Not checked item by item (out_of_scope). H23 lists 'a bandit over task categories' as a generator, "
                                "but SEC only re-weights a fixed pool (no task synthesis) and the product is weights.",
               evidence_ids=["son55:E002", "son55:E004", "opus:O01"]),
        ["complete pinned v4 text incl. appendices (§2 method, Algorithm 1, §3 experiments, Appendix C)"],
        {"initial_judgment_before_seat_scores": "Read abstract, §2 and §3.1: bandit scheduler inside GRPO; results are best "
                                                "checkpoints → out_of_scope (A3).",
         "integrity_checks": "Both seats a1 on 2505.14970v4, material sha ca2feb88…; both independently out_of_scope; hashes "
                             "equal conflicts.json.",
         "core_claim_check": "Independently confirmed the A3 basis (opus:O01–O03); noted best-checkpoint reporting (informational).",
         "rating_agreement": "All eight unknown in both seats; kept."})
    S[p]["resolutions"] = [
        res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
            "As for 2505.03335: null is canonical for out-of-scope records.", ["opus:O02"], "none"),
        res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
            "Not assessed under this rubric; null with a note.", ["opus:O02"], "none"),
        res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "reframe_as_solvable_object",
            "son55's informational identification (curriculum → non-stationary MAB) is correct and kept.",
            ["son55:E002", "son55:E004"], "none"),
        res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["reframe_as_solvable_object", None]],
            "Parent only; no sub fits.", ["son55:E004"], "none"),
        res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55", [["self_generate_the_curriculum", "H23"]],
            "H23 names a bandit over task categories; low fit (no synthesis), informational.", ["son55:E002"], "none"),
        X(p, "local:2505.14970-1", *C(p, "expectations[local:2505.14970-1].status"), "sol", "met",
          "Informational: Algorithm 1 returns the fine-tuned LLM and all experiments evaluate checkpoints (opus:O02).",
          ["sol:E003", "opus:O02"]),
    ]

    # =========================================================== 2505.17716 AgentRR
    p = "2505.17716"
    scope_e = ["complete pinned v1 text §1–§7 incl. Tables 1–2 and Figure 1–4 captions; no appendix exists",
               "§5 case study read specifically: qualitative walkthrough, no AgentRR timing, success rate, denominator or control",
               "no theorem, lemma or proof anywhere (state-transition §3.4 is definitional) — A1 exception not triggered"]
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Our design and evaluation demonstrate that AgentRR effectively addresses the challenges of agent reliability, privacy, and performance",
                    "§6", "The paper claims an evaluation that it does not contain."),
            opus_ev(p, "O02", "The SOTA LLM-based agent like OpenAI’s CUA requires approximately three minutes to process this form",
                    "§5", "The only number in the paper is an anecdote about a baseline; nothing is measured for AgentRR."),
            opus_ev(p, "O03", "we establish theoretical foundations and propose novel solutions for future research in agent systems",
                    "Abstract", "Claimed 'theoretical foundations' are definitions (§3.4); no proved result exists, so A1's formal-result exception does not apply."),
            opus_ev(p, "O04", "The store is likely implemented as a database storing the Experience organized as JSON or a graph database format",
                    "§3.3", "The Experience Store is described hypothetically ('likely implemented')."),
            opus_ev(p, "O05", "whether performed by a ML model or manually", "§4.2",
                    "The summary operation (traces → experiences) is left open between model and manual."),
            opus_ev(p, "O06", "First, there is still a lack of clear definitions for different levels of experiences.", "§6",
                    "Authors concede the level definitions are missing."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: recorded experiences condition a (smaller) model at replay without parameter updates; C03 not "
                      "assigned (no unified schema learned upstream, no category holdout).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial (design level)", "resolves_problem": "no evidence (no experiments)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                dmatch("son55", p, "index_experience_for_reuse", "H03"),
            ],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2505.17716-1"): "local:2505.17716-4",
                    ("son55", "local:2505.17716-2"): "local:2505.17716-3",
                    ("son55", "local:2505.17716-3"): "local:2505.17716-2"},
            overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": None,
            "evidence_level_note": "No EVIDENCE.md level: the paper reports no measured output, score or cost for AgentRR "
                                   "(opus:O02); levels start at an observed task gain (cal-dev 1112.5309 precedent). Null, not 'none'.",
            "claim_support": "unsupported",
            "strongest_supported_claim": "A design that records traces, verifies them by replay, summarizes them into low-level "
                                         "parameterized scripts and high-level procedural guidance with check functions, stores them "
                                         "for sharing and replays the lowest workable level, illustrated by one qualitative "
                                         "form-filling walkthrough. Claimed gains in reliability, privacy, cost and speed — and the "
                                         "§6 claim of an 'evaluation' (opus:O01) — have no supporting measurement.",
            "unresolved": ["Any measured benefit; level definitions (opus:O06); check-function soundness; comparison with MobileGPT/Workflow Use."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The exact-replay vs generalization tension is concrete and the closest "
                   "replay neighbours (MobileGPT hierarchical sub-task replay, Workflow Use, UFO2) are named, but the residue is "
                   "asserted in one sentence each and the four-challenge framing is broad.",
                   ["son55:E002", "son55:E019", "son55:E020", "sol:E010"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Multi-level experience + check functions target the stated "
                   "trade-off with a specific mechanism sketch; the load-bearing assumption (LLM-written experiences and check "
                   "functions are trustworthy) rests on 'conservative generalization' and user audit.",
                   ["son55:E004", "son55:E005", "son55:E007", "son55:E008"]),
            "X": R("resolved", 2, "Both seats 2; re-checked against anchor text ('main steps described; retention/recovery/"
                   "interfaces or key conditions unclear'): record → replay-verify → summarize → store → replay with fallback is "
                   "described and walked through in §5, but the summary operation is left open (opus:O05), the store is hypothetical "
                   "(opus:O04), level definitions are missing (opus:O06), and level selection/versioning are goals only.",
                   ["son55:E009", "son55:E010", "son55:E012", "son55:E016", "opus:O04", "opus:O05", "opus:O06"]),
            **{k: R("not_reported", 0, f"A1 (both seats; re-checked): framework paper without experiments; no {what}. "
                    "The single CUA timing is about a baseline (opus:O02); no formal result triggers the A1 exception (opus:O03).",
                    ["opus:O02", "opus:O03"], [], scope_e)
               for k, what in (("E.measurement", "metric or verifier for any claimed benefit"),
                               ("E.causality", "control, ablation or comparison"),
                               ("E.holdout", "evaluation set, split or reuse test"),
                               ("E.statistics", "denominator, repeat, interval or failure count"),
                               ("E.cost", "measured time, token or money cost of AgentRR"))},
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text; in scope (B): a retained, replay-verified experience store designed for reuse in later "
                  "tasks; framework without experiments, scored under A1 (five E items not_reported = 0).",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "No measurement → no level; null+reason is canonical. son55's literal 'none' is normalised to null (rv2); sol's "
                "'not_applicable' would wrongly imply the label does not apply to an in-scope system paper.",
                ["opus:O02"], "none (labels are not scored)"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["index_experience_for_reuse", "H03"]],
                "Two different mains, each with its best sub: H02 for the shared, packaged experience store; H03 for low-level "
                "experiences as parameterized, re-bindable cases admitted after replay verification (§5 Summary/Replay).",
                ["son55:E009", "son55:E010", "son55:E012"], "none"),
            X(p, "local:2505.17716-3", *C(p, "expectations[local:2505.17716-3].status"), "revised",
              "local-3 = sol's statistics question → unmet (son55's equivalent local-2 merged, also unmet); son55's local-3 (cost) "
              "merged into local-2 → unmet",
              "A4 collision. son55's cost question equals sol's local-2; acknowledging user burden qualitatively is not partial "
              "cost reporting when nothing is measured (E.cost not_reported), so sol's unmet stands.",
              ["sol:E008", "son55:E018"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55", "unmet",
              "Verified: one form example; prototype limited to repetitive tasks.", ["son55:E017"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55", "unmet",
              "Verified: completeness/robustness listed as open questions only.", ["son55:E003"]),
            X(p, "rsi:abstract_experience_into_guidance/H02-step3",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H02-step3].status"), "sol", "partial",
              "Verified: raw traces are replay-verified before summarization; no admission rate, merge or versioning of compiled "
              "experiences.", ["sol:E002", "opus:O04"]),
            X(p, "rsi:abstract_experience_into_guidance/H02-step5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H02-step5].status"), "sol", "unmet",
              "Verified: no reuse evaluation at all.", ["sol:E006"]),
            X(p, "rsi:index_experience_for_reuse/F4", *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"), "son55",
              "partial", "Verified: LLM-generated experiences/check functions rely on user audit and replay verification.",
              ["son55:E007", "son55:E009"]),
            X(p, "rsi:index_experience_for_reuse/F6", *C(p, "expectations[rsi:index_experience_for_reuse/F6].status"), "son55",
              "partial", "Verified: the multi-level shape is the contribution with no evidence linking shape to benefit.",
              ["son55:E004"]),
            X(p, "rsi:index_experience_for_reuse/S2", *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"), "son55",
              "partial", "Verified: replay reproducibility check before write; no outcome gate after write.", ["son55:E009"]),
            X(p, "rsi:index_experience_for_reuse/S4", *C(p, "expectations[rsi:index_experience_for_reuse/S4].status"), "son55",
              "partial", "Verified: selection goal stated ('lowest-level ... highest success rate'), no algorithm.", ["son55:E010"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "son55",
              "unmet", "Verified: no store-off ablation (no experiments).", ["son55:E013"]),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2505.17716-1] / expectations[local:2505.17716-2]",
             "sol_value": "local-1 unmet — check-function soundness; local-2 unmet — cost",
             "son55_value": "local-1 unmet — benefits unmeasured; local-2 unmet — replay success/failure denominators",
             "correction": "Two A4 collisions hidden by equal status. sol's numbering kept (local-1 soundness, local-2 cost, "
                           "local-3 statistics); son55 local-1 → local-4, local-2 → local-3 (merged), local-3 → local-2 (merged).",
             "evidence_ids": ["sol:E005", "son55:E015"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Position/vision paper: record → replay-verify → summarize into multi-level "
                                                   "experiences + check functions → store → replay. Only a qualitative case study; the "
                                                   "one number is an anecdote about CUA; no theorems. → A1: five E not_reported; G/M/X "
                                                   "design-level ≈2.",
            "integrity_checks": "Both seats a1 on 2505.17716v1, material sha ad71ce37…; hashes equal conflicts.json; ids valid.",
            "shared_error_audit": "Controller asked to check the common 27.5: A1 is applied correctly in both seats (five E "
                                  "not_reported, rating 0, search scope recorded; no formal result, opus:O03). G/M/X 2/2/2 re-checked "
                                  "against the anchors: X considered at 1 because summary/store/levels are unspecified (opus:O04–O06), "
                                  "kept at 2 because anchor 2 is defined as 'main steps described, retention or key conditions "
                                  "unclear', which is exactly this case. claim_support unsupported confirmed (opus:O01). No rating change.",
            "rating_agreement": "8/8 identical and re-checked unchanged.",
        },
    }
    return S


def batch_notes():
    return [
        "2504.07952: E.holdout corrected 2→1 for both seats (in-stream memory precedent: r01b 2407.08937, 2406.04271).",
        "2504.15228: H20 step 4 and make_the_improver_editable success conditions quote this paper's own '$7000 for fifteen "
        "iterations' (A5 card-result leak); not used as evidence; rewrite proposed for stage end.",
        "2504.15228: son55's H19/H20 boundary proposal endorsed (archive + greedy argmax parent).",
        "2505.03335 / 2505.14970: both seats independently out_of_scope; A3 basis independently confirmed. son55's proposal to "
        "reconcile boundary cards (self_generate_the_curriculum H22/H23 list weight-updating members) with A3 is forwarded to stage end.",
        "2505.17716: shared 27.5 audited; A1 correctly applied; no change.",
        "No requests for new material: every ruling uses the pinned texts; seats' requests for neighbour full texts (BoT, "
        "MobileGPT, Gödel Agent) do not affect any final rating and are not re-raised.",
    ]
