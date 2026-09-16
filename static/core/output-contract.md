# Adaptive Output Contract

Output size and structure follow the user's goal and selected reading depth.

## Scan

Return only orientation: what the paper is about, its central contribution, and preliminary relevance to the user's current goal when a goal is known. Do not imply that detailed experimental support has been verified.

## Triage

Prefer this compact structure:

1. Relevance to the user's current goal: high / medium / low / cannot judge, with the goal and reasons stated. Relevance is not equivalent to deep-read value, a research gap, or a recommended research direction.
2. What the paper contributes.
3. What to read first: prioritized sections, figures, tables, or modules.
4. What can remain unread for now, when defensible.
5. Candidate research leverage: preliminary observations, Candidate Gaps, or Candidate Ideas when visible.
6. One recommended next action.

Do not append a full experiment inventory or claim matrix unless needed to justify the triage decision.

## Targeted

Answer the exact question. Include the relevant method/evidence chain, source locators, uncertainty, and only the surrounding context needed to avoid a misleading answer.

## Deep

Use the repository's established evidence-map structure: source/coverage ledger, research question, method map, experiment map, claim-evidence-boundary matrix, consistency issues, unknowns, and prioritized next checks.

## Audit

Re-open decisive evidence, log what was re-inspected, record counterevidence/alternative explanations, and classify each consequential claim as retain / narrow / do not accept yet / cannot judge with a defensible rewritten boundary.

## Idea and gap status

- **Observation** — something notable in the paper.
- **Candidate Gap** — a traceable possible gap. Keep `origin` (explicit/inferred), internal `gap_status`, and external `novelty_status` separate when structured detail is needed.
- **Candidate Idea** — a testable direction derived from a Candidate Gap, not automatically a novel research contribution.
- **Research Idea** — use only after the required internal gap support and the novelty/feasibility checks needed by the intended claim.

Never collapse gap maturity and novelty into a single `Candidate -> Verified -> Novel` ladder. External novelty remains unchecked until literature is actually searched, and “no close prior found” within a search scope is not proof of absence.

## Final check

Before responding, verify that every consequential statement is necessary for the user's current goal, evidence-grounded at the selected depth, and no broader than the inspected evidence supports. Apply the Minimum-Sufficient Rule and stop when sufficient.
