# SOURCE — 2610.05437

- 论文：TeleTune: Evolving Agent Skills From Offline Telemetry（Chen, Stengel-Eskin, Chen, Llado, Counts, Bansal, Van Durme, Jhamtani, Verma；UNC Chapel Hill / Microsoft）
- 版本：arXiv:2610.05437**v2**（2026-10-06）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2610.05437.txt`（正文 + 附录 A–F 已通读，含待补项 Table 3/4 原值与扰动附表 Table 7）
- Fig.3 读图：钉定文本只有正文数值。本项目下载 arXiv HTML v2 图资源 `https://arxiv.org/html/2610.05437v2/optimization.svg` 渲染查看，得到在线检查点所在步（1、10、20、27）与 Q 的大致轨迹；私有缓存未提交。
- 初筛记录：L1 `batches/b072.jsonl` → L2 `batches/l2c01.jsonl`（P3 / confirmed / to_l3）；L3 `l3-final-2.tsv` #4、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 问题三卡 | 无目标、不可重放、交织 | 摘要；§1 |
| SkillOpt 对比 | SkillOpt 用已知目标并在线执行验证每个编辑 | §1 第 4 段；§5 |
| 研究动作 | 推断目标；teacher forcing；skill-guided progress Q（Eq.2）；dev 平均 Q 严格上升才接受；最终库冻结后在线测试 | §2.1、§2.2 Validate、§2.4；附录 C Table 5 “Acceptance rule” |
| 胶片帧 | 示意；改写自 §2.2 被接受技能的案例（用户留空 assigned to 并点 Run，预测器填了用户名）；字段名 “Install status” 为示意 | §2.2 “Edit” 段 |
| 不计分步 | CSS 选择器、nth=0 等只进历史不计分 | §2.1 “Offline Evaluation by Teacher Forcing” |
| 首错交给优化器 | 每轨迹第一个错误；含推断目标、历史、预测与记录；每案例显示最近 8 个动作 | §2.2 Reflect；Table 5 “Failure cases per step” |
| Reflect / Edit 数值 | 每步至多 6 个失败案例（Q 最低优先）、至多 3 处编辑；看得到被拒编辑 | Table 5；§2.2 Edit |
| 冻结 → 上线 | 最终库 + 工作流检索 8 条示范 | §2.3、§2.4；§3 Baselines（k=8） |
| 引用技能 | “In list filters, if the needed value is absent …” | §2.2（原文引用） |
| 2×2 析因 | L1/L2/OM2W：65.1/54.2/72.9；66.8/52.6/74.3；83.7/60.8/75.1；92.3/61.8/80.6；+18.6/+6.6/+2.2；+1.7/−1.6/+1.4；+8.6 | §4.2 Table 3 及正文 |
| 基线表 | Naive 45.6/48.0/63.9；AWM 75.7/51.9/71.9；AWM+Random-k 80.3/60.4/70.2；TeleTune 92.3±2.0/61.8±2.8/80.6±4.1 | Table 1 |
| L2 / Mistral | L2 领先 1.4；Mistral-3.5 与最强基线持平（L1 +0.5，L2 −1.1） | §4.1；Table 2 |
| Q 曲线 | 工作流阶段约 50%；步 10 由 51.3 升到 66.9；最终 73.0；在线 74.1→83.1→88.7→92.3；32 步 14 步接受，后 5 步无接受未画 | §4.2 首段；Fig.3 图注；Table 4（Steps 32、Ckpt. 14） |
| 读图近似 | Q 步 1 ≈49、步 20 ≈70；检查点位于步 1/10/20/27 | Fig.3（arXiv HTML 矢量图读图，画报以空心点标示） |
| 任务交织 | q=1.0 L1 TeleTune 74.8 对 Random-k 75.9；AWM 49.3；L2 TeleTune 62.1；q>0 单种子 | §4.2；附录 E Table 7 及表注 |
| 优化代价 | L1 173.84M token，预测器占 99% 以上（优化器 <0.5%）；在线验证约 2.8B、16 倍；L2 约 75 倍、M2W 约 5 倍 | §4.2 Table 4 及正文 |
| 推理代价 | L1 每回合 636.9K 对 343.4–386.1K；库 56 条技能约 6.4K token；Random-k k=30 用 504.2K 得 63.7 | §4.2 末段；附录 E Table 8 |
| 限制 1 | WorkArena 用成功的 oracle 轨迹；Mind2Web 为标注者录制；交织为人工构造；WorkArena 测试是训练模板的其他种子 | §3 Dataset；附录 D 首段与 Table 6 注 |
| 限制 2 | 推断目标由整段轨迹写成，提示禁止描述动作序列 | §2.2 Reflect |
| 限制 3 | 65–85%：636.9/386.1≈1.65，636.9/343.4≈1.85（本项目算术） | Table 8 |

## 示意与重绘

- 胶片帧为示意；Fig.3 曲线按正文数值重绘，读图近似点已标空心。
- 2×2 析因与基线表按 Table 1、Table 3 数值重排。
- 本项目未运行实验或复现结果。

## 核对结论与展示补充

- 与 L2 记录、selection-002 一致，无 correction。
- 补读附录后新增两条展示边界（selection-002 未写）：① Table 7 中 q>0 的全部格子为单种子；② WorkArena 测试实例是训练任务模板的其他种子，迁移只在同模板内。两条均已写入画报。
