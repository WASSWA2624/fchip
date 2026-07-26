# FCHIP app-ui

Visual directory of **proposed** FCHIP screens from `.cursor/app-write-up.mdc` and `app-flows/`.
Not generated from `frontend/` code.

**103 screens** × mobile / tablet / desktop = **309 mockups**.

Slogan: **Your health, our mission.**

## Breakpoints

| Name | Size |
| --- | --- |
| mobile | 390 × 844 |
| tablet | 768 × 1024 |
| desktop | 1440 × 900 |

## Data feeders covered (SoT §4.2 / app-flows 03)

| Feeder party | Module folder |
| --- | --- |
| CHWs / VHTs | `01-chw-vht-mobile` |
| Patients / caregivers | `02-community-caregiver` |
| Communities · events · dialogues | `21-community-events` (+ needs in `02`) |
| Outreach programmes | `03-outreach-school-health` |
| Schools | `14-schools-health` |
| Hospitals / clinics (manual + share) | `06-facility-dashboard` · `07-referrals-desk` |
| Existing EMR / HMS | `08-emr-connector` |
| Pharmacies / drug shops | `15-pharmacy-outlets` |
| ANC / PNC · immunisation · nutrition | `18-mch-touchpoints` |
| Corporate / workplace wellness | `17-corporate-wellness` |
| Labs / PoC | `16-labs-poc` |
| Gericare / NCD cohorts | `19-ncd-gericare` |
| CHIS / livelihoods (optional) | `05-chis-livelihoods` |
| HMIS / DHIS2 (where approved) | `20-hmis-dhis2` |
| Research / NGO M&E uploads | `11-ngo-partner` · `12-research-exports` |
| Climate API | `22-climate-feeds` (+ fusion in `09`) |

## Modules

### [00-shared](00-shared/README.md)

- **FCHIP** — `00-shared/splash/` ([mobile](00-shared/splash/mobile.png) · [tablet](00-shared/splash/tablet.png) · [desktop](00-shared/splash/desktop.png))
- **Sign in** — `00-shared/login/` ([mobile](00-shared/login/mobile.png) · [tablet](00-shared/login/tablet.png) · [desktop](00-shared/login/desktop.png))
- **Choose your workspace** — `00-shared/role-surface-picker/` ([mobile](00-shared/role-surface-picker/mobile.png) · [tablet](00-shared/role-surface-picker/tablet.png) · [desktop](00-shared/role-surface-picker/desktop.png))
- **Notifications** — `00-shared/notifications-center/` ([mobile](00-shared/notifications-center/mobile.png) · [tablet](00-shared/notifications-center/tablet.png) · [desktop](00-shared/notifications-center/desktop.png))

### [01-chw-vht-mobile](01-chw-vht-mobile/README.md)

- **Today’s worklist** — `01-chw-vht-mobile/worklist-home/` ([mobile](01-chw-vht-mobile/worklist-home/mobile.png) · [tablet](01-chw-vht-mobile/worklist-home/tablet.png) · [desktop](01-chw-vht-mobile/worklist-home/desktop.png))
- **Household visit** — `01-chw-vht-mobile/household-visit-form/` ([mobile](01-chw-vht-mobile/household-visit-form/mobile.png) · [tablet](01-chw-vht-mobile/household-visit-form/tablet.png) · [desktop](01-chw-vht-mobile/household-visit-form/desktop.png))
- **Symptoms & vitals** — `01-chw-vht-mobile/symptoms-vitals/` ([mobile](01-chw-vht-mobile/symptoms-vitals/mobile.png) · [tablet](01-chw-vht-mobile/symptoms-vitals/tablet.png) · [desktop](01-chw-vht-mobile/symptoms-vitals/desktop.png))
- **Maternal / child** — `01-chw-vht-mobile/maternal-child-indicators/` ([mobile](01-chw-vht-mobile/maternal-child-indicators/mobile.png) · [tablet](01-chw-vht-mobile/maternal-child-indicators/tablet.png) · [desktop](01-chw-vht-mobile/maternal-child-indicators/desktop.png))
- **Create referral** — `01-chw-vht-mobile/create-referral/` ([mobile](01-chw-vht-mobile/create-referral/mobile.png) · [tablet](01-chw-vht-mobile/create-referral/tablet.png) · [desktop](01-chw-vht-mobile/create-referral/desktop.png))
- **Alerts inbox** — `01-chw-vht-mobile/alerts-inbox/` ([mobile](01-chw-vht-mobile/alerts-inbox/mobile.png) · [tablet](01-chw-vht-mobile/alerts-inbox/tablet.png) · [desktop](01-chw-vht-mobile/alerts-inbox/desktop.png))
- **Act on alert** — `01-chw-vht-mobile/alert-follow-up/` ([mobile](01-chw-vht-mobile/alert-follow-up/mobile.png) · [tablet](01-chw-vht-mobile/alert-follow-up/tablet.png) · [desktop](01-chw-vht-mobile/alert-follow-up/desktop.png))
- **Sync status** — `01-chw-vht-mobile/sync-status/` ([mobile](01-chw-vht-mobile/sync-status/mobile.png) · [tablet](01-chw-vht-mobile/sync-status/tablet.png) · [desktop](01-chw-vht-mobile/sync-status/desktop.png))

