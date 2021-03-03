from utils import load_data, load_template
from urllib.parse import unquote_plus
import json

def str_cleanup(request):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        anot=corpo.split('&')
        return unquote_plus(anot[-1]), unquote_plus(anot[-2])
    
def write_json(data, filename):
    path="./data/"+filename
    with open(path,'w') as f:
        data=(json.load(f)).append(data)
        json.dump(data, f, ensure_ascii=False, indent=4) 

def index(request):
    if request.startswith('GET'):
        # Cria uma lista de <li>'s para cada anotação
        # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        note_template = load_template('components/note.html')
        notes_li = [
            note_template.format(title=dados['titulo'], details=dados['detalhes'])
            for dados in load_data('notes.json')
        ]
        notes = '\n'.join(notes_li)
        return load_template('index.html').format(notes=notes).encode()
    
    elif request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            key=append(chave_valor.split('=')[0])
            value=append(chave_valor.split('=')[1])
            params[key]=value
            