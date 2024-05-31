"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez.
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Lucas'
iterator = iter(texto)

while True:

    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
