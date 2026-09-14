# 快速开始

## 在 ChatGPT 中使用（推荐）

1. 打开[中文完整版 Project Instructions](../prompts/zh-CN/project-instructions.md)。
2. 在 ChatGPT 中新建一个 Project，例如 **Paper Evidence Map**。
3. 把完整提示词粘贴到 Project instructions。
4. 每篇论文使用一个聊天，上传正文 PDF 和关系明确的补充材料。
5. 直接问你的真实问题。**不需要每篇论文都从“第一轮”开始。**

例如：

```text
这篇论文适不适合我读？我现在主要想找自动驾驶场景挖掘相关方向。
```

```text
我只关心 Retrieval 模块，解释它怎么工作，以及作者用什么证据证明它有效。
```

```text
Table 4 真的能支持作者说的 robust 吗？
```

```text
这篇论文能不能给我一个候选 research idea？
```

PEM 应自动选择最小必要阅读深度：

```text
Scan -> Triage -> Targeted -> Deep -> Audit
```

只有当前深度不足以可靠回答问题时才继续升级。

## 兼容旧用法

原来的两轮流程继续保留：

- `第一轮` -> Deep Evidence Map；
- `第二轮` -> 严格复核关键主张；
- `聚焦 <问题>` -> Targeted；
- `阅读状态` -> 只报告覆盖范围；
- `Export JSON` -> 按 schema 导出结构化结果。

如果来源清单错误选择了旧 Project 文件而不是当前聊天论文，使用 [S1 恢复指令](../prompts/zh-CN/chat-triggers.md)。

## 验证证据忠实度

1. 上传 [`examples/synthetic/paper.pdf`](../examples/synthetic/paper.pdf)。
2. 发送 `第一轮`。
3. 与 [`expected-findings.md`](../examples/synthetic/expected-findings.md) 对照。
4. 使用 [evaluation.zh-CN.md](evaluation.zh-CN.md) 评分。
5. 可选：保存回答后运行：

```bash
python scripts/validate.py --response path/to/response.md --fixture synthetic
```

Validator 检查确定性结构和 fixture 条件，不代表所有科研判断都一定正确。

## 验证自适应路由

同一篇 synthetic paper，每个问题使用新聊天：

```text
如果我现在主要关注鲁棒分类，这篇值得我读吗？
```

预期：**Triage**，而不是完整 Evidence Map。

```text
Module C 到底是不是必要的？
```

预期：**Targeted**，重点检查 Module C 方法描述和对应 ablation。

```text
这篇能不能给我一个 research idea？
```

预期：优先使用 **Candidate Gap / Candidate Idea**，除非已经实际完成 novelty 检查。

完整 routing test matrix 见 [evaluation-adaptive.md](evaluation-adaptive.md)。

## 推荐组织方式

- 一个大研究方向使用一个 Project；
- 一篇论文使用一个聊天；
- 还在判断论文值不值得读时，先问窄问题；
- 确定论文重要后再进入 Deep；
- 真正影响研究判断的主张再使用 Audit；
- 补充材料与正文放在同一个论文聊天，并保持来源关系明确。

## 不使用 Project

也可以在普通聊天开头粘贴完整 Project Instructions，上传论文后直接问问题。每个新聊天都需要重新粘贴。
