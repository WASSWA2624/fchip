# 25 - Slice Execution Playbook

The repeatable loop for delivering **one** chronology screen (`S-NNN`) with its matching backend. Step `24` and [`slices/chronology.yaml`](./slices/chronology.yaml) own the order; this step owns the method.

## Applicable Rules

You must follow [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc), [`product_delivery.mdc`](../.cursor/product_delivery.mdc), [`feature_workflow.mdc`](../.cursor/feature_workflow.mdc), [`ui-workspace.mdc`](../.cursor/ui-workspace.mdc), [`permissions.mdc`](../.cursor/permissions.mdc), [`backend/.cursor/vertical-slice-delivery.mdc`](../../backend/.cursor/vertical-slice-delivery.mdc), and [`backend/.cursor/module-creation.mdc`](../../backend/.cursor/module-creation.mdc).

## Phase 0 - Pick the next screen

1. Open [`slices/chronology.yaml`](./slices/chronology.yaml).
2. Take the first row where `deferred: false` and `status` is not `done`.
3. Confirm no other screen is already `ui-fixtures` through `wired`.
4. Set that row's `status` to `ui-fixtures` and note its `slice` (`VS-NN`).

## Phase 1 - Read the screen

5. Open `app-ui/<module>/<screen>/screen.json` and record `route`, `parent_route`, `roles`, `access`, `state`, `supported_states`, `phase`, `l10n_key_prefix`, `layout`, `body_layouts`, `shells`, and `navigation`.
6. Open all six mockups and the module `README.md`.
7. Open the connected journey in [`app-flows/`](../../app-flows/), especially `07-navigation.md`.
8. Resolve `layout` and component slugs against `app-ui/00-shared/layouts/` and `app-ui/00-shared/components/`.
9. Start the screen record from [`slices/TEMPLATE.md`](./slices/TEMPLATE.md).

## Phase 2 - Build the UI on fixtures

10. Create the route in `lib/app/router/` exactly as declared, with its access guard.
11. Build the responsive screen from the shared kit at `390×844`, `768×1024`, and `1440×900`, light and dark.
12. Implement every declared state: loading, empty, error, forbidden, success, offline, conflict.
13. Add localization keys under the declared `l10n_key_prefix`; no hard-coded user text.
14. Back the screen with a typed fixture or fake repository and add unit, widget, and golden tests.

## Phase 3 - Derive the contract

Walk the built UI and write down what it truly needs. Each left-hand fact creates a backend obligation.

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

15. Write the smallest repository interface and request/response shapes that satisfy the table. Set chronology `status` to `contract-defined`. Do not design unused generic endpoints.

## Phase 4 - Build the matching backend

16. Follow `backend/dev-plan/P016_slice_pairing.md`, then `P009_models` → `P015_offline` only as the table requires.
17. Deliver in one pass: Prisma models and migration, Zod schemas, repository, service, controller, route, permissions, consent, audit, events, seeds, and tests.
18. Seeds must reproduce every state the screen declares.
19. Set chronology `status` to `backend-in-progress`, then `wired` when the real repository is connected.

## Phase 5 - Wire and prove

20. Replace the fixture with the real repository and delete the fake unless a test still overrides it.
21. Run the user action against the real backend and confirm the response drives the UI.
22. Add one cross-stack test covering the journey plus its declared failure states.
23. Set chronology `status: done` and `backend: paired` (or `none` with evidence). Complete the tracker record. Bump the slice's `backend_paired` count in both registries.
24. Run `python tool/check_slice_coverage.py`.

## Acceptance Criteria

- Route, roles, states, layout, and localization prefix match `screen.json` exactly.
- Every contract row in Phase 3 has shipped backend behavior, or the record explains why it is `n/a`.
- No public payload or widget exposes an internal database ID.
- Frontend and backend tests pass, and the cross-stack proof is named in the tracker.
- `backend: none` appears only for a screen proven static.
- The next chronology screen does not begin while this screen has an undocumented backend gap.
