"""Opus rulings for r19a a1 (data only; consumed by _build.py)."""
import copy


def batch_notes():
    return [
        "2605.06614 SkillOS (seat Δ6.25): final 66.25, between the seats (sol 70.0, son55 63.75). X → sol 3: the "
        "insert/update/delete interface, BM25 top-5 read, write-back after every task and Table 4 hyperparameters "
        "are given; there is no gate, rollback or size bound. E.causality → son55 2: store-off (No Memory), "
        "untrained-curator (SkillOS-base) and Gemini-curator arms exist, but there is no frozen-repo or "
        "no-experience arm, no RL-curator neighbour, and the Table 3 ablations are single-run on ALFWorld only, "
        "with drops (2.6/1.2/3.9) inside the main-table SD (±4.6). E.holdout → sol 2: the test-time stream "
        "protocol (order, reset, number of passes, use of task-type grouping) is never stated (opus:O01), ALFWorld "
        "uses valid_seen (opus:O04), and there is no frozen-store evaluation. The H26 card's step 4 and failure "
        "mode name exactly this case: online accumulation during evaluation. A2: the stream-protocol defect is "
        "scored once, in E.holdout, not again in X. Paper facts recorded: the training reward is self-judged by the "
        "frozen executor (opus:O02); '+7.9 vs base' is 8.1 in Table 1 (opus:O03); Table 4's KL 0.001 contradicts "
        "'we discard the KL term' (opus:O05). These are ≤0.2-pp secondary mismatches and the headline numbers check "
        "out, so the run's E.measurement cap is not applied. RS → son55 self_supervised_signal_engineering (sub "
        "null) plus adapt_via_conditioning (sub null; C03 needs a reader trained to read the schema, and the executor "
        "is frozen).",
        "2605.06822 SHARP (Δ1.25): final 68.75 = sol. E.measurement → sol 2. The 5-bps charge is applied to entries "
        "only, while the random null counts a flip as two trades (sol:E014). Appendix A promises baseline "
        "implementations but describes only Random/Momentum/MeanRev/Static, so FinCon, FinHEAR and Lopez-Lira are "
        "undocumented (opus:O02, son55:E019). §4.2 calls the remaining baselines 'economically negligible', but Table "
        "1 gives FinHEAR-4o a 3-sector mean of 11.1% and FinCon-4.1 9.0%, and SHARP-4.1 (13.4%) is below FinCon-4o "
        "(15.9%) (opus:O01). Run convention: text–table contradiction caps the item at 2. E.causality → sol 3. "
        "Static (no evolution) is run on all four backbones: it is below Evo in all 6 sector cells for the 4o/4.1 "
        "backbones and in both 3-sector averages for Qwen/Llama. A2 is a purpose-built alternative-optimizer arm "
        "(free-form rewrite with the same init, budget and gate) and A1 removes attribution. The remaining gaps are "
        "single-sector ablations and no gate-off arm. Single runs are scored in E.statistics (A2 rule), not here. RS "
        "→ sol generative_process_redesign: the fixed component is the free-text mutation operator/representation. "
        "son55 itself rated structural_prior_encoding as weak.",
        "2605.08083 AutoTTS (Δ3.75): final 65.0 = sol. G → sol 3. The bottleneck is concrete: costly online "
        "evaluation, hyperparameter blow-up and uninformative scalar feedback, each demonstrated by the paper's own "
        "replay/β/trace ablations. The TTS lineage (SC/ASC/ESC/Parallel-Probe) is compared empirically and the "
        "discovery lineage (Meta-Harness/ADAS) is named. son55's main G reason, that automated tuning of existing "
        "controllers is not considered, is an alternative-optimizer control. It is scored in E.causality=2 (A2 "
        "rule), not again in G. Shared ratings confirmed: Table 3's 'Avg' includes the search set but the text calls "
        "it held-out (sol:E016/E017). At 4B/8B, ASC dominates some AutoTTS operating points (son55:E024), "
        "contradicting the figure-only 'consistently stronger frontier' (opus:O01). The $39.9 excludes the 128-"
        "trajectory pre-sampling. sol's rs_pattern.primary was written as a {main_id, sub_id} object; it is read as "
        "generative_process_redesign (a schema variance, not blocking). RS → son55 reframe_as_solvable_object "
        "primary + sol generative_process_redesign supporting. Domain → son55 H14 (the card names replay "
        "evaluators and control-policy genomes) + sol H17 (frozen offline design). H12 (low) is dropped.",
        "2605.08374 MemQ (Δ5): final 66.25, below both seats (sol 68.75, son55 73.75). E.causality → sol 2. The "
        "γ=0/λ=0 arms are clean, but they cover 3 of 5 benchmarks with 35–116-task evaluation sets. The headline "
        "MemQ>MemRL margins are confounded with configuration: initial Q is 0.66 vs 0 on DSBench/AutomationBench, "
        "the two benchmarks the paper cites for its largest gains, and Table 6 shows initialization moves LCB eval "
        "by 17 pp; w_s/w_q and batch size also differ (son55:E026, son55:E015). E.cost → sol 2: token totals cover "
        "1 of 8 benchmarks, the gap is within one SD, and DAG upkeep is only asymptotic. Shared correction: "
        "E.measurement 3 → 2. Table 11 gives MemQ-LCB w_s/w_q = 0.4/0.6, yet the reported held-out 51.43 equals the "
        "Table 7 row for 0.6/0.4, which §5.4 calls 'the reported mixed ranking' (opus:O01). The 0.4/0.6 row is "
        "48.57, and Table 6/7's Final/CSR (61.79/67.62) differ from Table 2 (64.76/69.76). BFCL eval is 62.83 in "
        "Table 6 vs 62.38 in Table 1. The Table 3 coverage gaps are cited as 'Table 4' (opus:O03). Domain → son55 "
        "H29 + H03. RS → reframe_as_solvable_object only; C03 is not kept (no reader is trained).",
        "2605.08399 CoCoDA (Δ10, adjudicated item by item): final 50.0, below both seats (sol 56.25, son55 66.25). "
        "G → son55 2: the trained libraries hold 205–382 tools (Table 5) and accuracy plateaus by ~400, so the "
        "context-budget bottleneck that motivates TDR does not bind in the regime the method produces. The "
        "'missing quadrant' is the paper's own taxonomy (the H-Mem precedent). M → sol 2. The formal support for the "
        "design is invalid. Theorem 1 infers o(C_flat) from a limsup ratio ≤ α1α2 < 1, and L2 still ranks all α1·n "
        "L1 survivors. Corollary 5's log-depth argument fails on a chain (sol:E031). The Theorem 4 library step "
        "assumes LLM-judged L3 checks certify equivalence. The saved-call reward can credit unnecessary composites, "
        "which the authors concede (sol:E025). X → sol 2: the admission gate is self-contradictory. R_res is "
        "binary {0,1} (Table 4), yet the ρ sweep reports 419/364/207 retained composites at ρ = 0.5/0.8/1.0, "
        "which is impossible on fixed binary rewards (sol:E019, sol:E026). Equivalence validation is an LLM "
        "prompt, and the EvalPlus query stream is undefined. E.holdout → sol 2. EvalPlus has no training split, "
        "but an EvalPlus library was evolved (Table 5/6). λ and k2 were chosen on GSM8K test accuracy: Table 8's "
        "λ=0.20 value equals the Table 1 test score, and no validation split exists (opus:O02, opus:O03, opus:O05). "
        "E.cost → sol 2: no baseline or teacher bill, no matched budget, and Figure 2(b)'s 1,600-node regime is "
        "never produced by training (opus:O04). Shared correction: E.measurement 3 → 2. Table 2's Δ column does "
        "not equal the mean of its own per-benchmark drops: −1.97 vs −1.79 for TDR, −4.46 vs −4.64, −5.01 vs −5.18 "
        "(opus:O01). The appendix says the all-off variant equals a ReTool-style planner, yet it sits 3–5 pts below "
        "ReTool (son55:E012). Tool counts disagree: 1,873 vs 309, and 42 vs 14–22 primitives (son55:E020). "
        "E.causality=2 is confirmed. CoCoDA beats ReTool in all 24 cells, but by 0.1–1.6 pts with SD ≤ 0.4–0.7, and "
        "parity (teacher SFT, tool inventory) is unstated. RS → son55 decompose_and_delegate C25 + "
        "structural_prior_encoding (sub null; C13 requires message passing over the wiring). Domain → union "
        "H08 + H04 + H28.",
        "A4 hygiene. Same-ID collisions on different questions were renumbered: 06614 son55 local-2 → local-5; "
        "08083 son55 local-1 → local-5; 08374 son55 local-1 → local-4; 08399 son55 local-1 → local-7 and local-3 → "
        "local-8. Same-question pairs were merged: 06614 local-1; 06822 son55 local-1 → local-5 and local-2 → "
        "local-3; 08083 son55 local-2 → local-2 and local-3 → local-1; 08374 son55 local-2 → local-3; 08399 "
        "local-2.",
        "Expectations from cards not kept as pattern matches stay as check questions with a note; they never score "
        "directly. These are evidence_gated_retention S2 (06614), structural_prior_encoding RE-3/RE-4 (06822) and "
        "attribute_and_patch_incumbent H12 S3 (08083).",
        "Figure dependence: SkillOS Figures 3–6 (cross-task transfer matrix, curator behaviour), SHARP Figure 3, "
        "AutoTTS Figures 3–4, MemQ Figures 4–5 (γ/λ sweeps; ablation values are given in the text) and CoCoDA "
        "Figures 2–3 are image-only. Only values stated in text or tables are used.",
        "No material requests. The seats' requests for neighbour originals (ATLAS, Meta-Harness, MemRL, ReTool, "
        "DreamCoder/TroVE, the RL curators Wang 2025a/Ye 2026) are non-blocking.",
        "Card revision proposal (stage end, not applied): H26 step 4. When a paper's claimed setting is streaming "
        "test-time evolution with only self-judged signals (SkillOS), the card should require the test-stream "
        "protocol (order, reset, passes, use of grouping metadata) as a reporting item in addition to the "
        "frozen-store test.",
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

    def RC(p, k, dec, final, reason, ev=(), impact=""):
        return res(f"ratings.{k}", *C(p, f"ratings.{k}"), dec, final, reason, ev, impact)

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

    def renum(old, new):
        return {"note": f"Renumbered from son55 {old} to {new}: A4 hidden ID collision, because sol used {old} for a "
                        "different question."}

    def merged(other):
        return {"note": f"Merged with son55 {other} (same question; A4 same_supported_fact)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on *_pattern.matches)."}

    def rr(v):
        return {"status": "resolved", "rating": v}

    # =========================================================== 2605.06614 SkillOS
    p = "2605.06614"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "We consider a streaming test-time setting", "§3.1",
                    "The evaluated setting is a test-time stream in which the SkillRepo keeps evolving. The full "
                    "text never states the test stream order, whether the repo is reset per seed or benchmark, the "
                    "number of passes, or whether test tasks are grouped by task type as they are in training "
                    "(App B.2). Grouped order would favour within-stream reuse.", kind="our_inference"),
            opus_ev(p, "O02", "is obtained via LLM-as-a-judge with the frozen agent executor", "§4.1 Implementation",
                    "The outcome signal the curator sees, and by the shared 𝟙(ξ) notation the r_task reward, is "
                    "judged by the frozen executor itself. This supports the 'manufactured signal' (C08-family "
                    "parent) reading of the RS card. At test time no gold label enters the store."),
            opus_ev(p, "O03", "with Qwen3-8B for ALFworld, compared with", "§4.2",
                    "The text says +7.9 over SkillOS-base with the Qwen3-8B executor, but Table 1 gives "
                    "61.2 − 53.1 = 8.1. The stated 3.1-step saving for Gemini is 17.7 − 14.8 = 2.9 in the table. "
                    "Both mismatches are ≤0.2 in secondary derived statements; the headline 55.7 → 61.2 (+9.8% "
                    "relative) is correct.", kind="our_inference"),
            opus_ev(p, "O04", "valid_seen tasks for the test set", "App B.3.1 ALFWorld",
                    "The ALFWorld evaluation uses the 140 valid_seen tasks (seen rooms), not valid_unseen."),
            opus_ev(p, "O05", "we discard the KL term in GRPO to encourage policy exploration", "§3.2.2",
                    "This contradicts Table 4's 'KL loss Coef 0.001' (sol:E018). It is a reconstructability "
                    "detail, not a measurement defect."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Opus. The load-bearing move is manufacturing a training signal for curation decisions that "
                      "have no per-decision label. Grouped task streams let later related tasks score earlier edits, "
                      "and the outcome signal is self-judged by the frozen executor (opus:O02) plus an LLM content "
                      "judge. That matches self_supervised_signal_engineering, with no C-sub reproducing the "
                      "grouped-stream credit move (son55). adapt_via_conditioning is kept as supporting with sub "
                      "null: the frozen executor adapts only through retrieved skills, but C03 requires an upstream "
                      "phase that teaches the reader the conditioning schema, and the reader here is frozen. sol's "
                      "generative_process_redesign is not kept: 'heuristic curation released as a free variable' "
                      "restates the RL-curator premise, not a generative-procedure component.",
            "matches": [
                smatch("son55", p, "self_supervised_signal_engineering", role="primary",
                       reason="Opus final: grouped-stream delayed credit plus self-judged outcome and judge-based "
                              "content reward is a manufactured signal for an unlabeled decision. Fit partial: "
                              "GRPO is standard and a composite proxy is added."),
                smatch("sol", p, "adapt_via_conditioning", role="supporting", sub_id=None, fit="partial",
                       reason="Opus: the executor-side adaptation is conditioning on retrieved Markdown skills without "
                              "weight updates. C03 dropped because no reader is trained to read the schema."),
            ],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "amortize_improver_into_trained_policy", "H26"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01")],
                           "unassigned": [],
                           "reason": "Both seats chose H26 + H01; no conflict. H26 is the boundary card, and SkillOS "
                                     "sits in its failure-mode description: the store accumulates online during "
                                     "evaluation, and there is no frozen-store test (step 4).",
                           "revision_proposals": ["H26 step 4: require the test-stream protocol (order, reset, "
                                                  "passes, grouping metadata) as a reporting item when the claimed "
                                                  "setting is streaming self-evolution (see batch notes).",
                                                  "son55: H26 step 3 can be met by reward-through-frozen-reader "
                                                  "without co-training (SkillOS)."]},
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": None,
            "domain": {"namespace": "rsi", "main": "amortize_improver_into_trained_policy", "sub": "H26"},
            "operation_correspondence": "The manufactured delayed signal (later related tasks scored by the "
                                        "frozen executor's own judgment) is H26's credit path: curation actions "
                                        "after task k are rewarded by tasks k+1..|G| that read the repo.",
            "necessary_conditions": "Grouped related tasks and a reader that consumes the store.",
            "differences": "The signal is partly a proxy (validity, judge, compression); the store is not frozen "
                           "before evaluation.",
            "evidence_ids": ["son55:E006", "sol:E004", "opus:O02"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.06614-2"): "local:2605.06614-5"},
            overrides={
                "local:2605.06614-1": {"reason": "Merged (same question in both seats: no content-level control "
                                                 "such as a frozen, shuffled or removed-skill arm, and no "
                                                 "RL-curator neighbour). Partial: store-off and untrained-curator "
                                                 "arms exist."},
                "local:2605.06614-5": {"status": "unmet",
                                       "reason": "Renumbered from son55 local-2 (A4 collision: sol's local-2 is the "
                                                 "holdout question). Revised from 'unknown': the complete text was "
                                                 "read. §4.1 promises tokens per reasoning problem, but Table 2 and "
                                                 "the rest of the text report only accuracy, steps and scores, so "
                                                 "the item is not reported.",
                                       "search_scope": ["full text incl. Tables 1–6 and Appendices A–F"]},
                "rsi:amortize_improver_into_trained_policy/S3": {
                    "status": "partial",
                    "reason": "Opus revised (sol challenged_with_evidence / son55 unmet). The writer is coupled to "
                              "the reader through the reward (later-task success through the frozen executor), but "
                              "they are not co-trained. The staleness risk the condition guards against does not "
                              "arise with a frozen reader. The frozen-reader choice is supported only by "
                              "author-reported cross-executor gains."},
                "rsi:evidence_gated_retention/S2": dropped_card("evidence_gated_retention"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O04"]), "C3", ["opus:O03"]),
        "assessment": assess("son55", p, [
            "Opus: the test-time stream protocol (order, reset, passes, grouping) is unstated (opus:O01).",
            "Opus: secondary text–table mismatches of ≤0.2 (opus:O03) and the KL contradiction (opus:O05)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3, confirmed. The bottleneck is specific: learning long-horizon "
                   "curation (update/delete) of a persistent skill store from delayed, indirect feedback. Named "
                   "neighbours: heuristic memory (ReasoningBank, MemP, run), skill-use RL (SkillRL, D2Skill) and "
                   "short-stream RL curators (Wang 2025a, Ye 2026), with the residual 'short-horizon supervision'. "
                   "Not 4: the RL-curator neighbours are neither run nor characterised beyond one sentence.",
                   ["son55:E002", "son55:E003", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Grouped streams make later related tasks score earlier "
                   "edits. Rollout-level GRPO over the whole curation sequence, plus a reward that excludes the "
                   "first (empty-repo) task, is a reconstructable answer to delayed credit, and grouped vs random "
                   "order is a checkable prediction. Weak points: the composite proxy terms (judge, compression), "
                   "the uniform token advantage, and the self-judged outcome (opus:O02).",
                   ["son55:E001", "son55:E006", "sol:E005", "son55:E013"], ["son55:E007", "opus:O02"]),
            "X": R("resolved", 3, "Opus = sol. The operation chain is reconstructable: insert/update/delete "
                   "function calls, ApplyOps after each task, BM25 top-5 read by the next task, prompts (App A) and "
                   "hyperparameters (Table 4). Not 4: no admission gate beyond call validity, no rollback, version "
                   "or size bound, and deletion is reported only as a share. Table 4's KL coefficient contradicts "
                   "the text (opus:O05). The unstated test-stream protocol is scored once, in E.holdout (A2), as in "
                   "the run's H-Mem precedent (static flow reconstructable, no gate → 3).",
                   ["sol:E002", "sol:E003", "son55:E004", "sol:E015"], ["son55:E025", "opus:O05"]),
            "E.measurement": R("resolved", 3, "Both seats 3, confirmed. The metrics are environment-native and "
                               "deterministic: ALFWorld goal-state SR (macro-averaged, steps counted over failed "
                               "episodes), the WebShop programmatic reward, math_verify and GPQA exact match. Not 4: "
                               "the self-judged curation signal is not validated, and there are two ≤0.2 "
                               "text–table mismatches in secondary statements (opus:O03). These do not touch the "
                               "headline values, so the run's contradiction cap is not triggered.",
                               ["sol:E012", "son55:E009", "son55:E022"], ["opus:O03", "son55:E024"]),
            "E.causality": R("resolved", 2, "Opus = son55. Relevant controls: No Memory (store-off), ReasoningBank "
                             "and MemP (heuristic curation), SkillOS-base (same model, prompt and interface, "
                             "untrained), SkillOS-gemini, and reward/grouping ablations. Not 3, for three reasons. "
                             "(1) There is no frozen-repo, shuffled-skill or no-experience arm, so 'the RL-trained "
                             "curator injects training-split priors' is not separated from 'it curates test-stream "
                             "experience'. (2) The RL-curator neighbours are not run. (3) The Table 3 ablations are "
                             "single-run on ALFWorld only, and their drops (2.6/1.2/3.9) sit inside the main-table "
                             "SD of ±4.6. Unequal training budget is scored in E.cost.",
                             ["son55:E011", "son55:E013", "son55:E014", "sol:E011"],
                             ["son55:E012", "son55:E015"]),
            "E.holdout": R("resolved", 2, "Opus = sol. The curator is trained on train splits and evaluated on "
                           "official test splits, with unseen executors (Qwen3-32B, Gemini-2.5-Pro, "
                           "Gemini-3.1-Flash-Lite) and cross-task transfer (Fig 3, image-only). Not 3: the repo "
                           "evolves online on the evaluation stream, and the stream protocol (order, reset, passes, "
                           "task-type grouping) is never stated (opus:O01). There is no frozen-store evaluation on "
                           "unseen tasks, which is H26 step 4 and the card's leading failure mode. ALFWorld is "
                           "valid_seen only (opus:O04), and checkpoint selection is not stated.",
                           ["sol:E013", "son55:E010", "son55:E023", "son55:E021"],
                           ["opus:O01", "opus:O04", "son55:E019"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2). Main tables report mean ± SD over "
                              "3 runs, without stating which randomness the runs cover. There is no CI or "
                              "significance test, the ablations have no SD, and several margins are inside the SD "
                              "(e.g. ALFWorld 61.2±4.6 vs 55.7±3.1).",
                              ["sol:E006", "son55:E016"], ["son55:E024"]),
            "E.cost": R("resolved", 2, "Both seats 2, confirmed. Reported: 16 H100s for 3/2.5/5 training days, step "
                        "counts, and a shared retrieval/step budget across methods. Missing: curator inference and "
                        "judge tokens, the promised reasoning token counts (local-5 unmet), and a matched-budget "
                        "prompted-curator baseline against the multi-day RL training.",
                        ["sol:E009", "son55:E017", "sol:E010"], ["son55:E018"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (body, Tables 1–6, Appendices A–F). In scope under A3 bullet 2: the "
                  "evaluated retained object is the Markdown SkillRepo, read by a frozen executor; the curator's RL "
                  "weights are the improver. claim_type component_training (both seats). All eight items resolved; "
                  "no unresolved scoring dispute.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (A3 bullet 2): retained object = SkillRepo read at test time by a frozen executor; curator "
              "weights are the improver.",
        "improver_check": "not claimed; the curator is trained by fixed GRPO and is not itself edited by the loop.",
        "figure_dependence": "Figures 3–6 (cross-task transfer, curator operations, skill usage) are image-only; "
                             "the qualitative text claims are not credited with magnitudes.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "See rs_pattern.reason: the core move is a manufactured delayed signal (opus:O02).",
                ["son55:E006", "opus:O02"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["self_supervised_signal_engineering", None], ["adapt_via_conditioning", None]],
                "son55's primary is kept. sol's adapt_via_conditioning is kept as supporting with sub null (C03 needs "
                "a trained reader of the schema). sol's generative_process_redesign is dropped.",
                ["son55:E006", "sol:E003", "son55:E020"], NOSCORE),
            XC(p, "local:2605.06614-2", "sol", "partial",
               "Different questions under one ID (A4). sol's local-2 (holdout: official splits, no frozen-store test) "
               "is verified partial. son55's local-2 (token counts) moves to local-5 and is revised to unmet after "
               "complete search.", ["sol:E013", "son55:E018"]),
            XC(p, "local:2605.06614-3", "sol", "partial",
               "sol-only question (statistics). Verified: 3-run SD, no CI or test.", ["sol:E006"]),
            XC(p, "local:2605.06614-4", "sol", "partial",
               "sol-only question (cost). Verified: training days reported, curator/judge tokens are not.",
               ["sol:E009"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "met",
               "son55-only (card kept). Cross-executor and cross-task transfer are reported, with the magnitude for "
               "the latter image-only.", ["son55:E010", "son55:E021"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-5", "son55", "partial",
               "son55-only. Training days are reported; inference curation cost is not.", ["son55:E017"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "sol", "partial",
               "sol-only. Explicit edit operations and a compression reward, but no hard bound or rollback.",
               ["sol:E002", "sol:E014"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "sol", "unmet",
               "sol-only. No execution or regression gate on edits; call validity is not content reliability.",
               ["sol:E014"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/F4", "son55", "partial",
               "son55-only. Task outcome flows through the reader, but validity, judge and compression proxy terms "
               "are added, and the proxies are shown to matter (Table 3).", ["son55:E007", "son55:E014"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/H26-step4", "son55", "partial",
               "son55-only. Splits are official, but the store evolves on the evaluation stream with an unstated "
               "protocol (opus:O01). Scored in E.holdout=2.", ["son55:E019", "opus:O01"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/H26-step5", "son55", "partial",
               "son55-only. Trained-vs-prompted curator arms exist, but there is no store-frozen or shuffled-skill "
               "arm.", ["son55:E011"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S1", "son55", "partial",
               "son55-only. The reward is mean later-task success with a GRPO group baseline, not a delta against a "
               "no-memory reference.", ["son55:E006"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S3", "revised", "partial",
               "See the expectation override. Coupled through the reward, not co-trained. Neither 'challenged' "
               "(sol) nor 'unmet' (son55) fits, because coupling via a frozen reader is half of the condition.",
               ["sol:E010", "son55:E020", "son55:E006"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "son55-only. Kept as a check question (card not a match): no admission test or rollback.",
               ["son55:E025"]),
            RC(p, "X", "sol", rr(3), "See ratings.X. son55's 2 relied partly on the unstated test protocol, which "
               "is scored in E.holdout (A2).", ["sol:E003", "son55:E004"], "+5.0 vs son55"),
            RC(p, "E.causality", "son55", rr(2), "See ratings.E.causality. sol itself lists the missing content "
               "intervention and RL-curator comparison.", ["son55:E012", "son55:E015", "sol:E011"],
               "−3.75 vs sol"),
            RC(p, "E.holdout", "sol", rr(2), "See ratings.E.holdout. son55 lists the same gaps (test stream also the "
               "adaptation stream, unspecified order/reset, valid_seen) but rated 3. H26 step 4 makes the "
               "missing frozen-store test the decisive item.", ["sol:E013", "opus:O01", "opus:O04"],
               "−2.5 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text first. RL-trained curator, non-weight "
                                                   "SkillRepo read by a frozen executor, so in scope. Solid "
                                                   "store-off and untrained-curator controls, but online test-stream "
                                                   "evolution with an unstated protocol, single-run ablations, and "
                                                   "small secondary text–table mismatches. Expected mid-60s.",
            "integrity_checks": "Both seats a1 on 2605.06614v1, material sha a9d7a649…; canonical seat hashes equal "
                                "conflicts.json. son55's top-level status is an object {status, reason} (schema "
                                "variance, normalised by rv2).",
            "core_claim_check": "Tables 1–3 and 6 re-read; the headline 55.7 → 61.2 and the step reductions were "
                                "recomputed (opus:O03).",
            "shared_error_review": "Shared G/M/E.measurement/E.statistics/E.cost confirmed. Neither seat recorded the "
                                   "two small arithmetic mismatches (opus:O03); they are below the run's "
                                   "contradiction cap.",
            "rating_agreement": "X and E.holdout = sol; E.causality = son55. Final 66.25.",
        },
    }

    # =========================================================== 2605.06822 SHARP
    p = "2605.06822"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "The remaining baselines exceed the Random null but remain economically negligible",
                    "§4.2",
                    "Contradicted by Table 1. The 3-sector means are FinHEAR-4o (22.8+9.2+1.2)/3 = 11.1% and "
                    "FinCon-4.1 (8.5+10.0+8.6)/3 = 9.0%, neither negligible and neither mentioned. SHARP-4.1's "
                    "3-sector mean (13.4%) is below FinCon-4o (15.9%). The verified averages are SHARP-4o 20.9/1.83, "
                    "Static-4o 0.6/0.09, SHARP-4.1 13.4/0.87 and Static-4.1 −4.4/−0.36.", kind="our_inference"),
            opus_ev(p, "O02", "baseline implementations, hyperparameters, and computational resources are deferred "
                              "to Appendix", "§4.1",
                    "Appendix A describes only Random L/S, Momentum, Mean Reversion and Static. The adaptation, "
                    "tuning and training windows of Lopez-Lira, FinCon and FinHEAR are never given (son55:E019)."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus = sol. The paper's move targets the representation and mutation operator of an "
                      "iterative optimizer: a free-text prompt rewritten wholesale becomes a bounded set of "
                      "condition–action rules edited atomically. That operator was conventionally fixed in "
                      "prompt-optimization loops, and here it is treated as a design variable. son55's "
                      "structural_prior_encoding is not kept (son55 itself rated it weak): no known invariant of "
                      "the market is encoded, and locality of edits is an interface choice, not a symmetry or "
                      "topology prior.",
            "matches": [smatch("sol", p, "generative_process_redesign", role="primary")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "attribute_and_patch_incumbent", "H10"),
                                       dmatch("sol", p, "evidence_gated_retention", "H31")],
                           "unassigned": [],
                           "reason": "Both seats chose H10 + H31 (medium); no conflict. H10: one rule document is "
                                     "rewritten from aggregated error diagnosis and gated on a disjoint validation "
                                     "window. The card's step 1 (collect successes) is not followed.",
                           "revision_proposals": ["sol: H31 at medium, and note the gate is non-statistical."]},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.06822-1"): "local:2605.06822-5",
                    ("son55", "local:2605.06822-2"): "local:2605.06822-3"},
            overrides={
                "local:2605.06822-5": {"reason": "Merged (sol local-5 + son55 local-1: is the P&L measurement "
                                                 "credible?). Partial: O2O execution, a news cutoff and a "
                                                 "1000-trial cost-aware null are good. Entry-only vs flip cost "
                                                 "accounting is inconsistent (sol:E014), slippage and impact are "
                                                 "omitted, the LLM baselines are undocumented (opus:O02), and "
                                                 "'remaining baselines negligible' is contradicted by Table 1 "
                                                 "(opus:O01)."},
                "local:2605.06822-3": {"reason": "Merged (sol local-3 + son55 local-2: statistics). Partial for the "
                                                 "broad question: 3 windows, 122 days and negative cells are "
                                                 "reported. The narrower item son55 asked about (repeated evolution "
                                                 "runs, intervals) is absent, which is why E.statistics=1."},
                "rs:structural_prior_encoding/RE-3": dropped_card("structural_prior_encoding"),
                "rs:structural_prior_encoding/RE-4": dropped_card("structural_prior_encoding"),
            }),
        "claims": lambda c: add_counter(c, "C2", ["opus:O01", "opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: the 'remaining baselines negligible' prose is contradicted by Table 1 (opus:O01).",
            "Opus: LLM-baseline implementations are undocumented (opus:O02)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3, confirmed. The bottleneck is concrete: credit assignment for "
                   "free-form prompt optimizers under noisy, delayed P&L. Named neighbours are ATLAS/OPRO, FinCon "
                   "and GEPA/MIPRO, and the failure is reproduced in-paper (A2). Not 4: the prompt-optimizer "
                   "neighbours are not run, and 'inevitably leading to drift' is over-general.",
                   ["son55:E001", "son55:E002", "sol:E015"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Rule-ID localisation, cross-sample diagnosis over the "
                   "20 worst days with recurrence ≥3, ≤3 atomic edits and a disjoint validation gate are a coherent, "
                   "distinguishable alternative to whole-prompt rewrites. Weak points: attribution is self-reported "
                   "and tail-only.", ["son55:E003", "son55:E004", "sol:E003"], ["sol:E002"]),
            "X": R("resolved", 3, "Both seats 3, confirmed. Algorithm 1, the cap of 18 rules, ≤3 mutations, ε = 50 "
                   "bps, K_attr = 20, the rollback rule and frozen deployment are reconstructable. Not 4: the "
                   "attribution and evolution prompts are not given, the sector-specific initial rules are only in "
                   "the code, the gate is whole-candidate, and there is no cross-window retention.",
                   ["sol:E004", "sol:E010", "sol:E012", "son55:E021"], ["son55:E020"]),
            "E.measurement": R("resolved", 2, "Opus = sol, at the run's cap for text–table contradictions. The "
                               "metrics themselves (O2O returns, Sharpe, MaxDD, Calmar, a 1000-trial cost-aware "
                               "null) are reconstructable. Problems: (1) costs are charged on entries only for the "
                               "methods, while the null counts a flip as two trades (sol:E014); (2) slippage and "
                               "impact are omitted; (3) the comparator LLM baselines are undocumented (opus:O02); "
                               "(4) §4.2's 'remaining baselines negligible' is contradicted by Table 1 (FinHEAR-4o "
                               "11.1%, FinCon-4.1 9.0%; opus:O01).",
                               ["sol:E006", "sol:E014", "son55:E017"], ["opus:O01", "opus:O02", "son55:E019"]),
            "E.causality": R("resolved", 3, "Opus = sol. Static (same backbone, inputs and initial rubric, no "
                             "evolution) is run on all four backbones: it is below Evo in all 6 sector cells for the "
                             "two OpenAI backbones and in both open-model 3-sector averages. A2 is a purpose-built "
                             "alternative-optimizer arm (free-form rewrite with identical init, budget and gate), "
                             "and A1 removes attribution. Not 4: the ablations are on AI Tech only (the best "
                             "sector), there is no gate-off arm, and the named optimizer neighbours are not run. "
                             "son55's single-run point is scored in E.statistics (A2 rule). The regime-fit reading "
                             "(momentum flip in a rally) is the adaptation mechanism itself, judged out of sample.",
                             ["sol:E008", "son55:E012", "son55:E013", "sol:E015"],
                             ["son55:E014", "son55:E023", "son55:E025"]),
            "E.holdout": R("resolved", 3, "Both seats 3, confirmed. Walk-forward windows of 4-month train, 1-month "
                           "validation and 2-month test, with the rubric frozen at test. Backbone cutoffs predate "
                           "the data, there is a 23:59 UTC news cutoff, and the news window is chosen on validation. "
                           "Not 4: one market regime over ~6 months, three windows, no data-overlap audit, and the "
                           "choice of sector for the ablations is not justified.",
                           ["sol:E005", "sol:E011", "son55:E009", "son55:E008"], ["son55:E016"]),
            "E.statistics": R("resolved", 1, "Both seats 1, confirmed (A2 tier 1). Sample sizes (122 days, three "
                              "windows), negative cells and a random null are reported, but there are no repeated "
                              "evolution runs, intervals or tests. The authors disclaim significance.",
                              ["sol:E007", "son55:E010"], ["son55:E025"]),
            "E.cost": R("resolved", 2, "Both seats 2, confirmed. Per-sector wall-clock covers all evolution stages "
                        "(API about 3h30; 4×H100 about 5h40–6h55). There are no token or dollar totals, no baseline "
                        "compute, and no matched-budget optimizer comparison beyond A2.",
                        ["sol:E013", "son55:E018"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (body, Tables 1–4, Appendices A–G). Class A: the rubric (non-weight "
                  "rule document) is edited from P&L feedback, gated, frozen and reused on later dates. All eight "
                  "items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: the evolved object is a non-weight rule document; the LLM is frozen.",
        "improver_check": "not claimed; the three-agent loop is fixed.",
        "figure_dependence": "Figure 3 (cumulative returns) is image-only; Tables 1–4 carry all credited values.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "See rs_pattern.reason.", ["sol:E008", "sol:E015"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["generative_process_redesign", None]],
                "structural_prior_encoding is dropped; son55 rated it weak, and no structural invariant is encoded.",
                ["sol:E008"], NOSCORE),
            XC(p, "local:2605.06822-2", "sol", "partial",
               "Different questions under one ID (A4). sol's local-2 (holdout) is verified partial. son55's local-2 "
               "(statistics) is merged into local-3.", ["sol:E005", "sol:E011"]),
            XC(p, "local:2605.06822-3", "sol", "partial",
               "Merged with son55 local-2 (A4). See the expectation note; the narrow repeat-run item is absent.",
               ["sol:E007", "son55:E010"]),
            XC(p, "local:2605.06822-4", "sol", "partial",
               "sol-only cost question. Verified: wall-clock only.", ["sol:E013"]),
            XC(p, "local:2605.06822-5", "sol", "partial",
               "Merged with son55 local-1 (same measurement question). Partial, for the reasons in the expectation "
               "note.", ["sol:E014", "opus:O01", "opus:O02"]),
            XC(p, "rs:structural_prior_encoding/RE-3", "son55", "partial",
               "son55-only (card not retained; check question). A2 swaps only the operator, on one sector.",
               ["son55:E013", "son55:E014"]),
            XC(p, "rs:structural_prior_encoding/RE-4", "son55", "partial",
               "son55-only (check question). LLM baselines are undocumented and ATLAS/GEPA are not run.",
               ["son55:E019", "opus:O02"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F1", "son55", "partial",
               "son55-only. The method is argued generically but validated only on equity long-short trading.",
               ["son55:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F5", "son55", "partial",
               "son55-only. The activation trace is self-reported and nothing checks the attribution. The recurrence "
               "filter (≥3 days) and the validation gate are partial guards.", ["son55:E003", "sol:E002"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S1", "son55", "met",
               "Card S1 asks whether the edit scope matches the artifact's structure; edits are single rules. sol's "
               "reservation (self-reported attribution) belongs to F5 and is recorded there.",
               ["son55:E022", "sol:E010"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S4", "sol", "met",
               "sol-only. Patterns recurring on ≥3 of the 20 worst days are aggregated before editing.",
               ["sol:E003", "sol:E016"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "met",
               "son55-only. The attribution agent sees holdings, predictions, rules, P&L and news (App G).",
               ["son55:E004"]),
            RC(p, "E.measurement", "sol", rr(2), "See ratings.E.measurement. son55 recorded the undocumented "
               "baselines (son55:E019) but placed them under causality. Neither seat noticed the contradicted "
               "'negligible' claim (opus:O01).", ["sol:E014", "opus:O01", "opus:O02"], "−2.5 vs son55"),
            RC(p, "E.causality", "sol", rr(3), "See ratings.E.causality. son55's single-run reason is scored in "
               "E.statistics, which is 1 in both seats.", ["sol:E008", "son55:E013"], "+3.75 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A clear A-class loop with strong "
                                                   "designed controls (Static on every backbone, A2 matched "
                                                   "free-form optimizer) but no repeats and three windows. Several "
                                                   "reporting gaps: undocumented LLM baselines, a contradicted "
                                                   "'negligible' sentence, and asymmetric cost accounting. Expected "
                                                   "upper 60s.",
            "integrity_checks": "Both seats a1 on 2605.06822v1, material sha bb1e13d9…; canonical seat hashes "
                                "equal conflicts.json.",
            "core_claim_check": "Every 3-sector average in §4.2 and Table 3 recomputed from Tables 1 and 4; the "
                                "lifts of 9.8/12.9 pp were verified.",
            "shared_error_review": "No shared rating error. Shared G/M/X/E.holdout/E.statistics/E.cost confirmed.",
            "rating_agreement": "All items = sol. Final 68.75.",
        },
    }

    # =========================================================== 2605.08083 AutoTTS
    p = "2605.08083"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "Overall, the discovered controller consistently achieves a stronger accuracy–efficiency "
                              "frontier", "§5.2 (Figure 3 text)",
                    "This figure-only claim is not fully consistent with Table 1. Qwen3-4B AIME25: ASC 76.4 at "
                    "277.3k vs AutoTTS β=0.5 at 73.8/332.3k (ASC dominates). Qwen3-8B held-out averages: ASC "
                    "62.8/485.7k vs β=1.0 at 62.7/710.8k (ASC dominates). The frontier advantage holds clearly only "
                    "for 0.6B/1.7B.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": ["generative_process_redesign"],
            "outside_taxonomy": False,
            "reason": "Opus. The paper's own stated move (§1, §2) is to recast TTS strategy design as controller "
                      "synthesis over a replay MDP, so that cheap program search (an existing machinery) applies. "
                      "That is reframe_as_solvable_object, sub null (son55). sol's generative_process_redesign is "
                      "kept as supporting: the conventionally fixed allocation heuristic of a staged sampling "
                      "procedure becomes a free design variable. sol's record wrote primary as an object "
                      "{main_id, sub_id}; it is read as generative_process_redesign.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object", role="primary"),
                        smatch("sol", p, "generative_process_redesign", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "population_search_executable_fitness", "H14",
                                              fit="high"),
                                       dmatch("sol", p, "search_agent_architecture", "H17", fit="medium")],
                           "unassigned": [],
                           "reason": "Opus. H14 is primary: its genome list names control policies, step 1 "
                                     "prescribes replay or proxy evaluators when live evaluation is expensive, and "
                                     "step 3 grounds mutations in evaluator traces, which is AutoTTS's design. H17 "
                                     "is kept as secondary: offline search over executable inference-time workflow "
                                     "code, one frozen design deployed and certified on held-out sets. son55's H12 "
                                     "(low) is dropped: there is no incumbent patching or promote/rollback, and the "
                                     "template is reset each round.",
                           "revision_proposals": ["son55: a domain-card note for inference-time algorithm discovery "
                                                  "on offline replay environments under H14/H15."]},
        "pattern_mapping": [{
            "rs_main": "reframe_as_solvable_object", "rs_sub": None,
            "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": "H14"},
            "operation_correspondence": "The TTS design problem becomes a replay MDP, and an LLM explorer proposes "
                                        "controller code that the deterministic replay evaluator scores. The best "
                                        "search-set controller is retained and frozen.",
            "necessary_conditions": "Pre-collected trajectories and probe answers; a single-knob interface.",
            "differences": "History archive rather than parent sampling; no replay-to-live fidelity check.",
            "evidence_ids": ["son55:E004", "son55:E007", "sol:E020"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.08083-1"): "local:2605.08083-5",
                    ("son55", "local:2605.08083-3"): "local:2605.08083-1"},
            overrides={
                "local:2605.08083-1": {"reason": "Merged (sol local-1 + son55 local-3: cost accounting). Partial: "
                                                 "$39.9/160 min and ablation search costs are reported; the "
                                                 "128-trajectory pre-sampling and live probe costs are not."},
                "local:2605.08083-2": {"status": "unmet",
                                       "reason": "Merged (sol local-2 + son55 local-2: repeat/variance). Opus = "
                                                 "son55. There is one five-round discovery per configuration and no "
                                                 "spread across the 64 subsample draws or across explorer runs. The "
                                                 "64-draw averaging is variance reduction, not uncertainty "
                                                 "reporting."},
                "local:2605.08083-5": {"reason": "Renumbered from son55 local-1 (A4 collision). Unmet: there is no "
                                                 "matched-effort tuning of the handcrafted baselines on the AIME24 "
                                                 "replay set, and no non-LLM search control. Scored in "
                                                 "E.causality=2."},
                "rsi:attribute_and_patch_incumbent/S3": dropped_card("attribute_and_patch_incumbent (H12)"),
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01"]),
        "assessment": assess("son55", p, [
            "Opus: the Figure 3 'consistently stronger frontier' is not borne out at 4B/8B against ASC in Table 1 "
            "(opus:O01).",
            "Opus: Table 3's Avg includes the search set (sol:E016)."]),
        "ratings": {
            "G": R("resolved", 3, "Opus = sol. The bottleneck is concrete and partly demonstrated: online "
                   "evaluation of candidate allocation policies is too costly (answered by replay), many free "
                   "hyperparameters overfit (the paper's preliminary finding and the w/o-β row), and scalar "
                   "feedback does not explain failures (the w/o-traces row). The TTS lineage (SC/ASC/ESC/"
                   "Parallel-Probe) is compared empirically; the discovery lineage (FunSearch/ADAS/AlphaEvolve/"
                   "Meta-Harness) is named, with the inherited trace idea acknowledged. Not 4: the 'first "
                   "algorithmic-search formulation of TTS' and the 'unexplored space' are asserted, not checked. "
                   "son55's missing automated-tuning alternative is an E.causality control (A2 rule) and is scored "
                   "there.", ["sol:E001", "sol:E003", "sol:E021", "son55:E021"], ["son55:E002"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. Replay MDP → code candidates → trace-augmented "
                   "history → single-β schedule → search-set selection → frozen reuse is reconstructable and "
                   "answers the stated problems. Weak points: β's anti-overfit role rests on a preliminary "
                   "observation, and the schedule fans out to 12 hand-set forms.",
                   ["son55:E004", "son55:E006", "sol:E004"], ["son55:E022"]),
            "X": R("resolved", 3, "Both seats 3, confirmed. The prompt, environment API, replay protocol, "
                   "selection rule and full controller code are disclosed. Not 4: the explorer version and seed, "
                   "and the β grid, are unspecified; there is no promotion gate beyond search accuracy; there are "
                   "docstring/code mismatches (the ema_alpha comment, a non-existent burst_senior).",
                   ["sol:E019", "sol:E020", "son55:E007", "sol:E022"], ["son55:E023"]),
            "E.measurement": R("resolved", 2, "Both seats 2, confirmed. Accuracy against ground truth and total "
                               "branch tokens target the claim, but everything is replay on 30-problem sets. Probing "
                               "is treated as free, which favours probe-based methods over full-read ASC/ESC. "
                               "Table 3's 'Avg' includes the search set but is called held-out (sol:E017). The "
                               "figure-only frontier claim is not borne out at 4B/8B against ASC in Table 1 "
                               "(opus:O01).",
                               ["sol:E010", "son55:E018"], ["sol:E016", "sol:E017", "son55:E017", "opus:O01"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. There are handcrafted baselines and "
                             "w/o-β and w/o-traces discovery ablations. The w/o-β arm sits at a 6× lower token "
                             "budget (not iso-cost). The ablations are single discovery runs. There is no "
                             "matched-effort tuning of the baselines, no non-LLM or random search control, and no "
                             "per-mechanism ablation of CMC.",
                             ["son55:E014", "son55:E015", "sol:E016"], ["son55:E011", "son55:E024"]),
            "E.holdout": R("resolved", 3, "Both seats 3, confirmed. Selection is on AIME24 replay; AIME25/HMMT25 are "
                           "never used for discovery or selection; R1-Distill-Llama-8B and GPQA are extra transfer "
                           "tests. Not 4: all four Qwen sizes are in the search union, so 'across model scales' is "
                           "not unseen-scale evidence; held-out curves were tracked per round; the held-out sets "
                           "are near-distribution.",
                           ["sol:E008", "sol:E009", "sol:E014"], ["son55:E026"]),
            "E.statistics": R("resolved", 1, "Both seats 1, confirmed (A2 tier 1). Sample sizes (30-problem sets, a "
                              "128-trajectory pool, 64 subsample draws) and dominated or negative points are shown, "
                              "but there is no spread, interval or test, and only one discovery run.",
                              ["sol:E007", "son55:E010"], ["son55:E025"]),
            "E.cost": R("resolved", 2, "Both seats 2, confirmed. Discovery $39.9/160 min and the ablation search "
                        "costs are reported, and inference tokens are central. The pre-sampling of 128 trajectories "
                        "per model–problem and live probing costs are excluded, and baseline effort is not matched.",
                        ["sol:E018", "son55:E016"], ["sol:E003"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text read (body, Tables 1–3, Appendices A–D including the prompt and the "
                  "discovered code). Class A: execution feedback over five rounds edits and retains controller code, "
                  "which is frozen and reused on held-out benchmarks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: the retained object is non-weight controller code; the explorer is a frozen coding agent.",
        "improver_check": "not claimed; the explorer is not improved.",
        "figure_dependence": "Figures 1, 3 and 4 (cost panel, scaling curves, discovery trajectory) are image-only; "
                             "only Table 1–3 values and text-stated costs are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "reframe_as_solvable_object",
                "See rs_pattern.reason. sol's object-valued primary is read as generative_process_redesign and kept "
                "as supporting.", ["son55:E004", "sol:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["reframe_as_solvable_object", None], ["generative_process_redesign", None]],
                "Union: son55 primary + sol supporting.", ["son55:E004", "sol:E001"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["population_search_executable_fitness", "H14"], ["search_agent_architecture", "H17"]],
                "See domain_pattern.reason: H14 primary, H17 secondary, H12 (low) dropped.",
                ["son55:E004", "sol:E020", "son55:E023"], NOSCORE),
            XC(p, "local:2605.08083-1", "sol", "partial",
               "Different questions under one ID (A4). sol's local-1 (cost) is verified partial and merged with "
               "son55 local-3 (same cost question). son55's local-1 (baseline tuning / non-LLM search) moves to "
               "local-5, unmet.", ["sol:E018", "son55:E016"]),
            XC(p, "local:2605.08083-2", "son55", "unmet",
               "Same question in both seats (repeat/variance). There is one discovery run and no spread; the "
               "64-draw averaging is not uncertainty reporting.", ["son55:E010", "son55:E025", "sol:E007"]),
            XC(p, "local:2605.08083-4", "sol", "partial",
               "sol-only measurement question. Verified: Table 3's Avg includes AIME24 (search) while the text says "
               "held-out.", ["sol:E016", "sol:E017"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "sol-only (card kept as supporting). There is no per-mechanism ablation of CMC.", ["sol:E016"]),
            XC(p, "rs:generative_process_redesign/RE-6", "sol", "partial",
               "sol-only. There are scaling curves, but ASC dominates at 4B/8B (opus:O01).",
               ["sol:E012", "sol:E013", "opus:O01"]),
            XC(p, "rs:reframe_as_solvable_object/RE-3", "son55", "partial",
               "son55-only. The replay environment and β are new structure; the search machinery is re-used.",
               ["son55:E003", "son55:E021"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "unmet",
               "son55-only. There is no replay-to-live equivalence check.", ["son55:E004", "son55:E017"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "son55", "not_applicable",
               "son55-only, check question (H12 not kept). No incumbent is patched; the template resets each round.",
               ["son55:E023"]),
            XC(p, "rsi:population_search_executable_fitness/F1", "son55", "partial",
               "son55-only. Search-level contributions exist (replay, β, traces), but there is no search-algorithm "
               "comparison.", ["son55:E003"]),
            XC(p, "rsi:population_search_executable_fitness/F4", "son55", "partial",
               "son55-only. Replay tokens exclude probing; the proxy-to-live tie is argued, not tested.",
               ["son55:E017"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "partial",
               "son55-only. The evaluator is deterministic and built first, but replay fidelity is not validated.",
               ["son55:E004"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "partial",
               "son55-only. Traces are ablated; the history itself is not.", ["son55:E015"]),
            XC(p, "rsi:search_agent_architecture/S1", "sol", "met",
               "sol-only. Replay plus the single-β interface are the search-shaping primitives.",
               ["sol:E003", "sol:E004"]),
            XC(p, "rsi:search_agent_architecture/S3", "sol", "met",
               "sol-only. Selection is by search-set correctness, not explorer self-assessment.",
               ["sol:E008", "sol:E009"]),
            XC(p, "rsi:search_agent_architecture/S6", "sol", "partial",
               "sol-only. Held-out benchmarks and one extra family; the scales are not unseen.",
               ["sol:E008", "sol:E014"]),
            RC(p, "G", "sol", rr(3), "See ratings.G.", ["sol:E003", "sol:E021"], "+3.75 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A clean held-out benchmark split and a "
                                                   "frozen code artifact, but replay-only measurement, no variance, "
                                                   "ASC-dominated points at 4B/8B, an Avg that mixes in the search "
                                                   "set, and partial cost accounting. Expected low-to-mid 60s.",
            "integrity_checks": "Both seats a1 on 2605.08083v2, material sha 5b02d360…; canonical seat hashes equal "
                                "conflicts.json. sol's rs_pattern.primary is an object (read as "
                                "generative_process_redesign, per controller note).",
            "core_claim_check": "Table 1 averages recomputed: β=0.5 is 45.3 vs SC@64 45.1 (the text says 45.2), 5/8 "
                                "cases verified, 3/4 models on average verified, and ASC dominance at 4B/8B. Table 3 "
                                "Avg = mean of three sets including AIME24.",
            "shared_error_review": "Shared M/X/E items confirmed. The Figure 3 frontier claim is tempered by Table 1 "
                                   "(opus:O01), already reflected in E.measurement=2.",
            "rating_agreement": "All items = sol. Final 65.0.",
        },
    }

    # =========================================================== 2605.08374 MemQ
    p = "2605.08374"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "compared with 51.43% for the reported mixed ranking", "§5.4 RQ3",
                    "Table 11 lists MemQ's LiveCodeBench retrieval weights as w_s 0.4 / w_q 0.6, and the Table 7 row "
                    "for 0.4/0.6 gives evaluation SR 48.57. The 51.43 that equals the main Table 1 LCB held-out "
                    "value, and that the text calls 'the reported mixed ranking', is the Table 7 row for "
                    "w_s 0.6 / w_q 0.4. The Final/CSR in Tables 6–7 (61.79/67.62) also differ from Table 2's main "
                    "LCB values (64.76/69.76). The configuration behind a headline cell is therefore "
                    "contradictory.", kind="our_inference"),
            opus_ev(p, "O02", "The best-performing weights identified here were not adopted in the main experiments, "
                              "which use the configurations reported in Appendix", "App D.6",
                    "This conflicts with O01: on LCB, the main held-out value coincides with the best-evaluation row of "
                    "the sweep, not with the stated main configuration."),
            opus_ev(p, "O03", "compared with 14.58 pp for MemRL (Table", "§5.4",
                    "The coverage-gap numbers are in Table 3, not Table 4 (the token table). A second reporting "
                    "slip: BFCL evaluation SR is 62.83 in Table 6 vs 62.38 in Table 1."),
        ],
        "rs_pattern": {
            "primary": "reframe_as_solvable_object", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats chose reframe_as_solvable_object (sub null) as primary: the setting is formalised "
                      "as an EC-MDP, and TD(λ) machinery is transferred to a structural graph. sol's supporting "
                      "adapt_via_conditioning C03 is not kept: no reader is trained to interpret a conditioning "
                      "schema, so the frozen-LLM conditioning is background.",
            "matches": [smatch("son55", p, "reframe_as_solvable_object", role="primary")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "evidence_gated_retention", "H29"),
                                       dmatch("son55", p, "index_experience_for_reuse", "H03")],
                           "unassigned": [],
                           "reason": "Opus = son55. H29 is exact: the card names 'credit propagated backward "
                                     "through the provenance of entries that were built from other entries'. H03 is "
                                     "kept: the store is a growing case base of proceduralised trajectories and "
                                     "reflections, retrieved by similarity with an ε-greedy value re-rank and "
                                     "appended after every task. sol rejected H04, not H03; H04 stays unassigned.",
                           "revision_proposals": []},
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.08374-1"): "local:2605.08374-4",
                    ("son55", "local:2605.08374-2"): "local:2605.08374-3"},
            overrides={
                "local:2605.08374-4": renum("local:2605.08374-1", "local:2605.08374-4"),
                "local:2605.08374-3": {"reason": "Merged (sol local-3 + son55 local-2: statistics). Partial: 3 "
                                                 "seeds, SD and approximate CIs on averages. No tests, the CIs "
                                                 "overlap with MemP, and one LCB problem is 2.9 pp."},
            }),
        "claims": lambda c: add_counter(c, "C3", ["opus:O01", "son55:E026"]),
        "assessment": assess("son55", p, [
            "Opus: the LCB main configuration contradicts the ablation tables (opus:O01, opus:O02)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3, confirmed. The residual is precise (ancestor credit in "
                   "memory-creation chains) against a named, run neighbour (MemRL, γ=0), with a clear TD lineage. "
                   "Not 4: the depth and frequency of such chains are never shown, and other utility methods are "
                   "only cited.", ["son55:E001", "son55:E002", "son55:E003"]),
            "M": R("resolved", 3, "Both seats 3, confirmed. The EC-MDP, first-order projection with residual, and "
                   "path-weighted TD(λ) over exposure edges are coherent and give distinguishable predictions "
                   "(γ=0 / λ=0). Weak points: edges record exposure, not causation; theory covers fixed DAGs with "
                   "unclipped updates only; parent-mean initialisation is an extra assumption.",
                   ["son55:E004", "son55:E005", "sol:E014"], ["son55:E018", "son55:E019"]),
            "X": R("resolved", 3, "Both seats 3, confirmed. Algorithm 1, depth cap, pruning floor, clipping and "
                   "per-benchmark tables make it reconstructable. Not 4: unconditional admission, no retirement or "
                   "rollback, and an append-only store.",
                   ["son55:E020", "sol:E005", "sol:E006"], ["son55:E026"]),
            "E.measurement": R("resolved", 2, "Shared-error correction (both seats 3). The benchmark-native success "
                               "metrics are sound, and Final SR/CSR are labelled as accumulation-split metrics. But "
                               "the provenance of a headline cell is contradictory. Table 11's LCB weights (0.4/0.6) "
                               "give 48.57 in Table 7, while the reported 51.43 is the 0.6/0.4 row, which §5.4 "
                               "calls 'the reported mixed ranking' (opus:O01, opus:O02). The ablation-pipeline "
                               "Final/CSR differ from Table 2, BFCL is 62.83 vs 62.38, and the coverage gap is "
                               "cited as Table 4 (opus:O03). Run convention: text–table contradictions cap at 2.",
                               ["sol:E001", "son55:E008", "son55:E028"], ["opus:O01", "opus:O02", "opus:O03"]),
            "E.causality": R("resolved", 2, "Opus = sol. The γ=0 and λ=0 arms are clean mechanism ablations (LCB "
                             "−5.72/−8.57, BFCL −2.43/−4.41, DSBench −3.73/−4.88 eval SR), but they cover 3 of 5 "
                             "benchmarks with 35–116-task evaluation sets, i.e. 2–3 LCB problems. The headline "
                             "MemQ-vs-MemRL comparison is confounded with configuration. Initial Q is 0.66 vs 0 on "
                             "DSBench/AutomationBench, the two benchmarks credited with the largest gains, and "
                             "initialisation moves LCB eval by 17 pp. w_s/w_q differ on ERQA, GPQA and "
                             "AutomationBench, and GPQA batch size differs. The Q-success correlation is "
                             "correlational.",
                             ["son55:E012", "sol:E011", "son55:E015"],
                             ["son55:E026", "son55:E009", "son55:E014"]),
            "E.holdout": R("resolved", 3, "Both seats 3, confirmed. Each benchmark has a separate held-out split, "
                           "and the best-epoch bank is selected on the accumulation split. Not 4: no-held-out "
                           "tuning is stated only for LLAB, γ/λ sweeps are on train SR, and the LCB weight "
                           "contradiction (scored in E.measurement) leaves open whether the evaluation SR influenced "
                           "that configuration. The held-out sets are small.",
                           ["sol:E009", "son55:E006", "son55:E011", "sol:E016"], ["son55:E010"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2). Three seeds with SD, approximate "
                              "95% CIs on averages (overlapping with MemP), no tests, point-estimate ablations, and "
                              "per-benchmark margins of +0.2 to +2.3 pp inside SDs of 0.5–2.9.",
                              ["sol:E010", "son55:E023"], ["son55:E025"]),
            "E.cost": R("resolved", 2, "Opus = sol. DSBench training tokens (agent, judge and memory calls) are "
                        "reported with SD for three proceduralising methods, and epochs, backbone and data are "
                        "matched. But this covers 1 of 8 benchmarks, the 11–16% saving is within one SD, DAG "
                        "traversal cost is given only asymptotically, and wall-clock is absent.",
                        ["sol:E012", "sol:E013", "son55:E016"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v4 text read (body, Tables 1–17, Appendices A–F). Class A: execution outcomes update "
                  "persistent non-weight memory content, Q-values and provenance edges, which are reused on later "
                  "and held-out tasks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope: the LLM is frozen; the retained object is the memory store with per-entry values and DAG.",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 4–5 (γ/λ sweeps, ablation bars) are image-only; their differences are stated "
                             "in the text and only those are used.",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["reframe_as_solvable_object", None]],
                "C03 needs a trained reader; the frozen LLM is not one.", ["son55:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["evidence_gated_retention", "H29"], ["index_experience_for_reuse", "H03"]],
                "See domain_pattern.reason.", ["son55:E004", "son55:E020"], NOSCORE),
            XC(p, "local:2605.08374-1", "sol", "met",
               "Different questions under one ID (A4). sol's local-1 (bank selected on the accumulation split) is "
               "verified met. son55's local-1 (initial-Q confound) moves to local-4, partial.",
               ["sol:E009", "son55:E015"]),
            XC(p, "local:2605.08374-3", "sol", "partial",
               "Merged with son55 local-2 (same statistics question); partial in both.", ["sol:E010", "son55:E023"]),
            XC(p, "rs:reframe_as_solvable_object/RE-1", "son55", "partial",
               "son55-only. Fixed-DAG theory; the residual is bounded but not measured.",
               ["son55:E018", "son55:E019"]),
            XC(p, "rs:reframe_as_solvable_object/RE-4", "son55", "partial",
               "son55-only. There is no causal check that ancestors contributed.", ["son55:E005", "son55:E012"]),
            XC(p, "rsi:evidence_gated_retention/F5", "son55", "partial",
               "son55-only. Values demote by ranking but never remove entries.", ["son55:E020"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "unmet",
               "Applicable as a check: the store grows without admission or retirement. sol's not_applicable "
               "(ranking-only claim) is noted, but the condition asks whether the gate exists.", ["son55:E020"]),
            XC(p, "rsi:evidence_gated_retention/S5", "sol", "partial",
               "sol-only. The token account covers DSBench only.", ["sol:E012"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "unmet",
               "son55-only. Every trajectory or reflection is admitted.", ["son55:E020"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "met",
               "son55-only. No Memory and RAG baselines, with the bank frozen for held-out evaluation.",
               ["son55:E008", "son55:E006"]),
            RC(p, "E.causality", "sol", rr(2), "See ratings.E.causality. son55 documented the initial-Q confound "
               "itself (son55:E009, son55:E026) but still rated 3.", ["son55:E026", "son55:E015"],
               "−3.75 vs son55"),
            RC(p, "E.cost", "sol", rr(2), "See ratings.E.cost.", ["sol:E012", "son55:E016"], "−1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "reason": "Neither seat compared Table 11's LCB weights with Tables 6–7 and §5.4. The reported "
                       "held-out 51.43 is the w_s/w_q = 0.6/0.4 row, while the stated main configuration (0.4/0.6) "
                       "gives 48.57. The ablation-pipeline Final/CSR differ from Table 2. BFCL is 62.83 vs 62.38, and "
                       "a table reference is wrong. With these contradictions the run convention caps E.measurement "
                       "at 2.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03"],
             "score_impact": "−2.5 (sol 68.75 and son55 73.75 → 66.25 together with the E.causality/E.cost rulings)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A precise mechanism with clean γ/λ "
                                                   "ablations, but tiny held-out sets, a configuration asymmetry vs "
                                                   "MemRL exactly where gains are largest, and appendix tables that "
                                                   "do not reconcile with the stated main LCB configuration. "
                                                   "Expected mid-60s.",
            "integrity_checks": "Both seats a1 on 2605.08374v4, material sha 393cd273…; canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Abstract deltas 2.53/4.23/2.13 and per-benchmark Final-SR deltas vs MemRL "
                                "recomputed; Tables 6–8 cross-checked against Tables 1, 2 and 11.",
            "shared_error_review": "One shared error: E.measurement 3 → 2 (see shared_error_corrections). Others "
                                   "confirmed.",
            "rating_agreement": "E.causality and E.cost = sol; E.measurement corrected. Final 66.25.",
        },
    }

    # =========================================================== 2605.08399 CoCoDA
    p = "2605.08399"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "mean loss isolates what code-specific hierarchy buys", "§4.4 / Table 2",
                    "Table 2's Δ column is not the mean of its own per-benchmark drops. Recomputed from the cells: "
                    "w/o CTD −3.46 (reported −3.49), w/o TDR −1.97 (−1.79), w/o GAR −1.47 (−1.40), w/o CTD+TDR −4.46 "
                    "(−4.64), all-off −5.01 (−5.18). The −1.79 the text builds on is itself off by 0.18.",
                    kind="our_inference"),
            opus_ev(p, "O02", "sweeps the compositional weight", "App K, Table 8",
                    "The λ sweep reports GSM8K accuracy, and its λ = 0.20 value (92.64) is exactly the Table 1 "
                    "4B GSM8K test score. App G uses the training split as seed set and query stream, and reports "
                    "evaluation on the test split; no validation split is described. λ was therefore selected on "
                    "test accuracy.", kind="our_inference"),
            opus_ev(p, "O03", "as the knee of the accuracy–cost frontier", "App K",
                    "k2 = 32 is likewise chosen from GSM8K accuracy and latency, with no validation split stated."),
            opus_ev(p, "O04", "as library size sweeps from", "§4.3",
                    "Figure 2(b) sweeps 50 → 1,600 nodes, but the trained libraries end at 205–382 nodes (Table 5) "
                    "and saturate. How the 800- and 1,600-node libraries were obtained, and what 'matched 4B "
                    "accuracy' means there, is not stated.", kind="our_inference"),
            opus_ev(p, "O05", "The training split is used both as the seed set", "App G",
                    "Every benchmark's seed set and GRPO stream is its training split. Table 6 lists no EvalPlus "
                    "training split, yet Table 5 reports an evolved EvalPlus library (22 primitives, 183 "
                    "composites, 61 rejections). Its query source is undefined."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["structural_prior_encoding"],
            "outside_taxonomy": False,
            "reason": "Opus. C25 fits the operation: the planner emits typed sub-goals and tool-call traces, routes "
                      "them to an executor (a sound solver) and a deterministic verifier, uses the verified outcome "
                      "for credit (GRPO with R_res + R_comp), and accumulates verified by-products into reusable "
                      "capital (the composite library). sol's structural_prior_encoding is kept as supporting with "
                      "sub null. Acyclicity and flat-size are guaranteed by construction, but C13 requires "
                      "message-passing or propagation over the wiring, and the DAG here only drives retrieval "
                      "descent and reward bookkeeping.",
            "matches": [smatch("son55", p, "decompose_and_delegate", role="primary"),
                        smatch("sol", p, "structural_prior_encoding", role="supporting", sub_id=None, fit="partial",
                               reason="Opus: DAG invariants (acyclicity, flat size) are kept by construction. C13 "
                                      "(propagation over relational wiring) is not literal, so sub is null.")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "crystallize_executable_capability", "H08"),
                                       dmatch("sol", p, "index_experience_for_reuse", "H04", fit="medium"),
                                       dmatch("son55", p, "couple_context_and_weight_updates", "H28")],
                           "unassigned": [],
                           "reason": "Opus, union. H08 is shared by both seats: a typed compositional skill DAG "
                                     "with promotion of recurring sequences. H04 (sol): restructures the store into "
                                     "coarse-to-fine tiers with child pointers, and the claim is certified by cost "
                                     "vs flat retrieval (Fig 2b). H28 (son55, boundary card): the same rollouts "
                                     "drive GRPO and library insertion, and the planner is trained to read the tool "
                                     "cards (S1, S3). Scope stays in under A3 bullet 2 and the run's ASH precedent: "
                                     "the library is read at deployment and has its own structural control (w/o "
                                     "CTD) plus a fixed-inventory control (ReTool).",
                           "revision_proposals": []},
        "pattern_mapping": [{
            "rs_main": "decompose_and_delegate", "rs_sub": "C25",
            "domain": {"namespace": "rsi", "main": "crystallize_executable_capability", "sub": "H08"},
            "operation_correspondence": "Verified tool-call trajectories (delegated execution) are abstracted into "
                                        "typed composite tools and folded into the DAG library, which later "
                                        "queries retrieve and invoke.",
            "necessary_conditions": "A deterministic verifier and an executable tool interface.",
            "differences": "Composites are written by a fixed teacher, and equivalence is LLM-judged rather than "
                           "executed (F5 unmet).",
            "evidence_ids": ["son55:E003", "son55:E022", "sol:E018"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.08399-1"): "local:2605.08399-7",
                    ("son55", "local:2605.08399-3"): "local:2605.08399-8"},
            overrides={
                "local:2605.08399-2": {"reason": "Merged (same question in both seats: EvalPlus training/library "
                                                 "source). Partial: five official splits are separated; the "
                                                 "EvalPlus stream is undefined (opus:O05). In addition, λ and k2 "
                                                 "were selected on test accuracy (opus:O02, opus:O03)."},
                "local:2605.08399-7": renum("local:2605.08399-1", "local:2605.08399-7"),
                "local:2605.08399-8": {"note": "Renumbered from son55 local-3 (A4 collision with sol's statistics "
                                               "question). Partial. Scored in E.measurement=2 together with the "
                                               "Table 2 Δ mismatch (opus:O01)."},
                "rsi:crystallize_executable_capability/F3": {
                    "status": "partial",
                    "reason": "Opus revised (son55 unmet). Composites are abstracted from the student's own "
                              "verified successful trajectories, but by a fixed stronger teacher that also writes "
                              "the SFT demonstrations. The skill source is external supervision, not a human; the "
                              "failure is partly avoided."},
                "rsi:crystallize_executable_capability/F5": {
                    "status": "unmet",
                    "reason": "Opus = son55. L3 spec checks and MERGE decisions are LLM prompts; only acyclicity is "
                              "programmatic. The source trajectory is executed, but the abstracted composite's "
                              "equivalence is not."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C3", ["opus:O01", "son55:E012"]), "C1", ["opus:O02"]),
        "assessment": assess("son55", p, [
            "Opus: Table 2 Δ column ≠ mean of its cells (opus:O01).",
            "Opus: λ and k2 selected on test accuracy (opus:O02, opus:O03).",
            "Opus: the binary R_res is incompatible with the reported ρ sweep (sol:E026).",
            "Opus: theory steps invalid (sol:E028, sol:E031)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus = son55. Growing a library with the planner is a real problem, and the "
                   "lineage is broad. But the motivating context-budget bottleneck does not bind in the regime the "
                   "method produces: the trained libraries are 205–382 tools (Table 5), accuracy plateaus by about "
                   "400, and the 1,600-node regime is never reached by training (opus:O04). The 'never both' "
                   "missing quadrant is the paper's own taxonomy (run precedent: H-Mem). Most named neighbours "
                   "(Voyager, CRAFT, ReGAL, DreamCoder/Stitch) are not compared.",
                   ["son55:E001", "son55:E002", "son55:E017"], ["son55:E018", "opus:O04"]),
            "M": R("resolved", 2, "Opus = sol. The design (typed cascade, teacher-folded composites, saved-call "
                   "reward) is concrete, but its stated justification is invalid in key places. Theorem 1 derives "
                   "o(C_flat) from limsup ≤ α1α2 < 1, and L2 still ranks all α1·n L1 survivors (sol:E028, "
                   "sol:E004). Corollary 5's log-depth argument fails on a chain (sol:E031). Theorem 4's library "
                   "step treats LLM-judged L3 checks as certified equivalence, with 'no false positives under "
                   "faithful reading' (sol:E005, sol:E030). The saved-call reward can credit unnecessary "
                   "composites, which the authors concede for large λ (sol:E007, sol:E025). Mechanism plausible, "
                   "key assumptions weak.",
                   ["sol:E002", "sol:E003", "son55:E004"],
                   ["sol:E028", "sol:E031", "sol:E030", "sol:E007", "sol:E025"]),
            "X": R("resolved", 2, "Opus = sol. Algorithms 1–3, prompts and Table 4 are given, but the retention "
                   "mechanism cannot be reconstructed as reported. The admission threshold ρ acts on a binary "
                   "R_res ∈ {0,1} (Table 4), yet the ρ sweep reports 419/364/207 retained composites at "
                   "0.5/0.8/1.0, which is impossible on fixed binary rewards (sol:E019, sol:E026). Child-spec "
                   "validation and dedup are LLM prompts. The EvalPlus query stream is undefined (opus:O05). There "
                   "is no retirement, versioning or rollback.",
                   ["sol:E008", "sol:E010", "sol:E018", "son55:E003"], ["sol:E019", "sol:E026", "opus:O05"]),
            "E.measurement": R("resolved", 2, "Shared-error correction (both seats 3). The verifiers are standard "
                               "and deterministic, but the reported numbers do not reconcile. (1) Table 2's Δ column "
                               "≠ the mean of its cells (−1.97 vs −1.79, −4.46 vs −4.64, −5.01 vs −5.18; opus:O01). "
                               "(2) The appendix equates the all-off variant with a ReTool-style planner, yet it "
                               "sits 3–5 pts below ReTool (son55:E012). (3) Tool counts disagree: 1,873 vs 309, "
                               "and 42 vs 14–22 primitives (son55:E020). (4) The 'upper bound' teacher is "
                               "tool-free CoT. Run convention: contradictions cap at 2.",
                               ["sol:E013", "son55:E007", "son55:E016"],
                               ["opus:O01", "son55:E012", "son55:E020", "son55:E008"]),
            "E.causality": R("resolved", 2, "Both seats 2, confirmed. ReTool (frozen inventory, same RL backbone) "
                             "is the intended co-evolution control: CoCoDA is ahead in all 24 cells, but by "
                             "0.1–1.6 pts against SDs ≤0.4–0.7, and parity (teacher SFT, tool inventory, steps) is "
                             "unstated. The component ablations are internally inconsistent with that control "
                             "(all-off ≪ ReTool). w/o CTD also zeroes the reward. There is no static-library arm, "
                             "and they cover 4B only.",
                             ["son55:E010", "son55:E011", "son55:E026"],
                             ["son55:E009", "son55:E012", "sol:E023"]),
            "E.holdout": R("resolved", 2, "Opus = sol. Five benchmarks use official train/test splits, with the "
                           "library and planner built on training streams. Not 3, for two reasons. (1) EvalPlus has "
                           "no training split, but an EvalPlus library was evolved from an undefined stream "
                           "(opus:O05). (2) λ and k2 were selected on test accuracy: Table 8's λ = 0.20 value equals "
                           "the Table 1 test score, and there is no validation split (opus:O02, opus:O03). The "
                           "sensitivity in [0.1, 0.3] is ≤0.6 pts, so the bias is small but real. There is no "
                           "leakage guard.",
                           ["sol:E020", "son55:E016"], ["opus:O02", "opus:O03", "opus:O05"]),
            "E.statistics": R("resolved", 2, "Both seats 2, confirmed (A2 tier 2). Three named seeds with SD upper "
                              "bounds (≤0.4 / ≤0.7) in prose. There are no per-cell SDs, CIs or tests, and the "
                              "ablations have no SD. Several ReTool margins (e.g. 0.11 at 4B WTQ/FinQA) are below "
                              "the stated SD bound.",
                              ["sol:E022", "son55:E015"], ["son55:E026"]),
            "E.cost": R("resolved", 2, "Opus = sol. CoCoDA's stage wall-clock and GPU-hours (35–98) and the "
                        "retrieval-token ratios (11.4×/4.7× at 1,600 nodes) are reported. The teacher-call cost, "
                        "the baselines' training cost and any matched-budget comparison are absent, and the "
                        "token-ratio regime is not one training produces (opus:O04).",
                        ["sol:E014", "sol:E021", "son55:E024"], ["opus:O04"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read (body, Tables 1–8, Appendices A–L including proofs). In scope under A3 "
                  "bullet 2 (ASH precedent): the non-weight tool DAG is read at deployment and has structural and "
                  "fixed-inventory controls, although planner weights are co-trained. The many internal "
                  "contradictions are author-side facts priced into M/X/E, not missing material. All eight items "
                  "resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (A3 bullet 2): the tool DAG is retained, read at deployment and controlled (w/o CTD, "
              "ReTool); planner GRPO weights are co-trained (H28 boundary).",
        "improver_check": "not claimed; the teacher abstractor is fixed.",
        "figure_dependence": "Figures 2–4 (growth curves, context-cost scaling, latency, DAG snapshot) are "
                             "image-only; only text-stated ratios (11.4×, 4.7×) are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "See rs_pattern.reason.", ["son55:E003", "son55:E005"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["decompose_and_delegate", "C25"], ["structural_prior_encoding", None]],
                "son55's C25 is primary; sol's card is kept as supporting with the sub dropped (C13 not literal).",
                ["son55:E003", "sol:E002"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["crystallize_executable_capability", "H08"], ["index_experience_for_reuse", "H04"],
                 ["couple_context_and_weight_updates", "H28"]],
                "Union of both seats; see domain_pattern.reason.", ["sol:E002", "son55:E023", "sol:E014"], NOSCORE),
            XC(p, "local:2605.08399-1", "sol", "unmet",
               "Different questions under one ID (A4). sol's local-1 (formal bounds need extra premises) is verified "
               "unmet (sol:E028, sol:E031). son55's local-1 (baseline parity) moves to local-7, unknown.",
               ["sol:E028", "sol:E031"]),
            XC(p, "local:2605.08399-2", "sol", "partial",
               "Same question in both seats (EvalPlus training source). As an expectation about holdout separation "
               "it is partial: five splits are clean and one is undefined. son55's 'unknown' describes the EvalPlus "
               "fact, which is priced into E.holdout=2.", ["sol:E020", "son55:E016", "opus:O05"]),
            XC(p, "local:2605.08399-4", "sol", "unmet",
               "sol-only. The binary R_res makes the ρ sweep's different library sizes impossible (verified against "
               "Table 4 and App K).", ["sol:E019", "sol:E026"]),
            XC(p, "local:2605.08399-5", "sol", "partial",
               "sol-only cost question. Verified: no baseline or teacher bill.", ["sol:E014", "sol:E021"]),
            XC(p, "local:2605.08399-6", "sol", "unmet",
               "sol-only. The workload-baseline and monotonicity steps hold only for equivalent rewrites (verified "
               "in §3.3 and L.5).", ["sol:E006", "sol:E030"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "partial",
               "son55-only. GPU-hours and retrieval tokens are reported; teacher and baseline costs are not.",
               ["son55:E019", "son55:E024"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "son55-only. 4B-only ablations and no static-library arm.", ["son55:E011", "son55:E012"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "met",
               "son55-only. Breadth: six benchmarks in three categories and four sizes.", ["son55:E007", "son55:E016"]),
            XC(p, "rsi:couple_context_and_weight_updates/S3", "son55", "met",
               "son55-only. The planner is GRPO-trained on rollouts conditioned on retrieved tool cards (App D.7).",
               ["son55:E004", "son55:E023"]),
            XC(p, "rsi:crystallize_executable_capability/F3", "revised", "partial",
               "Teacher-written composites distilled from the student's own verified trajectories: external "
               "supervision, not a human. Partly avoided.", ["son55:E003", "son55:E023"]),
            XC(p, "rsi:crystallize_executable_capability/F5", "son55", "unmet",
               "Equivalence is LLM-judged, not executed. sol's 'partial' credited the executed source trajectory, "
               "which F5 does not ask about.", ["son55:E006", "son55:E022", "sol:E005"]),
            XC(p, "rsi:index_experience_for_reuse/S3", "sol", "met",
               "sol-only. Executable bodies and L1–L4 index records are separate.", ["sol:E002", "sol:E003"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "sol", "met",
               "sol-only. The cascade is selective (top-32 before spec/example checks).", ["sol:E003", "sol:E004"]),
            XC(p, "rsi:index_experience_for_reuse/S6", "sol", "partial",
               "sol-only. Local insertion is O(|Ch|+|E|), but sublinearity is unproven (sol:E028).",
               ["sol:E010", "sol:E028"]),
            RC(p, "G", "son55", rr(2), "See ratings.G.", ["son55:E017", "son55:E018", "opus:O04"],
               "−3.75 vs sol"),
            RC(p, "M", "sol", rr(2), "See ratings.M. son55 noted LLM-judged equivalence and reward over-favouring "
               "but did not engage the invalid proofs that carry the sublinearity and monotonicity claims.",
               ["sol:E028", "sol:E031", "sol:E030"], "−5.0 vs son55"),
            RC(p, "X", "sol", rr(2), "See ratings.X. son55 itself recorded that 'internal numbers do not "
               "reconcile'. The decisive item is the contradictory ρ gate on a binary reward.",
               ["sol:E019", "sol:E026", "opus:O05"], "−5.0 vs son55"),
            RC(p, "E.holdout", "sol", rr(2), "See ratings.E.holdout. Both seats flagged EvalPlus; test-set "
               "selection of λ/k2 (opus:O02) decides between 2 and 3.", ["sol:E020", "opus:O02", "opus:O05"],
               "−2.5 vs son55"),
            RC(p, "E.cost", "sol", rr(2), "See ratings.E.cost.", ["sol:E014", "son55:E024", "opus:O04"],
               "−1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "reason": "Both seats saw individual inconsistencies: son55 the tool counts and the all-off vs ReTool "
                       "gap, sol the ρ/binary conflict. Neither applied the run's cap. Neither recomputed Table 2: its "
                       "Δ column does not equal the mean of its own cells (opus:O01). With several text–table and "
                       "table–table contradictions the run convention caps E.measurement at 2.",
             "evidence_ids": ["opus:O01", "son55:E012", "son55:E020"],
             "score_impact": "−2.5 (sol 56.25 → 50.0 together with G; son55 66.25 → 50.0 together with "
                             "M/X/E.holdout/E.cost)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A plausible design with consistent "
                                                   "but tiny gains over ReTool, wrapped in invalid theory, a "
                                                   "self-contradictory admission gate, an undefined EvalPlus "
                                                   "stream, test-chosen λ, and table summaries that do not "
                                                   "reconcile. Expected around 50.",
            "integrity_checks": "Both seats a1 on 2605.08399v1, material sha 8fc6e854…; canonical seat hashes equal "
                                "conflicts.json.",
            "core_claim_check": "Table 1 margins vs ReTool and teacher, Table 2 deltas recomputed (opus:O01), Table "
                                "4/5/6/8 and App H/K cross-checked, and the Theorem 1/Corollary 5 proofs re-read.",
            "shared_error_review": "One shared error: E.measurement 3 → 2. E.causality=2 and E.statistics=2 "
                                   "confirmed.",
            "rating_agreement": "G = son55; M, X, E.holdout, E.cost = sol; E.measurement corrected. Final 50.0.",
        },
    }
    return S
