# FCHIP app-ui

Visual directory of **proposed** FCHIP screens from `.cursor/app-write-up.mdc` and `app-flows/`.
Not generated from `frontend/` code.

**127 screens** × mobile / tablet / desktop × light / dark = **762 mockups**.

Slogan: **Your health, our mission.**

## Breakpoints

| Name | Size |
| --- | --- |
| mobile | 390 × 844 |
| tablet | 768 × 1024 |
| desktop | 1440 × 900 |

Every screen also has a `*-dark.png` system-theme specimen.

## Data feeders covered (SoT §4.2 / app-flows 03)

| Feeder party | Module folder |
| --- | --- |
| CHWs / VHTs | `01-chw-vht-mobile` |
| Patients / caregivers | `09-community-caregiver` |
| Communities · events · dialogues | `22-community-events` (+ needs in `09`) |
| Outreach programmes | `10-outreach-school-health` |
| Schools | `15-schools-health` |
| Hospitals / clinics (manual + share) | `04-facility-dashboard` · `05-referrals-desk` |
| Existing EMR / HMS | `06-emr-connector` |
| Pharmacies / drug shops | `16-pharmacy-outlets` |
| ANC / PNC · immunisation · nutrition | `19-mch-touchpoints` |
| Corporate / workplace wellness | `18-corporate-wellness` |
| Labs / PoC | `17-labs-poc` |
| Gericare / NCD cohorts | `20-ncd-gericare` |
| CHIS / livelihoods (optional) | `13-chis-livelihoods` |
| HMIS / DHIS2 (where approved) | `21-hmis-dhis2` |
| Research / NGO M&E uploads | `14-ngo-partner` · `23-research-exports` |
| Climate API | `07-climate-feeds` (+ fusion in `02`) |

## Consumer surfaces (§7)

| Customer | Module |
| --- | --- |
| CHW / VHT | `01-chw-vht-mobile` |
| Caregivers (optional) | `09-community-caregiver` |
| Medical centres & clinics | `04` · `05` · `06` |
| District health offices | `08-district-moh` |
| Ministries of health (national) | `08-district-moh/05-national-roll-up` (Phase 3) |
| NGOs & partners | `14-ngo-partner` · `03-cascade-metrics` |
| Research institutions | `23-research-exports` |
| Insurance companies | `12-insurance-insights` (prevention only) |

## Split notes

- `10-outreach-school-health` = programme planning; `15-schools-health` = school feeder.
- `04/.../open-referrals` = overview; `05-referrals-desk` = working queue.
- `02-intelligence` = shared stack (incl. clinical support guidance); not district-owned.
- Screens reference kit layouts via `layout` in each `screen.json`.

## Modules

### [00-shared](00-shared/README.md)

- **FCHIP** — `00-shared/01-splash/` ([mobile](00-shared/01-splash/mobile.png) · [tablet](00-shared/01-splash/tablet.png) · [desktop](00-shared/01-splash/desktop.png))
- **Create account** — `00-shared/02-create-account/` ([mobile](00-shared/02-create-account/mobile.png) · [tablet](00-shared/02-create-account/tablet.png) · [desktop](00-shared/02-create-account/desktop.png))
- **Sign in** — `00-shared/03-login/` ([mobile](00-shared/03-login/mobile.png) · [tablet](00-shared/03-login/tablet.png) · [desktop](00-shared/03-login/desktop.png))
- **Reset password** — `00-shared/04-forgot-password/` ([mobile](00-shared/04-forgot-password/mobile.png) · [tablet](00-shared/04-forgot-password/tablet.png) · [desktop](00-shared/04-forgot-password/desktop.png))
- **Consent first** — `00-shared/05-consent-first-onboarding/` ([mobile](00-shared/05-consent-first-onboarding/mobile.png) · [tablet](00-shared/05-consent-first-onboarding/tablet.png) · [desktop](00-shared/05-consent-first-onboarding/desktop.png))
- **Offline PIN** — `00-shared/06-offline-pin-lock/` ([mobile](00-shared/06-offline-pin-lock/mobile.png) · [tablet](00-shared/06-offline-pin-lock/tablet.png) · [desktop](00-shared/06-offline-pin-lock/desktop.png))
- **Session locked** — `00-shared/07-session-locked/` ([mobile](00-shared/07-session-locked/mobile.png) · [tablet](00-shared/07-session-locked/tablet.png) · [desktop](00-shared/07-session-locked/desktop.png))
- **Choose your workspace** — `00-shared/08-role-surface-picker/` ([mobile](00-shared/08-role-surface-picker/mobile.png) · [tablet](00-shared/08-role-surface-picker/tablet.png) · [desktop](00-shared/08-role-surface-picker/desktop.png))
- **Notifications** — `00-shared/09-notifications-center/` ([mobile](00-shared/09-notifications-center/mobile.png) · [tablet](00-shared/09-notifications-center/tablet.png) · [desktop](00-shared/09-notifications-center/desktop.png))
- **Access denied** — `00-shared/10-access-denied/` ([mobile](00-shared/10-access-denied/mobile.png) · [tablet](00-shared/10-access-denied/tablet.png) · [desktop](00-shared/10-access-denied/desktop.png))
- **Page not found** — `00-shared/11-not-found/` ([mobile](00-shared/11-not-found/mobile.png) · [tablet](00-shared/11-not-found/tablet.png) · [desktop](00-shared/11-not-found/desktop.png))
- **Language & appearance** — `00-shared/12-preferences/` ([mobile](00-shared/12-preferences/mobile.png) · [tablet](00-shared/12-preferences/tablet.png) · [desktop](00-shared/12-preferences/desktop.png))

