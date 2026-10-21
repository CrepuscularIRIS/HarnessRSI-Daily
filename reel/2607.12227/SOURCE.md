# SOURCE — Rethinking the Evaluation of Harness Evolution for Agents

Read from: arXiv 2607.12227v4
Paper figures shown: none

The exact-version PDF was downloaded from https://arxiv.org/pdf/2607.12227v4 to `/home/lingxufeng/reel-work/2607.12227/paper.pdf`. Its title block and version stamp were checked; all 26 pages, including appendices, were read using layout/plain extraction and rendered page inspection. All poster diagrams, charts and tables are our own drawings from the reported protocol and table values. Figure reuse is allowed by the supplied task metadata, but no paper figure is reused. No code from the paper repository was run. Code QR/link supplied by the board: https://github.com/rethinking-harness-evolution/code (PDF gives the parent GitHub organization URL).

## Bibliography

Exact title: **Rethinking the Evaluation of Harness Evolution for Agents**.
Authors, in PDF order: Yike Wang; Huaisheng Zhu; Zhengyu Hu; Yige Yuan; Zhengyu Chen; Shakti Senthil; Hannaneh Hajishirzi; Yulia Tsvetkov; Noah A. Smith; Pradeep Dasigi; Teng Xiao. Affiliations: Allen Institute for AI; University of Washington; Independent. Version stamp: 5 Oct 2026. Poster uses “Yike Wang et al.” for space, not a reordered author list.

## Claim and numerical provenance

| Content | PDF source | Scope / interpretation |
|---|---|---|
| Critique names Meta-Harness, AHE, AEVO | §§1–2, pp1–2 | These are cited works, not three independently reproduced systems. |
| Four-method taxonomy; update signal; selection rules | §§3.1–3.5, pp3–5 | Drawn by us. Shared Harness Evolution and instance-level Harness Scaling are distinct. Model weights fixed. |
| Actual Terminal implementation | §3.4 p4; §4.1 p5; A.1 p12 | AHE propose/refine loop with external explore agent disabled. All methods start with the same minimal bash-only harness. This is not complete AHE, nor an independent rerun of Meta-Harness or AEVO. |
| Terminal tasks, exact model labels, rollout budget, repetition | §4.1 p5 | 89 tasks; Claude Opus 4.6 / GPT-5.4 / GPT-5.4 mini; K=5, m=1; two independent runs. These repetition statements apply to Section 4, not automatically to ARC. |
| Terminal without tests | Table 1 p6 | All numbers are pass@1 percent. Average initial68.2, parallel72.3, sequential69.3, evolution67.4, scaling71.8. Claude scaling76.0 vs parallel74.7; GPT initial75.3 vs evolution69.7. |
| Terminal with tests | Table 2 p6 | pass@1 / pass@5 percent: initial67.6/—; parallel82.0/82.0; sequential76.9/87.1; evolution69.7/79.0; scaling75.5/85.6. Different initial controls in Tables 1 and 2 are not cross-compared or called inconsistent. |
| Definitions and denominator | A.1 p13, equations1–2 | pass@1 is average reward over rollouts; pass@k is at-least-one success. Infrastructure failures count as zero, not excluded. The protocol's oracle-return descriptions and rollout-based metrics are kept separate. |
| Held-out generalization | Table 3, §4.4 p7 | 45 train/10 validation/34 test, disjoint; validation selects final harness. Initial/evolved average63.2/63.2%; per-model63.3/64.5,72.1/72.1,54.4/53.0%. No significance test or CI reported. No task assignments, split-construction rule or random seed specified. |
| Terminal configuration and costs | Table6 p12; A.1 p13 | Fixed reference-run configuration, high reasoning,128,000 max generation tokens per turn,200,000 context; debugger/meta same model. Harness-edit cost explicitly excluded, not measured numerically. Same K is not measured total inference-cost equivalence. |
| Larger K exception | A.3, Tables7–9 p15 | Claude Opus 4.6 only, two independent runs; K10 with tests: scaling90.5/94.4% (pass@1/pass@10), sequential89.6/93.1%, shared evolution73.6/86.5%; held-out initial63.3 vs evolved63.0%. Authors call gap within run-to-run variance without providing the variance numbers. |
| ARC scope, budget, RHAE averages | §5.2 pp8–9; Table4 p8; B.1 pp16–17 | All25 public games;2,000 environment actions. Claude Opus4.8 VISTA*43.3,VISTA59.3,full77.5; GPT-5.6 Terra21.1,25.9,38.2. Units are RHAE, not win %. Relative79.0%/81.0% are printed in §5.2, not computed by us. Plain CLI reference44.3/4.6 RHAE. |
| ARC ablation/access scope | B.1 pp16–17, Table10 | VISTA* retains PNG/inspection/context-reset features but disables both memory files; VISTA restores evolving memory; full adds writable skills/tools/hooks. No single-component isolation, no equal-write-access alternative optimizer. Agent configs are listed; no internal token cap or independent tuning split/sweep budget stated. |
| ARC heterogeneous outcomes | Table4 p8 | GPT tr87full100 vs VISTA*11.8; sk48full0.0 vs0.8; vc33full0.0 vs0.6; Claude tn36full3.6 vs18.5. Named tasks avoid computed win counts. Run count/variance not specified for ARC. |
| Usage and mechanism examples | B.2–B.3 pp18–23, Tables12–13 | Artifact operations are usage, not causal component values; full harness includes hooks as well as skills/tools. We do not turn these examples into an independent transfer test. |
| Edge headline means, per-task counterexamples | §5.3, Table5 p9 | Five Interactive Games & Simulators bot-programming tasks only. Scores0–100. Claude Opus4.8 fixed48.3/scaling54.7 (paper13.3% relative); GPT-5.4 fixed45.9/scaling49.8 (paper8.5%). Two independent runs, no SD/CI. Claude NetHack44.3/61.3, Wesnoth88.0/86.0; GPT OpenRCT236.2/50.0, NetHack50.4/49.0, OpenTTD51.6/50.5. |
| Edge feedback, budget and adoption | C.1 pp23–25, Tables14–15 |12-hour wall clock includes summarization/editing and pauses; update after3 submissions or120minutes. Only validated changes installed, no validation criterion given. Visible submission feedback vs hidden host snapshot feedback separated; best-so-far includes both. Not an unseen-task test. |
| Hypotheses versus tested limits | §5 p7; §§5.1–5.3 pp8–10; appendices | Saturation and weak harness dependence are proposed explanations, not controlled causal tests. No game-held-out/cross-model artifact-transfer/improved-improver comparison reported. |

