pessoas = [{
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "estado": "SP",
    "nacionalidade": "brasileiro"
},{
    "nome": "Maria",
    "idade": 30,
    "cidade": "Rio de Janeiro",
    "estado": "RJ",
    "nacionalidade": "brasileira"

}]

import json
with open("pessoa.json", "w") as arquivo:
    json.dump(pessoas, arquivo)