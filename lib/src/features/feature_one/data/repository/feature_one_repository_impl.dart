
import '../../business/repository/feature_one_repository.dart';
import '../datasource/feature_one_datasource.dart';

class FeatureOneRepositoryImpl implements FeatureOneRepository {
    final FeatureOneDataSource dataSource;
    const FeatureOneRepositoryImpl({required this.dataSource});

    @override
    Future<void> methodOne() async {
    }
    @override
    Future<void> methodTwo() async {
    }
}
