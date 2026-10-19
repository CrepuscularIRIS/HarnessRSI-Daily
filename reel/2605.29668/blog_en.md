# An agent that edits its own instructions, and keeps an edit only if it breaks nothing

*GRASP (arXiv 2605.29668) gates every self-written skill edit on a balanced held-out probe*

A common way to make an LLM agent improve itself is to let it write notes after it fails: “check the units before answering,” “always query the record first.” The notes go into the prompt next time. The approach is cheap and needs no weight updates, but it has a quiet failure mode. A note written to fix one failed task can change how the agent behaves on tasks it already solved, and an append-only memory never checks.

GRASP (Gated Regression-Aware Skill Proposer), by Johannes Moll and colleagues, takes that failure mode as its starting point. The agent still writes its own guidance, as a small library of Markdown “skills.” But every proposed change to that library has to pass a test before it is kept: on a balanced set of held-out cases, it must fix more than it breaks.

*Figure 1 (shown on poster.png). GRASP overview: run the agent, collect failing and previously passing episodes, propose skill edits on a forked copy of the library, score each candidate on a balanced probe, and accept it only on net improvement with no new regressions. Figure from the authors' repository github.com/jomoll/GRASP (MIT License); the paper is licensed CC BY 4.0.*

Paper: https://arxiv.org/abs/2605.29668 · Code: https://github.com/jomoll/GRASP

## What the system changes about itself

The only thing GRASP changes is its skill library: short Markdown documents, each with a “when to use this” section and correct and wrong examples. The base model's weights stay fixed. At most 10 learned skills fit in the library, and up to 3 relevant skills are injected into the prompt at each turn. The signal for change is the agent's own traces: which development tasks it failed, and which it passed.

## How an edit is proposed and judged

After each batch of development tasks, failing traces are classified by failure mode and grouped. A writer model then samples K candidate edits. Each one adds a skill (ADD), modifies an existing skill (MODIFY), or removes one (REMOVE). Adding is blocked when the library is full unless the same edit also removes a skill.

Each candidate is applied to a copy of the library and tested on a probe: half previously failing and half previously passing development cases, drawn from earlier batches. The same probe is also run with the current library, so the comparison is causal rather than absolute. A candidate's score is its fixes minus its regressions, both relative to that baseline run. The best candidate is applied only if the score is positive and it adds no regressions beyond the baseline. If no candidate clears that bar, the library does not change. At the end of training, the library from the best validation epoch is restored.

## What the paper reports

The main testbed is clinical: agents call a FHIR health-record API on MedAgentBench, MedAgentBench-v2 and FHIR-AgentBench. The authors use five base models and compare against five self-improvement methods (Sequential and Batch memory, ExpeL, Evo-MedAgent, SkillX). Test and out-of-distribution (OOD) splits are never used for training, checkpointing or hyperparameter selection. Results are mean ± standard deviation over 5 seeds for gpt-oss-120b and DeepSeek, and 3 seeds for the other models.

**Table 1. MedAgentBench with gpt-oss-120b, accuracy in % (mean ± s.d., 5 seeds), recomputed from the authors' released per-seed results.**

| **Method**        | **Test**    | **OOD**     |
|-------------------|-------------|-------------|
| No skills         | 40.6 ± 3.9  | 8.7 ± 3.2   |
| Sequential Memory | 41.2 ± 5.5  | 16.7 ± 15.6 |
| Batch Memory      | 34.4 ± 8.0  | 13.0 ± 8.1  |
| ExpeL             | 49.1 ± 6.3  | 12.0 ± 5.2  |
| SkillX            | 53.1 ± 4.6  | 21.3 ± 3.6  |
| Evo-MedAgent      | 67.8 ± 14.1 | 31.3 ± 21.7 |
| GRASP             | 88.8 ± 5.8  | 56.3 ± 14.5 |

With gpt-oss-120b on MedAgentBench, GRASP reaches 88.8% test accuracy, against 40.6% without skills and 67.8% for the strongest baseline, Evo-MedAgent. On the OOD split the numbers are 56.3% versus 31.3%, with a wide spread across seeds. The gains are not uniform. On FHIR-AgentBench, GRASP scores 54.5% against 52.0% without skills, and two baselines score slightly higher. Outside medicine, on four AgentBench environments with gpt-oss-120b, GRASP improves ALFWorld from 23.3% to 51.7%, WebShop from 20.7% to 41.3% and DBBench from 65.6% to 70.6%. It is flat on the open-ended OS environment (48.6% to 49.5%).

## Is it the gate or the writing?

The ablations separate the two. When every proposed edit is applied without testing (one proposal per update), MedAgentBench test accuracy is 40.1%, the same as using no skills at all. With four proposals but still no gate, it is 63.5%. Variants that keep the gate but drop other parts (failure clustering, the regression term, or the ability to modify and remove) stay between 80% and 84%, under a separate 5-epoch budget. Writing skills alone does not explain the gain; the validation step does.

Two further findings matter for reuse. Frozen libraries transfer across models and benchmarks that share a tool-calling convention, and degrade when the interface differs. A library written by a stronger model helps a weaker one, but not the reverse. The gate has a cost: GRASP makes more training-time LLM calls per batch than the simplest memory baselines, almost all of them for probe validation.

## Our read

HarnessRSI-Daily scores this paper 84/100 (★★★), with evidence level “retained”: the retained skill library improves held-out tasks. The paper reports held-out test and OOD splits, seed variance, training-time call cost, and released code with per-seed results and learned libraries. It reports a matched-compute control for the gate only in part. It does not report an explicit test for leakage between probe and test data, beyond keeping the splits separate. The largest gains are on MedAgentBench; elsewhere they are smaller or absent.
