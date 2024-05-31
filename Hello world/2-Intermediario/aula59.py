import json

# pessoa = {
#     'nome': 'Lucas',
#     'sobrenome': 'Souza',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 10},
#         {'rua': 'R2', 'numero': 15},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (2, 7),
#     'dev': True,
#     'nada': None
# }

# with open('aula59.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

with open('aula59.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    print(pessoa['nome'])
