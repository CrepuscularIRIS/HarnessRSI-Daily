# SOURCE — PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

Read from: arXiv 2608.04003v1
Paper figures shown: none

License: arXiv non-exclusive distribution (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from (page numbers are PDF pages)
- Table 2 (Hermes, seven models, p8); Table 3 (fixed MiniMax-M2.7, frameworks, p9); Table 4 (single-mechanism ablations, p12); Table 5 (focused Procedural diagnostic, p12); Table 6 (Hermes+ on five models, p13); Section 4.4 text on run-to-run variation (p12) and Table 11 (p30); Table 7 (episode counts, p19); Table 8 (judge validation, p26); Table 9 (Codex CLI / Claude Code, p28); Table 10 (per-family, pp29-30); Table 12 (cost, p31); Appendix C.1 (Agent-Zero 1,200 s budget, adapters, pp26-27); Appendix A.2 (task construction, pp19-20); Section 6 (limits, pp13-14).
- Figures 9 and 10 (heatmap, frontier) repeat Table 4 / Table 3 values and are not reproduced.

## ‡ numbers (computed by us)
- −0.17‡ = 0.38 (Hermes+ Procedural persistence-on score) − 0.55 (Hermes), Table 4 / Table 11.
- Token ratios Hermes+ / Hermes per episode (Table 12): 0.90‡ = 11,218 / 12,473 (DeepSeek-V4-Pro); 1.5‡ = 13,504 / 8,964 (GPT-5.4); 1.84‡ = 10,203 / 5,551 (Sonnet 4.6); 0.55‡ = 11,022 / 19,986 (Opus 4.6). The ≈2.5× on MiniMax-M2.7 (31,859 / 12,615) is stated by the paper.
- Poster: "Update Δ changes by −0.05‡ to +0.05‡" on the other four models = Hermes+ (Table 6) minus Hermes (Table 2): DeepSeek 0.13−0.18 = −0.05, GPT-5.4 0.31−0.34 = −0.03, Sonnet 0.33−0.29 = +0.04, Opus 0.33−0.28 = +0.05.

## Statements derived by us from table comparisons (no new numbers)
- "Each single-mechanism row has a lower Overall persistence-on score than Base Hermes": 0.62, 0.60, 0.51, 0.55, 0.55 vs 0.66 (Table 4).
- "E4 alone Overall Δ +0.17 is above all five together (+0.15)": Table 4.
- Update Δ on the other four models, Hermes (Table 2) to Hermes+ (Table 6): DeepSeek-V4-Pro 0.18 to 0.13, GPT-5.4 0.34 to 0.31, Claude Sonnet 4.6 0.29 to 0.33, Claude Opus 4.6 0.28 to 0.33.
- Mech, Hermes (Table 2) to Hermes+ (Table 6): DeepSeek 0.71 to 0.69, MiniMax 0.64 to 0.73, GPT-5.4 0.80 to 0.80, Sonnet 0.76 to 0.77, Opus 0.70 to 0.70.
- The Overall-Δ range "+0.13 to +0.24" and capability ranges (Memory +0.23 to +0.37, Procedural +0.03 to +0.19, Info +0.05 to +0.11, Update +0.12 to +0.36) are min/max over the seven Hermes rows of Table 2.
- "Judge = tuning model": the judge is MiniMax-M2.7 (App. B.4) and Hermes+ was tuned on MiniMax-M2.7 (S4.4); the paper does not discuss whether this matters.
- "No held-out split for the Hermes+ design": Section 4.3 derives the five mechanisms from low-gain traces of the benchmark's own runs and Section 4.4 evaluates on the same benchmark; the paper describes no separate test set. "Control-episode scores are not tabulated": the controls (no-retention, distractor, stale, wrong-mechanism) and cold episodes are described in Sections 3.1-3.2, but no table reports their scores (checked text, tables, Figures 9-10).

## Inconsistencies in the paper (reported neutrally; table values used)
- Table 2's caption says results are "average across 3 runs" for all seven models; Appendix D.5 says "Two configurations have three independent runs: Hermes/MiniMax-M2.7 and Hermes+/MiniMax-M2.7". Only those two have an SD (Table 11).
- Table 5 (focused Procedural diagnostic): Base Hermes +0.087 and Full Hermes+ +0.085, whereas Tables 4/11 give Procedural Δ +0.05 and −0.02 for the same two systems; the paper says Table 5 is "a focused diagnostic rather than a full-benchmark estimate" but not which subset or runs.
- Table 10: rows PC01_sop_bootstrap_05 and _06 are identical in three of four cells (Hermes 0.488 / +0.117; Hermes+ w/ 0.231) and differ only in Hermes+ Δ (+0.022 vs −0.005); not commented on.
- Section 4.4 calls Hermes+'s Procedural result "declines slightly"; Table 4/11 show persistence-on 0.55 to 0.38.
- Per-family counts are 7-8 episodes (Table 7), each averaged over three runs (Table 10 caption).

## More reading notes (added after independent check)
- Update gain: Table 10 shows five of seven Update families rose (fact correction −0.078 to +0.492, SOP patch 01 +0.041 to +0.163, rule migration +0.135 to +0.226, temporary-exception pollution +0.034 to +0.235, scoped rule migration +0.354 to +0.502) and two fell (recall-then-modify +0.347 to +0.190, SOP patch 02 +0.017 to −0.127); fact correction has the largest rise. Wording is "dominated by one family", not "concentrated".
- Runs: Appendix B.1 says "Each episode is run across three independent trials"; Tables 9 and 10 say "means over three runs". This may be what Table 2's "3 runs" refers to, but the paper does not say whether trials or full-suite runs are meant, and it names no headline seed (matched on/off pairs share "the same seed"; Table 4 Base and Full equal the Table 11 means; not stated for Tables 3, 4, 6 generally).
- Why Hermes+ mechanisms were not added: Appendix C.1 gives the overlap-with-own-persistence-stack rationale for Agent-Zero and nanobot only; for ZeroClaw it states only that the adapters do not add them; Hermes was chosen because it "directly exposes" the loop and persistence surfaces.
- Limits (Table 15): Hermes/Hermes+ 50 iterations and 300 s; nanobot 30 iterations and 300 s; ZeroClaw recursion limit 100 and 300 s; Agent-Zero 1,200 s. A timed-out or crashed episode scores zero and is not rerun; the paper reports no timeout counts. It writes both that the Agent-Zero budget is "a methodological footnote rather than a fairness adjustment" and that "Agent-Zero is competitive on score given enough budget", yet its Overall Δ is −0.08.
- Token cost: the ≈2.5× holds on MiniMax-M2.7 only (ratios elsewhere above, ‡). ZeroClaw (43,955) and Agent-Zero (53,100) tokens/episode are above Hermes+ (31,859) with Overall Δ +0.12 and −0.08; nanobot (10,905) ties Hermes on Δ (+0.13). The paper says wall-clock rose only 1.10× because the extra tokens are mostly added to system-prompt context rather than generated output.
- "No verifier described" is our reading from absence. Figure 3 shows E5 with a "Background Review" step (reusable workflow? corrected method? max iterations 15) and a memory flush; the paper does not describe either as a verifier or filter.
- E4 (Figure 3, Section 4.3): the gate "withhold[s] once and inject[s] a synthetic message" and "blocks a draft answer when the task depends on prior state and no persistence read has occurred, then requires a read"; the poster wording follows this and does not claim an enforced guarantee.
- Mech by construction (our reading): E1 and E4 force reads; E2, E3, E5 force typed writes; Mech's recall term (Eq. 2, Appendix B.3.2) credits an evaluation episode only if it fired the expected retrieval signal. Part of the Mech rise (0.64 to 0.73) may therefore follow from the design. The paper says Mech measures consistency with an expected pathway rather than causal necessity.
- Task generation (Appendix A.2): tasks, graders and expected artifacts were generated with Codex (GPT-5.4) and Claude Code (Claude Opus 4.6) and checked by three authors; GPT-5.4 has the largest Overall Δ in Table 2 (+0.24). The paper does not test generator effects.

## Judgment notes
Our judgment (batch b12): evidence level `retained`, `variance: yes`, `held_out: partial`, `budget_matched: unclear`, `optimizer_cost: partial`, `leakage_guard: tested`, `improver_comparison: yes`. The full paper is consistent with all of these except one nuance: `leakage_guard: tested` rests on the described control-episode design (no-retention, distractor, stale, wrong-mechanism controls), but the paper reports no control-episode scores, so the guard is described rather than shown with numbers. Also, `variance: yes` applies only to Hermes and Hermes+ on MiniMax-M2.7 (three runs); no other row has an SD. Judgment files were not edited.
