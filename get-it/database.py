import sqlite3
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
    
def DB_PATH(DB_NAME):
    try:
        DB_NAME=str(DB_NAME)
        if not DB_NAME.endswith('.db'):
            return Path(DB_NAME + '.db')
        else:
            return Path(DB_NAME)
    except:
        raise ValueError("Did not enter a valid file name.")

class Database:
    def __init__(self, DB_NAME):
        self.DB_NAME=DB_PATH(DB_NAME)
        self.conn=sqlite3.connect(self.DB_NAME)
        self.action="CREATE TABLE IF NOT EXISTS dados_pessoais (nome_da_rua TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE, identificador INTEGER PRIMARY KEY);"
        self.conn.execute(self.action)
        self.conn.commit()
        
    def add(self, note):
        self.notation = f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(self.notation)
        self.conn.commit()

    def get_all(self,):
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.note_list = []
        for linha in self.cursor:
            note_obj = Note(linha[0], linha[1], linha[2])
            self.note_list.append(note_obj)
        return self.note_list

    def update(self, entry):
        string_edition = f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id};"
        self.cursor = self.conn.execute(string_edition)
        self.conn.commit()

    def delete(self, note_id):
        delete_command = f"DELETE FROM note WHERE id = {note_id};"
        self.cursor = self.conn.execute(delete_command)
        self.conn.commit()