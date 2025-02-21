quadradros = [x**2 for x in range(20) if x % 3 != 0]

entrada = []
for i in range(20):
    if i % 3 != 0:
        entrada.append(i**2)