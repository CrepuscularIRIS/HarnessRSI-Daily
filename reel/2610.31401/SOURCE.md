# SOURCE — 2610.31401

- 论文：HERD: Harness-Evolving Recursive Distillation for Continual Learning（Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu）
- 版本：arXiv:2610.31401**v1**（2026-10-22）
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/2610.31401.txt`（HTML 转文本，sha256 `91f681d5…02ee7e7e`）。正文 §1–§5、Limitations 与附录 A–E 全部通读。
- 初筛记录：L1 `batches/inc-l1-02.jsonl` → L2 `batches/inc-l2-03.jsonl`（P3 / confirmed / capability / to_l3）；L3 `selection-004.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 结论（画报展示口径）

在 TRACE+17 的 25 阶段任务流、Qwen3.5-4B、固定记忆与每阶段 32×32 更新预算下，HERD 每阶段演化技能与高残差记忆，再在检查点锚与基座锚的漂移预算下把 harness 自蒸馏进权重：习得与 Seq-LoRA 持平，AA 与 uniform replay 持平，遗忘与通用能力损失显著更小。去掉技能（单种子）AA 降 5.0 点，支持 harness 在训练中承重；但部署时 harness 不再贡献分数，守门也没有挡住坏技能。

## 断言 / 数字 → 原文（行号指钉定文本）

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 标题 / 副标题 | 日间 harness / 夜间权重比喻；部署只用权重 | §1（L59–，“episodic memory … sleep consolidates”）；Abstract（L39–） |
| 01 只改 harness | ACE 第 2 个任务到 15,410 tokens、超 16,384 回滚；HCL 几乎不提交；AA 0.427/0.433 vs 0.419 | §3.2 Non-parametric methods（L1725–1733）；Table 1（L1574–） |
| 01 只改权重 | Seq-LoRA GSM8K 0.89→0.18、IFEval 0.82→0.33；损失 20.0–25.5 点；最差一类 62–68 点 | §3.2 General capability（L1775–1800）；§1（L229） |
| 01 注 | 两个上下文基线在此设定几乎没学到东西，不作一般证明 | 本项目阅读判断（依据同上与附录 B 的 ACE/HCL 配置） |
| 设定 | 8 TRACE + 17 SuperNI；500/100/100；G-test 5 类 × 200；Qwen3.5-4B；32×32；三种子；4,000 次配对自助 | §3.1（L1615–1700）；附录 B（L2697–） |
| 02 白天 | 窗口 8,192；检查点先作答、至多 4 个错例；θ₀ 一次写 ≤768；前缀路由 | §2.3（L710–760）；附录 A（L2175–） |
| 02 守门 | 残差（Eq. 2）下降才提交；75 次全部通过 | §2.3 Guard（L748–）；附录 D（L4133） |
| 02 记忆 | B_R 32,768 中 24,576 给任务记录；按残差保留完整记录；不重放、只供探针 | §2.3 Residual refresh（L842–）；附录 A |
| 02 夜间 | 教师 = 冻结 θ̄_{t−1}+技能+回放 y*；学生 = 新 LoRA、裸提示；前向 KL | §2.4（L878–）；Eq. 3；附录 A |
| 02 双锚 | D_C 对 θ̄_{t−1}、探针来自 R、按任务分组；D_0 对 θ₀、通用探针、按来源分组；ε = 0.05；前 32 token、最差组；对偶上升 | §2.4 Drift / Two anchors / Enforcement（L1096–）；Eq. 4–6；附录 A（ε、η） |
| 02 合并 | LoRA 合并、每阶段新适配器；部署只用 θ̄_t | §2.2；附录 A |
| 03 表 | AA / Acq / F / G-test / ΔC_min 各方法数值 | Table 1（L1574–1613） |
| 03 注 | SDFT 崩溃 AA 0.021 | §3.2 Long-horizon stability（L1822–）；附录 D |
| 03 配对比较 | −0.002 [−0.010, 0.007]；+0.007 [−0.001, 0.016]；F −0.010 [−0.020, −0.004]；G-test +0.175 [0.150, 0.201]；对静态 harness −1.7 点含 0 | Table 2（L3274–）；Paired comparisons（L3279–3300） |
| 04 消融表 | 各变体 AA / F / ΔC_min | Table 3（L3820–）；§3.3（L1837–1960） |
| 04 文字 | 去技能 −4.5 / −5.0；三倍 SD 尺度 0.024 / 0.009 / 0.036；数学 0.885→0.395 | §3.3 Harness evolution / Two anchors；Seeds and uncertainty（L4040–4062） |
| 04 成本 | 10,723 / 10,463 / 888,082 / 659,000 秒；15,410 tokens | §3.2 Cost（L1817）；Table 4（L3971–） |
| 05 限制 1 | 一个模型一条流；需 y* 与已知边界 | Limitations（L2142–2150）；附录 E |
| 05 限制 2 | 消融与 ε_C 扫描单次 | Table 3 注；Seeds and uncertainty（L4040–） |
| 05 限制 3 | 部署挂回 harness 变化 ≤ 0.4 点 | Ablations（L3985–4038）末段 |
| 05 限制 4 | 75 次提交全部通过；superni:074 两种子 21 / 64 条为问题 | 附录 D HERD’s failing cases（L4123–4137） |
| 05 限制 5 | 9–10 个旧任务无探针；superni:192 0.83→0.52 | 附录 D（L4124–4131） |
| 05 限制 6 | 32 token 锚；IFEval 17 题 0.71–0.76→0.18–0.24（原模型 0.94）；G-test 掉 6.3 点 | 附录 D（L4136–4139）；§1（L229） |
| 06 长程 | 前 8 任务 0.664→0.665；Seq-LoRA 0.372→0.637；探针 0.28/0.16/0.37→0.59，HERD ≥ 0.75；OPHSD 0.741→0.661→0.613→0.582 | §3.2 Long-horizon stability（L1822–1836）；附录 C General capability by category（L3312–3324） |
| 06 漂移审计 | 阶段末 D_C ≤ 0.045、D_0 ≤ 0.044；峰值超 0.05 的阶段 9 / 11；第 6 阶段 0.168 / 0.324 | 附录 C Drift audit（L3325–3340） |
| 本项目读法 | 卡片解释与 q3 条件性结论 | 本项目阅读判断，与 L2 biggest_gap 一致 |

## 示意与重绘

- “一个阶段”日夜流程图、锚图标为本项目示意，按 §2 文字与 Figure 1–2 说明重画。
- 结果表的条形长度按 Table 1 数值等比，本项目绘制。
- 本项目没有运行实验，也没有复现结果。

## 核对结论

与 L2 记录一致，无 correction。补充两处 L2 未写的边界（不改档位）：(1) 作者用来说明“只靠 harness 装不下”的两个上下文基线在此设定下基本没有运行起来（ACE 超输入上限回滚、HCL 几乎不提交），L2 对 H28 Step 1 记 holds 偏宽，画报只作为这两个实现的观测；(2) 部署时挂回 harness 几乎不变、守门 75/75 全过，说明本文确认的是“harness 作为训练期挑选器与教师”的作用，不是推理期 harness 的留存收益。
