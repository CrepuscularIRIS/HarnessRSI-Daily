# SOURCE — 2611.15276 Verify by Doing

原文：arXiv 2611.15276v1。全文缓存：research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.15276.txt。主骨干 DeepSeek-V4-Flash-0731（全角色冻结权重），3 rounds×2 执行，离线评分 GPT-5.6-sol xhigh，3 runs mean±SD。

| 海报数值 | 原文位置 |
|---|---|
| AutomationBench 总分 VbD 37.0±1.9 / RQGM 33.7 / HGM 31.7 / RHI 31.7 / RHO 27.7 / SP 27.7 / BoN 31.2 / Base 22.3 | 主实验表（AutomationBench 600 任务） |
| 六域 Finance 53.3 / Sales 32.7 / Marketing 52.0 / Ops 56.3 / Support 18.0 / HR 9.7（海报引用 Support/HR 弱项） | AutomationBench 分域表 |
| τ³Banking VbD 49.5±2.1，vs Base 35.1（+14.4），RHI 45.4 / HGM、RQGM 41.2 / RHO 38.8 / BoN 40.5 | τ³Banking 节主表 |
| GDPval 133 任务九 sector 全胜，rubric 82.4% vs RQGM 80.1% | GDPval 节 |
| 消融：w/o active verification 34.3（−2.7）、w/o Evaluator evolution 35.4（−1.6） | 消融表 |
| 回归拒绝 89.3% vs RQGM 71.2%（+18.1pp），precision 77.6 vs 77.0 | 回归检查节 |
| 固定 BoN 池只换 Evaluator：pass +4.6pp、partial credit +2.4 over BoN | 固定池实验节 |
| 外部反馈上界† 42.6 / 56.4 | 作者标注构造性参照（上界讨论节） |
| 限制：同骨干共享错误、任务结束清空 harness（within-task only） | 原文 Limitations L2076 附近 |

海报中"挑对先于写好"为本项目概括，非作者表述。本项目重绘，非作者海报，未复现实验。
