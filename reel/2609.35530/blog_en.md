# AutoRef: optimize the harness, not the image model

**AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation**  
Yuta Oshima, Ku Onoda, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta. Oshima and Onoda contributed equally.  
[Paper](https://arxiv.org/abs/2609.35530v1) · [Code announced by the authors](https://github.com/KuOnoda/AutoRef)  
**Our score: 65 / 100 · ★★ · retained evidence.**

## What changes, and what gets kept?

AutoRef searches over executable Python harnesses around a frozen image generator and reasoning model. It can rewrite prompts, reference handling, generation schedules, diagnosis, selection and control flow—not model weights. The search uses Claude Fable 5.1 as proposer, GPT-5.5 as runtime reasoner, FLUX.2 [klein] 4B as generator, and Qwen3-VL-8B-Instruct as external evaluator. These are different roles, not one model grading itself.

The distinctive boundary is between **feedback for rewriting** and **feedback for survival**. A beam of two harnesses begins with vanilla generation and GEMS. Each of five iterations proposes four new harnesses. The proposer can inspect all training-side code, scores, rationales, images and traces, including rejected candidates. A separate validation set ranks the new candidates; only its two survivors replace the beam. Parents do not compete again. The proposer learns survivor identities and code, but not validation scores or artifacts. The final artifact is the highest-validation harness in the final beam. Thus validation performance is selection evidence, not an independent outcome.

The search uses 48 training and 48 validation tasks from the four-reference MultiBanana setting; 133 test tasks remain unseen during search. The paper specifies beam width, proposal count and iteration count, but does not report a separate sweep or which split selected those defaults. Fresh proposer sessions reconstruct history from files, and an isolated container excludes validation/test evaluation results. Instructions prohibit task-specific hardcoding. This is a meaningful procedural guard, not a reported reference-image/content-overlap audit.

## What the discovered harness does

The retained program generates three images. Reference-grounded prompts assign requested elements to reference images. Draft A emphasizes structured scene/subject descriptions; draft B anchors the canvas on a background/style reference, putting it first. Without that kind of reference, B resamples A's prompt. Selection prioritizes hard failures, then tests tied candidates in both presentation orders: a challenger must win both. Up to five reference-specific complaints about the winner guide draft C; without complaints, C resamples the winner's prompt. The same selection rule chooses the final output. GPT-5.5 performs this runtime selection; the external benchmark evaluator does not.

## Headline: a stronger system, not an equal-cost vanilla call

On the **133-task four-reference MultiBanana test**, FLUX.2 [klein] 4B rises from **5.72 to 7.37** (Table 1). This average first combines five criteria within task types, then gives equal weight to the four types. It is not a task-count-weighted pooled average. Vanilla uses one generated image; AutoRef uses three plus reasoning. The headline is therefore a system-level improvement, not a free upgrade to the generator.

All four task types improve: object **5.95→7.27**, local **6.11→7.87**, global **5.50→7.64**, background **5.34→6.70**. The gain is not confined to one category. Its average exceeds the reported one-image proprietary baselines, but not every category: local trails GPT-Image-1.5's **8.12**, and global trails Seedream 4.5's **7.83**. FLUX 9B with the harness also scores higher on object (**7.49**).

## Controls that matter

Table 6 supplies the crucial image-budget controls with the same generator and reasoning model:

| Harness | Test average | Mean generated images |
|---|---:|---:|
| Vanilla | 5.72 | 1 |
| Best-of-3 | 6.01 | 3 |
| IPR | 7.02 | 3 |
| Idea2Img, budget-matched | 6.42 | 3 |
| Idea2Img, original schedule | 7.12 | 9 |
| GEMS | 5.37 | 2.7 |
| AutoRef-Harness | 7.37 | 3 |

These are not reference-blind straw men. Best-of-3's selector sees the references and candidates. GEMS uses published prompts/default rounds, with references explicitly supplied to its verifier. IPR is reimplemented from equations/prompts because code was unavailable; its planner sees references and the current image. Idea2Img's original iterative schedule gets feedback, while the matched version uses three prompts in one round without feedback. Proprietary models use default API settings. Separate baseline tuning-search budgets are not reported; equal image counts do not equalize reasoning calls, tokens, dollars or total search cost.

The search comparison reports Meta-Harness **6.23**, greedy search **6.67**, and AutoRef **7.37**. Meta-Harness uses the same proposer/models/evaluator and is described as budget-matched, but ranks on the same tasks used for proposal feedback and exposes full history. Greedy retains split separation with one parent. This supports the search design, but does not independently isolate every design difference or establish measured total-compute parity. Meta-Harness uses five iterations here, versus its original longer protocol.

The retained-component ablations are substantial evidence (Tables 4/9). Removing diverse drafts gives **7.01**, complaint revision **6.99**, or failure-aware selection **6.93**, against **7.37**. Removed generation steps are replaced with resampling, preserving three images. Grounding alone reaches **6.91** with one image; selection alone reaches **6.15**. Much of the headline lift already appears with grounding. This is not a clean grounding leave-one-out while all other components remain. Complaint revision barely changes object scores (**7.24** versus **7.27**), despite a larger local effect (**7.01** versus **7.87**).

## Transfer, failures and uncertainty

The same harness transfers without reoptimization to FLUX 9B (**5.78→7.10**) and Qwen-Image-Edit-2511 (**4.44→5.69**) on four references. On unseen three-/five-reference settings, each with 96 tasks, 4B improves **6.94→7.76** and **5.19→6.36**. But Qwen with five references declines **1.89→1.87**. Appendix I reports all three Qwen drafts hard-fail on **87/96** tasks (**91%**). This is a clear failure boundary, not universal portability.

OmniContext is unseen during search and uses GPT-4.1 evaluation: 120 tasks across eight types, with geometric means of prompt-following and subject-consistency scores. The 4B average improves **8.30→8.85**, but single-character falls **9.22→8.94** and multiple-character-plus-object falls **8.68→8.59**. Scene-object improves **7.47→8.89**, whereas scene-character changes only **9.18→9.28**. The aggregate remains below GPT-Image-1.5's **9.41**. Benefits are uneven, not a universal ranking reversal.

Four human raters assessed 50 held-out tasks per baseline comparison with randomized output order. Against Nano Banana Pro, AutoRef wins **46%** and loses **40%**—a much narrower comparison than versus vanilla 4B (**70%** versus **17%**). No confidence intervals, per-cell seed/run counts or repeated-search variance are reported. Do not interpret small differences as statistically established, or label results “single-run” without evidence. Qualitative examples were selected among the largest score gaps, not sampled at random.

## Our read

**65 / 100, ★★, retained.** There is a genuinely retained executable artifact, held-out testing, image-count-matched runtime controls, transfer, human evaluation and component ablations. The result is stronger than merely resampling three times; it is not evidence that the optimization procedure itself recursively improves.

The missing pieces are repeated-search/seed uncertainty and end-to-end optimization economics. Twenty proposed harnesses and the GPU model are disclosed, but total optimization wall time, GPU-hours, tokens, dollars and total image generation are not. Transfer also inherits the original search expenditure. Split separation constrains feedback leakage; it does not establish reference/content independence. Our stored judgment understates retained ablation evidence: the full PDF does report it. Its budget-matching and leakage labels need the narrower qualifications above, without changing the published score.
