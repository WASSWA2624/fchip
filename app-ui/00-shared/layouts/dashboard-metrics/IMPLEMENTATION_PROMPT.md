# Implementation prompt — shared layout `dashboard-metrics`

> Paste this whole file into an agent session when implementing this reusable page layout.

## Mission

Implement **Dashboard metrics** as a reusable responsive layout shell in `frontend/lib/shared/layout`, composed from shared components, so product screens declare `dashboard-metrics` in `screen.json` and plug content slots instead of rebuilding chrome.

_Purpose: Overview with stats + list + CTA_

## Identity

| Field | Value |
| --- | --- |
| Kind | Shared layout |
| Slug | `dashboard-metrics` |
| Suggested Dart name | `AppDashboardMetrics` |
| Surfaces | `facility`, `district`, `NGO`, `feeder homes` |
| Breakpoints | `mobile`, `tablet`, `desktop` |
| Themes | `light`, `dark`, `system` |

## Visual sources

Folder: `app-ui/00-shared/layouts/dashboard-metrics/`

- `desktop-dark.png`
- `desktop.png`
- `mobile-dark.png`
- `mobile.png`
- `tablet-dark.png`
- `tablet.png`

Also read:

- `app-ui/00-shared/layouts/README.md`
- `layout.json` in this folder
- Specimens for each composed component

## Composes (implement or reuse these first)

- `stat-card-row` → `app-ui/00-shared/components/**/stat-card-row/` + `frontend/lib/shared/components/`
- `list-row-card` → `app-ui/00-shared/components/**/list-row-card/` + `frontend/lib/shared/components/`
- `filter-chip-row` → `app-ui/00-shared/components/**/filter-chip-row/` + `frontend/lib/shared/components/`
- `primary-cta` → `app-ui/00-shared/components/**/primary-cta/` + `frontend/lib/shared/components/`

## Target code locations

| Layer | Path |
| --- | --- |
| Layout widget | `frontend/lib/shared/layout/app_dashboard_metrics.dart` |
| Layout barrel | `frontend/lib/shared/layout/` |
| Supporting shells | `frontend/lib/shared/layout/` (`ResponsivePage`, `AsyncStateScaffold`, workspace shells) |
| Tests | `frontend/test/shared/layout/app_dashboard_metrics_test.dart` |
| Goldens | `frontend/test/shared/layout/goldens/` |

## Applicable rules

### Product & structure

- `.cursor/mandatories.mdc`
- `.cursor/app-write-up.mdc`
- `.cursor/index.mdc`
- `frontend/.cursor/index.mdc`
- `frontend/.cursor/project_structure.mdc`
- `frontend/.cursor/architecture.mdc`
- `frontend/.cursor/layouts.mdc`
- `frontend/.cursor/ui-workspace.mdc`
- `frontend/.cursor/navigation.mdc`

### UI kit

- `frontend/.cursor/design-system.mdc`
- `frontend/.cursor/components.mdc`
- `frontend/.cursor/layouts.mdc`
- `frontend/.cursor/ui-patterns.mdc`
- `frontend/.cursor/ui-workspace.mdc`
- `frontend/.cursor/ui-feedback.mdc`
- `frontend/.cursor/navigation.mdc`
- `frontend/.cursor/accessibility.mdc`
- `frontend/.cursor/assets_branding.mdc`

### Quality

- `frontend/.cursor/localization_i18n.mdc`
- `frontend/.cursor/validation.mdc`
- `frontend/.cursor/error_handling.mdc`
- `frontend/.cursor/testing.mdc`
- `frontend/.cursor/performance.mdc`
- `frontend/.cursor/observability.mdc`
- `frontend/.cursor/coding_conventions.mdc`

## Actionable implementation plan

1. Confirm whether `dashboard-metrics` already maps to an existing shared layout (`ResponsiveAppShell`, workspace layouts, auth shell). Prefer adapting the existing shell over a parallel tree.
2. Define named content slots that screens will fill, for example: `header`, `filters`, `body`, `primaryAction`, `footer`, `sidePanel` — only slots visible in the specimens.
3. Wire composed shared components listed above; if a component is missing, implement that component prompt first.
4. Apply breakpoint behavior from `frontend/.cursor/layouts.mdc`:
   - `<600` one column / bottom nav or drawer when the specimens show it
   - `600–1199` rail / compact side nav
   - `≥1200` menu bar + side nav as shown
5. Enforce max content widths appropriate to the layout purpose (auth, form, detail, dashboard, data-heavy).
6. Integrate with `AsyncStateScaffold` so host screens can pass loading/empty/error/forbidden states without custom scaffolds.
7. Localize only chrome owned by the layout; leave screen-specific copy to callers.
8. Add widget + golden tests for all six specimens.
9. Update consuming screens to select this layout by slug from `screen.json` instead of bespoke scaffolding.

## Reusability checklist

- [ ] One layout slug → one shared implementation
- [ ] Screens pass slots/providers; layout does not own feature repositories
- [ ] Works for every surface listed in `layout.json`
- [ ] Navigation destinations omitted when unauthorized (caller + permissions)
- [ ] No hard-coded feature routes inside the layout except optional documented slot defaults

## Backend linkage

Layouts are structural. Backend pairing belongs to each **screen** that uses `dashboard-metrics`. Ensure the layout supports the states those screens declare (`loading`, `empty`, `error`, `forbidden`, `offline`, `conflict`) via slots or `AsyncStateScaffold`, so backend-driven states render consistently.

## Done when

- Specimens matched across breakpoints/themes
- At least one real screen composes this layout through shared APIs
- Goldens/tests pass
- `app-ui` screens that declare `layout: "dashboard-metrics"` can mount without forking chrome

## Do not

- Duplicate this layout inside a feature folder
- Bake module-specific business logic into the shell
- Ignore tablet/desktop specimens
- Ship without empty/loading regions the specimens show
