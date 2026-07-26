import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/discharge/domain/entities/discharge_entities.dart';
import 'package:fchip/features/ipd/domain/entities/ipd_entities.dart';
import 'package:fchip/shared/data/data.dart';

abstract interface class DischargeRepository {
  Future<Result<AppPage<IpdAdmissionSummary>>> listQueue(
    DischargeWorklistQuery query,
  );

  Future<Result<DischargeAdmissionDetail>> getAdmissionDetail(
    String admissionId,
  );

  Future<Result<DischargeReferenceData>> loadReferenceData();

  Future<Result<void>> planDischarge(
    String admissionId,
    Map<String, Object?> payload,
  );

  Future<Result<void>> finalizeDischarge(
    String admissionId,
    Map<String, Object?> payload,
  );

  Future<Result<void>> updateDischargeClearance(
    String admissionId,
    Map<String, Object?> payload,
  );

  Future<Result<void>> createFinalInvoice(Map<String, Object?> payload);

  Future<Result<void>> createPharmacyOrder(Map<String, Object?> payload);
}
