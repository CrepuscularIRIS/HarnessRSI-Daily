# SkillLens: skills can improve an agent—and a better skill can still be worse than no skill

*A Reel interpretation of [arXiv 2605.23899v1](https://arxiv.org/abs/2605.23899v1), **From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills**. HarnessRSI Daily score **65**, ★★, evidence level **retained**. Code: [microsoft/SkillLens](https://github.com/microsoft/SkillLens) (repository supplied by our board; the PDF links aka.ms/SkillLens).*

## What the system changes about itself

The retained artifact is a **domain-level procedural skill**, not model weights. A target agent first produces its own successful and failed execution traces. An extractor turns those traces, outcomes and rewards into a compact skill; the same target then receives the skill in its system prompt on new tasks. The study separates the ability to **extract** useful advice from the ability to **consume** it. Its main experiment uses one skill per target–extractor–domain combination, not a large retrieved skill library.

## The loop, and the keep/reject rule

1. Collect the target's trajectories on an experience-generation split, over multiple rounds.
2. Extract up to **3** success or failure patterns per trajectory. The prompt asks for transferable patterns without task-specific filenames, identifiers, error messages or API calls, and allows an empty list when nothing useful is found.
3. Merge pattern sets in groups of **10**, deduplicating, generalizing and dropping vague or low-value patterns at the extractor's discretion.
4. Synthesize one skill with a **3000-character** limit. Schema and length constraints are enforced; length errors lead to shortening and retry.
5. Inline the skill in the same target's system prompt and measure its change against the no-skill target on the same test split.

**There is no reported downstream-score acceptance gate.** Quality rejection is prompt-directed during extraction and merging, plus structural validation—not a test that the final skill improves utility before retaining it. Harmful skills are evaluated too. This is an extractor-assisted single-step update, not evidence of an indefinitely improving deployment loop.

## Headline result, as reported

Table 1 spans **five domains, six targets and five extractors**. The domains are ALFWorld, SpreadsheetBench, SWE-bench-Verified, SEAL-0 and the multi-turn BFCL-v4 subset. Targets come from GPT, Gemini and Qwen; Qwen3.5-9B is excluded as an extractor because it could not reliably follow the extraction protocol. The authors summarize the matrix as **75% positive and 25% negative transfer**, with negative transfer most frequent on ALFWorld (**47%**).

All Table 1 entries, **including the no-skill baselines**, average **three independent evaluation runs**. No per-cell standard deviation or confidence interval accompanies these means. TE averages each target's gain across extractors; EE averages each extractor's gain across targets, whose experience pools differ.

| Table 1 comparison | Reported gain (percentage points) |
|---|---:|
| GPT-5.4 target, SpreadsheetBench TE | +9.66 |
| Qwen3.5-9B target, SpreadsheetBench TE | +1.46 |
| Gemini-3.1-Flash-Lite extractor, SpreadsheetBench EE | +5.86 |
| GPT-5.4 extractor, SpreadsheetBench EE | +1.67 |
| GPT-5.4 target, ALFWorld TE | +4.93 |
| Gemini-3.1-Flash-Lite target, ALFWorld TE | −1.59 |

The intervention is a **meta-skill in the extractor prompt**: encode failure mechanisms, provide actionable specifics, and blacklist high-risk actions. In Table 11 it improves all **nine** evaluated conditions relative to the **original extracted skill**, averaging **+1.55 pp**. The generic seven-dimension plausibility rubric instead averages **−0.59 pp**, hurting six conditions. The largest improvements are concentrated in **SpreadsheetBench** (**+2.33, +3.58, +3.69 pp**); ALFWorld and SWE-bench gains are smaller. **Table 1 explicitly averages three runs; Table 11’s separate run/seed aggregation and extractor identity are not specified.** Table 11 also provides no per-cell uncertainty; this does not establish that it is single-run.

## The controls that decide whether the gain is real

- **Experience/test separation.** The paper uses a **1:1** experience/test allocation. Where an official training split exists, experience tasks are sampled from it; otherwise instances are randomly partitioned with a fixed seed. Splits are shared across model combinations. The PDF does not give per-domain task counts, numerical pool sizes or the split seed. These are same-domain held-out tasks, not a demonstrated cross-domain skill transfer.
- **Same skill, different consumers.** Section 5.3 fixes GPT-5.4-mini as extractor and transfers two SpreadsheetBench skills, distilled respectively from GPT-5.4 and Qwen3.5-9B experience, to all six targets. The strong-pool skill helps every target, ranging from **+1.8** on Gemini-3.1-Pro to **+9.5** on Qwen3.5-35B. The weak-pool skill causes **−2.0** on GPT-5.4. This fixed-text comparison complements Table 1, where both consumer and source experience change.
- **Experience composition and format.** Section 5.1 changes success/failure mixtures with a fixed extractor across three domains and three targets; the best mixture depends on the domain. Appendix C rewrites skills into four formats, verifies semantic preservation and evaluates each for three rounds. Format effects are not detected (**all p > 0.34**), while extractor effects are significant for five of six targets in that control. Table 8's target roster includes GPT-5.2 and GPT-5.4-nano; it is not identical to Table 1's roster. Its round-noise statistics are not uncertainty intervals for the headline matrix.
- **Judge improvement is not independent validation.** GPT-5.4 judges **151** skill pairs with utility gaps above **0.5 pp**, using nine votes and randomized presentation order. Utility-grounded guidance raises accuracy from **46.4% to 73.8% on the same pairs**. The rubric was discovered from high-gap main-matrix pairs and screened using utility; no independent rubric-development/test split is described. Our reading: this is useful diagnostic feedback, not an untouched-test estimate of a general skill-quality judge. The subsequent meta-skill experiment also reports no separate benchmark holdout reserved for rubric design.
- **Baseline access and budgets.** The no-skill baseline is the same target without the extracted skill, evaluated on the same split—not a baseline granted an equivalent retrieved library. Original, plausibility-guided and utility-guided extraction use the unified extraction framework; the main protocol directly injects one skill, without retrieval. The paper does not report a compute-matched extra-inference baseline, baseline tuning budgets, or which split selected the extraction defaults. It discloses API access, medium reasoning for GPT/Gemini and local Qwen hardware, but not trajectory-collection, extraction or rubric-discovery tokens, dollars or wall time. The library-building cost therefore remains unquantified.
- **Leakage boundary.** Extraction uses experience-split traces and asks for task-specific details to be removed. No measured audit for evaluation-task overlap or near-duplicate/task-relative leakage is reported. Related tasks could still share procedural specifics; that is a limitation of what is established, not evidence that contamination occurred. Rubric design's use of downstream utilities is a separate issue from direct test-task inclusion in skills.

## Where the gain is absent or small

- **Improving a skill does not ensure improvement over no skill.** Table 11's ALFWorld Qwen3.5-35B scores **57.21 no skill → 53.73 original → 54.11 validated**. SpreadsheetBench's row labelled Gemini scores **37.50 → 33.17 → 36.75**. Both validated skills still trail their own no-skill controls. We preserve Table 11's Gemini label; its exact alignment to Table 1 is unresolved (SOURCE.md).
- **The validated rubric is not best in every comparison.** On SWE-bench's Gemini row, plausibility guidance scores **70.96**, above validated guidance at **70.58**. “All nine improve” means relative to Original, not relative to every competing condition.
- **Small or negative averages remain.** SWE-bench Qwen3.5-9B TE is only **+0.37**; SEAL-0 Gemini-3.1-Pro TE is **−1.04** (Table 1). Without cell uncertainty, small positive means are not established significant wins.
- **Alternative harnesses are mixed.** Appendix F evaluates SpreadsheetBench with Claude Code and Codex, reporting **+0.4 pp** overall. TE is **−0.5** for Claude Code Opus 4.6, **+2.3** for Sonnet 4.6, **+0.7** for Codex GPT-5.4 and **−1.0** for Codex GPT-5.4-mini. This is a narrow harness check, not a broad guarantee for skill libraries in production.

## Our read

**Score 65 · ★★ · retained**, as recorded on the board. The paper reports same-domain held-out evaluation, three-run means for Table 1, format/experience controls, cross-model fixed-skill transfer, alternative harnesses and a comparison of extraction guidance. It does not report per-cell uncertainty in the main results, cost-matched baseline gains, library-building cost, an overlap audit, or independent validation of the utility-selected rubric. Table 11’s separate run/seed aggregation and extractor identity are not specified. Appendix C does quantify round noise; it would be inaccurate to say there is no variance analysis anywhere.

The practical takeaway is narrower than “skills work”: **utility depends on the experience source, extractor and consumer; concrete remedies help, but the acceptance criterion must remain downstream behavior rather than plausible prose.** Even the improved meta-skill can leave an agent below its no-skill baseline.
