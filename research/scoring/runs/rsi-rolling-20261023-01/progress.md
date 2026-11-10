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
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：28815（备选）+ 本班 5 = 6 篇 ≥3 → 明早每日 Opus 班选题。
- 待办：pending_experiment 8 篇待实验对照材料；needs_material 0。

## 2026-10-27 12:17 巡检班

- 新增：12 篇（inbox/2026-10-27-0036，corpus 1632→1644，全文 12/12，材料 12/12 abstract_intro）。入库两遇 arXiv API 429/超时，15 分钟退避后成功；教训：inbox mv 只挂入库成功后。
- L1：inc-l1-04 12/12 完成（assessed 11 / oos 1；P3×10 / P2×1 / null×1）。
- L2：按增量轮声明执行（本班 to_l2 全部 11 篇；high 遗留 0；工具默认多排的 8 篇遗留 medium 已裁出，留待将来声明扩充）。inc-l2-05（6）+ inc-l2-06（5）= 11/11 完成。**5 篇 P3/confirmed/to_l3**（34027/34238/34938/35316/35579）；35193 P2/pending_material（被引源文件未核，封顶 P2）；35434 P3/pending_experiment；33024/33046/33845/33956 P3/pending_experiment/park。子卡合计 110 项（33 holds / 58 partial / 15 fails / 6 unknown / 1 challenged / 1 NA——fails 为论文被诊断系统违反条件，非诊断失败）。
- 漏检抽查：0.1×11=1.1→1 名额，本班未用（队列构建时无待抽查池），欠账累计 ~1.7。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：5 篇 ≥3 → 明早 Opus 班选题（第五期）。

## 2026-10-28 08:43 每日 Opus 判断（第五期选题 + C-005-1 落档）

- 新增 confirmed P3：5 篇 ≥3 → 第五期选题。终选 3 篇（34938 自演化实证 / 34238 Δτ-Bench+STEWARD / 35579 Infinity Machine 限 L2 确认范围），3 张全过 QA；34027 列下期备选（双主卡与 34938 重叠 + 单 seed 优选）。见 selection-005.md。累计 24 张。
- Correction C-005-1（35316：Q2 vertical_port + 最小种子基线增益 + Table 3/4 冲突）已退回 Sol 修订：inc-l2-06-rev1-35316.jsonl → **P1/confirmed/park**（q2=vertical_port、q3=incremental、q4=partial；三点全接受，64.98/+28.02 标 Table 3 basis）。原记录保留。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：34027（备选）。

## 2026-10-28 06:17 巡检班

- 新增：7 篇（inbox/2026-10-28-0642，corpus 1644→1651，全文 7/7，材料 7/7 abstract_intro；收集 +8 中 1 个为 GitHub-only（langchain design-agent），arXiv 检索无命中留 inbox 待关联）。入库脚本一次因无 arxiv 字段项崩溃并连带误挪 inbox——已恢复，mv 改挂在校验断言之后。
- L1：inc-l1-05 7/7 完成（全 assessed；P3×3 / P2×4）。
- L2：inc-l2-07 7/7 完成（本班 to_l2 全部）。**4 篇 P3/confirmed/to_l3**（37651/36826/37255/34073）；36077 P3/pending_experiment；36774/37046 P2/park。
- 漏检抽查：0.7→0 名额，欠账累计 ~2.4。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：34027（备选）+ 本班 4 = 5 篇 ≥3 → 今晨 Opus 班第六期选题。

## 2026-10-29 06:17 巡检班

- 新增：2 篇（inbox/2026-10-29-0036 + 0643，corpus 1651→1653，全文 2/2，材料 2/2 abstract_intro）。
- L1：inc-l1-06 2/2 完成（全 assessed，P3×2）。
- L2：inc-l2-08 2/2 完成（本班 to_l2 全部）。**1 篇 P3/confirmed/to_l3**（37201——L3 须保留选择模型假设/最低起始分数敏感性/正向例外/timeout 排除边界）；35966 P3/pending_experiment/park（失败归因与护栏缺独立对照）。子卡 23 项：holds 7 / partial 14 / fails 1 / unknown 1。
- 漏检抽查：0.2→0 名额，欠账累计 ~2.6。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：36826（上期备选）+ 本班 1 = 2 篇 <3 → 今晨 Opus 班预计跳过（除非日内再增）。

## 2026-10-29 08:43 每日 Opus 判断

- selection-006 后新增 confirmed P3：2 篇（36826 备选 + 37201）<3 → 跳过。12:17 巡检班若再增，明日选题。

## 2026-10-31 12:17 巡检班

