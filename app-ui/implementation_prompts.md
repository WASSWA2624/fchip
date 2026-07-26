# App UI — implementation prompts

Professional, actionable prompts for every `app-ui` pack that has visual specimens.
Each leaf folder contains `implementation_prompt.md` ready to paste into an agent session.

Regenerate:

```bash
python app-ui/tool/generate_implementation_prompts.py
```

## How to use

1. Pick the next unfinished screen from `frontend/dev-plan/slices/chronology.yaml` (screens only).
2. Open that folder's `implementation_prompt.md` and paste it into the agent.
3. For missing shared chrome, run the matching **component** or **layout** prompt first.
4. Follow the playbook in `frontend/dev-plan/25-slice-execution-playbook.md`.

## Inventory (186 prompts)

| Module | Screens | Components | Layouts |
| --- | ---: | ---: | ---: |
| `00-shared` | 12 | 42 | 17 |
| `01-chw-vht-mobile` | 14 | 0 | 0 |
| `02-intelligence` | 7 | 0 | 0 |
| `03-cascade-metrics` | 3 | 0 | 0 |
| `04-facility-dashboard` | 8 | 0 | 0 |
| `05-referrals-desk` | 4 | 0 | 0 |
| `06-emr-connector` | 5 | 0 | 0 |
| `07-climate-feeds` | 4 | 0 | 0 |
| `08-district-moh` | 5 | 0 | 0 |
| `09-community-caregiver` | 4 | 0 | 0 |
| `10-outreach-school-health` | 5 | 0 | 0 |
| `11-admin-consent` | 5 | 0 | 0 |
| `12-insurance-insights` | 3 | 0 | 0 |
| `13-chis-livelihoods` | 4 | 0 | 0 |
| `14-ngo-partner` | 5 | 0 | 0 |
| `15-schools-health` | 5 | 0 | 0 |
| `16-pharmacy-outlets` | 5 | 0 | 0 |
| `17-labs-poc` | 4 | 0 | 0 |
| `18-corporate-wellness` | 4 | 0 | 0 |
| `19-mch-touchpoints` | 5 | 0 | 0 |
| `20-ncd-gericare` | 4 | 0 | 0 |
| `21-hmis-dhis2` | 4 | 0 | 0 |
| `22-community-events` | 4 | 0 | 0 |
| `23-research-exports` | 4 | 0 | 0 |

## Prompt index

### `00-shared`

