
"""9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla."""


from math import pow

variable = 5

resultado = pow(variable, 4) - variable * 2
print(resultado)