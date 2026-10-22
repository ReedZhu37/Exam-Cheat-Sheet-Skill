import copy
import json
import shutil
from pathlib import Path

import pytest

from exam_cheat_sheet.compile import compile_concepts, freeze_sheet, validate_concepts, verify_freeze


def concept(cid, *, status="unknown", prerequisites=()):
    return {
        "concept_id": cid, "name": f"Concept {cid}", "aliases": [],
        "definition": "A source-backed definition.", "formulas": [],
        "prerequisites": list(prerequisites), "recognition": "Use for a matching problem.",
        "procedure": ["Identify the assumptions."], "pitfalls": ["Check the conditions."],
        "sources": [{"source_id": "notes", "page": 1}], "evidence": [],
        "scope_status": status, "confidence": "high",
    }


def dataset(*records, scope=()):
    return {"title": "Audit sheet", "scope": list(scope), "concepts": list(records),
            "sources": {"notes": {"split": "train"}, "exam": {"split": "train"}}}


def test_scope_closure_survives_budget_and_preserves_formula(tmp_path):
    first = concept("a", prerequisites=["b"])
    first["formulas"] = [{"expression": "P(A | B) = P(A ∩ B) / P(B)",
                          "variables": {"A": "an event", "B": "conditioning event"},
                          "conditions": "P(B) > 0", "source": {"source_id": "notes", "page": 2}}]
    data = dataset(first, concept("b", status="out", prerequisites=["c"]), concept("c"), scope=["a", "missing"])
    report = compile_concepts(data, tmp_path, budget_words=1)
    assert all(r["selected"] and r["protected"] for r in report["concepts"])
    assert report["missing_scope"] == ["missing"]
    assert report["over_budget_words"] > 0
    text = (tmp_path / "cheatsheet.md").read_text(encoding="utf-8")
    for preserved in ("P(A ∩ B)", "conditioning event", "P(B) > 0", "[notes, p. 2]", "[c]"):
        assert preserved in text
    assert any("Out-of-scope prerequisites" in w for w in report["warnings"])
    assert {p.name for p in tmp_path.iterdir()} == {
        "review-guide.md", "cheatsheet-expanded.md", "cheatsheet.md", "priority-report.json", "coverage-report.md"}


def test_optional_bundle_is_excluded_if_complete_dependencies_do_not_fit(tmp_path):
    small = concept("small")
    heavy = concept("heavy", prerequisites=["dependency"])
    dependency = concept("dependency", status="out")
    dependency["definition"] = "large " * 500
    heavy["evidence"] = [{"kind": "exam", "source_id": "exam", "page": 1, "exam_id": "exam-1"}]
    report = compile_concepts(dataset(small, heavy, dependency), tmp_path, budget_words=110)
    rows = {r["concept_id"]: r for r in report["concepts"]}
    assert rows["small"]["selected"]
    assert not rows["heavy"]["selected"]
    assert not rows["dependency"]["selected"]
    assert report["budget_met"]


def test_frequency_deduplicates_exam_and_points_are_shared(tmp_path):
    a, b = concept("a"), concept("b")
    evidence = {"kind": "exam", "source_id": "exam", "page": 1,
                "exam_id": "2020-final", "item_id": "3", "points": 12, "concept_tags": ["a", "b"]}
    a["evidence"] = [evidence, dict(evidence, page=2), dict(evidence, item_id="4", points=8)]
    b["evidence"] = [copy.deepcopy(evidence)]
    report = compile_concepts(dataset(a, b), tmp_path)
    rows = {r["concept_id"]: r for r in report["concepts"]}
    assert rows["a"]["exam_frequency"] == 1
    assert rows["a"]["allocated_points"] == 10
    assert rows["b"]["allocated_points"] == 6
    assert rows["a"]["evidence_band"] == "A"


@pytest.mark.parametrize("split", ["dev", "sealed_test"])
@pytest.mark.parametrize("location", ["sources", "evidence", "formulas"])
def test_holdout_references_rejected(split, location):
    a = concept("a")
    ref = {"source_id": "holdout", "page": 1}
    if location == "sources":
        a[location].append(ref)
    elif location == "evidence":
        a[location].append(dict(ref, kind="teaching"))
    else:
        a[location].append({"expression": "x = 1", "variables": {"x": "count"}, "conditions": "Always", "source": ref})
    data = dataset(a)
    data["sources"]["holdout"] = {"split": split}
    with pytest.raises(ValueError, match="Builder cannot use"):
        validate_concepts(data)


def test_missing_prerequisite_and_missing_source_rejected():
    with pytest.raises(ValueError, match="unknown prerequisite"):
        validate_concepts(dataset(concept("a", prerequisites=["absent"])))
    a = concept("a")
    a["sources"] = []
    with pytest.raises(ValueError, match="at least one source"):
        validate_concepts(dataset(a))


def test_cycles_rejected():
    with pytest.raises(ValueError, match="Prerequisite cycle"):
        validate_concepts(dataset(concept("a", prerequisites=["b"]), concept("b", prerequisites=["a"]), scope=["a"]))


