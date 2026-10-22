# HarnessRSI Daily

从每日论文中识别有具体方法和可信证据的研究，积累可复用的领域 pattern，挑出少数值得深入阅读的工作做成画报。

核心问题：**究竟改进了哪个非权重组件，如何接受并留存，之后的任务是否因此变好？** 收录边界见 [EVIDENCE](docs/EVIDENCE.md)。

> 2026-10-22：旧版评分与 Reel 已撤下（[重置核查](docs/RESET_2026-10-22.md)）；同日按 problem-core-v1.1 完成全量重评并发布本期 Reel 8 篇。

## 本期速览（2026-10-22）

**1597 篇全语料 L1 初筛 → 350 篇 L2 全文核对 → 8 篇 L3 终选 Reel**（[run 记录](research/scoring/runs/rsi-l1-20261022-03/progress.md)）

- L1：P3（好问题）×483、P2×451、范围外×600、待补材料×78
- L2：确认 P3 ×316，**228 篇 confirmed**；漏检抽查 31 篇改判 12 篇
- L3：Opus 5.5 精读 12 篇候选，终选 8 篇（宁缺毋滥），3 条 correction 退回 Sol 复核

## 精选画报（每张版式互不重复）

<table width="100%"><tr>
<td width="33%" align="center" valign="top"><img src="reel/2601.22436/poster.png" width="260" alt="Faithful Self-Evolvers poster"><br><b>Are Not Always Faithful Self-Evolvers</b><br>Self-evolving agents barely use their compressed experience<br>自演化代理的收益基本不依赖压缩经验（F1 证伪）<br><sub>深色证伪矩阵版式</sub></td>
<td width="33%" align="center" valign="top"><img src="reel/2603.28052/poster.png" width="260" alt="Meta-Harness poster"><br><b>Meta-Harness</b><br>Proposers need raw trajectories, not scalar scores<br>提议者能读原始轨迹才是关键（F1/F5）<br><sub>蓝图管线版式</sub></td>
<td width="33%" align="center" valign="top"><img src="reel/2602.05832/poster.png" width="260" alt="UI-Mem poster"><br><b>UI-Mem</b><br>Strong memory guidance collapses GRPO advantage signals<br>强记忆指导让组内学习信号消失（F2/F3）<br><sub>因果链+信号曲线版式</sub></td>
</tr><tr>
<td width="33%" align="center" valign="top"><img src="reel/2605.25815/poster.png" width="260" alt="EvoMap poster"><br><b>Behind EvoMap</b><br>Self-reported metadata does not certify shared skills<br>自报元数据担保不了共享技能质量（F2/F5）<br><sub>报纸三栏审计版式</sub></td>
<td width="33%" align="center" valign="top"><img src="reel/2603.19461/poster.png" width="260" alt="Hyperagents poster"><br><b>Hyperagents</b><br>An editable meta-agent vs a fixed one<br>可编辑 meta agent 对比固定版（F3/F1）<br><sub>浅色分屏时间线版式</sub></td>
<td width="33%" align="center" valign="top"><img src="reel/2602.15654/poster.png" width="260" alt="Zombie Agents poster"><br><b>Zombie Agents</b><br>One injection persists across sessions via memory<br>一次注入跨会话持续控制代理（F4/F2）<br><sub>警示攻击链版式</sub></td>
</tr><tr>
<td width="33%" align="center" valign="top"><img src="reel/2604.15719/poster.png" width="260" alt="Pre-Resolution Signals poster"><br><b>Pre-Resolution Signals</b><br>Revisiting open questions before labels arrive<br>结果揭晓前重访同一问题修订 harness（F4/F2）<br><sub>信号时序图版式</sub></td>
<td width="33%" align="center" valign="top"><img src="reel/2604.04247/poster.png" width="260" alt="Combee poster"><br><b>Combee</b><br>Parallel prompt learning buys speed, not quality<br>并行学提示的质量崩塌边界（F0/F5）<br><sub>规模-质量曲线版式</sub></td>
<td width="33%"></td>
</tr></table>

