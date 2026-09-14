# Depth Router

Choose the minimum reading depth that can answer the user's current question reliably.

## D0 — Scan

Use when the user only needs orientation. Inspect enough primary material to identify the problem, contribution, and paper type. Do not claim detailed experimental support.

## D1 — Triage

Use by default for relevance and “worth reading?” questions. Determine:

- fit to the user's stated goal;
- the paper's likely knowledge or research value;
- the highest-value sections/evidence objects to inspect next;
- candidate gaps or idea hooks, if visible;
- what can safely remain unread for now.

Triage is a decision aid, not a miniature full review.

## D2 — Targeted

Use for a specific method, module, experiment, table, claim, or research question. Inspect the local evidence plus enough surrounding Methods/Results context to avoid a misleading answer.

## D3 — Deep

Use when the user explicitly wants comprehensive understanding or when a high-stakes synthesis requires it. Reconstruct the method, experiments, major claims, evidence links, unknowns, and boundaries. Existing Round 1 evidence rules apply.

## D4 — Audit

Use for skeptical re-checking. Re-open decisive primary evidence, search for counterevidence and alternative explanations, check design/statistical/external-validity risks, and narrow or withdraw claims as needed. Existing Round 2 rules apply.

## Escalation rules

Escalate only when the current depth cannot support the requested conclusion.

- Scan -> Triage when the user needs a decision about relevance or reading value.
- Triage -> Targeted when one section, result, or anomaly determines the decision.
- Targeted -> Deep when the answer depends on interactions across several major sections.
- Deep/Targeted -> Audit when the user asks whether a claim is actually justified or when conflicting evidence appears.

## Stop rule

Once the user's immediate question is answered with adequate evidence and uncertainty, stop. State the best next optional step rather than executing it automatically.
