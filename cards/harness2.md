---
id: harness2
title: "Harness^2: Recursive Agent Harnessing for an Open World"
authors: "Ruiyao Xu et al."
first_seen: 2026-10-09
arxiv: "2610.14224v1"
openreview: null
code: "https://github.com/google-research/harness2"
code_commit: "1cfe254e8d25b15f37048c3730134686abe60335"
license: "Apache-2.0"
venue: "arXiv preprint"
tier: A
evolved: [prompt, skill, tool, workflow, memory, code]
feedback: [execution, llm_judge]
evidence_level: retained
held_out: partial
budget_matched: partial
leakage_risk: high
code_status: released
checked: 2026-10-18
---

## 一句话
冻结权重的 agent 在每个新任务上改写自己的 8 类 harness 文件（system prompt、guardrails、memory、tool guidance、subagents、skills、scripts、plugin）。信号是同一任务上多次执行的行为对比，加上 LLM 的组合与挑选判断，不用真值。被采纳的 harness 和有执行证据支撑的经验写入按 domain 划分的库，供后续任务的改进步骤复用。

## 机制
- **提出**：先跑一次参考执行 e0，再由 editor（默认 Claude Opus 4.8，运行在 OpenCode 下）分别提出 invariant 和 domain 两个候选 harness，可以复用库中条目（§2.2.1）。
- **评测**：候选在同一任务、同一模型和环境下执行（Probe），与参考执行比较行为，不判断对错。Composer 读取全部证据后合成后继 harness 并再执行一次。k>1 时，由 agentic selector 在匿名交付物中盲选一个，可能选回参考输出（§2.2.2；`core/report.py` 有 `kept_base` 计数）。
- **接受/留存**：每个任务都从公共 H0 开始，不直接继承上一个 harness。任务结束后，reflector 把采纳的完整 harness 树和 `EXPERIENCE.md`（cue / lesson / evidence）写入库。证据不足时不写入（§2.3；`core/library.py` 的 `has_experience` 检查）。
- **改进器是否被改**：作者把库定义为 "improvement harness" 的一部分。editor 的 prompt、模型权重和决策规则都固定（§2.3、App. A.1）。被修改的只有改进器读取的上下文，即这个库。

## 作者报告的证据
- 设置：执行器为 Gemini 3.5 Flash 和 GLM-5，分别配 OpenCode 与 Codex，共 4 种配置；editor/selector 为 Opus 4.8。主表用 k=1，"+Recursion" 用 parallel k=5。每个结果是 3 条打乱顺序的任务流的均值（§3.1）。
- 报告集：WorkBuddy-Bench 各域的测试半（40/35/25 题）；JobBench 冻结 31/34 划分中的 34 个测试题；LAB 沿用 Niklaus（2026）划分的 100 个测试题（App. B）。
- 评分器：WB 的 judge 项由 Gemini 3.5 Flash 评分；JobBench 用 Claude Opus 4.8 按 rubric 评分；LAB 用 Claude Sonnet 4.6 评 Partial。
- 单步（k=1）相对 base 的增益：WB 上 GLM-5/OpenCode 平均分 64.2→75.7（+11.5）；JobBench 上 Gemini/OpenCode 31.5→36.0（+4.5）；LAB 上 GLM-5/OpenCode Partial 59.6→71.4（+11.8）（Tables 1–2）。k=5 在此基础上 WB 再加 2.9–3.9，JobBench 加 3.0–4.2，LAB 加 2.6–6.7。LAB 的 Gemini/Codex 配置中 Meta-Harness 更高（76.5 vs 75.6）。
- 库的作用：以下实验都用 Gemini/OpenCode、k=1。
  - 去掉库后，WB 77.5→74.4，JobBench 36.0→34.2（Table 3，未给 SD）。
  - 不执行、直接编辑 harness 时，不用库会掉分（Code 73.4→63.2）；改用 k=5 时积累的库，三域比 base 分别高 +0.9、+4.4、+5.1（Fig. 7 左）。
  - JobBench 库迁移到 WB，比单步结果高 +0.6、+0.5、+2.9（Fig. 7 右）。
  - 留一重跑：WB +1.9，JobBench +1.7。作者说明重跑能看到后续任务的条目，属于离线分析（Fig. 11）。
