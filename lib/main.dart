import 'dart:convert';
import 'dart:io';

import 'package:args/args.dart';

void main(List<String> arguments) {
  ArgParser initParser() {
    final ArgParser parser = ArgParser();
    parser.addOption('projectPath', abbr: 'p', help: 'Specify the project path');
    return parser;
  }

  ArgParser createFeatureParser() {
    final ArgParser parser = ArgParser();
    parser.addOption('featureName', abbr: 'n', help: 'Specify the feature name');
    return parser;
  }

  ArgParser argParser = ArgParser()
    ..addCommand('init', initParser())
    ..addCommand('create-feature', createFeatureParser());

  final ArgResults argResults = argParser.parse(arguments);

  print(argResults);

  if (argResults.command?.name == 'init') {
    final String? projectPath = argResults.command!['projectPath'];

    if (projectPath != null) {
      initProject(projectPath);
      // have to fix it
      isInitialized = true;
    } else {
      print('Error: Please provide a project path.');
    }
  } else if (argResults.command?.name == 'create-feature') {
    if (isInitialized) {
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
}

void initProject(String projectPath) {
  // Store the projectPath in config.json
  final Map<String, dynamic> configData = {'projectPath': projectPath};
  final File configFile = File('${projectPath}/config.json');

  try {
    configFile.writeAsStringSync(jsonEncode(configData));
    print('${projectPath}/config.json created successfully.');
    editJsonFile({"projectPath": projectPath, "features": []}, 'config.json', projectPath);
    print('config.json file updated successfully.');
    print('Project initialized at: $projectPath');
  } catch (e) {
    print('Error creating the config.json file: $e');
  }
}

void createFeature(String featureName) {
  final String featurePath = 'features/$featureName';

  try {
    Directory(featurePath).createSync(recursive: true);
    print('Feature "$featureName" created successfully at: $featurePath');
  } catch (e) {
    print('Error creating the feature folder: $e');
  }
}

void editJsonFile(Map<String, dynamic> datas, String fileName, String path) {
  final File configFile = File('${path}/$fileName');
  try {
    configFile.writeAsStringSync(jsonEncode(datas));
  } catch (e) {
    print('Error creating the config.json file: $e');
  }
}

bool isInitialized() {
  final File configFile = File('config.json');
  String configData = configFile.readAsStringSync();
  Map<String, dynamic> configJson = jsonDecode(configData);
  bool projectPath = configJson['projectPath'] != null || configJson['projectPath'] != '';
  return configFile.existsSync() && projectPath;
}
