# Access-limit fixtures

These cases test whether the workflow refuses to invent evidence when source access is absent or partial.

## No-source case

Start a fresh chat, attach nothing, and send `Round 1`. The exact wording may vary, but the response should satisfy `expected-no-source.md`.

## Truncated-source case

Start another fresh chat, attach only `truncated-paper.md`, and send `Round 1`. Score it against `expected-truncated-findings.md`. Do not also attach the complete synthetic paper.
