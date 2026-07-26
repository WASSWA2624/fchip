# Frontend Development Plan

Entry point for FCHIP frontend delivery. Build the shared foundation once, then build the product as frontend-first vertical slices where **every screen ships with the backend that serves it**.

## The pairing law

Product development starts at the Flutter UI and never leaves the backend behind:

```text
screen.json + mockups → Flutter UI (fixtures) → typed contract
→ matching backend (models, migration, API, authz, audit, seeds, tests)
→ real repository wired → cross-stack proof → slice closed
```

A slice is not done because the UI looks right. It is done when a real user action travels from the Flutter widget to the database and back. See [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc) and [`24-product-vertical-slices.md`](./24-product-vertical-slices.md).

## Read order

| Step | File | Role |
| --- | --- | --- |
| 00 | [`00-execution-policy.md`](./00-execution-policy.md) | How to run every step; reuse and patch rules |
| 01–23 | Foundation steps | Shared technical base, built or verified once |
| 23 | [`23-final-validation-checklist.md`](./23-final-validation-checklist.md) | Gate before product slices begin |
| 24 | [`24-product-vertical-slices.md`](./24-product-vertical-slices.md) | Product build order and per-slice gates |
| 25 | [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md) | The repeatable loop for one screen |

## Foundation steps (01–23)

Setup and shape: `01-project-setup`, `02-dependencies-and-tooling`, `03-app-architecture`, `04-folder-structure`, `05-environment-configuration`, `06-startup-bootstrap`.

Shell and look: `07-routing-and-navigation`, `08-responsive-layout-system`, `09-theme-system`, `10-localization-readiness`, `11-reusable-components`.

Data and access: `12-state-management-and-di`, `13-api-and-repository-readiness`, `14-data-modeling-storage-and-offline-sync`, `15-auth-session-security-and-permissions`, `16-forms-validation-search-and-data-tables`.

Quality: `17-error-handling-and-observability`, `18-platform-accessibility-and-input`, `19-performance-and-scalability`, `20-testing-readiness`, `21-build-ci-deployment-and-release`, `22-documentation-and-feature-workflow`, `23-final-validation-checklist`.

Foundation steps may prepare reusable infrastructure without a screen. Steps `24`–`25` may not: they only run against a real `app-ui` screen.

## Slice records

| Path | Role |
| --- | --- |
| [`slices/registry.yaml`](./slices/registry.yaml) | Machine-readable slice and screen ownership |
| [`slices/tracker.md`](./slices/tracker.md) | Live status of every slice and its backend pairing |
| [`slices/TEMPLATE.md`](./slices/TEMPLATE.md) | Per-slice record to copy into the tracker |

The backend mirror is [`backend/dev-plan/slices/registry.yaml`](../../backend/dev-plan/slices/registry.yaml). Both registries must agree on slice IDs.

## Enforcement

Run the coverage check before closing any slice:

```bash
python tool/check_slice_coverage.py
```

It fails when an `app-ui` screen has no owning slice, a registry lists a screen that does not exist, the two registries disagree, or a claimed-done slice has no backend disposition.

## Sources

Product identity: [`.cursor/app-write-up.mdc`](../../.cursor/app-write-up.mdc). Journeys: [`app-flows/`](../../app-flows/). Screens: [`app-ui/`](../../app-ui/). Rules: [`frontend/.cursor/index.mdc`](../.cursor/index.mdc).