### [01-chw-vht-mobile](01-chw-vht-mobile/README.md)

- **Today’s worklist** — `01-chw-vht-mobile/01-worklist-home/` ([mobile](01-chw-vht-mobile/01-worklist-home/mobile.png) · [tablet](01-chw-vht-mobile/01-worklist-home/tablet.png) · [desktop](01-chw-vht-mobile/01-worklist-home/desktop.png))
- **Today’s worklist** — `01-chw-vht-mobile/02-worklist-empty/` ([mobile](01-chw-vht-mobile/02-worklist-empty/mobile.png) · [tablet](01-chw-vht-mobile/02-worklist-empty/tablet.png) · [desktop](01-chw-vht-mobile/02-worklist-empty/desktop.png))
- **Household visit** — `01-chw-vht-mobile/04-household-visit-form/` ([mobile](01-chw-vht-mobile/04-household-visit-form/mobile.png) · [tablet](01-chw-vht-mobile/04-household-visit-form/tablet.png) · [desktop](01-chw-vht-mobile/04-household-visit-form/desktop.png))
- **Symptoms & vitals** — `01-chw-vht-mobile/05-symptoms-vitals/` ([mobile](01-chw-vht-mobile/05-symptoms-vitals/mobile.png) · [tablet](01-chw-vht-mobile/05-symptoms-vitals/tablet.png) · [desktop](01-chw-vht-mobile/05-symptoms-vitals/desktop.png))
- **Maternal / child** — `01-chw-vht-mobile/06-maternal-child-indicators/` ([mobile](01-chw-vht-mobile/06-maternal-child-indicators/mobile.png) · [tablet](01-chw-vht-mobile/06-maternal-child-indicators/tablet.png) · [desktop](01-chw-vht-mobile/06-maternal-child-indicators/desktop.png))
- **Create referral** — `01-chw-vht-mobile/08-create-referral/` ([mobile](01-chw-vht-mobile/08-create-referral/mobile.png) · [tablet](01-chw-vht-mobile/08-create-referral/tablet.png) · [desktop](01-chw-vht-mobile/08-create-referral/desktop.png))
- **Alerts inbox** — `01-chw-vht-mobile/10-alerts-inbox/` ([mobile](01-chw-vht-mobile/10-alerts-inbox/mobile.png) · [tablet](01-chw-vht-mobile/10-alerts-inbox/tablet.png) · [desktop](01-chw-vht-mobile/10-alerts-inbox/desktop.png))
- **Act on alert** — `01-chw-vht-mobile/11-alert-follow-up/` ([mobile](01-chw-vht-mobile/11-alert-follow-up/mobile.png) · [tablet](01-chw-vht-mobile/11-alert-follow-up/tablet.png) · [desktop](01-chw-vht-mobile/11-alert-follow-up/desktop.png))
- **Sync status** — `01-chw-vht-mobile/12-sync-status/` ([mobile](01-chw-vht-mobile/12-sync-status/mobile.png) · [tablet](01-chw-vht-mobile/12-sync-status/tablet.png) · [desktop](01-chw-vht-mobile/12-sync-status/desktop.png))
- **Sync failed** — `01-chw-vht-mobile/13-sync-failed/` ([mobile](01-chw-vht-mobile/13-sync-failed/mobile.png) · [tablet](01-chw-vht-mobile/13-sync-failed/tablet.png) · [desktop](01-chw-vht-mobile/13-sync-failed/desktop.png))
- **Today’s worklist** — `01-chw-vht-mobile/03-worklist-loading/` ([mobile](01-chw-vht-mobile/03-worklist-loading/mobile.png) · [tablet](01-chw-vht-mobile/03-worklist-loading/tablet.png) · [desktop](01-chw-vht-mobile/03-worklist-loading/desktop.png))
- **Visit saved** — `01-chw-vht-mobile/07-visit-saved/` ([mobile](01-chw-vht-mobile/07-visit-saved/mobile.png) · [tablet](01-chw-vht-mobile/07-visit-saved/tablet.png) · [desktop](01-chw-vht-mobile/07-visit-saved/desktop.png))
- **Referral sent** — `01-chw-vht-mobile/09-referral-status/` ([mobile](01-chw-vht-mobile/09-referral-status/mobile.png) · [tablet](01-chw-vht-mobile/09-referral-status/tablet.png) · [desktop](01-chw-vht-mobile/09-referral-status/desktop.png))
- **Review sync conflict** — `01-chw-vht-mobile/14-sync-conflict/` ([mobile](01-chw-vht-mobile/14-sync-conflict/mobile.png) · [tablet](01-chw-vht-mobile/14-sync-conflict/tablet.png) · [desktop](01-chw-vht-mobile/14-sync-conflict/desktop.png))

### [02-intelligence](02-intelligence/README.md)

