<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->

# GeoNatureAgent：文献分类记录

| 字段 | 核查记录 |
|---|---|
| 完整英文标题 | GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks |
| 仓库短名称 | GeoNatureAgent |
| 实际 Benchmark 名称 | GeoNatureAgent Benchmark（v5/v6合计103任务） |
| 年份与平台 | 2026；GeoIndustry 2026；归档arXiv v1 |
| 原文网址 | [官方原文](https://arxiv.org/abs/2610.09112v1) |
| 唯一主类别 | A |
| 阅读优先级 | P0 |
| 阅读优先级理由 | 可冻结JSON、工具日志和答案，检查子串、数值窗口与v5/v6预算豁免。 |
| 分类理由 | 在固定16工具接口上提供103环境/地学任务及确定性案例检查，是门控评分审计对象。 |
| 研究用途 | 直接审计对象：可冻结JSON、工具日志和答案，检查子串、数值窗口与v5/v6预算豁免。 |
| 辅助标签 | 环境；确定性规则；部分得分；参数正确性；效率与成本 |
| 主要测量对象 | 期望工具/动作、答案数值与关键词、图表URL、轮次预算 |
| 评价机制 | 8种检查；v5免成本、v6能力口径还免轮次/预算；raw与combined分别记录 |
| Ground Truth 类型 | 案例JSON的期望集合、关键词、数值、预算与固定地区统计 |
| 实证审计可行性 | R1 |
| 可行性依据 | 实际取回93条v5案例JSON（含ground_truth等）与scoring.py；服务/API、运行环境和独立人工判据尚未测试。 |
| 开源状态 | 代码与v5任务/GT实际可访问且已保存工作缓存；当前v7不混入本次v5/v6；未配置服务、未运行。 |
| 原文证据位置 | 摘要p1；工具§3 p3；§5 p5；实验§6 pp5–8；§8 p9 |
| 核验状态 | 原文定向核验（分类所需章节）；非代码/实验复现 |
| 原文核验范围 | 英文摘要；方法/任务与数据构建；评价机制/指标；实验或系统案例；讨论、局限或结论边界 |
| 重点阅读章节 | §5表4/脚注first float%；§6.5表9合并口径；§6.7提示版本与格式适配。 |
| 局限与研究边界 | 作者指出小类别、地域和服务商差异；§6.7报告格式不匹配待核实。当前仓库v7不替代本地v5/v6证据。 |
| 归档英文页数 | 10 |
| 核验日期 | 2026-11-24 |
| 实际目录 | [论文翻译/GeoNatureAgent](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent) |
| 版本注意 | 本地PDF DOI为10.1145/3849727.3856786，Task02访问的当前README另给DOI；本目录按已归档arXiv v1，不静默混版。 |

## 阅读材料

| 材料 | 入口 / 状态 |
|---|---|
| 中文主入口及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 其他中文稿及范围 | [章节中文译稿（未认定全文覆盖）](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E4%B8%AD%E6%96%87%E8%AF%91%E6%96%87.md) |
| 英文原文 | [本地原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E8%8B%B1%E6%96%87%E5%8E%9F%E6%96%87_%E9%80%90%E9%A1%B5%E5%AE%8C%E6%95%B4%E6%8F%90%E5%8F%96.md) · [官方](https://arxiv.org/abs/2610.09112v1)；完整英文原文/逐页提取稿（以归档原文为准） |
| PDF | [PDF](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |
| 图表与原页 | [图表/原页1](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/images) · [图表/原页2](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/source_pages) |
| 核查报告 | [核查](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/QA_%E9%80%90%E9%A1%B5%E6%A0%B8%E6%9F%A5.md) |
| 阅读说明 | [阅读说明](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/README_%E7%9B%AE%E5%BD%95%E8%AF%B4%E6%98%8E.md) |
| 用于核验的本地原文 | [归档原文](../../../%E8%AE%BA%E6%96%87%E7%BF%BB%E8%AF%91/GeoNatureAgent/%E5%8E%9F%E5%A7%8B%E8%AE%BA%E6%96%87.pdf) |

## 原文核验与研究判断

论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；测量对象字段概括评价操作，不把局部得分外推为完整地学能力。

研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。

## 实证条件分项检查

| 条件 | 实际核查状态 |
|---|---|
| 任务集 | 已读官方v5案例JSON，93条 |
| GT | JSON含ground_truth/notes与期望工具/动作/关键词 |
| 参考轨迹 | 未核查 |
| 输出产物 | 未核查 |
| 评价器源码 | scoring.py已取回；未作完整代码审计 |
| 执行环境 | 未配置自托管API/模型服务 |
| API依赖 | API部署与凭据/费用条件未验证 |
| 固定轨迹重复评分 | 候选可离线评分；尚未验证 |
| 对照样本构造 | 未核查 |
| 独立人工核验 | 需建立独立案例意图/数值判据 |

## 开源证据阶段

| 阶段 | 状态 |
|---|---|
| 1 作者声明 | 论文与官方仓库给出代码/案例 |
| 2 提供链接 | https://github.com/gabrielireland/GeoNatureAgent_Benchmark |
| 3 实际可访问 | 实际取回scoring.py和benchmark_v5.json |
| 4 文件已下载 | 小型源码/JSON保存于工作缓存；未下载大影像资产 |
| 5 已验证运行 | 未运行 |

## 译稿范围声明摘录

以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。

```text
# GeoNatureAgent（GNA）：面向地理空间与环境任务工具型智能体的部署前评估框架与基准

**英文原题：** GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks  
**作者：** Gabriel Diaz-Ireland、Diego Prieto-Herráez、Mario García Peces 等。  
**原稿：** 10 页；GeoIndustry '26。

> **译文范围提示：** 以下是摘要全文翻译及正文核心内容的顺序中文译述，工具 API 名称、代码路径、参数与指标名称保留英文，便于核验。完整英文原文、所有参考文献和跨栏表格截图保留在同包；本文未将所有原文段落逐词汉化。

## 摘要（全文翻译）

在将具备工具调用能力的大语言模型智能体部署到环境与地理空间工作流之前，开发团队需要证据证明智能体能够可靠地选择适当的操作，并与真实 API 正确交互。然而，目前缺少可复用、自托管的部署前评估基础设施。本文提出 **GeoNatureAgent（GNA）**，一种面向工具型智能体的部署前评估框架。GNA 将固定的 **16 工具**地理空间接口（12 项主要操作、4 项辅助操作）以 **Model Context Protocol（MCP）**服务器的形式发布，使被测智能体成为唯一变化因素：任何兼容 MCP 的客户端都可以直接接入，并由相同的工具层、任务集合和确定性评分器进行评价。

该框架的旗舰实例是包含 **103 道任务**的基准，其中有覆盖 **18 个类别的 93 道主测试任务**和 **10 道比较类扩展任务**。任务涉及工具选择、多轮对话、空间推理、跨指标综合、错误处理、多语言理解、任务拒绝等能力，并在面向西班牙和葡萄牙三类环境指标的开放式自托管地理空间 API 上执行。作者在 Vertex AI、OpenRouter 和 Anthropic 平台上比较了九个大型语言模型，每个模型以温度 1.0 运行三个不同随机种子，并把任务能力与每题成本作为正交维度分别报告。

实验结果表明：（1）Claude Sonnet 4 在全部 103 题上取得最高的 **61.7% ± 0.7%** 能力准确率（93 题主集为 **60.8% ± 0.8%**），DeepSeek V3.2 以 **57.9% ± 3.9%** 紧随其后，其余模型都未超过 53%；（2）成本—准确率帕累托前沿主要由开放权重模型占据，DeepSeek V3.2 以 **11.3 倍更低的标价成本**达到 Claude 约 93% 的能力，
```

[返回文献总索引](../../%E6%96%87%E7%8C%AE%E6%80%BB%E7%B4%A2%E5%BC%95.md)
