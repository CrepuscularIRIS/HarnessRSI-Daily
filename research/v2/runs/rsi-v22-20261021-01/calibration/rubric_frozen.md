# 冻结 rubric v1.0 — rsi-v22-20261021-01 生产批次评分锚点

状态：**frozen**（开发集 cal-dev 6 篇双席＋Opus 聚合后冻结；留出集 cal-h1/h2 用于一致性验收，不调权重）。
权重：SCORE_SPEC v2.2 初始提案不变 —— G15 / M20 / X20 / E45（E.measurement 10 / E.causality 15 / E.holdout 10 / E.statistics 5 / E.cost 5）。
基础 0/2/4 锚点沿用 SCORE_SPEC 分档表；以下为开发集实证后补充的本领域适用判据（记录依据见 batches/cal-dev/）。

## A1 无实验的框架/理论论文（开发集 1112.5309 案例归纳）

- 五个 E 子项一律 `not_reported`（rating 0），查找范围写明"全文含附录无实验/无外部验证报告"。
- 唯一例外：论文内被证明、且直接对应该子项命题的形式结果（如已证代价界），该子项至多 1，并引用定理/引理定位。
- "由构造保证"的性质只在 M/X 计一次，不在 E 重复计分。
- 此类论文不因设计优雅获得 E 分；总分低是分级如实反映，不是惩罚性调整。

## A2 单一缺陷对应单一证据子项（防重复扣分/重复加分）

- oracle / 真值重试信号 → E.holdout。
- 小样本 / 无误差线 → E.statistics。
- 预算/算力不对等的对照 → E.causality 与 E.cost。
- E.measurement 只判指标与验证器本身是否可信（含对平凡基线如多数类标签的核对）；搜索分奖励标签多样性这类"指标可被非目标因素满足"的问题归此处。
- 统计阶梯：1 = 有样本量与负结果但主结果无不确定性；2 = 测试集置信区间或重复运行失败计数，但无跨搜索/运行方差；3+ = 多种子＋区间＋显著性检验；0 = 完整查找后相应统计全缺。

## A3 范围判定按"被评价对象"（开发集 2410.15639、1605.03142 案例归纳）

- improver 的更新对象与产物**都是权重** → out_of_scope，即使过程中生成并复用了代码；被留存复用的"合并配方"不是 prompt/skill/tool/workflow/memory/评测器。
- 被评价的留存对象是非权重 harness 组件 → 在范围内，即使 improver 本身是权重训练的（claim_type 相应取 component_training / system_method）。
- 自我修改的激励/理论分析（无执行反馈闭环）→ out_of_scope；如需收录应走显式领域卡修订，不得低分代替范围裁定。

## A4 期望 ID 规范（消除两席同查不同名的伪冲突；cal-dev 95 项冲突中 53 项为 ID 不一致）

期望条目 ID 只允许三种语法，两席与聚合必须使用同一语法：

1. `rs:<原主卡id>/<RE-*>` —— 原 15+31 卡内建 reviewer expectation。
2. `rsi:<领域主卡id>/<S#|F#|H##子卡id或步骤id>` —— 本领域卡条件/失败模式衍生的检查问题。
3. `local:<paper_key>-<n>` —— 论文特有的审稿期望（来自该文自身实践/局限归纳），必须带 source_strength（observed_in_reviews / common_practice / single_source）与 applies_when。

禁止自造无命名空间 ID（如 SOL-REF-1 这类）。同一检查在两席若 ID 不同而实质相同，聚合记 `same_supported_fact`。

## A5 卡片结果泄漏防护

领域卡条件中引用的具体成员论文结果（例：make_the_improver_editable 的 F2 引用某成员 14% 结果）只作为检查问题的来源，**不得**当作被评论文自身的证据、锚点或计分依据。评某篇时卡片只提供"条件是否落实"的检查框架。

## 与既有规范的关系

- 本文件不改 SCORE_SPEC 权重与基础锚点表；生产批 manifest 的 rubric.hash 绑定本文件。
- 领域卡修订提案（H31 口径、H26/H27、make_the_improver_editable F2 重写去泄漏）积累于 calibration/card_revision_proposals.md，按 PATTERN_PROTOCOL 阶段末处理，批内不改卡。
- claim_type 三类解释、evidence_level 判定、claim_support 语义均按 SCORE_SPEC/EVIDENCE.md 原文执行。
