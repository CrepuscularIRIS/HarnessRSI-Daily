# run rsi-pilot-20261022-02 — problem-core-v1.1 试点（L1→L2，10 篇）

- 触发：用户 2026-10-22「全部按照这个（v1.1）重新跑」。supersede rsi-pilot-20261022-01（v1 脚手架，无输出，已标 SUPERSEDED）。
- 规则：research/scoring/，problem-core-v1.1（四字段 problem_tier/evidence_status/priority/next_action；无四轴、无 screen_score）。试点完成并经用户授权（§9.4）后才启动全量。
- 执行模型：6.1 Sol（CC Agent model type sonnet）单席。L1 1 批 10 篇（试点批）；L2 批次 = L1 判 to_l2 的全部 + ≥3 篇 P0/P1/F0/needs_material 漏检抽查（§9.2）。
- L2 预算（§5）：试点无独立篇数上限（全部 to_l2 + 抽查 3）；token 上限不设，实测用量写入试点报告。
- 选材（§9.1）：F1 2605.19576/2610.14216；F2 2610.14216/2607.12227；F3 2608.10319/2606.16420；F4 2609.00069；F5 2605.19576/2608.10319；诊断/审计=2605.19576；疑似 vertical_port=2604.14475；abstract-only=2210.11610、2312.10003；卡片成员（测 Q2 自我比较排除）=2305.16291 Voyager（crystallize_executable_capability/H02 归纳来源之一）。注：仓库无逐篇-卡片映射，「唯一来源卡」论文不可判定，以典型成员替代并记入试点报告局限。
- 材料：l1_materials/（摘要+引言头 ≤9K 字符，8 abstract_intro + 2 abstract），复用钉定缓存，零新增抓取；l1_inputs.jsonl 记录级别。
- 卡片版本：patterns/ sha 汇总 343dc4a1c6b58e84（51 文件），run 内固定不改卡。
- Git HEAD：88a70c5ad892562dc435dbe070c2b4c6e1c14868（含未提交的 v1.1 规范工作区改动，属规范会话，本 run 不提交）
- 工具：research/scoring/tools/l1_material.py、check_record.py（v1.1 枚举/封顶/schema 校验）。
- 输出：batches/p1.jsonl（L1）→ batches/l2a.jsonl 等（L2，supersedes 链）→ 试点报告交用户 §9.3 审（漏检、L2 推翻 L1、IO 用量）。
