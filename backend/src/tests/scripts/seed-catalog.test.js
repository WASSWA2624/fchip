const {
  DEMO_ADD_ON_CATALOG,
  DEMO_PLAN_CATALOG,
  DEMO_ROLE_CODES,
  DEMO_TENANT} = require('../../../scripts/seeders/seed-catalog');

describe('seed-catalog', () => {
  it('keeps canonical plan tier coverage aligned to the pricing baseline', () => {
    expect(DEMO_PLAN_CATALOG.map((entry) => entry.code)).toEqual([
      'free',
      'basic',
      'advanced',
      'pro',
      'custom',
      'developer']);

    const basicPlan = DEMO_PLAN_CATALOG.find((entry) => entry.code === 'basic');
    expect(basicPlan.max_facilities).toBe(1);

    const proPlan = DEMO_PLAN_CATALOG.find((entry) => entry.code === 'pro');
    expect(proPlan.extension_json.price_notes.yearly).toBe(890);
  });

  it('keeps optional suites explicitly scoped to custom plans', () => {
    expect(DEMO_ADD_ON_CATALOG.map((entry) => entry.code)).toEqual([
      'compliance_audit_suite',
      'integrations_webhooks_pack']);
    expect(
      DEMO_ADD_ON_CATALOG.every(
        (entry) => entry.minimum_plan_tier_code === 'CUSTOM',
      ),
    ).toBe(true);
  });

  it('pins the default seeded login emails for the demo workspace', () => {
    expect(DEMO_TENANT.users.map((entry) => entry.email)).toEqual([
      'super.admin@fchip.com',
      'tenant.admin@fchip.com',
      'facility.admin@fchip.com',
      'doctor@fchip.com',
      'nurse@fchip.com',
      'lab@fchip.com',
      'radiology@fchip.com',
      'pharmacy@fchip.com',
      'reception@fchip.com',
      'billing@fchip.com',
      'operations@fchip.com',
      'hr@fchip.com',
      'biomed@fchip.com',
      'housekeeping@fchip.com',
      'mortuary.staff@fchip.com',
      'mortuary.manager@fchip.com',
      'ambulance@fchip.com',
      'patient.portal@fchip.com']);
  });

  it('keeps every demo user role inside the complete shipped role catalog', () => {
    const assignedRoles = DEMO_TENANT.users.flatMap((entry) => [
      entry.role,
      ...((Array.isArray(entry.extra_roles) ? entry.extra_roles : []).filter(Boolean))]);

    expect(new Set(assignedRoles).size).toBe(assignedRoles.length);
    expect(
      assignedRoles.every((role) => DEMO_ROLE_CODES.includes(role)),
    ).toBe(true);
    expect(DEMO_ROLE_CODES).toEqual(
      expect.arrayContaining([
        'INTEGRATION_ADMIN',
        'HR_STAFF',
        'DISCHARGE_PLANNER',
        'DENTIST',
        'RADIOLOGIST',
        'SONOGRAPHER',
        'ACCOUNTANT',
        'SUPPORT_STAFF',
        'VISITOR_GUEST']),
    );
  });
});
