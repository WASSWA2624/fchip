import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/core/config/app_config.dart';

final appConfigProvider = Provider<AppConfig>((ref) {
  const String environmentName = String.fromEnvironment('APP_ENV');
  if (environmentName.isEmpty) {
    return AppConfig.fromValues(
      environmentName: 'development',
      apiBaseUrl: 'http://localhost:3000',
      logLevelName: 'error',
    );
  }

  return AppConfig.fromEnvironment();
});
