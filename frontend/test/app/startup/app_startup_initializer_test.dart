import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:fchip/app/app.dart';
import 'package:fchip/app/startup/app_preferences_restorer.dart';
import 'package:fchip/app/startup/app_startup_initializer.dart';
import 'package:fchip/app/startup/startup_providers.dart';
import 'package:fchip/app/startup/startup_shell.dart';
import 'package:fchip/core/config/app_config.dart';
import 'package:fchip/core/security/session_controller.dart';
import 'package:fchip/core/storage/secure/app_secure_storage.dart';
import 'package:fchip/features/home/presentation/pages/home_page.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  group('AppStartupInitializer', () {
    setUp(() {
      SharedPreferences.setMockInitialValues(<String, Object>{});
      FlutterSecureStorage.setMockInitialValues(<String, String>{});
    });

    test('initializes dependencies and startup state', () async {
      SharedPreferences.setMockInitialValues(<String, Object>{
        AppPreferenceKeys.themeMode: 'dark',
        AppPreferenceKeys.locale: 'en',
      });

      final result = await const AppStartupInitializer().initialize(
        config: AppConfig.fromValues(
          environmentName: 'development',
          apiBaseUrl: 'http://localhost:8080',
        ),
      );

      expect(result.state.themeMode, ThemeMode.dark);
      expect(result.state.locale, const Locale('en'));
      expect(result.state.storageReadiness.isReady, isTrue);
      expect(result.state.sessionReadiness.isReady, isTrue);
      final container = result.createProviderContainer();
      addTearDown(container.dispose);

      expect(container.read(appStartupStateProvider), same(result.state));
      expect(
        container.read(sessionStateProvider),
        result.state.sessionReadiness,
      );
    });

    testWidgets('replaces loading shell with configured app scope', (
      WidgetTester tester,
    ) async {
      FlutterSecureStorage.setMockInitialValues(<String, String>{
        SecureStorageKeys.accessToken: 'test-access-token',
      });

      await tester.pumpWidget(const StartupLoadingApp());
      await tester.pump();

      final result = await const AppStartupInitializer().initialize(
        config: AppConfig.fromValues(
          environmentName: 'development',
          apiBaseUrl: 'http://localhost:8080',
        ),
      );

      await tester.pumpWidget(
        result.buildProviderScope(child: const FchipApp()),
      );
      await tester.pumpAndSettle();

      expect(find.byType(HomePage), findsOneWidget);
      expect(tester.takeException(), isNull);
    });
  });
}
