#Crie um programa que dada uma lista de 10 elemetos randomicos
#gere uma segunda lista com seu quadrado

import random

entrada = []

for i in range(10):
    entrada.append(random.randint(1, 100))

saida = list(map(lambda numero: numero ** 2, entrada))
print(entrada)
print(saida)