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
| Ministries of health (national) | `08-district-moh/national-roll-up` (Phase 3) |
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

- **FCHIP** — `00-shared/splash/` ([mobile](00-shared/splash/mobile.png) · [tablet](00-shared/splash/tablet.png) · [desktop](00-shared/splash/desktop.png))
- **Create account** — `00-shared/create-account/` ([mobile](00-shared/create-account/mobile.png) · [tablet](00-shared/create-account/tablet.png) · [desktop](00-shared/create-account/desktop.png))
- **Sign in** — `00-shared/login/` ([mobile](00-shared/login/mobile.png) · [tablet](00-shared/login/tablet.png) · [desktop](00-shared/login/desktop.png))
- **Reset password** — `00-shared/forgot-password/` ([mobile](00-shared/forgot-password/mobile.png) · [tablet](00-shared/forgot-password/tablet.png) · [desktop](00-shared/forgot-password/desktop.png))
- **Consent first** — `00-shared/consent-first-onboarding/` ([mobile](00-shared/consent-first-onboarding/mobile.png) · [tablet](00-shared/consent-first-onboarding/tablet.png) · [desktop](00-shared/consent-first-onboarding/desktop.png))
- **Offline PIN** — `00-shared/offline-pin-lock/` ([mobile](00-shared/offline-pin-lock/mobile.png) · [tablet](00-shared/offline-pin-lock/tablet.png) · [desktop](00-shared/offline-pin-lock/desktop.png))
- **Session locked** — `00-shared/session-locked/` ([mobile](00-shared/session-locked/mobile.png) · [tablet](00-shared/session-locked/tablet.png) · [desktop](00-shared/session-locked/desktop.png))
- **Choose your workspace** — `00-shared/role-surface-picker/` ([mobile](00-shared/role-surface-picker/mobile.png) · [tablet](00-shared/role-surface-picker/tablet.png) · [desktop](00-shared/role-surface-picker/desktop.png))
- **Notifications** — `00-shared/notifications-center/` ([mobile](00-shared/notifications-center/mobile.png) · [tablet](00-shared/notifications-center/tablet.png) · [desktop](00-shared/notifications-center/desktop.png))
- **Access denied** — `00-shared/access-denied/` ([mobile](00-shared/access-denied/mobile.png) · [tablet](00-shared/access-denied/tablet.png) · [desktop](00-shared/access-denied/desktop.png))
- **Page not found** — `00-shared/not-found/` ([mobile](00-shared/not-found/mobile.png) · [tablet](00-shared/not-found/tablet.png) · [desktop](00-shared/not-found/desktop.png))
- **Language & appearance** — `00-shared/preferences/` ([mobile](00-shared/preferences/mobile.png) · [tablet](00-shared/preferences/tablet.png) · [desktop](00-shared/preferences/desktop.png))

### [01-chw-vht-mobile](01-chw-vht-mobile/README.md)

