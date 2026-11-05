# SOURCE — 2611.05445 · 可执行工具库蓝图（LIBRA）

- 论文：LIBRA: Programmatic Induction of Executable Tool Libraries（Zekai Li, Zhenke Liu, Yonghao Li, Junhan Liu, Xulong Xiao, Jiapeng Zhang；布朗大学 / 南加州大学）
- 版本：arXiv:2611.05445**v1**（cs.SE，2026-11-03）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.05445.txt`（arxiv.org/html/2611.05445v1，sha256 `4deab8f2…`，与 `research/scoring/runs/rsi-rolling-20261023-01/materials/2611.05445.json` 的 pin 一致，complete: true）。正文 §1–§7 与附录 B（执行过滤消融）、C（构库统计）、D（数据处理与基线改编）、E（检索敏感性）、F（实现）、G（迭代曲线文字）、H（算法 1–2）**通读**；附录 A 提示词浏览（契约规则逐条读）。
- 初筛记录：L1 `batches/inc-l1-13.jsonl` → L2 `batches/inc-l2-15.jsonl`（P3 / confirmed / capability / to_l3）；L3 `selection-010.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认范围：冷启动可执行工具目录的前置工具检索。不把 Recall 增益写成任务成功；不把“运行时验证”写成依赖真值或普适精度；TGR-Adapt 不是原始 TGR 复现。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 标题 / 图 1 例 | “Find Alice in my contact and I will make the transfer”；Search_users → Login | 图 1 说明 L337–344 |
| 副标题 | 独立排名漏前置；构库在请求前；有它成换掉败 | 摘要 L99–109；§1 L146–150、L258–261 |
| 规格栏 | 不需标注 / 轨迹 / 训练；1 + 至多 2 次 LLM 调用；DeepSeek-V4-Flash；Qwen3-Embedding-0.6B、仅原始元数据、无重排；指标 | §3.1 L594–595；§4.1 L1093、L1174–1197；§3 L519、L723 |
| A 排名尺 | update_alarm #1 / login #28；tail #3 / touch #16；GetNPR2 #1 / SELFIEStoSMILES #169；均被提入前 K | 图 3 说明 L1305；§5.1 L1349–1376。**刻度尺为本项目示意重绘** |
| A 文字 | 请求不写前置步骤；嵌入不必相似 | §1 L148；§5.1 L1377–1379 |
| B 契约与测试 | 契约内容；同一保存状态替换为独立值或省略；状态依赖前后对照；兼容边需字段语义对齐；card / trans_id 反例 | §3.1 L534–676；算法 1（L8581–9255）；图 1 L331–335。**示意图为本项目重绘** |
| C 公式与剪枝 | 前 15 种子、一跳、每输入至多两个提供者、平均传播 | §3.2 L723–1043；表 6 默认 Ks = 15 |
| C 注 | 全部提供者时 SciToolEval 76.4 vs 91.1；两跳 −2.3 | 附录 E L8288–8315（表 6） |
| C 柱图 | QTS / Schema-Only / LIBRA 的 R 与 NDCG | 附录 B 表 4 L7722–7770 |
| C 注 | +12.0 / +7.0 / +4.6 | **本项目按表 4 相减** |
| D 表 | BM25、QTS、TGR-Adapt、Ego-Trip、SciToolKG、LIBRA 的 R / NDCG | 表 2（L741–857） |
| D 文字 | +7.9 / +3.7；ToolReAGt +4.5 / +2.9，3 LLM × 3 种子，8/9 最高 Recall | 摘要 L112–113；§4.2 L1218；§4.3 L1250–1284；图 2 说明 L1165 |
| D 漏检分解 | 860 / 224 / 85；各原因百分比 | 表 3 L1407（§5.2） |
| D 注 | search_contacts 需任务数据、建库跑不出 phone_number | §5.3 L1501–1516 |
| E 成本表 | 473 / 477 / 128；581,690 / 163,608 / 12,762；1,946/0、732/0、595/77；260:40、20:45、4:28 | 附录 C 表 5 L7831 |
| E 注 | 96 CPU worker、384 GB、L40S；线性 LLM 调用、最坏平方级；约 12.6 倍 | 附录 C L7791–7809；§3.1 L595 |
| F 限制 | 仅检索指标；无边级金标准；需可执行运行时；SciToolEval 270 / 530、AppWorld 90 + 57；TGR 改编；修订份数 218 / 48 / 37；精度不管覆盖 | §4 L1066；附录 C L7783、L7812–7821；附录 D L7893–7906、L8156；§7 L1595–1605 |
| 改变的判断 | 元数据推断不够、执行检验才有用 | 附录 B L7767–7770；表述为**本项目阅读判断** |

L2 facts 中可核对的数字（581,690 候选；260m40s、96 CPU、384 GB、L40S；270 / 530）与原文一致。
