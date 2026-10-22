# run rsi-v3-20261022-01 — HarnessRSI Daily v3 全量重打分

- 触发：用户 2026-10-22 授权「用 v3 思路对仓库全部论文重新打分，之后 Opus 挑选高质量做 Reel」。
- 规则版本：sol-batch-v3（research/v3/spec/ 副本，SHA256SUMS.txt 为准；来源 ~/radar-scoring-v3-draft 2026-10-22 修订版，含 CC 内置 Subagent 并行派批条款）。
- profile：rsi-v3，G=15 M=20 X=20 E=45；screen_score=(15G+20M+20X+45E)/4。
- 执行模型：单席 6.1 Sol = CC Agent model type `sonnet`（用户 CLAUDE.md 映射 ANTHROPIC_DEFAULT_SONNET_MODEL → gpt-6.1-sol；实际路由以 worker transcript 为准）。禁无头 claude -p / cc -p。
- 并发：默认 4 个评分 Subagent 滚动补位；无限流可升至 6–8；每批 10–20 篇上限、实际按总字符预算 480K 决定（材料均 ~81K 字符/篇，典型 4–12 篇/批，共 177 批）。
- 范围：仓库当前全部论文 = v2 queue 930 篇（材料复用 research/fulltext/review-runs/rsi-v22-20261021-01/materials/，sha 钉定）+ inbox 新增 3 篇（2610.26426/2610.16523/2610.24649，本轮钉定于 research/fulltext/review-runs/rsi-v3-20261022-01/materials/），共 933 篇，material_level 全部 full。v2 分数不作为输入。
- 排除：inbox/processed/2026-10-21-1835.jsonl 为 GitHub 线索（无 arXiv ID），不属论文评分范围。
- 卡片版本：patterns/ 整目录 sha256 汇总 343dc4a1c6b58e84（51 文件）；researchstudio-15-31 冻结副本 c13954d440a031d9（54 文件）。卡片不加权。
- 材料：inputs.jsonl 逐篇 text_path+sha256（930 复用 v2 钉定件 + 3 新钉定，全部 complete）。
- Git HEAD（run 创建时）：09622359087bc35e14674a461f75bc476ad3386d
- 工具：make_batches.py（分组）、check_batch.py（机械校验：ID 一一对应/档位范围/算术/字段）。结构通过≠科学验证。
- 产物：batches/bNNN.jsonl（每篇一行）、batches/bNNN-inputs.tsv（总控写）、progress.md（总控写）。评分后按 spec/SELECTION.md 出 selection.md → Opus 5.5（model type fable）核对 ≤15 候选并制作 Reel（≤9）。