- **Ingest & sync** — `02-intelligence/01-ingest-pipeline/` ([mobile](02-intelligence/01-ingest-pipeline/mobile.png) · [tablet](02-intelligence/01-ingest-pipeline/tablet.png) · [desktop](02-intelligence/01-ingest-pipeline/desktop.png))
- **AI / predictive** — `02-intelligence/05-ai-risk-scores/` ([mobile](02-intelligence/05-ai-risk-scores/mobile.png) · [tablet](02-intelligence/05-ai-risk-scores/tablet.png) · [desktop](02-intelligence/05-ai-risk-scores/desktop.png))
- **GIS maps** — `02-intelligence/03-gis-explorer/` ([mobile](02-intelligence/03-gis-explorer/mobile.png) · [tablet](02-intelligence/03-gis-explorer/tablet.png) · [desktop](02-intelligence/03-gis-explorer/desktop.png))
- **Climate fusion** — `02-intelligence/04-climate-fusion/` ([mobile](02-intelligence/04-climate-fusion/mobile.png) · [tablet](02-intelligence/04-climate-fusion/tablet.png) · [desktop](02-intelligence/04-climate-fusion/desktop.png))
- **Clinical support guidance** — `02-intelligence/07-clinical-support-guidance/` ([mobile](02-intelligence/07-clinical-support-guidance/mobile.png) · [tablet](02-intelligence/07-clinical-support-guidance/tablet.png) · [desktop](02-intelligence/07-clinical-support-guidance/desktop.png))
- **Alerts & worklists engine** — `02-intelligence/06-alerts-worklists-engine/` ([mobile](02-intelligence/06-alerts-worklists-engine/mobile.png) · [tablet](02-intelligence/06-alerts-worklists-engine/tablet.png) · [desktop](02-intelligence/06-alerts-worklists-engine/desktop.png))
- **Feeder health board** — `02-intelligence/02-feeder-health-board/` ([mobile](02-intelligence/02-feeder-health-board/mobile.png) · [tablet](02-intelligence/02-feeder-health-board/tablet.png) · [desktop](02-intelligence/02-feeder-health-board/desktop.png))

### [03-cascade-metrics](03-cascade-metrics/README.md)

- **Cascade metrics** — `03-cascade-metrics/01-indicators-overview/` ([mobile](03-cascade-metrics/01-indicators-overview/mobile.png) · [tablet](03-cascade-metrics/01-indicators-overview/tablet.png) · [desktop](03-cascade-metrics/01-indicators-overview/desktop.png))
- **Gap detection** — `03-cascade-metrics/02-gap-detection/` ([mobile](03-cascade-metrics/02-gap-detection/mobile.png) · [tablet](03-cascade-metrics/02-gap-detection/tablet.png) · [desktop](03-cascade-metrics/02-gap-detection/desktop.png))
- **Partner reports** — `03-cascade-metrics/03-partner-reports/` ([mobile](03-cascade-metrics/03-partner-reports/mobile.png) · [tablet](03-cascade-metrics/03-partner-reports/tablet.png) · [desktop](03-cascade-metrics/03-partner-reports/desktop.png))

### [04-facility-dashboard](04-facility-dashboard/README.md)

- **Facility overview** — `04-facility-dashboard/01-overview/` ([mobile](04-facility-dashboard/01-overview/mobile.png) · [tablet](04-facility-dashboard/01-overview/tablet.png) · [desktop](04-facility-dashboard/01-overview/desktop.png))
- **Catchment map** — `04-facility-dashboard/02-catchment-map/` ([mobile](04-facility-dashboard/02-catchment-map/mobile.png) · [tablet](04-facility-dashboard/02-catchment-map/tablet.png) · [desktop](04-facility-dashboard/02-catchment-map/desktop.png))
- **Referral summary** — `04-facility-dashboard/03-open-referrals/` ([mobile](04-facility-dashboard/03-open-referrals/mobile.png) · [tablet](04-facility-dashboard/03-open-referrals/tablet.png) · [desktop](04-facility-dashboard/03-open-referrals/desktop.png))
- **Stock signal** — `04-facility-dashboard/04-stock-signal/` ([mobile](04-facility-dashboard/04-stock-signal/mobile.png) · [tablet](04-facility-dashboard/04-stock-signal/tablet.png) · [desktop](04-facility-dashboard/04-stock-signal/desktop.png))
- **Medicine demand forecast** — `04-facility-dashboard/08-medicine-demand-forecast/` ([mobile](04-facility-dashboard/08-medicine-demand-forecast/mobile.png) · [tablet](04-facility-dashboard/08-medicine-demand-forecast/tablet.png) · [desktop](04-facility-dashboard/08-medicine-demand-forecast/desktop.png))
- **Outreach priorities** — `04-facility-dashboard/05-outreach-priorities/` ([mobile](04-facility-dashboard/05-outreach-priorities/mobile.png) · [tablet](04-facility-dashboard/05-outreach-priorities/tablet.png) · [desktop](04-facility-dashboard/05-outreach-priorities/desktop.png))
- **Clinical share confirm** — `04-facility-dashboard/06-clinical-share-confirm/` ([mobile](04-facility-dashboard/06-clinical-share-confirm/mobile.png) · [tablet](04-facility-dashboard/06-clinical-share-confirm/tablet.png) · [desktop](04-facility-dashboard/06-clinical-share-confirm/desktop.png))
- **Manual case signal** — `04-facility-dashboard/07-manual-case-signal/` ([mobile](04-facility-dashboard/07-manual-case-signal/mobile.png) · [tablet](04-facility-dashboard/07-manual-case-signal/tablet.png) · [desktop](04-facility-dashboard/07-manual-case-signal/desktop.png))

### [05-referrals-desk](05-referrals-desk/README.md)

