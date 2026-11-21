# SOURCE — 2611.25534 无反馈技能侵蚀

**How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study** · arXiv 2611.25534v1 · 2026-11-19
全文缓存：research/fulltext/2611.25534.txt。核对模型：glm-5.3（selection-020，2026-11-21）。

## 问题
- 无反馈自演化让 agent 重写自身技能，缺少任务、运行或判断的校正 — §1。
- 核心问题："重写是改进技能，还是把专家知识磨掉？" — §1 三问之一。
- 六个模型（GPT-5.6-Luna / GPT-6.1-Sol / MiMo-V2.5-Pro / Claude Haiku 5.5 / Qwen3.7-Plus / Qwen3.8-Flash）× 三基准（SkillsBench 87 / LogicBench 760 / MedCalc-Bench 1100）— §3。

## 数值映射
| 海报数值 | 原文位置 |
|---|---|
| SkillsBench 30 轮平均 −15.0pp（六模型均值） | §3.1（"decreases performance by up to 15.0 percentage points on average across all six models"） |
| 第一轮 −7.1pp | §3.1（"an average loss of 7.1 percentage points already after the first rewrite"） |
| 30 轮后比原始技能低 10.3–23.0pp（各 agent×基准） | §3.1（"10.3 to 23.0 percentage points below the original skill"） |
| LogicBench 86.2%→71.4% = 无技能水平；MedCalc 89.7%→78.7% &lt; 无技能 81.1% | §3.1（"equal to the no-skill level … 71.4%""below the no-skill level … 78.7% vs 81.1%"） |
| 条目存活率 23.1% vs 84.2%（0/10 含 vs 10/10 全含），gap 61.1pp | §3.2（"survival rate of 23.1% … versus 84.2%"） |
| 中间两档 ~56% / ~74%（趋势示意） | §3.2 Fig.3 单调趋势（原文未逐档给数，海报标"示意"） |
| 换 judge（GPT-6.1-Sol 复验 20 任务）gap 仍 49.5/52.5pp | §3.2（"robust to judge choice" 段） |
| TF-IDF 距离 1.37→1.19（第 5 赫[轮]）→1.22（第 30 轮），自写技能 ≈1.0 | §3.2（"distance 1.37 … 1.19 … 1.22"） |
| SkillDiff 标记 +4.8pp（六 agent 全部增益，同批对照控漂移） | §4（"improves performance by 4.8 percentage points on average … across all six agents"） |
| 恢复先验外条目多挽回 vs 恢复先验内条目 | §3.3（"restoring out-of-prior items recovers more performance than restoring in-prior ones"） |

## 机制（§3.2/§4，示意重绘）
- 条目存活 = 30 轮重写后该条目仍以等价语义存在；LLM judge 判存。
- 先验分组 = 10 份自写技能（同模型零样本写技能）中含该条目的份数 0/10、1–5/10、6–9/10、10/10。
- SkillDiff = 不重写，只给"10/10 都不含"的条目加 FOCUS 标记与一行说明；删标记行即字节级还原。

## 限制（原文 Limitations 及 §5）
- 重写为递归链式（每轮基于上一轮），未做分支/温度敏感性分析。
- 条目存亡由 LLM judge 判定（已换 judge 复验，仍非人工全量）。
- SkillDiff 增益仅在 SkillsBench 多步设定验证，单提示场景未测。
- 自写技能仅 10 份采样先验，条目分组边界对采样量敏感。
