def primalidad(arg1: int) -> bool:
    for i in range(2, arg1):
        if arg1 % i == 0:
            return False
            break
        else:
            if i >= arg1//2:
                return True
                break

def run():
    number: int = int(input("Ingrese un número: "))
    print(primalidad(number))

if __name__ == '__main__':
    run()
