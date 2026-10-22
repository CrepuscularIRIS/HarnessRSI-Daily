# 问题族映射：HarnessRSI Daily

配合 [PROBLEM_CORE.md](PROBLEM_CORE.md) 使用，版本 `problem-core-v1`，初版映射，尚未试点。依据为各主卡“Cognitive barriers”与“Failure modes”两节。本表只用于检索和归组；判断 Q2、Q3 时必须引用卡片原文，不能只引本表。

| 主卡 | 问题族 | 卡片中的锚点要点 |
|---|---|---|
| [abstract_experience_into_guidance](../../patterns/main/abstract_experience_into_guidance.md) | F1、F2、F5 | 上下文文本算学习需与额外算力区分；看似合理的教训取决于结果信号；经验越多越好不成立 |
| [amortize_improver_into_trained_policy](../../patterns/main/amortize_improver_into_trained_policy.md) | F1、F3 | 改进器的奖励应是它引起的改进而非刚碰过任务的分数；不存在单一全局最优产物 |
| [attribute_and_patch_incumbent](../../patterns/main/attribute_and_patch_incumbent.md) | F1、F5 | 失败可能是执行失误而非产物错误；反馈传得越远不一定越好 |
| [coevolve_the_evaluator](../../patterns/main/coevolve_the_evaluator.md) | F2、F4 | 可信信号重复使用会变成训练信号；judge 评已见过的候选有偏，靠隔离而非强度 |
| [couple_context_and_weight_updates](../../patterns/main/couple_context_and_weight_updates.md) | F1、F2 | 在上下文中有用的经验不自动是干净的训练信号；接口与执行器需成对评估 |
| [crystallize_executable_capability](../../patterns/main/crystallize_executable_capability.md) | F1、F3、F5 | 成功一次不等于能力，须在未见输入上验证；库越大不一定越好；需与强骨干区分 |
| [diagnose_self_improvement](../../patterns/main/diagnose_self_improvement.md) | F1 | 演化分数上升不等于真实自我改进；记忆的格式和提示效应可能承载收益 |
| [evidence_gated_retention](../../patterns/main/evidence_gated_retention.md) | F1、F5 | 留存越多或开发集分越高不等于改进；共同检索时结果信号无法归到单个条目 |
| [index_experience_for_reuse](../../patterns/main/index_experience_for_reuse.md) | F2、F5 | 更多历史不自动有益；按需检索取决于触发信号的区分力 |
| [make_the_improver_editable](../../patterns/main/make_the_improver_editable.md) | F1、F4 | 固定子集反复评估导致过拟合；锚点泄漏（调用更强模型、共享盲点的 judge）使归因失效 |
| [population_search_executable_fitness](../../patterns/main/population_search_executable_fitness.md) | F2、F3 | 评估器分数在搜索未见数据上确认前只是选择压力 |
| [search_agent_architecture](../../patterns/main/search_agent_architecture.md) | F2、F5 | 编辑模型自身的判断不一定指向改进；更大的设计空间本身不是贡献 |
| [self_generate_the_curriculum](../../patterns/main/self_generate_the_curriculum.md) | F2 | 自生成不等于自认证；只奖励难度会偏向含糊或错误任务 |

另见 [anti-patterns](../../patterns/anti-patterns.md)：AP1、AP2 和 H00 观察项都是 Q2 `vertical_port` 的典型来源。
