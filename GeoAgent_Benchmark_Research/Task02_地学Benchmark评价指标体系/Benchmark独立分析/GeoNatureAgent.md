# GeoNatureAgent：独立分析

核查日期：2026-11-24。本文件基于[本地英文原文](../../../论文翻译/GeoNatureAgent/原始论文.pdf)。中文稿只用于术语辅助；所有论文事实按下列原文节页追溯。

## 对象定位与基本信息

- **定位**：GNA系统+103任务Benchmark；BigEarthNet为数据域，不另计Benchmark。
- **声称能力**：多轮地学工具选择、数据读取/比较、UI与答案合规。
- **任务**：v5 18类93任务；v6比较与聚合10任务。
- **规模**：103=93+10；9模型；通常3种seed，Claude2次独立采样。
- **工具**：16工具（12主+4辅）；Cloud Run、MCP式接口；Spain COG与Portugal预聚合统计。
- **执行**：真实服务调用；ReAct；max_turns=10；temperature=1。
- **输入**：任务JSON；西班牙侵蚀/CO2；葡萄牙BigEarthNet地区统计。
- **输出**：答案、工具记录、UI action、图表URL。
- **GT构建**：预定义案例JSON、固定指标数值及期望工具/动作；论文未完整交代多人标注一致性。
- **GT形式**：expected_tools/actions、关键词、标签数值与预算。
- **参考轨迹**：有预期工具集合；完整唯一逐步参考轨迹未报告。
- **真实产物**：有工具返回和图表URL；所有任务的独立GT地学文件未报告。
- **评价器**：确定性集合召回、子串、数值解析与预算门。
- **评分流程**：8种适用检查→v5仅免成本；v6能力分免成本及轮次；raw严格分另报；按seed聚合。
- **作者局限**：§8：小类别、地域/工具有限、服务商部署差异、严格门掩盖部分完成；§6.7格式不匹配待核实。

上述基础信息出处：§3–8；表4、6、9，PDF物理页3–9。

## 正式评价指标与组件

| ID | 原文名称/缩写 | 实际测量对象 | 判分规则与分母 | 来源 |
| --- | --- | --- | --- | --- |
| M032 | v5 capability accuracy / Cap_v5（primary） | 相应协议下多项合规/能力门全通过 | 所有适用能力检查通过；只豁免max_cost_usd；每seed任务准确率；通常3seed均值±SD；Claude2次 | §5、§6.5 表9 PDF5 |
| M033 | v6 capability accuracy / Cap_v6（primary） | 相应协议下多项合规/能力门全通过 | 豁免预算/round exhaustion；与v5口径不同；每seed任务准确率；通常3seed均值±SD；Claude2次 | §5、§6.5 表9 PDF8 |
| M034 | Strict/raw pass accuracy / Raw（primary） | 相应协议下多项合规/能力门全通过 | 不豁免round/budget的严格适用检查；cost-gated列可由CSV恢复；每seed任务准确率；通常3seed均值±SD；Claude2次 | §5、§6.5 表9 PDF5、8 |
| M035 | Combined 103-task capability accuracy / Cap_103（primary） | 相应协议下多项合规/能力门全通过 | v5+v6 inclusive汇总；继承各子集不同豁免口径；每seed任务准确率；通常3seed均值±SD；Claude2次 | §5、§6.5 表9 PDF8 |
| M036 | expected_tools / expected_tools（component） | 预期工具召回 | 每个预期工具均调用；额外工具不使失败；recall=1；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M037 | expected_actions / expected_actions（component） | UI动作覆盖 | 每个预期UI action生成；recall=1；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M038 | must_contain / must_contain（component） | 答案必需关键词覆盖 | 所有关键词在答案中以不区分大小写子串出现；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M039 | must_not_contain / must_not_contain（component） | 答案禁止关键词合规 | 禁止词不在答案中出现；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M040 | numeric_accuracy / numeric_accuracy（component） | 标签数值回复准确性 | 标签后120字符窗口第一个float%与GT差≤tol；默认±2pp；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M041 | chart_generated / chart_generated（component） | 图表URL产出 | 仅预期generate_chart时检查至少1图表URL；不核实图表内容；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |
| M042 | max_rounds / max_rounds（component） | 循环预算内完成 | loop iterations≤case budget；v6 capability可豁免；二元检查并入相应capability；不适用项不应强记0 | §5 表4与脚注 PDF5 |

完整公式、变量、阈值与未报告细节见[03_评价指标定义与公式](../03_评价指标定义与公式.md)。逐项能力结论边界见[07_构念效度](../07_构念效度与测量对象分析.md)。

