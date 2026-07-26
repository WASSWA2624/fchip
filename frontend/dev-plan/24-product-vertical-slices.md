# 24 - Product Vertical Slices

Build the real FCHIP product from `app-ui/` and `app-flows/`. This plan starts product development after the shared foundation in steps `01`–`23`.

## Starting Baseline

The current frontend/backend contain broad hospital HIS workspaces. Reuse suitable platform primitives such as auth, tenancy, consent, repositories, responsive shells, sync, integrations, and tests, but do not rename an HIS page and count it as a FCHIP screen. Add FCHIP feature folders and routes from `screen.json`; retire unrelated HIS surfaces through explicit migration/feature-gate decisions.

## Non-Negotiable Delivery Loop

Do not build all Flutter screens and postpone the backend. For each screen, or the smallest connected journey:

1. Read its `screen.json`, six mockups, module README, shared component/layout references, and connected app flow.
2. Implement the responsive Flutter route first using typed fixtures.
3. Record every visible field, filter, action, state, access rule, data source, offline rule, and realtime need.
4. Define the smallest repository/API contract needed by that UI.
5. Immediately implement the matching backend schema, migration, seed data, authorization, validation, repository, service, endpoint, audit, sync/event behavior, and tests.
6. Wire the real repository and prove the journey end to end.
7. Close the slice only after frontend, backend, and cross-stack gates pass.

Follow `frontend/.cursor/product_delivery.mdc` and `backend/.cursor/vertical-slice-delivery.mdc`. A state specimen such as loading or empty may share the parent screen's endpoint, but it must still have its own widget/golden assertion.

## Slice Record

For each screen keep: route; phase; roles/ABAC scope; visual references; supported states; frontend files/tests; repository methods; API routes/events; models/migration; permissions/consent/audit; offline/idempotency/conflict policy; seeds; and validation evidence. Mark `backend: none` only for a proven static screen.

Maintain a machine-readable slice registry under `frontend/dev-plan/slices/` with the same slice IDs mirrored under `backend/dev-plan/slices/`. Add a coverage check that reads all `app-ui/**/screen.json` files and fails when a route, localization prefix, supported state, frontend owner, or backend disposition is missing.

## Delivery Order

Within a module, follow the screen order below unless a listed journey requires two screens to land together.

### Wave 0 - Entry, identity, access, and shared shell

- `00-shared`: `splash`, `create-account`, `login`, `forgot-password`, `consent-first-onboarding`, `offline-pin-lock`, `session-locked`, `role-surface-picker`, `notifications-center`, `access-denied`, `not-found`, `preferences`.
- Backend in tandem: identity/session recovery, consent, offline device unlock boundary, effective-access/workspace response, notifications, user preferences, localization/theme preference, and audit.

### Wave 1 - MVP capture-to-action loop

1. `01-chw-vht-mobile`: `worklist-home`, `worklist-empty`, `worklist-loading`, `household-visit-form`, `symptoms-vitals`, `maternal-child-indicators`, `visit-saved`, `create-referral`, `referral-status`, `alerts-inbox`, `alert-follow-up`, `sync-status`, `sync-failed`, `sync-conflict`.
2. `09-intelligence` foundation: `ingest-pipeline`, `feeder-health-board`.
3. `04-cascade-metrics`: `indicators-overview`, `gap-detection`, `partner-reports`.
4. `06-facility-dashboard` MVP: `overview`, `catchment-map`, `open-referrals`, `stock-signal`, `outreach-priorities`, `clinical-share-confirm`, `manual-case-signal`.
5. `07-referrals-desk`: `referral-queue`, `referral-queue-empty`, `referral-detail`, `outcome-feedback`.
6. `08-emr-connector`: `connector-status`, `connector-degraded`, `api-scopes-setup`, `push-event-log`, `facility-onboarding`.
7. `22-climate-feeds`: `climate-home`, `rainfall-temperature`, `extremes-flood-heat`, `feed-config-audit`.
8. `09-intelligence` decision loop: `gis-explorer`, `climate-fusion`, `ai-risk-scores`, `alerts-worklists-engine`, `clinical-support-guidance`.
9. `10-district-moh` MVP: `population-map`, `early-warnings`, `action-deploy`, `cascade-planning`.

