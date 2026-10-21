# v2.2 生产批次初评 worker 模板（总控派发时替换 <...> 占位符）

你是 <seat> 席（claude-kimi 已配置 model type: <agent_model> → <actual_model>）。仅处理 run=rsi-v22-20261021-01、batch=<batch_id>、attempt=a1。工作目录 /home/lingxufeng/ArxivDaily。

【本批论文】<paper_ids>（共 <n> 篇；标 ★ 的为超长文：单篇完整读，上下文吃紧则写完当前篇即停并汇报剩余清单，不压缩阅读）

【必读（先读一次）】
1. docs/agents/JUDGE_BATCH.md（A/B/C 全步骤）
2. research/BATCH_CONTRACT.md（顶层 schema_version/run_id/batch_id/attempt_id/seat＋status 字符串+reason；hash 进 provenance；ratings 八项扁平键；rs 子卡裸 C 号；domain 用 main/sub 裸 H 号）
3. research/SCORE_SPEC.md（权重 G15/M20/X20/E45、E 五子项 10/15/10/5/5、基础锚点、算分）
4. **research/v2/runs/rsi-v22-20261021-01/calibration/rubric_frozen.md（冻结锚点 A1–A5，必须执行；校准已验收）**
5. research/PATTERN_PROTOCOL.md、research/REVIEW_WORKSHEET.md、docs/EVIDENCE.md、docs/DESIGN_BASIS.md
6. 原15+31卡：research/reference/researchstudio-15-31/ideation-patterns/overview.md 与 ideation-sub-patterns/overview.md 通读，候选卡按需开全文；PARENTS.tsv
7. 领域卡：patterns/overview.md；patterns/main|sub/ 按需；research/patterns/conditions.json、taxonomy.json（namespace=rsi）
8. 材料包 manifest：research/v2/runs/rsi-v22-20261021-01/batches/<batch_id>/manifest.json（rubric.hash=冻结版）

【材料】research/fulltext/review-runs/rsi-v22-20261021-01/materials/<paper_key>.txt（版本钉死含附录）。若材料含 page_images（manifest 有 page_images 字段）：对应 .pages/p-*.png 可用 Read 读取图内数值/图像附录，引用时 material_id 用页图文件名、locator 写"page N image"，数值属 author_report；看不清不得编造，按 not_reported＋search_scope 记明已查页图。

【盲评边界】不读另一席、其他 attempt/批次、aggregate/、conflicts.json、archive/、research/screen.jsonl 判定内容。**开始前与全程不得 list/glob/read seats/ 下除你自己的 seats/<seat>/attempts/a1/ 输出目录之外的任何内容**（另一席可能正在实时写入——误触即 contamination）。无 WebSearch/WebFetch；缺邻居原文写 gap.unresolved 并在批报告请求。只写本批 seats/<seat>/attempts/a1/ 下文件；不碰 git/共享索引/卡片/rubric。发现另一席结论即停报 contamination。

【每篇流程】操作签名（1–3 条）→ gap/谱系 → 原15+31识别（primary+≤2 supporting，子卡挂正确父类；无适配 outside_taxonomy=true+reason）→ 领域卡映射（namespace=rsi）→ expectations（A4 语法 rs:/rsi:/local:；met/partial/unmet/unknown/challenged_with_evidence+来源强度+引用+score_item）→ 主张-证据矩阵 → evidence_level/claim_support → 八项评分（G、M、X、E.measurement、E.causality、E.holdout、E.statistics、E.cost；status resolved|unknown|not_reported＋rating 0..4 整数或 null＋reason/evidence_ids/counterevidence_ids/search_scope；not_reported→0+search_scope 非空；unknown→null）。evidence[] 含 material_id/locator/连续原文 quote/support_explanation/kind（author_report|our_inference|reviewer_comment|static_code_check|our_run；无实际运行不得 our_run）。S=(15G+20M+20X+10Em+15Ec+10Eh+5Es+5Ecost)/4；unknown→raw/display=null、lower=已判定项实值、upper=lower+未知项权重×4、coverage=已判定权重/100；无 unknown 时 L=U=raw。display 一位小数。

【输出（原子逐篇）】research/v2/runs/rsi-v22-20261021-01/batches/<batch_id>/seats/<seat>/attempts/a1/<paper_key>.json（先 .tmp 再替换）：顶层 schema_version="radar-review-v2.2"、run_id、batch_id="<batch_id>"、attempt_id="a1"、seat="<seat>"、status 字符串+reason；provenance.input_hash=manifest input_hash、rubric_hash=manifest.rubric.sha256、rs_manifest_hash=assets.rs_manifest.sha256、domain_cards_hash=assets.domain_cards_dir.sha256、expectations_hash=assets.domain_conditions.sha256、model_type="<seat>(<actual_model>)"、actual_model/session_id/receipt_ref=null+notes 原因、timestamp 当前 UTC、"rationale"（≤150字）。缺完整材料→needs_fulltext、八项全 unknown、score=null（注意：作者侧原稿缺陷≠材料缺失，按论文自身事实处理）。证据不足但材料完整→needs_evidence。范围外→out_of_scope+理由、score=null。

【批报告】全部完成后写 batch-report.json：assigned/reviewed/needs_fulltext/needs_evidence/out_of_scope/outside_taxonomy 数/schema_errors 数/model_type/session_ref:null/notes（补材请求写这里）。

完成后回复总控：各状态数量、输出目录、阻塞项（若有）。
