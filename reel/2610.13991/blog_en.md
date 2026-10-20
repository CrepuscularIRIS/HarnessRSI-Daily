# Predict Before You Modify: a forecasting module inside a self-evolving agent — medians are higher in all four domains, but the controls and the run-to-run spread qualify the gain

*A Reel interpretation of [arXiv 2610.13991v2](https://arxiv.org/abs/2610.13991v2) (HarnessRSI Daily score 72, ★★★). The paper prints an anonymous code link: [anonymous.4open.science/r/Predictive-self-evolution](https://anonymous.4open.science/r/Predictive-self-evolution/).*

## What the system changes about itself

The paper builds on HyperAgents: a **task agent** that solves the target tasks and a **meta agent** that edits both the task agent and itself, with an archive of evaluated agents as parents. It adds a third editable part, the **Improvement Dynamics Model (IDM)**: a program that calls a frozen LLM to forecast, for every task, the outcome of a proposed code diff (for example "resolved / unresolved / incomplete / empty patch" in coding, or the probability that a robotics reward function is unusable). Model weights never change; the retained artifacts are code and prompts.

## The loop, and the keep/reject rule

1. A parent is drawn with the fixed HyperAgents selection rule; the meta agent writes a **draft diff**.
2. The IDM forecasts the draft. A fixed rule requests **one extra revision** when the bias-corrected predicted score is below the parent's observed score; the task-level forecast is appended to the revision request. Otherwise the draft is kept.
3. The final diff is forecast again, the child is **always evaluated**, and the (forecast, observed outcome) record is stored.
4. Every K = 5 generations the meta agent edits the IDM's forecasting code and instructions. The candidate is tested on the next K records, collected while the current IDM stays deployed, and **replaces the current IDM only if its prediction loss is lower and its centered mean squared error does not increase**.

Each setting is five complete runs of 40 generations. Task agents and meta agents differ by domain (for example o3-mini with Claude Sonnet 4.6 on Polyglot coding; GPT-4o with GPT-5.4 on paper review and math grading).

## Headline result, as reported

The only baseline in every domain is HyperAgents (no extra revision). Scores are normalized area under the best-so-far curve (AUBC), medians over five runs; the AUBC counts how early good agents are found, not only the final score.

| Setting (AUBC, 40 generations) | HyperAgents | Selective IDM (ours) |
|---|---|---|
| Polyglot coding | 0.210 | 0.306 |
| Paper review (×100) | 73.50‡ | 77.85‡ |
| Robotics reward design (×100) | 76.45‡ | 77.35‡ |
| Joint paper + robotics (×100) | 73.15‡ | 75.99‡ |
| Math grading (×100) | 50.65‡ | 53.68‡ |

The Paper, Robotics and Joint rows come from the same joint-evolution runs (Fig. 4 caption: Paper and Robotics track the best descendant per domain, Joint the best single descendant on the joint score).

Under matched token budgets the paper reports coding +10.9%, paper review 74.95‡ vs 72.00‡, robotics 75.79‡ vs 75.08‡, joint 72.46‡ vs 71.79‡, and math 53.56‡ vs 51.05‡. On 166 held-out Polyglot tasks, agents selected from Selective IDM runs gain a median 13.25 percentage points over the common initial agent (initial resolve rate 16.27%), against 5.42 for HyperAgents. Held-out tasks were not used for modification or selection.

## The controls that decide whether the gain is real

- **Is it just an extra revision? (Polyglot only).** Reflective HyperAgents revises every draft once without IDM feedback. Median AUBC at 40 generations: Selective IDM 0.3058, IDM Reflection 0.2888, Frozen Selective IDM 0.2792, Reflective HyperAgents 0.2617, HyperAgents 0.210. So a plain extra revision recovers about 54%‡ of the HyperAgents-to-Selective-IDM gap (0.052‡ of 0.096‡). Under a common 145.79M-token budget Selective IDM is 3.9%, 2.9% and 3.6% above Reflective, Frozen and IDM Reflection. The Table 7 intervals (Selective IDM minus comparator, AUBC ×100, 95% bootstrap over five runs) all include zero: 4.42 [−6.54, 9.25], 2.67 [−3.29, 7.62] and 1.71 [−14.17, 5.46] at 40 generations; 1.21 [−6.32, 4.79], 0.92 [−4.73, 2.64] and 1.13 [−9.78, 2.85] under matched tokens. The cleanest contrast for IDM feedback itself, IDM Reflection against Reflective HyperAgents (both revise every draft), is 0.2888 against 0.2617, 2.7‡ AUBC points ×100; the paper gives no interval for this pair, since Table 7 compares only against Selective IDM. The paper reports no Reflective-style control for the joint or math settings.
- **Does editing the IDM matter?** Frozen Selective IDM (same selective rule and bias calibration, IDM never edited) is below the evolving version in median, with the interval above.
- **Do the forecasts get better?** On Polyglot, the candidate IDM has lower Brier loss than the current one in 19 of 28 comparisons, including rejected candidates; this is the same comparison that gates adoption (a candidate must lower the loss on that block without raising CMSE), and the number of adopted candidates is not stated. On fixed historical modifications from generations 1–5 of "selected runs", the final deployed IDM's loss is 8.7%–24.4% below the initial one (coding 89.75‡, paper review 91.34‡, robotics 79.53‡, math 75.58‡, initial = 100). The paper does not say how these runs were selected or whether the generation 1–5 records were among those used to edit the IDM; since IDM edits use "accumulated records" and the archive is an IDM input, these comparisons may be in-sample. Giving the IDM the diff lowers its mean prediction loss relative to a No-diff condition by 16.18% (paper review), 19.98% (robotics) and 16.25% (joint), on 15 modifications. The paper reports no simple non-LLM predictor for comparison.
- **Transfer (math grading).** One IDM evolved on paper review and robotics, chosen "based on source-domain prediction improvements and a preference for fewer domain-specific heuristics" before the math experiments, initializes all five Transferred IDM runs. AUBC ×100: HyperAgents 50.65‡, Selective IDM 53.68‡, Transferred IDM 55.52‡ (matched tokens 51.05‡, 53.56‡, 54.81‡). Held-out accuracy on 100 tasks: 47%, 51%, 55%; four of five transfer runs exceed the median of Selective IDM from scratch. This is one donor IDM and one target domain, and the Transferred IDM cost (104.15M tokens) and its matched-token AUBC do not include the cost of evolving the donor IDM; Table 6 gives no donor cost.
- **Cost.** Mean tokens per complete 40-generation run, including evaluation: coding 49.45M for HyperAgents against 170.22M for Selective IDM (about 3.4×‡); joint 101.67M against 140.61M; math 69.46M against 99.13M (Transferred IDM 104.15M). Against the controls, Selective IDM's 170.22M is about 23%‡ above Reflective HyperAgents (138.56M) and 26%‡ above Frozen Selective IDM (134.62M). Matched-token AUBC against HyperAgents is evaluated at HyperAgents' median cost; for coding that is 44.21M, about 26%‡ of Selective IDM's mean full-run cost. Selective IDM's mean cost is 18.0% lower than IDM Reflection's, which revises every draft. The paper does not report a tuning budget for any baseline.

## Where the gain is absent or small

- **Run-to-run spread.** Medians are over five runs and the plotted 95% intervals overlap for most paired bars (Figures 3–4, 6); in Table 7 all six Selective-IDM-versus-ablation intervals include zero. Against HyperAgents, all five Selective IDM coding runs exceed the HyperAgents median under both budgets (App. B.3). In the paper-review panel of Fig. 10 (read off the plot), the Selective IDM median of 77.85‡ is carried by two high runs (roughly 88 and 95) and two of the five Selective IDM runs lie at or below the HyperAgents median; in the math panel (Fig. 11) two of five Selective IDM runs lie below the HyperAgents median.
- **Robotics.** 76.45‡ vs 77.35‡ (40 generations) and 75.08‡ vs 75.79‡ (matched tokens), under one point on the ×100 scale; joint matched-token 71.79‡ vs 72.46‡.
- **Math.** Selective IDM over HyperAgents is 53.68‡ vs 50.65‡ on AUBC and 51% vs 47% held-out (100 tasks); the transfer gain over Selective IDM is 4 points on those same 100 held-out tasks.
- **Much of the coding gain is reproduced by a plain extra revision.** Reflective HyperAgents (no IDM) reaches a median 29.25% mean resolve rate on the preliminary tasks and 35.0% of generations fully evaluated, against 29.50% and 45.0% for Selective IDM and 17.00% and 5.0% for HyperAgents (Table 5). Archive scores count unevaluated tasks as zero and a draft is fully evaluated only after solving at least four of ten preliminary tasks, so part of the AUBC gap reflects how often drafts pass this gate.
- **No held-out set for paper review or robotics.** The joint results are on the scores that guide evolution (paper-review validation accuracy, robotics training fitness on six trials).
- **Stated scope.** All results build on HyperAgents with one model assignment per domain; the paper has no separate limitations section.

## Our read

HarnessRSI score **72**, band ★★★, evidence level **improver**: the paper varies the improvement mechanism itself (forecast-guided revision, IDM updates, transfer of the IDM) and compares against ablations. It reports held-out evaluation for coding and math, cross-domain transfer, five runs per setting with bootstrap intervals, matched-token AUBC, token costs, and a code link. It does not report a same-mechanism control (always-revise) outside Polyglot, where a plain extra revision accounts for much of the gain over HyperAgents; an audit of benchmark or model contamination; held-out tasks for paper review and robotics; or the cost of the donor IDM. Most paired intervals overlap, and Selective IDM uses more tokens per run than HyperAgents and the controls.

*Numbers marked ‡ were either computed by us (token ratios, percentages of gaps, the IDM Reflection minus Reflective HyperAgents difference) or read from figure labels or plots that are not in the paper's HTML text; see SOURCE.md.*
