# SOURCE — 2610.31326

- 论文：AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments（Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, Jun Zhang, Yun-Song Piao；中国科学院大学）
- 版本：arXiv:2610.31326**v1**（2026-10-22）
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/2610.31326.txt`（HTML 转文本，sha256 `5db08485…98ff4`）。正文 §I–§VIII 与补充材料 S1–S4 全部通读（S3-B 逐方程表按需核对）。
- 初筛记录：L1 `batches/inc-l1-02.jsonl` → L2 `batches/inc-l2-03.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-004.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 结论（画报展示口径）

在岛屿 + MAP-Elites 的 LLM 程序演化中，只删除“代理在正式评测之间自己写脚本做实验”的工具（No-analysis），其余机制不变：OBP 与 DJSS 两个启发式任务、三个 Flash 档模型、各 5 次独立运行，AgenticEvolve 最终程序在隐藏集上均值都最好（12 个差值区间都不含 0，9 个 Mann–Whitney 显著），在未见实例上同样领先；但每次运行费用是 No-analysis 的 2.6–13 倍，同费用优势只在 OBP 上对三模型都成立。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 标题 / 副标题 | 持续代理在正式评测之间做实验；No-analysis 对照 | Abstract（L78–）；§III-D（L375–397） |
| In [1] | 单次请求生成、无执行工具；评测耗预算且实例隐藏；研究问题 | §I（L86–）；§II-A |
| In [2] 代理框 | 持续对话；上下文 70% 时交接摘要 | §III-B（L325–）；S1-A、S1-D |
| In [2] analysis 框 | analysis.py 可 import program；临时目录只含两文件与任务数据；看不到评估器和隐藏输入；每次提交最多 10 次 | §III-B；§IV-B（L452–）；S1-D 系统提示 |
| In [2] 正式评测框 | 每次提交耗 1 单位预算（失败也算）；只回指标或异常类型与位置 | §III-B；§III-D（L377–）；版本说明 S1-D |
| In [2] 档案 / 岛 | MAP-Elites 每维 10 格；3 岛环形迁移；代理自决是否读取；read_commit | §III-C（L359–）；§IV-B |
| In [2] 说明 | No-analysis 删除内容与保留内容；OpenEvolve 对齐设置 | §III-D；§IV-B；S1-B Table S1 |
| Out[2] 图 | OBP / DJSS 隐藏集均值 ± SD；Best Fit 6.55、FunSearch 6.10、R1 = 1 | Table II（L567–）；Table S2 |
| Out[2] p 值 | 前对 No-analysis、后对 OpenEvolve | Table II p 列；Table S3（L2240–） |
| Out[2] 注 | 12 个区间不含 0、9 个显著、例外三处；No-analysis 与 OpenEvolve 无显著差；最小精确 p 0.008 | §V-A（L543–）；§IV-C（L515–） |
| 未见实例表 | OR1 与 DJSS 新种子的三方法均值；FunSearch 5.30、Best Fit 5.81 | Table II Unseen 列；Table S2；§V-A |
| 费用表 | 每次运行估算费用 | Table II Cost 列 |
| 费用注 | 2.6–13 倍为本项目按 Table II 计算（1.08/0.42 至 1.72/0.13）；同费用比较的任务依赖 | §V-C（L917–） |
| In [3] 日志 | 10 次分析与结果；隐藏集 6.553% → 5.392%；注释与实际来源不一致 | §V-D（L948–）；Table S5（L2939–）及其后说明 |
| 按评测次数 | 5/6 情形 20 次内追上；7/17/3、19/26/8；91 次共同范围 | §V-B（L903–）；Table S4（L2828–） |
| 方程发现表 | 结构恢复 11/6/6/3/1；OOD 达标 12/8/8/3/1；费用 6.54/12.12/6.59/111.34 | Table III（L1091–）；Table IV（L1186–）；§VI-C（L1480–） |
| 方程发现注 | 训练数据可被分析；DeepSeek-V4.1-Flash；每题 1 次 | §VI-A（L1036–）；§VII（L1613） |
| 限制 1 | 同评测上限、总费用不同；等总费用下 No-analysis 是否追平未测 | §VII 末段 |
| 限制 2 | 无 OS 沙箱；尝试读取隐藏数据 / 重建实例，审计未见成功 | §VII（L1602 段）；S4-A（L6584–）、S4-B（L6600–） |
| 限制 3 | 启发式实验均在旧反馈口径；方程发现 AgenticEvolve 为 0.2.0、No-analysis 为 0.2.1 | §IV-C 末；S1-E；S4-B Table S10 |
| 限制 4 | 持续对话、迁移未单独消融；215 次跨岛读取后 169 次刷新岛内最好分 | §VII；S2-D Table S6 |
| 限制 5 | 两任务、12 方程、Flash 档、n=5；4/90 程序导入时调参（重评 < 10⁻³） | §VII；S2-A |
| 限制 6（本项目读法） | 留存的是任务程序；确认的是条件性判断 | 本项目阅读判断，与 L2 biggest_gap 一致 |

## 示意与重绘

- 机制图（代理、analysis 回路、档案网格、三岛环）为本项目示意；网格着色不对应任何真实档案。
- 两张均值 ± SD 图按 Table II 数值等比绘制；单次运行的散点原文只在 Fig. 2，未逐点抄录，因此没有画个体点。
- 本项目没有运行实验，也没有复现结果。

## 核对结论

与 L2 记录一致，无 correction。补充一处 L2 未写的边界：方程发现部分 AgenticEvolve 与 No-analysis 跑在不同框架版本（失败反馈口径不同），已写入限制 3；该部分为单次运行，画报只作为附带证据。
