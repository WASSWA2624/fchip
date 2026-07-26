import 'package:dio/dio.dart';
import 'package:fchip/core/network/api_client.dart';
import 'package:fchip/core/network/api_endpoints.dart';
import 'package:fchip/core/network/api_result.dart';
import 'package:fchip/features/example/data/dtos/example_resource_dto.dart';

abstract interface class ExampleResourceRemoteDataSource {
  Future<ApiResult<ExampleResourceDto>> fetchById(
    String id, {
    CancelToken? cancelToken,
  });
}

final class DioExampleResourceRemoteDataSource
    implements ExampleResourceRemoteDataSource {
  const DioExampleResourceRemoteDataSource({required ApiClient apiClient})
    : _apiClient = apiClient;

  final ApiClient _apiClient;

  @override
  Future<ApiResult<ExampleResourceDto>> fetchById(
    String id, {
    CancelToken? cancelToken,
  }) {
    return _apiClient.get<ExampleResourceDto>(
      ApiEndpoints.byId(HmsApiResource.public, id),
      decoder: ExampleResourceDto.fromResponseData,
      cancelToken: cancelToken,
    );
  }
}
