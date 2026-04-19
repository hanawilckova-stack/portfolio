from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Output path
output_path = "/Users/hanawilckova/portfolio/Videolektor_case_study_texty.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=3*cm,
    rightMargin=3*cm,
    topMargin=3*cm,
    bottomMargin=3*cm,
)

# Colors
COLOR_ACCENT = colors.HexColor("#E8583D")
COLOR_TEXT = colors.HexColor("#1D1D1F")
COLOR_MUTED = colors.HexColor("#6E6E73")
COLOR_BG = colors.HexColor("#F2F1F5")

# Styles
styles = getSampleStyleSheet()

style_label = ParagraphStyle(
    "label",
    fontSize=7,
    textColor=COLOR_MUTED,
    spaceAfter=2,
    spaceBefore=0,
    leading=10,
    fontName="Helvetica-Bold",
    letterSpacing=1,
)

style_h1 = ParagraphStyle(
    "h1",
    fontSize=26,
    textColor=COLOR_TEXT,
    spaceAfter=6,
    spaceBefore=0,
    leading=30,
    fontName="Helvetica-Bold",
)

style_h2 = ParagraphStyle(
    "h2",
    fontSize=16,
    textColor=COLOR_TEXT,
    spaceAfter=8,
    spaceBefore=0,
    leading=20,
    fontName="Helvetica-Bold",
)

style_section_num = ParagraphStyle(
    "section_num",
    fontSize=8,
    textColor=COLOR_MUTED,
    spaceAfter=4,
    spaceBefore=0,
    leading=12,
    fontName="Helvetica",
    letterSpacing=0.5,
)

style_body = ParagraphStyle(
    "body",
    fontSize=10,
    textColor=COLOR_TEXT,
    spaceAfter=10,
    spaceBefore=0,
    leading=16,
    fontName="Helvetica",
)

style_italic = ParagraphStyle(
    "italic",
    fontSize=10,
    textColor=COLOR_MUTED,
    spaceAfter=10,
    spaceBefore=0,
    leading=16,
    fontName="Helvetica-Oblique",
)

style_step_title = ParagraphStyle(
    "step_title",
    fontSize=10,
    textColor=COLOR_TEXT,
    spaceAfter=2,
    spaceBefore=0,
    leading=14,
    fontName="Helvetica-Bold",
)

style_step_desc = ParagraphStyle(
    "step_desc",
    fontSize=9,
    textColor=COLOR_MUTED,
    spaceAfter=10,
    spaceBefore=0,
    leading=13,
    fontName="Helvetica",
)

style_meta_label = ParagraphStyle(
    "meta_label",
    fontSize=7,
    textColor=COLOR_MUTED,
    spaceAfter=1,
    spaceBefore=0,
    leading=10,
    fontName="Helvetica-Bold",
)

style_meta_value = ParagraphStyle(
    "meta_value",
    fontSize=9,
    textColor=COLOR_TEXT,
    spaceAfter=0,
    spaceBefore=0,
    leading=13,
    fontName="Helvetica-Bold",
)

# Build content
story = []

# Header note
story.append(Paragraph("INTERNÍ DOKUMENT KE SCHVÁLENÍ TEXTACE", style_label))
story.append(Spacer(1, 0.3*cm))
story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_ACCENT, spaceAfter=12))

# Title
story.append(Paragraph("Redesign uživatelského profilu Videolektor.cz", style_h1))
story.append(Spacer(1, 0.3*cm))

# Meta table
meta_data = [
    [Paragraph("KLIENT", style_meta_label), Paragraph("ROLE", style_meta_label),
     Paragraph("NÁSTROJ", style_meta_label), Paragraph("TYP", style_meta_label)],
    [Paragraph("Videolektor.cz", style_meta_value), Paragraph("UX Designer", style_meta_value),
     Paragraph("Figma, Claude Code", style_meta_value), Paragraph("Freelance", style_meta_value)],
]
meta_table = Table(meta_data, colWidths=[3.5*cm, 3.5*cm, 4.5*cm, 3.5*cm])
meta_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(meta_table)
story.append(Spacer(1, 0.6*cm))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E0DFE5"), spaceAfter=20))

