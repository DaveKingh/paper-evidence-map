# Gap Lens

Use to represent a traceable possible gap without overstating maturity or novelty.

Keep independent internal dimensions:

- `origin`: explicit / inferred
- `gap_status`: candidate / supported / contradicted / unresolved
- `novelty_status`: unchecked / partially_checked / no_close_prior_found / contradicted / unclear

For an inferred gap preserve:

`Observation + Evidence refs + Reasoning chain + Alternative explanations + Verification needed`

These fields are primarily traceability controls. In ordinary user-facing answers, translate them into natural language unless structured status is requested, an audit/export requires the exact fields, or showing them materially reduces ambiguity.

A missing experiment alone is not a publishable gap. Internal support and external novelty are separate questions. “No close prior found” within a documented search scope is not proof of absence.
