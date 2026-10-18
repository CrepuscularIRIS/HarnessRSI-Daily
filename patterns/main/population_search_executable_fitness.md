# Search a Population Against an Executable Fitness
_id: `population_search_executable_fitness` · sub-patterns: H13, H14, H15, H16 · corpus support: 103 papers (accepted 35 · rejected 31 · unlabeled 37)_

**Definition.** Treat the artifact — a prompt, program, heuristic or configuration — as a genome, and use an LLM as the
variation operator inside a generate–evaluate–select loop driven by an automated fitness function. The persistent
improvement is the retained population or archive, not any single model call. Variants differ in what is mutated,
how search history is exploited, and which candidates survive selection.

**Operational signature.** sample parents from the population → LLM mutates / recombines → score with an executable
fitness on a selection split → select (elite, frontier, quality-diversity) and archive → report on a disjoint split

**When to apply.** A cheap, trustworthy automated evaluator exists, the space is too irregular for gradients, and the
evaluation budget allows many calls. If failures yield readable traces, critique-directed rewriting is the closer move.

## Sub-patterns
| id | name | papers | one-line tactic |
|---|---|---|---|
| [H13](../sub/H13.md) | Search a Population of Prompts | 44 | Undirected LLM variation over instructions or demonstrations, scored on a small set; the lever is what fitness rewards. |
| [H14](../sub/H14.md) | Evolve Programs with LLM Mutation | 31 | LLM edits small executable units inside a validity-preserving scaffold; an evaluator runs each child. |
| [H15](../sub/H15.md) | Guide Evolution with Distilled Search Memory | 15 | Distil history into credited rules, snippets or principles that condition later proposals. |
| [H16](../sub/H16.md) | Preserve a Frontier of Complementary Candidates | 13 | Retain a per-instance, multi-objective or quality-diversity frontier instead of one incumbent. |

H13/H14 are defined by the genome, H15 by a knowledge layer over the search, H16 by the retention rule; H15 and H16
compose with either genome.

## Success conditions (from accepted work)
- **The contribution lives at the search level, not the domain.** Accepted members change what fitness measures
  (worst case over a shift, robustness over paraphrases, end-to-end credit across pipeline modules) or how evaluations
  are spent (novelty rejection, adaptive parent sampling, bandit allocation); a new metaheuristic alone rarely suffices.
- **The evaluator is built before the loop and is hard to game.** Execution scores, end-to-end metrics or verified
  correctness make selection pressure meaningful; proxies are checked for rank transfer to the real setting.
- **The evolved unit is small and sits in a scaffold.** Operators, priority functions or skeletons with numerically
  fitted constants keep children valid and the search tractable.
- **Mutations are grounded in what the evaluator observed.** Training curves, legality violations or failure
  analyses fed back to the proposer give variation a direction that selection alone does not.
- **Memory and archives earn their place by measured effect.** Accepted memory designs credit items by child-versus-
  parent fitness change and keep negative evidence; frontier designs name the axis of complementarity they preserve.
- **The genome is enlarged only when text-level search plateaus.** Moving from wording to whole configurations,
  non-text prompt parts or code is motivated by a named ceiling of the smaller genome.

## Failure modes (from rejected work)
- **A generic loop pointed at a new domain.** Most rejected members in H13 and H14 apply standard evolution to attacks,
  routing, solvers, kernels or feature engineering with no search-level novelty; they read as application notes.
- **Re-skinned metaheuristics or ensembles.** A new swarm or hierarchy metaphor, or a vote over existing optimizers,
  without a new objective or genome is the commonest high-fit rejected shape in H13.
- **Search buried inside a larger pipeline.** 14 of the 31 rejected members are low-fit, where population search is
  one component and its contribution cannot be isolated.
- **Proxy fitness in ill-specified or adversarial targets.** Several rejected designs select on a proxy (synthetic-
  sample precision, classifier-guided attributes) where nothing ties the proxy to the stated goal.
- **Orchestration in place of search.** Splitting a standard loop into cooperating agent roles, or changing a
  retrieval key, alters the plumbing but not the generate–evaluate–select dynamics.
