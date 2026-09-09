# Quickstart

## Use it in ChatGPT (recommended)

1. Download this repository, or open the [full prompt](../prompts/en/project-instructions.md) on GitHub. Choose the [compact prompt](../prompts/en/project-instructions-compact.md) when you only need the shorter Round 1/2 core.
2. In ChatGPT, create a Project named **Paper Deep Reading**.
3. Open the Project menu → Project settings → Project instructions.
4. Paste the complete prompt and save.
5. Start a separate chat for each paper. Upload the paper and its supplement, then wait until the attachment is available.
6. Send `Round 1`.
7. Confirm that the source ledger names the current-chat paper as S1. If an older Project file is selected, use the [S1 recovery trigger](../prompts/en/chat-triggers.md).
8. Read the “Access limits” and “Unknowns” before trusting the verdict.
9. Send `Round 2` for the claims that affect your decision.

OpenAI's current documentation says a ChatGPT Project keeps related chats, files, instructions, and sources together, and that Project instructions apply across its chats: [Projects and chats](https://learn.chatgpt.com/docs/projects).

## Verify with the included synthetic paper

1. Upload the publication-like [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf). Use [`paper.md`](../examples/synthetic/paper.md) only to audit the fixture source.
2. Send `Round 1`.
3. Compare the response with [`expected-findings.md`](../examples/synthetic/expected-findings.md).
4. Score it using the [evaluation rubric](evaluation.md).
5. Save the response locally and run:

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

Passing the script means the response contains expected structural signals and the eight deterministic synthetic-fixture findings. It does not mean every scientific judgment is correct. Next, use the [adversarial fixture](../examples/adversarial/README.md), [access-limit fixtures](../examples/access-limits/README.md), and [current-chat precedence fixture](../examples/current-chat-precedence/README.md) for safety cases that the basic paper does not isolate.

## Use without a Project

Paste the complete Project prompt at the start of a normal chat, then upload the paper and send `Round 1`. This works, but you must paste the instructions again in each new chat.

## Suggested chat organization

- One Project per broad field or research program.
- One chat per paper.
- A separate comparison chat only after each paper has its own evidence map.
- Keep supplements in the same paper chat.
- Use `Focus: ...` when you care about one decision rather than a full review.
