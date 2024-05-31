# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def nao_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÂO está filmando.')
            return

        print(f'{self.nome} parou de filmar.')
        self.filmando = False

    def foto(self):
        if self.filmando:
            print(
                f'Não é possivel tirar foto enquanto {self.nome} está filmando.')
        else:
            print(f'Foto tirada na {self.nome} com sucesso.')


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.foto()
c1.nao_filmar()
c1.nao_filmar()
# print(c1.filmando)
# print(c2.filmando)
# c1.foto()
# c2.foto()
