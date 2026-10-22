# HarnessRSI Daily

从论文中识别具体的研究方法和可信证据，积累可复用的领域 pattern，挑出少数值得深入阅读的工作。

核心问题：**究竟改进了哪个非权重组件，如何接受并留存，之后的任务是否因此变好？** 收录边界见 [EVIDENCE](docs/EVIDENCE.md)。

> 2026-10-22：旧版评分与 Reel 已撤下（[重置核查](docs/RESET_2026-10-22.md)）；同日按 problem-core-v1.1 完成全量重评（1597 篇，run [rsi-l1-20261022-03](research/scoring/runs/rsi-l1-20261022-03/progress.md)），并发布本期 Reel 8 篇（见下方精选）。

## 2026 精选（confirmed P3，经 Opus 原文核对）

问题优先两层评价：好问题（P3=成立且开放、解决后改变能力或判断）＋子卡条件核对。下表为本期 Reel 终选 8 篇；全部 confirmed P3 候选池（228 篇）见 [l3-candidates.tsv](research/scoring/runs/rsi-l1-20261022-03/l3-candidates.tsv)。

| 论文 | 好问题 | 命中领域卡 | 画报 |
|---|---|---|---|
| [Are Not Always Faithful Self-Evolvers](https://arxiv.org/abs/2601.22436) · [code](https://github.com/Dreamcatcher0622/Faithfulness) | 冻结骨干的自演化代理收益是否真的依赖所留存经验的语义内容？七类内容干预证伪「记忆有效即在用记忆」 | `diagnose_self_improvement` · `index_experience_for_reuse` | [Reel](reel/2601.22436/) |
| [Meta-Harness](https://arxiv.org/abs/2603.28052) · [code](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact) | harness 搜索的后果延迟多步出现——提议者需要按需读原始轨迹，而非只看标量分数或压缩摘要 | `attribute_and_patch_incumbent` · `make_the_improver_editable` | [Reel](reel/2603.28052/) |
| [UI-Mem](https://arxiv.org/abs/2602.05832) | 移动 GUI 在线 GRPO 中，每条 rollout 都获强记忆指导会让组内优势信号消失；经验要随策略更新 | `couple_context_and_weight_updates` · `abstract_experience_into_guidance` | [Reel](reel/2602.05832/) |
| [Behind EvoMap](https://arxiv.org/abs/2605.25815) | 共享自演化技能网络的发布奖励与自报验证日志，实测担保不了被复用资产的质量（84% 拆解为 66% 无验证＋18% 平凡验证） | `diagnose_self_improvement` · `evidence_gated_retention` | [Reel](reel/2605.25815/) |
| [Hyperagents](https://arxiv.org/abs/2603.19461) · [code](https://github.com/facebookresearch/Hyperagents) | 「任务求解提升＝自修改能力提升」在非代码领域不成立——把 meta agent 本身做成可编辑对象 | `make_the_improver_editable` | [Reel](reel/2603.19461/) |
| [Zombie Agents](https://arxiv.org/abs/2602.15654) | 只读网页经正常记忆更新写入长期记忆后，一次间接注入能否在无关后续会话持续控制代理（77%→3–15%） | `diagnose_self_improvement` · `index_experience_for_reuse` | [Reel](reel/2602.15654/) |
| [Pre-Resolution Signals](https://arxiv.org/abs/2604.15719) | 未来预测题在结果揭晓前没有标签——用对同一未决问题多次重访的信号修订持久 harness | `abstract_experience_into_guidance` · `evidence_gated_retention` | [Reel](reel/2604.15719/) |
| [Combee](https://arxiv.org/abs/2604.04247) | 大量并行轨迹学提示时，单次聚合过多反思导致上下文过载与质量崩塌；收益主要是速度 | `abstract_experience_into_guidance` | [Reel](reel/2604.04247/) |

## 使用流程

Grok 收集候选 → 6.1 Sol 按已有领域 pattern 批量评分 → 少量候选 → Opus 5.5 核对原文并制作 Reel。

| 内容 | 入口 |
|---|---|
| 领域模式卡 | [patterns/overview](patterns/overview.md)；评分依据是这些卡的机制、条件、失败模式和审稿期望 |
| 新版评分 | [规则](research/scoring/SCORE_SPEC.md) · [本领域配置](research/scoring/PROFILE.md) |
| CC 执行 | [启动提示词](docs/agents/START_CC.md) · [完整批量提示词](research/scoring/SOL_BATCH_PROMPT.md) |
| 精选 Reel | [选题](research/scoring/SELECTION.md) · [Opus 制作](research/scoring/OPUS_REEL_PROMPT.md) · [成品入口](reel/README.md) |
| 候选收集 | [Grok 提示词](docs/agents/GROK_PROMPT.md) · [inbox](inbox/README.md) |

默认 CC 内置 4 个评分 Subagent 并行，model type 使用已配置的 6.1 Sol，每批通常 10–20 篇，完成一批立即补派；不另起无头 Claude。Opus 只负责少量候选核对与 Reel。

评分顺序是论文操作 → 相关领域卡 → 适用判据 → 论文证据 → 得分。G/M/X/E 只汇总这些判断。原 ResearchStudio 15＋31 保留为方法来源，不是逐篇评分 taxonomy；匹配卡数、录用率、代码链接和名气不加分。

初步材料足够即可简评，缺材料不冒充低分。通常每期不到 10 篇 Reel；先核对、后制作，不把全部论文做成海报墙。

维护说明：[PIPELINE](docs/PIPELINE.md) · [MAINTAINING](docs/MAINTAINING.md)。`make check` 只验证本地结构，不代表科学结论正确。

## Credits and license

MIT (see [LICENSE](LICENSE)), inherited from [yang3kc/daily_arxiv_digest](https://github.com/yang3kc/daily_arxiv_digest).
Corpus seed lists: lobehub/awesome-rsi, ANative-Lab/Awesome-Self-Evolving-Agents, XMUDeepLIT/Awesome-Self-Evolving-Agents,
selfimproving-agent/Awesome-Self-Improving-Agents, wkqdzkd/Awesome-Reliable-Self-Evolving-Agents,
EvoMap/awesome-agent-evolution, iSEngLab/Awesome-Self-Evolving-Coding-Agents. Outcome labels from OpenReview.
