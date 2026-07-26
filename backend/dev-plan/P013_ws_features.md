# P013 WebSocket Features
Publish authorized domain events only after their owning modules are stable.

## Event Families

Add an event only when the active screen needs visible live reconciliation. Expected families include session revocation, notifications, worklist/referral changes, ingest/feed health, sync outcomes, alerts, action deployment, connector state, map/risk refresh, and approved workflow status changes.

## Contract

- Event names and payload fields must remain stable and use `snake_case`.
- Subscriptions must enforce the same tenant, facility, role, entitlement, and module scope as HTTP endpoints.
- Events must not expose data beyond the subscriber's current authorization.
- Domain services should publish through the shared transport abstraction.
- Frontend controllers must consume typed deltas or perform the smallest targeted refresh; widgets must not depend on raw event payloads.
- Do not add speculative event families for screens not yet being delivered.
