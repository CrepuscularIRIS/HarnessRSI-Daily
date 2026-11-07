# L3 选题第十一期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席串行。
- 编号：本仓 Reel 第十一期。前十期共 39 篇（[selection.md](../rsi-l1-20261022-03/selection.md)、[selection-002.md](../rsi-l1-20261022-03/selection-002.md)、[selection-003.md](selection-003.md) 至 [selection-010.md](selection-010.md)）不再重复入选。
- 候选池：5 篇，均为本 run 最新 L2 记录（`inc-l2-16`）`P3 / confirmed / to_l3`：2611.07048、2611.07123、2611.07372、2611.07624、2611.08318。无 P2 编辑入池项（2611.08483 为 P2 / confirmed / park，L2 未写编辑理由，不入池）。本期上限 3 篇。
- 产出：本文件 + `reel/<pid>/` 三套成品。未改动任何 L1/L2 批次记录，未操作 git，未派子代理，未启动无头进程，未运行论文代码。

## selection_cutoff 说明

本期结果只代表这 5 篇候选在 3 篇上限与去重口径下的选择，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论；Reel 不把它呈现为权威评分。2611.08318 同时是 Embodied 仓候选。三仓不混榜，本仓只按 harness-RSI 领域卡口径独立核对，它在 Embodied 仓的去留与本文件无关。

## 钉定全文位置

5 篇钉定全文都在 `research/fulltext/review-runs/rsi-l1-20261022-03/materials/<pid>.txt`，pin 在本 run 的 `materials/<pid>.json`。5 篇 sha256 已逐一与 pin 核对，全部一致（07048 `f5850211…`、07123 `bdfa672a…`、07372 `daad7d2b…`、07624 `f46aa8d0…`、08318 `d96c507b…`）。5 篇都是 `complete: true`、v1、HTML 来源；corpus 中 `updated` 与 `published` 相同，没有更新版本。

**材料缺口**：2611.07372 的全部结果表（每个基准的基线 / EnvOpt / GEPA / Meta-Harness 对比、迁移、只换工具的消融、训练成本与耗时）在钉定文本中都缺失，正文里的表格引用渲染为空白。2026-11-07 从 arxiv.org/html/2611.07372v1 补读，确认同样没有可读表格（没有表号、单元格或替代文字），只有正文散文中的数字。需要 PDF 才能核对，见 correction C-011-1。2611.08318 附录 C 的逐任务改写表也在 HTML 中转换失败，但画报不使用这部分细节。

## 候选（5）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2611.08318 | Criteria Exposure（学任务还是学判卷） | P3 / confirmed | judgment | F2, F4 | diagnose_self_improvement; coevolve_the_evaluator | inc-l2-16 | 正文 §1–§6 + 附录 A、B 全部通读；附录 C 只读规则段（改写表 HTML 缺失） | **入选** |
| 2611.07624 | Beneath the Surface（演化收益冰山） | P3 / confirmed | judgment | F1, F5 | evidence_gated_retention; make_the_improver_editable; diagnose_self_improvement | inc-l2-16 | 正文 §1–§9 + 附录 A–D 通读；附录 E 浏览 | **入选** |
| 2611.07123 | PromptOps（判卷提示词持续维护） | P3 / confirmed | judgment | F2, F3 | coevolve_the_evaluator; attribute_and_patch_incumbent | inc-l2-16 | 正文 §1–§6 + 附录 0.A–0.E 全部通读 | **入选** |
| 2611.07372 | EnvOpt（优化代理环境） | P3 / confirmed | judgment | F1, F4 | index_experience_for_reuse; attribute_and_patch_incumbent | inc-l2-16 | 正文 §1–§5 + 附录 A（五个基准的研究代理指令）通读；结果表缺失 | **暂停，correction C-011-1 退回** |
| 2611.07048 | Darwinian / Lamarckian / Agent-Directed（理论） | P3 / confirmed | judgment | F2, F5 | coevolve_the_evaluator; population_search_executable_fitness | inc-l2-16 | §1、§2 前半、§8 全文、§9、附录 A；§3–§7 只读定理 / 命题陈述与 §7 表；证明未逐行核对 | 落选（同卡去重，理论结果近于由机制定义直接给出） |

## 原文核对（逐篇）

**本期 correction 1 项（C-011-1，07372）**；其余四篇的 L2 判断成立。下面是阅读备注，不改档位、不改记录；入选三篇的画报按备注收窄了展示口径。标“请 Sol 复核时顺带补注”的条目不是 correction。

