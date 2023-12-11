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
            path = 'lib/src/features/' + snake_name
            lst = path.split('/')
            print(lst)
            for i in range(1, len(lst)):
                if not check_exists('/'.join(lst[:i])):
                    create_item('/'.join(lst[:i]))
            """ create_item(path, is_folder=False, content='''import 'package:flutter/material.dart';''')
            print('Feature created successfully') """


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
