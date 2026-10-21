"""Opus rulings for r05a a1 (data only; consumed by _build.py)."""
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

    def rsp(s, p, **upd):
        r = prefix(copy.deepcopy(seat(s, p)["rs_pattern"]), s)
        r.update(upd)
        return r

    def exp_of(s, p, eid):
        for e in seat(s, p)["expectations"]:
            if e["id"] == eid:
                return e
        raise KeyError((s, p, eid))

    def take(s, p, eid, **extra):
        """Override payload that makes the merged entry carry seat s's status/reason/evidence."""
        e = exp_of(s, p, eid)
        d = {"status": e.get("status"), "reason": e.get("reason"),
             "evidence_ids": prefix({"evidence_ids": e.get("evidence_ids", [])}, s)["evidence_ids"]}
        d.update(extra)
        return d

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev,
                   "none (expectations are not scored directly)")

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    NOSCORE = "none (patterns never score)"

    def rr(p, k, dec, rating, reason, ev, impact):
        return res(f"ratings.{k}", *C(p, f"ratings.{k}"), dec, {"status": "resolved", "rating": rating}, reason, ev, impact)

    # =========================================================== 2505.18524 metaTextGrad (Δ10)
    p = "2505.18524"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "GPT-4o for the MIPROv2 and TGD optimizers, and the o1 model for the structure optimizer and the "
                    "meta-optimizers", "§4.1 Experimental Setup",
                    "Model allocation: the structure-search baseline ADAS-TG (the paper's 'structure optimizer') already runs on "
                    "o1; only TGD/MIPROv2 run on GPT-4o. The o1-vs-GPT-4o confound therefore applies to the TGD comparison, not "
                    "to ADAS-TG vs ADAS-TG(O)."),
            opus_ev(p, "O02", "ADAS is an algorithm for automatically searching and optimizing the program", "§4.1 Baselines",
                    "Identifies ADAS-TG as the structure-searching optimizer referred to in opus:O01."),
            opus_ev(p, "O03", "First, we analyze the token usage at different levels within a single epoch of meta optimization.",
                    "§4.3 Cost analysis",
                    "The only optimization-cost figure is per single epoch on one dataset (Abstract Algebra)."),
            opus_ev(p, "O04", "Max Meta-Iterations", "Algorithm 2 input line",
                    "J (meta-iterations) and I (inner iterations) appear only as symbols; neither is instantiated anywhere in "
                    "§4, Appendix C or the checklist, so the total search cost cannot be reconstructed (searched: 'epoch', "
                    "'iteration', 'J', 'budget')."),
        ],
        "rs_pattern": rsp("son55", p, reason=(
            "Both seats: generative_process_redesign, no sub-card. Kept: the conventionally fixed component of the iterative "
            "prompt/program optimization procedure (the hand-written, task-agnostic optimizer prompt and composition) is "
            "treated as a free design variable and redesigned per task. C15/C23/C24 are 3D-representation / diffusion-chain / "
            "conditioning-interface sub-patterns and do not fit, so sub_id stays null.")),
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "make_the_improver_editable", "H19")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son, rename={},
            overrides={
                "rsi:make_the_improver_editable/S3": take("son55", p, "rsi:make_the_improver_editable/S3"),
                "rsi:make_the_improver_editable/S5": {
                    "applicable": False, "status": "not_applicable",
                    "reason": "Opus final: H19 is single-lineage by definition (greedy σ>σ* replacement); archive tolerance of "
                              "non-improving steps is the H20 condition. son55 already marked applicable=false; status aligned."},
                "rsi:make_the_improver_editable/F5": {
                    "status": "partial",
                    "reason": "Opus final: anchor leak only on the TGD side (o1 meta-optimizer rewrites a GPT-4o optimizer). "
                              "ADAS-TG baseline and ADAS-TG(O) both run on o1 (opus:O01, opus:O02), so that comparison holds "
                              "the optimizer model fixed; the meta prompt additionally sees training Q/A examples, which is "
                              "the method itself, not a leak.",
                    "evidence_ids": ["son55:E005", "opus:O01", "opus:O02"]},
                "local:2505.18524-1": {
                    "status": "partial",
                    "reason": "Opus final: a same-model contrast exists for ADAS-TG → ADAS-TG(O) on Dyck (test .16 → .37, both "
                              "o1; opus:O01), isolating the meta-prompt step from optimizer-model strength there; for TGD the "
                              "o1-written prompt is still confounded, and no arm injects the o1-written task analysis directly "
                              "into the program prompt.",
                    "evidence_ids": ["son55:E010", "son55:E020", "opus:O01", "opus:O02"]},
            }),
        "claims": lambda c, p=p: add_counter(c, "C1", ["opus:O01"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "The meta-optimized optimizer (a retained non-weight improver) is selected on D_val and then "
                                   "applied to a separate test split and to one other model and one other dataset. Not "
                                   "'improver': there is no comparable-budget comparison of the edited vs fixed improver "
                                   "(J undisclosed, o1 meta loop on top of the baselines).",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, 5-seed test means without spread on four small splits (40–100 items): "
                                         "meta-optimized TextGrad optimizers yield programs that beat fixed TGD/ADAS-TG on "
                                         "Word Sorting, Dyck and GPQA and tie on Abstract Algebra (below zero-shot MIPROv2); "
                                         "on Dyck the meta-prompt step helps both TGD and ADAS-TG while the meta-structure "
                                         "step adds nothing. Total optimization cost and a budget-matched improver comparison "
                                         "are absent; Theorem 1 does not certify the data-dependent argmin. Not reproduced.",
            "unresolved": ["J/I and total meta-search cost undisclosed.",
                           "Variance of the whole search (only 5-seed test means).",
                           "PromptBreeder/STOP-style self-referential optimizer neighbours are not in the fixed material "
                           "(background only; no request filed because G=2 is supported by in-paper evidence)."]},
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The non-weight object (task-agnostic optimizer prompt and optimizer "
                   "composition) is concrete, but the bottleneck evidence is one anecdote of noisy textual feedback plus low "
                   "baseline scores, and §5 covers prompt optimization and classical meta-learning only — no self-referential "
                   "or optimizer-editing neighbour is discussed while §1 asserts 'no method' exists. sol's 3 itself notes the "
                   "lineage is checked only in-text.",
                   ["son55:E001", "son55:E002", "son55:E023", "sol:E001"]),
            "M": R("resolved", 2, "Opus sides with son55. Propose = sample one training Q/A + current prompt → o1 rewrite; "
                   "Update = keep if inner-loop validation improves: reconstructable. The causal story (task-specific optimizer "
                   "prior dampens noisy feedback) is plausible but not separated from the naive alternative of o1 injecting "
                   "task knowledge, and Theorem 1 applies Hoeffding to a data-dependent argmin without a uniform-convergence "
                   "step (both seats), so the offered 'theoretical foundation' does not carry the key assumption.",
                   ["son55:E003", "son55:E004", "son55:E016", "son55:E022", "sol:E012"]),
            "X": R("resolved", 3, "Both seats 3; re-checked and kept. Algorithms 1–4 plus Appendix D prompts make the outer and "
                   "inner loops, information access (train examples to the meta-prompt, D_val for promotion, test held back) "
                   "and the σ>σ* retention rule reconstructable. Not 4: J and I are never instantiated (opus:O04), failure "
                   "handling of non-executable generated optimizer code is not described, and Appendix E.2's final evaluator "
                   "interface is inconsistent (sol:E011).",
                   ["son55:E003", "son55:E004", "son55:E025", "sol:E002", "sol:E003", "sol:E011", "opus:O04"],
                   ["son55:E010"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Accuracy against ground truth is meaningful, but "
                               "graders differ by method: regex exact match for TextGrad methods vs a GPT-4o judge for DSPy "
                               "baselines on MMLU/GPQA (son55:E014, sol:E008), BBH is GPT-4o-judged, and ADAS-TG is a "
                               "re-implementation.",
                               ["son55:E014", "sol:E008", "son55:E009", "son55:E026"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked with a correction to son55's reason. Fixed-optimizer "
                             "baselines and the Dyck component ablation (TGD→TGD(O), ADAS-TG→ADAS-TG(O), Struct(O)) are "
                             "relevant; ADAS-TG and ADAS-TG(O) both run on o1 (opus:O01), so on Dyck the meta-prompt gain is "
                             "not an optimizer-model effect. Remaining: the extra outer-loop budget is unmatched, the ablation "
                             "covers one task, the structure optimizer adds nothing there (son55:E010), and the TGD side keeps "
                             "the o1-vs-GPT-4o confound.",
                             ["son55:E020", "son55:E010", "sol:E006", "opus:O01", "opus:O02"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Fixed train/val/test splits (TextGrad's for BBH; authors' "
                           "for MMLU-AA and GPQA); promotion uses D_val, results are reported on the untouched test split, "
                           "plus one cross-model and one cross-dataset transfer. Not 4: D_val is reused by inner and outer "
                           "selection, no contamination check, and each transfer is a single small slice (Claude Dyck .35 vs "
                           "ADAS-TG .34).",
                           ["sol:E007", "son55:E004", "son55:E013", "son55:E024"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked. 5-seed test means with item counts and negative "
                              "results (AA tie, structure step no gain), but no spread, interval or test on any headline; "
                              "A2 rung 1.",
                              ["sol:E005", "son55:E007", "son55:E006"]),
            "E.cost": R("resolved", 1, "Opus sides with son55. The only search-cost data is a per-epoch token split on one "
                        "dataset (opus:O03); the number of meta and inner iterations is never given (opus:O04), so total "
                        "optimization cost is not reconstructable, and Table 3's dollar comparison is deployment cost of the "
                        "final program. No equal-budget improver comparison though the meta level uses o1. sol's 2 lists the "
                        "same gaps; the missing iteration counts put this below 'relevant result with gaps'.",
                        ["son55:E011", "son55:E012", "sol:E009", "opus:O03", "opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–I and checklist; in scope (B): the retained non-weight object is "
                  "the optimizer prompt/code edited by a meta-optimizer from downstream validation scores; all eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["make_the_improver_editable", "H19"]],
                "H19 kept by both. son55's low-fit H17 dropped: the object searched by the meta structure optimizer is the "
                "optimizer (improver) code, already the H19 match; H17 concerns the agent/program design space, which here "
                "is searched by the ADAS-TG baseline/inner optimizer, not by the contribution.",
                ["sol:E003", "son55:E025"], NOSCORE),
            X(p, "local:2505.18524-1", *C(p, "expectations[local:2505.18524-1].status"), "revised", "partial",
              "son55's 'no same-model optimizer control' is partly wrong: ADAS-TG runs on o1 (opus:O01, opus:O02), so ADAS-TG "
              "vs ADAS-TG(O) is same-model; TGD remains confounded.", ["son55:E010", "opus:O01", "opus:O02"]),
            X(p, "local:2505.18524-2", *C(p, "expectations[local:2505.18524-2].status"), "son55", "unmet",
              "Verified: AA 40 and GPQA 68 test items, no intervals; AA shows no gain.", ["son55:E006", "son55:E007"]),
            X(p, "rs:generative_process_redesign/RE-1", *C(p, "expectations[rs:generative_process_redesign/RE-1].status"),
              "son55", "partial", "Verified: component ablation on Dyck only; structure step adds nothing.",
              ["son55:E010", "son55:E020"]),
            X(p, "rs:generative_process_redesign/RE-3", *C(p, "expectations[rs:generative_process_redesign/RE-3].status"),
              "son55", "partial", "Verified: per-module ablation only on Dyck.", ["son55:E020"]),
            X(p, "rs:generative_process_redesign/RE-4", *C(p, "expectations[rs:generative_process_redesign/RE-4].status"),
              "son55", "unmet", "Verified: Theorem 1 proof applies Hoeffding to the data-dependent θ̂ (both seats).",
              ["son55:E022", "sol:E012"]),
            X(p, "rsi:make_the_improver_editable/F4", *C(p, "expectations[rsi:make_the_improver_editable/F4].status"), "sol",
              "unmet", "Noise-compounding guard absent: only 5-seed test means are described, no variance and no repeated "
                       "search lineage; greedy promotion on one D_val run. son55's 'partial' credits the test averaging, which "
                       "does not address noisy promotion.", ["sol:E005", "son55:E007"]),
            X(p, "rsi:make_the_improver_editable/F5", *C(p, "expectations[rsi:make_the_improver_editable/F5].status"),
              "revised", "partial", "Leak only on the TGD side; ADAS-TG comparison is o1-vs-o1.",
              ["son55:E005", "opus:O01", "opus:O02"]),
            X(p, "rsi:make_the_improver_editable/S1", *C(p, "expectations[rsi:make_the_improver_editable/S1].status"),
              "son55", "partial", "Verified: the hand-designed meta-optimizer is stated as fixed only in the conclusion.",
              ["son55:E015"]),
            X(p, "rsi:make_the_improver_editable/S3", *C(p, "expectations[rsi:make_the_improver_editable/S3].status"),
              "son55", "met", "The success condition is the comparison against the fixed hand-designed improver, which "
                              "exists (TGD, ADAS-TG, MIPROv2). Budget parity is the separate S4/F5 check; sol's 'partial' "
                              "folds S4 into S3.", ["son55:E021", "sol:E006"]),
            X(p, "rsi:make_the_improver_editable/S5", *C(p, "expectations[rsi:make_the_improver_editable/S5].status"),
              "revised", "not_applicable", "son55 marked applicable=false with status 'unmet'; aligned to not_applicable "
                                           "(H19 single lineage by definition).", ["son55:E004"]),
            rr(p, "G", "son55", 2, "See ratings.G: anecdotal bottleneck; no optimizer-editing neighbour discussed.",
               ["son55:E002", "son55:E023"], "−3.75 vs sol (15×1/4)"),
            rr(p, "M", "son55", 2, "See ratings.M: causal story not separated from o1 task-knowledge injection; Theorem 1 "
                                   "does not carry it.", ["son55:E016", "son55:E022"], "−5.0 vs sol (20×1/4)"),
            rr(p, "E.cost", "son55", 1, "See ratings.E.cost: J/I undisclosed; only per-epoch tokens and deployment dollars.",
               ["opus:O03", "opus:O04", "son55:E011"], "−1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"scope": "son55 reasons (ratings.E.causality, expectations F5 / local-1, assessment.unresolved)",
             "error": "States that the meta level (o1) is stronger than all baseline optimizers (GPT-4o) and that no same-model "
                      "optimizer control exists.",
             "correction": "§4.1 assigns o1 to 'the structure optimizer' (ADAS-TG) as well as to the meta-optimizers; only "
                           "TGD/MIPROv2 run on GPT-4o. ADAS-TG vs ADAS-TG(O) is a same-model contrast. E.causality stays 2 "
                           "(unmatched budget, one-task ablation remain).",
             "evidence_ids": ["opus:O01", "opus:O02", "son55:E005"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read all of §1–6 and Appendices A–I first: improver-level non-weight edit "
                                                   "(optimizer prompt + optimizer code merge), greedy keep-if-D_val-improves, "
                                                   "applied once to test. Noted before seats: no optimizer-editing neighbour "
                                                   "in §5; Theorem 1 uses Hoeffding on a data-dependent argmin; DSPy graded "
                                                   "by GPT-4o vs regex for others; 5-seed means without spread; J never "
                                                   "given; o1 meta level.",
            "integrity_checks": "Both seats a1 on 2505.18524v2, material sha bed1ec31…; seat hashes equal conflicts.json; both "
                                "did full 15+31 + domain identification with valid namespaces.",
            "core_claim_check": "Table 1 re-read: test gains on WS/Dyck/GPQA, AA tie with TGD (0.71) and below MIPROv2 (0.77); "
                                "Table 6: meta-structure adds nothing on Dyck.",
            "rating_agreement": "5 of 8 items agreed and re-verified; G/M/E.cost resolved for son55.",
        },
    }

    # =========================================================== 2505.20286 Alita (Δ2.5)
    p = "2505.20286"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "on GAIA with and without Alita-generated MCPs based on GPT-4o.", "§5.1.2",
                    "The MCP reuse experiment is evaluated on GAIA, the same dataset from whose runs the MCPs were collected "
                    "(§5.1.1); no source/test separation or overlap audit is described."),
            opus_ev(p, "O02", "Due to limitations in resources, we randomly selected 100 samples from the dataset.",
                    "§4.1.1 MathVista / PathVQA",
                    "MathVista/PathVQA are random 100-item slices with no reported tuning on them — the only evaluations not "
                    "tied to the GAIA library-building runs."),
        ],
        "rs_pattern": rsp("son55", p, reason=(
            "Both seats decompose_and_delegate / C25: the manager emits executable tool scripts as the structured, "
            "machine-checkable intermediate artifact, routes them to an interpreter in an isolated environment and closes "
            "the loop with execution results (repair, register). Execution success is not task correctness (sol).")),
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "crystallize_executable_capability", "H07")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2505.20286-1"): "local:2505.20286-3",
                    ("son55", "local:2505.20286-2"): "local:2505.20286-4"},
            overrides={
                "rsi:crystallize_executable_capability/S2": {
                    "status": "partial",
                    "reason": "Opus final: creation is gap-gated (MCP Brainstorming first decides whether additional tools are "
                              "needed), but no dedup/redundancy or capability-increment check of the registry is described. "
                              "son55's 'unknown' is replaced because the gap check is stated; sol recorded S2 partial in its "
                              "condition checks.",
                    "evidence_ids": ["son55:E017", "sol:E001", "sol:E015"]},
                "local:2505.20286-3": {"reason": "son55 local-1 renumbered (A4 hidden collision with sol local-1). pass@3 is "
                                                 "best-of-three with ground-truth selection; comparisons should be pass@1 with "
                                                 "per-run spread. Scored once under E.holdout (A2)."},
                "local:2505.20286-4": {"reason": "son55 local-2 renumbered (A4 hidden collision with sol local-2). The library "
                                                 "needs a generation/holdout split or reuse on another benchmark."},
            }),
        "claims": lambda c, p=p: add_counter(c, "C2", ["opus:O01"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "The retained MCP library is collected from GAIA runs and its reuse is evaluated on GAIA "
                                   "(opus:O01); with no source/test separation the library on/off gains are selection-set "
                                   "results (EVIDENCE rule 2). Both seats.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: Alita with Claude-Sonnet-4/3.7 + GPT-4o reaches 75.15/72.73 pass@1 on "
                                         "GAIA validation (pass@3 is best-of-three with ground-truth selection), and MCPs "
                                         "harvested from GAIA runs raise ODR-smolagents by about 6–7 points on the same GAIA "
                                         "set. Neither the contribution of MCP creation within Alita nor retained-library "
                                         "benefit on unseen tasks is shown; no cost is reported. Not reproduced.",
            "unresolved": ["Which run pass@1 refers to; MCP count and the 'expected results' gate signal.",
                           "Overlap between MCP source questions and evaluated questions.", "Any cost figure."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. The object (predefined tool set → runtime-generated retained MCPs) "
                   "is concrete and tool-creation neighbours (CRAFT, TroVE, CREATOR, AutoAgent, OpenHands) are cited, but the "
                   "three limitations are asserted rather than measured and the claimed MCP advantage over plain tool creation "
                   "('better reusability') has no evidence.",
                   ["son55:E001", "son55:E002", "son55:E022", "sol:E012", "sol:E015"]),
            "M": R("resolved", 2, "Opus sides with son55. Gap self-assessment → web/GitHub grounding → script + env generation → "
                   "isolated execution → register is reconstructable and answers 'long-tail tool coverage'. But the "
                   "load-bearing assumptions are untested — the 'expected results' gate certifies correctness, Brainstorming's "
                   "self-assessment is accurate, and minimal predefinition helps — and no prediction separates it from a "
                   "code-writing agent without MCP packaging (sol's own reason: distinguishing predictions weak).",
                   ["son55:E003", "son55:E004", "son55:E017", "son55:E021", "sol:E001", "sol:E002"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Tools, environment management and fallback/discard are specific; "
                   "the admission signal ('expected results' / 'accurate result formulation') is undefined, registry "
                   "retrieval/ranking/versioning/retirement are not described, prompts are not disclosed and pass@1's run is "
                   "unspecified.",
                   ["son55:E004", "son55:E005", "son55:E017", "son55:E019", "sol:E004", "sol:E013"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked (reason re-based per A2). GAIA exact-match scoring is "
                               "credible, but baseline numbers come from heterogeneous leaderboard configurations, the text's "
                               "'outperforms all baseline agents across the GAIA levels' is contradicted at Level 1 (A-World "
                               "86.79, OWL 84.91 > 81.13), and MathVista/PathVQA scoring is unspecified. The oracle pass@k "
                               "selection is scored under E.holdout only (correction to son55's reason).",
                               ["son55:E009", "son55:E015", "sol:E005", "sol:E014"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Library on/off within one framework (ODR-smolagents "
                             "GPT-4o; base framework GPT-4o-mini) supports a local library effect, but Alita itself has no "
                             "MCP-creation on/off, removal of predefined tools is confounded with the new component, and the "
                             "main table compares across backbones and harnesses.",
                             ["son55:E012", "son55:E014", "son55:E008", "sol:E008", "sol:E009"],
                             ["son55:E020", "son55:E021"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55. Not 0: part of the central claim has applicable evidence — "
                           "pass@1 on GAIA and random 100-item MathVista/PathVQA slices with no reported tuning (opus:O02). But "
                           "the retained-library claim has no separation at all: MCPs are harvested from GAIA runs and reused "
                           "on GAIA (opus:O01; the case-study MCP is question-specific), GAIA validation answers are public, "
                           "and pass@3 selects the best answer with ground truth (A2: oracle → E.holdout). sol's 0 reads the "
                           "claim as the library claim only.",
                           ["son55:E010", "son55:E011", "son55:E018", "sol:E006", "sol:E007", "sol:E010", "opus:O01",
                            "opus:O02"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked. Item counts and a negative result (GPT-4o-mini 43.64) "
                              "are reported; no per-run spread of the three GAIA rounds, no intervals; Level 3 has 26 items and "
                              "a 2-item change is called 'tripling'. A2 rung 1.",
                              ["son55:E007", "son55:E013", "sol:E010", "sol:E011"]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; re-checked: 'cost', 'token', 'latency', 'budget' do not "
                        "occur in the pinned text; the only cost statement is the unquantified 'easier, cheaper, and faster' "
                        "than distillation.", [],
                        scope=["full text §1–6, Tables 1–4, Appendix A case study, Appendix B limitations",
                               "string search: cost, token, latency, budget, seed, variance"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–B; in scope (A): runtime-created MCPs are retained in an MCP box "
                  "for later tasks and other agents; all eight items resolved (E.cost not_reported after full search).",
        "aggregate_status": "accepted_final",
        "resolutions": [
            X(p, "rs:decompose_and_delegate/RE-2", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"), "sol",
              "partial", "One isolation of the claimed load-bearing artifact exists (MCP library on/off in ODR-smolagents, two "
                         "backbones), though on the source set; Alita's own components (creation, Brainstorming, web agent) "
                         "are not ablated. Partial, not unmet.", ["sol:E008", "sol:E009", "son55:E012"]),
            X(p, "rs:decompose_and_delegate/RE-3", *C(p, "expectations[rs:decompose_and_delegate/RE-3].status"), "son55",
              "unmet", "Verified: 'We designed specialized prompts' — prompts not disclosed.", ["son55:E017"]),
            X(p, "rs:decompose_and_delegate/RE-4", *C(p, "expectations[rs:decompose_and_delegate/RE-4].status"), "son55",
              "partial", "Verified: MathVista/PathVQA 100-item slices beyond GAIA; library not reused across them.",
              ["son55:E015", "opus:O02"]),
            X(p, "rs:decompose_and_delegate/RE-5", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"), "son55",
              "partial", "Verified: ODR-smolagents is the same skeleton; main table mixes backbones.", ["son55:E008"]),
            X(p, "rsi:crystallize_executable_capability/F1",
              *C(p, "expectations[rsi:crystallize_executable_capability/F1].status"), "son55", "partial",
              "Verified: MCP creation sits inside the manager + web-agent architecture, isolated only via Tables 2/3.",
              ["son55:E012"]),
            X(p, "rsi:crystallize_executable_capability/S2",
              *C(p, "expectations[rsi:crystallize_executable_capability/S2].status"), "revised", "partial",
              "Gap-gated creation is stated (Brainstorming), increment/redundancy checks are not; unknown → partial.",
              ["son55:E017", "sol:E001"]),
            rr(p, "M", "son55", 2, "See ratings.M: gate correctness, self-assessment accuracy and the minimalism premise "
                                   "untested; no distinguishing prediction.", ["son55:E017", "son55:E021"],
               "−5.0 vs sol (20×1/4)"),
            rr(p, "E.holdout", "son55", 1, "See ratings.E.holdout: some applicable evidence for the system claim; none for "
                                           "the library claim; oracle pass@k.", ["opus:O01", "opus:O02", "son55:E010"],
               "+2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"scope": "A4 hidden collision: local:2505.20286-1 (both seats 'unmet', not in conflicts.json)",
             "error": "sol local-1 asks for run variance/CIs (E.statistics); son55 local-1 asks for pass@1-based comparison "
                      "instead of oracle pass@3 — different questions under one ID.",
             "correction": "sol keeps local:2505.20286-1; son55's question renumbered local:2505.20286-3 (status unmet kept).",
             "evidence_ids": ["sol:E006", "son55:E006"], "score_impact": "none"},
            {"scope": "A4 hidden collision: local:2505.20286-2 (both seats 'unmet', not in conflicts.json)",
             "error": "sol local-2 asks for a ground-truth-free answer selector for pass@k; son55 local-2 asks for a "
                      "generation/holdout split of the library — different questions under one ID.",
             "correction": "sol keeps local:2505.20286-2; son55's question renumbered local:2505.20286-4 (status unmet kept).",
             "evidence_ids": ["sol:E006", "son55:E010"], "score_impact": "none"},
            {"scope": "son55 reason, ratings.E.measurement",
             "error": "Counts oracle pass@k selection as a measurement defect.",
             "correction": "Rubric A2 assigns oracle/ground-truth retry selection to E.holdout only; E.measurement=2 rests on "
                           "heterogeneous baselines, the Level-1 overclaim and unspecified MathVista/PathVQA scoring.",
             "evidence_ids": ["son55:E006", "son55:E009"], "score_impact": "none (rating unchanged)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first: MCP box retained via an undefined execution-success "
                                                   "gate; reuse experiments evaluate GAIA with MCPs harvested from GAIA runs; "
                                                   "pass@3 = best of three with ground truth; no Alita MCP-creation ablation; "
                                                   "no cost anywhere.",
            "integrity_checks": "Both seats a1 on 2505.20286v1, material sha 2f3982ba…; hashes equal conflicts.json; full "
                                "identification by both.",
            "core_claim_check": "Tables 1–4 re-read; Level-1 'outperforms all' claim contradicted by A-World/OWL; library "
                                "on/off +6.1 (GPT-4o) / +7.3 (GPT-4o-mini) on GAIA.",
            "rating_agreement": "6 of 8 agreed and re-verified; M and E.holdout resolved for son55.",
        },
    }

    # =========================================================== 2506.04651 HexMachina (Δ2.5)
    p = "2506.04651"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "computes the expected value of successor states via chance expansion and a fast heuristic value "
                    "function", "§3 Alpha-Beta Benchmark",
                    "AlphaBeta's own machinery is chance expansion + pruning; the induced adapters.py exposes "
                    "execute_spectrum / expand_spectrum / prune_robber_actions (son55:E017), so the evolved player inherits "
                    "the baseline's search primitives — an alternative explanation for the discovery gain."),
            opus_ev(p, "O02", "Read local file, web search", "§4.2 Agents, Researcher tools",
                    "The Researcher may read local files and search the web; what it could read (e.g. Catanatron/AlphaBeta "
                    "source) is not bounded, so the 'without documentation' information boundary is unstated."),
        ],
        "rs_pattern": rsp("son55", p, reason=(
            "decompose_and_delegate / C25 (son55): the LLM stops choosing per-turn actions and instead emits an executable "
            "player program (structured, machine-checkable intermediate artifact) that the simulator executes, closing the "
            "loop with game outcomes. sol's generative_process_redesign (sub null) concerns fixed components of iterative "
            "generative procedures, and heterogeneous_decomposition requires partitioning one resource by a measured "
            "property; neither fits the operation as well as C25.")),
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                        dmatch("son55", p, "crystallize_executable_capability", "H07")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2506.04651-1"): "local:2506.04651-4"},
            overrides={
                "local:2506.04651-2": {
                    "reason": "Opus final (status unknown kept): the paper does not say whether the Researcher (local file read "
                              "+ web search, opus:O02) could read AlphaBeta source; observed: the adapters export the "
                              "baseline's chance-expansion/pruning utilities (son55:E017, opus:O01).",
                    "evidence_ids": ["son55:E017", "son55:E026", "opus:O01", "opus:O02"]},
                "local:2506.04651-4": {"reason": "son55 local-1 renumbered (A4 collision with sol local-1). Needs held-out "
                                                 "opponents/maps/seeds before claiming a general strategy rather than an "
                                                 "AlphaBeta-specific exploit."},
            }),
        "claims": lambda c, p=p: add_counter(c, "C2", ["opus:O01"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "The retained player is promoted on 30-game batches against AlphaBeta under fixed seeds and "
                                   "then stress-tested against the same opponent with no stated seed separation; the reported "
                                   "configuration was chosen on these results; the retained-artifact effect (adapters / "
                                   "archive on-off) has no in-text numbers. Selection/test separation not established → task "
                                   "(sol). son55's 'retained' rests on the 1000-game run being separate, which the text does "
                                   "not establish.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported: the best evolved GPT-5-mini-coded player wins 54.1% [51, 57] of "
                                         "1000 two-player games against AlphaBeta (AlphaBeta self-play 51.0% [48, 54]); Mistral "
                                         "and Claude orchestrators do not exceed AlphaBeta; removing the Analyst collapses "
                                         "evolution. The decoupling claim lacks in-text numbers and is confounded by adapters "
                                         "that expose AlphaBeta's own search primitives. Single game, single opponent. Not "
                                         "reproduced.",
            "unresolved": ["Seed separation between evolution and stress-test games.",
                           "No-discovery numbers (Figure 3 only, not in the pinned text).",
                           "Table 3 'No Strategist + Researcher' row equals the 10×100 stress-test result (54.1%, 8.2) and is "
                           "not attainable as k/30 or k/90 under the stated 3-run × 30-game protocol.",
                           "Researcher's access to AlphaBeta source; total LLM spend."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Specific bottleneck (per-turn re-parsing of large states, context "
                   "saturation) with a measured symptom (per-turn LLM player 16.4%) and named neighbours (Voyager, Eureka, "
                   "AlphaEvolve, PromptBreeder) with a stated breadth-vs-depth difference. Not 4: the comparison table is "
                   "author-scored and the 'shallow heuristics' failure of the Voyager-style learner rests on one code "
                   "example.",
                   ["son55:E001", "son55:E002", "son55:E003", "sol:E001"]),
            "M": R("resolved", 2, "Opus sides with son55. Discovery → adapters → Analyst/Coder/Orchestrator loop → simulator "
                   "feedback is reconstructable and the per-turn vs compiled-policy prediction is clear, but the key "
                   "assumption behind the central novelty (separating discovery from improvement yields strategic depth) has "
                   "an untreated simpler explanation — the induced adapters expose AlphaBeta's chance-expansion and pruning "
                   "utilities (son55:E017, opus:O01) — and preserve/discard is an unconstrained LLM decision.",
                   ["son55:E017", "son55:E018", "son55:E022", "son55:E026", "sol:E003", "sol:E005", "opus:O01"]),
            "X": R("resolved", 2, "Opus sides with sol. Phases, role I/O, memory types and the evolution cap are described, but "
                   "the retention criterion is the Orchestrator's free judgment (no threshold or regression check), how the "
                   "'best-evolved' player is chosen is only a best-so-far curve, rollback and hallucinated-code filtering are "
                   "not specified, the run length is inconsistent (20 evolutions per phase vs 10-step runs), and the "
                   "information boundary for 'without documentation' is open (Researcher reads local files and the web, "
                   "opus:O02).",
                   ["sol:E002", "sol:E005", "sol:E008", "son55:E004", "son55:E005", "son55:E006", "son55:E008",
                    "opus:O02"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Win rate and victory points from a deterministic "
                               "simulator against a fixed opponent are direct and reproducible, with game-level intervals. "
                               "Not 4: coarse metrics (authors' own limitation) and a single opponent / 2-player format.",
                               ["son55:E007", "son55:E024", "son55:E027", "sol:E012", "sol:E013", "sol:E016"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Analyst and Strategist+Researcher ablations and backend "
                             "variation are relevant; the decoupling has no in-text numbers, the 'No Strategist + Researcher' "
                             "row reproduces the stress-test value rather than the stated ablation protocol, the "
                             "library-primitive explanation is not excluded (opus:O01), and there is no budget-matched "
                             "alternative (e.g. independent regeneration without retention).",
                             ["son55:E012", "son55:E013", "son55:E014", "son55:E017", "sol:E014", "sol:E015", "opus:O01"],
                             ["son55:E013"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. The 10×100 stress test is a separate run, but (i) its seeds are "
                           "not stated to differ from the fixed-seed 30-game promotion batches, (ii) the reported configuration "
                           "was selected on these results ('Thus, we report results using this streamlined configuration') "
                           "and its ablation row equals the stress-test number, (iii) promotion and test use the same single "
                           "opponent with no other opponents/maps, and (iv) the Researcher's file/web access leaves possible "
                           "access to AlphaBeta source unbounded (opus:O02). son55's 2 credits the separate run, which the "
                           "text does not show to be independent.",
                           ["sol:E004", "sol:E011", "son55:E009", "son55:E010", "son55:E024", "son55:E025", "opus:O02"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked. Game-level intervals on the final players (10×100) and "
                              "negative results; no spread across independent evolution runs (ablation's 3 runs report none), "
                              "best run reported. A2 rung 2.",
                              ["sol:E011", "sol:E012", "son55:E010", "son55:E014"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. 60 h wall-clock on two laptops and ~70 queries per game for "
                        "the per-turn baseline; no token/dollar figure for evolution, no failed-candidate accounting, no "
                        "budget comparison; authors call it expensive.",
                        ["sol:E017", "sol:E018", "son55:E015", "son55:E019", "son55:E020"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendix A.1/A.2 code (Figures 3/4 are images; their values are not in the text "
                  "and were not used); in scope (A): executable adapters and player code are retained and evolved from "
                  "simulated game outcomes; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "See assessment.evidence_level_note: promotion and stress test share the opponent, seed separation is "
                "unstated, configuration chosen on the reported numbers.", ["sol:E011", "son55:E009", "son55:E024"],
                "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "LLM emits an executable program executed by a simulator with outcome feedback (C25).",
                ["son55:E007", "sol:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["decompose_and_delegate", "C25"]],
                "C25 fits step 2–3 (machine-checkable artifact, closed loop with execution results); sol's two matches have no "
                "sub-card and weaker operation correspondence.", ["son55:E007", "sol:E003"], NOSCORE),
            X(p, "local:2506.04651-1", *C(p, "expectations[local:2506.04651-1].status"), "revised",
              "local-1 = sol's budget-parity question → partial; son55's local-1 (held-out opponents/maps) renumbered local-4 = "
              "unmet", "A4 collision: same ID, different questions. sol's question verified partial (20-game per-turn Claude "
              "vs multi-run mixed-model evolution); son55's verified unmet (single opponent/map).",
              ["sol:E009", "son55:E025"]),
            X(p, "local:2506.04651-2", *C(p, "expectations[local:2506.04651-2].status"), "son55", "unknown",
              "Not resolvable from the pinned text; observed primitive overlap recorded.", ["son55:E017", "opus:O02"]),
            X(p, "local:2506.04651-3", *C(p, "expectations[local:2506.04651-3].status"), "son55", "partial",
              "Verified: intervals are game-level; 3 ablation runs without spread.", ["son55:E014"]),
            X(p, "rs:decompose_and_delegate/RE-1", *C(p, "expectations[rs:decompose_and_delegate/RE-1].status"), "son55",
              "partial", "Verified: 60 h and baseline query counts only.", ["son55:E019", "son55:E020"]),
            X(p, "rs:decompose_and_delegate/RE-2", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"), "son55",
              "partial", "Verified: role ablations exist; decoupling has no in-text numbers.", ["son55:E013", "son55:E012"]),
            X(p, "rs:decompose_and_delegate/RE-4", *C(p, "expectations[rs:decompose_and_delegate/RE-4].status"), "son55",
              "unmet", "Verified: one game, one opponent, 2-player; authors list other benchmarks as future work.",
              ["son55:E025"]),
            X(p, "rs:decompose_and_delegate/RE-5", *C(p, "expectations[rs:decompose_and_delegate/RE-5].status"), "son55",
              "partial", "Verified: per-turn LLM baseline on 20 games with a different model.", ["son55:E015"]),
            X(p, "rsi:attribute_and_patch_incumbent/F3", *C(p, "expectations[rsi:attribute_and_patch_incumbent/F3].status"),
              "son55", "unmet", "Failure mode present: a single game-player program is evolved against its own benchmark "
                                "(card F3 names game-player generators). Quality concern, not a scope ruling (A3: retained "
                                "non-weight code is evaluated).", ["son55:E025", "sol:E003"]),
            X(p, "rsi:attribute_and_patch_incumbent/F4", *C(p, "expectations[rsi:attribute_and_patch_incumbent/F4].status"),
              "son55", "met", "Verified: simulator outcomes, not self-evaluation, certify edits.", ["son55:E007"]),
            X(p, "rsi:attribute_and_patch_incumbent/H12", *C(p, "expectations[rsi:attribute_and_patch_incumbent/H12].status"),
              "sol", "partial", "Verified: trace diagnosis drives code edits; improver itself fixed; no cross-task "
                                "certification.", ["sol:E005", "sol:E008"]),
            X(p, "rsi:attribute_and_patch_incumbent/S1", *C(p, "expectations[rsi:attribute_and_patch_incumbent/S1].status"),
              "son55", "unknown", "Edit scope (local patch vs whole rewrite) is not stated anywhere.", ["son55:E005"]),
            X(p, "rsi:attribute_and_patch_incumbent/S5", *C(p, "expectations[rsi:attribute_and_patch_incumbent/S5].status"),
              "son55", "partial", "Verified: Analyst reads game artifacts and code; Coder sees objective + adapters.",
              ["son55:E005", "sol:E008"]),
            X(p, "rsi:crystallize_executable_capability/S3",
              *C(p, "expectations[rsi:crystallize_executable_capability/S3].status"), "sol", "partial",
              "adapters.py is reused across all later improvement-phase and stress-test game states (inputs it was not "
              "built from) but never on another environment or interface, so the doc-free induction claim is untested "
              "beyond Catanatron. Partial rather than son55's unmet.", ["sol:E011", "son55:E018"]),
            rr(p, "M", "son55", 2, "See ratings.M: decoupling assumption has an untreated library-primitive explanation.",
               ["son55:E017", "opus:O01"], "−5.0 vs sol (20×1/4)"),
            rr(p, "X", "sol", 2, "See ratings.X: free-form retention, unspecified best-player choice, open information "
                                 "boundary.", ["sol:E005", "opus:O02"], "−5.0 vs son55 (20×1/4)"),
            rr(p, "E.holdout", "sol", 1, "See ratings.E.holdout: seed separation unstated, configuration chosen on reported "
                                         "numbers, single opponent, unbounded Researcher access.",
               ["son55:E009", "opus:O02"], "−2.5 vs son55 (10×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–9 and Appendix A first: retained adapters + evolved player; "
                                                   "best-so-far player from 30-game fixed-seed batches then 10×100 stress test "
                                                   "against the same opponent; no-discovery baseline only in Figure 3; Table 3 "
                                                   "row equal to Table 2; 60 h wall-clock, no LLM spend.",
            "integrity_checks": "Both seats a1 on 2506.04651v2, material sha 8b07806e…; hashes equal conflicts.json; full "
                                "identification by both; neither used figure values (consistent with the controller note).",
            "core_claim_check": "Table 2 CIs overlap with AlphaBeta self-play (54.1 [51,57] vs 51.0 [48,54]): 'outperform' is "
                                "a point estimate; adapters import AlphaBeta-side utilities (son55:E017).",
            "rating_agreement": "5 of 8 agreed and re-verified; M → son55, X and E.holdout → sol; final 52.5 is below both "
                                "seats because item-level rulings split.",
            "shared_error_check": "No shared error found; sol's 'retained' gap and son55's unseparated-run credit resolved "
                                  "as above.",
        },
    }

    # =========================================================== 2506.06254 PersonaAgent (Δ8.75)
    p = "2506.06254"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "the corresponding true user response", "§2.1 Episodic Memory, gloss of Eq. (1)",
                    "Eq. (1) defines the calligraphic D^u as the user's episodic buffer of past queries with their true "
                    "responses; Algorithm 1's input 'Test User data D' uses the same symbol, and 'Test User' means a user of "
                    "the 100-user test population (opus:O03)."),
            opus_ev(p, "O02", "a profile set representing their historical behaviors, and a test set reserved for final "
                    "evaluation", "Appendix G",
                    "Per-user chronological split; the later test split is stated to be reserved for final evaluation."),
            opus_ev(p, "O03", "our test set consists of the 100 users with the most extensive activity histories",
                    "Appendix G", "'Test set' = population of 100 users, so 'Test User data' denotes a test user's data, "
                                  "not the test split."),
            opus_ev(p, "O04", "test-time user-preference alignment strategy that simulate the latest", "Abstract",
                    "Alignment simulates the latest n interactions (n=3, one iteration; Appendix F) — at evaluation time "
                    "these are the most recent profile items preceding the reserved test split."),
            opus_ev(p, "O05", "triggered immediately after each user session completes", "§3.7 Efficiency Analysis",
                    "Counter-reading: in deployment, alignment would run after each session; the offline LaMP protocol does "
                    "not state any re-alignment on revealed test labels, and the paper never states batch/test disjointness "
                    "explicitly."),
            opus_ev(p, "O06", "up to around 3 iterations, after which performance plateaus or slightly declines", "§3.5",
                    "The deployed setting uses one iteration (Appendix F), below the observed optimum, so the reported "
                    "configuration is not the test-optimal point of the LaMP-2M scaling study."),
        ],
        "rs_pattern": rsp("sol", p, reason=(
            "adapt_via_conditioning (both seats). C03 kept (sol): its complementary sub-move — retrieving the nearest "
            "reference instances as a first-class input to a frozen model — matches top-K retrieval over the user's own "
            "history conditioned through the persona; C03's main upstream multi-task tuning branch does not apply (fit "
            "partial). son55's null is replaced because one C03 branch is executed.")),
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "attribute_and_patch_incumbent", "H10"),
                        dmatch("sol", p, "index_experience_for_reuse", "H03")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2506.06254-2"): "local:2506.06254-4"},
            overrides={
                "local:2506.06254-1": {
                    "status": "partial",
                    "reason": "Opus final: the batch source is identified from notation and split language — D is the episodic "
                              "buffer of past interactions (opus:O01), the test split is 'reserved for final evaluation' "
                              "(opus:O02), alignment uses the latest n interactions (opus:O04) — but disjointness is never "
                              "stated explicitly and §3.7 describes per-session re-alignment for deployment (opus:O05). "
                              "Partial, not unknown.",
                    "evidence_ids": ["sol:E004", "sol:E012", "son55:E026", "opus:O01", "opus:O02", "opus:O03", "opus:O04",
                                     "opus:O05"]},
                "local:2506.06254-4": {
                    "status": "partial",
                    "reason": "son55 local-2 renumbered (A4 collision with sol's cost question). No separate dev split for "
                              "n/iterations/K, but the deployed defaults are not the test optimum (1 iteration vs observed "
                              "peak ~3, opus:O06; n=3 though larger batches help; K=4 is the LaMP default), so test-set "
                              "selection of the reported configuration is not indicated. unmet → partial.",
                    "evidence_ids": ["son55:E015", "son55:E016", "sol:E010", "opus:O06"]},
            }),
        "claims": lambda c, p=p: add_counter(c, "C2", ["opus:O02", "opus:O05"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Shared correction (both seats 'task'): the persona is rewritten from the latest profile "
                                   "interactions (opus:O01, opus:O04) and then used on the chronologically later, reserved "
                                   "test split (opus:O02); the 'w/o alignment' ablation, with the same profile still "
                                   "available through memory, drops on all eight metrics. That is a retained change improving "
                                   "later tasks on a held-out split (EVIDENCE.md 'retained'), single run without intervals; "
                                   "disjointness is read from notation and split language, not from an explicit statement.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported single run on the 100 most active LaMP users: PersonaAgent leads six "
                                         "baselines on LaMP-1/2M/2N/3 (+2.8–5.7 points) and test-time persona rewriting adds "
                                         "about 2–3 points over the same system without it, on the reserved later test split; "
                                         "no intervals, no equal-information simpler alternative, alignment cost off the "
                                         "latency path. Not reproduced.",
            "unresolved": ["Explicit statement of alignment-batch / test disjointness and of how often alignment runs in the "
                           "offline protocol.", "Total test-item counts; any interval.",
                           "Token/dollar cost of alignment."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Object (per-user persona prompt mediating memory and tools) is "
                   "concrete and the per-user fine-tuning scalability motive is sourced, but 'first personalized agent' is "
                   "asserted, differences to memory-equipped agents rest on the author-scored Table 1, and TextGrad is reused "
                   "unchanged.",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E029", "sol:E001", "sol:E015"]),
            "M": R("resolved", 2, "Opus sides with son55. The persona-as-intermediary + textual-loss rewrite is reconstructable "
                   "and grounded in true responses, but no prediction separates it from simply re-summarising the profile or "
                   "appending the n recent ground truths, whether feedback localises to the persona (vs retrieval/tools) is "
                   "untested, and the initial persona hard-codes 'use at least two tools', confounding the 'intermediary' "
                   "story. sol's 3 cites the ablations, which belong to E.",
                   ["son55:E004", "son55:E005", "son55:E020", "son55:E021", "sol:E003"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Prompts, n, iterations, K, tools and splits are disclosed and the "
                   "chain is reconstructable; the persona is rewritten unconditionally (no gate, version, rollback, conflict "
                   "or expiry handling), memory maintenance is unspecified and the batch source is only inferable.",
                   ["son55:E006", "son55:E007", "son55:E008", "son55:E025", "sol:E002", "sol:E010"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Official LaMP metrics against real user labels under a "
                               "unified pipeline at low temperature. Not 4: top-100 most active users only, test-item counts "
                               "not given.",
                               ["son55:E010", "son55:E011", "son55:E019", "sol:E007"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Four component ablations (alignment, persona, memory, "
                             "action) and a cold-start setting; missing an equal-information cheaper alternative, the forced "
                             "two-tool rule confounds 'w/o persona', and the alignment calls are unmatched.",
                             ["sol:E006", "sol:E008", "sol:E009", "son55:E014", "son55:E021"], ["son55:E021"]),
            "E.holdout": R("resolved", 2, "Opus sides with sol after reading Algorithm 1 against the data definitions. 'Test "
                           "User data D' denotes a test-population user's data (opus:O03) under the same symbol as the "
                           "episodic buffer of past interactions (opus:O01); the batch is the latest n interactions "
                           "(opus:O04); the chronologically later test split is 'reserved for final evaluation' (opus:O02); "
                           "and the deployed n/iterations are not the test optimum (opus:O06). So the alignment batch is "
                           "profile-sourced on the paper's own terms and the evaluation is a chronological holdout. Not 3: "
                           "disjointness is never stated explicitly and §3.7 describes per-session re-alignment (opus:O05); "
                           "no dev split, no contamination analysis, one benchmark family and the 100 most active users. "
                           "son55's 1 treated the D composition as open; the text resolves it to the profile reading with "
                           "residual ambiguity.",
                           ["sol:E004", "sol:E012", "sol:E013", "sol:E018", "son55:E015", "son55:E026", "opus:O01",
                            "opus:O02", "opus:O03", "opus:O04", "opus:O06"], ["opus:O05"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked. Single run (Appendix F) on 100 users; no intervals, "
                              "variance or test while 2–6-point gaps are called significant. A2 rung 1.",
                              ["son55:E009", "son55:E011", "son55:E013", "sol:E011"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Per-sample runtime is measured for PersonaAgent and three "
                        "baselines on all four tasks in one environment (Table 5), and the alignment budget per trigger is "
                        "bounded and derivable from the disclosed settings (n=3 simulations + feedback calls, one update, one "
                        "iteration). Gaps: alignment tokens/dollars and trigger frequency are unreported and it is excluded "
                        "from the latency path; no budget-matched baseline. Unlike metaTextGrad (same batch), the improvement "
                        "loop's size is reconstructable, so 2 rather than 1.",
                        ["sol:E010", "sol:E016", "sol:E017", "son55:E017", "son55:E018"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–M; in scope (A): a per-user persona prompt is rewritten from "
                  "execution feedback (simulated vs true responses) and retained for later queries; all eight items resolved; "
                  "the Algorithm 1 batch-source question is ruled from the text (see ratings.E.holdout).",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "C03's retrieved-reference-instance sub-move is executed (top-K user history into a frozen model).",
                ["sol:E019", "son55:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H10"], ["index_experience_for_reuse", "H03"]],
                "H10 (rewrite one incumbent prompt from textual-gradient error analysis) is the exact operation; son55's H00 "
                "maps the same rewrite again — H00 appends lessons to a store, while the persona is one document rewritten in "
                "place. The abstract_experience_into_guidance expectations are kept as informative checks.",
                ["sol:E003", "son55:E006"], NOSCORE),
            X(p, "local:2506.06254-1", *C(p, "expectations[local:2506.06254-1].status"), "sol", "partial",
              "Batch source ruled profile-sourced from notation and split language; explicit disjointness statement absent.",
              ["opus:O01", "opus:O02", "opus:O04", "opus:O05"]),
            X(p, "local:2506.06254-2", *C(p, "expectations[local:2506.06254-2].status"), "revised",
              "local-2 = sol's cost question → partial; son55's local-2 (dev split for n/iterations) renumbered local-4 = "
              "partial", "A4 collision: same ID, different questions. sol's verified (latency only). son55's question revised "
              "unmet → partial: defaults are not the test optimum (opus:O06).", ["sol:E016", "son55:E015", "opus:O06"]),
            X(p, "local:2506.06254-3", *C(p, "expectations[local:2506.06254-3].status"), "son55", "unmet",
              "Verified: single run, no intervals.", ["son55:E009"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "son55",
              "partial", "Verified: four ablations, no equal-information unconditioned control.", ["son55:E014"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55",
              "unmet", "Verified: no contamination/overlap analysis is reported (the split is stated, not audited).",
              ["son55:E024"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "partial", "Verified: RAG/PAG/MemBank compared; no 'append recent ground truths' alternative.",
              ["son55:E019"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55",
              "partial", "Verified: six LaMP tasks, one benchmark family.", ["son55:E024"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55",
              "partial", "Verified: cold start (10 interactions) and K scaling; no noise/shift analysis.",
              ["son55:E022", "son55:E016"]),
            X(p, "rsi:abstract_experience_into_guidance/S3",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "son55", "met",
              "Verified: ground-truth user responses drive feedback.", ["son55:E005"]),
            X(p, "rsi:abstract_experience_into_guidance/S4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "son55", "unmet",
              "Verified: whole-persona rewrite, no delta edits/consolidation/forgetting.", ["son55:E006"]),
            X(p, "rsi:abstract_experience_into_guidance/S5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S5].status"), "son55", "unmet",
              "Verified: no gate before the new persona replaces the old.", ["son55:E007"]),
            X(p, "rsi:attribute_and_patch_incumbent/F5", *C(p, "expectations[rsi:attribute_and_patch_incumbent/F5].status"),
              "son55", "partial", "Verified: whether errors come from the persona vs retrieval/tools is untested.",
              ["son55:E020"]),
            X(p, "rsi:attribute_and_patch_incumbent/H10", *C(p, "expectations[rsi:attribute_and_patch_incumbent/H10].status"),
              "sol", "partial", "Verified: aggregated 3-item feedback rewrite executed; no candidate selection or "
                                "validation.", ["sol:E003", "sol:E010"]),
            X(p, "rsi:attribute_and_patch_incumbent/S4", *C(p, "expectations[rsi:attribute_and_patch_incumbent/S4].status"),
              "son55", "partial", "Verified: n=3 aggregation before edit; generality untested.", ["son55:E008"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"), "sol",
              "partial", "Verified: w/o memory drops, but removes information and calls together.", ["sol:E008", "sol:E009"]),
            rr(p, "M", "son55", 2, "See ratings.M: no distinguishing prediction vs simpler profile updates; forced-tool rule "
                                   "confound.", ["son55:E020", "son55:E021"], "−5.0 vs sol (20×1/4)"),
            rr(p, "E.holdout", "sol", 2, "See ratings.E.holdout: Algorithm 1's D is the profile/episodic buffer on the "
                                         "paper's own notation; test split reserved; residual explicitness gap.",
               ["opus:O01", "opus:O02", "opus:O03", "opus:O04"], "+2.5 vs son55 (10×1/4)"),
            rr(p, "E.cost", "sol", 2, "See ratings.E.cost: comparative online latency measured; per-trigger alignment budget "
                                      "derivable; totals missing.", ["sol:E016", "sol:E010"], "+1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"scope": "assessment.evidence_level (both seats 'task')",
             "error": "Both seats capped the label at 'task' because the Algorithm 1 batch source was treated as open.",
             "correction": "With the batch ruled profile-sourced (opus:O01–O04) and the test split reserved (opus:O02), the "
                           "'w/o alignment' ablation shows the retained persona rewrite improving later held-out queries → "
                           "'retained' (scoped; single run; explicit disjointness statement absent). Not 'improver'.",
             "evidence_ids": ["sol:E008", "sol:E009", "opus:O01", "opus:O02", "opus:O04"],
             "score_impact": "none (evidence_level is not scored)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first, focusing on Algorithm 1 vs Eq. (1) and Appendix F/G: "
                                                   "D is the episodic buffer symbol; 'Test User' = test-population user; "
                                                   "test split 'reserved'; n=3, one iteration, single run; latency table "
                                                   "excludes alignment; ablation drops on all metrics.",
            "integrity_checks": "Both seats a1 on 2506.06254v2, material sha f2e0e525…; hashes equal conflicts.json; full "
                                "identification by both.",
            "core_claim_check": "Tables 2/3 re-read (LaMP-1 .919 vs MemBank .862; w/o alignment .894); Appendix L Table 5 "
                                "latency 1.79 s vs PAG 1.24 s.",
            "e_holdout_ruling": "Controller-flagged point resolved from the text: profile-sourced alignment batch, "
                                "chronological reserved test split; residual ambiguity keeps E.holdout at 2, not 3.",
            "rating_agreement": "5 of 8 agreed and re-verified; M → son55, E.holdout and E.cost → sol.",
        },
    }

    # =========================================================== 2506.06698 CER (Δ5)
    p = "2506.06698"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "show the system prompts for distillation modules, while Figure", "Appendix A.1",
                    "Distillation and retrieval prompts are published in full (Figures 3–6), making the write (dedupe-append) "
                    "and read (VLM top-k over the whole buffer, k_d=k_s=5) rules reconstructable."),
        ],
        "rs_pattern": rsp("son55", p, reason=(
            "adapt_via_conditioning, no sub-card (son55; sol's primary agrees). Frozen GPT-4o adapts by conditioning on "
            "retrieved distilled experiences. sol's supporting heterogeneous_decomposition is dropped: dynamics vs skills "
            "is a two-prompt module design, and the paper never characterizes a discriminating property of one resource "
            "that the card requires.")),
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2506.06698-1"): "local:2506.06698-4",
                    ("son55", "local:2506.06698-2"): "local:2506.06698-5"},
            overrides={
                "rsi:abstract_experience_into_guidance/S3": take("son55", p, "rsi:abstract_experience_into_guidance/S3"),
                "local:2506.06698-4": {"reason": "son55 local-1 renumbered (A4 collision with sol local-1). Task order in the "
                                                 "online/hybrid stream and its sensitivity are not reported (status unknown "
                                                 "kept)."},
                "local:2506.06698-5": {"reason": "son55 local-2 renumbered (A4 collision with sol local-2). No multi-run "
                                                 "variance or intervals; subset ablations differ by a few tasks."},
            }),
        "claims": lambda c, p=p: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats. Offline: the buffer is distilled from human-annotated tasks filtered against "
                                   "the test set, frozen, and the same base agent improves 24.3 → 33.4 on the full 812-task "
                                   "WebArena. Online/hybrid learn prequentially from the evaluated stream (no labels in the "
                                   "default loop) and are reported separately. Not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported single runs with GPT-4o in one BrowserGym harness: a retained "
                                         "dynamics+skills buffer raises WebArena success 24.3 → 33.4 (offline, test-disjoint "
                                         "human tasks), 33.2 (online), 36.7 (hybrid) and VisualWebArena to 31.9 (online), at "
                                         "+5.8–17.3% input tokens; failed-trajectory distillation costs about 2 points vs "
                                         "oracle filtering. Not reproduced; no same-condition comparison with AWM/ExpeL.",
            "unresolved": ["Online task order and its sensitivity; multi-run variance.",
                           "Whether distillation/retrieval calls are inside the Table 3 token deltas.",
                           "AWM/ExpeL/Synapse not run under the same harness (neighbour texts not in the fixed material)."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed object (per-task re-exploration without retained "
                   "environment knowledge) and residue (long raw trajectories, reward-gated or rewrite-style memories) are "
                   "named against ExpeL, Synapse, AWM, AutoGuide, AutoManual, Learn-by-interact and Voyager. Not 4: the "
                   "neighbour claims (reward dependence, no retrieval) are not tested and no raw-trajectory baseline checks "
                   "the 'distilled beats raw' residue.",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E004", "sol:E001", "sol:E002"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Separate dynamics/skills distillation with variable abstraction, "
                   "dedupe against the buffer, LLM retrieval and in-context replay form a reconstructable chain with testable "
                   "predictions (cross-template SR, stability/plasticity, per-type ablation). Not 4: no contrastive or "
                   "outcome-grounded distillation, and 'distilled beats raw' is not tested.",
                   ["son55:E005", "son55:E006", "son55:E018", "son55:E021", "sol:E004", "sol:E005"], ["son55:E020"]),
            "X": R("resolved", 3, "Opus sides with son55. Prompts for all four modules (opus:O01), k_d=k_s=5, model snapshot, "
                   "the three settings and the experience format are disclosed; information permissions are explicit (no "
                   "ground-truth reward in the main loop; the oracle-filtered variant is reported separately); write = "
                   "dedupe-append and read = top-k over the whole buffer are unambiguous. Not 4: no admission gate, "
                   "conflict/expiry or rollback (captured by H00 S4/S5), online task order unstated, retrieval cost grows with "
                   "the buffer. sol's 2 treats absent protections as unclear steps; here the steps are clear and the missing "
                   "protections are design limits.",
                   ["son55:E005", "son55:E006", "son55:E013", "son55:E027", "sol:E003", "sol:E023", "opus:O01"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Functional evaluators on the full 812/910 task sets "
                               "with a same-harness reproduced baseline. Not 4: peer numbers come from other harnesses, and "
                               "relative-gain arithmetic is inconsistent (36.7/24.3 = +51.0% in the abstract vs 52.5% in "
                               "Table 3; offline 37.4% vs 37.8%).",
                               ["son55:E010", "son55:E011", "son55:E012", "sol:E008", "sol:E014"], ["son55:E017"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-harness store-off baseline, offline/online/hybrid, "
                             "dynamics/skills ablation, oracle filtering and data-source contrasts; missing raw-trajectory "
                             "replay, random/mismatched experience, retrieval/dedupe ablations and same-condition AWM/ExpeL; "
                             "ablations on the Forum split only.",
                             ["son55:E011", "son55:E020", "son55:E021", "son55:E022", "sol:E016", "sol:E025"],
                             ["son55:E003"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Offline training tasks are human-designed and filtered "
                           "against the test set (~5% of its size) with a frozen buffer: a genuine holdout for the retained "
                           "claim. Online/hybrid learn from the evaluated stream (prequential, no labels) where same-template "
                           "siblings can help; cross-template SR is checked on Forum only; no template-level filter on the "
                           "offline tasks; no contamination analysis.",
                           ["son55:E007", "son55:E008", "son55:E009", "son55:E018", "sol:E009", "sol:E021"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked. Full denominators and negative results (self-guided "
                              "hybrid below online), but no repeated runs, orders or intervals; Forum-subset differences are a "
                              "few tasks. A2 rung 1.",
                              ["son55:E013", "son55:E019", "son55:E021", "sol:E008"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Table 3 gives input-token deltas for all three settings and "
                        "a tree-search token comparison; output tokens are excluded, whether distillation/retrieval calls are "
                        "counted is unclear, 'dozens of times fewer' (intro) vs 'at least 3 times fewer' (§4.2) disagree, and "
                        "human annotation effort is not costed.",
                        ["son55:E014", "son55:E015", "son55:E016", "sol:E019", "sol:E020"], ["son55:E015"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A.1–A.5; in scope (A): a non-weight experience buffer is distilled "
                  "from trajectories, retained and replayed in later tasks; all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "heterogeneous_decomposition dropped: module split, no characterized discriminating property.",
                ["son55:E005", "sol:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["abstract_experience_into_guidance", "H00"]],
                "H00 kept by both. son55's low-fit H02 dropped: H02 needs portable, versioned packages mined from many sources "
                "behind a retention gate (card differentiation); CER appends one agent's own distilled lessons, which is H00.",
                ["sol:E003", "son55:E005"], NOSCORE),
            X(p, "local:2506.06698-1", *C(p, "expectations[local:2506.06698-1].status"), "revised",
              "local-1 = sol's equal-budget raw-memory question → partial; son55's local-1 (task order) renumbered local-4 = "
              "unknown", "A4 collision: same ID, different questions; both verified.", ["sol:E010", "son55:E018"]),
            X(p, "local:2506.06698-2", *C(p, "expectations[local:2506.06698-2].status"), "revised",
              "local-2 = sol's token-coverage question → partial; son55's local-2 (variance) renumbered local-5 = unmet",
              "A4 collision: same ID, different questions; both verified.", ["sol:E019", "son55:E013"]),
            X(p, "local:2506.06698-3", *C(p, "expectations[local:2506.06698-3].status"), "son55", "partial",
              "Verified: the abstract's 51.0% refers to the hybrid setting.", ["son55:E010"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "son55",
              "partial", "Verified: store-off baseline on full benchmark; no random/mismatched-experience control.",
              ["son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55",
              "unmet", "Verified: task-level overlap filter only; no template or pretraining-contamination analysis.",
              ["son55:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "unmet", "Verified: raw-trajectory memory is criticised but not run.", ["son55:E003"]),
            X(p, "rs:adapt_via_conditioning/RE-4", *C(p, "expectations[rs:adapt_via_conditioning/RE-4].status"), "son55",
              "partial", "Verified: dynamics/skills ablated on Forum; retrieval/dedupe not.", ["son55:E021"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55",
              "partial", "Verified: WA + VWA, Llama on Gitlab only; web navigation only.", ["son55:E025"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "son55",
              "met", "Verified: Tables 7 and 9 characterize trajectory-quality sensitivity.", ["son55:E020", "son55:E022"]),
            X(p, "rsi:abstract_experience_into_guidance/F2",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/F2].status"), "son55", "partial",
              "Verified: web domain, but the dynamics/skills split and three settings go beyond the generic signature.",
              ["son55:E007"]),
            X(p, "rsi:abstract_experience_into_guidance/H00",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/H00].status"), "sol", "partial",
              "Verified: offline buffer disjoint and frozen; online stream updates separately reported.", ["sol:E009"]),
            X(p, "rsi:abstract_experience_into_guidance/S1",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S1].status"), "son55", "met",
              "Verified: names the specific fixed object (no retained environment knowledge), not frozen weights.",
              ["son55:E002"]),
            X(p, "rsi:abstract_experience_into_guidance/S2",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"), "son55", "unmet",
              "Verified: per-trajectory narration, no success/failure contrast.", ["son55:E005"]),
            X(p, "rsi:abstract_experience_into_guidance/S3",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "son55", "unmet",
              "S3 asks for a grounding signal that decides what becomes a lesson; in the default loop nothing decides "
              "(success and failure trajectories are both distilled; only dedupe), and the oracle-filtered variant is a "
              "separate ablation. Observation-grounded content (sol's partial) does not meet the 'decides' condition.",
              ["son55:E020", "sol:E018"]),
            X(p, "rsi:abstract_experience_into_guidance/S4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "son55", "partial",
              "Verified: dedupe only; no forgetting/conflict handling.", ["son55:E005", "sol:E023"]),
            rr(p, "X", "son55", 3, "See ratings.X: fully specified write/read rules and permissions; missing protections are "
                                   "design limits scored once here (not 4).", ["opus:O01", "son55:E027"],
               "+5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first: ungated dedupe-append buffer; offline buffer from "
                                                   "test-disjoint human tasks; online/hybrid prequential on the evaluated "
                                                   "stream with same-template siblings; single runs; input tokens only.",
            "integrity_checks": "Both seats a1 on 2506.06698v1, material sha 796760ec…; hashes equal conflicts.json; full "
                                "identification by both.",
            "core_claim_check": "Tables 1, 3, 7–9 re-read; relative-gain arithmetic inconsistency noted (both seats saw it).",
            "rating_agreement": "7 of 8 agreed and re-verified; X resolved for son55.",
            "neighbour_material": "AWM/ExpeL/Synapse full texts are not in the fixed package; no request filed because G=3 "
                                  "and E.causality=2 already reflect the untested neighbour claims and would not change "
                                  "with the texts alone (a same-condition run would be needed).",
        },
    }

    return S


def batch_notes():
    return [
        "2506.06254 PersonaAgent (controller flag): Algorithm 1's 'Test User data D' read against Eq. (1) and Appendix G — "
        "'Test User' is a member of the 100-user test population, D is the episodic-buffer symbol for past interactions, the "
        "batch is the latest n=3 interactions, and the later test split is 'reserved for final evaluation'. Ruled "
        "profile-sourced with residual ambiguity (no explicit disjointness statement; §3.7 deployment re-alignment): "
        "E.holdout=2 (sol), evidence_level corrected to retained for both seats.",
        "2505.18524 metaTextGrad: §4.1 puts the ADAS-TG baseline on o1, so son55's 'no same-model optimizer control' is "
        "corrected; E.cost=1 because meta/inner iteration counts are never instantiated.",
        "2506.04651 HexMachina: final 52.5 is below both seats (M→son55, X/E.holdout→sol). Table 3 'No Strategist + "
        "Researcher' equals the 10×100 stress-test value and is not attainable under the stated 3×30-game protocol; adapters "
        "expose AlphaBeta's own chance-expansion/pruning primitives. No figure values used.",
        "2505.20286 Alita: two hidden A4 collisions (local-1, local-2; equal status, different questions) renumbered and "
        "recorded; oracle pass@k scored under E.holdout only (A2).",
        "2506.06698 CER: only X conflicted; neighbour texts (AWM/ExpeL/Synapse) not requested because no rating depends on "
        "them beyond what the pinned text shows.",
        "E.cost consistency within the batch: 1 where the improvement-loop budget is not reconstructable (metaTextGrad, "
        "HexMachina), 2 where it is bounded/derivable or reported as token deltas (PersonaAgent, CER), 0 not_reported for "
        "Alita.",
        "No card revision proposals; no requests for new material.",
    ]
