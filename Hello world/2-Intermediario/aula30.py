# Generator expression, Iterables and Iterators in Python
import sys
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__


lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
