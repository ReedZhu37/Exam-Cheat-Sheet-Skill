"""Export every exam page as text and raster, preserving the supplied formula page."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path

from pypdf import PdfReader
import pypdfium2 as pdfium


def _sha(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def _sealed(path: Path) -> bool:
    return any(part.casefold() == 'sealed_test' for p in (path, path.resolve()) for part in p.parts)


def verified_freeze(freeze: Path | None, expected_hash: str | None = None) -> tuple[dict, str]:
    if freeze is None:
        raise ValueError('Final material requires --freeze')
    from exam_cheat_sheet.compile import verify_freeze

    frozen = verify_freeze(freeze)
    digest = _sha(freeze.read_bytes())
    if expected_hash is not None and digest != expected_hash:
        raise ValueError('Bundle freeze hash mismatch')
    return frozen, digest


def _bundle_file(directory: Path, name: str) -> Path:
    if not isinstance(name, str) or not name or name in {'.', '..'} or any(c in name for c in '/\\:'):
        raise ValueError('Unsafe bundle path')
    path = directory / name
    if not path.resolve().is_relative_to(directory.resolve()):
        raise ValueError('Bundle path escapes its directory')
    return path


def load_bundle(directory: Path, expected_role: str, freeze: Path | None = None) -> dict:
    """Validate a new-format export before returning any task text or images."""
    if _sealed(directory):
        verified_freeze(freeze)
    ledger_path = _bundle_file(directory, 'pages.json')
    try:
        ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ValueError('Missing or invalid bundle ledger; export a new bundle') from exc
    required = {'schema_version', 'split', 'role', 'source_id', 'pdf_hash', 'exam_text_hash',
                'freeze_sha256', 'page_count', 'pages'}
    if not isinstance(ledger, dict) or not required <= ledger.keys() or ledger['schema_version'] != 1:
        raise ValueError('Legacy or invalid bundle metadata; export a new bundle without modifying the old artifacts')
    if ledger['split'] not in {'train', 'dev', 'sealed_test'} or ledger['role'] != expected_role:
        raise ValueError('Bundle split or role mismatch')
    if _sealed(directory) and ledger['split'] != 'sealed_test':
        raise ValueError('Reserved sealed_test path contradicts bundle split')
    if not isinstance(ledger['source_id'], str) or not ledger['source_id']:
        raise ValueError('Bundle source_id is required')
    for key in ('pdf_hash', 'exam_text_hash'):
        digest = ledger[key]
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
            raise ValueError(f'Invalid bundle {key}')
    if ledger['split'] == 'sealed_test':
        if not isinstance(ledger['freeze_sha256'], str) or not ledger['freeze_sha256']:
            raise ValueError('Final bundle requires a freeze hash')
        verified_freeze(freeze, ledger['freeze_sha256'])
    elif ledger['freeze_sha256'] is not None:
        raise ValueError('Nonfinal bundle must not claim a final freeze')
    count, pages = ledger['page_count'], ledger['pages']
    if type(count) is not int or count < 1 or not isinstance(pages, list) or len(pages) != count:
        raise ValueError('Invalid bundle page count')
    images = []
    for number, page in enumerate(pages, 1):
        if not isinstance(page, dict) or type(page.get('page')) is not int or page['page'] != number:
            raise ValueError('Bundle pages must be exactly 1..page_count in order')
        image = _bundle_file(directory, page.get('image'))
        if image.suffix.lower() != '.png' or image in images:
            raise ValueError('Invalid or duplicate bundle image')
        images.append(image)
    if {p.name for p in directory.glob('*.png')} != {p.name for p in images}:
        raise ValueError('Bundle image inventory mismatch; stale or missing pages')
    text = _bundle_file(directory, 'exam.md').read_bytes()
    if _sha(text) != ledger['exam_text_hash']:
        raise ValueError('Bundle exam text hash mismatch')
    for page, image in zip(pages, images):
        if _sha(image.read_bytes()) != page.get('image_sha256'):
            raise ValueError('Bundle image hash mismatch')
    return {'metadata': ledger, 'text': text.decode('utf-8'), 'images': images}


def load_sheet(sheet: Path, bundle: dict, freeze: Path | None = None) -> str:
    """Read the assisted-condition sheet, bound to the final freeze when applicable."""
    if bundle['metadata']['split'] != 'sealed_test':
        return sheet.read_text(encoding='utf-8')
    frozen, _ = verified_freeze(freeze, bundle['metadata']['freeze_sha256'])
    expected = (freeze.resolve().parent / frozen['sheet'] / 'cheatsheet.md').resolve()
    if sheet.resolve() != expected:
        raise ValueError('Final assisted condition requires the frozen cheatsheet.md path')
    blob = sheet.read_bytes()
    if _sha(blob) != frozen['outputs'].get('cheatsheet.md'):
        raise ValueError('Final sheet hash mismatch')
    # Preserve read_text's universal-newline behavior after hashing exact bytes.
    return blob.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')


def export(pdf: Path, out: Path, *, split: str | None = None, role: str | None = None,
           freeze: Path | None = None, inventory: Path | None = None,
           source_id: str | None = None, root: Path = Path('.local/materials')):
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError('Refusing to overwrite a nonempty export directory; use a new directory')
    final = _sealed(pdf) or split == 'sealed_test'
    freeze_hash = None
    if final:
        _, freeze_hash = verified_freeze(freeze)
        if inventory is None or not source_id:
            raise ValueError('Final preparation requires --inventory and --source-id')
    pin = None
    if inventory is not None:
        entries = json.loads(inventory.read_text(encoding='utf-8'))['sources']
        matches = [entry for entry in entries if entry.get('source_id') == source_id]
        if len(matches) != 1:
            raise ValueError('Inventory requires one matching --source-id')
        pin = matches[0]
        if not {'source_id', 'url', 'path', 'sha256', 'bytes', 'role', 'split'} <= pin.keys():
            raise ValueError('Incomplete downloader inventory entry')
        if split is not None and split != pin['split'] or role is not None and role != pin['role']:
            raise ValueError('Inventory split or role mismatch')
        split, role = pin['split'], pin['role']
        final = final or split == 'sealed_test'
        if final:
            _, freeze_hash = verified_freeze(freeze)
        from exam_cheat_sheet.manifest import resolve_source

        if resolve_source(pin, root) != pdf.resolve():
            raise ValueError('Inventory path does not match the supplied PDF')
    split = split or ('sealed_test' if final else 'dev')
    role = role or 'past_exam'
    if split not in {'train', 'dev', 'sealed_test'} or role not in {'past_exam', 'solution'}:
        raise ValueError('Preparation requires a valid exam/solution split and role')
    if final and split != 'sealed_test':
        raise ValueError('Reserved sealed_test path contradicts source split')
    blob = pdf.read_bytes()
    if pin is not None and (_sha(blob) != pin['sha256'] or len(blob) != pin['bytes']):
        raise ValueError('Inventory PDF hash or byte count mismatch')
    out.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(io.BytesIO(blob), strict=True)
    parts, pages = [], []
    with pdfium.PdfDocument(blob) as doc:
        if not len(doc) or len(doc) != len(reader.pages):
            raise ValueError('PDF parser/render page counts disagree or PDF is empty')
        for i, page in enumerate(reader.pages):
            text = page.extract_text(extraction_mode='layout') or ''
            parts.append(f'## Original PDF page {i+1}\n\n{text}')
            image = out / f'page-{i+1:02d}.png'
            raster = doc[i]
            try:
                bitmap = raster.render(scale=1.6)
                try:
                    pil = bitmap.to_pil()
                    try:
                        pil.save(image)
                    finally:
                        pil.close()
                finally:
                    bitmap.close()
            finally:
                raster.close()
            pages.append({'page': i+1, 'image': image.name, 'image_sha256': _sha(image.read_bytes()), 'text_sha256': _sha(text.encode('utf-8'))})
    text_blob = '\n\n'.join(parts).encode('utf-8')
    (out / 'exam.md').write_bytes(text_blob)
    ledger = {'schema_version': 1, 'split': split, 'role': role, 'source_id': source_id or pdf.stem,
              'pdf_hash': _sha(blob), 'exam_text_hash': _sha(text_blob), 'freeze_sha256': freeze_hash,
              'page_count': len(pages), 'pages': pages}
    (out / 'pages.json').write_text(json.dumps(ledger, indent=2) + '\n', encoding='utf-8')
    print(f'Exported {len(pages)} pages to {out}')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf', type=Path)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--split', choices=['train', 'dev', 'sealed_test'])
    p.add_argument('--role', choices=['past_exam', 'solution'])
    p.add_argument('--freeze', type=Path)
    p.add_argument('--inventory', type=Path)
    p.add_argument('--source-id')
    p.add_argument('--root', type=Path, default=Path('.local/materials'))
    args = p.parse_args()
    export(args.pdf, args.out, split=args.split, role=args.role, freeze=args.freeze,
           inventory=args.inventory, source_id=args.source_id, root=args.root)
