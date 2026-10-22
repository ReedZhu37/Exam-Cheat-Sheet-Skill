"""Synthetic controller integrity checks; no actual materials or model calls."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from exam_cheat_sheet.compile import freeze_sheet, verify_freeze
from exam_cheat_sheet.evaluate import FINAL_WEIGHTS, score_grading


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import grade_exam
import prepare_exam
import run_isolated
import solve_exam


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


@pytest.fixture(autouse=True)
def no_model_calls(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError('Synthetic tests must not execute subprocesses or models')

    monkeypatch.setattr(subprocess, 'run', forbidden)


@pytest.fixture
def frozen_repo(tmp_path, monkeypatch):
    import exam_cheat_sheet.compile as compiler

    repo = tmp_path / 'repository'
    package = repo / 'src' / 'exam_cheat_sheet'
    package.mkdir(parents=True)
    module = package / 'compile.py'
    module.write_text('# synthetic package implementation\n', encoding='utf-8')
    monkeypatch.setattr(compiler, '__file__', str(module))
    for name, content in {
        'pyproject.toml': '[project]\nname = "synthetic"\n',
        'uv.lock': '# synthetic dependency lock\n',
        'scripts/run_isolated.py': '# synthetic evaluator\n',
        'schemas/manifest.schema.json': '{}\n',
    }.items():
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
    sheet = repo / 'sheet'
    sheet.mkdir()
    (sheet / 'cheatsheet.md').write_text('Synthetic frozen sheet.\n', encoding='utf-8')
    concepts = repo / 'concepts.json'
    concepts.write_text('{}\n', encoding='utf-8')
    freeze = repo / 'freeze.json'
    freeze_sheet(sheet, [concepts], freeze)
    return repo, freeze


def make_bundle(directory, *, split='dev', role='past_exam', freeze=None, count=2):
    directory.mkdir(parents=True)
    text = b'Synthetic exam text only.\n'
    (directory / 'exam.md').write_bytes(text)
    pages = []
    for number in range(1, count + 1):
        image = directory / f'page-{number:02d}.png'
        image.write_bytes(f'synthetic image {number}'.encode())
        pages.append({'page': number, 'image': image.name, 'image_sha256': sha(image.read_bytes())})
    ledger = {
        'schema_version': 1, 'split': split, 'role': role, 'source_id': 'synthetic-' + role,
        'pdf_hash': sha(b'synthetic PDF identity'), 'exam_text_hash': sha(text),
        'freeze_sha256': sha(freeze.read_bytes()) if freeze else None,
        'page_count': count, 'pages': pages,
    }
    (directory / 'pages.json').write_text(json.dumps(ledger), encoding='utf-8')
    return ledger


def write_ledger(directory, ledger):
    (directory / 'pages.json').write_text(json.dumps(ledger), encoding='utf-8')


def deny_reads(monkeypatch, *paths):
    originals = {path.resolve() for path in paths}
    original_open = Path.open

    def guarded(path, *args, **kwargs):
        if path.resolve() in originals:
            raise AssertionError(f'Material read before its gate: {path}')
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, 'open', guarded)


def final_grading():
    return {
        'items': [{'item_id': iid, 'max_points': weight, 'correct': True,
                   'rationale': 'Synthetic checked result.', 'official_anchor': 'synthetic:p1',
                   'sheet_references': [], 'error_type': 'none'}
                  for iid, weight in FINAL_WEIGHTS.items()],
        'total_points': 105, 'max_points': 105, 'correct_subparts': 11, 'total_subparts': 11,
        'notes': 'Synthetic judgment only.',
    }


def test_final_grader_rejects_normalized_duplicate_exploit():
    result = final_grading()
    result['items'].append(dict(result['items'][0], item_id='P1(a)'))
    result.update(total_points=115, max_points=115, correct_subparts=12, total_subparts=12)
    with pytest.raises(ValueError, match='Duplicate normalized'):
        grade_exam.validate_grading(result, 'A', True)


def test_generated_grading_is_scoring_cli_compatible(tmp_path):
    result = final_grading()
    result['items'][0]['item_id'] = '1(a)'
    original = copy.deepcopy(result)
    validated = grade_exam.validate_grading(result, 'A', True)
    assert result == original
    assert validated['group'] == 'A'
    assert validated['benchmark'] == 'mit-6041-final'
    assert validated['items'][0]['item_id'] == 'P1a'
    assert validated['items'][0]['error_type'] == 'none'
    path = tmp_path / 'grading.json'
    path.write_text(json.dumps(validated), encoding='utf-8')
    assert score_grading(path)['weighted_points'] == 105


@pytest.mark.parametrize('mutation', ['weights', 'rationale', 'partial', 'arithmetic'])
def test_grader_uses_strict_shared_scoring(mutation):
    result = final_grading()
    if mutation == 'weights':
        result['items'][0]['max_points'], result['items'][4]['max_points'] = 5, 10
    elif mutation == 'rationale':
        result['items'][0]['rationale'] = ''
    elif mutation == 'partial':
        result['items'][0]['awarded_points'] = 5
    else:
        result['total_points'] = 104
    with pytest.raises(ValueError):
        grade_exam.validate_grading(result, 'B', True)


def test_export_refuses_nonempty_directory_without_reading_pdf(tmp_path, monkeypatch):
    out = tmp_path / 'export'
    make_bundle(out, count=3)
    before = {p.name: p.read_bytes() for p in out.iterdir()}
    pdf = tmp_path / 'shorter.pdf'
    deny_reads(monkeypatch, pdf)
    with pytest.raises(ValueError, match='nonempty export'):
        prepare_exam.export(pdf, out)
    assert {p.name: p.read_bytes() for p in out.iterdir()} == before


@pytest.mark.parametrize('kind', ['image', 'text', 'extra_page', 'missing_page', 'page_order', 'traversal', 'absolute', 'duplicate_image'])
def test_bundle_rejects_corruption_and_unsafe_paths(tmp_path, kind):
    directory = tmp_path / 'bundle'
    ledger = make_bundle(directory)
    if kind == 'image':
        (directory / 'page-01.png').write_bytes(b'changed')
    elif kind == 'text':
        (directory / 'exam.md').write_text('changed', encoding='utf-8')
    elif kind == 'extra_page':
        (directory / 'page-03.png').write_bytes(b'stale')
    elif kind == 'missing_page':
        (directory / 'page-02.png').unlink()
    elif kind == 'page_order':
        ledger['pages'].reverse()
    elif kind == 'traversal':
        ledger['pages'][0]['image'] = '../outside.png'
    elif kind == 'absolute':
        ledger['pages'][0]['image'] = 'C:\\outside.png'
    else:
        ledger['pages'][1]['image'] = ledger['pages'][0]['image']
    write_ledger(directory, ledger)
    with pytest.raises(ValueError):
        prepare_exam.load_bundle(directory, 'past_exam')


def test_legacy_bundle_fails_clearly_without_reading_text(tmp_path, monkeypatch):
    directory = tmp_path / 'bundle'
    directory.mkdir()
    write_ledger(directory, {'page_count': 1, 'pages': []})
    deny_reads(monkeypatch, directory / 'exam.md')
    with pytest.raises(ValueError, match='Legacy.*new bundle'):
        prepare_exam.load_bundle(directory, 'past_exam')


@pytest.mark.parametrize('detection', ['path', 'split'])
@pytest.mark.parametrize('gate', ['missing', 'drifted'])
def test_final_preparation_gates_before_source_reads(frozen_repo, monkeypatch, detection, gate):
    repo, freeze = frozen_repo
    pdf = repo / ('sealed_test' if detection == 'path' else 'neutral') / 'synthetic.pdf'
    pdf.parent.mkdir()
    pdf.write_bytes(b'never parsed')
    if gate == 'drifted':
        (repo / 'sheet' / 'cheatsheet.md').write_text('changed', encoding='utf-8')
    deny_reads(monkeypatch, pdf)
    with pytest.raises(ValueError, match='requires --freeze|Freeze drift'):
        prepare_exam.export(pdf, repo / 'export', split='sealed_test' if detection == 'split' else None,
                            freeze=freeze if gate == 'drifted' else None)
    assert not (repo / 'export').exists()


@pytest.mark.parametrize('gate', ['missing', 'drifted', 'different_freeze'])
def test_final_bundle_gate_precedes_material_reads(frozen_repo, monkeypatch, gate):
    repo, freeze = frozen_repo
    directory = repo / 'neutral-bundle'
    make_bundle(directory, split='sealed_test', freeze=freeze)
    if gate == 'drifted':
        (repo / 'sheet' / 'cheatsheet.md').write_text('changed', encoding='utf-8')
    elif gate == 'different_freeze':
        frozen = json.loads(freeze.read_text(encoding='utf-8'))
        frozen['created_at'] = 'different valid snapshot identity'
        freeze.write_text(json.dumps(frozen), encoding='utf-8')
    deny_reads(monkeypatch, directory / 'exam.md', directory / 'page-01.png', directory / 'page-02.png')
    with pytest.raises(ValueError, match='requires --freeze|Freeze drift|freeze hash mismatch'):
        prepare_exam.load_bundle(directory, 'past_exam', None if gate == 'missing' else freeze)


def test_final_assisted_sheet_must_be_exact_frozen_path(frozen_repo, monkeypatch):
    repo, freeze = frozen_repo
    directory = repo / 'bundle'
    make_bundle(directory, split='sealed_test', freeze=freeze)
    bundle = prepare_exam.load_bundle(directory, 'past_exam', freeze)
    sheet = repo / 'sheet' / 'cheatsheet.md'
    substitute = repo / 'same-bytes.md'
    substitute.write_bytes(sheet.read_bytes())
    assert prepare_exam.load_sheet(sheet, bundle, freeze) == 'Synthetic frozen sheet.\n'
    deny_reads(monkeypatch, substitute)
    with pytest.raises(ValueError, match='frozen cheatsheet.md path'):
        prepare_exam.load_sheet(substitute, bundle, freeze)


def test_solution_bundle_cannot_reach_solver(tmp_path, monkeypatch):
    directory = tmp_path / 'official'
    make_bundle(directory, role='solution')
    deny_reads(monkeypatch, directory / 'exam.md', directory / 'page-01.png')
    with pytest.raises(ValueError, match='role mismatch'):
        prepare_exam.load_bundle(directory, 'past_exam')


def synthetic_pdf(path):
    from reportlab.pdfgen import canvas

    path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(path))
    pdf.drawString(72, 720, 'Synthetic exercise: add one and one.')
    pdf.showPage()
    pdf.save()


def inventory_for(repo, pdf, *, role='past_exam', split='sealed_test'):
    inventory = repo / 'inventory.json'
    entry = {'source_id': 'synthetic-exam', 'url': 'https://example.invalid/synthetic.pdf',
             'path': pdf.relative_to(repo / 'materials').as_posix(), 'sha256': sha(pdf.read_bytes()),
             'bytes': pdf.stat().st_size, 'role': role, 'split': split}
    inventory.write_text(json.dumps({'sources': [entry]}), encoding='utf-8')
    return inventory, entry


def test_final_export_and_bundle_roundtrip_uses_pinned_pdf(frozen_repo):
    repo, freeze = frozen_repo
    pdf = repo / 'materials' / 'sealed_test' / 'synthetic.pdf'
    synthetic_pdf(pdf)
    inventory, entry = inventory_for(repo, pdf)
    out = repo / 'export'
    prepare_exam.export(pdf, out, freeze=freeze, inventory=inventory,
                        source_id=entry['source_id'], root=repo / 'materials')
    bundle = prepare_exam.load_bundle(out, 'past_exam', freeze)
    assert bundle['metadata']['pdf_hash'] == entry['sha256']
    assert bundle['metadata']['source_id'] == entry['source_id']
    assert bundle['metadata']['split'] == 'sealed_test'
    assert bundle['metadata']['page_count'] == len(bundle['images']) == 1
    assert 'Synthetic exercise' in bundle['text']
    assert bundle['images'][0].read_bytes().startswith(b'\x89PNG')


@pytest.mark.parametrize('mutation', ['hash', 'bytes', 'path', 'role', 'split', 'missing_inventory'])
def test_final_preparation_rejects_unpinned_identity(frozen_repo, mutation):
    repo, freeze = frozen_repo
    pdf = repo / 'materials' / 'sealed_test' / 'synthetic.pdf'
    synthetic_pdf(pdf)
    inventory, entry = inventory_for(repo, pdf)
    if mutation == 'hash':
        entry['sha256'] = '0' * 64
    elif mutation == 'bytes':
        entry['bytes'] += 1
    elif mutation == 'path':
        other = pdf.with_name('other.pdf')
        other.write_bytes(pdf.read_bytes())
        entry['path'] = other.relative_to(repo / 'materials').as_posix()
    elif mutation == 'role':
        entry['role'] = 'solution'
    elif mutation == 'split':
        entry['split'] = 'dev'
    inventory.write_text(json.dumps({'sources': [entry]}), encoding='utf-8')
    with pytest.raises(ValueError):
        prepare_exam.export(pdf, repo / 'export', split='sealed_test', role='past_exam', freeze=freeze,
                            inventory=None if mutation == 'missing_inventory' else inventory,
                            source_id=entry['source_id'], root=repo / 'materials')
    assert not (repo / 'export').exists()


@pytest.mark.parametrize('controller', [solve_exam, grade_exam])
def test_rejected_rerun_preserves_original_prompt(tmp_path, monkeypatch, controller):
    out = tmp_path / 'attempt'
    out.mkdir()
    (out / 'prompt.md').write_bytes(b'original prompt')
    (out / 'response.md').write_bytes(b'original response')
    args = ['controller', '--exam', str(tmp_path / 'unread-exam'), '--out', str(out)]
    if controller is grade_exam:
        args += ['--official', str(tmp_path / 'unread-official'), '--response', str(out / 'response.md')]
    monkeypatch.setattr(sys, 'argv', args)
    with pytest.raises(ValueError, match='existing attempt'):
        controller.main()
    assert (out / 'prompt.md').read_bytes() == b'original prompt'
    assert (out / 'response.md').read_bytes() == b'original response'


def test_grader_requires_response_before_official_bundle(tmp_path, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['grade', '--exam', str(tmp_path / 'unread-exam'),
                                    '--official', str(tmp_path / 'unread-official'),
                                    '--response', str(tmp_path / 'absent.md'), '--out', str(tmp_path / 'attempt')])
    with pytest.raises(ValueError, match='existing --response'):
        grade_exam.main()
    assert not (tmp_path / 'attempt').exists()


@pytest.mark.parametrize('split,flag', [('dev', True), ('sealed_test', False)])
def test_grader_final_flag_must_match_bundle_metadata(frozen_repo, monkeypatch, split, flag):
    repo, freeze = frozen_repo
    for name, role in [('exam', 'past_exam'), ('official', 'solution')]:
        make_bundle(repo / name, split=split, role=role, freeze=freeze if split == 'sealed_test' else None)
    response = repo / 'answer.md'
    response.write_text('Synthetic answer.', encoding='utf-8')
    args = ['grade', '--exam', str(repo / 'exam'), '--official', str(repo / 'official'),
            '--response', str(response), '--out', str(repo / 'attempt'), '--freeze', str(freeze)]
    if flag:
        args += ['--final']
    monkeypatch.setattr(sys, 'argv', args)
    with pytest.raises(ValueError, match='--final must match'):
        grade_exam.main()
    assert not (repo / 'attempt' / 'prompt.md').exists()


@pytest.mark.parametrize('assisted', [False, True])
def test_final_solver_passes_only_verified_exam_and_bound_sheet(frozen_repo, monkeypatch, assisted):
    repo, freeze = frozen_repo
    directory = repo / 'exam'
    make_bundle(directory, split='sealed_test', freeze=freeze)
    out = repo / 'attempt'
    calls = []
    monkeypatch.setattr(subprocess, 'run', lambda command, **kwargs: calls.append(command))
    args = ['solve', '--exam', str(directory), '--freeze', str(freeze), '--out', str(out)]
    if assisted:
        args += ['--sheet', str(repo / 'sheet' / 'cheatsheet.md')]
    monkeypatch.setattr(sys, 'argv', args)
    solve_exam.main()
    assert len(calls) == 1
    assert calls[0][calls[0].index('--attach') + 1:] == [str(directory / f'page-{n:02d}.png') for n in (1, 2)]
    prompt = (out / 'prompt.md').read_text(encoding='utf-8')
    assert 'Synthetic exam text only.' in prompt
    assert ('Synthetic frozen sheet.' in prompt) == assisted
    assert {p.name for p in out.iterdir()} == {'prompt.md'}


def test_final_grader_pipeline_writes_cli_compatible_group_record(frozen_repo, monkeypatch):
    repo, freeze = frozen_repo
    for name, role in [('exam', 'past_exam'), ('official', 'solution')]:
        make_bundle(repo / name, split='sealed_test', role=role, freeze=freeze)
    response = repo / 'answer.md'
    response.write_text('Synthetic answer.', encoding='utf-8')
    out = repo / 'attempt'
    calls = []

    def fake_run(command, **kwargs):
        calls.append(command)
        (out / 'response.md').write_text(json.dumps(final_grading()), encoding='utf-8')

    monkeypatch.setattr(subprocess, 'run', fake_run)
    monkeypatch.setattr(sys, 'argv', ['grade', '--exam', str(repo / 'exam'), '--official', str(repo / 'official'),
                                    '--response', str(response), '--out', str(out), '--freeze', str(freeze),
                                    '--final', '--group', 'A'])
    grade_exam.main()
    score = score_grading(out / 'grading.json')
    assert score['group'] == 'A' and score['benchmark'] == 'mit-6041-final'
    assert score['item_count'] == 11 and score['weighted_points'] == 105
    assert calls[0][calls[0].index('--attach') + 1:] == [str(repo / name / f'page-{n:02d}.png')
                                                      for name in ('exam', 'official') for n in (1, 2)]


@pytest.mark.parametrize('existing', ['run.json', 'stderr.txt', 'events.jsonl', 'response.md'])
def test_runner_rejects_partial_or_completed_attempt_before_runtime_writes(tmp_path, monkeypatch, existing):
    out = tmp_path / 'attempt'
    out.mkdir()
    prompt = out / 'prompt.md'
    prompt.write_text('Synthetic prompt.', encoding='utf-8')
    (out / existing).write_text('original', encoding='utf-8')
    runtime = tmp_path / 'runtime'
    monkeypatch.setattr(sys, 'argv', ['run', '--prompt', str(prompt), '--out', str(out), '--runtime', str(runtime)])
    with pytest.raises(ValueError, match='existing run'):
        run_isolated.main()
    assert (out / existing).read_text(encoding='utf-8') == 'original'
    assert not runtime.exists()


@pytest.mark.parametrize('relative', ['scripts/run_isolated.py', 'schemas/manifest.schema.json', 'pyproject.toml', 'uv.lock'])
@pytest.mark.parametrize('change', ['edit', 'delete'])
def test_freeze_detects_evaluation_schema_and_dependency_drift(frozen_repo, relative, change):
    repo, freeze = frozen_repo
    assert relative in verify_freeze(freeze)['code_files']
    path = repo / relative
    if change == 'edit':
        path.write_text('changed', encoding='utf-8')
    else:
        path.unlink()
    with pytest.raises(ValueError, match='code'):
        verify_freeze(freeze)


@pytest.mark.parametrize('relative', ['scripts/new_controller.py', 'schemas/new.schema.json'])
def test_freeze_detects_implementation_additions(frozen_repo, relative):
    repo, freeze = frozen_repo
    (repo / relative).write_text('new', encoding='utf-8')
    with pytest.raises(ValueError, match='code'):
        verify_freeze(freeze)
