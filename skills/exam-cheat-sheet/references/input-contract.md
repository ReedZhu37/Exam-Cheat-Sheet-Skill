# Input and persistence contract

This is a portable semantic contract. An implementation may use JSON, JSONL, or a database and different field names, provided these facts and invariants survive round trips. Use the implementation's actual schema for executable inputs. `assets/project-config.json` is an editable planning template, not an asserted CLI schema.

## Project facts

Record a project ID, course, target assessment, explicit included/excluded topics, scope citations, language/notation, intended output formats, and layout constraints. Count printed **sides**, not merely sheets. Record paper size, margins, columns, minimum font size, color assumptions, and whether a supplied formula page counts toward the allowed limit. Unknown constraints remain `null`, not guessed defaults.

Record permitted local processing, upload to a model provider, redistribution, and exam use separately. Source rights do not establish exam-use permission. A missing exam rule should leave an exam-ready label unset rather than prevent study-guide authoring.

## Sources and ingestion units

Each source needs:

- Stable `source_id`, title, local path, content SHA-256, media type, and role: textbook, slides, scope, past exam, formula page, or other evidence.
- Creator/publisher, original URL when known, license/permission basis, attribution text, and transformation notes. Unknown rights are recorded as unknown.
- Eligible page/slide ranges and split (`train`, `dev`, `sealed`, or non-evaluation course material). A mirrored exam and its solutions share the same canonical `exam_id`.
- Extraction engine/version/settings, timestamp, unit count, and source-level failures. A new hash makes downstream authored claims stale until checked.

Each unit needs a stable unit ID, source hash, 1-based physical PDF page or slide index, printed page label when available, extracted text, method (`native`, `ocr`, `manual`, or `failed`), review status, and issues. Slide notes are separate from visible slide text. Preserve tables, images, and equation locations or references rather than flattening them invisibly.

DOCX has no reliable physical page count before rendering: use paragraph/table/cell locators and label them as such. Legacy `.ppt`/`.doc` need an explicitly recorded conversion; the named Python parsers handle `.pptx`/`.docx`, not those legacy formats.

Persist empty, unreadable, excluded, and reviewed units. A manifest must account for every source unit. Store corrections alongside original extracted text, reviewer identity, and rationale. OCR confidence alone cannot mark a mathematical page reviewed. Keep previews in a generated location and raw downloads under `.local/`.

## Authored knowledge

Concept records include:

- Stable ID, title, aliases, scope status, and prerequisite IDs.
- Definition; symbols; formula with assumptions and domain; procedure; recognition cues; pitfalls; worked example or explicit absence of one.
- Claim-level evidence: source/unit locator, a short supporting span or image region description, support type (`direct`, `derived`, `author_example`, `uncertain`), and review status. Derived claims also identify their reasoning and source claims.
- Exam-subpart evidence, unique exam IDs, allocated points, rank, rank reasons, protection reason, and uncertainty.
- View content or selectors for review, expanded, and compact outputs; inclusion status; compression decisions; revision/provenance information.

Only a real supporting citation can establish teacher emphasis. A student's recollection may be recorded as an unverified note, not upgraded to documentary evidence.

## Exams, frequency, and points

Each exam has a canonical ID independent of filename, mirrors, question paper, answer key, and extracted page. Each subpart has a unique `(exam_id, subpart_id)`, stated maximum points, source locator, and concept allocations with a brief rationale.

For concept `c`, use:

```text
frequency(c) = number of distinct eligible exam_ids with supported mappings to c
allocated_points(c) = sum of c's allocations over eligible subparts
```

Display the eligible-exam denominator and split. The default authoring pool is train; keep dev diagnostics separate and exclude sealed data. Repeated subparts in one exam increase possible point evidence, not exam frequency. Unknown point values remain unknown.

For a subpart worth `p`, all concept allocations are nonnegative and sum to at most `p`. Put any remainder in an explicit unallocated bucket; allocations plus remainder must equal `p`. Do not give every mapped concept full credit for the same points. Prerequisite links do not automatically earn another copy of a subpart's points. Topic coverage and earned student marks are different measures.

## Audit records and invalidation

Keep a coverage matrix from each scope item and required prerequisite to its evidence and location in each view. Distinguish missing source, unresolved extraction, not yet authored, compact omission, and covered. Report protected omissions as unresolved, never as successfully covered.

Deletion records include concept/claim ID, affected view, previous revision, retained destination if merged, removed information, reason, protection status, and review decision. Compression that drops a condition is a substantive deletion. Prefer a revision log over destructive overwrites.

A changed source, concept, scope, or prerequisite invalidates dependent rankings and views. Save manifests and hashes with every build. A resumed run must distinguish unchanged verified records from stale or pending ones.