- **Today’s worklist** — `01-chw-vht-mobile/worklist-home/` ([mobile](01-chw-vht-mobile/worklist-home/mobile.png) · [tablet](01-chw-vht-mobile/worklist-home/tablet.png) · [desktop](01-chw-vht-mobile/worklist-home/desktop.png))
- **Today’s worklist** — `01-chw-vht-mobile/worklist-empty/` ([mobile](01-chw-vht-mobile/worklist-empty/mobile.png) · [tablet](01-chw-vht-mobile/worklist-empty/tablet.png) · [desktop](01-chw-vht-mobile/worklist-empty/desktop.png))
- **Household visit** — `01-chw-vht-mobile/household-visit-form/` ([mobile](01-chw-vht-mobile/household-visit-form/mobile.png) · [tablet](01-chw-vht-mobile/household-visit-form/tablet.png) · [desktop](01-chw-vht-mobile/household-visit-form/desktop.png))
- **Symptoms & vitals** — `01-chw-vht-mobile/symptoms-vitals/` ([mobile](01-chw-vht-mobile/symptoms-vitals/mobile.png) · [tablet](01-chw-vht-mobile/symptoms-vitals/tablet.png) · [desktop](01-chw-vht-mobile/symptoms-vitals/desktop.png))
- **Maternal / child** — `01-chw-vht-mobile/maternal-child-indicators/` ([mobile](01-chw-vht-mobile/maternal-child-indicators/mobile.png) · [tablet](01-chw-vht-mobile/maternal-child-indicators/tablet.png) · [desktop](01-chw-vht-mobile/maternal-child-indicators/desktop.png))
- **Create referral** — `01-chw-vht-mobile/create-referral/` ([mobile](01-chw-vht-mobile/create-referral/mobile.png) · [tablet](01-chw-vht-mobile/create-referral/tablet.png) · [desktop](01-chw-vht-mobile/create-referral/desktop.png))
- **Alerts inbox** — `01-chw-vht-mobile/alerts-inbox/` ([mobile](01-chw-vht-mobile/alerts-inbox/mobile.png) · [tablet](01-chw-vht-mobile/alerts-inbox/tablet.png) · [desktop](01-chw-vht-mobile/alerts-inbox/desktop.png))
- **Act on alert** — `01-chw-vht-mobile/alert-follow-up/` ([mobile](01-chw-vht-mobile/alert-follow-up/mobile.png) · [tablet](01-chw-vht-mobile/alert-follow-up/tablet.png) · [desktop](01-chw-vht-mobile/alert-follow-up/desktop.png))
- **Sync status** — `01-chw-vht-mobile/sync-status/` ([mobile](01-chw-vht-mobile/sync-status/mobile.png) · [tablet](01-chw-vht-mobile/sync-status/tablet.png) · [desktop](01-chw-vht-mobile/sync-status/desktop.png))
- **Sync failed** — `01-chw-vht-mobile/sync-failed/` ([mobile](01-chw-vht-mobile/sync-failed/mobile.png) · [tablet](01-chw-vht-mobile/sync-failed/tablet.png) · [desktop](01-chw-vht-mobile/sync-failed/desktop.png))
- **Today’s worklist** — `01-chw-vht-mobile/worklist-loading/` ([mobile](01-chw-vht-mobile/worklist-loading/mobile.png) · [tablet](01-chw-vht-mobile/worklist-loading/tablet.png) · [desktop](01-chw-vht-mobile/worklist-loading/desktop.png))
- **Visit saved** — `01-chw-vht-mobile/visit-saved/` ([mobile](01-chw-vht-mobile/visit-saved/mobile.png) · [tablet](01-chw-vht-mobile/visit-saved/tablet.png) · [desktop](01-chw-vht-mobile/visit-saved/desktop.png))
- **Referral sent** — `01-chw-vht-mobile/referral-status/` ([mobile](01-chw-vht-mobile/referral-status/mobile.png) · [tablet](01-chw-vht-mobile/referral-status/tablet.png) · [desktop](01-chw-vht-mobile/referral-status/desktop.png))
- **Review sync conflict** — `01-chw-vht-mobile/sync-conflict/` ([mobile](01-chw-vht-mobile/sync-conflict/mobile.png) · [tablet](01-chw-vht-mobile/sync-conflict/tablet.png) · [desktop](01-chw-vht-mobile/sync-conflict/desktop.png))

### [02-intelligence](02-intelligence/README.md)

- **Ingest & sync** — `02-intelligence/ingest-pipeline/` ([mobile](02-intelligence/ingest-pipeline/mobile.png) · [tablet](02-intelligence/ingest-pipeline/tablet.png) · [desktop](02-intelligence/ingest-pipeline/desktop.png))
- **AI / predictive** — `02-intelligence/ai-risk-scores/` ([mobile](02-intelligence/ai-risk-scores/mobile.png) · [tablet](02-intelligence/ai-risk-scores/tablet.png) · [desktop](02-intelligence/ai-risk-scores/desktop.png))
- **GIS maps** — `02-intelligence/gis-explorer/` ([mobile](02-intelligence/gis-explorer/mobile.png) · [tablet](02-intelligence/gis-explorer/tablet.png) · [desktop](02-intelligence/gis-explorer/desktop.png))
- **Climate fusion** — `02-intelligence/climate-fusion/` ([mobile](02-intelligence/climate-fusion/mobile.png) · [tablet](02-intelligence/climate-fusion/tablet.png) · [desktop](02-intelligence/climate-fusion/desktop.png))
- **Clinical support guidance** — `02-intelligence/clinical-support-guidance/` ([mobile](02-intelligence/clinical-support-guidance/mobile.png) · [tablet](02-intelligence/clinical-support-guidance/tablet.png) · [desktop](02-intelligence/clinical-support-guidance/desktop.png))
- **Alerts & worklists engine** — `02-intelligence/alerts-worklists-engine/` ([mobile](02-intelligence/alerts-worklists-engine/mobile.png) · [tablet](02-intelligence/alerts-worklists-engine/tablet.png) · [desktop](02-intelligence/alerts-worklists-engine/desktop.png))
- **Feeder health board** — `02-intelligence/feeder-health-board/` ([mobile](02-intelligence/feeder-health-board/mobile.png) · [tablet](02-intelligence/feeder-health-board/tablet.png) · [desktop](02-intelligence/feeder-health-board/desktop.png))

### [03-cascade-metrics](03-cascade-metrics/README.md)

