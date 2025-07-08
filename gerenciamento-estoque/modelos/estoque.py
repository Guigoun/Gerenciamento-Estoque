from modelos.produto import Produtos
from servicos.input import entrada_dados

class Estoque:
    def __init__(self):
        self.estoque = {}
    
    def cadastrar_produto(self): #Cadastro de novos produtos
        
        nome_produto = entrada_dados('Digite o nome do produto que deseja cadastrar: ', 'str', 'produto')   
         
        if nome_produto in self.estoque:
            print(f'O produto {nome_produto} já está cadastrado! Tente outro nome')
            return
        
        preco_produto = entrada_dados('Digite o preço do produto: ', 'float', 'preço')
        quantidade_produto = entrada_dados('Digite a quantidade de produtos: ', 'int', 'quantidade')
        
        
        produto = Produtos(nome_produto, preco_produto, quantidade_produto)
        self.estoque[nome_produto] = produto

        print('\nProduto cadastrado com sucesso!')
    
    def listar_produtos(self): #Lista os produtos em estoque
        
        if not self.estoque:
            print('\nNão há produtos nos estoque')
            return
            
        print(f"{'Produto'.ljust(20)} | {'Preço'.ljust(20)} | {'Quantidade'.ljust(20)}")
        
        for i,produto in enumerate(self.estoque.values(), start=1):
            print(f'{i}. {produto.nome.ljust(17)} | {str(produto.preco).ljust(20)} | {str(produto.quantidade).ljust(20)}')
    
    def atualizar_produtos(self): #Atualiza um produto do estoque
    
        nome_produto = entrada_dados('Digite o nome do produto que deseja atualizar: ', 'str', 'produto')

       
        if nome_produto not in self.estoque:
            print(f'\nO produto {nome_produto} não está cadastrado para ser atualizado')
            return
        
        novo_preco = entrada_dados('Digite o novo preço do produto: ', 'float', 'preço')
        nova_quantidade = entrada_dados('Digite a nova quantidade do produto: ', 'int', 'quantidade')
                
        produto = self.estoque[nome_produto]                 
        produto.preco = novo_preco
        produto.quantidade = nova_quantidade 
        print('\nProduto atualizado')
                      
    def remover_produto(self): #Remove um produto do estoque
        nome_produto = entrada_dados('Digite o nome do produto que deseja remover: ', 'str', 'produto')
        
        if nome_produto not in self.estoque:
            print(f'\nO produto {nome_produto} não foi encontrado no estoque')
            return
        
        del self.estoque[nome_produto]
        print('\nProduto removido com sucesso!')
            
    def valor_total_estoque(self): #Faz o calculo do valor total do estoque
        
        if not self.estoque:
            print('\nNão há produtos cadastrados para fazer a soma do estoque')
            return
                
        soma_total = sum(produto.preco * produto.quantidade for produto in self.estoque.values())
        print(f'O valor total do estoque é de R${soma_total: .2f}')
