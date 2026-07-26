import 'package:flutter_test/flutter_test.dart';
import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/app/router/route_status_pages.dart';
import 'package:fchip/core/security/session_state.dart';
import 'package:fchip/features/auth/presentation/pages/login_page.dart';
import 'package:integration_test/integration_test.dart';

import '../test/helpers/test_harness.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('unauthenticated users are redirected to login', (
    WidgetTester tester,
  ) async {
    await pumpFchipApp(
      tester,
      overrides: testReadyAppOverrides(
        initialLocation: AppRoutes.patients.path,
      ),
    );
    await tester.pumpAndSettle();

    expect(find.byType(LoginPage), findsOneWidget);
    expect(find.text('Sign in'), findsWidgets);
  });

  testWidgets('login page renders for unauthenticated startup', (
    WidgetTester tester,
  ) async {
    await pumpFchipApp(
      tester,
      overrides: testReadyAppOverrides(initialLocation: AppRoutes.login.path),
    );
    await tester.pumpAndSettle();

    expect(find.byType(LoginPage), findsOneWidget);
    expect(
      find.text('Use your facility account to open the FCHIP workspace.'),
      findsOneWidget,
    );
  });

  testWidgets('session restore shell renders while session is unknown', (
    WidgetTester tester,
  ) async {
    await pumpFchipApp(
      tester,
      overrides: testReadyAppOverrides(
        sessionState: const SessionState.notReady(),
        initialLocation: AppRoutes.home.path,
      ),
    );
    await tester.pumpAndSettle();

    expect(find.byType(SessionRestoringPage), findsOneWidget);
    expect(find.text('Checking session'), findsOneWidget);
  });
}
