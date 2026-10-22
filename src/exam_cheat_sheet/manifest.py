"""Manifest validation and material access policy.

Only manifest-listed sources are eligible for reads. Builder: train materials,
including explicitly labelled archival solutions for concepts and learning.
Solutions are not additional question-frequency evidence. Evaluator: dev
past_exam questions. Grader: dev past_exam and solution. Final evaluator/grader
have analogous sealed_test access only after verifying an explicit freeze.
Train access does not require a freeze or any dev-evaluation gate.
Reserved directory components are checked both before and after resolution.
Validation never reads source contents; ingestion applies policy before opening.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker


class ManifestError(ValueError):
    """Invalid manifest, provenance, ledger, or material access."""


ACCESS_POLICIES = {
    "builder": {("train", role) for role in ("textbook", "slides", "notes", "past_exam", "solution", "scope")},
    "evaluator": {("dev", "past_exam")},
    "grader": {("dev", "past_exam"), ("dev", "solution")},
    "final_evaluator": {("sealed_test", "past_exam")},
    "final_grader": {("sealed_test", "past_exam"), ("sealed_test", "solution")},
}


def _schema() -> dict:
    packaged = Path(__file__).parent / "_schemas" / "manifest.schema.json"
    path = packaged if packaged.is_file() else Path(__file__).parents[2] / "schemas" / "manifest.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _check_reserved(path: str | Path, source: dict) -> None:
    # Treat both separators identically, including when validating on POSIX.
    parts = {p.casefold() for p in PurePosixPath(str(path).replace("\\", "/")).parts[:-1]}
    for names, split in (({"test", "sealed_test"}, "sealed_test"), ({"dev"}, "dev"), ({"train"}, "train")):
        if names & parts and source["split"] != split:
            raise ManifestError(f"Reserved path component contradicts split: {path}")
    if {"solution", "solutions"} & parts and source["role"] != "solution":
        raise ManifestError(f"Reserved solutions path contradicts role: {path}")


def resolve_source(source: dict, root: Path, *, must_exist: bool = True) -> Path:
    """Resolve the allowlisted path and reject traversal and symlink escapes."""
    root = Path(root).resolve(strict=True)
    raw = Path(source["path"])
    _check_reserved(raw, source)
    candidate = raw if raw.is_absolute() else root / raw
    try:
        lexical = candidate.relative_to(root)
        _check_reserved(lexical, source)
        resolved = candidate.resolve(strict=must_exist)
        relative = resolved.relative_to(root)
    except (OSError, ValueError, RuntimeError) as exc:
        raise ManifestError(f"Source must resolve under allowed root: {source['path']}") from exc
    _check_reserved(relative, source)
    if must_exist and not resolved.is_file():
        raise ManifestError(f"Source is not a regular file: {source['path']}")
    return resolved


def authorize_source(source: dict, root: Path, access: str, *, freeze: Path | None = None) -> Path:
    """Apply identity and freeze gates before resolving any material path.

    Final identities require a caller-supplied freeze produced by freeze_sheet;
    verify_freeze rejects changed sheet outputs, inputs, or code. Ordinary train
    and dev identities do not invoke freeze verification.
    """
    if access not in ACCESS_POLICIES:
        raise ManifestError(f"Unknown access identity: {access}")
    if not isinstance(source, dict):
        raise ManifestError("Source must be a manifest entry")
    if not isinstance(source.get("split"), str) or not isinstance(source.get("role"), str):
        raise ManifestError("Source split and role must be strings")
    if (source.get("split"), source.get("role")) not in ACCESS_POLICIES[access]:
        raise ManifestError(f"{access} cannot read {source.get('split')}/{source.get('role')}")
    if access in {"final_evaluator", "final_grader"}:
        if freeze is None:
            raise ManifestError(f"{access} requires an explicit freeze path")
        from .compile import verify_freeze

        try:
            verify_freeze(freeze)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise ManifestError(f"Freeze verification failed: {exc}") from exc
    if not isinstance(source.get("path"), str) or not source["path"]:
        raise ManifestError("Source path must be a nonempty string")
    return resolve_source(source, root)


def _validate_ledger(source: dict) -> None:
    metadata = source["metadata"]
    if metadata is None:
        return
    pages = metadata["pages"]
    if len(pages) != metadata["page_count"] or [p["page_number"] for p in pages] != list(range(1, metadata["page_count"] + 1)):
        raise ManifestError("Missing, repeated, or out-of-order page ledger entries")
    seen = {}
    anchors = set()
    for page in pages:
        if page["anchor"] in anchors:
            raise ManifestError("Duplicate page anchor")
        anchors.add(page["anchor"])
        if hashlib.sha256(page["text"].encode("utf-8")).hexdigest() != page["text_sha256"]:
            raise ManifestError("Page text checksum mismatch")
        previous = seen.get(page["page_sha256"])
        if page["duplicate_of"] != previous:
            raise ManifestError("Duplicate page detection ledger is inconsistent")
        seen.setdefault(page["page_sha256"], page["page_number"])
        if previous is not None and page["quality"] != "needs_review":
            raise ManifestError("Duplicate pages require review")
        if metadata["page_unit"] == "pdf_page" and (not page["raster_path"] or page["quality"] != "needs_review"):
            raise ManifestError("PDF pages require full-page raster assets and visual review")


def validate_manifest(data: dict, root: Path | None = None) -> dict:
    """Validate schema, acquisition state, page continuity and path aliases.

    With root, resolve every entry (pending files may not yet exist). Contradictory
    aliases are rejected. This is structural validation, not a new file checksum
    verification; ingest_source verifies stored checksums before re-ingestion.
    The caller must supply a trusted manifest; metadata cannot infer file purpose.
    """
    errors = sorted(Draft202012Validator(_schema(), format_checker=FormatChecker()).iter_errors(data), key=lambda e: str(e.path))
    if errors:
        raise ManifestError(errors[0].message)
    ids, aliases = set(), {}
    for source in data["sources"]:
        if source["id"] in ids:
            raise ManifestError(f"Duplicate source id: {source['id']}")
        ids.add(source["id"])
        acquired_at = source["provenance"]["acquired_at"]
        if acquired_at is not None:
            try:
                timestamp = datetime.fromisoformat(acquired_at.replace("Z", "+00:00"))
                if timestamp.tzinfo is None:
                    raise ValueError("timezone required")
            except ValueError as exc:
                raise ManifestError("acquired_at must be an ISO 8601 timestamp with timezone") from exc
        _check_reserved(source["path"], source)
        resolved = resolve_source(source, root, must_exist=source["status"] in {"acquired", "validated"}) if root is not None else Path(source["path"])
        key = os.path.normcase(str(resolved))
        identity = (source["role"], source["split"])
        if key in aliases and aliases[key] != identity:
            raise ManifestError(f"Contradictory realpath alias: {source['path']}")
        aliases[key] = identity
        _validate_ledger(source)
    return data


def load_manifest(path: str | Path) -> dict:
    """Load JSON and validate structure; pass root to validate_manifest for paths."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"Cannot load manifest: {path}") from exc
    return validate_manifest(data)
