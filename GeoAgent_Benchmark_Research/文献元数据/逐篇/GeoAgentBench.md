<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# GeoAgentBench：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis |
| 仓库短名称 | GeoAgentBench |
| 实际 Benchmark 名称 | GeoAgentBench (GABench) |
| 年份与平台 | 2026；arXiv预印本 v1 |
| 原文网址 | [官方原文](https://arxiv.org/abs/2604.13888v1) |
| 唯一主类别 | A |
| 阅读优先级 | P0 |
| 阅读优先级理由 | 比较参数末次尝试对齐、参考路径与地图VLM的测量边界。 |
| 分类理由 | 提出117工具、53任务真实GIS执行沙箱及轨迹/参数/视觉评分，直接对应地学评价机制审计。 |
| 研究用途 | 直接审计对象：比较参数末次尝试对齐、参考路径与地图VLM的测量边界。 |
| 辅助标签 | GIS；参数正确性；轨迹匹配；VLM Judge；真实空间产物 |
| 主要测量对象 | 工具集合、顺序前缀、末次参数与可见地图质量 |
| 评价机制 | TAO-P/R/F1、TIO(LCS)、TEM(LCP)、PEA动态映射/文件存在、VLM；效率另报 |
| Ground Truth 类型 | 专家原子Toolchain、参数、数据文件与参考地图 |
| 实证审计可行性 | RU |
| 可行性依据 | Task02确认评价目录存在；本次benchmark.csv实际仅返回Git LFS指针（目标193385字节），尚未核实真实GT/数据payload和必要环境。 |
| 开源状态 | 代码目录可见；benchmark CSV为LFS指针，不能按已取得CSV内容记账；未运行。 |
| 原文证据位置 | 摘要p1；§3 pp7–9；§4 pp9–11；§6 pp13–15；§7 p16（PDF物理页） |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §4.1 PEA怎样处理重试/文件重命名？§4.2视觉正确是否覆盖数值/拓扑？§4.3成功子集如何筛选？ |
| 局限与研究边界 | §7讨论复杂参数与扩展任务；VLM权重、效率成功门等实现细节未完整给定（Task02已列待核项）。 |
| 归档英文页数 | 20 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/GeoAgentBench](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [正文译稿（代码/参考文献等保留英文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) |
| 其他中文稿及范围 | [正文译稿（代码/参考文献等保留英文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E4%B8%AD%E6%96%87%E5%85%A8%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) · [官方](https://arxiv.org/abs/2604.13888v1)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | 本地原始 PDF 缺失（见官方原文） |
| 图表与原页 | [图表/原页1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/images) · [图表/原页2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/source_pages) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/QA_%E6%A0%B8%E6%9F%A5%E6%8A%A5%E5%91%8A.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/README.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoAgentBench/GeoAgentBench_%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5.md) |

## 原文核验与研究判断

论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；测量对象字段概括评价操作，不把局部得分外推为完整地学能力。

研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。

## 实证条件分项检查

| 条件 | 实际核查状态 |
|---|---|
| 任务集 | benchmark/benchmark.csv仅返回Git LFS指针 |
| GT | CSV目标payload未核验，不能当已读53任务GT |
| 参考轨迹 | 未核查 |
| 输出产物 | 未核查 |
| 评价器源码 | Task02已确认evaluation文件目录；实现尚未运行 |
| 执行环境 | GIS依赖/数据LFS payload未配置 |
| API依赖 | 未核查 |
| 固定轨迹重复评分 | 未核查 |
| 对照样本构造 | 未核查 |
| 独立人工核验 | 未核查 |

## 开源证据阶段

| 阶段 | 状态 |
|---|---|
| 1 作者声明 | 原文与GABench官方仓库声明公开 |
| 2 提供链接 | https://github.com/geox-lab/GABench |
| 3 实际可访问 | 目录可访问；CSV为LFS pointer，不证明目标数据已下载 |
| 4 文件已下载 | 仅指针/目录元数据与README缓存；真实任务/大数据未取回 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# GeoAgentBench：面向空间分析工具增强型智能体的动态执行基准

**原题**：*GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis*  
**作者**：Bo Yu、Cheng Yang、Dongyang Hou（通讯作者）、Chengfu Liu、Jiayao Liu、Chi Wang、Zhiming Zhang、Haifeng Li、Wentao Yang  
**机构**：中南大学地球科学与信息物理学院；湖南科技大学地球科学与空间信息工程学院  
**版本**：arXiv:2604.13888v1，2026-04-15（预印本）  
**代码与数据**：https://github.com/geox-lab/GABench

> **译文说明**：本文件按论文原有章节组织，保留 GIS 算法名、基准名、工具函数名、参数符号和引用标识。图表为从原始 PDF 直接裁切的图像。论文的逐页英文提取、全部 20 页原稿图像分别见同目录的英文 Markdown 和 `source_pages/`。原文中的数学公式及其原始版式同时可在对应页图像中核对。

## 摘要

将大语言模型（Large Language Models，LLMs）引入地理信息系统（Geographic Information Systems，GIS），标志着空间分析向自主化迈进的范式转变。然而，由于地理空间工作流具有复杂、多步骤的特性，评估此类基于 LLM 的智能体仍然面临困难。现有基准主要依赖静态文本或代码匹配，忽视了动态运行时反馈以及空间分析输出的多模态性质。为弥补这一缺口，我们提出 GeoAgentBench（GABench）：一种专门面向工具增强型 GIS 智能体的动态、交互式评测基准。

GABench 提供集成 **117 个原子 GIS 工具**的真实执行沙箱，覆盖 **6 个核心 GIS 领域中的 53 项典型空间分析任务**。考虑到在动态 GIS 环境中，精确的参数配置是决定执行成功与否的首要因素，我们设计了**参数执行准确率**（Parameter Execution Accuracy，PEA），采用“**最后一次尝试对齐**”（Last-Attempt Alignment）策略，量化智能体隐式参数推断的准确程度。同时，提出基于**视觉—语言模型**（Vision-Language Model，VLM）的验证方法，以评估数据空间准确性及地图制图风格遵循程度。

此外，为应对参数不一致和运行时异常导致的频繁任务失败，我们提出一种模拟专家认知工作流的新型智能体架构——**Plan-and-React（规划—反应）**，通过分离全局编排和逐
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
