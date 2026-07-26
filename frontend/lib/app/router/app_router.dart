import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:fchip/app/router/app_route_icons.dart';
import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/app/router/route_guards.dart';
import 'package:fchip/app/router/route_refresh_listenable.dart';
import 'package:fchip/app/router/route_status_pages.dart';
import 'package:fchip/app/router/shell_badge_counts.dart';
import 'package:fchip/app/router/shell_route_access.dart';
import 'package:fchip/core/network/app_connectivity_status.dart';
import 'package:fchip/core/permissions/access_policy.dart';
import 'package:fchip/core/permissions/permission_providers.dart';
import 'package:fchip/core/security/auth_session.dart';
import 'package:fchip/core/security/session_controller.dart';
import 'package:fchip/core/subscriptions/tenant_subscription_summary.dart';
import 'package:fchip/features/access_admin/domain/entities/access_admin_entities.dart';
import 'package:fchip/features/access_admin/presentation/pages/access_admin_workspace_page.dart';
import 'package:fchip/features/auth/data/repositories/auth_repository_impl.dart';
import 'package:fchip/features/auth/presentation/pages/forgot_password_page.dart';
import 'package:fchip/features/auth/presentation/pages/login_page.dart';
import 'package:fchip/features/auth/presentation/pages/register_page.dart';
import 'package:fchip/features/auth/presentation/pages/reset_password_page.dart';
import 'package:fchip/features/auth/presentation/pages/verify_email_page.dart';
import 'package:fchip/features/auth/presentation/widgets/auth_shell_layout.dart';
import 'package:fchip/features/communications/domain/entities/communications_entities.dart';
import 'package:fchip/features/communications/presentation/pages/communications_workspace_page.dart';
import 'package:fchip/features/home/presentation/pages/home_page.dart';
import 'package:fchip/features/settings/presentation/pages/settings_page.dart'
    show SettingsPage, SettingsPageQuery;
import 'package:fchip/features/settings/presentation/widgets/settings_account_section.dart';
import 'package:fchip/features/subscriptions/domain/entities/subscription_entities.dart';
import 'package:fchip/features/subscriptions/presentation/pages/subscriptions_workspace_page.dart';
import 'package:fchip/features/subscriptions/presentation/widgets/subscription_expired_prompt.dart';
import 'package:fchip/features/subscriptions/presentation/widgets/subscription_header_button.dart';
import 'package:fchip/features/subscriptions/presentation/widgets/subscription_report_admins_dialog.dart';
import 'package:fchip/features/subscriptions/presentation/widgets/subscription_upgrade_dialog.dart';
import 'package:fchip/features/tenant_facility/presentation/pages/tenant_facility_setup_page.dart';
import 'package:fchip/features/tenant_facility/presentation/widgets/tenant_facility_setup_helpers.dart';
import 'package:fchip/l10n/app_localizations.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/layout/app_shell_sidebar_preference.dart';
import 'package:fchip/shared/layout/responsive_shell_scaffold.dart';
import 'package:fchip/shared/layout/shell_navigation_loading.dart';

final appInitialLocationProvider = Provider<String?>((ref) {
  return null;
});

