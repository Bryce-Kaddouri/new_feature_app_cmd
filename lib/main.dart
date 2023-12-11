import 'dart:convert';
import 'dart:io';

import 'package:args/args.dart';
String test= 'test';
void main(List<String> arguments) {
  ArgParser initParser() {
    final ArgParser parser = ArgParser();
    parser.addOption('projectPath',
        abbr: 'p', help: 'Specify the project path');
    return parser;
  }

  ArgParser createFeatureParser() {
    final ArgParser parser = ArgParser();
    parser.addOption('featureName',
        abbr: 'n', help: 'Specify the feature name');
    return parser;
  }

  ArgParser argParser = ArgParser()
    ..addCommand('init', initParser())
    ..addCommand('create-feature', createFeatureParser());

  final ArgResults argResults = argParser.parse(arguments);

  if (argResults.command?.name == 'init') {
    final String? projectPath = argResults.command!['projectPath'];

    if (projectPath != null) {
      initProject(projectPath);
    } else {
      print('Error: Please provide a project path.');
    }
  } else if (argResults.command?.name == 'create-feature') {
    if (isInitialized()) {
      final String? featureName = argResults.command!['featureName'];

      if (featureName != null) {
        createFeature(featureName);
      } else {
        print('Error: Please provide a feature name.');
      }
    } else {
      print('Error: Project not initialized. Use "init" command first.');
    }
  } else {
    print('Invalid command. Use "init" or "create-feature".');
  }
  print(test);
}

void initProject(String projectPath) {

  // Store the projectPath in config.json
  final Map<String, dynamic> configData = {'projectPath': projectPath};
  final File configFile = File('config.json');


  try {
    configFile.writeAsStringSync(jsonEncode(configData));
    print('config.json created successfully.');

    RegExp regExp = RegExp(r'^\/[a-zA-Z0-9_]+(?:\/[a-zA-Z0-9_]+)*\/');
    if (!regExp.hasMatch(projectPath)) {
      print('Error: Invalid project path.');
      print('Please provide a valid path (/path/to/project).');
      return;
    }else{

      editJsonFile({"projectPath": projectPath}, 'config.json');
      print('config.json file updated successfully.');
      print('Project initialized at: $projectPath');
      test = '${projectPath}config.json';
    }


  } catch (e) {
    print('Error creating the config.json file: $e');
  }
}

void createFeature(String featureName) {
  print('Creating feature "$featureName"...');
  print('test $test');
  final String featurePath = 'features/$featureName';

  try {
/*
    Directory(featurePath).createSync(recursive: true);
*/
    print('Feature "$featureName" created successfully at: $featurePath');
  } catch (e) {
    print('Error creating the feature folder: $e');
  }
}

void editJsonFile(Map<String, dynamic> datas, String fileName) async{
  final File configFile = File('$fileName');
  try {
    // get the current content of the file
    bool isDone = false;
    String configData = await configFile.readAsString().then((value) {
      isDone = true;
      print('value $value');

      return value;
    });
    while (!isDone) {
      await Future.delayed(Duration(seconds: 1)).then((value) {
        print('isDone $isDone');
      });

    }
    Map<String, dynamic> configJson = jsonDecode(configData);
    List<String> allProjectPath = configJson['projectPath'];
    print('allProjectPath $allProjectPath');
    allProjectPath.add(datas['projectPath']);
    configJson.addAll(datas);
    configFile.writeAsStringSync(jsonEncode({
      'projectPath': allProjectPath,
    }));
  } catch (e) {
    print('Error creating the config.json file: $e');
  }
}

bool isInitialized() {
  print('test $test');
  final File configFile = File('config.json');
  String configData = configFile.readAsStringSync();
  Map<String, dynamic> configJson = jsonDecode(configData);
  bool projectPath =
      configJson['projectPath'] != null || configJson['projectPath'] != '';
  return configFile.existsSync() && projectPath;
}



