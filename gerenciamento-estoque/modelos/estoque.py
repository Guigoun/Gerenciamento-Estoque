from modelos.produto import Produtos
from servicos.input import entrada_dados

class Estoque:
    def __init__(self):
        self.estoque = {}
        self.proximo_id = 1
        
    def cadastrar_produto(self): #Cadastro de novos produtos
        
        nome_produto = entrada_dados('Digite o nome do produto que deseja cadastrar: ', 'str', 'produto')   
       
        if any(produto.nome == nome_produto for produto in self.estoque.values()):
            print(f"\nO Produto {nome_produto} já está cadastrado!")
            return
                
        preco_produto = entrada_dados('Digite o preço do produto: ', 'float', 'preço')
        quantidade_produto = entrada_dados('Digite a quantidade de produtos: ', 'int', 'quantidade')
        
        produto = Produtos(self.proximo_id, nome_produto, preco_produto, quantidade_produto)
        self.estoque[self.proximo_id] = produto
        self.proximo_id += 1

        print('\nProduto cadastrado com sucesso!')
    
    def listar_produtos(self): #Lista os produtos em estoque
        
        if not self.estoque:
            print('\nNão há produtos nos estoque')
            return
            
        print(f"{'ID'.ljust(20)} | {'Produto'.ljust(20)} | {'Preço'.ljust(20)} | {'Quantidade'.ljust(20)}")
        
        for produto in self.estoque.values():
            print(f'{str(produto.id).ljust(20)} | {produto.nome.ljust(20)} | {str(produto.preco).ljust(20)} | {str(produto.quantidade).ljust(20)}')

    def atualizar_produtos(self): #Atualiza um produto do estoque
    
        id_produto = entrada_dados('Digite o ID do produto que deseja atualizar: ', 'int', 'ID do Produto')

       
        if id_produto not in self.estoque:
            print(f'\nO produto não está cadastrado para ser atualizado')
            return
        
        nome_produto = entrada_dados('Digite o nome do produto: ', 'str', 'produto')
        novo_preco = entrada_dados('Digite o novo preço do produto: ', 'float', 'preço')
        nova_quantidade = entrada_dados('Digite a nova quantidade do produto: ', 'int', 'quantidade')
                
        produto = self.estoque[id_produto]
        produto.produto = nome_produto                 
        produto.preco = novo_preco
        produto.quantidade = nova_quantidade 
        print('\nProduto atualizado')
                      
    def remover_produto(self): #Remove um produto do estoque
        id_produto = entrada_dados('Digite o ID do produto que deseja remover: ', 'int', 'ID do Produto')
        
        if id_produto not in self.estoque:
            print(f'\nO produto não foi encontrado no estoque')
            return
        
        del self.estoque[id_produto]
        print('\nProduto removido com sucesso!')
            
    def valor_total_estoque(self): #Faz o calculo do valor total do estoque
        
        if not self.estoque:
            print('\nNão há produtos cadastrados para fazer a soma do estoque')
            return
                
        soma_total = sum(produto.preco * produto.quantidade for produto in self.estoque.values())
        print(f'O valor total do estoque é de R${soma_total: .2f}')
