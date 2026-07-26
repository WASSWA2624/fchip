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
- **screen** [`Access denied`](00-shared/access-denied/implementation_prompt.md) · `S-010`
- **screen** [`Consent first`](00-shared/consent-first-onboarding/implementation_prompt.md) · `S-005`
- **screen** [`Create account`](00-shared/create-account/implementation_prompt.md) · `S-002`
- **screen** [`Reset password`](00-shared/forgot-password/implementation_prompt.md) · `S-004`
- **screen** [`Sign in`](00-shared/login/implementation_prompt.md) · `S-003`
- **screen** [`Page not found`](00-shared/not-found/implementation_prompt.md) · `S-011`
- **screen** [`Notifications`](00-shared/notifications-center/implementation_prompt.md) · `S-009`
- **screen** [`Offline PIN`](00-shared/offline-pin-lock/implementation_prompt.md) · `S-006`
- **screen** [`Language & appearance`](00-shared/preferences/implementation_prompt.md) · `S-012`
- **screen** [`Choose your workspace`](00-shared/role-surface-picker/implementation_prompt.md) · `S-008`
- **screen** [`Session locked`](00-shared/session-locked/implementation_prompt.md) · `S-007`
- **screen** [`FCHIP`](00-shared/splash/implementation_prompt.md) · `S-001`

### `01-chw-vht-mobile`

- **screen** [`Act on alert`](01-chw-vht-mobile/alert-follow-up/implementation_prompt.md) · `S-023`
- **screen** [`Alerts inbox`](01-chw-vht-mobile/alerts-inbox/implementation_prompt.md) · `S-022`
- **screen** [`Create referral`](01-chw-vht-mobile/create-referral/implementation_prompt.md) · `S-020`
- **screen** [`Household visit`](01-chw-vht-mobile/household-visit-form/implementation_prompt.md) · `S-016`
- **screen** [`Maternal / child`](01-chw-vht-mobile/maternal-child-indicators/implementation_prompt.md) · `S-018`
- **screen** [`Referral sent`](01-chw-vht-mobile/referral-status/implementation_prompt.md) · `S-021`
- **screen** [`Symptoms & vitals`](01-chw-vht-mobile/symptoms-vitals/implementation_prompt.md) · `S-017`
- **screen** [`Review sync conflict`](01-chw-vht-mobile/sync-conflict/implementation_prompt.md) · `S-026`
- **screen** [`Sync failed`](01-chw-vht-mobile/sync-failed/implementation_prompt.md) · `S-025`
- **screen** [`Sync status`](01-chw-vht-mobile/sync-status/implementation_prompt.md) · `S-024`
- **screen** [`Visit saved`](01-chw-vht-mobile/visit-saved/implementation_prompt.md) · `S-019`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-empty/implementation_prompt.md) · `S-014`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-home/implementation_prompt.md) · `S-013`
- **screen** [`Today’s worklist`](01-chw-vht-mobile/worklist-loading/implementation_prompt.md) · `S-015`

### `02-intelligence`

- **screen** [`AI / predictive`](02-intelligence/ai-risk-scores/implementation_prompt.md) · `S-054`
- **screen** [`Alerts & worklists engine`](02-intelligence/alerts-worklists-engine/implementation_prompt.md) · `S-055`
- **screen** [`Climate fusion`](02-intelligence/climate-fusion/implementation_prompt.md) · `S-053`
- **screen** [`Clinical support guidance`](02-intelligence/clinical-support-guidance/implementation_prompt.md) · `S-056`
- **screen** [`Feeder health board`](02-intelligence/feeder-health-board/implementation_prompt.md) · `S-028`
- **screen** [`GIS maps`](02-intelligence/gis-explorer/implementation_prompt.md) · `S-052`
- **screen** [`Ingest & sync`](02-intelligence/ingest-pipeline/implementation_prompt.md) · `S-027`

### `03-cascade-metrics`

- **screen** [`Gap detection`](03-cascade-metrics/gap-detection/implementation_prompt.md) · `S-030`
- **screen** [`Cascade metrics`](03-cascade-metrics/indicators-overview/implementation_prompt.md) · `S-029`
- **screen** [`Partner reports`](03-cascade-metrics/partner-reports/implementation_prompt.md) · `S-031`

