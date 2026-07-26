import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:fchip/core/permissions/access_requirement.dart';
import 'package:fchip/core/security/session_controller.dart';
import 'package:fchip/core/security/session_state.dart';
import 'package:fchip/features/pharmacy/data/repositories/pharmacy_repository_impl.dart';
import 'package:fchip/features/pharmacy/domain/entities/pharmacy_entities.dart';
import 'package:fchip/features/pharmacy/domain/repositories/pharmacy_repository.dart';
import 'package:fchip/features/pharmacy/presentation/widgets/pharmacy_storage_panel.dart';
import 'package:fchip/l10n/app_localizations.dart';
import 'package:fchip/shared/data/data.dart';
import 'package:mocktail/mocktail.dart';

class _MockPharmacyRepository extends Mock implements PharmacyRepository {}

const AccessRequirement _writeRequirement = AccessRequirement();

PharmacyWorkspaceState _stateWithRooms() {
  const PharmacyStorageLayout layout = PharmacyStorageLayout(
    rooms: <PharmacyStorageRoom>[
      PharmacyStorageRoom(
        id: 'room-1',
        name: 'Main store',
        code: 'MAIN',
        shelves: <PharmacyStorageShelf>[
          PharmacyStorageShelf(
            id: 'shelf-1',
            shelfCode: 'A1',
            label: 'Aisle A',
          ),
        ],
      ),
      PharmacyStorageRoom(id: 'room-2', name: 'Cold room', code: 'COLD'),
    ],
  );
  return const PharmacyWorkspaceState(
    query: PharmacyWorkbenchQuery(),
    workbench: PharmacyWorkbench(
      summary: PharmacyWorkbenchSummary(),
      orders: AppPage<PharmacyOrder>(
        items: <PharmacyOrder>[],
        request: AppPageRequest(),
      ),
    ),
    drugQuery: PharmacyDrugQuery(),
    drugs: AppPage<PharmacyDrug>(
      items: <PharmacyDrug>[],
      request: AppPageRequest(),
    ),
    formularyQuery: PharmacyFormularyQuery(),
    formularyItems: AppPage<PharmacyFormularyItem>(
      items: <PharmacyFormularyItem>[],
      request: AppPageRequest(),
    ),
    inventoryQuery: PharmacyInventoryStockQuery(),
    inventoryWorkbench: PharmacyInventoryWorkbench(
      summary: PharmacyInventoryStockSummary(),
      stocks: AppPage<PharmacyInventoryStock>(
        items: <PharmacyInventoryStock>[],
        request: AppPageRequest(),
      ),
    ),
    storageLayout: layout,
  );
}

Future<void> _pump(WidgetTester tester, _MockPharmacyRepository repository) {
  return tester.pumpWidget(
    ProviderScope(
      overrides: [
        pharmacyRepositoryProvider.overrideWithValue(repository),
        initialSessionStateProvider.overrideWithValue(
          const SessionState.ready(),
        ),
      ],
      child: MaterialApp(
        localizationsDelegates: AppLocalizations.localizationsDelegates,
        supportedLocales: AppLocalizations.supportedLocales,
        home: Scaffold(
          body: SizedBox(
            height: 260,
            child: PharmacyStoragePanel(
              state: _stateWithRooms(),
              writeRequirement: _writeRequirement,
              showHeaderActions: false,
              compact: true,
            ),
          ),
        ),
      ),
    ),
  );
}

void main() {
  late _MockPharmacyRepository repository;

  setUp(() {
    repository = _MockPharmacyRepository();
  });

  testWidgets(
    'compact storage panel scrolls without overflow in a constrained height',
    (WidgetTester tester) async {
      tester.view.physicalSize = const Size(400, 300);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);

      await _pump(tester, repository);
      await tester.pumpAndSettle();

      expect(find.text('Main store'), findsOneWidget);
      expect(find.text('Cold room'), findsOneWidget);
      expect(tester.takeException(), isNull);
    },
  );
}
