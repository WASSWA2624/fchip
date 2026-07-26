# Shared layouts

Page shells for maximum reuse across consumer surfaces and data-feeder modules.
Pick a layout, then drop in shared components.

**17 layouts** × mobile / tablet / desktop × light / dark.
Dark specimens use the same filename with `-dark` before `.png`.

| Layout | Purpose | Composes | Specimens |
| --- | --- | --- | --- |
| **Auth centered card** (`01-auth-centered-card`) | Create account / sign in — phone number + password only | `01-logo-lockup`, `02-slogan-line`, `01-labeled-field`, `01-primary-cta`, … | [m](01-auth-centered-card/mobile.png) · [t](01-auth-centered-card/tablet.png) · [d](01-auth-centered-card/desktop.png) |
| **List / worklist** (`02-list-worklist`) | Today’s tasks, alerts, notifications | `02-section-header`, `01-status-chip`, `01-list-row-card`, `01-primary-cta`, … | [m](02-list-worklist/mobile.png) · [t](02-list-worklist/tablet.png) · [d](02-list-worklist/desktop.png) |
| **Field mobile shell** (`03-field-mobile-shell`) | CHW / caregiver / feeder capture on phone | `03-top-app-bar`, `02-section-header`, `04-bottom-nav-field`, `01-status-chip`, … | [m](03-field-mobile-shell/mobile.png) · [t](03-field-mobile-shell/tablet.png) · [d](03-field-mobile-shell/desktop.png) |
| **Field tablet shell** (`04-field-tablet-shell`) | Adaptive field IA with a compact navigation rail and wider content column | `03-top-app-bar`, `05-side-nav-desktop`, `02-section-header`, `03-stat-card-row`, … | [m](04-field-tablet-shell/mobile.png) · [t](04-field-tablet-shell/tablet.png) · [d](04-field-tablet-shell/desktop.png) |
| **Desktop sidebar shell** (`05-desktop-sidebar-shell`) | Facility · district · admin · feeder desktop chrome | `05-side-nav-desktop`, `03-top-app-bar`, `04-cascade-footer` | [m](05-desktop-sidebar-shell/mobile.png) · [t](05-desktop-sidebar-shell/tablet.png) · [d](05-desktop-sidebar-shell/desktop.png) |
| **Empty state shell** (`06-empty-state-shell`) | Happy-path layout with empty body (worklist / queue) | `02-section-header`, `01-status-chip`, `01-empty-state`, `01-primary-cta` | [m](06-empty-state-shell/mobile.png) · [t](06-empty-state-shell/tablet.png) · [d](06-empty-state-shell/desktop.png) |
| **Settings / admin** (`07-settings-admin`) | Org · roles · consent · API scopes · feeder registry | `02-section-header`, `01-list-row-card`, `04-note-banner`, `01-primary-cta` | [m](07-settings-admin/mobile.png) · [t](07-settings-admin/tablet.png) · [d](07-settings-admin/desktop.png) |
| **Form capture** (`08-form-capture`) | Structured offline / online data entry | `02-section-header`, `02-form-stack`, `03-consent-toggle`, `01-primary-cta`, … | [m](08-form-capture/mobile.png) · [t](08-form-capture/tablet.png) · [d](08-form-capture/desktop.png) |
| **Detail + action** (`09-detail-action`) | Explainable alert / referral detail with CTA | `03-stat-card-row`, `05-explainability-block`, `01-list-row-card`, `01-primary-cta`, … | [m](09-detail-action/mobile.png) · [t](09-detail-action/tablet.png) · [d](09-detail-action/desktop.png) |
| **Dashboard metrics** (`10-dashboard-metrics`) | Overview with stats + list + CTA | `03-stat-card-row`, `01-list-row-card`, `03-filter-chip-row`, `01-primary-cta` | [m](10-dashboard-metrics/mobile.png) · [t](10-dashboard-metrics/tablet.png) · [d](10-dashboard-metrics/desktop.png) |
| **Connector status** (`11-connector-status`) | External system health (EMR, HMIS, climate) | `03-stat-card-row`, `01-list-row-card`, `03-feeder-health-pill`, `06-warn-banner` | [m](11-connector-status/mobile.png) · [t](11-connector-status/tablet.png) · [d](11-connector-status/desktop.png) |
| **Map explorer** (`12-map-explorer`) | GIS hotspot + climate legend | `03-filter-chip-row`, `04-hotspot-map`, `02-section-header` | [m](12-map-explorer/mobile.png) · [t](12-map-explorer/tablet.png) · [d](12-map-explorer/desktop.png) |
| **Queue desk** (`13-queue-desk`) | Referral / lab / result queues | `03-filter-chip-row`, `05-queue-item`, `01-primary-cta`, `04-sync-status-strip` | [m](13-queue-desk/mobile.png) · [t](13-queue-desk/tablet.png) · [d](13-queue-desk/desktop.png) |
| **Feeder home** (`14-feeder-home`) | Home for schools, pharmacy, lab, MCH, corporate, NCD, community, climate | `03-stat-card-row`, `01-list-row-card`, `04-offline-ready-chip`, `01-primary-cta`, … | [m](14-feeder-home/mobile.png) · [t](14-feeder-home/tablet.png) · [d](14-feeder-home/desktop.png) |
| **Upload / batch** (`15-upload-batch`) | File upload + validation + push to ingest | `05-file-upload-field`, `05-error-inline`, `03-success-toast`, `01-primary-cta`, … | [m](15-upload-batch/mobile.png) · [t](15-upload-batch/tablet.png) · [d](15-upload-batch/desktop.png) |
| **Dual-pane desktop** (`16-dual-pane-desktop`) | Two-column lists / dashboards on wide screens | `05-side-nav-desktop`, `01-list-row-card`, `03-stat-card-row` | [m](16-dual-pane-desktop/mobile.png) · [t](16-dual-pane-desktop/tablet.png) · [d](16-dual-pane-desktop/desktop.png) |
| **Insurance prevention** (`17-insurance-prevention`) | §7 prevention population insights — not claims / not CHIS identity | `03-stat-card-row`, `01-list-row-card`, `04-note-banner`, `01-primary-cta` | [m](17-insurance-prevention/mobile.png) · [t](17-insurance-prevention/tablet.png) · [d](17-insurance-prevention/desktop.png) |

## When to use which

| Need | Layout |
| --- | --- |
| Splash / login / role pick | `01-auth-centered-card` |
| CHW phone capture | `03-field-mobile-shell` + `08-form-capture` / `02-list-worklist` |
| Tablet field work | `04-field-tablet-shell` |
| Desktop consoles | `05-desktop-sidebar-shell` + body layout |
| Overview dashboards | `10-dashboard-metrics` or `16-dual-pane-desktop` |
| Feeder party home | `14-feeder-home` |
| Maps | `12-map-explorer` |
| Queues | `13-queue-desk` |
| Alert / referral detail | `09-detail-action` |
| Admin / scopes / registry | `07-settings-admin` |
| CSV / API batches | `15-upload-batch` |
| EMR / HMIS / climate health | `11-connector-status` |

## Regenerate

```bash
python app-ui/00-shared/generate_kit.py
```
