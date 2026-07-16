import sqlite3


CAMINHO_BANCO = "app/data/bagconnect.db"


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            CAMINHO_BANCO
        )

        self.cursor = self.connection.cursor()


    def criar_tabelas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            cpf TEXT UNIQUE,
            passageiro_id INTEGER,
            FOREIGN KEY (passageiro_id)
            REFERENCES passageiros(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passageiros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bagagens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL,
            passageiro_id INTEGER NOT NULL,
            FOREIGN KEY (passageiro_id)
            REFERENCES passageiros(id)
        )
        """)

        self.connection.commit()


    def fechar(self):

        self.connection.close()