- **Referrals desk** — `05-referrals-desk/01-referral-queue/` ([mobile](05-referrals-desk/01-referral-queue/mobile.png) · [tablet](05-referrals-desk/01-referral-queue/tablet.png) · [desktop](05-referrals-desk/01-referral-queue/desktop.png))
- **Referrals desk** — `05-referrals-desk/01-referral-queue-empty/` ([mobile](05-referrals-desk/01-referral-queue-empty/mobile.png) · [tablet](05-referrals-desk/01-referral-queue-empty/tablet.png) · [desktop](05-referrals-desk/01-referral-queue-empty/desktop.png))
- **Referral detail** — `05-referrals-desk/03-referral-detail/` ([mobile](05-referrals-desk/03-referral-detail/mobile.png) · [tablet](05-referrals-desk/03-referral-detail/tablet.png) · [desktop](05-referrals-desk/03-referral-detail/desktop.png))
- **Outcome feedback** — `05-referrals-desk/04-outcome-feedback/` ([mobile](05-referrals-desk/04-outcome-feedback/mobile.png) · [tablet](05-referrals-desk/04-outcome-feedback/tablet.png) · [desktop](05-referrals-desk/04-outcome-feedback/desktop.png))

### [06-emr-connector](06-emr-connector/README.md)

- **EMR / HMS connector** — `06-emr-connector/01-connector-status/` ([mobile](06-emr-connector/01-connector-status/mobile.png) · [tablet](06-emr-connector/01-connector-status/tablet.png) · [desktop](06-emr-connector/01-connector-status/desktop.png))
- **EMR / HMS connector** — `06-emr-connector/02-connector-degraded/` ([mobile](06-emr-connector/02-connector-degraded/mobile.png) · [tablet](06-emr-connector/02-connector-degraded/tablet.png) · [desktop](06-emr-connector/02-connector-degraded/desktop.png))
- **API scopes setup** — `06-emr-connector/03-api-scopes-setup/` ([mobile](06-emr-connector/03-api-scopes-setup/mobile.png) · [tablet](06-emr-connector/03-api-scopes-setup/tablet.png) · [desktop](06-emr-connector/03-api-scopes-setup/desktop.png))
- **Push event log** — `06-emr-connector/04-push-event-log/` ([mobile](06-emr-connector/04-push-event-log/mobile.png) · [tablet](06-emr-connector/04-push-event-log/tablet.png) · [desktop](06-emr-connector/04-push-event-log/desktop.png))
- **Facility onboarding** — `06-emr-connector/05-facility-onboarding/` ([mobile](06-emr-connector/05-facility-onboarding/mobile.png) · [tablet](06-emr-connector/05-facility-onboarding/tablet.png) · [desktop](06-emr-connector/05-facility-onboarding/desktop.png))

### [07-climate-feeds](07-climate-feeds/README.md)

- **Climate feeds home** — `07-climate-feeds/01-climate-home/` ([mobile](07-climate-feeds/01-climate-home/mobile.png) · [tablet](07-climate-feeds/01-climate-home/tablet.png) · [desktop](07-climate-feeds/01-climate-home/desktop.png))
- **Rainfall & temperature** — `07-climate-feeds/02-rainfall-temperature/` ([mobile](07-climate-feeds/02-rainfall-temperature/mobile.png) · [tablet](07-climate-feeds/02-rainfall-temperature/tablet.png) · [desktop](07-climate-feeds/02-rainfall-temperature/desktop.png))
- **Extremes · flood · heat** — `07-climate-feeds/03-extremes-flood-heat/` ([mobile](07-climate-feeds/03-extremes-flood-heat/mobile.png) · [tablet](07-climate-feeds/03-extremes-flood-heat/tablet.png) · [desktop](07-climate-feeds/03-extremes-flood-heat/desktop.png))
- **Feed config & audit** — `07-climate-feeds/04-feed-config-audit/` ([mobile](07-climate-feeds/04-feed-config-audit/mobile.png) · [tablet](07-climate-feeds/04-feed-config-audit/tablet.png) · [desktop](07-climate-feeds/04-feed-config-audit/desktop.png))

### [08-district-moh](08-district-moh/README.md)

- **Population map** — `08-district-moh/01-population-map/` ([mobile](08-district-moh/01-population-map/mobile.png) · [tablet](08-district-moh/01-population-map/tablet.png) · [desktop](08-district-moh/01-population-map/desktop.png))
- **Early warnings** — `08-district-moh/02-early-warnings/` ([mobile](08-district-moh/02-early-warnings/mobile.png) · [tablet](08-district-moh/02-early-warnings/tablet.png) · [desktop](08-district-moh/02-early-warnings/desktop.png))
- **Deploy action** — `08-district-moh/03-action-deploy/` ([mobile](08-district-moh/03-action-deploy/mobile.png) · [tablet](08-district-moh/03-action-deploy/tablet.png) · [desktop](08-district-moh/03-action-deploy/desktop.png))
- **Cascade M&E planning** — `08-district-moh/04-cascade-planning/` ([mobile](08-district-moh/04-cascade-planning/mobile.png) · [tablet](08-district-moh/04-cascade-planning/tablet.png) · [desktop](08-district-moh/04-cascade-planning/desktop.png))
- **MoH national roll-up** — `08-district-moh/05-national-roll-up/` ([mobile](08-district-moh/05-national-roll-up/mobile.png) · [tablet](08-district-moh/05-national-roll-up/tablet.png) · [desktop](08-district-moh/05-national-roll-up/desktop.png))

