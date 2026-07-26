import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/core/permissions/access_policy.dart';

bool canAccessShellRoute(AppRouteData route, AppAccessPolicy accessPolicy) {
  if (!route.accessRequirement.isAllowed(accessPolicy)) {
    return false;
  }

  // Custom roles / direct grants only: map permissions to their home workspaces
  // instead of letting broad route any-permission lists leak across modules.
  if (accessPolicy.isPermissionScopedShellUser) {
    return accessPolicy.isShellRouteAllowedByPermissionDomain(
      allPermissions: route.requiredPermissions,
      anyPermissions: route.requiredAnyPermissions,
      allowedDomains: AppRoutes.permissionScopedDomainsFor(route),
    );
  }

  return true;
}
