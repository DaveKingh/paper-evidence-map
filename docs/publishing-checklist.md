# Publishing checklist

## Identity and metadata

- [ ] Confirm the repository remains `DaveKingh/paper-evidence-map`.
- [ ] Confirm publication-critical URLs contain `DaveKingh`, not `YOUR_USERNAME`.
- [ ] Confirm `LICENSE` and `CITATION.cff` retain `Haochen Yang`.
- [ ] Confirm `CITATION.cff` version/date match the release.
- [ ] Use the description and topics in `docs/launch-plan.md`.
- [ ] Upload [`assets/social-preview.png`](../assets/social-preview.png) in GitHub repository settings.
- [ ] Follow the Chinese step-by-step [publishing guide](publish-to-github.zh-CN.md) if useful.

## Product proof

- [ ] Run the synthetic case at least three times in a fresh Project.
- [ ] Record mode/model, date, rubric score, misses, and fabricated locators.
- [ ] Confirm all required findings can be found by at least one fresh tester without coaching.
- [ ] Publish known limitations next to results.
- [ ] Run A9 at least three times with an older Project file and a newly uploaded current-chat paper; publish every run.

## Clean-download gate

- [ ] Use Python 3.9 or newer and run `python -m unittest discover -s scripts/tests -v`.
- [ ] Run `python scripts/build_fixture_pdf.py --check`.
- [ ] Run `python scripts/validate.py --response examples/synthetic/expected-output.md --fixture synthetic`.
- [ ] Run `python scripts/validate.py --json examples/synthetic/expected-output.json --fixture synthetic`.
- [ ] Run `python scripts/validate.py --strict-publish`; it must pass after owner placeholders are replaced.
- [ ] Test once from a fresh `git clone` and once from GitHub's **Download ZIP**, not from the working copy.
- [ ] Confirm the archive contains `.github/`, `.gitignore`, `paper.pdf`, `expected-output.json`, the Schema, and validator tests.
- [ ] Repeat the gate on at least one case-sensitive system (both CI jobs run on Linux).

The structural score checks output shape. The synthetic assertions check eight planted facts. Neither substitutes for the manual evidence-fidelity rubric.

## Repository settings

- [ ] Set the default branch to `main`.
- [ ] Enable Issues and Discussions.
- [ ] Add branch protection requiring the validation workflow.
- [ ] Enable secret scanning and dependency alerts where available.
- [ ] Keep the existing `v0.1.0` tag and Release unchanged.
- [ ] Create release `v0.1.1` from `docs/releases/v0.1.1.md`.
- [ ] Confirm the release tag points to the exact commit that passed CI.
- [ ] Pin the failure-case contribution issue.

## License choice

MIT is used here because it is familiar, permissive, and simple for code, prompts, and documentation in one small repository. If you require attribution for prompt reuse or want different terms for content and code, obtain legal advice before replacing it with a dual-license approach.