### [09-community-caregiver](09-community-caregiver/README.md)

- **My household** — `09-community-caregiver/01-my-household/` ([mobile](09-community-caregiver/01-my-household/mobile.png) · [tablet](09-community-caregiver/01-my-household/tablet.png) · [desktop](09-community-caregiver/01-my-household/desktop.png))
- **Self-report** — `09-community-caregiver/02-self-report/` ([mobile](09-community-caregiver/02-self-report/mobile.png) · [tablet](09-community-caregiver/02-self-report/tablet.png) · [desktop](09-community-caregiver/02-self-report/desktop.png))
- **Guidance** — `09-community-caregiver/03-guidance-hints/` ([mobile](09-community-caregiver/03-guidance-hints/mobile.png) · [tablet](09-community-caregiver/03-guidance-hints/tablet.png) · [desktop](09-community-caregiver/03-guidance-hints/desktop.png))
- **Household needs** — `09-community-caregiver/04-household-needs-capture/` ([mobile](09-community-caregiver/04-household-needs-capture/mobile.png) · [tablet](09-community-caregiver/04-household-needs-capture/tablet.png) · [desktop](09-community-caregiver/04-household-needs-capture/desktop.png))

### [10-outreach-school-health](10-outreach-school-health/README.md)

- **Campaign planner** — `10-outreach-school-health/01-campaign-planner/` ([mobile](10-outreach-school-health/01-campaign-planner/mobile.png) · [tablet](10-outreach-school-health/01-campaign-planner/tablet.png) · [desktop](10-outreach-school-health/01-campaign-planner/desktop.png))
- **Session log** — `10-outreach-school-health/02-session-log/` ([mobile](10-outreach-school-health/02-session-log/mobile.png) · [tablet](10-outreach-school-health/02-session-log/tablet.png) · [desktop](10-outreach-school-health/02-session-log/desktop.png))
- **Coverage map** — `10-outreach-school-health/03-coverage-map/` ([mobile](10-outreach-school-health/03-coverage-map/mobile.png) · [tablet](10-outreach-school-health/03-coverage-map/tablet.png) · [desktop](10-outreach-school-health/03-coverage-map/desktop.png))
- **Screening results entry** — `10-outreach-school-health/04-screening-results-entry/` ([mobile](10-outreach-school-health/04-screening-results-entry/mobile.png) · [tablet](10-outreach-school-health/04-screening-results-entry/tablet.png) · [desktop](10-outreach-school-health/04-screening-results-entry/desktop.png))
- **Home-visit batch** — `10-outreach-school-health/05-home-visit-batch-upload/` ([mobile](10-outreach-school-health/05-home-visit-batch-upload/mobile.png) · [tablet](10-outreach-school-health/05-home-visit-batch-upload/tablet.png) · [desktop](10-outreach-school-health/05-home-visit-batch-upload/desktop.png))

### [11-admin-consent](11-admin-consent/README.md)

- **Org · catchment · facilities** — `11-admin-consent/01-org-catchment/` ([mobile](11-admin-consent/01-org-catchment/mobile.png) · [tablet](11-admin-consent/01-org-catchment/tablet.png) · [desktop](11-admin-consent/01-org-catchment/desktop.png))
- **Users & roles** — `11-admin-consent/02-users-roles/` ([mobile](11-admin-consent/02-users-roles/mobile.png) · [tablet](11-admin-consent/02-users-roles/tablet.png) · [desktop](11-admin-consent/02-users-roles/desktop.png))
- **Consent & privacy** — `11-admin-consent/03-consent-privacy/` ([mobile](11-admin-consent/03-consent-privacy/mobile.png) · [tablet](11-admin-consent/03-consent-privacy/tablet.png) · [desktop](11-admin-consent/03-consent-privacy/desktop.png))
- **EMR API access** — `11-admin-consent/04-emr-api-access/` ([mobile](11-admin-consent/04-emr-api-access/mobile.png) · [tablet](11-admin-consent/04-emr-api-access/tablet.png) · [desktop](11-admin-consent/04-emr-api-access/desktop.png))
- **Feeder party registry** — `11-admin-consent/05-feeder-party-registry/` ([mobile](11-admin-consent/05-feeder-party-registry/mobile.png) · [tablet](11-admin-consent/05-feeder-party-registry/tablet.png) · [desktop](11-admin-consent/05-feeder-party-registry/desktop.png))

### [12-insurance-insights](12-insurance-insights/README.md)

- **Prevention overview** — `12-insurance-insights/01-prevention-overview/` ([mobile](12-insurance-insights/01-prevention-overview/mobile.png) · [tablet](12-insurance-insights/01-prevention-overview/tablet.png) · [desktop](12-insurance-insights/01-prevention-overview/desktop.png))
- **Risk cohort insights** — `12-insurance-insights/02-risk-cohort-insights/` ([mobile](12-insurance-insights/02-risk-cohort-insights/mobile.png) · [tablet](12-insurance-insights/02-risk-cohort-insights/tablet.png) · [desktop](12-insurance-insights/02-risk-cohort-insights/desktop.png))
- **Anonymised trends** — `12-insurance-insights/03-anonymised-trends/` ([mobile](12-insurance-insights/03-anonymised-trends/mobile.png) · [tablet](12-insurance-insights/03-anonymised-trends/tablet.png) · [desktop](12-insurance-insights/03-anonymised-trends/desktop.png))
### [13-chis-livelihoods](13-chis-livelihoods/README.md)

