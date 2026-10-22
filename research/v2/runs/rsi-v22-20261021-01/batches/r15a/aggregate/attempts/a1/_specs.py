"""Opus rulings for r15a a1 (data only; consumed by _build.py)."""
import copy

NOSCORE = "none (patterns never score)"
NOEXP = "none (expectations are not scored directly)"


def batch_notes():
    return [
        "2604.01480 metasurface skill evolution (seat Δ2.5, both on a3/v3 = text + 21 page images): final 56.25. "
        "E.holdout → son55 2. Test templates are held out and the test split never selects. But the Same-type test uses "
        "sibling templates that differ only in task instances. New-type-B's validation family shares the test class, "
        "and the authors themselves call it within-class learning. New-type-A is the only cross-class split, and it "
        "shows no gain. Validation summaries also feed the meta-agent's revisions. Opus page-image finding (shared "
        "correction, no rating change): the starter skill already reads a cross-iteration memory "
        "(context/strategy_summary.md mirrored from meta_agent/strategy_summary.md). The evolved iter-1 SKILL.md is a "
        "training-phase protocol: it loads data/train.json, writes context/ files and writes a solution per training "
        "sample. S1's 'single SKILL.md + static reference/' inventory therefore omits retained state present in both "
        "arms, and the test-time procedure is never stated. RS → adapt_via_conditioning primary + "
        "decompose_and_delegate/C25 (the solver-programming inner loop). Domain → son55 (H10 whole-document rewrite "
        "from diagnosed errors + H31).",
        "2604.01687 CoEvoSkills (seat Δ3.75): final 58.75, G → sol 2. The paper frames its gap as working 'without "
        "ground-truth', yet every reported task consults its own hidden tests as a pass/fail oracle up to K=5 times. "
        "The best-oracle snapshot is kept, and that same task's tests score the deployed skill. This is a weaker "
        "held-out position than EvoSkill's held-out validation, the neighbour it criticises, so the residual gap is "
        "not bounded. Both seats had E.holdout 1 and evidence_level task; both kept. Opus count finding (shared, no "
        "rating change): App. B reports 10 of 85 evolution tasks failing the oracle, about 88% oracle-pass. That is "
        "unreconciled with Fig. 2's 75% at round 5 and the 71.1% deployed headline. Domain → son55 (H25 + H02; H02's "
        "own failure clause, 'building on-demand skills for the very workflows used for evaluation', applies).",
        "2604.03964 SkillFoundry (seat Δ10): final 43.75. All five rating conflicts resolve to son55 on independent "
        "reading. M 2: retention signals measure executability and keyword novelty, not usefulness, and the layer-2 "
        "utility benchmark has no reported cases or results. E.measurement 2: library validity and 71.1% novelty are "
        "self-judged. E.causality 1: the only manipulation is skills vs no skills; there is no alternative "
        "documentation/library control and no ablation of tree, validation or novelty. E.holdout 2: MoSciBench is "
        "external but has no overlap audit, and on-demand skills are built for the evaluated task. E.statistics 1: the "
        "main benchmark is a single run with unreported per-dataset n. Opus finding (shared correction): 'five of six "
        "datasets' holds only under Paper-Acc. Under the official-repo Repo-Acc, four of six improve (nurse stress and "
        "terra are unchanged). The inferred Repo gain is about 54→59 of 88 items.",
        "2604.04347 RoboPhD (seat Δ2.5): final 67.5, E.holdout → son55 3. Four fixed train/test splits are used "
        "identically across engines, and the final agent is chosen by training-sample Elo only. The test-informed "
        "choice (baselines' validation size 100) favours the baselines. RoboPhD's Text2SQL origin and model "
        "contamination remain unaudited, which keeps it below 4. RS → son55 (assumption_audit_and_pivot: the "
        "validate-then-select premise is the audited assumption). Domain revised to H14 + H32. H16 is rejected: an "
        "Elo-ranked population with noise-injection diversity names no frontier or complementarity axis. The "
        "Elo-vs-KotH tally is 2:2, so validation-free Elo itself is not isolated; both seats and the authors say so.",
        "2604.04804 SkillX (seat Δ7.5): final 48.75, same total as sol with a different composition. X → sol 2: the "
        "abstract's 'generates and validates novel skills' has no stated validation for synthesized tasks, Eq. 7's "
        "union conflicts with modify/merge, and the 'execution-feedback refinement' re-extracts successful "
        "trajectories only. E.holdout → sol 1: Eq. 8 explicitly stops refinement on test performance, and the GLM-4.6 "
        "'SkillX' row equals the best test row per benchmark (Vanilla-Iter2 for BFCL, Expand-Iter3 for AppWorld). "
        "E.statistics → son55 1 (Avg@4 means with no dispersion; ~1-point margins called consistent). E.cost → son55 "
        "2 (inference tokens/steps analysed; construction budget unreported), consistent with 2604.01480. Shared "
        "corrections: retained rests only on Vanilla-Iter1 (no test-based choice), and §6.1's 'consistent gains' is "
        "contradicted by GPT-4.1 Self-Extract Pass@4 (BFCL 58.39→56.67; AppWorld 82.74→82.14). Domain revised to "
        "H02 + H23. H01 is dropped because H02 already covers merge/versioning.",
        "A4 hygiene: hidden local-ID collisions renumbered: 2604.01480 son55 local-2/3/4 → local-3 (merged)/7/8; "
        "2604.01687 son55 local-1 → local-3; 2604.03964 son55 local-1 → local-4; 2604.04347 son55 local-1 → local-5 "
        "with son55 local-3 merged into sol local-1 (same question); 2604.04804 sol local-1 → local-5. "
        "'challenged_with_evidence' is reserved for a paper that presents evidence against a conventional "
        "expectation (kept for RoboPhD S3). Where a seat used it to mean 'we challenge the paper' (01480 son55 "
        "local-4, 01687 son55 local-2, 04804 sol local-1), the status was revised to unmet/partial.",
        "Figure dependence: 2604.01480 Figs 2–3 and S7 were opened as page images (p-06, p-07, p-17…p-21); the "
        "values used are those also stated in the text. 01687 Figs 2/4/5/6/B1, 03964 Figs 2–4, 04347 Fig 1 and 04804 "
        "Fig 3 are image-only and not in the package. Only prose/table values are used, and no figure value is "
        "invented.",
        "No material requests: every disputed field was answerable from the pinned packages. Nearest-neighbour full "
        "texts (MCE/ACE, EvoSkill, SkillHub/SkillSMP, GEPA/Autoresearch originals, AWM/ExpeL) are not in the "
        "packages; G already records the uncompared neighbours, so none blocks a rating.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, opus_img_ev, merge_exps = (g["R"], g["res"], g["conflict"], g["opus_ev"],
                                                         g["opus_img_ev"], g["merge_exps"])
    seat, prefix = g["seat"], g["prefix"]
    g["PAGES_READ"].update({"2604.01480": {
        "p-06.png": "Table 1 + §3.2–3.3 text", "p-07.png": "Figs 2–3 (rescued/regressed, cost boxes, validation curves)",
        "p-17.png": "Table S5 + Listing S7.1 start", "p-18.png": "Listing S7.1 end + S7.2 start",
        "p-19.png": "Listing S7.2 Steps 2–6", "p-20.png": "Listing S7.2 API reference",
        "p-21.png": "Listing S7.2 strategy table, principles, checklist"}})
    S = {}

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
            if (m.get("main") or m.get("main_id")) == main and (m.get("sub") or m.get("sub_id")) == sub:
                m2 = prefix(copy.deepcopy(m), s)
                m2.update(upd)
                return m2
        raise KeyError((s, p, main, sub))

    def pm(s, p, idx=None):
        maps = seat(s, p)["pattern_mapping"]
        if idx is not None:
            maps = [maps[i] for i in idx]
        return [prefix(copy.deepcopy(m), s) for m in maps]

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def kept(s, p, k, reason, ev, cev=()):
        r = seat(s, p)["ratings"][k]
        return R(r["status"], r["rating"], reason, ev, cev, r.get("search_scope") or ())

    def a4(field, sol_v, son_v, final, reason, ev):
        return {"field_path": field, "sol_value": sol_v, "son55_value": son_v, "final_value": final,
                "reason": reason, "evidence_ids": ev, "score_impact": "none"}

    # =========================================================== 2604.01480 metasurface (sol 58.75 / son55 56.25)
    p = "2604.01480"
    S[p] = {
        "base": "son55",
        "figure_dependence": "Figs 2–3 and the S7 listings were read from pinned page images p-06/p-07/p-17…p-21. "
                             "Fig. 2/3 values used are also stated in the text.",
        "a3": "none (in scope: non-weight SKILL.md evolved from solver feedback, base model and solver fixed)",
        "opus_evidence": [
            opus_ev(p, "O01", "Once a skill-evolution iteration finishes, the meta-agent inspects the per-task records "
                              "and validation summaries to revise the current skill files.", "§2.1",
                    "The selection split's results reach the proposer. Validation is therefore not a sealed commit "
                    "split (relevant to E.holdout and the H31 S2 check)."),
            opus_ev(p, "O02", "This representation makes explicit that the evolving core is a single", "App. S1",
                    "S1 states the retained inventory as one SKILL.md plus a static reference/ subtree and archives; "
                    "contrast opus:I01–I03."),
            opus_img_ev(p, "I01", "p-18.png",
                        "If a `context/` directory exists, treat it as optional learned guidance. Read "
                        "`context/strategy_summary.md` first when present. It is the cross-iteration memory mirrored "
                        "from `meta_agent/strategy_summary.md`, so use it to anchor durable strategy choices before "
                        "consulting batch-local context.",
                        "Listing S7.1 (starter skill, iter0), '## Optional Context'",
                        "Even the STARTER skill reads a cross-iteration memory file that S1 never lists. A retained "
                        "channel besides SKILL.md therefore exists in the baseline arm too. The starter-vs-evolved "
                        "contrast is not 'no retained state vs retained SKILL.md', and strategy_summary contents in "
                        "either arm are unreported."),
            opus_img_ev(p, "I02", "p-19.png",
                        "### Step 2: Load and Parse Training Results\nLoad `data/train.json`. For each sample, extract:",
                        "Listing S7.2 (evolved skill, iter1), Methodology Step 2",
                        "The evolved file is a training-phase context-engineering protocol: it reads training results "
                        "(§2 per-task records)."),
            opus_img_ev(p, "I03", "p-19.png",
                        "### Step 5: Write the Solution for Each Training Sample\nFor each sample in the current batch "
                        "(task-environment will call you once per sample), write `solution.py` that:",
                        "Listing S7.2 (evolved skill, iter1), Methodology Step 5",
                        "With Step 6 ('Commit updated context files so they carry forward', sol:E10), this shows the "
                        "evolved file is written for training batches. How it is executed on the 50 test tasks "
                        "(whether data/train.json/context/ are present, and whether test outcomes are written back "
                        "across test tasks) is never stated.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["decompose_and_delegate"],
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", role="primary",
                       reason="Opus confirms sol's primary. The headline operation conditions a frozen coding agent on "
                              "a rewritten, validation-selected text file; no weights change (son55:E001). C03 is not "
                              "assigned: there is no retrieved reference substrate or trained parser (both seats). Run "
                              "convention for frozen-model text-artifact evolution: r08a EvoTest."),
                smatch("son55", p, "decompose_and_delegate", role="supporting",
                       reason="Supporting, as son55 proposed: the LLM emits an executable optimization program that a "
                              "sound solver/evaluator executes, with per-criterion margins closing the loop (Algorithm "
                              "1; son55:E026, E027). C25's 'solver by-products as reusable capital' is what the outer "
                              "loop does. It is not primary, because the paper's contribution is the skill-file "
                              "evolution, not the delegation boundary (inherited from the authors' MCP work [20])."),
            ],
            "outside_taxonomy": False,
            "reason": "Two executed operations: frozen-model conditioning on an evolving text artifact (primary), and "
                      "an LLM-program → physics-solver delegation loop whose by-products feed the artifact "
                      "(supporting C25).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H10"),
                                       dmatch("son55", p, "evidence_gated_retention", "H31")],
                           "unassigned": [{"candidate": "H00", "reason": "Opus: the paper's described operation is a "
                                           "meta-agent rewriting one incumbent file from per-task error/criterion "
                                           "records with elitist validation (H10's tell). H00's append-a-lesson store "
                                           "describes only the inner context/ protocol inside the evolved file "
                                           "(opus:I02), which the paper does not present as its mechanism."},
                                          {"candidate": "H11", "reason": "No defect-vs-lapse attribution (son55)."}],
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("son55", p),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.01480-2"): "local:2604.01480-3",
                    ("son55", "local:2604.01480-3"): "local:2604.01480-7",
                    ("son55", "local:2604.01480-4"): "local:2604.01480-8"},
            overrides={
                "local:2604.01480-1": {"status": "unmet", "reason": "Opus (son55; sol local-1 merged, same question). "
                                       "Only the minimal starter skill is compared. There is no expert-written skill, "
                                       "no full-documentation injection, no other improver and no budget-matched "
                                       "alternative (son55:E014, E032)."},
                "local:2604.01480-3": {"status": "partial", "reason": "Opus (sol; son55 local-2 'variance' merged here "
                                       "as the same E.statistics question). n=50 and paired rescued/regressed counts "
                                       "are reported, plus a negative transfer result. There is a single evolution "
                                       "trajectory per setting, with no seeds, intervals or variance."},
                "local:2604.01480-5": {"status": "unmet", "reason": "Opus (revised; sol partial / son55 unknown, same "
                                       "question). The inventory is demonstrably incomplete, not merely unknown. S1 "
                                       "lists SKILL.md + static reference/ (opus:O02). The starter reads "
                                       "meta_agent/strategy_summary.md memory (opus:I01). The evolved file writes "
                                       "context/ and works on data/train.json (opus:I02, I03). Test-time carry-over "
                                       "is never stated."},
                "local:2604.01480-8": {"status": "unmet", "reason": "Opus (revised from son55 "
                                       "'challenged_with_evidence', renumbered from son55 local-4). The paper does not "
                                       "challenge the isolation expectation; it fails it and then scopes the B claim "
                                       "honestly (son55:E006, E017, E018; opus:O01)."},
                "rsi:abstract_experience_into_guidance/S2": {"status": "partial", "reason": "Opus (revised from sol "
                                       "'met'). The success/failure contrast appears as instructions inside the "
                                       "evolved file (sol:E09). The meta-agent's own rewrite procedure is delegated to "
                                       "[21] and not shown contrasting outcomes."},
                "local:2604.01480-7": {"note": "A4: son55 local-3 (evaluator re-checks physical context) renumbered."},
            }),
        "claims": lambda c: add_counter(c, "C5", ["opus:I01", "opus:I02", "opus:I03"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats retained; kept. A validation-selected SKILL.md (with whatever context "
                                   "state it carries) improves 50 test tasks from templates never used for training "
                                   "or selection (Same-type, New-type-B). New-type-A shows no gain. Not improver: the "
                                   "meta-agent is fixed.",
            "claim_support": "scoped",
            "strongest_supported_claim": "With Claude Sonnet 4.6 and TorchRDIT fixed, one validation-selected evolved "
                                         "skill package raises single-run test SG on held-out sibling templates from "
                                         "19/50 to 37/50 (18 rescued, 0 regressed) and on New-type-B from 10/50 to 45/50. "
                                         "Validation there exposes the test device class (within-class acquisition). "
                                         "On the only cross-class split, A, it gives no gain (one rescued, two "
                                         "regressed). Gains are not attributed to skill content versus the auxiliary "
                                         "context/strategy memory.",
            "unresolved": ["Test-time handling of context/ and meta_agent/strategy_summary.md (opus:I01–I03).",
                           "Evolution-phase cost and R/A caps.",
                           "No alternative improver, expert skill or documentation-injection control.",
                           "Single evolution run per setting."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 2; re-checked. The fixed object (solver tactics not retained, "
                      "son55:E003) and the direct MCE lineage (son55:E004) are clear. Novelty is a domain application "
                      "(son55:E005), and MCE/ACE/EvoTest neighbours are cited but not compared.",
                      ["son55:E003", "son55:E004", "son55:E005", "son55:E021", "sol:E01"]),
            "M": kept("son55", p, "M", "Both seats 3; re-checked. The chain is reconstructable: per-task records → "
                      "rewrite → lexicographic validation ranking → strict-improvement replacement → reuse "
                      "(son55:E006–E008, sol:E02). The A/B role swap is a distinguishable prediction (class convention "
                      "missing vs present; son55:E047). Not 4: no content attribution or comparison with a naive "
                      "alternative, and the starter already carries a strategy portfolio (son55:E034).",
                      ["son55:E006", "son55:E007", "son55:E008", "son55:E027", "son55:E047", "sol:E02"],
                      ["son55:E034"]),
            "X": kept("son55", p, "X", "Both seats 2; kept, with an Opus shared correction to the reason. The "
                      "retention gate, tie order, archive and restart-from-best are specified (son55:E008, E024, "
                      "E025). The persisted state is inconsistent with the paper's own inventory. S1 says single "
                      "SKILL.md + static reference/ (opus:O02), but the starter already reads a cross-iteration "
                      "strategy_summary memory (opus:I01), and the evolved file is a training-phase protocol over "
                      "data/train.json that writes context/ (opus:I02, I03; son55:E038). The test-time execution of "
                      "that protocol is unstated. This is anchor 2 (key retention/interface condition unclear), not 1: "
                      "the outer loop itself is reconstructable.",
                      ["son55:E008", "son55:E024", "son55:E025", "son55:E036", "sol:E08", "opus:O02", "opus:I01",
                       "opus:I02", "opus:I03"], ["son55:E038", "son55:E045"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; re-checked. A deterministic physics "
                                  "evaluator outside the agent with machine-checkable criteria (son55:E026, sol:E15) "
                                  "and attainable-optimum families (son55:E030) is credible. Not 4: whether the "
                                  "evaluator re-imposes the task's physical context or trusts the candidate-built "
                                  "SolverResults is unstated (son55:E043), BM assigns 0 to failed executions "
                                  "(son55:E028), and there is a single solver.",
                                  ["son55:E026", "son55:E030", "sol:E15"], ["son55:E028", "son55:E043"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 2; re-checked. Same-model, same-solver, "
                                "same-test starter-vs-evolved pairs with rescued/regressed counts (son55:E014, E015) "
                                "and the A/B swap are relevant. Missing: content ablation, expert/doc-injection/"
                                "alternative-improver controls, and a gate-off run. Opus adds that both arms carry a "
                                "cross-iteration memory channel of unreported content (opus:I01), so the arms differ "
                                "by more than the SKILL.md text.",
                                ["son55:E014", "son55:E015", "son55:E044", "sol:E05"],
                                ["son55:E017", "son55:E018", "opus:I01"]),
            "E.holdout": R("resolved", 2, "Opus → son55 2 (sol 3). For: template-level disjoint 50/15/50 splits, test "
                           "never used for selection (son55:E010–E012, sol:E03). Against, for the central transfer "
                           "claim: Same-type tests are siblings that 'differ only in task instances' (son55:E029). B's "
                           "validation family shares the test class and its summaries reach the proposer (opus:O01, "
                           "son55:E017, E018). A, the one cross-class split, shows no gain (son55:E020). Test-time "
                           "context carry-over is unstated (opus:I03). Anchor 3 needs a clean held-out test of the "
                           "claimed transfer; the evidence supports only near-distribution and validation-exposed "
                           "transfer. These are limits rather than shown contamination, so 2, not 1.",
                           ["son55:E010", "son55:E011", "son55:E012", "sol:E03", "sol:E04"],
                           ["opus:O01", "son55:E017", "son55:E018", "son55:E020", "son55:E029", "opus:I03"]),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 1; A2 ladder re-checked. n=50 per split, "
                                 "paired rescue/regression counts and a negative A result are reported. There is a "
                                 "single evolution trajectory and test run per setting, with no intervals or seeds.",
                                 ["son55:E014", "son55:E015", "sol:E05", "sol:E06"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 2; re-checked. Test-time median $/task and attempts are "
                           "reported numerically (son55:E016, sol:E07). Meta-agent, 4×50 training and validation "
                           "evaluation costs are not, so there is no break-even.",
                           ["son55:E016", "sol:E07"], ["son55:E013"]),
        },
        "status": "reviewed",
        "reason": "Pinned v3 package read: full text plus 21 page images (S7 listings and Figs 2–3 opened). In scope: "
                  "a non-weight skill file evolved from solver feedback is retained and reused. claim_type "
                  "system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "See rs_pattern.reason. The contribution is conditioning a frozen agent on an evolving file; C25 "
                "describes the inherited inner loop, so it is supporting.", ["son55:E001", "son55:E026"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "Final set equals son55's, with roles swapped (adapt primary). C25 is executed: program → solver → "
                "per-criterion margins (Algorithm 1).", ["son55:E026", "son55:E027"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["attribute_and_patch_incumbent", "H10"], ["evidence_gated_retention", "H31"]],
                "H10's tell fits: one textual incumbent, rewritten from verbalizable errors, best kept on a disjoint "
                "split. H00 is rejected as primary: its append-lesson store describes only the inner protocol inside "
                "the evolved file (opus:I02).", ["son55:E007", "son55:E008", "opus:I02"], NOSCORE),
            XC(p, "local:2604.01480-1", "son55", "unmet", "Same question in both seats (attribution vs alternatives); "
               "merged. No alternative improver, expert skill or doc-injection control: unmet, not partial.",
               ["son55:E014", "son55:E032"]),
            XC(p, "local:2604.01480-2", "sol", "partial", "A4 collision: sol local-2 = generalization beyond "
               "development families (kept, partial); son55 local-2 = variance (merged into local-3).",
               ["sol:E03", "sol:E04", "son55:E017"]),
            XC(p, "local:2604.01480-3", "sol", "partial", "A4 collision: final local-3 = sol's statistics question, "
               "merged with son55 local-2. son55 local-3 (evaluator physical-context check) moved to local-7 and keeps "
               "'unknown'.", ["sol:E05", "son55:E043"]),
            XC(p, "local:2604.01480-4", "sol", "partial", "A4 collision: final local-4 = sol's cost question (partial: "
               "test $ reported, evolution cost not). son55 local-4 (isolation) moved to local-8 and revised to unmet.",
               ["sol:E07", "son55:E016"]),
            XC(p, "local:2604.01480-5", "revised", "unmet", "Same question in both seats. The inventory is shown to be "
               "incomplete (opus:O02 vs opus:I01–I03), which is unmet rather than partial/unknown. Test-time "
               "carry-over remains unstated.", ["opus:O02", "opus:I01", "opus:I02", "opus:I03"]),
            XC(p, "local:2604.01480-6", "son55", "unknown", "Verified: no contamination analysis of TorchRDIT/"
               "reference examples.", ["son55:E030"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet", "Verified: no cheaper conditioning (full docs, "
               "longer context) compared; reference/ is static in both arms.", ["son55:E023"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial", "Verified: the A/B swap is a one-off coverage-"
               "sensitivity probe.", ["son55:E017", "son55:E020"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial", "Verified: test cost only.", ["son55:E016"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet", "Verified: no ablation of retries, evaluator "
               "feedback or skill content.", ["son55:E014"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "partial", "Verified: snapshots and task JSON given; code "
               "deferred; meta-agent prompt delegated to [21].", ["son55:E031", "son55:E023"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial", "Verified: one solver, one base model, "
               "RCWA families only.", ["son55:E021"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial", "Verified: the baseline is the same pipeline "
               "with the starter skill only.", ["son55:E014", "son55:E003"]),
            XC(p, "rs:decompose_and_delegate/RE-6", "son55", "partial", "Verified: error taxonomy and baseline SE/CPF "
               "indicate the bottleneck; no dedicated diagnosis.", ["son55:E003", "son55:E019"]),
            XC(p, "rsi:abstract_experience_into_guidance/S1", "sol", "met", "Kept as a check question (H00 not "
               "adopted). The previously unretained object is named.", ["sol:E01", "sol:E08"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "revised", "partial", "Contrast is instructed inside "
               "the evolved file, not shown in the meta-agent's rewrite.", ["sol:E09"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "partial", "Verified: versioning exists, no "
               "conflict/forgetting protocol.", ["sol:E08", "sol:E10"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F1", "son55", "partial", "Verified: an MCE loop ported to a new "
               "domain, with a domain-specific physics evaluator and A/B design.", ["son55:E004", "son55:E005"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "met", "Verified: deterministic external "
               "evaluator.", ["son55:E026"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "unmet", "Verified: no defect-vs-lapse separation "
               "or repeated runs.", ["son55:E015"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "unknown", "Verified: edit granularity is not "
               "described (whole-file rewrite; [21]).", ["son55:E023"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial", "Verified: elitist whole-file gate, 15 "
               "validation tasks; A regresses two tasks.", ["son55:E008", "son55:E015"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "partial", "Verified: grouping is instructed in "
               "S7; the meta-agent's clustering is not shown.", ["son55:E036", "son55:E037"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met", "Verified: the proposer sees raw per-task "
               "records.", ["son55:E007"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "partial", "Verified: generality claimed, one "
               "stack instantiated.", ["son55:E046", "son55:E021"]),
            XC(p, "rsi:evidence_gated_retention/H31", "sol", "partial", "Verified (sol's step-level summary): a "
               "strict-improvement elitist incumbent, but validation summaries reach the proposer (opus:O01) and "
               "there is no error-controlled rule.", ["sol:E02", "opus:O01"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "partial", "Verified: aggregate on/off pair only.",
               ["son55:E014"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "unmet", "Verified: no gate-off run; on Same-type "
               "validation saturates at iteration 1.", ["son55:E019"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "unmet", "Verified: gate cost not reported.",
               ["son55:E012"]),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.holdout. The held-out evidence for the central transfer claim is near-distribution "
                "(Same-type) or validation-exposed (B), and the clean cross-class split (A) shows no gain. sol's own "
                "reason lists these limits without crediting them.",
                ["son55:E029", "son55:E018", "son55:E020", "opus:O01"], "-2.5 (58.75 → 56.25)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.X.reason", "sol_value": "2 (auxiliary context persistence unclear)",
             "son55_value": "2 (context/ written by evolved skill; S1 inconsistent)", "final_value": 2,
             "reason": "Both seats located the extra persistence in the evolved file's context/ writes. Neither noted "
                       "that the STARTER skill already reads a cross-iteration memory mirrored from "
                       "meta_agent/strategy_summary.md (opus:I01), so both arms carry an unlisted retained channel. "
                       "Neither noted that the evolved file is a training-phase protocol (data/train.json, one "
                       "solution per training sample; opus:I02, I03) whose test-time execution is never described. "
                       "This affects interpretation of E.causality, but no rating moves.",
             "evidence_ids": ["opus:I01", "opus:I02", "opus:I03"], "score_impact": "none"},
            a4("expectations[local:2604.01480-*].id", "local-1 attribution; -2 generalization; -3 statistics; "
               "-4 cost; -5 inventory", "local-1 alternatives; -2 variance; -3 evaluator context; -4 isolation; "
               "-5 inventory; -6 contamination",
               "local-1 (merged), -2 sol, -3 sol+son55 local-2 (merged), -4 sol, -5 (merged), -6 son55, "
               "-7 = son55 local-3, -8 = son55 local-4",
               "A4 hidden ID collisions; renumbered and merged by question.", ["sol:E05", "son55:E043"]),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text and opened the S7 listings and Figs 2–3 before "
                                                   "the seat records. In scope; system_method; retained. Same-type and "
                                                   "B gains are on held-out templates, but B's validation shares the "
                                                   "test class and A shows no gain. Both skill files reference "
                                                   "context/strategy memory beyond S1's inventory. Single run; "
                                                   "evolution cost unreported. Expected G2 M2–3 X2 Em3 Ec1–2 Eh2 Es1 "
                                                   "Ecost2.",
            "integrity_checks": "Both seats a3 under overrides.json, input_hash 2e171db8… (v3 package); a1 not read. "
                                "Canonical seat hashes equal conflicts.json. Text sha 445d5237… and the 21 page-image "
                                "shas match the pinned manifest. Both completed 15+31 with valid parents.",
            "core_claim_check": "Table 1, the rescued/regressed counts and the costs recompute from text and images. "
                                "The abstract's 'new-type families' headline is scoped by the body (B within-class).",
            "rating_agreement": "Seven of eight items agree and were re-derived; E.holdout resolved to 2.",
        },
    }

    # =========================================================== 2604.01687 CoEvoSkills (sol 58.75 / son55 62.5)
    p = "2604.01687"
    S[p] = {
        "base": "son55",
        "figure_dependence": "Figs 2/4/5/6/B1 are image-only; only prose/table values are used (Table 3, Table A1, "
                             "App. B/C text).",
        "a3": "none (in scope: non-weight multi-file skill packages evolved from execution/verifier feedback)",
        "opus_evidence": [
            opus_ev(p, "O01", "The 10 tasks that failed to achieve a perfect Ground Truth Oracle score cluster at "
                              "higher iteration counts", "App. B",
                    "Of 85 evolution tasks, 10 fail the oracle, so about 75/85 ≈ 88% reach oracle pass during "
                    "evolution.", kind="our_inference"),
            opus_ev(p, "O02", "converging at 75% by round 5", "§4.5 (Fig. 2 prose)",
                    "Fig. 2's round-5 pass rate (75%) is not reconcilable with opus:O01 (~88%) or with the 71.1% "
                    "deployed headline without a stated denominator or condition difference."),
            opus_ev(p, "O03", "reports the distribution of verification cycles and Ground Truth Oracle rounds across "
                              "85 evolution tasks.", "App. B",
                    "85 evolution tasks are counted, alongside 'We exclude two tasks' (son55:E018). Whether 85 is "
                    "before or after exclusion is unstated."),
            opus_ev(p, "O04", "The evolved skills are structured multi-file packages installed before agent test.",
                    "App. A (ablation setting 1)",
                    "The deployed skill is installed for the same task whose hidden tests gated evolution (son55:E002, "
                    "E003)."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering",
            "supporting": ["decompose_and_delegate"],
            "matches": [
                smatch("sol", p, "self_supervised_signal_engineering", role="primary",
                       reason="Opus confirms sol's primary. The paper's core move manufactures a dense supervision "
                              "signal (verifier-synthesized assertions) where only an opaque bit exists. No C07/C08/"
                              "C26 tactic fits (no internal statistics, synthetic training set or preference "
                              "training), so sub=null."),
                smatch("son55", p, "decompose_and_delegate", role="supporting",
                       reason="Supporting: generator artifacts are routed to a separate checker whose executable "
                              "assertions close the loop mid-construction, and the verification step is ablated "
                              "(son55:E006). generative_process_redesign is dropped: iterative generate-verify-refine "
                              "is not the conventionally fixed artifact being freed."),
            ],
            "outside_taxonomy": False,
            "reason": "Surrogate supervision construction (primary) plus a generator→checker delegation loop with "
                      "ablated verification (C25 supporting).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "coevolve_the_evaluator", "H25"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H02",
                                              fit="low-moderate (portable skill packages from task docs and "
                                                  "feedback; H02 step-5 failure applies: skills are built for the "
                                                  "very tasks scored)")],
                           "unassigned": [],
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("son55", p),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.01687-1"): "local:2604.01687-3"},
            overrides={
                "local:2604.01687-2": {"status": "unmet", "reason": "Opus (revised from son55 "
                                       "'challenged_with_evidence'). The paper does not challenge like-with-like "
                                       "comparison; it compares task-specific, oracle-gated packages with generic "
                                       "human documentation (son55:E019, E020), so the expectation is unmet."},
                "rsi:abstract_experience_into_guidance/S5": {"status": "partial", "reason": "Opus (revised from son55 "
                                       "'met'). A deployment gate exists (surrogate + oracle), but it is the target "
                                       "task's own hidden test, not a reuse gate (son55:E003)."},
                "local:2604.01687-3": {"note": "A4: renumbered from son55 local-1 (results on tasks not used for "
                                       "oracle-gated selection; unmet)."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02", "opus:O03"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats task; kept. Each skill is evolved per task with up to five pass/fail "
                                   "queries of that task's hidden tests, the best-oracle snapshot is kept, and the "
                                   "same tests score it. EVIDENCE rule 2: selection set ≠ held-out → at most task. "
                                   "Cross-model transfer is on the same tasks.",
            "claim_support": "scoped",
            "strongest_supported_claim": "On 85 SkillsBench tasks, per-task skill packages evolved with an isolated "
                                         "surrogate verifier plus ≤5 opaque oracle bits on the same task raise a fresh "
                                         "Opus-4.6 agent's pass rate on those tasks (71.1% vs 30.6% no-skill, 5 runs). "
                                         "A single-run ablation attributes ~30pp to the verifier's dense diagnostics "
                                         "over oracle-bit-only evolution. Unseen-task benefit and the 'better than "
                                         "human skills' comparison are not established on like-for-like terms.",
            "unresolved": ["Results on tasks not used for oracle-gated selection.",
                           "Reconciliation of ~88% oracle-pass (App. B), 75% (Fig. 2) and 71.1% deployed.",
                           "Surrogate–oracle agreement statistics; token/dollar cost."],
        },
        "ratings": {
            "G": R("resolved", 2, "Opus → sol 2 (son55 3). The bottleneck (single-pass multi-file skills unreliable; "
                   "uneven human skills) is real and sourced (son55:E013, E014). But the gap is framed as working "
                   "'without ground-truth' and against EvoSkill's GT use (son55:E012), while the method itself "
                   "consults each target task's hidden oracle up to 5 times and keeps the best snapshot "
                   "(son55:E002, E021). That is a weaker held-out position than the held-out validation it "
                   "criticises, so the residual gap over the nearest neighbour is not bounded. EvoSkill is not run. "
                   "Not 1: the multi-file packaging problem is concrete.",
                   ["sol:E01", "son55:E012", "son55:E013", "son55:E014"], ["son55:E002", "son55:E021"]),
            "M": kept("son55", p, "M", "Both seats 3; re-checked. Isolated verifier → dense diagnostics → repair, with "
                      "escalation only on surrogate-pass/oracle-fail (son55:E022, sol:E02, E03). The prediction vs "
                      "oracle-bit-only retries was tested (41.1% vs 71.1%; sol:E08). The surrogate–hidden-test "
                      "alignment assumption is illustrated only by one case.",
                      ["son55:E001", "son55:E022", "son55:E026", "sol:E02", "sol:E03", "sol:E08"]),
            "X": kept("son55", p, "X", "Both seats 3; re-checked. Algorithm 1 (K, M, β, early exit, escalation "
                      "trigger), the isolation rules and verbatim prompts make it reproducible (son55:E003, E024). "
                      "Retention is per task, with no cross-task versioning (stated boundary; sol:E09).",
                      ["son55:E003", "son55:E009", "son55:E021", "son55:E024", "sol:E09"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; kept, with an Opus shared correction to "
                                  "the reason. SkillsBench deterministic verifiers with an all-tests-pass criterion "
                                  "are credible (son55:E015). Opus adds that the reported counts do not reconcile: "
                                  "App. B implies ~88% oracle-pass over 85 evolution tasks (opus:O01, O03), Fig. 2 "
                                  "says 75% at round 5 (opus:O02), and the deployed headline is 71.1%. Whether 85 "
                                  "precedes the two exclusions is unstated (son55:E018). This is a reporting defect; "
                                  "the verifier itself is sound, so the rating stays 3.",
                                  ["son55:E015", "son55:E018", "sol:E04", "sol:E06"],
                                  ["opus:O01", "opus:O02", "opus:O03"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 2; re-checked. The w/o-surrogate arm (same "
                                "oracle access, 5 iterations) is a fair internal control (41.1 vs 71.1; sol:E08). "
                                "Baselines lack the oracle/iteration budget, human skills are generic vs per-task "
                                "tuned (son55:E019, E020), ablations are single-run, and EvoSkill is not run.",
                                ["son55:E005", "son55:E006", "son55:E007", "son55:E008", "sol:E07", "sol:E08"],
                                ["son55:E019", "son55:E020"]),
            "E.holdout": kept("son55", p, "E.holdout", "Both seats 1; re-checked. The hidden tests of each evaluated "
                              "task select and stop its skill and also score it (son55:E002, E003; opus:O04). No "
                              "unseen-task result exists. Partial credit only for opaque-bit limiting and "
                              "fresh-environment re-execution; cross-model runs are on the same tasks.",
                              ["son55:E002", "son55:E003", "son55:E009", "son55:E011", "opus:O04", "sol:E02",
                               "sol:E09"]),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 2; A2 ladder. Main methods: 5 runs ± std. "
                                 "Transfer: 3 runs. Ablations: single. No significance tests and no evolution-level "
                                 "variance.", ["son55:E007", "son55:E016", "son55:E017", "sol:E05", "sol:E11"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 1; re-checked. Only cycle/oracle-round counts and "
                           "timeouts are given (4.1 / 2.4; 3000s cap). No tokens or dollars, and no matched "
                           "iterative budget for baselines.", ["son55:E025", "son55:E027", "sol:E10"]),
        },
        "status": "reviewed",
        "reason": "Full v3 text including Appendices A–D read. In scope: non-weight skill packages evolved from "
                  "execution feedback. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "self_supervised_signal_engineering",
                "The headline problem is the lack of ground-truth feedback, answered by manufacturing a surrogate "
                "signal. Delegation to a checker is the means (supporting).", ["son55:E001", "sol:E02"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["decompose_and_delegate", "C25"], ["self_supervised_signal_engineering", None]],
                "Final set equals son55's, with roles swapped. generative_process_redesign (sol) is dropped: the "
                "verifier is a new component, not a freed fixed artifact.", ["son55:E006", "son55:E022"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["coevolve_the_evaluator", "H25"]],
                "H25 is agreed. H02 is added at low-moderate fit: portable multi-file skill packages compiled from "
                "docs plus feedback and reused across models. Its own failure clause ('on-demand skills for the very "
                "workflows used for evaluation') is the documented weakness.", ["son55:E009", "son55:E011"], NOSCORE),
            XC(p, "local:2604.01687-2", "revised", "unmet", "'challenged_with_evidence' means the paper rebuts the "
               "expectation with evidence. Here the expectation (like-with-like) simply fails.",
               ["son55:E019", "son55:E020"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial", "Verified: cycle counts only.",
               ["son55:E025", "son55:E027"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial", "Verified: verifier and evolution ablated, "
               "single runs.", ["son55:E006", "son55:E007"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "met", "Verified: prompts verbatim, code link.",
               ["son55:E024"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial", "Verified: one benchmark, same tasks.",
               ["son55:E011", "son55:E015"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial", "Verified: baselines lack the oracle budget; "
               "EvoSkill not run.", ["son55:E005", "son55:E012"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "sol", "partial", "Verified.", ["sol:E07", "sol:E08"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "sol", "met", "Verified: the final metric is the "
               "benchmark oracle, not the surrogate.", ["sol:E04", "sol:E06"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "sol", "partial", "Verified.", ["sol:E10"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial", "Verified: the 'no ground-truth' "
               "framing is weakened by per-task oracle use.", ["son55:E002", "son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "revised", "partial", "The gate exists but is the "
               "target task's own test.", ["son55:E003"]),
            XC(p, "rsi:coevolve_the_evaluator/F3", "son55", "unmet", "Verified (failure present): the same labels "
               "select and validate.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:coevolve_the_evaluator/F4", "son55", "partial", "Verified.", ["son55:E026"]),
            XC(p, "rsi:coevolve_the_evaluator/H25-step1", "sol", "partial", "Verified: the anchor is repeatedly "
               "consulted on the evolved tasks (H25 step 1 names this leak).", ["sol:E02", "sol:E08"]),
            XC(p, "rsi:coevolve_the_evaluator/H25-step2", "sol", "met", "Verified: verifier isolation.", ["sol:E03"]),
            XC(p, "rsi:coevolve_the_evaluator/H25-step5", "sol", "partial", "Verified: no surrogate validity "
               "statistics.", ["sol:E09"]),
            XC(p, "rsi:coevolve_the_evaluator/S1", "son55", "partial", "Verified.", ["son55:E002", "son55:E026"]),
            XC(p, "rsi:coevolve_the_evaluator/S2", "son55", "met", "Verified.", ["son55:E021", "son55:E022"]),
            XC(p, "rsi:coevolve_the_evaluator/S5", "son55", "partial", "Verified.", ["son55:E006", "son55:E007"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.G. son55 itself notes the 'no ground-truth' framing is blurred by the oracle bit and that "
                "EvoSkill is not run. Those are exactly the incomplete-residual conditions of anchor 2.",
                ["son55:E002", "son55:E012", "sol:E01"], "-3.75 vs son55 (62.5 → 58.75)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "3", "son55_value": "3 (noted 75% vs 71.1%)",
             "final_value": 3,
             "reason": "Neither seat recorded that App. B's '10 tasks failed' over 85 evolution tasks implies ~88% "
                       "oracle-pass, inconsistent with Fig. 2's 75% at round 5 and the 71.1% deployed rate. Nor did "
                       "either note that the 85 count's relation to the two exclusions is unstated. Recorded as an "
                       "unexplained reporting inconsistency; no rating change.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none"},
            a4("expectations[local:2604.01687-1].id", "local-1 = misalignment explanation (unmet)",
               "local-1 = unseen-task results (unmet)", "local-1 = sol; local-3 = son55 local-1",
               "A4 hidden ID collision with equal status, so the mechanical diff missed it; renumbered.",
               ["sol:E13", "son55:E009"]),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before the seat records. In scope; "
                                                   "system_method. The per-task hidden oracle gates and selects the "
                                                   "skill and also scores it, so evidence_level is task. The "
                                                   "w/o-verifier arm is the one fair control. Expected G2 M3 X3 Em2–3 "
                                                   "Ec2 Eh1 Es2 Ecost1.",
            "integrity_checks": "Both seats a1 on v3, input_hash fb05ffc5…; canonical hashes equal conflicts.json; "
                                "material sha aa6054af…; 15+31 complete, valid parents.",
            "core_claim_check": "Table 3 and Table A1 values re-read. The 71.1 / 30.6 / 53.5 figures are prose-stated. "
                                "The App. B / Fig. 2 / headline counts do not reconcile (shared correction).",
            "rating_agreement": "Seven of eight items agree and were re-derived; G resolved to 2.",
        },
    }

    # =========================================================== 2604.03964 SkillFoundry (sol 53.75 / son55 43.75)
    p = "2604.03964"
    S[p] = {
        "base": "son55",
        "figure_dependence": "Figs 2–4 are image-only. Cell-annotation and scDRS values come from prose/Table 2; the "
                             "MoSciBench per-dataset n is inferred from Table 1 percentages (our_inference).",
        "a3": "none (in scope as B-class: a non-weight skill library built and pruned by execution-validation "
              "feedback)",
        "opus_evidence": [
            opus_ev(p, "O01", "Averaged over all six datasets, Repo-Acc increases from 61.19% to 66.73%, and Paper-Acc "
                              "increases from 43.85% to 53.05%.", "§4.2",
                    "These are macro-averages. Back-solving Table 1 percentages gives n = 17/15/13/15/14/14 (88 items) and "
                    "Repo-correct 54→59, Paper-correct 39→47: +5 and +8 items, single run.", kind="our_inference"),
            opus_ev(p, "O02", "w/ skills 80.00 66.67 100.00 71.43 57.14 100.00 64.29 42.86 100.00",
                    "Table 1 (nurse stress / cyclone / terra, with skills)",
                    "terra Repo-Acc is 64.29 with skills."),
            opus_ev(p, "O03", "w/o skills 80.00 66.67 100.00 64.29 42.86 100.00 64.29 35.71 100.00",
                    "Table 1 (nurse stress / cyclone / terra, without skills)",
                    "terra Repo-Acc is 64.29 without skills, so under the official-repo scorer only four of six "
                    "datasets improve (nurse stress and terra unchanged). 'Five of six' holds only for Paper-Acc.",
                    kind="our_inference"),
            opus_ev(p, "O04", "Every candidate skill is subjected to execution testing and synthetic-data testing",
                    "§4.1", "The validity screen is internal; failed/repaired/removed candidate counts are never "
                    "reported, so 'all retained skills pass' is survivorship."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["decompose_and_delegate"],
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", role="primary",
                       reason="Opus confirms sol's primary. The library's value is realised as inference-time "
                              "conditioning of fixed agents (Codex, Biomni) with no weight change. C03 is not assigned: "
                              "skill delivery is 'availability of the relevant skills', with no stated retrieval "
                              "substrate."),
                smatch("son55", p, "decompose_and_delegate", role="supporting",
                       reason="Supporting: candidate skills are executable artifacts closed by execution/system/"
                              "synthetic-data tests with a repair loop (son55:E003, E030)."),
            ],
            "outside_taxonomy": False,
            "reason": "unify_into_shared_representation (son55 primary) is rejected. The operational contract is a "
                      "packaging schema, not a learned tokenizer/projector/shared substrate (son55's own fit "
                      "'weak-moderate'), and its RE checks are kept only as questions.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": [{"candidate": "H07", "reason": "Opus: only the on-demand design_skill path is "
                                           "demand-triggered tool forging. The library mechanism is H02's "
                                           "resource-mined, coverage-tree-guided packaging, which H02 names "
                                           "explicitly ('Track coverage — a domain tree')."}],
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H02",
             "operation_correspondence": "Resource-mined, contract-compiled skill packages (H02) are the conditioning "
                                         "the fixed coding agent reads at inference (adapt_via_conditioning).",
             "differences": "No retrieval substrate or category-level holdout; mining is from documents, not "
                            "interaction streams.",
             "evidence_ids": ["son55:E002", "son55:E026"], "origin": "opus"},
        ] + pm("son55", p, [1]),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.03964-1"): "local:2604.03964-4"},
            overrides={"local:2604.03964-4": {"note": "A4: renumbered from son55 local-1 (candidate survival counts)."},
                       "local:2604.03964-1": {"reason": "Opus (sol, kept). Expert-blinded scDRS scoring supports "
                                              "scientific correctness for one workflow; the library is otherwise "
                                              "internally validated only (sol:E13). Under the official scorer, "
                                              "MoSciBench improves on four of six datasets, not five (opus:O02, "
                                              "O03)."}}),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01", "opus:O02", "opus:O03"]), "C1",
                                        ["opus:O04"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats retained; kept. A pre-built, retained library is toggled on later, "
                                   "external MoSciBench tasks with the agent fixed. This is weak, small-n evidence "
                                   "with no overlap audit, and on-demand skills are built for the evaluated task.",
            "claim_support": "scoped",
            "strongest_supported_claim": "A 286-skill library that passes its own execution/synthetic tests is "
                                         "associated with +5 (Repo) / +8 (Paper) of ~88 MoSciBench items for one coding "
                                         "agent in a single run (four or five of six datasets, depending on scorer). Two "
                                         "on-demand skills improve one cell-annotation run and a three-replicate scDRS "
                                         "comparison. Novelty is keyword-judged, and the self-evolving loop's "
                                         "contribution is not isolated.",
            "unresolved": ["Candidate survival/repair/prune counts.", "Alternative-library / raw-doc controls.",
                           "Which skills were made available per MoSciBench dataset, and by whom.",
                           "Design-case vs evaluation separation for on-demand skills."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 2; re-checked. Fragmented resources → usable skills is a real "
                      "limitation with named tool- and skill-centric neighbours (son55:E018, E019). The bottleneck is "
                      "asserted, and existing libraries are not used as a comparator.",
                      ["son55:E018", "son55:E019", "son55:E020", "sol:E01"]),
            "M": R("resolved", 2, "Opus → son55 2 (sol 3). Tree-guided mining → contract → multi-layer tests → merge/"
                   "prune is a coherent response (son55:E002, sol:E09). But the retention signals measure "
                   "executability, mock-input stability and keyword novelty, not usefulness (son55:E003). The "
                   "layer-2 'skill vs no-skill' utility check has no reported cases or outcomes (son55:E021), and the "
                   "authors concede internal validation is only screening (son55:E006). There is no distinguishing "
                   "prediction against handing the agent the raw documentation. Key assumptions are thin → 2.",
                   ["son55:E002", "son55:E003", "son55:E021", "sol:E09", "sol:E10"], ["son55:E006"]),
            "X": kept("son55", p, "X", "Both seats 2; re-checked. Stages, model allocation, registry states and "
                      "controlled state mutation are described (son55:E022, E023). Missing: layer-2 thresholds, "
                      "rollback, conflict handling, and how 'the relevant' skills reach the agent at use time "
                      "(son55:E026).", ["son55:E022", "son55:E023", "son55:E027", "sol:E02", "sol:E11"],
                      ["son55:E026"]),
            "E.measurement": R("resolved", 2, "Opus → son55 2 (sol 3). Downstream metrics are partly credible: the "
                               "official and paper MoSciBench scorers, and blinded expert scDRS grading with RMSE "
                               "(son55:E015, sol:E07). But two of the paper's three headline claims rest on "
                               "self-judged measurements: 'internally valid' means passing its own tests, with "
                               "unreported failure counts (opus:O04), and 71.1% novelty is a keyword search "
                               "(son55:E005). The 'five of six' summary also misstates the official-scorer result "
                               "(four of six; opus:O02, O03).",
                               ["son55:E005", "son55:E015", "sol:E07"],
                               ["opus:O02", "opus:O03", "opus:O04", "son55:E006"]),
            "E.causality": R("resolved", 1, "Opus → son55 1 (sol 2). The only manipulation is skills present vs "
                             "absent for a fixed agent (son55:E026). Unlike a starter-vs-evolved design, the "
                             "no-skill arm also lacks all domain documentation, so pipeline value cannot be separated "
                             "from 'any relevant guidance'. There is no SkillHub/SkillSMP, raw-doc or RAG control, and "
                             "no ablation of tree guidance, validation layers, repair or novelty pruning. The cell-"
                             "annotation comparison pits a task-built skill against vanilla Codex, with SpatialAgent "
                             "still better (son55:E012). Relevant but not attributable → 1.",
                             ["son55:E026", "son55:E008", "sol:E05", "sol:E08"], ["son55:E012", "son55:E025"]),
            "E.holdout": R("resolved", 2, "Opus → son55 2 (sol 1). MoSciBench is an external benchmark evaluated with "
                           "an already-mined library, and nothing says it was used in construction (son55:E024). "
                           "There is no overlap audit, though mining draws on papers/repos MoSciBench may derive "
                           "from. The skills used are 'the relevant' ones, selector unstated (son55:E026). On-demand "
                           "skills are designed and tested 'for the task' with unspecified case separation "
                           "(son55:E025, E021). Gaps rather than shown leakage for the main claim → 2.",
                           ["son55:E024", "son55:E025"], ["son55:E021", "son55:E026"]),
            "E.statistics": R("resolved", 1, "Opus → son55 1 (sol 2). A2 ladder: the main benchmark result is a single "
                              "run with per-dataset n unreported (inferred 13–17; opus:O01) and differences of 0–2 "
                              "items, with no uncertainty. scDRS has 3 replicates per arm (son55:E014, E015), but the "
                              "headline result carries none. Candidate failure counts are absent.",
                              ["son55:E009", "son55:E014", "son55:E015", "opus:O01"], [],
                              ["Table 1, §4.1–4.4, App. A.2.1: no run counts, intervals or tests for MoSciBench or "
                               "cell annotation"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 1; re-checked. Stage runtimes under a capped search "
                           "budget only; tokens are explicitly not reported; no baseline cost comparison.",
                           ["son55:E007", "sol:E12"]),
        },
        "status": "reviewed",
        "reason": "Full v1 text including Appendix A read. In scope (B-class): an execution-validated non-weight skill "
                  "library. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "See rs_pattern.reason. The unify card's substrate/projector operation is not executed.",
                ["son55:E002", "son55:E026"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "Primary from sol; C25 supporting from son55 (executable skills closed by tests with repair).",
                ["son55:E003", "son55:E030"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H02"], ["evidence_gated_retention", "H30"]],
                "H02 fits the resource-mined, coverage-tree packaging; H07 covers only the on-demand path. H30 is "
                "agreed.", ["son55:E002", "son55:E022"], NOSCORE),
            XC(p, "local:2604.03964-1", "sol", "partial", "A4 collision: sol local-1 = scientific correctness beyond "
               "internal validation (partial, kept); son55 local-1 (survival counts, unmet) moved to local-4.",
               ["sol:E07", "sol:E13"]),
            XC(p, "local:2604.03964-2", "son55", "partial", "Verified: novelty is not tied to utility.",
               ["son55:E005"]),
            XC(p, "local:2604.03964-3", "son55", "unknown", "Verified: layer-2 case sources are unstated.",
               ["son55:E021", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial", "Verified: no overlap audit.", ["sol:E05"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "sol", "unmet", "Verified: no raw-doc/long-context alternative.",
               ["sol:E05", "sol:E10"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet", "Verified: runtime only.", ["son55:E007"]),
            XC(p, "rs:decompose_and_delegate/RE-3", "son55", "partial", "Verified: abbreviated prompts.",
               ["son55:E024"]),
            XC(p, "rs:unify_into_shared_representation/RE-1", "son55", "unmet", "Kept as a check question (card not "
               "matched): no interface ablation.", ["son55:E026"]),
            XC(p, "rs:unify_into_shared_representation/RE-2", "son55", "unmet", "Kept as a check question: no "
               "skeptic baseline.", ["son55:E008"]),
            XC(p, "rs:unify_into_shared_representation/RE-3", "son55", "partial", "Kept as a check question.",
               ["son55:E017", "son55:E024"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial", "Verified.", ["son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial", "Verified: executability, not "
               "utility.", ["son55:E003", "son55:E021"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial", "Verified: no counts.",
               ["son55:E022"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "met", "Verified: tests + novelty review gate "
               "admission (a gate exists; its utility is a separate question).", ["son55:E003", "son55:E022"]),
            XC(p, "rsi:crystallize_executable_capability/H07-step2", "sol", "met", "Kept as a check question: "
               "resource-grounded.", ["sol:E01", "sol:E02"]),
            XC(p, "rsi:crystallize_executable_capability/H07-step5", "sol", "partial", "Kept as a check question.",
               ["sol:E05", "sol:E10"]),
            XC(p, "rsi:evidence_gated_retention/H30-step4", "sol", "partial", "Verified: no size bound or retirement "
               "thresholds.", ["sol:E02", "sol:E11"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unknown", "Verified: layer-2 outcomes are not "
               "reported.", ["son55:E021"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "unmet", "Verified: no gate ablation.", ["son55:E026"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial", "Verified.", ["son55:E007"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M: retention signals do not measure usefulness, and the utility layer has no evidence.",
                ["son55:E003", "son55:E021"], "-5"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.measurement: two headline claims rest on self-judged measures; the summary misstates "
                "the official scorer.", ["son55:E005", "opus:O03"], "-2.5"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.causality: the skills-vs-nothing toggle cannot attribute value to the pipeline.",
                ["son55:E026"], "-3.75"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.holdout: the external benchmark has gaps, not shown leakage. sol's 1 rests on the "
                "on-demand path and layer-2, which do not bear on the main benchmark claim.",
                ["son55:E024", "son55:E025"], "+2.5"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.statistics: the headline result is single-run with no uncertainty; scDRS replicates do "
                "not lift the main result.", ["son55:E009", "opus:O01"], "-1.25"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims[C2] / ratings.E.measurement.reason", "sol_value": "five of six datasets improve",
             "son55_value": "five of six (about one or two items each)",
             "final_value": "four of six under official-repo Repo-Acc (nurse stress, terra unchanged); five of six "
                            "under Paper-Acc; ≈ +5/88 (Repo), +8/88 (Paper), single run",
             "reason": "Both seats repeated the paper's 'five of six'. Table 1 shows terra Repo-Acc 64.29 → 64.29 "
                       "(opus:O02, O03), so the claim holds only for the paper's alternative scorer.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none (E.measurement already 2)"},
            a4("expectations[local:2604.03964-1].id", "local-1 = correctness beyond internal validation (partial)",
               "local-1 = candidate survival counts (unmet)", "local-1 = sol; local-4 = son55 local-1",
               "A4 hidden ID collision; renumbered.", ["sol:E13", "son55:E030"]),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before the seat records. In scope (B-class). "
                                                   "The main evidence is a single-run skills-on/off MoSciBench "
                                                   "comparison worth a handful of items, with self-judged "
                                                   "validity/novelty and no mechanism ablations. Expected G2 M2 X2 "
                                                   "Em2 Ec1 Eh1–2 Es1 Ecost1.",
            "integrity_checks": "Both seats a1 on v1, input_hash fb05ffc5…; hashes equal conflicts.json; material sha "
                                "83112527…; 15+31 complete, valid parents.",
            "core_claim_check": "Table 1 averages recompute (61.19/66.73; 43.85/53.05). The per-dataset n back-solve "
                                "is our inference. 'Five of six' fails under Repo-Acc.",
            "rating_agreement": "G, X, E.cost agree and were re-derived. Five conflicts resolved, all to son55 on "
                                "independent reasons.",
        },
    }

    # =========================================================== 2604.04347 RoboPhD (sol 65.0 / son55 67.5)
    p = "2604.04347"
    S[p] = {
        "base": "son55",
        "figure_dependence": "Fig. 1 is a schematic; all results are in Tables 1–4 text.",
        "a3": "none (in scope: non-weight agent code evolved from execution feedback and evaluated on held-out tests)",
        "opus_evidence": [
            opus_ev(p, "O01", "Reducing from 200 to 100 improves all eight paired comparisons.", "Table 3 caption",
                    "Table 2's GEPA/Autoresearch cells equal Table 3's val=100 column (e.g., ARC 58.5/54.2, DocFinQA "
                    "40.0/48.2). Baselines are thus reported at their test-better setting, a test-informed choice "
                    "that favours the baselines, not RoboPhD.", kind="our_inference"),
            opus_ev(p, "O02", "We argue in Section 4.2 that the evidence points towards a narrow win for our default "
                              "Elo-based configuration over KotH", "§3.5",
                    "Default vs KotH, Table 2: KotH higher on ARC (67.0 vs 65.8) and Can't Be Late; default higher on "
                    "Text2SQL and DocFinQA. 2:2 in single runs, so the 3-agent Elo tournament itself is not shown "
                    "to matter.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "assumption_audit_and_pivot",
            "supporting": ["controlled_diagnostic_design"],
            "matches": [smatch("son55", p, "assumption_audit_and_pivot"),
                        smatch("son55", p, "controlled_diagnostic_design")],
            "outside_taxonomy": False,
            "reason": "son55 adopted. The paper's headline move audits the validate-then-select premise and drops it "
                      "(son55:E001, E004), with a selection-noise analysis as the substitute certificate. "
                      "generative_process_redesign (sol) is weaker: no conventionally fixed artifact of the "
                      "generative process is freed. The matched-budget comparison is controlled_diagnostic_design "
                      "(agreed by both).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H14"),
                                       dmatch("son55", p, "diagnose_self_improvement", "H32")],
                           "unassigned": [{"candidate": "H16", "reason": "Opus: rejected. The Elo-ranked population "
                                           "with random top-2 pairing, clone penalty and tie randomization injects "
                                           "noise but preserves no frontier and names no complementarity axis."}],
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("son55", p),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.04347-1"): "local:2604.04347-5",
                    ("son55", "local:2604.04347-3"): "local:2604.04347-1"},
            overrides={"local:2604.04347-1": {"reason": "Opus (sol local-1 + son55 local-3, same question; unmet). "
                                              "No RoboPhD-with-validation or validation-free-baseline run on identical "
                                              "infrastructure. The 200→100 trend (8 single runs) cannot establish "
                                              "zero as optimal, and KotH (also validation-free) ties default 2:2 "
                                              "(opus:O02)."},
                       "local:2604.04347-5": {"note": "A4: renumbered from son55 local-1 (multiple evolution runs)."}}),
        "claims": lambda c: add_counter(c, "C2", ["opus:O02"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats retained; kept. Evolved agent code, selected only on training "
                                   "samples, improves separate test sets. Not improver: the evolution AI and strategy "
                                   "are fixed and meta-evolution is untested.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Under a matched 1,500-evaluation budget and shared diagnostics, single runs "
                                         "of default RoboPhD score above the authors' GEPA and Autoresearch runs on "
                                         "held-out ARC-AGI, BIRD dev and DocFinQA tests. A matched validation-free "
                                         "KotH variant is as good on 2 of 4, so validation-free Elo selection "
                                         "specifically, and self-instrumentation, are not isolated.",
            "unresolved": ["Run-to-run variance.", "Evolution-AI token/time cost per engine.",
                           "Faithfulness of adapted baselines and GEPA's API-vs-Code channel."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 3; re-checked. The bottleneck is quantified (validation consumes "
                      "the budget; 7–13 candidates) and baselines are actually run (son55:E004, E005, E029). "
                      "Noisy-fitness/bandit precedent is not discussed.",
                      ["son55:E004", "son55:E005", "son55:E014", "son55:E029", "sol:E01", "sol:E06"]),
            "M": kept("son55", p, "M", "Both seats 3; re-checked. Biased-noisy selection accumulated by Elo, with an "
                      "exact selection-accuracy analysis and a stated falsifying regime (compact task). The distinct "
                      "prediction vs greedy KotH is weakly borne out.",
                      ["son55:E001", "son55:E008", "son55:E009", "son55:E012", "sol:E02", "sol:E03", "sol:E04"],
                      ["son55:E013"]),
            "X": kept("son55", p, "X", "Both seats 3; re-checked. Algorithm 1, the Elo constants, sample size, clone "
                      "penalty, ties, Deep Focus and the strategy prompt are given. Broken-agent handling and rollback "
                      "beyond the AI's judgment are unspecified.",
                      ["son55:E006", "son55:E007", "son55:E027", "son55:E031", "sol:E05", "sol:E14"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; re-checked. Executable/exact-match "
                                  "scorers, cost caps with breach rate <1%, and a disclosed and fixed simulator "
                                  "exploit (son55:E018, E021).",
                                  ["son55:E019", "son55:E021", "son55:E018", "sol:E10", "sol:E13"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 2; re-checked. KotH, the Deep Focus ablation and "
                                "the validation-size sweep are useful. Engines differ in proposer channel (API vs "
                                "Claude Code), sampling and tooling (son55:E015, E026). No run isolates "
                                "validation-free selection, and the default-vs-KotH tally is 2:2 (opus:O02).",
                                ["son55:E012", "son55:E013", "son55:E014", "son55:E015", "son55:E016", "son55:E030",
                                 "opus:O02"], ["son55:E026"]),
            "E.holdout": R("resolved", 3, "Opus → son55 3 (sol 2). Four fixed train/test splits are used "
                           "identically across engines; every engine's final artifact is chosen without touching "
                           "test (Elo on fresh training samples for RoboPhD; son55:E019, E020, sol:E01, E05). The "
                           "test-informed choice sol cites (validation size) set the BASELINES at their better val=100 "
                           "configuration (opus:O01). That inflates the comparators, not RoboPhD's own claim. Below 4: "
                           "RoboPhD's defaults descend from Text2SQL-specific development (son55:E024) with BIRD dev "
                           "use unaudited, the Deep Focus default is justified by a test-set ablation, and there is no "
                           "contamination audit for ARC/BIRD.",
                           ["son55:E019", "son55:E020", "son55:E032", "sol:E01", "sol:E05"],
                           ["son55:E024", "opus:O01", "sol:E09"]),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 1; A2 ladder. Test sizes and a negative task "
                                 "are reported; every cell is a single run with no intervals. The selection-noise "
                                 "simulation is not end-to-end uncertainty.",
                                 ["son55:E010", "son55:E011", "son55:E017", "sol:E08"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 2; re-checked. The evaluation budget is matched "
                           "(including Deep Focus) and per-problem solver caps are enforced. Evolution-AI tokens/time, "
                           "which differ sharply between Claude Code sessions and API reflection, are unreported.",
                           ["son55:E021", "son55:E022", "son55:E005", "sol:E06", "sol:E12"], ["son55:E015"]),
        },
        "status": "reviewed",
        "reason": "Full v1 text including Appendices A–D read. In scope: evolved non-weight agent code retained and "
                  "evaluated on held-out tests. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "assumption_audit_and_pivot",
                "See rs_pattern.reason.", ["son55:E001", "son55:E004"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["assumption_audit_and_pivot", None], ["controlled_diagnostic_design", None]],
                "controlled_diagnostic_design is agreed. The pivot card replaces generative_process_redesign.",
                ["son55:E001", "son55:E029"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["diagnose_self_improvement", "H32"], ["population_search_executable_fitness", "H14"]],
                "H14 is agreed. H32 is added (son55): the matched-budget engine comparison and the KotH isolation are "
                "a claimed contribution. H16 is rejected (no frontier/complementarity axis).",
                ["son55:E027", "son55:E030"], NOSCORE),
            XC(p, "local:2604.04347-2", "son55", "unmet", "Verified: evolution-AI cost is not reported per engine.",
               ["son55:E005", "son55:E015"]),
            XC(p, "local:2604.04347-3", "same_supported_fact", "unmet",
               "Same question as sol local-1 (validation-free attribution), both unmet; merged into local-1 (A4).",
               ["son55:E014", "sol:E09"]),
            XC(p, "local:2604.04347-4", "son55", "unmet", "Verified: print-diagnostics channel not ablated.",
               ["son55:E023"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-2", "son55", "partial", "Verified.", ["son55:E009"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-4", "son55", "partial", "Verified: noisy-fitness precedent "
               "absent.", ["son55:E028"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-6", "son55", "partial", "Verified.", ["son55:E014"]),
            XC(p, "rs:controlled_diagnostic_design/RE-3", "son55", "partial", "Verified.",
               ["son55:E021", "son55:E022"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial", "Kept as a check question.",
               ["sol:E07", "sol:E08"]),
            XC(p, "rs:generative_process_redesign/RE-5", "sol", "partial", "Kept as a check question.",
               ["sol:E06", "sol:E12"]),
            XC(p, "rs:generative_process_redesign/RE-6", "sol", "partial", "Kept as a check question.",
               ["sol:E08", "sol:E12"]),
            XC(p, "rsi:diagnose_self_improvement/F1", "son55", "partial", "Verified: KotH matched; GEPA differs.",
               ["son55:E015", "son55:E030"]),
            XC(p, "rsi:diagnose_self_improvement/S3", "son55", "met", "Verified.", ["son55:E019", "son55:E020"]),
            XC(p, "rsi:population_search_executable_fitness/F5", "son55", "partial", "Verified: the authors concede "
               "shared features carry much of the gain.", ["son55:E013"]),
            XC(p, "rsi:population_search_executable_fitness/H14-step3", "sol", "met", "Verified.",
               ["sol:E02", "sol:E03"]),
            XC(p, "rsi:population_search_executable_fitness/H14-step4", "sol", "partial", "Verified.",
               ["sol:E12", "sol:E14"]),
            XC(p, "rsi:population_search_executable_fitness/H14-step5", "sol", "partial", "Verified: single runs.",
               ["sol:E01", "sol:E12"]),
            XC(p, "rsi:population_search_executable_fitness/S1", "son55", "met", "Verified.", ["son55:E001"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial", "Verified: exploit found and "
               "patched.", ["son55:E018"]),
            XC(p, "rsi:population_search_executable_fitness/S3", "son55", "challenged_with_evidence",
               "Legitimate use: the paper's own results (600–1,100-line agents with held-out gains on three LLM "
               "tasks, the compact task won by an 87-line artifact) present evidence against 'small unit in a "
               "scaffold' as a necessity here. There is no matched small-genome control.",
               ["son55:E003", "son55:E010", "son55:E011"]),
            XC(p, "rsi:population_search_executable_fitness/S4", "son55", "met", "Verified.", ["son55:E007"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "partial", "Verified.",
               ["son55:E012", "son55:E027"]),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.holdout. The test-informed decision favours the baselines, and no final artifact is "
                "selected on test.", ["opus:O01", "son55:E020"], "+2.5 vs sol (65.0 → 67.5)"),
        ],
        "shared_error_corrections": [
            a4("expectations[local:2604.04347-1].id", "local-1 = validation-free attribution (unmet)",
               "local-1 = multi-run variance (unmet); local-3 = validation-free attribution (unmet)",
               "local-1 = sol local-1 + son55 local-3 (merged); local-5 = son55 local-1",
               "A4 hidden collision with equal status, so the mechanical diff missed it; renumbered and merged.",
               ["sol:E09", "son55:E014"]),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before the seat records. In scope; retained. "
                                                   "Clean held-out tests, never used for selection. Single runs; "
                                                   "Elo vs KotH 2:2; the GEPA API-vs-Code confound. Expected G3 M3 X3 "
                                                   "Em3 Ec2 Eh3 Es1 Ecost2.",
            "integrity_checks": "Both seats a1 on v1, input_hash fb05ffc5…; hashes equal conflicts.json; material sha "
                                "170afd3e…; 15+31 complete, valid parents.",
            "core_claim_check": "Tables 2–4 re-read. Baseline cells equal Table 3 val=100 (opus:O01). The '3 of 4' "
                                "claim holds for default; KotH ties it 2:2.",
            "rating_agreement": "Seven of eight items agree and were re-derived; E.holdout resolved to 3.",
        },
    }

    # =========================================================== 2604.04804 SkillX (sol 48.75 / son55 56.25)
    p = "2604.04804"
    S[p] = {
        "base": "son55",
        "figure_dependence": "Fig. 3 (a–f) is image-only; skill-level, iteration, token and step values are used "
                             "only as described in prose. Tables 1–3 carry the numbers used.",
        "a3": "none (in scope: a retained non-weight skill library built from execution rollouts)",
        "opus_evidence": [
            opus_ev(p, "O01", "We find that SkillX provides consistent performance gains, whether the skills are "
                              "extracted by these stronger models themselves or constructed using GLM-4.6.", "§6.1",
                    "The paper's consistency claim, contradicted by opus:O02."),
            opus_ev(p, "O02", "Self-Extract 50.67 56.67 68.60 82.14", "Table 2 (GPT-4.1, Self-Extract row)",
                    "Against GPT-4.1 No Memory (49.66 / 58.39 / 66.37 / 82.74; son55:E031), Self-Extract Pass@4 "
                    "falls on both BFCL (58.39→56.67) and AppWorld (82.74→82.14).", kind="our_inference"),
            opus_ev(p, "O03", "Vanilla-Iter1 78.50 85.33 62.35 83.33", "Table 3",
                    "The only SkillX configuration that involves no test-based choice (first iteration, no "
                    "expansion). It improves GLM-4.6 Avg@4 over No Memory (76.67→78.50; 60.27→62.35); Pass@4 is flat on "
                    "AppWorld. This is the basis for 'retained'."),
            opus_ev(p, "O04", "proactively generates and validates novel skills to expand coverage beyond seed "
                              "training data", "Abstract",
                    "§3.4 synthesizes tasks from exploration and reruns extraction, but states no validation of the "
                    "synthesized tasks or their success signal."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["heterogeneous_decomposition"],
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "heterogeneous_decomposition")],
            "outside_taxonomy": False,
            "reason": "son55 adopted. Retrieved skill packages condition frozen agents (C03's retrieved-reference "
                      "form; run convention r02a AWM, r11b AutoSkill/Uni-Skill). The plan/functional/atomic split "
                      "has its own per-level analysis (Fig. 3a prose), which is heterogeneous_decomposition "
                      "(precedent r13a MineEvolve).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H02"),
                                       dmatch("son55", p, "self_generate_the_curriculum", "H23")],
                           "unassigned": [{"candidate": "H01", "reason": "Opus: dropped. Merge/modify/versioning is "
                                           "covered by H02, and there is no delete/forget policy."},
                                          {"candidate": "H06", "reason": "sol's choice. Skills are textual tool-usage "
                                           "packages distilled from task rollouts, not executed parameterized "
                                           "callables admitted by replay; H02 fits better."}],
                           "revision_proposals": prefix(copy.deepcopy(
                               seat("son55", p)["domain_pattern"]["revision_proposals"]), "son55")},
        "pattern_mapping": pm("son55", p, [0]) + [
            {"rs_main": "heterogeneous_decomposition", "rs_sub": None, "domain_namespace": "rsi",
             "domain_main": "abstract_experience_into_guidance", "domain_sub": "H02",
             "operation_correspondence": "The H02 package is split into planning/functional/atomic levels with "
                                         "separate extraction and per-level use.",
             "differences": "The split is by granularity, not by source or modality; per-level gains are "
                            "model-dependent.",
             "evidence_ids": ["son55:E023", "son55:E022"], "origin": "opus"}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2604.04804-1"): "local:2604.04804-5"},
            overrides={"local:2604.04804-5": {"status": "partial", "reason": "Opus (renumbered from sol local-1; "
                                              "revised from 'challenged_with_evidence'). The paper reports "
                                              "model-specific best skill levels and round-3 regression "
                                              "(sol:E10, E18), but still claims consistency. The mechanism claim is "
                                              "only partly scoped."}}),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01", "opus:O02"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats retained; kept on a narrower basis (shared correction). The headline "
                                   "rows are on the test split that also chose the iteration count and per-benchmark "
                                   "configuration (son55:E008, E014–E016), which is at most task under EVIDENCE rule "
                                   "2. Retained rests on Vanilla-Iter1 (opus:O03), a fixed first iteration with no "
                                   "test-based choice that improves held-out test Avg@4.",
            "claim_support": "scoped",
            "strongest_supported_claim": "A GLM-4.6-extracted multi-level skill library built on training splits "
                                         "improves weaker models on held-out test tasks (e.g., Qwen3-32B BFCL Avg@4 "
                                         "53.67→63.67) and leads reproduced A-Mem/AWM/ExpeL under a unified protocol. "
                                         "Reported SkillX configurations were chosen with test results. Margins over "
                                         "ExpeL for GLM-4.6 are ~1 point with no dispersion, and gains are not "
                                         "consistent for GPT-4.1 self-extraction.",
            "unresolved": ["Selection of rounds/configuration on a disjoint split.", "Construction budget vs baselines.",
                           "Validation of synthesized tasks.", "Run- and library-level variance."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 2; re-checked. Real limitations (isolated re-extraction, weak "
                      "transfer, long-context skills) and named families, but the limitations are asserted and "
                      "per-neighbour residuals are unstated.",
                      ["son55:E002", "son55:E003", "son55:E004", "son55:E033", "sol:E08"]),
            "M": kept("son55", p, "M", "Both seats 2; re-checked. Hierarchy plus guided exploration is coherent. "
                      "'Refinement from execution feedback' reduces to re-extracting successful trajectories and "
                      "merging, and merge is a vector-update metaphor (son55:E034).",
                      ["son55:E005", "son55:E026", "son55:E034", "sol:E01", "sol:E04"], ["son55:E023"]),
            "X": R("resolved", 2, "Opus → sol 2 (son55 3). Extraction prompts, clustering, filters, retrieval "
                   "thresholds and MMR are reconstructable (son55:E006, E007, E028; sol:E14, E15). But key retention "
                   "conditions are unclear or inconsistent. (1) The abstract's 'generates and validates novel skills' "
                   "has no stated validation of synthesized tasks or their success signal (opus:O04, son55:E027). "
                   "(2) Eq. 7 defines the update as a union while the text describes modify/merge. (3) Admission is "
                   "an LLM good/bad judge plus a schema check, with no utility gate or retirement. The test-based stop "
                   "rule is counted under E.holdout only (A2), so this is not double-counted. Anchor 2.",
                   ["son55:E006", "son55:E007", "son55:E028", "sol:E03", "sol:E14", "sol:E15"],
                   ["opus:O04", "son55:E027"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; re-checked. Standard executable/"
                                  "state-based scorers with Avg@4/Pass@4. τ²'s LLM user simulator and small domains "
                                  "are noted.", ["son55:E032", "son55:E010", "son55:E011", "sol:E07", "sol:E16"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 2; kept, with an Opus addition. Unified-"
                                "protocol baselines in two extraction regimes and per-level/iteration/expansion "
                                "analyses are useful. The pseudo-plan and filters are not ablated, construction "
                                "budgets are unmatched, and GLM-4.6's margin over ExpeL is ~1 point. Opus adds that "
                                "the claimed cross-model consistency fails for GPT-4.1 self-extraction Pass@4 "
                                "(opus:O02).",
                                ["son55:E017", "son55:E036", "son55:E015", "son55:E016", "sol:E08", "sol:E10"],
                                ["son55:E023", "opus:O02"]),
            "E.holdout": R("resolved", 1, "Opus → sol 1 (son55 2). Eq. 8 makes test performance the objective and "
                           "stops refinement 'when this test performance no longer improves' (son55:E008). The GLM-4.6 "
                           "'SkillX' row equals the best Table 3 test row per benchmark: Vanilla-Iter2 on BFCL, "
                           "Expand-Iter3 on AppWorld (son55:E014–E016). The reported method is therefore "
                           "test-selected per benchmark. There is also no overlap audit, BFCL is a random "
                           "within-category split, and τ² training covers test patterns (son55:E010, E012). Only "
                           "Vanilla-Iter1 (opus:O03) and AppWorld's distribution gap (son55:E013) stand apart from the "
                           "selection → 1, not 0.",
                           ["son55:E008", "son55:E014", "son55:E015", "son55:E016", "sol:E02"],
                           ["opus:O03", "son55:E013"]),
            "E.statistics": R("resolved", 1, "Opus → son55 1 (sol 2). A2 ladder: Avg@4 and Pass@4 average four runs "
                              "into point estimates with no dispersion, intervals or tests, from a single library "
                              "construction. ~1-point differences are called consistent (GLM-4.6 vs ExpeL BFCL 79.50 "
                              "vs 78.83; son55:E017). Sample sizes (BFCL 150) and harmful cases are reported, so 1, "
                              "not 0.",
                              ["son55:E032", "son55:E017", "son55:E021", "son55:E022"], [],
                              ["§5.1–6.2, Tables 1–3, App. A: no std/CI/significance; one library per setting"]),
            "E.cost": R("resolved", 2, "Opus → son55 2 (sol 1). Inference input tokens and execution steps are "
                        "analysed against baselines (Fig. 3e–f; values image-only), with the honest note that SkillX "
                        "is not minimal (son55:E030). Construction parameters are stated (4 rollouts/task, ≤3 rounds, "
                        "1 exploration rollout; son55:E025). No token/dollar ledger for construction and no budget "
                        "matching. This matches the 2604.01480 treatment (test-time cost reported, construction cost "
                        "missing → 2).",
                        ["son55:E030", "son55:E025", "son55:E028", "sol:E09", "sol:E12"]),
        },
        "status": "reviewed",
        "reason": "Full v2 text including Appendices A–C read. In scope: a non-weight skill library retained from "
                  "rollouts and reused by other models. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["heterogeneous_decomposition", None]],
                "C03 by run convention for retrieved skill libraries conditioning frozen agents. The level split has "
                "its own analysis.", ["son55:E028", "son55:E023"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H02"], ["self_generate_the_curriculum", "H23"]],
                "H02 (portable cross-model skill packages with merge/filter) and H23 (exploration targeted at failure-"
                "prone/unused tools, then task synthesis). H01 is subsumed; H06 (sol) is rejected.",
                ["son55:E026", "son55:E027", "son55:E031"], NOSCORE),
            XC(p, "local:2604.04804-1", "son55", "unmet", "A4 collision: final local-1 = son55's question "
               "(rounds/config chosen on a disjoint split; unmet). sol local-1 moved to local-5 and revised to "
               "partial.", ["son55:E008", "son55:E014"]),
            XC(p, "local:2604.04804-2", "son55", "unmet", "Verified: construction budgets unmatched.",
               ["son55:E025", "son55:E024"]),
            XC(p, "local:2604.04804-3", "son55", "unmet", "Verified: no spread.", ["son55:E032", "son55:E017"]),
            XC(p, "local:2604.04804-4", "son55", "met", "Verified: harmful/flat cases are reported (to which Opus "
                                                        "adds the GPT-4.1 self-extract drop, opus:O02).",
               ["son55:E020", "son55:E022", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial", "Verified.", ["son55:E017", "son55:E036"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "sol", "partial", "Verified.", ["sol:E06", "sol:E13"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "met", "Verified: extractor-source comparison.",
               ["son55:E031", "son55:E035"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "unmet", "Verified: success-only extraction.",
               ["son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met", "Verified.",
               ["son55:E005", "son55:E007"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial", "Verified.",
               ["son55:E006", "son55:E034"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial", "Verified.", ["son55:E007"]),
            XC(p, "rsi:crystallize_executable_capability/H06-step3", "sol", "partial", "Kept as a check question.",
               ["sol:E01", "sol:E03"]),
            XC(p, "rsi:crystallize_executable_capability/H06-step5", "sol", "partial", "Kept as a check question.",
               ["sol:E02", "sol:E09"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet", "Verified.", ["son55:E006", "son55:E007"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "partial", "Verified.", ["son55:E015", "son55:E016"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "met", "Verified.", ["son55:E028", "son55:E022"]),
            XC(p, "rsi:self_generate_the_curriculum/S1", "son55", "unknown", "Verified: synthesized-task validity is "
               "not described (opus:O04).", ["son55:E027", "opus:O04"]),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.X: key retention/validation conditions are unclear or inconsistent (opus:O04, Eq. 7).",
                ["opus:O04", "son55:E027"], "-5 vs son55"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: an explicit test-based stop plus per-benchmark best-row reporting.",
                ["son55:E008", "son55:E014", "son55:E015", "son55:E016"], "-2.5 vs son55"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.statistics: four-run means without dispersion are not uncertainty.",
                ["son55:E032", "son55:E017"], "-1.25 vs sol"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.E.cost: partial reporting (inference tokens/steps), construction unreported.",
                ["son55:E030", "son55:E025"], "+1.25 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level (basis)", "sol_value": "retained", "son55_value": "retained",
             "final_value": "retained (basis: Vanilla-Iter1 only)",
             "reason": "Both seats cited the headline rows. Those rows were chosen on the test split (EVIDENCE rule "
                       "2 → task at most). Retained holds only via Vanilla-Iter1 (opus:O03), which involves no "
                       "test-based choice.",
             "evidence_ids": ["opus:O03", "son55:E008", "son55:E014"], "score_impact": "none"},
            {"field_path": "claims[C1].counterevidence", "sol_value": "none on cross-model consistency",
             "son55_value": "none on cross-model consistency", "final_value": "+ opus:O01, opus:O02",
             "reason": "Neither seat noted that §6.1's 'consistent performance gains … whether the skills are "
                       "extracted by these stronger models themselves' is contradicted by GPT-4.1 Self-Extract "
                       "Pass@4 (BFCL 58.39→56.67; AppWorld 82.74→82.14).",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
            a4("expectations[local:2604.04804-1].id", "local-1 = mechanism consistency (challenged_with_evidence)",
               "local-1 = rounds/config on disjoint split (unmet)", "local-1 = son55; local-5 = sol local-1 (partial)",
               "A4 hidden ID collision; renumbered. sol's 'challenged_with_evidence' revised to partial.",
               ["sol:E10", "son55:E008"]),
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before the seat records. In scope. Eq. 8 "
                                                   "stops on test, and the GLM-4.6 headline equals the best test "
                                                   "rows per benchmark. Four-run means without dispersion. The "
                                                   "GPT-4.1 self-extract Pass@4 drop contradicts §6.1. Expected G2 M2 "
                                                   "X2 Em3 Ec2 Eh1 Es1 Ecost1–2.",
            "integrity_checks": "Both seats a1 on v2, input_hash fb05ffc5…; hashes equal conflicts.json; material sha "
                                "c28b8992…; 15+31 complete, valid parents.",
            "core_claim_check": "Tables 1–3 re-read. The Table 1 GLM-4.6 SkillX row = Vanilla-Iter2 (BFCL) / "
                                "Expand-Iter3 (AppWorld).",
            "rating_agreement": "G, M, E.measurement, E.causality agree and were re-derived. Four conflicts resolved "
                                "(X, E.holdout → sol; E.statistics, E.cost → son55).",
        },
    }
    return S
