"""
enumerate - enumera iteráveis (índices)
"""
lista = ['baka', 'yamete', 'kudasai']

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# for i in enumerate(lista):
#     indice, nomes = i
#     print(indice, nomes)

for tuple in enumerate(lista):
    print('For da tuple:')
    for valor in tuple:
        print(f'\t{valor}')
