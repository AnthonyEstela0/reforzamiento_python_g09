"""8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario ya creado.
➢ Mostrar en consola los valores de su variable final (ya sea diccionario o lista)."""

datos = {"nombre" : "Anthony", "edad" : 28, "salario" : 4200, "antiguedad" : "3 años"}

datos["carrera"] = "Ing. de Telecomunicaciones"

lista = list(datos.values())

variable_final = lista[4]
print(variable_final)