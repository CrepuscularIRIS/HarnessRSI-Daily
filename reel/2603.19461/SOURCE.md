# SOURCE — 2603.19461 Hyperagents

- 版本：arXiv 2603.19461**v1**（2026-03-19），钉定全文 `research/fulltext/review-runs/rsi-v22-20261021-01/materials/2603.19461.txt`（私有缓存，不提交）。
- 阅读范围：§1–§7 全文；附录 B（DGM 指令生成）、D.1–D.4（模型、成本、imp@k 定义、迁移 agent 选择）；E.3 只读 §5.2 引用的代码片段说明。
- 初筛记录：L1 `research/scoring/runs/rsi-l1-20261022-03/batches/b038.jsonl`；L2 `batches/l2b06.jsonl`（P3 / confirmed / to_l3）；L3 `selection.md` 终选 #5、`l3-final.tsv`。本篇无 correction。

| 画报内容 | 原文位置 |
|---|---|
| 问题：DGM 假设“任务能力↑＝自改能力↑”只在编码域成立；指令生成步骤手写且不可改 | §1 第 2 段；§2 Self-referential meta-learning；附录 B |
| hyperagent＝task+meta 合成单一可编辑程序 | §1、§3 Hyperagents |
| 对照 w/o self-improve：meta 全程固定为初始 meta；w/o open-ended 去掉归档 | §4.1 |
| 外环（父代选择、评估）固定、不可改 | §3 末段；§7 第二条限制 |
| 初始 task agent 单次 FM 调用；meta 读仓库与历史评估 | §4 |
| 100 代、5 次运行、中位数 + 95% bootstrap CI（1,000 次重采样）、Wilcoxon | §5 开头；§5.1 |
| 测试集结果表全部数字（0.0/0.060；DGM 0.0(0.0–0.510)/0.0(0.0–0.090)；DGM-custom 0.590(0.570–0.650)/0.348(0.305–0.385)；w/o self-improve 0.0(0.0–0.130)/0.213(0.180–0.348)；w/o open-ended 0.0(0.0–0.560)/0.116(0.0–0.348)；DGM-H 0.710(0.590–0.750)/0.372(0.355–0.436)） | §5.1（对应 Fig. 2 右） |
| 显著性：DGM-H 对 DGM、w/o self-improve、w/o open-ended p<0.05；对 DGM-custom p>0.05 | §5.1 |
| 按验证分（无验证集时按训练分）选最佳 agent 后测试 | §5.1；§4.2 |
| 自改/评估模型：Claude 4.5 Sonnet；GPT-4o（论文评审）、Claude 4.5 Sonnet（奖励设计）、o4-mini（IMO 评分） | 附录 D.1 Table 3 |
| PerformanceTracker、持久记忆（洞见/因果假设/计划） | §5.2 末段代码片段说明；附录 E.3 |
| imp@50：初始 meta（DGM w/o SI）0.0(0.0–0.0)；初始 meta（DGM-H w/o SI）0.0(0.0–0.130)；DGM-custom 迁移 0.0(0.0–0.010)；DGM-H 迁移 0.630(0.540–0.630)，对初始 p<0.05 | §5.2；定义见附录 D.3 |
| 迁移的是 task+meta 整体代码；迁移 agent 按后代增长（深度折扣）选取 | §5.2；附录 D.4 |
| 200 代复利：0.640(0.550–0.720) 对 0.610(0.510–0.680)，p>0.05 | §5.3 |
| 起点为 0 的原因：输出格式不合规 | §5.1（论文评审）；§5.2（IMO 评分、迁移 hyperagent 起点 0.0） |
| 成本：100 代自改约 33M token；含评估约 88.6M token | 附录 D.2 |

## 自绘与重绘

- 中部 A/B 分屏流程：**示意**，本项目自绘，不是论文 Fig. 1。
- imp@50 柱状图：按 §5.2 正文数值**重绘**，不是论文 Fig. 3；须线只画 CI 上界（第 2、4 柱，DGM-H 画 0.540–0.630）。
- 未使用论文原图。

## 展示边界（来自 selection.md 第 5 条，均已上版）

等迭代不等于等总成本；跨域累积 0.640 对 0.610 不显著；迁移的是整套 task+meta 代码。另据核读补充：早期增益里有“修好输出格式”这一低门槛。
