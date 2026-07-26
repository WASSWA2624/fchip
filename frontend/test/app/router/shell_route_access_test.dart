import 'package:flutter_test/flutter_test.dart';
import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/app/router/shell_route_access.dart';
import 'package:fchip/core/permissions/access_policy.dart';
import 'package:fchip/core/security/auth_session.dart';
import 'package:fchip/core/security/session_tokens.dart';

const List<AppModuleEntitlement> _activeShellModules = <AppModuleEntitlement>[
  AppModuleEntitlement(
    code: 'notifications-communications',
    licenseStatus: 'ACTIVE',
  ),
];

void main() {
  group('shell route access (FCHIP)', () {
    AppAccessPolicy policyForRole(String role) {
      return AppAccessPolicy.fromSession(
        AuthSession(
          tokens: SessionTokens(accessToken: 'token'),
          user: AuthUserProfile(
            tenantId: 'tenant-1',
            facilityId: 'facility-1',
            roles: <String>[role],
          ),
          moduleEntitlements: _activeShellModules,
        ),
      );
    }

    test('authenticated users can open home and settings', () {
      final AppAccessPolicy policy = policyForRole('DOCTOR');
      expect(canAccessShellRoute(AppRoutes.home, policy), isTrue);
      expect(canAccessShellRoute(AppRoutes.settings, policy), isTrue);
    });

    test('communications requires module + role/permission pack', () {
      final AppAccessPolicy doctor = policyForRole('DOCTOR');
      expect(canAccessShellRoute(AppRoutes.communications, doctor), isTrue);

      final AppAccessPolicy patient = policyForRole('PATIENT');
      // Patient role is not in communicationsWorkspaceRoles.
      expect(canAccessShellRoute(AppRoutes.communications, patient), isFalse);
    });

    test('subscriptions is super-admin only', () {
      final AppAccessPolicy admin = policyForRole('SUPER_ADMIN');
      expect(canAccessShellRoute(AppRoutes.subscriptions, admin), isTrue);

      final AppAccessPolicy doctor = policyForRole('DOCTOR');
      expect(canAccessShellRoute(AppRoutes.subscriptions, doctor), isFalse);
    });

    test('access admin is available to facility admins', () {
      final AppAccessPolicy facilityAdmin = policyForRole('FACILITY_ADMIN');
      expect(canAccessShellRoute(AppRoutes.accessAdmin, facilityAdmin), isTrue);

      final AppAccessPolicy doctor = policyForRole('DOCTOR');
      expect(canAccessShellRoute(AppRoutes.accessAdmin, doctor), isFalse);
    });
  });
}
