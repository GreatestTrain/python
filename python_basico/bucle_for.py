def potencia(arg1):
    for i in range(1, arg1+1):
        print(2**i)

def run():
    op = int(input("Ingrese un numero: "))
    potencia(op)

if __name__ == "__main__":
    try:
        run()
    except:
        print("Error.")
