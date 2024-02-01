"""6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista) dentro de la lista."""

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

print("La cantidad de veces que aparece el curso Física: {}".format(nueva_lista.count("Física")))