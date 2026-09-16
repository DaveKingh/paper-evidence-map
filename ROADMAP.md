# Roadmap

## v0.2 — adaptive, evidence-grounded reading

- Replace the fixed universal `Round 1 -> Round 2` entry point with goal-first routing.
- Support Scan, Triage, Targeted, Deep, and Audit reading depths.
- Keep `Round 1` / `Round 2` as backward-compatible Deep/Audit shortcuts.
- Add composable reading lenses for relevance, contribution, method, experiment, evidence, critical review, gaps, ideas, learning, and presentation.
- Use a thin `SKILL.md` + declarative `manifest.yaml` + always-load/on-demand structure.
- Preserve the existing claim → evidence → support → defensible-boundary core.
- Distinguish Candidate Gap / Candidate Idea from stronger Research Idea claims.
- Add routing-specific evaluation for OVERREAD, UNDERREAD, MISROUTE, NO_STOP, EVIDENCE_BYPASS, and IDEA_OVERPROMOTION.
- Run repeated live evaluations on the adaptive routing matrix before release.

## v0.3 — stronger evaluation

- Add at least three synthetic fixtures covering statistics, causal claims, and benchmark leakage.
- Measure inter-rater agreement for the manual rubric.
- Add JSON outputs and deterministic content assertions for every accepted fixture.
- Integrate stable adaptive-routing contract checks into main CI where useful without pretending deterministic checks can score semantic routing quality.

## v0.4 — discipline packs

- Pilot opt-in checklists for empirical ML, clinical studies, and systematic reviews.
- Require a domain maintainer and fixture for each pack.

## v0.5 — portability

- Test and document behavior in additional assistants without weakening the core model-neutral rules.
- Add importable prompt formats only when they can be maintained and evaluated.

## Explicit non-goals

- Claiming to replace peer review or replication.
- Ranking paper quality with a single opaque score.
- Turning PEM into a full end-to-end research/writing platform.
- Uploading or redistributing papers without clear permission.
- Adding dependencies merely to make a simple workflow look like an application.
