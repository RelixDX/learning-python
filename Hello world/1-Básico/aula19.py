primeiro_valor = input('Primeiro valor: ')
segundo_valor = input('Segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'"{primeiro_valor}" é maior que "{segundo_valor}"')
elif primeiro_valor < segundo_valor:
    print(f'"{segundo_valor}" é maior que "{primeiro_valor}"')
else:
    print(f'{primeiro_valor} e {segundo_valor} são iguais')