### [02-community-caregiver](02-community-caregiver/README.md)

- **My household** — `02-community-caregiver/my-household/` ([mobile](02-community-caregiver/my-household/mobile.png) · [tablet](02-community-caregiver/my-household/tablet.png) · [desktop](02-community-caregiver/my-household/desktop.png))
- **Self-report** — `02-community-caregiver/self-report/` ([mobile](02-community-caregiver/self-report/mobile.png) · [tablet](02-community-caregiver/self-report/tablet.png) · [desktop](02-community-caregiver/self-report/desktop.png))
- **Guidance** — `02-community-caregiver/guidance-hints/` ([mobile](02-community-caregiver/guidance-hints/mobile.png) · [tablet](02-community-caregiver/guidance-hints/tablet.png) · [desktop](02-community-caregiver/guidance-hints/desktop.png))
- **Household needs** — `02-community-caregiver/household-needs-capture/` ([mobile](02-community-caregiver/household-needs-capture/mobile.png) · [tablet](02-community-caregiver/household-needs-capture/tablet.png) · [desktop](02-community-caregiver/household-needs-capture/desktop.png))

### [03-outreach-school-health](03-outreach-school-health/README.md)

- **Campaign planner** — `03-outreach-school-health/campaign-planner/` ([mobile](03-outreach-school-health/campaign-planner/mobile.png) · [tablet](03-outreach-school-health/campaign-planner/tablet.png) · [desktop](03-outreach-school-health/campaign-planner/desktop.png))
- **Session log** — `03-outreach-school-health/session-log/` ([mobile](03-outreach-school-health/session-log/mobile.png) · [tablet](03-outreach-school-health/session-log/tablet.png) · [desktop](03-outreach-school-health/session-log/desktop.png))
- **Coverage map** — `03-outreach-school-health/coverage-map/` ([mobile](03-outreach-school-health/coverage-map/mobile.png) · [tablet](03-outreach-school-health/coverage-map/tablet.png) · [desktop](03-outreach-school-health/coverage-map/desktop.png))
- **Screening results entry** — `03-outreach-school-health/screening-results-entry/` ([mobile](03-outreach-school-health/screening-results-entry/mobile.png) · [tablet](03-outreach-school-health/screening-results-entry/tablet.png) · [desktop](03-outreach-school-health/screening-results-entry/desktop.png))
- **Home-visit batch** — `03-outreach-school-health/home-visit-batch-upload/` ([mobile](03-outreach-school-health/home-visit-batch-upload/mobile.png) · [tablet](03-outreach-school-health/home-visit-batch-upload/tablet.png) · [desktop](03-outreach-school-health/home-visit-batch-upload/desktop.png))

### [04-cascade-metrics](04-cascade-metrics/README.md)

