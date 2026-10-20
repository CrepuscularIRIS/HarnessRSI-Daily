# GrIPS: random phrase edits to a task instruction, kept when a small score set says so — and what the controls show

*A Reel interpretation of [arXiv 2203.07281v2](https://arxiv.org/abs/2203.07281v2) (Archiki Prasad, Peter Hase, Xiang Zhou, Mohit Bansal; UNC Chapel Hill). HarnessRSI Daily score 67, ★★. Code: [archiki/GrIPS](https://github.com/archiki/GrIPS).*

## What the system changes about itself

GrIPS edits the **natural-language instruction** inside a prompt. The model weights are not touched, so it also works on API-only models. The instruction is split into phrases with a constituency parser, and four phrase-level edit operations are applied at random: **delete**, **swap** two phrases, **paraphrase** a phrase (a PEGASUS paraphrase model), and **add** back a phrase deleted earlier. The prompt template words are kept fixed; only the instruction text is searched. The kept artifact is the searched instruction.

## The loop, and the keep/reject rule

1. Start from the task's original instruction (the "base").
2. Each iteration, build m = 5 candidates, each with l = 1 random edit.
3. Score every candidate on a **score set** of 100 labelled examples that is "not a part of the test set". Score = balanced accuracy plus 10 × the entropy of the predicted labels (the entropy term favours candidates whose predictions are not all one label).
4. If the best candidate scores higher than the base, it becomes the new base; otherwise the base is kept.
5. Stop when the patience (P = 2) runs out or after 10 iterations (the text says no improvement for P iterations; the Algorithm 1 pseudocode in Appendix C returns after P + 1 non-improving iterations). The final instruction is evaluated on the test set. A beam-search variant keeps the top B candidates (B = 5), at about B times more model evaluations.

## Headline result, as reported

Table 1: eight binary classification tasks from NATURAL-INSTRUCTIONS, Instruction-Only prompts, 300 random test examples per task (sampled as balanced as possible, Appendix A), 3 search seeds, 95% confidence intervals in parentheses.

| Model | No search | GrIPS |
|---|---|---|
| GPT-2 XL | 49.54 (1.9) | 58.90 (2.0) |
| InstructGPT babbage | 55.80 (2.5) | 60.09 (3.7) |
| InstructGPT curie | 63.71 (1.9) | 66.07 (1.6) |

The paper reports gains of 9.36, 4.29 and 2.36 points, significant at p < 0.05 (bootstrap over examples and seeds). A majority-label baseline in the same table is 59.83. (The abstract says "up to 4.30 percentage points" for InstructGPT; the text and Table 1 give 4.29.)

## The controls that decide whether the gain is real

All numbers below are on 100-example test subsets per task, so they differ from Table 1, and Tables 2–6 report no confidence intervals.

- **Edit-operation ablation (Table 2, GPT-2 XL).** GrIPS 53.68 against 48.38 with no search. Removing the entropy term gives 52.20, removing delete 51.12, swap 52.67, paraphrase 52.54, add 52.42. Each drop is 1.01 to 2.56 points on a single reported number; Table 1's confidence intervals for the same model family are 1.6 to 3.7 points wide, so the individual ablation gaps are of that size and the paper gives no variance for them. The paper also tried a T5 paraphraser (53.33) and simulated annealing (57.46 against 57.79 for greedy on babbage, "no statistically significant difference").
- **Manual rewriting (Tables 3 and 10).** Two variants: plain rewriting 47.70 / 55.50 / 57.87 (GPT-2 XL / babbage / curie), and rewriting plus an added label-space line ("+ Labels", Table 10) 48.12 / 55.37 / 55.37, against GrIPS 53.68 / 57.79 / 59.37. The paper's stated margins (5.56, 2.29, 1.50) are against the better variant for each model. The rewriting was done by the first three authors (about 5 hours) following published guidelines; the paper describes no use of a score set for it. On GPT-2 XL plain rewriting is below no search (47.70 against 48.38) and improves 1 of 8 tasks (Table 10); on babbage (55.50 against 55.37) and curie (57.87 against 57.25) it is close to no search.
- **Example search at the same query budget (Table 3).** A random-sampling search over in-context examples, using the same score set and the same maximum number of model queries: 56.00 / 56.25 / 57.75. GrIPS is **lower** on GPT-2 XL (53.68 against 56.00) and higher on babbage (57.79) and curie (59.37), by 1.54 and 1.62. These are single averages with no variance, example search uses Examples-Only prompts while GrIPS uses Instruction-Only prompts, and the paper says task-level results vary a lot, "more so in the case of InstructGPT curie" (Appendix E.2). The paper notes that example search costs more per query in dollars, and that other example-search heuristics were not run.
- **Gradient-based tuning (Table 4, GPT-2 XL, one number each).** Direct finetuning 55.88, adapters 55.08, prefix-tuning 53.29 (51.12 without MLP reparametrization), GrIPS 53.68, GrIPS with beam search (B = 5) 56.50. Greedy GrIPS is below finetuning (by 2.2) and adapters (by 1.4); beam search is above all of them, using about B times more evaluations. The gradient methods got an 80:20 train/dev split of the score set and "only use test input and not instructions" (footnote 11); their tuning settings and compute are not reported. The "up to 2.56 and 5.38" margin over prefix-tuning compares with the weaker no-MLP variant; against the 53.29 variant the gaps are 0.39‡ (greedy) and 3.21‡ (beam). Only GPT-2 XL was used for this comparison; the gradient methods cannot run on the API models.
- **Seeds and variance.** Search was run with 3 seeds (5 for Instruction + Examples). Confidence intervals appear only in Table 1 and Figure 4; Tables 2–6 give single averages.
- **Other settings.** Starting from a task-agnostic instruction (Table 5): 51.87 to 54.29 (GPT-2 XL), 52.37 to 54.41, 53.75 to 55.96. Instruction + Examples prompts (Table 3): 52.40 to 54.40, 55.70 to 57.88, 57.65 to 59.44. Open models (Table 6): OPT, BLOOM, GPT-J and GPT-NeoX go from 46.38–49.75 to 52.75–55.1; FLAN-T5 goes from 71.25 to 74.33, and the authors note FLAN-T5 was instruction-tuned on NATURAL-INSTRUCTIONS, "possibly exposing the model to the test instances".
- **Score-set size (Figure 3, babbage).** 20 examples: 56.37‡; 50: 56.92‡; 100: 57.79; no search 55.37. The text says "4.27 point gain when |S| = 100"; the figure and Table 3 give 57.79 against 55.37, i.e. 2.42‡. We could not reproduce 4.27 from any table or figure and leave this unresolved.
- **Cost (p. 5).** One search run over the 8 tasks costs $20–25 (babbage) or $125–175 (curie) per seed; all experiments about $2400; evaluating the found instructions on the test sets about $150 in total. GPT-2 XL runs took a little over 5 GPU-hours in total.

## Where the gain is absent or small

- **GPT-2 XL after search is not above the majority label.** 58.90 against 59.83; babbage reaches 60.09 with a confidence interval of 3.7; only curie (66.07) is clearly above. In Figure 4, the majority-label bars for tasks 021 and 022 (about 79% and 90% of the test sets, read off the figure; the source datasets are more than 90% skewed, Table 8, but test sets were sampled as balanced as possible, Appendix A) appear above the after-search bars of all three models, closely so for curie on 021 and the InstructGPT models on 022.
- **The average gain is concentrated in a few tasks (read off Figure 4, approximate).** Most of GPT-2 XL's +9.36 comes from tasks 022, 195 and 021; about half of babbage's +4.29 comes from task 021; curie is slightly lower after search on tasks 021 and 022. On GPT-2 XL, tasks 021 and 022 start far below the majority-label bars.
- **Many tasks do not improve.** Table 10 counts tasks (of 8) with a positive change: GrIPS Instruction-Only GPT-2 XL 4, babbage 7, curie 5. For tasks 069, 137 and 139, search with GPT-2 XL stopped and returned the original instruction (Appendix G).
- **Example search wins on GPT-2 XL** (56.00 against 53.68), and finetuning (55.88) and adapters (55.08) beat greedy GrIPS.
- **Smaller gains with less data.** The babbage gain shrinks as the score set shrinks (Figure 3); the paper reports a 1.0-point gain with 20 examples.
- **Searched instructions are often incoherent.** The authors show instructions where definitions are deleted or reversed in meaning ("indicating no") and accuracy still improves; 68.5% of searched instructions are shorter than the original. They say how the models use instructions "remains largely unknown".
- **Scope limits stated by the authors.** Classification tasks only (8 tasks, chosen for cost and for diversity, balance and stability of the dataset versions, Appendix A; four of them have source-dataset label skew above 90%, Table 8), no davinci model, edits cannot add new information, and better instruction-followers "may need less optimization of their prompts".
- **Hyperparameters.** m, n, l and patience were chosen by line search using GPT-2 L and XL "on select tasks during preliminary experiments"; the tasks are not named and the paper does not say which examples. GPT-2 XL is also a reported model.

## Our read

HarnessRSI score **67**, band ★★, evidence level **retained**: the searched instruction (the kept artifact) is evaluated on test examples that were not used to select it. The paper reports a held-out test set, 95% confidence intervals in Table 1 (their computation is not described; the significance tests bootstrap over examples and seeds), a same-query-budget example-search baseline, a manual-rewriting baseline, a gradient-based comparison on one model, optimizer cost in dollars, and an ablation of edit operations and the score function. It does not report a leakage check between the score set, the searched instruction and the test set, transfer of a searched instruction to other tasks or models, confidence intervals outside Table 1 and Figure 4, or runs of other discrete prompt-search methods (AutoPrompt is argued about, not run). The gains in Table 1 are largest for the weakest model and smallest for curie, and on GPT-2 XL half of the tasks do not improve.

*Numbers marked ‡ were computed by us from paper numbers; see SOURCE.md.*
