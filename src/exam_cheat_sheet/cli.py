"""Command-line entry points for the original Python project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="exam-cheat-sheet")
    sub = parser.add_subparsers(dest="command", required=True)
    ingest = sub.add_parser("ingest", help="Ingest eligible sources from a manifest")
    ingest.add_argument("manifest", type=Path)
    ingest.add_argument("--root", type=Path, required=True)
    ingest.add_argument("--out", type=Path, required=True)
    ingest.add_argument("--access", choices=("builder", "evaluator", "grader", "final_evaluator", "final_grader"), default="builder")
    ingest.add_argument("--freeze", type=Path, help="Verified freeze required for final access")
    compile_cmd = sub.add_parser("compile", help="Compile an evidence-backed concept dataset")
    compile_cmd.add_argument("concepts", type=Path)
    compile_cmd.add_argument("--out", type=Path, required=True)
    compile_cmd.add_argument("--budget-words", type=int, default=2400)
    render = sub.add_parser("render", help="Render and verify a Unicode PDF")
    render.add_argument("markdown", type=Path)
    render.add_argument("--out", type=Path, required=True)
    render.add_argument("--max-pages", type=int, default=6)
    render.add_argument("--min-font", type=float, default=9)
    freeze = sub.add_parser("freeze", help="Freeze sheet outputs and inputs with SHA256")
    freeze.add_argument("--sheet", type=Path, required=True)
    freeze.add_argument("--inputs", type=Path, nargs="+", required=True)
    freeze.add_argument("--out", type=Path, required=True)
    score = sub.add_parser("score", help="Score an anchor-backed A/B grading record")
    score.add_argument("grading", type=Path)
    score.add_argument("--out", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "ingest":
            from .ingest import ingest_source
            from .manifest import ACCESS_POLICIES, load_manifest, validate_manifest

            final_kwargs = {}
            if args.access in {"final_evaluator", "final_grader"}:
                from .compile import verify_freeze

                if args.freeze is None:
                    raise ValueError("Final access requires --freeze")
                verify_freeze(args.freeze)
                final_kwargs["freeze"] = args.freeze
            elif args.freeze is not None:
                raise ValueError("--freeze is only used with final_evaluator/final_grader")
            manifest = load_manifest(args.manifest)
            validate_manifest(manifest, root=args.root)
            result = dict(manifest)
            result["sources"] = [
                ingest_source(source, args.root, args.out, access=args.access, **final_kwargs)
                if (source["split"], source["role"]) in ACCESS_POLICIES[args.access] else source
                for source in manifest["sources"]
            ]
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        elif args.command == "compile":
            from .compile import compile_concepts

            result = compile_concepts(args.concepts, args.out, args.budget_words)
        elif args.command == "render":
            from .render import render_markdown

            result = render_markdown(args.markdown, args.out, args.max_pages, args.min_font)
        elif args.command == "freeze":
            from .compile import freeze_sheet

            result = freeze_sheet(args.sheet, args.inputs, args.out)
        else:
            from .evaluate import score_grading

            result = score_grading(args.grading, args.out)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0
