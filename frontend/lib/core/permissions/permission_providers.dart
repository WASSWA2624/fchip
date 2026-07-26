import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/core/permissions/access_policy.dart';
import 'package:fchip/core/permissions/app_permission.dart';
import 'package:fchip/core/security/session_controller.dart';

final grantedAppPermissionsProvider = Provider<AppPermissionGrant>((ref) {
  return AppPermissionGrant(ref.watch(appAccessPolicyProvider).permissions);
});

final appAccessPolicyProvider = Provider<AppAccessPolicy>((ref) {
  return AppAccessPolicy.fromSession(
    ref.watch(sessionStateProvider.select((state) => state.session)),
  );
});
