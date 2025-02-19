def menu():
    print("Agenda")
    print("1 - Adicionar pessoa")
    print("2 - Listar pessoas")
    print("3 - Sair")
    return int(input("Escolha uma opção: "))

while True:
    print("Iniciando o programa")
    opcao = menu()
    if opcao == 1:
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        cpf = input("CPF: ")
        #salva em arquivo a pessoa adicionada
        with open("pessoas.txt", "a") as arquivo:
            print(f'{nome}#{endereco}#{cpf}', file=arquivo)
    elif opcao == 2:
        #arbra o arquivo e atribua a uma lista
        with open("pessoas.txt", 'r') as arquivo:
            pessoas = arquivo.read()

            for pessoa in pessoas.split('\n')[: -1]:
                dados = pessoa.split('#')
                print('Nome:', dados[0])
                print('Endereço:', dados[1])
                print('CPF:', dados[2])
    elif opcao == 3:
        break
    else:
        print("Opção inválida")
