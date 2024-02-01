"""8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista vacía."""


def verificar_lista(l):
    if len(l) == 0:
        return "Lista vacía"
    else:
        return "Lista no vacía"


lista_1 = [15, 4, 58, 4, 48, 8]
lista_2 = []

print(verificar_lista(lista_1))
print(verificar_lista(lista_2))