# SOURCE — 2604.11811

- 论文：M★: Every Task Deserves Its Own Memory Harness（Pan, Liu, Zhou, Zhang, Shi, Xu, Jia；CityU HK / Microsoft）
- 版本：arXiv:2604.11811**v2**（2026-05-23）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2604.11811.txt`（正文 + 附录 A–L 已通读，含待补项附录 B、D）
- Fig.5 原始数值：钉定文本中没有（图为矢量图）。本项目下载 arXiv HTML v2 的图资源 `https://arxiv.org/html/2604.11811v2/fig4.svg`（页面中 Figure 5 引用此文件），用 headless Chrome 渲染后读取柱顶标注（两位小数）。私有缓存未提交。
- 初筛记录：L1 `batches/b040.jsonl` → L2 `batches/l2c14.jsonl`（P3 / confirmed / to_l3）；L3 `l3-final-2.tsv` #2、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03

## Fig.5 读数（目标 × 来源）

| 目标 \ 来源 | Universal mem. | LoCoMo mem. | ALFWorld mem. | Legal mem. |
|---|---|---|---|---|
| LoCoMo（Token F1） | 0.26 | **0.46**（本地） | 0.02 | 0.09 |
| ALFWorld（Success Rate） | 0.64 | 0.62 | **0.88**（本地） | 0.58 |
| PRBench（Rubric Score） | 0.47 | 0.06 | 0.58 | **0.66**（本地） |

- 6 次迁移中低于种子 5 次（0.02、0.09、0.62、0.58、0.06），高于 1 次（ALFWorld→PRBench 0.58 > 0.47）——与 §5 “Five of six transferred programs perform worse than the universal seed baseline” 一致。
- “Universal mem.” 识别为 Vector Search 种子：三格数值与 Table 1 Vector Search（LoCoMo F1 0.256、ALFWorld Unseen 0.643、PR-Legal 0.466）一致，属本项目推断，画报已注明。
- ALFWorld 面板本地值 0.88 = Table 1 ALFWorld Unseen 0.881；PRBench 面板本地值 0.66 = Table 1 PR-Legal 0.660，故画报标为 “ALFWorld Unseen”“PRBench-Legal”。
- 坐标上限 0.6 / 1.0 / 0.8 取自原图各面板 y 轴。

## 其他断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 问题 | 不同任务需要不同存储与检索；最强基线随任务变化 | §1；§5 首段；Table 1 |
| 研究动作 / 机制 | Schema / Logic / Instruction / Toolkit；静态 + 轮换验证；编码代理补丁；编译与运行检查；程序池 softmax 抽样 | §3.1–3.3；Algorithm 1 |
| 机制数值 | 3 个种子（Vector Search / LLM Summarizer / Experience Learner）；τ=0.15；静态子集 32–60 题（k-means）；轮换 5 题 / 轮；修复 3 次；20 轮 | 附录 D.2 Table 7；附录 E Table 8；§4 |
| Toolkit 约束 | 每次 read/write ≤1 次 LLM 调用、read 输出 ≤3000 字符、60 秒超时 | 附录 G.2 “Runtime Constraints” |
| 程序结构 | LoCoMo 7 字段 SQLite+Chroma；ALFWorld Unseen SQLite-only 加精确匹配加分；PR-Legal 22 字段 | 附录 F.1、F.2；Table 9 |
| verdict 3 | 演化会把任务特定启发式写进逻辑（ALFWorld 同义词表），限制迁移 | 附录 J 第三条 |
| 7/8 项最优 | M★ 在 8 项中 7 项最好；PR-Finance 0.586 对 GEPA 0.449；LoCoMo 0.459 对 Mem0 0.373；ALFWorld Seen 0.700 对 GEPA+VS 0.820 | §5；Table 1 |
| 14/15 | 3 基准 × 5 种子，14 次胜最强基线，CV ≤10%；LoCoMo seed 2 = 0.364 | §6 Table 3；附录 I.2 Table 13 |
| 消融 | −Code −0.203（0.256）、−Instruction −0.106、−Diversity −0.141、Max parent −0.078 | §5 Table 2（仅 LoCoMo） |
| 限制 2 | 固定 GPT-5.4 Mini + GPT-5.3-Codex，未测依赖 | §4；附录 D.1；附录 J 第二条 |
| 限制 3 | 每基准演化 $12–90；ALFWorld 约 100h；LoCoMo 测试 100 QA；时间 / 因果类 Mem0、GEPA+VS 更强 | 附录 D.1 Table 6 及注；附录 B.1 Table 5；§6 Table 4 |

## 示意与重绘

- 迁移棋盘：Fig.5 数值按 目标 × 来源 重排，格底细条按原图坐标上限换算比例；不是新实验。
- 机制流程图与棋子图标为示意。
- 本项目未运行实验或复现结果。

## 核对结论

与 L2 记录、selection-002 一致，无 correction。补充：迁移矩阵每格为单一最佳程序，原文未给重复或误差，画报限制中已写明。