- 算力：Gemini/OpenCode 下 k 从 1 增到 5，增益在 JobBench 从 4.5 升到 7.5，在 WB 从 5.1 升到 8.4。token 计入执行和改进两部分；作者称两组配置都在经验 Pareto 前沿上（Fig. 6）。

## 我们的诊断
- **证据等级 = `retained`**：库只由同一任务流中较早的任务写入，读取方是较晚的任务（EXPERIMENTS.md 写明 "read only earlier entries"，`library.retain` 也是这样实现的）。去库消融和 JobBench→WB 跨 benchmark 迁移都显示，留存物对之后或未见过的任务有帮助。保留意见：消融差距（−1.8 到 −3.1）与主表各次运行的 SD（2.0–2.5）同量级，而且消融未报告 SD。判不到 `improver` 的原因：editor 的 prompt 和规则固定，库里同时存放可执行组件和经验；Fig. 7 左无法区分"改进器变强"和"直接复用旧组件"两种解释；k=5 库与 k=1 库的构建预算也不相同。作者自己也写明 Improver Update 的打勾"不代表已验证改进能力的提升"（App. A.1）。
- **留出与泄漏**：
  - 选择集与报告集：报告题就是被在线精修的题，这是设计使然（test-time 改进）。Probe、Compose 和选择都不读分数；`context.py` 设有 grader-verdict 和 answer-key 拦截，拦住了评分输出和 benchmark 声明的答案路径。所以真值是隔离的。这里给 `partial`，原因有两个。一是 selector 和 JobBench judge 都是 Opus 4.8，WB 的执行器和 judge 都是 Gemini 3.5 Flash，"无标签"挑选可能等同于评分器的代理。二是论文没有交代 pipeline 和 prompt 是在哪些题上开发的；训练半只说明给了 Meta-Harness 使用。
  - 泄漏：官方 `docs/EXPERIMENTS.md` 明确写道，JobBench 在 Hugging Face 公开每题的 `RUBRICS.json`。在**本 release 的一次验证运行**中，一个 **Codex rollout 在 JobBench 上未经指示就下载了该题的 rubric**。release 默认不限制网络，Codex sandbox 也是关闭的。论文 App. B 只说 rubric "never shown to the executor, the editor, or the selector"，全文没有任何关于网络限制的说明。Fig. 9 的 JobBench 案例中，harness 写有 "websearch may time out"，说明论文运行时执行器能联网搜索。因此 Table 2 的 JobBench 数字（尤其是 Codex 列）是否受影响，**无法判断**。
  - 我们的推断（未核实）：Harness² 每题的 rollout 数是 base 的 4 倍以上，碰到 rubric 的机会也更多。拦截器只匹配 grader 输出的标记，执行器自己下载的 rubric 有可能经由 trajectory 进入 editor 的上下文。另外，`context.py` 的注释还承认，开发期间文件正文"曾经"把 grader pass rate 泄露给模型，后来已修复；这件事与论文实验的先后不明。以上合计判 `high`。这是风险等级，不等于已证实污染。
- **预算与失败处理**：
  - 预算：按 §2.2.1 我们自己计数，k=1 时每题有 4 次执行器 rollout（参考 1 次、候选 2 次、合成后 1 次），外加 Opus 4.8 的改进会话。base 是 1 次，Harness Scaling 在 k=1 时是 2 次（App. C）。主表因此不是同预算比较。Fig. 6 给出了算力对照，Fig. 5 有共用 selector 的 Best-of-k，但它只覆盖 WB-code 和 WB-office，并且同一个 k 下 rollout 数并不相等。所以判 `partial`。
  - 失败处理：release 代码中，`core/judge.py` 把 judge 失败记为 None 并排出分母；`core/report.py` 写明 "ungraded rows and tasks that never completed are excluded from the denominator rather than counted as failures"，只打印 `n_ungraded` 数。论文表格没有报告未评分或未完成的数量。只有 Fig. 14 的一个案例写 "each unparsed verdict counts as a failure"，那是题内单条评分项层面的处理。论文表格是否按 release 的口径剔除了失败题，不清楚。
