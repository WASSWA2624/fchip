# 09 - Theme System
Provide balanced light, dark, and system themes through shared Material tokens.

## Applicable Rules
You must follow [`00-execution-policy.md`](./00-execution-policy.md), [`design-system.mdc`](../.cursor/design-system.mdc), [`assets_branding.mdc`](../.cursor/assets_branding.mdc), [`accessibility.mdc`](../.cursor/accessibility.mdc), and [`localization_i18n.mdc`](../.cursor/localization_i18n.mdc).

## Implementation
1. Generate or map Material 3 `AppTheme.light` and `AppTheme.dark` from `app-ui/00-shared/tokens.json`; FCHIP health teal (`#006D77`) is the primary baseline.
2. Define `AppThemeTokens` for spacing, radius, sizing, and optional status colors.
3. Implement `themeModeControllerProvider`; persistence may store only non-sensitive preferences.
4. Buttons, icons, fields, cards, dialogs, and navigation should avoid excessive padding or rounding.
5. Repeated raw colors, spacing, and shapes must not remain in starter UI.
6. Add theme smoke tests.
7. Replace legacy azure/HIS palette values when they differ from the FCHIP tokens; do not maintain two competing theme systems.

## Acceptance Criteria
- Light mode must be the default.
- System and dark modes must work.
- Shared components must use theme tokens.
- Theme-aware starter UI and its provider/controller must be present.
- Token checks must prove light/dark values remain aligned with `app-ui/00-shared/tokens.json`.
