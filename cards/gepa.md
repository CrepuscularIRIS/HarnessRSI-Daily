---
# 机器可读字段：CI 会校验这些 key 是否存在、取值是否在枚举内
id: gepa
title: "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning"
authors: "Lakshya A Agrawal et al."
first_seen: 2025-07-25
arxiv: "2507.19457v2"
openreview: null
code: "https://github.com/gepa-ai/gepa"
code_commit: "f1cfdee2856e9dc4b5b4dc5cc2e391d0aa20d819"
license: "MIT"
venue: "ICLR 2026 (Oral)"
tier: B
evolved: [prompt]
feedback: [ground_truth, execution]
evidence_level: retained
held_out: partial
budget_matched: partial
leakage_risk: low
code_status: released
checked: 2026-10-18
---

## 一句话
GEPA 改的是复合 AI 系统里各模块的 instruction prompt。信号是指标分数加上 feedback function `μ_f` 返回的评测文本，例如编译错误、未满足的约束、还没检索到的 gold 文档。一个新候选要先在 minibatch 上严格变好才进入候选池，在 `D_pareto` 上评分之后，通过逐实例 Pareto 前沿参与后续采样。预算用完时，返回 `D_pareto` 平均分最高的那个候选。

## 机制
- **提出**：用 Pareto 采样选出父候选，再按 round-robin 选一个模块，在 `D_feedback` 的 minibatch（b=3）上跑一遍并收集轨迹和 `μ_f` 文本。反思 LM 用固定的 meta-prompt（附录 C）重写这个模块的 instruction。可选的 Merge 会把两条谱系里各自改过的模块拼成一个新候选（附录 D.1）。
- **评测**：新候选和父候选在同一个 minibatch 上比较。
- **接受**：只有 minibatch 总分严格高于父候选时才接受，然后在整个 `D_pareto`（论文里就是验证集）上评分并记录祖先。
- **留存**：所有被接受的候选都留在候选池里。`SelectCandidate` 先保留在至少一个实例上得分最高的候选，剪掉被支配的，再按"领先实例数"的比例随机采样，这样后代会继承祖先积累下来的规则。
- **改进器**：反思 LM、meta-prompt 和选择策略都是固定的，改进器本身不被修改。论文写"optimized entirely for (and using) the weaker Qwen3-8B"，看上去反思 LM 和任务模型是同一个，但正文没有单独说明。

## 作者报告的证据
以下都是作者自己的数字。任务是 HotpotQA / IFBench / HoVer / PUPA / AIME-2025 / LiveBench-Math，划分为 train 150 / val 300 / test 300 左右（IFBench test 294，PUPA 111/111/221，AIME 用 2022–2024 年题目对半分 train/val，以 2025 年 30 题 ×5 作为 test）。
- **Qwen3 8B（表 1）**：test 聚合分 baseline 48.70，GRPO 51.26，MIPROv2 46.60，GEPA 54.85，GEPA+Merge 52.40。GRPO 固定 24,000 rollouts（LoRA r=16，500 步）。GEPA 每个任务的预算在 1,839 到 7,051 rollouts 之间，平均 3,936。GEPA 在 AIME 上输给 GRPO（32.00 对 38.00）。GEPA+Merge 在 IFBench 上降到 28.23，作者归因于两个模型共用了同一组超参。
- **GPT-4.1 Mini（表 2）**：聚合分 baseline 53.03，MIPROv2 58.67，TextGrad 59.14，Trace 56.30，GEPA 65.22，GEPA+Merge 66.36。在 Qwen 上优化、迁移到 4.1 Mini 评测的 GEPA-Qwen-Opt 是 62.03。表 2 全部实验总花费不到 $500（附录 E.3）。
- **候选选择消融（表 3，Qwen3 8B，4 个任务，同预算）**：SelectBestCandidate 54.89，BeamSearch(N=4) 53.95，Pareto 61.28。
- **样本效率**：作者说 GEPA 的大部分 rollout 花在验证集上，只算 train rollouts 的话，79 到 737 次就达到最优。整次优化中反思 LM 的调用次数为 17–92（附录 N）。
- **5.1 节 kernel 推理期搜索（GPT-4o）**：NPUEval 平均向量利用率 30.52%（Sequential10 为 4.25%）。KernelBench 35 题上 fast_1 超过 20%。这一节明确让 `D_train = D_pareto =` 全部任务，没有留出集。
- 正文和附录都没有报告随机种子数、重复次数或方差。

