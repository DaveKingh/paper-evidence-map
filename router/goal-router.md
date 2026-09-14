# Goal Router

Infer the user's immediate research goal before choosing an analysis workflow. Prefer the narrowest interpretation that answers the request without losing necessary evidence.

| User intent | Primary lenses | Typical depth |
|---|---|---|
| “What is this paper about?” | Contribution | Scan |
| “Is this worth reading for me?” | Relevance + Contribution | Triage |
| “Can this paper help me generate ideas?” | Relevance + Gap + Idea | Triage -> Targeted |
| “How does this method/module work?” | Method | Targeted |
| “Why did they choose X?” | Method + Experiment | Targeted |
| “Does Table/Figure X support this claim?” | Evidence + Critical | Targeted -> Audit |
| “Read this paper deeply.” | Contribution + Method + Experiment + Evidence | Deep |
| “Audit/check the paper strictly.” | Evidence + Critical | Audit |
| “What research gaps are here?” | Gap + Evidence + Critical | Targeted -> Audit as needed |
| “I need to present this paper.” | Contribution + Method + Experiment + Presentation | Targeted or Deep |
| “What do I need to learn first?” | Learning + Method | Triage or Targeted |

## Ambiguous requests

When the user uploads a paper without specifying a goal, do not launch a full evidence map. Perform a short Triage that explains what the paper is, what it appears useful for, and the most valuable next reading paths.

When the user's goal is partially known, infer the likely lens from the current conversation. Ask a clarifying question only when different interpretations would materially change what evidence must be inspected.

## Dynamic rerouting

A reading session is not a fixed pipeline. New observations can activate another lens.

Examples:

- A method question reveals an unsupported causal explanation -> activate Critical.
- A zero-shot table and fine-tuning table expose an unexplained model-selection choice -> register a Candidate Gap and activate Gap/Idea.
- An apparent idea depends on whether a comparison is fair -> activate Evidence before promoting the idea.

Do not activate unrelated lenses simply for completeness.
