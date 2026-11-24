# GeoLLM-Engine：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/GeoLLM-Engine/原始论文.pdf)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：地学Copilot环境+Benchmark套件；query与tool task分开计数。
- **声称能力**：长链工具调用、最终回复/环境状态及地学视觉任务。
- **任务**：目标检测、地表覆盖、VQA、检索、地图/UI操作等。
- **规模**：10k queries/50,830 tool tasks；100k queries/521,868 tool tasks；1,149,612 images。
- **工具**：Mapbox UI/CLI；Python GIS、Vision、Web、DB；表1合计174，正文称over175。
- **执行**：共享初始环境执行；确定性状态假设；工具/最终状态检查。
- **输入**：影像与文本等7类数据来源、任务模板。
- **输出**：工具序列、参数、回复、地图/UI/数据状态。
- **GT构建**：250人工种子、GPT4解答与确认→10候选执行；9/10最终状态一致接受GT。
- **GT形式**：(q,T*,r*,S*)；工具参数与最终状态。
- **参考轨迹**：有；GPT4生成工具序列与状态。
- **真实产物**：有状态/输出；完整开源文件未核实。
- **评价器**：model-checker谓词：工具/字符串精确、数值ε、ROUGE阈值、地图/UI状态。
- **评分流程**：correctness谓词累计错误→CorrectnessRate；success谓词→SuccessRate；回复ROUGE与下游任务分数。
- **作者局限**：§7：GPT4生成并验证GT可能偏向GPT4；复杂视觉任务困难；ε与完整最终成功聚合未完整给定。

上述基础信息出处：§2–5；表1、3、4；§7，PDF物理页3–8（印刷587–592）。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M107 | Success rate / SuccessRate（primary） | 最终任务回复与环境状态满足目标 | 表3success谓词；完整各任务组合逻辑未详述；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF4–5 |
| M108 | Correctness rate / CorrectnessRate（primary） | 工具与参数的错误归一计分 | valid/needed/missed/str/num错误；非产物成功；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF4–5 |
| M109 | Reply ROUGE-L recall / ROUGE_reply（primary） | 最终回复的参考文本LCS召回 | ROUGE-L recall；不等于地学事实核验；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF5 |
| M110 | Object-detection F1 / ObjDet F1（primary） | 地学视觉目标检测结果 | 表4下游目标检测；IoU/匹配阈值本文未详述；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF6 |
| M111 | Land-cover classification recall / LCC Recall（primary） | 地表覆盖分类结果召回 | 表4LCC Recall；宏/微/类别权重未给完整定义；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF6 |
| M112 | Visual QA ROUGE-L / VQA ROUGE-L（primary） | 视觉问答参考文本重叠 | 表4单列下游VQA；不与总回复ROUGE混算；主套件/模型与10k、100k规模分别报；不合并query与tool task | §3–5 表3–4 PDF6 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M113 | f_validtool | 2_辅助诊断 | 工具名属于catalog；§3 表3 PDF4–5 |
| M114 | f_needed | 2_辅助诊断 | 调用工具在GT中；§3 表3 PDF4–5 |
| M115 | f_missed | 2_辅助诊断 | GT工具未被候选包含；§3 表3 PDF4–5 |
| M116 | f_str | 2_辅助诊断 | 字符串参数相等；§3 表3 PDF4–5 |
| M117 | f_num | 2_辅助诊断 | 数值参数绝对差<ε；§3 表3 PDF4–5 |
| M118 | f_reply | 2_辅助诊断 | ROUGE(reply,reference)>εR；§3 表3 PDF4–5 |
| M119 | f_output | 2_辅助诊断 | 输出对象正确；完整比较器未报告；§3 表3 PDF4–5 |
| M120 | f_map | 2_辅助诊断 | 最终map状态相等；§3 表3 PDF4–5 |
| M121 | f_ui | 2_辅助诊断 | UI状态相等；§3 表3 PDF4–5 |
| M122 | Average tokens per task | 3_效率成本数据特征 | 表4；不报告为成功率；§5 表4 PDF6 |
| M129 | Correctness-error type distribution | 2_辅助诊断 | 图5按错误类别比较；不是另一个Agent成功率；§5 图5 PDF7 |

## 原文核查中的定位修订

100k是自然语言查询数，521,868是工具级task数；表1工具数加和174，正文称over175，记为清单差异。表3两行同名f_map分别表示map/UI，台账UI别名f_ui仅为便于辨识。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R25：GPT4生成并验证GT带来模型偏向 | A；作者§7承认；9/10同状态不等于人工正确；§3 pp3–4；§7 p8 | 盲抽分层GT由独立专家从任务意图重做；记录双标一致与裁决 |
| R26：惩罚多余调用与最终成功不是同一构念 | C；表3/§3明确unnecessary tool可不改最终状态；§3表3 p5 | 固定相同最终状态插入无副作用额外调用；分别读取correctness与success，不要求两者相同 |
| R27：精确状态或文本重叠是否超出用户目标 | C；map/UI全相等；reply ROUGE阈值；任务相关字段规则不足；表3 p5 | 冻结任务，只改无关视图字段/同义回复或反转关键数值，专家判目标满足 |
| R28：默认ε与下游匹配细节不足 | D；正文给可调ε但未完整默认/匹配实现；§3–5 pp4–7 | 取得官方scorer/GT后核默认值与端点；先不执行Agent |

## 资源与优先级

阅读优先级：已完成：第三批。实验优先级（本次分析建议）：中/待资源：作者项目仓库仅网页资产；先拿到官方scorer与GT。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | [代码](https://github.com/dstamoulis/geollm-engine) | 仅项目网页仓库可访问；index.html明确code/dataset coming soon；非评分实现 | 否；否 |
| 数据/任务集 | [数据/任务集](https://github.com/dstamoulis/geollm-engine) | 仅项目网页仓库可访问；index.html明确code/dataset coming soon；非评分实现 | 否；否 |
| GT/参考 | [GT/参考](https://github.com/dstamoulis/geollm-engine) | 仅项目网页仓库可访问；index.html明确code/dataset coming soon；非评分实现 | 否；否 |
| 评价器 | [评价器](https://github.com/dstamoulis/geollm-engine) | 仅项目网页仓库可访问；index.html明确code/dataset coming soon；非评分实现 | 否；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
