from typing import Callable


def a_mayusculas(func) -> Callable:
    def envoltura(texto: str):
        string: str = str(func(texto).upper())
        print("Convirtiendo a mayusculas ---")
        return string
    return envoltura

# @a_mayusculas
def get_nombre(pregunta: str = "Cual es tu nombre?: "):
    nombre: str = input(pregunta)
    return nombre

get_nombre_mayusculas = a_mayusculas(get_nombre)

estudiante1 = get_nombre_mayusculas("hola?: ")
print(estudiante1)

