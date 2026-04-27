#!/usr/bin/env python3
"""Build a deterministic character dossier PDF.

Default layout:
- Page 1: full art sheet
- Page 2: readable notes
"""
from __future__ import annotations

import argparse
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle


def parse_brief(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = [line.rstrip() for line in text.splitlines()]
    data: dict[str, object] = {"description": [], "sections": {}}
    current: str | None = None
    for line in lines:
        if not line:
            continue
        if line.startswith("#"):
            title = line.lstrip("# ").strip()
            if title.lower().startswith("character brief"):
                current = "description"
            else:
                current = title
                data["sections"].setdefault(current, [])  # type: ignore[index]
            continue
        if current is None:
            current = "description"
        if current == "description":
            data["description"].append(line.lstrip("- ").strip())  # type: ignore[index]
        else:
            data["sections"][current].append(line.lstrip("- ").strip())  # type: ignore[index]
    return data


def add_section(story: list, title: str, items: list[str], styles) -> None:
    if not items:
        return
    story.append(Paragraph(title, styles["HeadingNice"]))
    for item in items:
        story.append(Paragraph("• " + item, styles["BulletNice"]))


def fit_image(path: Path, max_w_mm: float, max_h_mm: float) -> Image:
    # Keep aspect ratio, fit in a box.
    from PIL import Image as PILImage
    im = PILImage.open(path)
    w, h = im.size
    scale = min(max_w_mm / w, max_h_mm / h)
    return Image(str(path), width=w * scale * mm, height=h * scale * mm)


def build_pdf(name: str, brief: Path, sheet: Path, output: Path, force: bool = False) -> None:
    if output.exists() and not force:
        raise SystemExit(f"Refusing to overwrite {output}; pass --force to replace it")
    output.parent.mkdir(parents=True, exist_ok=True)
    data = parse_brief(brief)
    description = " ".join(data["description"])  # type: ignore[index]
    sections: dict[str, list[str]] = data["sections"]  # type: ignore[assignment]

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleBig", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=colors.HexColor("#27222c")))
    styles.add(ParagraphStyle(name="Subtle", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#625766")))
    styles.add(ParagraphStyle(name="BodyNice", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=13, textColor=colors.HexColor("#2b2730")))
    styles.add(ParagraphStyle(name="HeadingNice", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, leading=15, textColor=colors.HexColor("#403047"), spaceBefore=6, spaceAfter=3))
    styles.add(ParagraphStyle(name="BulletNice", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=11.5, leftIndent=9, firstLineIndent=-7, textColor=colors.HexColor("#2b2730")))

    doc = SimpleDocTemplate(str(output), pagesize=landscape(A4), rightMargin=10*mm, leftMargin=10*mm, topMargin=9*mm, bottomMargin=9*mm)
    story: list = []

    # Page 1: pure art first. No title/header; readable notes live on page 2.
    story.append(fit_image(sheet, 277, 170))

    # Force page break with a large spacer is unreliable; use PageBreak import locally.
    from reportlab.platypus import PageBreak
    story.append(PageBreak())

    # Page 2: notes.
    story.append(Paragraph(name + " — Character Notes", styles["TitleBig"]))
    story.append(Paragraph("Deterministic text dossier. These notes are the source of readable character description, not generated image text.", styles["Subtle"]))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("Character description", styles["HeadingNice"]))
    story.append(Paragraph(description, styles["BodyNice"]))

    omitted_default_sections = {"Consistency rules / forbidden drift", "Forbidden drift", "QA notes", "QA / caveats"}
    preferred_order = [
        "Key visual elements",
        "Pose and expression notes",
        "Outfit and accessories",
        "Palette and materials",
        "Style bible",
    ]
    used = set()
    for title in preferred_order:
        if title in sections and title not in omitted_default_sections:
            add_section(story, title, sections[title], styles)
            used.add(title)
    for title, items in sections.items():
        if title not in used and title not in omitted_default_sections:
            add_section(story, title, items, styles)

    doc.build(story)
    print(f"saved {output}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--brief-md", required=True, type=Path)
    ap.add_argument("--sheet", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--force", action="store_true", help="Overwrite existing output PDF")
    args = ap.parse_args()
    build_pdf(args.name, args.brief_md, args.sheet, args.output, args.force)


if __name__ == "__main__":
    main()
