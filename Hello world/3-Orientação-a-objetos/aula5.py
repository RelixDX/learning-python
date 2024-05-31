# Atributos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birthday(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Lucas', 20)
p2 = Pessoa('Tiago', 16)
print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1
print(p1.get_birthday())
print(p2.get_birthday())
