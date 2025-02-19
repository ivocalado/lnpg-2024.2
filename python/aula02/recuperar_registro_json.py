import json

with open("pessoa.json", "r") as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa["nome"])
    print(pessoa["idade"])
    print(pessoa["cidade"])
    print(pessoa["estado"])
    print(pessoa["nacionalidade"])