# Implementation prompt — `21-hmis-dhis2/03-aggregate-push-pull`

> Paste this whole file into an agent session when implementing this UI. Do not invent a different screen.

## Mission

Implement **Aggregate push / pull** as a production Flutter screen in `frontend/lib`, with maximum reuse of the shared kit, correct responsive behavior from the six mockups, typed domain/data layers, and a **matching backend** in the same atomic chronology unit before starting the next screen.

_Subtitle: Scheduled exchange with district HMIS_

## Identity

| Field | Value |
| --- | --- |
| Kind | Screen (`form`) |
| Module | `21-hmis-dhis2` |
| Screen slug | `03-aggregate-push-pull` |
| Chronology | `S-116` |
| Slice | `VS-21` |
| Phase | `phase-2` |
| Deferred | `false` |
| Chronology status | `not-started` |
| Route | `/21-hmis-dhis2/03-aggregate-push-pull` |
| Parent route | `/21-hmis-dhis2/03-aggregate-push-pull` |
| Layout | `form-capture` |
| Body layouts | `mobile` → `form-capture`, `tablet` → `form-capture`, `desktop` → `form-capture` |
| Shells | `mobile` → `field-mobile-shell`, `tablet` → `field-tablet-shell`, `desktop` → `desktop-sidebar-shell` |
| Roles | `hmis-operator` |
| Supported states | `default`, `loading`, `error`, `success`, `offline`, `forbidden` |
| Localization prefix | `21_hmis_dhis2.03_aggregate_push_pull` |
| Access policy | RBAC + ABAC + subscription + assigned modules |
| Identifier policy | Display human_friendly_id only; never expose raw database IDs |

## Visual sources (match; do not raster-copy)

Folder: `app-ui/21-hmis-dhis2/03-aggregate-push-pull/`

Specimens present:

- `desktop-dark.png`
- `desktop.png`
- `mobile-dark.png`
- `mobile.png`
- `tablet-dark.png`
- `tablet.png`

Also read:

- `app-ui/21-hmis-dhis2/README.md`
- `app-ui/00-shared/tokens.json`
- Shared layout specimens for `form-capture` under `app-ui/00-shared/layouts/form-capture/`
- Shared component specimens listed by that layout's `layout.json` `composes` array
- Connected journeys under `app-flows/` (especially `07-navigation.md` and module journeys)

## Target code locations (reuse before create)

| Layer | Path |
| --- | --- |
| Feature root | `frontend/lib/features/hmis_dhis2/` |
| Page | `frontend/lib/features/hmis_dhis2/presentation/pages/03_aggregate_push_pull_page.dart` |
| Widgets (feature-only) | `frontend/lib/features/hmis_dhis2/presentation/widgets/` |
| Presentation state | `frontend/lib/features/hmis_dhis2/presentation/state/` |
| Domain | `frontend/lib/features/hmis_dhis2/domain/` |
| Data / repository impl | `frontend/lib/features/hmis_dhis2/data/` |
| Repository contract | `frontend/lib/features/hmis_dhis2/domain/repositories/hmis_dhis2_repository.dart` |
| Router entry | `frontend/lib/app/router/` (route must equal `/21-hmis-dhis2/03-aggregate-push-pull`) |
| Shared layout | `frontend/lib/shared/layout/` (implement/reuse `form-capture`) |
| Shared components | `frontend/lib/shared/components/` |
| Tests | `frontend/test/features/hmis_dhis2/` |
| Backend module | `backend/src/modules/hmis_dhis2/` |

**Reuse rule:** If a compliant shared widget, layout, repository helper, or route guard already exists, patch it — do not fork a second copy under another name.

## Applicable rules (must follow)

### Product & delivery