- 新增：12 篇（inbox/2026-10-30-0835，corpus 1653→1665，全文 12/12，材料 12/12 abstract_intro）。
- L1：inc-l1-07 12/12（assessed 10，out_of_scope 2：40191、38946；to_l2 10 = high 5 / medium 5）。
- L2：inc-l2-09 11/11（本班 to_l2 10 全部 + 遗留 high 0；抽查 1/1）。改判：3 篇 P2→P3 升档（升级判断见批次记录）。**7 篇 P3/confirmed/to_l3**（39122/40023/38392/39714/39358/39417/39813）；39158 P3/pending_experiment/park（缺独立提交/评测与噪声控制）；39508/39884 P2/confirmed/park。抽查 30851 维持 P2，漏检改判 0。
- 漏检抽查：seed=20261031，名额 1（预算 10×10%），audit_pool 2，抽中 30851。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：2（36826、37201）+ 本班 7 = 9 篇 ≥3 → 明晨 Opus 班可做 selection。

## 2026-10-31 08:43 每日 Opus 判断（第七期选题 + C-007-1 落档）

- selection-006 后新增 confirmed P3：9 篇 ≥3 → 第七期选题。终选 3 篇（39122 赞美训练劫持 / 38392 冗余护栏掩蔽侵蚀 / 37201 BiPA 轮次成本归因），均过视觉 QA（各 2–3 轮修复）；36826 上期理由仍成立继续落选。见 selection-007.md。累计 30 张。
- Correction C-007-1（40023 HEMO 记忆预载非同条件）已退回 Sol 修订：inc-l2-09-rev1-40023.jsonl → q4_fit=partial / pending_experiment / park（保留 P3/high）。原记录保留。
- 隔夜收集 +5 未评（06:17 巡检班丢失），12:17 班补。

## 2026-10-31 12:17 巡检班

- 新增：4 篇（inbox/2026-10-31-0840，corpus 1665→1669，全文 4/4，材料 4/4 abstract_intro）。
- L1：inc-l1-08 4/4（assessed 3，out_of_scope 1：38266；to_l2 3 全 medium）。
- L2：inc-l2-11 5/5（本班 to_l2 3 + 欠账补抽 2；遗留 high 0）。改判 2 篇 P2→P3（08671、39276）。**1 篇 P3/confirmed/to_l3**（39276 MemSteer）；08671 P3/pending_experiment/park（缺隔离机制新实验，另有首版与 v4 贡献边界待核）；39446 P2/park。补抽 32412、30017 均维持 P2，漏检改判 0。
- 漏检抽查：seed=20261043，本班名额 0（预算 3×10%），欠账 2.6→补抽 2（池 2 全抽），余 ~0.9 滚存。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：selection-007 用 9 篇后剩 0 + 本班 1 = 1 篇 <3 → 明晨 Opus 班预计跳过。

## 2026-11-01 08:43 每日 Opus 判断

- selection-007 后新增 confirmed P3：1 篇（39276）<3 → 跳过。周末 arXiv 停更无新增。

## 2026-11-02 08:43 每日 Opus 判断

- selection-007 后新增 confirmed P3：仍 1 篇（39276）<3 → 跳过。隔夜收集 +7 待 12:17 巡检班入库评分。

## 2026-11-02 12:17 巡检班

- 新增：7 篇（inbox/2026-11-02-0835，corpus 1669→1676，全文 7/7，材料 7/7 abstract_intro）。
- L1：inc-l1-09 7/7（assessed 6，out_of_scope 1：40917；to_l2 6 = high 2 / medium 4）。
- L2：inc-l2-12 6/6（本班 to_l2 全部；遗留 high 0）。改判 2 篇 P2→P3。**2 篇 P3/confirmed/to_l3**（40758 自演化规则膨胀基准、41216 TinyAstral 迁移）；4 篇 pending_experiment/park（42141/40901/41245/40721）。
- 漏检抽查：名额 1（预算 6×10%）但池 0（pending 篇均已 L2）→ 欠账 ~0.9+1→~1.9 滚存。seed=20261102。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：1（39276）+ 本班 2 = 3 篇 ≥3 → 明晨 Opus 班可做 selection。

## 2026-11-03 08:43 每日 Opus 判断（第八期选题，补跑）

- selection-007 后新增 confirmed P3：3 篇 ≥3 → 第八期选题。终选 3/3（39276 MemSteer / 40758 CLR-Bench / 41216 TinyAstral），各 2–3 轮修复后过视觉 QA；无 correction（TinyAstral 吸收主张、MemSteer 数字出入、CLR-Bench 类别构造偏置均按原文收窄展示口径）。见 selection-008.md。累计 33 张。

## 2026-11-04 08:43 每日 Opus 判断

- selection-008 后新增 confirmed P3：0 篇 <3 → 跳过。收集端自 11-02 晨无新产出（Grok 端静默，非本管线丢失）；巡检班待收集恢复后自动续评。

