# SOURCE — EffiSkill: Agent Skill Based Automated Code Efficiency Optimization

Read from: arXiv 2603.27850v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, chart and tables on the poster were drawn by us from the paper's numbers. Authors as in the PDF title block: Zimu Wang, Yuling Shi, Mengfan Li, Zijun Liu, Jie M. Zhang, Chengcheng Wan, Xiaodong Gu. The paper links no code repository (code_url is null in our records); p11 gives a Zenodo data/artifact DOI (10.5281/zenodo.19249527), which we cite in the blogs but did not turn into a code QR.

## Where the numbers come from (PDF pages)
- Stage I / II description, 29 operator skills, merge threshold 0.8, 3 skill sets, 2–3 plans: pp4–5, p9 (RQ4).
- Mining corpus 900 + 900 pairs, ratio ≥ 2, overlap statement, EffiBench-X 623 tasks, public/private 20/80 split with seed 42, baselines, k = 8, OPT@k definition, three executions per candidate: pp5–6.
- Table 1 (headline, significance markers *, †): p6. Fig. 4–6: p7. Table 2 (ablation) and Table 3 (skill families): p8. Case study 3838.11 ms / 1434.23 ms: pp9–10. Threats to validity: p10. Data availability: p11.

## ‡ numbers
Computed by us from Table 1 / Table 2 values (differences of printed numbers):
- 5.29‡ = 26.48 − 21.19 (GPT-5-mini Python OPT@1, vs FasterPy); 5.30‡ = 21.35 − 16.05 (Qwen Python OPT@1, vs CoT); 5.78‡ = 34.19 − 28.41 (Qwen C++ OPT@1, vs SBLLM). The fourth OPT@1 gap, 3.69 = 44.62 − 40.93 (GPT C++, vs CoT), is printed in the abstract. The poster/blog range "3.69–5.78‡" is the min/max of the four OPT@1 gaps.
- OPT@8 gaps 4.98 (37.40 − 32.42), 12.03 (66.77 − 54.74), 8.35 (36.60 − 28.25), 12.52 (56.50 − 43.98) are printed in the paper (Sec 5.3, intro, abstract) and match Table 1.
- 0.16‡ points = 1/623 of tasks (623 tasks per language; Fig. 5 panels each sum to 623: 455+26+142, 401+41+181, 348+34+241, 313+103+207; 26.48% = 165/623 and 18.62% = 116/623 checked). "About 23 tasks‡" = 3.69 pp × 6.23.
- 62.60‡ = 100 − 37.40 and 63.40‡ = 100 − 36.60 (Python OPT@8 of EffiSkill, so the share of tasks with no qualifying candidate at k = 8).
- Fig. 5 wins / ties / losses (455 / 26 / 142, 401 / 41 / 181, 348 / 34 / 241, 313 / 103 / 207) are read off the stacked-bar labels of Figure 5 (p7) and checked against the rendered page; they are not in the text.

