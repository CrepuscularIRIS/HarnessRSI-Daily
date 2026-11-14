# L3 选题第十五期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席串行。
- 编号：本仓 Reel 第十五期。前十四期共 51 篇（[selection.md](../rsi-l1-20261022-03/selection.md)、[selection-002.md](../rsi-l1-20261022-03/selection-002.md)、[selection-003.md](selection-003.md) 至 [selection-014.md](selection-014.md)）不再重复入选。
- 候选池：6 篇，均为 `inc-l2-21` 新增、最新记录 `P3 / confirmed / to_l3`：2611.15268、2611.15276、2611.15309、2611.15700、2611.16378、2611.16591。`inc-l2-21` 其余记录（2611.15178、2611.17068、2611.15754 P3 / pending_experiment / park；2611.15481、2611.14949 P2 / pending_experiment / park）不入池。本期上限 3 篇。
- 产出：本文件 + `reel/<pid>/` 下两套成品。没有改动任何 L1/L2 批次记录，没有操作 git、派子代理、启动无头进程或运行论文代码。

## selection_cutoff 说明

本期只代表这 6 篇在 3 篇上限和去重口径下的取舍，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论。本期**只选 2 篇**：第三个位置的两个候选（15276、15700）都与既有画报同族、关键增量落在噪声量级附近，按 SELECTION.md “允许少于上限”不凑数。

## 钉定全文位置

6 篇都在 `research/fulltext/review-runs/rsi-l1-20261022-03/materials/<pid>.txt`，pin 在本 run 的 `materials/<pid>.json`。sha256 已逐一核对，全部一致；都是 `complete: true`、v1、HTML 来源，corpus 中 `latest_version` 均为 v1。本期未从 arxiv.org 补读。

| pid | sha256 |
|---|---|
| 15268 | `22a1b30a…` |
| 15276 | `4093924b…` |
| 15309 | `e8656868…` |
| 15700 | `34c97b8a…` |
| 16378 | `764a9eab…` |
| 16591 | `dbdc4433…` |

## 候选（6）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2611.15268 | Knowledge in the Harness, Reliability in the Weights | P3 / confirmed | judgment | F1, F3 | couple_context_and_weight_updates; attribute_and_patch_incumbent | inc-l2-21 | 正文 §1–§6 + 附录 A–E 通读 | **入选** |
| 2611.16591 | Singularity-Bench | P3 / confirmed | judgment | F2, F4 | diagnose_self_improvement; coevolve_the_evaluator | inc-l2-21 | 正文 §1–§7 + 附录 A 通读；B–G 浏览；H 体例通读、其余浏览 | **入选** |
| 2611.15276 | Verify by Doing（VbD） | P3 / confirmed | capability | F2, F4 | coevolve_the_evaluator; evidence_gated_retention | inc-l2-21 | 正文 §1–§6 + 附录 A、B 通读；C–E 未读 | 落选（见下） |
| 2611.15700 | AskALCF | P3 / confirmed | judgment | F1, F2 | attribute_and_patch_incumbent; coevolve_the_evaluator | inc-l2-21 | 全文通读（无附录） | 落选（见下） |
| 2611.15309 | Where Autonomy Belongs（EvoTrias） | P3 / confirmed | judgment | F4, F1 | population_search_executable_fitness; diagnose_self_improvement | inc-l2-21 | 正文 §1–§7 + 附录 C.10 通读；其余附录未读 | 落选（同题去重） |
| 2611.16378 | Evidence-Governed Adoption（EGE） | P3 / confirmed | judgment | F2, F5 | evidence_gated_retention; coevolve_the_evaluator | inc-l2-21 | §1–§5 通读，§8 Monte Carlo 与局限核对 | **退回（C-015-1）** |

## 原文核对（逐篇）

### 1. 2611.15268（入选）

已核对表 2、3、11–15，§4–§5.6，Limitations，附录 A、E，与 L2 一致：2×2 交叉 72.6/56.0、78.3/62.5、77.4/68.5、85.1/75.5（零售 / 航空 pass¹）；“从没解出”组规则 44 vs 权重 25（零售，n=8）、27 vs 5（航空，n=15）；“本来全会”组权重 95 / 99 vs 规则 87 / 93；行李额等航空计算知识点上只换权重几乎不动。

