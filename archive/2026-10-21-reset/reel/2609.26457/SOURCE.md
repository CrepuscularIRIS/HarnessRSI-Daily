# SOURCE — Recursive self-improvement of AI research agents

Read from: arXiv 2609.26457v1
Paper figures shown: none

Exact-version PDF: https://arxiv.org/pdf/2609.26457v1, downloaded directly to `/home/lingxufeng/reel-work/2609.26457/paper.pdf`. Read all 28 pages including references and Appendices A–E, using layout and plain text; inspected rendered pages 11, 24 and 26. Exact title and author order copied from PDF p1. Figure reuse prohibited for this task; all poster geometry and results charts are original redraws from the reported numbers. No paper/repository code executed. No code URL supplied.

## Provenance

| Content | Paper source |
|---|---|
| Title, authors, Weco AI affiliation | p1 title block |
| Two loops, public/private separation, mean g, best-grade incumbent, initialization and finite K | pp3–4, equations 1–4, Algorithm 1 |
| AIDE0 refactor, AIDEhuman baseline, reviewer roles, Opus 4.7 / Gemini 3 Flash, model choice on selection tasks | pp4–5 §2.2 |
| 8 days, 100 nodes, 99 proposals, seven accepted steps, 0.703 → 0.778; two further runs | pp5–6 §3.2; Figure 2 caption (also says buggy proposals get no grade) |
| External task non-overlap, family-level ID/OOD, checkpoint selection | pp6–7 §3.3 |
| All benchmark means and SEs in blogs and poster | p24 Table 1; chart redraw uses AIDE0, AIDE85, AIDEhuman, with ± one SE value labels |
| Tasks, seeds, models, dollar/step/time constraints and early-termination handling | p24 Table 2 and Appendix A prose |
| Weather task scoring relative to initial dynamical core, not leaderboard | p25 Appendix A |
| Reward-hacking rates 55%, 39%, 32%, human 39% | p8 §3.4 prose, not figure-label-only values |
| 38 pairs; three-seed averaging before classification; >1.02× and half-survival/crash criterion | pp24–25 Table 2 and Appendix A |
| Bandit, periodic forking, error memory, 15% threshold | pp8–9 §3.5 |
| Unchanged ranking under robustness penalty; evaluator-script repair | p10 §3.5 |
| Ignition: same AIDE47 initial inner agent, three seeds per arm, 50 steps, inconclusive | pp10–11 §3.6; 0.780 / 0.782 are explicitly in Figure 7 caption, not values inferred from plot |
| Total-cost limitations, compounded noise, unknown component attribution | pp10–13 §3.6 / Discussion; full PDF searched, no aggregate dollar/token/GPU-hour bill found |
| AIDEhuman compared to AI Scientist v2, Autoresearch, original AIDE, OpenEvolve, AI Scientist v1, AIRA; AdaptiveSearch excluded | p25 Appendix B. We do not reproduce figure-only comparator values or claim statistical superiority. These six are not the Table 1 baseline set. |
| Cross-model $20 cap / ALE 36-hour cap; stronger ALE than MLE; Fable MLE within one SE | p26 Appendix C prose; Figure 9 |
| Representative rejected proposals, pooled runs, not direct implementations | pp26–27 Appendix D, Table 3 |
| Context-limit failures: five AIDE0 FML, 48 larger-budget ALE; other harnesses avoid them | pp24, 27 Appendices A/E |

## ‡ values

- **0.823‡ and 0.828‡**, in both blogs: AIDE0 and AIDE85 Fable 5 MLE-Bench private-percentile means, read directly from Figure 9b bar labels on PDF p26 and visually verified against the rendered page. Appendix C prose states the improvement is within one SE. They are not arithmetic derivations. No paper image is reproduced.
- No computed delta, percentage, task count or inferred win count is used. Poster numerical results all come from tables or prose/captions and require no ‡ marker.

## Scope and absence checks

- Equal-budget wording applies to fixed per-task selection budgets and the explicit per-benchmark evaluation protocol. FML and kernel evaluation match steps, not dollars. It does not mean equal historical development or self-improvement compute.
- Main Table 1 uses multiple evaluation seeds per task but checkpoints from the featured RSI lineage. Additional full runs are reported, but no external evaluation aggregate across their final agents is given. Ignition separately has three independent outer-loop seeds per arm; no general single-run claim is made.
- Table 1 does report SEs, so the main comparison must not be called variance-free. Reward-hacking rates lack rate CIs. Ignition has min–max bands and run curves, not CIs or a decisive test. MLE/FML numerical advantages over AIDEhuman are small relative to SEs; no significance is inferred from separate SEs.
- Gemini 3 Flash is selected on the selection tasks. Retained defaults optimize g; no separate hyperparameter-development split, baseline tuning-search budget, explicit selection-task inventory/count/budget table, or precise repetitions per grade is reported in the full paper.
- External tasks were excluded from the RSI selection loop according to §3.3. This does not establish their absence from model pretraining. Kernel downstream testing is a reward-hacking diagnostic, not a comprehensive benchmark contamination audit.
- The private evaluation-script repair is author-described. The paper does not report a matched baseline-with-that-repair ablation; we do not infer malicious behavior, altered answers, or the size of any effect.
- Algorithm 1 and prose have no identified initialization/acceptance disagreement. The algorithm leaves incumbent selection implicit until its final argmax while prose defines the best-so-far incumbent; this is not treated as a contradiction.
- No text–table numerical inconsistency is claimed. Different budgets/models in Appendix C are distinct experiments, not discrepancies with Table 1.
- No per-task breakdown supports concentration analysis within each aggregate. We can identify weak benchmark/model comparisons (FML vs human; Fable MLE) but cannot assign the aggregate gains to individual tasks.
- Related methods in Table 3 are conceptual analogues, not executed competitors. No claims imported from the related Reel posters.

## Judgment notes

Stored record: `research/scores.jsonl`, score 64, band ★★, evidence level retained; latest matching judgment is `research/judgments/b18.jsonl`. Neither file modified.

1. **Variance understated in the record.** `variance: unclear` does not reflect full-PDF Table 1's SEs, Table 2's evaluation seeds or Figure 7's repeated outer-loop arms. We report these explicitly without recomputing the score.
2. **Leakage scope narrower than its label.** The stored `leakage_guard: tested` quote points to kernel reward-hacking testing. It supports a held-out behavioral diagnostic, not a comprehensive contamination audit. We preserve the score but distinguish these claims.
3. **Cost evidence partial in units.** The judgment credits optimizer cost using wall-clock/trajectory size; the full PDF does not supply the aggregate monetary/token bill.
4. **Retained remains appropriate.** A changed research harness transfers externally; the direct improver comparison is expressly inconclusive, so no established improver-level or accelerating-RSI claim is made.

## Local verification

Poster created using the house-style shared library without changing it. Local render checks card overflow; final visual and typography checks cover SVG and body labels. Required repository validation is run on the delivered directory. Skill defaults that require copied paper figures, subagents, new shared files, or publication are not used: the worker brief explicitly forbids these and requests only the five local deliverables.
