
import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';

class FeatureOneDataSource {
    final SharedPreferences? sharedPreferences;
    final DioClient? dioClient;
    const FeatureOneDataSource({required this.sharedPreferences, required this.dioClient});
}
