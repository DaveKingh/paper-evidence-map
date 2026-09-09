# Methodology

## Core object: the claim–evidence–boundary triple

For every consequential claim, the workflow asks three questions:

1. **Claim** — What exactly is being asserted, and by whom?
2. **Evidence** — What result or method detail bears on it, and where is it?
3. **Boundary** — What is the strongest narrower statement that the evidence can defend?

The third question prevents a common failure: correctly finding a result but repeating a broader conclusion than that result warrants.

## Why two rounds

Round 1 optimizes coverage. It reconstructs the paper and exposes missing links. Round 2 optimizes falsification: it re-opens the most important evidence, seeks alternative explanations, and revises the claim rather than merely adding more prose.

The rounds should be separate because a single long answer can give the appearance of depth without actually re-checking decisive evidence.

## Evidence labels

| Label | Meaning | Example |
|---|---|---|
| Paper fact | Explicit and locatable report | “Table 2 reports 0.78 macro-F1.” |
| Author interpretation | Explanation or generalization made by authors | “The authors attribute the gain to Module G.” |
| Analyst judgment | Inference from internal evidence | “The ablation weakens the necessity claim.” |
| Unknown | Missing or inaccessible | “The number of random seeds is not specified.” |

Labels apply to the proposition, not merely to the fact that words appear in a paper. “Table 2 reports 0.78” is a paper fact. “This proves the module is essential” is an author interpretation if made by the authors, even though the sentence itself is locatable. A response should split a sentence that mixes an observation with an inference.

## Support levels

- **Strong:** direct, well-matched evidence with appropriate comparisons and uncertainty reporting supports the stated scope.
- **Moderate:** relevant evidence exists but a material limitation remains.
- **Weak:** evidence is indirect, narrow, under-controlled, or inconsistent with the claim's breadth.
- **Cannot judge:** decisive information is missing or inaccessible.

These labels are local to a claim. They are not an overall quality ranking.

“Weak” and “Cannot judge” are deliberately different. Use **Weak** when accessible evidence bears on the claim but is indirect, mismatched, poorly controlled, or contradictory. Use **Cannot judge** when the evidence needed to decide is missing or inaccessible. This distinction prevents absence of access from being misreported as negative evidence.

## Access and provenance gate

An attachment icon is not evidence that its content was read. Before making substantive claims, the workflow records:

- which files are primary papers, supplements, or non-paper context;
- which sections and evidence objects were inspected;
- which present content was not inspected;
- which content was missing, unreadable, truncated, or OCR-uncertain.

When no substantive primary-paper content is accessible, the correct output is an access-limit notice—not a partly filled evidence map inferred from the title or a previous answer. With partial access, conclusions must stay inside the visible range.

For multiple files, stable source IDs prevent evidence laundering across a paper, supplement, review, and answer key. A locator should identify the source and the evidence object, for example `S1, Table 2, row “without C”`. Printed page numbers may be used only when visible; viewer page indexes must be labeled as such. A prose reference such as “see Figure 4” does not establish that Figure 4 exists in the supplied content or was inspected.

Within a Project, availability is not the same as selection. The newest accessible paper attached in the current chat takes precedence as the primary `S1` candidate over older Project files and prior analyses. If multiple current-chat papers are plausible, the assistant must ask which one to use. This product-dependent behavior has a [manual regression fixture](../examples/current-chat-precedence/README.md) and a documented [recovery procedure](known-issues.md#the-wrong-project-file-is-selected).

This gate follows the current [official ChatGPT Projects documentation](https://learn.chatgpt.com/docs/projects): projects carry uploaded files and instructions across chats, but the sources needed for a task still have to be uploaded or connected. Product interfaces and limits can change, so the repository offers full and compact instructions without claiming a fixed character limit.

## Claim-local support decision

Ask these questions in order:

1. Is the decisive evidence accessible? If not, **Cannot judge**.
2. Does the cited object contain the reported value, direction, and comparison? If not, withdraw/correct the locator or rate the claim **Weak** when contradictory evidence is visible.
3. Does the design match the exact claim—population, task, intervention, baseline, metric, and time horizon?
4. Are controls and uncertainty adequate for that scope?
5. What is the strongest narrower statement that survives?

A direct descriptive number can be strongly supported as “the paper reports X” while a causal or universal conclusion drawn from the same number remains weak. Support attaches to the wording being judged.

## Threat model

The workflow explicitly addresses:

- abstract and conclusion overstatement;
- result/interpretation conflation;
- unreported details filled in from convention;
- one-condition evidence generalized broadly;
- missing ablations for “essential” modules;
- inconsistent values across text and tables;
- document-embedded prompt injection;
- source mixing between papers, supplements, reviews, and answer keys;
- an older Project file silently replacing the paper attached in the current chat;
- fabricated pages, figures, values, quotations, or citations;
- false claims of full-document coverage.

It does not solve fabricated source data, sophisticated statistical errors, inaccessible content, or field-wide novelty without external evidence.

## Prompt variants and feature boundary

- `project-instructions.md` is the complete contract. It includes Round 1, Round 2, provenance controls, locator verification, external novelty-search boundaries, comparisons, and a self-contained JSON export contract.
- `project-instructions-compact.md` keeps the highest-value Round 1/2 evidence controls with fewer persistent instructions. It intentionally omits JSON export and specialist triggers.

No prompt can guarantee compliant behavior. The prompt is one component of a testable workflow: use a known fixture, score content rather than style, inspect every cited location, and repeat live runs under recorded model/mode/date conditions.

## Why JSON is self-contained

Project instructions may be copied without the rest of this repository. The full prompt therefore embeds the required keys and enums for `Export JSON`. If the schema file is available, it remains the authoritative machine check; if not, the embedded contract prevents the model from having to guess fields. Unknown values use `null` or empty arrays rather than invented content.
