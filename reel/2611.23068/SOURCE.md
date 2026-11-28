# 2611.23068 · The Resolution Hypothesis — 数字与主张对照表

- 论文：The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements（arXiv 2611.23068v1，2026-11-17）
- 全文材料：research/fulltext/2611.23068.txt（节选缓存，24.5k 字符：摘要、§1、§3、§4、§5.1 开头、§6、§7、Limitations；**§5.2/§5.3 正文数值与 Table 6/9 不在缓存**）
- 初筛记录：batches/inc-l2-29#2611.23068（P3 / confirmed / to_l3，F2/F1，judgment）
- 海报：reel/2611.23068/poster.html（1680×1600，"分辨率标尺 + 三栏"版式）

## 海报逐项对照

| 海报位置 | 内容 | 来源 |
|---|---|---|
| 头部速览·规模 | 7 方法 × 6 模型 × 4 基准（另 9 基准审增益） | §3.2 Experiments |
| 头部速览·规模 | 1,030 次独立演化 / 150 配置 / >210 万测试轨迹 | §4.1 第 1 段 |
| 头部速览·规模 | >10M LLM 调用、400K CPU core hours | §3.2 末段 |
| 头部速览·规模 | 每配置演化 8 次（文本产物法在 GPT-5.4 nano 上 16 次）× 每产物评 16 次（Terminal-Bench 与 harness 法 8 次） | §4.1 第 1 段 |
| 头部速览·规模 | 九篇论文主表 171 个基准–模型结果；无一报告方差估计；仅 6 个平均超过一次演化 | §4.1 "Reported margins fall in the same range" |
| 标尺·σ_eval 1.0–3.7（SpreadsheetBench / OfficeQA / ALFWorld）、Terminal-Bench 4.5 | 评估噪声标准差 | §4.1 第 2 段 |
| 标尺·单次比较 SD 1.7–4.1 | 演化一次、评估一次的典型得分 SD（各基准配置中位；Table 6） | §4.1 第 2 段 |
| 标尺·σ_run 0–12.3 | run 间标准差 | §4.1 第 2 段 |
| 标尺·已发表领先中位 3.4（IQR 1.2–6.6） | 171 个结果的领先幅度 | §4.1 第 3 段 |
| 标尺·注 1 | >60% 配置对的全运行均值差距 < 1 个单次比较 SD；逐方法 53–79%（App D.1） | §4.1 第 2 段 |
| 标尺·注 2 | 单次运行挑出 4 个文本产物法中真正最佳：51–73%（SSB/OA/ALF）、33%（TB）；随机 25%（App D.2） | §1、§4.1 末段 |
| 方法级·80% 功效运行数 | 3.4pp 边距下 SpreadsheetBench 5 / OfficeQA 10 / ALFWorld 19 / Terminal-Bench 23；下四分位边距 TB 181（式 2，Fig 2b） | §4.1 "Identifying such margins takes many runs" |
| 方法级·方法名单 | GEPA / SkillOpt-Lite / Trace2Skill / ReasoningBank；HarnessLens / Meta-Harness / AHE | §3.2 |
| 增益审计·步骤 1 | 12 基准 × 3 模型；27 个报告增益 >3pp 的模型–基准对；向未演化基线只追加一句最关键规则 | §4.2 |
| 增益审计·步骤 2 | 规则多为评估捷径（只认一种答案格式的评分器 / 方法自带偏离官方评估的基准版本，Table 9） | §4.2 |
| 增益审计·17.6 → 0.8 | 修复评估后同一产物中位增益；修复后重跑文本产物法增益不回来（App E.3） | §4.2 末段 |
| 候选级·P1 | Proposal Pool：10 个 TB 训练任务生成技能 → 10 个不相交测试任务 × 16 rollouts/对（16,000 次）；Quality@K 高于等质量零曲线；单个共享技能跨度 >15pp | §5.1 |
| 候选级·P2 | Selection Pool：TB + DeepSWE 轨迹、11 个 TB 任务；选择器只见 1 次 rollout（原生 SkillOpt-Lite/GEPA 2 次）；选出更优者 ≈ 掷硬币（执行分与 LLM 判断皆然） | §5.2 开头、摘要、§1 |
| 候选级·P3 | 每轮接受"恰好分高"候选，分数升而产物不变好；误差逐轮累积成独立运行间差异 | §1、§7 |
| 候选级·方向 | 更细粒度过程检查（未掩码诊断率噪声更低，Table 13）；提议者 Quality@K / 选择者选择质量曲线分评；发表 σ_eval 与 σ_run | §6 |
| 读法与边界 | 仅冻结权重；候选级仅 Terminal-Bench v2.1（Proposal 10 / Selection 11 / 轨迹重评 2 方法 × 2 模型）；噪声在天花板处缩小、TB 三模型中位 3.5–4.0pp | Limitations |

## 海报中的示意元素
- "分辨率标尺"的条带位置按 pp 线性映射（0–12.3pp），σ_eval / 单次 SD / IQR / 中位均为原文数值；条带本身是编辑绘制，不对应论文插图。
- "需要运行数"条长按次数线性缩放，181 截断为满条显示。
- 增益审计三步为编辑转述的流程，数字全部来自 §4.2。

## 未上海报但核对过的相关数
- §5.1：2 小时预算与原始超时两种口径下 Quality@K 均高于零曲线；最强共享技能 artifact-063（具体数值在缓存中被剥离）。
- §4.1：识别单个固定产物的增益只受 σ_eval 限制，识别两方法差异受 σ_eval²+σ_run² 限制（§3.1）。

## 缓存限制（如实记录）
- §5.2 / §5.3 正文、Table 6（逐配置方差）、Table 9（捷径清单）、Fig 2–4 数值不在本地缓存；海报对 P2/P3 只用摘要/引言/结论中的定性表述，不引具体数值。
