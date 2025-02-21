import random

entrada = []

for i in range(100):
    entrada.append(random.randint(1, 100))

filtro_menor_que_25 = lambda numero: numero <= 25

saida = list(filter(filtro_menor_que_25, entrada))

print(saida)