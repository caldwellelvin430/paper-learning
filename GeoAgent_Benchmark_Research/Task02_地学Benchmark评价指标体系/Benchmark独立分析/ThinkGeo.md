# ThinkGeo：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/ThinkGeo/原始论文.pdf)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：遥感工具增强Agent Benchmark；不是仅知识问答集。
- **声称能力**：逐步指令/工具/参数/总结，以及端到端感知与逻辑解题。
- **任务**：7个RGB任务类别；另50 SAR任务。
- **规模**：486=436 RGB+50 SAR；SAR参考244推理步。
- **工具**：AgentLego扩展变化检测/像素分割等感知、逻辑与操作工具。
- **执行**：step-by-step教师参考上下文和自由end-to-end为不同协议。
- **输入**：影像、问题、GSD/框等元数据。
- **输出**：Thought/Action/Observation轨迹、文本/图像相关答案、分割等。
- **GT构建**：人工分析影像并补标，o4-mini半自动界面辅助构建ReAct；人工与脚本验证；未报告完整多人一致性统计。
- **GT形式**：gold dialogues：工具名/参数/观察/答案与图像信息。
- **参考轨迹**：有ReAct参考对话；逐步评分条件含参考历史。
- **真实产物**：工具实际生成；非所有结果采用独立几何GT直接计分。
- **评价器**：GTA式逐步accuracy；GPT-4o-mini查询特定答案判定；部分机制未详述。
- **评分流程**：逐步四accuracy与端到端P/O/L、Ans、AnsI；两个协议不可混算。
- **作者局限**：正文讨论难任务与循环；补充S2格式失败；完整Judge公式/空输出分母未报告。

上述基础信息出处：§3–5；表3；S1–S3、S7，PDF物理页4–8、11–14。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M078 | Instruction following accuracy / InstAcc（primary） | 逐步指令格式/协议遵循 | GTA式逐步评测；精确解析式/分母未报告；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF6–7 |
| M079 | Tool selection accuracy / ToolAcc（primary） | 逐步工具选择 | GTA式逐步评测；并非自由端到端任务成功率；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF6–7 |
| M080 | Argument prediction accuracy / ArgAcc（primary） | 逐步工具参数 | 精确/语义匹配、条件分母未详细给定；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF6–7 |
| M081 | Summarization accuracy / SummAcc（primary） | 逐步总结 | GTA式汇总；完整rubric未报告；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF6–7 |
| M082 | Perception-tool accuracy / P（primary） | 端到端感知工具使用 | 表3P列；工具类别分母与错误后处理未详述；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF7 |
| M083 | Operation-tool accuracy / O（primary） | 端到端操作工具使用 | 表3O列；不是图像产物精度；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF7 |
| M084 | Logic-tool accuracy / L（primary） | 端到端逻辑工具使用 | 表3L列；具体命中计算未详述；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF7 |
| M085 | Answer accuracy / Ans（primary） | 端到端最终答案满足查询 | GPT-4o-mini判定替代原GTA字符串；缺完整Judge稳定性协议；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF6–7 |
| M086 | Image-grounded answer accuracy / AnsI（primary） | 图像相关答案正确性 | 表3AnsI；与Ans不同子域；具体图像输入与判分细节未完整给；表3按模型/两协议百分比；SAR另表复用定义 | §4–5 表3；S1 PDF7 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M087 | No Action rate | 2_辅助诊断 | planning failure无action；S2；图6 PDF7、11 |
| M088 | Invalid JSON rate | 2_辅助诊断 | 不合法JSON；S2；图6 PDF7、11 |
| M089 | Invalid argument value rate | 2_辅助诊断 | ArgValues错误；S2；图6 PDF7、11 |
| M090 | Invalid tool name rate | 2_辅助诊断 | ToolName错误；S2；图6 PDF7、11 |
| M091 | Single-step final-answer format error rate | 2_辅助诊断 | FinalAnswerSingleStep错误；S2；图6 PDF7、11 |
| M092 | Tool-call error rate | 2_辅助诊断 | 图6工具调用错误；确切跨任务加权未给；S2；图6 PDF7、11 |
| M093 | Total tool calls | 3_效率成本数据特征 | 图6累计调用数量；图6；S7表A4 PDF7、13 |
| M094 | Step-by-step latency | 3_效率成本数据特征 | Table A4 s/query；执行所有reasoning steps，不是平均单步耗时；图6；S7表A4 PDF7、13 |
| M095 | End-to-end latency per query | 3_效率成本数据特征 | 每查询自由执行耗时；S7表A4；图6；S7表A4 PDF7、13 |
| M126 | Step metric–answer Pearson correlation | 4_Benchmark元评价 | Fig5 Pearson；相关不证明局部能力导致任务成功；§5 图5 PDF7 |
| M127 | Human annotation effort | 3_效率成本数据特征 | 补充S6人工投入；不计入Agent能力；S6 PDF13 |
| M128 | Number of tool-call errors | 2_辅助诊断 | Fig6报告工具调用总数及对应错误数；不与错误率混同；§5 图6 PDF7 |

## 原文核查中的定位修订

表3主体是RGB436查询，SAR50在补充表A1复用九项定义；不把486全体都说成主体表的共同分母。逐步教师上下文和端到端实际执行不可当同一控制条件。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R19：局部accuracy匹配及分母定义不充分 | D；沿用GTA名称但文中无完整公式；不能直接当精确参数成功；§4 p6；表3 p7 | 定位GTA继承类；检查错误格式、未调用、空args等样本的条件分母与得分 |
| R20：Judge与图像grounding评分稳定性待检 | C；4o-mini按查询定制问题；缺完整Judge-only实验；§4 p6；表3 p7 | 冻结对话、图像、问题与rubric，独立重复Judge并做图像交换/答案反事实 |

## 资源与优先级

阅读优先级：已完成：第三批。实验优先级（本次分析建议）：高：冻结gold对话核实accuracy分母及答案Judge。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | [代码](https://github.com/mbzuai-oryx/ThinkGeo) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 数据/任务集 | [数据/任务集](https://huggingface.co/datasets/MBZUAI/ThinkGeo) | 未直接请求HF；仅官方README链接确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| GT/参考 | [GT/参考](https://huggingface.co/datasets/MBZUAI/ThinkGeo) | 未直接请求HF；仅官方README链接确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 评价器 | [评价器](https://github.com/mbzuai-oryx/ThinkGeo/tree/main/opencompass) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
