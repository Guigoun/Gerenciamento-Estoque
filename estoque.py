import os

produtos = []

def exibir_opcoes(): #Exibe as opções que devem ser selecionadas
    print('1. Cadastrar produto\n2. Listar produtos\n3. Atualizar Produto\n4. Remover produto\n5. Valor Total\n6. Sair\n')

def voltar_menu_principal(): #Volta para o menu principal
    input('\nDigite qualquer tecla para voltar ao menu princial: ')
    os.system('cls')
    main()

def finalizar_programa(): #Encerra o programa
    os.system('cls')
    print('Finalizando programa')

def cadastrar_produto(): #Cadastra novos produtos
    
    while True: 
        nome_produto = input('Digite o nome do produto que deseja cadastrar: ')
        
        if any(produto['nome'] == nome_produto for produto in produtos):
            print(f'O produto {nome_produto} já está cadastrado! Tente outro nome.')
        else:
            break
                 
    while True:
        try:      
            preco_produto = float(input('Digite o preço do produto: '))
            break
        except ValueError:
            print('Erro: ditie um valor número válido para preço')
    
    while True:
        try:
            quantidade_produto = int(input('Digite a quantidade de produtos: '))
            break
        except ValueError:
            print('Erro: ditie um valor número válido para quantidade')
            
    dados_produto = {'nome': nome_produto, 'preço': preco_produto, 'quantidade': quantidade_produto}
    produtos.append(dados_produto)
    print('\nProduto cadastrado com sucesso')
        
    voltar_menu_principal()
    
def listar_produtos(): #Lista os produtos no estoque
    
    if not produtos:
            print('Não há produtos no estoque')
            voltar_menu_principal()           
    
    for produto in produtos:
        print(f'{produto['nome']} - {produto['preço']:.2f} - {produto['quantidade']}')
             
    voltar_menu_principal()
  
def atualizar_produto(): #Atualiza o produto desejado
    nome_produto = input('Digite o nome do produto que deseja atualizar: ') 
    
    for produto in produtos:
        if nome_produto == produto['nome']:   
            while True:
                try:
                    novo_preco = float(input('Digite o novo valor do produto: '))
                    break
                except ValueError:
                    print('Erro: ditie um valor número válido para preço')
                    
            while True:
                try:
                    nova_quantidade = int(input('Digite a nova quantidade: '))
                    break  
                except ValueError:
                    print('Erro: ditie um valor número válido para quantidade')

            produto['preço'] = novo_preco
            produto['quantidade'] = nova_quantidade
            print('\nProduto atualizado!')
            break   
        else:
            print('Produto não encontrado')
    
    
    voltar_menu_principal()

def remover_produto(): #Remove um produto do estoque
    nome_produto = input('Digite o nome do produto que deseja remover: ')

    for produto in produtos:
        if nome_produto == produto['nome']:
            produtos.remove(produto)
            print('\nProduto removido')
            break
        else:
            print('Produto não encontrado')
    
    voltar_menu_principal()

def valor_total(): #Exibe o valor total do estoque
    soma_total = sum(produto['preço'] * produto['quantidade'] for produto in produtos)
    print(f'\nO valor total do estoque é de R$ {soma_total:.2f}')

    voltar_menu_principal()
    
def escolher_opcao(): #Função para escolher um opção
    
    try:
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            remover_produto()
        elif opcao == 5:
            valor_total()
        elif opcao == 6:
            finalizar_programa()
        else:
            print('Opção inválida!')
            voltar_menu_principal()
    except:
        print('Opção inválida!')
        voltar_menu_principal()
            
def main(): #Função principal a ser executada
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__": #Linha do principal executável
    main()