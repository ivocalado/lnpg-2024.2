import random

entrada = []

for i in range(100):
    entrada.append(random.randint(1, 100))


saida = list(filter(lambda numero: numero <= 25, entrada))

print(saida)