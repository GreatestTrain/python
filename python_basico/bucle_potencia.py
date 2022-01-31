def potencia(arg1):
    i = 0
    while(i<arg1):
        i += 1
        print(2**i)

def run():
    op = int(input("Ingrese un numero: "))
    potencia(op)

if __name__ == "__main__":
    try:
        run()
    except:
        print("Error.")
