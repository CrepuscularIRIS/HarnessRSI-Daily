# SOURCE — Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills

Read from: arXiv 2606.07412v1
Paper figures shown: none

Version note: The task identifies an original candidate-metadata discrepancy: 2606.07412v2 returns 404 and the abstract page lists only [v1]. Downloaded and read https://arxiv.org/pdf/2606.07412v1, whose title-page stamp explicitly says arXiv:2606.07412v1. No v2 content was read or inferred. At final validation the live candidate record already names v1, so the unmodified repository checker passes normally. We did not edit candidate metadata or the checker.

Visuals: the task explicitly requires figure_reuse=false, which we follow even though the live candidate record permits reuse. No paper image, crop, figure or screenshot is included. All poster graphics are our own schematic and charts from table numbers. The PDF was read in full, including references and Appendices A–H (21 pages); both layout-preserving and plain-text extractions were used. Rendered pages 8, 10 and 18 were checked visually for headline, ablation and cost tables.

## Title and authors

Exact title from PDF p1: **Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills**.
Authors in PDF order: Chuan Xiao, Zhengbo Jiao, Shaobo Wang, Wei Wang, Bing Zhao, HU WEI, Linfeng Zhang, Lin Qu. Affiliations: AI Data, Alibaba Group; Shanghai Jiao Tong University. The poster preserves the title-block spelling HU WEI. No author/code information is inferred from external pages.

## Claim and number provenance

| Surface/claim | PDF provenance |
|---|---|
| Skill contents, successful/failed traces, semantic deduplication and trace coverage | §3.2, p5 |
| Shared Generator/Solver weights, GRPO/GDPO, no frozen-weight inference-only experiment | §§3.1–3.5, pp4–7; §4.1 p7 |
| Format/grounding/execution/semantics acceptance | §3.3, Eq6, p6; Algorithm1 p14 |
| Alignment reward versus acceptance gate | Eq2 p4, Eq8 p6, Algorithm1 lines9–10 and22–25 p14; AppendixD pp16–17, AppendixF p18 |
| Solver hides reference solution and Generator verifier internals; full/partial/regression rewards | §3.4 p6; Table7 p20 |
| Qwen3.5-9B, Qwen3.6-27B, three rounds,12k instances/round,36k total;500/300/731 evaluation issues; harnesses | §4.1 p7; Table1 p8; AppendixB pp14–15 |
| Headline chart/table: Base42.60/29.67/17.24/10.11; SSR47.00/34.00/20.66/12.36; full50.40/36.67/22.85/14.61 | Table1 p8, Verified/Lite/Pro/TB2 order, final-iteration rows |
| Overall24.91/28.51/31.13 is benchmark mean, not seed mean; +6.22 overall; +7.80/+7.00/+5.61/+4.50 over base | Table1 and §4.2 p8 |
| +3.40 over SSR on Verified | Introduction p3 and AppendixF.1 p18; also Table1 p8 |
| SSR strongest final baseline, TB2 tie with Socratic-Zero12.36; Socratic-SWE first-round12.36 | All baseline iterations checked, Table1 p8; §4.2 pp8–9 wording does not establish statistical distinction |
| Registry46.20; manual skills48.00; GRPO48.60; full50.40 | Table2 p10; explanation that no trace distillation means manual skills in §5.2 p9 |
| Extractor9B49.80/default27B50.40/Opus4.5 51.00 | Table2 and §5.3 p10 |
| Hardness47.40, uncertainty48.20, Gaussian variance48.80, alignment50.40, hybrid50.60, hybrid+0.20 | Table3 p16; AppendixD.2 p17 |
| Inner product49.40 versus cosine50.40 | Table6 p18 |
| BeyondSWE100 reference tasks excluded from Solver training and final evaluation; language-stratified; gradients influence Generator | AppendixE.1 p17 |
| Validation size20/100/200 gives Verified49.20/50.40/50.60; +0.20 at200; two independent rollout sets measure gradient stability | Table4 and AppendixE.2 p17 |
| No separate default/hyperparameter selection split specified | AppendixE pp17 and Table7 p20; sensitivity results are on SWE-bench Verified |
| Comparable instance/interaction budgets,10% SWE-smith seeds where needed, per-baseline mechanisms and397B Teacher | §4.1 p7, AppendixB pp14–15 |
| No baseline explicitly given same trace registry/alignment; baseline-specific tuning budget absent | Baseline details AppendixB pp14–15; Table7 p20 covers Socratic-SWE only |
| 8×A100-80G,15.0h/iteration;4.2/7.8/1.7/0.5/0.8h stages | Table5 p18; Table7 p20 |
| Alignment1.3h/iteration; about3.9h over45h, comparable FLOPs claim versus SSR | AppendixF.1 pp17–18; skill extraction is not separately itemized nor explicitly said to be included |
| Extended five-round52.00 versus48.00; plateau with fixed repositories | §5.1 p9 **prose**, not figure-only label reads; Figure4 not reused |
| Initialization/registry-update ambiguity | §3.2 p5 seed-task trace collection versus AppendixB p14 repo-only/no-pre-existing-traces claim; Algorithm1 p14 takes S,D0 as input and omits refresh |
| Reversible bug, original-code reference, no test edits | AppendixG.1 pp18–19 |
| Oracle-patch disclosure safeguard and repeated targeted tests in OAuthLib example | AppendixH pp20–21; not presented as a global contamination audit |
| Hidden benchmark tests not provided | AppendixG.3 p19 |
| Fixed-pool, validation dependence, executable-test and broader-transfer limits | Limitations p10; §5.1 p9 |
| No seeds/run counts/CI/SD for main or ablation outcomes; no seed-repo list or overlap/pretraining-contamination audit | Full PDF pp1–21, including setup, all tables, AppendicesA–H and limitations searched/read; absence claims are reporting limits, not assertions that no checks were performed |

