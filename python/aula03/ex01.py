import random

entrada = []

for i in range(100):
    entrada.append(random.randint(1, 100))

saida = []
for posicao in entrada:
    if posicao <= 25:
        saida.append(posicao)

print(saida)