### `04-facility-dashboard`

- **screen** [`Catchment map`](04-facility-dashboard/catchment-map/implementation_prompt.md) · `S-033`
- **screen** [`Clinical share confirm`](04-facility-dashboard/clinical-share-confirm/implementation_prompt.md) · `S-037`
- **screen** [`Manual case signal`](04-facility-dashboard/manual-case-signal/implementation_prompt.md) · `S-038`
- **screen** [`Medicine demand forecast`](04-facility-dashboard/medicine-demand-forecast/implementation_prompt.md) · `S-122`
- **screen** [`Referral summary`](04-facility-dashboard/open-referrals/implementation_prompt.md) · `S-034`
- **screen** [`Outreach priorities`](04-facility-dashboard/outreach-priorities/implementation_prompt.md) · `S-036`
- **screen** [`Facility overview`](04-facility-dashboard/overview/implementation_prompt.md) · `S-032`
- **screen** [`Stock signal`](04-facility-dashboard/stock-signal/implementation_prompt.md) · `S-035`

### `05-referrals-desk`

- **screen** [`Outcome feedback`](05-referrals-desk/outcome-feedback/implementation_prompt.md) · `S-042`
- **screen** [`Referral detail`](05-referrals-desk/referral-detail/implementation_prompt.md) · `S-041`
- **screen** [`Referrals desk`](05-referrals-desk/referral-queue/implementation_prompt.md) · `S-039`
- **screen** [`Referrals desk`](05-referrals-desk/referral-queue-empty/implementation_prompt.md) · `S-040`

### `06-emr-connector`

- **screen** [`API scopes setup`](06-emr-connector/api-scopes-setup/implementation_prompt.md) · `S-045`
- **screen** [`EMR / HMS connector`](06-emr-connector/connector-degraded/implementation_prompt.md) · `S-044`
- **screen** [`EMR / HMS connector`](06-emr-connector/connector-status/implementation_prompt.md) · `S-043`
- **screen** [`Facility onboarding`](06-emr-connector/facility-onboarding/implementation_prompt.md) · `S-047`
- **screen** [`Push event log`](06-emr-connector/push-event-log/implementation_prompt.md) · `S-046`

### `07-climate-feeds`

- **screen** [`Climate feeds home`](07-climate-feeds/climate-home/implementation_prompt.md) · `S-048`
- **screen** [`Extremes · flood · heat`](07-climate-feeds/extremes-flood-heat/implementation_prompt.md) · `S-050`
- **screen** [`Feed config & audit`](07-climate-feeds/feed-config-audit/implementation_prompt.md) · `S-051`
- **screen** [`Rainfall & temperature`](07-climate-feeds/rainfall-temperature/implementation_prompt.md) · `S-049`

### `08-district-moh`

- **screen** [`Deploy action`](08-district-moh/action-deploy/implementation_prompt.md) · `S-059`
- **screen** [`Cascade M&E planning`](08-district-moh/cascade-planning/implementation_prompt.md) · `S-060`
- **screen** [`Early warnings`](08-district-moh/early-warnings/implementation_prompt.md) · `S-058`
- **screen** [`MoH national roll-up`](08-district-moh/national-roll-up/implementation_prompt.md) · `S-123`
- **screen** [`Population map`](08-district-moh/population-map/implementation_prompt.md) · `S-057`

### `09-community-caregiver`

- **screen** [`Guidance`](09-community-caregiver/guidance-hints/implementation_prompt.md) · `S-063`
- **screen** [`Household needs`](09-community-caregiver/household-needs-capture/implementation_prompt.md) · `S-064`
- **screen** [`My household`](09-community-caregiver/my-household/implementation_prompt.md) · `S-061`
- **screen** [`Self-report`](09-community-caregiver/self-report/implementation_prompt.md) · `S-062`

### `10-outreach-school-health`

- **screen** [`Campaign planner`](10-outreach-school-health/campaign-planner/implementation_prompt.md) · `S-065`
- **screen** [`Coverage map`](10-outreach-school-health/coverage-map/implementation_prompt.md) · `S-067`
- **screen** [`Home-visit batch`](10-outreach-school-health/home-visit-batch-upload/implementation_prompt.md) · `S-069`
- **screen** [`Screening results entry`](10-outreach-school-health/screening-results-entry/implementation_prompt.md) · `S-068`
- **screen** [`Session log`](10-outreach-school-health/session-log/implementation_prompt.md) · `S-066`

