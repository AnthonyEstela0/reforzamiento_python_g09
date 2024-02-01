"""5. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""

datos = {"nombre" : "Anthony", "edad" : 28, "salario" : 4200, "antiguedad" : "3 años"}

datos["DNI"] = 75712812

del datos["edad"]

lista = list(datos)

print(type(lista))