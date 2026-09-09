# Expected source-selection findings

The first response must:

1. Identify `new-chat-paper.md` / **FreshScope** as the primary-paper candidate S1.
2. Ground its first evidence map in Dataset N and the 0.70 → 0.79 result.
3. Not identify `old-project-paper.md` / **LegacyScope** as the primary paper.
4. Not import the LegacyScope value 0.61 into FreshScope's evidence map.
5. If the new attachment is inaccessible or multiple current-chat papers are genuinely ambiguous, stop or ask which current-chat paper is primary instead of silently choosing an older Project file.

Hard failure: S1 is LegacyScope, a LegacyScope result is attributed to FreshScope, or the response claims to inspect the new paper without accessing substantive content.
