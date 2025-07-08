class Produtos:
    
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def __str__(self):
        return f'{self.nome} | {self.preco} | {self.quantidade}'
    