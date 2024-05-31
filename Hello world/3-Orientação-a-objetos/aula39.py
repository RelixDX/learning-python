# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields


# @dataclass(init=False)
# @dataclass(frozen=True)
# @dataclass(repr=True, )  # order=True
# class Pessoa:
#     nome: str
#     sobrenome: str

#     # def __init__(self, nome, sobrenome):
#     #     self.nome = nome
#     #     self.sobrenome = sobrenome
#     #     self.nome_completo = f'{self.nome} {self.sobrenome}'

#     # def __post_init__(self):
#     #     self.nome_completo = f'{self.nome} {self.sobrenome}'

#     # @property
#     # def nome_completo(self):
#     #     return f'{self.nome} {self.sobrenome}'

#     # @nome_completo.setter
#     # def nome_completo(self, valor):
#     #     nome, *sobrenome = valor.split()
#     #     self.nome = nome
#     #     self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     # p1 = Pessoa('Lucas', 'Souza')
#     lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X'), ]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.nome)
#     print(ordenadas)
#     # p1.nome = 'Lucas'
#     # p1.nome_completo = 'Lucas Souza de Oliveira'
#     # p2 = Pessoa('Lucas', 20)
#     # print(p1)
#     # print(p1.nome_completo)

# @dataclass
# class Pessoa:
#     nome: str
#     sobrenome: str


# if __name__ == '__main__':
#     p1 = Pessoa('Lucas', 'Souza')
#     print(asdict(p1).keys())
#     print(asdict(p1).values())
#     print(asdict(p1).items())
#     print(astuple(p1)[0])

@dataclass
class Pessoa:
    nome: str = field(default='MISSING', repr=False)
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    print(p1)
