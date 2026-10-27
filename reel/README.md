# 精选 Reel

2026-10-22，run [rsi-l1-20261022-03](../research/scoring/runs/rsi-l1-20261022-03/progress.md)：1597 篇 L1 → 978 篇 L2 全文核对 → confirmed P3 池 562 篇 → 终选 **15 篇**（宁缺毋滥）。2026-10-24，rolling run [rsi-rolling-20261023-01](../research/scoring/runs/rsi-rolling-20261023-01/progress.md) 增量 5 篇 confirmed P3 → 第三期终选 **3 篇**（1 篇退回修订）；随后同一 rolling run 补跑班后候选池 6 篇 confirmed P3 → 第四期终选 **3 篇**（无退回）；第五期候选池 5 篇 confirmed P3 → 终选 **3 篇**（1 篇退回修订）。共 **24 篇**。每张画报经 Opus 5.5 原文核对（含附录补读）、逐数溯源（SOURCE.md）与实际视觉 QA（QA.md）；24 种版式互不重复。选题全程：[selection 1](../research/scoring/runs/rsi-l1-20261022-03/selection.md) · [selection 2](../research/scoring/runs/rsi-l1-20261022-03/selection-002.md) · [selection 3](../research/scoring/runs/rsi-rolling-20261023-01/selection-003.md) · [selection 4](../research/scoring/runs/rsi-rolling-20261023-01/selection-004.md) · [selection 5](../research/scoring/runs/rsi-rolling-20261023-01/selection-005.md)。按新到旧排列：

| 论文 | 问题族 | 一句话 |
|---|---|---|
| [2610.35579](2610.35579/) Infinity Machine | F1/F2 | 唯一自改候选因成本被拒、发现全出自初始 genome；评分器被钻 4 次；写反方向的评分穿过全部机器检查 |
| [2610.34938](2610.34938/) /retro 复盘迁移 | F1/F3 | 复盘改动逐条迁移：只有覆盖到实际遇到实例的 2 条消除目标动作，4 条未减少，不完整清单还添活 |
| [2610.34238](2610.34238/) Δτ-Bench | F3/F5 | 六版本演化工具生态：成功率掩盖错过的更短路径；按依赖增量维护技能胜过冻结与全量重建 |
| [2610.32322](2610.32322/) Beyond Gain 技能退休 | F2/F1 | 零增益既可能是已会也可能是都不会；增益规则删掉 57.5% 的未覆盖技能，按不带技能的水平读 |
| [2610.31401](2610.31401/) HERD | F3/F5 | harness 挑出要学的、双锚约束下蒸进权重：习得持平，遗忘与通用能力损失最小（部署只用权重） |
| [2610.31326](2610.31326/) AgenticEvolve | F1/F4 | 只删“提交前自己做实验”的工具作对照：三模型两任务上程序更好，费用高 2.6–13 倍 |
| [2610.30499](2610.30499/) ARC-AGI-3 自改 harness | F1/F3 | 27 条谱系：开发 +8.42，留出只 +2.80（区间含 0）——会搭不等于会改好 |
| [2610.29005](2610.29005/) VeriEvolve | F2/F4 | 合成评估器在自出考卷上 141/141，到搜索状态上 113/122；外部校准下可修补 |
| [2610.28798](2610.28798/) Feedback Contract | F2/F4 | 每轮给精确验证分，无信号任务也报出增益；按配对标准误发放分数 |
| [2610.07792](2610.07792/) ServeLearnBench | F4 | 隐藏且变化的策略下，从结果反馈推断知识的缺口与副作用 |
| [2610.05437](2610.05437/) TeleTune | F4 | 不可重放的离线遥测里，用动作预测准确率门控技能编辑 |
| [2610.02920](2610.02920/) HASTE | F4 | 演化安全 harness 本身（Zombie 的防御侧） |
| [2605.25815](2605.25815/) Behind EvoMap | F2/F5 | 自报元数据担保不了共享技能质量（实测审计） |
| [2605.06614](2605.06614/) SkillOS | F1 | 冻结执行器，只训练写技能库的 curator（延迟信用） |
| [2604.15719](2604.15719/) Pre-Resolution Signals | F4/F2 | 结果揭晓前无标签，靠重访同一问题修订 harness |
| [2604.11811](2604.11811/) M★ | F3 | 每个任务值得自己的记忆 harness——跨任务迁移矩阵 |
| [2604.04247](2604.04247/) Combee | F0/F5 | 并行学提示的质量崩塌边界；收益主要是速度 |
| [2603.28052](2603.28052/) Meta-Harness | F1/F5 | harness 搜索里提议者能读原始轨迹才是关键 |
| [2603.19461](2603.19461/) Hyperagents | F3/F1 | 可编辑 meta agent 对比固定 meta agent |
| [2603.03329](2603.03329/) AutoHarness | F0 | 只合成动作合法性过滤器，新种子合法率验收 |
| [2602.15654](2602.15654/) Zombie Agents | F4/F2 | 一次网页注入写入记忆后跨会话持续控制代理 |
| [2602.10233](2602.10233/) ImprovEvolve | F0 | 种群搜索＋盆地跳跃的 LLM 进化优化 |
| [2602.05832](2602.05832/) UI-Mem | F2/F3 | 强记忆指导让 GRPO 组内奖励趋同、学习信号消失 |
| [2601.22436](2601.22436/) Are Not Always Faithful Self-Evolvers | F1 | 自演化代理的收益基本不依赖压缩经验——七类内容干预的证伪 |

每篇目录：`poster.png / poster.pdf / poster.html（可编辑源）/ SOURCE.md / QA.md`。

[选题规则](../research/scoring/SELECTION.md) · [制作提示词](../research/scoring/OPUS_REEL_PROMPT.md) · [撤下说明](../docs/RESET_2026-10-22.md)
