# Skill-3D: keep scene-aware tool workflows, not just more tool calls

*A Reel interpretation of [arXiv 2606.07436v2](https://arxiv.org/abs/2606.07436v2), **Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning**, by Haoyuan Li, Zhengdong Hu, Jun Wang, Hehe Fan and Yi Yang. HarnessRSI Daily score **63**, band ★★. Code: [skill-3d/Skill-3D](https://github.com/skill-3d/Skill-3D).*

## What the system changes about itself

Skill-3D retains a **Scene Memory** of visual-question-answering trajectories and a **library of scene-aware skills**. A skill is a reusable procedure: when it applies, what evidence is needed, the order and arguments of tool calls, and how evidence supports an answer. Failures become lessons or fallback rules. This is procedural guidance, not a learned motor skill or a simulator policy.

Fixed static seed skills cover such routines as counting, metric distance, relative depth, view selection, detection–depth fusion, detection–segmentation fusion, orientation and reconstruction. Dynamic skills are distilled from experience. Tools include Pi3, GroundingDINO, SAM3, Depth Anything 3, Orient Anything v2 and SwinIR. The closed-source experiments change the surrounding skill harness; the Qwen experiments additionally update model weights through SFT and GRPO. Their gains therefore do not isolate library evolution alone.

## The loop, and the keep/reject rule

1. Identify the scene and task from the question and visual observations; retrieve candidate skills and let the policy select a compact subset.
2. Run the tool workflow and record reasoning, tool outputs, answer and outcome in Scene Memory.
3. Distill a successful trajectory into a new skill, or merge it into an existing one only if it adds useful coverage, stronger evidence or a lower-cost workflow. A redundant success only updates statistics.
4. Attach evidence-supported failures as lessons; patch a dynamic skill when the failure supports a reliable fallback. Recurring failures under a static skill can produce a new dynamic skill.
5. The Skill Manager accepts only updates that are evidence-supported and consistent with previous successful cases; otherwise it rejects them. Figure 2 depicts MLLM judgment. The paper does not give a numerical acceptance threshold, a detailed success-labeling procedure, or a separately rerun regression-test gate. It is not documented as simulator-success selection.

GPT-5.4 is the teacher for skill distillation and SFT-data generation, using training samples only. Training splits from all benchmarks are pooled into one shared memory/library, which is **frozen for evaluation and post-training**. At inference, semantic/context/evidence retrieval also considers success history, lessons and cost; the policy chooses which retrieved skills to use.

## Headline result, as reported

Table 1 evaluates GPT-4o, GPT-5.4, Gemini-2.5-Pro and Gemini-3-Flash on question-disjoint test data. Selected results show the comparison ladder rather than only the weakest baseline:

| Model and evaluated subtask | w/o Tools | w/ Tools | Think3D | Skill-3D |
|---|---:|---:|---:|---:|
| Gemini-3-Flash, MMSI-Bench positional relationship | 32.7 | 36.8 | 49.2 | 54.8 |
| GPT-5.4, VSI absolute distance | 43.6 | 47.8 | 55.0 | 61.5 |
| GPT-5.4, VSI room size | 55.7 | 58.2 | 69.9 | 77.6 |
| GPT-5.4, BLINK multi-view subset | 73.4 | 75.1 | 78.3 | 82.0 |

The abstract's **67%** Gemini-3-Flash MMSI gain is relative to **no tools**, not to Think3D. Table 2 also reports post-trained Qwen3-VL-4B/8B. For Qwen3-VL-8B, VSI room size is 41.6 without tools, 58.1 with Think3D-8B and 67.9 with Skill-3D-8B; MMSI positional relationship is 31.0, 41.2 and 42.8 respectively.

Tables 1 and 2 give point scores, without seed/run counts, standard deviations or confidence intervals. Do not read them as established single-run results or statistically resolved differences.

## The controls that decide whether the gain is real

- **Library ablations (Table 3, GPT-5.4).** The displayed VSI tasks are counting, absolute distance, object size and room size—not all VSI categories. The reported Avg. is 69.9 for full Skill-3D, 68.1 without failure lessons, 67.8 without dynamic skills, 65.6 without static skills, 65.5 without MLLM skill selection and 64.1 without retrieval. In Table 3's reported ablations, static priors and retrieval/selection have larger effects than dynamic skills alone. No per-row variance or run count is supplied. The full Avg. is consistent with averaging all eight Table 1 VSI categories rather than only the four displayed here, but Table 3 does not explicitly define that scope; see SOURCE.md. We retain the paper's Avg. rather than silently replacing it. **The no-dynamic VSI Avg. is 67.8 in Table 3 but 63.4 in Table B.2; their evaluation/configuration relationship is unexplained. We keep comparisons within each table, not as interchangeable estimates of dynamic skills' contribution.**
- **Actual cross-benchmark transfer (Table B.2).** This is not just the pooled headline: dynamic skills are built from one source benchmark while **the static skills and GPT-5.4 stay the same**. VSI-derived dynamic skills raise target MMSI-PR from 52.6 without dynamic skills to 57.8, and CV-3D Avg. from 92.2 to 93.7. MMSI-derived skills give VSI Avg. 67.3 versus 63.4 without dynamic skills. Some transfers are much smaller: BLINK-derived skills give VSI 63.9 versus 63.4; CV-3D-derived skills give BLINK 77.5 versus 77.2. The pooled library scores 60.4 on MMSI-PR. These averages have no variance/CI; static priors are shared, not reset to an empty library.
- **Freeze versus continued updating (Figure 5).** With Qwen3-VL-8B, frozen skills plus SFT cold start have the strongest, most stable reported GRPO training-reward curve. Online skill updating and skipping SFT fare worse. Shading is called “training variance,” without a seed count or a definition of the band; it does not establish multi-seed uncertainty for Tables 1–3.
- **Inference efficiency is not evolution cost (Table B.1, GPT-5.4, VSI).** Think3D averages 1.8 calls and 35.1 seconds per query; Skill-3D averages **2.6 calls and 20.8 seconds**, with 0.5 seconds retrieval overhead. Direct tool use is faster at 13.2 seconds. Skill-3D uses more calls, not fewer, but shifts away from expensive reconstruction. Effective tool usage rises from 39.2% for direct tools to 78.7%: the fraction of calls returning usable evidence that is substantively consumed downstream. These values occur in the table and prose, not only figure labels. Timing averages have no dispersion or stated repetition count.
- **Baseline access and budget.** “w/o Tools” has no tools; “w/ Tools” is direct tool use; Think3D is the reconstruction-based agent baseline. The paper does not report giving each of them Skill-3D's static/dynamic library, nor a matched teacher/distillation/interaction budget. It also does not establish identical post-training budgets for Think3D-4B/8B and Skill-3D-4B/8B. Thus the controls support the package, not an equal-budget comparison of skill-learning algorithms.

## Where the gain is small—and what remains unverified

The gains are not confined to one displayed subtask, but their size depends strongly on the comparator. Gemini-3-Flash jumps from 9.2 to 56.1 on VSI absolute distance and from 31.3 to 73.4 on appearance order against no tools; the corresponding Think3D scores are already 52.3 and 69.3. With Gemini-2.5-Pro on CV-3D, Skill-3D's 94.0 versus Think3D's 92.7 for depth order and 92.8 versus 91.6 for relative distance are much smaller margins. The post-trained Qwen3-VL-8B MMSI comparison is likewise 42.8 versus 41.2. Without uncertainty estimates, we cannot say whether these small gaps exceed noise. Skill-3D is not the fastest inference setting either.

**The split is by question, not demonstrated to be by scene.** The paper describes category-wise random sampling of 30% for training, with the rest disjoint for test. Table C.3 lists train/test sizes of 708/1654 for VSI, 157/345 for MMSI, 360/840 for CV-3D and 40/93 for BLINK. It reports neither scene/video-level separation nor an overlap audit, so shared visual scenes across skill construction and evaluation are not ruled out. This is indoor visual QA over supplied observations, not embodied navigation or simulator exploration; simulator-step cost is not an applicable reported budget.

**Settings versus tuning provenance.** Table C.4 does supply post-training numerical settings, including SFT/GRPO learning rates, batch sizes, group size, clipping and KL coefficient. But the numerical retrieval k, maximum tool budget B and acceptance threshold are not supplied. Which split selected defaults/hyperparameters is also not stated, nor are a separate validation split or baseline tuning budgets. That is different from saying no hyperparameters were reported.

The reported 500 SFT samples, 1k GRPO samples, one epoch, four NVIDIA RTX PRO 6000 Blackwell GPUs, roughly 3 SFT hours and 28 RL hours describe **post-training**, not the cost of constructing/evolving the skill library. Teacher tokens, dollars, construction rollouts and tool-call totals are unreported. The equations sum correctness/format/tool rewards without weights, whereas implementation prose gives correctness/tool/format weights of 0.6/0.2/0.2; the paper does not reconcile those descriptions. SOURCE.md also records unresolved aggregate/reporting differences without guessing their cause.

## Our read

HarnessRSI score **63**, band **★★**, evidence level **retained**. The retained library is frozen and evaluated on question-held-out data; dynamic/static/lesson/retrieval ablations are reported. The full appendix additionally reports source-to-target benchmark transfer, which the stored judgment's `cross_task: no` misses; we note that without changing the score or judgment files. The paper reports inference and post-training costs, but not library-evolution cost, matched construction budgets, scene-level leakage testing or uncertainty for the main scores. The useful result is scene-conditioned procedural guidance; the evidence does not establish an improved improver or embodied simulator generalization.
