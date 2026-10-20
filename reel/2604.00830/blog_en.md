# Meta-TTL: learning the "how to improve" prompt instead of hand-writing it — consistent gains, but the controls that would size them are thin

*A Reel interpretation of [arXiv 2604.00830v4](https://arxiv.org/abs/2604.00830v4) (Zhanzhi Lou, Hui Chen, Yibo Li, Qian Wang, Bryan Hooi; National University of Singapore). HarnessRSI Daily score 69, ★★. Code: [zzzlou/meta-ttl](https://github.com/zzzlou/meta-ttl).*

## What the system changes about itself

In test-time learning (TTL) an agent attempts the same task for several episodes and rewrites its own context between attempts. Meta-TTL leaves the **actor** untouched (a frozen Gemini-3-Flash) and treats the *procedure that rewrites the actor's system prompt* as the learnable object. That procedure is a **meta-prompt** ϕ, a natural-language document read by a separate **meta-agent** (GPT-5 in the main experiments). After each episode the meta-agent reads the trajectory history and writes the actor's system prompt for the next episode. A session has 6 episodes on Jericho and 3 on WebArena-Lite and τ²-bench, and is scored by W-AUC, a normalised average over episodes that weights later episodes more (weight k for episode k).

## The meta-training loop and the keep/reject rule

1. Keep one **expert** meta-prompt ϕ⋆, initialised from a seed meta-prompt.
2. Sample a training task and run a full TTL session with ϕ⋆.
3. Two-stage reflection: first extract task-specific facts from the session, then use the session, the facts and ϕ⋆ to write a revised candidate meta-prompt.
4. Run TTL sessions with **both** the expert and the candidate on a set of validation tasks and score each by W-AUC.
5. Normalise each task's W-AUC against that task's score history (z-score), and average the candidate-minus-expert difference over tasks: the **balanced improvement score (BIS)**. The candidate replaces the expert only if BIS is positive.

Meta-training runs 12–15 iterations with 205–350 TTL sessions and costs about $30–70 in API calls per benchmark (one-time, no GPU). The final meta-prompt is frozen and applied to unseen tasks. Nothing in the actor's weights changes; the kept artifact is a text document. The search is a single incumbent with a greedy accept rule, not a population.

## Headline result, as reported

All main rows use a Gemini-3-Flash actor; baselines that need a separate adaptation LLM also use GPT-5, the same model as Meta-TTL's meta-agent. Average W-AUC, Meta-TTL against the strongest baseline in that column (Tables 1–3):

| Benchmark | Meta-TTL | Strongest baseline |
|---|---|---|
| Jericho ID games (5 runs) | 0.396 | 0.323 (EvoTest), +23% |
| Jericho OOD games | 0.414 | 0.325 (EvoTest), +27% |
| WebArena-Lite ID domains (3 runs) | 0.693 | 0.619 (Memory Agent), +12% |
| WebArena-Lite OOD domains | 0.766 | 0.728 (TextGrad), +5% |
| τ²-bench Airline | 0.717 | 0.650 (TextGrad), +10% |
| τ²-bench Retail | 0.700 | 0.633 (Memory Agent), +11% |
| τ²-bench Telecom (OOD) | 0.583 | 0.525 (Reflexion), +11% |

Baselines: Static, Reflexion, Memory Agent, AWM, TextGrad, EvoPrompt, EvoTest, plus a Naive meta-agent. The paper states the number of repeated runs for Jericho (five) and WebArena-Lite (three) but not for τ²-bench; the performance tables (Tables 1–5, 7–8) give means without standard deviations. Spread is shown only in Figure 3 (standard error over five runs, Jericho) and as ± SD on wall-clock time in Table 6.

## The controls that decide whether the gain is real

- **Naive meta-agent (same architecture and models, unoptimised self-improvement policy).** The paper lists it as a baseline (not in its ablation section); it is the closest thing to a with/without-meta-training comparison, since only the self-improvement policy differs. W-AUC: Jericho 0.215 ID / 0.286 OOD against 0.396 / 0.414; WebArena-Lite 0.567 / 0.722 against 0.693 / 0.766; τ²-bench 0.633 / 0.558 / 0.433 against 0.717 / 0.700 / 0.583. On Jericho ID the Naive meta-agent's average score (55.01) is not above Static (55.61), and its W-AUC (0.215) is close to Static's 0.195. The paper does not say the Naive meta-agent is the seed meta-prompt.
- **Other optimisers on the same task (Table 5, Jericho W-AUC, Qwen3-4B meta-agent, Gemini-3-Flash actor).** Meta-training the meta-agent by GRPO (1,920 rollouts) or by a GEPA outer loop, versus Meta-TTL's outer loop (350 rollouts). ID average: untrained 0.146, GRPO 0.150, GEPA 0.152, Meta-TTL 0.164. OOD average: 0.168, 0.174, 0.198, 0.232. The paper's plausible explanation for GEPA's weaker OOD result is that its candidate selection "preserves prompts specialized to individual tasks"; it adds that this is "also consistent with our finding that the prompts produced by GEPA contain substantial task-specific facts and solutions" (the GEPA prompt in Appendix A.4 includes Detective-specific content such as "330/360"). The three ID games here are the meta-training games. The paper does not state GEPA's rollout budget or the number of runs for this table.
- **Parameter-updating TTL (Table 4, Jericho W-AUC, Qwen3-8B actor, K = 3 episodes, at most 30 steps; a different setting from the main tables, so 0.182 is not comparable with 0.396).** Meta-TTL here uses a Qwen3-8B actor and a Qwen3-8B meta-agent running "the meta-prompt learned in our main experiments" (meta-trained with the GPT-5 meta-agent and Gemini actor, then reused, not re-meta-trained on Qwen3-8B). Meta-TTL 0.182 ID / 0.201 OOD against Online GRPO 0.118 / 0.114, Online SFT 0.116 / 0.092, SFT+MAML 0.122 / 0.157, Static 0.084 / 0.094. The ID games are the meta-training games, also for SFT+MAML, whose initialisation was meta-learned on them (15 meta-steps on 2×H200). The paper does not state the number of runs for this table.
- **Different meta-agent backbone (Appendix D, GLM-5.3-Flash).** Covers Jericho and WebArena-Lite only (not τ²-bench). The meta-prompt was re-trained with that backbone; Meta-TTL is best in every column of Tables 7 and 8, against only three baselines (Naive, AWM, EvoTest). Jericho OOD average score is a near-tie (0.343 vs EvoTest 0.334), and Meta-TTL's Jericho W-AUCs here (0.379 ID, 0.371 OOD) are lower than the main-table 0.396 and 0.414 (different meta-agent).
- **Cost at test time (Table 6, Jericho, 3 runs).** Meta-TTL 860.9 ± 66.2 s wall-clock, 364k tokens, 5 adaptation LLM calls; Static 593.2 s and 196k; EvoTest 759.1 s and 181k. The paper calls this "comparable" to prompt-optimisation baselines.

Not run or not reported: a matched-compute comparison against the main baselines (they receive no meta-training budget; the $30–70 is not granted to them, and their tuning budget is not reported); standard deviations for any performance-table cell (Tables 1–5, 7–8); repeated meta-training runs (one learned meta-prompt per benchmark is shown in Appendix A); the sizes of the validation and evaluation task sets.

## Where the gain is absent or small

- **Jericho ID is dominated by one game, and is the meta-training set.** Against EvoTest, W-AUC gaps are 0.162‡ on Detective, 0.011‡ on Zork 1 and 0.046‡ on Temple. The paper says that for Jericho "ID evaluation uses the meta-training games", so these three games are not held out; the held-out Jericho result is the OOD rows.
- **Ties and near-ties against the strongest baseline in a column.** Jericho OOD Zork 3: 0.427 against EvoTest 0.423 (0.004‡; on Balances and Library the gaps to the strongest baseline, the Naive meta-agent in both, are 0.092‡ and 0.113‡). WebArena-Lite GitLab W-AUC: 0.883, equal to AWM. WebArena-Lite Shopping Admin: 0.760 against 0.749. τ²-bench Retail average score: 0.633, equal to Reflexion. No confidence intervals are given, so these cells cannot be separated from noise.
- **Against GEPA on one ID game.** On Jericho Temple (Table 5) Meta-TTL's outer loop scores 0.129, equal to the untrained meta-agent and below GEPA's 0.154. Table 5's ID games are also the meta-training games.
- **Against weight-updating baselines on single OOD games (Table 4).** SFT+MAML scores 0.405 on Zork 3 against Meta-TTL's 0.238, and Online GRPO scores 0.147 against 0.131 on Balances.
- **Jericho OOD Zork 3 average score** is 2.87 for both Meta-TTL and EvoTest.
- **No limitations section.** The paper has none and reports no contamination or leakage test.

## Our read

HarnessRSI score **69**, band ★★, evidence level **improver**: the self-improvement policy itself is optimised, and compared against a Naive meta-agent and against other optimisers. The paper reports held-out evaluation on unseen domains (partly: Jericho ID uses the training games), cross-domain transfer, optimiser cost, a Naive-meta-agent baseline, an RL and a GEPA outer-loop comparison, and a second meta-agent backbone. It does not report per-cell standard deviations, a matched-compute comparison against the main baselines, repeated meta-training runs, the evaluation-set sizes, or a leakage test. Internal points of the paper: the abstract's "up to 23% … on ID tasks and 27% on OOD tasks" refers to W-AUC, while Table 1's OOD average score is +33% (10.61 vs 7.99); Algorithm 2 lists an acceptance margin δ and episode-0 baseline results as inputs but its accept rule is a plain comparison of mean z-scores; Tables 7–8 report average score on a normalised scale unlike Table 1's raw game scores. Read the headline as a consistent direction over eight baselines in seven columns, with the size of each cell untested for noise.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
