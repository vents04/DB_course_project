#!/usr/bin/env python3
"""Generate a professional PDF presentation for the UniCredit Bulbank complaint digitalization project."""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

# --- Font Registration ---
FONT_PATHS = {
    "Arial": "/System/Library/Fonts/Supplemental/Arial.ttf",
    "ArialBold": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "ArialNarrow": "/System/Library/Fonts/Supplemental/Arial Narrow.ttf",
    "ArialUnicode": "/Library/Fonts/Arial Unicode.ttf",
}

for name, path in FONT_PATHS.items():
    if os.path.exists(path):
        pdfmetrics.registerFont(TTFont(name, path))

FONT = "Arial"
FONT_BOLD = "ArialBold"
FONT_NARROW = "ArialNarrow"

# --- Color Palette ---
NAVY = HexColor("#1a2744")
DARK_BLUE = HexColor("#1e3a5f")
MEDIUM_BLUE = HexColor("#2d6da3")
LIGHT_BLUE = HexColor("#e8f0fe")
GOLD = HexColor("#c8963e")
WARM_GOLD = HexColor("#d4a843")
DARK_TEXT = HexColor("#2c3e50")
GRAY_TEXT = HexColor("#5d6d7e")
LIGHT_GRAY = HexColor("#ecf0f1")
OFF_WHITE = HexColor("#f8f9fa")
TEAL = HexColor("#1a7a6d")
CORAL = HexColor("#c0392b")
GREEN = HexColor("#27ae60")

# Speaker accent colors
SPEAKER_COLORS = {
    1: MEDIUM_BLUE,  # Венцислав
    2: TEAL,         # Максим
    3: CORAL,        # Петър
}

# --- Page Setup ---
PAGE_W, PAGE_H = landscape(A4)
MARGIN = 40
HEADER_H = 65
FOOTER_H = 35
SIDEBAR_W = 8


def draw_background(c):
    """Draw the white background."""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_header(c, title, subtitle=None, speaker=0):
    """Draw the top header bar with title."""
    # Header background
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)

    # Gold accent line
    c.setFillColor(GOLD)
    c.rect(0, PAGE_H - HEADER_H - 3, PAGE_W, 3, fill=1, stroke=0)

    # Speaker sidebar accent
    if speaker in SPEAKER_COLORS:
        c.setFillColor(SPEAKER_COLORS[speaker])
        c.rect(0, FOOTER_H, SIDEBAR_W, PAGE_H - HEADER_H - 3 - FOOTER_H, fill=1, stroke=0)

    # Title text
    c.setFillColor(white)
    c.setFont(FONT_BOLD, 22)
    c.drawString(MARGIN + 10, PAGE_H - 42, title)

    if subtitle:
        c.setFont(FONT, 13)
        c.setFillColor(HexColor("#b0c4de"))
        c.drawString(MARGIN + 10, PAGE_H - 58, subtitle)


def draw_footer(c, slide_num, total=22):
    """Draw footer with slide number and project info."""
    # Footer background
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, FOOTER_H, fill=1, stroke=0)

    # Gold top line
    c.setFillColor(GOLD)
    c.rect(0, FOOTER_H, PAGE_W, 2, fill=1, stroke=0)

    # Footer text
    c.setFillColor(HexColor("#8899aa"))
    c.setFont(FONT_NARROW, 9)
    c.drawString(MARGIN, 14, "ТУ — София  |  Дигитализация в банкирането  |  Курсов проект 2026")

    # Slide number
    c.setFillColor(GOLD)
    c.setFont(FONT_BOLD, 11)
    c.drawRightString(PAGE_W - MARGIN, 14, f"{slide_num} / {total}")


def draw_box(c, x, y, w, h, fill_color=LIGHT_BLUE, border_color=None, radius=6):
    """Draw a rounded rectangle box."""
    c.setFillColor(fill_color)
    if border_color:
        c.setStrokeColor(border_color)
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)


def draw_bullet_list(c, x, y, items, font_size=13, line_height=22, color=DARK_TEXT, bullet_color=GOLD):
    """Draw a bullet list. Returns the y position after the last item."""
    for item in items:
        # Gold bullet
        c.setFillColor(bullet_color)
        c.setFont(FONT_BOLD, font_size)
        c.drawString(x, y, "▸")
        # Text
        c.setFillColor(color)
        c.setFont(FONT, font_size)
        # Handle long text wrapping simply
        text = item
        max_chars = int((PAGE_W - x - MARGIN - 20) / (font_size * 0.52))
        if len(text) > max_chars:
            # Split at word boundary
            words = text.split()
            line1 = ""
            line2 = ""
            for word in words:
                if len(line1 + word) < max_chars:
                    line1 += word + " "
                else:
                    line2 += word + " "
            c.drawString(x + 16, y, line1.strip())
            if line2.strip():
                y -= line_height
                c.drawString(x + 16, y, line2.strip())
        else:
            c.drawString(x + 16, y, text)
        y -= line_height
    return y


