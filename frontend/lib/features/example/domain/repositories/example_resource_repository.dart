import 'package:fchip/core/errors/result.dart';
import 'package:fchip/features/example/domain/entities/example_resource.dart';

abstract interface class ExampleResourceRepository {
  Future<Result<ExampleResource>> fetchById(String id);
}
