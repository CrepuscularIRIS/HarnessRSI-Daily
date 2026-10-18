---
id: rrsi
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses"
authors: "Peng Xia et al."
first_seen: 2026-09-21
arxiv: "2609.24972v3"
openreview: null
code: "https://github.com/google-research/rrsi"
code_commit: be50316e1db05914068a973f322770ef08ed7ba1
license: "Apache-2.0"
venue: "arXiv preprint"
tier: A
evolved: [prompt, skill, tool, workflow, memory, code, config]
feedback: [ground_truth, execution, llm_judge]
evidence_level: retained
held_out: yes
budget_matched: partial
leakage_risk: low
code_status: released
checked: 2026-10-18
---

## 一句话
冻结 backbone，让 LLM proposer 改 agent harness 的源码（prompt、control flow、tool、skill、memory、sub-agent、config 都能改）。信号是 evolve set 上的 verifier 分数（单元测试 / LLM judge 按 rubric 打分 / 仿真器）。候选要先过 leakage critic，再满足噪声下限和 token 成本规则，才能取代 incumbent。

## 机制
- **提出**：proposer 读 analyst 汇总的失败轨迹，加上整段 edit history（component、hypothesis、diff、ΔS、ΔC、是否被接受）。每个候选能捆绑几条 edit 由余弦退火预算 b_t 决定（b_max 3–4，退到 1）。连续 w=3 轮进展都落在噪声带 δ 内就判为 stall，这时留 1 个候选位给没碰过的 component。被判为"不再贡献"的 component 交给 proposer 删除（pruning）。
- **评测**：每轮 2 个候选，各在自己的 git worktree 里，在完整 evolve set 上跑 k 次（k = 2/2/4）。
- **接受**：S' ≥ S* − δ（S* 是历史最高分）。ΔS > δ 时要求 ΔC ≤ β0 + β1·ΔS；ΔS 在噪声带内时要求 w_s·ΔS − w_c·ΔC + w_n·ν > 0（ν 是从未进入过获胜 edit 的结构类 component 数）。另有领域 guard。admissible 候选里取 S' 最大的；一个都没有就保留 H_t。
- **留存**：接受的候选 fast-forward 到 `evolve/<domain>` 分支，下一轮在它上面继续。
- **改进器**：proposer、analyst、critic 都是固定的 Claude Opus 4.8，它们的"宪法"`domains/<name>/SKILL.md`、`PATTERNS.md` 不在 `harness_path` 里。**改进器本身不被修改。**

## 作者报告的证据
所有数字都是作者报告的，policy 均为 Claude Opus 4.8，与 H_0 在同一时间窗口内测。轮数 T = 20/20/40，每轮 2 个候选。
- Coding（evolve = Terminal-Bench 2.1 全部 89 题）：TB2.1 74.2→80.2；SWE-bench Verified（OOD）82.0→83.8。
- Workspace（Harvey LAB 固定划分，evolve 120 题、held-out 40 题）：evolve 89.4→90.5；ID held-out 86.9→89.2；JobBench 36.0→40.7；GDPval 48.8→52.3；APEX-Agents（480 题，pass@1）34.2→37.9。
- Engineering（evolve = EngDesign 61 题，不设 ID held-out）：50.0→54.9；Frontier-Eng（OOD，Medal 分，47 题中 38 题有分，与 evolve set 重叠的 EngDesign 子域已剔除）17.7→22.0。
- 与 H_0 比的增益做了逐题配对 bootstrap（10,000 次重采样，Table 6），95% CI 都不含 0。例：JobBench [+2.9, +7.4]，SWE-bench [+1.1, +4.0]，Frontier-Eng [+1.1, +12.1]。
- 重复搜索一次（Table 7）：workspace OOD 平均 43.6 / 43.7；TB2.1 80.2 / 82.0。只重复了 RRSI。
- 与基线比（Table 1，**仅 workspace 一个领域**）：起点 H_0、evolve set、候选预算都相同。OOD 平均 H_0 39.7、RRSI 43.6；Meta-Harness 的 evolve 分最高（93.0），OOD 平均比 H_0 高 0.9；AHE、TTHE 的 OOD 平均低于 H_0。coding 和 engineering 的基线只在 Fig.1(b–d) 以"四个基线的平均"出现，我没读到具体数值（是图片）。
- 消融（Table 2，workspace，单次运行）：完全不加正则时 evolve 92.8、OOD 平均 40.3、3.80M tokens/trial；RRSI 为 90.5 / 43.6 / 2.42M；H_0 为 1.56M。
- 换 policy：用 Gemini 3.5 Flash 跑 coding 搜索，TB2.1 64.6→78.7，SWE-bench 76.8→79.0。把这个 harness 直接换给 Gemini 3.1 Flash Lite，TB2.1 11.2→14.6。
- workspace 主运行：20 轮共评测 32 个候选，最终接受 4 条 edit。

