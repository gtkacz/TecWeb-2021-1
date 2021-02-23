from pathlib import Path

def extract_route(string):
    string=string.split()[1][1:]
    return string

def read_file(path):
    extension=path.suffix
    if extension == '.txt' or extension == '.html' or extension == '.css' or extension == '.js':
        with open(path, 't') as file:
            return file.read()
    else:
        with open(path, 'rb') as file:
            return file.read()