1. **2611.08318**：表 1、表 2、§4.2.1–4.2.2、附录 A.1–A.4、B 已核实，与 L2 一致（51.6 / 27.8 → 45.0 / 47.2；差距缩小 25.9，区间 4.7–54.4；65/80/71；45/48/46）。本项目复算：
   - 表 1“全部 25 题”按 320 + 180 回合加权，得 24.56 / 47.78 / 62.04，与 24.6 / 47.8 / 62.0 一致。
   - 配对计数自洽：51.6% × 320 = 165、27.8% × 320 = 89，差 76，等于 93 − 17；45.0% / 47.2% 对应 144 / 151，差 −7，等于 47 − 54。
   - 差距缩小 23.8 − (−2.2) = 26.0，与 25.9 只差舍入。

   备注：
   - (a) §4.2.1 正文写“Figure 5 shows the lead of exposure disappear”，按内容应指图 4，属交叉引用笔误。
   - (b) w/ CE 一次给了判据源码、每回合分数和阶段三样东西，效应不能单归源码（L2 已注）。
   - (c) 跨任务迁移一行中，只看成败的库比读判据的库更好（80 vs 71，各 200 回合），但没有方差估计。
2. **2611.07624**：表 1、3、4、5、6、7、10、附录 D.1–D.4 已核实，与 L2 一致（16 冠军 loss 2–10、gain 1–15；15/16；6/8；15 → 6；160 / 152）。本项目复算：
   - 表 10 新增 − 丢失，按题数换算后与 ΔPass 全部一致（例：τ³ MiniSWE AHE 15 − 4 = 11 题，即 +11.3）。
   - 交互项 −6.4 / −6.5 / 0.0 / +2.1，与附录 D.3 的 −6.3 / −6.6 / 0.0 / +2.1 只差舍入。
   - 测试题可靠度 10/16 为正、迁移覆盖 7/8 降与 7/8 升，均已逐格计数。

   备注：
   - (a) 表 1 的冠军 vs 种子比较覆盖全部题（含训练题）。按表 3 拆分，部分谱系的覆盖增益全部来自训练 / 验证题：Codex AHE τ³ 为 +6.2 / 0 / 0，Codex HyperAgents τ³ 为 +8.2 / +1.0 / 0。画报已列出这一点。
   - (b) “15/16 组件优于泛泛提醒”有一部分来自提醒本身在 Codex 上拉低可靠度。16 个组件中有 4 个单独加到种子上反而低于种子（本项目计数），画报已注明。
   - (c) AGE 的四处修订来自同一批基准上的诊断，父代诊断的最佳父代标签又取自测试题，且只跑种子 0 一次。因此表 10 中 AGE 的优势不是干净的留出对比。L2 已写“AGE 整体胜出不认证每个解释”，这里补上信息来源这一层（请 Sol 复核时顺带补注）。
3. **2611.07123**：表 1、表 2、附录表 5、式 (1) 已核实，与 L2 一致（500 条、三条流、两个后端；214 位于 163 / 265 之间；12 组最终优于静态；HighSmall .49 / .47 vs 定期 .59 / .53；LowBig Rubric .56）。本项目复算：
   - 按式 (1) 推出的更新位置为 20 / 50 / 95 / 163 / 265 / 417，与原文一致。

   备注（请 Sol 复核时顺带补注）：
   - (a) 表 2 中定期 GEPA(S) 记 0.59，而表 1 同一 Low–First 流、同一 GPT 后端、同一配置的总体 MAE 是 0.55。按 0.55 计算，“GEPA 四个自适应设置全部优于定期”与“8 个中 7 个持平或更好”仍然成立，但两表数字不一致需要作者澄清。L2 fact 直接引用了 .59。
   - (b) 突变后第一次更新反而更差的情况不少：Split 流 GPT Rubric(M) 相对改进 −77.7 → −106.4，Low–First 流 GPT Rubric(S) −8.4 → −3.9（绝对 MAE 0.67 → 0.72）。按 NewElements 定义推算，265 那次更新的开发集是 96–163，全部在突变之前，这可能是原因之一。这是本项目的推算，原文未写，画报已标明。
4. **2611.07048**：§8 机制 8.1、定理 5、§8.2 与结论已核实，L2 的两条 fact 与原文一致。备注：
   - (a) 定理 5(ii) 中“更多变体不消除真实残差”在机制 8.1 下几乎由定义给出：搜索、评价器选择和学习三步都朝 p̃ 移动，收敛到 p̃ 是构造本身的结果。它的增量在于把速率与残差分开表达，以及独立自然选择的恢复率 2ℛ(p̃)。
   - (b) 评价器、学习效力和变体分布都固定，递归改进改进器不在已证范围内（作者自述）。
   - (c) 附录 A 的 AI 使用声明写“an evolutionary framework that selects the weights of multiple objectives … originated solely with the author”，与正文内容（没有多目标权重）和两位作者署名都不符，像是模板残留。不影响结论。
   - (d) 请 Sol 复核时顺带补注：Q2 只列了 FunSearch / AlphaEvolve / DGM 的奖励漏洞边界。同类“代理指标随搜索量上升、真实指标不随之改善”的实测工作（如 best-of-n 对奖励模型过度优化的缩放研究）条件不同（不是继承式演化），不构成 prior_solved，但可写进 q2 说明。

