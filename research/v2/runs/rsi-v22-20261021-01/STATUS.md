# run 状态：SUPERSEDED（2026-10-22）

应用户要求停用 v2.2 双席打分流水线，改用新的打分方式（规格待出）。

- 中断点：218/930 已处置（169 得分；36+ 范围外；其余 needs_* 与单篇补评混合）
- 校准：已通过并冻结（rubric_frozen.md b44708af…，一致性 10 对/中位 1.875/100%≤10）
- 产物：r01–r20 批次全记录、rounds/ 检查点、两起 attempt 关闭违规处置记录均在位
- 可复用：queue.jsonl（含 930 篇 ID/版本/状态）、materials/（930 篇版本钉定全文 sha，文本在本地
  research/fulltext/review-rsI-v22-20261021-01/）、fetch/validate 工具链
- 未启动：r22a–r22d 批 manifest 已建未派（40 篇，占用即弃或新方式重排）
- 新方式启动时：另立 run_id；本 run 全部输入可直接继承，分数不带入