## 我们的诊断
- **证据等级 = `retained`。** 最终留存的 harness 在没参与选择的 ID held-out 和 5 个 OOD 基准上都提升，CI 不含 0，第二次搜索复现了这一结果，所以够 `retained`。不到 `improver`：proposer、critic、analyst 和它们的 prompt 都是固定的。edit history 只是改进器的输入，改进机制本身没变，也没有实验比较"改进后的改进器"。名字里的 "Recursive" 是架构层面的说法，不构成证据。
- **留出与泄漏**：
  - 选择集只有 evolve split（TB2.1 全集、Harvey LAB 120 题、EngDesign 61 题）。
  - 最终报告集：Harvey LAB 40 题 ID held-out，加上 SWE-bench Verified、JobBench、GDPval、APEX-Agents、Frontier-Eng。
  - 论文称超参（δ 来自 H_0 的重复评测，β 来自开局几轮）"从不查看 held-out/OOD"。另有一个风险：方法设计本身是否参考过 OOD 结果，这一点无法核查。
  - **leakage screening 只看 diff，不看 proposal 的理由文字。** 拒收的内容包括：
    - 任务名、实体名、任务特定值或答案、suite 专属逻辑、inert machinery；
    - 代码里还有：试图读取或推断 verifier/judge/rubric 的"grader gaming"、跨 trial 持久化任务数据的 memory/skill、无上限的循环、未声明的捆绑。
  - 实现分两层：确定性正则，加 Opus 4.8 审查。critic 的召回率没有测过。论文披露 coding 运行中 38 个被筛候选只有 1 个被拒（10-B），而且原因是声明的 component 与 diff 不符，不是泄漏。
  - 报告集从不进入选择，所以 headline 结论的泄漏风险判为 low。evolve 上的数字仍然属于选择集。
- **预算与失败处理**：
  - 与基线只对齐了"候选预算"，proposer/critic 的 LLM 开销没有报告。与 H_0 比，推理 token 也没对齐（2.42M vs 1.56M/trial，作者承认"部分增益买自 test-time compute"），所以判 `partial`。
  - 失败计数：缺失或 infra 失败的 trial 记 0 分，并留在完整分母里（APEX、Harvey LAB 在文中也写明了）。
  - 缺失比例超过 `invalid_missing_frac`（coding 0.2、workspace 0.1）时先重试一次。重试只补缺失的 trial；仍超标就判 `eval_invalid`，不能被接受。
- **最强的反驳**：核心的比较结论是"正则化带来了比现有方法更好的迁移"，但它只有 workspace 一个领域的数据。每个基线只跑一次，方法之间的差没有 CI，基线由谁、按什么配置复现也没有说明。RRSI 比 Meta-Harness 的 OOD 平均高 3.0，而单个 OOD 基准上 RRSI 对 H_0 增益的 CI 宽度约 4–6 分，这个差距可能落在基线自身的运行间方差里。

