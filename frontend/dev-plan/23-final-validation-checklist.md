# 23 - Foundation Validation Checklist
Verify the shared foundation before product vertical slices begin.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`checklists.mdc`](../.cursor/checklists.mdc), [`validation-snapshot-2026-05-14.mdc`](../.cursor/reference/validation-snapshot-2026-05-14.mdc), [`scope.mdc`](../.cursor/scope.mdc), and [`ci_cd_quality_gates.mdc`](../.cursor/ci_cd_quality_gates.mdc).

## Validation
1. Confirm all rules are consistent and every plan references relevant rules.
2. Run generation first when used, then:
   ```bash
   flutter pub get
   dart format --set-exit-if-changed .
   flutter analyze
   flutter test
   ```
3. Test `320px` mobile and large desktop layouts, including menu bar and expanded/collapsed side navigation.
4. Confirm fixture-backed API-contract readiness and reusability for step `24`.
5. Confirm the slice registries and tracker are consistent:
   ```bash
   python tool/check_slice_coverage.py
   ```
6. Update `frontend/.cursor/reference/validation-snapshot-2026-05-14.mdc` with actual results.

## Acceptance Criteria
- Steps `00` through `23` must be executable in order.
- The result must be a working reusable foundation.
- Architecture, UI behavior, conventions, and validation results must be deterministic.
- The coverage check must pass so product slices start from an accurate screen inventory.
- This gate does not mean the product is complete; product completion is tracked screen by screen in `slices/chronology.yaml` via steps `24` and `25`, and every screen must ship with its backend.
