# Frozen benchmark protocol

This protocol specifies a prospective comparison. It does not report a result. No exam or solution downloads are required to install or use the skill.

## Fixed assessment family and splits

Use **MIT OpenCourseWare 6.041SC, Probabilistic Systems Analysis and Applied Probability, Fall 2013**, Quiz 1 materials, with these historical assessment identities:

| Role | Exam | Allowed use |
| --- | --- | --- |
| Train | Spring 2009 Quiz 1 (`S2009`) | Authoring examples, concept mappings, historical frequency/point evidence |
| Development | Fall 2009 Quiz 1 (`F2009`) | Pre-freeze protocol and artifact refinement; log every revision |
| Sealed final | Fall 2010 Quiz 1 (`F2010`) | One frozen final evaluation; excluded from build and tuning |

The Fall 2013 course label identifies the OCW collection, not the year of each historical paper. Use stable source hashes and canonical exam IDs. Dev feedback may guide documented revisions but must not inflate train frequency. Keep final questions, solutions, grading keys, and any derived summaries out of authoring manifests, search indexes, examples, and the author's context.

Final questions become available to each solver only after freeze. Final solutions/test answers remain **grader-only**, never solver attachments or retrieval sources. Use separate contexts and file access for author, solver, and grader. `evaluation/private/` being ignored by Git is not access isolation: stage only an allowlisted input bundle for each role. If contamination occurs, disclose it and invalidate the sealed comparison rather than silently rerunning until favorable.

## Freeze before opening the final

Record a freeze manifest containing:

- Source IDs/hashes and roles; scope; ingestion review state; structured concept revision.
- Review, expanded, and compact artifact hashes, layout settings, ranking policy, and deletion/coverage logs.
- Author and solver model identifiers/versions, prompts, system settings, temperature, seed where supported, tools, retrieval policy, token/time budgets, and package versions.
- The predeclared number of trials, paired seeds where supported, grading rubric, metrics, and handling of refusals, incomplete answers, and tool failures.
- Common formula-page handling and the exact artifact supplied to each arm.

Finish development and freeze the build **before** exposing final question content. If a change is made afterward, preserve the original final result; any changed run is exploratory, not another sealed final. Version identifiers and seeds improve traceability but do not guarantee model reproducibility.

## Comparison arms

These labels name evaluation conditions, not concept tiers:

- **A — baseline solving:** final question paper and its exam-supplied formula page; no generated cheat sheet.
- **B — augmented solving:** the same question paper and identical exam-supplied formula page, plus the frozen compact cheat sheet.
- **C — evidence-only audit:** inspect the frozen source-to-claim mapping and sheet against final subparts after freeze. Record supported coverage, missing prerequisites, retrieval locations, unsupported claims, and citation quality. C does not solve or grade the exam and is not a third score-comparison arm.

A and B use fresh independent contexts and the same model, prompts apart from the sheet attachment, tool access, decoding settings, time/token budgets, and question order. Supply the formula page to **both** arms even if its formulas also appear on the sheet. Do not give B the expanded reference or review guide unless a separately preregistered experiment explicitly tests that package. Neither arm sees the answer key or the other's work. No online retrieval of exam answers.

C must not supply new content to B or retroactively alter the frozen sheet. Its audit should use evidence and questions, not the grader-only answer key. Distinguish formula presence from enough conditions and prerequisites to support use; coverage is not correctness or earned marks.

## Final grading ledger

The final has **105 points in 11 subparts**, not 100 points:

| Problem | Subparts in paper order | Maximum |
| --- | --- | ---: |
| P1 | 10, 10, 10, 10, 5, 10, 10, 10 | 75 |
| P2 | 10, 10, 10 | 30 |
| Total | 11 subparts | 105 |

Use the paper's actual subpart labels when available, preserving this ordered ledger. Do not invent a twelfth part or normalize the raw total to 100. A percentage, if shown, is `100 * earned / 105`.

The grader receives anonymized responses, the rubric, and grader-only official answers. Award partial credit consistently; cite each deduction to the rubric or answer reasoning. Store per-subpart maxima, earned points, and grading rationale. Check all bounds and sums. If the supplied paper conflicts with this ledger, stop and verify exam identity before running or silently changing the denominator.

Report A/B raw totals, percentage totals, paired point differences, subpart results, and failures. If multiple trials were predeclared, publish all of them and summarize variability; do not cherry-pick the best sample. Report C's supported/partial/missing evidence counts separately. One exam or one trial does not establish broad performance gains.

## Release record

State whether the run is `not_run`, `development`, `frozen_pending_final`, `completed`, or `invalidated`. Publish only artifacts whose source permissions permit publication. Retain grader-only files privately and publish enough hashes, settings, scoring rationale, and non-answer evidence to make the procedure auditable. Do not claim improvement, accuracy, or successful final coverage before the corresponding run and audit exist.