- **Cascade metrics** — `03-cascade-metrics/indicators-overview/` ([mobile](03-cascade-metrics/indicators-overview/mobile.png) · [tablet](03-cascade-metrics/indicators-overview/tablet.png) · [desktop](03-cascade-metrics/indicators-overview/desktop.png))
- **Gap detection** — `03-cascade-metrics/gap-detection/` ([mobile](03-cascade-metrics/gap-detection/mobile.png) · [tablet](03-cascade-metrics/gap-detection/tablet.png) · [desktop](03-cascade-metrics/gap-detection/desktop.png))
- **Partner reports** — `03-cascade-metrics/partner-reports/` ([mobile](03-cascade-metrics/partner-reports/mobile.png) · [tablet](03-cascade-metrics/partner-reports/tablet.png) · [desktop](03-cascade-metrics/partner-reports/desktop.png))

### [04-facility-dashboard](04-facility-dashboard/README.md)

- **Facility overview** — `04-facility-dashboard/overview/` ([mobile](04-facility-dashboard/overview/mobile.png) · [tablet](04-facility-dashboard/overview/tablet.png) · [desktop](04-facility-dashboard/overview/desktop.png))
- **Catchment map** — `04-facility-dashboard/catchment-map/` ([mobile](04-facility-dashboard/catchment-map/mobile.png) · [tablet](04-facility-dashboard/catchment-map/tablet.png) · [desktop](04-facility-dashboard/catchment-map/desktop.png))
- **Referral summary** — `04-facility-dashboard/open-referrals/` ([mobile](04-facility-dashboard/open-referrals/mobile.png) · [tablet](04-facility-dashboard/open-referrals/tablet.png) · [desktop](04-facility-dashboard/open-referrals/desktop.png))
- **Stock signal** — `04-facility-dashboard/stock-signal/` ([mobile](04-facility-dashboard/stock-signal/mobile.png) · [tablet](04-facility-dashboard/stock-signal/tablet.png) · [desktop](04-facility-dashboard/stock-signal/desktop.png))
- **Medicine demand forecast** — `04-facility-dashboard/medicine-demand-forecast/` ([mobile](04-facility-dashboard/medicine-demand-forecast/mobile.png) · [tablet](04-facility-dashboard/medicine-demand-forecast/tablet.png) · [desktop](04-facility-dashboard/medicine-demand-forecast/desktop.png))
- **Outreach priorities** — `04-facility-dashboard/outreach-priorities/` ([mobile](04-facility-dashboard/outreach-priorities/mobile.png) · [tablet](04-facility-dashboard/outreach-priorities/tablet.png) · [desktop](04-facility-dashboard/outreach-priorities/desktop.png))
- **Clinical share confirm** — `04-facility-dashboard/clinical-share-confirm/` ([mobile](04-facility-dashboard/clinical-share-confirm/mobile.png) · [tablet](04-facility-dashboard/clinical-share-confirm/tablet.png) · [desktop](04-facility-dashboard/clinical-share-confirm/desktop.png))
- **Manual case signal** — `04-facility-dashboard/manual-case-signal/` ([mobile](04-facility-dashboard/manual-case-signal/mobile.png) · [tablet](04-facility-dashboard/manual-case-signal/tablet.png) · [desktop](04-facility-dashboard/manual-case-signal/desktop.png))

### [05-referrals-desk](05-referrals-desk/README.md)

- **Referrals desk** — `05-referrals-desk/referral-queue/` ([mobile](05-referrals-desk/referral-queue/mobile.png) · [tablet](05-referrals-desk/referral-queue/tablet.png) · [desktop](05-referrals-desk/referral-queue/desktop.png))
- **Referrals desk** — `05-referrals-desk/referral-queue-empty/` ([mobile](05-referrals-desk/referral-queue-empty/mobile.png) · [tablet](05-referrals-desk/referral-queue-empty/tablet.png) · [desktop](05-referrals-desk/referral-queue-empty/desktop.png))
- **Referral detail** — `05-referrals-desk/referral-detail/` ([mobile](05-referrals-desk/referral-detail/mobile.png) · [tablet](05-referrals-desk/referral-detail/tablet.png) · [desktop](05-referrals-desk/referral-detail/desktop.png))
- **Outcome feedback** — `05-referrals-desk/outcome-feedback/` ([mobile](05-referrals-desk/outcome-feedback/mobile.png) · [tablet](05-referrals-desk/outcome-feedback/tablet.png) · [desktop](05-referrals-desk/outcome-feedback/desktop.png))

### [06-emr-connector](06-emr-connector/README.md)

