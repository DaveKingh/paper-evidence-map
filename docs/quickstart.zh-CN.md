# 快速开始

## 在 ChatGPT 中使用（推荐）

1. 下载仓库，或在 GitHub 打开[完整版提示词](../prompts/zh-CN/project-instructions.md)；只需要较短的两轮核心流程时，改用[精简版提示词](../prompts/zh-CN/project-instructions-compact.md)。
2. 在 ChatGPT 中新建一个 Project，命名“论文深度阅读”。
3. 打开 Project 菜单 → Project settings → Project instructions。
4. 粘贴完整提示词并保存。
5. 每篇论文新建一个聊天，上传正文 PDF 和补充材料，并等待附件可用。
6. 发送 `第一轮`。
7. 确认来源清单把当前聊天的论文列为 S1；如果选中了旧 Project 文件，使用 [S1 恢复指令](../prompts/zh-CN/chat-triggers.md)。
8. 先看“访问限制”和“未知项”，再看结论。
9. 对影响决策的关键结论发送 `第二轮`。

OpenAI 当前官方文档说明，ChatGPT Project 会把相关聊天、文件、说明和来源放在一起，Project instructions 会应用于其中的聊天：[Projects and chats](https://learn.chatgpt.com/docs/projects)。

## 用仓库自带案例验证

1. 上传更接近实际使用的 [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf)；只有审阅夹具源码时才打开 [`paper.md`](../examples/synthetic/paper.md)。
2. 发送 `第一轮`。
3. 与 [`expected-findings.md`](../examples/synthetic/expected-findings.md) 对照。
4. 按 [评分量表](evaluation.zh-CN.md) 打分。
5. 把回答保存成本地 Markdown，再运行：

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

通过脚本表示结构信号和合成论文的 8 个确定性必找项齐全，不表示所有科研判断正确。随后可运行[多文件对抗案例](../examples/adversarial/README.md)、[访问限制案例](../examples/access-limits/README.md)和[当前聊天附件优先案例](../examples/current-chat-precedence/README.md)，检查基础论文没有单独覆盖的安全行为。

## 不使用 Project

也可以在普通聊天开头粘贴完整提示词，再上传论文并发送 `第一轮`。缺点是每次新建聊天都要重新粘贴。

## 推荐组织方式

- 一个大方向使用一个 Project；
- 一篇论文使用一个聊天；
- 每篇分别建图后，再新建对比聊天；
- 补充材料与正文放在同一个论文聊天；
- 只关心一个决策时使用 `聚焦：...`。
