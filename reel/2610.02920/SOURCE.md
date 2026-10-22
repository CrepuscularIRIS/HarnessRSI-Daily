# SOURCE — 2610.02920

- 论文：HASTE: Evolving Agent Harnesses Against Emerging Attacks Using Sparse Evidence（Xiong, Li, Ma, Li, Wang, Feng, He；中国科大 / 新加坡国立 / 新加坡管理大学）
- 版本：arXiv:2610.02920**v1**（2026-10-02）；代码 github.com/xxiqiao/HASTE（未运行）
- 钉定全文：`research/fulltext/review-runs/rsi-v22-20261021-01/materials/2610.02920.txt`（正文 §1–5 与附录 A–E 已通读，包括 selection-002 待补项中的附录 C 与表 10；图 1–5 是图片，不在文本中，未从中取数）
- 初筛记录：L1 `batches/b069.jsonl` → L2 `batches/l2c22.jsonl`（P3 / confirmed / high / to_l3）；L3 `l3-final-2.tsv` #5、`selection-002.md` 阶段二
- run：rsi-l1-20261022-03（第二期）

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处 |
|---|---|---|
| 右上“能拿到什么” | blind 只有描述；seen 另有少量观测样例，从基准抽样，其余样本构成留出评测集；ASB 2,000 题、STAC 483 题 | §3.2 Final Harness Selection 末段；附录 C.1 |
| 问题 | 稀疏证据（描述 / 少量样例），覆盖有限；改模型代价高；手工改 harness 费人力；ASR / SHR 定义 | §1、§3.1 公式 (1) |
| 问题右侧对比 | Meta-Harness 在固定用例集上用经验更新；HASTE 规格与用例对抗共演化 | §2、§4.1 Baselines、§4.2 结论 (3)；图 1 思路（用文字重述，未复制图） |
| 机制图 ① | 攻击解析器把 𝒪 提炼为攻击规格 a，全程固定；解析器用 GPT-5.1 | 公式 (2)；附录 C.3 |
| 机制图 ②③ | σ_t = π_spec(a, h_{t−1}, ℱ_{t−1})；h_t = π_prop(h_{t−1}, σ_t)，在上一版上修订；Claude Code + DeepSeek-V4-Pro | 公式 (3)(5)；§4.1 Implementation；附录 C.3 |
| 机制图 ④ | (𝒢_s, 𝒢_ns) = π_case(…)；𝒢_ns 无安全完成路径，𝒢_s 可安全完成；用 h_0 做可行性筛查，不判安全 / 效用，失败用例带日志退回 | 公式 (4)；§3.2 Stage 2 |
| 保密幕 | 当轮新生成的用例对规格优化器和提案者隐藏 | §3.2 Stage 2：“newly generated cases are withheld from both the specification optimizer and the proposer” |
| 机制图 ⑤ | 𝒞_t = 生成用例 ∪ 观测样例；judge 给 s、u 与诊断；ℱ_t = ℱ_{t−1} ∪ (h_t, ℛ_t)；适应期 AgentDoG（安全）、DeepSeek-V4-Flash（效用） | 公式 (6)–(10)；附录 C.2 |
| 盾牌三层 | 验证门控 / 上下文治理 / 证据执行 | 附录 D.2 及图 6–9 伪代码 |
| 选择规则 | blind 取 h_T；seen 取 argmax(1 − ASR_t + SHR_t)，在固定观测样例上算 | 公式 (11)(12)；附录 E |
| 预算与评测 | 5 轮、16 个安全用例（“sampled from the target benchmark”），ASB 另 16 个可完成用例；最终评测 ShieldAgent + GPT-5.6-luna（ASB）、DeepSeek-V4-Flash（STAC）；3 次重复 | §4.1；附录 C.2、C.3 |
| 哑铃图 | 四骨干 × {无防御、blind、Meta-Harness、seen} 的 ASR / SHR 及平均（51.39/44.52、35.75/49.81、32.03/49.85、28.50/58.39） | 表 1 |
| 哑铃图注 | Safiron 平均 ASR 40.67、SHR 37.20（六个固定防御中 ASR 最低）；Phi-4-mini seen 40.33 对 Meta-Harness 40.06；blind 50.75 | 表 1 |
| 冻结消融 | ASB-300、Qwen3-8B：无防御 54.00/45.00；blind 完整 26.00±4.67、冻结规格 46.33±8.11、冻结用例 53.67±1.00；seen 25.56±14.61、40.22±13.36、55.89±1.68；SHR 54/49/48、52/50/47 | 表 3 与 §4.3 |
| 边界 2 | STAC 平均 ASR：seen 15.76，Meta-Harness 16.29，blind 29.12；seen 在 Qwen3-8B 上 28.52±26.82 | 表 2 |
| 边界 3 | ASB-300 安全 judge 两两一致 69.35–84.22%，ShieldAgent–AgentDoG 74.00；换最终 judge 后相对排序大体不变 | 表 11、表 10 |
| 边界 4 | 顺序引入 8 类风险，三种方法在首类风险上的 ASR 总体上升，seen 最稳 | §4.4 Continual Evolution（图 3、4，只引作者文字） |

## 示意与重绘

- 机制图（含保密幕、盾牌三层剖面）为本项目示意，不是论文图 2 的复制。
- 哑铃图、条形图由表 1、表 3 数值绘制，未做任何换算。

## 核对说明

- 与 selection-002 / L2 一致，无 correction。
- 口径补充：原文“16 safety cases sampled from the target benchmark”与 blind“只靠生成用例”在字面上不完全对应，画报写成“16 个安全用例（原文称从目标基准抽样）”，不替作者解释。
- “新兴攻击实为已发表基准”“STAC 上差距在波动内”是本项目阅读判断，画报已标注。
