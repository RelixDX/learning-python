# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # def __str__(self):
    #     return f'({self.x}, {self.y})'

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

# p1 = Ponto(1, 2)
# p2 = Ponto(978, 876)
# print(p1)
# print(repr(p2))
# print(f'{p2!r}')


if __name__ == '__main__':
    m1 = Ponto(4, 2)  # 6
    m2 = Ponto(6, 4)  # 10
    m3 = m1 + m2
    print(m3)
    print('P1 é maior que P2', m1 > m2)
    print('P2 é maior que P1', m2 > m1)
