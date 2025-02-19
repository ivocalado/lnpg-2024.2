def menu() -> int:
    print("Agenda")
    print("1 - Adicionar pessoa")
    print("2 - Recuperar pessoa por CPF")
    print("3 - Deletar pessoa por CPF")
    print("4 - Sair")
    return int(input("Escolha uma opção: "))

def adicionar_pessoa():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    #salva em arquivo a pessoa adicionada
    with open("pessoas.txt", "a") as arquivo:
        print(f'{nome}#{endereco}#{cpf}', file=arquivo)

def imprimir_pessoa_cpf():
    cpf = input("CPF: ")
    with open("pessoas.txt", 'r') as arquivo:
        for linha in arquivo:
            nome, endereco, cpf_arquivo = linha.strip().split("#")
            if cpf == cpf_arquivo:
                print(f"Nome: {nome}")
                print(f"Endereço: {endereco}")
                print(f"CPF: {cpf}")
                break
        else:
            print("Pessoa não encontrada")

def deletar_pessoa_cpf():
    # 1. Ler o cpf a ser deletado
    cpf = input("CPF: ")

    # 2. Ler arquivo para memoria
    with open("pessoas.txt", 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # 3. Criar novo arquivo zerado        
    with open("pessoas.txt", 'w') as arquivo:
        for linha in linhas:
            nome, endereco, cpf_arquivo = linha.strip().split("#")
            # 4. Escrever todas as linhas que não tem o cpf informado no novo arquivo
            if cpf != cpf_arquivo:                
                print(f'{nome}#{endereco}#{cpf_arquivo}', file=arquivo)
    print("Pessoa deletada")

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