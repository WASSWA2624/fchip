# P010 API Endpoints
Lock the smallest public contract required by the active frontend slice.

## Path Rules

- Business endpoints must live under `/api/v1`.
- Resource paths must use plural kebab-case.
- Standard operations must provide list, create, get, update, and archive or soft-delete behavior as applicable.
- Workflow transitions must use `POST /resource/:human_friendly_id/<action>`.
- Request/response/problem fixtures must be shared with frontend contract tests.
- List, map, dashboard, and worklist endpoints return only the fields the active UI needs.

## Slice Contract

For the current screen define:

- roles, permissions, subscription/module gate, and ABAC scope;
- request fields, validation, filters, pagination, sorting, and map bounds;
- success envelope plus stable error codes for declared UI states;
- consent, audit, rate-limit, upload/download, retention, and anonymisation needs;
- idempotency/version/conflict rules for offline writes;
- scoped realtime event only when the visible UI needs live updates.

## Acceptance

Route names, permissions, entitlements, model ownership, seed fixtures, and the frontend repository must remain aligned. The contract is not complete until the real frontend route consumes it.
