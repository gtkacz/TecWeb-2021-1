from pathlib import Path
import json

def extract_route(string):
    return string.split()[1][1:]

def is_path(subject):
    if not type(subject) is Path:
        return Path(subject)
    else:
        return subject
        
def read_file(path):
    path=is_path(path)
    extension=path.suffix
    if extension == '.txt' or extension == '.html' or extension == '.css' or extension == '.js':
        with open(path, 'rt') as file:
            data=file.read()
        return data
    else:
        with open(path, 'rb') as file:
            data=file.read()
        return data
    
def has_directory(string, directory):
    c=0
    for i in string:
        if i == '/':
            c+=1
    if c>1:
        return string
    else:
        return Path('./{0}/{1}'.format(directory, string))

def load_data(path):
    path=has_directory(path, 'data')
    with open(path) as file: 
        data=json.load(file)
    return data

def load_template(name):
    path=has_directory(name, 'templates')
    return read_file(path)

def build_response(body='', code=200, reason='OK', headers=''):
    args = [str(code), reason]
    response = 'HTTP/1.1 ' + (' '.join(args))
    if headers == '':
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body
    return response.encode()