import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fchip/app/startup/app_startup_state.dart';
import 'package:fchip/core/security/session_controller.dart';
import 'package:fchip/core/security/session_state.dart';
import 'package:fchip/core/storage/storage_readiness.dart';

final appStartupStateProvider = Provider<AppStartupState>((ref) {
  return const AppStartupState.defaults();
});

final storageReadinessProvider = Provider<StorageReadiness>((ref) {
  return ref.watch(
    appStartupStateProvider.select((state) => state.storageReadiness),
  );
});

final sessionReadinessProvider = Provider<SessionState>((ref) {
  return ref.watch(sessionStateProvider);
});
