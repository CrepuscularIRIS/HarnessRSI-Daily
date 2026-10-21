"""Opus rulings for r10a a1 (data only; consumed by _build.py)."""
import copy

FIG_SHA = "de6d89f49e6e37bcaf73a631b27c03d97dfe262d983c5d171a8cd4ad3b16cafe"
FIG_PATH = "research/fulltext/review-runs/rsi-v22-20261021-01/materials/2512.18746.pages/p-09.png"


def batch_notes():
    return [
        "2512.10398 CCA (seat Δ13.75): final 40.0, below both seats (56.25 / 42.5). G, M and X go to son55 "
        "(2/2/1): the gap is broad and not measured against Live-SWE-Agent, the meta-agent's acceptance rule, test "
        "set and iteration count are never reported, and notes have no gate. Shared-error correction: "
        "E.measurement 3→2 (both seats). Several reported percentages are arithmetically impossible for their "
        "stated denominators: Table 2 48.6/51.6 on a '100-example subset', Table 3 49.2/203 and 44.1/86 with "
        "buckets summing to 639 of 731, and Table 4 Run 2 54.4 on 151 tasks. The commercial rows are copied from "
        "system cards, although the caption calls the environments 'identical'. This is the same reporting-integrity "
        "cap as r09b EvoRoute/AgentDevel. evidence_level → task (son55): the note rerun uses the 151 tasks that "
        "produced the notes, and the tool ablation compares against a naive stack rather than a pre-meta-agent "
        "stack. RS layer → sol (generative_process_redesign + adapt_via_conditioning, both sub null), the run "
        "convention for agent-rewritten scaffolds (r08b Live-SWE-agent, r03b SICA) and for retrieved notes; fit is "
        "low/partial.",
        "2512.10696 ReMe (seats tied at 65.0): final 61.25. G → son55 2. The 'no removal mechanism' gap is "
        "overstated: the deletion thresholds are themselves taken from prior work on memory deletion (Xiong et "
        "al. 2025). E.causality → sol 2: acquisition (N=8), reflection retries and rerank/rewrite calls are not "
        "budget-matched against the baselines (A2). The component ablations are single-configuration without std, "
        "and dynamic-vs-fixed mixes in test-stream success feedback. Shared items were re-checked. son55's finding "
        "is confirmed: 8B+ReMe beats 14B-no-memory only on averaged Pass@4 (+0.38), not on Avg@4 (−0.68), and the "
        "7.29/8.83 gains are swapped in both the introduction and §4.2. sol missed the swap but scoped the claim. "
        "New shared omission: K=5 and the usage-scenario retrieval key were chosen on the 150-task evaluation set. "
        "No score change (E.holdout stays 2).",
        "2512.17102 SAGE (Δ2.5): final 72.5, above both seats (65.0 / 67.5), reached item by item. X → sol 3: "
        "both the training and the deployment chain can be reconstructed, and the same-scenario boundary is stated. "
        "E.causality → son55 3: the same-weights library toggle, the budget-matched reward ablation and the "
        "SFT-initialised GRPO control all have std; the GRPO compute gap is charged here and in E.cost, but the "
        "components are isolated at matched budget. E.holdout → son55 3: official Train/Dev/Test, Dev-only "
        "checkpoint selection, Test-Challenge with unseen apps, and the privileged scenario label shown "
        "non-load-bearing (label-free Query N-gram 72.0/60.1). The test-time save gate uses no reward. E.cost → son55 "
        "2. The retained library is short-lived (one 3-task scenario of near-duplicate queries), which limits claim "
        "scope, not scoring. RS: C03 supporting added (the policy is trained to read a library-conditioned format).",
        "2512.18552 SSR: out_of_scope confirmed independently (A3). Shared-policy RL updates weights; bug artifacts "
        "are training data; the scaffold is inherited from CWM. Informational fields follow the r09b GenEnv "
        "convention: claim_type component_training, evidence_level/claim_support null, C08 "
        "(proposer–solver co-training).",
        "2512.18746 MemEvolve (Δ1.25): final 62.5 (= son55 by item). E.measurement → son55 2. Under the run's "
        "reporting-integrity cap, the GAIA 73.33 has two provenances: App. 9.1 says GAIA systems are evolved on "
        "GAIA Level-1, Sec. 5.3/Table 3 says TaskCraft. Judge protocols are also unspecified. E.cost → son55 2 "
        "(per-task $/latency/steps reported against seven baselines; the meta-evolution cost is absent). Domain H17 "
        "is dropped: H21 already names this operation, a search over the inner learning mechanism. Shared-error "
        "correction (no score change): every TaskCraft value in Table 2 is k/300 and none fits n=180. The TaskCraft "
        "column therefore includes the 120 meta-evolution queries; both seats left this 'unclear'.",
        "Figure dependence (MemEvolve): Figure 4 was read from the page image p-09.png (sha256 " + FIG_SHA[:12] + "…; "
        "the controller-cited materials/2512.18746.pages.json does not exist, so the sha was computed here). It "
        "reports relative gains (OWL +7.1/+10.9/+11.9/+2.7 %, CK-Pro +4.2/+16.1/+4.8/+8.4 % on Web/xBench/TaskCraft/"
        "GAIA); its TaskCraft bars inherit the evolution-set overlap. No rating depends on the figure. If the "
        "controller wants cross-framework transfer to carry evidence weight, re-dispatch both seats with the page "
        "images. Recommendation, not a blocker.",
        "A4 hygiene: hidden or flagged local-ID collisions were renumbered in 2512.10398 (sol local-1/2 → local-4/5), "
        "2512.10696 (sol local-1 merged into local-3, sol local-2 → local-5), 2512.17102 (sol local-1 → local-3) and "
        "2512.18552 (sol local-1 → local-2). son55's two 'challenged_with_evidence' statuses (the paper's own claim "
        "is undercut) were corrected to unmet. son55's ReMe expectation from a card no seat matched "
        "(index_experience_for_reuse/F3) was moved to local-6.",
        "No blocking material requests. Every disputed field was answered from the pinned texts, plus the "
        "MemEvolve page image for Figure 4.",
    ]