- **CHIS enrolment** — `13-chis-livelihoods/01-enrolment/` ([mobile](13-chis-livelihoods/01-enrolment/mobile.png) · [tablet](13-chis-livelihoods/01-enrolment/tablet.png) · [desktop](13-chis-livelihoods/01-enrolment/desktop.png))
- **Contributions** — `13-chis-livelihoods/02-contributions/` ([mobile](13-chis-livelihoods/02-contributions/mobile.png) · [tablet](13-chis-livelihoods/02-contributions/tablet.png) · [desktop](13-chis-livelihoods/02-contributions/desktop.png))
- **Claims / access** — `13-chis-livelihoods/03-claims-access/` ([mobile](13-chis-livelihoods/03-claims-access/mobile.png) · [tablet](13-chis-livelihoods/03-claims-access/tablet.png) · [desktop](13-chis-livelihoods/03-claims-access/desktop.png))
- **IGA participation entry** — `13-chis-livelihoods/04-iga-participation-entry/` ([mobile](13-chis-livelihoods/04-iga-participation-entry/mobile.png) · [tablet](13-chis-livelihoods/04-iga-participation-entry/tablet.png) · [desktop](13-chis-livelihoods/04-iga-participation-entry/desktop.png))

### [14-ngo-partner](14-ngo-partner/README.md)

- **Programme monitoring** — `14-ngo-partner/01-programme-monitoring/` ([mobile](14-ngo-partner/01-programme-monitoring/mobile.png) · [tablet](14-ngo-partner/01-programme-monitoring/tablet.png) · [desktop](14-ngo-partner/01-programme-monitoring/desktop.png))
- **Impact evidence** — `14-ngo-partner/02-impact-evidence/` ([mobile](14-ngo-partner/02-impact-evidence/mobile.png) · [tablet](14-ngo-partner/02-impact-evidence/tablet.png) · [desktop](14-ngo-partner/02-impact-evidence/desktop.png))
- **Training · skills analytics** — `14-ngo-partner/03-training-skills-analytics/` ([mobile](14-ngo-partner/03-training-skills-analytics/mobile.png) · [tablet](14-ngo-partner/03-training-skills-analytics/tablet.png) · [desktop](14-ngo-partner/03-training-skills-analytics/desktop.png))
- **Field dataset upload** — `14-ngo-partner/04-field-dataset-upload/` ([mobile](14-ngo-partner/04-field-dataset-upload/mobile.png) · [tablet](14-ngo-partner/04-field-dataset-upload/tablet.png) · [desktop](14-ngo-partner/04-field-dataset-upload/desktop.png))
- **Partner indicator entry** — `14-ngo-partner/05-partner-indicator-entry/` ([mobile](14-ngo-partner/05-partner-indicator-entry/mobile.png) · [tablet](14-ngo-partner/05-partner-indicator-entry/tablet.png) · [desktop](14-ngo-partner/05-partner-indicator-entry/desktop.png))

### [15-schools-health](15-schools-health/README.md)

- **School health home** — `15-schools-health/01-school-home/` ([mobile](15-schools-health/01-school-home/mobile.png) · [tablet](15-schools-health/01-school-home/tablet.png) · [desktop](15-schools-health/01-school-home/desktop.png))
- **Health education session** — `15-schools-health/02-health-education-session/` ([mobile](15-schools-health/02-health-education-session/mobile.png) · [tablet](15-schools-health/02-health-education-session/tablet.png) · [desktop](15-schools-health/02-health-education-session/desktop.png))
- **Learner screening entry** — `15-schools-health/03-learner-screening-entry/` ([mobile](15-schools-health/03-learner-screening-entry/mobile.png) · [tablet](15-schools-health/03-learner-screening-entry/tablet.png) · [desktop](15-schools-health/03-learner-screening-entry/desktop.png))
- **Absenteeism & wellness** — `15-schools-health/04-absenteeism-wellness/` ([mobile](15-schools-health/04-absenteeism-wellness/mobile.png) · [tablet](15-schools-health/04-absenteeism-wellness/tablet.png) · [desktop](15-schools-health/04-absenteeism-wellness/desktop.png))
- **School sync status** — `15-schools-health/05-school-sync-status/` ([mobile](15-schools-health/05-school-sync-status/mobile.png) · [tablet](15-schools-health/05-school-sync-status/tablet.png) · [desktop](15-schools-health/05-school-sync-status/desktop.png))

### [16-pharmacy-outlets](16-pharmacy-outlets/README.md)

