"""Acquire only explicitly selected OCW resources; never download a course bundle."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE = 'https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/'
FILES = {
    'review': ('337c2b848282f31191196653a3fd7a45_MIT6_041SCF13_quiz01_revi.pdf', 'slides', 'train'),
    'train-exam': ('dd524390df7bb78133d1bff2fc5d13ae_MIT6_041SCF13_quiz01_s09.pdf', 'past_exam', 'train'),
    'train-solution': ('ce9cf1921235ff105c2f08ba70ccd487_MIT6_041SCF13_qu01_s09_sol.pdf', 'solution', 'train'),
    'dev-exam': ('658092a5b70f843d55476d84eb5b3510_MIT6_041SCF13_quiz01_f09.pdf', 'past_exam', 'dev'),
    'dev-solution': ('mit6_041scf09_qu01_sol_v2.pdf', 'solution', 'dev'),
    'final-exam': ('f168b1a65cbabf8a6c66bd00058745df_MIT6_041SCF13_quiz01.pdf', 'past_exam', 'sealed_test'),
    'final-solution': ('71ce04e1629139e5f120a73f43f683da_MIT6_041SCF13_quiz01_sol.pdf', 'solution', 'sealed_test'),
}


def fetch(url: str) -> bytes:
    # Native curl uses the platform trust store on Windows. Never disable TLS
    # verification to work around Python/OpenSSL missing intermediate roots.
    return subprocess.run(['curl.exe' if __import__('os').name == 'nt' else 'curl',
                           '--fail', '--silent', '--show-error', '--location',
                           '--proto', '=https', '--proto-redir', '=https',
                           '--max-time', '90', url], check=True, capture_output=True).stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage', choices=['train', 'dev', 'final-questions', 'final-solutions'], default='train')
    parser.add_argument('--root', type=Path, default=Path('.local/materials'))
    parser.add_argument('--manifest', type=Path, default=Path('benchmarks/mit-6041-quiz1/downloads.json'))
    parser.add_argument('--freeze', type=Path)
    args = parser.parse_args()
    if args.stage.startswith('final'):
        if not args.freeze:
            parser.error('final acquisition requires --freeze; create and verify the frozen sheet first')
        from exam_cheat_sheet.compile import verify_freeze
        verify_freeze(args.freeze)
    entries = dict(FILES)
    if args.stage == 'train':
        for i in range(1, 8):
            resource = BASE + f'resources/mit6_041scf13_l{i:02d}/'
            html = fetch(resource).decode('utf-8')
            links = re.findall(r'href="([^"]+\.pdf)"', html)
            match = next((s for s in links if f'_l{i:02d}.pdf' in s.lower()), None)
            if not match:
                raise RuntimeError(f'No verified lecture PDF link: {resource}')
            entries[f'lecture-{i}'] = (match.rsplit('/', 1)[-1], 'slides', 'train')
    selected = {
        'train': lambda k, v: v[2] == 'train',
        'dev': lambda k, v: v[2] == 'dev',
        'final-questions': lambda k, v: k == 'final-exam',
        'final-solutions': lambda k, v: k == 'final-solution',
    }[args.stage]
    manifest = json.loads(args.manifest.read_text(encoding='utf-8')) if args.manifest.exists() else {'sources': []}
    existing = {s['source_id']: s for s in manifest['sources']}
    for sid, (filename, role, split) in entries.items():
        if not selected(sid, (filename, role, split)):
            continue
        relative = Path(split) / f'{sid}.pdf'
        target = args.root / relative
        data = target.read_bytes() if target.exists() else fetch(BASE + filename)
        if not data.startswith(b'%PDF-'):
            raise ValueError(f'Not PDF: {sid}')
        digest = hashlib.sha256(data).hexdigest()
        if sid in existing and existing[sid]['sha256'] != digest:
            raise ValueError(f'Pinned hash mismatch: {sid}')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        from pypdf import PdfReader
        source = {
            'source_id': sid, 'title': f'MIT 6.041SC {sid}', 'author': 'MIT OpenCourseWare / John Tsitsiklis',
            'url': BASE + filename, 'path': relative.as_posix(), 'role': role, 'split': split,
            'license': 'CC-BY-NC-SA-4.0', 'retrieved_at': datetime.now(timezone.utc).isoformat(),
            'sha256': digest, 'bytes': len(data), 'pages': len(PdfReader(target).pages),
            'parser_version': None, 'page_range': None, 'extraction_status': 'needs_review',
            'assets': [], 'restrictions': ['Noncommercial; share adaptations alike; see source for third-party exceptions.'],
        }
        existing[sid] = source
        print(f'{sid}: {source["pages"]} pages, {len(data)} bytes, {digest}')
    manifest['sources'] = list(existing.values())
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
