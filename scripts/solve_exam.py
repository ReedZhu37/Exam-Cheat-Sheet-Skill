"""Assemble equal-condition exam prompts, then launch a fresh isolated respondent."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

COMMON = '''Solve the attached probability exam. Give a complete answer to every distinct subpart, including requested proofs and intermediate reasoning. Repeated question/answer pages count once. Preserve original part labels. You may use your mathematical prior knowledge and the exam's own formula summary equally in every condition. You have no tools, outside sources, web search, previous sessions or official solutions. Page images are authoritative if extracted text is damaged. If information is unreadable, say so rather than invent it. Limit your response to 8000 words. At the end list any uncertain answers. Do not infer a grading key from source filenames.\n'''


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--exam', type=Path, required=True)
    p.add_argument('--sheet', type=Path)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--audit', action='store_true')
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    prompt = COMMON
    if args.audit:
        if not args.sheet:
            p.error('--audit requires --sheet')
        prompt = '''Perform a sheet-only coverage audit, NOT an unrestricted exam solution. For each distinct subpart, outline the required reasoning steps and cite the supplied sheet concept IDs for EVERY substantive rule. You may do arithmetic/algebra but may not invent absent probability rules. Mark a step NOT COVERED if its rule or needed worked strategy is absent. Label each subpart FULL, PARTIAL, or ABSENT. State full count / total distinct subparts. Formula summary inside the exam is also permitted with its page citation. Do not assume that general topic mention establishes coverage. Limit output to 8000 words.\n'''
    prompt += '\n# Exam text (all pages; images also attached)\n' + (args.exam / 'exam.md').read_text(encoding='utf-8')
    if args.sheet:
        prompt += '\n# Additional study sheet\n' + args.sheet.read_text(encoding='utf-8')
    target = args.out / 'prompt.md'
    target.write_text(prompt, encoding='utf-8')
    subprocess.run([sys.executable, str(Path(__file__).with_name('run_isolated.py')), '--prompt', str(target), '--out', str(args.out), '--attach', *map(str, sorted(args.exam.glob('page-*.png')))], check=True)


if __name__ == '__main__':
    main()
