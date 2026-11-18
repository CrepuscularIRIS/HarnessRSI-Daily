# SOURCE.md — 2611.18856（SIM：自改进记忆迁移）

- 论文：arXiv:2611.18856v1（缓存：research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.18856.txt，v1 html complete，sha256 816f322c…）
- 海报为非作者重绘；全部数值出自论文正文，未复现、未运行论文代码。

## 逐数溯源

| 海报数字 | 论文位置 | 原文依据 |
|---|---|---|
| 配对 10 组 mean +2.36 [1.05, 3.68]，p=0.003，9/10 胜 | 主实验（配对续优化） | coding 续优化配对实验，SIM 相对无 SIM 基线 |
| 6/6 跨数据集 Full SIM 最高；超 Harness Transfer 2.43–4.35 点、Problem-Only 0.20–6.06 点 | 跨数据集迁移表 | 六个目标数据集、三种迁移臂对照 |
| 4/4 跨模型全胜；Opus→Gemini 领先 3.60–11.33；workspace 84.75 vs 73.42（原 harness）、68.41（改后 harness 无 SIM） | 跨模型迁移表 | 同任务换模型三臂对照 |
| 世代链 TB2.1：seed 75.72 / FewShotAll 72.92 / Harness-only 74.12（冷启动 75.92）/ Full SIM 77.92 | 源改进≠目标起点消融 | 直搬改进低于 seed；唯 Full SIM 净胜 |
| 4Argon 95.6 vs 94.8（−0.8） | 世代链 | 世代自改进收益衰减并转负 |
| 统一合成 75.24 vs 分模型 75.20（held-out） | 合成策略消融 | 差异可忽略 |
| SIM 记录四栏（问题/所选修改+理由/预测vs实测/评估背景） | 方法节 | 按 harness 问题组织 |

## 机制卡片语义

"问/改/测/境"四栏台账为本项目对论文 SIM 记录结构的重绘排版，栏名与分栏为本项目措辞；各栏内容语义与论文方法节一致。

## 缓存边界

缓存为 v1 html complete（materials/2611.18856.json 记录 v1 html complete, sha256 816f322c…），主实验、消融、限制节均在内；海报未引用缓存外数字。
