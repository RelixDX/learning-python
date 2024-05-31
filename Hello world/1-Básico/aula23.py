# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4
#  L u c a s
# -5-4-3-2-1

# nome = 'Lucas'
# print(nome[2])
# print(nome[-3])

# print('c' in nome)
# print('e' in nome)
# print(10 * '-')
# print('c' not in nome)
# print('e' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você busca: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')