- **EMR / HMS connector** — `06-emr-connector/connector-status/` ([mobile](06-emr-connector/connector-status/mobile.png) · [tablet](06-emr-connector/connector-status/tablet.png) · [desktop](06-emr-connector/connector-status/desktop.png))
- **EMR / HMS connector** — `06-emr-connector/connector-degraded/` ([mobile](06-emr-connector/connector-degraded/mobile.png) · [tablet](06-emr-connector/connector-degraded/tablet.png) · [desktop](06-emr-connector/connector-degraded/desktop.png))
- **API scopes setup** — `06-emr-connector/api-scopes-setup/` ([mobile](06-emr-connector/api-scopes-setup/mobile.png) · [tablet](06-emr-connector/api-scopes-setup/tablet.png) · [desktop](06-emr-connector/api-scopes-setup/desktop.png))
- **Push event log** — `06-emr-connector/push-event-log/` ([mobile](06-emr-connector/push-event-log/mobile.png) · [tablet](06-emr-connector/push-event-log/tablet.png) · [desktop](06-emr-connector/push-event-log/desktop.png))
- **Facility onboarding** — `06-emr-connector/facility-onboarding/` ([mobile](06-emr-connector/facility-onboarding/mobile.png) · [tablet](06-emr-connector/facility-onboarding/tablet.png) · [desktop](06-emr-connector/facility-onboarding/desktop.png))

### [07-climate-feeds](07-climate-feeds/README.md)

- **Climate feeds home** — `07-climate-feeds/climate-home/` ([mobile](07-climate-feeds/climate-home/mobile.png) · [tablet](07-climate-feeds/climate-home/tablet.png) · [desktop](07-climate-feeds/climate-home/desktop.png))
- **Rainfall & temperature** — `07-climate-feeds/rainfall-temperature/` ([mobile](07-climate-feeds/rainfall-temperature/mobile.png) · [tablet](07-climate-feeds/rainfall-temperature/tablet.png) · [desktop](07-climate-feeds/rainfall-temperature/desktop.png))
- **Extremes · flood · heat** — `07-climate-feeds/extremes-flood-heat/` ([mobile](07-climate-feeds/extremes-flood-heat/mobile.png) · [tablet](07-climate-feeds/extremes-flood-heat/tablet.png) · [desktop](07-climate-feeds/extremes-flood-heat/desktop.png))
- **Feed config & audit** — `07-climate-feeds/feed-config-audit/` ([mobile](07-climate-feeds/feed-config-audit/mobile.png) · [tablet](07-climate-feeds/feed-config-audit/tablet.png) · [desktop](07-climate-feeds/feed-config-audit/desktop.png))

### [08-district-moh](08-district-moh/README.md)

- **Population map** — `08-district-moh/population-map/` ([mobile](08-district-moh/population-map/mobile.png) · [tablet](08-district-moh/population-map/tablet.png) · [desktop](08-district-moh/population-map/desktop.png))
- **Early warnings** — `08-district-moh/early-warnings/` ([mobile](08-district-moh/early-warnings/mobile.png) · [tablet](08-district-moh/early-warnings/tablet.png) · [desktop](08-district-moh/early-warnings/desktop.png))
- **Deploy action** — `08-district-moh/action-deploy/` ([mobile](08-district-moh/action-deploy/mobile.png) · [tablet](08-district-moh/action-deploy/tablet.png) · [desktop](08-district-moh/action-deploy/desktop.png))
- **Cascade M&E planning** — `08-district-moh/cascade-planning/` ([mobile](08-district-moh/cascade-planning/mobile.png) · [tablet](08-district-moh/cascade-planning/tablet.png) · [desktop](08-district-moh/cascade-planning/desktop.png))
- **MoH national roll-up** — `08-district-moh/national-roll-up/` ([mobile](08-district-moh/national-roll-up/mobile.png) · [tablet](08-district-moh/national-roll-up/tablet.png) · [desktop](08-district-moh/national-roll-up/desktop.png))

### [09-community-caregiver](09-community-caregiver/README.md)

- **My household** — `09-community-caregiver/my-household/` ([mobile](09-community-caregiver/my-household/mobile.png) · [tablet](09-community-caregiver/my-household/tablet.png) · [desktop](09-community-caregiver/my-household/desktop.png))
- **Self-report** — `09-community-caregiver/self-report/` ([mobile](09-community-caregiver/self-report/mobile.png) · [tablet](09-community-caregiver/self-report/tablet.png) · [desktop](09-community-caregiver/self-report/desktop.png))
- **Guidance** — `09-community-caregiver/guidance-hints/` ([mobile](09-community-caregiver/guidance-hints/mobile.png) · [tablet](09-community-caregiver/guidance-hints/tablet.png) · [desktop](09-community-caregiver/guidance-hints/desktop.png))
- **Household needs** — `09-community-caregiver/household-needs-capture/` ([mobile](09-community-caregiver/household-needs-capture/mobile.png) · [tablet](09-community-caregiver/household-needs-capture/tablet.png) · [desktop](09-community-caregiver/household-needs-capture/desktop.png))

