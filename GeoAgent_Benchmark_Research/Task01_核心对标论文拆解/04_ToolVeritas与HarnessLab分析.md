# 论文设计与公开实现

## 可获得性与版本

v1 p.9 Availability仅承诺将发布，未给工具仓库。2026-11-24查到作者组织的[论文配套仓库](https://github.com/CoreThink-AI/benchmarking-the-benchmarks)，根README明确关联论文，并链接两个子项目及Google Drive轨迹包。已克隆并静态检查上述提交；未安装、未运行。不能把2026年后续公开代码视为v1实验当时的完全相同版本。

官方独立仓库另有 [Tool-Veritas](https://github.com/CoreThink-AI/Tool-Veritas) 与 [Harness Lab](https://github.com/CoreThink-AI/harness-lab-oss)。本次代码分析基于配套仓库内的版本，不混用独立repo的行号。Drive下载链接存在，但未下载和核验压缩包，不宣称已获得论文逐轨迹判定数据。

## Tool-Veritas

【论文事实】配置式任务t=(q,s0,A,G,J)，16领域内以事实状态谓词为硬门，LLM仅评通信质量等定性标准；记录动作、工具响应、状态、门结果、修复及Judge输出（§3.8，pp.4–5，表1）。验证限于70任务×6模型，非地学环境。

【源码事实】输入TestCase JSON/JSONL，包含environment、interaction、execution_layer；工具、MCP及领域通过configs与registry加载。core/substrate/sandbox.py实现内存mock世界，并非真实GIS或真实银行业务环境。输出单case结果JSON以及workflow.log、workflow.jsonl。代码入口main.py，组织见Tool-Veritas/README.md。

| 模块 | 静态核查位置（相对官方repo） | 已确认实现 |
| --- | --- | --- |
| 运行与工具别名 | Tool-Veritas/benchmark/runtime/benchmark_runner.py，_build_tool_equivalence、_on_turn_complete | 按底层handler身份归并同一函数的工具别名；逐轮硬门；这不等于任意语义等价GIS流程识别 |
| 硬门 | Tool-Veritas/benchmark/gates/gating_engine.py，evaluate_turn、_check_execution_rules | 最大调用次数、required_tools、是否允许空工具轮、领域状态检查；规则失败直接返回，状态失败可进入修复窗口 |
| 状态判据 | Tool-Veritas/benchmark/gates/state_checker.py，check_filesystem等 | 文件存在、不存在、contains、equals等；确定性不自动消除过严GT或错误断言 |
| Judge整合 | Tool-Veritas/evaluator/evaluator/integration/__init__.py，evaluate_run、build_evaluation_result | 默认门通过后调用Judge；最终有Judge结果时passed=gates_all AND SUCCESS；关闭Judge时按门结果返回 |
| Judge策略 | Tool-Veritas/evaluator/evaluator/core/scoring.py，decide_label；core/pipeline.py | 明确失败条件优先、成功条件、可选部分分阈值；pipeline按metadata使用0.85或分支条件0.90。属于当前代码配置，不能写成论文统一阈值 |

GT既有初始状态和hard_state_checks，也有required_tools与定性grading_instructions。评估配置允许强制Judge运行；在已查整合函数中，有Judge结果时仍与gates_all合取，不能因为存在eval-force参数就断言LLM能推翻硬门。BenchmarkRunner设置evaluate_samples=3，Judge可多次投票，但这不是论文23次LiveMCPBench重跑。

修复逻辑涉及跨轮窗口与auto_recovery_state注入。必须分别记录Agent真实修复与系统注入的恢复，不能将注入后的状态算作Agent原本就完成。公开代码检查了工具等价别名，仍有required_tools规则；语义不同但结果等价的算法可能被拒绝，这是需用对照用例核验的机制风险，未作运行实验不判定它已造成实际错误。

## Harness Lab

【论文事实】论文描述7个family、21个suite变体；保留每个原生runner与evaluator，支持原始材料保存、首失败轮定位、成对比较、选择重试及独立人工标签（§3.9，pp.5–6，表2）。统一的是运行与诊断接口，不是跨基准同一个成功语义或统一可比分数。

【源码事实】harness-lab-oss/apps/api为FastAPI控制面，apps/runner为Python执行worker，apps/web为Next.js界面；packages、vendors存适配和固定上游包装。apps/api/app/store.py维护artifact和人工标签；bfcl_turn_diagnostics.py解释BFCL状态不匹配；main.py暴露查询与人工判定接口。SOURCE_SNAPSHOT.md明确公共版只保留BFCL v4、TAU2 Retail、MCP-Atlas、LiveMCPBench四类，私有历史、数据库、日志、原始审计工作目录未复制。公开目录数不能当作论文所有21变体已公开可跑的证据。

输入为suite、模型endpoint、运行参数、基准任务和原runner；输出为原始成绩文件、轨迹、诊断、比较视图和人工overlay。运行同一配置不保证外部API或模型端点稳定。Selective retry会重新生成病例并重新评分，适合定位临时失败；用于正式比较时必须保留原始全量运行和重试策略，否则可能产生挑选最好结果的偏差。

## 复现边界与统一评分判断

harness-lab-oss/reproducibility/arxiv-2607.02577/README.md及reported_claims.json明确：缺少权威496行判定导出和23轮原始分数向量，仅重算汇总数；均值、标准差仅保留论文报告值。成功执行make reproduce-paper也不能代表逐轨迹复现成功。本次只阅读源码，未执行该命令。

Tool-Veritas建立本工具内部的评分政策；Harness Lab保留各Benchmark官方评分。这两者都没有证明不同任务分布的分数可以直接做公平排行榜。对地学迁移，应先统一证据记录与独立判据，再决定是否存在共同可比的测量对象。


依据：仓库英文原稿 [PDF](../../论文翻译/Benchmarking%20the%20Benchmarks/英文原论文.pdf)、[逐页英文](../../论文翻译/Benchmarking%20the%20Benchmarks/英文原文_逐页.md)；页码均为 PDF 自身页码（1–12）。[arXiv v1](https://arxiv.org/abs/2607.02577v1)。
标记约定：【论文事实】指作者报告；【源码事实】指静态检查所得；【分析】指本次判断；【迁移假设／建议】不代表已在地学 Benchmark 中验证。
官方源码基线：[CoreThink-AI/benchmarking-the-benchmarks](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/tree/09576dbee8f0c44896317edc82ae21ec4de8a6db)，提交 09576dbee8f0c44896317edc82ae21ec4de8a6db。本次未安装工具、未调用模型、未执行 Agent 实验。


## 固定版本源码定位

| 函数 | 官方固定提交链接 |
| --- | --- |
| _build_tool_equivalence | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/benchmark/runtime/benchmark_runner.py#L220) |
| evaluate_turn | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/benchmark/gates/gating_engine.py#L121) |
| check_filesystem | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/benchmark/gates/state_checker.py#L62) |
| build_evaluation_result | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/evaluator/evaluator/integration/__init__.py#L59) |
| evaluate_run | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/evaluator/evaluator/integration/__init__.py#L93) |
| decide_label | [源码](https://github.com/CoreThink-AI/benchmarking-the-benchmarks/blob/09576dbee8f0c44896317edc82ae21ec4de8a6db/Tool-Veritas/evaluator/evaluator/core/scoring.py#L126) |

【源码风险观察】build_evaluation_result在gate_results为空时将gates_all设为True；这只是条件分支事实。正常运行是否允许无门任务、是否能被输入校验阻断，需要离线负例检查，本次未运行，不能据此宣布已经发现可利用的误判。
