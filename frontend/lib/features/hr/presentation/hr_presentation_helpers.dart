import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/core/errors/app_failure.dart';
import 'package:fchip/core/permissions/access_policy.dart';
import 'package:fchip/core/permissions/access_requirement.dart';
import 'package:fchip/core/permissions/app_permission.dart';
import 'package:fchip/features/hr/domain/entities/hr_entities.dart';
import 'package:fchip/features/hr/presentation/controllers/hr_workspace_controller.dart';
import 'package:fchip/features/hr/presentation/hr_reference_localizations.dart';
import 'package:fchip/l10n/app_localizations.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/components/components.dart';

const AccessRequirement hrWriteRequirement = AccessRequirement(
  allPermissions: <AppPermission>[AppPermissions.hrWrite],
  activeModules: <String>['hr-rosters'],
);

const AccessRequirement hrRosterWriteRequirement = AccessRequirement(
  anyPermissions: <AppPermission>[
    AppPermissions.hrWrite,
    AppPermissions.rosterWrite,
  ],
  activeModules: <String>['hr-rosters'],
);

const AccessRequirement hrRosterApproveRequirement = AccessRequirement(
  anyPermissions: <AppPermission>[
    AppPermissions.hrWrite,
    AppPermissions.rosterApprove,
  ],
  activeModules: <String>['hr-rosters'],
);

const AccessRequirement hrRosterPublishRequirement = AccessRequirement(
  anyPermissions: <AppPermission>[
    AppPermissions.hrWrite,
    AppPermissions.rosterPublish,
  ],
  activeModules: <String>['hr-rosters'],
);

const AccessRequirement hrPayrollRequirement = AccessRequirement(
  allPermissions: <AppPermission>[AppPermissions.hrWrite],
  anyPermissions: <AppPermission>[AppPermissions.financialApprove],
  activeModules: <String>['hr-rosters'],
);

/// Reads the current HR workspace state when the controller has loaded successfully.
HrWorkspaceState? readHrWorkspaceState(WidgetRef ref) {
  return ref
      .read(hrWorkspaceControllerProvider)
      .asData
      ?.value
      .when(success: (HrWorkspaceState state) => state, failure: (_) => null);
}

List<AppSelectOption<String>> hrSelectOptions(List<HrOption> options) {
  return <AppSelectOption<String>>[
    for (final HrOption option in options)
      AppSelectOption<String>(value: option.value, label: option.label),
  ];
}

List<AppSelectOption<String>> hrLocalizedSelectOptions(
  AppLocalizations l10n,
  List<HrOption> options,
) {
  return <AppSelectOption<String>>[
    for (final HrOption option in options)
      AppSelectOption<String>(
        value: option.value,
        label: l10n.hrLocalizedOptionLabel(option),
      ),
  ];
}

void showHrMutationSnackBar(BuildContext context, AppFailure? failure) {
  if (!context.mounted) {
    return;
  }
  final AppLocalizations l10n = context.l10n;
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Text(
        failure == null ? l10n.hrSavedMessage : l10n.failureMessage(failure),
      ),
    ),
  );
}
