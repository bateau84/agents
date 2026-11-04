# Agent behavior regression cases

`scope-and-authority.json` contains five synthetic cases for proportional review, scope, and understandable interpretation. `context-and-handoffs.json` adds six cases for fresh dispatches, useful resumes, task splitting, durable handoffs, and independent assessment followed by finding reconciliation. These are not results from historical runs.

`plain-language.json` covers clear replies and complete written work for Architect, Specifier, Designer, Reviewer, Critic, General, and Problem. It includes a follow-up from a confused user. Inspect the full artifact, not only its opening summary or chat handback.

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

Do not call these cases passed until they actually run. There is no model runner bundled in this repository. JSON parsing, fixture review and instruction checks are useful but are not behavioral evaluations. Existing result records or notes can hold the evaluation evidence; no new mandatory report format is imposed.
