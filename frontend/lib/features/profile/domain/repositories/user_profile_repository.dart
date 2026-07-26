import 'package:fchip/core/errors/result.dart';
import 'package:fchip/core/security/auth_session.dart';
import 'package:fchip/features/profile/domain/entities/user_profile_entities.dart';

abstract interface class UserProfileRepository {
  Future<Result<UserProfileView>> loadCurrentProfile(AuthSession session);

  Future<Result<UserProfileRecord>> updateProfile(
    String profileId,
    UserProfileDraft draft,
  );
}
