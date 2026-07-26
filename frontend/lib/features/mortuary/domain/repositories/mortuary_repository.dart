import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/mortuary/domain/entities/mortuary_entities.dart';

abstract interface class MortuaryRepository {
  Future<Result<MortuaryWorkspacePayload>> getWorkspace(
    MortuaryWorkspaceQuery query,
  );

  Future<Result<MortuaryLookupData>> getLookups({
    String? facilityId,
    String? search,
  });

  Future<Result<MortuaryWorkspaceItem>> getItem({
    required String resource,
    required String id,
    MortuaryWorkspaceQuery baseQuery = const MortuaryWorkspaceQuery(),
  });
}
