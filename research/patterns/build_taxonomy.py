"""Assemble and validate the Harness-RSI pattern taxonomy."""
import collections
import json

OUT = "/home/lingxufeng/ArxivDaily/research/patterns/"
rows = [json.loads(l) for l in open(OUT + "induction_input.jsonl")]
ids = [r["arxiv"] for r in rows]

# --- revision pass 1 overrides (arxiv -> code|sec|fit) ---
OVERRIDES = {
    "2602.02979": "CUR1||h", "2608.08311": "REF1|GAT|h", "2609.04094": "EVA1||h",
    "2510.14253": "EVA1|CUR|l", "2607.05297": "REF2||h",
    "2604.17091": "IDX3|ABS|l", "2508.09736": "IDX3|LIM|l",
}
assign = {}
for line in open("/tmp/assign_v1.txt"):
    if line.strip():
        a, code, sec, fit = line.strip().split("|")
        assign[a] = (code, sec, fit)
for a, v in OVERRIDES.items():
    assign[a] = tuple(v.split("|"))
assign = {a: (c.replace("INT1a", "INT").replace("INT1b", "INT"), s, f) for a, (c, s, f) in assign.items()}

MAIN = {
 "ABS": dict(id="abstract_experience_into_guidance", name="Abstract Experience into Reusable Guidance",
  definition="Convert the agent's own task outcomes into compact natural-language guidance (lessons, principles, curated notes, skill documents) that persists outside the weights and conditions later episodes. The improvement lives in an editable textual state, and the load-bearing choice is the abstraction level: specific enough to act on, general enough to transfer.",
  operational_signature="act and observe outcome → reflect or contrast to abstract guidance → write/curate the guidance store → retrieve and inject into later tasks",
  when_to_apply="When the model is frozen or costly to train but tasks recur enough that distilled lessons transfer.",
  cognitive_barrier="That learning requires parameter updates — editable text in context can itself be the learned state."),
 "IDX": dict(id="index_experience_for_reuse", name="Index Raw Experience for Reuse",
  definition="Keep experience close to its raw form (trajectories, workflows, cases, facts) and invest in how it is organized and when it is retrieved, so the right precedent is found and adapted as the store grows. Gains come from recall and adaptation of precedent rather than from abstraction.",
  operational_signature="record episodes/cases → structure the store (index, hierarchy, graph, tiers) → retrieve relevant precedent when needed → adapt it and append the new outcome",
  when_to_apply="When tasks recur with concrete details that abstraction would lose and retrieval quality, not storage, limits gains.",
  cognitive_barrier="That storing more history or widening context automatically helps — retrieval organization and timing are the bottleneck."),
 "CRY": dict(id="crystallize_executable_capability", name="Crystallize Solutions into Executable Capabilities",
  definition="Turn successful solutions into verified executable artifacts (functions, tools, servers, programmatic skills) that enter the agent's action space, so future tasks invoke rather than re-derive them. Execution-based verification gates admission and composition lets the capability set grow cumulatively.",
  operational_signature="solve or practice a task → abstract the solution into parameterized code → execute/test to verify → register in the action space → compose on later tasks",
  when_to_apply="When recurring subproblems are procedural and an execution environment can verify candidate code.",
  cognitive_barrier="That the agent's action space is fixed by the designer rather than grown by the agent."),
 "PAT": dict(id="attribute_and_patch_incumbent", name="Attribute Failures and Patch the Incumbent",
  definition="Maintain one deployed artifact (prompt, rule document, skill file, harness code) and improve it by tracing failures to the responsible component and applying localized edits, re-validated before they replace the incumbent. The load-bearing step is credit assignment from rich traces rather than from a scalar score.",
  operational_signature="execute and collect traces → diagnose and attribute failures to a component → propose a localized edit → re-validate → replace the incumbent",
  when_to_apply="When execution traces are rich and the artifact decomposes so that failures can be localized.",
  cognitive_barrier="That a black-box score is the only usable optimization signal for non-differentiable artifacts."),
 "POP": dict(id="population_search_executable_fitness", name="Search a Population Against an Executable Fitness",
  definition="Treat the artifact (prompt, program, heuristic, configuration) as a genome and use an LLM as the variation operator inside a generate–evaluate–select loop driven by an automated fitness function. The retained population or archive is the persistent improvement; variants differ in how they exploit search history and preserve diversity.",
  operational_signature="sample parents from the population → LLM mutates/recombines → evaluate with executable fitness → select (elite, Pareto, QD) and archive",
  when_to_apply="When a cheap, trustworthy automated evaluator exists and the search space is too irregular for gradients.",
  cognitive_barrier="That the LLM is the solver rather than a mutation operator inside a search algorithm."),
 "ARC": dict(id="search_agent_architecture", name="Search the Agent's Architecture",
  definition="Lift the agent's structure — roles, communication topology, workflow code, module composition — into the optimization space and improve it from execution feedback, either offline over a design space or online for a specific team and task.",
  operational_signature="define a design space of modules/topologies/workflow code → propose designs → execute and score → retain or adapt the structure",
  when_to_apply="When hand-designed orchestration, not individual prompts, caps performance.",
  cognitive_barrier="That orchestration is fixed scaffolding around tunable prompts."),
 "REF": dict(id="make_the_improver_editable", name="Make the Improver Editable",
  definition="Place the improvement procedure itself (optimizer prompt, meta-agent code, mutation operators, memory or context design) inside the space being modified, so task gains can compound into better future improvement. Progress is justified empirically by evaluating descendants rather than by proofs.",
  operational_signature="improver proposes a change → apply it to the task agent and/or the improver → evaluate descendants → retain (incumbent or archive) → recurse",
  when_to_apply="When the design of the improvement loop itself is the bottleneck and its products are evaluable.",
  cognitive_barrier="That the meta-level optimizer must stay fixed and human-designed."),
 "CUR": dict(id="self_generate_the_curriculum", name="Self-Generate the Curriculum",
  definition="Let the system produce its own training tasks or environments, targeted at its current competence frontier or diagnosed weaknesses, and train on them so the data distribution evolves with the learner. Validity and difficulty are controlled by verification, solver success rates, or failure analysis.",
  operational_signature="estimate the learner's frontier or weaknesses → generate tasks/environments → verify solvability and difficulty → train the learner → regenerate",
  when_to_apply="When curated data saturates or is unavailable but solutions can be verified.",
  cognitive_barrier="That the training distribution is a fixed external input."),
 "EVA": dict(id="coevolve_the_evaluator", name="Co-Evolve the Evaluator",
  definition="Treat the grader (rubric, verifier, reward criteria, test suite) as an artifact that evolves alongside the policy, anchored to a small trusted signal so that it tracks new failure modes without drifting into a hackable target.",
  operational_signature="observe policy outputs → expose evaluator blind spots → revise criteria/tests → validate against a trusted anchor → use as reward or acceptance gate",
  when_to_apply="When fixed rewards are stale, hackable, or absent, as with open-ended outputs.",
  cognitive_barrier="That the objective must stay fixed while the policy improves."),
 "LIM": dict(id="amortize_improver_into_trained_policy", name="Amortize the Improver into a Trained Policy",
  definition="Instead of prompting a frozen model to curate memory, write skills, edit prompts, or design workflows, train that improver with RL or preference learning on the downstream improvement it causes, turning repeated per-task search into a learned policy.",
  operational_signature="improver acts (write memory, edit artifact, design workflow) → measure downstream task outcome → credit the improver's action → update improver weights",
  when_to_apply="When the improvement operation recurs often and its downstream effect is measurable.",
  cognitive_barrier="That curation and editing are fixed heuristics or zero-shot abilities rather than trainable skills."),
 "INT": dict(id="couple_context_and_weight_updates", name="Couple Context-Level and Weight-Level Learning",
  definition="Run fast, editable context adaptation (memory, skills, harness, prompts) and slow parameter updates as one system — internalizing validated experience into weights, or choosing which lever to pull when one plateaus.",
  operational_signature="adapt in context → collect experience-shaped rollouts → train weights on them → re-adapt context for the updated model",
  when_to_apply="When context adaptation plateaus or bloats while pure RL is sample-inefficient.",
  cognitive_barrier="That in-context adaptation and weight training are alternative, separately optimized pathways."),
 "GAT": dict(id="evidence_gated_retention", name="Gate Retention on Measured Evidence",
  definition="Decide what persists — a memory entry, a library skill, or a new incumbent — by measured counterfactual utility or a statistically sound comparison rather than by plausibility or a raw score delta. The move separates proposing a change from authorizing it.",
  operational_signature="propose a candidate entry or change → measure its marginal effect (paired, held-out, utility credit) → admit, demote, or roll back → keep provenance",
  when_to_apply="When evaluation is noisy, regressions are costly, or accumulated state degrades over time.",
  cognitive_barrier="That more retained experience, or a higher development score, means improvement."),
 "DIA": dict(id="diagnose_self_improvement", name="Diagnose Whether Self-Improvement Is Real",
  definition="Construct controlled interventions, benchmarks, or attacks that isolate whether persistent self-modification causally produces transferable and safe improvement, separating update quality, uptake, search compute, leakage, and contamination.",
  operational_signature="identify a confound in end-to-end evolution scores → design matched/frozen/held-out conditions or an attack → measure the isolated effect → report the failure mode",
  when_to_apply="When reported gains could be explained by extra compute, leakage, or memorization, or persistence opens new attack surfaces.",
  cognitive_barrier="That a rising score curve over evolution steps is evidence of genuine self-improvement."),
}

