with open('saida.txt', 'a') as saida:
    while True:
        nome = input()
        if nome == 'sair':
            break
        print(nome, file = saida)