### [10-outreach-school-health](10-outreach-school-health/README.md)

- **Campaign planner** — `10-outreach-school-health/campaign-planner/` ([mobile](10-outreach-school-health/campaign-planner/mobile.png) · [tablet](10-outreach-school-health/campaign-planner/tablet.png) · [desktop](10-outreach-school-health/campaign-planner/desktop.png))
- **Session log** — `10-outreach-school-health/session-log/` ([mobile](10-outreach-school-health/session-log/mobile.png) · [tablet](10-outreach-school-health/session-log/tablet.png) · [desktop](10-outreach-school-health/session-log/desktop.png))
- **Coverage map** — `10-outreach-school-health/coverage-map/` ([mobile](10-outreach-school-health/coverage-map/mobile.png) · [tablet](10-outreach-school-health/coverage-map/tablet.png) · [desktop](10-outreach-school-health/coverage-map/desktop.png))
- **Screening results entry** — `10-outreach-school-health/screening-results-entry/` ([mobile](10-outreach-school-health/screening-results-entry/mobile.png) · [tablet](10-outreach-school-health/screening-results-entry/tablet.png) · [desktop](10-outreach-school-health/screening-results-entry/desktop.png))
- **Home-visit batch** — `10-outreach-school-health/home-visit-batch-upload/` ([mobile](10-outreach-school-health/home-visit-batch-upload/mobile.png) · [tablet](10-outreach-school-health/home-visit-batch-upload/tablet.png) · [desktop](10-outreach-school-health/home-visit-batch-upload/desktop.png))

### [11-admin-consent](11-admin-consent/README.md)

- **Org · catchment · facilities** — `11-admin-consent/org-catchment/` ([mobile](11-admin-consent/org-catchment/mobile.png) · [tablet](11-admin-consent/org-catchment/tablet.png) · [desktop](11-admin-consent/org-catchment/desktop.png))
- **Users & roles** — `11-admin-consent/users-roles/` ([mobile](11-admin-consent/users-roles/mobile.png) · [tablet](11-admin-consent/users-roles/tablet.png) · [desktop](11-admin-consent/users-roles/desktop.png))
- **Consent & privacy** — `11-admin-consent/consent-privacy/` ([mobile](11-admin-consent/consent-privacy/mobile.png) · [tablet](11-admin-consent/consent-privacy/tablet.png) · [desktop](11-admin-consent/consent-privacy/desktop.png))
- **EMR API access** — `11-admin-consent/emr-api-access/` ([mobile](11-admin-consent/emr-api-access/mobile.png) · [tablet](11-admin-consent/emr-api-access/tablet.png) · [desktop](11-admin-consent/emr-api-access/desktop.png))
- **Feeder party registry** — `11-admin-consent/feeder-party-registry/` ([mobile](11-admin-consent/feeder-party-registry/mobile.png) · [tablet](11-admin-consent/feeder-party-registry/tablet.png) · [desktop](11-admin-consent/feeder-party-registry/desktop.png))

### [12-insurance-insights](12-insurance-insights/README.md)

- **Prevention overview** — `12-insurance-insights/prevention-overview/` ([mobile](12-insurance-insights/prevention-overview/mobile.png) · [tablet](12-insurance-insights/prevention-overview/tablet.png) · [desktop](12-insurance-insights/prevention-overview/desktop.png))
- **Risk cohort insights** — `12-insurance-insights/risk-cohort-insights/` ([mobile](12-insurance-insights/risk-cohort-insights/mobile.png) · [tablet](12-insurance-insights/risk-cohort-insights/tablet.png) · [desktop](12-insurance-insights/risk-cohort-insights/desktop.png))
- **Anonymised trends** — `12-insurance-insights/anonymised-trends/` ([mobile](12-insurance-insights/anonymised-trends/mobile.png) · [tablet](12-insurance-insights/anonymised-trends/tablet.png) · [desktop](12-insurance-insights/anonymised-trends/desktop.png))
### [13-chis-livelihoods](13-chis-livelihoods/README.md)