# code: (sub id, name, tactical_pattern, differentiation)
SUB = [
 ("ABS1", "Reflect on Outcomes into Transferable Lessons",
  "After each attempt the agent reflects on the outcome — often contrasting successful and failed trajectories, or rollouts within a group — and writes an abstracted lesson, principle, or strategy (frequently with a trigger condition) into a persistent store that is retrieved into the context of later tasks. The model stays frozen; the improvement is the accumulated lesson set. The decisive choice is abstraction level and grounding: lessons are tied to observed outcomes (ground truth, execution, or self-judgment) rather than generic advice, and contrast between outcomes isolates what actually mattered.",
  "Unlike the curated-memory sibling, the store mainly grows by appending reflections; unlike skill-package mining, the input is the agent's own trajectories rather than heterogeneous sessions or external resources."),
 ("ABS2", "Curate a Living Memory with Edit Operations",
  "The guidance store is treated as a living document maintained by explicit edit operations — add, update, merge, delete, no-op, or localized deltas — chosen by an LLM curator after each interaction. Consolidation, conflict resolution, and forgetting are first-class steps, so the store stays compact and consistent instead of growing monotonically, and incremental delta updates avoid the collapse that comes from rewriting the whole context.",
  "The distinguishing move is the editing policy over existing entries, not how a new lesson is extracted (ABS1) or how a reusable package is formatted (ABS3)."),
 ("ABS3", "Mine Interaction Streams into Skill Packages",
  "Recurring procedures are mined from interaction histories, pooled user sessions, guides, or scientific resources and compiled into structured, versioned skill packages (instructions, scripts, metadata, hierarchy) that are portable across agents and models. Extraction is followed by deduplication, merging with neighboring skills, and quality filtering before the package is published to a shared library.",
  "Targets portable, structured skill artifacts built from many sources, whereas ABS1 distills the agent's own outcomes into free-form lessons and ABS2 edits a single memory."),
 ("IDX1", "Retrieve and Adapt Precedent Cases",
  "Successful (and corrected failed) trajectories, workflows, subtasks, or repair records are stored as cases, possibly with instance-specific values removed, and retrieved by similarity or distribution matching to serve as demonstrations or plans for new tasks, then adapted to the new arguments. New outcomes are appended so the case base grows with use.",
  "Retains near-raw precedent and relies on matching and adaptation; ABS-family patterns instead compress experience into lessons, and IDX2 changes the store's structure rather than the retrieve-adapt loop."),
 ("IDX2", "Restructure the Memory Substrate",
  "The persistent store is reorganized into a structure suited to long-horizon recall — hierarchical tiers, temporal knowledge graphs, entity or sentence graphs, clusters, or paged OS-like tiers — with promotion, linking, and decay rules so retrieval stays precise and cheap as history grows. The improvement claim rests on representation and index design rather than on what lessons are written.",
  "Concerns the shape of the store and its index; IDX1 concerns case reuse and IDX3 concerns when retrieval is invoked."),
 ("IDX3", "Retrieve Only When Needed",
  "Retrieval becomes a decision taken by the agent or a controller — triggered by uncertainty, confusion, memory pressure, or an explicit reasoning-time request — instead of a fixed pre-task injection. Experience is consulted at the step where it is needed, and irrelevant or weakly matched memories are suppressed, which keeps context small and avoids distraction.",
  "Changes the timing and gating of memory use rather than its content (ABS) or structure (IDX2)."),
 ("CRY1", "Discover Skills Through Self-Directed Practice",
  "The agent proposes its own practice tasks (or works through training problems), writes code to solve them, verifies the code by execution, and abstracts verified solutions into reusable functions or APIs that join a skill library. A self-generated curriculum drives exploration, and the library compounds as new skills call older ones.",
  "Library growth is driven by an exploration curriculum before deployment demand, unlike CRY2 where a capability gap in a live task triggers synthesis."),
 ("CRY2", "Forge Tools When a Capability Gap Appears",
  "While solving a task, the agent detects that no available tool covers a need, then searches for, generates, installs, or wraps code (including external repositories) into a tool, debugs it against execution feedback, and registers it for reuse. Tool creation becomes an inline decision during problem solving rather than an offline engineering step.",
  "Triggered by live demand within a task; CRY1 practices proactively and CRY3 reorganizes an existing library."),
 ("CRY3", "Maintain a Compositional Skill Graph",
  "Executable skills are organized as a typed graph or DAG of compositions; traces assign responsibility to individual skills for localized repair, refactoring, and promotion of recurring text plans or tool sequences into new callable primitives, with rollback protecting mature skills. The library is treated as a structured program that is maintained, not just appended to.",
  "Operates on relations among existing executable skills (composition, promotion, repair) rather than on acquiring new ones (CRY1, CRY2)."),
 ("PAT1", "Propagate Feedback Through a Compound System",
  "The system is modeled as a computation graph of prompts, tools, and code; natural-language feedback on the final output is propagated backward so each upstream component receives a component-specific critique, conditioned on its neighbors, and is updated jointly. This is the 'textual backpropagation' move that solves credit assignment across multiple interacting components.",
  "Distributes credit across several components of a graph; PAT2 rewrites a single document from a critique, and PAT4 patches harness code from trace diagnosis."),
 ("PAT2", "Rewrite a Document from Diagnosed Errors",
  "A single prompt, instruction set, rule document, or tool description is iteratively rewritten from error analysis: failures (and often successes) are collected, a critic verbalizes what went wrong as a 'textual gradient' or strategy, and candidate rewrites are scored and the best retained, sometimes with momentum, beam, or tree search over rewrites. Atomic or localized edits and regression checks keep earlier wins.",
  "One textual artifact and a critique-driven rewrite; PAT1 handles multi-component credit, PAT3 targets skill files with attribution to sections, and POP1 relies on undirected mutation."),
 ("PAT3", "Revise Skills by Failure Attribution",
  "Execution failures are attributed to specific skill files or skill sections — distinguishing genuine skill defects from execution lapses — and the skill is rewritten with bounded edits, then re-run on the attributed cases and retained only if utility improves. Edit budgets and diagnosis-bound repair principles prevent rewrites from erasing working guidance.",
  "Specialized to reusable skill documents with per-section attribution; PAT2 rewrites prompts or rules and GAT2 decides admission and retirement rather than content edits."),
 ("PAT4", "Patch the Harness from Trace Diagnosis",
  "A coding agent inspects execution traces and harness source (tools, middleware, memory, control flow), localizes recurring failure mechanisms to editable code, writes scoped patches with falsifiable predictions, and promotes them after replay or regression checks, rolling back on failure. The harness becomes a versioned codebase improved by release-engineering discipline.",
  "Edits executable scaffolding with code-level diagnosis; PAT2 and PAT3 edit textual guidance, and REF1 additionally edits the improver itself."),
 ("POP1", "Search a Population of Prompts",
  "Candidate prompts or instructions are generated by LLM paraphrase, phrase edits, or genetic operators, scored on a small evaluation set, and the fittest are retained and reproduced; bandits, Bayesian surrogates, or tournaments allocate evaluation budget. Direction comes from selection pressure rather than from error diagnosis.",
  "Undirected variation plus selection over prompts; PAT2 uses critique-directed rewrites, and POP2 evolves executable programs."),
 ("POP2", "Evolve Programs with LLM Mutation",
  "Executable programs (algorithms, heuristics, reward functions, policies, kernels) are evolved by having an LLM propose code edits to sampled parents, running them against an automated evaluator, and keeping winners in a population or archive. Efficiency tricks include novelty rejection, bandit choice of mutation models, and budget allocation across lineages.",
  "Executable artifacts with an automated evaluator and no explicit knowledge store; POP3 adds distilled search memory and POP4 is defined by its diversity-preserving selection."),
 ("POP3", "Guide Evolution with Distilled Search Memory",
  "The search history is distilled into reusable knowledge — transformation rules, edit residuals, idea hierarchies, design principles, credited code snippets — that conditions future proposals and is updated as results arrive, sometimes shared across agents or campaigns. The search learns how to search in addition to finding better candidates.",
  "Adds an explicit, evolving knowledge layer over the search; POP2 relies on the raw parent pool, and REF patterns edit the search procedure itself."),
 ("POP4", "Preserve a Frontier of Complementary Candidates",
  "Instead of keeping one winner, selection retains a Pareto frontier (per-instance, cost-utility, or multi-objective), niches, or quality-diversity cells, so globally weaker candidates that win on some cases survive and can later be recombined. This counters premature convergence and lets complementary strategies merge.",
  "Defined by the selection and retention rule (frontier/QD), applicable to prompts, workflows, skills, or harnesses; siblings are defined by proposal mechanism."),
 ("ARC1", "Search an Offline Agent Design Space",
  "Agent designs — modules, graph topologies, workflow code — are represented in a searchable space (code, typed graphs, supernets, standardized modules) and optimized offline on a task set with execution scores, often via MCTS, evolution, or REINFORCE over connections, before a fixed design is deployed.",
  "Produces one design per task distribution before deployment; ARC3 adapts the team per instance at test time, and LIM2 trains a generator that outputs designs."),
 ("ARC3", "Co-Evolve Roles and Topology at Test Time",
  "During inference, a multi-agent team rewires itself: roles are generated or rewritten, edges added or pruned, and routers or profiles updated from task feedback, often at two rates (fast local capability, slower structural edits) with caching of verified specialists for later instances.",
  "Online, per-instance or per-stream structural adaptation; ARC1 searches offline, and PAT1 propagates textual feedback without necessarily changing structure."),
 ("REF1", "Apply the Improver to Itself",
  "A single lineage whose optimizer — a prompt, meta-agent program, or loop configuration — is submitted to its own improvement procedure, or improved by an outer loop using the downstream performance of what it produces, so stronger improvers are reused for later improvement. Promotion authority or review logic is often kept fixed as an anchor.",
  "Single-lineage self-application; REF2 branches from an archive of agents, and REF3 redesigns a separate learning mechanism such as memory."),
 ("REF2", "Branch Self-Modifying Agents from an Archive",
  "Self-modifying coding agents are kept in an open-ended archive; parents are sampled by performance, novelty, or estimated descendant productivity, edit their own code, and offspring are evaluated and archived even if not immediately better, so suboptimal agents can serve as stepping stones.",
  "Archive and parent selection are the load-bearing elements, unlike REF1's single lineage; distinct from POP2 because the evolved artifact is the self-modifying agent itself."),
 ("REF3", "Redesign the Inner Learning Mechanism",
  "An outer loop searches over the design of the inner loop's learning mechanism — memory schema, update and retrieval code, context-engineering skills, or retrieval-policy pools — evaluating each design by how well the agent learns with it across tasks.",
  "The target is the experience-learning mechanism (memory or context design), not the task policy or the improver's own code (REF1, REF2)."),
 ("CUR1", "Co-Train a Proposer Against a Solver",
  "A proposer (often sharing the solver's weights) is trained to generate tasks at the solver's frontier — rewarded for intermediate difficulty, uncertainty, regret, or learning progress — while the solver is trained on those tasks with verifiable or consensus rewards. The curriculum co-evolves without external data.",
  "Both roles are learned and coupled by a difficulty reward; CUR2 synthesizes tasks from diagnosed weaknesses without co-training an adversarial proposer."),
 ("CUR2", "Synthesize Tasks from Diagnosed Weaknesses",
  "The learner's current failures, uncertainty, or forgetting signals are diagnosed and used to generate, simplify, re-difficulty, or wrap tasks and environments (including procedural difficulty windows and simulated experience), which are verified and fed back into training.",
  "Generation is steered by diagnostics or schedules rather than by a co-trained adversary as in CUR1."),
 ("EVA1", "Evolve Rubrics as Training Rewards",
  "Query- or task-specific rubrics are generated, filtered for discriminativeness and correlation with correctness, and refreshed as the policy changes, then converted into dense rewards or step-level credit for RL; rubric generation may be trained jointly with the policy.",
  "The evolving evaluator serves as an RL reward signal; EVA2 revises evaluators that act as acceptance gates or measurement instruments."),
 ("EVA2", "Revise the Evaluator Against a Trusted Anchor",
  "Verifiers, test suites, detectors, or rubrics used to judge candidates are repaired or replaced when they disagree with a small trusted anchor (oracle bits, sparse labels, ground-truth checks), with selective score erasure or validity tests so that the evaluator can co-evolve with the artifacts without becoming gameable.",
  "Centered on anchoring evaluator validity for selection and measurement, unlike EVA1's reward shaping for weight updates."),
 ("LIM1", "Train the Curator on Downstream Utility",
  "Memory-write, memory-management, skill-extraction, or skill-curation actions are produced by a trainable policy whose reward comes from later task success when the written memory or skill is used, often across grouped task streams, so curation is learned instead of prompted.",
  "Trains the component that maintains persistent state; LIM2 trains the proposer of edits or designs."),
 ("LIM2", "Train the Proposer to Amortize Search",
  "An editor, reflector, algorithm generator, or workflow generator is trained by RL or preference optimization on the measured improvement its proposals cause (score deltas, next-episode return), replacing repeated per-task search with a single learned proposer that conditions on the query.",
  "Trains the proposer of artifact changes or designs; LIM1 trains memory and skill curation."),
 ("INT", "Couple In-Context Adaptation with Weight Training",
  "Context-level assets (memories, skills, harness, system prompts) and model weights are updated in one loop: experience-shaped rollouts become training data, validated context is internalized into parameters or latent tokens, or a controller chooses between scaffold edits and RL when progress stalls, at different timescales.",
  "The only sub-pattern of its parent; defined by the explicit coupling of the two learning pathways."),
 ("GAT1", "Value Memory Entries by Measured Utility",
  "Each stored experience receives a utility estimate learned from outcomes — Q-values, bandit statistics, citation rewards, with/without-memory contrasts, provenance-propagated credit — and retrieval ranking, admission, or suppression uses that value instead of semantic similarity alone.",
  "Entry-level credit assignment for memories; GAT2 governs library membership and GAT3 governs incumbent commits."),
 ("GAT2", "Govern Library Admission and Retirement",
  "Additions to a skill or experience library pass attribution and admissibility checks, marginal-gain or counterfactual tests, and regression budgets, and existing entries are retired or quarantined when evidence of harm accumulates, under bounded library size and versioned provenance.",
  "Manages membership of a shared library; GAT1 ranks entries and GAT3 decides whether to replace a single incumbent."),
 ("GAT3", "Use a Statistically Sound Commit Rule",
  "A candidate change replaces the incumbent only after passing a disjoint held-out or regression gate, a paired statistical test, an anytime-valid e-process, a drift index, or a sealed external audit — or, in theoretical work, only under conditions proven to preserve goals or bound value loss.",
  "Concerns the acceptance rule for whole-system updates, including formal analyses of when self-modification is safe; the GAT siblings manage individual entries and library membership."),
 ("DIA1", "Isolate Effects with Controlled Interventions",
  "Matched or frozen conditions — perturbing memory content, crossing evolver and executor models, freezing state while injecting feedback subsets, compute-matched baselines — separate whether gains come from the evolved artifact, extra search, or superficial prompt effects; negative results are reported as findings.",
  "An analysis protocol on existing systems; DIA2 builds reusable benchmarks and DIA4 targets adversarial persistence."),
 ("DIA2", "Benchmark Persistent Improvement over Streams",
  "Benchmarks present ordered task streams with frozen validation, held-out or shifted test views, replay, and cost accounting to measure whether retained experience transfers, persists, and avoids forgetting, rather than single-episode success.",
  "Measures the persistence and transfer of improvement; DIA3 measures the capability to run the improvement loop."),
 ("DIA3", "Benchmark Agents Doing AI R&D",
  "Isolated, budgeted workspaces ask agents to build training pipelines, harnesses, data strategies, or learning algorithms, with frozen post-submission evaluators that rerun from scratch to verify that the artifact itself improves learning.",
  "Evaluates the capability to perform the self-improvement work, not the persistence of improvements (DIA2)."),
 ("DIA4", "Audit Persistence as an Attack Surface",
  "Poisoning, injection, tampering, or benign misevolution is introduced into evolving memory, skills, or harnesses, and its persistence, propagation, and evasion of defenses are traced across sessions and generations.",
  "Safety and adversarial focus on persistent state, unlike the capability-focused DIA siblings."),
]

