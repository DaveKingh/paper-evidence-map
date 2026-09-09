# Known issues

## Current-chat attachment can lose priority

In one live ChatGPT Project test on 2026-09-09, a new chat received a newly uploaded paper and the user sent only `Round 1`, but the source ledger selected an older Project file. The same chat recovered after the user explicitly named the newly uploaded PDF as S1. This is an observed, product-dependent failure—not evidence that every account or run behaves the same way.

Version 0.1.1 adds an explicit current-chat attachment-precedence rule, a recovery trigger, and the manual fixture in [`examples/current-chat-precedence/`](../examples/current-chat-precedence/). Because the offline validator cannot control ChatGPT's attachment routing, do not call this fixed until repeated live runs pass.

Recovery trigger:

```text
Use <paper filename>, which I just uploaded in this chat, as S1. Ignore files from other chats and older Project files, then rerun Round 1.
```

Chinese:

```text
请以我本对话刚刚上传的 <论文文件名> 作为 S1，忽略其他聊天和 Project 历史文件，重新执行第一轮。
```

## Full reports can be long

Live tests of the full instructions have produced reports hundreds of lines long. The checks can be useful, but length is not evidence of quality. Use the compact prompt for the shorter Round 1/2 core, or use `Focus: <question>` after the initial map. A future default-short-output change needs repeated comparison tests so that brevity does not hide missed evidence.
