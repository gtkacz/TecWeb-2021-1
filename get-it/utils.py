from pathlib import Path

def extract_route(string):
    string=string.split()[1][1:]
    return string

def read_file(path):
    extension=path.suffix
    if extension == '.txt' or extension == '.html' or extension == '.css' or extension == '.js':
        file=open(path, "t")
        return str(file)
    else:
        file=open(path, "rb")
        return bytes(file)
