#!/usr/bin/env python3
"""
Reusable FCHIP UI components + layouts under app-ui/00-shared.
Derived from app-flows + SoT patterns used across app-ui screens.
Brand marks load from frontend/assets/logos via app-ui/branding.py.
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
COMPONENTS = ROOT / "components"
LAYOUTS = ROOT / "layouts"

sys.path.insert(0, str(ROOT.parent))
from branding import LOGO_MARK, LOGO_SPLASH, paste_logo, paste_logo_centered
from ui_primitives import C, DARK_C, SIZES, font, rr, tx

# Compact specimen canvas for isolated components
SPECIMEN = {
    "mobile": (390, 520),
    "tablet": (768, 560),
    "desktop": (1100, 520),
}

def save_meta(path: Path, meta: dict):
    path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def specimen_frame(bp: str, title: str, subtitle: str) -> tuple[Image.Image, ImageDraw.ImageDraw, int, int, int]:
    w, h = SPECIMEN[bp]
    img = Image.new("RGB", (w, h), C["canvas"])
    draw = ImageDraw.Draw(img)
    pad = 20 if bp == "mobile" else 28
    tx(draw, (pad, 18), title, size=16, bold=True, fill=C["primary"])
    tx(draw, (pad, 42), subtitle, size=11, fill=C["muted"])
    # stage card
    stage_top = 68
    rr(draw, (pad, stage_top, w - pad, h - 24), C["bg"], radius=16, outline=C["line"])
    return img, draw, pad + 16, stage_top + 16, w - pad - 16


# --- primitive drawers used by components & layouts ---


def draw_app_bar(img, draw, x0, y0, x1, y1, title="FCHIP", right="Your health, our mission.", *, brand=False):
    draw.rectangle([x0, y0, x1, y1], fill=C["primary"])
    mid_y = (y0 + y1) / 2
    if brand or title == "FCHIP":
        mark_h = max(24, int(y1 - y0) - 16)
        lw, _ = paste_logo(img, (x0 + 16, mid_y), max_w=mark_h, max_h=mark_h, tint=None, anchor="lm")
        if title and title != "FCHIP":
            tx(draw, (x0 + 24 + lw, mid_y), title, size=14, bold=True, fill=C["on_primary"], anchor="lm")
    else:
        tx(draw, (x0 + 16, mid_y), title, size=14, bold=True, fill=C["on_primary"], anchor="lm")
    tx(draw, (x1 - 16, mid_y), right, size=10, fill=(210, 235, 236), anchor="rm")


def draw_bottom_nav(draw, x0, y0, x1, y1, items: list[str], active=0):
    draw.rectangle([x0, y0, x1, y1], fill=C["surface"])
    draw.line([(x0, y0), (x1, y0)], fill=C["line"])
    slot = (x1 - x0) / max(len(items), 1)
    for i, item in enumerate(items):
        cx = x0 + slot * i + slot / 2
        color = C["primary"] if i == active else C["muted"]
        rr(
            draw,
            (cx - 13, y0 + 6, cx + 13, y0 + 32),
            C["primary_soft"] if i == active else C["surface"],
            radius=8,
            outline=color,
        )
        tx(draw, (cx, y0 + 19), item[:1], size=11, bold=True, fill=color, anchor="mm")
        tx(draw, (cx, y0 + 44), item, size=11, fill=color, anchor="mm")


def draw_side_nav(img, draw, x0, y0, x1, y1, items: list[str], active=0):
    draw.rectangle([x0, y0, x1, y1], fill=C["chrome"])
    compact = (x1 - x0) < 120
    if compact:
        paste_logo_centered(img, (x0 + x1) / 2, y0 + 36, max_w=36, max_h=36, tint=None)
    else:
        paste_logo(img, (x0 + 20, y0 + 18), max_w=40, max_h=40, tint=None, anchor="lt")
        tx(draw, (x0 + 68, y0 + 28), "FCHIP", size=14, bold=True, fill=C["white"], anchor="lm")
        tx(draw, (x0 + 20, y0 + 68), "Community Health\nIntelligence Platform", size=10, fill=(160, 190, 194))
    y = y0 + (90 if compact else 110)
    for i, item in enumerate(items):
        fill = C["accent"] if i == active else (32, 54, 60)
        rr(draw, (x0 + 12, y, x1 - 12, y + 38), fill, radius=10)
        tx(draw, (x0 + 24, y + 19), item, size=12, fill=C["white"], anchor="lm")
        y += 46
    if not compact:
        tx(draw, (x0 + 20, y1 - 28), "Cascade Data & Feedback", size=11, fill=(120, 150, 155))


def draw_chip(draw, x, y, label, soft=True):
    tw = draw.textlength(label, font=font(11)) + 20
    fill = C["primary_soft"] if soft else C["ok_soft"]
    color = C["primary"] if soft else C["ok"]
    rr(draw, (x, y, x + tw, y + 24), fill, radius=12)
    tx(draw, (x + 10, y + 12), label, size=11, fill=color, anchor="lm")
    return tw + 8


def draw_stat(draw, x, y, w, h, label, value):
    rr(draw, (x, y, x + w, y + h), C["surface"], radius=14, outline=C["line"])
    tx(draw, (x + 14, y + 16), label, size=11, fill=C["muted"])
    tx(draw, (x + 14, y + 40), value, size=18, bold=True, fill=C["primary"])


def draw_list_row(draw, x, y, w, title, sub):
    rr(draw, (x, y, x + w, y + 56), C["surface"], radius=14, outline=C["line"])
    tx(draw, (x + 16, y + 18), title, size=13, bold=True)
    tx(draw, (x + 16, y + 38), sub, size=11, fill=C["muted"])
    tx(draw, (x + w - 16, y + 28), "›", size=18, fill=C["muted"], anchor="rm")


def draw_field(draw, x, y, w, label, value):
    tx(draw, (x + 2, y), label, size=11, fill=C["muted"])
    rr(draw, (x, y + 16, x + w, y + 54), C["surface"], radius=12, outline=C["line"])
    tx(draw, (x + 14, y + 35), value, size=13, anchor="lm")


def draw_cta(draw, x, y, w, label, fill=None):
    rr(draw, (x, y, x + w, y + 48), fill or C["primary"], radius=14)
    tx(draw, (x + w / 2, y + 24), label, size=14, bold=True, fill=C["on_primary"], anchor="mm")


def draw_map_block(draw, x, y, w, h, note: str):
    rr(draw, (x, y, x + w, y + h), C["map"], radius=16)
    spots = [(0.28, 0.35, 22), (0.55, 0.42, 30), (0.42, 0.62, 18)]
    for fx, fy, r in spots:
        cx, cy = x + w * fx, y + h * fy
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=C["warn"])
        draw.ellipse([cx - r * 0.4, cy - r * 0.4, cx + r * 0.4, cy + r * 0.4], fill=C["white"])
    rr(draw, (x + 10, y + h - 44, x + w - 10, y + h - 10), C["surface"], radius=10)
    tx(draw, (x + 20, y + h - 27), note, size=11, anchor="lm")


# ========== COMPONENTS ==========


@dataclass
class Component:
    category: str
    slug: str
    title: str
    purpose: str
    used_by: list[str] = field(default_factory=list)
    variants: list[str] = field(default_factory=lambda: ["default"])


COMPONENTS_CATALOG: list[Component] = [
    # 01-brand
    Component(
        "01-brand",
        "01-logo-lockup",
        "Logo lockup",
        "FCHIP mark from frontend/assets/logos for headers and auth",
        ["all shells", "splash", "login"],
    ),
    Component("01-brand", "02-slogan-line", "Slogan line", "Your health, our mission.", ["top app bar", "auth", "cover"]),
    Component("01-brand", "03-master-loop-badge", "Master loop badge", "CAPTURE → FUSE → PREDICT → ALERT → ACT → LEARN", ["splash", "onboarding"]),
    Component("01-brand", "04-cascade-footer", "Cascade footer", "Cascade Data & Feedback cue", ["desktop side nav"]),
    # 02-buttons
    Component("02-buttons", "01-primary-cta", "Primary CTA", "Main action on a screen", ["forms", "lists", "dashboards"]),
    Component("02-buttons", "02-secondary-cta", "Secondary CTA", "Alternate / cancel action", ["forms", "dialogs"]),
    Component("02-buttons", "03-danger-cta", "Danger CTA", "Destructive or high-urgency action", ["alerts", "revoke access"]),
    Component("02-buttons", "04-text-link", "Text link", "Inline navigation without button chrome", ["lists", "auth"]),
    # 03-chips
    Component("03-chips", "01-status-chip", "Status chip", "Compact status or count", ["worklists", "queues"]),
    Component("03-chips", "02-filter-chip-row", "Filter chip row", "Horizontal chip group", ["maps", "lists"]),
    Component("03-chips", "03-offline-ready-chip", "Offline-ready chip", "Field offline readiness", ["CHW", "feeders"]),
    Component("03-chips", "04-risk-chip", "Risk chip", "High / elevated risk flag", ["alerts", "facility"]),
    # 04-cards
    Component("04-cards", "01-stat-card", "Stat card", "Single metric tile", ["dashboards"]),
    Component("04-cards", "02-stat-card-row", "Stat card row", "2–4 metrics in a row", ["dashboards", "feeder homes"]),
    Component("04-cards", "03-list-row-card", "List row card", "Tappable title + subtitle row", ["worklists", "inboxes"]),
    Component("04-cards", "04-note-banner", "Note banner", "Calm info / positioning note", ["optional CHIS", "EMR note"]),
    Component("04-cards", "05-warn-banner", "Warn banner", "Attention callout", ["gaps", "consent"]),
    Component("04-cards", "06-explainability-block", "Explainability block", "Why an alert fired", ["alert follow-up", "district warnings"]),
    # 05-forms
    Component("05-forms", "01-labeled-field", "Labeled field", "Label + value input shell", ["all forms"]),
    Component("05-forms", "02-form-stack", "Form stack", "Vertical stack of labeled fields", ["visit", "referral", "feeder entry"]),
    Component("05-forms", "03-consent-toggle", "Consent toggle", "Consent / privacy affirmation", ["capture", "self-report", "EMR share"]),
    Component("05-forms", "04-file-upload-field", "File upload field", "Batch / dataset upload cue", ["NGO", "lab batch", "HMIS"]),
    Component("05-forms", "05-select-field", "Select field", "Single-choice shell", ["urgency", "facility picker"]),
    # 06-navigation
    Component("06-navigation", "01-top-app-bar", "Top app bar", "Brand + slogan / screen title", ["all surfaces"]),
    Component("06-navigation", "02-bottom-nav-field", "Bottom nav · field", "CHW tabs", ["01"]),
    Component("06-navigation", "03-bottom-nav-caregiver", "Bottom nav · caregiver", "Home · Report · Guidance · More", ["02"]),
    Component("06-navigation", "04-bottom-nav-feeder", "Bottom nav · feeder", "School / pharmacy / lab / MCH tabs", ["14–19", "21"]),
    Component("06-navigation", "05-bottom-nav-intel", "Bottom nav · intelligence", "Ingest · AI · GIS · Guidance", ["09"]),
    Component("06-navigation", "06-bottom-nav-insurance", "Bottom nav · insurance", "Prevent · Cohorts · Trends", ["23"]),
    Component("06-navigation", "07-side-nav-desktop", "Side nav · desktop", "Desktop chrome navigation", ["facility", "district", "admin", "feeders"]),
    Component("06-navigation", "08-role-picker-row", "Role picker row", "Workspace choice row", ["role-surface-picker"]),
    Component("06-navigation", "09-section-header", "Section header", "Title + subtitle block", ["mobile/tablet screens"]),
    # 07-feedback
    Component("07-feedback", "01-empty-state", "Empty state", "No items yet", ["queues", "inboxes"]),
    Component("07-feedback", "02-sync-status-strip", "Sync status strip", "Queue · last sync · errors", ["sync screens", "feeder sync"]),
    Component("07-feedback", "03-success-toast", "Success toast", "Saved / synced confirmation", ["forms"]),
    Component("07-feedback", "04-error-inline", "Error inline", "Validation / feed error", ["forms", "connectors"]),
    Component("07-feedback", "05-loading-skeleton", "Loading skeleton", "Placeholder while data loads", ["dashboards"]),
    # data display
    Component("08-data-display", "01-hotspot-map", "Hotspot map", "GIS + climate overlay block", ["facility", "district", "coverage"]),
    Component("08-data-display", "02-queue-item", "Queue item", "Desk / referral / lab queue row", ["07", "16"]),
    Component("08-data-display", "03-feeder-health-pill", "Feeder health pill", "Healthy / degraded / silent", ["09 feeder board", "admin"]),
    Component("08-data-display", "04-metrics-spark-row", "Metrics spark row", "Compact trend labels", ["facility", "NGO"]),
    Component("08-data-display", "05-timeline-step", "Timeline step", "Signal → prediction → action", ["use-case detail"]),
]


def render_component(comp: Component, bp: str) -> Image.Image:
    img, draw, x, y, x1 = specimen_frame(bp, comp.title, comp.purpose)
    w = x1 - x
    slug = comp.slug

    if slug == "01-logo-lockup":
        paste_logo(img, (x, y + 8), name=LOGO_MARK, max_w=72, max_h=72, tint=C["primary"], anchor="lt")
        tx(draw, (x + 88, y + 28), "FCHIP", size=28, bold=True, fill=C["primary"], anchor="lm")
        tx(draw, (x + 88, y + 58), "Community Health Intelligence Platform", size=12, fill=C["muted"], anchor="lm")
    elif slug == "02-slogan-line":
        tx(draw, (x, y + 24), "Your health, our mission.", size=20, bold=True, fill=C["primary"])
        tx(draw, (x, y + 56), "Obulamu eri Bonna · Afya kwa Wote · Oburamu bwa Boona", size=11, fill=C["muted"])
    elif slug == "03-master-loop-badge":
        rr(draw, (x, y, x1, y + 90), C["primary_soft"], radius=16)
        tx(
            draw,
            ((x + x1) / 2, y + 45),
            "CAPTURE → FUSE → PREDICT\nALERT → ACT → LEARN",
            size=13,
            fill=C["primary"],
            anchor="mm",
        )
    elif slug == "04-cascade-footer":
        rr(draw, (x, y, x1, y + 48), C["chrome"], radius=10)
        tx(draw, (x + 16, y + 24), "Cascade Data & Feedback", size=12, fill=(180, 205, 208), anchor="lm")
    elif slug == "01-primary-cta":
        draw_cta(draw, x, y + 10, w, "Primary action")
    elif slug == "02-secondary-cta":
        rr(draw, (x, y + 10, x1, y + 58), C["surface"], radius=14, outline=C["primary"], width=2)
        tx(draw, ((x + x1) / 2, y + 34), "Secondary action", size=14, bold=True, fill=C["primary"], anchor="mm")
    elif slug == "03-danger-cta":
        draw_cta(draw, x, y + 10, w, "Urgent / revoke", fill=C["warn"])
    elif slug == "04-text-link":
        tx(draw, (x, y + 24), "View all alerts ›", size=14, bold=True, fill=C["accent"])
    elif slug == "01-status-chip":
        cx = x
        for label in ("12 visits", "3 alerts", "Offline ready"):
            cx += draw_chip(draw, cx, y + 16, label)
    elif slug == "02-filter-chip-row":
        cx = x
        for label in ("District", "Climate", "GIS", "Cases"):
            cx += draw_chip(draw, cx, y + 16, label)
    elif slug == "03-offline-ready-chip":
        draw_chip(draw, x, y + 16, "Offline ready")
        tx(draw, (x, y + 56), "Use on CHW and feeder capture shells", size=11, fill=C["muted"])
    elif slug == "04-risk-chip":
        rr(draw, (x, y + 16, x + 90, y + 40), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 28), "High risk", size=11, fill=C["warn"], anchor="lm")
    elif slug == "01-stat-card":
        draw_stat(draw, x, y, min(180, w), 72, "Open alerts", "5")
    elif slug == "02-stat-card-row":
        cols = 2 if bp == "mobile" else 4
        gap = 10
        cw = (w - gap * (cols - 1)) / cols
        labels = [("CHWs", "48"), ("Referrals", "71%"), ("Outreach", "12"), ("Flags", "4")]
        for i, (lab, val) in enumerate(labels[:cols]):
            draw_stat(draw, x + i * (cw + gap), y, cw, 72, lab, val)
    elif slug == "03-list-row-card":
        draw_list_row(draw, x, y, w, "Household visit · Nakato", "Kyebando · due 09:30")
    elif slug == "04-note-banner":
        rr(draw, (x, y, x1, y + 52), C["primary_soft"], radius=12)
        tx(draw, (x + 14, y + 26), "Not core product identity — programme intelligence only", size=11, fill=C["primary"], anchor="lm")
    elif slug == "05-warn-banner":
        rr(draw, (x, y, x1, y + 52), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 26), "High outreach / low completed referrals — rebalance", size=11, fill=C["warn"], anchor="lm")
    elif slug == "06-explainability-block":
        rr(draw, (x, y, x1, y + 110), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 14, y + 18), "Why flagged", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 42), "Fever reports + heavy rain + GIS cluster", size=13, bold=True)
        tx(draw, (x + 14, y + 70), "Suggested action", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 92), "Home visit · RDT · refer if needed", size=12)
    elif slug == "01-labeled-field":
        tx(draw, (x + 4, y), "Household ID · focused", size=11, fill=C["primary"])
        rr(draw, (x, y + 18, x + w, y + 60), C["surface"], radius=12, outline=C["primary"], width=3)
        tx(draw, (x + 14, y + 39), "HH-4821", size=13, anchor="lm")
    elif slug == "02-form-stack":
        yy = y
        for lab, val in [("Village", "Kyebando"), ("Members", "4"), ("Needs", "Fever · missed ANC")]:
            draw_field(draw, x, yy, w, lab, val)
            yy += 72
    elif slug == "03-consent-toggle":
        rr(draw, (x, y, x1, y + 56), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 16, y + 28), "Consent recorded", size=13, bold=True, anchor="lm")
        rr(draw, (x1 - 64, y + 14, x1 - 16, y + 42), C["ok"], radius=14)
        tx(draw, (x1 - 40, y + 28), "ON", size=11, bold=True, fill=C["on_primary"], anchor="mm")
    elif slug == "04-file-upload-field":
        rr(draw, (x, y, x1, y + 88), C["surface"], radius=14, outline=C["line"])
        tx(draw, ((x + x1) / 2, y + 34), "Drop CSV / choose file", size=13, bold=True, fill=C["primary"], anchor="mm")
        tx(draw, ((x + x1) / 2, y + 58), "visits_2026-07-26.csv · 48 records", size=11, fill=C["muted"], anchor="mm")
    elif slug == "05-select-field":
        draw_field(draw, x, y, w, "Urgency", "Within 48 hours ▾")
    elif slug == "01-top-app-bar":
        draw_app_bar(img, draw, x, y, x1, y + 52, brand=True)
    elif slug == "02-bottom-nav-field":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Worklist", "Alerts", "Sync", "More"])
    elif slug == "03-bottom-nav-caregiver":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Home", "Report", "Guidance", "More"])
    elif slug == "04-bottom-nav-feeder":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Home", "Session", "Screen", "Sync"])
    elif slug == "05-bottom-nav-intel":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Ingest", "AI", "GIS", "Guidance"])
    elif slug == "06-bottom-nav-insurance":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Prevent", "Cohorts", "Trends", "More"])
    elif slug == "07-side-nav-desktop":
        side_w = min(220, w)
        draw_side_nav(img, draw, x, y, x + side_w, y + 280, ["Overview", "Map", "Referrals", "Stock"])
    elif slug == "08-role-picker-row":
        draw_list_row(draw, x, y, w, "CHW / VHT mobile", "Worklists · visits · alerts")
        draw_list_row(draw, x, y + 66, w, "School health feed", "Sessions · screening · absenteeism")
    elif slug == "09-section-header":
        tx(draw, (x, y + 8), "Today’s worklist", size=22, bold=True)
        tx(draw, (x, y + 40), "Visits · follow-ups · alert tasks", size=12, fill=C["muted"])
    elif slug == "01-empty-state":
        rr(draw, (x, y, x1, y + 120), C["surface"], radius=14, outline=C["line"])
        tx(draw, ((x + x1) / 2, y + 44), "No open items", size=16, bold=True, fill=C["muted"], anchor="mm")
        tx(draw, ((x + x1) / 2, y + 72), "New referrals and alerts will show here", size=12, fill=C["muted"], anchor="mm")
    elif slug == "02-sync-status-strip":
        for i, (lab, val) in enumerate([("Queued", "7"), ("Failed", "0"), ("Last sync", "14:22")]):
            draw_stat(draw, x + i * ((w - 20) / 3 + 10), y, (w - 20) / 3, 70, lab, val)
    elif slug == "03-success-toast":
        rr(draw, (x, y, x1, y + 48), C["ok_soft"], radius=12)
        tx(draw, (x + 16, y + 24), "Saved locally · will sync when online", size=12, fill=C["ok"], anchor="lm")
    elif slug == "04-error-inline":
        rr(draw, (x, y, x1, y + 48), C["warn_soft"], radius=12)
        tx(draw, (x + 16, y + 24), "Validation failed · 2 rows need review", size=12, fill=C["warn"], anchor="lm")
    elif slug == "05-loading-skeleton":
        for i in range(3):
            rr(draw, (x, y + i * 40, x1, y + 28 + i * 40), C["line"], radius=8)
    elif slug == "01-hotspot-map":
        draw_map_block(draw, x, y, w, 160, "GIS · climate overlay")
    elif slug == "02-queue-item":
        draw_list_row(draw, x, y, w, "New · maternal", "Arrive by 16:00")
    elif slug == "03-feeder-health-pill":
        cx = x
        for label, soft in (("Healthy 12", False), ("Degraded 2", True), ("Silent 1", True)):
            tw = draw.textlength(label, font=font(11)) + 20
            fill = C["ok_soft"] if not soft or "Healthy" in label else C["warn_soft"]
            color = C["ok"] if "Healthy" in label else C["warn"]
            rr(draw, (cx, y + 16, cx + tw, y + 40), fill, radius=12)
            tx(draw, (cx + 10, y + 28), label, size=11, fill=color, anchor="lm")
            cx += tw + 8
    elif slug == "04-metrics-spark-row":
        tx(draw, (x, y + 12), "ACT  +28%   ·   ORS  +12%   ·   ANC kit  Stable", size=13, fill=C["primary"])
    elif slug == "05-timeline-step":
        steps = ["Signal", "Predict", "Action", "Learn"]
        for i, s in enumerate(steps):
            cx = x + i * (w / 4) + (w / 8)
            draw.ellipse([cx - 14, y + 20, cx + 14, y + 48], fill=C["primary"] if i < 2 else C["primary_soft"])
            tx(draw, (cx, y + 34), str(i + 1), size=11, bold=True, fill=C["on_primary"] if i < 2 else C["primary"], anchor="mm")
            tx(draw, (cx, y + 64), s, size=11, fill=C["ink"], anchor="mm")
            if i < 3:
                draw.line([(cx + 18, y + 34), (cx + w / 4 - 18, y + 34)], fill=C["line"], width=2)
    else:
        tx(draw, (x, y + 20), comp.title, size=14, bold=True)

    # footer tag
    tx(draw, (16, img.height - 10), f"components/{comp.category}/{comp.slug} · {bp}", size=11, fill=C["muted"], anchor="lb")
    return img


# ========== LAYOUTS ==========


@dataclass
class Layout:
    slug: str
    title: str
    purpose: str
    composes: list[str]
    surfaces: list[str]


LAYOUTS_CATALOG: list[Layout] = [
    Layout(
        "01-auth-centered-card",
        "Auth centered card",
        "Create account / sign in — phone number + password only",
        ["01-logo-lockup", "02-slogan-line", "01-labeled-field", "01-primary-cta", "03-master-loop-badge"],
        ["00-shared"],
    ),
    Layout(
        "04-field-mobile-shell",
        "Field mobile shell",
        "CHW / caregiver / feeder capture on phone",
        ["01-top-app-bar", "09-section-header", "02-bottom-nav-field", "01-status-chip", "01-primary-cta"],
        ["01", "02", "14–19", "21"],
    ),
    Layout(
        "05-field-tablet-shell",
        "Field tablet shell",
        "Adaptive field IA with a compact navigation rail and wider content column",
        ["01-top-app-bar", "07-side-nav-desktop", "09-section-header", "02-stat-card-row", "03-list-row-card"],
        ["01", "02", "feeders"],
    ),
    Layout(
        "06-desktop-sidebar-shell",
        "Desktop sidebar shell",
        "Facility · district · admin · feeder desktop chrome",
        ["07-side-nav-desktop", "01-top-app-bar", "04-cascade-footer"],
        ["06–13", "14–22 desktop"],
    ),
    Layout(
        "11-dashboard-metrics",
        "Dashboard metrics",
        "Overview with stats + list + CTA",
        ["02-stat-card-row", "03-list-row-card", "02-filter-chip-row", "01-primary-cta"],
        ["facility", "district", "NGO", "feeder homes"],
    ),
    Layout(
        "09-form-capture",
        "Form capture",
        "Structured offline / online data entry",
        ["09-section-header", "02-form-stack", "03-consent-toggle", "01-primary-cta", "03-success-toast"],
        ["visits", "referrals", "all feeder entry"],
    ),
    Layout(
        "02-list-worklist",
        "List / worklist",
        "Today’s tasks, alerts, notifications",
        ["09-section-header", "01-status-chip", "03-list-row-card", "01-primary-cta", "01-empty-state"],
        ["CHW worklist", "alerts inbox", "notifications"],
    ),
    Layout(
        "14-queue-desk",
        "Queue desk",
        "Referral / lab / result queues",
        ["02-filter-chip-row", "02-queue-item", "01-primary-cta", "02-sync-status-strip"],
        ["07", "16"],
    ),
    Layout(
        "13-map-explorer",
        "Map explorer",
        "GIS hotspot + climate legend",
        ["02-filter-chip-row", "01-hotspot-map", "09-section-header"],
        ["facility map", "district map", "coverage", "population"],
    ),
    Layout(
        "10-detail-action",
        "Detail + action",
        "Explainable alert / referral detail with CTA",
        ["02-stat-card-row", "06-explainability-block", "03-list-row-card", "01-primary-cta", "03-danger-cta"],
        ["alert follow-up", "referral detail", "deploy action"],
    ),
    Layout(
        "08-settings-admin",
        "Settings / admin",
        "Org · roles · consent · API scopes · feeder registry",
        ["09-section-header", "03-list-row-card", "04-note-banner", "01-primary-cta"],
        ["13", "08 scopes", "20 mapping", "22 config"],
    ),
    Layout(
        "15-feeder-home",
        "Feeder home",
        "Home for schools, pharmacy, lab, MCH, corporate, NCD, community, climate",
        ["02-stat-card-row", "03-list-row-card", "03-offline-ready-chip", "01-primary-cta", "04-bottom-nav-feeder"],
        ["14–22"],
    ),
    Layout(
        "03-dual-pane-desktop",
        "Dual-pane desktop",
        "Two-column lists / dashboards on wide screens",
        ["07-side-nav-desktop", "03-list-row-card", "02-stat-card-row"],
        ["facility overview", "cascade metrics", "NGO monitor"],
    ),
    Layout(
        "16-upload-batch",
        "Upload / batch",
        "File upload + validation + push to ingest",
        ["04-file-upload-field", "04-error-inline", "03-success-toast", "01-primary-cta", "04-note-banner"],
        ["NGO upload", "lab batch", "outreach batch", "HMIS exchange"],
    ),
    Layout(
        "12-connector-status",
        "Connector status",
        "External system health (EMR, HMIS, climate)",
        ["02-stat-card-row", "03-list-row-card", "03-feeder-health-pill", "05-warn-banner"],
        ["08", "20", "22", "09 feeder board"],
    ),
    Layout(
        "07-empty-state-shell",
        "Empty state shell",
        "Happy-path layout with empty body (worklist / queue)",
        ["09-section-header", "01-status-chip", "01-empty-state", "01-primary-cta"],
        ["01 worklist-empty", "07 referral-queue-empty"],
    ),
    Layout(
        "17-insurance-prevention",
        "Insurance prevention",
        "§7 prevention population insights — not claims / not CHIS identity",
        ["02-stat-card-row", "03-list-row-card", "04-note-banner", "01-primary-cta"],
        ["12-insurance-insights"],
    ),
]


def render_layout(layout: Layout, bp: str) -> Image.Image:
    w, h = SIZES[bp]
    img = Image.new("RGB", (w, h), C["bg"])
    draw = ImageDraw.Draw(img)
    slug = layout.slug

    left = 0
    top = 56
    bottom_nav_h = 0

    if bp in {"tablet", "desktop"} and slug not in {"01-auth-centered-card"}:
        left = 76 if bp == "tablet" else 220
        items = {
            "06-desktop-sidebar-shell": ["Overview", "Map", "Referrals", "Stock"],
            "11-dashboard-metrics": ["Overview", "Map", "Referrals", "Stock"],
            "03-dual-pane-desktop": ["Overview", "Map", "Metrics", "Plan"],
            "08-settings-admin": ["Org", "Users", "Consent", "APIs"],
            "12-connector-status": ["Status", "Scopes", "Log", "Onboard"],
            "15-feeder-home": ["Home", "Session", "Screen", "Sync"],
            "13-map-explorer": ["Map", "Warnings", "Metrics", "Plan"],
            "09-form-capture": ["Home", "Capture", "Queue", "Sync"],
            "02-list-worklist": ["Worklist", "Alerts", "Sync", "More"],
            "14-queue-desk": ["Queue", "Detail", "Outcomes", "Sync"],
            "10-detail-action": ["Inbox", "Detail", "Act", "More"],
            "16-upload-batch": ["Upload", "Validate", "Push", "Audit"],
            "04-field-mobile-shell": ["Worklist", "Alerts", "Sync", "More"],
            "05-field-tablet-shell": ["Worklist", "Alerts", "Sync", "More"],
        }.get(slug, ["Home", "Map", "Metrics", "More"])
        if bp == "tablet":
            draw.rectangle([0, 0, left, h], fill=C["chrome"])
            paste_logo_centered(img, left / 2, 36, max_w=36, max_h=36, tint=None)
            nav_y = 110
            for index, item in enumerate(items):
                rr(
                    draw,
                    (16, nav_y, left - 16, nav_y + 40),
                    C["accent"] if index == 0 else (32, 54, 60),
                    radius=10,
                )
                tx(draw, (left / 2, nav_y + 20), item[:1], size=13, bold=True, fill=C["white"], anchor="mm")
                nav_y += 48
        else:
            draw_side_nav(img, draw, 0, 0, left, h, items)
        draw_app_bar(img, draw, left, 0, w, top, title=layout.title)
    elif slug == "01-auth-centered-card":
        draw_app_bar(img, draw, 0, 0, w, top, brand=True)
    else:
        draw_app_bar(img, draw, 0, 0, w, top)
        if bp == "mobile":
            bottom_nav_h = 72
            nav_items = {
                "04-field-mobile-shell": ["Worklist", "Alerts", "Sync", "More"],
                "05-field-tablet-shell": ["Worklist", "Alerts", "Sync", "More"],
                "15-feeder-home": ["Home", "Session", "Screen", "Sync"],
                "02-list-worklist": ["Worklist", "Alerts", "Sync", "More"],
                "09-form-capture": ["Home", "Form", "Sync", "More"],
                "14-queue-desk": ["Queue", "Open", "Done", "More"],
                "13-map-explorer": ["Map", "Warnings", "Metrics", "Plan"],
                "11-dashboard-metrics": ["Overview", "Map", "Referrals", "Stock"],
                "10-detail-action": ["Inbox", "Act", "Sync", "More"],
                "16-upload-batch": ["Upload", "Queue", "Sync", "More"],
                "08-settings-admin": ["Org", "Users", "Consent", "More"],
                "12-connector-status": ["Status", "Log", "Scopes", "More"],
                "03-dual-pane-desktop": ["Overview", "Map", "Metrics", "More"],
            }.get(slug, ["Home", "List", "Sync", "More"])
            draw_bottom_nav(draw, 0, h - bottom_nav_h, w, h, nav_items)

    pad = 16 if bp == "mobile" else (24 if bp == "tablet" else 32)
    available_w = w - left - pad * 2
    content_cap = 720 if slug in {"09-form-capture", "08-settings-admin", "16-upload-batch"} else 1200
    max_w = min(available_w, content_cap)
    x = left + pad + max(0, (available_w - max_w) / 2)
    y = top + 18
    content_bottom = h - bottom_nav_h - 16

    if slug == "01-auth-centered-card":
        card_w = min(420, max_w)
        cx = left + (w - left - card_w) / 2
        cy = top + (60 if bp != "mobile" else 36)
        rr(draw, (cx, cy, cx + card_w, cy + 420), C["surface"], radius=20, outline=C["line"])
        paste_logo_centered(img, cx + card_w / 2, cy + 56, name=LOGO_SPLASH, max_w=72, max_h=72, tint=C["primary"])
        tx(draw, (cx + card_w / 2, cy + 108), "Your health, our mission.", size=13, fill=C["muted"], anchor="mm")
        rr(draw, (cx + 36, cy + 140, cx + card_w - 36, cy + 230), C["primary_soft"], radius=14)
        tx(
            draw,
            (cx + card_w / 2, cy + 185),
            "CAPTURE → FUSE → PREDICT\nALERT → ACT → LEARN",
            size=12,
            fill=C["primary"],
            anchor="mm",
        )
        draw_field(draw, cx + 28, cy + 250, card_w - 56, "Phone number", "+256 700 000 000")
        draw_field(draw, cx + 28, cy + 320, card_w - 56, "Password", "••••••••")
        draw_cta(draw, cx + 28, cy + 380, card_w - 56, "Sign in")
        return img

    if bp != "desktop":
        tx(draw, (x, y), layout.title, size=20, bold=True)
        y += 26
        tx(draw, (x, y), layout.purpose, size=12, fill=C["muted"])
        y += 28
    else:
        tx(draw, (x, y), layout.purpose, size=12, fill=C["muted"])
        y += 26

    if slug in {"11-dashboard-metrics", "15-feeder-home", "12-connector-status", "10-detail-action", "03-dual-pane-desktop", "05-field-tablet-shell"}:
        cols = 2 if bp == "mobile" else 4
        gap = 10
        cw = (max_w - gap * (cols - 1)) / cols
        stats = [("Open", "5"), ("Queued", "18"), ("Risk", "Elev."), ("Sync", "OK")]
        for i, (lab, val) in enumerate(stats[:cols]):
            draw_stat(draw, x + i * (cw + gap), y, cw, 70, lab, val)
        y += 86

    if slug in {"02-list-worklist", "04-field-mobile-shell", "15-feeder-home", "14-queue-desk"}:
        cx = x
        for chip in ("Today", "3 alerts", "Offline ready"):
            cx += draw_chip(draw, cx, y, chip)
        y += 40

    if slug == "13-map-explorer":
        cx = x
        for chip in ("GIS", "Climate", "Cases"):
            cx += draw_chip(draw, cx, y, chip)
        y += 36
        map_h = min(340, content_bottom - y - 40)
        draw_map_block(draw, x, y, max_w, map_h, "Hotspots + climate overlay")
        y += map_h + 12

    if slug == "09-form-capture":
        for lab, val in [("Household ID", "HH-4821"), ("Village", "Kyebando"), ("Consent", "Recorded")]:
            if y + 70 > content_bottom - 60:
                break
            draw_field(draw, x, y, max_w, lab, val)
            y += 72
        rr(draw, (x, y, x + max_w, y + 48), C["surface"], radius=12, outline=C["line"])
        tx(draw, (x + 14, y + 24), "Consent toggle · ON", size=12, bold=True, anchor="lm")
        y += 60
        draw_cta(draw, x, min(y, content_bottom - 56), max_w, "Save locally")

    elif slug == "16-upload-batch":
        rr(draw, (x, y, x + max_w, y + 90), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + max_w / 2, y + 36), "Drop CSV / choose file", size=13, bold=True, fill=C["primary"], anchor="mm")
        tx(draw, (x + max_w / 2, y + 60), "48 records · 2 warnings", size=11, fill=C["muted"], anchor="mm")
        y += 106
        rr(draw, (x, y, x + max_w, y + 44), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 22), "Validation failed · 2 rows need review", size=11, fill=C["warn"], anchor="lm")
        y += 56
        draw_cta(draw, x, y, max_w, "Upload to ingest")

    elif slug == "08-settings-admin":
        for title, sub in [
            ("Org · catchment · facilities", "Pilot peri-urban catchments"),
            ("Users & roles", "Consumers + feeder parties"),
            ("Consent & privacy", "Least privilege"),
            ("Feeder party registry", "Schools · pharmacy · lab · …"),
        ]:
            if y + 64 > content_bottom - 60:
                break
            draw_list_row(draw, x, y, max_w, title, sub)
            y += 66
        draw_cta(draw, x, min(y + 4, content_bottom - 56), max_w, "Save")

    elif slug == "10-detail-action":
        rr(draw, (x, y, x + max_w, y + 100), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 14, y + 18), "Why flagged", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 42), "Fever + rainfall + GIS cluster", size=13, bold=True)
        tx(draw, (x + 14, y + 72), "Act: testing · nets · CHW worklist", size=12)
        y += 116
        draw_cta(draw, x, y, max_w, "Mark follow-up done")

    elif slug == "07-empty-state-shell":
        rr(draw, (x, y, x + max_w, y + 156), C["surface"], radius=16, outline=C["line"])
        tx(draw, (x + max_w / 2, y + 52), "No open items", size=16, bold=True, fill=C["muted"], anchor="mm")
        tx(
            draw,
            (x + max_w / 2, y + 86),
            "New work will appear here when it is assigned.",
            size=12,
            fill=C["muted"],
            anchor="mm",
        )
        draw_cta(draw, x, y + 172, max_w, "Refresh")

    elif slug == "06-desktop-sidebar-shell":
        tx(draw, (x, y), "Content region", size=16, bold=True)
        y += 28
        rr(draw, (x, y, x + max_w, content_bottom - 20), C["surface"], radius=16, outline=C["line"])
        tx(
            draw,
            (x + max_w / 2, (y + content_bottom - 20) / 2),
            "Swap in dashboard · form · map · settings body",
            size=13,
            fill=C["muted"],
            anchor="mm",
        )

    elif slug == "03-dual-pane-desktop" and bp == "desktop":
        col = (max_w - 16) / 2
        rows = [("Fever cluster", "3 villages"), ("Maternal risk", "4 open"), ("Stock hint", "ACT +28%"), ("Gap", "Referrals")]
        for i, (t, s) in enumerate(rows):
            draw_list_row(draw, x if i % 2 == 0 else x + col + 16, y + (i // 2) * 66, col, t, s)
    else:
        # default list body for worklist / queue / feeder / metrics / shells
        rows = [
            ("Primary item", "Subtitle · context"),
            ("Secondary item", "Subtitle · context"),
            ("Tertiary item", "Subtitle · context"),
        ]
        if slug == "14-queue-desk":
            rows = [("New · maternal", "Arrive by 16:00"), ("In progress · fever", "Lab pending"), ("Completed · BP", "Outcome synced")]
        if slug == "02-list-worklist":
            rows = [("Household visit · Nakato", "Kyebando · due 09:30"), ("Follow-up · high BP", "Alert task"), ("ANC check · Achieng", "Due today")]
        if slug == "12-connector-status":
            rows = [("Clinic A", "Healthy · real-time"), ("Climate API", "Healthy"), ("School · Kikaaya", "Session overdue")]
        if slug == "15-feeder-home":
            rows = [("Next task", "Log today’s session"), ("Pending sync", "2 forms"), ("Open flags", "Absenteeism + fever")]

        if bp == "desktop" and slug in {"11-dashboard-metrics", "02-list-worklist", "15-feeder-home"} and len(rows) >= 3:
            col = (max_w - 16) / 2
            for i, (t, s) in enumerate(rows):
                draw_list_row(draw, x if i % 2 == 0 else x + col + 16, y + (i // 2) * 66, col, t, s)
            y += math.ceil(len(rows) / 2) * 66
        else:
            for t, s in rows:
                if y + 64 > content_bottom - 60:
                    break
                draw_list_row(draw, x, y, max_w, t, s)
                y += 66
            if slug not in {"13-map-explorer", "06-desktop-sidebar-shell"}:
                draw_cta(draw, x, min(y + 4, content_bottom - 56), max_w, "Primary action")

    return img


def write_components_readme(by_cat: dict[str, list[Component]]):
    lines = [
        "# Shared UI components",
        "",
        "Reusable building blocks for every `app-ui` screen. Compose screens from these — do not invent one-off chrome.",
        "",
        "Brand: teal health system · slogan **Your health, our mission.**",
        "",
        f"**{sum(len(v) for v in by_cat.values())} components** × mobile / tablet / desktop × light / dark.",
        "Dark specimens use the same filename with `-dark` before `.png`.",
        "",
    ]
    for cat, items in by_cat.items():
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| Component | Purpose | Specimens |")
        lines.append("| --- | --- | --- |")
        for c in items:
            lines.append(
                f"| **{c.title}** (`{c.slug}`) | {c.purpose} | "
                f"[m]({cat}/{c.slug}/mobile.png) · [t]({cat}/{c.slug}/tablet.png) · [d]({cat}/{c.slug}/desktop.png) |"
            )
        lines.append("")
    lines += [
        "## Regenerate",
        "",
        "```bash",
        "python app-ui/00-shared/generate_kit.py",
        "# or via",
        "python app-ui/generate_mockups.py",
        "```",
        "",
    ]
    (COMPONENTS / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_layouts_readme(layouts: list[Layout]):
    lines = [
        "# Shared layouts",
        "",
        "Page shells for maximum reuse across consumer surfaces and data-feeder modules.",
        "Pick a layout, then drop in shared components.",
        "",
        f"**{len(layouts)} layouts** × mobile / tablet / desktop × light / dark.",
        "Dark specimens use the same filename with `-dark` before `.png`.",
        "",
        "| Layout | Purpose | Composes | Specimens |",
        "| --- | --- | --- | --- |",
    ]
    for lay in layouts:
        comps = ", ".join(f"`{c}`" for c in lay.composes[:4])
        if len(lay.composes) > 4:
            comps += ", …"
        lines.append(
            f"| **{lay.title}** (`{lay.slug}`) | {lay.purpose} | {comps} | "
            f"[m]({lay.slug}/mobile.png) · [t]({lay.slug}/tablet.png) · [d]({lay.slug}/desktop.png) |"
        )
    lines += [
        "",
        "## When to use which",
        "",
        "| Need | Layout |",
        "| --- | --- |",
        "| Splash / login / role pick | `01-auth-centered-card` |",
        "| CHW phone capture | `04-field-mobile-shell` + `09-form-capture` / `02-list-worklist` |",
        "| Tablet field work | `05-field-tablet-shell` |",
        "| Desktop consoles | `06-desktop-sidebar-shell` + body layout |",
        "| Overview dashboards | `11-dashboard-metrics` or `03-dual-pane-desktop` |",
        "| Feeder party home | `15-feeder-home` |",
        "| Maps | `13-map-explorer` |",
        "| Queues | `14-queue-desk` |",
        "| Alert / referral detail | `10-detail-action` |",
        "| Admin / scopes / registry | `08-settings-admin` |",
        "| CSV / API batches | `16-upload-batch` |",
        "| EMR / HMIS / climate health | `12-connector-status` |",
        "",
        "## Regenerate",
        "",
        "```bash",
        "python app-ui/00-shared/generate_kit.py",
        "```",
        "",
    ]
    (LAYOUTS / "README.md").write_text("\n".join(lines), encoding="utf-8")


def update_shared_readme():
    path = ROOT / "README.md"
    body = path.read_text(encoding="utf-8") if path.exists() else "# 00-shared\n"
    marker = "## Reusable kit"
    kit_block = "\n".join(
        [
            "## Reusable kit",
            "",
            "Shared pieces for every module screen:",
            "",
            f"- **[components/](components/README.md)** — {len(COMPONENTS_CATALOG)} UI components (brand, buttons, chips, cards, forms, navigation, feedback, data-display)",
            f"- **[layouts/](layouts/README.md)** — {len(LAYOUTS_CATALOG)} page layouts (auth, field shells, dashboards, forms, maps, queues, feeders, admin)",
            "",
            "Each item ships **mobile · tablet · desktop** specimens.",
            "",
            "Regenerate: `python app-ui/00-shared/generate_kit.py`",
            "",
        ]
    )
    if marker in body:
        # replace from marker to end of kit section roughly — rewrite file cleanly from screens table + kit
        pre = body.split(marker)[0].rstrip() + "\n\n"
        # keep only the screens table part (before kit)
        path.write_text(pre + kit_block, encoding="utf-8")
    else:
        path.write_text(body.rstrip() + "\n\n" + kit_block, encoding="utf-8")


def main():
    COMPONENTS.mkdir(parents=True, exist_ok=True)
    LAYOUTS.mkdir(parents=True, exist_ok=True)

    by_cat: dict[str, list[Component]] = {}
    for comp in COMPONENTS_CATALOG:
        by_cat.setdefault(comp.category, []).append(comp)
        out = COMPONENTS / comp.category / comp.slug
        out.mkdir(parents=True, exist_ok=True)
        save_meta(
            out / "component.json",
            {
                "title": comp.title,
                "category": comp.category,
                "slug": comp.slug,
                "purpose": comp.purpose,
                "used_by": comp.used_by,
                "breakpoints": list(SPECIMEN.keys()),
                "themes": ["light", "dark", "system"],
            },
        )
        light_palette = C.copy()
        for bp in SPECIMEN:
            render_component(comp, bp).save(out / f"{bp}.png", optimize=True)
            C.update(DARK_C)
            render_component(comp, bp).save(out / f"{bp}-dark.png", optimize=True)
            C.clear()
            C.update(light_palette)

    for lay in LAYOUTS_CATALOG:
        out = LAYOUTS / lay.slug
        out.mkdir(parents=True, exist_ok=True)
        save_meta(
            out / "layout.json",
            {
                "title": lay.title,
                "slug": lay.slug,
                "purpose": lay.purpose,
                "composes": lay.composes,
                "surfaces": lay.surfaces,
                "breakpoints": list(SIZES.keys()),
                "themes": ["light", "dark", "system"],
            },
        )
        light_palette = C.copy()
        for bp in SIZES:
            render_layout(lay, bp).save(out / f"{bp}.png", optimize=True)
            C.update(DARK_C)
            render_layout(lay, bp).save(out / f"{bp}-dark.png", optimize=True)
            C.clear()
            C.update(light_palette)

    write_components_readme(by_cat)
    write_layouts_readme(LAYOUTS_CATALOG)
    update_shared_readme()

    n_comp = len(COMPONENTS_CATALOG) * len(SPECIMEN) * 2
    n_lay = len(LAYOUTS_CATALOG) * len(SIZES) * 2
    print(
        f"Kit: {len(COMPONENTS_CATALOG)} components ({n_comp} PNGs), "
        f"{len(LAYOUTS_CATALOG)} layouts ({n_lay} PNGs) under {ROOT}"
    )


if __name__ == "__main__":
    main()
