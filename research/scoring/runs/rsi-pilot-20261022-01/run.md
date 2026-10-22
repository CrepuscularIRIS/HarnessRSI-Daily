# run rsi-pilot-20261022-01 — problem-core-v1 试点（L1→L2，10 篇）

- 触发：用户 2026-10-22「全部重新打分」；按 PROBLEM_CORE §8 试点先行，试点通过并经用户授权后才启动 933 篇全量 L1。
- 规则：research/scoring/，problem-core-v1（两层：第一层问题档 P0–P3；第二层子卡固定问题）。v3.1 四轴不用于全量。
- 执行模型：6.1 Sol（CC Agent model type sonnet），单席；本试点 1 批 L1（10 篇），L2 视 P2/to_l2 数量。
- 试点选材（§8 覆盖）：F1 归因×4（2605.19576/2610.14216/2610.27610/2210.11610）、F2 信号（2610.14216/2607.12227）、F3 迁移（2608.10319/2606.16420/2312.10003）、F4 信息访问（2609.00069）、F5 单调（2605.19576/2608.10319）；诊断/审计＝2605.19576；明显 vertical_port 候选＝2604.14475（Evo-MedAgent，经验记忆移植医疗）；abstract-only＝2210.11610、2312.10003（material=abstract，测 L1 降级路径）。实际 families 由 worker 判定，此处仅为选材覆盖预估。
- 材料：l1_materials/（摘要+引言头 ≤9K 字符，自钉定全文缓存切出；无全文者仅摘要），l1_inputs.jsonl 逐篇记录级别。复用缓存，不新增抓取。
- 卡片版本：patterns/ sha 汇总 343dc4a1c6b58e84（51 文件）。
- Git HEAD：None
- 工具：research/scoring/tools/l1_material.py（切料）、l1_check.py（§7 机械校验，L1 封顶 P2）。
- 输出：batches/p1.jsonl（L1）→ L2 对 to_l2 论文补 Q4 与子卡问题 → 报告交用户 §8 人工审。
