import sqlite3
from db.conectar import conectar
from models.produto import Produto

def atualizar_produto(produto: Produto):
    """
    Atualiza os dados de um produto no banco de dados.
    
    :param produto: Objeto Produto contendo os novos valores e o ID do produto a ser atualizado.
    """
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    UPDATE produtos SET nome = ?, categoria = ?, quantidade = ?, preco = ?, validade = ? WHERE id = ?
    """
    
    valores = (produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.validade, produto.id)
    try:
        cursor.execute(query, valores)
        if cursor.rowcount == 0:
            print("Produto não encontrado para atualização.")
        else:
            conexao.commit()
            print("Produto atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o produto: {e}")
    finally:
        conexao.close()
        