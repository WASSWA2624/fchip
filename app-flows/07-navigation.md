# 07 — Navigation and complete journeys

SoT: `.cursor/app-write-up.mdc` §2, §4, §6, §7. Screen routes and role metadata are generated into `app-ui/**/screen.json`.

## Entry and access

```text
Splash → Sign in / Create account → Consent → Choose workspace → Role home
```

- Existing users: `splash → login → role-surface-picker`.
- New users: `splash → create-account → consent-first-onboarding → role-surface-picker`.
- Offline PIN unlocks saved device work; it is not account authentication.
- Unauthorized routes go to `access-denied`; unknown routes go to `not-found`.
- Navigation only shows workspaces and actions allowed by the user’s role, grants, subscription, and catchment.

## Primary role homes

- CHW/VHT → `01-chw-vht-mobile/worklist-home`
- Caregiver → `02-community-caregiver/my-household`
- Facility → `06-facility-dashboard/overview`
- District/MoH → `10-district-moh/population-map`
- NGO/partner → `11-ngo-partner/programme-monitoring`
- Admin → `13-admin-consent/org-catchment`
- Intelligence operator → `09-intelligence/ingest-pipeline`
- Research → `12-research-exports/evidence-catalog`
- Insurance → `23-insurance-insights/prevention-overview`
- Feeder roles → their module home or first capture screen

## CHW visit and referral loop

```text
Worklist → Household visit → Symptoms & vitals → Maternal/child
→ Visit saved → Create referral → Referral status
→ Facility referral queue → Referral detail → Outcome feedback
→ CHW worklist + cascade metrics
```

Saving locally never depends on a live connection. Pending, syncing, synced, failed, and conflict states preserve the record.

## Disease-surveillance loop

```text
CHW fever signal → Ingest → Climate fusion + GIS + AI risk
→ District warning → Deploy response → Pharmacy pre-stock
→ Outreach result → Cascade metrics → Learn
```

## Research export

```text
Evidence catalog → Export request → Privacy/ethics review
→ Pending or denied → Approved anonymised download
```

Raw PHI is never exported.

## Navigation rules

1. Each role has one home and no more than four primary destinations.
2. Task steps are child routes, not extra tabs.
3. “More” opens shared notifications/preferences or less-used granted modules.
4. Mobile uses bottom navigation; tablet uses a compact rail; desktop uses side navigation.
5. Every primary CTA has a declared destination in `screen.json`.
6. Every async screen declares supported loading, empty, error, success, forbidden, offline, or conflict states as relevant.
