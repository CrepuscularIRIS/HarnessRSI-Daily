# SOURCE — Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents

Read from: arXiv 2610.13991v2
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but no paper figure is reproduced. The method diagram and charts on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Setup, splits, protocol: Sec 4.1 (p6), Table 1 (p14), Table 2 (p15), Table 3 (p15), App A.2–A.5 (pp14–18).
- Headline: Sec 4.2 (pp6–7) and Fig 3 (p7; 0.306 / 0.210 are printed on the curve and in the text; 10.9%, 13.25 pp, 5.42 pp, 16.27%, 166 tasks in text/caption); Fig 4 (p8; bar labels 73.50/77.85, 76.45/77.35, 73.15/75.99 and matched-token 72.00/74.95, 75.08/75.79, 71.79/72.46); Fig 6 (p9; 50.65/53.68/55.52, 51.05/53.56/54.81, 47%/51%/55%).
- Controls: Fig 7 (p9), Fig 8 and Table 6 (pp18–19), Table 7 (p19), Table 5 (p18), Fig 5 and Sec 4.3 (pp7–8), App B.3 (p20), App B.4 and Fig 12 (pp20–22), App A.3 (donor IDM selection, p15).
- Cost: Table 6 (mean tokens, M) and App B.2 (matched budgets 44.21M / 111.98M / 69.36M / 145.79M).

## ‡ numbers (computed by us)
- 3.4×‡ = 170.22 / 49.45 = 3.44 (Table 6, coding, Selective IDM vs HyperAgents mean tokens per complete 40-generation run).
- Figure-label numbers marked ‡ in the blogs (not computed): 73.50, 77.85, 76.45, 77.35, 73.15, 75.99 (Fig 4a, p8); 72.00, 74.95, 75.08, 75.79, 71.79, 72.46 (Fig 4b, p8); 50.65, 53.68, 55.52 (Fig 6a, p9); 51.05, 53.56, 54.81 (Fig 6b, p9); 89.75, 91.34, 79.53, 75.58 (Fig 5b, p8). These are printed on the bars/markers of the figures in the PDF but are not in the running text or tables, so the checker (which uses the arXiv HTML text) cannot find them; we read them from the PDF text layer and checked them against the page images. The ‡ marks them as "not found in the HTML text", not as recomputed values.
- 54%‡ (also 0.052‡, 0.096‡): Polyglot 40-generation AUBC, (0.2617 Reflective HyperAgents − 0.210 HyperAgents) / (0.306 Selective IDM − 0.210) = 0.0517 / 0.096 ≈ 0.54 (Fig 3a, Fig 7; the 0.2617 value is assigned as described under Notes).
- 2.7‡ AUBC points (×100) = (0.2888 IDM Reflection − 0.2617 Reflective HyperAgents) × 100 (Fig 7). The paper gives no interval for this pair (Table 7 compares only against Selective IDM).
- 23%‡ = 170.22 / 138.56 − 1 (Selective IDM vs Reflective HyperAgents mean tokens, Table 6); 26%‡ = 170.22 / 134.62 − 1 (vs Frozen Selective IDM); 26%‡ = 44.21 / 170.22 (coding matched-token budget as a share of Selective IDM's mean full-run cost; 44.21M from App B.2, 170.22M from Table 6).
- Fig 10 / Fig 11 statements (blog: roughly 88 and 95; two of five Selective IDM runs at or below / below the HyperAgents median) are read by us off the individual-run dots (pp 20–21) and are approximate; the paper prints no numbers for them.
- Poster "1.4–3.4×" = range of the same ratio over settings: 140.61 / 101.67 = 1.38 (joint), 99.13 / 69.46 = 1.43 (math), 170.22 / 49.45 = 3.44 (coding).

## Notes
- The Fig 7 / Fig 8 per-method values were matched to method names by us: the figure text lists the numbers without clear per-line labels in the PDF text. Assignment 0.3058 Selective IDM, 0.2888 IDM Reflection, 0.2792 Frozen Selective IDM, 0.2617 Reflective HyperAgents (40 generations) is consistent with Table 7 (differences 4.42, 2.67, 1.71 ×100 against 0.3058 within rounding) and with the Fig 7 curve colours/ordering; matched-token 0.3211 / 0.3119 / 0.3090 / 0.3098 (Selective / Frozen / Reflective HA / IDM Reflection) is consistent with Table 7 (1.21, 0.92, 1.13) and with the 3.9%, 2.9%, 3.6% in App B.2.
- Poster chart: Polyglot bars are plotted at 21.0 / 30.6 (= 0.210 / 0.306 × 100) so they share the 0–100 axis with the ×100 AUBC values of the other domains; their labels show the paper's raw 0.210 / 0.306.
- The paper's Fig 3(b) (matched-token coding AUBC) carries no bar labels; only the text value "10.9% higher" is used. 3(c)'s held-out values 13.25 pp and 5.42 pp are in the text.
- "All six intervals include zero" refers to the six 95% run-level bootstrap intervals in Table 7 (three comparators × two budgets). "Most paired intervals overlap" is our reading of the error bars in Figs 3, 4 and 6 (no numeric CIs are printed for those).
- "Fixed historical modifications from generations 1–5 of selected runs" (Fig 5b): the paper does not say whether these records were also among those used to edit the IDM; we report it as not stated; since Sec 3.4 says IDM edits use "accumulated records" and the archive is an IDM input, the comparison may be in-sample (our inference). Likewise the 19 of 28 comparison in Fig 5a is the same K-record comparison that gates adoption (Sec 3.4, App A.4.2); the number of adopted candidates is not stated. We found no non-LLM / trivial forecasting baseline in the paper.
- Held-out sets exist for Polyglot coding (166 tasks, disjoint from modification and selection) and math grading (100 tasks); Table 1 lists none for paper review (train 100, val 100) or robotics (6 trials).
- Code: the paper prints an anonymous review-mirror link (p1 footnote, p10); it is shown on the poster as "Code (anon.)". candidates.jsonl lists no code_url.
- Median over five runs is the reported statistic; the paper gives no means or standard deviations (individual runs appear as plot dots in Figs 9–11 only).

## Judgment notes
- Batch 2026-10-19-a has `variance: unclear`. The full paper reports five complete runs per setting, medians, 95% run-level bootstrap intervals (Sec 4.1, App A.5) and per-run results (App B.3, Figs 9–11, Table 7), so variance is reported — though most intervals overlap and all Table 7 intervals include zero. A rating of `partial` would match the text better.
- scores.jsonl has `code_url: null`, while the judgment has `code: yes`; the paper prints an anonymous.4open.science link (p1, p10).
- Otherwise consistent with our judgment: `budget_matched: partial` (matched at the baseline's median cost; baselines' own mechanisms not matched outside Polyglot), `leakage_guard: untested`, `held_out: partial` (coding and math only).
- App B.4 / Fig 12: access to the diff reduces mean prediction loss relative to No-diff by 16.18% / 19.98% / 16.25% (blogs and poster use this direction).
- The donor IDM's evolution cost is not in Table 6 (which lists only the three conditions' own runs, and excludes initialization, held-out evaluation and post-hoc analyses), so Transferred IDM's 104.15M tokens and its matched-token AUBC exclude it.
- Author order on the poster follows p1: Zixuan Xie, Chang Xu, Yuhua Jiang, Li Zhao.
