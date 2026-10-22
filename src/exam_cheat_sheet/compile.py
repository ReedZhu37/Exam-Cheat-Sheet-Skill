"""Evidence-ranked, auditable cheat-sheet compilation (no probability estimates)."""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FORBIDDEN_SPLITS = {"dev", "sealed_test"}


def _words(text: str) -> int:
    return len(re.findall(r"[\u3400-\u9fff]|[^\s\u3400-\u9fff]+", text))


def _registry(data: dict) -> dict[str, dict]:
    raw = data.get("sources", {})
    if isinstance(raw, list):
        result = {}
        for source in raw:
            if not isinstance(source, dict) or not isinstance(source.get("source_id", source.get("id")), str):
                raise ValueError("sources entries require source_id")
            sid = source.get("source_id", source.get("id"))
            if sid in result:
                raise ValueError(f"Duplicate source: {sid}")
            result[sid] = source
        return result
    if isinstance(raw, dict) and all(isinstance(v, dict) for v in raw.values()):
        return raw
    raise ValueError("sources must be a source_id-keyed object or a list of source records")


def validate_concepts(data: dict) -> dict[str, dict]:
    """Validate records, references, and builder/holdout separation."""
    if not isinstance(data, dict) or not isinstance(data.get("title"), str):
        raise ValueError("Dataset requires a title string")
    if not isinstance(data.get("scope"), list) or not all(isinstance(x, str) for x in data["scope"]):
        raise ValueError("scope must be a list of concept IDs")
    if not isinstance(data.get("concepts"), list):
        raise ValueError("concepts must be a list")
    if not isinstance(data.get('scope_notes', []), list) or not all(isinstance(note, str) for note in data.get('scope_notes', [])):
        raise ValueError('scope_notes must be a list of strings')
    registry = _registry(data)
    for sid, source in registry.items():
        if source.get("split") not in {"train", "dev", "sealed_test"}:
            raise ValueError(f"Source {sid} requires split=train/dev/sealed_test")
    records = {}

    def source_ref(ref: Any) -> None:
        if not isinstance(ref, dict) or not isinstance(ref.get("source_id"), str) or not ref["source_id"]:
            raise ValueError("Every citation requires source_id")
        if type(ref.get("page")) is not int or ref["page"] < 1:
            raise ValueError(f"Citation {ref['source_id']} requires a positive, 1-based page")
        if "locator" in ref and not isinstance(ref["locator"], str):
            raise ValueError("Citation locator must be a string")
        if "sources" in data and ref["source_id"] not in registry:
            raise ValueError(f"Unregistered source: {ref['source_id']}")
        split = registry.get(ref["source_id"], {}).get("split", ref.get("split"))
        if split in FORBIDDEN_SPLITS or ref.get("split") in FORBIDDEN_SPLITS:
            raise ValueError(f"Builder cannot use {split} source: {ref['source_id']}")
        source = registry.get(ref["source_id"], {})
        metadata = source.get("metadata") or {}
        bounds = []
        for info in (source, metadata):
            if "page_count" in info:
                if type(info["page_count"]) is not int or info["page_count"] < 0:
                    raise ValueError(f"Invalid page_count for {ref['source_id']}")
                bounds.append(info["page_count"])
            if "pages" in info:
                pages = info["pages"]
                if type(pages) is int and pages >= 0:
                    bounds.append(pages)
                elif isinstance(pages, list):
                    bounds.append(len(pages))
                else:
                    raise ValueError(f"Invalid pages for {ref['source_id']}")
        if bounds and ref["page"] > min(bounds):
            raise ValueError(f"Citation {ref['source_id']} page {ref['page']} exceeds page bound {min(bounds)}")

    for record in data["concepts"]:
        if not isinstance(record, dict):
            raise ValueError("Each concept must be an object")
        for field in ("concept_id", "name", "definition"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"Concept requires nonempty {field}")
        cid = record["concept_id"]
        if cid in records:
            raise ValueError(f"Duplicate concept ID: {cid}")
        for field in ("aliases", "prerequisites", "procedure", "pitfalls"):
            if not isinstance(record.get(field), list) or not all(isinstance(x, str) for x in record[field]):
                raise ValueError(f"{cid}: {field} must be a list of strings")
        recognition = record.get("recognition")
        if not isinstance(recognition, str) and not (
            isinstance(recognition, list) and all(isinstance(x, str) for x in recognition)
        ):
            raise ValueError(f"{cid}: recognition must be a string or list of strings")
        if record.get("scope_status") not in {"in", "out", "unknown"}:
            raise ValueError(f"{cid}: invalid scope_status")
        if cid in data["scope"] and record["scope_status"] == "out":
            raise ValueError(f"{cid}: explicit scope conflicts with scope_status=out")
        if record.get("confidence") not in {"high", "medium", "low"}:
            raise ValueError(f"{cid}: invalid confidence")
        if not isinstance(record.get("sources"), list) or not record["sources"]:
            raise ValueError(f"{cid}: at least one source is required")
        for ref in record["sources"]:
            source_ref(ref)
        if not isinstance(record.get("formulas"), list):
            raise ValueError(f"{cid}: formulas must be a list")
        for formula in record["formulas"]:
            if not isinstance(formula, dict) or not isinstance(formula.get("expression"), str) or not formula["expression"]:
                raise ValueError(f"{cid}: formula requires expression")
            if not isinstance(formula.get("variables"), dict) or not all(
                isinstance(k, str) and isinstance(v, str) for k, v in formula["variables"].items()
            ):
                raise ValueError(f"{cid}: formula variables must map names to descriptions")
            if not isinstance(formula.get("conditions"), str) or not formula["conditions"].strip():
                raise ValueError(f"{cid}: formula requires explicit conditions (use 'None' if unconditional)")
            source_ref(formula.get("source"))
        if not isinstance(record.get("evidence"), list):
            raise ValueError(f"{cid}: evidence must be a list")
        for evidence in record["evidence"]:
            source_ref(evidence)
            if evidence.get("kind") not in {"scope", "exam", "teaching", "emphasis"}:
                raise ValueError(f"{cid}: invalid evidence kind")
            if evidence["kind"] == "exam" and not evidence.get("exam_id"):
                raise ValueError(f"{cid}: exam evidence requires canonical exam_id")
            role = registry.get(evidence["source_id"], {}).get("role", evidence.get("role"))
            if evidence["kind"] == "exam" and role is not None and role != "past_exam":
                raise ValueError(f"{cid}: exam frequency evidence requires role=past_exam, not {role}")
            for field in ("exam_id", "item_id"):
                if field in evidence and (not isinstance(evidence[field], str) or not evidence[field]):
                    raise ValueError(f"{cid}: {field} must be a nonempty string")
            if "points" in evidence:
                points = evidence["points"]
                if type(points) not in (int, float) or not 0 <= points < float("inf"):
                    raise ValueError(f"{cid}: points must be finite and nonnegative")
                if evidence["kind"] != "exam" or not evidence.get("item_id"):
                    raise ValueError(f"{cid}: points require exam evidence with item_id")
            if "concept_tags" in evidence:
                tags = evidence["concept_tags"]
                if not isinstance(tags, list) or not tags or not all(isinstance(x, str) for x in tags) or cid not in tags:
                    raise ValueError(f"{cid}: concept_tags must contain this concept ID")
        records[cid] = record
    for cid, record in records.items():
        for prerequisite in record["prerequisites"]:
            if prerequisite not in records:
                raise ValueError(f"{cid}: unknown prerequisite {prerequisite}")
        for evidence in record["evidence"]:
            for tag in evidence.get("concept_tags", []):
                if tag not in records:
                    raise ValueError(f"{cid}: unknown concept tag {tag}")
    _prerequisite_order(records)
    # Point evidence must identify one shared item budget and allocation set.
    # Otherwise two concepts could each silently receive the full item value.
    allocations = {}
    for cid, record in records.items():
        for evidence in record['evidence']:
            if 'points' not in evidence:
                continue
            key = (evidence['exam_id'], evidence['item_id'])
            tags = frozenset(evidence.get('concept_tags', [cid]))
            declaration = (evidence['points'], tags)
            if key in allocations and allocations[key] != declaration:
                raise ValueError(f'Conflicting shared point allocation for {key}; use identical points and concept_tags')
            allocations[key] = declaration
    return records


