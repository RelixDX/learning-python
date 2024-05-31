# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(lista1, lista2):
#     # Encontra o comprimento da menor lista
#     tamanho_menor = min(len(lista1), len(lista2))

#     # Usa a função zip para combinar as duas listas até o tamanho da menor lista
#     resultado = list(zip(lista1[:tamanho_menor], lista2[:tamanho_menor]))

#     return resultado

from itertools import zip_longest

# Exemplo de uso
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

# resultado = zipper(lista1, lista2)
# print(resultado)
print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2, fillvalue='SEM CIDADE')))
