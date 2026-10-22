"""Readable Unicode PDF rendering with measured bounds and raster verification."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


def _fonts() -> tuple[list[str], dict]:
    import reportlab
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase.ttfonts import TTFont

    windows = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
    candidates = [
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/local/share/fonts/DejaVuSans.ttf"),
        windows / "DejaVuSans.ttf", windows / "seguisym.ttf", windows / "segoeui.ttf",
        windows / "arial.ttf", windows / "cambria.ttc",
        Path(reportlab.__file__).parent / "fonts" / "Vera.ttf",
    ]
    names, maps = [], {}
    for i, candidate in enumerate(candidates):
        if not candidate.is_file():
            continue
        name = f"ExamUnicode{i}"
        try:
            font = TTFont(name, str(candidate))
            pdfmetrics.registerFont(font)
        except Exception:
            continue
        names.append(name)
        maps[name] = font.face.charToGlyph
    if not names:
        raise ValueError("No readable Unicode TrueType font found")
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    return names, maps


def render_markdown(source: str | Path, out: str | Path, max_pages: int = 6, min_font: float = 9) -> dict:
    """Render literal Unicode formulas; fail visibly if the constraints cannot hold."""
    import pypdfium2 as pdfium
    from pypdf import PdfReader
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfgen import canvas

    if type(max_pages) is not int or max_pages < 1:
        raise ValueError("max_pages must be a positive integer")
    if type(min_font) not in (int, float) or not 0 < min_font < 100:
        raise ValueError("min_font must be positive and below 100")
    raw = Path(source).read_text(encoding="utf-8")
    target = Path(out)
    target.parent.mkdir(parents=True, exist_ok=True)
    report_path = target.parent / "render-report.json"
    names, maps = _fonts()
    page_width, page_height = A4
    margin = 36.0
    usable = page_width - 2 * margin
    size = float(min_font)
    leading = size * 1.25
    content_bottom = margin + size * 3
    lines = []
    unsupported = set()

    def font_for(char: str) -> str:
        code = ord(char)
        if 0x3400 <= code <= 0x9FFF or 0x3000 <= code <= 0x303F or 0xFF00 <= code <= 0xFFEF:
            return "STSong-Light"
        for name in names:
            if code in maps[name]:
                return name
        unsupported.add(char)
        return names[0]

    # Measure each actual glyph. Prefer word boundaries, but split long tokens safely.
    for raw_line in raw.splitlines():
        heading = re.match(r"^(#{1,6})\s+", raw_line)
        text = raw_line[heading.end():] if heading else raw_line
        text = text.expandtabs(4).replace("\x00", "")
        font_size = size + (3 if heading and len(heading[1]) == 1 else 1 if heading else 0)
        chars = [(char, font_for(char)) for char in text]
        if not chars:
            lines.append(([], font_size, leading * 0.35, False, False))
            continue
        first_heading_line = bool(heading)
        while chars:
            width, end, last_space = 0.0, 0, 0
            while end < len(chars):
                char, font = chars[end]
                advance = pdfmetrics.stringWidth(char, font, font_size)
                if width + advance > usable:
                    break
                width += advance
                end += 1
                if char.isspace():
                    last_space = end
            if end == 0:
                raise ValueError("A glyph exceeds the available page width")
            if end < len(chars) and last_space:
                end = last_space
            chunk, chars = chars[:end], chars[end:]
            lines.append((chunk, font_size, font_size * 1.25, bool(heading), first_heading_line))
            first_heading_line = False
    if unsupported:
        report = {"passed": False, "max_pages": max_pages, "min_font": min_font,
                  "unsupported_characters": sorted(unsupported), "error": "No font supports these characters; replace with supported plain Unicode."}
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise ValueError(report["error"] + " " + repr("".join(sorted(unsupported))))
    pdf = canvas.Canvas(str(target), pagesize=A4)
    pdf.setTitle(Path(source).stem)
    page, baseline = 1, page_height - margin - size - 3
    boxes, fonts_used, font_sizes = [], set(), []

    def footer() -> None:
        pdf.setFont(names[0], size)
        pdf.drawCentredString(page_width / 2, margin + size, f"Page {page}")
        fonts_used.add(names[0])

    for line_index, (chars, font_size, height, is_heading, first_heading_line) in enumerate(lines):
        required_height = height
        rendered_text = ''.join(char for char, _ in chars)
        if rendered_text.startswith('Formula:'):
            # Keep the expression, variables and assumptions together.
            group_height = height
            for following_chars, _, following_height, following_heading, _ in lines[line_index + 1:]:
                following_text = ''.join(char for char, _ in following_chars)
                if following_heading or following_text.startswith(('Formula:', 'Procedure:')):
                    break
                group_height += following_height
                if following_text.startswith('Formula source:'):
                    required_height = group_height
                    break
            if required_height > page_height - margin - size - 3 - content_bottom:
                raise ValueError('A formula and its conditions cannot fit on one page')
        if first_heading_line:
            following_content = 0
            for following_chars, _, following_height, following_heading, _ in lines[line_index + 1:]:
                required_height += following_height
                if following_chars and not following_heading:
                    following_content += 1
                if following_content == 2:
                    break
            if required_height > page_height - margin - size - 3 - content_bottom:
                raise ValueError("Heading and its next two content lines cannot fit on one page")
        if baseline - required_height < content_bottom:
            footer()
            pdf.showPage()
            page += 1
            baseline = page_height - margin - size - 3
        x = margin
        # Group adjacent glyphs using the same font; do not interpret LaTeX or Markdown math.
        runs = []
        for char, font in chars:
            if runs and runs[-1][0] == font:
                runs[-1][1] += char
            else:
                runs.append([font, char])
        for font, text in runs:
            pdf.setFont(font, font_size)
            pdf.drawString(x, baseline, text)
            width = pdfmetrics.stringWidth(text, font, font_size)
            ascent, descent = pdfmetrics.getAscentDescent(font, font_size)
            boxes.append({"page": page, "x0": x, "y0": baseline + descent,
                          "x1": x + width, "y1": baseline + ascent})
            x += width
            fonts_used.add(font)
            font_sizes.append(font_size)
        baseline -= height
    footer()
    pdf.showPage()
    pdf.save()
    reader = PdfReader(str(target))
    actual_pages = len(reader.pages)
    # PDFium examines the finished PDF, independently of our layout calculations.
    document = pdfium.PdfDocument(str(target))
    previews, actual_boxes, actual_sizes, violations = [], 0, [], []
    try:
        for index in range(len(document)):
            rendered_page = document[index]
            try:
                textpage = rendered_page.get_textpage()
                try:
                    for char_index in range(textpage.count_chars()):
                        char = textpage.get_text_range(char_index, 1)
                        if not char.strip():
                            continue
                        left, bottom, right, top = textpage.get_charbox(char_index)
                        actual_boxes += 1
                        actual_sizes.append(float(pdfium.raw.FPDFText_GetFontSize(textpage.raw, char_index)))
                        if left < margin - 1 or bottom < margin - 1 or right > page_width - margin + 1 or top > page_height - margin + 1:
                            violations.append({"page": index + 1, "char_index": char_index, "box": [left, bottom, right, top]})
                finally:
                    textpage.close()
                preview = target.with_name(f"{target.stem}-page-{index + 1:03d}.png")
                bitmap = rendered_page.render(scale=1.5)
                try:
                    bitmap.to_pil().save(preview)
                finally:
                    bitmap.close()
                previews.append(str(preview))
            finally:
                rendered_page.close()
    finally:
        document.close()
    minimum_actual = min(actual_sizes) if actual_sizes else None
    layout_violations = [box for box in boxes if box["x0"] < margin - 0.01 or box["x1"] > page_width - margin + 0.01
                         or box["y0"] < margin - 0.01 or box["y1"] > page_height - margin + 0.01]
    passed = actual_pages <= max_pages and minimum_actual is not None and minimum_actual >= min_font - 0.01 and not violations and not layout_violations
    report = {"passed": passed, "pdf": str(target), "actual_pages": actual_pages, "max_pages": max_pages,
              "min_font": min_font, "actual_min_font": minimum_actual, "fonts": sorted(fonts_used),
              "page_size_points": [page_width, page_height], "margin_points": margin,
              "bounds_checked": actual_boxes, "bounds_violations": violations, "layout_bounds_violations": layout_violations,
              "previews": previews, "line_height_multiplier": 1.25, "page_numbers": True,
              "heading_keep_content_lines": 2, "formula_mode": "literal plain Unicode; LaTeX is not typeset"}
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not passed:
        raise ValueError(f"Render constraints failed; see {report_path}")
    return report
