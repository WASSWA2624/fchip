import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/components/app_button.dart';
import 'package:fchip/shared/components/app_dialog.dart';

/// Fault reporting previously depended on the biomedical HIS workspace.
/// In FCHIP that module is removed, so this dialog explains the gap.
Future<void> showAppGlobalFaultReportDialog({
  required BuildContext context,
  required WidgetRef ref,
  VoidCallback? onCompleted,
}) async {
  await showAppDialog<void>(
    context: context,
    builder: (BuildContext dialogContext) {
      final l10n = dialogContext.l10n;
      return AppDialog(
        title: Text(l10n.workspaceGlobalFaultReportAction),
        content: const Text(
          'Equipment fault reporting is not available in this FCHIP build.',
        ),
        actions: <Widget>[
          AppButton.secondary(
            label: l10n.commonCloseActionLabel,
            onPressed: () => Navigator.of(dialogContext).pop(),
          ),
        ],
      );
    },
  );
}
