#!/usr/bin/env python3
"""Render the canonical specification with Pandoc and WeasyPrint (no network assets).
Usage: python3 tools/render_pdf.py /absolute/path/to/output.pdf
Reference environment: Pandoc 3.1.11.1, WeasyPrint 68.0, Noto Serif and Noto Sans.
This reproduces the layout; exact bytes can vary with tool/font versions.
"""
import argparse, html, re, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser(description=__doc__);p.add_argument('output',type=Path);args=p.parse_args()
out=args.output.expanduser().resolve()
body=subprocess.run(['pandoc','--from=gfm','--to=html5',str(ROOT/'SPECIFICATION.md')],check=True,capture_output=True,text=True).stdout
# Per-table column layouts; default proportions for new tables are reusable.
# Keys are the first visible cell of each table, not page numbers.
TABLE_WIDTHS = {
    'Document': (27, 73), 'Domain': (40, 60),
    'Kind': (22, 31, 47), 'Layer': (23, 48, 29),
    'Label': (30, 70), 'Check': (44, 56), 'Term': (29, 71),
    'Field': (29, 71), 'Basis': (22, 39, 39),
    'Class': (25, 39, 36), 'State': (20, 40, 40),
    'Answer state': (22, 30, 48), 'ID': (9, 36, 13, 10, 32),
    'Category': (26, 46, 28), 'Property (hypothetical)': (45, 55),
    'Item': (30, 70),
}
def size_table(match):
    opening, rest = match.group(1), match.group(2)
    row = re.search(r'<tr(?:\s[^>]*)?>(.*?)</tr>', rest, re.S)
    if row is None or re.search(r'<colgroup\b', rest):
        return match.group(0)
    cells = re.findall(r'<t[dh]\b[^>]*>(.*?)</t[dh]>', row.group(1), re.S)
    if not cells: return match.group(0)
    key = html.unescape(re.sub(r'<[^>]+>', '', cells[0])).strip()
    widths = TABLE_WIDTHS.get(key)
    if widths is None or len(widths) != len(cells):
        widths = {2: (28, 72), 3: (25, 37, 38)}.get(len(cells), (100/len(cells),)*len(cells))
    cols = ''.join(f'<col style="width:{w:.4f}%">' for w in widths)
    return opening + '<colgroup>' + cols + '</colgroup>' + rest
body = re.sub(r'(<table\b[^>]*>)(.*?</table>)', size_table, body, flags=re.S)
headings=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',body,re.S)
assert len(headings)>=10
nav='<nav id="contents"><h2>Contents</h2><ol>'+''.join(f'<li><a href="#{html.escape(i)}">{t}</a></li>' for i,t in headings if re.match(r'\d+\.',t) or t in ('References','Acknowledgement of AI assistance','Authorship note on tikanga, te reo Māori and Te Tiriti','Licence and notices'))+'</ol></nav>'
# TOC immediately before the first numbered section, not before the cover metadata.
first=re.search(r'<h2 id="[^"]+">1\. Scope</h2>',body)
assert first
body=body[:first.start()]+nav+body[first.start():]
# Make relative links to repository material usable in the archived PDF.
body=re.sub(r'href="(?!https?://|mailto:|#)([^"<>]+)"',lambda m:'href="https://github.com/KNIT-NZ/authority-aware-ai/tree/v0.6.1/'+m.group(1)+'"',body)
css=(ROOT/'tools/publication.css').read_text()
logo=(ROOT/'assets/knit-logo.png').resolve().as_uri()
body='<div class="cover-logo"><img src="'+logo+'" alt="KNIT logo"></div>'+body
page='''<!DOCTYPE html><html lang="en-NZ"><head><meta charset="UTF-8"><title>KNIT WD-0000 · Authority-Aware AI</title><meta name="author" content="Brendan McBryde, KNIT"><meta name="description" content="Working Draft 0.6.1; DOI 10.5281/zenodo.24546015"><style>'''+css+'</style></head><body>'+body+'</body></html>'
with tempfile.TemporaryDirectory() as d:
 f=Path(d)/'publication.html';f.write_text(page,encoding='utf-8');subprocess.run(['weasyprint','--allowed-protocols','file,data','--pdf-tags',str(f),str(out)],check=True)
