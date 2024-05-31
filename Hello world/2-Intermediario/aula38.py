import importlib
import aula38_m

print(aula38_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula38_m)

print('Fim')
