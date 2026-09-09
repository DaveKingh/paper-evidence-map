# Contributing

Thank you for helping make paper reading more auditable. Contributions are judged by whether they improve evidence fidelity, reproducibility, or usability—not by how sophisticated the wording sounds.

## High-value contributions

- An original synthetic paper fixture with a clear answer key and planted failure modes.
- An anonymized, non-copyrighted failure report with a minimal reproduction.
- A discipline-specific evaluation addendum reviewed by a domain user.
- A prompt change with complete before/after multi-run results.
- A translation maintained by a fluent speaker.
- Accessibility, privacy, portability, or documentation improvements.

Do not upload copyrighted papers, confidential manuscripts, peer-review material, personal data, or model output that reveals restricted source text.

## Before opening an issue

Search existing issues. If a real paper exposed the problem, reduce it to a synthetic example whenever possible. State the repository version, product and displayed model/mode, run date, available files, exact trigger, observed output, expected behavior, and why the difference matters.

Use the bug form for reproducible defects, the prompt form for instruction changes, and the fixture form for new evaluation cases. Security or privacy reports belong in the private channel described in [SECURITY.md](SECURITY.md).

## Pull-request workflow

1. Fork the repository and create one focused branch.
2. Make one logically complete change. Preserve English/Chinese parity where the behavior is shared.
3. Add or update a fixture for behavior changes, or explain why no fixture applies.
4. From the repository root, run the complete local gate below with Python 3.9 or newer:

   ```bash
   python -m unittest discover -s scripts/tests -v
   python scripts/build_fixture_pdf.py --check
   python scripts/validate.py
   python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic
   python scripts/validate.py --json examples/synthetic/expected-output.json --fixture synthetic
   ```

   On systems where Python 3 is named `python3`, replace `python` with `python3`.

5. For prompt changes, run the same fixture at least three times before and after. Include every run, not only the best one.
6. Update `CHANGELOG.md` under **Unreleased** for user-visible changes.
7. Open a non-draft PR only when the local gate passes. GitHub Actions repeats it on Python 3.9 and the newest tested Python.

## Adding a fixture

Create a folder under `examples/` containing:

- `paper.md`: the canonical, entirely original or clearly redistributable input;
- `paper.pdf`: a convenient upload copy of the same input;
- `expected-findings.md`: a content-level answer key with valid locations;
- `expected-output.md`: one representative Markdown output, identified as such;
- `expected-output.json`: the same evidence map in the included JSON contract.

Keep fixtures short enough to audit manually. Test consequential failure modes—overclaiming, leakage, missing uncertainty, contradictory tables—not obscure trivia. A representative output is documentation, not proof that the prompt is reliable.

Product-integration behavior that the offline validator cannot reproduce may use a manual fixture instead. Include a setup README, minimal original old/new sources, a clear oracle, and an explicit statement of what must be checked in the product. See `examples/current-chat-precedence/` for the expected pattern.

The bundled synthetic fixture treats `paper.md` as its canonical source. Maintainers can make a deterministic, dependency-free PDF candidate with:

```bash
python scripts/build_fixture_pdf.py --output work/paper.generated.pdf
```

Before replacing the distributed PDF, extract its text, render every page, and visually check clipping, tables, spacing, and legibility. Then run `python scripts/build_fixture_pdf.py --check`. The repository check verifies PDF structure, two-page count, and critical extractable phrases; it does not replace visual QA.

## Prompt-change evidence

Report all of the following in the PR:

- old and new commit or prompt version;
- product, displayed model/mode, and run date;
- number of runs and identical test conditions;
- manual-rubric total and per-dimension scores;
- required-finding hit rate and fabricated-locator count;
- regressions, unusually poor runs, and unresolved tradeoffs.

The automated structural score can reject malformed output but cannot establish scientific correctness. The synthetic assertions cover only the facts deliberately planted in that fixture. Manual evidence review remains required.

## JSON contract changes

Validate exports with `--json`. The validator enforces the bundled Schema plus cross-field rules such as unique claim IDs, honest full-read status, and located evidence for strong/moderate support. Treat incompatible field or enum changes as breaking changes; update the Schema identifier, examples, prompts, tests, and changelog together.

## Style

- Prefer direct, testable instructions.
- Use “not specified” rather than guessing.
- Avoid claims that the workflow eliminates hallucination or guarantees correctness.
- Keep product-specific UI instructions in docs, not in the core evidence rules.
- Do not silently weaken coverage disclosure, location requirements, or claim boundaries to shorten a prompt.

By contributing, you agree that your contribution is licensed under the repository's MIT License and that you have the right to submit it.