code2sid = {c: f"H{i:02d}" for i, (c, *_ ) in enumerate(SUB)}
main_of = lambda code: MAIN[code[:3]]["id"]

# validate assignment
assert set(assign) == set(ids) and len(ids) == len(set(ids)), "coverage mismatch"
lines, counts = [], collections.Counter()
for a in ids:
    code, sec, fit = assign[a]
    assert code in code2sid, code
    secs = [MAIN[s]["id"] for s in sec.split(",") if s]
    assert len(secs) <= 2 and main_of(code) not in secs, (a, code, sec)
    assert fit in "hl"
    counts[code2sid[code]] += 1
    lines.append({"arxiv": a, "sub_pattern": code2sid[code], "secondary_main": secs,
                  "fit": "high" if fit == "h" else "low"})

subs = [{"id": code2sid[c], "parent": main_of(c), "name": n, "tactical_pattern": t,
         "differentiation_within_parent": d, "n_papers": counts[code2sid[c]]} for c, n, t, d in SUB]
mains = []
for k, m in MAIN.items():
    m = dict(m, n_papers=sum(s["n_papers"] for s in subs if s["parent"] == m["id"]),
             sub_patterns=[s["id"] for s in subs if s["parent"] == m["id"]])
    mains.append(m)
mains.sort(key=lambda m: -m["n_papers"])

