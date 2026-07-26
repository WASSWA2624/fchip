# 25 - Slice Execution Playbook

The repeatable loop for delivering **one** `app-ui` screen with its matching backend. Step `24` owns the order; this step owns the method.

## Applicable Rules
You must follow [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc), [`product_delivery.mdc`](../.cursor/product_delivery.mdc), [`feature_workflow.mdc`](../.cursor/feature_workflow.mdc), [`ui-workspace.mdc`](../.cursor/ui-workspace.mdc), [`permissions.mdc`](../.cursor/permissions.mdc), [`backend/.cursor/vertical-slice-delivery.mdc`](../../backend/.cursor/vertical-slice-delivery.mdc), and [`backend/.cursor/module-creation.mdc`](../../backend/.cursor/module-creation.mdc).

## Phase 1 - Read the screen

1. Open `app-ui/<module>/<screen>/screen.json` and record `route`, `parent_route`, `roles`, `access`, `state`, `supported_states`, `phase`, `l10n_key_prefix`, `layout`, `body_layouts`, `shells`, and `navigation`.
2. Open all six mockups (mobile, tablet, desktop; light and dark) and the module `README.md`.
3. Open the connected journey in [`app-flows/`](../../app-flows/), especially `07-navigation.md`.
4. Resolve `layout` and component slugs against `app-ui/00-shared/layouts/` and `app-ui/00-shared/components/`.
5. Start the slice record from [`slices/TEMPLATE.md`](./slices/TEMPLATE.md).

## Phase 2 - Build the UI on fixtures

6. Create the route in `lib/app/router/` exactly as declared, with its access guard.
7. Build the responsive screen from the shared kit at `390×844`, `768×1024`, and `1440×900`, light and dark.
8. Implement every declared state: loading, empty, error, forbidden, success, offline, conflict.
9. Add localization keys under the declared `l10n_key_prefix`; no hard-coded user text.
10. Back the screen with a typed fixture or fake repository and add unit, widget, and golden tests.

## Phase 3 - Derive the contract

Walk the built UI and write down what it truly needs. This table is the bridge from screen to backend — each left-hand fact creates a backend obligation.

| Observed in the UI | Backend obligation |
| --- | --- |
| Displayed field | Model column and response field |
| Filter, sort, search, pagination | Query parameter, index, pagination contract |
| Map bounds or hotspot layer | Geography fields, bounds query, quality metadata |
| Button or workflow action | `POST /resource/:human_friendly_id/<action>` with a status transition |
| Declared role or ABAC scope | Permission key, entitlement gate, scope filter |
| `forbidden` state | Authorization failure path and problem response |
| `empty` / `error` state | Seed fixture and stable error code |
| `offline` / `conflict` state | Idempotency key, version field, deterministic conflict rule |
| Live-updating region | Scoped realtime event |
| Sensitive read or share | Consent check plus audit evidence |
| Upload or export | Storage path, retention, anonymisation, approval |

11. Write the smallest repository interface and request/response shapes that satisfy the table. Do not design unused generic endpoints.

## Phase 4 - Build the matching backend

12. Follow `backend/dev-plan/P016_slice_pairing.md`, then `P009_models` → `P015_offline` only as the table requires.
13. Deliver in one pass: Prisma models and migration, Zod schemas, repository, service, controller, route, permissions, consent, audit, events, seeds, and tests.
14. Seeds must reproduce every state the screen declares, including empty, error, forbidden, offline, and conflict.

## Phase 5 - Wire and prove

15. Replace the fixture with the real repository and delete the fake unless a test still overrides it.
16. Run the user action against the real backend and confirm the response drives the UI.
17. Add one cross-stack test covering the journey plus its declared failure states.
18. Complete the slice record and run `python tool/check_slice_coverage.py`.

## Acceptance Criteria
- Route, roles, states, layout, and localization prefix match `screen.json` exactly.
- Every contract row in Phase 3 has shipped backend behavior, or the record explains why it is `n/a`.
- No public payload or widget exposes an internal database ID.
- Frontend and backend tests pass, and the cross-stack proof is named in the tracker.
- `backend: none` appears only for a screen proven static.
- The next slice does not begin while this screen has an undocumented backend gap.
