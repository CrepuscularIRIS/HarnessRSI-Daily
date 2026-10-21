# 领域卡修订提案（阶段末处理，批内不落地）

来源：cal-dev 聚合席 batch-report 与总控记录。按 PATTERN_PROTOCOL，生产期间只积累，不在批内改卡。

1. `make_the_improver_editable` F2：现文引用具体成员论文（Gödel Agent 2410.04444）的结果数字，泄漏进该类论文的盲评。提案：F2 条件改写为机制描述（"被接受成员需报告改进率与分母"），成员结果只留在 patterns/ 卡内统计段，不进条件文本。
2. `H31`（evidence_gated_retention 子卡）：开发集发现其口径把"理论成员"与"机制成员"混在一张子卡。提案：H31 条件文本区分"理论分析成员（无执行反馈）"与"门控留存成员"，或为前者单列子卡；范围裁定按 rubric A3 执行，不依赖卡归属。
3. `H26/H27`（amortize_improver 子卡）：holdout 步骤条件与 E.holdout 的适用边界重叠表述不清。提案：明确 H27 步骤 5 是检查问题（X 轴），E.holdout 只判实际留出证据。
4. 期望条目补稳定 ID：按冻结 rubric A4 语法为 patterns/ 各卡 S/F 条件补 `rsi:<main>/<id>` 形式的规范 ID（现卡内无显式 ID，两席自行拼装导致 53 项伪冲突）。属纯来源增补，需新版本号。
