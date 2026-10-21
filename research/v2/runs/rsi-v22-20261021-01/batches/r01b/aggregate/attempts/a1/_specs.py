"""Opus rulings for r01b a1 (data only; consumed by _build.py)."""

VER = "rsi-cards@52ff9657"
DOM_SRC = "research/patterns/conditions.json"


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    S = {}

    # =========================================================== 2402.11359 AgentOptimizer
    p = "2402.11359"
    S[p] = {
        "base": "sol",
        "a3": "none",
        "opus_evidence": [
            opus_ev(p, "O01", "Interestingly, for counting and probability problems, when training GPT-4+ agent, the training "
                    "performance remains the same while test performance improves from 72.5% to 76.3%.",
                    "§3.2 Mathematical reasoning; raw line 1349",
                    "C.Probability had zero training-set improvement, yet it is one of the three ablation types chosen for "
                    "'largest performance improvements' (§3.3.1) — so the ablation subset was picked by test-set gains. "
                    "Main-table holdout is unaffected (test never drives rollback); the ablation is test-selected."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: the conventionally fixed, hand-written function set of a staged agent becomes a learnable design "
                      "variable while the backbone stays frozen. Main-card fit only; C15/C23/C24 target generative "
                      "conditioning/latent redesign and do not fit tool-code editing.",
            "matches": [{"main_id": "generative_process_redesign", "sub_id": None, "role": "primary", "fit": "partial (low-medium)",
                         "tactic_steps_checked": ["name the fixed component (manual function set)", "treat as free variable",
                                                  "isolate load-bearing mechanism by ablation (progressive update, rollback)"],
                         "success_checks": ["component named and reframed", "ablation of update mechanism exists"],
                         "failure_checks": ["no evidence the hand-written function set is the bottleneck (no curated-tool baseline)"],
                         "evidence_ids": ["sol:E002", "son55:E001", "son55:E014"],
                         "reason": "Shared by both seats; kept at main level."}],
            "executes_pattern": "partial (component freed and redesigned; bottleneck status of fixed tools not tested)",
            "resolves_problem": "partial: author-reported held-out gains in 11/14 MATH cells and GAIA/TabMWP, single runs",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                {"main": "attribute_and_patch_incumbent", "sub": "H12", "version": VER, "fit": "medium-high",
                 "condition_checks": "S3 partial (aggregate training-set rollback, no per-case or independent regression set); "
                                     "S5 met (full execution histories + current functions); S6 met (same optimizer across two agents, "
                                     "three task families); F5 failure present (no check that a failure is caused by the edited function).",
                 "evidence_ids": ["sol:E001", "sol:E003", "son55:E004", "son55:E005"]},
                {"main": "crystallize_executable_capability", "sub": "H06", "version": VER, "fit": "low-medium",
                 "condition_checks": "Parent fits (retained executable functions). Sub revised from son55's H07 to H06: functions are "
                                     "built offline by walking a training-problem pool before deployment (H06 step 1), not forged "
                                     "inline when a live task exposes a gap (H07). S1 partial (admission by aggregate replayed "
                                     "training accuracy, not per-function invocation evidence); S3 partial; S5 met (w/ vs w/o "
                                     "learned functions on disjoint test, rest of agent fixed; single run).",
                 "evidence_ids": ["son55:E001", "son55:E005", "son55:E023", "sol:E004"]},
            ],
            "unassigned": [],
            "revision_proposals": ["H06/H07 boundary: offline epoch-level tool training from a labelled training pool (AgentOptimizer) "
                                   "should be named as an H06 variant; H07 text implies inline gap-triggered forging (stage end, not applied)."],
        },
        "pattern_mapping": [
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "attribute_and_patch_incumbent", "domain_sub": "H12",
             "operation_correspondence": "Freeing the fixed tool inventory is realised as trace-driven add/revise/remove patches "
                                         "promoted by training-set rollback.",
             "necessary_conditions_and_differences": "H12 asks for promotion on a separate split; here promotion uses the training "
                                                     "set (10–20 items) and certification uses a disjoint test subset.",
             "evidence_ids": ["sol:E002", "sol:E003"]},
            {"rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "crystallize_executable_capability", "domain_sub": "H06",
             "operation_correspondence": "The retained artifact is a library of executable functions reused at test time.",
             "necessary_conditions_and_differences": "H06 admits per-skill after execution verification; AgentOptimizer admits "
                                                     "the whole set by aggregate training accuracy.",
             "evidence_ids": ["son55:E023", "sol:E004"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2402.11359-1"): "local:2402.11359-4",
                    ("son55", "local:2402.11359-2"): "local:2402.11359-5"},
            overrides={"rsi:crystallize_executable_capability/S5": {
                "status": "met",
                "reason": "Opus revision: the 'w/o agent training' rows are the same agent with only the initial Python function, "
                          "i.e. the learned library removed while the rest is fixed; gains on the disjoint test subsets (11/14 MATH "
                          "cells, GAIA, TabMWP) are therefore a retained-artifact contrast. Single run, no per-function ablation."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Functions are learned offline on a training subset and evaluated frozen on a disjoint test subset; "
                                   "no improver-level evidence.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: a function set learned offline from training-set execution histories, with "
                                         "training-set rollback, improves held-out test accuracy in most (not all) reported cells for "
                                         "two agent types; single runs, small test subsets, no cost ledger.",
            "unresolved": ["Run-to-run variance and optimizer cost.",
                           "Table 4: GPT-4+ trained MATH test 66.25% is below CREATOR 75.0% and CRAFT 73.8%; 'outperform in most cases' only partly holds.",
                           "Ablation types were selected by test-set gains (opus:O01)."]},
        "ratings": {
            "G": R("resolved", 3, "Opus sides with sol. Gap is concrete: hand-crafted or one-shot per-query tools (CREATOR, CRAFT, "
                   "Tool-maker) are created without optimisation against downstream performance, and two of these neighbours are "
                   "compared empirically (Table 4). Not 4: executable skill-library neighbours (e.g. Voyager-type libraries) are not "
                   "covered and the 'train without weights' framing is background (son55's point, which caps G below 4 but does not "
                   "make the neighbour comparison 'incomplete' at the 2 anchor).",
                   ["sol:E008", "son55:E002", "son55:E003", "son55:E016"]),
            "M": R("resolved", 3, "Opus sides with sol. Mechanism is reconstructable (full-training-set histories → one of "
                   "add/revise/remove per step → rollback + failure memory) and its distinguishing predictions against naive "
                   "alternatives (one-shot regeneration; no rollback) are stated and tested (Table 3). Not 4 because the acceptance "
                   "signal is accuracy on 10–20 training items (noisy) and authors observe overfitting; son55's gate-noise point is "
                   "real but the causal logic is not merely partial, so 2 under-rates it.",
                   ["sol:E001", "sol:E002", "son55:E014", "son55:E005"], ["sol:E007"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Actions, inputs, rollback, failure-list write-back and next-epoch read "
                   "are specified; epochs=10 with early-stop threshold 10 means early stop never fires; no versioning or retirement.",
                   ["sol:E002", "sol:E003", "sol:E009", "son55:E006", "son55:E007"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Exact-match accuracy on standard labelled benchmarks; small "
                               "sub-samples (80/100 test per cell); TabMWP training accuracies (66.7%, 73.3%) are inconsistent with "
                               "the stated 10 training items.",
                               ["sol:E004", "sol:E011", "son55:E008", "son55:E009", "son55:E013"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Store-off (w/o training), rollback-off and progressive-off "
                             "ablations and two tool-creation baselines exist, but ablations run only on three test-selected types "
                             "(opus:O01), optimizer compute is unmatched, and Table 4 partly contradicts the summary.",
                             ["sol:E005", "sol:E006", "son55:E014", "son55:E016", "son55:E017", "opus:O01"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Rollback and early stop use training data only; the disjoint "
                           "test subset certifies the frozen set; cross-type transfer (Fig. 3) adds evidence. Deductions: same-"
                           "distribution sub-samples, authors report overfitting, ablation and illustrative types were chosen after "
                           "seeing test results.",
                           ["sol:E004", "sol:E007", "son55:E008", "son55:E011"], ["opus:O01", "son55:E024"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample counts and negative cells reported, but every result is "
                              "a single run without intervals; ±5pp differences at n=80–100 are within noise.",
                              ["sol:E004", "son55:E011", "son55:E020"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked: no optimizer token/call/time or budget-matched "
                        "comparison anywhere; only a remark that OpenAI cost forced sub-sampling.",
                        ["son55:E021"], [],
                        ["Full pinned text: §§1–5, Appendices A–H, Tables 1–8; searched cost/budget/token/time/price/USD."]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 text; all eight items resolved; no material blocker.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("domain_pattern.matches", *conflict(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H12"], ["crystallize_executable_capability", "H06"]],
                "H12 shared. son55 is right that the retained executable-function library also instantiates "
                "crystallize_executable_capability, but the sub-pattern is H06 (offline practice over a training-problem pool before "
                "deployment, rollback on regression) rather than H07 (inline forging when a live task exposes a gap).",
                ["son55:E001", "sol:E004", "son55:E023"], "none (patterns never score)"),
            res("expectations[local:2402.11359-1].status", *conflict(p, "expectations[local:2402.11359-1].status"), "revised",
                "local-1 = sol's question (separate early-stop utility) → partial; son55's local-1 (single runs) kept as "
                "local:2402.11359-4 = unmet",
                "Same ID, different questions. sol-1: rollback and early stop are removed jointly, so early stop's own utility is "
                "untested (and with E=C=10 it cannot fire) → partial. son55-1: all results single-run → unmet; kept as local:2402.11359-4.",
                ["sol:E006", "sol:E009", "son55:E011"], "none; consistent with E.causality=2 and E.statistics=1"),
            res("expectations[local:2402.11359-2].status", *conflict(p, "expectations[local:2402.11359-2].status"), "revised",
                "local-2 = sol's question (holdout breadth) → partial; son55's local-2 (optimizer cost) kept as local:2402.11359-5 = unmet",
                "Same ID, different questions. sol-2: disjoint instance holdout exists but overfitting and contamination limit "
                "generalisation → partial. son55-2: no optimizer cost or budget matching → unmet (verified).",
                ["sol:E004", "sol:E007", "son55:E021"], "none; consistent with E.holdout=3 and E.cost=0"),
            res("expectations[local:2402.11359-3].status", *conflict(p, "expectations[local:2402.11359-3].status"), "sol",
                "partial",
                "Only sol asked whether function correctness is certified: task accuracy gives indirect support, cyclomatic "
                "complexity (Table 6) does not certify correctness. Verified.", ["sol:E012"], "none"),
            res("expectations[rs:generative_process_redesign/RE-1].status",
                *conflict(p, "expectations[rs:generative_process_redesign/RE-1].status"), "son55", "partial",
                "Only son55 answered the shared RS card's RE-1. Verified: ablations show the update mechanism is load-bearing, but "
                "no curated hand-written function-set baseline tests that the fixed tool set is the bottleneck.",
                ["son55:E014"], "none"),
            res("expectations[rs:generative_process_redesign/RE-2].status",
                *conflict(p, "expectations[rs:generative_process_redesign/RE-2].status"), "son55", "partial",
                "Verified: CREATOR/CRAFT are compared but Table 4 is mixed (GPT-4+ MATH test 66.25% below both); no equal-budget "
                "memory/skill-library or prompt-optimizer baseline.", ["son55:E016", "son55:E017"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/F5].status",
                *conflict(p, "expectations[rsi:attribute_and_patch_incumbent/F5].status"), "son55", "unmet",
                "Verified: nothing checks that a failed task was caused by the edited function rather than reasoning/formatting; "
                "'unmet' here records that the failure mode is present.", ["son55:E004"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S6].status",
                *conflict(p, "expectations[rsi:attribute_and_patch_incumbent/S6].status"), "son55", "met",
                "Verified: one optimizer and hyper-parameter set across GPT-4+ and ReAct agents and three task families.",
                ["sol:E009", "son55:E006"], "none"),
            res("expectations[rsi:crystallize_executable_capability/S1].status",
                *conflict(p, "expectations[rsi:crystallize_executable_capability/S1].status"), "son55", "partial",
                "Verified: admission is by aggregate replayed training accuracy (execution-based but not per-function invocation "
                "evidence); successful-call counts are reported only descriptively.", ["son55:E005", "son55:E023"], "none"),
            res("expectations[rsi:crystallize_executable_capability/S3].status",
                *conflict(p, "expectations[rsi:crystallize_executable_capability/S3].status"), "son55", "partial",
                "Verified: functions are used on disjoint test inputs (Table 5) but admission itself never validates on unseen "
                "inputs; transfer only via Fig. 3.", ["son55:E011"], "none"),
            res("expectations[rsi:crystallize_executable_capability/S5].status",
                *conflict(p, "expectations[rsi:crystallize_executable_capability/S5].status"), "revised", "met",
                "son55 said no retained-artifact ablation exists. The 'w/o agent training' rows are exactly the agent with the "
                "learned library removed and everything else fixed, evaluated on the same disjoint test subsets; that is the "
                "retained-library contrast (single run).", ["son55:E012", "son55:E013", "sol:E005"],
                "none; E.causality stays 2 for the reasons in its rating"),
            res("expectations[rsi:evidence_gated_retention/S1].status",
                *conflict(p, "expectations[rsi:evidence_gated_retention/S1].status"), "son55", "partial",
                "Verified: before/after training-set accuracy is a set-level counterfactual for each update, unpaired and untested; "
                "per-function marginal utility is not measured.", ["son55:E005"], "none"),
            res("ratings.G", *conflict(p, "ratings.G"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.G: closest tool-creation neighbours are named and two are run head-to-head; missing skill-library "
                "neighbours cap at 3, not 2.", ["sol:E008", "son55:E003", "son55:E016"], "+3.75 vs son55 (15×1/4)"),
            res("ratings.M", *conflict(p, "ratings.M"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.M: distinguishing predictions are stated and tested by ablation; noisy small-sample acceptance keeps it "
                "below 4.", ["sol:E002", "son55:E014", "son55:E005"], "+5.0 vs son55 (20×1/4)"),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A-class): retained executable function set learned offline from execution "
                                                   "histories with training-set rollback; disjoint small test subsets; single runs; "
                                                   "no cost; Table 4 partly contradicts its summary; ablation types test-selected.",
            "integrity_checks": "Both seats a1 on 2402.11359v4, material sha 8bcba377…, input_hash 21ce283d…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; RS/domain ids and parents valid.",
            "core_claim_check": "Re-read Tables 1–4, §3.3.1 ablation selection, Appendix G hyper-parameters and the whole appendix for cost.",
            "rating_agreement": "6/8 items identical across seats and re-checked unchanged; G and M resolved for sol.",
            "expectation_renumbering": "son55 local-1 → local-4, local-2 → local-5 (same ID, different questions).",
        },
    }

    # =========================================================== 2406.04271 BoT
    p = "2406.04271"
    pages_note = ("Page images are of arXiv v1 (6 Jun 2024, 'Preprint. Under review'), NOT the pinned v2 text (14 Oct 2024). "
                  "Values are corroboration only and are not used to change any seat-disputed rating.")
    S[p] = {
        "base": "son55",
        "a3": "not required for this decision (no rating depends on figure values). If the controller wants figure-value-aware "
              "dual ratings, first re-render page images from the pinned v2 PDF (current images are v1), then dispatch a3 on "
              "E.causality/E.statistics/E.cost only.",
        "extra_materials": [
            {"material_id": f"2406.04271.pages/{f}", "url": "https://arxiv.org/pdf/2406.04271v1",
             "version": "2406.04271v1 (page image; differs from pinned v2)", "sha256": g["PAGE_SHA"][f],
             "local_path": f"research/fulltext/review-runs/rsi-v22-20261021-01/materials/2406.04271.pages/{f}",
             "sections_read": ["Opus: visual read for figure values (Figs 3–10) and version header"], "complete": True,
             "missing_sections": [], "note": pages_note}
            for f in ("p-01.png", "p-07.png", "p-08.png", "p-09.png", "p-10.png", "p-11.png")],
        "opus_evidence": [
            opus_ev(p, "O01", "T_{new}=LLM_{\\text{distill}}(x_{d},S_{x}),", "§3.3 Template Distillation eq. 4; raw line 815",
                    "Distillation input is the distilled problem and the model's own solution; nothing in §3.3 conditions "
                    "insertion on correctness or an external check (insertion gate is novelty only, eq. 5)."),
            opus_ev(p, "O02", "arXiv:2406.04271v1 [cs.CL] 6 Jun 2024", "page image p-01.png, left margin header",
                    "Supplied page images are v1, whereas the manifest pins v2 text. " + pages_note,
                    kind="our_inference", page="p-01.png"),
            opus_ev(p, "O03", "Ablation study of buffer-manager -- Accuracy: BoT+GPT4 56.8, 78.5, 87.4, 88.5; "
                    "BoT+GPT4 (w/o buffer-manager) 52.8, 53.6, 57.4, 54.1 (Rounds 1–4)",
                    "Figure 9, page image p-11.png (v1)",
                    "Single-run store-on vs store-off curves over four rounds of 50 new questions per benchmark; magnitude "
                    "corroborates the v2 text's qualitative claim (§6). " + pages_note, page="p-11.png"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Both seats: tasks are solved by conditioning a frozen model on a retrieved template. C03 kept (son55) because its "
                      "step 3 explicitly covers the no-upstream-tuning branch that aligns a query to a retrievable reference bank; "
                      "fit is low because category holdout and the nearest-neighbour baseline are absent. decompose_and_delegate/C25 "
                      "kept as supporting: the strongest gains (Game of 24, Checkmate) come from templates instantiated as executable "
                      "programs routed to an interpreter / python-chess.",
            "matches": [
                {"main_id": "adapt_via_conditioning", "sub_id": "C03", "role": "primary", "fit": "low-medium",
                 "tactic_steps_checked": ["canonical template schema", "retrievable reference bank", "no upstream tuning, query-to-bank retrieval",
                                          "category-level holdout (absent)", "cheaper-alternative baseline (absent)"],
                 "success_checks": ["retrieval-conditioned reuse without parameter updates"],
                 "failure_checks": ["no contamination audit", "no nearest-neighbour / raw-case baseline"],
                 "evidence_ids": ["son55:E006", "son55:E007", "sol:E001"], "reason": "son55 match accepted after card check."},
                {"main_id": "decompose_and_delegate", "sub_id": "C25", "role": "supporting", "fit": "low",
                 "tactic_steps_checked": ["executable intermediate artifact", "routed to sound solver"],
                 "success_checks": ["program templates executed"], "failure_checks": ["delegation not isolated from 'thought reuse'"],
                 "evidence_ids": ["son55:E015", "son55:E024"], "reason": "son55 supporting match accepted."}],
            "executes_pattern": "partial", "resolves_problem": "partial: author-reported gains; attribution to experience reuse vs "
                                                              "programmatic solving not separated",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                {"main": "abstract_experience_into_guidance", "sub": "H00", "version": VER, "fit": "medium",
                 "condition_checks": "S1 met; S2 unmet (no success/failure contrast); S3 unmet (no grounding signal decides what becomes "
                                     "a template, opus:O01); S4 partial (novelty dedup only); S5 unmet (similarity gate, not utility); "
                                     "F5 failure present.",
                 "evidence_ids": ["son55:E002", "son55:E004", "son55:E006", "opus:O01"]},
                {"main": "index_experience_for_reuse", "sub": "H03", "version": VER, "fit": "low",
                 "condition_checks": "Secondary only: retrieve-by-similarity → re-bind de-instantiated template → append matches H03's "
                                     "operation, but the parent claims gain from near-raw precedent, while BoT abstracts. S1 met; "
                                     "S2 unmet; S5 partial (store-off ablations); F3 present for the round ablation; F4 present.",
                 "evidence_ids": ["son55:E007", "son55:E018", "son55:E021"]},
            ],
            "unassigned": [],
            "revision_proposals": ["H00/H03 boundary: de-instantiated procedural templates retrieved by similarity sit between the two "
                                   "parents; note in H03 'differentiation' (stage end, not applied)."],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2406.04271-2"): "local:2406.04271-3"},
            overrides={
                "local:2406.04271-1": {"status": "unmet",
                                       "reason": "Same question in both seats (code/library confound). Opus: unmet — PAL is a code baseline "
                                                 "but receives neither python-chess nor templates; the confound is not controlled."},
                "rsi:abstract_experience_into_guidance/S3": {"status": "unmet",
                                                             "reason": "Opus: no verification or correctness signal decides insertion; "
                                                                       "the model's own solution is distilled (opus:O01)."},
                "rs:adapt_via_conditioning/RE-6": {"status": "unmet",
                                                   "reason": "Opus revision: only a stated limitation about weaker models and a template-"
                                                             "count distribution; no sensitivity experiment on source quality/coverage."},
            }),
        "claims": lambda c: [dict(x, opus_note=("Opus: in-stream store-on/off contrast over later rounds is author-reported in v2 text "
                                                 "(son55:E019, son55:E020); v1 Fig. 9 values (opus:O03) corroborate magnitude, single run.")
                                  if x["claim_id"] == "C2" else None) if x["claim_id"] == "C2" else x for x in c],
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Store-on vs store-off contrast across four successive rounds of newly sampled questions (§6 text); "
                                   "same distribution, single run, no frozen-store holdout. Main Table 1 alone would be task-level.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: BoT (GPT-4) scores above listed prompting baselines on ten tasks, and a growing "
                                         "template buffer improves later same-benchmark rounds versus a manager-off variant. Attribution "
                                         "to 'thought reuse' is confounded by executable templates (python-chess, enumeration); buffer "
                                         "construction vs Table 1 test separation is not stated.",
            "unresolved": ["Table 1 evaluation-set sizes and buffer initialisation for main runs", "programmatic-template confound",
                           "variance", "construction cost", "page images supplied are v1, not pinned v2"]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. Gap (no reuse of high-level guidelines from completed tasks) is sourced and "
                   "Thought-Retriever/analogical/meta-prompting are named, but the closest experience-abstraction neighbours "
                   "(insight-extraction memories, Reflexion-style memory, skill libraries) are neither discussed nor compared; "
                   "multi-query cost is generic background.", ["son55:E002", "son55:E003"]),
            "M": R("resolved", 2, "Opus sides with son55. Distil→retrieve→instantiate is concrete, but the key assumption — that a "
                   "template distilled from a single, unverified solution is reusable guidance — is weak (opus:O01), and no prediction "
                   "distinguishes template abstraction from raw-case retrieval or plain program delegation.",
                   ["son55:E006", "son55:E007", "opus:O01"], ["son55:E024"]),
            "X": R("resolved", 2, "Opus sides with son55. Retrieval threshold, novelty rule and fallback templates are described, but "
                   "insertion has no correctness gate, no retirement/versioning, and the buffer state/initialisation used for the "
                   "main Table 1 runs is not specified — a key operating condition left unclear (2 anchor). sol's own reason lists the "
                   "same gaps.", ["son55:E004", "son55:E005", "son55:E008", "sol:E001"], ["son55:E021"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Verifiable tasks, but Table 1 evaluation-set sizes are not "
                               "reported, the Sonnet-writing metric is unspecified, and headline deltas are internally inconsistent "
                               "(abstract 11% vs §4.1 23% on Game of 24). python-chess comparability is scored under E.causality (A2).",
                               ["son55:E010", "son55:E011", "son55:E013", "son55:E014"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Distiller-off, meta-buffer-off and manager-off ablations exist; "
                             "executable templates (python-chess, enumeration) and extra calls are not matched in baselines; no raw-"
                             "case retrieval control. v1 figure values (opus:O03) confirm direction, do not lift this.",
                             ["sol:E004", "son55:E018", "son55:E020", "opus:O03"], ["son55:E015", "son55:E024"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Rounds draw new questions from the same benchmarks the buffer is "
                           "built from; no overlap check, no frozen-store held-out set; main-run buffer construction relative to test "
                           "items unstated.", ["sol:E003", "son55:E018", "son55:E021"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked. Ten repeated 1000-sample evaluations reported as means only; "
                              "Table 1 single values, sizes missing, no intervals.", ["sol:E006", "son55:E017"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Relative inference time and the '12% of cost' claim (time-based) and "
                        "a component time split are reported; no token/$ ledger, buffer construction not amortised, not budget-matched.",
                        ["sol:E005", "son55:E016"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read; ratings rest on text. v1 page images used only as non-binding corroboration.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", "retained", "task", "sol", "retained",
                "The v2 text itself reports a store-on/store-off contrast over four rounds of newly sampled questions (son55:E018–E020): "
                "retained changes help later tasks, which meets 'retained' (holdout 'preferably' independent). Weak holdout is scored in "
                "E.holdout=1. Not dependent on figure values; v1 Fig. 9 (opus:O03) only corroborates.",
                ["son55:E018", "son55:E019", "son55:E020", "sol:E003", "opus:O03"], "none (evidence_level never scores)"),
            res("rs_pattern.matches", *conflict(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["decompose_and_delegate", "C25"]],
                "C03 step 3 covers retrieval over a reference bank without upstream tuning; C25 captures executable templates routed "
                "to interpreter/python-chess, the source of the largest gains.", ["son55:E007", "son55:E015", "son55:E024"],
                "none (patterns never score)"),
            res("domain_pattern.matches", *conflict(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"]],
                "Kept son55's two matches but H03 demoted to low-fit secondary: parent claims gain from near-raw precedent whereas "
                "BoT abstracts; the retrieve/re-bind/append operation still matches.", ["son55:E007", "son55:E021"],
                "none (patterns never score)"),
            res("expectations[local:2406.04271-1].status", "partial", "unmet", "son55", "unmet",
                "Same question both seats. PAL is code-based but lacks python-chess and templates; confound uncontrolled.",
                ["son55:E015", "son55:E024", "sol:E008"], "none; consistent with E.causality=2"),
            res("expectations[local:2406.04271-2].status", "partial", "unmet", "revised",
                "local-2 = sol's cost question → partial; son55's local-2 (statistics) kept as local:2406.04271-3 = unmet",
                "Same ID, different questions; both verified.", ["sol:E005", "son55:E017"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-1].status", None, "partial", "son55", "partial",
                "Verified: meta-buffer-off ablation exists; no equal-data raw-case/longer-context control.", ["son55:E018"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-2].status", None, "unmet", "son55", "unmet",
                "Verified: no overlap/contamination analysis between buffer contents and evaluation items.", ["son55:E021"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-3].status", None, "unmet", "son55", "unmet",
                "Verified: no nearest-neighbour, longer-context or few-shot retrieval baseline.", ["son55:E023"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-6].status", None, "partial", "revised", "unmet",
                "Only a limitation sentence and a template-count chart; no sensitivity experiment on source quality or coverage.",
                ["son55:E022", "son55:E021"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-1].status", None, "partial", "son55", "partial",
                "Verified: time, not tokens/calls; construction cost missing.", ["son55:E016"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-5].status", None, "partial", "son55", "partial",
                "Verified: PAL/ToT compared but library/code access differs.", ["son55:E015"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/F5].status", None, "unmet", "son55", "unmet",
                "Verified: storage is not conditioned on an outcome signal (failure mode present).", ["son55:E004", "opus:O01"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00].status", "partial", None, "sol", "partial",
                "Only sol asked the H00 retained-store question; verified: four-round manager-off contrast, no frozen-store holdout.",
                ["sol:E003", "sol:E004"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S1].status", None, "met", "son55", "met",
                "Verified: names manually designed exemplars/reasoning structures as the fixed object made learnable.",
                ["son55:E002"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S2].status", None, "unmet", "son55", "unmet",
                "Verified: templates distilled from single solutions; no success/failure contrast.", ["son55:E006"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S3].status", "partial", "unmet", "son55", "unmet",
                "Solutions supply content but no grounding signal decides insertion (opus:O01).", ["son55:E004", "opus:O01"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S4].status", None, "partial", "son55", "partial",
                "Verified: novelty threshold deduplicates; no merge/forget/conflict handling.", ["son55:E005"], "none"),
            res("expectations[rsi:index_experience_for_reuse/F3].status", None, "unmet", "son55", "unmet",
                "Verified for the round ablation (buffer grows from benchmark stream); unstated for Table 1.",
                ["son55:E018", "son55:E021"], "none; consistent with E.holdout=1"),
            res("expectations[rsi:index_experience_for_reuse/F4].status", None, "unmet", "son55", "unmet",
                "Verified: model outputs enter the buffer without external check.", ["son55:E004", "opus:O01"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S2].status", None, "unmet", "son55", "unmet",
                "Verified: write gate is novelty only.", ["son55:E004", "son55:E005"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S5].status", None, "partial", "son55", "partial",
                "Verified: store-off ablations exist (text), single run.", ["son55:E018", "son55:E020"], "none"),
            res("ratings.G", *conflict(p, "ratings.G"), "son55", {"status": "resolved", "rating": 2},
                "Nearest experience-abstraction neighbours absent from discussion and comparison.", ["son55:E002", "son55:E003"],
                "−3.75 vs sol"),
            res("ratings.M", *conflict(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "Key reuse assumption rests on unverified single solutions; no distinguishing prediction vs raw-case retrieval.",
                ["son55:E006", "opus:O01"], "−5.0 vs sol"),
            res("ratings.X", *conflict(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "No correctness gate/retirement; main-run buffer state unspecified.", ["son55:E004", "son55:E021"], "−5.0 vs sol"),
            res("ratings.E.measurement", *conflict(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "Eval sizes unreported, Sonnet metric unspecified, inconsistent headline deltas.", ["son55:E013", "son55:E014"],
                "−2.5 vs sol"),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope: retained template buffer with novelty-only admission (no correctness gate); "
                                                   "store-off round ablation supports scoped retained reuse; executable templates are a "
                                                   "major attribution confound; protocol details (eval sizes, buffer init) missing.",
            "integrity_checks": "Both seats a1 on 2406.04271v2 text sha e0467491…; canonical seat hashes match. Page-image package "
                                "declares v1 and p-01 shows 'arXiv:2406.04271v1 … 6 Jun 2024' — version mismatch with pinned v2, "
                                "reported to controller.",
            "figure_values_policy": "Opus read v1 Figs 3–10. No resolution changes a seat-disputed value on the basis of figure "
                                    "values; evidence_level=retained rests on v2 text (son55:E018–E020). Hence no a3 needed.",
            "rating_agreement": "4/8 identical and re-checked; G, M, X, E.measurement resolved for son55.",
        },
    }

    # =========================================================== 2406.18532 Symbolic Learning
    p = "2406.18532"
    S[p] = {
        "base": "son55",
        "a3": "none",
        "opus_evidence": [],
        "rs_pattern": {
            "primary": "relax_discrete_search_to_continuous", "supporting": ["generative_process_redesign"], "outside_taxonomy": False,
            "reason": "Opus revision combining both seats. The paper's own move is to replace combinatorial prompt/pipeline search "
                      "(DSPy, GPTSwarm) with a gradient-analogue joint update of all symbolic components — the parent's 'relax and "
                      "jointly optimize structure' signature, with C22 (reify hand-engineered pipeline as one configuration space) as "
                      "the only sub; no real relaxation or amortization, so fit is low-medium. sol's generative_process_redesign is kept "
                      "as supporting for the 'fixed engineering component freed' framing.",
            "matches": [
                {"main_id": "relax_discrete_search_to_continuous", "sub_id": "C22", "role": "primary", "fit": "low-medium",
                 "tactic_steps_checked": ["name hand-engineered artifact", "unified configuration space", "collapse search (absent)",
                                          "validate vs strong baselines (partial)"],
                 "success_checks": ["joint optimisation of prompts/tools/pipeline"],
                 "failure_checks": ["no ablation of load-bearing step", "no cost/amortisation"],
                 "evidence_ids": ["son55:E001", "son55:E025", "sol:E003"], "reason": "son55 primary accepted."},
                {"main_id": "generative_process_redesign", "sub_id": None, "role": "supporting", "fit": "low",
                 "tactic_steps_checked": ["fixed component named"], "success_checks": [], "failure_checks": ["no load-bearing ablation"],
                 "evidence_ids": ["sol:E010", "son55:E002"], "reason": "sol's main-level match kept as supporting."}],
            "executes_pattern": "partial", "resolves_problem": "unresolved: joint-vs-isolated advantage untested",
        },
        "domain_pattern": None,  # filled from son55 below (both seats identical H09)
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2406.18532-1"): "local:2406.18532-3",
                    ("son55", "local:2406.18532-2"): "local:2406.18532-4"},
            overrides={"rsi:attribute_and_patch_incumbent/F4": {
                "status": "partial",
                "reason": "Opus revision: on the three standard benchmarks the language loss can be given ground-truth labels "
                          "(sol:E001), so self-constructed validation replaces ground truth only on the open-ended tasks and in "
                          "the claimed unsupervised mode; failure mode partially present."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "task",
            "claim_support": "scoped",
            "strongest_supported_claim": "A reconstructable loss→textual-gradient→optimizer recipe with rollback; author-reported scores of "
                                         "the optimised Agents pipelines exceed listed baselines in most reported cells under an "
                                         "undisclosed train/test protocol. Joint-vs-isolated advantage, retained generalisation and "
                                         "unsupervised deployed self-evolution are not established.",
            "unresolved": ["train/test split and sample sizes", "cost", "per-component ablations", "AgentOptimizer/GPTSwarm comparison",
                           "reliability of label-free loss"]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Concrete manual-engineering gap and named neighbours; 'isolated "
                   "optimisation → local optimum' is an analogy, untested; AgentOptimizer/GPTSwarm not compared.",
                   ["son55:E002", "son55:E003", "sol:E010"]),
            "M": R("resolved", 2, "Opus sides with son55. The chain is reconstructable, but its central causal claim (holistic "
                   "back-propagated critiques avoid local optima) rests on the neural-network analogy with no derivative "
                   "guarantee, and acceptance is a rollback on the same example scored by an LLM loss — key assumptions weak "
                   "(2 anchor). sol's own reason ('analogy supplies no derivative guarantee or reliable credit') states this.",
                   ["son55:E007", "son55:E008", "sol:E002", "sol:E005"], ["son55:E003"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Prompts and atomic pipeline edits given; training-set size, epochs, batch "
                   "size, optimizer model and pipeline-edit acceptance are missing.", ["son55:E009", "son55:E010", "sol:E004"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Standard metrics for QA/math/code; GPT-4 score and a 1–4 "
                               "executability rubric without validation; text claims 'consistently improves over all' while "
                               "HumanEval GPT-3.5 DSPy 66.7 > 64.5.", ["sol:E006", "sol:E007", "son55:E011", "son55:E012", "son55:E013"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Whole-system baselines only; no ablation of gradients, "
                             "joint update, any optimizer or rollback; budgets unknown.", ["son55:E014", "son55:E015", "sol:E003"]),
            "E.holdout": R("not_reported", 0, "Both seats not_reported; re-checked: no split, training-set size or selection data stated "
                           "anywhere.", [], [],
                           ["Entire pinned v1 text: §§1–5, Algorithm 1, Tables 1–6, Appendices A–B."]),
            "E.statistics": R("not_reported", 0, "Opus sides with son55 (A2 ladder). Level 1 requires reported sample sizes; no "
                              "evaluation-set sizes, repeats, seeds or intervals are given for Tables 1–3 (software dev = one integer "
                              "per named game). Negative cells alone do not lift it to 1.", [], [],
                              ["Tables 1–3 and captions", "§4.1 settings", "§4.2–4.3 results/analysis", "Appendices A–B"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked: no calls/tokens/time/$ or budget matching.", [], [],
                        ["§3 method", "§4 experiments", "Appendices A–B", "conclusion (no limitations section)"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text; protocol, statistics and cost absent in the paper itself (not_reported with search scope), "
                  "not a material gap.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.claim_support", "scoped", "unresolved", "sol", "scoped",
                "Calibration precedent (cal-dev 1112.5309, no experiments → scoped) applies claim_support to the central claim with "
                "a narrower supported conclusion. Here the reconstructable recipe and author-reported table gains support a narrow "
                "statement; the broader parts (joint-vs-isolated, unsupervised self-evolution, generalisation) are listed as "
                "unresolved in the assessment rather than making the whole claim unresolved.",
                ["son55:E012", "son55:E013", "sol:E003"], "none"),
            res("rs_pattern.primary", "generative_process_redesign", "relax_discrete_search_to_continuous", "son55",
                "relax_discrete_search_to_continuous",
                "The authors position against combinatorial search (DSPy/GPTSwarm) and replace it with a gradient-analogue joint "
                "update — the relax-and-jointly-optimize signature; generative_process_redesign's definition targets staged "
                "generative procedures and fits only at the framing level.", ["son55:E001", "son55:E025", "sol:E010"],
                "none (patterns never score)"),
            res("rs_pattern.matches", *conflict(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["relax_discrete_search_to_continuous", "C22"]],
                "Primary relax/C22 (son55) plus sol's generative_process_redesign as supporting; they answer different aspects.",
                ["son55:E001", "sol:E010"], "none (patterns never score)"),
            res("expectations[local:2406.18532-1].status", "partial", "unmet", "revised",
                "local-1 = sol's measurement question → partial; son55's local-1 (no split) renamed local-3 and merged with sol's "
                "identical local-3 = unmet",
                "Same ID, different questions. son55-1 and sol-3 ask the same holdout question.", ["sol:E006", "sol:E007"], "none"),
            res("expectations[local:2406.18532-3].status", "unmet", None, "same_supported_fact", "unmet",
                "son55 asked the same question as its local-1 (no split/sizes/epochs); merged. Note: local-2 is 'unmet' in both seats "
                "but asks different questions (sol: per-axis toggles; son55: HumanEval contradiction) — son55's kept as local-4.",
                ["sol:E005"], "none; consistent with E.holdout=0"),
            res("expectations[rs:relax_discrete_search_to_continuous/RE-1].status", None, "unmet", "son55", "unmet",
                "Verified: no ablation of gradients, joint update or optimizers.", ["son55:E014"], "none"),
            res("expectations[rs:relax_discrete_search_to_continuous/RE-2].status", None, "unmet", "son55", "unmet",
                "Verified: no optimizer cost/amortisation.", [], "none"),
            res("expectations[rs:relax_discrete_search_to_continuous/RE-3].status", None, "partial", "son55", "partial",
                "Verified: DSPy/AutoPE/ToT compared; AgentOptimizer/GPTSwarm only cited.", ["son55:E011", "son55:E016"], "none"),
            res("expectations[rs:relax_discrete_search_to_continuous/RE-5].status", None, "unmet", "son55", "unmet",
                "Verified: no seeds/intervals.", [], "none"),
            res("expectations[rs:relax_discrete_search_to_continuous/RE-6].status", None, "partial", "son55", "partial",
                "Verified: config language and atomic ops described; training settings missing.", ["son55:E025", "son55:E024"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/F4].status", None, "unmet", "revised", "partial",
                "Ground-truth labels can enter the loss on standard benchmarks (sol:E001/son55:E005); self-constructed validation "
                "applies to open-ended tasks and the unsupervised mode only.", ["sol:E001", "son55:E005", "son55:E019"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/F5].status", None, "unmet", "son55", "unmet",
                "Verified: nothing checks that the edited node caused the failure.", ["son55:E007"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/H09].status", "partial", None, "sol", "partial",
                "Only sol asked the H09 sub-condition; verified.", ["sol:E002", "sol:E004", "sol:E005"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S1].status", None, "partial", "son55", "partial",
                "Verified: node-level gradients along the whole chain.", ["son55:E007"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S3].status", None, "partial", "son55", "partial",
                "Verified: per-example rollback on LLM loss, illegal edits discarded.", ["son55:E008", "son55:E009"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S4].status", None, "unmet", "son55", "unmet",
                "Verified: per-example updates; batching aggregates gradients per node but no cross-task diagnosis.",
                ["son55:E010"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S5].status", None, "partial", "son55", "partial",
                "Verified: trajectories stored, critique passed via LLM summaries.", ["son55:E007"], "none"),
            res("expectations[rsi:attribute_and_patch_incumbent/S6].status", None, "met", "son55", "met",
                "Verified: one framework for prompts/tools/pipeline across five tasks.", ["son55:E001", "son55:E025"], "none"),
            res("expectations[rsi:search_agent_architecture/F1].status", None, "unmet", "son55", "unmet",
                "Verified: all axes co-optimised without axis-level ablation (failure mode present).", ["son55:E014"], "none"),
            res("ratings.M", *conflict(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "Central causal mechanism is an untested analogy; acceptance by same-example LLM loss.",
                ["son55:E007", "son55:E008", "sol:E002"], "−5.0 vs sol"),
            res("ratings.E.statistics", *conflict(p, "ratings.E.statistics"), "son55",
                {"status": "not_reported", "rating": 0},
                "A2 level 1 needs reported sample sizes; none for any main table.", [], "−1.25 vs sol"),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (prompts/tools/pipeline config edited and kept). Evidence is task-level: "
                                                   "no split, sizes, seeds, ablations or cost; HumanEval cell contradicts 'consistently'.",
            "integrity_checks": "Both seats a1 on 2406.18532v1 sha 3bc20eab…; seat hashes match; ids valid.",
            "son55_hint_check": "son55's E.holdout/statistics/cost not_reported verified by full read: none of the three is reported "
                                "anywhere in the pinned text, including Appendices A–B.",
            "rating_agreement": "6/8 identical and re-checked; M and E.statistics resolved for son55.",
        },
    }

    # =========================================================== 2407.08937 SE-GPT
    p = "2407.08937"
    S[p] = {
        "base": "son55",
        "a3": "optional: sol supplied no ratings (deferred on the Appendix E question). Final ratings rest on son55 plus Opus "
              "independent re-check of every item. If the controller wants a second independent seat on the score, dispatch sol "
              "a3 for all eight items with the material ruling below.",
        "opus_evidence": [
            opus_ev(p, "O01", "In this section, we demonstrate examples of our framework.", "Appendix E heading text; raw line 6157",
                    "The externally hosted continuation carries illustrative execution examples only. All results, ablations, human "
                    "evaluations (Tables 1–7) and token costs (A.4) are in the pinned text, so the external pages are author-side "
                    "supplementary content (not_reported in search_scope), not a material gap for any scored item."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "son55 accepted after card check: without labels the system manufactures practice questions, answers them, and "
                      "filters by web-grounded LLM verification, using the result as its adaptation signal (C08 generate→gate, with "
                      "experience induction instead of retraining, low-medium fit). Conditioning the frozen model on stored task "
                      "experience is the supporting adapt_via_conditioning move (C03 retrieval-to-bank branch, low).",
            "matches": [
                {"main_id": "self_supervised_signal_engineering", "sub_id": "C08", "role": "primary", "fit": "low-medium",
                 "tactic_steps_checked": ["generator reaching new region (web-grounded questions)", "single quality gate (LLM+Wikipedia check)",
                                          "retrain (replaced by induction)"],
                 "success_checks": ["filter exists and is evaluated (87.7% human-checked accuracy)"],
                 "failure_checks": ["signal not used to train; no cost-benefit"],
                 "evidence_ids": ["son55:E005", "son55:E028"], "reason": "son55 primary accepted."},
                {"main_id": "adapt_via_conditioning", "sub_id": "C03", "role": "supporting", "fit": "low",
                 "tactic_steps_checked": ["retrieve from bank, condition frozen model"], "success_checks": [],
                 "failure_checks": ["no category holdout"], "evidence_ids": ["son55:E002", "sol:E002"],
                 "reason": "Consistent with the BoT ruling on C03."}],
            "executes_pattern": "partial", "resolves_problem": "partial: author-reported 3.8/5.3pp gains in-stream; retained growth not measured",
        },
        "domain_pattern": None,
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2407.08937-2"): "local:2407.08937-3"},
            drop={("sol", "local:2407.08937-1")},
            overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Memory grows on the evaluated stream (inputs only); no frozen-memory held-out evaluation and no "
                                   "accuracy-vs-stream-position curve, so retained benefit is not separately shown.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: in a label-free online setting where memory is built from the evaluated stream's "
                                         "inputs, SE-GPT averages 3.8/5.3pp above zero-shot GPT-3.5/GPT-4 and above cheap experience/"
                                         "demonstration baselines, at ~70× zero-shot-CoT tokens.",
            "unresolved": ["accuracy vs stream position", "independent held-out tasks", "budget-matched memory-off control",
                           "GPT-4 lacks AutoP-ICL / Modified Self-ICL rows"]},
        "ratings": {
            "G": R("resolved", 3, "son55 3 accepted after Opus re-check (sol unknown, see resolution). Gap (manual acquisition and "
                   "selection of experience; environment feedback unavailable for NLP; noisy self-generated demonstrations) is "
                   "sourced, nearest neighbours named and Self-ICL family run; skill-library neighbours not compared.",
                   ["son55:E003", "son55:E004"]),
            "M": R("resolved", 3, "son55 3 accepted after re-check. Categorise → transfer → web-grounded practice with check → "
                   "contrastive induction → merge → skip rule; AutoP-ICL and Self-EXP give distinguishing predictions; verifier is "
                   "an LLM with ~12% error.", ["son55:E005", "son55:E014", "son55:E028"], ["son55:E028"]),
            "X": R("resolved", 2, "son55 2 accepted after re-check. Parameters and all prompts given; induced experience overwrites "
                   "memory without a utility gate, no versioning/rollback, skip rule based on self-check.",
                   ["son55:E002", "son55:E006", "son55:E030"], ["son55:E006"]),
            "E.measurement": R("resolved", 3, "son55 3 accepted after re-check. Labelled standard datasets, accuracy, 1000/500 per set; "
                               "human module evaluations by three graduate annotators without agreement statistics.",
                               ["son55:E009", "son55:E010", "son55:E024", "sol:E003"]),
            "E.causality": R("resolved", 2, "son55 2 accepted after re-check. Seven baselines plus w/o-transfer/w/o-induction "
                             "ablations; ablation gaps 1–1.5pp; no budget-matched memory-off control; GPT-4 rows incomplete.",
                             ["son55:E014", "son55:E017", "son55:E019", "son55:E020"], ["son55:E017"]),
            "E.holdout": R("resolved", 1, "son55 1 accepted after re-check. Labels never used, but memory is built from the same "
                           "evaluated stream (opus-verified sol:E002/son55:E007); no frozen-memory or independent held-out "
                           "evaluation. Same treatment as BoT's in-stream rounds.", ["son55:E007", "son55:E008", "sol:E002"]),
            "E.statistics": R("resolved", 1, "son55 1 accepted after re-check: sizes and three-round means, no intervals or "
                              "order variance.", ["son55:E009", "son55:E010"]),
            "E.cost": R("resolved", 3, "son55 3 accepted after re-check. Per-module token ledger including retries and API errors, "
                        "run time (≈5 days GPT-3.5; 3–5× for GPT-4), ~70× zero-shot-CoT tokens openly discussed; baselines not "
                        "budget-matched keeps it below 4.", ["son55:E022", "son55:E023", "sol:E007"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text. Appendix E's external Google-Drive continuation holds illustrative examples only "
                  "(opus:O01); treated as author-side supplementary content, not a material gap. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": (
            [res("assessment.claim_support", "unresolved", "scoped", "son55", "scoped",
                 "sol's 'unresolved' followed only from its needs_fulltext deferral; with the material ruling, the in-stream author "
                 "report supports a scoped claim.", ["son55:E011", "opus:O01"], "none"),
             res("rs_pattern.primary", "adapt_via_conditioning", "self_supervised_signal_engineering", "son55",
                 "self_supervised_signal_engineering", "Load-bearing novelty is label-free manufacture and filtering of the "
                 "adaptation signal; conditioning is the delivery channel.", ["son55:E005", "son55:E028"], "none (patterns never score)"),
             res("rs_pattern.matches", *conflict(p, "rs_pattern.matches"), "son55",
                 [["adapt_via_conditioning", "C03"], ["self_supervised_signal_engineering", "C08"]],
                 "Accepted after card check (see rs_pattern.reason).", ["son55:E005", "son55:E002"], "none (patterns never score)"),
             res("expectations[local:2407.08937-2].status", "partial", "unmet", "revised",
                 "local-2 = sol's cost-reporting question → partial; son55's local-2 (no budget matching) kept as local:2407.08937-3 = unmet",
                 "Same ID, different questions; both verified (Table 7 ledger exists; no budget-matched baselines). Also: both seats "
                 "had local-1 = unmet with different questions; sol's local-1 (missing continuation) is withdrawn by the material "
                 "ruling and son55's local-1 (accuracy vs stream position) is kept.", ["son55:E023", "sol:E007"], "none")]
            + [res(f"expectations[{eid}].status", sv, nv, dec, fv, why, ev, "none") for eid, sv, nv, dec, fv, why, ev in [
                ("rs:adapt_via_conditioning/RE-3", None, "partial", "son55", "partial",
                 "Verified: Self-EXP/Self-ICL compared; no kNN/longer-context baseline.", ["son55:E015"]),
                ("rs:self_supervised_signal_engineering/RE-2", None, "partial", "son55", "partial",
                 "Verified: AutoP-ICL/Self-EXP partly isolate; no equal-compute memory-off.", ["son55:E014", "son55:E015"]),
                ("rs:self_supervised_signal_engineering/RE-3", None, "met", "son55", "met",
                 "Verified: downstream accuracy on six datasets.", ["son55:E013", "son55:E018"]),
                ("rs:self_supervised_signal_engineering/RE-5", None, "partial", "son55", "partial",
                 "Verified: cost reported but no benefit/cost trade-off.", ["son55:E023"]),
                ("rs:self_supervised_signal_engineering/RE-6", None, "partial", "son55", "partial",
                 "Verified: label-free and deployment-like, but stream-order and cold-start assumptions unexamined.", ["son55:E027"]),
                ("rsi:abstract_experience_into_guidance/F5", None, "met", "son55", "met",
                 "Verified: store is grounded in verified practice (failure mode avoided, weakly).", ["son55:E005", "son55:E028"]),
                ("rsi:abstract_experience_into_guidance/H00", "partial", None, "sol", "partial",
                 "Only sol asked the H00 sub-condition; verified (contrastive induction, reuse, no frozen-store split).", ["sol:E002"]),
                ("rsi:abstract_experience_into_guidance/S1", None, "met", "son55", "met",
                 "Verified: manual acquisition/selection named as the fixed object.", ["son55:E003"]),
                ("rsi:abstract_experience_into_guidance/S2", None, "met", "son55", "met",
                 "Verified: induction contrasts correct vs incorrect examples.", ["son55:E005"]),
                ("rsi:abstract_experience_into_guidance/S3", None, "partial", "son55", "partial",
                 "Verified: LLM + Wikipedia check, ~12% error.", ["son55:E028"]),
                ("rsi:abstract_experience_into_guidance/S4", None, "partial", "son55", "partial",
                 "Verified: merge/dedup, 20-insight cap, no forgetting.", ["son55:E030"]),
                ("rsi:abstract_experience_into_guidance/S5", None, "unmet", "son55", "unmet",
                 "Verified: induced experience replaces memory with no utility gate.", ["son55:E002", "son55:E006"]),
                ("rsi:evidence_gated_retention/S1", None, "unmet", "son55", "unmet",
                 "Verified: no per-entry marginal measurement.", ["son55:E019"]),
                ("rsi:index_experience_for_reuse/F3", None, "unmet", "son55", "unmet",
                 "Verified: memory grows from the evaluated stream (failure mode present).", ["son55:E007"]),
            ]]
            + [res(f"ratings.{k}", {"status": "unknown", "rating": None}, {"status": "resolved", "rating": v}, "son55",
                   {"status": "resolved", "rating": v},
                   "sol deferred every item because Appendix E continues on an external Drive link. Opus read the pinned text: "
                   "Appendix E is 'examples of our framework' (opus:O01) and carries no evidence for any scored item, so the "
                   "deferral does not apply; son55's value was re-checked against the text and kept (see ratings." + k + ").",
                   ["opus:O01"] + ev, "fixes this item; total score 58.75")
               for k, v, ev in [("G", 3, ["son55:E003"]), ("M", 3, ["son55:E005"]), ("X", 2, ["son55:E006"]),
                                ("E.measurement", 3, ["son55:E009"]), ("E.causality", 2, ["son55:E019"]),
                                ("E.holdout", 1, ["son55:E007"]), ("E.statistics", 1, ["son55:E010"]),
                                ("E.cost", 3, ["son55:E023"])]]
            + [res("status", "needs_fulltext", "reviewed", "son55", "reviewed",
                   "Controller's fact ruling independently verified: the external continuation holds only illustrative examples; "
                   "per production convention author-hosted external content is not a material gap unless it carries core "
                   "evidence, which it does not here.", ["opus:O01", "sol:E001"], "enables scoring (58.75)")]
        ),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A-class online textual-experience memory). Label-free, but memory built "
                                                   "from the evaluated stream; honest token-cost ledger; small ablation gaps.",
            "integrity_checks": "Both seats a1 on 2407.08937v1 sha c7b89795…; sol marked materials.complete=false citing Appendix E; "
                                "Opus ruling: complete for scoring. Seat hashes match.",
            "single_seat_basis": "Score-bearing ratings come from son55 + Opus re-check because sol deferred; see a3 note.",
            "rating_agreement": "All 8 items: sol unknown vs son55 resolved; all resolved to son55's values after independent re-check.",
        },
    }

    # =========================================================== 2408.08435 ADAS
    p = "2408.08435"
    S[p] = {
        "base": "sol",
        "a3": "none",
        "opus_evidence": [
            opus_ev(p, "O01", "We evaluate all discovered agents on the held-out test set and report the test accuracy in",
                    "§4.1 ARC setup; raw line 550",
                    "Every ARC design is scored on the test set, and the ARC transfer agents are then chosen by that test accuracy "
                    "(sol:E004)."),
            opus_ev(p, "O02", "\\mathbf{53.4\\pm 3.5}", "Table 1 MGSM 'Meta Agent Search' cell (raw line 937) and Table 2 "
                    "'Dynamic Role-Playing Architecture' MGSM cell (raw line 1265)",
                    "The single Table 1 MGSM number equals the MGSM test score of the first of the 'top 3 agents from MGSM' whose "
                    "ranking criterion is never stated (son55:E016); together with the explicit ARC test-ranking, the headline "
                    "per-domain numbers are plausibly best-of-~30 on the test set.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "relax_discrete_search_to_continuous", "supporting": ["generative_process_redesign"], "outside_taxonomy": False,
            "reason": "Opus revision combining both seats (same treatment as 2406.18532). C22 explicitly covers reifying an agent/"
                      "workflow topology as an executable-code search variable, with rediscovery/transfer validation; the parent's "
                      "relaxation/amortisation step is absent (LLM-proposal discrete search), so fit is low-medium. sol's "
                      "generative_process_redesign kept as supporting framing.",
            "matches": [
                {"main_id": "relax_discrete_search_to_continuous", "sub_id": "C22", "role": "primary", "fit": "low-medium",
                 "tactic_steps_checked": ["name hand-engineered artifact", "unified code representation", "collapse search (absent)",
                                          "strong baselines + transfer"],
                 "success_checks": ["executable-code space", "cross-domain/model transfer"],
                 "failure_checks": ["no archive ablation", "single search run"],
                 "evidence_ids": ["son55:E001", "son55:E003", "sol:E001"], "reason": "son55 primary accepted."},
                {"main_id": "generative_process_redesign", "sub_id": None, "role": "supporting", "fit": "low",
                 "tactic_steps_checked": ["fixed component named"], "success_checks": [], "failure_checks": ["no load-bearing ablation"],
                 "evidence_ids": ["sol:E001", "son55:E002"], "reason": "sol's main-level match kept as supporting."}],
            "executes_pattern": "partial", "resolves_problem": "partial: DROP/MGSM gains with test CIs; archive causality untested",
        },
        "domain_pattern": None,
        "pattern_mapping": None,
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2408.08435-1"): "local:2408.08435-3",
                    ("son55", "local:2408.08435-2"): "local:2408.08435-4"},
            overrides={
                "rsi:search_agent_architecture/S1": {
                    "status": "partial",
                    "reason": "Opus: the scored archive is the search-shaping primitive (present), but the card's condition is that "
                              "accepted members win through it; no archive-off run shows that, and empty initialisation keeps the "
                              "archive mechanism (sol)."},
                "rsi:search_agent_architecture/S3": {
                    "status": "partial",
                    "reason": "Opus revision: validation outcome is computed and fed back, but every runnable design is added to "
                              "the archive — no outcome gate decides what persists; deployment choice is by (test) ranking."},
            }),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Searched agent code is frozen and reused on held-out target domains/models (GSM8K, GSM-Hard, "
                                   "other FMs); source-domain headline numbers are likely test-selected.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: offline archive-conditioned code search yields agents that beat hand-designed "
                                         "baselines with test CIs on DROP and MGSM and transfer to unseen math sets and other FMs; "
                                         "smaller domains within CI; not isolated archive causality, not improver-level.",
            "unresolved": ["selection rule for Table 1 agents", "archive-off and budget-matched controls", "single search run per domain"]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked.", ["sol:E001", "son55:E002", "son55:E003"]),
            "M": R("resolved", 3, "Both seats 3; re-checked: archive→propose→reflect→debug→validate→archive is clear; archive "
                   "hypothesis untested; novelty self-judged.", ["sol:E001", "sol:E002", "son55:E026", "son55:E027"], ["son55:E024"]),
            "X": R("resolved", 3, "Both seats 3; re-checked: prompts, framework, pseudocode, splits, iterations given; reported-agent "
                   "selection rule unstated; append-only archive.", ["sol:E002", "sol:E005", "son55:E004", "son55:E006"],
                   ["sol:E008"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked: objective accuracy/F1 with bootstrap CIs; baselines in same "
                               "framework; ARC easy subset, 60 test items.", ["sol:E003", "sol:E006", "son55:E025"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked: strong hand baselines + OPRO + empty-init; no archive/"
                             "reflection ablation; discovered agents use more calls, unmatched.", ["son55:E011", "son55:E019", "sol:E009"],
                             ["son55:E030"]),
            "E.holdout": R("resolved", 2, "Opus sides with sol. Validation/test splits are real and transfer to GSM8K/GSM-Hard/other "
                           "FMs is clean holdout for the frozen agents. But ARC agents are explicitly ranked on the test set "
                           "(sol:E004, opus:O01) and Table 1's single per-domain number equals the MGSM test score of a 'top' agent "
                           "whose ranking criterion is unstated (opus:O02): the source-domain headline is plausibly best-of-~30 on "
                           "test (EVIDENCE rule 2). A key control gap at the 2 anchor; son55 noted the same deductions but under-"
                           "weighted that they hit the headline rows themselves.",
                           ["sol:E003", "sol:E005", "son55:E016", "son55:E017"], ["sol:E004", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked: test bootstrap CIs (A2 level 2); one search per domain.",
                              ["sol:E006", "son55:E009", "son55:E014"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked: ~$500 ARC / ~$300 per domain search+eval; no per-agent inference "
                        "ledger or budget matching.", ["sol:E009", "son55:E020"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text including Appendices A–J; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": (
            [res("rs_pattern.primary", "generative_process_redesign", "relax_discrete_search_to_continuous", "son55",
                 "relax_discrete_search_to_continuous", "C22 explicitly names agent/workflow topology in an executable-code "
                 "representation; generative_process_redesign targets staged generative procedures.", ["son55:E001", "son55:E003"],
                 "none (patterns never score)"),
             res("rs_pattern.matches", *conflict(p, "rs_pattern.matches"), "revised",
                 [["generative_process_redesign", None], ["relax_discrete_search_to_continuous", "C22"]],
                 "Primary relax/C22 plus sol's main-level match as supporting.", ["son55:E001", "sol:E001"],
                 "none (patterns never score)"),
             res("expectations[local:2408.08435-1].status", "partial", "unmet", "revised",
                 "local-1 = sol's statistics question → partial; son55's local-1 (ARC test selection) kept as local:2408.08435-3 = unmet",
                 "Same ID, different questions; both verified.", ["sol:E006", "son55:E015"], "none"),
             res("expectations[local:2408.08435-2].status", "partial", "unmet", "revised",
                 "local-2 = sol's cost-reporting question → partial; son55's local-2 (budget matching) kept as local:2408.08435-4 = unmet",
                 "Same ID, different questions; both verified.", ["sol:E009", "son55:E020"], "none")]
            + [res(f"expectations[{eid}].status", sv, nv, dec, fv, why, ev, "none") for eid, sv, nv, dec, fv, why, ev in [
                ("rs:relax_discrete_search_to_continuous/RE-1", None, "unmet", "son55", "unmet",
                 "Verified: archive/reflection not ablated.", ["son55:E019"]),
                ("rs:relax_discrete_search_to_continuous/RE-2", None, "partial", "son55", "partial",
                 "Verified: $ cost given, no amortisation/inference cost.", ["son55:E020"]),
                ("rs:relax_discrete_search_to_continuous/RE-3", None, "partial", "son55", "partial",
                 "Verified: OPRO run; graph-search neighbours only discussed.", ["son55:E011", "son55:E003"]),
                ("rs:relax_discrete_search_to_continuous/RE-4", None, "partial", "son55", "partial",
                 "Verified: strong math/model transfer; MMLU transfer cell 62.4 < CoT 65.4.", ["son55:E017"]),
                ("rs:relax_discrete_search_to_continuous/RE-5", None, "partial", "son55", "partial",
                 "Verified: CIs, single search.", ["son55:E014"]),
                ("rs:relax_discrete_search_to_continuous/RE-6", None, "met", "son55", "met",
                 "Verified: framework, prompts, pseudocode given.", ["son55:E004", "son55:E027"]),
                ("rsi:population_search_executable_fitness/S2", None, "met", "son55", "met",
                 "Verified: ground-truth accuracy as fitness.", ["son55:E004"]),
                ("rsi:population_search_executable_fitness/S5", None, "unmet", "son55", "unmet",
                 "Verified: archive not credited by measured effect.", ["son55:E019"]),
                ("rsi:search_agent_architecture/F1", None, "partial", "son55", "partial",
                 "Verified: whole-agent code searched, no axis ablation, single primitive focus.", ["son55:E001"]),
                ("rsi:search_agent_architecture/F3", None, "partial", "son55", "partial",
                 "Verified: validation accuracy plus LLM 'interestingness'.", ["son55:E027"]),
                ("rsi:search_agent_architecture/H17", "partial", None, "sol", "partial",
                 "Only sol asked the H17 sub-condition; verified incl. displayed-code discrepancy.", ["sol:E008", "sol:E002"]),
                ("rsi:search_agent_architecture/S1", "partial", "met", "sol", "partial",
                 "Primitive present; that wins come through it is untested (no archive-off).", ["sol:E001", "son55:E019"]),
                ("rsi:search_agent_architecture/S3", None, "met", "revised", "partial",
                 "All runnable designs enter the archive; no outcome gate on persistence.", ["son55:E006", "sol:E002"]),
                ("rsi:search_agent_architecture/S4", None, "partial", "son55", "partial",
                 "Verified: seeds remain in archive; no retreat rule.", ["son55:E006"]),
                ("rsi:search_agent_architecture/S5", None, "unmet", "son55", "unmet",
                 "Verified: objective unchanged despite expensive evaluation.", ["son55:E020"]),
            ]]
            + [res("ratings.E.holdout", *conflict(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 2},
                   "Headline source-domain rows are test-selected (ARC explicit; MGSM/Table 1 criterion unstated, opus:O02); clean "
                   "holdout is limited to the frozen transfers.", ["sol:E004", "opus:O01", "opus:O02", "son55:E016"],
                   "−2.5 vs son55")]
        ),
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (B/A-class architecture search with retained code archive). Real splits and "
                                                   "CIs; headline agents likely test-ranked; no archive ablation; single search; $ cost given.",
            "integrity_checks": "Both seats a1 on 2408.08435v2 sha 4b9a5ab0…; seat hashes match; ids valid.",
            "rating_agreement": "7/8 identical and re-checked; E.holdout resolved for sol.",
            "expectation_renumbering": "son55 local-1 → local-3, local-2 → local-4 (same ID, different questions).",
        },
    }

    # domain patterns identical across seats for these three papers: take the adopted seat's block, ids prefixed
    import copy
    for pk, s in (("2406.18532", "son55"), ("2407.08937", "son55"), ("2408.08435", "son55")):
        d = copy.deepcopy(g["seat"](s, pk)["domain_pattern"])
        for m in d["matches"]:
            m.setdefault("version", VER)
        S[pk]["domain_pattern"] = g["prefix"](d, s)
    S["2408.08435"]["pattern_mapping"] = (g["prefix"](g["seat"]("son55", "2408.08435")["pattern_mapping"], "son55")
                                          + g["prefix"](g["seat"]("sol", "2408.08435")["pattern_mapping"], "sol"))
    # ADAS domain condition checks: record Opus S1/S3 revisions on the match too
    for m in S["2408.08435"]["domain_pattern"]["matches"]:
        if m.get("sub") == "H17":
            m["opus_condition_note"] = "Opus: S1 partial (archive utility not isolated), S3 partial (no persistence gate); see expectations."
    S["2406.18532"]["pattern_mapping"] = (g["prefix"](g["seat"]("son55", "2406.18532")["pattern_mapping"], "son55")
                                          + g["prefix"](g["seat"]("sol", "2406.18532")["pattern_mapping"], "sol"))
    S["2407.08937"]["pattern_mapping"] = (g["prefix"](g["seat"]("son55", "2407.08937")["pattern_mapping"], "son55")
                                          + g["prefix"](g["seat"]("sol", "2407.08937")["pattern_mapping"], "sol"))
    return S


def batch_notes():
    return [
        "2406.04271 (BoT) a3 recommendation: NOT required. Opus read the page images but no rating or seat-disputed field was "
        "changed on the basis of figure values; evidence_level=retained rests on v2 text (§6). Material issue for the controller: "
        "2406.04271.pages.json declares version 2406.04271v1 and p-01.png shows 'arXiv:2406.04271v1 [cs.CL] 6 Jun 2024' "
        "('Preprint. Under review'), while the manifest pins v2 text (14 Oct 2024). If figure-aware dual ratings are wanted, "
        "re-render v2 pages first, then a3 on E.causality/E.statistics/E.cost only.",
        "2407.08937 (SE-GPT): controller's Appendix-E ruling independently verified (external pages = 'examples of our framework'; "
        "no scored evidence). sol deferred all eight items, so the score rests on son55 + Opus re-check; optional sol a3 if a second "
        "independent seat is required for this paper's score.",
        "2406.18532: son55 hint verified — E.holdout, E.statistics, E.cost absent from the entire pinned text including appendices.",
        "Rating disputes resolved: 2402.11359 G,M→sol (+8.75 vs son55); 2406.04271 G,M,X,Em→son55 (−16.25 vs sol); 2406.18532 "
        "M,Es→son55 (−6.25 vs sol); 2407.08937 all eight→son55 values after material ruling; 2408.08435 Eh→sol (−2.5 vs son55).",
        "Pattern rulings are score-neutral. RS: relax_discrete_search_to_continuous/C22 adopted as primary for both agent-search "
        "papers (2406.18532, 2408.08435) with generative_process_redesign supporting; adapt_via_conditioning/C03 accepted at low "
        "fit for retrieval-to-bank conditioning (BoT, SE-GPT). Domain: 2402.11359 adds crystallize_executable_capability/H06 "
        "(not H07); BoT keeps H03 as low-fit secondary.",
        "Card revision proposals (stage end, not applied): H06/H07 boundary for offline training-pool tool learning; H00/H03 "
        "boundary for de-instantiated procedural templates.",
        "Expectation local-ID collisions (same ID, different questions across seats) renumbered; no score impact.",
    ]