## Notes and internal inconsistencies (we use the table values)
- Intro (p2) gives the Qwen3-Coder gains as 12.36 (C++) and 8.67 (Python), and the RQ3 answer box (p8) says "up to +12.36". Table 1 and the Sec 5.3 body give 12.52 and 8.35 (OPT@8 vs SBLLM 43.98 and FasterPy 28.25); the abstract's "3.69 to 12.52" matches the table. We use the table values. Within the Qwen3-Coder rows, no baseline row on either metric gives a gap of 12.36 or 8.67. Coincidences, for what they are worth: 8.67 is SBLLM's own Qwen Python OPT@8, and also equals the GPT-5-mini Python OPT@8 gap to CoT (37.40 − 28.73) — a different model from the one the intro names; 12.36 equals the Qwen "w/ Random Skills" OPT@1 in Table 2. We do not claim any of these explains the text.
- Fig. 5 caption says "strongest non-EffiSkill baselines". The comparators drawn are SBLLM (Python / GPT-5-mini), EffiCoder (Python / Qwen), CoT (C++ / GPT-5-mini), Instruction (C++ / Qwen). By Table 1 OPT@1 and OPT@8 the highest baselines are FasterPy, FasterPy / CoT, CoT, SBLLM respectively; only the CoT panel matches. The paper does not define "strongest" for the figure or say what a "win" compares, so it may use another criterion. We state it as a mismatch with Table 1, not as an error.
- Top-5 skill share: Sec 5.4 gives 68.3% (GPT-5-mini) and 70.0% (Qwen); Sec 6.1 gives "68.0–69.7%"; the RQ4 box gives "68.0–70.0%". Minor; not used on the poster.
- Table 2 (p8) has no language label and the Sec 5.2 text gives none; its "EffiSkill" rows equal the Python cells of Table 1 (26.48/37.40, 21.35/36.60), so we READ it as Python (inference). We found no C++ ablation. "One value per cell / no repeated runs" is also our reading of what the paper reports: it never says "single run", it describes no repeated generation runs or seeds, and it averages 3 executions per candidate for runtime noise (p6).
- "Cross-language transfer" (RQ3, Sec 4.1/5.3): the paper reports one mining corpus of 900 Python + 900 C++ pairs (p5) and one 29-skill library (p9); the skill cards in Fig. 2 have a `language` metadata field. It never says whether the library is pooled across languages or built per language. All we state: C++ pairs are in the mining corpus, so the C++ result is not zero-shot transfer of Python-mined skills. The RQ3 answer box says: "EffiSkill generalizes across Python and C++ at the framework level."
- "Execution-free" means no candidate execution inside generation. All methods then pass the same public-test filter/rank step (20% of each task's tests), which does execute candidates.
- Not found in the paper (we searched the full text for tokens, cost, seed, temperature, variance, contamination; there is no appendix in v1): per-task tokens/LLM calls or wall-clock; Stage I cost; sampling temperature; repeated generation runs or seeds; backbone-contamination discussion; method of the mining/benchmark overlap check; choice procedure for merge threshold, 3 skill sets, 2–3 plans; number of Meta Skills; which model performs the post-trace distillation and merge steps (gpt-5.1 is named only for trace extraction).
- Ablation reading: only "w/o Retrieval" removes skills altogether (it generates directly from the diagnosis brief, no composed plans, Sec 5.2); "w/ Random Skills" and "w/o Multi Plans" still use skills. The paper's conclusion is "Together, these components account for the gains". All six ablated OPT@8 values are below plain Instruction OPT@8 (31.62; 24.40), which is equally consistent with degraded pipelines. The paper does not say how 8 candidates arise from 3 skill sets × 2–3 plans.
- Table 2 oddity: GPT-5-mini "w/ Random Skills" OPT@8 = 27.82 is not a multiple of 100/623 (173/623 = 27.77, 174/623 = 27.93); every other Table 1/2 value is. Possibly a typo; used as printed.
- Related Work (p10) says each skill is "validated offline via execution feedback"; Sec 3 describes no such validation step beyond the mining pairs being filtered by speed-up ratio ≥ 2 (Sec 4.2). We say only that the library has no keep/reject loop at inference.
- Our own characterisations, not the paper's: SBLLM as a "weakened adaptation" (the paper says it adopted a single-iteration variant without execution-based selection "for fair comparison"); "none of the baselines receives the mined library or gpt-5.1 traces" (the paper describes none as doing so); "several stages" for EffiSkill (the paper does not state LLM calls). EffiCoder: the paper does not say whether it was fine-tuned by the authors or a released checkpoint, nor on which data.
- Poster Table 1 column "OPT@1 best baseline": GPT Python FasterPy 21.19, GPT C++ CoT 40.93, Qwen Python CoT 16.05 (FasterPy's is 13.96), Qwen C++ SBLLM 28.41; the OPT@8 bars use FasterPy / CoT / FasterPy / SBLLM.
- Poster charts show Table 1 values only (OPT@8 bars; OPT@1 as printed numbers).

## Judgment notes
Judgment batch b01 (research/judgments/b01.jsonl): variance unclear, budget_matched partial, optimizer_cost unclear, retained_ablation unclear, leakage_guard tested, held_out yes, cross_task yes, evidence level retained. Notes from the full paper (judgment files not edited):
- `retained_ablation: unclear` — Table 2 does remove ("w/o Retrieval") or randomize ("w/ Random Skills") the retrieved skills and reports the drop, on Python only, single runs, no SD. This looks closer to `yes` than `unclear`.
- `leakage_guard: tested` rests on one sentence stating a no-overlap check between mining corpus and EffiBench-X tasks; the method is not described, and the authors themselves say "some distributional similarity may remain" (p10).
- `variance: unclear` is consistent: the only statistics are a paired bootstrap over tasks; no repeated runs.
- `code: 10` in scores.jsonl comes from the Zenodo artifact DOI; code_url is null.
