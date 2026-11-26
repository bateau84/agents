# Verification reuse across reviews — executed qualification

**PASS for the bounded case `tests-evidence-reuse-and-invalidation`.** This record
closes review finding F-01 for agents PR #18. It executes the existing case from
[`test-lifecycle.json`](../../../evals/test-lifecycle.json); it adds no new case or CI gate.

## Observed behavior

| Stage | Evidence supplied | Reviewer action | Outcome |
| --- | --- | --- | --- |
| Initial review, revision A | Source, tests, real full/domain results, revision, environment and file hashes | Independently inspected the implementation and assertions; checked evidence applicability; executed no tests | Reused the applicable full-suite evidence and returned a bounded GO |
| Later serialization correction, revision B | Changed source and diff; a new domain pass only | Identified the changed CLI and full-gate proof as unproven; ran the real CLI serialization check and required full suite | Both checks passed for B; the previous run was not promoted to B evidence |

The initial target started with `fork_turns=none`. The later correction and
follow-up were not created or delivered until its first review completed and
source immutability was checked. The same target then performed the follow-up;
that second review is not described as independent rediscovery.

Both stages used the candidate Reviewer charter at agents
`0b7652ca64ad60004b99f831f1e3387b5bc5cd3b` and companion skills at
`876824087f0632bf7d83bd1df9864655d47e9b2e`. No role or skill instruction changed
during execution. Product source, tests and policy were unchanged by the target.
The recorder captured actual reads, commands, outputs, revisions, exits and
timings; closure records and the target's checks bind each stage to clean source
and all tracked-file hashes.

## Evidence map

- [Independent assessment](assessment.md): per-expectation adjudication and F-01 closure.
- [Result and limits](result.json): compact observed outcome.
- [Exact dispatches](dispatches.json): initial task, context settings, and later follow-up.
- [Guidance provenance](guidance-manifest.json): frozen files, source revisions and hashes.
- [Revision A fixture](fixture-a/README.md): runnable source and tests.
- [Initial evidence manifest](evidence/initial-manifest.json), [raw full-suite output](evidence/initial-full.stderr.txt), and [implementation diff](evidence/initial-change.patch).
- [First review](evidence/stage1-review.md), [command trace](evidence/stage1-commands.jsonl), and [closure](evidence/stage1-close.json).
- [Serialization diff](evidence/serialization-change.patch) and [new domain-only evidence](evidence/changed-manifest.json).
- [Follow-up review](evidence/stage2-review.md), [command trace](evidence/stage2-commands.jsonl), and [closure](evidence/stage2-close.json).
- [Command recorder](capture.py): the bounded recording utility used during this exercise.

## Inspect or reproduce

All dependencies are in Python's standard library. Copy `fixture-a/` into a
disposable directory and run `python3 -B -m unittest discover -s tests -v`.
Apply `evidence/serialization-change.patch` there with `git apply` to obtain B,
then run the focused API command and full command shown in the trace. The
recorded Git revisions identify the original disposable fixture history; use
the manifests' content hashes to compare a reconstructed copy.

To repeat the model exercise, use separate `project/`, `guidance/`, and
`evidence/` directories under an owned temporary root; the recorder expects that
layout. Restore the guidance from the pinned sources and adapt only the temporary
path in the saved dispatches. Keep the later source change and follow-up hidden
until the first review finishes, and collect actual results rather than copying
this run's verdict. Owned temporary execution files are cleaned after this record is published.

## Limits

This is one guided synthetic case with explicit repository obligations. The
original case's sixteen-minute full-suite cost is a **modeled input**, not an
observed duration; the small executable fixture ran quickly and had no artificial
delay. Actual timings remain in the raw records. No production time saving is
claimed. The protocol supplied the obligations and scope; it is not evidence of
unprompted adoption or a causal comparison against older instructions.

The subagent interface exposed no separate resolved provider model identifier or
sampling seed. No model override was requested. There was no old-instruction or
no-skill comparison, population study, failing-serializer/unavailable-run variant,
whole-objective cost evaluation, or product-repository suite execution. Those
limits do not turn this observed staged result into a broader effectiveness claim.
