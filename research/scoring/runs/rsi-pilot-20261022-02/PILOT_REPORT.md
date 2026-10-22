# 试点报告 — rsi-pilot-20261022-02（problem-core-v1.1，2026-10-22）

按 PROBLEM_CORE §9.3 交用户审。结构校验通过 ≠ 科学判断正确。

## 覆盖

L1：10/10（1 批，Sol 单席，约 294 秒 / 127K subagent tokens，均 ~12.7K/篇）。
L2：9/10（to_l2 8 篇全跑 + 2 篇漏检抽查；约 975 秒 / 176K tokens，均 ~19.5K/篇）。2312.10003（abstract-only out_of_scope）未重复 L2——与 2210.11610 同类，摘要级复查无增量信息。

## 结果

| paper | L1 | L2 | 变化 |
|---|---|---|---|
| 2605.19576 Library Drift | P3 pending | **P2** pending_experiment | **推翻**：漂移假说缺直接对照，q1→asserted |
| 2604.14475 Evo-MedAgent | null needs_material | **P1** park | 补全文后判：移植为主、约束变化证据弱 |
| 2608.10319 Personalized Skills | P3 | P3 **confirmed** → to_l3 | — |
| 2609.00069 Harness Tampering | P3 | P3 pending_experiment（留 to_l2：误报校准/人工复核依据不足） | 降确认级 |
| 2610.14216 Cortex | P3 | P3 confirmed → to_l3 | — |
| 2607.12227 Rethinking Harness Eval | P3 | P3 confirmed → to_l3 | — |
| 2606.16420 Transferable Playbooks | P3 | P3 confirmed → to_l3 | — |
| 2305.16291 Voyager（抽查） | P3（F0） | P3 confirmed → to_l3 | F0 未降档；卡片成员身份未触发自我比较 |
| 2210.11610（抽查） | out_of_scope | 维持排除（仅摘要可查，q4 unknown） | 材料受限 |

子卡条件检查：6 张子卡（H00/H06/H30/H31/H32/H35）共 55 项：成立 24、部分 28、不成立 2、NA 1；同子卡固定问题组执行。

## §9.3 三问

1. **漏检**：2 篇抽查无 upward 推翻；F0 的 Voyager P3 成立（F0 同资格规则有效）。系统性风险点：abstract-only 记录的范围判定只能到摘要级（本试点 2/2 abstract-only 均判 out_of_scope，无法从摘要验证方法侧成分）——全量时这类记录建议照 v1.1 §5 按 priority 排队补材料，而不是直接排除。
2. **L2 推翻 L1**：1 篇 P3→P2、1 篇 null→P1、1 篇降确认级——漏斗按设计工作；L1 的 P3 高判（7/10）在试点选材偏强的情况下仍有 1 篇被降，说明 pending_method 门有用。
3. **用量**：L1 ~12.7K tokens/篇、L2 ~19.5K/篇（subagent 侧，估算）。外推全量 933 篇：L1 ≈ 12M；L2 按默认 20% 预算（187 篇）≈ 3.7M。若含 corpus 全部 1597（664 篇 abstract-only 材料≈0.5K/篇，L1 极廉价）：L1 ≈ 20M。

## 局限（如实）

- 「唯一来源卡」论文不可判定（仓库无逐篇-卡片映射）；以 Voyager（crystallize/H02 成员）替代测试 Q2 自我比较排除，未触发误判。建议后续在卡片中记录成员论文 ID（§9.4 修订项）。
- 试点 10 篇为刻意选强/选异质样本，档位分布不代表全量。
- L2 中 2609.00069 留在 to_l2（需实验级核对），全量规则下此类论文按预算循环。

## 待用户决定

1. 是否授权全量 L1；范围 933（有钉定全文）还是 1597（含 664 篇 abstract-only，按 v1.1 处理路径走 needs_material 排队）。
2. L2 预算确认（默认 L1 篇数 20% + 10% 漏检抽查）。
3. 对 v1.1 规则本身的修订意见（§9.4：三处同步 + PROBLEM_MAP）。
