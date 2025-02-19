import json
def menu() -> int:
    print("Agenda")
    print("1 - Adicionar pessoa")
    print("2 - Recuperar pessoa por CPF")
    print("3 - Deletar pessoa por CPF")
    print("4 - Sair")
    return int(input("Escolha uma opção: "))

def ler_pessoas():
    try:
        with open("pessoas.json", 'r') as arquivo:
            pessoas = json.load(arquivo)
            return pessoas
    except FileNotFoundError:
        return []

def adicionar_pessoa():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    #salva em arquivo a pessoa adicionada
    pessoas = ler_pessoas()
    pessoas.append({"nome": nome, "endereco": endereco, "cpf": cpf})
    with open("pessoas.json", "w") as arquivo:
        json.dump(pessoas, arquivo)

def imprimir_pessoa_cpf():
    cpf = input("CPF: ")
    pessoas = ler_pessoas()
    for pessoa in pessoas:
        if cpf == pessoa["cpf"]:
            print(f"Nome: {pessoa['nome']}")
            print(f"Endereço: {pessoa['endereco']}")
            print(f"CPF: {pessoa['cpf']}")
            break
    else:
        print("Pessoa não encontrada")

def deletar_pessoa_cpf():
    # 1. Ler o cpf a ser deletado
    cpf = input("CPF: ")
    pessoas = ler_pessoas()
    # 2. Criar novo arquivo zerado
    pessoas_novo = []
    for pessoa in pessoas:
        if cpf != pessoa["cpf"]:
            pessoas_novo.append(pessoa)
    with open("pessoas.json", 'w') as arquivo:
        json.dump(pessoas_novo, arquivo)

if __name__ == "__main__":
    while True:
        opcao = menu()

        if opcao == 1:
            adicionar_pessoa()
        elif opcao == 2:
            imprimir_pessoa_cpf()
        elif opcao == 3:
            deletar_pessoa_cpf()
        elif opcao == 4:
            break
        else:
            print("Opção inválida")
    print("Fim do programa")