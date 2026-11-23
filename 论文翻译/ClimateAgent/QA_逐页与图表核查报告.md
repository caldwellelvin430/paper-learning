# ClimateAgent — QA 逐页与图表完整性核查报告

## 结构与文件覆盖
- 源 PDF：`原始论文.pdf`；PDF 原始页数与逐页图像一致：**53 页**。
- 逐页英文文本：53 页，每页均包含可提取文字。
- 原稿截图：53 张，对应每页，不因裁图失败而丢弃图文。
- 独立图表区域截图：20 张，按 PDF 内带编号 Figure/Table 的图题识别。
- 图题/表题自动识别：10 个 Figure、10 个 Table。
- 参考文献：在逐页英文原文中保留完整，另存带页码英文参考文献提取件。
- 中文：重点章节及摘要已人工组织成中文学术译稿；**未完成全 146 页逐段完整中文翻译，不能标注为全文精校译文**。

## 页级文本核验
| PDF 页码 | 英文字符数 | 嵌入图像资源 | 图片/表格标题数 | 截图 |
|---:|---:|---:|---:|---|
| 1 | 3005 | 0 | 0 | [第1页](./source_pages/page-001.jpg) |
| 2 | 5413 | 0 | 0 | [第2页](./source_pages/page-002.jpg) |
| 3 | 4630 | 0 | 0 | [第3页](./source_pages/page-003.jpg) |
| 4 | 4923 | 0 | 0 | [第4页](./source_pages/page-004.jpg) |
| 5 | 2852 | 1 | 1 | [第5页](./source_pages/page-005.jpg) |
| 6 | 4146 | 0 | 0 | [第6页](./source_pages/page-006.jpg) |
| 7 | 4045 | 0 | 0 | [第7页](./source_pages/page-007.jpg) |
| 8 | 2304 | 0 | 0 | [第8页](./source_pages/page-008.jpg) |
| 9 | 4043 | 0 | 0 | [第9页](./source_pages/page-009.jpg) |
| 10 | 3925 | 0 | 0 | [第10页](./source_pages/page-010.jpg) |
| 11 | 3819 | 0 | 0 | [第11页](./source_pages/page-011.jpg) |
| 12 | 3810 | 0 | 2 | [第12页](./source_pages/page-012.jpg) |
| 13 | 4734 | 0 | 0 | [第13页](./source_pages/page-013.jpg) |
| 14 | 2413 | 21 | 1 | [第14页](./source_pages/page-014.jpg) |
| 15 | 4199 | 0 | 1 | [第15页](./source_pages/page-015.jpg) |
| 16 | 3199 | 0 | 4 | [第16页](./source_pages/page-016.jpg) |
| 17 | 4014 | 0 | 0 | [第17页](./source_pages/page-017.jpg) |
| 18 | 3761 | 0 | 0 | [第18页](./source_pages/page-018.jpg) |
| 19 | 4081 | 0 | 0 | [第19页](./source_pages/page-019.jpg) |
| 20 | 3692 | 0 | 0 | [第20页](./source_pages/page-020.jpg) |
| 21 | 1090 | 0 | 0 | [第21页](./source_pages/page-021.jpg) |
| 22 | 3193 | 0 | 0 | [第22页](./source_pages/page-022.jpg) |
| 23 | 2963 | 0 | 0 | [第23页](./source_pages/page-023.jpg) |
| 24 | 2874 | 0 | 0 | [第24页](./source_pages/page-024.jpg) |
| 25 | 2645 | 0 | 0 | [第25页](./source_pages/page-025.jpg) |
| 26 | 2932 | 0 | 0 | [第26页](./source_pages/page-026.jpg) |
| 27 | 892 | 0 | 0 | [第27页](./source_pages/page-027.jpg) |
| 28 | 3128 | 0 | 0 | [第28页](./source_pages/page-028.jpg) |
| 29 | 1474 | 0 | 0 | [第29页](./source_pages/page-029.jpg) |
| 30 | 3233 | 0 | 0 | [第30页](./source_pages/page-030.jpg) |
| 31 | 324 | 0 | 0 | [第31页](./source_pages/page-031.jpg) |
| 32 | 2511 | 1 | 1 | [第32页](./source_pages/page-032.jpg) |
| 33 | 2066 | 1 | 0 | [第33页](./source_pages/page-033.jpg) |
| 34 | 2848 | 0 | 0 | [第34页](./source_pages/page-034.jpg) |
| 35 | 2510 | 0 | 0 | [第35页](./source_pages/page-035.jpg) |
| 36 | 3320 | 0 | 0 | [第36页](./source_pages/page-036.jpg) |
| 37 | 2519 | 0 | 0 | [第37页](./source_pages/page-037.jpg) |
| 38 | 3244 | 0 | 0 | [第38页](./source_pages/page-038.jpg) |
| 39 | 3498 | 0 | 1 | [第39页](./source_pages/page-039.jpg) |
| 40 | 2315 | 1 | 1 | [第40页](./source_pages/page-040.jpg) |
| 41 | 3910 | 0 | 0 | [第41页](./source_pages/page-041.jpg) |
| 42 | 3829 | 0 | 1 | [第42页](./source_pages/page-042.jpg) |
| 43 | 3794 | 0 | 0 | [第43页](./source_pages/page-043.jpg) |
| 44 | 4772 | 0 | 1 | [第44页](./source_pages/page-044.jpg) |
| 45 | 3398 | 0 | 0 | [第45页](./source_pages/page-045.jpg) |
| 46 | 2458 | 0 | 0 | [第46页](./source_pages/page-046.jpg) |
| 47 | 2941 | 0 | 0 | [第47页](./source_pages/page-047.jpg) |
| 48 | 3013 | 0 | 1 | [第48页](./source_pages/page-048.jpg) |
| 49 | 1278 | 2 | 2 | [第49页](./source_pages/page-049.jpg) |
| 50 | 3867 | 0 | 0 | [第50页](./source_pages/page-050.jpg) |
| 51 | 4189 | 0 | 2 | [第51页](./source_pages/page-051.jpg) |
| 52 | 3039 | 0 | 0 | [第52页](./source_pages/page-052.jpg) |
| 53 | 3685 | 0 | 1 | [第53页](./source_pages/page-053.jpg) |

## 裁图方式的限制
PDF 的 Figure 与 Table 可能由矢量、文字与嵌入图片混合构成，因此截图采用原版页面的宽区域裁取以防内容被拆散。宽区域有时会包含相邻段落，少数跨页表可能无法由一张裁图独立呈现；原始页截图已作为保真兜底，不能以“裁图数量”等同于所有逻辑图表的严格人工定稿数量。

## 翻译覆盖及科研使用边界
本次交付含全文英文提取、原稿截图、参考文献及部分中文学术翻译/译述。尤其是公式、超长表格、附录提示词、代码和参考文献尚未逐句人工汉译。对于论文的关键数值、推导与科学结论，引用时应对照 PDF 原文。