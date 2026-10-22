from pypdf import PdfReader

from exam_cheat_sheet.render import render_markdown


def test_formula_cannot_be_separated_from_applicability_conditions(tmp_path):
    source = tmp_path / 'sheet.md'
    source.write_text('\n'.join(['Filler'] * 62 + [
        'Formula: P(A|B)=P(A intersect B)/P(B)',
        'Variables: A and B are events.',
        'Conditions: P(B)>0.',
        'Formula source: synthetic page 1.',
    ]), encoding='utf-8')
    target = tmp_path / 'sheet.pdf'
    render_markdown(source, target, max_pages=2, min_font=9)
    pages = [p.extract_text() for p in PdfReader(target).pages]
    matching = [text for text in pages if 'Formula: P(A|B)' in text]
    assert len(matching) == 1
    assert 'Variables: A and B' in matching[0]
    assert 'Conditions: P(B)>0' in matching[0]
    assert 'Formula source:' in matching[0]
