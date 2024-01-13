import os

restaurantes = [ 
    {'nome':'Praça', 'Categoria':'Japonesa','Ativo':False},
    {'nome':'Pizza Suprema','Categoria':'Italiana','Ativo':True},
    {'nome':'Mexican Food','Categoria':'Mexicana','Ativo':False} 
     ]

def exibir_nome_do_programa():
    '''Essa função é responsável por mostrar o nome de app de um forma mais personalizada'''

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    '''Essa função é responsável por mostrar o menu de opções ao usuário'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair')

def opcao_invalida():
    '''Essa função é responsável apontar que o usuário digitou uma opção inválida e retorna ao menu principal'''

    print('Opção inválida! \n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adicona um novo restaurante a lista de restaurantes
  
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    # Pegando dados do restaurante 
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restaurante} : ')

    # Inserindo em um dicionário
    dados_restaurante = {'nome':nome_do_restaurante, 'Categoria':categoria, 'Ativo': False}

    # Adicionando a lista de restaurantes 
    restaurantes.append(dados_restaurante)
    
    #Adicionando conteudo a nossa lista
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi adicionado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes, com nome, categoria e estado se ativo ou desativado'''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'

        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função é responsável por dar escolha navegavel ao menu'''
    try:
        # Agora pediremos um input, lembrando que ele deve ser inteiro
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()        
        else:
            opcao_invalida()
    except:
        print('Opção inválida, provávelmente você digitou uma letra ao invés de número')

def alterar_estado_restaurante():
    '''Essa função é responsável por alterar o estado restaurante, se ativo, desativa, se desativado, ativa'''

    exibir_subtitulo('Alterando estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    '''Essa função é responsável por fechar o app'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Essa função é responsável por retornar ao menu principal'''

    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por limpar a tela e exibir o subtitulo da opção selecionado'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


#método que chama todos outros métodos
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

#condição que verifica se estamos na main, se estiver chama método main()
if __name__ == '__main__':
    main()