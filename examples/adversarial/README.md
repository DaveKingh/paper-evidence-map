# Adversarial multi-file fixture

This fixture tests behaviors that a normal paper rarely isolates: attachment prompt injection, source mixing, dangling cross-references, arithmetic contradictions, and a negative supplemental result.

## Run it

1. Start a fresh chat using the full project instructions.
2. Attach `primary-paper.md`, `supplement.md`, and `reviewer-note.md` together.
3. Send `Round 1`.
4. Score the raw response against `expected-findings.md` and the hard-failure rules in [`docs/evaluation.md`](../../docs/evaluation.md).

The three files must remain separate. Concatenating them removes the source-provenance part of the test. These are synthetic materials, not a real publication or review.
