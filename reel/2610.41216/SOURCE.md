# SOURCE — 2610.41216 · 换规划器的装配说明（TinyAstral）

- 论文：TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents（Kehong Gong, Xiaoxu Zheng, Guanli Hou, Seunghun Lee, Mengqi Guo, Runjia Tan, Zhengyu Wen, Qi Wang, Xiaoyu He, Mingyuan Zhang, Michael Bi Mi；华为诺亚方舟实验室等）
- 版本：arXiv:2610.41216**v1**（cs.RO，2026-10-30）
- 钉定全文：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2610.41216.txt`（arxiv.org/html/2610.41216v1 转文本，sha256 `7968645…a601a572`，与 `research/scoring/runs/rsi-rolling-20261023-01/materials/2610.41216.json` 的 pin 一致；文本位于 rsi-l1 目录，见 selection-008.md）。正文 §1–§5 与附录 A–G **全部通读**；图 1–5 只有图注。
- 初筛记录：L1 `batches/inc-l1-09.jsonl` → L2 `batches/inc-l2-12.jsonl`（P3 / confirmed / capability / to_l3）；L3 `selection-008.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认的范围：冻结权重下演化的 harness 收益跨规划器保留，并可配合同接口蒸馏在小模型上部署。不展示为“双向 context–weight 共演化”“改进器层改进”或“全流程五倍便宜”。画报补充本项目读法：Table 1 中未训练 4B 与学生的 harness 增益相同（+26.6），蒸馏增量各版近似恒定，因此不能说明 harness 改进已写进权重；harness 演化收益只在 RoboTwin 同批任务上测，零样本基准无 H₁ 对照。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首 | 两段流程；180B / 552B / 0.8–4B；学生在同一 harness 替换教师 | Abstract；§1（L40–44）；Table 2 行名 |
| 第 1 步 | harness 与规划器分工；SAM 3 + 深度；done 谓词核验、两次拒绝后不再检查；成功标志不进输入；严格成功定义 | §3.1（L394 起、L443 起）；附录 G Tools（L3460，OFF_TARGET） |
| 第 1 步图 | 部件框与可换插槽；4 卡 FP8 / 1 卡 bf16 | 示意，据 §3.1、附录 G 与 Table 4（L1969）自绘 |
| 第 2 步 | 10 类失败；不许按任务名分支；触发标记；~1,150 配对；97.5% 下界、净胜、≥ 2 点否决 | §3.2（L504–522）；附录 E Direction screen / Statistical verdict（L3357–3383） |
| 第 2 步账本 | 296 / 121 / 16 / 142 / 17；101 项；7 收 3；评测种子 ≥ 100,000 | 附录 E Capability ledger（L3414）；§3.2；§4.1（L689 起） |
| 第 3 步折线 | 四规划器 × H₁ / H₇ / H₁₆ / H* 严格成功率 | Table 1（L792 起）；§4.2（L857–905） |
| 第 3 步黄标 | 21.6 / 21.2 / 26.2 / 21.6；两者都 +26.6 | **本项目按 Table 1 计算**，非作者结论 |
| 第 4 步 | 83,753 样本、一半仿真；严格成功筛选；恢复分支；保留推理 | §3.3（L581–625）；§3.4（L666）；附录 F（L3422） |
| 第 4 步表 | 去推理 / 去真机的 8 行配对差 | Table 3（L1788 起） |
| 第 4 步注 | 49/300 vs 7；0.235 → 0.923；19,598 中 15,089 条为给定参考后解释 | §4.4 Teacher reasoning（L1928）；Auxiliary real-robot（L1936）；附录 F Real-robot next-call pool（L3431） |
| 第 5 步左 | 62.8 / 63.6、93.6 / 94.7、78.3 / 80.0；未训练 4B 41.2 / 75.1 / 36.3；0.8B 54.7 | Table 2（L985 起）；§4.3 Student versus teacher（L1729）；Smaller students（L1777）；Table 5（L2403） |
| 第 5 步右 | 66.6 / 68.0、88.5 / 86.5、41.2 / 38.8、27.6 / 29.8；与 552B 差 ≤ 2.4；比教师低 2.6–5.0（本项目按表计算） | Table 2；§4.3 Generalization（L1749） |
| 部署账单 | 25.3 / 123.8 / 249.6 卡·秒；14/20、12/20、13/20；不含 RSI 等成本 | Table 4（L1969）；§4.5（L2050） |
| 部署注 | 教师在他人 harness：78.9 / 57.3 / 53.0；协议差异 | Table 2；附录 B Same teacher in alternative systems（L2505） |
| 注意框 | RoboTwin 为 RSI 开发基准、任务备注在 RSI 中修订、零样本无 H₁；分别训练；单次运行；20 回合 | §3.2 Task memory（L531）；§4.1；§4.2；Table 4 图注；本项目阅读 |
| 读法 | 与 2610.37255、2610.31401 的区别 | 本项目阅读，非作者原话 |

## 未展示

Table 7 已发表结果全表、图 3–5 的恢复案例（含一个学生失败案例）、真机 SO-ARM101 三项闭环任务（只有定性图）、附录 B 各基准调用上限。
