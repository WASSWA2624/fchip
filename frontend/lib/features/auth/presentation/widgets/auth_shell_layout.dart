import 'package:fchip/app/theme/app_theme_extensions.dart';
import 'package:fchip/core/responsive/app_breakpoints.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/components/app_logo_lockup.dart';
import 'package:flutter/material.dart';

class AuthShellLayout extends StatelessWidget {
  const AuthShellLayout({required this.child, super.key});

  final Widget child;

  @override
  Widget build(BuildContext context) {
    final ThemeData theme = Theme.of(context);
    final ColorScheme colorScheme = theme.colorScheme;
    final AppBreakpoint breakpoint = AppBreakpoints.of(context);

    return Scaffold(
      body: DecoratedBox(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: <Color>[
              colorScheme.primaryContainer.withValues(alpha: 0.45),
              theme.scaffoldBackgroundColor,
              theme.scaffoldBackgroundColor,
            ],
            stops: const <double>[0, 0.32, 1],
          ),
        ),
        child: SafeArea(
          child: LayoutBuilder(
            builder: (BuildContext context, BoxConstraints constraints) {
              final double maxFormWidth = switch (breakpoint) {
                AppBreakpoint.xs || AppBreakpoint.sm => constraints.maxWidth,
                AppBreakpoint.md => constraints.maxWidth.clamp(0, 480),
                _ => constraints.maxWidth.clamp(0, 520),
              };

              final EdgeInsets pagePadding = EdgeInsets.symmetric(
                horizontal: theme.spacing.lg,
                vertical: switch (breakpoint) {
                  AppBreakpoint.xs || AppBreakpoint.sm => theme.spacing.md,
                  _ => theme.spacing.xl,
                },
              );

              return SingleChildScrollView(
                child: ConstrainedBox(
                  constraints: BoxConstraints(minHeight: constraints.maxHeight),
                  child: Center(
                    child: ConstrainedBox(
                      constraints: BoxConstraints(maxWidth: maxFormWidth),
                      child: Padding(
                        padding: pagePadding,
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: <Widget>[
                            const _AuthBrandHeader(),
                            SizedBox(
                              height: switch (breakpoint) {
                                AppBreakpoint.xs ||
                                AppBreakpoint.sm => theme.spacing.lg,
                                _ => theme.spacing.xl,
                              },
                            ),
                            child,
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              );
            },
          ),
        ),
      ),
    );
  }
}

class _AuthBrandHeader extends StatelessWidget {
  const _AuthBrandHeader();

  @override
  Widget build(BuildContext context) {
    final ThemeData theme = Theme.of(context);
    final ColorScheme colorScheme = theme.colorScheme;
    final l10n = context.l10n;
    final AppBreakpoint breakpoint = AppBreakpoints.of(context);
    final bool isLarge = breakpoint.index >= AppBreakpoint.lg.index;
    final double logoSize = isLarge ? 56 : 48;

    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 360, minHeight: 72),
        child: AppLogoLockup(
          mode: AppLogoLockupMode.full,
          logoSize: logoSize,
          wordmark: l10n.appShortTitle,
          slogan: l10n.appSlogan,
          wordmarkStyle: theme.textTheme.titleMedium?.copyWith(
            color: colorScheme.primary,
            fontWeight: FontWeight.w700,
            fontSize: isLarge ? 24 : 20,
            height: 1.1,
            letterSpacing: -0.2,
          ),
          sloganStyle: theme.textTheme.bodySmall?.copyWith(
            color: colorScheme.onSurfaceVariant,
            height: 1.25,
          ),
        ),
      ),
    );
  }
}
