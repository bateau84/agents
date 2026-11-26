# agents

Standalone agent instructions in [`agents/`](agents/).

## Definition of Done and bounded completion

The **Definition of Done** is the applicable shared quality baseline. **Acceptance criteria** describe the particular outcome. A **completion contract** combines both with the assignment's scope, contribution to the parent goal, required evidence and stopping boundary. Existing requests, plans and result records can carry this information; no new artifact or host schema is required.

The responsible agent finishes once that bounded contract is evidenced, or returns the exact unfinished condition when work is partial or blocked. Optional improvement does not create another assignment. Credible material defects and mandatory evidence gaps still require attention. A document ready for downstream work, a completed implementation task, an accepted milestone and a release are different claims; none silently proves the next.

Allocate shared quality obligations to responsible owners and acceptance boundaries. Local completion satisfies only the criteria and quality obligations allocated to that assignment. Independent review or integration proof assigned elsewhere remains mandatory and open at the parent boundary. For example, Coder can finish implementation, regression tests and docs before Reviewer performs independent review; General completes the parent objective only after all its obligations are evidenced. Executors cannot move an unmet check to another owner or waive it to obtain DONE.

General preserves this context through dispatch, Task-manager makes completion executable, Coder implements and verifies it, and Reviewer/Critic judge the claim at its actual boundary. Brainstorm, Specifier and Architect define observable outcomes and document readiness without claiming the product already exists. Role-local instructions remain usable when loaded independently of this README.

The wording adapts established practices: the [Scrum Guide](https://scrumguides.org/scrum-guide.html) and [Scrum.org's DoD/acceptance distinction](https://www.scrum.org/node/72145) separate shared quality from individual outcomes; [NASA's requirements traceability](https://www.nasa.gov/reference/6-2-requirements-management/), [verification](https://www.nasa.gov/reference/5-3-product-verification/) and [validation](https://www.nasa.gov/reference/5-4-product-validation/) connect intent to evidence at the right level; [Google's code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html) distinguishes necessary quality from optional polish. These are method sources, not an adoption of their full processes or evidence that this wording reduces agent effort.

## Test-suite ownership

Agents maintain the value of the affected suite as well as its coverage. Coder inspects existing tests and chooses whether to extend, consolidate, replace, retire, or add coverage. Debugger separates diagnostic experiments from durable regressions. Reviewer and Critic assess distinct protection and maintenance cost; General and Task-manager preserve applicable evidence across handoffs, and Evaluator examines verification cost over whole objectives. Role-local instructions remain usable without loading this README.

The shared method lives in `test-driven-development` in [bateau84/skills](https://github.com/bateau84/skills/tree/main/skills/test-driven-development). It retains TDD's behavioral test list and Red–Green–Refactor cycle, including refactoring tests. The [test pyramid's duplication guidance](https://martinfowler.com/articles/practical-test-pyramid.html#AvoidTestDuplication) and [Google's testing guidance](https://abseil.io/resources/swe-book/html/ch11.html) inform choosing adequate, economical evidence while preserving distinct integration boundaries. Domain language and invariants guide what to protect; DDD does not prescribe test counts or suite-duration quotas. These are method choices, not measured evidence that these instructions reduce cost.

Required gates, independent judgment, accepted guarantees, and meaningful regression protection remain binding. A long suite can be justified. The goal is confidence worth its cumulative cost, not fewer tests or a universal time limit.

## Clear replies and written work

Each agent carries the same short communication rules. They apply throughout authorized work: replies, documents, specifications, designs, reports, plans, comments, and handoffs. Use familiar words, explain necessary terms, remove repetition, and lead with what the result means for the reader.

Keep the details needed to implement, check, or act. Clear writing must preserve conditions, exceptions, uncertainty, evidence, and exact technical contracts. A short chat reply does not replace a required complete artifact. These rules do not expand an agent's permissions or change who owns a decision.

The core rules are embedded in each agent file because those files can be loaded on their own. No separate communication skill or automatic loading of this README is assumed. Keep the common section consistent when changing it; role-specific guidance stays with the role.

Behavioral evaluation cases and their limitations are described in [`evals/README.md`](evals/README.md).