## 2026-11-04 18:17 巡检班（GitHub 查新首班）

- 查新来源：refs/lists 上游拉齐（selfimproving-agent→11-02、XMUDeepLIT→10-25、EvoMap→11-02；CUA 侧 Awesome-CUA 等 3 仓亦更新）。Grok 收件箱仍静默。事故与修复：build_corpus.py 全量重写曾丢 ~471 条 inbox 记录，已 checkout 恢复并改为临时文件差分 append；此后为常设流程。
- 新增：7 篇（GitHub 查新，corpus 1676→1683，全文 7/7，材料 7/7 abstract_intro）。
- L1：inc-l1-10 7/7（assessed 4，out_of_scope 3：12762/16429/21427；to_l2 4）。
- L2：inc-l2-13 4/4（to_l2 全部；遗留 high 0）。改判 1 篇 P2→P3（2608.11250）。**2 篇 P3/confirmed/to_l3**（2609.33378 递归 harness 蒸馏、2610.21082 SciΠvot）；2608.11250 P3/pending_experiment/park；2608.16876 P2/park。
- 漏检抽查：名额 0（预算 4×10%），欠账 ~1.9+0.4→~2.3 滚存（池 0）。seed=20261104。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：0 + 2 = 2 篇 <3 → 明晨 Opus 班暂不达标（除非夜间再增）。

## 2026-11-04 00:17 巡检班（GitHub 查新）

- 查新来源：selfimproving-agent list 再更新 → 2 篇新候选（corpus 1683→1685，全文/材料 2/2）。
- L1：inc-l1-11 2/2，**均 out_of_scope/exclude**（2611.00053 SIMIT 视觉自想象权重自改进；2609.36808 Spotter 冻结策略+VLM 反思不属 harness-RSI 收录口径）。无 to_l2，无 L2。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：维持 2 篇 <3。

## 2026-11-06 08:17 巡检班（收集端恢复）

- 新增：12 篇（inbox/2026-11-04-0935，Grok 收集端 11-04 恢复；corpus 1685→1697，全文 12/12，材料 10 abstract_intro + 2 abstract）。
- L1：inc-l1-12 12/12（全 assessed，to_l2 12 = high 8 / medium 4）。
- L2：inc-l2-14 12/12（to_l2 全部；遗留 high 0）。改判 3 篇 P2→P3（2611.03238、2611.04180、2611.04035）。**9 篇 P3/confirmed/to_l3**（2611.01834/02797/03238/04003/04180/04277/04952/02079/05139）；2611.00463 pending_material（§5.4 表头截断）；04035、03868 pending_experiment/park。子卡 83 项。
- 漏检抽查：名额 1（预算 12×10%）但池 0 → 欠账 ~2.3+1→~3.3 滚存。seed=20261106。
- to_l3 池：4（本班）+ 0 遗留 = 4 篇 ≥3 → 今日 Opus 班达标。
- 备用记录：2 + 9 = 11 篇 ≥3 → 今日 Opus 班达标。

## 2026-11-06 每日 Opus 判断（第九期选题）

- selection-008 后新增 confirmed P3：11 篇 ≥3 → 第九期选题。终选 3 篇（04952 能力链分步断裂 / 01834 LegoEnv 环境修复根因 / 05139 Meta² 离线编辑指导），各 1–2 轮修复后过视觉 QA；无 correction（05139 附录 H 脚手架差异记为 Sol 备注，Q4/P3 维持）。2609.33378 与上期 41216 同题、21082 SciΠvot 案例筛选自含等 8 篇落选。见 selection-009.md。累计 36 张。

## 2026-11-06 06:17 巡检班

- 新增：9 篇（inbox/2026-11-05-0919 收集端 11-05 产出，corpus 1697→1706，全文 9/9，材料 9/9 abstract_intro）。
- L1：inc-l1-13 9/9（assessed 7，out_of_scope 2；to_l2 7）。
- L2：inc-l2-15 7/7（to_l2 全部；遗留 high 0）。改判 1 篇 P2→P3（06321）。**4 篇 P3/confirmed/to_l3**（05445/05450/06444/06768）；06254 P2/park；06321、06049 pending_experiment/park。
- 漏检抽查：名额 1（预算 7×10%）但池 0 → 欠账 ~3.3+1→~4.3 滚存。seed=20261108。

## 2026-11-07 每日 Opus 判断（第十期选题）