- **CHIS enrolment** — `13-chis-livelihoods/enrolment/` ([mobile](13-chis-livelihoods/enrolment/mobile.png) · [tablet](13-chis-livelihoods/enrolment/tablet.png) · [desktop](13-chis-livelihoods/enrolment/desktop.png))
- **Contributions** — `13-chis-livelihoods/contributions/` ([mobile](13-chis-livelihoods/contributions/mobile.png) · [tablet](13-chis-livelihoods/contributions/tablet.png) · [desktop](13-chis-livelihoods/contributions/desktop.png))
- **Claims / access** — `13-chis-livelihoods/claims-access/` ([mobile](13-chis-livelihoods/claims-access/mobile.png) · [tablet](13-chis-livelihoods/claims-access/tablet.png) · [desktop](13-chis-livelihoods/claims-access/desktop.png))
- **IGA participation entry** — `13-chis-livelihoods/iga-participation-entry/` ([mobile](13-chis-livelihoods/iga-participation-entry/mobile.png) · [tablet](13-chis-livelihoods/iga-participation-entry/tablet.png) · [desktop](13-chis-livelihoods/iga-participation-entry/desktop.png))

### [14-ngo-partner](14-ngo-partner/README.md)

- **Programme monitoring** — `14-ngo-partner/programme-monitoring/` ([mobile](14-ngo-partner/programme-monitoring/mobile.png) · [tablet](14-ngo-partner/programme-monitoring/tablet.png) · [desktop](14-ngo-partner/programme-monitoring/desktop.png))
- **Impact evidence** — `14-ngo-partner/impact-evidence/` ([mobile](14-ngo-partner/impact-evidence/mobile.png) · [tablet](14-ngo-partner/impact-evidence/tablet.png) · [desktop](14-ngo-partner/impact-evidence/desktop.png))
- **Training · skills analytics** — `14-ngo-partner/training-skills-analytics/` ([mobile](14-ngo-partner/training-skills-analytics/mobile.png) · [tablet](14-ngo-partner/training-skills-analytics/tablet.png) · [desktop](14-ngo-partner/training-skills-analytics/desktop.png))
- **Field dataset upload** — `14-ngo-partner/field-dataset-upload/` ([mobile](14-ngo-partner/field-dataset-upload/mobile.png) · [tablet](14-ngo-partner/field-dataset-upload/tablet.png) · [desktop](14-ngo-partner/field-dataset-upload/desktop.png))
- **Partner indicator entry** — `14-ngo-partner/partner-indicator-entry/` ([mobile](14-ngo-partner/partner-indicator-entry/mobile.png) · [tablet](14-ngo-partner/partner-indicator-entry/tablet.png) · [desktop](14-ngo-partner/partner-indicator-entry/desktop.png))

### [15-schools-health](15-schools-health/README.md)

- **School health home** — `15-schools-health/school-home/` ([mobile](15-schools-health/school-home/mobile.png) · [tablet](15-schools-health/school-home/tablet.png) · [desktop](15-schools-health/school-home/desktop.png))
- **Health education session** — `15-schools-health/health-education-session/` ([mobile](15-schools-health/health-education-session/mobile.png) · [tablet](15-schools-health/health-education-session/tablet.png) · [desktop](15-schools-health/health-education-session/desktop.png))
- **Learner screening entry** — `15-schools-health/learner-screening-entry/` ([mobile](15-schools-health/learner-screening-entry/mobile.png) · [tablet](15-schools-health/learner-screening-entry/tablet.png) · [desktop](15-schools-health/learner-screening-entry/desktop.png))
- **Absenteeism & wellness** — `15-schools-health/absenteeism-wellness/` ([mobile](15-schools-health/absenteeism-wellness/mobile.png) · [tablet](15-schools-health/absenteeism-wellness/tablet.png) · [desktop](15-schools-health/absenteeism-wellness/desktop.png))
- **School sync status** — `15-schools-health/school-sync-status/` ([mobile](15-schools-health/school-sync-status/mobile.png) · [tablet](15-schools-health/school-sync-status/tablet.png) · [desktop](15-schools-health/school-sync-status/desktop.png))

### [16-pharmacy-outlets](16-pharmacy-outlets/README.md)

- **Pharmacy outlet home** — `16-pharmacy-outlets/pharmacy-home/` ([mobile](16-pharmacy-outlets/pharmacy-home/mobile.png) · [tablet](16-pharmacy-outlets/pharmacy-home/tablet.png) · [desktop](16-pharmacy-outlets/pharmacy-home/desktop.png))
- **Stock levels entry** — `16-pharmacy-outlets/stock-levels-entry/` ([mobile](16-pharmacy-outlets/stock-levels-entry/mobile.png) · [tablet](16-pharmacy-outlets/stock-levels-entry/tablet.png) · [desktop](16-pharmacy-outlets/stock-levels-entry/desktop.png))
- **Dispense log** — `16-pharmacy-outlets/dispense-log/` ([mobile](16-pharmacy-outlets/dispense-log/mobile.png) · [tablet](16-pharmacy-outlets/dispense-log/tablet.png) · [desktop](16-pharmacy-outlets/dispense-log/desktop.png))
- **Common complaints** — `16-pharmacy-outlets/common-complaints/` ([mobile](16-pharmacy-outlets/common-complaints/mobile.png) · [tablet](16-pharmacy-outlets/common-complaints/tablet.png) · [desktop](16-pharmacy-outlets/common-complaints/desktop.png))
- **Pre-stock acknowledgement** — `16-pharmacy-outlets/prestock-ack/` ([mobile](16-pharmacy-outlets/prestock-ack/mobile.png) · [tablet](16-pharmacy-outlets/prestock-ack/tablet.png) · [desktop](16-pharmacy-outlets/prestock-ack/desktop.png))

