<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# GeoMMBench_GeoMMAgent：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing |
| 仓库短名称 | GeoMMBench_GeoMMAgent |
| 实际 Benchmark 名称 | GeoMMBench |
| 年份与平台 | 2026；CVPR 2026, pp34843–34853 |
| 原文网址 | [官方原文](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_GeoMMBench_and_GeoMMAgent_Toward_Expert-Level_Multimodal_Intelligence_in_Geoscience_and_CVPR_2026_paper.pdf) |
| 唯一主类别 | D |
| 阅读优先级 | P2 |
| 阅读优先级理由 | 研究视觉grounding、地学专业知识与答案格式提取的关系，防止Agent名称引起分类误计。 |
| 分类理由 | GeoMMAgent虽是工具系统，主Benchmark仍以1053专家级多模态选项问答为统一评分对象，保留D。 |
| 研究用途 | 相关工作：研究视觉grounding、地学专业知识与答案格式提取的关系，防止Agent名称引起分类误计。 |
| 辅助标签 | 多模态问答；专家知识；正则匹配；Agent基线；视觉grounding |
| 主要测量对象 | 跨地学/遥感学科、传感器和任务的专家级MCQ解题 |
| 评价机制 | 正则提取选项/数值，无效输出判错；micro-averaged Accuracy；人类专家参照 |
| Ground Truth 类型 | 专家级图片问题、正确选项/数值及val/test划分 |
| 实证审计可行性 | RU |
| 可行性依据 | 尚未核查任务、GT、评价器与必要环境的完整可用链，不凭论文公开声明评级 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要p1；§3 pp2–4；§4 p5；§5 pp6–8；结论p8 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §3专家题构建；§4多Agent作为基线；§5.1正则与micro-accuracy；§5.2视觉语言错位。 |
| 局限与研究边界 | 最终MCQ分不直接评价Agent轨迹或真实空间产物；专家val参照与test系统得分不可脱离分区比较。 |
| 归档英文页数 | 11 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/GeoMMBench_GeoMMAgent](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [摘要全译＋主要章节译述（非全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E4%B8%AD%E6%96%87%E5%AD%A6%E6%9C%AF%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E4%B8%8E%E6%A0%B8%E5%BF%83%E7%AB%A0%E8%8A%82.md) |
| 其他中文稿及范围 | [摘要全译＋主要章节译述（非全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E4%B8%AD%E6%96%87%E5%AD%A6%E6%9C%AF%E8%AF%91%E7%A8%BF_%E6%91%98%E8%A6%81%E4%B8%8E%E6%A0%B8%E5%BF%83%E7%AB%A0%E8%8A%82.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%85%A8%E6%96%87.md) · [官方](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiao_GeoMMBench_and_GeoMMAgent_Toward_Expert-Level_Multimodal_Intelligence_in_Geoscience_and_CVPR_2026_paper.pdf)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95.md) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5%E6%8A%A5%E5%91%8A.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/README_%E9%98%85%E8%AF%BB%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoMMBench_GeoMMAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

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
| 2 提供链接 | https://geo-mm-agi.github.io |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# GeoMMBench 与 GeoMMAgent：面向地学与遥感的专家级多模态智能

> **翻译范围说明**：摘要全文翻译、正文核心部分译述；英文全文、原图与原始 PDF 保留，可用于逐段补译。

## 原文摘要｜完整中文翻译

多模态大语言模型（Multimodal Large Language Models，MLLMs）的最新进展推动了面向特定领域的人工智能发展，但地球科学与遥感领域的进步仍受到若干特有挑战的制约：学科知识范围广、传感器模态异构以及任务类型分散。为弥补这些不足，作者提出 GeoMMBench，一项覆盖多样遥感学科、传感器和任务的综合性多模态问答基准，能够比以往基准开展更广泛、更加严格的评价。利用 GeoMMBench，作者评估了 36 个开源及专有大语言模型，发现它们在领域知识、感知锚定和推理能力方面存在系统性的不足；这些能力对专家级地理空间解释至关重要。除评价之外，作者还提出 GeoMMAgent：一种通过领域专用遥感模型和工具，策略性地整合检索、感知与推理的多智能体框架。大量实验表明，GeoMMAgent 明显优于独立使用的语言模型，说明工具增强智能体对于动态解决复杂地学与遥感问题具有重要价值。

## Benchmark 构建与任务｜重点译述

GeoMMBench 包含 **1,053 道专家级、基于图像的多项选择题**。问题覆盖遥感、摄影测量、地理信息系统和全球导航卫星系统等领域，涉及光学影像、SAR、多光谱、高光谱、LiDAR 和数字高程模型等传感器或数据类型。问题不仅要求识别影像对象，也涉及专业术语、数据预处理、空间关系和高层地学应用。

作者强调专家知识与人工审校的重要性。任务由领域专家共同设计，经过文本推断偏差和不准确样本的检查：对于仅凭文字表述就能猜出答案、没有真正依赖图像信息的题目，需要修改或剔除。

## GeoMMAgent 的基本机制｜重点译述

GeoMMAgent 将复杂问题分解到**检索—感知—推理**三个功能阶段，使通用语言模型能够借助知识检索与领域遥感工具完成专家级问题。它是一种与 Benchmark 配套的 Agent 方法，但 Benchmark 本身主要通过专家构建的图像多项选择题评价模型，而不是只考察工具调用轨迹。

## 实验与评价｜重点译述

论文对 36 个模型进行比较，利用专家标注的答案评价表现；此外，使用 GeoMMAgent 说明多 Agent 协同对提升复杂地学任务解决能力的贡献。与执行型 GIS Benchmark 不同，此处最关键的评价对象是**专业知识、视觉感知与推理输出**，需要与 GIS 工具真实执行结果区分。

## 图表阅读提示

- **图 1**：地学知识、传感器模态与任务类别的覆盖维度。
- **表 1**：GeoMMBench 与其他地学多模态 Benc
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
