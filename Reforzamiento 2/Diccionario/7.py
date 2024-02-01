"""7. Crear un diccionario con 6 departamentos en el país.
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario."""

departamento = {"dep_1": "Arequipa", "dep_2": "Lima", "dep_3": "Cajamarca", "dep_4": "Trujillo", "dep_5": "Ica", "dep_6": "Junin"}

del departamento["dep_3"]

print(departamento)