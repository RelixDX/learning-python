# Calculator project

class Calculator:
    def plus(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        return x / y

    print('Digite: [p] soma; [s] menos; [m] multiplicar; [d] dividir')
    calculator_open = input('Digite qual operação quer fazer: ')

    if calculator_open == 'p':
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        print(plus(soma1, soma2))
    if calculator_open == 's':
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        print(minus(soma1, soma2))
    if calculator_open == 'm':
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        print(multiplication(soma1, soma2))
    if calculator_open == 'd':
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
        print(division(soma1, soma2))


Calculator()
