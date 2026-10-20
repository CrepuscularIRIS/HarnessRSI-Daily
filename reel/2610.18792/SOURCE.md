# SOURCE — SEAR: Self-Evolving Agentic Robotics

Read from: arXiv 2610.18792v1
Paper figures shown: none

License: arXiv default (no figure reuse). The method diagram, charts and tables on the poster were drawn by us from the paper's numbers.

## Where the numbers come from
- Table 6 (library vs no library per model and family, p20; ¶ cells have two runs), Table 5 (session and library terms, p20), Table 7 (library vs rerun noise, p21), Table 3 (tiers, p9), Table 4 (hardware, p12), Figure 6 labels (library gain by capability bin, p8), §3.2 (crossover 46.9 / 42.4 / 60.6 / 55.7, p8; Appendix A.3), §3.3 (persisting mistakes, p9), §4.1 and §4.3, §4.4 (hardware, p11), Appendix A.8 (limitations, pp24–25).
- The poster's DeepSeek-v4-flash RoboLab bars use the first 58 tasks only (Vanilla 26.6, Lineage 30.7; Table 6 footnote), because its runs stopped when the model was retired.

- Added after independent check (all verified in the paper): best-of-3 caveats and submission rates (§3.1 p7; Appendix F p31: BO3 attempts on LIBERO-family tasks are told their 20-minute limit, selecting by validation "overstates the winner", restarts should not be "interpreted as equal compute", Lineage's "experience used to construct the library remains part of the lineage's history"); one-run auto-research (§2.4 p6, Appendix A.8 p24); Table 3 caption (T5 "not a transfer result", p9); crossover scope (Appendix A.3 p21); leakage findings (Appendix A.9 p25); Table 7 numbers are shares of comparisons (p21); capability-band means and fitted curve (Fig. 6 p8).

## ‡ numbers (computed by us)
None. Every number is printed in the paper.

## Notes
- The code link on the poster (github.com/Self-Evolving-Agentic-Robotics/SEAR) is the one printed in the paper's contributions list (p4); `candidates.jsonl` has no code URL for this paper. We did not open or run it.
- All hardware numbers are one practice run per agent (Table 4, Appendix A.8); we say so on the poster and in both blogs.

## Judgment notes
- Code: our judgment batch 2026-10-19-a records the code as "announced" (score code = 3) and `candidates.jsonl` has `code_url: null`, but the paper itself prints a GitHub URL (p4, contributions). The URL was not verified. No judgment file was edited.
- Everything else is consistent with the full paper: `budget_matched: partial` (matched in wall-clock time, not compute, Appendix A.8), `improver_comparison: unclear` (the harvest/keep rule is not varied or compared), `leakage_guard: tested` (Appendix A.9 audit).