## 排列与取舍

1. 全部 P3、q3 全部为 judgment，不分先后。
2. **池内同卡去重**：07048、07123 都以 coevolve_the_evaluator 为主卡，问题都是“评价器不对 / 不随时间对时，自改进会怎样”。保留证据更直接的 07123（同一条流上与静态 judge 的受控对照、触发策略实测）。07048 是在标量模型中给出的定理，安全部分的核心结论近于由机制定义直接给出，又没有 harness 层数据，记为“同题去重”。08318 虽然也挂 coevolve_the_evaluator，但主问题是“学习器读不读判据”（diagnose_self_improvement），对象不同，保留。
3. **与既有 39 张去重**：
   - **08318 vs 2610.28798（Feedback Contract）、2611.05139（Meta²）、2610.41216（TinyAstral）**：Feedback Contract 讲每轮给精确验证分会在无信号任务上报出增益；Meta² 讲离线特权对照；TinyAstral 讲机器人 harness 换规划器后的迁移。08318 是唯一一篇用“同一批轨迹两份判据各判一次 + 交换所读判据”来测量判据暴露效应的工作。保留。
   - **07624 vs 2610.30499（ARC-AGI-3 开发 vs 留出）、2610.37201（BiPA 未改候选回放）、2610.38392（Masked Erosion 验收门）、2611.04952（Artifact-to-Capability）**：这几篇各自审一个环节。07624 在 4 方法 × 2 harness × 2 基准上同时给出覆盖换手、父代生产力（统一分支程序）、组件交互和冻结池门重放，独有“均分之下的新增 / 丢失”与“最高分父代 ≠ 最能生的父代”。保留，并在画报中避开 AGE 的方法排名。
   - **07123 vs 2610.29005（VeriEvolve）、2610.05437（TeleTune）、2610.28798**：VeriEvolve 讲合成评估器的外部校准，TeleTune 讲用离线遥测门控技能编辑。07123 是唯一一篇研究“judge 在流上随构成变化需要持续维护、何时触发”的工作。保留。
4. **入选三篇**主族为 F2 / F1 / F2，次族为 F4 / F5 / F3，主卡互不相同（diagnose_self_improvement / evidence_gated_retention / coevolve_the_evaluator）。08318 与 07123 主族同为 F2，但一个问“学习器该不该看判卷器”，一个问“判卷器本身怎样随时间维护”，对象与机制不同，两篇都保留。

## 入选（3）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2611.08318 | F2/F4 | diagnose_self_improvement | 学习器读了基准判据，学到的是任务还是判卷器？ | 冻结执行者，只切换学习器能否读判据；作者改写忠于指令的判据；同一批终测轨迹两份判据各判一次；交换所读判据 | 原判据 51.6 vs 27.8 → 忠于指令判据 45.0 vs 47.2（差距缩小 25.9，区间 4.7–54.4）；读改写判据的库 65.0 → 13.5；跨任务 80 vs 71 |
| 2 | 2611.07624 | F1/F5 | evidence_gated_retention | 演化均分上升时，水面下丢了什么？选父代、组合、准入是否用对了证据？ | 冠军与种子在全部题上各跑 8 遍；统一分支程序测父代生产力；组件 vs 提醒切断；冻结池门重放 | 16/16 冠军既有新增也有丢失（丢 2–10）；4 池最高分父代均非最能生；15/16 组件优于提醒；严门使留住最佳的池 15 → 6 |
| 3 | 2611.07123 | F2/F3 | coevolve_the_evaluator | 被评对象构成变化后，judge 提示词何时、怎样重调？ | Controller / Dispatcher / Sample Selector / Optimizer 分解；同一条流上的静态 judge 对照；定期 vs 滑窗触发 | 突变后改进全部下降；最终 12 个都优于静态，但多数低于突变前；7/8 自适应触发持平或优于定期（理想 oracle 反馈、只有构成变化） |

## Correction

**C-011-1 · 2611.07372（EnvOpt）· 退回 Sol 单篇修订（保留原记录，不直接修改）**

