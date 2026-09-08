# Quickstart

## Use it in ChatGPT (recommended)

1. Download this repository or open [`prompts/en/project-instructions.md`](../prompts/en/project-instructions.md) on GitHub.
2. In ChatGPT, create a Project named **Paper Deep Reading**.
3. Open the Project menu → Project settings → Project instructions.
4. Paste the complete prompt and save.
5. Start a separate chat for each paper. Upload the paper and its supplement.
6. Send `Round 1`.
7. Read the “Access limits” and “Unknowns” before trusting the verdict.
8. Send `Round 2` for the claims that affect your decision.

OpenAI's current documentation says a ChatGPT Project keeps related chats, files, instructions, and sources together, and that Project instructions apply across its chats: [Projects and chats](https://learn.chatgpt.com/docs/projects).

## Verify with the included synthetic paper

1. Upload [`examples/synthetic/paper.md`](../examples/synthetic/paper.md) as if it were a paper.
2. Send `Round 1`.
3. Compare the response with [`expected-findings.md`](../examples/synthetic/expected-findings.md).
4. Score it using the [evaluation rubric](evaluation.md).
5. Save the response locally and run:

```bash
python scripts/validate.py --response path/to/response.md
```

Passing the script means the response contains expected structural signals. It does not mean every scientific judgment is correct.

## Use without a Project

Paste the complete Project prompt at the start of a normal chat, then upload the paper and send `Round 1`. This works, but you must paste the instructions again in each new chat.

## Suggested chat organization

- One Project per broad field or research program.
- One chat per paper.
- A separate comparison chat only after each paper has its own evidence map.
- Keep supplements in the same paper chat.
- Use `Focus: ...` when you care about one decision rather than a full review.

