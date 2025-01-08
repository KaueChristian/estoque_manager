import sqlite3

# Caminho para o banco de dados
DB_PATH = "data/estoque.db"

def conectar():
    return sqlite3.connect(DB_PATH)
    
def criar_tabelas():
    """Cria as tabelas no banco de dados se não existirem."""
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Tabela de produtos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL.
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        validade DATE
    )
    """)
    
    # Tabela de movimentação
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER NOT NULL,
        tipo TEXT CHECK('entrada, 'saida')) NOT NULL
        quantidade INTEGER NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (produto_id) REFERENCES produtos (id)
    )
    """)
    
    conexao.commit()
    conexao.commit()


if __name__ == "__main__":
    try:
        criar_tabelas()
        print("Banco de Dados ")
        
    except sqlite3.Error as e:
        print(f'Erro ao criar tabelas: {e}')
    except Exception as e:
        print(f"Erro inesperado: {e}")