def test_solution_sources_do_not_count_as_historical_exams():
    data = dataset(concept("a"))
    data["sources"]["notes"]["role"] = "solution"
    data["concepts"][0]["evidence"] = [{"kind": "teaching", "source_id": "notes", "page": 1}]
    data["concepts"][0]["formulas"] = [{"expression": "x = 1", "variables": {"x": "count"},
                                        "conditions": "Always", "source": {"source_id": "notes", "page": 1}}]
    validate_concepts(data)
    data["concepts"][0]["evidence"][0].update(kind="exam", exam_id="historical")
    with pytest.raises(ValueError, match="requires role=past_exam"):
        validate_concepts(data)


def test_item_points_cannot_be_fully_duplicated_across_concepts():
    a, b = concept('a'), concept('b')
    evidence = {'kind': 'exam', 'source_id': 'exam', 'page': 1,
                'exam_id': 'exam-1', 'item_id': '1a', 'points': 10}
    a['evidence'] = [dict(evidence)]
    b['evidence'] = [dict(evidence)]
    with pytest.raises(ValueError, match='shared point allocation'):
        validate_concepts(dataset(a, b))
    a['evidence'][0]['concept_tags'] = ['a', 'b']
    b['evidence'][0]['concept_tags'] = ['b', 'a']
    validate_concepts(dataset(a, b))