def draw_table(c, x, y, headers, rows, col_widths, font_size=11, row_height=22):
    """Draw a simple styled table."""
    total_w = sum(col_widths)

    # Header row
    c.setFillColor(NAVY)
    c.rect(x, y - row_height + 4, total_w, row_height, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(FONT_BOLD, font_size)
    cx = x
    for i, h in enumerate(headers):
        c.drawString(cx + 6, y - row_height + 10, h)
        cx += col_widths[i]
    y -= row_height

    # Data rows
    for ri, row in enumerate(rows):
        bg = OFF_WHITE if ri % 2 == 0 else white
        c.setFillColor(bg)
        c.rect(x, y - row_height + 4, total_w, row_height, fill=1, stroke=0)
        c.setFillColor(DARK_TEXT)
        c.setFont(FONT, font_size)
        cx = x
        for i, cell in enumerate(row):
            c.drawString(cx + 6, y - row_height + 10, str(cell))
            cx += col_widths[i]
        y -= row_height

    # Bottom border
    c.setStrokeColor(GOLD)
    c.setLineWidth(2)
    c.line(x, y + 4, x + total_w, y + 4)
    return y


def draw_key_value_box(c, x, y, key, value, box_w=200, box_h=60, accent=GOLD):
    """Draw a highlighted key-value metric box."""
    draw_box(c, x, y, box_w, box_h, fill_color=OFF_WHITE, border_color=LIGHT_GRAY)
    # Accent top line
    c.setFillColor(accent)
    c.rect(x, y + box_h - 4, box_w, 4, fill=1, stroke=0)
    # Value (big)
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 18)
    c.drawCentredString(x + box_w / 2, y + box_h - 28, value)
    # Key (small)
    c.setFillColor(GRAY_TEXT)
    c.setFont(FONT, 9)
    c.drawCentredString(x + box_w / 2, y + 8, key)


# =====================================================================
# SLIDE DEFINITIONS
# =====================================================================

def slide_01_title(c):
    """Title slide."""
    draw_background(c)

    # Full navy background
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Gold horizontal line
    c.setFillColor(GOLD)
    c.rect(PAGE_W * 0.15, PAGE_H * 0.62, PAGE_W * 0.7, 3, fill=1, stroke=0)
    c.rect(PAGE_W * 0.15, PAGE_H * 0.32, PAGE_W * 0.7, 2, fill=1, stroke=0)

    # University
    c.setFillColor(HexColor("#8899aa"))
    c.setFont(FONT, 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.68, "Технически университет — София")

    # Title
    c.setFillColor(white)
    c.setFont(FONT_BOLD, 28)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.52, "Дигитализация на процеса по жалби")

    c.setFont(FONT_BOLD, 24)
    c.setFillColor(WARM_GOLD)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.45, "в УниКредит Булбанк")

    # Subtitle
    c.setFillColor(HexColor("#b0c4de"))
    c.setFont(FONT, 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.36, "Вариант 3  —  Курсов проект")

    # Names
    c.setFillColor(white)
    c.setFont(FONT, 15)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.24, "Венцислав  •  Максим  •  Петър")

    # Year
    c.setFillColor(GOLD)
    c.setFont(FONT_BOLD, 14)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.16, "2026")

    draw_footer(c, 1)


def slide_02_current_state(c):
    """Текущо състояние."""
    draw_background(c)
    draw_header(c, "Текущо състояние — УниКредит Булбанк", speaker=1)
    draw_footer(c, 2)

    y_start = PAGE_H - HEADER_H - 30
    left = MARGIN + SIDEBAR_W + 20

    # Left column: channels
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left, y_start, "Налични канали:")

    items = [
        "Клон (на хартия, с лична идентификация)",
        "Онлайн формуляр / email",
        "Телефон / писмо",
    ]
    y = draw_bullet_list(c, left + 10, y_start - 25, items, font_size=12)

    # Warning box
    y -= 10
    draw_box(c, left, y - 65, 360, 65, fill_color=HexColor("#fef5e7"), border_color=WARM_GOLD)
    c.setFillColor(CORAL)
    c.setFont(FONT_BOLD, 12)
    c.drawString(left + 12, y - 20, "⚠  Критична бариера:")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 11)
    c.drawString(left + 12, y - 38, "Жалби с лични данни → изискват КЕП")
    c.drawString(left + 12, y - 54, "(квалифициран е-подпис) или посещение на клон")

    # Right column: test results
    right = PAGE_W / 2 + 30
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT_BOLD, 14)
    c.drawString(right, y_start, "Тестване (2026-04-09):")

    test_items = [
        "Формулярът НЕ дава референтен номер",
        "Няма потвърждение по email",
        "Няма проследяване на статуса",
    ]
    draw_bullet_list(c, right + 10, y_start - 25, test_items, font_size=12, bullet_color=CORAL)

    # Bottom insight box
    draw_box(c, right, y - 65, 360, 65, fill_color=LIGHT_BLUE)
    c.setFillColor(MEDIUM_BLUE)
    c.setFont(FONT_BOLD, 11)
    c.drawString(right + 12, y - 20, "Извод:")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 11)
    c.drawString(right + 12, y - 38, "Онлайн формулярът е де факто")
    c.drawString(right + 12, y - 54, "неизползваем за реални жалби")


