import 'package:fchip/core/permissions/access_policy.dart';
import 'package:fchip/core/permissions/access_requirement.dart';
import 'package:fchip/core/permissions/app_permission.dart';

enum AppRouteAccess { public, authenticated }

final class AppRouteData {
  const AppRouteData({
    required this.name,
    required this.path,
    this.access = AppRouteAccess.public,
    this.requiredPermissions = const <AppPermission>[],
    this.requiredAnyPermissions = const <AppPermission>[],
    this.requiredAnyRoles = const <AppRole>[],
    this.requiredActiveModules = const <String>[],
    this.requiresTenantContext = false,
    this.requiresFacilityContext = false,
  });

  final String name;
  final String path;
  final AppRouteAccess access;
  final Iterable<AppPermission> requiredPermissions;
  final Iterable<AppPermission> requiredAnyPermissions;
  final Iterable<AppRole> requiredAnyRoles;
  final Iterable<String> requiredActiveModules;
  final bool requiresTenantContext;
  final bool requiresFacilityContext;

  bool get requiresAuthenticatedSession {
    return access == AppRouteAccess.authenticated ||
        accessRequirement.isEmpty == false;
  }

  AccessRequirement get accessRequirement {
    return AccessRequirement(
      allPermissions: requiredPermissions,
      anyPermissions: requiredAnyPermissions,
      anyRoles: requiredAnyRoles,
      activeModules: requiredActiveModules,
      requiresTenantContext: requiresTenantContext,
      requiresFacilityContext: requiresFacilityContext,
    );
  }

  bool get isAuthEntryRoute {
    return path == AppRoutes.login.path ||
        path == AppRoutes.register.path ||
        path == AppRoutes.verifyEmail.path ||
        path == AppRoutes.forgotPassword.path ||
        path == AppRoutes.resetPassword.path;
  }

  bool matchesPath(String locationPath) {
    return locationPath == path;
  }

  String location({
    Map<String, String> queryParameters = const <String, String>{},
  }) {
    return Uri(
      path: path,
      queryParameters: queryParameters.isEmpty ? null : queryParameters,
    ).toString();
  }

  String locationWithFrom(Uri from) {
    return location(queryParameters: <String, String>{'from': from.toString()});
  }
}

abstract final class AppRoutes {
  static const List<AppRole> adminShellRoles = <AppRole>[
    AppRole.superAdmin,
    AppRole.tenantAdmin,
    AppRole.facilityAdmin,
  ];

  static const List<AppRole> communicationsWorkspaceRoles = <AppRole>[
    ...adminShellRoles,
    AppRole.doctor,
    AppRole.nurse,
    AppRole.labTech,
    AppRole.radiologyTech,
    AppRole.pharmacist,
    AppRole.receptionist,
    AppRole.billing,
    AppRole.operations,
    AppRole.hr,
    AppRole.biomed,
    AppRole.houseKeeper,
    AppRole.ambulanceOperator,
    AppRole.wardManager,
    AppRole.icuManager,
    AppRole.theatreManager,
    AppRole.housekeepingManager,
    AppRole.biomedManager,
    AppRole.mortuaryStaff,
    AppRole.mortuaryManager,
  ];

  static const List<AppRole> tenantSetupWorkspaceRoles = <AppRole>[
    ...adminShellRoles,
  ];

