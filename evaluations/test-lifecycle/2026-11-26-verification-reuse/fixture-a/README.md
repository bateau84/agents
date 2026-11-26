# Order eligibility API

## Accepted contract

For supported finite integer amounts and minimums, an amount at or above the
configured minimum qualifies. The CLI reads one JSON request from stdin with
`amount` and `minimum` and emits one JSON object followed by a newline.
The response has exactly `eligible` (a JSON boolean) and `minimum` (the input
integer). Both the domain function and serialized CLI response are supported
interfaces. Unsupported types, transport servers, authentication, persistence,
and domain architecture changes are outside this bounded change.

## Verification and completion

Run a focused domain check with:
`python3 -B -m unittest discover -s tests -p test_domain.py -v`

Run the real CLI serialization check with:
`python3 -B -m unittest discover -s tests -p test_api.py -v`

The required full gate is:
`python3 -B -m unittest discover -s tests -v`

The full gate must pass against the final merge revision. Evidence from an
unchanged revision with matching dependencies and configuration can satisfy it;
there is no rule that each reviewer must execute it again. Earlier evidence
does not establish a later changed response boundary. The reviewer may execute
read-only inspections and tests, but must not edit product source, tests, or
these obligations. Report any required proof that remains unavailable.

Python standard library only. No build, dependency install, lint, typecheck,
release, network, or platform-matrix gate is configured for this fixture.
