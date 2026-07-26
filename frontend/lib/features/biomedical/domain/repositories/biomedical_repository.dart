import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/biomedical/domain/entities/biomedical_entities.dart';

abstract interface class BiomedicalRepository {
  Future<Result<BiomedicalWorkbench>> getWorkspace(
    BiomedicalWorkspaceQuery query,
  );

  Future<Result<BiomedicalLookupData>> getLookups({String? search});

  Future<Result<BiomedicalMutationResult>> createFaultReport(
    Map<String, Object?> payload,
  );

  Future<Result<BiomedicalMutationResult>> createResource(
    String resource,
    Map<String, Object?> payload,
  );

  Future<Result<BiomedicalMutationResult>> updateResource(
    String resource,
    String id,
    Map<String, Object?> payload,
  );

  Future<Result<BiomedicalMutationResult>> startWorkOrder(
    String id,
    Map<String, Object?> payload,
  );

  Future<Result<BiomedicalMutationResult>> returnToService(
    String id,
    Map<String, Object?> payload,
  );
}
