import sqlite3

DB_PATH = "data/estoque.db"

def conectar():
    """Estabelece conexão com o banco de dados."""
    return sqlite3.connect(DB_PATH)
