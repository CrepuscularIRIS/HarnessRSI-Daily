# SOURCE — Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries

Read from: arXiv 2605.19576v3
Paper figures shown: none

License: CC BY-NC-SA (no figure reuse). The method diagram and the gain chart on the poster were drawn by us from the paper's table numbers; no figure of the paper is reproduced.

## Where the numbers come from
- Table 1 (all conditions: baseline, peak, gain, router %, active/retired, critic calls; p5), Table 3 (per-seed gain, p9), Table 2 (hyperparameters, p8), protocol Sec. 6.1 (p4), ablation text Sec. 6.3 (pp4–5), cost Sec. 6.4 (p5), Proposition 1 (p4) and proof sketch App. D (p8), limitations (p6), abstract (p1). Poster/blog numbers are table values; the text value "18.9%" (A4 router engagement, p3) is shown as 19 in Table 1.
- The paper has 9 pages; its appendices are A (architecture), B (hyperparameters), C (per-seed results), D (proof sketch).

## ‡ numbers (computed by us)
- 0.326‡ = 0.584 (late-window mean, abstract) − 0.258 (Default baseline, Table 1). The paper's +0.328 is computed within each run as mean(last 10) − mean(first 10) rounds (Table 1 caption), so it is not the difference of these two numbers.
- 45%‡ = (10k + 4.3k + 152)/10k − 1 = 44.5%, from the paper's own call breakdown (Sec. 6.4); the paper states 43% more calls than A1 and we quote that figure, noting the breakdown gives about 45%.
- 0.025‡ = 1/40, one eval task of the 40-task eval split (Sec. 6.1). Used to say that A4's −0.019 is smaller than one task.

## Notes
- Judged from the paper only; no code from the repository was read or run.
- Statements that something is "not run" / "not reported" (no condition without retirement, without the cap, or with an unbounded library; no other skill-library system as baseline; no compute-matched no-skill run; no leakage check; no statement of how the Default meta-skill was written or how the Default knob values were chosen) mean we found no such row, text or appendix item in the 9 pages of v3. "Bloat" is attributed to earlier systems on p3 and described as prevented in the Default by the cap.
- The Default is not the best-scoring row: A5 (+0.374), A6 (+0.363) and A8 (+0.372) have higher mean gain; the paper calls A5/A6 "within ±2σ at n = 3". Each A8 seed gain (+0.365, +0.355, +0.395; Table 3) is above each Default seed gain (+0.303, +0.340, +0.343) — a reading of Table 3, no new number.
- Internal inconsistencies, neutrally: the text says A4's bank "collapsed to 2 active skills by round 30"; Table 1 lists A4 as Active 2 / Retired 51 at round 100. Table 1's caption defines Baseline as round-0 pass@1 while Gain is last-10 minus first-10 mean.
- The paper uses one fixed-seed 60/40 split (Sec. 6.1) and does not describe resampling tasks per seed. Round-0 baselines for the same pipeline range 0.175 to 0.350 per seed (Table 3) and 0.200 to 0.300 across condition means (Table 1); the paper calls this sampling noise from n = 40 eval tasks.
- A1: Sec. 3.3 says the full pipeline (synthesizer, critic, curator) runs, but Table 1 lists Critic = 0 while A1 ends with 42 active / 15 retired skills; skills are born from critic-labelled failure clusters and retirement needs injection trials. We flag it and use Table 1 values.
- A4 changes two knobs (N_min 100 → 20 and τ 0.10 → 0.0) although the paper says each ablation modifies one knob; it attributes the harm to the evidence floor but does not separate the two.
- Hoeffding: the paper's ε ≈ 0.20 (N_min = 100) and 0.44 (N_min = 20) match sqrt(ln(2/δ)/(2n)) with δ = 10^-3 (our recomputation: 0.195, 0.436), i.e. a range-1 bound, whereas ĉ lies in [−1, 1]; the paper says A4 "validates Prop. 1" although A4 does not test the bound. Mentioned as one clause in the blogs; not on the poster.
- Held-out: skills are written from train-split failures (App. A); the paper is silent on whether eval-task capsules feed the Curator's contribution scores (Sec. 4.1 says only "capsules where s was injected").
- The SkillsBench figures (+0.0pp, +16.2pp) quoted in the paper come from another paper (Li et al., 2026); we do not report them as results of this paper.

## Judgment notes
No disagreement with our judgment (batch b14: evidence level `retained`, score 74): held_out yes, variance yes (3 seeds), budget_matched partial (extra critic/synthesis calls, 43% more calls than A1; no compute-matched control), optimizer_cost yes, retained_ablation yes (A1), improver_comparison yes (A8 refresh), cross_task no, leakage_guard unclear, code present. One observation, not a correction: the `retained_ablation` quote is A1 (injection off); no row of Table 1 removes retirement or the cap, so the paper's statement that these two are load-bearing rests on A4 (harsher retirement), A7 (looser cap, comparable mean +0.317 vs +0.328) and A3 (meta-skill removal) rather than on removal of retirement or the cap.
