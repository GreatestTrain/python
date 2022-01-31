def ciclo(num1):
    for i in range(0,10000000,1):
    # i = 0
    # while(True):
        # i = i + 1
        if 2**i == num1:
            print(f'Se necesitaron {i} intentos')
            break
        elif 2**i > num1:
            print(f'No existe un numero entero de intentos')
            break

def run():
    numero = int(input("Escribe un número: "))
    ciclo(numero)

if __name__ == "__main__" :
    try:
        run()
    except:
        print("error.")
