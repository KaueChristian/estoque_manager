from db.conectar import conectar
from models.movimentacao import Movimentacao

def registrar_movimentacao(movimentacao: Movimentacao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO movimentacoes (produto_id, tipo, quantidade, data)
        VALUES (?, ?, ?, ?)
    """, (movimentacao.produto_id, movimentacao.tipo, movimentacao.quantidade, movimentacao.data))

    conexao.commit()
    conexao.close()

def carregar_movimentacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, produto_id, tipo, quantidade, data FROM movimentacoes")
    registros = cursor.fetchall()
    return [Movimentacao(id=r[0], produto_id=r[1], tipo=r[2], quantidade=r[3], data=r[4]) for r in registros]
