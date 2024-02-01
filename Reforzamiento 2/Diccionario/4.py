"""4. Elimina el key edad tipo de tu diccionario, incluyendo su valor."""

datos = {"nombre" : "Anthony", "edad" : 28, "salario" : 4200, "antiguedad" : "3 años"}

datos["DNI"] = 75712812

del datos["edad"]

print(datos)


