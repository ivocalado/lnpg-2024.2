import random

def filtro_menor_que_25(numero):
    return numero <= 25

entrada = []

for i in range(100):
    entrada.append(random.randint(1, 100))

saida = list(filter(filtro_menor_que_25, entrada))

print(saida)