"""Opus rulings for r16b a1 (data only; consumed by _build.py)."""
import copy

KEYS = ["G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost"]


def batch_notes():
    return [
        "Seat-input integrity: all ten a1 seat records match conflicts.json seat_record_hashes and the batch manifest "
        "(input_hash bed8c93a…, per-paper version and material sha256). No controller action needed.",
        "2604.17658 ErrorProbe (Δ17.5): final 45.0 (= son55). G → son55 2 (step-localisation gap is sourced, but the "
        "memory-corruption gap is only asserted and AgenTracer/Yu et al. are never compared). M → son55 2 (Verify = a "
        "reproducible tool symptom, not evidence that the step is the originating one; dependency-graph construction "
        "unspecified). X → son55 2 (append-only store; Table 3's α/1536-d embedding retrieval contradicts §4.4's exact-"
        "MAST-tag signature match; Verify for web/file traces unspecified). E.causality → son55 1 (store-off is the only "
        "isolating control; the introduction's claimed component ablations do not exist; the 'verified' gate is never "
        "ablated; pipeline vs judges is compute-unmatched; PRIME r14b / 2603.17187 r12b convention). Opus findings: five "
        "Table 1 'Average' cells are not the mean of their rows (Claude no-memory step is 40.30, not 41.90, so the Claude "
        "memory step gain is +2.4, not +0.8); TracerTraj's code subset is drawn from MBPP+/KodCode tasks, so Fig. 3's "
        "'OOD' KodCode→AgenTracer transfer is not source-disjoint.",
        "2604.18292 Agent-World (status conflict): out_of_scope (= son55) under rubric A3. The improved and evaluated "
        "object is GRPO-trained Qwen3-8B/14B weights; environments, tasks and diagnosis guidelines are RL training data "
        "for the next policy (§3.2.1, §3.2.2, Algorithm 1, §4.1, §4.3), not a harness component read at test time. "
        "sol's needs_fulltext: confirmed that the pinned HTML ends after the '9.1 Case 1: Ecomm MCP Server' heading "
        "(LaTeXML footer follows) and that Appendix 7's Table 7 output schema is absent; this is an HTML-conversion "
        "loss. The official PDF v1 exists (48 pp; its outline lists Appendix C 'Case Study' with 'Case 1: Ecomm MCP "
        "Server' and 'Case 3: Population Data Server'), so it is recoverable, but no material request is raised: the A3 "
        "ruling rests on sections present in full. The PDF was opened once only to check recoverability; it is not "
        "evidence and was not added to the materials.",
        "2604.19572 TACO (Δ5): final 63.75 (= son55). X → son55 3 (rule schema, the information-boundary table, all "
        "prompts, write-back and suppression rules are given; τ, the confidence update and round counts are missing "
        "parameters, not missing structure; EvolveRouter r14b convention). RS → generative_process_redesign primary "
        "(sol) + self_supervised_signal_engineering supporting, sub null (complaint signal; C08 is a retraining tactic). "
        "Domain → H01 + H07 + H30. evidence_level task (both): rules evolve over several rounds on the evaluated "
        "benchmark, k/N are tuned on TB 2.0 and 'reuse' is re-run on TB 2.0.",
        "2604.19795 Prism (Δ10): final 21.25 (= son55). claim_support → unsupported (son55). Sub-claims are refuted "
        "(Theorem 3.2's bound exceeds |M| when n·k>|M|, and Pinsker is used backwards), but the headline LOCOMO/IR "
        "claims are unsupported rather than refuted. G → 1, X → 1, E.statistics → not_reported 0 (son55). Opus finding "
        "neither seat raised: Table 3 reports KR 0.42/0.38/0.35 for single-agent Prism, but KR is defined as the "
        "fraction of retrieved memories contributed by other agents, so it must be 0 with one agent. The r=0.89 "
        "'knowledge, not compute' evidence is internally inconsistent.",
        "2604.19837 Forage V2 (Δ7.5): final 45.0 (between seats: sol 53.75, son55 46.25). G → son55 2, M → son55 2, E.cost → "
        "sol 2, evidence_level → sol task. Opus findings: seeded runs append to the knowledge base that later seeded "
        "runs read (B.4 source 'Sonnet seeded run_005'; 106 entries), so the 'three independent runs at 266' are "
        "sequentially anchored. Counting the six Opus runs that built the base (≈$30.30), seeded Sonnet does not save "
        "money over six runs (≈$61.1 vs ≈$56.4 cold). Opus's own accumulation shows no round or coverage trend (all "
        "4 rounds).",
        "A4 hygiene: hidden local-ID collisions handled in 17658 (local-1/-2), 19572 (local-1/-2), 19795 (local-1/-2) and "
        "19837 (local-2). Same-question pairs were merged and different questions renumbered. Every move is recorded in "
        "the expectation note and in shared_error_corrections or the resolution.",
        "Figure dependence: ErrorProbe Figs 1/3, TACO Figs 1/3–6, Prism Figs 2–3 and Forage Figs 2–5 are image-only or "
        "axis-tick text only. Only values stated in text or tables are used, and no curve value is read off a figure.",
        "No material requests. Seats' requests for neighbour originals (AgenTracer/Yu et al./Who&When; SWE-Pruner/"
        "LongCodeZip; Mem0/Coral; Forage V1/Hermes/MemRL/Voyager) are non-blocking: no disputed rating depends on them.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"

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

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a = prefix(a, s)
        a.update(upd)
        return a

    def merged(other, extra_ev=()):
        return {"note": f"{other} merged here (A4: same question under a colliding or different ID).",
                "merged_from": other, "merged_evidence_ids": list(extra_ev)}

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    # =========================================================== 2604.17658 ErrorProbe (Δ17.5)
    p = "2604.17658"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "specifically focusing on the code generation domain (e.g., tasks from MBPP+, KodCode)",
                    "Appendix A, Benchmark Details (TracerTraj)",
                    "The TracerTraj code subset used as the 'AgenTracer' target is built from MBPP+/KodCode tasks. Fig. 3's "
                    "transfer 'from KodCode to AgenTracer', which §6.2 calls an OOD setting, is therefore not task-source "
                    "disjoint, and no overlap audit is reported.", kind="our_inference"),
            opus_ev(p, "O02", "68.50% 34.60% 49.20% 58.70% 46.60% 27.6% 56.33% 41.90%",
                    "Table 1, ErrorProbe (ours) / Claude 3.7 Sonnet row",
                    "Opus arithmetic: the listed Average Agent/Step (56.33/41.90) are not the means of the three benchmark "
                    "cells, which are (68.5+49.2+46.6)/3 = 54.77 and (34.6+58.7+27.6)/3 = 40.30. The with-memory Claude "
                    "step average (42.73) is correct, so the Claude memory step gain on the macro average is +2.43, not "
                    "+0.83. The per-benchmark gains are +4.8/+0.8/+1.7.", kind="our_inference"),
            opus_ev(p, "O03", "67.70% 8.70% 55.60% 41.30% 43.10% 13.80% 57.03% 21.27%",
                    "Table 1, LLM-as-a-Judge / Claude 3.7 Sonnet row",
                    "Opus arithmetic: the Agent average should be (67.7+55.6+43.1)/3 = 55.47, not 57.03. The step average "
                    "21.27 is correct. With recomputed values the Claude agent ordering is judge 55.47 ≈ ErrorProbe 54.77 "
                    "< +memory 61.17 (the with-memory row lists 59.60, but its cells give 61.17).",
                    kind="our_inference"),
            opus_ev(p, "O04", "70.40% 20.50% 46.80% 29.40% 56.90% 27.60% 58.46% 25.83%",
                    "Table 1, ErrorProbe (ours) / GPT-OSS-120B row",
                    "Opus arithmetic: the Agent average is 58.03, not 58.46. In total, 5 of the 24 Average cells in Table 1 "
                    "are mis-computed. Separately, the text says GPT-OSS step 'improves … from 13.7%', but the table "
                    "difference to the judge is 25.83 − 15.13 = 10.7.", kind="our_inference"),
            opus_ev(p, "O05", "Weight for semantic similarity in hybrid retrieval (vs. frequency)",
                    "Appendix A, Table 3 (α = 0.6; d = 1536 'Embedding dimension for memory keys')",
                    "The hyperparameter table describes embedding-based hybrid retrieval weighted against frequency. §4.4 "
                    "instead specifies a structured signature match requiring an exact MAST tag, multiplied by an RFI "
                    "quality score. The implemented retrieval rule cannot be reconstructed uniquely.",
                    kind="our_inference"),
            opus_ev(p, "O06", "Re-runs code snippets in a sandbox to confirm runtime errors.",
                    "§4.3 The Investigator (toolset: CodeExec, LogicProbe)",
                    "The memory gate's Verify(E) is defined as success of tool-grounded reproduction with CodeExec or "
                    "LogicProbe. Reproducing a runtime symptom confirms that an error exists, not that the hypothesised step "
                    "is where it originated."),
            opus_ev(p, "O07", "The tasks involve complex, multi-step real-world scenarios such as open-ended web navigation "
                              "and file manipulation.",
                    "Appendix A, Who&When-Hand",
                    "For web-navigation and file-manipulation traces, the paper never states how CodeExec or LogicProbe "
                    "'reproduces' an error, so the write gate's operation on one of the three main benchmarks is "
                    "unspecified.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus: the gain the paper headlines (Table 1: Claude macro step 21.27 → 40.30 recomputed, ≈+19) comes "
                      "from splitting diagnosis into backward tracing, hypothesis generation, tool-grounded verification "
                      "(the Investigator 'must generate a diff or an execution log') and arbitration. A machine-checkable "
                      "artifact is routed to a sandbox, which is decompose_and_delegate/C25 (son55). The retained part, "
                      "verified guards retrieved into later diagnoses without parameter updates, is "
                      "adapt_via_conditioning/C03's reference-substrate sub-move (sol), kept as supporting. son55's "
                      "self_supervised_signal_engineering/C08 is dropped: C08 manufactures and filters training instances "
                      "for retraining, while here the filtered output is inference-time memory (son55 itself rated it "
                      "weak).",
            "matches": [smatch("son55", p, "decompose_and_delegate"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30",
                                              fit="weak (admission gate only; no retirement, bound or replay)")],
                           "unassigned": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]["unassigned"]), "sol"),
                           "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "decompose_and_delegate", "rs_sub": "C25",
             "domain": {"namespace": "rsi", "main": "evidence_gated_retention", "sub": "H30"},
             "operation_correspondence": "Investigator's executable evidence (diff/execution log) is the machine-checkable "
                                         "artifact. The same verdict (Verify ∧ c>τ) decides admission of a guard to the "
                                         "persistent store.",
             "necessary_conditions_and_differences": "H30 needs admission paired with retirement, a size bound and a "
                                                     "replay or regression budget; ErrorProbe has admission only. C25 "
                                                     "needs an ablation showing the delegated check is load-bearing; none "
                                                     "is reported.",
             "evidence_ids": ["son55:E002", "son55:E018", "opus:O06"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H00"},
             "operation_correspondence": "Verified diagnoses are abstracted into natural-language guards (H00 lesson "
                                         "store) and retrieved as conditioning for later traces without parameter "
                                         "updates (C03 reference-substrate transfer).",
             "necessary_conditions_and_differences": "C03 earns generalisation by holding out whole categories; Fig. 3's "
                                                     "target overlaps its source (opus:O01). H00 asks for contrast and "
                                                     "maintenance (S2/S4), which are absent.",
             "evidence_ids": ["son55:E021", "sol:E005", "sol:E007", "opus:O01"]},
        ],
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.17658-1"): "local:2604.17658-4",
                    ("son55", "local:2604.17658-2"): "local:2604.17658-1"},
            overrides={
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "unmet",
                    "reason": "Opus (revised from sol partial): RE-2 asks for an overlap analysis before a held-out or "
                              "transfer claim is accepted. None is given, and TracerTraj's code subset is drawn from "
                              "MBPP+/KodCode tasks (opus:O01), so the 'OOD' KodCode→AgenTracer curve is not source-"
                              "disjoint. The Table 2 train/test split is real but has no dedup or size report.",
                    "evidence_ids": ["sol:E006", "sol:E007", "sol:E009", "opus:O01"]},
                "rsi:abstract_experience_into_guidance/S3": {
                    "status": "partial",
                    "reason": "Opus (shared correction; both seats wrote met): grounding exists for code traces "
                              "(CodeExec, LogicProbe). It is unspecified for Who&When-Hand web and file traces "
                              "(opus:O07), and a reproduced symptom does not certify the originating step (opus:O06)."},
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "unmet",
                    "reason": "Opus (son55): Eq. 2 is a pure union. RFI recency/frequency statistics only rank "
                              "retrieval. There is no merge, forgetting, conflict handling or bound."},
                "local:2604.17658-1": {
                    "status": "partial",
                    "reason": "Opus: holdout of the retained memory. Table 2 builds memory on a train partition and tests "
                              "on manually annotated test traces (sizes not given). Table 1 accumulates memory on the "
                              "evaluated stream, label-free but with undeclared order. Hyperparameters are tuned on a "
                              "10% TracerTraj subset whose relation to the test set is not stated.",
                    **merged("son55:local:2604.17658-2 (stream accumulation = reported stream, partial)",
                             ["son55:E011"])},
                "local:2604.17658-4": {
                    **renum("son55:local:2604.17658-1"),
                    "reason": "Opus (verified son55): the stated objective includes 'minimizing memory size and false "
                              "positive updates', but no false-positive write rate, rejection count or memory size is "
                              "reported."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O02", "opus:O03"]), "C2", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: five Table 1 Average cells are mis-computed (opus:O02–O04). Recomputed, the Claude memory step gain is "
            "+2.4 (not +0.8), and Claude agent accuracy is judge 55.47 ≈ ErrorProbe 54.77 < +memory 61.17.",
            "Opus: Fig. 3's 'OOD' transfer source (KodCode) is inside the target benchmark's task sources (opus:O01).",
            "Opus: the retrieval rule in §4.4 (exact MAST-tag signature × RFI) conflicts with Table 3's embedding-based "
            "hybrid retrieval (opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The step-localisation gap is concrete and sourced: single-pass "
                   "judges score below 10% step accuracy on TracerTraj (Table 1, son55:E004). Not 3: (i) the "
                   "self-improvement half of the gap ('naive approaches degrade', memory corruption) is asserted and "
                   "never demonstrated; (ii) the nearest neighbours, the trained tracer AgenTracer (whose dataset is used) "
                   "and Yu et al.'s training-free transfer, are named but never compared (son55:E023); (iii) the "
                   "remaining residual is not bounded.",
                   ["son55:E004", "son55:E018", "son55:E023", "sol:E001"]),
            "M": R("resolved", 2, "Opus sides with son55. The chain MAST tags → backward pruning → hypotheses → tool "
                   "evidence → arbiter → gated write → retrieval is coherent and makes a distinguishing prediction "
                   "(gated vs naive memory under shift). But the load-bearing assumption is weak. Verify(E) certifies "
                   "that a symptom reproduces (opus:O06), not that the hypothesised step is the originating one, which "
                   "is the very quantity the paper targets. Verify is undefined for web/file traces (opus:O07), and how "
                   "dependency edges are built is unstated (son55:E026).",
                   ["son55:E002", "son55:E020", "son55:E026", "sol:E003", "sol:E004", "opus:O06", "opus:O07"]),
            "X": R("resolved", 2, "Opus sides with son55. The pipeline and the k/τ/threshold settings are given, but key "
                   "conditions are unclear or contradictory. The store is append-only, with no retirement, merge, "
                   "conflict handling, versioning or rollback (son55:E024). The §4.4 retrieval rule (exact MAST-tag "
                   "signature × RFI, τ_ret = 0.75) contradicts Table 3's embedding hybrid retrieval with α = 0.6 and "
                   "d = 1536 (opus:O05). RFI's 'performance delta' has no label-free definition. Verify for non-code "
                   "traces and the dependency parser are unspecified. An undefined 'Analyzer' role appears in §4.4.",
                   ["son55:E002", "son55:E003", "son55:E024", "son55:E026", "sol:E005", "opus:O05", "opus:O07"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. Top-1 agent/step accuracy against programmatic "
                               "(TracerTraj) or human (Who&When) labels suits the claim. Limits: 127/127/58 items; the "
                               "authors annotated the Table 2 test traces with no agreement reported; and reporting "
                               "errors in 5 of 24 Table 1 averages (opus:O02–O04). Table 4 says Who&When-Algo ground "
                               "truth is 'Algorithm Generated' while the text says human-annotated. Charged here once "
                               "(A2).",
                               ["son55:E004", "son55:E010", "son55:E017", "sol:E013", "sol:E014", "opus:O02",
                                "opus:O03", "opus:O04"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. The only isolating control is memory on/off (Table 1 "
                             "on three backbones, Table 2 on four domains; sol:E012, son55:E006). Everything else that "
                             "would attribute the gains is missing. (i) The introduction claims 'ablations showing that "
                             "backward tracing, structured failure-mode cues, and verified memory each contribute' "
                             "(son55:E018), but no such ablation exists in the paper or Appendices A–B. (ii) The defining "
                             "'verified-before-write' gate has no gate-off or naive-memory arm. (iii) The headline pipeline "
                             "gain over the judges is compute-unmatched: multi-agent tool calls against one pass. Convention: "
                             "PRIME r14b and 2603.17187 r12b (store-off only → 1).",
                             ["son55:E005", "son55:E006", "son55:E018", "sol:E012"], ["sol:E012"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked, with an Opus addition. Table 2 builds memory on train "
                           "and tests on held-out annotated traces, and the write gate uses no labels. But Table 1 "
                           "accumulates memory on the evaluated stream in an undeclared order, and hyperparameters are "
                           "tuned on a TracerTraj subset whose overlap is unstated. Fig. 3's 'OOD' source KodCode is one "
                           "of the target benchmark's task sources (opus:O01), so the cross-domain claim is scoped to "
                           "in-domain transfer. Kept at 2 because the Table 2 split is a genuine held-out test.",
                           ["son55:E010", "son55:E011", "son55:E016", "son55:E019", "sol:E006", "sol:E009", "opus:O01"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder). There are 5 runs with stated typical SD "
                              "(±1.5/±2.5) and a two-proportion z-test against the judge. The tables report medians only, "
                              "the same paragraph says 'averaged', memory on/off is never tested, and Table 2 test sets "
                              "are tiny (e.g., GSM8K 25/30/50/65% implies about 20 items).",
                              ["son55:E012", "son55:E013", "son55:E014", "sol:E008"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only a ≈45 s Claude latency per diagnosis is given. "
                        "There are no token or call counts, no sandbox or memory costs and no budget-matched judge "
                        "(e.g., self-consistency).", ["son55:E015", "sol:E010"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text with Appendices A–B read. In scope (system_method): verified natural-"
                  "language diagnostic guards are written from execution evidence, retained and retrieved into later "
                  "diagnoses (non-weight memory). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Fig. 1 (bars) and Fig. 3 (learning curves) are image-only; only text-stated +1.6/+4.0 and "
                             "table values are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "The headline gain comes from the decomposition with a machine-checked Investigator artifact (C25), not "
                "from the memory. See rs_pattern.reason.", ["son55:E002", "sol:E003", "opus:O02"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["decompose_and_delegate", "C25"], ["adapt_via_conditioning", "C03"]],
                "son55's C25 is the primary. sol's C03 (reference-substrate conditioning) is kept as supporting for the "
                "retained memory. son55's C08 is dropped: there is no retraining, and the filtered product is inference-"
                "time memory.",
                ["son55:E002", "son55:E021", "sol:E004", "sol:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["evidence_gated_retention", "H30"]],
                "H00 is agreed. H30 is kept at weak fit because the paper's stated remedy for memory corruption is an "
                "admission gate. The missing retirement, bound and replay are recorded as unmet conditions (S2/S4), "
                "not used to drop the match.", ["son55:E002", "son55:E024"], NOSCORE),
            XC(p, "local:2604.17658-1", "sol", "partial",
               "A4 hidden collision. sol's local-1 asks about holdout of the retained memory, son55's about the gate's "
               "false-positive write rate. Final local-1 is sol's question; son55's local-2 (the stream equals the "
               "reported stream) is the same question and is merged here, partial in both. son55's local-1 moved to "
               "local-4 (unmet, verified).", ["sol:E006", "son55:E011", "son55:E024"]),
            XC(p, "local:2604.17658-3", "sol", "partial",
               "Cost (sol only). Verified: 45 s latency only, with no total verification or memory cost.", ["sol:E010"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "adapt_via_conditioning is kept as supporting. Memory on/off isolates the conditioning channel, but there "
               "is no naive-cache or budget-matched alternative.", ["sol:E012", "son55:E006"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "revised", "unmet",
               "RE-2 requires an overlap analysis before held-out claims. None is reported, and the Fig. 3 source "
               "(KodCode) is among the target benchmark's task sources (opus:O01).", ["sol:E007", "opus:O01"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Verified: only latency is reported, with no tokens, calls or sandbox cost.", ["son55:E015"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "Verified: the claimed per-component ablations are absent in the main text and Appendices A–B "
               "(son55:E018).", ["son55:E018"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "There are three attribution benchmarks plus one transfer pair, all in MAS attribution, with the pair "
               "overlapping (opus:O01).", ["son55:E017", "son55:E019", "opus:O01"]),
            XC(p, "rs:decompose_and_delegate/RE-5", "son55", "partial",
               "There are judge and Agent-as-a-Judge baselines, but no trained tracer (AgenTracer) and unmatched compute.",
               ["son55:E004", "son55:E005", "son55:E023"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "The vertical (MAS failure attribution) carries much of the novelty. The execution-reproduction gate is "
               "a partial differentiator.", ["son55:E001", "son55:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Eq. 2 is a pure union and RFI statistics only rank retrieval. There is no maintenance operation.",
               ["son55:E024", "sol:E004"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "not_applicable",
               "The paper claims verification-based retention, not counterfactual-utility credit. RFI's 'performance "
               "delta' is never operationalised, which is recorded under X, not here.", ["son55:E002"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Verified: admission only, with no retirement or size bound.", ["son55:E024"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "unmet",
               "Verified: no gate-off or naive-write arm, so the gate's effect is not ablated.", ["son55:E018"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.G. The self-improvement gap is asserted, and the nearest neighbours are uncompared.",
                ["son55:E018", "son55:E023"], "−3.75 vs sol"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M. Verify certifies a reproducible symptom, not the originating step, and is undefined for "
                "web traces.", ["son55:E020", "opus:O06", "opus:O07"], "−5.0 vs sol"),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.X. The store is append-only and the retrieval rule is described inconsistently (opus:O05).",
                ["son55:E024", "opus:O05"], "−5.0 vs sol"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.E.causality. Store-off is the only control; the claimed ablations are absent; the gate is "
                "untested; compute is unmatched.", ["son55:E018", "son55:E006"], "−3.75 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims/assessment: Table 1 macro averages",
             "sol_value": "flagged one cell (with-memory Claude agent 59.60 vs 61.17)",
             "son55_value": "used the listed averages (e.g., Claude memory step gain +0.8; agent average below the judge)",
             "final_value": "5 of 24 Average cells are mis-computed (opus:O02–O04). Recomputed Claude step: 40.30 → 42.73 "
                            "(+2.43). Claude agent: judge 55.47, ErrorProbe 54.77, +memory 61.17.",
             "reason": "Neither seat checked the rows. The qualitative reading is unchanged: agent accuracy ≈ judge, and "
                       "the Claude memory gain is small. Charged once under E.measurement.",
             "evidence_ids": ["opus:O02", "opus:O03", "opus:O04"], "score_impact": "none"},
            {"field_path": "expectations[rs:adapt_via_conditioning/RE-2] and the Fig. 3 'OOD' transfer",
             "sol_value": "partial (cross-dataset transfer treated as supported)",
             "son55_value": "Fig. 3 read as cross-domain (one pair)",
             "final_value": "unmet. KodCode is among the TracerTraj task sources (opus:O01).",
             "reason": "Both seats accepted the authors' OOD label. The transfer claim is scoped to in-domain reuse. "
                       "E.holdout stays at 2 because the Table 2 split is real.",
             "evidence_ids": ["opus:O01"], "score_impact": "none"},
            {"field_path": "expectations[rsi:abstract_experience_into_guidance/S3].status",
             "sol_value": "met", "son55_value": "met", "final_value": "partial",
             "reason": "Grounding is specified only for code traces (CodeExec). Its operation on Who&When-Hand web and "
                       "file traces is unstated (opus:O07), and reproduction does not certify the originating step "
                       "(opus:O06).",
             "evidence_ids": ["opus:O06", "opus:O07"], "score_impact": "none"},
            {"field_path": "expectations[local:2604.17658-*].id",
             "sol_value": "local-1 = holdout, local-2 = statistics, local-3 = cost",
             "son55_value": "local-1 = false-positive writes, local-2 = stream holdout",
             "final_value": "local-1 = holdout (merged with son55 local-2), local-2 = statistics, local-3 = cost, local-4 = "
                            "false-positive writes",
             "reason": "A4 hidden ID collisions on local-1 and local-2.", "evidence_ids": ["sol:E006", "son55:E024"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §3–6, Tables 1–6 and Appendices A–B first. In scope "
                                                   "(verified guard memory). There is a large step-localisation gain over "
                                                   "judges with no component ablation despite the introduction's claim, "
                                                   "store on/off as the only memory control, an untested gate, a single "
                                                   "latency figure for cost, and averages that do not add up. Initial "
                                                   "view: G2 M2 X2 Em2 Ec1–2 Eh2 Es2 Ecost1.",
            "integrity_checks": "Both seats a1 on 2604.17658v1, material sha 92df3920…. Canonical seat hashes equal "
                                "conflicts.json, and both complete RS 15+31 and domain identification.",
            "core_claim_check": "The step gain is real in the reported tables. The memory gain is consistent but small for "
                                "Claude. The cross-domain claim is scoped (opus:O01). The component-ablation claim is "
                                "unsupported (son55:E018).",
            "rating_agreement": "G/M/X/E.causality are resolved to son55 by reading the text. Em/Eh/Es/Ecost agree and "
                                "were re-checked, with Opus additions in Em and Eh.",
        },
    }

    # =========================================================== 2604.18292 Agent-World (status conflict)
    p = "2604.18292"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: the "
          "policy is updated with GRPO on synthesized environments (opus:O01), and each self-evolution round ends by "
          "continuing RL to obtain the next policy (opus:O02, opus:O03) from SFT-initialised Qwen3-8B/14B backbones "
          "(son55:E003). The diagnosis guidelines, environments and targeted tasks are curriculum data consumed by that "
          "training (opus:O05). They are not a prompt, skill, tool or memory read by the evaluated agent at test time, "
          "and the 23 benchmarks evaluate the trained checkpoints. Not scored; null is a disposition, not a zero-quality "
          "rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p, "claim_type": "component_training"},
        "materials": [{
            "material_id": f"{p}.txt", "url": "https://arxiv.org/html/2604.18292v1", "version": "2604.18292v1",
            "sha256": "3487c04d726b0a15074104e3b16a67048f13b6a3540b4de9095b0a560d265013",
            "local_path": "research/fulltext/review-runs/rsi-v22-20261021-01/materials/2604.18292.txt",
            "sections_read": ["Opus: §1–6 read in full before opening seat records, plus Appendix 7 (diagnosis prompt), "
                              "Appendix 8 (environment cards, skimmed) and the Appendix 9 remnant"],
            "complete": False,
            "missing_sections": [
                "Appendix 9 Case Study: the text stops after the '9.1 Case 1: Ecomm MCP Server' heading and the arXiv "
                "LaTeXML footer follows (HTML-conversion truncation, opus:O04)",
                "Appendix 7 'Table 7' output schema referenced but absent from the HTML (opus:O05 context)"],
            "note": "Verified extraction loss, not an author omission. arxiv.org/pdf/2604.18292v1 exists (48 pages; its "
                    "outline lists Appendix C 'Case Study' with 'Case 1: Ecomm MCP Server' and 'Case 3: Population Data "
                    "Server'), so the content is recoverable from the official PDF. The PDF was opened once only to check "
                    "this, is not cited as evidence and is not part of the pinned input. No request is raised because "
                    "the A3 disposition depends only on §3.2, Algorithm 1, §4.1 and §4.3, which are complete."}],
        "opus_evidence": [
            opus_ev(p, "O01", "we adopt Group Relative Policy Optimization (GRPO) [ grpo ] to directly maximize the "
                              "verifiable returns defined above", "§3.2.1 Policy Update",
                    "The learning update is GRPO on the policy weights."),
            opus_ev(p, "O02", "we then perform multi-environment agent RL (Sec. 3.2.1 ) on the augmented data to obtain "
                              "an improved policy", "§3.2.2 Agent-Environment Co-Evolution",
                    "Diagnosis-targeted tasks are 'augmented data' for continued RL; the product of each round is a policy."),
            opus_ev(p, "O03", "finally, targeted synthesis and continual RL produce the next-round policy",
                    "§4.3 self-evolving arena analysis (Table 2)",
                    "The self-evolution gains in Table 2 are gains of successive trained policies."),
            opus_ev(p, "O04", "We present three representative trajectories with at least 7 interaction turns.",
                    "Appendix 9 Case Study preamble",
                    "Only the preamble and the 9.1 heading survive in the pinned HTML, after which the LaTeXML 'build "
                    "logs' footer begins. This confirms sol's material finding as an HTML conversion loss.",
                    kind="our_inference"),
            opus_ev(p, "O05", "This arena-driven loop turns scalable environments into an automated curriculum engine",
                    "§3.2.2 (after Algorithm 1)",
                    "The authors themselves cast the environments and tasks as a training curriculum."),
        ],
        "rs_pattern": {"primary": None, "supporting": [], "matches": [], "outside_taxonomy": False,
                       "reason": "Not identified: out_of_scope weight-training paper; neither seat ran the 15+31 "
                                 "identification and none is required for an excluded row. It is not recorded as "
                                 "outside_taxonomy. No score effect.",
                       "executes_pattern": None, "resolves_problem": None},
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "self_generate_the_curriculum", "H23",
                                              fit="high (informational; out_of_scope weight-level boundary member)")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b–r13a). sol wrote null; son55 wrote the non-canonical "
                                              "'not_assessed'.",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric. The benchmark gains are author-reported "
                                             "results of GRPO-trained checkpoints. Both seats wrote 'unresolved'; see "
                                             "shared_error_corrections.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are "
                                      "wrong.",
                                      "The Appendix 9 case trajectories and Table 7 schema are missing from the pinned "
                                      "HTML (conversion loss; recoverable from the PDF). This does not bear on A3."]},
        "ratings": {k: R("unknown", None, a3, ["opus:O01", "opus:O02"]) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "out_of_scope (sol needs_fulltext overruled: the missing appendix material is irrelevant to the A3 "
              "disposition)",
        "figure_dependence": "No figure is used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", None,
                "Null is the run's canonical value for an excluded weight-level row. son55's 'not_assessed' is non-"
                "canonical.", ["opus:O01"], "none (row is unscored)"),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["self_generate_the_curriculum", "H23"]],
                "Informational, per run convention for excluded curriculum papers (r13a H22). The diagnosis agent ranks "
                "weak environments and writes task-generation guidelines (§3.2.2), and targeted tasks are synthesised "
                "and verified for further training. That is H23's (diagnostic signal, verifier) pair; the card itself "
                "is marked as a weight boundary.", ["son55:E001", "son55:E004", "opus:O05"], NOSCORE),
            res("status", *C(p, "status"), "son55", "out_of_scope",
                "A3: the improver's update object and product are both weights (opus:O01–O03). The retained 'arena' "
                "artefacts are training data, not an evaluated non-weight component (opus:O05). sol's needs_fulltext "
                "finding is confirmed (opus:O04: HTML truncation after 9.1; Table 7 missing). It is an extraction loss "
                "recoverable from the PDF, but the missing case trajectories and output schema cannot change what is "
                "trained and evaluated, so they do not block the disposition.",
                ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05", "sol:E001"], "none (row is unscored)"),
        ],
        "shared_error_corrections": [
            {"field_path": "paper.claim_type", "sol_value": "system_method", "son55_value": "system_method",
             "final_value": "component_training",
             "reason": "The paper's evaluated product is trained policy checkpoints (an environment-synthesis + RL "
                       "training recipe). Run precedent for excluded weight-training rows (r13a MM-Zero).",
             "evidence_ids": ["opus:O01", "opus:O03"], "score_impact": "none (row is unscored)"},
            {"field_path": "assessment.claim_support", "sol_value": "unresolved", "son55_value": "unresolved",
             "final_value": None,
             "reason": "Claim support is not assessed for an excluded row, so null is canonical (precedent r09b GenEnv, "
                       "r11a, r12b, r13a).", "evidence_ids": ["opus:O01"], "score_impact": "none (row is unscored)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §1–4 and Algorithm 1 first. Qwen3 backbones are "
                                                   "SFT-initialised then GRPO-trained; the arena loop diagnoses, "
                                                   "synthesises targeted tasks and continues RL → out_of_scope (A3). "
                                                   "Then checked the appendices: Appendix 9 is truncated and Table 7 is "
                                                   "absent.",
            "integrity_checks": "Both seats a1 on 2604.18292v1, material sha 3487c04d…. Canonical seat hashes equal "
                                "conflicts.json. son55's materials entry claims complete=true with no missing sections, "
                                "which is wrong (opus:O04); sol's missing_sections are correct. This is a seat-level "
                                "material description error, not a version mismatch, and needs no controller action.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03 and O05.",
            "rating_agreement": "All eight are unknown in both seats; kept unknown with the A3 reason.",
        },
    }

    # =========================================================== 2604.19572 TACO (Δ5)
    p = "2604.19572"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "the reused rules remain effective on TB 2.0, indicating that they capture generalizable "
                              "terminal-output patterns rather than benchmark-specific artifacts",
                    "§4.7 Rule Reusability",
                    "The 'generalizable' conclusion is drawn from re-running the frozen pool on the same TB 2.0 tasks it "
                    "evolved on, which cannot distinguish general patterns from benchmark-specific ones. Pool rules "
                    "include task-instance triggers such as the FLAG extractor (son55:E020).", kind="our_inference"),
            opus_ev(p, "O02", "TACO updates compression rules only from observation-level interaction signals and does "
                              "not access benchmark correctness signals.",
                    "Appendix I, Table 11 caption",
                    "The information permissions of the improver are stated explicitly, as X asks."),
            opus_ev(p, "O03", "This appendix presents the prompts used in TACO for task-level rule initialization and "
                              "rule evolution.", "Appendix N",
                    "All three LLM call types (selection/refinement, new rule, conservative update) and the static "
                    "baselines' prompts are given."),
            opus_ev(p, "O04", "For an existing effective rule, TACO updates its global confidence",
                    "§2.6 Global Rule Score Updating",
                    "The update rule for c_r^g, the computation of the task-level confidence c_r^t (beyond complaint→0), τ "
                    "and the number of evolution rounds are not given numerically. These are missing parameters of an "
                    "otherwise explicit retention rule.", kind="our_inference"),
            opus_ev(p, "O05", "Qwen3-Coder-480B 23.3 45.7 21,718", "Table 3 (TB 2.0 baseline row)",
                    "Table 3's baseline 23.3 differs from Tables 2/8 (23.90) and Table 4 (23.9 ± 2.9), and its +TACO 25.8 "
                    "matches 25.86. This is a reporting inconsistency of 0.6 points, recorded only.",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["self_supervised_signal_engineering"],
            "outside_taxonomy": False,
            "reason": "Opus: the paper's framing move is to take the compression rule set, previously fixed by hand-crafted "
                      "heuristics or a trained pruner, and make it a variable that evolves online inside a fixed "
                      "conservative executor. That is generative_process_redesign (sol; sub null, since C15/C23/C24 are "
                      "diffusion/geometry/interface tactics), consistent with run convention for skill-evolution papers "
                      "(EvoSkill r11b, MemSkill r10b, SkillClaw r14b). son55's self_supervised_signal_engineering is kept "
                      "as supporting with sub null: the reward-free complaint signal (the agent asking for full output or "
                      "repeating a command) is a manufactured adaptation signal. C08 is a generate → filter → retrain "
                      "tactic and nothing is retrained. heterogeneous_decomposition (the Critical bypass) is a design "
                      "detail, not a pattern-level move, and is dropped.",
            "matches": [smatch("sol", p, "generative_process_redesign"),
                        smatch("son55", p, "self_supervised_signal_engineering", sub_id=None, role="supporting",
                               reason="Supporting: complaint-driven, label-free adaptation signal. sub_id set to null "
                                      "because C08 manufactures training instances for retraining, which TACO never "
                                      "does.")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "crystallize_executable_capability", "H07"),
                                       dmatch("son55", p, "evidence_gated_retention", "H30",
                                              fit="weak (write-back gate + confidence decay; no bound or replay)")],
                           "unassigned": ["Opus: son55's attribute_and_patch_incumbent/H11 is not kept. The complaint → "
                                          "trace triggering rule → conservative replacement step is H01's update edit; "
                                          "H11's decisive gate (separate defect from lapse; re-run and accept only on "
                                          "disjoint validation) is absent."],
                           "revision_proposals": []},
        "pattern_mapping": [
            {"rs_main": "generative_process_redesign", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "abstract_experience_into_guidance", "sub": "H01"},
             "operation_correspondence": "The fixed compression rule set becomes a living store maintained by add "
                                         "(uncovered output), update (conservative variant on complaint), suppress and "
                                         "decay, and is read by later tasks via top-k + LLM selection.",
             "necessary_conditions_and_differences": "H01 asks for an ablation of the edit operations at bounded store "
                                                     "size. Only the w/o-ITRSE/GRPE arms exist, on one model, and the "
                                                     "store is unbounded.",
             "evidence_ids": ["sol:E004", "sol:E005", "sol:E014"]},
            {"rs_main": "self_supervised_signal_engineering", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "crystallize_executable_capability", "sub": "H07"},
             "operation_correspondence": "An uncovered high-volume output (capability gap) triggers LLM generation of an "
                                         "executable regex rule. Its retention and repair are driven by the reward-free "
                                         "complaint signal.",
             "necessary_conditions_and_differences": "H07 wants admission by execution and validation on unseen inputs. "
                                                     "Here admission is usage and complaint statistics, and reuse is "
                                                     "tested only on the evolving benchmark (opus:O01).",
             "evidence_ids": ["son55:E003", "son55:E004", "son55:E020", "opus:O01"]},
        ],
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.19572-1"): "local:2604.19572-5",
                    ("son55", "local:2604.19572-2"): "local:2604.19572-1"},
            overrides={
                "local:2604.19572-1": {
                    "reason": "Opus (both seats unmet): rules evolve over multiple rounds on the evaluated benchmark; k/N "
                              "are chosen on TB 2.0; 'reuse' is re-run on TB 2.0 (opus:O01). Reward-free evolution "
                              "prevents label leakage but is not a task-level holdout.",
                    **merged("son55:local:2604.19572-2 (independent task set, unmet)", ["son55:E007", "son55:E018"])},
                "local:2604.19572-5": {
                    **renum("son55:local:2604.19572-1"),
                    "reason": "Opus (verified son55): no comparison with observation masking, context folding, SWE-Pruner "
                              "or LongCodeZip. Only static rules and LLM summaries."},
            }),
        "claims": lambda c: add_counter(c, "C4", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: Table 3's TB 2.0 baseline for Qwen3-Coder-480B (23.3) differs from Tables 2/4/8 (23.9) (opus:O05).",
            "Opus: the confidence update, τ and round counts are unspecified parameters (opus:O04)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. A concrete bottleneck is quantified (manual extraction "
                   "removes 24.6–44.1% of tokens on 50 TB 2.0 trajectories). The previously fixed object (hand-crafted "
                   "rules or a trained pruner) and the residual (exact-string preservation) are named. Not 4: SWE-Pruner, "
                   "LongCodeZip and masking/folding are discussed but not compared.",
                   ["son55:E002", "son55:E025", "sol:E001", "sol:E010"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Rule representation, Critical bypass, complaint → suppress "
                   "+ conservative variant, confidence × usage ranking and LLM task selection form a reconstructable "
                   "causal account, with distinguishing predictions (static vs evolved; batch size; frozen pool needs "
                   "intra-task evolution). Not 4: the key assumption that complaints catch the critical losses rests on "
                   "a 200-pair judge audit.",
                   ["son55:E004", "son55:E019", "son55:E021", "sol:E002", "sol:E003"]),
            "X": R("resolved", 3, "Opus sides with son55. The operation chain is reconstructable. There is a rule "
                   "schema with real examples (App. L), all LLM prompts (App. N, opus:O03), an explicit information "
                   "boundary for the improver (Table 11, opus:O02), write-back and suppression conditions (Δn≥1 ∧ "
                   "c_r^t≥τ; complaint → c=0 and decay), the ranking formula and a reward-free stopping metric. Not 4: "
                   "τ, the c_r^g/c_r^t update and the round count are unspecified (opus:O04); there is no capacity bound "
                   "or explicit retirement; and the complaint protocol needs a scaffold change (son55:E024). These are "
                   "missing parameters and lifecycle limits, not a missing or contradictory step (EvolveRouter r14b "
                   "convention: unspecified δ → X3).",
                   ["son55:E003", "son55:E004", "son55:E005", "son55:E026", "sol:E005", "opus:O02", "opus:O03",
                    "opus:O04"], ["son55:E024"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. Task success comes from deterministic "
                               "benchmark verifiers, tokens are end-to-end including auxiliary calls, and a 200-pair "
                               "judge audit has manual inspection of all 8 flagged losses. Not 4: the judge is unvalidated, "
                               "and there are reporting inconsistencies (Table 4 vs Table 8 SDs, sol:E018; Table 3 "
                               "baseline 23.3 vs 23.9, opus:O05).",
                               ["son55:E006", "son55:E010", "son55:E017", "son55:E021", "sol:E008", "sol:E018",
                                "opus:O05"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Static controls (200 human rules, static LLM "
                             "rules, LLM summary), w/o-GRPE/ITRSE arms and matched-token-budget curves address 'just "
                             "fewer tokens'. Limits: one model each; human rules sit within SD of TACO; the frozen pool "
                             "alone (w/o ITRSE 38.9) is below the baseline (40.6), so the retained pool carries gains "
                             "only together with intra-task evolution; there are no neighbour compressors and no gate-off "
                             "arm.",
                             ["son55:E012", "son55:E013", "son55:E014", "son55:E023", "sol:E010", "sol:E014"],
                             ["son55:E014"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The information boundary prevents label leakage "
                           "(opus:O02). But the pool evolves over several rounds on the evaluated benchmark, k/N are "
                           "tuned on TB 2.0, the 'reuse' test re-runs TB 2.0 (opus:O01), and rules are instance-specific "
                           "(son55:E020). The selection set serves as the test set.",
                           ["son55:E006", "son55:E007", "son55:E015", "son55:E018", "son55:E020", "sol:E006", "opus:O01"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder). There are five evaluation runs with SD and "
                              "rescued/regressed counts. There are no tests or intervals, gains are often inside the "
                              "baseline SD (MiniMax TB1 +2.95 vs SD 3.94), there is no variance across evolution seeds, "
                              "and the ablation is single-valued.",
                              ["son55:E009", "son55:E013", "son55:E022", "son55:E030", "sol:E015"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. End-to-end tokens include the <2% auxiliary calls, and "
                        "there are matched-budget curves. The multi-round cold-start evolution cost on each benchmark is "
                        "not quantified, beyond the claim that it is 'incurred only once'.",
                        ["son55:E016", "son55:E017", "sol:E009", "sol:E017"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 HTML text with Appendices A–N read. In scope (system_method): a non-weight "
                  "compression rule pool evolves from reward-free interaction feedback, is written back under a gate "
                  "and is reused by later tasks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1 and 3–6 (redundancy, matched-budget curves, convergence, hyperparameters, pass@k) are "
                             "image-only; only text statements and Tables 1–14 are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "The framing move liberates the fixed compression rule set; see rs_pattern.reason.",
                ["sol:E004", "sol:E010", "son55:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["generative_process_redesign", None], ["self_supervised_signal_engineering", None]],
                "sol's primary is kept. son55's complaint-signal card is kept as supporting with sub null (no "
                "retraining, so not C08). heterogeneous_decomposition is dropped.",
                ["sol:E004", "son55:E004", "son55:E006"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H01"], ["crystallize_executable_capability", "H07"],
                 ["evidence_gated_retention", "H30"]],
                "sol's H01 (edit-maintained store) is kept, plus son55's H07 (gap-triggered executable rule) and H30 "
                "(weak: gate + decay). son55's H11 is dropped (no defect/lapse attribution gate, no disjoint-validation "
                "acceptance).", ["sol:E005", "son55:E003", "son55:E004"], NOSCORE),
            XC(p, "local:2604.19572-2", "sol", "partial",
               "A4 hidden collision. sol's local-2 asks whether evolution beats static/local-only compression (partial: "
               "the controls exist on one model each). son55's local-2 is the holdout question, identical to sol's "
               "local-1 and merged there (unmet in both). son55's local-1 moved to local-5.",
               ["sol:E010", "sol:E014", "son55:E007"]),
            XC(p, "local:2604.19572-3", "sol", "partial", "Statistics (sol only). Verified: SDs exist, tests do not.",
               ["sol:E015", "sol:E018"]),
            XC(p, "local:2604.19572-4", "sol", "partial", "Cold-start amortisation cost is not quantified (sol only).",
               ["sol:E013", "sol:E017"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "There is a static-vs-evolved comparison and a module ablation, but on a single model.", ["sol:E010", "sol:E014"]),
            XC(p, "rs:generative_process_redesign/RE-6", "sol", "partial",
               "Matched budgets and negatives are reported, but cold-start cost is not.", ["sol:E009", "sol:E012", "sol:E017"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "partial",
               "Six benchmarks and six models, but each pool evolves on its own benchmark.", ["son55:E008", "son55:E010"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-2", "son55", "partial",
               "There are static and ablation arms, but no equal-evolution-compute alternative.",
               ["son55:E012", "son55:E013", "son55:E023"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-3", "son55", "met",
               "The downstream task success itself is reported side by side.", ["son55:E008", "son55:E010"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "partial",
               "Auxiliary calls are counted; evolution rounds are not.", ["son55:E016", "son55:E017"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial",
               "Pre-evolution on evaluated tasks and the scaffold complaint interface reduce deployment realism.",
               ["son55:E007", "son55:E024"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01", "sol", "partial",
               "Add, update, suppress and decay exist; decay formulas, dedup and bounds do not.", ["sol:E004", "sol:E005"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "partial",
               "Admission is by usage and complaint statistics, not replayed task success.", ["son55:E003"]),
            XC(p, "rsi:crystallize_executable_capability/S3", "son55", "unmet",
               "The abstraction is never checked on inputs outside the evolving benchmark (opus:O01).",
               ["son55:E015", "son55:E020", "opus:O01"]),
            XC(p, "rsi:crystallize_executable_capability/S4", "son55", "met",
               "Repair is driven by an obtainable complaint signal and stays local.", ["son55:E004"]),
            XC(p, "rsi:crystallize_executable_capability/S5", "son55", "partial",
               "w/o GRPE and reuse exist, but the frozen pool alone is below the baseline.", ["son55:E013", "son55:E014"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Rule value is confidence × usage, with no rule-off counterfactual.", ["son55:E003"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "partial",
               "There is a write-back gate and decay, but no hard bound or deletion.", ["son55:E003", "son55:E026"]),
            XC(p, "rsi:evidence_gated_retention/S3", "son55", "partial",
               "Over-compression is named and audited, but there is no ungoverned-accumulation control.", ["son55:E021"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial",
               "Auxiliary overhead is stated; evolution rounds are not.", ["son55:E016", "son55:E017"]),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 3},
                "See ratings.X. The structure and permissions are explicit (opus:O02, O03); the gaps are unspecified "
                "parameters (opus:O04).", ["opus:O02", "opus:O03", "opus:O04", "son55:E026"], "+5.0 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2604.19572-*].id",
             "sol_value": "local-1 = holdout, local-2 = static vs evolved, local-3 = stats, local-4 = cost",
             "son55_value": "local-1 = neighbour compressors, local-2 = holdout",
             "final_value": "local-1 = holdout (merged), local-2 = static vs evolved, local-3 = stats, local-4 = cost, "
                            "local-5 = neighbour compressors",
             "reason": "A4 hidden ID collisions on local-1 and local-2.", "evidence_ids": ["sol:E006", "son55:E025"],
             "score_impact": "none"},
            {"field_path": "E.measurement (reporting)", "sol_value": "Table 4 vs Table 8 SD discrepancy noted",
             "son55_value": "not noted",
             "final_value": "Also Table 3 baseline 23.3 vs 23.9 (opus:O05); recorded under E.measurement without change",
             "reason": "Neither seat noted the Table 3 mismatch. It is 0.6 points and does not alter any conclusion.",
             "evidence_ids": ["opus:O05", "sol:E018"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–4, Tables 1–14 and Appendices E–N first. In scope (rule pool). "
                                                   "Gains of +1–4 points, often within SD. Evolution happens on the "
                                                   "evaluated benchmark, so holdout is weak (task level). Good token "
                                                   "accounting and explicit information boundaries. Initial view: G3 M3 "
                                                   "X3 Em3 Ec2 Eh1 Es2 Ecost2.",
            "integrity_checks": "Both seats a1 on 2604.19572v3, material sha 9451afb6…. Canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Accuracy and token gains are as reported. The 'generalizable rules' claim is not "
                                "supported by same-benchmark reuse (opus:O01). Retained pool alone < baseline.",
            "rating_agreement": "Only X differs (resolved to son55). The seven agreeing items were re-checked and kept.",
        },
    }

    # =========================================================== 2604.19795 Prism (Δ10)
    p = "2604.19795"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "the fraction of retrieved memories drawn from other agents’ contributions",
                    "§5.3 (definition of KR in the r = 0.89 sentence)",
                    "KR is defined as the share of retrieved memories contributed by other agents."),
            opus_ev(p, "O02", "Prism (1) 1 0.31 0.42 35,640 380", "Table 3, 100-City TSP, single-agent Prism row",
                    "Single-agent Prism is reported with KR 0.42 (and 0.38 and 0.35 on circle packing and the kernel). "
                    "With one agent there are no other agents' contributions, so by the paper's own definition (opus:O01, "
                    "O03) KR must be 0. The KR numbers, and the r = 0.89 KR–IR correlation built on them, are internally "
                    "inconsistent.", kind="our_inference"),
            opus_ev(p, "O03", "A KR of 0 means the agent only uses its own memories.", "Appendix B, Definition B.1",
                    "This confirms the definition: KR counts only memories with α(m) ≠ i."),
            opus_ev(p, "O04", "reaching 0.74 at turn 500 compared to 0.42 for single-agent", "§5.5 (Figure 2 text)",
                    "This repeats a non-zero single-agent KR. It also gives 4-agent KR 0.74 against Table 3's 0.71 on "
                    "the same task.", kind="our_inference"),
            opus_ev(p, "O05", "OpenEvolve 1 0.15 — 38,920 500", "Table 3, TSP OpenEvolve row",
                    "Table 4's 'All removed (flat vector, 1 agent)' row (J 67.2, IR 0.15; son55:E014) reproduces exactly "
                    "the Mem0 J (Table 1) and the OpenEvolve IR. The ablation's floor row appears to be copied baseline "
                    "values rather than a run of Prism's own ablated configuration.", kind="our_inference"),
            opus_ev(p, "O06", "nats, λ = 0.01", "§5.1 Setup",
                    "The thresholds are given in nats, while Definition 3.1 uses log2. Definition 3.1 also sums "
                    "−p log p over the realised tokens, which is not the entropy of the memory. The quantity that "
                    "drives tier assignment is ill-defined.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": ["reframe_as_solvable_object"],
            "outside_taxonomy": False,
            "reason": "Opus: the paper names the entropy-gated tri-partite hub (S2) as its 'core architectural "
                      "innovation'. Memories are partitioned by a measured property (token entropy, frequency) and each "
                      "partition gets its own treatment (always loaded, ANN, grep on demand). That is "
                      "heterogeneous_decomposition (sol; sub null, since C04 is model-compression specific). son55's "
                      "reframe_as_solvable_object is kept as supporting, not primary. The paper does recast retrieval "
                      "choice as Hedge, stagnation as quickest detection and confidence as replicator dynamics to borrow "
                      "guarantees, but the correspondence is unproven or wrong (Theorems 3.2/3.3), so the pattern is "
                      "invoked rather than executed (son55 executes_pattern=false).",
            "matches": [smatch("sol", p, "heterogeneous_decomposition"),
                        smatch("son55", p, "reframe_as_solvable_object", role="supporting")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H04",
                                              fit="moderate (tiered hub + causal graph + decay rules is H04's move)"),
                                       dmatch("son55", p, "evidence_gated_retention", "H29")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": pm("sol", p) + pm("son55", p),
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.19795-1"): "local:2604.19795-5",
                    ("son55", "local:2604.19795-2"): "local:2604.19795-6"},
            overrides={
                "local:2604.19795-2": {
                    "status": "unmet",
                    "reason": "Opus (revised from sol partial): J's judge configuration and the provenance of the baseline "
                              "values are unstated; IR has no formula; KR's single-agent values contradict its definition "
                              "(opus:O02, O03); the ablation floor row copies baseline numbers (opus:O05). The measurements "
                              "cannot carry the capability conclusions.",
                    "evidence_ids": ["sol:E004", "sol:E009", "sol:E010", "opus:O02", "opus:O03", "opus:O05"]},
                "local:2604.19795-5": {**renum("son55:local:2604.19795-1"),
                                       "reason": "Opus (verified son55): no seeds, runs, variance or n for the reported "
                                                 "correlations."},
                "local:2604.19795-6": {**renum("son55:local:2604.19795-2"),
                                       "reason": "Opus (verified son55): no multi-agent-without-shared-memory or "
                                                 "budget-matched parallel single-agent control."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O02", "opus:O03", "opus:O04"]),
                                        "C1", ["opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: single-agent KR values (0.42/0.38/0.35) contradict KR's definition, which forces 0 for one agent "
            "(opus:O01–O04). The 'knowledge, not compute' correlation is internally inconsistent.",
            "Opus: Table 4's all-removed row equals Mem0 J and OpenEvolve IR exactly (opus:O05).",
            "Sub-claims refuted: Theorem 3.2's bound exceeds |M| when n·k > |M| (sol:E013), and Pinsker is used backwards "
            "(sol:E014, son55:E004)."],
            claim_support_note="unsupported (son55). The headline empirical claims (LOCOMO J 88.1, 2.8× IR) are "
                               "unsupported for lack of protocol, variance and controls, not refuted. Specific sub-claims "
                               "are contradicted: the coverage guarantee (Theorem 3.2) and the KR mechanism evidence. "
                               "sol's 'contradicted' is recorded as applying to those sub-claims."),
        "ratings": {
            "G": R("resolved", 1, "Opus sides with son55. The 'gap' is a union of features each neighbour lacks (single-"
                   "agent only, no evolutionary dynamics, 'lacks formal memory architecture'). No neighbour is shown to "
                   "fail on any task because of the missing piece. Coral, the nearest neighbour, is never compared "
                   "(son55:E018), and LOCOMO is single-conversation, so the multi-agent motivation does not bind there. "
                   "Not 0: the neighbours and the changed non-weight objects (tiering, confidence dynamics, retrieval "
                   "strategy) are named.",
                   ["son55:E018", "sol:E001", "sol:E003"]),
            "M": R("resolved", 1, "Both seats 1; re-checked. The links from mechanism to problem are analogies (entropy ↔ "
                   "reusability, confidence plateau ↔ task stagnation). The formal justifications fail: Theorem 3.2's "
                   "bound can exceed |M| and uses Pinsker in the wrong direction (sol:E013, E014). The Theorem 3.3 "
                   "Lyapunov step treats +λV as decreasing V (son55:E005). Theorems 3.5/3.6 are textbook bounds whose "
                   "premises (bounded reward, geometric onset) are not shown.",
                   ["sol:E013", "sol:E014", "sol:E015", "son55:E002", "son55:E004", "son55:E005", "son55:E019",
                    "son55:E020"]),
            "X": R("resolved", 1, "Opus sides with son55. Pseudo-code and a few hyperparameters exist, but the loop's "
                   "load-bearing quantities are undefined or contradictory: the 'positive evaluation' that sets fitness "
                   "(son55:E003); IR (son55:E009); how EVOI is estimated; how agents generate candidates in the "
                   "optimisation tasks; and token entropy, defined with log2 but thresholded in nats over realised "
                   "tokens (opus:O06). Writes are LLM-decided with no external gate. Per the anchor, key conditions "
                   "missing or contradictory gives 0–1; 1 because the store operations are specified.",
                   ["son55:E003", "son55:E009", "son55:E022", "sol:E002", "sol:E006", "opus:O06"]),
            "E.measurement": R("resolved", 1, "Both seats 1; re-checked, with an Opus addition. The LOCOMO judge setup and "
                               "baseline provenance are unstated, and Claude Code memory is 'simulated' (son55:E017). IR "
                               "is undefined. KR's single-agent values contradict its definition (opus:O02, O03). Table "
                               "4's floor row copies the baselines (opus:O05).",
                               ["son55:E006", "son55:E007", "son55:E009", "son55:E017", "opus:O02", "opus:O03",
                                "opus:O05"]),
            "E.causality": R("resolved", 1, "Both seats 1; re-checked. There is a single-run component ablation table, "
                             "but its all-removed row reproduces baseline values (opus:O05). There is no memory-off arm "
                             "on the optimisation tasks, and 4 vs 1 agents run at unmatched evaluations. The KR–IR "
                             "correlation is both observational and inconsistent (opus:O02).",
                             ["son55:E010", "son55:E011", "son55:E012", "son55:E014", "son55:E015", "opus:O02",
                              "opus:O05"]),
            "E.holdout": R("not_reported", 0, "Both seats not_reported 0; re-checked. No build/test separation and no "
                           "unseen-task result. τ and λ/μ are chosen by sweeping the reported LOCOMO J and TSP IR (App. "
                           "C).", ["son55:E016", "sol:E016"],
                           scope=["full text §1–7, Tables 1–6, Figs 2–3 captions, Appendices A–C (Opus re-read)"]),
            "E.statistics": R("not_reported", 0, "Opus sides with son55. There are no seeds, run counts, SDs, intervals "
                              "or tests for any reported J/F1/IR value. The only statistics are r = 0.89 / 0.91 "
                              "correlations with p < 0.01 and no n, for a secondary analysis whose KR values are "
                              "themselves inconsistent (opus:O02). Evaluation counts are budgets, not sample sizes. A2 "
                              "ladder: the statistics for the claims are absent after a full search.",
                              ["son55:E015", "opus:O02"],
                              scope=["full text §5, Tables 1–6, Figs 2–3 text, Appendices A–C (Opus re-read)"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. p95 latency, 'savings' and per-run evaluation counts are "
                        "given. Extraction, causal-edge, consolidation and reflection LLM calls are uncounted, and 4- vs "
                        "1-agent budgets are unmatched.", ["son55:E010", "son55:E022", "sol:E009"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text with Appendices A–C read. In scope (system_method): a shared non-weight "
                  "memory with outcome-driven confidence evolution, consolidation and retrieval-strategy weights. All "
                  "eight items resolved; the low score reflects the evidence, not a scope ruling.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree; A1 does not apply because experiments are reported)",
        "figure_dependence": "Figs 2–3 render only as axis ticks; only text-stated values (0.74/0.42, r = 0.91) are used.",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", "unsupported",
                "The headline empirical claims lack protocol, variance and controls (unsupported). sol's contradicted "
                "applies to sub-claims (Theorem 3.2's counterexample; KR inconsistency) and is preserved in "
                "claim_support_note. No compromise label is used.",
                ["sol:E013", "son55:E006", "son55:E015", "opus:O02"], "none (claim_support is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "heterogeneous_decomposition",
                "The core innovation named by the paper is entropy-based partition with differentiated access.",
                ["sol:E003", "son55:E002"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["heterogeneous_decomposition", None], ["reframe_as_solvable_object", None]],
                "sol's partition card is primary; son55's reframing card is supporting (invoked, correspondence unproven).",
                ["sol:E003", "son55:E004", "son55:E020"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H01"], ["evidence_gated_retention", "H29"],
                 ["index_experience_for_reuse", "H04"]],
                "H01 (ADD/UPDATE/DELETE/NOOP + AutoDream) is agreed. The tiered hub, causal graph and decay rules are "
                "H04's substrate restructuring. Retrieval-success fitness driving confidence is H29's utility valuation, "
                "without a counterfactual.", ["son55:E002", "son55:E003", "sol:E002"], NOSCORE),
            XC(p, "local:2604.19795-2", "revised", "unmet",
               "A4 hidden collision. sol's local-2 (do J/IR/KR support capability conclusions) is kept, revised to unmet "
               "by the KR contradiction and the copied ablation row (opus:O02, O05). son55's local-2 (multi-agent gain "
               "attributed to memory) moved to local-6 (unmet). son55's local-1 moved to local-5.",
               ["opus:O02", "opus:O05", "sol:E010"]),
            XC(p, "local:2604.19795-3", "sol", "unmet", "Verified: no frozen-store unseen-task evaluation.",
               ["sol:E008", "sol:E016"]),
            XC(p, "local:2604.19795-4", "sol", "partial", "Cost and latency fragments exist; variance does not.",
               ["sol:E009", "sol:E010"]),
            XC(p, "rs:heterogeneous_decomposition/RE-4", "sol", "partial",
               "A flat-tier ablation exists, but single-run and with no matched-capacity control.", ["sol:E012"]),
            XC(p, "rs:heterogeneous_decomposition/RE-5", "sol", "unmet",
               "The entropy–reusability heterogeneity is posited, not measured.", ["sol:E003", "sol:E016"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "son55", "unmet",
               "The reductions are asserted. Theorem 3.2 is false as stated and the Theorem 3.3 proof is flawed.",
               ["son55:E004", "son55:E005", "sol:E013"]),
            XC(p, "rs:reframe_as_solvable_object/RE-2", "son55", "unmet",
               "Fitness's 'positive evaluation' and IR are not formally defined.", ["son55:E003", "son55:E009"]),
            XC(p, "rs:reframe_as_solvable_object/RE-3", "son55", "partial",
               "Hedge, CUSUM and replicator dynamics are reused machinery attached to memory subsystems.",
               ["son55:E019", "son55:E020"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "unmet",
               "No intervention validates entropy ↔ reusability, plateau ↔ stagnation or ESMS ↔ a better store.",
               ["son55:E002", "son55:E019"]),
            XC(p, "rsi:abstract_experience_into_guidance/H01", "sol", "partial",
               "Edit operations and pruning are designed, but curator reliability is untested.", ["sol:E002", "sol:E006"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "partial",
               "Decay, MI pruning and consolidation are specified, but their effects are unmeasured.",
               ["son55:E016", "son55:E022"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "Writes are LLM-decided, with no execution or external gate.", ["son55:E022"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Fitness is retrieval-success share, with no memory-on/off counterfactual.", ["son55:E003"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "partial",
               "There is a replicator-off ablation row, single-run.", ["son55:E012"]),
            XC(p, "rsi:index_experience_for_reuse/F6", "son55", "partial",
               "A new store shape stands in for much of the argument, with an ablation attempt.",
               ["son55:E012", "son55:E013"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "unmet",
               "There is no whole-store-off arm; the floor row copies Mem0 (opus:O05).", ["son55:E014", "opus:O05"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.G. The gap is a feature union with no demonstrated failure of any neighbour.",
                ["son55:E018"], "−3.75 vs sol"),
            res("ratings.X", *C(p, "ratings.X"), "son55", {"status": "resolved", "rating": 1},
                "See ratings.X. The fitness signal, IR, EVOI and entropy are undefined or contradictory (opus:O06).",
                ["son55:E003", "son55:E009", "opus:O06"], "−5.0 vs sol"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "son55",
                {"status": "not_reported", "rating": 0},
                "See ratings.E.statistics. The applicable statistics are absent. The lone correlation p-values have no "
                "n and rest on inconsistent KR values.", ["son55:E015", "opus:O02"], "−1.25 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "E.measurement / E.causality (KR evidence)",
             "sol_value": "KR read as a valid cross-agent reuse share", "son55_value": "KR read as a valid observational share",
             "final_value": "Single-agent KR > 0 contradicts its definition (opus:O02–O04)",
             "reason": "Neither seat checked KR against Definition B.1. The ratings were already 1, so this strengthens "
                       "the reasons without changing them.", "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"],
             "score_impact": "none"},
            {"field_path": "expectations[local:2604.19795-*].id",
             "sol_value": "local-1 = formal guarantees, local-2 = measurement, local-3 = holdout, local-4 = stats/cost",
             "son55_value": "local-1 = statistics, local-2 = multi-agent attribution",
             "final_value": "sol's local-1..4 kept; son55's local-1 → local-5, local-2 → local-6",
             "reason": "A4 hidden ID collisions on local-1 and local-2.", "evidence_ids": ["sol:E013", "son55:E015"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole paper (§1–7, Tables 1–6, Appendices A–C) first. Single "
                                                   "runs, no protocol, hyperparameters swept on the test metrics, "
                                                   "theorems with wrong steps, single-agent KR > 0 against its definition, "
                                                   "and the ablation floor equal to the baselines. Initial view: G1 M1 X1 "
                                                   "Em1 Ec1 Eh0 Es0 Ecost1.",
            "integrity_checks": "Both seats a1 on 2604.19795v1, material sha 68e3a23e…. Canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Headline claims are unsupported. The coverage theorem is refuted (sol:E013). The KR "
                                "mechanism evidence is inconsistent (opus:O02).",
            "rating_agreement": "G/X/E.statistics are resolved to son55. The five agreeing items were re-checked and kept.",
        },
    }

    # =========================================================== 2604.19837 Forage V2 (Δ7.5)
    p = "2604.19837"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Scope: product_catalog_collection Source run: NVIDIA Sonnet seeded run_005",
                    "Appendix B.4 (entry three_round_completion_at_266_confirmed_again_v2)",
                    "Seeded Sonnet runs write entries into the knowledge base that later seeded runs read. This entry, "
                    "from run_005, records the 266 figure."),
            opus_ev(p, "O02", "Sonnet cold runs produce 60 knowledge entries across six runs; Sonnet seeded runs produce "
                              "106.", "§6.2 Bidirectional transfer",
                    "The seeded condition keeps accumulating, so seeded runs 004–006 are sequentially dependent through "
                    "the shared base.", kind="our_inference"),
            opus_ev(p, "O03", "Three independent runs, each starting from scratch (no shared session state), arrive at "
                              "identical denominator estimates because the accumulated knowledge encodes a consistent "
                              "product definition.", "§5.3 Denominator variance",
                    "This is the paper's independence claim for the '266 convergence'. It is contradicted by O01/O02 and "
                    "by run_006's own statement citing prior-run entries (son55:E013): the runs share an evolving base "
                    "that states 266, so identical denominators are expected under anchoring.", kind="our_inference"),
            opus_ev(p, "O04", "NVIDIA Opus $5.05 $4.36–5.72 $0.60", "§5.5 Table 10",
                    "Opus arithmetic: building the base took six Opus runs ≈ 6 × $5.05 = $30.30. Over six runs, seeded "
                    "Sonnet costs ≈ 6 × $5.13 + $30.30 = $61.1 against cold Sonnet's 6 × $9.40 = $56.4. The 'halves cost' "
                    "claim holds only per run after a free, pre-built base.", kind="our_inference"),
            opus_ev(p, "O05", "while Forage’s method isolation ensures that knowledge is extracted through independently "
                              "evaluated outcomes", "§7.3 Hermes and MemRL",
                    "This is the mechanism claim that stored knowledge is validated. In fact post-mortem lessons are "
                    "appended with no gate (§3.1), and the breach incident shows unvalidated lessons entering and "
                    "propagating (son55:E020).", kind="our_inference"),
            opus_ev(p, "O06", "converges in half the rounds (mean 4.5 vs. 7.0)", "Abstract",
                    "4.5/7.0 = 0.64, a 36% reduction, not half (also sol:E019).", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["decompose_and_delegate"],
            "outside_taxonomy": False,
            "reason": "Opus: V2's two claims, accumulation and transfer, both work by injecting the accumulated lesson "
                      "base (INDEX.md) as conditioning into fresh sessions and a weaker model, with no parameter update. "
                      "That is adapt_via_conditioning (sol; sub null, because C03's broad schema and category holdout are "
                      "not executed). son55's decompose_and_delegate/C25 is the Evaluator/Planner split with "
                      "machine-checked eval.py/action.py run by a deterministic Executor. It is inherited from V1 and "
                      "kept as supporting, not primary, because V2's contribution and evidence concern the knowledge "
                      "layer.",
            "matches": [smatch("sol", p, "adapt_via_conditioning"),
                        smatch("son55", p, "decompose_and_delegate", role="supporting")],
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "coevolve_the_evaluator", "H25",
                                              fit="weak-moderate (isolated evaluator revises eval.py/denominator; no "
                                                  "trusted-anchor acceptance test)")],
                           "unassigned": ["Opus: son55's diagnose_self_improvement/H35 is not kept. The contamination "
                                          "incident is an accidental, unquantified case report, not a designed "
                                          "persistence audit with paired conditions."] +
                                         prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]["unassigned"]), "sol")[:1],
                           "revision_proposals": []},
        "pattern_mapping": [pm("sol", p)[0], pm("son55", p)[0]],
        "expectations": lambda sol, son, p=p: merge_exps(
            p, sol, son,
            rename={("son55", "local:2604.19837-2"): "local:2604.19837-5"},
            overrides={
                "rs:adapt_via_conditioning/RE-2": {
                    "status": "unmet",
                    "reason": "Opus (son55): the base is built on, and evaluated on, the same task instance, and it "
                              "carries instance-level answers (the curated product lists in B.2, the 266 figure in B.4). "
                              "No leakage or overlap analysis accompanies the '266 calibrates evaluation' "
                              "interpretation.",
                    "evidence_ids": ["sol:E015", "sol:E017", "son55:E013", "son55:E014", "son55:E016", "opus:O01"]},
                "local:2604.19837-1": {"note": "Same question and status in both seats (self-referential coverage "
                                               "metric); merged."},
                "local:2604.19837-5": {**renum("son55:local:2604.19837-2"),
                                       "reason": "Opus (verified son55): the number of breached and excluded runs and the "
                                                 "re-run rule are not reported."},
            }),
        "claims": lambda c: add_counter(add_counter(add_counter(c, "C2", ["opus:O01", "opus:O02", "opus:O03", "opus:O04",
                                                                           "opus:O06"]),
                                                    "C3", ["opus:O05"]), "C1", []),
        "assessment": assess("son55", p, [
            "Opus: the seeded condition appends to the base that later seeded runs read (opus:O01, O02), so the "
            "'independent' 266 convergence (opus:O03) is sequential anchoring.",
            "Opus: counting the six Opus runs that built the base (≈$30.30), seeded Sonnet does not save money over six "
            "runs (opus:O04).",
            "Opus: 'half the rounds' is a 36% reduction (opus:O06)."],
            evidence_level="task",
            evidence_level_note="task (sol). The base is built from, and evaluated on, the same static task instance. "
                                "It encodes instance-specific answers. Opus's own six-run accumulation shows no round or "
                                "coverage trend. The cold/seeded contrast shows the base changes behaviour on re-runs of "
                                "that instance, not a retained improvement on later tasks (EVIDENCE rule 2 spirit; TACO "
                                "convention in this batch)."),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The V2 gaps (no cross-run experience, no transfer, fragile "
                   "isolation) are real but generic. The cross-episode reflective-memory neighbours (Reflexion/ExpeL "
                   "type) are not engaged (son55:E030). The premise that accumulation helps is not borne out by the "
                   "paper's own Opus series (constant 4 rounds, 100% from run 001; son55:E006, E007). The most specific "
                   "new finding, knowledge contamination, is a case report.",
                   ["son55:E006", "son55:E007", "son55:E025", "son55:E030", "sol:E013"], ["son55:E020"]),
            "M": R("resolved", 2, "Opus sides with son55. Role-isolated post-mortem, append-only advisory lessons and "
                   "prompt injection form a coherent story, with a distinguishing prediction (exploration gap vs "
                   "reasoning gap; transfer helps survival but not the reasoning ceiling on Q6). But the load-bearing "
                   "claim that stored knowledge is 'extracted through independently evaluated outcomes' (opus:O05) does "
                   "not match the mechanism: lessons are appended with no validation gate, and contamination did "
                   "propagate. The 'calibrates evaluation' account is confounded by anchoring (opus:O03).",
                   ["son55:E013", "son55:E020", "son55:E027", "sol:E001", "sol:E003", "opus:O03", "opus:O05"]),
            "X": R("resolved", 2, "Both seats 2; re-checked. Schema, isolated post-mortem, append-only versioning, INDEX "
                   "injection, transfer protocol, physical isolation and recovery are described. There is no write gate; "
                   "curation, conflict handling, retirement and capacity are deferred to V3; INDEX injection is "
                   "unbounded; and prompts and implementation live only in the codebase.",
                   ["son55:E002", "son55:E003", "son55:E004", "sol:E002", "sol:E006", "sol:E007"]),
            "E.measurement": R("resolved", 1, "Both seats 1; re-checked. The main metric, coverage, is relative to each "
                               "run's self-chosen denominator (the authors concede it is not comparable across runs). "
                               "V2 drops V1's external recall. Q10 has no correctness check. Cost and rounds are "
                               "reliable but secondary.",
                               ["son55:E018", "son55:E019", "son55:E029", "sol:E016"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-model cold vs seeded Sonnet on the same task "
                             "and runtime is a real store on/off control, and it supports the headline transfer claim "
                             "for cost and rounds. Not 3: the seeded base contains instance answers and the 266 anchor "
                             "(opus:O01, O03); there is no unrelated-knowledge, strategy-only or Sonnet-self-accumulated "
                             "arm; the accumulation claim has no control and no trend; and isolation and co-evolution "
                             "are not ablated in V2. Kept above ErrorProbe's 1 because here the headline claim itself "
                             "has the isolating control.",
                             ["son55:E011", "son55:E013", "son55:E016", "son55:E017", "sol:E008", "sol:E009", "opus:O03"],
                             ["son55:E006"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. The base is built on the same task it is tested on; "
                           "cross-task transfer is explicitly not claimed; there is one static instance per task type; and "
                           "the base carries answer-like content (son55:E016, opus:O01).",
                           ["son55:E016", "son55:E021", "son55:E025", "son55:E026", "sol:E015", "sol:E017", "opus:O01"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 ladder). Six runs per condition with full per-run tables, "
                              "cost SDs and full failure denominators (Q6 survival, Q10 planner timeouts). There are no "
                              "tests or intervals, the Q6 survival conclusion turns on one run, the excluded breached "
                              "runs are uncounted, and the seeded runs are not independent replicates (opus:O02).",
                              ["son55:E011", "son55:E021", "son55:E022", "son55:E023", "sol:E012", "opus:O02"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Per-run API cost (mean, range, SD), rounds, fixed budget "
                        "parameters and the plugin overhead are disclosed. But the headline 'halves cost' omits the cost "
                        "of building the base. Over the reported six runs, seeded Sonnet plus the ≈$30.30 Opus build costs "
                        "more than cold Sonnet (≈$61.1 vs ≈$56.4; opus:O04), and no break-even or amortisation is "
                        "analysed. An unaccounted search or build cost that reverses the stated saving caps this at 2.",
                        ["son55:E024", "son55:E032", "sol:E014", "opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text with Appendices A–B read. In scope (system_method): post-mortem lessons "
                  "are written to a persistent non-weight knowledge base and injected into later runs and other "
                  "models. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figs 1–5 are image-only; only Tables 1–10 and text values are used.",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "The base is built on and evaluated on the same static task instance and carries instance answers. "
                "Cold vs seeded shows behaviour change on re-runs of that instance. Opus's own accumulation shows no "
                "improvement. This does not reach 'retained' on later tasks (EVIDENCE rule 2 spirit; consistent with "
                "TACO in this batch).", ["son55:E006", "son55:E016", "sol:E015", "opus:O01"],
                "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "adapt_via_conditioning",
                "V2's contribution and evidence are the conditioning knowledge layer; the V1 role split is inherited.",
                ["sol:E003", "sol:E004", "son55:E004"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["adapt_via_conditioning", None], ["decompose_and_delegate", "C25"]],
                "sol's conditioning card is primary; son55's C25 role split (machine-checked scripts, deterministic "
                "Executor) is supporting.", ["sol:E003", "son55:E019", "son55:E027"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H00"], ["coevolve_the_evaluator", "H25"]],
                "H00 is agreed. son55's H25 is kept at weak-moderate: the isolated Evaluator revises eval.py and the "
                "denominator across runs (Q10 rigor evolution), with no trusted-anchor acceptance. son55's H35 is "
                "dropped: an accidental case report, not a persistence audit.",
                ["son55:E018", "son55:E020", "son55:E031"], NOSCORE),
            XC(p, "local:2604.19837-2", "sol", "partial",
               "A4 hidden collision. sol's local-2 (high-difficulty transfer statistics) is kept as partial. son55's "
               "local-2 (excluded breached runs) is a different question, moved to local-5 (unmet, verified).",
               ["sol:E011", "sol:E012", "son55:E021"]),
            XC(p, "local:2604.19837-3", "sol", "partial", "The base build cost is not netted (opus:O04).",
               ["sol:E014", "opus:O04"]),
            XC(p, "local:2604.19837-4", "sol", "partial",
               "A real breach case and a new isolation description; shared-lesson anchoring remains.",
               ["sol:E006", "sol:E013", "sol:E018"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "sol", "partial",
               "Same-model store on/off exists; there is no equal-information alternative conditioning.",
               ["sol:E008", "sol:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "The base carries instance answers and the 266 anchor, and no overlap or leakage analysis is reported.",
               ["son55:E013", "son55:E014", "son55:E016", "opus:O01"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "No cheaper or alternative conditioning control (strategy-only, unrelated, self-accumulated).",
               ["son55:E011", "son55:E026"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "Per-run cost is reported; the base build cost is not.", ["son55:E024", "son55:E032", "opus:O04"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "unmet",
               "No V2 ablation of isolation, co-evolution or the self-audit checklist.", ["son55:E019", "son55:E031"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "Three task types, one static instance each.", ["son55:E022", "son55:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/H00", "sol", "partial",
               "The append/read chain is clear and has a store-off contrast. Cross-task transfer and the full budget are "
               "missing.", ["sol:E001", "sol:E003", "sol:E008"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
               "Lessons follow from runs with an isolated evaluator, but entries themselves are unvalidated (opus:O05).",
               ["son55:E020", "son55:E027", "opus:O05"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Append-only, with curation deferred to V3.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "unmet",
               "No retention gate; all lessons are written.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:coevolve_the_evaluator/F4", "son55", "partial",
               "The evaluator changes per run without an external certificate.", ["son55:E018", "son55:E029"]),
            XC(p, "rsi:coevolve_the_evaluator/S2", "son55", "partial",
               "The anchor is isolated by design; V2 validity is cited from V1 and was breached once in development.",
               ["son55:E019", "son55:E020"]),
            XC(p, "rsi:diagnose_self_improvement/S6", "son55", "partial",
               "Kept as a check question even though H35 is dropped: the cold/seeded cut isolates the base but mixes in "
               "answer content and the 266 anchor.", ["son55:E011", "son55:E013", "son55:E016"]),
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.G. The gap is generic, reflective-memory neighbours are absent, and the paper's own Opus "
                "series undercuts the accumulation premise.", ["son55:E006", "son55:E030"], "−3.75 vs sol"),
            res("ratings.M", *C(p, "ratings.M"), "son55", {"status": "resolved", "rating": 2},
                "See ratings.M. The validated-knowledge premise is contradicted by the ungated append and the "
                "contamination case (opus:O05).", ["son55:E020", "opus:O05"], "−5.0 vs sol"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "resolved", "rating": 2},
                "See ratings.E.cost. Omitting the build cost reverses the headline saving over six runs (opus:O04).",
                ["opus:O04", "sol:E014"], "−1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "claims[C2] (independence of the 266 convergence)",
             "sol_value": "noted that run_006 relies on prior knowledge",
             "son55_value": "noted that run_006 reads 266 from the knowledge base",
             "final_value": "The seeded condition appends to the base read by later seeded runs (opus:O01, O02); the "
                            "'independent runs' statement (opus:O03) is contradicted.",
             "reason": "Both seats saw anchoring at run_006 but not the mechanism: the seeded runs form one evolving "
                       "lineage. This strengthens the E.causality, E.statistics and evidence_level reasons without "
                       "changing ratings.", "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"],
             "score_impact": "none"},
            {"field_path": "expectations[local:2604.19837-2].id",
             "sol_value": "local-2 = high-difficulty transfer statistics", "son55_value": "local-2 = excluded breached runs",
             "final_value": "local-2 = sol's; son55's → local-5",
             "reason": "A4 hidden ID collision.", "evidence_ids": ["sol:E012", "son55:E021"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole paper including Appendix B first. In scope (lesson "
                                                   "base). Coverage is self-referential. Opus accumulation shows no "
                                                   "trend. The cold vs seeded transfer is the one real control. The base "
                                                   "carries instance answers. The seeded runs accumulate, so 266 is "
                                                   "anchored. The cost claim omits the build cost. Initial view: G2 M2 X2 "
                                                   "Em1 Ec2 Eh1 Es2 Ecost2.",
            "integrity_checks": "Both seats a1 on 2604.19837v1, material sha a5b3cfaf…. Canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Transfer gains in cost and rounds are as reported, per run. The calibration claim is "
                                "confounded by anchoring. The accumulation claim is not supported by the Opus series.",
            "rating_agreement": "G/M are resolved to son55 and E.cost to sol. The five agreeing items were re-checked "
                                "and kept.",
        },
    }
    return S