## ‡ numbers and figure-label reads

None. No newly computed numerical differences or counts are used, and no figure-label values are transcribed. All reported decimal values occur in PDF prose or tables; chart values come from Table 4. No figure credits table is needed because no paper figure is shown.

## Statistical, configuration and scope notes

- Section 4 and Appendix A.3 explicitly average two independent runs; Table 5 independently makes that statement for Edge. ARC's tables and Appendix B do not specify repetition count. We do not infer a single run, or extend Terminal's two-run protocol to ARC. No seed IDs, paired-seed guarantee, SDs or confidence intervals are supplied for the displayed comparisons. Appendix A.3's variance claim is attributed to the authors, not independently established.
- Hidden game seeds are not the same as paired experimental seeds. Appendix C describes five hidden seeds for DCSS, five maps for OpenTTD, and the Wesnoth multi-game judge. This does not establish seed matching across method conditions.
- Hyperparameter selection: Terminal defaults come from a fixed reference snapshot; the stated validation tasks choose a harness. ARC settings deliberately avoid saturated/entirely-unsolved models, with no independent tuning split identified. Edge gives update defaults. Separate baseline tuning budgets are not reported. Missing numerical settings named in blogs (Terminal temperature and split seed/assignments, ARC internal token cap) are distinguished from missing tuning-split disclosure. We do not infer test-set tuning.
- There is no identified unresolved text/table discrepancy needed for our claims. We checked the larger-budget variants before qualifying the abstract's negative statement: Table 8 really does contain larger Harness Scaling cells; it is not a text/table inconsistency because the authors discuss them as within variance. No controls from different tables are used to compute gains.
- The game improvements do not establish cross-task reuse. Positive ARC results occur on public games under action matching; Edge reports best-so-far within the adaptation window, including evaluator-only snapshots. Neither supports a held-out-game claim.
- Final caption correction after independent fact-check: at 2400px poster width, body/caption text and both QR captions measure at least 22px; the ARC legend measures above 22px after SVG scaling. All chart text and method-step text also measure above 22px. Print-emulated DOM/SVG font measurements and card-overflow assertions passed; the re-rendered PNG was visually inspected with no clipping or collisions. Measurements are saved in `/home/lingxufeng/reel-work/2607.12227/out/layout-check.json`. The compact poster directs readers to the blogs for full access/tuning detail.

## Judgment notes

Source: `/home/lingxufeng/ArxivDaily/research/scores.jsonl` and the latest matching record in `/home/lingxufeng/ArxivDaily/research/judgments/b12.jsonl`. Score63, band★★, evidence level`task`. No score or judgment file was edited.

The full PDF supports a qualified reading of the record, not a new score:

1. **`budget_matched: yes` is resource-specific.** Terminal matches K and rollout feedback but omits editing cost; ARC matches actions, not internal reasoning tokens; Edge includes editing inside wall-clock time. A single yes must not imply exact total-compute equivalence or equal tuning budgets. This critique applies directly to our budget-matched scoring dimension.
2. **`held_out: partial` does not imply positive transfer.** The paper rigorously separates search/validation/test in Terminal but observes a flat average. The board should distinguish doing a held-out diagnostic from proving the retained artifact improves on unseen tasks. Games provide positive same-task adaptation, consistent with `task`, not a demonstrated broad retained benefit.
3. **`variance: unclear` remains appropriate.** The full paper reports repeated means on Terminal and Edge, not numerical variance. Two independent runs cannot be silently upgraded to reported variability; ARC run count is unspecified.
4. **`retained_ablation: yes` is a bundled control.** VISTA vs full harness varies editable surfaces (including hooks), while VISTA* disables the memory files. This is informative but not an individually isolated skill/tool/hook causal effect, nor an equal-artifact-access update-rule comparison. Our scoring dimension should retain that qualification.
5. **`leakage_guard: tested` concerns selection/evaluation separation.** The Terminal disjoint-split experiment tests the same-task evaluation concern. It is not a pretraining-contamination audit, a universal leakage audit, or a positive held-out result for the games. Our leakage dimension should not conflate these.
6. **`optimizer_cost: partial` is bounded.** Edge counts editing time, whereas Terminal excludes it and ARC leaves internal reasoning outside the action metric. No comprehensive numerical optimizer token/dollar breakdown is supplied.
7. **Evidence ladder.** Changing a harness is not proof of improving the improver. This paper does not compare an evolved improvement procedure against its predecessor at matched budget. Multiple benchmarks are not themselves cross-task artifact transfer. The score summarizes our rubric; it must not be read as resolving the paper's critique of our topic.
