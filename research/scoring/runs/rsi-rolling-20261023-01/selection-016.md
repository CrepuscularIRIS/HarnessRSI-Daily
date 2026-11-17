# 第十六期 L3 终选与 Reel

- 日期：2026-11-17；run：`rsi-rolling-20261023-01`；规范：`problem-core-v1.1`。
- 执行席：**gpt-6-astra（本会话环境报告；fable槽位；未独立探测后端）**。仓库入口虽名为OPUS_REEL_PROMPT，本次不记作Opus 5.5。单席串行核对，没有额外模型会话。
- 输入：`batches/inc-l1-20.jsonl`、`batches/inc-l2-22.jsonl`中用户指定的4篇，原记录均P3 / confirmed / to_l3。
- 已读维护／范围／流程、SELECTION、PROBLEM_CORE、OPUS_REEL_PROMPT与[上期](selection-015.md)；四篇全文连同附录均已读。
- 结果：**选2篇，退回单篇Sol修订2篇；不补第三篇。** 此处是L3选择与追加纠正，不覆盖原始L1/L2，不改共享进度或候选池总数。

## 排列与终选

先看问题的实测依据、开放性和能力／判断增量，再核对执行。能力与判断不做数值排序；以下是阅读顺序，不是总分榜。

| 顺序 | 论文 | 原L2问题族／卡 | L3结论 |
|---|---|---|---|
| 1 | 2611.17696 Co-Sight Harness | F1/F2；attribute_and_patch_incumbent、evidence_gated_retention、diagnose_self_improvement | 选入：控制与知识两组加／减消融直接区分完成和内容质量；保留人工审批、未来自动修订与开发隔离边界。 |
| 2 | 2611.18533 ModHarness-RL | F1/F5；couple_context_and_weight_updates、attribute_and_patch_incumbent、evidence_gated_retention | 选入：固定压缩与动态纠偏的模块更新消融提供判断增量；不泛化成所有harness应采用的更新规律。 |
| — | 2611.17539 Verifiable pXRD | F3/F2；self_generate_the_curriculum、crystallize_executable_capability | 暂缓：C-016-1，实测面板参与早期人工开发；退回复核H06与迁移边界。 |
| — | 2611.17939 Can You Trust Your Finance Agent? | F1/F2；diagnose_self_improvement、attribute_and_patch_incumbent、evidence_gated_retention | 暂缓：C-016-2，七基线并非全部同后端；退回修订漂移与0.83阈值来源。 |

两篇入选原L2均为measured_own / open_failure；Co-Sight的capability和ModHarness的judgment在受限任务设置下可保留。前者提供可用控制基础设施而非已实现自主改进器；后者完整联合证据主要CodeSearch，不把其他环境的单模块结果当作联合系统泛化。

## 与已有53篇去重

完整对照 `reel/README.md` 的53个既有ID，本期无相同ID。主题比较优先明确机制和直接证据，不用新论文倒推旧论文的问题价值失效。

- Co-Sight与2610.37201 BiPA均涉及归因；BiPA侧重成本／选择噪声，当前篇分别添加、移除控制和知识组件，区分完成率与内容质量，非同一结论换标题。
- ModHarness与2611.15268都讨论harness／权重，但旧篇分知识与可靠性的承载层，新篇分压缩与纠偏的更新节奏；与2602.05832 UI-Mem的强指导压缩GRPO奖励差异也不同。
- 上述三篇历史SOURCE已细读。Finance接近2610.28798、2610.30499、2610.37201的漂移／虚假晋升主题，但本期退回原因是事实纠正，不是只因重复。pXRD的合成到实测科学任务不同，仍须先纠正开发面板边界。
- 版式对照既有QA描述及索引，不声称重新打开全部53张历史图。当前两图分别为控制／知识分流和全宽双速训练编排，非固定四格换文案。

## 全文覆盖与固定来源

本地全文位于 `research/fulltext/review-runs/rsi-l1-20261022-03/materials/`。四篇均为v1、HTML完整抓取；对应本run `materials/<id>.json`记录版本、URL、时间与完整性。此次核对无缺失全文；未重跑抓取、论文代码或实验。

| ID | SHA256 | 关键补读 |
|---|---|---|
| 2611.17539 | `6cc117672b0d1262b4594a16906942fd0860556da948bd50d99cda0eb8fc674e` | 单相／多相分别阅读，A.8.2–A.8.3的包组成、开发面板和诊断 |
| 2611.17696 | `f416bb980a88058fea33e061bad7b90ebc5f3c98f564904d42519ffb5599ba34` | §4、§5.7表7–8、§6与附录 |
| 2611.17939 | `0d57dd5ad753be120d94edd14f227de636276f634b4cdc5ca3c9c0dc3470c659` | 主结果、bootstrap范围、附录E后端替换 |
| 2611.18533 | `2d119df847d8a7d68243ae3ac49b20d0ed1ec817fa84d4dbd411338aecbe2228` | §3、表1/3、A.1/A.3、C.2/C.5与图12 |

