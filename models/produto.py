class Produto:
    def __init__(self, id=None, nome="", categoria="", quantidade=0, preco=0.0, validade=None):
        """
        Inicializa um objeto Produto.
        
        :param id: ID único do produto (gerado automaticamente pelo banco de dados).
        :param nome: Nome do produto.
        :param categoria: Categoria do produto.
        :param quantidade: Quantidade disponível no estoque.
        :param preco: Preço unitário do produto.
        :param validade: Data de validade do produto (formato ISO: YYYY-MM-DD).
        """
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.validade = validade
        
    def __str__(self):
        """Representação amigável de produto."""
        return f"{self.nome} - {self.categoria} - {self.quantidade} unidades - R$ {self.preco}"
        