def slide_03_competitors(c):
    """Локални конкуренти."""
    draw_background(c)
    draw_header(c, "Българска банкова сцена — сравнение", speaker=1)
    draw_footer(c, 3)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 30

    headers = ["Аспект", "УКБ", "UBB", "DSK Bank"]
    rows = [
        ["Уеб формуляр", "Да (с КЕП)", "Да", "Да"],
        ["КЕП задължителен", "⚠ ДА", "Не", "Не"],
        ["Реф. номер", "Не", "Не", "✓ Да"],
        ["Email потвърждение", "Не", "Не", "✓ 2 email-а"],
        ["Срок на отговор", "Не посочен", "45 дни", "✓ 3 р.д. / ~13ч"],
        ["Чатбот за жалби", "Не", "→ уеб форма", "→ уеб форма"],
        ["In-app жалба", "Не", "Не", "Не"],
    ]
    col_widths = [170, 120, 120, 150]
    draw_table(c, left, y_start, headers, rows, col_widths, font_size=11, row_height=24)

    # Key insight box
    y_bottom = y_start - (len(rows) + 1) * 24 - 20
    draw_box(c, left, y_bottom - 40, PAGE_W - 2 * MARGIN - SIDEBAR_W - 20, 40, fill_color=HexColor("#fef5e7"), border_color=WARM_GOLD)
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left + 16, y_bottom - 25, "Извод: Нито една българска банка не обработва жалби in-app или чрез чатбот")


def slide_04_international(c):
    """Международни лидери."""
    draw_background(c)
    draw_header(c, "Международни еталони", speaker=1)
    draw_footer(c, 4)

    y_start = PAGE_H - HEADER_H - 30
    left = MARGIN + SIDEBAR_W + 20
    card_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 60) / 3
    card_h = 180

    companies = [
        ("Revolut", "Великобритания / ЕС", MEDIUM_BLUE, [
            "Жалба директно от приложението",
            "AI чатбот разпознава намерението",
            "Пренасочва към жив агент",
        ]),
        ("Monzo", "Великобритания", TEAL, [
            "\"Жалбата е възможност\"",
            "Специалист по домейн",
            "Тенденционен анализ → подобрения",
        ]),
        ("DBS Bank", "Сингапур", GOLD, [
            "Gen AI чатбот (Joy) — 120K+ чата",
            "AI Ко-пилот → -23% CSAT",
            "Ескалация бот → специалист",
        ]),
    ]

    for i, (name, country, accent, features) in enumerate(companies):
        x = left + i * (card_w + 20)
        draw_box(c, x, y_start - card_h, card_w, card_h, fill_color=OFF_WHITE, border_color=LIGHT_GRAY)

        # Accent top
        c.setFillColor(accent)
        c.rect(x, y_start - 4, card_w, 4, fill=1, stroke=0)

        # Company name
        c.setFillColor(NAVY)
        c.setFont(FONT_BOLD, 16)
        c.drawString(x + 14, y_start - 28, name)

        # Country
        c.setFillColor(GRAY_TEXT)
        c.setFont(FONT, 10)
        c.drawString(x + 14, y_start - 44, country)

        # Features
        draw_bullet_list(c, x + 14, y_start - 68, features, font_size=11, line_height=24, bullet_color=accent)


def slide_05_tier_model(c):
    """Tier модел."""
    draw_background(c)
    draw_header(c, "Предложение: 4-степенен Tier модел", speaker=1)
    draw_footer(c, 5)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    headers = ["Tier", "Тип", "Кой решава"]
    rows = [
        ["A", "Информационно запитване", "Чатбот (без действие)"],
        ["B", "Безопасно клиентско действие", "Клиент чрез чатбот"],
        ["C", "AI-предложено, човек одобрява", "Специалист + AI Ко-пилот"],
        ["D", "Пълно ръчно разследване", "Специалист + compliance"],
    ]
    col_widths = [60, 250, 250]
    draw_table(c, left, y_start, headers, rows, col_widths, font_size=12, row_height=28)

    # Key rule box
    y = y_start - 5 * 28 - 25
    draw_box(c, left, y - 55, 560, 55, fill_color=HexColor("#fdedec"), border_color=CORAL)
    c.setFillColor(CORAL)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left + 16, y - 22, "Ключово правило (EBA/ESMA JC 2018 35):")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 12)
    c.drawString(left + 16, y - 42, "Нито едно монетарно действие без изрично одобрение от специалист")


def slide_06_methodology(c):
    """Hybrid методология."""
    draw_background(c)
    draw_header(c, "Задача 4: Проектен план — Hybrid (Water-Scrum-Fall)", speaker=1)
    draw_footer(c, 6)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    # Why Hybrid section
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left, y_start, "Защо Hybrid?")

    reasons = [
        "Регулаторно — sign-off gates за Compliance, Legal, Risk",
        "Гъвкавост — sprint retrospectives в Phase 3",
        "Ранна обратна връзка — sprint демо на всеки 2 седмици",
        "Индустриален стандарт — UniCredit Group ползва SAFe",
    ]
    y = y_start - 25
    for r in reasons:
        c.setFillColor(GREEN)
        c.setFont(FONT_BOLD, 12)
        c.drawString(left + 10, y, "✓")
        c.setFillColor(DARK_TEXT)
        c.setFont(FONT, 12)
        c.drawString(left + 26, y, r)
        y -= 22

    # Phase flow
    y -= 15
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left, y, "Структура на проекта:")
    y -= 30

    phases = [
        ("P0", "Initiation", "1м", MEDIUM_BLUE),
        ("P1", "Requirements", "2м", MEDIUM_BLUE),
        ("P2", "Design", "2м", MEDIUM_BLUE),
        ("P3", "Implementation", "4м", TEAL),
        ("P4", "Testing", "2м", TEAL),
        ("P5", "Deploy", "1м", MEDIUM_BLUE),
        ("P6", "Hypercare", "2м", MEDIUM_BLUE),
    ]

    box_w = 95
    box_h = 50
    gap = 8
    start_x = left + 5
    for i, (code, name, dur, color) in enumerate(phases):
        x = start_x + i * (box_w + gap)
        draw_box(c, x, y - box_h, box_w, box_h, fill_color=color)
        c.setFillColor(white)
        c.setFont(FONT_BOLD, 11)
        c.drawCentredString(x + box_w / 2, y - 20, f"{code}: {name}")
        c.setFont(FONT, 9)
        c.drawCentredString(x + box_w / 2, y - 36, dur)

        # Arrow
        if i < len(phases) - 1:
            c.setFillColor(GOLD)
            c.setFont(FONT_BOLD, 14)
            c.drawCentredString(x + box_w + gap / 2, y - 25, "→")

    # Gates note
    y -= box_h + 20
    c.setFillColor(GRAY_TEXT)
    c.setFont(FONT, 11)
    c.drawString(left, y, "4 формални Gate-а:  Requirements ✋  Design ✋  Go/No-Go ✋  Release ✋")


