# Quickstart

## Use it in ChatGPT (recommended)

1. Open the [full adaptive prompt](../prompts/en/project-instructions.md), or use the [compact adaptive prompt](../prompts/en/project-instructions-compact.md) when you want fewer persistent instructions.
2. Create a ChatGPT Project such as **Paper Evidence Map**.
3. Open Project settings and paste the complete prompt into Project instructions.
4. Start one chat per paper. Upload the primary paper and any clearly linked supplement.
5. Ask your real question directly. You do **not** need to start with `Round 1`.

Examples:

```text
What is this paper about?
Is it worth reading for my research direction?
Explain Section 3.2 and the role of Module C.
Does Table 4 really support the robustness claim?
Can this paper give me a research idea?
I need to present this tomorrow — what should I focus on?
```

The workflow will infer the minimum useful depth:

```text
Scan → Triage → Targeted → Deep → Audit
```

It stops once the current goal is satisfied unless more evidence is necessary.

## Legacy commands still work

```text
Round 1  → Deep evidence-map pass
Round 2  → Audit the consequential claims
Focus: X → Targeted reading
```

Use these when you deliberately want a known reproducible path rather than automatic routing.

## Verify with the included evidence fixture

To test the Deep evidence-map path:

1. Upload [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf).
2. Send `Round 1`.
3. Compare the response with [`expected-findings.md`](../examples/synthetic/expected-findings.md).
4. Score it using the [evidence evaluation rubric](evaluation.md).
5. Save the response and run:

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

Passing the script means expected structural signals and deterministic fixture findings were detected. It does not certify all scientific judgments.

## Verify adaptive routing

Use the same synthetic paper but ask different questions in fresh chats. See [`examples/adaptive-routing/`](../examples/adaptive-routing/README.md) and the [adaptive routing evaluation](evaluation-adaptive.md).

Validate the routing fixture definition first:

```bash
python scripts/check_adaptive_routes.py
```

Then run the R1–R7 cases under the same model/mode/date and record routing failures such as `OVERREAD`, `UNDERREAD`, `MISROUTE`, `NO_STOP`, `EVIDENCE_BYPASS`, or `IDEA_OVERPROMOTION`.

## Source selection check

Confirm that the active source is the paper uploaded in the current chat. If an older Project file is selected, use the [S1 recovery trigger](../prompts/en/chat-triggers.md).

Read access limits before trusting any substantive verdict. Attachment visibility alone does not prove that decisive tables, figures, or appendices were actually inspected.

## Use without a Project

Paste the complete Project prompt at the start of a normal chat, then upload the paper and ask your question. You must paste the instructions again in each new chat.

## Suggested organization

- one Project per broad field or research program;
- one chat per paper;
- supplements in the same paper chat;
- use natural-language goals for most work;
- use `Round 1` / `Round 2` when you intentionally want Deep/Audit reproducibility;
- use a separate comparison chat after individual papers have been inspected enough for the comparison goal.
