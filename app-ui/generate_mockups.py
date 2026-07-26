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
        "Consumers · data feeders · admin",
        "list",
        rows=[
            ("CHW / VHT mobile", "Worklists · visits · alerts"),
            ("Facility dashboard", "Trends · referrals · maps"),
            ("District / MoH console", "Early warning · M&E"),
            ("NGO / partner M&E", "Programme impact"),
            ("School health feed", "Sessions · screening · absenteeism"),
            ("Pharmacy outlet feed", "Stock · dispense · complaints"),
            ("Lab / PoC feed", "RDT · Hb · glucose results"),
            ("Admin", "Org · consent · feeder access"),
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
    Screen(
        "02-community-caregiver",
        "household-needs-capture",
        "Household needs",
        "Community members feed priorities into cascade",
        "form",
        rows=[
            ("Priority theme", "Preventive health"),
            ("Detail", "More immunisation outreach"),
            ("Who is affected", "Children under 5"),
            ("Consent to share", "Yes · with CHW"),
        ],
        primary_cta="Submit needs signal",
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
    Screen(
        "03-outreach-school-health",
        "screening-results-entry",
        "Screening results entry",
        "Outreach teams feed camp outcomes into ingest",
        "form",
        rows=[
            ("Campaign", "Malaria screening · Bukoto"),
            ("People screened", "124"),
            ("Positive / referred", "11"),
            ("Common findings", "Fever · anaemia proxies"),
            ("Offline queue", "Ready to sync"),
        ],
        primary_cta="Queue to ingest",
        nav="field",
    ),
    Screen(
        "03-outreach-school-health",
        "home-visit-batch-upload",
        "Home-visit batch",
        "Supervisors upload structured visit packs",
        "form",
        rows=[
            ("Batch file", "visits_2026-07-26.csv"),
            ("Records", "48"),
            ("Validation", "2 warnings"),
            ("Catchment", "Kyebando"),
        ],
        primary_cta="Upload batch",
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
    Screen(
        "06-facility-dashboard",
        "clinical-share-confirm",
        "Clinical share confirm",
        "Facility staff approve what leaves EMR into FCHIP",
        "form",
        rows=[
            ("Encounter pack", "Today · 36 records"),
            ("Scopes included", "Vitals · diagnoses · completed referrals"),
            ("Consent check", "Passed"),
            ("Destination", "FCHIP ingest · least privilege"),
        ],
        note="FCHIP does not replace the facility EMR/HMS",
        primary_cta="Push to FCHIP",
        nav="facility",
    ),
    Screen(
        "06-facility-dashboard",
        "manual-case-signal",
        "Manual case signal",
        "When EMR link is down — structured facility feed",
        "form",
        rows=[
            ("Signal type", "Fever caseload uptick"),
            ("Count (today)", "14"),
            ("Age group", "Under 15"),
            ("Catchment link", "Bukoto villages"),
        ],
        primary_cta="Send signal",
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
    Screen(
        "07-referrals-desk",
        "outcome-feed-back",
        "Outcome feed-back",
        "Completed referral outcomes return into cascade metrics",
        "form",
        rows=[
            ("Referral ID", "REF-9021"),
            ("Clinical outcome", "Stabilised · ANC plan"),
            ("EMR encounter ID", "EMR-44102"),
            ("Feed to metrics", "Yes"),
        ],
        primary_cta="Sync outcome",
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
    Screen(
        "08-emr-connector",
        "push-event-log",
        "Push event log",
        "EMR/HMS systems feeding FCHIP in real time",
        "list",
        chips=["Live"],
        rows=[
            ("Clinic A · encounters", "36 records · OK"),
            ("Centre B · vitals batch", "120 records · OK"),
            ("Hospital C · test ping", "Auth OK · scopes pending"),
        ],
        primary_cta="Download audit CSV",
        nav="admin",
    ),
    Screen(
        "08-emr-connector",
        "facility-onboarding",
        "Facility onboarding",
        "Register an existing EMR/HMS as a data feeder",
        "form",
        rows=[
            ("Facility name", "Partner medical centre"),
            ("EMR / HMS vendor", "Existing system"),
            ("Auth method", "Client credentials"),
            ("Catchment link", "Kamwokya"),
        ],
        primary_cta="Issue feeder credentials",
        nav="admin",
    ),
    # 09 intelligence
    Screen(
        "09-intelligence",
        "ingest-pipeline",
        "Ingest & sync",
        "All feeder parties → validate → store",
        "dashboard",
        stats=[("Sources live", "15"), ("Lag", "48s"), ("Validate fails", "0.2%")],
        rows=[
            ("CHW / caregiver / community", "Streaming"),
            ("Schools · pharmacy · lab · MCH", "Daily + live"),
            ("Corporate · NCD · HMIS", "Scheduled"),
            ("EMR APIs · climate API", "Real-time"),
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
    Screen(
        "09-intelligence",
        "feeder-health-board",
        "Feeder health board",
        "Which data parties are sending clean signals",
        "dashboard",
        stats=[("Healthy", "12"), ("Degraded", "2"), ("Silent", "1")],
        rows=[
            ("Pharmacy · Kisaasi", "Stock lag 6h"),
            ("School · Kikaaya P.S.", "Session overdue"),
            ("Climate API", "Healthy"),
        ],
        primary_cta="Open silent feeders",
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
    Screen(
        "11-ngo-partner",
        "field-dataset-upload",
        "Field dataset upload",
        "NGO M&E teams feed anonymised programme data",
        "form",
        rows=[
            ("Programme", "Maternal outreach 2026"),
            ("File", "me_indicators_july.csv"),
            ("Grain", "Parish aggregates"),
            ("PHI check", "Blocked if identifiers found"),
        ],
        primary_cta="Upload to ingest",
        nav="partner",
    ),
    Screen(
        "11-ngo-partner",
        "partner-indicator-entry",
        "Partner indicator entry",
        "Manual M&E indicators where APIs are absent",
        "form",
        rows=[
            ("Indicator", "Education sessions held"),
            ("Period", "July 2026"),
            ("Value", "9"),
            ("Catchment", "Bukoto"),
        ],
        primary_cta="Submit indicator",
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
    Screen(
        "12-research-exports",
        "research-contribution-upload",
        "Research contribution upload",
        "Academic partners feed approved anonymised field sets",
        "form",
        rows=[
            ("Study", "School wellness cohort B"),
            ("Dataset type", "De-identified vitals"),
            ("Ethics ID", "REC-2026-118"),
            ("Reuse licence", "FCHIP cascade learning only"),
        ],
        primary_cta="Contribute dataset",
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
        "Consumers and data-feeder roles",
        "settings",
        rows=[
            ("CHW / VHT · caregiver", "Field / household capture"),
            ("School · pharmacy · lab · MCH", "Feeder capture modules"),
            ("Corporate · NCD cohort", "Wellness / chronic feeds"),
            ("Facility · EMR operator", "Clinical share · referrals"),
            ("District · NGO · research · admin", "Console · consent · APIs"),
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
    Screen(
        "13-admin-consent",
        "feeder-party-registry",
        "Feeder party registry",
        "Register every source that may push into ingest",
        "settings",
        rows=[
            ("Schools", "4 active"),
            ("Pharmacies", "6 active"),
            ("Labs / PoC", "3 active"),
            ("MCH posts · corporate · NCD", "Onboarded"),
            ("HMIS / DHIS2 · climate", "Approved where linked"),
        ],
        primary_cta="Add feeder party",
        nav="admin",
    ),
    # --- Data feeder parties (SoT §4.2 / app-flows 03) ---
    Screen(
        "14-schools-health",
        "school-home",
        "School health home",
        "Schools feed sessions · screening · absenteeism",
        "dashboard",
        stats=[("Sessions", "3"), ("Screened", "86"), ("Flags", "4")],
        rows=[
            ("Next health day", "Friday · Kisaasi P.S."),
            ("Pending sync", "2 session logs"),
            ("Open flags", "Absenteeism + fever"),
        ],
        primary_cta="Log today’s session",
        nav="school",
    ),
    Screen(
        "14-schools-health",
        "health-education-session",
        "Health education session",
        "School / community education metrics",
        "form",
        rows=[
            ("School", "Kikaaya Primary"),
            ("Topic", "Handwashing · diarrhoea prevention"),
            ("Learners reached", "210"),
            ("Teachers present", "8"),
        ],
        primary_cta="Save to cascade metrics",
        nav="school",
    ),
    Screen(
        "14-schools-health",
        "learner-screening-entry",
        "Learner screening entry",
        "School screening camp results → ingest",
        "form",
        rows=[
            ("Screen type", "Vision · nutrition · fever check"),
            ("Learners screened", "64"),
            ("Referred to CHW/facility", "7"),
            ("Consent on file", "Yes"),
        ],
        primary_cta="Submit screening pack",
        nav="school",
    ),
    Screen(
        "14-schools-health",
        "absenteeism-wellness",
        "Absenteeism & wellness",
        "Wellness signals from school rolls",
        "form",
        rows=[
            ("Week", "2026-W30"),
            ("Absent (illness)", "18"),
            ("Fever / diarrhoea noted", "6"),
            ("Link to parish", "Kikaaya"),
        ],
        primary_cta="Send wellness signal",
        nav="school",
    ),
    Screen(
        "14-schools-health",
        "school-sync-status",
        "School sync status",
        "Offline school forms → cloud",
        "detail",
        stats=[("Queued", "2"), ("Last sync", "11:04"), ("Errors", "0")],
        rows=[
            ("Session logs", "1 pending"),
            ("Screening pack", "1 pending"),
        ],
        primary_cta="Sync now",
        nav="school",
    ),
    Screen(
        "15-pharmacy-outlets",
        "pharmacy-home",
        "Pharmacy outlet home",
        "Drug shops feed stock · dispense · complaints",
        "dashboard",
        stats=[("Stock SKUs", "42"), ("Dispenses today", "31"), ("Complaints", "5")],
        rows=[
            ("ACT on hand", "Low · 2 days cover"),
            ("Top complaint", "Fever · headache"),
            ("Demand hint", "Rainfall-linked uptick"),
        ],
        primary_cta="Update stock",
        nav="pharmacy",
    ),
    Screen(
        "15-pharmacy-outlets",
        "stock-levels-entry",
        "Stock levels entry",
        "Medicine availability signals for demand forecasts",
        "form",
        rows=[
            ("Outlet", "Kamwokya drug shop"),
            ("ACT strips", "18"),
            ("ORS sachets", "40"),
            ("RDT kits", "12"),
            ("ANC supplements", "25"),
        ],
        primary_cta="Push stock snapshot",
        nav="pharmacy",
    ),
    Screen(
        "15-pharmacy-outlets",
        "dispense-log",
        "Dispense log",
        "Dispensing patterns into multi-source ingest",
        "form",
        rows=[
            ("Item", "ACT"),
            ("Quantity", "6"),
            ("Complaint linked", "Fever"),
            ("Age band", "5–14"),
        ],
        primary_cta="Log dispense",
        nav="pharmacy",
    ),
    Screen(
        "15-pharmacy-outlets",
        "common-complaints",
        "Common complaints",
        "Community symptom patterns from outlets",
        "list",
        rows=[
            ("Fever", "12 this week"),
            ("Cough", "8 this week"),
            ("Diarrhoea", "5 this week"),
            ("BP check request", "4 this week"),
        ],
        primary_cta="Submit weekly rollup",
        nav="pharmacy",
    ),
    Screen(
        "15-pharmacy-outlets",
        "prestock-ack",
        "Pre-stock acknowledgement",
        "Respond to district medicine demand actions",
        "form",
        rows=[
            ("Alert", "ACT demand +28% · 14 days"),
            ("Received shipment", "Yes · 40 strips"),
            ("Ready for surge", "Yes"),
        ],
        primary_cta="Confirm to district",
        nav="pharmacy",
    ),
    Screen(
        "16-labs-poc",
        "lab-home",
        "Lab / PoC home",
        "Labs feed RDT · Hb · glucose and related results",
        "dashboard",
        stats=[("Today", "27"), ("Pending sync", "3"), ("Flags", "2")],
        rows=[
            ("Malaria RDT+", "4"),
            ("Low Hb proxies", "2"),
            ("Glucose elevated", "1"),
        ],
        primary_cta="Enter result",
        nav="lab",
    ),
    Screen(
        "16-labs-poc",
        "result-entry",
        "Result entry",
        "Point-of-care / lab result → ingest",
        "form",
        rows=[
            ("Test", "Malaria RDT"),
            ("Result", "Positive"),
            ("Site", "Outreach camp · Bukoto"),
            ("Link household / referral", "HH-1190"),
            ("Consent", "Recorded"),
        ],
        primary_cta="Submit result",
        nav="lab",
    ),
    Screen(
        "16-labs-poc",
        "batch-results-upload",
        "Batch results upload",
        "Facility lab batches into FCHIP",
        "form",
        rows=[
            ("Batch file", "poc_results_26jul.csv"),
            ("Tests", "Malaria · Hb · glucose"),
            ("Records", "88"),
            ("Validation", "Clean"),
        ],
        primary_cta="Upload batch",
        nav="lab",
    ),
    Screen(
        "16-labs-poc",
        "result-queue",
        "Result queue",
        "Results waiting to sync or link to referrals",
        "queue",
        chips=["3 pending"],
        rows=[
            ("RDT+ · HH-1190", "Needs CHW follow-up"),
            ("Hb low · ANC", "Link maternal alert"),
            ("Glucose high · NCD", "Cohort follow-up"),
        ],
        primary_cta="Sync queue",
        nav="lab",
    ),
    Screen(
        "17-corporate-wellness",
        "corporate-home",
        "Corporate wellness home",
        "Workplace programmes feed BP · BMI · glucose",
        "dashboard",
        stats=[("Camps", "2"), ("Checked", "140"), ("High BP", "19")],
        rows=[
            ("This week camp", "Partner office · Kampala"),
            ("Top signal", "Hypertension hotspot"),
            ("Follow-ups queued", "11"),
        ],
        primary_cta="Start camp entry",
        nav="corporate",
    ),
    Screen(
        "17-corporate-wellness",
        "camp-vitals-entry",
        "Camp vitals entry",
        "BP · BMI · glucose from corporate / school wellness",
        "form",
        rows=[
            ("Participant code", "CW-204"),
            ("Blood pressure", "148 / 92"),
            ("BMI", "28.1"),
            ("Glucose", "6.4"),
            ("Consent", "Yes"),
        ],
        primary_cta="Save vitals",
        nav="corporate",
    ),
    Screen(
        "17-corporate-wellness",
        "camp-summary-push",
        "Camp summary push",
        "Aggregate wellness signals to NCD intelligence",
        "form",
        rows=[
            ("Camp", "July workplace screening"),
            ("Participants", "140"),
            ("Elevated BP", "19"),
            ("Referred", "11"),
        ],
        primary_cta="Push summary to ingest",
        nav="corporate",
    ),
    Screen(
        "17-corporate-wellness",
        "occupational-flags",
        "Occupational flags",
        "Workplace health risk patterns",
        "list",
        rows=[
            ("BP cluster · Site A", "Above baseline"),
            ("BMI rising · Site B", "Watch"),
            ("Heat strain week", "Climate-linked"),
        ],
        nav="corporate",
    ),
    Screen(
        "18-mch-touchpoints",
        "mch-home",
        "MCH touchpoints home",
        "ANC / PNC · immunisation · nutrition posts feed care signals",
        "dashboard",
        stats=[("ANC today", "16"), ("PNC", "7"), ("Imm doses", "22")],
        rows=[
            ("Missed ANC list", "5 mothers"),
            ("Nutrition flags", "3 children"),
            ("Heat advisory", "Share with visits"),
        ],
        primary_cta="Open ANC register",
        nav="mch",
    ),
    Screen(
        "18-mch-touchpoints",
        "anc-visit-entry",
        "ANC visit entry",
        "Antenatal touchpoint → maternal intelligence",
        "form",
        rows=[
            ("Mother ID", "MCH-881"),
            ("Gestation week", "28"),
            ("BP / Hb proxy", "132/84 · anaemia watch"),
            ("Next appointment", "In 2 weeks"),
        ],
        primary_cta="Save ANC visit",
        nav="mch",
    ),
    Screen(
        "18-mch-touchpoints",
        "pnc-visit-entry",
        "PNC visit entry",
        "Postnatal follow-up signals",
        "form",
        rows=[
            ("Mother / newborn", "MCH-774"),
            ("Day post-birth", "7"),
            ("Danger signs", "None"),
            ("Feeding support", "Yes"),
        ],
        primary_cta="Save PNC visit",
        nav="mch",
    ),
    Screen(
        "18-mch-touchpoints",
        "immunisation-entry",
        "Immunisation entry",
        "Immunisation post doses → child health coverage",
        "form",
        rows=[
            ("Child ID", "CH-552"),
            ("Antigen", "Measles"),
            ("Dose date", "2026-07-26"),
            ("Catchment", "Kyebando"),
        ],
        primary_cta="Record dose",
        nav="mch",
    ),
    Screen(
        "18-mch-touchpoints",
        "nutrition-monitoring",
        "Nutrition monitoring",
        "Growth / nutrition programme feed",
        "form",
        rows=[
            ("Child ID", "CH-310"),
            ("MUAC / growth", "At risk"),
            ("Diarrhoea recent", "Yes"),
            ("Support given", "Counselling · follow-up"),
        ],
        primary_cta="Submit nutrition flag",
        nav="mch",
    ),
    Screen(
        "19-ncd-gericare",
        "cohort-home",
        "NCD / Gericare home",
        "Chronic and elderly cohorts feed longitudinal signals",
        "dashboard",
        stats=[("Cohort", "186"), ("Due visits", "24"), ("High risk", "9")],
        rows=[
            ("Hypertension due", "14"),
            ("Diabetes due", "7"),
            ("Elderly home checks", "3"),
        ],
        primary_cta="Start cohort visit",
        nav="ncd",
    ),
    Screen(
        "19-ncd-gericare",
        "cohort-visit-entry",
        "Cohort visit entry",
        "Hypertension · diabetes · elderly care checks",
        "form",
        rows=[
            ("Member ID", "NCD-044"),
            ("BP", "156 / 98"),
            ("Glucose", "9.1"),
            ("Med adherence", "Partial"),
            ("Home / clinic", "Home visit"),
        ],
        primary_cta="Save cohort visit",
        nav="ncd",
    ),
    Screen(
        "19-ncd-gericare",
        "bp-screening-batch",
        "BP screening batch",
        "Community/clinic BP packs for hotspot detection",
        "form",
        rows=[
            ("Site", "Parish screening · Kamwokya"),
            ("Readings", "92"),
            ("Elevated", "21"),
            ("Referred", "12"),
        ],
        primary_cta="Push BP batch",
        nav="ncd",
    ),
    Screen(
        "19-ncd-gericare",
        "stroke-risk-flags",
        "Stroke / NCD risk flags",
        "Signals that feed NCD predictions",
        "list",
        rows=[
            ("Member NCD-044", "BP rising · 3 visits"),
            ("Parish 3 hotspot", "Hypertension density up"),
            ("Elderly cluster", "Missed follow-ups"),
        ],
        nav="ncd",
    ),
    Screen(
        "20-hmis-dhis2",
        "hmis-home",
        "HMIS / DHIS2 home",
        "Approved public-health aggregates into FCHIP",
        "dashboard",
        stats=[("Last pull", "06:00"), ("Datasets", "5"), ("Gaps", "1")],
        rows=[
            ("OPD fever aggregates", "Synced"),
            ("Immunisation coverage", "Synced"),
            ("Maternal indicators", "Mapping needed"),
        ],
        note="Only where integration is approved",
        primary_cta="Run sync",
        nav="hmis",
    ),
    Screen(
        "20-hmis-dhis2",
        "dataset-mapping",
        "Dataset mapping",
        "Map HMIS/DHIS2 elements to cascade indicators",
        "settings",
        rows=[
            ("Fever OPD", "→ Surveillance signal"),
            ("ANC1 / ANC4", "→ Maternal adherence"),
            ("Penta3 coverage", "→ Child immunisation"),
            ("Stock-out forms", "→ Medicine demand"),
        ],
        primary_cta="Save mapping",
        nav="hmis",
    ),
    Screen(
        "20-hmis-dhis2",
        "aggregate-push-pull",
        "Aggregate push / pull",
        "Scheduled exchange with district HMIS",
        "form",
        rows=[
            ("Direction", "Pull into FCHIP"),
            ("Period", "July 2026"),
            ("Org units", "Pilot catchments"),
            ("Approval", "District signed"),
        ],
        primary_cta="Execute exchange",
        nav="hmis",
    ),
    Screen(
        "20-hmis-dhis2",
        "hmis-audit",
        "HMIS audit",
        "What public aggregates entered the pipeline",
        "list",
        rows=[
            ("06:00 pull", "5 datasets · OK"),
            ("Mapping warning", "1 unmapped element"),
            ("Rejected row", "0 PHI violations"),
        ],
        nav="hmis",
    ),
    Screen(
        "21-community-events",
        "events-home",
        "Community events home",
        "Churches · mosques · dialogues feed community signals",
        "dashboard",
        stats=[("Events", "6"), ("Reach", "420"), ("Needs logged", "18")],
        rows=[
            ("Health dialogue · Bukoto", "Saturday"),
            ("Mosque wellness talk", "Logged"),
            ("Open needs", "Water · fever concern"),
        ],
        primary_cta="Log event",
        nav="community",
    ),
    Screen(
        "21-community-events",
        "outreach-event-log",
        "Outreach event log",
        "Community outreach events → ingest",
        "form",
        rows=[
            ("Venue", "Church hall · Kyebando"),
            ("Theme", "Maternal danger signs"),
            ("Attendance", "85"),
            ("Referrals / CHW links", "6"),
        ],
        primary_cta="Save event",
        nav="community",
    ),
    Screen(
        "21-community-events",
        "community-dialogue",
        "Community dialogue",
        "Needs & priorities from community conversations",
        "form",
        rows=[
            ("Parish", "Kisaasi"),
            ("Priority raised", "More child immunisation days"),
            ("Vulnerable groups noted", "Mothers · urban poor"),
            ("Follow-up owner", "CHW supervisor"),
        ],
        primary_cta="Submit dialogue notes",
        nav="community",
    ),
    Screen(
        "21-community-events",
        "participation-register",
        "Participation register",
        "Who engaged — cascade participation signal",
        "list",
        rows=[
            ("Health day · Kamwokya", "112 participants"),
            ("Dialogue · Bukoto", "64 participants"),
            ("Mosque session", "40 participants"),
        ],
        primary_cta="Export register",
        nav="community",
    ),
    Screen(
        "22-climate-feeds",
        "climate-home",
        "Climate feeds home",
        "Climate API as a first-class data feeder",
        "dashboard",
        stats=[("Rain 7d", "High"), ("Heat", "Moderate"), ("Extremes", "1 watch")],
        rows=[
            ("Provider status", "Healthy"),
            ("Last ingest", "12 min ago"),
            ("Fusion jobs", "3 running"),
        ],
        primary_cta="Refresh feeds",
        nav="climate",
    ),
    Screen(
        "22-climate-feeds",
        "rainfall-temperature",
        "Rainfall & temperature",
        "Weather signals fused with health",
        "detail",
        stats=[("Rain mm", "68"), ("Max °C", "31"), ("Humidity", "82%")],
        rows=[
            ("Catchments covered", "5 peri-urban"),
            ("Anomaly", "Above-normal rainfall"),
            ("Health link", "Malaria / fever watch"),
        ],
        nav="climate",
    ),
    Screen(
        "22-climate-feeds",
        "extremes-flood-heat",
        "Extremes · flood · heat",
        "Short-term climate risks for early warning",
        "list",
        rows=[
            ("Heat advisory", "Maternal strain risk"),
            ("Flood watch", "Diarrhoea sanitation risk"),
            ("No cyclone signal", "Clear"),
        ],
        nav="climate",
    ),
    Screen(
        "22-climate-feeds",
        "feed-config-audit",
        "Feed config & audit",
        "Which climate feeds may enter the pipeline",
        "settings",
        rows=[
            ("Rainfall", "Enabled"),
            ("Temperature / heat", "Enabled"),
            ("Flood proxies", "Enabled"),
            ("Retention", "Programme policy"),
        ],
        primary_cta="Save feed config",
        nav="climate",
    ),
    # CHIS feeder extras (optional domain already module 05)
    Screen(
        "05-chis-livelihoods",
        "iga-participation-entry",
        "IGA participation entry",
        "Livelihood groups feed participation where tracked",
        "form",
        rows=[
            ("Group", "Savings · Kamwokya"),
            ("Households active", "22"),
            ("Health access link", "CHIS co-pay support"),
            ("Period", "July 2026"),
        ],
        primary_cta="Submit IGA signal",
        nav="partner",
    ),
]


NAV = {
    "auth": [],
    "field": ["Worklist", "Alerts", "Sync", "More"],
    "facility": ["Overview", "Map", "Referrals", "Stock"],
    "district": ["Map", "Warnings", "Metrics", "Plan"],
    "partner": ["Monitor", "Evidence", "Reports", "More"],
    "admin": ["Org", "Users", "Consent", "APIs"],
    "school": ["Home", "Session", "Screen", "Sync"],
    "pharmacy": ["Stock", "Dispense", "Complaints", "Sync"],
    "lab": ["Home", "Results", "Queue", "Sync"],
    "corporate": ["Home", "Vitals", "Summary", "Flags"],
    "mch": ["Home", "ANC", "Immunise", "Nutrition"],
    "ncd": ["Home", "Visit", "BP", "Flags"],
    "hmis": ["Home", "Map", "Exchange", "Audit"],
    "community": ["Home", "Events", "Dialogue", "Register"],
    "climate": ["Home", "Rain", "Extremes", "Config"],
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
        "## Data feeders covered (SoT §4.2 / app-flows 03)",
        "",
        "| Feeder party | Module folder |",
        "| --- | --- |",
        "| CHWs / VHTs | `01-chw-vht-mobile` |",
        "| Patients / caregivers | `02-community-caregiver` |",
        "| Communities · events · dialogues | `21-community-events` (+ needs in `02`) |",
        "| Outreach programmes | `03-outreach-school-health` |",
        "| Schools | `14-schools-health` |",
        "| Hospitals / clinics (manual + share) | `06-facility-dashboard` · `07-referrals-desk` |",
        "| Existing EMR / HMS | `08-emr-connector` |",
        "| Pharmacies / drug shops | `15-pharmacy-outlets` |",
        "| ANC / PNC · immunisation · nutrition | `18-mch-touchpoints` |",
        "| Corporate / workplace wellness | `17-corporate-wellness` |",
        "| Labs / PoC | `16-labs-poc` |",
        "| Gericare / NCD cohorts | `19-ncd-gericare` |",
        "| CHIS / livelihoods (optional) | `05-chis-livelihoods` |",
        "| HMIS / DHIS2 (where approved) | `20-hmis-dhis2` |",
        "| Research / NGO M&E uploads | `11-ngo-partner` · `12-research-exports` |",
        "| Climate API | `22-climate-feeds` (+ fusion in `09`) |",
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
        "# screens + shared kit (components + layouts)",
        "```",
        "",
        "## Shared kit (`00-shared`)",
        "",
        "- [Components](00-shared/components/README.md) — reusable UI pieces",
        "- [Layouts](00-shared/layouts/README.md) — page shells for every surface / feeder",
        "",
        "## Sources",
        "",
        "- `.cursor/app-write-up.mdc`",
        "- `app-flows/01-overview.md` … `06-mvp-phases.md` (especially `04-modules.md`)",
        "",
    ]
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(SCREENS)} screens × 3 breakpoints = {total} PNGs under {ROOT}")

    # Shared reusable kit (components + layouts) under 00-shared/
    import runpy

    kit = ROOT / "00-shared" / "generate_kit.py"
    if kit.exists():
        runpy.run_path(str(kit), run_name="__main__")


if __name__ == "__main__":
    main()
