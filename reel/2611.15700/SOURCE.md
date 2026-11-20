# SOURCE — 2611.15700 AskALCF

原文：arXiv 2611.15700v1（2026-11-11，Argonne/Clemson）。全文缓存：research/fulltext/review-runs/rsi-l1-20261022-03/materials/2611.15700.txt。语料：1,229 sessions / 2,174 scored assistant turns / 2,211 ticket threads。

| 海报数值 | 原文位置 |
|---|---|
| unattributable 900/2174 (41.4%) → 309 (14.2%)；attributed 924→1,295；同 turns 前后对照（受控） | §V-B + Fig.4 |
| 机制：729 turns 原无 retrieval verdict，684 落 unknown；修后去向 no_failure 198 / knowledge 150 / retrieval 147 / prompt 75，剩 106 unattributed | §V-B Fig.4 机制段 |
| 16 harness arms：3 接受 / 9 拒绝 / 4 参照（基线+null+两次复现）；被拒的多为「不改证据只改 judge 结论」 | §V-C 首段 |
| expert agreement 108/150→123/150；A1 117 / A2 120 / A3 123（采用 A3）；eval split 35/52→40/52；评估 turns 不用于提出或挑选 arm | Table II 及上下文 |
| null control：中性编辑改 9/11 of 171 routes（绕过缓存）；两复现仅 2 turns 同变；rubric 修订 72%→66% 回滚 | §V-C null control 段 |
| 规则树 vs agent judge 分歧 354/2169 (16.3%)；judge 少归 model（85 vs 159）、少留 unknown（205 vs 306）；大流 model→no_failure 59 / unknown→knowledge 45 / prompt→no_failure 36 / model→prompt 31 | §V-D + Fig.6 |
| 置信度门无效（confidence 反映证据多寡非校准概率）；规则条件门 +7–9pp、九 route 修正零回归 | §V-D + Table III |
| ticket：18% flagged-complete 实未解决、319 resolved 未 flag | §V-B 末段 |
| 限制：accuracy 仅 150 expert turns、分层非均匀、2,024 无参照；修复绕过 retrieval 属上界；单专家多标签；merge/reindex 未完成 | §V-B caveats + §VII 限制 |

海报中「先修归因，再修系统」为本项目概括，非作者表述。本项目重绘，非作者海报，未复现实验。
