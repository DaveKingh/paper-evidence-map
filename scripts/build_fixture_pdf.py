#!/usr/bin/env python3
"""Build the synthetic PDF from its canonical Markdown source.

This maintainer utility uses only the Python standard library and writes a
small, text-first PDF. The hand-auditable ``paper.md`` remains the canonical
source. Run with ``--check`` to verify the distributed PDF without rewriting
it.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import textwrap
from pathlib import Path

from validate import check_pdf_fixture


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "examples" / "synthetic" / "paper.md"
DEFAULT_OUTPUT = ROOT / "examples" / "synthetic" / "paper.pdf"


def clean_markdown(text: str) -> str:
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", text)


def styled_lines(markdown: str) -> list[tuple[str, str]]:
    """Convert the fixture's small Markdown subset to styled text lines."""

    output: list[tuple[str, str]] = []
    for raw in markdown.splitlines():
        line = clean_markdown(raw.strip())
        if not line:
            output.append(("space", ""))
        elif line.startswith("# "):
            output.append(("title", line[2:].strip()))
        elif line.startswith("## "):
            output.append(("heading", line[3:].strip()))
        elif line.startswith("> "):
            for wrapped in textwrap.wrap(line[2:].strip(), width=92):
                output.append(("note", wrapped))
        elif line.startswith("|"):
            if re.fullmatch(r"\|?[\s|:-]+\|?", line):
                continue
            table_text = " | ".join(cell.strip() for cell in line.strip("|").split("|"))
            for wrapped in textwrap.wrap(table_text, width=112, subsequent_indent="  "):
                output.append(("table", wrapped))
        else:
            for wrapped in textwrap.wrap(line, width=94):
                output.append(("body", wrapped))
    return output


def pdf_escape(text: str) -> str:
    try:
        text.encode("latin-1")
    except UnicodeEncodeError as exc:
        raise ValueError("fixture PDF builder currently supports Latin-1 text only") from exc
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def command(font: str, size: float, x: float, y: float, text: str, color: str) -> str:
    return (
        f"q {color} rg BT /{font} {size:.1f} Tf "
        f"1 0 0 1 {x:.1f} {y:.1f} Tm ({pdf_escape(text)}) Tj ET Q"
    )


def paginate(lines: list[tuple[str, str]]) -> list[list[str]]:
    pages: list[list[str]] = [[]]
    y = 736.0
    bottom = 66.0
    styles = {
        "title": ("F2", 16.0, 22.0, 48.0, "0.08 0.22 0.29"),
        "heading": ("F2", 12.0, 18.0, 48.0, "0.08 0.22 0.29"),
        "note": ("F1", 8.5, 11.0, 54.0, "0.45 0.30 0.07"),
        "table": ("F3", 7.2, 10.0, 54.0, "0.12 0.18 0.22"),
        "body": ("F1", 9.2, 12.0, 48.0, "0.12 0.18 0.22"),
    }
    for style, text in lines:
        if style == "space":
            y -= 4.0
            continue
        font, size, leading, x, color = styles[style]
        if style == "heading":
            y -= 3.0
        if y - leading < bottom:
            pages.append([])
            y = 736.0
        pages[-1].append(command(font, size, x, y, text, color))
        y -= leading
    return pages


def content_stream(commands: list[str], page_number: int) -> bytes:
    header = command(
        "F2", 8.0, 48.0, 762.0, "PAPER EVIDENCE MAP  /  SYNTHETIC FIXTURE", "0.35 0.45 0.50"
    )
    rule = "q 0.82 0.87 0.89 RG 0.6 w 48 752 m 564 752 l S Q"
    footer = command("F1", 8.0, 48.0, 38.0, f"Synthetic fixture  |  Page {page_number}", "0.35 0.45 0.50")
    return ("\n".join([header, rule, *commands, footer]) + "\n").encode("latin-1")


def make_pdf(markdown: bytes) -> bytes:
    text = markdown.decode("utf-8")
    source_hash = hashlib.sha256(markdown).hexdigest()
    pages = paginate(styled_lines(text))
    if len(pages) != 2:
        raise ValueError(f"expected the fixture to fit on 2 pages; generated {len(pages)}")

    objects: dict[int, bytes] = {
        1: b"<< /Type /Catalog /Pages 2 0 R >>",
        3: b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        4: b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
        5: b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>",
    }
    page_ids: list[int] = []
    for index, page_commands in enumerate(pages):
        page_id = 6 + index * 2
        stream_id = page_id + 1
        page_ids.append(page_id)
        stream = content_stream(page_commands, index + 1)
        objects[page_id] = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
            f"/Contents {stream_id} 0 R >>"
        ).encode("ascii")
        objects[stream_id] = (
            f"<< /Length {len(stream)} >>\nstream\n".encode("ascii")
            + stream
            + b"endstream"
        )
    kids = " ".join(f"{item} 0 R" for item in page_ids)
    objects[2] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode("ascii")
    info_id = max(objects) + 1
    objects[info_id] = (
        "<< /Title (TinyRank synthetic evaluation fixture) "
        "/Author (Paper Evidence Map contributors) "
        f"/Subject (Canonical source SHA-256: {source_hash}) "
        "/Creator (scripts/build_fixture_pdf.py) >>"
    ).encode("ascii")

    document = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = {0: 0}
    for object_id in range(1, info_id + 1):
        offsets[object_id] = len(document)
        document.extend(f"{object_id} 0 obj\n".encode("ascii"))
        document.extend(objects[object_id])
        document.extend(b"\nendobj\n")
    xref = len(document)
    document.extend(f"xref\n0 {info_id + 1}\n".encode("ascii"))
    document.extend(b"0000000000 65535 f \n")
    for object_id in range(1, info_id + 1):
        document.extend(f"{offsets[object_id]:010d} 00000 n \n".encode("ascii"))
    document.extend(
        (
            f"trailer\n<< /Size {info_id + 1} /Root 1 0 R /Info {info_id} 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n"
        ).encode("ascii")
    )
    return bytes(document)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="canonical Markdown source")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="PDF destination")
    parser.add_argument(
        "--check",
        action="store_true",
        help="check the distributed PDF's integrity and key content without rewriting it",
    )
    args = parser.parse_args()

    if args.check:
        errors = check_pdf_fixture(ROOT)
        if errors:
            print("Synthetic PDF check: FAIL")
            for error in errors:
                print(f"  ERROR: {error}")
            return 1
        print("Synthetic PDF check: PASS (2 pages; key text is extractable)")
        return 0

    source = args.source.resolve()
    output = args.output.resolve()
    if not source.is_file():
        parser.error(f"source does not exist: {source}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(make_pdf(source.read_bytes()))
    print(f"Built {output} from {source}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
