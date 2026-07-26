# 24 - Product Vertical Slices

Build the real FCHIP product from `app-ui/` and `app-flows/`, **one screen at a time**, after the shared foundation in steps `01`–`23`.

This step owns **what to build and in what order**. The machine-readable order is [`slices/chronology.yaml`](./slices/chronology.yaml) (`S-001` … `S-127`). [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md) owns **how to build one screen** and its backend. Status lives in [`slices/tracker.md`](./slices/tracker.md).

## Atomic unit

One atomic delivery unit = **one** `app-ui/<module>/<screen>/` folder:

1. Flutter UI from `screen.json` + six mockups.
2. Matching backend (models, migration, API, authz, audit, seeds, tests) — or explicit `backend: none`.
3. Real repository wired and cross-stack proof.
4. Only then open the next `S-NNN`.

Do not batch an entire module's UI and postpone its backends. State specimens (`*-empty`, `*-loading`) may share a parent endpoint, but each still needs its own widget/golden assertion and a chronology row.

## Starting baseline

The current frontend/backend contain broad hospital HIS workspaces. Reuse suitable platform primitives (auth, tenancy, consent, repositories, shells, sync, tests). Do not rename an HIS page and count it as a FCHIP screen. Add FCHIP feature folders and routes from `screen.json`; retire unrelated HIS surfaces through explicit migration/feature-gate decisions.

## Non-negotiable delivery loop

For the next unfinished, non-deferred row in `chronology.yaml`:

1. Read its `screen.json`, six mockups, module README, shared layout/components, and connected `app-flows/` journey.
2. Implement the responsive Flutter route first using typed fixtures.
3. Record every visible field, filter, action, state, access rule, data source, offline rule, and realtime need.
4. Define the smallest repository/API contract needed by that UI.
5. Immediately implement the matching backend schema, migration, seed data, authorization, validation, repository, service, endpoint, audit, sync/event behavior, and tests (`backend/dev-plan/P016_slice_pairing.md`).
6. Wire the real repository and prove the journey end to end.
7. Close the screen only after frontend, backend, and cross-stack gates pass.
8. Update chronology `status` / `backend`, tracker record, and both registries' `backend_paired` counts.

Follow `frontend/.cursor/product_delivery.mdc` and `backend/.cursor/vertical-slice-delivery.mdc`.

## Chronological waves

Order inside each wave matches `chronology.yaml`. Do not reorder without updating that file and the coverage check.

### Wave 0 — Entry, identity, access (`S-001`–`S-012`)

`00-shared`: splash → create-account → login → forgot-password → consent-first-onboarding → offline-pin-lock → session-locked → role-surface-picker → notifications-center → access-denied → not-found → preferences.

Backend in tandem: identity/session recovery, consent, offline device unlock boundary, effective-access/workspace, notifications, preferences, localization/theme preference, audit.

### Wave 1 — MVP capture-to-action (`S-013`–`S-060`)

1. `01-chw-vht-mobile` (`S-013`–`S-026`): worklist → visit → referral → alerts → sync states.
2. `02-intelligence` foundation (`S-027`–`S-028`): ingest-pipeline, feeder-health-board.
3. `03-cascade-metrics` (`S-029`–`S-031`).
4. `04-facility-dashboard` MVP (`S-032`–`S-038`) — defer `medicine-demand-forecast`.
5. `05-referrals-desk` (`S-039`–`S-042`).
6. `06-emr-connector` (`S-043`–`S-047`).
7. `07-climate-feeds` (`S-048`–`S-051`).
8. `02-intelligence` decision (`S-052`–`S-056`).
9. `08-district-moh` MVP (`S-057`–`S-060`) — defer `national-roll-up`.

Prove both MVP journeys before Wave 2:

- CHW visit → sync → referral → facility queue/detail → outcome → CHW status → cascade metric.
- Fever/case signal → ingest → climate/GIS/risk → warning → deployed response → follow-up → metric/learning.

### Wave 2 — Remaining MVP (`S-061`–`S-077`)

`09-community-caregiver` → `10-outreach-school-health` → `11-admin-consent` → `12-insurance-insights`.

Insurance responses must be prevention-focused, aggregated, anonymised, and unable to reveal raw PHI.

### Wave 3 — Phase 2 feeders (`S-078`–`S-121`)

`13-chis-livelihoods` → `14-ngo-partner` → `15-schools-health` → `16-pharmacy-outlets` → `17-labs-poc` → `18-corporate-wellness` → `19-mch-touchpoints` → `20-ncd-gericare` → `21-hmis-dhis2` → `22-community-events`.

Each feeder enters the shared ingest/provenance spine and exposes feed health. CHIS stays optional and must not become product identity.

### Wave 4 — Later phase (`S-122`–`S-127`)

Deferred phase-3 screens, then research exports: `medicine-demand-forecast`, `national-roll-up`, then `23-research-exports` (ethics review, anonymisation, expiring download, immutable audit; no raw PHI).

## Per-screen acceptance

- Route, parent, tabs, primary action, roles, phase, layout, shells, localization prefix, and supported states match `screen.json`.
- Mobile `390×844`, tablet `768×1024`, and desktop `1440×900` work in light and dark themes.
- Frontend tests cover logic, repository mapping, widgets, and relevant goldens.
- Backend tests cover schema, access, consent/audit, service, route, contract, and workflow behavior.
- Offline flows prove local save, idempotent retry, sync states, conflict handling, and current authorization.
- Realtime flows prove scoped delivery and targeted Riverpod reconciliation.
- No public payload or UI exposes internal database IDs.
- Real backend wired (or `backend: none` with evidence) before the next chronology screen.
- `python tool/check_slice_coverage.py` passes.

## Completion

The product is complete only when all 127 chronology rows are `done` and every `app-flows/07-navigation.md` journey has cross-stack proof. Deferred routes stay feature-gated and must not be reported as implemented early.