- **Cascade metrics** — `04-cascade-metrics/indicators-overview/` ([mobile](04-cascade-metrics/indicators-overview/mobile.png) · [tablet](04-cascade-metrics/indicators-overview/tablet.png) · [desktop](04-cascade-metrics/indicators-overview/desktop.png))
- **Gap detection** — `04-cascade-metrics/gap-detection/` ([mobile](04-cascade-metrics/gap-detection/mobile.png) · [tablet](04-cascade-metrics/gap-detection/tablet.png) · [desktop](04-cascade-metrics/gap-detection/desktop.png))
- **Partner reports** — `04-cascade-metrics/partner-reports/` ([mobile](04-cascade-metrics/partner-reports/mobile.png) · [tablet](04-cascade-metrics/partner-reports/tablet.png) · [desktop](04-cascade-metrics/partner-reports/desktop.png))

### [05-chis-livelihoods](05-chis-livelihoods/README.md)

- **CHIS enrolment** — `05-chis-livelihoods/enrolment/` ([mobile](05-chis-livelihoods/enrolment/mobile.png) · [tablet](05-chis-livelihoods/enrolment/tablet.png) · [desktop](05-chis-livelihoods/enrolment/desktop.png))
- **Contributions** — `05-chis-livelihoods/contributions/` ([mobile](05-chis-livelihoods/contributions/mobile.png) · [tablet](05-chis-livelihoods/contributions/tablet.png) · [desktop](05-chis-livelihoods/contributions/desktop.png))
- **Claims / access** — `05-chis-livelihoods/claims-access/` ([mobile](05-chis-livelihoods/claims-access/mobile.png) · [tablet](05-chis-livelihoods/claims-access/tablet.png) · [desktop](05-chis-livelihoods/claims-access/desktop.png))
- **IGA participation entry** — `05-chis-livelihoods/iga-participation-entry/` ([mobile](05-chis-livelihoods/iga-participation-entry/mobile.png) · [tablet](05-chis-livelihoods/iga-participation-entry/tablet.png) · [desktop](05-chis-livelihoods/iga-participation-entry/desktop.png))

### [06-facility-dashboard](06-facility-dashboard/README.md)

- **Facility overview** — `06-facility-dashboard/overview/` ([mobile](06-facility-dashboard/overview/mobile.png) · [tablet](06-facility-dashboard/overview/tablet.png) · [desktop](06-facility-dashboard/overview/desktop.png))
- **Catchment map** — `06-facility-dashboard/catchment-map/` ([mobile](06-facility-dashboard/catchment-map/mobile.png) · [tablet](06-facility-dashboard/catchment-map/tablet.png) · [desktop](06-facility-dashboard/catchment-map/desktop.png))
- **Open referrals** — `06-facility-dashboard/open-referrals/` ([mobile](06-facility-dashboard/open-referrals/mobile.png) · [tablet](06-facility-dashboard/open-referrals/tablet.png) · [desktop](06-facility-dashboard/open-referrals/desktop.png))
- **Stock signal** — `06-facility-dashboard/stock-signal/` ([mobile](06-facility-dashboard/stock-signal/mobile.png) · [tablet](06-facility-dashboard/stock-signal/tablet.png) · [desktop](06-facility-dashboard/stock-signal/desktop.png))
- **Outreach priorities** — `06-facility-dashboard/outreach-priorities/` ([mobile](06-facility-dashboard/outreach-priorities/mobile.png) · [tablet](06-facility-dashboard/outreach-priorities/tablet.png) · [desktop](06-facility-dashboard/outreach-priorities/desktop.png))
- **Clinical share confirm** — `06-facility-dashboard/clinical-share-confirm/` ([mobile](06-facility-dashboard/clinical-share-confirm/mobile.png) · [tablet](06-facility-dashboard/clinical-share-confirm/tablet.png) · [desktop](06-facility-dashboard/clinical-share-confirm/desktop.png))
- **Manual case signal** — `06-facility-dashboard/manual-case-signal/` ([mobile](06-facility-dashboard/manual-case-signal/mobile.png) · [tablet](06-facility-dashboard/manual-case-signal/tablet.png) · [desktop](06-facility-dashboard/manual-case-signal/desktop.png))

### [07-referrals-desk](07-referrals-desk/README.md)

