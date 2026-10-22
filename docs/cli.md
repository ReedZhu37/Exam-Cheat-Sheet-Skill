# Executable contracts and commands

Run commands from the repository root after `uv sync --locked`.

## Material manifest

The canonical ingestion schema is `schemas/manifest.schema.json`. A pending
entry can be authored before parsing. `id` is the stable source ID (concept
citations call this same value `source_id`).

```json
{
  "schema_version": "1.0",
  "sources": [{
    "id": "lecture-1",
    "path": "train/lecture-1.pdf",
    "role": "slides",
    "split": "train",
    "status": "pending",
    "provenance": {
      "origin": "https://example.edu/lecture-1.pdf",
      "license": "Record the actual source license",
      "acquired_at": null
    },
    "metadata": null
  }]
}
```

```sh
uv run python -m exam_cheat_sheet ingest manifest.json --root materials --out extracted
```

The returned `extracted/manifest.json` adds original file hash/size, parser
version, page count, per-page text, raster paths, duplicate candidates, and
review reasons. `status=validated` means acquisition/structure validation,
**not mathematical or visual verification**. PDF page quality remains
`needs_review`. DOCX has logical document/paragraph/table anchors, not physical
page numbers. Embedded DOCX/PPTX pictures are preserved with hashes; spatial
layout, charts and slide rasterization still require separate visual inspection.

Builder accepts train sources including explicitly identified archival
solutions. Solutions cannot count as independent exam frequency evidence.
Evaluator accepts dev questions, grader dev questions/solutions. Final access
uses `final_evaluator`/`final_grader` and requires `--freeze`.
The manifest is trusted administrative input; a user who can edit both the
manifest and storage can relabel content. Realpath validation and tool-denied
evaluation contexts are the enforced boundaries, not semantic detection of a
renamed examination.

`downloads.json` in the benchmark is a **separate downloader inventory**:
URL, title, author, retrieval time, pinned hash/bytes/pages. Convert and ingest:

```sh
uv run python scripts/fetch_benchmark.py --stage train
uv run python scripts/ingest_benchmark.py
```

This verifies downloaded hashes before ingestion and produces the canonical
`benchmarks/mit-6041-quiz1/manifest.json`. Raw files and raster assets stay local.

## Concept authoring

Use `schemas/concept.schema.json` for each concept record and
`examples/mit-6041/concepts-v1.json` for a complete dataset. Its envelope is:

```text
title: string
scope: concept ID array
sources: source registry (array with source_id/split/role/pages, or keyed object)
concepts: concept records
```

The compiler additionally validates graph links, eligibility, citation page
bounds when known, and evidence accounting. It does not manufacture concepts
from text. Register every source so split eligibility can be checked.

```sh
uv run python -m exam_cheat_sheet compile concepts.json --out output --budget-words 3000
uv run python -m exam_cheat_sheet render output/cheatsheet.md --out output/cheatsheet.pdf --max-pages 6 --min-font 9
uv run python -m exam_cheat_sheet freeze --sheet output --inputs concepts.json manifest.json --out freeze.json
```

`priority-report.json` records each inclusion/exclusion and any budget excess.
Scope/prerequisite protection can exceed a word budget; the tool reports that
fact instead of silently deleting indispensable content. Rendering fails on a
page/font/bounds violation and retains its diagnostic report. The example's
6-page/9-point budget is an implementation default, not a verified exam rule.

## Evaluation controller

`prepare_exam.py` exports **every** page, including the exam formula summary.
`solve_exam.py` sends text and page images to the same pinned model for both
conditions. `run_isolated.py` checks the actual model identity, delivered image
count, and absence of tool events, retaining hashes and raw final-response
events. Provider reasoning traces are not published.

`grade_exam.py` receives an existing response and separately exported official
solutions, invokes a new tool-denied grader, and validates score arithmetic.
The grader is an LLM judge, not an official examiner. Raw judgments and any
reviews must be preserved. For final grading, use `--final` to enforce the
105-point/11-subpart ledger.

The scripts require OpenCode V2 credentials on the running machine and use
`openai/gpt-6-astra#high` in this registered demonstration. Porting to another
model requires registering a new comparison; existing deterministic outputs
and tests work without that provider.
