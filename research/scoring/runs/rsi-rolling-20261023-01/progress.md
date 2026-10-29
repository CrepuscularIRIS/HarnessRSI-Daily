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

## 2026-10-24 08:43 每日 Opus 判断（附 C1 修订落档）

- 新增 confirmed P3：5 篇 ≥3 → 执行第三期选题。终选 3 篇（30499/28798/29005），3 张画报视觉 QA 全过；28815 落选（同题去重+单次消融）列下期备选。见 selection-003.md。
- Correction C1（2610.30042 统计单位误读）已退回 Sol 单篇修订：inc-l2-02-rev1-30042.jsonl——降为 P2/pending_experiment/to_l2（q3=incremental）；C1 三点实质接受、两处限定（± 定义原文未写明、"一次搜索"不能确证）。原 L2 记录保留。
- 本 run to_l3 候选池余 2 篇（28815 备选 + 30042 已降档出局）。

## 2026-10-25 08:43 每日 Opus 判断

- selection-003 后新增 confirmed P3：0 篇（候选池余 28815 备选一篇，上期已评估落选）<3 → 本轮跳过 Reel。巡检班 12:17 确认无新收集。

## 2026-10-26 08:43 每日 Opus 判断

- selection-003 后新增 confirmed P3：0 篇 <3 → 跳过（池内 28815 备选维持）。无 L2 预算可用（累计 L1=23、L2 已用 7 超出 20% 上限），待新 L1 解锁。

## 2026-10-27 补跑班（fetch 盲区修复后）

- 盲区说明：10-24/25/26 巡检未先 git fetch，漏掉 Grok 直推远端收集；本班补齐（cron 提示词已改 fetch-first，记忆已更新）。
- 新增：12 篇（inbox/2026-10-26-0030，corpus 1620→1632，全文 12/12，材料 12/12 abstract_intro）。
- L1：inc-l1-03 12/12 完成（assessed 11 / oos 1——2610.31846 LoRA 参数学习超范围；2610.32412 摘要与正文差异标 L2 核）。档位 P3×6 / P2×5 / null×1。
- 预算修订：run.md 2026-10-27 增量轮声明（每班 to_l2 全部 + 遗留 high ≤5），替代 20% 累计默认。
- L2：inc-l2-03（10 篇：6 篇遗留 P2-medium + 4 篇遗留 P3-high）+ inc-l2-04（7 篇：6 本班 + 1 抽查）= 17/17 完成。**5 篇 P3/confirmed/to_l3**（31326/31401/32026/32253/32322）；2 篇 P2→P3 上移至 pending_experiment（2605.14089、2610.29357，L2 发现自有实验解除 Q1 封顶）；32813 漏检抽查无改判（P2→P2/park）。
- 漏检抽查：首次执行（seed=44，1 名额），改判 0/1；欠账余 ~1.5（累计未取整部分），继续攒。
- to_l3 池：28815（备选）+ 本班 5 = 6 篇 ≥3 → 明早每日 Opus 班选题。
- 待办：pending_experiment 8 篇待实验对照材料；needs_material 0。

## 2026-10-27 12:17 巡检班

- 新增：12 篇（inbox/2026-10-27-0036，corpus 1632→1644，全文 12/12，材料 12/12 abstract_intro）。入库两遇 arXiv API 429/超时，15 分钟退避后成功；教训：inbox mv 只挂入库成功后。
- L1：inc-l1-04 12/12 完成（assessed 11 / oos 1；P3×10 / P2×1 / null×1）。
- L2：按增量轮声明执行（本班 to_l2 全部 11 篇；high 遗留 0；工具默认多排的 8 篇遗留 medium 已裁出，留待将来声明扩充）。inc-l2-05（6）+ inc-l2-06（5）= 11/11 完成。**5 篇 P3/confirmed/to_l3**（34027/34238/34938/35316/35579）；35193 P2/pending_material（被引源文件未核，封顶 P2）；35434 P3/pending_experiment；33024/33046/33845/33956 P3/pending_experiment/park。子卡合计 110 项（33 holds / 58 partial / 15 fails / 6 unknown / 1 challenged / 1 NA——fails 为论文被诊断系统违反条件，非诊断失败）。
- 漏检抽查：0.1×11=1.1→1 名额，本班未用（队列构建时无待抽查池），欠账累计 ~1.7。
- to_l3 池：5 篇 ≥3 → 明早 Opus 班选题（第五期）。

## 2026-10-28 08:43 每日 Opus 判断（第五期选题 + C-005-1 落档）

- 新增 confirmed P3：5 篇 ≥3 → 第五期选题。终选 3 篇（34938 自演化实证 / 34238 Δτ-Bench+STEWARD / 35579 Infinity Machine 限 L2 确认范围），3 张全过 QA；34027 列下期备选（双主卡与 34938 重叠 + 单 seed 优选）。见 selection-005.md。累计 24 张。
- Correction C-005-1（35316：Q2 vertical_port + 最小种子基线增益 + Table 3/4 冲突）已退回 Sol 修订：inc-l2-06-rev1-35316.jsonl → **P1/confirmed/park**（q2=vertical_port、q3=incremental、q4=partial；三点全接受，64.98/+28.02 标 Table 3 basis）。原记录保留。
- to_l3 池：34027（备选）。

## 2026-10-28 06:17 巡检班

- 新增：7 篇（inbox/2026-10-28-0642，corpus 1644→1651，全文 7/7，材料 7/7 abstract_intro；收集 +8 中 1 个为 GitHub-only（langchain design-agent），arXiv 检索无命中留 inbox 待关联）。入库脚本一次因无 arxiv 字段项崩溃并连带误挪 inbox——已恢复，mv 改挂在校验断言之后。
- L1：inc-l1-05 7/7 完成（全 assessed；P3×3 / P2×4）。
- L2：inc-l2-07 7/7 完成（本班 to_l2 全部）。**4 篇 P3/confirmed/to_l3**（37651/36826/37255/34073）；36077 P3/pending_experiment；36774/37046 P2/park。
- 漏检抽查：0.7→0 名额，欠账累计 ~2.4。
- to_l3 池：34027（备选）+ 本班 4 = 5 篇 ≥3 → 今晨 Opus 班第六期选题。

## 2026-10-29 06:17 巡检班

- 新增：2 篇（inbox/2026-10-29-0036 + 0643，corpus 1651→1653，全文 2/2，材料 2/2 abstract_intro）。
- L1：inc-l1-06 2/2 完成（全 assessed，P3×2）。
- L2：inc-l2-08 2/2 完成（本班 to_l2 全部）。**1 篇 P3/confirmed/to_l3**（37201——L3 须保留选择模型假设/最低起始分数敏感性/正向例外/timeout 排除边界）；35966 P3/pending_experiment/park（失败归因与护栏缺独立对照）。子卡 23 项：holds 7 / partial 14 / fails 1 / unknown 1。
- 漏检抽查：0.2→0 名额，欠账累计 ~2.6。
- to_l3 池：36826（上期备选）+ 本班 1 = 2 篇 <3 → 今晨 Opus 班预计跳过（除非日内再增）。

## 2026-10-29 08:43 每日 Opus 判断

- selection-006 后新增 confirmed P3：2 篇（36826 备选 + 37201）<3 → 跳过。12:17 巡检班若再增，明日选题。
