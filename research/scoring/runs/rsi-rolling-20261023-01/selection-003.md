# L3 选题第三期 — run rsi-rolling-20261023-01

- 规则：`problem-core-v1.1`（PROBLEM_CORE §4 `to_l3`、SELECTION.md、OPUS_REEL_PROMPT.md）。执行：Opus 5.5 单席，2026-10-24。
- 编号：本仓 Reel 第三期（第一、二期为旧 run `rsi-l1-20261022-03` 的 [selection.md](../rsi-l1-20261022-03/selection.md) 与 [selection-002.md](../rsi-l1-20261022-03/selection-002.md)，已入选 15 篇不再重复入选）。
- 候选池：本 rolling run 的 `inc-l2-01` / `inc-l2-02` 批次中最新记录为 L2、`P3 / confirmed / to_l3` 的全部 5 篇（无 P2 编辑入池项）。本期硬上限 3 篇。
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/<pid>.txt`（均为 arXiv v1 的 HTML 转文本）。
- 产出：本文件 + `reel/<pid>/` 三套成品。未改动任何 L1/L2 批次记录。

## selection_cutoff 说明

本期结果只代表这 5 篇候选、按本期 3 篇上限与去重口径的选择，不否定落选论文。问题档位是本项目的阅读判断，不是审稿结论，Reel 不呈现为权威评分。

## 候选（5）

| pid | 标题（简） | tier / evidence | q3 | 族 | 主卡 | L2 批次 | 原文核对 | 结论 |
|---|---|---|---|---|---|---|---|---|
| 2610.30499 | Can LLMs Improve Their Own Harness? (ARC-AGI-3) | P3 / confirmed | judgment | F1, F3 | diagnose_self_improvement | inc-l2-02 | 正文 + 附录 A–E 通读 | **入选** |
| 2610.28798 | Explicit Feedback Contract | P3 / confirmed | judgment | F2, F4 | diagnose_self_improvement; coevolve_the_evaluator | inc-l2-01 | 全文通读（无附录） | **入选** |
| 2610.29005 | VeriEvolve | P3 / confirmed | capability | F2, F4 | coevolve_the_evaluator | inc-l2-01 | 正文通读 + 附录 A.1, D.2–D.4, E.6–E.7 | **入选** |
| 2610.28815 | Successive Scale Racing (SSR) | P3 / confirmed | judgment | F5, F2 | abstract_experience_into_guidance; search_agent_architecture | inc-l2-01 | 正文 + 附录 A.6, B–E 通读（G 为最终 harness 原文，未逐行读） | 落选（证据边界 + 同题） |
| 2610.30042 | HGM-Dual | P3 / confirmed | judgment | F1, F3 | attribute_and_patch_incumbent; search_agent_architecture | inc-l2-02 | 全文 + 附录 A.1–A.6 通读 | 落选，**correction C1** 退回 |

## 排列与取舍

1. 全部 P3，档位无先后；q3 上 capability（29005）与 judgment（其余）并列不分先后。
2. 先剔除 2610.30042：发现 L2 依据的统计单位读错，写 correction 退回（见下），本期不入选。
3. 余下 4 篇取 3。判断顺序：问题是否清楚、证据是否直接、与已有 15 张及本期其他入选的机制是否重复。
   - **2610.30499**：问题最清楚、证据最直接——27 条独立构建谱系、每个快照都在从不参与适应的 20 个游戏上评测、整谱系自助区间、失败与修复全部入账，且有单 harness 10 次重跑给出评测噪声尺度。首选。
   - **2610.28798**：与 30499 同属 diagnose_self_improvement，都碰到“开发/验证涨分高估真实改进”。保留理由：两篇问的是不同环节——30499 测的是更新者能力（谁来改、改得是否迁移），28798 改的是反馈通道本身（代理能看到什么、何时停），并给出一个真实增益按构造为 0 的对照和一条可直接部署的发放规则。机制不重复，按 SELECTION“已覆盖的卡只在机制明显不同时再选”的口径保留，记为同卡双选。
   - **2610.29005**：coevolve_the_evaluator 卡已有 HASTE（2610.02920）。保留理由：HASTE 演化的是安全规格与攻击用例，VeriEvolve 合成的是任务 fitness 用的可执行状态评估器，核心证据“生成套件 141/141 对 搜索状态 113/122”在已有画报中没有对应；q3=capability，也补足本期全是 judgment 的倾斜。
   - **2610.28815** 落选，理由见下。
4. 族覆盖：本期主族 F1×1（30499）、F2×2（28798, 29005）。F5 无入选（唯一 F5 主族候选 28815 落选），F3 只作次族出现。

## 入选（3）

| # | pid | 族 | 主卡 | 问题 | 关键动作 | 证据（一句） |
|---|---|---|---|---|---|---|
| 1 | 2610.30499 | F1/F3 | diagnose_self_improvement | 能搭出 harness 是否意味着能把它改得在未见任务上更好 | 固定模型与编码引导的谱系协议，H0/H1/H2 全部冻结、全部在 20 个留出游戏上评测 | 开发 +8.42、留出 +2.80 [−1.44, 7.35]、差距 5.62 [1.78, 9.77]；15 升 12 降 |
| 2 | 2610.28798 | F2/F4 | diagnose_self_improvement | 代理每轮读精确验证分时，选择噪声会被报告成改进 | 反馈契约：配对标准误阈值才公布新分、按更新事件计耐心、测试只评一次 | 无信号对照上精确分数报告 0.0157（测试 −0.0006）并用满 30 次；契约差 0.0000、10.4 轮停 |
| 3 | 2610.29005 | F2/F4 | coevolve_the_evaluator | 有状态工具任务没有现成 fitness，合成评估器在生成套件上的全对掩盖缺口 | 评估器先行三阶段：合成→冻结指导工作流演化→强弱执行器状态差修补 | 生成套件 141/141 对搜索状态 113/122；弱执行器 6/30→18/30；3/3 假阳性修掉但只 1 例随后做对 |

### 逐篇原文核对状态与展示边界

1. **2610.30499**：§5 数字、Table 3 逐行（本项目复算均值 24.54/25.87/27.34、升 15 条，Sonnet #3 表值平局按作者未取整口径为降）、Table 5/7/8/10 均核实。边界：一个基准、5 个开发游戏、两次修订；每快照只评一次（单 harness 重跑 SD 3.99）；无统一推理预算，模型排名只是描述；去掉 r11l 差距降到 3.02；修订行为标注为 LLM 双编码、未经人工比对。与 L2 一致。
2. **2610.28798**：Table 2/4/5、Algorithm 1、§4.3 命题与末段均核实。边界：真实任务差距只收窄约一成、三 seed、表格数据；保证只覆盖固定阈值，部署规则是启发式，η_min 下限说明与 Algorithm 1 不一致且常数未给；文件隔离只是协议规定；收益归于“发放 + 停止”整体，没有同轮数对照；Claude 骨干两接口停止轮相近且为旧协议。L2 未提及的一点：§5.3 Table 3 的提交方式是 Signed Boosting，不是主实验的 Codex 代理，画报已分开说明；不构成 correction。
3. **2610.29005**：Table 1–4、14、17、18、22 核实。边界：不是无 verifier 闭环（准入、假阳性发现、F⁺ 都依赖外部 verifier；回溯替代触发误报 10/18）；每个 Filesystem 条件一次运行、无等预算搜索基线（作者承认部分增益可能来自反复采样）；留出状态是按评估器排名保留的每轮最佳，非独立样本；挑战集与评估器同为 Claude；S1 成本未记录。与 L2 一致。

## 落选（2）

### 2610.28815（SSR）——证据边界 + 同题去重

- 原文核对：§3 预研、§6 主表与消融、附录 B–E 通读。L2 判断大体成立，不写 correction，但证据不足以支撑画报的核心叙事“更多任务反而更差”：
  - 退化现象来自 §3 预研（只在 SWE-Pro-V、一个执行设置，基线在不同池大小下的预算是否随之调整未说明）；SSR 自己的“40→200 任务单调上升”实验同时按比例放大了执行预算与验证配额（附录 C Table 2：200/400/600/800/1000、b_v 4/8/12/16/20），不能读成纯数据量效应。
  - 组件消融（多尺度 +1.4/+1.3、RER +1.0/+0.7）均为单次演化；主表领先 1.3–3.0pp，三次运行、未做显著性检验。
  - 正文 §6.3 两处把任务池增长图引为 Figure 6a，与 Figure 5 的图注不一致；资源增长实验中 MGM 在 800 预算时 51.0%，低于主表初始 harness 57.7%，口径未解释。
- 同题：与第一期 Combee（2604.04247，“上下文过载”下更多并行反思使质量崩塌）同属 abstract_experience_into_guidance 的“更多经验不单调有益”问题族，Combee 已有画报，且其数量/质量下降有自测直接证据。
- 去向：保持 L2 原判（P3/confirmed），列为下期备选；若作者补出等预算的任务池增长对照与多次运行的组件消融，可重新考虑。

### 2610.30042（HGM-Dual）——correction C1，退回

见下。修订完成前不入选。

## Correction（不改批次记录；退回 Sol 单篇修订）

- **C1 · 2610.30042（HGM-Dual）**：L2 判 `q4_fit=fits`、`evidence_status=confirmed`，subcard H17 Step 5 写“表1/2有spread”，并把表 3/4 的单项对照当作“直接排除仅更多分支”的证据。原文核对发现统计单位读错：
  1. 全文没有说明每个方法跑了几次独立搜索。Table 1/2 的“±”不是搜索间方差——种子 harness（评估预算 0、不经搜索）同样带 ±（travel 76.46 ± 0.22、shopping 81.91 ± 1.17），HGM 在 1k 与 4k 预算下的数值与 ± 完全相同（77.06 ± 0.53 / 83.12 ± 0.27），说明 ± 只是同一最终 agent 的重复评测波动。因此每个方法实际可读作一次搜索。
  2. 关键归因对照都是单次结果：去掉 error-conditioning 的 87.68 对 90.35 只在 shopping、1k 预算（Table 4，与 Table 2 shopping 列同源）；evolution context 的 31.3%→41.0% 只在 travel（Table 3），编辑数未给。travel 1k 时 HGM-CF（84.90）反而高于 HGM-Dual（83.83）。
  3. 动机统计（41.8% 重复编辑模式、19.4% 指向父代未失败类别、64.2% 保留主导错误）来自一次 HGM shopping 搜索的 67 个提案；类别标注规则“同一规则”但未说明由人工还是模型完成。
  4. 总体分（Table 1/2）含 60 道训练题；case accuracy 无任何不确定性；弱骨干 Mistral 上 case accuracy 1.6%→1.6%（120 题中 2 题）。
  - 建议：`evidence_status` → `pending_experiment`（需要每方法多次独立搜索、同预算下的 context / error-conditioning 消融，以及只在 60 道未见题上的对比）。问题本身（编码自改迁移到规划时编辑冗余、不对准）仍成立；q3 是否仍为 `judgment` 请 Sol 在补齐统计单位后复判——若只剩“定向编辑 + 谱系上下文让同接口 HGM-CF 再提高 2.6–3.7 分”，更接近 `incremental`。旧记录保留。

## 待补与其他

- **待补清单（priority=high 但未确认）**：本 run 内 2610.29303、2610.30184 为 `P3 / pending_experiment / to_l2`（缺口见其 L2 biggest_gap），不在本期候选池；L2 预算外另有 13 篇 to_l2（progress.md）。本步未处理。
- **漏检抽查**：本 run 两班次抽查名额均为 0（预算×10% 取整），无改判记录；本步未复核。
- **下期备选**：2610.28815（见上）；2610.30042 待 C1 修订结果。
- **Reel 成品**（均已完成实际视觉 QA，状态 ready；详见各目录 QA.md）：
  - `reel/2610.30499/`：poster.png（1600×2263）/ poster.pdf（单页）/ poster.html / SOURCE.md / QA.md
  - `reel/2610.28798/`：同上
  - `reel/2610.29005/`：同上
- 索引更新：`reel/README.md` 新增本期 3 条；仓库 `README.md` 只改头部统计行 Reel 数（15→18）与 Featured Reel 段落 / 墙。README 内部旧表数字的已知矛盾本次未修。
