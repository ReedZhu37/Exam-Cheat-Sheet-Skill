"""Give official answers to an isolated grader only after a response exists."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--exam', type=Path, required=True)
    p.add_argument('--official', type=Path, required=True)
    p.add_argument('--response', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--final', action='store_true')
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    prompt = '''Independently grade the anonymous exam response against the supplied official solutions. Strict all-or-nothing scoring per distinct subpart: every requested result and proof must be correct for full points, otherwise 0. Accept equivalent mathematics and allowed unsimplified forms. Repeated answer pages do not create extra questions. No partial credit. Carefully check proofs, quantifiers, and multiple requests within a subpart. Do not search or use tools. Classify each error as content_missing, misleading_sheet, solving_error, extraction_damage, or none (do not infer sheet deficiencies when sheet is not supplied). Keep original question IDs. Give your result as exactly one JSON object, without Markdown fencing, with keys items (array), total_points, max_points, correct_subparts, total_subparts, notes. Each item must have item_id, max_points, correct (boolean), rationale (including all required results checked), official_anchor (PDF page and part), sheet_references (array; empty if unavailable), error_type. Limit response to 8000 words.\n'''
    if args.final:
        prompt += '\nFixed final rubric: P1(a-h) max 10,10,10,10,5,10,10,10 and P2(a-c) max 10,10,10. Exactly 11 subparts, total 105.\n'
    prompt += '\n# Exam\n' + (args.exam / 'exam.md').read_text(encoding='utf-8')
    prompt += '\n# Official solutions (grader-only)\n' + (args.official / 'exam.md').read_text(encoding='utf-8')
    prompt += '\n# Anonymous response\n' + args.response.read_text(encoding='utf-8')
    target = args.out / 'prompt.md'
    target.write_text(prompt, encoding='utf-8')
    images = [*sorted(args.exam.glob('page-*.png')), *sorted(args.official.glob('page-*.png'))]
    subprocess.run([sys.executable, str(Path(__file__).with_name('run_isolated.py')), '--prompt', str(target), '--out', str(args.out), '--attach', *map(str, images)], check=True)
    raw = (args.out / 'response.md').read_text(encoding='utf-8').strip()
    if raw.startswith('```'):
        raw = '\n'.join(raw.splitlines()[1:-1])
    result = json.loads(raw)
    items = result['items']
    if len({item['item_id'] for item in items}) != len(items):
        raise ValueError('duplicate grading items')
    if any(type(item['correct']) is not bool for item in items):
        raise ValueError('correct must be boolean')
    score = sum(item['max_points'] for item in items if item['correct'])
    maximum = sum(item['max_points'] for item in items)
    count = sum(item['correct'] for item in items)
    if (score, maximum, count, len(items)) != (result['total_points'], result['max_points'], result['correct_subparts'], result['total_subparts']):
        raise ValueError('grader arithmetic inconsistent; preserve original and review')
    if args.final and (maximum != 105 or len(items) != 11 or [item['max_points'] for item in items] != [10,10,10,10,5,10,10,10,10,10,10]):
        raise ValueError('final rubric mismatch')
    (args.out / 'grading.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Strict score: {score}/{maximum}; correct parts: {count}/{len(items)}')


if __name__ == '__main__':
    main()
