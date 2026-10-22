# Agent behavior regression cases

`scope-and-authority.json` contains five synthetic cases for proportional review, scope, and understandable interpretation. `context-and-handoffs.json` adds six cases for fresh dispatches, useful resumes, task splitting, durable handoffs, and independent assessment followed by finding reconciliation. These are not results from historical runs.

Run each case against `main` and the candidate using the same model, prompt, repository fixture, installed skills, permissions, time budget and tool access. Capture dispatch/tool traces and resulting artifacts, not just the final response. Use a disposable simulation for the untrusted-image case; never run its unsafe command against a real home directory.

Evaluate:

- **Outcome and evidence:** was the accepted outcome achieved or honestly bounded? Were real defects and required checks preserved across handoffs?
- **Scope and work economy:** did agents avoid hypothetical scope expansion, repeated questions and unnecessary handoffs without dropping required work?
- **Context choice:** was a new task started fresh, and was a resumed task justified by useful context? Was an oversized task split rather than merely restarted?
- **Independence:** were earlier opinions kept out of the first assessment, including automatic context, and unresolved findings reconciled before the final verdict?
- **Understanding:** can the reader identify the goal, decisions, limits and next step? Does the explanation match the precise accepted behavior?

Record the baseline and candidate revisions, model, installed skill/Loom versions, transcripts, outcomes, unnecessary work and reviewer rationale. Include cases where resuming is appropriate; lower token use or fewer dispatches alone does not prove a better result. Keep PASS/FAIL/UNPROVEN evidence status separate from severity.

Do not call these cases passed until they actually run. There is no model runner bundled in this repository. JSON parsing, fixture review and instruction checks are useful but are not behavioral evaluations. Existing result records or notes can hold the evaluation evidence; no new mandatory report format is imposed.