def slide_07_releases(c):
    """Two-release стратегия."""
    draw_background(c)
    draw_header(c, "Два последователни Release-а", speaker=1)
    draw_footer(c, 7)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25
    half_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 60) / 2

    # Release 1
    draw_box(c, left, y_start - 200, half_w, 200, fill_color=OFF_WHITE, border_color=MEDIUM_BLUE)
    c.setFillColor(MEDIUM_BLUE)
    c.rect(left, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left + 14, y_start - 28, "Release 1 — Compliance CMS")
    c.setFillColor(GOLD)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left + 14, y_start - 48, "14 месеца")

    r1_items = [
        "Tier C + D (формални жалби)",
        "Пълно регулаторно съответствие",
        "Без AI — ръчна категоризация",
        "8 спринта, 40 user stories, 197 SP",
        "~15.85 FTE",
    ]
    draw_bullet_list(c, left + 14, y_start - 70, r1_items, font_size=11, line_height=22)

    # Release 2
    rx = left + half_w + 30
    draw_box(c, rx, y_start - 200, half_w, 200, fill_color=OFF_WHITE, border_color=TEAL)
    c.setFillColor(TEAL)
    c.rect(rx, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 15)
    c.drawString(rx + 14, y_start - 28, "Release 2 — AI / UX подобрения")
    c.setFillColor(GOLD)
    c.setFont(FONT_BOLD, 13)
    c.drawString(rx + 14, y_start - 48, "8 месеца")

    r2_items = [
        "Tier A + B (deflection чрез чатбот)",
        "AI_CHATBOT, NLP_ENGINE, AI_COPILOT",
        "Analytics и тенденционен анализ",
        "~9.25 FTE",
    ]
    draw_bullet_list(c, rx + 14, y_start - 70, r2_items, font_size=11, line_height=22)

    # Bottom summary
    y_bottom = y_start - 230
    draw_key_value_box(c, left, y_bottom - 70, "Обща програма", "22 месеца", box_w=220, accent=GOLD)
    draw_key_value_box(c, left + 240, y_bottom - 70, "Период", "2026-05 → 2028-02", box_w=220, accent=MEDIUM_BLUE)
    draw_key_value_box(c, left + 480, y_bottom - 70, "Общо FTE", "~25.10", box_w=180, accent=TEAL)


def slide_08_transition_to_bpm(c):
    """Transition slide."""
    draw_background(c)
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Gold lines
    c.setFillColor(GOLD)
    c.rect(PAGE_W * 0.2, PAGE_H * 0.55, PAGE_W * 0.6, 2, fill=1, stroke=0)
    c.rect(PAGE_W * 0.2, PAGE_H * 0.35, PAGE_W * 0.6, 2, fill=1, stroke=0)

    c.setFillColor(TEAL)
    c.setFont(FONT_BOLD, 20)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.47, "Задача 2: Бизнес процес")

    c.setFillColor(white)
    c.setFont(FONT, 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.39, "Максим")

    draw_footer(c, 8)


def slide_09_bpm_scope(c):
    """BPM обхват и действащи лица."""
    draw_background(c)
    draw_header(c, "Бизнес процес — Обхват и действащи лица", speaker=2)
    draw_footer(c, 9)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    # Scope
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left, y_start, "Обхват:")

    scope_items = [
        "Целият процес: подаване → обработка → отговор → обратна връзка",
        "Изцяло дистанционно — без посещение на клон",
    ]
    y = draw_bullet_list(c, left + 10, y_start - 25, scope_items, font_size=12)

    # Actors table
    y -= 15
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left, y, "Действащи лица:")
    y -= 10

    headers = ["Роля", "Тип", "Описание"]
    rows = [
        ["Клиент", "Външен (pool)", "Автентикиран в Булбанк Мобайл"],
        ["AI Чатбот", "Вътрешна lane", "Прием, NLP анализ, Tier A/B/C/D"],
        ["CMS", "Вътрешна lane", "Регистрация, маршрутизиране, одит"],
        ["Специалист + Ко-пилот", "Вътрешна lane", "Разследване, одобрение"],
        ["Ръководител", "Вътрешна lane", "Вътрешен преглед при ескалация"],
    ]
    col_widths = [180, 140, 300]
    draw_table(c, left, y, headers, rows, col_widths, font_size=11, row_height=24)


