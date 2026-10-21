"""Opus rulings for r02b a1 (data only; consumed by _build.py)."""
import copy

VER = "rsi-cards@52ff9657"
FULL = "Opus: complete pinned text incl. all tables, algorithms, appendices"


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

    def C(p, f):
        return conflict(p, f)

    # =========================================================== 2502.16796 MobileSteward
    p = "2502.16796"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Similar to the steward in reality, with the accumulation of experience, he will become more "
                    "familiar with the staff about their suitable work.", "§1 Introduction",
                    "The retained-memory (self-evolution) gap is motivated by analogy, not by a measured failure of static "
                    "or exploration-built app memories."),
            opus_ev(p, "O02", "The diversity among apps makes existing methods ineffective in solving tasks on various apps",
                    "§2.1 (after MobileGPT/AutoDroid)",
                    "Experience-memory neighbours (MobileGPT hierarchical app memory, AutoDroid UTG memory) are dismissed in "
                    "one sentence; MobileGPT is not run and the residual vs. its app-specific memory is not argued."),
            opus_ev(p, "O03", "In comparison, our MobileSteward only decreased by 33% as the task complexity increased.",
                    "§4.5.2 Complexity analysis",
                    "The app-oriented decomposition makes a distinguishing prediction (smaller degradation with more apps) that "
                    "is tested; Table 5 values reproduce 33% (0.72→0.48) and MobileAgent-v2 46% (0.26→0.14)."),
            opus_ev(p, "O04", "MobileSteward GPT-4v 0.55 0.76 0.99", "Table 2 (GPT-4v row; whitespace-normalised)",
                    "Table 2 GPT-4v Task Rate 0.76 vs Table 3 full-model 0.81 with identical SR 0.55 / App Rate 0.99: the "
                    "headline ablation row is internally inconsistent with the main table (corroborates son55:E013)."),
            opus_ev(p, "O05", "When updating the Task Guideline Memory, the StewardAgent updates the",
                    "§3.7 Memory-Based Self-Evolution",
                    "M_G receives every self-judged successful (task, guideline) pair; only M_E has a write/no-write decision; "
                    "no merge, forgetting or retirement."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "The paper's load-bearing move is the object-oriented split of a cross-app instruction into per-app tasks "
                      "routed over a DAG to app-specialist agents (decompose_and_delegate, partial: delegates are LLM agents, not "
                      "sound solvers, so C25 is not assigned). The retained memories condition the frozen executors/scheduler "
                      "via retrieval (adapt_via_conditioning, supporting; C03 not assigned: no distribution-level holdout).",
            "matches": [
                smatch("son55", p, "decompose_and_delegate"),
                smatch("son55", p, "adapt_via_conditioning",
                       reason="Supporting: BM25 top-3 success guidelines and the expertise list are injected as conditioning "
                              "with no parameter updates; sol's identical parent match (sol:E002, sol:E008) agrees; C03 not "
                              "assigned (no category-level holdout)."),
            ],
            "executes_pattern": "partial (decomposition + retrieval conditioning instantiated; no sound-solver handoff)",
            "resolves_problem": "partial: large author-reported gains over baselines; retained-memory share small (+0.05 SR, one run)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                {"main": "abstract_experience_into_guidance", "sub": "H00", "version": VER, "fit": "medium-low",
                 "condition_checks": "S3 partial (Steward self-judged success gates extraction; judge error unmeasured); S4 unmet "
                                     "(no consolidation/forgetting; M_G append-only); S5 partial (single LLM write/no-write "
                                     "decision for M_E only); H00 step 4 failure present (memories also updated during the test "
                                     "stream); step 5 partial (evolution-off ablation, no budget match).",
                 "evidence_ids": ["sol:E001", "sol:E015", "son55:E005", "sol:E003", "opus:O05"]},
                {"main": "index_experience_for_reuse", "sub": "H03", "version": VER, "fit": "medium",
                 "condition_checks": "S4 met (BM25 top-3 app-specific cases); S2 partial and F4 present (admission on the "
                                     "model's own success verdict); S5 partial (joint evolution-off ablation, one run); F3 "
                                     "present (store keeps updating on the test stream).",
                 "evidence_ids": ["sol:E008", "son55:E003", "son55:E001", "son55:E002", "sol:E004"]},
            ],
            "unassigned": [],
            "revision_proposals": ["H00/H01 boundary: a single LLM write/no-write decision on a new entry (MobileSteward M_E) "
                                   "is not an H01 editing policy; say so in H01 'when to pick' (stage end, not applied)."],
        },
        "pattern_mapping": [
            {"rs_main": "decompose_and_delegate", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "index_experience_for_reuse", "domain_sub": "H03",
             "operation_correspondence": "Per-app delegation is made adaptive by app-specific precedent retrieval: each StaffAgent "
                                         "reads BM25 top-3 successful (task, guideline) pairs from its own M_G.",
             "necessary_conditions_and_differences": "H03 wants externally gated writes and re-bindable cases; here writes are "
                                                     "gated by the Steward's own verdict and cases are near-raw demonstrations. "
                                                     "The delegation structure itself is static design, not retained change.",
             "evidence_ids": ["son55:E001", "son55:E003", "son55:E005"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H00",
             "operation_correspondence": "Expertise summaries extracted from successful runs condition the frozen Steward's "
                                         "recruitment; guidelines condition StaffAgent planning.",
             "necessary_conditions_and_differences": "H00 asks for contrastive extraction and a frozen store at test; here "
                                                     "extraction uses successes only and the store keeps updating during test.",
             "evidence_ids": ["sol:E001", "sol:E002", "sol:E003"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2502.16796-1"): "local:2502.16796-3",
                    ("son55", "local:2502.16796-2"): "local:2502.16796-4"},
            overrides={"rs:decompose_and_delegate/RE-3": {
                "status": "partial",
                "reason": "Opus revision of son55 'unknown': the complete text was read, so the question is answerable. "
                          "Implementation details are disclosed (model versions, temperature 0, N_try=3, N_step=20, 2-shot "
                          "ICL for recruitment/evaluation, BM25 top-3) but no prompts; code only promised by URL (not "
                          "inspected)."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Memories are built on ~350 non-test CAPBench instructions and read on the 150 disjoint test "
                                   "instructions; the w/o Self-Evolution row is the retained-store contrast (SR 0.55 vs 0.50, "
                                   "one run). Weak: the store also updates during the test stream, test items are "
                                   "template-siblings of the build items, and the gain is ~7-8 of 150 tasks.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: on author-built CAPBench (GPT-4v/4o, Android emulator) the app-oriented "
                                         "multi-agent system beats single- and multi-agent baselines run under different step "
                                         "budgets and base models; retained memories add a small single-run gain (+0.05 SR) "
                                         "under an online-updating protocol. Not reproduced.",
            "unresolved": ["Who/what adjudicates Success Rate is never stated.",
                           "Table 2 (GPT-4v TR 0.76) vs Table 3 full-model row (TR 0.81) inconsistency (opus:O04).",
                           "Per-memory attribution (M_E vs M_G), frozen-store evaluation, variance, build-phase cost."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The cross-app limitation is real (baselines ≤0.21 SR on CAPBench) and "
                   "MobileAgent-v2 is run, but this domain's G asks what fixed non-weight object becomes adaptive and how it "
                   "differs from same-class memory neighbours: the self-evolution gap is an analogy (opus:O01), and the "
                   "app-specific experience memories of MobileGPT/AutoDroid are dismissed in one sentence without comparison "
                   "(opus:O02). Real limitation with incomplete neighbour comparison = anchor 2; sol's 3 credits the "
                   "multi-agent gap but not the memory residual.",
                   ["son55:E012", "sol:E009", "opus:O01", "opus:O02"], ["sol:E014"]),
            "M": R("resolved", 3, "Opus sides with sol. Each named bottleneck (task relations, app diversity, error propagation) "
                   "maps to a module whose removal is tested, and the decomposition makes a distinguishing prediction "
                   "(smaller degradation as app count grows) that is checked (opus:O03). Below 4 because the retention "
                   "mechanism's key assumption (self-judged success is a reliable write gate) is unexamined and the M_E update "
                   "rule is unspecified; son55's points on the update rule are charged under X (2), not twice.",
                   ["sol:E001", "sol:E002", "sol:E008", "opus:O03", "son55:E004"], ["son55:E005"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1 gives the write/read chain (Extract→Update, BM25 top-3 "
                   "read, M_E in Schedule), but M_G is append-only (opus:O05), M_E admission is one LLM decision, no "
                   "versioning/rollback/retirement, prompts absent.",
                   ["sol:E001", "sol:E015", "son55:E005", "son55:E003", "opus:O05"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55. Success Rate is defined only as 'whether the instruction is "
                               "completed' with no stated adjudicator (human, rule or LLM); App Rate is satisfiable by opening "
                               "the labelled apps; CAPBench is GPT-4-generated from authors' templates; the full-model ablation "
                               "row contradicts Table 2 (opus:O04). The headline metric's validator is unverifiable, which is "
                               "below the anchor-2 'relevant results with gaps'.",
                               ["son55:E007", "sol:E013", "opus:O04", "son55:E006", "sol:E004"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Evolution-off and module ablations exist (Table 3), but "
                             "M_E and M_G are removed jointly, one run, baselines get 80 steps vs 20×3 per sub-task and different "
                             "base models, and no alternative memory scheme is compared.",
                             ["sol:E004", "sol:E005", "son55:E004", "son55:E008"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked and kept. Build/test instructions are disjoint, but memories "
                           "keep updating on the test stream (index_experience F3 / H00 step 4 failure mode), build and test "
                           "items are instantiated from one template pool with no overlap audit, and the 50-task online-user "
                           "check measures the system, not the frozen store.",
                           ["sol:E003", "son55:E002", "son55:E006", "sol:E011"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes (150 test, 50 SAP, 100 MobileAgentBench, 50 "
                              "online) and degradations are reported, but one run, no intervals; the +0.05 SR memory effect is "
                              "~7-8 tasks.",
                              ["sol:E007", "son55:E004", "son55:E010"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Actions/task and tokens/action vs MobileAgent-v2 are reported "
                        "(Table 6); the ~350-instruction build phase, Extract/Update/Evaluate calls and the unequal step budget "
                        "are not costed.",
                        ["sol:E006", "son55:E011", "son55:E008"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text (no appendix exists); in scope (A): retained non-weight memories written from executions "
                  "and read later; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "EVIDENCE.md 'retained' = a retained change improves later tasks, preferably on independent held-out tasks. The "
                "store is built on non-test instructions and the evolution-off contrast is measured on the disjoint 150-task "
                "split (0.55 vs 0.50). Online test-time updates and template siblings weaken holdout (E.holdout=1) but do not "
                "turn this into a selection-set-only result; the test set never selects what is kept.",
                ["sol:E003", "son55:E002", "sol:E004"], "none (labels are not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "The central contribution (object-oriented split, DAG scheduling, app-specialist delegation, three of four "
                "contributions) is a decomposition move; memory conditioning is one module. sol's reason for rejecting C25 "
                "(no sound solver) is correct and retained at sub level, not at parent level.",
                ["son55:E004", "son55:E008", "opus:O03"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["decompose_and_delegate", None], ["adapt_via_conditioning", None]],
                "Both parents apply with sub null; sol's conditioning match is kept as the supporting entry.",
                ["son55:E003", "sol:E008"], "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"]],
                "H01 is defined by an editing policy over existing entries (update/merge/delete/forget). MobileSteward has only a "
                "write/no-write decision for M_E and append-only M_G (opus:O05); son55's own check found no consolidation. H00 "
                "(extract lessons from own outcomes and append) fits better, at medium-low fit (successes only, no contrast).",
                ["sol:E001", "sol:E015", "opus:O05"], "none"),
            res("expectations[local:2502.16796-1].status", *C(p, "expectations[local:2502.16796-1].status"), "revised",
                "local-1 = sol's cost question → partial; son55's local-1 (Success-Rate evaluator unspecified) kept as "
                "local:2502.16796-3 = unmet",
                "Same ID, different questions (A4 collision). Both answers verified: Table 6 costs actions/tokens but not build/"
                "maintenance (partial); the SR adjudicator is never named (unmet).",
                ["sol:E006", "son55:E007"], "none; consistent with E.cost=2 and E.measurement=1"),
            res("expectations[rs:decompose_and_delegate/RE-1].status", *C(p, "expectations[rs:decompose_and_delegate/RE-1].status"),
                "son55", "partial", "Verified Table 6 (A/T, T/A vs MobileAgent-v2); build-phase and Steward calls uncosted.",
                ["son55:E011"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-2].status", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"),
                "son55", "partial", "Verified Table 3: three modules ablated once; memories not separated; extra tries/steps "
                "not controlled.", ["son55:E004", "son55:E008"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-3].status", *C(p, "expectations[rs:decompose_and_delegate/RE-3].status"),
                "revised", "partial",
                "'unknown' is not appropriate after a complete read: implementation details are given (§4.2.3) but prompts are "
                "not; code only promised. Partial disclosure.", ["sol:E005", "son55:E003"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-4].status", *C(p, "expectations[rs:decompose_and_delegate/RE-4].status"),
                "son55", "partial", "Verified: author-built CAPBench plus SAPBench (50), MobileAgentBench (100, baselines copied "
                "from another paper) and 50 online tasks.", ["son55:E006", "son55:E010"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-5].status", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"),
                "son55", "partial", "Verified: single-agent baselines run, but with different base models (GPT-4/4v/4o) and an "
                "80-step cap vs 20 steps × 3 tries per sub-task.", ["son55:E008"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-6].status", *C(p, "expectations[rs:decompose_and_delegate/RE-6].status"),
                "son55", "partial", "Verified: bottlenecks named and the complexity analysis links app count to failure "
                "(opus:O03), but no per-bottleneck diagnostic.", ["son55:E004", "opus:O03"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00.step5].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/H00.step5].status"), "son55", "partial",
                "Applies because H00 is the final sub-card. Store-off ablation present; no budget matching, no variance.",
                ["son55:E004", "son55:E008"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S3].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "sol", "partial",
                "Verified: grounding signal is the Steward's own success verdict; imperfection unacknowledged and unmeasured.",
                ["sol:E001", "sol:E015"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S4].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "sol", "unmet",
                "Verified: no consolidation, forgetting or rollback (opus:O05).", ["sol:E015", "opus:O05"], "none"),
            res("expectations[rsi:index_experience_for_reuse/F4].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"), "son55", "unmet",
                "Verified: failure mode present — entries admitted on the model's own success verdict.",
                ["son55:E001", "son55:E005"], "none"),
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.G: memory-neighbour residual unargued; retained-memory gap is analogy.",
                ["opus:O01", "opus:O02", "son55:E012"], "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.M: module-to-bottleneck mapping with a tested distinguishing prediction; update-rule gaps charged "
                "to X.", ["opus:O03", "sol:E001", "sol:E008"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.measurement: headline metric's adjudicator unstated plus Table 2/3 inconsistency.",
                ["son55:E007", "opus:O04"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2502.16796-2]",
             "sol_value": "unmet — statistics: no repeated-run/order uncertainty",
             "son55_value": "unmet — holdout: template-sibling overlap not audited",
             "correction": "Same ID used by both seats for different questions (A4 violation hidden by equal status). sol's kept "
                           "as local:2502.16796-2; son55's renumbered local:2502.16796-4.",
             "evidence_ids": ["sol:E007", "son55:E006"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): two retained text memories (M_E expertise, M_G task guidelines) "
                                                   "written after self-judged success and read later. Strong system gains vs "
                                                   "budget-unmatched baselines; memory share +0.05 SR, one run; memories update "
                                                   "during test; SR adjudicator unstated; Table 2/3 TR mismatch.",
            "integrity_checks": "Both seats a1 on 2502.16796v1, material sha f2cf4520…, input_hash a98a9774…, rubric b44708af…; "
                                "canonical seat hashes equal conflicts.json; all seat quotes verbatim; RS/domain ids/parents valid.",
            "core_claim_check": "Re-read §3.7, §4.2.3, Tables 2–7 and §4.5; recomputed Table 5/Fig.5 percentages (33%, 46%, 1.77×, "
                                "2.43×) — consistent.",
            "rating_agreement": "5/8 items identical and re-checked unchanged; G and E.measurement → son55, M → sol.",
            "expectation_renumbering": "son55 local-1 → local-3, local-2 → local-4 (same ID, different questions).",
        },
    }

    # =========================================================== 2503.00735 LADDER
    p = "2503.00735"
    oos_reason = ("out_of_scope (rubric A3): the improver's update target and the evaluated product are both solver weights "
                  "(GRPO on the base LLM; TTRL fine-tunes per question then rolls back). Variant trees are training data; the "
                  "transformation library is a one-off static aid, not an execution-feedback-updated retained harness object. "
                  "Not scored; null is not a zero-quality rating.")
    unk = lambda: R("unknown", None, oos_reason, ["opus:O01", "opus:O02"], [],
                    ["complete pinned v3 text: §1–§5, Algorithms 1–2, figures, failed-question appendix"])
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "and finally the model is rolled back to its original parameters for the next test question.",
                    "§3.1.5 TTRL", "TTRL's adaptation is per-question weight training that is discarded; nothing non-weight is retained."),
            opus_ev(p, "O02", "This transformation library served as a foundation for guiding variant generation.",
                    "§3.1.2 Variant Generation",
                    "The only non-weight artifact is generated once by the base model and never updated from execution feedback."),
            opus_ev(p, "O03", "Second, we perform the reinforcement learning protocol described in section",
                    "§3.1.5", "Both LADDER and TTRL deliver their improvement through GRPO on model weights."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): model-generated, verifier-filtered variant problems manufacture the training "
                      "distribution for RL on weights — C08 (generate → gate → retrain). sol's C26 (comparative/preference "
                      "signal) fits less: the reward is an absolute numeric-verification bit; what is manufactured is the data.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": "yes (informational)", "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [{"main": "self_generate_the_curriculum", "sub": "H23", "version": VER, "fit": "low (boundary, informational)",
                         "condition_checks": "S1 partial (numeric verifier, admittedly imperfect); S3 unmet for LADDER (static "
                                             "one-shot variant set), partial for TTRL; F2 partial (generic easier-variant "
                                             "schedule). Both seats agree; resemblance does not override A3.",
                         "evidence_ids": ["opus:O02", "opus:O03"]}],
            "unassigned": [],
            "revision_proposals": [],
        },
        "pattern_mapping": [
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": "C08", "domain_namespace": "rsi",
             "domain_main": "self_generate_the_curriculum", "domain_sub": "H23",
             "operation_correspondence": "Generate-and-verify synthetic variants = self-generated curriculum consumed by weight RL.",
             "necessary_conditions_and_differences": "Informational only: H23's retained object would be a curriculum generator "
                                                     "or task set inside a harness loop; here the retained object is weights.",
             "evidence_ids": ["opus:O02", "opus:O03"]},
        ],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": None,
            "evidence_level_note": "Harness evidence labels are not assigned to out-of-scope weight-level self-improvement.",
            "claim_support": None,
            "claim_support_note": "Not assessed under this rubric; the integration results are recorded as author-reported only.",
            "strongest_supported_claim": None,
            "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong."]},
        "ratings": {k: unk() for k in ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")},
        "status": "out_of_scope",
        "reason": oos_reason,
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", None,
                "Out-of-scope records carry no harness evidence label (cal-dev precedent); 'not_assessed' and null mean the same "
                "here, null is the canonical form.", ["opus:O01"], "none"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Neither 'scoped' (sol) nor 'unresolved' (son55) was the result of checking the central claim under this rubric; "
                "claim_support is left null with a note.", ["opus:O03"], "none"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["self_supervised_signal_engineering", "C08"]],
                "C08 (controllable generator → single gate → retrain) matches the variant-generation + verifier + GRPO shape; "
                "C26 needs a comparative/preference unit of supervision, which this binary verifier reward is not.",
                ["opus:O02", "opus:O03"], "none"),
            res("expectations[local:2503.00735-1].status", *C(p, "expectations[local:2503.00735-1].status"), "sol", "unmet",
                "Verified (informational): the measured product is a fine-tuned model; TTRL resets per question (opus:O01).",
                ["opus:O01"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-2].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-2].status"), "son55", "not_applicable",
                "Not scored for an out-of-scope record.", [], "none"),
            res("expectations[rsi:self_generate_the_curriculum/S6].status",
                *C(p, "expectations[rsi:self_generate_the_curriculum/S6].status"), "son55", "not_applicable",
                "Not scored for an out-of-scope record.", [], "none"),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–§5 and appendix: GRPO on variant trees (LADDER) and per-question GRPO "
                                                   "with rollback (TTRL); no retained non-weight component updated by feedback "
                                                   "→ out_of_scope per A3.",
            "integrity_checks": "Both seats a1 on 2503.00735v3, material sha f03a6eeb…; both out_of_scope independently; hashes "
                                "equal conflicts.json.",
            "core_claim_check": "Independently confirmed the A3 basis (opus:O01–O03); noted TTRL counts a question solved if any "
                                "point during adaptation is verifier-correct (informational, not scored).",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2503.08026 RMM
    p = "2503.08026"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "The reranker is an MLP with a residual connection.", "Appendix A.1",
                    "Conflicts with §6.1 ('linear layer with residual connections'); reranker architecture not uniquely specified."),
            opus_ev(p, "O02", "accuracy improvement over the baseline without memory management on the", "Abstract",
                    "Abstract '>10%' holds only vs Long Context with GTE (57.4→70.4); vs RAG-GTE it is +6.8 and with the "
                    "default Contriever +2.4 over RAG."),
            opus_ev(p, "O03", "This allows for online refinement of the retriever as the conversation progresses",
                    "§1 Introduction",
                    "RR is designed to update online during conversation; when and on which queries it updates in the main "
                    "evaluation, and whether it is reset per user/instance, is never stated."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["generative_process_redesign"], "outside_taxonomy": False,
            "reason": "Retrospective Reflection manufactures a label-free per-memory reward from the generator's own citations "
                      "and trains a reranker on it (C26, partial: scalar ±1 REINFORCE rather than pairwise). Prospective "
                      "Reflection frees the conventionally fixed conditioning granularity (turn/session) — the "
                      "generative_process_redesign definition names 'conditioning granularity' explicitly. sol's "
                      "adapt_via_conditioning is true of any RAG memory and does not capture either specific operation.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering"),
                        smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": "partial", "resolves_problem": "partial (small-to-moderate gains, no variance)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [{"main": "index_experience_for_reuse", "sub": "H04", "version": VER, "fit": "medium-high",
                         "condition_checks": "S3 met (topic-summary key / raw-dialogue content); S5 met (No-History, flat RAG "
                                             "and +PR rows on the same raw dialogue); S6 partial (local add/merge vs top-K "
                                             "neighbours, cost unmeasured); F4 present (LLM-written/merged summaries admitted "
                                             "without an external gate); F3 unknown for the RR reranker (update timing vs "
                                             "evaluation unstated).",
                         "evidence_ids": ["sol:E001", "sol:E002", "son55:E005", "son55:E003", "opus:O03"]}],
            "unassigned": ["Retrospective Reflection: online RL of a retrieval reranker (weights) from consumer-citation credit; "
                           "no domain sub-card fits exactly (son55)."],
            "revision_proposals": [
                "son55: a sub-condition for 'consumer-credited retrieval selector' distinct from H26 (single_source; needs a "
                "second full-text member).",
                "Scope note for A3: small trained auxiliary modules inside a harness (rerankers/adapters) are weights; a paper "
                "stays in scope only through a separately evaluated non-weight retained object (here the PR memory bank)."],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2503.08026-2"): "local:2503.08026-4"},
            overrides={"rsi:index_experience_for_reuse/S5": {
                "status": "met",
                "reason": "Opus: son55's value. S5 asks that the store be certified by removing it: No-History (0.0 Acc), flat "
                          "RAG over the same raw dialogue and +PR are all reported on two benchmarks; frozen/budget-matched "
                          "concerns (sol) are charged to E.causality/E.holdout, not to whether the removal ablation exists."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "The PR memory bank is written from earlier sessions only and read for later responses; the "
                                   "+PR row (no RR) isolates that retained non-weight artifact vs flat RAG on the same history "
                                   "(Contriever: Recall@5 54.3→57.4, Acc 58.8→59.6, 3-run means). The RR part is weight "
                                   "learning with an unstated update/evaluation boundary and does not raise the label.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, Gemini-1.5-Flash: topic-organized memory plus a citation-rewarded "
                                         "reranker improves recall and response metrics over flat RAG on MSC and LongMemEval "
                                         "(GTE: Acc 63.6→70.4; Contriever: 58.8→61.2); the abstract's '>10%' holds only against "
                                         "Long Context with GTE (opus:O02).",
            "unresolved": ["RR update timing relative to evaluation and reset per user/instance (opus:O03).",
                           "Variance (3-run means only); evaluated denominators not stated.",
                           "No cost numbers; RMM retrieves K=20 then reranks vs RAG K=5.",
                           "Reranker architecture: linear (§6.1) vs MLP (A.1) (opus:O01); several table/figure cross-references "
                           "mislabelled (Table 3 cited as 4, Figure 4 as 5, Table 5 as 7) — presentation only."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Two concrete bottlenecks (fixed granularity, fixed retriever) with "
                   "MemoryBank/LD-Agent re-implemented as baselines and own analyses that probe both (granularity oracle, "
                   "direct retriever RL collapse); newer memory managers only cited.",
                   ["son55:E001", "son55:E002", "son55:E009", "son55:E013"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Topic memory and citation-reward reranking are each argued and give "
                   "distinguishing predictions (reranker needed vs direct retriever RL; PR vs fixed granularity); citation "
                   "≠ usefulness is the weak assumption.",
                   ["son55:E003", "son55:E004", "son55:E008", "sol:E001"], ["son55:E014"]),
            "X": R("resolved", 3, "Opus sides with sol. The in-scope retained object (PR memory bank) is fully reconstructable: "
                   "extraction and merge prompts (App. D), top-K neighbour retrieval, explicit add/merge decision that handles "
                   "updated facts; REINFORCE hyper-parameters given. Not 4: no external gate, deletion or rollback, reranker "
                   "architecture inconsistent (opus:O01), RR update schedule unstated (opus:O03). son55's schedule point "
                   "concerns the weight module and is charged under E.holdout.",
                   ["sol:E001", "sol:E002", "son55:E015", "sol:E004"], ["opus:O01", "opus:O03"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. LongMemEval Recall@5 against annotated evidence and judge "
                               "accuracy; MSC METEOR/BERT plus LLM-judge with human agreement κ 0.69–0.71 (inter-human 0.82) on "
                               "100 items; citation validity checked only against another Gemini model.",
                               ["sol:E007", "sol:E015", "son55:E008", "son55:E007"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. +PR/+RR/direct-retriever-RL/full ablations on two datasets "
                             "are useful, but the obvious alternatives for each load-bearing claim are untested: no random- or "
                             "no-reward reranker (is the gain the citation reward or the extra K=20 candidate pool?), no "
                             "budget-matched memory manager for PR's extra extraction/merge calls. Gains with the default "
                             "retriever are small (Acc +0.8 PR, +1.4 RR). Variance is charged to E.statistics, not here.",
                             ["son55:E005", "son55:E006", "sol:E009"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. PR memory is built only from history sessions, but the "
                           "headline numbers include RR, whose update/evaluation boundary and reset policy are unstated "
                           "(opus:O03); single model family; offline-pretraining split exists only for §8.6.",
                           ["son55:E010", "son55:E011", "opus:O03"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): 3-run means, negative ablation (direct retriever RL) and "
                              "a 100-item human study, but no std/CI; margins of 0.8–2.4 points untested.",
                              ["sol:E006", "son55:E007", "son55:E005"]),
            "E.cost": R("not_reported", 0, "Opus sides with son55. No calls, tokens, latency or RL-step cost anywhere; the "
                        "single-call design remark (sol:E012) and the 16×A100 hardware line are not cost evidence, and the "
                        "Limitations only concede RL 'can be computationally expensive'. Consistent with r01b precedent "
                        "(qualitative remark ≠ cost report).",
                        ["son55:E012", "sol:E010", "sol:E012"], [],
                        ["Full pinned v2 text: §1–§9, Limitations, Appendices A–D; searched cost/token/latency/time/call/GPU."]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–D. In scope via the retained non-weight topic memory bank (separately "
                  "ablated); the RR reranker is a weight-updated auxiliary module, recorded but not the basis of scope.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "retained",
                "The +PR-only row is a retained-artifact contrast on later responses with the store built from earlier sessions "
                "only. sol's split/reset ambiguity is real but concerns RR (weights), which does not carry the label.",
                ["son55:E005", "sol:E008"], "none (labels are not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "Citation-derived label-free reward for the reranker is the paper's most specific operation; "
                "adapt_via_conditioning is generic to all RAG memories.", ["son55:E002", "son55:E004"], "none"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["generative_process_redesign", None], ["self_supervised_signal_engineering", "C26"]],
                "C26 partial (non-human in-distribution signal, per-memory granularity, scalar not pairwise); "
                "generative_process_redesign supporting because its definition names conditioning granularity, which PR frees.",
                ["son55:E001", "son55:E004", "son55:E009"], "none"),
            res("expectations[local:2503.08026-3].status", *C(p, "expectations[local:2503.08026-3].status"), "sol", "unmet",
                "Verified: no end-to-end cost; consistent with E.cost=not_reported.", ["sol:E009", "sol:E010"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-1].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-1].status"), "son55", "partial",
                "Verified: two benchmarks, three retrievers, two Gemini sizes; one model family.", ["son55:E007"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-2].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-2].status"), "son55", "partial",
                "Verified: ablations exist; no no-reward/random-reward reranker or compute-matched control.",
                ["son55:E005", "son55:E006"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-3].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-3].status"), "son55", "met",
                "Verified: downstream QA accuracy and response metrics are reported, not only citation statistics.",
                ["son55:E005", "son55:E007"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-5].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-5].status"), "son55", "unmet",
                "Verified: cost named as a limitation, never measured.", ["son55:E012"], "none"),
            res("expectations[rs:self_supervised_signal_engineering/RE-6].status",
                *C(p, "expectations[rs:self_supervised_signal_engineering/RE-6].status"), "son55", "partial",
                "Verified: label-free reward is deployment-realistic; update-on-evaluation and reset unstated (opus:O03).",
                ["son55:E010", "son55:E011", "opus:O03"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/F4].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/F4].status"), "son55", "met",
                "Cross-card check kept: the authors frame RR as retrieval refinement, so the 'retrieval fix presented as "
                "learning' failure is avoided ('met' = expectation satisfied).", ["son55:E002"], "none"),
            res("expectations[rsi:index_experience_for_reuse/F3].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/F3].status"), "son55", "unknown",
                "PR store is built from history only; for RR the update timing vs evaluation is genuinely unstated, so unknown "
                "is the honest status (not 'unmet').", ["son55:E010", "son55:E011", "opus:O03"], "none"),
            res("expectations[rsi:index_experience_for_reuse/F4].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"), "son55", "unmet",
                "Verified: extracted/merged summaries enter the bank on LLM judgment alone (failure mode present).",
                ["son55:E003"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S3].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/S3].status"), "sol", "met",
                "Verified: entries are (topic summary as key, raw dialogue as content); son55 records the same in its domain "
                "condition check (same_supported_fact in substance).", ["sol:E001"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S5].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "son55", "met",
                "S5 asks whether the store is certified by removing it; No-History/flat-RAG/+PR rows do this on two "
                "benchmarks. Budget and frozen-state concerns belong to E.causality/E.holdout.",
                ["son55:E005"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S6].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/S6].status"), "sol", "partial",
                "Verified: local add/merge against top-K neighbours at session end; cost growth unmeasured (son55's domain "
                "check also partial).", ["sol:E002", "sol:E010"], "none"),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.X: the in-scope retention chain is reconstructable with prompts; RR schedule gap charged to E.holdout.",
                ["sol:E002", "son55:E015", "opus:O01"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.causality: no random-reward reranker or budget-matched memory manager; small default-retriever "
                "gains.", ["son55:E005", "son55:E006", "sol:E009"], "−3.75 vs son55 (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55",
                {"status": "not_reported", "rating": 0},
                "See ratings.E.cost: qualitative design remark and hardware line are not a cost report.",
                ["son55:E012", "sol:E012"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2503.08026-2]",
             "sol_value": "unmet — statistics: three-run means without variance",
             "son55_value": "unmet — holdout: no frozen-reranker evaluation",
             "correction": "Same ID for different questions (A4 collision hidden by equal status); son55's renumbered "
                           "local:2503.08026-4. (local-1 is the same question in both seats and is merged.)",
             "evidence_ids": ["sol:E006", "son55:E010"], "score_impact": "none"},
            {"field_path": "assessment.strongest_supported_claim / paper.central_claim",
             "sol_value": "no comment on the abstract's '>10% accuracy improvement'",
             "son55_value": "no comment on the abstract's '>10% accuracy improvement'",
             "correction": "The abstract's '>10%' is true only against Long Context with GTE (+13.0); against RAG with the same "
                           "retriever it is +6.8 and with the default Contriever +2.4. Allowed conclusion states the narrower "
                           "margins.",
             "evidence_ids": ["opus:O02"], "score_impact": "none (claim scope only)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope via PR memory bank (non-weight, add/merge, prompts given); RR is "
                                                   "REINFORCE on a small reranker (weights) with unstated online/eval "
                                                   "boundary. Ablations on two datasets; 3-run means without variance; no cost; "
                                                   "abstract >10% claim narrow.",
            "integrity_checks": "Both seats a1 on 2503.08026v2, material sha 6f8f921d…, hashes equal conflicts.json; quotes verbatim.",
            "core_claim_check": "Re-read §5–§8, Tables 1–7, Appendix A/B; checked Table 3 F1 arithmetic (86.7) and the abstract/"
                                "intro margins against Table 1.",
            "rating_agreement": "5/8 identical and re-checked; X and E.causality → sol, E.cost → son55.",
            "expectation_renumbering": "son55 local-2 → local-4.",
        },
    }

    # =========================================================== 2503.10071 ATLASS
    p = "2503.10071"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Apply other models like ChatGPT 3.5 or open-source LLM for less demanding tasks like Task "
                    "Analyzer and Tool Selector and compare results.", "§VI Limitations and Future Work",
                    "Contradicts §IV-C's 'overall cost is minimized by utilizing ... GPT-3.5' (son55:E011): the GPT-3.5 saving "
                    "is future work, all measured runs used gpt-4-0613."),
            opus_ev(p, "O02", "result in basic, task-specific tools that overlook the reuse of similar task requirements.",
                    "§I Introduction",
                    "The reuse gap vs LATM is the authors' characterisation; LATM's original is not in the fixed package, so "
                    "the premise is unverified rather than refuted."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: decompose_and_delegate/C25 — the LLM emits executable Python, the interpreter's errors are fed "
                      "back during construction, and working code becomes a reusable library. Fit partial: 'runs without "
                      "error' is not a sound verifier and the loop is not ablated.",
            "matches": [smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": "partial", "resolves_problem": "not shown (no task-success measurement)",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [{"main": "crystallize_executable_capability", "sub": "H07", "version": VER, "fit": "medium",
                         "condition_checks": "S1 partial (execution-without-error + human code review; no replayed task "
                                             "success); S3 unmet (no unseen-input validation of a tool); S4 met (tracebacks "
                                             "drive repair); S5 partial (DB on/off compared on tokens only); S6 met (SerpAPI "
                                             "documentation grounds API tools); F1 present (forging buried in a multi-agent "
                                             "pipeline, no isolated test).",
                         "evidence_ids": ["sol:E002", "sol:E003", "son55:E006", "son55:E008", "sol:E004"]}],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2503.10071-1"): "local:2503.10071-4",
                    ("son55", "local:2503.10071-2"): "local:2503.10071-5"},
            overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Even task-level success is not measured; the only retained-artifact effect is lower token "
                                   "cost when a tool is already stored, apparently on the same 8 prompts.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, gpt-4-0613, 8 illustrative prompts: a generate-repair-register tool "
                                         "pipeline can produce and reuse tools, and re-running a prompt whose tool is stored "
                                         "costs ~34% fewer tokens (2895→1920). 'Better than similar research' is unsupported; "
                                         "the authors list quantitative comparison as future work.",
            "unresolved": ["Tool correctness/task success, selector accuracy, held-out reuse, executed LATM comparison.",
                           "API-key handling: key 'combined to create a new prompt' (§III-B.4) vs inserted by regex 'instead of "
                           "passing it to the model' (§VII).",
                           "GPT-3.5 cost claim (§IV-C) vs future-work list (opus:O01)."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The dependency/API-documentation problem for generated tools is concrete "
                   "and named against LATM; the reuse premise about LATM is an unverified author characterisation (opus:O02) "
                   "and the literature review is mostly off-topic, so neighbour comparison is incomplete — that is the "
                   "anchor-2 description. son55's 1 would require the problem itself to be vague or its premise refuted; "
                   "neither holds on the fixed material.",
                   ["sol:E010", "sol:E012", "opus:O02", "son55:E007"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Requirement analysis, equivalence-based selection, interpreter repair "
                   "loop and doc-grounded API tools respond to the gap; 'runs without error' as acceptance and LLM equivalence "
                   "are unjustified assumptions.",
                   ["sol:E001", "sol:E002", "sol:E003", "son55:E003"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. DB format and write/read chain explicit; unbounded repair loop, no "
                   "correctness gate, versioning or retirement, no prompts, contradictory API-key handling.",
                   ["sol:E002", "sol:E007", "sol:E008", "sol:E009", "son55:E002"]),
            "E.measurement": R("not_reported", 0, "Opus sides with son55. No task-success metric, verifier or accuracy figure "
                               "exists: Table II checkmarks have no success criterion, the 'Tool Selection Accuracy' section "
                               "reports no number, Table I is one qualitative example. Illustrations are not measurements; "
                               "token counts belong to E.cost.",
                               ["son55:E005", "son55:E007", "sol:E013", "sol:E006"], [],
                               ["Full pinned v1 text §§I–VII, Tables I–III, all examples; no appendix exists."]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Only a DB-present vs DB-absent token comparison; no "
                             "outcome ablation and no executed LATM run.",
                             ["sol:E005", "son55:E008"], ["son55:E010"]),
            "E.holdout": R("not_reported", 0, "Both seats not_reported; re-checked. No held-out tasks or tool split; reuse shown on "
                           "one qualitative example; cost on prompts that appear to be the generating ones.",
                           ["son55:E006", "son55:E008"], [],
                           ["Full pinned v1 text §§I–VII, Tables I–III; searched held-out/test/split/unseen."]),
            "E.statistics": R("not_reported", 0, "Opus sides with son55 (A2 ladder 0). Eight hand-picked prompts, one run, and no "
                              "failure of ATLASS itself is reported anywhere (LATM's ✗ marks are baseline capability claims, "
                              "not the method's failure denominator); no variance or intervals.",
                              ["son55:E008", "sol:E013"], [],
                              ["Tables II–III, §IV-C text, Limitations; searched run/repeat/variance/fail."]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked arithmetic (23163/8=2895, 15364/8=1920; $0.807/8≈0.1008, "
                        "$0.4992/8=0.0624). Per-prompt tokens/USD with and without stored tools; no baseline cost, retries, "
                        "SerpAPI or human-review cost; GPT-3.5 saving asserted but contradicted (opus:O01).",
                        ["sol:E005", "son55:E008", "son55:E004"], ["son55:E011", "opus:O01"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text (no appendix exists); in scope (A): generated tools persist in a tool database and are "
                  "re-read by the Tool Selector. Evidence is illustrative; low scores reflect missing measurement, not missing material.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("expectations[local:2503.10071-1].status", *C(p, "expectations[local:2503.10071-1].status"), "revised",
                "local-1 = sol's cost-completeness question → partial; son55's local-1 (no correctness check beyond 'workable "
                "code') kept as local:2503.10071-4 = unmet",
                "Same ID, different questions (A4 collision); both answers verified.", ["sol:E005", "son55:E003"], "none"),
            res("expectations[local:2503.10071-3].status", *C(p, "expectations[local:2503.10071-3].status"), "sol", "unmet",
                "Verified: capability table lacks correctness adjudication; quantitative evaluation is future work.",
                ["sol:E006", "sol:E013"], "none; consistent with E.measurement=not_reported"),
            res("expectations[rs:decompose_and_delegate/RE-1].status", *C(p, "expectations[rs:decompose_and_delegate/RE-1].status"),
                "son55", "partial", "Verified Table III; no call counts, retries, human-review or baseline cost.",
                ["son55:E008", "son55:E004"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-2].status", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"),
                "son55", "unmet", "Verified: no ablation of any agent or of the DB on task quality.", ["son55:E010"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-3].status", *C(p, "expectations[rs:decompose_and_delegate/RE-3].status"),
                "son55", "unmet", "Verified: no prompts or code in the text and no code link.", ["son55:E002"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-4].status", *C(p, "expectations[rs:decompose_and_delegate/RE-4].status"),
                "son55", "partial", "Eight prompts across six domains show breadth of demos, but no benchmark or held-out "
                "tasks; partial is the most that can be given.", ["son55:E007"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-5].status", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"),
                "son55", "unmet", "Verified: LATM compared by checkmarks only; no unified single-agent baseline.",
                ["son55:E007", "son55:E010"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-6].status", *C(p, "expectations[rs:decompose_and_delegate/RE-6].status"),
                "son55", "unmet", "Verified: no diagnostic linking a sub-task to outcomes.", ["son55:E009"], "none"),
            res("expectations[rsi:crystallize_executable_capability/F1].status",
                *C(p, "expectations[rsi:crystallize_executable_capability/F1].status"), "son55", "unmet",
                "Verified: failure mode present — no isolated test of the forged-tool artifact.", ["son55:E010"], "none"),
            res("expectations[rsi:crystallize_executable_capability/S1].status",
                *C(p, "expectations[rsi:crystallize_executable_capability/S1].status"), "sol", "partial",
                "Verified: admission after error-free execution, not validated task correctness (son55's domain check also "
                "partial).", ["sol:E002", "sol:E003"], "none"),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G: concrete dependency/API gap with incomplete, unverified neighbour comparison = anchor 2.",
                ["sol:E010", "opus:O02"], "+3.75 vs son55 (15×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.measurement: no metric or verifier exists; illustrations are not measurements.",
                ["son55:E005", "sol:E013"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "not_reported", "rating": 0},
                "See ratings.E.statistics: no own-failure denominator, one run, eight prompts.",
                ["son55:E008"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2503.10071-2]",
             "sol_value": "unmet — X: contradictory API-key handling",
             "son55_value": "unmet — E.measurement: 'Tool Selection Accuracy' has no number",
             "correction": "Same ID for different questions (A4 collision hidden by equal status); son55's renumbered "
                           "local:2503.10071-5.",
             "evidence_ids": ["sol:E008", "son55:E005"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): tool DB of generated Python tools reused by a selector. No "
                                                   "quantitative task evaluation (authors defer it), checkmark capability table, "
                                                   "cost table on 8 prompts; internal contradictions on API key and GPT-3.5.",
            "integrity_checks": "Both seats a1 on 2503.10071v1, material sha 2a98bf0f…, hashes equal conflicts.json; quotes verbatim.",
            "core_claim_check": "Re-read §III–§VII and Tables I–III; recomputed Table III averages (match).",
            "rating_agreement": "5/8 identical and re-checked; G → sol; E.measurement and E.statistics → son55.",
            "expectation_renumbering": "son55 local-1 → local-4, local-2 → local-5.",
        },
    }

    # =========================================================== 2503.13856 MDTeamGPT
    p = "2503.13856"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "yields 2.1% and 5.4% higher accuracy on MedQA and PubMedQA, respectively, compared to using only",
                    "§4.3 Ablation", "KB variants make distinguishing predictions that are tested: CorrectKB-only > ChainKB-only, "
                    "both > either (Table 2 rows 5–7; arithmetic verified)."),
            opus_ev(p, "O02", "likely because Medprompt is evaluated solely on four-option scenarios",
                    "§4.2 Main Results",
                    "Implies the Medprompt row was not re-run under the authors' 4/5-option protocol, at odds with the Table 1 "
                    "caption 'all results were obtained using gpt-4-turbo'; strongest baseline comparability unresolved."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Both seats: primary adapt_via_conditioning — retrieved success summaries and error reflections condition "
                      "frozen specialist agents. C03 accepted at partial fit (retrieving reference instances as a first-class "
                      "input, plus a distribution-level cross-dataset test), consistent with r01b's low-fit C03 for "
                      "retrieval-to-bank conditioning. decompose_and_delegate (sub null) supporting for triage/specialist roles "
                      "and lead-physician aggregation, which are a separate operation from KB conditioning.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"), smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": "yes (conditioning toggled on/off)", "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [
                {"main": "abstract_experience_into_guidance", "sub": "H00", "version": VER, "fit": "medium",
                 "condition_checks": "S2 partial (separate success and failure stores, both retrieved; no paired contrast); S3 "
                                     "partial (gold correctness in §3.3 but Appendix A.4 describes a similarity-based "
                                     "correctness step — gate ambiguous); S4 unmet (append-only, no consolidation/forgetting); "
                                     "H00 step 4 met (train-only stores, test not written); step 5 partial (store-off "
                                     "ablation, no budget match).",
                 "evidence_ids": ["sol:E002", "sol:E003", "sol:E013", "son55:E004", "son55:E005"]},
                {"main": "index_experience_for_reuse", "sub": "H03", "version": VER, "fit": "medium",
                 "condition_checks": "S1 unmet (whole-question records); S2 partial (gold routes cases; CorrectKB admission "
                                     "gated, ChainKB admits every failed case's LLM-written reflection unchecked); S4 partial "
                                     "(top-5 per KB from round 2); S5 met (KB-off row); F3 avoided (training-set stores).",
                 "evidence_ids": ["son55:E001", "son55:E003", "son55:E004", "son55:E005"]},
            ],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2503.13856-1"): "local:2503.13856-4",
                    ("son55", "local:2503.13856-3"): "local:2503.13856-5",
                    ("sol", "rsi:abstract_experience_into_guidance/H00-step4"): "rsi:abstract_experience_into_guidance/H00.step4",
                    ("sol", "rsi:abstract_experience_into_guidance/H00-step5"): "rsi:abstract_experience_into_guidance/H00.step5"},
            overrides={
                "rsi:abstract_experience_into_guidance/H00.step4": {
                    "status": "met",
                    "reason": "Opus: son55's value. Step 4 asks that the lesson stream be separated from evaluation (store "
                              "frozen before testing): both KBs contain only training-set experiences and test items are not "
                              "written. The test-curve-informed choice of 600 rounds is a separate selection issue recorded "
                              "in local:2503.13856-5 and E.holdout."},
                "rsi:index_experience_for_reuse/S2": {
                    "status": "partial",
                    "reason": "Opus revision of son55 'met': gold correctness routes every case, so CorrectKB admission is "
                              "externally gated, but ChainKB admits every failed case with an unverified LLM-written reflection, "
                              "and Appendix A.4 describes a similarity-based correctness step."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Training-set-built KBs, frozen for test, with a same-backbone KB-off row and per-KB variants "
                                   "(MedQA 84.3→90.1, PubMedQA 77.6→83.9) and cross-dataset reuse (+3.6/+2.1).",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, gpt-4-turbo, single run: gold-routed knowledge bases built from 600 "
                                         "training consultations raise test accuracy by ~6 points on MedQA and PubMedQA; "
                                         "cross-dataset stores add 2–4 points. 'Transferable abstract reasoning', 'rationality', "
                                         "safety and efficiency claims exceed the evidence.",
            "unresolved": ["Test-set sizes, seeds, intervals (temperature 0.7, random tie-break).",
                           "Correctness gate: gold label (§3.3) vs similarity retrieval (Appendix A.4).",
                           "Medprompt row comparability (opus:O02) vs the 'all gpt-4-turbo' caption.",
                           "No same-cases-without-reflection or few-shot control; no overlap/contamination audit; no cost."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Concrete problems (context overload, stores without error "
                   "reflection), but the experience-store neighbours (ExpeL, IER, Agent Hospital) are only characterised, "
                   "not compared.",
                   ["sol:E001", "sol:E018", "son55:E014"]),
            "M": R("resolved", 3, "Opus sides with sol. Residual aggregation and outcome-routed dual stores are each tied to a "
                   "named problem and yield distinguishing predictions that are tested (residual+lead jointly vs either alone; "
                   "CorrectKB vs ChainKB vs both, opus:O01; accuracy vs store size). Below 4 because the abstraction-vs-raw-case "
                   "hypothesis is not separated and the gate needs privileged gold labels. son55's 'alternatives not "
                   "distinguished' concerns missing controls, charged under E.causality.",
                   ["sol:E003", "sol:E005", "sol:E006", "sol:E009", "opus:O01"], ["son55:E006"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithms 1–2, all prompts, record schemas, retrieval timing and "
                   "round caps make the chain reconstructable; gate description inconsistent (Appendix A.4) and no maintenance.",
                   ["sol:E002", "sol:E003", "sol:E005", "sol:E017", "son55:E003"], ["sol:E013"]),
            "E.measurement": R("resolved", 3, "Opus sides with son55. Accuracy/F1 against MedQA/PubMedQA gold answers is a "
                               "credible validator for the accuracy claim. Not 4: test sizes not stated, random tie-break, and "
                               "the rationality claim rests on a 10-question, 5-rater survey (an answer can be right with flawed "
                               "reasoning, sol:E014). The rationality/abstract-reasoning parts are excluded from the strongest "
                               "supported claim rather than scored down twice.",
                               ["son55:E007", "sol:E009", "sol:E015"], ["sol:E014", "son55:E013"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Clean same-backbone KB-off and per-KB ablations, but no "
                             "same-cases-without-reflection/few-shot control, no compute matching with baselines, and the "
                             "strongest baseline (Medprompt) appears to be under a different protocol (opus:O02).",
                             ["sol:E009", "sol:E010", "son55:E005", "son55:E008", "opus:O02"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Training-only stores and a cross-dataset test are real "
                           "separation; 600 rounds chosen with test-accuracy curves visible, no overlap/contamination audit, two "
                           "datasets in one domain.",
                           ["sol:E007", "sol:E011", "son55:E009"], ["sol:E012"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): negative component results and the human-eval size are "
                              "reported; no test sizes, seeds or intervals despite temperature 0.7.",
                              ["sol:E015", "sol:E019", "son55:E013"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked: no tokens/calls/latency for multi-round "
                        "consultation or the 600-round build; only a subjective low efficiency rating.",
                        ["sol:E016", "son55:E012"], [],
                        ["Full pinned v1 text §1–§5, Limitations, Appendices A–B; searched cost/token/latency/time/price."]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–B; in scope (A): outcome-routed non-weight knowledge bases written "
                  "after consultations and read in later ones.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["decompose_and_delegate", None]],
                "C03 (singleton under the parent) covers retrieving reference instances as first-class conditioning with a "
                "distribution-level test (Table 3) — partial fit; the role decomposition is a distinct operation and is kept "
                "as supporting.", ["son55:E003", "son55:E006", "son55:E005"], "none"),
            res("expectations[local:2503.13856-1].status", *C(p, "expectations[local:2503.13856-1].status"), "revised",
                "local-1 = sol's measurement question → partial; son55's local-1 (label-free deployment untested) kept as "
                "local:2503.13856-4 = unmet",
                "Same ID, different questions (A4 collision); both verified.", ["sol:E014", "son55:E001"], "none"),
            res("expectations[local:2503.13856-3].status", *C(p, "expectations[local:2503.13856-3].status"), "revised",
                "local-3 = sol's cost question → unmet; son55's local-3 (600 chosen with test curves visible) kept as "
                "local:2503.13856-5 = partial",
                "Same ID, different questions (A4 collision); both verified.", ["sol:E016", "son55:E009"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-1].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"),
                "son55", "met", "Verified: KB on/off with other modules fixed (Table 2 rows 4 vs 7).", ["son55:E005"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-2].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"),
                "son55", "unmet", "Verified: no overlap or contamination analysis.", ["son55:E004"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-3].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"),
                "son55", "unmet", "Verified: no nearest-neighbour few-shot or same-cases-without-reflection control.",
                ["son55:E005"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-4].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-4].status"),
                "son55", "partial", "Verified: seven configurations, single run, interacting modules.", ["son55:E005"], "none"),
            res("expectations[rs:adapt_via_conditioning/RE-5].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"),
                "son55", "partial", "Verified: two QA datasets, gold-label-dependent construction.", ["son55:E015", "son55:E001"],
                "none"),
            res("expectations[rs:adapt_via_conditioning/RE-6].status", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"),
                "son55", "partial", "Verified: accuracy vs stored-case curves (figure-only values) and one cross-dataset gap.",
                ["son55:E010", "son55:E006"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-1].status", *C(p, "expectations[rs:decompose_and_delegate/RE-1].status"),
                "son55", "unmet", "Verified: no cost of consultation or KB build.", ["son55:E012"], "none"),
            res("expectations[rs:decompose_and_delegate/RE-5].status", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"),
                "son55", "partial", "Verified, and sharpened by opus:O02 (Medprompt protocol mismatch).",
                ["son55:E007", "son55:E008", "opus:O02"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00-step4].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/H00-step4].status"), "son55",
                "met (canonical ID rsi:abstract_experience_into_guidance/H00.step4)",
                "sol's 'H00-step4' and son55's 'H00.step4' are the same card step (A4 syntax variant). Store/test separation "
                "is explicit; the 600-round choice is charged elsewhere.", ["son55:E004", "sol:E007"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00-step5].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/H00-step5].status"), "same_supported_fact",
                "partial (canonical ID rsi:abstract_experience_into_guidance/H00.step5)",
                "Same step, same status in both seats (store-off ablation, no budget match/variance).",
                ["sol:E009", "son55:E005"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00.step4].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/H00.step4].status"), "son55", "met",
                "See H00-step4 resolution.", ["son55:E004"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/H00.step5].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/H00.step5].status"), "same_supported_fact", "partial",
                "See H00-step5 resolution.", ["son55:E005", "son55:E013"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S2].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"), "sol", "partial",
                "Success and failure stores are both retrieved for a case (an implicit contrast), but no paired contrast is "
                "constructed; son55's domain check said unmet, sol's partial is the better reading.",
                ["sol:E003", "sol:E009"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S3].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "sol", "partial",
                "Verified the Appendix A.4 text (sol:E013): the correctness step is described as similarity retrieval, at odds "
                "with §3.3's gold validation; the grounding signal is therefore ambiguous (son55's domain check 'met' missed it).",
                ["sol:E002", "sol:E013"], "none"),
            res("expectations[rsi:abstract_experience_into_guidance/S4].status",
                *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "sol", "unmet",
                "Verified: no maintenance, contradiction removal or rollback.", ["sol:E003", "sol:E005"], "none"),
            res("expectations[rsi:index_experience_for_reuse/S2].status",
                *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"), "revised", "partial",
                "Gold routing gates CorrectKB admission, but every failed case enters ChainKB with an unchecked LLM reflection, "
                "and the appendix gate is ambiguous.", ["son55:E001", "son55:E002", "sol:E013"], "none"),
            res("ratings.M", *C(p, "ratings.M"), "sol", {"status": "resolved", "rating": 3},
                "See ratings.M: tested distinguishing predictions; missing controls charged to E.causality.",
                ["opus:O01", "sol:E009"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.measurement: gold-answer accuracy is credible; rationality claims scoped out, not double-penalised.",
                ["son55:E007", "sol:E014"], "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims[C1] / ratings.E.causality",
             "sol_value": "Medprompt comparison not discussed",
             "son55_value": "protocol differs (four-option) noted, caption contradiction not noted",
             "correction": "The Table 1 caption says all results used gpt-4-turbo, but the text explains the Medprompt gap by its "
                           "four-option-only evaluation, implying the row is not a same-protocol re-run; the closest baseline's "
                           "comparability is unresolved (recorded in assessment.unresolved and E.causality).",
             "evidence_ids": ["opus:O02", "son55:E007"], "score_impact": "none (E.causality already 2)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "In scope (A): gold-routed CorrectKB/ChainKB built on training sets, frozen at "
                                                   "test; clean KB-off and per-KB ablations; cross-dataset reuse; single run, no "
                                                   "test sizes/variance/cost; gate described two ways; Medprompt protocol unclear.",
            "integrity_checks": "Both seats a1 on 2503.13856v1, material sha a1fa1432…, hashes equal conflicts.json; quotes verbatim.",
            "core_claim_check": "Re-read §3.3, §4.1–4.6, Appendix A.4 and B.3; recomputed Table 1/2/3 deltas and averages "
                                "(all consistent; Table 2 row 6 avg 81.65 shown as 81.6).",
            "rating_agreement": "6/8 identical and re-checked; M → sol, E.measurement → son55.",
            "expectation_renumbering": "son55 local-1 → local-4, local-3 → local-5; sol H00-step4/5 → H00.step4/5.",
        },
    }
    return S


def batch_notes():
    return [
        "2503.00735 (LADDER): both seats' out_of_scope independently confirmed under A3 (GRPO weights are update target and "
        "product; TTRL rolls back; transformation library static). RS sub-card set to C08.",
        "2503.08026 (RMM): son55's scope hint confirmed — in scope only through the separately ablated non-weight PR memory "
        "bank; the RR reranker is a weight-updated auxiliary module whose online/eval boundary is unstated (E.holdout=1).",
        "Rating disputes resolved: 2502.16796 G,Em→son55, M→sol (48.75; sol 55.0, son55 43.75); 2503.08026 X,Ec→sol, Ecost→son55 "
        "(60.0; 61.25/58.75); 2503.10071 G→sol, Em,Es→son55 (33.75; 37.5/30.0); 2503.13856 M→sol, Em→son55 (58.75; 56.25/53.75).",
        "Seat-flagged internal inconsistencies verified: MobileSteward Table 2 vs 3 Task Rate (0.76 vs 0.81); RMM reranker "
        "linear (§6.1) vs MLP (A.1) and mislabelled table/figure references; ATLASS API-key prompt vs regex and GPT-3.5 cost "
        "claim vs future work; MDTeamGPT Appendix A.4 similarity-based correctness step vs §3.3 gold validation. Arithmetic in "
        "MobileSteward Table 5, RMM Table 3, ATLASS Table III and MDTeamGPT Tables 1–3 recomputed and consistent.",
        "Local expectation ID collisions (same ID, different questions) renumbered in 4 papers; recorded as shared corrections "
        "where the equal status hid them from the mechanical diff. No score impact.",
        "Card revision proposals (stage end, not applied): H00/H01 boundary for a single write/no-write decision (MobileSteward); "
        "son55's 'consumer-credited retrieval selector' sub-condition (RMM, single source); A3 scope note for small trained "
        "auxiliary modules (rerankers/adapters) inside a harness.",
        "Material requests (not blocking): fixed originals of MobileGPT/AutoDroid, MemoryBank/LD-Agent/Theanine, LATM, "
        "ExpeL/Agent Hospital/IER would allow verifying the authors' neighbour characterisations (G items).",
    ]
