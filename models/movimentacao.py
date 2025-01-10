class Movimentacao:
    def __init__(self, id=None, produto_id=None, tipo="", quantidade=0, data=None):
        """
        Inicializa um objeto Movimentacao.
        
        :param id: ID único da movimentação (gerado automaticamente pelo banco de dados).
        :param produto_id: ID do produto relacionado à movimentação.
        :param tipo: Tipo de movimentação ('entrada' ou 'saida').
        :param quantidade: Quantidade movimentada.
        :param data: Data e hora da movimentação (formato ISO: YYYY-MM-DD HH:MM:SS).
        """
        self.id = id
        self.produto_id = produto_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data
    
    def __str__(self):
        """Representação amigável da movimentação"""
        return f"{self.tipo.capitalize()} de {self.quantidade} unidades (Produto ID: {self.produto_id})"

        