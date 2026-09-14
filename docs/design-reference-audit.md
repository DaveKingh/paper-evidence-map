# Design Reference Audit for v0.2

This note records what Paper Evidence Map v0.2 borrows from mature research-skill architectures, what it deliberately does not copy, and what remains PEM-specific.

## Nature Skills: primary architectural reference

The strongest architectural influence is `nature-reader` and the wider Nature Skills static/dynamic pattern.

Borrowed design ideas:

- Keep `SKILL.md` as a short router rather than a complete workflow specification.
- Use a declarative `manifest.yaml` to separate always-loaded core rules from dynamically selected guidance.
- Load deep references only when the current task needs them.
- Treat narrow follow-up questions as local source-grounded tasks instead of rebuilding the entire paper artifact.
- Keep output contracts explicit and reviewable.

Not copied:

- PEM does not default to building a full bilingual paper reader or source-map artifact.
- PEM does not require complete-paper processing before answering a focused research question.
- PEM's primary output is a bounded research judgment, not a reconstructed paper document.

## Academic Research Suite: secondary orchestration and quality reference

ARS contributes a different set of ideas:

- Route by user intent before entering a workflow.
- Do not load an entire suite by default.
- Keep compatibility aliases separate from the underlying workflow semantics.
- Escalate into more rigorous modes only when the research state requires them.
- Treat quality/integrity checks as explicit stages rather than stylistic suggestions.

Not copied:

- PEM is not an end-to-end research/writing/review/experiment platform.
- PEM does not need an agent-team architecture for ordinary single-paper reading.
- PEM does not reproduce ARS's full workflow/mode registry or runtime adapter layer.

## Paper Evidence Map: retained differentiator

PEM keeps its own evidence model as the product core:

`claim -> evidence -> support -> defensible boundary`

v0.2 extends that model without replacing it:

`user goal -> minimum reading depth -> selected lenses -> evidence check -> bounded answer`

For research ideation:

`observation -> Candidate Gap -> targeted evidence check -> Candidate Idea -> external novelty/feasibility checks when needed -> Research Idea`

## Architecture decision

PEM v0.2 therefore uses:

- **Nature Skills** mainly for packaging, progressive loading, manifest-driven structure, and task-local source use.
- **Academic Research Suite** mainly for intent routing, staged rigor, compatibility routing, and quality-gate thinking.
- **Paper Evidence Map v0.1** for provenance discipline, claim/evidence/boundary logic, source isolation, adversarial fixtures, and testability.

The result should remain smaller than ARS and more analytical than Nature Reader.
