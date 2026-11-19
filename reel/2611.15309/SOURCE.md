# SOURCE.md — 2611.15309（自洽权分给谁）

数据到原文的逐项映射。全部数值取自 arXiv:2611.15309v1 本地缓存全文（research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.15309.txt）。本海报为本项目重绘，非作者出品。

## 三平面栏

| 海报表述 | 原文位置 |
| --- | --- |
| 三决策 govern / propose / judge；两系（controller-centric vs agent-centric）各抓一头 | §1 与 Fig.1；"These failures share one root: autonomy is misallocated across the three decisions" |
| agent 系教训直进共享记忆、无人把关 → 过早收窄 | §1："One agent's lesson from a single attempt goes straight into the memory every other agent reads. No independent owner checks whether it holds … so the search narrows before the evidence justifies it" |
| −64% token vs 四 agent CORAL（同 wall-clock，Math 七题领先六题） | §1 与 §6.2："at about 64% lower token cost than four-agent CORAL"；"Leading six of seven Math tasks" |
| 680K 行 OR-Tools CP-SAT、solver 质量 +16.9% | §1 与 §6：680K-line industrial repository, "improves end-to-end solver quality by up to 16.9%" |
| Protected Judgment 只返回 validity / fitness / metrics；运行时钩子拦截评估器读取 | §4.4 与附录 A.7（Permission hooks decide individual tool calls） |
| 治理移出 agent 轨迹、算力集中构造候选 | §6.2："Structured Governance moves history interpretation and search routing out of the expensive agent trajectory" |

## 裁判可见性表（Table 3 全六行）

| 海报数值 | 原文位置 |
| --- | --- |
| CORAL-1 暴露 0.793/0.750/0.705/−0.089；保护 0.664/0.646/0.639/−0.025 | §6.3 Table 3 |
| CORAL-4 暴露 0.789/0.756/0.711/−0.078；保护 0.708/0.716/0.731/+0.023 | §6.3 Table 3 |
| EvoTrias 暴露 0.803/0.745/0.721/−0.083；保护 0.733/0.732/0.741/+0.007 | §6.3 Table 3 |
| 3 独立 run / cell；终程序在 Original / IID / OOD 各评一次 | 附录 C.10.1："Each of the six cells is three independent runs"；"Each run's final program is then scored once on the original evaluator and once on each held-out suite" |
| IID / OOD 套构造（同族新参数化 / 加宽分布+新族） | 附录 C.10.2 Table 16 |
| 暴露平均抬 Original +0.093、OOD 只 +0.009 | §6.3 正文："exposure raises the Original score by 0.093 on average, but this advantage contracts to 0.009 OOD" |
| Circle Packing 暴露效应 <1% | §6.3 正文与 C.10.2："exposure shifts the score by less than 1%" |

## 两个代码案例

| 海报表述 | 原文位置 |
| --- | --- |
| 暴露版：按五固定信号族路由、强制 last-sample lag=0、注释自述"调过 grader 固定种子"；Original 0.809 → OOD 0.688 | 附录 C.10.3 代码案例 |
| 保护版：Haar-MAD 噪声估计 + 自相关 Matérn 长度尺度；Original 0.719 → OOD 0.730 | 附录 C.10.3 代码案例 |

## 限制条

| 海报表述 | 原文位置 |
| --- | --- |
| 无独立渗透测试 | L2 记录限制；原文未提供对钩子层的红队攻击实验 |
| 同 wall-clock 而非同 token 口径 | §6.2 budget alignment 描述（matched wall-clock budget） |
| SOTA 对照名单（OpenEvolve / EvoX / AdaEvolve / CORAL-1/4） | §5 基线配置 |
| 三平面消融（去 judge / 去 governance 各自掉分） | 附录（judge ablation 即 exposed 设置；§6.3 引用 "an ablation of the third plane"） |
