# DS-1000：面向数据科学代码生成的真实且可靠的基准 · 逐页核查报告

- 原稿 PDF：**27 页**。
- 已保存原稿页图：**27 张**。
- 原始图表截图：**31 幅图、8 张表**。
- Markdown 中图片引用：**39 处**，未发现失效或缺失。
- 英文全文已逐页提取（两种文本顺序，原始图内字形同时保留在页图中）。
- 译文范围：第 1–6 节与附录 A/B/C 的研究内容已译述；31 幅图中的原始代码、英文问题和堆栈信息仍以原稿截图为准。

## 翻译及视觉检查说明

逐页检查了渲染总览图、主要图表裁切及图表与 Markdown 的引用关系；特别核验跨页图表与同一页的多幅插图。程序化自检包含 PDF 页数、截图数量、文件尺寸、图片内容与相对路径。

**重要限制：** 代码、API 调用字面量、URL、原始技术提示词、图表内英文及参考文献保留原文。中文文档不是对这些英文字段的逐字符翻译；如需验证原文完整性，请对照逐页英文文本和原始 PDF。图中非可选取文字不会被 OCR 重写。

## 每页内容与图表索引

| PDF 页码 | 原稿页图 | 截取的图表 |
|---:|---|---|
| 1 | [第1页](./source_pages/page-001.jpg) | — |
| 2 | [第2页](./source_pages/page-002.jpg) | 图1 |
| 3 | [第3页](./source_pages/page-003.jpg) | 图2 |
| 4 | [第4页](./source_pages/page-004.jpg) | 表1, 表2 |
| 5 | [第5页](./source_pages/page-005.jpg) | 表3 |
| 6 | [第6页](./source_pages/page-006.jpg) | 表4 |
| 7 | [第7页](./source_pages/page-007.jpg) | 表5 |
| 8 | [第8页](./source_pages/page-008.jpg) | 表6 |
| 9 | [第9页](./source_pages/page-009.jpg) | — |
| 10 | [第10页](./source_pages/page-010.jpg) | — |
| 11 | [第11页](./source_pages/page-011.jpg) | — |
| 12 | [第12页](./source_pages/page-012.jpg) | 表7 |
| 13 | [第13页](./source_pages/page-013.jpg) | 表8, 图3, 图4, 图6 |
| 14 | [第14页](./source_pages/page-014.jpg) | 图5, 图7 |
| 15 | [第15页](./source_pages/page-015.jpg) | 图8 |
| 16 | [第16页](./source_pages/page-016.jpg) | 图9, 图10 |
| 17 | [第17页](./source_pages/page-017.jpg) | 图11, 图12 |
| 18 | [第18页](./source_pages/page-018.jpg) | 图13, 图14 |
| 19 | [第19页](./source_pages/page-019.jpg) | 图15, 图16 |
| 20 | [第20页](./source_pages/page-020.jpg) | 图17, 图18 |
| 21 | [第21页](./source_pages/page-021.jpg) | 图19, 图20 |
| 22 | [第22页](./source_pages/page-022.jpg) | 图21, 图22 |
| 23 | [第23页](./source_pages/page-023.jpg) | 图23, 图24 |
| 24 | [第24页](./source_pages/page-024.jpg) | 图25, 图26 |
| 25 | [第25页](./source_pages/page-025.jpg) | 图27, 图28 |
| 26 | [第26页](./source_pages/page-026.jpg) | 图29, 图30 |
| 27 | [第27页](./source_pages/page-027.jpg) | 图31 |

## 跨页与特殊情况

正文中出现 Figure 16 等数字的是对后续附录图的交叉引用，而非本页图题；这些附录图的截图已按实际图体页定位。**图 6** 的真实图体位于第 14 页。

## 图表原文索引

| 图表 | 原论文页码（图题） | 图片文件 |
|---|---:|---|
| 图1 | 2 | [截图](./images/figure-01.png) |
| 图2 | 3 | [截图](./images/figure-02.png) |
| 表1 | 4 | [截图](./images/table-01.png) |
| 表2 | 4 | [截图](./images/table-02.png) |
| 表3 | 5 | [截图](./images/table-03.png) |
| 表4 | 6 | [截图](./images/table-04.png) |
| 表5 | 7 | [截图](./images/table-05.png) |
| 表6 | 8 | [截图](./images/table-06.png) |
| 表7 | 12 | [截图](./images/table-07.png) |
| 表8 | 13 | [截图](./images/table-08.png) |
| 图3 | 13 | [截图](./images/figure-03.png) |
| 图4 | 13 | [截图](./images/figure-04.png) |
| 图6 | 13（图体第 14 页） | [截图](./images/figure-06.png) |
| 图5 | 14 | [截图](./images/figure-05.png) |
| 图7 | 14 | [截图](./images/figure-07.png) |
| 图8 | 15 | [截图](./images/figure-08.png) |
| 图9 | 16 | [截图](./images/figure-09.png) |
| 图10 | 16 | [截图](./images/figure-10.png) |
| 图11 | 17 | [截图](./images/figure-11.png) |
| 图12 | 17 | [截图](./images/figure-12.png) |
| 图13 | 18 | [截图](./images/figure-13.png) |
| 图14 | 18 | [截图](./images/figure-14.png) |
| 图15 | 19 | [截图](./images/figure-15.png) |
| 图16 | 19 | [截图](./images/figure-16.png) |
| 图17 | 20 | [截图](./images/figure-17.png) |
| 图18 | 20 | [截图](./images/figure-18.png) |
| 图19 | 21 | [截图](./images/figure-19.png) |
| 图20 | 21 | [截图](./images/figure-20.png) |
| 图21 | 22 | [截图](./images/figure-21.png) |
| 图22 | 22 | [截图](./images/figure-22.png) |
| 图23 | 23 | [截图](./images/figure-23.png) |
| 图24 | 23 | [截图](./images/figure-24.png) |
| 图25 | 24 | [截图](./images/figure-25.png) |
| 图26 | 24 | [截图](./images/figure-26.png) |
| 图27 | 25 | [截图](./images/figure-27.png) |
| 图28 | 25 | [截图](./images/figure-28.png) |
| 图29 | 26 | [截图](./images/figure-29.png) |
| 图30 | 26 | [截图](./images/figure-30.png) |
| 图31 | 27 | [截图](./images/figure-31.png) |