final appRouterProvider = Provider<GoRouter>((ref) {
  final String? initialLocation = ref.watch(appInitialLocationProvider);
  final RouteRefreshListenable refreshListenable = ref.watch(
    routeRefreshListenableProvider,
  );

  return GoRouter(
    initialLocation: initialLocation,
    overridePlatformDefaultLocation: initialLocation != null,
    refreshListenable: refreshListenable,
    redirect: (_, GoRouterState state) {
      final AppRouteGuards guards = AppRouteGuards(
        sessionState: ref.read(sessionStateProvider),
      );

      return guards.redirect(
        AppRouteGuardRequest(
          location: state.uri,
          grantedPermissions: ref.read(grantedAppPermissionsProvider),
        ),
      );
    },
    routes: <RouteBase>[
      ShellRoute(
        builder: (_, GoRouterState state, Widget child) {
          return _AppShell(location: state.uri, child: child);
        },
        routes: <RouteBase>[
          GoRoute(
            path: AppRoutes.home.path,
            name: AppRoutes.home.name,
            builder: (_, _) => const HomePage(),
          ),
          GoRoute(
            path: AppRoutes.subscriptions.path,
            name: AppRoutes.subscriptions.name,
            builder: (_, GoRouterState state) {
              return SubscriptionsWorkspacePage(
                initialQuery: SubscriptionsWorkspaceQuery.fromUri(state.uri),
              );
            },
          ),
          GoRoute(
            path: AppRoutes.communications.path,
            name: AppRoutes.communications.name,
            builder: (_, GoRouterState state) {
              return CommunicationsWorkspacePage(
                initialQuery: CommunicationsWorkspaceQuery.fromUri(state.uri),
              );
            },
          ),
          GoRoute(
            path: AppRoutes.settings.path,
            name: AppRoutes.settings.name,
            builder: (_, GoRouterState state) => SettingsPage(
              initialQuery: SettingsPageQuery.fromUri(state.uri),
            ),
          ),
          GoRoute(
            path: AppRoutes.tenantFacilitySetup.path,
            name: AppRoutes.tenantFacilitySetup.name,
            builder: (_, GoRouterState state) => TenantFacilitySetupPage(
              initialQuery: TenantFacilitySetupPageQuery.fromUri(state.uri),
            ),
          ),
          GoRoute(
            path: AppRoutes.accessAdmin.path,
            name: AppRoutes.accessAdmin.name,
            builder: (_, GoRouterState state) {
              return AccessAdminWorkspacePage(
                initialQuery: AccessAdminWorkspaceQuery.fromUri(state.uri),
              );
            },
          ),
          GoRoute(
            path: AppRoutes.profile.path,
            name: AppRoutes.profile.name,
            redirect: (_, _) => const SettingsPageQuery(
              tab: 'account',
              panel: SettingsAccountSection.profilePanel,
            ).location(),
          ),
        ],
      ),
      ShellRoute(
        builder: (_, _, Widget child) => AuthShellLayout(child: child),
        routes: <RouteBase>[
          GoRoute(
            path: AppRoutes.login.path,
            name: AppRoutes.login.name,
            builder: (_, GoRouterState state) {
              return LoginPage(from: state.uri.queryParameters['from']);
            },
          ),
          GoRoute(
            path: AppRoutes.register.path,
            name: AppRoutes.register.name,
            builder: (_, _) => const RegisterPage(),
          ),
          GoRoute(
            path: AppRoutes.verifyEmail.path,
            name: AppRoutes.verifyEmail.name,
            builder: (_, GoRouterState state) {
              return VerifyEmailPage(
                token: state.uri.queryParameters['token'],
                email: state.uri.queryParameters['email'],
                reason: state.uri.queryParameters['reason'],
              );
            },
          ),
          GoRoute(
            path: AppRoutes.forgotPassword.path,
            name: AppRoutes.forgotPassword.name,
            builder: (_, _) => const ForgotPasswordPage(),
          ),
          GoRoute(
            path: AppRoutes.resetPassword.path,
            name: AppRoutes.resetPassword.name,
            builder: (_, GoRouterState state) {
              return ResetPasswordPage(
                token: state.uri.queryParameters['token'],
                email: state.uri.queryParameters['email'],
              );
            },
          ),
        ],
      ),
      GoRoute(
        path: AppRoutes.sessionRestoring.path,
        name: AppRoutes.sessionRestoring.name,
        builder: (_, _) => const SessionRestoringPage(),
      ),
      GoRoute(
        path: AppRoutes.authRequired.path,
        name: AppRoutes.authRequired.name,
        builder: (_, _) => const AuthRequiredPage(),
      ),
      GoRoute(
        path: AppRoutes.forbidden.path,
        name: AppRoutes.forbidden.name,
        builder: (_, _) => const ForbiddenPage(),
      ),
    ],
    errorBuilder: (_, GoRouterState state) {
      return NotFoundPage(location: state.uri.path);
    },
  );
});

final class _ShellDestinationRoute {
  const _ShellDestinationRoute({
    required this.route,
    required this.destination,
  });

  final AppRouteData route;
  final ResponsiveShellDestination destination;
}