@pytest.fixture
def portable_repo(tmp_path, monkeypatch):
    import exam_cheat_sheet.compile as compiler

    repo = tmp_path / "original"
    code = repo / "src" / "exam_cheat_sheet"
    code.mkdir(parents=True)
    (repo / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
    module = code / "compile.py"
    module.write_text("# synthetic package code\n", encoding="utf-8")
    monkeypatch.setattr(compiler, "__file__", str(module))
    return repo


@pytest.mark.parametrize("drift", ["edit", "add", "delete", "input"])
def test_freeze_rejects_drift(portable_repo, drift):
    sheet = portable_repo / "sheet"
    compile_concepts(dataset(concept("a"), scope=["a"]), sheet)
    source = portable_repo / "concepts.json"
    source.write_text("original", encoding="utf-8")
    freeze = sheet / "freeze.json"
    frozen = freeze_sheet(sheet, [source], freeze)
    assert frozen["config"]["budget_words"] == 2400
    assert len(frozen["code_version"]) == 64
    assert verify_freeze(freeze) == frozen
    if drift == "edit":
        (sheet / "cheatsheet.md").write_text("changed", encoding="utf-8")
    elif drift == "add":
        (sheet / "extra.md").write_text("added", encoding="utf-8")
    elif drift == "delete":
        (sheet / "cheatsheet.md").unlink()
    else:
        source.write_text("changed", encoding="utf-8")
    with pytest.raises(ValueError, match="Freeze drift"):
        verify_freeze(freeze)


def test_freeze_verifies_after_clone_and_rejects_cloned_code_drift(portable_repo, tmp_path):
    sheet = portable_repo / "build" / "sheet"
    compile_concepts(dataset(concept("a")), sheet)
    source = portable_repo / "concepts.json"
    source.write_text("synthetic input", encoding="utf-8")
    freeze = sheet / "freeze.json"
    frozen = freeze_sheet(sheet, [source], freeze)
    assert frozen["schema_version"] == 2
    assert not any(Path(p).is_absolute() for p in [*frozen["inputs"], *frozen["outputs"], *frozen["code_files"]])
    clone = tmp_path / "cloned"
    shutil.copytree(portable_repo, clone)
    shutil.rmtree(portable_repo)
    copied_freeze = clone / "build" / "sheet" / "freeze.json"
    assert verify_freeze(copied_freeze) == frozen
    (clone / "src" / "exam_cheat_sheet" / "compile.py").write_text("# changed code\n", encoding="utf-8")
    with pytest.raises(ValueError, match="code"):
        verify_freeze(copied_freeze)


@pytest.mark.parametrize("page_metadata", [{"page_count": 3}, {"pages": 3}, {"pages": [{}, {}, {}]},
                                          {"metadata": {"page_count": 3, "pages": [{}, {}, {}]}}])
def test_citation_cannot_exceed_registered_pages(page_metadata):
    data = dataset(concept("a"))
    data["sources"]["notes"].update(page_metadata)
    data["concepts"][0]["sources"][0]["page"] = 999
    with pytest.raises(ValueError, match="exceeds page bound"):
        validate_concepts(data)


def test_compact_hierarchy_review_order_and_source_review_flags(tmp_path):
    a, z = concept("a", prerequisites=["z"]), concept("z")
    a["evidence"] = [{"kind": "exam", "source_id": "exam", "page": 1, "exam_id": "old-exam"}]
    z["evidence"] = [{"kind": "teaching", "source_id": "notes", "page": 1}]
    data = dataset(a, z, scope=["a"])
    data["sources"]["notes"]["extraction_status"] = "verified"
    data["sources"]["exam"]["extraction_status"] = "needs_review"
    report = compile_concepts(data, tmp_path)
    compact = (tmp_path / "cheatsheet.md").read_text(encoding="utf-8")
    expanded = (tmp_path / "cheatsheet-expanded.md").read_text(encoding="utf-8")
    review = (tmp_path / "review-guide.md").read_text(encoding="utf-8")
    assert "## [A] [a]" in compact and "## [B] [z]" in compact
    assert compact.count("\n\n") < expanded.count("\n\n")
    assert "Procedure:\n1. Identify the assumptions.\nPitfalls: Check the conditions." in compact
    assert review.index("## [B] [z]") < review.index("## [A] [a]")
    assert report["historical_exam_count"] == 1
    assert any("Small historical sample" in w for w in report["warnings"])
    assert [issue["source_id"] for issue in report["source_issues"]] == ["exam"]
    assert "Source extraction issues" in (tmp_path / "coverage-report.md").read_text(encoding="utf-8")


def test_render_checks_actual_pdf_unicode_and_png(tmp_path):
    from exam_cheat_sheet.render import render_markdown

    source = tmp_path / "sheet.md"
    source.write_text("# 概率复习\n\n## [bayes] Bayes\nP(A | B) = P(A ∩ B) / P(B)\n条件: P(B) > 0\n" + "LongToken" * 80, encoding="utf-8")
    report = render_markdown(source, tmp_path / "sheet.pdf", max_pages=1, min_font=9)
    assert report["passed"]
    assert report["actual_pages"] == 1
    assert report["actual_min_font"] >= 9
    assert report["bounds_checked"] > 100
    assert not report["bounds_violations"]
    assert (tmp_path / "sheet-page-001.png").read_bytes().startswith(b"\x89PNG")


def test_render_page_limit_is_enforced_without_shrinking_font(tmp_path):
    from exam_cheat_sheet.render import render_markdown

    source = tmp_path / "long.md"
    source.write_text("A readable line.\n" * 90, encoding="utf-8")
    with pytest.raises(ValueError, match="Render constraints failed"):
        render_markdown(source, tmp_path / "long.pdf", max_pages=1, min_font=12)
    report = json.loads((tmp_path / "render-report.json").read_text(encoding="utf-8"))
    assert report["actual_pages"] > 1
    assert report["actual_min_font"] >= 12


def test_render_keeps_heading_with_two_content_lines_and_numbers_pages(tmp_path):
    from exam_cheat_sheet.render import render_markdown
    from pypdf import PdfReader

    source = tmp_path / "orphans.md"
    source.write_text("Filler line.\n" * 62 + "## [A] [target] Heading\n\nFirst content line.\nSecond content line.\n", encoding="utf-8")
    report = render_markdown(source, tmp_path / "orphans.pdf", max_pages=2, min_font=9)
    pages = [p.extract_text() for p in PdfReader(tmp_path / "orphans.pdf").pages]
    target = next(text for text in pages if "[target]" in text)
    assert "First content line." in target and "Second content line." in target
    assert len(pages) == 2
    assert all(f"Page {index}" in text for index, text in enumerate(pages, 1))
    assert report["heading_keep_content_lines"] == 2


def test_final_cli_requires_freeze_before_loading_manifest(tmp_path):
    from exam_cheat_sheet.cli import main

    with pytest.raises(SystemExit) as exc:
        main(["ingest", str(tmp_path / "unread.json"), "--root", str(tmp_path), "--out", str(tmp_path / "out"),
              "--access", "final_evaluator"])
    assert exc.value.code == 2
    assert not (tmp_path / "out").exists()


@pytest.mark.parametrize("access", ["builder", "final_evaluator", "final_grader"])
def test_cli_verifies_and_passes_freeze_only_for_final_access(tmp_path, monkeypatch, access):
    from exam_cheat_sheet.cli import main
    import exam_cheat_sheet.compile as compiler
    import exam_cheat_sheet.ingest as ingest
    import exam_cheat_sheet.manifest as manifest

    calls = []
    source = {"id": "synthetic", "split": "train" if access == "builder" else "sealed_test", "role": "past_exam"}
    monkeypatch.setattr(compiler, "verify_freeze", lambda path: calls.append(("verify", path)))
    monkeypatch.setattr(manifest, "load_manifest", lambda path: calls.append(("load", path)) or {"sources": [source]})
    monkeypatch.setattr(manifest, "validate_manifest", lambda data, root: data)

    def fake_ingest(source, root, out, **kwargs):
        calls.append(("ingest", kwargs))
        return source

    monkeypatch.setattr(ingest, "ingest_source", fake_ingest)
    args = ["ingest", str(tmp_path / "synthetic.json"), "--root", str(tmp_path), "--out", str(tmp_path / "out"), "--access", access]
    if access != "builder":
        args.extend(["--freeze", str(tmp_path / "freeze.json")])
    assert main(args) == 0
    kwargs = next(value for name, value in calls if name == "ingest")
    if access == "builder":
        assert "freeze" not in kwargs and calls[0][0] == "load"
    else:
        assert kwargs["freeze"] == tmp_path / "freeze.json"
        assert [name for name, _ in calls] == ["verify", "load", "ingest"]