NOTES = """Revision pass: (1) split 'textual gradient' into PAT1 (multi-component credit propagation) vs PAT2 (single-document critique rewrite); single-prompt TG papers moved to PAT2.
(2) merged 'amortized workflow generator' (formerly under ARC) into LIM2: training a workflow generator and training a prompt/harness editor are the same move (amortize search into a learned proposer).
(3) merged 'certify the commit rule' (theory/statistical) into GAT3; merged two INT subclusters (internalize vs lever-choice) because several papers do both.
(4) reassigned 4 boundary papers to bring EVA1, REF2 and IDX3 to at least 8 (co-trained reward model -> EVA1; descendant-productivity meta-skills -> REF2; on-demand and RL-iterative retrieval -> IDX3).
Residual: no residual bucket (0%); weak fits are flagged fit=low instead (see counts). Largest sub: ABS1; IDX1 and PAT4 carry the most low-fit domain-application papers.
RS counterparts: diagnose_self_improvement ~ controlled_diagnostic_design; self_generate_the_curriculum / coevolve_the_evaluator ~ self_supervised_signal_engineering;
abstract_experience_into_guidance / index_experience_for_reuse ~ adapt_via_conditioning; make_the_improver_editable ~ generative_process_redesign (liberate a fixed component); evidence_gated_retention ~ assumption_audit_and_pivot (drop 'score delta = improvement')."""

