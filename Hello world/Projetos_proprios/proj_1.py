import random

while True:
    secreto = random.randint(1, 100)

    palpite = input('Descubra o número de 1 à 100: ')
    palpite_int = int(palpite)

    try:
        if palpite_int == secreto:
            print(f'Você acertou o número {palpite_int}')
        else:
            print(f'Você errou, o número era {secreto}')
    except:
        print('Digite um número')

    again = input('Deseja jogar novamente? (s/n): ').lower()

    if again == 's':
        continue
    elif again == 'n':
        break
    else:
        print('Digite "S" ou "N"!')