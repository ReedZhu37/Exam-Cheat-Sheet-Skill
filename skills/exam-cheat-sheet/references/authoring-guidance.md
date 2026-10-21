# Semantic authoring and compression

## The authoring loop

Work in coherent topic batches, not arbitrary keyword counts. For each batch:

1. Read the scope and all relevant ingestion units, viewing equations and figures as needed.
2. State the conceptual distinction being taught, its assumptions, and what a learner needs to recognize in a new problem.
3. Write a concept record and claim-level citations. Explain any inference rather than presenting it as a quotation.
4. Connect prerequisites and map supported exam subparts. Reconcile notation and conflicting source statements explicitly.
5. Check the claims back against the sources. Mark unresolved issues; do not silently complete a missing equation from memory.
6. Save the authored records and their provenance before generating output views.

An LLM call or agent turn must carry out these steps. Extraction, heuristic title detection, term frequency, and template filling are preparation aids, not semantic synthesis. If semantic authoring has not happened, report `extracted; awaiting authoring`, not `cheat sheet complete`.

Useful compact entries contain a recognition cue, rule, applicability conditions, and one common trap. Review entries additionally explain why the method works and show a worked path. Label invented practice examples as author-created, verify the reasoning, and keep them separate from cited historical exam evidence. Never manufacture a teacher's voice or emphasis.

## Explainable priority tiers

Priority tiers **A/B/C are content ranks** and are unrelated to evaluation arms A/B/C.

Apply protections before using historical frequency to choose space allocation:

- **A — protected/core:** explicitly required scope items and the transitive prerequisites necessary to use them. Explain each protection with a scope citation or prerequisite path. Strong documented emphasis or repeated, substantial train-exam evidence may also justify A; record that justification rather than implying scope protection.
- **B — supporting:** useful in-scope elaboration, corroborated applications, or contextual material with evidence but no protection. Order with unique-exam frequency, allocated points, relevance, and uncertainty visible separately.
- **C — optional/defer:** redundant detail, weakly supported enrichment, and out-of-scope material not required as a prerequisite. Explain why it is optional. Low historical frequency alone cannot put required scope or a necessary prerequisite here.

Store the component facts and a short rank rationale. Do not hide policy inside a single unexplained numeric score. With only one train exam, `1/1` means observed once, not reliable prediction of the final. New topics can be protected even when frequency is zero.

Detect missing prerequisite IDs and cycles. A cycle may reflect a bad decomposition: revise it or document a co-requisite group. An explicitly excluded topic that is genuinely necessary for an included one is a scope conflict to resolve, not a reason to silently delete the prerequisite.

## Three views, one authored source

| View | Purpose | Content |
| --- | --- | --- |
| Review guide | Learning and preparation | Definitions, intuition, prerequisites, worked reasoning, practice cues, uncertainty, references |
| Evidence-expanded reference | Inspectability | Rules, conditions, provenance, exam mappings, rank reasons, detailed citations, unresolved issues |
| Compact cheat sheet | Fast retrieval | Essential rules, conditions, decision cues, minimal notation key, compact citation/claim IDs |

Keep compact citation IDs resolvable in the expanded reference. Expanded evidence is not permission to copy complete solutions or turn the compact artifact into an answer key. Each view uses the same concept revision and should declare its build ID.

## Compression order

1. Remove literal duplication and merge genuinely equivalent notation.
2. Shorten prose while preserving quantifiers, conditions, units, boundary cases, and symbol definitions.
3. Move long derivations and secondary examples to the review/expanded views.
4. Defer optional C material, then lower-value B elaborations, with an omission record.
5. If protected content still cannot fit legibly, report the conflict and ask which constraint can change. Keep an explicitly incomplete draft instead of silently removing A material or shrinking below the agreed font limit.

Recheck the shortened formula, not just its original. A rule that omits independence, positivity, support, or conditioning assumptions is not an equivalent abbreviation. Show figure information with a checked diagram or an adequate textual substitute; "see diagram" without the diagram is a gap.

## Review gates

- **Ingestion:** every included unit accounted for; all evidence-bearing OCR/math/figure issues reviewed or visibly blocked.
- **Knowledge:** claims supported; derivations labeled; scope and prerequisite closure checked; emphasis cited.
- **Evidence:** unique exams deduplicated; splits respected; subpart allocations conserved; unknowns retained.
- **Views:** IDs/revisions agree; every omission logged; compact references resolve; conditions survive compression.
- **Print:** actual page dimensions, font sizes, sides, clipping, equation glyphs, line breaks, and visual density inspected from rendered output.

Passing a schema is necessary for machine processing, but is not evidence that a mathematical claim or a page layout is correct.
