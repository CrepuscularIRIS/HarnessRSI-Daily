"""Opus rulings for r19b a1 (data only; consumed by _build.py)."""
import copy

RK = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")


def batch_notes():
    return [
        "2605.14211 ASH (scope conflict): IN SCOPE, sol. A3 bullet 2 and the run's RMM (r02b) / PsychAgent (r13b) "
        "precedent: the key-moment memory is a non-weight object (HDBSCAN classifier K, re-fitted at every stuck-"
        "triggered bootstrap, plus a per-agent bank appended during play). The deployed policy reads it at every step "
        "(opus:O07), and two controls evaluate it: memory-off (−2.5 milestones) and random-frame content (6.00 vs "
        "7.75). This differs from SEAgent (r05b), DreamGym (r07b) and EvoEnv (this batch), where the non-weight "
        "asset is only training data. Weight-side gains from bootstrapping are not credited as harness evidence. "
        "Final 61.25, below sol's 65.0. E.causality is revised 3 → 2 for two reasons. First, the random-frame "
        "control is stated only for inference (opus:O01), so a train/inference mismatch can explain the drop. "
        "Second, no frozen-K arm separates the feedback-driven update of the memory from weight retraining "
        "(opus:O06). son55's finding is confirmed: the paper gives three different 'strongest baseline' values "
        "(intro 6.5/6.0 = the BC row; Appendix C '9'; Table 6 Voyager 9.25/7.83), and §4.1 says 'no baseline exceeds "
        "milestone 8', which contradicts the 9.25 mean. RS → son55 C08 (IDM inverse mapping over naturally "
        "occurring video, failure-targeted retrieval, cluster gate, iterate). Domain → sol H04 + H28.",
        "2605.14392 EvoEnv: OUT OF SCOPE. This is a shared-error correction: both seats wrote 'reviewed'. Under A3 "
        "bullet 1 the improver's update object and product are both weights. One shared policy is GRPO-trained in "
        "both roles (opus:O01, opus:O05). Every reported number is a trained checkpoint (opus:O03), and the "
        "ablations change the generator reward used for policy training (opus:O04). The environment pool is RL "
        "training data: it is retired after a fixed number of solver epochs (opus:O02), it is never read by an "
        "evaluated agent at test time, and it is never transferred to a fresh solver. A3 explicitly covers this "
        "case ('even if code is generated and reused in the process'). Precedents: CoEvolve r17a, DreamGym r07b "
        "(Opus overturned both seats), Agent-World r16b, R-Zero/SPELL. Not scored (seats 61.25 / 63.75). "
        "Informational C08 + H22.",
        "2605.15461 DrugSAGE (seat Δ5): final 61.25. X → son55 2. The cross-task memory is append-all (every "
        "executed candidate is written back), with no admission gate, versioning, expiry or rollback. The search and "
        "transfer hyperparameters (α, β, λ, γ, δ) and the order in which the 16 source tasks fill the memory are not "
        "stated. Shared correction: E.measurement 3 → 2. The analog-task ablation reports 'TDC leaderboard best' "
        "values of 0.820/0.898/0.728 (opus:O01), but Table 2 and Table 6 give 0.859/0.916/0.790 for the same "
        "targets (opus:O02, opus:O04). On CYP2D6, the 0.733 'remains competitive' claim is therefore 0.057 below the "
        "paper's own leaderboard value. The abstract's '33 tasks, single-task, nine agents' also conflicts with the "
        "body (22 TDC tasks, eight baselines; son55's finding). Run convention: text–table contradictions cap "
        "E.measurement at 2. RS → adapt_via_conditioning, sub null (r17b convention). heterogeneous_decomposition is "
        "not kept. Domain → H03 + H15. H02 is not kept: the skills come from literature, not from the agent's own "
        "outcomes.",
        "2605.15611 TopoEvo (Δ1.25): final 28.75, below both seats (33.75 / 35.0); each item was decided "
        "separately. X → son55 1: the memory's read interface is never described. The write gate ('solved "
        "incidents'), the refresh rates, τ/γ of Eq. 19, the TTA confidence thresholds and top-K/H are all "
        "unspecified, and there is no versioning or rollback. E.measurement → sol 1. Text and tables disagree "
        "repeatedly. Text says TAMO is stronger on B Acc@1, but the table has 75.66 vs 72.22. The prose gives "
        "ablation values 56.10/74.10/61.10/58.10 and a 'full 71.90' on B that appear nowhere in Table II. "
        "'15–16 points on all subsets' does not hold for B (19.8), and '≥8 points' fails on A_s (7.68) and A_n (7.29). "
        "MRR, latency and faithfulness are defined but never reported, and no denominators are given. "
        "E.causality → sol 1: the only retention-relevant ablation (w/o SEM) removes the memory and the "
        "weight-side TTA together, and both may run on the evaluated incidents (opus:O05). The MOMA/VQ/HET "
        "ablations keep it above 0. RS → sol C13 primary + son55 C25 supporting (C08 not kept).",
        "2605.15701 H-Mem (Δ12.5): final 57.5. G → son55 2: the gap is a combination gap defined by the paper's own "
        "taxonomy. The table narrows 'evolution' so that EverMemOS/Zep look incomplete, and there is no failure "
        "analysis. M → sol 3: son55's main reason was that there is no execution-feedback loop, which judges a "
        "B-class component as if it were A-class (SCORE_SPEC: A/B is an inclusion type, not a quality grade). The "
        "tree/graph operations map onto both stated gap halves, and the ablations test both. X → sol 3: the static "
        "build/retrieve flow is reconstructable down to the hyperparameters (windows; thresholds 0.8/0.7/0.6; weights "
        "0.70/0.15/0.15; τ = 365 d; η = 0.5; entity-resolution rules; prompts). It has no admission gate, deletion or "
        "versioning. E.cost → sol 2: five cost dimensions are measured, but the text gives only ordinal positions "
        "(values are in the Figure 2 image, not read), there is no budget-matched comparison, and H-Mem uses more "
        "indexing/retrieval tokens than most baselines. Paper facts recorded: fixed-Mixed retrieval matches "
        "accuracy (92.21 vs 92.01) at 1.8× tokens; top-k is chosen on LoCoMo test; 'largest gains on temporal' is "
        "contradicted by the Accuracy cells.",
        "A4 hygiene. Same-ID collisions on different questions were renumbered: 15611 son55 local-1 (drift) → "
        "local-3, and 15701 son55 local-1 (no dev set) → local-3. Same-question pairs were merged: 15611 son55 "
        "local-2 → local-1, plus the existing shared IDs 14211 local-1, 14392 local-1 and 15461 local-1.",
        "Expectations from cards that are not kept as pattern matches are retained as check questions with a note; "
        "they never score directly. These are generative_process_redesign (14211), evidence_gated_retention H30 "
        "(14392), abstract_experience_into_guidance (15701), and adapt_via_conditioning RE-* on 15701, whose "
        "adapt_via_conditioning match is kept as supporting.",
        "Figure dependence: ASH Figures 2/4/6, EvoEnv Figures 3/4, DrugSAGE Figures 3–5 (memory ablation, API cost), "
        "TopoEvo Figures 5/6 and H-Mem Figures 2–4 are image-only. Only values stated in the text or tables are "
        "used; no value was read from an image. sol's H-Mem page-image request is non-blocking: E.cost=2 rests on "
        "the textual ordinal statements, and exact Figure 2 values could not move it to 3 without a budget-matched "
        "comparison.",
        "No material requests. The seats' requests for neighbour originals (VPT, RAEA, Agentomics, TAMO/Nezha, "
        "EverMemOS/Zep/MemTree) are non-blocking: no disputed rating depends on them.",
        "Card revision proposal (stage end, not applied): add to the A3/H28 note that coupled weight+memory learners "
        "stay in scope only when the non-weight memory is read at deployment and has its own removal control (ASH), "
        "and are out of scope when the context asset only feeds training (SEAgent r05b).",
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

    def pmap(s, p, i, **upd):
        m = prefix(copy.deepcopy(seat(s, p)["pattern_mapping"][i]), s)
        m.update(upd)
        return m

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

    def renum(old):
        return {"note": f"Renumbered from {old} (A4 hidden ID collision: the other seat used that ID for a different "
                        "question)."}

    def dropped_card(card):
        return {"note": f"Kept as a check question only: {card} is not retained as a pattern match in this final "
                        "record (see resolutions on *_pattern.matches)."}

    def rr(v):
        return {"status": "resolved", "rating": v}

    # =========================================================== 2605.14211 ASH (scope conflict)
    p = "2605.14211"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "we replace the w l w_{l} key moments with w l w_{l} frames sampled uniformly at random "
                              "from the agent’s trajectory during inference", "§4.5 Long-term Memory Analysis",
                    "The random-frame control is described only at inference. The paper does not say whether this "
                    "arm's policy was also trained with random-frame memory. If it was trained on key-moment prefixes, "
                    "the 7.75 → 6.00 drop can come from a train/inference input mismatch rather than from the value of "
                    "key-moment content.", kind="our_inference"),
            opus_ev(p, "O02", "Since we cannot perform dynamic bootstrapping with randomly sampled long memory, we "
                              "compare against Bootstrapped Agent + Long Memory", "§4.5",
                    "The content control runs under the fixed bootstrap schedule, four trajectories of four hours "
                    "(Table 2). It is not the configuration that produced the headline results."),
            opus_ev(p, "O03", "ASH completes an average of 11.2 Pokémon milestones compared to the next best baseline "
                              "which completes 9.", "Appendix C, milestone distribution",
                    "This is a third value for the strongest baseline, after the introduction's 6.5 (the BC row) and "
                    "Table 6's Voyager+Opus 5 at 9.25. Neither seat recorded it."),
            opus_ev(p, "O04", "We derive our milestones from online walkthroughs", "§4 Milestones",
                    "Milestones are defined from walkthroughs. The text never says how a milestone's completion is "
                    "detected during an 8-hour run: automatic RAM/state readout, a visual detector, or manual "
                    "annotation.", kind="our_inference"),
            opus_ev(p, "O05", "removes both the long-term memory and dynamic bootstrapping, fixing the bootstrap "
                              "interval to", "§4.2 Component Ablations",
                    "This is the store-off arm. 'Bootstrapped Agent' has no long-term memory channel, and '+ Long "
                    "Memory' adds it back under the same fixed schedule. The +2.5 milestones (sol:E005) is this "
                    "contrast. Each arm is four shared-policy trajectories."),
            opus_ev(p, "O06", "is built by applying the HDBSCAN [ 40 ] clustering algorithm over the embeddings of",
                    "§3 Discovering key moments",
                    "The non-weight classifier K is re-fitted at every bootstrap on newly retrieved video plus all "
                    "previous embeddings. No arm freezes K after initialisation, so the effect of updating the "
                    "memory's admission rule is never separated from the weight retraining that happens in the same "
                    "bootstrap.", kind="our_inference"),
            opus_ev(p, "O07", "At each step, agent n n reads the w l w_{l} most recent key moments from its memory bank",
                    "§3 Inference",
                    "The non-weight memory is read by the deployed policy at every action. This is the A3 bullet-2 "
                    "fact separating ASH from the out-of-scope cases where the non-weight asset only feeds training."),
            opus_ev(p, "O08", "The strongest baseline gets stuck in both environments, achieving an average of 6.5 6.5 "
                              "and 6.0 6.0 milestones, respectively.", "§1 Introduction",
                    "6.5/6.0 are the BC row of Table 6. Voyager+Opus 5 is reported at 9.25/7.83 there and in the "
                    "abstract (son55's finding, with the numbers)."),
        ],
        "paper_update": {"scope_note": "Opus: in scope (A3 bullet 2). The key-moment memory (classifier K and per-agent "
                                       "bank) is a non-weight object, read by the deployed policy at every step and "
                                       "evaluated by memory-off and random-frame controls. Weight-side bootstrapping "
                                       "gains are not credited as harness evidence."},
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus: son55's card. The paper's core move is C08: an inverse (artifact→specification) mapper "
                      "(the IDM) labels naturally occurring internet video, the data is steered to the learner's "
                      "current failure region (the stuck trigger), passed through a gate (one-to-one window matching, "
                      "≥30-trajectory cluster recurrence) and used for retraining, and the procedure iterates. The "
                      "real target is measured directly (game milestones), and the 94% vs 8% retrieval-relevance "
                      "audit links the intermediate property to the target. sol's generative_process_redesign is not "
                      "kept: the 'fixed component' it names (static corpus, fixed IDM) is exactly C08's coverage "
                      "defect, and C08 already describes the dynamic loop. sol's supporting adapt_via_conditioning is "
                      "not kept either: the memory conditions a policy that is retrained, not one that adapts "
                      "without retraining.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", role="primary",
                               reason="Opus final: IDM inverse mapping + failure-targeted retrieval + cluster/matching "
                                      "gate + iterate + real-target milestones = C08. Fit partial: retrieval, not "
                                      "synthesis, so the data cannot leave the corpus's support.")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("sol", p, "index_experience_for_reuse", "H04")],
                           "unassigned": [],
                           "reason": "Opus sides with sol. H28 is a boundary card that lists papers whose harness part "
                                     "is load-bearing. Its success condition S3 holds (the policy is trained to "
                                     "condition on the memory artifact), but its failure mode F1 (weight-side "
                                     "machinery carries the paper) also largely applies. H04: the content is raw "
                                     "frames, the index is the cluster boundaries, the read is selective (the last "
                                     "10), and there is a removal control.",
                           "revision_proposals": ["A3/H28 note: coupled weight+memory learners stay in scope only "
                                                  "when the memory is read at deployment and has its own removal "
                                                  "control (see batch notes)."]},
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": "C08",
            "domain": {"namespace": "rsi", "main": "couple_context_and_weight_updates", "sub": "H28"},
            "operation_correspondence": "The same stuck-triggered retrieved set D^R feeds both levers: it re-fits the "
                                        "non-weight key-moment classifier K and, after IDM labelling, retrains the "
                                        "memory-conditioned policy. That is C08's generate–gate–retrain loop over "
                                        "H28's shared-data interface.",
            "necessary_conditions": "A shared retrieved stream and a policy trained to read the memory prefix.",
            "differences": "No context-only / weight-only / coupled comparison on unseen tasks (H28 step 5). "
                           "Adaptation and evaluation run on one stream (F5).",
            "evidence_ids": ["sol:E001", "sol:E003", "opus:O06", "opus:O07"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "rs:generative_process_redesign/RE-1": dropped_card("generative_process_redesign"),
                "rsi:couple_context_and_weight_updates/F5": {
                    "status": "unmet",
                    "reason": "Opus (sol's status; son55 left 'unknown' as out of scope). The complete text was read: "
                              "adaptation and reported progress run on the same gameplay stream, and the only "
                              "replay (§4.6) re-runs the same game with frozen weights. No split is declared."},
                "local:2605.14211-1": {
                    "reason": "Merged (same question in both seats). The strongest-baseline value takes three forms: "
                              "6.5/6.0 in the introduction (the BC row, opus:O08), '9' in Appendix C (opus:O03), and "
                              "9.25/7.83 in Table 6 and the abstract. §4.1's 'no baseline exceeds milestone 8' "
                              "contradicts the 9.25 mean. Unmet."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O03", "opus:O08"]), "C2", ["opus:O01", "opus:O06"]),
        "assessment": assess("sol", p, [
            "Opus: the random-frame control is described only at inference (opus:O01), so the 1.75-milestone content "
            "effect may include train/inference mismatch.",
            "Opus: no frozen-K arm separates the memory's feedback-driven update from weight retraining (opus:O06).",
            "Opus: milestone detection procedure not described (opus:O04)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats (sol 3; son55 did not score under its out_of_scope reading). The bottleneck "
                   "is concrete and demonstrated by the baselines plateauing: a fixed corpus and IDM do not cover later "
                   "mechanics, and bounded short memory loses history needed for decisions (Appendix A, Fig. 8 "
                   "example). The lineage VPT → RAEA → Voyager is explicit and empirically compared. Not 4: memory-side "
                   "neighbours (memory-augmented architectures, skill libraries) are only named in one sentence.",
                   ["sol:E001", "sol:E010", "sol:E015", "son55:E011"]),
            "M": R("resolved", 3, "Opus = sol. Novelty against clusters admits memories and drives the stuck trigger. "
                   "Retrieval targets the current roadblock, and the IDM's use of future frames makes labelling easier "
                   "than policy learning. Each operation answers a stated failure, and the key-moment vs random-frame "
                   "prediction is checkable. Not 4: 'recurring across ≥30 trajectories = key moment' is an assumption, "
                   "and only 48% of sampled clusters pass the authors' key-moment check.",
                   ["sol:E001", "sol:E002", "sol:E003", "sol:E005"], ["sol:E007", "sol:E010"]),
            "X": R("resolved", 3, "Opus = sol. Algorithms 1–5 plus the settings (N=4, w_s=64, w_l=10, k=100, w_r=540, "
                   "c_min=30, Δ=4800, 10% held-out samples, initial checkpoints) make the loop reconstructable, "
                   "including halt/resume and the per-step memory read (opus:O07). Thin points: no memory "
                   "retirement other than recency, no rollback of a harmful bootstrap, and an unstated milestone "
                   "detection procedure (opus:O04).",
                   ["sol:E002", "sol:E003", "sol:E007", "sol:E016", "opus:O07"], ["opus:O04"]),
            "E.measurement": R("resolved", 2, "Opus = sol, at the run's cap for text–table contradictions. Milestones are "
                               "defined (Tables 3–4), and their uneven spacing is audited against five human "
                               "walkthroughs (Table 5). Retrieval and cluster quality are human-annotated. But the "
                               "headline baseline magnitude is internally inconsistent: 6.5 in the introduction, '9' in "
                               "Appendix C, 9.25 in Table 6, and '§4.1: no baseline exceeds 8' (opus:O08, opus:O03, "
                               "sol:E011, sol:E012). Completion detection is undescribed (opus:O04).",
                               ["sol:E011", "sol:E013", "sol:E007", "opus:O03", "opus:O08"],
                               ["sol:E012", "son55:E013", "opus:O04"]),
            "E.causality": R("resolved", 2, "Revised (sol 3; son55 unscored). Relevant controls exist. The memory-off arm "
                             "(opus:O05) gives +2.5 milestones under the same fixed schedule, plotted against online "
                             "GPU hours. Fixed vs dynamic scheduling gives +1.5, and key-moment vs random-frame memory "
                             "gives 7.75 vs 6.00. Two gaps keep this at 2 rather than 3. (1) The random-frame control is "
                             "stated only at inference (opus:O01), so the content effect is confounded with a "
                             "train/inference mismatch. (2) No frozen-K arm isolates the retained component's "
                             "feedback-driven update from the weight retraining in the same bootstrap (opus:O06). The "
                             "headline baseline contrast also compares different information sources (400 h of "
                             "curated data for VPT/BC, the Opus 5 API for Voyager). This follows the run convention "
                             "that a clean store-off without the non-feedback arm is 2.",
                             ["sol:E005", "sol:E006", "opus:O05", "opus:O02"], ["opus:O01", "opus:O06"]),
            "E.holdout": R("resolved", 1, "Opus = sol. Adaptation and reported progress share one stream (H28 F5 unmet). "
                           "The 10% split is sample-level early stopping, IDM testing uses a separate playthrough, and "
                           "the §4.6 replay re-runs the same game. No held-out game, and no frozen-memory transfer.",
                           ["sol:E008", "sol:E009", "sol:E016"]),
            "E.statistics": R("resolved", 2, "Opus = sol (A2 tier 2). The main result is a mean ± std over 12 "
                              "trajectories from 3 ASH training runs (one trained policy per baseline), and there are "
                              "negative component outcomes. No significance test or CI. The ablations are four "
                              "shared-policy trajectories, i.e. one training run per arm.",
                              ["sol:E004", "sol:E008", "sol:E011"]),
            "E.cost": R("resolved", 2, "Opus = sol. A 288-GPU-hour cap (4×H100) applies to all methods, the "
                        "initialisation runs (3 and 9 GPU h) are stated, the ablations are plotted per online GPU hour, "
                        "and Table 10 uses 96-GPU-hour runs. Missing: DINOv2 indexing of about 39k videos, the "
                        "Voyager+Opus 5 API spend, and the actual ASH total.",
                        ["sol:E014", "sol:E004"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v5 HTML text read (body, Algorithms 1–5, Tables 1–14, Appendices A–I). In scope "
                  "under A3 bullet 2. The key-moment memory (classifier K + per-agent bank) is a non-weight component "
                  "that is updated at stuck-triggered bootstraps and read by the deployed policy at every step "
                  "(opus:O07), with removal and content controls (opus:O05, sol:E006). This follows the run's RMM "
                  "(r02b) and PsychAgent (r13b) rulings. Weight-side bootstrapping gains are not counted as harness "
                  "evidence. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "in scope (A3 bullet 2), sol over son55: the key-moment memory (K + per-agent bank) is non-weight, is read "
              "by the deployed policy at every step, and is evaluated by memory-off (−2.5) and random-frame (7.75 vs "
              "6.00) controls. Unlike SEAgent/DreamGym/EvoEnv, its non-weight asset is not only training data.",
        "improver_check": "not claimed; the bootstrap procedure itself is fixed.",
        "figure_dependence": "Figures 2 and 4 (milestone curves, ablation curves) and Figure 6 (replay) are image-only. "
                             "The text/table values (Table 6, +2.5/+1.5, Table 2) are used.",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "sol", "system_method",
                "In scope, so the claim type follows the author's system claim (a self-improving agent system). "
                "son55's component_training went with its out_of_scope reading.", ["sol:E005", "opus:O07"],
                "none (claim_type does not change weights)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "Adaptation and evaluation share one stream, and nothing is frozen and transferred, so not retained. "
                "son55's null went with out_of_scope.", ["sol:E008", "sol:E009"], "none (label is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "sol", "scoped",
                "The narrow claim is supported (selected key-moment memory plus stuck-triggered retraining improves "
                "same-game progression). The broad 'scalable recipe' is not. son55's 'unresolved' was the scope "
                "question, now resolved.", ["sol:E005", "sol:E006", "sol:E011"], "none (label is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "self_supervised_signal_engineering",
                "See rs_pattern.reason.", ["son55:E002", "son55:E003", "son55:E012"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "C08 kept. sol's generative_process_redesign and adapt_via_conditioning are rejected (see "
                "rs_pattern.reason).", ["son55:E002", "son55:E003", "son55:E007", "son55:E012"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["couple_context_and_weight_updates", "H28"], ["index_experience_for_reuse", "H04"]],
                "son55 left this empty under out_of_scope and noted H28 fit=low because 'the memory bank is not an "
                "editable context artifact the policy is trained to read'. That is contradicted by the text: the "
                "policy is trained with K-constructed memory prefixes (Algorithm 4) and reads them at inference "
                "(opus:O07).", ["sol:E001", "sol:E003", "opus:O07"], NOSCORE),
            XC(p, "local:2605.14211-2", "sol", "partial",
               "sol-only question (cost accounting). Verified: there is a GPU cap and GPU-normalised curves, but no "
               "indexing/API totals.", ["sol:E014"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "Kept as a check question (card not retained). Verified: there are fixed-vs-dynamic and memory "
               "removals, but no factorial.", ["sol:E005"]),
            XC(p, "rsi:couple_context_and_weight_updates/F5", "sol", "unmet",
               "son55 left 'unknown' because it did not evaluate an out-of-scope row. The complete text shows no "
               "declared split between the adaptation and reported streams.", ["sol:E008", "sol:E016"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "sol", "partial",
               "sol-only. Verified: admission is cluster recurrence, not an external utility check.",
               ["sol:E002", "sol:E007"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "sol", "met",
               "sol-only. A store-removal arm exists (opus:O05). Its weaknesses are scored in E.causality=2, not "
               "here.", ["sol:E005", "opus:O05"]),
            RC(p, "G", "sol", rr(3), "See ratings.G. son55's unknown was the out_of_scope consequence.",
               ["sol:E001", "sol:E015"], "+11.25 vs son55's unscored row"),
            RC(p, "M", "sol", rr(3), "See ratings.M.", ["sol:E002", "sol:E003"], "+15 (row now scored)"),
            RC(p, "X", "sol", rr(3), "See ratings.X.", ["sol:E003", "opus:O07"], "+15 (row now scored)"),
            RC(p, "E.measurement", "sol", rr(2), "See ratings.E.measurement; Appendix C's '9' added (opus:O03).",
               ["sol:E011", "opus:O03"], "+5 (row now scored)"),
            RC(p, "E.causality", "revised", rr(2), "Neither seat: sol's 3 is lowered because of the inference-only "
               "random-frame control and the missing frozen-K arm (opus:O01, opus:O06).",
               ["opus:O01", "opus:O05", "opus:O06"], "−3.75 vs sol"),
            RC(p, "E.holdout", "sol", rr(1), "See ratings.E.holdout.", ["sol:E008", "sol:E016"], "+2.5 (row now scored)"),
            RC(p, "E.statistics", "sol", rr(2), "See ratings.E.statistics.", ["sol:E004", "sol:E008"],
               "+2.5 (row now scored)"),
            RC(p, "E.cost", "sol", rr(2), "See ratings.E.cost.", ["sol:E014"], "+2.5 (row now scored)"),
            res("status", *C(p, "status"), "sol", "reviewed",
                "A3 bullet 2 (see reason and the a3 note). son55 flagged the long-memory ablation as a boundary item "
                "for re-check; the re-check finds the memory is read at deployment (opus:O07) and has its own "
                "removal control (opus:O05). This matches RMM (r02b), where a separately ablated non-weight memory "
                "bank kept a paper with a weight-trained module in scope.",
                ["opus:O05", "opus:O07", "sol:E006", "son55:E007"], "son55 null → 61.25"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v5 text first. The improvement is mostly carried by "
                                                   "π/IDM weights, but a non-weight key-moment memory is updated, "
                                                   "read at every step and ablated twice. Leaned in scope (A3 bullet "
                                                   "2), with E.causality limited by inference-only random frames and "
                                                   "no frozen-K arm.",
            "integrity_checks": "Both seats a1 on 2605.14211v5, material sha 506c1991…; canonical seat hashes equal "
                                "conflicts.json. son55 completed identification for its excluded row.",
            "core_claim_check": "Table 6, §4.2, Table 2, Table 9–11 and the three strongest-baseline values re-read.",
            "shared_error_review": "No shared rating error (son55 did not score). Both seats missed Appendix C's third "
                                   "value (opus:O03); recorded in E.measurement.",
            "rating_agreement": "All items = sol except E.causality (revised 3 → 2). Final 61.25.",
        },
    }

    # =========================================================== 2605.14392 EvoEnv (shared scope correction)
    p = "2605.14392"
    OOS = ("out_of_scope (rubric A3 bullet 1; shared-error correction, since both seats wrote 'reviewed'). The improver's "
           "update object and product are both weights. One policy plays generator and solver, and the two roles "
           "'share parameters' and are optimised with one role-conditioned GRPO objective (opus:O01, opus:O05). Every "
           "reported number is the resulting trained policy on external benchmarks or 50 unseen RLVE environments "
           "(opus:O03). The ablations change the generator reward that trains the policy (opus:O04). The retained "
           "non-weight object, the executable environment pool, is RL training data: environments are sampled for "
           "solver rollouts and retired after a fixed number of solver epochs (opus:O02). No evaluated agent reads "
           "them at test time, and the pool is never frozen and transferred to a fresh solver. A3 bullet 1 states "
           "this case: out_of_scope 'even if code is generated and reused in the process'. Run precedents: CoEvolve "
           "(r17a), DreamGym (r07b, where Opus overturned both seats' in-scope readings), Agent-World (r16b), "
           "R-Zero/SPELL. Flip condition: the evolved pool is evaluated as a reusable artifact, e.g. frozen and used to "
           "train a fresh solver against an equally sized static pool, or released and certified as a benchmark "
           "resource. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "We normalize advantages within solver groups and generator groups separately, then "
                              "optimize the shared policy with a role-conditioned GRPO objective:", "§3.4",
                    "Generator and solver are one set of GRPO-updated weights."),
            opus_ev(p, "O02", "After an environment has been used for a fixed number of solver epochs, it is retired from",
                    "§3.4 Pool rotation",
                    "Pool membership exists to supply solver training rollouts (and few-shot seeds for the generator "
                    "prompt during training). It is consumed by training, not read by an evaluated agent."),
            opus_ev(p, "O03", "Nevertheless, the resulting policy improves on external benchmarks with different formats",
                    "§4.2", "The evaluated object is the trained policy."),
            opus_ev(p, "O04", "Each ablation removes one component while keeping training steps, seeds, and evaluation "
                              "protocol identical to the full EvoEnv run on Qwen3-4B-Thinking-2507.", "§4.5",
                    "The only component ablations change the generator reward, i.e. the training procedure of the "
                    "weights. There is no pool-transfer or pool-off-at-test arm."),
            opus_ev(p, "O05", "The two roles use distinct prompts but share parameters.", "§3.4",
                    "Same as O01: shared weights."),
        ],
        "paper_update": {"scope_class": "out_of_scope (Opus, A3 bullet 1)"},
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope). Both seats chose C08 (a generator of code-defined task "
                      "distributions, a layered admission gate, retraining, iteration), which is the run convention "
                      "for proposer–solver co-training. sol's supporting generative_process_redesign is not kept. "
                      "Scope is decided by A3, not by the card match.",
            "matches": [smatch("son55", p, "self_supervised_signal_engineering", fit="informational (out_of_scope)",
                               role="primary")],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "self_generate_the_curriculum", "H22",
                                              fit="informational (out_of_scope)")],
                           "unassigned": [],
                           "reason": "Informational (out_of_scope). Both seats chose H22, a boundary card that includes "
                                     "weight-trained members. son55's H30 is not kept: retirement is by epoch count, "
                                     "not by evidence-gated retention of a harness artifact.",
                           "revision_proposals": []},
        "pattern_mapping": [{
            "rs_main": "self_supervised_signal_engineering", "rs_sub": "C08",
            "domain": {"namespace": "rsi", "main": "self_generate_the_curriculum", "sub": "H22"},
            "operation_correspondence": "Informational. The policy authors executable environments, the L1–L5 / "
                                        "self-review / pass-rate / novelty gates admit them, and the solver role "
                                        "trains on them.",
            "necessary_conditions": "Frozen executable scorers and a solver-relative difficulty signal.",
            "differences": "The evaluated product is weights (A3 bullet 1).",
            "evidence_ids": ["opus:O01", "opus:O02", "son55:E003"]}],
        "expectations": lambda sol, son: [
            dict(e, informational=True,
                 reason="Informational (row out_of_scope; not scored). " + str(e.get("reason", "")))
            for e in merge_exps(p, sol, son, rename={}, overrides={
                "rsi:self_generate_the_curriculum/S5": {
                    "status": "unmet",
                    "reason": "son55's status. No actual GPU hours, tokens or rollout totals are reported. The "
                              "configuration counts in Table 9 are settings, not cost (r12a UI-Mem precedent)."},
                "rsi:evidence_gated_retention/S2": dropped_card("evidence_gated_retention"),
            })],
        "claims": lambda c: add_counter(c, "C1", ["opus:O03", "opus:O04"]) if any(x.get("claim_id") == "C1" for x in c) else c,
        "assessment": assess("sol", p, [
            "Out-of-scope disposition is not a judgment that the RL results are wrong.",
            "Boundary recorded with a flip condition (see reason)."],
            evidence_level=None,
            evidence_level_note="No harness evidence label for an out-of-scope weight-level paper (run convention). "
                                "Both seats wrote 'task'; normalized to null (shared correction).",
            claim_support=None,
            claim_support_note="Not assessed under this rubric. The gains are author-reported RL checkpoint results.",
            strongest_supported_claim=None),
        "ratings": {k: R("unknown", None, OOS, ["opus:O01", "opus:O02", "opus:O03"]) for k in RK},
        "status": "out_of_scope",
        "reason": OOS,
        "aggregate_status": "accepted_final",
        "a3": "out_of_scope (A3 bullet 1; shared-error correction, both seats 'reviewed'): the shared generator/solver "
              "policy is GRPO-trained, every result is a checkpoint, and the environment pool is RL training data "
              "never read at test time or transferred (CoEvolve r17a / DreamGym r07b precedent).",
        "improver_check": "not applicable (out_of_scope).",
        "figure_dependence": "Figures 3–4 are image-only; not used (row not scored).",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55",
                [["self_supervised_signal_engineering", "C08"]],
                "Informational. C08 agreed; sol's generative_process_redesign is not kept (run convention for "
                "proposer–solver co-training).", ["son55:E003", "son55:E005"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["self_generate_the_curriculum", "H22"]],
                "Informational. H22 agreed; son55's H30 is not kept (retirement by epoch count is not "
                "evidence-gated retention of a harness artifact).", ["son55:E006", "opus:O02"], NOSCORE),
            XC(p, "local:2605.14392-2", "sol", "met",
               "Informational (row out_of_scope). sol-only question (seed/knowledge disclosure); the ten seeds and "
               "their archive origin are disclosed in Appendix F.", ["sol:E011"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial",
               "Informational (row out_of_scope). son55-only; the scope limit is stated in Appendix H.",
               ["son55:E019"]),
            XC(p, "rsi:evidence_gated_retention/S2", "son55", "partial",
               "Informational (row out_of_scope; card not retained).", ["son55:E006"]),
            XC(p, "rsi:self_generate_the_curriculum/S2", "son55", "partial",
               "Informational (row out_of_scope). son55-only; m=8 single-response calibration on the candidate's "
               "own instances.", ["son55:E005"]),
            XC(p, "rsi:self_generate_the_curriculum/S5", "son55", "unmet",
               "Informational (row out_of_scope). No actual cost is reported; configuration counts are settings, "
               "not cost.", ["son55:E021", "sol:E014"]),
            RC(p, "E.holdout", "revised", {"status": "unknown", "rating": None},
               "Out-of-scope rows carry all eight items as unknown. For the record only (not a score): Opus would "
               "side with sol's 2, not son55's 3. The external benchmarks are disjoint from training, but there is "
               "no contamination audit for AIME'24/'25 on Qwen3 pretraining, and four seeds come from public archives.",
               ["opus:O03", "sol:E006", "sol:E011"], "none (not scored)"),
        ],
        "shared_error_corrections": [
            {"field_path": "status / scope", "sol_value": "reviewed (scope_class A)", "son55_value": "reviewed (boundary)",
             "final_value": "out_of_scope",
             "reason": "Both seats read A3 bullet 2 ('the evaluated retained object is a non-weight harness "
                       "component'). But the pool is not an evaluated object. All results come from the trained "
                       "policy (opus:O03), the ablations change training (opus:O04), and the pool exists to produce RL "
                       "rollouts (opus:O02). Both seats' own records say the gain is carried by the weights and that no "
                       "fresh-solver frozen-pool test exists (sol assessment; son55 status reason). A3 bullet 1 applies "
                       "('even if code is generated and reused').",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "son55:E016"],
             "score_impact": "row not scored (sol 61.25, son55 63.75 → null; L=0, U=100, coverage 0)"},
            {"field_path": "assessment.evidence_level / assessment.claim_support",
             "sol_value": ["task", "scoped"], "son55_value": ["task", "scoped"], "final_value": [None, None],
             "reason": "Out-of-scope rows carry null level and support (run convention).",
             "evidence_ids": ["opus:O01"], "score_impact": "none (not scored)"},
            {"field_path": "ratings.G, ratings.M, ratings.X, ratings.E.measurement, ratings.E.causality, "
                           "ratings.E.statistics, ratings.E.cost",
             "sol_value": "resolved 3/3/3/2/2/1/1", "son55_value": "resolved 3/3/3/2/2/1/1",
             "final_value": "unknown ×7 (E.holdout is handled in resolutions)",
             "reason": "Consequence of the scope correction. The agreeing seat values are kept only as the "
                       "informational shadow in aggregate_review.",
             "evidence_ids": ["opus:O03"], "score_impact": "none (not scored)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole v1 text with appendices first. A single "
                                                   "GRPO-trained policy acts as generator and solver, every result is "
                                                   "a checkpoint, and the environment pool is training data. Leaned "
                                                   "out_of_scope (A3 bullet 1), against both seats.",
            "integrity_checks": "Both seats a1 on 2605.14392v1, material sha 180099a5…; canonical seat hashes equal "
                                "conflicts.json. sol's batch report says its a1 record was written in an earlier "
                                "continuation; the hash binding is what is checked.",
            "core_claim_check": "§3.4, §4.2–4.5 and Appendices E/F/I re-read for any pool-as-artifact evaluation; none "
                                "found.",
            "shared_error_review": "Scope (both 'reviewed') → out_of_scope; evidence_level/claim_support → null.",
            "rating_agreement": "Informational shadow only (not a score): the seats agree on G/M/X 3, E.measurement 2, "
                                "E.causality 2, E.statistics 1, E.cost 1 and differ on E.holdout (2 vs 3; Opus would "
                                "take 2), which gives 61.25. Not carried.",
        },
    }

    # =========================================================== 2605.15461 DrugSAGE (Δ5)
    p = "2605.15461"
    S[p] = {
        "base": "son55",
        "opus_evidence": [
            opus_ev(p, "O01", "DrugSAGE-zero remains competitive with the TDC leaderboard best on all three targets: "
                              "0.822 0.822 versus 0.820 0.820 on CYP2C9 inhibition, 0.892 0.892 versus 0.898 0.898 on "
                              "CYP3A4 inhibition, and 0.733 0.733 versus 0.728 0.728 on CYP2D6 inhibition.",
                    "§4.3 Impact of analog tasks",
                    "The 'leaderboard best' values here (0.820/0.898/0.728) do not match the leaderboard values the "
                    "paper itself tabulates for the same three tasks (0.859/0.916/0.790; opus:O02, opus:O04). Against "
                    "those, the analog-removed DrugSAGE-zero is 0.037/0.024/0.057 below the leaderboard, so 'remains "
                    "competitive with the TDC leaderboard best' is contradicted by the paper's own tables."),
            opus_ev(p, "O02", "The cross-task performance (without normalization) of DrugSAGE-zero on six TDC held-out "
                              "tasks.", "§4.2 Table 2 caption",
                    "Table 2's 'TDC Leaderboard Best' column lists CYP2C9 Inhibition 0.859 ± 0.001, CYP3A4 Inhibition "
                    "0.916 ± 0.000 and CYP2D6 Inhibition 0.790 ± 0.001 (table cells; HTML splits them across lines)."),
            opus_ev(p, "O03", "0.852 ± 0.003", "§4.2 Table 2, CYP2C9 Inhibition row",
                    "The full-pool DrugSAGE-zero CYP2C9 value. With the same-category source removed it drops to 0.822 "
                    "(opus:O01), against a tabulated leaderboard value of 0.859."),
            opus_ev(p, "O04", "Per-task scores on the TDC-ADMET benchmark, reported as mean", "Appendix D Table 6 caption",
                    "Table 6's Leaderboard column for the CYP inhibition rows reads 0.859 ± 0.001 (CYP2C9), "
                    "0.790 ± 0.001 (CYP2D6) and 0.916 ± 0.000 (CYP3A4), the same as Table 2 and not the values in "
                    "§4.3."),
            opus_ev(p, "O05", "the normalized score increases monotonically, while the cost decreases monotonically",
                    "§4.3 Importance of cross-task memory",
                    "The memory-off / Q-only / full ablation is reported only as a direction in the text. The values "
                    "are in Figure 4(b), an image, and were not read."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Opus: adapt_via_conditioning (both seats name it), sub null. The frozen Claude agent adapts to a "
                      "new task by conditioning on retrieved cross-task experience, and DrugSAGE-zero routes a "
                      "verified recipe by task signature with no search. C03 is not assigned (r17b convention): there "
                      "is no upstream phase that teaches a model to parse a unified schema, and the routing is a "
                      "metadata lookup of a recipe that is then retrained on the target. sol's primary "
                      "heterogeneous_decomposition is not kept: the R/H/Q split is a storage schema that the paper "
                      "never contrasts with a uniform store of the same content, so the card's tactic (showing that "
                      "uniform treatment is suboptimal) is not executed.",
            "matches": [smatch("son55", p, "adapt_via_conditioning", sub_id=None, role="primary",
                               reason="Opus final: conditioning a frozen agent on retrieved cross-task experience; "
                                      "recipe routing at B=0. C03's upstream-parsing tactic is absent, so sub null.")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("sol", p, "index_experience_for_reuse", "H03"),
                                       dmatch("son55", p, "population_search_executable_fitness", "H15")],
                           "unassigned": ["H02 not kept: the skill library is built from literature/GitHub "
                                          "(Appendix H), not mined from the agent's own interaction outcomes."],
                           "reason": "H03 (both seats): whole verified recipes are stored and retrieved for the "
                                     "closest analog task. H15 (son55): the refinement memory stores child-vs-parent "
                                     "validation deltas and rationales and conditions the next LLM edit proposals "
                                     "across tasks, which is H15's 'credit by child-versus-parent fitness change'.",
                           "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0, rs_sub=None,
                                 note="Opus: rs_sub set to null (C03 not assigned in the final record)."),
                            pmap("son55", p, 1, rs_sub=None,
                                 note="Opus: rs_sub set to null (C03 not assigned in the final record).")],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "local:2605.15461-1": {
                    "status": "unmet",
                    "reason": "Merged (same question: whole-lifecycle cost amortisation). Opus = son55: test-time "
                              "API cost is shown (Figure 4a; text qualitative), but building the 16-task memory and "
                              "the literature skill library (24 h per task cap, LLM calls) is never costed. The "
                              "test-time reporting is credited in E.cost=2, not here."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C4", ["opus:O01", "opus:O02", "opus:O04"]), "C3", ["opus:O05"]),
        "assessment": assess("son55", p, [
            "Opus: the analog-task ablation's 'leaderboard best' values (0.820/0.898/0.728) contradict Tables 2 and 6 "
            "(0.859/0.916/0.790) (opus:O01, opus:O02, opus:O04).",
            "Opus: memory-ablation values are figure-only (opus:O05)."],
            evidence_level="retained",
            evidence_level_note="Opus (both seats): memory is built on 16 source tasks and read on 17 held-out "
                                "targets (11 Polaris tasks never enter Z). The store-off comparison on the held-out "
                                "TDC targets (Figure 4b) is stated in text as monotone (opus:O05). Its values are "
                                "figure-only, which limits E.causality, not the level."),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. Search is repeated from scratch on every task. Baselines "
                   "with only within-task memory are compared, and Agentomics is named as the closest neighbour. "
                   "Not 4: no other cross-task-memory ML agent is compared, and the neighbours are checked only as "
                   "this paper describes them.",
                   ["son55:E001", "son55:E002", "son55:E011", "sol:E015"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Each memory type feeds one search interface (family "
                   "prior via UCB, parent sampler, edit grounding, verified repair), and B=0 routing is specified. "
                   "Not 4: transferability is assumed from metric/type/size/description similarity, and the "
                   "regret theorem is a weak, order-only guarantee.",
                   ["son55:E003", "son55:E004", "son55:E005", "son55:E007", "son55:E022"]),
            "X": R("resolved", 2, "Opus sides with son55. Read-side interfaces and the skill library's tiered "
                   "validation are clear. The cross-task memory, however, writes back every executed candidate with no "
                   "admission gate, deduplication, expiry, conflict handling or rollback (son55:E006). The "
                   "algorithm's own constants (α, β, λ in Eqs. 1/3; γ, δ in Appendix I) and the order in which the 16 "
                   "source tasks populate Z are not stated (full text searched). Main steps are described; "
                   "retention conditions are not (anchor 2).",
                   ["son55:E006", "son55:E008", "sol:E002", "sol:E012"]),
            "E.measurement": R("resolved", 2, "Shared correction (both seats 3). The official TDC 5-seed splits and "
                               "native metrics are trustworthy, and the per-task absolute tables exist. But the paper's "
                               "numbers contradict each other on claims it relies on. The §4.3 analog ablation quotes "
                               "leaderboard values 0.820/0.898/0.728 against the 0.859/0.916/0.790 in Tables 2 and 6 "
                               "(opus:O01, opus:O02, opus:O04). The abstract's '33 tasks, single-task, nine agents' does "
                               "not match the 22 TDC tasks and eight baselines (son55:E019, son55:E020). Headline gains "
                               "are on a min-max scale, and Biomni is not reproduced. Run convention caps text–table "
                               "contradictions at 2.",
                               ["son55:E020", "son55:E015", "son55:E027", "opus:O02", "opus:O04"],
                               ["opus:O01", "son55:E019", "son55:E021"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. DrugSAGE-anchor isolates the skill library, the "
                             "memory-off/Q/full ablation exists (direction only, opus:O05), and same-category sources "
                             "are removed on 3 targets. Missing: a B=0 'skill library, no memory' or fixed-best-recipe "
                             "arm, and baselines with K. The comparators lack both K and Z, so the 10–30% cannot be "
                             "attributed to memory.",
                             ["son55:E013", "son55:E016", "son55:E017", "sol:E007"],
                             ["son55:E011", "son55:E025", "opus:O05"]),
            "E.holdout": R("resolved", 3, "Both seats 3; re-checked. There are 16 source tasks and 17 targets, the 11 "
                           "Polaris tasks never enter Z, selection is on validation, and test is reported. Not 4: no "
                           "molecule-overlap or pretraining audit (the transferred recipes are leaderboard model "
                           "ensembles), and the 6 TDC targets share the benchmark.",
                           ["son55:E010", "son55:E012", "sol:E005", "sol:E006"], ["son55:E029"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 tier 2): per-task mean ± std over 5 seeds, plus "
                              "negative cases (LD50). No repeats of the agent search or memory construction, no "
                              "interval on the 17-task averages, no significance tests.",
                              ["son55:E027", "son55:E028", "sol:E014"]),
            "E.cost": R("resolved", 2, "Both seats 2; re-checked. A test-time API cost comparison exists (Figure 4a; "
                        "the text states the ordering and near-zero zero-search cost), along with the L40S/24 h cap "
                        "and the B mapping. Construction cost of Z and K and the cost of failed candidates are not "
                        "amortised.",
                        ["son55:E018", "son55:E023", "sol:E009", "sol:E010"], ["son55:E029"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (body, Tables 1–9, Appendices A–J). In scope (system_method): a "
                  "persistent non-weight cross-task memory and skill library are written from execution and read on "
                  "held-out tasks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree).",
        "improver_check": "not claimed; the search loop's own procedure is not edited.",
        "figure_dependence": "Figures 3 (budget curves), 4 (cost, memory ablation, analog ablation) and 5 are "
                             "image-only. Text values (0.90/0.97; 0.822/0.892/0.733) and Tables 1/2/6–9 are used.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "See rs_pattern.reason.", ["son55:E009", "sol:E005"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised", [["adapt_via_conditioning", None]],
                "Neither seat as is: son55's single main card with sol's null sub. sol's heterogeneous_decomposition "
                "is not kept.", ["son55:E009", "sol:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["index_experience_for_reuse", "H03"], ["population_search_executable_fitness", "H15"]],
                "H03 (both) + H15 (son55). son55's H02 is dropped because its source is literature, not the agent's "
                "own outcomes.", ["son55:E004", "son55:E008", "sol:E002"], NOSCORE),
            XC(p, "local:2605.15461-1", "son55", "unmet", "Same question in both seats; see the expectation reason.",
               ["son55:E029", "sol:E009"]),
            XC(p, "local:2605.15461-2", "son55", "unmet",
               "son55-only. Verified: the abstract says 33 tasks / nine agents for the single-task setting, but the "
               "body has 22 TDC tasks and eight baselines.", ["son55:E019", "son55:E020"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "partial",
               "son55-only. Verified: memory on/off exists only as a figure; the comparators are not matched.",
               ["son55:E016", "opus:O05"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "son55", "unmet",
               "son55-only. Verified: no overlap/contamination analysis; the routed recipes are ensembles of public "
               "leaderboard models.", ["son55:E012", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "son55-only. Verified: no 'top leaderboard recipe' or 'K without Z at B=0' arm.",
               ["son55:E011", "son55:E025"]),
            XC(p, "rsi:index_experience_for_reuse/F2", "son55", "partial",
               "son55-only. Verified: routing is by metric/type/size/embedding (Ames→BBB, CYP inhibition→CYP "
               "substrate). The analog-removal test covers 3 targets, and its leaderboard comparison is internally "
               "inconsistent (opus:O01).", ["son55:E022", "son55:E017", "opus:O01"]),
            XC(p, "rsi:index_experience_for_reuse/S1", "sol", "met",
               "sol-only. Verified: whole recipes are re-bound per target (Appendix G tables).", ["sol:E002", "sol:E008"]),
            XC(p, "rsi:population_search_executable_fitness/S2", "son55", "met",
               "son55-only. Verified: the official split and validation-based selection exist before the loop.",
               ["son55:E020", "son55:E023"]),
            XC(p, "rsi:population_search_executable_fitness/S5", "son55", "partial",
               "son55-only. Verified: H stores parent-child deltas, but there is no repeated-observation or "
               "negative-evidence gate.", ["son55:E004", "son55:E006"]),
            RC(p, "X", "son55", rr(2), "See ratings.X.", ["son55:E006", "son55:E008"], "−5 vs sol"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "reason": "Both seats accepted §4.3's 'competitive with the TDC leaderboard best' (son55 C4: '近排行榜'). "
                       "Neither compared its leaderboard values (0.820/0.898/0.728) with the paper's own Table 2 and "
                       "Table 6 values (0.859/0.916/0.790). son55 also recorded the abstract/body task-count mismatch "
                       "but still gave 3. With these contradictions the run convention caps E.measurement at 2.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O04", "son55:E019"],
             "score_impact": "−2.5 (sol 68.75 → 61.25 together with X; son55 63.75 → 61.25)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the whole text first. A real cross-task non-weight memory "
                                                   "with held-out targets. The causal share of memory vs the "
                                                   "literature skill library is unresolved, the memory is append-all, "
                                                   "and §4.3's leaderboard numbers contradict Tables 2/6.",
            "integrity_checks": "Both seats a1 on 2605.15461v1, material sha 99ffb363…; canonical seat hashes equal "
                                "conflicts.json. son55's numeric table evidence has null quotes (HTML cell splitting), "
                                "allowed per the controller's note.",
            "core_claim_check": "Tables 1, 2, 6, 8, 9, §4.2–4.3 and Appendices B/G/H/I re-read; CYP rows checked "
                                "cell by cell.",
            "shared_error_review": "E.measurement 3 → 2 (shared).",
            "rating_agreement": "X → son55 (2). Others agree except the shared E.measurement correction. Final 61.25.",
        },
    }

    # =========================================================== 2605.15611 TopoEvo (Δ1.25)
    p = "2605.15611"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "On the node level and Dataset B, although TAMO is stronger on Acc@1/3, TopoEvo "
                              "consistently ranks second and achieves the best Acc@5", "§IV-C1",
                    "Table I, Dataset B: TopoEvo Acc@1 75.66% vs TAMO 72.22%. The text reverses the direction for "
                    "Acc@1 on B (it holds for Acc@3: 79.80 vs 80.55)."),
            opus_ev(p, "O02", "w/o SEM decreases AC@1 from 66.10 % 66.10\\% to 58.10 % 58.10\\%", "§IV-D SEM",
                    "Table II gives A_p w/o SEM = 58.73, not 58.10. The prose values for MOMA (56.10, 74.10) and VQ "
                    "(61.10) also differ from Table II (56.38, 74.36, 60.92)."),
            opus_ev(p, "O03", "from 71.90 % 71.90\\% to 63.90 % 63.90\\%", "§IV-D SEM (Dataset B)",
                    "The B 'full' value 71.90 appears nowhere in Tables I–II (full B = 75.66; w/o SEM = 63.28)."),
            opus_ev(p, "O04", "w/o HET reduces AC@1 by 15 15 – 16 16 points on all subsets", "§IV-D HET",
                    "Table II: B drops 75.66 → 55.84 (19.8 points). Separately, the 'smaller but still notable drop (≥ 8 "
                    "points)' claimed for SEM fails on A_s (73.10 → 65.42 = 7.68) and A_n (84.10 → 76.81 = 7.29)."),
            opus_ev(p, "O05", "During deployment, high-confidence diagnoses (strong support, low missingness, and "
                              "consistent topology constraints) are treated as pseudo-labeled samples and accumulated "
                              "in a buffer", "§III-E2",
                    "TTA (a weight update) runs on the deployment stream. The evaluation protocol never says whether "
                    "the evaluated incidents are that stream, or whether the memory is written from them.",
                    kind="our_inference"),
            opus_ev(p, "O06", "For efficiency, we measure end-to-end diagnosis latency (wall-clock time per incident, "
                              "including agent/tool calls when applicable).", "§IV-A3",
                    "Latency, MRR and the topology-faithfulness score are announced but never reported in §IV."),
            opus_ev(p, "O07", "stores solved incidents as compact records consisting of candidate-centric topology "
                              "fingerprints", "§III-E1",
                    "The write unit is defined, but how a stored record is retrieved and used by the HET agents is "
                    "never described.", kind="our_inference"),
        ],
        "rs_pattern": {
            "primary": "structural_prior_encoding", "supporting": ["decompose_and_delegate"], "outside_taxonomy": False,
            "reason": "Opus: sol's primary plus son55's supporting card. The load-bearing idea in the title and "
                      "motivation is C13: the dependency topology is encoded in a GAT over the flattened "
                      "node/service/pod graph and then enforced on reasoning (an H-hop candidate subgraph, path "
                      "consistency). C25 is kept as supporting. HET decomposes diagnosis into planner, modality agents "
                      "and judge, which exchange structured, checkable artifacts (symptom tokens, cached evidence), "
                      "and its removal is the largest ablation drop. son55's C08 (pseudo-label TTA) is not kept: it is "
                      "a weight-side add-on with no generator or gate described.",
            "matches": [smatch("sol", p, "structural_prior_encoding", role="primary"),
                        smatch("son55", p, "decompose_and_delegate", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi", "matches": [dmatch("sol", p, "index_experience_for_reuse", "H04")],
                           "unassigned": ["TTA is a weight branch (not harness evidence)",
                                          "HET is within-incident verification, not a persistent improver"],
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.15611-1"): "local:2605.15611-3",
                    ("son55", "local:2605.15611-2"): "local:2605.15611-1"},
            overrides={
                "local:2605.15611-3": renum("son55:local:2605.15611-1"),
                "local:2605.15611-1": {
                    "reason": "Merged: sol local-1 and son55 local-2 ask the same question (text–table consistency). "
                              "Unmet: the B Acc@1 direction is reversed (opus:O01), four ablation values and a 'full "
                              "71.90' are absent from Table II (opus:O02, opus:O03), and two magnitude claims fail "
                              "(opus:O04)."},
                "rsi:index_experience_for_reuse/S5": {
                    "status": "partial",
                    "reason": "Opus = son55. A removal exists (w/o SEM), but it removes the memory and the "
                              "weight-side TTA together, so it is a bundled removal (partial), not a store-only "
                              "certification. The bundling is scored in E.causality=1."},
            }),
        "claims": lambda c: add_counter(c, c[0]["claim_id"], ["opus:O01", "opus:O02", "opus:O03", "opus:O04"]) if c else c,
        "assessment": assess("sol", p, [
            "Opus: Dataset B Acc@1 direction reversed in text (opus:O01); prose ablation values absent from Table II "
            "(opus:O02, opus:O03, opus:O04).",
            "Opus: whether memory/TTA run on the evaluated incidents is unstated (opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Both seats 2; re-checked. Symptom amplification and topology drift are real, and "
                   "TAMO/Nezha/Eadro/HolisticRCA are compared. But symptom amplification is never quantified, drift "
                   "has no experiment, and the residual over TAMO's multimodal-alignment-plus-tools design is not "
                   "bounded.",
                   ["sol:E001", "sol:E013", "son55:E001", "son55:E002"]),
            "M": R("resolved", 2, "Both seats 2; re-checked. The HET temporal/path/template checks give a concrete "
                   "reason why upstream causes should be preferred over downstream victims. How the memory affects "
                   "diagnosis is unstated (opus:O07), and topology consistency is not causal identification (§V).",
                   ["sol:E005", "sol:E006", "son55:E008", "son55:E009"], ["opus:O07", "sol:E012"]),
            "X": R("resolved", 1, "Opus sides with son55. The static pipeline is partly specified (two-layer GAT, 8 "
                   "heads, K=128, GPT-4o). But for the retained/self-evolving part, the key operations are missing: "
                   "the memory read interface (opus:O07), the write gate ('solved incidents'), the per-level refresh "
                   "rates, τ/γ of Eq. 19, the TTA confidence criteria and buffer size, and the candidate top-K and "
                   "H-hop values. There is no versioning or rollback. Of the retention mechanics, only expiry "
                   "(stochastic forgetting) is given. Below anchor 2's 'main steps described, retention unclear'.",
                   ["son55:E003", "son55:E005", "son55:E006", "sol:E003"], ["opus:O07", "son55:E022"]),
            "E.measurement": R("resolved", 1, "Opus sides with sol. Acc@k and F1 are standard, and Dataset A has "
                               "injected ground truth. But the paper's reported numbers are unreliable in several "
                               "places. The B Acc@1 direction is reversed in the text (opus:O01). Four ablation values "
                               "and a 'full 71.90' in the prose are absent from Table II (opus:O02, opus:O03). Two "
                               "magnitude claims fail (opus:O04). MRR, latency and faithfulness are defined but never "
                               "reported (opus:O06). Incident counts are not given, and the ground-truth source for "
                               "Dataset B is not described. This goes beyond the 'one contradiction → 2' convention.",
                               ["sol:E008", "sol:E009", "son55:E019", "son55:E021"],
                               ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O06"]),
            "E.causality": R("resolved", 1, "Opus sides with sol. The MOMA/VQ/HET removals are relevant component "
                             "evidence for the static pipeline, which keeps this above 0. But the claimed "
                             "self-evolving / drift-robustness contribution has no isolable causal test: w/o SEM "
                             "removes the non-weight memory and the weight-side TTA together (sol:E004), and both may "
                             "run on the evaluated incidents (opus:O05). There is also no same-LLM topology-off "
                             "control. Number inconsistencies are scored once, in E.measurement (A2).",
                             ["sol:E007", "son55:E014", "son55:E020"], ["sol:E004", "opus:O05"]),
            "E.holdout": R("not_reported", 0, "Both seats not_reported; confirmed. There is no train/validation/test "
                           "split, incident count, temporal ordering or memory/TTA-vs-test isolation, and no drift/OOD "
                           "split.",
                           ["son55:E022"], [], ["Full v1 text §I–VI incl. Tables I–II and Figures 1–7 text; no "
                                                "appendix exists. §IV-A/B setup and §III-E protocol checked."]),
            "E.statistics": R("not_reported", 0, "Both seats not_reported; confirmed. No seeds, variance, intervals, "
                              "tests or sample sizes.", ["son55:E022"], [],
                              ["Tables I–II, §IV-C–F prose; full v1 text searched."]),
            "E.cost": R("not_reported", 0, "Both seats not_reported; confirmed. Latency is announced but not reported "
                        "(opus:O06), and there are no LLM-call, token, memory-maintenance or TTA costs. The hardware "
                        "description is a setting, not a cost.", ["opus:O06", "sol:E010"], [],
                        ["§IV-A3 metrics, §IV-B implementation, §IV-C–G results, §V; full v1 text searched."]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (§I–VI; the paper has no appendix). In scope as a boundary case "
                  "(both seats): the hierarchical incident memory is a persistent non-weight component read at "
                  "deployment, alongside a weight-side TTA branch that is not credited. All eight items resolved; "
                  "low scores reflect the paper's own missing protocol and inconsistent numbers, not missing "
                  "material.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree). The TTA branch updates encoder weights and is treated as a "
              "confound, not as harness evidence.",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 5–6 (vocabulary quality, K sensitivity) are image-only; only the text "
                             "statements are used, and the no-numbers result is not credited.",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "structural_prior_encoding",
                "See rs_pattern.reason.", ["sol:E005", "sol:E006"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "revised",
                [["structural_prior_encoding", "C13"], ["decompose_and_delegate", "C25"]],
                "sol's C13 primary + son55's C25 as supporting; son55's C08 is not kept.",
                ["sol:E005", "son55:E008", "son55:E009"], NOSCORE),
            XC(p, "local:2605.15611-2", "son55", "unmet (merged into local:2605.15611-1)",
               "A4: son55's local-2 is sol's local-1 (text–table consistency). Verified unmet (opus:O01–O04).",
               ["opus:O01", "opus:O02", "son55:E016", "son55:E021"]),
            XC(p, "rs:decompose_and_delegate/RE-1", "son55", "unmet",
               "son55-only (card retained as supporting). Verified: latency is defined but not reported, and there "
               "are no call/cost figures.", ["opus:O06", "son55:E012"]),
            XC(p, "rs:decompose_and_delegate/RE-2", "son55", "partial",
               "son55-only. Verified: per-module ablations exist, SEM bundles two mechanisms, and there is no "
               "same-LLM no-topology control.", ["son55:E014", "son55:E015"]),
            XC(p, "rs:decompose_and_delegate/RE-4", "son55", "partial",
               "son55-only. Verified: two datasets (one injected, one production), with no split or sizes.",
               ["son55:E010", "son55:E011"]),
            XC(p, "rs:structural_prior_encoding/RE-1", "sol", "unmet",
               "sol-only. Verified: topology consistency is not causal identification; the authors defer "
               "intervention checks (§V).", ["sol:E006", "sol:E012"]),
            XC(p, "rs:structural_prior_encoding/RE-3", "sol", "partial",
               "sol-only. Verified: module removals exist, but no control holds the agents and tokens while removing "
               "only the wiring.", ["sol:E007", "sol:E005"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "son55", "unknown",
               "son55-only. Kept as unknown, not converted to 'met' or 'unmet'. The full text does not say whether "
               "memory/TTA are written from the evaluated incidents, but the design runs TTA 'during deployment' "
               "(opus:O05), so the risk is live.", ["opus:O05", "son55:E022"]),
            XC(p, "rsi:index_experience_for_reuse/H04", "sol", "partial",
               "sol-only. Verified: per-level refresh and forgetting exist in form, with rates and thresholds "
               "unspecified.", ["sol:E003"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "son55", "unmet",
               "son55-only (sol checked S2 inside its domain match as partial). Opus = son55: records are admitted as "
               "'solved incidents' by the system's own judge. No external outcome gate is operationalised.",
               ["son55:E003", "son55:E006", "opus:O07"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "See the expectation reason: a bundled removal is partial, not unmet.", ["son55:E015", "sol:E004"]),
            XC(p, "rsi:index_experience_for_reuse/S6", "son55", "partial",
               "son55-only. Verified: hierarchical update rates are named but not quantified, and no maintenance cost "
               "is given.", ["son55:E004"]),
            RC(p, "X", "son55", rr(1), "See ratings.X.", ["son55:E003", "opus:O07"], "−5 vs sol"),
            RC(p, "E.measurement", "sol", rr(1), "See ratings.E.measurement.",
               ["opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O06"], "−2.5 vs son55"),
            RC(p, "E.causality", "sol", rr(1), "See ratings.E.causality.", ["sol:E004", "opus:O05"], "−3.75 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A static RCA pipeline with a thin "
                                                   "self-evolving module whose read path is undefined. There is no "
                                                   "split, variance or cost, and many prose/table contradictions. "
                                                   "Expected a low score driven by E.",
            "integrity_checks": "Both seats a1 on 2605.15611v1, material sha 5660f7a3…; canonical seat hashes equal "
                                "conflicts.json. son55's numeric table evidence has null quotes (allowed).",
            "core_claim_check": "Tables I–II recomputed against every prose number in §IV-C/D.",
            "shared_error_review": "No shared error found: both seats' G/M 2 and E.holdout/E.statistics/E.cost "
                                   "not_reported are confirmed.",
            "rating_agreement": "X → son55 1, E.measurement → sol 1, E.causality → sol 1. Final 28.75, below both "
                                "seats; each item decided separately, not by taking the minimum.",
        },
    }

    # =========================================================== 2605.15701 H-Mem (Δ12.5)
    p = "2605.15701"
    S[p] = {
        "base": "sol",
        "opus_evidence": [
            opus_ev(p, "O01", "The fixed Mixed policy also achieves comparable QA performance, with an accuracy of "
                              "92.21 % 92.21\\% .", "Appendix A.4 Memory scope distribution",
                    "The agentic scope planner does not improve accuracy (92.01 vs 92.21 for fixed Mixed); its "
                    "contribution is the 1.8× retrieval-token saving."),
            opus_ev(p, "O02", "Notably, the embedding-only setting also performs well. This is because H-Mem retrieves "
                              "over clean and atomic memory events rather than raw conversational chunks.",
                    "Appendix A.4 Effect of retrieval model components",
                    "The authors themselves credit atomic-event extraction, not the hybrid structure, for retrieval "
                    "quality. A flat store of the same atomic events is the untested alternative explanation.",
                    kind="author_report"),
            opus_ev(p, "O03", "Therefore, we use the setting that balances F1 and LLM-Judge Accuracy as the default "
                              "configuration in the main experiments.", "Appendix A.4 Effect of top-k",
                    "The default top-k is chosen from a sweep on LoCoMo, the same benchmark that carries the headline "
                    "table and every ablation. Table 2 also shows an extra 'H-Mem (k=30)' row."),
            opus_ev(p, "O04", "To reduce accidental variation introduced by the planning stage, we reuse the same planner "
                              "outputs across the three runs", "Appendix A.5",
                    "The repeats measure the evaluation pipeline only, not index construction or planning variance."),
            opus_ev(p, "O05", "Overall, H-Mem consistently outperforms the baselines, with the largest gains appearing "
                              "on multi-hop and temporal questions.", "§4.2",
                    "Contradicted by the Accuracy cells: LoCoMo GPT-4o-mini Temporal 80.06 vs EverMemOS 82.87; "
                    "GPT-4.1-mini Multi-hop 89.01 vs 90.43; REALTALK Temporal 74.29 vs 80.56 (Tables 2, 4)."),
            opus_ev(p, "O06", "Figures 2 (b)–(c) show that H-Mem has relatively high indexing token cost and index "
                              "storage.", "§4.2 efficiency",
                    "The cost text gives ordinal positions only (absolute values are in the Figure 2 image, not "
                    "read). H-Mem costs more than most baselines on indexing tokens and storage."),
            opus_ev(p, "O07", "In terms of retrieval token cost, Figure 2 (e) shows that H-Mem is higher than most "
                              "baselines but lower than Zep.", "§4.2 efficiency",
                    "Online token cost is also above most baselines. Accuracy margins over EverMemOS (e.g. 92.01 vs "
                    "90.78) are not shown at a matched token budget."),
            opus_ev(p, "O08", "which marks a prediction as correct only if an LLM judge determines that it is "
                              "semantically consistent with the gold answer", "§4.1 Metrics",
                    "The judge model's identity is not stated anywhere (son55's finding); the prompt follows MemGPT."),
        ],
        "rs_pattern": {
            "primary": "heterogeneous_decomposition", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Opus sides with sol. The paper's thesis is the card's move: one memory resource has two "
                      "systematically different needs (temporal-semantic abstraction vs entity-relational "
                      "connectivity), and a single uniform index cannot serve both, so each gets its own structure "
                      "(tree vs graph), bridged by provenance. Both halves are removed in the ablation (w/o tree, w/o "
                      "graph). C04 (non-uniform compression of a high-impact minority) is not the tactic, so sub null. "
                      "adapt_via_conditioning is kept as supporting (retrieved evidence conditions a frozen LLM), sub "
                      "null. son55's C03 is rejected: there is no upstream parsing phase and no category holdout "
                      "(r17b convention), and son55 itself rated the fit 'weak'. Unlike DrugSAGE, where the R/H/Q "
                      "split is an incidental schema, here the split is the claimed contribution and is ablated.",
            "matches": [smatch("sol", p, "heterogeneous_decomposition", role="primary"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi", "matches": [dmatch("sol", p, "index_experience_for_reuse", "H04")],
                           "unassigned": ["B-class memory substrate; no execution-feedback optimiser loop"],
                           "reason": "H04 (both seats). son55's H01 (fit low) is not kept: consolidation summarises "
                                     "but there is no update/delete/no-op curation policy and no outcome signal.",
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2605.15701-1"): "local:2605.15701-3"},
            overrides={
                "local:2605.15701-3": renum("son55:local:2605.15701-1"),
                "rsi:abstract_experience_into_guidance/S3": dropped_card("abstract_experience_into_guidance"),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O02", "opus:O03", "opus:O05"]), "C2",
                                        ["opus:O06", "opus:O07"]),
        "assessment": assess("sol", p, [
            "Opus: the authors attribute retrieval quality to atomic event extraction (opus:O02); no flat-atomic-store "
            "baseline.",
            "Opus: top-k chosen on LoCoMo test (opus:O03); 'largest gains on temporal' contradicted by Accuracy cells "
            "(opus:O05)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The non-weight object (the memory index) is clear and the "
                   "nearest neighbours are compared under one configuration. But the gap is a combination gap "
                   "defined by the paper's own Table 1, which narrows 'Memory Evolution' to temporal-window "
                   "consolidation so that hierarchical MemTree/MemOS/MemoryOS score 'No' and Zep's temporal graph "
                   "does not count (sol:E020, son55:E022). No failure analysis shows that current systems fail "
                   "because one index lacks the other property. A-Mem is named but not compared.",
                   ["son55:E001", "son55:E002", "son55:E022", "sol:E020"]),
            "M": R("resolved", 3, "Opus sides with sol. The operations map onto both stated halves of the gap: windowed "
                   "consolidation for evolution, the entity graph with multi-hop expansion for relations, and "
                   "graph → fragment → bottom-up tree bridging. The prediction (both are needed) is checkable and is "
                   "tested by w/o tree / w/o graph. son55's main reason, that there is no execution-feedback loop, "
                   "judges this B-class component against the A-class loop; SCORE_SPEC says A/B is an inclusion type, "
                   "not a quality grade. Not 4: the Ebbinghaus robustness prior is heuristic, and no distinguishing "
                   "prediction is made against a flat atomic-event store (opus:O02).",
                   ["sol:E002", "sol:E003", "sol:E004", "son55:E003"], ["opus:O02", "sol:E005"]),
            "X": R("resolved", 3, "Opus sides with sol. The static construction/retrieval flow (SCORE_SPEC anchor 4: "
                   "'或相应静态流程可重建') is reconstructable to the hyperparameter level: four day/week/month/year "
                   "windows, consolidation thresholds 0.8/0.7/0.6, ranking weights 0.70/0.15/0.15, τ=365 d, η=0.5, "
                   "entity-resolution and graph-repair rules, a level-activation rule by memory age, and the full "
                   "prompts. Missing: an admission gate on extracted events and summaries, deletion and versioning "
                   "of outdated facts (only ranking decay), and rollback, so not 4. This differs from DrugSAGE "
                   "(X=2), whose own search and transfer constants are undisclosed.",
                   ["sol:E002", "sol:E003", "sol:E004", "sol:E015", "sol:E017"], ["son55:E013"]),
            "E.measurement": R("resolved", 2, "Both seats 2; re-checked. F1 with answer simplification is specified, "
                               "and the same judge prompt is applied to all methods. The judge model is unnamed "
                               "(opus:O08), there is no human calibration, two of three benchmarks are LLM-simulated, "
                               "and the baselines were re-run by the authors. The text also contradicts the table on "
                               "where the gains are largest (opus:O05).",
                               ["sol:E006", "son55:E007", "son55:E008"], ["opus:O05", "opus:O08"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Six component removals and the fixed-Mixed and "
                             "retriever-size controls are relevant. Missing: a flat store of the same atomic events "
                             "or a full-context baseline, which is the authors' own suggested explanation (opus:O02). "
                             "The ablations are single-run and on one benchmark/backbone.",
                             ["sol:E010", "son55:E019", "opus:O01"], ["opus:O02", "son55:E021"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. Top-k (opus:O03) and threshold schedules are "
                           "compared on the reported benchmarks, and LoCoMo carries both the selection and the "
                           "headline and ablation results. Whether LongMemEval/REALTALK were used for any selection "
                           "is unstated. There is no online future-stream test.",
                           ["sol:E014", "son55:E015", "son55:E016", "opus:O03"]),
            "E.statistics": R("resolved", 2, "Both seats 2 (A2 tier 2): the question denominators are given, and "
                              "three repeats report mean ± std. But the repeats reuse planner outputs at temperature 0 "
                              "(opus:O04), so only pipeline noise is measured. No significance test or paired "
                              "interval, and conversation-level clustering (10 conversations) is ignored.",
                              ["sol:E013", "sol:E018", "sol:E019", "opus:O04"]),
            "E.cost": R("resolved", 2, "Opus sides with sol. Five cost dimensions (indexing time, indexing tokens, "
                        "storage, retrieval latency, retrieval tokens) are measured against all baselines, and the "
                        "fixed-Mixed 1.8× token result is stated. But the text gives only ordinal positions "
                        "(opus:O06, opus:O07); the values are in the Figure 2 image and were not read. The "
                        "measurement covers LoCoMo only. H-Mem spends more indexing and retrieval tokens than most "
                        "baselines, and its accuracy margins are not shown at a matched budget. son55's 3 credits "
                        "honest disclosure, which does not substitute for budget fairness.",
                        ["sol:E011", "sol:E012", "opus:O06", "opus:O07"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 HTML text read (body, Tables 1–10, Appendices A–C). In scope as a B-class "
                  "memory substrate (both seats): a persistent non-weight memory structure directly usable by "
                  "agents. No execution-feedback optimiser loop is claimed or inferred. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope as B-class memory component; both seats agree).",
        "improver_check": "not claimed.",
        "figure_dependence": "Figures 2 (costs), 3 (top-k) and 4 (scope distribution) are image-only. Only text "
                             "statements (ordinal cost positions, 92.21 vs 92.01, 1.8×) are used. sol's page-image "
                             "request is non-blocking (see batch notes).",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "heterogeneous_decomposition",
                "See rs_pattern.reason.", ["sol:E001", "sol:E010"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", None], ["heterogeneous_decomposition", None]],
                "Both null subs; son55's C03 is rejected (weak by its own account; r17b convention).",
                ["sol:E001", "sol:E004", "son55:E004"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["index_experience_for_reuse", "H04"]],
                "H04 agreed; son55's low-fit H01 is not kept (no curation edit policy or outcome signal).",
                ["sol:E002", "son55:E003"], NOSCORE),
            XC(p, "local:2605.15701-1", "revised", "met (sol's question); son55's question kept as local:2605.15701-3 "
                                                   "(unmet)",
               "A4 hidden collision. sol's local-1 asks whether scope prediction is credited only for efficiency: met "
               "(opus:O01). son55's local-1 asks for an independent dev set: unmet (opus:O03). Both are kept, under "
               "different IDs.", ["opus:O01", "opus:O03", "sol:E012", "son55:E016"]),
            XC(p, "local:2605.15701-2", "son55", "unmet",
               "son55-only. Verified: 'largest gains on temporal questions' is contradicted by Temporal Accuracy on "
               "LoCoMo/GPT-4o-mini and REALTALK (opus:O05).", ["opus:O05", "son55:E009"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "unmet",
               "son55-only (card kept as supporting). Verified: no full-context or naive-RAG baseline.",
               ["son55:E021"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "partial",
               "son55-only. Verified: retriever-size and top-k sensitivity exist; extraction quality is never related "
               "to outcomes.", ["son55:E013", "son55:E016"]),
            XC(p, "rs:heterogeneous_decomposition/RE-3", "sol", "partial",
               "sol-only. Verified: tree/graph/summary removals exist; there is no same-content uniform store.",
               ["sol:E010", "opus:O02"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "not_applicable",
               "Kept as a check question (card not retained). The content is a conversation stream, not "
               "execution-outcome reflection.", ["son55:E001"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "sol", "partial",
               "sol-only. Building the store from the conversation is the task's design (gold answers are never "
               "written). The unstated tuning/test separation is the partial part.", ["sol:E014", "sol:E016"]),
            XC(p, "rsi:index_experience_for_reuse/F4", "son55", "partial",
               "son55-only. Verified: LLM-generated events/summaries keep provenance but have no admission gate.",
               ["son55:E013", "sol:E015"]),
            XC(p, "rsi:index_experience_for_reuse/H04", "sol", "partial",
               "sol-only. Verified: local incremental maintenance; no scaling or maintenance study against flat "
               "retrieval.", ["sol:E002", "sol:E011"]),
            XC(p, "rsi:index_experience_for_reuse/S2", "sol", "partial",
               "sol-only. Verified: provenance and prompt constraints exist, without an external gate.",
               ["sol:E015", "sol:E017"]),
            XC(p, "rsi:index_experience_for_reuse/S4", "son55", "met",
               "son55-only. Verified: scope selection, top-k, dedup/rerank, and follow-up only on missing slots.",
               ["son55:E004", "son55:E017"]),
            XC(p, "rsi:index_experience_for_reuse/S5", "son55", "partial",
               "son55-only. Verified: structural removals exist; there is no no-memory or flat-store arm.",
               ["son55:E019", "son55:E021"]),
            XC(p, "rsi:index_experience_for_reuse/S6", "son55", "partial",
               "son55-only. Verified: incremental insertion, with indexing tokens and storage above most baselines "
               "(opus:O06).", ["son55:E003", "opus:O06"]),
            RC(p, "G", "son55", rr(2), "See ratings.G.", ["son55:E022", "sol:E020"], "−3.75 vs sol"),
            RC(p, "M", "sol", rr(3), "See ratings.M.", ["sol:E002", "sol:E004"], "+5 vs son55"),
            RC(p, "X", "sol", rr(3), "See ratings.X.", ["sol:E002", "sol:E015"], "+5 vs son55"),
            RC(p, "E.cost", "sol", rr(2), "See ratings.E.cost.", ["opus:O06", "opus:O07"], "−1.25 vs son55"),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text first. A carefully specified B-class memory "
                                                   "substrate with real ablations. The gap is self-defined, the "
                                                   "planner wins on efficiency only, and holdout is weak (top-k on "
                                                   "the test benchmark). Expected high-50s.",
            "integrity_checks": "Both seats a1 on 2605.15701v1, material sha e15eab30…; canonical seat hashes equal "
                                "conflicts.json. son55's numeric table evidence has null quotes (allowed).",
            "core_claim_check": "Tables 2–5, 8–10 and Appendix A.2/A.4/A.5 re-read; every category cell compared "
                                "against the 'largest gains' sentence.",
            "shared_error_review": "No shared error found: E.measurement 2, E.causality 2, E.holdout 1 and "
                                   "E.statistics 2 are confirmed.",
            "rating_agreement": "G → son55, M/X/E.cost → sol. Final 57.5 (seats 61.25 / 48.75).",
        },
    }
    return S
