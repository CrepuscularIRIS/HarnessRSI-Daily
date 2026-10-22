# SOURCE — 2604.04247 Combee

- 版本：arXiv 2604.04247**v2**（2026-09-25），标题 *Combee: Scaling Parallel Prompt Learning for Self-Improving LLM Agents*（按钉定的 v2）。钉定全文 `research/fulltext/review-runs/rsi-v22-20261021-01/materials/2604.04247.txt`（私有缓存，不提交）。
- 阅读范围：§1–§6 全文；附录 B（限制）、C、D、E（Table 4–10）、F、G（Table 11）、H（Table 12）、I 的说明段。附录 J 的 playbook 快照没有逐条阅读。
- 初筛记录：L1 `research/scoring/runs/rsi-l1-20261022-03/batches/b039.jsonl`；L2 `batches/l2b06.jsonl`（P3 / confirmed / to_l3）；L3 `selection.md` 终选 #8、`l3-final.tsv`。本篇无 correction。

| 画报内容 | 原文位置 |
|---|---|
| 生成-反思-更新、ACE/GEPA 按串行或低并行设计 | §1 第 3 段；§2.1 |
| 上下文过载定义；128K 窗口内仍发生；有损压缩成泛化模式 | §2.2 |
| Formula 264→21、87.0%→72.5%（批 1→100）；FiNER 246→11 | §2.2 Quantitative Evidence（图 2） |
| 命中 ≥3 次条目 19→0（Formula 批 1→100） | §2.2 Qualitative Evidence |
| Map–Shuffle–Reduce；√n 分组；复制 p=2；动态批控制器 | §1；§3.1–3.3；图 3 |
| “扩展层，不改变生成与更新机制” | §1；§3 Interface |
| GEPA Formula 规模曲线：朴素 5/10/25/50/100 = 0.855/0.860/0.855/0.810/0.723（2981/1894/844/510/360 s）；固定批+shuffle/scan 20/25/50/60 = 0.859/0.856/0.852/0.849；Combee 动态批 84 = 0.845 / 338 s；基座 0.640 | 附录 E Table 8（GEPA 部分）、Table 6 |
| 三次重复：Combee 0.857±0.005 / 459.3 s；批 10 0.857±0.007 / 2071.3 s；批 80 0.771±0.005 | 附录 E Table 4 |
| ACE Formula 曲线：朴素 5/10/20/50/60 = 0.820/0.810/0.755/0.745/0.715；固定批+shuffle/scan 20/40/60/80 = 0.850/0.830/0.820/0.825；动态批 80 = 0.825 / 3510 s；批 20 固定 5450 s；朴素批 5 9464 s | 附录 E Table 8（ACE 部分）、Table 7 |
| 去增广洗牌消融 p=1→2：GEPA 0.803→0.857，ACE 0.825→0.855（Formula） | §4.4 Table 3 |
| AppWorld 全表（ReAct、DeepSeek-V3.1、90 个训练任务、Test-Normal） | §4.1；§4.2 Table 1 |
| Terminal-Bench 2.0 全表（Terminus-2、60 条 DeepSeek 3.2 离线轨迹、29 个留出任务、3 次平均） | §4.1；§4.2 Table 2 |
| 17×（42.4→2.4 min）、12×（86→7 min） | §4.2 正文；Table 1–2 |
| 生成阶段未计入成本 | 附录 H 第 1 段 |
| 规模限制（90/89 任务、千级轨迹未测、两层设计） | 附录 B Scaling to Larger Trace Volumes |
| 同一配置不同表数值不同：Combee+GEPA Formula 0.845（Table 6/8 单次代表性运行）对 0.857（Table 3/4） | 附录 E Table 6 注；§4.4 Table 3 |

## 自绘与重绘

- Map→Shuffle→Reduce 对照图：**示意**，按 §3 与图 3 文字自绘，不是论文原图。
- 两张规模-质量曲线：按附录 E Table 6/8 数值**重绘**，不是论文图 4/5/7。横轴为对数批大小；“分叉区：批 > 25”是本项目标注（25 是朴素并行与 shuffle/scan 仍重合的最大批）。

## 展示边界（selection.md 第 8 条＋L2 子卡 partial 项，均已上版）

朴素批 10 质量接近，增益主要是速度；Terminal-Bench 仍低于串行；离线 rollout 成本未计；更大 playbook 的推理成本未匹配。另据核读补充：AppWorld 未注明重复次数；ACE 上动态选批不如固定批 20；曲线为单次代表性运行。