- **Referrals desk** — `07-referrals-desk/referral-queue/` ([mobile](07-referrals-desk/referral-queue/mobile.png) · [tablet](07-referrals-desk/referral-queue/tablet.png) · [desktop](07-referrals-desk/referral-queue/desktop.png))
- **Referral detail** — `07-referrals-desk/referral-detail/` ([mobile](07-referrals-desk/referral-detail/mobile.png) · [tablet](07-referrals-desk/referral-detail/tablet.png) · [desktop](07-referrals-desk/referral-detail/desktop.png))
- **Outcome feed-back** — `07-referrals-desk/outcome-feed-back/` ([mobile](07-referrals-desk/outcome-feed-back/mobile.png) · [tablet](07-referrals-desk/outcome-feed-back/tablet.png) · [desktop](07-referrals-desk/outcome-feed-back/desktop.png))

### [08-emr-connector](08-emr-connector/README.md)

- **EMR / HMS connector** — `08-emr-connector/connector-status/` ([mobile](08-emr-connector/connector-status/mobile.png) · [tablet](08-emr-connector/connector-status/tablet.png) · [desktop](08-emr-connector/connector-status/desktop.png))
- **API scopes setup** — `08-emr-connector/api-scopes-setup/` ([mobile](08-emr-connector/api-scopes-setup/mobile.png) · [tablet](08-emr-connector/api-scopes-setup/tablet.png) · [desktop](08-emr-connector/api-scopes-setup/desktop.png))
- **Push event log** — `08-emr-connector/push-event-log/` ([mobile](08-emr-connector/push-event-log/mobile.png) · [tablet](08-emr-connector/push-event-log/tablet.png) · [desktop](08-emr-connector/push-event-log/desktop.png))
- **Facility onboarding** — `08-emr-connector/facility-onboarding/` ([mobile](08-emr-connector/facility-onboarding/mobile.png) · [tablet](08-emr-connector/facility-onboarding/tablet.png) · [desktop](08-emr-connector/facility-onboarding/desktop.png))

### [09-intelligence](09-intelligence/README.md)

- **Ingest & sync** — `09-intelligence/ingest-pipeline/` ([mobile](09-intelligence/ingest-pipeline/mobile.png) · [tablet](09-intelligence/ingest-pipeline/tablet.png) · [desktop](09-intelligence/ingest-pipeline/desktop.png))
- **AI / predictive** — `09-intelligence/ai-risk-scores/` ([mobile](09-intelligence/ai-risk-scores/mobile.png) · [tablet](09-intelligence/ai-risk-scores/tablet.png) · [desktop](09-intelligence/ai-risk-scores/desktop.png))
- **GIS maps** — `09-intelligence/gis-explorer/` ([mobile](09-intelligence/gis-explorer/mobile.png) · [tablet](09-intelligence/gis-explorer/tablet.png) · [desktop](09-intelligence/gis-explorer/desktop.png))
- **Climate fusion** — `09-intelligence/climate-fusion/` ([mobile](09-intelligence/climate-fusion/mobile.png) · [tablet](09-intelligence/climate-fusion/tablet.png) · [desktop](09-intelligence/climate-fusion/desktop.png))
- **Alerts & worklists engine** — `09-intelligence/alerts-worklists-engine/` ([mobile](09-intelligence/alerts-worklists-engine/mobile.png) · [tablet](09-intelligence/alerts-worklists-engine/tablet.png) · [desktop](09-intelligence/alerts-worklists-engine/desktop.png))
- **Feeder health board** — `09-intelligence/feeder-health-board/` ([mobile](09-intelligence/feeder-health-board/mobile.png) · [tablet](09-intelligence/feeder-health-board/tablet.png) · [desktop](09-intelligence/feeder-health-board/desktop.png))

### [10-district-moh](10-district-moh/README.md)

