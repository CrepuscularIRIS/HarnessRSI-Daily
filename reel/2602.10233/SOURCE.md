# SOURCE — 2602.10233

- 论文：ImprovEvolve: Basin-Hopping Meets LLM-Guided Evolutionary Search（Kravatskiy, Khrulkov, Oseledets）
- 版本：arXiv:2602.10233**v2**（2026-06-26；与 `l3-final-2.tsv` 的 v2 一致）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2602.10233.txt`（正文 §1–6、Limitations、附录 A–D 的文字部分已读；附录中的演化代码清单只核对了 EDIT / LLM-EDIT 标记，即 selection-002 待补项“人工编辑 diff”；图 1–14 为图片，未从中取数）
- 初筛记录：L1 `batches/b035.jsonl` → L2 `batches/l2c13.jsonl`（P3 / confirmed / high / to_l3）；L3 `l3-final-2.tsv` #7、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03（第二期）

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 刊头 / 问题 | 单体程序直接输出解；生成程序依赖 L-BFGS-B 等现成例程；三方法接口；三个好处（降低负担、可读可调、可从任意给定解继续） | 摘要、§1、附录 A.1 两份提示词 |
| 单体接口代码 | `entrypoint(hex_num=11, seed=0) -> (centers, angles)` | 附录 A.1.1（简化） |
| 三算子接口 | `class Improver: improve / perturb / generate_config` | §1 列表、附录 A.1.2（简化） |
| 比例尺 | HEX 11 演化期 σ 档位 [1e2 … 1e-3] 共 11 档 | 表 2 |
| 外层种群 | 单岛 MAP-Elites，适应度为唯一描述子、150 个箱；Gemini 3 Pro 生成 5 个初始程序；Gemini 3 Flash Preview 演化；N_elites = 6、N_parents = 2、N_offspring = 10；improve 返回无效解即丢弃；程序适应度 = 内层最好解 | §3 Initialization / Evolutionary setup、§4 首段 |
| 内层两阶段 | 阶段 A：K 个种子 generate→improve 取最好；阶段 B：R 轮，σ 从 σ_max 几何递减到 σ_min（M 步），improve(perturb(x*, σ))，不变差才接受（T = 0），每轮重启 σ 调度 | 算法 1、§3 Validation Scheme |
| 区间图 | HEX 11：GigaEvo 3.9309 ± 0.0016 [3.9270, 3.9349]、最好 3.9296；ImprovEvolve 3.9261 ± 0.0014 [3.9227, 3.9295]、最好 3.9245；p = 0.0086。ACI 2：0.9430 ± 0.0041 [0.9328, 0.9532]、最好 0.9478；0.9494 ± 0.0019 [0.9447, 0.9541]、最好 0.9512；p = 0.0493。各 3 次独立 100 代运行，条件相同 | §4.3 表 4（含待补项“ACI 2 完整行”） |
| 单次最好对照 | HEX 11：AlphaEvolve 3.9301、全局求解器 3.9249、ImprovEvolve 3.9245；ACI 2：AlphaEvolve 0.96102、ImprovEvolve 0.9512 | 表 1 |
| 反例表 | A only 3.9282（K 1000、R 0）；B only 3.9269（1、100）；A+B 3.9245（100、5）；A+B+LLM 3.9270（100、100）；Lat.+B 3.9310（100、100）；GigaEvo 被 LLM 调大 Langevin 噪声后六边形重叠 | 表 5、§5.1 |
| 六边形规模条 | n = 11、12 来自表 1；n = 13–24 来自表 3 的 ImprovEvolve / +E 列；GigaEvo 最好程序在 n = 12 出现重叠；验证用 K = 100、R = 100、GPU | 表 1 及脚注、表 3、§4.1 |
| +E 编辑内容 | HEX：L-BFGS-B → SLSQP、软化初始罚权、放宽变量边界、迭代上限 800 → 10000（附录 A.2.2 EDIT 行）；ACI 2：多重网格改为从输入分辨率逐级升到 160 万步、去掉 1e-10 下限截断、提高 L-BFGS 迭代上限，从 AlphaEvolve 解出发 15 轮得到 0.96258 | §4.1、§4.2、附录 A.2.2、B.2.2 |
| 边界 4 | 球面码：++ 版本以 LLM 建议的 14 个高余量配置作演化信号，并在同一组配置上校准搜索，再用于 90 个配置 | 附录 D.2 |
| 边界 5 | HEX 单次演化约 10 小时（单机），ACI 2 约 40 小时 | §3 Computational cost |
| 边界 1 | 新纪录为单次运行最好值 | Limitations |

## 规模条状态的判定（本项目）

- “未经人工改动即超过已知最好”：ImprovEvolve 列严格小于表中已有最好值 → n = 11（3.9245 < 3.9249）、12（3.9416 < 3.9417）、15（4.4473 < 4.4477）、16（4.5275 < 4.5279）。
- “专家编辑后作者报告新最好”：n = 14、17、23，依据 §4.1 文字。n = 14 的 +E 值 4.2690 与求解器的 4.2690 在 4 位小数上相同，原文仍称新最好，画报照作者表述并标 “作者报告”。
- 其余为与已知最好持平（4 位小数相同）；n = 22 未编辑时 5.2857 略差，+E 后 5.2856 持平；n = 23 未编辑时 5.4848，差于已知 5.4286。

## 示意与重绘

- 等高线地形、跳跃路径、阶段 A 种子位置、种群谱系与“被改写的算子”黑框均为本项目示意，不是论文图 1 / 图 7 的复制。
- 区间图、规模条、反例表数值直接取自表 1、3、4、5。

## 核对说明

- 与 selection-002 / L2 一致，无 correction。
- 球面码结果（v2 新增）未上图，只在边界中说明其校准与评测配置是否分开原文未说明。