List<_ShellDestinationRoute> _localizedShellDestinations(
  AppLocalizations l10n, {
  required AppAccessPolicy accessPolicy,
  int? subscriptionsWorkloadCount,
  int? communicationsWorkloadCount,
}) {
  final String overviewGroup = l10n.navigationGroupOverviewLabel;
  final String administrationGroup = l10n.navigationGroupAdministrationLabel;

  return <_ShellDestinationRoute>[
    _ShellDestinationRoute(
      route: AppRoutes.home,
      destination: ResponsiveShellDestination(
        label: l10n.navigationHomeLabel,
        shortLabel: l10n.navigationHomeShortLabel,
        groupLabel: overviewGroup,
        icon: AppRouteIcons.home,
        selectedIcon: AppRouteIcons.homeSelected,
      ),
    ),
    _ShellDestinationRoute(
      route: AppRoutes.communications,
      destination: ResponsiveShellDestination(
        label: l10n.navigationCommunicationsLabel,
        shortLabel: l10n.navigationCommunicationsShortLabel,
        groupLabel: administrationGroup,
        icon: AppRouteIcons.communications,
        selectedIcon: AppRouteIcons.communicationsSelected,
        badgeCount: communicationsWorkloadCount,
      ),
    ),
    _ShellDestinationRoute(
      route: AppRoutes.accessAdmin,
      destination: ResponsiveShellDestination(
        label: l10n.accessAdminTitle,
        shortLabel: 'Access',
        groupLabel: administrationGroup,
        icon: AppRouteIcons.accessAdmin,
        selectedIcon: AppRouteIcons.accessAdminSelected,
      ),
    ),
    _ShellDestinationRoute(
      route: AppRoutes.subscriptions,
      destination: ResponsiveShellDestination(
        label: l10n.navigationSubscriptionsLabel,
        shortLabel: l10n.navigationSubscriptionsShortLabel,
        groupLabel: administrationGroup,
        icon: AppRouteIcons.subscriptions,
        selectedIcon: AppRouteIcons.subscriptionsSelected,
        badgeCount: subscriptionsWorkloadCount,
      ),
    ),
    _ShellDestinationRoute(
      route: AppRoutes.settings,
      destination: ResponsiveShellDestination(
        label: l10n.navigationSettingsLabel,
        shortLabel: l10n.navigationSettingsShortLabel,
        groupLabel: administrationGroup,
        icon: AppRouteIcons.settings,
        selectedIcon: AppRouteIcons.settingsSelected,
      ),
    ),
    _ShellDestinationRoute(
      route: AppRoutes.tenantFacilitySetup,
      destination: ResponsiveShellDestination(
        label: tenantFacilitySetupNavigationLabel(accessPolicy, l10n),
        shortLabel: l10n.navigationSetupShortLabel,
        groupLabel: administrationGroup,
        icon: AppRouteIcons.setup,
        selectedIcon: AppRouteIcons.setupSelected,
      ),
    ),
  ];
}

class _AppShell extends ConsumerWidget {
  const _AppShell({required this.location, required this.child});

  final Uri location;
  final Widget child;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final AppLocalizations l10n = context.l10n;
    final accessPolicy = ref.watch(appAccessPolicyProvider);
    final bool canAccessCommunications = _canAccessShellRoute(
      AppRoutes.communications,
      accessPolicy,
    );
    final ShellBadgeCounts badges = ref.watch(shellBadgeCountsProvider);
    final List<_ShellDestinationRoute> shellDestinations =
        _localizedShellDestinations(
              l10n,
              accessPolicy: accessPolicy,
              subscriptionsWorkloadCount: badges.subscriptionsWorkloadCount,
              communicationsWorkloadCount: badges.communicationsWorkloadCount,
            )
            .where((_ShellDestinationRoute destination) {
              return _canAccessShellRoute(destination.route, accessPolicy);
            })
            .toList(growable: false);
    final int selectedIndex = _selectedIndexForPath(
      location.path,
      shellDestinations,
    );
    final AuthSession? session = ref.watch(
      sessionStateProvider.select((state) => state.session),
    );
    final AppConnectivityStatus connectivityStatus = ref
        .watch(appConnectivityStatusProvider)
        .when(
          data: (AppConnectivityStatus status) => status,
          error: (_, _) => AppConnectivityStatus.online,
          loading: () => AppConnectivityStatus.online,
        );
    final bool isShellLoading = ref.watch(shellNavigationLoadingProvider);

