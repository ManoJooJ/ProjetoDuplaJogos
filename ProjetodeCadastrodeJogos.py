def exibir_menu():
    print("1. Cadastrar Jogos")
    print("2. Exibir Lista")
    print("3. Mostrar quantidade de Jogos cadastrados")
    print("4. Sair do sistema")

def cadastrar(lista):
    nome_jogo = input("Digite um jogo para ser cadastrado: ")
    nota_jogo = input("Nota para o jogo (ex: 10/10): ")
    lista.append((nome_jogo, nota_jogo)) 
    print(f"O Jogo {nome_jogo} foi cadastrado com sucesso com a nota {nota_jogo}!")

def exibir_lista(lista):
    if len(lista) == 0:  
        print("Nenhum jogo cadastrado!")  
    else:
        print("Lista de Jogos:")
        for jogo, nota in lista:
            print(f"Jogo: {jogo} - Nota: {nota}")

def mostrar_quantidade(lista):
    print(f"A quantidade de jogos que foram cadastrados: {len(lista)}")

def main():
    lista_de_jogos = []
    nome_usuario = input("Por favor, insira seu nome: ")

    while True:
        print(f"\nSeja bem-vindo ao sistema de Cadastro de Jogos, {nome_usuario}!")
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar(lista_de_jogos)
        elif opcao == '2':
            exibir_lista(lista_de_jogos)
        elif opcao == '3':  
            mostrar_quantidade(lista_de_jogos)
        elif opcao == '4':  
            print("Saindo do sistema, por favor aguarde...")
            break
        else:
            print("Opção inválida! Por favor, selecione uma das opções acima.")

if __name__ == "__main__":
    main()
