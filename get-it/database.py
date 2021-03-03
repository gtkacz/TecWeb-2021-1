import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, DB_NAME):
        if not DB_NAME.endswith('.db'):
            self.DB_NAME=DB_NAME + '.db'
        else:
            self.DB_NAME=DB_NAME
            
        self.conn=sqlite3.connect(self.DB_NAME)
        "CREATE TABLE IF NOT EXISTS dados_pessoais (nome_da_rua TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE, identificador INTEGER PRIMARY KEY);"
        "INSERT INTO dados_pessoais (nome_da_rua,cpf) VALUES ('R. Quatá','123.456.789-00');"
        self.conn.execute()
        self.conn.commit()
        
    def add(self, note):
        self.id=note.id
        self.title=note.title
        self.content=note.content
        
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
