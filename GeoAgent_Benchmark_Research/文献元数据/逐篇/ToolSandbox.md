<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# ToolSandbox：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities |
| 仓库短名称 | ToolSandbox |
| 实际 Benchmark 名称 | ToolSandbox |
| 年份与平台 | 2025；Findings of NAACL 2025, pp1160–1183 |
| 原文网址 | [官方原文](https://aclanthology.org/2025.findings-naacl.65/) |
| 唯一主类别 | E |
| 阅读优先级 | P1 |
| 阅读优先级理由 | 借鉴不锁定逐条动作的中间状态门、DAG依赖与禁止行为检查。 |
| 分类理由 | 有状态对话工具基准用milestone/minefield表示必须/禁止事件，主要评价通用Agent而非审计Benchmark自身。 |
| 研究用途 | 相关工作：借鉴不锁定逐条动作的中间状态门、DAG依赖与禁止行为检查。 |
| 辅助标签 | 状态验证；部分得分；里程碑；通用工具调用；用户模拟 |
| 主要测量对象 | 工具状态依赖、用户交互、目标里程碑与过程合规 |
| 评价机制 | milestone相似度0–1与DAG时序匹配、minefield惩罚；模型/场景分层 |
| Ground Truth 类型 | 人工里程碑/禁区定义、数据库状态与对话证据 |
| 实证审计可行性 | RU |
| 可行性依据 | 尚未核查任务、GT、评价器与必要环境的完整可用链，不凭论文公开声明评级 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要p1；系统§2 pp3–5；实验§4 pp6–8；局限§7 p10；A.7 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §2.3里程碑和minefield；A.7相似度；§4用户模拟器误差是否影响分数；§7人工成本。 |
| 局限与研究边界 | 作者明确mandatory milestones编制依赖专家且难扩展，用户模拟仍有幻觉/指令偏离。 |
| 归档英文页数 | 24 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/ToolSandbox](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 其他中文稿及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://aclanthology.org/2025.findings-naacl.65/)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/original.pdf) |
| 图表与原页 | [图表/原页1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E5%8E%9F%E7%94%9F%E5%9B%BE%E5%83%8F_%E6%8F%90%E5%8F%96%E7%B4%A2%E5%BC%95.md) · [图表/原页2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95_%E5%8E%9F%E5%A7%8B%E6%88%AA%E5%9B%BE.md) · [图表/原页3](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/%E5%9B%BE%E8%A1%A8%E9%A2%98%E5%90%8D_%E4%B8%AD%E8%8B%B1%E5%AF%B9%E7%85%A7.md) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/README_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/ToolSandbox/original.pdf) |

## 原文核验与研究判断

论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；测量对象字段概括评价操作，不把局部得分外推为完整地学能力。

研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。

## 实证条件分项检查

| 条件 | 实际核查状态 |
|---|---|
| 任务集 | 未核查 |
| GT | 未核查 |
| 参考轨迹 | 未核查 |
| 输出产物 | 未核查 |
| 评价器源码 | 未核查 |
| 执行环境 | 未核查 |
| API依赖 | 未核查 |
| 固定轨迹重复评分 | 未核查 |
| 对照样本构造 | 未核查 |
| 独立人工核验 | 未核查 |

## 开源证据阶段

| 阶段 | 状态 |
|---|---|
| 1 作者声明 | 原文给出资源入口，未独立确认所有资产可用 |
| 2 提供链接 | https://github.com/apple/ToolSandbox |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# ToolSandbox：面向大语言模型工具使用能力的有状态、对话式、交互式评估基准

**英文题名**：*ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities*  
**作者**：Jiarui Lu、Thomas Holleis、Yizhe Zhang、Bernhard Aumayer、Feng Nan、Felix Bai、Shuang Ma、Shen Ma、Mengyu Li、Guoli Yin、Zirui Wang、Ruoming Pang  
**发表**：Findings of NAACL 2025，论文页码 1160–1183（PDF 共 24 页）  
**项目地址**：https://github.com/apple/ToolSandbox

> **译文范围声明**：摘要及主要研究章节为中文译文或紧贴原文的分节译述；长篇技术附录、示例对话和参考文献尚未逐行翻译。全文英文内容见 `英文原文_逐页完整提取.md`，所有原稿页面见 `source_pages/`。保留代码、参数名与模型名原文，以维护可复现性。

## 摘要（中文翻译）

大型语言模型（LLM）的最新进展激发了人们对使用工具辅助 LLM 解决现实世界问题的研究兴趣，这也要求研究者对模型的工具使用能力进行全面评价。既有研究往往仅评估基于无状态 Web 服务（RESTful API）的单轮用户请求，或基于预先收集、与当前策略无关的离线对话轨迹。与之不同，**ToolSandbox** 引入有状态工具执行、工具之间隐含的状态依赖、支持基于当前策略开展对话评估的内置用户模拟器，以及能够在任意交互轨迹上动态评价中间和最终里程碑的策略。实验表明，开源模型与专有模型之间存在明显的性能差距；与此同时，ToolSandbox 定义的状态依赖（State Dependency）、规范化（Canonicalization）和信息不足（Insufficient Information）等复杂任务，即使对性能最强的模型也仍具有挑战性。这些结果为理解 LLM 的工具使用能力提供了新认识。

## 1 引言

大语言模型的进步使它们能够作为自主智能体观察环境、理解自然语言目标，并调用现实世界的 API 完成复杂任务。与传统对话状态跟踪中要求模型按照预定义本体显式产生对话状态和动作不同，工具调用智能体往往直接依据观察生成工具调用，在内部隐式维护对话状态和世界状态。因此，**工具之间的状态关联、持续多轮对话和执行中的不确定性**构成了评价系统必须面对的问题。

许多工具调用基准依赖无状态服务或单轮、无歧义的请求。即使能够修改环境状态，也未必考察工具之间的隐式依赖
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