- **Diversity as the deliverable.** Selecting a complementary set as the end product, with no executable fitness loop
  around it, falls outside what this move buys.

## Accepted vs rejected gap
Across sub-patterns the dividing line is not which genome or metaheuristic is used but whether the paper changes
something about the search itself — the fitness definition, the evaluation-allocation rule, how memory earns credit,
or what survives selection. Accepted mechanisms target the loop: robust or end-to-end fitness, sample-efficient
allocation, evaluator-grounded mutation, credited memory, frontier retention. Rejected mechanisms mostly target a
domain: the loop is unchanged and the novelty is the application, a metaheuristic metaphor, an optimizer ensemble, an
agent-role split, or a proxy objective. Caveat: rejected signatures were extracted from abstracts only and audited
evidence exists only for corpus papers, so this gap is drawn from mechanism and design fields alone; it says nothing
about whether rejected papers reported less rigor or fewer limitations.

## Outcome contrast
| view | n | accepted | rejected | accept rate | Δ vs base | 95% CI |
|---|---|---|---|---|---|---|
| iclr_2025_2026 | 50 | 19 | 31 | 0.38 | +3.6 pp | [0.259, 0.518] |
| iclr_2025_2026_high_fit | 30 | 13 | 17 | 0.433 | +4.1 pp | [0.274, 0.608] |
| all_labeled | 66 | 35 | 31 | 0.53 | -4.6 pp | [0.412, 0.646] |

Base rates 0.344, 0.393 and 0.576. Acceptance is not quality, and every CI contains its base rate: adopting this move
neither helps nor hurts acceptance detectably. The sign flips between views (slightly above base at ICLR, below in the
pooled set), which is what noise at this n looks like. Sub-level rows are no stronger — H13 at -13.5 pp and H14 at
-12.6 pp in the pooled view both have CIs spanning base, and with ~50 sub-pattern tests per view any single
"significant" sub-row could be chance. H15 and H16 have too few labeled rejections for any rate.

## Reviewer expectations (pending — derived from the evidence audit, not from reviews)
Counts below cover only the 24 corpus members with a quote-grounded evidence block; they describe corpus practice,
not an accepted-vs-rejected difference.
- **A disjoint report split.** Selection must never touch reported examples; held-out is yes for 11 of 24, no for 7.
- **Variance across seeds for every arm,** baselines and ablations included; yes for only 5 of 24.
- **Budget-matched comparison in tokens or wall-clock,** not just iterations; full match for 7 of 24.
- **A simpler-search baseline** (greedy, random, best initial proposal) and a no-search control; 4 of 24.
- **An ablation of the retained structure** (memory, frontier, archive); 5 of 24. Optimizer cost: 13 of 24.
- **A leakage guard on the evaluator** against memorised solutions or gamed proxies; tested in 1 of 24.

## Cognitive barriers
- That the LLM is the solver; here it is a mutation operator, and the algorithm around it does the optimizing.
- That a better proposer is the contribution; the fitness function and the allocation rule usually matter more.
- That one winner is the output; complementary losers, and distilled lessons from discarded candidates, are assets.
- That an evaluator score is a result; it is selection pressure until confirmed on data the search never saw.

## Lessons
### From accepted work
- Redefining what fitness rewards beats inventing a new variation operator.
- Sample efficiency — rejecting redundant children, exploration-aware parent choice, bandit allocation — is a
  contribution on its own.
- Evolve small units inside a scaffold and fit constants numerically; the output stays inspectable code.
- Ground mutations in what the evaluator observed rather than in the model's prior alone.
- Credit memory items by measured fitness change and keep negative evidence; only then is memory auditable.
- Per-instance or multi-objective frontiers escape greedy local optima when inputs are heterogeneous.
### From rejected work
- An unchanged evolution loop in a new domain reads as an application, not a method.
- A metaheuristic metaphor or optimizer ensemble without a new objective reads as a re-skin.
- When search is one stage of a larger system, isolate its effect or the claim is unattributed.
- Splitting the loop into agent roles is orchestration; show what changes in the search dynamics.
- A proxy fitness needs an argument, or a check, that it tracks the real objective.
- Correctness-critical domains need correctness gates inside fitness, not just a framework description.
