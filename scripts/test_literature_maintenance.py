"""Exercise incremental generation, idempotence and invalid-input rejection on synthetic data.

No original paper files are copied. Synthetic fixtures live in an isolated temporary folder.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit

import yaml

sys.dont_write_bytecode = True
from generate_literature_navigation import CATALOG, RESEARCH, build


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON proof destination")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    script = root / "scripts/generate_literature_navigation.py"
    source = yaml.safe_load((root / CATALOG).read_text(encoding="utf-8"))
    data = {k: copy.deepcopy(v) for k, v in source.items() if k != "papers"}
    data["papers"] = []
    data["core_reference"] = "Synthetic1"
    assertions = []
    temp_base = Path(tempfile.gettempdir()).resolve()
    with tempfile.TemporaryDirectory(prefix="paper-navigation-qa-", dir=temp_base) as directory:
        fixture = Path(directory).resolve()
        assert fixture.is_relative_to(temp_base) and fixture != temp_base
        # Only the classification norm is copied, never any original paper/translation/image.
        norm = fixture / data["norm_path"]
        norm.parent.mkdir(parents=True)
        norm.write_bytes((root / data["norm_path"]).read_bytes())

        def paper(number):
            p = copy.deepcopy(source["papers"][-1])
            short = f"Synthetic{number}"
            p.update(paper_id=short, paper_short_name=short, paper_title=f"Synthetic test paper {number}",
                     source_url=f"https://example.invalid/synthetic/{number}",
                     local_path=f"论文翻译/{short}", record_path=f"{RESEARCH}/文献元数据/逐篇/{short}.md",
                     primary_category="G", baseline_category="G", reading_priority="P3", reproducibility="N/A",
                     relevance_order=number, classification_reason=f"Synthetic classification reason {number}",
                     reading_focus=f"Synthetic reading focus {number}", translation_scope_evidence="Synthetic fixture; no original paper content.")
            p["chinese_primary"] = p["local_path"] + "/中文.md"
            p["english_primary"] = p["local_path"] + "/English.md"
            p["original_source_file"] = p["english_primary"]
            p["chinese_materials"] = [dict(path=p["chinese_primary"], scope="Synthetic")]
            p["english_materials"] = [p["english_primary"]]
            for key in ["pdf_paths", "figure_paths", "qa_paths", "reading_notes", "legacy_links"]: p[key] = []
            d = fixture / p["local_path"]
            d.mkdir(parents=True)
            (fixture / p["chinese_primary"]).write_text("Synthetic fixture", encoding="utf-8")
            (fixture / p["english_primary"]).write_text("Synthetic fixture", encoding="utf-8")
            return p

        def prepare():
            (fixture / CATALOG).parent.mkdir(parents=True, exist_ok=True)
            (fixture / CATALOG).write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
            expected = build(data)
            # Create only synthetic support documents for non-generated navigation targets.
            for rel, payload in expected.items():
                if not rel.endswith(".md"): continue
                for target in re.findall(r"\]\(([^\n)]+)\)", re.sub(r"```.*?```", "", payload.decode("utf-8"), flags=re.S)):
                    parts = urlsplit(target)
                    if parts.scheme or target.startswith("#"): continue
                    path = (fixture / rel).parent.joinpath(unquote(parts.path)).resolve()
                    assert path.is_relative_to(fixture)
                    key = path.relative_to(fixture).as_posix()
                    if key in expected or path.exists(): continue
                    if not path.suffix: path.mkdir(parents=True, exist_ok=True)
                    else:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text("Synthetic support document", encoding="utf-8")

        def run(ok=True, check=False):
            process = subprocess.run([sys.executable, str(script), "--root", str(fixture)] + (["--check"] if check else []),
                                     capture_output=True, encoding="utf-8", errors="replace",
                                     env={**os.environ, "PYTHONIOENCODING": "utf-8"})
            assert (process.returncode == 0) == ok, process.stdout + process.stderr
            return json.loads(process.stdout) if ok else process.stderr

        data["papers"].append(paper(1))
        prepare()
        assert run()["papers"] == 1
        data["papers"].append(paper(2))
        prepare()
        result = run()
        assert result["papers"] == 2 and result["categories"] == {"G": 2}
        home = (fixture / "README.md").read_text(encoding="utf-8")
        assert "2 篇论文" in home and "P3：2" in home and "Synthetic2" in home
        assertions.append("新增1篇合成文献：1→2条，三层导航、G类与P3统计同步；无52篇硬编码")
        before = {f: hashlib.sha256((fixture / f).read_bytes()).hexdigest() for f in build(data)}
        assert run()["changed_files"] == 0
        after = {f: hashlib.sha256((fixture / f).read_bytes()).hexdigest() for f in build(data)}
        assert before == after and run(check=True)["changed_files"] == 0
        assertions.append("重复生成：0文件改变，全部生成文件SHA-256一致，--check通过")
        data["papers"].append(copy.deepcopy(data["papers"][0]))
        prepare()
        assert "重复唯一键" in run(ok=False)
        data["papers"].pop()
        assertions.append("重复paper_id/短名/目录/记录路径被拒绝")
        data["papers"][0]["classification_reason"] = ""
        prepare()
        assert "classification_reason" in run(ok=False)
        data["papers"][0]["classification_reason"] = "Synthetic reason restored"
        assertions.append("分类理由空缺被拒绝")
        data["papers"][0]["chinese_primary"] = "论文翻译/Missing/中文.md"
        prepare()
        # prepare creates link fixtures, so explicitly remove this one synthetic file.
        invalid_path = (fixture / data["papers"][0]["chinese_primary"]).resolve()
        assert invalid_path.is_relative_to(fixture)
        invalid_path.unlink()
        assert "资料不存在" in run(ok=False)
        assertions.append("不存在的中文阅读文件被拒绝")
    proof = dict(result="PASS", generator_sha256=hashlib.sha256(script.read_bytes()).hexdigest(),
                 assertions=assertions, original_paper_files_copied=0, original_repo_modified=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(proof, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(proof, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
