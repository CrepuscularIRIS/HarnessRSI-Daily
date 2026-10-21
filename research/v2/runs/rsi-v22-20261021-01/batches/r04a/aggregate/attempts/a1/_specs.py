"""Opus rulings for r04a a1 (data only; consumed by _build.py). Seat records: sol a1 and son55 a1 for all five papers."""
import copy

VER = "rsi-cards@52ff9657"


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

    def dmatch(s, p, main, **upd):
        for m in seat(s, p)["domain_pattern"]["matches"]:
            if (m.get("main") or m.get("main_id")) == main:
                m2 = prefix(copy.deepcopy(m), s)
                m2["main"] = m2.pop("main_id", None) or m2["main"]
                if "sub_id" in m2:
                    m2["sub"] = m2.pop("sub_id")
                m2["version"] = VER
                m2.update(upd)
                return m2
        raise KeyError((s, p, main))

    def C(p, f):
        return conflict(p, f)

    def X(p, eid):
        return f"expectations[{eid}].status"

    def take(p, eid, who, reason, ev=(), impact="none"):
        sv, nv = C(p, X(p, eid))
        return res(X(p, eid), sv, nv, who, sv if who == "sol" else nv, reason, ev, impact)

    def rev(p, eid, final, reason, ev=(), impact="none"):
        sv, nv = C(p, X(p, eid))
        return res(X(p, eid), sv, nv, "revised", final, reason, ev, impact)

    def rating_res(p, item, who, final, reason, ev, impact):
        sv, nv = C(p, f"ratings.{item}")
        return res(f"ratings.{item}", sv, nv, who, final, reason, ev, impact)

    # =========================================================== 2503.22678 MedAgentSim
    p = "2503.22678"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "In the NEJM benchmark, MedAgentSim achieves 26.7% with LLaMA 3.3, a substantial improvement over "
                    "the baseline Multi-Agent Clinic, where models struggle to exceed 20.0%.", "§3 Results and Analysis",
                    "Text claim about the NEJM baseline ceiling."),
            opus_ev(p, "O02", "ChatGPT [ 20 ] 4o 26.7 25.8 52.8 52.3 34.4", "Table 1, Multi-Agent Clinic GPT-4o row",
                    "The baseline GPT-4o already scores 26.7 on NEJM and 25.8 on NEJM Ext., contradicting 'struggle to exceed "
                    "20.0%' and 'best baseline 24.2%'."),
            opus_ev(p, "O03", "ChatGPT [ 20 ] 4o 26.7 27.5 66.0 67.8 75.3", "Table 1, MedAgentSim GPT-4o row",
                    "Same backbone with MedAgentSim: NEJM 26.7 = baseline 26.7 (no gain), NEJM Ext. +1.7."),
            opus_ev(p, "O04", "This gap widens in NEJM Extended, where MedAgentSim reaches 28.3% with LLaMA 3.3, surpassing the "
                    "best baseline performance of 24.2%.", "§3 Results and Analysis",
                    "Best NEJM Ext. baseline in Table 1 is GPT-4o 25.8, not 24.2."),
            opus_ev(p, "O05", "If the revised diagnosis is correct, only the CLIP-embedded reflection insights are stored in the "
                    "Experience Records Buffer; otherwise, the case is discarded", "§2 Records Storage",
                    "Writes and the reflected retry are gated on correctness against the reference diagnosis — an oracle "
                    "label; nothing states whether these are scored cases."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: retrieved past cases/reflections condition a frozen doctor LLM (C03, medium). No conflict.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial (retrieval conditioning present; isolation and cheaper-alternative controls absent)",
            "resolves_problem": "partial: MedQA memory step +4.7/+5.7 points, single run, separation unknown",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "index_experience_for_reuse", fit="medium"),
                        dmatch("son55", p, "abstract_experience_into_guidance", fit="medium")],
            "unassigned": [],
            "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("sol", "local:2503.22678-1"): "local:2503.22678-3"}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "A persistent two-buffer store exists, but no separation between store-building and scored "
                                   "cases, no frozen-store test and no store-off comparison beyond a cumulative MedQA step; "
                                   "retained benefit is not shown.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Author-reported, single run: on MedQA (n=106) a pipeline adding measurement, case "
                                         "memory, CoT and voting scores above single-pass Multi-Agent Clinic (LLaMA 3.3 "
                                         "54.7→70.8; memory step +5.7). On NEJM the same backbone gains nothing for GPT-4o "
                                         "(26.7 vs 26.7) and the text misreports the baseline ceiling (opus:O01–O04); "
                                         "'progressive learning' is not demonstrated.",
            "unresolved": ["Whether buffers are built from the scored stream and whether the reflected second attempt counts "
                           "toward accuracy (opus:O05).", "LLM judge identity/agreement.", "Call budget of CoT/voting/memory."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Environment gap (pre-compiled reports, no imaging) is sourced; the "
                   "memory gap is generic attempt-reflect-store-retrieve applied to a new vertical (abstract_experience F2) "
                   "and memory-replay neighbours [4,11] are not compared.", ["son55:E009", "son55:E010", "son55:E011", "sol:E07"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Outcome-gated two-buffer store with KNN few-shot is a coherent "
                   "mechanism; reflection is one-sided, CLIP similarity for clinical reasoning is assumed, and the write signal "
                   "is a reference-label oracle.", ["son55:E001", "son55:E002", "opus:O05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Write gate and read path stated; k, injection format, dedup, "
                   "forgetting, versioning and rollback absent.", ["son55:E001", "son55:E002", "sol:E01", "sol:E02"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55. Binary diagnosis judged by an unnamed LLM with no "
                               "agreement figure, datasets converted by GPT-4o (also an evaluated model) and only 'manually "
                               "reviewed'; the reported NEJM comparison contradicts Table 1 (opus:O01–O04), so the "
                               "measurement as reported cannot be taken at face value. 1, not 2.",
                               ["son55:E003", "son55:E004", "opus:O01", "opus:O02", "opus:O04"], ["opus:O03"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Table 2 cumulative steps give a memory increment on two "
                             "backbones (+4.7/+5.7 on n=106), but no random few-shot/longer-context control, buffers not "
                             "separated, compute unmatched vs single-pass baseline.", ["son55:E007", "sol:E06"]),
            "E.holdout": R("not_reported", 0, "Both seats 0; re-checked. No statement that buffers are built on cases disjoint "
                           "from scored ones; writes and the retry use the reference label (opus:O05); no frozen-store, order "
                           "or contamination check.", ["opus:O05", "son55:E012"], [],
                           ["complete pinned v2 text: §1–§4, Tables 1–4, figure captions; no appendix exists"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): case counts and a visible no-gain cell (GPT-4o NEJM), "
                              "no intervals, seeds or order variance; NEJM differences are single cases of 15.",
                              ["son55:E004", "son55:E007", "opus:O03"]),
            "E.cost": R("not_reported", 0, "Both seats 0; re-checked. Only GPU hardware; no calls, tokens, ensemble size or "
                        "reflection cost.", ["sol:E08"], [],
                        ["complete pinned v2 text incl. experimental details and all tables"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML (no appendix exists); in scope as A-class retained case/experience memory; all eight "
                  "items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            take(p, "local:2503.22678-1", "son55",
                 "ID collision (A4): sol's local-1 is the LLM-judge question (renumbered local-3, same as son55 local-3); "
                 "son55's local-1 asks for an accuracy-vs-patients curve or disjoint build/test split — verified absent.",
                 ["son55:E012", "son55:E007"], "none; consistent with E.holdout=0"),
            take(p, "local:2503.22678-2", "son55", "Verified: no call/token count; baseline is single-pass.", ["son55:E007"],
                 "none; consistent with E.cost=0"),
            res(X(p, "local:2503.22678-3"), *C(p, X(p, "local:2503.22678-3")), "same_supported_fact", "partial",
                "sol's renumbered local-1 and son55's local-3 are the same judge-reliability question, both partial.",
                ["son55:E003", "sol:E03"], "none"),
            take(p, "rs:adapt_via_conditioning/RE-1", "sol",
                 "Card RE-1 (isolate the conditioning signal): Table 2 adds memory as a separate cumulative step — partial; "
                 "two buffers not separated.", ["sol:E06"], "none"),
            take(p, "rs:adapt_via_conditioning/RE-3", "son55",
                 "Card RE-3 (cheaper alternative: longer context / nearest-neighbour / random few-shot): none run.",
                 ["son55:E007"], "none"),
            take(p, "rsi:abstract_experience_into_guidance/F2", "son55",
                 "Failure mode present: generic attempt→reflect→store→retrieve applied to clinical consultation; the "
                 "environment, not the memory, is the specific contribution. Card cites the pattern only as a check (A5).",
                 ["son55:E011", "son55:E009"], "none; supports G=2"),
            take(p, "rsi:abstract_experience_into_guidance/H00-step4", "son55",
                 "No frozen-store or online-update on/off test; status unknown is the honest state (not reported).",
                 ["son55:E012"], "none"),
            take(p, "rsi:abstract_experience_into_guidance/S2", "son55",
                 "Verified: only corrected failures are reflected; no success-vs-failure contrast.", ["son55:E001"], "none"),
            take(p, "rsi:abstract_experience_into_guidance/S3", "son55",
                 "Grounding signal = correctness vs reference diagnosis: real but an oracle unavailable in deployment.",
                 ["son55:E001", "opus:O05"], "none"),
            take(p, "rsi:abstract_experience_into_guidance/S5", "son55",
                 "Correctness gate on the retry exists; no marginal-utility test or rollback.", ["son55:E001"], "none"),
            take(p, "rsi:index_experience_for_reuse/F3", "son55",
                 "Text never states whether buffers come from the scored stream — unknown; charged as not_reported under "
                 "E.holdout.", ["son55:E012", "opus:O05"], "none"),
            take(p, "rsi:index_experience_for_reuse/S2", "sol",
                 "Writes gated by correctness (external label) — partial because the judge is uncalibrated.",
                 ["sol:E02", "sol:E03"], "none"),
            rating_res(p, "E.measurement", "son55", {"status": "resolved", "rating": 1},
                       "sol's 2 credited the manual log review; but the judge is unnamed with no agreement, GPT-4o converts "
                       "the data, and the paper's own NEJM text contradicts Table 1 (opus:O01–O04). son55's 1 stands.",
                       ["son55:E003", "opus:O01", "opus:O02", "opus:O04"], "-2.5 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims (NEJM) / assessment.strongest_supported_claim",
             "seat_values": {"sol": "NEJM text-table conflict not noted", "son55": "noted text misreads Table 1; GPT-4o 26.7=26.7"},
             "final_value": "NEJM: MedAgentSim gives no gain for GPT-4o (26.7 vs 26.7); best NEJM Ext. baseline is GPT-4o 25.8, "
                            "not 24.2; 'significantly outperforms across all benchmarks' does not hold for this cell.",
             "reason": "One-seat omission (sol) corrected in the final claim; recorded so the final claim text is traceable.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04"], "score_impact": "none beyond E.measurement=1"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first. Provisional: in scope (A, case memory); G2 M2 X2 "
                                                   "Em1–2 Ec2 Eh0 Es1 Ecost0; found GPT-4o NEJM tie and baseline-ceiling "
                                                   "misstatement; write gate uses reference labels.",
            "integrity_checks": "Both seats on 2503.22678v2, sha fd45477f…; hashes equal conflicts.json; both full 15+31 "
                                "identification (C03) and rsi namespace correct.",
            "core_claim_check": "Recomputed: Table 2 LLaMA 70.8−54.7=16.1 ✓ (points, called '%'); Table 2 totals match Table 1 "
                                "MedQA (53.8, 70.8) ✓; NEJM text vs Table 1 ✗ (opus:O01–O04).",
            "retention_check": "Failure denominator: n=15/106/214/120/288, single run; selection vs test: unknown, label-gated "
                               "writes; extra budget: CoT + multi-doctor voting + reflection retry vs single-pass baseline; "
                               "'stored' is not shown to be 'retained improvement'.",
        },
    }

    # =========================================================== 2504.00185 Escher
    p = "2504.00185"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "ViT-L-14 LM4CV Ours Ours-H CIFAR-100 84.48 89.63 86.73 CUB-200-2011 63.26 83.17 81.58 Food101 "
                    "94.77 94.97 94.97 NABirds 76.58 78.21 77.35 Oxford Flowers 94.80 96.86 96.86 Stanford Cars 86.84 93.76 88.09",
                    "Appendix 7.1, Table 6", "No-history variant (critic kept)."),
            opus_ev(p, "O02", "ViT-L-14 LM4CV Ours Ours-H-VC CIFAR-100 84.48 89.63 86.76 CUB-200-2011 63.26 83.17 82.41 Food101 "
                    "94.77 94.97 94.95 NABirds 76.58 78.21 77.29 Oxford Flowers 94.80 96.86 96.08 Stanford Cars 86.84 93.76 88.12",
                    "Appendix 7.2, Table 7", "No-history AND random-critic variant. Ours-H minus Ours-H-VC = −0.03, −0.83, "
                    "+0.02, +0.06, +0.78, −0.03: the critic's isolated effect is ≈0 (negative on CUB), while Ours-H-VC still "
                    "reaches 82.41 on CUB vs 66.09 for count-matched concepts."),
            opus_ev(p, "O03", "suggesting that feedback from a VLM critic is essential", "Table 4 caption",
                    "Authors' attribution to the critic, not supported by Tables 6–7."),
            opus_ev(p, "O04", "Additionally, in every case, refining CBMs iteratively using Escher leads to better performance "
                    "than relying on a fixed set of concepts.", "§5.5 Observations",
                    "Contradicted by ties in Table 5 (CbD CUB 56.16=56.16, NABirds 45.25=45.25) and Table 10 (NABirds 41.48=41.48)."),
            opus_ev(p, "O05", "CUB-200-2011 57.06 70.90 77.17 56.16 56.16", "Table 5 (ViT-B/16), CUB row",
                    "CbD and CbD+Escher identical."),
            opus_ev(p, "O06", "The specific heuristic and hyperparameters vary depending on the task and underlying algorithm, "
                    "and grid-searching for such hyperparameters proves to be practical and effective.", "§5 Methodology",
                    "Selection split for heuristic/hyperparameters not named; Table 9 reports heuristic choice on test accuracy."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "The load-bearing move the paper claims is a label-free signal manufactured from the VLM's own scores "
                      "(pseudo-confusion) that steers concept generation: self_supervised_signal_engineering/C07 (internal "
                      "readout, small lever, frozen backbones). C07 step 5 (show the signal causally tracks the target) fails: "
                      "Tables 6–7 put the critic's isolated effect at ≈0 (opus:O02). generative_process_redesign is not kept: "
                      "its definition targets fixed internals of an iterative generative procedure (prior, endpoints, latent, "
                      "conditioning granularity), while the concept library is the classifier's input vocabulary.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering")],
            "executes_pattern": "partial (signal manufactured and used; causal role of the signal not shown)",
            "resolves_problem": "partial: library growth helps LM4CV on held-out test; critic not shown necessary",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "attribute_and_patch_incumbent")],
            "unassigned": ["Perception-side concept library read by a VLM scorer; H10 fits loosely (append-only, no selection rule)."],
            "revision_proposals": ["sol: class-pair proxy feedback growing a non-program concept library as a medium-fit "
                                   "attribute_and_patch variant (proposal only).",
                                   "son55: boundary note for perception-side concept libraries edited from critic feedback "
                                   "(proposal only)."],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("sol", "local:2504.00185-2"): "local:2504.00185-4"},
            overrides={"local:2504.00185-1": {"status": "partial", "opus_note": "Evolution signal on validation logits (met); "
                       "heuristic/hyperparameter selection split unstated and Table 9 picks the heuristic on test accuracy "
                       "(opus:O06)."},
                       "rs:self_supervised_signal_engineering/RE-2": {"status": "unmet", "opus_note": "The critic's isolated "
                       "effect is ≈0 (opus:O01, opus:O02); the gain is not attributable to the manufactured signal."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "The concept library is evolved on validation logits and used on the test split; a "
                                   "count-matched LLM-concept control loses most of the gain (CUB 66.09 vs 83.17). Narrow: "
                                   "same classes, single run; heuristic chosen with test-set results.",
            "claim_support": "scoped",
            "strongest_supported_claim": "For fine-tuned LM4CV, growing the concept library by LLM pairwise-disambiguation "
                                         "queries raises test top-1 over the initial library and a count-matched concept "
                                         "control (largest on CUB, Cars, CIFAR-100). The VLM critic is not shown necessary "
                                         "(random pairs + no history ≈ critic + no history, opus:O02); zero-shot gains are "
                                         "small, few-shot mixed, and 'improves in every case' is contradicted by ties "
                                         "(opus:O04, opus:O05).",
            "unresolved": ["History-on random-critic control.", "Split used for heuristic/hyperparameter search (opus:O06).",
                           "Run-to-run variance (Food101 94.90 vs 94.97 for the same configuration)."]},
        "ratings": {
            "G": R("resolved", 3, "Opus sides with sol. The fixed one-shot concept set and per-class mutation's poor scaling "
                   "are concrete, with lineage over non-parametric/parametric CBMs and library learning. Not 4: the "
                   "closest neighbour [5] is dismissed qualitatively. Not running it is charged once, under E.causality.",
                   ["son55:E014", "son55:E015", "sol:E01"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Confusion-targeted pair disambiguation with history yields "
                   "distinguishable predictions (random pairs, count control, history off). That the critic turns out "
                   "≈0 is a result, scored under E.causality.", ["son55:E002", "son55:E003", "son55:E009", "son55:E016"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm, hyperparameters and prompts are given; retention is an "
                   "unconditional union with no gate, rollback or pruning; Algorithm 1 line 17 (C_{t+1}←C_t) conflicts "
                   "with lines 13–14.", ["son55:E001", "son55:E005", "son55:E018", "sol:E02"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Standard test top-1 on public datasets; minor "
                               "inconsistency (Food101 94.90 vs 94.97) and an unlisted seventh dataset (Pets).",
                               ["son55:E004", "son55:E006", "sol:E05"]),
            "E.causality": R("resolved", 2, "Opus sides with son55. Count-matched concepts and history ablations are real "
                             "controls, but recomputing Tables 6–7 the critic's isolated contribution is ≈0 and negative on "
                             "CUB (opus:O01, opus:O02), contradicting the authors' 'critic is essential' (opus:O03); no "
                             "history-on random-critic run, no call/step-matched baseline, [5] not run.",
                             ["son55:E009", "son55:E011", "opus:O01", "opus:O02"], ["opus:O03", "son55:E012"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. Evolution reads validation logits and reporting uses the "
                           "test split, but heuristic/hyperparameters are grid-searched on an unstated split and the "
                           "heuristic is chosen from test-set Table 9 (opus:O06); no new-class transfer.",
                           ["son55:E005", "son55:E004", "opus:O06"], ["son55:E019"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): mixed few-shot and tie cells are visible, but every "
                              "cell is one run with no intervals.", ["son55:E007", "son55:E013", "opus:O05"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. Queries/iteration, token estimate (12.8M) and per-iteration "
                        "time given; no cost-matched baseline or grid-search total.", ["son55:E018", "sol:E09"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. supplementary §7.1–7.11; in scope (retained non-weight concept library, only a "
                  "linear adapter refit); all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "The paper's stated engine is a label-free signal from the VLM's own outputs; generative_process_redesign's "
                "scope (internals of an iterative generative procedure) does not cover a classifier's concept vocabulary.",
                ["son55:E002", "son55:E016", "opus:O02"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["self_supervised_signal_engineering", "C07"]],
                "C07 (internal readout + small lever) is the closest sub; step 5 fails (critic ≈0).", ["son55:E011", "opus:O02"],
                "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55", [["attribute_and_patch_incumbent", "H10"]],
                "H10 (rewrite a textual artifact from diagnosed errors) is the nearest sub at low fit; sol's null is also "
                "defensible but a low-fit sub is more informative and both seats agree on the main card.",
                ["son55:E001", "son55:E002"], "none"),
            rev(p, "local:2504.00185-1", "partial",
                "Same question in both seats (selection vs test). Evolution uses validation logits (sol's 'met' part) but the "
                "grid-search split is unstated and Table 9 picks the heuristic from test accuracy (opus:O06) — partial on "
                "evidence, not as a compromise.", ["son55:E005", "sol:E04", "opus:O06"], "none; consistent with E.holdout=2"),
            take(p, "local:2504.00185-2", "son55",
                 "ID collision: sol's local-2 (cost, partial) renumbered local-4. son55's local-2 (no call/step-matched "
                 "baseline) verified.", ["son55:E010", "son55:E017"], "none"),
            take(p, "local:2504.00185-3", "son55", "Verified: single run per cell; Food101 94.90 vs 94.97.",
                 ["son55:E006", "son55:E013"], "none"),
            take(p, "rs:generative_process_redesign/RE-1", "sol",
                 "Kept as a check question though the card is not matched: removing library learning (count-matched "
                 "concepts) collapses the gain — met.", ["sol:E06"], "none"),
            take(p, "rs:generative_process_redesign/RE-3", "sol",
                 "Per-component ablations exist for history and critic+history; the critic is not justified alone — partial.",
                 ["sol:E07", "sol:E12", "opus:O02"], "none"),
            take(p, "rs:self_supervised_signal_engineering/RE-1", "son55",
                 "Three CBM families, seven datasets, two backbone swaps.", ["son55:E009"], "none"),
            rev(p, "rs:self_supervised_signal_engineering/RE-2", "unmet",
                "RE-2 asks that the gain be attributable to the manufactured signal itself. son55's own reading (critic ≈0) "
                "answers it: Ours-H vs Ours-H-VC differ by ≤0.83 with mixed sign (opus:O01, opus:O02). Unmet, not partial.",
                ["opus:O01", "opus:O02", "son55:E011"], "none; supports E.causality=2"),
            take(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "Downstream top-1 reported.", ["son55:E004"], "none"),
            take(p, "rs:self_supervised_signal_engineering/RE-4", "son55", "Delta to [5] argued, not run.", ["son55:E014"],
                 "none"),
            take(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "Own cost disclosed; no cost-benefit vs baselines.",
                 ["son55:E018"], "none"),
            take(p, "rs:self_supervised_signal_engineering/RE-6", "son55",
                 "Calibration assumed (E016) and blamed for weak zero/few-shot results.", ["son55:E016", "son55:E008"], "none"),
            take(p, "rsi:abstract_experience_into_guidance/S4", "son55",
                 "Used as a generic store-maintenance check: no pruning/merging; adapter down-weights useless concepts.",
                 ["son55:E018"], "none"),
            take(p, "rsi:attribute_and_patch_incumbent/F5", "son55",
                 "Confusion may come from the CLIP backbone; γ decay mitigates but nothing verifies the cause.",
                 ["son55:E003"], "none"),
            take(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "Edit scope = the confused pair's concept sets.",
                 ["son55:E002"], "none"),
            rating_res(p, "G", "sol", {"status": "resolved", "rating": 3},
                       "The gap names what was fixed (one-shot concept set; per-class mutation) with lineage; son55's "
                       "deduction (neighbour [5] not run) is an evidence-side defect already charged under E.causality "
                       "(A2: one defect, one item).", ["son55:E014", "sol:E01"], "+3.75 vs son55 value"),
            rating_res(p, "E.causality", "son55", {"status": "resolved", "rating": 2},
                       "sol's 3 noted that the critic ablation also removes history but still credited the critic. "
                       "Recomputed Tables 6–7: critic isolated effect ≈0, negative on CUB; the authors' attribution is "
                       "contradicted by their own tables.", ["opus:O01", "opus:O02", "opus:O03"], "-3.75 vs sol value"),
            rating_res(p, "E.holdout", "son55", {"status": "resolved", "rating": 2},
                       "Selection on test for the heuristic (Table 9) and an unstated grid-search split are selection-vs-test "
                       "issues (EVIDENCE rule 2); sol's 3 did not weigh them.", ["opus:O06", "son55:E019"], "-2.5 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims (backbone generality) / assessment.strongest_supported_claim",
             "seat_values": {"sol": "not noted", "son55": "noted CbD cells without gain in RE-6 only"},
             "final_value": "'In every case Escher leads to better performance' is false: Table 5 CbD CUB 56.16=56.16, NABirds "
                            "45.25=45.25; Table 10 NABirds 41.48=41.48.",
             "reason": "Neither seat carried the tie cells into the claim check.",
             "evidence_ids": ["opus:O04", "opus:O05"], "score_impact": "none (E.statistics 1, claim scoped)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text and supplement first. Provisional: in scope (retained "
                                                   "non-weight library); G2–3 M3 X2 Em3 Ec1–2 Eh2 Es1 Ecost2; found critic "
                                                   "≈0 (Tables 6 vs 7), ties contradicting 'every case', heuristic picked on test.",
            "integrity_checks": "Both seats on 2504.00185v1, sha per manifest; hashes equal conflicts.json; full 15+31 "
                                "identification in both seats (different cards; resolved above).",
            "core_claim_check": "Recomputed critic effect (Table 6 − Table 7 per dataset): −0.03, −0.83, +0.02, +0.06, +0.78, "
                                "−0.03. Count control CUB 66.09 vs 83.17 ✓.",
            "retention_check": "Selection vs test: validation logits for evolution, test for reporting, heuristic picked on "
                               "test. Extra budget: ~100 LLM queries/iteration × 60 iterations vs one-shot baseline; count "
                               "control matches concept count, not calls/steps. Retention is unconditional union.",
        },
    }

    # =========================================================== 2504.00587 AgentNet
    p = "2504.00587"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "AFLOW 91.67 88.00 28.00", "Table 1, DeepSeek-V3 AFLOW row",
                    "MATH test has 140 items: 91.67% = 128.3 items, not an attainable count."),
            opus_ev(p, "O02", "Self-Consistency 88.00 85.00 29.00", "Table 1, DeepSeek-V3 Self-Consistency row",
                    "88.00% of 140 = 123.2 items, not attainable; all other MATH cells are multiples of 1/140."),
            opus_ev(p, "O03", "while the test set consists of 20 examples per type (total of 140 problems)", "§4.1 MATH",
                    "Stated MATH test denominator."),
            opus_ev(p, "O04", "w/o evolution 77.86 23.00 76.00 AgentNet 85.00 32.00 86.00", "Table 3 (gpt-4o-mini)",
                    "Evolution ablation; API-Bank AgentNet 32.00."),
            opus_ev(p, "O05", "AgentNet 85.00 86.00 29.00", "Table 1, gpt-4o-mini AgentNet row",
                    "Same configuration reports API-Bank 29.00, not 32.00 (32.00 is the Qwen-turbo value)."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: per-agent retrieved trajectory fragments condition frozen LLM routers/executors (C03). No "
                      "conflict; fit low–medium because routing/topology are not conditioning.",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial: bundled evolution on/off only",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "search_agent_architecture"), dmatch("son55", p, "index_experience_for_reuse")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("sol", "local:2504.00587-2"): "local:2504.00587-4"},
            overrides={"rs:adapt_via_conditioning/RE-2": {"status": "unmet", "opus_note": "No overlap/contamination analysis at "
                       "all; sample sizes are not what RE-2 asks."}}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Training-phase evolution of memories/capabilities/edges, then a disjoint test split; "
                                   "MATH 77.86→85.00 and BBH 76→86 match Table 1. Narrow: 'w/o evolution' undefined, test-time "
                                   "freezing unstated, API-Bank figure conflicts between tables (opus:O04, opus:O05).",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single run, gpt-4o-mini, 3 agents: a bundled training-phase evolution is associated "
                                         "with higher accuracy on small in-distribution test splits of MATH (140) and BBH "
                                         "(100); the API-Bank gain is either 6 or 9 points depending on which table is "
                                         "right. AgentNet is competitive with, not consistently above, strong baselines. "
                                         "Decentralisation benefits (fault tolerance, privacy, efficiency) are untested.",
            "unresolved": ["Definition of 'w/o evolution' and of success metric S.", "Memory freezing at test.",
                           "Denominators behind 91.67/88.00 on a 140-item test (opus:O01–O03)."]},
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Static roles/central control are real limits, but the headline "
                   "stakes are unmeasured and the compared methods are not shown to be central-controller bottlenecked.",
                   ["son55:E016", "son55:E017", "son55:E021", "sol:E12"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Coherent memory+EMA edges+capability vectors+routing, but S, Δc, "
                   "Φ and the pruning prompt are verbal; no prediction separates decentralisation from memory+routing.",
                   ["son55:E001", "son55:E003", "son55:E004"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Algorithm 1 and update rules exist; success definition, values, "
                   "test-time freezing and rollback absent.", ["son55:E001", "son55:E002", "son55:E003", "son55:E004"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55, with added grounds. Scorer undescribed; two MATH cells "
                               "are unattainable on the stated 140-item test (opus:O01–O03), so denominators differ across "
                               "methods; the evolution ablation's API-Bank number contradicts Table 1 for the same "
                               "configuration (opus:O04, opus:O05).",
                               ["son55:E005", "son55:E006", "opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Evolution on/off and router ablations exist; evolution "
                             "is one undefined block (memory, capabilities, edges), no per-component or matched-budget "
                             "control, global-router comparison is figure-only.",
                             ["son55:E007", "son55:E015", "sol:E07"], ["opus:O05"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. Disjoint train/test per benchmark, small and "
                           "in-distribution; test-time freezing and hyperparameter split unstated; no contamination check.",
                           ["son55:E005", "son55:E006", "sol:E05", "sol:E06"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): sizes, ties and the 3-agent heterogeneity loss are "
                              "visible; single deterministic run, no intervals.", ["son55:E009", "son55:E010", "son55:E012"]),
            "E.cost": R("not_reported", 0, "Both seats 0; re-checked. Efficiency is claimed but no tokens, calls, latency, "
                        "communication or evolution cost; baselines matched on agent count only.", ["son55:E019"], [],
                        ["complete pinned v2 text: §1–§7, Algorithm 1, Tables 1–3, figure captions; no appendix exists"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 HTML (no appendix); in scope (A: per-agent memories, capability vectors and edge weights "
                  "are non-weight state updated from task success); all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            take(p, "local:2504.00587-3", "son55", "Verified: single deterministic run; 1-problem margins read as wins.",
                 ["son55:E009", "son55:E010"], "none"),
            res(X(p, "rs:adapt_via_conditioning/RE-2"), *C(p, X(p, "rs:adapt_via_conditioning/RE-2")), "son55", "unmet",
                "Card RE-2 requires a contamination/overlap analysis before held-out claims; none exists. sol's 'partial' "
                "rested on sample sizes, which RE-2 does not ask for.", ["son55:E005", "son55:E006"], "none"),
            take(p, "rs:adapt_via_conditioning/RE-3", "son55", "No longer-context / nearest-neighbour memory baseline at matched "
                 "budget.", ["son55:E020"], "none"),
            take(p, "rs:adapt_via_conditioning/RE-4", "son55", "Components never ablated individually.", ["son55:E007"], "none"),
            take(p, "rs:adapt_via_conditioning/RE-5", "son55", "Three task families, three backbones, one configuration.",
                 ["son55:E009"], "none"),
            take(p, "rsi:index_experience_for_reuse/F3", "son55", "Freezing during test never stated; unknown is honest.",
                 ["son55:E005"], "none"),
            take(p, "rsi:index_experience_for_reuse/S5", "son55", "Evolution on/off exists but does not isolate the store.",
                 ["son55:E007"], "none"),
            take(p, "rsi:search_agent_architecture/F1", "son55", "Failure present: all axes adapt together, bundled ablation.",
                 ["son55:E007"], "none"),
            take(p, "rsi:search_agent_architecture/F3", "son55", "Capability deltas from LLM assessment, not an independent "
                 "verifier.", ["son55:E004"], "none"),
            take(p, "rsi:search_agent_architecture/H18-step5", "son55", "No evolution/communication cost.", ["son55:E019"],
                 "none; consistent with E.cost=0"),
            take(p, "rsi:search_agent_architecture/S4", "son55", "No retreat path to a simpler network.", ["son55:E003"], "none"),
            rating_res(p, "E.measurement", "son55", {"status": "resolved", "rating": 1},
                       "sol's 2 noted the API table conflict; Opus additionally finds two MATH cells unattainable on the "
                       "stated 140-item test (opus:O01–O03), i.e. per-method denominators are not the stated test set. "
                       "With an undescribed scorer this is 1.", ["opus:O01", "opus:O02", "opus:O03", "opus:O05"],
                       "-2.5 vs sol value"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims (Table 1 denominators) / ratings.E.measurement.reason",
             "seat_values": {"sol": "not noted", "son55": "noted implausible spreads, not unattainable values"},
             "final_value": "AFLOW 91.67 and Self-Consistency 88.00 (DeepSeek-V3, MATH) cannot arise from 140 items; every "
                            "other MATH cell is a multiple of 1/140. Failure/denominator handling differs across methods.",
             "reason": "Neither seat checked cell attainability against the stated denominator (task step 6).",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none beyond E.measurement=1"},
            {"field_path": "claims (evolution ablation API-Bank)",
             "seat_values": {"sol": "noted Table 1 API 29 vs Table 3 API 32", "son55": "reported +9 without the conflict"},
             "final_value": "API-Bank evolution gain is 23→32 (Table 3) or 23→29 (Table 1 value for the same configuration).",
             "reason": "son55 omission; final claim keeps both values.", "evidence_ids": ["opus:O04", "opus:O05"],
             "score_impact": "none"},
            {"field_path": "expectations[local:2504.00587-2]",
             "seat_values": {"sol": "local-2 = cost question (unmet)", "son55": "local-2 = baseline spread question (unmet)"},
             "final_value": "Hidden A4 ID collision: sol's local-2 renumbered local-4; son55's local-2 kept.",
             "reason": "Same ID and status, different questions; no mechanical conflict was raised.",
             "evidence_ids": ["son55:E009"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text first. Provisional: in scope (A); G2 M2 X2 Em1–2 Ec1–2 Eh2 "
                                                   "Es1 Ecost0; found unattainable MATH cells, Table 1/3 API conflict, "
                                                   "undefined 'w/o evolution'.",
            "integrity_checks": "Both seats on 2504.00587v2; hashes equal conflicts.json; full 15+31 identification (C03) in "
                                "both; domain sets identical (H18, H03).",
            "core_claim_check": "MATH cells × 140 checked: all integers except 91.67 and 88.00. Table 3 MATH/BBH match "
                                "Table 1; API-Bank does not.",
            "retention_check": "Selection vs test: train evolution, test split, freezing unknown. Extra budget: training "
                               "phase (700/627/100 items) not given to Direct/ReAct/SC/SR baselines. Retained store shown "
                               "only as a bundled on/off.",
        },
    }

    # =========================================================== 2504.06821 ASI
    p = "2504.06821"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "unverified, text 32.6 verified, program 36.4 verified, text 39.0 Add as Actions verified, program 40.1",
                    "Table 3 (shopping)", "Ablation values: 36.4−32.6 = 3.8, not the 4.2 stated."),
            opus_ev(p, "O02", "Claude Vanilla 5.6 32.7 32.6 36.8 36.8 26.1 38.5 20.8 AWM 5.9 36.3 34.8 39.0 51.9 28.9 39.4 18.8",
                    "Table 1, Claude rows", "Shopping: Vanilla 32.6, AWM 34.8. Table 3's '(unverified, text)' = AWM-style "
                    "row equals the Vanilla value; against AWM 34.8, verified-program-in-memory adds 1.6 and verified text 4.2."),
            opus_ev(p, "O03", "improves end success rate by 4.2 points", "§3.3", "Text claim for the verification effect."),
            opus_ev(p, "O04", "reducing the number of steps in solutions by 15.3% and 10.6% than vanilla and AWM agents",
                    "§3.2", "Swapped: 5.0 vs Vanilla 5.6 is 10.7%; vs AWM 5.9 is 15.3%."),
            opus_ev(p, "O05", "shopping 21 8 96 180 admin 38 15 108 156 reddit 24 11 14 105 map 13 10 80 109 gitlab 25 11 10 175",
                    "Appendix B.1, Table 8", "Totals sum to 725, not 812; the 42.5% reuse and 7.6% induction rates use 725."),
            opus_ev(p, "O06", "that contains 812 test examples", "§3.1", "Main evaluation set size."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Skills are emitted as executable programs (a machine-checkable intermediate artifact) and verified by "
                      "re-execution before admission — decompose_and_delegate/C25. architectural_operator_substitution needs "
                      "a cheaper surrogate with a proved preserved property; ASI offers no proof and its gain is not a cost "
                      "substitution, so it is not kept (sol's own fit note says the guarantee condition fails).",
            "matches": [smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": "partial (artifact + execution loop; verification bounded by an LM judge)",
            "resolves_problem": "partial: +4.1 SR over re-run AWM, single run",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "crystallize_executable_capability",
                               reason="H06 admission tactic (succeeded, invoked, changed environment) matches exactly; the "
                                      "practice source is the online test stream, not self-directed practice, hence medium.")],
            "unassigned": [],
            "revision_proposals": ["sol: online post-episode crystallisation is neither H06 practice nor H07 forging; consider a "
                                   "boundary note (proposal only).",
                                   "Opus: evidence_gated_retention/H30 not assigned — ASI has admission only, no retirement; "
                                   "S2 is kept as a check question."],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("sol", "local:2504.06821-1"): "local:2504.06821-4",
                                 ("sol", "local:2504.06821-2"): "local:2504.06821-5"}, overrides={}),
        "claims": lambda c: [
            {**x, "allowed_conclusion": "On shopping, verification-related settings add most of the gain over unverified "
                                        "skills, but the '(unverified, text)' row (32.6) equals Vanilla, not AWM (34.8, Table 1); "
                                        "against 34.8, verified programs in memory add 1.6, verified text 4.2, programs as "
                                        "actions 5.3. The stated +4.2 is 3.8 by the table. One site, one run.",
             "opus_correction": "opus:O01, opus:O02, opus:O03"} if x.get("claim_id") == "CL2" else x for x in c],
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Skills induced online (no ground-truth reward) persist in the action space and are reused "
                                   "on later tasks (reuse 42.5% of the 725 tasks in Table 8); a fixed library also transfers "
                                   "to three real sites (10 queries each). Induction stream = scored stream.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Claude-3.5, single online pass on WebArena: ASI 40.4 vs re-run AWM 36.3 vs static "
                                         "32.7 SR (relative +11.3%/+23.5%) with fewer macro-steps. Attribution to "
                                         "verification rests on a shopping-only ablation whose anchor row does not match "
                                         "Table 1 (opus:O01, opus:O02); cross-site SR vs AWM is not significant (p=0.167); "
                                         "the 'verification guarantee' is an LM judgment plus invocation/state-change checks.",
            "unresolved": ["Run-to-run/order variance on the 812-task stream.", "LM-evaluator precision.",
                           "Induction + verification-replay cost.", "87 tasks absent from Table 8 (opus:O05)."]},
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The fixed object (unverified text skills in memory) is named, AWM "
                   "re-run on the same backbone with cleaning; other program-library neighbours not compared.",
                   ["son55:E017", "son55:E018", "son55:E019", "sol:E07"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Cleaning, rewritten prefix, truncation against spurious success "
                   "and three admission checks each have a rationale and testable predictions; correctness rests on the "
                   "same LM judge.", ["son55:E003", "son55:E004", "son55:E005", "sol:E03"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. Prompts, action space, gate and reuse path reconstructable; no "
                   "repair loop, retirement, versioning or library bound.", ["son55:E001", "son55:E003", "son55:E011", "sol:E04"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked and kept. The central SR metric is the official "
                               "WebArena programmatic checker (opus:O06). Deductions: macro-step 'efficiency' is partly by "
                               "construction, scaled-up/real-site scoring unspecified, and several text-table slips "
                               "(opus:O03, opus:O04). Not lowered: the slips concern secondary ablation/prose, not the "
                               "headline SR cells.", ["son55:E006", "opus:O06"], ["opus:O03", "opus:O04", "son55:E002"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-backbone AWM re-run and a verification×format "
                             "ablation, but one site, one run, an anchor row that equals Vanilla rather than AWM "
                             "(opus:O01, opus:O02), no library-removed control, verification rollouts unbudgeted.",
                             ["son55:E009", "son55:E010", "son55:E017", "opus:O01", "opus:O02"], ["son55:E005"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked. No ground-truth reward is used, but induction runs on "
                           "the scored stream; independent test is 10 real-site queries per domain.",
                           ["son55:E013", "son55:E015", "sol:E11", "sol:E16"]),
            "E.statistics": R("resolved", 1, "Shared correction (both seats 2). Frozen A2 ladder: 1 = sample sizes and "
                              "negative results but the main result carries no uncertainty. The central 812-task comparison "
                              "is one online pass with no interval, seed or order variation; t-tests exist only for the "
                              "small scaled-up and cross-site sets (incl. non-significant ASI vs AWM).",
                              ["son55:E007", "son55:E014", "sol:E13", "sol:E14"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Macro-steps and induction counts only; no LM calls, tokens, "
                        "verification replays or wall-clock.", ["son55:E012", "sol:E12"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–C; in scope (A: executable skill library edited from own "
                  "execution feedback, retained and reused); all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "Executable skill programs verified by re-execution are C25's machine-checkable artifact; the operator-"
                "substitution card requires a proved preserved property that ASI does not offer.",
                ["son55:E001", "son55:E003", "sol:E03"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["decompose_and_delegate", "C25"]],
                "One primary, sub C25 (artifact + verify loop).", ["son55:E003", "son55:E004"], "none"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised", [["crystallize_executable_capability", "H06"]],
                "H06's admission gate (succeeded, invoked, changed state) is exactly ASI's, so a sub is warranted over sol's "
                "null; H30 is dropped because ASI has no retirement, size bound or marginal replay (its S2 stays as a check).",
                ["son55:E003", "sol:E04"], "none"),
            take(p, "local:2504.06821-2", "son55",
                 "ID collision: sol's local-2 (cost) renumbered local-5. son55's local-2 (skill call = one step, partly by "
                 "construction) verified.", ["son55:E001", "son55:E012"], "none"),
            take(p, "local:2504.06821-3", "son55", "Verified: single pass, no significance test on Table 1.", ["son55:E007"],
                 "none; supports E.statistics=1"),
            take(p, "rs:architectural_operator_substitution/RE-1", "sol",
                 "Kept as a check: no proof that program skills preserve semantics; replay ≠ guarantee — partial.",
                 ["sol:E03", "sol:E05"], "none"),
            take(p, "rs:architectural_operator_substitution/RE-2", "sol",
                 "Verification and format ablated on one site; unverified-programs-as-actions missing — partial.",
                 ["sol:E09"], "none"),
            take(p, "rs:decompose_and_delegate/RE-1", "son55", "No token/call cost for induction and verification.",
                 ["son55:E012"], "none"),
            take(p, "rs:decompose_and_delegate/RE-2", "son55", "2×2-style ablation, one site, checks not separated.",
                 ["son55:E009", "son55:E010"], "none"),
            take(p, "rs:decompose_and_delegate/RE-3", "son55", "Prompts and action space listed (App. A).", ["son55:E003"], "none"),
            take(p, "rs:decompose_and_delegate/RE-4", "son55", "WebArena + curated long-horizon + 10-query real sites; one "
                 "backbone.", ["son55:E015", "son55:E016"], "none"),
            take(p, "rs:decompose_and_delegate/RE-5", "son55", "Static and re-run AWM included; other program libraries not.",
                 ["son55:E017"], "none"),
            take(p, "rs:decompose_and_delegate/RE-6", "son55", "Qualitative skill defects; no sub-task→success diagnostic.",
                 ["son55:E019"], "none"),
            take(p, "rsi:crystallize_executable_capability/F4", "son55", "Site-specific constants; reported openly.",
                 ["son55:E015"], "none"),
            take(p, "rsi:crystallize_executable_capability/H06-step1", "son55", "Practice source = scored stream.",
                 ["son55:E013"], "none"),
            take(p, "rsi:crystallize_executable_capability/S1", "son55", "Execution+usage+state checks, correctness by LM.",
                 ["son55:E002", "son55:E003"], "none"),
            take(p, "rsi:crystallize_executable_capability/S3", "sol", "Validated on the source query; fixed-library transfer "
                 "on 10 queries/site — partial.", ["sol:E11", "sol:E16"], "none"),
            take(p, "rsi:crystallize_executable_capability/S4", "son55", "Failed candidates dropped; no repair loop.",
                 ["son55:E003"], "none"),
            take(p, "rsi:crystallize_executable_capability/S5", "son55", "No library-removed run holding the loop fixed.",
                 ["son55:E007"], "none"),
            take(p, "rsi:evidence_gated_retention/S2", "son55", "Check question only (card not assigned): admission without "
                 "retirement or size bound.", ["son55:E003"], "none"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.statistics",
             "seat_values": {"sol": {"status": "resolved", "rating": 2}, "son55": {"status": "resolved", "rating": 2}},
             "final_value": {"status": "resolved", "rating": 1},
             "reason": "Both seats credited t-tests on the small secondary sets toward the main result. Under the frozen A2 "
                       "ladder the central 812-task comparison has no uncertainty at all, which is level 1.",
             "evidence_ids": ["son55:E007", "son55:E014"], "score_impact": "-1.25 (65.0 → 63.75)"},
            {"field_path": "claims[CL2] (Table 3 attribution)",
             "seat_values": {"sol": "noted 4.2 vs 3.8 and 32.6 vs AWM 34.8", "son55": "noted 4.2 vs 3.8 only; built CL2 on 32.6"},
             "final_value": "Table 3 anchor row equals Vanilla shopping (32.6), not AWM (34.8); the verification effect on "
                            "shopping is 1.6 (program in memory) to 4.2 (text) points vs AWM.",
             "reason": "Base-seat claim rested on the mismatched anchor; corrected in claims.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"], "score_impact": "none beyond E.causality=2"},
            {"field_path": "claims (efficiency and reuse denominators)",
             "seat_values": {"sol": "not noted", "son55": "not noted"},
             "final_value": "Step reductions are 10.7% vs Vanilla and 15.3% vs AWM (text swaps them); Table 8 covers 725 of "
                            "812 tasks, so 42.5% reuse and 7.6% induction are over 725.",
             "reason": "Neither seat recomputed these ratios against their denominators.",
             "evidence_ids": ["opus:O04", "opus:O05", "opus:O06"], "score_impact": "none"},
            {"field_path": "expectations[local:2504.06821-1]",
             "seat_values": {"sol": "local-1 = Table 6 significance wording (unmet)", "son55": "local-1 = LM-evaluator precision (unmet)"},
             "final_value": "Hidden A4 ID collision: sol's local-1 renumbered local-4; son55's kept.",
             "reason": "Same ID and status, different questions; no mechanical conflict was raised.",
             "evidence_ids": ["sol:E13", "son55:E002"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text and appendices first. Provisional: in scope (A); G3 M3 X3 Em3 "
                                                   "Ec2 Eh2 Es1 Ecost1 (63.75); found Table 3 anchor = Vanilla, 4.2 vs 3.8, "
                                                   "swapped step percentages, Table 8 = 725 tasks, Table 6 caption overclaims "
                                                   "significance.",
            "integrity_checks": "Both seats on 2504.06821v2; hashes equal conflicts.json; full 15+31 identification in both.",
            "core_claim_check": "40.4/32.7 = +23.5% rel ✓; 40.4/36.3 = +11.3% rel ✓; steps 5.0/5.6 = −10.7%, 5.0/5.9 = −15.3% "
                                "(text swapped); Table 3 36.4−32.6 = 3.8 (text 4.2); 32.6 = Vanilla shop.",
            "same_score_review": "Seats agreed at 65.0 on every rating. Item-by-item re-check kept G/M/X/Em/Ec/Eh/Ecost and "
                                 "corrected the shared E.statistics over-credit (2→1).",
            "retention_check": "Failure denominator: Table 8 over 725/812; selection vs test: online on the scored stream, no "
                               "labels; extra budget: verification replays and evaluator calls not counted.",
        },
    }

    # =========================================================== 2504.07079 SkillWeaver
    p = "2504.07079"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "we observe a substantial relative improvement in success rate, 39.8 % 39.8\\% on average, for the "
                    "baseline agent with GPT-4o", "§4.1 WebArena Results",
                    "Table 1 GPT-4o average is 22.6→29.8 = +31.9% (Δ 32%); 39.8% is the live-site figure."),
            opus_ev(p, "O02", "and an even larger improvement of 54.3 % 54.3\\% with GPT-4o-mini", "§4.1",
                    "Table 1 GPT-4o-mini average 9.2→14.1 = +53.3%; the table's own Δ prints 45%."),
            opus_ev(p, "O03", "Gitlab: 180 tasks", "Appendix B",
                    "Per-site counts 180+109+187+182+106 = 764, while §3.1 states 812 tasks; the averaging denominator is "
                    "unstated."),
            opus_ev(p, "O04", "Because our criteria for a function to be “verified” was to have it be called without producing "
                    "an exception", "Appendix D.2.1", "Admission criterion for honed APIs."),
            opus_ev(p, "O05", "Successfully completed express checkout, resulting in an order confirmation page with order "
                    "number 000000191.", "Appendix D.1.1, express_checkout usage log",
                    "Exploration places real orders in the WebArena shopping sandbox; no state reset before evaluation is "
                    "described."),
            opus_ev(p, "O06", "Do not interact with the Advanced Reporting tab if you are using Magento.", "Appendix A.1",
                    "Hand-written, benchmark-specific guardrails in the exploration prompt."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": [], "outside_taxonomy": False,
            "reason": "Same ruling as 2504.06821: Playwright API programs are C25's machine-checkable artifacts, executed as "
                      "unit tests in a verify-and-revise loop; no proved property preservation for operator substitution.",
            "matches": [smatch("son55", p, "decompose_and_delegate")],
            "executes_pattern": "partial (artifact + test loop; exception-free acceptance)",
            "resolves_problem": "partial: library on/off +7.2 points WebArena, +9/57 live",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("son55", p, "crystallize_executable_capability")],
            "unassigned": [], "revision_proposals": [],
        },
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("sol", "local:2504.07079-1"): "local:2504.07079-4",
                                 ("sol", "local:2504.07079-2"): "local:2504.07079-5"}, overrides={}),
        "claims": lambda c: c,
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Library built by task-agnostic exploration, frozen, then used on unseen WebArena and live "
                                   "tasks and by a weaker agent; same-agent skills on/off isolates the library as a whole.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single runs: the pre-built library lifts the same GPT-4o agent 22.6→29.8 on "
                                         "WebArena (+31.9% rel), 23→32 of 57 manually judged live tasks, and GPT-4o-mini "
                                         "9.2→14.1 (+53.3% rel; paper prints 45% and 54.3%). 'Robust' APIs are not "
                                         "established (exception-free acceptance, opus:O04); SteP is higher overall; the "
                                         "role of proposal/reward/honing stages and exploration cost are not shown.",
            "unresolved": ["Scored WebArena denominator (764 vs 812, opus:O03).", "Sandbox state reset after exploration "
                           "(opus:O05).", "Exploration cost.", "Stage ablations."]},
        "ratings": {
            "G": R("resolved", 3, "Opus sides with sol. The fixed objects (trajectory demonstrations, unverifiable text "
                   "routines, test-query access in AWM/ICAL) and the residual problem (query-free autonomous skill "
                   "acquisition) are concrete with Voyager/Friday/AWM lineage. Not 4: neighbours compared via external "
                   "numbers only — charged under E.causality, as for 2504.00185 and 2504.06821.",
                   ["son55:E018", "sol:E02", "sol:E03"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. Propose–practise–synthesise–hone is coherent, but the "
                   "assumptions that the novelty curriculum and LLM reward select good skills are untested and the honing "
                   "check accepts exception-free code (opus:O04). This gate weakness is charged here once.",
                   ["son55:E002", "son55:E003", "son55:E005", "opus:O04"], ["son55:E006"]),
            "X": R("resolved", 3, "Opus sides with son55. Every stage is reconstructable from full prompts (proposal, action "
                   "synthesis, success check, persistence, scraping, retrieval), the library format carries pre-conditions "
                   "and usage logs, and failure modes are reported openly; retirement, versioning, size and state reset "
                   "absent. The weak gate is not charged twice (it is in M).",
                   ["son55:E004", "son55:E005", "son55:E007", "son55:E016", "son55:E019"]),
            "E.measurement": R("resolved", 2, "Opus sides with sol. The 812-task WebArena checker is credible, but the scored "
                               "denominator is ambiguous (764 per-site vs 812, opus:O03), live results are author-judged "
                               "without blinding, and headline relative gains disagree across abstract, §4.1 and Table 1 "
                               "(opus:O01, opus:O02). Unlike 2504.06821 the inconsistencies sit in the headline gain figures.",
                               ["sol:E19", "sol:E10", "opus:O01", "opus:O02", "opus:O03"], ["son55:E011"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Skills on/off on two agents and two benchmarks is a "
                             "clean store-off control; no stage ablation, no equal-compute alternative, external-number "
                             "comparisons (SteP higher overall).", ["son55:E008", "son55:E014", "son55:E010", "sol:E20"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. Exploration never sees benchmark queries and the library "
                           "transfers to a different executor; deductions: no overlap check, unspecified sandbox reset after "
                           "state-changing exploration (opus:O05), benchmark-specific prompt guardrails (opus:O06).",
                           ["son55:E013", "son55:E014", "sol:E02", "opus:O05", "opus:O06"]),
            "E.statistics": R("resolved", 1, "Both seats 1 (A2 ladder): counts and a null cell (Cars) visible; one run at "
                              "temperature 0.3, no intervals.", ["son55:E011", "sol:E11"]),
            "E.cost": R("resolved", 1, "Opus sides with sol. The exploration budget is stated in iterations (160 per site, "
                        "iteration defined) and cost is cited as a selection constraint, so cost is not wholly unreported; "
                        "no tokens, time, honing or retrieval cost. Same level as 2504.06821 (steps/induction counts only).",
                        ["sol:E07", "son55:E012"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–D (figures 3, 9–10 are images, text-only use); in scope "
                  "(A: self-built executable skill library); all eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "Consistent with 2504.06821: executable artifact + test loop (C25); no proved substitution property.",
                ["son55:E004", "son55:E005", "sol:E01"], "none (patterns never score)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["decompose_and_delegate", "C25"]],
                "Sub C25.", ["son55:E005"], "none"),
            take(p, "local:2504.07079-1", "son55",
                 "ID collision: sol's local-1 (relative-gain inconsistencies, partial) renumbered local-4. son55's local-1 "
                 "(live tasks manually judged, no blinding or second rater) verified.", ["son55:E011", "sol:E10"], "none"),
            take(p, "local:2504.07079-3", "son55", "Verified: single run, no tests; figures inconsistent.",
                 ["son55:E021", "opus:O01"], "none"),
            take(p, "rs:architectural_operator_substitution/RE-1", "sol", "Check kept: no semantic-preservation argument; "
                 "D.2.1 shows silent no-ops pass — partial.", ["sol:E13"], "none"),
            take(p, "rs:architectural_operator_substitution/RE-2", "sol", "Library on/off exists; no stage ablation — partial.",
                 ["sol:E20"], "none"),
            take(p, "rs:decompose_and_delegate/RE-1", "son55", "No exploration/selection cost.", ["son55:E007"], "none"),
            take(p, "rs:decompose_and_delegate/RE-2", "son55", "No ablation of proposal, reward, honing, composition or "
                 "selection.", ["son55:E008"], "none"),
            take(p, "rs:decompose_and_delegate/RE-3", "son55", "Prompts listed (App. A).", ["son55:E019"], "none"),
            take(p, "rs:decompose_and_delegate/RE-4", "son55", "WebArena + live sites + weaker agent.", ["son55:E013",
                 "son55:E014"], "none"),
            take(p, "rs:decompose_and_delegate/RE-5", "son55", "Skills-off fair; AutoEval/SteP external; AWM/ICAL not run.",
                 ["son55:E010"], "none"),
            take(p, "rs:decompose_and_delegate/RE-6", "son55", "Failure analysis qualitative only.", ["son55:E017"], "none"),
            take(p, "rsi:crystallize_executable_capability/F4", "son55", "Per-site libraries; data-dependent skills lack test "
                 "inputs.", ["son55:E005"], "none"),
            take(p, "rsi:crystallize_executable_capability/H06-step1", "son55", "Exploration uses no benchmark queries.",
                 ["son55:E013"], "none"),
            take(p, "rsi:crystallize_executable_capability/H06-step5", "son55", "Construction cost not reported in tokens/time.",
                 ["son55:E007"], "none"),
            res(X(p, "rsi:crystallize_executable_capability/S1"), *C(p, X(p, "rsi:crystallize_executable_capability/S1")),
                "sol", "unmet",
                "S1 requires execution-based success (replayed success, invocation, state change), not judgment. Practice "
                "success is an LLM reward and honing accepts any exception-free call; the authors show broken APIs passing "
                "(opus:O04). Execution is present but not as the success criterion — unmet.", ["sol:E13", "opus:O04"],
                "none; charged once under M=2"),
            take(p, "rsi:crystallize_executable_capability/S2", "son55", "Novelty by prompt only.", ["son55:E002"], "none"),
            take(p, "rsi:crystallize_executable_capability/S3", "sol", "LLM-made test parameters; real-data gap (D.2.2).",
                 ["sol:E06", "sol:E15"], "none"),
            take(p, "rsi:crystallize_executable_capability/S4", "son55", "Error-driven selector repair (D.1.2).",
                 ["son55:E005"], "none"),
            take(p, "rsi:crystallize_executable_capability/S5", "son55", "Skills on/off on 812 and 57 tasks.", ["son55:E008"],
                 "none"),
            rating_res(p, "G", "sol", {"status": "resolved", "rating": 3},
                       "son55's deductions (neighbours not run, external numbers) are evidence-side and charged under "
                       "E.causality=2; the gap and lineage themselves are concrete.", ["son55:E018", "sol:E02"],
                       "+3.75 vs son55 value"),
            rating_res(p, "X", "son55", {"status": "resolved", "rating": 3},
                       "sol's X=2 and M=2 both charge the exception-free gate; per A2 one defect is charged once (M). The "
                       "remaining X evidence (full prompts, library format, selection module, open failure reporting) "
                       "supports 3.", ["son55:E005", "son55:E016", "opus:O04"], "+5.0 vs sol value"),
            rating_res(p, "E.measurement", "sol", {"status": "resolved", "rating": 2},
                       "son55's 3 treated the inconsistencies as prose slips; they sit in the headline relative gains "
                       "(opus:O01, opus:O02) and the averaging denominator is unstated (opus:O03), with unblinded live "
                       "judging.", ["opus:O01", "opus:O02", "opus:O03", "sol:E10"], "-2.5 vs son55 value"),
            rating_res(p, "E.cost", "sol", {"status": "resolved", "rating": 1},
                       "An iteration budget (160/site, defined) is a reported cost scale, so not_reported (0) overstates the "
                       "absence; still no tokens/time.", ["sol:E07"], "+1.25 vs son55 value"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2504.07079-2]",
             "seat_values": {"sol": "local-2 = cost (unmet)", "son55": "local-2 = reward-model/library correctness audit (unmet)"},
             "final_value": "Hidden A4 ID collision: sol's local-2 renumbered local-5; son55's kept.",
             "reason": "Same ID and status, different questions; no mechanical conflict was raised.",
             "evidence_ids": ["sol:E07", "son55:E006"], "score_impact": "none"},
            {"field_path": "assessment.unresolved / ratings.E.holdout.reason",
             "seat_values": {"sol": "not noted", "son55": "website-state reset listed as unresolved, no evidence cited"},
             "final_value": "Exploration mutates the evaluation sandbox (orders placed, branches deleted) and the exploration "
                            "prompt carries benchmark-specific guardrails; no reset is described.",
             "reason": "Grounded with quotes so the E.holdout deduction is traceable.",
             "evidence_ids": ["opus:O05", "opus:O06"], "score_impact": "none (E.holdout stays 3)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read full text and appendices first. Provisional: in scope (A); G2–3 M3 X2–3 "
                                                   "Em2 Ec2 Eh3 Es1 Ecost1; found 39.8% misattributed to WebArena, 54.3 vs 45 "
                                                   "vs 53.3, 764 vs 812, sandbox mutation during exploration.",
            "integrity_checks": "Both seats on 2504.07079v1; hashes equal conflicts.json; full 15+31 identification in both.",
            "core_claim_check": "29.8/22.6 = +31.9% ✓ (§4.1 says 39.8 ✗); 14.1/9.2 = +53.3% (table 45 ✗, text 54.3 ✗); live "
                                "weighted averages 40.2/56.2 reproduce from per-site rates and 23/17/8/9 tasks ✓.",
            "retention_check": "Selection vs test: task-agnostic exploration, frozen library; extra budget: 160 exploration "
                               "iterations/site uncounted vs baseline; 'kept library' shown via on/off, robustness not shown.",
        },
    }
    return S


def batch_notes():
    return [
        "Seat inputs: sol a1 and son55 a1 for all five papers (no overrides). Hashes equal conflicts.json seat_record_hashes.",
        "Rating disputes resolved: 2503.22678 Em→son55 (38.75; sol 41.25, son55 38.75); 2504.00185 G→sol, Ec,Eh→son55 (60.0; "
        "66.25/56.25); 2504.00587 Em→son55 (43.75; 46.25/43.75); 2504.07079 G,Em,Ecost→sol, X→son55 (58.75; 53.75/56.25).",
        "2504.06821 (both seats 65.0, zero rating conflicts): item-by-item re-check; shared E.statistics over-credit corrected "
        "2→1 under the frozen A2 ladder (main 812-task result has no uncertainty) → 63.75. Table 3 anchor row equals Vanilla, "
        "not AWM; '+4.2' is 3.8 by the table; step percentages swapped; Table 8 covers 725/812.",
        "2504.00185 (Δ10): recomputed Tables 6 vs 7 — the VLM critic's isolated effect is ≈0 (negative on CUB), contradicting "
        "'critic is essential'; 'improves in every case' contradicted by tie cells.",
        "2504.00587: two DeepSeek-V3 MATH cells (91.67, 88.00) are unattainable on the stated 140-item test; Table 3 API-Bank "
        "32.00 vs Table 1 29.00 for the same configuration.",
        "2503.22678: NEJM text contradicts Table 1 (GPT-4o baseline 26.7 = MedAgentSim 26.7; best NEJM Ext. baseline 25.8).",
        "2504.07079: headline relative gains inconsistent across abstract/§4.1/Table 1; 764 vs 812 denominator; exploration "
        "mutates the sandbox without described reset; honing accepts exception-free code.",
        "RS rulings: executable-skill papers (2504.06821, 2504.07079) → decompose_and_delegate/C25 consistently; Escher → "
        "self_supervised_signal_engineering/C07. Hidden local-ID collisions renumbered in 4 papers and recorded.",
        "Card revision proposals (stage end, not applied): attribute_and_patch boundary for perception-side concept libraries "
        "(sol, son55); online post-episode crystallisation vs H06 practice (sol).",
    ]
