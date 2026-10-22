# SOURCE — 2610.07792

- 论文：ServeLearnBench: How Well Can Agents Self-Improve from Serving Experience?（Zheng, Di, Sadhukhan, Jin, Chen；CMU / Amazon）
- 版本：arXiv:2610.07792**v1**（2026-10-06）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2610.07792.txt`（HTML 转文本；正文 + 附录 A–D 已通读，含待补项 B.2–B.4）
- 初筛记录：L1 `batches/b068.jsonl` → L2 `batches/l2c01.jsonl`（P3 / confirmed / to_l3）；L3 `l3-final-2.tsv` #1、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 印章 | Oracle Hidden 均值 95.4、Blind 14.1（六模型） | §1 发现 1；§4.2 首段；Table 2 Avg. H 列（本项目复核：六模型 Oracle 95.5/93.6/95.6/93.1/97.1/97.6 均值 95.4，Blind 12.3/13.9/14.4/14.6/14.5/15.1 均值 14.1） |
| 第一题 | 现有基准或显式给知识、或假设静态环境；“能更新 ≠ 学到可复用知识” | §1 第 2–3 段；§2 |
| 第二题 | Blind / Oracle 定义；Hidden-Dependent / Fully Specified 定义；3 领域 × 3 档、53 窗、4,508 服务 + 3,210 测试 | §3.1、§3.2 “Reference baselines”；Table 1 |
| 第三题网格 | Retail L3 12 条规则的含义与逐窗激活；每窗服务/测试题数 | 附录 C.3 Table 7、Table 8；附录 C.2 Table 6（L3 行 78/60 … 78/65） |
| 学习者能/不能看到 | 可见：题面、自身轨迹、标量结果、持久状态；不可见：slice 标签、规则值、规则族、纠正动作、评估说明 | 附录 B.3 “Model-visible inputs and optimizer access” |
| 冻结协议 | 服务 + 计划更新后冻结；测试独立运行、丢弃局部状态、不进入更新/验证/选择 | 附录 B.3 “Serving-side and test-side isolation”；B.1 末 |
| SkillOpt 例外 | 调度器使用窗口分段安排更新与重放，提示中无窗口标签 | 附录 B.2 “When and how each harness learns”；B.3 |
| 第四题 条件 | 同任务流与计分、同模型同推理强度、50 次工具调用 / 100 轮、只给分数反馈 | §4.1；附录 B.2 第 2 段 |
| 条形图 | Prime 61.7、CH 57.7、RAG 43.4、SkillOpt 39.8、Mem0 38.3（四开源权重模型 × 九设置，冻结状态测试 Adapt） | 附录 D.4 Table 3 “Test (frozen state) Adapt”（与 Table 2 Avg. H 四模型均值一致：如 Prime 61.7/63.7/60.3/61.1 → 61.7） |
| Blind 13.8 / Oracle ≈94.5 线 | 本项目按 Table 2 四开源模型 Avg. H 计算：Blind (12.3+13.9+14.4+14.6)/4=13.8；Oracle (95.5+93.6+95.6+93.1)/4=94.45 | Table 2（本项目算术，画报已注明） |
| “差约 33–56 分” | 94.5−61.7≈33；94.5−38.3≈56 | 本项目算术 |
| 59.6 / 中位 22.0 | Retail L3 最佳 59.6、28 组合中位 22.0；最佳为 GLM-5.3 + CH | §1 发现 1；Table 2（GLM-5.3 区块 CH 行 Retail Hidden L3 = 59.6） |
| 98.9 → 89.5–95.5 | Retail FS：Blind 98.9 对学习 harness 89.5–95.5；Banking 91.7 对 83.6–86.2，Prime 95.2、Mem0 92.7 | §5.2（Figure 6 正文数值） |
| $2,479 对 $102 | Kimi K3 上 Prime 对 Oracle 成本；4–101× | §1 发现 2；Table 2 Cost 列（Kimi K3 区块） |
| 探索 AUC | 1.16/1.02/0.88/0.65/0.51，ρ=1.00；细分 30 格 ρ=0.75 | §5.3；附录 D.3 Figure 11 正文 |
| 限制 1 | 每格一次运行、无 SE/CI；28/30 组合，两组因成本省略 | Table 3 注；§4.1；Table 2（Opus 5、GPT-5.6 Terra 区块无 Prime 行） |
| 限制 2 | 不对齐更新节奏 / 状态预算 / 学习侧算力；Prime 运行时更强，CH–Prime 差含运行时 | 附录 B.2 第 1–3 段、“Acting agent” |
| 限制 3 | Pitch 用固定 GLM-5.3 Flash 评委；Opus 5 Blind 在 Banking FS 69.1/52.7/58.8，因自行猜测限制；FS 变化相对 Blind 解读 | 附录 B.1、C.6；附录 D.6 |

Table 2 模型区块识别：HTML 转文本中模型名出现在每个区块 SkillOpt 行前，本项目用正文交叉核对区块归属（Kimi K3 Prime $2,479 / Oracle $102；GLM-5.3 CH 69.8 对 Prime 63.7；GLM-5.3 Flash CH 49.7/82.8、Prime 61.1/95.2；Opus 5 Pitch L1 Oracle 90.8 对 CH 99.7），全部吻合。

## 示意与重绘

- 规则网格：按附录 Table 7/8 逐格重绘，Z5/Z6/Z8 三条全程激活规则合并为一行；规则中文名为本项目翻译。
- 条形图：按 Table 3 数值重绘；Blind/Oracle 线为本项目算术，已在画报注明。
- 本项目没有运行实验，也没有复现结果。

## 核对结论

与 L2 记录及 selection-002 一致，无 correction。展示边界沿用 selection-002：单次运行、非等算力、探索关联非因果。
