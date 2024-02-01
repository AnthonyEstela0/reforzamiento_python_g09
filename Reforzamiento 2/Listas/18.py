"""Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""

lista = []

i = 1
while i <= 29:
    lista.append(i)
    i = i + 2

lista.append(3.0)
lista.append(15.0)
lista.append(21.0)

lista.insert(3, "Anthony")

del(lista[3])

print(lista)