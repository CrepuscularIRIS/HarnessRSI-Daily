# SOURCE — 2610.40758 · 例外清单还是规则（CLR-Bench）

- 论文：More Rules, Longer Lists? Benchmarking Self-Evolving Agents on a Hidden-Rule Curriculum（Chenjie Qiu, Boyan Xu, Shaobin Shi, Bingfeng Chen, Ruichu Cai, Dongsheng Luo；Singapore Management University、广东工业大学）
- 版本：arXiv:2610.40758**v1**（cs.AI，2026-10-29）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2610.40758.txt`（arxiv.org/html/2610.40758v1 转文本，sha256 `cc903eed…e34fe1af`，与 `research/scoring/runs/rsi-rolling-20261023-01/materials/2610.40758.json` 的 pin 一致；文本位于 rsi-l1 目录而非本 run 目录，见 selection-008.md）。正文 §1–§8 与附录 A（Table 4–11、A.1–A.4）**全部通读**；图 1–8 只有图注（HTML 转文本无图），图中数值未单独核对。
- 初筛记录：L1 `batches/inc-l1-09.jsonl` → L2 `batches/inc-l2-12.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-008.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认的范围：在“隐藏命名分组”任务、认证模型 GPT-6-Luna 条件下，自我演化方法把纠错记成例外清单，练习通过率不反映学习；更强的 GPT-6-Sol 下 ACE / DC 只靠反馈就能学会。画报保留：类别按 Luna 认证筛选（LEARNABLE 探针用到测试成员）、每条件单次运行、GEPA 主结果加了中性提示、“说明”是额外信息、token 预算不对齐、可识别性依赖命名分组约定。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首 | 持久状态改写、20 链 × 4 级 = 80 条规则、10 领域 | Abstract（L120 起）；§1（L49 起）；§4.3（L1139） |
| 数据页 | Lufthansa / Thai Airways / ITA Airways / United Airlines 示例；B8；练习“最大总数”、测试“总和” | §1（L52–53）；§3.2（L964 起）；附录 A.4（L3302 起） |
| 数据页两种状态 | ACE 一级后状态与加说明后的状态（译述） | §7.2.1（L1425 起，“In a chain whose class is the founding members of Star Alliance…”） |
| 数据页注 | 练习只插 m₀ / n_p；冻结台阶 0.80 / 0.60 / 0.40 / 0.20 | §3.2（L964–1006） |
| 四道章 | KNOWN / HIDDEN / LEARNABLE / SOLVABLE 及阈值 | Table 3；§4.2（L1117 起） |
| 四道章注 | 6.5 个（最多 20）其他名单；冻结实测 0.80 / 0.57 / 0.34 / 0.20；另四模型最多 4 / 80 高于台阶 | §4.3（L1139）；§4.2 末；§7.1.2（L1390）；Table 9（L2653） |
| 主图 | 两底座 × 8 条件的未见成员排除率、非成员保留率、平均准确率 | Table 10（L2746 起）；图 4 为 Luna 版 |
| 主图注 | +1.8–5.0；6–12% vs 20%；Sol 78.3 / 78.5、68–76% vs 70.3；Sol 冻结 32.5；GEPA / EvoSkill 48% / 41%、66% / 53% | §7.1.1（L1314）；§7.1.2（L1334、L1382）；Table 7（L1896） |
| 章 01 | 92.5% vs 12.2%；DC 80.0 / 11.8；GEPA 87.0 / 5.8；75–98% vs ≤ 3%；89% / 93% vs 9% | §7.2.1（L1425 起）；§7.2.1 状态标注段（L1444 起）；附录 A.1（L3234） |
| 章 02 | 95% → 8%；91% → 13%；m₂ 9.5 / 4.0 / 14.0 vs 12.0 / 4.5 / 11.0；19.5 → 42.0 | §7.2.3（L1528）；§7.2.2（L1489） |
| 章 03 | TF-GRPO 状态全空；EvoSkill 9/20、449 提案约 1/3 格式错误、70% / 14%；ReasoningBank 51%、−14 点；6M / 0.9M / 0.07M | §7.1.1（L1322 起）；§7.2.3（L1528） |
| 附页表 | 52.5 / 52.8；55.0 / 55.0；71.5 / 65.8；67.0 / 68.3；72.0 / 53.8；63.8 / 64.3；73.5 / 75.8 | Table 7（L1896）；Table 8（L2444）；§7.2.1（L1459、L1476） |
| 附页注 | 69% 状态丢标签；说明文字内容；第 2–4 级 75 / 58 / 39 vs 64 / 44 / 23 | §7.2.1（L1459–1476）；附录 A.2 |
| 签注 | 单次运行 / 20 链平均；Sol 1–2 级 > 80%、第 4 级余 41 点；GEPA 原版 6.8% | §6.2；§7.1.2；附录 A.3 GEPA note（L3286–3297） |
| 读法 | 与 2610.34938 方向一致 | 本项目阅读，非作者原话 |

## 自绘与重绘

- 主图：按 Table 10 数值用脚本重绘（标签位置为避免重叠手调，未改数据）。
- 数据页流程与状态卡：按 §1、附录 A.4 与 §7.2.1 原文译述改绘，不是原论文图。

## 未展示

Table 1–2（相关基准与方法对比）、Table 4 全部类名、Table 11 分领域结果（说明在网络安全与药房审核领域增益小）、图 7–8 的失败模式与保留曲线。