## ‡ numbers

None. No computed numeric deltas, computed row/task counts, or figure-only values are used. Five-round52.00/48.00, the +3.40 SSR gap, and other quoted increments occur in the paper's prose as well as any tables/figures. Chart ticks are scale guides, not empirical measurements. Model/version names are identifiers, not derived quantities.

## Interpretation and unresolved details

- Weight updates are explicit in the method. The interpretation does not recast this as a frozen-model skill-memory intervention. Ablations of the registry are embedded in the full weight-training pipeline.
- Eq2 and Algorithm1 hard-gate on Valid. Eq8 supplies a policy-training reward, while AppendixD/F use selection language without an operational cutoff. No invented positive-cosine keep rule is shown.
- The bootstrap (seed-task collection versus no pre-existing tasks) and registry-refresh details are not resolved by Algorithm1. We flag missing reconciliation neutrally without guessing which procedure ran.
- Named validation/evaluation datasets do not prove repository-disjoint training. The seed corpus and trace/evaluation overlap are unspecified; no benchmark decontamination audit is reported. The AppendixH anti-oracle rule and AppendixG hidden-test prompt are narrower safeguards.
- Hyperparameter/default sensitivity uses Verified outcomes, with no independent selection split stated. This is not an allegation that the final benchmark was necessarily used for all tuning; the split story is unreported.
- No statistical confidence claim is made. Table4's independent gradient-rollout comparison is not evidence of repeated training/evaluation runs. We do not infer single-run results.
- Budget equality is stated for instances and interaction. The SSR comparable-FLOPs statement is an author claim; complete baseline/extractor/Teacher compute accounting and tuning budgets are unavailable.

## Judgment notes

Stored score:64, band★★, evidence level retained, from research/scores.jsonl. Latest matching judgment found: research/judgments/b23.jsonl (version_read:v1). No newer matching record was found.

1. The stored optimizer_cost is unclear. The full v1 PDF **does report** runtime and gradient-alignment overhead in AppendixF/Table5. Our read acknowledges this evidence rather than repeating the absence. Distillation-specific cost and baseline cost ledgers remain unreported. Score/judgment files were not edited.
2. The recorded retained level is reproduced as the board's judgment, not a fresh reclassification. Because Generator/Solver weights are jointly trained, the work does not isolate a non-weight retained artifact's benefit with frozen weights. That boundary is explicit in both blogs and the poster.
3. Budget matching is reported, but restricted to the stated instance/interaction budgets and SSR comparable-FLOPs claim; equal access to distilled knowledge and complete extra-model compute are not established.

## Validation status

Executed the stock `python3 research/check_reel.py reel/2606.07412` from the repository root: `ok reel/2606.07412`, `1 reel dirs, 0 failing`. The live candidate version is v1 at validation time. No override, monkeypatch, candidate edit or checker edit was needed. Poster rendered with no OVERFLOW; final PNG was visually inspected. All five required artifacts are delivered.
