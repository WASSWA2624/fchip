import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/core/errors/app_failure.dart';
import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/discharge/data/repositories/discharge_repository_impl.dart';
import 'package:fchip/features/discharge/domain/entities/discharge_entities.dart';
import 'package:fchip/features/discharge/presentation/widgets/discharge_planning_dialog.dart';
import 'package:fchip/l10n/app_localizations.dart';
import 'package:fchip/l10n/app_localizations_x.dart';
import 'package:fchip/shared/clinical_actions/clinical_disposition_actions.dart';
import 'package:fchip/shared/components/components.dart';

/// Opens the shared system-validated discharge planning dialog.
Future<bool?> showDischargePlanningDialog({
  required BuildContext context,
  required WidgetRef ref,
  required String admissionId,
  Widget? title,
  DischargeAdmissionDetail? initialDetail,
  void Function(AppFailure failure)? onFailure,
}) async {
  final String normalizedAdmissionId = admissionId.trim();
  if (normalizedAdmissionId.isEmpty) {
    return null;
  }

  DischargeAdmissionDetail? detail = initialDetail;
  if (detail == null) {
    final Result<DischargeAdmissionDetail> result = await ref
        .read(dischargeRepositoryProvider)
        .getAdmissionDetail(normalizedAdmissionId);
    final AppFailure? failure = result.when(
      success: (_) => null,
      failure: (AppFailure value) => value,
    );
    if (failure != null) {
      onFailure?.call(failure);
      return null;
    }
    detail = result.when(
      success: (DischargeAdmissionDetail value) => value,
      failure: (_) => null,
    );
  }

  if (detail == null || !context.mounted) {
    return null;
  }

  final AppLocalizations l10n = context.l10n;
  final Widget resolvedTitle =
      title ??
      Text(
        clinicalDispositionActionLabel(
          l10n,
          sourceQueue: 'IPD',
          status: detail.summary.admissionStatus,
          stage: detail.summary.stage,
          location: detail.summary.location,
          hasAdmission: true,
        ),
      );

  return showAppDialog<bool>(
    context: context,
    barrierDismissible: false,
    builder: (_) => DischargePlanningDialog(
      admissionId: normalizedAdmissionId,
      title: resolvedTitle,
      initialDetail: detail,
    ),
  );
}
