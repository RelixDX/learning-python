# Ímpar ou par

def impar_ou_par(x):
    if x % 2 == 0:
        return print(f'{x} é par')
    else:
        return print(f'{x} é ímpar')


numero = int(input('Digite um número: '))

impar_ou_par(numero)
