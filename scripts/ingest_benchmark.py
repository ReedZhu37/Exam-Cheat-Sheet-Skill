"""Convert pinned download inventory to the canonical acquisition/ledger manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from exam_cheat_sheet.ingest import ingest_source
from exam_cheat_sheet.manifest import validate_manifest, authorize_source


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--downloads', type=Path, default=Path('benchmarks/mit-6041-quiz1/downloads.json'))
    p.add_argument('--root', type=Path, default=Path('.local/materials'))
    p.add_argument('--out', type=Path, default=Path('.local/extracted'))
    p.add_argument('--manifest', type=Path, default=Path('benchmarks/mit-6041-quiz1/manifest.json'))
    args = p.parse_args()
    inventory = json.loads(args.downloads.read_text(encoding='utf-8'))['sources']
    sources = [{
        'id': s['source_id'], 'path': s['path'], 'role': s['role'], 'split': s['split'],
        'status': 'pending', 'metadata': None,
        'provenance': {'origin': s['url'], 'license': s['license'], 'acquired_at': s['retrieved_at'],
                       'citation': s['author'] + ': ' + s['title'], 'notes': 'Downloaded file identity pinned in downloads.json; semantic fidelity remains review-required.'},
    } for s in inventory]
    manifest = {'schema_version': '1.0', 'sources': sources}
    validate_manifest(manifest, root=args.root)
    for source, pin in zip(sources, inventory):
        path = authorize_source(source, args.root, 'builder')
        if hashlib.sha256(path.read_bytes()).hexdigest() != pin['sha256'] or path.stat().st_size != pin['bytes']:
            raise ValueError(f'Download pin mismatch: {source["id"]}')
    manifest['sources'] = [ingest_source(source, args.root, args.out) for source in sources]
    # Keep published asset locators relocatable; the generic API returns absolute
    # paths, but this repository example uses repository-relative paths.
    repo = Path(__file__).resolve().parents[1]
    for source in manifest['sources']:
        for page in source['metadata']['pages']:
            if page.get('raster_path'):
                page['raster_path'] = Path(page['raster_path']).relative_to(repo).as_posix()
            for block in page.get('blocks', []):
                if block.get('asset_path'):
                    block['asset_path'] = Path(block['asset_path']).relative_to(repo).as_posix()
    validate_manifest(manifest, root=args.root)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Ingested {len(sources)} sources; {sum(s["metadata"]["page_count"] for s in manifest["sources"])} ledger pages')


if __name__ == '__main__':
    main()
