# SOURCE — 2610.37651

- 论文：GEPA-Curator: Curated Learning for Self Improving Agents（Zack Yu, Nicholas Lee 等；UC Berkeley / ICSI / LBNL / Furiosa AI / KAIST）
- 版本：arXiv:2610.37651**v1**（cs.CL，2026-10-27）
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/2610.37651.txt`（HTML 转文本，sha256 `c9f2abbc…5ae9`）。正文 §1–§6、附录 A–F 全部通读。
- 初筛记录：L1 `batches/inc-l1-05.jsonl` → L2 `batches/inc-l2-07.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-006.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 展示口径

按 L2 确认范围：噪声失败可经反思损害可解任务（受控混合 + 可追踪的负迁移实例），以及该方案在给定协议下缓解。不展示为“Curator 每次归因正确”或“等总成本更优”；诊断任务的事后挑选、验证集消融、高效版与完整版的成本差别均在画报中写明。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首 | 失败可来自 prompt、harness、随机执行、噪声 judge；先挑任务再给成功对照 | Abstract（L85–101）；§1（L131–183） |
| 展品 I | 第 7 轮、两个 Impossible 任务、evaluator 建议、“Exhaustive Exploration”规则（中文转述）；WCAG 任务 5 步成功 → 30 步用尽；minibatch 8 → 9 被接受为候选 5 | 附录 A.2（L1835–1867） |
| 展品 I 注 | 验证式闸门依赖聚合分、在变异后才起作用 | §1（L166–173） |
| 展品 II | 每任务历史；跳过类别（mastered / impossible / 无信号 / flaky / evaluator-broken / 基础设施）；拿不准就跑；跳过每 epoch 重审 | §3.1（L416–426）；附录 B.2 提示词（L2054–2088） |
| 展品 II | 成功锚点须另有独立干净成功佐证，否则弃权；一次调用联合决策 | §3.2（L428–444）；附录 B.2（L2090–2110） |
| 展品 II | Curator 与反思器同一模型；minibatch 16；单谱系贪心、无 Pareto；每 16 步验证 | §4.1（L465–487） |
| 展品 III 图 | Gemini 种子 72.4±2.4 / GEPA 78.7±0.6 / Curator 82.1±1.7；Opus 73.1±1.8 / 79.5±1.2 / 84.5±1.0 | Table 1（L561–804） |
| 展品 III 文 | 6.3/6.4、9.7/11.4、3.4/5.0；逐站 0.6–7.4；3:1:1、验证选终版、5,000 rollout、同种子 prompt | §4.1–4.2（L489–559） |
| 展品 III 表 | ALFWorld / AppWorld-N / AppWorld-C / τ-bench 各方法分数；τ-bench（Opus）持平 82.9 | Table 2（L824–1060） |
| 展品 III 注 | “5 repeated runs”原文措辞；成本“one run per method and benchmark”；HotpotQA −1.3 | §4.1（L487）；§5.4（L1739）；附录 E Table 16（L3465–3479） |
| 展品 IV | 消融 82.8 / 84.2 / 84.7 / 88.6（520/200，验证集上报告）；w/o Pareto 82.5（正文提及，画报未列） | §4.3 Table 3（L1062–1136） |
| 展品 IV | 48/54/45/21 组成；62.5 / 66.2 / 67.4 / 70.2 | §5.1 Table 4（L1218–1276） |
| 展品 V | 75/1,581（4.7%）；impossible 18 中 12 为 harness/环境；flaky 65 中 30 任务含糊、7 推测、5 推翻 | §5.2（L1281–1288）；附录 C.1 Table 9–11（L2293–2536） |
| 展品 V | 554 合格任务中相关选择 17、有理由弃权 50 | 附录 C.2 Table 14（L2903–3100） |
| 展品 VI | 各项美元成本；高效版 WebArena 均值 82.3；1.31×；按 Gemini 价格、不含测试与托管 | §5.4 Table 8（L1637–1771）；附录 D Table 15（L3102–3358） |
| 展品 VII | Fig. 2 曲线在训练集上、最多 12/16；分组依先导运行与人工检查 | §5.1（L1186–1216）；附录 A.1（L1822–1833） |
| 展品 VII | QA 类平均 +1.1；Meta-Harness 每设置一次优化 | 附录 E（L3480–3505）；§5.3（L1334） |
| 本项目读法 | 先归因再喂优化器；B 类组件 | 本项目阅读判断；收录口径见 docs/EVIDENCE.md |

## 自行绘制 / 示意说明

- 展品 I 的两条路径按附录 A.2 文字顺序重绘，中间步骤未逐一计数，图中注明“示意”。
- 展品 II 机制图按 §3 与附录 B.2 提示词绘制，原文 Fig. 1 未引用其图形。
- 展品 III 点图与展品 IV 条形按表格数值绘制；展品 IV 条长自 76 / 58 起算以放大差异，已在图注说明。
