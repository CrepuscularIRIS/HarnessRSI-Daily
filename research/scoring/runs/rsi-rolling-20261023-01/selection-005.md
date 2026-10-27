# L3 选题第五期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席。
- 编号：本仓 Reel 第五期。前四期共 21 篇（[selection.md](../rsi-l1-20261022-03/selection.md)、[selection-002.md](../rsi-l1-20261022-03/selection-002.md)、[selection-003.md](selection-003.md)、[selection-004.md](selection-004.md)）不再重复入选。
- 候选池：本 run 最新记录为 L2 且 `P3 / confirmed / to_l3` 的 5 篇（`inc-l2-05`：34027、34238；`inc-l2-06`：34938、35316、35579）。无 P2 编辑入池项。本期上限 3 篇。
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/<pid>.txt`（均为 arXiv v1；34238 为 PDF 转文本，其余为 HTML 转文本）。
- 产出：本文件 + `reel/<pid>/` 三套成品。未改动任何 L1/L2 批次记录，未操作 git，未派子代理，未启动无头进程。

## selection_cutoff 说明

本期结果只代表这 5 篇候选、按本期 3 篇上限与去重口径的选择，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论，Reel 不呈现为权威评分。

## 候选（5）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2610.34938 | /retro 复盘改动迁移 | P3 / confirmed | judgment | F1, F3 | diagnose_self_improvement; evidence_gated_retention | inc-l2-06 | 正文 §I–§VI 通读（无附录） | **入选** |
| 2610.34238 | Δτ-Bench + STEWARD | P3 / confirmed | capability | F3, F5 | abstract_experience_into_guidance; index_experience_for_reuse | inc-l2-05 | 正文 §1–§8 + 附录 A–C 通读，附录 D 提示词浏览 | **入选** |
| 2610.35579 | Infinity Machine | P3 / confirmed（范围限评分漏洞与自改未晋升） | judgment | F1, F2 | diagnose_self_improvement; coevolve_the_evaluator; make_the_improver_editable | inc-l2-06 | 正文 §1–§7 + 附录 A–F 通读 | **入选**（按 L2 范围展示） |
| 2610.34027 | GEPA merge 诊断 | P3 / confirmed | judgment | F1, F2 | diagnose_self_improvement; evidence_gated_retention | inc-l2-05 | 正文 §1–§8 + 附录 A–D 通读 | 落选（同卡去重 + 证据边界） |
| 2610.35316 | RSIV-Harness | P3 / confirmed | capability | F3, F5 | attribute_and_patch_incumbent; evidence_gated_retention | inc-l2-06 | 正文 §1–§6 通读（无附录） | **暂停，correction 退回** |

## 排列与取舍

1. 全部 P3。q3：capability（34238、35316）与 judgment（34938、35579、34027）并列不分先后。
2. 原文核对：35316 发现 L2 问题判断错误，按规则暂停并写 correction（见下），不入选；表间数字待澄清项也一并记录。其余 4 篇 L2 判断成立，仅有阅读备注。
3. 剩余 4 取 3。判断顺序：问题是否清楚、证据是否直接、与已有 21 张及本期其他入选的机制 / 卡片是否重复。
   - **2610.34938**：问题最清楚、干预最直接——单条改动 on/off 各 5 次、新容器、同提示，并逐会话记录“遇到 / 覆盖 / 加载 / 查阅 / 复现”。结论是可核查的反例集：7 个有信息事件中 2 消除、1 减轻、4 未减少，无关对照上 0/5 → 4/5。与 2601.22436（七类内容干预、聚合层面）机制不同：本篇是逐条留存产物的迁移检验。与 34027 共享主卡组合（diagnose_self_improvement + evidence_gated_retention），保留本篇（见 34027 落选理由）。
   - **2610.34238**：本期唯一入选的 capability。问题（工具持续退役 / 拆分 / 合并时留存技能跟不上，且成功率掩盖错过的更短路径）有本文自测；同一 v1 库下冻结 / 全量重建 / 增量维护对照直接隔离维护策略，并有成本列。与 2610.07792 ServeLearnBench（隐藏漂移策略、F4）、2605.06614 SkillOS（只训 curator）机制不同。
   - **2610.35579**：主卡（coevolve_the_evaluator、make_the_improver_editable）与本期另两张不同。按 L2 确认范围只展示：唯一自导 genome 候选因成本 2.02 > 1.5 被拒、所有发现出自初始 genome；操作者手写策略臂对稳定子秩与 LM 结果起决定作用；4 次评分器被钻；自主运行 2 评分方向写反却穿过校准、审计、盲查、报告。与 2610.29005 VeriEvolve（评估器自出考卷 vs 搜索状态）、2610.28798（精确验证分泄露）不同：本篇的新点是“检查只测接受对象，不测分数方向”，以及自改收益与操作者贡献的分账。证据为个案级存在性反例，画报如实标注。
4. 族覆盖：本期主族 F1×2（34938、35579）、F3×1（34238）；F2、F5 作次族出现。诊断类（judgment）占 2/3，34238 补足 capability。

## 入选（3）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2610.34938 | F1/F3 | diagnose_self_improvement | 复盘产生并实施的 harness 改动，能否在同仓库后续任务中减少它针对的重复动作？断在哪一环？ | 12 条改动一次一条迁移，原版 / 改后各 5 个新容器会话，逐会话标注遇到、查阅、复现 | 7 个有信息事件：覆盖实际实例的 2 条 5/5→0/5、3/5→0/5；未覆盖的 1 条 5/5→2/5、4 条未减少；Sphinx 对照 0/5→4/5、82→245 s；任务成功最多差 1 会话 |
| 2 | 2610.34238 | F3/F5 | abstract_experience_into_guidance | 工具生态持续演化时，留存技能能否及时修订、并发现更高效路径？ | Δτ-Bench：六版本保能力变换 + 构造空间内最优路径 + SPE/IDR/DAR；STEWARD 按依赖增量维护三级技能、按需供给 | 最强 SR 42.27，召回 90.36 / 精确 19.90；v3 EvoSkill/AutoSkill DAR 0 对不用技能 11.11；增量维护比全量重建 +2.22/+1.82 点、维护 token −39.5%/−30.4% |
| 3 | 2610.35579 | F1/F2 | coevolve_the_evaluator; make_the_improver_editable | 可自改研究 harness 如何把真实发现与评分器漏洞、操作者贡献、不划算的自更新分开？ | kernel / genome 分离 + 成本闸门；自主模式以校准、对抗审计、盲查替代人工批准；作者完整自报负结果 | 自改候选 held-in 0.944 vs 0.927、成本 2.02× 被拒；4 次钻空子（TESS 重评 94.5→30.5）；反向评分下 179 会得 0.364 < 记录 0.455，四道检查都放行 |

### 逐篇原文核对状态与展示边界

1. **2610.34938**：Table I、Table II 逐行、§III 抽样 / 合格 / 迁移定义、§IV 时长与成功率、§V 全部核实，与 L2 一致。边界（画报已写）：后续 issue 为挑选复现问题者、第二批会话非随机；5 会话 / 7 事件；覆盖分组为标注后事后分组；标注非完全盲；挑选、实施、标注均由作者完成；一个代理、一个 /retro、只涉及环境类问题；动作减少不等于任务改善。
2. **2610.34238**：Table 1、Table 2、Table 3、§4.2–4.3 与 §6 正文数值、附录 A–C 核实，与 L2 一致。阅读备注（不改档位，画报已写）：Table 2 中 DeepSeek-V3.2 增量维护平均 SR 36.83 与 Fig. 6 / §6 中 STEWARD 平均 39.04 口径不同，原文未说明（可能是供给设置或平均范围不同），画报两处分开引用。其余边界：合成 42 领域、一条变化流；“最优”只在构造实现空间内；成本为 LLM 赋 1–10 分；全部单次运行、无种子方差；用户模拟器与技能研究任务模型均为 DeepSeek-V3.2。
3. **2610.35579**：§2、§3.8、§4 全部小节、Table 1/3/4/5、附录 B、E、F 核实，与 L2 一致。L2 已注的“seven in ten”与 Table 5 不精确一致确认属实：未超过父代 65/104 = 62.5%，画报写明出入。展示边界：只按 L2 确认范围呈现负结果与归因；量子信息、SABRE、芯片、TESS 等发现均为操作者主导战役，不作为自改或自主发现证据重述；无种子 / 消融 / 等算力；精确验证类任务公开 = 私有划分。

## 落选（1）与退回（1）

### 2610.34027（GEPA merge 诊断）——同卡去重 + 证据边界

- 原文核对：Table 3、4、5、7、8 与 §4.2–§6.2 核实，L2 判断成立，不写 correction。核对确认：29 对 probe 结果最差恰为 −10.00（Qwen × HotpotQA seed 1），GPT 五任务均值为正、Qwen 三任务均值为正，与正文一致。
- 不入选理由：与入选的 34938 共享主卡组合（diagnose_self_improvement + evidence_gated_retention），按“同一张卡保留问题最清楚、证据最直接的一篇”保留 34938。本篇最稳的发现是诊断性的（NoMerge 种子标准差 3–5 点；单种子灾难格重跑不复现；仅提示词特征 AUC ≤ 0.58；逐步 Δval 反思在 10 个模型-任务对上都高于 merge），而标题级主张“合适配置下 merge 对两模型都有益”来自每格单种子、按测试集事后挑 9 个配置中的最优，落在作者自测的噪声底内；probe 缺同种子默认 merge 对照。“选择信号噪声底”这一判断与已入选的 2610.28798、2610.30499 同属一类，本篇的独立增量有限。
- 去向：保持 L2 原判（P3 / confirmed）；若作者补多种子 sweep、同种子默认 merge 对照与独立任务上的选参验证，可作为下期备选。

### 2610.35316（RSIV-Harness）——correction，退回 Sol 单篇修订

见下节。按 SELECTION“发现 L2 判断错误时暂停该篇”，本期不入选、不制作。

## Correction

### C-005-1 · 2610.35316（退回 Sol 单篇 L2 修订；保留旧记录 `inc-l2-06#2610.35316`）

