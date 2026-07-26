# P011 Backend Modules
Implement one backend capability at a time behind the active frontend screen or journey.

## Delivery Source

Module order is owned by `frontend/dev-plan/24-product-vertical-slices.md`:

1. shared entry, identity, consent, access, notifications, and preferences;
2. CHW offline capture and referral loop;
3. ingest, cascade metrics, facility/referrals, EMR connector, climate/GIS/risk/alerts, and district action;
4. remaining MVP caregiver, outreach, administration, and anonymised insurance surfaces;
5. phase-2 feeders and partner modules;
6. phase-3 forecast/national roll-up and phase-4 approved research exports.

## Module Gate

- Each active slice must follow `backend/.cursor/vertical-slice-delivery.mdc` and `backend/.cursor/module-creation.mdc`.
- Workflows must remain inside their subscription and assigned-module boundaries while sharing the canonical ingest, metrics, alert, identity, and audit spines.
- Permission keys, route families, entitlements, and models must stay aligned with documentation.
- Frontend, tests, documentation, migration, and seed changes must be completed together.
- A later screen must not begin while the active screen has an undocumented backend gap.
- FCHIP integrates with external EMR/HMS; it must not grow generic inpatient, theatre, payroll, mortuary, or other unrelated HIS modules.
