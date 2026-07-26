# P012 Seeder
Provide reproducible data for every declared state of the active frontend slice.

## Per-Slice Seed Order

1. Tenant/organization, catchment/facility/programme, users, roles, permissions, subscription, and assigned modules needed by the screen.
2. Domain records matching the frontend repository fixtures.
3. Data for default/success plus loading-independent empty, forbidden, error trigger, offline/conflict, degraded, pending, or denied states where declared.
4. Connected records needed to prove the complete journey.

## Script Policy

- Existing seed families should be extended before adding script names.
- `seed-demo-data`, verification, and catalog scripts must remain deterministic and follow slice order.
- Obsolete helpers must be removed when their replacements land.

## Acceptance

Seeded environments must reproduce the active screen's fixtures and cross-stack journey deterministically without exposing real PHI.
