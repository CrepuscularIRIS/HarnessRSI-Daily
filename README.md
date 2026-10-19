# HarnessRSI Daily

A research radar for **harness-level recursive self-improvement (RSI)**: systems that improve their own
*non-weight* components — prompts, skills, tools, workflows, memory, agent code, evaluators — from their own
execution feedback, and keep those changes for later tasks.

Lists of such papers already exist (e.g. [awesome-rsi](https://github.com/lobehub/awesome-rsi)). This repo goes
the other way: **depth over breadth**. It asks of each paper *what exactly improves, how the change is accepted,
and whether the evidence shows a real, retained improvement* — and it maps the field into recurring research
patterns, learned from the corpus itself.

> 中文简介：专门追踪「非权重层面的递归自我改进」（Harness RSI）。不做又一个论文列表，而是对每篇论文判定
> 它改了什么、怎么决定保留、证据是否真的支持"留存下来的提升"；并从语料中逆向归纳出 Harness 版的研究模式卡。

<!-- BOARD:START -->
## Top 30 papers by HarnessRSI score

Out of 155 scored so far (3 at ★★★ ≥ 70). Full board, grouped by pattern: [papers/](papers/README.md). Score (0–100) = **E**vidence (50) + e**X**ecution against the pattern card (30) + evidence **L**evel (10) + **C**ode (10); every judgment is quote-backed — see [SCORE_SPEC](research/SCORE_SPEC.md). It measures what a paper reports and how it executes its move, not the value of the idea.

| Date | Paper | Pattern | Score | Code |
|---|---|---|---|---|
| 2026-05-28 | **[GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents](https://arxiv.org/abs/2605.29668v3)**<br>GRASP：面向自我改进LLM智能体的门控回归感知技能提议器<br><sub>Edits a bounded skill library from grouped failures, committing an edit only if it nets fixes over regressions on a held-out probe under a hard regression budget.</sub> | [H30](patterns/sub/H30.md) | **84** ★★★<br><sub>E41 X27 L6 C10</sub> | [code](https://github.com/jomoll/GRASP) |
| 2026-03-19 | **[Hyperagents](https://arxiv.org/abs/2603.19461v1)**<br>超智能体（Hyperagents）<br><sub>A single editable program holding task agent and meta agent rewrites both, including its own modification procedure; variants are archived DGM-style and scored on task performance.</sub> | [H20](patterns/sub/H20.md) | **74** ★★★<br><sub>E31 X23 L10 C10</sub> | [code](https://github.com/facebookresearch/Hyperagents) |
| 2026-05-19 | **[Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576v3)**<br>库漂移：诊断并修复自演化LLM技能库中的一种静默失效模式<br><sub>Frozen LLM writes, routes, and retires its own skills; outcome-driven retirement, bounded active cap and a meta-skill authoring prior govern which skills persist.</sub> | [H30](patterns/sub/H30.md) | **74** ★★★<br><sub>E35 X23 L6 C10</sub> | [code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet) |
| 2026-03-29 | **[EffiSkill: Agent Skill Based Automated Code Efficiency Optimization](https://arxiv.org/abs/2603.27850v1)**<br>EffiSkill：基于智能体技能的自动化代码效率优化<br><sub>Mines operator and meta skills by contrasting slow/fast program pairs, clusters and merges them into a library, then retrieves and composes skills to optimize unseen programs.</sub> | [H00](patterns/sub/H00.md) | **67** ★★<br><sub>E25 X26 L6 C10</sub> | — |
| 2026-06-17 | **[Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/abs/2606.28374v1)**<br>基于留出选择的递归自演化智能体<br><sub>Frozen LLM rewrites a three-layer strategy/skills/playbook state from its trajectories, committing only strict improvements on a disjoint validation split with empty-state fallback.</sub> | [H31](patterns/sub/H31.md) | **67** ★★<br><sub>E35 X23 L6 C3</sub> | — |
| 2025-09-11 | **[SEDM: Selective Self-Evolving Distributed Memory for Agents](https://arxiv.org/abs/2509.09498v4)**<br>SEDM：面向智能体的选择性自演化分布式记忆<br><sub>Shared agent-society memory admits entries via paired replay A/B tests, reweights/retires them by measured utility, and a calibrated gate decides per task whether to inject memory.</sub> | [H29](patterns/sub/H29.md) | **65** ★★<br><sub>E34 X25 L6 C0</sub> | — |
| 2025-10-17 | **[EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079v3)**<br>EvolveR：基于经验驱动生命周期的自进化LLM智能体<br><sub>Agent self-distills success/failure trajectories into a scored, deduplicated principle base it retrieves via a search action, while GRPO trains the policy on the same online trajectories.</sub> | [H28](patterns/sub/H28.md) | **65** ★★<br><sub>E27 X22 L6 C10</sub> | [code](https://github.com/Edaizi/EvolveR) |
| 2026-04-13 | **[Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923v1)**<br>Mem²Evolve：通过能力扩展与经验蒸馏协同演化实现自我演化智能体<br><sub>Creates tools and expert agents on demand guided by distilled experience, admits tools after executing LLM-synthesized tests with self-correction, and retains assets plus lessons.</sub> | [H07](patterns/sub/H07.md) | **65** ★★<br><sub>E19 X30 L6 C10</sub> | — |
| 2025-07-25 | **[GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457v2)**<br>GEPA：反思式提示进化可以胜过强化学习<br><sub>Evolves module prompts of a compound AI system via LLM reflection on execution/evaluation traces, keeping a per-instance Pareto frontier of candidates selected on validation.</sub> | [H16](patterns/sub/H16.md) | **62** ★★<br><sub>E19 X27 L6 C10</sub> | [code](https://github.com/gepa-ai/gepa) |
| 2026-01-27 | **[MetaMem: Evolving Meta-Memory for Knowledge Utilization through Self-Reflective Symbolic Optimization](https://arxiv.org/abs/2602.11182v2)**<br>MetaMem：通过自反思符号优化演化用于知识利用的元记忆<br><sub>Reflects on judged-correct/incorrect sampled answers to ADD/DEL/MOD a meta-memory of memory-utilization experiences, built in mini-batches and reused at inference.</sub> | [H01](patterns/sub/H01.md) | **62** ★★<br><sub>E24 X22 L6 C10</sub> | [code](https://github.com/OpenBMB/MetaMem) |
| 2026-02-16 | **[Evolutionary System Prompt Learning for Reinforcement Learning in LLMs](https://arxiv.org/abs/2602.14697v3)**<br>面向LLM强化学习的进化式系统提示学习<br><sub>Each RL iteration samples under several system prompts; the same rollouts update LoRA weights and TrueSkill-rate prompts, which evolve by reflective mutation and crossover.</sub> | [H28](patterns/sub/H28.md) | **62** ★★<br><sub>E24 X22 L6 C10</sub> | [code](https://github.com/LunjunZhang/E-SPL) |
| 2026-05-09 | **[Ace-Skill: Bootstrapping Multimodal Agents with Prioritized and Clustered Evolution](https://arxiv.org/abs/2605.08887v1)**<br>Ace-Skill：以优先级采样与聚类演化自举多模态智能体<br><sub>Bootstraps multimodal agent knowledge by prioritizing under-mastered training samples via decayed Beta proficiency and storing merged, capped experiences and skill documents per semantic cluster.</sub> | [H01](patterns/sub/H01.md) | **62** ★★<br><sub>E24 X22 L6 C10</sub> | [code](https://github.com/AMAP-ML/Ace-Skill) |
| 2026-06-06 | **[PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106v1)**<br>PACE：面向自演化智能体的任意时刻有效接受检验<br><sub>Prompt-evolving agent commits a proposed edit only when a paired testing-by-betting e-process versus the incumbent crosses an anytime-valid threshold, replacing greedy dev-score acceptance.</sub> | [H31](patterns/sub/H31.md) | **62** ★★<br><sub>E29 X27 L6 C0</sub> | — |
| 2026-03-09 | **[RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback](https://arxiv.org/abs/2603.08561v6)**<br>RetroAgent：通过回顾式双重内在反馈从解题走向进化<br><sub>Online RL agent reflects on each episode to produce a progress-based intrinsic reward and textual lessons in a UCB-retrieved memory; the reflector itself can be RL-trained.</sub> | [H28](patterns/sub/H28.md) | **61** ★★<br><sub>E19 X26 L6 C10</sub> | [code](https://github.com/zhangxy-2019/RetroAgent) |
| 2026-04-17 | **[Harnessing Pre-Resolution Signals for Future Prediction Agents](https://arxiv.org/abs/2604.15719v3)**<br>利用结果揭晓前信号构建未来预测智能体<br><sub>Revisiting an unresolved forecasting question, the agent contrasts checkpoint notes to extract pre-resolution signals and applies bounded add/revise/deprecate patches to a typed question-local harness.</sub> | [H00](patterns/sub/H00.md) | **61** ★★<br><sub>E25 X30 L6 C0</sub> | — |
| 2026-10-09 | **[Harness^2: Recursive Agent Harnessing for an Open World](https://arxiv.org/abs/2610.14224v1)**<br>Harness^2：面向开放世界的递归式智能体框架构建<br><sub>Refines each task's execution harness via contrastive propose-probe-compose without verifiers, and keeps adopted harnesses plus lessons in a library that guides future harness edits.</sub> | [H21](patterns/sub/H21.md) | **61** ★★<br><sub>E26 X15 L10 C10</sub> | [code](https://github.com/google-research/harness2) |
| 2026-06-08 | **[Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://arxiv.org/abs/2606.09365v4)**<br>经验成就技能：通过自演化技能记忆实现可泛化的医疗智能体推理<br><sub>Medical agent distills trajectories into a branched skill repo, credits skills by category-normalized outcome advantage, and governs retrieval, promotion, merging, deprecation and capacity.</sub> | [H30](patterns/sub/H30.md) | **60** ★★<br><sub>E28 X23 L6 C3</sub> | — |
| 2026-03-13 | **[MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Embodied Minecraft Agents](https://arxiv.org/abs/2603.13131v3)**<br>MineEvolve：面向长时程具身 Minecraft 智能体的知识累积自进化<br><sub>Converts typed execution feedback into skills (from successes) and remedies (from failures), validated and merged by a curator, then used to repair unfinished plans.</sub> | [H00](patterns/sub/H00.md) | **59** ★★<br><sub>E21 X22 L6 C10</sub> | [code](https://github.com/xzw-ustc/MC-MineEvolve) |
| 2026-04-21 | **[A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://arxiv.org/abs/2604.19572v3)**<br>通过观测上下文压缩实现高效终端智能体的自进化框架<br><sub>Terminal agents learn structured observation-compression rules: added for uncovered outputs, replaced on over-compression complaints, and written to a confidence-ranked global pool only if reliably applied.</sub> | [H01](patterns/sub/H01.md) | **59** ★★<br><sub>E21 X26 L2 C10</sub> | [code](https://github.com/multimodal-art-projection/TACO) |
| 2026-09-21 | **[RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972v3)**<br>RRSI：智能体框架（harness）的正则化递归自我改进<br><sub>Evolves agent harness code from evolve-set feedback under regularized proposal (annealed edit budget, credit history) and selection (leakage critic, noise floor, cost gate, pruning).</sub> | [H31](patterns/sub/H31.md) | **59** ★★<br><sub>E23 X20 L6 C10</sub> | [code](https://github.com/google-research/rrsi) |
| 2025-05-29 | **[Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954v3)**<br>达尔文哥德尔机：自我改进智能体的开放式进化<br><sub>Coding agents edit their own codebase from benchmark logs; children that keep editing ability join an open-ended archive, parents sampled by score and novelty.</sub> | [H20](patterns/sub/H20.md) | **58** ★★<br><sub>E22 X20 L6 C10</sub> | [code](https://github.com/jennyzzt/dgm) |
| 2026-06-23 | **[Metis: Bridging Text and Code Memory for Self-Evolving Agents](https://arxiv.org/abs/2606.24151v1)**<br>Metis：为自我演化智能体打通文本记忆与代码记忆<br><sub>Keeps reflection-distilled text memory (plans, facts, pitfalls) and promotes execution plans into sandbox-validated callable tools only after repeated reuse across distinct queries.</sub> | [H08](patterns/sub/H08.md) | **58** ★★<br><sub>E22 X30 L6 C0</sub> | — |
| 2026-04-18 | **[FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills](https://arxiv.org/abs/2607.21596v2)**<br>FlowEvo：通过工作流与可执行技能协同演化实现自我演化智能体<br><sub>Compiles verifier-passed workflows into callable skills admitted by interface, replay and safety checks, reuses them directly or as context, and suppresses skills with negative contrastive utility.</sub> | [H08](patterns/sub/H08.md) | **58** ★★<br><sub>E26 X20 L2 C10</sub> | [code](https://github.com/DEFENSE-SEU/FlowEvo) |
| 2023-05-26 | **[Large Language Models as Tool Makers](https://arxiv.org/abs/2305.17126v2)**<br>大语言模型作为工具制造者<br><sub>A strong LLM writes and unit-test-verifies a Python tool per task type from few demos; a cheap LLM reuses it, cached as a functional cache.</sub> | [H06](patterns/sub/H06.md) | **57** ★★<br><sub>E16 X25 L6 C10</sub> | [code](https://github.com/ctlllll/LLM-ToolMaker) |
| 2026-03-18 | **[AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000v1)**<br>AgentFactory：通过可执行子智能体积累与复用实现自我演化的框架<br><sub>Saves successful task-solving subagents as executable Python code, repairs them from execution feedback on later similar tasks, and reuses or exports them.</sub> | [H06](patterns/sub/H06.md) | **57** ★★<br><sub>E18 X23 L6 C10</sub> | [code](https://github.com/zzatpku/AgentFactory) |
| 2026-04-15 | **[Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents](https://arxiv.org/abs/2604.14004v1)**<br>记忆迁移学习：编码智能体中记忆如何跨领域迁移<br><sub>Evaluates coding agents with leave-one-benchmark-out memory pools in four abstraction formats; abstract insights transfer across domains while raw trajectories cause negative transfer.</sub> | [H32](patterns/sub/H32.md) | **57** ★★<br><sub>E24 X27 L6 C0</sub> | — |
| 2026-05-21 | **[Ratchet: How Reliable Must an LLM Judge Be to Retire a Skill?](https://arxiv.org/abs/2605.22148v3)**<br>Ratchet：LLM评审需要多可靠才能淘汰一个技能？<br><sub>Skill library evicts skills on measured per-skill contribution under a width cap and authoring prior; proves when an LLM judge's error direction disables eviction.</sub> | [H31](patterns/sub/H31.md) | **57** ★★<br><sub>E18 X23 L6 C10</sub> | [code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet) |
| 2026-02-04 | **[SE-Bench: Benchmarking Self-Evolution with Knowledge Internalization](https://arxiv.org/abs/2602.04811v2)**<br>SE-Bench：以知识内化衡量自我进化<br><sub>Obfuscates NumPy into a pseudo-novel API so held-out coding tasks are impossible without internalized knowledge, then diagnoses memory, SFT, RL and self-play internalization.</sub> | [H33](patterns/sub/H33.md) | **56** ★★<br><sub>E13 X27 L6 C10</sub> | [code](https://github.com/thunlp/SE-Bench) |
| 2023-05-25 | **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291v2)**<br>Voyager：基于大语言模型的开放式具身智能体<br><sub>Minecraft agent self-proposes curriculum tasks, writes and repairs code skills from execution feedback, admits critic-verified skills to a reusable embedding-indexed library.</sub> | [H06](patterns/sub/H06.md) | **55** ★★<br><sub>E19 X20 L6 C10</sub> | [code](https://github.com/MineDojo/Voyager) |
| 2025-12-11 | **[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2512.10696v2)**<br>记住我，完善我：面向经验驱动智能体演化的动态程序性记忆框架<br><sub>Procedural memory distills success/failure/comparative experiences, admits via LLM-judge validation, dedup and success-only addition, and deletes entries whose recall-time success utility falls below threshold.</sub> | [H30](patterns/sub/H30.md) | **55** ★★<br><sub>E19 X20 L6 C10</sub> | [code](https://github.com/agentscope-ai/ReMe) |
<!-- BOARD:END -->

## What is here

| Path | What |
|---|---|
| [`cards/`](cards/) | Per-paper **diagnosis cards** (GEPA, RRSI, Harness² so far): mechanism, author-reported evidence, our diagnosis (held-out, budget, leakage, strongest rebuttal), code check at a pinned SHA |
| [`patterns/`](patterns/) | **Harness pattern cards** — start at [overview](patterns/overview.md): 13 [main patterns](patterns/main/) and 36 [sub-patterns](patterns/sub/) induced from the corpus, with accept-vs-reject contrast from ICLR, plus [anti-patterns](patterns/anti-patterns.md) |
| [`docs/EVIDENCE.md`](docs/EVIDENCE.md) | Scope (tier A/B), and the task / retained / improver evidence levels |
| [`docs/MAINTAINING.md`](docs/MAINTAINING.md) | Daily maintenance rules for the maintainer agent and humans |
| [`research/`](research/) | The reproducible pipeline and its data (see below) |
| `main.py`, `src/` | Daily arXiv fetch + LLM relevance scoring, inherited from [daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest) ([usage](docs/digest-pipeline.md)); topics set in `config.example.json`, keywords in `keywords.json` |

## How the pattern cards were built

The method mirrors how [ResearchStudio-Idea](https://github.com/microsoft/ResearchStudio) derived its ideation patterns
(signature extraction → pattern discovery → operational cards), adapted to harness RSI:

1. **Corpus.** Every arXiv paper cited by 7 public RSI / self-evolving-agent lists, plus anchor works: **1,198 papers**
   (`research/corpus.jsonl`). Lists contribute arXiv ids only.
2. **Screening** from abstracts into tier A (a harness-level self-improvement loop), B (a component usable inside one),
   C (out of scope, incl. weight-level self-improvement): **A 400 / B 185**.
3. **Contrast set.** Curated lists hold few rejected papers, so all ICLR 2025–2026 submissions matching harness-RSI
   terms were pulled from OpenReview — **including 406 rejected and 222 withdrawn** — and screened the same way (193 A/B).
4. **Signatures.** For each A/B paper: the problem, the assumption it drops, an operational signature, the
   load-bearing mechanism, what is evolved, how candidates are proposed, selected and retained.
5. **Pattern induction** over 585 signatures, with outcome labels withheld: **13 main patterns / 36 sub-patterns**.
   An independent re-assignment of 120 papers agreed on the main pattern 86% of the time (Cohen's κ = 0.84).
6. **Quote-grounded evidence** for 200 outcome-labeled papers: every non-"unclear" judgment carries a verbatim
   quote, mechanically checked against the paper text (`research/check_evidence.py`).
7. **Contrast.** Accept rates per pattern within ICLR 2025–2026 (base rate 35%), `research/patterns/contrast.md`.
8. **Cards** distilled from the above. Cards never name a paper; `research/check_patterns.py` verifies every count and Δ against `contrast.json` and greps for member titles.

The strongest finding: **single-document critique-and-rewrite (H10)** is accepted at ICLR far below base (17% vs 34%, n=30) — the only signal whose CI excludes the base rate in every view. For most other patterns, *membership* does not predict acceptance; *execution* does (see each card's "accepted vs rejected gap").

Pipeline state and decisions: [`research/PIPELINE.md`](research/PIPELINE.md).

## Caveats

- Screening, signatures and assignments are LLM-produced. Inter-rater agreement measures how clear the taxonomy is
  *given* the signatures, not whether the signatures are right.
- Acceptance is not quality, and n is small: read the confidence intervals in `contrast.md` before believing a Δ.
- Rejected papers come mostly from OpenReview and were read from abstracts only; evidence and limitations are therefore
  not comparable across outcomes, and cards compare accepted vs rejected work on mechanism only.
- ICLR reviews could not be fetched in this run (OpenReview rate limits); each main card's "Reviewer expectations"
  panel is derived from the quote-grounded evidence audit and is marked pending.
- Paper full texts were used locally and are not redistributed here. ICLR 2027 in-review submissions appear as ids and
  titles only.

## Credits and license

MIT (see [LICENSE](LICENSE)), inherited from [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest).
Corpus seed lists: lobehub/awesome-rsi, ANative-Lab/Awesome-Self-Evolving-Agents, XMUDeepLIT/Awesome-Self-Evolving-Agents,
selfimproving-agent/Awesome-Self-Improving-Agents, wkqdzkd/Awesome-Reliable-Self-Evolving-Agents,
EvoMap/awesome-agent-evolution, iSEngLab/Awesome-Self-Evolving-Coding-Agents. Outcome labels from OpenReview.
