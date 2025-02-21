# Crie um programa que dada uma lista de 10 valores randomicos
# calcula a soma dos valores positivos


entrada = [10, -80, 14, 4, -9, -1, 0, 5, 7, -2]

soma = sum(filter(lambda numero: numero > 0, entrada))

