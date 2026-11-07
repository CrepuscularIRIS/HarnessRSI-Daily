# SOURCE — 2611.07123 · 判卷模型示波器（PromptOps）

- 论文：PromptOps: Iterative Prompt Optimization for LLM-as-a-Judge Systems（Sven Kleinkop, Tamás Janusko 等；德累斯顿应用技术大学 HTW Dresden）
- 版本：arXiv:2611.07123**v1**（cs.AI，2026-11-04）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.07123.txt`（arxiv.org/html/2611.07123v1，sha256 `bdfa672a…`，与本 run `materials/2611.07123.json` 的 pin 一致，complete: true）。正文 §1–§6 与附录 0.A（G-Eval 提示词）、0.B（Dispatcher / 参数 / 样本选择）、0.C、0.D、0.E（Split / Easy 流表 5）**全部通读**。图 2–8 为图片，只用正文对其的文字描述。
- 初筛记录：L1 `batches/inc-l1-14.jsonl` → L2 `batches/inc-l2-16.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-011.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 收窄：“漂移”只是参考分数构成变化（同一数据集重排），不是人类政策或 judge 模型变化；反馈是理想化即时 oracle；结论是同流固定对照下的条件性恢复与触发成本取舍，不是通用 judge 漂移解法、不是等费用胜出。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 标题 / 副标题 | judge drift 定义；恢复而非复原；优化器与时机不通用 | 摘要 L97–107；§1 L129–134；§4.3 L1002–1008 |
| 信息栏 | FairBotBench 600 段德英电商对话、三维度、三人均值 1–5；GPT-5.4-nano（low）/ Gemma 4 26B-A4B Q4；专家 GPT-5.4（high）；五种优化器 | §4.1 L747–811；§3.1 L475；作者 L39–61 |
| SCREEN 1 · 四框 | Controller / Dispatcher / Sample Selector / Optimizer | §1 L163–173；§3 L408–462 |
| SCREEN 1 · 时间轴 | 500 条；更新位置 20/50/95/163/265/417（式 (1)，p = 20）；第 214 条后突变；四个区间 | §4.1 L826–859；§4.3 L918–921；表 1 说明 L1079–1106。**时间轴为示意重绘** |
| SCREEN 1 · 红 / 绿条 | 265 次更新：训练 164–265、开发集 96–163 | 由 NewElements 定义（§4.1 L821；附录 0.B.3）与更新位置**本项目推算**，原文未单独写出 |
| SCREEN 1 · 注 | 理想化 oracle 反馈；只用已到达记录；静态基线为初始 G-Eval 提示词 | §3 L464–466；§4.1 L758–788 |
| SCREEN 2 · 两图 | GPT 6 配置 × 4 区间、Gemma 6 配置 × 4 区间的相对改进（%） | 表 1 L1077–1400（rel 列）。**折线为本项目按表值绘制** |
| SCREEN 2 · 文字 | 突变后 12 个全部下降、个别运行低于静态；最终 12 个优于静态、多数低于突变前；Gemma Rubric(S)、TPE(L) 例外 | §4.3 L1002–1008（图 5，三种流合并） |
| SCREEN 2 · 注 | 绝对 MAE 不可跨流比较；Split 流 GPT Rubric(M) 55.2 → −77.7 → −106.4 → 35.8 | §4.3 L981–982；附录 0.E 表 5 L2527–2560 |
| 触发时机 · 表 | 表 2 全部 10 个值；τ = 0.4 / 0.6、w = 20 / 50 | §4.4 L1487–1600 |
| 触发时机 · 文字 | 7/8 持平或更好；High–Small 最好但最频繁；Low–Big 差 0.03（5.7%）；只 GPT + Low–First + 两配置 | §4.4 L1492–1542；附录 0.C L2479–2503 |
| 触发时机 · 注 | 表 2 定期 GEPA(S) 0.59 vs 表 1 Low–First GPT GEPA(S) 总体 0.55 | 表 2 L1544–1597；表 1 L1077 起 GEPA(S) 行。**内部不一致为本项目核对发现** |
| 优化器 | 23 配置 × 2 后端 × 3 次；只有 Rubric(S)/(M) 两边帕累托；GPT ≈ 0.48；Gemma SIMBA(M) ≈ 1870 万 token、0.5；SIMBA(L) ≈ 2630 万 token；Rubric 专化非因果 | §4.2 L864–910；§5 L1629–1635 |
| 量程之外 | 理想反馈；构成重排；一个基准 / 500 条 / 3 条流 / 两后端；无长期回归金标 | §3 L464–466；§5 L1650；§6；L2 子卡检查 |
| 改变的判断 | judge 不是部署即忘的组件；触发是一等设计决定 | §5–§6 L1613–1665。**“本项目读法”为本项目阅读判断** |

L2 facts（500 条、三条流、两后端；214 位于 163 / 265 之间；12 组最终优于静态；HighSmall GEPA / Rubric .49 / .47 vs 定期 .59 / .53；LowBig Rubric .56）与原文一致；L2 未提 0.59 / 0.55 表间差异，已在 selection-011 记为备注。
