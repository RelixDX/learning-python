"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Boa Noite')
falar_boa_noite = criar_saudacao('Boa Noite')

for nome in ['Lucas', 'Tiago', 'Ana Julia', 'Joaquim']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
