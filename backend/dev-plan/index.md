# Backend Development Plan
Build the reusable backend foundation, then deliver product capabilities in tandem with the active frontend slice.

## Execution Order

1. Prepare or verify the minimum shared foundation in `P000_setup` through `P008_perf`.
2. Start product work from [`frontend/dev-plan/24-product-vertical-slices.md`](../../frontend/dev-plan/24-product-vertical-slices.md), not from a backend module backlog.
3. For each active frontend screen/journey, apply `P009_models` through `P015_offline` only as needed inside that same slice.
4. Wire and prove the real frontend repository before opening the next slice.

The backend may never get ahead by building speculative product domains. Foundation work may be reused across slices, but data models, endpoints, modules, seeds, events, locales, and offline behavior are justified by a current UI/flow.

## Release Gates

- Foundation gates must pass before product slices; each active slice must pass its own frontend, backend, and cross-stack gates before the next slice begins.
- Every slice must follow `backend/.cursor/vertical-slice-delivery.mdc` and `backend/.cursor/module-creation.mdc`.
- Module names, permissions, entitlements, routes, states, and contracts must remain aligned with the product SoT, `app-flows/`, the active `screen.json`, and the frontend repository.
- Preserve multi-role RBAC + ABAC + subscription/module intersection, consent, audit, offline-first field work, `snake_case`, `human_friendly_id`, documentation, and script hygiene.
- Existing generic HIS code may be reused only when it directly serves the FCHIP slice and is renamed/scoped without preserving unrelated hospital product behavior.
