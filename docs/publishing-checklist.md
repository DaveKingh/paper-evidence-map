# Publishing checklist

## Identity and metadata

- [ ] Choose the final repository owner and confirm the name `paper-evidence-map`.
- [ ] Replace every `DaveKingh` value (`python scripts/validate.py` lists them).
- [ ] Replace the generic copyright holder in `LICENSE` if you want a personal or organization name.
- [ ] Update `CITATION.cff` authors and repository URL.
- [ ] Use the description and topics in `docs/launch-plan.md`.
- [ ] Add the social preview image in GitHub repository settings.
- [ ] Follow the Chinese step-by-step [publishing guide](publish-to-github.zh-CN.md) if useful.

## Product proof

- [ ] Run the synthetic case at least three times in a fresh Project.
- [ ] Record mode/model, date, rubric score, misses, and fabricated locators.
- [ ] Confirm all required findings can be found by at least one fresh tester without coaching.
- [ ] Publish known limitations next to results.

## Repository settings

- [ ] Set the default branch to `main`.
- [ ] Enable Issues and Discussions.
- [ ] Add branch protection requiring the validation workflow.
- [ ] Enable secret scanning and dependency alerts where available.
- [ ] Create release `v0.1.0` from `docs/releases/v0.1.0.md`.
- [ ] Pin the failure-case contribution issue.

## License choice

MIT is used here because it is familiar, permissive, and simple for code, prompts, and documentation in one small repository. If you require attribution for prompt reuse or want different terms for content and code, obtain legal advice before replacing it with a dual-license approach.

