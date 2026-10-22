"""Exam materials with explicit provenance and least-privilege ingestion."""

from .ingest import IngestError, ingest_source
from .manifest import ManifestError, load_manifest, validate_manifest

__all__ = [
    "IngestError", "ManifestError", "ingest_source", "load_manifest", "validate_manifest"
]
__version__ = "0.1.0"