## 代码核查
- **版本**：固定 SHA be50316e1db05914068a973f322770ef08ed7ba1。已通过 GitHub API 确认这个 commit 存在（2026-09-23）；本地快照里 `domain.py`、`selection.py`、`evaluate.py` 的 sha256 与该 SHA 下 raw 文件一致。快照没有 `.git`。
- **另外读了**（同一 SHA，现取）：`rrsi/critic.py`、`rrsi/loop.py`（部分）、`domains/{coding,workspace}/adapter.py`、`rrsi.json`。**未运行。**
- **已确认**：
  - `selection.judge` 的顺序是：floor（相对 S*）→ cost_rule → guards → 在 admissible 里取 argmax S'。
  - 噪声带内的候选确实可能凭 −w_c·ΔC 或 w_n·ν 被接受。ΔS 可以为负，所以分数略低于 incumbent 的候选也可能取代它。论文附录 D.3 写明这是有意设计的。
  - 配置：coding 的 w_s = 0；workspace 的 w_s = 1414；w_c = 15，w_n = 0.5。论文称这些权重列在 Table 5，但 v3 的 Table 5 里没有它们，只能在 `rrsi.json` 里找到。
  - `aggregate` 的分母是所有 trial 的权重之和。两个 adapter 都把缺失 trial 补成 0.0：workspace 把权重设为该题 rubric 条目数；coding 只把 infra 失败当缺失，普通失败本来就是 0 分。
- **发现的不一致**：
  - `C_hat` 只对 token 数 > 0 的 trial 求平均，与 docstring 和 Eq.(1) 写的 1/(k|D|) 不一致。
  - 任一侧 token 数缺失时，`relative_cost_change` 返回 0，成本规则相当于失效。
- **没确认**：
  - `propose.py` 是否在技术上禁止写 `harness_path` 之外的文件；
  - eng adapter 的写法；
  - 各领域 `critic_patterns` 的具体内容；
  - 主实验里是否用过 `reevaluate`（对 infra 失败的轮次重测）。
- **另一处不一致**：摘要说 OOD 增益"最高 4.3"，但 JobBench 是 +4.7（论文正文和 README 都写的 +4.7）。

## 相对已有工作的增量
- **Meta-Harness**（Lee et al., 2026b，本文的基线）：edit space 一样开放，proposer 也读历史和轨迹。RRSI 新增的是作用在搜索动态上的正则：退火的 edit 预算、按全历史做信用分配、评测前的 diff 级泄漏筛查、噪声下限、成本规则、剪枝。论文的 Table 9 认为 Meta-Harness 留存的是"复述评分方案"的长 prompt。
- **Darwin Gödel Machine**（Zhang et al., 2026b，论文只把它列为"自我改进 agent 的机制与风险来源"）：以下是我们自己的知识，不是论文的说法。DGM 用 archive 做开放式搜索，并且改的是包括自我修改逻辑在内的 agent 代码。RRSI 用贪心的 incumbent，改进器固定，重点放在泛化，不追求开放性。
- **HarnessCompass**（Zhang et al., 2026d，同期工作）：把泛化写进搜索目标。RRSI 自称与它正交：目标不变，只约束搜索轨迹。论文没有和它做实验比较。

## 适合 / 不适合
- **适合**：已经有可信、可重复的 verifier，并且能给 evolve set 和独立的 held-out 集都跑通完整评测的团队。
- **接入代价**：
  - 要写一个 `Domain` adapter（run / score / load_trial / render_trace / smoke / critic_patterns / briefs / guards），每个候选一个 git worktree；
  - 用 H_0 的重复评测标定 δ；
  - 每轮 2 个候选 × 整个 evolve set × k 次 trial，算力开销大；
  - 默认用 Vertex 上的 Opus 4.8，可以通过 LiteLLM 换成别的模型。
- **不适合**：
  - evolve set 很小、δ 相对增益太大的场景（engineering 实例因此没设 ID held-out）；
  - 没有 token 计数、成本规则会失效的执行器；
  - 想证明"改进器自身变强"的研究，RRSI 不改改进器。
- **注意**：`admissible` 不等于"显著改进"。面向发布的版本仍应另做晋升评测。

## 一个值得验证的问题
把 H_0 的 test-time compute 拉到与 RRSI 相同的水平（workspace 约 2.42M tokens/trial，例如放宽步数和上下文上限，或者用同 token 的 best-of-n），RRSI 在 JobBench、GDPval、APEX-Agents 上 +3.9 的 OOD 平均增益还剩多少？同时把每个基线也重复跑 2 次，看 RRSI 与 Meta-Harness 的 OOD 差距是否超出运行间方差。

## 来源
- 论文：https://arxiv.org/abs/2609.24972v3 （v1 2026-09-21，v3 2026-10-04；全文读的是 https://arxiv.org/html/2609.24972v3）
- 代码：https://github.com/google-research/rrsi/tree/be50316e1db05914068a973f322770ef08ed7ba1
