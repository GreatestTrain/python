def get_nombre() -> str:
    nombre: str = input("Cual es tu nombre?: ")
    return nombre.upper()

estudiante1 = get_nombre()