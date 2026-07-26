import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/app/router/shell_route_access.dart';
import 'package:fchip/core/errors/result.dart';
import 'package:fchip/core/permissions/permission_providers.dart';
import 'package:fchip/features/communications/domain/entities/communications_entities.dart';
import 'package:fchip/features/communications/presentation/controllers/communications_workspace_controller.dart';
import 'package:fchip/features/subscriptions/domain/entities/subscription_entities.dart';
import 'package:fchip/features/subscriptions/presentation/controllers/subscriptions_workspace_controller.dart';

@immutable
final class ShellBadgeCounts {
  const ShellBadgeCounts({
    this.subscriptionsWorkloadCount,
    this.communicationsWorkloadCount,
    this.notificationUnreadCount,
  });

  static const ShellBadgeCounts empty = ShellBadgeCounts();

  final int? subscriptionsWorkloadCount;
  final int? communicationsWorkloadCount;
  final int? notificationUnreadCount;

  @override
  bool operator ==(Object other) {
    return identical(this, other) ||
        other is ShellBadgeCounts &&
            subscriptionsWorkloadCount == other.subscriptionsWorkloadCount &&
            communicationsWorkloadCount == other.communicationsWorkloadCount &&
            notificationUnreadCount == other.notificationUnreadCount;
  }

  @override
  int get hashCode => Object.hash(
    subscriptionsWorkloadCount,
    communicationsWorkloadCount,
    notificationUnreadCount,
  );
}

int? _positiveOrNull(int count) => count > 0 ? count : null;

int? _selectBadge<T>(
  AsyncValue<Result<T>> value,
  int? Function(T state) selector,
) {
  return value.maybeWhen(
    data: (Result<T> result) {
      return result.when(
        success: selector,
        failure: (_) => null,
      );
    },
    orElse: () => null,
  );
}

final shellBadgeCountsProvider = Provider<ShellBadgeCounts>((Ref ref) {
  final accessPolicy = ref.watch(appAccessPolicyProvider);
  final bool canSubscriptions = canAccessShellRoute(
    AppRoutes.subscriptions,
    accessPolicy,
  );
  final bool canCommunications = canAccessShellRoute(
    AppRoutes.communications,
    accessPolicy,
  );

  return ShellBadgeCounts(
    subscriptionsWorkloadCount: canSubscriptions
        ? ref.watch(
            subscriptionsWorkspaceControllerProvider.select(
              (v) => _selectBadge<SubscriptionsWorkspaceState>(
                v,
                (s) => _positiveOrNull(s.workloadCount),
              ),
            ),
          )
        : null,
    communicationsWorkloadCount: canCommunications
        ? ref.watch(
            communicationsWorkspaceControllerProvider.select(
              (v) => _selectBadge<CommunicationsWorkspaceState>(
                v,
                (s) => _positiveOrNull(s.workloadCount),
              ),
            ),
          )
        : null,
    notificationUnreadCount: canCommunications
        ? ref.watch(
            communicationsWorkspaceControllerProvider.select(
              (v) => _selectBadge<CommunicationsWorkspaceState>(v, (s) {
                return s.unreadBadgeCount > 0 ? s.unreadBadgeCount : null;
              }),
            ),
          )
        : null,
  );
});
