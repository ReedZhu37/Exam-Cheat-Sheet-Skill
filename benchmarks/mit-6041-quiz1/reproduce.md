# Reproduce or inspect the demonstration

Run from a fresh clone with `uv sync --locked`. The published artifacts are the
original observations. New model calls are **new runs**, not guaranteed replicas.
Do not overwrite an existing attempt directory.

## Check published frozen bytes and tests

```sh
uv run python -c "from exam_cheat_sheet.compile import verify_freeze; verify_freeze('benchmarks/mit-6041-quiz1/freeze.json'); print('verified')"
uv run pytest -q --basetemp .pytest-tmp
```

The freeze includes v2 outputs (including six previews), concept sources,
training/development inventories, training ledger, protocol, implementation
scripts/schemas/dependency declarations, and the evidence-byte Git attributes.
The final question/answer inventories and results were created **after** this
freeze and do not silently extend its training input set. Clone verification
has been run against an independent checkout.

To rebuild text/PDF into a separate destination:

```sh
uv run python -m exam_cheat_sheet compile examples/mit-6041/concepts-v2.json --out .local/rebuild-v2 --budget-words 3000
uv run python -m exam_cheat_sheet render .local/rebuild-v2/cheatsheet.md --out .local/rebuild-v2/cheatsheet.pdf --max-pages 6 --min-font 9
```

Platform fonts, PDF creation metadata, and native text line endings can change
new output bytes. Published frozen bytes are preserved exactly by Git attributes;
regeneration is a separate build, not replacement of the original observations.

## Acquire source PDFs

```sh
uv run python scripts/fetch_benchmark.py --stage train
uv run python scripts/fetch_benchmark.py --stage dev --manifest benchmarks/mit-6041-quiz1/dev-downloads.json
uv run python scripts/fetch_benchmark.py --stage final-questions --freeze benchmarks/mit-6041-quiz1/freeze.json --manifest benchmarks/mit-6041-quiz1/final-downloads.json
```

Downloads validate pinned SHA-256 values and use verified HTTPS. No course
bundle or separately copyrighted textbook is fetched. `ingest_benchmark.py`
can rebuild the training ledger; use `--manifest .local/rebuilt-manifest.json`
to retain the exact published freeze.

## New final runs (requires authenticated OpenCode V2)

```sh
uv run python scripts/prepare_exam.py .local/materials/sealed_test/final-exam.pdf --out .local/sealed_test/repeat-exam --split sealed_test --role past_exam --freeze benchmarks/mit-6041-quiz1/freeze.json --inventory benchmarks/mit-6041-quiz1/final-downloads.json --source-id final-exam

uv run python scripts/solve_exam.py --exam .local/sealed_test/repeat-exam --freeze benchmarks/mit-6041-quiz1/freeze.json --out .local/repeat-A
uv run python scripts/solve_exam.py --exam .local/sealed_test/repeat-exam --sheet examples/mit-6041/v2/cheatsheet.md --freeze benchmarks/mit-6041-quiz1/freeze.json --out .local/repeat-B
uv run python scripts/solve_exam.py --exam .local/sealed_test/repeat-exam --sheet examples/mit-6041/v2/cheatsheet.md --freeze benchmarks/mit-6041-quiz1/freeze.json --out .local/repeat-C --audit
```

Both A/B receive all 12 original page images and the same formula summary.
The agent denies every tool action; delivery metadata checks the actual
model/variant and image count. C is a separate sheet-only derivation audit.

Only after the independent answers exist:

```sh
uv run python scripts/fetch_benchmark.py --stage final-solutions --freeze benchmarks/mit-6041-quiz1/freeze.json --manifest benchmarks/mit-6041-quiz1/final-downloads.json
uv run python scripts/prepare_exam.py .local/materials/sealed_test/final-solution.pdf --out .local/sealed_test/repeat-official --split sealed_test --role solution --freeze benchmarks/mit-6041-quiz1/freeze.json --inventory benchmarks/mit-6041-quiz1/final-downloads.json --source-id final-solution
uv run python scripts/grade_exam.py --exam .local/sealed_test/repeat-exam --official .local/sealed_test/repeat-official --response .local/repeat-A/response.md --out .local/repeat-grade-A --final --group A --freeze benchmarks/mit-6041-quiz1/freeze.json
uv run python scripts/grade_exam.py --exam .local/sealed_test/repeat-exam --official .local/sealed_test/repeat-official --response .local/repeat-B/response.md --out .local/repeat-grade-B --final --group B --freeze benchmarks/mit-6041-quiz1/freeze.json
```

Each graded result can be passed directly to the `score` CLI. To regenerate
the published summary from the already preserved judgments and C classification:

```sh
uv run python scripts/summarize_results.py
```

The v1 development run used an earlier exporter before the final bundle
hardening. Its prompts, answers, image hashes, model metadata and raw judgments
are retained unchanged. Re-export dev PDFs to new directories with explicit
`--split dev --role past_exam` / `--role solution` to use the current controller.
Do not relabel a new dev run as the historical v1 observation.
