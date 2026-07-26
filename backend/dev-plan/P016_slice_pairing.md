# P016 — Screen-to-Backend Pairing

Goal: turn one implemented frontend chronology screen (`S-NNN`) into the smallest correct backend, in the same atomic unit. Run this before `P009_models` through `P015_offline`, which supply the detail.

## Entry condition

Do not start until:

1. The screen is the next unfinished, non-deferred row in `frontend/dev-plan/slices/chronology.yaml`.
2. Its Flutter UI exists on fixtures and its typed repository contract is written.
3. You have read `app-ui/<module>/<screen>/screen.json`, its mockups, the module `README.md`, and the connected `app-flows/` journey.
4. The slice ID in `backend/dev-plan/slices/registry.yaml` matches the frontend registry and the chronology row's `slice`.

## Derivation table

Every fact on the left creates the obligation on the right. Nothing else gets built.

| From the screen | Backend obligation | Detail in |
| --- | --- | --- |
| Displayed field | Model column and response field | `P009_models` |
| Filter, sort, search, pagination | Query parameter and index | `P010_api_endpoints`, `P008_perf` |
| Map bounds or hotspot layer | Geography, observation window, source, quality fields | `P009_models` |
| Button or workflow action | `POST /resource/:human_friendly_id/<action>` plus status transition | `P010_api_endpoints` |
| `roles` and `access` | Permission key, entitlement gate, ABAC scope filter | `P001_core`, `P011_modules` |
| `forbidden` state | Authorization failure path and problem response | `P010_api_endpoints` |
| `empty`, `error` states | Seed fixture and stable error code | `P012_seeder` |
| `offline`, `conflict` states | Idempotency key, version metadata, deterministic conflict rule | `P015_offline` |
| Live-updating region | Scoped realtime event | `P013_ws_features` |
| Sensitive read, share, or export | Consent check, audit evidence, anonymisation | `P006_storage`, compliance rules |
| User-facing message | `en` catalog key | `P014_locales` |

If a row has no matching UI fact, do not build it. If a UI fact has no row, record the decision in the slice tracker before coding.

## Build order

1. Confirm ownership: does an existing FCHIP entity already serve this? Extend before adding.
2. Add only the Prisma models, relations, indexes, and migration the table requires.
3. Add Zod schemas, then repository, service, controller, route, audit, and scoped events.
4. Add seeds that reproduce every declared state, including empty, forbidden, offline, and conflict.
5. Add schema, authorization, service, route, contract, and workflow tests.
6. Wire the real frontend repository and prove the journey across both stacks.
7. Set chronology `backend: paired` (or `none` with evidence) and update the tracker.

Follow `backend/.cursor/module-creation.mdc` for the per-module sequence and `backend/.cursor/vertical-slice-delivery.mdc` for the done gate.

## Reuse boundary

Existing generic HIS modules and models may be reused only when they directly serve this FCHIP screen, and only after being scoped and renamed to community-health meaning. Do not carry over unrelated inpatient, theatre, payroll, mortuary, or billing behavior. Do not create a backend domain no current screen needs.

## Acceptance

- Every obligation raised by the derivation table has shipped code, or the tracker records why it is `n/a`.
- Routes, permissions, entitlements, models, and seeds agree with the frontend contract.
- Public payloads expose `human_friendly_id` only.
- `python tool/check_slice_coverage.py` passes.
- The frontend route runs on the real contract and cross-stack tests cover the declared states.
- The next chronology screen is not opened while this screen has an undocumented backend gap.
