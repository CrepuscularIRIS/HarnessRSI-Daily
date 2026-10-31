# L3 选题第七期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席。
- 编号：本仓 Reel 第七期。前六期共 27 篇（[selection.md](../rsi-l1-20261022-03/selection.md)、[selection-002.md](../rsi-l1-20261022-03/selection-002.md)、[selection-003.md](selection-003.md) 至 [selection-006.md](selection-006.md)）不再重复入选。
- 候选池：本 run 最新记录为 L2 且 `P3 / confirmed / to_l3` 的 9 篇（`inc-l2-07`：36826，上期落选备选；`inc-l2-08`：37201；`inc-l2-09`：39122、40023、38392、39714、39358、39417、39813）。无 P2 编辑入池项（`inc-l2-09` 的 39508、39884、30851 为 P2 / park，未写编辑理由，不入池）。本期上限 3 篇。
- 产出：本文件 + `reel/<pid>/` 三套成品。未改动任何 L1/L2 批次记录，未操作 git，未派子代理，未启动无头进程，未运行论文代码。

## selection_cutoff 说明

本期结果只代表这 9 篇候选、按 3 篇上限与去重口径的选择，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论，Reel 不呈现为权威评分。

## 钉定全文位置（数据管线提示，请总控处理）

`inc-l2-09` 的 7 篇（39122、40023、38392、39714、39358、39417、39813）的钉定全文与 pin 不在本 run 目录，而在 `research/fulltext/review-runs/rsi-l1-20261022-03/materials/<pid>.txt` 与 `research/scoring/runs/rsi-l1-20261022-03/materials/<pid>.json`（后者在当前 git status 中为未跟踪文件；同目录还有 38946、39508、39884、40191、39158 等本班材料）。sha256 与 pin 逐一核对一致（39122 `d677b93d…`、38392 `43d10529…` 等），内容可用；只是位置与本 run 其他论文（`…/rsi-rolling-20261023-01/materials/`）不一致。本期 SOURCE.md 按实际路径记录，未移动任何文件。

## 候选（9）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2610.39122 | 授权混淆（自我演化降低 IPI 鲁棒性） | P3 / confirmed | judgment | F2, F4 | diagnose_self_improvement; abstract_experience_into_guidance | inc-l2-09 | 正文 §1–§5 + 附录 A–E 全部通读 | **入选** |
| 2610.38392 | Masked Erosion | P3 / confirmed | judgment | F2, F3 | evidence_gated_retention; diagnose_self_improvement | inc-l2-09 | 正文 §1–§5 + 附录 A–K 全部通读 | **入选** |
| 2610.37201 | BiPA（技能优化器归因） | P3 / confirmed | judgment | F1, F2 | diagnose_self_improvement; evidence_gated_retention | inc-l2-08 | 正文 §1–§7 + 附录 A–G 全部通读 | **入选** |
| 2610.40023 | HEMO | P3 / confirmed | capability | F1, F3 | make_the_improver_editable | inc-l2-09 | 正文 §I–§VI 通读；附录 H 实验细节读完，其余附录浏览 | **暂停 · 退回**（C-007-1） |
| 2610.39714 | MolRSI | P3 / confirmed | capability | F3, F1 | make_the_improver_editable; search_agent_architecture | inc-l2-09 | §1–§3 通读；Methods / 补充材料按 RSI 对照检索阅读（S3.2、Table S13） | 落选（RSI 贡献与湿实验命中未隔离） |
| 2610.39358 | Skill Utility Shifts | P3 / confirmed | capability | F1, F3 | evidence_gated_retention; couple_context_and_weight_updates | inc-l2-09 | 全文（正文 + 附录 A–B）通读 | 落选（诊断评估标签依据不清 + 与上期 37255 同卡） |
| 2610.39417 | ExLabel（SWE 数据质量） | P3 / confirmed | judgment | F2, F5 | coevolve_the_evaluator; abstract_experience_into_guidance | inc-l2-09 | 正文 §1–§9 通读；在线附录未读 | 落选（同卡已饱和 + 基准清洗与所学经验同向） |
| 2610.39813 | EvoTeam | P3 / confirmed | judgment | F3, F5 | search_agent_architecture; abstract_experience_into_guidance | inc-l2-09 | 正文 §1–§6 + Limitations 通读；附录未读 | 落选（证据较弱、作用域未隔离） |
| 2610.36826 | RuHarness（rubric–harness 共演化） | P3 / confirmed | judgment | F2, F3 | coevolve_the_evaluator; attribute_and_patch_incumbent | inc-l2-07 | 上期已通读（selection-006）；本期确认无新版本，未复读 | 落选（上期理由仍成立） |