def slide_10_bpmn(c):
    """BPMN процесна диаграма."""
    draw_background(c)
    draw_header(c, "BPMN 2.0 — Колаборационна диаграма", speaker=2)
    draw_footer(c, 10)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    # Image placeholder
    cx = PAGE_W / 2
    draw_box(c, left, y_start - 170, PAGE_W - 2 * MARGIN - SIDEBAR_W - 20, 170,
             fill_color=LIGHT_GRAY, border_color=HexColor("#cccccc"))
    c.setFillColor(GRAY_TEXT)
    c.setFont(FONT, 14)
    c.drawCentredString(cx, y_start - 80, "[BPMN диаграма — вмъкнете скрийншот от bpmn.io]")
    c.setFont(FONT, 10)
    c.drawCentredString(cx, y_start - 100, "complaint_process.bpmn")

    y = y_start - 195
    items = [
        "2 pool-а: Клиент + Банка (4 lane-а)",
        "20 задачи, 6 gateway-я, 37 sequence flow-а",
        "BPMN 2.0 XML — зареждаем в bpmn.io, Camunda Modeler",
        "SLA и регулаторни анотации директно в диаграмата",
        "AUDIT_LOG data store за одитна пътека",
    ]
    draw_bullet_list(c, left, y, items, font_size=12, line_height=22)


def slide_11_phases(c):
    """7 фази на процеса."""
    draw_background(c)
    draw_header(c, "7 фази на процеса", speaker=2)
    draw_footer(c, 11)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20

    phases = [
        ("Фаза 1", "Иницииране", "Клиент → Чатбот (категория, описание, прикачени)", MEDIUM_BLUE),
        ("Фаза 2", "NLP анализ", "Определяне на Tier (A/B/C/D)", MEDIUM_BLUE),
        ("Фаза 3а", "Бърз път (A/B)", "Чатботът решава без формална жалба", TEAL),
        ("Фаза 4", "Регистрация (C/D)", "Реф. номер, потвърждение in-app + email + push", GOLD),
        ("Фаза 5", "Разследване", "Специалист + AI Ко-пилот", GOLD),
        ("Фаза 6", "Изпълнение", "⚠ Монетарно действие → само с одобрение", CORAL),
        ("Фаза 6а", "Ескалация", "Ръководител → БНБ / КЗП / ПКПС", CORAL),
        ("Фаза 7", "Обратна връзка", "Проучване + тенденционен анализ", TEAL),
    ]

    card_h = 38
    gap = 5
    for i, (phase, name, desc, color) in enumerate(phases):
        y = y_start - i * (card_h + gap)
        # Phase badge
        c.setFillColor(color)
        c.roundRect(left, y - card_h + 8, 90, card_h - 4, 4, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont(FONT_BOLD, 10)
        c.drawCentredString(left + 45, y - 12, phase)

        # Name
        c.setFillColor(NAVY)
        c.setFont(FONT_BOLD, 12)
        c.drawString(left + 100, y - 12, name)

        # Desc
        c.setFillColor(DARK_TEXT)
        c.setFont(FONT, 11)
        c.drawString(left + 100, y - 28, desc)


def slide_12_rules(c):
    """Правила за движение."""
    draw_background(c)
    draw_header(c, "Правила за преминаване", speaker=2)
    draw_footer(c, 12)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25
    half_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 60) / 2

    # Forward rules
    draw_box(c, left, y_start - 220, half_w, 220, fill_color=HexColor("#eafaf1"), border_color=GREEN)
    c.setFillColor(GREEN)
    c.setFont(FONT_BOLD, 15)
    c.drawString(left + 14, y_start - 22, "НАПРЕД →")

    fwd = [
        "Логин → Чатбот (успешна автентикация)",
        "Чатбот → Tier A/B (NLP определение)",
        "Чатбот → Регистрация (Tier C/D)",
        "Разследване → Решение",
        "Решение → Изпълнение (одобрение)",
        "Отговор → Приключване",
    ]
    draw_bullet_list(c, left + 14, y_start - 50, fwd, font_size=11, line_height=24, bullet_color=GREEN)

    # Backward rules
    rx = left + half_w + 30
    draw_box(c, rx, y_start - 220, half_w, 220, fill_color=HexColor("#fef5e7"), border_color=CORAL)
    c.setFillColor(CORAL)
    c.setFont(FONT_BOLD, 15)
    c.drawString(rx + 14, y_start - 22, "НАЗАД ←")

    bwd = [
        "Разследване → Клиент (доп. инфо)",
        "Отговор → Разследване (уточнение)",
        "Tier A/B → Регистрация (настояване)",
        "Маршрутизиране → Друг специалист",
    ]
    draw_bullet_list(c, rx + 14, y_start - 50, bwd, font_size=11, line_height=24, bullet_color=CORAL)


