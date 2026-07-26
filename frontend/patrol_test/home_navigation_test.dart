import 'package:fchip/app/router/app_routes.dart';
import 'package:fchip/features/home/presentation/pages/home_page.dart';

import 'helpers/demo_credentials.dart';
import 'helpers/failure_reporter.dart';
import 'helpers/patrol_harness.dart';

void main() {
  patrolTestWithDiagnostics(
    'home loads for authenticated tenant admin',
    ($) async {
      await pumpPatrolE2eApp($);
      await loginAs($, DemoAccount.tenantAdmin);

      expect(find.byType(HomePage), findsOneWidget);
      expect(
        find.text('Welcome to FairBanks Community Health Information Platform.'),
        findsOneWidget,
      );
    },
    targetFile: 'patrol_test/home_navigation_test.dart',
  );

  patrolTestWithDiagnostics(
    'sidebar navigation opens settings',
    ($) async {
      await pumpPatrolE2eApp($);
      await loginAs($, DemoAccount.tenantAdmin);
      final l10n = patrolL10n($);

      await $.tester.tap(find.text(l10n.navigationSettingsLabel));
      await $.pumpAndSettle();

      expect(find.text(l10n.navigationSettingsLabel), findsWidgets);
    },
    targetFile: 'patrol_test/home_navigation_test.dart',
  );

  patrolTestWithDiagnostics(
    'direct route navigation reaches settings shell',
    ($) async {
      await loginAndOpenRoute($, DemoAccount.tenantAdmin, AppRoutes.settings.path);
      final l10n = patrolL10n($);

      expect(find.text(l10n.navigationSettingsLabel), findsWidgets);
    },
    targetFile: 'patrol_test/home_navigation_test.dart',
  );
}
