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
    def entrada_dados(cls, mensagem, tipo, mensagem_de_erro):
        while True:
            try:
                valor = input(mensagem)
                
                if not valor:
                    raise ValueError('Erro: o campo não pode estar vazio!')
                
                if tipo == 'float':
                    return float(valor)
                elif tipo == 'int':
                    return int(valor)
                else:
                    return valor
                
            except ValueError:
                print(f'Erro: digite um valor válido para {mensagem_de_erro}')
    
    
    @classmethod
    def cadastrar_produto(cls):
        
        nome_produto = cls.entrada_dados('Digite o nome do produto que deseja cadastrar: ', 'str', 'produto')   
         
        if any(produto._nome == nome_produto for produto in cls.produtos):
            print(f'O produto {nome_produto} já está cadastrado! Tente outro nome')
            return
        
        preco_produto = cls.entrada_dados('Digite o preço do produto: ', 'float', 'preço')
        quantidade_produto = cls.entrada_dados('Digite a quantidade de produtos: ', 'int', 'quantidade')
        
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
    
        nome_produto = cls.entrada_dados('Digite o nome do produto que deseja atualizar: ', 'str', 'produto')

        if not any(produto._nome == nome_produto for produto in cls.produtos):
            print(f'\nO produto {nome_produto} não está cadastrado para ser atualizado')
                    
        for produto in cls.produtos:
            if nome_produto == produto._nome:
                novo_preco = cls.entrada_dados('Digite o novo preço do produto: ', 'float', 'preço')
                nova_quantidade = cls.entrada_dados('Digite a nova quantidade do produto: ', 'int', 'quantidade')
                                
                produto._preco = novo_preco
                produto._quantidade = nova_quantidade 
                print('\nProduto atualizado')
                      
                
    @classmethod
    def remover_produto(cls):
        nome_produto = cls.entrada_dados('Digite o nome do produto que deseja remover: ', 'str', 'produto')
        
        if not any(produto._nome == nome_produto for produto in cls.produtos):
            print(f'\nO produto {nome_produto} não foi encontrado no estoque')
        
        for produto in cls.produtos:
            if nome_produto == produto._nome:
                cls.produtos.remove(produto)
                print('\nProduto removido com sucesso!')
            
            
    @classmethod
    def valor_total_estoque(cls):
        
        if not cls.produtos:
            print('\nNão há produtos cadastrados para fazer a soma do estoque')
            return
                
        soma_total = sum(produto._preco * produto._quantidade for produto in cls.produtos)
        print(f'O valor total do estoque é de R${soma_total: .2f}')
