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

Out of 585 scored so far (16 at ★★★ ≥ 70). Full board, grouped by pattern: [papers/](papers/README.md). Score (0–100) = **E**vidence (50) + e**X**ecution against the pattern card (30) + evidence **L**evel (10) + **C**ode (10); every judgment is quote-backed — see [SCORE_SPEC](research/SCORE_SPEC.md). It measures what a paper reports and how it executes its move, not the value of the idea.

| Date | Paper | Pattern | Score | Code |
|---|---|---|---|---|
| 2026-04-10 | **[M$^\star$: Every Task Deserves Its Own Memory Harness](https://arxiv.org/abs/2604.11811v2)**<br>M*：每个任务都值得拥有自己的记忆框架<br><sub>Evolves task-specific memory programs (Python schema, storage logic, instructions) via reflective coding-agent mutation over a softmax-sampled population, selected on static validation, reported on held-out test.</sub> | [H21](patterns/sub/H21.md) | **90** ★★★<br><sub>E40 X30 L10 C10</sub> | [code](https://github.com/wbopan/mstar) |
| 2026-05-28 | **[GRASP: Gated Regression-Aware Skill Proposer for Self-Improving LLM Agents](https://arxiv.org/abs/2605.29668v3)**<br>GRASP：面向自我改进LLM智能体的门控回归感知技能提议器<br><sub>Edits a bounded skill library from grouped failures, committing an edit only if it nets fixes over regressions on a held-out probe under a hard regression budget.</sub> | [H30](patterns/sub/H30.md) | **84** ★★★<br><sub>E41 X27 L6 C10</sub> | [code](https://github.com/jomoll/GRASP) |
| 2026-04-20 | **[Co-evolving Agent Architectures and Interpretable Reasoning for Automated Optimization](https://arxiv.org/abs/2604.17708v2)**<br>协同进化智能体架构与可解释推理以实现自动化优化<br><sub>OR-agent workflows become AOE graphs; a fitness-weighted architecture graph is grown and pruned while a population of reasoning trajectories evolves by path recombination and semantic mutation.</sub> | [H17](patterns/sub/H17.md) | **81** ★★★<br><sub>E45 X20 L6 C10</sub> | — |
| 2026-08-24 | **[AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](https://arxiv.org/abs/2608.23041v1)**<br>AutoSaddler：基于智能体执行轨迹的持久更新式自动Harness优化<br><sub>Mini-batch harness optimization: an agent diagnoses failure traces with harness source, writes typed prompt/tool/middleware patches, verifies on the batch then a dev set, and logs lessons in an evolution DAG.</sub> | [H12](patterns/sub/H12.md) | **79** ★★★<br><sub>E33 X30 L6 C10</sub> | [code](https://github.com/microsoft/AutoSaddler) |
| 2026-02-08 | **[Learning to Continually Learn via Meta-learning Agentic Memory Designs](https://arxiv.org/abs/2602.07755v1)**<br>通过元学习智能体记忆设计实现持续学习的学习<br><sub>A meta agent samples an archive of code-level memory designs (update/retrieve), proposes new ones, scores each by a fixed agent's deployment success after memory collection.</sub> | [H21](patterns/sub/H21.md) | **75** ★★★<br><sub>E28 X27 L10 C10</sub> | [code](https://github.com/zksha/alma) |
| 2026-03-19 | **[Hyperagents](https://arxiv.org/abs/2603.19461v1)**<br>超智能体（Hyperagents）<br><sub>A single editable program holding task agent and meta agent rewrites both, including its own modification procedure; variants are archived DGM-style and scored on task performance.</sub> | [H20](patterns/sub/H20.md) | **74** ★★★<br><sub>E31 X23 L10 C10</sub> | [code](https://github.com/facebookresearch/Hyperagents) |
| 2026-04-23 | **[AEL: Evolving Agent Harness in Open-Ended Environments](https://arxiv.org/abs/2604.21725v2)**<br>AEL：在开放式环境中进化智能体框架<br><sub>Thompson-sampling bandit picks memory-retrieval policies per episode; slow LLM reflection diagnoses degradation and injects new retrieval policies as bandit arms; learning frozen at test.</sub> | [H21](patterns/sub/H21.md) | **74** ★★★<br><sub>E32 X22 L10 C10</sub> | [code](https://github.com/WujiangXu/AEL) |
| 2026-05-19 | **[Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576v3)**<br>库漂移：诊断并修复自演化LLM技能库中的一种静默失效模式<br><sub>Frozen LLM writes, routes, and retires its own skills; outcome-driven retirement, bounded active cap and a meta-skill authoring prior govern which skills persist.</sub> | [H30](patterns/sub/H30.md) | **74** ★★★<br><sub>E35 X23 L6 C10</sub> | [code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet) |
| 2023-08-20 | **[ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144v3)**<br>ExpeL：大语言模型智能体是经验学习者<br><sub>Agent gathers train-task trajectories, contrasts failures with successes into an insight list maintained by add/edit/upvote/downvote operations, and recalls insights plus successful trajectories on unseen tasks.</sub> | [H00](patterns/sub/H00.md) | **72** ★★★<br><sub>E32 X24 L6 C10</sub> | [code](https://github.com/LeapLabTHU/ExpeL) |
| 2026-05-21 | **[Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents](https://arxiv.org/abs/2605.22166v3)**<br>适配接口而非模型：确定性LLM智能体的运行时harness适配<br><sub>An evolution LLM turns recurring training-trajectory failures into edits across four runtime-harness layers; a candidate replaces the incumbent only if training-batch accuracy improves, then freezes.</sub> | [H12](patterns/sub/H12.md) | **72** ★★★<br><sub>E29 X27 L6 C10</sub> | [code](https://github.com/Tianshi-Xu/Life-Harness) |
| 2026-07-06 | **[EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202v1)**<br>EvoAgentBench：通过能力迁移评测智能体自进化<br><sub>Benchmark builds trace-grounded Ability Graphs so every held-out task has train-side procedural support, then measures transfer gain of skill/memory/prompt evolution methods over no-evolution.</sub> | [H33](patterns/sub/H33.md) | **72** ★★★<br><sub>E29 X27 L6 C10</sub> | [code](https://huggingface.co/datasets/EverMind-AI) |
| 2026-06-15 | **[REFLEX: Reflective Evolution from LLM Experience](https://arxiv.org/abs/2606.16496v2)**<br>REFLEX：基于LLM经验的反思式进化<br><sub>Program evolution where a vision Critic diagnoses behavioral-evidence images, BM25 retrieves credited code snippets from a persistent Skill Memory, an Actor writes children; snippets credited by child-parent fitness change.</sub> | [H15](patterns/sub/H15.md) | **71** ★★★<br><sub>E42 X23 L6 C0</sub> | — |
| 2026-08-04 | **[PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](https://arxiv.org/abs/2608.04003v1)**<br>PAST-Bench：评测个人智能体递归自我改进的基础能力<br><sub>Benchmark of fresh-session task families with matched persistence-on/off runs and trace-level mechanism evidence; proposes Hermes+ with five memory/skill read-write interventions.</sub> | [H33](patterns/sub/H33.md) | **71** ★★★<br><sub>E27 X28 L6 C10</sub> | [code](https://github.com/Gen-Verse/PAST-Bench) |
| 2026-02-02 | **[MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474v2)**<br>MemSkill：为自进化智能体学习并进化记忆技能<br><sub>Memory operations become an evolving skill bank: RL controller selects skills, fixed LLM designer refines/adds skills from hard cases, rolling back skill banks that degrade performance.</sub> | [H21](patterns/sub/H21.md) | **70** ★★★<br><sub>E27 X23 L10 C10</sub> | [code](https://github.com/ViktorAxelsen/MemSkill) |
| 2026-06-03 | **[The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?](https://arxiv.org/abs/2606.04455v1)**<br>元智能体挑战：当前智能体能否自主开发智能体？<br><sub>Benchmark where a code meta-agent iteratively programs an agent artifact against a dev-set evaluation API, scored on a hidden test split with anti-reward-hacking isolation and auditing.</sub> | [H34](patterns/sub/H34.md) | **70** ★★★<br><sub>E27 X27 L6 C10</sub> | [code](https://github.com/ant-research/meta-agent-challenge) |
| 2026-06-24 | **[The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294v3)**<br>红皇后哥德尔机：智能体与其评估器的协同进化<br><sub>Self-modifying agent search co-evolves learned evaluators in epochs; a challenger evaluator replaces the frozen one only if it scores higher on a held-out labeled anchor, erasing dependent records.</sub> | [H25](patterns/sub/H25.md) | **70** ★★★<br><sub>E34 X23 L10 C3</sub> | — |
| 2026-04-01 | **[Meta-TTL: Meta-Learning Self-Improvement Policies for Language Agents](https://arxiv.org/abs/2604.00830v4)**<br>Meta-TTL：为语言智能体元学习自我改进策略<br><sub>Meta-learns the natural-language meta-prompt governing cross-episode prompt rewriting via reflective meta-training; candidates replace the incumbent only if balanced validation TTL improvement is positive.</sub> | [H19](patterns/sub/H19.md) | **69** ★★<br><sub>E26 X23 L10 C10</sub> | [code](https://github.com/zzzlou/meta-ttl) |
| 2026-08-19 | **[SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution](https://arxiv.org/abs/2608.18933v1)**<br>SkillForge：面向项目特定问题修复的自蒸馏智能体<br><sub>Before real issues arrive, an SWE agent solves test-grounded synthetic issues made by masked re-implementation of repo code, distilling entity-linked global and local skills injected on file access.</sub> | [H02](patterns/sub/H02.md) | **69** ★★<br><sub>E31 X22 L6 C10</sub> | [code](https://github.com/cslsolow/SkillForge) |
| 2026-06-16 | **[FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](https://arxiv.org/abs/2606.17642v6)**<br>FinAcumen：基于自进化经验记忆框架的金融多模态推理<br><sub>Financial VLM agent distills gold-scored training trajectories into a frozen memory of strategies and cautionary rules, injected only above a similarity threshold with fallback, alongside deterministic tools.</sub> | [H05](patterns/sub/H05.md) | **68** ★★<br><sub>E29 X23 L6 C10</sub> | [code](https://github.com/CamelliaLilium/FinAcumen) |
| 2022-03-14 | **[GrIPS: Gradient-free, Edit-based Instruction Search for Prompting Large Language Models](https://arxiv.org/abs/2203.07281v2)**<br>GrIPS：面向大语言模型提示的无梯度、基于编辑的指令搜索<br><sub>Greedy/beam local search applies random phrase-level edits (delete, swap, paraphrase, add) to task instructions, keeping the edit that raises balanced-accuracy-plus-entropy on a score set.</sub> | [H13](patterns/sub/H13.md) | **67** ★★<br><sub>E31 X20 L6 C10</sub> | [code](https://github.com/archiki/GrIPS) |
| 2026-03-29 | **[EffiSkill: Agent Skill Based Automated Code Efficiency Optimization](https://arxiv.org/abs/2603.27850v1)**<br>EffiSkill：基于智能体技能的自动化代码效率优化<br><sub>Mines operator and meta skills by contrasting slow/fast program pairs, clusters and merges them into a library, then retrieves and composes skills to optimize unseen programs.</sub> | [H00](patterns/sub/H00.md) | **67** ★★<br><sub>E25 X26 L6 C10</sub> | — |
| 2026-04-15 | **[Memory Transfer Learning: How Memories are Transferred Across Domains in Coding Agents](https://arxiv.org/abs/2604.14004v1)**<br>记忆迁移学习：编码智能体中记忆如何跨领域迁移<br><sub>Evaluates coding agents with leave-one-benchmark-out memory pools in four abstraction formats; abstract insights transfer across domains while raw trajectories cause negative transfer.</sub> | [H32](patterns/sub/H32.md) | **67** ★★<br><sub>E24 X27 L6 C10</sub> | [code](https://github.com/KangsanKim07/MemoryTransferLearning) |
| 2026-06-08 | **[Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://arxiv.org/abs/2606.09365v4)**<br>经验成就技能：通过自演化技能记忆实现可泛化的医疗智能体推理<br><sub>Medical agent distills trajectories into a branched skill repo, credits skills by category-normalized outcome advantage, and governs retrieval, promotion, merging, deprecation and capacity.</sub> | [H30](patterns/sub/H30.md) | **67** ★★<br><sub>E28 X23 L6 C10</sub> | [code](https://github.com/manglu097/SkeMex) |
| 2026-06-17 | **[Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/abs/2606.28374v1)**<br>基于留出选择的递归自演化智能体<br><sub>Frozen LLM rewrites a three-layer strategy/skills/playbook state from its trajectories, committing only strict improvements on a disjoint validation split with empty-state fallback.</sub> | [H31](patterns/sub/H31.md) | **67** ★★<br><sub>E35 X23 L6 C3</sub> | — |
| 2026-06-29 | **[ManimAgent: Self-Evolving Multimodal Agents for Visual Education](https://arxiv.org/abs/2606.30296v2)**<br>ManimAgent：面向可视化教育的自演化多模态智能体<br><sub>A Manim-coding agent writes VLM-gated success rationales and validated failure-to-success lessons into a dual-channel memory, frozen and evaluated read-only on disjoint probe tasks.</sub> | [H00](patterns/sub/H00.md) | **67** ★★<br><sub>E25 X26 L6 C10</sub> | [code](https://github.com/jwj1342/Paper2Manim) |
| 2026-08-25 | **[Meta$^n$: Recursive Self-Improvement through Emergent Depth](https://arxiv.org/abs/2608.24735v1)**<br>Meta^n：通过涌现深度实现递归自我改进<br><sub>A fixed meta-operation repeatedly reads solver-stack traces and code, writing new layers (pre-process plus helper library); depth grows until no improvement, with an archive over layer chains.</sub> | [H19](patterns/sub/H19.md) | **67** ★★<br><sub>E31 X20 L6 C10</sub> | [code](https://github.com/minnesotanlp/meta-n) |
| 2026-07-15 | **[HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution](https://arxiv.org/abs/2607.13683v2)**<br>HarnessBank：带门控验证的语义基因库搜索用于智能体框架自进化<br><sub>Evolver agent diagnoses task-agent failures and proposes harness patches; a semantic gene bank keyed by component and pathology keeps elites, admitted via validity, activation and paired-significance gates.</sub> | [H16](patterns/sub/H16.md) | **66** ★★<br><sub>E27 X30 L6 C3</sub> | — |
| 2026-09-03 | **[DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://arxiv.org/abs/2609.04094v1)**<br>DRACO：面向长时程智能体训练的动态评分细则细粒度信用分配<br><sub>Outcome-blind GRPO for tool agents: a frozen judge generates per-task rubrics from rollouts, drops criteria nobody failed, and redistributes advantage to the steps each verdict cites.</sub> | [H24](patterns/sub/H24.md) | **66** ★★<br><sub>E33 X17 L6 C10</sub> | [code](https://github.com/IBM/draco) |
| 2025-09-11 | **[SEDM: Selective Self-Evolving Distributed Memory for Agents](https://arxiv.org/abs/2509.09498v4)**<br>SEDM：面向智能体的选择性自演化分布式记忆<br><sub>Shared agent-society memory admits entries via paired replay A/B tests, reweights/retires them by measured utility, and a calibrated gate decides per task whether to inject memory.</sub> | [H29](patterns/sub/H29.md) | **65** ★★<br><sub>E34 X25 L6 C0</sub> | — |
| 2025-10-17 | **[EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079v3)**<br>EvolveR：基于经验驱动生命周期的自进化LLM智能体<br><sub>Agent self-distills success/failure trajectories into a scored, deduplicated principle base it retrieves via a search action, while GRPO trains the policy on the same online trajectories.</sub> | [H28](patterns/sub/H28.md) | **65** ★★<br><sub>E27 X22 L6 C10</sub> | [code](https://github.com/Edaizi/EvolveR) |
<!-- BOARD:END -->

## What is here

| Path | What |
|---|---|
| [`papers/`](papers/README.md) | **Paper board**: every scored paper, grouped by pattern, with Chinese title, one-line summary, score breakdown and code link |
| [`cards/`](cards/) | Per-paper **diagnosis cards** (GEPA, RRSI, Harness² so far): mechanism, author-reported evidence, our diagnosis (held-out, budget, leakage, strongest rebuttal), code check at a pinned SHA |
| [`patterns/`](patterns/) | **Harness pattern cards** — start at [overview](patterns/overview.md): 13 [main patterns](patterns/main/) and 36 [sub-patterns](patterns/sub/) induced from the corpus, with accept-vs-reject contrast from ICLR, plus [anti-patterns](patterns/anti-patterns.md) |
| [`docs/EVIDENCE.md`](docs/EVIDENCE.md) | Scope (tier A/B), and the task / retained / improver evidence levels |
| [`docs/PIPELINE.md`](docs/PIPELINE.md) · [`docs/agents/`](docs/agents/ROLES.md) | How new papers flow in (collector → inbox → ingest → screen → signature → pattern → quote-backed judgment → score → board), and the prompts for the collector and maintainer agents |
| [`inbox/`](inbox/README.md) | Candidate papers waiting to be processed |
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
