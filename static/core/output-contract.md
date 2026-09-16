# Adaptive Output Contract

Output size and structure follow the user's goal and selected reading depth. Depth controls how broadly evidence is inspected; the active goal/lens controls what is ultimately shown. Internal traceability structures do not need to be exposed verbatim.

## Scan

Return only orientation: what the paper is about, its central contribution, and preliminary relevance to the user's current goal when a goal is known. Do not imply that detailed experimental support has been verified.

## Triage

Reading value is goal-relative. Prefer this compact core structure:

1. Relevance to the user's current goal: high / medium / low / cannot judge, with the goal and reasons stated. Relevance is not equivalent to deep-read value, a research gap, or a recommended research direction.
2. What the paper contributes.
3. What to read first: prioritized sections, figures, tables, or modules.
4. What can remain unread for now, when defensible.
5. One recommended next action.

Then apply a **goal-conditioned extension**. If the explicit request or current conversation establishes that the user's purpose includes finding ideas, gaps, topics, or research directions, research leverage is required: inspect enough paper-internal evidence to decide whether a meaningful hook exists, and report a Candidate Gap / Candidate Idea when justified. If the purpose is presentation, learning, benchmark selection, experiment understanding, or another specific goal, add only the judgments needed for that purpose.

If research exploration is not part of the goal and no material research hook emerges naturally, do not activate Gap/Idea or expand scope just to fill the output template. Conversely, when idea-seeking is the established goal, do not omit research leverage merely because the latest utterance is only “is this worth reading?”.

For idea-oriented Triage, stop after deciding whether a research hook is worth pursuing. If none is sufficiently supported, say so. If one exists, give its paper evidence and the highest-value next check. Do not automatically continue into full Gap Mining, Audit, or external novelty search.

Do not append a full experiment inventory or claim matrix unless needed to justify the triage decision.

## Targeted

Answer the exact question. Include the relevant method/evidence chain, source locators, uncertainty, and only the surrounding context needed to avoid a misleading answer.

## Deep

Cover the major source/coverage, research question, method, experiment, consequential claim-evidence-boundary relations, consistency issues, unknowns, and prioritized checks needed for comprehensive understanding. Deep is broad but still Minimum-Sufficient: do not mechanically inspect or display every table, experiment, or internal object when it cannot materially affect the comprehensive understanding requested.

If Deep is selected under Presentation, Learning, or another goal-specific lens, use Deep to support evidence coverage but shape the final answer for that goal. Do not emit the full evidence-map structure unless the user asks for it or it is itself the requested deliverable.

## Audit

Re-open decisive evidence, log what was re-inspected, record counterevidence/alternative explanations, and classify each consequential claim as retain / narrow / do not accept yet / cannot judge with a defensible rewritten boundary.

## Idea and gap status

- **Observation** — something notable in the paper.
- **Candidate Gap** — a traceable possible gap. Internally keep `origin` (explicit/inferred), internal `gap_status`, and external `novelty_status` separate.
- **Candidate Idea** — a testable direction derived from a Candidate Gap, not automatically a novel research contribution.
- **Research Idea** — use only after the required internal gap support and the novelty/feasibility checks needed by the intended claim.

The raw status fields are primarily for traceability. In ordinary answers, express maturity in natural language unless the user asks for structured state, an audit/export requires it, or the fields materially reduce ambiguity.

Never collapse gap maturity and novelty into a single `Candidate -> Verified -> Novel` ladder. External novelty remains unchecked until literature is actually searched, and “no close prior found” within a search scope is not proof of absence.

## Final check

Before responding, verify that every consequential statement is necessary for the user's current goal, evidence-grounded at the selected depth, and no broader than the inspected evidence supports. Apply the Minimum-Sufficient Rule and stop when sufficient.
