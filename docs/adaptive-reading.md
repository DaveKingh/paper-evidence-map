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

A useful separation is:

- **Depth** controls how broadly evidence must be inspected.
- **Lens** controls which analytical capability is used.
- **User goal** controls the final answer shape.

Therefore Deep evidence coverage does not require exposing a full evidence-map structure when the user actually wants a presentation, prerequisite explanation, or another goal-specific deliverable.

## Five depths

| Depth | Purpose |
|---|---|
| Scan | Orientation and preliminary goal-relative relevance |
| Triage | Decide relevance to the current goal and what to read next |
| Targeted | Answer one focused question |
| Deep | Build broad evidence coverage for comprehensive understanding |
| Audit | Skeptically re-check decisive claims |

The default for an unspecified paper-reading request is **Triage**, not Deep.

### Triage is goal-conditioned

“Worth reading?” is not a context-free value judgment. PEM interprets it against the user's current purpose. Every Triage still answers a compact core: relevance to the current goal, what the paper contributes, what to read first, what can wait, and one best next action.

On top of that core, Triage activates a **goal-conditioned extension**:

- if the user is reading to find ideas, gaps, topics, or research directions, research leverage becomes a required Triage question and Gap / Idea lenses are activated as needed;
- if the user is preparing a presentation, learning a method, selecting a benchmark, or pursuing another purpose, only the judgments needed for that purpose are added;
- if no research-exploration goal is present and no material research hook emerges naturally, PEM does not expand scope merely to manufacture an idea.

A stable purpose already established in the conversation carries forward. If a researcher says they are currently reading papers mainly to find new ideas, a later “is this one worth reading?” should inherit that purpose instead of requiring it to be restated.

Idea-oriented Triage is still Minimum-Sufficient. It asks only whether there is a paper-supported research hook worth pursuing. If not, it says so and stops. If yes, it surfaces a Candidate Gap / Candidate Idea, its evidence, and the highest-value next check, then stops instead of automatically launching full Gap Mining, Audit, or novelty search.

Deep is broad by intent but remains Minimum-Sufficient: cover all major evidence that could materially change comprehensive understanding, not every table, experiment, or low-value detail mechanically.

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

Users should not need to know these names. Natural-language goals are the primary interface. Additional lenses are activated only when they pass the Materiality Gate or are required by the established goal.

Presentation is a useful example: it can rely on Deep evidence coverage internally while still outputting only the background, method, decisive results, limitations, and likely questions needed by the intended audience.

## Candidate issues, gaps, and ideas

A side anomaly that is not material to the current question can remain a **Candidate Issue** rather than expanding the read.

A **Candidate Gap** keeps independent dimensions internally:

- `origin`: explicit / inferred;
- `gap_status`: candidate / supported / contradicted / unresolved;
- `novelty_status`: unchecked / partially_checked / no_close_prior_found / contradicted / unclear.

For inferred gaps, preserve the observation, evidence references, reasoning chain, alternative explanations, and verification needed. Internal support and external novelty are different questions.

These fields are traceability controls, not mandatory user-facing syntax. Ordinary answers should normally translate them into natural language; exact field names/values are most useful for structured export, audit, precise tracking, or explicit user requests.

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
