#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
import fitz
from pathlib import Path

html_path = Path(__file__).parent / "resume.html"
pdf_path = Path(__file__).parent / "resume.pdf"

html = html_path.read_text(encoding="utf-8")

story = fitz.Story(html)
writer = fitz.DocumentWriter(str(pdf_path))
mediabox = fitz.paper_rect("a4")
content_rect = mediabox + (56, 42, -56, -42)

while True:
    dev = writer.begin_page(mediabox)
    more, _ = story.place(content_rect)
    story.draw(dev)
    writer.end_page()
    if not more:
        break

writer.close()
print(f"Generated: {pdf_path}")
