# Implementation prompt — `01-chw-vht-mobile/08-create-referral`

> Paste this whole file into an agent session when implementing this UI. Do not invent a different screen.

## Mission

Implement **Create referral** as a production Flutter screen in `frontend/lib`, with maximum reuse of the shared kit, correct responsive behavior from the six mockups, typed domain/data layers, and a **matching backend** in the same atomic chronology unit before starting the next screen.

_Subtitle: Send household to facility_

## Identity

| Field | Value |
| --- | --- |
| Kind | Screen (`form`) |
| Module | `01-chw-vht-mobile` |
| Screen slug | `08-create-referral` |
| Chronology | `S-020` |
| Slice | `VS-01` |
| Phase | `mvp` |
| Deferred | `false` |
| Chronology status | `not-started` |
| Route | `/01-chw-vht-mobile/08-create-referral` |
| Parent route | `/01-chw-vht-mobile/01-worklist-home` |
| Layout | `08-form-capture` |
| Body layouts | `mobile` → `08-form-capture`, `tablet` → `08-form-capture`, `desktop` → `08-form-capture` |
| Shells | `mobile` → `03-field-mobile-shell`, `tablet` → `04-field-tablet-shell`, `desktop` → `05-desktop-sidebar-shell` |
| Roles | `chw`, `vht` |
| Supported states | `default`, `loading`, `error`, `success`, `offline`, `forbidden` |
| Localization prefix | `01_chw_vht_mobile.08_create_referral` |
| Access policy | RBAC + ABAC + subscription + assigned modules |
| Identifier policy | Display human_friendly_id only; never expose raw database IDs |

## Visual sources (match; do not raster-copy)

Folder: `app-ui/01-chw-vht-mobile/08-create-referral/`

Specimens present:

- `desktop-dark.png`
- `desktop.png`
- `mobile-dark.png`
- `mobile.png`
- `tablet-dark.png`
- `tablet.png`

Also read:

- `app-ui/01-chw-vht-mobile/README.md`
- `app-ui/00-shared/tokens.json`
- Shared layout specimens for `08-form-capture` under `app-ui/00-shared/layouts/08-form-capture/`
- Shared component specimens listed by that layout's `layout.json` `composes` array
- Connected journeys under `app-flows/` (especially `07-navigation.md` and module journeys)

## Target code locations (reuse before create)

| Layer | Path |
| --- | --- |
| Feature root | `frontend/lib/features/chw_vht_mobile/` |
| Page | `frontend/lib/features/chw_vht_mobile/presentation/pages/08_create_referral_page.dart` |
| Widgets (feature-only) | `frontend/lib/features/chw_vht_mobile/presentation/widgets/` |
| Presentation state | `frontend/lib/features/chw_vht_mobile/presentation/state/` |
| Domain | `frontend/lib/features/chw_vht_mobile/domain/` |
| Data / repository impl | `frontend/lib/features/chw_vht_mobile/data/` |
| Repository contract | `frontend/lib/features/chw_vht_mobile/domain/repositories/chw_vht_mobile_repository.dart` |
| Router entry | `frontend/lib/app/router/` (route must equal `/01-chw-vht-mobile/08-create-referral`) |
| Shared layout | `frontend/lib/shared/layout/` (implement/reuse `08-form-capture`) |
| Shared components | `frontend/lib/shared/components/` |
| Tests | `frontend/test/features/chw_vht_mobile/` |
| Backend module | `backend/src/modules/chw_vht_mobile/` |

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

Follow `frontend/dev-plan/25-slice-execution-playbook.md` for `S-020`:

### Phase 0 — Claim the screen

1. Confirm `S-020` is the next unfinished non-deferred row in `chronology.yaml` (or stop if another screen is already in progress).
2. Set chronology `status` to `ui-fixtures`.
3. Start a tracker block from `frontend/dev-plan/slices/TEMPLATE.md`.

### Phase 1 — Read before coding

4. Treat `screen.json` in this folder as the contract for route, roles, access, layout, shells, states, navigation, and `l10n_key_prefix`.
5. Open all six mockups (mobile/tablet/desktop × light/dark) and note hierarchy, spacing, CTAs, empty regions, and chrome.
6. Resolve `08-form-capture` and every composed component against `app-ui/00-shared/`.
7. Map navigation:
   - Tabs: Worklist → `/01-chw-vht-mobile/01-worklist-home`; Alerts → `/01-chw-vht-mobile/10-alerts-inbox`; Sync → `/01-chw-vht-mobile/12-sync-status`; More → `/00-shared/09-notifications-center`
   - Primary action: Submit referral → `/01-chw-vht-mobile/09-referral-status`
   - Access denied → `/00-shared/10-access-denied`
   - Not found → `/00-shared/11-not-found`

### Phase 2 — Flutter UI on fixtures (maximum reuse)

8. Register route `/01-chw-vht-mobile/08-create-referral` with the access guard for roles `chw`, `vht`.
9. Compose the page from shared shells + `08-form-capture` + catalog components. Prefer:
   - `AsyncStateScaffold`, `ResponsivePage`, `AppWorkspace`, `AppListTable`, `AppWorkspaceDetailPanel`, `AppActionPanel` when they fit `ui-workspace.mdc`.
10. Implement **every** supported state: `default`, `loading`, `error`, `success`, `offline`, `forbidden`.
11. Add ARB keys under `01_chw_vht_mobile.08_create_referral` only — no hard-coded user strings.
12. Verify at `390×844`, `768×1024`, `1440×900` in light and dark.
13. Back with a typed fixture / fake repository; add unit, widget, and golden tests.
14. Place feature-only widgets under `frontend/lib/features/chw_vht_mobile/presentation/widgets/`; anything reusable across modules must move to `frontend/lib/shared/`.

### Phase 3 — Derive the backend contract from the built UI

15. Walk the UI and fill the derivation table (field → model; filter → query; CTA → `POST …/<action>`; role → permission; forbidden → authz path; offline/conflict → idempotency + version; live region → scoped event; sensitive read → consent + audit).
16. Define the smallest repository interface and DTO shapes. Set chronology `status` to `contract-defined`.
17. Expose **`human_friendly_id` only** — never raw DB IDs in UI or public payloads.

### Phase 4 — Matching backend (same atomic unit)

18. Implement under `backend/src/modules/chw_vht_mobile/` per `backend/dev-plan/P016_slice_pairing.md` and backend rules above: Prisma + migration, Zod, repository, service, controller, routes, permissions, consent, audit, events, seeds, tests.
19. Seeds must reproduce every declared UI state.
20. Set chronology `status` to `backend-in-progress`, then `wired` when the real repository replaces fixtures.

### Phase 5 — Wire, prove, close

21. Delete the fake repository unless tests still override it.
22. Prove one real user action end-to-end plus declared failure states.
23. Mark `S-020` `status: done`, `backend: paired` (or `none` with static evidence only).
24. Update `tracker.md` and both registries; run `python tool/check_slice_coverage.py`.

## Reusability checklist

- [ ] No duplicate button, chip, banner, form field, nav, or feedback widget invented in the feature folder when a shared catalog item exists
- [ ] Layout `08-form-capture` is a shared layout implementation, not a one-off Scaffold tree
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
