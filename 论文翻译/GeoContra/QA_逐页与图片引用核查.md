# GeoContra：文件与逐页视觉核查报告

- 原始 PDF 文件：`Xiao 等 - 2026 - GeoContra From Fluent GIS Code to Verifiable Spatial Analysis with Geography-Grounded Repair.pdf`
- 原稿页数：**19**；逐页截图：**19**
- 图表/算法/清单截图：**16**，分类：figure=5, algorithm=6, table=5
- PDF 逐页提取总字符数：**50,922**；空白文本页：[]
- Markdown 文件数量：**3**；图片相对路径引用数量：**69**
- 机器可验证问题：**0**

## 自检方式

1. 使用 PyMuPDF 打开 PDF，逐页提取文本并渲染原稿页图像；对照实际页数，不以目录或印刷页码推测。
2. 检测 Figure、Table、Algorithm 与 Listing 标题，裁切相应图表；有些复杂表格或代码跨页时，以完整逐页原稿截图作为无损视觉依据。
3. 检查每个生成图像能否解码，并检查全部 Markdown 图片相对路径是否存在。
4. 论文的公式、参考文献、正文、附录以及代码示例由英文逐页全文与原稿截图完整覆盖；对有跨栏或文本流顺序异常的页面，以整页截图为准。

## 译文完成度与重要限制

**中文精读版并非逐句全文译本**：完整翻译摘要并详述论文核心论证、方法和结果；完整英文正文、参考文献和附录已提取，但尚未对英文所有段落逐句翻译。这一点会在交付时明确说明，不将仅有英文的页面标作完成中文翻译。

PDF 提取工具可能把上下标、数学字体、多栏表格文字或分词换行与正文混在一起，因此所有复杂公式和表格均需以对应原稿页图复核。当前已进行图表截图接触表视觉抽查；不能据此宣称逐字人工校对了每个公式、引文与页内数值。

## 异常清单

无失效的图片路径或无法解码的图片。

## 图表索引

| 原文页 | 类型 | 编号 | 图片文件 | 中文描述 |
|---:|---|---:|---|---|
| 5 | figure | 1 | `images/figure-1-p05.png` | GeoContra 的整体框架与地理契约驱动的修复循环 |
| 6 | algorithm | 1 | `images/algorithm-1-p06.png` | 构建 GeoContra-Real 数据集的算法 |
| 7 | figure | 2 | `images/figure-2-p07.png` | 静态、运行时和语义验证的详细修复引擎 |
| 8 | algorithm | 2 | `images/algorithm-2-p08.png` | 验证器引导的程序生成与修复 |
| 8 | algorithm | 3 | `images/algorithm-3-p08.png` | 静态检查器 |
| 9 | algorithm | 4 | `images/algorithm-4-p09.png` | 运行时检查器 |
| 10 | algorithm | 5 | `images/algorithm-5-p10.png` | 任务语义验证器 |
| 10 | algorithm | 6 | `images/algorithm-6-p10.png` | 生成修复提示 |
| 12 | table | 1 | `images/table-1-p12.png` | GeoContra-Real 任务家族与难度组成 |
| 12 | table | 2 | `images/table-2-p12.png` | 闭源模型整体实验结果 |
| 13 | figure | 3 | `images/figure-3-p13.png` | 各任务族的空间正确率提升 |
| 14 | table | 3 | `images/table-3-p14.png` | 开源模型在 300 个任务上的空间正确率 |
| 14 | figure | 4 | `images/figure-4-p14.png` | 11 个开源模型的空间正确率对比 |
| 15 | figure | 5 | `images/figure-5-p15.png` | 最终静态、运行时与语义违规数量 |
| 16 | table | 4 | `images/table-4-p16.png` | 失败与修复案例分析 |
| 18 | table | 5 | `images/table-5-p18.png` | 大波士顿 15 个研究区的数据多样性统计 |