def slide_13_seq1(c):
    """Sequence диаграма 1."""
    draw_background(c)
    draw_header(c, "Sequence диаграма: Подаване и регистрация", speaker=2)
    draw_footer(c, 13)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    # Image placeholder
    draw_box(c, left, y_start - 140, PAGE_W - 2 * MARGIN - SIDEBAR_W - 20, 140,
             fill_color=LIGHT_GRAY, border_color=HexColor("#cccccc"))
    c.setFillColor(GRAY_TEXT)
    c.setFont(FONT, 13)
    c.drawCentredString(PAGE_W / 2, y_start - 65, "[Sequence диаграма 1 — вмъкнете SVG/PNG от 02_bpm_process FINAL/]")

    y = y_start - 165

    # Participants flow
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 12)
    c.drawString(left, y, "Участници:  BBM_USER → BBM → BBO_BE → AI_CHATBOT → NLP_ENGINE → CMS → NOTIF")

    y -= 30
    steps = [
        "Автентикация (биометрия / ПИН)",
        "Чатбот събира категория + описание",
        "NLP анализ → Tier определяне",
        "Регистрация в CMS → референтен номер",
        "Многоканално потвърждение (in-app + email + push)",
    ]
    draw_bullet_list(c, left, y, steps, font_size=12, line_height=22)


def slide_14_seq23(c):
    """Sequence диаграми 2+3."""
    draw_background(c)
    draw_header(c, "Разследване → Решение → Изпълнение", speaker=2)
    draw_footer(c, 14)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25
    half_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 60) / 2

    # Diagram 2
    draw_box(c, left, y_start - 200, half_w, 200, fill_color=OFF_WHITE, border_color=TEAL)
    c.setFillColor(TEAL)
    c.rect(left, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left + 14, y_start - 26, "Диаграма 2 — AI Ко-пилот контекст:")
    items2 = [
        "CORE_BANKING → клиентски профил",
        "CORE_ACC → сметки и транзакции",
        "CARD_SYSTEM → детайли за карта",
        "CRM → история на взаимодействия",
        "CMS → подобни минали случаи",
    ]
    draw_bullet_list(c, left + 14, y_start - 55, items2, font_size=11, line_height=22, bullet_color=TEAL)

    # Diagram 3
    rx = left + half_w + 30
    draw_box(c, rx, y_start - 200, half_w, 200, fill_color=OFF_WHITE, border_color=GOLD)
    c.setFillColor(GOLD)
    c.rect(rx, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 13)
    c.drawString(rx + 14, y_start - 26, "Диаграма 3 — Решение и изпълнение:")
    items3 = [
        "Специалист одобрява → AUDIT_LOG",
        "CORE_BANKING → кредитира сметка",
        "Многоканален отговор → Клиент",
        "Реакция: Приема / Уточнение / Ескалация",
    ]
    draw_bullet_list(c, rx + 14, y_start - 55, items3, font_size=11, line_height=22, bullet_color=GOLD)


def slide_15_transition_to_arch(c):
    """Transition to architecture."""
    draw_background(c)
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    c.setFillColor(GOLD)
    c.rect(PAGE_W * 0.2, PAGE_H * 0.55, PAGE_W * 0.6, 2, fill=1, stroke=0)
    c.rect(PAGE_W * 0.2, PAGE_H * 0.35, PAGE_W * 0.6, 2, fill=1, stroke=0)

    c.setFillColor(CORAL)
    c.setFont(FONT_BOLD, 20)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.47, "Задача 3: Технологична архитектура")

    c.setFillColor(white)
    c.setFont(FONT, 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.39, "Петър")

    draw_footer(c, 15)


def slide_16_arch_overview(c):
    """Архитектура общ изглед."""
    draw_background(c)
    draw_header(c, "Технологична архитектура — Общ изглед", speaker=3)
    draw_footer(c, 16)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 25

    # Image placeholder
    draw_box(c, left, y_start - 180, PAGE_W - 2 * MARGIN - SIDEBAR_W - 20, 180,
             fill_color=LIGHT_GRAY, border_color=HexColor("#cccccc"))
    c.setFillColor(GRAY_TEXT)
    c.setFont(FONT, 13)
    c.drawCentredString(PAGE_W / 2, y_start - 80,
                        "[Архитектура — вмъкнете Final diagram.drawio.png]")
    c.setFont(FONT, 10)
    c.drawCentredString(PAGE_W / 2, y_start - 100,
                        "03_architecture FINAL/Final diagram.drawio.png")

    # Stats boxes
    y = y_start - 210
    stats = [
        ("Мрежови зони", "7"),
        ("Компоненти", "69"),
        ("Връзки", "37"),
        ("Firewall-и", "3 + WAF"),
    ]
    bw = 150
    gap = 25
    start_x = left + (PAGE_W - 2 * MARGIN - SIDEBAR_W - 20 - 4 * bw - 3 * gap) / 2
    for i, (label, value) in enumerate(stats):
        draw_key_value_box(c, start_x + i * (bw + gap), y - 65, label, value, box_w=bw, accent=CORAL)


