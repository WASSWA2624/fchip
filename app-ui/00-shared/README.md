# 00-shared

Source: `app-flows/` + `.cursor/app-write-up.mdc` (especially §2, §4, §6, §7).

| Screen | Layout (kit) | State | Light | Dark |
| --- | --- | --- | --- | --- |
| FCHIP (`01-splash`) | `01-auth-centered-card` | `default` | [mobile](01-splash/mobile.png) · [tablet](01-splash/tablet.png) · [desktop](01-splash/desktop.png) | [mobile](01-splash/mobile-dark.png) · [tablet](01-splash/tablet-dark.png) · [desktop](01-splash/desktop-dark.png) |
| Create account (`02-create-account`) | `01-auth-centered-card` | `default` | [mobile](02-create-account/mobile.png) · [tablet](02-create-account/tablet.png) · [desktop](02-create-account/desktop.png) | [mobile](02-create-account/mobile-dark.png) · [tablet](02-create-account/tablet-dark.png) · [desktop](02-create-account/desktop-dark.png) |
| Sign in (`03-login`) | `01-auth-centered-card` | `default` | [mobile](03-login/mobile.png) · [tablet](03-login/tablet.png) · [desktop](03-login/desktop.png) | [mobile](03-login/mobile-dark.png) · [tablet](03-login/tablet-dark.png) · [desktop](03-login/desktop-dark.png) |
| Reset password (`04-forgot-password`) | `01-auth-centered-card` | `default` | [mobile](04-forgot-password/mobile.png) · [tablet](04-forgot-password/tablet.png) · [desktop](04-forgot-password/desktop.png) | [mobile](04-forgot-password/mobile-dark.png) · [tablet](04-forgot-password/tablet-dark.png) · [desktop](04-forgot-password/desktop-dark.png) |
| Consent first (`05-consent-first-onboarding`) | `01-auth-centered-card` | `default` | [mobile](05-consent-first-onboarding/mobile.png) · [tablet](05-consent-first-onboarding/tablet.png) · [desktop](05-consent-first-onboarding/desktop.png) | [mobile](05-consent-first-onboarding/mobile-dark.png) · [tablet](05-consent-first-onboarding/tablet-dark.png) · [desktop](05-consent-first-onboarding/desktop-dark.png) |
| Offline PIN (`06-offline-pin-lock`) | `01-auth-centered-card` | `offline` | [mobile](06-offline-pin-lock/mobile.png) · [tablet](06-offline-pin-lock/tablet.png) · [desktop](06-offline-pin-lock/desktop.png) | [mobile](06-offline-pin-lock/mobile-dark.png) · [tablet](06-offline-pin-lock/tablet-dark.png) · [desktop](06-offline-pin-lock/desktop-dark.png) |
| Session locked (`07-session-locked`) | `01-auth-centered-card` | `default` | [mobile](07-session-locked/mobile.png) · [tablet](07-session-locked/tablet.png) · [desktop](07-session-locked/desktop.png) | [mobile](07-session-locked/mobile-dark.png) · [tablet](07-session-locked/tablet-dark.png) · [desktop](07-session-locked/desktop-dark.png) |
| Choose your workspace (`08-role-surface-picker`) | `02-list-worklist` | `default` | [mobile](08-role-surface-picker/mobile.png) · [tablet](08-role-surface-picker/tablet.png) · [desktop](08-role-surface-picker/desktop.png) | [mobile](08-role-surface-picker/mobile-dark.png) · [tablet](08-role-surface-picker/tablet-dark.png) · [desktop](08-role-surface-picker/desktop-dark.png) |
| Notifications (`09-notifications-center`) | `02-list-worklist` | `default` | [mobile](09-notifications-center/mobile.png) · [tablet](09-notifications-center/tablet.png) · [desktop](09-notifications-center/desktop.png) | [mobile](09-notifications-center/mobile-dark.png) · [tablet](09-notifications-center/tablet-dark.png) · [desktop](09-notifications-center/desktop-dark.png) |
| Access denied (`10-access-denied`) | `07-empty-state-shell` | `forbidden` | [mobile](10-access-denied/mobile.png) · [tablet](10-access-denied/tablet.png) · [desktop](10-access-denied/desktop.png) | [mobile](10-access-denied/mobile-dark.png) · [tablet](10-access-denied/tablet-dark.png) · [desktop](10-access-denied/desktop-dark.png) |
| Page not found (`11-not-found`) | `07-empty-state-shell` | `error` | [mobile](11-not-found/mobile.png) · [tablet](11-not-found/tablet.png) · [desktop](11-not-found/desktop.png) | [mobile](11-not-found/mobile-dark.png) · [tablet](11-not-found/tablet-dark.png) · [desktop](11-not-found/desktop-dark.png) |
| Language & appearance (`12-preferences`) | `08-settings-admin` | `default` | [mobile](12-preferences/mobile.png) · [tablet](12-preferences/tablet.png) · [desktop](12-preferences/desktop.png) | [mobile](12-preferences/mobile-dark.png) · [tablet](12-preferences/tablet-dark.png) · [desktop](12-preferences/desktop-dark.png) |

## Reusable kit

Shared pieces for every module screen:

- **[components/](components/README.md)** — 42 UI components (brand, buttons, chips, cards, forms, navigation, feedback, data-display)
- **[layouts/](layouts/README.md)** — 17 page layouts (auth, field shells, dashboards, forms, maps, queues, feeders, admin)

Each item ships **mobile · tablet · desktop** specimens.

Regenerate: `python app-ui/00-shared/generate_kit.py`