- **原判**：q2_open = `open_failure`，q3 = `capability`，q4 = `fits`，P3 / confirmed / to_l3。L2 理由：“未知数据源、对话歧义与跨轮约束改变可用信息和任务条件，不自动判 vertical_port”。
- **问题 1（Q2，影响档位）**：上述约束是**被改进的任务代理**面对的任务条件，不是**改进机制**面对的约束。自改回路本身（从训练失败轨迹聚类 → 有界编辑 → 验证锚 + 回归记忆门 → 拒绝回滚）在本文的条件仍是：冻结权重、带金标的训练任务、可执行等价比较器、固定验证锚——与本文 §2.2 自引的既有 harness 演化工作（“weakness-driven proposal with regression testing”等）同一问题、同一条件；本文自述的差别（“不支持开放库澄清、不支持查询-图表耦合的多轮回归验证提交”）都是领域属性。L2 的 card_anchor 本身引用了 attribute_and_patch_incumbent 的失败模式“不能将通用回路的领域应用当机制贡献”。按 PROBLEM_CORE §3 Q2 定义，就 harness-RSI 问题而言更接近 `vertical_port`（封顶 P1）。ODAC-Vis 基准对 text-to-vis 领域或有新意，但不属于本项目的 RSI 问题层面。
- **问题 2（Q3 / Q4，影响 confirmed）**：
  - 标题级 +28.02（可执行性）、+34.01（图表结构）的比较对象是作者刻意设为“最小”的种子 H0；该种子在 DeepSeek 上可执行性 64.98、执行准确率 24.51，均低于单次调用、无工具的 Direct Prompt（81.32、31.91）。最能反映图表数据是否正确的执行准确率，演化后 31.52 仍低于 Direct Prompt 31.91。
  - 跨骨干：冻结 harness 在 GPT-6 Luna 上相对最强 GPT 基线多数指标更低（可执行性 −4.67 等），执行准确率较静态 harness 反降 0.78。
  - “避免修复新失败损害已解决案例”这半个问题，在测试集上没有直接测量（无逐例回归统计）；唯一证据是“去稳定规则”再跑一轮的整体对比——两侧各一次运行、无种子。§5.1.4 只演化一轮、无独立谱系、无总提议成本。
  - 据此 q4 至多 `partial`，q3 的 capability 主张（“解决后可支持联合约束下的跨任务修复”）证据不足，更接近 `incremental` 或 `local`。
