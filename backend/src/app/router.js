/**
 * Root Router
 *
 * Health endpoints are at root level (not under /api/v1/)
 * Per health-checks.md: Health endpoints are public at root level
 * Per api-versioning.md: All API endpoints must be versioned under /api/v1/
 *
 * Clinical / hospital HIS modules are unmounted. This router mounts
 * FCHIP platform auth, tenancy, access, notifications, audit, consent,
 * subscriptions, and integration skeleton only.
 */

const express = require('express');
const router = express.Router();

// Health check utilities
const { healthCheck, readinessCheck, livenessCheck } = require('@lib/health');
const { asyncHandler } = require('@lib/async');
const { authenticate } = require('@middlewares/auth.middleware');
const { hydrateRequestScope, enforceTenantScope } = require('@middlewares/tenant-scope.middleware');
const { hydrateRequestContext } = require('@middlewares/request-context.middleware');
const { enforceModuleEntitlement } = require('@middlewares/module-entitlement.middleware');
const { enforceAbacAccess } = require('@middlewares/abac.middleware');

/**
 * @description Health check endpoint (public)
 * @method GET
 * @route /health
 * @authentication None
 * @permissions Public
 * @urlParams None
 * @queryParams None
 * @bodyParams None
 * @returns {Object} Health status payload
 * @throws 503 Service unavailable
 */
router.get('/health', (req, res) => {
  const health = healthCheck();
  const statusCode = health.status === 'healthy' ? 200 : 503;
  return res.status(statusCode).json(health);
});

/**
 * @description Readiness check endpoint (public)
 * @method GET
 * @route /ready
 * @authentication None
 * @permissions Public
 * @urlParams None
 * @queryParams None
 * @bodyParams None
 * @returns {Object} Readiness status payload
 * @throws 503 Service unavailable
 */
router.get('/ready', asyncHandler(async (req, res) => {
  const readiness = await readinessCheck();
  const statusCode = readiness.status === 'ready' ? 200 : 503;
  return res.status(statusCode).json(readiness);
}));

/**
 * @description Liveness check endpoint (public)
 * @method GET
 * @route /live
 * @authentication None
 * @permissions Public
 * @urlParams None
 * @queryParams None
 * @bodyParams None
 * @returns {Object} Liveness status payload
 */
router.get('/live', (req, res) => {
  const liveness = livenessCheck();
  return res.status(200).json(liveness);
});

/**
 * API v1 Router
 * Per api-versioning.mdc: All API endpoints must be versioned
 * Per module-creation.mdc: Modules are mounted under /api/v1/<module>
 */
const apiV1Router = express.Router();

// Public / auth (before authenticate middleware)
apiV1Router.use('/auth', require('../modules/auth/routes/auth.routes'));
apiV1Router.use('/public', require('../modules/public/routes/public.routes'));

// Global protection for all non-auth API v1 routes.
apiV1Router.use(authenticate());
apiV1Router.use(hydrateRequestScope());
apiV1Router.use(enforceTenantScope());
apiV1Router.use(hydrateRequestContext());
apiV1Router.use(require('../middlewares/live-access.middleware').hydrateLiveAccess());
apiV1Router.use(enforceModuleEntitlement());
apiV1Router.use(enforceAbacAccess());

// Identity / sessions
apiV1Router.use('/user-sessions', require('../modules/user-session/routes/user-session.routes'));
apiV1Router.use('/users', require('../modules/user/routes/user.routes'));
apiV1Router.use('/user-profiles', require('../modules/user-profile/routes/user-profile.routes'));
apiV1Router.use('/user-roles', require('../modules/user-role/routes/user-role.routes'));
apiV1Router.use('/user-mfas', require('../modules/user-mfa/routes/user-mfa.routes'));
apiV1Router.use('/oauth-accounts', require('../modules/oauth-account/routes/oauth-account.routes'));