- **component** [`brand/cascade-footer`](00-shared/components/brand/cascade-footer/implementation_prompt.md)
- **component** [`brand/logo-lockup`](00-shared/components/brand/logo-lockup/implementation_prompt.md)
- **component** [`brand/master-loop-badge`](00-shared/components/brand/master-loop-badge/implementation_prompt.md)
- **component** [`brand/slogan-line`](00-shared/components/brand/slogan-line/implementation_prompt.md)
- **component** [`buttons/danger-cta`](00-shared/components/buttons/danger-cta/implementation_prompt.md)
- **component** [`buttons/primary-cta`](00-shared/components/buttons/primary-cta/implementation_prompt.md)
- **component** [`buttons/secondary-cta`](00-shared/components/buttons/secondary-cta/implementation_prompt.md)
- **component** [`buttons/text-link`](00-shared/components/buttons/text-link/implementation_prompt.md)
- **component** [`cards/explainability-block`](00-shared/components/cards/explainability-block/implementation_prompt.md)
- **component** [`cards/list-row-card`](00-shared/components/cards/list-row-card/implementation_prompt.md)
- **component** [`cards/note-banner`](00-shared/components/cards/note-banner/implementation_prompt.md)
- **component** [`cards/stat-card`](00-shared/components/cards/stat-card/implementation_prompt.md)
- **component** [`cards/stat-card-row`](00-shared/components/cards/stat-card-row/implementation_prompt.md)
- **component** [`cards/warn-banner`](00-shared/components/cards/warn-banner/implementation_prompt.md)
- **component** [`chips/filter-chip-row`](00-shared/components/chips/filter-chip-row/implementation_prompt.md)
- **component** [`chips/offline-ready-chip`](00-shared/components/chips/offline-ready-chip/implementation_prompt.md)
- **component** [`chips/risk-chip`](00-shared/components/chips/risk-chip/implementation_prompt.md)
- **component** [`chips/status-chip`](00-shared/components/chips/status-chip/implementation_prompt.md)
- **component** [`data-display/feeder-health-pill`](00-shared/components/data-display/feeder-health-pill/implementation_prompt.md)
- **component** [`data-display/hotspot-map`](00-shared/components/data-display/hotspot-map/implementation_prompt.md)
- **component** [`data-display/metrics-spark-row`](00-shared/components/data-display/metrics-spark-row/implementation_prompt.md)
- **component** [`data-display/queue-item`](00-shared/components/data-display/queue-item/implementation_prompt.md)
- **component** [`data-display/timeline-step`](00-shared/components/data-display/timeline-step/implementation_prompt.md)
- **component** [`feedback/empty-state`](00-shared/components/feedback/empty-state/implementation_prompt.md)
- **component** [`feedback/error-inline`](00-shared/components/feedback/error-inline/implementation_prompt.md)
- **component** [`feedback/loading-skeleton`](00-shared/components/feedback/loading-skeleton/implementation_prompt.md)
- **component** [`feedback/success-toast`](00-shared/components/feedback/success-toast/implementation_prompt.md)
- **component** [`feedback/sync-status-strip`](00-shared/components/feedback/sync-status-strip/implementation_prompt.md)
- **component** [`forms/consent-toggle`](00-shared/components/forms/consent-toggle/implementation_prompt.md)
- **component** [`forms/file-upload-field`](00-shared/components/forms/file-upload-field/implementation_prompt.md)
- **component** [`forms/form-stack`](00-shared/components/forms/form-stack/implementation_prompt.md)
- **component** [`forms/labeled-field`](00-shared/components/forms/labeled-field/implementation_prompt.md)
- **component** [`forms/select-field`](00-shared/components/forms/select-field/implementation_prompt.md)
- **component** [`navigation/bottom-nav-caregiver`](00-shared/components/navigation/bottom-nav-caregiver/implementation_prompt.md)
- **component** [`navigation/bottom-nav-feeder`](00-shared/components/navigation/bottom-nav-feeder/implementation_prompt.md)
- **component** [`navigation/bottom-nav-field`](00-shared/components/navigation/bottom-nav-field/implementation_prompt.md)
- **component** [`navigation/bottom-nav-insurance`](00-shared/components/navigation/bottom-nav-insurance/implementation_prompt.md)
- **component** [`navigation/bottom-nav-intel`](00-shared/components/navigation/bottom-nav-intel/implementation_prompt.md)
- **component** [`navigation/role-picker-row`](00-shared/components/navigation/role-picker-row/implementation_prompt.md)
- **component** [`navigation/section-header`](00-shared/components/navigation/section-header/implementation_prompt.md)
- **component** [`navigation/side-nav-desktop`](00-shared/components/navigation/side-nav-desktop/implementation_prompt.md)
- **component** [`navigation/top-app-bar`](00-shared/components/navigation/top-app-bar/implementation_prompt.md)
- **layout** [`auth-centered-card`](00-shared/layouts/auth-centered-card/implementation_prompt.md)
- **layout** [`connector-status`](00-shared/layouts/connector-status/implementation_prompt.md)
- **layout** [`dashboard-metrics`](00-shared/layouts/dashboard-metrics/implementation_prompt.md)
- **layout** [`desktop-sidebar-shell`](00-shared/layouts/desktop-sidebar-shell/implementation_prompt.md)
- **layout** [`detail-action`](00-shared/layouts/detail-action/implementation_prompt.md)
- **layout** [`dual-pane-desktop`](00-shared/layouts/dual-pane-desktop/implementation_prompt.md)
- **layout** [`empty-state-shell`](00-shared/layouts/empty-state-shell/implementation_prompt.md)
- **layout** [`feeder-home`](00-shared/layouts/feeder-home/implementation_prompt.md)
- **layout** [`field-mobile-shell`](00-shared/layouts/field-mobile-shell/implementation_prompt.md)
- **layout** [`field-tablet-shell`](00-shared/layouts/field-tablet-shell/implementation_prompt.md)
- **layout** [`form-capture`](00-shared/layouts/form-capture/implementation_prompt.md)
- **layout** [`insurance-prevention`](00-shared/layouts/insurance-prevention/implementation_prompt.md)
- **layout** [`list-worklist`](00-shared/layouts/list-worklist/implementation_prompt.md)
- **layout** [`map-explorer`](00-shared/layouts/map-explorer/implementation_prompt.md)
- **layout** [`queue-desk`](00-shared/layouts/queue-desk/implementation_prompt.md)
- **layout** [`settings-admin`](00-shared/layouts/settings-admin/implementation_prompt.md)
- **layout** [`upload-batch`](00-shared/layouts/upload-batch/implementation_prompt.md)
- **screen** [`FCHIP`](00-shared/01-splash/implementation_prompt.md) · `S-001`
- **screen** [`Create account`](00-shared/02-create-account/implementation_prompt.md) · `S-002`
- **screen** [`Sign in`](00-shared/03-login/implementation_prompt.md) · `S-003`
- **screen** [`Reset password`](00-shared/04-forgot-password/implementation_prompt.md) · `S-004`
- **screen** [`Consent first`](00-shared/05-consent-first-onboarding/implementation_prompt.md) · `S-005`
- **screen** [`Offline PIN`](00-shared/06-offline-pin-lock/implementation_prompt.md) · `S-006`
- **screen** [`Session locked`](00-shared/07-session-locked/implementation_prompt.md) · `S-007`
- **screen** [`Choose your workspace`](00-shared/08-role-surface-picker/implementation_prompt.md) · `S-008`
- **screen** [`Notifications`](00-shared/09-notifications-center/implementation_prompt.md) · `S-009`
- **screen** [`Access denied`](00-shared/10-access-denied/implementation_prompt.md) · `S-010`
- **screen** [`Page not found`](00-shared/11-not-found/implementation_prompt.md) · `S-011`
- **screen** [`Language & appearance`](00-shared/12-preferences/implementation_prompt.md) · `S-012`

