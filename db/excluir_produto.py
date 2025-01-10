import sqlite3
from db.conectar import conectar
from models.produto import Produto

def excluir_produto(produto_id: int):
    """
    Exclui um produto do banco de dados com base no ID fornecido.
    
    :param produto_id: ID do produto a ser excluído.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM produtos WHERE id = ?"

    try:
        cursor.execute(query, (produto_id,))
        if cursor.rowcount == 0:
            print("Produto não encontrado para exclusão")
        else:
            conexao.commit()
            print("Produto excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir o produto: {e}")
    finally:
        conexao.close()