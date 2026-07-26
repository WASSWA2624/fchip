# Shared layouts

Page shells for maximum reuse across consumer surfaces and data-feeder modules.
Pick a layout, then drop in shared components.

**17 layouts** × mobile / tablet / desktop × light / dark.
Dark specimens use the same filename with `-dark` before `.png`.

| Layout | Purpose | Composes | Specimens |
| --- | --- | --- | --- |
| **Auth centered card** (`01-auth-centered-card`) | Create account / sign in — phone number + password only | `01-logo-lockup`, `02-slogan-line`, `01-labeled-field`, `01-primary-cta`, … | [m](01-auth-centered-card/mobile.png) · [t](01-auth-centered-card/tablet.png) · [d](01-auth-centered-card/desktop.png) |
| **Field mobile shell** (`04-field-mobile-shell`) | CHW / caregiver / feeder capture on phone | `01-top-app-bar`, `09-section-header`, `02-bottom-nav-field`, `01-status-chip`, … | [m](04-field-mobile-shell/mobile.png) · [t](04-field-mobile-shell/tablet.png) · [d](04-field-mobile-shell/desktop.png) |
| **Field tablet shell** (`05-field-tablet-shell`) | Adaptive field IA with a compact navigation rail and wider content column | `01-top-app-bar`, `07-side-nav-desktop`, `09-section-header`, `02-stat-card-row`, … | [m](05-field-tablet-shell/mobile.png) · [t](05-field-tablet-shell/tablet.png) · [d](05-field-tablet-shell/desktop.png) |
| **Desktop sidebar shell** (`06-desktop-sidebar-shell`) | Facility · district · admin · feeder desktop chrome | `07-side-nav-desktop`, `01-top-app-bar`, `04-cascade-footer` | [m](06-desktop-sidebar-shell/mobile.png) · [t](06-desktop-sidebar-shell/tablet.png) · [d](06-desktop-sidebar-shell/desktop.png) |
| **Dashboard metrics** (`11-dashboard-metrics`) | Overview with stats + list + CTA | `02-stat-card-row`, `03-list-row-card`, `02-filter-chip-row`, `01-primary-cta` | [m](11-dashboard-metrics/mobile.png) · [t](11-dashboard-metrics/tablet.png) · [d](11-dashboard-metrics/desktop.png) |
| **Form capture** (`09-form-capture`) | Structured offline / online data entry | `09-section-header`, `02-form-stack`, `03-consent-toggle`, `01-primary-cta`, … | [m](09-form-capture/mobile.png) · [t](09-form-capture/tablet.png) · [d](09-form-capture/desktop.png) |
| **List / worklist** (`02-list-worklist`) | Today’s tasks, alerts, notifications | `09-section-header`, `01-status-chip`, `03-list-row-card`, `01-primary-cta`, … | [m](02-list-worklist/mobile.png) · [t](02-list-worklist/tablet.png) · [d](02-list-worklist/desktop.png) |
| **Queue desk** (`14-queue-desk`) | Referral / lab / result queues | `02-filter-chip-row`, `02-queue-item`, `01-primary-cta`, `02-sync-status-strip` | [m](14-queue-desk/mobile.png) · [t](14-queue-desk/tablet.png) · [d](14-queue-desk/desktop.png) |
| **Map explorer** (`13-map-explorer`) | GIS hotspot + climate legend | `02-filter-chip-row`, `01-hotspot-map`, `09-section-header` | [m](13-map-explorer/mobile.png) · [t](13-map-explorer/tablet.png) · [d](13-map-explorer/desktop.png) |
| **Detail + action** (`10-detail-action`) | Explainable alert / referral detail with CTA | `02-stat-card-row`, `06-explainability-block`, `03-list-row-card`, `01-primary-cta`, … | [m](10-detail-action/mobile.png) · [t](10-detail-action/tablet.png) · [d](10-detail-action/desktop.png) |
| **Settings / admin** (`08-settings-admin`) | Org · roles · consent · API scopes · feeder registry | `09-section-header`, `03-list-row-card`, `04-note-banner`, `01-primary-cta` | [m](08-settings-admin/mobile.png) · [t](08-settings-admin/tablet.png) · [d](08-settings-admin/desktop.png) |
| **Feeder home** (`15-feeder-home`) | Home for schools, pharmacy, lab, MCH, corporate, NCD, community, climate | `02-stat-card-row`, `03-list-row-card`, `03-offline-ready-chip`, `01-primary-cta`, … | [m](15-feeder-home/mobile.png) · [t](15-feeder-home/tablet.png) · [d](15-feeder-home/desktop.png) |
| **Dual-pane desktop** (`03-dual-pane-desktop`) | Two-column lists / dashboards on wide screens | `07-side-nav-desktop`, `03-list-row-card`, `02-stat-card-row` | [m](03-dual-pane-desktop/mobile.png) · [t](03-dual-pane-desktop/tablet.png) · [d](03-dual-pane-desktop/desktop.png) |
| **Upload / batch** (`16-upload-batch`) | File upload + validation + push to ingest | `04-file-upload-field`, `04-error-inline`, `03-success-toast`, `01-primary-cta`, … | [m](16-upload-batch/mobile.png) · [t](16-upload-batch/tablet.png) · [d](16-upload-batch/desktop.png) |
| **Connector status** (`12-connector-status`) | External system health (EMR, HMIS, climate) | `02-stat-card-row`, `03-list-row-card`, `03-feeder-health-pill`, `05-warn-banner` | [m](12-connector-status/mobile.png) · [t](12-connector-status/tablet.png) · [d](12-connector-status/desktop.png) |
| **Empty state shell** (`07-empty-state-shell`) | Happy-path layout with empty body (worklist / queue) | `09-section-header`, `01-status-chip`, `01-empty-state`, `01-primary-cta` | [m](07-empty-state-shell/mobile.png) · [t](07-empty-state-shell/tablet.png) · [d](07-empty-state-shell/desktop.png) |
| **Insurance prevention** (`17-insurance-prevention`) | §7 prevention population insights — not claims / not CHIS identity | `02-stat-card-row`, `03-list-row-card`, `04-note-banner`, `01-primary-cta` | [m](17-insurance-prevention/mobile.png) · [t](17-insurance-prevention/tablet.png) · [d](17-insurance-prevention/desktop.png) |

## When to use which

| Need | Layout |
| --- | --- |
| Splash / login / role pick | `01-auth-centered-card` |
| CHW phone capture | `04-field-mobile-shell` + `09-form-capture` / `02-list-worklist` |
| Tablet field work | `05-field-tablet-shell` |
| Desktop consoles | `06-desktop-sidebar-shell` + body layout |
| Overview dashboards | `11-dashboard-metrics` or `03-dual-pane-desktop` |
| Feeder party home | `15-feeder-home` |
| Maps | `13-map-explorer` |
| Queues | `14-queue-desk` |
| Alert / referral detail | `10-detail-action` |
| Admin / scopes / registry | `08-settings-admin` |
| CSV / API batches | `16-upload-batch` |
| EMR / HMIS / climate health | `12-connector-status` |

## Regenerate

```bash
python app-ui/00-shared/generate_kit.py
```
