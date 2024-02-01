"""7. Borra el primer ítem de la lista usando debidamente su índice"""

cursos = ["Calculo", "Física", "Ecuaciones diferenciales", "Programación", "Redes y comunicación de datos", "Comunicaciones ópticas"]

cursos.append("Sistemas radioeléctricos")
cursos.append("Seguridad informática")
cursos.append("Sistemas de comunicación digital")
cursos.append("Sistemas de comunicación satelital")

nueva_lista = cursos

nueva_lista.remove("Sistemas radioeléctricos")
nueva_lista.remove("Seguridad informática")

nueva_lista.reverse()

nueva_lista.append("Física")
nueva_lista.append("Física")
nueva_lista.append("Física")
nueva_lista.append("Física")

nueva_lista.pop(0)

print(nueva_lista)