def slide_17_dmz(c):
    """DMZ + Digital Channels."""
    draw_background(c)
    draw_header(c, "Зони 1–3: Клиент → DMZ → Digital Channels", speaker=3)
    draw_footer(c, 17)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20
    half_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 50) / 2

    # DMZ
    draw_box(c, left, y_start - 225, half_w, 225, fill_color=OFF_WHITE, border_color=CORAL)
    c.setFillColor(CORAL)
    c.rect(left, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 14)
    c.drawString(left + 14, y_start - 26, "DMZ (Demilitarized Zone)")

    dmz = [
        "WAF (ModSecurity, RHEL 9)",
        "Load Balancer (F5/HAProxy) TLS 1.3",
        "Reverse Proxy (NGINX 1.25, RHEL 9)",
        "API Gateway (Kong 3.x, Ubuntu 22.04)",
        "Identity Provider (Keycloak, Tomcat 10)",
    ]
    draw_bullet_list(c, left + 14, y_start - 52, dmz, font_size=11, line_height=28, bullet_color=CORAL)

    # Digital Channels
    rx = left + half_w + 25
    draw_box(c, rx, y_start - 225, half_w, 225, fill_color=OFF_WHITE, border_color=MEDIUM_BLUE)
    c.setFillColor(MEDIUM_BLUE)
    c.rect(rx, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 14)
    c.drawString(rx + 14, y_start - 26, "Digital Channels (съществуващи)")

    dc = [
        "BBO_BE — Spring Boot 3, Java 21, Tomcat 10",
        "BBM Backend — Spring Boot 3, RHEL 9",
        "Session / Auth Service + Redis",
    ]
    draw_bullet_list(c, rx + 14, y_start - 52, dc, font_size=11, line_height=28, bullet_color=MEDIUM_BLUE)

    # Client zone note
    y_bottom = y_start - 248
    draw_box(c, rx, y_bottom - 40, half_w, 40, fill_color=LIGHT_BLUE)
    c.setFillColor(MEDIUM_BLUE)
    c.setFont(FONT_BOLD, 11)
    c.drawString(rx + 12, y_bottom - 15, "Клиент:")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 11)
    c.drawString(rx + 72, y_bottom - 15, "iOS / Android / уеб браузър / email")


def slide_18_complaint_services(c):
    """Complaint Services Zone."""
    draw_background(c)
    draw_header(c, "Зона 4: Complaint Services (Kubernetes / OpenShift)", "НОВА", speaker=3)
    draw_footer(c, 18)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20

    # K8s note
    draw_box(c, left, y_start - 30, PAGE_W - 2 * MARGIN - SIDEBAR_W - 20, 30, fill_color=LIGHT_BLUE)
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 11)
    c.drawString(left + 12, y_start - 20, "K8s 1.29 (OpenShift 4.14)  +  Istio mTLS  +  RHEL UBI 9 / Alpine / Ubuntu")

    y = y_start - 42
    headers = ["Услуга", "Технология", "OS", "Порт"]
    rows = [
        ["AI_CHATBOT", "Python 3.12, FastAPI", "RHEL UBI 9", "8443/8444"],
        ["NLP_ENGINE", "PyTorch/ONNX, GPU", "RHEL UBI 9", "50051 gRPC"],
        ["CMS", "Spring Boot 3, Zeebe", "RHEL 9", "8443"],
        ["AI_COPILOT", "Python 3.12, FastAPI", "RHEL UBI 9", "8443"],
        ["NOTIF_SERVICE", "Node.js 20, Express", "Ubuntu 22.04", "8443"],
        ["AUDIT_LOG", "Go 1.22 (append-only)", "Alpine", "8443"],
        ["Specialist Workbench", "React 18, NGINX", "Alpine", "443"],
        ["Analytics", "Python, Airflow 2.x", "RHEL UBI 9", "Kafka"],
    ]
    col_widths = [170, 200, 120, 110]
    draw_table(c, left, y, headers, rows, col_widths, font_size=10, row_height=22)


def slide_19_core_db(c):
    """Core Banking + Database Zones."""
    draw_background(c)
    draw_header(c, "Зони 5–6: Core Banking (legacy) + Бази данни", speaker=3)
    draw_footer(c, 19)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20
    half_w = (PAGE_W - 2 * MARGIN - SIDEBAR_W - 50) / 2

    # Core Banking
    draw_box(c, left, y_start - 210, half_w, 210, fill_color=OFF_WHITE, border_color=GOLD)
    c.setFillColor(GOLD)
    c.rect(left, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left + 14, y_start - 24, "Core Banking (не се променят)")

    core = [
        "CORE_BANKING — JBoss EAP 7.4, RHEL 9",
        "CORE_ACC — вграден, JBoss, RHEL 9",
        "CARD_SYSTEM — .NET 8, IIS 10, Win 2022",
        "CRM — Dynamics 365, IIS, Win 2022",
        "Integration Bus — IBM MQ 9.3, RHEL 9",
    ]
    draw_bullet_list(c, left + 14, y_start - 50, core, font_size=11, line_height=26, bullet_color=GOLD)

    # Database
    rx = left + half_w + 25
    draw_box(c, rx, y_start - 210, half_w, 210, fill_color=OFF_WHITE, border_color=MEDIUM_BLUE)
    c.setFillColor(MEDIUM_BLUE)
    c.rect(rx, y_start - 4, half_w, 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 13)
    c.drawString(rx + 14, y_start - 24, "Database Zone (изолирана)")

    db = [
        "Oracle 19c — Core Banking (1521)",
        "PostgreSQL 15 — CMS (5432)",
        "PostgreSQL 15 — AUDIT_LOG, WORM (5432)",
        "Redis 7.2 — сесии, Sentinel HA (6379)",
        "MinIO — прикачени, AES-256 (9000)",
        "Elasticsearch 8 — analytics (9200)",
        "SQL Server 2022 — CRM+Cards (1433)",
    ]
    draw_bullet_list(c, rx + 14, y_start - 50, db, font_size=11, line_height=22, bullet_color=MEDIUM_BLUE)


