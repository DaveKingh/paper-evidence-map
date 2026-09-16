# Changelog

All notable user-facing changes are documented here. This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Adaptive paper-reading router with Scan, Triage, Targeted, Deep, and Audit depths.
- Goal-driven reading lenses for relevance, contribution, method, experiment, evidence, critical review, gaps, ideas, learning, and presentation.
- Manifest-driven Skill structure with thin `SKILL.md`, always-loaded core rules, and on-demand references.
- Candidate Gap / Candidate Idea status model to prevent premature novelty claims.
- Adaptive-routing evaluation guide, machine-readable routing fixture, and deterministic fixture-contract checker.
- Multi-paper session control for stable goals, active-paper selection, paper sets, explicit comparison sets, and paper-internal evidence isolation.

### Changed

- The default unspecified paper-reading request now routes to Triage instead of automatically building a full evidence map.
- `Round 1` / `第一轮` and `Round 2` / `第二轮` remain backward-compatible Deep and Audit shortcuts rather than universal entry points.
- Full and compact English/Chinese Project instructions now use goal-first, minimum-sufficient-depth routing.
- README, quickstart, and methodology documentation now describe adaptive reading as the primary workflow.
- Evaluation now distinguishes evidence-fidelity failures from routing failures such as OVERREAD, UNDERREAD, MISROUTE, NO_STOP, EVIDENCE_BYPASS, IDEA_OVERPROMOTION, and PROVENANCE_LEAK, with R12/R13 multi-paper cases.

### Planned

- Repeated live evaluations across the adaptive routing matrix.
- Deterministic integration of adaptive-routing checks into the main repository validator/CI where appropriate.
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
