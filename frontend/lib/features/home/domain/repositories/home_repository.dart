import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/home/domain/entities/home_dashboard.dart';
import 'package:fchip/features/home/domain/entities/home_dashboard_lookups.dart';

abstract interface class HomeRepository {
  Future<Result<HomeDashboard>> loadDashboard(HomeDashboardRequest request);

  Future<Result<HomeDashboardLookups>> loadLookups(
    HomeDashboardRequest request,
  );
}
