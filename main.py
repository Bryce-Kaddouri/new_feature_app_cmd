import argparse
import re
import os

import os

def create_item(path, is_folder=True, content=None):
    try:
        if is_folder:
            os.makedirs(path)
            print(f"Folder creating: {path}")
            print(f"Folder created: {path}")
        else:
            with open(path, 'w') as file:
                if content:
                    file.write(content)
                    print(f"File created with content: {path}")
                else:
                    print(f"Empty file created: {path}")
    except OSError as e:
        print(f"Error creating {'' if is_folder else 'file '}{path}: {e}")

''' def to check if file or folder exists '''
def check_exists(path):
    return os.path.exists(path)






def camel_to_snake(word):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', word).lower()

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

def snakeToCamelLower(word):
    return word[0].lower() + snakeToCamel(word)[1:]




parser = argparse.ArgumentParser(description='Process some integers.')

subparsers = parser.add_subparsers(dest='command', help='Subcommands')

# Create command
create_parser = subparsers.add_parser('create-feature', help='Create a new feature')


# Init command
init_parser = subparsers.add_parser('init', help='Initialize a new project')
init_parser.add_argument('--path', dest='path', required=True, help='Path for initializing the project')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed arguments
print(args)


def main():
     while True:
        print('''
        1. Create a new feature
        2. Initialize a new project
        3. Exit
        ''')
        choice = input('Enter your choice [1-3]: ')
        if choice == '1':
            print('Creating a new feature...')
            name = input('Enter the name of the feature (use the same format: FeatureName) : ')
            print('name: ', name)
            snake_name = camel_to_snake(name)
            lower_camel_name = snake_to_camel(snake_name)
            path = 'lib/src/features/' + snake_name
            lst = path.split('/')
            print(lst)
            for i in range(1, len(lst)):
                if not check_exists('/'.join(lst[:i])):
                    create_item('/'.join(lst[:i]))
            create_item(path, is_folder=True)
            create_item(path + '/presentation', is_folder=True)
            ''' provider '''
            create_item(path + '/presentation/provider', is_folder=True)
            create_item(path + '/presentation/provider/' + snake_name + '.dart', is_folder=False, content='''
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class ''' + name + '''Provider with ChangeNotifier {
    ''' + name + '''Provider();
}
''')

            create_item(path + '/presentation/screen', is_folder=True)
            create_item(path + '/presentation/screen/' + snake_name + '_screen.dart', is_folder=False, content='''
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
class ''' + name + '''Screen extends StatelessWidget {
    const ''' + name + '''Screen({Key? key}) : super(key: key);

    @override
    Widget build(BuildContext context) {
        return Placeholder();
    }
}
''')

            create_item(path + '/presentation/widget', is_folder=True)

            create_item(path + '/data', is_folder=True)
            create_item(path + '/data/datasource', is_folder=True)
            create_item(path + '/data/datasource/' + snake_name + '_datasource.dart', is_folder=False, content='''
import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ''' + name + '''DataSource {
    final SharedPreferences? sharedPreferences;
    final DioClient? dioClient;
    const ''' + name + '''DataSource({required this.sharedPreferences, required this.dioClient});
}
''')

            create_item(path + '/data/model', is_folder=True)
            create_item(path + '/data/model/' + snake_name + '_model.dart', is_folder=False, content='''
class ''' + name + '''Model {
    int? id;
    ''' + name + '''Model({this.id});

    ''' + name + '''Model.fromJson(Map<String, dynamic> json){
        id = json['id'];
    }

    Map<String, dynamic> toJson() {
        final Map<String, dynamic> data = <String, dynamic>{};
        data['id'] = id;
        return data;
    }
}
''')

            create_item(path + '/data/repository', is_folder=True)

            create_item(path + '/business', is_folder=True)
            create_item(path + '/business/param', is_folder=True)

            create_item(path + '/business/repository', is_folder=True)


            create_item(path + '/business/usecase', is_folder=True)
            create_method_isDone = False
            content_repo_abstract = '''abstract class ''' + name + '''Repository {'''
            content_repo_impl = '''
import '../../business/repository/''' + snake_name + '''_repository.dart';
import '../datasource/''' + snake_name + '''_datasource.dart';

class ''' + name + '''RepositoryImpl implements ''' + name + '''Repository {
    final ''' + name + '''DataSource ''' + '''dataSource;
    const ''' + name + '''RepositoryImpl({required this.dataSource});
'''

            while not create_method_isDone:
                want_method = input('Do you want to create a new method in repository? (y/n): ')

                if want_method == 'y':
                    method_name = input('Enter the name of the method (nameOfMethod): ')
                    content_repo_abstract += '''
    Future<void> ''' + method_name + '''();'''
                    content_repo_impl += '''
    @override
    Future<void> ''' + method_name + '''() async {
    }'''
                else:
                    create_method_isDone = True

            content_repo_abstract += '''
}
'''
            content_repo_impl += '''
}
'''
            create_item(path + '/data/repository/' + snake_name + '_repository_impl.dart', is_folder=False, content=content_repo_impl)
            create_item(path + '/business/repository/' + snake_name + '_repository.dart', is_folder=False, content=content_repo_abstract)


            print('Feature created successfully')


        elif choice == '2':
            print('Initializing a new project...')
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please choose again.')

if __name__ == "__main__":
    main()





"""
# Driver code
str = "GeeksForGeeks"
print(change_case(str)) """
