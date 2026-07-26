# Backend Development Plan

Build the reusable backend foundation, then deliver product capabilities **in tandem with each frontend chronology screen**.

## Execution Order

1. Prepare or verify the minimum shared foundation in `P000_setup` through `P008_perf`.
2. Start product work from [`frontend/dev-plan/slices/chronology.yaml`](../../frontend/dev-plan/slices/chronology.yaml) (`S-001` … `S-127`). Do not drive product work from a backend module backlog.
3. For the active frontend screen, run [`P016_slice_pairing`](./P016_slice_pairing.md) to derive the work, then apply `P009_models` through `P015_offline` only as that derivation requires.
4. Wire and prove the real frontend repository before the next chronology screen opens.

The backend may never get ahead by building speculative product domains. Foundation work may be reused across screens, but data models, endpoints, modules, seeds, events, locales, and offline behavior are justified by a current UI/flow.

## Plan files

| Range | Role |
| --- | --- |
| `P000_setup` – `P008_perf` | Reusable foundation; may be built without a screen |
| [`P016_slice_pairing`](./P016_slice_pairing.md) | Turn one frontend screen into its backend obligations |
| `P009_models` – `P015_offline` | Per-concern detail, applied only inside an active screen |
| [`slices/registry.yaml`](./slices/registry.yaml) | Backend half of module ownership; IDs mirror the frontend registry |

Screen order: [`frontend/dev-plan/slices/chronology.yaml`](../../frontend/dev-plan/slices/chronology.yaml).  
Status: [`frontend/dev-plan/slices/tracker.md`](../../frontend/dev-plan/slices/tracker.md).

## Release Gates

- Foundation gates must pass before product screens; each active screen must pass its frontend, backend, and cross-stack gates before the next screen begins.
- Every screen must follow `backend/.cursor/vertical-slice-delivery.mdc` and `backend/.cursor/module-creation.mdc`.
- `python tool/check_slice_coverage.py` must pass before a screen is closed.
- Module names, permissions, entitlements, routes, states, and contracts must remain aligned with the product SoT, `app-flows/`, the active `screen.json`, and the frontend repository.
- Preserve multi-role RBAC + ABAC + subscription/module intersection, consent, audit, offline-first field work, `snake_case`, `human_friendly_id`, documentation, and script hygiene.
- Existing generic HIS code may be reused only when it directly serves the FCHIP screen and is renamed/scoped without preserving unrelated hospital product behavior.
