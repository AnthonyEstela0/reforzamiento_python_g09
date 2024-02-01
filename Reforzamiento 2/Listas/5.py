"""5. Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el resultado en consola. (Pista: len(lista))"""

cursos = ["Calculo", "Física", "Ecuaciones diferenciales", "Programación", "Redes y comunicación de datos", "Comunicaciones ópticas"]

cursos.append("Sistemas radioeléctricos")
cursos.append("Seguridad informática")
cursos.append("Sistemas de comunicación digital")
cursos.append("Sistemas de comunicación satelital")

nueva_lista = cursos

nueva_lista.remove("Sistemas radioeléctricos")
nueva_lista.remove("Seguridad informática")

nueva_lista.reverse()

print("La cantidad de items que tengo son: {}".format(len(nueva_lista)))