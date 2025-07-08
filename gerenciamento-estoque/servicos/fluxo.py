from modelos.estoque import Estoque
import os

estoque_produtos = Estoque()


def exibir_opcoes(): #Exibe as opções que devem ser selecionadas
    print('1. Cadastrar produto\n2. Listar produtos\n3. Atualizar Produto\n4. Remover produto\n5. Valor Total\n6. Sair\n')

def voltar_menu_principal(): #Volta para o menu principal
    input('\nDigite qualquer tecla para voltar ao menu princial: ')
    os.system('cls')
    main()
     
def finalizar_programa(): #Encerra o programa
    os.system('cls')
    print('Finalizando programa')

def escolher_opcao(): #Função para escolher um opção

    try:
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            estoque_produtos.cadastrar_produto()
            voltar_menu_principal()
        elif opcao == 2:
            estoque_produtos.listar_produtos()
            voltar_menu_principal()
        elif opcao == 3:
            estoque_produtos.atualizar_produtos()
            voltar_menu_principal()
        elif opcao == 4:
            estoque_produtos.remover_produto()
            voltar_menu_principal()
        elif opcao == 5:
            estoque_produtos.valor_total_estoque()
            voltar_menu_principal()
        elif opcao == 6:
            finalizar_programa()
        else:
            print('Opção inválida!')
            voltar_menu_principal()
    except:
        print('Opção inválida!')
        voltar_menu_principal()
        
def main(): #Ordem que deve ser executado
    exibir_opcoes()
    escolher_opcao()