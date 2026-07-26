# Shared layouts

Page shells for maximum reuse across consumer surfaces and data-feeder modules.
Pick a layout, then drop in shared components.

**17 layouts** × mobile / tablet / desktop.

| Layout | Purpose | Composes | Specimens |
| --- | --- | --- | --- |
| **Auth centered card** (`auth-centered-card`) | Splash · login · role picker on a centered card | `logo-lockup`, `slogan-line`, `labeled-field`, `primary-cta`, … | [m](auth-centered-card/mobile.png) · [t](auth-centered-card/tablet.png) · [d](auth-centered-card/desktop.png) |
| **Field mobile shell** (`field-mobile-shell`) | CHW / caregiver / feeder capture on phone | `top-app-bar`, `section-header`, `bottom-nav-field`, `status-chip`, … | [m](field-mobile-shell/mobile.png) · [t](field-mobile-shell/tablet.png) · [d](field-mobile-shell/desktop.png) |
| **Field tablet shell** (`field-tablet-shell`) | Same field IA with wider content column | `top-app-bar`, `section-header`, `bottom-nav-field`, `stat-card-row`, … | [m](field-tablet-shell/mobile.png) · [t](field-tablet-shell/tablet.png) · [d](field-tablet-shell/desktop.png) |
| **Desktop sidebar shell** (`desktop-sidebar-shell`) | Facility · district · admin · feeder desktop chrome | `side-nav-desktop`, `top-app-bar`, `cascade-footer` | [m](desktop-sidebar-shell/mobile.png) · [t](desktop-sidebar-shell/tablet.png) · [d](desktop-sidebar-shell/desktop.png) |
| **Dashboard metrics** (`dashboard-metrics`) | Overview with stats + list + CTA | `stat-card-row`, `list-row-card`, `filter-chip-row`, `primary-cta` | [m](dashboard-metrics/mobile.png) · [t](dashboard-metrics/tablet.png) · [d](dashboard-metrics/desktop.png) |
| **Form capture** (`form-capture`) | Structured offline / online data entry | `section-header`, `form-stack`, `consent-toggle`, `primary-cta`, … | [m](form-capture/mobile.png) · [t](form-capture/tablet.png) · [d](form-capture/desktop.png) |
| **List / worklist** (`list-worklist`) | Today’s tasks, alerts, notifications | `section-header`, `status-chip`, `list-row-card`, `primary-cta`, … | [m](list-worklist/mobile.png) · [t](list-worklist/tablet.png) · [d](list-worklist/desktop.png) |
| **Queue desk** (`queue-desk`) | Referral / lab / result queues | `filter-chip-row`, `queue-item`, `primary-cta`, `sync-status-strip` | [m](queue-desk/mobile.png) · [t](queue-desk/tablet.png) · [d](queue-desk/desktop.png) |
| **Map explorer** (`map-explorer`) | GIS hotspot + climate legend | `filter-chip-row`, `hotspot-map`, `section-header` | [m](map-explorer/mobile.png) · [t](map-explorer/tablet.png) · [d](map-explorer/desktop.png) |
| **Detail + action** (`detail-action`) | Explainable alert / referral detail with CTA | `stat-card-row`, `explainability-block`, `list-row-card`, `primary-cta`, … | [m](detail-action/mobile.png) · [t](detail-action/tablet.png) · [d](detail-action/desktop.png) |
| **Settings / admin** (`settings-admin`) | Org · roles · consent · API scopes · feeder registry | `section-header`, `list-row-card`, `note-banner`, `primary-cta` | [m](settings-admin/mobile.png) · [t](settings-admin/tablet.png) · [d](settings-admin/desktop.png) |
| **Feeder home** (`feeder-home`) | Home for schools, pharmacy, lab, MCH, corporate, NCD, community, climate | `stat-card-row`, `list-row-card`, `offline-ready-chip`, `primary-cta`, … | [m](feeder-home/mobile.png) · [t](feeder-home/tablet.png) · [d](feeder-home/desktop.png) |
| **Dual-pane desktop** (`dual-pane-desktop`) | Two-column lists / dashboards on wide screens | `side-nav-desktop`, `list-row-card`, `stat-card-row` | [m](dual-pane-desktop/mobile.png) · [t](dual-pane-desktop/tablet.png) · [d](dual-pane-desktop/desktop.png) |
| **Upload / batch** (`upload-batch`) | File upload + validation + push to ingest | `file-upload-field`, `error-inline`, `success-toast`, `primary-cta`, … | [m](upload-batch/mobile.png) · [t](upload-batch/tablet.png) · [d](upload-batch/desktop.png) |
| **Connector status** (`connector-status`) | External system health (EMR, HMIS, climate) | `stat-card-row`, `list-row-card`, `feeder-health-pill`, `warn-banner` | [m](connector-status/mobile.png) · [t](connector-status/tablet.png) · [d](connector-status/desktop.png) |
| **Empty state shell** (`empty-state-shell`) | Happy-path layout with empty body (worklist / queue) | `section-header`, `status-chip`, `empty-state`, `primary-cta` | [m](empty-state-shell/mobile.png) · [t](empty-state-shell/tablet.png) · [d](empty-state-shell/desktop.png) |
| **Insurance prevention** (`insurance-prevention`) | §7 prevention population insights — not claims / not CHIS identity | `stat-card-row`, `list-row-card`, `note-banner`, `primary-cta` | [m](insurance-prevention/mobile.png) · [t](insurance-prevention/tablet.png) · [d](insurance-prevention/desktop.png) |

## When to use which

| Need | Layout |
| --- | --- |
| Splash / login / role pick | `auth-centered-card` |
| CHW phone capture | `field-mobile-shell` + `form-capture` / `list-worklist` |
| Tablet field work | `field-tablet-shell` |
| Desktop consoles | `desktop-sidebar-shell` + body layout |
| Overview dashboards | `dashboard-metrics` or `dual-pane-desktop` |
| Feeder party home | `feeder-home` |
| Maps | `map-explorer` |
| Queues | `queue-desk` |
| Alert / referral detail | `detail-action` |
| Admin / scopes / registry | `settings-admin` |
| CSV / API batches | `upload-batch` |
| EMR / HMIS / climate health | `connector-status` |

## Regenerate

```bash
python app-ui/00-shared/generate_kit.py
```
