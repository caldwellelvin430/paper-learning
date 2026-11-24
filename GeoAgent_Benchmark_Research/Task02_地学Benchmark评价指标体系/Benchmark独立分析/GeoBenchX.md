# GeoBenchX：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/GeoBenchX/原始论文.pdf)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：工具调用Benchmark；ReAct为测试Agent。
- **声称能力**：可解任务工具方案生成及不可解任务识别/拒绝。
- **任务**：4组199任务+3个无工具任务；含不可解任务。
- **规模**：202=123可解+79不可解；23操作工具及reject工具。
- **工具**：LangGraph；23个地学数据工具；本地CSV/矢量/栅格快照。
- **执行**：真实执行并记录对话；至多25迭代；最终主要评分算法代码。
- **输入**：18 CSV、21 vector、11 raster及自然语言请求。
- **输出**：Python式工具调用方案、回复与运行图像；最终回复不纳入主体评分。
- **GT构建**：作者构建一个或多个可接受参考工具调用方案，并记录可变参数/顺序；50例人工标注校准Judge。
- **GT形式**：参考Python调用片段；不可解任务reject；少数空方案。
- **参考轨迹**：有；允许多参考与语义等价。
- **真实产物**：执行产生；未用完整最终产物GT匹配。
- **评价器**：3个LLM Judge语义匹配代码方案。
- **评分流程**：每Judge给0/1/2及理由→计算各分数频率→对3个Judge频率取平均。
- **作者局限**：§8：最终回复不评、规模中等、每Agent单次运行、缺生成方差；Judge校准非独立外部审计。

上述基础信息出处：§4–6、§8，PDF物理页2–4、6–8。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M063 | No-match frequency / Freq0（primary） | 候选工具方案与允许参考方案语义等价程度 | 每Judge输出0不匹配/1部分/2匹配及理由；不是最终产物匹配；每Judge分数频率→3Judge平均；按任务组/可解性分层 | §5–6.1 PDF4 |
| M064 | Partial-match frequency / Freq1（primary） | 候选工具方案与允许参考方案语义等价程度 | 每Judge输出0不匹配/1部分/2匹配及理由；不是最终产物匹配；每Judge分数频率→3Judge平均；按任务组/可解性分层 | §5–6.1 PDF4 |
| M065 | Match frequency / success rate / Freq2（primary） | 候选工具方案与允许参考方案语义等价程度 | 每Judge输出0不匹配/1部分/2匹配及理由；不是最终产物匹配；每Judge分数频率→3Judge平均；按任务组/可解性分层 | §5–6.1 PDF4 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M066 | Normalized solution-length difference | 3_效率成本数据特征 | 文本称relative to candidate length；0.5解释与常见百分增幅不一致；不替作者修正；§6.1 PDF4 |
| M067 | Input tokens | 3_效率成本数据特征 | 每模型一次；不是重复运行期望成本；§6.4 PDF6–7 |
| M068 | Output tokens | 3_效率成本数据特征 | 每模型一次；不是重复运行期望成本；§6.4 PDF6–7 |
| M069 | Judge–human score agreement | 4_Benchmark元评价 | GPT4.1 96%、Claude3.5 94%、Gemini2.5 88%；同集合调参与选Judge，无独立holdout；§5.2 图1 PDF4 |

## 原文核查中的定位修订

202任务里199落入四组，另3项无工具任务；123可解/79不可解是另一分层。三Judge平均的是匹配频率，不是平均0/1/2分或多数票。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R15：Judge校准与选型均用同50例，外部一致性未知 | C；§5.2 tuned and selected same set，无独立holdout说明；§5.2 p4 | 预注册独立任务/候选holdout，固定rubric及模型重复评分；人标者与调参者分离 |
| R16：最终答案不纳入主体评分 | A；作者局限明确；算法片段语义匹配；§5 p4；§8 p8 | 固定方案替换最终回复/实际输出；分别标方案与交付成功，检验跨构念外推 |

## 资源与优先级

阅读优先级：已完成：第二批。实验优先级（本次分析建议）：高：已有方案可冻结，适合Judge重复评分与顺序置换。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | [代码](https://github.com/Solirinai/GeoBenchX) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 数据/任务集 | [数据/任务集](https://github.com/Solirinai/GeoBenchX/tree/main/data) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| GT/参考 | [GT/参考](https://github.com/Solirinai/GeoBenchX/blob/main/benchmark_set/tasks_and_reference_solutions.json) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 评价器 | [评价器](https://github.com/Solirinai/GeoBenchX/blob/main/geobenchx/evaluation.py) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
