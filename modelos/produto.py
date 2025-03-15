class Estoque:
    
    produtos = []
    
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        Estoque.produtos.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._quantidade}'
    
    @classmethod
    def entrada_dadoss(cls, mensagem, tipo):
        pass
    
    @classmethod
    def cadastrar_produto(cls):
        
        while True:       
            try:
                nome_produto = input('Digite o nome do produto que deseja cadastrar: ')
                
                if not nome_produto:
                    raise ValueError('Erro: o campo não pode estar vazio!')
                
                if any(produto._nome == nome_produto for produto in cls.produtos):
                    print(f'O produto {nome_produto} já está cadastrado! Tente outro nome')
                else:
                    break
            except ValueError:
                print('Erro: digite um valor string válido para nome do produto')
        
        while True:     
            try:
                preco_produto = float(input('Digite o preço do produto: '))
                break
            except ValueError:
                print('Erro: digite um valor numério válido para preço')
                
        while True:       
            try:
                quantidade_produto = int(input('Digite a quantidade de produtos: '))
                break
            except ValueError:
                print('Erro: digite um valor numério válido para quantidade')
                
 
        novo_produto = cls(nome_produto, preco_produto, quantidade_produto)
        print('\nProduto cadastrado com sucesso!')
        return novo_produto
    
    @classmethod
    def listar_produtos(cls):
        
        if not cls.produtos:
            print('\nNão há produtos nos estoque')
            return
            
        print(f'{'Produto'.ljust(20)} | {'Preço'.ljust(20)} | {'Quantidade'.ljust(20)}')
        
        for produto in cls.produtos:
            print(f'{produto._nome.ljust(20)} | {str(produto._preco).ljust(20)} | {str(produto._quantidade).ljust(20)}')
    
    @classmethod
    def atualizar_produtos(cls):
        
        while True:
            try:
                nome_produto = input('Digite o nome do produto que deseja atualizar: ')
                
                if not nome_produto:
                    raise ValueError('Erro: o campo não pode estar vazio!')
                else:
                    break
            except ValueError:  
                print('Erro: digite um valor string válido para nome do produto')
                
        for produto in cls.produtos:
            if nome_produto == produto._nome:
                while True:
                    try:
                        novo_preco = float(input('Digite o novo preço do produto: '))
                        break
                    except ValueError:
                        print('Erro: digite um valor numério válido para preço')
                        
                while True:
                    try:
                        nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                        break
                    except ValueError:
                        print('Erro: digite um valor numério válido para quantidade')
                        
                produto._preco = novo_preco
                produto._quantidade = nova_quantidade 
                print('\nProduto atualizado')
                break
            else:
                print('Esse produto não existe')
                return
                
    @classmethod
    def remover_produto(cls):
        nome = input('Digite o nome do produto que deseja remover: ')
        
        for produto in cls.produtos:
            if nome == produto._nome:
                cls.produtos.remove(produto)
                print('Produto removido com sucesso!')
            else:
                print('Produto não encontrado')
                return
            
    @classmethod
    def valor_total_estoque(cls):
        
        if not cls.produtos:
            print('Não há produtos cadastrados para fazer a soma do estoque')
            return
                
        soma_total = sum(produto._preco * produto._quantidade for produto in cls.produtos)
        print(f'O valor total do estoque é de R${soma_total: .2f}')