- **Pharmacy outlet home** — `16-pharmacy-outlets/01-pharmacy-home/` ([mobile](16-pharmacy-outlets/01-pharmacy-home/mobile.png) · [tablet](16-pharmacy-outlets/01-pharmacy-home/tablet.png) · [desktop](16-pharmacy-outlets/01-pharmacy-home/desktop.png))
- **Stock levels entry** — `16-pharmacy-outlets/02-stock-levels-entry/` ([mobile](16-pharmacy-outlets/02-stock-levels-entry/mobile.png) · [tablet](16-pharmacy-outlets/02-stock-levels-entry/tablet.png) · [desktop](16-pharmacy-outlets/02-stock-levels-entry/desktop.png))
- **Dispense log** — `16-pharmacy-outlets/03-dispense-log/` ([mobile](16-pharmacy-outlets/03-dispense-log/mobile.png) · [tablet](16-pharmacy-outlets/03-dispense-log/tablet.png) · [desktop](16-pharmacy-outlets/03-dispense-log/desktop.png))
- **Common complaints** — `16-pharmacy-outlets/04-common-complaints/` ([mobile](16-pharmacy-outlets/04-common-complaints/mobile.png) · [tablet](16-pharmacy-outlets/04-common-complaints/tablet.png) · [desktop](16-pharmacy-outlets/04-common-complaints/desktop.png))
- **Pre-stock acknowledgement** — `16-pharmacy-outlets/05-prestock-ack/` ([mobile](16-pharmacy-outlets/05-prestock-ack/mobile.png) · [tablet](16-pharmacy-outlets/05-prestock-ack/tablet.png) · [desktop](16-pharmacy-outlets/05-prestock-ack/desktop.png))

### [17-labs-poc](17-labs-poc/README.md)

- **Lab / PoC home** — `17-labs-poc/01-lab-home/` ([mobile](17-labs-poc/01-lab-home/mobile.png) · [tablet](17-labs-poc/01-lab-home/tablet.png) · [desktop](17-labs-poc/01-lab-home/desktop.png))
- **Result entry** — `17-labs-poc/02-result-entry/` ([mobile](17-labs-poc/02-result-entry/mobile.png) · [tablet](17-labs-poc/02-result-entry/tablet.png) · [desktop](17-labs-poc/02-result-entry/desktop.png))
- **Batch results upload** — `17-labs-poc/03-batch-results-upload/` ([mobile](17-labs-poc/03-batch-results-upload/mobile.png) · [tablet](17-labs-poc/03-batch-results-upload/tablet.png) · [desktop](17-labs-poc/03-batch-results-upload/desktop.png))
- **Result queue** — `17-labs-poc/04-result-queue/` ([mobile](17-labs-poc/04-result-queue/mobile.png) · [tablet](17-labs-poc/04-result-queue/tablet.png) · [desktop](17-labs-poc/04-result-queue/desktop.png))

### [18-corporate-wellness](18-corporate-wellness/README.md)

- **Corporate wellness home** — `18-corporate-wellness/01-corporate-home/` ([mobile](18-corporate-wellness/01-corporate-home/mobile.png) · [tablet](18-corporate-wellness/01-corporate-home/tablet.png) · [desktop](18-corporate-wellness/01-corporate-home/desktop.png))
- **Camp vitals entry** — `18-corporate-wellness/02-camp-vitals-entry/` ([mobile](18-corporate-wellness/02-camp-vitals-entry/mobile.png) · [tablet](18-corporate-wellness/02-camp-vitals-entry/tablet.png) · [desktop](18-corporate-wellness/02-camp-vitals-entry/desktop.png))
- **Camp summary push** — `18-corporate-wellness/03-camp-summary-push/` ([mobile](18-corporate-wellness/03-camp-summary-push/mobile.png) · [tablet](18-corporate-wellness/03-camp-summary-push/tablet.png) · [desktop](18-corporate-wellness/03-camp-summary-push/desktop.png))
- **Occupational flags** — `18-corporate-wellness/04-occupational-flags/` ([mobile](18-corporate-wellness/04-occupational-flags/mobile.png) · [tablet](18-corporate-wellness/04-occupational-flags/tablet.png) · [desktop](18-corporate-wellness/04-occupational-flags/desktop.png))

### [19-mch-touchpoints](19-mch-touchpoints/README.md)

- **MCH touchpoints home** — `19-mch-touchpoints/01-mch-home/` ([mobile](19-mch-touchpoints/01-mch-home/mobile.png) · [tablet](19-mch-touchpoints/01-mch-home/tablet.png) · [desktop](19-mch-touchpoints/01-mch-home/desktop.png))
- **ANC visit entry** — `19-mch-touchpoints/02-anc-visit-entry/` ([mobile](19-mch-touchpoints/02-anc-visit-entry/mobile.png) · [tablet](19-mch-touchpoints/02-anc-visit-entry/tablet.png) · [desktop](19-mch-touchpoints/02-anc-visit-entry/desktop.png))
- **PNC visit entry** — `19-mch-touchpoints/03-pnc-visit-entry/` ([mobile](19-mch-touchpoints/03-pnc-visit-entry/mobile.png) · [tablet](19-mch-touchpoints/03-pnc-visit-entry/tablet.png) · [desktop](19-mch-touchpoints/03-pnc-visit-entry/desktop.png))
- **Immunisation entry** — `19-mch-touchpoints/04-immunisation-entry/` ([mobile](19-mch-touchpoints/04-immunisation-entry/mobile.png) · [tablet](19-mch-touchpoints/04-immunisation-entry/tablet.png) · [desktop](19-mch-touchpoints/04-immunisation-entry/desktop.png))
- **Nutrition monitoring** — `19-mch-touchpoints/05-nutrition-monitoring/` ([mobile](19-mch-touchpoints/05-nutrition-monitoring/mobile.png) · [tablet](19-mch-touchpoints/05-nutrition-monitoring/tablet.png) · [desktop](19-mch-touchpoints/05-nutrition-monitoring/desktop.png))

### [20-ncd-gericare](20-ncd-gericare/README.md)

