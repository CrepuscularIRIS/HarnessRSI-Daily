# SOURCE — 2605.06614

- 论文：SkillOS: Learning Skill Curation for Self-Evolving Agents（Ouyang et al.；Google Cloud AI Research / UIUC / MIT）
- 版本：arXiv:2605.06614**v1**（2026-05-07）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2605.06614.txt`（正文 + 附录 A–F 已通读，含待补项附录 B.3 与评测期协议）
- 初筛记录：L1 `batches/b044.jsonl` → L2 `batches/l2c15.jsonl`（P3 / confirmed / to_l3）；L3 `l3-final-2.tsv` #3、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 问题 | 手工整理不可扩展；规则式操作无下游反馈；RL 工作或教“用”技能、或短任务流 | §1 第 3 段；§2 |
| 研究动作 | 分组任务流（ALFWorld 用 6 类任务类型，数学由 Gemini-2.5-Pro 标注 5 维属性）；组大小 Random(5,12)；每步库清空 | §3.2.1；附录 B.1 Table 4；附录 B.2 |
| 拆解图 ① | 首题用空库，r_task = 第 2…|G| 题平均成功 | §3.2.2 “Task outcome reward”；Algorithm 1 |
| 拆解图 ② | 技能 = 单个 Markdown（YAML frontmatter + 正文）；insert/update/delete_skill | §3.1 |
| 拆解图 ③ | 执行器冻结、BM25 检索、ReAct；测试换 Qwen3-32B、Gemini-2.5-Pro、Gemini-3.1-Flash-Lite | §3.1；§4.1；附录 C.1 |
| 技能卡片 | search-fallback、look-under-lamp、元技能——按附录 Figure 17、19 及 §5 Fig.5 描述意译，示意 | 附录 C.2；§5 |
| 整理者 | Qwen3-8B、GRPO、组大小 8、lr 1e-6、去 KL；输入为轨迹 + 执行器自评对错 + 检索技能 | §3.1 “Skill Curator”；§3.2.2；§4.1 |
| 奖励式 | r = r_task + 1.0 r_fc + 0.1 r_cnt + 0.05 r_comp；r_cnt 由 Qwen3-32B 评委给出 | Eq.1；§4.1 λ 设置；附录 A.3 |
| 8 条整理序列 | 同组 N 条完整整理序列、组内相对优势 | §3.2.2 |
| 结果条件 | 同冻结执行器、检索预算、步数上限、解码温度；3 次运行；valid_seen 140 题 | 附录 B.3.2、B.3.3 “Evaluation protocol”；附录 B.3.1；Table 1 |
| Qwen3-8B 执行器 | 47.9±1.2 / RB 55.7±3.1 / base 53.1±2.5 / gemini 50.7±3.6 / SkillOS 61.2±4.6 | Table 1 Avg. SR |
| Gemini 执行器 | 66.4±2.0 / MemP 74.3±3.4 / base 70.7±3.0 / gemini 79.3±2.6 / SkillOS 80.2±3.1 | Table 1 Avg. SR |
| 差值 | +8.1、+10.5、+13.8、+9.5、0.9 | 本项目按 Table 1 算术。注：正文 §4.2 写 Qwen3-8B 执行器相对 base “+7.9”，但 Table 1 差为 61.2−53.1=8.1，画报采用表值 |
| 消融 | 61.2 / w/o grouping 57.3 / w/o r_cnt 58.6 / w/o r_comp 60.0（无标准差） | §5 Table 3 |
| 行为 | 早期 insert 主导，update 上升，delete 少量略增；元技能出现 | §5 Fig.4、Fig.5 正文 |
| 其他任务 | WebShop SR 16.5 / base 13.6 / 无记忆 9.8；推理平均 73.8 / 无记忆 69.6；AIME 各 30 题；推理增益较小 | Table 2；附录 B.3.1；§4.2 |
| 限制 1 | valid_seen；评测期按执行器自评在线改库；评测是否从空库开始原文未说明（仅训练写明“initialize an empty SkillRepo”） | 附录 B.3.1；§3.1、§4.1 “Task outcome signal”；Algorithm 1 |
| 限制 2 | 16×H100，ALFWorld 约 3 天、推理 2.5 天、WebShop 5 天；r_cnt 来自 Qwen3-32B | §4.1；附录 A.3 |
| 限制 3 | Avg. SR 标准差 0.7–4.6（Table 1 各 Avg. SR 下标范围）；复合奖励无单条信用 | Table 1；L2 biggest_gap |

## 示意与重绘

- 分层拆解图为示意（层次关系依 §3 与 Algorithm 1），卡片内容为意译。
- 条形与误差棒按 Table 1 均值 ± 标准差重绘。
- 本项目未运行实验或复现结果。

## 核对结论与展示收窄

- 与 L2 记录一致，无 correction。
- **展示收窄**：selection-002 终选表写“迁移到 Gemini 执行器 66.4→80.2，优于 Gemini 自己当 curator”。核对 Table 1：Gemini 执行器下 SkillOS 80.2±3.1 对 Gemini 整理者 79.3±2.6，差 0.9、误差重叠；明显优于 Gemini 整理者的只有 Qwen3-8B 执行器（61.2 对 50.7）。画报按此收窄并明写“不能说更好”。
- 消融未报标准差，去分组 −3.9 小于完整方法标准差 4.6，画报注明。
- 待补项“评测期是否从空库开始”：原文未写明，记为未知，画报限制中注明。
