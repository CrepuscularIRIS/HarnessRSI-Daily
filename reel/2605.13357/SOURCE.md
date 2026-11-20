# SOURCE — 2605.13357 AI Harness Engineering

原文：arXiv 2605.13357v1（2026-05-13）。全文缓存：research/fulltext/2605.13357.txt。**注意：缓存为节选本（多处 `[...]` 截断）**，本表逐项标注可证性。

| 海报内容 | 原文位置 | 可证性 |
|---|---|---|
| 「模型–harness–环境」分析单元；harness 为中介基底 | Abstract + §Introduction + §A runtime view | 逐字可证 |
| 11 项组件职责：任务规范/上下文选择/工具访问/项目记忆/任务状态/可观测性/失败归因/验证/权限/熵审计/干预记录 | Abstract + §The AI Harness Engineering（Table 1 枚举段） | 名称逐字可证 |
| Table 1 结构：职责 × 运行时契约 × 缺位失败模式 × 证据工件 | §The AI Harness Engineering "Table 1 enumerates..." | 结构可证；海报中每格的具体契约/失败模式措辞为**本项目按原文 Introduction 失败列举概括**，非逐字引用 |
| H0 逐字定义：只有任务描述+仓库文件；无工具注册、无项目记忆、无验证协议 | §A controlled harness ladder L18 | 逐字可证 |
| H0–H3「逐级暴露运行时支撑；固定任务/仓库/模型把 harness 贡献与模型贡献剥离」 | §A controlled harness ladder 首句 + Contribution (ii) | 逐字可证 |
| H1–H2 具体定义 | —— | **缓存截断不可得**，海报如实标注 |
| 受控验证任务：低级别只产最终 patch；高级别产复现日志/失败归因/确定性需求检查/结构化验证报告 | Abstract + Contribution (iv) | 逐字可证（定性） |
| 8 类 trace：action/tool/context/verification/failure-attribution/intervention/entropy/outcome | §Trace-based evaluation | 逐字可证 |
| 5 类结局定义（autonomous_verified_success 等，含 unverified_success 定义「patch 对但证据不足」） | §Trace-based evaluation Outcome taxonomy 段 | 逐字可证 |
| 5 设计原则 P1–P5（显式资源/可追溯中介/需求级验证/先归因再恢复/维护与熵入账） | §The AI Harness Engineering Five design principles | 逐字可证 |
| M-HIR：missing-harness human intervention rate；人指文件=上下文缺位、人解读失败=可观测性/归因缺位 | §A runtime view "Human intervention as runtime signal" | 逐字可证 |
| 8 类失败分类、熵审计 0–3 级 | §A runtime view + §Trace-based evaluation | 名称可证 |
| 「仅一个受控验证任务」 | Abstract/Contribution (iv) 口径 + 缓存未见其他实验表 | 本项目核验结论 |

海报标题「别问模型行不行，问 harness 给没给到位」与职责矩阵格内措辞为本项目概括。本项目重绘，非作者海报，未复现实验。