- `.cursor/mandatories.mdc`
- `.cursor/app-write-up.mdc`
- `.cursor/index.mdc`
- `frontend/.cursor/index.mdc`
- `frontend/.cursor/scope.mdc`
- `frontend/.cursor/product_delivery.mdc`
- `frontend/.cursor/feature_workflow.mdc`
- `frontend/.cursor/project_structure.mdc`
- `frontend/.cursor/architecture.mdc`
- `frontend/.cursor/checklists.mdc`
- `frontend/dev-plan/index.md`
- `frontend/dev-plan/00-execution-policy.md`
- `frontend/dev-plan/24-product-vertical-slices.md`
- `frontend/dev-plan/25-slice-execution-playbook.md`
- `frontend/dev-plan/slices/chronology.yaml`
- `frontend/dev-plan/slices/registry.yaml`
- `frontend/dev-plan/slices/tracker.md`
- `frontend/dev-plan/slices/TEMPLATE.md`
- `backend/dev-plan/P016_slice_pairing.md`

### UI / UX / structure

- `frontend/.cursor/design-system.mdc`
- `frontend/.cursor/components.mdc`
- `frontend/.cursor/layouts.mdc`
- `frontend/.cursor/ui-patterns.mdc`
- `frontend/.cursor/ui-workspace.mdc`
- `frontend/.cursor/ui-feedback.mdc`
- `frontend/.cursor/navigation.mdc`
- `frontend/.cursor/accessibility.mdc`
- `frontend/.cursor/assets_branding.mdc`

### Data, network, sync

- `frontend/.cursor/state_management.mdc`
- `frontend/.cursor/data_modeling.mdc`
- `frontend/.cursor/network_api.mdc`
- `frontend/.cursor/database_strategy.mdc`
- `frontend/.cursor/offline_sync.mdc`
- `frontend/.cursor/realtime_sync.mdc`
- `frontend/.cursor/instant_ui_sync.mdc`
- `frontend/.cursor/storage_strategy.mdc`

### Security & permissions

- `frontend/.cursor/security.mdc`
- `frontend/.cursor/authentication_session.mdc`
- `frontend/.cursor/permissions.mdc`

### Quality

- `frontend/.cursor/localization_i18n.mdc`
- `frontend/.cursor/validation.mdc`
- `frontend/.cursor/error_handling.mdc`
- `frontend/.cursor/testing.mdc`
- `frontend/.cursor/performance.mdc`
- `frontend/.cursor/observability.mdc`
- `frontend/.cursor/coding_conventions.mdc`

### Backend pairing

- `backend/.cursor/index.mdc`
- `backend/.cursor/vertical-slice-delivery.mdc`
- `backend/.cursor/module-creation.mdc`
- `backend/.cursor/api.mdc`
- `backend/.cursor/architecture.mdc`
- `backend/.cursor/prisma.mdc`
- `backend/.cursor/auth-security.mdc`
- `backend/.cursor/validation.mdc`
- `backend/.cursor/response-format.mdc`
- `backend/.cursor/compliance.mdc`
- `backend/.cursor/offline-support.mdc`
- `backend/.cursor/websockets.mdc`
- `backend/.cursor/testing.mdc`

## Actionable implementation plan

Follow `frontend/dev-plan/25-slice-execution-playbook.md` for `S-116`:

### Phase 0 — Claim the screen

1. Confirm `S-116` is the next unfinished non-deferred row in `chronology.yaml` (or stop if another screen is already in progress).
2. Set chronology `status` to `ui-fixtures`.
3. Start a tracker block from `frontend/dev-plan/slices/TEMPLATE.md`.

### Phase 1 — Read before coding

4. Treat `screen.json` in this folder as the contract for route, roles, access, layout, shells, states, navigation, and `l10n_key_prefix`.
5. Open all six mockups (mobile/tablet/desktop × light/dark) and note hierarchy, spacing, CTAs, empty regions, and chrome.
6. Resolve `form-capture` and every composed component against `app-ui/00-shared/`.
7. Map navigation:
   - Tabs: Home → `/21-hmis-dhis2/01-hmis-home`; Map → `/21-hmis-dhis2/02-dataset-mapping`; Exchange → `/21-hmis-dhis2/03-aggregate-push-pull`; Audit → `/21-hmis-dhis2/04-hmis-audit`
   - Primary action: Execute exchange → `/21-hmis-dhis2/03-aggregate-push-pull?state=success`
   - Access denied → `/00-shared/10-access-denied`
   - Not found → `/00-shared/11-not-found`