- 原判：`inc-l2-16` L2 记 q4_fit = fits、P3 / confirmed / to_l3，q3 = judgment（“改变 agent 优化单位与成本归因”）。子卡 H04 Step-by-Step §§1–2 记 holds，依据是“§4.4 对比原环境加新工具与完整重组，直接检查不只是新工具的收益”。biggest_gap 写“核心受控环境 / 工具切断、留出与转移支持优化单位判断”。
- **问题 1（F1 归因，判断错误）**：附录 A 的研究代理指令表明，每个基准交付的“环境”都包含直接进入目标代理上下文的指令 / 引导：
  - AutomationBench 的 access layer 包括 `inject_context`（任务开始时把预取的世界整理成一条 system message 插到提示最前）、“an always-on guide that teaches the assistant the efficient, correct pattern”，以及“the instructions that tell it how to work”（A.1）。
  - Bleve 要求把启动引导写进每轮自动加载的 `layer/CLAUDE.md`（A.4）。
  - Tenacity 规定 `layer/AGENTS.md` 是唯一入口（A.5）。
  - Workspace-Bench 与 Data-Eng-Bench 允许“leave a guide”（A.2、A.3）。

  因此 §4.4 的消融（E0 + E5 的工具 vs 完整 E5）比较的是“只换工具”和“工具 + 数据重组 + 注入的 system 上下文 / 引导”，没有把“同一信息 I 的表示”与“提示 / 上下文层的改动”分开。后者正是论文声称与之正交的 harness / 提示优化轴。与 Meta-Harness、GEPA 的比较同样不能证明这是第三条独立的优化轴。H04 §§1–2 的 holds 和“优化单位判断”的确认高估了现有证据。
- **问题 2（材料）**：所有结果表在钉定 HTML 和 arxiv.org/html/2611.07372v1 上都无法读取（见上文“材料缺口”），§4.4 消融在正文中没有任何数字。L2 的 Q4 确认依赖的表格数字在现有材料中无法核对，需要补读 PDF。
- **问题 3（表述，附带）**：Meta-Harness 叠加的结果，摘要写“adds 11.17% accuracy over Meta-Harness alone”，引言写“16% improvement in pass rate”。多处“%”是相对值还是百分点没有交代（如 Opus 5 的“1.34% gain”）。
- 请 Sol 处理：
  - 补读 PDF 结果表后，复核 q4_fit 是否应为 `partial`（环境表示与注入引导未分离），并据此决定 evidence_status（`pending_material` 或 `pending_experiment`）和 next_action。
  - 如果 Q4 改为 partial，顺带复核 q3 的 judgment 是否仍然成立，还是只支持“环境 + 访问层整体能降成本”的 incremental 判断。
  - 问题本身（Q1、共享环境表示是否值得优化）不在退回范围内。
- 处理：本期暂停该篇，不制作 Reel。

## 待补与其他

- **待补清单（priority=high 但未确认）**：本期范围内 2 篇 `pending_experiment / park`：
  - 2611.07051（`inc-l2-16`）：缺独立真值、真实外环采纳和生产效度；不能用 ICC / kappa 或离线缺陷注入代替。
  - 2611.06972（`inc-l2-16`）：缺专家路径的部署可用性、合理多解与执行失误的区分、逐条回归和独立种子 / 费用。
  - 另有 2611.07469、2611.07595 为 P2 / pending_experiment / park；2611.08483 为 P2 / confirmed / park（程序搜索的增量效率，无编辑例外）；2611.03743 为 P3 / confirmed，但已按范围口径 exclude（反馈进入 RL 权重），不入池。
  - 沿用上期待补：2611.06321、2611.06049、2611.00463。本步均未处理。
- **退回项跟进**：新增 C-011-1（07372），待 Sol 修订。
- **漏检抽查**：本步未执行（progress.md 记欠账约 5.3，滚存；池为 0）。
- **下期备选**：
  - 2611.07372：视 C-011-1 修订结果，且需 PDF 表格。
  - 2611.06768：沿用 selection-010 的条件。
  - 沿用 selection-009 所列：2609.33378、2611.03238、2610.21082、2611.02079。
  - 2611.07048 已按同题去重落选。如果后续出现带实测的评价器错配 / 搜索强度工作，可作为理论背景引用，不单独做 Reel。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2611.08318/`：poster.png（1600×2263）/ poster.pdf（单页 1200×1697pt）/ poster.html / SOURCE.md / QA.md
  - `reel/2611.07624/`：同上
  - `reel/2611.07123/`：同上
- 版式：考试试卷与密封线（08318）、冰山测深报告（07624）、示波器仪器面板（07123），与既有 39 张及彼此互不重复。构建脚本（生成内联 SVG）在本地 `/tmp/rv011/`，poster.html 本身即完整可编辑源。
- 索引更新：
  - `reel/README.md`：头段新增第十一期句，共 42 篇、42 种版式，加 selection 11 链接；表格顶部新增 3 行。
  - 仓库 `README.md`：只改头部统计与 Featured Reel 段的篇数、selection 11 链接和画报墙。