- **Population map** — `10-district-moh/population-map/` ([mobile](10-district-moh/population-map/mobile.png) · [tablet](10-district-moh/population-map/tablet.png) · [desktop](10-district-moh/population-map/desktop.png))
- **Early warnings** — `10-district-moh/early-warnings/` ([mobile](10-district-moh/early-warnings/mobile.png) · [tablet](10-district-moh/early-warnings/tablet.png) · [desktop](10-district-moh/early-warnings/desktop.png))
- **Deploy action** — `10-district-moh/action-deploy/` ([mobile](10-district-moh/action-deploy/mobile.png) · [tablet](10-district-moh/action-deploy/tablet.png) · [desktop](10-district-moh/action-deploy/desktop.png))
- **Cascade M&E planning** — `10-district-moh/cascade-planning/` ([mobile](10-district-moh/cascade-planning/mobile.png) · [tablet](10-district-moh/cascade-planning/tablet.png) · [desktop](10-district-moh/cascade-planning/desktop.png))

### [11-ngo-partner](11-ngo-partner/README.md)

- **Programme monitoring** — `11-ngo-partner/programme-monitoring/` ([mobile](11-ngo-partner/programme-monitoring/mobile.png) · [tablet](11-ngo-partner/programme-monitoring/tablet.png) · [desktop](11-ngo-partner/programme-monitoring/desktop.png))
- **Impact evidence** — `11-ngo-partner/impact-evidence/` ([mobile](11-ngo-partner/impact-evidence/mobile.png) · [tablet](11-ngo-partner/impact-evidence/tablet.png) · [desktop](11-ngo-partner/impact-evidence/desktop.png))
- **Field dataset upload** — `11-ngo-partner/field-dataset-upload/` ([mobile](11-ngo-partner/field-dataset-upload/mobile.png) · [tablet](11-ngo-partner/field-dataset-upload/tablet.png) · [desktop](11-ngo-partner/field-dataset-upload/desktop.png))
- **Partner indicator entry** — `11-ngo-partner/partner-indicator-entry/` ([mobile](11-ngo-partner/partner-indicator-entry/mobile.png) · [tablet](11-ngo-partner/partner-indicator-entry/tablet.png) · [desktop](11-ngo-partner/partner-indicator-entry/desktop.png))

### [12-research-exports](12-research-exports/README.md)

- **Evidence catalog** — `12-research-exports/evidence-catalog/` ([mobile](12-research-exports/evidence-catalog/mobile.png) · [tablet](12-research-exports/evidence-catalog/tablet.png) · [desktop](12-research-exports/evidence-catalog/desktop.png))
- **Export request** — `12-research-exports/export-request/` ([mobile](12-research-exports/export-request/mobile.png) · [tablet](12-research-exports/export-request/tablet.png) · [desktop](12-research-exports/export-request/desktop.png))
- **Research contribution upload** — `12-research-exports/research-contribution-upload/` ([mobile](12-research-exports/research-contribution-upload/mobile.png) · [tablet](12-research-exports/research-contribution-upload/tablet.png) · [desktop](12-research-exports/research-contribution-upload/desktop.png))

### [13-admin-consent](13-admin-consent/README.md)

- **Org · catchment · facilities** — `13-admin-consent/org-catchment/` ([mobile](13-admin-consent/org-catchment/mobile.png) · [tablet](13-admin-consent/org-catchment/tablet.png) · [desktop](13-admin-consent/org-catchment/desktop.png))
- **Users & roles** — `13-admin-consent/users-roles/` ([mobile](13-admin-consent/users-roles/mobile.png) · [tablet](13-admin-consent/users-roles/tablet.png) · [desktop](13-admin-consent/users-roles/desktop.png))
- **Consent & privacy** — `13-admin-consent/consent-privacy/` ([mobile](13-admin-consent/consent-privacy/mobile.png) · [tablet](13-admin-consent/consent-privacy/tablet.png) · [desktop](13-admin-consent/consent-privacy/desktop.png))
- **EMR API access** — `13-admin-consent/emr-api-access/` ([mobile](13-admin-consent/emr-api-access/mobile.png) · [tablet](13-admin-consent/emr-api-access/tablet.png) · [desktop](13-admin-consent/emr-api-access/desktop.png))
- **Feeder party registry** — `13-admin-consent/feeder-party-registry/` ([mobile](13-admin-consent/feeder-party-registry/mobile.png) · [tablet](13-admin-consent/feeder-party-registry/tablet.png) · [desktop](13-admin-consent/feeder-party-registry/desktop.png))