def build_specs(g):
    R, res, conflict, opus_ev, merge_exps = g["R"], g["res"], g["conflict"], g["opus_ev"], g["merge_exps"]
    seat, prefix, MD = g["seat"], g["prefix"], g["MD"]
    S = {}
    NOSCORE = "none (patterns never score)"
    NOEXP = "none (expectations are not scored directly)"
    KEYS = ("G", "M", "X", "E.measurement", "E.causality", "E.holdout", "E.statistics", "E.cost")

    def C(p, f):
        return conflict(p, f)

    def XC(p, eid, dec, final, reason, ev=()):
        return res(f"expectations[{eid}].status", *C(p, f"expectations[{eid}].status"), dec, final, reason, ev, NOEXP)

    def RC(p, key, dec, final, reason, ev, impact):
        return res(f"ratings.{key}", *C(p, f"ratings.{key}"), dec, {"status": "resolved", "rating": final},
                   reason, ev, impact)

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

    def add_counter(claims, cid, ids):
        for c in claims:
            if c["claim_id"] == cid:
                key = "counterevidence_ids" if "counterevidence_ids" in c else "counterevidence"
                ce = c.get(key)
                c[key] = (ce if isinstance(ce, list) else ([ce] if ce else [])) + list(ids)
        return claims

    def assess(s, p, extra_unresolved=(), **upd):
        a = copy.deepcopy(seat(s, p)["assessment"])
        u = a.get("unresolved")
        a["unresolved"] = (u if isinstance(u, list) else ([u] if u else [])) + list(extra_unresolved)
        a.update(upd)
        return a

    def conv(old):
        return {"converted_from": old,
                "source_note": f"Moved from {old}: that card is not in the final pattern record (see resolutions). "
                               "The check is still a valid question about this paper's claim, so it is kept as a "
                               "paper-local expectation (A4)."}

    # =========================================================== 2512.10398 CCA (Δ13.75)
    p = "2512.10398"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "3–4 files 49.2 203", "Table 3 (edited-file buckets)",
                    "Our arithmetic on the same table: 49.2 % of 203 and 44.1 % of 86 ('5–6 files 44.1 86') are not "
                    "attainable as k/n for single runs or 3-run means. The bucket sizes 294+203+86+38+18 sum to 639, "
                    "not the 731 tasks of the public split, and the missing 92 tasks are not explained.",
                    kind="our_inference"),
            opus_ev(p, "O02", "Anthropic’s proprietary scaffold, from Claude Opus 4.5 system card",
                    "Table 1 caption footnote",
                    "The commercial rows (52.0, 56.0) are copied from system cards for proprietary scaffolds. Yet the "
                    "caption says 'All methods share identical environments', and the abstract claims superiority "
                    "over commercial results 'under identical repositories, model backends, and tool access' (opus:O03)."),
            opus_ev(p, "O03", "exceeding prior research baselines as well as commercial results, under identical "
                              "repositories, model backends, and tool access.", "Abstract",
                    "Headline claim. For the commercial comparison it is not supported by the paper's own setup."),
            opus_ev(p, "O04", "For Run 1: We execute the task from scratch (no context editing either); use note "
                              "taker agent to write down notes. For Run 2: We pass the notes from Run 1 to CCA and rerun.",
                    "§3.5", "Run 1 also disables context editing. Whether Run 2 does is not stated, so the "
                            "notes-on/notes-off contrast may be confounded with a configuration change. Both runs use "
                            "the same 151 tasks, and there is no repeated notes-off run."),
        ],
        "rs_pattern": {
            "primary": "generative_process_redesign", "supporting": ["adapt_via_conditioning"], "outside_taxonomy": False,
            "reason": "Opus sides with sol on identification, with low fit. The two parts scored as RSI are (a) a meta-agent "
                      "that rewrites the hand-designed prompts, tool wrappers and error messages of a coding scaffold "
                      "from test traces, and (b) persistent notes read back as conditioning by later sessions. Run "
                      "convention: (a) is generative_process_redesign, the card used for agent-rewritten scaffolds "
                      "(r08b Live-SWE-agent, r03b SICA, cal-dev Gödel Agent). (b) is adapt_via_conditioning, as for "
                      "every retrieved-experience memory in this run. Both subs are null: C15/C23/C24 are generative-model "
                      "tactics, and C03's canonical-schema training and category holdout are absent. son55's "
                      "outside_taxonomy is a fair reading of the SDK as a whole, but the run identifies the "
                      "self-improvement operations that are actually scored, not the surrounding engineering. "
                      "Pattern matches never score.",
            "matches": [smatch("sol", p, "generative_process_redesign", fit="low (meta-agent described generically)"),
                        smatch("sol", p, "adapt_via_conditioning", fit="low (same-instance note reuse only)")],
            "executes_pattern": "partial", "resolves_problem": False,
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "attribute_and_patch_incumbent", "H12"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H00")],
                           "unassigned": seat("son55", p)["domain_pattern"]["unassigned"],
                           "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2512.10398-1"): "local:2512.10398-4",
                    ("sol", "local:2512.10398-2"): "local:2512.10398-5"},
            overrides={
                "rsi:abstract_experience_into_guidance/S4": {
                    "status": "unmet",
                    "reason": "Opus (sides with son55). Edit/delete tools and a README index exist, but no "
                              "consolidation, conflict or forgetting policy is described, and the store is exercised "
                              "once (151 notes, one rerun). Primitives without a maintenance policy do not meet S4."},
                "rsi:abstract_experience_into_guidance/S5": {
                    "status": "partial",
                    "reason": "Opus (revised). The note-taker skips trajectories 'where no meaningful insight can be "
                              "distilled' (son55:E018): a self-judged quality filter, which S5 lists. There is no "
                              "independent or outcome-based gate, so partial, not unmet."},
                "rsi:attribute_and_patch_incumbent/S3": {
                    "status": "unmet",
                    "reason": "Opus (revised). The only retention rule is that patches 'are applied to the agent, and "
                              "the test loop is rerun' until target metrics are met (son55:E004). There is no per-edit "
                              "acceptance, rollback or protection of earlier wins. This was checked after a full read, "
                              "so unmet rather than unknown."},
                "local:2512.10398-4": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = "
                                               "same-task note reuse)."},
                "local:2512.10398-5": {"note": "sol's local-2 renumbered (A4 collision with son55's local-2 = no "
                                               "notes-off rerun control)."},
            }),
        "claims": lambda c: add_counter(add_counter(c, "C1", ["opus:O02", "opus:O03"]), "C3", ["opus:O04"]),
        "assessment": assess("son55", p,
                             ["Reported percentages inconsistent with stated denominators (Tables 2–4; opus:O01).",
                              "Run 2 configuration vs Run 1 (context editing) not stated (opus:O04)."]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The limitation is real but broad: flat histories, hand-tuned "
                   "prompts/tool wiring, context overflow. Neighbours are named (SWE-Agent, OpenHands, Agentless, "
                   "Live-SWE-Agent, Satori-SWE), but no baseline failure is measured. The residual over Live-SWE-Agent, "
                   "which already self-edits prompts/tools/config, is not stated, and automated agent-design work "
                   "(ADAS-type) is absent. sol's 3 credited a gap whose residue (sol:'remaining_gap') sol itself "
                   "left open.",
                   ["son55:E021", "son55:E022", "son55:E020", "sol:E016"]),
            "M": R("resolved", 2, "Opus sides with son55. The mechanisms can be restated (Architect compression, "
                   "asynchronous hindsight notes, a meta-agent that reads traces and patches prompts/extensions). But "
                   "the meta-agent's candidate generation and acceptance criteria, and any prediction that separates it "
                   "from manual tuning, are missing. Notes are written without outcome grounding. A concrete mechanism "
                   "with a thin causal account is anchor 2.",
                   ["son55:E003", "son55:E004", "son55:E015", "son55:E016", "sol:E005"]),
            "X": R("resolved", 1, "Opus sides with son55. For both retention paths, the condition that makes a change "
                   "persist is absent, not merely unclear. The meta-agent applies patches and reruns 'until target "
                   "metrics are met', with no per-edit accept/reject, rollback or version record. The run that produced "
                   "CCA is not described (test set, iterations, what was accepted). Notes have no admission gate beyond "
                   "a self-judged skip and no maintenance policy. The read path is only 'pass the note directory'. The "
                   "interfaces themselves (memory tree, tools) are described, which keeps X above 0.",
                   ["son55:E002", "son55:E004", "son55:E015", "sol:E002", "sol:E006"], ["son55:E018"]),
            "E.measurement": R("resolved", 2, "Shared-error correction (both seats 3). The official test-based Resolve "
                               "Rate is a credible metric. But the reported numbers fail the run's reporting-integrity "
                               "check. Table 2's 48.6 and 51.6 are not attainable on the captioned 100-example subset "
                               "(single run or 3-run mean), and §3.4.1 describes a different, outcome-filtered subset. "
                               "Table 3's 49.2/203 and 44.1/86 are unattainable, and its buckets cover 639 of 731 tasks. "
                               "Table 4's Run 2 54.4 % is not k/151 (or k/453). The commercial rows are system-card "
                               "numbers under a caption claiming identical environments. Same cap as r09b "
                               "EvoRoute/AgentDevel.",
                               ["son55:E011", "sol:E008", "opus:O01", "son55:E006", "sol:E011", "son55:E014"],
                               ["opus:O02", "son55:E010"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. Same-backbone, same-environment SWE-Agent and "
                             "Live-SWE-Agent comparisons, plus the advanced-vs-simple tool ablation (51.0 vs 44.0), give "
                             "some attribution. There is no meta-agent-vs-manual or rival-optimizer control. The "
                             "context-management subset is selected on both variants producing executable solutions. "
                             "The notes contrast is Run 1 vs Run 2 on the same tasks, with a possible configuration "
                             "difference (opus:O04).",
                             ["sol:E009", "sol:E010", "son55:E005"],
                             ["sol:E011", "son55:E012", "son55:E025", "opus:O04"]),
            "E.holdout": R("resolved", 1, "Both seats 1; re-checked. SWE-Bench-Pro/Verified are external benchmarks, "
                           "so not 0. But the meta-agent's 'production-grade test set' is not identified or separated "
                           "from the evaluation, and the notes are generated on and re-evaluated on the same 151 tasks "
                           "(Appendix F shows instance-specific fixes).",
                           ["son55:E002", "sol:E012"], ["son55:E013", "son55:E024", "sol:E005"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). The main results are three-run "
                              "means with stated sample sizes and no variance. The ablations (100/50/151 tasks) and "
                              "the +1.4 notes gain have no uncertainty, and the denominator inconsistencies (opus:O01) "
                              "leave the failure counts unclear.",
                              ["sol:E007", "son55:E011"], ["son55:E019", "opus:O01"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only the notes run reports turns/tokens (system "
                        "prompt excluded). Meta-agent iterations and cost, note-taking cost, and token parity with "
                        "baselines are absent.",
                        ["sol:E013", "sol:E014"], ["sol:E006", "son55:E023"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v6 text incl. Appendices A–H read. In scope as a mixed A/B paper: the meta-agent's "
                  "build-test-improve edits to non-weight prompts/tools and the persistent cross-session notes are "
                  "the scored RSI parts. The SDK/AX-UX-DX engineering is context. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", "task",
                "EVIDENCE rule 2: the notes are generated on and re-run on the same 151 tasks, so the selection set is "
                "the test set and evidence is at most 'task'. The tool ablation removes the meta-agent-derived stack in "
                "favour of a naive SWE-Agent-like stack. It does not compare the loop's retained change with the "
                "pre-loop state, and the loop's tuning set is unknown. No retained change is shown to cause later "
                "gains on independent tasks.",
                ["sol:E012", "son55:E013", "son55:E005", "son55:E002"], "none (evidence_level is not scored)"),
            res("rs_pattern.primary", *C(p, "rs_pattern.primary"), "sol", "generative_process_redesign",
                "See rs_pattern.reason. The scored RSI operation (an agent rewriting a scaffold's hand-designed "
                "prompts/tools from traces) follows the run convention (Live-SWE-agent, SICA). son55's outside_taxonomy "
                "describes the SDK, not the scored loop.", ["sol:E005", "sol:E006", "son55:E003"], NOSCORE),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", None], ["generative_process_redesign", None]],
                "Follows primary. adapt_via_conditioning is supporting for the notes path, sub null.",
                ["sol:E003", "sol:E004", "sol:E012"], NOSCORE),
            XC(p, "local:2512.10398-1", "son55", "unmet",
               "A4 ID collision. sol's local-1 (missing run variance, E.statistics) and son55's local-1 (notes reused "
               "on the generating tasks, E.holdout) are different questions. Final local-1 = son55's, verified "
               "(§3.5, App. F). sol's question is kept as local-4 (partial, verified).",
               ["son55:E013", "son55:E024", "sol:E007"]),
            XC(p, "local:2512.10398-2", "son55", "unmet",
               "A4 ID collision. sol's local-2 (unaccounted note/meta-search cost, E.cost) and son55's local-2 (no "
               "notes-off rerun, E.causality) are different questions. Final local-2 = son55's, verified: Run 1 vs Run 2 "
               "only, with a possible configuration change (opus:O04). sol's question is kept as local-5 (partial).",
               ["son55:E014", "opus:O04", "sol:E014"]),
            XC(p, "local:2512.10398-3", "son55", "unmet",
               "Verified: the only meta-agent evidence is the advanced-vs-naive stack ablation and one refined error "
               "message. No iteration, cost or manual-tuning control.", ["son55:E005", "son55:E007"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "unmet",
               "Card retained (supporting). Verified: there is no overlap analysis, and the notes are evaluated on "
               "their source tasks.", ["sol:E012", "sol:E017"]),
            XC(p, "rs:generative_process_redesign/RE-1", "sol", "partial",
               "Card retained (primary). Verified: removing the meta-agent-derived tools drops 51.0→44.0. But the "
               "replacement is a different naive stack, not the un-redesigned stack, so 'removing the redesign "
               "collapses the gain' is only partly shown.", ["sol:E010", "son55:E005"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "partial",
               "Verified: notes draw on compile/runtime errors (execution feedback), but no outcome signal decides what "
               "becomes a note.", ["son55:E016", "son55:E018"]),
            XC(p, "rsi:abstract_experience_into_guidance/S4", "son55", "unmet",
               "Edit/delete primitives without any consolidation or forgetting policy. The store is used once. "
               "sol's 'partial' credited the primitives.", ["son55:E015", "sol:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "revised", "partial",
               "Neither seat's value as given. sol's own domain check rated S5 partial ('meaningful insight' filter); "
               "son55 said no gate. The self-judged skip is a weak quality filter, so partial.",
               ["son55:E018", "sol:E012"]),
            XC(p, "rsi:attribute_and_patch_incumbent/F4", "son55", "unknown",
               "Verified: 'production-grade test set' / 'regression tasks (e.g., representative GitHub issues or "
               "internal tickets)'. Whether the certifying tasks are independent of the proposing model cannot be "
               "determined.", ["son55:E002", "son55:E003"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S3", "revised", "unmet",
               "The text states the rule: apply patches, rerun until target. That is not a rule protecting earlier "
               "wins, so the status is determinable (unmet), not unknown (son55) and not partial (sol).",
               ["son55:E004", "sol:E006"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S5", "son55", "partial",
               "Verified: outputs, logs and tool traces are observed; source/candidate history is not stated.",
               ["son55:E003"]),
            XC(p, "rsi:attribute_and_patch_incumbent/S6", "son55", "partial",
               "Verified: stated as an SDK-level general mechanism, demonstrated on CCA only.",
               ["son55:E002", "son55:E003"]),
            RC(p, "G", "son55", 2, "See ratings.G. The residual over Live-SWE-Agent is unstated and no baseline failure "
               "is measured.", ["son55:E020", "son55:E021"], "-3.75 vs sol (15×1/4)"),
            RC(p, "M", "son55", 2, "See ratings.M. The meta-agent's acceptance criteria and distinguishing predictions "
               "are missing. sol's 3 rests on reconstructibility, which belongs to X.",
               ["son55:E003", "son55:E004"], "-5.0 vs sol (20×1/4)"),
            RC(p, "X", "son55", 1, "See ratings.X. Retention conditions are absent for both paths, and the run that "
               "built CCA is undocumented. sol's 2 treated 'missing' as 'unclear'.",
               ["son55:E004", "son55:E015"], "-5.0 vs sol (20×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.measurement",
             "sol_value": {"status": "resolved", "rating": 3}, "son55_value": {"status": "resolved", "rating": 3},
             "correction": {"status": "resolved", "rating": 2},
             "reason": "Both seats accepted the reported numbers at face value. Arithmetic shows impossible values for "
                       "the stated denominators in Tables 2, 3 and 4. Table 3 leaves 92 of 731 tasks unaccounted for. "
                       "The commercial comparison is labelled 'identical environments' although it is copied from "
                       "system cards. Run reporting-integrity cap (r09b EvoRoute/AgentDevel).",
             "evidence_ids": ["opus:O01", "opus:O02", "son55:E006", "son55:E014", "sol:E011"],
             "score_impact": "-2.5 (10×1/4)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text (§1–5, App. A–H) before opening the seats. The "
                                                   "RSI parts are the meta-agent loop (one paragraph + App. C.1, no "
                                                   "acceptance rule or tuning set) and notes (re-run on the same 151 "
                                                   "tasks, +1.4). Tool ablation is against a naive stack; context "
                                                   "subset is outcome-filtered. k/n checks failed on Tables 2–4. "
                                                   "Initial bands G2 M2 X1 Em2 Ec2 Eh1 Es1 Ecost1; evidence_level task; "
                                                   "claim scoped.",
            "integrity_checks": "Both seats a1 on 2512.10398v6, material sha fc3c8f22…; canonical seat hashes equal "
                                "conflicts.json; namespaces/parents valid.",
            "core_claim_check": "Re-read §3.2–3.5, Tables 1–4, App. B/C/F. Recomputed every Table 2–4 percentage "
                                "against its denominator (opus:O01).",
            "rating_agreement": "5/8 identical and re-checked; E.measurement corrected 3→2 for both seats; G, M, X → "
                                "son55. The final (40.0) is below both seats by per-item ruling.",
            "expectation_renumbering": "sol local-1 → local-4, sol local-2 → local-5 (A4 collisions).",
            "retained_vs_retained_gain": "Notes persist and are read back, but only on their source tasks. Meta-agent "
                                         "edits are retained in CCA, but the loop's effect is not isolated → task.",
        },
        "figure_dependence": None,
    }

    # =========================================================== 2512.10696 ReMe (tie 65.0)
    p = "2512.10696"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "achieving average gains of 8.83% in Avg@4 and 7.29% in Pass@4.", "§1 Introduction",
                    "Table 1 gives 8B dynamic vs 8B no-memory averages of Avg@4 34.94−27.65 = 7.29 and Pass@4 "
                    "55.03−46.20 = 8.83. The introduction (here) and §4.2 (son55:E024) both swap the labels, and the "
                    "introduction attaches them to the 8B-vs-14B sentence.", kind="our_inference"),
            opus_ev(p, "O02", "This is why we select K = 5 K=5 in the main experiments.", "§4.4 Effect of Retrieved "
                    "Experience Number (Figure 5)",
                    "K is chosen from a sweep evaluated in the ReMe(fixed) setting on BFCL-V3, whose evaluation set is "
                    "the 150 held-out tasks (opus:O03). The retrieval key (usage scenario, Figure 4/Table 9) is chosen "
                    "the same way."),
            opus_ev(p, "O03", "The remaining 150 tasks serve as the evaluation set.", "§4.1 Datasets",
                    "BFCL has no separate validation split, so design sweeps on BFCL use the evaluation tasks."),
            opus_ev(p, "O04", "threshold selection follows the prior work ( Xiong et al., 2025 )", "§4.1 Implementation",
                    "The deletion thresholds come from the same prior work (Xiong et al., 2025) that §2 cites while "
                    "saying existing methods 'neglect strategic experience removal'. The removal gap is narrower "
                    "than stated."),
        ],
        "rs_pattern": {
            "primary": "adapt_via_conditioning", "supporting": [], "outside_taxonomy": False,
            "reason": "Both seats: adapt_via_conditioning (retrieved, rewritten procedural experience conditions a frozen "
                      "executor). Sub: Opus sides with sol (C03, partial fit). C03's complementary move is 'retrieving "
                      "nearest reference instances as a first-class input'. ReMe also runs a category-level transfer "
                      "test (pool from 50 base-category tasks evaluated on the Missing-Param/Missing-Func/Long-Context "
                      "categories, Table 8). That differs from the r09b MemRL case, where no category holdout existed. "
                      "The canonical-schema training branch is absent.",
            "matches": [smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "abstract_experience_into_guidance", "H00"),
                                       dmatch("son55", p, "abstract_experience_into_guidance", "H01"),
                                       dmatch("son55", p, "evidence_gated_retention", "H29")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0, rs_sub="C03"), pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2512.10696-1"): "local:2512.10696-3",
                    ("sol", "local:2512.10696-2"): "local:2512.10696-5",
                    ("son55", "rsi:index_experience_for_reuse/F3"): "local:2512.10696-6"},
            overrides={
                "local:2512.10696-3": {
                    "status": "unmet",
                    "reason": "Opus. Merged: sol's local-1 and son55's local-3 ask the same question (does the "
                              "memory-scaling headline hold?). Averaged over the two benchmarks, 8B+ReMe(dynamic) vs "
                              "14B no-memory is Pass@4 55.03 vs 54.65 (+0.38, below the per-benchmark std) and Avg@4 "
                              "34.94 vs 35.62 (−0.68). On BFCL both metrics are lower. The gains are also mislabelled "
                              "(opus:O01). son55's 'challenged_with_evidence' is for a paper rebutting an expectation, "
                              "so it is corrected; the abstract's unqualified claim is unmet.",
                    "evidence_ids": ["son55:E001", "son55:E003", "son55:E004", "son55:E024", "opus:O01", "sol:E008"]},
                "rs:adapt_via_conditioning/RE-1": {
                    "status": "met",
                    "reason": "Opus (sides with son55). No Memory vs ReMe(fixed) with the same executor and prompt "
                              "protocol is exactly the conditioning toggle, across three model sizes and two "
                              "benchmarks. sol's retry/compute concern is a budget question (E.causality/E.cost), not "
                              "RE-1."},
                "local:2512.10696-5": {"note": "sol's local-2 renumbered (A4 collision with son55's local-2 = "
                                               "dynamic-stream order/trial sharing)."},
                "local:2512.10696-6": dict(conv("rsi:index_experience_for_reuse/F3")),
            }),
        "claims": lambda c: add_counter(add_counter(c, "C2", ["opus:O01"]), "C1", ["opus:O02"]),
        "assessment": assess("son55", p,
                             ["K=5 and retrieval key selected on the BFCL evaluation set (opus:O02)."],
                             cannot_say=seat("son55", p)["assessment"]["cannot_say"]
                             + ["the reported 7.29/8.83 labels (swapped; opus:O01)"]),
        "ratings": {
            "G": R("resolved", 2, "Opus sides with son55. The granularity and stale-pool limitations are concrete, and "
                   "Synapse/HiAgent/AWM/Agent KB/CER/A-Mem/LangMem are named. But the central framing, that existing "
                   "methods 'neglect strategic experience removal', is contradicted by the paper's own reliance on "
                   "prior deletion work for its thresholds (opus:O04). Close procedural-memory neighbours with "
                   "maintenance (e.g. ExpeL insight edits) are not discussed, so the residual is not bounded.",
                   ["son55:E028", "son55:E029", "son55:E030", "sol:E001"], ["opus:O04"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Multi-faceted distillation → judge/dedup → "
                   "scenario-indexed retrieval with rerank/rewrite → success-gated add, reflection and utility deletion "
                   "is aligned with the stated problem, with distinguishable predictions against trajectory-level and "
                   "full-addition alternatives. Not 4: recall-success utility is not marginal credit (co-retrieved "
                   "entries).",
                   ["son55:E012", "son55:E014", "son55:E015", "son55:E018", "sol:E006"], ["sol:E014"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. N=8, success threshold 1.0, judge 0.3, dedup, top-5, ≤3 "
                   "reflections, α=5/β=0.5, retrieve-once read path. Not 4: dedup threshold, pool size and deletion "
                   "counts, conflict/rollback and dynamic-stream ordering are unreported.",
                   ["son55:E013", "son55:E014", "son55:E015", "son55:E032", "sol:E005"], ["son55:E023"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. The BFCL-V3 AST/executable checks and "
                               "AppWorld state-based unit tests are credible verifiers, with Avg@4 and Pass@4 both "
                               "reported. The tables are internally consistent (BFCL Pass@4 values are k/450, and Table "
                               "3/5 rows match Table 1). The swapped gain labels and the overstated headline are "
                               "narrative errors handled in claim support and expectation local-3, not metric failures "
                               "(A2). One AppWorld Pass@4 value (32.85) does not fit k/504; this is isolated and not "
                               "load-bearing.",
                               ["son55:E031", "sol:E010", "sol:E008"], ["opus:O01"]),
            "E.causality": R("resolved", 2, "Opus sides with sol. The store toggle (No Memory vs ReMe-fixed) and the "
                             "granularity ablation are informative. But ReMe's pool construction (N=8 sampling, "
                             "summarizer, judge) and dynamic reflection retries (≤3) and rerank/rewrite calls are not "
                             "matched for the baselines (A2: budget mismatch → causality and cost). The component "
                             "ablations are single-model, single-benchmark, without std, and the deletion effect "
                             "(+0.17 Avg@4) is within noise. Dynamic-vs-fixed also adds test-stream success feedback, "
                             "an alternative explanation the paper never tests.",
                             ["son55:E002", "son55:E005", "son55:E018", "son55:E017", "sol:E011"],
                             ["son55:E016", "son55:E013", "sol:E005", "sol:E006"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked, with a shared omission added. The fixed pool is "
                           "built from disjoint training tasks (BFCL 50/150, AppWorld official), with a category "
                           "transfer in Table 8. The headline dynamic variant updates on the evaluation stream using "
                           "success feedback. Neither seat noted that K=5 and the usage-scenario key were chosen on the "
                           "150-task evaluation set (opus:O02/O03). The margins between alternatives are small (Table 9), "
                           "so the band stays 2.",
                           ["son55:E009", "son55:E025", "sol:E007"], ["son55:E011", "opus:O02", "opus:O03"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked (A2 ladder). The main table has three-run "
                              "mean±std. The ablations have none, there are no significance tests, and the 0.38 Pass@4 "
                              "margin is below the std.",
                              ["son55:E031", "sol:E013"], ["son55:E016", "son55:E024"]),
            "E.cost": R("resolved", 1, "Both seats 1; re-checked. Only AppWorld inference latency (+2.54 s) is reported. "
                        "There is no construction, judge, rerank/rewrite or reflection cost, and no compute-matched "
                        "model-scale frontier for the 'computation-efficient path' claim.",
                        ["son55:E021", "sol:E012"], ["son55:E013", "sol:E005"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. appendices and prompt tables read. In scope (system_method, A class): "
                  "a persistent procedural-experience pool written back from execution outcomes and read by later "
                  "tasks. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol", [["adapt_via_conditioning", "C03"]],
                "See rs_pattern.reason. C03's retrieval-substrate move plus a real category-transfer test (Table 8) "
                "justify the sub. son55's null is defensible only on the schema-training branch.",
                ["sol:E003", "son55:E025"], NOSCORE),
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "son55",
                [["abstract_experience_into_guidance", "H00"], ["abstract_experience_into_guidance", "H01"],
                 ["evidence_gated_retention", "H29"]],
                "H00 added (son55): ReMe's acquisition step contrasts successful and failed trajectories into "
                "abstracted lessons with trigger conditions ('when_to_use'), the H00 tactic. H01 (add/dedup/delete "
                "maintenance) and H29 (recall-success utility) are kept by both seats. This follows ArcMemo, EvolveR "
                "and TF-GRPO in this run.", ["son55:E012", "son55:E032", "sol:E002"], NOSCORE),
            XC(p, "local:2512.10696-1", "son55", "unknown",
               "A4 ID collision. sol's local-1 (memory-scaling headline) is merged into local-3. Final local-1 = son55's "
               "(pool size/deletion counts), verified as not reported. The underlying fact, whether deletion fires, is "
               "unknown, so the status stays unknown.", ["son55:E015", "son55:E016", "sol:E008"]),
            XC(p, "local:2512.10696-2", "son55", "unknown",
               "A4 ID collision. sol's local-2 (statistics) is renumbered local-5. Final local-2 = son55's (dynamic-stream "
               "order and whether the four trials share an evolving pool), verified as undescribed.",
               ["son55:E011", "sol:E013"]),
            XC(p, "local:2512.10696-3", "revised", "unmet",
               "Merged with sol's local-1 (same question). The table supports the claim on one averaged metric only, by "
               "less than the std, and not on BFCL. sol's 'partial' is too lenient for an unqualified abstract claim. "
               "son55's 'challenged_with_evidence' is the wrong status type.",
               ["son55:E003", "son55:E004", "son55:E001", "opus:O01"]),
            XC(p, "local:2512.10696-4", "son55", "unknown",
               "Verified: whether reflection retries and extra calls count toward Avg@4/Pass@4 or a budget is not "
               "stated.", ["son55:E013", "son55:E010"]),
            XC(p, "rs:adapt_via_conditioning/RE-1", "son55", "met",
               "The memory on/off toggle with the same executor is RE-1's requested ablation. Budget is a separate "
               "item.", ["son55:E002", "son55:E005"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
               "There is no overlap analysis, but the splits are disjoint by construction (BFCL random, AppWorld "
               "official). Some design choices were tuned on the BFCL evaluation set (opus:O02). That is partial: "
               "something is known, so not unknown.", ["sol:E007", "opus:O02", "son55:E008"]),
            XC(p, "rs:adapt_via_conditioning/RE-3", "son55", "partial",
               "Verified: trajectory-level, A-Mem and LangMem are compared; there is no longer-context or equal-budget "
               "control.", ["son55:E018", "son55:E006"]),
            XC(p, "rs:adapt_via_conditioning/RE-4", "son55", "partial",
               "Verified: most modules are ablated on 8B/BFCL without std; dedup and the judge are not.",
               ["son55:E016", "son55:E017", "son55:E019"]),
            XC(p, "rs:adapt_via_conditioning/RE-5", "son55", "partial",
               "Verified: two benchmarks, three Qwen sizes, six extra LLMs on BFCL only.", ["son55:E033", "son55:E025"]),
            XC(p, "rs:adapt_via_conditioning/RE-6", "son55", "met",
               "Verified: summarizer-capability, K, retrieval-key and cross-category pool sensitivity are all reported.",
               ["son55:E020", "son55:E034", "son55:E025"]),
            XC(p, "rsi:abstract_experience_into_guidance/S2", "son55", "partial",
               "Verified: comparative insights exist (best/worst pairs); their separate contribution is not ablated.",
               ["son55:E012", "sol:E002"]),
            XC(p, "rsi:abstract_experience_into_guidance/S3", "son55", "met",
               "Verified: benchmark reward thresholds decide success/failure trajectories; judge limits acknowledged.",
               ["son55:E032", "son55:E022"]),
            XC(p, "rsi:abstract_experience_into_guidance/S5", "son55", "partial",
               "Verified: judge, dedup and success-only addition gate entries; no execution replay of an entry.",
               ["son55:E012", "son55:E032"]),
            XC(p, "rsi:evidence_gated_retention/S4", "son55", "met",
               "Verified: Table 3 toggles selective addition, reflection and deletion separately.",
               ["son55:E016", "son55:E017"]),
            XC(p, "rsi:evidence_gated_retention/S5", "son55", "partial",
               "Verified: latency only; judge/rerank/rewrite/reflection calls are not costed.",
               ["son55:E021", "son55:E013"]),
            XC(p, "rsi:index_experience_for_reuse/F3", "revised", {"moved_to": "local:2512.10696-6", "status": "partial"},
               "No seat matched index_experience_for_reuse. The check (dynamic pool built from the test stream) is "
               "valid and is kept as local-6, partial: true for ReMe(dynamic), false for ReMe(fixed).",
               ["son55:E011", "son55:E009"]),
            RC(p, "G", "son55", 2, "See ratings.G. The removal-gap framing is overstated (opus:O04) and the residual "
               "is unbounded.", ["son55:E030", "opus:O04"], "-3.75 vs sol (15×1/4)"),
            RC(p, "E.causality", "sol", 2, "See ratings.E.causality. The pool-construction and reflection budgets "
               "are unmatched and the ablations are single-config without std. The dynamic gains mix in test-stream "
               "feedback.", ["son55:E013", "sol:E005", "son55:E016"], "-3.75 vs son55 (15×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.counterevidence_ids",
             "sol_value": "not noted", "son55_value": "not noted",
             "correction": "added opus:O02, opus:O03",
             "reason": "Both seats missed that K=5 (Figure 5 sweep) and the usage-scenario retrieval key (Figure 4/Table "
                       "9) were selected on the BFCL evaluation set. This is selection-on-test for two design choices. "
                       "Band unchanged at 2: the margins are small and the fixed pool's train/test separation stands.",
             "evidence_ids": ["opus:O02", "opus:O03"], "score_impact": "none (E.holdout stays 2)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats. The fixed pool from "
                                                   "disjoint training tasks beats no-memory across 3 sizes × 2 "
                                                   "benchmarks; dynamic adds test-stream success updates and ≤3 "
                                                   "reflections. Recomputed Table 1: 8B dynamic vs 14B none fails on "
                                                   "Avg@4, gain labels swapped. K/key chosen on the eval set; deletion "
                                                   "thresholds borrowed. Initial bands G2 M3 X3 Em3 Ec2 Eh2 Es2 "
                                                   "Ecost1; evidence_level retained; claim scoped.",
            "integrity_checks": "Both seats a1 on 2512.10696v2, material sha 2acae485…; canonical seat hashes equal "
                                "conflicts.json; namespaces/parents valid.",
            "core_claim_check": "Shared 65.0 not accepted as-is. Each item was re-derived: G and E.causality move down "
                                "(final 61.25), one shared omission was added, and son55's headline/label finding was "
                                "confirmed by recomputation (sol missed the label swap).",
            "rating_agreement": "6/8 identical and re-checked; G → son55, E.causality → sol.",
            "expectation_renumbering": "sol local-1 merged into local-3; sol local-2 → local-5; son55 "
                                       "index_experience_for_reuse/F3 → local-6 (card not matched).",
            "retained_vs_retained_gain": "The fixed pool persists from training tasks and improves disjoint test "
                                         "tasks against a store-off control → retained. The dynamic gains are not "
                                         "certified on a sealed stream.",
        },
        "figure_dependence": None,
    }

    # =========================================================== 2512.17102 SAGE (Δ2.5)
    p = "2512.17102"
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "we finally obtained 384 rollouts for each step.", "App. G Rollout Settings",
                    "SAGE uses 384 rollouts/step vs GRPO's 288 (son55:E024), and sequential rollouts roughly double the "
                    "per-rollout time. SAGE's checkpoint is step 75 (opus:O02); GRPO's step count is not given."),
            opus_ev(p, "O02", "Thus, we selected the model checkpoint at step 75 as our final agent model.",
                    "App. G Training Details", "Checkpoint selection uses Dev only (son55:E020)."),
            opus_ev(p, "O03", "Some tasks within the same scenario even use identical query under different simulated users.",
                    "App. I.2", "The retained library is reused on near-duplicate queries within one scenario, which "
                                "bounds what 'skill transfer' can mean here."),
            opus_ev(p, "O04", "For simplicity, we employed an advanced model, specifically Claude 3.5 Sonnet V2, as the "
                              "expert to produce high-quality trajectories within the skill library agent.",
                    "§4.1 SAGE", "Extra expert data is part of SAGE's pipeline and is not in the GRPO baseline; the "
                                 "SFT-initialised GRPO control (son55:E018) addresses it partly."),
        ],
        "rs_pattern": {
            "primary": "self_supervised_signal_engineering", "supporting": ["adapt_via_conditioning"],
            "outside_taxonomy": False,
            "reason": "Both seats: primary self_supervised_signal_engineering/C26, an engineered skill-use reward that "
                      "credits generation through downstream use. Opus adds sol's supporting adapt_via_conditioning/C03. "
                      "SFT then RL explicitly train the policy to parse a library-conditioned format (C03's 'upstream "
                      "phase teaches the model to read the schema'). At deployment, new scenarios are absorbed through "
                      "the library without weight updates, and Test-Challenge holds out unseen apps. Fit partial.",
            "matches": [smatch("sol", p, "self_supervised_signal_engineering"),
                        smatch("sol", p, "adapt_via_conditioning")],
            "executes_pattern": "partial", "resolves_problem": "partial",
        },
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "amortize_improver_into_trained_policy", "H26"),
                                       dmatch("son55", p, "couple_context_and_weight_updates", "H28"),
                                       dmatch("son55", p, "crystallize_executable_capability", "H07")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("sol", p, 0), pmap("sol", p, 1)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2512.17102-1"): "local:2512.17102-3"},
            overrides={
                "local:2512.17102-2": {
                    "status": "partial",
                    "note": "sol's and son55's local-2 are the same statistics question (merged).",
                    "reason": "Opus (sides with sol). Three evaluation runs with std are reported for every table, "
                              "so not unmet. There are no training seeds or significance tests, so not met. The "
                              "rollout-count difference son55 bundled in is a cost/causality matter (A2)."},
                "local:2512.17102-3": {"note": "sol's local-1 renumbered (hidden A4 collision with son55's local-1 = "
                                               "privileged scenario labels)."},
            }),
        "claims": lambda c: c,
        "assessment": assess("son55", p, ["Retained library spans one 3-task scenario of near-duplicate queries "
                                          "(opus:O03)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The bottleneck has a source and is confirmed by the paper's "
                   "own data: prompt-based skill libraries depend on instruction following (Skill Library Agent 30.7 "
                   "TGC < ReAct 39.2). Voyager/AWM/ASI/DynaSaur and LOOP are compared. Not 4: contemporaneous "
                   "RL-trained memory/skill curators are not discussed.",
                   ["son55:E025", "son55:E026", "son55:E005", "sol:E002"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. Sequential two-task chains with a reward that credits "
                   "skill generation through later successful use target the delayed-credit problem, with "
                   "distinguishable predictions against outcome-only and chain-only rewards (Table 4). Not 4: the "
                   "usage indicator is not marginal utility, and an error-free save is not semantic validity.",
                   ["son55:E010", "son55:E013", "sol:E004"], ["son55:E031"]),
            "X": R("resolved", 3, "Opus sides with sol. Both chains can be rebuilt from the text. Training: chain "
                   "construction, reward formula, rollouts, lr, Dev selection at step 75. Deployment: retrieve → "
                   "use/generate/update → save only if it executes without error. The same-scenario assumption is "
                   "stated, and the label-free retrieval alternatives are specified. Not 4: no retirement, versioning "
                   "or conflict handling, and admission is execution-without-error only. son55's points (test labels, "
                   "near-duplicate scope) are evidence-scope issues, charged to E.holdout.",
                   ["sol:E003", "sol:E016", "sol:E017", "son55:E012", "son55:E010"], ["son55:E030"]),
            "E.measurement": R("resolved", 3, "Both seats 3; re-checked. AppWorld's state-based programmatic checks "
                               "give TGC/SGC, plus steps/tokens. Headline arithmetic verified (8.9 SGC, 26 % steps, 59 % "
                               "tokens), and SGC values are k/168. One ablation value (RL warm-up SGC 55.3) does not fit "
                               "k/168; this is isolated and not load-bearing.",
                               ["son55:E022", "son55:E001", "sol:E007"], ["son55:E011"]),
            "E.causality": R("resolved", 3, "Opus sides with son55. Four controls isolate SAGE's components, each with "
                             "three-run std: the same-weights library toggle (SGC 60.7 vs 54.8, steps 12.1 vs 16.0), the "
                             "reward ablation at identical chain budget (60.7 vs 55.4/56.6), initialisation variants, "
                             "and SFT-initialised GRPO (51.2 SGC), which separates expert data from the method. Not 4: "
                             "the headline vs GRPO is not compute-matched (384 vs 288 rollouts, unknown GRPO steps, "
                             "Claude SFT data; opus:O01/O04), there is one training seed, and the TGC gain over GRPO is "
                             "within std.",
                             ["son55:E007", "son55:E013", "son55:E018", "son55:E016", "sol:E012"],
                             ["opus:O01", "opus:O04", "son55:E024", "son55:E006"]),
            "E.holdout": R("resolved", 3, "Opus sides with son55. The official Train/Dev/Test split is respected, the "
                           "checkpoint is chosen on Dev only, and Test-Challenge needs apps absent from training. The "
                           "default same-scenario retrieval uses test labels, but label-free Query N-gram reaches "
                           "72.0/60.1, so the privilege is not load-bearing. The test-time save gate uses no reward. "
                           "Not 4: AppWorld only, and reuse is within near-duplicate scenarios (opus:O03), which "
                           "bounds the 'new environments' claim.",
                           ["son55:E020", "son55:E021", "son55:E016", "opus:O02"],
                           ["son55:E015", "son55:E028", "opus:O03"]),
            "E.statistics": R("resolved", 2, "Both seats 2; re-checked (A2 ladder). Every table has three evaluation "
                              "runs with std, and the key SGC gaps exceed the std. There is a single training run and "
                              "no significance tests.",
                              ["son55:E022", "sol:E007"], ["sol:E013"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Inference steps/tokens are reported for every method, "
                        "along with training hardware, rollouts/step, batch sizes and the selected step. The "
                        "efficiency claim is about inference. Missing: total GPU-hours, the cost of generating Claude "
                        "expert data, and the GRPO step count, so the training budget is partly disclosed but not "
                        "matched.",
                        ["son55:E001", "son55:E023", "opus:O01", "sol:E022"], ["son55:E024", "son55:E032"]),
        },
        "status": "reviewed",
        "reason": "Complete pinned v2 text incl. Appendices A–L read. In scope under rubric A3 (second bullet): the "
                  "improver is weight-trained, but the evaluated retained object is the non-weight executable skill "
                  "library (component_training). All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree under A3 second bullet)",
        "resolutions": [
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "sol",
                [["adapt_via_conditioning", "C03"], ["self_supervised_signal_engineering", "C26"]],
                "See rs_pattern.reason. The policy is explicitly trained to read a library-conditioned format, and the "
                "C03 holdout element (Test-Challenge unseen apps) exists.", ["sol:E003", "sol:E014", "son55:E021"],
                NOSCORE),
            XC(p, "local:2512.17102-2", "sol", "partial",
               "Same question in both seats (statistics). Evaluation std exists, training seeds do not → partial.",
               ["son55:E022", "sol:E007"]),
            XC(p, "rs:adapt_via_conditioning/RE-2", "sol", "partial",
               "Card retained (supporting). Verified: official splits and unseen-API Challenge; no explicit overlap "
               "analysis.", ["sol:E005", "sol:E014"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-1", "son55", "unmet",
               "Verified: one model (Qwen2.5-32B), one benchmark.", ["son55:E028"]),
            XC(p, "rs:self_supervised_signal_engineering/RE-6", "son55", "partial",
               "Verified: test-set scenario labels by default; label-free retrieval nearly recovers.",
               ["son55:E015", "son55:E016"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/F4", "son55", "met",
               "Failure avoided (met): the writer and reader are the same policy in one chain, not an isolated writer "
               "on a proxy reward.", ["son55:E010", "son55:E013"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/H26", "sol", "partial",
               "Verified: delayed use credit and the store toggle are implemented; frozen-store transfer beyond the "
               "scenario is not shown.", ["sol:E004", "sol:E010"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S1", "son55", "partial",
               "Verified: the usage bonus rewards success-with-use, not improvement relative to a pre-edit state.",
               ["son55:E010", "son55:E013"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S2", "son55", "met",
               "Verified: R1 credits generation only when q2 uses the skill and succeeds.", ["son55:E010"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S3", "son55", "met",
               "Verified: the same policy writes and reads.", ["son55:E010"]),
            XC(p, "rsi:amortize_improver_into_trained_policy/S5", "son55", "unmet",
               "Verified: a single benchmark family.", ["son55:E028"]),
            XC(p, "rsi:couple_context_and_weight_updates/S1", "son55", "partial",
               "Verified: shared rollouts train weights and populate the library; context candidates are not ranked.",
               ["son55:E010"]),
            XC(p, "rsi:crystallize_executable_capability/S1", "son55", "partial",
               "Verified: admission = executes without error; no replay or invocation check.", ["son55:E012"]),
            XC(p, "rsi:crystallize_executable_capability/S3", "sol", "partial",
               "Verified: no per-skill check beyond the source task; only aggregate later-task evidence.",
               ["sol:E003", "sol:E010"]),
            XC(p, "rsi:crystallize_executable_capability/S5", "son55", "met",
               "Verified: skills on/off at every stage (SAGE SGC +5.9).", ["son55:E007", "son55:E008"]),
            RC(p, "X", "sol", 3, "See ratings.X. The training and deployment chains are fully specified and the "
               "boundary is stated. son55's deductions are scope/evidence issues charged to E.holdout.",
               ["sol:E003", "sol:E016", "son55:E012"], "+5.0 vs son55 (20×1/4)"),
            RC(p, "E.causality", "son55", 3, "See ratings.E.causality. The components are isolated at matched budget "
               "with std. The GRPO compute gap limits only the headline comparison.",
               ["son55:E007", "son55:E013", "son55:E018"], "+3.75 vs sol (15×1/4)"),
            RC(p, "E.holdout", "son55", 3, "See ratings.E.holdout. Dev-only selection, an unseen-app split, and the "
               "privileged label shown non-load-bearing.", ["son55:E020", "son55:E021", "son55:E016"],
               "+2.5 vs sol (10×1/4)"),
            RC(p, "E.cost", "son55", 2, "See ratings.E.cost. Inference cost is complete and training cost partly "
               "disclosed. sol's 1 undercounts the disclosed rollout/hardware/step information.",
               ["son55:E023", "opus:O01"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "expectations[local:2512.17102-1]",
             "sol_value": "local-1 = token-efficiency claim vs SFT-initialised GRPO (E.cost), partial",
             "son55_value": "local-1 = privileged scenario labels at test (E.holdout), partial",
             "correction": "Hidden A4 collision (equal status, so not flagged by conflicts.json). Final local-1 = son55's; "
                           "sol's is renumbered local-3.",
             "evidence_ids": ["son55:E015", "son55:E016", "sol:E021"], "score_impact": NOEXP},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats. GRPO-trained "
                                                   "skill-library agent; the deployment library is non-weight (A3 in "
                                                   "scope). Same-weights library toggle +5.9 SGC / +0.6 TGC; reward "
                                                   "ablation at matched chain budget; SFT-GRPO control; Dev selection; "
                                                   "Test-Challenge; label-free retrieval ≈ oracle; 384 vs 288 rollouts; "
                                                   "near-duplicate scenarios. Initial bands G3 M3 X3 Em3 Ec2–3 Eh3 Es2 "
                                                   "Ecost2; evidence_level retained; claim scoped.",
            "integrity_checks": "Both seats a1 on 2512.17102v2, material sha dd13f079…; canonical seat hashes equal "
                                "conflicts.json; namespaces/parents valid.",
            "core_claim_check": "Re-read §3–4, Tables 1–7, App. E–L. Verified the abstract's percentages and SGC k/168.",
            "rating_agreement": "4/8 identical and re-checked; X → sol; E.causality, E.holdout, E.cost → son55. The "
                                "final (72.5) is above both seats by per-item ruling: each seat was one band harsher on "
                                "different items, for reasons that belong to other items.",
            "expectation_renumbering": "sol local-1 → local-3 (hidden collision); local-2 merged.",
            "retained_vs_retained_gain": "The same weights with vs without the accumulated library on held-out test "
                                         "scenarios → retained (within-scenario only).",
        },
        "figure_dependence": None,
    }

    # =========================================================== 2512.18552 SSR (both out_of_scope)
    p = "2512.18552"
    a3 = ("out_of_scope (rubric A3; EVIDENCE.md excludes weight-updating self-improvement). Independently checked: a "
          "single policy plays bug-injector and solver, and its shared weights are updated by RL on both signals "
          "(son55:E002, son55:E003). Bug artifacts (patches, test scripts, parsers) are training curriculum. The tool "
          "scaffold is CWM's with minor prompt changes (son55:E006). No non-weight harness component is retained and "
          "evaluated. Not scored; null is not a zero-quality rating.")
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "opus_evidence": [
            opus_ev(p, "O01", "Both roles share parameters and are trained jointly with RL.", "§1",
                    "The evaluated product is the jointly RL-trained weight set."),
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55"),
        "domain_pattern": prefix(copy.deepcopy(seat("son55", p)["domain_pattern"]), "son55"),
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son,
            rename={("sol", "local:2512.18552-1"): "local:2512.18552-2"},
            overrides={"local:2512.18552-2": {"note": "sol's local-1 renumbered (A4 collision with son55's local-1 = "
                                                      "retained non-weight component)."}}),
        "claims": lambda c: c,
        "assessment": {"evidence_level": None,
                       "evidence_level_note": "No harness evidence label for an out-of-scope weight-level paper (run "
                                              "precedent r05b–r09b).",
                       "claim_support": None,
                       "claim_support_note": "Not assessed under this rubric; SWE-bench gains are author-reported "
                                             "results of RL-trained checkpoints.",
                       "strongest_supported_claim": None,
                       "unresolved": ["Out-of-scope disposition is not a judgment that the RL results are wrong."]},
        "ratings": {k: R("unknown", None, a3) for k in KEYS},
        "status": "out_of_scope", "reason": a3,
        "aggregate_status": "accepted_final",
        "a3": "none (both seats out_of_scope; confirmed independently)",
        "resolutions": [
            res("paper.claim_type", *C(p, "paper.claim_type"), "son55", "component_training",
                "Informational: the evaluated product is a trained agent model (r09b GenEnv convention). sol's "
                "system_method fits the self-play loop as a procedure, but no harness system is retained.",
                ["son55:E003", "opus:O01"], "none (out_of_scope row; claim_type is identification only)"),
            res("assessment.evidence_level", *C(p, "assessment.evidence_level"), "son55", None,
                "Null is canonical for out-of-scope rows (r05b–r09b). The task/retained/improver ladder does not apply "
                "to weight-level work.", ["son55:E003"], "none (evidence_level is not scored)"),
            res("assessment.claim_support", *C(p, "assessment.claim_support"), "son55", None,
                "Null is canonical for out-of-scope rows; claim support is not assessed under this rubric.",
                ["son55:E003"], "none"),
            res("rs_pattern.matches", *C(p, "rs_pattern.matches"), "son55", [["self_supervised_signal_engineering", "C08"]],
                "Informational. The run convention for proposer–solver co-training is C08 (r05b R-Zero, r07a SPELL, r08b "
                "Agent0, r09b GenEnv): a generator steered by solver feedback, execution-gated, retrained. sol's C26 "
                "(preference/scalar reward manufacture) describes the solver's binary test reward, which is not the "
                "distinctive operation.", ["son55:E005", "son55:E009", "son55:E011"], NOSCORE),
            XC(p, "local:2512.18552-1", "son55", "unmet",
               "A4 ID collision. sol's local-1 (is the scope basis directly evidenced? met) and son55's local-1 (is any "
               "non-weight component retained? unmet) are different questions. Final local-1 = son55's, verified. "
               "sol's question is kept as local-2 (met). Informational.", ["son55:E003", "son55:E006", "sol:E002"]),
            XC(p, "rsi:self_generate_the_curriculum/S1", "son55", "met",
               "Informational. The oracle test files are reset to the original repository versions before every "
               "check. Seven execution consistency checks (incl. inverse mutation testing) gate each artifact. The "
               "generator cannot redefine the oracle tests. sol's 'parser authored by the policy' concern is real but "
               "covered by the parser-validity check.", ["son55:E005", "sol:E005"]),
            XC(p, "rsi:self_generate_the_curriculum/S2", "son55", "partial",
               "Informational. The solve-rate band is measured on the solver's own attempts, not a fixed validation "
               "environment, and its reward contribution is negligible.", ["son55:E009"]),
            XC(p, "rsi:self_generate_the_curriculum/S6", "son55", "met",
               "Informational. SWE-bench Verified/Pro against human-data RL and repair-only (static-bug) baselines; "
               "evaluation noise is acknowledged.", ["son55:E007", "son55:E008"]),
        ],
        "shared_error_corrections": [],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read §1–3 and App. C before opening the seats. Shared-weight "
                                                   "injector/solver RL on CWM-sft, CWM scaffold, bug artifacts as "
                                                   "curriculum → out_of_scope (A3).",
            "integrity_checks": "Both seats a1 on 2512.18552v3, material sha a1a36dbf…; canonical seat hashes equal "
                                "conflicts.json; both out_of_scope independently.",
            "core_claim_check": "A3 basis confirmed with opus:O01, son55:E003 and son55:E006.",
            "rating_agreement": "All eight unknown in both seats; kept.",
        },
        "figure_dependence": None,
    }

    # =========================================================== 2512.18746 MemEvolve (Δ1.25)
    p = "2512.18746"
    fig = {"evidence_id": "opus:F01", "material_id": "2512.18746.pages/p-09.png", "material_hash": FIG_SHA,
           "sha256": FIG_SHA, "locator": "Figure 4 (page image p-09.png, PDF p. 9)",
           "quote": "The cross-framework generalization analysis.",
           "support_explanation": "Read from the page image. Bars give pass@1 before/after transferring the "
                                  "TaskCraft-evolved memory to OWL-Workforce (+7.1/+10.9/+11.9/+2.7 % relative on "
                                  "Web/xBench/TaskCraft/GAIA) and CK-Pro (+4.2/+16.1/+4.8/+8.4 %). The TaskCraft bars "
                                  "include the evolution queries (opus:O01). Baseline-bar provenance cannot be fully "
                                  "confirmed from the image. Not used as the basis of any rating.",
           "kind": "author_report"}
    S[p] = {
        "base": "son55",
        "paper_update": {"paper_id": p},
        "extra_materials": [{"material_id": "2512.18746.pages/p-09.png",
                             "url": "local render of arXiv 2512.18746v1 PDF page 9", "version": "2512.18746v1",
                             "sha256": FIG_SHA, "local_path": FIG_PATH,
                             "sections_read": ["Figure 4 and Table 3 as rendered"], "complete": True,
                             "missing_sections": [],
                             "note": "The controller cited materials/2512.18746.pages.json for page hashes. That "
                                     "file does not exist; sha256 was computed by Opus. Only p-09 was used."}],
        "opus_evidence": [
            opus_ev(p, "O01", "We collect 300 queries as a working subset and use 120 of them for three rounds of "
                              "meta-evolution, with 40 queries per round.", "App. 9.1 TaskCraft",
                    "Our arithmetic: every TaskCraft value in Table 2 (e.g. 69.67, 72.00, 67.67, 64.00, 58.00, 75.33) "
                    "is an exact k/300 and none fits n=180. The TaskCraft evaluation therefore covers all 300 queries, "
                    "including the 120 used for meta-evolution.", kind="our_inference"),
            fig,
        ],
        "rs_pattern": prefix(copy.deepcopy(seat("son55", p)["rs_pattern"]), "son55"),
        "domain_pattern": {"namespace": "rsi",
                           "matches": [dmatch("son55", p, "make_the_improver_editable", "H21")],
                           "unassigned": [], "revision_proposals": []},
        "pattern_mapping": [pmap("son55", p, 0)],
        "expectations": lambda sol, son: merge_exps(
            p, sol, son, rename={},
            overrides={
                "rsi:make_the_improver_editable/S4": {
                    "status": "unmet",
                    "reason": "Opus (sides with son55). S4 asks for the search cost. Only per-task deployment "
                              "cost/latency is reported; the meta-evolution cost (rounds × candidates × 60 "
                              "trajectories + diagnose/design calls) is absent. Deployment cost is credited under "
                              "E.cost, not S4."},
                "local:2512.18746-2": {
                    "status": "unmet",
                    "reason": "Opus (status corrected from 'challenged_with_evidence', which is for a paper rebutting "
                              "an expectation). App. 9.1 says GAIA systems are evolved on GAIA Level-1 + 67 TaskCraft "
                              "queries, while Sec. 5.3 says the Table 3 numbers come from the TaskCraft-evolved system. "
                              "The same 73.33 appears in both tables. Either the GAIA number is contaminated by "
                              "Level-1 selection, or its provenance is misreported. Unmet."},
                "rs:generative_process_redesign/RE-5": {
                    "status": "partial",
                    "reason": "Opus (revised from unknown). Deployment-compute confounding is addressed: per-task API "
                              "cost is at parity with no-memory, and the backbone is the same. The one-time evolution "
                              "compute is not reported. Part of the expectation is answered, so partial."},
            }),
        "claims": lambda c: add_counter(c, "C1", ["opus:O01"]),
        "assessment": assess("son55", p, ["TaskCraft evaluation includes the 120 evolution queries (opus:O01)."]),
        "ratings": {
            "G": R("resolved", 3, "Both seats 3; re-checked. The bottleneck (a fixed memory architecture across task "
                   "families) is concrete and shown by the paper's own Table 3: hand-designed memories are unstable "
                   "and ExpeL is below no-memory on all three. Twelve memory systems are re-implemented. Not 4: the "
                   "automated agent-design/self-referential lineage (ADAS-type, H21 members) is not discussed.",
                   ["son55:E002", "son55:E003", "son55:E019", "sol:E001"]),
            "M": R("resolved", 3, "Both seats 3; re-checked. The bilevel loop (empty-memory inner runs → three-way "
                   "fitness → Pareto parent selection → trajectory-replay diagnosis → constrained redesign within the "
                   "four-module interface) is a reasoned response. Not 4: no prediction distinguishing it from random "
                   "mutation or design without diagnosis.",
                   ["son55:E004", "son55:E007", "son55:E008", "son55:E009"]),
            "X": R("resolved", 3, "Both seats 3; re-checked. K_max=3, K=1, S=3, 60 trajectories (40 new + 20 reused), "
                   "empty memory per iteration, the BaseMemoryProvider interface and the frozen deployment can be "
                   "reconstructed. Not 4: candidate validity checks, rollback, design prompts and lineage rules are "
                   "missing, and greedy K=1 keeps no non-improving candidates.",
                   ["son55:E005", "son55:E006", "son55:E010", "son55:E033", "sol:E007"]),
            "E.measurement": R("resolved", 2, "Opus sides with son55. Exact-match and LLM-as-judge protocols are both "
                               "supported, and which benchmark uses which is not stated. WebWalkerQA is a 170-query "
                               "sample. The reported GAIA 73.33 has two incompatible provenances (App. 9.1 vs Sec. "
                               "5.3/Table 3), a reporting-integrity failure under the run cap (r09b "
                               "EvoRoute/AgentDevel). The 'up to 17.06 %' headline is an absolute-point gain on the "
                               "weakest baseline. Cost/latency/steps are reported alongside, and GAIA/WW counts are "
                               "consistent k/n.",
                               ["son55:E027", "son55:E025", "son55:E017", "son55:E018"],
                               ["son55:E021", "son55:E022", "son55:E015", "son55:E016"]),
            "E.causality": R("resolved", 2, "Both seats 2; re-checked. The no-memory control and seven re-implemented "
                             "human memories on the same framework are informative. There is no evolved-vs-seed "
                             "(AgentKB-style) number, no diagnose-vs-random redesign and no K/S/round ablation, and "
                             "re-implementation fidelity is unverified (ExpeL < no-memory everywhere).",
                             ["son55:E017", "son55:E018", "son55:E019", "sol:E013"], ["son55:E020", "son55:E034"]),
            "E.holdout": R("resolved", 2, "Both seats 2; re-checked, with a shared correction. The TaskCraft→"
                           "WebWalkerQA/xBench transfer and the cross-LLM runs are real separation. GAIA is affected "
                           "by Level-1 use in evolution or misreported provenance. The TaskCraft column includes the "
                           "120 evolution queries (k/300; opus:O01), which both seats left as 'unclear'.",
                           ["son55:E024", "sol:E011", "sol:E012"], ["son55:E022", "son55:E021", "opus:O01"]),
            "E.statistics": R("resolved", 1, "Both seats 1; re-checked (A2 ladder). Single-run pass@1, no seeds, "
                              "intervals or tests; sample sizes and negative baseline results are given.",
                              ["son55:E025", "son55:E026", "sol:E013"], ["son55:E028"]),
            "E.cost": R("resolved", 2, "Opus sides with son55. Per-task API $, latency and steps are reported for "
                        "MemEvolve and seven memories plus no-memory on three benchmarks, which supports the scoped "
                        "claim of no cost increase per task. The meta-evolution cost (calls, tokens, time) is absent, "
                        "the gap that S4 records. Partial disclosure → 2. sol's 1 treated the missing search cost as "
                        "nearly total absence.",
                        ["son55:E017", "son55:E018", "son55:E030", "sol:E014"], []),
        },
        "status": "reviewed",
        "reason": "Complete pinned v1 text read, plus page image p-09 for Figure 4. In scope (system_method): the "
                  "retained object is executable non-weight memory-architecture code, redesigned from execution "
                  "feedback and deployed frozen. All eight items resolved.",
        "aggregate_status": "accepted_final",
        "a3": "none (in scope; both seats agree)",
        "resolutions": [
            res("domain_pattern.matches", *C(p, "domain_pattern.matches"), "sol", [["make_the_improver_editable", "H21"]],
                "H21 ('outer loop searches over the design of the inner loop's learning mechanism — memory schema, "
                "update and retrieval code') names this exact operation. son55's H17 is a coarser description of the "
                "same search: generic offline agent-design search, and son55 notes its distinguishing primitives are "
                "absent. Listing both counts one operation twice. The frozen-transfer check H17-S6 would add is "
                "already covered by make_the_improver_editable F3/F6.", ["son55:E004", "son55:E008", "sol:E006"],
                NOSCORE),
            XC(p, "local:2512.18746-1", "son55", "unmet",
               "Verified: the progression is shown only qualitatively (Figure 6); there are no per-round or seed "
               "scores.", ["son55:E034"]),
            XC(p, "local:2512.18746-2", "revised", "unmet",
               "Substance verified (App. 9.1 vs Sec. 5.3, the same 73.33). Status corrected from "
               "'challenged_with_evidence' to unmet.", ["son55:E022", "son55:E021", "son55:E014", "son55:E018"]),
            XC(p, "local:2512.18746-3", "son55", "unmet",
               "Verified: single pass@1 numbers on 100–170 tasks.", ["son55:E025", "son55:E026"]),
            XC(p, "rs:generative_process_redesign/RE-1", "son55", "partial",
               "Verified: Table 3 shows fixed architectures are inconsistent, but no architecture-evolution ablation "
               "exists.", ["son55:E019", "son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-3", "son55", "unmet",
               "Verified: no ablation of diagnosis, Pareto selection, replay, K or S.", ["son55:E004", "son55:E007"]),
            XC(p, "rs:generative_process_redesign/RE-5", "revised", "partial",
               "Per-task inference cost parity and the same backbone address deployment-compute confounding. The "
               "evolution compute is missing → partial, not unknown.", ["son55:E030", "son55:E017", "son55:E018"]),
            XC(p, "rs:generative_process_redesign/RE-6", "son55", "partial",
               "Verified: cost/delay/steps are tabulated; there is no failure-case analysis of evolved designs.",
               ["son55:E017", "son55:E018"]),
            XC(p, "rsi:make_the_improver_editable/F5", "son55", "unknown",
               "Verified: designer and agent share GPT-5-mini, and the per-benchmark judge setup is unspecified. "
               "Whether the anchor leaks cannot be determined.", ["son55:E027"]),
            XC(p, "rsi:make_the_improver_editable/S4", "son55", "unmet",
               "S4 is specifically search cost, and it is absent. Deployment cost is credited in E.cost.",
               ["son55:E030", "sol:E014"]),
            XC(p, "rsi:make_the_improver_editable/S5", "son55", "unmet",
               "Verified: K=1, only the top-ranked architecture expands.", ["son55:E005"]),
            RC(p, "E.measurement", "son55", 2, "See ratings.E.measurement. The GAIA provenance conflict and the "
               "unspecified judge protocols → reporting-integrity cap. sol's 3 did not apply the inconsistency that sol "
               "itself noted under E.holdout.", ["son55:E021", "son55:E022", "son55:E027"], "-2.5 vs sol (10×1/4)"),
            RC(p, "E.cost", "son55", 2, "See ratings.E.cost. Per-task costs against eight comparators are reported; "
               "only the search cost is missing.", ["son55:E017", "son55:E018"], "+1.25 vs sol (5×1/4)"),
        ],
        "shared_error_corrections": [
            {"field_path": "ratings.E.holdout.counterevidence_ids",
             "sol_value": "TaskCraft 120/300 overlap 'unclear'", "son55_value": "TaskCraft split 'not stated'",
             "correction": "added opus:O01: the TaskCraft column includes the 120 evolution queries",
             "reason": "Both seats treated the TaskCraft evaluation split as undetermined. Every Table 2 TaskCraft "
                       "value is an exact k/300 and none fits n=180, so the evaluation includes the meta-evolution "
                       "queries. Band unchanged at 2: the WebWalkerQA/xBench transfers are the clean holdout and were "
                       "already the basis of 2.",
             "evidence_ids": ["opus:O01", "sol:E010", "son55:E023"], "score_impact": "none (E.holdout stays 2)"},
        ],
        "aggregate_review": {
            "initial_judgment_before_seat_scores": "Read the full text before opening the seats. Bilevel memory-"
                                                   "architecture evolution (K=1, S=3, 3 rounds) on TaskCraft, frozen "
                                                   "transfer to WW/xBench (+3.5/+5 on Flash-Searcher, single run). "
                                                   "Seven human memories compared at per-task cost parity. No "
                                                   "evolved-vs-seed number, no evolution cost. GAIA provenance "
                                                   "conflict; TaskCraft k/300 overlap. Initial bands G3 M3 X3 Em2 Ec2 "
                                                   "Eh2 Es1 Ecost2; evidence_level retained (improver considered and "
                                                   "rejected: no evolved-vs-unevolved mechanism comparison at matched "
                                                   "budget).",
            "integrity_checks": "Both seats a1 on 2512.18746v1, material sha 599089df…; canonical seat hashes equal "
                                "conflicts.json; namespaces/parents valid.",
            "core_claim_check": "Re-read §4–5, Tables 2–3, App. 9.1. k/n-checked GAIA/WW/TaskCraft columns. Read "
                                "Figure 4 from page image p-09 (opus:F01); no rating depends on it.",
            "rating_agreement": "6/8 identical and re-checked; E.measurement, E.cost → son55. Final 62.5 equals son55's "
                                "total by item.",
            "expectation_renumbering": "None needed; son55 local-2 status corrected; S4/RE-5 statuses revised.",
            "retained_vs_retained_gain": "The evolved architecture is frozen and improves later, separate benchmarks "
                                         "→ retained. Improver level is not met: the evolved mechanism is never "
                                         "compared with the unevolved seed under a matched budget.",
        },
        "figure_dependence": "Figure 4 (cross-framework transfer) read from page image p-09 (sha256 " + FIG_SHA[:12] +
                             "…). Not load-bearing for any rating. Re-dispatch seats with page images only if "
                             "cross-framework transfer should carry evidence weight.",
    }

    return S
