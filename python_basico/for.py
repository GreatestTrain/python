def contar(arg1):
    i = 0
    for i in range(0,arg1+1):
        print(i)

def run():
    op = int(input("Ingrese un numero: "))
    contar(op)

run()
