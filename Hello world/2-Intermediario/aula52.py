# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]


def mudar_preco(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}


# novos_produtos = map(
#     mudar_preco,
#     produtos
# )

# Filter -----------------------------------

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
