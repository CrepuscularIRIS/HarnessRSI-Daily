# rsi-v3.1 — HarnessRSI Daily

> 自 `problem-core-v1.1` 起，下文的四轴权重与轴表停用。本文件仍提供：收录范围（`out_of_scope` 判断）、领域核心问题、证据等级和优先查阅的卡片。

权重：G=15、M=20、X=20、E=45。正式范围以仓库 `docs/EVIDENCE.md` 为准。

核心问题：**改了哪个非权重组件，如何决定接受并留存，后续任务是否因这个改动变好？**

收录基于反馈改变并留存 prompt、skill、tool、workflow、memory/playbook、agent 代码、评测器或配置的闭环，以及直接用于该闭环的组件和评测。纯权重更新、单次答案修改、无留存变化的通用 agent 不因名字含 self-improvement 而收录。

| 轴 | 本领域的具体判断 |
|---|---|
| G | 现有非权重组件存在什么瓶颈？“模型冻结也能进步”只是背景，不足以成为具体 gap。 |
| M | 反馈如何变成候选修改，为什么这项修改对准问题？区分改执行器、记忆检索器与 improver。 |
| X | 修改→选择/拒绝→保存→后续读取的流程是否清楚？按主张检查门控、回退、冲突或过期条件。 |
| E | 是否支持留存收益，而非只在挑选候选的样本上变好？优先看 store-off/gate-off、相同模型/预算、后续任务、失败和搜索成本。 |

按论文主张只选最相关的 1–2 个问题，不把上表变成每篇几十项检查。B 类组件按组件贡献评价，不强求其自身构成完整闭环。

证据等级沿用 task / retained / improver，材料不够则 unknown。只在选择集上变好不能判 retained；架构里写了递归不等于证明 improver。等级单列，不加分。

可按机制优先查这些现有领域卡（不是所有论文必读清单）：

- `patterns/main/abstract_experience_into_guidance.md`：从经验抽取可复用指导。
- `patterns/main/evidence_gated_retention.md`：依据效果决定收录、降级或回滚。
- `patterns/main/diagnose_self_improvement.md`：隔离“自我改进”测量里的混淆。
- `patterns/main/make_the_improver_editable.md`：改进器本身作为修改对象。

新评分不继承模式卡内的录用率、旧 score、旧 VERIFIED 或历史是否入选 Reel。直接使用本项目领域主卡/子卡及其条件，不加载原 15＋31 分类。
