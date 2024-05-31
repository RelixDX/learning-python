# Exercício
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

# def numeros(numero1, numero2, numero3):
#     def duplicar():
#         return numero1 * 2

#     def triplicar():
#         return numero2 * 3

#     def quadruplicar():
#         return numero3 * 4

#     for num in duplicar(), triplicar(), quadruplicar():
#         print(num)


# numeros(2, 3, 4)


def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
