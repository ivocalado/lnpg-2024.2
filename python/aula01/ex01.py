#ler arquivo a.txt e imprimir na tela

with open("meu_nome.txt", 'r') as arquivo:
    with open('destino.txt', 'a') as destino:
        nomes = arquivo.readlines()
        for nome in nomes:
            print(nome, file=destino)
