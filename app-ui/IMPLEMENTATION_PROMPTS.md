# App UI — implementation prompts

Professional, actionable prompts for every `app-ui` pack that has visual specimens.
Each leaf folder contains `IMPLEMENTATION_PROMPT.md` ready to paste into an agent session.

Regenerate:

```bash
python app-ui/tool/generate_implementation_prompts.py
```

## How to use

1. Pick the next unfinished screen from `frontend/dev-plan/slices/chronology.yaml` (screens only).
2. Open that folder's `IMPLEMENTATION_PROMPT.md` and paste it into the agent.
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

- **component** [`brand/cascade-footer`](00-shared/components/brand/cascade-footer/IMPLEMENTATION_PROMPT.md)
- **component** [`brand/logo-lockup`](00-shared/components/brand/logo-lockup/IMPLEMENTATION_PROMPT.md)
- **component** [`brand/master-loop-badge`](00-shared/components/brand/master-loop-badge/IMPLEMENTATION_PROMPT.md)
- **component** [`brand/slogan-line`](00-shared/components/brand/slogan-line/IMPLEMENTATION_PROMPT.md)
- **component** [`buttons/danger-cta`](00-shared/components/buttons/danger-cta/IMPLEMENTATION_PROMPT.md)
- **component** [`buttons/primary-cta`](00-shared/components/buttons/primary-cta/IMPLEMENTATION_PROMPT.md)
- **component** [`buttons/secondary-cta`](00-shared/components/buttons/secondary-cta/IMPLEMENTATION_PROMPT.md)
- **component** [`buttons/text-link`](00-shared/components/buttons/text-link/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/explainability-block`](00-shared/components/cards/explainability-block/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/list-row-card`](00-shared/components/cards/list-row-card/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/note-banner`](00-shared/components/cards/note-banner/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/stat-card`](00-shared/components/cards/stat-card/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/stat-card-row`](00-shared/components/cards/stat-card-row/IMPLEMENTATION_PROMPT.md)
- **component** [`cards/warn-banner`](00-shared/components/cards/warn-banner/IMPLEMENTATION_PROMPT.md)
- **component** [`chips/filter-chip-row`](00-shared/components/chips/filter-chip-row/IMPLEMENTATION_PROMPT.md)
- **component** [`chips/offline-ready-chip`](00-shared/components/chips/offline-ready-chip/IMPLEMENTATION_PROMPT.md)
- **component** [`chips/risk-chip`](00-shared/components/chips/risk-chip/IMPLEMENTATION_PROMPT.md)
- **component** [`chips/status-chip`](00-shared/components/chips/status-chip/IMPLEMENTATION_PROMPT.md)
- **component** [`data-display/feeder-health-pill`](00-shared/components/data-display/feeder-health-pill/IMPLEMENTATION_PROMPT.md)
- **component** [`data-display/hotspot-map`](00-shared/components/data-display/hotspot-map/IMPLEMENTATION_PROMPT.md)
- **component** [`data-display/metrics-spark-row`](00-shared/components/data-display/metrics-spark-row/IMPLEMENTATION_PROMPT.md)
- **component** [`data-display/queue-item`](00-shared/components/data-display/queue-item/IMPLEMENTATION_PROMPT.md)
- **component** [`data-display/timeline-step`](00-shared/components/data-display/timeline-step/IMPLEMENTATION_PROMPT.md)
- **component** [`feedback/empty-state`](00-shared/components/feedback/empty-state/IMPLEMENTATION_PROMPT.md)
- **component** [`feedback/error-inline`](00-shared/components/feedback/error-inline/IMPLEMENTATION_PROMPT.md)
- **component** [`feedback/loading-skeleton`](00-shared/components/feedback/loading-skeleton/IMPLEMENTATION_PROMPT.md)
- **component** [`feedback/success-toast`](00-shared/components/feedback/success-toast/IMPLEMENTATION_PROMPT.md)
- **component** [`feedback/sync-status-strip`](00-shared/components/feedback/sync-status-strip/IMPLEMENTATION_PROMPT.md)
- **component** [`forms/consent-toggle`](00-shared/components/forms/consent-toggle/IMPLEMENTATION_PROMPT.md)
- **component** [`forms/file-upload-field`](00-shared/components/forms/file-upload-field/IMPLEMENTATION_PROMPT.md)
- **component** [`forms/form-stack`](00-shared/components/forms/form-stack/IMPLEMENTATION_PROMPT.md)
- **component** [`forms/labeled-field`](00-shared/components/forms/labeled-field/IMPLEMENTATION_PROMPT.md)
- **component** [`forms/select-field`](00-shared/components/forms/select-field/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/bottom-nav-caregiver`](00-shared/components/navigation/bottom-nav-caregiver/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/bottom-nav-feeder`](00-shared/components/navigation/bottom-nav-feeder/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/bottom-nav-field`](00-shared/components/navigation/bottom-nav-field/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/bottom-nav-insurance`](00-shared/components/navigation/bottom-nav-insurance/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/bottom-nav-intel`](00-shared/components/navigation/bottom-nav-intel/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/role-picker-row`](00-shared/components/navigation/role-picker-row/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/section-header`](00-shared/components/navigation/section-header/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/side-nav-desktop`](00-shared/components/navigation/side-nav-desktop/IMPLEMENTATION_PROMPT.md)
- **component** [`navigation/top-app-bar`](00-shared/components/navigation/top-app-bar/IMPLEMENTATION_PROMPT.md)
- **layout** [`auth-centered-card`](00-shared/layouts/auth-centered-card/IMPLEMENTATION_PROMPT.md)
- **layout** [`connector-status`](00-shared/layouts/connector-status/IMPLEMENTATION_PROMPT.md)
- **layout** [`dashboard-metrics`](00-shared/layouts/dashboard-metrics/IMPLEMENTATION_PROMPT.md)
- **layout** [`desktop-sidebar-shell`](00-shared/layouts/desktop-sidebar-shell/IMPLEMENTATION_PROMPT.md)
- **layout** [`detail-action`](00-shared/layouts/detail-action/IMPLEMENTATION_PROMPT.md)
- **layout** [`dual-pane-desktop`](00-shared/layouts/dual-pane-desktop/IMPLEMENTATION_PROMPT.md)
- **layout** [`empty-state-shell`](00-shared/layouts/empty-state-shell/IMPLEMENTATION_PROMPT.md)
- **layout** [`feeder-home`](00-shared/layouts/feeder-home/IMPLEMENTATION_PROMPT.md)
- **layout** [`field-mobile-shell`](00-shared/layouts/field-mobile-shell/IMPLEMENTATION_PROMPT.md)
- **layout** [`field-tablet-shell`](00-shared/layouts/field-tablet-shell/IMPLEMENTATION_PROMPT.md)
- **layout** [`form-capture`](00-shared/layouts/form-capture/IMPLEMENTATION_PROMPT.md)
- **layout** [`insurance-prevention`](00-shared/layouts/insurance-prevention/IMPLEMENTATION_PROMPT.md)
- **layout** [`list-worklist`](00-shared/layouts/list-worklist/IMPLEMENTATION_PROMPT.md)
- **layout** [`map-explorer`](00-shared/layouts/map-explorer/IMPLEMENTATION_PROMPT.md)
- **layout** [`queue-desk`](00-shared/layouts/queue-desk/IMPLEMENTATION_PROMPT.md)
- **layout** [`settings-admin`](00-shared/layouts/settings-admin/IMPLEMENTATION_PROMPT.md)
- **layout** [`upload-batch`](00-shared/layouts/upload-batch/IMPLEMENTATION_PROMPT.md)
- **screen** [`Access denied`](00-shared/access-denied/IMPLEMENTATION_PROMPT.md) · `S-010`
- **screen** [`Consent first`](00-shared/consent-first-onboarding/IMPLEMENTATION_PROMPT.md) · `S-005`
- **screen** [`Create account`](00-shared/create-account/IMPLEMENTATION_PROMPT.md) · `S-002`
- **screen** [`Reset password`](00-shared/forgot-password/IMPLEMENTATION_PROMPT.md) · `S-004`
- **screen** [`Sign in`](00-shared/login/IMPLEMENTATION_PROMPT.md) · `S-003`
- **screen** [`Page not found`](00-shared/not-found/IMPLEMENTATION_PROMPT.md) · `S-011`
- **screen** [`Notifications`](00-shared/notifications-center/IMPLEMENTATION_PROMPT.md) · `S-009`
- **screen** [`Offline PIN`](00-shared/offline-pin-lock/IMPLEMENTATION_PROMPT.md) · `S-006`
- **screen** [`Language & appearance`](00-shared/preferences/IMPLEMENTATION_PROMPT.md) · `S-012`
- **screen** [`Choose your workspace`](00-shared/role-surface-picker/IMPLEMENTATION_PROMPT.md) · `S-008`
- **screen** [`Session locked`](00-shared/session-locked/IMPLEMENTATION_PROMPT.md) · `S-007`
- **screen** [`FCHIP`](00-shared/splash/IMPLEMENTATION_PROMPT.md) · `S-001`

### `01-chw-vht-mobile`

- **screen** [`Act on alert`](01-chw-vht-mobile/alert-follow-up/IMPLEMENTATION_PROMPT.md) · `S-023`
- **screen** [`Alerts inbox`](01-chw-vht-mobile/alerts-inbox/IMPLEMENTATION_PROMPT.md) · `S-022`
- **screen** [`Create referral`](01-chw-vht-mobile/create-referral/IMPLEMENTATION_PROMPT.md) · `S-020`
- **screen** [`Household visit`](01-chw-vht-mobile/household-visit-form/IMPLEMENTATION_PROMPT.md) · `S-016`
- **screen** [`Maternal / child`](01-chw-vht-mobile/maternal-child-indicators/IMPLEMENTATION_PROMPT.md) · `S-018`
- **screen** [`Referral sent`](01-chw-vht-mobile/referral-status/IMPLEMENTATION_PROMPT.md) · `S-021`
- **screen** [`Symptoms & vitals`](01-chw-vht-mobile/symptoms-vitals/IMPLEMENTATION_PROMPT.md) · `S-017`
- **screen** [`Review sync conflict`](01-chw-vht-mobile/sync-conflict/IMPLEMENTATION_PROMPT.md) · `S-026`
- **screen** [`Sync failed`](01-chw-vht-mobile/sync-failed/IMPLEMENTATION_PROMPT.md) · `S-025`
- **screen** [`Sync status`](01-chw-vht-mobile/sync-status/IMPLEMENTATION_PROMPT.md) · `S-024`
- **screen** [`Visit saved`](01-chw-vht-mobile/visit-saved/IMPLEMENTATION_PROMPT.md) · `S-019`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-empty/IMPLEMENTATION_PROMPT.md) · `S-014`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-home/IMPLEMENTATION_PROMPT.md) · `S-013`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-loading/IMPLEMENTATION_PROMPT.md) · `S-015`

### `02-intelligence`

- **screen** [`AI / predictive`](02-intelligence/ai-risk-scores/IMPLEMENTATION_PROMPT.md) · `S-054`
- **screen** [`Alerts & worklists engine`](02-intelligence/alerts-worklists-engine/IMPLEMENTATION_PROMPT.md) · `S-055`
- **screen** [`Climate fusion`](02-intelligence/climate-fusion/IMPLEMENTATION_PROMPT.md) · `S-053`
- **screen** [`Clinical support guidance`](02-intelligence/clinical-support-guidance/IMPLEMENTATION_PROMPT.md) · `S-056`
- **screen** [`Feeder health board`](02-intelligence/feeder-health-board/IMPLEMENTATION_PROMPT.md) · `S-028`
- **screen** [`GIS maps`](02-intelligence/gis-explorer/IMPLEMENTATION_PROMPT.md) · `S-052`
- **screen** [`Ingest & sync`](02-intelligence/ingest-pipeline/IMPLEMENTATION_PROMPT.md) · `S-027`

### `03-cascade-metrics`

- **screen** [`Gap detection`](03-cascade-metrics/gap-detection/IMPLEMENTATION_PROMPT.md) · `S-030`
- **screen** [`Cascade metrics`](03-cascade-metrics/indicators-overview/IMPLEMENTATION_PROMPT.md) · `S-029`
- **screen** [`Partner reports`](03-cascade-metrics/partner-reports/IMPLEMENTATION_PROMPT.md) · `S-031`

### `04-facility-dashboard`

- **screen** [`Catchment map`](04-facility-dashboard/catchment-map/IMPLEMENTATION_PROMPT.md) · `S-033`
- **screen** [`Clinical share confirm`](04-facility-dashboard/clinical-share-confirm/IMPLEMENTATION_PROMPT.md) · `S-037`
- **screen** [`Manual case signal`](04-facility-dashboard/manual-case-signal/IMPLEMENTATION_PROMPT.md) · `S-038`
- **screen** [`Medicine demand forecast`](04-facility-dashboard/medicine-demand-forecast/IMPLEMENTATION_PROMPT.md) · `S-122`
- **screen** [`Referral summary`](04-facility-dashboard/open-referrals/IMPLEMENTATION_PROMPT.md) · `S-034`
- **screen** [`Outreach priorities`](04-facility-dashboard/outreach-priorities/IMPLEMENTATION_PROMPT.md) · `S-036`
- **screen** [`Facility overview`](04-facility-dashboard/overview/IMPLEMENTATION_PROMPT.md) · `S-032`
- **screen** [`Stock signal`](04-facility-dashboard/stock-signal/IMPLEMENTATION_PROMPT.md) · `S-035`

### `05-referrals-desk`

- **screen** [`Outcome feedback`](05-referrals-desk/outcome-feedback/IMPLEMENTATION_PROMPT.md) · `S-042`
- **screen** [`Referral detail`](05-referrals-desk/referral-detail/IMPLEMENTATION_PROMPT.md) · `S-041`
- **screen** [`Referrals desk`](05-referrals-desk/referral-queue/IMPLEMENTATION_PROMPT.md) · `S-039`
- **screen** [`Referrals desk`](05-referrals-desk/referral-queue-empty/IMPLEMENTATION_PROMPT.md) · `S-040`

### `06-emr-connector`

- **screen** [`API scopes setup`](06-emr-connector/api-scopes-setup/IMPLEMENTATION_PROMPT.md) · `S-045`
- **screen** [`EMR / HMS connector`](06-emr-connector/connector-degraded/IMPLEMENTATION_PROMPT.md) · `S-044`
- **screen** [`EMR / HMS connector`](06-emr-connector/connector-status/IMPLEMENTATION_PROMPT.md) · `S-043`
- **screen** [`Facility onboarding`](06-emr-connector/facility-onboarding/IMPLEMENTATION_PROMPT.md) · `S-047`
- **screen** [`Push event log`](06-emr-connector/push-event-log/IMPLEMENTATION_PROMPT.md) · `S-046`

### `07-climate-feeds`

- **screen** [`Climate feeds home`](07-climate-feeds/climate-home/IMPLEMENTATION_PROMPT.md) · `S-048`
- **screen** [`Extremes · flood · heat`](07-climate-feeds/extremes-flood-heat/IMPLEMENTATION_PROMPT.md) · `S-050`
- **screen** [`Feed config & audit`](07-climate-feeds/feed-config-audit/IMPLEMENTATION_PROMPT.md) · `S-051`
- **screen** [`Rainfall & temperature`](07-climate-feeds/rainfall-temperature/IMPLEMENTATION_PROMPT.md) · `S-049`

### `08-district-moh`

- **screen** [`Deploy action`](08-district-moh/action-deploy/IMPLEMENTATION_PROMPT.md) · `S-059`
- **screen** [`Cascade M&E planning`](08-district-moh/cascade-planning/IMPLEMENTATION_PROMPT.md) · `S-060`
- **screen** [`Early warnings`](08-district-moh/early-warnings/IMPLEMENTATION_PROMPT.md) · `S-058`
- **screen** [`MoH national roll-up`](08-district-moh/national-roll-up/IMPLEMENTATION_PROMPT.md) · `S-123`
- **screen** [`Population map`](08-district-moh/population-map/IMPLEMENTATION_PROMPT.md) · `S-057`

### `09-community-caregiver`

- **screen** [`Guidance`](09-community-caregiver/guidance-hints/IMPLEMENTATION_PROMPT.md) · `S-063`
- **screen** [`Household needs`](09-community-caregiver/household-needs-capture/IMPLEMENTATION_PROMPT.md) · `S-064`
- **screen** [`My household`](09-community-caregiver/my-household/IMPLEMENTATION_PROMPT.md) · `S-061`
- **screen** [`Self-report`](09-community-caregiver/self-report/IMPLEMENTATION_PROMPT.md) · `S-062`

### `10-outreach-school-health`

- **screen** [`Campaign planner`](10-outreach-school-health/campaign-planner/IMPLEMENTATION_PROMPT.md) · `S-065`
- **screen** [`Coverage map`](10-outreach-school-health/coverage-map/IMPLEMENTATION_PROMPT.md) · `S-067`
- **screen** [`Home-visit batch`](10-outreach-school-health/home-visit-batch-upload/IMPLEMENTATION_PROMPT.md) · `S-069`
- **screen** [`Screening results entry`](10-outreach-school-health/screening-results-entry/IMPLEMENTATION_PROMPT.md) · `S-068`
- **screen** [`Session log`](10-outreach-school-health/session-log/IMPLEMENTATION_PROMPT.md) · `S-066`

### `11-admin-consent`

- **screen** [`Consent & privacy`](11-admin-consent/consent-privacy/IMPLEMENTATION_PROMPT.md) · `S-072`
- **screen** [`EMR API access`](11-admin-consent/emr-api-access/IMPLEMENTATION_PROMPT.md) · `S-073`
- **screen** [`Feeder party registry`](11-admin-consent/feeder-party-registry/IMPLEMENTATION_PROMPT.md) · `S-074`
- **screen** [`Org · catchment · facilities`](11-admin-consent/org-catchment/IMPLEMENTATION_PROMPT.md) · `S-070`
- **screen** [`Users & roles`](11-admin-consent/users-roles/IMPLEMENTATION_PROMPT.md) · `S-071`

### `12-insurance-insights`

- **screen** [`Anonymised trends`](12-insurance-insights/anonymised-trends/IMPLEMENTATION_PROMPT.md) · `S-077`
- **screen** [`Prevention overview`](12-insurance-insights/prevention-overview/IMPLEMENTATION_PROMPT.md) · `S-075`
- **screen** [`Risk cohort insights`](12-insurance-insights/risk-cohort-insights/IMPLEMENTATION_PROMPT.md) · `S-076`

### `13-chis-livelihoods`

- **screen** [`Claims / access`](13-chis-livelihoods/claims-access/IMPLEMENTATION_PROMPT.md) · `S-080`
- **screen** [`Contributions`](13-chis-livelihoods/contributions/IMPLEMENTATION_PROMPT.md) · `S-079`
- **screen** [`CHIS enrolment`](13-chis-livelihoods/enrolment/IMPLEMENTATION_PROMPT.md) · `S-078`
- **screen** [`IGA participation entry`](13-chis-livelihoods/iga-participation-entry/IMPLEMENTATION_PROMPT.md) · `S-081`

### `14-ngo-partner`

- **screen** [`Field dataset upload`](14-ngo-partner/field-dataset-upload/IMPLEMENTATION_PROMPT.md) · `S-085`
- **screen** [`Impact evidence`](14-ngo-partner/impact-evidence/IMPLEMENTATION_PROMPT.md) · `S-083`
- **screen** [`Partner indicator entry`](14-ngo-partner/partner-indicator-entry/IMPLEMENTATION_PROMPT.md) · `S-086`
- **screen** [`Programme monitoring`](14-ngo-partner/programme-monitoring/IMPLEMENTATION_PROMPT.md) · `S-082`
- **screen** [`Training · skills analytics`](14-ngo-partner/training-skills-analytics/IMPLEMENTATION_PROMPT.md) · `S-084`

### `15-schools-health`

- **screen** [`Absenteeism & wellness`](15-schools-health/absenteeism-wellness/IMPLEMENTATION_PROMPT.md) · `S-090`
- **screen** [`Health education session`](15-schools-health/health-education-session/IMPLEMENTATION_PROMPT.md) · `S-088`
- **screen** [`Learner screening entry`](15-schools-health/learner-screening-entry/IMPLEMENTATION_PROMPT.md) · `S-089`
- **screen** [`School health home`](15-schools-health/school-home/IMPLEMENTATION_PROMPT.md) · `S-087`
- **screen** [`School sync status`](15-schools-health/school-sync-status/IMPLEMENTATION_PROMPT.md) · `S-091`

### `16-pharmacy-outlets`

- **screen** [`Common complaints`](16-pharmacy-outlets/common-complaints/IMPLEMENTATION_PROMPT.md) · `S-095`
- **screen** [`Dispense log`](16-pharmacy-outlets/dispense-log/IMPLEMENTATION_PROMPT.md) · `S-094`
- **screen** [`Pharmacy outlet home`](16-pharmacy-outlets/pharmacy-home/IMPLEMENTATION_PROMPT.md) · `S-092`
- **screen** [`Pre-stock acknowledgement`](16-pharmacy-outlets/prestock-ack/IMPLEMENTATION_PROMPT.md) · `S-096`
- **screen** [`Stock levels entry`](16-pharmacy-outlets/stock-levels-entry/IMPLEMENTATION_PROMPT.md) · `S-093`

### `17-labs-poc`

- **screen** [`Batch results upload`](17-labs-poc/batch-results-upload/IMPLEMENTATION_PROMPT.md) · `S-099`
- **screen** [`Lab / PoC home`](17-labs-poc/lab-home/IMPLEMENTATION_PROMPT.md) · `S-097`
- **screen** [`Result entry`](17-labs-poc/result-entry/IMPLEMENTATION_PROMPT.md) · `S-098`
- **screen** [`Result queue`](17-labs-poc/result-queue/IMPLEMENTATION_PROMPT.md) · `S-100`

### `18-corporate-wellness`

- **screen** [`Camp summary push`](18-corporate-wellness/camp-summary-push/IMPLEMENTATION_PROMPT.md) · `S-103`
- **screen** [`Camp vitals entry`](18-corporate-wellness/camp-vitals-entry/IMPLEMENTATION_PROMPT.md) · `S-102`
- **screen** [`Corporate wellness home`](18-corporate-wellness/corporate-home/IMPLEMENTATION_PROMPT.md) · `S-101`
- **screen** [`Occupational flags`](18-corporate-wellness/occupational-flags/IMPLEMENTATION_PROMPT.md) · `S-104`

### `19-mch-touchpoints`

- **screen** [`ANC visit entry`](19-mch-touchpoints/anc-visit-entry/IMPLEMENTATION_PROMPT.md) · `S-106`
- **screen** [`Immunisation entry`](19-mch-touchpoints/immunisation-entry/IMPLEMENTATION_PROMPT.md) · `S-108`
- **screen** [`MCH touchpoints home`](19-mch-touchpoints/mch-home/IMPLEMENTATION_PROMPT.md) · `S-105`
- **screen** [`Nutrition monitoring`](19-mch-touchpoints/nutrition-monitoring/IMPLEMENTATION_PROMPT.md) · `S-109`
- **screen** [`PNC visit entry`](19-mch-touchpoints/pnc-visit-entry/IMPLEMENTATION_PROMPT.md) · `S-107`

### `20-ncd-gericare`

- **screen** [`BP screening batch`](20-ncd-gericare/bp-screening-batch/IMPLEMENTATION_PROMPT.md) · `S-112`
- **screen** [`NCD / Gericare home`](20-ncd-gericare/cohort-home/IMPLEMENTATION_PROMPT.md) · `S-110`
- **screen** [`Cohort visit entry`](20-ncd-gericare/cohort-visit-entry/IMPLEMENTATION_PROMPT.md) · `S-111`
- **screen** [`Stroke / NCD risk flags`](20-ncd-gericare/stroke-risk-flags/IMPLEMENTATION_PROMPT.md) · `S-113`

### `21-hmis-dhis2`

- **screen** [`Aggregate push / pull`](21-hmis-dhis2/aggregate-push-pull/IMPLEMENTATION_PROMPT.md) · `S-116`
- **screen** [`Dataset mapping`](21-hmis-dhis2/dataset-mapping/IMPLEMENTATION_PROMPT.md) · `S-115`
- **screen** [`HMIS audit`](21-hmis-dhis2/hmis-audit/IMPLEMENTATION_PROMPT.md) · `S-117`
- **screen** [`HMIS / DHIS2 home`](21-hmis-dhis2/hmis-home/IMPLEMENTATION_PROMPT.md) · `S-114`

### `22-community-events`

- **screen** [`Community dialogue`](22-community-events/community-dialogue/IMPLEMENTATION_PROMPT.md) · `S-120`
- **screen** [`Community events home`](22-community-events/events-home/IMPLEMENTATION_PROMPT.md) · `S-118`
- **screen** [`Outreach event log`](22-community-events/outreach-event-log/IMPLEMENTATION_PROMPT.md) · `S-119`
- **screen** [`Participation register`](22-community-events/participation-register/IMPLEMENTATION_PROMPT.md) · `S-121`

### `23-research-exports`

- **screen** [`Evidence catalog`](23-research-exports/evidence-catalog/IMPLEMENTATION_PROMPT.md) · `S-124`
- **screen** [`Export under review`](23-research-exports/export-pending/IMPLEMENTATION_PROMPT.md) · `S-127`
- **screen** [`Export request`](23-research-exports/export-request/IMPLEMENTATION_PROMPT.md) · `S-125`
- **screen** [`Research contribution upload`](23-research-exports/research-contribution-upload/IMPLEMENTATION_PROMPT.md) · `S-126`

## Rules referenced across prompts

Root: `.cursor/mandatories.mdc`, `.cursor/app-write-up.mdc`

Frontend: `frontend/.cursor/index.mdc`, `product_delivery.mdc`, `feature_workflow.mdc`, `project_structure.mdc`, `components.mdc`, `layouts.mdc`, `ui-workspace.mdc`, `permissions.mdc`, `network_api.mdc`, `testing.mdc`, and related owners listed in each prompt.

Backend: `backend/.cursor/vertical-slice-delivery.mdc`, `module-creation.mdc`, `api.mdc`, `prisma.mdc`, `auth-security.mdc`, plus `backend/dev-plan/P016_slice_pairing.md`.

Plan: `frontend/dev-plan/00-execution-policy.md`, `25-slice-execution-playbook.md`, `slices/chronology.yaml`.
