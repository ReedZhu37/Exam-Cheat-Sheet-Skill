"""Export every exam page as text and raster, preserving the supplied formula page."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader
import pypdfium2 as pdfium


def export(pdf: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(pdf)
    doc = pdfium.PdfDocument(pdf)
    parts, pages = [], []
    for i, page in enumerate(reader.pages):
        text = page.extract_text(extraction_mode='layout')
        parts.append(f'## Original PDF page {i+1}\n\n{text}')
        image = out / f'page-{i+1:02d}.png'
        raster = doc[i]
        bitmap = raster.render(scale=1.6)
        bitmap.to_pil().save(image)
        bitmap.close()
        raster.close()
        pages.append({'page': i+1, 'image': image.name, 'image_sha256': hashlib.sha256(image.read_bytes()).hexdigest(), 'text_sha256': hashlib.sha256(text.encode()).hexdigest()})
    doc.close()
    (out / 'exam.md').write_text('\n\n'.join(parts), encoding='utf-8')
    (out / 'pages.json').write_text(json.dumps({'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'page_count': len(pages), 'pages': pages}, indent=2), encoding='utf-8')
    print(f'Exported {len(pages)} pages to {out}')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf', type=Path)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    export(args.pdf, args.out)
