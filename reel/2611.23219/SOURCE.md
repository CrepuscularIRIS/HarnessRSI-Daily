# 2611.23219 · Do LLM Agents Still Need to Be Told How to Self-Improve? — 数字与主张对照表

- 论文：Do LLM Agents Still Need to Be Told How to Self-Improve?（arXiv 2611.23219v1，2026-11-17）
- 全文材料：research/fulltext/2611.23219.full.txt（未截断全文，65k 字符：§1–§8 与附录 A–F，Table 1–4 按行渲染）
- 初筛记录：batches/inc-l2-31#2611.23219（P3 / confirmed / to_l3，F1/F2，judgment；supersedes inc-l2-29）
- 海报：reel/2611.23219/poster.html（1700×1500 横版，"只给原语 → 自己组出的学习程序 → 证据"三联画）

## 海报逐项对照

| 海报位置 | 内容 | 来源 |
|---|---|---|
| 头部·6 模型 | Claude Opus-4.6/5、GPT 5.6-Sol/6-Astra、GLM 4.7/5.3 | §3.4 |
| 头部·20 / 150 | 更新预算 / gameplay 预算；低推理强度；每回合 20k token；3 个独立 teacher 会话 | §3.4、Table 3 |
| 头部·20 回合 | PuzzleScript、20 回合、25k token/局的规范设定；PS-t20 共享此约束 | §3.4、§5.1 |
| 头部·4 基准 | PS-t20（20 局/20 回合/25k/4 rollouts）、PS-t30（20/30/31,250/4）、ARC-AGI-3 L1（17/30/31,250/4）、MazeBench（16/100/75k/2） | Table 2 |
| 头部·98.8% | 10 个基线 100% 胜率关卡上，学到的产物后仍 98.8±0.0 | App D.4 Table 4 |
| ①·给什么 | Read/Write（player_folder 放 prompt 与技能文本）、Bash、Gameplay（返回分数、终局原因、预算状态、转录路径）；目标＝改进 player 在未见游戏上的表现、产物对未见任务/机制有用 | §3.2 Tools / Context、App C.1 |
| ①·不给什么 | 不规定何时用工具、如何组织产物；无真实任务、无验证分数；无人工游戏；Gameplay 拒绝不编译或 BFS 判定胜利态不可达（BFS 超时则接受） | §3.2、§3 引言、App C.1 |
| ①·harness 关闭项 | 默认系统提示、自动记忆、联网、子代理等 | App C.1 |
| ①·怎么量 | J(c_final) − J(c_0)：有无优化上下文在留出测试集上的差；新 player 会话、固定回合/token 预算；teacher 从未见测试游戏 | §3.3、§5 |
| ②·A/B 测试 | 同一局自生成游戏，有/无 teacher 文本产物各跑一遍 | §4.2 Fig 5 |
| ②·难度校准生成 | 随机关卡生成器 + BFS 求解器过滤；更少"解长 <5 且 100% teacher 观测胜率"的琐碎游戏 | §4.2 Fig 5/8 |
| ②·对抗测试 | 设计考验笔记的对抗游戏；跨早期游戏跑回归检查 | §4.2 Fig 8 |
| ②·小步更新 | Opus-5 与 GLM 5.3 偏好更小的上下文更新；GPT 6-Astra 与 GLM 5.3 更多"至少在一局上提升观测胜率"的批量更新 | §4.2 Fig 5 |
| ②·重放在哪 | 100% 胜率游戏很少重放；Opus-5 / GLM 5.3 多数重放集中在 20–60% 观测胜率；形似非对称自博弈 / UED 的 learnability 目标 | §4.2 Fig 7 |
| ③·代际差 | PS-t20 上 Opus-5 +20%、GPT 6-Astra +10%、GLM 5.3 +6%；老一代（Opus-4.6、GPT 5.6-Sol、GLM 4.7）很少或无改进 | §4.1 Fig 4 |
| ③·与 GEPA 同预算 | Opus-5 自组织学习与 GEPA（20 个真实分布内游戏爬山）在匹配 rollout 预算下相当；GEPA 10 训练 + 10 验证关卡、与测试集无共同基础游戏、同 player/reflection 模型、150 局预算前停 | Fig 3、App D.1 |
| ③·跨模型双向 | Opus 5 player：None 25.4±3.6 → GPT-6 Astra 产物 47.5±4.5；GPT-6 Astra player：None 67.1±3.8 → Opus 5 产物 72.1±4.0（PS-t20 胜率 %，3 seeds） | §5.3 Table 1 |
| ③·迁移 | Gameplay (PS-t20) 优化的上下文：PS-t20 +20%、PS-t30 +9%、ARC-AGI-L1 +21%、MazeBench SPL +0.15 | §5.1 Fig 9 |
| ③·无 Gameplay 工具 | Read-Write 在除 MazeBench 外所有基准上恢复的 Gameplay 增益 <50%；Read-Write-Bash 居中、未恢复全部 | §5.1 Fig 9 |
| ③·Python 游戏 | Python gameplay 在 3/4 情形恢复 PuzzleScript gameplay 几乎全部增益 | §5.1 Fig 10 |
| 读法与边界 1 | §5 迁移/信息/跨模型分析用 Opus-5；其他模型 +10% / +6% | §5、§4.1 |
| 读法与边界 2 | 测试集按 Claude Opus-5 8/8 过滤饱和关卡（PS-t20/t30、ARC-AGI-3 L1 同法），过滤后重跑基线 | App B |
| 读法与边界 3 | PS-t20 与自学习设定共享引擎与 20 回合约束 | §3.4、App B |
| 读法与边界 4 | 施加 t20 回合/token 预算 → PS-t20 升而 PS-t30 迁移降；最高细节上下文 6,551 token 使 PS-Narrow 升而 ARC-AGI-3 平台/微降 | §5.2 Fig 11、App C.2/C.3 |
| 读法与边界 5 | SRL 13 子过程对齐（GPT 6-Astra 判，0–3 分）是相关非因果；20 次更新后平台，加预算先升后平台 | §4.2、Limitations、App D.3 |
| 读法与边界 6 | 游戏域先验强（课程设计/可学任务生成文献可能已被摄入） | Limitations |

## 海报中的示意元素
- "重放在哪"的倒 U 曲线为**示意**（海报已标注），形状依 Fig 7 文字描述绘制，不对应原图像素；20–60% 区间与"100% 胜率很少重放"为原文数值。
- 代际差与迁移条按数值线性缩放（+20% = 满条；MazeBench SPL +0.15 按同刻度极短）。
- ①②③ 三栏为编辑组织，不对应论文插图。

## 未上海报但核对过的相关数
- §5.1：Gameplay (t-30) 跨基准最好，甚至在 PS-t20 上超过 Gameplay (PS-t20)；一个 Read-Write-Bash 会话在无 Gameplay 工具、提示未提游戏的情况下自己写并跑游戏模拟器测试笔记（App E.2）。
- App C.2：无约束 Gameplay 设定按算力配平（3000 回合 / 3.75M token = 150×20 与 150×25k）。
- §5.2：Zimmerman 框架原 17 子过程，4 个在试点中被判 consistently unassessable 而剔除（App C.6）。