### `01-chw-vht-mobile`

- **screen** [`Today’s worklist`](01-chw-vht-mobile/01-worklist-home/implementation_prompt.md) · `S-013`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/02-worklist-empty/implementation_prompt.md) · `S-014`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/03-worklist-loading/implementation_prompt.md) · `S-015`
- **screen** [`Household visit`](01-chw-vht-mobile/04-household-visit-form/implementation_prompt.md) · `S-016`
- **screen** [`Symptoms & vitals`](01-chw-vht-mobile/05-symptoms-vitals/implementation_prompt.md) · `S-017`
- **screen** [`Maternal / child`](01-chw-vht-mobile/06-maternal-child-indicators/implementation_prompt.md) · `S-018`
- **screen** [`Visit saved`](01-chw-vht-mobile/07-visit-saved/implementation_prompt.md) · `S-019`
- **screen** [`Create referral`](01-chw-vht-mobile/08-create-referral/implementation_prompt.md) · `S-020`
- **screen** [`Referral sent`](01-chw-vht-mobile/09-referral-status/implementation_prompt.md) · `S-021`
- **screen** [`Alerts inbox`](01-chw-vht-mobile/10-alerts-inbox/implementation_prompt.md) · `S-022`
- **screen** [`Act on alert`](01-chw-vht-mobile/11-alert-follow-up/implementation_prompt.md) · `S-023`
- **screen** [`Sync status`](01-chw-vht-mobile/12-sync-status/implementation_prompt.md) · `S-024`
- **screen** [`Sync failed`](01-chw-vht-mobile/13-sync-failed/implementation_prompt.md) · `S-025`
- **screen** [`Review sync conflict`](01-chw-vht-mobile/14-sync-conflict/implementation_prompt.md) · `S-026`

### `02-intelligence`

- **screen** [`Ingest & sync`](02-intelligence/01-ingest-pipeline/implementation_prompt.md) · `S-027`
- **screen** [`Feeder health board`](02-intelligence/02-feeder-health-board/implementation_prompt.md) · `S-028`
- **screen** [`GIS maps`](02-intelligence/03-gis-explorer/implementation_prompt.md) · `S-052`
- **screen** [`Climate fusion`](02-intelligence/04-climate-fusion/implementation_prompt.md) · `S-053`
- **screen** [`AI / predictive`](02-intelligence/05-ai-risk-scores/implementation_prompt.md) · `S-054`
- **screen** [`Alerts & worklists engine`](02-intelligence/06-alerts-worklists-engine/implementation_prompt.md) · `S-055`
- **screen** [`Clinical support guidance`](02-intelligence/07-clinical-support-guidance/implementation_prompt.md) · `S-056`

### `03-cascade-metrics`

