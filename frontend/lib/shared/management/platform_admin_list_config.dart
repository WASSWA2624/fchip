import 'package:fchip/shared/data/app_pagination.dart';

/// Shared list settings for Super Admin platform management dialogs.
abstract final class PlatformAdminListConfig {
  static const int pageSize = 25;

  static const AppPageRequest initialPageRequest = AppPageRequest(
    pageSize: pageSize,
  );
}