    return SubscriptionExpiredPromptHost(
      summary: session?.subscriptionSummary,
      platformAdminContact: session?.platformAdminContact,
      tenantAdminContacts:
          session?.tenantAdminContacts ?? const <OrgAdminContact>[],
      facilityAdminContacts:
          session?.facilityAdminContacts ?? const <OrgAdminContact>[],
      canManageBilling: ref
          .watch(appAccessPolicyProvider)
          .canManageSubscriptionBilling(),
      onRenewed: () async {
        if (session == null) {
          return;
        }
        final refreshResult = await ref
            .read(authRepositoryProvider)
            .fetchCurrentUser(session);
        refreshResult.when(
          success: (AuthSession refreshed) {
            ref.read(sessionStateProvider.notifier).persistSession(refreshed);
          },
          failure: (_) {},
        );
      },
      child: ResponsiveAppShell(
        title: l10n.appTitle,
        compactTitle: l10n.appShortTitle,
        initialSidebarCollapsed: ref.watch(appShellSidebarCollapsedProvider),
        onSidebarCollapsedChanged: (bool collapsed) {
          unawaited(
            ref
                .read(appShellSidebarCollapsedProvider.notifier)
                .setCollapsed(collapsed: collapsed),
          );
        },
        connectivityStatus: connectivityStatus,
        onlineLabel: l10n.appStatusOnlineLabel,
        offlineLabel: l10n.appStatusOfflineLabel,
        fullscreenEnterLabel: l10n.workspaceFullscreenEnterLabel,
        fullscreenExitLabel: l10n.workspaceFullscreenExitLabel,
        openMenuTooltip: l10n.appOpenNavigationMenuTooltip,
        closeDrawerTooltip: l10n.appCloseNavigationMenuTooltip,
        toggleSidebarTooltip: l10n.appToggleSidebarTooltip,
        navigationSearchLabel: l10n.appNavigationSearchLabel,
        navigationSearchHint: l10n.appNavigationSearchHint,
        navigationSearchNoResultsLabel: l10n.appNavigationSearchNoResultsLabel,
        accountTooltip: l10n.appAccountTooltip,
        notificationsTooltip: l10n.appNotificationsTooltip,
        unreadNotificationCount: badges.notificationUnreadCount ?? 0,
        notificationsUnreadLabel: l10n.appNotificationsUnreadLabel(
          badges.notificationUnreadCount ?? 0,
        ),
        onNotificationsSelected: canAccessCommunications
            ? () {
                context.go(
                  AppRoutes.communications.location(
                    queryParameters: <String, String>{
                      'panel': CommunicationsPanel.notifications.serverValue,
                    },
                  ),
                );
              }
            : null,
        profileLabel: l10n.appUserMenuProfileLabel,
        settingsLabel: l10n.appUserMenuSettingsLabel,
        changePasswordLabel: l10n.appUserMenuChangePasswordLabel,
        logoutLabel: l10n.appUserMenuLogoutLabel,
        signedInLabel: l10n.appUserMenuSignedInLabel,
        userProfile: _userMenuProfile(session),
        showUserAvatar: session != null,
        onProfileSelected: () {
          final String target = const SettingsPageQuery(
            tab: 'account',
            panel: SettingsAccountSection.profilePanel,
          ).location();
          context.go(target);
        },
        onSettingsSelected: () {
          if (!AppRoutes.settings.matchesPath(location.path)) {
            context.go(AppRoutes.settings.location());
          }
        },
        onChangePasswordSelected: () {
          final String target = const SettingsPageQuery(
            tab: 'account',
            panel: SettingsAccountSection.changePasswordPanel,
          ).location();
          context.go(target);
        },
        onLogoutSelected: () async {
          await ref.read(authRepositoryProvider).logout();
          await ref.read(sessionStateProvider.notifier).logout();
          if (context.mounted) {
            context.go(AppRoutes.login.location());
          }
        },
        headerTrailingActions: _subscriptionHeaderAction(
          context: context,
          ref: ref,
          session: session,
          l10n: l10n,
        ),
        destinations: <ResponsiveShellDestination>[
          for (final _ShellDestinationRoute destination in shellDestinations)
            destination.destination,
        ],
        selectedIndex: selectedIndex,
        onDestinationSelected: (int index) {
          if (index == selectedIndex) {
            return;
          }

          context.go(shellDestinations[index].route.location());
        },
        isShellLoading: isShellLoading,
        shellRouteKey: location.path,
        child: child,
      ),
    );
  }

  int _selectedIndexForPath(
    String locationPath,
    List<_ShellDestinationRoute> shellDestinations,
  ) {
    final int index = shellDestinations.indexWhere((
      _ShellDestinationRoute destination,
    ) {
      return destination.route.matchesPath(locationPath);
    });

    return index < 0 ? 0 : index;
  }
}

