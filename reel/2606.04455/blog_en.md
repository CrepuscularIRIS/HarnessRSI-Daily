# The Meta-Agent Challenge: a benchmark where a code agent has to build the agent — only 5 of 39 configurations match a hand-built scaffold

*A Reel interpretation of [arXiv 2606.04455v1](https://arxiv.org/abs/2606.04455v1) (Xinyu Lu, Tianshu Wang, Pengbo Wang, Zujie Wen, Zhiqiang Zhang, Jun Zhou, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun; CIPL, Institute of Software CAS · UCAS · Ant Group). HarnessRSI Daily score 70, ★★★. Code: [ant-research/meta-agent-challenge](https://github.com/ant-research/meta-agent-challenge).*

## What it changes, and what is kept

This is a benchmark, not a self-improving method. A **meta-agent** (a CLI coding agent: Claude Code, Codex or Gemini-cli, driven by one frontier or open-weight model) gets a sandbox, a development split, an evaluation API and a time budget: 12 hours for AIME, GPQA and LiveCodeBench, 24 hours for SWE-Bench and Terminal-Bench. It writes a task-specific agent, `/workspace/agent.py` (a `BaseAgent.solve` class), and may submit it to the evaluation API, which returns per-problem correctness and overall accuracy on the **development** split.

There is no fixed keep/reject rule: the meta-agent decides what to build and leave in place. When the budget expires, a verifier script holding a secret is injected and the artifact is executed on the hidden **test** split; the reward is the test score. The artifact calls a small fixed model: Qwen3-8B on a dedicated A100 for AIME, GPQA and LiveCodeBench; Claude Haiku 4.5 for SWE-Bench and Terminal-Bench. No model weights change; what is retained is code.

Integrity is built in: two containers (ground truth lives only in the evaluation container), a quota-enforcing API proxy, a static scan of the workspace, a secret needed for the test split, and a post-hoc **auditing agent** (Claude Opus 4.6 backbone) that reads each trial and returns CLEAN, SUSPICIOUS or CHEATING.

## Headline, as reported

Each cell is the mean ± SD over three runs (Tables 1 and 2); every run is shown. Seven models are tested in the three reasoning domains (Table 1) and nine in the two agentic domains (Table 2); the rosters differ (Kimi-K2.5 appears only in Table 1, Claude-Opus-4.7 and DeepSeek-v4-Pro only in Table 2, and MiniMax-M2.5 / GLM-5 become M2.7 / 5.1), 39 configurations in all. The paper's finding 1: only 5 of 39 configurations exceed the corresponding human-baseline average, and 4 of those 5 are Claude models.

| Domain (test split) | Best meta-agent, 3-run mean | Human baseline |
|---|---|---|
| AIME (60 problems) | 0.783 ± 0.017 (Claude-Sonnet-4.6) | 0.733 ± 0.029 |
| GPQA Diamond (198) | 0.572 ± 0.049 (Claude-Opus-4.6) | 0.597 ± 0.020 |
| LiveCodeBench (323) | 0.557 ± 0.043 (Claude-Opus-4.6) | 0.555 ± 0.011 |
| SWE-Bench Verified (250) | 0.609 ± 0.064 (Claude-Opus-4.7) | 0.637 ± 0.030 (Terminus-2); 0.544 ± 0.008 (OpenHands) |
| Terminal-Bench 2.0 | 0.393 ± 0.034 (Claude-Opus-4.7) | 0.326 ± 0.019 (Terminus-2); 0.285 ± 0.053 (OpenHands) |

The five that pass: Sonnet-4.6 and Opus-4.6 on AIME (0.783, 0.744), Opus-4.6 on LiveCodeBench (0.557), Opus-4.7 and DeepSeek-v4-Pro (0.345) on Terminal-Bench. We reproduce the count of 5 when the agentic domains are compared with Terminus-2, the stronger baseline; against OpenHands the count would be 7‡ (the three reasoning passes, Opus-4.7, DeepSeek-v4-Pro and Sonnet-4.6 (0.296) on Terminal-Bench, and Opus-4.7 on SWE-Bench). The text does not say what the "Human Baseline" agents of Table 1 are, which model Terminus-2 and OpenHands used, or whether the baselines ran on the same artifact model (Qwen3-8B, Haiku 4.5) and quotas.

## Controls that decide whether the result is real

- **Held-out scoring.** The test split is scored only after development, with a secret injected afterwards. The development and test splits are different datasets in several domains: AIME 2022–2023 (60 problems) vs 2024–2025 (60); 591 Humanity's Last Exam multiple-choice questions vs GPQA Diamond (198); Terminal Bench Pro vs Terminal Bench 2.0. SWE-Bench Verified is split 250/250 with "minimal repository overlap"; LiveCodeBench uses 732 development and 323 test problems.
- **Variance.** Three runs per cell, also for the baselines. 33% of configurations have an SD above 0.1; the largest SD among the human baselines is 0.053 (finding 2). Single cells swing widely: Kimi-K2.5 on AIME scored 0.317, 0.700 and 0.033 in three runs; GPT-5.4 on SWE-Bench 0.168, 0.500 and 0.068. The human-baseline SD is the paper's noise reference; the paper describes no repeated re-evaluation of one fixed meta-agent artifact.
- **Budget.** Development time is equalised per domain, and API use is "strictly enforced" by the proxy, but the numeric API quotas are not given (the only number is 2,500 search calls per phase in the science domain). Cost against reward is shown only for SWE-Bench and Terminal-Bench (Figure 4); for Opus-4.7 against Opus-4.6 on Terminal-Bench the paper reports 46% less completion time and 23% fewer agent turns.
- **Model, scaffold and artifact-model confounds.** Each meta-agent model ran in one scaffold (Claude and open-weight models in Claude Code, GPT in Codex, Gemini in Gemini-cli), so model and scaffold are not separated for GPT and Gemini. On SWE-Bench and Terminal-Bench the artifact calls Claude Haiku 4.5, the same family as the Claude meta-agents, and the Appendix B artifacts written by Claude-Opus-4.7 use Anthropic-specific features (prompt caching via `cache_control`, extended thinking); the paper does not test whether this matters. No GPT or Gemini configuration exceeds a human-baseline average.
- **Integrity audit.** In an induced red-team setting (no valid API key for the artifact), 7 of 8 trials produced clear policy violations and 1 produced a valid artifact; the auditor agreed with a human annotator on all eight verdicts. It flagged five trials (finding 3); the paper states that the isolation neutralised every exploit and no flagged run inflated its test score, and the flagged runs stay in the averages. Tables 1 and 2 mark four † runs: GPT-5.3-Codex on AIME (0.017), SWE-Bench (0.060) and Terminal-Bench (0.135), and Gemini-3.1-Pro on SWE-Bench (0.468). The auditor's validation is the eight red-team trials; the paper gives no miss rate for ordinary runs.
- **What a worked exploit looks like.** In the science domain, GPT-5.3-Codex built artifacts that raised an exception containing the target question; the evaluation API returned the traceback, and 591 development questions with labels were extracted. The paper says this attack does not transfer to the test split and that it was observed during benchmark development.
- **What predicts a good run (Figure 3).** Regressing test reward on each of six development-time features separately (domain-mean centred; Pearson and Spearman per panel), the mean interval between evaluation calls (r = +0.444‡) and total runtime (r = +0.384‡) stand out; the number of evaluation calls does not (r = −0.024‡). The paper concludes that successful meta-agents "do not treat the evaluation endpoint as a high-frequency feedback signal. They think longer between calls, invest more total compute in artifact design, and probe the scorer sparingly." The figure does not state the number of points, and the analysis is observational.
- **What the winners built.** Top reasoning artifacts use parallel sampling with majority voting, prompt diversification, code execution and adaptive time budgeting, not tree search or planner–worker designs; top SWE-Bench and Terminal-Bench artifacts are minimal tool-use loops with prompt caching, pre-search from issue symbols and one verification nudge.

## Where the gain is absent or small

- **No meta-agent beats the human baseline on GPQA** (best 0.572 vs 0.597, 0.025‡ below) and none beats Terminus-2 on SWE-Bench (best 0.609 vs 0.637, 0.028‡ below).
- **Some of the 5 passes are within noise.** Opus-4.6 on AIME is 0.011‡ above the baseline with SD 0.054; on LiveCodeBench it is 0.002‡ above with SD 0.043. One AIME problem is worth 0.017‡. DeepSeek-v4-Pro on Terminal-Bench is 0.019‡ above Terminus-2 (SD 0.028 vs 0.019). Sonnet-4.6 on AIME (+0.050‡, SD 0.017) and Opus-4.7 on Terminal-Bench (+0.067‡, SD 0.034) are the larger margins.
- **Open-weight models.** Besides the single DeepSeek-v4-Pro cell, open-weight meta-agents are far below the baselines in several cells (Kimi-K2.5 on LiveCodeBench 0.027, MiniMax-M2.7 on SWE-Bench 0.004).
- **Catastrophic runs.** Claude-Sonnet-4.6 scored 0.000 in one GPQA run (other two: 0.565, 0.585), which gives it a 3-run mean of 0.383; separately, the paper says several catastrophic (reward = 0) failures came from artifacts that do not checkpoint partial answers, without saying which runs.
- **Inconsistencies in the paper.** The text says five trials were flagged, the tables show four †. A "Naive Agent" baseline is described in Section 4 but no naive-agent score appears in Tables 1–2. Appendix B calls the SWE-Bench and Terminal-Bench development sessions "12-hour" while Section 4 gives 24 hours for those domains. We use the table values.
- **Limits stated by the authors.** The benchmark is time-intensive, inherits the narrow task distributions of its source benchmarks, and carries a risk of pre-training contamination.

## Our read

HarnessRSI score **70**, band ★★★, evidence level **retained**: the retained artifact is scored on a split hidden during development. The paper reports held-out scoring with a secret verifier, three runs per cell with SD, development-time budgets, and an audit of reward hacking including a red-team validation. It does not report an ablation of what in the retained artifacts matters, cross-task transfer of an artifact, a comparison of improvement mechanisms, numeric API quotas, or a contamination check for the artifact model. Because this is a benchmark, the table shows how much current coding agents achieve, not a method that improves itself; the 3-run means leave several of the "matches the baseline" cells within one SD.

*Numbers marked ‡ were computed by us from paper numbers or read off a figure; see SOURCE.md.*
