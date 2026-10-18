# Harness RSI patterns — overview

13 main patterns and 36 sub-patterns, induced from 585 harness-level self-improvement papers (outcome labels withheld during induction). Paper counts below are the arXiv corpus; accept rates are within ICLR 2025–2026 submissions (base rate 34%). Read the cards for confidence intervals; most differences are not significant. See also [anti-patterns](anti-patterns.md).

Like ResearchStudio's ideation patterns, these are diagnostic vocabulary for research moves, not labels for domains.

| main pattern | operational signature | papers | ICLR accept rate |
|---|---|---|---|
| [Abstract Experience into Reusable Guidance](main/abstract_experience_into_guidance.md) | act and observe outcome → reflect or contrast to abstract guidance → write/curate the guidance store → retrieve and inject into later tasks | 82 | 20% (-14.4 pp, n=20) |
| [Attribute Failures and Patch the Incumbent](main/attribute_and_patch_incumbent.md) | execute and collect traces → diagnose and attribute failures to a component → propose a localized edit → re-validate → replace the incumbent | 82 | 22% (-12.4 pp, n=41) |
| [Index Raw Experience for Reuse](main/index_experience_for_reuse.md) | record episodes/cases → structure the store (index, hierarchy, graph, tiers) → retrieve relevant precedent when needed → adapt it and append the new outcome | 70 | 30% (-4.0 pp, n=23) |
| [Search a Population Against an Executable Fitness](main/population_search_executable_fitness.md) | sample parents from the population → LLM mutates/recombines → evaluate with executable fitness → select (elite, Pareto, QD) and archive | 61 | 38% (+3.6 pp, n=50) |
| [Self-Generate the Curriculum](main/self_generate_the_curriculum.md) *(boundary: touches weights)* | estimate the learner's frontier or weaknesses → generate tasks/environments → verify solvability and difficulty → train the learner → regenerate | 46 | 58% (+23.3 pp, n=26) |
| [Diagnose Whether Self-Improvement Is Real](main/diagnose_self_improvement.md) | identify a confound in end-to-end evolution scores → design matched/frozen/held-out conditions or an attack → measure the isolated effect → report the failure mode | 46 | n<10 |
| [Gate Retention on Measured Evidence](main/evidence_gated_retention.md) | propose a candidate entry or change → measure its marginal effect (paired, held-out, utility credit) → admit, demote, or roll back → keep provenance | 41 | n<10 |
| [Crystallize Solutions into Executable Capabilities](main/crystallize_executable_capability.md) | solve or practice a task → abstract the solution into parameterized code → execute/test to verify → register in the action space → compose on later tasks | 36 | 27% (-7.7 pp, n=15) |
| [Make the Improver Editable](main/make_the_improver_editable.md) | improver proposes a change → apply it to the task agent and/or the improver → evaluate descendants → retain (incumbent or archive) → recurse | 29 | n<10 |
| [Amortize the Improver into a Trained Policy](main/amortize_improver_into_trained_policy.md) *(boundary: touches weights)* | improver acts (write memory, edit artifact, design workflow) → measure downstream task outcome → credit the improver's action → update improver weights | 28 | 40% (+5.6 pp, n=20) |
| [Search the Agent's Architecture](main/search_agent_architecture.md) | define a design space of modules/topologies/workflow code → propose designs → execute and score → retain or adapt the structure | 26 | 44% (+9.4 pp, n=16) |
| [Couple Context-Level and Weight-Level Learning](main/couple_context_and_weight_updates.md) *(boundary: touches weights)* | adapt in context → collect experience-shaped rollouts → train weights on them → re-adapt context for the updated model | 20 | 36% (+2.0 pp, n=11) |
| [Co-Evolve the Evaluator](main/coevolve_the_evaluator.md) | observe policy outputs → expose evaluator blind spots → revise criteria/tests → validate against a trusted anchor → use as reward or acceptance gate | 18 | n<10 |

## Sub-patterns

| id | sub-pattern | parent | papers | ICLR accept rate |
|---|---|---|---|---|
| [H00](sub/H00.md) | Reflect on Outcomes into Transferable Lessons | Abstract Experience into Reusable Guidance | 45 | 19% (-15.6 pp, n=16) |
| [H01](sub/H01.md) | Curate a Living Memory with Edit Operations | Abstract Experience into Reusable Guidance | 22 | n<10 |
| [H02](sub/H02.md) | Mine Interaction Streams into Skill Packages | Abstract Experience into Reusable Guidance | 15 | n<10 |
| [H03](sub/H03.md) | Retrieve and Adapt Precedent Cases | Index Raw Experience for Reuse | 36 | 25% (-9.4 pp, n=12) |
| [H04](sub/H04.md) | Restructure the Memory Substrate | Index Raw Experience for Reuse | 25 | 30% (-4.4 pp, n=10) |
| [H05](sub/H05.md) | Retrieve Only When Needed | Index Raw Experience for Reuse | 9 | n<10 |
| [H06](sub/H06.md) | Discover Skills Through Self-Directed Practice | Crystallize Solutions into Executable Capabilities | 12 | n<10 |
| [H07](sub/H07.md) | Forge Tools When a Capability Gap Appears | Crystallize Solutions into Executable Capabilities | 15 | n<10 |
| [H08](sub/H08.md) | Maintain a Compositional Skill Graph | Crystallize Solutions into Executable Capabilities | 9 | n<10 |
| [H09](sub/H09.md) | Propagate Feedback Through a Compound System | Attribute Failures and Patch the Incumbent | 8 | n<10 |
| [H10](sub/H10.md) | Rewrite a Document from Diagnosed Errors | Attribute Failures and Patch the Incumbent | 28 | 17% (-17.7 pp, n=30) |
| [H11](sub/H11.md) | Revise Skills by Failure Attribution | Attribute Failures and Patch the Incumbent | 14 | n<10 |
| [H12](sub/H12.md) | Patch the Harness from Trace Diagnosis | Attribute Failures and Patch the Incumbent | 32 | n<10 |
| [H13](sub/H13.md) | Search a Population of Prompts | Search a Population Against an Executable Fitness | 18 | 32% (-2.3 pp, n=28) |
| [H14](sub/H14.md) | Evolve Programs with LLM Mutation | Search a Population Against an Executable Fitness | 18 | 39% (+4.5 pp, n=18) |
| [H15](sub/H15.md) | Guide Evolution with Distilled Search Memory | Search a Population Against an Executable Fitness | 14 | n<10 |
| [H16](sub/H16.md) | Preserve a Frontier of Complementary Candidates | Search a Population Against an Executable Fitness | 11 | n<10 |
| [H17](sub/H17.md) | Search an Offline Agent Design Space | Search the Agent's Architecture | 14 | 43% (+8.5 pp, n=14) |
| [H18](sub/H18.md) | Co-Evolve Roles and Topology at Test Time | Search the Agent's Architecture | 12 | n<10 |
| [H19](sub/H19.md) | Apply the Improver to Itself | Make the Improver Editable | 13 | n<10 |
| [H20](sub/H20.md) | Branch Self-Modifying Agents from an Archive | Make the Improver Editable | 8 | n<10 |
| [H21](sub/H21.md) | Redesign the Inner Learning Mechanism | Make the Improver Editable | 8 | n<10 |
| [H22](sub/H22.md) | Co-Train a Proposer Against a Solver | Self-Generate the Curriculum | 25 | 60% (+25.6 pp, n=10) |
| [H23](sub/H23.md) | Synthesize Tasks from Diagnosed Weaknesses | Self-Generate the Curriculum | 21 | 56% (+21.9 pp, n=16) |
| [H24](sub/H24.md) | Evolve Rubrics as Training Rewards | Co-Evolve the Evaluator | 8 | n<10 |
| [H25](sub/H25.md) | Revise the Evaluator Against a Trusted Anchor | Co-Evolve the Evaluator | 10 | n<10 |
| [H26](sub/H26.md) | Train the Curator on Downstream Utility | Amortize the Improver into a Trained Policy | 17 | n<10 |
| [H27](sub/H27.md) | Train the Proposer to Amortize Search | Amortize the Improver into a Trained Policy | 11 | 42% (+7.7 pp, n=19) |
| [H28](sub/H28.md) | Couple In-Context Adaptation with Weight Training | Couple Context-Level and Weight-Level Learning | 20 | 36% (+2.0 pp, n=11) |
| [H29](sub/H29.md) | Value Memory Entries by Measured Utility | Gate Retention on Measured Evidence | 14 | n<10 |
| [H30](sub/H30.md) | Govern Library Admission and Retirement | Gate Retention on Measured Evidence | 12 | n<10 |
| [H31](sub/H31.md) | Use a Statistically Sound Commit Rule | Gate Retention on Measured Evidence | 15 | n<10 |
| [H32](sub/H32.md) | Isolate Effects with Controlled Interventions | Diagnose Whether Self-Improvement Is Real | 12 | n<10 |
| [H33](sub/H33.md) | Benchmark Persistent Improvement over Streams | Diagnose Whether Self-Improvement Is Real | 15 | n<10 |
| [H34](sub/H34.md) | Benchmark Agents Doing AI R&D | Diagnose Whether Self-Improvement Is Real | 9 | n<10 |
| [H35](sub/H35.md) | Audit Persistence as an Attack Surface | Diagnose Whether Self-Improvement Is Real | 10 | n<10 |