## 非正式能力统计的分流

| ID | 统计 | 类型 | 规则/来源 |
| --- | --- | --- | --- |
| M043 | Check score | 2_辅助诊断 | passed checks / applicable checks；成本门是否计分母需核代码；§5 PDF5 |
| M044 | Keyword coverage | 2_辅助诊断 | 大小写不敏感子串；关键词分母为适用词；§5 PDF5 |
| M045 | Tool F1 | 2_辅助诊断 | 连续诊断；不作为capability gate；§5 PDF5 |
| M046 | Dominant error-category frequency | 2_辅助诊断 | 按tool→chart→data→round→cost→keyword→forbidden优先级；非多标签；§5 PDF5 |
| M047 | max_cost_usd | 3_效率成本数据特征 | 估计token成本≤case预算；v5默认$0.10；不入v5能力门；§5–6 PDF5–7 |
| M048 | Estimated USD cost | 3_效率成本数据特征 | 按token与模型费率估计；§5–6 PDF5–7 |
| M049 | Token consumption | 3_效率成本数据特征 | 输入/输出token；§5–6 PDF5–7 |
| M050 | Cost utilisation | 3_效率成本数据特征 | 成本/案例预算；完整公式未报告；§5–6 PDF5–7 |
| M051 | Estimated energy | 3_效率成本数据特征 | 0.40 Wh/1000 tokens；非硬件实测；§5–6 PDF5–7 |
| M052 | Estimated carbon | 3_效率成本数据特征 | 400 gCO2/kWh；非地理时变实测；§5–6 PDF5–7 |
| M053 | Seed variation and bootstrap confidence interval | 4_Benchmark元评价 | SD跨seed；95% bootstrap 2000重采样93案例；不能当Judge-only方差；§6.3、6.7 PDF6、8 |

## 原文核查中的定位修订

当前官方cases目录还有benchmark_v7.json；本次严格以本地论文的v5/v6/103口径为对象，不用v7覆盖。表4nearest percentage与脚注first float%有表述差异，脚注更具体。

## 下一轮可检验风险

| 风险 | 证据等级与依据 | 检验方式 |
| --- | --- | --- |
| R09：字符串或窗口首数字可能与真实意图错绑定 | C；标签后120字符第一个float%；必需词子串；§5表4 p5 | 同一正确数值改表述、插入邻近数字、否定句；固定case重评分，专家双盲判意图 |
| R10：v5/v6豁免门不一致，合并不能当同一严格成功 | C；v5仅免成本；v6还免round exhaustion；表9明确；§5 p5；§6.5 p8 | 冻结103条原始结果，同时导出all-strict、cost-only、cost+rounds三口径及每门混淆 |
| R11：格式不匹配导致能力低分的作者报告待核实 | A；§6.7 Sonnet4.5 partial85%但capability30.1%；作者flagged for verification；§6.7 p8 | 取得该次CSV/原始tool payload，核格式适配与规则版本；不重新生成Agent回复 |
| R12：URL存在不代表图内容正确 | C；表4只查至少1 URL；属于有限生成检查；§5表4 p5 | 保留URL但交换/损坏图表，独立核图内容与引用来源 |

## 资源与优先级

阅读优先级：已完成：第一批。实验优先级（本次分析建议）：最高：纯评分规则可用固定JSON/答案低成本验证。

| 资源 | 官方入口 | 已完成检查 | 下载/运行 |
| --- | --- | --- | --- |
| 代码 | [代码](https://github.com/gabrielireland/GeoNatureAgent_Benchmark) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 数据/任务集 | [数据/任务集](https://github.com/gabrielireland/GeoNatureAgent_Benchmark/tree/main/geoagentbench/cases) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| GT/参考 | [GT/参考](https://github.com/gabrielireland/GeoNatureAgent_Benchmark/blob/main/geoagentbench/cases/benchmark_v5.json) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |
| 评价器 | [评价器](https://github.com/gabrielireland/GeoNatureAgent_Benchmark/blob/main/geoagentbench/scoring.py) | 是：仓库/指定父目录响应确认 | 否：本次只保存目录JSON/部分README至work；没有任务/GT/scorer资产下载；否 |

## 后续记录规则

本次未运行新Agent或官方评价器。后续审计记录必须写明任务/轨迹ID、数据与环境版本、scorer commit、rubric、模型配置、原分数、独立标签与争议裁决。新增实证结果单独追加，不把本文件的C级假设改写成既成事实。