def _prerequisite_order(records: dict[str, dict], preferred: list[str] | None = None) -> list[str]:
    """Deterministic prerequisite-first order, rejecting cycles with their IDs."""
    ordered, visiting, visited = [], [], set()

    def visit(cid: str) -> None:
        if cid in visiting:
            raise ValueError("Prerequisite cycle: " + " -> ".join(visiting[visiting.index(cid):] + [cid]))
        if cid in visited:
            return
        visiting.append(cid)
        for prerequisite in sorted(records[cid]["prerequisites"]):
            visit(prerequisite)
        visiting.pop()
        visited.add(cid)
        ordered.append(cid)

    for cid in preferred if preferred is not None else sorted(records):
        visit(cid)
    return ordered


def _citation(ref: dict) -> str:
    locator = f", {ref['locator']}" if ref.get("locator") else ""
    return f"[{ref['source_id']}, p. {ref['page']}{locator}]"


def _text(value: str | list[str]) -> str:
    return "; ".join(value) if isinstance(value, list) else value


def _section(record: dict, compact: bool = False, band: str | None = None) -> str:
    priority = f"[{band}] " if band else ""
    lines = [f"## {priority}[{record['concept_id']}] {record['name']}", record["definition"]]
    if not compact and record["aliases"]:
        lines.append("Aliases: " + ", ".join(record["aliases"]))
    if record["recognition"]:
        lines.append("Recognize: " + _text(record["recognition"]))
    for formula in record["formulas"]:
        lines.extend([
            "Formula: " + formula["expression"],
            "Variables: " + ("; ".join(f"{k}: {v}" for k, v in formula["variables"].items()) or "No variables."),
            "Conditions: " + formula["conditions"],
            "Formula source: " + _citation(formula["source"]),
        ])
    if record["procedure"]:
        lines.append("Procedure:")
        lines.extend(f"{i}. {step}" for i, step in enumerate(record["procedure"], 1))
    if record["pitfalls"]:
        lines.append("Pitfalls: " + "; ".join(record["pitfalls"]))
    if record["prerequisites"]:
        lines.append("Prerequisites: " + ", ".join(f"[{cid}]" for cid in record["prerequisites"]))
    lines.append("Sources: " + " ".join(_citation(ref) for ref in record["sources"]))
    if not compact:
        lines.append(f"Scope: {record['scope_status']}; confidence: {record['confidence']}.")
        lines.extend("Evidence: " + evidence["kind"] + " " + _citation(evidence) for evidence in record["evidence"])
    return ("\n" if compact else "\n\n").join(lines) + "\n"