- **NCD / Gericare home** — `20-ncd-gericare/01-cohort-home/` ([mobile](20-ncd-gericare/01-cohort-home/mobile.png) · [tablet](20-ncd-gericare/01-cohort-home/tablet.png) · [desktop](20-ncd-gericare/01-cohort-home/desktop.png))
- **Cohort visit entry** — `20-ncd-gericare/02-cohort-visit-entry/` ([mobile](20-ncd-gericare/02-cohort-visit-entry/mobile.png) · [tablet](20-ncd-gericare/02-cohort-visit-entry/tablet.png) · [desktop](20-ncd-gericare/02-cohort-visit-entry/desktop.png))
- **BP screening batch** — `20-ncd-gericare/03-bp-screening-batch/` ([mobile](20-ncd-gericare/03-bp-screening-batch/mobile.png) · [tablet](20-ncd-gericare/03-bp-screening-batch/tablet.png) · [desktop](20-ncd-gericare/03-bp-screening-batch/desktop.png))
- **Stroke / NCD risk flags** — `20-ncd-gericare/04-stroke-risk-flags/` ([mobile](20-ncd-gericare/04-stroke-risk-flags/mobile.png) · [tablet](20-ncd-gericare/04-stroke-risk-flags/tablet.png) · [desktop](20-ncd-gericare/04-stroke-risk-flags/desktop.png))

### [21-hmis-dhis2](21-hmis-dhis2/README.md)

- **HMIS / DHIS2 home** — `21-hmis-dhis2/01-hmis-home/` ([mobile](21-hmis-dhis2/01-hmis-home/mobile.png) · [tablet](21-hmis-dhis2/01-hmis-home/tablet.png) · [desktop](21-hmis-dhis2/01-hmis-home/desktop.png))
- **Dataset mapping** — `21-hmis-dhis2/02-dataset-mapping/` ([mobile](21-hmis-dhis2/02-dataset-mapping/mobile.png) · [tablet](21-hmis-dhis2/02-dataset-mapping/tablet.png) · [desktop](21-hmis-dhis2/02-dataset-mapping/desktop.png))
- **Aggregate push / pull** — `21-hmis-dhis2/03-aggregate-push-pull/` ([mobile](21-hmis-dhis2/03-aggregate-push-pull/mobile.png) · [tablet](21-hmis-dhis2/03-aggregate-push-pull/tablet.png) · [desktop](21-hmis-dhis2/03-aggregate-push-pull/desktop.png))
- **HMIS audit** — `21-hmis-dhis2/04-hmis-audit/` ([mobile](21-hmis-dhis2/04-hmis-audit/mobile.png) · [tablet](21-hmis-dhis2/04-hmis-audit/tablet.png) · [desktop](21-hmis-dhis2/04-hmis-audit/desktop.png))

### [22-community-events](22-community-events/README.md)

- **Community events home** — `22-community-events/01-events-home/` ([mobile](22-community-events/01-events-home/mobile.png) · [tablet](22-community-events/01-events-home/tablet.png) · [desktop](22-community-events/01-events-home/desktop.png))
- **Outreach event log** — `22-community-events/02-outreach-event-log/` ([mobile](22-community-events/02-outreach-event-log/mobile.png) · [tablet](22-community-events/02-outreach-event-log/tablet.png) · [desktop](22-community-events/02-outreach-event-log/desktop.png))
- **Community dialogue** — `22-community-events/03-community-dialogue/` ([mobile](22-community-events/03-community-dialogue/mobile.png) · [tablet](22-community-events/03-community-dialogue/tablet.png) · [desktop](22-community-events/03-community-dialogue/desktop.png))
- **Participation register** — `22-community-events/04-participation-register/` ([mobile](22-community-events/04-participation-register/mobile.png) · [tablet](22-community-events/04-participation-register/tablet.png) · [desktop](22-community-events/04-participation-register/desktop.png))

### [23-research-exports](23-research-exports/README.md)

- **Evidence catalog** — `23-research-exports/01-evidence-catalog/` ([mobile](23-research-exports/01-evidence-catalog/mobile.png) · [tablet](23-research-exports/01-evidence-catalog/tablet.png) · [desktop](23-research-exports/01-evidence-catalog/desktop.png))
- **Export request** — `23-research-exports/02-export-request/` ([mobile](23-research-exports/02-export-request/mobile.png) · [tablet](23-research-exports/02-export-request/tablet.png) · [desktop](23-research-exports/02-export-request/desktop.png))
- **Research contribution upload** — `23-research-exports/03-research-contribution-upload/` ([mobile](23-research-exports/03-research-contribution-upload/mobile.png) · [tablet](23-research-exports/03-research-contribution-upload/tablet.png) · [desktop](23-research-exports/03-research-contribution-upload/desktop.png))
- **Export under review** — `23-research-exports/04-export-pending/` ([mobile](23-research-exports/04-export-pending/mobile.png) · [tablet](23-research-exports/04-export-pending/tablet.png) · [desktop](23-research-exports/04-export-pending/desktop.png))


## Regenerate

```bash
python app-ui/generate_mockups.py
# screens + shared kit (components + layouts)
```

## Shared kit (`00-shared`)

- [Components](00-shared/components/README.md) — reusable UI pieces
- [Layouts](00-shared/layouts/README.md) — page shells for every surface / feeder

## Sources

- `.cursor/app-write-up.mdc`
- `app-flows/01-overview.md` … `07-navigation.md` (especially `04-modules.md` and `07-navigation.md`)
