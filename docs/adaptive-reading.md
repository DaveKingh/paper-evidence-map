# Adaptive Reading Model

Paper Evidence Map v0.2 shifts from a fixed two-round entry point to goal-directed, adaptive reading.

The evidence-first core remains unchanged: consequential claims must be grounded in accessible primary-paper evidence, locators must be real, author interpretation must be separated from paper facts, and conclusions must be narrowed to what the evidence can defend.

What changes is **when** those tools are used.

## Why adaptive reading

A researcher often does not know whether a paper deserves a full deep read. Common first questions are narrower:

- Is this paper relevant to my current problem?
- Does it contain knowledge I need?
- Is there an interesting research hook here?
- Which section should I read first?
- I only care about this method or table—what does it mean?

Running a complete evidence map before answering these questions creates unnecessary reading and output.

## The control model

```text
paper + user goal
       |
       v
   Access Gate
       |
       v
 Goal / Depth Router
       |
       v
Minimum-Sufficient Reading
 + required lenses
       |
       v
    Evidence
       |
       +-- side finding --> Materiality Gate
       |                    | yes: minimum necessary check, then return
       |                    | no: Candidate Issue, do not expand
       |
       v
Sufficiency / STOP Gate
       | no: continue minimum necessary reading
       | yes
       v
     Answer
```

The three gates answer different questions:

- **Access Gate:** is enough primary evidence accessible for the requested conclusion?
- **Materiality Gate:** could a newly discovered issue materially change the current answer or next decision?
- **Sufficiency / STOP Gate:** is the current goal already answered reliably enough to stop?

D0–D4 and lenses are control parameters/capabilities selected inside this architecture, not mandatory stages in a fixed pipeline.

## Five depths

| Depth | Purpose |
|---|---|
| Scan | Orientation and preliminary goal-relative relevance |
| Triage | Decide relevance to the current goal and what to read next |
| Targeted | Answer one focused question |
| Deep | Build a broad evidence map |
| Audit | Skeptically re-check decisive claims |

The default for an unspecified paper-reading request is **Triage**, not Deep.

## Lenses are capabilities, not commands

The router may activate only the capabilities relevant to the current question:

- Relevance
- Contribution
- Method
- Experiment
- Evidence
- Critical
- Gap
- Idea
- Learning
- Presentation

Users should not need to know these names. Natural-language goals are the primary interface. Additional lenses are activated only when they pass the Materiality Gate.

## Candidate issues, gaps, and ideas

A side anomaly that is not material to the current question can remain a **Candidate Issue** rather than expanding the read.

A **Candidate Gap** keeps independent dimensions when structured detail is needed:

- `origin`: explicit / inferred;
- `gap_status`: candidate / supported / contradicted / unresolved;
- `novelty_status`: unchecked / partially_checked / no_close_prior_found / contradicted / unclear.

For inferred gaps, preserve the observation, evidence references, reasoning chain, alternative explanations, and verification needed. Internal support and external novelty are different questions.

A Candidate Gap may produce a **Candidate Idea** before a full-paper audit, but not an automatic novelty claim:

```text
observation
  -> candidate gap
  -> targeted internal evidence check when needed
  -> candidate idea
  -> external novelty / feasibility checks when required
  -> research idea with bounded claims
```

“No close prior found” within a documented search scope is not proof that no prior work exists.

## Relationship to Round 1 and Round 2

Round 1 and Round 2 remain available for reproducibility and backward compatibility:

- Round 1 maps to a Deep evidence-map pass.
- Round 2 maps to an Audit pass over consequential claims.

They are optional tools rather than the required entrance to every reading session.

## Minimum-Sufficient Rule

**Inspect, verify, and output only what is necessary to answer the user's current goal reliably. Stop when sufficient. Expand scope, activate another lens, or increase depth only when a new finding could materially change the current answer.**

Two additional scientific constraints remain:

- **No evidence -> no strong claim.**
- **No sufficiently supported gap -> no strong research idea; external novelty remains a separate status.**

## Test the router, not just the evidence map

Adaptive reading adds failure modes that v0.1 could not measure:

- `OVERREAD`
- `UNDERREAD`
- `MISROUTE`
- `NO_STOP`
- `EVIDENCE_BYPASS`
- `IDEA_OVERPROMOTION`
- `PROVENANCE_LEAK`
- `NOVELTY_OVERCLAIM`

Cross-case invariants also test the Access, Materiality, and Sufficiency gates plus the rule that external evidence cannot repair missing internal evidence.

Use [`examples/adaptive-routing/`](../examples/adaptive-routing/README.md) and [`docs/evaluation-adaptive.md`](evaluation-adaptive.md) for live routing tests.

The fixture contract itself can be checked with:

```bash
python scripts/check_adaptive_routes.py
```

That deterministic script checks only that the evaluation matrix is well formed. It does not claim to judge semantic routing quality automatically.