### [17-labs-poc](17-labs-poc/README.md)

- **Lab / PoC home** — `17-labs-poc/lab-home/` ([mobile](17-labs-poc/lab-home/mobile.png) · [tablet](17-labs-poc/lab-home/tablet.png) · [desktop](17-labs-poc/lab-home/desktop.png))
- **Result entry** — `17-labs-poc/result-entry/` ([mobile](17-labs-poc/result-entry/mobile.png) · [tablet](17-labs-poc/result-entry/tablet.png) · [desktop](17-labs-poc/result-entry/desktop.png))
- **Batch results upload** — `17-labs-poc/batch-results-upload/` ([mobile](17-labs-poc/batch-results-upload/mobile.png) · [tablet](17-labs-poc/batch-results-upload/tablet.png) · [desktop](17-labs-poc/batch-results-upload/desktop.png))
- **Result queue** — `17-labs-poc/result-queue/` ([mobile](17-labs-poc/result-queue/mobile.png) · [tablet](17-labs-poc/result-queue/tablet.png) · [desktop](17-labs-poc/result-queue/desktop.png))

### [18-corporate-wellness](18-corporate-wellness/README.md)

- **Corporate wellness home** — `18-corporate-wellness/corporate-home/` ([mobile](18-corporate-wellness/corporate-home/mobile.png) · [tablet](18-corporate-wellness/corporate-home/tablet.png) · [desktop](18-corporate-wellness/corporate-home/desktop.png))
- **Camp vitals entry** — `18-corporate-wellness/camp-vitals-entry/` ([mobile](18-corporate-wellness/camp-vitals-entry/mobile.png) · [tablet](18-corporate-wellness/camp-vitals-entry/tablet.png) · [desktop](18-corporate-wellness/camp-vitals-entry/desktop.png))
- **Camp summary push** — `18-corporate-wellness/camp-summary-push/` ([mobile](18-corporate-wellness/camp-summary-push/mobile.png) · [tablet](18-corporate-wellness/camp-summary-push/tablet.png) · [desktop](18-corporate-wellness/camp-summary-push/desktop.png))
- **Occupational flags** — `18-corporate-wellness/occupational-flags/` ([mobile](18-corporate-wellness/occupational-flags/mobile.png) · [tablet](18-corporate-wellness/occupational-flags/tablet.png) · [desktop](18-corporate-wellness/occupational-flags/desktop.png))

### [19-mch-touchpoints](19-mch-touchpoints/README.md)

- **MCH touchpoints home** — `19-mch-touchpoints/mch-home/` ([mobile](19-mch-touchpoints/mch-home/mobile.png) · [tablet](19-mch-touchpoints/mch-home/tablet.png) · [desktop](19-mch-touchpoints/mch-home/desktop.png))
- **ANC visit entry** — `19-mch-touchpoints/anc-visit-entry/` ([mobile](19-mch-touchpoints/anc-visit-entry/mobile.png) · [tablet](19-mch-touchpoints/anc-visit-entry/tablet.png) · [desktop](19-mch-touchpoints/anc-visit-entry/desktop.png))
- **PNC visit entry** — `19-mch-touchpoints/pnc-visit-entry/` ([mobile](19-mch-touchpoints/pnc-visit-entry/mobile.png) · [tablet](19-mch-touchpoints/pnc-visit-entry/tablet.png) · [desktop](19-mch-touchpoints/pnc-visit-entry/desktop.png))
- **Immunisation entry** — `19-mch-touchpoints/immunisation-entry/` ([mobile](19-mch-touchpoints/immunisation-entry/mobile.png) · [tablet](19-mch-touchpoints/immunisation-entry/tablet.png) · [desktop](19-mch-touchpoints/immunisation-entry/desktop.png))
- **Nutrition monitoring** — `19-mch-touchpoints/nutrition-monitoring/` ([mobile](19-mch-touchpoints/nutrition-monitoring/mobile.png) · [tablet](19-mch-touchpoints/nutrition-monitoring/tablet.png) · [desktop](19-mch-touchpoints/nutrition-monitoring/desktop.png))

### [20-ncd-gericare](20-ncd-gericare/README.md)

