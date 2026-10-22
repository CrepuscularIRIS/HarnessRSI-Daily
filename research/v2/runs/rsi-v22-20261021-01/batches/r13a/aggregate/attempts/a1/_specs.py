"""Opus rulings for r13a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2603.05860 MACRO (both seats 42.5): final 42.5, all eight ratings re-derived from the text and kept. Two "
        "findings neither seat recorded are filed as shared corrections without a rating change. (1) X: a composite "
        "is defined two ways, as an action in a growing action space (§3.1) and, in the reward (Eq. 9), as a "
        "contiguous run of atomic tool names inside one step. The paper never says how a composite is shown to or "
        "executed by the policy at inference, including Table 3 row C (no GRPO), the row with the largest gain. "
        "That is anchor 2, as for r12b ARISE. (2) The 'three conditions' ablation lists four rows, and 'recall' is "
        "claimed but never reported. Both are text slips that do not touch the metric; the RAM-W600 row recomputes "
        "exactly. evidence_level stays task (both seats): retained would need a stated build/test split, and "
        "REFUGE2/MITEA splits are not described. RS → sol (generative_process_redesign primary for the growing action "
        "space, C03 supporting). self_supervised_signal_engineering is rejected because ground-truth labels gate every "
        "write. Domain → sol (H08 promotion-by-recurrence, H03, H28).",
        "2603.09206 MM-Zero: out_of_scope confirmed independently (A3). Proposer, Coder and Solver all start from one "
        "base model, and each is GRPO-trained with full fine-tuning ('LoRA rank 0; the vision tower is trainable'). "
        "The SVG code and rendered images are per-round training data, not a retained tool or skill read at test "
        "time. Identification follows the run convention for proposer–solver co-training (C08 + H22). evidence_level "
        "and claim_support are null, the canonical out_of_scope value. Both seats wrote evidence_level 'task'; that "
        "is filed as a shared correction.",
        "2603.09716 AutoAgent (seat Δ2.5): final 30.0, below both seats (33.75 / 36.25). X → sol 1: the evolution "
        "loop is prose only (selector 'a learned or heuristic module', validation 'e.g., for consistency', "
        "'periodically'), and the experiments never say whether cognition evolves during the main runs. "
        "E.causality → son55 1: two of four announced ablations are missing, and the only evolved-cognition test is "
        "a synthetic 50-question perturbation. E.cost → sol 0: the step and token caps are design parameters, not "
        "cost evidence. The promised 'step efficiency' metric is never reported, and the analyzer/EMO calls sit "
        "outside the step cap (precedents r02a 2410.08197, r04a 2504.00587). RS → sol (generative_process_redesign + "
        "heterogeneous_decomposition). son55's outside_taxonomy is rejected: the run uses generative_process_redesign "
        "for papers that turn a fixed agent artifact into an editable one. Shared measurement finding (no rating "
        "change): besides the seats' 48.5/15.2 text–table mismatches, the text also says 2Wiki is state of the art "
        "'under both evaluation metrics', but IRCoT has higher accuracy (0.492 vs 0.466) and Self-Ask a higher "
        "LLM-judge score (0.478 vs 0.474). It also says HLE is best on Qwen3-30B-A3B, but DeepAgent scores 7.2 to "
        "AutoAgent's 6.2.",
        "2603.13131 MineEvolve (seat Δ2.5): final 68.75. E.holdout → son55 2. The Table 6 'held-out hard tasks' are "
        "weighted with group sizes 16/6/7/13, i.e. all 42 hard tasks of the suite, and the accumulation episodes' "
        "source is unstated. Diamond-only self-learning trains and tests on the same seven tasks. Only Curriculum "
        "Pretrain→Freeze (lower tiers → Diamond) is a clean group-level transfer. The main table's knowledge-base "
        "state is also unstated, and 'Static Store' is the frozen variant, which implies the full system keeps "
        "updating during evaluation. Domain → H00 + H01. H30 is rejected: admission checks only, with no retirement "
        "or marginal-gain test; its S1/S2 stay as check questions. RS → sol (C03 + heterogeneous_decomposition for "
        "the skill/remedy split with its own ablation). The Figure 4 component-ablation values are image-only and "
        "are used only as described in the text; Figure 5's values are in Table 6.",
        "2603.13258 MemCoder (seat Δ5): final 50.0. M → son55 2: the tested chain is commit-history retrieval plus a "
        "refining sub-agent. The write-back that defines the claimed co-evolution is a bare set union after an "
        "unspecified human review, never exercised. Shared correction: evidence_level retained → task. At evaluation "
        "the memory holds only LLM-structured human commits made before each issue. No agent-produced, human-"
        "validated entry is ever written and then reused, so the store is not a retained self-change. The gains "
        "rest on a non-weight retrieval component, which keeps the paper in scope as B-class. E.holdout stays 2. "
        "Opus adds that the default initial top-k=8 sits at the knee of a sweep run on a 200-issue subset of the "
        "test set (r12b ARISE precedent).",
        "A4 hygiene: hidden local-ID collisions (the same local:<key>-n used for different questions) were renumbered "
        "in 2603.05860, 2603.09206, 2603.09716, 2603.13131 and 2603.13258. Same-question pairs under different IDs "
        "were merged (AutoAgent sol local-1 / son55 local-3; MineEvolve sol local-2 / son55 local-1).",
        "Figure dependence: MACRO Fig. 3, MineEvolve Fig. 4, MemCoder Figs. 3–5 and the MM-Zero Fig. 2 curves are "
        "image-only. No figure value was invented, and ratings rely on captions, body text and tables.",
        "No material requests: every disputed field could be answered from the pinned texts. Both seats asked for "
        "nearest-neighbour full texts (Biomni/EvolveR, Reflexion/Voyager, XENON, A-mem). These do not block any "
        "rating, because G already records the uncompared neighbours.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    NOLVL = "none (evidence_level is not scored)"
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

    def dmatch(s, p, main, seat_sub, **upd):
        for m in seat(s, p)["domain_pattern"]["matches"]:
            if m["main"] == main and m.get("sub") == seat_sub:
                m2 = prefix(copy.deepcopy(m), s)
                m2.update(upd)
                return m2
        raise KeyError((s, p, main, seat_sub))

    def pmap(s, p, idx, **upd):
        m = prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][idx]), s)
        m.update(upd)
        return m

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def kept(s, p, k, reason, ev, cev=()):
        """Rating both seats agree on; Opus re-checked and writes its own reason."""
        r = seat(s, p)["ratings"][k]
        return R(r["status"], r["rating"], reason, ev, cev, r.get("search_scope") or ())

    # =========================================================== 2603.05860 MACRO (both 42.5)
    p = "2603.05860"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "we parse the action to extract the sequence of tool names invoked within that step (if any).",
                    "§3.4 Reward Function (Eq. 9)",
                    "In the reward, a composite counts as 'used' when its atomic tool names occur contiguously inside one "
                    "step. Composite use is thus defined over atomic calls, not over a callable composite action."),
            opus_ev(p, "O02", "is a dynamically growing set of composite tools (multi-step procedures discovered during training; see §",
                    "§3.1 Action space with evolving abstractions",
                    "Here a composite is a member of the action space A_t = T ∪ C_t ∪ {answer}. The paper never states how "
                    "a composite is presented to the policy or expanded at execution, so O01 and O02 give two "
                    "unreconciled definitions. Table 3 row C (composites, no GRPO) has no described channel through "
                    "which the registry acts at inference.", kind="our_inference"),
            opus_ev(p, "O03", "We design an ablation study comprising three conditions to evaluate the contribution of each core component",
                    "§4.3 Effectiveness of the Proposed Key Components",
                    "Four conditions (A–D) follow. The text also says memory 'improves recall', but no recall figure is "
                    "reported in Tables 1–3. These are text slips, not metric defects."),
            opus_ev(p, "O04", "MACRO (Ours) 61.75 30.00 90.01 28.50 95.00 31.61", "Table 2 (RAM-W600 test)",
                    "Opus recomputation. BACC = (SEN+SPC)/2 = (28.50+95.00)/2 = 61.75, and F1 = 2·PRE·SEN/(PRE+SEN) = "
                    "2·0.3161·0.285/0.6011 ≈ 0.300. The reported row is internally consistent. Table 1 deltas vs Qwen "
                    "(38.4/64.0/27.2/74.9) also recompute.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign",
            "supporting": ["adapt_via_conditioning"],
            "matches": [
                smatch("sol", p, "generative_process_redesign",
                       reason="Opus confirms sol. The headline operation (title, contributions, largest ablation step) "
                              "treats the conventionally fixed tool set / action space of the iterative agent loop as a "
                              "free variable that grows from recurring successful sequences (son55:E001, sol:E003). That "
                              "matches the run convention for papers that make a fixed agent artifact editable (r01b "
                              "2402.11359, r10b 2602.02474). C15/C23/C24 are specific generative-model operations, so "
                              "sub=null."),
                smatch("sol", p, "adapt_via_conditioning",
                       reason="Supporting: image-feature retrieval of correct step demonstrations conditions a policy "
                              "trained (SFT/GRPO) to read them, C03's retrieved-reference + upstream-training form (run "
                              "convention r08a EvolveR, r12b ARISE). It explains only the memory branch."),
            ],
            "outside_taxonomy": False,
            "reason": "Two executed operations: growing the action space from mined successful subsequences "
                      "(generative_process_redesign, primary) and retrieval conditioning of a trained policy (C03). "
                      "son55's self_supervised_signal_engineering is rejected. Ground-truth labels gate every memory and "
                      "registry write (son55:E015, sol:E009), so the card's 'absence of ground-truth labels' premise "
                      "fails, as son55 itself notes. The composite-usage reward is an auxiliary shaping term.",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("sol", p, "crystallize_executable_capability", "H08",
                                              fit="medium (promotion of recurring tool sequences into primitives; no "
                                                  "typed graph, trace-level repair or rollback)"),
                                       dmatch("sol", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.05860-1"): "local:2603.05860-3"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "met",
                    "reason": "Opus (revised from son55 'partial'). Rows A→B add memory retrieval to the same SFT recipe "
                              "with identical hyperparameters (sol:E005), which is the required conditioning-vs-same-"
                              "training comparison. It is single-run (counted under E.statistics)."},
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'unmet'). Row A is the plain fine-tuning alternative and the "
                              "task-specific classifiers are trained baselines. There is no nearest-neighbour-only or "
                              "longer-context alternative to the composite/GRPO stack."},
                "rs:adapt_via_conditioning/RE-4": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'met'). The A→B→C→D chain is additive only. Composites without "
                              "memory and GRPO without composites are never run, and the card names this shallow form "
                              "as insufficient."},
                "rsi:crystallize_executable_capability/S3": {
                    "status": "partial",
                    "reason": "Opus (revised from son55 'unknown'). Composites mined from training trajectories are "
                              "used on evaluation images, and row C vs B shows an aggregate gain there. No per-composite "
                              "check on inputs it was not mined from is reported."},
                "local:2603.05860-3": {
                    "note": "A4: son55's local-1 (trajectory-level verification of composites) renumbered to local-3; "
                            "local-1 is sol's held-out/cross-domain question."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats 'task'; kept. The memory and registry are built on training episodes and "
                                   "read at evaluation, and Table 3 toggles them. But REFUGE2/MITEA splits, patient "
                                   "separation and test-time update behaviour are unstated (index F3 unknown). So the "
                                   "'later tasks' cannot be confirmed as distinct from the build stream. retained would "
                                   "need that split stated.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, author-reported BACC/F1 gains on REFUGE2 and MITEA (and RAM-W600 "
                                         "against task-specific classifiers) for a LoRA-tuned 3B agent that adds "
                                         "label-gated memory retrieval, frequency-mined composite tools and a "
                                         "composite-usage GRPO stage. The additive ablation points the same way. "
                                         "Cross-domain generalization, composite-level validity and the causal channel "
                                         "of composites at inference are not shown.",
            "unresolved": ["Train/test splits for REFUGE2/MITEA and whether memory/registry update at test time.",
                           "τ, k and the composite inventory; how a composite is presented/executed at inference "
                           "(opus:O01, opus:O02).",
                           "Nearest neighbours (Biomni, EvolveR, MemSkill, Voyager-type libraries) not compared."],
        },
        "ratings": {
            "G": kept("sol", p, "G", "Both seats 2; re-checked. 'Tool sets and invocation strategies are predefined and "
                      "remain static' is a concrete fixed object (son55:E001), and MemSkill/EvolveR/Biomni are cited "
                      "(sol:E001). General tool/skill-library growth outside medicine is not compared (son55:E014), and "
                      "brittleness under shift is asserted, not measured.",
                      ["son55:E001", "sol:E001", "son55:E014"]),
            "M": kept("sol", p, "M", "Both seats 2; re-checked. Label-gated memory, frequency-mined composites and a "
                      "GRPO stage form a concrete chain. But the RL reward pays for composite presence, not correctness "
                      "(son55:E002, sol:E004), frequency stands in for utility (sol:E003), and no account is given of "
                      "why composites should raise diagnostic accuracy. Not refuted by the paper's own equations, so "
                      "not 1.",
                      ["son55:E002", "son55:E005", "sol:E003", "sol:E004"], ["son55:E005"]),
            "X": kept("sol", p, "X", "Both seats 2; kept, with an Opus finding added (shared correction on the reason). "
                      "The write gate (correct final answer; sol:E009), mining rule (sol:E003) and image retrieval "
                      "(sol:E002) are specified. τ, k, the composite inventory, retirement and versioning are not. The "
                      "paper also defines a composite two ways: as an action in a growing action space (opus:O02) and, "
                      "in the reward, as an atomic tool-name run inside one step (opus:O01). It never says how a "
                      "composite reaches the policy at inference, including in row C (no GRPO). That is anchor 2 (key "
                      "interface unclear or conflicting; precedent r12b ARISE). Not 1, because the write and read paths "
                      "themselves are reconstructable.",
                      ["sol:E002", "sol:E003", "sol:E009", "son55:E003", "opus:O01", "opus:O02"], ["sol:E008"]),
            "E.measurement": kept("sol", p, "E.measurement", "Both seats 2; re-checked. BACC/F1 on public labelled "
                                  "datasets suit imbalanced diagnosis. The RAM-W600 row and the Table 1 deltas recompute "
                                  "exactly (opus:O04). Gaps: no sample sizes or confusion matrices, task-specific "
                                  "baselines near chance (son55:E013), and two text slips (four conditions called "
                                  "'three'; 'recall' claimed but never reported; opus:O03). These do not touch the "
                                  "metric.",
                                  ["son55:E008", "opus:O04", "sol:E007"], ["son55:E013", "opus:O03"]),
            "E.causality": kept("sol", p, "E.causality", "Both seats 2; re-checked. There is a same-hyperparameter "
                                "additive ablation A→B→C→D (sol:E005, son55:E006, son55:E007). Missing: leave-one-out "
                                "arms, a hand-designed/random-composite or correctness-aware-reward control, and a "
                                "stated channel for row C (counted under X, A2). Table 1 sets a per-dataset-trained "
                                "agent against zero-shot VLMs and agents (unequal training exposure; A2 also E.cost).",
                                ["sol:E005", "son55:E006", "son55:E007", "sol:E006"], ["son55:E008"]),
            "E.holdout": kept("sol", p, "E.holdout", "Both seats 1; re-checked. Only RAM-W600 names a test set. "
                              "REFUGE2/MITEA splits, patient-level separation and whether memory/registry update at test "
                              "time are unstated, and the cross-domain claim (son55:E012) has no transfer experiment. "
                              "Not 0: the comparisons are on evaluation splits, and label-gated writes cannot grow the "
                              "store from unlabeled test inputs as described.",
                              ["son55:E012", "son55:E015", "sol:E009"]),
            "E.statistics": kept("sol", p, "E.statistics", "Both seats not_reported; re-checked. There are no sample "
                                 "sizes, seeds, intervals or repeated runs anywhere in §1–5, Tables 1–3 or the figure "
                                 "captions (A2 ladder: 0).", []),
            "E.cost": kept("sol", p, "E.cost", "Both seats not_reported; re-checked. There is no compute, GPU time, "
                           "teacher-call count or mining/RL cost. The LoRA/lr settings are configuration, not cost.", []),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (no appendix in the HTML). In scope (A3): the retained, evaluated objects "
                  "are a non-weight memory and a composite-tool registry, built from execution feedback and toggled in "
                  "the ablation, even though LoRA weights are also trained. claim_type system_method. All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 3 (composite count / BACC curves; the caption's +8.8%) is image-only and not used for "
                             "any rating. Figure 4 is a qualitative case study.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "See rs_pattern.reason. The headline operation is growing the action space from recurring successful "
                "sequences, and C03 covers only the memory branch. son55's own note that its primary 'does not describe' "
                "composite discovery supports this.", ["son55:E001", "sol:E003", "sol:E005"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", "C03"], ["generative_process_redesign", None]],
                "self_supervised_signal_engineering is rejected because ground-truth labels gate all writes (son55:E015). "
                "C03 is kept as supporting.", ["son55:E015", "sol:E009", "sol:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["couple_context_and_weight_updates", "H28"], ["crystallize_executable_capability", "H08"],
                 ["index_experience_for_reuse", "H03"]],
                "H08's tactical pattern explicitly includes 'recurring text plans or tool sequences are promoted into new "
                "callable primitives once recurrence is demonstrated'. That is MACRO's operation, so the closest sub "
                "is H08 (fit medium: no graph, repair or rollback), not null. H28 and H03 agree in both seats.",
                ["sol:E003", "son55:E003"], NOSCORE),
            XC(p, "local:2603.05860-1", "sol", "unmet",
               "A4 hidden collision: sol's local-1 asks about held-out/cross-domain evidence, son55's about trajectory-"
               "level composite verification. Final local-1 is sol's question: unmet (no split, patient or unseen-domain "
               "protocol). son55's question moved to local-3 and keeps its 'partial'.", ["sol:E009", "son55:E012"]),
            XC(p, "local:2603.05860-2", "son55", "unmet",
               "Verified: the GRPO reward is 1 if any registered composite appears and does not depend on correctness "
               "(son55:E002, son55:E005), so it can be gamed by emitting composite sequences. No control rules this out.",
               ["son55:E002", "son55:E005"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "revised", "met",
               "Rows A→B are the conditioning-on/off comparison on the same SFT recipe with identical hyperparameters "
               "(sol:E005). son55's 'no matched unconditioned baseline' overlooks row A.", ["sol:E005", "son55:E007"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "Verified: no overlap or split analysis exists, yet cross-domain generalization is claimed (son55:E012).",
               ["son55:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "revised", "partial",
               "Plain fine-tuning (row A) and trained task-specific classifiers are present. A nearest-neighbour-only or "
               "longer-context alternative is not, so partial rather than unmet.", ["sol:E005", "son55:E013"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "revised", "partial",
               "Additive single-order ablation only. Interactions (composites without memory, GRPO without composites) "
               "are untested, which the card names as insufficient.", ["son55:E006", "son55:E007"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "unmet",
               "Verified: there is no sensitivity analysis to memory quality or coverage, or to teacher vs self "
               "trajectories.", ["son55:E011"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "unmet",
               "Kept as a check question although the card is not matched. One 3B base model and three datasets.",
               ["son55:E010"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "unmet",
               "Kept as a check question. No cost is given for teacher trajectories, mining or RL.", ["son55:E011"]),
            XC(p, "rsi:crystallize_executable_capability/F1", "son55", "unmet",
               "Verified (failure present): composites are entangled with memory, SFT and GRPO, and only the additive "
               "chain separates them.", ["son55:E006", "son55:E007"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "sol", "partial",
               "Admission rests on executed trajectories whose final answer matches ground truth, plus a recurrence "
               "count. That is execution-grounded, not LLM judgment, but the composite itself is never replayed or "
               "invoked in isolation (sol:E008). So partial, not son55's unmet.", ["sol:E003", "sol:E008", "son55:E004"]),
            XC(p, "rsi:crystallize_executable_capability/S3", "revised", "partial",
               "Composites are applied to evaluation inputs and row C shows an aggregate gain there, so this is not "
               "unknown. There is still no per-composite validation on unseen inputs.", ["son55:E006"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unknown",
               "Verified: test-time update behaviour and split construction are not stated.", ["son55:E015"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "met",
               "Verified: writes require the final prediction to match the label (§3.2).", ["son55:E015", "sol:E009"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "Verified: one memory-removal step (A→B), single run.", ["son55:E007"]),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.X.reason", "sol_value": "2 (interface/τ/retirement gaps)",
             "son55_value": "2 (execution semantics absent)", "final_value": 2,
             "reason": "Both seats saw that composite execution details are missing, but neither recorded that the paper "
                       "gives two incompatible definitions of a composite: an action in A_t (opus:O02) and an atomic "
                       "name run inside one step, as rewarded by Eq. 9 (opus:O01). Nor did they note that row C (no "
                       "GRPO), the largest ablation gain, has no stated inference channel. Counted under X (A2); the "
                       "rating stays 2 under the r12b ARISE precedent for conflicting key conditions.",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none"},
            {"field_path": "expectations[local:2603.05860-1].id", "sol_value": "local-1 = held-out/cross-domain (unmet)",
             "son55_value": "local-1 = composite trajectory-level verification (partial)",
             "final_value": "local-1 = held-out; local-3 = composite verification",
             "reason": "A4 hidden ID collision; renumbered.", "evidence_ids": ["sol:E009", "son55:E009"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full pinned text first. Initial view: in scope (memory and "
                                                   "composite registry are non-weight, retained from training, toggled "
                                                   "in Table 3). The reward pays for composite presence, not correctness. "
                                                   "Composite inference semantics conflict between §3.1 and Eq. 9. No "
                                                   "splits, sample sizes or costs. Tables recompute. Expected G 2, M 2, "
                                                   "X 1–2, Em 2, Ec 2, Eh 1, Es 0, Ecost 0.",
            "integrity_checks": "Both seats a1 on 2603.05860v1, material sha 302781e3…; canonical seat hashes equal "
                                "conflicts.json; both completed 15+31 identification with valid parents.",
            "core_claim_check": "Identical seat totals (42.5) re-derived item by item. Two shared omissions are filed as "
                                "reason-level corrections (X; the ablation-text slips, under E.measurement). No rating "
                                "moves. evidence_level task kept.",
            "rating_agreement": "All eight items agree across seats and were re-checked against the text.",
        },
    }

    # =========================================================== 2603.09206 MM-Zero (both out_of_scope)
    p = "2603.09206"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: "
          "Proposer, Coder and Solver are 'initialized from the same base model and trained using GRPO' (opus:O01), with "
          "full fine-tuning and a trainable vision tower (opus:O02). The SVG code and rendered images are filtered "
          "per-round training data for the solver (opus:O03), not a tool, skill or memory retained and read at test "
          "time. The evaluated product is the trained checkpoint. Not scored; null is a disposition, not a zero-quality "
          "rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p, "claim_type": "component_training"},
        "opus_evidence": [
            opus_ev(p, "O01", "All three roles are initialized from the same base model and trained using Group Relative Policy Optimization (GRPO)",
                    "Abstract", "All three roles improve through GRPO weight updates."),
            opus_ev(p, "O02", "All three models use full fine-tuning (LoRA rank 0); the vision tower is trainable.",
                    "Appendix 0.B", "The persisted change is full model weights."),
            opus_ev(p, "O03", "We retain only successfully rendered images and their associated questions as the training set for the solver.",
                    "§2.2 Solver", "The 'retained' artifacts are RL training data, not a harness component."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("sol", p)["rs_pattern"]), "sol") | {
            "reason": "Informational (out_of_scope). Both seats: generated-and-filtered synthetic samples with majority-vote "
                      "pseudo-labels retrain the roles, C08's generate → filter → retrain loop (run convention for "
                      "proposer–solver co-training: r05b, r07b, r09b, r11a, r12b). No score effect."},
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22",
                                              fit="high (informational; out_of_scope weight-level member)")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={("son55", "local:2603.09206-1"): "local:2603.09206-2"},
            overrides={"local:2603.09206-2": {"note": "A4: son55's local-1 (seed variance/scaling) renumbered to local-2."}}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b–r12b). Both seats wrote 'task'; see shared_error_corrections.",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric. Benchmark gains are author-reported results "
                                             "of GRPO-trained checkpoints. Noted for completeness: the text's 'reaching "
                                             "56.6% at Iter 5' does not match Table 2 (54.5; sol C1).",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the weight-training results are wrong."]},
        "ratings": {k: R("unknown", None, a3, ["opus:O01", "opus:O02"]) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "figure_dependence": "Figure 2 (render success / solvability curves) is image-only; not used.",
        "resolutions": [
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "revised", None,
                "Claim support is not assessed for an excluded row, so null is canonical (precedent r09b GenEnv, r11a, "
                "r12b SAGE/GASP). Neither 'scoped' nor 'unresolved' is the run's value.", ["opus:O01", "opus:O02"],
                "none (row is unscored)"),
            XC(p, "local:2603.09206-1", "sol", "unmet",
               "A4 hidden collision: sol's local-1 asks whether the code generation forms a retained harness component "
               "(unmet: it does not; opus:O03), son55's whether seed variance and scaling are reported. Final local-1 "
               "is sol's question. son55's moved to local-2 (unknown, informational).", ["sol:E003", "sol:E004", "opus:O03"]),
            XC(p, "rsi:self_generate_the_curriculum/F3", "son55", "unmet",
               "Informational. The validity (easy-question agreement) and difficulty (self-consistency) certificates "
               "both come from the model family being trained.", ["son55:E004"]),
            XC(p, "rsi:self_generate_the_curriculum/S1", "son55", "partial",
               "Informational. Rendering is an execution check, but semantic validity is a proxy judged by the same "
               "Solver. sol's own domain condition check also says partial.", ["son55:E004", "son55:E006"]),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level", "sol_value": "task", "son55_value": "task", "final_value": None,
             "reason": "Both seats labelled an out_of_scope weight-training paper 'task'. EVIDENCE.md's ladder grades "
                       "retained non-weight changes, and this paper has none, so the canonical value is null (run "
                       "precedent r05b–r12b).",
             "evidence_ids": ["opus:O01", "opus:O02"], "score_impact": "none (row is unscored)"},
            {"field_path": "expectations[local:2603.09206-1].id", "sol_value": "local-1 = harness-retention scope check",
             "son55_value": "local-1 = seed variance / scaling", "final_value": "local-1 = scope; local-2 = seeds",
             "reason": "A4 hidden ID collision; renumbered.", "evidence_ids": ["sol:E004", "son55:E005"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the abstract, §2 (pipeline, rewards), §3–4 and Appendix 0.B first: "
                                                   "three roles from one base model, each GRPO-trained with full "
                                                   "fine-tuning → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2603.09206v1, material sha a2a8a5b3…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O03.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2603.09716 AutoAgent (Δ2.5)
    p = "2603.09716"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "establishes new state-of-the-art results on three of the four benchmarks (HotpotQA, 2Wiki, and Bamboogle) under both evaluation metrics.",
                    "§8.2", "Text claim checked against Table 1 (O02–O04)."),
            opus_ev(p, "O02", "AutoAgent 0.530 0.630 0.466 0.474", "Table 1 (HotpotQA Acc/LLM, 2Wiki Acc/LLM)",
                    "Opus check. AutoAgent 2Wiki Acc 0.466 is below IRCoT's 0.492 (O03), and its LLM score 0.474 is below "
                    "Self-Ask's 0.478 (O04). The 2Wiki 'state of the art under both metrics' claim is false on both.",
                    kind="our_inference"),
            opus_ev(p, "O03", "IRCoT 0.434 0.308 0.492 0.114", "Table 1 IRCoT row", "IRCoT 2Wiki Acc 0.492."),
            opus_ev(p, "O04", "Self-Ask 0.392 0.462 0.336 0.478", "Table 1 Self-Ask row", "Self-Ask 2Wiki LLM 0.478."),
            opus_ev(p, "O05", "obtaining the best overall scores on QwQ-32B and Qwen3-30B-A3B", "§8.3 Open-source models",
                    "Contradicted by Table 3 (O06): on Qwen3-30B-A3B, HLE-all is DeepAgent 7.2 vs AutoAgent 6.2."),
            opus_ev(p, "O06", "DeepAgent 20.4 4.2 10.5 15.8 8.0 4.4 7.2 48.5 76.6 AutoAgent 34.0 25.0 34.2 30.9 5.7 8.0 6.2 58.2 61.2",
                    "Table 3, Qwen3-30B-A3B block", "HLE text/mm/all: DeepAgent 8.0/4.4/7.2; AutoAgent 5.7/8.0/6.2."),
            opus_ev(p, "O07", "It presents the selector (a learned or heuristic module) with the sequence of compressed summaries",
                    "§6.1 Dynamic Assembly Stage", "The EMO selector's type is left open; no algorithm, prompt or training is given."),
            opus_ev(p, "O08", "The Elastic Memory Orchestrator periodically supplies structured experience data",
                    "§3.3 Evolution Cycle", "The evolution trigger is 'periodically'. §8.1 never states whether, when or on "
                    "which tasks cognition evolves during the reported runs."),
            opus_ev(p, "O09", "we also report average step efficiency (number of actions taken).", "§8.1 Metrics",
                    "Promised but absent: Tables 1–5 contain no step-efficiency, token or call figures."),
            opus_ev(p, "O10", "For every LLM call across all systems, the maximum generation tokens are set to 1024",
                    "§8.1 Implementation Details", "Per-call caps and a step cap are equalised. The number of calls, "
                    "including the analyzer, summariser and EMO selector, is not bounded or reported."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign",
            "supporting": ["heterogeneous_decomposition"],
            "matches": [
                smatch("sol", p, "generative_process_redesign",
                       reason="Opus confirms sol. The conventionally fixed, hand-written tool and peer descriptions of an "
                              "iterative agent loop (son55:E001) become a free variable revised from intention-outcome "
                              "analysis. Run convention: this card for papers that turn a fixed agent artifact into an "
                              "editable one (r01b 2402.11359, r10b 2602.02474). C15/C23/C24 do not fit, so sub=null."),
                smatch("sol", p, "heterogeneous_decomposition",
                       reason="Supporting: the EMO partitions history steps by current relevance and treats each part "
                              "differently (raw / summary / omit), not with one uniform compression. No C04 fit."),
            ],
            "outside_taxonomy": False,
            "reason": "son55's outside_taxonomy is rejected: a card fits at medium strength under the run's convention, and "
                      "outside_taxonomy is for operations no card describes. Identification has no score effect.",
            "executes_pattern": True, "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "attribute_and_patch_incumbent", "H10"),
                                       dmatch("son55", p, "crystallize_executable_capability", None,
                                              **{"sub": "H08",
                                                 "fit": "low (§7.2 promotes frequent successful action sequences into "
                                                        "composite tools, H08's promotion-by-recurrence; never "
                                                        "instantiated, counted or ablated in the experiments)"}),
                                       dmatch("sol", p, "index_experience_for_reuse", "H04")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.09716-1"): "local:2603.09716-3",
                    ("son55", "local:2603.09716-3"): "local:2603.09716-1"},
            overrides={
                "local:2603.09716-1": {
                    "status": "unmet",
                    "reason": "Opus (sol local-1 and son55 local-3 ask the same question). No practice/evaluation split, "
                              "task order or frozen-cognition transfer is described, either for Table 5 (first 50 GAIA "
                              "questions) or for the main benchmarks. The expectation is therefore not met. son55's "
                              "'unknown' describes the overlap, not whether the protocol was reported.",
                    "note": "A4: son55's local-3 merged here; son55's local-1 (text vs table) moved to local-3."},
                "local:2603.09716-3": {
                    "reason": "son55's text-vs-table question, renumbered (A4). Opus adds two more false narrative claims: "
                              "2Wiki 'state of the art under both metrics' (opus:O01–O04) and best HLE on Qwen3-30B-A3B "
                              "(opus:O05, opus:O06).",
                    "evidence_ids": ["son55:E012", "son55:E013", "son55:E014", "opus:O02", "opus:O06"]},
                "rsi:crystallize_executable_capability/S5": {
                    "status": "unmet",
                    "reason": "Opus (revised from son55 'unknown'). Skill distillation is listed as an ablation "
                              "(son55:E011), but no result appears in the complete text (no appendix). The retained "
                              "library is not shown to carry any gain."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O02", "opus:O06"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats 'task'; kept. Table 5 compares initial vs evolved cognition on the first 50 "
                                   "GAIA questions with no stated practice/test separation. Main-benchmark gains are not "
                                   "traced to retained cognition.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, author-reported results. The combined architecture beats the listed "
                                         "baselines on many (not all) cells under a 5-step cap. EMO on/off helps "
                                         "DeepSeek-R1 on GAIA/HLE. In a synthetic 50-question tool-failure setting, "
                                         "evolved tool descriptions raise EM. Retained improvement on later disjoint "
                                         "tasks, skill distillation, collaboration robustness and efficiency are not "
                                         "shown, and several narrative claims contradict the tables.",
            "unresolved": ["Whether and how cognition evolves during the main benchmark runs (opus:O08).",
                           "Practice/test separation for Table 5.",
                           "Text–table contradictions (son55:E012, son55:E013, opus:O02, opus:O06).",
                           "LLM-judge validity; call/token cost of analyzer and EMO."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 2; re-checked. Static hand-written tool and peer descriptions are a "
                      "named fixed object (son55:E001). Reflexion/Voyager/MemGPT are cited, but the claimed residual "
                      "('episodic', son55:E017) is asserted. Brittleness is shown only in the synthetic test.",
                      ["son55:E001", "son55:E017", "sol:E012"]),
            "M": kept("son55", p, "M", "Both seats 2; re-checked. The chain is concrete: intention-outcome analysis → "
                      "localized description edits, raw/summary/omit assembly, composite actions. It has one "
                      "discriminating test (son55:E010). The attribution assumption (the failure lies in the "
                      "description) and the consistency-only acceptance (son55:E004) are weak.",
                      ["son55:E003", "son55:E004", "son55:E010", "sol:E005"]),
            "X": R("resolved", 1, "Opus sides with sol. The loop exists only as prose: the selector is 'a learned or "
                   "heuristic module' (opus:O07), validation is 'e.g., for consistency' (son55:E004), the evolution "
                   "trigger is 'periodically' (opus:O08), and composite admission has no threshold (son55:E005). No "
                   "prompts, algorithm or code are provided. The experimental section never states whether cognition, "
                   "skills or peer models evolve during the reported runs. The key operations' effective conditions "
                   "are missing, so this falls below anchor 2.",
                   ["opus:O07", "opus:O08", "son55:E004", "son55:E005", "sol:E003", "sol:E004"]),
            "E.measurement": R("resolved", 1, "Both seats 1; kept, with Opus additions. Standard benchmarks are used, but "
                               "GAIA/HLE pass@1 comes from an unvalidated o3-mini judge (sol:E007), and HLE is described "
                               "two different ways (son55:E014). The narrative contradicts the tables in at least four "
                               "places: DeepSeek-R1 GAIA 48.5 vs 52.1 and HLE 15.2 vs 28.2 (son55:E012, son55:E013), "
                               "2Wiki 'SOTA under both metrics' false on both (opus:O02), and Qwen3-30B HLE 'best' false "
                               "(opus:O06). The RAG backbone is unstated. The tables themselves are not refuted, so 1, "
                               "not 0.",
                               ["sol:E007", "son55:E014", "son55:E012", "son55:E013", "opus:O02", "opus:O06"],
                               ["son55:E012", "son55:E013"]),
            "E.causality": R("resolved", 1, "Opus sides with son55. Four ablations are announced (son55:E011) and two are "
                             "reported. EMO on/off (one backbone, two benchmarks; son55:E008) concerns per-task context "
                             "management, not the retained cognition. The only evolved-vs-initial test is a synthetic "
                             "50% failure injection on 50 questions (son55:E009, son55:E010). Main-table gains are not "
                             "attributed to self-evolution, skill distillation or collaboration, and the analyzer/EMO "
                             "calls are uncounted against step-capped baselines (opus:O10; A2 also E.cost). sol's 2 "
                             "credits two partial tests for the whole system claim.",
                             ["son55:E008", "son55:E009", "son55:E010", "son55:E011", "opus:O10"], ["son55:E011"]),
            "E.holdout": kept("sol", p, "E.holdout", "Both seats not_reported; re-checked. No practice/evaluation split, "
                              "task order, frozen-cognition test or overlap statement exists for Table 5 or the main "
                              "benchmarks (full text, no appendix).", []),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 1 (A2 ladder). Some n are given (first 50 GAIA, "
                                 "HLE-500) and negative cells appear (Musique, ALFWorld DeepSeek-R1). Every result is a "
                                 "single run with no uncertainty (son55:E006).",
                                 ["son55:E006", "son55:E009", "sol:E011"]),
            "E.cost": R("not_reported", 0, "Opus sides with sol. Only caps are given: 5 steps, 1024 generation tokens per "
                        "call, temperature 0.7 (son55:E007, opus:O10). Caps are design parameters, not cost evidence "
                        "(precedents r02a 2410.08197, r10b 2602.02369). They also do not bound the analyzer, summariser "
                        "or selector calls. The promised 'average step efficiency' is never reported (opus:O09), and "
                        "the token-reduction claim has no figure (son55:E015). Precedent r04a 2504.00587 (efficiency "
                        "claimed, matched agent count only) → 0.",
                        ["son55:E007", "son55:E015", "opus:O09", "opus:O10"], [],
                        ["§8.1 Metrics and Implementation Details; §8.2–8.4 Tables 1–5; §6 EMO; §7 evolution; "
                         "full text, no appendix"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (no appendix). In scope: the retained object is prompt-level cognition "
                  "(tool and peer descriptions, skill library) revised from execution outcomes without retraining "
                  "(son55:E002). claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 1–3 are architecture diagrams; all results used are in Tables 1–5.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "See rs_pattern.reason: the fixed hand-written tool/peer descriptions are liberated as a variable "
                "revised from feedback. outside_taxonomy is reserved for operations no card describes.",
                ["son55:E001", "son55:E002", "sol:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["generative_process_redesign", None], ["heterogeneous_decomposition", None]],
                "Follows primary. The EMO raw/summary/omit partition is a differentiated treatment of history, kept as "
                "supporting.", ["sol:E004", "son55:E008"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["attribute_and_patch_incumbent", "H10"], ["crystallize_executable_capability", "H08"],
                 ["index_experience_for_reuse", "H04"]],
                "H10 and H04 agree. son55's crystallize match is kept: §7.2 composite actions exist in the method. The "
                "sub is H08 (promotion of recurring action sequences into callable primitives), the same reading as "
                "MACRO in this batch, rather than null. Fit is low because the experiments never instantiate or ablate "
                "composites.", ["son55:E005", "son55:E011"], NOSCORE),
            XC(p, "local:2603.09716-3", "revised", "unmet",
               "A4. son55's local-3 (no evolution-then-test protocol) is the same question as sol's local-1 and is "
               "merged there, final unmet. The local-3 ID now carries son55's text-vs-table question (its local-1), "
               "unmet, extended with opus:O02/O06. Neither question is 'unknown' after a full search.",
               ["son55:E009", "son55:E012", "son55:E013", "opus:O02", "opus:O06"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "unknown",
               "Verified: whether failures are decided by environment outcomes or by the LLM analyzer's own judgment is "
               "not stated.", ["son55:E003"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "unmet",
               "Verified (failure present): edits presume the description caused the failure, and nothing tests that "
               "against reasoning or tool noise.", ["son55:E003", "son55:E004"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "partial",
               "Verified: edits target individual tool/peer entries, but attribution correctness is unchecked. sol's "
               "domain condition check said 'met' for localization alone.", ["son55:E003", "sol:E002"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "unmet",
               "Verified: no execution replay or invocation evidence gates composite admission.", ["son55:E005"]),
            XC(p, "rsi:crystallize_executable_capability/S5", "revised", "unmet",
               "The skill-distillation ablation is announced but absent from the complete text, so the requirement is "
               "not met (not 'unknown').", ["son55:E011"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unknown",
               "Verified: the split between evolution data and reported tasks is not described.", ["son55:E006", "son55:E009"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "met",
               "Verified: per-step raw/summary/omit selection under a context budget.", ["son55:E008", "sol:E004"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "Verified: w/o-EMO on one backbone and two benchmarks.", ["son55:E008"]),
            res("ratings.X", *C(p, "ratings.X"), "sol", 1,
                "See ratings.X. The selector type, acceptance rule and evolution trigger are left open, and whether "
                "evolution runs in the experiments is unstated (opus:O07, opus:O08). That is 'key operations' effective "
                "conditions missing', below anchor 2.", ["opus:O07", "opus:O08", "son55:E004"], "−5.0 vs son55 (20×1/4)"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "son55", 1,
                "See ratings.E.causality. Two of four announced ablations are missing, and the cognition test is "
                "synthetic and single-setting. Headline gains are unattributed, and extra module calls are uncounted.",
                ["son55:E011", "son55:E009", "opus:O10"], "−3.75 vs sol (15×1/4)"),
            res("ratings.E.cost", *C(p, "ratings.E.cost"), "sol", {"status": "not_reported", "rating": 0},
                "See ratings.E.cost. Caps are design parameters and do not bound the extra module calls. The promised "
                "efficiency metric is absent (opus:O09). Precedents r02a/r04a/r10b → 0.",
                ["opus:O09", "opus:O10", "son55:E015"], "−1.25 vs son55 (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": "1 (judge, HLE naming, table/text 48.5/15.2)",
             "son55_value": "1 (same)", "final_value": 1,
             "reason": "Both seats missed two further narrative claims contradicted by the tables: 2Wiki 'state of the "
                       "art under both evaluation metrics' (IRCoT Acc 0.492 > 0.466; Self-Ask LLM 0.478 > 0.474), and "
                       "best HLE overall on Qwen3-30B-A3B (DeepAgent 7.2 > 6.2). They strengthen the existing 1 and do "
                       "not reach 0, because the tables themselves are not refuted.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05", "opus:O06"],
             "score_impact": "none"},
            {"field_path": "expectations[local:2603.09716-1].id", "sol_value": "local-1 = practice/test split (unmet)",
             "son55_value": "local-1 = text vs table (unmet)",
             "final_value": "local-1 = split (merged with son55 local-3); local-3 = text vs table",
             "reason": "A4 hidden ID collision with equal status, so the mechanical diff missed it. Renumbered and merged.",
             "evidence_ids": ["sol:E008", "son55:E012"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. Initial view: in scope (prompt-level "
                                                   "cognition revised from feedback). The method is prose without an "
                                                   "algorithm, and evolution in the experiments is unspecified (X ≈ 1). "
                                                   "Only EMO and a synthetic cognition test are ablated (Ec ≈ 1). The "
                                                   "narrative contradicts the tables (DeepSeek-R1 48.5/15.2, 2Wiki, "
                                                   "Qwen3 HLE) (Em 1). No split (Eh 0), no cost figures (Ecost 0).",
            "integrity_checks": "Both seats a1 on 2603.09716v1, material sha d20e305b…; canonical seat hashes equal "
                                "conflicts.json; sol completed identification, son55 declared outside_taxonomy with a "
                                "reason (valid, rejected on substance).",
            "core_claim_check": "The central self-evolution claim is supported only by Table 5 (synthetic, split "
                                "unstated). 'Consistent' superiority, efficiency and collaboration claims are not "
                                "supported. claim_support scoped.",
            "rating_agreement": "G, M, Em, Eh, Es agree and were re-checked (Em with additions). X → sol, Ec → son55, "
                                "Ecost → sol.",
        },
    }

    # =========================================================== 2603.13131 MineEvolve (Δ2.5)
    p = "2603.13131"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Hard Avg. is the task-count-weighted average over Iron, Redstone, Diamond, and Armor, using group sizes 16, 6, 7, and 13, respectively.",
                    "Appendix D.4, Table 6 caption",
                    "The 'held-out hard tasks' are weighted by the full hard-group sizes, i.e. all 42 hard tasks of the "
                    "suite. Task-level held-out status would require that accumulation episodes exclude these tasks, "
                    "and the source of the 0–400 accumulation episodes is never stated.", kind="our_inference"),
            opus_ev(p, "O02", "Static Store freezes the knowledge base and is used to examine whether continuous knowledge updates truly bring self-evolutionary gains.",
                    "§4.3", "The frozen store is the ablation, which implies the full system (Table 1, Fig. 4) keeps "
                            "updating during evaluation. The main table's knowledge-base state is otherwise unstated. "
                            "In Table 6 'Static Store' nevertheless rises 25.13→28.22 across checkpoints."),
            opus_ev(p, "O03", "task outcome and updated knowledge store", "Appendix C.1, Algorithm 1 (Output)",
                    "The loop writes K during task execution, consistent with online updating on the evaluated stream."),
            opus_ev(p, "O04", "Cold Start (Empty KB) 2.6 2.8 2.7 2.8 2.9", "Appendix D.5, Table 9",
                    "With an empty KB on the seven Diamond tasks, D.5 gives 2.6–2.9%, while Table 6's 0-episode "
                    "Diamond (also empty) is 9.0 (O05). D.5 declares a different protocol (O06), so this is "
                    "unexplained rather than contradictory."),
            opus_ev(p, "O05", "Iron 39.8 45.4 48.2 51.3 53.4 Redstone 24.2 27.2 28.6 30.0 31.0 Diamond 9.0 11.2 12.7 14.4 15.8",
                    "Appendix D.4, Table 6 (MineEvolve rows)",
                    "Opus recomputation: Hard Avg at 400 eps = (16·53.4+6·31.0+7·15.8+13·24.6)/42 = 35.02. That matches "
                    "the table but is below the main-table Qwen3.5-Plus hard average 37.13 (O07), so the main "
                    "evaluation uses a different, unstated knowledge state.", kind="our_inference"),
            opus_ev(p, "O06", "This experiment differs from the unified MCU evaluation protocol used in the main experiments",
                    "Appendix D.5", "D.5 numbers are not comparable to Table 6/Table 1 by the authors' own statement."),
            opus_ev(p, "O07", "MineEvolve 98.71 93.48 55.83 13.79 31.24 17.06 27.63 52.52", "Appendix D.2, Table 4 (Qwen3.5-Plus)",
                    "Opus recomputation: Easy (11·98.71+10·93.48+7·13.79)/28 = 75.61; Hard (16·55.83+6·31.24+7·17.06+"
                    "13·27.63)/42 = 37.13; Overall 52.52. These match Table 1, and Table 2's typed row is the same 37.13.",
                    kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["heterogeneous_decomposition"],
            "matches": [
                smatch("sol", p, "adapt_via_conditioning",
                       reason="Both seats: a curated skill/remedy bank conditions a frozen planner at inference (C03 "
                              "reference-substrate branch; no upstream training)."),
                smatch("sol", p, "heterogeneous_decomposition",
                       reason="Opus confirms sol's supporting match. Execution feedback is partitioned by outcome type "
                              "(successful segments → skills with verification rules; failed/stagnant segments → "
                              "remedies with triggers and repair actions), with a dedicated Skills-Only/Remedies-Only "
                              "ablation. C04 (compression of a high-impact minority) does not fit, so sub=null."),
            ],
            "outside_taxonomy": False,
            "reason": "Conditioning on a retained, curated bank (primary) plus a differentiated treatment of success vs "
                      "failure feedback (supporting).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("sol", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": ["H30 rejected: admission checks exist, but there is no retirement, size bound "
                                          "or marginal-gain test, and H30's decisive choice is pairing the two."],
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.13131-1"): "local:2603.13131-2",
                    ("son55", "local:2603.13131-2"): "local:2603.13131-4",
                    ("son55", "local:2603.13131-3"): "local:2603.13131-5"},
            overrides={
                "local:2603.13131-2": {
                    "status": "unmet",
                    "reason": "Opus (sol local-2 and son55 local-1 ask the same question). Run counts R_t are symbolic, "
                              "the number of world seeds is never given, and no interval, std or test appears anywhere. "
                              "Some main-table margins are under one point (GLM-4.7 overall +0.37 vs Optimus-2). A bare "
                              "'multiple world seeds' declaration does not partially meet the expectation.",
                    "note": "A4: son55's local-1 merged here."},
                "local:2603.13131-4": {
                    "reason": "son55's held-out question (its local-2), renumbered. Opus adds that Table 6's 'held-out' "
                              "hard tasks are all 42 hard tasks (opus:O01).",
                    "evidence_ids": ["son55:E015", "son55:E016", "son55:E017", "opus:O01"],
                    "note": "A4: renumbered from son55 local-2."},
                "local:2603.13131-5": {"note": "A4: renumbered from son55 local-3 (LLM-judged curator validation)."},
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "met",
                    "reason": "Opus (son55's value). S5 asks for a gate (execution tests, quality filters or judge-"
                              "controlled merges) before entries are published. The five-part Curator acceptance rule "
                              "is such a gate. Counterfactual utility is evidence_gated_retention/S1's question, not "
                              "this one."},
            }),
        "claims": lambda c: add_counter(c, "C3", ["opus:O01", "opus:O02"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained'; kept. A knowledge base frozen after 0–400 accumulation "
                                   "episodes raises later hard-task SR against empty, Static Store and Text Reflection "
                                   "stores under equal eval-time budgets (Table 6). Frozen lower-tier knowledge transfers "
                                   "to Diamond (Table 9). The Table 6 'held-out' set is the full hard-task set, so the "
                                   "cleanest independence is the cross-tier transfer. Author-reported, not reproduced.",
            "claim_support": "scoped",
            "strongest_supported_claim": "In Minecraft MCU, a curated store of typed-feedback skills and remedies, frozen "
                                         "at evaluation, raises hard-group success over empty, Static-Store and "
                                         "Text-Reflection stores built from the same 400 episodes. Typed feedback beats "
                                         "binary and trajectory reflection under matched budgets. Lower-tier knowledge "
                                         "transfers to Diamond. Main-table margins over Optimus-2 are small and lack "
                                         "uncertainty, and the main-table knowledge state is unstated.",
            "unresolved": ["Source of accumulation episodes vs the 42 evaluated hard tasks (opus:O01).",
                           "Knowledge-base state and online updating in Table 1 / Fig. 4 (opus:O02, opus:O03, opus:O05).",
                           "Static Store definition vs its rising curve; Table 9 vs Table 6 empty-KB Diamond (opus:O04).",
                           "Seed/run counts and variance; Figure 4 values image-only; XENON not compared."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 3; re-checked. Feedback granularity and knowledge form are specific "
                      "fixed objects, with Voyager/Optimus-1/XENON named (sol:E002, sol:E003). The bottleneck is tested "
                      "directly (Table 2). XENON, the closest neighbour, is described but not compared, so not 4.",
                      ["sol:E002", "sol:E003", "son55:E002", "son55:E018"]),
            "M": kept("son55", p, "M", "Both seats 3; re-checked. Typed environment feedback → trigger-conditioned "
                      "skill/remedy → curated store → suffix repair is coherent and makes distinguishable predictions "
                      "(binary vs reflection vs typed). The typed fields are hand-engineered for Minecraft "
                      "(son55:E021).", ["son55:E004", "son55:E005", "son55:E018", "sol:E010"], ["son55:E021"]),
            "X": kept("son55", p, "X", "Both seats 3; re-checked. Pseudocode (Alg. 1–3), schemas, the acceptance rule, "
                      "budgeted retrieval and repair scope are reconstructable. Missing: retirement/rollback, threshold "
                      "values (λ, ε_p, η_fail, h) and the main-run store state (opus:O02). 'Executability' is an LLM "
                      "judgment, not a replay (son55:E009).",
                      ["son55:E006", "son55:E007", "son55:E008", "sol:E008", "opus:O03"], ["son55:E009", "opus:O02"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; re-checked. Success is read from game "
                                  "state on an established tech-tree suite, and the task-weighted aggregates recompute "
                                  "exactly (opus:O07, opus:O05). Caveats: the 70-task subset selection, five-backbone "
                                  "baseline re-implementations, and the unexplained empty-KB Diamond gap between D.5 "
                                  "and Table 6 (opus:O04; D.5 declares a different protocol, opus:O06).",
                                  ["son55:E022", "son55:E011", "opus:O07", "opus:O05"], ["opus:O04"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 3; re-checked. Numeric controls: typed vs binary "
                                "vs trajectory reflection under matched KB size and LLM-call budget (Table 2), and "
                                "empty/Static-Store/Text-Reflection stores from the same 400 episodes (Table 6). The "
                                "component ablations (Fig. 4) are image-only and used only as described. Not 4: no "
                                "Voyager/XENON-style alternative on the same protocol, and Static Store's rising curve "
                                "(opus:O02) clouds the update-vs-freeze contrast.",
                                ["son55:E018", "son55:E013", "son55:E015", "son55:E019", "sol:E013"], ["opus:O02", "sol:E020"]),
            "E.holdout": R("resolved", 2, "Opus sides with son55. The knowledge base is frozen at evaluation (son55:E014). "
                           "But Table 6's 'held-out hard tasks' are weighted over all 42 hard tasks (opus:O01), and the "
                           "accumulation episodes' source is unstated. Diamond-only learning re-tests its own seven "
                           "tasks (son55:E017). The main table appears to update online on the evaluated stream "
                           "(opus:O02, opus:O03). The genuine held-out evidence is Curriculum Pretrain→Freeze "
                           "(lower tiers → Diamond; son55:E016), on seven tasks with an unstated seed count. That is "
                           "anchor 2 (key coverage gaps). sol's 3 took 'held-out' at face value.",
                           ["son55:E013", "son55:E014", "son55:E016", "opus:O01"], ["son55:E017", "opus:O02", "opus:O03"]),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 1 (A2 ladder). Task counts and the low-SR "
                                 "boundaries are reported. Run counts are symbolic (son55:E012), seeds are unstated, and "
                                 "there are no intervals despite sub-point margins (son55:E010).",
                                 ["son55:E012", "son55:E010", "sol:E022"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 2; re-checked. Eval-time LLM calls, retrieved tokens, "
                           "latency and KB size are reported (Table 7), and eval-time call budgets are matched "
                           "(son55:E011). The 400-episode accumulation cost (Monitor/Inducer/Curator calls, environment "
                           "rollouts) and baselines' actual spend are absent.",
                           ["son55:E020", "son55:E011", "sol:E021"], ["son55:E020"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text, including Appendices A–E, read. In scope: an external skill/remedy store "
                  "built from execution feedback, gated, retained and read by a frozen planner (no parameter updates). "
                  "claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figure 4 (component ablations) is image-only: used only as the text describes it, no "
                             "values taken. Figure 5's values are given numerically in Table 6.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", "C03"], ["heterogeneous_decomposition", None]],
                "C03 agrees. heterogeneous_decomposition is added as supporting: the success/failure partition with "
                "differentiated knowledge forms is a core design with its own ablation (Skills Only / Remedies Only).",
                ["sol:E004", "sol:E014"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"]],
                "H01 (merge/insert/conflict-filter maintenance by an LLM curator) agrees. H00 is added from son55: "
                "remedies and skills are trigger-conditioned lessons grounded in typed outcomes. H30 is rejected: there "
                "is no retirement, size bound or marginal-gain test (son55's own 'partial' says so). Its S1/S2 remain as "
                "check questions.", ["son55:E005", "son55:E006", "son55:E007", "sol:E007"], NOSCORE),
            XC(p, "local:2603.13131-1", "sol", "partial",
               "A4 hidden collision: sol's local-1 is the Static Store question, son55's is seeds/variance. Final "
               "local-1 is sol's question: partial (the control exists, but its definition conflicts with its rising "
               "curve; opus:O02). son55's question merged into local-2 (final unmet).", ["sol:E019", "sol:E020", "opus:O02"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "met",
               "Verified: trajectory/case-retrieval systems (JARVIS-1, Optimus-1), a static store and free-form reflection "
               "are compared.", ["son55:E010", "son55:E019"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "met",
               "Verified at author-report level: each module has an ablation variant under matched budgets. The Fig. 4 "
               "values are image-only, so only the text's ordering is used.", ["son55:E018", "son55:E019"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "unmet",
               "Verified: single environment; the feedback fields are Minecraft-specific.", ["son55:E021"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "Verified: a store-size sweep and construction pathways exist, but no noisy-entry injection.",
               ["son55:E013", "son55:E016"]),
            XC(p, "rsi:abstract_experience_into_guidance/F2", "son55", "partial",
               "Verified: a Minecraft application of act-reflect-store, but the typed-feedback and repair deltas are "
               "isolated by controls.", ["son55:E018"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: skills and remedies come from success and failure separately, with no paired contrast on the "
               "same situation.", ["son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "met",
               "The five-part Curator acceptance rule precedes persistence (son55:E006). S5 asks for a gate, not a "
               "counterfactual, so sol's 'partial' applies a stricter H29/H30 standard here.", ["son55:E006", "son55:E009"]),
            XC(p, "rsi:evidence_gated_retention/S1", "son55", "unmet",
               "Kept as a check question although H30 is not matched. Verified: support counts and usage history are "
               "stored, but no with/without-entry credit is computed.", ["son55:E007"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Kept as a check question. Verified: no retirement or size bound; the KB grows to 143 skills and 191 "
               "remedies.", ["son55:E007", "son55:E020"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "met",
               "Verified: budgeted relevance retrieval (1216 tokens at 400 eps).", ["son55:E008", "son55:E020"]),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "son55", 2,
                "See ratings.E.holdout. Table 6's 'held-out' set is the full 42-task hard set (opus:O01), the "
                "accumulation source is unstated, and the main evaluation updates online. Only the cross-tier Diamond "
                "transfer is clean. These are key coverage gaps (anchor 2).",
                ["opus:O01", "son55:E016", "son55:E017", "opus:O02"], "−2.5 vs sol (10×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason", "sol_value": 3, "son55_value": 3, "final_value": 3,
             "reason": "Both seats missed that the empty-KB Diamond SR differs between D.5 (2.6–2.9) and Table 6 (9.0). "
                       "D.5 declares a different protocol without saying how, so this is recorded as an unexplained "
                       "gap. No rating change; the main aggregates recompute exactly.",
             "evidence_ids": ["opus:O04", "opus:O05", "opus:O06"], "score_impact": "none"},
            {"field_path": "assessment.unresolved (main-table knowledge state)", "sol_value": "not recorded",
             "son55_value": "noted as unstated", "final_value": "online updating on the evaluated stream implied",
             "reason": "The full system is contrasted with a frozen 'Static Store', and Algorithm 1 returns an updated K "
                       "per task (opus:O02, opus:O03). Its 37.13 exceeds the 400-episode frozen 35.02 (opus:O05). So the "
                       "main-table gains include online learning on the evaluated tasks. That is counted under E.holdout.",
             "evidence_ids": ["opus:O02", "opus:O03", "opus:O05"], "score_impact": "none (counted in E.holdout)"},
            {"field_path": "expectations[local:2603.13131-2/-3].id", "sol_value": "local-2 = seeds; local-3 = cost",
             "son55_value": "local-2 = held-out accumulation; local-3 = LLM curator validation",
             "final_value": "local-2 = seeds (merged with son55 local-1); local-3 = cost; local-4 = held-out; local-5 = curator",
             "reason": "A4 hidden ID collisions with equal status ('partial'), so the mechanical diff missed them. "
                       "Renumbered and merged.", "evidence_ids": ["sol:E022", "son55:E009"], "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–5 and Appendices A–E first. Initial view: in scope, a strong "
                                                   "design with rich ablations (G/M/X 3). Main-table arithmetic "
                                                   "recomputes. Concerns: the Table 6 'held-out' set equals the whole "
                                                   "hard set, the main-table KB state is unstated, Static Store's rising "
                                                   "curve, no variance, and Fig. 4 is image-only. Expected Eh 2, Es 1, "
                                                   "Ec 3, Ecost 2.",
            "integrity_checks": "Both seats a1 on 2603.13131v3, material sha 7b5489e3…; canonical seat hashes equal "
                                "conflicts.json; both completed 15+31 identification with valid parents.",
            "core_claim_check": "Retained-knowledge gains are supported at author-report level (frozen KB, alternative "
                                "stores, cross-tier transfer). Held-out independence and main-table protocol are "
                                "weaker than stated. claim_support scoped.",
            "rating_agreement": "Seven items agree and were re-checked (Em/Ec with notes). E.holdout → son55.",
        },
    }

    # =========================================================== 2603.13258 MemCoder (Δ5)
    p = "2603.13258"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "we strictly restrict the agent at test time to retrieve only historical experiences created prior to the corresponding test issue.",
                    "§4.1 Metrics and Baselines",
                    "Evaluated memory = LLM-structured human commits that predate each issue."),
            opus_ev(p, "O02", "This new commit will be learned in Stage 1 next run", "Appendix B, Algorithm 1, Stage 3",
                    "Internalization happens only after human review and a later sync. No experiment runs a stream in "
                    "which agent-produced, human-validated entries are written and then retrieved. The evaluated store "
                    "therefore contains no retained self-change.", kind="our_inference"),
            opus_ev(p, "O03", "The initial topk value is 8", "Appendix C, Refining Agent prompt",
                    "The deployed default initial top-k."),
            opus_ev(p, "O04", "as top-k exceeds 8, the rate of performance gain diminishes", "§4.3 Retrieval Quantity (Fig. 5)",
                    "The default sits at the knee of a sweep run on a 200-instance subset of the evaluated SWE-bench "
                    "Verified set (son55:E012), and the subset is part of the 500 reported. The selection set overlaps "
                    "the test set.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning",
            "supporting": ["decompose_and_delegate"],
            "matches": [
                smatch("son55", p, "adapt_via_conditioning",
                       reason="Both seats: retrieved structured precedents condition a frozen LLM at inference (C03 "
                              "reference-substrate branch)."),
                smatch("son55", p, "decompose_and_delegate",
                       reason="Opus confirms son55's supporting match. The primary agent delegates verification to a "
                              "Refining Sub-agent that writes and executes reproduction tests and returns a checklist "
                              "(execution as the sound solver). It is a separate operation with its own ablation (w/o DSR), "
                              "following the run convention for sub-agent + executor designs (C25)."),
            ],
            "outside_taxonomy": False,
            "reason": "Retrieval conditioning (primary) and delegated, execution-checked verification (supporting).",
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "index_experience_for_reuse", "H03"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H05"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0), pmap("son55", p, 1), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2603.13258-3"): "local:2603.13258-4"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "met",
                    "reason": "Opus (son55's value). w/o CR removes retrieval on the same backbone and scaffold "
                              "(son55:E007), which is the required isolation. Unmatched call budgets are an E.cost/"
                              "E.causality matter, not a missing isolation."},
                "rsi:index_experience_for_reuse/S5": {
                    "status": "met",
                    "reason": "Opus (son55's value) for the store as evaluated: removing commit retrieval drops 77.8→71.6 "
                              "and history-off gives 68.4. The untested write-back store is local-1's question."},
                "local:2603.13258-2": {
                    "status": "unmet",
                    "reason": "Opus (son55's value; sol's local-2 asks the same comparability question). The SOTA and "
                              "'efficiency per attempt' claims compare MemCoder pass@1/pass@2 runs with copied official "
                              "OpenHands pass@3 numbers on other backbones and scaffold versions. Nothing is rerun under "
                              "matched attempts, and no call/token budget is given. The pass@1 denominator (sol) is real "
                              "but does not make the comparison fair.",
                    "note": "Merged: sol local-2 and son55 local-2 are the same question."},
                "local:2603.13258-4": {"note": "A4: renumbered from son55 local-3 (single run / small ablation deltas)."},
            }),
        "claims": lambda c: add_counter(c, "C4", ["opus:O02"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Opus shared correction (both seats 'retained'). The evaluated memory contains only "
                                   "LLM-structured human commits made before each issue (opus:O01). No agent-produced, "
                                   "human-validated entry is written and later reused in any experiment (opus:O02). The "
                                   "gains come from a non-weight retrieval component (in scope, B-class), but the "
                                   "ladder's 'retained' requires a retained system change that improves later tasks, and "
                                   "none is evaluated.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Single-run, author-reported SWE-bench Verified gains on DeepSeek-V3.2 (68.4→77.8, "
                                         "342→389 of 500) from retrieving LLM-structured, time-restricted repository "
                                         "commit history plus a test-writing refining sub-agent. Structured beats raw "
                                         "commits (73.0→76.4). The self-internalization / co-evolution loop is untested, "
                                         "and SOTA comparability is not established (mixed pass@k, copied baselines).",
            "unresolved": ["Any stream experiment of write-back (internalization) effects.",
                           "Enforcement of the temporal cutoff; backbone contamination.",
                           "top-k default chosen on a test subset (opus:O03, opus:O04).",
                           "Matched-attempt baselines; tokens/calls; Figures 3–5 values image-only."],
        },
        "ratings": {
            "G": kept("son55", p, "G", "Both seats 2; re-checked. Repository history as a source of tacit conventions is "
                      "a real, named fixed object. Neighbours cited are mostly generic memory work (A-mem, MemInsight, "
                      "MemoryBank), SWE-specific experience-memory lines are not compared, and the internalization gap "
                      "rests on no measured failure.", ["son55:E002", "son55:E003", "sol:E003", "son55:E017"]),
            "M": R("resolved", 2, "Opus sides with son55. The tested chain (commit → LLM sextuple → k+p index → "
                   "agent-issued dual-stage retrieval → test-writing refiner) is concrete. Raw vs structured gives a "
                   "discriminating prediction (son55:E009). But the domain's M criterion is the feedback → candidate → "
                   "accept → write-back → reuse chain. Here the knowledge source is human commits, not the agent's own "
                   "execution feedback (son55:E017), and write-back is a bare set union after an unspecified human "
                   "review (son55:E006, son55:E014), with no admission or error control. The loop that carries the "
                   "central co-evolution claim is the weakest part. sol's 3 credits the retrieval pipeline's "
                   "reconstructability.", ["son55:E006", "son55:E009", "son55:E014", "son55:E017", "sol:E005"],
                   ["son55:E009"]),
            "X": kept("son55", p, "X", "Both seats 2; re-checked. The retrieval pipeline, Algorithm 1 and the full "
                      "Refining prompt are reconstructable. The write-back gate, merge/conflict/retirement, versioning, "
                      "human-review protocol and hyperparameters are absent, and next-run use is never traced.",
                      ["son55:E006", "son55:E013", "son55:E014", "sol:E023"]),
            "E.measurement": kept("son55", p, "E.measurement", "Both seats 3; re-checked. Resolution comes from official "
                                  "SWE-bench tests via sb-cli (son55:E015), and every reported percentage matches its "
                                  "count out of 500 (389, 394, 419, 382, 365, 358, 342). The generated-test verifier is "
                                  "internal only; leaderboard pass@k mixing is a causality matter.",
                                  ["son55:E015", "son55:E007", "sol:E012", "sol:E014"]),
            "E.causality": kept("son55", p, "E.causality", "Both seats 2; re-checked. Cumulative ablations and the "
                                "none/raw/structured comparison isolate retrieval and structuring (son55:E007, "
                                "son55:E009). The evolution claim has no test, baselines are copied pass@3 numbers "
                                "(son55:E010), there are no alternative memory/retrieval methods, and refiner/retrieval "
                                "calls are unmatched.", ["son55:E007", "son55:E009", "son55:E010"], ["son55:E010"]),
            "E.holdout": kept("son55", p, "E.holdout", "Both seats 2; re-checked with an Opus addition. A temporal "
                              "restriction to commits before each issue is stated (opus:O01) but not audited. The default "
                              "initial top-k=8 (opus:O03) sits at the knee of a sweep run on a 200-issue subset of the "
                              "same test set (opus:O04), so the selection set overlaps the test set (precedent r12b ARISE: "
                              "anchor 2). Backbone contamination is unexamined.",
                              ["son55:E004", "opus:O01"], ["opus:O03", "opus:O04", "son55:E012"]),
            "E.statistics": kept("son55", p, "E.statistics", "Both seats 1 (A2 ladder). Instance counts and negative "
                                 "top-k boundaries are reported. There is a single pass@1 run with no intervals, and the "
                                 "DSR effect is 7/500.", ["son55:E011", "son55:E007", "son55:E012"]),
            "E.cost": kept("son55", p, "E.cost", "Both seats 1; re-checked. Retrieval frequency and retrieved-entry "
                           "counts are measured on a 200-issue sweep (Fig. 4, image-only values). There is no token, "
                           "dollar or latency figure, no memory-construction or human-review cost, and no "
                           "matched-attempt baselines.", ["son55:E012", "son55:E016"], ["son55:E010"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text with Appendices A–C read. In scope as a B-class non-weight memory component "
                  "(LLM-structured commit memory with agent-issued retrieval) designed for a write-back loop. That loop "
                  "itself is untested. claim_type system_method. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "figure_dependence": "Figures 3–5 (leaderboard, top-k curves) are image-only; used only as the text describes "
                             "them. All counts come from Tables 1–2.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["adapt_via_conditioning", "C03"], ["decompose_and_delegate", "C25"]],
                "C03 agrees. C25 is added as supporting: delegated, execution-checked verification by a sub-agent is a "
                "distinct operation with its own ablation.", ["son55:E005", "son55:E007", "sol:E023"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["index_experience_for_reuse", "H03"],
                 ["index_experience_for_reuse", "H05"]],
                "H00 and H03 agree. H05 is added (fit partial): retrieval is an agent-issued, reasoning-time call with "
                "progressive top-k (son55:E018), which is H05's 'explicit reasoning-time request'. The gated-vs-always "
                "comparison is missing.", ["son55:E018", "sol:E007"], NOSCORE),
            XC(p, "local:2603.13258-2", "son55", "unmet",
               "Same question in both seats (comparability of the SOTA/efficiency claims). The baselines are copied "
               "pass@3 numbers with other backbones, and no matched attempts or budgets exist, so unmet. sol's "
               "'partial' credited the pass@1 denominator.", ["son55:E010", "sol:E016"]),
            XC(p, "local:2603.13258-3", "sol", "partial",
               "A4 hidden collision: sol's local-3 asks about the generated-test verifier (partial: the prompt requires "
               "base-vs-patched reproduction, but there is no false-positive audit). son55's asks about single-run "
               "statistics and moved to local-4 (unmet).", ["sol:E023", "sol:E012"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "w/o CR isolates the retrieval signal on the same backbone and scaffold. Unmatched call budgets are "
               "counted under E.cost/E.causality.", ["son55:E007", "son55:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: raw commits are a cheaper comparator; there is no BM25 or other memory system on the same "
               "scaffold.", ["son55:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: cumulative removals only; ER-only and the reranker are not isolated.", ["son55:E007", "son55:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "unmet",
               "Verified: one benchmark (Python repositories).", ["son55:E011"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "Verified: no token, call or dollar cost for the sub-agent and retrieval.", ["son55:E012", "son55:E016"]),
            XC(p, "rsi:abstract_experience_into_guidance/F5", "son55", "unmet",
               "Verified (failure present): the evaluated store derives from human commits, not the agent's outcomes. "
               "This is also the basis of the evidence_level correction.", ["son55:E017", "opus:O01"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Kept as a check question. No retirement or size bound; admission is by human review.",
               ["son55:E006", "son55:E014"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "met",
               "The historical store is certified by removal (w/o CR 71.6, w/o all 68.4). The write-back store is "
               "local-1's question (unmet in both seats).", ["son55:E007"]),
            res("ratings.M", *C(p, "ratings.M"), "son55", 2,
                "See ratings.M. The tested chain is concrete, but the write-back that defines the paper's claimed "
                "mechanism is a bare set union after unspecified human review, and the store is not built from the "
                "agent's own feedback. 'Key assumptions weak' = anchor 2.",
                ["son55:E006", "son55:E014", "son55:E017"], "−5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level", "sol_value": "retained", "son55_value": "retained",
             "final_value": "task",
             "reason": "Both seats treated the existence of a stored memory as retention. EVIDENCE.md's 'retained' needs "
                       "a retained change that improves later tasks. Here the evaluated store is pre-issue human commit "
                       "history structured by an LLM (opus:O01). No agent-generated, human-validated entry is ever "
                       "written and then retrieved (opus:O02); both seats' own C3/C4 say the internalization loop is "
                       "untested. This is the 'retained a modification' vs 'shown a retained improvement' confusion.",
             "evidence_ids": ["opus:O01", "opus:O02", "son55:E017", "sol:E022"], "score_impact": NOLVL},
            {"field_path": "expectations[local:2603.13258-3].id", "sol_value": "local-3 = generated-test verifier (partial)",
             "son55_value": "local-3 = single-run statistics (unmet)",
             "final_value": "local-3 = verifier; local-4 = statistics",
             "reason": "A4 hidden ID collision; renumbered.", "evidence_ids": ["sol:E023", "son55:E011"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text and Appendices A–C first. Initial view: in scope "
                                                   "as a memory component. The evaluated store is human commit history; "
                                                   "the write-back loop has no experiment (evidence_level task, not "
                                                   "retained). Retrieval/structuring ablations are concrete. top-k is "
                                                   "tuned on a test subset. Single run. Expected G 2, M 2, X 2, Em 3, "
                                                   "Ec 2, Eh 2, Es 1, Ecost 1.",
            "integrity_checks": "Both seats a1 on 2603.13258v1, material sha f55a24f1…; canonical seat hashes equal "
                                "conflicts.json; both completed 15+31 identification with valid parents.",
            "core_claim_check": "The co-evolution claim is unsupported (no stream experiment). The narrow retrieval claim "
                                "is supported at author-report level. evidence_level corrected to task.",
            "rating_agreement": "Seven items agree and were re-checked (Eh with the top-k selection addition). M → son55.",
        },
    }

    return S
