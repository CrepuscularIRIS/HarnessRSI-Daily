# SOURCE — 2611.14505 · 考勤工时卡

- 论文：Continual-ARC: Measuring Skill Acquisition over a Working Lifetime（Daniel Lenton，unify）
- 版本：arXiv:2611.14505**v1**（cs.LG，2026-11-10）；corpus 中无更新版本
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.14505.txt`（arxiv.org/html/2611.14505v1，sha256 `70adf820…`，与 run `materials/2611.14505.json` 的 pin 一致，complete: true）。正文 §1–§6、附录 A–F、H **通读**；附录 G（相关工作扩展表）、I–L 浏览。
- 初筛记录：L1 `batches/inc-l1-18.jsonl` → L2 `batches/inc-l2-20.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-014.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 收窄：确认“新实例复发＋清空孪生”能揭示笔记、缓存、程序与权重的差别；不把“没测到迁移”写成零泛化定理，不普遍判权重胜过 harness。

## 断言 / 数字 → 原文（行号指钉定文本，约数）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 标题 / 副标题 / 卡号栏 | 25 任务、200 实例、每任务 8 次、seed 0；演示 / 错答各计 1、失败 16；两张冻结考卷 | 摘要；§2.1 L152 起；§2.2 L468–474；§2.3 |
| 打卡条 | 任务成段出现、休眠后返回 | 图 2 / 附录 B 的流程。**示意重绘，不是真实排程** |
| 孪生与 S 定义 | reset、L、S_seen、S_held | §2.4 L527 起 |
| 区间图 | 9 行 S_seen / S_held 点与 95% 区间 | 表 1 L904 起；GLM 原样三次合计 0.25 [0.17, 0.33] 见 §4 L1082 段 |
| 结果框（左） | QC 0.37；Q、G 未超地板；DAgger 0.29 [0.23, 0.35]；库上限 131 原语 S_held −0.06 [−0.17, 0.04] | §4 Baselines L1035、Harnesses as shipped L1082、Generalization L1192；附录 F 库上限 L3007–3011 |
| 结果框（右） | GE 0.74；GPT-6 Luna H-E 0.62–0.72；prime-agent 600 会话未写全局存储；openclaw 未升格；不保留已买演示 | §4 Expert guidance L1174；附录 E.1、E.4、E.5 |
| 卡在哪 | 106 条记忆、6 条摘要、154/175、43 次主动搜读、40/154；0.88 / 10.6% / 40；2.11 / 23.7% / 108；G₀ 2.29 / 24.7% | §4 L1142；附录 E.2 L2773 起 |
| 证据边界 | seed 0；区间为任务重抽；放弃 48–68%；Q₀ 18/100 vs 31；DAgger 47–52；老师读指引、反馈不计费；23 个 held-out 用于配置搜索、剔除后 0.27 [0.20, 0.34]；公开题；openclaw 嵌入不可达 | 附录 A Intervals L1709；附录 D.3 Readable replies L2673–2675；§4 L1216–1224；§3 L955；附录 H L4769、L4791–4793；附录 A L1549；附录 D.2 |
| 完整性记录 | 5,302 个计划外请求、20 个成功、一局索要演示、发布版已封堵 | 附录 D.2 Isolation L2585 |
| 本项目阅读 | 三个具体条件；评测含义 | **本项目阅读判断**；“无共享原语”依据附录 A“Why the held-out test can show transfer”与附录 F GB |

## 复核

- 40＋114 = 154；40/40、108/114 解出；154 ≤ 175 次返回。
- 表 1 中 G 行 S_seen +0.12 [−0.03, 0.27] 与正文“三次运行 0.25 [0.17, 0.33]”并存：画报两者都写明。
- L2 facts（seen 100 新实例 / 100 未见任务、四次重玩、主结果 seed 0；规则常未送达；expert program 改善 seen 但无跨任务泛化）与原文一致。
