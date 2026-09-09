## What changed

<!-- One focused description. -->

## Why it improves evidence fidelity or usability

<!-- Link the failure mode or issue. -->

## Verification

- [ ] `python -m unittest discover -s scripts/tests -v`
- [ ] `python scripts/build_fixture_pdf.py --check`
- [ ] `python scripts/validate.py`
- [ ] `python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic`
- [ ] `python scripts/validate.py --json examples/synthetic/expected-output.json --fixture synthetic`
- [ ] Behavior changes include a fixture or explain why one is not applicable.
- [ ] Prompt changes include at least three before/after runs with model/mode and date.
- [ ] All runs and known regressions are reported, not only the best result.
- [ ] JSON-contract changes update the Schema, prompts, examples, tests, and changelog together.
- [ ] `CHANGELOG.md` is updated for user-visible changes.
- [ ] No confidential, identifying, restricted, or non-redistributable content is included.

## Results and limitations

<!-- Scores, misses, fabricated locators, and unresolved tradeoffs. -->
