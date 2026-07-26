# Slice tracker

Live status of FCHIP product delivery. Every screen listed here must pair Flutter UI with the backend that serves it, per [`.cursor/mandatories.mdc`](../../../.cursor/mandatories.mdc).

**Build order:** [`chronology.yaml`](./chronology.yaml) (`S-001` … `S-127`).  
**Loop:** [`25-slice-execution-playbook.md`](../25-slice-execution-playbook.md).  
**Module ownership:** [`registry.yaml`](./registry.yaml).  
**Per-screen record:** [`TEMPLATE.md`](./TEMPLATE.md).

## How to use this file

1. Only **one** chronology screen may be active at a time.
2. When you start a screen, copy a block from `TEMPLATE.md` under [Screen records](#screen-records) and set its chronology `status`.
3. Never mark a screen `done` without cross-stack proof (or proven `backend: none`).
4. Run `python tool/check_slice_coverage.py` before closing a screen.

## Status vocabulary

| Chronology `status` | Meaning |
| --- | --- |
| `not-started` | No FCHIP work for this screen |
| `ui-fixtures` | Flutter UI exists on fixtures |
| `contract-defined` | Typed repository/API contract written |
| `backend-in-progress` | Matching backend being built |
| `wired` | Real repository connected |
| `done` | Cross-stack proof recorded |

| Slice status | Meaning |
| --- | --- |
| `not-started` | No FCHIP screens delivered in the module |
| `in-progress` | At least one screen active or done |
| `blocked` | Waiting on a decision or dependency |
| `done` | Every owned screen (including deferred when unlocked) is done |

Legacy HIS workspaces do **not** count as FCHIP delivery.

## Next screen

| Field | Value |
| --- | --- |
| Next `seq` | `S-001` |
| Screen | `00-shared/01-splash` |
| Slice | `VS-00` |
| Active now | _(none)_ |

Update this table whenever a screen opens or closes.

## Module status

| Wave | Slice | Module | Screens | Status | Backend paired |
| --- | --- | --- | --- | --- | --- |
| 0 | VS-00 | `00-shared` | 12 | not-started | 0/12 |
| 1 | VS-01 | `01-chw-vht-mobile` | 14 | not-started | 0/14 |
| 1 | VS-02 | `02-intelligence` | 7 | not-started | 0/7 |
| 1 | VS-03 | `03-cascade-metrics` | 3 | not-started | 0/3 |
| 1 | VS-04 | `04-facility-dashboard` | 8 | not-started | 0/8 |
| 1 | VS-05 | `05-referrals-desk` | 4 | not-started | 0/4 |
| 1 | VS-06 | `06-emr-connector` | 5 | not-started | 0/5 |
| 1 | VS-07 | `07-climate-feeds` | 4 | not-started | 0/4 |
| 1 | VS-08 | `08-district-moh` | 5 | not-started | 0/5 |
| 2 | VS-09 | `09-community-caregiver` | 4 | not-started | 0/4 |
| 2 | VS-10 | `10-outreach-school-health` | 5 | not-started | 0/5 |
| 2 | VS-11 | `11-admin-consent` | 5 | not-started | 0/5 |
| 2 | VS-12 | `12-insurance-insights` | 3 | not-started | 0/3 |
| 3 | VS-13 | `13-chis-livelihoods` | 4 | not-started | 0/4 |
| 3 | VS-14 | `14-ngo-partner` | 5 | not-started | 0/5 |
| 3 | VS-15 | `15-schools-health` | 5 | not-started | 0/5 |
| 3 | VS-16 | `16-pharmacy-outlets` | 5 | not-started | 0/5 |
| 3 | VS-17 | `17-labs-poc` | 4 | not-started | 0/4 |
| 3 | VS-18 | `18-corporate-wellness` | 4 | not-started | 0/4 |
| 3 | VS-19 | `19-mch-touchpoints` | 5 | not-started | 0/5 |
| 3 | VS-20 | `20-ncd-gericare` | 4 | not-started | 0/4 |
| 3 | VS-21 | `21-hmis-dhis2` | 4 | not-started | 0/4 |
| 3 | VS-22 | `22-community-events` | 4 | not-started | 0/4 |
| 4 | VS-23 | `23-research-exports` | 4 | not-started | 0/4 |

**Total:** 0 of 127 screens delivered.

Wave 4 also covers deferred screens inside earlier slices: `04-facility-dashboard/08-medicine-demand-forecast` (`S-122`) and `08-district-moh/05-national-roll-up` (`S-123`). Keep them feature-gated until unlocked.

## Journey proofs

Both MVP journeys must pass end to end before delivery moves past Wave 1.

| Journey | Screens involved | Proof |
| --- | --- | --- |
| CHW visit → sync → referral → facility queue/detail → outcome → CHW status → cascade metric | `S-013`–`S-042`, cascade metrics | pending |
| Fever signal → ingest → climate/GIS/risk → district warning → deployed response → result → metric | `S-027`–`S-060` (intelligence, climate, district) | pending |

## Screen records

No screen records yet. Copy blocks from [`TEMPLATE.md`](./TEMPLATE.md) as screens open. Prefix each heading with the chronology `seq` (for example `### S-001 · VS-00 · 00-shared/01-splash`).
