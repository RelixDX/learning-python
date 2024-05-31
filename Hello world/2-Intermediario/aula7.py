# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função que fala se um número é ímpar ou par.
# Retorne se o número é par ou ímpar.

def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


variavel = multi(3, 5, 2)
print(variavel)

# if variavel % 2 == 0:
#     print('Par')
# else:
#     print('Ímpar')


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'


print(par_impar(4))
print(par_impar(2))
print(par_impar(3))
print(par_impar(6))
