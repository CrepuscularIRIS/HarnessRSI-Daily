# SOURCE.md — 2611.20655（MetaAct：知道≠做到）

- 论文：arXiv:2611.20655v1（缓存：research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.20655.txt，v1 html complete，sha256 bccb702f…）
- 海报为非作者重绘；全部数值出自论文正文，未复现、未运行论文代码。

## 逐数溯源

| 海报数字 | 论文位置 | 原文依据 |
|---|---|---|
| knowing-doing：规则进 prompt WebShop 0.390 vs 基线 0.400；SciWorld 0.700 vs 0.700 | knowing-doing 消融（Fig.4/5） | 同批规则两种去处对照 |
| 编译为 guard：WebShop 违规 0.010、SciWorld 0.700→0 | 同上 | typed guard 执行层拦截 |
| 主表：SciWorld SR 0.367 / score 62.1 最佳；ALFWorld 0.955；TextCraft 0.950/97.5；WebShop 62.1 | Table 1（DeepSeek-V4-flash） | 与 AutoGen 等基线对照 |
| matched-evidence：SciWorld 文本指导 −0.15 vs MetaAct +10.15；WebShop +8.01 | Table 2（matched-evidence 消融） | 同证据量下指导 vs 约束 |
| replay gate：有效阻断率 AUROC 0.966；接受约束 harmful blocking 6.5% vs 拒绝 23.1%；灾难性 10.0%→0.2% | replay 验证节 | 规则准入门评估 |
| 去 replay 验证：覆盖 0.211→0.433、harmful 0.069 | 消融 | 验证门的作用 |
| token：SciWorld MetaAct-synth 84.7k/回合、oracle 139.9k vs AutoGen 27.7k；合成一次性 487k/23 类 | token 附录 | guard 零 token 但拦截触发重规划 |
| AgentSpec TextCraft 0.0 | Table 1 | runtime-guard 基线适配失败（海报仅作提示不作排序） |

## 机制卡片语义

四步流程（从失败合成→replay 验证准入→编译为 guard→拦截重规划）为本项目按论文 GEAR 框架流程重绘；"知道/做到"双臂对比为本项目对 Fig.4 knowing-doing 消融的排版重述。与 AutoHarness（2603.03329）的差异框为本项目编辑注记。

## 缓存边界

缓存为 v1 html complete（materials/2611.20655.json），主表/消融/token 附录均在内；海报未引用缓存外数字。