### [14-schools-health](14-schools-health/README.md)

- **School health home** — `14-schools-health/school-home/` ([mobile](14-schools-health/school-home/mobile.png) · [tablet](14-schools-health/school-home/tablet.png) · [desktop](14-schools-health/school-home/desktop.png))
- **Health education session** — `14-schools-health/health-education-session/` ([mobile](14-schools-health/health-education-session/mobile.png) · [tablet](14-schools-health/health-education-session/tablet.png) · [desktop](14-schools-health/health-education-session/desktop.png))
- **Learner screening entry** — `14-schools-health/learner-screening-entry/` ([mobile](14-schools-health/learner-screening-entry/mobile.png) · [tablet](14-schools-health/learner-screening-entry/tablet.png) · [desktop](14-schools-health/learner-screening-entry/desktop.png))
- **Absenteeism & wellness** — `14-schools-health/absenteeism-wellness/` ([mobile](14-schools-health/absenteeism-wellness/mobile.png) · [tablet](14-schools-health/absenteeism-wellness/tablet.png) · [desktop](14-schools-health/absenteeism-wellness/desktop.png))
- **School sync status** — `14-schools-health/school-sync-status/` ([mobile](14-schools-health/school-sync-status/mobile.png) · [tablet](14-schools-health/school-sync-status/tablet.png) · [desktop](14-schools-health/school-sync-status/desktop.png))

### [15-pharmacy-outlets](15-pharmacy-outlets/README.md)

- **Pharmacy outlet home** — `15-pharmacy-outlets/pharmacy-home/` ([mobile](15-pharmacy-outlets/pharmacy-home/mobile.png) · [tablet](15-pharmacy-outlets/pharmacy-home/tablet.png) · [desktop](15-pharmacy-outlets/pharmacy-home/desktop.png))
- **Stock levels entry** — `15-pharmacy-outlets/stock-levels-entry/` ([mobile](15-pharmacy-outlets/stock-levels-entry/mobile.png) · [tablet](15-pharmacy-outlets/stock-levels-entry/tablet.png) · [desktop](15-pharmacy-outlets/stock-levels-entry/desktop.png))
- **Dispense log** — `15-pharmacy-outlets/dispense-log/` ([mobile](15-pharmacy-outlets/dispense-log/mobile.png) · [tablet](15-pharmacy-outlets/dispense-log/tablet.png) · [desktop](15-pharmacy-outlets/dispense-log/desktop.png))
- **Common complaints** — `15-pharmacy-outlets/common-complaints/` ([mobile](15-pharmacy-outlets/common-complaints/mobile.png) · [tablet](15-pharmacy-outlets/common-complaints/tablet.png) · [desktop](15-pharmacy-outlets/common-complaints/desktop.png))
- **Pre-stock acknowledgement** — `15-pharmacy-outlets/prestock-ack/` ([mobile](15-pharmacy-outlets/prestock-ack/mobile.png) · [tablet](15-pharmacy-outlets/prestock-ack/tablet.png) · [desktop](15-pharmacy-outlets/prestock-ack/desktop.png))

### [16-labs-poc](16-labs-poc/README.md)

- **Lab / PoC home** — `16-labs-poc/lab-home/` ([mobile](16-labs-poc/lab-home/mobile.png) · [tablet](16-labs-poc/lab-home/tablet.png) · [desktop](16-labs-poc/lab-home/desktop.png))
- **Result entry** — `16-labs-poc/result-entry/` ([mobile](16-labs-poc/result-entry/mobile.png) · [tablet](16-labs-poc/result-entry/tablet.png) · [desktop](16-labs-poc/result-entry/desktop.png))
- **Batch results upload** — `16-labs-poc/batch-results-upload/` ([mobile](16-labs-poc/batch-results-upload/mobile.png) · [tablet](16-labs-poc/batch-results-upload/tablet.png) · [desktop](16-labs-poc/batch-results-upload/desktop.png))
- **Result queue** — `16-labs-poc/result-queue/` ([mobile](16-labs-poc/result-queue/mobile.png) · [tablet](16-labs-poc/result-queue/tablet.png) · [desktop](16-labs-poc/result-queue/desktop.png))