def _metrics(record: dict) -> dict:
    exams = set()
    items: dict[tuple[str, str], float] = {}
    emphasis = set()
    kinds = set()
    for evidence in record["evidence"]:
        kinds.add(evidence["kind"])
        if evidence["kind"] == "exam":
            exams.add(evidence["exam_id"])
            if "points" in evidence:
                key = (evidence["exam_id"], evidence["item_id"])
                allocated = evidence["points"] / len(set(evidence.get("concept_tags", [record["concept_id"]])))
                if key in items and items[key] != allocated:
                    raise ValueError(f"Conflicting point evidence for {record['concept_id']}: {key}")
                items[key] = allocated
        if evidence["kind"] == "emphasis":
            emphasis.add((evidence["source_id"], evidence["page"], evidence.get("locator", "")))
    band = "out" if record["scope_status"] == "out" else "A" if exams else "B" if kinds & {"teaching", "emphasis"} else "C"
    return {"evidence_band": band, "exam_ids": sorted(exams), "exam_frequency": len(exams),
            "allocated_points": sum(items.values()), "emphasis_count": len(emphasis)}


def compile_concepts(data: dict | str | Path, out: str | Path, budget_words: int = 2400) -> dict:
    """Write all five artifacts from validated records and return the priority report."""
    if type(budget_words) is not int or budget_words < 1:
        raise ValueError("budget_words must be a positive integer")
    if isinstance(data, (str, Path)):
        data = json.loads(Path(data).read_text(encoding="utf-8"))
    records = validate_concepts(data)
    metrics = {cid: _metrics(record) for cid, record in records.items()}

    def closure(seeds: set[str]) -> set[str]:
        found = set(seeds)
        pending = list(seeds)
        while pending:
            for prerequisite in records[pending.pop()]["prerequisites"]:
                if prerequisite not in found:
                    found.add(prerequisite)
                    pending.append(prerequisite)
        return found

    missing_scope = sorted(set(data["scope"]) - records.keys())
    scope = (set(data["scope"]) & records.keys()) | {cid for cid, r in records.items() if r["scope_status"] == "in"}
    protected = closure(scope)
    ordered = sorted(records, key=lambda cid: (
        cid not in protected,
        {"A": 0, "B": 1, "C": 2, "out": 3}[metrics[cid]["evidence_band"]],
        -metrics[cid]["exam_frequency"], -metrics[cid]["allocated_points"], -metrics[cid]["emphasis_count"], cid,
    ))
    sections = {cid: _section(record, compact=True, band=metrics[cid]["evidence_band"]) for cid, record in records.items()}
    header = f"# {data['title']}\n\nPlain Unicode formulas; citations use 1-based source pages.\n[A] Historical exam evidence; [B] teaching/emphasis; [C] scope-only/limited evidence; [out] out of scope.\n\n"

    def sheet(ids: set[str]) -> str:
        return header + "\n".join(sections[cid] for cid in ordered if cid in ids)

    selected = set(protected)
    reasons = {cid: "scope" if cid in scope else "required prerequisite" for cid in protected}
    for cid in ordered:
        if cid in selected:
            continue
        if records[cid]["scope_status"] == "out":
            reasons[cid] = "out of scope"
            continue
        proposed = selected | closure({cid})
        if _words(sheet(proposed)) <= budget_words:
            for added in proposed - selected:
                reasons[added] = "ranked within budget" if added == cid else f"prerequisite of {cid}"
            selected = proposed
        else:
            reasons[cid] = "budget: complete concept and prerequisite bundle does not fit"
    text = sheet(selected)
    word_count = _words(text)
    warnings = []
    historical_exams = sorted({exam for metric in metrics.values() for exam in metric["exam_ids"]})
    if len(historical_exams) < 2:
        warnings.append(f"Small historical sample: {len(historical_exams)} unique exams; frequency is descriptive, not a prediction.")
    source_issues = []
    for sid, source in sorted(_registry(data).items()):
        status = source.get("extraction_status", (source.get("metadata") or {}).get("extraction_status", "unknown"))
        if status != "verified":
            source_issues.append({"source_id": sid, "extraction_status": status,
                                  "issue": "Source extraction has not been verified; human review remains outstanding."})
    if "sources" not in data:
        warnings.append("No source registry supplied: source split eligibility cannot be independently verified.")
    if missing_scope:
        warnings.append("Missing scope concepts: " + ", ".join(missing_scope))
    conflicts = sorted(cid for cid in selected if records[cid]["scope_status"] == "out")
    if conflicts:
        warnings.append("Out-of-scope prerequisites retained: " + ", ".join(conflicts))
    if word_count > budget_words:
        warnings.append(f"Over budget by {word_count - budget_words} words: protected scope/prerequisites retained intact.")
    report = {
        "title": data["title"], "budget_words": budget_words, "actual_words": word_count,
        "over_budget_words": max(0, word_count - budget_words), "budget_met": word_count <= budget_words,
        "word_count_method": "Whitespace tokens, with each CJK character counted separately",
        "missing_scope": missing_scope, "warnings": warnings, "source_issues": source_issues,
        "historical_exam_ids": historical_exams, "historical_exam_count": len(historical_exams),
        "ranking_policy": "Protect scope and prerequisite closure; then A/B/C, unique exam count, allocated points, emphasis, ID. No appearance probabilities.",
        "evidence_bands": {"A": "Observed in a historical exam", "B": "Teaching or explicit emphasis evidence", "C": "Scope-only or no exam/teaching evidence", "out": "Explicitly out of scope"},
        "concepts": [{"concept_id": cid, **metrics[cid], "selected": cid in selected,
                      "protected": cid in protected, "reason": reasons[cid], "compact_words": _words(sections[cid]),
                      "confidence": records[cid]["confidence"]} for cid in ordered],
    }
    destination = Path(out)
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "cheatsheet.md").write_text(text, encoding="utf-8")
    (destination / "cheatsheet-expanded.md").write_text(
        header + "\n".join(_section(records[cid], band=metrics[cid]["evidence_band"]) for cid in ordered if cid in selected), encoding="utf-8")
    (destination / "review-guide.md").write_text(
        header + "\n".join(_section(records[cid], band=metrics[cid]["evidence_band"]) for cid in _prerequisite_order(records, ordered)), encoding="utf-8")
    (destination / "priority-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    coverage = [f"# Coverage: {data['title']}", "", f"Selected: {len(selected)}/{len(records)} concepts.",
                f"Word budget: {word_count}/{budget_words}.", "", "## Warnings", *(warnings or ["None."]),
                "", "## Concept decisions"]
    coverage.extend(f"- [{cid}] {'included' if cid in selected else 'excluded'}: {reasons[cid]}" for cid in ordered)
    coverage.extend(["", "## Missing scope", *(f"- [{cid}] missing source record" for cid in missing_scope)])
    coverage.extend(['', '## Scope and material limitations', *('- ' + note for note in data.get('scope_notes', []))])
    coverage.extend(["", "## Source extraction issues",
                     *(f"- [{issue['source_id']}] {issue['extraction_status']}: {issue['issue']}" for issue in source_issues)])
    if not source_issues:
        coverage.append("No unverified extraction flags in the supplied registry; this does not certify concept correctness.")
    (destination / "coverage-report.md").write_text("\n".join(coverage) + "\n", encoding="utf-8")
    return report


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _implementation_files(repo_root: Path, code_root: Path) -> list[Path]:
    """Enumerate the portable implementation and dependency declarations."""
    files = set(code_root.rglob('*.py'))
    files.update((repo_root / 'scripts').rglob('*.py'))
    files.update((repo_root / 'schemas').rglob('*.json'))
    files.update(repo_root / name for name in ('pyproject.toml', 'uv.lock'))
    return sorted(p for p in files if p.is_file())


