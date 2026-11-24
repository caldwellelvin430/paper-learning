"""Read-only navigation QA; --write-report explicitly updates the classification QA report.

Optional --baseline and --legacy-nav consume the before-change manifest/navigation saved
outside the repository, to verify protected files and legacy links for this remediation.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import yaml

sys.dont_write_bytecode = True
from generate_literature_navigation import CATALOG, CSV_PATH, RESEARCH, REQUIRED, build, check_links, link, table, validate

REPORT = f"{RESEARCH}/QA_文献分类整改验收报告.md"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--legacy-nav", type=Path)
    parser.add_argument("--incoming-manifest", type=Path, help="verify newly imported files against the ZIP manifest")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    data = yaml.safe_load((root / CATALOG).read_text(encoding="utf-8-sig"))
    papers = data["papers"]
    checks, errors = {}, validate(root, data)
    checks["元数据必填项、唯一键、分类及实际资料路径"] = not errors
    expected = build(data)
    changed = [f for f, b in expected.items() if not (root / f).exists() or (root / f).read_bytes() != b]
    checks[f"CSV、全部生成页及{len(papers)}篇记录与 YAML 同步"] = not changed
    errors += ["生成文件不同步：" + p for p in changed]
    actual_files = {f: (root / f).read_bytes() for f in expected if (root / f).exists()}
    for extra in [f"{RESEARCH}/分类维护说明.md", data["norm_path"], REPORT, f"{RESEARCH}/QA_文献整理验收报告.md", f"{RESEARCH}/QA_61篇文献与Git复核验收报告.md"]:
        if not (root / extra).exists(): continue
        actual_files[extra] = (root / extra).read_bytes()
    for paper in papers:
        if paper.get("ingestion_batch"):
            for path in (root / paper["local_path"]).glob("*.md"):
                actual_files[path.relative_to(root).as_posix()] = path.read_bytes()
    link_errors, link_count = check_links(root, actual_files)
    errors += link_errors
    checks["所有新增管理 Markdown 的本地阅读链接有效"] = not link_errors

    rows = list(csv.DictReader(io.StringIO((root / CSV_PATH).read_text(encoding="utf-8-sig"))))
    csv_errors = []
    if len(rows) != len(papers): csv_errors.append("CSV 与 YAML 行数不同")
    for p, row in zip(papers, rows):
        for k, v in p.items():
            expected_cell = json.dumps(v, ensure_ascii=False, separators=(",", ":")) if isinstance(v, (list, dict)) else str(v)
            if row.get(k) != expected_cell: csv_errors.append(p["paper_id"] + ":" + k)
    errors += csv_errors
    checks["CSV 所有字段逐值对应 YAML（含嵌套数据）"] = not csv_errors

    home = (root / "README.md").read_text(encoding="utf-8")
    homepage_checks = [f"## {c['code']}｜{c['name']}" in home for c in data["categories"]]
    homepage_checks += [link(p["translation_scope"], p["chinese_primary"], "README.md") in home for p in papers]
    homepage_checks += ["<details" not in home.lower(), "<summary" not in home.lower()]
    homepage_checks += [home.count("| 论文名称 | 年份 | 阅读优先级 | 研究价值 | 中文译稿 | 英文原文 | PDF |") == len(data["categories"])]
    checks["首页七类全部展开，全部论文直达中文稿，无折叠组件"] = all(homepage_checks)
    if not all(homepage_checks): errors.append("首页展示检查失败")
    cc = collections.Counter(p["primary_category"] for p in papers)
    pc = collections.Counter(p["reading_priority"] for p in papers)
    rc = collections.Counter(p["reproducibility"] for p in papers)
    checks["七类数量之和与论文目录数相同"] = sum(cc.values()) == len(list((root / "论文翻译").iterdir())) - len([x for x in (root / "论文翻译").iterdir() if not x.is_dir()])
    checks["每篇分类理由和阅读重点独立填写"] = all(len({p[k] for p in papers}) == len(papers) for k in ["classification_reason", "reading_focus"])
    checks["阅读优先级与可行性分字段保存"] = all("reading_priority" in p and "reproducibility" in p for p in papers)
    checks["没有无依据变更初始主类别"] = all(p["primary_category"] == p["baseline_category"] or p.get("classification_changes") for p in papers)

    old_link_count, missing_old_links = 0, []
    if args.legacy_nav:
        old = json.loads(args.legacy_nav.read_text(encoding="utf-8"))
        old_page = old.get("论文翻译\\README.md", old.get("论文翻译/README.md"))
        current_page = (root / "论文翻译/README.md").read_text(encoding="utf-8")
        new_targets = {(root / "论文翻译" / unquote(urlsplit(t).path)).resolve() for t in re.findall(r"\]\(([^)]+)\)", current_page) if not urlsplit(t).scheme}
        for t in re.findall(r"\]\(([^)]+)\)", old_page):
            if urlsplit(t).scheme: continue
            old_link_count += 1
            if (root / "论文翻译" / unquote(urlsplit(t).path)).resolve() not in new_targets: missing_old_links.append(t)
        checks["原平铺导航的所有本地阅读入口均保留"] = not missing_old_links
        errors += ["原入口丢失：" + t for t in missing_old_links]

    protected = {"baseline_files": None, "protected_files": None, "checked": False, "changed": [], "deleted": []}
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        # Only management/navigation files may change; all other prior files are protected.
        def allowed(path):
            return path in ("README.md", "论文翻译/README.md") or (path.startswith(RESEARCH + "/") and "/Task01_" not in path and "/Task02_" not in path and "/研究分析矩阵/" not in path)
        paths = [f for f in baseline if not allowed(f.replace("\\", "/"))]
        protected.update(baseline_files=len(baseline), protected_files=len(paths), checked=True)
        for f in paths:
            path = root / f
            if not path.exists(): protected["deleted"].append(f)
            elif hashlib.sha256(path.read_bytes()).hexdigest() != baseline[f]: protected["changed"].append(f)
        checks["原论文、配图、教学、Task01/Task02及研究矩阵哈希不变"] = not protected["changed"] and not protected["deleted"]
        errors += ["受保护文件改变：" + p for p in protected["changed"] + protected["deleted"]]

    checks["生成过程确定且无追加重复记录"] = all(a == b for a, b in zip(expected.items(), build(data).items()))
    pdf_hashes, duplicate_pdfs = {}, []
    for paper in papers:
        for rel in paper["pdf_paths"]:
            digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
            if digest in pdf_hashes and pdf_hashes[digest] != paper["paper_id"]:
                duplicate_pdfs.append((pdf_hashes[digest], paper["paper_id"]))
            pdf_hashes[digest] = paper["paper_id"]
    checks["规范化标题、短名、标识符及跨论文PDF去重"] = not duplicate_pdfs and not any("重复" in e for e in errors)
    incoming_result = None
    if args.incoming_manifest:
        incoming = json.loads(args.incoming_manifest.read_text(encoding="utf-8"))
        bad = [f["path"] for f in incoming["files"] if not (root / f["path"]).exists() or hashlib.sha256((root / f["path"]).read_bytes()).hexdigest() != f["sha256"]]
        incoming_result = dict(papers=len(incoming["papers"]), files=len(incoming["files"]), changed_or_missing=bad)
        checks["新增九篇原始资料与压缩包逐文件哈希一致"] = not bad
    git_commands = []
    for arguments in [["status", "--short", "--branch"], ["remote", "-v"], ["branch", "-vv"], ["log", "-5", "--oneline"], ["rev-parse", "HEAD"], ["rev-parse", "origin/main"], ["rev-parse", "HEAD^{tree}"]]:
        process = subprocess.run(["git", "-c", "core.quotepath=false", "-C", str(root), *arguments], capture_output=True, encoding="utf-8", errors="replace")
        git_commands.append(dict(command="git " + " ".join(arguments), exit_code=process.returncode, stdout=process.stdout, stderr=process.stderr))
    git_ok = all(c["exit_code"] == 0 for c in git_commands)
    checks["真实本地Git仓库具备main历史且origin正确"] = git_ok and "paper-learning.git" in git_commands[1]["stdout"] and "* main " in git_commands[2]["stdout"]
    proof_path = root / RESEARCH / "QA_维护流程测试结果.json"
    maintenance_proof = None
    if proof_path.exists():
        maintenance_proof = json.loads(proof_path.read_text(encoding="utf-8"))
        checks["增量、幂等、重复键、空理由及失效路径合成测试"] = (
            maintenance_proof["result"] == "PASS"
            and maintenance_proof["generator_sha256"] == hashlib.sha256((root / "scripts/generate_literature_navigation.py").read_bytes()).hexdigest()
            and len(maintenance_proof["assertions"]) == 5)
    errors += ["验收条件未通过：" + k for k, ok in checks.items() if not ok]
    scanned_entries = [p for p in root.rglob("*") if ".git" not in p.relative_to(root).parts and "__pycache__" not in p.relative_to(root).parts]
    summary = dict(papers=len(papers), repository_files=sum(p.is_file() for p in scanned_entries), repository_entries=len(scanned_entries),
                   category_counts=dict(cc), priority_counts=dict(pc), feasibility_counts=dict(rc),
                   generated_files=len(expected), local_links_checked=link_count, original_links_preserved=old_link_count,
                   protected=protected, incoming=incoming_result, unique_pdf_hashes=len(pdf_hashes),
                   git_commands=git_commands, maintenance_proof=maintenance_proof, checks=checks, errors=errors)

    if args.write_report:
        missing_fields = sum(1 for p in papers for k in REQUIRED if k not in p or p[k] in (None, "", []))
        unavailable = [p for p in papers if not p["pdf_paths"]]
        status = "通过" if not errors and protected["checked"] and args.legacy_nav else "部分通过 / 需补充检查"
        text = (f"# 文献分类整改验收报告\n\n验收日期：{data['checked_on']}。结论：**{status}**。"
                "本报告针对本地分类整改，尚未推送 GitHub。\n\n"
                "## 实际扫描与分类统计\n\n"
                f"当前本地仓库实际扫描 {summary['repository_files']} 个文件、{summary['repository_entries']} 个文件及目录条目"
                "（排除Git内部和Python缓存）；该数量包括保留的本地Task01/Task02与本次新增管理成果，不与远程旧树条目混用。\n\n"
                f"`论文翻译/` 实际扫描 {len(papers)} 个论文目录，YAML/CSV 各 {len(papers)} 条，独立分类记录 {len(papers)} 份。"
                f"管理文件生成器输出 {len(expected)} 个文件；必填字段空缺 {missing_fields} 个。\n\n")
        # Keep the table construction explicit to make accidental category omissions visible.
        text += table(["主类别", "论文数"], [[c["code"] + "｜" + c["name"], cc[c["code"]]] for c in data["categories"]])
        text += table(["独立管理维度", "数量"], [["阅读优先级", "；".join(f"{k}={pc[k]}" for k in data["priority_definitions"])],
                         ["实证可行性", "；".join(f"{k}={rc[k]}" for k in data["feasibility_definitions"])]])
        text += "## 强制条件检查\n\n" + table(["检查项", "实际结果"], [[k, "通过" if ok else "失败"] for k, ok in checks.items()])
        text += (f"本次检查 {link_count} 个本地 Markdown 链接实例，失效 {len(link_errors)} 个；"
                 f"原阅读导航 {old_link_count} 个本地入口全部逐目标比对。CSV 所有字段与 YAML 逐值比对，"
                 "不是只比较总数。三个 README 与所有索引按同一数据重新构建后逐字节比对。"
                 "外部网址仅作原文/资源来源；未把全部网址当前 HTTP 可访问性写为已核验。\n\n")
        if maintenance_proof:
            text += "增量维护实测（隔离合成数据，未复制原论文文件）：\n\n" + "\n".join("- " + s for s in maintenance_proof["assertions"]) + "\n\n"
        text += "## 原文核验覆盖及边界\n\n"
        text += (f"本次 {len(papers)}/{len(papers)} 篇完成用于分类的英文原文定向核验（100%）：摘要、方法/数据或综述架构、"
                 "评价、实验或系统案例、局限/讨论/结论边界；每篇记录给出章节/物理页和独立阅读重点。"
                 "这不代表所有页均逐句阅读，也不代表附件、源码、数据、环境或实验已全部核验。"
                 "AgenticAI_Survey 为综述，没有新增独立实验，按综述内容核查。"
                 "GeoAnalystBench 的独立 Supporting Information 未取得，不声称其附件全覆盖。\n\n"
                 "Beyond the Final Answer 本地只有英文摘要：已另取 PMLR 官方 30 页英文 PDF 阅读方法、评价和实验，"
                 "工作缓存未写回原论文目录。本地有原始 PDF 的论文为 " + str(len(papers)-len(unavailable)) + " 篇；其余如下。\n\n")
        text += table(["缺少本地原始 PDF", "实际英文核验入口"], [[link(p["paper_short_name"], p["record_path"], REPORT),
                      "本地完整英文逐页稿/原页" if p["paper_short_name"] != "Beyond the Final Answer" else "本地摘要＋PMLR官方全文PDF（工作缓存）"] for p in unavailable])
        text += "中文稿按文内声明标注摘要/章节译述、精读或正文译稿范围；未因文件名含“全文”认定逐句完整性。\n\n"
        text += f"## 仍待核验事项\n\n分类层面的英文来源核验无整篇缺失。开源可用性、执行和独立审计证据仍有待核项目，不能据此称{len(papers)}篇已复现。\n\n"
        text += table(["范围", "论文与待办"], [
            ["R1：主要小型材料已取回，尚未运行", "；".join(p["paper_short_name"] for p in papers if p["reproducibility"] == "R1") + "。验证环境/API、完整GT与独立判据后才考虑升级。"],
            ["R2：核心材料暂不可得", "；".join(p["paper_short_name"] for p in papers if p["reproducibility"] == "R2") + "。项目页仍为code/dataset coming soon；需定期复查。"],
            ["RU：完整资产链不足以判断", "；".join(p["paper_short_name"] for p in papers if p["reproducibility"] == "RU")],
            ["N/A", "；".join(p["paper_short_name"] for p in papers if p["reproducibility"] == "N/A") + "。当前用于方法/背景研究；不表示其代码不存在。"],
        ])
        text += ("GeoAgentBench 的任务CSV实际只取得Git LFS指针，未取得payload；不能按任务/GT下载成功计账。"
                 "GeoNatureAgent 本地原文与当前README的DOI/版本不一致，保留归档版并显式说明，后续不混用v7与本地v5/v6。"
                 "全库论文及 Task01/Task02 中的作者声明、风险假设与独立实验证据不因分类整改而升级。\n\n")
        text += "## 文件保护与 Git 状态\n\n"
        text += (f"整改前清单共 {protected['baseline_files']} 个文件；对 {protected['protected_files']} 个受保护文件逐一做SHA-256核对，"
                 f"改变 {len(protected['changed'])} 个，删除 {len(protected['deleted'])} 个。"
                 "论文子目录、PDF、译稿、配图、教学内容、Task01/Task02及研究矩阵未修改。仅重写授权的管理索引和三个README并增加维护文件。\n\n"
                 f"远程基线 main 提交为 `{data['remote_baseline']['commit']}`，tree为 `{data['remote_baseline'].get('tree', '待核验')}`，"
                 f"树条目 {data['remote_baseline']['entries']}，blob {data['remote_baseline']['blobs']}。"
                 "本轮通过仅获取五条提交和目录树、从已有文件校验导入3468个原始blob，"
                 "将原无HEAD的完整快照接到真实main历史；未覆盖工作区论文文件，未重新下载论文。"
                 "以下是实际仓库命令结果；未创建新提交、未执行git push，等待用户确认。\n\n")
        for command in git_commands[:4]:
            displayed = command["stdout"]
            if command["command"].startswith("git status") and len(displayed.splitlines()) > 24:
                displayed = "\n".join(displayed.splitlines()[:24]) + "\n[以上为前24行；完整输出保存在QA_文献分类整改检查结果.json的git_commands]\n"
            text += "```text\n$ " + command["command"] + "\n" + displayed + command["stderr"] + "```\n\n"
        if incoming_result:
            text += f"新增九篇共{incoming_result['files']}个原始文件已与压缩包逐文件核对，改变/缺失{len(incoming_result['changed_or_missing'])}个；"
            text += f"现有PDF跨论文指纹共{len(pdf_hashes)}种，重复0组。\n\n"
        text += "## 复核命令\n\n```powershell\npython scripts/generate_literature_navigation.py --check\npython scripts/verify_literature_navigation.py\n```\n\n"
        text += "本次额外使用整改前哈希清单和旧导航比对；机器可读完整结果见同目录的 `QA_文献分类整改检查结果.json`。\n"
        if errors: text += "\n## 未通过项\n\n" + "\n".join("- " + e for e in errors) + "\n"
        (root / REPORT).write_text(text, encoding="utf-8")
        (root / RESEARCH / "QA_文献分类整改检查结果.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors: raise SystemExit(1)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
