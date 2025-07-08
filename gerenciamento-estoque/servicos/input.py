def entrada_dados(mensagem, tipo, mensagem_de_erro): #Função genérica de entrada de dados e tratamento
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
