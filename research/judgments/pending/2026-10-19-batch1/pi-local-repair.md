---
id: pi-local-repair
title: "Imitation Holds a Key to Evolution: Localized Repair and Verified Skill Acquisition for Adaptive Agents"
authors: "Kai Hu and Hua Huang"
first_seen: 2026-10-12
arxiv: "2610.16125v1"
openreview: null
code: "https://github.com/FriendOfYishan/PI"
code_commit: "58bc2861aa60f7720f5b994c9d4d31387fb63d43"
license: null
venue: "arXiv preprint"
tier: A
evolved: [skill, memory]
feedback: [execution, ground_truth]
evidence_level: retained
held_out: yes
budget_matched: partial
leakage_risk: low
code_status: released
checked: 2026-10-19
---

## 一句话
把结构化失败定位到单个步骤，小样本验证修补后，再凭完整任务通过的记录保留可复用技能。

## 机制
提出：符号控制器根据失败断言的输出路径定位阶段，从演示的前后状态差异检索作用匹配的片段，并补充枚举候选动作。
评测：一次只替换一个阶段，在两个完整订单历史组成的小数据上执行候选，随后进行完整任务审计。
接受/拒绝：局部目标断言通过才暂存补丁；最终完整审计决定能否增加未来复用所需的确认记录。
留存：以工具版本、阶段和目标为键保存成功/失败、累计激励与已通过任务标识；至少两个不同任务确认且启发式分数达到0.7才能提前复用。
改进器是固定的符号控制和证据更新规则，没有演化自身。它没有使用LLM或神经训练，按筛选规范属于持久L2闭环，但其实现是符号机制，不是LLM能力实证。

## 作者报告的证据
论文v1摘要报告：十个模拟工具世界、三次小试验预算下，600个冷启动留出组合任务全部成功；整轨迹控制为6.17%，表达能力相同的组合修复控制同样全部成功。
未见工具版本上，PI成功率70.0%，去除小试验为24.0%，自试验枚举为79.0%。探索性追加24个新版本学习任务后，首提成功率达到100%；此结果是已学习版本内留存，不是零样本转移。
这些是作者报告的符号环境结果，本卡没有运行代码或重新产生数字。诊断卡补读了v1在线正文第6.3–9节及实现附录说明；评分仍严格使用规定的本地提取文本，未把提取缺失的方差信息补进评分记录。

## 我们的诊断
- **证据等级**：retained。学习阶段改变明确持久状态，冻结评测时不更新，且重置/无留存控制用于区分当次修补与后续首提收益。更新机制没有被修改并比较，不属于improver证据。
- **留出与泄漏**：组合任务从演示和初始学习流中留出，任务标识隔离，冻结批次前后状态哈希相同。低风险限于本合成环境；公开角色映射、类型化血缘和结构化断言显著降低了诊断难度，不能外推自然语言场景。
- **预算与失败处理**：同组控制使用相同任务和小试验/完整提交上限，记录失败试验和访问行数。行阶段访问量只覆盖解释器执行，不包括检索、控制器计算或语料构建，也不是LLM token成本；总体成本对等仅partial。
- **最强的反驳**：强组合修复控制与PI持平，完美可辨识的小测试使激励阈值近乎冗余。收益可能主要来自人工给定的可分解接口，而不是其独有激励规则。

## 代码核查
固定提交：`58bc2861aa60f7720f5b994c9d4d31387fb63d43`。仅读取，未运行。
- `run_correction.py`第240–510行：检查`Controller`的条件化记录、两个任务确认和0.7门槛；`episode`显式限制小试验/完整提交，只在`learn=True`时强化；`frozen_batch`前后比较状态哈希。确认这些路径实现了文中修补与冻结边界。
- `verify_correction.py`：读取全部完整性检查。它枚举有限动作组合，断言小数据/完整数据合同结果一致、任务集合不重叠、反馈不包含正确动作和隐含阶段、冻结状态不变。看到断言存在不等于本卡验证运行通过。
- `run_online_adaptation.py`：读取全部；24个新版本学习任务与最终任务标识分离，0/6/12/24检查点调用冻结评测，并明确标注探索性后续。
- `PRIMARY_PROTOCOL.md`与`README.md`：核对固定种子、预算、强控制及有限环境声明。根目录树没有LICENSE文件，许可未确认，不能据公开可读推定自由复用授权。
没有核查发行压缩包中的每条日志、复现结果或检查上述区间之外所有环境实现。

## 相对已有工作的增量
相对Reflexion的反馈记忆、ExpeL的经验提炼和Agent Workflow Memory的工作流复用，本工作的可检验增量是把局部作用匹配、暂存修补、全任务审计与条件化复用分成独立步骤，并在有限接口中给出可辨识性假设和强组合控制。作者没有复现这些LLM方法，不能将跨论文数值视为优胜证据。

## 适合 / 不适合
适合研究有明确阶段、可执行断言、可重复小数据测试的工作流修补机制；接入需要可信血缘映射、完整审计及版本化证据表。
不适合直接当作开放式LLM代理已获泛化提升的证据，也不适合在缺少可靠完整验证器时凭两次通过就自动信任技能。使用代码前仍需确认许可。

## 一个值得验证的问题
当小测试以可控概率漏检，而完整审计保持可靠时，PI的激励门槛是否在相同总执行预算下优于简单已验证映射复用？同时测量误晋升、修补成功和持久表增长。

## 来源
- [论文v1](https://arxiv.org/abs/2610.16125v1)
- [固定代码提交](https://github.com/FriendOfYishan/PI/tree/58bc2861aa60f7720f5b994c9d4d31387fb63d43)
- [控制器实现](https://github.com/FriendOfYishan/PI/blob/58bc2861aa60f7720f5b994c9d4d31387fb63d43/run_correction.py#L240-L510)
- [完整性检查](https://github.com/FriendOfYishan/PI/blob/58bc2861aa60f7720f5b994c9d4d31387fb63d43/verify_correction.py)
- [在线后续](https://github.com/FriendOfYishan/PI/blob/58bc2861aa60f7720f5b994c9d4d31387fb63d43/run_online_adaptation.py)
