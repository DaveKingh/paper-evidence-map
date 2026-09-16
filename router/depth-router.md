# Depth Router

Choose the minimum reading depth that can answer the user's current question reliably. Depth is a control parameter, not a mandatory stage sequence.

## D0 — Scan

Use when the user only needs orientation. Inspect enough primary material to identify the problem, claimed contribution, paper type, and preliminary relevance to the current goal when known. Do not claim detailed experimental support or give a vague overall paper-value rating.

## D1 — Triage

Use by default for relevance and “worth reading?” questions. Determine:

- relevance to the user's stated goal, without equating relevance with research value or a research gap;
- what the paper contributes;
- the highest-value sections/evidence objects to inspect next;
- candidate gaps or idea hooks, if visible;
- what can safely remain unread for now.

Triage is a decision aid, not a miniature full review.

## D2 — Targeted

Use for a specific method, module, experiment, table, claim, or research question. Inspect the local evidence plus enough surrounding Methods/Results context to avoid a misleading answer.

## D3 — Deep

Use when the user explicitly wants comprehensive understanding or when the requested synthesis genuinely depends on several major sections. Reconstruct the method, experiments, major claims, evidence links, unknowns, and boundaries. Existing Round 1 evidence rules apply.

## D4 — Audit

Use for skeptical re-checking. Re-open decisive primary evidence, search for counterevidence and alternative explanations, check design/statistical/external-validity risks, and narrow or withdraw claims as needed. Existing Round 2 rules apply.

## Escalation and Materiality Gate

Apply the Minimum-Sufficient Rule. Do not escalate merely because more analysis is possible.

- Scan -> Triage when the user needs a decision about goal-relative relevance or what to read next.
- Triage -> Targeted when one section, result, or anomaly could materially change that decision.
- Targeted -> Deep only when interactions across several major sections are necessary to answer the current question.
- Deep/Targeted -> Audit when skeptical re-checking is requested or conflicting evidence could materially change the current conclusion.

A side finding that cannot materially change the current answer should remain a Candidate Issue rather than triggering deeper reading.

## Sufficiency / STOP Gate

Once the user's immediate question is answered with adequate evidence and uncertainty, stop. State at most the best next optional step rather than executing it automatically.
