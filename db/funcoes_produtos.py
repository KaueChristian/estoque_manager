from db.conectar import conectar
from models.produto import Produto

def salvar_produto(produto: Produto):
    conexao = conectar()
    cursor = conexao.cursor()
    
    if produto.id is None:
        cursor.execute("""
            INSERT INTO produtos (nome, categoria, quantidade, preco, validade)
            VALUES (?, ?, ?, ?, ?)
        """, (produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.validade))
    else:
        cursor.execute("""
            UPDATE produtos
            SET nome = ?, categoria = ?, quantidade = ?, preco = ?, validade = ?
            WHERE id = ?
        """, (produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.validade, produto.id))
        
    conexao.commit()
    conexao.close()
    
def carregar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome, categoria, quantidade, preco, validade FROM produtos")
    registros = cursor.fetchall()
    
    return [Produto(id=r[0], nome=r[1], categoria=r[2], quantidade=r[3], preco=r[4], validade=r[5]) for r in registros]
