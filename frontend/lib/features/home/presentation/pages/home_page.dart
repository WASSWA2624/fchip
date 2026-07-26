import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/app/theme/app_theme_extensions.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/components/app_button.dart';
import 'package:fchip/shared/components/app_logo_lockup.dart';
import 'package:fchip/shared/layout/layout.dart';

/// FCHIP home landing — welcome shell without hospital HIS dashboards.
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final ThemeData theme = Theme.of(context);
    final AppSpacingTokens spacing = theme.spacing;
    final l10n = context.l10n;

    return ResponsivePage(
      maxWidth: PageMaxWidth.reading,
      centerVertically: true,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          AppLogoLockup(
            wordmark: l10n.appShortTitle,
            slogan: l10n.appSlogan,
            mode: AppLogoLockupMode.full,
            logoSize: 56,
          ),
          SizedBox(height: spacing.lg),
          Text(
            l10n.appTitle,
            style: theme.textTheme.headlineMedium,
            textAlign: TextAlign.center,
          ),
          SizedBox(height: spacing.sm),
          Text(
            l10n.appSlogan,
            style: theme.textTheme.titleMedium?.copyWith(
              color: theme.colorScheme.onSurfaceVariant,
            ),
            textAlign: TextAlign.center,
          ),
          SizedBox(height: spacing.xl),
          Text(
            'Welcome to FairBanks Community Health Intelligence Platform.',
            style: theme.textTheme.bodyLarge,
            textAlign: TextAlign.center,
          ),
          SizedBox(height: spacing.lg),
          AppButton(
            label: l10n.navigationSettingsLabel,
            onPressed: () => context.go(AppRoutes.settings.location()),
          ),
        ],
      ),
    );
  }
}