- **screen** [`Cascade metrics`](03-cascade-metrics/01-indicators-overview/implementation_prompt.md) · `S-029`
- **screen** [`Gap detection`](03-cascade-metrics/02-gap-detection/implementation_prompt.md) · `S-030`
- **screen** [`Partner reports`](03-cascade-metrics/03-partner-reports/implementation_prompt.md) · `S-031`

### `04-facility-dashboard`

- **screen** [`Facility overview`](04-facility-dashboard/01-overview/implementation_prompt.md) · `S-032`
- **screen** [`Catchment map`](04-facility-dashboard/02-catchment-map/implementation_prompt.md) · `S-033`
- **screen** [`Referral summary`](04-facility-dashboard/03-open-referrals/implementation_prompt.md) · `S-034`
- **screen** [`Stock signal`](04-facility-dashboard/04-stock-signal/implementation_prompt.md) · `S-035`
- **screen** [`Outreach priorities`](04-facility-dashboard/05-outreach-priorities/implementation_prompt.md) · `S-036`
- **screen** [`Clinical share confirm`](04-facility-dashboard/06-clinical-share-confirm/implementation_prompt.md) · `S-037`
- **screen** [`Manual case signal`](04-facility-dashboard/07-manual-case-signal/implementation_prompt.md) · `S-038`
- **screen** [`Medicine demand forecast`](04-facility-dashboard/08-medicine-demand-forecast/implementation_prompt.md) · `S-122`

### `05-referrals-desk`

- **screen** [`Referrals desk`](05-referrals-desk/01-referral-queue/implementation_prompt.md) · `S-039`
- **screen** [`Referrals desk`](05-referrals-desk/02-referral-queue-empty/implementation_prompt.md) · `S-040`
- **screen** [`Referral detail`](05-referrals-desk/03-referral-detail/implementation_prompt.md) · `S-041`
- **screen** [`Outcome feedback`](05-referrals-desk/04-outcome-feedback/implementation_prompt.md) · `S-042`

### `06-emr-connector`

- **screen** [`EMR / HMS connector`](06-emr-connector/01-connector-status/implementation_prompt.md) · `S-043`
- **screen** [`EMR / HMS connector`](06-emr-connector/02-connector-degraded/implementation_prompt.md) · `S-044`
- **screen** [`API scopes setup`](06-emr-connector/03-api-scopes-setup/implementation_prompt.md) · `S-045`
- **screen** [`Push event log`](06-emr-connector/04-push-event-log/implementation_prompt.md) · `S-046`
- **screen** [`Facility onboarding`](06-emr-connector/05-facility-onboarding/implementation_prompt.md) · `S-047`

### `07-climate-feeds`

- **screen** [`Climate feeds home`](07-climate-feeds/01-climate-home/implementation_prompt.md) · `S-048`
- **screen** [`Rainfall & temperature`](07-climate-feeds/02-rainfall-temperature/implementation_prompt.md) · `S-049`
- **screen** [`Extremes · flood · heat`](07-climate-feeds/03-extremes-flood-heat/implementation_prompt.md) · `S-050`
- **screen** [`Feed config & audit`](07-climate-feeds/04-feed-config-audit/implementation_prompt.md) · `S-051`

### `08-district-moh`

- **screen** [`Population map`](08-district-moh/01-population-map/implementation_prompt.md) · `S-057`
- **screen** [`Early warnings`](08-district-moh/02-early-warnings/implementation_prompt.md) · `S-058`
- **screen** [`Deploy action`](08-district-moh/03-action-deploy/implementation_prompt.md) · `S-059`
- **screen** [`Cascade M&E planning`](08-district-moh/04-cascade-planning/implementation_prompt.md) · `S-060`
- **screen** [`MoH national roll-up`](08-district-moh/05-national-roll-up/implementation_prompt.md) · `S-123`

### `09-community-caregiver`

- **screen** [`My household`](09-community-caregiver/01-my-household/implementation_prompt.md) · `S-061`
- **screen** [`Self-report`](09-community-caregiver/02-self-report/implementation_prompt.md) · `S-062`
- **screen** [`Guidance`](09-community-caregiver/03-guidance-hints/implementation_prompt.md) · `S-063`
- **screen** [`Household needs`](09-community-caregiver/04-household-needs-capture/implementation_prompt.md) · `S-064`

### `10-outreach-school-health`

