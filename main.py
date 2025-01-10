from db.criar_tabelas import criar_tabelas
from db.funcoes_produtos import salvar_produto, carregar_produtos
from db.atualizar_produto import atualizar_produto
from db.excluir_produto import excluir_produto
from models.produto import Produto

def main():
    # Listar produtos
    produtos = carregar_produtos()
    print("\nProdutos cadastrados:")
    for p in produtos:
        print(p)
        
    produto_novo = Produto(id=2, nome="Mouse gamer", categoria="eletrônico", quantidade="28", preco=245.56, validade=None)
    atualizar_produto(produto_novo)
    
    produtos = carregar_produtos()
    print("\nProdutos cadastrados:")
    for p in produtos:
        print(p)

if __name__ == "__main__":
    main()