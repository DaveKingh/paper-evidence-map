# Changelog

All notable user-facing changes are documented here. This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned

- Additional discipline-specific evaluation cases.
- Community-submitted anonymized failure cases.

## [0.1.1] - Unreleased

### Added

- Current-chat attachment precedence, recovery triggers, known-issue documentation, and a manual Project-contamination fixture.
- Adversarial multi-file and access-limit fixtures.
- Representative JSON export and Schema-backed cross-field validation.
- Deterministic PDF builder, PDF checks, and 20 validator regression tests.
- Ready-to-upload 1280×640 GitHub social preview.

### Changed

- Structural scoring requires real headings and a claim/evidence table; exact support labels no longer confuse `StrongBase` with `Strong`.
- Markdown validation checks image and HTML targets, repository boundaries, and path case.
- Full and compact bilingual prompts strengthen source isolation, access gates, locator verification, and bounded output.
- CI preserves the required `repository` check and adds a Python 3.9 compatibility job.

### Fixed

- Added a safeguard for observed cases where an older Project file can be selected instead of the paper uploaded in the current chat.

## [0.1.0] - 2026-09-08

### Added

- English and Simplified Chinese Project instructions.
- Two-round evidence-map and skeptical-audit workflow.
- Synthetic paper, expected findings, and representative output.
- Zero-dependency repository and response validator.
- JSON Schema for optional structured exports.
- Bilingual quickstart, methodology, evaluation, and FAQ.
- GitHub issue templates, pull-request template, and CI.
