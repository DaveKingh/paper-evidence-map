# Depth Router

Choose the minimum reading depth that can answer the user's current question reliably. Depth is a control parameter, not a mandatory stage sequence.

Depth primarily controls **how broadly evidence must be inspected**. The active lens and user goal control **what analysis is performed and what is ultimately shown**. A deeper depth does not require exposing every internal analysis object.

## D0 — Scan

Use when the user only needs orientation. Inspect enough primary material to identify the problem, claimed contribution, paper type, and preliminary relevance to the current goal when known. Do not claim detailed experimental support or give a vague overall paper-value rating.

## D1 — Triage

Use by default for relevance and “worth reading?” questions. Reading value is goal-relative. Determine the five core items:

- relevance to the user's current goal, without equating relevance with research value or a research gap;
- what the paper contributes;
- the highest-value sections/evidence objects to inspect next;
- what can safely remain unread for now;
- one best next action.

Then apply a **goal-conditioned extension**. If the explicit request or current conversation establishes that the user is reading to find ideas, gaps, topics, or research directions, research leverage becomes a required Triage question and Gap / Idea lenses should be activated as needed. If the user's purpose is presentation, learning, benchmark selection, or another goal, extend Triage only with judgments directly relevant to that purpose.

Do not search for Candidate Gaps / Ideas merely to fill a template when research exploration is not part of the goal. Conversely, do not omit research leverage when idea-seeking is the established goal simply because the latest user utterance is only “is this worth reading?”.

For idea-oriented Triage, inspect only enough evidence to decide whether a meaningful research hook is worth pursuing. If no sufficiently supported hook appears, say so and stop. If a hook appears, report the Candidate Gap / Candidate Idea, its internal evidence, and the highest-value next check, then stop unless the user asks to continue.

Triage is a decision aid, not a miniature full review.

## D2 — Targeted

Use for a specific method, module, experiment, table, claim, or research question. Inspect the local evidence plus enough surrounding Methods/Results context to avoid a misleading answer.

## D3 — Deep

Use when the user explicitly wants comprehensive understanding or when the requested synthesis genuinely depends on several major sections. Cover the major methods, experiments, consequential claims, evidence links, boundaries, consistency issues, and unknowns that could materially affect that understanding.

Deep is broad by intent but still Minimum-Sufficient: it does not require mechanically inspecting or displaying every table, experiment, or low-value detail. When Deep is used under a presentation, learning, or other goal-specific lens, Deep governs evidence coverage while that lens governs the final output form.

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
