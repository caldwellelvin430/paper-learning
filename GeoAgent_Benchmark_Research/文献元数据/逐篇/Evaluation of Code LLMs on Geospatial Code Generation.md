<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# Evaluation of Code LLMs on Geospatial Code Generation：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | Evaluation of Code LLMs on Geospatial Code Generation |
| 仓库短名称 | Evaluation of Code LLMs on Geospatial Code Generation |
| 实际 Benchmark 名称 | Geospatial code-generation benchmark（原文未单独命名） |
| 年份与平台 | 2024；7th ACM SIGSPATIAL International Workshop on AI for Geographic Knowledge Discovery (GeoAI 2024) |
| 原文网址 | [官方原文](https://doi.org/10.1145/3687123.3698286) |
| 唯一主类别 | D |
| 阅读优先级 | P1 |
| 阅读优先级理由 | 对照相似度评分与多测试场景功能正确性，借鉴边界测例和部分通过规则。 |
| 分类理由 | 评价独立地学函数生成与测试用例，属于D静态代码评测；执行验证方法与审计直接相关故提升阅读优先级。 |
| 研究用途 | 相关工作：对照相似度评分与多测试场景功能正确性，借鉴边界测例和部分通过规则。 |
| 辅助标签 | 地学代码；可执行测试；参考代码；测试覆盖；部分得分 |
| 主要测量对象 | 生成地学Python函数对测试场景的功能正确性 |
| 评价机制 | Accuracy测试用例通过比例、Pass@1全通过、Pass_any@1至少一项通过；执行单函数 |
| Ground Truth 类型 | 人工任务、参考函数和多个测试场景/期望值 |
| 实证审计可行性 | RU |
| 可行性依据 | 尚未核查任务、GT、评价器与必要环境的完整可用链，不凭论文公开声明评级 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要p1；数据§3 pp3–4；§4.1 p5；结果pp6–7；§5 p8 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §3任务复杂度/库覆盖；§4.1预导入依赖、输出裁剪与三指标分母；§5边界案例不足。 |
| 局限与研究边界 | 作者仅测7B/8B模型且需增加任务/库/边界场景；测试通过只支持已覆盖功能。 |
| 归档英文页数 | 9 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/Evaluation of Code LLMs on Geospatial Code Generation](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 其他中文稿及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87_%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://doi.org/10.1145/3687123.3698286)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95.md) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/README_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Evaluation%20of%20Code%20LLMs%20on%20Geospatial%20Code%20Generation/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

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
| 1 作者声明 | PDF p1明确声称公开数据集和可复现评价代码，尚未独立核查 |
| 2 提供链接 | https://github.com/kraina-ai/geospatial-code-llms-dataset |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# 地理空间代码生成大模型的评估

**原题：** Evaluation of Code LLMs on Geospatial Code Generation  
**作者：** Piotr Gramacki、Bruno Martins、Piotr Szymański  
**发表：** GeoAI’24（第七届 ACM SIGSPATIAL 地理知识发现人工智能国际研讨会），2024 年 10 月 29 日—11 月 1 日，美国亚特兰大。  
**DOI：** 10.1145/3687123.3698286  
**复现仓库：** https://github.com/kraina-ai/geospatial-code-llms-dataset

> 本稿依照原文的章节顺序翻译论文主体（摘要及第 1–5 节）；模型标识符、Python 语法和文献著录保持英文。全部 9 页英文文本在 `英文全文_逐页提取.md`，原论文及每页截图亦附于压缩包。图表保持原文截图，提供中文解读。

## 摘要

人们很早就开始研究软件开发辅助工具，近年来的研究开始利用大语言模型（Large Language Models，LLMs）生成代码。这些模型能够为数据科学和机器学习应用生成 Python 代码。LLM 可以提高软件工程师日常工作的生产效率，也能为经验不足的开发者充当“导师”，成为可行的学习辅助工具。利用 LLM 生成高质量代码同样有益于地理空间数据科学。然而，地理空间领域面临与通用代码生成不同的挑战，而代码生成 LLM 通常并未接受地理空间任务的专门评估。

本文介绍如何通过选择一组地理空间任务，为代码生成模型构建评估基准。研究人员根据任务复杂度和所需工具对地理空间任务进行分类，进而设计数据集，以考察模型在**空间推理、空间数据处理和地理空间工具使用**方面的能力。数据集由人工精心编制的具体编程问题组成，以保证质量。每道题均配有一组测试情形，以自动检查生成代码的正确性。作者还利用这一数据集测试了多种现有代码生成大模型在地理空间领域的表现，并将数据集和可复现的评估代码公开在 GitHub 仓库中，希望它能成为今后评估新模型的基准，并推动能够高准确率解决地理空间编码任务的专用模型与智能编程助手的发展。

**ACM CCS 概念：** 计算方法—自然语言处理；信息系统—地理信息系统；以人为中心的计算—自然语言接口。  
**关键词：** 地理空间数据科学、代码生成、大语言模型。

## 1 引言

如今，大语言模型已能够有效应用于代码生成，尤其适用于较常见的编程语言及领域，例如面向数据科学和机器学习的 Python 编程。这类能力能够辅助专家编写代码，提高工作效率；同时，模型能够根据自然语言问题描述返回代码示例，为初学者提供学习支持。这些优势也可以扩展到地理空间数据科学。
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
