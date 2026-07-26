# 00-shared

Source: `app-flows/04-modules.md` + `.cursor/app-write-up.mdc`.

| Screen | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| FCHIP (`splash`) | [mobile](splash/mobile.png) | [tablet](splash/tablet.png) | [desktop](splash/desktop.png) |
| Sign in (`login`) | [mobile](login/mobile.png) | [tablet](login/tablet.png) | [desktop](login/desktop.png) |
| Choose your workspace (`role-surface-picker`) | [mobile](role-surface-picker/mobile.png) | [tablet](role-surface-picker/tablet.png) | [desktop](role-surface-picker/desktop.png) |
| Notifications (`notifications-center`) | [mobile](notifications-center/mobile.png) | [tablet](notifications-center/tablet.png) | [desktop](notifications-center/desktop.png) |

## Reusable kit

Shared pieces for every module screen:

- **[components/](components/README.md)** — 39 UI components (brand, buttons, chips, cards, forms, navigation, feedback, data-display)
- **[layouts/](layouts/README.md)** — 15 page layouts (auth, field shells, dashboards, forms, maps, queues, feeders, admin)

Each item ships **mobile · tablet · desktop** specimens.

Regenerate: `python app-ui/00-shared/generate_kit.py`
