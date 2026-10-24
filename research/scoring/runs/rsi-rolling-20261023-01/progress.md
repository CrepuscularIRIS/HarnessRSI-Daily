# rsi-rolling-20261023-01 进度

## 2026-10-23 巡检班（首班）

- 新增：12 篇（inbox/2026-10-22-0000，arXiv API 元数据入库 corpus 1597→1609，全文 12/12 缓存，L1 材料 12/12 abstract_intro）。
- L1：inc-l1-01 12/12 完成。assessed 11 / needs_material 0 / out_of_scope 1（2610.29641 仅演化通信交付程序）。档位 P3×5 / P2×6 / null×1；priority high×5 / medium×6 / none×1。
- L1 校验：v1.1 字段/枚举/封顶/逐条核对通过（12/12）。注：tools/l1_check.py 仍按 v3.1 字段名校验，对本批误报 72 错，已改用 v1.1 校验；该工具待修。
- L2：预算 3（=max(3, 20%×12 取整)，seed=42，l2-queue.tsv）。inc-l2-01 3/3 完成，**全部 P3 confirmed → to_l3**（2610.28798 / 2610.28815 / 2610.29005）。
- 漏检抽查：3×10%=0.3 取整 0，本轮无抽查名额（audit_pool=2：2610.29121、2610.30017）；累计至后续班次预算增大后补做。
- L2 限制（已写入记录，非阻塞）：28798 文件隔离未证实；28815 消融单 run、增长实验混杂变量；29005 仍依赖外部 verifier 校准。
- 待办：8 篇 to_l2 未入本轮预算（P3-high 2 + P2-medium 6），下班次预算按累计 L1 重算；needs_material 0。

## 2026-10-24 巡检班（第二班）

- 新增：11 篇（inbox/2026-10-23-0038，corpus 1609→1620，全文 11/11，L1 材料 11/11 abstract_intro）。另 1 个 GitHub-only 候选（RoboDoctor）留 inbox 待关联。
- L1：inc-l1-02 11/11 完成（assessed 10 / out_of_scope 1）。档位 P3×6 / P2×4 / null×1。
- L2：预算 4（=max(3, 20%×累计 23 篇=4.6 取整)），seed=43；inc-l2-02 4/4 完成：**2610.30042、2610.30499 P3/confirmed/to_l3**；2610.29303、2610.30184 P3/pending_experiment/to_l2。
- 漏检抽查：4×10%=0.4→0，无名额（audit_pool=4），累计待预算 ≥10 时触发。
- 工具修复：l2_queue.py 排除已有 L2 记录的论文（修上轮重复排队问题）。
- 累计 to_l3 候选（本 run）：5 篇（28798/28815/29005/30042/30499）待每日 Opus 判断。
- 待办：to_l2 未入预算 13 篇（P3-high 2 + P2-medium 11），下班次按累计 L1=34 重算；needs_material 0。
