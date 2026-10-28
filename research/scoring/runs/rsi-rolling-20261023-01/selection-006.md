# L3 选题第六期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席。
- 编号：本仓 Reel 第六期。前五期共 24 篇（[selection.md](../rsi-l1-20261022-03/selection.md)、[selection-002.md](../rsi-l1-20261022-03/selection-002.md)、[selection-003.md](selection-003.md)、[selection-004.md](selection-004.md)、[selection-005.md](selection-005.md)）不再重复入选。
- 候选池：本 run 最新记录为 L2 且 `P3 / confirmed / to_l3` 的 5 篇（`inc-l2-07`：37651、36826、37255、34073；`inc-l2-05`：34027，上期备选）。无 P2 编辑入池项（`inc-l2-07` 的 36774、37046 为 P2 / park，未写编辑理由，不入池）。本期上限 3 篇。
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/<pid>.txt`（均为 arXiv v1，HTML 转文本）。
- 产出：本文件 + `reel/<pid>/` 三套成品。未改动任何 L1/L2 批次记录，未操作 git，未派子代理，未启动无头进程。

## selection_cutoff 说明

本期结果只代表这 5 篇候选、按本期 3 篇上限与去重口径的选择，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论，Reel 不呈现为权威评分。

## 候选（5）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2610.37255 | Your Policy Is Secretly a Harness | P3 / confirmed | judgment | F1, F3 | couple_context_and_weight_updates; diagnose_self_improvement | inc-l2-07 | 正文 §1–§7 + 附录 F.1–F.8 通读；附录 C–E 证明浏览 | **入选** |
| 2610.37651 | GEPA-Curator | P3 / confirmed | judgment | F1, F2 | attribute_and_patch_incumbent | inc-l2-07 | 正文 §1–§6 + 附录 A–F 通读 | **入选** |
| 2610.34073 | Memory Tax | P3 / confirmed | judgment | F1, F5 | diagnose_self_improvement; index_experience_for_reuse | inc-l2-07 | 正文 §1–§8 + 附录 A–C 通读；D–F 浏览 | **入选** |
| 2610.36826 | RuHarness（rubric–harness 共演化） | P3 / confirmed | judgment | F2, F3 | coevolve_the_evaluator; attribute_and_patch_incumbent | inc-l2-07 | 正文 §1–§6 + 附录 A.1–A.8 通读 | 落选（已选同卡同类判断 + 证据较弱） |
| 2610.34027 | GEPA merge 诊断 | P3 / confirmed | judgment | F1, F2 | diagnose_self_improvement; evidence_gated_retention | inc-l2-05 | 正文 §1–§8 复读（上期已含附录 A–D 通读） | 落选（上期理由仍成立 + GEPA 族本期已选 37651） |

## 原文核对（逐篇）

五篇 L2 判断均成立，**本期无 correction**。以下为阅读备注，不改档位、不改记录；画报按备注收窄展示口径。

1. **2610.37255**：§4.2 Table 1、附录 F.3 Table 8–9、F.4 Table 10、§6.3 Table 2 / F.7 Table 13 逐数核实，与 L2 一致（85.0→19.2；85.05→72.90；88.17 vs 83.37；7/9 swaps；ρ = 0.95）。备注：(a) 附录 F.4 另报“只看上限差”排序 ρ = 0.86，正文未提，说明适配后增益主要由 ΔC 决定，T − r₂ 的增量有限——画报并列三个 ρ；(b) H2→H5 回报 +0.045 而成功率 −0.5 点，正则回报与成功率可不同向；(c) 每支训练单次运行，区间为任务 bootstrap（L2 已注）；(d) 对权重永远冻结的纯 harness 闭环，冻结回报就是实际收益，本文改变的是对冻结比较的解读——画报写明。
2. **2610.37651**：Table 1–4、8、附录 A.1–A.2、C.1–C.2、D、E 核实，与 L2 一致（3.4 / 5.0 点；1.31×；12/16；8→9 被接受）。备注：(a) §4.1 “averaged over 5 repeated runs” 未说明是否重复优化，§5.4 成本按“one run per method and benchmark”计，种子 prompt 也带 ±——± 很可能主要反映评测重复而非优化随机性，画报注明歧义；(b) 主结果为完整版 Curator，成本表为高效版（L2 已注）；(c) Table 4 的报告集未写明（“five evaluations of each optimized prompt”）；(d) 附录 E QA 类 HotpotQA −1.3。
3. **2610.34073**：Table 1、2、5、6、12、13、15、16 与 §4–§5 文本核实，与 L2 一致。备注：(a) 本项目按 Table 1 计数：11 × 9 = 99 格中 9 格高于 RAG（2 轮），LongMemEval-s 33 格全负；(b) 逐题收益 / 税计数只在 Fig. 2 / 附录 C.1 图中，文本无数，画报不转述；(c) §6 两条设计建议在 HTML 文本中“Results in Table”后无表，画报不展示；(d) 主体为对话式个人记忆，离 harness 级自我改进最近的是 §5.1 经验记忆（单骨干 Qwen3.5-4B、结果有正有负），画报单列为附表——按 EVIDENCE.md 收录口径与 L2 一致，作为持久非权重记忆更新的 B 类审计组件。
4. **2610.36826**：Table 1、2、6、附录 A.2–A.8 核实，与 L2 一致（动态 53.7 / 无 rubric 45.8 / 冻结 44.4；最强基线 +4.5 / +5.3）。备注：冻结 rubric 劣于无 rubric 的宏平均差 1.4 点由知识工作（34.0 vs 44.0）与代码实现（57.0 vs 65.1）驱动，其余 3 域冻结 rubric 反而高于无 rubric（+6.1 / +2.8 / +2.0）；Table 1–2 为单次运行，held-out 每域 36–100 题，种子重复只在两个设置；无诊断 token 成本。L2 写“支持固定指导**可能**有害”，措辞成立。
5. **2610.34027**：复读 §1–§8，上期核对结论不变（单 seed 优选、按测试集事后挑格、probe 缺同 seed 默认 merge 对照）。

## 排列与取舍

1. 全部 P3、q3 全部为 judgment，不分先后。
2. 同族判断（34027 vs 37651，均为 GEPA 反思式 prompt 优化）：**依原文不是同一问题**。34027 问的是 merge 算子的不稳定是“算法性还是超参性”（§1 L112、§4.1），对象是 merge 的时机与算子；37651 问的是“哪些轨迹对反思是有效信号、应附带什么历史证据”（§2 L333–334、§3），对象是反思器的输入。两者主卡也不同（diagnose_self_improvement + evidence_gated_retention vs attribute_and_patch_incumbent）。因此不按“同题去重”处理；但同为 GEPA 族、本期只取一篇以保持问题族多样性，取证据更直接的 37651（held-out 测试、两种优化器、可追踪的负迁移实例、完整成本拆分）。
3. 34027 上期落选理由复核：(a) 主卡组合与已入选的 2610.34938 相同——仍成立；(b) 标题级“合适配置下 merge 对两模型都有益”来自每格单 seed、按测试集事后挑选，落在作者自测噪声底内——仍成立，原文无新版本；(c) “选择信号噪声底”判断与已入选 2610.28798、2610.30499 同类——仍成立。加上本期 GEPA 族已选 37651，继续落选。
4. 36826 不入选：主卡 coevolve_the_evaluator 已有 3 张画报（2610.28798、2610.29005、2610.35579），其中 2610.29005“评估器在自出考卷上全对、到搜索状态上失准”与本篇“诊断 rubric 随 harness 演化而过时”属同一判断（评估信号随被评对象分布漂移而失效）；按 PROBLEM_CORE §4 “与已选论文内容重复”与 SELECTION “同一张卡保留证据最直接的一篇”，且本篇关键证据（冻结 rubric < 无 rubric）为单次运行、逐域方向不一致。保持 L2 原判（P3 / confirmed），可作下期备选，条件是补多种子消融与诊断成本。
5. 入选三篇的主卡互不相同（couple_context_and_weight_updates / attribute_and_patch_incumbent / index_experience_for_reuse），主族 F1 × 3、次族 F2 / F3 / F5 各一。诊断类占满本期（候选池全为 judgment），按问题族多样性选题，不改任何记录字段。
6. 与既有 24 张的机制区分：37255 是唯一涉及“harness 与权重互相适配”的精确分解（2610.31401 HERD 是把 harness 蒸进权重，不涉及比较规则）；37651 关注反思输入的可学性（2603.28052 Meta-Harness 是提议者能否读原始轨迹）；34073 是“记忆净值相对原始检索”的逐题记账（2601.22436 是经验内容干预，不比原始历史检索）。

## 入选（3）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2610.37255 | F1/F3 | couple_context_and_weight_updates | 用冻结后训练模型比较 harness，会不会把“上限更高、只是这份权重用不好”的 harness 拒掉？ | 把 6 个 harness 编译成有限图，精确算出上限 C 与失配 M（J = C − M），同权重分支等预算续训 / 适配 | H1 冻结 85.05%→72.90%，同 1,024 步适配后 88.17% > 续训 83.37%；9 个被拒换装中升上限的 7 个全部反超，事前预测 ρ = 0.95（冻结变化 0.17）；只倒序观测字段 85.0%→19.2%、最优策略不变 |
| 2 | 2610.37651 | F1/F2 | attribute_and_patch_incumbent | 反思式 prompt 优化把环境 / 任务 / judge 造成的失败当成 prompt 缺陷，会不会写出伤害可解任务的规则？ | Curator 按每任务历史决定跑 / 跳，并给失败配一条有佐证的同任务成功作对照，优化器不改 | 一次坏变异让可解任务 5 步→30 步失败但 minibatch 8→9 被接受；WebArena 四站 held-out 比 GEPA 高 3.4 / 5.0 点；高效版成本 1.31× |
| 3 | 2610.34073 | F1/F5 | index_experience_for_reuse | 把原始历史加工成记忆，相对直接检索原始历史是净赚还是净亏？亏在哪？ | 11 个系统 × 3 基准 × 3 骨干对齐检索范围后与 RAG 比，逐题拆收益 / 税，再拆保真、可达、稳健 | 99 格中 9 格高于 RAG（2 轮），LongMemEval-s 全负；MemoryOS 98.4% 无损仍低 7.6–10.0 点；经验记忆有正有负 |

## Correction

本期无。

## 待补与其他

- **待补清单（priority=high 但未确认）**：本期新增 `inc-l2-07` 的 2610.36077（P3 / pending_experiment / to_l2；缺口见其 L2 `biggest_gap`：需相同总训练 token 下的课程 / 组织对照、无需 Oracle 的模块迁移分析，并说明准备与正式实例是否重叠；补齐后才可能确认 Q4，现有全文不足）。上期所列（`inc-l2-05` 的 33024、33046、33845、33956；`inc-l2-06` 的 35434；35193 P2 / pending_material）及 selection-004 所列 9 篇本步未处理。
- **退回项跟进**：C-005-1（2610.35316）已由 Sol 修订为 P1 / park（`inc-l2-06-rev1-35316.jsonl`），不入池。
- **漏检抽查**：本步未执行。
- **下期备选**：2610.36826（条件见上）；2610.34027（条件同上期：多种子 sweep、同种子默认 merge 对照、独立任务上的选参验证）。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2610.37255/`：poster.png（1600×2263）/ poster.pdf（单页 1200×1697pt）/ poster.html / SOURCE.md / QA.md
  - `reel/2610.37651/`：同上
  - `reel/2610.34073/`：同上
- 版式：黑板粉笔（37255）、美术馆展厅（37651）、官方税表（34073），与既有 24 张及彼此互不重复。
- 索引更新：`reel/README.md` 头段（新增第六期句、共 27 篇、27 种版式、selection 6 链接）与表格顶部新增 3 行；仓库 `README.md` 只改头部统计行（“added 9 → 24 posters”→“added 12 → 27 posters”）与 Featured Reel 段（Twenty-four → Twenty-seven、中文 24 → 27、selection 6 链接、画报墙新增首行 3 张）。README 内其他已知旧数字矛盾（如“8 were checked”“Reel（画报）| 8”）本次未修。