## 原文核对（逐篇）

**本期有 1 项 correction（C-007-1，40023）**；其余八篇 L2 判断成立。以下为阅读备注，不改档位、不改记录；画报按备注收窄展示口径。

1. **2610.39122**：Table 1–3、5–7 与附录 B.3、C.3–C.5、D.2–D.5 逐数核实，与 L2 一致（反馈对照 35.8 / 35.0 / 5.8；分隔 97.5→47.5）。备注：(a) 摘要的 “14.0–48.8 / 3.0–39.3” 只来自第 1 种适应顺序；顺序 2、3 方向一致（21/21 均值上升），但幅度大幅波动（RL·GPT-OSS-120B：+39.3 / +10.8 / +0.8；技能·Qwen3.8-27B：+17.8 / +37.7 / +66.7）——画报并列三列；(b) 反馈对照只在 Qwen3.8-27B × File–Create、每条件一个库；(c) 有害指令 119/162 的 27 条指令经单回合初筛挑选（D.3），不是发生率；(d) 演化后代理的重测是预设但不对称的规则（B.3）。
2. **2610.38392**：Table 1–3、7、14、17、20–23、30–35 与 §4 文本核实，与 L2 一致。备注：(a) 图 1 谱系即 Table 14 “veto ρ=1 第 5 条”，终态 {verify}：DeepSeek 0.025、Qwen3-30B 0.575（Table 34）；(b) 自然改写层“多放过 0.19”是只计能抽出规则的探针，全部合并为 0.325（附录 G）——画报两数并列；(c) 120 任务批为有放回重采样，去重翻转 4/10 接受，作者自己声明只确认方向；(d) 换模效应只在更弱执行模型上显著（Luna / Sol 差 0.025）。
3. **2610.37201**：Table 1、附录 C.1–C.5、D.1–D.3、E.1–E.3、F.1–F.2 核实，与 L2 一致（+0.1 / UB +1.6；1.16×；73% / 21%；93% / 10%；337 条中 0 条限读）。备注：(a) 回放结论依赖“从种子最低开发分起算”，随机起点下 τ³ 的 P 降到 0.02–0.17（L2 已注）；(b) Luna AutoBench 增益真实，作者的成本规则在那里会退回种子；(c) AutoBench 的串行写有并发覆盖的正当理由，log ρ 减半的大头即这些写——画报写明“并非每个多出的回合都是浪费”；(d) 每格只有一次优化运行。
4. **2610.40023**：见 C-007-1。另：与最强 LLM-AOD 基线（MPaGE / E2OC）差距多在千分位到百分位（如 Bi-TSP20 HV 0.6258 vs EoH 0.6266），Table I 无方差；迁移任务（新记忆，信息条件可比）上 9 格中 5 格最优。
5. **2610.39714**：L2 判断成立（L2 已注湿实验为历史非同期对照、每目标一次搜索）。补充备注：(a) MART-1 上“有 / 无 RSI”的 EF@1% 3.65 vs 0（Table S13）——按 27/3,845 阳性折算，前 1%（约 38 个候选）中约 1 个命中 vs 0 个，EF@2% 约 3 个 vs 0 个，是本项目按原文数据的折算，单目标、单次搜索；(b) 抗菌 17/107（15.9%）vs 历史专家 21/241（8.7%）、pMHC 8 个命中 vs Claude Science 0 个，比较的是整条工作流，湿实验中没有“无 RSI”臂，命中不能归于跨任务记忆；(c) 抗菌六目标“有 RSI 全部提升”的逐目标数值只在图中。
6. **2610.39358**：L2 判断成立。阅读备注（请 Sol 复核时顺带澄清，非 correction）：Table 1 共评估 25+42+22+18+20+11 = 138 个技能并给出“下降”比例，而附录 B.3 / 图 6 只报告 47 个“至少两个任务支撑”的技能估计、其中 36 个区间不含 0（17 降 19 升）——其余技能的“下降”标签似乎来自点估计，AP / P@5 的正类集合可靠性不清；L2 的 H29 §5 记为 holds，未提及这一缺口。
7. **2610.39417**：L2 判断成立，L2 已在 H25 §§1–2 指出“作者清理‘exact-message 却判 adequate’项，选择偏差未完全排除”。补充：人工清洗删除的两类“错误标注”（外链信息、精确报错信息断言）正是 ExLabel 展示的经验规则（“避免过度规定实现细节”）所针对的模式，清洗方向与被测方法的所学经验同向，使留出一致性对该规则有利；下游 SFT 为单次训练。
8. **2610.39813**：L2 判断成立。补充：单基准演化平均 58.85 vs Meta-Team 58.30（+0.55，LOCA 63.75 vs 69.58 落后）；混合演化 +4.03；“负迁移”动机来自预实验图 2a（正文无数值）。
9. **2610.36826**：无新版本；上期备注与落选条件（补多种子消融与诊断成本）未变。