## 我们的诊断
- **证据等级 `retained`**：留存下来的产物（最终 prompt）是在验证集上选出的，在不相交的 test split 上仍然有提升。IFBench 的 test 含 58 个训练里没有的新约束，另外还有跨模型迁移结果（表 2），可以算作较弱的跨分布证据。不判 `improver`，因为反思机制本身没有被修改，也没有"改进后的改进器"的对照实验。这里的"后续任务"是同一任务分布下没见过的实例，不是新任务，而且每个设置只有单次运行，这些都限制了 `retained` 的强度。
- **留出与泄漏**：选择集是 `D_pareto` 也就是 val。优化器只看到 val 的分数，看不到内容，反思用的轨迹全部来自 train。最终报告用 test。这部分划分是干净的，所以 `leakage_risk` 判为 `low`。`held_out` 判为 `partial` 有三个原因。(1) 5.1 节的 kernel 结果直接在被优化的任务集上报告。(2) GEPA 和 GEPA+Merge 两个变体都在 test 上报告，摘要里"up to 20%"取的是两者中较好的那个，Merge 是否启用并没有通过 val 预先决定。(3) GRPO 的超参是"manually explore"的，正文没说依据哪个集合。还有一点：代码在 `valset=None` 时会让 `val_loader = train_loader`（`api.py` 第 231 行），用户不显式传 val 的话，选择集就等于训练集。
- **预算与失败处理**：和 MIPROv2、Trace、TextGrad 的比较是按 rollout 对齐的，GEPA 的上限设为 MIPROv2 的实际用量，差距在 10.15% 以内，这部分算 yes。和 GRPO 的比较不对等：GRPO 固定 24k rollouts，GEPA 少用 4–35 倍，这本身就是论文要论证的点。但 rollout 数不等于算力，反思 LM 的调用也不计入 rollout 预算。代码里 `max_metric_calls` 只统计 `increment_evals`，也就是父候选的 minibatch、子候选的 minibatch 和 valset 评测，所以综合判 `partial`。失败处理方面，被拒绝的提案所消耗的评测都计入了预算。代码约定单个样本失败时返回回退分（例如 0.0），并计入均值的分母。系统性异常默认会抛出（`raise_on_exception=True`）。论文本身没有说明解析失败或评测失败怎么计分。
- **最强的反驳**：GEPA 和 GRPO 的差距同时混进了"算法"和"监督信息量"两个因素。HoVer 和 HotpotQA 是 GEPA 相对 GRPO 领先最多的两个任务，在这两个任务上，`μ_f` 会把"还缺哪些 gold 文档"直接写成文本交给反思 LM，而 GRPO 只拿到标量 reward。Trace 和 TextGrad 拿到了同样的反馈，GRPO 没有。再加上每个设置只跑一次、test 集也小（AIME 只有 30 题 ×5），在 IFBench（+2.73）、LiveBench（+0.69）这类小差距上，"超过 RL"的结论还不稳。