- selection-009 后新增 confirmed P3：4 篇 ≥3 → 第十期选题。终选 3 篇（05450 ReScopeBench 陈旧内容修订 / 06444 EvoGuard 在线双技能选择器 / 05445 LIBRA 执行过滤工具图），各修复后过视觉 QA；无 correction。06768 落选（真机数为开发尝试汇总、冻结证据仅仿真单次、含人工介入、与 41216 同题；RoboDojo 数字存在正文/附录矛盾——备注退 Sol，84.4% 不再用于展示）。见 selection-010.md。累计 39 张。

## 2026-11-08 08:43 每日 Opus 判断

- selection-010 后新增 confirmed P3：0 篇 <3 → 跳过（06768 已落选，无其他候选）。隔夜收集 +12 待 12:17 巡检班入库评分。

## 2026-11-08 12:17 巡检班

- 新增：12 篇（inbox/2026-11-06-0937，corpus 1706→1718，全文 12/12，材料 12/12 abstract_intro）。
- L1：inc-l1-14 12/12（assessed 11，out_of_scope 1：08483? 不——06946 类边界研究入 to_l2；to_l2 11 = 本批 11 篇 assessed 全部 + needs_material 若干）。
- L2：inc-l2-16 11/11。改判 3 篇 P2→P3；**2611.03743 判定 P3/confirmed 但 next_action=exclude**（反馈学习进入 RL 权重，属范围外口径，理由见批次）；**5 篇 P3/confirmed/to_l3**（07048/07123/07372/07624/08318）；07051、06972 P3/pending_experiment/park（缺独立锚点/归因）；07469、07595 P2/pending_experiment/park；08483 P2/confirmed/park。子卡 63 项。
- 漏检抽查：名额 1（预算 11×10%）但池 0 → 欠账 ~4.3+1→~5.3 滚存。seed=20261109。
- to_l3 池：0 + 5 = 5 篇 ≥3 → 明晨 Opus 班达标。

## 2026-11-09 每日 Opus 判断（第十一期选题）

- selection-010 后新增 confirmed P3：5 篇 ≥3 → 第十一期选题。终选 3 篇（08318 任务 vs 验证器学习 / 07624 聚合分数盲区 / 07123 PromptOps 判官再调优），各 2–4 轮修复后过视觉 QA。07048 与 07123 同主卡、理论构造无 harness 数据落选。见 selection-011.md。累计 42 张。
- Correction C-011-1（07372 EnvOpt 归因未隔离、消融无数值/PDF 缺表）退回 Sol：需复读 PDF 表后复核 q4（疑 partial）、evidence_status、next_action 与 q3。
- 备注未退回：07123 两表 0.59/0.55 不一致（结论不受影响）；07624 AGE 修订用测试集标签单 seed。

## 2026-11-09 C-011-1 落档

- 07372 EnvOpt 修订：q4→partial、pending_experiment/park（P3/high 保留）；两项 holds 改 partial，"第三轴正交"确认撤回。PDF 表核对：11.17pp + 成本 -83.45% 成立，引言 16% 不支持；Table 2 显示 full 非全面优于 tools-only。原记录保留。

## 2026-11-10 08:43 每日 Opus 判断

- selection-011 后新增 confirmed P3：0 篇 <3 → 跳过（池内 07048 同卡落选、07372 已 correction 降为 park）。

## 2026-11-11 08:43 每日 Opus 判断

- selection-011 后新增 confirmed P3：0 篇 <3 → 跳过。

## 2026-11-12 06:17 巡检班

- 新增：9 篇（inbox/2026-11-09-0925，收集端恢复，corpus 1718→1727，全文 9/9，材料 9/9 abstract_intro）。
- L1：inc-l1-15 9/9（全 assessed，to_l2 9）。L2：inc-l2-17 9/9（遗留 high 0）。改判 2 篇。**5 篇 P3/confirmed/to_l3**（08644/09218/09030/09348/09291）；09318 降 P1/park（Q2 已解决类）；08723/08643 P2/park；08946 P3/pending_experiment。
- 漏检抽查：名额 1（预算 9×10%）但池 0 → 欠账 ~5.3+1→~6.3 滚存。seed=20261112。
- to_l3 池：0 + 5 = 5 篇 ≥3 → 今晨 Opus 班达标。

## 2026-11-10 14:17 巡检班（GitHub 查新 + arXiv 限流处置）

- 查新来源：selfimproving-agent list → 1 篇 2605.16757（材料 1/1 abstract_intro）；inbox 空。
- 过程异常：arXiv API 429 限流，RSI 单篇元数据重试一次成功；限流期间连带误写 l1_inputs.jsonl 重复行与错误 TSV，已当场清理（237→219 行，未提交）。
- L1（单篇快通道）：inc-l1-16 1/1 → **out_of_scope/exclude**（NeuroMAS 训练节点 adapters，冻结骨干≠不更新权重，非 harness 级自修改）；L2 按条件未执行。
- to_l3 池：维持 5。