- **screen** [`Campaign planner`](10-outreach-school-health/01-campaign-planner/implementation_prompt.md) · `S-065`
- **screen** [`Session log`](10-outreach-school-health/02-session-log/implementation_prompt.md) · `S-066`
- **screen** [`Coverage map`](10-outreach-school-health/03-coverage-map/implementation_prompt.md) · `S-067`
- **screen** [`Screening results entry`](10-outreach-school-health/04-screening-results-entry/implementation_prompt.md) · `S-068`
- **screen** [`Home-visit batch`](10-outreach-school-health/05-home-visit-batch-upload/implementation_prompt.md) · `S-069`

### `11-admin-consent`

- **screen** [`Org · catchment · facilities`](11-admin-consent/01-org-catchment/implementation_prompt.md) · `S-070`
- **screen** [`Users & roles`](11-admin-consent/02-users-roles/implementation_prompt.md) · `S-071`
- **screen** [`Consent & privacy`](11-admin-consent/03-consent-privacy/implementation_prompt.md) · `S-072`
- **screen** [`EMR API access`](11-admin-consent/04-emr-api-access/implementation_prompt.md) · `S-073`
- **screen** [`Feeder party registry`](11-admin-consent/05-feeder-party-registry/implementation_prompt.md) · `S-074`

### `12-insurance-insights`

- **screen** [`Prevention overview`](12-insurance-insights/01-prevention-overview/implementation_prompt.md) · `S-075`
- **screen** [`Risk cohort insights`](12-insurance-insights/02-risk-cohort-insights/implementation_prompt.md) · `S-076`
- **screen** [`Anonymised trends`](12-insurance-insights/03-anonymised-trends/implementation_prompt.md) · `S-077`

### `13-chis-livelihoods`

- **screen** [`CHIS enrolment`](13-chis-livelihoods/01-enrolment/implementation_prompt.md) · `S-078`
- **screen** [`Contributions`](13-chis-livelihoods/02-contributions/implementation_prompt.md) · `S-079`
- **screen** [`Claims / access`](13-chis-livelihoods/03-claims-access/implementation_prompt.md) · `S-080`
- **screen** [`IGA participation entry`](13-chis-livelihoods/04-iga-participation-entry/implementation_prompt.md) · `S-081`

### `14-ngo-partner`

- **screen** [`Programme monitoring`](14-ngo-partner/01-programme-monitoring/implementation_prompt.md) · `S-082`
- **screen** [`Impact evidence`](14-ngo-partner/02-impact-evidence/implementation_prompt.md) · `S-083`
- **screen** [`Training · skills analytics`](14-ngo-partner/03-training-skills-analytics/implementation_prompt.md) · `S-084`
- **screen** [`Field dataset upload`](14-ngo-partner/04-field-dataset-upload/implementation_prompt.md) · `S-085`
- **screen** [`Partner indicator entry`](14-ngo-partner/05-partner-indicator-entry/implementation_prompt.md) · `S-086`

### `15-schools-health`

- **screen** [`School health home`](15-schools-health/01-school-home/implementation_prompt.md) · `S-087`
- **screen** [`Health education session`](15-schools-health/02-health-education-session/implementation_prompt.md) · `S-088`
- **screen** [`Learner screening entry`](15-schools-health/03-learner-screening-entry/implementation_prompt.md) · `S-089`
- **screen** [`Absenteeism & wellness`](15-schools-health/04-absenteeism-wellness/implementation_prompt.md) · `S-090`
- **screen** [`School sync status`](15-schools-health/05-school-sync-status/implementation_prompt.md) · `S-091`

### `16-pharmacy-outlets`

- **screen** [`Pharmacy outlet home`](16-pharmacy-outlets/01-pharmacy-home/implementation_prompt.md) · `S-092`
- **screen** [`Stock levels entry`](16-pharmacy-outlets/02-stock-levels-entry/implementation_prompt.md) · `S-093`
- **screen** [`Dispense log`](16-pharmacy-outlets/03-dispense-log/implementation_prompt.md) · `S-094`
- **screen** [`Common complaints`](16-pharmacy-outlets/04-common-complaints/implementation_prompt.md) · `S-095`
- **screen** [`Pre-stock acknowledgement`](16-pharmacy-outlets/05-prestock-ack/implementation_prompt.md) · `S-096`

### `17-labs-poc`

- **screen** [`Lab / PoC home`](17-labs-poc/01-lab-home/implementation_prompt.md) · `S-097`
- **screen** [`Result entry`](17-labs-poc/02-result-entry/implementation_prompt.md) · `S-098`
- **screen** [`Batch results upload`](17-labs-poc/03-batch-results-upload/implementation_prompt.md) · `S-099`
- **screen** [`Result queue`](17-labs-poc/04-result-queue/implementation_prompt.md) · `S-100`