## 排列与取舍

1. 全部 P3；q3：capability 3 篇（40023、39714、39358），judgment 6 篇，不分先后。
2. **同卡去重**：coevolve_the_evaluator 已有 3 张画报（2610.28798、2610.29005、2610.35579，另 2610.02920 为对抗共演化），本期又有 36826、39417 两篇——两篇均落选：36826 理由同上期；39417 的核心证据（留出标注一致性）受基准清洗方向影响，证据不如同卡已选论文直接。
3. **同族判断（39122 vs 38392，均为“自我改进侵蚀安全”）**：依原文不是同一问题。39122 问的是**学到的内容**——正常正反馈让留存技能丢掉“用户授权”这一条件（§3.2）；38392 问的是**验收门看得见什么**——重叠防护下单层删除被掩蔽，门只按成功率决定（§3.2–3.3）。对象（技能文本 vs 验收规则）、机制（授权泛化 vs 冗余不可观测）、主卡均不同，两篇并选，并记录本期安全主题占两席这一编辑选择。
4. **37201 与既有画报**：其“开发增益落在挑选噪声里”与第三期 2610.28798（反馈契约）、2610.30499（ARC-AGI-3 留出）属同一判断，按 SELECTION “同一张卡保留证据最直接的一篇”，这一半不构成入选理由。入选理由是另一半：**成本藏在回合而不是技能长度里**（回合变化解释 93% 的 token 变化方差、技能长度 10%；337 条新增规则无一限读；被拒与被留编辑 token 涨幅无差别）——这一判断在既有 27 张中没有。画报重心放在成本记账，选择噪声部分写明与 28798 / 30499 同判断。37201 与 38392 卡片组合相同（diagnose_self_improvement + evidence_gated_retention），但问题不同（开发增益与成本 vs 安全冗余），不作同题去重。
5. **capability 三篇未入选**：40023 退回（C-007-1）；39714 的 RSI 贡献在湿实验中未隔离、计算对照每目标一次搜索；39358 诊断评估的标签依据不清，且主卡 couple_context_and_weight_updates 上期刚选 2610.37255。本期因此全为 judgment，记作编辑理由，不改任何记录字段。
6. 入选三篇主族 F2 × 2、F1 × 1，次族 F4 / F3 / F2；主卡 diagnose_self_improvement（39122、37201）与 evidence_gated_retention（38392）。

