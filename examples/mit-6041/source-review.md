# v1 source-review ledger

## Boundary and format

Authored `concepts-v1.json` from train material only. No dev, sealed, or final material was opened. The dataset has 23 concepts, ASCII math, per-formula page citations, variable dictionaries, conditions, prerequisites, recognition cues, procedures, pitfalls, and evidence. Page numbers are **one-based original PDF pages**, not extracted line numbers. Source metadata is copied from `benchmarks/mit-6041-quiz1/downloads.json`; source paths are relative to `.local/materials/`.

Exam evidence uses `exam_id: S2009` and original subitem IDs. Each cited exam subitem occurs only once in the evidence lists; its solution is supporting provenance, not another exam occurrence. No point weights or teacher-emphasis claims are supplied. Review scope is evidence of coverage, not evidence of special emphasis.

## Actual review performed

| Source | Text read | Images actually inspected | Limits |
| --- | --- | --- | --- |
| `review` | `.local/author/review/exam.md`, all original pages 1-27 | PNG pages **4-26 inclusive** | Pages 1-3 and 27 were text-only. Page 2 supplies the stated Chapters 1-2 / lectures 1-7 scope. All directly cited review formula pages were visually checked. |
| `train-exam` | `.local/author/train-exam/exam.md`, all pages 1-10 | PNG pages **1, 6, 7** | Other pages were extraction-only. Checked Q1 wording and the two Q3 joint tables directly. |
| `train-solution` | `.local/author/train-solution/exam.md`, all pages 1-11 | PNG pages **3, 4, 5, 6, 9, 10** | Other pages were extraction-only. Checked the aces, driving-test, conditional Bernoulli, bicycle, and stopping examples. |
| `lecture-4` | PDF tool's parsed text, pages 1-3 | **None** | Counting corroboration only; not a dataset source. No claim of slide visual verification. |
| `lecture-5` | PDF tool's parsed text, pages 1-3 | PDF-rendered **page 1** | Page 2 formulas were text-only; dataset uses visually checked review citations instead. |
| `lecture-6` | PDF tool's parsed text, pages 1-3 | PDF-rendered **page 2** | Verified geometric convention, memorylessness illustration, total expectation and conditional/joint PMFs. Page 1 was text-only. |
| `lecture-7` | PDF tool's parsed text, pages 1-3 | PDF-rendered **page 1** | Hat exercise on page 2 is text-reviewed, not visually verified; its answer is explicitly generated. Indicator formula citations use the visually checked review's Bernoulli and linearity statements. |
| `lecture-1`, `lecture-2`, `lecture-3` | Not opened | None | No coverage or visual-review claims. |

The PDF reader returned selected rendered pages along with parsed text; only the displayed pages listed above count as visually inspected. Reading all extracted text is not a complete visual review of any PDF.

## Formula and example decisions

- Reviewed probability axioms, overlap correction, conditional probability, path multiplication, total probability, Bayes trees, both notions of event independence, counting and labeled partitions in review pages 4-14.
- Checked PMF transformations, expectations, variance, joint/marginal/conditional laws, total expectation, and random-variable independence in review pages 15-25. ASCII `intersect`, `union`, `sum`, `product`, `C(n,k)`, and powers replace unreliable extracted symbols.
- Review page 26 visibly contains **Bernoulli, binomial, geometric, and discrete uniform**, including their means and variances. Geometric counts trials starting at one. Discrete uniform includes both endpoints.
- Complement probability, the cumulative PMF sum, and the indicator-sum mean are explicitly labeled corollaries/derivations in formula conditions or locators. Their references identify the actual supporting theorem; they do not pretend the exact derived expression was printed.
- The CDF notation is a useful derived threshold-sum convenience under the PMF concept, not evidence of an explicit CDF lesson. No independent CDF exam-frequency claim is made.
- Poisson and total variance are **not found in the reviewed review, exam, solution, or lecture 4-7 text**. They are omitted rather than inventing train citations or declaring them definitively outside the full course. Confirming their inclusion would require additional train evidence. Total expectation and independent-sum variance are included fully.
- Worked examples marked `Train` are concise paraphrases/calculations using the cited train item. Examples marked `Generated` are authored illustrations or extensions, not claimed source quotations or new exam evidence.
- The Bayes reverse question is generated from Q3's dice setup. It is not counted as a Bayes exam item. Direct table inspection gives first-pair doubles probability 2/5 and second-pair doubles probability 1/4; the mixture probability is 29/80 and the generated posterior is 24/29.

## Source discrepancies and limitations

1. **S2009 solution Q3(f), PDF page 9, contains a genuine arithmetic error.** Visual inspection shows `11*(1/(3/4))-11` followed by `11/12 = .9167`. The preceding expression equals **11/3**, the correct expected number of tails before eleven heads. The dataset records the correction explicitly. This is not an OCR correction.
2. **Q1(c) wording differs between exam and solution.** Exam page 1 asks which statement is false and says A and C are not independent in option (ii); solution text page 1 rewrites the question as which is true and says they are independent. The underlying probability example agrees. Dataset evidence identifies the original exam item and explains the events, avoiding option-letter answers.
3. Extracted summations, conditional bars, factorials, and tables are frequently mangled. Images, not malformed extracted expressions, governed the cited core formulas and Q3 table values.
4. Lecture handouts include fill-in blanks. Generated hat-example arithmetic is author-supplied reasoning from the exercise and verified general rules, not a claimed printed solution.
5. Full visual review of every exam/solution page was not performed. Formula references directly in the `formulas` arrays were visually checked, except that explicitly marked derived formulas cite their visually checked parent rules. Calculations in examples were independently reasoned through as well as compared with the cited sources.

## Structural verification

Read-only checks confirmed valid JSON, train-only provenance matching the manifest, valid citation page bounds, resolved prerequisite/scope IDs, unique exam evidence keys, and ASCII-only dataset text. The compact instructional core is approximately 1,900 whitespace-delimited words, including formulas, conditions, and variable descriptions; provenance and schema labels are excluded.

## Attribution

Adapted and paraphrased from MIT OpenCourseWare / John Tsitsiklis materials, as identified by the manifest. Manifest license: CC-BY-NC-SA-4.0, with source-specific third-party exceptions noted there. Preserve source attribution and applicable noncommercial/share-alike terms when redistributing this adaptation. See also `ATTRIBUTION.md`.
