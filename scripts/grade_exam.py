"""Give official answers to an isolated grader only after a response exists."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from exam_cheat_sheet.evaluate import score_grading
from prepare_exam import load_bundle
from run_isolated import reserve_attempt


def validate_grading(result: dict, group: str = 'B', final: bool = False) -> dict:
    """Apply the scoring CLI's strict contract and retain the original judgments."""
    data = dict(result, group=group, benchmark='mit-6041-final' if final else 'mit-6041-dev')
    score = score_grading(data)
    actual = (score['weighted_points'], score['max_points'], score['correct_count'], score['item_count'])
    reported = tuple(result.get(key) for key in ('total_points', 'max_points', 'correct_subparts', 'total_subparts'))
    if any(type(value) not in (int, float) for value in reported) or actual != reported:
        raise ValueError('grader arithmetic inconsistent; preserve original and review')
    data['items'] = [dict(original, **validated) for original, validated in zip(result['items'], score['items'])]
    data['allow_partial'] = False
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--exam', type=Path, required=True)
    p.add_argument('--official', type=Path, required=True)
    p.add_argument('--response', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--final', action='store_true')
    p.add_argument('--freeze', type=Path)
    p.add_argument('--group', choices=['A', 'B'], default='B')
    args = p.parse_args()
    if not args.response.is_file():
        raise ValueError('An existing --response is required before loading official solutions')
    reserve_attempt(args.out)
    exam = load_bundle(args.exam, 'past_exam', args.freeze)
    official = load_bundle(args.official, 'solution', args.freeze)
    if exam['metadata']['split'] != official['metadata']['split']:
        raise ValueError('Exam and official solution splits must match')
    final = exam['metadata']['split'] == 'sealed_test'
    if args.final != final:
        raise ValueError('--final must match the bundles: required for sealed_test and forbidden for other splits')
    prompt = '''Independently grade the anonymous exam response against the supplied official solutions. Strict all-or-nothing scoring per distinct subpart: every requested result and proof must be correct for full points, otherwise 0. Accept equivalent mathematics and allowed unsimplified forms. Repeated answer pages do not create extra questions. No partial credit. Carefully check proofs, quantifiers, and multiple requests within a subpart. Do not search or use tools. Classify each error as content_missing, misleading_sheet, solving_error, extraction_damage, or none (do not infer sheet deficiencies when sheet is not supplied). Keep original question IDs. Give your result as exactly one JSON object, without Markdown fencing, with keys items (array), total_points, max_points, correct_subparts, total_subparts, notes. Each item must have item_id, max_points, correct (boolean), rationale (including all required results checked), official_anchor (PDF page and part), sheet_references (array; empty if unavailable), error_type. Limit response to 8000 words.\n'''
    if final:
        prompt += '\nFixed final rubric: P1(a-h) max 10,10,10,10,5,10,10,10 and P2(a-c) max 10,10,10. Exactly 11 subparts, total 105.\n'
    prompt += '\n# Exam\n' + exam['text']
    prompt += '\n# Official solutions (grader-only)\n' + official['text']
    prompt += '\n# Anonymous response\n' + args.response.read_text(encoding='utf-8')
    prompt += f'\nImage attachment order: first {len(exam["images"])} exam pages in order, then {len(official["images"])} official-solution pages in order. The two documents have independent page numbering.\n'
    target = args.out / 'prompt.md'
    target.write_text(prompt, encoding='utf-8')
    images = [*exam['images'], *official['images']]
    subprocess.run([sys.executable, str(Path(__file__).with_name('run_isolated.py')), '--prompt', str(target), '--out', str(args.out), '--attach', *map(str, images)], check=True)
    raw = (args.out / 'response.md').read_text(encoding='utf-8').strip()
    if raw.startswith('```'):
        raw = '\n'.join(raw.splitlines()[1:-1])
    result = validate_grading(json.loads(raw), args.group, final)
    (args.out / 'grading.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Strict score: {result["total_points"]}/{result["max_points"]}; correct parts: {result["correct_subparts"]}/{result["total_subparts"]}')


if __name__ == '__main__':
    main()
