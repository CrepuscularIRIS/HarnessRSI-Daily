# SOURCE — 2610.38392 · 被掩蔽的侵蚀

- 论文：Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents（Hau-Sing So, Daixian Liu, Weicai Long；University of Macau / Tsinghua University）
- 版本：arXiv:2610.38392**v1**（cs.AI，2026-10-28）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2610.38392.txt`（HTML 转文本，sha256 `43d10529…a1fe`，与 pin `research/scoring/runs/rsi-l1-20261022-03/materials/2610.38392.json` 一致；pin 位置问题见 selection-007.md）。正文 §1–§5、Limitations 与附录 A–K **全部通读**。
- 初筛记录：L1 `batches/inc-l1-07.jsonl` → L2 `batches/inc-l2-09.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-007.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认范围：冗余防护被效用门控侵蚀的受控反例，不是生产环境频率，也不是已获保证的防护方案。画报保留：120 任务批为有放回重采样、去重会翻转 4/10 接受（只确认方向）；GEPA 只有 3 个种子、为个案；177 条预测中 49 条失败、主结论 14 项检验 7 项达标；换模效应限于更弱的执行模型。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首 | 验收门只看当前模型下的行为；重叠防护的删除被掩蔽 | Abstract（L58）；§1（L67–110） |
| 四层色带 | auth / verify / profile / caution 的功能 | §4.1（AppWorld 段）；附录 A Table 4（L240 附近） |
| 01 格点图 | 16 个子集的合并危害率（DeepSeek，校准+确认） | 附录 Table 17（L4005 起）；§4.2（L885–910）；Fig. 3a |
| 01 余量 | A、V 单独足够；H0 余量 2；masking 上界 | §3.2（L481–610，Eq. 2–3、L602）；§4.2 |
| 01 红线谱系 | 审计门 ρ=1：删 P → A → C，终态 V，余量 2→1；DeepSeek 0.025、Qwen3-30B 0.575、强 API 模型 ≤ 0.05 | Fig. 1 说明（L67–75）；§1；附录 Table 14 “veto ρ=1 第 5 条”（L3407 起）；Table 34 V 行 |
| 01 为什么看不见 | h₀₁ 0.016（UB 0.028）vs 0.422；约 6%；14/18 vs 2/29 | §4.2（L907）；§4.5（L1188–1195）；附录 C Table 7 段（L2050 附近） |
| 02 漂移表 | 接受率 0.48 / 0.44 / 0.04；失守 5/6、2/6、0/6；+0.075 改进放行 8% vs 96%；64 代 0.19；0.358 vs 0.400 | §4.3（L931–975，L940） |
| 02 选择图 | 成本 0 / .033 / .083 / .150 / .317 → 配对失守 0,0,1,6,4、贪心 5,4,5,3,5；n=20 @.15 0/6；n=120 @.033/.083 5/6；断点 0.08–0.15；冻结区间 | §4.4（L1138–1162）；附录 F Table 20（L4284 起）；Table 23 |
| 02 注 | 120 任务批有放回、去重翻转 4/10 | 附录 B “Archived Batch Replay”（L1698 附近）；§4.4 |
| 03 审计表 | Table 3 全部五行；区间 [0.16, 0.47]；Qwen3-8B 0.16；Luna/Sol 0.025 | Table 3（L1274）；§4.5（L1280–1310）；附录 I Table 33（L6137） |
| 03 GEPA | 3 种子 × 800 次调用；规则逐字保留；模板改写；2/40、5/40 vs 0/80；Fisher .003、符号检验 .125；验证增益 ≤ +0.22、T_final 0.35–0.45 | §4.6（L1320–1330）；附录 H Table 30（L5908）、“Where the Harm Came From”（L5929） |
| 04 补救 | 冻结安全文本：Qwen 0.019、未冻结提示；余量感知：0/6 vs 5/6、p = .031、OpsSim 代价 0.35、verify 被改弱 | §4.7（L1331–1350）；附录 F Table 21（L4526）、Table 22（L4657）；附录 G “Read-Only Safety Text”（L5768） |
| 04 边界 | 393/411 压力谱系；强模型本就避开；177/113/49；14 项 7 项；GEPA 预测后冻结 | Limitations（L1368）；§3.4（L797）；附录 A（L1481）；附录 K / Table 35（L6418–6580） |
| 05 自然改写 | 10 条被接受安全文本改动新任务增益 0.075 [0.007, 0.163]、7 条放松；改写层多放过 0.19 [0.08, 0.31]（合并 0.325）；profile 改写 .63 vs .38 | §4.4 “Natural Proposers”（L1164）；附录 G（L5436、L5616–5650、Fig. 8 L5643） |
| 05 无冗余 | 单层删除暴露 0.08–0.34；贪心 6/6、ρ=1 5/6、大审计 0/6，拒 23 次 | 附录 F “Without Redundancy”（L4534 起）；§4.5 |
| 05 作者做法 | 三条做法；Spearman 0.65 / 0.80 | §5 Conclusion；§4.5 末段（L1305）；附录 I Table 32（L6071） |
| 读法 | “当前安全 ≠ 出事后仍安全” | 本项目阅读（卡片 evidence_gated_retention），非作者原话 |

## 未展示

τ²-bench / AgentDojo / 隐私模拟的负面探索细节、时间一致误差控制（Table 27）、长程投影（Table 26）、Luna / Qwen3-30B 作为环路模型的结果（Table 18 等）。
