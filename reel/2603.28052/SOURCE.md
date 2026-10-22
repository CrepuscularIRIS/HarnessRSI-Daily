# SOURCE — 2603.28052

- 论文：Meta-Harness: End-to-End Optimization of Model Harnesses（Lee, Nair, Zhang, Lee, Khattab, Finn；Stanford / KRAFTON / MIT）
- 版本：arXiv:2603.28052**v1**（2026-03-30）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2603.28052.txt`（正文 §1–5 与附录 A–E 已通读；Fig.1/3/4/7 是图片，不在文本中）
- 初筛记录：L1 `batches/b038.jsonl` → L2 `batches/l2b06.jsonl`（P3 / confirmed / high / to_l3）；L3 `l3-final.tsv` #2、`selection.md` 阶段二
- run：rsi-l1-20261022-03

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 规格框 | 提议者 Claude Code + Opus-4.6；基础模型冻结；约 60 个候选 / 20 轮；只按 search set 选择；最后对 Pareto 前沿测一次测试集；单文件 Python | §3 “Practical implementation”“Meta-Harness search loop” |
| 问题 | 决策后果延迟出现；压缩反馈移除定位信息；“可扩展性取舍，不是长程依赖无用的证据” | §1 |
| 压缩比条形 | OPRO 0.002 · TextGrad 0.015 · AlphaEvolve 0.022 · GEPA 0.008 · Feedback Descent 0.012 · TTT-Discover 0.026 · Meta-Harness 10.0 MTok/iter | Table 1 |
| 机制图 | 文件系统存源码 / 分数 / 轨迹；grep、cat；不设父代选择规则；接口校验后评估；结束后测试 | §3、Fig.2、Algorithm 1、附录 D |
| 机制图 | 单次评估最多约 1000 万 token 诊断信息 | §1 |
| 机制图 | 每轮读文件中位 82（69–99）；源码 41%、轨迹 40%、分数/摘要 6%、其他 13% | 附录 A.1 Table 8 |
| 通道对照 | 只给分数 34.6 / 41.3 / 26；+摘要 34.9 / 38.7 / 23；完整接口 50.0 / 56.7 / 39；列（分数、源码、摘要、轨迹）的勾选 | §4.1 Table 3 |
| 通道对照注 | “中位候选高于两种消融的最佳”；摘要可能有害 | §4.1 Table 3 正文 |
| 其他优化器 | GEPA 32.6/40.2 · Best-of-N 34.0/44.2 · OpenEvolve 39.1/43.3 · TTT-Discover 34.1/45.6 · Meta-Harness 50.0/56.7（search set） | Table 4 |
| 同预算 | 同一提议者配置；相同的候选评估预算 | §4.1 “Comparison vs text optimizers” |
| 留出：分类 | 48.6；ACE 40.9（+7.7）；MCE 40.0；few-shot(all) 40.8；上下文 11.4K vs 50.8K | Table 2 |
| 留出：OOD | 9 个未见数据集平均 73.1 vs ACE 70.2 | Table 5 |
| 留出：数学 | 250 题 search set、40 轮、109 个候选；用 GPT-OSS-20B 选择；200 道 IMO 级题；Table 6 各列数值 | §4.2、Table 6、附录 C.3 |
| 留出：TB2 | 同一套 89 题搜索和评估；Opus 76.4 vs KIRA 74.7；Haiku 37.6 vs Goose 35.5；他方数字来自榜单；相对 KIRA 在 7/89 题上有增益 | §4.3、Table 7、附录 B.3 |
| 案例 | 基线 64.4%；第 1–2 轮 58.9 / 57.8；第 3 轮 63.3；第 4–6 轮退步；第 7 轮环境快照为最佳 | 附录 A.2 |
| 限制 4 | §4.2 写 250 题 search set；附录 D 写“88 problems for math retrieval” | §4.2 vs 附录 D |
| 限制 2 | 只用一个强提议者，换提议者留待未来工作 | §5 |

## 本项目计算

“其余 4 个未见模型均值”（GPT-5.4-nano、GPT-5.4-mini、Gemini-3.1-Flash-Lite、Gemini-3-Flash）由 Table 6 逐项算术平均：无检索 30.75→30.8；BM25 34.70；Dense k=5 35.925→35.9；Meta-Harness 35.825→35.8。

## 示意与重绘

- 压缩比条形：log10 刻度、起点 0.001，**示意比例**。
- 搜索回路图、通道管道：本项目**示意**；管道粗细不代表 token 数。
- 其余数字均直接取自原文表格。没有运行任何实验。

## 展示边界与核对说明

- 接口消融在 search set 上，每个条件一次搜索，只有一个提议者；TerminalBench 不是留出结果（与 selection.md 一致）。
- **展示口径收窄**：selection.md / l3-final 写“5 个未见模型 +4.7”。原文 §4.2 说的是“four models not seen during search”另加用于选择的 GPT-OSS-20B；摘要中的“five held-out models”指的是题目留出。画报写成“未见题目 · 模型部分未见”，并补充：相对 BM25 只 +1.3，在 4 个未见模型上与 Dense k=5 持平。这只是缩窄展示口径，不改变档位，不需要 correction。
