class FueraDelRango(Exception):
    message: str = ""
    print(f'{type(message)=}')
    def __init__(self, *args):
        if args:
          self.message = args[0]
        else:
          self.message = "No ingresaste un numero dentro del rango"
    def __str__(self):
        print('Existe un error')
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'
def run():
    try:
        numero: int = int(input("Ingresa un numero entre 6 y 9: "))
        if numero > 9 or numero < 6:
            raise FueraDelRango("Este es un error")
    except ValueError as fdr:
        print("El valor esta fuera de los limites")
run()