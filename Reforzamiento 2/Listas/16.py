"""16. Mostrar sólo los datos comprendidos entre la posición 10 y 35"""

lista = []

i = 1
while i <= 100:
    lista.append(i)
    i = i + 1

nueva_lista = lista[10:35]

print(nueva_lista)