# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birthday(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Lucas', 'idade': 20}
p1 = Pessoa(**dados)
# p1.nome = 'Eita'
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Eita'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)
