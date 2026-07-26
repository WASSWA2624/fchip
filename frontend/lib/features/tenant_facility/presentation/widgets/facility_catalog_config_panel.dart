import 'package:flutter/material.dart';
import 'package:fchip/app/theme/app_theme_extensions.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/components/app_content_panel.dart';

/// Placeholder for facility clinical catalog configuration.
///
/// Hospital HIS catalog packs were removed from FCHIP; this panel keeps the
/// tenant/facility setup desk section compilable until a CHIS catalog lands.
class FacilityCatalogConfigPanel extends StatelessWidget {
  const FacilityCatalogConfigPanel({
    this.facilityId,
    this.tenantId,
    this.defaultCurrency,
    this.enabled = true,
    super.key,
  });

  final String? facilityId;
  final String? tenantId;
  final String? defaultCurrency;
  final bool enabled;

  @override
  Widget build(BuildContext context) {
    final ThemeData theme = Theme.of(context);
    final l10n = context.l10n;

    return AppSectionPanel(
      title: l10n.tenantFacilityCatalogConfigureAction,
      children: <Widget>[
        Text(
          'Clinical catalog configuration is not part of this FCHIP build yet.',
          style: theme.textTheme.bodyMedium?.copyWith(
            color: theme.colorScheme.onSurfaceVariant,
          ),
        ),
        if (!enabled) ...<Widget>[
          SizedBox(height: theme.spacing.sm),
          Text(
            'You do not have permission to change facility catalogs.',
            style: theme.textTheme.bodySmall,
          ),
        ],
      ],
    );
  }
}
