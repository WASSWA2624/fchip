# Implementation prompt — shared component `02-buttons/02-secondary-cta`

> Paste this whole file into an agent session when implementing this reusable component.

## Mission

Implement **Secondary CTA** as a single reusable Flutter widget in `frontend/lib/shared/components`, matching the six specimens, with no feature business logic, so every FCHIP screen can compose it safely.

_Purpose: Alternate / cancel action_

## Identity

| Field | Value |
| --- | --- |
| Kind | Shared component |
| Category | `02-buttons` |
| Slug | `02-secondary-cta` |
| Suggested Dart name | `App02SecondaryCta` |
| Used by | `forms`, `dialogs` |
| Breakpoints | `mobile`, `tablet`, `desktop` |
| Themes | `light`, `dark`, `system` |

## Visual sources

Folder: `app-ui/00-shared/components/02-buttons/02-secondary-cta/`

- `desktop-dark.png`
- `desktop.png`
- `mobile-dark.png`
- `mobile.png`
- `tablet-dark.png`
- `tablet.png`

Also read:

- `app-ui/00-shared/components/README.md`
- `app-ui/00-shared/tokens.json`
- `component.json` in this folder

## Target code locations

| Layer | Path |
| --- | --- |
| Widget | `frontend/lib/shared/components/02-buttons/app_02_secondary_cta.dart` |
| Barrel / exports | `frontend/lib/shared/components/` |
| Widget tests | `frontend/test/shared/components/02-buttons/app_02_secondary_cta_test.dart` |
| Goldens | `frontend/test/shared/components/02-buttons/goldens/` |

If an equivalent shared widget already exists under another name, **extend or rename in place** — do not create a second component for the same job (`frontend/.cursor/components.mdc`).

## Applicable rules

### Product & delivery

- `.cursor/mandatories.mdc`
- `.cursor/app-write-up.mdc`
- `.cursor/index.mdc`
- `frontend/.cursor/index.mdc`
- `frontend/.cursor/project_structure.mdc`
- `frontend/.cursor/architecture.mdc`
- `frontend/.cursor/checklists.mdc`

### UI kit

- `frontend/.cursor/design-system.mdc`
- `frontend/.cursor/components.mdc`
- `frontend/.cursor/layouts.mdc`
- `frontend/.cursor/ui-patterns.mdc`
- `frontend/.cursor/ui-workspace.mdc`
- `frontend/.cursor/ui-feedback.mdc`
- `frontend/.cursor/navigation.mdc`
- `frontend/.cursor/accessibility.mdc`
- `frontend/.cursor/assets_branding.mdc`

### Quality & a11y

- `frontend/.cursor/localization_i18n.mdc`
- `frontend/.cursor/validation.mdc`
- `frontend/.cursor/error_handling.mdc`
- `frontend/.cursor/testing.mdc`
- `frontend/.cursor/performance.mdc`
- `frontend/.cursor/observability.mdc`
- `frontend/.cursor/coding_conventions.mdc`
- `frontend/.cursor/multi_platform_input.mdc`
- `frontend/.cursor/platform_guidelines.mdc`

### Permissions note

- Unauthorized actions that wrap this component must not render the action (`frontend/.cursor/permissions.mdc`).
- Components must not embed RBAC logic beyond accepting an `enabled` / visibility flag from the caller.

## Actionable implementation plan

1. Inventory existing `frontend/lib/shared/components/**` for the same job; reuse or patch first.
2. Read all specimens and list variants (size density, emphasis, icon presence, destructive vs normal, dense tablet vs phone).
3. Design a small public API: required data props, optional style flags, callbacks (`onPressed`, `onSelected`), and localization inputs (pass already-localized `String`s or `Text` widgets — do not hard-code copy inside the component unless it is brand chrome owned by the kit).
4. Implement `App02SecondaryCta` with:
   - `const` constructor where possible
   - Design tokens only (no raw colors/spacings)
   - Responsive sizing via `frontend/lib/core/responsive/` helpers
   - States: enabled, disabled, loading, error, focused, empty as relevant
   - Semantics / accessibility labels
5. Export from the shared components barrel.
6. Add widget + golden tests for mobile/tablet/desktop × light/dark using the specimens as visual references (not as image assets inside the widget).
7. Replace any feature-local duplicates once this ships.

## Reusability checklist

- [ ] Lives only under `frontend/lib/shared/components/`
- [ ] Contains **no** feature repository calls, routing, or domain rules
- [ ] One component job → one implementation
- [ ] Works in light and dark; scales across breakpoints
- [ ] All user-facing strings come from callers or brand constants already localized
- [ ] Entities shown inside the component use `human_friendly_id` labels only when data-bound

## Backend linkage

Shared presentational components normally need **no backend**. If this component displays live data (status, sync, risk, feeder health), the **screen** that hosts it owns the repository, providers, and pairing — keep this widget dumb and props-driven.

## Done when

- Specimens matched across breakpoints/themes
- Catalog README entry remains accurate
- Tests/goldens pass
- No second parallel widget exists for the same job

## Do not

- Put this under `frontend/lib/features/**`
- Hard-code feature colors or copy
- Embed API clients or Riverpod notifiers inside the widget
- Copy PNG files into the widget tree