# ── 01 Kontext a problém ──────────────────────────────────────────
story.append(Paragraph("01 · KONTEXT &amp; PROBLÉM", style_section_num))
story.append(Paragraph("Profil jako pouhý formulář", style_h2))
story.append(Paragraph(
    "Videolektor.cz je online vzdělávací platforma pro účetní fungující od roku 2013 "
    "s více než 2 000 předplatiteli. Redesign uživatelského profilu je jedním "
    "z větších projektů, které jsem pro ně realizovala.",
    style_body
))
story.append(Paragraph(
    "Původní profil byl v podstatě jen formulář. Chyběl přehled aktivity uživatelů, "
    "sekce byly oddělené a nepropojené. Uživateli se nikam neukládal jeho oblíbený "
    "obsah: rozkoukaná školení, absolvované kurzy ani položené dotazy. Neexistoval "
    "žádný dashboard, kde by uživatel hned na jednom místě našel svou aktivitu.",
    style_body
))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E0DFE5"), spaceAfter=16))

# ── 02 Můj proces ────────────────────────────────────────────────
story.append(Paragraph("02 · MŮJ PROCES", style_section_num))
story.append(Paragraph("Od průzkumu po návrh stavů", style_h2))

steps = [
    ("1", "Zmapování stávajícího stavu",
     "Vlastní průchod platformou, poznámky k problematickým místům a chybějícím prvkům."),
    ("2", "Definice rolí a jejich kombinací",
     "Tři hlavní role zákazníků (běžný uživatel, lektor školení, odborný poradce) a jejich možné kombinace."),
    ("3", "Návrh stavů profilu",
     "Tři různé pohledy: co vidí uživatel sám, co vidí ostatní, co vidí návštěvník bez předplatného."),
]

for num, title, desc in steps:
    step_data = [[
        Paragraph(f"<b>{num}</b>", ParagraphStyle("n", fontSize=9, textColor=colors.white,
                  fontName="Helvetica-Bold", alignment=1, leading=12)),
        [Paragraph(title, style_step_title), Paragraph(desc, style_step_desc)]
    ]]
    step_table = Table(step_data, colWidths=[0.7*cm, 13.8*cm])
    step_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("BACKGROUND", (0, 0), (0, 0), COLOR_ACCENT),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
        ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
    ]))
    story.append(step_table)
    story.append(Spacer(1, 0.15*cm))

story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E0DFE5"), spaceAfter=16))

# ── 03 Výzva ────────────────────────────────────────────────────
story.append(Paragraph("03 · VÝZVA", style_section_num))
story.append(Paragraph("Tři role uživatele, devět kombinací", style_h2))
story.append(Paragraph(
    "Největší výzva bylo zvládnout kombinace rolí. Platforma má tři hlavní role: "
    "uživatel, lektor a poradce a každá se může překrývat. Jeden člověk může být "
    "zároveň uživatel i lektor, nebo lektor i poradce.",
    style_body
))
story.append(Paragraph(
    "Zároveň jsem řešila tři různé pohledy na profil: co vidí uživatel sám, co vidí "
    "ostatní přihlášení uživatelé a co vidí návštěvník bez předplatného. Každý pohled "
    "vyžadoval jiné zobrazení dat a jiný přístup.",
    style_body
))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E0DFE5"), spaceAfter=16))

# ── 04 Výsledek ──────────────────────────────────────────────────
story.append(Paragraph("04 · VÝSLEDEK", style_section_num))
story.append(Paragraph("Profil jako dashboard aktivity", style_h2))
story.append(Paragraph(
    "Nový profil zobrazuje aktivitu na platformě: rozkoukaná školení, oblíbené "
    "položky, položené dotazy, absolvované testy, osvědčení. Přidala jsem možnost "
    "rychlého přepnutí do editace a celkově hravější vizuál.",
    style_body
))
story.append(Paragraph(
    "Prototyp je ve finální podobě a čeká na spuštění.",
    style_body
))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#E0DFE5"), spaceAfter=16))

# ── 05 Zpětný pohled ─────────────────────────────────────────────
story.append(Paragraph("05 · ZPĚTNÝ POHLED", style_section_num))
story.append(Spacer(1, 0.2*cm))
story.append(Paragraph(
    "Projekt ještě nebyl spuštěn — tuto sekci doplním po spuštění a po prvních "
    "datech z ostrého provozu.",
    style_italic
))

story.append(Spacer(1, 1*cm))
story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_ACCENT, spaceAfter=10))
story.append(Paragraph(
    "Hana Wilčková · UX Designer · hana@wilckova.cz",
    ParagraphStyle("footer", fontSize=7, textColor=COLOR_MUTED, fontName="Helvetica", leading=10)
))

# Build
doc.build(story)
print(f"PDF vytvořeno: {output_path}")