with open(OUT + "taxonomy.json", "w") as f:
    json.dump({"main_patterns": mains, "sub_patterns": subs, "notes": NOTES}, f, indent=2, ensure_ascii=False)
with open(OUT + "assignments.jsonl", "w") as f:
    f.writelines(json.dumps(l) + "\n" for l in lines)

# --- self-check on written files ---
tax = json.load(open(OUT + "taxonomy.json"))
asg = [json.loads(l) for l in open(OUT + "assignments.jsonl")]
mids = {m["id"] for m in tax["main_patterns"]}
sids = {s["id"] for s in tax["sub_patterns"]}
assert sorted(a["arxiv"] for a in asg) == sorted(ids)
assert all(a["sub_pattern"] in sids and set(a["secondary_main"]) <= mids for a in asg)
assert all(s["parent"] in mids for s in tax["sub_patterns"])
c = collections.Counter(a["sub_pattern"] for a in asg)
assert all(s["n_papers"] == c[s["id"]] for s in tax["sub_patterns"])
assert min(c.values()) >= 8, c
assert len(NOTES.splitlines()) <= 10
print("OK", len(mids), "main", len(sids), "sub", "low-fit", sum(a["fit"] == "low" for a in asg))
for m in tax["main_patterns"]:
    print(f'{m["n_papers"]:4d} {m["id"]}', [(s, c[s]) for s in m["sub_patterns"]])
