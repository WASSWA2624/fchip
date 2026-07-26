#!/usr/bin/env python3
"""
Reusable FCHIP UI components + layouts under app-ui/00-shared.
Derived from app-flows + SoT patterns used across app-ui screens.
Does not read frontend/.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
COMPONENTS = ROOT / "components"
LAYOUTS = ROOT / "layouts"

C = {
    "bg": (247, 250, 249),
    "surface": (255, 255, 255),
    "ink": (26, 46, 53),
    "muted": (90, 110, 118),
    "line": (214, 226, 224),
    "primary": (0, 109, 119),
    "primary_soft": (214, 237, 239),
    "accent": (20, 145, 155),
    "warn": (196, 92, 38),
    "warn_soft": (255, 236, 224),
    "ok": (46, 125, 90),
    "ok_soft": (220, 240, 230),
    "map": (168, 206, 198),
    "chrome": (18, 38, 44),
    "white": (255, 255, 255),
    "canvas": (236, 242, 240),
}

SIZES = {
    "mobile": (390, 844),
    "tablet": (768, 1024),
    "desktop": (1440, 900),
}

# Compact specimen canvas for isolated components
SPECIMEN = {
    "mobile": (390, 520),
    "tablet": (768, 560),
    "desktop": (1100, 520),
}


def font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rr(draw, box, fill, radius=12, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def tx(draw, xy, value, size=14, bold=False, fill=None, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill or C["ink"], anchor=anchor)


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


def draw_app_bar(draw, x0, y0, x1, y1, title="FCHIP", right="Your health, our mission."):
    draw.rectangle([x0, y0, x1, y1], fill=C["primary"])
    tx(draw, (x0 + 16, (y0 + y1) / 2), title, size=14, bold=True, fill=C["white"], anchor="lm")
    tx(draw, (x1 - 16, (y0 + y1) / 2), right, size=10, fill=(210, 235, 236), anchor="rm")


def draw_bottom_nav(draw, x0, y0, x1, y1, items: list[str], active=0):
    draw.rectangle([x0, y0, x1, y1], fill=C["surface"])
    draw.line([(x0, y0), (x1, y0)], fill=C["line"])
    slot = (x1 - x0) / max(len(items), 1)
    for i, item in enumerate(items):
        cx = x0 + slot * i + slot / 2
        color = C["primary"] if i == active else C["muted"]
        tx(draw, (cx, y0 + 18), "●", size=9, fill=color, anchor="mm")
        tx(draw, (cx, y0 + 40), item, size=10, fill=color, anchor="mm")


def draw_side_nav(draw, x0, y0, x1, y1, items: list[str], active=0):
    draw.rectangle([x0, y0, x1, y1], fill=C["chrome"])
    tx(draw, (x0 + 20, y0 + 24), "FCHIP", size=16, bold=True, fill=C["white"])
    tx(draw, (x0 + 20, y0 + 48), "Community Health\nIntelligence Platform", size=10, fill=(160, 190, 194))
    y = y0 + 100
    for i, item in enumerate(items):
        fill = C["accent"] if i == active else (32, 54, 60)
        rr(draw, (x0 + 12, y, x1 - 12, y + 38), fill, radius=10)
        tx(draw, (x0 + 24, y + 19), item, size=12, fill=C["white"], anchor="lm")
        y += 46
    tx(draw, (x0 + 20, y1 - 28), "Cascade Data & Feedback", size=9, fill=(120, 150, 155))


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
    tx(draw, (x + w / 2, y + 24), label, size=14, bold=True, fill=C["white"], anchor="mm")


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
    # brand
    Component("brand", "logo-lockup", "Logo lockup", "FCHIP wordmark for headers and auth", ["all shells", "splash", "login"]),
    Component("brand", "slogan-line", "Slogan line", "Your health, our mission.", ["top app bar", "auth", "cover"]),
    Component("brand", "master-loop-badge", "Master loop badge", "CAPTURE → FUSE → PREDICT → ALERT → ACT → LEARN", ["splash", "onboarding"]),
    Component("brand", "cascade-footer", "Cascade footer", "Cascade Data & Feedback cue", ["desktop side nav"]),
    # buttons
    Component("buttons", "primary-cta", "Primary CTA", "Main action on a screen", ["forms", "lists", "dashboards"]),
    Component("buttons", "secondary-cta", "Secondary CTA", "Alternate / cancel action", ["forms", "dialogs"]),
    Component("buttons", "danger-cta", "Danger CTA", "Destructive or high-urgency action", ["alerts", "revoke access"]),
    Component("buttons", "text-link", "Text link", "Inline navigation without button chrome", ["lists", "auth"]),
    # chips
    Component("chips", "status-chip", "Status chip", "Compact status or count", ["worklists", "queues"]),
    Component("chips", "filter-chip-row", "Filter chip row", "Horizontal chip group", ["maps", "lists"]),
    Component("chips", "offline-ready-chip", "Offline-ready chip", "Field offline readiness", ["CHW", "feeders"]),
    Component("chips", "risk-chip", "Risk chip", "High / elevated risk flag", ["alerts", "facility"]),
    # cards
    Component("cards", "stat-card", "Stat card", "Single metric tile", ["dashboards"]),
    Component("cards", "stat-card-row", "Stat card row", "2–4 metrics in a row", ["dashboards", "feeder homes"]),
    Component("cards", "list-row-card", "List row card", "Tappable title + subtitle row", ["worklists", "inboxes"]),
    Component("cards", "note-banner", "Note banner", "Calm info / positioning note", ["optional CHIS", "EMR note"]),
    Component("cards", "warn-banner", "Warn banner", "Attention callout", ["gaps", "consent"]),
    Component("cards", "explainability-block", "Explainability block", "Why an alert fired", ["alert follow-up", "district warnings"]),
    # forms
    Component("forms", "labeled-field", "Labeled field", "Label + value input shell", ["all forms"]),
    Component("forms", "form-stack", "Form stack", "Vertical stack of labeled fields", ["visit", "referral", "feeder entry"]),
    Component("forms", "consent-toggle", "Consent toggle", "Consent / privacy affirmation", ["capture", "self-report", "EMR share"]),
    Component("forms", "file-upload-field", "File upload field", "Batch / dataset upload cue", ["NGO", "lab batch", "HMIS"]),
    Component("forms", "select-field", "Select field", "Single-choice shell", ["urgency", "facility picker"]),
    # navigation
    Component("navigation", "top-app-bar", "Top app bar", "Brand + slogan / screen title", ["all surfaces"]),
    Component("navigation", "bottom-nav-field", "Bottom nav · field", "CHW tabs", ["01"]),
    Component("navigation", "bottom-nav-caregiver", "Bottom nav · caregiver", "Home · Report · Guidance · More", ["02"]),
    Component("navigation", "bottom-nav-feeder", "Bottom nav · feeder", "School / pharmacy / lab / MCH tabs", ["14–19", "21"]),
    Component("navigation", "bottom-nav-intel", "Bottom nav · intelligence", "Ingest · AI · GIS · Guidance", ["09"]),
    Component("navigation", "bottom-nav-insurance", "Bottom nav · insurance", "Prevent · Cohorts · Trends", ["23"]),
    Component("navigation", "side-nav-desktop", "Side nav · desktop", "Desktop chrome navigation", ["facility", "district", "admin", "feeders"]),
    Component("navigation", "role-picker-row", "Role picker row", "Workspace choice row", ["role-surface-picker"]),
    Component("navigation", "section-header", "Section header", "Title + subtitle block", ["mobile/tablet screens"]),
    # feedback
    Component("feedback", "empty-state", "Empty state", "No items yet", ["queues", "inboxes"]),
    Component("feedback", "sync-status-strip", "Sync status strip", "Queue · last sync · errors", ["sync screens", "feeder sync"]),
    Component("feedback", "success-toast", "Success toast", "Saved / synced confirmation", ["forms"]),
    Component("feedback", "error-inline", "Error inline", "Validation / feed error", ["forms", "connectors"]),
    Component("feedback", "loading-skeleton", "Loading skeleton", "Placeholder while data loads", ["dashboards"]),
    # data display
    Component("data-display", "hotspot-map", "Hotspot map", "GIS + climate overlay block", ["facility", "district", "coverage"]),
    Component("data-display", "queue-item", "Queue item", "Desk / referral / lab queue row", ["07", "16"]),
    Component("data-display", "feeder-health-pill", "Feeder health pill", "Healthy / degraded / silent", ["09 feeder board", "admin"]),
    Component("data-display", "metrics-spark-row", "Metrics spark row", "Compact trend labels", ["facility", "NGO"]),
    Component("data-display", "timeline-step", "Timeline step", "Signal → prediction → action", ["use-case detail"]),
]


def render_component(comp: Component, bp: str) -> Image.Image:
    img, draw, x, y, x1 = specimen_frame(bp, comp.title, comp.purpose)
    w = x1 - x
    slug = comp.slug

    if slug == "logo-lockup":
        tx(draw, (x, y + 20), "FCHIP", size=36, bold=True, fill=C["primary"])
        tx(draw, (x, y + 64), "Community Health Intelligence Platform", size=13, fill=C["muted"])
    elif slug == "slogan-line":
        tx(draw, (x, y + 24), "Your health, our mission.", size=20, bold=True, fill=C["primary"])
        tx(draw, (x, y + 56), "Obulamu eri Bonna · Afya kwa Wote · Oburamu bwa Boona", size=11, fill=C["muted"])
    elif slug == "master-loop-badge":
        rr(draw, (x, y, x1, y + 90), C["primary_soft"], radius=16)
        tx(
            draw,
            ((x + x1) / 2, y + 45),
            "CAPTURE → FUSE → PREDICT\nALERT → ACT → LEARN",
            size=13,
            fill=C["primary"],
            anchor="mm",
        )
    elif slug == "cascade-footer":
        rr(draw, (x, y, x1, y + 48), C["chrome"], radius=10)
        tx(draw, (x + 16, y + 24), "Cascade Data & Feedback", size=12, fill=(180, 205, 208), anchor="lm")
    elif slug == "primary-cta":
        draw_cta(draw, x, y + 10, w, "Primary action")
    elif slug == "secondary-cta":
        rr(draw, (x, y + 10, x1, y + 58), C["surface"], radius=14, outline=C["primary"], width=2)
        tx(draw, ((x + x1) / 2, y + 34), "Secondary action", size=14, bold=True, fill=C["primary"], anchor="mm")
    elif slug == "danger-cta":
        draw_cta(draw, x, y + 10, w, "Urgent / revoke", fill=C["warn"])
    elif slug == "text-link":
        tx(draw, (x, y + 24), "View all alerts ›", size=14, bold=True, fill=C["accent"])
    elif slug == "status-chip":
        cx = x
        for label in ("12 visits", "3 alerts", "Offline ready"):
            cx += draw_chip(draw, cx, y + 16, label)
    elif slug == "filter-chip-row":
        cx = x
        for label in ("District", "Climate", "GIS", "Cases"):
            cx += draw_chip(draw, cx, y + 16, label)
    elif slug == "offline-ready-chip":
        draw_chip(draw, x, y + 16, "Offline ready")
        tx(draw, (x, y + 56), "Use on CHW and feeder capture shells", size=11, fill=C["muted"])
    elif slug == "risk-chip":
        rr(draw, (x, y + 16, x + 90, y + 40), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 28), "High risk", size=11, fill=C["warn"], anchor="lm")
    elif slug == "stat-card":
        draw_stat(draw, x, y, min(180, w), 72, "Open alerts", "5")
    elif slug == "stat-card-row":
        cols = 2 if bp == "mobile" else 4
        gap = 10
        cw = (w - gap * (cols - 1)) / cols
        labels = [("CHWs", "48"), ("Referrals", "71%"), ("Outreach", "12"), ("Flags", "4")]
        for i, (lab, val) in enumerate(labels[:cols]):
            draw_stat(draw, x + i * (cw + gap), y, cw, 72, lab, val)
    elif slug == "list-row-card":
        draw_list_row(draw, x, y, w, "Household visit · Nakato", "Kyebando · due 09:30")
    elif slug == "note-banner":
        rr(draw, (x, y, x1, y + 52), C["primary_soft"], radius=12)
        tx(draw, (x + 14, y + 26), "Not core product identity — programme intelligence only", size=11, fill=C["primary"], anchor="lm")
    elif slug == "warn-banner":
        rr(draw, (x, y, x1, y + 52), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 26), "High outreach / low completed referrals — rebalance", size=11, fill=C["warn"], anchor="lm")
    elif slug == "explainability-block":
        rr(draw, (x, y, x1, y + 110), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 14, y + 18), "Why flagged", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 42), "Fever reports + heavy rain + GIS cluster", size=13, bold=True)
        tx(draw, (x + 14, y + 70), "Suggested action", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 92), "Home visit · RDT · refer if needed", size=12)
    elif slug == "labeled-field":
        draw_field(draw, x, y, w, "Household ID", "HH-4821")
    elif slug == "form-stack":
        yy = y
        for lab, val in [("Village", "Kyebando"), ("Members", "4"), ("Needs", "Fever · missed ANC")]:
            draw_field(draw, x, yy, w, lab, val)
            yy += 72
    elif slug == "consent-toggle":
        rr(draw, (x, y, x1, y + 56), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 16, y + 28), "Consent recorded", size=13, bold=True, anchor="lm")
        rr(draw, (x1 - 64, y + 14, x1 - 16, y + 42), C["ok"], radius=14)
        tx(draw, (x1 - 40, y + 28), "ON", size=11, bold=True, fill=C["white"], anchor="mm")
    elif slug == "file-upload-field":
        rr(draw, (x, y, x1, y + 88), C["surface"], radius=14, outline=C["line"])
        tx(draw, ((x + x1) / 2, y + 34), "Drop CSV / choose file", size=13, bold=True, fill=C["primary"], anchor="mm")
        tx(draw, ((x + x1) / 2, y + 58), "visits_2026-07-26.csv · 48 records", size=11, fill=C["muted"], anchor="mm")
    elif slug == "select-field":
        draw_field(draw, x, y, w, "Urgency", "Within 48 hours ▾")
    elif slug == "top-app-bar":
        draw_app_bar(draw, x, y, x1, y + 52)
    elif slug == "bottom-nav-field":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Worklist", "Alerts", "Sync", "More"])
    elif slug == "bottom-nav-caregiver":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Home", "Report", "Guidance", "More"])
    elif slug == "bottom-nav-feeder":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Home", "Session", "Screen", "Sync"])
    elif slug == "bottom-nav-intel":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Ingest", "AI", "GIS", "Guidance"])
    elif slug == "bottom-nav-insurance":
        draw_bottom_nav(draw, x, y, x1, y + 64, ["Prevent", "Cohorts", "Trends", "More"])
    elif slug == "side-nav-desktop":
        side_w = min(220, w)
        draw_side_nav(draw, x, y, x + side_w, y + 280, ["Overview", "Map", "Referrals", "Stock"])
    elif slug == "role-picker-row":
        draw_list_row(draw, x, y, w, "CHW / VHT mobile", "Worklists · visits · alerts")
        draw_list_row(draw, x, y + 66, w, "School health feed", "Sessions · screening · absenteeism")
    elif slug == "section-header":
        tx(draw, (x, y + 8), "Today’s worklist", size=22, bold=True)
        tx(draw, (x, y + 40), "Visits · follow-ups · alert tasks", size=12, fill=C["muted"])
    elif slug == "empty-state":
        rr(draw, (x, y, x1, y + 120), C["surface"], radius=14, outline=C["line"])
        tx(draw, ((x + x1) / 2, y + 44), "No open items", size=16, bold=True, fill=C["muted"], anchor="mm")
        tx(draw, ((x + x1) / 2, y + 72), "New referrals and alerts will show here", size=12, fill=C["muted"], anchor="mm")
    elif slug == "sync-status-strip":
        for i, (lab, val) in enumerate([("Queued", "7"), ("Failed", "0"), ("Last sync", "14:22")]):
            draw_stat(draw, x + i * ((w - 20) / 3 + 10), y, (w - 20) / 3, 70, lab, val)
    elif slug == "success-toast":
        rr(draw, (x, y, x1, y + 48), C["ok_soft"], radius=12)
        tx(draw, (x + 16, y + 24), "Saved locally · will sync when online", size=12, fill=C["ok"], anchor="lm")
    elif slug == "error-inline":
        rr(draw, (x, y, x1, y + 48), C["warn_soft"], radius=12)
        tx(draw, (x + 16, y + 24), "Validation failed · 2 rows need review", size=12, fill=C["warn"], anchor="lm")
    elif slug == "loading-skeleton":
        for i in range(3):
            rr(draw, (x, y + i * 40, x1, y + 28 + i * 40), C["line"], radius=8)
    elif slug == "hotspot-map":
        draw_map_block(draw, x, y, w, 160, "GIS · climate overlay")
    elif slug == "queue-item":
        draw_list_row(draw, x, y, w, "New · maternal", "Arrive by 16:00")
    elif slug == "feeder-health-pill":
        cx = x
        for label, soft in (("Healthy 12", False), ("Degraded 2", True), ("Silent 1", True)):
            tw = draw.textlength(label, font=font(11)) + 20
            fill = C["ok_soft"] if not soft or "Healthy" in label else C["warn_soft"]
            color = C["ok"] if "Healthy" in label else C["warn"]
            rr(draw, (cx, y + 16, cx + tw, y + 40), fill, radius=12)
            tx(draw, (cx + 10, y + 28), label, size=11, fill=color, anchor="lm")
            cx += tw + 8
    elif slug == "metrics-spark-row":
        tx(draw, (x, y + 12), "ACT  +28%   ·   ORS  +12%   ·   ANC kit  Stable", size=13, fill=C["primary"])
    elif slug == "timeline-step":
        steps = ["Signal", "Predict", "Action", "Learn"]
        for i, s in enumerate(steps):
            cx = x + i * (w / 4) + (w / 8)
            draw.ellipse([cx - 14, y + 20, cx + 14, y + 48], fill=C["primary"] if i < 2 else C["primary_soft"])
            tx(draw, (cx, y + 34), str(i + 1), size=11, bold=True, fill=C["white"] if i < 2 else C["primary"], anchor="mm")
            tx(draw, (cx, y + 64), s, size=11, fill=C["ink"], anchor="mm")
            if i < 3:
                draw.line([(cx + 18, y + 34), (cx + w / 4 - 18, y + 34)], fill=C["line"], width=2)
    else:
        tx(draw, (x, y + 20), comp.title, size=14, bold=True)

    # footer tag
    tx(draw, (16, img.height - 10), f"components/{comp.category}/{comp.slug} · {bp}", size=9, fill=C["muted"], anchor="lb")
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
        "auth-centered-card",
        "Auth centered card",
        "Create account / sign in — phone number + password only",
        ["logo-lockup", "slogan-line", "labeled-field", "primary-cta", "master-loop-badge"],
        ["00-shared"],
    ),
    Layout(
        "field-mobile-shell",
        "Field mobile shell",
        "CHW / caregiver / feeder capture on phone",
        ["top-app-bar", "section-header", "bottom-nav-field", "status-chip", "primary-cta"],
        ["01", "02", "14–19", "21"],
    ),
    Layout(
        "field-tablet-shell",
        "Field tablet shell",
        "Same field IA with wider content column",
        ["top-app-bar", "section-header", "bottom-nav-field", "stat-card-row", "list-row-card"],
        ["01", "02", "feeders"],
    ),
    Layout(
        "desktop-sidebar-shell",
        "Desktop sidebar shell",
        "Facility · district · admin · feeder desktop chrome",
        ["side-nav-desktop", "top-app-bar", "cascade-footer"],
        ["06–13", "14–22 desktop"],
    ),
    Layout(
        "dashboard-metrics",
        "Dashboard metrics",
        "Overview with stats + list + CTA",
        ["stat-card-row", "list-row-card", "filter-chip-row", "primary-cta"],
        ["facility", "district", "NGO", "feeder homes"],
    ),
    Layout(
        "form-capture",
        "Form capture",
        "Structured offline / online data entry",
        ["section-header", "form-stack", "consent-toggle", "primary-cta", "success-toast"],
        ["visits", "referrals", "all feeder entry"],
    ),
    Layout(
        "list-worklist",
        "List / worklist",
        "Today’s tasks, alerts, notifications",
        ["section-header", "status-chip", "list-row-card", "primary-cta", "empty-state"],
        ["CHW worklist", "alerts inbox", "notifications"],
    ),
    Layout(
        "queue-desk",
        "Queue desk",
        "Referral / lab / result queues",
        ["filter-chip-row", "queue-item", "primary-cta", "sync-status-strip"],
        ["07", "16"],
    ),
    Layout(
        "map-explorer",
        "Map explorer",
        "GIS hotspot + climate legend",
        ["filter-chip-row", "hotspot-map", "section-header"],
        ["facility map", "district map", "coverage", "population"],
    ),
    Layout(
        "detail-action",
        "Detail + action",
        "Explainable alert / referral detail with CTA",
        ["stat-card-row", "explainability-block", "list-row-card", "primary-cta", "danger-cta"],
        ["alert follow-up", "referral detail", "deploy action"],
    ),
    Layout(
        "settings-admin",
        "Settings / admin",
        "Org · roles · consent · API scopes · feeder registry",
        ["section-header", "list-row-card", "note-banner", "primary-cta"],
        ["13", "08 scopes", "20 mapping", "22 config"],
    ),
    Layout(
        "feeder-home",
        "Feeder home",
        "Home for schools, pharmacy, lab, MCH, corporate, NCD, community, climate",
        ["stat-card-row", "list-row-card", "offline-ready-chip", "primary-cta", "bottom-nav-feeder"],
        ["14–22"],
    ),
    Layout(
        "dual-pane-desktop",
        "Dual-pane desktop",
        "Two-column lists / dashboards on wide screens",
        ["side-nav-desktop", "list-row-card", "stat-card-row"],
        ["facility overview", "cascade metrics", "NGO monitor"],
    ),
    Layout(
        "upload-batch",
        "Upload / batch",
        "File upload + validation + push to ingest",
        ["file-upload-field", "error-inline", "success-toast", "primary-cta", "note-banner"],
        ["NGO upload", "lab batch", "outreach batch", "HMIS exchange"],
    ),
    Layout(
        "connector-status",
        "Connector status",
        "External system health (EMR, HMIS, climate)",
        ["stat-card-row", "list-row-card", "feeder-health-pill", "warn-banner"],
        ["08", "20", "22", "09 feeder board"],
    ),
    Layout(
        "empty-state-shell",
        "Empty state shell",
        "Happy-path layout with empty body (worklist / queue)",
        ["section-header", "status-chip", "empty-state", "primary-cta"],
        ["01 worklist-empty", "07 referral-queue-empty"],
    ),
    Layout(
        "insurance-prevention",
        "Insurance prevention",
        "§7 prevention population insights — not claims / not CHIS identity",
        ["stat-card-row", "list-row-card", "note-banner", "primary-cta"],
        ["23-insurance-insights"],
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

    if bp == "desktop" and slug not in {"auth-centered-card"}:
        left = 220
        items = {
            "desktop-sidebar-shell": ["Overview", "Map", "Referrals", "Stock"],
            "dashboard-metrics": ["Overview", "Map", "Referrals", "Stock"],
            "dual-pane-desktop": ["Overview", "Map", "Metrics", "Plan"],
            "settings-admin": ["Org", "Users", "Consent", "APIs"],
            "connector-status": ["Status", "Scopes", "Log", "Onboard"],
            "feeder-home": ["Home", "Session", "Screen", "Sync"],
            "map-explorer": ["Map", "Warnings", "Metrics", "Plan"],
            "form-capture": ["Home", "Capture", "Queue", "Sync"],
            "list-worklist": ["Worklist", "Alerts", "Sync", "More"],
            "queue-desk": ["Queue", "Detail", "Outcomes", "Sync"],
            "detail-action": ["Inbox", "Detail", "Act", "More"],
            "upload-batch": ["Upload", "Validate", "Push", "Audit"],
            "field-mobile-shell": ["Worklist", "Alerts", "Sync", "More"],
            "field-tablet-shell": ["Worklist", "Alerts", "Sync", "More"],
        }.get(slug, ["Home", "Map", "Metrics", "More"])
        draw_side_nav(draw, 0, 0, left, h, items)
        draw_app_bar(draw, left, 0, w, top, title=layout.title, right="DESKTOP")
    elif slug == "auth-centered-card":
        draw_app_bar(draw, 0, 0, w, top)
    else:
        draw_app_bar(draw, 0, 0, w, top)
        if bp != "desktop":
            bottom_nav_h = 64
            nav_items = {
                "field-mobile-shell": ["Worklist", "Alerts", "Sync", "More"],
                "field-tablet-shell": ["Worklist", "Alerts", "Sync", "More"],
                "feeder-home": ["Home", "Session", "Screen", "Sync"],
                "list-worklist": ["Worklist", "Alerts", "Sync", "More"],
                "form-capture": ["Home", "Form", "Sync", "More"],
                "queue-desk": ["Queue", "Open", "Done", "More"],
                "map-explorer": ["Map", "Warnings", "Metrics", "Plan"],
                "dashboard-metrics": ["Overview", "Map", "Referrals", "Stock"],
                "detail-action": ["Inbox", "Act", "Sync", "More"],
                "upload-batch": ["Upload", "Queue", "Sync", "More"],
                "settings-admin": ["Org", "Users", "Consent", "More"],
                "connector-status": ["Status", "Log", "Scopes", "More"],
                "dual-pane-desktop": ["Overview", "Map", "Metrics", "More"],
            }.get(slug, ["Home", "List", "Sync", "More"])
            draw_bottom_nav(draw, 0, h - bottom_nav_h, w, h, nav_items)

    pad = 20 if bp == "mobile" else 28
    x = left + pad
    max_w = w - left - pad * 2
    y = top + 18
    content_bottom = h - bottom_nav_h - 16

    if slug == "auth-centered-card":
        card_w = min(420, max_w)
        cx = left + (w - left - card_w) / 2
        cy = top + (60 if bp != "mobile" else 36)
        rr(draw, (cx, cy, cx + card_w, cy + 420), C["surface"], radius=20, outline=C["line"])
        tx(draw, (cx + card_w / 2, cy + 48), "FCHIP", size=28, bold=True, fill=C["primary"], anchor="mm")
        tx(draw, (cx + card_w / 2, cy + 84), "Your health, our mission.", size=13, fill=C["muted"], anchor="mm")
        rr(draw, (cx + 36, cy + 120, cx + card_w - 36, cy + 210), C["primary_soft"], radius=14)
        tx(
            draw,
            (cx + card_w / 2, cy + 165),
            "CAPTURE → FUSE → PREDICT\nALERT → ACT → LEARN",
            size=12,
            fill=C["primary"],
            anchor="mm",
        )
        draw_field(draw, cx + 28, cy + 220, card_w - 56, "Phone number", "+256 700 000 000")
        draw_field(draw, cx + 28, cy + 290, card_w - 56, "Password", "••••••••")
        draw_cta(draw, cx + 28, cy + 370, card_w - 56, "Sign in")
        return img

    if bp != "desktop":
        tx(draw, (x, y), layout.title, size=20, bold=True)
        y += 26
        tx(draw, (x, y), layout.purpose, size=12, fill=C["muted"])
        y += 28
    else:
        tx(draw, (x, y), layout.purpose, size=12, fill=C["muted"])
        y += 26

    if slug in {"dashboard-metrics", "feeder-home", "connector-status", "detail-action", "dual-pane-desktop", "field-tablet-shell"}:
        cols = 2 if bp == "mobile" else 4
        gap = 10
        cw = (max_w - gap * (cols - 1)) / cols
        stats = [("Open", "5"), ("Queued", "18"), ("Risk", "Elev."), ("Sync", "OK")]
        for i, (lab, val) in enumerate(stats[:cols]):
            draw_stat(draw, x + i * (cw + gap), y, cw, 70, lab, val)
        y += 86

    if slug in {"list-worklist", "field-mobile-shell", "feeder-home", "queue-desk"}:
        cx = x
        for chip in ("Today", "3 alerts", "Offline ready"):
            cx += draw_chip(draw, cx, y, chip)
        y += 40

    if slug == "map-explorer":
        cx = x
        for chip in ("GIS", "Climate", "Cases"):
            cx += draw_chip(draw, cx, y, chip)
        y += 36
        map_h = min(340, content_bottom - y - 40)
        draw_map_block(draw, x, y, max_w, map_h, "Hotspots + climate overlay")
        y += map_h + 12

    if slug == "form-capture":
        for lab, val in [("Household ID", "HH-4821"), ("Village", "Kyebando"), ("Consent", "Recorded")]:
            if y + 70 > content_bottom - 60:
                break
            draw_field(draw, x, y, max_w, lab, val)
            y += 72
        rr(draw, (x, y, x + max_w, y + 48), C["surface"], radius=12, outline=C["line"])
        tx(draw, (x + 14, y + 24), "Consent toggle · ON", size=12, bold=True, anchor="lm")
        y += 60
        draw_cta(draw, x, min(y, content_bottom - 56), max_w, "Save locally")

    elif slug == "upload-batch":
        rr(draw, (x, y, x + max_w, y + 90), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + max_w / 2, y + 36), "Drop CSV / choose file", size=13, bold=True, fill=C["primary"], anchor="mm")
        tx(draw, (x + max_w / 2, y + 60), "48 records · 2 warnings", size=11, fill=C["muted"], anchor="mm")
        y += 106
        rr(draw, (x, y, x + max_w, y + 44), C["warn_soft"], radius=12)
        tx(draw, (x + 14, y + 22), "Validation failed · 2 rows need review", size=11, fill=C["warn"], anchor="lm")
        y += 56
        draw_cta(draw, x, y, max_w, "Upload to ingest")

    elif slug == "settings-admin":
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

    elif slug == "detail-action":
        rr(draw, (x, y, x + max_w, y + 100), C["surface"], radius=14, outline=C["line"])
        tx(draw, (x + 14, y + 18), "Why flagged", size=11, fill=C["muted"])
        tx(draw, (x + 14, y + 42), "Fever + rainfall + GIS cluster", size=13, bold=True)
        tx(draw, (x + 14, y + 72), "Act: testing · nets · CHW worklist", size=12)
        y += 116
        draw_cta(draw, x, y, max_w, "Mark follow-up done")

    elif slug == "desktop-sidebar-shell":
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

    elif slug == "dual-pane-desktop" and bp == "desktop":
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
        if slug == "queue-desk":
            rows = [("New · maternal", "Arrive by 16:00"), ("In progress · fever", "Lab pending"), ("Completed · BP", "Outcome synced")]
        if slug == "list-worklist":
            rows = [("Household visit · Nakato", "Kyebando · due 09:30"), ("Follow-up · high BP", "Alert task"), ("ANC check · Achieng", "Due today")]
        if slug == "connector-status":
            rows = [("Clinic A", "Healthy · real-time"), ("Climate API", "Healthy"), ("School · Kikaaya", "Session overdue")]
        if slug == "feeder-home":
            rows = [("Next task", "Log today’s session"), ("Pending sync", "2 forms"), ("Open flags", "Absenteeism + fever")]

        if bp == "desktop" and slug in {"dashboard-metrics", "list-worklist", "feeder-home"} and len(rows) >= 3:
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
            if slug not in {"map-explorer", "desktop-sidebar-shell"}:
                draw_cta(draw, x, min(y + 4, content_bottom - 56), max_w, "Primary action")

    tx(
        draw,
        (x, h - bottom_nav_h - 8 if bottom_nav_h else h - 10),
        f"layouts/{layout.slug} · {bp}",
        size=9,
        fill=C["muted"],
        anchor="lb",
    )
    return img


def write_components_readme(by_cat: dict[str, list[Component]]):
    lines = [
        "# Shared UI components",
        "",
        "Reusable building blocks for every `app-ui` screen. Compose screens from these — do not invent one-off chrome.",
        "",
        "Brand: teal health system · slogan **Your health, our mission.**",
        "",
        f"**{sum(len(v) for v in by_cat.values())} components** × mobile / tablet / desktop.",
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
        f"**{len(layouts)} layouts** × mobile / tablet / desktop.",
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
        "| Splash / login / role pick | `auth-centered-card` |",
        "| CHW phone capture | `field-mobile-shell` + `form-capture` / `list-worklist` |",
        "| Tablet field work | `field-tablet-shell` |",
        "| Desktop consoles | `desktop-sidebar-shell` + body layout |",
        "| Overview dashboards | `dashboard-metrics` or `dual-pane-desktop` |",
        "| Feeder party home | `feeder-home` |",
        "| Maps | `map-explorer` |",
        "| Queues | `queue-desk` |",
        "| Alert / referral detail | `detail-action` |",
        "| Admin / scopes / registry | `settings-admin` |",
        "| CSV / API batches | `upload-batch` |",
        "| EMR / HMIS / climate health | `connector-status` |",
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
            },
        )
        for bp in SPECIMEN:
            render_component(comp, bp).save(out / f"{bp}.png", optimize=True)

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
            },
        )
        for bp in SIZES:
            render_layout(lay, bp).save(out / f"{bp}.png", optimize=True)

    write_components_readme(by_cat)
    write_layouts_readme(LAYOUTS_CATALOG)
    update_shared_readme()

    n_comp = len(COMPONENTS_CATALOG) * 3
    n_lay = len(LAYOUTS_CATALOG) * 3
    print(
        f"Kit: {len(COMPONENTS_CATALOG)} components ({n_comp} PNGs), "
        f"{len(LAYOUTS_CATALOG)} layouts ({n_lay} PNGs) under {ROOT}"
    )


if __name__ == "__main__":
    main()
