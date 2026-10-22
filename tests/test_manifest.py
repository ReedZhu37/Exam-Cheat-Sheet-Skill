import copy
import json
import os
from pathlib import Path

import pytest

from exam_cheat_sheet import ManifestError, ingest_source, load_manifest, validate_manifest
from exam_cheat_sheet.manifest import authorize_source


def entry(path="notes.txt", **changes):
    source = {
        "id": "notes", "path": path, "role": "notes", "split": "train",
        "status": "pending", "metadata": None,
        "provenance": {"origin": "Locally authored synthetic fixture", "license": "CC0-1.0", "acquired_at": None},
    }
    source.update(changes)
    return source


def manifest(*sources):
    return {"schema_version": "1.0", "sources": list(sources)}


def test_pending_manifest_loads_without_acquisition(tmp_path):
    data = manifest(entry("not-acquired.pdf"))
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    assert load_manifest(path) == data
    assert validate_manifest(data, root=tmp_path) == data


@pytest.mark.parametrize("change", [
    {"status": "validated"}, {"status": "acquired"},
    {"provenance": {}}, {"role": "answer"}, {"split": "test"},
])
def test_invalid_schema_and_acquisition_state(change):
    with pytest.raises(ManifestError):
        validate_manifest(manifest(entry(**change)))


@pytest.mark.parametrize("path,role,split", [
    ("test/book.txt", "notes", "train"),
    ("sealed_test/book.txt", "past_exam", "dev"),
    ("SeAlEd_TeSt/book.txt", "notes", "train"),
    ("solutions/book.txt", "notes", "train"),
    ("dev/book.txt", "notes", "train"),
    ("test\\book.txt", "notes", "train"),
])
def test_reserved_paths_cannot_spoof_labels(path, role, split):
    with pytest.raises(ManifestError):
        validate_manifest(manifest(entry(path, role=role, split=split)))


def test_explicit_training_solution_manifest_is_allowed(tmp_path):
    source = entry("train/solutions/archival.txt", role="solution")
    assert validate_manifest(manifest(source), tmp_path)["sources"] == [source]


def test_traversal_and_absolute_escape(tmp_path):
    root = tmp_path / "allowed"
    root.mkdir()
    outside = tmp_path / "outside.txt"
    outside.write_text("private", encoding="utf-8")
    for path in ("../outside.txt", str(outside)):
        with pytest.raises(ManifestError):
            authorize_source(entry(path), root, "builder")


def symlink_or_skip(link: Path, target: Path):
    try:
        link.symlink_to(target)
    except OSError as exc:
        pytest.skip(f"Symlinks unavailable on this host: {exc}")


def test_symlink_escape(tmp_path):
    root = tmp_path / "allowed"
    root.mkdir()
    outside = tmp_path / "outside.txt"
    outside.write_text("private", encoding="utf-8")
    symlink_or_skip(root / "innocent.txt", outside)
    with pytest.raises(ManifestError):
        authorize_source(entry("innocent.txt"), root, "builder")


def test_symlink_cannot_hide_reserved_path(tmp_path):
    reserved = tmp_path / "sealed_test"
    reserved.mkdir()
    target = reserved / "hidden.txt"
    target.write_text("synthetic holdout", encoding="utf-8")
    symlink_or_skip(tmp_path / "innocent.txt", target)
    with pytest.raises(ManifestError, match="Reserved"):
        authorize_source(entry("innocent.txt"), tmp_path, "builder")


def test_contradictory_realpath_alias(tmp_path):
    (tmp_path / "notes.txt").write_text("synthetic", encoding="utf-8")
    data = manifest(entry(), entry("./notes.txt", id="alias", role="past_exam", split="dev"))
    with pytest.raises(ManifestError, match="alias"):
        validate_manifest(data, tmp_path)