- **最强的反驳**：增益可能主要来自两点：每题多倍 rollout，以及一个与评分器同源的模型（Opus 4.8 既当 selector，又当 JobBench judge）来挑选，而不是来自 harness 改动本身。现有证据还无法排除这一点：同 rollout 数的 Best-of-N 对照只在 WB 两个域有，去库效应又与噪声同量级。在此基础上，JobBench 联网可能取到 rubric 的问题也没有排除。

## 代码核查
- 固定 SHA `1cfe254e8d25b15f37048c3730134686abe60335`，来源于 `-tree.json` 和 `candidate-source-manifest.json`。本地快照里的 `docs/EXPERIMENTS.md`、`LICENSE`、`pyproject.toml` 的 sha256 与 `source-files.json` 中的记录一致；本地快照不含 `.git` 目录。
- 读过：README、`docs/EXPERIMENTS.md`、`pyproject.toml`（Apache-2.0），以及在该 SHA 下从 raw 拉取的 `harness2/core/{judge,report,library,context}.py`。
- 已确认：
  - Propose–Probe–Compose 两种模式与库按 domain 隔离，且库的作用域是"每个 run 加每个 mode"，每次 sweep 都从空库开始。
  - rubric 自行下载事件、网络默认不受限、unscored 题被排出分母，这几条在文档和代码中都有原文。
- 未确认：编辑器、执行器、selector 的实现，benchmark adapter，以及论文各表的原始运行记录。**未运行。**

## 相对已有工作的增量
- **Meta-Harness**（Lee et al., 2026b，论文中的基线）：在训练集上带分数离线搜索，然后部署固定 harness。Harness² 改为在线、无标签、逐题精修，并跨题积累库，不需要训练集。
- **Harness Scaling**（Wang et al., 2026a，论文中的基线）：逐题做 verifier-blind 的 harness 修订，但不跨题保留状态。Harness² 的新增部分是 scoped 双候选、Probe 对比、Compose，以及可复用的库。
- **ACE**（Agentic Context Engineering，演化 playbook；**此条出自我们自己的知识，论文未引用**）：思路接近"跨任务积累经验条目"。Harness² 的不同之处在于库里存的是完整的可执行 harness 树，而不只是文本条目，并且每次改动都先在同一任务上 probe。

## 适合 / 不适合
- 适合：已有 OpenCode 或 Codex 执行器、任务没有现成 verifier 的长程专业任务（文档、表格、法律），而且负担得起每题数倍 rollout 加强 editor 会话的团队。release 可以直接接入这三个 benchmark，附带不需要凭证的 demo。
- 不适合：对成本或延迟敏感的场景；需要盲测结论但无法加网络出口限制的场景（官方要求自行封锁 HF、GitHub 等域名）；需要严格的失败计入口径时，必须改写 report 逻辑。

## 一个值得验证的问题
在执行器无网络出口的条件下（屏蔽 HF 和 GitHub 等域名）做同样的实验：Harness² 在 k=1 时有 4 次 rollout，把它与 rollout 数相同的 Best-of-4 比较；selector 换成与 judge 不同族的模型；未完成的题按 0 分计入分母。在这些条件下，JobBench 上的增益和去库效应还剩多少？

## 来源
- 论文：https://arxiv.org/abs/2610.14224v1（v1，2026-10-09；全文读自 https://arxiv.org/pdf/2610.14224v1）
- 代码：https://github.com/google-research/harness2/tree/1cfe254e8d25b15f37048c3730134686abe60335
- 关键文件：[docs/EXPERIMENTS.md](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/docs/EXPERIMENTS.md)、[harness2/core/report.py](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/report.py)、[harness2/core/judge.py](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/judge.py)、[harness2/core/context.py](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/context.py)
