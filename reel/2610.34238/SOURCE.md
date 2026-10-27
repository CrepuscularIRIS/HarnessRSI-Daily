# SOURCE — 2610.34238

- 论文：Δτ-Bench: Pushing Agents Toward a Moving Capability Frontier（Shuofei Qiao, Xuanguang Pan, Yijun Chen, Wendi Feng, Bin Wu, Runnan Fang, Yuqi Zhu, Shumin Deng, Emine Yilmaz；浙江大学 / UCL）
- 版本：arXiv:2610.34238**v1**（cs.CL，2026-10-25）
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/2610.34238.txt`（PDF 转文本，sha256 `1f15bf68…0b9282`）。正文 §1–§8 与附录 A（构造、指标、统计）、B（基线）、C（STEWARD 细节）通读；附录 D 提示词浏览。图中数值（Fig. 3、4、6、7）只采用正文写出的数字。
- 初筛记录：L1 `batches/inc-l1-04.jsonl` → L2 `batches/inc-l2-05/06.jsonl`（P3 / confirmed / capability / to_l3）；L3 `selection-005.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 结论（画报展示口径）

在一个合成的、六版本演化的工具生态里（42 领域、1,588 任务），最强模型 / harness 成功率 42.3%，检索召回高、精确低，成功率高不等于路径高效；四种现有技能方法 v1 有益但跟不上后续版本。STEWARD（按工具依赖增量维护三级技能 + 按需供给工具与技能）六个版本成功率均最高；同一 v1 库下增量维护优于冻结与全量重建且维护 token 更少。全部为单次运行、合成生态、构造空间内的“最优”。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 页首 | 42 领域、1,588 任务、六个生态状态；最强 42.3%；技能方法初始收益不持续；STEWARD 概述 | Abstract（L13 起）；§1 |
| 01 线路图 | 各版本工具数 892/841/837/799/858/890；新增 / 退役 / 修改计数 | Table 3（L2549–2567 附近） |
| 01 文字 | 三类变换；多合一只合并已验证轨迹相邻调用；并存或替换；覆盖校验；描述扰动；1,191/397；9,528 实例 | §3.2（L519 起）；附录 A.2（L2243 起）；§3 首段（L472） |
| 02 路径示例 | f1→f2→f3→f4 4 步成本 4；f1→m→f4 3 步成本 5；权重 f (1,1)、m (1,3)（**按 Fig. 2 示例重绘**） | Fig. 2（L453 附近，L417） |
| 02 文字 | 参考路径只在构造的实现空间内最优；DP 求步数 / 成本最小；SR 按状态差覆盖；SPE / IDR / DAR 定义 | §3.2（L519 起，L552）；§3.3（L706 起）；附录 A.3（L2330 起） |
| 03 表 | Codex-GPT-5.5、Gemini-3.6-Flash、GPT-5.5、Claude-Sonnet-5、DeepSeek-V4-Pro、GLM-5.2 的 SR / R / P / Step-SPE / Step SPE/SR | Table 1（L575 起） |
| 03 文字 | 召回 90.36 对精确 19.90；DeepSeek-V4-Pro 与 GLM-5.2 对比；逐级提供工具 → 上升，Oracle Path 无进一步提升 | §4.1；§4.2 / Fig. 3（L1050–1065 附近） |
| 03 注 | 另三个开源模型 SR 27.00–30.10 | Table 1 |
| 04 | DeepSeek-V3.2 为任务模型；v1 四法均优于 No Skill；AutoSkill v3、v5 低于 No Skill；v3 EvoSkill/AutoSkill DAR 为 0 对 No Skill 11.11/10.25；No Skill v2 最高 Cost-IDR、v5 两项 DAR 最高；SkillOpt ~3,000K token/任务、2–3 倍 | §4 Setup（L1003）；§4.3（L1206–1212） |
| 05 结构图 | 三级技能、规划技能固定、只用验证成功轨迹局部编辑、失活保留；供给四步、retrieve_tools / explore_capabilities ≤3 次、只放行目录内已检查工具 | §5（L1221 起）；附录 C（L2738 起） |
| 05 文字 | 平均 SR 39.04 对 36.36；维护 token 1.2–5.5 倍；IDR +4.04/+3.69，DAR +5.28/+4.76 | §6（L1514–1519）；Fig. 6 标题（L1477） |
| 06 条形 | Table 2 两模型冻结 / 重建 / 增量的平均 SR 与维护 token；+2.22/+1.82；−39.5%/−30.4%；GPT-5.5 重建 38.99 < 冻结 39.60 | Table 2（L1526 起）；§6（L1620） |
| 06 文字 | 供给消融：工具搜索 SR +8.65、F1 +4.14、Step-DAR −2.76；合用相对工具搜索 DAR +11.41/+9.30、F1 +4.90 | §6 / Fig. 7（L1643–1647） |
| 07 限制 | 合成领域与 LLM 生成；成本为 LLM 赋 1–10 分（L552）；用户模型 DeepSeek-V3.2（L1003）；无种子 / 区间（全文未见） | §3.1–3.2；§4 Setup |
| 07 核对备注 | Table 2 增量维护 36.83 与 Fig. 6 STEWARD 39.04 口径不同、原文未说明 | Table 2；§6（L1514） |
| 本项目读法 | 技能跟随工具目录、局部编辑、以当前可达最优为参照的指标 | 本项目阅读判断 |

## 自行绘制 / 示意说明

- 01 线路图按 Table 3 计数重绘；站间距等距，不表示时间。
- 02 路径为 Fig. 2 示例的重绘（论文示意，不是实验数据）。
- 04 DAR 条形只画正文给出数值的 v3 三项；06 条形按 Table 2 数值等比（轴从 30 起，已在图中标注）。
