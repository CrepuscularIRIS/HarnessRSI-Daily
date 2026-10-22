# SOURCE — 2601.22436

- 论文：Large Language Model Agents Are Not Always Faithful Self-Evolvers（Zhao et al.，哈工大 / SMU）
- 版本：arXiv:2601.22436**v3**（2026-06-12）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2601.22436.txt`（HTML 转文本，正文 + 附录 A–D 已通读；图 2–6 的柱状数值是图片，文本中没有）
- 初筛记录：L1 `batches/b034.jsonl` → L2 `batches/l2b05.jsonl`（P3 / confirmed / high / to_l3）；L3 `l3-final.tsv` #1、`selection.md` 阶段二
- run：rsi-l1-20261022-03

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 副标题 | raw 扰动明显降分；condensed 换乱码/无关文本几乎不变；只提供 condensed 时仍如此 | 摘要；§4.1；§4.2 |
| 假设框 | faithfulness 定义：扰动经验后行为是否因果改变 | §1 |
| 矩阵 第 1 行 | 去掉 raw、Empty、Irrelevant 使成绩“同样严重”下降；Shuffle 部分稳健（附录 D.3 “partial robustness”），但 GPT-5.2 执行 raw Shuffle 75.4→47.0 | §4.1；附录 D.3、D.5 |
| 矩阵 第 2 行 | Corrupt / Irrelevant / Filler 与基线几乎无差别；去掉 condensed 只有轻微影响 | §4.1 |
| 矩阵 第 3 行 | ReasoningBank 去掉 condensed 在 4 个 WebArena 子任务上都下降；语义扰动影响可忽略甚至略升；作者把收益归于“有一块文本”或风格（Empty） | §4.2、Fig.4 图注；附录 D.4 |
| 矩阵脚注 | GPQA、MMLU-Pro 上两类经验敏感度接近；FEVER 上 raw 影响较弱 | §4.1 末段；§4.3 |
| 研究动作 | 干预样例（raw 原文、Shuffle、cond 原文、Corrupt、Irrelevant、Filler、Empty） | 附录 Table 3；§3.2–3.3；附录 D.1–D.2 |
| 范围 | 4 个框架、骨干列表、9 个基准、骨干冻结 | §3.1；附录 A–B |
| §3 左侧条形 | G-Memory · Qwen3-235B-A22B · ALFWorld：基线 78.4；参考 raw Irrelevant 47.8（−30.6）；执行 raw Empty −6.8；condensed Filler 77.6 | 附录 D.5 |
| §3 右侧 | GPT-5.2 G-Memory ALFWorld 执行 raw Shuffle 75.4→47.0；Claude-Sonnet-4.6 ExpeL HotpotQA condensed 干预 53→47–56 | 附录 D.5；附录 D.3 |
| §3 右侧注 | Qwen3 1.7B–32B 放大；ExpeL 摘要由骨干自己生成，condensed 仍不敏感 | §4.4 |
| §4 表 | 2WikiMultiHopQA / Musique：62/48；raw 63–65 / 43–47；condensed 63–65 / 44–47（各 100 例，EM，Qwen3-32B） | §5.3 Table 2 |
| §5 失败类型 | 偏离目标 Gemini-2.5-Flash 18.8–45.2%、Qwen3-32B 61.9–79.2%、Qwen3-14B 60.9–86.7%；套用先验 Gemini 27.3–33.3%；过早下结论 Gemini 22.6–50.0% | §5.1 Table 1 |
| §5 IG 句 | condensed 段梯度贡献低、深层以当前轨迹为主；附录说明实际用的是嵌入梯度范数近似 | §5.2；附录 D.7 |
| 边界 | 骨干数 13 vs 10 | 摘要 / §1 vs §3.1 |

数值范围（如 63–65）由本项目按原表逐项取最小、最大值汇总。

## 示意与重绘

- §1 矩阵是**示意**：按原文文字结论归纳（下降、近乎不变、轻微），不是原图数值。
- §3 条形图根据原文附录**文字给出的数值**重绘；“执行 raw → Empty”只标原文给的降幅 −6.8，条长取 78.4−6.8。
- 本项目没有运行实验，也没有复现结果。

## 展示边界（来自 selection.md 并经核对）

无方差；“不敏感”针对聚合成功率；IG 归因只是相关证据；多跳表上 raw 也不敏感（依赖任务）；13 vs 10 骨干计数不一，不影响结论。核对未发现与 L2 记录冲突，无 correction。
