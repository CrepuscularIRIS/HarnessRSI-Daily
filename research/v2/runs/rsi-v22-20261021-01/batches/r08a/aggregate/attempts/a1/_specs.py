"""Opus rulings for r08a a1 (data only; consumed by _build.py)."""
import copy


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix = g["seat"], g["prefix"]
    S = {}
    NOSCORE = "none (patterns never score)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def X(p, eid, s_val, n_val, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", s_val, n_val, dec, final, reason, ev,
                   "none (expectations are not scored directly)")

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
        hit = False
        for c in claims:
            if c["claim_id"] == cid:
                ce = c.get("counterevidence")
                c["counterevidence"] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
                hit = True
        assert hit, cid
        return claims

    def keep(s, p, k, note):
        r = copy.deepcopy(seat(s, p)["ratings"][k])
        r = prefix(r, s)
        r["reason"] = note + " " + r["reason"]
        return r

    # =========================================================== 2510.11290 AAS (Δ11.25)
    p = "2510.11290"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "serving as the ground truth for evaluation and iteration", "§4.1 Datasets",
                    "The same expert-edited stream both drives the simulation ('iteration') and is the scoring reference."),
            opus_ev(p, "O02", "Subsequently, the Gemini-2.5-Pro model generated an initial 5-day sequence of agent actions "
                    "and interactions", "§4.1 Datasets",
                    "The reference is LLM-generated then expert-edited, not observed school behaviour (only classroom "
                    "teaching actions come from real classrooms)."),
            opus_ev(p, "O03", "reflecting fluency and content overlap", "§4.2 automated evaluation",
                    "The authors themselves describe ROUGE-L as lexical overlap/fluency, not behavioural fidelity."),
            opus_ev(p, "O04", "the experts were asked to vote for the answer they believed best reflected a realistic "
                    "response in the given educational context", "§4.2 human evaluation",
                    "Forced single-choice vote among four answers; the vote-aggregation rule across nine experts and "
                    "inter-rater agreement are not reported."),
            opus_ev(p, "O05", "However, some scholars have pointed out the limitations of current agents in the education "
                    "field", "§1 Introduction", "The motivating limitation is asserted without a citation."),
            opus_ev(p, "O06", "Comprises the entirety of the respective Experience Base or Knowledge Base.",
                    "§3.1.3 Long-term Memory", "Long-term memory is unbounded: no capacity, forgetting or consolidation rule."),
            opus_ev(p, "O07", "Based on the agent’s autonomous selection, selected new memories are also added to the "
                    "agent’s Short-term Memory", "§3.2 Memory Update",
                    "Short-term admission is the model's own choice; no external write gate."),
            opus_ev(p, "O08", "9 0.10 0.17 0.22 0.25 0.26 0.25 0.25 0.24 0.26 0.24", "Table 2 (GPT-4o), ID 9, 5%–50%",
                    "Context-only (no external memory) also rises 0.10→0.25 over the stream, so part of the rise is "
                    "accumulating stream context, not memory evolution."),
            opus_ev(p, "O09", "2 0.08 0.16 0.18 0.23 0.28 0.31 0.35 0.36 0.36 0.38", "Table 4 (Qwen3-8B), ID 2, 5%–50%",
                    "Unified memory (ID 2) is ≥ full model (ID 1: 0.07 0.14 0.17 0.2 0.29 0.28 …) for most of the first "
                    "30% of the stream."),
            opus_ev(p, "O10", "ID 1 consistently outperforms ID 2", "§5.1",
                    "The 'consistently' claim is contradicted early in the stream (opus:O09)."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": ["heterogeneous_decomposition"], "outside_taxonomy": False,
            "reason": "Final = sol's identification with fit lowered. Retrieved memories condition a frozen LLM (C03 "
                      "skip-upstream branch: retrieved reference instances as a first-class prompt input; run convention "
                      "for retrieval memories, e.g. r07a ArcMemo). The load-bearing design claim of the paper is the "
                      "partition of the store (experience vs knowledge, short- vs long-term with priority retrieval), "
                      "which the Table 1 grid ablates — heterogeneous_decomposition as supporting, sub null (C04 is "
                      "lossy compression).",
            "matches": [
                smatch("sol", p, "adapt_via_conditioning", fit="partial (C03 retrieval branch only; no category holdout, "
                                                               "no leakage audit)"),
                smatch("sol", p, "heterogeneous_decomposition", fit="low (partition ablated, heterogeneity never "
                                                                    "characterized; both bases get the same cosine retrieval)"),
            ],
            "executes_pattern": "partial", "resolves_problem": False,
        },
        "domain_pattern": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]), "sol"),
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol"),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "local:2510.11290-1": {
                    "status": "unmet", "score_item": "E.holdout",
                    "applies_when": "fidelity/evolution claimed from one curated 5-day stream",
                    "reason": "Opus final (sol local-1 and son55 local-1 ask the same question: does the fidelity claim hold "
                              "beyond the single curated stream?). No independent school, scenario, role population or "
                              "external fidelity benchmark; the same reference stream drives iteration and scoring "
                              "(opus:O01) and is LLM-generated (opus:O02).",
                    "evidence_ids": ["sol:E007", "sol:E013", "son55:E009", "son55:E016", "opus:O01", "opus:O02"]},
                "local:2510.11290-2": {
                    "status": "unmet",
                    "reason": "Opus final: the paper says 'significantly outperforms' with one run per configuration, no "
                              "seeds, CI, significance test, vote-aggregation rule or inter-rater agreement (opus:O04). "
                              "Denominators (50 QA × 10 checkpoints) are given, but that does not back a significance claim.",
                    "evidence_ids": ["sol:E010", "sol:E012", "son55:E010", "opus:O04"]},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O08", "opus:O09", "opus:O10"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats 'task', re-checked. Memory written at step t is read later and a context-only "
                                   "control exists, but the scoring reference is also the stream that drives the simulation "
                                   "(opus:O01): the later-stream gain cannot be separated from storing reference-stream "
                                   "content, and context-only itself rises (opus:O08). No frozen-memory or held-out test.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + seat("son55", p)["assessment"]["unresolved"],
        },
        "ratings": {
            "G": R("resolved", 1, "Opus sides with son55. The motivating limitation is asserted without a source "
                   "(opus:O05) and the closest neighbours (Generative Agents memory stream + reflection, Agent Hospital "
                   "experience base) are adopted as the template (sol:E002) rather than contrasted: no residual is stated for "
                   "what a dual/tiered store adds over their memory and reflection mechanisms. A domain application gap, "
                   "not a located fixed-component gap; above 0 because the target (role-consistent multi-agent school "
                   "simulation) is concrete.",
                   ["opus:O05", "sol:E001", "sol:E002", "son55:E002", "son55:E003"]),
            "M": keep("sol", p, "M", "Both seats 2; re-checked."),
            "X": R("resolved", 2, "Opus sides with sol. Write/read path is reconstructable from §3.2 and the Appendix B/C "
                   "prompts (retrieve ST then LT, write LT experience/knowledge, agent-selected ST, role-setting rewrite). "
                   "Missing: external write gate (opus:O07), capacity/forgetting (LT is 'the entirety', opus:O06), conflict "
                   "handling, versioning/rollback, and which agent actions (generated or reference) enter memory. That is "
                   "the anchor-2 description 'main steps described, retention/recovery or key conditions unclear'; nothing "
                   "is contradictory or missing at the operation level, so not 1. The information-permission gap is "
                   "scored once, under E.holdout (A2).",
                   ["sol:E004", "sol:E006", "sol:E014", "son55:E005", "son55:E006", "opus:O06", "opus:O07"]),
            "E.measurement": R("resolved", 1, "Opus sides with son55. The central claim is fidelity to real educational "
                               "dynamics, but both instruments are anchored to an LLM-generated, expert-edited stream "
                               "(opus:O02). The automated metric is lexical overlap by the authors' own description "
                               "(opus:O03), which a memory that stores reference-stream text can raise without behavioural "
                               "fidelity. The blind expert vote is the stronger instrument but is forced-choice, GPT-4o "
                               "only, three of nine configurations, and reports no aggregation rule or agreement (opus:O04). "
                               "Above 0 because the blinded expert design measures perceived realism directly.",
                               ["sol:E009", "sol:E010", "son55:E009", "son55:E010", "opus:O02", "opus:O03", "opus:O04"],
                               ["sol:E007"]),
            "E.causality": keep("sol", p, "E.causality", "Both seats 2; re-checked (9-config grid × 3 backbones incl. "
                                "store-off; role-setting update not ablated; ID1>ID2 not consistent early, opus:O09; "
                                "context-only also rises, opus:O08)."),
            "E.holdout": keep("son55", p, "E.holdout", "Both seats 1; re-checked (same stream for iteration and scoring, "
                              "opus:O01)."),
            "E.statistics": keep("sol", p, "E.statistics", "Both seats 1; re-checked (A2 ladder: denominators, no "
                                 "uncertainty)."),
            "E.cost": keep("sol", p, "E.cost", "Both seats not_reported; re-checked."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text incl. Appendices A–D read; in scope (system_method): a non-weight memory written "
                  "during the simulation and read on later steps. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("ratings.G", *C(p, "ratings.G"), "son55", {"status": "resolved", "rating": 1},
                "Uncited motivating limitation (opus:O05); nearest neighbours adopted, not contrasted (sol:E002). sol's own "
                "reason ('neighbours only narrated; residual not checked') describes the anchor-1 situation.",
                ["opus:O05", "sol:E002", "son55:E003"], "-3.75 vs sol (15×1/4)"),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "Main write/read steps reconstructable with prompts; missing gate/forgetting/rollback = anchor-2 wording. "
                "son55's ground-truth-in-loop point is real but belongs to E.holdout (A2: one defect, one item).",
                ["sol:E006", "sol:E014", "opus:O06", "opus:O07"], "+5.0 vs son55 (20×1/4)"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "son55", {"status": "resolved", "rating": 1},
                "Synthetic reference + lexical metric + under-reported forced-choice vote for a real-world fidelity claim.",
                ["opus:O02", "opus:O03", "opus:O04"], "-2.5 vs sol (10×1/4)"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", "C03"], ["heterogeneous_decomposition", None]],
                "C03's skip-upstream branch (retrieved reference instances as prompt input) is executed, matching the run "
                "convention for retrieval memories (r07a ArcMemo, partial fit). The store partition is the paper's "
                "ablated design claim, so heterogeneous_decomposition is a fair supporting card (low fit).",
                ["sol:E003", "sol:E004", "sol:E008"], NOSCORE),
            X(p, "local:2510.11290-1", *C(p, "expectations[local:2510.11290-1].status"), "son55", "unmet",
              "Same question in both seats (does fidelity hold beyond the one curated stream). Nothing outside the stream "
              "is tested and the stream drives iteration (opus:O01); 'partial' credited same-stream fit, which is not what "
              "the expectation asks.", ["opus:O01", "opus:O02", "son55:E016"]),
            X(p, "local:2510.11290-2", *C(p, "expectations[local:2510.11290-2].status"), "revised", "unmet",
              "Both seats ask whether the 'significant' claims are statistically backed. Full text read, so 'unknown' "
              "(son55) is not the right state; denominators alone (sol 'partial') do not back a significance claim.",
              ["sol:E012", "son55:E010", "opus:O04"]),
            X(p, "local:2510.11290-3", *C(p, "expectations[local:2510.11290-3].status"), "sol", "unmet",
              "Verified: no call/token/time/memory-growth cost anywhere; son55 recorded the same fact as E.cost "
              "not_reported.", ["sol:E008"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "son55",
              "partial", "Verified: ID 9 isolates external memory; no alternative conditioning at matched budget.",
              ["son55:E012"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55",
              "unmet", "Verified: no audit of whether reference-stream content enters memory; applies because fidelity "
                       "to later behaviour is claimed (opus:O01).", ["son55:E008", "opus:O01"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "partial", "Verified: unified/LT-only/context-only variants; no reflection-memory or literature baseline.",
              ["son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-4", *C(p, "expectations[rs:adapt_via_conditioning/RE-4].status"), "son55",
              "partial", "Verified: memory modules ablated; the role-setting rewrite (App. C) is never ablated.",
              ["son55:E007", "son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55",
              "unmet", "Verified: one simulated school, one 5-day stream; authors list scale as a limitation.",
              ["son55:E015"]),
            X(p, "rsi:abstract_experience_into_guidance/S4",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S4].status"), "sol", "partial",
              "App. B asks the agent to update/correct/reinforce existing LT entries (localized edits exist), but there is "
              "no consolidation, forgetting or bound (opus:O06). son55 recorded S4 'unmet' only as an H01 condition "
              "check; the update instruction makes 'partial' the supported state.", ["sol:E006", "opus:O06"]),
            X(p, "rsi:index_experience_for_reuse/F3", *C(p, "expectations[rsi:index_experience_for_reuse/F3].status"),
              "son55", "unmet", "Verified: the store is built on the evaluated stream (opus:O01); sol recorded the same "
                                "fact under local-1.", ["son55:E014", "opus:O01"]),
            X(p, "rsi:index_experience_for_reuse/F4", *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"),
              "same_supported_fact", "unmet", "Same fact as S2 (sol): model outputs enter memory on the agent's own "
                                              "selection (opus:O07).", ["son55:E006", "opus:O07"]),
            X(p, "rsi:index_experience_for_reuse/S2", *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"),
              "same_supported_fact", "unmet", "Same fact as F4 (son55), which also lists 'S2 unmet' in its H04 condition "
                                              "checks.", ["sol:E005", "sol:E006", "opus:O07"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–8 and App. A–D before opening seats: dual memory + ST/LT is a "
                                                   "Generative-Agents-style store applied to a school simulation; the scoring "
                                                   "reference is also the stream that drives iteration; ROUGE-L vs an "
                                                   "LLM-generated reference; context-only also rises; single run. Expected "
                                                   "low G and measurement, E.holdout 1, cost not reported.",
            "integrity_checks": "Both seats a1 on 2510.11290v1, material sha c32ddaf4…; canonical seat hashes equal "
                                "conflicts.json; both completed RS + domain identification.",
            "core_claim_check": "Central claim scoped to in-stream ROUGE-L/expert-preference gains; 'consistently' and "
                                "'significantly' claims contradicted or unbacked (opus:O09, O10, O04).",
            "rating_agreement": "M, E.causality, E.holdout, E.statistics, E.cost agree and were re-checked; G/X/E.measurement "
                                "resolved above.",
        },
    }

    # =========================================================== 2510.13220 EvoTest (Δ12.5)
    p = "2510.13220"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "EvoTest (w/ Simple Mutation) 0.65 0.07 0.20", "Table 5",
                    "With the structured Evolver prompt replaced by a generic one (other channels kept), whole-system "
                    "EvoTest equals EvoPrompt on Detective and is below it on Zork1/Balances (opus:O02)."),
            opus_ev(p, "O02", "EvoPrompt 0.65 0.10 0.24", "Table 5", "Prompt-only evolutionary baseline on the same games."),
            opus_ev(p, "O03", "Memory 0.56 ± .02", "Table 8 (Appendix F)",
                    "Memory baseline on Detective is 0.56 here vs 0.25 in Table 1, while the Table 8 average (0.13) matches "
                    "a value near 0.25, i.e. an internal inconsistency in a baseline row."),
            opus_ev(p, "O04", "Memory 0.25 0.26 0.18 0.20", "Table 1", "Memory baseline in the main table."),
            opus_ev(p, "O05", "Generate a new, complete configuration by following the four parts below.",
                    "Appendix H master prompt", "One Evolver call returns one configuration."),
            opus_ev(p, "O06", "whole-system evolution by generating a set of new candidate child configurations", "§4.2",
                    "§4.2 describes m children per step; m is never given (O05 vs O06; Table 2 lists 1 LLM call)."),
            opus_ev(p, "O07", "this insight is not stored in a database to be queried", "Appendix J.2",
                    "Contradicts §4.2 (opus:O08), where failures are recorded in a failure table."),
            opus_ev(p, "O08", "identifies sequences of interactions that led to no progress and records them in a",
                    "§4.2 Memory Update", "Failure table in the method section."),
            opus_ev(p, "O09", "All methods are evaluated under the same step budget and use the same backbone LLMs for "
                    "their respective roles to ensure a fair comparison.", "§5.1 Baselines",
                    "Only environment steps are matched; the optimizer model used by TextGrad/Promptbreeder/EvoPrompt/"
                    "Reflexion is not named."),
            opus_ev(p, "O10", "The Evolver Agent, which performs the most complex reasoning, is powered by "
                    "openai/o3-2025-04-16", "§5.1 Setup",
                    "EvoTest's optimizer is o3; Table 4 shows Evolver strength drives AUC (qwen3-8b Evolver 0.68 vs o3 0.94)."),
            opus_ev(p, "O11", "w/o Memory 0.82 0.11 0.28 w/o Hyperpara. 0.89 0.12 0.30 w/o Tool-Use 0.91 0.13 0.30",
                    "Table 3", "Non-prompt channels contribute 0.01–0.12 AUC in single-run ablations on 3 games; 0.01–0.03 "
                               "deltas are within the ±.02 seed SD of Table 8."),
            opus_ev(p, "O12", "The game environment is reset to its identical initial state after each episode",
                    "Appendix C.1", "Every 'later task' is the identical game instance."),
            opus_ev(p, "O13", "This vision for unified optimization is shared by EvoAgent", "§2 Related Work",
                    "Closest whole-system neighbours named without a stated residual."),
            opus_ev(p, "O14", "are a form of strategic overfitting to the current task instance", "Appendix A",
                    "Authors scope the learned artifact to the instance."),
            opus_ev(p, "O15", "EvoTest (Ours) 0.93 ± .02", "Table 8", "Five-seed SD for EvoTest on Detective."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Final = son55's card. The paper's core move and RQ3 are 'improve without fine-tuning': a frozen "
                      "actor is adapted between episodes purely through conditioning (evolved prompt, memory hints, "
                      "state-extractor output), contrasted with SFT/GRPO. generative_process_redesign (sol) concerns a "
                      "fixed component of an iterative generative procedure (priors, endpoints, latents) and sol itself "
                      "found none of its subs applicable. Sub null: neither C03's upstream-schema branch nor a held-out "
                      "category claim; the reference-retrieval branch exists only in the minor memory channel (opus:O11).",
            "matches": [smatch("son55", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": False,
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "attribute_and_patch_incumbent", "H10"),
                        dmatch("sol", p, "population_search_executable_fitness", None)],
            "unassigned": seat("sol", p)["domain_pattern"]["unassigned"] + [
                "Opus: H00 (son55) not assigned — lessons are written into the incumbent prompt as an instance walkthrough, "
                "not into a separate store retrieved by later different tasks; H12 (son55) only partial — a generated "
                "state-extractor function, but no source inspection, scoped patch with prediction, or regression gate."],
            "revision_proposals": [],
        },
        "pattern_mapping": [
            {"rs_main": "adapt_via_conditioning", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "attribute_and_patch_incumbent", "sub": "H10"},
             "operation_correspondence": "The conditioning document (policy prompt) is the incumbent; the Evolver diagnoses "
                                         "the full transcript and rewrites it (walkthrough + avoid list + exploration plan).",
             "necessary_conditions_and_differences": "H10 expects candidate rewrites to be scored before retention; here "
                                                     "a child is promoted by UCB and scored only by playing it.",
             "evidence_ids": ["sol:E001", "sol:E006", "sol:E015", "opus:O05"]},
            {"rs_main": "adapt_via_conditioning", "rs_sub": None,
             "domain": {"namespace": "rsi", "main": "population_search_executable_fitness", "sub": None},
             "operation_correspondence": "Parent + children pool with UCB selection on native game return.",
             "necessary_conditions_and_differences": "No H13–H16 sub fits: variation is diagnosis-directed (not H13), the "
                                                     "genome is a configuration (not H14), no distilled search memory or "
                                                     "frontier.", "evidence_ids": ["sol:E006", "sol:E007", "opus:O06"]},
        ],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2510.13220-1"): "local:2510.13220-4",
                    ("sol", "local:2510.13220-2"): "local:2510.13220-3",
                    ("sol", "local:2510.13220-3"): "local:2510.13220-2"},
            overrides={
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "partial",
                    "reason": "Opus final: Static and per-channel ablations exist; the prompt channel is clearly isolated "
                              "(0.94→0.52), but memory/tool/hyperparameter ablations are single-run on 3 of 6 games with "
                              "deltas of 0.01–0.12 (opus:O11), partly inside seed noise."},
                "local:2510.13220-3": {"reason": "Opus final (sol local-2 + son55 local-3, same statistics question): "
                                                 "5-seed mean±SD for the main table only; no CI/test; ablations single run; "
                                                 "Table 1 vs Table 8 baseline row inconsistent (opus:O03)."},
                "local:2510.13220-2": {"reason": "Opus final (sol local-3 + son55 local-2, same cost question): per-update "
                                                 "time/call counts and complexity analysis, but no session token/$ for the "
                                                 "o3 Evolver and m unstated."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O01", "opus:O11"]), "C2", ["opus:O10"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Opus sides with sol. Retained configurations are re-read and later-episode scores rise "
                                   "against Static and per-channel ablations, but every later episode is the identical game "
                                   "instance (opus:O12), configurations are selected by UCB on the returns of those same "
                                   "episodes, and the authors call the artifact instance overfitting (opus:O14). Run "
                                   "precedent cal-h1-v2 (Reflexion-style retries of the same task → task) and EVIDENCE rule "
                                   "2: a retained change helping later attempts of the same instance it was selected on is "
                                   "not 'improvement on later tasks'.",
            "claim_support": "scoped",
            "strongest_supported_claim": "Within one session on an identical replayed game, evolving the policy prompt with a "
                                         "structured walkthrough-extracting Evolver (o3) raises AUC well above Static, "
                                         "reflection, memory and prompt-evolution baselines (5 seeds, Gemini actor). That "
                                         "the gain comes from whole-system (multi-channel) evolution rather than the "
                                         "structured Evolver prompt and stronger optimizer is not established (opus:O01, "
                                         "O10, O11).",
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + [
                "Optimizer LLM used by the prompt-optimization baselines (opus:O09).",
                "m children vs one configuration per Evolver call (opus:O05, O06); failure-memory storage (opus:O07, O08)."],
        },
        "ratings": {
            "G": R("resolved", 2, "Opus sides with sol. The single-channel limitation of prompt-only/memory-only adaptation "
                   "is concrete and tested, but the closest whole-system neighbours are named as sharing the vision "
                   "(EvoAgent, MASS; opus:O13) without a stated residual or comparison, and repeated-attempt learning on "
                   "one task is Reflexion's setting, so the J-TTL 'missing testbed' gap is a reframing. Anchor 2: real "
                   "limitation, incomplete nearest-neighbour comparison.",
                   ["sol:E002", "son55:E002", "son55:E003", "opus:O13"]),
            "M": keep("sol", p, "M", "Both seats 3; re-checked."),
            "X": R("resolved", 2, "Opus sides with sol. Config tuple, full master prompt, memory schema and UCB rule are "
                   "given, and the parent stays in the pool. But the candidate-generation step is internally inconsistent "
                   "(m children per step vs one configuration per call, m never given; opus:O05/O06), the UCB value of an "
                   "untried child and β are unspecified, failure memory is a table in §4.2 but 'not stored' in App. J.2 "
                   "(opus:O07/O08), and evolved Python runs with no validation. Promotion happens without a prior test (a "
                   "child is played and its episode counts). Key conditions unclear → anchor 2, not 3.",
                   ["sol:E004", "sol:E006", "sol:E007", "sol:E014", "sol:E017", "son55:E008", "opus:O05", "opus:O06",
                    "opus:O07", "opus:O08"]),
            "E.measurement": keep("son55", p, "E.measurement",
                                  "Both seats 3; re-checked. The Table 1 vs 8 discrepancy (opus:O03/O04) is in a baseline "
                                  "row whose Table 8 average matches Table 1, so it reads as a transcription error rather "
                                  "than a measurement fault in EvoTest's own numbers (0.94 vs 0.93±.02)."),
            "E.causality": R("resolved", 2, "Opus sides with sol. Rich ablations exist, but they leave the central "
                             "attribution ('whole-system beats single-channel') open: (i) with a generic Evolver prompt, "
                             "whole-system EvoTest equals EvoPrompt on Detective and trails it on Zork1/Balances "
                             "(opus:O01/O02), so the gain tracks the engineered walkthrough-extracting prompt; (ii) "
                             "memory/tool/hyperparameter channels add 0.01–0.12 in single-run ablations (opus:O11); (iii) "
                             "EvoTest's optimizer is o3 while the baselines' optimizer model is unstated and only "
                             "environment steps are matched (opus:O09/O10), and Evolver strength moves Detective AUC from "
                             "0.68 to 0.94. Key control missing → 2.",
                             ["sol:E009", "sol:E010", "son55:E010", "son55:E012", "son55:E013", "opus:O01", "opus:O02",
                              "opus:O09", "opus:O10", "opus:O11"], ["sol:E011"]),
            "E.holdout": keep("sol", p, "E.holdout", "Both seats 1; re-checked (identical reset, opus:O12)."),
            "E.statistics": keep("sol", p, "E.statistics", "Both seats 2; re-checked (A2: multi-seed SD, no CI/test)."),
            "E.cost": keep("sol", p, "E.cost", "Both seats 2; re-checked."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–N read; in scope (system_method): prompt, memory, "
                  "hyperparameters and tool routines rewritten from execution transcripts and retained across episodes. "
                  "All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "sol", "task",
                "Identical replays of the selection instance (opus:O12, O14); precedent cal-h1-v2.", ["opus:O12", "opus:O14"],
                "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "adapt_via_conditioning",
                "See rs_pattern.reason.", ["son55:E001", "sol:E001"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["adapt_via_conditioning", None]],
                "See rs_pattern.reason.", ["son55:E001", "son55:E012"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["attribute_and_patch_incumbent", "H10"], ["population_search_executable_fitness", None]],
                "H10 is the load-bearing channel (single prompt rewritten from transcript diagnosis; w/o Prompt is the "
                "largest drop). Population search with UCB over parent+children against native return fits the main card. "
                "H00 and H12 rejected, see domain_pattern.unassigned.", ["sol:E001", "sol:E006", "sol:E009", "opus:O05"],
                NOSCORE),
            X(p, "local:2510.13220-1", *C(p, "expectations[local:2510.13220-1].status"), "son55", "unmet",
              "A4 ID collision: sol local-1 (comparison vs online RL) and son55 local-1 (instance-replay brittleness) are "
              "different questions. Final local-1 = son55's question: unmet (no task variants; identical reset, "
              "opus:O12/O14). sol's question kept as local:2510.13220-4 (partial).", ["son55:E015", "opus:O12", "opus:O14"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "revised",
              "partial", "Prompt channel isolated; other channels single-run, 3 games, small deltas (opus:O11).",
              ["son55:E012", "opus:O11"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "son55",
              "unmet", "Verified: public Jericho games, no check of backbone/Evolver knowledge of walkthroughs.",
              ["son55:E016"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "met", "Verified: full-history Memory, RAG and Summary baselines under the same step budget.",
              ["son55:E010", "son55:E011"]),
            X(p, "rs:adapt_via_conditioning/RE-5", *C(p, "expectations[rs:adapt_via_conditioning/RE-5].status"), "son55",
              "partial", "Verified: six games and several backbones, one benchmark family.", ["son55:E016"]),
            X(p, "rsi:abstract_experience_into_guidance/F5",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/F5].status"), "son55", "met",
              "Verified: success memory is keyed on score deltas (outcome-grounded). Kept as a satisfied check although "
              "H00 is not assigned in the final domain match.", ["son55:E006"]),
            X(p, "rsi:attribute_and_patch_incumbent/S2", *C(p, "expectations[rsi:attribute_and_patch_incumbent/S2].status"),
              "sol", "met", "Verified: UCB steers which configuration gets the next episode; greedy ablation degrades.",
              ["sol:E006", "sol:E009"]),
            X(p, "rsi:attribute_and_patch_incumbent/S3", *C(p, "expectations[rsi:attribute_and_patch_incumbent/S3].status"),
              "sol", "partial", "Parent fallback protects earlier wins after a bad episode, but a child is promoted "
                                "without any prior check and its bad episode counts; memory updates are inherited by all "
                                "children unconditionally. Fallback ≠ 'accepted only if they individually improve'.",
              ["sol:E005", "sol:E007", "son55:E008"]),
            X(p, "rsi:population_search_executable_fitness/S6",
              *C(p, "expectations[rsi:population_search_executable_fitness/S6].status"), "sol", "partial",
              "Verified: genome enlargement is motivated by a named prompt-only ceiling, but the added channels contribute "
              "little (opus:O11).", ["sol:E002", "opus:O11"]),
            res("ratings.G", *C(p, "ratings.G"), "sol", {"status": "resolved", "rating": 2},
                "Closest whole-system neighbours named without residual (opus:O13).", ["opus:O13", "son55:E003"],
                "-3.75 vs son55"),
            res("ratings.X", *C(p, "ratings.X"), "sol", {"status": "resolved", "rating": 2},
                "Candidate-generation inconsistency, unspecified UCB init/β/m, failure-memory contradiction.",
                ["opus:O05", "opus:O06", "opus:O07", "opus:O08"], "-5.0 vs son55"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", {"status": "resolved", "rating": 2},
                "Simple-mutation ablation ≈ EvoPrompt; optimizer-model confound; small non-prompt deltas.",
                ["opus:O01", "opus:O02", "opus:O09", "opus:O10", "opus:O11"], "-3.75 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2510.13220-2]",
             "sol_value": "partial — statistics", "son55_value": "partial — cost (Evolver vs weight-update baselines)",
             "final_value": "local-2 = cost (sol local-3 + son55 local-2); local-3 = statistics (sol local-2 + son55 local-3)",
             "correction": "A4 hidden collision: same IDs, different questions, equal statuses, so the mechanical diff did "
                           "not flag them.", "evidence_ids": ["sol:E012", "son55:E019"], "score_impact": "none"},
            {"field_path": "claims[C1].counterevidence",
             "sol_value": "ablation/backbone confounds noted", "son55_value": "Evolver parity noted",
             "final_value": "adds opus:O01 (generic-prompt EvoTest = EvoPrompt) and opus:O11",
             "correction": "Neither seat used Table 5's Simple-Mutation row as counterevidence to the whole-system "
                           "attribution.", "evidence_ids": ["opus:O01", "opus:O02"],
             "score_impact": "supports E.causality 2 (already sol's value)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before seats: strong in-session gains with 5 seeds; same instance "
                                                   "replayed → task-level; Simple-Mutation row equals EvoPrompt, so the "
                                                   "multi-channel attribution is weak; o3 optimizer vs unspecified baseline "
                                                   "optimizers; m/β missing and failure-memory contradiction.",
            "integrity_checks": "Both seats a1 on 2510.13220v2, material sha d6016baf…; seat hashes equal conflicts.json; "
                                "both completed identification.",
            "core_claim_check": "Strongest supported claim narrowed to the prompt-evolution gain on identical replays.",
            "rating_agreement": "M 3, E.measurement 3, E.holdout 1, E.statistics 2, E.cost 2 agree and were re-checked.",
        },
    }

    # =========================================================== 2510.13614 MemoTime (Δ10)
    p = "2510.13614"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Qwen3-32B 68.2 42.5 77.6 62.1 81.7", "Table 1 (MultiTQ)", "Main-table Qwen3-32B overall 68.2."),
            opus_ev(p, "O02", "1.3 61.4 46.2", "Table 3 (MultiTQ, Qwen3-32B IO / MemoTime / gain)",
                    "Same backbone and dataset: 61.4 here vs 68.2 in Table 1 (opus:O01)."),
            opus_ev(p, "O03", "7.5 70.9 8.5", "Table 3 (MultiTQ, DeepSeek-V3)", "70.9 vs 73.0 in Table 1 (opus:O04)."),
            opus_ev(p, "O04", "DeepSeek-V3 73.0 45.9 82.9 67.7 84.6", "Table 1 (MultiTQ)", "Main-table DeepSeek-V3."),
            opus_ev(p, "O05", "12.0 76.3 5.4", "Table 3 (MultiTQ, GPT-4-Turbo)", "76.3 vs 77.9 in Table 1."),
            opus_ev(p, "O06", "DeepSeek-V3 67.8 63.1 53.3 71.3 54.3", "Table 2 (TimeQuestions)",
                    "67.8 vs 64.6 for the same cell in Table 3; differences up to 6.8 pp exceed the 4.4 pp memory effect."),
            opus_ev(p, "O07", "For each baseline, we adopt the reported performance values from their original publications",
                    "Appendix D", "Baselines are copied numbers with their own (mostly GPT-3.5) backbones."),
            opus_ev(p, "O08", "The incorrect samples are used as warnings.", "§4.4",
                    "Implies correctness of stored traces is known; the source of that label is not stated."),
            opus_ev(p, "O09", "All experiences are dynamically learned from verified reasoning traces, with five predefined "
                    "exemplars used for cold-start initialization.", "Appendix D",
                    "The data stream the pool is built from (train vs test) is not stated."),
            opus_ev(p, "O10", "w/o Experience Memory 59.8", "Table 4", "Single store-off point: GPT-4o-mini, MultiTQ, one run."),
            opus_ev(p, "O11", "Fine-tune 64.8 66.0 52.9 77.6 45.5", "Table 2 (TimeR4)",
                    "TimeR4 overall 64.8 exceeds MemoTime with Qwen3-32B (60.6, opus:O12) and GPT-4o-mini (60.9)."),
            opus_ev(p, "O12", "Qwen3-32B 60.6 58.3 51.1 69.8 53.3", "Table 2 (TimeQuestions)", "See opus:O11."),
            opus_ev(p, "O13", "MemoTime achieves new state-of-the-art results under all backbone LLMs", "§5.1",
                    "Contradicted by opus:O11/O12."),
            opus_ev(p, "O14", "the overall accuracy increases from 64.2% to 58.3%", "§5.2", "Text error (it decreases)."),
            opus_ev(p, "O15", "obsolete or low-value traces are periodically pruned to prevent redundancy", "§4.4",
                    "Pruning/decay without criteria or thresholds."),
        ],
        "rs_pattern": {
            "primary": "decompose_and_delegate", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Primary = son55: the framework's load-bearing operation is decomposing temporal questions into "
                      "indicator-typed sub-questions routed to symbolic temporal toolkits/BiBFS (removing retrieval collapses "
                      "64.2→11.2; tree removal costs multi-entity 40.3→19.3). Supporting adapt_via_conditioning with C03 "
                      "(sol): typed experience exemplars retrieved as first-class prompt inputs to a frozen LLM, the run's "
                      "convention for retrieval memories (partial fit; no category holdout or leakage audit).",
            "matches": [smatch("son55", p, "decompose_and_delegate"),
                        smatch("sol", p, "adapt_via_conditioning", role="supporting",
                               fit="partial (C03 retrieval branch; secondary component)")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": prefix(copy.deepcopy(seat("sol", p)["domain_pattern"]), "sol"),
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol"),
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "rs:adapt_via_conditioning/RE-3": {
                    "status": "unmet",
                    "reason": "Opus final (son55): the stated gap is static exemplars, yet no equal-size static exemplar "
                              "bank, flat retrieval or longer-context baseline is run; IO and memory-off are not cheaper "
                              "conditioning alternatives (the card treats own-method ablations as insufficient)."},
                "local:2510.13614-2": {
                    "status": "partial",
                    "reason": "Opus final: against raw GPT-4-Turbo (IO 12.0 / 44.0) Qwen3-4B+MemoTime (55.3 / 45.3) is "
                              "comparable or better, which supports the abstract's wording; against GPT-4-Turbo inside the "
                              "same pipeline (76.3 / 68.1) it is far behind. The claim holds only in the IO reading. "
                              "'challenged_with_evidence' denotes an author challenge to the expectation, not a refuted "
                              "claim."},
                "rsi:index_experience_for_reuse/F1": {
                    "status": "partial",
                    "reason": "Opus final: the store is a real growing, reused store (so F1's 'not a growing store' "
                              "failure does not literally apply), but it is secondary — memory-off costs 4.4 pp while "
                              "retrieval-off collapses accuracy."},
                "rsi:index_experience_for_reuse/F3": {
                    "status": "unmet",
                    "reason": "Opus final: full text read, so not 'unknown'. Whether the pool is built from the test "
                              "stream is not stated (opus:O09) and 'incorrect samples' implies label knowledge (opus:O08); "
                              "no separation is shown."},
                "rsi:index_experience_for_reuse/F4": {
                    "status": "unmet",
                    "reason": "Opus final: admission is the LLM's own sufficiency/debate verdict — exactly 'on the "
                              "model's own word'. Same fact as S2 (sol, unmet)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O11", "opus:O12", "opus:O13"]),
                                        "C3", ["opus:O02", "opus:O06"]),
        "assessment": {
            "evidence_level": "task",
            "evidence_level_note": "Both seats 'task', re-checked: one store-off point (opus:O10) on an unstated "
                                   "construction stream (opus:O09) with possible label access (opus:O08); no frozen-store "
                                   "or held-out evaluation, so retained is not certified.",
            "claim_support": "scoped",
            "strongest_supported_claim": seat("son55", p)["assessment"]["strongest_supported_claim"],
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + [
                "Evaluated test-subset size (54,584 MultiTQ test questions at ~43 s each).",
                "Meaning and source of 'incorrect samples are used as warnings' (opus:O08)."],
        },
        "ratings": {
            "G": keep("sol", p, "G", "Both seats 2; re-checked."),
            "M": R("resolved", 3, "Opus sides with sol. M judges the whole method against its four stated problems: "
                   "monotone time filtering, co-constrained multi-entity paths, operator toolkits and typed experience "
                   "reuse each target a named failure and make distinguishable predictions that the ablations test "
                   "(multi-entity 40.3→23.5 without graph retrieval, →19.3 without the tree). son55's 2 rests on the "
                   "memory sub-mechanism alone ('why accumulated exemplars beat fixed ones is asserted'), which is a valid "
                   "weakness but one component of the method; it is kept in X/E.causality.",
                   ["sol:E002", "sol:E003", "sol:E005", "sol:E011", "son55:E009", "son55:E017"], ["son55:E002"]),
            "X": keep("sol", p, "X", "Both seats 2; re-checked (self-judged admission, pruning without criteria, "
                      "opus:O15)."),
            "E.measurement": R("resolved", 2, "Opus sides with sol. Hits@1 against gold is a trustworthy metric, but the "
                               "system's own headline scores are not stably reported: every backbone cell repeated in "
                               "Table 3 differs from Tables 1/2 (68.2 vs 61.4, 73.0 vs 70.9, 77.9 vs 76.3; TimeQuestions "
                               "67.8 vs 64.6 …; opus:O01–O06) with no explanation, by up to 6.8 pp — more than the 4.4 pp "
                               "memory effect. Under A2 inconsistent result reporting is a results/measurement-credibility "
                               "defect and is scored here once (not again under E.statistics).",
                               ["sol:E010", "sol:E013", "opus:O01", "opus:O02", "opus:O03", "opus:O04", "opus:O05",
                                "opus:O06"], ["son55:E012"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. Same-backbone component ablations (graph, embedding, "
                             "all retrieval, question tree, memory) attribute the main parts; the store-off point exists. "
                             "Missing: static-exemplar control for the memory claim, ablations beyond one backbone/dataset, "
                             "and backbone-matched baselines (baseline numbers are copied from papers with weaker LLMs, "
                             "opus:O07). Relevant results with key controls missing = 2; son55's 1 weighs only the memory "
                             "component.",
                             ["sol:E006", "sol:E007", "sol:E009", "son55:E009", "son55:E010", "opus:O07", "opus:O10"],
                             ["son55:E017"]),
            "E.holdout": R("resolved", 1, "Opus sides with sol. Standard train/dev/test splits on two benchmarks give the "
                           "system-level claim some held-out scope, so this is not a full absence (not_reported needs the "
                           "applicable evidence to be wholly missing). For the memory claim, the construction stream "
                           "(opus:O09), its order, any label access (opus:O08) and a frozen-store test are unreported, "
                           "which keeps the item at 1.",
                           ["sol:E011", "son55:E008", "opus:O08", "opus:O09"],
                           [], ["Full text incl. §4.4, §5, Algorithms 1–4, Appendices B–E, Table 8"]),
            "E.statistics": R("resolved", 1, "Opus sides with sol. A2 ladder: test-split denominators per type are given "
                              "(Table 8) and negative/ablation results are reported, but there are no seeds, intervals or "
                              "tests — 1. The cross-table inconsistency is scored under E.measurement (A2), and the "
                              "suspicion that only a subset was evaluated is an inference (recorded as unresolved), not a "
                              "reported fact.",
                              ["sol:E006", "sol:E013", "son55:E011"], ["son55:E013"],
                              ["Full text incl. Tables 1–13, Appendices B and D"]),
            "E.cost": keep("sol", p, "E.cost", "Both seats 1; re-checked."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A–E read; in scope (system_method) through the self-written "
                  "experience pool reused on later questions, which is a secondary component of a TKGQA system. All eight "
                  "items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "son55", "decompose_and_delegate",
                "Decomposition + delegation to symbolic toolkits is the load-bearing operation; memory conditioning is "
                "secondary (see rs_pattern.reason).", ["son55:E011", "son55:E017", "sol:E007"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["decompose_and_delegate", "C25"], ["adapt_via_conditioning", "C03"]],
                "Same two mains in both seats; C03 retained for the retrieval-exemplar branch per run convention.",
                ["sol:E002", "sol:E003"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol",
                [["index_experience_for_reuse", "H03"], ["index_experience_for_reuse", "H04"]],
                "H03 primary (verified traces retrieved as precedents). H04 kept at low fit: a type-partitioned index with "
                "dual embeddings, a hit-ranked high-frequency buffer tier and decay/rebalancing rules are described, but "
                "the structure is never ablated (F6 risk noted).", ["sol:E002", "sol:E005", "opus:O15"], NOSCORE),
            X(p, "local:2510.13614-2", *C(p, "expectations[local:2510.13614-2].status"), "revised", "partial",
              "Claim holds against raw GPT-4-Turbo, not against GPT-4-Turbo in the same pipeline; 'challenged_with_evidence' "
              "is the wrong state for a partly supported author claim.", ["son55:E014"]),
            X(p, "rs:adapt_via_conditioning/RE-1", *C(p, "expectations[rs:adapt_via_conditioning/RE-1].status"), "sol",
              "partial", "Verified: memory-off exists (opus:O10); no same-budget static bank.", ["sol:E006", "opus:O10"]),
            X(p, "rs:adapt_via_conditioning/RE-2", *C(p, "expectations[rs:adapt_via_conditioning/RE-2].status"), "sol",
              "unmet", "Verified: no pool/test separation or overlap audit (opus:O09).", ["sol:E011", "opus:O09"]),
            X(p, "rs:adapt_via_conditioning/RE-3", *C(p, "expectations[rs:adapt_via_conditioning/RE-3].status"), "son55",
              "unmet", "No equal-size static exemplar or other cheaper conditioning baseline; IO/memory-off are own-method "
                       "ablations.", ["son55:E002", "son55:E009"]),
            X(p, "rs:decompose_and_delegate/RE-2", *C(p, "expectations[rs:decompose_and_delegate/RE-2].status"), "son55",
              "partial", "Verified: each component ablated once (GPT-4o-mini, MultiTQ, one run).", ["son55:E009"]),
            X(p, "rs:decompose_and_delegate/RE-3", *C(p, "expectations[rs:decompose_and_delegate/RE-3].status"), "sol",
              "met", "Verified: algorithms, toolkit table, hyperparameters and all prompts disclosed (disclosure, not "
                     "reproduction).", ["sol:E003", "sol:E011"]),
            X(p, "rsi:index_experience_for_reuse/F1", *C(p, "expectations[rsi:index_experience_for_reuse/F1].status"),
              "revised", "partial", "Growing reused store exists but is secondary (−4.4 pp vs retrieval collapse).",
              ["son55:E010", "son55:E017", "opus:O10"]),
            X(p, "rsi:index_experience_for_reuse/F3", *C(p, "expectations[rsi:index_experience_for_reuse/F3].status"),
              "revised", "unmet", "Full text read; separation not shown (opus:O08/O09). 'unknown' is reserved for "
                                  "unread material.", ["son55:E008", "opus:O08", "opus:O09"]),
            X(p, "rsi:index_experience_for_reuse/F4", *C(p, "expectations[rsi:index_experience_for_reuse/F4].status"),
              "revised", "unmet", "LLM sufficiency verdict is the model's own word; same fact as S2.",
              ["son55:E004", "sol:E003"]),
            X(p, "rsi:index_experience_for_reuse/S2", *C(p, "expectations[rsi:index_experience_for_reuse/S2].status"),
              "same_supported_fact", "unmet", "Same fact as F4 (no external write gate).", ["sol:E003", "sol:E011"]),
            X(p, "rsi:index_experience_for_reuse/S5", *C(p, "expectations[rsi:index_experience_for_reuse/S5].status"),
              "sol", "met", "Verified: same-backbone memory-off 64.2→59.8 (opus:O10); only one setting.",
              ["sol:E006", "opus:O10"]),
            X(p, "rsi:index_experience_for_reuse/S6", *C(p, "expectations[rsi:index_experience_for_reuse/S6].status"),
              "sol", "partial", "Verified: buffer and pruning described without thresholds or growth curve (opus:O15).",
              ["sol:E005", "opus:O15"]),
            res("ratings.M", *C(p, "ratings.M"), "sol", {"status": "resolved", "rating": 3},
                "Whole-method problem-fit with tested predictions; memory weakness kept elsewhere.",
                ["sol:E003", "son55:E009"], "+5.0 vs son55"),
            res("ratings.E.measurement", *C(p, "ratings.E.measurement"), "sol", {"status": "resolved", "rating": 2},
                "Own headline numbers inconsistent across tables by up to 6.8 pp; scored here once per A2.",
                ["opus:O01", "opus:O02", "opus:O06"], "-2.5 vs son55"),
            res("ratings.E.causality", *C(p, "ratings.E.causality"), "sol", {"status": "resolved", "rating": 2},
                "Component ablations attribute the main parts; memory and baseline-backbone controls missing.",
                ["sol:E007", "opus:O07", "opus:O10"], "+3.75 vs son55"),
            res("ratings.E.holdout", *C(p, "ratings.E.holdout"), "sol", {"status": "resolved", "rating": 1},
                "Standard test splits give partial system-level scope; memory construction stream unreported.",
                ["opus:O08", "opus:O09"], "+2.5 vs son55"),
            res("ratings.E.statistics", *C(p, "ratings.E.statistics"), "sol", {"status": "resolved", "rating": 1},
                "Denominators and negative results but no uncertainty (A2 → 1); table conflict scored under E.measurement.",
                ["sol:E013", "son55:E011"], "+1.25 vs son55"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement.reason / ratings.E.statistics.reason",
             "sol_value": "table conflict under E.measurement", "son55_value": "table conflict under E.statistics "
                                                                              "(and E.measurement 'marked down')",
             "final_value": "scored once, under E.measurement (A2 single-defect rule)",
             "correction": "son55 counted the Table 1/3 conflict in both items.", "evidence_ids": ["opus:O02", "opus:O06"],
             "score_impact": "accounted in the E.statistics resolution"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before seats: strong TKGQA system, memory secondary (−4.4 pp, one "
                                                   "setting); main-table vs Table 3 numbers disagree for every backbone; "
                                                   "baselines copied with weaker LLMs; pool construction stream and "
                                                   "'incorrect samples as warnings' unexplained; 'SOTA under all backbones' "
                                                   "contradicted by TimeR4 on TimeQuestions.",
            "integrity_checks": "Both seats a1 on 2510.13614v3, material sha 4769b6a7…; seat hashes equal conflicts.json; "
                                "both completed identification.",
            "core_claim_check": "C2 (SOTA under all backbones) contradicted (opus:O11–O13); C3 (continual improvement) "
                                "unsupported beyond one store-off point.",
            "rating_agreement": "G 2, X 2, E.cost 1 agree and were re-checked.",
        },
    }

    # =========================================================== 2510.14253 ASL (both out_of_scope)
    p = "2510.14253"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Checked independently: the "
          "Prompt Generator, Policy Model and Generative Reward Model share one LLM's parameters (opus:O01) and each is "
          "updated by RL (opus:O02); the retained artifacts — validated generated QA pairs and (question, answer, "
          "difficulty-flag) triples — are training sets consumed by the next round of weight updates (opus:O03, O04), and "
          "every reported result is the test accuracy of trained checkpoints (opus:O05). Same ruling as r07a Middo / "
          "r06a SyncLoop (evolved training data + retraining). Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Since all roles share parameters, skill improvements in one role naturally benefit the others",
                    "§3.4", "One parameter set serves all three roles."),
            opus_ev(p, "O02", "use it as the reward signal to update the Prompt Generator’s parameters", "§3.3 Phase 1",
                    "Even the 'prompt' generator improves by weight updates."),
            opus_ev(p, "O03", "we then store the pair into the Policy Model training set", "§3.3 Phase 1",
                    "Retained tasks are policy training data."),
            opus_ev(p, "O04", "is stored into the Prompt Generator’s training dataset", "§3.3 Phase 3",
                    "Difficulty-flag triples are generator training data."),
            opus_ev(p, "O05", "The test accuracy of LLM agents trained by ASL and baseline methods.", "Figure 4 caption",
                    "Evaluated object = trained agent weights."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": [], "outside_taxonomy": False,
            "reason": "Informational (out_of_scope): a generator synthesizes QA tasks, a learned GRM gate (mean score > C) "
                      "admits them, the policy is retrained on them, and learner difficulty feedback steers the next "
                      "batch — C08's generate→gate→retrain loop with dynamic learner feedback (run precedent r07a Middo/"
                      "SPELL). Both seats skipped identification for an excluded row, which the contract allows.",
            "matches": [{"main_id": "self_supervised_signal_engineering", "sub_id": "C08", "role": "primary",
                         "fit": "medium (informational, out_of_scope)",
                         "tactic_steps_checked": "C08: controllable generator → single quality gate (GRM K-rollout mean "
                                                 "> C) → retained instances folded into training → iterated with learner "
                                                 "difficulty flags.",
                         "success_checks": "Author-reported round-over-round test gains; not used as Harness-RSI evidence.",
                         "failure_checks": "Frozen-GRM ablation shows reward hacking (author-reported).",
                         "evidence_ids": ["opus:O03", "opus:O04", "sol:E005"],
                         "reason": "Informational only; no score."}],
            "executes_pattern": True, "resolves_problem": "not assessed (out_of_scope)",
        },
        "domain_pattern": {"namespace": "rsi", "matches": [], "unassigned": True, "revision_proposals": [],
                           "reason": "Kept from sol: no non-weight domain card is assigned to an excluded row; coevolve_"
                                     "the_evaluator / self_generate_the_curriculum resemble the loop but the evaluator and "
                                     "curriculum are weights and training data (A3)."},
        "pattern_mapping": [],
        "expectations": lambda sol, son: merge_exps(p, sol, son, rename={}, overrides={}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b/r06a/r07a).",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; Figure 4–6 gains are author-reported RL "
                                             "checkpoint results.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; independently re-checked and confirmed)",
        "resolutions": [
            X(p, "local:2510.14253-1", *C(p, "expectations[local:2510.14253-1].status"), "sol", "unmet",
              "Informational: the expectation that the retained, evaluated object be a non-weight harness component is "
              "unmet (opus:O01–O05). son55 recorded no expectations for an excluded row, which the contract allows.",
              ["opus:O01", "opus:O03", "opus:O05"]),
        ],
        "shared_error_corrections": [
            {"field_path": "assessment.evidence_level", "sol_value": "task", "son55_value": "task", "final_value": None,
             "correction": "Run convention for out_of_scope rows is null (r05b/r06a/r07a): the task/retained/improver "
                           "ladder grades harness changes and does not apply to a weight-level paper.",
             "evidence_ids": ["opus:O05"], "score_impact": "none (not scored)"},
            {"field_path": "assessment.claim_support", "sol_value": "unresolved", "son55_value": "unresolved",
             "final_value": None, "correction": "Same convention: claim support is not assessed for excluded rows.",
             "evidence_ids": ["opus:O05"], "score_impact": "none"},
            {"field_path": "rs_pattern", "sol_value": "primary null, outside_taxonomy false",
             "son55_value": "primary null, outside_taxonomy true",
             "final_value": "informational self_supervised_signal_engineering/C08",
             "correction": "Not an error (identification is optional for out_of_scope rows); completed for consistency "
                           "with r07a precedent and to remove the outside_taxonomy disagreement. son55's 'outside_taxonomy' "
                           "was wrong: C08 covers the loop.", "evidence_ids": ["opus:O03", "opus:O04"],
             "score_impact": "none"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read abstract, §1–5 and Appendix A prompts before seats: three RL-"
                                                   "trained roles on shared weights; retained data are training sets; "
                                                   "results are checkpoints → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2510.14253v2, material sha 11543e97…; seat hashes equal conflicts.json; "
                                "both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01–O05. The meta-prompt triples that condition the generator "
                                "are its RL training prompts, not a deployed non-weight artifact.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
    }

    # =========================================================== 2510.16079 EvolveR (tie 67.5)
    p = "2510.16079"
    S[p] = {
        "base": "sol",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "No No Yes 0.325", "Table 4 (component attribution, 3B)",
                    "The 'RL only' row (no distillation, no retrieval) is 0.325 …"),
            opus_ev(p, "O02", "Search-R1-instruct 0.341 0.324 0.545 0.378 0.319 0.103 0.264 0.325", "Table 1 (3B)",
                    "… identical to the Search-R1-instruct average, i.e. the RL-only control is the external Search-R1 "
                    "baseline row, not an EvolveR-recipe run without the experience lifecycle (our inference from the "
                    "identical values; no separate RL-only configuration is described)."),
            opus_ev(p, "O03", "No None 0.325", "Table 5 (memory configuration)", "Same reused value as the no-store row."),
            opus_ev(p, "O04", "Yes Yes No 0.357", "Table 4", "The 'no RL' row …"),
            opus_ev(p, "O05", "EvolveR(SFT) 0.415 0.357 0.584 0.419 0.366 0.106 0.248 0.357", "Table 8",
                    "… equals the SFT-trained variant, so 'no RL' still trains weights on EvolveR trajectories."),
            opus_ev(p, "O06", "Principle Distillation Principle Retrieval RL Avg. Score No No No 0.134", "Table 4",
                    "The 'nothing' row …"),
            opus_ev(p, "O07", "Direct Inference 0.106 0.149 0.288 0.108 0.244 0.020 0.024 0.134", "Table 1 (3B)",
                    "… equals Direct Inference (no cold-start SFT either)."),
            opus_ev(p, "O08", "Following prior works, we compare against a comprehensive suite of baselines built upon the "
                    "Qwen2.5 foundational models.", "§4.1.2", "Baselines follow prior work; parity of training recipe "
                                                              "with EvolveR is not stated."),
            opus_ev(p, "O09", "we introduce a cold-start stage to stabilize early RL training by first fine-tuning the base "
                    "model on a small, curated dataset of CoT interaction trajectories", "§4.1.4",
                    "EvolveR alone gets a cold-start SFT stage …"),
            opus_ev(p, "O10", "This prompt guides a powerful LLM (we used GPT-4o) to act as an expert problem-solver",
                    "Appendix A.4.1", "… on GPT-4o-generated trajectories that already include experience-principle "
                                      "usage — privileged external-teacher data in a 'self-contained' lifecycle."),
            opus_ev(p, "O11", "w/o exp-retrieve variant is denied access to the experience base during evaluation.",
                    "§5.2.2", "The only in-pipeline store contrast removes the store from a policy trained to rely on it."),
            opus_ev(p, "O12", "the average performance drops significantly from 0.382 to 0.340", "§5.2.2",
                    "The store-off policy (0.340) still exceeds the Search-R1 row (0.325), so part of the gain over "
                    "Search-R1 is the training recipe, not the retained store."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Final = sol (C03). EvolveR executes C03 more fully than retrieval-only memories: an upstream phase "
                      "(cold-start SFT + GRPO with retrieved principles in context) teaches the policy to read the "
                      "conditioning substrate, and generalization is tested on five held-out datasets. Held-out "
                      "datasets, not task categories, and no contamination audit → fit kept 'high' only for the "
                      "operation, not the evidence.",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": True, "resolves_problem": "partial",
        },
        "domain_pattern": {
            "namespace": "rsi",
            "matches": [dmatch("sol", p, "abstract_experience_into_guidance", "H00"),
                        dmatch("sol", p, "abstract_experience_into_guidance", "H01"),
                        dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                        dmatch("son55", p, "evidence_gated_retention", "H29")],
            "unassigned": [],
            "revision_proposals": [],
            "boundary_notes": seat("sol", p)["domain_pattern"].get("boundary_notes"),
        },
        "pattern_mapping": prefix(copy.deepcopy(seat("sol", p)["pattern_mapping"]), "sol") + [
            {"rs_main": "adapt_via_conditioning", "rs_sub": "C03",
             "domain": {"namespace": "rsi", "main": "couple_context_and_weight_updates", "sub": "H28"},
             "operation_correspondence": "C03's upstream 'learn to read the conditioning' phase is the GRPO update on "
                                         "experience-conditioned rollouts — H28's coupling of a context artifact with "
                                         "weight training through shared rollouts.",
             "necessary_conditions_and_differences": "H28 S3 met (policy trained to condition on the principle base); "
                                                     "the internalization variant (exp-absorb) is reported negative.",
             "evidence_ids": ["sol:E012", "sol:E021", "son55:E001"]}],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("son55", "local:2510.16079-1"): "local:2510.16079-3",
                    ("son55", "local:2510.16079-2"): "local:2510.16079-4"},
            overrides={
                "local:2510.16079-3": {"reason": "Opus final (sol local-3 + son55 local-1, same statistics question): no "
                                                 "seeds, intervals or tests; conclusions rest on 0.01–0.02 gaps (0.382 vs "
                                                 "0.370 self vs teacher; flat pruning sweep)."},
                "local:2510.16079-4": {
                    "status": "unmet", "score_item": "E.causality",
                    "reason": "Opus final (son55's question, re-ID'd): full text read, so not 'unknown'. EvolveR alone "
                              "receives cold-start SFT on GPT-4o-generated experience-format trajectories (opus:O09, O10); "
                              "the RL-only comparator is the Search-R1 row (opus:O01, O02); recipe parity is not shown."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C4", ["opus:O01", "opus:O02", "opus:O09", "opus:O10", "opus:O12"]),
                                        "C1", ["opus:O11"]),
        "assessment": {
            "evidence_level": "retained",
            "evidence_level_note": "Both seats 'retained', re-checked: the principle base is built on NQ/HotpotQA training "
                                   "splits and read on disjoint test sets incl. five evaluation-only datasets; removing it "
                                   "at evaluation drops the same trained policy 0.382→0.340. Caveat: that contrast removes "
                                   "a store the policy was trained to depend on (opus:O11), and no recipe-matched no-store "
                                   "policy exists (opus:O01/O02), so the size of the retained-store effect is bounded only "
                                   "loosely. Not improver.",
            "claim_support": "scoped",
            "strongest_supported_claim": "With an RL-trained 3B/7B policy that learned to consult it, a self-built principle "
                                         "base from training splits improves later held-out QA versus the same policy "
                                         "without access (author-reported, single runs). Superiority of the whole "
                                         "lifecycle over Search-R1 is confounded with a GPT-4o cold-start SFT recipe "
                                         "Search-R1 did not receive; self- vs teacher-distillation at 3B (0.382 vs 0.370) "
                                         "is within untested noise.",
            "unresolved": seat("sol", p)["assessment"]["unresolved"] + seat("son55", p)["assessment"]["unresolved"],
        },
        "ratings": {
            "G": keep("sol", p, "G", "Both seats 2; re-checked."),
            "M": keep("sol", p, "M", "Both seats 3; re-checked."),
            "X": keep("sol", p, "X", "Both seats 3; re-checked (thresholds, prompts, masking disclosed; offline cadence "
                      "and test-time freezing of the base unstated)."),
            "E.measurement": keep("son55", p, "E.measurement", "Both seats 3; re-checked."),
            "E.causality": R("resolved", 2, "Shared-error correction (both seats 3 → 2). The decisive control for the "
                             "central claim — the lifecycle versus RL alone under the same recipe — is not run: Table 4's "
                             "'RL only' row and Table 5's no-store row are the Search-R1 baseline average (0.325, "
                             "opus:O01–O03), the 'no RL' row is the SFT-trained variant (opus:O04/O05) and the 'nothing' "
                             "row is Direct Inference (opus:O06/O07). EvolveR alone gets cold-start SFT on GPT-4o-"
                             "generated experience-format trajectories (opus:O09/O10) and a format reward, so the gap to "
                             "Search-R1 mixes recipe and store; the store-off policy (0.340) already beats that row "
                             "(opus:O12). The only in-pipeline store contrast removes the store from a policy trained to "
                             "use it (opus:O11). No raw-trajectory memory or curator-off control; self vs teacher gap "
                             "0.012 single run. Real controls exist (store-off, teacher, SFT-vs-RL) → 2, not 1.",
                             ["sol:E011", "sol:E012", "sol:E013", "son55:E010", "son55:E021", "opus:O01", "opus:O02",
                              "opus:O04", "opus:O05", "opus:O09", "opus:O10", "opus:O11", "opus:O12"],
                             ["son55:E016", "son55:E017"]),
            "E.holdout": keep("sol", p, "E.holdout", "Both seats 3; re-checked (train-split construction, five "
                              "evaluation-only datasets; no contamination audit)."),
            "E.statistics": keep("sol", p, "E.statistics", "Both seats 1; re-checked."),
            "E.cost": keep("sol", p, "E.cost", "Both seats 2; re-checked (GPT-4o cold-start data and teacher calls "
                           "uncharged)."),
        },
        "status": "reviewed",
        "reason": "Complete pinned v3 text incl. Appendices A.1–A.6 read; in scope under A3: the non-weight principle base "
                  "is retained and evaluated on its own (store-off at evaluation) even though the consuming policy is "
                  "RL-trained. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "C03's upstream 'learn to read conditioning' phase plus held-out datasets are executed (see "
                "rs_pattern.reason).", ["sol:E007", "sol:E008", "sol:E012", "sol:E021"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "revised",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"],
                 ["couple_context_and_weight_updates", "H28"], ["evidence_gated_retention", "H29"]],
                "Union: H00 (both) — outcome-labelled trajectories distilled into principles; H01 (sol) — add/merge/prune "
                "maintenance; H28 (son55) — the defining feature is GRPO on experience-conditioned rollouts so the policy "
                "learns to use the base; H29 (son55, low fit) — per-principle success/usage utility drives pruning, "
                "without a counterfactual (S1 unmet). Each card's operation is present; none is redundant.",
                ["sol:E003", "sol:E004", "sol:E005", "sol:E012", "son55:E006", "son55:E011"], NOSCORE),
            X(p, "local:2510.16079-1", *C(p, "expectations[local:2510.16079-1].status"), "sol", "partial",
              "A4 ID collision: sol local-1 (pruning efficacy / improving distillation) vs son55 local-1 (≤0.02 component "
              "gaps without repeats). Final local-1 = sol's question (partial: score-tier audit is correlational, creation-"
              "phase analysis is survivor-biased). son55's question merged into local-3 (statistics, unmet — same as "
              "sol's local-3).", ["sol:E015", "sol:E016", "sol:E020", "son55:E012", "son55:E013"]),
            X(p, "local:2510.16079-2", *C(p, "expectations[local:2510.16079-2].status"), "sol", "partial",
              "A4 ID collision: sol local-2 (efficiency/scalability claim; partial) vs son55 local-2 (cold-start/baseline "
              "parity; 'unknown'). Final local-2 = sol's question. son55's question re-ID'd local:2510.16079-4 and "
              "revised to unmet (full text read; parity not shown, opus:O01/O02/O09/O10).",
              ["sol:E018", "sol:E019", "son55:E016", "son55:E017", "opus:O09"]),
            X(p, "local:2510.16079-3", *C(p, "expectations[local:2510.16079-3].status"), "sol", "unmet",
              "Verified: no seeds/intervals/tests; son55 asked the same under local-1 (unmet).",
              ["sol:E010", "sol:E013", "son55:E012"]),
            X(p, "rs:adapt_via_conditioning/RE-6", *C(p, "expectations[rs:adapt_via_conditioning/RE-6].status"), "sol",
              "partial", "Source quality/coverage is probed (teacher vs self, score-tier audit, base-size table), but the "
                         "size table is confounded with training progress, teacher vs self is one run, and there is no "
                         "controlled noise injection.", ["sol:E011", "sol:E015", "sol:E018"]),
            X(p, "rsi:abstract_experience_into_guidance/S2",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S2].status"), "sol", "partial",
              "Verified: separate success/failure prompts; no paired contrast. son55 noted the same in its H00 condition "
              "checks.", ["sol:E002"]),
            X(p, "rsi:abstract_experience_into_guidance/S3",
              *C(p, "expectations[rsi:abstract_experience_into_guidance/S3].status"), "sol", "met",
              "Verified: trajectory success is gold EM, not self-judgment; son55's H00 checks say the same.",
              ["sol:E006", "son55:E008"]),
            X(p, "rsi:couple_context_and_weight_updates/S3",
              *C(p, "expectations[rsi:couple_context_and_weight_updates/S3].status"), "son55", "met",
              "Verified: GRPO trains on experience-conditioned rollouts with principle tokens masked — the policy learns "
              "to use the base.", ["son55:E001", "son55:E011", "sol:E021"]),
            X(p, "rsi:evidence_gated_retention/S1", *C(p, "expectations[rsi:evidence_gated_retention/S1].status"),
              "son55", "unmet", "Verified: s(p) is a smoothed success/usage ratio with no with/without-entry contrast.",
              ["son55:E006", "sol:E005"]),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.causality", "sol_value": {"status": "resolved", "rating": 3},
             "son55_value": {"status": "resolved", "rating": 3}, "final_value": {"status": "resolved", "rating": 2},
             "correction": "Both seats credited Table 4/5 as an attribution grid. Its control rows are reused baseline "
                           "values (RL-only = Search-R1 0.325, no-RL = SFT variant 0.357, nothing = Direct Inference "
                           "0.134; opus:O01–O07), EvolveR alone receives GPT-4o cold-start SFT (opus:O09/O10), and the "
                           "store-off policy already beats the RL-only row (opus:O12). son55 flagged cold-start parity as "
                           "'unknown' but still scored 3.",
             "evidence_ids": ["opus:O01", "opus:O02", "opus:O05", "opus:O07", "opus:O09", "opus:O10", "opus:O12"],
             "score_impact": "-3.75 (67.5 → 63.75)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Before seats: retained principle base on held-out QA (store-off at eval "
                                                   "−0.042 at 3B); but Table 4/5 control rows coincide with other tables' "
                                                   "baselines, GPT-4o cold start only for EvolveR, single runs, self vs "
                                                   "teacher within noise. Expected E.causality 2, otherwise ~seat level.",
            "integrity_checks": "Both seats a1 on 2510.16079v3, material sha 7b5662a3…; seat hashes equal conflicts.json; "
                                "both completed identification; namespaces/parents valid.",
            "core_claim_check": "Same score in both seats (67.5) re-derived item by item; one shared error found "
                                "(E.causality).",
            "rating_agreement": "All eight items agreed between seats; seven confirmed, E.causality corrected.",
        },
    }
    return S


def batch_notes():
    return [
        "2510.11290 AAS: G 1 (son55), X 2 (sol), E.measurement 1 (son55); scoring reference doubles as the stream that "
        "drives iteration; context-only also rises. Final 37.5 (sol 43.75, son55 32.5).",
        "2510.13220 EvoTest: evidence_level task (identical replays, UCB selection on the same episodes; cal-h1-v2 "
        "precedent). G/X/E.causality 2 (sol): Simple-Mutation EvoTest = EvoPrompt, o3 optimizer vs unstated baseline "
        "optimizers, m-children vs one-config-per-call inconsistency. RS → adapt_via_conditioning (son55), domain H10 + "
        "population search (sol). Final 55.0 (sol 55.0, son55 67.5).",
        "2510.13614 MemoTime: all five rating conflicts resolved to sol (M 3, Em 2, Ec 2, Eh 1, Es 1); Table 1/2 vs "
        "Table 3 conflict scored once under E.measurement. RS primary decompose_and_delegate (son55) with C03 supporting. "
        "Final 50.0 (sol 50.0, son55 40.0).",
        "2510.14253 ASL: both out_of_scope confirmed (three RL-trained roles on shared weights; retained data are training "
        "sets). Shared corrections: evidence_level/claim_support → null; informational RS C08.",
        "2510.16079 EvolveR: same seat score 67.5; shared error in E.causality (3 → 2): Table 4/5 control rows reuse "
        "Search-R1 / SFT-variant / Direct-Inference values and only EvolveR gets GPT-4o cold-start SFT. Domain union H00, "
        "H01, H28, H29. Final 63.75.",
        "Card revision proposals (not applied): none new this batch. Note for calibration: son55 used "
        "'challenged_with_evidence' (2510.13614 local-2) and 'unknown' after a full read (13614 F3, 16079 local-2, "
        "11290 local-2) — worker prompt could restate that expectation 'unknown' is for unread material.",
        "Seat quote check: 11 son55 quotes (11290 E005/E007/E009/E013; 13220 E006/E008/E009/E018/E019; 16079 "
        "E003/E020) miss only the strict whitespace match; all match verbatim after normalising curly to straight "
        "apostrophes/quotes and en/em dashes — transcription of punctuation, not fabricated text.",
        "No requests for new material.",
    ]
