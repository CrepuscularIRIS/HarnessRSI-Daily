# 苏格拉底式技能学习：教练边看边评，模型自己写 Skill——相对“无 Skill”收益明确，相对其他协议收益更小、也更不确定

*Reel 解读：[arXiv 2610.17860v1](https://arxiv.org/abs/2610.17860v1)，作者 Letian Zhu、Han Li、Yifan Yao、Xinping Lei、Xinyu Che、Jiahao Wang、Dianyi Wang、Yucheng Fu、Jiakai Wang、Zhiqi Bai、Wenbo Su、Jiaheng Liu（南京大学；阿里巴巴集团）。HarnessRSI Daily 评分 69，★★。代码：[NJU-LINK/Socratic-Skill-Learning](https://github.com/NJU-LINK/Socratic-Skill-Learning)。*

## 系统改变了自己的什么

被改变的是一个 **Agent Skill 包**：一个 `SKILL.md`，加上可选的脚本、参考资料和资源文件。模型权重始终不更新。在苏格拉底式技能学习（SSL）中，两个模型围绕同一个任务族工作。**学生（Student）**（也就是之后真正解题的那个模型）是唯一操作环境的智能体，也是 Skill 包的唯一作者。**教育者（Educator）**（更强的模型）对学生近期工作和当前 Skill 包只有只读权限，可以解释、质疑、诊断、建议检查，或者保持沉默。学生可以质疑、测试、调整或拒绝这些建议。

学习阶段只使用一个可执行的**锚点（anchor）**任务和公开的任务族说明（不变量与允许的变化范围）。共 3 轮，每轮结束后由一个全新的求解器在重置后的锚点上测试 Skill 包，其轨迹和验证器反馈进入下一轮。只有**最终的 Skill 包**被冻结，并在全新的求解会话中、于同一任务族的留出成员上评测。论文没有描述按轮次挑选最优包，也没有对包的修改设置接受/拒绝闸门。

两种调度决定教育者何时复盘：

- **Fixed-Window SSL（固定窗口）**：学生每完成 g 次工具调用复盘一次（主条件 g = 10，另比较 5 和 20），每轮另有一次收尾复盘。
- **Issue-Guided SSL（议题引导）**：教育者的每条指导变成持久的*学习议题*（焦点 + 验收标准 + 关联修订）。首次复盘（第一次修订时或经过一段预热的工具调用后）之后，只有议题新开、变化或重开时才复盘；“已验证关闭”需要指导之后的一次成功检查，锚点上与之矛盾的新求解器反馈可以让议题重开。

## 基准与主要结果

作者构建了 **SKILLTRANSFERBENCH**：35 个任务族、408 个可执行用例、六个领域，由专家与智能体协作，从六个已有基准改编而来。主队列保留“至少有 5 个已验证留出用例，且在全目录 No-Skill 筛查中至少有两次非满分结果”的任务族：22 个任务族、155 个留出用例。论文没有说明筛查运行是否独立于作为基线报告的 No-Skill 重复；若二者重叠，按 No-Skill 非满分结果挑选任务族可能抬高所有方法的增益（这是我们的推断，不是论文的结论）。得分为按任务族宏平均的 Avg@3（每个任务族权重相同；每个任务族与条件做 3 次独立的学习运行）。学生与求解器为 Qwen3.7 Plus；教育者或直接作者为 Qwen3.7 Max。

| 方法（Qwen 主队列，效用） | 效用 | 相对无 Skill 的增益，百分点 [95% CI] |
|---|---|---|
| No Skill | 0.723 | – |
| Expert Authoring（Max 直接写包） | 0.728 | +0.46 [−5.46, 6.56] |
| Post-hoc Teaching | 0.748 | +2.44 [−3.36, 7.90] |
| 改造版 Trace2Skill | 0.761 | +3.76 [−0.50, 8.96] |
| 改造版 SKILL-KD | 0.751 | +2.76 [−1.59, 8.09] |
| **Fixed-Window SSL** | **0.801** | **+7.75 [3.53, 12.68]** |
| **Issue-Guided SSL** | **0.805** | **+8.18 [3.54, 13.57]** |

两种 SSL 调度在总体和六个领域中都排名第一、第二。Fixed-Window SSL 比改造版 Trace2Skill 高 3.99 个百分点（95% 配对任务族自助法置信区间 [1.45, 6.49]），比改造版 SKILL-KD 高 4.99 个百分点（[1.79, 8.48]）。全通过率（每项私有检查都通过）从无 Skill 的 32.50% 升到 49.49%（Fixed-Window）和 50.82%（Issue-Guided）。头条效用是三次重复的均值（Fixed-Window 为 0.772、0.799、0.831；SD 0.030），每一次 SSL 重复都高于对应的 No-Skill 重复（0.719、0.730、0.721）；改造版 SKILL-KD 的三次重复（0.746、0.756、0.750）同样如此。论文没有报告 Trace2Skill、Expert Authoring、Post-hoc Teaching 的各次重复。

## 决定收益是否可信的对照实验

- **所有方法使用同一求解器、同一批留出用例和同一验证器。** Expert Authoring、Post-hoc Teaching 和两种 SSL 都采用 3 轮学习并带新求解器的锚点反馈；其中 Expert Authoring 由外部的 Max 模型（而非学生）探索并写包。改造版 Trace2Skill（对种子包生成的轨迹做并行补丁）和 SKILL-KD（三次访问锚点并编辑规则）不使用这套轮次回路。让 Max 自己写包（0.728）并不比无 Skill 好，其增益的置信区间跨过 0。Fixed-Window SSL 比它高 7.29 个百分点（[3.62, 11.44]），比 Post-hoc Teaching 高 5.31（[2.34, 9.09]），并且学习阶段 token 比 Post-hoc Teaching 少 21%。
- **三组模型（共享的 lite 子集：10 个任务族、77 个用例）。** 相对无 Skill 的增益（百分点），顺序为 Fixed-Window / Issue-Guided / Expert Authoring / Post-hoc Teaching：Qwen +4.1 / +4.5 / +1.1 / −0.7；DeepSeek +3.1 / +2.5 / +1.2 / +0.5；Kimi +8.2 / +7.4 / +5.8 / +4.1。DeepSeek 与 Kimi 只重复一次。Fixed-Window 减 No Skill 的区间为 [1.02, 8.03]（Qwen）、[−4.63, 13.03]（DeepSeek）、[2.48, 15.62]（Kimi），因此 DeepSeek 的 +3.1 与 0 无法区分。Fixed-Window SSL 在三组模型上都胜过 Post-hoc Teaching（分别高 4.88、2.54、4.09 个百分点），但该子集上这一对比没有给出区间；而 Fixed-Window 减 Expert Authoring 的配对置信区间在三组模型上都包含 0（[−0.83, 7.14]、[−1.93, 7.15]、[−2.33, 7.98]）。
- **复盘调度（Qwen，主队列）。** 固定 g = 5：效用 0.776，每次运行 9.56 M token；g = 10：0.801，6.89 M；g = 20：0.776，6.61 M；Issue-Guided：0.805，5.72 M。Issue-Guided SSL 用 60.6 M 教育者 token，对比 g = 10 的 158.2 M（少 61.7%），总学习 token 少 16.9%，每个教育者 token 带来的迁移增益是 2.75 倍。在 DeepSeek 与 Kimi 上教育者 token 分别少 63.8% 和 77.4%；总学习 token 在 Kimi 上下降，在 DeepSeek 上反而上升（每次运行 20.01 M 到 21.11 M）。
- **过程证据（观察性）。** 常规复盘中给出指导的比例从第一轮的 73.0% 降到第三轮的 16.1%，同时锚点效用从 0.824 升到 0.990。收到指导后，学生下一次调用写入或编辑文件的概率高 23.9 个百分点（[13.0, 36.1]），十次调用内 Skill 包发生变化的概率高 38.6 个百分点（[10.7, 57.8]）；后一对比只覆盖 193 个十次调用窗口中的 112 个，其余窗口缺少起止两端可比的 Skill 版本。作者明确这些只是关联，因为复盘决策本身就在响应学生正在进行的工作。一个个案（HTML 财务核验）显示学生把通用算术换成财务关系式，新求解器在一份未见过的报表上通过了 4/4 项检查。这只是一个任务族的一次重复，而且该任务族并不偏向 SSL：Expert Authoring 为 1.000，Fixed-Window SSL 为 0.917（表 9）。

## 增益缺失、较小或在噪声之内之处

- **四个基线的增益区间都没有越过 0。** Expert Authoring、Post-hoc Teaching、Trace2Skill、SKILL-KD 相对无 Skill 的增益置信区间都包含 0；只有两种 SSL 调度的区间在 0 之上。
- **Fixed-Window 与 Issue-Guided 没有被区分开。** 主队列上是 0.801 对 0.805，各次重复间的 SD 分别为 0.030（Fixed-Window）和 0.036（Issue-Guided）。在共享 lite 子集上，三组模型的 Issue 减 Fixed 置信区间都包含 0（[−0.84, 1.44]、[−5.34, 3.14]、[−4.72, 2.89]），DeepSeek 与 Kimi 的点估计还略偏向另一边（0.784 对 0.779；0.762 对 0.753）。论文自己的表述是效用保持在 Fixed-Window SSL 的一个百分点之内；这是效用相近而教育者 token 更少，而不是效用提升。论文没有给出主队列上 Issue 减 Fixed 的区间，所以主队列上“未被区分”是我们根据各次重复的 SD 做出的推断。
- **复盘间隔并非可直接读出的最优值。** 效用随 g 非单调（g = 5、10、20 分别为 0.776、0.801、0.776）；0.025‡ 的差距与 Fixed-Window 各次重复的 SD 0.030 同量级，论文也没有说明 g = 10 为何成为主条件。
- **增益在任务族之间不均匀。** Fixed-Window SSL 在 22 个任务族中有 16 个相对无 Skill 提升。有四个下降：Bank transaction filter 0.678 到 0.593，SPARQL professors 0.706 到 0.680，Financial documents 0.921 到 0.913，XLSX structure 0.933 到 0.923；ACL inheritance 与 SQLite truncation 持平。最大的四项增益（DB WAL recovery 0.473 到 0.884，Flask 0.408 到 0.690，Organization JSON 0.778 到 1.000，HTML finance verification 0.731 到 0.917）约占宏平均增益 7.75 个百分点中的 5.0‡ 个百分点，而且这些增益并非 SSL 独有：在 DB WAL recovery 上，改造版 Trace2Skill（0.905）和 SKILL-KD（0.901）高于 Fixed-Window SSL（0.884）；在 Organization JSON 上，Expert Authoring、Post-hoc Teaching 与 SKILL-KD 同样达到 1.000；在 HTML finance verification 上，Expert Authoring（1.000）和 Post-hoc Teaching（0.944）高于 Fixed-Window SSL（0.917）。按用例看（155 个），Fixed-Window SSL 提升 72 个、持平 59 个、退步 24 个。
- **基线排序随队列而变。** 在主队列上 Post-hoc Teaching（0.748）高于 Expert Authoring（0.728）；在共享任务族上，它在每组模型里都落后于 Expert Authoring。这一顺序翻转处于噪声之内：主队列上 Post-hoc 减 Expert 的配对区间包含 0（[−1.57, 5.64]），共享任务族上 Expert 减 Post-hoc 的区间（[−1.28, 6.05]、[−0.89, 2.23]、[−1.13, 4.76]）同样包含 0。论文把共享任务族上的顺序解读为支持“边练边指导”而非“事后复盘”。
- **成本。** Issue-Guided SSL 节省的教育者 token 按 token 计（含缓存输入），不是美元。每次运行 token：Expert Authoring 4.95 M，Post-hoc 8.71 M，Fixed-Window 6.89 M，Issue-Guided 5.72 M。改造版 Trace2Skill 与 SKILL-KD 的成本不在同一统计口径（SKILL-KD 的审计为每次运行 1.94 M token）。
- **作者自述的范围。** 研究采用共享的单锚点设定；局限性一节指出，还需要更受控的比较来分离教育者、复盘时机和议题结构各自的贡献。Issue-Guided SSL 同时改变了复盘触发条件、上下文和后续对话策略。

## 我们的解读（Our read）

HarnessRSI 评分 **69**，档位 ★★，证据等级 **retained**：冻结的 Skill 包在新求解会话中、于同一任务族的留出成员上确有帮助，但改进机制本身只以协议变体的形式做了比较（谁来写、何时复盘）。论文报告了在每个任务族未见变体上的留出评测，主队列上三次重复的配对任务族自助法区间，10 个任务族子集上的三组模型，四种协议与各复盘调度的 token 成本，以及过程分析。论文没有报告：各协议之间按 token 匹配的比较；针对公开源基准的污染或记忆检查（论文只说明私有测试与参考解答放在智能体工作区之外）；向不同任务族的迁移；改造版 Trace2Skill 与 SKILL-KD 在同一口径下的成本或调参预算；分离教育者、复盘时机和议题结构的消融。基准由作者自己构建，主队列是按 No-Skill 筛查挑选的。

*标有 ‡ 的数字由我们根据论文数字计算，详见 SOURCE.md。*
