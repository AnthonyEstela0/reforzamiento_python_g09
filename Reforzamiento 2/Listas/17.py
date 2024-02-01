"""17. Crear una lista con los 10 primeros números al cuadrado y mostrar el resultado en
terminal."""

lista = []

i = 1
while i <= 10:
    cuadrado = i * i
    lista.append(cuadrado)
    i = i + 1
print(lista)