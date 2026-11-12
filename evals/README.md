# Agent behavior regression cases

`evidence-and-evaluation.json` covers Evaluator's whole-objective attribution, positive learning, trend uncertainty and opt-in live experiments. Fixtures specify boundaries; they do not establish historical outcomes.

`quality-scenarios.json` exercises QS discovery, cross-role traceability, bounded fixes that should not gain QS ceremony, unsettled targets, evidence under actual conditions, and BR/QS/OC composition during review and adversarial adjudication. It also checks that compatible artifact sets are not turned into false conflicts or new gates. These synthetic fixtures are not evaluated outcomes.

`scope-and-authority.json` contains five synthetic cases for proportional review, scope, and understandable interpretation. `context-and-handoffs.json` adds six cases for fresh dispatches, useful resumes, task splitting, durable handoffs, and independent assessment followed by finding reconciliation. These are not results from historical runs.

`plain-language.json` covers clear replies and complete written work for Architect, Specifier, Designer, Reviewer, Critic, General, and Problem. It includes a follow-up from a confused user. Inspect the full artifact, not only its opening summary or chat handback.

`documentation-maintenance.json` covers accepted requirement refactoring, General/Coder routing for settled terminology, and unresolved findings across review handoffs. Check the source documents, resulting edits, and dispatches; preserving meaning and ownership matters more than mentioning a skill.

`strategic-programming.json` covers useful local preparation, direct fixes, one-implementation boundaries, speculative extension points, behavior preservation, consequential migration, review of caller complexity, and evidence-based deferral. It includes an architectural comparison where direct extension is sufficient. Judge concrete changes and routing decisions; neither the smallest diff nor the largest refactor automatically wins.

Run each case against `main` and the candidate using the same model, prompt, repository fixture, installed skills, permissions, time budget and tool access. Capture dispatch/tool traces and resulting artifacts, not just the final response. Use a disposable simulation for the untrusted-image case; never run its unsafe command against a real home directory.

Evaluate:

- **Outcome and evidence:** was the accepted outcome achieved or honestly bounded? Were real defects and required checks preserved across handoffs?
- **Scope and work economy:** did agents avoid hypothetical scope expansion, repeated questions and unnecessary handoffs without dropping required work?
- **Context choice:** was a new task started fresh, and was a resumed task justified by useful context? Was an oversized task split rather than merely restarted?
- **Independence:** were earlier opinions kept out of the first assessment, including automatic context, and unresolved findings reconciled before the final verdict?
- **Understanding:** can the reader identify the goal, decisions, limits and next step? Does the explanation match the precise accepted behavior?
- **Whole-work clarity:** are requirements, explanations, findings, and handoffs understandable throughout? Does a reader unfamiliar with the specialist terms still know what happens and what to do? Required technical names can stay when their meaning is clear.
- **Meaning preserved:** do conditions, exceptions, ordering, numbers, units, uncertainty, source references, and unrun checks survive? Can an implementer or reviewer use the artifact without inventing missing detail?

For the language cases, ask the intended reader to explain the outcome, limits, and any next step in their own words. Compare the answer with the fixture facts. Judge accuracy and understanding before length; word counts and reading scores alone cannot establish a pass. A detailed artifact can pass when its detail is needed. A shorter reply fails if it hides a material finding or changes a promise. After a confusion follow-up, check whether the explanation actually changes or adds a useful example.

Record the baseline and candidate revisions, model, installed skill/Loom versions, transcripts, outcomes, unnecessary work and reviewer rationale. Include cases where resuming is appropriate; lower token use or fewer dispatches alone does not prove a better result. Keep PASS/FAIL/UNPROVEN evidence status separate from severity.

For strategic-programming cases, materialize the source facts before either run, keep the evaluator rubric separate, and inspect preserved behavior and actual ownership of rules or coordination. An agent-only comparison keeps skills fixed; a combined agents-and-skills comparison must name both revisions and limit its conclusions to that combined change. A skill load is useful discovery evidence, not evidence that the method was followed.

To test whether preparation helps later work, run a second related feature in a fresh session against each resulting repository, without showing the first agent that follow-up task. Compare correctness and the total preparation, implementation, review, and follow-up effort; include a case where direct implementation is sufficient. The optional companion `software-engineering/evals/artifact-workflow.md` in [bateau84/skills](https://github.com/bateau84/skills/tree/main/skills/software-engineering/evals) describes a concrete two-change exercise. It is evaluation material, not an installed-agent or Loom dependency. These JSON cases alone do not establish later-change benefit.

Do not call these cases passed until they actually run. There is no model runner bundled in this repository. JSON parsing, fixture review and instruction checks are useful but are not behavioral evaluations. Existing result records or notes can hold the evaluation evidence; no new mandatory report format is imposed.
