# SOURCE — 2611.26132 AdaObs

**Sage-Evolve-Preview: Adaptive Observation for Post-Training Self-Improvement** · arXiv 2611.26132v1 · 2026-11-19
全文缓存：research/fulltext/2611.26132.txt。核对模型：glm-5.3（selection-020，2026-11-21）。

## 问题
- 自改进循环只拿锚定基准总分当唯一观测，早期增益后陷入停滞与重复探索 — §1。
- 关键句："a plateau may reflect an exhausted observation rather than an exhausted capability" — Abstract/§1。
- 现有 harness 演化改"作用于什么/怎么作用"（数据、合成代码、agent 组件），观测侧被冻结 — §1。

## 机制（§3，示意重绘）
- 观测三元组（基准集、难度/子集选择、诊断分辨率 ψ）；锚定观测 O★ 冻结，主动观测 O_t 平台期升级 — §3.1/§3.2。
- 七阶段循环：观察→分析→计划→生产→验证→训练→评测；实验记忆存确认与失败结论，跳过已证伪更新 — §3.1。
- 阶梯 L1 细化诊断粒度 / L2 难度升级（累计保留旧层）/ L3 加相邻任务；每步只动三元组一格其余继承 — §3.2。
- harness 更新走慢时钟：重复失败触发受限候选，修复集+回归缓冲双回放才提交；评测器/锚定/验证门不可变 — §3.3。

## 数值映射
| 海报数值 | 原文位置 |
|---|---|
| 66.4 → 73.7（八锚定均值，同预算超 FixedObs） | Abstract（"raises the mean score from 66.4 to 73.7 under a matched data budget"）；§4.2 |
| 8/8 锚定全部超 FixedObs，超过 Qwen3.5-35B-A3B 与 Qwen3.6-35B-A3B 现成检查点 | §4.2（"on every benchmark … surpassing both off-the-shelf Qwen checkpoints"） |
| L1 案例机制：超长率+think 触发率 → 增量缺 think 轨迹稀释基座监督 → 重滚后超长率大降、MRCR v2 / AA-LCR 脱困 | §5.1 全段（具体比率数值在缓存全文中被公式掏空，海报只用定性描述） |
| L2：更难子集加入后最早观测子集最终最强；难侧增量不对称回流 | §5.2 |
| L3：LongBench v2 纳入 AA-LCR、MRCR v2；LIFBench 纳入 IFBench、AdvancedIF；主基准再上台阶 | §5.2 |
| PostTrainBench 双后端迁移：GLM-5.2 / Opus-4.8 均升，harness 冻结不改 | §4.3（"lifting the seven-benchmark average … under both backends"，具体数值缓存截断不可见） |
| 单杠杆消融只收回部分增益，全阶梯才完整 | §4.2 末（"A single-lever ablation (Appendix Table 4) confirms that each lever alone recovers only part of the gain"） |
| 消融饼图 34/33/33 分割 | 示意（原文 Table 4 数值截断不可见），柱状主结果 66.4/73.7 为摘要实数 |

## 限制（原文声明 + 核对发现）
- 主证据为单基座（Qwen3.5-35B-A3B-base）单训练形态（全参 SFT），主循环 agent 后端固定 Claude-Opus-4.8 — §4.1。
- 预算为"comparable effective-increment budget"，是当量而非逐字节相同 — §4.2。
- 阶梯顺序固定 L1→L2→L3（"The ladder fixes only the order"），未报告其他顺序对照 — §3.2。
- 核对发现：缓存全文在 §5.3 中段与各表格数值处被公式/表格提取截断，迁移幅度、L1 案例具体数值、Table 4 消融数值不可见；海报只用摘要级数值（66.4→73.7、8/8）与定性结论，饼图为示意。
