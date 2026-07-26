# 00-shared

Source: `app-flows/` + `.cursor/app-write-up.mdc` (especially §2, §4, §6, §7).

| Screen | Layout (kit) | State | Light | Dark |
| --- | --- | --- | --- | --- |
| FCHIP (`splash`) | `01-auth-centered-card` | `default` | [mobile](splash/mobile.png) · [tablet](splash/tablet.png) · [desktop](splash/desktop.png) | [mobile](splash/mobile-dark.png) · [tablet](splash/tablet-dark.png) · [desktop](splash/desktop-dark.png) |
| Create account (`create-account`) | `01-auth-centered-card` | `default` | [mobile](create-account/mobile.png) · [tablet](create-account/tablet.png) · [desktop](create-account/desktop.png) | [mobile](create-account/mobile-dark.png) · [tablet](create-account/tablet-dark.png) · [desktop](create-account/desktop-dark.png) |
| Sign in (`login`) | `01-auth-centered-card` | `default` | [mobile](login/mobile.png) · [tablet](login/tablet.png) · [desktop](login/desktop.png) | [mobile](login/mobile-dark.png) · [tablet](login/tablet-dark.png) · [desktop](login/desktop-dark.png) |
| Reset password (`forgot-password`) | `01-auth-centered-card` | `default` | [mobile](forgot-password/mobile.png) · [tablet](forgot-password/tablet.png) · [desktop](forgot-password/desktop.png) | [mobile](forgot-password/mobile-dark.png) · [tablet](forgot-password/tablet-dark.png) · [desktop](forgot-password/desktop-dark.png) |
| Consent first (`consent-first-onboarding`) | `01-auth-centered-card` | `default` | [mobile](consent-first-onboarding/mobile.png) · [tablet](consent-first-onboarding/tablet.png) · [desktop](consent-first-onboarding/desktop.png) | [mobile](consent-first-onboarding/mobile-dark.png) · [tablet](consent-first-onboarding/tablet-dark.png) · [desktop](consent-first-onboarding/desktop-dark.png) |
| Offline PIN (`offline-pin-lock`) | `01-auth-centered-card` | `offline` | [mobile](offline-pin-lock/mobile.png) · [tablet](offline-pin-lock/tablet.png) · [desktop](offline-pin-lock/desktop.png) | [mobile](offline-pin-lock/mobile-dark.png) · [tablet](offline-pin-lock/tablet-dark.png) · [desktop](offline-pin-lock/desktop-dark.png) |
| Session locked (`session-locked`) | `01-auth-centered-card` | `default` | [mobile](session-locked/mobile.png) · [tablet](session-locked/tablet.png) · [desktop](session-locked/desktop.png) | [mobile](session-locked/mobile-dark.png) · [tablet](session-locked/tablet-dark.png) · [desktop](session-locked/desktop-dark.png) |
| Choose your workspace (`role-surface-picker`) | `02-list-worklist` | `default` | [mobile](role-surface-picker/mobile.png) · [tablet](role-surface-picker/tablet.png) · [desktop](role-surface-picker/desktop.png) | [mobile](role-surface-picker/mobile-dark.png) · [tablet](role-surface-picker/tablet-dark.png) · [desktop](role-surface-picker/desktop-dark.png) |
| Notifications (`notifications-center`) | `02-list-worklist` | `default` | [mobile](notifications-center/mobile.png) · [tablet](notifications-center/tablet.png) · [desktop](notifications-center/desktop.png) | [mobile](notifications-center/mobile-dark.png) · [tablet](notifications-center/tablet-dark.png) · [desktop](notifications-center/desktop-dark.png) |
| Access denied (`access-denied`) | `07-empty-state-shell` | `forbidden` | [mobile](access-denied/mobile.png) · [tablet](access-denied/tablet.png) · [desktop](access-denied/desktop.png) | [mobile](access-denied/mobile-dark.png) · [tablet](access-denied/tablet-dark.png) · [desktop](access-denied/desktop-dark.png) |
| Page not found (`not-found`) | `07-empty-state-shell` | `error` | [mobile](not-found/mobile.png) · [tablet](not-found/tablet.png) · [desktop](not-found/desktop.png) | [mobile](not-found/mobile-dark.png) · [tablet](not-found/tablet-dark.png) · [desktop](not-found/desktop-dark.png) |
| Language & appearance (`preferences`) | `08-settings-admin` | `default` | [mobile](preferences/mobile.png) · [tablet](preferences/tablet.png) · [desktop](preferences/desktop.png) | [mobile](preferences/mobile-dark.png) · [tablet](preferences/tablet-dark.png) · [desktop](preferences/desktop-dark.png) |

## Reusable kit

Shared pieces for every module screen:

- **[components/](components/README.md)** — 42 UI components (brand, buttons, chips, cards, forms, navigation, feedback, data-display)
- **[layouts/](layouts/README.md)** — 17 page layouts (auth, field shells, dashboards, forms, maps, queues, feeders, admin)

Each item ships **mobile · tablet · desktop** specimens.

Regenerate: `python app-ui/00-shared/generate_kit.py`
