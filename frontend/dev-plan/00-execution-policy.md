# 00 - Execution Policy

Use this workflow to establish the shared foundation, then deliver FCHIP as **atomic, chronological, frontend-first screens** — each with its matching backend.

## Applicable Rules

You must follow [`scope.mdc`](../.cursor/scope.mdc), [`product_delivery.mdc`](../.cursor/product_delivery.mdc), [`project_structure.mdc`](../.cursor/project_structure.mdc), [`architecture.mdc`](../.cursor/architecture.mdc), [`checklists.mdc`](../.cursor/checklists.mdc), [`index.mdc`](../.cursor/index.mdc), and [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc).

## Execution Order

1. Steps `01`–`23` establish or verify only the shared technical foundation. Reuse compliant existing code. Do not postpone product delivery for optional infrastructure.
2. Step [`24-product-vertical-slices.md`](./24-product-vertical-slices.md) owns **what to build and in what order**. The machine order is [`slices/chronology.yaml`](./slices/chronology.yaml) (`S-001` … `S-127`).
3. Step [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md) is the loop for **one** chronology screen and its backend.
4. Within every product screen: reference → fixture-backed UI → typed contract → matching backend → real wiring → cross-stack proof.
5. Backend domain work must not run as a separate later programme. It is part of the active screen, per [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc).
6. Only one chronology screen may be `in-progress` at a time. Do not skip ahead while an earlier non-deferred screen is unfinished.

## Required Workflow

1. Read the rules referenced by the current step.
2. Inspect the existing Flutter project before editing.
3. Keep compliant implementations unchanged; patch incomplete, duplicated, or noncompliant work.
4. Create files only when the step or rules require them.
5. You must not recreate working code under another name or add out-of-scope requirements.
6. Run the smallest practical validation command.
7. For product screens, record created/modified/skipped files plus backend routes/events, models, migration, seeds, and proof in [`slices/tracker.md`](./slices/tracker.md). Update the screen's `status` and `backend` fields in [`slices/chronology.yaml`](./slices/chronology.yaml).
8. Run `python tool/check_slice_coverage.py` before closing a product screen.

## Acceptance Criteria

- Each step must run independently without breaking earlier steps.
- Reuse, patch, or creation decisions must be explicit.
- Every product screen must stay aligned with `app-ui`, `app-flows`, product scope, and its implemented backend contract.
- A screen cannot be marked done with a fake repository unless it is explicitly static and needs no backend.
- Chronology order is the build order; module slices (`VS-NN`) are ownership groups, not a licence to skip screens.
