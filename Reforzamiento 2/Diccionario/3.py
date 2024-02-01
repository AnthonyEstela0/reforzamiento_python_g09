"""3. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor
desalario en consola."""

datos = {"nombre" : "Anthony", "edad" : 28, "salario" : 4200, "antiguedad" : "3 años"}

datos['DNI'] = 75712812

print(datos)

print("\nEl valor del salario es: {}".format(datos["salario"]))