def slide_20_communications(c):
    """Комуникации и протоколи."""
    draw_background(c)
    draw_header(c, "Комуникационни връзки (37 стрелки)", speaker=3)
    draw_footer(c, 20)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20

    # Incoming traffic
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left, y_start, "Входящ трафик:")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 12)
    c.drawString(left + 10, y_start - 22, "Client → HTTPS 443, TLS 1.3 → WAF → LB → RP → API GW → BBO_BE / BBM (REST 8443 mTLS + JWT)")

    # Internal APIs
    y = y_start - 55
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left, y, "Вътрешни API-та (Complaint Zone):")
    internal = [
        "AI_CHATBOT ↔ NLP_ENGINE: gRPC 50051",
        "BBO_BE ↔ AI_CHATBOT: WebSocket 8444 (real-time чат)",
        "CMS → NOTIF_SERVICE: Kafka 9093 (async)",
        "CMS → AUDIT_LOG: REST 8443 (sync за критични events)",
    ]
    y = draw_bullet_list(c, left + 10, y - 22, internal, font_size=11, line_height=22)

    # AI Co-pilot
    y -= 10
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left, y, "AI Co-pilot context assembly:")
    copilot = [
        "CORE_BANKING (SOAP/REST 8443), CORE_ACC (SOAP 8443)",
        "CARD_SYSTEM (REST 443), CRM (OData 443), CMS (REST 8443)",
    ]
    y = draw_bullet_list(c, left + 10, y - 22, copilot, font_size=11, line_height=22)

    # Notifications
    y -= 10
    c.setFillColor(NAVY)
    c.setFont(FONT_BOLD, 13)
    c.drawString(left, y, "Нотификации:")
    c.setFillColor(DARK_TEXT)
    c.setFont(FONT, 12)
    c.drawString(left + 10, y - 22, "NOTIF → in-app (8443)  +  SMTP (587)  +  FCM (443)  +  APNS (443)")


def slide_21_security(c):
    """Сигурност и съответствие."""
    draw_background(c)
    draw_header(c, "Сигурност и регулаторно съответствие", speaker=3)
    draw_footer(c, 21)

    left = MARGIN + SIDEBAR_W + 20
    y_start = PAGE_H - HEADER_H - 20

    headers = ["Изискване", "Реализация"]
    rows = [
        ["EBA/ESMA JC 2018", "AUDIT_LOG + WORM PostgreSQL, hash chain, 7 г."],
        ["DORA", "K8s HA, DB репликация, 3-node Kafka/ES"],
        ["GDPR", "In-app автентикация (без КЕП), AES-256, TLS"],
        ["PSD2 SCA", "OAuth2 + JWT + MFA в API Gateway"],
        ["Мрежова сегментация", "3 firewall-а, VLAN per zone"],
        ["Zero-trust", "Istio service mesh mTLS между всички pods"],
        ["Secrets mgmt", "HashiCorp Vault"],
        ["Одит на администратори", "Bastion host + SIEM (ELK)"],
    ]
    col_widths = [200, 500]
    draw_table(c, left, y_start, headers, rows, col_widths, font_size=12, row_height=26)


def slide_22_questions(c):
    """Final slide — Questions."""
    draw_background(c)
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Gold decorative lines
    c.setFillColor(GOLD)
    c.rect(PAGE_W * 0.15, PAGE_H * 0.68, PAGE_W * 0.7, 3, fill=1, stroke=0)
    c.rect(PAGE_W * 0.15, PAGE_H * 0.28, PAGE_W * 0.7, 2, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont(FONT_BOLD, 30)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.55, "Благодарим за вниманието!")

    c.setFillColor(WARM_GOLD)
    c.setFont(FONT_BOLD, 24)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.44, "Въпроси?")

    c.setFillColor(HexColor("#b0c4de"))
    c.setFont(FONT, 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H * 0.33, "Венцислав  •  Максим  •  Петър")

    draw_footer(c, 22)


# =====================================================================
# MAIN
# =====================================================================

def main():
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "presentation.pdf")

    c = canvas.Canvas(output_path, pagesize=landscape(A4))
    c.setTitle("Дигитализация на процеса по жалби — УниКредит Булбанк")
    c.setAuthor("Венцислав, Максим, Петър — ТУ София 2026")
    c.setSubject("Курсов проект — Дигитализация в банкирането, Вариант 3")

    slides = [
        slide_01_title,
        slide_02_current_state,
        slide_03_competitors,
        slide_04_international,
        slide_05_tier_model,
        slide_06_methodology,
        slide_07_releases,
        slide_08_transition_to_bpm,
        slide_09_bpm_scope,
        slide_10_bpmn,
        slide_11_phases,
        slide_12_rules,
        slide_13_seq1,
        slide_14_seq23,
        slide_15_transition_to_arch,
        slide_16_arch_overview,
        slide_17_dmz,
        slide_18_complaint_services,
        slide_19_core_db,
        slide_20_communications,
        slide_21_security,
        slide_22_questions,
    ]

    for i, slide_fn in enumerate(slides):
        slide_fn(c)
        if i < len(slides) - 1:
            c.showPage()

    c.save()
    print(f"✅ Presentation saved to: {output_path}")
    print(f"   {len(slides)} slides generated")


if __name__ == "__main__":
    main()
