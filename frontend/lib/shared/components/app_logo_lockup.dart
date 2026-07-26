import 'package:fchip/app/theme/app_theme_extensions.dart';
import 'package:fchip/shared/components/app_logo.dart';
import 'package:flutter/material.dart';

/// Space-aware brand lockup: logo left · FCHIP right · slogan under FCHIP.
///
/// Matches `app-ui/00-shared/components/01-brand/01-logo-lockup` and
/// `app-ui/branding.py` modes:
/// - [AppLogoLockupMode.full] — logo + wordmark + slogan
/// - [AppLogoLockupMode.wordmark] — logo + wordmark
/// - [AppLogoLockupMode.mark] — logo only
/// - [AppLogoLockupMode.auto] — pick from available width/height
enum AppLogoLockupMode { full, wordmark, mark, auto }

class AppLogoLockup extends StatelessWidget {
  const AppLogoLockup({
    required this.wordmark,
    this.slogan,
    this.mode = AppLogoLockupMode.auto,
    this.logoSize = 40,
    this.assetPath,
    this.wordmarkStyle,
    this.sloganStyle,
    this.gap,
    this.semanticLabel,
    super.key,
  });

  /// Localized product short name (e.g. FCHIP).
  final String wordmark;

  /// Localized slogan shown under [wordmark] in full mode.
  final String? slogan;

  final AppLogoLockupMode mode;
  final double logoSize;
  final String? assetPath;
  final TextStyle? wordmarkStyle;
  final TextStyle? sloganStyle;
  final double? gap;
  final String? semanticLabel;

  static AppLogoLockupMode resolveMode({
    required double maxWidth,
    required double maxHeight,
    AppLogoLockupMode mode = AppLogoLockupMode.auto,
  }) {
    if (mode != AppLogoLockupMode.auto) {
      return mode;
    }
    if (maxHeight < 36 || maxWidth < 48) {
      return AppLogoLockupMode.mark;
    }
    if (maxHeight < 54 || maxWidth < 168) {
      return AppLogoLockupMode.wordmark;
    }
    return AppLogoLockupMode.full;
  }

  @override
  Widget build(BuildContext context) {
    final ThemeData theme = Theme.of(context);
    final ColorScheme colorScheme = theme.colorScheme;
    final double resolvedGap = gap ?? theme.spacing.sm;

    return LayoutBuilder(
      builder: (BuildContext context, BoxConstraints constraints) {
        final double maxW = constraints.maxWidth.isFinite
            ? constraints.maxWidth
            : 480;
        final double maxH = constraints.maxHeight.isFinite
            ? constraints.maxHeight
            : logoSize * 2;
        final AppLogoLockupMode used = resolveMode(
          maxWidth: maxW,
          maxHeight: maxH,
          mode: mode,
        );

        final String label =
            semanticLabel ??
            (used == AppLogoLockupMode.mark
                ? wordmark
                : used == AppLogoLockupMode.full &&
                      slogan != null &&
                      slogan!.trim().isNotEmpty
                ? '$wordmark. $slogan'
                : wordmark);

        final Widget mark = AppLogo(
          size: logoSize,
          assetPath: assetPath ?? 'assets/logos/logo.png',
        );

        if (used == AppLogoLockupMode.mark) {
          return Semantics(label: label, child: mark);
        }

        final TextStyle titleStyle =
            wordmarkStyle ??
            theme.textTheme.titleMedium?.copyWith(
              color: colorScheme.primary,
              fontWeight: FontWeight.w700,
              height: 1.1,
              letterSpacing: -0.2,
            ) ??
            TextStyle(
              color: colorScheme.primary,
              fontWeight: FontWeight.w700,
              fontSize: logoSize >= 48 ? 22 : 16,
              height: 1.1,
            );

        final TextStyle subtitleStyle =
            sloganStyle ??
            theme.textTheme.bodySmall?.copyWith(
              color: colorScheme.onSurfaceVariant,
              height: 1.2,
            ) ??
            TextStyle(
              color: colorScheme.onSurfaceVariant,
              fontSize: 12,
              height: 1.2,
            );

        final bool showSlogan =
            used == AppLogoLockupMode.full &&
            slogan != null &&
            slogan!.trim().isNotEmpty;

        return Semantics(
          label: label,
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              mark,
              SizedBox(width: resolvedGap),
              Flexible(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text(
                      wordmark,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: titleStyle,
                    ),
                    if (showSlogan) ...<Widget>[
                      const SizedBox(height: 2),
                      Text(
                        slogan!,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: subtitleStyle,
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
