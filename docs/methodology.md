# Methodology

## Core object: the claim–evidence–boundary triple

For every consequential claim, the workflow asks three questions:

1. **Claim** — What exactly is being asserted, and by whom?
2. **Evidence** — What result or method detail bears on it, and where is it?
3. **Boundary** — What is the strongest narrower statement that the evidence can defend?

The third question prevents a common failure: correctly finding a result but repeating a broader conclusion than that result warrants.

## Adaptive reading before full mapping

Paper Evidence Map does not assume that every paper deserves a full evidence map on first contact. It first asks what the user is trying to accomplish, then chooses the minimum reading depth that can answer that goal reliably.

The default depth for an unspecified paper-reading request is **Triage**, not Deep.

| Depth | Purpose |
|---|---|
| Scan | Establish what the paper is about |
| Triage | Decide relevance, reading value, and what to inspect next |
| Targeted | Answer one focused method, experiment, claim, or idea question |
| Deep | Reconstruct the broad method/experiment/claim–evidence map |
| Audit | Re-open decisive evidence and try to falsify or narrow key claims |

The workflow escalates only when the current depth cannot support the requested conclusion. Once the user's current question is answered with adequate evidence and uncertainty, it stops instead of automatically generating additional sections.

## Where Round 1 and Round 2 fit

The historical two-round workflow remains useful, but it is now a **Deep → Audit** path rather than the universal entry point.

- **Round 1 / 第一轮** maps to a Deep pass: reconstruct the paper, expose missing links, and build the broad claim–evidence map.
- **Round 2 / 第二轮** maps to an Audit pass: re-open the most consequential evidence, seek counterevidence and alternative explanations, and narrow or withdraw claims where needed.

Keeping these passes separate still reduces the risk that one long response merely appears skeptical without re-checking decisive evidence. The change in v0.2 is that many real research questions should stop earlier at Triage or Targeted depth.

## Evidence labels

| Label | Meaning | Example |
|---|---|---|
| Paper fact | Explicit and locatable report | “Table 2 reports 0.78 macro-F1.” |
| Author interpretation | Explanation or generalization made by authors | “The authors attribute the gain to Module G.” |
| Analyst judgment | Inference from internal evidence | “The ablation weakens the necessity claim.” |
| Unknown | Missing or inaccessible | “The number of random seeds is not specified.” |

Labels apply to the proposition, not merely to the fact that words appear in a paper. “Table 2 reports 0.78” is a paper fact. “This proves the module is essential” is an author interpretation if made by the authors, even though the sentence itself is locatable. Split a sentence that mixes observation and inference.

## Support levels

- **Strong:** direct, well-matched evidence with appropriate comparisons and uncertainty reporting supports the stated scope.
- **Moderate:** relevant evidence exists but a material limitation remains.
- **Weak:** evidence is indirect, narrow, under-controlled, or inconsistent with the claim's breadth.
- **Cannot judge:** decisive information is missing or inaccessible.

These labels are local to a claim, not an overall paper score. “Weak” means accessible evidence bears on the claim but is mismatched or insufficient; “Cannot judge” means the decisive evidence is unavailable.

## Access and provenance gate

An attachment icon is not evidence that its content was read. Before making substantive claims, the workflow establishes enough source/access context for the selected depth:

- which files are primary papers, supplements, or non-paper context;
- which sections and evidence objects were inspected;
- which present content was not inspected when that distinction matters;
- which content was missing, unreadable, truncated, or OCR-uncertain.

The gate scales with depth. A Triage response does not need an exhaustive whole-paper inventory, but it must still disclose missing decisive material. Deep/Audit passes require a broader source and coverage ledger.

When no substantive primary-paper content is accessible, the correct output is an access-limit notice—not a partly filled analysis inferred from title, filename, memory, or previous answers.

For multiple files, stable source IDs prevent evidence laundering across a paper, supplement, review, and answer key. A locator should identify the source and evidence object, for example `S1, Table 2, row “without C”`. Printed page numbers may be used only when visible; viewer page indexes must be labeled as such.

Within a Project, availability is not the same as selection. The newest accessible paper attached in the current chat takes precedence as the primary `S1` candidate over older Project files and prior analyses. If multiple current-chat papers are plausible, the assistant must ask which one to use. This product-dependent behavior has a [manual regression fixture](../examples/current-chat-precedence/README.md) and a documented [recovery procedure](known-issues.md#the-wrong-project-file-is-selected).

## Claim-local support decision

Ask these questions in order:

1. Is the decisive evidence accessible? If not, **Cannot judge**.
2. Does the cited object contain the reported value, direction, and comparison? If not, withdraw/correct the locator or rate the claim **Weak** when contradictory evidence is visible.
3. Does the design match the exact claim—population, task, intervention, baseline, metric, and time horizon?
4. Are controls and uncertainty adequate for that scope?
5. What is the strongest narrower statement that survives?

A direct descriptive number can be strongly supported as “the paper reports X” while a causal or universal conclusion drawn from the same number remains weak. Support attaches to the wording being judged.

## Candidate gaps and research ideas

Paper Evidence Map may surface useful research leverage before a full-paper audit, but early observations must be typed conservatively.

A paper-internal anomaly or omission becomes a **Candidate Gap** only when it is concrete and traceable to the paper. A missing experiment is not automatically a publishable research gap.

A **Candidate Idea** should preserve this chain:

`observation → candidate gap → research question → hypothesis → minimal experiment → possible contribution → risks`

Promotion to a stronger Research Idea requires enough targeted evidence to establish that the gap is real and, where relevant, external novelty and feasibility checks. This is the basis of the rule: **No verified gap → no strong research idea.**

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
- false claims of full-document coverage;
- over-reading: producing a full audit when a narrow answer would have satisfied the user;
- idea over-promotion: presenting an early anomaly as established novelty.

It does not solve fabricated source data, sophisticated statistical errors, inaccessible content, or field-wide novelty without external evidence.

## Prompt variants and feature boundary

- `project-instructions.md` is the complete adaptive contract. It includes intent/depth routing, provenance controls, Deep/Audit compatibility, gap/idea handling, locator verification, external novelty-search boundaries, comparisons, and self-contained JSON export.
- `project-instructions-compact.md` keeps the adaptive router and highest-value evidence controls with fewer persistent instructions. It intentionally omits JSON export and specialist triggers.

No prompt can guarantee compliant behavior. The prompt is one component of a testable workflow: use known fixtures, score content and routing rather than style, inspect cited locations, and repeat live runs under recorded model/mode/date conditions.

## Why JSON is self-contained

Project instructions may be copied without the rest of this repository. The full prompt therefore embeds the required keys and enums for `Export JSON`. If the schema file is available, it remains the authoritative machine check; if not, the embedded contract prevents the model from guessing fields. Unknown values use `null` or empty arrays rather than invented content.
