# Quickstart

## Use it in ChatGPT (recommended)

1. Open the [full Project instructions](../prompts/en/project-instructions.md).
2. Create a ChatGPT Project such as **Paper Evidence Map**.
3. Paste the complete prompt into Project instructions.
4. Start one chat per paper and upload the paper plus clearly linked supplements.
5. Ask your real question directly. You do **not** need to start with `Round 1`.

Examples:

```text
Is this paper worth reading for my current research direction?
```

```text
I only care about the retrieval module. Explain how it works and what evidence supports it.
```

```text
Does Table 4 really justify the robustness claim?
```

```text
Can this paper give me a candidate research idea?
```

PEM should choose the minimum useful depth automatically:

```text
Scan -> Triage -> Targeted -> Deep -> Audit
```

It should escalate only when a deeper read is necessary for a reliable answer.

## Legacy shortcuts

The original workflow remains available:

- `Round 1` -> Deep evidence map.
- `Round 2` -> skeptical audit of consequential claims.
- `Focus: <question>` -> targeted reading.
- `Reading status` -> coverage only.
- `Export JSON` -> schema-oriented structured output.

If a source ledger selects an older Project file instead of the current-chat paper, use the [S1 recovery trigger](../prompts/en/chat-triggers.md).

## Verify evidence fidelity

1. Upload [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf).
2. Send `Round 1`.
3. Compare with [`expected-findings.md`](../examples/synthetic/expected-findings.md).
4. Score it with [evaluation.md](evaluation.md).
5. Optionally save the response locally and run:

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

The validator checks deterministic structure and fixture assertions. It does not prove every scientific judgment is correct.

## Verify adaptive routing

Use a fresh chat for each case with the same synthetic paper:

```text
Is this worth reading if I mainly care about robust classification?
```

Expected: **Triage**, not a full evidence map.

```text
Is Module C actually necessary?
```

Expected: **Targeted**, centered on the relevant method description and ablation evidence.

```text
Can this paper give me a research idea?
```

Expected: **Candidate Gap / Candidate Idea** language unless novelty has actually been checked.

Use the full routing matrix in [evaluation-adaptive.md](evaluation-adaptive.md).

## Suggested chat organization

- One Project per broad research area or program.
- One chat per paper.
- Ask narrow questions first when you are still deciding whether the paper is worth deeper reading.
- Use Deep only for papers that deserve comprehensive reconstruction.
- Use Audit when a claim matters enough to re-open decisive evidence skeptically.
- Keep supplements in the same paper chat when their relation is clear.

## Use without a Project

Paste the complete Project instructions at the start of a normal chat, upload the paper, and ask your question normally. You will need to paste the instructions again in each new chat.
