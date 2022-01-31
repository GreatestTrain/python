def comprobacion_numero():
    num = random.randint(0, 100)
    # print(num)
    op = -1
    while(op != num):
        op = int(input("Adivina un numero del 1 al 100: "))
        if op == num:
            print("Felicidades! Adivinaste el número.")
            break
        if op > num:
            print("Elige un numero menor.")
        else:
            print("Elige un numero mayor")
        print("Intenta de nuevo.")


def run():
    comprobacion_numero()

if __name__ == '__main__':
    run()