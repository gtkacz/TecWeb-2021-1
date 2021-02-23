from pathlib import Path

def extract_route(string):
    string=string.split()[1][1:]
    return string

def read_file(path):
    ext=path.suffix
    if ext == '.txt' or ext == '.html' or ext == '.css' or ext == '.js':
        file=open(str(path), "t")
        return str(file)
    else:
        file=open(str(path), "b")
        return bytes(file)