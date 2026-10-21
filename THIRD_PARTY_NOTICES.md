# Third-party notices

Original project code and documentation: Copyright (c) 2026 ReedZhu37, MIT License. Third-party software and course content retain their own licenses. This inventory points to upstream licensing information; it does not replace the license and notice files required with redistributed distributions.

## Runtime and document libraries

| Component | Principal upstream license | Upstream |
| --- | --- | --- |
| Python | Python Software Foundation License; additional notices apply to included components | https://docs.python.org/3/license.html |
| pypdf | BSD-3-Clause | https://github.com/py-pdf/pypdf |
| pypdfium2 binding | Apache-2.0 or BSD-3-Clause; upstream documentation/examples are CC BY 4.0 | https://github.com/pypdfium2-team/pypdfium2 |
| PDFium, often bundled by pypdfium2 | BSD-style license plus licenses/notices for bundled dependencies | https://pdfium.googlesource.com/pdfium/ |
| ReportLab | BSD-style license | https://www.reportlab.com/opensource/ |
| python-pptx | MIT | https://github.com/scanny/python-pptx |
| python-docx | MIT | https://github.com/python-openxml/python-docx |
| jsonschema | MIT | https://github.com/python-jsonschema/jsonschema |

Transitive dependencies, optional OCR software, fonts, and platform-specific binary components have their own notices. The installed distribution is authoritative for the precise version and full component list; this table is not a complete binary redistribution manifest.

**PDFium redistribution:** retain pypdfium2's license files and the complete PDFium/bundled third-party notices shipped with the installed wheel or binary distribution. Consult upstream `LICENSES/` and `BUILD_LICENSES/` as well as the installed package's notices. Do not strip these files during packaging. The binding's permissive license does not supersede the licenses of its bundled components.

## Conceptual references

- [wyc79/cheatsheet-creator-skill](https://github.com/wyc79/cheatsheet-creator-skill): MIT License; copyright (c) 2026 wyc79.
- [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill): MIT License; copyright (c) 2026 ZeKaiNie.

These projects are acknowledged for ideas only. No source or skill text from them is incorporated in the original portable skill/documentation. No Anthropic proprietary document skill content is incorporated. The license of the referenced "Evan" material is unverified; no material from it is copied.

## Course material

MIT OpenCourseWare 6.041SC Fall 2013 course materials and derived examples are separate from the MIT-licensed software and are covered by CC BY-NC-SA 4.0, subject to source-specific exceptions. Retain the applicable attribution and identify adaptations. This notice does not imply that raw course files or solutions are bundled in the repository.

- Course: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
- Terms: https://ocw.mit.edu/pages/privacy-and-terms-of-use/
- License: https://creativecommons.org/licenses/by-nc-sa/4.0/

MIT and MIT OpenCourseWare do not endorse this project. See [docs/licensing.md](docs/licensing.md) for attribution and redistribution boundaries.
