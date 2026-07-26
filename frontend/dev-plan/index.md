# Frontend Development Plan

Entry point for FCHIP frontend delivery. Two phases, in order:

1. **Foundation** (`00`–`23`) — shared Flutter shell, once.
2. **Product screens** (`24`–`25` + `slices/`) — one `app-ui` screen at a time, each with its matching backend.

## The pairing law

Real app development starts at the frontend. Every screen ships with the backend and database that serve it:

```text
next S-NNN in chronology.yaml
  → screen.json + mockups
  → Flutter UI (fixtures while coding)
  → typed contract from the UI
  → matching backend (models, migration, API, authz, audit, seeds, tests)
  → real repository wired
  → cross-stack proof
  → mark screen done → open next S-NNN
```

A screen is not done because the UI looks right. It is done when a real user action travels from the Flutter widget to the database and back. See [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc).

## Read order

| Step | File | Role |
| --- | --- | --- |
| 00 | [`00-execution-policy.md`](./00-execution-policy.md) | How to run every step |
| 01–23 | Foundation steps | Shared technical base, built or verified once |
| 23 | [`23-final-validation-checklist.md`](./23-final-validation-checklist.md) | Gate before product screens |
| 24 | [`24-product-vertical-slices.md`](./24-product-vertical-slices.md) | Atomic chronological screen order |
| 25 | [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md) | Loop for one screen + its backend |

## Foundation steps (01–23)

Setup and shape: `01-project-setup`, `02-dependencies-and-tooling`, `03-app-architecture`, `04-folder-structure`, `05-environment-configuration`, `06-startup-bootstrap`.

Shell and look: `07-routing-and-navigation`, `08-responsive-layout-system`, `09-theme-system`, `10-localization-readiness`, `11-reusable-components`.

Data and access: `12-state-management-and-di`, `13-api-and-repository-readiness`, `14-data-modeling-storage-and-offline-sync`, `15-auth-session-security-and-permissions`, `16-forms-validation-search-and-data-tables`.

Quality: `17-error-handling-and-observability`, `18-platform-accessibility-and-input`, `19-performance-and-scalability`, `20-testing-readiness`, `21-build-ci-deployment-and-release`, `22-documentation-and-feature-workflow`, `23-final-validation-checklist`.

Foundation may prepare reusable infrastructure without a screen. Steps `24`–`25` may not: they only run against a real `app-ui` screen.

## Atomic product records

| Path | Role |
| --- | --- |
| [`slices/chronology.yaml`](./slices/chronology.yaml) | **Build order** — every screen as `S-001` … `S-127` |
| [`slices/registry.yaml`](./slices/registry.yaml) | Module ownership (`VS-00` … `VS-23`) |
| [`slices/tracker.md`](./slices/tracker.md) | Live status and per-screen pairing records |
| [`slices/TEMPLATE.md`](./slices/TEMPLATE.md) | Per-screen record to copy into the tracker |

Backend mirror: [`backend/dev-plan/slices/registry.yaml`](../../backend/dev-plan/slices/registry.yaml). Slice IDs must match. Chronology is the source of delivery order.

## Enforcement

```bash
python tool/check_slice_coverage.py
```

Fails when an `app-ui` screen has no owning slice, chronology misses or duplicates a screen, registries disagree, or a claimed-done screen has no backend disposition.

## Sources

Product identity: [`.cursor/app-write-up.mdc`](../../.cursor/app-write-up.mdc). Journeys: [`app-flows/`](../../app-flows/). Screens: [`app-ui/`](../../app-ui/). Rules: [`frontend/.cursor/index.mdc`](../.cursor/index.mdc).
