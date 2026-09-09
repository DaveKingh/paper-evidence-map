# Current-chat attachment precedence fixture

This manual fixture reproduces a product-dependent failure observed during a real Project test: a new chat received a newly uploaded paper, but the first `Round 1` response selected an older Project file as S1.

## Run it

1. Add `old-project-paper.md` to a ChatGPT Project, or analyze it in an earlier chat in that Project.
2. Start a completely new chat inside the same Project.
3. Upload only `new-chat-paper.md` to that new chat and wait until the attachment is available.
4. Send only `Round 1`.
5. Score the source ledger against `expected-findings.md` before reading the rest of the answer.

Repeat this case at least three times and preserve every raw response. This behavior depends on the product's attachment and Project context, so the offline validator can verify that the fixture and prompt contract are present but cannot simulate the product itself.