### [17-corporate-wellness](17-corporate-wellness/README.md)

- **Corporate wellness home** — `17-corporate-wellness/corporate-home/` ([mobile](17-corporate-wellness/corporate-home/mobile.png) · [tablet](17-corporate-wellness/corporate-home/tablet.png) · [desktop](17-corporate-wellness/corporate-home/desktop.png))
- **Camp vitals entry** — `17-corporate-wellness/camp-vitals-entry/` ([mobile](17-corporate-wellness/camp-vitals-entry/mobile.png) · [tablet](17-corporate-wellness/camp-vitals-entry/tablet.png) · [desktop](17-corporate-wellness/camp-vitals-entry/desktop.png))
- **Camp summary push** — `17-corporate-wellness/camp-summary-push/` ([mobile](17-corporate-wellness/camp-summary-push/mobile.png) · [tablet](17-corporate-wellness/camp-summary-push/tablet.png) · [desktop](17-corporate-wellness/camp-summary-push/desktop.png))
- **Occupational flags** — `17-corporate-wellness/occupational-flags/` ([mobile](17-corporate-wellness/occupational-flags/mobile.png) · [tablet](17-corporate-wellness/occupational-flags/tablet.png) · [desktop](17-corporate-wellness/occupational-flags/desktop.png))

### [18-mch-touchpoints](18-mch-touchpoints/README.md)

- **MCH touchpoints home** — `18-mch-touchpoints/mch-home/` ([mobile](18-mch-touchpoints/mch-home/mobile.png) · [tablet](18-mch-touchpoints/mch-home/tablet.png) · [desktop](18-mch-touchpoints/mch-home/desktop.png))
- **ANC visit entry** — `18-mch-touchpoints/anc-visit-entry/` ([mobile](18-mch-touchpoints/anc-visit-entry/mobile.png) · [tablet](18-mch-touchpoints/anc-visit-entry/tablet.png) · [desktop](18-mch-touchpoints/anc-visit-entry/desktop.png))
- **PNC visit entry** — `18-mch-touchpoints/pnc-visit-entry/` ([mobile](18-mch-touchpoints/pnc-visit-entry/mobile.png) · [tablet](18-mch-touchpoints/pnc-visit-entry/tablet.png) · [desktop](18-mch-touchpoints/pnc-visit-entry/desktop.png))
- **Immunisation entry** — `18-mch-touchpoints/immunisation-entry/` ([mobile](18-mch-touchpoints/immunisation-entry/mobile.png) · [tablet](18-mch-touchpoints/immunisation-entry/tablet.png) · [desktop](18-mch-touchpoints/immunisation-entry/desktop.png))
- **Nutrition monitoring** — `18-mch-touchpoints/nutrition-monitoring/` ([mobile](18-mch-touchpoints/nutrition-monitoring/mobile.png) · [tablet](18-mch-touchpoints/nutrition-monitoring/tablet.png) · [desktop](18-mch-touchpoints/nutrition-monitoring/desktop.png))

### [19-ncd-gericare](19-ncd-gericare/README.md)

- **NCD / Gericare home** — `19-ncd-gericare/cohort-home/` ([mobile](19-ncd-gericare/cohort-home/mobile.png) · [tablet](19-ncd-gericare/cohort-home/tablet.png) · [desktop](19-ncd-gericare/cohort-home/desktop.png))
- **Cohort visit entry** — `19-ncd-gericare/cohort-visit-entry/` ([mobile](19-ncd-gericare/cohort-visit-entry/mobile.png) · [tablet](19-ncd-gericare/cohort-visit-entry/tablet.png) · [desktop](19-ncd-gericare/cohort-visit-entry/desktop.png))
- **BP screening batch** — `19-ncd-gericare/bp-screening-batch/` ([mobile](19-ncd-gericare/bp-screening-batch/mobile.png) · [tablet](19-ncd-gericare/bp-screening-batch/tablet.png) · [desktop](19-ncd-gericare/bp-screening-batch/desktop.png))
- **Stroke / NCD risk flags** — `19-ncd-gericare/stroke-risk-flags/` ([mobile](19-ncd-gericare/stroke-risk-flags/mobile.png) · [tablet](19-ncd-gericare/stroke-risk-flags/tablet.png) · [desktop](19-ncd-gericare/stroke-risk-flags/desktop.png))