@pytest.mark.skipif(os.name != "nt", reason="Windows case-insensitive path aliases")
def test_contradictory_case_alias(tmp_path):
    (tmp_path / "notes.txt").write_text("synthetic", encoding="utf-8")
    data = manifest(entry(), entry("NOTES.TXT", id="alias", role="past_exam", split="dev"))
    with pytest.raises(ManifestError, match="alias"):
        validate_manifest(data, tmp_path)


@pytest.mark.parametrize("timestamp", ["not-a-date", "2026-10-22T12:00:00"])
def test_acquisition_timestamp_requires_timezone(timestamp):
    source = entry()
    source["provenance"]["acquired_at"] = timestamp
    with pytest.raises(ManifestError):
        validate_manifest(manifest(source))


def test_contradictory_symlink_alias(tmp_path):
    target = tmp_path / "notes.txt"
    target.write_text("synthetic", encoding="utf-8")
    symlink_or_skip(tmp_path / "alias.txt", target)
    data = manifest(entry(), entry("alias.txt", id="alias", role="past_exam", split="dev"))
    with pytest.raises(ManifestError, match="alias"):
        validate_manifest(data, tmp_path)


@pytest.mark.parametrize("access,role,split,allowed", [
    ("builder", "notes", "train", True),
    ("builder", "solution", "train", True),
    ("builder", "solution", "dev", False),
    ("builder", "solution", "sealed_test", False),
    ("builder", "past_exam", "dev", False),
    ("builder", "past_exam", "sealed_test", False),
    ("evaluator", "past_exam", "dev", True),
    ("evaluator", "solution", "dev", False),
    ("evaluator", "notes", "dev", False),
    ("grader", "solution", "dev", True),
    ("grader", "past_exam", "dev", True),
    ("grader", "solution", "sealed_test", False),
    ("final_evaluator", "solution", "sealed_test", False),
    ("final_evaluator", "past_exam", "dev", False),
    ("final_grader", "notes", "sealed_test", False),
    ("final_grader", "solution", "train", False),
    ("admin", "notes", "train", False),
])
def test_explicit_access_policies(tmp_path, access, role, split, allowed):
    path = tmp_path / "material.txt"
    path.write_text("synthetic", encoding="utf-8")
    source = entry("material.txt", role=role, split=split)
    if allowed:
        assert authorize_source(source, tmp_path, access) == path.resolve()
    else:
        with pytest.raises(ManifestError):
            authorize_source(source, tmp_path, access)


@pytest.mark.parametrize("access", ["final_evaluator", "final_grader"])
def test_final_authorization_requires_freeze_before_path_resolution(tmp_path, monkeypatch, access):
    import exam_cheat_sheet.manifest as module

    def forbidden_resolution(*args, **kwargs):
        pytest.fail("Material path resolved before freeze verification")

    monkeypatch.setattr(module, "resolve_source", forbidden_resolution)
    with pytest.raises(ManifestError, match="requires an explicit freeze"):
        authorize_source(entry("sealed_test/unread.txt", role="past_exam", split="sealed_test"), tmp_path, access)


def test_invalid_ledger_and_checksum(tmp_path):
    (tmp_path / "notes.txt").write_text("synthetic", encoding="utf-8")
    result = ingest_source(entry(), tmp_path, tmp_path / "out")
    for mutation in ("missing", "repeat", "checksum", "duplicate"):
        broken = copy.deepcopy(result)
        metadata = broken["metadata"]
        if mutation == "missing":
            metadata["page_count"] = 2
        elif mutation == "repeat":
            metadata["pages"].append(copy.deepcopy(metadata["pages"][0]))
            metadata["page_count"] = 2
        elif mutation == "checksum":
            metadata["pages"][0]["text"] = "tampered"
        else:
            metadata["pages"][0]["duplicate_of"] = 1
        with pytest.raises(ManifestError):
            validate_manifest(manifest(broken), tmp_path)


def test_duplicate_ids_rejected():
    with pytest.raises(ManifestError, match="Duplicate source id"):
        validate_manifest(manifest(entry(), entry()))
