def exibir_menu():
    print("1. Cadastrar Jogos")
    print("2. Exibir jogos cadastrados")
    print("3. Sair do sistema")

def cadastrar(lista):
    item = input("Digite um jogo para ser cadastrado: ")
    lista.append(item)
    print("O Jogo foi cadastrado com sucesso!")

def exibir_lista(lista):
    print("Lista de Jogos:")
    for item in lista:
        print(item)

def main():
    lista_de_dados = []
    nome_usuario = input("Por favor, insira seu nome: ")  

    while True:

        print(f"\nSeja bem-vindo ao sistema de Cadastro de Jogos, {nome_usuario}!")
        exibir_menu()
        opcao = input("Escolha uma das opção: ")

        if opcao == '1':
            cadastrar(lista_de_dados)
        elif opcao == '2':
            exibir_lista(lista_de_dados)
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Porfavor, selecione uma das opções acima.")

if __name__ == "__main__":
    main()