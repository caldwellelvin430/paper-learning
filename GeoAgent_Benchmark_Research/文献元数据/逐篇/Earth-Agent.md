<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# Earth-Agent：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents |
| 仓库短名称 | Earth-Agent |
| 实际 Benchmark 名称 | Earth-Bench |
| 年份与平台 | 2026；ICLR 2026；归档arXiv v3 |
| 原文网址 | [官方原文](https://arxiv.org/abs/2509.23141v3) |
| 唯一主类别 | C |
| 阅读优先级 | P1 |
| 阅读优先级理由 | 追溯TAO/TIO/TEM/参数指标来源，比较轨迹匹配与最终EO答案。 |
| 分类理由 | Earth-Agent系统配套Earth-Bench跨RGB/光谱/产品任务，专项研究价值在地球观测定量执行而非仅系统示例。 |
| 研究用途 | 跨领域验证候选：追溯TAO/TIO/TEM/参数指标来源，比较轨迹匹配与最终EO答案。 |
| 辅助标签 | 地球观测；参考轨迹；光谱；参数正确性；执行环境 |
| 主要测量对象 | 多模态EO工具规划、参数、科学定量答案与调用效率 |
| 评价机制 | 双层step-by-step和end-to-end；TAO/TIO/TEM/Parameter Accuracy及最终Accuracy/Efficiency |
| Ground Truth 类型 | 248问题的专家解决路径与参考答案、EO影像/光谱/产品数据 |
| 实证审计可行性 | RU |
| 可行性依据 | 尚未核查任务、GT、评价器与必要环境的完整可用链，不凭论文公开声明评级 |
| 开源状态 | 代码、任务/数据、GT、评分器和环境的当前完整可用链尚未核查；RU或N/A不由论文链接自动升级；未运行。 |
| 原文证据位置 | 摘要pp1–2；框架§3 pp4–6；§3.3/§4 p6；实验pp7–10；附录B |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §3.3 dual protocol；§4任务与GT；附录B.2公式；区分Earth-Agent与HTAM EarthAgent。 |
| 局限与研究边界 | 专门EO工具/模型和数据约束适用范围；正确金路径不保证感知输出无误；发布承诺不等于已复现。 |
| 归档英文页数 | 65 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/Earth-Agent](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent) |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [摘要与章节译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 其他中文稿及范围 | [摘要与章节译述（非逐句全文）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E8%8B%B1%E6%96%87%E5%85%A8%E6%96%87_%E9%80%90%E9%A1%B5%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2509.23141v3)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E5%9B%BE%E8%A1%A8%E7%B4%A2%E5%BC%95.md) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/README_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/Earth-Agent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

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
| 2 提供链接 | https://github.com/opendatalab/Earth-Agent |
| 3 实际可访问 | 未核查 |
| 4 文件已下载 | 未核查实验资产；本地论文存在不等于资产下载 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# Earth-Agent：借助智能体释放地球观测的全部潜力

**原题：** Earth-Agent: Unlocking the Full Landscape of Earth Observation with Agents  
**作者：** Peilin Feng、Zhutao Lv、Junyan Ye、Xiaolei Wang、Xinjie Huo、Jinhua Yu、Wanghan Xu、Wenlong Zhang、Lei Bai、Conghui He、Weijia Li  
**收录：** ICLR 2026，原稿 65 页。  
**代码：** https://github.com/opendatalab/Earth-Agent  
**数据集：** https://huggingface.co/datasets/Sssunset/Earth-Bench  
**项目页面：** https://opendatalab.github.io/Earth-Agent/

> 说明：本中文稿按原文章节结构译写摘要、导言、相关工作、核心方法、评价指标、主要实验和结论，并整理附录 A–G 的技术说明与全部图表索引。大量工具 API 表格、长代码块及案例图中的英文原始内容保留为截图和逐页英文稿，尚不能视为每个英文句子均已逐句汉化的严格全译本。原始 PDF、65 页逐页提取稿以及原稿截图全部附于压缩包。

## 摘要

地球观测（Earth Observation，EO）对于理解地球系统不断变化的状态至关重要。尽管近年来多模态大语言模型（Multimodal Large Language Models，MLLMs）推动了 EO 研究的发展，但它们仍缺少解决复杂任务所需的多步推理与领域专用工具使用能力。基于智能体（Agent）的方法提供了有前景的方向，但现有工作仍处于早期阶段，通常局限于 RGB 图像感知、浅层推理，且缺少系统性的评价协议。

为克服这些限制，本文提出 **Earth-Agent**：一个基于模型上下文协议（Model Context Protocol，MCP）的工具生态，统一支持 RGB 与光谱类 EO 数据，使系统能够超越预训练 MLLM 的既有能力，完成跨模态、多步骤、定量的时空推理。Earth-Agent 可以动态调用专家工具和模型，完成地球物理参数反演、定量时空分析等复杂科学任务。

为实现综合评价，作者进一步构建 **Earth-Bench**，包含 **248 道专家编写的任务、13,729 幅图像**，覆盖光谱、地球观测产品和 RGB 三种数据模态，并引入同时评估推理轨迹与最终结果的双层评价协议。论文通过改变 LLM 主干模型、与通用智能体框架比较、与遥感 MLLM 在遥感任务上比较等实验，验证了 Earth-Agent 的有效
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