备注（不改档位）：
- (a) 零售 pass⁴ 交互 +12.3 [−0.9, 25.4]、零售“只加规则” pass¹ +4.8 [−0.7, 10.3] 区间都跨 0；画报只作方向。
- (b) 航空“从没解出”的 15 题有 14 题受技能拆分影响；拆分本身让起点比参考代理低 11.5 点，规则先修回自身造成的损失。不受拆分影响的 19 题终版 +14.5 才是较干净的提升。L2 已注“拆分损失恢复不当新能力”，画报⑥写明。
- (c) 噪声分析是这篇的附加价值：同种子对话题内相关 −0.09–0.07，回归均值会让 22/60 的保留决策反向；V 与官方增益 r = 0.98。

### 2. 2611.16591（入选）

已核对表 2–7、§4.1–4.3、§5、§6.1–6.4、附录 A.1–A.2、附录 H 体例，与 L2 一致：Harbor 被表 3 的攻击全部得手、加 LLM 裁判后表 4 的 6 条仍得手、Breakwater 下全部拦下；主表每格单次运行；API 成本不含 GPU。

备注：
- (a) 表 3 是作者所列的“a selection”，按 OWASP 计 22 条；不是攻击库全部，也没有未知攻击的命中率。L2 已注“防护围绕已发现攻击构造”。
- (b) 单次运行的波动在作者自己的消融中可见：Opus 5.5 推理引擎 high 档单代理 $7.31 < SGLang $8.18，max 档 $11.52；harness 领先只来自一次额外的 PR 成功；中期训练 1.82 倍单项拉高指数（去掉后其余五项平均约 1.14，本项目计算）。
- (c) 摘要“suggesting it may have the skills needed to reach the singularity”超出证据；L2 已写“不认证 Singularity-Index 意味着递归制造更强继任者”。画报写为本项目不支持的表述。
- (d) 利益相关：榜首代理为 Opus 5.5，本期制作者同为 Opus 5.5。画报只引作者数字并在页首声明，E 栏专列该代理的不稳定性。

### 3. 2611.15276（落选）

已核对表 1–3、8–11，§4–§5，附录 B.1–B.9，与 L2 一致：三基准、两骨干、每方法三次运行；固定 BoN 池上只换评价器 pass 31.2 → 35.8；回退拒绝率 89.3% vs RQGM 71.2%。

备注：“w/o Evaluator evolution” 在 AutomationBench 上只低 1.6 点（35.4 ± 1.8 vs 37.0 ± 1.9），与三次运行的 SD 同量级；harness 与历史每题重置，没有跨任务保留（作者局限中承认）。L2 已注“不认证跨任务 retained/improver”，不构成判断错误。

### 4. 2611.15700（落选）

已核对 §III–§VI、表 II–V，与 L2 一致：98 / 52 按会话切分，接受的 3 个分支使留出集 35/52 → 40/52；16 个分支含 9 拒绝与 null。

备注：留出增量是 5 题；同一份 171 条路由上，语义中性的改动因绕过缓存就会改变 9 和 11 条路由，两者量级相近；编辑由人类专家提出，修复只做到离线注入、未进部署索引。L2 已注“52 例 / 单站点 / 单次 campaign”“不宣称自主演化”，不构成判断错误。

### 5. 2611.15309（落选）

已核对 §3–§6、表 1–3、附录 C.10，与 L2 一致：暴露评价器源码使 Original 平均 +0.093、OOD 只 +0.009，CORAL-4 与 EvoTrias 在 OOD 上 −0.020；Circle Packing 影响 < 1%。

备注：暴露实验只在 Signal Processing 一个任务上，每格三次运行、表 3 不报 SD；暴露臂同时加入“鼓励读取源码”的提示，L2 已注“控制的是访问 + 鼓励读取协议”。

### 6. 2611.16378（退回，见 C-015-1）

## 排列与取舍