  static const AppRouteData home = AppRouteData(
    name: 'home',
    path: '/',
    access: AppRouteAccess.authenticated,
  );
  static const AppRouteData settings = AppRouteData(
    name: 'settings',
    path: '/settings',
    access: AppRouteAccess.authenticated,
  );
  static const AppRouteData subscriptions = AppRouteData(
    name: 'subscriptions',
    path: '/subscriptions',
    access: AppRouteAccess.authenticated,
    requiredAnyRoles: <AppRole>[AppRole.superAdmin],
  );
  static const AppRouteData communications = AppRouteData(
    name: 'communications',
    path: '/communications',
    access: AppRouteAccess.authenticated,
    requiredAnyPermissions: <AppPermission>[
      AppPermissions.communicationsRead,
      AppPermissions.communicationsWrite,
    ],
    requiredAnyRoles: communicationsWorkspaceRoles,
    requiredActiveModules: <String>['notifications-communications'],
  );
  static const AppRouteData tenantFacilitySetup = AppRouteData(
    name: 'tenantFacilitySetup',
    path: '/admin/setup',
    access: AppRouteAccess.authenticated,
    requiredAnyPermissions: <AppPermission>[
      AppPermissions.tenantAdmin,
      AppPermissions.facilityAdmin,
      AppPermissions.systemAdmin,
    ],
    requiredAnyRoles: tenantSetupWorkspaceRoles,
    requiresFacilityContext: true,
  );
  static const AppRouteData accessAdmin = AppRouteData(
    name: 'accessAdmin',
    path: '/admin/access',
    access: AppRouteAccess.authenticated,
    requiredAnyPermissions: <AppPermission>[
      AppPermissions.tenantAdmin,
      AppPermissions.facilityAdmin,
      AppPermissions.systemAdmin,
    ],
    requiredAnyRoles: <AppRole>[
      AppRole.superAdmin,
      AppRole.tenantAdmin,
      AppRole.facilityAdmin,
      AppRole.operations,
    ],
    requiresTenantContext: true,
  );
  static const AppRouteData profile = AppRouteData(
    name: 'profile',
    path: '/profile',
    access: AppRouteAccess.authenticated,
  );

  static const AppRouteData login = AppRouteData(name: 'login', path: '/login');

  static const AppRouteData register = AppRouteData(
    name: 'register',
    path: '/register',
  );

  static const AppRouteData verifyEmail = AppRouteData(
    name: 'verifyEmail',
    path: '/verify-email',
  );

  static const AppRouteData forgotPassword = AppRouteData(
    name: 'forgotPassword',
    path: '/forgot-password',
  );

  static const AppRouteData resetPassword = AppRouteData(
    name: 'resetPassword',
    path: '/reset-password',
  );

  static const AppRouteData sessionRestoring = AppRouteData(
    name: 'sessionRestoring',
    path: '/session-restoring',
  );

  static const AppRouteData authRequired = AppRouteData(
    name: 'authRequired',
    path: '/auth-required',
  );

  static const AppRouteData forbidden = AppRouteData(
    name: 'forbidden',
    path: '/forbidden',
  );

  static const List<AppRouteData> all = <AppRouteData>[
    home,
    subscriptions,
    communications,
    settings,
    tenantFacilitySetup,
    accessAdmin,
    profile,
    login,
    register,
    verifyEmail,
    forgotPassword,
    resetPassword,
    sessionRestoring,
    authRequired,
    forbidden,
  ];

  static const List<AppRouteData> shellRoutes = <AppRouteData>[
    home,
    subscriptions,
    communications,
    settings,
    tenantFacilitySetup,
    accessAdmin,
  ];

  static AppRouteData? matchPath(String locationPath) {
    for (final AppRouteData route in all) {
      if (route.matchesPath(locationPath)) {
        return route;
      }
    }

    return null;
  }

  /// Permission domains that may unlock [route] for custom-role-only users.
  ///
  /// - `null`: core destinations (home/settings) always allowed when authenticated
  /// - empty: custom roles cannot unlock (canonical staff roles only)
  /// - non-empty: at least one satisfying permission must use one of these domains
  static Set<String>? permissionScopedDomainsFor(AppRouteData route) {
    switch (route.name) {
      case 'home':
      case 'settings':
      case 'profile':
        return null;
      case 'tenantFacilitySetup':
        return const <String>{
          'hr',
          'unit',
          'roster',
          'tenant',
          'facility',
          'system',
        };
      case 'communications':
        return const <String>{'communications'};
      case 'accessAdmin':
        return const <String>{'tenant', 'facility', 'system'};
      case 'subscriptions':
        return const <String>{'subscriptions'};
      default:
        return const <String>{};
    }
  }
}
