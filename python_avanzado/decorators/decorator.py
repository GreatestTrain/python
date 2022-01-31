def decorador(func):
    def envoltura():
        print('Esto se anade a mi funcion original')
        func()
    return envoltura

def saludo():
    print('iHola!')

saludo = decorador(saludo)
saludo()