def freeze_sheet(sheet: str | Path, inputs: list[str | Path], out: str | Path, config: dict | None = None) -> dict:
    """Snapshot files using repository-relative paths, portable with a repository clone."""
    root, target = Path(sheet).resolve(), Path(out).resolve()
    code_root = Path(__file__).resolve().parent
    repo_root = next((p for p in code_root.parents if (p / "pyproject.toml").is_file() or (p / ".git").exists()), None)
    if repo_root is None:
        raise ValueError("Cannot identify repository root for a portable freeze")

    def relative(path: Path) -> str:
        try:
            return path.resolve().relative_to(repo_root).as_posix()
        except ValueError as exc:
            raise ValueError(f"Portable freeze inputs must be under repository root: {path}") from exc

    if not root.is_dir():
        raise ValueError(f"Sheet directory does not exist: {root}")
    relative(root)
    relative(target)
    outputs = {p.relative_to(root).as_posix(): _sha256(p) for p in sorted(root.rglob("*")) if p.is_file() and p.resolve() != target}
    if not outputs:
        raise ValueError("Cannot freeze an empty sheet directory")
    input_hashes = {}
    for raw in inputs:
        path = Path(raw).resolve()
        if not path.exists():
            raise ValueError(f"Input does not exist: {path}")
        paths = sorted(path.rglob("*")) if path.is_dir() else [path]
        for item in paths:
            if item.is_file() and item.resolve() != target:
                input_hashes[relative(item)] = _sha256(item)
    code = {relative(p): _sha256(p) for p in _implementation_files(repo_root, code_root)}
    code_version = hashlib.sha256(json.dumps(code, sort_keys=True).encode()).hexdigest()
    if config is None:
        priority = root / "priority-report.json"
        config = {"budget_words": json.loads(priority.read_text(encoding="utf-8"))["budget_words"]} if priority.is_file() else {}
        rendering = root / "render-report.json"
        if rendering.is_file():
            render_config = json.loads(rendering.read_text(encoding="utf-8"))
            config["render"] = {k: render_config[k] for k in ("max_pages", "min_font") if k in render_config}
    result = {"schema_version": 2, "created_at": datetime.now(timezone.utc).isoformat(),
              "path_base": {"repo_root": "freeze_parent", "sheet": "freeze_parent", "outputs": "sheet",
                            "input_paths": "repo_root", "inputs": "repo_root", "code_root": "repo_root", "code_files": "repo_root"},
              "repo_root": Path(os.path.relpath(repo_root, target.parent)).as_posix(),
              "sheet": Path(os.path.relpath(root, target.parent)).as_posix(), "outputs": outputs,
              "input_paths": [relative(Path(p)) for p in inputs], "inputs": input_hashes,
              "config": config, "code_root": relative(code_root), "code_files": code, "code_version": code_version}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def verify_freeze(path: str | Path) -> dict:
    """Reject file additions, deletions, edits, or code changes since freezing."""
    target = Path(path).resolve()
    frozen = json.loads(target.read_text(encoding="utf-8"))
    if frozen.get("schema_version") != 2:
        raise ValueError("Unsupported freeze schema; regenerate a portable schema_version=2 freeze")
    repo_root = (target.parent / frozen["repo_root"]).resolve()
    root = (target.parent / frozen["sheet"]).resolve()
    current_outputs = {p.relative_to(root).as_posix(): _sha256(p) for p in sorted(root.rglob("*")) if p.is_file() and p.resolve() != target}
    drift = []
    if current_outputs != frozen["outputs"]:
        drift.append("sheet outputs")
    current_inputs = {}
    for raw in frozen["input_paths"]:
        item = repo_root / raw
        if not item.exists():
            drift.append(f"missing input: {item}")
        for p in sorted(item.rglob("*")) if item.is_dir() else [item]:
            if p.is_file() and p.resolve() != target:
                current_inputs[p.resolve().relative_to(repo_root).as_posix()] = _sha256(p)
    if current_inputs != frozen["inputs"]:
        drift.append("inputs")
    current_code = {p.resolve().relative_to(repo_root).as_posix(): _sha256(p)
                    for p in _implementation_files(repo_root, repo_root / frozen["code_root"])}
    if current_code != frozen["code_files"]:
        drift.append("code")
    if hashlib.sha256(json.dumps(current_code, sort_keys=True).encode()).hexdigest() != frozen["code_version"]:
        drift.append("code version")
    if drift:
        raise ValueError("Freeze drift detected: " + ", ".join(drift))
    return frozen
