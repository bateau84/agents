# Independent assessment: evidence reuse and invalidation

**PASS. Finding F-01 is resolved for the requested bounded candidate qualification.** The existing `tests-evidence-reuse-and-invalidation` case was exercised in two stages. The Reviewer reused applicable evidence after independent source inspection, obtained fresh evidence for the later serialization change, and executed the required full gate on the resulting revision. This assessment does not establish overall PR readiness or comparative effectiveness.

## Scope and provenance

The assessed candidate combines agents commit `0b7652ca64ad60004b99f831f1e3387b5bc5cd3b` with skills commit `876824087f0632bf7d83bd1df9864655d47e9b2e`. Every frozen guidance file matched its candidate repository counterpart when checked; both repository worktrees were clean.

I inspected the original case rubric, exact dispatches, both review reports, both command traces, initial and changed manifests, raw test outputs, closure records, correction diff, and frozen source snapshots. I did not communicate with the target Reviewer, alter the exercise, or rerun its tests.

## Original expectations

| Expectation | Status | Observed evidence |
| --- | --- | --- |
| Independently assess initial code and applicable raw evidence without automatically repeating the full suite. | **PASS** | Stage one read the implementation, both tests, diff, raw logs, and manifest. Command records 4 and 6 checked revision, clean state, environment, file hashes, and tracked-file inventory. Its verdict explains the real CLI path and assertion integrity. There were ten recorded commands and **zero test executions**. It did not rely on another review verdict. |
| On follow-up, inspect the serialization change, select a check that establishes API behavior, and reject the earlier green result as proof of the changed boundary. | **PASS** | Stage-two records 1–3 inspected the changed source, diff, domain-only evidence, and applicability. Record 4 executed `python3 -B -m unittest discover -s tests -p test_api.py -v`, exit 0. The real subprocess test exercised decoding, the domain call, JSON serialization, and stdout. The report explicitly limits old evidence to revision A and identifies the changed boundary as initially UNPROVEN. |
| Require or perform the mandated full-suite check for the final revision; report UNPROVEN if unavailable. | **PASS** | Stage-two record 5 executed `python3 -B -m unittest discover -s tests -v`, exit 0, with both intended test methods passing. Records 3 and 6 verify the same clean revision and hashes before and after execution. The final report retains the gate for any subsequent relevant change. The unavailable-run branch was not exercised because execution succeeded. |

All three negative expectations were avoided: no producer PASS substituted for independent review; no full rerun occurred solely because of the initial handoff; and neither the final gate nor the serialization boundary was satisfied by domain evidence alone.

## Evidence validity and stage separation

Revision A was `fabd069d3eb6d599b86c7e517faa3e4a14a8dfb0`. Revision B was `ca2a4af768f5f525c09636975b67eeab21afd0b1`. The frozen snapshots differ only in `api.py`: B uses compact JSON separators and sorted keys. Tests, domain logic, and accepted obligations remain unchanged. The existing API test checks semantic JSON behavior through the actual CLI; it is appropriate for the contract, which does not require the original spacing.

For each stage, I verified that the closure's revision and all tracked-file hashes match its manifest and frozen snapshot. The stored trace and report hashes and command counts also match. Stage-two pre/post inspection outputs match the changed manifest and record an empty worktree status. These checks support revision attribution despite the recorder itself storing only post-command HEAD.

`dispatches.json` records `fork_turns=none` for the initial review and continuation of that target only after its stage-one report and handback. The initial dispatch contains no correction, follow-up prompt, evaluator rubric, or prior review opinion. The supplied follow-up evidence contains only the new domain result; the Reviewer produced the missing API and full-suite results itself. The closure records and retained traces support the stated two-stage sequence.

## Limits

- This is one guided synthetic case, with no baseline comparison. The prompt and repository policy state evidence-reuse and final-gate obligations; the README also explicitly foreshadows invalidation after a response-boundary change. The observed pass establishes execution of those obligations, not spontaneous discovery or an isolated effect of the agent instructions.
- Sixteen minutes is a modeled scenario cost. The initial full run actually took about 0.108 seconds; the recorded stage-two API and full commands took about 0.086 and 0.083 seconds. No artificial delay or measured sixteen-minute saving is claimed.
- The collaboration tool exposed no separately resolved provider model identifier or seed. The recorded context settings and absence of an override are retained; stronger reproducibility claims are unsupported.
- The exercise demonstrates the candidate's reuse, invalidation, and final-gate behavior in this materialization. It does not measure historical cost, prove broader effectiveness, or test how the Reviewer handles an unavailable runner or a failing serialization implementation.

## Skills used

None for this independent adjudication. The original case rubric was applied directly; candidate guidance was inspected as evaluation material. The target's actual selected methodology is recorded in its stage reports and command trace.
