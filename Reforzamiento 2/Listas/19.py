"""19. Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista."""

lista = []

i = 1
suma = 0
while i <= 10:
    variable = int(input("Ingrese un valor: "))
    lista.append(variable)
    i = i + 1

    suma = suma + variable

promedio = suma/10

print(lista)
print(suma)
print(promedio)