#!/usr/bin/env python3
"""
Generate FCHIP app-ui mockups (mobile / tablet / desktop) from app-flows + SoT.
Does not read or import anything from frontend/.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent

# Brand — health teal (not purple / cream-serif AI defaults)
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
    "map_hot": (196, 92, 38),
    "chrome": (18, 38, 44),
    "white": (255, 255, 255),
}

SIZES = {
    "mobile": (390, 844),
    "tablet": (768, 1024),
    "desktop": (1440, 900),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def round_rect(draw: ImageDraw.ImageDraw, box, fill, radius=12, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size=14, bold=False, fill=None, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill or C["ink"], anchor=anchor)


def wrap(draw, value: str, max_w: int, size=13) -> list[str]:
    f = font(size)
    words = value.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [value]


@dataclass
class Screen:
    module: str
    slug: str
    title: str
    subtitle: str
    kind: str  # list | form | map | dashboard | detail | auth | queue | settings
    chips: list[str] = field(default_factory=list)
    rows: list[tuple[str, str]] = field(default_factory=list)
    stats: list[tuple[str, str]] = field(default_factory=list)
    note: str = ""
    primary_cta: str = ""
    nav: str = "field"  # field | facility | district | partner | admin | auth


SCREENS: list[Screen] = [
    # 00 shared
    Screen(
        "00-shared",
        "splash",
        "FCHIP",
        "Your health, our mission.",
        "auth",
        note="Community Health Intelligence Platform",
        primary_cta="Continue",
        nav="auth",
    ),
    Screen(
        "00-shared",
        "login",
        "Sign in",
        "CHW · Facility · District · Partner",
        "auth",
        rows=[("Email / phone", "chw@fchip.ug"), ("Password", "••••••••")],
        primary_cta="Sign in",
        nav="auth",
    ),
    Screen(
        "00-shared",
        "role-surface-picker",
        "Choose your workspace",
        "One platform · cascade surfaces",
        "list",
        rows=[
            ("CHW / VHT mobile", "Worklists · visits · alerts"),
            ("Facility dashboard", "Trends · referrals · maps"),
            ("District / MoH console", "Early warning · M&E"),
            ("NGO / partner M&E", "Programme impact"),
            ("Admin", "Org · consent · access"),
        ],
        nav="auth",
    ),
    Screen(
        "00-shared",
        "notifications-center",
        "Notifications",
        "Alerts across your surfaces",
        "list",
        rows=[
            ("Outbreak risk · Bukoto", "Climate + fever cluster"),
            ("Referral overdue", "Household #4821"),
            ("Sync complete", "14 visits uploaded"),
            ("Campaign starts tomorrow", "School health · Kisaasi"),
        ],
        nav="field",
    ),
    # 01 CHW
    Screen(
        "01-chw-vht-mobile",
        "worklist-home",
        "Today’s worklist",
        "Visits · follow-ups · alert tasks",
        "list",
        chips=["12 visits", "3 alerts", "Offline ready"],
        rows=[
            ("Household visit · Nakato", "Kyebando · due 09:30"),
            ("Follow-up · high BP", "Alert task · Kamwokya"),
            ("ANC check · Achieng", "Maternal risk · due today"),
            ("School session support", "Kikaaya P.S. · 14:00"),
        ],
        primary_cta="Start next visit",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "household-visit-form",
        "Household visit",
        "Offline structured capture",
        "form",
        rows=[
            ("Household ID", "HH-4821"),
            ("Village / parish", "Kyebando"),
            ("Members present", "4"),
            ("Needs flagged", "Fever · missed ANC"),
            ("Notes", "Mother reports 2 days fever"),
        ],
        primary_cta="Save locally",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "symptoms-vitals",
        "Symptoms & vitals",
        "Structured field checks",
        "form",
        rows=[
            ("Temperature", "38.4 °C"),
            ("Blood pressure", "128 / 84"),
            ("Symptoms", "Fever · headache"),
            ("Malaria RDT", "Pending"),
            ("Duration", "2 days"),
        ],
        primary_cta="Continue to MCH",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "maternal-child-indicators",
        "Maternal / child",
        "ANC · growth · immunisation",
        "form",
        rows=[
            ("Pregnancy week", "28"),
            ("ANC adherence", "1 visit overdue"),
            ("Hb proxy / anaemia risk", "Elevated"),
            ("Child growth", "On track"),
            ("Immunisation", "Measles due"),
        ],
        primary_cta="Save indicators",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "create-referral",
        "Create referral",
        "Send household to facility",
        "form",
        rows=[
            ("Reason", "High-risk pregnancy"),
            ("Urgency", "Within 48 hours"),
            ("Facility", "Partner clinic · Bukoto"),
            ("Escort needed", "Yes"),
            ("Consent", "Recorded"),
        ],
        primary_cta="Submit referral",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "alerts-inbox",
        "Alerts inbox",
        "Risk flags from intelligence core",
        "list",
        chips=["2 high", "1 climate"],
        rows=[
            ("Maternal risk · Achieng", "Missed ANC + heat strain"),
            ("Fever cluster nearby", "3 villages · rainfall high"),
            ("Child immunisation gap", "Parish coverage low"),
        ],
        primary_cta="Open top alert",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "alert-follow-up",
        "Act on alert",
        "Explainable next steps",
        "detail",
        stats=[("Risk", "High"), ("Window", "14 days"), ("Signal", "Climate+fever")],
        rows=[
            ("Why flagged", "Fever reports + heavy rain + GIS cluster"),
            ("Suggested action", "Home visit · RDT · refer if needed"),
            ("Related households", "6 in catchment"),
        ],
        primary_cta="Mark follow-up done",
        nav="field",
    ),
    Screen(
        "01-chw-vht-mobile",
        "sync-status",
        "Sync status",
        "Offline queue health",
        "detail",
        stats=[("Queued", "7"), ("Failed", "0"), ("Last sync", "14:22")],
        rows=[
            ("Visits pending upload", "5 forms"),
            ("Referrals pending", "2"),
            ("Connection", "Weak · will retry"),
        ],
        primary_cta="Sync now",
        nav="field",
    ),
    # 02 community
    Screen(
        "02-community-caregiver",
        "my-household",
        "My household",
        "Optional caregiver self-view",
        "dashboard",
        stats=[("Members", "5"), ("Open tasks", "2"), ("CHW", "Namuli")],
        rows=[
            ("Next visit", "Tomorrow · morning"),
            ("Open referral", "ANC follow-up"),
            ("Guidance", "Hydration · heat advice"),
        ],
        nav="field",
    ),
    Screen(
        "02-community-caregiver",
        "self-report",
        "Self-report",
        "Symptoms · needs · concerns",
        "form",
        rows=[
            ("Who is unwell", "Child · 4 yrs"),
            ("Symptoms", "Diarrhoea · fever"),
            ("Since when", "Yesterday"),
            ("Need help now", "Yes · CHW call"),
        ],
        primary_cta="Send to CHW worklist",
        nav="field",
    ),
    Screen(
        "02-community-caregiver",
        "guidance-hints",
        "Guidance",
        "Care tips · appointment hints",
        "list",
        rows=[
            ("Heat safety", "Rest · drink water · shade"),
            ("ANC reminder", "Clinic visit due Friday"),
            ("When to seek care", "Fever > 2 days · danger signs"),
        ],
        nav="field",
    ),
    # 03 outreach
    Screen(
        "03-outreach-school-health",
        "campaign-planner",
        "Campaign planner",
        "Outreach · screening · school health",
        "dashboard",
        chips=["Draft", "3 sites"],
        stats=[("Sessions", "8"), ("Screenings", "240"), ("Schools", "4")],
        rows=[
            ("Malaria screening camp", "Bukoto · next week"),
            ("School health day", "Kisaasi P.S."),
            ("NCD BP drive", "Corporate + parish"),
        ],
        primary_cta="Create campaign",
        nav="district",
    ),
    Screen(
        "03-outreach-school-health",
        "session-log",
        "Session log",
        "Attendance · topics · outcomes",
        "form",
        rows=[
            ("Site", "Kamwokya community hall"),
            ("Topic", "Maternal danger signs"),
            ("Attendance", "62"),
            ("Screenings done", "28"),
            ("Referrals made", "5"),
        ],
        primary_cta="Save session",
        nav="district",
    ),
    Screen(
        "03-outreach-school-health",
        "coverage-map",
        "Coverage map",
        "Where programmes ran",
        "map",
        chips=["Outreach", "Schools"],
        note="Village/parish coverage for planned vs completed sessions",
        nav="district",
    ),
    # 04 cascade metrics
    Screen(
        "04-cascade-metrics",
        "indicators-overview",
        "Cascade metrics",
        "CHW · outreach · referrals · MCH · education",
        "dashboard",
        stats=[
            ("CHWs active", "48"),
            ("Referrals done", "71%"),
            ("Outreach", "12"),
            ("MCH visits", "186"),
        ],
        rows=[
            ("School sessions", "9 this month"),
            ("IGA households", "Optional · 34"),
            ("CHIS enrolment", "Optional · 210"),
        ],
        nav="district",
    ),
    Screen(
        "04-cascade-metrics",
        "gap-detection",
        "Gap detection",
        "Learn · improve · serve again",
        "list",
        chips=["2 gaps"],
        rows=[
            ("High outreach / low completed referrals", "Rebalance facility capacity"),
            ("Low CHW supervision in Kikaaya", "Schedule mentor visits"),
            ("School sessions lagging", "Add 2 health days"),
        ],
        primary_cta="Open action plan",
        nav="district",
    ),
    Screen(
        "04-cascade-metrics",
        "partner-reports",
        "Partner reports",
        "M&E exports from metrics spine",
        "list",
        rows=[
            ("Monthly cascade brief", "PDF · ready"),
            ("Referral completion trend", "CSV"),
            ("Outreach coverage", "Map pack"),
        ],
        primary_cta="Generate report",
        nav="partner",
    ),
    # 05 CHIS
    Screen(
        "05-chis-livelihoods",
        "enrolment",
        "CHIS enrolment",
        "Optional financial-protection data",
        "form",
        rows=[
            ("Household", "HH-4821"),
            ("Scheme", "Partner CHIS"),
            ("Members enrolled", "5"),
            ("Status", "Active"),
        ],
        note="Not core product identity — programme intelligence only",
        primary_cta="Save enrolment",
        nav="partner",
    ),
    Screen(
        "05-chis-livelihoods",
        "contributions",
        "Contributions",
        "Where partners capture payments",
        "list",
        rows=[
            ("July contribution", "Paid"),
            ("June contribution", "Paid"),
            ("May contribution", "Partial"),
        ],
        nav="partner",
    ),
    Screen(
        "05-chis-livelihoods",
        "claims-access",
        "Claims / access",
        "Livelihood-linked care access",
        "detail",
        stats=[("Open claims", "1"), ("Paid", "4"), ("IGA link", "Yes")],
        rows=[
            ("Latest claim", "ANC visit · approved"),
            ("Access note", "Covered at partner clinic"),
        ],
        nav="partner",
    ),
    # 06 facility
    Screen(
        "06-facility-dashboard",
        "overview",
        "Facility overview",
        "Alerts · caseload risk · cascade gaps",
        "dashboard",
        stats=[
            ("Open alerts", "5"),
            ("Inbound referrals", "18"),
            ("Catchment risk", "Elevated"),
            ("Cascade gap", "Referrals"),
        ],
        rows=[
            ("Fever cluster", "3 villages · 14-day window"),
            ("Maternal high-risk", "4 open"),
            ("Stock hint", "ACT demand rising"),
        ],
        nav="facility",
    ),
    Screen(
        "06-facility-dashboard",
        "catchment-map",
        "Catchment map",
        "Village hotspots + climate overlay",
        "map",
        chips=["GIS", "Climate"],
        note="Hotspots fused with rainfall / heat layers",
        nav="facility",
    ),
    Screen(
        "06-facility-dashboard",
        "open-referrals",
        "Open referrals",
        "Inbound from CHWs · completion",
        "queue",
        chips=["18 open"],
        rows=[
            ("HH-4821 · ANC risk", "CHW Namuli · due today"),
            ("HH-1190 · child fever", "Kyebando · urgent"),
            ("HH-3302 · NCD follow-up", "Scheduled"),
        ],
        primary_cta="Complete selected",
        nav="facility",
    ),
    Screen(
        "06-facility-dashboard",
        "stock-signal",
        "Stock signal",
        "Demand forecast hints",
        "dashboard",
        stats=[("ACT", "+28%"), ("ORS", "+12%"), ("ANC kit", "Stable")],
        rows=[
            ("Driver", "Fever cluster + rainfall"),
            ("Suggestion", "Pre-stock pharmacy partners"),
            ("Horizon", "Next 14 days"),
        ],
        nav="facility",
    ),
    Screen(
        "06-facility-dashboard",
        "outreach-priorities",
        "Outreach priorities",
        "Where facility should support field action",
        "list",
        rows=[
            ("Testing camp · Bukoto", "Outbreak window"),
            ("ANC catch-up visits", "4 mothers"),
            ("School immunisation support", "Kisaasi"),
        ],
        nav="facility",
    ),
    # 07 referrals desk
    Screen(
        "07-referrals-desk",
        "referral-queue",
        "Referrals desk",
        "Facility referral queue",
        "queue",
        chips=["Queue", "Today"],
        rows=[
            ("New · maternal", "Arrive by 16:00"),
            ("In progress · fever", "Lab pending"),
            ("Completed · BP", "Outcome synced"),
        ],
        primary_cta="Claim next",
        nav="facility",
    ),
    Screen(
        "07-referrals-desk",
        "referral-detail",
        "Referral detail",
        "Track completion · link EMR outcome",
        "detail",
        stats=[("Status", "In care"), ("Urgency", "48h"), ("Source", "CHW")],
        rows=[
            ("Reason", "Pre-eclampsia risk"),
            ("Household", "HH-4821 · Kamwokya"),
            ("EMR outcome", "Awaiting secure sync"),
            ("Cascade metric", "Counts when completed"),
        ],
        primary_cta="Mark completed",
        nav="facility",
    ),
    # 08 EMR connector
    Screen(
        "08-emr-connector",
        "connector-status",
        "EMR / HMS connector",
        "Secure ingest — does not replace EMR",
        "dashboard",
        stats=[("Linked facilities", "3"), ("Last push", "2m ago"), ("Errors", "0")],
        rows=[
            ("Clinic A", "Healthy · real-time"),
            ("Medical centre B", "Healthy · batch"),
            ("Hospital C", "Onboarding"),
        ],
        note="Authenticated · consent-aware · least privilege",
        nav="admin",
    ),
    Screen(
        "08-emr-connector",
        "api-scopes-setup",
        "API scopes setup",
        "What clinical data may flow in",
        "settings",
        rows=[
            ("Encounters", "Allowed"),
            ("Vitals / diagnoses", "Allowed"),
            ("Pharmacy dispense", "Partner only"),
            ("Raw notes / PHI dumps", "Blocked"),
        ],
        primary_cta="Save scopes",
        nav="admin",
    ),
    # 09 intelligence
    Screen(
        "09-intelligence",
        "ingest-pipeline",
        "Ingest & sync",
        "Field · EMR · climate → store",
        "dashboard",
        stats=[("Sources live", "11"), ("Lag", "48s"), ("Validate fails", "0.2%")],
        rows=[
            ("CHW mobile", "Streaming"),
            ("Climate API", "Rainfall · heat"),
            ("EMR APIs", "3 facilities"),
            ("School / outreach", "Daily batch"),
        ],
        nav="admin",
    ),
    Screen(
        "09-intelligence",
        "ai-risk-scores",
        "AI / predictive",
        "Risk scores · explainable alerts",
        "dashboard",
        stats=[("Models v1", "On"), ("Alerts today", "14"), ("Top risk", "Fever cluster")],
        rows=[
            ("Surveillance", "Malaria window 14d"),
            ("Maternal", "4 high-risk"),
            ("Child health", "Diarrhoea cluster watch"),
            ("NCD", "BP hotspot · parish 3"),
        ],
        nav="district",
    ),
    Screen(
        "09-intelligence",
        "gis-explorer",
        "GIS maps",
        "Disease distribution · hotspots · gaps",
        "map",
        chips=["Cases", "Resources"],
        note="Village/parish geography for early warning",
        nav="district",
    ),
    Screen(
        "09-intelligence",
        "climate-fusion",
        "Climate fusion",
        "Rainfall · heat · floods × health",
        "dashboard",
        stats=[("Rain 7d", "High"), ("Heat", "Moderate"), ("Flood risk", "Low")],
        rows=[
            ("Linked conditions", "Malaria · diarrhoea · heat strain"),
            ("Fusion note", "Rain + fever GIS cluster"),
            ("Action window", "Deploy testing / nets"),
        ],
        nav="district",
    ),
    Screen(
        "09-intelligence",
        "alerts-worklists-engine",
        "Alerts & worklists engine",
        "Routes intelligence to surfaces",
        "settings",
        rows=[
            ("CHW mobile", "Field alerts · tasks"),
            ("Facility dashboard", "Caseload · referrals"),
            ("District console", "Early warnings"),
            ("Explainability", "Always show why"),
        ],
        primary_cta="Save routing",
        nav="admin",
    ),
    # 10 district
    Screen(
        "10-district-moh",
        "population-map",
        "Population map",
        "District early-warning geography",
        "map",
        chips=["District", "Climate"],
        note="Kampala peri-urban catchments → district scale",
        nav="district",
    ),
    Screen(
        "10-district-moh",
        "early-warnings",
        "Early warnings",
        "Explainable outbreak & risk notices",
        "list",
        chips=["Active"],
        rows=[
            ("Malaria risk · 14 days", "3 villages · heavy rain"),
            ("Maternal cluster", "Missed ANC rising"),
            ("Medicine demand", "ACT pre-stock advised"),
        ],
        primary_cta="Deploy response",
        nav="district",
    ),
    Screen(
        "10-district-moh",
        "action-deploy",
        "Deploy action",
        "Testing · stock · outreach",
        "form",
        rows=[
            ("Response type", "Targeted testing + nets"),
            ("Parishes", "Bukoto · Kyebando · Kikaaya"),
            ("Pharmacy pre-stock", "ACT · RDTs"),
            ("CHW blast", "Alert worklists"),
        ],
        primary_cta="Launch deployment",
        nav="district",
    ),
    Screen(
        "10-district-moh",
        "cascade-planning",
        "Cascade M&E planning",
        "Plan from gaps and metrics",
        "dashboard",
        stats=[("Gaps", "2"), ("Camps planned", "3"), ("Training slots", "12")],
        rows=[
            ("Rebalance referrals", "Facility capacity week"),
            ("CHW supervision", "Kikaaya focus"),
            ("School health push", "2 sessions"),
        ],
        nav="district",
    ),
    # 11 NGO
    Screen(
        "11-ngo-partner",
        "programme-monitoring",
        "Programme monitoring",
        "Partner-scoped real-time M&E",
        "dashboard",
        stats=[("Reach", "1.2k"), ("Sessions", "18"), ("Referrals", "64%")],
        rows=[
            ("This week", "4 outreach days"),
            ("Top parish", "Kamwokya"),
            ("Risk flag", "Referral completion dip"),
        ],
        nav="partner",
    ),
    Screen(
        "11-ngo-partner",
        "impact-evidence",
        "Impact evidence",
        "Optimisation · donor-ready proof",
        "list",
        rows=[
            ("Before / after cascade gaps", "Improved 11 pts"),
            ("Climate-aware response time", "Down 3 days"),
            ("MCH referral completion", "Up 9 pts"),
        ],
        primary_cta="Export brief",
        nav="partner",
    ),
    # 12 research
    Screen(
        "12-research-exports",
        "evidence-catalog",
        "Evidence catalog",
        "Anonymised datasets · no raw PHI dumps",
        "list",
        rows=[
            ("Community fever signals 2026-Q2", "Aggregated"),
            ("ANC adherence catchment A", "De-identified"),
            ("Climate–health fusion samples", "Approved use"),
        ],
        nav="partner",
    ),
    Screen(
        "12-research-exports",
        "export-request",
        "Export request",
        "Approved research access",
        "form",
        rows=[
            ("Institution", "Partner university"),
            ("Purpose", "Climate-linked malaria study"),
            ("Dataset", "Fever + rainfall aggregates"),
            ("Ethics / approval", "Attached"),
        ],
        primary_cta="Submit request",
        nav="partner",
    ),
    # 13 admin
    Screen(
        "13-admin-consent",
        "org-catchment",
        "Org · catchment · facilities",
        "Where FCHIP is deployed",
        "settings",
        rows=[
            ("Catchments", "Bukoto · Kyebando · Kisaasi · Kamwokya · Kikaaya"),
            ("Partner facilities", "3 linked"),
            ("District scope", "Phase 1 peri-urban"),
        ],
        primary_cta="Save org",
        nav="admin",
    ),
    Screen(
        "13-admin-consent",
        "users-roles",
        "Users & roles",
        "CHW · Facility · District · Partner",
        "settings",
        rows=[
            ("CHW / VHT", "Field capture · alerts"),
            ("Facility staff", "Dashboard · referrals desk"),
            ("District / MoH", "Early warning · planning"),
            ("NGO partner", "Scoped M&E"),
            ("Admin", "Consent · API scopes"),
        ],
        primary_cta="Invite user",
        nav="admin",
    ),
    Screen(
        "13-admin-consent",
        "consent-privacy",
        "Consent & privacy",
        "Household consent · least privilege",
        "settings",
        rows=[
            ("Field capture consent", "Required"),
            ("Caregiver self-report", "Optional · explicit"),
            ("Research exports", "Anonymised only"),
            ("Retention", "Programme policy"),
        ],
        primary_cta="Update policy",
        nav="admin",
    ),
    Screen(
        "13-admin-consent",
        "emr-api-access",
        "EMR API access",
        "Facility credentials · scopes",
        "settings",
        rows=[
            ("Facility keys", "Rotate every 90 days"),
            ("Scopes", "Encounters · vitals"),
            ("Audit log", "Enabled"),
            ("Break-glass", "Disabled by default"),
        ],
        primary_cta="Issue key",
        nav="admin",
    ),
]


NAV = {
    "auth": [],
    "field": ["Worklist", "Alerts", "Sync", "More"],
    "facility": ["Overview", "Map", "Referrals", "Stock"],
    "district": ["Map", "Warnings", "Metrics", "Plan"],
    "partner": ["Monitor", "Evidence", "Reports", "More"],
    "admin": ["Org", "Users", "Consent", "APIs"],
}


def draw_header(draw, w, h, screen: Screen, breakpoint: str, content_left: int):
    bar_h = 56 if breakpoint != "desktop" else 64
    draw.rectangle([content_left, 0, w, bar_h], fill=C["primary"])
    label = screen.title if content_left else "FCHIP"
    text(draw, (content_left + 16, bar_h // 2), label, size=16, bold=True, fill=C["white"], anchor="lm")
    right = "DESKTOP" if content_left else "Your health, our mission."
    text(
        draw,
        (w - 16, bar_h // 2),
        right,
        size=11 if not content_left else 10,
        fill=(210, 235, 236),
        anchor="rm",
    )
    return bar_h


def draw_side_nav(img, draw, screen: Screen, breakpoint: str) -> int:
    if breakpoint != "desktop" or screen.nav == "auth":
        return 0
    sw = 220
    draw.rectangle([0, 0, sw, img.height], fill=C["chrome"])
    text(draw, (24, 28), "FCHIP", size=18, bold=True, fill=C["white"])
    text(draw, (24, 54), "Community Health\nIntelligence", size=11, fill=(160, 190, 194))
    y = 110
    for item in NAV.get(screen.nav, []):
        active = item.lower() in screen.title.lower() or item.lower() in screen.slug
        fill = C["accent"] if active else (32, 54, 60)
        round_rect(draw, (16, y, sw - 16, y + 40), fill, radius=10)
        text(draw, (28, y + 20), item, size=13, fill=C["white"], anchor="lm")
        y += 48
    text(draw, (24, img.height - 36), "Cascade Data & Feedback", size=10, fill=(120, 150, 155))
    return sw


def draw_bottom_nav(draw, w, h, screen: Screen, breakpoint: str):
    if breakpoint == "desktop" or screen.nav == "auth":
        return 0
    bh = 64
    y0 = h - bh
    draw.rectangle([0, y0, w, h], fill=C["surface"])
    draw.line([(0, y0), (w, y0)], fill=C["line"], width=1)
    items = NAV.get(screen.nav, [])
    if not items:
        return bh
    slot = w / len(items)
    for i, item in enumerate(items):
        cx = slot * i + slot / 2
        text(draw, (cx, y0 + 24), "●", size=10, fill=C["primary"] if i == 0 else C["muted"], anchor="mm")
        text(draw, (cx, y0 + 44), item, size=10, fill=C["ink"] if i == 0 else C["muted"], anchor="mm")
    return bh


def draw_chips(draw, x, y, chips, max_w):
    if not chips:
        return y
    cx = x
    for chip in chips:
        tw = draw.textlength(chip, font=font(11)) + 20
        if cx + tw > x + max_w:
            cx = x
            y += 30
        round_rect(draw, (cx, y, cx + tw, y + 24), C["primary_soft"], radius=12)
        text(draw, (cx + 10, y + 12), chip, size=11, fill=C["primary"], anchor="lm")
        cx += tw + 8
    return y + 36


def draw_stats(draw, x, y, stats, max_w, breakpoint: str):
    if not stats:
        return y
    cols = 2 if breakpoint == "mobile" else min(4, len(stats))
    gap = 10
    card_w = (max_w - gap * (cols - 1)) / cols
    card_h = 70
    for i, (label, value) in enumerate(stats):
        c = i % cols
        r = i // cols
        bx = x + c * (card_w + gap)
        by = y + r * (card_h + gap)
        round_rect(draw, (bx, by, bx + card_w, by + card_h), C["surface"], radius=14, outline=C["line"])
        text(draw, (bx + 14, by + 18), label, size=11, fill=C["muted"])
        text(draw, (bx + 14, by + 42), value, size=18, bold=True, fill=C["primary"])
    rows = math.ceil(len(stats) / cols)
    return y + rows * (card_h + gap) + 8


def draw_rows(draw, x, y, rows, max_w, bottom):
    for title, sub in rows:
        if y + 64 > bottom:
            break
        round_rect(draw, (x, y, x + max_w, y + 56), C["surface"], radius=14, outline=C["line"])
        text(draw, (x + 16, y + 18), title, size=13, bold=True)
        text(draw, (x + 16, y + 38), sub, size=11, fill=C["muted"])
        text(draw, (x + max_w - 16, y + 28), "›", size=18, fill=C["muted"], anchor="rm")
        y += 66
    return y


def draw_form(draw, x, y, rows, max_w, bottom):
    for label, value in rows:
        if y + 72 > bottom:
            break
        text(draw, (x + 4, y), label, size=11, fill=C["muted"])
        round_rect(draw, (x, y + 18, x + max_w, y + 58), C["surface"], radius=12, outline=C["line"])
        text(draw, (x + 14, y + 38), value, size=13, anchor="lm")
        y += 72
    return y


def draw_map(draw, x, y, max_w, max_h, note: str):
    round_rect(draw, (x, y, x + max_w, y + max_h), C["map"], radius=18)
    # simple hotspot blobs
    spots = [
        (0.28, 0.35, 28),
        (0.55, 0.42, 36),
        (0.42, 0.62, 22),
        (0.68, 0.28, 18),
    ]
    for fx, fy, r in spots:
        cx = x + max_w * fx
        cy = y + max_h * fy
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=C["map_hot"] + (0,))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(196, 92, 38, 180) if False else C["warn"])
        draw.ellipse([cx - r * 0.45, cy - r * 0.45, cx + r * 0.45, cy + r * 0.45], fill=C["white"])
    # legend
    round_rect(
        draw,
        (x + 12, y + max_h - 54, x + max_w - 12, y + max_h - 12),
        (255, 255, 255, 230) if False else C["surface"],
        radius=10,
    )
    text(draw, (x + 24, y + max_h - 33), note or "GIS · climate overlay", size=11, fill=C["ink"], anchor="lm")
    return y + max_h + 12


def draw_cta(draw, x, y, max_w, label: str):
    if not label:
        return y
    round_rect(draw, (x, y, x + max_w, y + 48), C["primary"], radius=14)
    text(draw, (x + max_w / 2, y + 24), label, size=14, bold=True, fill=C["white"], anchor="mm")
    return y + 60


def render_screen(screen: Screen, breakpoint: str) -> Image.Image:
    w, h = SIZES[breakpoint]
    img = Image.new("RGB", (w, h), C["bg"])
    draw = ImageDraw.Draw(img)

    left = draw_side_nav(img, draw, screen, breakpoint)
    top = draw_header(draw, w, h, screen, breakpoint, left)
    bottom_nav = draw_bottom_nav(draw, w, h, screen, breakpoint)
    content_bottom = h - bottom_nav - 16
    pad = 20 if breakpoint == "mobile" else 28
    x = left + pad
    max_w = w - left - pad * 2
    y = top + 18

    if screen.kind == "auth":
        # centered card
        card_w = min(420, max_w)
        card_x = left + (w - left - card_w) / 2
        y = top + (80 if breakpoint != "mobile" else 40)
        round_rect(draw, (card_x, y, card_x + card_w, y + 420), C["surface"], radius=20, outline=C["line"])
        text(draw, (card_x + card_w / 2, y + 48), screen.title, size=28, bold=True, fill=C["primary"], anchor="mm")
        text(draw, (card_x + card_w / 2, y + 84), screen.subtitle, size=13, fill=C["muted"], anchor="mm")
        if screen.note:
            for i, line in enumerate(wrap(draw, screen.note, int(card_w - 48), 12)):
                text(draw, (card_x + card_w / 2, y + 120 + i * 18), line, size=12, fill=C["ink"], anchor="mm")
        fy = y + 160
        if screen.rows:
            for label, value in screen.rows:
                text(draw, (card_x + 28, fy), label, size=11, fill=C["muted"])
                round_rect(
                    draw,
                    (card_x + 24, fy + 18, card_x + card_w - 24, fy + 56),
                    C["bg"],
                    radius=10,
                    outline=C["line"],
                )
                text(draw, (card_x + 36, fy + 37), value, size=13, anchor="lm")
                fy += 70
        elif screen.kind == "auth" and screen.slug == "splash":
            round_rect(
                draw,
                (card_x + 40, y + 150, card_x + card_w - 40, y + 260),
                C["primary_soft"],
                radius=16,
            )
            text(
                draw,
                (card_x + card_w / 2, y + 205),
                "CAPTURE → FUSE → PREDICT\nALERT → ACT → LEARN",
                size=12,
                fill=C["primary"],
                anchor="mm",
            )
            fy = y + 290
        draw_cta(draw, card_x + 24, min(fy + 10, y + 350), card_w - 48, screen.primary_cta or "Continue")
        text(
            draw,
            (card_x + card_w / 2, y + 400),
            "Obulamu eri Bonna",
            size=11,
            fill=C["muted"],
            anchor="mm",
        )
        return img

    # title block (mobile/tablet; desktop uses header title)
    if breakpoint != "desktop":
        text(draw, (x, y), screen.title, size=22, bold=True)
        y += 28
        text(draw, (x, y), screen.subtitle, size=12, fill=C["muted"])
        y += 28
    else:
        text(draw, (x, y), screen.subtitle, size=13, fill=C["muted"])
        y += 26

    y = draw_chips(draw, x, y, screen.chips, max_w)
    y = draw_stats(draw, x, y, screen.stats, max_w, breakpoint)

    if screen.kind == "map":
        map_h = min(360, content_bottom - y - 80)
        y = draw_map(draw, x, y, max_w, map_h, screen.note)
    elif screen.kind == "form":
        y = draw_form(draw, x, y, screen.rows, max_w, content_bottom - 70)
    elif screen.kind in {"list", "queue", "dashboard", "detail", "settings"}:
        # dual column on desktop for dashboard/list
        if breakpoint == "desktop" and screen.kind in {"dashboard", "list", "queue"} and len(screen.rows) >= 3:
            col_w = (max_w - 16) / 2
            y1 = draw_rows(draw, x, y, screen.rows[::2], col_w, content_bottom - 70)
            y2 = draw_rows(draw, x + col_w + 16, y, screen.rows[1::2], col_w, content_bottom - 70)
            y = max(y1, y2)
        else:
            y = draw_rows(draw, x, y, screen.rows, max_w, content_bottom - 70)
        if screen.kind == "detail" and screen.note:
            for line in wrap(draw, screen.note, int(max_w), 12):
                if y + 20 > content_bottom - 70:
                    break
                text(draw, (x, y), line, size=12, fill=C["muted"])
                y += 18

    if screen.note and screen.kind != "map" and screen.kind != "detail":
        y += 4
        round_rect(draw, (x, y, x + max_w, y + 44), C["warn_soft"], radius=12)
        note_lines = wrap(draw, screen.note, int(max_w - 24), 11)
        text(draw, (x + 12, y + 22), note_lines[0], size=11, fill=C["warn"], anchor="lm")
        y += 56

    if screen.primary_cta:
        draw_cta(draw, x, min(y + 8, content_bottom - 56), max_w, screen.primary_cta)

    # footer tag
    text(
        draw,
        (x, h - bottom_nav - 8 if bottom_nav else h - 10),
        f"{screen.module}/{screen.slug} · {breakpoint}",
        size=9,
        fill=C["muted"],
        anchor="lb",
    )
    return img


def write_module_readme(module: str, screens: list[Screen]):
    mod_dir = ROOT / module
    mod_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {module}",
        "",
        "Source: `app-flows/04-modules.md` + `.cursor/app-write-up.mdc`.",
        "",
        "| Screen | Mobile | Tablet | Desktop |",
        "| --- | --- | --- | --- |",
    ]
    for s in screens:
        lines.append(
            f"| {s.title} (`{s.slug}`) | [mobile]({s.slug}/mobile.png) | "
            f"[tablet]({s.slug}/tablet.png) | [desktop]({s.slug}/desktop.png) |"
        )
    (mod_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    by_module: dict[str, list[Screen]] = {}
    for screen in SCREENS:
        by_module.setdefault(screen.module, []).append(screen)
        out_dir = ROOT / screen.module / screen.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        meta = {
            "title": screen.title,
            "subtitle": screen.subtitle,
            "kind": screen.kind,
            "nav": screen.nav,
            "source": "app-flows + .cursor/app-write-up.mdc",
        }
        (out_dir / "screen.json").write_text(
            "{\n"
            + ",\n".join(f'  "{k}": "{v}"' for k, v in meta.items())
            + "\n}\n",
            encoding="utf-8",
        )
        for bp in SIZES:
            img = render_screen(screen, bp)
            img.save(out_dir / f"{bp}.png", optimize=True)

    for module, screens in by_module.items():
        write_module_readme(module, screens)

    # root index
    total = len(SCREENS) * 3
    lines = [
        "# FCHIP app-ui",
        "",
        "Visual directory of **proposed** FCHIP screens from `.cursor/app-write-up.mdc` and `app-flows/`.",
        "Not generated from `frontend/` code.",
        "",
        f"**{len(SCREENS)} screens** × mobile / tablet / desktop = **{total} mockups**.",
        "",
        "Slogan: **Your health, our mission.**",
        "",
        "## Breakpoints",
        "",
        "| Name | Size |",
        "| --- | --- |",
        "| mobile | 390 × 844 |",
        "| tablet | 768 × 1024 |",
        "| desktop | 1440 × 900 |",
        "",
        "## Modules",
        "",
    ]
    for module, screens in by_module.items():
        lines.append(f"### [{module}]({module}/README.md)")
        lines.append("")
        for s in screens:
            lines.append(
                f"- **{s.title}** — `{module}/{s.slug}/` "
                f"([mobile]({module}/{s.slug}/mobile.png) · "
                f"[tablet]({module}/{s.slug}/tablet.png) · "
                f"[desktop]({module}/{s.slug}/desktop.png))"
            )
        lines.append("")
    lines += [
        "## Regenerate",
        "",
        "```bash",
        "python app-ui/generate_mockups.py",
        "```",
        "",
        "## Sources",
        "",
        "- `.cursor/app-write-up.mdc`",
        "- `app-flows/01-overview.md` … `06-mvp-phases.md` (especially `04-modules.md`)",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(SCREENS)} screens × 3 breakpoints = {total} PNGs under {ROOT}")


if __name__ == "__main__":
    main()
