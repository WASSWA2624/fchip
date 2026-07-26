import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/settings/domain/entities/settings_workspace_entities.dart';

abstract interface class SettingsWorkspaceRepository {
  Future<Result<SettingsWorkspace>> getWorkspace(SettingsWorkspaceQuery query);

  Future<Result<SettingsReferenceData>> getReferenceData(
    SettingsWorkspaceQuery query,
  );
}
