# Render review — v2

Reviewed all six final PNG previews produced from `cheatsheet.pdf`, including
the re-rendered pages 5–6 after keeping each formula with its variables and
conditions. This is an on-screen visual review, not a physical printer test.

- A4, six pages, measured minimum font 9 pt; no clipping or glyph-bound
  violations. Page numbers, concept IDs, A/B/C labels, source locators and
  ASCII formula operators are readable in the previews.
- Formulas are plain text, not LaTeX. All 35 formula records preserve their
  source, variables and applicability conditions in the shared source.
- Some concepts continue onto the next page. Formula/variables/conditions
  groups stay together; continuation text and citations are retained.
- Course-content mathematical review is separately documented in
  `../source-review.md`; passing layout checks does not certify the mathematics.
- This is a study reference. Six pages and 9 pt are implementation budgets,
  not a claim about what this examination permits students to bring.

See `render-report.json` for measured page count, font sizes, bounds checks and
preview paths. No Chinese text occurs in this English course demonstration;
Chinese rendering is exercised separately by synthetic automated tests.
