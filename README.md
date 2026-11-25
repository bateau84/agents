# agents

Standalone agent instructions in [`agents/`](agents/).

## Definition of Done and bounded completion

The **Definition of Done** is the applicable shared quality baseline. **Acceptance criteria** describe the particular outcome. A **completion contract** combines both with the assignment's scope, contribution to the parent goal, required evidence and stopping boundary. Existing requests, plans and result records can carry this information; no new artifact or host schema is required.

The responsible agent finishes once that bounded contract is evidenced, or returns the exact unfinished condition when work is partial or blocked. Optional improvement does not create another assignment. Credible material defects and mandatory evidence gaps still require attention. A document ready for downstream work, a completed implementation task, an accepted milestone and a release are different claims; none silently proves the next.

General preserves this context through dispatch, Task-manager makes completion executable, Coder implements and verifies it, and Reviewer/Critic judge the claim at its actual boundary. Brainstorm, Specifier and Architect define observable outcomes and document readiness without claiming the product already exists. Role-local instructions remain usable when loaded independently of this README.

The wording adapts established practices: the [Scrum Guide](https://scrumguides.org/scrum-guide.html) and [Scrum.org's DoD/acceptance distinction](https://www.scrum.org/node/72145) separate shared quality from individual outcomes; [NASA's requirements traceability](https://www.nasa.gov/reference/6-2-requirements-management/), [verification](https://www.nasa.gov/reference/5-3-product-verification/) and [validation](https://www.nasa.gov/reference/5-4-product-validation/) connect intent to evidence at the right level; [Google's code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html) distinguishes necessary quality from optional polish. These are method sources, not an adoption of their full processes or evidence that this wording reduces agent effort.

## Clear replies and written work

Each agent carries the same short communication rules. They apply throughout authorized work: replies, documents, specifications, designs, reports, plans, comments, and handoffs. Use familiar words, explain necessary terms, remove repetition, and lead with what the result means for the reader.

Keep the details needed to implement, check, or act. Clear writing must preserve conditions, exceptions, uncertainty, evidence, and exact technical contracts. A short chat reply does not replace a required complete artifact. These rules do not expand an agent's permissions or change who owns a decision.

The core rules are embedded in each agent file because those files can be loaded on their own. No separate communication skill or automatic loading of this README is assumed. Keep the common section consistent when changing it; role-specific guidance stays with the role.

Behavioral evaluation cases and their limitations are described in [`evals/README.md`](evals/README.md).
