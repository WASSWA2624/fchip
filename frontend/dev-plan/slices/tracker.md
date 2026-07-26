# Slice tracker

Live status of FCHIP product delivery. Every slice listed here must pair a frontend screen with the backend that serves it, per [`.cursor/mandatories.mdc`](../../../.cursor/mandatories.mdc).

Order comes from [`24-product-vertical-slices.md`](../24-product-vertical-slices.md). The loop for a single screen is [`25-slice-execution-playbook.md`](../25-slice-execution-playbook.md). Add per-screen records using [`TEMPLATE.md`](./TEMPLATE.md).

## How to use this file

1. Only **one** product slice may be `in-progress` at a time.
2. When you start a slice, add its per-screen records from `TEMPLATE.md` under [Slice records](#slice-records).
3. Update the status column as the slice moves; never mark `done` without cross-stack proof.
4. Run `python tool/check_slice_coverage.py` before closing a slice.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| `not-started` | No FCHIP frontend or backend work exists for this module |
| `in-progress` | Screens are being delivered; see per-screen records |
| `blocked` | Waiting on a decision, dependency, or SoT clarification |
| `done` | Every screen wired to real backend with cross-stack proof |

Legacy HIS workspaces in `frontend/lib/features/` and `backend/src/modules/` do **not** count as FCHIP delivery. Reuse their primitives, but a slice stays `not-started` until its `app-ui` screens exist as FCHIP routes.

## Delivery status

| Wave | Slice | Module | Screens | Status | Backend paired |
| --- | --- | --- | --- | --- | --- |
| 0 | VS-00 | `00-shared` | 12 | not-started | 0/12 |
| 1 | VS-01 | `01-chw-vht-mobile` | 14 | not-started | 0/14 |
| 1 | VS-04 | `04-cascade-metrics` | 3 | not-started | 0/3 |
| 1 | VS-06 | `06-facility-dashboard` | 8 | not-started | 0/8 |
| 1 | VS-07 | `07-referrals-desk` | 4 | not-started | 0/4 |
| 1 | VS-08 | `08-emr-connector` | 5 | not-started | 0/5 |
| 1 | VS-09 | `09-intelligence` | 7 | not-started | 0/7 |
| 1 | VS-10 | `10-district-moh` | 5 | not-started | 0/5 |
| 1 | VS-22 | `22-climate-feeds` | 4 | not-started | 0/4 |
| 2 | VS-02 | `02-community-caregiver` | 4 | not-started | 0/4 |
| 2 | VS-03 | `03-outreach-school-health` | 5 | not-started | 0/5 |
| 2 | VS-13 | `13-admin-consent` | 5 | not-started | 0/5 |
| 2 | VS-23 | `23-insurance-insights` | 3 | not-started | 0/3 |
| 3 | VS-05 | `05-chis-livelihoods` | 4 | not-started | 0/4 |
| 3 | VS-11 | `11-ngo-partner` | 5 | not-started | 0/5 |
| 3 | VS-14 | `14-schools-health` | 5 | not-started | 0/5 |
| 3 | VS-15 | `15-pharmacy-outlets` | 5 | not-started | 0/5 |
| 3 | VS-16 | `16-labs-poc` | 4 | not-started | 0/4 |
| 3 | VS-17 | `17-corporate-wellness` | 4 | not-started | 0/4 |
| 3 | VS-18 | `18-mch-touchpoints` | 5 | not-started | 0/5 |
| 3 | VS-19 | `19-ncd-gericare` | 4 | not-started | 0/4 |
| 3 | VS-20 | `20-hmis-dhis2` | 4 | not-started | 0/4 |
| 3 | VS-21 | `21-community-events` | 4 | not-started | 0/4 |
| 4 | VS-12 | `12-research-exports` | 4 | not-started | 0/4 |

**Total:** 0 of 127 screens delivered.

Wave 4 also covers two deferred screens inside earlier slices: `06-facility-dashboard/medicine-demand-forecast` (phase 3) and `10-district-moh/national-roll-up` (phase 3). Keep them feature-gated and do not report them as implemented while deferred.

## Journey proofs

Both MVP journeys must pass end to end before delivery moves past Wave 1.

| Journey | Slices involved | Proof |
| --- | --- | --- |
| CHW visit → sync → referral → facility queue/detail → outcome → CHW status → cascade metric | VS-00, VS-01, VS-07, VS-04 | pending |
| Fever signal → ingest → climate/GIS/risk → district warning → deployed response → result → metric | VS-01, VS-09, VS-22, VS-10 | pending |

## Slice records

No slice records yet. Copy blocks from [`TEMPLATE.md`](./TEMPLATE.md) as slices open.