bool _canAccessShellRoute(AppRouteData route, AppAccessPolicy accessPolicy) {
  return canAccessShellRoute(route, accessPolicy);
}

Widget? _subscriptionHeaderAction({
  required BuildContext context,
  required WidgetRef ref,
  required AuthSession? session,
  required AppLocalizations l10n,
}) {
  if (session == null) {
    return null;
  }

  final TenantSubscriptionSummary? summary = session.subscriptionSummary;
  if (summary == null || !summary.headerState.isHydrated) {
    return null;
  }

  final bool canManageBilling = ref
      .watch(appAccessPolicyProvider)
      .canManageSubscriptionBilling();
  final bool needsAttention =
      summary.headerState == TenantSubscriptionHeaderState.expired ||
      summary.headerState == TenantSubscriptionHeaderState.expiringSoon;

  VoidCallback? onPressed;
  if (canManageBilling) {
    onPressed = () async {
      final bool? submitted = await showSubscriptionUpgradeDialog(
        context,
        initialSummary: summary,
        initialAdminContact: session.platformAdminContact,
      );
      if (submitted != true || !context.mounted) {
        return;
      }

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(l10n.subscriptionUpgradeSubmittedMessage)),
      );

      final refreshResult = await ref
          .read(authRepositoryProvider)
          .fetchCurrentUser(session);
      refreshResult.when(
        success: (AuthSession refreshed) {
          ref.read(sessionStateProvider.notifier).persistSession(refreshed);
        },
        failure: (_) {},
      );
    };
  } else if (needsAttention) {
    onPressed = () {
      unawaited(
        showSubscriptionReportAdminsDialog(
          context,
          headerState: summary.headerState,
          tenantAdmins: session.tenantAdminContacts,
          facilityAdmins: session.facilityAdminContacts,
          platformAdminContact: session.platformAdminContact,
        ),
      );
    };
  }

  return SubscriptionHeaderButton(summary: summary, onPressed: onPressed);
}

UserMenuProfileData? _userMenuProfile(AuthSession? session) {
  if (session == null) {
    return null;
  }

  final AuthUserProfile? user = session.user;
  final String? subject = _nonEmpty(session.subject);
  final String? email = _nonEmpty(user?.email) ?? _emailFromSubject(subject);
  final String? name =
      _nonEmpty(user?.fullName) ??
      _nonEmpty(user?.effectiveTitle) ??
      _distinct(subject, email) ??
      email;
  final String? initials =
      _nonEmpty(user?.initials) ?? _initialsFrom(name ?? email);

  return UserMenuProfileData(
    name: name,
    email: email,
    title:
        _distinct(user?.facilityName, name) ??
        _distinct(user?.effectiveTitle, name),
    overallRole: user?.overallRole,
    userType: user?.userType,
    initials: initials,
  );
}

String? _emailFromSubject(String? subject) {
  if (subject == null || !subject.contains('@')) {
    return null;
  }

  return subject;
}

final RegExp _initialsDelimiterPattern = RegExp(r'[@._-]+');
final RegExp _whitespacePattern = RegExp(r'\s+');

String? _initialsFrom(String? value) {
  final String? normalized = _nonEmpty(value);
  if (normalized == null) {
    return null;
  }

  final List<String> words = normalized
      .replaceAll(_initialsDelimiterPattern, ' ')
      .split(_whitespacePattern)
      .where((String word) => word.isNotEmpty)
      .toList(growable: false);
  if (words.isEmpty) {
    return null;
  }
  if (words.length == 1) {
    return words.first.substring(0, 1).toUpperCase();
  }

  return <String>[
    words.first.substring(0, 1),
    words.last.substring(0, 1),
  ].join().toUpperCase();
}

String? _distinct(String? value, String? other) {
  final String? normalized = _nonEmpty(value);
  final String? normalizedOther = _nonEmpty(other);
  if (normalized == null) {
    return null;
  }
  if (normalizedOther != null &&
      normalized.toLowerCase() == normalizedOther.toLowerCase()) {
    return null;
  }

  return normalized;
}

String? _nonEmpty(String? value) {
  final String? normalized = value?.trim();
  return normalized == null || normalized.isEmpty ? null : normalized;
}
