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

## The model

```text
paper + user goal
       |
       v
  source/access gate
       |
       v
    goal router
       |
       v
   depth router
       |
       v
 select reading lenses
       |
       v
 inspect only necessary evidence
       |
       v
 answer current question
       |
       +--> stop when sufficient
       |
       +--> escalate only if a decisive uncertainty remains
```

## Five depths

| Depth | Purpose |
|---|---|
| Scan | Orientation |
| Triage | Decide relevance and reading value |
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

Users should not need to know these names. Natural-language goals are the primary interface.

## Candidate gaps and ideas

Interesting observations may appear before a full paper audit. The workflow may therefore surface a **Candidate Gap** or **Candidate Idea** early, but must not present it as a validated research opportunity.

A useful progression is:

```text
observation
  -> candidate gap
  -> targeted evidence check
  -> candidate idea
  -> external novelty / feasibility checks when needed
  -> research idea
```

This preserves creative flexibility without confusing an interesting anomaly with established novelty.

## Relationship to Round 1 and Round 2

Round 1 and Round 2 remain available for reproducibility and backward compatibility:

- Round 1 maps to a Deep evidence-map pass.
- Round 2 maps to an Audit pass over consequential claims.

They are optional tools rather than the required entrance to every reading session.

## Three design rules

1. **No user need -> no analysis.**
2. **No evidence -> no strong claim.**
3. **No verified gap -> no strong research idea.**

The first rule controls scope, the second controls scientific support, and the third controls idea quality.

## Test the router, not just the evidence map

Adaptive reading adds failure modes that v0.1 could not measure:

- `OVERREAD`
- `UNDERREAD`
- `MISROUTE`
- `NO_STOP`
- `EVIDENCE_BYPASS`
- `IDEA_OVERPROMOTION`

Use [`examples/adaptive-routing/`](../examples/adaptive-routing/README.md) and [`docs/evaluation-adaptive.md`](evaluation-adaptive.md) for live routing tests.

The fixture contract itself can be checked with:

```bash
python scripts/check_adaptive_routes.py
```

That deterministic script checks only that the evaluation matrix is well formed. It does not claim to judge semantic routing quality automatically.