### `18-corporate-wellness`

- **screen** [`Corporate wellness home`](18-corporate-wellness/01-corporate-home/implementation_prompt.md) · `S-101`
- **screen** [`Camp vitals entry`](18-corporate-wellness/02-camp-vitals-entry/implementation_prompt.md) · `S-102`
- **screen** [`Camp summary push`](18-corporate-wellness/03-camp-summary-push/implementation_prompt.md) · `S-103`
- **screen** [`Occupational flags`](18-corporate-wellness/04-occupational-flags/implementation_prompt.md) · `S-104`

### `19-mch-touchpoints`

- **screen** [`MCH touchpoints home`](19-mch-touchpoints/01-mch-home/implementation_prompt.md) · `S-105`
- **screen** [`ANC visit entry`](19-mch-touchpoints/02-anc-visit-entry/implementation_prompt.md) · `S-106`
- **screen** [`PNC visit entry`](19-mch-touchpoints/03-pnc-visit-entry/implementation_prompt.md) · `S-107`
- **screen** [`Immunisation entry`](19-mch-touchpoints/04-immunisation-entry/implementation_prompt.md) · `S-108`
- **screen** [`Nutrition monitoring`](19-mch-touchpoints/05-nutrition-monitoring/implementation_prompt.md) · `S-109`

### `20-ncd-gericare`

- **screen** [`NCD / Gericare home`](20-ncd-gericare/01-cohort-home/implementation_prompt.md) · `S-110`
- **screen** [`Cohort visit entry`](20-ncd-gericare/02-cohort-visit-entry/implementation_prompt.md) · `S-111`
- **screen** [`BP screening batch`](20-ncd-gericare/03-bp-screening-batch/implementation_prompt.md) · `S-112`
- **screen** [`Stroke / NCD risk flags`](20-ncd-gericare/04-stroke-risk-flags/implementation_prompt.md) · `S-113`

### `21-hmis-dhis2`

- **screen** [`HMIS / DHIS2 home`](21-hmis-dhis2/01-hmis-home/implementation_prompt.md) · `S-114`
- **screen** [`Dataset mapping`](21-hmis-dhis2/02-dataset-mapping/implementation_prompt.md) · `S-115`
- **screen** [`Aggregate push / pull`](21-hmis-dhis2/03-aggregate-push-pull/implementation_prompt.md) · `S-116`
- **screen** [`HMIS audit`](21-hmis-dhis2/04-hmis-audit/implementation_prompt.md) · `S-117`

### `22-community-events`

- **screen** [`Community events home`](22-community-events/01-events-home/implementation_prompt.md) · `S-118`
- **screen** [`Outreach event log`](22-community-events/02-outreach-event-log/implementation_prompt.md) · `S-119`
- **screen** [`Community dialogue`](22-community-events/03-community-dialogue/implementation_prompt.md) · `S-120`
- **screen** [`Participation register`](22-community-events/04-participation-register/implementation_prompt.md) · `S-121`

### `23-research-exports`

- **screen** [`Evidence catalog`](23-research-exports/01-evidence-catalog/implementation_prompt.md) · `S-124`
- **screen** [`Export request`](23-research-exports/02-export-request/implementation_prompt.md) · `S-125`
- **screen** [`Research contribution upload`](23-research-exports/03-research-contribution-upload/implementation_prompt.md) · `S-126`
- **screen** [`Export under review`](23-research-exports/04-export-pending/implementation_prompt.md) · `S-127`

## Rules referenced across prompts

Root: `.cursor/mandatories.mdc`, `.cursor/app-write-up.mdc`

Frontend: `frontend/.cursor/index.mdc`, `product_delivery.mdc`, `feature_workflow.mdc`, `project_structure.mdc`, `components.mdc`, `layouts.mdc`, `ui-workspace.mdc`, `permissions.mdc`, `network_api.mdc`, `testing.mdc`, and related owners listed in each prompt.

Backend: `backend/.cursor/vertical-slice-delivery.mdc`, `module-creation.mdc`, `api.mdc`, `prisma.mdc`, `auth-security.mdc`, plus `backend/dev-plan/P016_slice_pairing.md`.

Plan: `frontend/dev-plan/00-execution-policy.md`, `25-slice-execution-playbook.md`, `slices/chronology.yaml`.
