from pathlib import Path
import json

def extract_route(string):
    return string.split()[1][1:]

def read_file(path):
    if not type(path) is Path:
        path=Path(path)
    extension=path.suffix
    if extension == '.txt' or extension == '.html' or extension == '.css' or extension == '.js':
        with open(path, 'rt') as file:
            data=file.read()
        return data
    else:
        with open(path, 'rb') as file:
            data=file.read()
        return data

def load_data(path):
    path='./data/'+path
    with open(path) as file: 
        data=json.load(file)
    return data

def load_template(name):
    path=Path('./templates/'+name)
    return read_file(path)