没有另做池外抽样审计；此前遗留缺材料事项不在本次解决范围，不能据此宣布历史缺口关闭。

## 追加纠正与Sol回修单

### C-016-1 · 2611.17539 · pending Sol revision

**原记录目标**：inc-l2-22中H06关于生成／选择与最终实测评价隔离的`holds`，及实测迁移证据的叙述。原始记录保持不变。

**原文反证**：[v1附录A.8.3](https://arxiv.org/html/2611.17539v1)，本地L7651–7700：15个实测图谱“informed earlier human decisions about the framework and synthetic generator, making this a developmental experimental evaluation”。冻结evolver没看实测目标／沉积解，不等于整套系统开发未看该面板。另有可变模型alias、不同日期和推理预算；追加Sr重复由初始结果后选择且为同一标本。

**请求单篇修订**：重新评H06隔离条件（至少考虑partial），在biggest_gap／Q3证据边界明确developmental experimental evaluation。不得将15图谱称独立于全系统开发的迁移测试；保留新合成面板和同化学族窄范围的工具／指导包证据。不预先强制P3降档，由Sol按收窄证据重判。

**保留与限制**：单相27→69%并非多相演化结果；多相实测平均Rwp 7.90→6.71同时耗时27.0→50.2分钟，framework access 5.98还优于framework＋v6的6.49。v6指导与helper未单独消融；Sr命中是同标本补测，不是新标本泛化；框架访问补测应区分10次尝试与9次完成。拟合更好不等于结构唯一正确。

**L3动作**：暂缓，不制作海报。此回修单待总控转交单篇Sol；本席未启动修订模型任务，未宣称修订已完成。

### C-016-2 · 2611.17939 · pending Sol revision

**原记录目标**：inc-l2-22将七次基线称为“同配置”run drift，以及H32首项`holds`的该部分证据、0.83自然漂移阈值的解释。原记录不覆盖。

**原文反证**：[v1附录E](https://arxiv.org/html/2611.17939v1)，本地L1951–2000：“Six of the seven dev baselines and every test measurement ran on the SEC endpoint; the first dev baseline ran on the third-party index.” 最宽0.830 twin ratio来自run1→2，横跨后端替换。两后端81/81目标主文件覆盖不等于输出完全一致：40个共同非空query平均Jaccard .85、21/40相同集合、27/40同首条。

**请求单篇修订**：改写“七次完全相同配置”的事实表述，区分运行波动与后端替换；重新计算或限定同后端漂移，说明作者0.83声明阈值包含跨后端比较，不能直接称“完全同配置自然噪声17%”。复核H32对应判据与biggest_gap，而不是抹掉所有漂移证据。

**仍成立的证据**：run2–7同SEC后端的通过数仍跨105–123/149。成本比.341、CI[.216,.580]仍明显低于作者声明的.83阈值，不能借此纠正反称节费失效。成本臂准确率−3.7pp、CI[−8.9,+1.1]不证明非劣；准确率臂开发+14pp到测试+1.5pp、CI[−5.3,+7.2]。单代理、9道测试题、单优化campaign、无diagnosis-free臂，不能隔离诊断本身因果贡献。

**L3动作**：暂缓，待总控转交Sol单篇回修；不是自动否定P3，也没有实际发起或完成Sol重评。

## 成品与QA

| ID | 成品目录 | 最终状态 |
|---|---|---|
| 2611.17696 | [reel/2611.17696](../../../../reel/2611.17696/) | HTML/PNG/PDF/SOURCE/QA齐备；1800×1440，PDF1页；ready |
| 2611.18533 | [reel/2611.18533](../../../../reel/2611.18533/) | HTML/PNG/PDF/SOURCE/QA齐备；1800×1530，PDF1页；ready |

两张首版均底部裁切，明确判失败；各只重做一次，同步扩大画布／打印页并修正字体字重。最终PNG原尺寸与600px缩图已实际打开，文字、表格、限制和页脚完整；缩图细注须放大。渲染几何及本地字体加载检查通过，详见各QA与assets/render-check.json。结构检查不等于科学验证。

完成仓库自定义五件套契约，不声称原版paper2assets/paper2poster完整资产包、固定模板fill gates、PPTX或音频流水线完成。目录携带本地字体与许可，无外部资源依赖。历史53＋本期2＝55；rolling新增由36到38，另有早期第二期2篇，不能误算为15＋38。

没有git操作、子代理、无头Claude、论文代码执行、作者联系或外部发布；没有改动AGENTS.md、原始批次或其他任务产物。
