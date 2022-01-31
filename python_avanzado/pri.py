def primalidad(arg1):
    for i in range(2, arg1):
        if arg1 % i == 0:
            print("No es primo. ")
            break
        else:
            if i >= arg1//2:
                print("Si es primo")
                break
 
def run():
    op = int(input("Ingrese un número: "))
    primalidad(op)
 
if __name__ == '__main__':
    run()