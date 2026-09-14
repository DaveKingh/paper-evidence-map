# Paper Evidence Map｜论文证据地图

> **不要只总结论文。先读你真正需要的，再判断它究竟证明了什么。**

[English](README.md) · [自适应阅读](docs/adaptive-reading.md) · [快速开始](docs/quickstart.zh-CN.md) · [合成论文挑战](#运行可复现挑战) · [方法说明](docs/methodology.zh-CN.md) · [评测方法](docs/evaluation.zh-CN.md)

Paper Evidence Map（PEM）是一套面向**单篇科研论文**的自适应、证据优先阅读工作流。它不再假设每篇论文都值得一开始就完整深读，而是先判断你**为什么要读这篇论文**，选择最小必要阅读深度，再把重要主张连接到方法、实验、图表、限制和可辩护的结论边界。

核心逻辑：

```text
用户当前目标
    ↓
阅读深度
    ↓
相关论文证据
    ↓
主张 → 证据 → 可辩护边界
    ↓
可选：Gap / Idea 形成
```

PEM 主要面向普通 ChatGPT / Project 使用。核心工作流不要求 API Key，也不绑定某个特定模型。

## 为什么改成自适应阅读

真实科研阅读通常先出现的是这些问题：

- 这篇论文对我现在有没有用？
- 值不值得花时间深入读？
- 我只关心其中一个模块，它到底怎么工作？
- 这个实验为什么这样设计？
- Table 4 真能支撑作者的结论吗？
- 这里有没有可能形成我自己的论文 idea？
- 我明天要汇报，应该重点看什么？

如果每次都先执行完整“第一轮”，会产生大量当前不需要的信息。

PEM v0.2 因此引入五级阅读深度：

| 深度 | 适合什么问题 |
|---|---|
| **Scan** | 这篇论文是干什么的？ |
| **Triage** | 值不值得读 / 和我有没有关系 / 有没有 idea 价值？ |
| **Targeted** | 只解决一个方法、实验、图表、主张问题 |
| **Deep** | 建立较完整 Evidence Map |
| **Audit** | 怀疑式复核关键结论 |

**默认入口是 Triage，而不是 Deep。**

## 三条核心规则

1. **没有用户需要 → 不分析。**
2. **没有证据 → 不下强结论。**
3. **没有核实的 Gap → 不包装成强 Research Idea。**

这意味着：当前问题已经被可靠回答后，PEM 应该停止，而不是自动把整套模板继续输出完。

## 每个 Project 设置一次

如果只是使用 PEM，不需要 clone 仓库。

1. 复制[中文完整版 Project Instructions](prompts/zh-CN/project-instructions.md)；英文用户可用[English version](prompts/en/project-instructions.md)。
2. 粘贴到 ChatGPT Project instructions。
3. 上传论文，然后直接说你的真实问题。

例如：

```text
这篇论文适不适合我读？我现在主要想找自动驾驶场景挖掘方面的研究方向。
```

```text
我只想搞懂作者的 Retrieval 模块，详细解释这部分。
```

```text
为什么作者 Zero-shot 最好的模型不是后面 Fine-tuning 的模型？
```

```text
这个 Table 真的能支持作者说的 broadly robust 吗？
```

```text
这篇论文能不能给我一些候选研究 idea？
```

以后**不需要每篇论文都从“第一轮”开始**。

旧触发词仍然兼容：

| 输入 | 行为 |
|---|---|
| `第一轮` / `Round 1` | Deep Evidence Map |
| `第二轮` / `Round 2` | Skeptical Audit |
| `聚焦 <问题>` | Targeted 阅读 |
| `阅读状态` | 只报告覆盖范围 |
| `Export JSON` | 结构化导出 |

## 原来的证据标准没有被削弱

自适应改变的是**什么时候做哪些分析**，不是降低证据要求。

PEM 仍然要求：

- 来源与访问范围可追踪；
- 区分论文事实 / 作者解释 / 分析判断 / 未知；
- 重要结论尽量给出精确 locator；
- 支持强度针对具体主张；
- 未报告与无法访问必须显式写出；
- 泛化、因果、鲁棒、稳定性、效率等结论必须限制到实验真正支持的范围；
- Audit 时主动寻找反证和替代解释；
- 单篇论文不能证明领域级新颖性。

PEM 最核心的科学对象仍然是：

```text
Claim → Evidence → Boundary
```

详见[方法说明](docs/methodology.zh-CN.md)。

## Candidate Gap 与 Research Idea

PEM 允许你在还没完整深读时先发现有趣异常，但不会马上把它包装成“创新点”。

```text
Observation
   ↓
Candidate Gap
   ↓
定向证据检查
   ↓
Candidate Idea
   ↓
必要时做 Novelty / Feasibility Check
   ↓
Research Idea
```

尤其要注意：

> **作者没有做某个实验，本身不等于 Research Gap。**

## 一个可以核对的例子

仓库内的合成论文故意让正文结论和原始表格冲突：

| 论文怎么说 | 原始证据怎么说 | 可辩护解读 |
|---|---|---|
| “两个数据集都提升 8 个点” | Table 1：A +8，B **只有 +4** | B 上的结论被夸大 |
| “两个模块都必不可少” | Table 2：移除 C 后 **0.78 → 0.78** | C 的必要性没有被证明 |
| “具有广泛鲁棒性” | 只测试一个数据集上的一种扰动强度 | 证据只支持该测试条件 |

可以检查[可上传 PDF](examples/synthetic/paper.pdf)、[Markdown 源文](examples/synthetic/paper.md)、[必找项](examples/synthetic/expected-findings.md)、[参考 Evidence Map](examples/synthetic/expected-output.md) 和 [JSON 参考](examples/synthetic/expected-output.json)。

## 运行可复现挑战

### 证据忠实度测试

上传 [`examples/synthetic/paper.pdf`](examples/synthetic/paper.pdf)，发送：

```text
第一轮
```

再与[预期发现](examples/synthetic/expected-findings.md)和[评测规则](docs/evaluation.zh-CN.md)对比。

### 自适应路由测试

同一篇 synthetic paper，每个问题使用新聊天：

```text
如果我现在主要关注鲁棒分类，这篇值得我读吗？
```

预期：**Triage**，不应该输出完整 Evidence Map。

```text
Module C 到底是不是必要的？
```

预期：**Targeted + Evidence/Critical**，重点检查对应 ablation。

```text
这篇能不能给我一个研究 idea？
```

预期：先输出 Candidate Gap / Candidate Idea，而不是直接声称“这是新颖研究方向”。

因此 PEM v0.2 新增了一个可测试能力：

> **不仅要读得严谨，还要判断当前到底需要读多少。**

## Skill 架构

PEM v0.2 采用薄入口 + manifest + 按需加载：

```text
SKILL.md
   ↓
manifest.yaml
   ├── always-load core
   ├── goal router
   ├── depth router
   ├── on-demand lenses
   └── on-demand references
```

这一工程结构主要参考 Nature Skills 的 progressive loading，同时吸收 Academic Research Suite 的 intent routing 和 staged rigor。哪些内容参考了它们、哪些明确没有照搬，记录在 [design-reference-audit](docs/design-reference-audit.md)。

## PEM 适合什么

| 需求 | 是否适合 |
|---|---|
| 判断一篇论文值不值得读 | **是——核心场景** |
| 搞懂一个方法/模块/实验 | **是——核心场景** |
| 核查论文主张是否被内部证据支持 | **是——核心场景** |
| 找到可追踪的 Candidate Gap / Idea | **是，但显式保留不确定性** |
| 搜索和排序整个领域文献 | 否 |
| 用单篇论文证明领域级 novelty | 否 |
| 替代同行评审或复现实验 | 否 |

Locator 提供的是可追踪性，不代表自动获得真理。重要科研判断仍需要人工核查。

## 仓库结构

```text
paper-evidence-map/
├── SKILL.md
├── manifest.yaml
├── static/core/             # 常驻原则、来源门、输出契约
├── router/                  # Goal / Depth Router
├── lenses/                  # 按需分析能力
├── prompts/                 # 中英文 Project Instructions
├── examples/                # synthetic / adversarial / access fixtures
├── schemas/                 # JSON Schema
├── scripts/validate.py      # deterministic checks
└── docs/                    # methodology / adaptive model / evaluation / design notes
```

## 成熟度

PEM 仍然是早期工作流与测试框架，不是已经验证的科学测量工具。结构检查通过不等于语义阅读正确；Prompt 版本比较应该通过多次真实运行完成。

MIT License，见 [LICENSE](LICENSE)。