### `11-admin-consent`

- **screen** [`Consent & privacy`](11-admin-consent/consent-privacy/implementation_prompt.md) · `S-072`
- **screen** [`EMR API access`](11-admin-consent/emr-api-access/implementation_prompt.md) · `S-073`
- **screen** [`Feeder party registry`](11-admin-consent/feeder-party-registry/implementation_prompt.md) · `S-074`
- **screen** [`Org · catchment · facilities`](11-admin-consent/org-catchment/implementation_prompt.md) · `S-070`
- **screen** [`Users & roles`](11-admin-consent/users-roles/implementation_prompt.md) · `S-071`

### `12-insurance-insights`

- **screen** [`Anonymised trends`](12-insurance-insights/anonymised-trends/implementation_prompt.md) · `S-077`
- **screen** [`Prevention overview`](12-insurance-insights/prevention-overview/implementation_prompt.md) · `S-075`
- **screen** [`Risk cohort insights`](12-insurance-insights/risk-cohort-insights/implementation_prompt.md) · `S-076`

### `13-chis-livelihoods`

- **screen** [`Claims / access`](13-chis-livelihoods/claims-access/implementation_prompt.md) · `S-080`
- **screen** [`Contributions`](13-chis-livelihoods/contributions/implementation_prompt.md) · `S-079`
- **screen** [`CHIS enrolment`](13-chis-livelihoods/enrolment/implementation_prompt.md) · `S-078`
- **screen** [`IGA participation entry`](13-chis-livelihoods/iga-participation-entry/implementation_prompt.md) · `S-081`

### `14-ngo-partner`

- **screen** [`Field dataset upload`](14-ngo-partner/field-dataset-upload/implementation_prompt.md) · `S-085`
- **screen** [`Impact evidence`](14-ngo-partner/impact-evidence/implementation_prompt.md) · `S-083`
- **screen** [`Partner indicator entry`](14-ngo-partner/partner-indicator-entry/implementation_prompt.md) · `S-086`
- **screen** [`Programme monitoring`](14-ngo-partner/programme-monitoring/implementation_prompt.md) · `S-082`
- **screen** [`Training · skills analytics`](14-ngo-partner/training-skills-analytics/implementation_prompt.md) · `S-084`

### `15-schools-health`

- **screen** [`Absenteeism & wellness`](15-schools-health/absenteeism-wellness/implementation_prompt.md) · `S-090`
- **screen** [`Health education session`](15-schools-health/health-education-session/implementation_prompt.md) · `S-088`
- **screen** [`Learner screening entry`](15-schools-health/learner-screening-entry/implementation_prompt.md) · `S-089`
- **screen** [`School health home`](15-schools-health/school-home/implementation_prompt.md) · `S-087`
- **screen** [`School sync status`](15-schools-health/school-sync-status/implementation_prompt.md) · `S-091`

### `16-pharmacy-outlets`

- **screen** [`Common complaints`](16-pharmacy-outlets/common-complaints/implementation_prompt.md) · `S-095`
- **screen** [`Dispense log`](16-pharmacy-outlets/dispense-log/implementation_prompt.md) · `S-094`
- **screen** [`Pharmacy outlet home`](16-pharmacy-outlets/pharmacy-home/implementation_prompt.md) · `S-092`
- **screen** [`Pre-stock acknowledgement`](16-pharmacy-outlets/prestock-ack/implementation_prompt.md) · `S-096`
- **screen** [`Stock levels entry`](16-pharmacy-outlets/stock-levels-entry/implementation_prompt.md) · `S-093`

### `17-labs-poc`

- **screen** [`Batch results upload`](17-labs-poc/batch-results-upload/implementation_prompt.md) · `S-099`
- **screen** [`Lab / PoC home`](17-labs-poc/lab-home/implementation_prompt.md) · `S-097`
- **screen** [`Result entry`](17-labs-poc/result-entry/implementation_prompt.md) · `S-098`
- **screen** [`Result queue`](17-labs-poc/result-queue/implementation_prompt.md) · `S-100`

