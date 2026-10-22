# Development revision: v1 → v2

## Observed results

Fall 2009 Quiz 1, publicly provided **Problem B, 98 points / 10 subparts**.
The published PDF contains repeated answer pages; these were not counted twice.
One independent v1-assisted respondent scored **98/98, 10/10**, using the same
strict all-or-nothing rule fixed for this project. A separate sheet-only audit
found all 10 subparts derivable from the sheet plus the original formula page.
These are developer-set diagnostics, not held-out generalization evidence.

No missing theorem or misleading formula was established. v2 therefore makes
three **clarity/lookup improvements**, not a claimed correction of wrong v1
answers or a demonstrated score gain:

| Concept | Development evidence | Revision | Train grounding |
| --- | --- | --- | --- |
| `geometric` | Dev 3(a), audit's parameter qualification: the stopping event is “unripe”; endpoints need care | Name stopping event first; explicitly dispatch p=0 and p=1 before using finite waiting-time formulas | Review p.26 and lecture-6 p.2; direct consequences of the stated geometric domain |
| `transformed-variables` | Dev 3(c): obtain joint support by solving two event equations | Put inverse-event constraints, integer support, then mass evaluation into one ordered procedure | Review pp.16,20: preimage summation, applied to a pair of outputs |
| `rv-independence` | Dev 3(d)(i) audit uses an impossible pair with positive marginals, with endpoint caveat | Make this counterexample strategy explicit; identify the constant-variable edge case | Review pp.24–25: universal PMF factorization criterion |

All 35 formula records and their conditions/variables remain unchanged. The
same 23 scope concepts and train-only exam evidence remain. Dev subjects are
not added to frequency counts. No final questions or solutions were available
to the author at revision time. Source-wide extraction status remains
`needs_review`; formula-specific inspection is recorded in `source-review.md`.

Reproduce the transformation:

```sh
uv run python scripts/revise_example.py
uv run python -m exam_cheat_sheet compile examples/mit-6041/concepts-v2.json --out examples/mit-6041/v2 --budget-words 3000
uv run python -m exam_cheat_sheet render examples/mit-6041/v2/cheatsheet.md --out examples/mit-6041/v2/cheatsheet.pdf --max-pages 6 --min-font 9
```

v1 is retained. No second development solution is reported as a new test.
