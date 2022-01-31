from types import NoneType


def decorador(func):
    print('Esto se añade a mi funcion')
    def envoltura(func2):
        def final(palabrasfinales):
            
            print(func)
            func2()
            palabrasfinales()
        return final
    return envoltura

def saludo(string = "hola"):
    print(string)

def despedida():
    print("adios")

def final():
    print("final")

# saludo = decorador(saludo)
# saludo()

# otro_saludo = decorador(despedida)("Dinal")

saludo_final = decorador(saludo)(despedida)(final)