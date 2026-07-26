# P009 Database Models
Add only the data required by the active frontend screen or connected journey.

## Slice Model Order

Within each slice:

1. Identify UI fields, filters, actions, states, scopes, provenance, consent, and history requirements.
2. Reuse existing FCHIP entities when ownership is correct; do not duplicate records per surface.
3. Add the smallest models, relations, indexes, and migration needed by the typed frontend contract.
4. Add status history, audit, version, source, geography, and sync metadata when the journey requires them.

## Shared Contract

- Names must use lowercase `snake_case`.
- Scoped models must consistently include the applicable tenant, catchment, facility, programme, feeder, geography, ownership, audit, version, and soft-delete fields.
- Public entities need unique immutable `human_friendly_id`; raw primary keys stay internal.
- Capture data must retain source and consent provenance. Referrals, alerts, sync, connectors, and export reviews must retain status history.
- GIS/climate observations retain geography, observation time, source, and quality metadata.
- Do not add generic HIS models unless a current FCHIP screen/flow explicitly needs them.

## Acceptance

The migration and seed data must support every state of the active screen without speculative unrelated tables or ownership drift.
