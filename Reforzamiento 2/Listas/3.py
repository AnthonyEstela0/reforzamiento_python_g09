"""3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice."""

cursos = ["Calculo", "Física", "Ecuaciones diferenciales", "Programación", "Redes y comunicación de datos", "Comunicaciones ópticas"]

cursos.append("Sistemas radioeléctricos")
cursos.append("Seguridad informática")
cursos.append("Sistemas de comunicación digital")
cursos.append("Sistemas de comunicación satelital")

nueva_lista = cursos

nueva_lista.remove("Sistemas radioeléctricos")
nueva_lista.remove("Seguridad informática")

print(nueva_lista)