Prove both complete MVP journeys before continuing:

- CHW visit → local save/sync → referral → facility queue/detail → outcome → CHW status → cascade metric.
- Fever/case signal → ingest → climate/GIS/risk → warning → deployed response → follow-up/result → metric/learning update.

### Wave 2 - Remaining MVP surfaces

- `02-community-caregiver`: `my-household`, `self-report`, `guidance-hints`, `household-needs-capture`.
- `03-outreach-school-health`: `campaign-planner`, `session-log`, `coverage-map`, `screening-results-entry`, `home-visit-batch-upload`.
- `13-admin-consent`: `org-catchment`, `users-roles`, `consent-privacy`, `emr-api-access`, `feeder-party-registry`.
- `23-insurance-insights`: `prevention-overview`, `risk-cohort-insights`, `anonymised-trends`.

Insurance responses must be prevention-focused, aggregated, anonymised, and unable to reveal raw PHI.

### Wave 3 - Phase 2 feeder and partner expansion

- `05-chis-livelihoods`: `enrolment`, `contributions`, `claims-access`, `iga-participation-entry`. Keep optional and do not make CHIS the product identity.
- `11-ngo-partner`: `programme-monitoring`, `impact-evidence`, `training-skills-analytics`, `field-dataset-upload`, `partner-indicator-entry`.
- `14-schools-health`: `school-home`, `health-education-session`, `learner-screening-entry`, `absenteeism-wellness`, `school-sync-status`.
- `15-pharmacy-outlets`: `pharmacy-home`, `stock-levels-entry`, `dispense-log`, `common-complaints`, `prestock-ack`.
- `16-labs-poc`: `lab-home`, `result-entry`, `batch-results-upload`, `result-queue`.
- `17-corporate-wellness`: `corporate-home`, `camp-vitals-entry`, `camp-summary-push`, `occupational-flags`.
- `18-mch-touchpoints`: `mch-home`, `anc-visit-entry`, `pnc-visit-entry`, `immunisation-entry`, `nutrition-monitoring`.
- `19-ncd-gericare`: `cohort-home`, `cohort-visit-entry`, `bp-screening-batch`, `stroke-risk-flags`.
- `20-hmis-dhis2`: `hmis-home`, `dataset-mapping`, `aggregate-push-pull`, `hmis-audit`.
- `21-community-events`: `events-home`, `outreach-event-log`, `community-dialogue`, `participation-register`.

Each feeder must enter through the shared ingest/provenance spine and expose feed health; do not create a separate product core.

### Wave 4 - Later phase screens

- Phase 3: `06-facility-dashboard/medicine-demand-forecast`, then `10-district-moh/national-roll-up`.
- Phase 4: `12-research-exports/evidence-catalog`, `export-request`, `research-contribution-upload`, `export-pending`.

Research export delivery must include ethics/privacy review, pending/denied/approved states, anonymisation proof, expiring download authorization, and immutable audit evidence. Raw PHI export is forbidden.

## Per-Slice Acceptance

- The route, parent, tabs, primary action, roles, phase, layout, shells, localization prefix, and supported states match `screen.json`.
- Mobile `390×844`, tablet `768×1024`, and desktop `1440×900` work in light and dark themes and reuse the shared kit.
- Frontend tests cover logic, repository mapping, widgets, and relevant goldens.
- Backend tests cover schema, access, consent/audit, service, route, contract, and workflow behavior.
- Offline-capable flows prove local save, idempotent retry, sync states, deterministic conflict handling, and current authorization.
- Realtime-capable flows prove scoped delivery and targeted Riverpod reconciliation.
- No public payload or UI exposes internal database IDs.
- The real backend is wired and the connected journey passes before the next slice starts.
- Frontend and backend slice registries agree, and automated coverage reports no missing or duplicate screen ownership.

## Completion

The product is complete only when all 127 catalogued screens have a slice record and every `app-flows/07-navigation.md` journey has cross-stack proof. Phase gates may defer later waves, but deferred routes must remain clearly feature-gated and must not be reported as implemented.