### Phase 2 — Flutter UI on fixtures (maximum reuse)

8. Register route `/21-hmis-dhis2/03-aggregate-push-pull` with the access guard for roles `hmis-operator`.
9. Compose the page from shared shells + `form-capture` + catalog components. Prefer:
   - `AsyncStateScaffold`, `ResponsivePage`, `AppWorkspace`, `AppListTable`, `AppWorkspaceDetailPanel`, `AppActionPanel` when they fit `ui-workspace.mdc`.
10. Implement **every** supported state: `default`, `loading`, `error`, `success`, `offline`, `forbidden`.
11. Add ARB keys under `21_hmis_dhis2.03_aggregate_push_pull` only — no hard-coded user strings.
12. Verify at `390×844`, `768×1024`, `1440×900` in light and dark.
13. Back with a typed fixture / fake repository; add unit, widget, and golden tests.
14. Place feature-only widgets under `frontend/lib/features/hmis_dhis2/presentation/widgets/`; anything reusable across modules must move to `frontend/lib/shared/`.

### Phase 3 — Derive the backend contract from the built UI

15. Walk the UI and fill the derivation table (field → model; filter → query; CTA → `POST …/<action>`; role → permission; forbidden → authz path; offline/conflict → idempotency + version; live region → scoped event; sensitive read → consent + audit).
16. Define the smallest repository interface and DTO shapes. Set chronology `status` to `contract-defined`.
17. Expose **`human_friendly_id` only** — never raw DB IDs in UI or public payloads.

### Phase 4 — Matching backend (same atomic unit)

18. Implement under `backend/src/modules/hmis_dhis2/` per `backend/dev-plan/P016_slice_pairing.md` and backend rules above: Prisma + migration, Zod, repository, service, controller, routes, permissions, consent, audit, events, seeds, tests.
19. Seeds must reproduce every declared UI state.
20. Set chronology `status` to `backend-in-progress`, then `wired` when the real repository replaces fixtures.

### Phase 5 — Wire, prove, close

21. Delete the fake repository unless tests still override it.
22. Prove one real user action end-to-end plus declared failure states.
23. Mark `S-116` `status: done`, `backend: paired` (or `none` with static evidence only).
24. Update `tracker.md` and both registries; run `python tool/check_slice_coverage.py`.

## Reusability checklist

- [ ] No duplicate button, chip, banner, form field, nav, or feedback widget invented in the feature folder when a shared catalog item exists
- [ ] Layout `form-capture` is a shared layout implementation, not a one-off Scaffold tree
- [ ] Feature widgets accept data via typed props / providers — no embedded API clients in widgets
- [ ] Repository is the only place that talks to the network / local DB for this screen's data
- [ ] Permissions hide unauthorized actions rather than showing disabled dead ends when policy says omit
- [ ] Loading uses logo-based `AppLoadingIndicator` / `AppButton.isLoading` per mandatories
- [ ] Shared multi-user data updates via realtime + instant UI sync helpers

## Done when

- Visual match to specimens across breakpoints and themes (not pixel-perfect raster copy)
- Route, roles, states, layout, shells, and l10n prefix match this folder's `screen.json`
- Real repository wired (or explicit `backend: none` with evidence)
- Cross-stack proof named in the tracker
- `python tool/check_slice_coverage.py` passes for this screen

## Do not

- Skip ahead while an earlier non-deferred chronology screen is unfinished
- Ship fixtures as "done"
- Expose internal database IDs
- Hard-code colors, spacing, typography, or user-facing strings
- Build unused generic backend endpoints
- Copy PNG mockups into `assets/` as the UI implementation
