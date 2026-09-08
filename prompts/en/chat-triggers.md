# English trigger cheat sheet

Add either `project-instructions.md` (full feature set) or `project-instructions-compact.md` (shorter Round 1/2 core) to ChatGPT Project instructions. Start a new chat for each paper, attach the paper, wait until the attachment is available, and use a short trigger.

```text
Round 1
```

```text
Round 2
```

```text
Focus: How far does the evidence support the cross-dataset generalization claim?
```

```text
Reading status
```

```text
Export JSON
```

JSON export belongs to the full instructions. The full prompt embeds the field contract, so the model does not have to see this repository's schema file. For machine validation, also attach `schemas/evidence-map.schema.json` when practical.

```text
Verify locator: C3
```

```text
Novelty check. Separate paper-internal claims from external findings and report the search date, sources, queries, nearest prior work, and coverage limits.
```

```text
Compare papers: map each one separately, then compare assumptions, data, metrics, key evidence, and claim boundaries for the same research question.
```

If the paper is absent or unreadable, do not ask the model to “try anyway”. Re-upload it, provide OCR, or paste the decisive passages. A correct access-limit response is safer than a plausible evidence map without primary content.
