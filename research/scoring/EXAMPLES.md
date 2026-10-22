# rsi 输出示例（problem-core-v1.1）

全部论文信息、定位和结果均为虚构，仅说明字段格式，不能进入任何名单。卡片 ID 引用本仓库真实卡片，实际评价必须读取对应卡原文和论文。

L1（摘要＋引言）：

```json
{"paper_id": "SYNTH-EXAMPLE", "stage": "L1", "supersedes": null, "status": "assessed", "material": "abstract_intro", "problem_statement": "虚构示例：共同检索时，结果信号无法归到单个记忆条目，留存决定可能保留无用条目。", "problem_source": "card_supported", "families": ["F1", "F5"], "cards": ["main/evidence_gated_retention"], "card_anchor": "Failure modes：共同检索时结果信号无法归到单个条目", "q1_basis": "measured_own", "q2_open": "challenges_barrier", "q2_prior": null, "later_work": null, "q3_change": "capability", "q3_loss": "虚构示例：该问题导致部署时出现可测的失败；解决后去掉这一失败来源。", "q4_fit": "unknown", "problem_tier": "P3", "evidence_status": "pending_method", "priority": "high", "next_action": "to_l2", "subcard_checks": [], "facts": [{"loc": "虚构 §1 ¶2", "fact": "仅用来展示字段，非真实结果。"}], "biggest_gap": "方法是否真正隔离该问题尚未看到；L2 需核对方法与主要实验。", "audit_sample": false}
```

L2（方法与实验；另写一条，不改 L1 原行）：

```json
{"paper_id": "SYNTH-EXAMPLE", "stage": "L2", "supersedes": "SYNTH-EXAMPLE#L1", "status": "assessed", "material": "core", "problem_statement": "虚构示例：共同检索时，结果信号无法归到单个记忆条目，留存决定可能保留无用条目。", "problem_source": "card_supported", "families": ["F1", "F5"], "cards": ["main/evidence_gated_retention"], "card_anchor": "Failure modes：共同检索时结果信号无法归到单个条目", "q1_basis": "measured_own", "q2_open": "challenges_barrier", "q2_prior": null, "later_work": null, "q3_change": "capability", "q3_loss": "虚构示例：该问题导致部署时出现可测的失败；解决后去掉这一失败来源。", "q4_fit": "partial", "problem_tier": "P3", "evidence_status": "pending_experiment", "priority": "high", "next_action": "park", "subcard_checks": [{"card": "sub/H29", "section": "Tactical failure mode", "question": "该机制依赖的条件是否成立，关键失败是否被排除", "verdict": "partial", "paper_evidence": "虚构 §3 / Table 2 只覆盖部分条件。"}], "facts": [{"loc": "虚构 §3 / Table 2", "fact": "仅用来展示字段，非真实结果。"}], "biggest_gap": "关键对照只覆盖一种设置；补齐后决定是否进入 L3。", "audit_sample": false}
```

材料不足以判断档位时：`problem_tier` 为 null，`status` 为 `needs_material`，`priority` 按潜在价值给出，不记 P0。没有合适子卡时 `subcard_checks` 写 `unassigned` 并说明原因，不扣分。
