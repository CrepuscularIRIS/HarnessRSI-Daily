# SOURCE — Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents

Read from: arXiv 2604.14004v1
Paper figures shown: none

License: CC BY 4.0 (figure reuse allowed), but the poster uses no paper figure: the method diagram, charts and tables were drawn by us from the paper's numbers.

Authors (PDF title block): Kangsan Kim, Minki Kang, Taeil Kim (KAIST); Yanlai Yang, Mengye Ren (NYU); Sung Ju Hwang (KAIST, DeepAuto.ai).

## Where the numbers come from
- Table 1 (headline, p5, Pass@3), Table 2 (memory baselines, p5, Pass@3), Table 4 (abstraction, p7), Table 6 (cross-model, Pass@1, p9), Table 7 (retrieval, Pass@3, p9), Table 8 (Pass@1, appendix A, p13), Figure 3 (benefit categories; only the 5.5% stated in the text, p6), Figure 6 (scaling, p9; described qualitatively, read off the figure, no values quoted). Setup: Sections 3.1-3.2 (pp3-4), Section 4.1.2 (p5).
- Pool/format/retrieval description: Sections 3.1.1-3.1.2; models and tools: Section 3.2.2.

## ‡ numbers (computed by us)
- 0.534‡ / 0.578‡ = plain mean of the six per-benchmark columns of GPT-5-mini zero-shot and MTL (Insight), Table 1: (0.910+0.470+0.730+0.315+0.111+0.667)/6 and (0.930+0.470+0.770+0.360+0.189+0.750)/6. They differ from the Table 1 Avg. (0.523 / 0.560).
- 491‡, 18‡, 7‡, ~12‡ (task counts): the paper states no benchmark sizes (only "randomly sample 100 tasks if the total number of sample is over 100", p4). Counts of 100/100/100/89/90/12 (LiveCodeBench, Aider-Polyglot, SWE-Bench Verified, Terminal Bench 2, ReplicationBench, MLGym) make every Pass@3 cell of Table 1 an integer fraction (e.g. 0.315 = 28/89, 0.111 = 10/90, 0.667 = 8/12), and reproduce the Avg. column of all nine Table 1 rows exactly as a pooled average over 491 tasks (e.g. 257/491 = 0.523 and 275/491 = 0.560 for GPT-5-mini zero-shot and Insight). This is our reading, not a statement of the paper. Under it, GPT-5-mini Insight vs zero-shot is +2, 0, +4, +4, +7, +1 tasks = 18 of 491; MLGym 0.667 -> 0.750 is 8 -> 9 of 12. DeepSeek V3.2 +13 tasks, Qwen3-Coder +9 (not shown).
- 1 and 2 tasks of 100 (blog): 0.930 vs 0.920 and 0.770 vs 0.750 (Table 2); these are percentage differences expressed in the stated 100-task samples (the paper states the cap of 100).

## Notes and paper inconsistencies (neutral)
- Averages: Table 1 "Avg." is a task-pooled average over 491 tasks (our reading, above); Table 8's Avg. also reproduces as a pooled average (denominators 3N; GPT-5-mini zero-shot 0.435 pooled vs 0.446 plain, printed 0.435). Table 2 (0.584 = mean of 0.910, 0.730, 0.111), Table 4, Table 6 and Table 7 use plain means of their columns. The aggregation differs between tables and is not stated in the paper.
- The text says Insight gives "more than 4.0% (up to 8.3%)" gains on four benchmarks; SWE-Bench Verified is exactly +4.0 in Table 1 (so "at least 4.0").
- The text (Section 4.4.4) says cross-model transfer "consistently underperforms" self-generated memory; in Table 6 the Qwen3-Coder target has 0.413 for both GPT-5-mini memories and its own. The memory format of Table 6 is not stated (our reading: Insight, since the GPT-5-mini row equals Table 8 MTL (I): 0.877 / 0.633 / 0.119).
- Section 4.4.3 says "using 9 domains yields the best overall performance" and Figure 6 has an axis 0/2/5/9; the paper evaluates six benchmarks and excludes the target from the pool (= 5 source benchmarks). It does not explain the 9. Figure 6's full-pool point equals the Table 6 GPT-5-mini self row vs zero-shot (0.543 vs 0.515; ReplicationBench 0.059 -> 0.119).
- "Pass@3" is not defined in the paper; Section 4.1.2 says each model is evaluated over three runs. We say "three runs" and do not state how Pass@3 is computed. Appendix A is titled "Average Pass@1"; we call it Pass@1 and do not claim how it is averaged.
- Table 4 does not name the model or the metric; we say so and give our reading (GPT-5-mini, averaged Pass@1; its Avg 0.523 coincides with Table 1's zero-shot Avg only by value).
- Table 2 does not name the model; the MTL row equals the GPT-5-mini Table 1 Insight cells (0.930, 0.770, 0.189) and the zero-shot row the GPT-5-mini zero-shot cells.
- Headline choice: the +3.7 delta is Insight vs zero-shot; Table 1 reports all four formats on the same test tasks and its caption notes "Among memory types, Insight achieves the highest average performance". No dev/validation split for format selection is mentioned anywhere; DeepSeek V3.2 and Qwen3-Coder were run with Insight only. We state this in the blogs and on the poster.
- No random/irrelevant-memory or generic-hint control exists in the paper (searched; the pool-size variants of Figure 6 subsample the same cross-domain pool, and No Memory / reranking / rewriting / AgentKB / ReasoningBank / cross-model are the only other conditions), so we list it under "does not report".
- Table 6's Qwen3-Coder-target tie (0.413 vs 0.413) is exact only at the printed precision; we say "at the printed precision".
- Code URL provenance: https://github.com/KangsanKim07/MemoryTransferLearning is not in the paper (the PDF links only https://memorytransfer.github.io/); it comes from reel/candidates.jsonl and research/scores.jsonl (code_url), and the poster's Code QR uses the same source.
- Searched the whole text including the appendix for: seed, variance, standard deviation, confidence, cost, token, leak, overlap, contamination, dedup, limitation. Found: none of these as reported results (no variance, no cost, no leakage check; no limitations section, only an Impact Statement). So "does not report" on the poster means "not found in the paper".
- Source/target tasks: "same sampled tasks" is our reading of Section 3.1.1 (trajectories come from running the agent on all benchmarks).
- Figure 5 (DBI/LISI) values and the other Figure 3 percentages are bar/figure labels and are not quoted.
- 391‡ / 401‡ = 491 − 100 and 491 − 90 under the task-count reading: the source-pool sizes implied for a target of LiveCodeBench / SWE-Bench (391) or ReplicationBench (401). Table 2's "431 memories" matches neither, and Figure 6's "9 domains" point sits at the same value as the "Full" pool although only six benchmarks are evaluated; the paper does not explain either number, so the pool composition is our reading.
- about one task of 90‡ = 0.200 (18/90) vs 0.189 (17/90), AgentKB vs MTL on ReplicationBench, Table 2; about five tasks of 100‡ = 0.770 vs 0.720, MTL vs AgentKB on SWE-Bench, Table 2; both under the task-count reading.
- +2.8‡ = 0.543 − 0.515 (Table 6, GPT-5-mini own memories vs zero-shot), the full-pool gain also shown in Figure 6.

## Judgment notes
None. The full paper is consistent with our judgment (batch b11): held_out yes, cross_task yes, retained_ablation yes; variance, budget_matched, optimizer_cost, improver_comparison and leakage_guard unclear (none found); evidence level retained; score 67, band ★★ (research/scores.jsonl).
