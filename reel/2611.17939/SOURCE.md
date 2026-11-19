# SOURCE.md — 2611.17939（榜单分数是一次抽奖）

数据到原文的逐项映射。全部数值取自 arXiv:2611.17939v1 本地缓存全文（research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.17939.txt）。本海报为本项目重绘，非作者出品。

## ① 漂移柱带（7 根柱）

| 海报数值 | 原文位置 |
| --- | --- |
| 119 / 116 / 120 / 123 / 105 / 116 / 109（149 项 rubric cells） | §3 Table 2，七次同配置 dev 运行逐跑 cells |
| 跨度 18 格＝12 个百分点 pass rate | §3 正文："Cells passed span 105 to 123 of 149: 18 criteria, twelve points of pass rate, with nothing changed" |
| 相邻两跑间 15–28 格翻转 | §3 twin 表："19 / 21 / 28 / 15 / 19" flips，正文 "Between two consecutive runs 15 to 28 criteria flip" |
| 账单波动 ±17% | §3："The bill moves by up to 17% (ratio of run totals 0.830 to 1.038)" |
| 单题成本 0.16×–5.43× | §3："a single question cost anywhere from 0.16× to 5.43×" |
| 默认晋级门槛落在漂移带内 | §3："a change is promoted if it cuts cost by at least 5% … or raises the pass rate by at least one point … §6.2 a +7-cell change is promoted, and +7 is the distance between baselines 6 and 7" |

## ② 故障归因横条

| 海报数值 | 原文位置 |
| --- | --- |
| policy 13 / tool 3 / data 0 / model 4（共 20 条失败轨迹） | §4.2 Table 4 总计行（reading A） |
| "谁拥有修复手段"分类、规则先行冻结 | §4.1 Table 3 投影表 + Rule M；"frozen before any analyzer run on the test trajectories" |
| 四盲读者 75/80 与分析器同故障；66/80 标 model、policy 仅 1 次 | §5.1 Table 6 与正文："blind readers said model in 66 of 80 labels and policy once" |

## ③ 双判决卡

| 海报数值 | 原文位置 |
| --- | --- |
| 成本臂 0.34×，CI [0.216, 0.580]，噪声带 [0.83, 1/0.83]，pass rate −3.7 pts CI [−8.9, +1.1] | §6.3 Table 9 cost winner 行 |
| 准确率臂 +1.5 pts，CI [−5.3, +7.2] 跨零 | §6.3 Table 9 accuracy winner 行；正文 "sign-flip test at p=0.74" |
| dev +14 pts（130/149 超全部基线）、VSEC 三副本全掉 | §6.2 Table 8 round 2；§6.3 正文 "VSEC lost cells in all three replicas" |
| 工具描述 0.996× 被拒 / system prompt 0.844× 晋级 | §6.1 Table 7 round 2 vs round 3；正文 "The same instruction saved nothing as a tool description and 16% of the bill as a system-prompt line" |

## 逐题账单条

| 海报数值 | 原文位置 |
| --- | --- |
| PFE 披露 $22.34→$3.95；CZR $13.01→$2.35；ASPI $9.26→$5.33；MAR/WH $6.63→$1.60；CRM $4.70→$5.30 | §6.3 Table 10（3 副本合计美元） |
| 嵌套检索 $62.91 / $71.17 | §6.3 正文："$62.91 of the baseline's $71.17 was nested-LLM spend, against $15.11 of the winner's $24.27" |
| CZR/ASPI 任何配置都过不了 | §6.3："Two questions, CZR and ASPI, are unsolved by every configuration" |
| CRM 129 轮、114 次单步计算器调用 | §6.3："the agent spends 129 turns and 114 single-operation calculator calls on it" |

## 警示条（未证明清单）

| 海报表述 | 原文位置 |
| --- | --- |
| 单 Judge、单 Agent、9 题 20 轨迹，解剖而非总体估计 | §7.1："Nine test questions and twenty failed trajectories make an anatomy, not an estimate of a population share" |
| 无"无诊断"对照臂 | §7.1："There is no control arm … we validate the loop, not the causal efficacy of its diagnosis" |
| accuracy winner 对照跨时间窗 | §7.1："the accuracy winner was compared against the baseline replicas of the first opening, reused, so the pair does not share a time window" |
| "没有漂移测量和预写规则会报告 +14 pts——真实而无价值" | §6.4 原文："Without the drift measurement and the written rule we would have reported '+14 points on dev', and it would have been true and worthless" |