### [20-hmis-dhis2](20-hmis-dhis2/README.md)

- **HMIS / DHIS2 home** — `20-hmis-dhis2/hmis-home/` ([mobile](20-hmis-dhis2/hmis-home/mobile.png) · [tablet](20-hmis-dhis2/hmis-home/tablet.png) · [desktop](20-hmis-dhis2/hmis-home/desktop.png))
- **Dataset mapping** — `20-hmis-dhis2/dataset-mapping/` ([mobile](20-hmis-dhis2/dataset-mapping/mobile.png) · [tablet](20-hmis-dhis2/dataset-mapping/tablet.png) · [desktop](20-hmis-dhis2/dataset-mapping/desktop.png))
- **Aggregate push / pull** — `20-hmis-dhis2/aggregate-push-pull/` ([mobile](20-hmis-dhis2/aggregate-push-pull/mobile.png) · [tablet](20-hmis-dhis2/aggregate-push-pull/tablet.png) · [desktop](20-hmis-dhis2/aggregate-push-pull/desktop.png))
- **HMIS audit** — `20-hmis-dhis2/hmis-audit/` ([mobile](20-hmis-dhis2/hmis-audit/mobile.png) · [tablet](20-hmis-dhis2/hmis-audit/tablet.png) · [desktop](20-hmis-dhis2/hmis-audit/desktop.png))

### [21-community-events](21-community-events/README.md)

- **Community events home** — `21-community-events/events-home/` ([mobile](21-community-events/events-home/mobile.png) · [tablet](21-community-events/events-home/tablet.png) · [desktop](21-community-events/events-home/desktop.png))
- **Outreach event log** — `21-community-events/outreach-event-log/` ([mobile](21-community-events/outreach-event-log/mobile.png) · [tablet](21-community-events/outreach-event-log/tablet.png) · [desktop](21-community-events/outreach-event-log/desktop.png))
- **Community dialogue** — `21-community-events/community-dialogue/` ([mobile](21-community-events/community-dialogue/mobile.png) · [tablet](21-community-events/community-dialogue/tablet.png) · [desktop](21-community-events/community-dialogue/desktop.png))
- **Participation register** — `21-community-events/participation-register/` ([mobile](21-community-events/participation-register/mobile.png) · [tablet](21-community-events/participation-register/tablet.png) · [desktop](21-community-events/participation-register/desktop.png))

### [22-climate-feeds](22-climate-feeds/README.md)

- **Climate feeds home** — `22-climate-feeds/climate-home/` ([mobile](22-climate-feeds/climate-home/mobile.png) · [tablet](22-climate-feeds/climate-home/tablet.png) · [desktop](22-climate-feeds/climate-home/desktop.png))
- **Rainfall & temperature** — `22-climate-feeds/rainfall-temperature/` ([mobile](22-climate-feeds/rainfall-temperature/mobile.png) · [tablet](22-climate-feeds/rainfall-temperature/tablet.png) · [desktop](22-climate-feeds/rainfall-temperature/desktop.png))
- **Extremes · flood · heat** — `22-climate-feeds/extremes-flood-heat/` ([mobile](22-climate-feeds/extremes-flood-heat/mobile.png) · [tablet](22-climate-feeds/extremes-flood-heat/tablet.png) · [desktop](22-climate-feeds/extremes-flood-heat/desktop.png))
- **Feed config & audit** — `22-climate-feeds/feed-config-audit/` ([mobile](22-climate-feeds/feed-config-audit/mobile.png) · [tablet](22-climate-feeds/feed-config-audit/tablet.png) · [desktop](22-climate-feeds/feed-config-audit/desktop.png))

## Regenerate

```bash
python app-ui/generate_mockups.py
```

## Sources

- `.cursor/app-write-up.mdc`
- `app-flows/01-overview.md` … `06-mvp-phases.md` (especially `04-modules.md`)
