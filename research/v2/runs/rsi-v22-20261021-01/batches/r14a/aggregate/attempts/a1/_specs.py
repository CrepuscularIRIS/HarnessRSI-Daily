"""Opus rulings for r14a a1 (data only; consumed by _build.py)."""
import copy

BIND_24639 = (
    "conflicts.json (written 20:42:02 local) binds sol 2603.24639 to hash 829f13af…, but the sol worker rewrote "
    "the file at 20:42:40 and wrote its batch-report at 20:42:58. No version on disk or in git (the only commit, "
    "807b252, holds the rewrite) has the bound hash, so conflicts.json was computed from a pre-final sol draft. A "
    "fresh rv2.diff_pair of the final sol file against son55 differs from conflicts.json in four expectation "
    "fields: the draft lacked sol RE-4/RE-5/RE-6 and used the ID S2 where the final uses step2. The rating, "
    "pattern and evidence-level conflict fields are unchanged. This aggregate is built on the final sol file "
    "(seat_inputs_used) and resolves the union of both field sets. Controller action: regenerate conflicts.json "
    "for 2603.24639, then re-issue this record (no change of substance expected) as accepted_final.")


def batch_notes():
    return [
        "Seat-input integrity (controller action needed). (1) sol 2603.18000: the working copy was rewritten at "
        "20:42:40, after conflicts.json (20:42:02). The only change is score.display (50 → 50.0). The version in "
        "commit 0014a72 matches the conflicts.json hash, and this aggregate is bound to it (git show, read-only); "
        "accepted_final stands. (2) sol 2603.24639: " + BIND_24639,
        "2603.18000 AgentFactory (seat Δ8.75): final 41.25 = son55. evidence_level → son55 task. The library is "
        "built on Batch 1 and read on Batch 2, but no same-scaffold store-off (AgentFactory on Batch 2 from "
        "scratch) is reported. Opus Batch 1 already halves orchestrator tokens before any reuse (4324 vs 8298), "
        "and the metric excludes subagent-internal LLM calls, so an accounting shift is not ruled out. Unlike the "
        "SWE-Exp k=0 precedent, there is no same-scaffold control, so 'retained' is not earned. M → son55 2 (no "
        "separating prediction against the named Voyager code library). E.causality → son55 1. Domain → sol (H07 "
        "only; H12 is the less specific card for the same repair step). Shared correction: 'We ensure that all "
        "tasks are completed without runtime errors' also hides any reruns from the failure denominator.",
        "2603.18620 LSE (Δ1.25): final 61.25 = son55. E.holdout → son55 1: improver train/eval domains are "
        "disjoint and checkpoints are chosen on a separate dev set, but every headline is best-of-25 on the same "
        "50-problem D that drives UCB. Opus adds that batch/D disjointness is unstated, while the summaries carry "
        "ground-truth answers and evolved MMLU instructions contain answer-level facts. E.causality → son55 2: "
        "trained-vs-untrained in the same loop is clean, but the reward ablation is BIRD-only and nothing separates "
        "feedback-driven evolution from a learned static instruction. The Arctic transfer has no untrained-improver "
        "arm, and RL training cost is unpriced against the untrained baselines.",
        "2603.23129 Polaris (seat Δ15): final 45.0 (sol 57.5 / son55 42.5). evidence_level → son55 task: runs are "
        "labelled 'Successful' by test improvement, the headline is the maximum over successful runs, and best-so-"
        "far is read off the test curve. Patch integration has no performance gate, so the test set is the only "
        "selection set (EVIDENCE rule 2). RS → sol outside_taxonomy: assumption_audit_and_pivot audits a result's "
        "or defence's assumption and re-proves; a context-budget engineering change is a forced low-fit match. "
        "son55's RE answers are kept as check questions only. G → son55 2, M → son55 2, E.measurement → sol 3 "
        "(A2: son55's grounds are selection/statistics defects charged in E.holdout/E.statistics), E.holdout → "
        "son55 1, E.cost → son55 1 (wall-clock/hardware only, per-query cost of evolved multi-response policies "
        "absent; r09/r10 precedent). Shared correction: the 'No improvement' threshold is stated as ≤0.8%, but on "
        "the 100-item GPQA test 2 samples = 2%. A4: sol local-1..4 and son55 local-1..3 asked different questions "
        "under the same IDs; merged by substance (sol local-1 → H12-step4, local-2 → local-3, local-3 → local-1, "
        "local-4 → local-2; sol S2 → S4, because S2 is evaluation-budget steering).",
        "2603.23420 Bilevel Autoresearch (seat Δ15): final 47.5 (sol 56.25 / son55 41.25). G → son55 2: the "
        "self-referential improver lineage (Gödel Agent, DGM, ADAS) is absent from related work, and the novelty "
        "claim is scoped to 'autoresearch systems'. M → son55 2: the generated mechanisms (tabu, bandit, "
        "orthogonal) are textbook diversification tools. No prediction separates LLM-generated mechanisms from "
        "simply diversifying a proposer that 'given the same state, generates nearly the same proposals every "
        "time'. E.measurement → sol 3 (A2: noise and selection grounds charged elsewhere). E.statistics → sol 2 "
        "(cross-run SD over 3 repeats exceeds the ladder-2 description; no interval or test keeps it below 3). "
        "E.holdout → sol resolved 0 (same rating; it rests on a reported design fact). E.causality 2 kept for both "
        "seats; Group D's gains without applied patches are the main counterevidence. Domain → sol (H19 only).",
        "2603.24639 ERL (Δ2.5): final 62.5, provisional, needs_revision (seat binding only; see above). "
        "evidence_level retained (both seats): a frozen pool from 8 universes is read on 2 disjoint universes with "
        "a store-off control. E.holdout → sol 2: Table 3 shows the k sweep and retriever comparison were run on "
        "the test universes (headline 56.1 = the k=20 cell), and the retrieval prompt was hand-selected; test-"
        "tuned k is charged here, not by lowering the level (SWE-Exp precedent). E.statistics → sol 2 (A2 ladder: "
        "pass^3/pass@3 are repeated-run failure counts; no intervals). E.cost → son55 3: per-phase tokens and "
        "dollars (+40%) and a token-matched few-shot control are reported. Not 4: retry-based baselines are not "
        "costed and latency is unmeasured. Source rollouts are not an extra cost under the paper's deployment "
        "framing. RS → sol (sub null: frozen model, no category holdout; r13b/r04b C03 convention). son55's "
        "non-A4 IDs budget-matched/variance/reflector-cost → H00-step5 / local-4 / local-5; sol step2 → S2; sol "
        "local-1/local-2 → local-4/local-6 (hidden collisions).",
        "Figure dependence: Polaris per-iteration accuracy curves (Figs. 3–6, 13–17), Bilevel Fig. 4, LSE Figs. "
        "2–3 and ERL Figs. 3–5 are image-only. Only values stated in text or tables are used, and no figure value "
        "was invented. Polaris absolute accuracies are not in the text, so its gains are cited only as the "
        "authors' relative figures.",
        "No material requests. The seats' requests for neighbour originals (Voyager/DGM, GEPA/TextGrad, Gödel "
        "Agent, AEvo/GEAR/Meta-Harness, ExpeL/AutoGuide) are non-blocking: each G rating rests on what the paper "
        "itself cites and omits.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    NOLVL = "none (evidence_level is not scored)"

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

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a = prefix(a, s)
        a.update(upd)
        return a

    def moved(old):
        return {"merged_from": old, "note": f"Merged here from {old} (A4: same question under a colliding or "
                                            "non-grammar ID)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on rs_pattern)."}

    # =========================================================== 2603.18000 AgentFactory (Δ8.75)
    p = "2603.18000"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "We ensure that all tasks are completed without runtime errors in all experiments.",
                    "§5.1 Evaluation Metric",
                    "'Ensure' implies runs were checked and, where needed, redone until error-free. The number of "
                    "failed/rerun attempts and their tokens are not reported, so the per-task means exclude a "
                    "failure denominator. Also, 'no runtime error' is the only correctness criterion.",
                    kind="our_inference"),
            opus_ev(p, "O02", "A notable finding is that Opus 4.6 already shows a significant reduction in "
                              "orchestration tokens during Batch 1 itself under AgentFactory (4324 vs. 8298 for ReAct)",
                    "§5.2 Results",
                    "Before any cross-batch reuse, the delegating architecture already halves the counted tokens, "
                    "because subagent-internal calls are excluded from the count. The Batch 2 contrast with ReAct "
                    "therefore mixes reuse with an accounting/architecture effect.", kind="our_inference"),
            opus_ev(p, "O03", "running the second batch with subagents created when evaluating on the first batch",
                    "§5.2 Results",
                    "AgentFactory has only two rows (Batch 1 from scratch, Batch 2 with saved). There is no "
                    "AgentFactory-on-Batch-2-from-scratch row, i.e. no same-scaffold store-off on the evaluated "
                    "tasks.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: decompose_and_delegate/C25 (executable intermediate artefacts retained as a "
                      "reusable library). Fit medium: the interpreter certifies only that code runs, not that it is "
                      "semantically right, and the load-bearing step is not ablated.",
            "matches": [smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "local:2603.18000-1": {
                    "status": "unmet",
                    "reason": "Opus (both seats asked the same total-cost/efficiency question): the only measure is "
                              "orchestrator output tokens with subagent-internal calls explicitly excluded. Input "
                              "tokens, total calls, latency and correctness are absent, so the expectation is unmet, "
                              "not partially met."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: no AgentFactory Batch-2-from-scratch row (same-scaffold store-off) (opus:O03).",
            "Opus: failed/rerun attempts behind 'we ensure … without runtime errors' are not counted (opus:O01)."],
            evidence_level="task",
            evidence_level_note="A self-written library is retained and read on separate Batch 2 tasks, but the "
                                "improvement is never isolated from the architecture: there is no same-scaffold "
                                "store-off, Batch 1 already shows the token drop without reuse, and the count "
                                "excludes subagent calls. EVIDENCE 'retained' requires the retained change to "
                                "produce the gain; here that is not shown. Contrast SWE-Exp (r-precedent), which "
                                "had a same-scaffold k=0 control."),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The text-vs-executable-store axis is real, but 'text "
                   "cannot guarantee re-execution' is asserted, and the closest neighbour (Voyager's executable "
                   "skill library) is named only, never differentiated.",
                   ["son55:E012", "son55:E013", "sol:E012"]),
            "M": R("resolved", 2, "Opus sides with son55. Create → save-on-success (Meta-Agent judgement) → retrieve "
                   "→ modify-on-failure → validate on the current task is a coherent chain, but it is the "
                   "Voyager-style recipe. The paper offers no reasoned prediction that separates it from a code-"
                   "skill library or from a well-built text store. Admission rests on an LLM's judgement of "
                   "'successful completion'. sol's 3 credits plausibility that anchor 2 already covers.",
                   ["son55:E001", "son55:E002", "son55:E003", "sol:E005"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Create/modify/save/list/view primitives, workspace "
                   "isolation and promotion are reconstructible. Validation is on the current task only, with no "
                   "regression replay, versioning, rollback or retirement.",
                   ["sol:E002", "sol:E003", "sol:E004", "son55:E004"]),
            "E.measurement": R("resolved", 1, "Both seats 1; re-checked. The only metric is orchestrator output "
                               "tokens, excluding subagent-internal LLM calls. 'Success' means no runtime error, and "
                               "chart/report/booking correctness is never checked (opus:O01).",
                               ["son55:E006", "son55:E007", "son55:E016", "opus:O01"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. Same-backbone ReAct and textual-experience "
                             "baselines exist, but the key alternative explanation is untested: the delegation "
                             "architecture moves work into uncounted subagent calls. Opus Batch 1 already shows "
                             "4324 vs 8298 before any reuse (opus:O02), and there is no same-scaffold store-off on "
                             "Batch 2 (opus:O03). Nothing ablates save/modify/tool allocation, and Sonnet Batch 1 "
                             "(9199 > 6893) contradicts the within-batch claim. Budget non-parity is charged here and "
                             "in E.cost (A2).",
                             ["son55:E009", "son55:E011", "son55:E015", "sol:E013", "sol:E014", "opus:O02", "opus:O03"],
                             ["son55:E008"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. The library is built on Batch 1 and read on 15 "
                           "separate Batch 2 tasks. Those tasks are 1:1 mirrored variants (the H07 'fixed input "
                           "shape' failure), it is not stated whether the library is frozen during Batch 2, and the "
                           "cross-system claim is a single anecdote.",
                           ["sol:E008", "sol:E010", "son55:E005", "son55:E014"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): n=15 per cell, and a negative cell (Sonnet "
                              "Batch 1) is visible. Single runs, no variance; reruns behind 'we ensure' are uncounted "
                              "(opus:O01).", ["sol:E013", "sol:E014", "son55:E009", "opus:O01"]),
            "E.cost": R("resolved", 1, "Both seats 1. Cost is the headline, but it counts only orchestrator output "
                        "tokens. Subagent calls, input tokens, latency and the cost of building/modifying subagents "
                        "are absent.", ["son55:E006", "son55:E016", "sol:E006"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text (with Appendices A–B) read. In scope (system_method): executable "
                  "subagent code is written from execution feedback, retained, and read on later tasks. All eight "
                  "items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 1–3 are schematic or case diagrams; all numbers come from Table 1 and the text.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "See assessment.evidence_level_note. Without a same-scaffold store-off, and with Batch 1 already "
                "showing the effect, the retained library is not shown to produce the gain. sol's 'retained' treats "
                "'the change was kept and reused' as 'the kept change improved later tasks'.",
                ["opus:O02", "opus:O03", "son55:E016"], NOLVL),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["crystallize_executable_capability", "H07"]],
                "H07 already covers the traceback-driven repair of a forged tool ('debug it against execution "
                "feedback, and register it'). son55's H12 (low fit) needs recurring-mechanism diagnosis over harness "
                "code plus a replay/regression promotion gate, and neither is present. The modify step is H07's "
                "repair loop on reuse, not a second pattern.", ["sol:E003", "son55:E003"], NOSCORE),
            XC(p, "local:2603.18000-1", "son55", "unmet",
               "Same question in both seats (total efficiency including delegated calls). sol's 'partial' rests on "
               "the very exclusion that makes it unmet: subagent calls are excluded by design.",
               ["son55:E006", "son55:E016", "sol:E006"]),
            XC(p, "local:2603.18000-2", "son55", "unmet",
               "Verified: modified subagents are validated only on the current task, with no regression check on "
               "earlier tasks and no rollback.", ["son55:E003"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Verified: the added structure's own cost (subagent LLM calls, creation, modification) is the part "
               "excluded from the only cost metric.", ["son55:E006", "son55:E016"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "Verified: there is no ablation of save, modify or tool allocation, and no same-scaffold store-off "
               "(opus:O03).", ["son55:E009", "opus:O03"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Verified: Batch 1 spans several domains, but Batch 2 mirrors it 1:1, and cross-system use is one "
               "anecdote.", ["son55:E005", "son55:E014"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "Verified: ReAct and a textual-experience agent are compared; no executable-library neighbour "
               "(Voyager) is.", ["son55:E011", "son55:E013"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "partial",
               "Verified: the bottleneck is asserted. The textual-experience comparison probes it only "
               "indirectly, through a confounded token metric.", ["son55:E012"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "partial",
               "Failure mode partly present (son55 convention: met = avoided). The forged subagent is measured only "
               "through whole-framework orchestrator tokens, never as an isolated artefact.", ["son55:E006"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: coherent chain, but no prediction distinguishes it from the named Voyager-style "
                "library.", ["son55:E001", "son55:E013"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality: the architecture/accounting alternative (opus:O02) and the missing "
                "same-scaffold store-off (opus:O03) leave the reuse effect unisolated. sol's 2 treats the ReAct and "
                "text baselines as isolating the narrow efficiency gap.",
                ["opus:O02", "opus:O03", "son55:E009"], "−3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.statistics.reason", "sol_value": "1 (runtime-error clause read as a "
             "correctness gap only)", "son55_value": "1 (same)", "final_value": 1,
             "reason": "Both seats read 'We ensure that all tasks are completed without runtime errors' only as a "
                       "weak success criterion. It also means failed or rerun attempts, and their tokens, sit "
                       "outside the reported means, so the failure denominator is hidden. Recorded in "
                       "E.statistics/E.measurement; no rating change, since both items are already at 1.",
             "evidence_ids": ["opus:O01"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: in scope; one metric "
                                                   "(orchestrator output tokens minus subagent calls); 'success' is "
                                                   "runtime-error-free; no same-scaffold store-off; Batch 1 already "
                                                   "shows the drop. G 1–2, M 2, X 2, Em 1, Ec 1, Eh 1–2, Es 1, "
                                                   "E.cost 1; evidence_level task.",
            "integrity_checks": "son55 a1 hash equals conflicts.json. sol a1 working copy rewritten after "
                                "conflicts.json (score.display type only); bound to commit 0014a72, whose canonical "
                                "hash equals conflicts.json. Both seats on 2603.18000v1, material sha b3859b6c…; "
                                "RS/domain IDs valid.",
            "core_claim_check": "Strongest supported claim: on 15 mirrored Batch 2 tasks, the orchestrator emits "
                                "fewer output tokens when saved subagents exist than ReAct or a textual-memory agent "
                                "does. Total cost, correctness and the reuse effect itself are not established. "
                                "claim_support scoped.",
            "rating_agreement": "G, X, Em, Eh, Es, E.cost agree and were re-checked; M and E.causality → son55. "
                                "Final 41.25.",
        },
    }

    # =========================================================== 2603.18620 Learning to Self-Evolve (Δ1.25)
    p = "2603.18620"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "report the best holdout performance achieved by each self-evolving method over the "
                              "course of evolution", "Appendix A, Evaluation protocol",
                    "The reported number is a max over 25 rounds on D, the same set that scores every node for UCB "
                    "selection and the final argmax."),
            opus_ev(p, "O02", "At each round, a batch of 10 problems is sampled with replacement and presented to "
                              "the action model.", "Appendix A, Evaluation protocol",
                    "Batches are drawn from the domain's problem pool (Table 4 lists 95–191 'evaluation problems per "
                    "domain'). Nowhere does the text say the batch pool excludes the 50 D problems.",
                    kind="our_inference"),
            opus_ev(p, "O03", "containing the problems, the outputs of the action LLM, ground-truth answers, and "
                              "per-problem correctness signals", "§3.2",
                    "The improver sees ground-truth answers for every batch problem."),
            opus_ev(p, "O04", "fertilization occurs in the fallopian tube, not the ovary or uterus",
                    "Appendix B.3, example instruction found by LSE (MMLU-Redux Anatomy)",
                    "Evolved instructions carry answer-level factual content. With ground-truth-bearing summaries "
                    "and unstated batch/D disjointness, part of the D gain may be answer transfer rather than better "
                    "procedure.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: reframe_as_solvable_object, sub null. Multi-step self-evolution is recast as a "
                      "single-step contextual bandit, with the pre-edit score as a known baseline. No C-sub fits.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "amortize_improver_into_trained_policy", "H27"),
                                       dmatch("son55", p, "attribute_and_patch_incumbent", "H10")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "rsi:amortize_improver_into_trained_policy/H27"):
                    "rsi:amortize_improver_into_trained_policy/H27-step5"},
            order=("son55", "sol"),
            overrides={
                "rsi:amortize_improver_into_trained_policy/H27-step5": {
                    "status": "partial",
                    "reason": "Opus: the same-size untrained improver runs with identical tree search, seeds and "
                              "rounds, so that part is met. But checkpoints are chosen on a separate dev set while "
                              "every headline is best-of-25 on D, and training cost is not priced.",
                    **moved("sol:rsi:amortize_improver_into_trained_policy/H27")},
                "local:2603.18620-2": {
                    "status": "unmet",
                    "reason": "Opus (both seats asked about statistics): one fixed seed per method, no interval or "
                              "test, and sub-point MMLU margins called 'matches'. Eight generations per D evaluation "
                              "reduce evaluation noise but are not an uncertainty estimate of the search."},
                "rsi:amortize_improver_into_trained_policy/S5": {
                    "status": "partial",
                    "reason": "Opus (revised from unmet): each improver trains across many databases (BIRD train) "
                              "or subjects (SuperGPQA) and is tested on unseen ones, i.e. across task families "
                              "within a task type. It does not cross task types, one policy per domain (conceded)."},
                "rsi:evidence_gated_retention/S1": {
                    "note": "Check question only (evidence_gated_retention is not a domain match). Met: the training "
                            "reward and the tree both credit an edit against an explicit counterfactual (pre-edit/"
                            "parent score)."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O04"]),
        "assessment": assess("son55", p, [
            "Opus: batch/D disjointness unstated while summaries contain ground-truth answers; evolved instructions "
            "contain answer-level facts (opus:O02–O04)."],
            evidence_level="task",
            evidence_level_note="EVIDENCE rule 2: every reported context score is a max on D, which also selects "
                                "nodes. The trained improver's domain hold-out is real but is graded in E.holdout; "
                                "it does not make the retained contexts 'retained' evidence."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A specific residual (the improver is never trained for "
                   "editing) is probed by a trained-vs-untrained 4B comparison, and prompt-optimiser, self-"
                   "referential and memory neighbours are surveyed. Not 4: RL-trained prompt-rewriting or reflection "
                   "models are not surveyed, so 'never explicitly train it' is unverified.",
                   ["son55:E002", "son55:E010", "son55:E016", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. The bandit reduction, null-edit baseline and tree-"
                   "sampled start states are derived honestly, including the admission that the delta and post-edit "
                   "rewards give equal gradients under a learned baseline. The correspondence between single-step "
                   "training and multi-step use is unproven.",
                   ["son55:E001", "son55:E012", "son55:E022", "son55:E026"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Algorithm 1, the edited field, prompts, the UCB rule "
                   "and the training recipe are reproducible. Retention is within-run tree only.",
                   ["son55:E015", "son55:E023", "son55:E024", "sol:E002", "sol:E010"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. SQL execution accuracy and MCQ accuracy "
                               "(8 generations each) are credible verifiers. The best-of-rounds aggregation and the "
                               "answer-transfer channel are charged in E.holdout (A2).",
                               ["son55:E005", "sol:E007", "sol:E009"]),
            "E.causality": R("resolved", 2, "Opus sides with son55. Trained-vs-untrained in the same loop and seeds "
                             "is clean, and frontier, GEPA and TextGrad improvers share protocol. But: the reward "
                             "ablation is BIRD-only, and the paper shows it reduces to a baseline-estimator change; "
                             "tree vs chain is tested only with the untrained improver; the Arctic transfer has no "
                             "untrained-improver arm. No control separates feedback-driven evolution from a learned "
                             "static instruction (first-edit-only or shuffled-summary). The RL training budget is "
                             "unpriced against the untrained baselines (A2).",
                             ["son55:E010", "son55:E011", "son55:E013", "son55:E014", "son55:E025", "sol:E013"],
                             ["son55:E012"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Improver training and evaluation use disjoint "
                           "domains (BIRD train → Mini-Dev DBs; SuperGPQA → MMLU-Redux), and checkpoints are picked "
                           "on a separate dev set; this is real hold-out evidence for the trained component, so not "
                           "0. But every reported context score is best-of-25 on the D that drives UCB (opus:O01). "
                           "Batch/D disjointness is unstated (opus:O02), while ground-truth answers reach the "
                           "improver (opus:O03) and evolved instructions carry answer-level facts (opus:O04).",
                           ["son55:E003", "son55:E004", "son55:E018", "son55:E019", "son55:E020",
                            "opus:O01", "opus:O02", "opus:O03", "opus:O04"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sample sizes are reported, but there is "
                              "one fixed seed, no interval or test, and sub-point MMLU margins.",
                              ["son55:E005", "son55:E008", "son55:E027", "sol:E010"]),
            "E.cost": R("resolved", 1, "Both seats 1. Rounds are matched, but RL training (200×20 data generation, "
                        "4 epochs) and frontier-improver calls are not costed or compared.",
                        ["son55:E017", "sol:E011", "sol:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text, including Appendices A–B, read. In scope per A3 "
                  "(component_training): the retained object is a non-weight instruction context; the improver is "
                  "weight-trained. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "A3 second clause: retained artefact non-weight (instruction field), improver trained → in scope as "
              "component_training (both seats).",
        "figure_dependence": "Figure 2(a)/(b) values used only as stated in the text; the Figure 3 per-round curve "
                             "is image-only and not used numerically.",
        "resolutions": [
            XC(p, "local:2603.18620-2", "son55", "unmet",
               "Same statistics question in both seats. Eight generations average evaluation noise but do not "
               "estimate search variance; no seed repeats, so unmet.", ["son55:E027", "sol:E010"]),
            XC(p, "local:2603.18620-3", "son55", "unmet",
               "Verified: Table 3 has only seed vs +LSE evolution for Arctic; no untrained-improver arm.",
               ["son55:E014"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "son55", "unmet",
               "Verified: no proof that single-step training corresponds to multi-step use; conceded in Limitations.",
               ["son55:E022"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "partial",
               "Verified: multi-round tree use with ground-truth accuracy is an empirical faithfulness check, but "
               "there is no per-depth analysis or multi-step-trained comparator.", ["son55:E010", "son55:E022"]),
            XC(p, "rs:reframe_as_solvable_object/RE-5", "son55", "partial",
               "Verified: lower rollout cost is argued, not measured; small environments are conceded.",
               ["son55:E017", "son55:E026"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/F1", "son55", "partial",
               "Failure mode partly present: the delta-baseline policy-gradient recipe on a known evolve loop is "
               "the main novelty, though the trained object is the paper's point.", ["son55:E001", "son55:E012"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/H27", "same_supported_fact",
               {"moved_to": "rsi:amortize_improver_into_trained_policy/H27-step5", "status": "partial"},
               "sol's whole-card H27 check (same-size untrained and search comparisons present; no independent test "
               "or cost match) is son55's H27 step 5. Same finding, same status; merged under the step ID.",
               ["sol:E007", "sol:E009", "son55:E010"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/H27-step5", "same_supported_fact", "partial",
               "See H27: same substance from both seats (sol's entry merged here).", ["son55:E010", "son55:E018"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S5", "revised", "partial",
               "son55 wrote unmet (one policy per domain). The card asks for meta-training across task families. "
               "Each improver trains across many databases/subjects and is tested on unseen ones, so partial; it "
               "does not cross task types.", ["son55:E015", "son55:E019", "sol:E018"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "sol", "partial",
               "Verified: the tree keeps all nodes and can backtrack, but nothing protects earlier wins beyond the "
               "argmax on the same D.", ["sol:E014", "sol:E008"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "met",
               "Check question only (card not matched). Verified: each edit is credited against its pre-edit/"
               "parent score.", ["son55:E001", "son55:E003"]),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 2,
                "See ratings.E.causality: the clean trained-vs-untrained contrast is offset by a BIRD-only reward "
                "ablation, no learned-static-instruction control, no untrained arm for transfer, and unpriced "
                "training budget. sol's 3 treats the three ablations as near-factorial isolation.",
                ["son55:E011", "son55:E012", "son55:E014"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: the domain hold-out of the trained improver keeps it above 0. Reporting "
                "best-of-25 on the selection set D, plus the unstated batch/D disjointness, keeps it at 1.",
                ["son55:E019", "opus:O01", "opus:O02"], "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.reason", "sol_value": "0 (D reuse; no batch/D overlap analysis)",
             "son55_value": "1 (overlap 'unstated', not linked to answer content)", "final_value": 1,
             "reason": "Neither seat connected three facts: the improver sees ground-truth answers for each batch "
                       "(opus:O03); the batch pool is not stated to exclude D (opus:O02); and the evolved MMLU "
                       "instruction contains answer-level facts (opus:O04). Together these form a possible answer-"
                       "transfer channel into D scores. It supports, not changes, the rating of 1.",
             "evidence_ids": ["opus:O02", "opus:O03", "opus:O04"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. Initial view: component_training "
                                                   "in scope; headline is best-of-25 on the UCB set D, with a real "
                                                   "domain hold-out for the trained improver. G 3, M 3, X 3, Em 3, "
                                                   "Ec 2, Eh 1, Es 1, E.cost 1; evidence_level task.",
            "integrity_checks": "Both seats a1 hash-equal to conflicts.json; 2603.18620v1, material sha 836565cb…; "
                                "both claim_type component_training; IDs valid.",
            "core_claim_check": "Strongest supported claim: under a protocol that selects and reports contexts on "
                                "the same 50 problems, an RL-trained 4B improver beats its untrained twin by ~5 pts "
                                "(BIRD) and ~2 pts (MMLU-Redux), with unquantified variance. claim_support scoped.",
            "rating_agreement": "Six items agree and were re-checked; E.causality and E.holdout → son55. Final "
                                "61.25.",
        },
    }

    # =========================================================== 2603.23129 Polaris (Δ15)
    p = "2603.23129"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "This yields a monotone non-decreasing performance profile for the deployed agent, "
                              "even if the internal search process remains volatile and exploratory.",
                    "Appendix B.4",
                    "The champion–challenger rule is described as what a deployment 'would' do. It is not part of "
                    "Algorithm 2, whose integration has no performance check, so the reported best-so-far policy is "
                    "picked post hoc."),
            opus_ev(p, "O02", "policy update improves test performance;", "§4, run categories",
                    "Run labels ('Successful') are defined on the test set; the headline then takes the maximum "
                    "over successful runs."),
            opus_ev(p, "O03", "policy update succeeds but yields no meaningful performance gain, defined as an "
                              "accuracy increase corresponding to", "§4, run categories",
                    "The threshold is '≤2 additional correctly solved samples (≤0.8%)'. That percentage holds for "
                    "250-item tests, but GPQA's test set has 100 items ('for GPQA, 20 validation and 100 test "
                    "samples'), where 2 samples = 2%.", kind="our_inference"),
            opus_ev(p, "O04", "Empirical results demonstrate consistent gains without supervision or retraining",
                    "§6 Conclusion",
                    "Failure analysis reads the reference answer, and only 17–18 of 40 Qwen2.5 runs are "
                    "'Successful'. Both 'without supervision' and 'consistent' overstate the evidence.",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": None, "supporting": [], "matches": [], "outside_taxonomy": True,
            "reason": "Opus sides with sol. assumption_audit_and_pivot locates the assumption behind a result, "
                      "guarantee or defence, relaxes it and re-derives, or violates it. Its success conditions "
                      "(tightness certificates, weaker condition shown to hold) and RE list are about guarantees. "
                      "Polaris shrinks the context budget of Gödel Agent for a 7B model, an engineering change; "
                      "son55 itself rates the fit 'low'. No other original card's operation is executed: "
                      "decompose_and_delegate needs routing to sound solvers, adapt_via_conditioning in-context "
                      "conditioning, self_supervised_signal_engineering a label-free signal (reference answers are "
                      "used here).",
            "executes_pattern": False, "resolves_problem": False,
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol"),
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12")],
                           "unassigned": ["make_the_improver_editable/H19 considered by both seats: Appendix A says "
                                          "the agent may rewrite its own improvement code, but repair operators and "
                                          "prompts are fixed and no improver-level edit is evidenced."],
                           "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.23129-1"): "rsi:attribute_and_patch_incumbent/H12-step4",
                    ("sol", "local:2603.23129-2"): "local:2603.23129-3",
                    ("sol", "local:2603.23129-3"): "local:2603.23129-1",
                    ("sol", "local:2603.23129-4"): "local:2603.23129-2",
                    ("sol", "rsi:attribute_and_patch_incumbent/S2"): "rsi:attribute_and_patch_incumbent/S4"},
            order=("son55", "sol"),
            overrides={
                "local:2603.23129-1": {
                    "status": "partial",
                    "reason": "Opus (revised): all-run denominators are reported (Tables 2–4: successful / no "
                              "improvement / unsuccessful per dataset), and bootstrap CIs are stated for two "
                              "datasets. But no expected gain or variance over all runs is given; the headline is "
                              "the max over successful runs.", **moved("sol:local:2603.23129-3")},
                "local:2603.23129-2": {
                    "status": "unmet",
                    "reason": "Opus: evolved GPQA/LitBench policies add responses and expert evaluators, but "
                              "neither per-query inference cost nor a cost-matched CoT-SC is reported. The 10-hour "
                              "evolution budget answers a different question.", **moved("sol:local:2603.23129-4")},
                "local:2603.23129-3": {
                    "status": "unmet",
                    "reason": "Opus: no abstraction-off variant (patching directly from reflections, or the same "
                              "memory budget without strategy synthesis). The Gödel Agent baseline differs in many "
                              "factors and never completes.", **moved("sol:local:2603.23129-2")},
                "rsi:attribute_and_patch_incumbent/H12-step4": {
                    "status": "unmet",
                    "reason": "Opus: patches are promoted on executability alone (opus:O01). Success labels and "
                              "best-so-far come from the test set (opus:O02), so there is no separate promotion "
                              "split.", **moved("sol:local:2603.23129-1")},
                "rsi:attribute_and_patch_incumbent/S4": {
                    "status": "partial",
                    "reason": "Opus: reflections over N=3/5 failed validation items are abstracted into 1–2 "
                              "strategies, a mechanism-level step. But there is no clustering across failure "
                              "families, and N is tiny.", **moved("sol:rsi:attribute_and_patch_incumbent/S2")},
                "rs:assumption_audit_and_pivot/RE-1": dropped_card("assumption_audit_and_pivot"),
                "rs:assumption_audit_and_pivot/RE-2": dropped_card("assumption_audit_and_pivot"),
                "rs:assumption_audit_and_pivot/RE-4": dropped_card("assumption_audit_and_pivot"),
                "rs:assumption_audit_and_pivot/RE-6": dropped_card("assumption_audit_and_pivot"),
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O01", "opus:O02", "opus:O04"]),
        "assessment": assess("son55", p, [
            "Opus: champion selection is hypothetical; best-so-far is read off test curves (opus:O01, opus:O02)."],
            evidence_level="task",
            evidence_level_note="Patches persist and are applied to unseen test items. But integration has no "
                                "performance gate, so the test set is the only place where runs are labelled and "
                                "best iterations chosen; EVIDENCE rule 2 caps the level at task."),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The bottleneck is real and evidenced (Table 1: the trimmed "
                   "Gödel Agent rarely completes at 7B), but the residue is a context-budget limit of one framework "
                   "configuration. Small-model-friendly self-improvement loops that are not Gödel-style (prompt or "
                   "workflow optimisers, memory/insight systems) are not positioned. Hence 'recursive self-"
                   "improvement with SLMs' as a gap is not shown beyond this framework (anchor 2: neighbour "
                   "comparison incomplete).",
                   ["son55:E002", "son55:E009", "son55:E013", "son55:E014", "son55:E027", "sol:E001"]),
            "M": R("resolved", 2, "Opus sides with son55. Reflection on N failures → 1–2 strategies → minimal "
                   "patch → executability check is a coherent context-control mechanism. Its key premise, that "
                   "abstraction rather than simply a smaller context makes 7B repair work, is never stated as a "
                   "prediction distinguishing it from naive alternatives; the improver is a fixed prompt pipeline.",
                   ["son55:E025", "son55:E026", "son55:E028", "sol:E002", "sol:E003"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithms and prompts are given. Acceptance is "
                   "executability only, rollback is deliberately omitted, and the champion rule is hypothetical "
                   "(opus:O01).", ["son55:E003", "son55:E004", "son55:E025", "sol:E010", "sol:E014", "opus:O01"]),
            "E.measurement": R("resolved", 3, "Opus sides with sol. MGSM/GPQA accuracy, DROP F1 and LitBench "
                               "preference accuracy against references are credible verifiers. son55's grounds are "
                               "the max-over-successful-runs aggregation and test-defined success, a selection "
                               "defect charged in E.holdout, and small test sets, charged in E.statistics (A2: one "
                               "defect, one item). Not 4: an LLM JSON 'helper' rewrites outputs during evaluation "
                               "and is not audited; the 'No improvement' threshold misstates GPQA's 2% as 0.8% "
                               "(opus:O03).", ["sol:E004", "sol:E005", "sol:E015", "son55:E016", "opus:O03"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. Baselines are iteration 0 and CoT-SC (5 "
                             "paths); the Gödel Agent baseline never yields an accuracy comparison. There is no "
                             "abstraction-off ablation, and evolved policies add responses and experts unmatched by "
                             "CoT-SC.", ["son55:E009", "son55:E010", "son55:E021", "son55:E022", "son55:E026", "sol:E006"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Separate validation/test splits exist, so not 0. "
                           "But runs are labelled successful on test (opus:O02), the headline is the max over those "
                           "runs, and with no performance gate the best-so-far iteration is chosen on test as well "
                           "(opus:O01). No independent final test after selection.",
                           ["son55:E005", "son55:E015", "son55:E018", "son55:E019", "son55:E020", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder): ten runs per cell with failure counts in the "
                              "denominator, and bootstrap CIs for two datasets. No all-run mean, variance or test.",
                              ["son55:E008", "son55:E011", "son55:E012", "son55:E016", "sol:E005", "sol:E007"]),
            "E.cost": R("resolved", 1, "Opus sides with son55. Hardware and the 10-hour budget per run are stated "
                        "(evolution budget as a design parameter), but there are no tokens and no per-query "
                        "inference cost of evolved multi-response policies against CoT-SC, the headline comparison "
                        "(A2; r09/r10 'hardware + budget' precedent = 1).",
                        ["son55:E021", "son55:E022", "son55:E023", "son55:E024", "sol:E006", "sol:E013"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 HTML text, including Appendices A–B, read. Per-iteration curves are image-only "
                  "and not used numerically. In scope (system_method): policy code is patched from execution "
                  "feedback and persists to later test items. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 3–6 and 13–17 (accuracy per repair iteration, variance) are image-only. "
                             "Absolute accuracies are not in the text, so only the authors' relative improvements "
                             "and the Tables 1–4 run counts are used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "See assessment.evidence_level_note: the test set labels runs and supplies best-so-far, and nothing "
                "selects on validation. sol's 'retained' credits the val/test split without the selection that "
                "happens on test.", ["opus:O01", "opus:O02", "son55:E018"], NOLVL),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", None,
                "See rs_pattern.reason: the guarantee-relaxation card is not executed by an engineering context "
                "reduction.", ["son55:E002"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [],
                "outside_taxonomy=true (primary null, no matches); son55's low-fit match is not kept.",
                ["son55:E002"], NOSCORE),
            XC(p, "local:2603.23129-1", "revised", "partial",
               "A4 collision: sol local-1 (holdout/champion selection) and son55 local-1 (expected gain over all "
               "runs) are different questions. Final local-1 = son55's question. sol's local-3 (statistics) is "
               "merged here, and sol's local-1 is moved to H12-step4. Status partial: all-run denominators are "
               "reported, but no gain estimate or variance over them.", ["son55:E011", "son55:E012", "sol:E005"]),
            XC(p, "local:2603.23129-2", "son55", "unmet",
               "A4 collision: final local-2 = son55's cost-matched baseline question; sol's local-4 (cost) is "
               "merged here and sol's local-2 (ablation) moved to local-3. Verified unmet.",
               ["son55:E021", "son55:E022", "sol:E006"]),
            XC(p, "local:2603.23129-3", "son55", "unmet",
               "A4 collision: final local-3 = son55's abstraction-off question; sol's local-2 is the same question "
               "(merged), and sol's local-3 moved to local-1. Verified unmet.", ["son55:E026", "sol:E001"]),
            XC(p, "local:2603.23129-4", "revised", {"moved_to": "local:2603.23129-2", "status": "unmet"},
               "sol's cost question merged into local-2. sol's partial credited the wall-clock budget, which does "
               "not answer per-query cost.", ["sol:E006", "sol:E013"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-1", "son55", "not_applicable",
               "Check question only (card not retained). Verified: no guarantee is claimed.", ["son55:E002"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-2", "son55", "partial",
               "Check question only. Verified: the weaker condition holds in ~43–45% of runs and is not "
               "characterised.", ["son55:E011", "son55:E012"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-4", "son55", "partial",
               "Check question only. Verified: DGM contrasted in text only; other small-model loops absent.",
               ["son55:E027"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-6", "son55", "met",
               "Check question only. Verified: Table 1 characterises the trimmed Gödel Agent failures before the "
               "Polaris results.", ["son55:E013", "son55:E014"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12", "sol", "partial",
               "Verified whole-card check: trace/source, local patches and reuse are present; promotion and "
               "rollback are not.", ["sol:E003", "sol:E010", "sol:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/H12-step4", "son55", "unmet",
               "Verified. sol's local-1 (same holdout question) merged here.", ["son55:E005", "son55:E018", "opus:O01"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: patches are minimal, but attribution to a code component is unchecked LLM reflection.",
               ["son55:E026", "son55:E028"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S2", "revised",
               {"moved_to": "rsi:attribute_and_patch_incumbent/S4", "status": "partial"},
               "Card S2 is 'evaluation budget is steered, not spread'. sol's S2 entry (abstracting many failures "
               "into 1–2 general strategies) answers S4 ('mechanisms are diagnosed, not instances'). It is merged "
               "into S4 with status partial, since there is no clustering and N=3/5. The true S2 question is not "
               "assessed by either seat. Opus reading: Polaris does not steer evaluation (no selection among "
               "candidates).", ["sol:E002", "son55:E026"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "Verified: no regression check, no rollback, no performance-based acceptance.", ["son55:E003", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "partial",
               "Verified. sol's mis-numbered S2 merged here; sol's 'met' overlooks the missing clustering.",
               ["son55:E026"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: one-framework resource residue, with non-Gödel small-model neighbours unpositioned.",
                ["son55:E027", "son55:E013"], "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: no prediction separating abstraction from mere context reduction.",
                ["son55:E026", "sol:E002"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 3,
                "See ratings.E.measurement: per A2, son55's grounds belong to E.holdout and E.statistics, where they "
                "are charged. The verifiers are reference-based.", ["sol:E004", "son55:E016"], "+2.5 vs son55 (10×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 1,
                "See ratings.E.holdout: test-defined success labels and test-read best-so-far. sol's 2 credits the "
                "split as if selection happened elsewhere.", ["opus:O01", "opus:O02"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 1,
                "See ratings.E.cost: wall-clock and hardware only; the headline comparison is not cost-matched.",
                ["son55:E021", "sol:E006"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "3 (threshold not checked)",
             "son55_value": "2 (threshold not checked)", "final_value": 3,
             "reason": "Neither seat checked the run-category threshold. '≤2 additional correctly solved samples "
                       "(≤0.8%)' is right for the 250-item tests, but on GPQA's 100-item test it is 2%, so "
                       "'No improvement' vs 'Successful' is drawn at different resolutions across datasets. Recorded "
                       "in E.measurement; no rating change.",
             "evidence_ids": ["opus:O03"], "score_impact": "none"},
            {"field_path": "assessment.claim_support", "sol_value": "scoped", "son55_value": "scoped",
             "final_value": "scoped",
             "reason": "Both seats scoped the claim, but neither flagged the conclusion's 'without supervision', "
                       "which contradicts failure analysis on reference answers (opus:O04). The narrow conclusion "
                       "must not repeat it.", "evidence_ids": ["opus:O04", "son55:E028"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v4 text first. Initial view: in scope; runs "
                                                   "labelled on test; headline = max relative gain over successful "
                                                   "runs; no performance gate; no abstraction ablation. G 2–3, M 2, "
                                                   "X 2, Em 2–3, Ec 1, Eh 1, Es 2, E.cost 1; evidence_level task.",
            "integrity_checks": "Both seats a1 hash-equal to conflicts.json; 2603.23129v4, material sha ac17895c…; "
                                "RS/domain IDs valid; both system_method.",
            "core_claim_check": "Strongest supported claim: with Qwen2.5-7B, the repair loop yields a policy that "
                                "beats its base policy on test in 17–18 of 40 runs (success labelled on test, best-"
                                "so-far); the trimmed Gödel Agent almost never completes. 'Consistent gains' and "
                                "'without supervision' are not supported. claim_support scoped.",
            "rating_agreement": "X, Ec, Es agree and were re-checked; G, M, Eh, E.cost → son55; Em → sol. Final 45.0.",
        },
    }

    # =========================================================== 2603.23420 Bilevel Autoresearch (Δ15)
    p = "2603.23420"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "The LLM, given the same state, generates nearly the same proposals every time.",
                    "§4.3, Group A",
                    "The baseline proposer is near-deterministic. The obvious naive fix (temperature/seed "
                    "diversity, restarts or a hand-coded tabu list) is never run, although Level 2's winning "
                    "mechanisms are exactly such diversifiers.", kind="our_inference"),
            opus_ev(p, "O02", "However, the per-repeat reports show that Group D’s generated mechanism patches were "
                              "not successfully applied or validated", "§4.3, Group D",
                    "Two of three Group D repeats reach −0.063/−0.039 with no applied mechanism, so the decisive "
                    "batch-size move occurs without successful injection."),
            opus_ev(p, "O03", "Baseline val_bpb varies slightly across repeats due to training randomness (range "
                              "1.094–1.114).", "Table 2 caption",
                    "The 0.02 baseline spread exceeds Groups A/B's gains (0.006–0.009); a single 300-s evaluation's "
                    "noise floor is never measured."),
            opus_ev(p, "O04", "We are not aware of earlier autoresearch systems in which an autonomous outer loop "
                              "writes and injects code that modifies the structural logic of the inner "
                              "autoresearch loop at runtime", "§2.6",
                    "The novelty claim is scoped to 'autoresearch systems'. Self-referential improvers that edit "
                    "their own improvement code (Gödel Agent, DGM, ADAS) do not appear in §2.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: generative_process_redesign, sub null. The fixed search/update mechanism of an "
                      "iterative procedure becomes a free design variable; C15/C23/C24 concern 3D/diffusion/"
                      "conditioning and do not apply.",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H19")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2603.23420-1"): "rsi:make_the_improver_editable/F4",
                    ("sol", "local:2603.23420-2"): "local:2603.23420-3",
                    ("sol", "rsi:make_the_improver_editable/S4"): "rsi:make_the_improver_editable/F3"},
            order=("son55", "sol"),
            overrides={
                "local:2603.23420-3": {
                    "status": "met",
                    "reason": "Opus (verified, sol's scope question): v2 claims only the first bilevel step and "
                              "states that recursive self-application is not established (§5.3, §5.4).",
                    "renumbered_from": "sol:local:2603.23420-2"},
                "rs:generative_process_redesign/RE-6": {
                    "status": "partial",
                    "reason": "Opus (revised from met): failure cases (C R2, D R1, the GP revert, the invalidated "
                              "preliminary run) are analysed, but only one operating point (300 s, 30 iterations, "
                              "one GPU, one model) is reported; no regime is characterised."},
                "rsi:make_the_improver_editable/F3": {
                    "status": "unmet",
                    "reason": "Failure mode present: val_bpb is both the keep/discard criterion and the reported "
                              "metric, on one benchmark.",
                    **moved("sol:rsi:make_the_improver_editable/S4")},
                "rsi:make_the_improver_editable/F4": {
                    "status": "unmet",
                    "reason": "Failure mode present: n=3, Group C SD = 67% of mean, baseline spread (0.02) larger "
                              "than Groups A/B's gains (opus:O03).",
                    **moved("sol:local:2603.23420-1")},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O02", "opus:O03"]), "C3", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: no naive diversification baseline for a near-deterministic proposer (opus:O01)."],
            evidence_level="task",
            evidence_level_note="The edited object is the inner improver, and C vs A/B compares mechanism-on with "
                                "mechanism-off at equal inner evaluations. But selection and report share val_bpb "
                                "(EVIDENCE rule 2), and Group D's gains without applied mechanisms leave the "
                                "improved mechanism's causal role open, so not 'improver' or 'retained'."),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The residue is evidenced (Group A repeats the same two "
                   "proposals for iterations 4–30), but the closest lineage (self-referential agents that edit "
                   "their own improvement code: Gödel Agent, DGM, ADAS) is absent, and novelty is scoped to "
                   "'autoresearch systems' (opus:O04). Anchor 2: neighbour comparison incomplete.",
                   ["son55:E003", "son55:E012", "son55:E022", "son55:E027", "sol:E001", "opus:O04"]),
            "M": R("resolved", 2, "Opus sides with son55. The two-level design and the stated hypotheses (L1.5 vs "
                   "L2) are reconstructible. But the diagnosed bottleneck is a proposer that 'generates nearly the "
                   "same proposals every time' (opus:O01), and the winning generated mechanisms are standard "
                   "diversifiers. No prediction separates LLM-generated mechanisms from directly diversifying the "
                   "proposer, and L1.5, the only stated contrast, is a freeze rule that the paper shows blocks the "
                   "decisive direction.", ["son55:E002", "son55:E006", "son55:E013", "sol:E002", "sol:E003", "opus:O01"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1, periods and the 4-call dialogue are "
                   "reproducible. Retention is import-validated only (no performance gate or retirement), the "
                   "anchor is unnamed, Group D patches failed to apply, and a silent-fallback bug invalidated a "
                   "preliminary run.", ["son55:E004", "son55:E006", "son55:E019", "son55:E024", "sol:E003", "sol:E015"]),
            "E.measurement": R("resolved", 3, "Opus sides with sol. val_bpb on a fixed validation split is a "
                               "credible metric for this task, and absolute Δ values are reported per repeat. son55's "
                               "two grounds, small gains below the baseline spread and the metric doubling as "
                               "selection criterion, are a noise defect (E.statistics) and a selection defect "
                               "(E.holdout), charged there (A2). Not 4: the '5×' is a ratio of improvement "
                               "magnitudes, and the per-evaluation noise floor is unmeasured (opus:O03).",
                               ["sol:E004", "sol:E006", "sol:E009", "son55:E005", "opus:O03"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. The four-group level ablation holds model, "
                             "GPU, training budget and inner evaluations fixed, and C separates from A/B. But Group "
                             "D reaches the same batch-size move without applied mechanisms (opus:O02), individual "
                             "mechanisms are not ablated, no naive diversification baseline exists (opus:O01), and "
                             "outer LLM calls are unmatched (A2).",
                             ["son55:E009", "son55:E010", "son55:E011", "son55:E013", "sol:E004", "opus:O01", "opus:O02"],
                             ["son55:E010"]),
            "E.holdout": R("resolved", 0, "Both seats 0 (sol resolved, son55 not_reported; Opus keeps resolved, "
                           "since the zero rests on reported design facts). The keep/discard metric is the reported "
                           "metric, best configurations are not re-evaluated, there is one task/GPU/LLM, and mechanism "
                           "transfer is future work.", ["sol:E013", "sol:E014", "son55:E005", "son55:E016"],
                           scope=["Methods 3.2–3.6", "Algorithm 1", "Results 4.1–4.4", "Discussion 5.1–5.5"]),
            "E.statistics": R("resolved", 2, "Opus sides with sol (A2 ladder). Three repeats per group with per-repeat "
                              "values and mean±SD give cross-run variance, beyond the ladder-2 description; no "
                              "interval or test, n=3 that the authors call insufficient, and an uncontrolled "
                              "baseline spread (opus:O03) keep it below 3. son55's 1 fits 'main result without "
                              "uncertainty', but the SD is reported.",
                              ["sol:E005", "sol:E006", "sol:E012", "son55:E007", "son55:E008", "son55:E015", "opus:O03"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Outer overhead per session is quantified (≈3 min, "
                        "4 LLM calls), and inner evaluations are matched with the non-parity stated. No total "
                        "tokens or wall-clock per group.", ["sol:E004", "sol:E011", "son55:E017", "son55:E018"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text read (no appendix). In scope (system_method): an outer loop edits "
                  "the inner loop's non-weight search mechanism from its trace, and the change persists for the "
                  "rest of the run. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "The Figure 4 running-minimum curves are image-only; all numbers come from Tables 2–3 "
                             "and the text.",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["make_the_improver_editable", "H19"]],
                "H19 (outer tuning of the inner improver, scored by its products) is the specific card. son55's H12 "
                "(low fit) describes the same code-reading patch step on harness code; with the improver itself as "
                "the edited object, H12 adds nothing but unmet checks.", ["sol:E002", "son55:E002"], NOSCORE),
            XC(p, "local:2603.23420-1", "son55", "unmet",
               "A4 collision: sol local-1 (statistics) vs son55 local-1 (no plain diversified-search control for "
               "the batch-size discovery). Final local-1 = son55's question, verified unmet (opus:O01). sol's "
               "statistics question merged into F4.", ["son55:E011", "son55:E012", "opus:O01"]),
            XC(p, "local:2603.23420-2", "son55", "unmet",
               "A4 collision: sol local-2 (scope of the recursion claim) vs son55 local-2 (Group D cannot "
               "attribute gains to injection). Final local-2 = son55's question, verified unmet (opus:O02). sol's "
               "question renumbered local-3 (met).", ["son55:E010", "opus:O02"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "unmet",
               "Verified: no alternative search procedure (restart, temperature/seed diversity, hand-coded tabu or "
               "bandit, population search).", ["son55:E007", "opus:O01"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", "partial",
               "Verified: level-wise ablation exists; the individual mechanisms are not ablated.",
               ["son55:E009", "son55:E014"]),
            XC(p, "rs:generative_process_redesign/RE-6", "revised", "partial",
               "son55 wrote met. RE-6 asks for the trade-off across the operating regime and for failure analysis. "
               "The failures are analysed, but only one operating point is reported.", ["son55:E014", "son55:E019", "sol:E014"]),
            XC(p, "rsi:make_the_improver_editable/F3", "son55", "unmet",
               "Verified. sol's mis-numbered S4 (card S4 is 'search cost on the table'; sol's content is benchmark "
               "reuse) merged here.", ["son55:E005", "son55:E016", "sol:E013"]),
            XC(p, "rsi:make_the_improver_editable/F4", "son55", "unmet",
               "Verified. sol's local-1 (same noise/statistics question, 'partial') merged here. As a failure-mode "
               "check, F4 is present, so unmet.", ["son55:E008", "son55:E015", "opus:O03"]),
            XC(p, "rsi:make_the_improver_editable/H19", "sol", "partial",
               "Verified whole-card check: the runner really changes and partly activates, with backup; there is no "
               "utility gate and no cross-task certification.", ["sol:E003", "sol:E007", "sol:E014"]),
            XC(p, "rsi:make_the_improver_editable/S1", "son55", "partial",
               "Verified: the anchor is not named, and Level 2 may patch runner.py, potentially including "
               "acceptance logic.", ["son55:E004", "son55:E006"]),
            XC(p, "rsi:make_the_improver_editable/S2", "son55", "met",
               "Verified: the improver is scored by inner-run val_bpb.", ["son55:E005", "son55:E009"]),
            XC(p, "rsi:make_the_improver_editable/S3", "son55", "partial",
               "Verified: compared with the unmodified loop and parameter-only adjustment at n=3; no stronger fixed "
               "improver.", ["son55:E009", "son55:E015"]),
            XC(p, "rsi:make_the_improver_editable/S4", "revised",
               {"moved_to": "rsi:make_the_improver_editable/F3", "status": "unmet"},
               "sol's S4 content (same val for keep/search/report; no frozen-improver test on a new task) is F3, "
               "'benchmark reuse passes for self-improvement'. Merged. The true S4 (search cost on the table) is "
               "covered by son55's H19 condition check (partial) and E.cost.", ["sol:E013", "sol:E014"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", 2,
                "See ratings.G: the self-referential improver lineage is missing.", ["son55:E027", "opus:O04"],
                "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M: no prediction separates generated mechanisms from naive diversification of a near-"
                "deterministic proposer.", ["opus:O01", "son55:E013"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", 3,
                "See ratings.E.measurement: A2 routes son55's noise and selection grounds to E.statistics and "
                "E.holdout.", ["sol:E004", "opus:O03"], "+5.0 vs son55 (10×2/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 0},
                "Same rating 0. Status resolved: the zero rests on reported design facts, not on an absence found "
                "by search. son55's search scope is kept in the final item.", ["sol:E013", "son55:E005"], "none"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 2,
                "See ratings.E.statistics: cross-run SD is reported, which places it at the A2 ladder's 2.",
                ["sol:E006", "son55:E008"], "+1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first. Initial view: in scope; n=3 per "
                                                   "group; best-of-30 on the acceptance metric; Group D gains "
                                                   "without applied patches; no naive diversification baseline; "
                                                   "Gödel/DGM/ADAS lineage absent. G 2, M 2–3, X 2, Em 2–3, Ec 1–2, "
                                                   "Eh 0, Es 2, E.cost 2; evidence_level task.",
            "integrity_checks": "Both seats a1 hash-equal to conflicts.json; 2603.23420v2, material sha d4467e53…; "
                                "son55 E027 is a null-quote negative fact (allowed); IDs valid.",
            "core_claim_check": "Strongest supported claim: on one 50M pretraining benchmark (RTX 5090, DeepSeek), "
                                "runs with Level 2 sessions found the batch-size reduction in 4 of 6 repeats vs 0 of "
                                "6 without, yielding larger best-of-30 val_bpb gains. Causation by injected "
                                "mechanisms is not established (Group D). claim_support scoped.",
            "rating_agreement": "X, Ec, E.cost agree (re-checked); Eh same rating; G, M → son55; Em, Es → sol. "
                                "Final 47.5.",
        },
    }

    # =========================================================== 2603.24639 ERL (Δ2.5)
    p = "2603.24639"
    S[p] = {
        "base": "son55",
        "seat_binding_issue": BIND_24639,
        "opus_evidence": [
            opus_ev(p, "O01", "with a 56.1% success rate", "Appendix C.2, LLM retrieval",
                    "The headline 56.1 is the k=20 cell of the Table 3 sweep (k ∈ {1,3,5,10,20}, and an embedding "
                    "sweep), which runs under the general configuration, i.e. on the test universes. k and the "
                    "retriever are thus selected on test.", kind="our_inference"),
            opus_ev(p, "O02", "Success rates on the Gaia2 test universes (3 runs).", "Figure 2 caption",
                    "Main table and ablations are reported on the two test universes."),
            opus_ev(p, "O03", "We sample a subset of training tasks matching the test set distribution (48 "
                              "execution, 28 search).", "Appendix B, ExpeL implementation",
                    "ExpeL builds from 76 source tasks (with retries), while ERL uses all 244. Experience budgets "
                    "are unmatched."),
            opus_ev(p, "O04", "and the best random selection configuration (53.8%)", "§3, Retrieval quality",
                    "Random heuristics already give +5.5 of the +7.8 gain, and 'best random' is itself the best "
                    "cell of a sweep on test."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning. Sub null, following sol: C03 needs a phase that teaches "
                      "the model to read a canonical schema and a category-level holdout. The agent is frozen, the "
                      "format is taught by prompt, and test universes share task types and tools (r13b/r04b "
                      "convention).",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol"),
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [], "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "rsi:abstract_experience_into_guidance/step2"): "rsi:abstract_experience_into_guidance/S2",
                    ("sol", "local:2603.24639-1"): "local:2603.24639-4",
                    ("son55", "rsi:abstract_experience_into_guidance/variance"): "local:2603.24639-4",
                    ("sol", "local:2603.24639-2"): "local:2603.24639-6",
                    ("son55", "rsi:abstract_experience_into_guidance/reflector-cost"): "local:2603.24639-5",
                    ("son55", "rsi:abstract_experience_into_guidance/budget-matched"):
                        "rsi:abstract_experience_into_guidance/H00-step5"},
            order=("son55", "sol"),
            overrides={
                "local:2603.24639-1": {
                    "status": "unmet",
                    "reason": "Opus (verified): the k sweep and retriever comparison run on the test universes, and "
                              "the headline is the best cell (opus:O01); the retrieval prompt was hand-selected."},
                "local:2603.24639-4": {
                    "status": "partial", "source_strength": "common_practice",
                    "applies_when": "An accumulating store is evaluated over repeated runs",
                    "reason": "Opus: three runs with pass@3/pass^3 counts and several negative results; no "
                              "intervals, a single accumulation ordering, and a single pool.",
                    **moved("son55:rsi:abstract_experience_into_guidance/variance; sol:local:2603.24639-1")},
                "local:2603.24639-5": {
                    "status": "met", "source_strength": "common_practice",
                    "applies_when": "Reflection and retrieval add model calls",
                    "reason": "Opus (verified): Appendix D itemises heuristic generation ($2.42) and retrieval "
                              "($1.38) tokens and cost.",
                    **moved("son55:rsi:abstract_experience_into_guidance/reflector-cost")},
                "local:2603.24639-6": {
                    "status": "partial",
                    "reason": "Opus (verified, sol's lifecycle-cost question): per-phase API cost is reported, "
                              "latency is not measured, and the GPT-5.2 ranker is stronger than the agent.",
                    "renumbered_from": "sol:local:2603.24639-2 (hidden A4 collision with son55 local-2)"},
                "rsi:abstract_experience_into_guidance/S2": {
                    "status": "unmet",
                    "reason": "Opus: heuristics come from single trajectories with no paired contrast. The paper "
                              "challenges the need for contrast, but its evidence (beating ExpeL/AutoGuide) is "
                              "confounded by unmatched source budgets (opus:O03) and a stronger ranker, so the "
                              "challenge is not established.",
                    **moved("sol:rsi:abstract_experience_into_guidance/step2")},
                "rsi:abstract_experience_into_guidance/H00-step5": {
                    "status": "unmet",
                    "reason": "Opus (verified): the store-off control is present, but there is no budget match "
                              "with ExpeL/AutoGuide (76-task subset with retries vs 244 single attempts).",
                    **moved("son55:rsi:abstract_experience_into_guidance/budget-matched")},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O03"]), "C4", ["opus:O04"]),
        "assessment": assess("son55", p, [
            "Opus: k and retriever selected on the test universes (opus:O01)."],
            evidence_level="retained",
            evidence_level_note="A pool frozen after accumulation on 8 universes is read on 2 disjoint universes, "
                                "with a store-off (ReAct) control. Test-tuned k/retriever is charged in E.holdout, "
                                "not by lowering the level (SWE-Exp precedent)."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A concrete deployment gap relative to ExpeL and "
                   "AutoGuide (retries, paired trajectories, all-insight prompts, per-turn retrieval). The overhead "
                   "claims are argued, and other experiential-memory systems are only cited.",
                   ["son55:E002", "son55:E030", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Single-attempt post-mortem → trigger/action guideline "
                   "→ LLM relevance retrieval, tested against distinguishable naive alternatives (raw trajectories, "
                   "random, embedding).", ["son55:E003", "son55:E004", "son55:E016", "son55:E009", "sol:E002"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Formats, prompts, k and injection are reproducible. "
                   "There is no admission gate, maintenance, conflict handling or versioning, and the online variant "
                   "degrades.", ["son55:E003", "son55:E004", "son55:E023", "son55:E024", "son55:E025", "sol:E017", "sol:E018"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Gaia2 ground-truth trajectories with "
                               "automatic verification, plus pass@3/pass^3. The ARE judge shares the agent's model "
                               "and is not audited.", ["son55:E005", "son55:E018", "son55:E027", "sol:E014"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Store-off, random, embedding, token-matched "
                             "raw trajectories and source-kind controls are present. But ExpeL/AutoGuide experience "
                             "budgets are unmatched (opus:O03), the GPT-5.2 ranker is stronger than the baselines' "
                             "retrievers, random heuristics give most of the gain (opus:O04), and failures-only "
                             "exceeds the headline.",
                             ["son55:E009", "son55:E010", "son55:E011", "son55:E012", "son55:E015", "son55:E019",
                              "sol:E012", "opus:O03", "opus:O04"]),
            "E.holdout": R("resolved", 2, "Opus sides with sol. Accumulation and test use disjoint universes and "
                           "τ²-bench train/test, which is real hold-out of the store content. But k and the retriever "
                           "are chosen from sweeps on the test universes (headline = best cell, opus:O01), the "
                           "retrieval prompt was hand-selected, and there are only two test universes. son55's 3 "
                           "names the test tuning but does not charge it; its own local-1 is 'unmet'.",
                           ["son55:E005", "son55:E006", "son55:E013", "son55:E026", "son55:E029", "sol:E004",
                            "sol:E009", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Opus sides with sol (A2 ladder): pass^3/pass@3 over three runs are "
                              "repeated-run failure counts, and sample sizes and negative results are reported. "
                              "There are no intervals or tests, and margins between variants are about 2 points on "
                              "76 tasks.", ["son55:E028", "son55:E018", "son55:E022", "son55:E024", "sol:E007", "sol:E017"]),
            "E.cost": R("resolved", 3, "Opus sides with son55. Appendix D gives per-phase input/output tokens, "
                        "cache share and dollars for baseline vs ERL (+40% overall), and C.1 adds a token-matched "
                        "few-shot comparison, which is real budget-fairness evidence against the cheapest "
                        "alternative. Source-trajectory rollouts are not an extra cost under the paper's deployment "
                        "framing, since tasks are run anyway. Not 4: retry-based baselines are not costed or budget-"
                        "matched, and latency is unmeasured.",
                        ["son55:E020", "son55:E017", "sol:E015", "sol:E016", "sol:E019"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML text, including Appendices A–G, read. In scope (system_method): "
                  "heuristics written from execution outcomes are retained and read on later disjoint tasks. All "
                  "eight items resolved. aggregate_status needs_revision only because the sol seat binding in "
                  "conflicts.json is stale (see seat_binding_issue).",
        "aggregate_status": "needs_revision",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "The Figure 2 table is transcribed in the text and used. Figure 3 pass values are used "
                             "only as stated in the text (+8.3/+10.6). Figures 4–5 curves are image-only; only "
                             "text-stated numbers (53.8, +5.5, +23.8) are used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "See rs_pattern.reason: C03's reader-training and category-holdout conditions are absent (frozen "
                "agent, same task types/tools); son55 itself marks step 3 'not applicable'.", ["son55:E006"], NOSCORE),
            XC(p, "local:2603.24639-1", "son55", "unmet",
               "A4 collision: sol local-1 (statistics) vs son55 local-1 (k/retriever tuned on test). Final local-1 "
               "= son55's question, verified unmet (opus:O01). sol's local-1 renumbered to local-4 and merged with "
               "son55's 'variance'.", ["son55:E013", "son55:E029", "opus:O01"]),
            XC(p, "local:2603.24639-3", "son55", "unmet",
               "Verified: the iterative (online) ERL reaches 50.7 vs 56.1 on test.", ["son55:E024"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "RE-1 asks for an ablation isolating the conditioning signal. The ReAct store-off and random-"
               "heuristic arms do that. sol's 'partial' rests on unmatched ExpeL/AutoGuide budgets, which bear on "
               "RE-3/H00-step5, not RE-1.", ["son55:E008", "son55:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "same_supported_fact", "partial",
               "conflicts.json shows sol null (pre-final draft); the final sol file also says partial (τ²-bench "
               "Telecom degrades; prompt hand-selected). Same finding.", ["son55:E021", "son55:E022", "sol:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "same_supported_fact", "partial",
               "conflicts.json shows sol null (pre-final draft); the final sol file also says partial. Verified: "
               "no-reward and random-k sensitivity are reported; pool coverage and distribution gap are not.",
               ["son55:E023", "sol:E014"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "sol", "partial",
               "Field present only in the fresh diff (final sol file). Verified: generation, retrieval and source-"
               "kind components are ablated, but ranker strength and actor are not crossed with them.",
               ["sol:E006", "sol:E012", "son55:E009"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00", "sol", "partial",
               "Verified whole-card check: retained guidance helps new data; there is no conflict or staleness "
               "governance.", ["sol:E003", "sol:E004", "son55:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "unmet",
               "conflicts.json lists sol's draft ID S2 (challenged_with_evidence); the final sol file names it "
               "step2. The paper's challenge to contrastive extraction rests on unmatched comparisons "
               "(opus:O03), so the challenge is not established by evidence; unmet.",
               ["son55:E003", "son55:E030", "opus:O03"]),
            XC(p, "rsi:abstract_experience_into_guidance/step2", "revised",
               {"moved_to": "rsi:abstract_experience_into_guidance/S2", "status": "unmet"},
               "Fresh-diff field (final sol ID). step2 is not an A4 grammar ID; H00 step 2 and card S2 are the same "
               "'contrast, not narration' question. Merged into S2 and ruled with it.", ["sol:E001", "sol:E020"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: environment validation reward, with the self-assessed-signal variant measured (70% "
               "accuracy → 51.2%).", ["son55:E003", "son55:E023"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Verified: no consolidation, forgetting or conflict resolution (future work).", ["son55:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Verified: every reflection is stored; no gate.", ["son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/budget-matched", "revised",
               {"moved_to": "rsi:abstract_experience_into_guidance/H00-step5", "status": "unmet"},
               "Non-grammar ID (A4). The question is H00 step 5 ('budget-match and ablate'). Status unmet "
               "verified (opus:O03).", ["son55:E010", "son55:E012", "opus:O03"]),
            XC(p, "rsi:abstract_experience_into_guidance/reflector-cost", "revised",
               {"moved_to": "local:2603.24639-5", "status": "met"},
               "Non-grammar ID (A4: the card's pending reviewer expectations carry no S/F/H ID), so it becomes "
               "local-5. Met verified.", ["son55:E020"]),
            XC(p, "rsi:abstract_experience_into_guidance/variance", "revised",
               {"moved_to": "local:2603.24639-4", "status": "partial"},
               "Non-grammar ID (A4), so it becomes local-4, merged with sol's statistics question (sol local-1). "
               "Partial verified.", ["son55:E028", "sol:E007"]),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", 2,
                "See ratings.E.holdout: universe hold-out of the store is real; test-tuned k/retriever caps it at "
                "2.", ["opus:O01", "son55:E013"], "−2.5 vs son55 (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", 2,
                "See ratings.E.statistics: pass^3/pass@3 are repeated-run failure counts (A2 ladder 2).",
                ["son55:E018", "sol:E007"], "+1.25 vs son55 (5×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", 3,
                "See ratings.E.cost: full per-phase cost plus a token-matched control. sol's missing-source-rollout "
                "objection does not apply under the deployment framing.", ["son55:E020", "son55:E017"],
                "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2603.24639-2].id", "sol_value": "local:2603.24639-2 (lifecycle cost)",
             "son55_value": "local:2603.24639-2 (retrieval vs random)", "final_value": "sol's → local:2603.24639-6",
             "reason": "Hidden A4 collision not flagged by conflicts.json (both 'partial'): the same ID covers two "
                       "different questions. son55's keeps local-2; sol's is renumbered local-6.",
             "evidence_ids": ["sol:E015", "son55:E015"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v2 text first. Initial view: in scope; frozen "
                                                   "pool on disjoint universes with store-off, so retained; k and "
                                                   "retriever tuned on test; ExpeL budget unmatched; detailed cost "
                                                   "table. G 2–3, M 2–3, X 2, Em 3, Ec 2, Eh 2, Es 1–2, E.cost 2–3.",
            "integrity_checks": "son55 a1 hash-equal to conflicts.json. sol a1 does NOT match: conflicts.json was "
                                "computed from a pre-final sol draft, and the bound version is unrecoverable "
                                "(seat_binding_issue). Built on the final sol file, with resolutions over "
                                "conflicts.json ∪ fresh diff. Both seats on 2603.24639v2, material sha 4e1c9188…; "
                                "IDs valid after A4 renames.",
            "core_claim_check": "Strongest supported claim: a heuristic pool from single attempts on 8 Gaia2 "
                                "universes raises success on 2 held-out universes by ~8 pts over ReAct (GPT-5-mini, "
                                "76 tasks, 3 runs), with k/retriever tuned on those universes; the gain over "
                                "ExpeL/AutoGuide is not budget-matched, and the online variant and τ²-bench do not "
                                "reproduce it. claim_support scoped.",
            "rating_agreement": "G, M, X, Em, Ec agree (re-checked); Eh, Es → sol; E.cost → son55. Final 62.5 "
                                "(provisional until re-bound).",
        },
    }
    return S
