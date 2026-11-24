"""Generate research navigation from literature_catalog.yaml; never edit paper assets.

Requires Python 3.10+ and PyYAML. Run from any directory, with --check for read-only QA.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import unicodedata
from urllib.parse import quote, unquote, urlsplit

import yaml

RESEARCH = "GeoAgent_Benchmark_Research"
CATALOG = f"{RESEARCH}/文献元数据/literature_catalog.yaml"
CSV_PATH = f"{RESEARCH}/文献元数据/literature_catalog.csv"
NORM = f"{RESEARCH}/文献分类与优先级规范.md"
HEADER = "<!-- 自动生成：仅修改 literature_catalog.yaml，再运行 scripts/generate_literature_navigation.py。 -->\n\n"
REQUIRED = (
    "paper_id paper_title paper_short_name benchmark_name year publication source_url "
    "primary_category reading_priority priority_reason classification_reason research_value "
    "research_role secondary_tags measurement_target evaluation_mechanism ground_truth_type "
    "reproducibility feasibility_reason open_source_status resource_stages evidence_location "
    "verification_status reading_focus local_path chinese_primary english_primary "
    "translation_scope original_source_file review_scope record_path checked_on"
).split()


def cell(value):
    return str(value).replace("|", "&#124;").replace("\r", "").replace("\n", "<br>")


def table(headers, rows):
    return "| " + " | ".join(headers) + " |\n|" + "|".join("---" for _ in headers) + "|\n" + "".join(
        "| " + " | ".join(cell(x) for x in row) + " |\n" for row in rows
    ) + "\n"


def link(label, target, current):
    if urlsplit(str(target)).scheme in ("https", "http"):
        return f"[{cell(label)}]({target})"
    relative = os.path.relpath(target, str(Path(current).parent)).replace("\\", "/")
    return f"[{cell(label)}]({quote(relative, safe='/._-')})"


def sorted_papers(papers):
    return sorted(papers, key=lambda p: (p["reading_priority"], p["relevance_order"], p["paper_id"]))


def asset_links(paths, label, current):
    return " · ".join(link(label if len(paths) == 1 else f"{label}{i+1}", p, current) for i, p in enumerate(paths)) or "未归档独立入口"


def english(p, current):
    label = "本地摘要" if "仅摘要" in p["english_scope"] else "本地原文"
    return link(label, p["english_primary"], current) + " · " + link("官方", p["source_url"], current)


def chinese(p, current):
    return link(p["translation_scope"], p["chinese_primary"], current)


def pdf(p, current):
    return asset_links(p["pdf_paths"], "PDF", current) if p["pdf_paths"] else "本地原始 PDF 缺失（见官方原文）"


def reading_table(papers, current):
    return table(["论文名称", "年份", "阅读优先级", "研究价值", "中文译稿", "英文原文", "PDF"], [
        [link(p["paper_short_name"], p["record_path"], current), p["year"], p["reading_priority"],
         p["research_value"], chinese(p, current), english(p, current), pdf(p, current)]
        for p in sorted_papers(papers)
    ])


def priority_nav(data, current):
    counts = collections.Counter(p["reading_priority"] for p in data["papers"])
    return table(["优先级", "数量", "阅读要求", "清单"], [
        [k, counts[k], v, link(k + " 阅读清单", f"{RESEARCH}/阅读优先级/{k}.md", current)]
        for k, v in data["priority_definitions"].items()
    ])


def research_entries(current):
    return "\n".join("- " + link(label, path, current) for label, path in [
        ("文献总索引", f"{RESEARCH}/文献总索引.md"),
        ("Benchmark 实证审计可行性矩阵", f"{RESEARCH}/实证审计可行性/Benchmark可行性矩阵.md"),
        ("分类规范 v1.0（原始规范）", NORM),
        ("YAML 元数据（唯一数据源）", CATALOG), ("CSV 元数据（自动导出）", CSV_PATH),
        ("分类维护说明", f"{RESEARCH}/分类维护说明.md"),
        ("本次分类整改验收报告", f"{RESEARCH}/QA_文献分类整改验收报告.md"),
    ]) + "\n\n"


def build(data):
    papers, categories = data["papers"], data["categories"]
    cc = collections.Counter(p["primary_category"] for p in papers)
    pc = collections.Counter(p["reading_priority"] for p in papers)
    rc = collections.Counter(p["reproducibility"] for p in papers)
    bycat = lambda c: [p for p in papers if p["primary_category"] == c]
    result = {}

    def emit(path, text):
        result[path] = (HEADER + text.rstrip() + "\n").encode("utf-8")

    def categories_nav(current):
        return table(["类别", "论文数量", "研究用途", "分类入口"], [
            [c["code"] + "｜" + c["name"], cc[c["code"]], c["research_use"],
             link("分类与精读记录", f"{RESEARCH}/{c['directory']}/README.md", current)] for c in categories
        ])

    def stats():
        return (f"共 **{len(papers)} 篇论文**，对应 {len(papers)} 个论文目录；分类与优先级统计由统一 YAML 自动生成。"
                f"最近核验：{data['checked_on']}。\n\n"
                + table(["统计项", "分布"], [["主类别", "；".join(f"{c['code']}：{cc[c['code']]}" for c in categories)],
                    ["阅读优先级", "；".join(f"{k}：{pc[k]}" for k in data["priority_definitions"])],
                    ["实证可行性（与阅读优先级独立）", "；".join(f"{k}：{rc[k]}" for k in data["feasibility_definitions"])]])
                + "原文核验指面向分类的摘要、方法、评价、实验及局限定向核验；不等于全部附录或源码已审计。"
                  "中文入口注明译稿范围；文件名中的“全文”不作为全文覆盖证明。\n\n")

    current = "README.md"
    text = ("# paper-learning\n\n## 研究方向\n\n" + data["research_direction"] + "。"
            "核心对标为《Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation》。"
            "先识别指标实际测量对象与评价器判据，再用独立证据验证评分风险，依据实证结果讨论改进。\n\n"
            "## 文献库统计\n\n" + stats() + "## 快速分类导航\n\n" + categories_nav(current)
            + "以下按 P0 → P1 → P2 → P3 排列；同一优先级内按当前研究相关性排序。论文名称进入逐篇研究记录，中文译稿可直接打开。\n\n")
    for c in categories:
        text += f"## {c['code']}｜{c['name']}\n\n" + reading_table(bycat(c["code"]), current)
    text += "## 阅读优先级导航\n\n" + priority_nav(data, current)
    text += "## 专题研究入口\n\n" + research_entries(current)
    text += "## 其他资源\n\n" + "\n".join("- " + link(label, path, current) for label, path in [
        ("论文阅读导航（含图表与核查报告）", "论文翻译/README.md"),
        ("科研研究导航", f"{RESEARCH}/README.md"),
        ("GitHub 上传与克隆教程", "教学/GitHub上传与克隆教程.md"),
    ]) + "\n"
    emit(current, text)

    current = "论文翻译/README.md"
    text = ("# 论文阅读导航\n\n" + stats() + "此处服务于原文和中文稿阅读。研究理由、测量对象和核验状态见逐篇分类记录；"
            "图表与核查报告入口沿用原目录，不改动原稿及图片路径。\n\n"
            + link("科研分类首页", f"{RESEARCH}/README.md", current) + " · " + link("仓库首页", "README.md", current) + "\n\n")
    for c in categories:
        text += f"## {c['code']}｜{c['name']}\n\n"
        rows = []
        for p in sorted_papers(bycat(c["code"])):
            used = {p["chinese_primary"], p["english_primary"], *p["pdf_paths"], *p["figure_paths"], *p["qa_paths"], *p["reading_notes"]}
            extras = [link(a["label"], a["path"], current) for a in p["legacy_links"] if a["path"] not in used]
            notes = asset_links(p["reading_notes"], "阅读说明", current) + (" · " + " · ".join(extras) if extras else "")
            rows.append([link(p["paper_short_name"], p["record_path"], current), p["reading_priority"], chinese(p, current),
                         english(p, current), pdf(p, current), asset_links(p["figure_paths"], "图表/原页", current),
                         asset_links(p["qa_paths"], "核查", current), notes])
        text += table(["论文", "优先级", "中文稿及范围", "英文原文", "PDF", "图表", "核查报告", "阅读说明与已有材料"], rows)
    text += "## 其他已有资源\n\n" + "\n".join("- " + link(label, path, current) for label, path in [
        ("Kim / Bhat 资料说明", "论文翻译/Kim_Bhat资料说明.md"),
        ("GitHub 上传与克隆教程", "教学/GitHub上传与克隆教程.md"),
    ]) + "\n"
    emit(current, text)

    current = f"{RESEARCH}/README.md"
    core = next(p for p in papers if p["paper_short_name"] == data["core_reference"])
    text = ("# GeoAgent Benchmark 科研文献导航\n\n" + data["research_direction"] + "。"
            "分类记录服务于研究设计、精读顺序与审计对象筛选；不将文献相关性视为可复现证据。\n\n"
            "## 文献统计与分类\n\n" + stats() + categories_nav(current)
            + "## 核心研究文献\n\n" + reading_table(bycat("A"), current)
            + "## Benchmark 审计方法\n\n核心对标：" + link(core["paper_title"], core["record_path"], current) + "。\n\n"
            + reading_table(bycat("B"), current)
            + "## 阅读优先级\n\n" + priority_nav(data, current)
            + "## 实证审计与评价指标 / Ground Truth\n\n"
            + "实证可行性单独记录任务、GT、轨迹、产物、评价器、环境/API及独立核验条件。R1 不表示已运行；RU 不表示资源不存在。\n\n")
    research_paths = [
        ("Benchmark 可行性矩阵", f"{RESEARCH}/实证审计可行性/Benchmark可行性矩阵.md"),
        ("Task01：核心对标论文拆解与审计方法", f"{RESEARCH}/Task01_核心对标论文拆解/QA_Task01_验收报告.md"),
        ("Task02：评价指标、测量对象与 GT 研究", f"{RESEARCH}/Task02_地学Benchmark评价指标体系/README.md"),
        ("Task02：指标完整汇总", f"{RESEARCH}/Task02_地学Benchmark评价指标体系/02_完整评价指标汇总.csv"),
    ]
    text += "\n".join("- " + link(a, b, current) for a, b in research_paths) + "\n\n"
    text += "## 分类规范与维护\n\n" + research_entries(current)
    text += ("统一数据源为 YAML；CSV、三个 README、类别与优先级索引和逐篇记录由脚本生成。"
             "未来新增文献先核实原文并更新 YAML，再生成和检查。原始论文目录保持原位。"
             "论文目录内随包保存的文献分类记录.yaml属于历史初步记录，不参与当前导航生成。\n\n"
             "## 原有研究材料\n\n"
             "Task01、Task02 成果及研究分析矩阵保留。早期矩阵属于阶段性研究记录，分类与阅读优先级以本次 YAML 为准。\n\n")
    for label, path in [("研究背景与目标", f"{RESEARCH}/00_研究背景与目标.md"),
                        ("原有研究分析矩阵", f"{RESEARCH}/研究分析矩阵"),
                        ("分类核验与变更记录", f"{RESEARCH}/03_文献分类调整记录.md"),
                        ("论文阅读与图表导航", "论文翻译/README.md"),
                        ("GitHub 上传与克隆教程", "教学/GitHub上传与克隆教程.md")]:
        text += "- " + link(label, path, current) + "\n"
    emit(current, text)

    current = f"{RESEARCH}/文献总索引.md"
    text = "# 文献总索引\n\n" + stats() + "每篇只有一个主类别。P 与 R 独立；以下每行均可进入包含原文证据、分类理由和重点章节的独立记录。\n\n"
    for c in categories:
        text += f"## {c['code']}｜{c['name']}\n\n" + table(
            ["论文 / 结构化记录", "实际 Benchmark", "年份 / 平台", "P", "R", "分类理由", "阅读重点", "原文证据", "资料目录"], [
                [link(p["paper_short_name"], p["record_path"], current), p["benchmark_name"], str(p["year"]) + " / " + p["publication"],
                 p["reading_priority"], p["reproducibility"], p["classification_reason"], p["reading_focus"], p["evidence_location"],
                 link("原论文目录", p["local_path"], current)] for p in sorted_papers(bycat(c["code"]))])
    emit(current, text)

    for c in categories:
        current = f"{RESEARCH}/{c['directory']}/README.md"
        text = (f"# {c['code']}｜{c['name']}\n\n共 {cc[c['code']]} 篇。{c['research_use']}。"
                "分类依据为 v1.0；兼有多项贡献的论文以研究用途确定唯一主类别，次要作用写入标签。\n\n"
                + reading_table(bycat(c["code"]), current) + "## 分类理由与重点章节\n\n"
                + table(["论文", "分类理由", "重点阅读", "P / R", "原文出处"], [
                    [link(p["paper_short_name"], p["record_path"], current), p["classification_reason"], p["reading_focus"],
                     p["reading_priority"] + " / " + p["reproducibility"], p["evidence_location"]] for p in sorted_papers(bycat(c["code"]))])
                + link("返回科研导航", f"{RESEARCH}/README.md", current) + "\n")
        emit(current, text)

    for priority, definition in data["priority_definitions"].items():
        current = f"{RESEARCH}/阅读优先级/{priority}.md"
        selected = [p for p in papers if p["reading_priority"] == priority]
        text = f"# {priority} 阅读清单\n\n{definition}。共 {len(selected)} 篇。阅读顺序不代表实验可行性排序。\n\n"
        text += table(["论文", "主类别", "优先级理由", "重点阅读章节", "实证可行性", "中文稿"], [
            [link(p["paper_short_name"], p["record_path"], current), p["primary_category"], p["priority_reason"],
             p["reading_focus"], p["reproducibility"], chinese(p, current)]
            for p in sorted(selected, key=lambda p: (p["primary_category"], p["relevance_order"]))])
        text += link("全部阅读优先级", f"{RESEARCH}/阅读优先级/README.md", current) + "\n"
        emit(current, text)
    current = f"{RESEARCH}/阅读优先级/README.md"
    emit(current, "# 阅读优先级\n\nP0–P3 衡量阅读必要性；实证可行性另用 R0/R1/R2/RU/N/A 管理。\n\n" + priority_nav(data, current))
    current = f"{RESEARCH}/02_核心文献阅读顺序.md"
    emit(current, "# 核心文献阅读顺序\n\n旧阅读顺序草案已由统一 YAML 的逐篇理由与优先级替代。先读核心对标，再按 A 类评价机制和 B 类方法对照阅读，"
         "随后阅读 P1 的专项与通用评分机制。可行性不决定阅读顺序。\n\n" + priority_nav(data, current))
    current = f"{RESEARCH}/03_文献分类调整记录.md"
    baseline_size = data.get("baseline_collection_size", len(papers))
    new_papers = [p for p in papers if p.get("ingestion_batch")]
    emit(current, "# 文献分类核验与调整记录\n\n" + f"核验日期：{data['checked_on']}。\n\n"
         + f"保留原有 {baseline_size} 篇的 A–G 初始映射，没有更改已有文献主类别；当前另纳入 {len(new_papers)} 篇新文献。"
         "以下列出容易因名称或次要贡献误归类的情况；不是新增类别。\n\n"
         + table(["论文", "主类别", "核验后的定位依据"], [
             [link(p["paper_short_name"], p["record_path"], current), p["primary_category"], p["classification_reason"]]
             for p in papers if p.get("ingestion_batch") or p["paper_short_name"] in ["GeoContra", "GeoAnalystBench", "HTAM_EarthAgent", "GeoMMBench_GeoMMAgent", "AgentSuite", "AgentJudgeBench", "GeoAgent"]])
         + "未来调整须在 YAML 逐篇写入原类别、原文证据与调整理由，再重新生成导航；禁止仅凭标题改类。\n")

    current = f"{RESEARCH}/实证审计可行性/Benchmark可行性矩阵.md"
    text = ("# Benchmark 实证审计可行性矩阵\n\n" + f"核验日期：{data['checked_on']}。包括全部 {len(papers)} 篇，N/A 明确表示当前非独立审计对象。"
            "作者的公开声明、链接可访问、文件已下载及实际运行分别记录。论文/PDF在本地不计实验资产下载。\n\n"
            + table(["等级", "数量", "判定条件"], [[k, rc[k], v] for k, v in data["feasibility_definitions"].items()])
            + "## 逐篇判定\n\n" + table(["论文", "类别 / 阅读优先级", "可行性", "实际依据与未完成事项", "开源状态"], [
                [link(p["paper_short_name"], p["record_path"], current), p["primary_category"] + " / " + p["reading_priority"],
                 p["reproducibility"], p["feasibility_reason"], p["open_source_status"]]
                for p in sorted(papers, key=lambda p: (p["primary_category"], p["relevance_order"]))])
            + "## 分项与证据阶段\n\n每篇独立记录另列十项条件和五阶段资源状态。R1 是进一步做小规模验证的候选，不是已经复现；"
              "未核查的条件保留 RU/未核查。现阶段没有完成小规模真实评分/重放验证，不授予 R0。\n")
    emit(current, text)

    for p in papers:
        current = p["record_path"]
        text = f"# {p['paper_short_name']}：文献分类记录\n\n"
        fields = [("完整英文标题", p["paper_title"]), ("仓库短名称", p["paper_short_name"]), ("实际 Benchmark 名称", p["benchmark_name"]),
                  ("年份与平台", str(p["year"]) + "；" + p["publication"]), ("原文网址", link("官方原文", p["source_url"], current)),
                  ("唯一主类别", p["primary_category"]), ("阅读优先级", p["reading_priority"]), ("阅读优先级理由", p["priority_reason"]),
                  ("分类理由", p["classification_reason"]), ("研究用途", "；".join(p["research_role"]) + "：" + p["research_value"]),
                  ("辅助标签", "；".join(p["secondary_tags"])), ("主要测量对象", p["measurement_target"]),
                  ("评价机制", p["evaluation_mechanism"]), ("Ground Truth 类型", p["ground_truth_type"]),
                  ("实证审计可行性", p["reproducibility"]), ("可行性依据", p["feasibility_reason"]),
                  ("开源状态", p["open_source_status"]), ("原文证据位置", p["evidence_location"]),
                  ("核验状态", p["verification_status"]), ("原文核验范围", "；".join(p["review_scope"])),
                  ("重点阅读章节", p["reading_focus"]), ("局限与研究边界", p["limitations_note"]),
                  ("归档英文页数", p["english_document_pages"]), ("核验日期", p["checked_on"]),
                  ("实际目录", link(p["local_path"], p["local_path"], current))]
        if p.get("edition_note"): fields.append(("版本注意", p["edition_note"]))
        text += table(["字段", "核查记录"], fields)
        text += "## 阅读材料\n\n" + table(["材料", "入口 / 状态"], [
            ("中文主入口及范围", chinese(p, current)), ("其他中文稿及范围", " · ".join(link(m["scope"], m["path"], current) for m in p["chinese_materials"])),
            ("英文原文", english(p, current) + "；" + p["english_scope"]), ("PDF", pdf(p, current)),
            ("图表与原页", asset_links(p["figure_paths"], "图表/原页", current)), ("核查报告", asset_links(p["qa_paths"], "核查", current)),
            ("阅读说明", asset_links(p["reading_notes"], "阅读说明", current)),
            ("用于核验的本地原文", link("归档原文", p["original_source_file"], current)),
        ])
        text += "## 原文核验与研究判断\n\n"
        text += ("论文事实：标题、任务/Benchmark定位、测量对象、评价机制及 GT 摘要来自上列英文原文位置；"
                 "测量对象字段概括评价操作，不把局部得分外推为完整地学能力。\n\n"
                 "研究判断：分类理由、研究用途、阅读优先级与阅读问题依据 v1.0 和当前研究方向确定；"
                 "阅读问题用于后续核验，不表示已经发现评价缺陷。局限记录区分作者范围说明与本研究尚缺的证据。\n\n")
        if p["paper_short_name"] == "Beyond the Final Answer":
            text += "本地英文材料仅摘要；本次另从 PMLR 官方全文 PDF 阅读方法与实验，未把外部缓存写回原论文目录。\n\n"
        text += "## 实证条件分项检查\n\n" + table(["条件", "实际核查状态"], p["resource_check_items"].items())
        stage_names = {"author_claim": "1 作者声明", "link_provided": "2 提供链接", "accessible": "3 实际可访问", "downloaded": "4 文件已下载", "verified_run": "5 已验证运行"}
        text += "## 开源证据阶段\n\n" + table(["阶段", "状态"], [(stage_names[k], v) for k, v in p["resource_stages"].items()])
        text += "## 译稿范围声明摘录\n\n以下为现有中文稿开头，用于判断译稿范围，不用作英文研究结论的证据。\n\n```text\n" + p["translation_scope_evidence"].replace("```", "~~~") + "\n```\n\n"
        text += link("返回文献总索引", f"{RESEARCH}/文献总索引.md", current) + "\n"
        emit(current, text)

    output = io.StringIO(newline="")
    columns = list(dict.fromkeys(k for p in papers for k in p))
    writer = csv.DictWriter(output, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for p in papers:
        writer.writerow({k: json.dumps(v, ensure_ascii=False, separators=(",", ":")) if isinstance(v, (list, dict)) else str(v) for k, v in p.items()})
    result[CSV_PATH] = output.getvalue().encode("utf-8-sig")
    result[f"{RESEARCH}/01_文献总索引.csv"] = result[CSV_PATH]
    return result


def validate(root, data):
    errors = []
    papers = data["papers"]
    categories = {c["code"] for c in data["categories"]}
    if categories != set("ABCDEFG"): errors.append("主类别必须严格为 A–G")
    for key in ("paper_id", "paper_short_name", "local_path", "record_path", "paper_title"):
        values = ["".join(c for c in unicodedata.normalize("NFKC", str(p[key])).casefold() if c.isalnum()) for p in papers]
        if len(values) != len(set(values)): errors.append("重复唯一键：" + key)
    identifiers = {}
    for p in papers:
        url = p["source_url"]
        match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url, re.I)
        doi = re.search(r"doi\.org/(10\.[^?#]+)", url, re.I)
        identifier = "arxiv:" + match[1] if match else (doi[1].lower().rstrip("/.") if doi else None)
        if identifier and identifier in identifiers: errors.append("重复论文标识：" + identifier)
        elif identifier: identifiers[identifier] = p["paper_id"]
    actual = {p.name for p in (root / "论文翻译").iterdir() if p.is_dir()}
    indexed = {Path(p["local_path"]).name for p in papers}
    if actual != indexed: errors.append(f"论文目录不一致：未纳入 {actual-indexed}，失效目录 {indexed-actual}")
    for p in papers:
        for k in REQUIRED:
            if k not in p or p[k] in (None, "", []): errors.append(f"{p['paper_id']} 缺失 {k}")
        if p["primary_category"] not in categories: errors.append(f"{p['paper_id']} 主类别非法")
        if p["reading_priority"] not in data["priority_definitions"]: errors.append(f"{p['paper_id']} 优先级非法")
        if p["reproducibility"] not in data["feasibility_definitions"]: errors.append(f"{p['paper_id']} 可行性非法")
        expected_record = f"{RESEARCH}/文献元数据/逐篇/{p['paper_short_name']}.md"
        if p["record_path"] != expected_record or "/" in p["paper_short_name"] or "\\" in p["paper_short_name"]:
            errors.append(f"{p['paper_id']} 独立记录输出路径非法")
        paths = [p[k] for k in ("local_path", "chinese_primary", "english_primary", "original_source_file")]
        paths += [m["path"] for m in p["chinese_materials"]] + [a["path"] for a in p["legacy_links"]]
        for k in ("pdf_paths", "english_materials", "figure_paths", "qa_paths", "reading_notes"): paths += p[k]
        for path in paths:
            resolved = (root / path).resolve()
            if not resolved.is_relative_to(root): errors.append("资料路径越出仓库：" + path)
            elif not resolved.exists(): errors.append("资料不存在：" + path)
        if len(p["resource_check_items"]) != 10: errors.append(f"{p['paper_id']} 实证分项不是10项")
        if len(p["resource_stages"]) != 5: errors.append(f"{p['paper_id']} 开源阶段不是5项")
    if hashlib.sha256((root / data["norm_path"]).read_bytes()).hexdigest() != data["norm_sha256"]:
        errors.append("原始规范哈希不一致")
    return errors


def check_links(root, files):
    errors, total = [], 0
    for rel, content in files.items():
        if not rel.endswith(".md"): continue
        text = re.sub(r"```.*?```", "", content.decode("utf-8"), flags=re.S)
        for target in re.findall(r"\]\(([^\n)]+)\)", text):
            target = target.strip("<>")
            parts = urlsplit(target)
            if parts.scheme or target.startswith("#"): continue
            total += 1
            resolved = (root / rel).parent.joinpath(unquote(parts.path)).resolve()
            if not resolved.is_relative_to(root): errors.append(f"{rel}：链接越界 {target}")
            elif not resolved.exists() and resolved.relative_to(root).as_posix() not in files:
                errors.append(f"{rel}：链接不存在 {target}")
    return errors, total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="read-only: check metadata, generated content and links")
    args = parser.parse_args()
    root = args.root.resolve()
    data = yaml.safe_load((root / CATALOG).read_text(encoding="utf-8-sig"))
    errors = validate(root, data)
    if errors:
        raise SystemExit("\n".join(errors))
    generated = build(data)
    for rel in generated:
        if not (root / rel).resolve().is_relative_to(root):
            raise SystemExit("生成文件路径越出仓库：" + rel)
    errors, links = check_links(root, generated)
    if errors: raise SystemExit("\n".join(errors))
    changed = [rel for rel, content in generated.items() if not (root / rel).exists() or (root / rel).read_bytes() != content]
    if args.check and changed:
        raise SystemExit("生成内容未同步：\n" + "\n".join(changed))
    if not args.check:
        for rel in changed:
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(generated[rel])
    print(json.dumps({"mode": "check" if args.check else "generate", "papers": len(data["papers"]),
                      "generated_files": len(generated), "changed_files": len(changed), "local_links_checked": links,
                      "categories": dict(collections.Counter(p["primary_category"] for p in data["papers"])),
                      "priorities": dict(collections.Counter(p["reading_priority"] for p in data["papers"]))}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
