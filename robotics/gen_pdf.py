#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown", "pymupdf"]
# ///
import markdown
import fitz
from pathlib import Path

md_path = Path(__file__).parent / "resume.md"
pdf_path = Path(__file__).parent / "resume.pdf"

md_text = md_path.read_text(encoding="utf-8")
html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

CSS = """
body { font-family: "Noto Sans CJK SC", "Microsoft YaHei", sans-serif; font-size: 11pt; line-height: 1.55; color: #222; }
h1 { text-align: center; font-size: 20pt; margin-bottom: 0.1em; }
h2 { font-size: 13pt; border-bottom: 1px solid #444; padding-bottom: 2px; margin-top: 0.7em; }
h3 { font-size: 11.5pt; margin-top: 0.5em; margin-bottom: 0.2em; }
ul { padding-left: 1.5em; }
li { margin-bottom: 0.1em; }
a { color: #1a73e8; text-decoration: none; }
hr { border: none; border-top: 0.5px solid #ccc; margin: 0.4em 0; }
strong { color: #111; }
"""

html = f"<html><head><style>{CSS}</style></head><body>{html_body}</body></html>"

story = fitz.Story(html)
writer = fitz.DocumentWriter(str(pdf_path))
mediabox = fitz.paper_rect("a4")
content_rect = mediabox + (56, 42, -56, -42)  # margins

while True:
    dev = writer.begin_page(mediabox)
    more, _ = story.place(content_rect)
    story.draw(dev)
    writer.end_page()
    if not more:
        break

writer.close()
print(f"Generated: {pdf_path}")
