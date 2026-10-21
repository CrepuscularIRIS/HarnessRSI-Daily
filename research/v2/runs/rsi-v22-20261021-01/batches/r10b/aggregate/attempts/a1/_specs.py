"""Opus rulings for r10b a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2602.02369 Live-Evo (seat Δ15): final 53.75 (sol 50.0, son55 65.0), decided field by field. E.holdout → sol 0. "
        "The paper claims 'strict time-based retrieval', but its own showcase trajectory reads 'Results confirm the game "
        "conclusion' and the memory-on reasoning cites the final score 33-31 of the game it was supposed to forecast. "
        "The filter only edits the query, and retrieved experience steers the memory-on arm toward searches close to the "
        "event (opus:O01), so leakage can differ between the two arms. Under A2 the defect is charged only to E.holdout; "
        "son55's E.measurement reason also counted it, and that part is struck from the final reason (E.measurement stays "
        "2, for the Table 5 / percentage arithmetic). E.causality → son55 3: the memory-off arm, ReMem, a four-way ablation "
        "and four backbones are present. The paired extra run is learning cost, not a prediction-time advantage, so it is "
        "charged to E.cost. X → sol 2: the within-batch timing of outcome feedback is unspecified (opus:O02), the gate is "
        "described both as 'statistically significant' and as a 0.05 threshold, and there is no rollback. E.cost → sol "
        "not_reported 0: the only cost information is qualitative (r09b AgentDevel precedent).",
        "2602.01966 EvoSC: final 45.0, below both seats (sol 56.25, son55 46.25). G and M → son55 2: the 'ignores "
        "failures' premise is broad, and there is no comparison with failure-contrast neighbours. Algorithm 1 computes "
        "Exp_c before the task outcome from an undefined C_fail and never reads the FIFO queues, which contradicts §4.1 "
        "and §4.3. Shared correction: E.measurement 3 → 2. The text contradicts the table (DB +9.7 vs +6.7; OS +3.0 vs "
        "+1.7), and the 'Avg' columns average different numbers of Exp settings around the OOM cells (r09b EvoRoute "
        "reporting-integrity cap). E.cost → sol 1: hardware and a context budget are reported, but there are no extraction "
        "or consolidation costs. evidence_level → sol retained, following the Dynamic Cheatsheet precedent: memory is "
        "built and read prequentially on later, different tasks, and it is not selected on the reported tasks.",
        "2602.02474 MemSkill: the only rating conflict, E.causality → son55 3. The w/o-designer, refine-only and "
        "random-controller ablations isolate the retained skill bank on two LLMs. It is not 4: the ablations cover "
        "LoCoMo only, there is a single run, and no RL memory-manager rival is included. Final 71.25. Domain cards: H11, "
        "H21 and H26 are all retained, because each names a distinct operation (bounded skill rewrites from clustered "
        "failures; outer redesign of the memory-construction mechanism; a selector trained on downstream utility).",
        "2602.04837 GEA: final 55.0 (sol 63.75, son55 56.25). evidence_level → son55 task (EVIDENCE rule 2). The reported "
        "numbers come from the staged sets that drive parent selection, and the best Polyglot agent is chosen with "
        "medium-set scores. 88.3% = 53/60 and DGM's 56.7% = 34/60 are 60-task figures, whereas the headline 71.0% is not a "
        "multiple of 1/60, so its evaluation set is ambiguous. E.holdout and E.statistics → son55 1 (A2 ladder: the five "
        "bug-repair trials do not give the main result any uncertainty). X → son55 2. E.cost → sol 2. The RS card follows "
        "the HGM precedent (assumption_audit_and_pivot). Domain cards: H20 + H12. H14 is excluded by H20's own "
        "differentiation, and H15 needs a distilled, credited knowledge layer, which GEA does not have. Shared correction: "
        "the 'evaluation set behind headline figures' expectation is changed from unknown to unmet. The true set stays "
        "unknown, but the paper plainly fails to state it.",
        "2602.02979 CPMöbius: out_of_scope confirmed independently (A3). Coach is trained by REINFORCE and Player by GRPO; "
        "the generated questions are consumed by one GRPO batch per round and are never retained. The RS/domain record is "
        "informational (C08/H22, the run convention for proposer–solver co-training).",
        "A4 hygiene: hidden ID collisions (the same local:<key>-n number used by both seats for different questions) in "
        "2602.01966, 2602.02369, 2602.02474 and 2602.04837 were renumbered or merged. Expectations from cards that were not "
        "retained were moved to local IDs. Seat uses of 'challenged_with_evidence' to mean 'our evidence challenges the "
        "paper' were corrected to unmet or partial.",
        "No material requests: every disputed field could be answered from the pinned texts. Figure-only values (EvoSC "
        "Fig. 6, Live-Evo Fig. 3, MemSkill Fig. 3, GEA Figs. 3–5) were not estimated.",
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

    def pmap(s, p, idx, **upd):
        m = prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][idx]), s)
        m.update(upd)
        return m

    def assess(s, p, **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        a.update(upd)
        return a

    def conv(old):
        return {"converted_from": old,
                "source_note": f"Moved from {old}: that card was not kept in the final pattern record (see "
                               "resolutions). The check is still a valid question about this paper's claim, so it is "
                               "kept as a paper-local expectation (A4)."}

    def RID(old, new):
        return {"renumbered_from": old, "note": f"{old} renumbered to {new} (A4: the two seats used the same local number "
                                                "for different questions)."}

    # =========================================================== 2602.01966 EvoSC
    p = "2602.01966"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "On the OS dataset, the performance gains are also significant, with improvements of +3.0% "
                              "and +4.4% on Llama and Qwen models, respectively.", "§5.2 Performance on DB and OS Tasks",
                    "Table 1 gives +1.7 for Llama OS (50.1 vs A-MEM 48.4), not +3.0. Together with DB +9.7 in the text vs "
                    "+6.7 in the table, the prose overstates the tabulated margins."),
            opus_ev(p, "O02", "“OOM” denotes out of memory, which is caused by the limited context window of LLMs.",
                    "Table 1 caption",
                    "Cells marked OOM are left out of the baselines' 'Avg', while EvoSC's Avg also includes Exp=32 (Qwen "
                    "DB/OS) or Exp=16 (Qwen KG). The headline margins therefore average different column sets; matched "
                    "cells must be compared one by one (the same applies to Table 3 Qwen rows)."),
            opus_ev(p, "O03", "most relevant entries from the experience queues to construct an augmented input",
                    "§4.3 Experience Enhanced Inference",
                    "§4.3 says the prompt is built from the top-K most relevant queue entries. Algorithm 1 instead "
                    "retrieves the top-K *recent* successful dialogs and inserts Exp_c/Exp_s computed in the same step, so "
                    "the FIFO queues are written but never read in Algorithm 1 (see son55:E022)."),
            opus_ev(p, "O04", "At periodic intervals, the framework triggers a self-consolidation process that distills "
                              "accumulated trajectories into learnable parameters.", "§4 Overview",
                    "The consolidation trigger, steps, learning rate and initialisation of the soft prompt are never "
                    "specified."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["self_supervised_signal_engineering"],
            "outside_taxonomy": False,
            "reason": "Opus follows son55. The executed operation is conditioning a frozen LLM on retrieved successful "
                      "dialogs, contrast-derived insight text and a learned 20-token prompt (adapt_via_conditioning, C03 "
                      "not executed: no canonical schema or category holdout). Supporting: the soft prompt is fitted to "
                      "actions the same LLM generates with a larger context. This is a manufactured target confined to a "
                      "compact conditioning input (self_supervised_signal_engineering success condition 6), with no "
                      "filter stage, so the fit is weak and no sub-card is assigned. Patterns do not score.",
            "matches": [smatch("son55", p, "adapt_via_conditioning"),
                        smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "couple_context_and_weight_updates", "H28")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [pmap("sol", p, 0), pmap("son55", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2602.01966-1"): "local:2602.01966-3",
                    ("son55", "local:2602.01966-2"): "local:2602.01966-4"},
            overrides={
                "local:2602.01966-3": {
                    "status": "unmet", "score_item": "E.statistics",
                    "reason": "Opus (merged sol local-3 and son55 local-1, which ask the same question). The paper averages "
                              "three seeds, but there is no spread, per-seed table, interval or test anywhere, and the DB/OS "
                              "margins are 0.7–1.7 points. The expectation (uncertainty for the main results) is unmet; "
                              "rating it partial would credit the seeds twice."},
                "local:2602.01966-4": {
                    "status": "partial",
                    "reason": "Opus (merged sol local-4 and son55's local-2, the same question). Hardware (two A40 per "
                              "experiment), prompt length and context budget (Exp, OOM) are reported. Extraction-call, "
                              "teacher and soft-prompt training costs are not. Partial, consistent with E.cost 1."},
            }),
        "claims": lambda c: c,
        "assessment": assess(
            "son55", p, evidence_level="retained",
            level_reason="Opus sides with sol (run precedent r03b Dynamic Cheatsheet). The success repository, insight "
                         "queues and soft prompt are written from earlier tasks and read on later, different tasks of "
                         "the stream (prequential). They are not selected on the reported tasks, and the Exp=0 column "
                         "(baselines ≈ no memory) and the EE/SE/PTC rows isolate stored-memory effects. Scoped: there is "
                         "no frozen-store held-out stream, and the soft-prompt part adds ≈0 on DB/OS."),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The context-exhaustion gap is real and is shown (baselines OOM). "
                   "The second premise, that replay 'focuses solely on success', is stated broadly. Failure/success "
                   "contrast for insight extraction is an established move, and the paper neither cites nor compares "
                   "such neighbours, nor context-distillation/soft-prompt memory. Nearest-neighbour coverage is "
                   "incomplete → anchor 2.",
                   ["son55:E001", "son55:E002", "son55:E020", "son55:E023", "sol:E001"], ["son55:E023"]),
            "M": R("resolved", 2, "Opus sides with son55. Contrastive extraction plus soft-prompt context distillation is "
                   "a concrete mechanism, but key assumptions are thin. Teacher actions A* are regenerated by the same "
                   "LLM and are not verified. Nothing argues why 20 tokens retain the consolidated knowledge, or how "
                   "that would differ from keeping fewer trajectories. The method text is internally inconsistent: "
                   "Algorithm 1 computes Exp_c before the outcome from an undefined C_fail and never reads the queues, "
                   "contradicting §4.1/§4.3 (son55:E022, opus:O03).",
                   ["son55:E003", "son55:E005", "son55:E006", "son55:E022", "opus:O03"], ["son55:E022"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Next-task reading (Eq. 7) and FIFO retention are stated. "
                   "There is no admission gate, versioning, rollback or conflict handling. The consolidation schedule, "
                   "steps and init are unspecified (opus:O04), retrieval is 'recent' in Algorithm 1 but 'most relevant' "
                   "in §4.3 (opus:O03), and the prompt templates are image-only.",
                   ["son55:E004", "son55:E009", "son55:E010", "son55:E022", "sol:E002", "sol:E011", "opus:O03", "opus:O04"],
                   ["son55:E022"]),
            "E.measurement": R("resolved", 2, "Opus shared-error correction (both seats 3). Environment-verified binary "
                               "success on LifelongAgentBench is a credible verifier. But the reported comparisons are "
                               "not cleanly measured: the prose contradicts the tables (DB +9.7 vs +6.7, OS +3.0 vs +1.7; "
                               "son55:E014, opus:O01), and the headline 'Avg' columns average different numbers of Exp "
                               "settings because OOM cells are dropped for baselines (opus:O02). Run precedent r09b "
                               "EvoRoute: text–table contradictions cap E.measurement at 2.",
                               ["sol:E005", "sol:E008", "son55:E011", "son55:E012", "son55:E013", "son55:E014", "opus:O01",
                                "opus:O02"], ["son55:E014", "opus:O01", "opus:O02"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Four memory baselines under the same Exp budget and "
                             "EE/SE/PTC ablation rows exist. But PTC adds ≈0 on Llama DB (65.2→65.1) and +0.6 on OS, "
                             "contradicting the 'most significant component' narrative. The KG ablation is image-only, "
                             "and there is no budget-matched summary/longer-window alternative or cost-matched "
                             "comparison.",
                             ["son55:E017", "son55:E018", "son55:E019", "son55:E020", "sol:E007"],
                             ["son55:E017", "son55:E019"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Memory is built prequentially on the reported "
                           "stream. That is legitimate for an online claim, but there is no frozen-store or independent "
                           "stream, hyperparameters (Exp, prompt length, teacher/student split) are not shown to be "
                           "chosen elsewhere, and there is no contamination check.",
                           ["son55:E011", "sol:E010"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Sample sizes (500/500/396) and the "
                              "three-seed averaging are stated, along with negative/flat ablation cells, but the main "
                              "results have no uncertainty.",
                              ["sol:E006", "son55:E008", "son55:E015"]),
            "E.cost": R("resolved", 1, "Opus sides with sol. Some quantitative resource information bears on the claimed "
                        "context efficiency: GPUs per run, a 20-token prompt, trajectory counts per Exp setting, and "
                        "where replay hits the context limit. The LLM calls for contrastive/success extraction (two per "
                        "task), teacher passes, soft-prompt training time and tokens are not reported. This is more than "
                        "a purely qualitative statement (contrast r09b AgentDevel), so it is not not_reported, but it is "
                        "far from a cost account.",
                        ["sol:E006", "son55:E007", "son55:E009", "son55:E020"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. appendix read; Figures 2, 5, 6 (plots) and 4, 7–12 (prompts) are image-only "
                  "and were not estimated. In scope (system_method, A class): retained success-trajectory repository, "
                  "insight queues and a 20-token soft prompt on a frozen LLM (A3: the evaluated retained objects are not "
                  "model weights). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "KG ablation (Fig. 6) and the prompt templates (Figs. 4, 7–12) are images; ratings use only "
                             "the tabulated DB/OS ablation and the textual method.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "retained",
                "See assessment.level_reason. Prequential reuse on later, different tasks, with no selection on the "
                "reported tasks, follows the r03b Dynamic Cheatsheet precedent (retained, scoped). son55's 'same stream' "
                "objection limits the scope but does not trigger EVIDENCE rule 2, because nothing is selected on the "
                "reported items.", ["sol:E002", "sol:E010", "son55:E010", "son55:E017"], "none (evidence_level is not scored)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", None], ["self_supervised_signal_engineering", None]],
                "Supporting C-family card kept as a weak, informational match: the soft-prompt target is generated by the "
                "same LLM with a richer context (son55:E006). No sub-card fits.", ["son55:E006", "son55:E009"], NOSCORE),
            XC(p, "local:2602.01966-1", "sol", "partial",
               "A4 ID collision: sol's local-1 (E.causality: a budget-matched three-arm comparison) and son55's local-1 "
               "(E.statistics: seed variance) are different questions. Final local-1 = sol's question, verified partial: "
               "EE/SE/PTC rows exist, but there is no weight-only or compute-matched arm. son55's question was merged "
               "into local-3.", ["sol:E007", "son55:E017"]),
            XC(p, "local:2602.01966-3", "revised", "unmet",
               "sol's local-3 and son55's local-1 ask the same question (uncertainty on main results). Verified: three "
               "seeds are averaged and no spread or test is reported → unmet (son55's status, sol's ID).",
               ["sol:E006", "son55:E008", "son55:E015"]),
            XC(p, "local:2602.01966-4", "sol", "partial",
               "son55's local-2 (cost) was merged here. Verified: hardware and context budget are given, extraction and "
               "consolidation costs are not → partial, consistent with E.cost 1.", ["sol:E006", "son55:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: replay baselines are run at equal Exp, but there is no budget-matched summary/longer-window "
               "variant.", ["son55:E020", "son55:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: the Table 3 ablation exists, PTC shows ≈0 on Llama DB, and KG is image-only.",
               ["son55:E017", "son55:E018"]),
            XC(p, "rsi:abstract_experience_into_guidance/F5", "son55", "met",
               "Verified (met = the failure is avoided): which queue is written is decided by EnvVerify, an outcome "
               "grounding.", ["son55:E003", "sol:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "unmet",
               "Verified: lessons accumulate on the reported stream, and there is no frozen-store evaluation.",
               ["son55:E011"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step5", "son55", "partial",
               "Verified: ablation rows exist, but there is no variance or budget-matched baseline.",
               ["son55:E008", "son55:E017"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "sol", "met",
               "Verified: failed and successful dialogs are explicitly contrasted (Eq. 3).", ["sol:E003", "son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "partial",
               "Verified: only verified-success trajectories enter R_succ (an execution gate), but insights are pushed "
               "without any utility admission → partial.", ["sol:E002", "son55:E004"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "son55", "unmet",
               "Verified (failure present): the adaptation stream and the reported stream coincide, and no split is "
               "declared.", ["son55:E011"]),
            XC(p, "rsi:couple_context_and_weight_updates/S4", "sol", "met",
               "Verified: history is compressed into 20 learnable tokens while recent insights stay as text. Only P_θ is "
               "optimised in L_consolid, so the backbone is frozen by construction (son55's doubt about freezing is "
               "answered by the loss definition).", ["sol:E004", "son55:E005", "son55:E007"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.G: the neighbour coverage is incomplete and the 'success-only' premise is broad.",
                ["son55:E023", "son55:E001"], "−3.75 vs sol (15×1/4)"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M: the teacher targets are unverified, Algorithm 1 contradicts §4.1/§4.3, and no argument "
                "separates consolidation from simply keeping fewer trajectories.",
                ["son55:E022", "opus:O03", "son55:E006"], "−5.0 vs sol (20×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 1},
                "See ratings.E.cost: partial quantitative resource information is tied to the claimed context "
                "efficiency, so not_reported (0) is too strong. It stays at 1 because none of the extraction or "
                "training cost is accounted for.",
                ["sol:E006", "son55:E009", "son55:E020"], "+1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "reason": "Both seats rated the verifier and missed two reporting-integrity defects in the compared numbers. "
                       "The prose margins contradict Table 1 (opus:O01, son55:E014). The 'Avg' columns average different "
                       "Exp sets around the OOM cells (opus:O02). Precedent r09b EvoRoute caps E.measurement at 2 for "
                       "text–table contradictions. son55 itself noted the OOM averaging (E018) under causality.",
             "evidence_ids": ["opus:O01", "opus:O02", "son55:E014", "son55:E018"],
             "score_impact": "−2.5 vs both seats (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: text insights + 20-token "
                                                   "soft prompt; Table 3 shows PTC ≈0 on Llama DB; the text contradicts "
                                                   "the tables (+9.7 vs +6.7); Avg over OOM-truncated columns; three "
                                                   "seeds without spread. Initial bands G2 M2 X2 Em2 Ec2 Eh1 Es1 Ecost1; "
                                                   "evidence_level retained (prequential, scoped).",
            "integrity_checks": "Both seats a1 on 2602.01966v1, material sha 27abc6dc…; canonical seat hashes equal "
                                "conflicts.json; RS/domain namespaces and parents valid.",
            "core_claim_check": "Re-read Algorithm 1, §4.1–4.3, Tables 1–3 and §5.1–5.2.1 for every disputed field.",
            "rating_agreement": "Five of eight items agree across seats and were re-checked (E.measurement corrected 3→2); "
                                "G and M → son55, E.cost → sol.",
            "expectation_renumbering": "son55 local-1 → local-3, son55 local-2 → local-4 (merged with sol's same "
                                       "questions; A4).",
            "retained_vs_retained_gain": "Retention is shown (stores are read on later tasks); the retained-gain evidence "
                                         "is author-reported, prequential, single-stream and without spread. The PTC "
                                         "contribution is not supported on DB/OS.",
        },
    }

    # =========================================================== 2602.02369 Live-Evo (Δ15)
    p = "2602.02369"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Incorporate dynamic, up-to-date info (roster, coaching) as the event approaches.",
                    "Appendix A.2.2 retrieved experience",
                    "The retrieved experience pushes the memory-on arm toward searches close to the event, which is "
                    "where a query-edit time filter is most likely to leak results. Leakage can therefore differ "
                    "between the memory-on and memory-off arms; it is not a neutral common-mode error."),
            opus_ev(p, "O02", "For each new task batch, the agent operates through four stages:", "§3 (Algorithm 1)",
                    "Weights are updated inside the per-task loop of a batch, but the paper never states when each "
                    "task's outcome becomes available relative to the close times of later tasks in the same batch. That "
                    "information-timing condition is central to a live-forecasting memory, and it is unspecified."),
            opus_ev(p, "O03", "Brier Score: 0.5329", "Appendix A.2, Table 5",
                    "For truth Cincinnati=1, the baseline's (0.35, 0.65) gives multiclass Brier 0.845 by Eq. 1, and "
                    "Live-Evo's (0.55, 0.45) gives 0.405; the table prints 0.5329 and 0.2500. The showcase metric does "
                    "not follow the stated formula."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus follows sol. Adaptation is by conditioning a frozen backbone on retrieved, weight-ranked "
                      "experiences compiled into a guideline (C03 not executed). son55's controlled_diagnostic_design is "
                      "not retained: that card builds an evaluation instrument that isolates a confound for measurement. "
                      "Here the paired memory-on/off run is an in-loop credit signal whose outputs drive retention. "
                      "That operation is carried by the domain card H29 (S1 counterfactual), not by a diagnostic design.",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "evidence_gated_retention", "H29"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [pmap("son55", p, 0), {
            "rs_main": "adapt_via_conditioning", "rs_sub": None, "domain_namespace": "rsi",
            "domain_main": "abstract_experience_into_guidance", "domain_sub": "H00",
            "operation_correspondence": "Poorly solved tasks are summarised into failure-reason/improvement entries "
                                        "(H00 lessons) that later condition the compiled guideline (RS conditioning).",
            "necessary_conditions_differences": "H00 grounding is met (realised Brier). The H00 step-4 frozen-store "
                                                "evaluation is absent.",
            "evidence_ids": ["son55:E007", "son55:E008", "son55:E014"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2602.02369-1"): "local:2602.02369-2",
                    ("son55", "local:2602.02369-2"): "local:2602.02369-6",
                    ("son55", "local:2602.02369-3"): "local:2602.02369-7",
                    ("son55", "rs:controlled_diagnostic_design/RE-3"): "local:2602.02369-8"},
            overrides={
                "local:2602.02369-2": {
                    "status": "unmet", "score_item": "E.holdout",
                    "reason": "Opus (sol local-2 merged with son55 local-1, the same question). Status corrected from "
                              "'challenged_with_evidence', which is for a paper that rebuts an expectation with "
                              "evidence; here our evidence shows the paper does not meet it. The expectation is evidence "
                              "that only pre-close information was available. The filter is a query edit (sol:E007), and "
                              "the showcase reads 'Results confirm the game conclusion' and cites the final 33-31 score. "
                              "Under A2 this is charged to E.holdout only."},
                "local:2602.02369-3": {
                    "status": "unmet",
                    "reason": "Opus: status corrected from 'challenged_with_evidence' (same misuse). Table 5 Brier values "
                              "do not follow Eq. 1 for the printed probabilities (opus:O03), and the headline 20.8%/12.9% "
                              "do not follow from Table 2 (0.19→0.14 is −26%; 1.24→1.46 is +17.7%)."},
                "local:2602.02369-6": dict(RID("son55 local:2602.02369-2", "local:2602.02369-6")),
                "local:2602.02369-7": dict(RID("son55 local:2602.02369-3", "local:2602.02369-7")),
                "local:2602.02369-8": dict(conv("rs:controlled_diagnostic_design/RE-3")),
            }),
        "claims": lambda c: c,
        "assessment": assess(
            "son55", p,
            level_reason="Both seats retained; re-checked. Weights, experiences and meta-guidelines written from earlier "
                         "weeks are read on later, different tasks, and the same agent without experience is the "
                         "store-off control. Scoped: the evidence is author-reported and single-run, and temporal "
                         "isolation of web search is contradicted by the showcase (E.holdout 0), so the magnitude of the "
                         "retained gain is uncertain. Not improver.",
            strongest_supported_claim="On the reported 10-week stream, the memory system had lower average Brier than "
                                      "the same agent without experience and than ReMem, and each of four ablated "
                                      "components moved both metrics the same way (single run). Whether the gain survives "
                                      "leak-free retrieval is not established: the paper's own showcase shows post-close "
                                      "information reaching the memory-on arm."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Staleness and how-to-use-experience under live streams are "
                   "specific gaps. Neighbours (ExpeL, BoT, AWM, A-Mem, ReMem) are named and ReMem is run. Not 4: "
                   "staleness is never measured, and the 'first' claim is asserted against one empirical neighbour.",
                   ["son55:E001", "son55:E002", "son55:E030", "sol:E002"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Paired on/off credit, weight × similarity retrieval, a "
                   "learnable compile instruction bank and gated write-back are a coherent, reconstructable response. "
                   "Not 4: the credit is uniform over co-retrieved entries and rests on one noisy paired difference.",
                   ["son55:E003", "son55:E004", "son55:E005", "son55:E007", "son55:E008"], ["son55:E005"]),
            "X": R("resolved", 2, "Opus sides with sol. Retrieval and weight formulas and the main parameters are given. "
                   "But a key condition of a live loop, when each outcome becomes visible to later tasks in the same "
                   "batch, is unspecified (opus:O02). The commit gate is described both as 'statistically significant' "
                   "and as a 0.05 single-task threshold on the generating task. Meta-guidelines are added without any "
                   "gate, there is no rollback or size bound, and the similarity thresholds conflict (0.5 vs 0.3) → "
                   "anchor 2.",
                   ["sol:E003", "son55:E008", "son55:E013", "opus:O02"], ["son55:E013", "son55:E008"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Brier and market return fit the task. The "
                               "reported numbers have arithmetic problems: the headline percentages do not follow from "
                               "Table 2, and Table 5 Brier values do not follow Eq. 1 (opus:O03). Per A2, the search "
                               "leakage is charged to E.holdout and is not counted here; son55's reason double-counted it.",
                               ["son55:E020", "sol:E004", "opus:O03"], ["son55:E020", "opus:O03"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. The same agent without experience, ReMem, a four-"
                             "component ablation (weights, meta-guidelines, compile, active retrieval) and four "
                             "backbones all point the same way. The extra memory-off run is a learning-time cost of the "
                             "credit signal, not extra prediction-time budget for the reported arm, so it is charged to "
                             "E.cost. Not 4: the commit gate is unablated, there is no memory-off row on Xbench, ReMem "
                             "parity is unspecified, and every comparison is a single run.",
                             ["son55:E016", "son55:E017", "son55:E024", "son55:E021"], ["son55:E022"]),
            "E.holdout": R("resolved", 0, "Opus sides with sol. For a live-forecasting claim the holdout question is "
                           "temporal isolation. The paper asserts 'strict time-based retrieval' (sol:E005), implements it "
                           "by editing queries (sol:E007), and its own showcase trajectory reads 'Results confirm the game "
                           "conclusion' and reasons from the final 33-31 score (sol:E008, son55:E011). The retrieved "
                           "experience steers the credited arm toward near-event searches (opus:O01). No audit bounds "
                           "how many tasks are affected. The forward-in-time ordering of weeks is a real design strength, "
                           "but it cannot certify a prospective evaluation when outcomes can be retrieved from the web. "
                           "Anchor 0: the evidence contradicts the isolation claim. It is not not_reported: the evidence "
                           "exists and refutes the claim.",
                           ["sol:E005", "sol:E007", "sol:E008", "sol:E009", "son55:E011", "son55:E012", "opus:O01"],
                           ["sol:E008", "son55:E011", "son55:E012", "opus:O01"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Sample size (500) and weekly rows "
                              "(including weeks lost or tied) are given; there are no seeds, intervals or tests on "
                              "0.01–0.05 Brier margins.",
                              ["son55:E014", "son55:E015", "son55:E016", "son55:E018"]),
            "E.cost": R("not_reported", 0, "Opus sides with sol (precedent r09b AgentDevel: qualitative cost information "
                        "only → not_reported). The method states that every task is run twice and that candidates are "
                        "re-evaluated (son55:E029), and caps turns at 20 (sol:E011). No tokens, dollars, calls or time "
                        "are reported for any arm, and the baselines get no matched budget.",
                        ["son55:E029", "sol:E011"], [],
                        ["§3.3–3.4 method", "§4.1 setup and hyperparameters", "§4.2–4.5 results/ablation",
                         "§6 Limitations", "Appendix A.1 implementation details", "Appendix A.2–A.3 case and prompts"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendix A read; Figure 3 curves and the Figure 4 image were not estimated. "
                  "In scope (system_method, A class): experience bank with feedback-updated retrieval weights, a "
                  "meta-guideline bank and gated write-back are retained non-weight components. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Cumulative return / weekly Brier plots (Fig. 3) are image-only; Table 1 values are used instead.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", None]],
                "controlled_diagnostic_design not retained. The paired run is a credit signal inside the improvement "
                "loop, not an evaluation instrument built to measure a property; H29's S1 counterfactual already "
                "describes it.", ["son55:E003", "son55:E029"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["evidence_gated_retention", "H29"],
                 ["evidence_gated_retention", "H30"]],
                "All three are real correspondences. H29: entry weights are updated from with/without-memory gains. "
                "H30: commit only after a re-evaluation improvement, with soft retirement via down-weighting "
                "(medium fit: no size bound or hard retirement). H00: failure-reason/improvement entries are "
                "summarised from poorly solved trajectories. sol's note that the gate is not full H30 governance is "
                "reflected in the medium fit.", ["son55:E004", "son55:E006", "son55:E008", "son55:E028"], NOSCORE),
            XC(p, "local:2602.02369-1", "sol", "unmet",
               "A4 ID collision: sol's local-1 (X: the 'statistically significant' commit test is undefined) and son55's "
               "local-1 (leakage) are different questions. Final local-1 = sol's, verified unmet: the text says "
               "'statistically significant', the setup gives min_brier_improvement=0.05, and Algorithm 1 uses '>'. "
               "son55's question was merged into local-2.", ["sol:E003", "son55:E008", "son55:E013"]),
            XC(p, "local:2602.02369-2", "revised", "unmet",
               "Final local-2 = the leakage question (sol local-2 + son55 local-1). Both seats marked it "
               "'challenged_with_evidence', which is corrected to unmet (shared correction). son55's own local-2 (Xbench "
               "memory-off control) was renumbered local-6, unmet.", ["sol:E007", "sol:E008", "son55:E011", "opus:O01"]),
            XC(p, "local:2602.02369-3", "revised", "unmet",
               "Final local-3 = sol's question (metric arithmetic), status corrected from 'challenged_with_evidence' to "
               "unmet, verified with opus:O03. son55's own local-3 (weekly overclaim, no variance) was renumbered "
               "local-7, unmet.", ["sol:E009", "son55:E020", "opus:O03"]),
            XC(p, "local:2602.02369-4", "sol", "partial",
               "Verified: component ablations exist, but no other agent is given an equal number of total calls.",
               ["sol:E010", "son55:E024"]),
            XC(p, "local:2602.02369-5", "sol", "unmet",
               "Verified: no token, dollar or time figures for the paired runs or re-evaluations.", ["son55:E029"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: a memory-off control and ReMem; no summarise-all or longer-context variant.",
               ["son55:E016", "son55:E017"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: four modules ablated; gate and meta-guideline verification are not; single run.",
               ["son55:E024"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: conditioning-source quality is probed only by the two-entry case study.", ["son55:E027"]),
            XC(p, "rs:controlled_diagnostic_design/RE-3", "revised", {"moved_to": "local:2602.02369-8", "status": "unmet"},
               "The card is not retained. The check (the second run is uncosted extra compute and the noise of a "
               "single-sample difference is unmeasured) is valid and is kept as local-8, unmet.",
               ["son55:E005", "son55:E029"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55", "unmet",
               "Verified: memory keeps updating on the reported weeks, and there is no frozen-store test.",
               ["son55:E014", "son55:E015"]),
            XC(p, "rsi:evidence_gated_retention/F4", "son55", "unmet",
               "Verified (failure present): credit needs a paired rollout per task and is spread over all retrieved "
               "entries.", ["son55:E005", "son55:E029"]),
            XC(p, "rsi:evidence_gated_retention/H29", "sol", "partial",
               "Verified: value-weighted retrieval is ablated (w/o weight-update), but credit is group-level, not per "
               "entry.", ["sol:E001", "son55:E024"]),
            XC(p, "rsi:evidence_gated_retention/H29-step5", "son55", "partial",
               "Verified: a value-stripped ablation exists; there is no held-out frozen-bank test.",
               ["son55:E024", "son55:E014"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "met",
               "Verified: every weight update is backed by a memory-on vs memory-off contrast on the same task. The "
               "group-level sharing of credit is recorded under H29 (partial).", ["son55:E003", "son55:E004"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "partial",
               "Verified: an admission gate plus soft retirement through weights; no hard bound or versioned rollback.",
               ["son55:E006", "son55:E008"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "unmet",
               "Verified: the cost of the extra contrastive and re-evaluation runs is not stated.", ["son55:E029"]),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.X: the information-timing condition is unspecified (opus:O02), the gate has two "
                "contradictory definitions, meta-guidelines are ungated, and there is no rollback.",
                ["opus:O02", "son55:E008", "son55:E013"], "−5.0 vs son55 (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.causality: the right kinds of controls exist (store-off, rival memory, component "
                "ablations, backbones). sol's budget point concerns the learning-time cost of the credit signal and "
                "is charged to E.cost (A2).", ["son55:E016", "son55:E024", "son55:E021"], "+3.75 vs sol (15×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 0},
                "See ratings.E.holdout: the paper's own trajectory contradicts its temporal-isolation claim, and the "
                "method steers the credited arm toward near-event retrieval. son55's 2 credited the forward ordering, "
                "but ordering cannot hold out outcomes that are retrievable from the web.",
                ["sol:E008", "son55:E011", "opus:O01", "sol:E007"], "−5.0 vs son55 (10×2/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol",
                {"status": "not_reported", "rating": 0},
                "See ratings.E.cost: only qualitative cost information (precedent r09b AgentDevel).",
                ["son55:E029", "sol:E011"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2602.02369-2].status (leakage question; son55's copy was local-1)",
             "sol_value": "challenged_with_evidence", "son55_value": "challenged_with_evidence", "final_value": "unmet",
             "reason": "Both seats used 'challenged_with_evidence' to mean 'our evidence challenges the paper'. In SCORE_SPEC "
                       "that status is for a paper that rebuts an expectation with its own evidence. The correct status "
                       "for an expectation the paper fails is unmet (same correction for sol's local-3).",
             "evidence_ids": ["sol:E008", "son55:E011"], "score_impact": "none (expectations are not scored directly)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: on/off paired credit, "
                                                   "gated write-back, weekly stream; the A.2 showcase reads the game "
                                                   "result ('Results confirm the game conclusion', '33-31'); Table 5 Brier "
                                                   "values do not follow Eq. 1; single run. Initial bands G3 M3 X2 Em2 "
                                                   "Ec2–3 Eh0–1 Es1 Ecost0.",
            "integrity_checks": "Both seats a1 on 2602.02369v1, material sha 4aecd66f…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid.",
            "core_claim_check": "Re-read §3.1–3.4, §4.1–4.5, A.1–A.3. The leakage evidence (A.2.4 Observation 3; Table 5 "
                                "reasoning) is quoted by both seats; Opus added the steering mechanism (opus:O01) and the "
                                "Brier arithmetic (opus:O03).",
            "rating_agreement": "Four of eight items agree and were re-checked (son55's E.measurement reason narrowed per "
                                "A2). X, E.holdout and E.cost → sol; E.causality → son55.",
            "expectation_renumbering": "son55 local-1 → local-2 (merged), local-2 → local-6, local-3 → local-7; "
                                       "controlled_diagnostic_design/RE-3 → local-8.",
            "retained_vs_retained_gain": "Retention is real (weights/entries are reused across weeks). The retained-gain "
                                         "magnitude is not certified because search leakage is demonstrated and "
                                         "unbounded.",
        },
    }

    # =========================================================== 2602.02474 MemSkill
    p = "2602.02474"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "achieving the best results across all three settings", "§4.3",
                    "K=7 is described as the best value on the reported HotpotQA curves, and K=7 is then used for "
                    "LoCoMo/LongMemEval evaluation (training uses K=3). The evaluation-time K looks chosen on "
                    "reported results."),
            opus_ev(p, "O02", "Span Size=512 offers the best overall balance, achieving the highest quality with much "
                              "lower runtime cost than MemoryOS, A-MEM, and LightMem.", "§4.5 Cost analysis",
                    "The default span size coincides with the best point of a sweep run on the reported LoCoMo split "
                    "(non-monotone: 53.14/51.61/53.82/48.11/50.46), which also shows ±2–5 point sensitivity."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus follows son55: one primary card. The fixed component of a staged memory-construction procedure "
                      "(hand-written operations and their granularity) becomes a learnable, evolvable variable, and the "
                      "w/o-designer ablation reverts it. sol's supporting adapt_via_conditioning is dropped. Its defining "
                      "condition (adaptation without per-task parameter updates) does not hold in-domain, because the "
                      "selector is PPO-trained per dataset (ALFWorld trained separately). The conditioning interface is "
                      "only how skills are consumed. No sub-card fits (C15/C23/C24 are 3D/diffusion tactics).",
            "matches": [smatch("son55", p, "generative_process_redesign")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H11"),
                                       dmatch("sol", p, "make_the_improver_editable", "H21"),
                                       dmatch("son55", p, "amortize_improver_into_trained_policy", "H26")],
                           "unassigned": [],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [pmap("son55", p, 0), pmap("son55", p, 1), {
            "rs_main": "generative_process_redesign", "rs_sub": None, "domain_namespace": "rsi",
            "domain_main": "amortize_improver_into_trained_policy", "domain_sub": "H26",
            "operation_correspondence": "Which skills shape each memory write is decided by an MLP selector trained "
                                        "with PPO on downstream QA/success after the memory is built (H26 credit "
                                        "through downstream use). It is the learned half of the liberated component.",
            "necessary_conditions_differences": "Edge fit: the trained policy selects skills; the frozen LLM writes. "
                                                "The reader is not co-trained (S3 unmet).",
            "evidence_ids": ["son55:E005", "son55:E006"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2602.02474-1"): "local:2602.02474-4"},
            overrides={
                "local:2602.02474-2": {
                    "status": "partial",
                    "reason": "Opus (status revised from son55's unmet). The main ALFWorld table uses in-context "
                              "demonstrations and memory built from expert training-split trajectories. Table 5 "
                              "(no demonstrations) is reported for all methods and removes the demonstration confound "
                              "(57.71 vs 45.99 LightMem). The expert-trajectory corpus is a shared, privileged source "
                              "for every method. Partial, not unmet."},
                "local:2602.02474-4": dict(RID("son55 local:2602.02474-1", "local:2602.02474-4")),
                "rsi:make_the_improver_editable/S4": {
                    "status": "unmet",
                    "reason": "Opus sides with son55. S4 asks for the search/evolution cost. Only inference-time cost is "
                              "reported, and the preparation (PPO + designer) cost is explicitly excluded as 'amortized'. "
                              "Inference tokens are not search cost."},
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed object (hand-designed memory operations) is named "
                   "and shown to be a bottleneck (w/o Des), and neighbours are listed. Not 4: the learned memory-manager "
                   "neighbours (Memory-R1, Mem-α, MemEvolve) are dismissed in text and not compared, and brittleness is "
                   "cited rather than measured.",
                   ["son55:E001", "son55:E002", "son55:E003", "son55:E023", "sol:E004"], ["son55:E003"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Downstream-reward selector, clustered hard cases, bounded "
                   "designer edits and an exploration bias form a reconstructable mechanism with a distinguishing "
                   "prediction (fixed primitives lose). Not 4: span granularity is changed at the same time, and the "
                   "selector works over a small bank (K=7 of ≈9).",
                   ["son55:E005", "son55:E006", "son55:E008", "son55:E011", "son55:E023"], ["son55:E026", "son55:E027"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Edit cap, snapshot rollback on tail-average reward, early "
                   "stopping, buffer expiry, exploration schedule and full prompts are given. Not 4: there is no "
                   "disjoint commit split, delete/noop are frozen, nothing is retired, and patience, rounds and final "
                   "bank size are not stated.",
                   ["son55:E009", "son55:E010", "son55:E011", "son55:E012", "son55:E035", "sol:E005", "sol:E012"],
                   ["son55:E010", "son55:E012"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Programmatic ALFWorld success, F1 and an LLM "
                               "judge (gpt-oss-120b, a different family from the base models), with stated rubrics. The "
                               "training reward is F1/success, not the judge. Not 4: the judge is not validated, and F1 "
                               "and L-J disagree on Qwen LongMemEval.",
                               ["son55:E017", "son55:E018", "son55:E021", "sol:E013"], ["son55:E021"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. The retained object is isolated by internal "
                             "ablations on two LLMs: w/o designer (fixed four primitives, same selector training and "
                             "span granularity) 46.50/36.15, refine-only 47.45/48.88, random selection 48.43/42.84, vs "
                             "53.82/54.14. A no-demonstration ALFWorld control and added experience baselines (LightMem, "
                             "AWM, ExpeL) are also reported. Not 4: the ablations cover LoCoMo only (≈2 test "
                             "conversations), each is a single run, RL memory-manager rivals are absent, and the "
                             "controller ablation is weak (7 of ≈9 skills).",
                             ["son55:E023", "son55:E037", "sol:E010"], ["son55:E003", "son55:E026", "son55:E027"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. LoCoMo is split by conversation (6/2/2), rollback "
                           "uses the training reward, ALFWorld uses the official seen/unseen splits, and there is "
                           "zero-shot transfer to LongMemEval/HotpotQA and to a second LLM. Not 4: tiny test sets, "
                           "LongMemEval configurations tuned on its validation split, and evaluation-time K and span size "
                           "apparently picked from reported curves (opus:O01, opus:O02).",
                           ["son55:E013", "son55:E014", "son55:E016", "sol:E007", "sol:E008", "sol:E009", "opus:O01",
                            "opus:O02"], ["son55:E028", "opus:O01", "opus:O02"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Sizes and per-metric rows, including "
                              "small and negative margins (AppWorld, span sweep), are given; there are no seeds, "
                              "intervals or tests.",
                              ["son55:E013", "son55:E014", "son55:E033", "son55:E034"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Inference tokens, calls and quality are tabulated "
                        "against three baselines across span sizes. The PPO and designer evolution cost, which the "
                        "self-evolving claim depends on, is excluded as amortized.",
                        ["son55:E025", "son55:E026", "sol:E011"], ["son55:E025"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–F read; Figure 3 bars and the Figure 4 image were not "
                  "estimated. In scope (system_method, A class): the evaluated retained object is a non-weight text "
                  "skill bank. Under A3 the small trained selector does not exclude the paper. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "HotpotQA transfer magnitudes (Fig. 3) are image-only; no rating relies on them.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["generative_process_redesign", None]],
                "adapt_via_conditioning dropped: in-domain use trains the selector per dataset, so the card's "
                "no-parameter-update premise fails. Conditioning is only the consumption interface.",
                ["son55:E005", "sol:E006"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["amortize_improver_into_trained_policy", "H26"], ["attribute_and_patch_incumbent", "H11"],
                 ["make_the_improver_editable", "H21"]],
                "Each card names a distinct executed operation. H11: clustered failures → bounded skill rewrites (≤3) → "
                "kept only if the cycle reward does not regress. H21: an outer loop redesigns the memory-construction "
                "mechanism. H26: a selector trained on downstream utility of the written memory (edge fit). sol's H21 "
                "entry (fit high) is used for H21.", ["son55:E005", "son55:E008", "son55:E009", "sol:E004"], NOSCORE),
            XC(p, "local:2602.02474-2", "revised", "partial",
               "See the expectation override: Table 5 removes the demonstration confound for all methods, and the "
               "expert corpus is shared → partial.", ["son55:E015", "sol:E009"]),
            XC(p, "local:2602.02474-3", "son55", "partial",
               "Verified: F1 and L-J are both reported; they disagree on Qwen LongMemEval; the judge is unvalidated.",
               ["son55:E017", "son55:E021"]),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "met",
               "Verified: w/o Des reverts to the four primitives and loses 7.3 / 18.0 L-J.", ["son55:E023"]),
            XC(p, "rs:generative_process_redesign/RE-2", "son55", "partial",
               "Verified: many fixed-pipeline baselines; RL memory managers and MemEvolve are not run.",
               ["son55:E003", "son55:E037"]),
            XC(p, "rs:generative_process_redesign/RE-6", "son55", "met",
               "Verified: an inference quality–cost frontier over span sizes vs three baselines (Table 3). It covers "
               "inference only; training cost is charged under make_the_improver_editable/S4 and E.cost.",
               ["son55:E026"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S2", "son55", "met",
               "Verified: the selector reward is QA/success after memory construction.", ["son55:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "partial",
               "Verified: the designer prompt triages storage/retrieval/quality failures; attribution accuracy is not "
               "measured.", ["son55:E008"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "partial",
               "Verified: best-snapshot rollback; only failures are fed to the designer; commit on training reward.",
               ["son55:E009", "son55:E010"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "son55", "met",
               "Verified: hard cases are clustered by query type before the designer edits.", ["son55:E008"]),
            XC(p, "rsi:make_the_improver_editable/F3", "sol", "partial",
               "Verified (failure partly present): LoCoMo is held out by conversation, but LongMemEval configurations "
               "are tuned on its validation split, and K and span size look chosen on reported curves.",
               ["sol:E007", "sol:E008", "opus:O01"]),
            XC(p, "rsi:make_the_improver_editable/H21-step4", "son55", "partial",
               "Verified: disjoint splits for LoCoMo and transfer sets; target-side tuning noted.",
               ["son55:E013", "son55:E014"]),
            XC(p, "rsi:make_the_improver_editable/S2", "sol", "met",
               "Verified: skills are scored by downstream task reward of the memory they produce.", ["sol:E003"]),
            XC(p, "rsi:make_the_improver_editable/S3", "sol", "met",
               "Verified: compared against the fixed hand-designed primitive set (w/o Des) and refine-only.",
               ["sol:E010", "son55:E023"]),
            XC(p, "rsi:make_the_improver_editable/S4", "son55", "unmet",
               "S4 concerns search cost. Only inference cost is given, and preparation cost is excluded (son55:E025).",
               ["son55:E025", "sol:E011"]),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.E.causality: the decisive control for the retained skill bank (fixed primitives, same "
                "selector and granularity) is run on two LLMs. sol's untrained-baseline budget point is real but "
                "does not undo the internal isolation; the missing training cost is charged to E.cost (2).",
                ["son55:E023", "sol:E010"], "+3.75 vs sol (15×1/4)"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full v2 text before opening the seats: text skill bank + "
                                                   "PPO selector; w/o Des −7.3/−18.0; LoCoMo test ≈2 conversations; "
                                                   "inference-only cost; K/SS seemingly picked on reported curves. "
                                                   "Initial bands G3 M3 X3 Em3 Ec3 Eh2–3 Es1 Ecost2; evidence_level "
                                                   "retained.",
            "integrity_checks": "Both seats a1 on 2602.02474v2, material sha 59deea69…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid.",
            "core_claim_check": "Re-read §3.4, §4.1–4.5, Appendix A.1–A.4, B.1–B.3, C, D.",
            "rating_agreement": "Seven of eight items agree; each was re-checked against the text (E.holdout kept at 3 "
                                "with K/SS selection noted). E.causality → son55.",
            "expectation_renumbering": "son55 local-1 → local-4 (A4 collision with sol local-1).",
            "retained_vs_retained_gain": "The best skill bank is deployed frozen on held-out conversations and transfer "
                                         "sets; w/o Des isolates its effect → retained. The designer is fixed, so not "
                                         "improver.",
        },
    }

    # =========================================================== 2602.02979 CPMöbius (both out_of_scope)
    p = "2602.02979"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "Coach is updated by REINFORCE and the Player by GRPO (son55:E002–E004, sol:E001). The only non-weight "
          "artifacts, the Coach's questions, are filtered by a 0.2–0.8 consistency band, consumed by one GRPO batch "
          "and discarded (son55:E005). The algorithm returns trained policies (sol:E002), and every reported result "
          "is a trained checkpoint. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "opus_evidence": [],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). The Coach generates questions, the Player's majority vote supplies "
                      "pseudo-labels, a difficulty band filters them, and both policies are retrained. This is C08's "
                      "generate → filter → retrain loop and the run convention for proposer–solver co-training (r05b "
                      "R-Zero, r07a SPELL, r08b Agent0, r09b GenEnv). sol's empty identification is allowed for an "
                      "excluded row; it is filled in for corpus statistics.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering",
                               fit="medium (informational, out_of_scope)")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={"local:2602.02979-1": {"note": "Informational only: the paper is out_of_scope, so the "
                                                      "expectation is not applied (status kept as son55 recorded)."}}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b–r09b).",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; the benchmark gains are author-reported "
                                             "results of trained checkpoints.",
                       "strongest_supported_claim": None,
                       "unresolved": ["The out-of-scope disposition is not a judgment that the weight-training results "
                                      "are wrong."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "figure_dependence": None,
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "For out-of-scope rows the canonical value is null (precedent r05b–r09b). sol's 'task' describes the "
                "weight-training result, which this ladder does not grade.", ["son55:E002", "sol:E002"],
                "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Null is canonical for out-of-scope rows (r09b GenEnv). Both sol's 'scoped' and son55's 'unresolved' "
                "are replaced; neither is a judgment under this rubric.", ["son55:E002"], "none"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "Informational C08 identification per the run convention for proposer–solver co-training; sol left it "
                "blank (allowed for out_of_scope).", ["son55:E005", "son55:E002"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]], "Follows primary.", ["son55:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["self_generate_the_curriculum", "H22"]],
                "Informational: H22 (a proposer co-trained against a solver with a learning-progress reward) is the "
                "domain card for this weight-level loop. The match does not bring the paper into scope.",
                ["son55:E002", "son55:E003"], NOSCORE),
            XC(p, "local:2602.02979-1", "son55", "unknown",
               "Informational only (applicable=false as son55 recorded): the paper is out_of_scope, so the holdout "
               "question is not graded.", ["son55:E006", "son55:E007"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1, §4 (Coach/Player, rewards), §5.1 and the ablation before "
                                                   "opening the seats: REINFORCE Coach + GRPO Player; per-round "
                                                   "questions are consumed, not retained → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2602.02979v3, material sha f4eb0c8f…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "Searched the text for any buffer, library or retained prompt: none.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2602.04837 GEA
    p = "2602.04837"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Claude Sonnet 4.5 SWE-bench 60 $370", "Appendix A.1 cost table",
                    "The breakdown covers only coding-model calls per 60 tasks. The o1 reflection calls and the larger "
                    "pooled-trace inputs, which are exactly what GEA changes, are not itemised, and the totals are "
                    "'estimated'."),
            opus_ev(p, "O02", "To mitigate the substantial cost of evaluating every evolved agent on the full "
                              "benchmarks, we adopt a staged evaluation strategy where agents must pass smaller subsets "
                              "before advancing.", "§4.1",
                    "Per-agent scores come from staged subsets (10 + 50 tasks). The 1/60 granularity of 20.0/56.7/48.3/"
                    "45.0/63.3/58.3 and of Polyglot 88.3/68.3 fits a 60-task pool, while the headline 71.0% does not."),
        ],
        "rs_pattern": {
            "primary": "assumption_audit_and_pivot", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus follows sol and the run precedent r07b Huxley-Gödel Machine (a DGM-family modification → "
                      "assumption_audit_and_pivot with H20). The audited, load-bearing assumption is single-parent "
                      "lineage isolation. GEA violates it by pooling traces across a parent group and demonstrates the "
                      "new behaviour (cross-branch tool consolidation). son55's generative_process_redesign is not "
                      "retained: the 'fixed component' would be the evolutionary unit of a search procedure, which would "
                      "make every change to an optimizer a liberated component (precedent r09b RoboPhD). No sub-card "
                      "fits (C01/C05/C11/C19/C28/C29 concern safety, identifiability or bounds).",
            "matches": [smatch("sol", p, "assumption_audit_and_pivot")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("sol", p, "make_the_improver_editable", "H20")],
                           "unassigned": ["H14 not assigned: H20's own differentiation separates archives of "
                                          "self-modifying agents from evolving executable programs. H15 not assigned: "
                                          "GEA pools raw traces of the current parent group each iteration; there is "
                                          "no distilled, credited knowledge layer that persists and is updated "
                                          "(sol's note)."],
                           "revision_proposals": seat("son55", p)["domain_pattern"]["revision_proposals"]},
        "pattern_mapping": [pmap("sol", p, 0), pmap("son55", p, 1, rs_main="assumption_audit_and_pivot",
                                                     operation_correspondence="The pivot (pooled cross-lineage traces) "
                                                     "is executed through H12's step: reflection over raw traces "
                                                     "yields framework-level patches to each agent's own code.")],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2602.04837-1"): "local:2602.04837-5",
                    ("son55", "local:2602.04837-2"): "local:2602.04837-6",
                    ("son55", "local:2602.04837-3"): "local:2602.04837-2",
                    ("son55", "local:2602.04837-4"): "local:2602.04837-1",
                    ("son55", "rs:generative_process_redesign/RE-1"): "local:2602.04837-7",
                    ("son55", "rs:generative_process_redesign/RE-2"): "local:2602.04837-8",
                    ("son55", "rs:generative_process_redesign/RE-3"): "local:2602.04837-9",
                    ("son55", "rs:generative_process_redesign/RE-5"): "local:2602.04837-10",
                    ("sol", "rsi:population_search_executable_fitness/S5"): "local:2602.04837-11"},
            overrides={
                "local:2602.04837-1": {
                    "status": "unmet",
                    "reason": "Opus (sol local-1 merged with son55 local-4, the same question; shared correction from "
                              "unknown). The expectation is that every headline figure has a stated evaluation set and "
                              "denominator. It is plainly not met: 56.7/88.3/68.3/20.0 fit a 60-task pool, 71.0 does "
                              "not, and only 'top-2 on full Verified' is mentioned (opus:O02). Which set produced 71.0% "
                              "remains unknown and is not guessed; the status records the reporting failure."},
                "local:2602.04837-5": {
                    "status": "partial",
                    "reason": "Opus (son55 local-1 renumbered; status corrected from 'challenged_with_evidence'). The "
                              "Haiku→Sonnet switch inflates the absolute 20%→71% rise and the 'mid-to-late "
                              "acceleration'. The GEA-vs-DGM comparison runs both arms under the same schedule, and the "
                              "transfer test fixes the backbone, so the confound is controlled for the comparative claim "
                              "only → partial."},
                "local:2602.04837-6": dict(RID("son55 local:2602.04837-2", "local:2602.04837-6")),
                "local:2602.04837-7": dict(conv("rs:generative_process_redesign/RE-1")),
                "local:2602.04837-8": dict(conv("rs:generative_process_redesign/RE-2")),
                "local:2602.04837-9": dict(conv("rs:generative_process_redesign/RE-3")),
                "local:2602.04837-10": dict(conv("rs:generative_process_redesign/RE-5")),
                "local:2602.04837-11": dict(conv("rsi:population_search_executable_fitness/S5")),
                "rsi:make_the_improver_editable/F3": {
                    "status": "unmet",
                    "reason": "Opus sides with son55 (failure present). The ≈60-task staged sets drive parent "
                              "selection and are the reported scores; the Polyglot medium set is used to pick agents; "
                              "the improver reads failures of evaluation tasks."},
                "rsi:make_the_improver_editable/F4": {
                    "status": "unmet",
                    "reason": "Opus sides with son55 (failure present). There is one evolution run per method; the five "
                              "bug-repair trials do not give the main comparison any variance."},
            }),
        "claims": lambda c: c,
        "assessment": assess(
            "son55", p,
            level_reason="Opus sides with son55 (EVIDENCE rule 2; precedent r03b SICA). The comparative numbers are on "
                         "the staged sets that drive parent selection, and the best Polyglot agent is picked by its "
                         "medium-set score. Only the top-2 SWE agents get a full-benchmark run, and its denominator is "
                         "ambiguous. Model transfer re-runs the same benchmark tasks. Retained code is reused across "
                         "iterations, but no independent task set shows the retained edits help → task. Contrast r07b "
                         "HGM (retained via 207 overlap-filtered Lite tasks)."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A concrete bottleneck (isolated branches lose discovered "
                   "tools), partly measured (4 of 9 tools never reach DGM's best agent), with DGM as the clear nearest "
                   "neighbour. Not 4: population methods that already share information across candidates are not "
                   "examined.",
                   ["son55:E001", "son55:E002", "son55:E023", "son55:E024", "sol:E001", "sol:E007"], ["son55:E018"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Pooling patches, logs and outcomes of a performance–novelty "
                   "parent group into every member's reflection is a clear operation that predicts faster cross-branch "
                   "propagation. Not 4: selection rule, K and extra context are not separated from sharing.",
                   ["son55:E007", "son55:E008", "son55:E004", "sol:E003"], ["son55:E018"]),
            "X": R("resolved", 2, "Opus sides with son55. Algorithms 1–2 give the loop, but key conditions are unclear. "
                   "The probe-task set behind z_i and the task set behind α_i are never named, and α mixes Haiku-era and "
                   "Sonnet-era scores. Admission is compile/basic-function only, with no regression check or rollback. "
                   "The reflection/evolution prompts are not given, and edit permissions are unaudited ('Updated tests "
                   "logic'). This fits anchor 2 (key conditions and recovery unclear), unlike r07b HGM, whose algorithm "
                   "and parameters were fully specified.",
                   ["son55:E003", "son55:E005", "son55:E006", "son55:E009", "son55:E014", "sol:E014", "sol:E015"],
                   ["son55:E009", "son55:E006"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Execution-based pass rates are valid verifiers, "
                               "but the headline figures mix denominators (1/60 multiples vs 71.0%, opus:O02), and the "
                               "human-framework comparison sets 60-task Claude subsets against full-benchmark GPT-5 "
                               "entries.",
                               ["son55:E011", "son55:E020", "son55:E022", "son55:E023", "sol:E008", "opus:O02"],
                               ["son55:E012", "son55:E022"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. There is one re-implemented DGM baseline at a "
                             "matched agent count and model schedule, a backbone-transfer control and observational "
                             "tool-provenance data. There is no ablation separating sharing from selection or K. The "
                             "bug-repair test gives the treatment a healthy peer by construction.",
                             ["son55:E019", "son55:E024", "son55:E026", "son55:E027", "sol:E007", "sol:E009", "sol:E012"],
                             ["son55:E017", "son55:E018", "son55:E028"]),
            "E.holdout": R("resolved", 1, "Opus sides with son55 (precedent r03b SICA / cal-h1-v2 POET: selection and "
                           "test coincide → 1). Staged sets drive both selection and reporting. Benchmark tasks and their "
                           "outcomes feed the improver. The Polyglot '50-task unseen' set is used to pick agents, and "
                           "88.3% = 53/60 looks pooled with the 10 evolution tasks. Only the top-2 SWE agents get a full "
                           "run (mostly unseen tasks, but its figure is ambiguous). sol's 2 took the Polyglot separation "
                           "at face value.",
                           ["son55:E007", "son55:E011", "son55:E012", "son55:E013", "sol:E005", "sol:E006"],
                           ["son55:E013"]),
            "E.statistics": R("resolved", 1, "Opus sides with son55 (A2 ladder). The main result is one evolution run "
                              "per method with no interval (one task = 1.7 points). The five bug-repair trials give "
                              "per-trial counts for a secondary claim only, so the ladder's level 2 (uncertainty on the "
                              "tested result) is not reached for the central claim.",
                              ["son55:E020", "son55:E023", "son55:E027", "sol:E011"]),
            "E.cost": R("resolved", 2, "Opus sides with sol (precedent r07b HGM: totals without per-arm measured use → "
                        "2). Run totals (≈$13k SWE, ≈$1.5k Polyglot) and a per-60-task coding-model table are given. "
                        "They are estimates, parity is argued from equal agent counts, and the o1 reflection calls and "
                        "the larger pooled-trace inputs (the component GEA changes) are not itemised (opus:O01).",
                        ["sol:E007", "sol:E013", "son55:E029", "son55:E030", "opus:O01"], ["son55:E030", "opus:O01"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendix A read; Figures 3–5 are image-only and were not estimated. In "
                  "scope (system_method, A class): self-modified agent code (tools, workflow, prompts) is retained in "
                  "an archive and re-used as parents. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Performance curves (Fig. 3), the tool matrix (Fig. 4) and model-transfer bars (Fig. 5) are "
                             "image-only; only the text statements about them are used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "See assessment.level_reason: the reported scores are on selection-contaminated staged sets, the "
                "Polyglot medium set is used for picking, and no independent task set exists (EVIDENCE rule 2).",
                ["son55:E011", "son55:E013", "sol:E005", "sol:E006"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "assumption_audit_and_pivot",
                "Run precedent r07b HGM for DGM-family changes. Violating single-lineage isolation is the audited "
                "assumption; generative_process_redesign would cover any change to a search procedure.",
                ["sol:E001", "sol:E003", "son55:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["assumption_audit_and_pivot", None]],
                "Follows primary.", ["sol:E001"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H12"], ["make_the_improver_editable", "H20"]],
                "H20 kept (both seats). H12 added from son55: each child is a trace-diagnosed patch of the agent's own "
                "harness code (raw logs and patches → framework patch); medium fit, with no replay/rollback. sol's H14 "
                "is not retained (H20's differentiation excludes it). son55's H15 is not retained (no persistent, "
                "distilled and credited knowledge layer).", ["son55:E007", "son55:E008", "son55:E009", "sol:E003"],
                NOSCORE),
            XC(p, "local:2602.04837-1", "revised", "unmet",
               "A4: sol's local-1 and son55's local-4 are the same question (headline evaluation set). Both seats said "
               "unknown, corrected to unmet (shared correction): the requirement is a stated denominator, and the paper "
               "fails it, while the true set remains unknown. son55's local-1 (model switch) moved to local-5 (partial).",
               ["sol:E008", "son55:E012", "son55:E020", "opus:O02"]),
            XC(p, "local:2602.04837-2", "sol", "partial",
               "sol's local-2 and son55's local-3 are the same question (the bug test gives GEA a healthy peer). Verified "
               "partial. son55's own local-2 (human-framework comparison) moved to local-6, unmet.",
               ["sol:E012", "son55:E028"]),
            XC(p, "local:2602.04837-3", "revised", {"moved_to": "local:2602.04837-2", "status": "partial"},
               "son55's local-3 was merged into local-2 (same question).", ["son55:E027", "son55:E028"]),
            XC(p, "local:2602.04837-4", "revised", {"moved_to": "local:2602.04837-1", "status": "unmet"},
               "son55's local-4 was merged into local-1 (same question); status corrected from unknown to unmet.",
               ["son55:E012", "son55:E020"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-4", "sol", "partial",
               "Verified: the DGM lineage is clear; closer multi-parent or shared-archive precedents are not checked.",
               ["sol:E001", "sol:E007"]),
            XC(p, "rs:assumption_audit_and_pivot/RE-6", "sol", "partial",
               "Verified: tool provenance and the DGM counterfactual support the isolation loss, but novelty, K and "
               "context length are not controlled.", ["sol:E003", "sol:E009"]),
            XC(p, "rs:generative_process_redesign/RE-1", "revised", {"moved_to": "local:2602.04837-7", "status": "partial"},
               "The card is not retained. Its check (an ablation removing only the redesign) is kept as local-7, partial: "
               "tools are lost in isolated DGM branches, but there is no sharing-only ablation.",
               ["son55:E024", "son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-2", "revised", {"moved_to": "local:2602.04837-8", "status": "partial"},
               "Kept as local-8, partial: the re-implemented DGM is the only evolutionary baseline.",
               ["son55:E018", "son55:E019"]),
            XC(p, "rs:generative_process_redesign/RE-3", "revised", {"moved_to": "local:2602.04837-9", "status": "unmet"},
               "Kept as local-9, unmet: selection, sharing and K are not separately ablated.",
               ["son55:E004", "son55:E015", "son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-5", "revised", {"moved_to": "local:2602.04837-10", "status": "partial"},
               "Kept as local-10, partial: the agent-count parity holds, but pooled inputs and the model switch are "
               "not costed.", ["son55:E019", "son55:E030"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "unmet",
               "Verified: admission is compile/basic-function only, with no regression replay or rollback.",
               ["son55:E009", "son55:E014"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met",
               "Verified: full tool-invocation logs, patches and outcomes are given to reflection.",
               ["son55:E007", "son55:E008"]),
            XC(p, "rsi:make_the_improver_editable/F3", "son55", "unmet",
               "Failure present; consistent with E.holdout 1.", ["son55:E011", "son55:E013"]),
            XC(p, "rsi:make_the_improver_editable/F4", "son55", "unmet",
               "Failure present; consistent with E.statistics 1.", ["son55:E020", "sol:E011"]),
            XC(p, "rsi:make_the_improver_editable/H20-step5", "son55", "partial",
               "Verified: backbone transfer vs the iteration-0 agent; no held-out tasks or seeds.",
               ["son55:E026"]),
            XC(p, "rsi:make_the_improver_editable/S1", "sol", "partial",
               "Verified: the selection formula and schedule are fixed, but the evaluator's protection from agent edits "
               "is unaudited.", ["sol:E014", "sol:E015"]),
            XC(p, "rsi:make_the_improver_editable/S3", "son55", "partial",
               "Verified: compared with an individual-lineage evolver; no fixed hand-designed group-mechanism baseline.",
               ["son55:E018"]),
            XC(p, "rsi:make_the_improver_editable/S4", "sol", "partial",
               "Verified: estimated totals per method; no measured per-arm usage (opus:O01).", ["sol:E013", "opus:O01"]),
            XC(p, "rsi:make_the_improver_editable/S5", "sol", "met",
               "Verified: every compiling, functional child is archived, whether or not it improves.", ["sol:E004"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "revised",
               {"moved_to": "local:2602.04837-11", "status": "partial"},
               "population_search_executable_fitness is not retained (H14/H15 dropped). The check (shared memory earns "
               "its place by a measured effect) is kept as local-11, partial: there is ancestry tracing but no "
               "credit/ablation.", ["sol:E007", "sol:E009"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.X: the selection-signal task sets are unnamed, archive scores mix model eras, admission is "
                "minimal with no rollback, and the prompts are absent.", ["son55:E005", "son55:E006", "son55:E009"],
                "−5.0 vs sol (20×1/4)"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.holdout: selection and reporting coincide; the Polyglot medium set is used for picking.",
                ["son55:E012", "son55:E013", "sol:E006"], "−2.5 vs sol (10×1/4)"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.statistics: the A2 ladder applies to the main result; the bug trials cover a secondary "
                "claim.", ["son55:E020", "son55:E027"], "−1.25 vs sol (5×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.cost: estimated totals; the component GEA changes (pooled reflection input, o1 calls) "
                "is not costed, so parity is asserted rather than shown.", ["sol:E013", "opus:O01", "son55:E030"],
                "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2602.04837-1].status (son55's copy was local-4)",
             "sol_value": "unknown", "son55_value": "unknown", "final_value": "unmet",
             "reason": "Both seats recorded unknown for 'headline figures have a stated evaluation set'. The underlying "
                       "set is unknown, but the expectation asks whether the paper states it, and it does not. Unknown "
                       "would leave a resolvable check open. The actual denominator of 71.0% is not guessed.",
             "evidence_ids": ["son55:E012", "son55:E020", "opus:O02"],
             "score_impact": "none (expectations are not scored directly; E.measurement 2 already reflects it)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats: K=2 parent groups, "
                                                   "pooled traces, staged 10/50 evaluation; Table 1 values are 1/60 "
                                                   "multiples except 71.0; Polyglot medium set used for picking; one run "
                                                   "per method; estimated cost. Initial bands G3 M3 X2 Em2 Ec2 Eh1 Es1 "
                                                   "Ecost2; evidence_level task.",
            "integrity_checks": "Both seats a1 on 2602.04837v1, material sha d7c45c77…; canonical seat hashes equal "
                                "conflicts.json; namespaces valid.",
            "core_claim_check": "Re-read §3.1–3.2, §4.1–4.3, §5.1–5.4, A.1–A.2 for each disputed field.",
            "rating_agreement": "Four of eight items agree and were re-checked; X, E.holdout and E.statistics → son55; "
                                "E.cost → sol.",
            "expectation_renumbering": "son55 local-4 → local-1, local-3 → local-2 (merged), local-1 → local-5, "
                                       "local-2 → local-6; generative_process_redesign RE-1/2/3/5 → local-7..10; "
                                       "population_search S5 → local-11.",
            "retained_vs_retained_gain": "The code is retained and reused across iterations, but the retained gain is "
                                         "shown only on selection-contaminated sets → task.",
        },
    }

    for sp in S.values():
        sp.setdefault("paper_update", {})
    return S
