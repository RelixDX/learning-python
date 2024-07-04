# Jogo do pedra, papel e tesoura
import random


def sortear():
    print('Jogo do pedra, papel e tesoura')
    print('Pedra = 0, Papel = 1 e Tesoura = 2')
    jogador = int(input('Escolha: '))
    computador = random.randint(0, 2)
    print(computador)

    if jogador == computador:
        print('Empate!')
    elif jogador == 0 and computador == 2:
        print('Jogador venceu!')
    elif jogador == 1 and computador == 0:
        print('Jogador venceu!')
    elif jogador == 2 and computador == 1:
        print('Jogador venceu!')
    else:
        print('Computador venceu!')


sortear()
