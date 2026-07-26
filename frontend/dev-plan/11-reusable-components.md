# 11 - Reusable Components
Build shared UI only where repeated behavior or styling justifies abstraction.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`components.mdc`](../.cursor/components.mdc), [`ui-patterns.mdc`](../.cursor/ui-patterns.mdc), [`design-system.mdc`](../.cursor/design-system.mdc), [`accessibility.mdc`](../.cursor/accessibility.mdc), and [`layouts.mdc`](../.cursor/layouts.mdc).

## Implementation
1. Inventory `app-ui/00-shared/components/README.md`, each `component.json`, and the six light/dark responsive specimens before creating the Flutter catalog.
2. Implement foundational buttons, fields, dialogs, async states, navigation, and layout helpers first; add the remaining catalog component when its first product screen needs it.
3. Form, select, radio, checkbox, switch, or date wrappers may be added only when demonstrated or required.
4. Relevant components must support loading, disabled, error, focus, hover, and accessibility states.
5. Add widget and relevant golden tests for important components.
6. Duplicate components must not solve the same responsibility.

## Acceptance Criteria
- Components must be localized and theme-aware.
- Components must support touch, mouse, keyboard, and screen readers.
- A small showcase may exist only when useful for validation.