### `18-corporate-wellness`

- **screen** [`Camp summary push`](18-corporate-wellness/camp-summary-push/implementation_prompt.md) · `S-103`
- **screen** [`Camp vitals entry`](18-corporate-wellness/camp-vitals-entry/implementation_prompt.md) · `S-102`
- **screen** [`Corporate wellness home`](18-corporate-wellness/corporate-home/implementation_prompt.md) · `S-101`
- **screen** [`Occupational flags`](18-corporate-wellness/occupational-flags/implementation_prompt.md) · `S-104`

### `19-mch-touchpoints`

- **screen** [`ANC visit entry`](19-mch-touchpoints/anc-visit-entry/implementation_prompt.md) · `S-106`
- **screen** [`Immunisation entry`](19-mch-touchpoints/immunisation-entry/implementation_prompt.md) · `S-108`
- **screen** [`MCH touchpoints home`](19-mch-touchpoints/mch-home/implementation_prompt.md) · `S-105`
- **screen** [`Nutrition monitoring`](19-mch-touchpoints/nutrition-monitoring/implementation_prompt.md) · `S-109`
- **screen** [`PNC visit entry`](19-mch-touchpoints/pnc-visit-entry/implementation_prompt.md) · `S-107`

### `20-ncd-gericare`

- **screen** [`BP screening batch`](20-ncd-gericare/bp-screening-batch/implementation_prompt.md) · `S-112`
- **screen** [`NCD / Gericare home`](20-ncd-gericare/cohort-home/implementation_prompt.md) · `S-110`
- **screen** [`Cohort visit entry`](20-ncd-gericare/cohort-visit-entry/implementation_prompt.md) · `S-111`
- **screen** [`Stroke / NCD risk flags`](20-ncd-gericare/stroke-risk-flags/implementation_prompt.md) · `S-113`

### `21-hmis-dhis2`

- **screen** [`Aggregate push / pull`](21-hmis-dhis2/aggregate-push-pull/implementation_prompt.md) · `S-116`
- **screen** [`Dataset mapping`](21-hmis-dhis2/dataset-mapping/implementation_prompt.md) · `S-115`
- **screen** [`HMIS audit`](21-hmis-dhis2/hmis-audit/implementation_prompt.md) · `S-117`
- **screen** [`HMIS / DHIS2 home`](21-hmis-dhis2/hmis-home/implementation_prompt.md) · `S-114`

### `22-community-events`

- **screen** [`Community dialogue`](22-community-events/community-dialogue/implementation_prompt.md) · `S-120`
- **screen** [`Community events home`](22-community-events/events-home/implementation_prompt.md) · `S-118`
- **screen** [`Outreach event log`](22-community-events/outreach-event-log/implementation_prompt.md) · `S-119`
- **screen** [`Participation register`](22-community-events/participation-register/implementation_prompt.md) · `S-121`

### `23-research-exports`

- **screen** [`Evidence catalog`](23-research-exports/evidence-catalog/implementation_prompt.md) · `S-124`
- **screen** [`Export under review`](23-research-exports/export-pending/implementation_prompt.md) · `S-127`
- **screen** [`Export request`](23-research-exports/export-request/implementation_prompt.md) · `S-125`
- **screen** [`Research contribution upload`](23-research-exports/research-contribution-upload/implementation_prompt.md) · `S-126`

## Rules referenced across prompts

Root: `.cursor/mandatories.mdc`, `.cursor/app-write-up.mdc`

Frontend: `frontend/.cursor/index.mdc`, `product_delivery.mdc`, `feature_workflow.mdc`, `project_structure.mdc`, `components.mdc`, `layouts.mdc`, `ui-workspace.mdc`, `permissions.mdc`, `network_api.mdc`, `testing.mdc`, and related owners listed in each prompt.

Backend: `backend/.cursor/vertical-slice-delivery.mdc`, `module-creation.mdc`, `api.mdc`, `prisma.mdc`, `auth-security.mdc`, plus `backend/dev-plan/P016_slice_pairing.md`.

Plan: `frontend/dev-plan/00-execution-policy.md`, `25-slice-execution-playbook.md`, `slices/chronology.yaml`.
