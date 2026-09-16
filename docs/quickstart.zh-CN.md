# 快速开始

## 在 ChatGPT 中使用（推荐）

1. 打开 [ChatGPT Project 专用版](../prompts/zh-CN/project-instructions-chatgpt-project.md)；它在 8,000 字符限制内尽量保留完整版规则。其他环境可使用[完整版](../prompts/zh-CN/project-instructions.md)，需要更短指令时使用 [Compact 版](../prompts/zh-CN/project-instructions-compact.md)。
2. 在 ChatGPT 新建一个 Project，例如 **论文证据地图 / Paper Evidence Map**。
3. 打开 Project settings，把 ChatGPT Project 专用版完整粘贴到 Project instructions。
4. 一篇论文一个聊天，上传主论文和关系明确的补充材料。
5. **直接问你真正的问题，不需要先发送“第一轮”。**

例如：

```text
这篇论文主要做什么？
适不适合我现在的研究方向？
解释一下 Sec. 3.2 和 Module C 的作用。
Table 4 真的支持作者的 robustness 结论吗？
这篇能不能给我一些论文 idea？
我明天要汇报，应该重点讲什么？
```

工作流会自动判断最小充分深度：

```text
Scan → Triage → Targeted → Deep → Audit
```

当前目标已经满足时停止；只有可靠回答还需要更多证据时才继续升级。

## 旧命令仍然兼容

```text
第一轮   → Deep 证据地图
第二轮   → Audit 关键结论
聚焦：X  → Targeted 定向阅读
```

当你明确想要一条可重复的固定路径，而不是自动路由时，可以继续使用这些命令。

## 用仓库自带案例验证证据能力

如果要测试 Deep 证据地图路径：

1. 上传 [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf)。
2. 发送 `第一轮`。
3. 与 [`expected-findings.md`](../examples/synthetic/expected-findings.md) 对照。
4. 按[证据评分量表](evaluation.zh-CN.md)评分。
5. 把回答保存成本地 Markdown，再运行：

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

通过脚本表示检测到预期结构信号和确定性夹具发现，不代表所有科研判断都正确。

## 验证自适应路由

使用同一篇 synthetic paper，但在多个全新聊天中分别提出不同问题。参见 [`examples/adaptive-routing/`](../examples/adaptive-routing/README.md) 和[自适应路由评测](evaluation-adaptive.md)。

先检查路由夹具定义：

```bash
python scripts/check_adaptive_routes.py
```

再在相同模型/模式/日期条件下运行 R1–R7，并记录：`OVERREAD`、`UNDERREAD`、`MISROUTE`、`NO_STOP`、`EVIDENCE_BYPASS`、`IDEA_OVERPROMOTION` 等失败类型。

## 检查来源选择

先确认当前主来源确实是本聊天上传的论文。如果错误选择了旧 Project 文件，使用 [S1 恢复指令](../prompts/zh-CN/chat-triggers.md)。

在相信任何实质结论前先看访问限制。出现附件不代表关键表格、图、附录已经真正检查过。

## 不使用 Project

也可以在普通聊天开头粘贴完整提示词，再上传论文并直接提问；缺点是每个新聊天都要重新粘贴。

## 推荐组织方式

- 一个大方向使用一个 Project；
- 一篇论文使用一个聊天；
- 补充材料和正文放在同一个论文聊天；
- 大多数情况直接用自然语言表达目的；
- 明确需要 Deep/Audit 可重复路径时再使用“第一轮/第二轮”；
- 多论文比较前，先分别对每篇论文做到满足比较目标所需的阅读深度。
