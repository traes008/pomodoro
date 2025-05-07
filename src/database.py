import os

def check_if_file_exists(file_path):
    return os.path.exists(file_path)

def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line)

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