- **问题 3（表间数字待澄清，L2 已标记）**：Table 3“Static Harnesses / DeepSeek”可执行性 64.98，Table 4“H0”行 51.36，其余五列完全一致。摘要的 +28.02 = 93.00 − 64.98（Table 3 口径）；若 Table 4 正确则为 +41.64。另注意 51.36 与 Table 3 GPT 静态行 51.75 接近，可能是抄录错误，但无法从原文判定。该差异不改变上面问题 1–2 的结论，但任何展示都只能标为“Table 3 口径”，且需作者澄清；本项不足以单独构成 correction，并入本条。
- **建议修订（供 Sol 单篇复核，不在此直接改记录）**：q2_open → `vertical_port`（或至少写明 q2_prior 为本文 §2.2 自引的回归测试式 harness 演化工作，并重新论证开放性），q4 → `partial`，q3 → `incremental`/`local`；problem_tier 相应降为 P1（或 P2 并写理由），evidence_status 视修订结果定；next_action 不再为 `to_l3`。
- 本期不制作该篇画报。

## 待补与其他

- **待补清单（priority=high 但未确认，本期新增的 L2 记录）**：`inc-l2-05` 的 2610.33024、2610.33046、2610.33845、2610.33956（均 P3 / pending_experiment / park），`inc-l2-06` 的 2610.35434（P3 / pending_experiment / to_l2）；缺口见各自 L2 `biggest_gap`，补齐后由 Sol 单篇 L2，不在此处直接入选。另 2610.35193 为 P2 / pending_material / medium。上期待补清单（selection-004 所列 9 篇）本步未处理。
- **漏检抽查**：本步未执行、未复核。
- **下期备选**：2610.34027（条件见上）；2610.35316 视 Sol 修订结果而定。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2610.34938/`：poster.png（1600×2263）/ poster.pdf（单页 1200×1697pt）/ poster.html / SOURCE.md / QA.md
  - `reel/2610.34238/`：同上
  - `reel/2610.35579/`：同上
- 版式：代码评审页（34938）、地铁线路图（34238）、会计账簿（35579），与既有 21 张及彼此互不重复。
- 索引更新：`reel/README.md` 头段计数（新增第五期句、共 24 篇、24 种版式、selection 5 链接）与表格顶部新增 3 行；仓库 `README.md` 只改头部统计行（“added 6 → 21 posters”→“added 9 → 24 posters”）与 Featured Reel 段（Twenty-one → Twenty-four、中文 21 → 24、selection 5 链接、画报墙新增首行 3 张）。README 内其他已知旧数字矛盾（如“8 were checked”“Reel（画报）| 8”）本次未修。