1. 全部 P3。q3 为 capability 的 15276 与 judgment 的其余各篇并列，不分先后。16378 因 C-015-1 暂停。
2. **与既有 51 张去重**：
   - **15268 vs 2610.31401（HERD）、2610.41216（TinyAstral）、2605.06614（SkillOS）**：HERD 与 TinyAstral 都把 harness 收益蒸进权重；SkillOS 训练写技能库的 curator。15268 独有的是“同一小模型自写规则 + 自训权重”的交叉检验，并给出相反方向的发现——RL 在规则就在上下文时**不会**把知识收进权重。保留。
   - **16591 vs 2611.08318（Criteria Exposure）、2610.35579（Infinity Machine）、2611.09348（Feedback Backdoor）**：三者都是单一自改闭环里评分信号被利用。16591 独有的是开放式“造系统”评测在执行层面的破口（提交物在评分时执行、跨阶段进程、可写日志、裁判解释劫持），以可执行攻击台账形式给出并配五道隔离措施。保留。
   - **15309 vs 2611.08318（Criteria Exposure）**：同为“学习器 / 提案者读到评分细节会使分数高估迁移”。08318 已用同批轨迹重判与换判据给出更直接的证据；15309 的暴露实验只有一个任务、三次运行且暴露与读取提示混在一起。**同题去重**，15309 的主体贡献（三权分立的演化系统、64% token 节省）不在本领域主问题上。
   - **15276 vs 2604.15719（Pre-Resolution Signals）、2610.29005（VeriEvolve）、2610.28798（Feedback Contract）**：同为“无外部标签时修订 harness / 评价器”族，既有三张已覆盖无标签修订与合成评价器的落差。15276 的独有点是“执行器与评价器在单题内同时演化 + 固定池隔离选择效用”，但评价器演化的消融差在一个 SD 内、且不跨任务保留。按上限让位。
   - **15700 vs 2610.37651（GEPA-Curator）、2610.37201（BiPA）**：同为“先归因再修补”。15700 的两范围充分性检验与“76% 缺失事实其实已在库里”有独立价值，但留出增量在噪声量级，改动由人提出。按上限让位，不凑满第三位。
3. **入选两篇**主族 F1 / F2，次族 F3 / F4，主卡不同（couple_context_and_weight_updates / diagnose_self_improvement）：一篇回答“改进应落在哪一层”，一篇回答“评测本身能不能被改进者绕过”，不重叠。没有改动任何记录字段。

## 入选（2）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2611.15268 | F1/F3 | couple_context_and_weight_updates | 无老师的小模型从自身日志同时改规则和权重时，两层各自贡献什么？ | 同一 12B 当代理 / 编辑器 / 受训者；规则编辑过三道检查、配对重测与噪声校准 V 门；最终两层 2×2 交叉 | 规则救从没解出的题（航空 27 vs 5，[8.3, 36.7]），权重稳住本来会的题（95 / 99 vs 87 / 93）；行李额等知识点只换权重几乎不动；单底座两域两轮、交叉非独立进化 |
| 2 | 2611.16591 | F2/F4 | diagnose_self_improvement | 代理端到端造 AI 系统时，评测能否挡住读答案、借资源、改日志与劫持裁判？ | 六任务对照人类系统；LLM 生成的攻击库在 Harbor、Harbor + 裁判、Breakwater 上实测 | 表 3 的 22 条攻击在 Harbor 全部得手，加裁判后 6 条仍得手，五道锁下全部拦下；成绩每格单次运行，同一代理换档位可跨过人类参考线 |

## Correction

**C-015-1 · 2611.16378（EGE）· 退回 Sol 单篇修订（保留原记录，不直接修改）**

