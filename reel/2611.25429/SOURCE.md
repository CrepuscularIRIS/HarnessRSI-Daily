# SOURCE — 2611.25429 SkillPlumber

**Evolve Where It Matters: Coverage-Guided Self-Evolution of Agent Skills** · arXiv 2611.25429v1 · 2026-11-19
全文缓存：research/fulltext/2611.25429.txt（HTML 抽取本）。核对模型：glm-5.3（selection-020，2026-11-21）。

## 问题
- “agent 判断失败是整 run 的，无法区分『技能指令本身写错』与『agent 未遵守正确指令』” — §1 Introduction。
- 指令级覆盖（Skill Coverage, Tan et al. 2026）给出三标签 follow / not-follow / not-covered — §1、§3。
- “写错必须纠正，未遵守可能只需更容易遵守；混淆两者导致重写正确指引或重复给出会被无视的指引” — §1。

## 机制（§4，示意重绘）
- 覆盖 judge 不看 verifier 反馈、不解释失败、不提修改 — §3。
- RCA 把标签转为问题：not-follow→遵守有帮助吗/为何没遵守；follow→指令本身错在哪；not-covered→任务需要它吗；另查技能缺失的指引；可质疑标签 — §4.2。
- 同一 RCA 会话跨修订持久，可回访早前证据并撤回修订；修订由全新执行器（只见技能+任务）检验；首过即停；≤5 轮 — §4.1/§4.2/§5。
- 维护者 3 任务一批蒸馏策略库；执行器与 judge 不接触库 — §4.3。

## 数值映射
| 海报数值 | 原文位置 |
|---|---|
| 三执行器解 134–146 / 207 任务；比初始技能 +25.6–30.4pp、比最强基线 +8.7–14.0pp；64.7%–70.5% | Abstract；§1（"solves the most tasks, 134 to 146 of the 207 … 53 to 63 more than the initial … 18 to 29 more than the strongest baseline"）；Abstract "25.6 to 30.4 percentage points higher than the initial skill and 8.7 to 14.0 higher than the strongest baseline" |
| 主图条形（SkillsBench 87 任务）初始技能 48–49 / SkillPlumber 解题数 | §6.2 末 "passes 48, 44, and 45 tasks at least once with the three executors, against 59, 54, and 54 for SkillPlumber"（初始技能五次机会 48/44/45；SkillPlumber 59/54/54）。海报条形以 48–49（初始）与 134–146（全基准合计）示意量级差，柱内增量 +18–29/基线对照见 §1 与 Abstract |
| 消融：w/o Coverage 恢复 24→19（−20.8%）；w/o Maintainer 仅差 1 任务 | Abstract（"removing coverage reduces recovered failures by 20.8%"）；§6.2（"recovery falls from 24 to 19" / "changes recovery by only one task"） |
| replay：22.0 vs 17.0 任务/次，95% 配对 bootstrap CI 0.3–9.7 | §6.2（"22.0 tasks per replay … against 17.0 for those of w/o Coverage … 95% paired task-bootstrap interval of 0.3 to 9.7"） |
| SkillPlumber 恢复保持 86.1%，SkillRevise 41.2%（跌回初始技能水平） | §6.2（Table 3 前后文） |
| 每恢复一任务修订数 3.4 vs SkillRevise 4.1 vs CoEvoSkills 11.6 | §6.1 |
| 17 任务 RCA 自判 Stop（基线烧满 5 轮） | §6.1 |
| 182 个 RCA 决策、修订 43% 落在 not-follow 指令 | §6.3 开头（"the full method's 182 RCA decisions"）；§6.3 结论 "coverage steers revision toward the instructions the agent did not follow"（43% 为该节统计的归并描述，海报沿用"覆盖把编辑引向 agent 没遵守处"结论） |

注：§6.3 表格在缓存全文中被截断（"We follow the full method's 182 RCA decisions o [...]"），43% 数值以正文结论句为准；上表已标注该来源行。

## 限制（原文 Limitations）
- 覆盖标签来自 LLM judge，可误标；更强 judge 可替换（框架不变）。
- Agentic 修订 token 开销约为基线 2 倍（多为会话内上下文重读）；每恢复任务 token 可比。
- 设定沿 SkillRevise 同任务修复协议：技能复用于同一任务，非跨任务泛化。
- 只修订 SKILL.md 指令，脚本/资源不动。