// Access control
apiV1Router.use('/roles', require('../modules/role/routes/role.routes'));
apiV1Router.use('/permissions', require('../modules/permission/routes/permission.routes'));
apiV1Router.use('/role-permissions', require('../modules/role-permission/routes/role-permission.routes'));
apiV1Router.use('/abac-policies', require('../modules/abac-policy/routes/abac-policy.routes'));
apiV1Router.use('/api-keys', require('../modules/api-key/routes/api-key.routes'));
apiV1Router.use('/api-key-permissions', require('../modules/api-key-permission/routes/api-key-permission.routes'));

// Tenancy / facility setup (light org tree)
apiV1Router.use('/tenants', require('../modules/tenant/routes/tenant.routes'));
apiV1Router.use('/facilities', require('../modules/facility/routes/facility.routes'));
apiV1Router.use('/departments', require('../modules/department/routes/department.routes'));
apiV1Router.use('/units', require('../modules/unit/routes/unit.routes'));
apiV1Router.use('/addresses', require('../modules/address/routes/address.routes'));
apiV1Router.use('/contacts', require('../modules/contact/routes/contact.routes'));
apiV1Router.use('/tenant-facility-workspace', require('../modules/tenant-facility-workspace/routes/tenant-facility-workspace.routes'));
apiV1Router.use('/access-admin-workspace', require('../modules/access-admin-workspace/routes/access-admin-workspace.routes'));
apiV1Router.use('/settings-workspace', require('../modules/settings-workspace/routes/settings-workspace.routes'));

// Consent / terms
apiV1Router.use('/consents', require('../modules/consent/routes/consent.routes'));
apiV1Router.use('/terms-acceptances', require('../modules/terms-acceptance/routes/terms-acceptance.routes'));

// Notifications
apiV1Router.use('/notifications', require('../modules/notification/routes/notification.routes'));
apiV1Router.use('/notification-deliveries', require('../modules/notification-delivery/routes/notification-delivery.routes'));

// Audit
apiV1Router.use('/audit-logs', require('../modules/audit-log/routes/audit-log.routes'));

// Templates (auth emails)
apiV1Router.use('/templates', require('../modules/template/routes/template.routes'));
apiV1Router.use('/template-variables', require('../modules/template-variable/routes/template-variable.routes'));

// Dashboard / analytics (home)
apiV1Router.use('/dashboard-widgets', require('../modules/dashboard-widget/routes/dashboard-widget.routes'));
apiV1Router.use('/dashboard-workspace', require('../modules/dashboard-workspace/routes/dashboard-workspace.routes'));
apiV1Router.use('/analytics-events', require('../modules/analytics-event/routes/analytics-event.routes'));

// Subscriptions / licensing
apiV1Router.use('/subscriptions-workspace', require('../modules/subscriptions-workspace/routes/subscriptions-workspace.routes'));
apiV1Router.use('/subscription-plans', require('../modules/subscription-plan/routes/subscription-plan.routes'));
apiV1Router.use('/subscriptions', require('../modules/subscription/routes/subscription.routes'));
apiV1Router.use('/subscription-invoices', require('../modules/subscription-invoice/routes/subscription-invoice.routes'));
apiV1Router.use('/modules', require('../modules/module/routes/module.routes'));
apiV1Router.use('/module-subscriptions', require('../modules/module-subscription/routes/module-subscription.routes'));
apiV1Router.use('/licenses', require('../modules/license/routes/license.routes'));

// Integrations skeleton (future EMR connector)
apiV1Router.use('/integrations', require('../modules/integration/routes/integration.routes'));
apiV1Router.use('/integration-logs', require('../modules/integration-log/routes/integration-log.routes'));
apiV1Router.use('/webhook-subscriptions', require('../modules/webhook-subscription/routes/webhook-subscription.routes'));
apiV1Router.use('/interop', require('../modules/interop/routes/interop.routes'));

// Mount API v1 router
router.use('/api/v1', apiV1Router);

module.exports = router;
