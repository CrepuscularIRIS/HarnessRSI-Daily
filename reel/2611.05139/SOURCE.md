# SOURCE — 2611.05139 · 局中改动进程单（Meta²）

- 论文：Meta²: Precomputing Reusable Knowledge for Online Harness Evolution in Long-Horizon Agents（Lingzhi Yuan, Yiguang Cai, Weize Liu, Siqi Yang, Feijiang Han, Yongkyun Lee, Udari Madhushani Sehwag, Furong Huang；马里兰大学 / UW / UIUC / Scale AI）
- 版本：arXiv:2611.05139**v1**（cs.AI，2026-11-03）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.05139.txt`（arxiv.org/html/2611.05139v1 转文本，sha256 `8696b7fe…`，与 `research/scoring/runs/rsi-rolling-20261023-01/materials/2611.05139.json` 的 pin 一致，complete: true）。正文 §1–§6 **全部通读**；附录 A（记号）、B（算法与检查点接口）、C（基准与基线设置）、D（案例图 5–8）、E（均值与标准差、成本前沿）、F（局限与讨论）、G（演化范式对比）、H（演化者与 REFLECT / AGGREGATE / UPDATE 提示词）通读；附录 I 的 Meta-Skill 条目全文浏览，细读 E-02 / E-03 / E-04 / E-06。
- 初筛记录：L1 `batches/inc-l1-12.jsonl` → L2 `batches/inc-l2-14.jsonl`（P3 / confirmed / capability / to_l3）；L3 `selection-009.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认的范围：离线特权对照学成的干预指南，在无判分器的局中部署时有限迁移（同基准随机留出），且局部改动不跨题保留更好。不展示为“单次编辑的因果效应”“特权信息无残留”或“跨基准 / 跨模型迁移”。本项目补充：消融第一级（加演化者）混入了工作代理脚手架差异，画报把“无指南演化者 → 对照式 Meta-Skill”标为最干净的一级。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首副标题 | 离线共享 harness 不能应变；在线演化缺判分器、从零推理；“上移一层” | Abstract（L66 起）；§1（L190–330，问题句 L213） |
| 信息屏 | 同一冻结模型做任务代理与演化者；1:2 随机划分；mean@5 / mean@3 | §4.1（L1198）；附录 C（L3252–3260、L3273） |
| BAY 1 三条件 | A 无演化者 / B 当前 Meta-Skill / C 特权验证信息 | §3.2（L960–990；A/B/C 段 L972 起） |
| BAY 1 五个方向 | informed / effective / harmful / overreach / unnecessary → act / avoid / hold | 附录 H REFLECT 提示（L4536–4610）；§3.2 |
| BAY 1 注 | AGGREGATE 需 ≥2 道训练题；C 禁止传递 + 事后审计剔除；对照只给方向 | 附录 B.1（L2739–2740）；§3.2（L987）；附录 C（L3402）；附录 F |
| BAY 2 进程单 | Rave 案例：无 Meta-Skill 在 t₃ 用最后一次 notice 改道 → Aeka–Rave 混合体 74 胜 / 需 75；有 Meta-Skill 依 E-06 保持 → 五项阈值全达到 | 附录 D 图 7（L3505–3515）；E-06 条目（L5560 起）。**检查点位置为本项目示意重绘，非实测** |
| BAY 2 保持 / 改动 | 第一步后、每 5 步、提交前；改动只作用本局剩余部分、结束即丢弃；Meta-Skill 部署中不更新 | §3.1；§3.3；附录 C（L3424） |
| BAY 2 通道 | notice（工作中至多 2 次）、常驻指令、check / probe、工具、技能、中间件、回滚、退回重做 | 附录 H 演化者系统提示（L4352 起，限额 L4426–4428） |
| BAY 3 结果图 | 12 行中选 9 行：TB 2.1 / DeepSWE 均值 ± 标准差 | 表 1（L1340–1600）；附录 E 标准差表（L3556 起） |
| BAY 3 注 | DeepSWE 上 ACE、CH 低于种子、AHE 持平；Pi agent 39.11；DeepSeek 底座 70.00 → 77.67、CH 74.67；各自重建 Meta-Skill | §4.2（L1309–1330）；表 2 |
| 逐件加上去 | 66.33/34.67 → 74.67/36.44 → 77.00/35.56 → 81.00/44.44；跨题保留 78.33/39.11 | §4.5 图 4 文本（L1809–1823） |
| 逐件注 | +6.33 / +8.00 | **本项目按 §4.5 数字相减** |
| 逐件注 · 脚手架 | A 设置的工作代理提示不同、无 check / probe 中间件、不分段；分段影响未测 | 附录 H REFLECT 提示（L4564–4566） |
| 账单 | 离线 + 在线：种子 34.09 / 62.67；CH 28.75+83.48 / 46.11+155.61；Meta-Harness 160.51+38.34 / 781.56+89.19；AHE 209.44+38.91 / 793.48+69.41；Meta² 110.19+64.72 / 238.52+129.34 | 表 1；§4.3（L1723–1740） |
| 账单注 | 在线约为种子 1.9× / 2.1×；摊薄取决于部署次数 | **本项目按表 1 计算**；附录 E（L3802） |
| 改变了什么判断 | 跨题保留 81.00 → 78.33、44.44 → 39.11；avoid / hold 案例 | §4.5（L1823）；附录 D 图 7、图 8 |
| 读之前先知道 | 每设置一份 Meta-Skill，±0.91 / ±0.77 为重复评测波动；89 / 113 题随机划分；C 靠提示 + 审计；案例为示意 | 附录 C（L3252–3260）；附录 E（L3556）；§3.2；附录 F |

## 未展示

检查点间隔扫描（§4.4：L = 1 / 3 / 5 / 11，81.00 在 L = 5；该扫描是否在测试集上选定原文未说明）、DeepSeek 底座的成本列、Codex CLI 以外的人工 harness（mini-swe-agent、DeepSeek Harness）与 ReasoningBank 行、附录 D 图 5 / 6 / 8 的另三个案例。
