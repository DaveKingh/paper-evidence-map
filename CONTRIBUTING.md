# Contributing

Thank you for helping make paper reading more auditable. Contributions are judged by whether they improve evidence fidelity, reproducibility, or usability—not by how sophisticated the wording sounds.

## High-value contributions

- A synthetic paper fixture with one or more clearly planted failure modes.
- An anonymized, non-copyrighted failure report and minimal reproduction.
- A discipline-specific evaluation addendum reviewed by a domain user.
- A prompt change with before/after multi-run scores.
- A translation maintained by a fluent speaker.
- Accessibility, privacy, or documentation improvements.

Do not upload copyrighted papers, confidential manuscripts, peer-review material, personal data, or model output that reveals restricted source text.

## Before opening an issue

Search existing issues. If a real paper exposed the problem, reduce it to a synthetic example whenever possible. State the model/mode, date, files available, exact trigger, observed output, expected behavior, and why it matters.

## Pull-request workflow

1. Fork the repository and create a focused branch.
2. Make one logically complete change.
3. Add or update a fixture when behavior changes.
4. Run:

   ```bash
   python scripts/validate.py
   python scripts/validate.py --response examples/synthetic/expected-output.md
   ```

5. For prompt changes, run the same fixture at least three times before and after. Include all scores and known regressions in the PR.
6. Update `CHANGELOG.md` under Unreleased for user-visible changes.
7. Open a non-draft PR only when checks pass.

## Adding a fixture

Create a folder under `examples/` containing:

- `paper.md`: entirely original or clearly redistributable input;
- `expected-findings.md`: content-level answer key with locations;
- `expected-output.md`: one representative output, identified as such.

Keep the fixture short enough for maintainers to audit manually. Include failures that weak summarizers are likely to miss, not obscure trivia.

## Prompt-change evidence

Report the model/mode, run date, number of runs, rubric totals, required-finding hit rate, fabricated-locator count, and any regression. A single best-looking run is insufficient.

## Style

- Prefer direct, testable instructions.
- Use “not specified” rather than guessing.
- Avoid unsupported claims that the workflow eliminates hallucination or guarantees correctness.
- Keep product-specific UI instructions in docs, not in the core evidence rules.
- Preserve English and Chinese behavior parity when possible.

By contributing, you agree that your contribution is licensed under the repository's MIT License and that you have the right to submit it.

