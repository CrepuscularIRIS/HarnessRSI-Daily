# M⋆: a coding agent rewrites an LLM agent's memory — and the gain depends on which control you read

*A Reel interpretation of [arXiv 2604.11811v2](https://arxiv.org/abs/2604.11811v2) (HarnessRSI Daily score 90, ★★★). Code: [wbopan/mstar](https://github.com/wbopan/mstar).*

## What the system changes about itself

M⋆ treats an agent's **memory harness** as a program. A memory program is a Python module with a fixed interface: a **Schema** (dataclasses for what is stored and queried), a **Logic** part (`write()` / `read()`, which may use SQLite, a vector database or an LLM call), and **Instruction** strings that tell the task agent how to extract, query and read memory. All three are edited together; the paper searches over the harness itself, not over a hand-picked set of modules.

## The loop, and the keep/reject rule

1. Start from three simple seed programs.
2. Sample a parent from the pool by softmax over its static-validation score (τ = 0.15).
3. Run the parent on a rotating batch of 5 validation items; its failed and successful trajectories, plus the change logs of earlier iterations, go to a coding agent (GPT-5.3-Codex) that writes a code patch.
4. Compile and runtime checks (output ≤ 3000 characters, ≤ 60 s, smoke test). A failing child goes back for automatic repair, up to 3 attempts, then is discarded.
5. Score the child on the static validation set and add it to the pool.

After 20 iterations the best program on validation is evaluated once on a held-out test split. The task agent is GPT-5.4 Mini. Nothing about the model weights changes: the retained artifact is code.

## Headline result, as reported

Across four benchmark families (seven configurations) and nine baselines, M⋆ has the best score on 7 of 8 reported metrics (Table 1), with relative improvements "up to 31%" over the best baseline in each winning column.

| Benchmark (test) | M⋆ | Best baseline |
|---|---|---|
| LoCoMo token F1 | 0.459 | 0.373 (Mem0) |
| HealthBench Data | 0.390 | 0.327 (GEPA + Vector Search) |
| PRBench Legal | 0.660 | 0.568 (GEPA) |
| PRBench Finance | 0.586 | 0.449 (GEPA) |
| ALFWorld Unseen success | 0.881 | 0.857 (GEPA) |

The evolved programs differ (all best programs use SQLite, but they differ in vector retrieval and read-time LLM use): the best ALFWorld program is a compact SQLite action cache with one read-time LLM call; the best LoCoMo program combines ChromaDB semantic search with SQLite lexical and metadata scoring.

## The controls that decide whether the gain is real

- **Ablations (LoCoMo F1, Table 2).** Full system 0.459. Evolving only the prompt instructions (code frozen at the Vector Search seed) gives 0.256; freezing the instructions gives 0.353; always picking the top parent instead of softmax sampling gives 0.381; dropping the population and mutating only the current best gives 0.318. The code part and the population both matter. Table 2 reports no variance, and the full-system anchor (0.459) is seed 0, above the five-seed mean of 0.421; three of the four ablated variants (0.353, 0.318, 0.256) fall below Mem0's 0.373, and the prompt-only variant equals Vector Search at 0.256. The "− Diversity" variant also starts from a single empty seed.
- **Seeds (Table 3).** Five evolution seeds, but only on three of the seven configurations. LoCoMo 0.421 ± 0.042 against Mem0's 0.373 (4 of 5 seeds above); HealthBench Data 0.391 ± 0.023 against 0.327 (5 of 5); PRBench Finance 0.561 ± 0.032 against 0.449 (5 of 5). The Table 1 numbers match seed 0 of these runs. For LoCoMo and PRBench Finance the five-seed means (0.421, 0.561) are lower than Table 1; for HealthBench Data it is the same (0.391 vs 0.390). LoCoMo's mean is 0.048‡ above Mem0, not the 0.086‡ of the headline.
- **Transfer (Figure 5).** The program evolved on a task beats programs evolved elsewhere on that task, and five of six transferred programs fall below the universal seed. On LoCoMo the seed scores 0.26, the native program 0.459, and the program evolved on ALFWorld 0.02.
- **Cost (Appendix D.1).** One 20-iteration evolution run costs $12–90 (LoCoMo $25.43, PRBench Legal $90.19), ALFWorld runs take about 100 hours of wall-clock time, which the paper attributes mainly to environment interaction. The paper says evolution is a one-time cost and an evolved program adds 0–2 LLM calls per query. The only baselines whose cost is listed (No Memory, Vector Search) cost $0.31–$1.51 per run. The paper reports no matched-compute baseline, no tuning budget for GEPA (the baseline that also optimizes on validation data), and no variance for any baseline.

## Where the gain is absent or small

- **ALFWorld Seen: M⋆ is not best.** 0.700, below GEPA + Vector Search (0.820), Trajectory Retrieval (0.780) and two baselines at 0.720 — a gap of 0.120‡ to the leader.
- **Thin margins on small test sets.** HealthBench Emergency 0.493 vs 0.487 (Dynamic Cheatsheet); ALFWorld Unseen 0.881 vs 0.857. Test sets have 50–100 items and no confidence intervals are given; for ALFWorld Unseen, Table 5 lists 50 episodes but the category counts in Appendix Table 10 sum to 42, so the 0.881-vs-0.857 margin is one episode.
- **LoCoMo by question type.** M⋆ is strongest on open-domain questions (0.51) and ties Mem0 on single-hop (0.33), but temporal questions score 0.19 against 0.38 for GEPA + Vector Search. Open-domain questions are 55 of the 100 LoCoMo test items, and the per-category scores in Table 4 weight to about 0.41‡, not the 0.459 of Table 1; the paper does not explain the difference. The authors say an aggregate objective can leave harder categories underserved.
- **Limits stated by the authors.** Only one task-agent / coding-agent pair was tried, and evolution can drift toward task-specific heuristics (for example the synonym table in the ALFWorld cache) that limit transfer.

## Our read

HarnessRSI score **90**, band ★★★, evidence level **improver**: the improvement mechanism itself (population selection, instruction vs. code evolution) is varied and compared, and gains are evaluated on held-out data. The paper reports held-out evaluation, cross-task transfer, multi-seed variance on three configurations, optimizer cost and ablations. It does not report a matched-compute comparison against the baselines, and it does not test for leakage between the validation and test sets (for LoCoMo both come from the same conversation pool). The headline table reflects one evolution seed per configuration; the multi-seed rows show the direction of the gain holds, with a smaller size on LoCoMo and PRBench Finance.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
