# SOURCE — 2603.03329

- 论文：AutoHarness: improving LLM agents by automatically synthesizing a code harness（Lou, Lázaro-Gredilla, Dedieu, Wendelken, Lehrach, Murphy；Google DeepMind）
- 版本：arXiv:2603.03329**v1**（2026-02-10）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2603.03329.txt`（正文 §1–5 与附录 A–D 已通读；图 1–7 为图片，未从中取数）
- 初筛记录：L1 `batches/b036.jsonl` → L2 `batches/l2c13.jsonl`（P3 / confirmed / high / to_l3）；L3 `l3-final-2.tsv` #6、`selection-002.md` 阶段二（含 correction C4）
- run：rsi-l1-20261022-03（第二期）

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 刊头 | 145 个 TextArena 游戏（剔除 9 个自由文本游戏），新种子合法率 100% | 摘要、§4、§4.1 |
| 问题 | 非法动作；微调与手写 harness 的代价 | §1 |
| 78% 引文 | Kaggle GameArena 中 Gemini-2.5-Flash 败局 78% 归因于非法走子 | 摘要、§1（作者引用，本项目未核对） |
| 观测样例 | 删去 “Valid moves” 列表前后的 Chess-v0 观测 | 附录 A.4–A.5（原文节选，棋盘行有省略） |
| 合成阶段 | 树结构 + Thompson 采样，节点启发值 = 平均合法率、权重 1.0；10 个并行环境、每次至多 1000 步、自动重置；非法动作或代码出错即终止；至多 5 个失败步给 Critic；Refiner 改代码；合法率 1.0 或超时停止；Gemini-2.5-Flash | §3、§4.1 |
| 改哪个函数 | is_legal 返回 True 但动作非法 → 两个都改；返回 False 且非法 → 只改 propose_action | §3 |
| 部署形态 | action-verifier：LLM 提议 → is_legal_action 验证 → 不合法则带 “illegal action” 警告重新提示；同一 Flash 先合成再过滤（脚注 2） | §3、§4.2 |
| 三种形态 | action-filter / action-verifier（主体）/ harness-as-policy | §3 |
| 条码 | 145 个游戏的 “# Learning Steps” 与合法率（全为 1.0）；单人 44、双人 101；端到端 32 个用 * 标记 | 附录表 1 |
| 测试方式 | 每游戏 10 个随机种子 × 1000 步的新测试 rollout | §4.1 |
| 双人卡 | 16 个游戏 × 40 局、先后手各半；对 Pro 赢 9/16 个游戏，总胜率 56.3% 对 Pro 38.2%；对 Flash 赢 12/16，总胜率 64.8% | §4.2 |
| 单人卡 | 16 个游戏 × 20 局；平均奖励 0.745 / 0.707（Pro）/ 0.673（Flash）；高于 Pro 8/16，持平 5/16 | §4.2 |
| Policy 卡 | 0.870、GPT-5.2-High 0.844、Pro 0.707、GPT-5.2 0.635；胜 3、GPT-5.2-High 胜 5、平 8；最多 256 轮、平均 89.4 轮、启发值 0.939；GPT-5.2 各重复 10 / 5 次；约 $640 | §4.3 |

## 本项目计算

- 由附录表 1 解析 145 行：学习步数中位数 4、均值 10.3、最大 136（Breakthrough-v0-small）；1 步的游戏 36 个；32 个带 * 的游戏均值 14.5，其中 19 个 < 10。
- 双人对 Pro 的 “平 5.5%” = 100 − 56.3 − 38.2；单人 “低于 Pro 3 个” = 16 − 8 − 5。

## 示意与重绘

- 代码假设树中的版本号与合法率（.31、.58…1.0）、示意走法 [e2e4] / [e2e5] 均为示意。
- 条码由表 1 原值绘制（对数纵轴，1 步的条画成最小高度 4px，以便可见）。

## 核对说明 / 口径收窄

- **C4 已遵守**：0.745 / 0.707 / 0.673 只出现在“单人游戏”卡，双人卡只写 9/16、56.3%、12/16、64.8%。
- **平均 14.5 次迭代的分母**：selection-002 写“平均 14.5 次迭代”，未写分母。按表 1 计算，14.5 是 32 个端到端游戏的均值（原文同一句的 “19/32” 也说明了这一点）；145 个游戏的均值是 10.3。画报按此写明分母，只是收窄口径，不影响档位与入选，无需 correction。
- 表 1 列名为 “# Learning Steps”，表题写 “number of LLM calls needed”，正文用 “tree search iterations”；画报统一写“学习步数”。
- “无闸门的 Flash 是否也能非法即重问”原文未说明，画报作为边界列出。