每张目录含 `poster.png / poster.pdf / poster.html（可编辑源）/ SOURCE.md（逐数溯源）/ QA.md（视觉验收）`，入口 [reel/](reel/README.md)。

## 高分论文（confirmed P3，经 Opus 原文核对）

| Paper | Code | Idea Cards | 提出的好问题 |
|---|---|---|---|
| [Are Not Always Faithful Self-Evolvers](https://arxiv.org/abs/2601.22436) | [GitHub](https://github.com/Dreamcatcher0622/Faithfulness) | `diagnose_self_improvement` · `index_experience_for_reuse` | 冻结骨干的自演化收益是否真依赖所留存经验的语义？七类内容干预证伪「记忆有效即在用记忆」 |
| [Meta-Harness](https://arxiv.org/abs/2603.28052) | [GitHub](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) | `attribute_and_patch_incumbent` · `make_the_improver_editable` | harness 搜索后果延迟多步——提议者需按需读原始轨迹，压缩摘要不够 |
| [UI-Mem](https://arxiv.org/abs/2602.05832) | — | `couple_context_and_weight_updates` · `abstract_experience_into_guidance` | 在线 GRPO 中每条 rollout 都获强记忆指导会让组内优势信号消失 |
| [Behind EvoMap](https://arxiv.org/abs/2605.25815) | — | `diagnose_self_improvement` · `evidence_gated_retention` | 共享技能网络的发布奖励与自报日志，实测担保不了资产质量（84%＝66% 无验证＋18% 平凡验证） |
| [Hyperagents](https://arxiv.org/abs/2603.19461) | [GitHub](https://github.com/facebookresearch/Hyperagents) | `make_the_improver_editable` | 「任务求解提升＝自修改能力提升」在非代码领域不成立——把 meta agent 做成可编辑对象 |
| [Zombie Agents](https://arxiv.org/abs/2602.15654) | — | `diagnose_self_improvement` · `index_experience_for_reuse` | 只读网页经正常记忆写入后，一次间接注入能否跨会话持续控制代理（77%→3–15%） |
| [Pre-Resolution Signals](https://arxiv.org/abs/2604.15719) | — | `abstract_experience_into_guidance` · `evidence_gated_retention` | 未来预测题结果揭晓前无标签——用多次重访的信号修订持久 harness |
| [Combee](https://arxiv.org/abs/2604.04247) | — | `abstract_experience_into_guidance` | 大量并行轨迹学提示时单次聚合过多反思导致质量崩塌；收益主要是速度 |

全部 confirmed P3 候选池（228 篇）：[l3-candidates.tsv](research/scoring/runs/rsi-l1-20261022-03/l3-candidates.tsv)；选题全程见 [selection.md](research/scoring/runs/rsi-l1-20261022-03/selection.md)。

## 流程与模型

```
Grok 收集候选 ──▶ 6.1 Sol L1 初筛（摘要+引言，4 并发滚动）
                     │  问题档 P0–P3（5 个问题族 F1–F5/F0 ＋ Q1–Q4）
                     ▼
                 6.1 Sol L2 核对（全文＋子卡条件检查，预算＝L1 的 20% ＋ 10% 漏检抽查）
                     │  确认 Q1/Q4、升 P3、supersedes 链保留 L1 原判
                     ▼
                 Opus 5.5 L3 选题（精读候选原文，跨族去重，宁缺毋滥）
                     │  correction 退回 Sol 单篇修订
                     ▼
                 Opus 5.5 Reel 制作（风格各异、逐数溯源、实际视觉 QA）
```

- **评价体系**：[problem-core-v1.1](research/scoring/PROBLEM_CORE.md)——先问问题好不好（P0–P3），再看机制条件是否成立（子卡 6 值检查）；两层分开记录，不算总分。判据全部来自本项目领域卡。
- **打分模型**：6.1 Sol（CC 内置 Subagent，model type `sonnet` 映射，默认 4 并发、每批 20 篇起、滚动补位；不另起无头会话）。
- **选题/Reel 模型**：Opus 5.5（`fable`）只处理少量候选——L3 原文核对与画报制作，不参与全量评分。
- 缺材料记 `needs_material` 排队补齐，不冒充低分；结构校验通过≠科学结论成立。

## 领域 Pattern 卡（评分判据的全部来源）

13 张主卡（`patterns/main/`）＋ 36 张子卡（`patterns/sub/` H00–H35）＋ 反模式（[anti-patterns](patterns/anti-patterns.md)）。评分依据是这些卡的**机制、适用条件、失败模式和有来源的审稿期望**，不是关键词匹配。

| 主卡 | 一句话机制 |
|---|---|
| `abstract_experience_into_guidance` | 把任务结果反思成可复用文字指导，留存并注入后续任务 |
| `amortize_improver_into_trained_policy` | 按改进器引起的下游改进给它记功，再训练改进器本身 |
| `attribute_and_patch_incumbent` | 归因失败到组件，局部修补后在不相交划分上复验替换 |
| `coevolve_the_evaluator` | 暴露评估器盲点、修订标准、对照可信锚点后再当奖励/门 |
| `couple_context_and_weight_updates` | 上下文经验与权重更新成对评估，有用≠干净训练信号 |
| `crystallize_executable_capability` | 解法固化为参数化代码并注册进动作空间，未见输入上验证 |
| `diagnose_self_improvement` | 命名上涨曲线背后的混淆，构造能杀死它的对照条件 |
| `evidence_gated_retention` | 按测得的边际效果决定收录、降级或回滚，保留出处 |
| `index_experience_for_reuse` | 结构化经验库＋按需检索先例，检索信号要有区分力 |
| `make_the_improver_editable` | 改进器本身作为修改对象，评估后代、保留现任、递归 |
| `population_search_executable_fitness` | 种群＋可执行适应度搜索，分数要在未见数据上确认 |
| `search_agent_architecture` | 声明模块/拓扑/工作流设计空间，搜索并留存赢家结构 |
| `self_generate_the_curriculum` | 自生成任务须独立验证可解性与难度，自生成≠自认证 |

索引与操作签名见 [PATTERN_INDEX](research/scoring/PATTERN_INDEX.md) · 问题族映射见 [PROBLEM_MAP](research/scoring/PROBLEM_MAP.md)。

## 使用入口

| 内容 | 入口 |
|---|---|
| 领域模式卡 | [patterns/overview](patterns/overview.md) |
| 评价规则 | [问题核心](research/scoring/PROBLEM_CORE.md) · [本领域配置](research/scoring/PROFILE.md) |
| CC 执行 | [启动提示词](docs/agents/START_CC.md) · [完整批量提示词](research/scoring/SOL_BATCH_PROMPT.md) |
| 精选 Reel | [选题](research/scoring/SELECTION.md) · [Opus 制作](research/scoring/OPUS_REEL_PROMPT.md) · [成品](reel/README.md) |
| 候选收集 | [Grok 提示词](docs/agents/GROK_PROMPT.md) · [inbox](inbox/README.md) |

维护说明：[PIPELINE](docs/PIPELINE.md) · [MAINTAINING](docs/MAINTAINING.md)。`make check` 只验证本地结构，不代表科学结论正确。

## Credits and license

MIT (see [LICENSE](LICENSE)), inherited from [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest).
Corpus seed lists: lobehub/awesome-rsi, ANative-Lab/Awesome-Self-Evolving-Agents, XMUDeepLIT/Awesome-Self-Evolving-Agents,
selfimproving-agent/Awesome-Self-Improving-Agents, wkqdzkd/Awesome-Reliable-Self-Evolving-Agents,
EvoMap/awesome-agent-evolution, iSEngLab/Awesome-Self-Evolving-Coding-Agents. Outcome labels from OpenReview.
