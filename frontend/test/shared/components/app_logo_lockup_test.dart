import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:fchip/app/theme/app_theme.dart';
import 'package:fchip/shared/components/app_logo_lockup.dart';

void main() {
  Future<void> pumpLockup(
    WidgetTester tester, {
    required AppLogoLockupMode mode,
    Size size = const Size(360, 120),
    String? slogan = 'Your health, our mission.',
  }) {
    return tester.pumpWidget(
      MaterialApp(
        theme: AppTheme.light,
        home: Scaffold(
          body: Center(
            child: SizedBox(
              width: size.width,
              height: size.height,
              child: AppLogoLockup(
                mode: mode,
                logoSize: 40,
                wordmark: 'FCHIP',
                slogan: slogan,
              ),
            ),
          ),
        ),
      ),
    );
  }

  testWidgets('full mode shows logo, FCHIP, and slogan under wordmark', (
    WidgetTester tester,
  ) async {
    await pumpLockup(tester, mode: AppLogoLockupMode.full);

    expect(find.text('FCHIP'), findsOneWidget);
    expect(find.text('Your health, our mission.'), findsOneWidget);
    expect(find.byType(Image), findsOneWidget);
  });

  testWidgets('wordmark mode hides slogan', (WidgetTester tester) async {
    await pumpLockup(tester, mode: AppLogoLockupMode.wordmark);

    expect(find.text('FCHIP'), findsOneWidget);
    expect(find.text('Your health, our mission.'), findsNothing);
  });

  testWidgets('mark mode is logo only', (WidgetTester tester) async {
    await pumpLockup(tester, mode: AppLogoLockupMode.mark);

    expect(find.text('FCHIP'), findsNothing);
    expect(find.text('Your health, our mission.'), findsNothing);
    expect(find.byType(Image), findsOneWidget);
  });

  test('auto mode resolves from available space', () {
    expect(
      AppLogoLockup.resolveMode(maxWidth: 40, maxHeight: 30),
      AppLogoLockupMode.mark,
    );
    expect(
      AppLogoLockup.resolveMode(maxWidth: 160, maxHeight: 48),
      AppLogoLockupMode.wordmark,
    );
    expect(
      AppLogoLockup.resolveMode(maxWidth: 280, maxHeight: 80),
      AppLogoLockupMode.full,
    );
  });
}
