# SOURCE — EvolvingBrain: An Adaptive Skill System for Multi-modal Agents Self-Evolution in Open Worlds

Read from: arXiv 2610.20786v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, bar chart and tables on the poster were drawn by us from the paper's table numbers. Authors per the PDF title block: Runxuan Liu*, Jingqi Shi*, Baoxin Wang†, Honghong Zhao, Haoyuan Xu, Yueqing Sun, Jiafeng Liang, Tao He, Dayong Wu, Qi Gu†, Shijin Wang, Ming Liu†, Bing Qin (* equal contribution, † corresponding). The poster header lists the first five and "et al. (13 authors)".

## Where the numbers come from (PDF pages)
- Method and keep rule: Sections 2.2–2.3 (pp3–6), Table 1 (p4); iteration cap, protocol, MMSkills handling: Appendix B (p11).
- Headline: Table 2 (p6) and Section 3.2 text (p6). Trap-Skill ablation: Table 4 (p13), text p7. Retrieval granularity: Table 5 (p13), text p7. Evolution iterations: Table 6 (p15), text p7–8. Out-of-domain: Section 3.4 (p8), Table 7 (p15). Splits: Appendix A.1 and Table 3 (pp10–11). Case study: Appendix C (pp11–12). Limitations: p9.
- 1.94‡ = 14.36 − 12.42 (Direct minus EvolvingBrain in-to-out-of-domain success drop, Section 3.4); 3.33‡ = 100/30 (one task of 30 held-out tasks, as percentage points, per run).
- Poster tables show Table 2, 4, 5, 6, 7 values directly; no value is read off a figure.

## ‡ numbers (computed or read by us)
- 15.35‡ = 73.02 − 57.67 (Qwen3.8-27B, VAB-Minecraft, Table 2); 6.80‡ = 68.52 − 61.72 (GPT-5.6-Sol, DiscoveryWorld, Table 2). Figures 3 shows the same differences as bar labels; the paper's text gives only the averages.
- 3.18‡ = 73.02 − 69.84 (EvolvingBrain minus MMSkills, Qwen, VAB-Minecraft, Table 2).
- 0.96‡ = 73.02 − 72.06, 0.61‡ = 58.02 − 57.41 (Qwen, VAB / DW, Table 5: adaptive minus the better fixed depth); 1.16‡ = 79.37 − 78.21, 1.23‡ = 74.07 − 72.84 (Kimi, VAB / DW). Figure 4 shows the same values (as losses of the other variants).
- 8.02‡ = 58.02 − 50.00, 10.49‡ = 74.07 − 63.58, 6.80‡ as above (in-domain DiscoveryWorld gains, Table 2; Figure 3 shows the same).
- "10.00 pp ≈ 3 tasks‡": 10.00 percentage points of 30 out-of-domain tasks = 3 tasks per run (the paper averages three runs, so the per-run reading is our inference).
- "73.02 = 138/189, 58.02 = 94/162‡": our reading of Table 2. The VAB-Minecraft success rates in Table 2 (57.67, 69.84, 73.02, 79.37, 68.78, 78.83, 70.37) are multiples of 1/189 (= 3 runs × 63); MMSkills on GPT (70.10) is not. The DiscoveryWorld in-domain rates in Table 2 (50.00, 58.02, 63.58, 74.07, 61.72, 68.52) are multiples of 1/162 (= 3 × 54). The text states 116 VAB-Minecraft test tasks (App. A.1) and 36 in-domain DiscoveryWorld test instances (Table 3), whose 3-run grids (1/348, 1/108) do not fit. Several values in Tables 4–6 fit neither grid. We cannot tell whether the paper evaluated different task counts, a subset, or uses a different averaging; we say only that they do not reconcile and use the table values.

## Notes
- Review-round edits: Table 4 ablates Trap Skill *retrieval* at test time only (library still built with Trap retries); Domain Skills feed memory update, gate and fusion in every variant (App. E prompts, Section 2.3), and Table 5 "coarse" retrieves only them; §2.2.1 (model-specific own trajectories) and App. A.1 (released VAB training trajectories, 90 task goals) are not reconciled by the paper; the flow diagram's ≤ 3 iteration loop is the Trap-retry / accept loop (steps 2–4), Domain Skills are derived afterwards (§2.2.5). Only Table 2 and 4 captions say "averaged over three runs". Several Table 4–6 values (75.27, 74.58, 66.38, 72.06, 68.68, 54.63) fit neither the 1/189 nor the 1/162 grid; held-out values fit 1/90.
- Limitations (p9) mention "online skill evolution" although the library is frozen at test time; Qwen and Kimi run at xhigh and GPT at high (App. B).
- "Three runs" in Tables 2 and 4 is not defined in the paper; no SD, CI or seed information appears anywhere (searched the body and Appendices A–E, including the prompt figures).
- MMSkills: "We evaluate MMSkills on VAB-Minecraft using its publicly released skills. We do not reconstruct its skill-generation process." It is therefore not the same mechanism applied to the same models' own trajectories.
- We found no cost, token or runtime figures for evolution or inference, and no ablation of the Structured Abstractive Memory, Domain Skills or the none/reuse/retrieve gate. The retry budget and the LLM used to write skills/memory are not stated in the text we read (searched for "teacher", "retry", "budget").
- Model names (Qwen3.8-27B, Kimi-K3, GPT-5.6-Sol) are as printed in the paper.
- Code: abstract says it is in the supplementary materials and will be released in the camera-ready version; candidates.jsonl has no code_url, so the poster has a paper QR only.

## Judgment notes
None. The full paper is consistent with our judgment (batch 2026-10-19-a): `variance: unclear` (three-run means, no SD), `budget_matched: partial` (same interaction budget, compute not matched), `optimizer_cost: unclear`, `improver_comparison: unclear`, `leakage_guard: untested`, `held_out`/`cross_task: yes` (two held-out DiscoveryWorld themes), `retained_ablation: yes`, `code: announced`.