- **原判**：`inc-l2-21` L2 记 q1_basis = `measured_own`、q2 = open_failure、q3 = judgment、q4 = fits，P3 / confirmed / to_l3；biggest_gap 写“Q1 取实测模拟而非升级成无条件安全 proof”。facts 第 2 条引 Monte Carlo：“某乐观偏差下 naive 为 2997/3000”。
- **问题 1（Q1 依据误记，影响档位）**：
  - §8 明说 Monte Carlo 是“synthetic by construction… tests a statistical failure mode under known data-generating assumptions… not evidence that EGE improves the behaviour of an implemented autonomous agent”（钉定文本 L2847 起），摘要也称“does not claim empirical validation on a real autonomous-agent system”（L46 附近）。
  - 2997/3000 来自作者**注入**的评价器乐观偏差 b = 0.25 对真实效应 −0.10 的设定；在该设定下朴素门接受有害候选是构造结果，不是对“候选依赖的评价器乐观偏差在代理系统里存在”的测量。错分布条件 3000/3000 同理。
  - 论文没有自己测量、也没有核对引用来源去证明这一偏差在真实代理更新中出现；相关工作段只引用了综述与 Lin et al.（更新生成 ≠ 更新受益），不是评价器偏差的测量。
  - 按 PROBLEM_CORE §3 Q1，问题存在的依据应为 `asserted`（或至多 `measured_cited_unchecked`），封顶规则使其最高 P2。定理只证明了所给下界在假设下的覆盖性，属于方法正确性，不是 Q1 的 `proof`。
- **问题 2（附带，供修订时判断）**：Q3 记 judgment，但作者给出的功效需要每次审计 5,000–80,000 级样本（§8.1、表 4），作者自己也说组合的都是熟知工具（Hoeffding、union bound、alpha spending），“改变只看单次正增益的更新实践”尚缺实际代理中的可行性证据；请复核 q3 是否应为 incremental。
- **请 Sol 处理**：复核 q1_basis 与 problem_tier（预期 P2），再按 PROBLEM_CORE §4 决定 evidence_status 与 next_action（P2 进 to_l3 需写编辑理由）；子卡 H31 各项的 holds 是否限定为“在假设下”。
- **处理**：本期暂停该篇，不制作 Reel。

## 待补与其他

- **待补清单（priority=high 但未确认）**：本期范围内 3 篇，均为 `inc-l2-21` 的 P3 / pending_experiment / park：
  - 2611.15178：自判准入后 72.7% 未救活，缺同协议下未见任务的单条与组合效用测试；补齐后决定技能准入能否作为因果认证。
  - 2611.17068：最终选型复用报告集、额外推理未配平，缺冻结后的新 split、等额思考控制与多搜索种子；补齐后决定证据保留 / 查询组合的设计判断。
  - 2611.15754：分类只基于训练频数与选择性翻转，缺留出全集盲标、独立优化种子；补齐后决定“准确率变好而编排故障不减”的协调归因。
  - 另有 2611.15481、2611.14949 为 P2 / pending_experiment / park，不入池。
  - 沿用上期待补：2611.14326、2611.11994、2611.10787、2611.10748，以及 2611.08946、2611.07051、2611.06972、2611.06321、2611.06049、2611.00463。本步均未处理。
- **退回项跟进**：新增 C-015-1（16378），待 Sol 修订。
- **漏检抽查**：本步未执行（沿用 progress.md 的欠账，滚存）。
- **下期备选**：
  - 2611.15276：如有跨任务保留、或评价器演化在更多运行下与冻结评价器拉开差距，可回看；
  - 2611.15700：如有重复标注 / 多次 campaign、或检索侧修复的端到端结果，可回看；
  - 2611.16378：视 C-015-1 的修订结果；
  - 沿用上期所列：2611.13336、2611.14320、2611.11558、2611.09291、2611.07372、2611.06768，以及 2609.33378、2611.03238、2610.21082、2611.02079。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2611.15268/`：poster.png（1600×2263）/ poster.pdf（单页 1200×1697pt）/ poster.html / SOURCE.md / QA.md
  - `reel/2611.16591/`：同上
- **版式**：遗传学实验记录本 + 2×2 杂交方格（15268）、金库安防检验报告（16591），与既有 51 张及彼此互不重复。构建脚本（生成内联 SVG）在本地 `/tmp/rv015/`（build_a.py、build_b.py、render.sh），poster.html 本身即完整可编辑源。
- **索引更新**：
  - `reel/README.md`：头段新增第十五期句，共 53 篇、53 种版式，加 selection 15 链接；表格顶部新增 2 行。
  - 仓库 `README.md`：只改头部统计、Featured Reel 段的篇数、selection 15 链接和画报墙。
