# Calculadora

while True:
    math = input('Digite o operador(Ex.: (+ - / *) ["s" para sair]): ')
    math = math.lower()

    while math == '+':
        num1 = input('Digite o número que vai somar: ')
        num2 = input('Digite o número que vai somar: ')
        num1_f = float(num1)
        num2_f = float(num2)

        print(f'A soma de {num1_f} + {num2_f} = {num1_f + num2_f}')
        break

    while math == '-':
        num1 = input('Digite o número que vai subtrair: ')
        num2 = input('Digite o número que vai subtrair: ')
        num1_f = float(num1)
        num2_f = float(num2)

        print(f'A subtração de {num1_f} - {num2_f} = {num1_f - num2_f}')
        break

    while math == '*':
        num1 = input('Digite o número que vai multiplicar: ')
        num2 = input('Digite o número que vai multiplicar: ')
        num1_f = float(num1)
        num2_f = float(num2)

        print(f'A multiplicação de {num1_f} * {num2_f} = {num1_f * num2_f}')
        break

    while math == '/':
        num1 = input('Digite o número que vai dividir: ')
        num2 = input('Digite o número que vai dividir: ')
        num1_f = float(num1)
        num2_f = float(num2)

        print(f'A divisão de {num1_f} / {num2_f} = {num1_f / num2_f}')
        break
    
    if math == 's':
        break
    else:
        continue