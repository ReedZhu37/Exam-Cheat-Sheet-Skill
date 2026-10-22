"""Cross-layer contracts that catch schema/implementation drift."""
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from exam_cheat_sheet.compile import validate_concepts


ROOT = Path(__file__).resolve().parents[1]


def test_published_concept_schema_matches_compiler():
    record = {
        'concept_id': 'conditional', 'name': 'Conditional probability',
        'aliases': [], 'definition': 'Restrict probability to an observed event.',
        'formulas': [{'expression': 'P(A|B) = P(A & B)/P(B)',
                      'variables': {'A': 'event', 'B': 'observed event'},
                      'conditions': 'P(B)>0', 'source': {'source_id': 'notes', 'page': 1}}],
        'prerequisites': [], 'recognition': 'Given an event',
        'procedure': ['Restrict the sample space.'], 'pitfalls': ['Do not reverse conditioning.'],
        'sources': [{'source_id': 'notes', 'page': 1}],
        'evidence': [{'kind': 'teaching', 'source_id': 'notes', 'page': 1}],
        'scope_status': 'in', 'confidence': 'high',
    }
    schema = json.loads((ROOT / 'schemas/concept.schema.json').read_text(encoding='utf-8'))
    Draft202012Validator(schema).validate(record)
    assert validate_concepts({'title': 'Synthetic', 'scope': ['conditional'],
                              'sources': {'notes': {'split': 'train', 'role': 'notes', 'pages': 1}},
                              'concepts': [record]})['conditional'] == record


@pytest.mark.parametrize('revision', ['v1', 'v2'])
def test_published_example_schema_and_source_bounds(revision):
    path = ROOT / f'examples/mit-6041/concepts-{revision}.json'
    if not path.exists():
        pytest.skip('Example not authored yet')
    data = json.loads(path.read_text(encoding='utf-8'))
    validate_concepts(data)
    schema = json.loads((ROOT / 'schemas/concept.schema.json').read_text(encoding='utf-8'))
    validator = Draft202012Validator(schema)
    for concept in data['concepts']:
        validator.validate(concept)
    pins = json.loads((ROOT / 'benchmarks/mit-6041-quiz1/downloads.json').read_text(encoding='utf-8'))
    by_id = {s['source_id']: s for s in pins['sources']}
    for source in data['sources']:
        assert source['sha256'] == by_id[source['source_id']]['sha256']
        assert source['split'] == 'train'