- **NCD / Gericare home** — `20-ncd-gericare/cohort-home/` ([mobile](20-ncd-gericare/cohort-home/mobile.png) · [tablet](20-ncd-gericare/cohort-home/tablet.png) · [desktop](20-ncd-gericare/cohort-home/desktop.png))
- **Cohort visit entry** — `20-ncd-gericare/cohort-visit-entry/` ([mobile](20-ncd-gericare/cohort-visit-entry/mobile.png) · [tablet](20-ncd-gericare/cohort-visit-entry/tablet.png) · [desktop](20-ncd-gericare/cohort-visit-entry/desktop.png))
- **BP screening batch** — `20-ncd-gericare/bp-screening-batch/` ([mobile](20-ncd-gericare/bp-screening-batch/mobile.png) · [tablet](20-ncd-gericare/bp-screening-batch/tablet.png) · [desktop](20-ncd-gericare/bp-screening-batch/desktop.png))
- **Stroke / NCD risk flags** — `20-ncd-gericare/stroke-risk-flags/` ([mobile](20-ncd-gericare/stroke-risk-flags/mobile.png) · [tablet](20-ncd-gericare/stroke-risk-flags/tablet.png) · [desktop](20-ncd-gericare/stroke-risk-flags/desktop.png))

### [21-hmis-dhis2](21-hmis-dhis2/README.md)

- **HMIS / DHIS2 home** — `21-hmis-dhis2/hmis-home/` ([mobile](21-hmis-dhis2/hmis-home/mobile.png) · [tablet](21-hmis-dhis2/hmis-home/tablet.png) · [desktop](21-hmis-dhis2/hmis-home/desktop.png))
- **Dataset mapping** — `21-hmis-dhis2/dataset-mapping/` ([mobile](21-hmis-dhis2/dataset-mapping/mobile.png) · [tablet](21-hmis-dhis2/dataset-mapping/tablet.png) · [desktop](21-hmis-dhis2/dataset-mapping/desktop.png))
- **Aggregate push / pull** — `21-hmis-dhis2/aggregate-push-pull/` ([mobile](21-hmis-dhis2/aggregate-push-pull/mobile.png) · [tablet](21-hmis-dhis2/aggregate-push-pull/tablet.png) · [desktop](21-hmis-dhis2/aggregate-push-pull/desktop.png))
- **HMIS audit** — `21-hmis-dhis2/hmis-audit/` ([mobile](21-hmis-dhis2/hmis-audit/mobile.png) · [tablet](21-hmis-dhis2/hmis-audit/tablet.png) · [desktop](21-hmis-dhis2/hmis-audit/desktop.png))

### [22-community-events](22-community-events/README.md)

- **Community events home** — `22-community-events/events-home/` ([mobile](22-community-events/events-home/mobile.png) · [tablet](22-community-events/events-home/tablet.png) · [desktop](22-community-events/events-home/desktop.png))
- **Outreach event log** — `22-community-events/outreach-event-log/` ([mobile](22-community-events/outreach-event-log/mobile.png) · [tablet](22-community-events/outreach-event-log/tablet.png) · [desktop](22-community-events/outreach-event-log/desktop.png))
- **Community dialogue** — `22-community-events/community-dialogue/` ([mobile](22-community-events/community-dialogue/mobile.png) · [tablet](22-community-events/community-dialogue/tablet.png) · [desktop](22-community-events/community-dialogue/desktop.png))
- **Participation register** — `22-community-events/participation-register/` ([mobile](22-community-events/participation-register/mobile.png) · [tablet](22-community-events/participation-register/tablet.png) · [desktop](22-community-events/participation-register/desktop.png))

### [23-research-exports](23-research-exports/README.md)

- **Evidence catalog** — `23-research-exports/evidence-catalog/` ([mobile](23-research-exports/evidence-catalog/mobile.png) · [tablet](23-research-exports/evidence-catalog/tablet.png) · [desktop](23-research-exports/evidence-catalog/desktop.png))
- **Export request** — `23-research-exports/export-request/` ([mobile](23-research-exports/export-request/mobile.png) · [tablet](23-research-exports/export-request/tablet.png) · [desktop](23-research-exports/export-request/desktop.png))
- **Research contribution upload** — `23-research-exports/research-contribution-upload/` ([mobile](23-research-exports/research-contribution-upload/mobile.png) · [tablet](23-research-exports/research-contribution-upload/tablet.png) · [desktop](23-research-exports/research-contribution-upload/desktop.png))
- **Export under review** — `23-research-exports/export-pending/` ([mobile](23-research-exports/export-pending/mobile.png) · [tablet](23-research-exports/export-pending/tablet.png) · [desktop](23-research-exports/export-pending/desktop.png))


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
