# 00 - Execution Policy
Use this workflow to establish the shared foundation, then deliver FCHIP as frontend-first vertical slices.

## Applicable Rules
You must follow [`scope.mdc`](../.cursor/scope.mdc), [`product_delivery.mdc`](../.cursor/product_delivery.mdc), [`project_structure.mdc`](../.cursor/project_structure.mdc), [`architecture.mdc`](../.cursor/architecture.mdc), [`checklists.mdc`](../.cursor/checklists.mdc), and [`index.mdc`](../.cursor/index.mdc).

## Execution Order

1. Steps `01`–`23` establish or verify only the shared technical foundation. Reuse compliant existing code and do not postpone product delivery for optional infrastructure.
2. Step [`24-product-vertical-slices.md`](./24-product-vertical-slices.md) is the product build plan and source of delivery order.
3. Step [`25-slice-execution-playbook.md`](./25-slice-execution-playbook.md) is the loop to run for each screen in that order.
4. Within every product slice, work starts from the Flutter screen: reference → fixture-backed UI → typed contract → matching backend → real wiring → cross-stack proof.
5. Backend domain implementation must not run as a separate later programme. It is part of the active frontend slice, per [`.cursor/mandatories.mdc`](../../.cursor/mandatories.mdc).

## Required Workflow
1. Read the rules referenced by the current step.
2. Inspect the existing Flutter project before editing.
3. Keep compliant implementations unchanged; patch incomplete, duplicated, or noncompliant work.
4. Create files only when the step or rules require them.
5. You must not recreate working code under another name or add out-of-scope requirements.
6. Run the smallest practical validation command.
7. Record created, modified, and skipped files plus the screen, backend routes/events, models, migration, seeds, and proof in [`slices/tracker.md`](./slices/tracker.md).
8. Run `python tool/check_slice_coverage.py` before closing a product slice.

## Acceptance Criteria
- Each step must run independently without breaking earlier steps.
- Reuse, patch, or creation decisions must be explicit.
- Every product screen must remain aligned with `app-ui`, `app-flows`, product scope, and its implemented backend contract.
- A slice cannot be marked done with a fake repository unless it is explicitly static and needs no backend.