## 代码核查
- 本地快照 `sources/gepa-ai__gepa` 只有 3 个文件：`LICENSE`、`pyproject.toml`（包版本 0.1.4）、`src/gepa/optimize_anything.py`。它们的 sha256 和 `source-files.json` 中 SHA `f1cfdee` 下的记录一致。本地快照没有 `.git`，SHA 取自 `candidate-source-manifest.json`。
- 我另外从 `raw.githubusercontent.com/gepa-ai/gepa/f1cfdee…/` 拉取并阅读了这些文件：`core/engine.py`、`core/state.py`、`core/adapter.py`、`api.py`、`gepa_utils.py`、`strategies/{acceptance,candidate_selector,eval_policy}.py`、`proposer/reflective_mutation/reflective_mutation.py`。
- 已确认的行为：
  - 默认的 `StrictImprovementAcceptance` 要求 minibatch 分数之和严格变大。
  - `ParetoCandidateSelector` 的默认 rng 是 `Random(0)`，并实现了支配剪枝，和算法 2 对得上。
  - 默认的 `FullEvaluationPolicy` 按 val 平均分选出最优候选。
  - 预算只统计评测调用。
  - `optimize_anything` 的 `test_set` 在预算之外评分，不会进入 eval server。
- 没有确认的部分：
  - 仓库目录树里没有找到复现论文表 1–3 的实验脚本。论文实验基于 DSPy 实现，GRPO 用的是 Ziems et al. / SkyRL 的实现。
  - 当前 0.1.4 版本已经扩展出 `oa/engines`（meta_harness、autoresearch 等），我没有逐项核对它和论文版本是否等价。
  - README 写的"100–500 evaluations vs. 5,000–25,000+ for GRPO"和论文表 1 的总预算对不上，在论文里找不到出处。
- **未运行。**

## 相对已有工作的增量
（以下比较依据论文第 6 节和附录 E.4，加上我们自己对这些工作的了解。后者另行标注。）
- **MIPROv2**：用 TPE 贝叶斯优化在 bootstrap 出的 instruction 和 demo 组合里搜索，依据是全局标量分。GEPA 只改 instruction，但利用了评测器的文本反馈。作者报告在同 rollout 预算下 GEPA 全面胜出，生成的 prompt 最多短 9.2 倍。
- **TextGrad**：反传文本梯度，作者把它的选择方式归为 SelectBestCandidate 一类。GEPA 新增的是逐实例的 Pareto 采样，表 3 的同框架消融单独隔离了这一项的贡献。
- **EvoPrompt / PromptBreeder 一类进化式 prompt 方法**（我们的知识，论文只引了 EvoPrompt）：它们也维护候选种群。GEPA 不同的地方在于按模块做定向变异、使用 `μ_f` 的评测轨迹，以及利用谱系信息的 Merge。
- 总结：真正新的部分是"逐实例 Pareto 前沿 + 评测轨迹文本反馈"这个组合，以及在严格同预算条件下和 MIPROv2 做的对比。

## 适合 / 不适合
- **适合**：已经有一个可调用的系统（Agent、DSPy 程序或任意文本组件），并且能写出带诊断文本的 evaluator 的团队。接入的代价主要是实现 `GEPAAdapter.evaluate` / `make_reflective_dataset`，或者 `optimize_anything` 的 evaluator，外加准备一个独立的 val 集和 test 集。可以把它当作 harness 闭环里的"单组件优化器"。
- **不适合**：拿不到可靠指标或可靠反馈文本的开放任务。GEPA 只优化 evaluator，evaluator 有偏时它会把这个偏差也一起优化进去。val 很小或评测噪声很大的场景也不适合，因为 Pareto 前沿是按单个实例记录最高分的，噪声会被当成"领先"。它也不能替代版本晋升和部署流程。

## 一个值得验证的问题
在 HoVer 和 HotpotQA 上，把 `μ_f` 换成只返回分数、不带任何文本（`μ_f = μ`），保持 rollout 预算和种子数一致（每个设置 ≥3 个 seed）。这时 GEPA 相对 MIPROv2 和 GRPO 的 test 优势还剩多少？剩下的部分才能归给"反思 + Pareto 搜索"，减掉的部分应该归给"更丰富的监督文本"。

## 来源
- 论文：https://arxiv.org/abs/2507.19457v2（HTML 全文 https://arxiv.org/html/2507.19457v2；v1 为 2025-07-25，v2 为 2026-02-14）
- 代码：https://github.com/gepa-ai/gepa/tree/f1cfdee2856e9dc4b5b4dc5cc2e391d0aa20d819
