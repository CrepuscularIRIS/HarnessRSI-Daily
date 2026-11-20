# selection-019 — 2026-11-20（执行模型 glm-5.3）

Run: [rsi-rolling-20261023-01](progress.md) · 选题规则：[SELECTION](../../SELECTION.md) · 制作规范：[OPUS_REEL_PROMPT](../../OPUS_REEL_PROMPT.md)

候选池 12 篇（P3/confirmed/to_l3，7 天窗口内未发布）。逐篇读全文缓存（batches/inc-l2-*.jsonl 最新 L2 记录）核对，**12 篇 L2 判断全部一致，correction 0 条**。深读 2611.15276、2611.15700、2605.13357 三篇，其余九篇摘要+数字抽查。

## 入选 3 篇（发布 3、fail 0、重做 0）

### 2611.15276 — Verify by Doing（F2/F4，capability）
无外部反馈下 Actor/Evaluator 双 harness 共演化；Evaluator 主动调工具核验工件（active verification），发现才写入偏好信号，两 harness 同轮更新；对比评审（同候选成对比较）+ Actor 需自身新输出支持。
- 入选理由：本期机制最完整的一篇——除主实验（AutomationBench 600 任务 37.0±1.9 vs RQGM 33.7）外，**固定 BoN 候选池只换 Evaluator（pass +4.6pp）与回归拒绝 89.3% vs 71.2% 两组消融**把"选好已有输出"与"写出更好输出"两个收益来源干净分离；消融 w/o active verification −2.7、w/o Evaluator evolution −1.6 各自归因到位。
- 差异化：现有 64 张中无"双 harness 同步演化 + Evaluator 主动工具核验"组合；与 SIM/ModHarness 类自改进记忆不同，本文 harness 任务结束清空，是 within-task 共演化而非跨任务留存。
- 限制（海报已列）：Actor/Evaluator/reviewer 同骨干共享错误、harness 任务结束清空、离线评分用 GPT-5.6-sol。

### 2611.15700 — AskALCF 归因审计（F1/F2，judgment）
HPC 用户支持 agent 的 2174 生产 turns 归因路由审计：unattributable 900 (41.4%)→309 (14.2%)，机制是 729 turns 原本连 retrieval verdict 都没有（684 落 unknown），修复后去向 no_failure 198/knowledge 150/retrieval 147/prompt 75；同 turns 前后对照。16 harness arms（3 接受/9 拒/4 参照含 null）；**null 对照：中性编辑也改 9/11 of 171 routes（绕缓存）**，作为噪声地板而非改进证据。
- 入选理由：与已发布 2611.17939 的差异化明确——17939 是 benchmark 分数漂移审计，本文是**生产系统归因管线**的受控改进（同 turns 前后对照 + 16 臂门槛 + null 噪声地板），"unattributable 本身是缺失 harness 信号"与 PROBLEM_CORE F1 直接对齐；rule tree vs agent judge 分歧 354/2169 的流向分析（judge 少归 model、少留 unknown）是少见的裁判间证据。
- 限制（海报已列）：accuracy 仅建立在 150 expert turns 上、分层抽样非均匀、2024 turns 无 reference、修复注入绕过 retrieval 属上界口径、单专家多标签。

### 2605.13357 — AI Harness Engineering（F1/F4，judgment）
立场+框架文：把 harness 本身当研究对象——11 项组件职责（任务规范/上下文选择/工具访问/项目记忆/任务状态/可观测性/失败归因/验证/权限/熵审计/干预记录）×运行时契约×缺位失败模式；H0–H3 四级受控阶梯固定任务/仓库/模型逐级暴露运行时支撑；5 类结局把 unverified_success（"patch 对但没证据"）从 success 里分离；M-HIR 把人工干预转为缺失 harness 信号。
- 入选理由：现有 61 张覆盖了各式 harness 改进，但无一张把 **harness 本身作为可枚举、可消融的研究对象**形式化；11 职责表与本 repo 的 pattern/sub-card 体系直接同构，H0–H3 阶梯给了"分离 harness 贡献与模型贡献"的可操作协议。作为框架入选、不作为实证结果入选。
- 风险控制：原文缓存为节选本（research/fulltext/2605.13357.txt 多处 [...] 截断），海报无数值、以框架为主体，H1–H2 定义截断处海报与 SOURCE.md 均如实标注"缓存截断，定义未列"；限制条明示"立场/框架文，仅一个受控验证任务"。

## 落选 9 篇

| pid | 名称 | 理由 |
|---|---|---|
| 2606.09461 | H2HMem | 自改进记忆主题 ready 已多张（SIM/ModHarness/UI-Mem/Teaching the Harness 等），本文差异化不足；跨模态失败归因（模态错位 44–46%）是相关性分析非受控归因；LLM 生成数据限制重（selection-017 已记） |
| 2606.18829 | GateMem | 同上自改进记忆重复压力；缓存仅 15k 字符摘要级、缺主实验表，SOURCE 无法逐数溯源（selection-017 已记） |
| 2611.19037 | Critic Can Hurt | 与已发布 2611.09348（反馈后门）同为反馈通道失真机制，连续两期落选维持；8B 小模型 critic 的四臂审计外推到强模型存疑 |
| 2504.00406 | VerifiAgent | 与已发布 2611.16591（评分室隔离）重叠度高，均以"先隔离再核验"防评价被劫持；元验证+按推理类型选工具的增量在同主题下不构成新机制面 |
| 2601.07348 | CSE | held-out 算子分离与方差报告缺失（selection-017 已记）；#Imp 1.79 vs 0.90 的增益无法与评估泄漏区分 |
| 2601.09465 | EvoFSM | 与已发布 2603.28052（Meta-Harness）宏微双层演化机制相邻；FSM 显式化是增量 |
| 2611.18883 | Splice | 单域（NLO）单优化器；冻结/可编辑臂的 bound 依赖 γ 假设，proxy 49.3% vs 58.9% 有趣但覆盖面窄 |
| 2611.19537 | Craftax goal compiler | 单 game 增量证据薄（selection-018 已记）；"部署时零 LLM 调用"角度被单适应性历史 feedback/ancestry 混杂稀释 |
| 2611.20856 | Synapse | 与已发布 2611.01834 机制相邻；37 patch 全写回、receipt 回归发现但 patch 仍被接受——发现回归≠禁止回归，证据弱一档且无同数随机对照 |

## 版式

三张各异，且不与近三期（016/017/018）雷同：
- 2611.15276：上下双层宽幅 1760×1540（上层深色机制带四节点共演化循环，下层三栏数据）。
- 2611.15700：竖版纸面瀑布对照 1240×1840（前后双柱+去向五格+16 臂横条+阶梯+分歧流+null 虚线框）。
- 2605.13357：深底蓝图矩阵 1720×1620（11 行职责×契约×失败模式矩阵+H0–H3 阶梯+5 结局格+五原则 pill）。

## 账目

- 候选 12 · 入选 3 · 发布 3 · fail 0 · 重做 0 · correction 0
- QA：三张均首版通过（几何审计零违规、字体加载 true、12 横带墨量非空、目测核对通过；详见各 QA.md）。
- ready 总数：61 → **64**（reel/README.md 与根 README.md 已同步）。
