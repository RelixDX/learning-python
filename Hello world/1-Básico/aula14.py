a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={name1:.2f}'
formato = string.format(
    a,
    b,
    name1=c
)

print(formato)