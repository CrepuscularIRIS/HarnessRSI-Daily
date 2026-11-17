# ModHarness-RL — 海报来源

- 论文：**ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL**，Zelin He、Siyu Zhu、Jacob Helwig、Yujian Liu、Li An、Rohit Jain、Shiyu Chang、Alborz Geramifard。
- 固定版本：[2611.18533v1](https://arxiv.org/abs/2611.18533v1)；[原文 HTML](https://arxiv.org/html/2611.18533v1)。未据此宣称会议录用。
- 本地来源：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.18533.txt`；SHA256 `2d119df847d8a7d68243ae3ac49b20d0ed1ec817fa84d4dbd411338aecbe2228`。抓取版本记录在 rolling run 的 `materials/2611.18533.json`。
- 上游：`rsi-rolling-20261023-01/batches/inc-l1-20.jsonl`、`inc-l2-22.jsonl`；规范 `problem-core-v1.1`；[第16期选题](../../research/scoring/runs/rsi-rolling-20261023-01/selection-016.md)。
- 制作日期：2026-11-17；模型按会话环境报告为 **gpt-6-astra**（fable 槽位，未独立探测后端），不是提示词角色名 Opus 5.5。

## 逐项溯源

| 图中内容 | 原文位置与含义 |
|---|---|
| 类型化 State、`cₜ = flatten(compress(sₜ) ⊕ steer(sₜ))` | §3.1 式(2)，本地 L551–650。完整状态保留；压缩改变视图，steering在触发时追加指导。 |
| 压缩训练前拟合一次、RL期间固定 | §3.2.1，L651–700。双速带为项目编排示意，不是学习曲线或逐轮实测效果。 |
| 提案→历史回放→干预判断→同当前策略准入 | §3，L1001–1100；附录A.3 L2901–3000。新程序在训练留出门上的分数严格更高才安装；最终报告任务另留。 |
| 历史回放不等于反事实；Case2指导仍有帮助 | 附录C.5 图12，L4801–4900。不指导也改善，不等于指导已造成伤害。 |
| 基础 harness＋RL：.303/.333/.361/.403 | 表1，L1151–1700；顺序为受限4B、受限8B、充足4B、充足8B。 |
| 不生成：.302/.378/.365/.375；不判断：.356/.377/.376/.411 | 表3，L2151–2300。“不判断”仍经准入门，不是无验证全接受。 |
| 每10步重学压缩：.336/.279/.360/.398 | 表3及其说明。 |
| 完整固定压缩＋演化纠偏：.368/.412/.424/.460 | 表3，与表1完整方法一致。 |
| .279→.412 | 受限8B两种方案对照，不是同一轨迹随时间增长，也不是成功率。CodeSearch指标为定位F1。 |
| Qwen3 4B/8B；1024/8192历史tokens；200训练步；末次检查点 | 实验设置 L1701–1900、附录A.1与C.2。历史预算不是所有提示token的总上限。 |
| 288评价任务 | 附录A.1 L2701–2800：CodeSearch的100 Lite、100 Verified、88 Pro。 |
| 128/256准入题、反复使用 | 附录A.3；CodeSearch/ALFWorld 128，BIRD 128或256。身份与报告集分离不意味着反复自适应准入无过拟合。 |
| 误差条非独立训练种子 | 附录C L3151–3200，同一检查点重复评价：CodeSearch10次、其他3次。 |
| 完整系统主要CodeSearch；总预算未完全匹配 | 实验与局限 L2451–2500、附录C.2 L3201–3250。ALFWorld/BIRD主要单模块实验。 |
| “表示稳定、干预随故障变化” | 项目基于消融的阅读结论，不是通用最优更新定律。 |

## 完整阅读边界

全文与附录已阅读。程序运行无额外模型调用不意味着创建／判断免费；creator/judge使用GPT-5-mini。回放只估计历史故障频率，新指导效果还需实际策略运行。128/256题反复使用的门不提供全程无回归保证。HarnessForge对照为迁移演化循环、用GRPO替代SFT，不能称原方法严格复现。无独立训练种子重复，也未完全匹配创建器与优化总预算。

本图是项目重绘与表格重排，全部实验值为作者报告；没有运行论文代码或独立复现。两种模块的不同更新节奏是选题重点，不能把参数训练收益全部归给harness。

## 输出

`poster.html` 是可编辑源；携带 `assets/fonts/poster.woff2` 与 `LICENSE.txt`。`poster.png` 和单页 `poster.pdf` 为本地渲染；[QA](QA.md) 记录实际看图及一次重做。没有复制作者海报、机构徽标或虚构会议背书。
