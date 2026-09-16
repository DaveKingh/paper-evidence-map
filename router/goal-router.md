# Goal Router

Infer the user's immediate research goal before choosing an analysis workflow. Prefer the narrowest interpretation that answers the request without losing necessary evidence.

| User intent | Primary lenses | Typical depth |
|---|---|---|
| “What is this paper about?” | Contribution | Scan |
| “Take a look at this paper.” | Relevance + Contribution | Triage |
| “Is this worth reading for me?” | Relevance + Contribution | Triage |
| “I am mainly looking for new research ideas—is this worth reading?” | Relevance + Contribution + Gap + Idea | Triage -> Targeted as needed |
| “Can this paper help me generate ideas?” | Relevance + Gap + Idea | Triage -> Targeted |
| “How does this method/module work?” | Method | Targeted |
| “Why did they choose X?” | Method + Experiment | Targeted |
| “Does Table/Figure X support this claim?” | Evidence + Critical | Targeted -> Audit |
| “Read this paper deeply.” | Contribution + Method + Experiment + Evidence | Deep |
| “Audit/check the paper strictly.” | Evidence + Critical | Audit |
| “What research gaps are here?” | Gap + Evidence + Critical | Targeted -> Audit as needed |
| “I need to present this paper.” | Contribution + Method + Experiment + Presentation | Targeted or Deep |
| “What do I need to learn first?” | Learning + Method | Triage or Targeted |

Depth controls evidence-inspection breadth; the active lenses and user goal control the analysis and final answer shape. In particular, a Presentation request may need Deep evidence coverage without requiring the full Deep evidence-map output.

## Goal-relative reading value

“Worth reading?” is incomplete without a purpose. Use the user's explicit current purpose or a stable purpose already established in the conversation. If the conversation establishes that the user is reading papers mainly to find ideas, gaps, topics, or research directions, a later short question such as “is this worth reading?” inherits that purpose and must activate Gap / Idea as part of Triage. Do not force the user to restate the goal in every turn.

If no purpose is known, perform ordinary Relevance + Contribution Triage. Do not invent personalized relevance: mark it cannot judge, state the two or three reading purposes for which the paper appears most useful, and complete the remaining Triage core. Ask a clarifying question only when different plausible purposes would materially change the evidence inspected or the decision.

## Multi-paper session control

Treat multiple papers as a source/session-control concern, not a new depth, lens, or schema.

- **Session Goal** carries a stable reading purpose across turns in the same chat.
- **Active Paper** is the paper analyzed now; default to the newest explicitly uploaded accessible paper.
- **Paper Set** contains the still-relevant current-chat papers under stable S1/S2... IDs.
- **Comparison Set** is created only when the user explicitly requests comparison, synthesis, commonalities/differences, or a shared cross-paper gap. Do not infer it merely because several papers are present.

By default, isolate each paper's internal evidence. Only the Active Paper and its clearly linked official supplement can support what that paper reports or claims; other papers must be explicitly labeled comparison/external sources and cannot repair missing reporting. Resolve “this paper,” “the previous paper,” and title-based references from context. Interpret “these papers” as a Comparison Set only when that set is uniquely recoverable. Ask only when unresolved provenance would materially change the answer.

For cross-paper work, bind every Paper fact and Author interpretation to its source. Analyst judgment may synthesize across papers only with the evidence sources and boundaries stated. Idea-oriented comparison preserves the external-novelty rule: novelty remains unchecked until an actual literature search is performed.

## Ambiguous requests

When the user uploads a paper without specifying a goal or says only “take a look,” “help me read this,” or “what do you think?”, do not use Scan and do not launch a full evidence map. Perform a short Triage that states personalized relevance cannot yet be judged, identifies the two or three purposes for which the paper appears useful, summarizes its contribution, prioritizes what to read first and what can wait, and gives one best next action. Do not search for Candidate Gaps or Ideas merely to fill the Triage; surface them only when research-idea exploration is part of the goal or a materially relevant hook appears naturally in already inspected evidence.

Reserve Scan for explicit orientation requests such as “what is this paper about?”, “give me a simple summary,” or “quick overview.”

When the user's goal is partially known, infer the likely lens from the current conversation. Ask a clarifying question only when different interpretations would materially change what evidence must be inspected.

## Dynamic rerouting

A reading session is not a fixed pipeline. New observations can activate another lens.

Examples:

- A method question reveals an unsupported causal explanation -> activate Critical.
- A zero-shot table and fine-tuning table expose an unexplained model-selection choice -> register a Candidate Gap and activate Gap/Idea when that issue is material to the current goal.
- An apparent idea depends on whether a comparison is fair -> activate Evidence before promoting the idea.

Do not activate unrelated lenses simply for completeness.
