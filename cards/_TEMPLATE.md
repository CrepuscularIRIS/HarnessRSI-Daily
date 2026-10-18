---
# 机器可读字段：CI 会校验这些 key 是否存在、取值是否在枚举内
id: slug-lowercase
title: "Full Paper Title"
authors: "First Author et al."
first_seen: YYYY-MM-DD          # arXiv v1 / OpenReview 首次公开日期
arxiv: "XXXX.XXXXXvN"           # 本卡实际读的版本；无则 null
openreview: null                # forum URL；无则 null
code: "https://github.com/owner/repo"   # 官方仓库；无则 null
code_commit: null               # 核查时的 SHA；未核查则 null
license: null                   # 仓库 LICENSE 原文类型；未确认则 null
venue: "arXiv preprint"         # 或 "ICLR 2027 submission" 等
tier: A                         # A=Harness 级 RSI 本身；B=可直接用于该闭环的组件
evolved: [prompt]               # 子集：prompt|skill|tool|workflow|memory|code|evaluator|config
feedback: [ground_truth]        # 子集：ground_truth|llm_judge|execution|self_critique|human
evidence_level: task            # task|retained|improver —— 我们判定的、有证据支持的最高级
held_out: unclear               # yes|partial|no|unclear —— 最终报告集是否与选择集隔离
budget_matched: unclear         # yes|partial|no|unclear —— 与基线的比较是否预算对等
leakage_risk: unclear           # low|medium|high|unclear
code_status: released           # none|announced|released|verified_run
checked: YYYY-MM-DD
---

## 一句话
它让系统改自己的什么、用什么信号、怎样决定保留。

## 机制
提出 → 评测 → 接受/拒绝 → 留存 的闭环，各一两句。指出谁是"改进器"，改进器本身是否也被改。

## 作者报告的证据
只转述作者的数字，并写清模型、任务、预算。不跨论文比较数值。

## 我们的诊断
- **证据等级**：为什么是 task / retained / improver（定义见 [docs/EVIDENCE.md](../docs/EVIDENCE.md)）。
- **留出与泄漏**：选择集、最终报告集各是什么；评测器或答案是否对被优化的系统可见。
- **预算与失败处理**：基线是否同预算；失败或未评分的 trial 怎么计。
- **最强的反驳**：一个最可能推翻主要结论的理由。

## 代码核查
读了哪些文件（固定 SHA）、确认了什么、没确认什么。没跑就写"未运行"。

## 相对已有工作的增量
和哪 1–3 篇最接近的工作比，真正新的部分是什么。

## 适合 / 不适合
谁今天能用它、接入代价是什么；什么场景不该用。

## 一个值得验证的问题
一个具体、可检验的后续研究问题。

## 来源
- 论文链接（含版本）
- 代码链接（含 SHA）
