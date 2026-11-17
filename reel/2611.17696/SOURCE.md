# Co-Sight Harness — 海报来源

- 论文：**Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents**，Luyao Wang、Xijun Zhu、Zhaohui Hao、Xiwen Zhang、Xingyu Wen、Weishan Li、Yuyang Liao、Yanqin Gao、Yongsheng Du、Lingjun Huang、Shaowei Zhao、Gang Li、Qifan Yu、Baoli Wang。
- 固定版本：[2611.17696v1](https://arxiv.org/abs/2611.17696v1)；[原文 HTML](https://arxiv.org/html/2611.17696v1)。未据此宣称会议录用。
- 本地来源：`research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.17696.txt`；SHA256 `f416bb980a88058fea33e061bad7b90ebc5f3c98f564904d42519ffb5599ba34`。版本及抓取记录在 rolling run 的 `materials/2611.17696.json`。
- 上游：`rsi-rolling-20261023-01/batches/inc-l1-20.jsonl`、`inc-l2-22.jsonl`；规范 `problem-core-v1.1`；[第16期选题](../../research/scoring/runs/rsi-rolling-20261023-01/selection-016.md)。
- 制作日期：2026-11-17；本席模型按会话环境报告为 **gpt-6-astra**（fable 槽位，未独立探测后端），不是按提示词角色名记作 Opus 5.5。

## 图中事实与来源

| 图中内容 | 原文位置与读法 |
|---|---|
| 固定骨干；版本化外部资产；控制线与知识线 | §4 的资产、编译器、确定性执行器与只读审计器设计。图是项目机制示意，不是作者原图或实测因果路径。 |
| 完成门、外部状态、状态机；双引擎检索、语义对齐 | §4；§5.7 的 additive/subtractive 定义。控制和知识是组件组合，不能将每一箭头解释为单独估计的效应。 |
| `Reg(K′) ≥ Reg(K)`、`ΔS ≥ 0`、人工批准 | §4 资产修订准入规则的简写；不是已验证的全程安全定理。确定性检查与语义正确分开。 |
| 自动审计提出资产修订仍为未来工作 | §6。当前图不声称已实现自主 RSI，更不声称改进器递归变强。 |
| B0：50.0%、F1 .267、440分钟；B1：75.0%、.334、250；B2：60.0%、.519、400；B3：90.0%、.569、170；B4：60.0%、.336、415 | §5.7 表7，本地原文 L3287–3853 覆盖实验设置和表7–8。120配对案例、13次运行；表中为报告均值，F1由报告平均P/R计算。F1不是成功率。 |
| B3 对 B4 +30 pp | 表7：90.0−60.0＝30.0个百分点。B4是计算量匹配的长提示／重试基线；不是30%的相对增长。 |
| 去完成门／返工：88.3→65.8%，−22.5 pp | 表8 A1 对 A2，另120案例×13次运行；不能与表7合并或加总效应。 |
| 去检索／语义对齐：.569→.371，−.198 | 表8 A1 对 A5；是F1绝对差，不是成功率差。 |
| 去独立评价会虚高 | 表8 A4及解释：F1 .582不能当作高于完整系统.569的真实内容质量。 |
| “先定位失败属于哪条线” | 项目阅读结论，由上述两组消融支持；不是作者验证过的通用更新算法。 |

## 边界

全文与附录已阅读。人工资产开发与最终测试隔离未完整交代；正文未给可审计的精确模型快照名称。现场50→100%的完成改善是组合干预，未用作单组件因果证据。两组消融案例独立，不能把13次运行当作1560个独立案例或在此宣称统计显著。审计语义与全运行安全性未获独立验证；门控设计不是无回归保证。

本图全部数值为作者报告，未运行论文代码、未独立复现。选入依据是组件归因与可操作的控制／知识区分，不把资产留存自动升级为后来任务已因自主修订变好。

## 编辑与输出

`poster.html` 是可编辑中文源，携带相对路径 `assets/fonts/poster.woff2`；移动时保留整个目录。字体许可见 `assets/fonts/LICENSE.txt`。`poster.png`、单页 `poster.pdf` 为本地浏览器渲染；[QA](QA.md) 记录失败首版和一次修订。无作者机构标识，无作者海报冒充。
