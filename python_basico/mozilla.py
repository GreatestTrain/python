#############################################
#           Generador de contraseñas        #
#############################################
import random

mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
caracteres = mayusculas + minusculas + numeros + simbolos

lista = {
}

def generador():
    length = int(input("Elige la longitud de tu contrasena: "))
    contrasena = []
    for i in range(length):
        contrasena.append(random.choice(caracteres))
    return "".join(contrasena)

def crear_contrasena():
    ## crear una contrasena ##
    # nombre de la contrasena = ndc
    ndc = input("Elija el nombre de la contrasena: ")
    lista[ndc] = generador();
    print("Tu nueva contrasena es: ", lista[ndc])

def eliminar_contrasena():
    ## eliminar contrasenas ##
    cadena = input("¿Qué contraseña desea eliminar? (escriba el nombre): ")
    lista.pop(cadena)
    print("Contrasena eliminada.\n")

def lista_contrasena():
    ## imprimir la lista de contrasenas ##
    print("""
#######################################
####### Lista de contrasenas ##########
#######################################
    """)
    for nombre, contrasena in lista.items():
        print(nombre, "\r\t\t|\t", contrasena)

def main():
    op = -1
    while op != 4:
        print("""
########## MENU ################
================================

1. Crear una contraseña
2. Eliminar una contraseña
3. Ver lista de las contraseñas
4. Salir
        """)
        op = int(input("Elige una opcion: "))
        if op == 1:
            crear_contrasena()
        elif op == 2:
            eliminar_contrasena()
        elif op == 3:
            lista_contrasena()
        elif op == 4:
            print("Saliendo del programa ....")
        else:
            print("Ingrese una opcion valida")

if __name__ == '__main__':
    main()
