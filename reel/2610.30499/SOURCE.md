# SOURCE — 2610.30499

- 论文：Can LLMs Improve Their Own Harness? A Controlled Study on ARC-AGI-3（Jens Lehmann, Sahar Vahdati；TU Dresden / Universität Hannover / TIB）
- 版本：arXiv:2610.30499**v1**（2026-10-21）
- 钉定全文：`research/fulltext/review-runs/rsi-rolling-20261023-01/materials/2610.30499.txt`（HTML 转文本，sha256 `19bdd2a9…be31`；正文 §1–§9 与附录 A–E 已通读，附录 F 只读了方法与可靠性段，附录 G 只读了重放协议段）
- 初筛记录：L1 `batches/inc-l1-02.jsonl` → L2 `batches/inc-l2-02.jsonl`（P3 / confirmed / judgment / to_l3）；L3 `selection-003.md`
- run：rsi-rolling-20261023-01，规则 problem-core-v1.1

## 结论（画报展示口径）

在“同一模型 + 固定 OpenCode 引导、5 个开发游戏反馈、两次修订”的协议下，27 条谱系的开发增益（+8.42）明显高于留出增益（+2.80，区间含 0），适应差距 5.62 [1.78, 9.77]；15 条升、12 条降。这说明“能搭出 harness”与“能把它改得在未见游戏上更好”需要分开测，不说明自改普遍无效。

## 断言 / 数字 → 原文

| 画报位置 | 内容 | 原文出处（行号指钉定文本） |
|---|---|---|
| 标题 / 副标题 | 构建能力 ≠ 改进能力；OpenCode 引导、5 开发游戏、两次修订、20 留出游戏 | Abstract（L74–102）；§1 末段（L199–209）；§4.2（L868–913） |
| 指标条 | 开发 +8.42、留出 +2.80 [−1.44, 7.35]、G₂ 5.62 [1.78, 9.77]、15 升 12 降、符号检验 p=.70 | §5（L964–1029）；Abstract |
| 问题卡 | 四种能力（构建、修复、证据→修改、选出能迁移的修改），前三不蕴含第四 | §2（L517–523） |
| 协议图 | 冒烟检查 2 个开发游戏、只查运行不看分、≤10 次修复；修订输入为自身源码 / 轨迹 / 分数 / 动作 / 费用；可保留父版本；无人工编辑 | §4.2（L894–910）；附录 A “Stage lifecycle”（L1511–1522） |
| 留出栅栏 | 20 个留出游戏不参与提案、接受、停止、选择；开发游戏战役前随机选定 tr87/vc33/r11l/bp35/ft09；本地与官方服务重放核分 | §4.2 “Held-out evaluation”（L918–931）；附录 A “Development split”（L1493–1509）、“Hosted replay”（L1524–1533）；附录 C Table 2 “Strict test” |
| 固定条件 | 同一 profile 构建与游戏、无联网、无跨游戏状态、24 h / 1 GiB；无统一美元或调用上限 | 附录 A “Repository boundary”（L1483–1491）、“Resource bounds”（L1629–1642） |
| 谱系图 | 27 条 H0/H1/H2 留出 RHAE | 附录 D Table 3（L1913–2201），本项目逐行重绘；均值 24.54 / 25.87 / 27.34 由本项目按表复算，与 Table 11（L3043–3079）一致 |
| 谱系图高亮 | Sol-high #1 20.38→29.24→53.56；Sol-xhigh #1 43.95→18.49→21.99 | Table 3；§6.1（L1145–1160） |
| 黄色区间 | 同一 H2（Sol-high #1）重跑 10 次：43.38–55.37，SD 3.99；事后选定 | §5 首段（L952–963）；附录 D.1 Table 10 与正文（L2766–2965） |
| 平局说明 | Sonnet 5 #3 表中 0.14→0.14；作者“Categories use unrounded changes”，计为下降 | Table 3；Figure 4 注（L1089–1090）；§5 “15 gains, 12 losses, and no ties” |
| 区间说明 | 100,000 次整条谱系自助重抽；只描述本研究池与固定游戏划分 | 附录 D “Uncertainty estimation”（L2218–2224） |
| r11l 影响 | 去掉 r11l 差距 5.62→3.02（描述性） | 附录 D（L3014–3020） |
| 事后选择表 | 保留 H0 24.54/$10.30；部署 H2 27.34/+2.80/$7.57；按开发分 29.06/+4.53/$9.15，选 9/6/12；oracle 30.66/+6.13/$9.80；+4.53 区间 [0.81, 8.68] | 附录 D Table 5（L2339–2437）及其前文（L2282–2337）；§5（L1030–1050） |
| “没有一次保留父版本” | “every scored trajectory changes its implementation” | §7 “Abstention is part of adaptation”（L1344–1347） |
| 四象限 | H0→H2：9 / 6 / 9 / 3 | 附录 D Table 7（L2467–2557）；§5（L1052–1072） |
| 费用 | 均值省 $2.72、中位 −$0.54；总计至少 $18,129.27 | §5（L1066–1094）；Table 6、Table 8 |
| 修订行为 1 | 54 次修订均检查逐游戏开发证据、diff 都针对至少一个有证据的问题、都通过运行检查 | §6.2 “Do broader edits…”（L1251–1258） |
| 修订行为 2 | 第一次修订 22/27 reorient、4 extend、1 preserve；无 replace | §6.1（L1133–1141） |
| 修订行为 3 | 大范围重写 +3.75 对局部 −0.20；交付 36 次 +2.48、反应式 18 次 −0.76，区间含 0 | §6.2（L1259–1294） |
| 修订行为 4 | GPT-5.6 Sol 两次独立编码；未与人工比对；diagnosis 0.35、incumbent protection 0.47、resource metareasoning 0.29 < 0.67 | §6.2 “Blinding and reliability”（L1182–1247）；§8（L1415–1423） |
| 限制 | 一个基准 / 两次修订；公共游戏可能在预训练中；每快照一次评测；无统一推理预算；Tycho 等 100 RHAE 但流程不同 | §8（L1398–1423）；§7（L1312–1342）；附录 D “Human-steered reference systems”（L2637–2694） |

## 示意与重绘

- 谱系图、指标条、四象限、事后选择表均按原文表格数值重绘；顶部像素色条与协议图中的方块为装饰 / 示意，不代表具体游戏。
- 本项目没有运行实验，也没有复现结果。

## 核对结论

与 L2 记录一致，无 correction。展示边界：结论限该固定模型 / 固定引导 / 五游戏反馈 / 两次修订协议；模型间排名只是描述；每快照单次评测。