## 入选（3）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2610.39122 | F2/F4 | diagnose_self_improvement | 个人代理从正常正反馈中自我演化，攻击者不参与学习，IPI 鲁棒性会变差吗？ | 两阶段受控设计：授权请求下学习、未授权请求下用新内容注入测试；确定性状态验证；反馈语义对照 | 技能演化后 5 任务均值 ASR 升 14.0–48.8 点（顺序 1；三顺序 21/21 方向一致、幅度波动）；只奖励“不执行未授权任务”把 35.8% 降到 5.8%，多加只读经历无效（35.0%） |
| 2 | 2610.38392 | F2/F3 | evidence_gated_retention | 重叠的安全规则中删一条时，验收门为什么看不见？ | 4 层防护 16 子集危害格点 + 411 条谱系 × 10 种门；成本剂量与批量的事前冻结预测；换弱模型复测 | 被掩蔽删除的子代独有危害 0.016；配对门压住漂移却在规则有成本时失守，20 任务批全保、40 任务批全失；审计门终态换 Qwen3-30B 滥用 0.575 |
| 3 | 2610.37201 | F1/F2 | diagnose_self_improvement | 技能优化器的开发增益是挑选出来的吗？多出的成本来自哪里？ | 用未改动候选回放接受规则；回合 × 上下文二部图与四项 token 拆分 | 16 个技能测试成功率 +0.1 点、输入 token 1.16×；73% 的增量来自多出的回合；回合变化解释 93% 方差、文本长度 10% |

## Correction

**C-007-1 · 2610.40023（HEMO）· 退回 Sol 单篇修订（保留原记录，不直接修改）**

- 原判：`inc-l2-09` L2，q4_fit = fits，P3 / confirmed / to_l3；子卡 H19 Step-by-Step §5 记 partial，依据只写“推理 2000/4000 调用和 timeout 共享，外层 200 状态评估与多模型生成额外成本未全等化”。
- 问题：原文附录 H（“HEMO self-evolution and inference settings”段）写明 **“For same-task inference, up to the latest 1,000 memory records collected during harness self-evolution are loaded to warm-start the memory filesystem”**，而基线（EoH、MEoH、MPaGE、E2OC）在“相同候选生成预算”下从空记忆起步（附录 H “LLM-based AOD baselines”段）。即源任务主表（Table I、Table III 的 ID 列）中，HEMO 除了被演化的 harness，还带着在**同一任务**上自我演化阶段积累的评测记录；只有迁移任务（“no source-task memory is transferred”）的信息条件可比。L2 未识别这一信息 / 算力不对等，H19 §5 的证据描述不完整。
- 影响：源任务上的优势不能单独归于“可编辑搜索控制”（F1 归因）；能支持该问题的是迁移表（Table II：9 格 5 格最优、4 格第二）与消融（Table V，需确认各变体是否同样暖启动）。请 Sol 复核 q4_fit 是否应为 `partial`，并据此决定 evidence_status / next_action（PROBLEM_CORE §4：P3 需 L2 确认 Q4 fits 才为 confirmed）。问题本身（Q1–Q3）不在退回范围内。
- 处理：本期暂停该篇，不制作 Reel。

## 待补与其他

- **待补清单（priority=high 但未确认）**：本期范围内新增 2610.39158（`inc-l2-09`，P3 / pending_experiment / park：需冻结技能 / 独立请求与盲评锚点、匹配生成 seed 与渲染预算的对照，直接报告误准入与跨任务回归；现有全文不足）、2610.35966（`inc-l2-08`，P3 / pending_experiment / park：需同表示 / 任务 / 预算下的归因、护栏分别去除或随机路由对照及独立搜索重复）。selection-006 及更早所列待补项本步未处理。
- **退回项跟进**：C-007-1（40023）待 Sol 修订。
- **漏检抽查**：本步未执行（`inc-l2-09` 抽查 30851 维持原判 P2 / park，见 progress.md，不在本池）。
- **下期备选**：2610.39714（条件：同一湿实验批次中设“无跨任务记忆”臂，或多次独立搜索的 RSI 对照）；2610.39358（条件：澄清 Table 1 下降标签与 B.3 区间支撑的关系）；2610.36826（条件同上期）；2610.40023（视 C-007-1 修订结果）。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2610.39122/`：poster.png（1600×2263）/ poster.pdf（单页 1200×1697pt）/ poster.html / SOURCE.md / QA.md
  - `reel/2610.38392/`：同上
  - `reel/2610.37201/`：同上
- 版式：即时通讯工作区（39122）、地层剖面（38392）、收银台小票（37201），与既有 27 张及彼此互不重复。
- 索引更新：`reel/README.md` 头段（新增第七期句、共 30 篇、30 种版式、selection 7 链接）与表格顶部新增 3 行；仓库 `README.md` 只改头部统计与 Featured Reel 段的篇数和链接。
