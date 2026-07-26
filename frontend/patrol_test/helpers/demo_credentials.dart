/// Seeded demo accounts for Patrol E2E against a running backend.
///
/// Source of truth: `backend/scripts/seeders/seed-catalog.js`
const String demoAccountPassword = 'Fchip@2624.';

enum DemoAccount {
  superAdmin('super.admin@fchip.com'),
  tenantAdmin('tenant.admin@fchip.com'),
  facilityAdmin('facility.admin@fchip.com'),
  doctor('doctor@fchip.com'),
  nurse('nurse@fchip.com'),
  lab('lab@fchip.com'),
  radiology('radiology@fchip.com'),
  pharmacy('pharmacy@fchip.com'),
  reception('reception@fchip.com'),
  billing('billing@fchip.com'),
  operations('operations@fchip.com'),
  hr('hr@fchip.com'),
  biomed('biomed@fchip.com'),
  housekeeping('housekeeping@fchip.com'),
  ambulance('ambulance@fchip.com'),
  patientPortal('patient.portal@fchip.com');

  const DemoAccount(this.email);

  final String email;
}
